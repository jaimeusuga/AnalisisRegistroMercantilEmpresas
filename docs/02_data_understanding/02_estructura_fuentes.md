
# ProyectoMercantil

## Fase 2. Comprensión de los datos

### Actividad 2. Exploración de metadatos y estructura

## 1. Propósito

Identificar la estructura de las fuentes de datos,
sus columnas, tipos y variables relevantes.

## 2. Procedimiento

Los metadatos se consultaron mediante la API
de metadatos de datos.gov.co, utilizando Python
y la librería requests.

Notebook:
notebooks/01_data_understanding/01_exploracion_metadatos.ipynb


## 3. Fuentes analizadas

| Fuente | ID | Nombre oficial | Columnas |
|---|---|---|---:|
| RUES | c82u-588k | Personas Naturales, Personas Jurídicas y Entidades Sin Animo de Lucro | 36 |
| TRM | mcec-87by | Tasa de Cambio Representativa del Mercado -Historico | 4 |
| Catálogo de actividades económicas | nuke-fusu | Catálogo de actividades económicas | 5 |
| SECOP II | jbjy-vk9h | SECOP II - Contratos Electrónicos | 95 |



## 4. Variables relevantes

### 4.1. RUES

- matricula
- razon_social
- cod_ciiu_act_econ_pri
- estado_matricula
- fecha_matricula
- ultimo_ano_renovado
- camara_comercio

### 4.2. TRM

- valor
- vigenciadesde
- vigenciahasta

### 4.3. Catálogo de actividades económicas

- code
- description
- status
- version

### 4.4. SECOP II

- id_contrato
- departamento
- sector
- fecha_de_firma
- valor_del_contrato
- proveedor_adjudicado
- documento_proveedor
- codigo_de_categoria_principal

## 5. Observaciones iniciales

- La fuente RUES dispone de códigos CIIU para
  clasificar actividades económicas.
- La TRM contiene fechas de vigencia y valores
  numéricos.
- El catálogo contiene códigos y descripciones
  de actividades económicas.
- SECOP II contiene información territorial,
  contractual y económica.
- No se ha comprobado todavía la compatibilidad
  entre los códigos de RUES y el catálogo.
- La fuente RUES no presenta una columna
  departamental explícita entre las consultadas.
- Los tipos de datos observados corresponden
  a los metadatos declarados por las fuentes.

## 6. Estado

Metadatos estructurales de las cuatro fuentes
consultados correctamente.

Variables candidatas identificadas.

Pendiente de evaluar cobertura territorial,
temporal y compatibilidad entre fuentes.
