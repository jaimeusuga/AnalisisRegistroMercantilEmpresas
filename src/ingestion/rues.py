
# ============================================================
# 01. MÓDULO DE INGESTA RUES - CAPA BRONZE
# ============================================================
# Objetivo:
# Descargar registros mercantiles por año y mes mediante
# lotes paginados y almacenarlos en archivos Parquet.
#
# Descripción:
# Consulta la API Socrata, filtra fecha_matricula en formato
# AAAAMMDD, valida los registros y publica los archivos
# en carpetas mensuales particionadas por año y mes.
# ============================================================

from datetime import datetime, timezone
from pathlib import Path
from calendar import monthrange
import logging
import shutil
import uuid

import pandas as pd
import requests

from src.ingestion.socrata import consultar_api


logger = logging.getLogger(__name__)

# ============================================================
# 03. GENERACIÓN DEL FILTRO MENSUAL
# ============================================================
# Objetivo:
# Construir intervalos mensuales para fecha_matricula.
#
# Descripción:
# La fuente almacena las fechas como texto AAAAMMDD.
# Se utiliza un límite superior exclusivo.
# ============================================================

def construir_filtro(anio, mes):

    inicio = f"{anio}{mes:02d}01"

    if mes == 12:
        fin = f"{anio + 1}0101"
    else:
        fin = f"{anio}{mes + 1:02d}01"

    return (
        f"fecha_matricula >= '{inicio}' "
        f"AND fecha_matricula < '{fin}'"
    )


# ============================================================
# 04. INGESTA MENSUAL POR LOTES
# ============================================================
# Objetivo:
# Descargar y almacenar todos los registros de un mes.
#
# Descripción:
# Utiliza paginación estable por identificador Socrata.
# Descarga primero a una carpeta temporal y solo publica
# el resultado cuando termina la extracción.
# ============================================================

def ingestar_rues_mes(
    config: dict,
    project_root: Path,
    anio: int,
    mes: int
) -> dict:

    if not 1 <= anio <= 9999:
        raise ValueError("El año debe estar entre 1 y 9999.")

    if not 1 <= mes <= 12:
        raise ValueError("El mes debe estar entre 1 y 12.")

    cfg = config["ingestion"]["rues"]

    tamano_lote = int(cfg["page_size"])
    if tamano_lote <= 0:
        raise ValueError("page_size debe ser mayor que cero.")

    url = config["sources"]["rues"]["url"]
    compresion = config["storage"]["compression"]

    ruta_bronze = (
        Path(project_root)
        / config["paths"]["bronze"]
        / "rues"
    )

    destino = (
        ruta_bronze
        / f"anio={anio}"
        / f"mes={mes:02d}"
    )

    filtro = construir_filtro(anio, mes)

    staging_root = ruta_bronze / "_staging"
    staging_root.mkdir(parents=True, exist_ok=True)

    temporal = (
        staging_root
        / f"{anio}_{mes:02d}_{uuid.uuid4().hex}"
    )

    temporal.mkdir(parents=True, exist_ok=False)

    total = 0
    numero_lote = 0
    fecha_carga = datetime.now(timezone.utc).isoformat()

    try:
        with requests.Session() as session:

            # Obtener el conteo inicial del período.
            respuesta_conteo = consultar_api(
                session,
                url,
                {
                    "$select": "count(*) AS total",
                    "$where": filtro
                }
            )

            esperado = int(respuesta_conteo[0]["total"])

            logger.info(
                "RUES %s-%02d | Esperados: %s",
                anio, mes, esperado
            )

            while total < esperado:

                registros = consultar_api(
                    session,
                    url,
                    {
                        "$where": filtro,
                        "$order": ":id ASC",
                        "$limit": tamano_lote,
                        "$offset": total
                    }
                )

                if not registros:
                    raise RuntimeError(
                        "La API devolvió un lote vacío "
                        "antes de completar la descarga."
                    )

                df = pd.DataFrame(registros)

                # Metadatos técnicos de la capa Bronze.
                df["_bronze_ingested_at"] = fecha_carga
                df["_bronze_source"] = "rues"

                numero_lote += 1

                archivo = (
                    temporal
                    / f"lote_{numero_lote:05d}.parquet"
                )

                df.to_parquet(
                    archivo,
                    engine="pyarrow",
                    compression=compresion,
                    index=False
                )

                total += len(df)

                logger.info(
                    "RUES %s-%02d | Lote %s | %s/%s",
                    anio, mes, numero_lote,
                    total, esperado
                )

            if total != esperado:
                raise RuntimeError(
                    f"Conteo inconsistente: "
                    f"{total} descargados, "
                    f"{esperado} esperados."
                )

        # Publicar los archivos en la carpeta del mes.
        # Se conserva un respaldo de los datos anteriores.
        respaldo = (
            staging_root
            / f"backup_{anio}_{mes:02d}_{uuid.uuid4().hex}"
        )

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
            "ruta": str(destino)
        }

    except Exception:
        logger.exception(
            "Falló la ingesta RUES %s-%02d",
            anio, mes
        )

        if temporal.exists():
            shutil.rmtree(temporal)

        raise
