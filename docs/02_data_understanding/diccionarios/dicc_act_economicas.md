
# Diccionario de datos - Catálogo de actividades económicas

## 1. Información general

**Fuente:** Catálogo de actividades económicas

**Sistema de clasificación:** Clasificación Industrial Internacional Uniforme (CIIU)

**Portal:** https://www.datos.gov.co/d/nuke-fusu

**Identificador:** `nuke-fusu`

**Total de variables:** 5

**Origen de las definiciones:** Metadatos publicados por la fuente.

## 2. Objetivo

Documentar las variables disponibles en el Catálogo de actividades económicas, sus tipos de datos y sus significados, para facilitar la interpretación y clasificación de las actividades económicas registradas en las fuentes de ProyectoMercantil.

Este catálogo se considera una fuente de referencia para interpretar los códigos de actividad económica, especialmente los registrados en RUES.

## 3. Diccionario de variables

| N.º | Variable | Tipo | Descripción |
|---:|---|---|---|
| 1 | `id` | number | C2 Identificador único del registro |
| 2 | `code` | text | Código de la actividad código CIIU |
| 3 | `description` | text | Descripción de la actividad económica |
| 4 | `status` | number | Estado de la version 1 activo 0 inactivo |
| 5 | `version` | number | Versión del catálogo publicado |

## 4. Observaciones técnicas

- La variable `id` está declarada como tipo `number` e identifica los registros del catálogo.
- La variable `code` contiene el código CIIU asociado a una actividad económica.
- La variable `description` contiene la descripción de la actividad económica.
- La variable `status` representa el estado de la versión, donde `1` corresponde a activo y `0` a inactivo, según los metadatos.
- La variable `version` identifica la versión del catálogo publicado.
- El catálogo no contiene variables de fecha ni campos de ubicación territorial.
- Se deberá comprobar la compatibilidad entre los códigos de este catálogo y los registrados en RUES.
- También será necesario verificar si un mismo código aparece en diferentes versiones del catálogo.

## 5. Relación potencial con RUES

La fuente RUES contiene las siguientes variables:

- `cod_ciiu_act_econ_pri`: actividad económica principal.
- `cod_ciiu_act_econ_sec`: actividad económica secundaria.
- `ciiu3`: otra actividad económica.
- `ciiu4`: otra actividad económica adicional.

Estas variables podrían relacionarse con `code` del catálogo para obtener la descripción de las actividades económicas.

La relación deberá validarse antes de implementarse, considerando las versiones de clasificación y los formatos de los códigos.

## 6. Estado del diccionario

**Estado:** Documentación inicial completada.

**Variables identificadas:** 5 de 5.

**Pendiente:** Validar las versiones disponibles, la unicidad de los códigos, sus estados y su compatibilidad con RUES durante la exploración de datos.
