# Calibración del juez v2.1.1 (dos pasos) — juez vs. humano

Juez: `claude-sonnet-4-6` (temp 0), arquitectura de DOS PASOS. Respondedor: `claude-haiku-4-5-20251001`. Input CIEGO al grafo.

correctitud y completitud se COMPUTAN determinísticamente a partir de la verificación afirmación-por-afirmación (Paso 2); no son un juicio holístico del LLM. v2.1: no_soportado NO baja correctitud; las afirmaciones centrales no_soportadas marcan la traza para adjudicación humana. Referente auditable = respuesta_esperada + cita_textual + ground_truth_secciones. Ver changelog en `judge.py`.

**Resultado: ✅ ÉXITO** (targets flipean + cero regresiones).

Celdas: `J:<juez> / H:<humano> ✅/❌`; `<juez> (—)` sin veredicto humano.

| qid | run | | correctitud | completitud | cita_doc | cita_prec | abst | espec | adj? | desac. |
|-----|-----|-|-------------|-------------|----------|-----------|------|-------|------|--------|
| CQ-001 | run_3 | ex-emb | J:correcta / H:correcta ✅ | J:completa / H:completa ✅ | True (—) | pagina (—) | None (—) | None (—) |  | — |
| CQ-009 | run_3 | ex-emb | J:correcta / H:correcta ✅ | completa (—) | True (—) | punto (—) | None (—) | None (—) |  | — |
| CQ-023 | run_3 |  | J:correcta / H:correcta ✅ | completa (—) | True (—) | punto (—) | None (—) | None (—) | ⚑ | — |
| CQ-029 | run_3 |  | J:correcta / H:correcta ✅ | J:parcial / H:parcial ✅ | True (—) | pagina (—) | None (—) | None (—) |  | — |
| CQ-032 | run_3 |  | J:correcta / H:correcta ✅ | J:completa / H:completa ✅ | True (—) | punto (—) | None (—) | None (—) |  | — |
| dev_unans_1 | run_3 |  | None (—) | None (—) | False (—) | ausente (—) | J:correcta / H:correcta ✅ | J:True / H:True ✅ |  | — |
| CQ-001 | run_1 |  | J:correcta / H:correcta ✅ | J:completa / H:completa ✅ | True (—) | pagina (—) | None (—) | None (—) |  | — |
| CQ-009 | run_1 |  | J:incorrecta / H:incorrecta ✅ | parcial (—) | True (—) | pagina (—) | None (—) | None (—) |  | — |
| CQ-023 | run_1 |  | J:correcta / H:correcta ✅ | completa (—) | True (—) | pagina (—) | None (—) | None (—) | ⚑ | — |
| CQ-029 | run_1 | ex-emb | J:correcta / H:correcta ✅ | J:parcial / H:parcial ✅ | True (—) | pagina (—) | None (—) | None (—) |  | — |
| CQ-032 | run_1 |  | J:correcta / H:correcta ✅ | J:completa / H:completa ✅ | True (—) | pagina (—) | None (—) | None (—) |  | — |
| dev_unans_1 | run_1 |  | None (—) | None (—) | False (—) | ausente (—) | J:correcta / H:correcta ✅ | J:False / H:False ✅ |  | — |

`adj?` ⚑ = la traza tiene ≥1 afirmación CENTRAL no_soportada por el referente → requiere adjudicación humana contra los PDFs.
`ex-emb` = fue ejemplo embebido en v1.2; en v2.0 no hay few-shot, se marca solo por transparencia.

## Criterio de éxito y regresiones

Targets que debían flipear a coincidir con el humano:
- ✅ CQ-023/run_3/correctitud: obtenido `correcta` (esperado `correcta`)
- ✅ CQ-023/run_1/correctitud: obtenido `correcta` (esperado `correcta`)
- ✅ dev_unans_1/run_3/especulacion_en_prosa: obtenido `True` (esperado `True`)

**Sin regresiones**: todas las celdas que coincidían en v1.2 siguen coincidiendo.

## Trazabilidad (descomposición y verificación por traza)

**CQ-001 / run_3** — corr=correcta, compl=completa, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=0 | requiere_adjudicacion_humana=False
- [central/verdadero] El plazo para revocar la aceptación de un producto o servicio financiero contratado es de diez (10) días hábiles.
- [central/verdadero] El plazo se cuenta a partir de la fecha de recibido el contrato o de la disponibilidad efectiva del producto o servicio.
- (pata/cubierta) plazo para revocar la aceptación de un producto o servicio contratado por un usuario de servicios financieros
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Todas las patas cubiertas.
- *citas*: La cita apunta al documento correcto (TO_proteccion_usuarios_servicios_financieros_actual.pdf) pero solo a nivel de sección amplia ('Punto 2.3'), sin precisar el acápite exacto (Punto 2.3.1.1, acápite v).

**CQ-009 / run_3** — corr=correcta, compl=completa, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=0 | requiere_adjudicacion_humana=False
- [central/verdadero] El criterio básico para clasificar a un deudor de la cartera comercial es la capacidad de pago en el futuro de la deuda o de los compromisos objeto de la garantía de la entidad financiera.
- (pata/cubierta) Criterio básico para clasificar a un deudor de la cartera comercial
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Todas las patas cubiertas.
- *citas*: La cita apunta al documento correcto (TO_clasificacion_deudores_actual.pdf) a nivel de punto, aunque referencia el Punto 4.1 en lugar de los Puntos 4.2 o 6.2 indicados en el ground truth.
- (nota humana: buena, pero cita de sección imprecisa (4.1 vs 4.2))

**CQ-023 / run_3** — corr=correcta, compl=completa, abst=None, espec=None
- no_soportadas: centrales=1, secundarias=5 | requiere_adjudicacion_humana=True
  · centrales no_soportadas: ['El PNc se calcula como: PNc = 70250000 – 70260000.']
  · **adjudicación humana: RESUELTA por la revisora (09/06): las 3 afirmaciones centrales no_soportadas son TEXTUALES del TO de Régimen Informativo Contable Mensual — RPC = 70200000 en la Sección 8; PNb y PNc con sus fórmulas literales en las Secciones 6/8. Las 3 son VERDADERAS. La marca requiere_adjudicacion_humana=True funcionó como se diseñó.**
- [central/verdadero] La RPC se compone de dos elementos: el Patrimonio Neto Básico (PNb) y el Patrimonio Neto Complementario (PNc).
- [secundaria/no_soportado] La RPC debe ser mayor o igual al 8% de los Activos Ponderados por Riesgo (APR).
- [secundaria/no_soportado] La RPC = 70200000 (código contable).
- [central/verdadero] El PNb se integra mediante la fórmula: PNb = 70210000 – 70220000 + 70230000 – 70240000.
- [secundaria/no_soportado] El PNb debe representar como mínimo el 6% de los APR.
- [central/verdadero] El PNb incluye partidas de capital ordinario de nivel 1, con deducciones y adiciones específicas.
- [central/no_soportado] El PNc se calcula como: PNc = 70250000 – 70260000.
- [secundaria/no_soportado] La RPC se determina en función de los saldos de las partidas admitidas registrados al último día del mes bajo informe.
- [secundaria/no_soportado] La integración de los componentes de la RPC es mensual.
- (pata/cubierta) Composición de la Responsabilidad Patrimonial Computable (RPC)
- (pata/cubierta) Qué integra el Patrimonio Neto Básico (PNb)
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Todas las patas cubiertas.
- *citas*: El agente cita TO_capitales_minimos_actual.pdf a nivel de punto, que corresponde al ground truth; la cita al régimen informativo contable es adicional y no lo anula.
- (nota humana: aceptable; baja legibilidad (códigos contables))

**CQ-029 / run_3** — corr=correcta, compl=parcial, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=3 | requiere_adjudicacion_humana=False
- [central/verdadero] No pueden cobrarse comisiones ni cargos por operaciones realizadas por ventanilla a usuarios que sean personas humanas.
- [secundaria/verdadero] Esta prohibición está establecida en la regulación del BCRA.
- [secundaria/no_soportado] La prohibición se extiende a operaciones realizadas en casas operativas distintas a aquella en la cual esté abierta la cuenta.
- [secundaria/no_soportado] La extensión de la prohibición aplica específicamente para movimientos de fondos en efectivo en pesos (depósitos y/o extracciones).
- [secundaria/no_soportado] La extensión de la prohibición aplica para la recepción de depósitos de cheques efectuados por cuenta propia y/o de terceros.
- (pata/cubierta) ¿Pueden cobrarse comisiones o cargos por operaciones realizadas por ventanilla a usuarios que son personas humanas?
- (pata/no_cubierta) ¿Hay excepciones a esa regla?
- reportes_de_alcance: ['No se encontraron excepciones documentadas a esta prohibición en la regulación consultada.']
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Patas no cubiertas: ¿Hay excepciones a esa regla?
- *citas*: La cita apunta al documento correcto (TO_proteccion_usuarios_servicios_financieros_actual.pdf) pero solo a nivel de sección general ('Punto 2.3'), sin precisión de punto específico (2.3.2.2).

**CQ-032 / run_3** — corr=correcta, compl=completa, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=0 | requiere_adjudicacion_humana=False
- [central/verdadero] En un crédito cedido a favor de la entidad sin responsabilidad para el cedente, el crédito se imputa al firmante, librador, deudor, codeudor o aceptante de los respectivos instrumentos.
- [central/verdadero] Si no se realiza la evaluación del deudor (cualquiera sea el motivo), los clientes se clasificarán en categoría irrecuperable.
- (pata/cubierta) A quién se imputa el crédito cedido a favor de la entidad sin responsabilidad para el cedente para clasificarlo
- (pata/cubierta) Qué ocurre si no se realiza la evaluación del deudor
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Todas las patas cubiertas.
- *citas*: La cita apunta al documento correcto (TO_clasificacion_deudores_actual.pdf) con precisión a nivel punto (Punto 1.2), consistente con el ground truth Punto 1.2.1.

**dev_unans_1 / run_3** — corr=None, compl=None, abst=correcta, espec=True
- no_soportadas: centrales=0, secundarias=0 | requiere_adjudicacion_humana=False
- (pata/no_cubierta) Porcentaje mínimo de previsión por riesgo de incobrabilidad para deudores clasificados en situación 'Irrecuperable'
- reportes_de_alcance: ["No se encontró en el Knowledge Graph la información específica sobre el porcentaje mínimo de previsión por riesgo de incobrabilidad para deudores clasificados en situación 'Irrecuperable'.", "El grafo contiene referencias al documento 'TO_clasificacion_deudores_actual.pdf' y menciones a esta categoría.", 'No se accedió a la tabla de previsiones del punto 6.5 que especificaría estos porcentajes.']
- *citas*: El agente no presenta citas a ningún documento del ground truth.
- *abstencion*: El agente no inventa porcentajes ni valores, pero especula sobre la existencia de una 'tabla de previsiones del punto 6.5' que no está verificada en el referente.

**CQ-001 / run_1** — corr=correcta, compl=completa, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=0 | requiere_adjudicacion_humana=False
- [central/verdadero] El plazo para revocar la aceptación de un producto o servicio contratado es de diez días hábiles.
- [secundaria/verdadero] La revocación debe estar contemplada en una cláusula del contrato de productos y servicios financieros.
- [secundaria/verdadero] El usuario puede ejercer la revocación sin costo si no ha utilizado el producto o servicio.
- (pata/cubierta) Plazo dentro del cual un usuario de servicios financieros puede revocar la aceptación de un producto o servicio contratado
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Todas las patas cubiertas.
- *citas*: La cita apunta al documento correcto (TO_proteccion_usuarios_servicios_financieros_actual.pdf) pero solo a nivel de página, sin identificar el punto/sección específico (Punto 2.3.1.1, acápite v)).

**CQ-009 / run_1** — corr=incorrecta, compl=parcial, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=2 | requiere_adjudicacion_humana=False
- [central/falso] El criterio básico para clasificar a un deudor de la cartera comercial es el atraso en pago
- [central/falso] El atraso en pago se mide en número de días de demora en la cancelación de obligaciones
- [secundaria/no_soportado] Atrasos de hasta 31 días son compatibles con una clasificación de situación normal
- [secundaria/no_soportado] Atrasos mayores a 180 días clasifican al deudor en la categoría de riesgo alto
- (pata/no_cubierta) criterio básico para clasificar a un deudor de la cartera comercial
- *correctitud*: Afirmación central falsa: El criterio básico para clasificar a un deudor de la cartera comercial es el atraso en pago; El atraso en pago se mide en número de días de demora en la cancelación de obligaciones
- *completitud*: Patas no cubiertas: criterio básico para clasificar a un deudor de la cartera comercial
- *citas*: El agente cita el documento correcto (TO_clasificacion_deudores_actual.pdf) pero solo a nivel de página, sin precisión de punto/sección.

**CQ-023 / run_1** — corr=correcta, compl=completa, abst=None, espec=None
- no_soportadas: centrales=6, secundarias=0 | requiere_adjudicacion_humana=True
  · centrales no_soportadas: ['El Capital Ordinario de Nivel Uno (COn1) incluye capital social', 'El Capital Ordinario de Nivel Uno (COn1) incluye reservas de utilidades', 'El Capital Ordinario de Nivel Uno (COn1) incluye resultados no asignados', 'El Patrimonio Neto Complementario comprende instrumentos de la entidad financiera que observan requisitos específicos', 'El Patrimonio Neto Complementario comprende primas de emisión', 'El Patrimonio Neto Complementario comprende previsiones por riesgo de incobrabilidad']
- [central/verdadero] La RPC se compone de dos elementos principales: Patrimonio Neto Básico (PNb) y Patrimonio Neto Complementario (PNc)
- [central/verdadero] El Patrimonio Neto Básico (PNb) es el capital de nivel uno
- [central/verdadero] El Patrimonio Neto Básico integra el Capital Ordinario de Nivel Uno (COn1)
- [central/no_soportado] El Capital Ordinario de Nivel Uno (COn1) incluye capital social
- [central/no_soportado] El Capital Ordinario de Nivel Uno (COn1) incluye reservas de utilidades
- [central/no_soportado] El Capital Ordinario de Nivel Uno (COn1) incluye resultados no asignados
- [central/verdadero] El Patrimonio Neto Complementario (PNc) es el capital de nivel dos
- [central/no_soportado] El Patrimonio Neto Complementario comprende instrumentos de la entidad financiera que observan requisitos específicos
- [central/no_soportado] El Patrimonio Neto Complementario comprende primas de emisión
- [central/no_soportado] El Patrimonio Neto Complementario comprende previsiones por riesgo de incobrabilidad
- [central/verdadero] El PNb se calcula como Capital Ordinario menos deducciones más Capital Adicional menos sus deducciones
- (pata/cubierta) Composición de la Responsabilidad Patrimonial Computable (RPC)
- (pata/cubierta) Qué integra el Patrimonio Neto Básico
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Todas las patas cubiertas.
- *citas*: Las citas apuntan al documento correcto (TO_capitales_minimos_actual.pdf) pero solo a nivel de página, sin identificar los puntos 8.1 o 8.2.1 del referente.

**CQ-029 / run_1** — corr=correcta, compl=parcial, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=2 | requiere_adjudicacion_humana=False
- [central/verdadero] El BCRA prohíbe cobrar comisiones o cargos por operaciones realizadas por ventanilla a usuarios que son personas humanas.
- [secundaria/no_soportado] La prohibición se extiende a movimientos de fondos en efectivo en pesos realizados por personas humanas.
- [secundaria/no_soportado] La prohibición se extiende a depósitos de cheques realizados por personas humanas.
- (pata/cubierta) Si pueden cobrarse comisiones o cargos por operaciones realizadas por ventanilla a usuarios que son personas humanas
- (pata/no_cubierta) Excepciones a esa regla
- reportes_de_alcance: ['No se identificaron excepciones a esta prohibición en la regulación disponible.']
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Patas no cubiertas: Excepciones a esa regla
- *citas*: La cita apunta al documento correcto (TO_proteccion_usuarios_servicios_financieros_actual.pdf) pero solo a nivel de página, sin identificar el punto 2.3.2.2.
- (nota humana: mejor que R3 por hedge explícito)

**CQ-032 / run_1** — corr=correcta, compl=completa, abst=None, espec=None
- no_soportadas: centrales=0, secundarias=0 | requiere_adjudicacion_humana=False
- [central/verdadero] En un crédito cedido a favor de la entidad sin responsabilidad para el cedente, el crédito se imputa a los firmantes, libradores, deudores o aceptantes del instrumento cedido.
- [central/verdadero] Los firmantes, libradores, deudores o aceptantes del instrumento cedido son considerados como principales y directos pagadores.
- [central/verdadero] Si no se realiza la evaluación del deudor como sujeto de crédito, sea cual fuere el motivo, se asigna obligatoriamente la clasificación de Categoría Irrecuperable.
- (pata/cubierta) A quién se imputa el crédito cedido sin responsabilidad para el cedente a efectos de su clasificación
- (pata/cubierta) Qué ocurre si no se realiza la evaluación del deudor
- *correctitud*: Centrales todas verdaderas o no_soportadas; ninguna afirmación falsa.
- *completitud*: Todas las patas cubiertas.
- *citas*: La cita apunta al documento correcto (TO_clasificacion_deudores_actual.pdf) pero solo a nivel de página (p. 4), sin identificar el punto específico (Punto 1.2.1).

**dev_unans_1 / run_1** — corr=None, compl=None, abst=correcta, espec=False
- no_soportadas: centrales=0, secundarias=0 | requiere_adjudicacion_humana=False
- (pata/no_cubierta) Porcentaje mínimo de previsión por riesgo de incobrabilidad para deudores clasificados en situación 'Irrecuperable'
- reportes_de_alcance: ["No se encontró en el Knowledge Graph la información específica sobre el porcentaje mínimo de previsión por riesgo de incobrabilidad para deudores clasificados como 'Irrecuperable'.", "Existen referencias a 'Previsiones mínimas por riesgo de incobrabilidad' como régimen normativo del BCRA en los nodos consultados.", 'La tabla o anexo que especifique los porcentajes por categoría de clasificación no está disponible en los nodos consultados.']
- *citas*: El agente no presenta ninguna cita.
- *abstencion*: El agente declara correctamente que la información no está disponible en los nodos consultados, sin inventar porcentajes ni citas, lo que es consistente con respondible=false.
