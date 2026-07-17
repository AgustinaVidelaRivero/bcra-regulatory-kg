# Verificaciones de la adjudicación del DEV v7 — barridos determinísticos (parte 1)

Fecha: 2026-07-16. SOLO LECTURA; escrituras: las 2 partes de este reporte. Sin verificador,
capa ni S1. **Solo HECHOS — cero adjudicación.** Mecanismo idéntico a
`verificaciones_validacion`: outputs completos re-ejecutados por traza (con nº de paso),
barridos normalizados (lowercase, sin acentos) sobre id+label+properties del kg del run —
provenances aparte donde se pide —, D1 (`evaluar_alcanzabilidad`) sobre candidatos no
expuestos, candidatos ÍNTEGROS, exposiciones con paso+nodo+fragmento.

Partes: **1** = tabla resumen + log de los puntos 1 (run_2/CQ-021) y 2 (run_4/CQ-008);
**2** = log de los puntos 3 (run_4/CQ-021) y 4 (run_4/CQ-028).

## Notas metodológicas (límites del método, documentados)

- **Exposición por substring de id:** el id corto `mpor` (run_4) matchea dentro de palabras
  como "importe" — su lista de pasos "expuestos" en CQ-008 es un FALSO POSITIVO mecánico
  del método (documentado; el resto de los ids son largos y no ambiguos).
- **Identificación de "nodos fuente" por descriptor `id=`:** los matches dentro de unidades
  de `ver_vecinos` (aristas) no aportan id de nodo al extractor — se listan igual con su
  descriptor de arista (relevante en r2/CQ-021, ver tabla).
- **Frases contiguas:** la exposición busca la frase exacta normalizada ("precancelacion
  parcial" no matchea "precancelación total o parcial" — se reporta aparte).

## Tabla resumen — verificación × resultado (puntero = rótulo de sección en el log)

| # | Verificación | Resultado (hecho, una línea) | Puntero |
|---|---|---|---|
| 1.1 | kg r2: `optativo\|optativa` | **0 nodos en todo el kg run_2** | parte 1, [1a] 'optativo\|optativa' |
| 1.2 | kg r2: `45 dias` | 6 nodos; el único de clasificación (`plazo:45_dias_de_realizada_la_reclasificacion`, prov "Sección 3 — preámbulo") expuesto SOLO en paso 6; los otros 5 (capitales/exterior) NO expuestos, D1 false | parte 1, [1a] '45 dias' |
| 1.3 | kg r2: `comunicar ∧ clasificacion` | 5 nodos; `obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente` expuesto en pasos 1,9,10,12,13,14; `comunicar_cambios_negativos` en 1,4,6; `comunicar_a_sefyc_opcion…` en 1 | parte 1, [1a] 'comunicar ∧ clasificacion' |
| 1.4 | kg r2: `saldo de deuda` | 7 nodos; **ninguno expuesto** (incluye `requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo`, D1 false rank 3109); todos D1 false | parte 1, [1a] 'saldo de deuda' |
| 1.5 | kg r2: `deudores comprendidos` | **0 nodos** | parte 1, [1a] 'deudores comprendidos' |
| 1.6 | kg r2: `3.4.2` (props y provs APARTE) | **0 en props · 0 en provenances** (el formato de provenance de run_2 es "Sección N > Punto X" y no contiene 3.4.2) | parte 1, [1a] '3.4.2' |
| 1.7 | Nodo del claim verdadero de los 45 días (por exposición) | La ÚNICA exposición de "45 dias" en los 15 outputs es la ARISTA `tiene_plazo→plazo:45_dias_de_realizada_la_reclasificacion` del ver_vecinos del paso 6 (vecino_label + provenances; las properties del nodo — "Plazo máximo para remitir información de cambios negativos…" — nunca se mostraron); contenido íntegro pegado | parte 1, [1b] |
| 2.1 | kg r4: `10 dias` | 17 nodos — **ninguno de clasificación** (exterior/capitales); ninguno expuesto de verdad (la lista de `mpor` es el falso positivo documentado); D1 false en todos | parte 1, [2a] '10 dias' |
| 2.2 | kg r4: `solicitud ∧ clasificacion` | **0 nodos en todo el kg run_4** | parte 1, [2a] 'solicitud ∧ clasificacion' |
| 2.3 | kg r4: `comunicar ∧ clasificacion` | 1 nodo: `deudor_en_gestion_judicial_o_extrajudicial_de_cobro` (prov "p.9-12 / Punto 3.4.2") — NO expuesto, D1 false (mejor rank 28) | parte 1, [2a] 'comunicar ∧ clasificacion' |
| 2.4 | kg r4: `central de deudores` | 1 nodo: `central_de_deudores_del_sistema_financiero` — expuesto SOLO en paso 15 (el último) | parte 1, [2a] 'central de deudores' |
| 2.5 | kg r4: `8.1` (props/provs APARTE) | 0 en props · 17 SOLO en provenances (regla de cruce declarada → 2 íntegros: `entidad_atipica` expuesto paso 10; `patrimonio_neto_basico_pnb` NO, D1 false) | parte 1, [2a] '8.1' |
| 3.1 | Fuentes de los 3 centrales verdaderos (r4/CQ-021, por exposición) | `optativ`: **AUSENTE en los 16 outputs**; `saldo`: expuesto (fuente principal `cambio_negativo_en_clasificacion`, description "…con excepciones segun el saldo de deuda", + 5 nodos saldo_* del paso 5); `regimen informativo`: la única exposición es `regimen_informativo_de_operaciones_de_cambio_rioc` (mecanismo de registro de CAMBIOS, paso 8) — 10 nodos fuente íntegros pegados | parte 2, [3a] |
| 3.2 | kg r4: `optativo\|optativa` | **0 nodos en todo el kg run_4** | parte 2, [3b] 'optativo\|optativa' |
| 3.3 | kg r4: `regimen informativo ∧ deudores` | **0 nodos** | parte 2, [3b] 'regimen informativo ∧ deudores' |
| 3.4 | kg r4: `saldo de deuda` | 5 nodos; expuestos: `cambio_negativo_en_clasificacion` (1,2,3,4,6,8,16), `saldo_de_deuda` (5,6,12), `saldo_de_deuda_pendiente` (5,6), `declaracion_jurada…` (5); `loan_to_value_ltv` NO (D1 false) | parte 2, [3b] 'saldo de deuda' |
| 3.5 | kg r4: `45 dias` | 4 nodos; `periodo_de_45_dias` expuesto (12,13,14,16) y `operaciones_dvp_fallidas_entre_31_y_45_dias` (12,16) — ambos de CAPITALES, no de clasificación; `factor_de_exigencia_de_capital_75` NO (D1 false) | parte 2, [3b] '45 dias' |
| 3.6 | kg r4: `3.4.2` (props/provs) | 0 en props · 10 SOLO en provenances; de esos, expuestos: `cambio_negativo_en_clasificacion` (1,2,3,4,6,8,16) y `deudor_en_gestion_judicial…` (4); el resto NO, D1 false | parte 2, [3b] '3.4.2' |
| 3.7 | Secundario r4/CQ-021: `medios ∧ comunicac` | **AUSENTE — ninguna unidad de los 16 outputs contiene ambos términos** | parte 2, [3e] |
| 4.1 | kg r4: `precancelacion` (TODOS íntegros) | 14 nodos íntegros pegados. El ÚNICO con el criterio es `comision_por_precancelacion` (prov "p.12-14 / Punto 2.3.2.1, párrafo segundo"), formulación EXACTA: "…cuando haya transcurrido al menos la cuarta parte del plazo original **o 180 días**." — **la cláusula "de ambos el mayor" del GT NO está en el nodo** (disyunción "o" simple, sin criterio de desempate) | parte 2, [4a] 'precancelacion' |
| 4.2 | kg r4: `180 dias` | 17 nodos (regla de cruce declarada); en outputs, "180 dias" aparece SOLO vía la description de `comision_por_precancelacion` (paso 3) | parte 2, [4a] '180 dias' + [4b] |
| 4.3 | kg r4: `cuarta parte` | 1 nodo (`comision_por_precancelacion`); en outputs solo vía paso 3 | parte 2, [4a] 'cuarta parte' + [4b] |
| 4.4 | kg r4: `2.3.2` (props/provs) | 0 en props · 19 SOLO en provenances (cruce declarado → 13 íntegros) | parte 2, [4a] '2.3.2' |
| 4.5 | Exposición del criterio "primero"/"el mayor" | "el mayor" aparece SOLO en `posicion_neta_total` (posiciones netas de moneda — otro tema); **el criterio de desempate del GT no está en ningún output** | parte 2, [4b] 'criterio' |
| 4.6 | D1 sobre no expuestos (CQ-028) | Todos false SALVO `precancelacion_de_capital_e_intereses` (nodo de EXTERIOR, operación de cambio): **D1 alcanzable=true, rank 8** con la consulta "comision precancelacion" | parte 2, [4a] (D1 por candidato) |
| 4.7 | Secundario CQ-028: `precancelacion parcial` | AUSENTE como frase contigua en outputs; la formulación expuesta es "precancelación **total o** parcial" (label de `derecho_de_precancelacion_total_o_parcial`, pasos 2,5) y "total o parcial de financiaciones" (description de `comision_por_precancelacion`, paso 3) | parte 2, [4d] + [4a] |

---

## LOG ÍNTEGRO — puntos 1 y 2

```
==============================================================================
1. run_2/CQ-021 (15 outputs re-ejecutables)
==============================================================================

[1a] barridos kg run_2 (exposición y D1 por candidato integrados):
  [barrido kg run_2: 'optativo|optativa'] en id/label/properties: 0
  [barrido kg run_2: '45 dias'] en id/label/properties: 6

  --- plazo:45_dias_previos_a_la_transferencia (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "plazo:45_dias_previos_a_la_transferencia",
 "type": "Plazo",
 "label": "45 días previos a la transferencia",
 "properties": {
  "description": "Plazo dentro del cual el originante o fiduciario debe llevar a cabo el análisis de las condiciones de cumplimiento de los activos.",
  "unidad": "días",
  "duracion": "45",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo /b"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2775, "n_consultas": 34, "top10": []}

  --- umbral:factor_de_capital_75 (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "umbral:factor_de_capital_75",
 "type": "Umbral",
 "label": "factor de capital 75%",
 "properties": {
  "description": "Exigencia de capital aplicable a operaciones DvP fallidas entre 31 y 45 días hábiles posteriores a la fecha de liquidación.",
  "valor": "75",
  "unidad": "porcentaje",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 76, "n_consultas": 34, "top10": []}

  --- plazo:entre_31_y_45_dias_habiles (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "plazo:entre_31_y_45_dias_habiles",
 "type": "Plazo",
 "label": "entre 31 y 45 días hábiles",
 "properties": {
  "description": "Rango de días hábiles posteriores a la liquidación para aplicar el factor de capital del 75%.",
  "duracion": "31-45",
  "unidad": "días hábiles",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 2369, "n_consultas": 34, "top10": []}

  --- plazo:45_dias_de_realizada_la_reclasificacion (props) | expuesto en outputs de CQ-021: pasos [6] ---
{
 "id": "plazo:45_dias_de_realizada_la_reclasificacion",
 "type": "Plazo",
 "label": "45 días de realizada la reclasificación",
 "properties": {
  "description": "Plazo máximo para remitir información de cambios negativos en clasificación a los deudores.",
  "duracion": "45 días",
  "unidad": "días",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}

  --- plazo:545_dias_corridos_para_pagos_anticipados_de_bienes_de_capital (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "plazo:545_dias_corridos_para_pagos_anticipados_de_bienes_de_capital",
 "type": "Plazo",
 "label": "545 días corridos para pagos anticipados de bienes de capital",
 "properties": {
  "description": "Plazo máximo de extensión para pagos anticipados de bienes de capital con demoras ajenas a la voluntad del importador.",
  "duracion": "545",
  "unidad": "días corridos",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1640, "n_consultas": 34, "top10": []}

  --- umbral:cargo_de_capital_entre_31_y_45_dias (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "umbral:cargo_de_capital_entre_31_y_45_dias",
 "type": "Umbral",
 "label": "cargo de capital entre 31 y 45 días",
 "properties": {
  "description": "Cargo de capital del 75% cuando la operación DvP falla entre 31 y 45 días hábiles posteriores a liquidación.",
  "valor": "75",
  "unidad": "%",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 82, "n_consultas": 34, "top10": []}
  [barrido kg run_2: 'comunicar ∧ clasificacion'] en id/label/properties: 5

  --- sujeto_regulado:entidad_financiera (props) | expuesto en outputs de CQ-021: pasos [6] ---
{
 "id": "sujeto_regulado:entidad_financiera",
 "type": "SujetoRegulado",
 "label": "entidad financiera",
 "properties": {
  "description": [
   "Sujeto regulado que debe cumplir con exigencias de capital mínimo bajo supervisión del BCRA.",
   "Sujeto obligado al cálculo y cumplimiento de exigencia de capital por riesgo de crédito conforme a la fórmula establecida.",
   "Sujeto regulado sobre cuya RPC se miden los límites de inversiones significativas.",
   "Entidad que otorga financiaciones y realiza operaciones en mercados de títulos valores, de monedas y de derivados.",
   "Entidad financiera que debe mantener exposiciones minoristas normativas diversificadas dentro de los límites regulados.",
   "Institución obligada a cumplir los límites de endeudamiento minorista y verificar información en operaciones de compra de cartera.",
   "Sujeto regulado responsable del otorgamiento y seguimiento de créditos hipotecarios.",
   "Organización que otorga créditos y mantiene exposiciones a deudores, responsable de evaluar situaciones de incumplimiento.",
   "Institución regulada sujeta a requisitos de capitales mínimos.",
   "Entidad regulada que participa en estructuras de titulización, puede ser originante, cedente o titular de posiciones.",
   "Persona jurídica que realiza operaciones de titulización y está sujeta a requisitos de capital mínimo.",
   "Entidad financiera que realiza operaciones de titulización y requiere calcular exigencia de capital.",
   "Institución sujeta a regulación de capitales mínimos por riesgo de crédito en inversiones en fondos.",
   "Entidad financiera que invierte en fondos y debe cumplir requisitos de capital.",
   "Institución financiera sujeta a las obligaciones de capital y seguimiento de riesgo de crédito de contraparte.",
   "Sujeto que debe constituir contratos de neteo y obtener opinión legal sobre exigibilidad del neteo en operaciones derivadas.",
   "Sujeto regulado que participa en operaciones de garantía y debe mantener capital mínimo.",
   "Sujeto que participa en operaciones con derivados y debe aplicar regulación de capitales mínimos.",
   "Sujeto obligado a calcular los parámetros de riesgo en instrumentos derivados.",
   "Entidad sujeta a regulación que puede tener exposición significativa al riesgo de base de productos.",
   "Sujeto regulado que debe cumplir con las exigencias de capital por exposición al riesgo de contraparte.",
   "Institución sujeta a requerimientos de capital mínimo por riesgo de crédito de contraparte.",
   "Institución sujeta a regulación de capitales mínimos que realiza operaciones con entidades de contraparte central.",
   "Entidad financiera sujeta a requisitos de capitalización mínima y regulaciones sobre exposiciones con contrapartes de compensación centralizada.",
   "Sujeto regulado obligado a cumplir requisitos de capital respecto de exposiciones con QCCP y CCP, y a aplicar ponderadores de riesgo a aportes de fondos de garantía.",
   "Entidad financiera sujeta a requisitos de capital y cobertura de riesgo de crédito.",
   "Institución financiera que contrata protección crediticia y asume garantías.",
   "Entidad financiera que aplica el método simple de cobertura mediante activos admitidos como garantía.",
   "Institución que realiza operaciones de pase y ejecuta procedimientos de liquidación y cobranza.",
   "Entidad financiera que realiza operaciones de financiación con títulos valores.",
   "Entidades financieras sujetas a regulación de capitales mínimos de riesgo de mercado.",
   "Sujeto regulado que posee derivados de crédito e instrumentos de crédito y debe cumplir exigencias de capital regulatorio.",
   "Sujeto regulado que debe cumplir exigencias de capital por riesgo de mercado en posiciones en acciones.",
   "Sujeto que realiza operaciones de derivados, índices y arbitraje sujeto a exigencias de capital mínimo.",
   "Sujeto regulado que utiliza derivados y mantiene posiciones en productos básicos.",
   "Sujeto regulado que debe cumplir con la determinación diaria de integración de capital según lo establecido en la norma.",
   "Institución financiera sujeta a los requisitos de capital mínimo y gestión de riesgos de mercado.",
   "Entidad sujeta a supervisión regulatoria que debe implementar marco de valuación prudente.",
   "Entidad sujeta a obligaciones de valuación de posiciones conforme a las metodologías establecidas.",
   "Entidades financieras sujetas a regulación de capitales mínimos.",
   "Institución financiera sujeta a los requisitos de capital mínimo establecidos por el BCRA.",
   "Entidad sujeta a requisitos de capital mínimo y obligaciones de divulgación de información regulatoria.",
   "Sujeto regulado obligado a computar el capital ordinario de nivel uno conforme a esta normativa.",
   "Institución sujeta a regulación de capitales mínimos por el BCRA.",
   "Sujeto regulado que debe cumplir con todos los requisitos y obligaciones relativos a instrumentos subordinados de capital.",
   "Entidad financiera sujeta a supervisión y regulación por el BCRA, incluyendo entidades y sus subsidiarias.",
   "Sujeto regulado que debe reconocer capital admisible emitido por subsidiarias sujetas a supervisión consolidada en su RPC.",
   "Sujeto regulado que realiza inversiones en capital de otras entidades financieras, empresas de servicios complementarios y compañías de seguro.",
   "Sujeto regulado a quien se aplican las reglas de deducción de capital por inversiones en otras entidades financieras.",
   "Sujeto regulado que integra y aumenta capital mediante aportes sujetos a estas normas.",
   "Sujeto regulado que debe implementar el proceso de mapping de calificaciones a ponderadores de riesgo.",
   "Personas jurídicas que otorgan financiaciones y deben clasificar a sus clientes.",
   "Entidad que cede créditos, otorga préstamos y realiza la clasificación de deudores.",
   "Instituciones financieras sujetas a las obligaciones de clasificación de deudores y previsionamiento reguladas por el BCRA.",
   "Institución financiera obligada a llevar legajo de cada deudor de su cartera y de sus corresponsales.",
   "Institución financiera responsable de la clasificación de deudores y la presentación de informes a la Superintendencia.",
   "Institución financiera responsable de clasificar su cartera según las categorías establecidas.",
   "Institución financiera responsable de clasificar deudores y realizar reevaluaciones de clasificación según los criterios establecidos.",
   "Institución que otorga financiaciones y clasifica clientes.",
   "Sujeto obligado a concertar acuerdos con deudores en mora y ejecutar procedimientos de clasificación.",
   "Institución financiera que otorga financiamiento y clasifica deudores según las normas del BCRA.",
   "Instituciones financieras obligadas a aplicar los criterios de clasificación de deudores y refinanciación establecidos en la norma.",
   "Entidad que asigna clasificación inicial al deudor y está obligada a recategorizar.",
   "Institución financiera sujeta a las obligaciones de reporte de incrementos de cartera irregular.",
   "Institución obligada a comunicar clasificaciones de deudores y cumplir normas de clasificación individual y consolidada.",
   "Sujeto regulado que debe cumplir con regímenes de clasificación de deudores y provisiones mínimas.",
   "Sujeto regulado que emite certificaciones de acceso al mercado de cambios.",
   "Intermediario responsable de verificar requisitos normativos antes de solicitar acceso al BCRA.",
   "Entidad que otorga acceso al mercado de cambios al cliente para operaciones de recompra, rescate y pago de gastos asociados.",
   "Entidad que otorga acceso al mercado de cambios a clientes para operaciones de recompra y rescate de títulos de deuda.",
   "Entidad que otorga acceso al mercado de cambios para pagos de capital e intereses mediante fideicomisos.",
   "Entidad financiera local que proporciona acceso al mercado de cambios para la operación.",
   "Entidad sujeta al deber de contar con conformidad del BCRA o requerir declaración jurada del cliente para acceso al mercado de cambios.",
   "Institución que actúa como intermediaria en operaciones de cambios y debe obtener conformidad o declaración jurada.",
   "Entidad regulada que debe realizar verificaciones y controles sobre operaciones de egresos de fondos al exterior.",
   "Entidad que actúa como intermediaria en operaciones de exportación y emisión de certificaciones.",
   "Intermediaria que canaliza operaciones a través del SML y debe cumplir requisitos.",
   "Entidad autorizada para registrar operaciones de cambio y emitir boletos de venta de cambio.",
   "Entidad que debe realizar el boleto de venta de cambio y obtener la documentación del cliente.",
   "Entidad financiera que realiza operaciones de liquidación de cobros de exportaciones y acceso a mercado de cambios bajo estos mecanismos.",
   "Institución financiera regulada que realiza operaciones con clientes.",
   "Persona jurídica que realiza operaciones en el mercado de cambios y debe registrarlas ante el BCRA.",
   "Entidad autorizada a elaborar boletos globales diarios según las condiciones establecidas en la norma.",
   "Entidad autorizada a recibir depósitos, mantener cuentas corresponsales y seguimiento de permisos de exportación.",
   "Institución financiera responsable de registrar operaciones y cumplir requisitos de ingreso y liquidación de divisas.",
   "Banco o institución de crédito elegible para ser designada por el exportador como responsable del seguimiento de operaciones de exportación.",
   "Entidad encargada del seguimiento de permisos de exportación y de realizar certificaciones y denuncias ante el BCRA.",
   "Entidad que debe cumplimentar el seguimiento de permisos de embarque y archivar documentación a disposición del BCRA.",
   "Entidad que opera en operaciones de comercio exterior y debe cumplir con requisitos de documentación.",
   "Entidad bancaria que autoriza y gestiona la imputación de descuentos, gastos y multas al permiso de embarque.",
   "Entidad regulada que debe cumplir obligaciones de documentación en operaciones de exportación.",
   "Entidad autorizada a operar en el mercado de cambios y registrar permisos de embarque.",
   "Entidad autorizada a emitir certificaciones de aplicación y seguimiento de operaciones de comercio exterior.",
   "Entidad autorizada a emitir certificaciones de aplicación de divisas en operaciones con el exterior.",
   "Entidad sujeta a las obligaciones de certificación, verificación y registro establecidas en la norma.",
   "Entidad financiera regulada por la normativa cambiaria del BCRA.",
   "Entidad que actúa como cliente en operaciones de cambio y debe efectuar boletos de venta según lo establecido en la norma.",
   "Entidad encargada de dar acceso al mercado de cambios y verificar cumplimiento de requisitos.",
   "Entidad autorizada a operar en el mercado de cambios y realizar pagos de importación.",
   "Entidades que operan en el mercado de cambios y deben cumplir requisitos de conformidad previa.",
   "Entidad financiera que emite u otorga cartas de crédito o letras avaladas para operaciones de importación.",
   "Entidad que accede al mercado de cambios para realizar pagos de importaciones y debe cumplir con obligaciones de registro e información.",
   "Entidad regulada que participa en operaciones de cambios y debe verificar requisitos.",
   "Institución que realiza el seguimiento del pago y registro en SEPAIMPO, y exige la documentación requerida.",
   "Entidad bancaria u otro intermediario que debe exigir documentación y declaraciones juradas para autorizar operaciones de importación con mora o insolvencia del proveedor.",
   "Entidad que debe verificar la separación de componentes de pago en operaciones de alquiler con opción de compra.",
   "Entidad financiera que otorga líneas de crédito del exterior para financiar importaciones de bienes y accede al mercado de cambios para su cancelación.",
   "Entidad sujeta a regulación que debe contar con declaración jurada del importador y opera en mercado de cambios.",
   "Institución que debe contar con documentación y requerimientos del cliente para operaciones de pago de deudas comerciales.",
   "Banco o institución financiera elegible para ser nominada por el importador para llevar a cabo el seguimiento de la oficialización de importación, salvo aquellas que hayan optado por no operar en comercio exterior.",
   "Entidad por donde se cursan los fondos y que debe certificar las devoluciones de pagos.",
   "Entidades financieras locales que intervienen en operaciones de cambios, financiamiento y garantías.",
   "Sujeto regulado responsable de verificar requisitos y acceder al mercado de cambios.",
   "Institución financiera que otorga crédito para financiar importaciones de servicios y accede al mercado de cambios.",
   "Entidad que opera en el mercado de cambios y otorga acceso a operaciones de cambio para proyectos RIGI.",
   "Entidad que otorga acceso al mercado de cambios y debe verificar requisitos complementarios.",
   "Institución financiera responsable de registrar aportes de capital en el régimen informático de operaciones de cambio (RIOC).",
   "Proveedor de servicios financieros que opera casas operativas y atiende usuarios.",
   "Sujeto regulado sometido al régimen informativo contable mensual de consolidación.",
   "Sujeto al que se aplica este régimen informativo de exigencia e integración de capitales mínimos.",
   "Sujeto obligado a cumplir con el régimen informativo contable mensual.",
   "Institución sujeta a obligaciones de información y cálculo de exigencias de capital.",
   "Sujeto regulado que debe reportar información contable mensual según régimen informativo.",
   "Sujeto obligado a cumplir requisitos de capitales mínimos y régimen informativo contable mensual.",
   "Sujeto obligado a realizar cálculos de valor económico del patrimonio y reportar información según régimen informativo contable mensual."
  ],
  "version": "vigente_2026-05",
  "modalidad": null
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Punto 2.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 3.1 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo /d"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 3.2 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 5.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /b"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3 /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3 /b"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 7.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 8.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 9 > Punto 10.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Encabezado"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 1.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 3.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 3.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 3.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 5.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /b"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.3"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Punto 7.4"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 10 > Punto 5593 /b"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Punto 4.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.8"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 7 > Punto 8.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 8 > Punto 8.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 9 > Sección 9 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Anexo d — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 11.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 11 > Anexo d > Sección 11 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Sección 13 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.4"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.6"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Sección 14 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 14.4"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 1 > Punto 1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Sección 9 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Sección 11 — preámbulo"
  }
 ]
}

  --- sujeto_regulado:entidades_financieras (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "sujeto_regulado:entidades_financieras",
 "type": "SujetoRegulado",
 "label": "entidades financieras",
 "properties": {
  "description": [
   "Instituciones financieras sujetas a los requisitos de capitales mínimos y obligadas a presentar planes de regularización ante incumplimientos.",
   "Sujetos regulados sujetos a clasificación en grupos conforme a su importancia sistémica.",
   "Instituciones financieras sujetas a los requisitos de análisis de contrapartes y debida diligencia establecidos en la norma.",
   "Entidades financieras sujetas a la obligación de asignar ponderadores de riesgo conforme a las definiciones establecidas.",
   "Instituciones autorizadas a clasificar exposiciones minoristas normativas según categorías transaccionales o no transaccionales, y obligadas a comunicar esa clasificación a SEFyC.",
   "Instituciones financieras sometidas a regulación por el BCRA.",
   "Entidades financieras sujetas a regulación de capitales mínimos.",
   "Entidades sometidas a los requisitos de capital mínimo y ponderación de riesgo establecidos en la norma.",
   "Sujetos regulados que pueden aplicar neteo bilateral en operaciones con contrapartes sujetas a acuerdos de novación o formas legalmente válidas de neteo.",
   "Entidades obligadas a considerar sensibilidad y volatilidad de subyacentes en operaciones derivadas complejas.",
   "Entidades sujetas al cálculo de parámetros de segmentos CDO y aplicación de factores regulatorios.",
   "Entidades sujetas a regulación de capitales mínimos conforme a normas de capitales mínimos.",
   "Sujetos regulados que pueden tener exposiciones con entidades de contraparte central y considerar QCCP según normas de la CNV.",
   "Instituciones financieras sujetas a los requisitos de capital mínimo y técnicas de cobertura de riesgo de crédito.",
   "Entidades financieras sujetas a los requisitos de aplicación de técnicas de coberturas del riesgo de crédito.",
   "Participantes esenciales del mercado sujetos a requisitos de capital mínimo.",
   "Entidades sujetas a requisitos de capitales mínimos que utilizan método integral para cobertura de riesgo de crédito.",
   "Ente admisible como garante o proveedor de protección crediticia.",
   "Instituciones financieras sujetas a exigencias de capital por riesgo de mercado según régimen de capitales mínimos.",
   "Sujetos obligados al cálculo y cumplimiento de exigencias de capital por riesgo de tasa de interés y riesgo específico.",
   "Personas jurídicas sujetas a la regulación de capitales mínimos por riesgo de mercado.",
   "Sujetos regulados obligados a calcular y mantener capital mínimo por riesgo de tipo de cambio.",
   "Sujetos regulados que emplean posiciones en moneda extranjera y oro, sujetos a requisitos de capital mínimo por riesgo de mercado.",
   "Personas jurídicas sujetas a regulación de capitales mínimos por riesgo de posiciones en opciones.",
   "Sujetos regulados que operan con opciones y deben cumplir con las obligaciones de cálculo y reporte de capital mínimo.",
   "Instituciones sujetas a los lineamientos de valuación prudente de posiciones de menor liquidez.",
   "Instituciones sujetas a la regulación del BCRA que realizan valuaciones de activos.",
   "Entidades sujetas a las normas de capital regulatorio del BCRA.",
   "Personas jurídicas que operan en mercados financieros y están sujetas a regulación del BCRA.",
   "Personas jurídicas sujetas a las prescripciones de los artículos 30 y 32 de la Ley de Entidades Financieras respecto del cálculo de capital regulatorio.",
   "Instituciones financieras sujetas a supervisión y regulación del BCRA en materia de capitales mínimos.",
   "Sujetos regulados a los que aplican los límites mínimos de capital.",
   "Entidades financieras, comprendidas sus filiales en el país y en el exterior, sujetas a supervisión de capitales mínimos.",
   "Instituciones financieras sujetas a regulación de capitales mínimos y evaluación de riesgos crediticios.",
   "Personas jurídicas sujetas a regulación de capitales mínimos por el BCRA.",
   "Sujetos regulados a quienes se aplican los requisitos de capitales mínimos establecidos en el texto ordenado.",
   "Instituciones financieras sujetas a regulación del BCRA que otorgan financiaciones y mantienen legajos de clientes.",
   "Sujetos que deben aplicar los criterios de clasificación de deudores establecidos en la norma.",
   "Instituciones financieras autorizadas que intermedian operaciones de cambios.",
   "Instituciones financieras locales que operan en el mercado de cambios.",
   "Personas jurídicas autorizadas a operar en el mercado de cambios regulado por el BCRA.",
   "Instituciones financieras locales autorizadas a operar en el mercado de cambios.",
   "Instituciones autorizadas a dar acceso al mercado de cambios a personas humanas residentes.",
   "Entidades autorizadas a dar acceso al mercado de cambios a residentes en condiciones específicas.",
   "Entidades autorizadas para operar en el mercado de cambios y dar acceso a residentes.",
   "Personas jurídicas autorizadas a operar en el mercado de cambios y dar acceso a residentes.",
   "Instituciones autorizadas a realizar operaciones de canje y arbitraje con clientes.",
   "Instituciones financieras que cancelan líneas de crédito del exterior y acceden al mercado de cambios.",
   "Instituciones financieras locales responsables de cumplir obligaciones respecto de operaciones de egresos y elaboración de declaraciones juradas.",
   "Entidades autorizadas a operar en el mercado de cambios sin límite de horario.",
   "Instituciones financieras reguladas por el BCRA sujetas a normas sobre posición general de cambios.",
   "Entidades sujetas a las obligaciones de confección de boletos de cambio y registro de operaciones propias.",
   "Entidades financieras locales sujetas a las regulaciones de operaciones de cambio y divisas del BCRA.",
   "Instituciones autorizadas a acceder al mercado de cambios para realizar operaciones de importación y financiamiento.",
   "Instituciones que otorgan acceso al mercado de cambios y verifican requisitos para operaciones de importación.",
   "Instituciones que pueden dar acceso al mercado de cambios para operaciones de importación.",
   "Entidades autorizadas a dar acceso al mercado de cambios y canalizar pagos de servicios a no residentes.",
   "Entidades financieras que emiten u otorgan cartas de crédito o letras avaladas.",
   "Instituciones financieras autorizadas a otorgar acceso al mercado de cambios para egresos.",
   "Personas jurídicas autorizadas por el BCRA para realizar operaciones de cambio de manera permanente o habitual.",
   "Sujetos obligados que ofrecen servicios financieros a usuarios de servicios financieros.",
   "Instituciones financieras reguladas que deben cumplir obligaciones de accesibilidad para usuarios con discapacidad auditiva.",
   "Entidades financieras sujetas a las obligaciones de accesibilidad y renovación de infraestructura.",
   "Instituciones financieras obligadas a cumplir con requisitos mínimos en la relación de consumo.",
   "Instituciones financieras que ofrecen productos y servicios a usuarios de servicios financieros.",
   "Instituciones financieras sujetas a las obligaciones de información sobre comisiones y cargos.",
   "Entidades financieras que atienden a usuarios de servicios financieros y están sujetas a obligaciones de protección.",
   "Sujetos obligados a cumplir el régimen informativo contable mensual relativo a exigencias e integración de capitales mínimos.",
   "Personas jurídicas sujetas a las obligaciones de reporte de exigencia e integración de capitales mínimos.",
   "Entidades financieras sujetas a los requisitos informativos sobre capitales mínimos.",
   "Instituciones financieras del país y del exterior clasificadas en riesgo específico de tasa.",
   "Todas las entidades financieras están obligadas a cumplir este requerimiento de información.",
   "Personas jurídicas sujetas al régimen informativo contable mensual del BCRA.",
   "Entidades sujetas a la presentación de informaciones contables mensuales con códigos de consolidación según lo dispuesto en el régimen informativo."
  ],
  "version": "vigente_2026-05",
  "modalidad": null,
  "valor": null,
  "unidad": null,
  "duracion": null
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 1 > Sección 1 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.8"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 4 > Punto 5.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 5.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Sección 5 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 5 > Punto 6.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo /a"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 2.4"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.6"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.10"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Sección 6 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 10.2"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 6 > Punto 6.11"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 7 > Punto 8.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Sección 8 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 8 > Punto 8.7"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 10 > Punto 11.3"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 12 > Anexo Punto > Punto 2.12"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Punto 6.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 2 > Punto 2.7"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.11"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.12"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.14"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 3 > Punto 3.15"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.9"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.10"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 5 > Punto 5.12"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 9 > Punto 10.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Sección 10 — preámbulo"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Anexo d > Punto 10.10"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 12 > Anexo d > Punto 13.1"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 13 > Anexo d > Punto 13.5"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 14.2"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 14 > Anexo d > Punto 15.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 5 > Punto 1.1"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 3"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.3"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.4"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 2 > Punto 2.5"
  },
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 3 > Punto 4.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Sección 4 — preámbulo"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 4 > Punto 4.3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 9 > Punto 10.1"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 11 > Punto 3"
  },
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "Sección 12 > Punto 12.4"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 34, "top10": []}

  --- obligacion:comunicar_a_sefyc_opcion_de_clasificacion_de_exposiciones_minoristas (props) | expuesto en outputs de CQ-021: pasos [1] ---
{
 "id": "obligacion:comunicar_a_sefyc_opcion_de_clasificacion_de_exposiciones_minoristas",
 "type": "Obligacion",
 "label": "comunicar a SEFyC opción de clasificación de exposiciones minoristas",
 "properties": {
  "description": "Las entidades financieras deben comunicar a la SEFyC el ejercicio de la opción de clasificar exposiciones minoristas normativas como transaccionales o no transaccionales.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Punto 2.8"
  }
 ]
}

  --- obligacion:comunicar_cambios_negativos_en_clasificacion (props) | expuesto en outputs de CQ-021: pasos [1, 4, 6] ---
{
 "id": "obligacion:comunicar_cambios_negativos_en_clasificacion",
 "type": "Obligacion",
 "label": "comunicar cambios negativos en clasificación",
 "properties": {
  "description": "Las entidades financieras deben comunicar a los deudores los cambios negativos en la clasificación asignada.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 3 > Sección 3 — preámbulo"
  }
 ]
}

  --- obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente (props) | expuesto en outputs de CQ-021: pasos [1, 9, 10, 12, 13, 14] ---
{
 "id": "obligacion:comunicar_clasificacion_del_deudor_a_solicitud_del_cliente",
 "type": "Obligacion",
 "label": "comunicar clasificación del deudor a solicitud del cliente",
 "properties": {
  "description": "La entidad financiera debe comunicar al cliente, a su solicitud, la última clasificación asignada, fundamentos, importe total de deudas con el sistema financiero y clasificaciones de la Central de deudores.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 7 > Sección 7 — preámbulo"
  }
 ]
}
  [barrido kg run_2: 'saldo de deuda'] en id/label/properties: 7

  --- obligacion:calcular_relacion_ltv_de_manera_prudente (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "obligacion:calcular_relacion_ltv_de_manera_prudente",
 "type": "Obligacion",
 "label": "calcular relación LTV de manera prudente",
 "properties": {
  "description": "La relación entre saldo de deuda y valor del inmueble (LTV) debe calcularse de manera prudente y con ajuste a requisitos específicos.",
  "modalidad": "obligacion",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 3109, "n_consultas": 34, "top10": []}

  --- requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "requisito:saldo_de_deuda_sin_deducir_previsiones_por_riesgo",
 "type": "Requisito",
 "label": "saldo de deuda sin deducir previsiones por riesgo",
 "properties": {
  "description": "El saldo de deuda pendiente debe computarse sin deducir previsiones por riesgo de incobrabilidad ni coberturas del riesgo de crédito.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 3702, "n_consultas": 34, "top10": []}

  --- concepto_definido:loan_to_value_ltv (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "concepto_definido:loan_to_value_ltv",
 "type": "ConceptoDefinido",
 "label": "loan-to-value (LTV)",
 "properties": {
  "description": "Relación entre el saldo de deuda pendiente y el valor del inmueble utilizada en la evaluación de préstamos hipotecarios.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "Sección 2 > Sección 2 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 34, "top10": []}

  --- concepto_definido:saldo_de_deuda_en_sistema_financiero (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "concepto_definido:saldo_de_deuda_en_sistema_financiero",
 "type": "ConceptoDefinido",
 "label": "saldo de deuda en sistema financiero",
 "properties": {
  "description": "Deuda registrada del cliente en la Central de deudores a la fecha de otorgamiento.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 749, "n_consultas": 34, "top10": []}

  --- umbral:porcentaje_de_riesgo_de_incobrabilidad (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "umbral:porcentaje_de_riesgo_de_incobrabilidad",
 "type": "Umbral",
 "label": "porcentaje de riesgo de incobrabilidad",
 "properties": {
  "description": "Porcentaje aplicado sobre saldo de deuda según peor clasificación asignada.",
  "valor": "porcentaje según peor clasificación",
  "unidad": "%",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "Sección 6 > Punto 6.5"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 267, "n_consultas": 34, "top10": []}

  --- requisito:declaracion_jurada_de_saldo_de_deuda_pendiente (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "requisito:declaracion_jurada_de_saldo_de_deuda_pendiente",
 "type": "Requisito",
 "label": "declaración jurada de saldo de deuda pendiente",
 "properties": {
  "description": "Declaración jurada consignando el saldo de deuda pendiente a la fecha, para importaciones oficializadas con anterioridad al 01/11/19, firmada por el importador o su representante legal.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 10 > Sección 10 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 3510, "n_consultas": 34, "top10": []}

  --- requisito:declaracion_jurada_con_detalle_de_pagos_y_saldo_de_deuda (props) | expuesto en outputs de CQ-021: NO ---
{
 "id": "requisito:declaracion_jurada_con_detalle_de_pagos_y_saldo_de_deuda",
 "type": "Requisito",
 "label": "declaración jurada con detalle de pagos y saldo de deuda",
 "properties": {
  "description": "Documento que consigna el detalle de pagos realizados con imputación por la oficialización y el saldo de deuda pendiente.",
  "version": "vigente_2026-05"
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "Sección 11 > Anexo d > Sección 11 — preámbulo"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 1472, "n_consultas": 34, "top10": []}
  [barrido kg run_2: 'deudores comprendidos'] en id/label/properties: 0
  [barrido kg run_2: '3.4.2 (props)'] en id/label/properties: 0 | SOLO en provenances: 0

[1b] nodo(s) que soportaron el claim verdadero de los 45 días — identificación por exposición:
  ['45 dias'] exposición en outputs de run_2/CQ-021:
    paso 6 salientes[3] tiene_plazo→plazo:45_dias_de_realizada_la_reclasificacion
       …ias_de_realizada_la_reclasificacion", "vecino_label": "45 dias de realizada la reclasificacion", "provenances": [{"so…

  nodos fuente identificados: []

==============================================================================
2. run_4/CQ-008 (15 outputs re-ejecutables)
==============================================================================

[2a] barridos kg run_4 (exposición y D1 por candidato integrados):
  [barrido kg run_4: '10 dias'] en id/label/properties: 17

  --- reclamo_ante_sujeto_obligado (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "reclamo_ante_sujeto_obligado",
 "type": "procedimiento_regulatorio",
 "label": "Reclamo ante sujeto obligado",
 "properties": {
  "description": "Presentación formal de un reclamo por cobro indebido que inicia el plazo de 10 días hábiles para reintegro.",
  "version": "vigente",
  "type_raw": [
   "Procedimiento regulatorio"
  ],
  "type_raw_counts": {
   "Procedimiento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
   "location": "p.15-17 / Punto 2.3.5.1"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- ventas_de_titulos_valores_con_liquidacion_en_moneda_extranjera (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "ventas_de_titulos_valores_con_liquidacion_en_moneda_extranjera",
 "type": "operacion_de_cambios",
 "label": "Ventas de títulos valores con liquidación en moneda extranjera",
 "properties": {
  "description": "Ventas de títulos valores con liquidación en moneda extranjera en el país o en el exterior cuando los fondos obtenidos se utilicen dentro de 10 días corridos en operaciones específicas de endeudamiento o repatriación de inversiones.",
  "version": "vigente",
  "type_raw": [
   "Operación de cambios",
   "Operación excluida de declaración jurada"
  ],
  "type_raw_counts": {
   "Operación de cambios": 1,
   "Operación excluida de declaración jurada": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.43-46 / Punto 3.16.2.1, inciso vi)"
  },
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.47-49 / Punto 3.16.3.6, inciso iii)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 569, "n_consultas": 33, "top10": []}

  --- plazo_para_denuncia_de_incumplido (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "plazo_para_denuncia_de_incumplido",
 "type": "requisito_temporal_regulatorio",
 "label": "Plazo para denuncia de incumplido",
 "properties": {
  "description": "Período de 10 días hábiles contados a partir de la fecha de vencimiento del plazo para liquidación de divisas, dentro del cual debe realizarse la denuncia.",
  "version": "vigente",
  "type_raw": [
   "Requisito temporal regulatorio"
  ],
  "type_raw_counts": {
   "Requisito temporal regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.110-112 / Sección 8.4.5"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 33, "n_consultas": 33, "top10": []}

  --- certificacion_para_pago_con_deuda_exterior (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "certificacion_para_pago_con_deuda_exterior",
 "type": "documento_regulatorio",
 "label": "Certificación para pago con deuda exterior",
 "properties": {
  "description": "Certificación emitida por entidad financiera que habilita el pago de importaciones con deuda contraída en el exterior, con validez de 10 días hábiles desde su emisión.",
  "version": "vigente",
  "type_raw": [
   "Documento regulatorio"
  ],
  "type_raw_counts": {
   "Documento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.163-167 / Punto 11.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- plazo_de_validez_de_certificacion (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "plazo_de_validez_de_certificacion",
 "type": "parametro_regulatorio",
 "label": "Plazo de validez de certificación",
 "properties": {
  "description": "Período de 10 días hábiles contados desde la fecha de emisión durante el cual la certificación mantiene su validez.",
  "version": "vigente",
  "type_raw": [
   "Parámetro regulatorio"
  ],
  "type_raw_counts": {
   "Parámetro regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_exterior_cambios_actual.pdf",
   "location": "p.163-167 / Punto 11.1.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 32, "n_consultas": 33, "top10": []}

  --- operaciones_sin_margen_de_variacion (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "operaciones_sin_margen_de_variacion",
 "type": "categoria_de_operacion",
 "label": "Operaciones sin margen de variación",
 "properties": {
  "description": "Operaciones de derivados cuyo horizonte temporal mínimo es el menor entre un año y el plazo residual del contrato, con mínimo de 10 días hábiles, sujetas a factor de plazo.",
  "version": "vigente",
  "type_raw": [
   "Categoría de operación"
  ],
  "type_raw_counts": {
   "Categoría de operación": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.74-77 / Acápite vi) a)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- derivados_que_no_se_liquidan_en_forma_centralizada (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "derivados_que_no_se_liquidan_en_forma_centralizada",
 "type": "categoria_de_derivado",
 "label": "Derivados que no se liquidan en forma centralizada",
 "properties": {
  "description": "Operaciones de derivados sujetas a acuerdos de márgenes diarios con período de riesgo de margen mínimo de 10 días hábiles.",
  "version": "vigente",
  "type_raw": [
   "Categoría de derivado"
  ],
  "type_raw_counts": {
   "Categoría de derivado": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.74-77 / Acápite vi) b), primer punto de enumeración"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 56, "n_consultas": 33, "top10": []}

  --- margen_de_variacion (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "margen_de_variacion",
 "type": "garantia",
 "label": "Margen de variación",
 "properties": {
  "description": "Margen recibido por la CCP de una operación. El fragmento especifica que cuando el activo del miembro compensador no está protegido contra insolvencia de la CCP, se aplica un horizonte temporal mínimo de 10 días hábiles.",
  "version": "vigente",
  "type_raw": [
   "Garantía",
   "Mecanismo de garantía",
   "Requisito de Garantía"
  ],
  "type_raw_counts": {
   "Garantía": 1,
   "Mecanismo de garantía": 1,
   "Requisito de Garantía": 1
  },
  "name_variants": [
   "Margen de Variación",
   "Margen de variación"
  ],
  "n_observations": 3
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.86-88 / Punto 4.3.1.5"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.89-91 / Párrafo sobre margen de variación y protección de activos"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.92-95 / Párrafos sobre cálculo de EAD para SFT; punto 4.3.3.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- periodo_de_riesgo_de_margen_mpor (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "periodo_de_riesgo_de_margen_mpor",
 "type": "parametro_de_calculo_regulatorio",
 "label": "Período de riesgo de margen (MPOR)",
 "properties": {
  "description": "Período mínimo utilizado para calcular la exposición al riesgo de margen en conjuntos de neteo. El fragmento establece un MPOR mínimo de 10 días para exposiciones a una CCP por operaciones de derivados OTC.",
  "version": "vigente",
  "type_raw": [
   "Parámetro de cálculo regulatorio"
  ],
  "type_raw_counts": {
   "Parámetro de cálculo regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.89-91 / Párrafo inicial; punto sobre MPOR mínimo de 10 días"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 88, "n_consultas": 33, "top10": []}

  --- operacion_de_derivado_otc (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "operacion_de_derivado_otc",
 "type": "tipo_de_operacion_financiera",
 "label": "Operación de derivado OTC",
 "properties": {
  "description": "Operación de derivado negociada en mercado extrabursátil. El fragmento establece un MPOR mínimo de 10 días para el cálculo de exposiciones a una CCP por estas operaciones.",
  "version": "vigente",
  "type_raw": [
   "Tipo de operación financiera"
  ],
  "type_raw_counts": {
   "Tipo de operación financiera": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.89-91 / Párrafo sobre MPOR mínimo de 10 días"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- mpor (props) | expuesto en outputs de CQ-008: pasos [2, 3, 4, 5, 7, 8, 9, 10, 11, 12, 14] ---
{
 "id": "mpor",
 "type": "parametro_temporal",
 "label": "MPOR",
 "properties": {
  "description": "Período de mantenimiento mínimo de 10 días utilizado para calcular la exposición potencial futura de la CCP en operaciones con derivados.",
  "version": "vigente",
  "type_raw": [
   "Parámetro Temporal"
  ],
  "type_raw_counts": {
   "Parámetro Temporal": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.92-95 / Párrafo sobre cálculo de EAD para derivados; punto 4.3.3.2"
  }
 ]
}

  --- metodo_integral (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "metodo_integral",
 "type": "metodo_de_calculo",
 "label": "Método integral",
 "properties": {
  "description": "Método para calcular la cobertura del riesgo de crédito que utiliza aforos regulatorios basados en valuación diaria a precios de mercado y liquidación/reposición diaria de márgenes con período de mantenimiento de 10 días hábiles.",
  "version": "vigente",
  "type_raw": [
   "Método de cálculo",
   "Método de cobertura de riesgo de crédito"
  ],
  "type_raw_counts": {
   "Método de cálculo": 1,
   "Método de cobertura de riesgo de crédito": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.96-99 / Punto 5.1.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.107-111 / Punto 5.3.2.2 y 5.3.2.3"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- aforo_por_descalce_de_monedas (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "aforo_por_descalce_de_monedas",
 "type": "ajuste_de_aforo",
 "label": "Aforo por descalce de monedas",
 "properties": {
  "description": "Aforo adicional del 8% aplicado cuando la exposición y el activo recibido en garantía se encuentran denominados en monedas diferentes, basado en un período de mantenimiento de 10 días hábiles y valuación diaria a precios de mercado.",
  "version": "vigente",
  "type_raw": [
   "Ajuste de aforo",
   "Componente de cálculo"
  ],
  "type_raw_counts": {
   "Ajuste de aforo": 1,
   "Componente de cálculo": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.107-111 / Punto 5.3.2.3, acápite i)"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.112-115 / Definición de Hfx en operaciones de garantía"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- operaciones_de_derivados_over_the_counter_otc (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "operaciones_de_derivados_over_the_counter_otc",
 "type": "operacion_de_financiacion_con_titulos_valores",
 "label": "Operaciones de derivados over-the-counter (OTC)",
 "properties": {
  "description": "Operaciones realizadas en el mercado de capitales que requieren liquidación/reposición diaria de márgenes y un período de mantenimiento mínimo de 10 días hábiles.",
  "version": "vigente",
  "type_raw": [
   "Operación de financiación con títulos valores"
  ],
  "type_raw_counts": {
   "Operación de financiación con títulos valores": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.107-111 / Punto 5.3.2.3, acápite iv)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- operaciones_de_financiacion_con_margen (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "operaciones_de_financiacion_con_margen",
 "type": "operacion_de_financiacion_con_titulos_valores",
 "label": "Operaciones de financiación con margen",
 "properties": {
  "description": "Operaciones realizadas en el mercado de capitales que requieren liquidación/reposición diaria de márgenes y un período de mantenimiento mínimo de 10 días hábiles.",
  "version": "vigente",
  "type_raw": [
   "Operación de financiación con títulos valores"
  ],
  "type_raw_counts": {
   "Operación de financiación con títulos valores": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.107-111 / Punto 5.3.2.3, acápite iv)"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

  --- aforo_por_descalce_de_monedas_en_proteccion_crediticia (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "aforo_por_descalce_de_monedas_en_proteccion_crediticia",
 "type": "componente_de_calculo",
 "label": "Aforo por descalce de monedas en protección crediticia",
 "properties": {
  "description": "Aforo del 8% aplicado al descalce de monedas entre la protección crediticia y la exposición, suponiendo un período de mantenimiento de 10 días hábiles y valuación diaria a precios de mercado.",
  "version": "vigente",
  "type_raw": [
   "Componente de cálculo"
  ],
  "type_raw_counts": {
   "Componente de cálculo": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.112-115 / Punto 5.4.6"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 517, "n_consultas": 33, "top10": []}

  --- deficiencia_persistente (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "deficiencia_persistente",
 "type": "incumplimiento_regulatorio",
 "label": "Deficiencia persistente",
 "properties": {
  "description": "Defecto de integración de capital que se mantiene por un término superior a 10 días hábiles, requiriendo presentación de plan de regularización y saneamiento.",
  "version": "vigente",
  "type_raw": [
   "Incumplimiento regulatorio"
  ],
  "type_raw_counts": {
   "Incumplimiento regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.138-141 / Sección 6.7.2.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}
  [barrido kg run_4: 'solicitud ∧ clasificacion'] en id/label/properties: 0
  [barrido kg run_4: 'comunicar ∧ clasificacion'] en id/label/properties: 1

  --- deudor_en_gestion_judicial_o_extrajudicial_de_cobro (props) | expuesto en outputs de CQ-008: NO ---
{
 "id": "deudor_en_gestion_judicial_o_extrajudicial_de_cobro",
 "type": "categoria_de_deudor",
 "label": "Deudor en gestión judicial o extrajudicial de cobro",
 "properties": {
  "description": "Deudor respecto del cual se han iniciado gestiones de cobro judicial o extrajudicial, a quien deben comunicarse los cambios negativos en clasificación en la medida que cuente con notificaciones postales o fehacientes.",
  "version": "vigente",
  "type_raw": [
   "Categoría de deudor"
  ],
  "type_raw_counts": {
   "Categoría de deudor": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.9-12 / Punto 3.4.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": 28, "n_consultas": 33, "top10": []}
  [barrido kg run_4: 'central de deudores'] en id/label/properties: 1

  --- central_de_deudores_del_sistema_financiero (props) | expuesto en outputs de CQ-008: pasos [15] ---
{
 "id": "central_de_deudores_del_sistema_financiero",
 "type": "sistema_de_informacion",
 "label": "Central de deudores del sistema financiero",
 "properties": {
  "description": "Base de datos centralizada que registra información sobre clasificaciones de deudores asignadas por múltiples acreedores y es consultada para determinar recategorizaciones obligatorias.",
  "version": "vigente",
  "type_raw": [
   "Base de datos regulatoria",
   "Sistema de información",
   "Fuente de información"
  ],
  "type_raw_counts": {
   "Base de datos regulatoria": 1,
   "Sistema de información": 2,
   "Fuente de información": 1
  },
  "name_variants": [],
  "n_observations": 4
 },
 "provenances": [
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.17-19 / Sección 6, punto 6.4.2"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.29-32 / Punto 6.6"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.33-35 / Punto 7.1"
  },
  {
   "source_doc": "TO_clasificacion_deudores_actual.pdf",
   "location": "p.39-43 / Sección 7, punto 7.3"
  }
 ]
}
  [barrido kg run_4: '8.1 (props)'] en id/label/properties: 0 | SOLO en provenances: 17
    (> 12 candidatos: regla declarada — ids completos abajo; íntegros solo los que cruzan con 'solicitud|10 dias|clasificacion|central': 2)
    ids: ['sefyc', 'responsabilidad_patrimonial_computable', 'responsabilidad_patrimonial_computable_rpc', 'cliente', 'exigencia_por_riesgo_de_mercado', 'exigencia_por_riesgo_operacional', 'activos_ponderados_por_riesgo', 'exigencia_por_riesgo_de_credito_sin_incluir_el_termino_inc', 'calculo_del_riesgo_de_tasa_de_interes_en_la_cartera_de_inversion_medida_de_riesgo_eve_estandarizada', 'entidad_atipica', 'capital_minimo_basico', 'banco_comercial', 'fondo_de_garantia_de_sustentabilidad_del_sistema_integrado_previsional_argentino', 'letras_hipotecarias_escriturales', 'permiso_de_embarque', 'patrimonio_neto_basico_pnb', 'patrimonio_neto_complementario_pnc']

  --- entidad_atipica (SOLO provenance) | expuesto en outputs de CQ-008: pasos [10] ---
{
 "id": "entidad_atipica",
 "type": "clasificacion_de_entidad_financiera",
 "label": "Entidad atípica",
 "properties": {
  "description": "Entidad financiera cuya medida de riesgo EVE supera el 15% del nivel de capital 1, sujeta a medidas específicas por la SEFyC.",
  "version": "vigente",
  "type_raw": [
   "Clasificación de entidad financiera"
  ],
  "type_raw_counts": {
   "Clasificación de entidad financiera": 1
  },
  "name_variants": [],
  "n_observations": 1
 },
 "provenances": [
  {
   "source_doc": "TO_regimen_informativo_contable_mensual_actual.pdf",
   "location": "p.36-39 / Sección 8.1.2"
  }
 ]
}

  --- patrimonio_neto_basico_pnb (SOLO provenance) | expuesto en outputs de CQ-008: NO ---
{
 "id": "patrimonio_neto_basico_pnb",
 "type": "componente_de_capital",
 "label": "Patrimonio neto básico (PNb)",
 "properties": {
  "description": "Componente del capital regulatorio emitido por subsidiarias sujetas a supervisión consolidada que puede reconocerse en el PNb de la entidad financiera si observa todos los requisitos para su clasificación como PNb a efectos de la RPC.",
  "version": "vigente",
  "type_raw": [
   "Componente de capital",
   "Componente de capital regulatorio"
  ],
  "type_raw_counts": {
   "Componente de capital": 1,
   "Componente de capital regulatorio": 1
  },
  "name_variants": [],
  "n_observations": 2
 },
 "provenances": [
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.150-154 / Sección 8.1"
  },
  {
   "source_doc": "TO_capitales_minimos_actual.pdf",
   "location": "p.161-163 / Punto 8.3.5.2"
  }
 ]
}
    D1: {"alcanzable": false, "mejor_rank": null, "n_consultas": 33, "top10": []}

```
