
# Cobertura temporal y territorial de las fuentes

## 1. Objetivo

Verificar los periodos y ámbitos geográficos
representados en las fuentes de ProyectoMercantil,
para determinar su utilidad en el análisis
empresarial y de contratación pública en Colombia.

## 2. Metodología

Se consultaron las API públicas de datos.gov.co
mediante Python y la librería requests.

Para las fuentes con campos de fecha se utilizaron
consultas agregadas que permiten identificar
las fechas mínima y máxima sin descargar
todos los registros.

## 3. Cobertura temporal

| Fuente | Fecha inicial | Fecha final | Estado |
|---|---|---|---|
| RUES | Pendiente | Pendiente | Requiere validar fechas almacenadas como texto |
| TRM | Pendiente | Pendiente | Consulta realizada |
| Catálogo económico | No aplica directamente | No aplica directamente | Revisar versiones |
| SECOP II | Pendiente | Pendiente | Consulta realizada |

### Observaciones

- Las fechas extremas permiten identificar
  el intervalo disponible en cada fuente.
- No garantizan continuidad ni completitud
  de los registros dentro del intervalo.
- La selección definitiva del periodo de análisis
  requiere verificar la disponibilidad por año.

## 4. Cobertura territorial

| Fuente | Campo territorial | Alcance identificado |
|---|---|---|
| RUES | camara_comercio | Pendiente de validar |
| TRM | No aplica | Nacional |
| Catálogo económico | No aplica | Clasificación de actividades |
| SECOP II | departamento | Pendiente de validar |

### Observaciones

- RUES identifica cámaras de comercio, pero
  estas no equivalen necesariamente a departamentos.
- SECOP II contiene un campo departamental;
  debe verificarse qué ubicación representa.
- La TRM es un indicador nacional.
- El catálogo económico no contiene registros
  territoriales de empresas.

## 5. Evaluación preliminar

El proyecto contempla analizar preferentemente
los dos años completos más recientes y realizar
comparaciones departamentales.

La viabilidad de estas condiciones dependerá
de la cobertura efectiva de RUES y SECOP II.

## 6. Pendientes

- Registrar las fechas obtenidas para TRM y SECOP II.
- Verificar la cobertura temporal de RUES.
- Examinar las versiones del catálogo económico.
- Comprobar registros por año.
- Verificar los territorios representados.
- Determinar el periodo y alcance geográfico
  definitivo del análisis.

## 7. Estado

Actividad en desarrollo.
Cobertura temporal parcialmente consultada.
Cobertura territorial pendiente de verificación.
