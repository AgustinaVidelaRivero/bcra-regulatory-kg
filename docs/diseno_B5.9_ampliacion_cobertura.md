# Diseño B5.9 — Ampliación de cobertura a los bloques excluidos (A y B)

**Estado: APROBADO por la autora — 07/09/2026**, con las tres enmiendas de su laudo aplicadas (alcance del bloque A en diez documentos / 41 páginas; desacople de secuencia; modelo de procedencia laudado con conteo exigido). La fase A.1 no gasta API; ninguna extracción arranca sin el mandato de su fase. Origen:
laudo de la autora del 07/09 (adenda 2 al laudo B5.5,
`docs/adenda2_laudo_B5.5_cobertura.md`, pendiente de firma), motivado por
la evidencia de U-COB-EXCL / U-COB-EXCL-2 (instrumento deóntico corregido
por el futuro impersonal: 5,58× → 1,56×; lectura a ciegas de 32 páginas
con pre-registro sellado: 23 prescriptivo / 9 referencia / 0 duda; diez de
los doce no segmentables contienen contenido prescriptivo).

## §0. La cuenta del alcance (recomputada contra `particion_152.json`)

| bloque | TOs | páginas | unidades hoy |
|---|--:|--:|--:|
| **A — extracción (enmienda 1 de la autora)** | **10** | **41** | 10 (una degenerada por documento) |
| A — declarados referencia, NO se extraen | 2 | 120 | 2 |
| **B — bloque ficha de los 2 parciales** | 2 | **2.175** (manual 1.830 + ri2_pm 345) | 0 (fuera del parseo de prosa) |
| (referencia) reconocidos plenos | 138 | 4.183 | 9.266 |
| (referencia) parciales, páginas totales | 2 | 2.413 | 46 (sus preámbulos) |

### §0.1 Los diez del bloque A, con la cuenta mostrada (regla i)

Enmienda 1 de la autora (07/09): `optico` (43 pág) y `plandecuentas`
(77 pág) **ya están adjudicados** por su lectura a ciegas como referencia
pura, y son exactamente los dos con densidad deóntica **0,000** en las
tres variantes del instrumento. No se redescubren en A.1 ni esperan al
cierre de B: **se censan para el registro y se DECLARAN referencia; no se
extraen.** `plandecuentas` es además material ficha (76 de sus 77
páginas), de modo que esta enmienda resuelve su caso y no la herencia
del bloque B.

| TO | páginas |
|---|--:|
| `ri_con` | 16 |
| `ri_spi` | 11 |
| `ri_tii` | 6 |
| `ri_rem` | 2 |
| `ri_chr` | 1 |
| `ri_fcem` | 1 |
| `ri_itme` | 1 |
| `ri_pfmipyme` | 1 |
| `ri_pscpp` | 1 |
| `ri_pspii` | 1 |
| **total (10)** | **41** |

Control: 161 − 43 − 77 = 41, recomputado contra `particion_152.json`
(coincide). **Proyección de costo recalculada**: 41 páginas × 1,38
unidades/página = **57 unidades** × 0,019437 USD/unidad = **USD 1,10** —
proyección por densidad, no medición; A.1 la reemplaza por el conteo
real. Reemplaza los USD 4,3 de la versión anterior de este diseño.

**Hallazgo del recomputo, a resolver en el diseño:** las páginas con rol
`ficha_registro` en el corpus son **2.281**, no 2.175. Las 106 restantes
están en `plandecuentas` (76 — que además es uno de los 12 del bloque A),
`ri_laft` (27) y `ri_transpa` (3), estos dos hoy reconocidos plenos. El
laudo define el bloque B como el de los dos parciales; el diseño lo
respeta y propone que esas 106 páginas se traten **por herencia**: si el
modelo de unidad-ficha del bloque B se valida, aplicarlo a ellas es
marginal y se lauda al cierre de B, no antes.

## §1. Los dos bloques NO son el mismo problema

Es la decisión de diseño más importante y conviene declararla primero.

- **Bloque A** es *prosa sin numeración*: el contenido es normativo y
  legible como texto corrido; lo que falta es la **espina** que da
  direcciones. Riesgo bajo, volumen chico, valor alto (es normativa
  vigente que el recurso excluiría). Su problema es de **procedencia**.
- **Bloque B** es *material tabular de registro* (planillas de cuentas,
  fichas por partida): su unidad natural no es el párrafo sino la fila o
  el bloque de campos. Riesgo alto, volumen desconocido y potencialmente
  dominante, y valor a demostrar. Su problema es de **modelo de datos y
  de balance del recurso**.

Consecuencia: **dos unidades separadas, con secuencia y frenos propios**.
No se mandatan juntas.

## §2. Guarda 3 — modelo de unidad y procedencia (bloque A)

La tesis afirma hoy, en la Introducción y en el capítulo del esquema, que
cada elemento del grafo registra **el punto** del texto oficial del que
proviene. Los 12 documentos del bloque A **no tienen punto**. El diseño
propone, para laudo explícito de la autora (guarda 3):

- **Unidad de extracción**: bloque de prosa contiguo dentro de una
  página, delimitado mecánicamente (líneas en blanco / cambio de bloque
  de layout), con la página como contenedor. Sin numeración inventada:
  **no se fabrica una espina que el documento no tiene.**
- **Procedencia**: `documento + página` (y offset del bloque dentro de la
  página, para reproducibilidad), con un campo explícito
  `granularidad_procedencia` que distinga `punto` (los 140 TOs con
  espina) de `pagina` (estos 12).
- **Consecuencia para la tesis, a escribir y no absorber**: la afirmación
  pasa de «cada elemento cita el punto exacto» a «cada elemento cita su
  ubicación en el texto oficial, con la granularidad que el documento
  permite: el punto donde hay numeración, la página donde no la hay». El
  campo hace la diferencia **medible y declarable por documento**, que es
  lo que la vuelve honesta en vez de una degradación silenciosa.

## §3. Las dos unidades

### U-COB-A — bloque A (los DIEZ; 41 páginas)

- **Fase A.1 — diagnóstico y diseño ($0, sin API).** Censo de los DIEZ por
  forma real (prosa corrida / listado / carátula), aplicación del modelo
  de unidad de §2, proyección de unidades por documento, y **guarda 2**:
  muestra pequeña de contenido cotejada a mano contra el vocabulario
  congelado (9 tipos / 13 relaciones / enum de 6) para responder si
  **cabe** — sin extraer. FRENO con el censo, la proyección y el
  veredicto de encaje.
- **Fase A.2 — piloto pago (tope declarado en su mandato).** Extracción
  de 2–3 documentos representativos con el prefijo v3 cableado, medición
  de encaje real (tipos emitidos, relaciones, rechazos de firma) y
  adjudicación de la autora sobre una muestra. FRENO.
- **Fase A.3 — masa.** Los restantes, solo si A.2 pasa.
- **Censo de los dos declarados referencia** (`optico`, `plandecuentas`):
  entra en A.1 como registro, con su evidencia (densidad deóntica 0,000
  en las tres variantes y la adjudicación de la lectura a ciegas). No se
  extraen.
- **Proyección de costo**: la de §0.1 — **57 unidades ≈ USD 1,10**.
- **CONTEO EXIGIDO (laudo de la autora sobre la guarda 3)**: el reporte
  entrega el **número exacto de elementos con `granularidad_procedencia
  = pagina` sobre el total del recurso**, para poder escribir en la tesis
  «N elementos de M, todos provenientes de los diez documentos sin
  numeración» en vez de una salvedad general.

### U-COB-B — bloque B (ficha; piloto ri2_pm, después manual)

- **Fase B.1 — diagnóstico, volumen y contenido ($0, sin API).** Tres
  entregables, y los tres son condición de arranque de B.2:
  1. **Guarda 4 — volumen medido**: cuántas unidades produce el modelo de
     unidad-ficha sobre ri2_pm y sobre manual, contado, no estimado, con
     la proyección de su peso relativo en el recurso final.
  2. **Adjudicación de contenido, espejo de la del bloque A**: el laudo
     apoya la ampliación en una lectura a ciegas de 32 páginas que
     cubrió los 12 del bloque A; el bloque B **no tiene esa evidencia**.
     El diseño exige una lectura a ciegas equivalente sobre una muestra
     de páginas ficha, con pre-registro sellado, ANTES de extraer: si el
     material resulta referencia y no prescripción, el bloque B se
     declara y no se extrae — que es la misma disciplina que llevó a
     incluir el bloque A.
  3. **Guarda 2 — encaje en el esquema congelado**: una ficha contable no
     es una obligación, una restricción, una excepción ni una operación.
     Si el material no cabe en los 9 tipos, **FRENO**: reabrir el esquema
     es laudo de la autora, jamás efecto colateral. (Antecedente
     directo: el hallazgo del modelo de datos sin hechos con valor, que
     ya está diferido a ESQ-RI-3/C1.7.)
- **Fase B.2 — piloto pago sobre ri2_pm** (345 páginas), con techo
  declarado. FRENO con adjudicación.
- **Fase B.3 — manual** (1.830 páginas), solo con laudo posterior a B.2.
- **Proyección de costo, con su rango y su supuesto**: a la densidad del
  corpus reconocido (1,38 u/pág) las 2.175 páginas darían ~**3.000
  unidades ≈ USD 58**; si la unidad natural fuera la fila de ficha, el
  volumen podría ser un múltiplo de eso. **No hay ancla para material
  ficha en este repositorio**: por eso la guarda 4 es medición previa
  obligatoria y no una estimación. **Cota superior de referencia**: el
  escalado completo de los 68 digeribles está presupuestado en ~USD 123
  — el bloque B puede costar una fracción importante de eso, o más.

## §4. Guarda 1 — regresión de no-cambio (vinculante en ambas unidades)

Idéntica a la de B5.8, con los cuatro controles que el laudo enumera,
verificados documento por documento y con los conteos recomputados:
**1.763** (5 de desarrollo, con desglose por TO), **762** (los 10 de
ESQ-2), **6.340** (los 68 originales) y **9.266** (los 138 reconocidos
plenos). Más byte-identidad de los artefactos E0 sellados y la batería de
selftests vigente en HEAD. **Cualquier diferencia = FRENO.**

Nota de diseño que refuerza la guarda: el modelo de unidad de estos
bloques **se activa solo donde el camino vigente no produce unidades de
prosa**, igual que en B5.8.1 — la no-alteración es estructural, no solo
demostrada.

## §5. Guarda de balance (agregado del diseño a la guarda 4)

Si el bloque B pasara a representar una fracción dominante de las
unidades del recurso, cambia **qué es el recurso**: un grafo cuya masa
principal fuera material de registro contable ya no es primariamente un
grafo de normativa prescriptiva. El diseño fija el disparador: si la
proyección de B.1 supera el **25 %** de las unidades totales del recurso
final, la fase B.2 **no arranca sin laudo explícito** de la autora sobre
el balance, con su consecuencia para la narrativa del capítulo. El umbral
es una convención declarada, no calibrada — su virtud es ser anterior.

## §6. Secuencia y efecto en la fecha (respuesta explícita al laudo)

**Lo que NO se mueve:**
- **El capítulo del esquema sigue su curso** (tramos 3, 4 y 5). Lo que
  los mentores validan es la metodología y el esquema, no la partición
  final. Bloquear el capítulo bloquearía la lectura, que es el gate del
  escalado: sería un cerrojo sobre el propio camino.
- **La lectura de mentores tampoco espera.**

**Lo que sí cambia en el capítulo, y lo mejora:** el tramo 5 narra la
partición de B5.8.4 como hecho verificado **y declara el hallazgo de
cobertura** — que el criterio de forma (¿tiene espina numerada?) no
coincide con el de contenido (¿manda algo?), medido con instrumento
corregido y lectura a ciegas. Es exactamente la clase de límite
argumentado que fortalece una tesis metodológica, y la ampliación en
curso se declara como tal.

**Lo que SÍ se mueve, con todas las letras: la fecha del escalado.** El
laudo pide ambos bloques ANTES de escalar. Estimación de trabajo:

| unidad | sesiones de ejecutor | costo API |
|---|--:|---|
| U-COB-A (A.1 + A.2 + A.3) | 3–5 | ≈ USD 4–8 |
| U-COB-B (B.1 + B.2 [+ B.3]) | 4–8 | USD 0 en B.1; B.2/B.3 a medir |

En serie —recomendado, porque ambas tocan el mismo módulo de
segmentación— son **7–13 sesiones más sus frenos**, del orden de **dos a
tres semanas de trabajo efectivo**, más el tiempo de las adjudicaciones
de la autora. El escalado se corre después. Si el laudo de balance de §5
frenara el bloque B, la fecha vuelve a acortarse.

**DECISIÓN DE LA AUTORA (07/09): DESACOPLE LAUDADO.**
Se desacoplan los bloques — **A antes del escalado** (barato, valor alto,
riesgo bajo, y es normativa vigente que hoy se excluiría) y **B después
del escalado**, como release posterior declarada (principio 9). Mueve la
fecha unos días en vez de semanas, y deja el bloque de mayor riesgo y
volumen fuera de la ruta crítica sin renunciar a él. El «ambos, no uno»
del laudo **sigue en pie en el qué**: B no se abandona, se declara con su
evidencia medida y su fase B.1 corre cuando el escalado esté encaminado.
Razones registradas por la autora: la superficie real de A es de días y
de un dólar; A es el único de los dos bloques que tiene su evidencia
detrás; B exige, antes de extraer una página, otra lectura a ciegas de la
autora, que es tiempo en la ruta crítica; y su costo no tiene ancla, con
la cota de referencia del escalado completo (~USD 123) como marco.
**Efecto neto sobre la fecha del escalado: días, no semanas.**
