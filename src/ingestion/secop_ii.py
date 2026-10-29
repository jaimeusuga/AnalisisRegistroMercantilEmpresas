"""Ingesta mensual de contratos SECOP II a la capa Bronze."""

from datetime import datetime, timezone
from pathlib import Path
import logging
import shutil
import uuid

import pandas as pd
import requests

from src.ingestion.socrata import consultar_api


logger = logging.getLogger(__name__)


def construir_filtro(anio: int, mes: int) -> str:
    """Construye el filtro mensual exclusivo de fecha_de_firma."""
    inicio = f"{anio}-{mes:02d}-01"
    if mes == 12:
        fin = f"{anio + 1}-01-01"
    else:
        fin = f"{anio}-{mes + 1:02d}-01"

    return (
        f"fecha_de_firma >= '{inicio}' "
        f"AND fecha_de_firma < '{fin}'"
    )


def ingestar_secop_ii_mes(
    config: dict,
    project_root: Path,
    anio: int,
    mes: int
) -> dict:
    """Descarga el mes de SECOP II y lo publica en archivos Parquet."""
    if not 1 <= anio <= 9999:
        raise ValueError("El año debe estar entre 1 y 9999.")
    if not 1 <= mes <= 12:
        raise ValueError("El mes debe estar entre 1 y 12.")

    cfg = config["ingestion"]["secop_ii"]
    tamano_lote = int(cfg["page_size"])
    if tamano_lote <= 0:
        raise ValueError("page_size debe ser mayor que cero.")

    url = config["sources"]["secop_ii"]["url"]
    compresion = config["storage"]["compression"]
    ruta_bronze = (
        Path(project_root)
        / config["paths"]["bronze"]
        / "secop_ii"
    )
    destino = (
        ruta_bronze
        / f"anio={anio}"
        / f"mes={mes:02d}"
    )
    filtro = construir_filtro(anio, mes)
    staging_root = ruta_bronze / "_staging"
    staging_root.mkdir(parents=True, exist_ok=True)
    temporal = staging_root / f"{anio}_{mes:02d}_{uuid.uuid4().hex}"
    temporal.mkdir(parents=True, exist_ok=False)

    total = 0
    numero_lote = 0
    fecha_carga = datetime.now(timezone.utc).isoformat()

    try:
        with requests.Session() as session:
            respuesta_conteo = consultar_api(
                session,
                url,
                {
                    "$select": "count(*) AS total",
                    "$where": filtro,
                }
            )
            if not respuesta_conteo or "total" not in respuesta_conteo[0]:
                raise ValueError(
                    "La API SECOP II no devolvió el conteo esperado."
                )

            esperado = int(respuesta_conteo[0]["total"])
            logger.info(
                "SECOP II %s-%02d | Esperados: %s",
                anio, mes, esperado
            )

            while total < esperado:
                limite = min(tamano_lote, esperado - total)
                registros = consultar_api(
                    session,
                    url,
                    {
                        "$where": filtro,
                        "$order": ":id ASC",
                        "$limit": limite,
                        "$offset": total,
                    }
                )
                if not registros:
                    raise RuntimeError(
                        "La API devolvió un lote vacío antes de "
                        "completar la descarga."
                    )

                df = pd.DataFrame(registros)
                df["_bronze_ingested_at"] = fecha_carga
                df["_bronze_source"] = "secop_ii"
                numero_lote += 1
                df.to_parquet(
                    temporal / f"lote_{numero_lote:05d}.parquet",
                    engine="pyarrow",
                    compression=compresion,
                    index=False
                )
                total += len(df)
                logger.info(
                    "SECOP II %s-%02d | Lote %s | %s/%s",
                    anio, mes, numero_lote, total, esperado
                )

            if total != esperado:
                raise RuntimeError(
                    f"Conteo inconsistente: {total} descargados, "
                    f"{esperado} esperados."
                )

        respaldo = staging_root / f"backup_{anio}_{mes:02d}_{uuid.uuid4().hex}"
        destino.parent.mkdir(parents=True, exist_ok=True)
        if destino.exists():
            destino.rename(respaldo)

        try:
            temporal.rename(destino)
        except Exception:
            if respaldo.exists():
                respaldo.rename(destino)
            raise

        if respaldo.exists():
            shutil.rmtree(respaldo)

        return {
            "anio": anio,
            "mes": mes,
            "registros": total,
            "lotes": numero_lote,
            "estado": "COMPLETADO",
            "ruta": str(destino),
        }

    except Exception:
        logger.exception("Falló la ingesta SECOP II %s-%02d", anio, mes)
        if temporal.exists():
            shutil.rmtree(temporal)
        raise
