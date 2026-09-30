# U-LECTURA-LIMITA · L1 — Lectura asistida de la muestra sellada de 30 aristas `limita`

**Lectura asistida**: la hizo una instancia de modelo. La revisión de la autora
está PENDIENTE y queda fuera de la unidad; ver «Desvío declarado». Mandato:
`docs/mandatos/ULECTURA_LIMITA_lectura_asistida.md` (firmado en `67a9e6b`).
USD 0: ningún script llama a la API y Neo4j no se usa. Plan, fila B2.11,
unidad 4b (`docs/plan_tesis.md:393`). Las anclas al plan de este reporte valen
igual en `67a9e6b`, HEAD al inicio, y en `9e411a0`, HEAD al cierre: hubo
commits de la autora en paralelo (`git show <sha>:docs/plan_tesis.md`).

## Fuentes

- Planilla sellada: `reports/u_umbral/muestra_limita_30.csv`, sellada en
  `e4d053b`, sha256 `8e9818173100ac880c7bdc34121a4f4e66916e42b16636421f5e4e993512b2a9`.
  Verifiqué el sha al inicio y al cierre (`shasum -a 256`), y el script lo
  verifica en cada corrida. La planilla no se editó.
- Población y sorteo: 284 aristas `limita` de KG-Tanda0-Desarrollo-r1
  (`reports/u_umbral/u2_muestra_trazas.md:45`, grafo en `:15`); procedimiento
  D-SORTEO (`:23`); planilla y columna vacía (`:47`).
- Copia de trabajo con la lectura: `lectura_limita_30.csv` (este directorio),
  con las 14 columnas de la planilla sin cambios más `veredicto`,
  `justificación`, `destino_esperado` y `revision_autora` (vacía). La columna de
  la planilla «el destino es el objeto del tope (sí / no / no decidible)» sigue
  vacía, como en la planilla sellada. El veredicto va en `veredicto`.

## Regla y cómo la apliqué

Regla fija, del mandato (decisión 3):
- «sí»: según el texto de E0, la Operacion es el acto o la magnitud que el
  tope de la Restriccion acota;
- «no»: el texto acota otra cosa, o la Operacion no aparece en la cláusula del
  tope;
- «no decidible»: el texto de la planilla no alcanza.

Leí solo las columnas de la planilla: descripción, `umbral` y labels de los
dos nodos, y texto de E0 propio y heredado.

Declaré una precisión de término después de ver las filas 1 a 5 y antes de
anotar el primer veredicto: «tope» es la limitación que fija la Restriccion.
Puede ser un monto o porcentaje máximo, un ponderador, un plazo o un mínimo, un
umbral de encuadre, o una exclusión o condición cualitativa.

Resolví todos los casos con el mismo criterio. Es «sí» cuando la Operacion es
la operación que lleva el acto o la magnitud acotada, aunque un calificativo
(etapa, calificación, plazo) quede en la Restriccion. Es «no» cuando la
Operacion resulta ser otra cosa:
- la base de la comparación (fila 13);
- el fin del tope (9);
- la consecuencia (20 y 25);
- el supuesto que habilita la imputación (14);
- otro objeto (7);
- la modalidad que la cláusula no acota (17).

No es un ajuste de la regla: lo dejo explícito para la revisión.

Cada justificación cita entre «» tramos del texto de E0. Verifiqué que los 48
tramos de las 30 justificaciones son subcadenas literales del texto de E0 de su
fila, uniendo los cortes de palabra con guion y los saltos de línea. Es un
control de una sola vez, en el scratchpad: no es parte del script.

## Conteos (lectura asistida)

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/lectura_limita/conteo_lectura.py
```

| Veredicto | Filas |
|---|---|
| sí | 21 |
| no | 7 |
| no decidible | 2 |
| **total** | **30** |

Intervalo de Wilson al 95 % para «sí» (z = 1,959963984540054, la misma
constante que `reports/tanda0/obs12_lectura/fila_obs12.md`, «Reproducción»):
- sobre los 30: 21 / 30 = 0,700; IC 95 % **0,521–0,833**;
- sobre los 28 decididos: 21 / 28 = 0,750; IC 95 % **0,566–0,873**.

Son fracciones sobre n = 30, de una sola muestra de un solo grafo. Los
controles del script (encabezado, 30 filas en orden, mismos `n_sorteo`,
`restriccion_id` y `operacion_id`, columnas de la planilla sin cambios,
veredictos válidos, destino solo en los «no») dan OK. La doble corrida da el
mismo texto byte a byte.

## Los «no» (7)

| n_sorteo | Índice | Restriccion → Operacion (labels) | Chunk | Justificación | Destino esperado |
|---|---|---|---|---|---|
| 7 | 11 | Ponderador 1250% — compromisos no desembolsados CCP no calificadas → Cálculo exigencia capital — exposiciones CCP no calificadas | `cap::4.3.4` | El 1250% se aplica «a sus aportes a los fondos de garantía para incumplimientos de las CCP que no califican» y a «los compromisos no desembolsados»; para las exposiciones por operaciones de negociación, que son la Operacion, el texto manda «considerar a estas CCP como entidades financieras». | Los compromisos no desembolsados con las CCP que no califican, cuyo importe determina la SEFYC. |
| 9 | 141 | Límite 0,2% concentración individual → Diversificación de cartera minorista | `cap::2.8.3.2` | El 0,2% acota «la exposición total con cada contraparte individual»; la Operacion nombra la diversificación de la cartera, que es el fin del tope («La cartera deberá estar diversificada. A tal efecto»), no lo que el tope acota. | La exposición total con cada contraparte individual dentro de las exposiciones minoristas normativas de la entidad. |
| 13 | 20 | Límite de cómputo de fondos — mecanismos con valor pendiente → Financiación computada como ingresada y liquidada | `ext::14.5.2` | El tope acota la disponibilidad de «cualquier mecanismo previsto en las normas cambiarias que tome en consideración el valor pendiente del endeudamiento»; los fondos computados como ingresados y liquidados, que son la Operacion, son la base de la proporción («hasta la proporción de los fondos recibidos por la financiación»). | El uso por el VPU de los mecanismos cambiarios que toman en consideración el valor pendiente del endeudamiento y/o el valor de las próximas cuotas de capital o intereses. |
| 14 | 254 | Imputación limitada al monto proporcional FOB → Reimportación mercadería rechazada en destino | `ext::8.5.6` | El tope fija hasta qué monto «La entidad podrá considerar cumplimentado parcial o totalmente el seguimiento de un permiso de embarque» («Por hasta el monto proporcional»); la reimportación, que es la Operacion, es el supuesto que habilita la imputación, no lo acotado. | La imputación al cumplimiento del seguimiento del permiso de embarque de la exportación rechazada y reimportada. |
| 17 | 272 | Tope USD 100 mensual efectivo con declaración jurada → Compra moneda extranjera billetes depósitos débito cuenta | `ext::3.8.1` | El tope rige «Si el cliente utiliza efectivo»; la Operacion es la compra cursada «con débito en cuenta del cliente», la modalidad que el punto exige y que la cláusula del tope no acota. | La compra de moneda extranjera (códigos A07 y A09) por personas humanas residentes cursada con efectivo. |
| 20 | 192 | Plazo de cancelación — adelantos sector público no financiero → Asistencia crediticia otorgada en el mes | `cap::8.4.1.16` | El plazo de cancelación se refiere a «los adelantos previstos en el punto 3.2.5.»; la Operacion, «El mayor saldo de la asistencia crediticia otorgada en el mes», es el concepto deducible que se computa cuando los adelantos no se cancelan a tiempo, no lo que el plazo acota. | Los adelantos previstos en el punto 3.2.5. de las normas sobre Financiamiento al sector público no financiero. |
| 25 | 124 | Umbral deuda 2,5% — clasificación irrecuperable → Clasificación irrecuperable — clientes sector privado | `cla::6.5.5.9` | El 2,5% se compara con la «deuda (por todo concepto) más el importe de la financiación solicitada» del cliente; la Operacion, la clasificación en irrecuperable, es la consecuencia del encuadre y no la magnitud acotada. | La financiación solicitada por clientes del sector privado no financiero (su deuda por todo concepto más el importe solicitado, al momento del otorgamiento). |

## Los «no decidible» (2)

| n_sorteo | Índice | Restriccion → Operacion (labels) | Chunk | Justificación |
|---|---|---|---|---|
| 27 | 258 | Límite del 14 % — período 1-12 meses → Reducción de exigencia por riesgo operacional | `ric::5.2.5` | El chunk es una lista de códigos linealizada que solo nombra la partida «reducción por aplicación del límite del 14%»; no dice qué magnitud acota el límite, y define el período (X) y el límite (Y) como referencias separadas. |
| 30 | 262 | Límite del 7 % — período 1-12 meses → Reducción de exigencia por riesgo operacional | `ric::5.2.5` | El chunk es una lista de códigos linealizada que solo nombra la partida «reducción por aplicación del límite del 7 %»; no dice qué magnitud acota el límite, y define el período (X) y el límite (Y) como referencias separadas. |

## Casos límite, para la revisión

En estas seis filas el veredicto depende de una lectura estrecha. La
justificación de cada una está en la copia:
- 8, «sí»: lo acotado es el monto que resulta de usar los mecanismos del 7.9 en
  las operaciones de la Operacion, no la operación entera;
- 9, «no»: la Operacion nombra la diversificación de la cartera minorista, no
  la exposición por contraparte;
- 14, «no»: la reimportación habilita una imputación sobre otro permiso;
- 17, «no»: la Operacion es la compra con débito en cuenta, y el tope rige la
  compra en efectivo;
- 20, «no»: la asistencia del mes es lo que se deduce, y los adelantos son lo
  que se debe cancelar;
- 21, «sí»: el tope suma también otras financiaciones del mismo deudor.

Las filas 6, 10, 11 y 29 tienen tablas linealizadas. Las decidí por el título
del punto, que nombra el objeto. La correspondencia de cada ponderador con su
calificación sale de leer las columnas en orden.

## Observaciones fuera de la regla (no entran en los conteos)

Surgieron al leer y no cambian ningún veredicto. No propongo cambios (decisión
4 del mandato):
- **Fila 25.** La descripción de la Restriccion dice «no deberá exceder». El
  texto no prohíbe: fija un umbral de encuadre para clasificar en irrecuperable
  («cuya deuda (por todo concepto) más el importe de la financiación
  solicitada»).
- **Fila 26.** La descripción de la Restriccion habla del «20% … de obligación
  de ingreso». El texto dice lo contrario: el 20 % es la porción exceptuada
  («quedarán exceptuadas de la obligación de ingreso y/o liquidación del
  contravalor en divisas por un porcentaje del valor percibido»).
- **Fila 29.** La descripción de la Operacion asigna 0 % a «Inferior a B-».
  Leída en orden de columnas, la tabla linealizada da 150 para esa columna.
- **Filas 27 y 30.** La Restriccion asocia el límite a «meses 1 a 12». El texto
  define el período y el límite como referencias separadas del código.

## Desvío declarado

- **Quién leyó.** La lectura no es humana. La hizo la instancia de modelo que
  ejecutó esta unidad, el 30/09/2026 (comando `date`, 14:18 -03 al inicio).
  La revisión de la autora está PENDIENTE: si cambia algún veredicto, lo anota
  en `revision_autora` y la mesa registra el resultado final. El resultado se
  rotula «lectura asistida» en todo artefacto de la unidad.
- **Modelo y versión.** Claude Opus 5.5, identificador `claude-opus-5-5`. Es la
  declaración de la propia instancia a partir de su contexto de sistema de
  esta sesión. Ningún artefacto del repo la respalda: NO VERIFICADA, a
  confirmar por la autora.
- **Material leído antes de la lectura.** Leí lo que el mandato pide y, para
  verificar sus anclas, `docs/plan_tesis.md:385-400`. Esa zona del plan
  (`:397`, unidad 8) nombra como tablas no detectadas por E0 tres chunks de la
  muestra: `cap::2.12.2.5` (fila 11), `cap::2.12.2.8` (fila 10) y
  `cap::2.12.3.2` (fila 6). No usé ese dato para decidir: los veredictos de
  esas filas se apoyan en el título del punto. No consulté el grafo, otras
  unidades ni EV2.
- **Precisión de término.** La precisión de «tope» y los criterios de la
  sección «Regla y cómo la apliqué» son de la instancia. La autora los revisa
  junto con los veredictos.

## Reproducción

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/lectura_limita/conteo_lectura.py
shasum -a 256 reports/u_umbral/muestra_limita_30.csv reports/u_umbral/lectura_limita/lectura_limita_30.csv
```
