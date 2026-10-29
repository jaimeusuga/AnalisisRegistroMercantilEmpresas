
# ProyectoMercantil

## Fase 1. Comprensión del negocio

### Actividad 6. Recursos, requisitos y riesgos

## 1. Propósito

Identificar los recursos disponibles, los requisitos
necesarios y los riesgos potenciales del proyecto,
con el fin de evaluar su viabilidad operativa.

## 2. Recursos disponibles

### 2.1 Infraestructura

- Equipo personal con 24 GB de memoria RAM.
- Sistema operativo Windows.
- Almacenamiento local.
- Conexión a Internet.

### 2.2 Herramientas de desarrollo

- Visual Studio Code.
- Python.
- Git y GitHub.
- Entorno virtual de Python.

### 2.3 Herramientas analíticas previstas

- Pandas: exploración y transformación.
- DuckDB: consultas SQL y procesamiento.
- Parquet: almacenamiento eficiente.
- Jupyter: desarrollo de análisis.
- Matplotlib y Seaborn: visualizaciones.
- Power BI: presentación de resultados.

La instalación y configuración de las herramientas
se verificará cuando corresponda utilizarlas.

### 2.4 Fuentes de información

Se utilizarán inicialmente cuatro conjuntos
de datos abiertos de Colombia:

- c82u-588k: RUES.
- mcec-87by: TRM.
- nuke-fusu: pendiente de caracterización.
- jbjy-vk9h: SECOP II.

La estructura, disponibilidad y pertinencia
de las fuentes se verificará durante la fase 2.

## 3. Requisitos del proyecto

### 3.1 Requisitos funcionales

RF01. Obtener datos de las fuentes seleccionadas.

RF02. Explorar su estructura y contenido.

RF03. Identificar problemas de calidad.

RF04. Limpiar y transformar los registros.

RF05. Construir indicadores empresariales
y de contratación pública.

RF06. Realizar comparaciones departamentales.

RF07. Generar visualizaciones e informes.

### 3.2 Requisitos técnicos

RT01. Utilizar un entorno virtual de Python.

RT02. Mantener las dependencias documentadas.

RT03. Conservar los datos originales.

RT04. Organizar los datos procesados por capas.

RT05. Mantener código reutilizable y documentado.

RT06. Utilizar Git para el control de versiones.

RT07. Permitir la reproducción de los análisis.

### 3.3 Requisitos de calidad

RC01. Documentar la procedencia de los datos.

RC02. Identificar valores faltantes y duplicados.

RC03. Validar tipos de datos y campos relevantes.

RC04. Documentar las transformaciones realizadas.

RC05. Verificar la consistencia de los indicadores.

RC06. Registrar las limitaciones identificadas.

## 4. Riesgos del proyecto

| Código | Riesgo | Impacto | Prevención |
|---|---|---|---|
| R01 | Cambios en las API | Alto | Documentar endpoints |
| R02 | Volumen elevado | Medio | DuckDB y Parquet |
| R03 | Datos incompletos | Alto | Controles de calidad |
| R04 | Fuentes incompatibles | Alto | Validar identificadores |
| R05 | Periodos diferentes | Alto | Verificar cobertura |
| R06 | Pérdida de trabajo | Medio | Git y respaldos |
| R07 | Complejidad excesiva | Medio | Desarrollo gradual |

Los impactos son estimaciones iniciales
y podrán revisarse durante el proyecto.

## 5. Estrategia de trabajo

- Implementar las actividades progresivamente.
- Verificar cada procedimiento antes de continuar.
- Evitar tecnologías que no aporten valor.
- Mantener documentación actualizada.
- Registrar cambios relevantes en Git.
- Revisar los riesgos cuando sea necesario.

## 6. Estado

Recursos y requisitos identificados.

Riesgos iniciales documentados.

Viabilidad operativa preliminar, pendiente
de comprobaciones técnicas y de datos.
