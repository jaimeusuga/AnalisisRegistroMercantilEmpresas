
# ============================================================
# 01. CONTROL DE CALIDAD RUES - CAPA BRONZE
# ============================================================
# Objetivo:
# Validar automáticamente cada partición mensual de RUES.
#
# Descripción:
# Utiliza DuckDB para comprobar cantidad de registros,
# fechas, duplicados exactos y número de archivos Parquet.
# No modifica ni elimina los datos originales.
# ============================================================

from pathlib import Path

import duckdb


def validar_rues_mes(
    project_root: Path,
    anio: int,
    mes: int,
    registros_esperados: int | None = None
) -> dict:
    """Valida los archivos Parquet de un mes de RUES."""

    if not 1 <= mes <= 12:
        raise ValueError("El mes debe estar entre 1 y 12.")

    ruta_mes = (
        Path(project_root)
        / "data"
        / "bronze"
        / "rues"
        / f"anio={anio}"
        / f"mes={mes:02d}"
    )

    archivos = sorted(ruta_mes.glob("*.parquet"))

    if not archivos:
        return {
            "periodo": f"{anio}-{mes:02d}",
            "registros": 0,
            "archivos": 0,
            "duplicados_exactos": None,
            "fuera_periodo": None,
            "fechas_nulas": None,
            "estado": "SIN_DATOS"
        }

    fecha_inicio = f"{anio}{mes:02d}01"

    if mes == 12:
        fecha_fin = f"{anio + 1}0101"
    else:
        fecha_fin = f"{anio}{mes + 1:02d}01"

    ruta_parquet = str(ruta_mes / "*.parquet")

    with duckdb.connect() as con:

        # Consultar únicamente las columnas físicas de origen.
        columnas = con.execute(
            """
            DESCRIBE SELECT *
            FROM read_parquet(
                ?,
                hive_partitioning = false,
                union_by_name = true
            )
            """,
            [ruta_parquet]
        ).df()["column_name"].tolist()

        columnas_origen = [
            columna for columna in columnas
            if not columna.startswith("_bronze_")
        ]

        if "fecha_matricula" not in columnas_origen:
            raise ValueError(
                "No existe fecha_matricula en los Parquet."
            )

        # Construcción segura de identificadores SQL.
        columnas_sql = ", ".join(
            '"' + columna.replace('"', '""') + '"'
            for columna in columnas_origen
        )

        resumen = con.execute(
            f"""
            WITH origen AS (
                SELECT {columnas_sql}
                FROM read_parquet(
                    ?,
                    hive_partitioning = false,
                    union_by_name = true
                )
            ),
            unicos AS (
                SELECT DISTINCT *
                FROM origen
            )
            SELECT
                (SELECT COUNT(*) FROM origen)
                    AS registros,

                (SELECT COUNT(*) FROM unicos)
                    AS registros_unicos,

                (
                    SELECT COUNT(*)
                    FROM origen
                    WHERE fecha_matricula IS NULL
                ) AS fechas_nulas,

                (
                    SELECT COUNT(*)
                    FROM origen
                    WHERE fecha_matricula IS NOT NULL
                      AND (
                          fecha_matricula < ?
                          OR fecha_matricula >= ?
                      )
                ) AS fuera_periodo
            """,
            [ruta_parquet, fecha_inicio, fecha_fin]
        ).fetchone()

    total, unicos, nulos, fuera = map(int, resumen)
    duplicados = total - unicos

    controles = {
        "sin_duplicados_exactos": duplicados == 0,
        "sin_fechas_nulas": nulos == 0,
        "fechas_en_periodo": fuera == 0,
        "conteo_esperado": (
            registros_esperados is None
            or total == registros_esperados
        )
    }

    estado = (
        "APROBADO"
        if all(controles.values())
        else "REVISAR"
    )

    return {
        "periodo": f"{anio}-{mes:02d}",
        "registros": total,
        "archivos": len(archivos),
        "duplicados_exactos": duplicados,
        "fuera_periodo": fuera,
        "fechas_nulas": nulos,
        "estado": estado,
        "controles": controles
    }
