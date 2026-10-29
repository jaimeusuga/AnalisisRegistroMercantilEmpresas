"""Validaciones de calidad SECOP II para una partición mensual Bronze."""

from pathlib import Path

import duckdb


def validar_secop_ii_mes(
    project_root: Path,
    anio: int,
    mes: int,
    registros_esperados: int | None = None,
) -> dict:
    """Valida conteos, IDs, fechas y duplicados exactos de un mes."""
    if not 1 <= anio <= 9999:
        raise ValueError("El año debe estar entre 1 y 9999.")
    if not 1 <= mes <= 12:
        raise ValueError("El mes debe estar entre 1 y 12.")

    ruta_mes = (
        Path(project_root)
        / "data"
        / "bronze"
        / "secop_ii"
        / f"anio={anio}"
        / f"mes={mes:02d}"
    )
    archivos = sorted(ruta_mes.glob("*.parquet"))
    if not archivos:
        return {
            "periodo": f"{anio}-{mes:02d}",
            "registros": 0,
            "contratos_unicos": 0,
            "ids_contrato_nulos": None,
            "duplicados_exactos": None,
            "fechas_nulas": None,
            "fuera_periodo": None,
            "archivos": 0,
            "estado": "SIN_DATOS",
        }

    fecha_inicio = f"{anio}-{mes:02d}-01"
    fecha_fin = (
        f"{anio + 1}-01-01"
        if mes == 12
        else f"{anio}-{mes + 1:02d}-01"
    )
    rutas = [str(archivo) for archivo in archivos]

    with duckdb.connect() as con:
        columnas = con.execute(
            """
            DESCRIBE SELECT *
            FROM read_parquet(?, union_by_name = true)
            """,
            [rutas],
        ).df()["column_name"].tolist()
        columnas_origen = [
            columna for columna in columnas
            if not columna.startswith("_bronze_")
        ]
        if "fecha_de_firma" not in columnas_origen:
            raise ValueError("No existe fecha_de_firma en los Parquet.")
        if "id_contrato" not in columnas_origen:
            raise ValueError("No existe id_contrato en los Parquet.")

        columnas_sql = ", ".join(
            '"' + columna.replace('"', '""') + '"'
            for columna in columnas_origen
        )
        resumen = con.execute(
            f"""
            WITH origen AS (
                SELECT {columnas_sql}
                FROM read_parquet(?, union_by_name = true)
            ),
            unicos AS (
                SELECT DISTINCT * FROM origen
            )
            SELECT
                (SELECT COUNT(*) FROM origen) AS registros,
                (SELECT COUNT(DISTINCT id_contrato) FROM origen)
                    AS contratos_unicos,
                (
                    SELECT COUNT(*)
                    FROM origen
                    WHERE id_contrato IS NULL OR trim(id_contrato) = ''
                ) AS ids_contrato_nulos,
                (
                    SELECT COUNT(*)
                    FROM origen
                    WHERE fecha_de_firma IS NULL
                ) AS fechas_nulas,
                (
                    SELECT COUNT(*)
                    FROM origen
                    WHERE fecha_de_firma IS NOT NULL
                      AND (
                          fecha_de_firma < ?
                          OR fecha_de_firma >= ?
                      )
                ) AS fuera_periodo,
                (
                    SELECT COUNT(*) FROM origen
                ) - (
                    SELECT COUNT(*) FROM unicos
                ) AS duplicados_exactos
            """,
            [rutas, fecha_inicio, fecha_fin],
        ).fetchone()

    total, ids, ids_nulos, fechas_nulas, fuera, duplicados = map(
        int, resumen
    )
    controles = {
        "conteo_esperado": (
            registros_esperados is None or total == registros_esperados
        ),
        "sin_ids_contrato_nulos": ids_nulos == 0,
        "sin_fechas_nulas": fechas_nulas == 0,
        "fechas_en_periodo": fuera == 0,
        "sin_duplicados_exactos": duplicados == 0,
    }

    return {
        "periodo": f"{anio}-{mes:02d}",
        "registros": total,
        "contratos_unicos": ids,
        "ids_contrato_nulos": ids_nulos,
        "duplicados_exactos": duplicados,
        "fechas_nulas": fechas_nulas,
        "fuera_periodo": fuera,
        "archivos": len(archivos),
        "estado": "APROBADO" if all(controles.values()) else "REVISAR",
        "controles": controles,
    }
