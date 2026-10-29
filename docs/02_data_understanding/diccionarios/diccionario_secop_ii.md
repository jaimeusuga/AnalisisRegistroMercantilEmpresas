# Diccionario de datos - SECOP II

## 1. Información general

**Fuente:** SECOP II - Contratos Electrónicos  
**Sistema:** Sistema Electrónico para la Contratación Pública (SECOP II)  
**Entidad responsable:** Agencia Nacional de Contratación Pública - Colombia Compra Eficiente  
**Portal:** https://www.datos.gov.co/d/jbjy-vk9h  
**Identificador:** `jbjy-vk9h`  
**Total de variables:** 95  
**Origen de las definiciones:** Descripciones de los metadatos consultados de la fuente.

## 2. Objetivo

Documentar las variables disponibles en SECOP II, sus tipos de datos declarados y sus significados para facilitar la exploración y el análisis de la contratación pública en ProyectoMercantil.

## 3. Diccionario de variables

| N.º | Variable | Tipo | Descripción |
|---:|---|---|---|
| 1 | `nombre_entidad` | text | Nombre de la entidad del estado que publica el contrato |
| 2 | `nit_entidad` | number | NIT de la entidad del estado que publica el contrato |
| 3 | `departamento` | text | Departamento en el cual se registró la entidad del estado que publica el contrato |
| 4 | `ciudad` | text | Ciudad en el cual se registró la entidad del estado que publica el contrato |
| 5 | `localizaci_n` | text | Ubicación completa de la entidad del estado que publica el contrato |
| 6 | `orden` | text | Orden entidad del estado que publica el contrato |
| 7 | `sector` | text | Sector entidad del estado que publica el contrato |
| 8 | `rama` | text | Rama del estado de la entidad que publica el contrato |
| 9 | `entidad_centralizada` | text | Define si la entidad es descentralizada o centralizada |
| 10 | `proceso_de_compra` | text | Identificador del proceso de compra publicado |
| 11 | `id_contrato` | text | Identificador del contrato firmado, generado por la plataforma |
| 12 | `referencia_del_contrato` | text | Identificador del contrato firmado, generado por la entidad del estado |
| 13 | `estado_contrato` | text | Estado del contrato, frente a su ejecución, firma o liquidación |
| 14 | `codigo_de_categoria_principal` | text | Codigo UNSPSC de la categoría principal para el contrato |
| 15 | `descripcion_del_proceso` | text | Descripción del objeto del proceso de compra |
| 16 | `tipo_de_contrato` | text | Tipo de contrato de acuerdo a su marco jurídico |
| 17 | `modalidad_de_contratacion` | text | Modalidad de contratación de acuerdo al modelo de selección |
| 18 | `justificacion_modalidad_de` | text | Justificación de la modalidad, el escenario bajo el cual se toma la decisión de definir una u otra modalidad de contratación |
| 19 | `fecha_de_firma` | calendar_date | Fecha de firma del contrato electronico |
| 20 | `fecha_de_inicio_del_contrato` | calendar_date | Fecha de inicio de las responsabilidades contractuales |
| 21 | `fecha_de_fin_del_contrato` | calendar_date | Fecha de fin de las responsabilidades contractuales |
| 22 | `condiciones_de_entrega` | text | Condiciones bajo las cuales se entrega el producto o servicio |
| 23 | `tipodocproveedor` | text | Tipo de documento del proveedor adjudicado |
| 24 | `documento_proveedor` | text | Número de documento del proveedor adjudicado |
| 25 | `proveedor_adjudicado` | text | Nombre del proveedor adjudicado |
| 26 | `es_grupo` | text | Determina el proveedor es un grupo de entidades, existe un conjunto de datos de CCE que contiene la conformación de los grupos |
| 27 | `es_pyme` | text | Determina si la empresa es una Pyme |
| 28 | `habilita_pago_adelantado` | text | Determina si el contrato tiene habilitada la opción de pago de adelantos |
| 29 | `liquidaci_n` | text | Determina si el contrato ha sido liquidado |
| 30 | `obligaci_n_ambiental` | text | Determina si el contrato tiene compromisos de cumplimiento a obligaciones ambientales |
| 31 | `obligaciones_postconsumo` | text | Determina si el contrato tiene compromisos de cumplimiento a obligaciones posteriores a la entrega del producto o prestación del servicio |
| 32 | `reversion` | text | Determina si el contrato ha sido reversado |
| 33 | `origen_de_los_recursos` | text | Origen de los Recursos, a nivel presupuestal |
| 34 | `destino_gasto` | text | Destino del gasto, a nivel presupuestal |
| 35 | `valor_del_contrato` | number | Valor total del contrato |
| 36 | `valor_de_pago_adelantado` | number | Valor del pago por adelantado |
| 37 | `valor_facturado` | number | Valor Facturado a la fecha |
| 38 | `valor_pendiente_de_pago` | number | Valor Pendiente de Pago a la fecha |
| 39 | `valor_pagado` | number | Valor Pagado a la fecha |
| 40 | `valor_amortizado` | number | Valor Amortizado a la fecha |
| 41 | `valor_pendiente_de` | number | Valor Pendiente de Amortizacion a la fecha |
| 42 | `valor_pendiente_de_ejecucion` | number | Valor Pendiente de Ejecucion a la fecha |
| 43 | `saldo_cdp` | number | Saldo del CDP asignado al proceso y al contrato |
| 44 | `saldo_vigencia` | number | Saldo actual para la vigencia del CDP asignado al proceso y al contrato |
| 45 | `espostconflicto` | text | Determina si el proceso está asociado a algún evento de acuerdo de paz |
| 46 | `dias_adicionados` | number | Días adicionados al contrato electrónico |
| 47 | `puntos_del_acuerdo` | text | Pilares del acuerdo de paz, si el contrato es post conflicto |
| 48 | `pilares_del_acuerdo` | text | Pilares del acuerdo de paz |
| 49 | `urlproceso` | url | URL del proceso de compra en la plataforma SECOP II |
| 50 | `nombre_representante_legal` | text | Nombre del representante legal de la entidad |
| 51 | `nacionalidad_representante_legal` | text | Nacionalidad del representante legal de la entidad |
| 52 | `domicilio_representante_legal` | text | Dirección de domicilio del representante legal de la entidad |
| 53 | `tipo_de_identificaci_n_representante_legal` | text | Tipo de identificación del representante legal de la entidad |
| 54 | `identificaci_n_representante_legal` | text | Numero de identificación del representante legal de la entidad |
| 55 | `g_nero_representante_legal` | text | Género sexual del representante legal de la entidad |
| 56 | `presupuesto_general_de_la_nacion_pgn` | number | Valor de origen de los recursos que corresponde al Presupuesto General de la Nacion – PGN |
| 57 | `sistema_general_de_participaciones` | number | Valor de origen de los recursos que corresponde al Sistema General de Participaciones |
| 58 | `sistema_general_de_regal_as` | number | Valor de origen de los recursos que corresponde al Sistema General de Regalías |
| 59 | `recursos_propios_alcald_as_gobernaciones_y_resguardos_ind_genas_` | number | Indica el valor de recursos de la entidad en el contrato electronico |
| 60 | `recursos_de_credito` | number | Valor de origen de los recursos que corresponde a Recursos de Credito |
| 61 | `recursos_propios` | number | Valor de origen de los recursos que corresponde a Recursos Propios |
| 62 | `ultima_actualizacion` | calendar_date | Fecha de última actualización del contrato electronico |
| 63 | `codigo_entidad` | number | Codigo de la entidad en la plataforma SECOPII |
| 64 | `codigo_proveedor` | text | Codigo del proveedor edn la plataforma SECOPII |
| 65 | `fecha_inicio_liquidacion` | calendar_date | Fecha de inicio de liquidación del contrato electrónico |
| 66 | `fecha_fin_liquidacion` | calendar_date | Fecha de fin de liquidación del contrato electrónico |
| 67 | `objeto_del_contrato` | text | Objeto del contrato electrónico |
| 68 | `duraci_n_del_contrato` | text | Describe la duración del contrato en el tiempo |
| 69 | `nombre_del_banco` | text | Indica el nombre del banco en donde se consignaran los pagos del contrato |
| 70 | `tipo_de_cuenta` | text | Tipo de cuenta en la que se se consignaran los pago del contrato |
| 71 | `n_mero_de_cuenta` | text | Numero de cuenta en donde se haran los pagos del contrato |
| 72 | `el_contrato_puede_ser_prorrogado` | text | Indica si el contrato puede ser o no prorrogado |
| 73 | `fecha_de_notificaci_n_de_prorrogaci_n` | calendar_date | Infica la fecha de notificación de la prorrogación del contrato |
| 74 | `nombre_ordenador_del_gasto` | text | Describe el nombre del ordenador del gasto de la entidad compradora |
| 75 | `tipo_de_documento_ordenador_del_gasto` | text | Indica el tipo de documento del ordenador del gasto de la entidad compradora |
| 76 | `n_mero_de_documento_ordenador_del_gasto` | text | Indica el número de documento del ordenador del gasto |
| 77 | `nombre_supervisor` | text | Describe el nombre del supervisor de la entidad compradora |
| 78 | `tipo_de_documento_supervisor` | text | Indica el tipo de documento del supervisor de la entidad compradora |
| 79 | `n_mero_de_documento_supervisor` | text | Indica el número de documento del supervisor |
| 80 | `nombre_ordenador_de_pago` | text | Describe el nombre del Ordenador de Pago de la entidad compradora |
| 81 | `tipo_de_documento_ordenador_de_pago` | text | Indica el tipo de documento del Ordenador de Pago de la entidad compradora |
| 82 | `n_mero_de_documento_ordenador_de_pago` | text | Indica el número de documento del Ordenador de Pago |
| 83 | `documentos_tipo` | text | Indica si se utilizaron documentos tipo en el contrato |
| 84 | `descripcion_documentos_tipo` | text | Descripción de los documentos tipo utilizados |
| 85 | `direcci_n_de_ejecuci_n_del_contrato` | text | Dirección en donde se ejecuto el contrato durante su vigencia |
| 86 | `criterios_de_sostenibilidad_ambiental` | text | Indica si se definieron Criterios de sostenibilidad ambiental |
| 87 | `requisitos_ambientales_en_las_especificaciones_t_cnicas` | text | Indica si se definieron Requisitos ambientales en las especificaciones técnicas |
| 88 | `criterios_ambientales_en_la_evaluaci_n_de_las_ofertas` | text | Indica si se definieron Criterios ambientales en la evaluación de las ofertas |
| 89 | `obligaciones_contractuales_o_poscontractuales_a_nivel_ambiental` | text | Indica si se definieron Obligaciones contractuales o poscontractuales a nivel ambiental |
| 90 | `uso_de_etiquetado_ecol_gico` | text | Indica si se definieron el Uso de etiquetado ecológico |
| 91 | `obligaciones_posconsumo` | text | Indica si se definieron Obligaciones posconsumo |
| 92 | `fecha_inicio_obligaciones_posconsumo` | calendar_date | Fecha inicio obligaciones posconsumo |
| 93 | `fecha_fin_obligaciones_posconsumo` | calendar_date | Fecha fin obligaciones posconsumo |
| 94 | `fecha_inicio_reversi_n` | calendar_date | Fecha inicio reversión |
| 95 | `fecha_fin_reversi_n` | calendar_date | Fecha fin reversión |

## 4. Observaciones técnicas

- `departamento` y `ciudad` describen el lugar de registro de la entidad estatal que publica el contrato; no deben confundirse automáticamente con el lugar de ejecución.
- `fecha_de_firma` puede servir como referencia temporal inicial, pero debe revisarse la disponibilidad de fechas nulas y la distribución por periodos.
- `valor_del_contrato` es un campo numérico; se deben verificar valores atípicos, nulos y posibles duplicidades por `id_contrato`.
- `codigo_de_categoria_principal` corresponde a la clasificación UNSPSC, distinta de los códigos CIIU de RUES.
- Los nombres de algunas variables contienen caracteres sustituidos por guiones bajos; se conservaron los identificadores tal como aparecen en los metadatos.
- Existen campos de identificación personal, domicilios y cuentas bancarias. Deben excluirse de informes y publicaciones salvo que exista una necesidad justificada y un tratamiento apropiado.
- Las descripciones reproducen el contenido suministrado por la fuente, incluidas posibles erratas.

## 5. Estado del diccionario

**Estado:** Documentación estructural inicial completada.  
**Variables identificadas:** 95 de 95.  
**Pendiente:** Verificar formatos, valores nulos, duplicados, cobertura temporal y territorial, y pertinencia de las variables para las preguntas de investigación.
