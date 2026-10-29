
# Diccionario de datos - TRM

## 1. Información general

**Fuente:** Tasa de Cambio Representativa del Mercado -Historico

**Sistema:** Tasa Representativa del Mercado (TRM)

**Portal:** https://www.datos.gov.co/d/mcec-87by

**Identificador:** `mcec-87by`

**Total de variables:** 4

**Origen de las definiciones:** Metadatos publicados por la fuente.

## 2. Objetivo

Documentar las variables disponibles en la fuente TRM, sus tipos de datos y sus significados, para facilitar la comprensión, exploración y utilización de la información sobre la tasa de cambio del peso colombiano frente al dólar estadounidense durante el desarrollo de ProyectoMercantil.

## 3. Diccionario de variables

| N.º | Variable | Tipo | Descripción |
|---:|---|---|---|
| 1 | `valor` | number | Valor numérico con la tasa de cambio del peso colombiano frente al dolar |
| 2 | `unidad` | text | Representación de la divisa según la norma ISO 4217 |
| 3 | `vigenciadesde` | calendar_date | Fecha de inicio de la vigencia de la tasa representativa del mercado |
| 4 | `vigenciahasta` | calendar_date | Fecha de finalización de la vigencia de la tasa representativa del mercado |

## 4. Observaciones técnicas

- La variable `valor` está declarada como tipo `number` y contiene el valor numérico de la tasa de cambio.
- La variable `unidad` está declarada como tipo `text` y permite identificar la divisa según la norma ISO 4217.
- Las variables `vigenciadesde` y `vigenciahasta` están declaradas como `calendar_date`.
- Los campos de vigencia permitirán analizar la evolución temporal de la TRM.
- Será necesario verificar la continuidad de las fechas, la presencia de valores nulos y la existencia de posibles registros duplicados.
- La TRM es un indicador de alcance nacional y no dispone de una desagregación departamental en esta fuente.

## 5. Estado del diccionario

**Estado:** Documentación inicial completada.

**Variables identificadas:** 4 de 4.

**Pendiente:** Validar los valores reales, la cobertura temporal, la continuidad de los registros y su calidad durante la exploración de datos.
