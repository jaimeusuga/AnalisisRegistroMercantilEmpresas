
# Diccionario de datos - RUES

## 1. Información general

**Fuente:** Personas Naturales, Personas Jurídicas y Entidades Sin Animo de Lucro

**Sistema:** Registro Único Empresarial y Social (RUES)

**Entidad responsable:** Confecámaras

**Portal:** https://www.datos.gov.co/d/c82u-588k

**Identificador:** `c82u-588k`

**Total de variables:** 36

**Origen de las definiciones:** Metadatos publicados por la fuente.

## 2. Objetivo

Documentar las variables disponibles en la fuente RUES, sus tipos de datos y sus significados, para facilitar la comprensión, exploración y selección de información durante el desarrollo de ProyectoMercantil.

## 3. Diccionario de variables

| N.º | Variable | Tipo | Descripción |
|---:|---|---|---|
| 1 | `codigo_camara` | text | Código de la Cámara de comercio que realiza la actualización de datos. |
| 2 | `camara_comercio` | text | Cámara de comercio que realiza la actualización de datos. |
| 3 | `matricula` | text | Número de Matricula Mercantil |
| 4 | `inscripcion_proponente` | text | Número de Inscripción en el registro de Proponentes |
| 5 | `razon_social` | text | Razón Social |
| 6 | `primer_apellido` | text | Primer Apellido |
| 7 | `segundo_apellido` | text | Segundo Apellido, otros apellidos |
| 8 | `primer_nombre` | text | Primer Nombre |
| 9 | `segundo_nombre` | text | Segundo Nombre u otros nombres |
| 10 | `sigla` | text | Sigla |
| 11 | `codigo_clase_identificacion` | text | Código Clase Identificación |
| 12 | `clase_identificacion` | text | Clase Identificación |
| 13 | `numero_identificacion` | text | Número de Identificación |
| 14 | `nit` | text | Número de Identificación Tributario |
| 15 | `digito_verificacion` | text | Digito de Verificación |
| 16 | `cod_ciiu_act_econ_pri` | text | Código CIIU actividad económica principal |
| 17 | `cod_ciiu_act_econ_sec` | text | Código CIIU actividad económica secundaria |
| 18 | `ciiu3` | text | Código actividad económica otras 1 |
| 19 | `ciiu4` | text | Código actividad económica otras 2 |
| 20 | `fecha_matricula` | text | Fecha Matricula |
| 21 | `fecha_renovacion` | text | Fecha de ultima renovación |
| 22 | `ultimo_ano_renovado` | text | Ultimo Año Renovado |
| 23 | `fecha_vigencia` | text | Fecha Vigencia |
| 24 | `fecha_cancelacion` | text | Fecha Cancelación |
| 25 | `codigo_tipo_sociedad` | text | Código Tipo sociedad |
| 26 | `tipo_sociedad` | text | Tipo sociedad |
| 27 | `codigo_organizacion_juridica` | text | Código Organización Jurídica |
| 28 | `organizacion_juridica` | text | Organización Jurídica |
| 29 | `codigo_categoria_matricula` | text | Código Categoría Matricula |
| 30 | `categoria_matricula` | text | Categoría Matricula |
| 31 | `codigo_estado_matricula` | text | Código Estado Matricula |
| 32 | `estado_matricula` | text | Estado Matricula |
| 33 | `clase_identificacion_rl` | text | Clase de identificación del representante legal de la empresa |
| 34 | `num_identificacion_representante_legal` | text | Numero de identificación del representante legal de la empresa |
| 35 | `representante_legal` | text | Nombre del representante legal de la empresa |
| 36 | `fecha_actualizacion` | text | Fecha Ultima Actualización de datos al RUES |

## 4. Observaciones técnicas

- Las 36 variables están declaradas como tipo `text` en los metadatos de la API.
- Los campos de fecha requerirán validación de formato antes de convertirse a tipos de fecha.
- Los códigos CIIU deberán contrastarse con el catálogo de actividades económicas.
- Las variables `codigo_camara` y `camara_comercio` identifican la cámara que actualiza los datos, no necesariamente el departamento donde opera la empresa.
- Las variables de identificación personal y del representante legal requieren un tratamiento cuidadoso para evitar exposiciones innecesarias.

## 5. Estado del diccionario

**Estado:** Documentación inicial completada.

**Variables identificadas:** 36 de 36.

**Pendiente:** Validar formatos reales, valores nulos, consistencia y utilidad analítica durante la exploración de registros.
