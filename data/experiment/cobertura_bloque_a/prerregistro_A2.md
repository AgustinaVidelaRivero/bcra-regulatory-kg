# Pre-registro de la fase A.2 — predicciones por brazo

Unidad U-COB-A. **Sellado ANTES de la corrida**: su sha256 se imprime en el
freno exprés y ninguna prediccion se edita despues de ese sello. Alcance:
NUEVE documentos (laudo 2 del 07/09; `ri_spi` fuera).

## 0. Definiciones operativas (comunes a los dos brazos)

**RINDE**: la unidad produce **≥1 entidad de tipo normativo**, es decir de
`{Operacion, Restriccion, Excepcion, Obligacion, Potestad, Condicion,
Definicion}`.

**NO RINDE**: la unidad produce 0 entidades, **o** produce unicamente
`TextoOrdenado` y/o `Comunicacion` — que son andamiaje documental emitido por
documento y no contenido normativo de la unidad.

**Entidades del brazo**: la union de las entidades de tipo normativo emitidas
por las unidades del brazo. Las fracciones por tipo se calculan sobre ese
total, no sobre el total del grafo.

---

## 1. BRAZO PROSA — 77 unidades · 13 páginas · 9 documentos (COMPLETO)

**PR-1 — el vocabulario congelado alcanza.** Cero emisiones de tipo o de
predicado fuera de los 9 y los 13.
*Falsable*: ≥1 emision fuera de lista.
*Ancla*: guarda 2 de A.1 — 10 de 10 muestras cubiertas, 0 no cabe.

**PR-2 — rendimiento alto pero por debajo del corpus de desarrollo.**
**≥ 80 %** de las 77 unidades rinden (≥ 62 de 77).
*Falsable*: < 80 %.
*Ancla*: **96,2 %** en el corpus de desarrollo (1.696 de 1.763 unidades tienen
≥1 nodo con su `chunk_id` en el grafo vigente `0226e947`). Se predice por
debajo porque el brazo incluye rotulos de una linea («Instrucciones
generales») que no portan norma.

**PR-3 — la Obligacion domina, y mas que en el corpus general.** `Obligacion`
es el tipo mas frecuente del brazo y representa **≥ 45 %** de sus entidades.
*Falsable*: no es el mas frecuente, o < 45 %.
*Ancla*: **38,0 %** en el grafo vigente (2.484 de 6.529). Se predice por
encima porque este material es regimen informativo, cuyo contenido es
precisamente el deber de presentar.

**PR-4 — `aplica_a` se degrada de forma acotada.** La fraccion de unidades con
≥1 arista `aplica_a` cae en el intervalo **(42,9 % ; 53,1 %)**.
*Falsable*: fuera del intervalo, por cualquiera de los dos lados.
*Anclas, y por que cada extremo importa*: **42,9 %** son las 33 de 77 unidades
del brazo que nombran literalmente un sujeto del catalogo congelado — por
debajo de ese piso el extractor no recupera ni los sujetos que estan escritos,
y la procedencia de pagina rompe el predicado; **53,1 %** son las 936 de 1.763
del corpus de desarrollo — por encima de ese techo esta **inventando** sujetos
donde el texto no los nombra, que por el principio §1 del laudo del esquema
congelado (falsedad en campo estructurado) es **peor** que omitirlos.

**PR-5 — la palabra partida se paga.** ≥1 entidad emitida tiene una palabra
cortada por guion de particion («obli- gacion») en su `label` o en su texto.
*Falsable*: cero casos.
*Ancla*: **30 de las 77** unidades del brazo (39,0 %) contienen al menos una
palabra partida, porque el modelo de unidad de pagina no hereda
`e0_lib.corregir_fronteras_intra_palabra`.

---

## 2. BRAZO PLANILLA — 24 unidades · 4 páginas · 3 documentos (MUESTRA, 21 %)

**PL-1 — el vocabulario congelado alcanza.** Identica a PR-1, medida por
separado sobre este brazo.
*Falsable*: ≥1 emision fuera de lista.

**PL-2 — la planilla rinde mucho menos que la prosa.** **< 50 %** de las 24
unidades rinden (< 12 de 24).
*Falsable*: ≥ 50 %.
*Ancla*: **no hay ancla de material de planilla en este repositorio** — esa
ausencia es la razon de ser del brazo. El 50 % es una **convencion declarada,
no calibrada**, elegida como punto medio entre «rinde como prosa» (≥80 %, PR-2)
y «no rinde nada» (0 %); su virtud es ser anterior a la medicion.

**PL-3 — testigo RX-10.** ≥1 unidad del brazo emite una entidad cuyo texto
mezcla el encabezado de una columna con el valor de otra.
*Falsable*: cero casos.
*Ancla*: RX-10 (`docs/backlog_reextraccion.md:267`) y el bloque de `ri_con`
p.5 citado en el reporte de A.1 §2.a.

**PL-4 — la modalidad no se alucina sobre un formulario.** `Obligacion`
representa **< 25 %** de las entidades de este brazo — muy por debajo del
≥45 % predicho para prosa.
*Falsable*: ≥ 25 %.
*Interpretacion PRE-DECLARADA*: si la planilla produce `Obligacion` en
proporcion de prosa, el extractor esta atribuyendo modalidad deontica a un
formulario. Eso es falsedad en campo estructurado, y por el principio §1 del
laudo del esquema congelado **se retira**, no se acepta con residuo.

**PL-5 — contraste con la lectura tabular sellada.** Las 2 paginas de `ri_tii`
del brazo (p.3 y p.4) tienen **5 tablas logicas** detectadas por B5.8.3. Para
esas 2 paginas, la lectura de prosa emitira **menos** entidades bien formadas
que filas tiene la lectura tabular.
*Falsable*: emite mas o igual.
*Ancla*: `python3 code/censo_forma.py` → `ri_tii.b583_tablas_logicas = 5`,
`b583_paginas_con_tabla = [3, 4]`. Es la **unica** comparacion directa
disponible en todo el bloque A entre las dos lecturas sobre el mismo material.

---

## 3. Qué se concluye de cada combinación (decidido ANTES de medir)

| resultado | conclusión pre-declarada |
|---|---|
| PR-2 y PR-4 se cumplen · PL-2 y PL-4 se cumplen | la prosa se extrae a escala (A.3); la planilla **se declara** y su tratamiento va al bloque B |
| PR-2 y PR-4 se cumplen · falla PL-2 **o** PL-4 (la planilla rinde como prosa) | se abre laudo: la planilla puede ser extraible y el bloque B se re-dimensiona — no se decide en A.2 |
| **falla PR-2** | el modelo de unidad de pagina no sirve **ni para prosa**: A.3 no arranca y la unidad vuelve a diseno |
| falla PR-4 por el techo (>53,1 %) | señal de invencion de sujetos: **freno** y muestreo manual antes de cualquier masa |
| PL-3 se cumple | no aborta nada: es la evidencia que sostiene **declarar** la planilla en vez de extraerla |

## 4. Limitación de poder del brazo planilla, declarada

El brazo planilla mide **24 de las 114 unidades (21 %)** y **4 de las 17
paginas (24 %)** del material de planilla de los nueve, con `ri_con` —que
aporta 102 de esas 114 unidades— representado por **una sola pagina**. Alcanza
para PL-1, PL-3 y una tasa gruesa de PL-2/PL-4; **no alcanza** para una
estimacion fina ni para un laudo de escala sobre las 17 paginas. El brazo
planilla COMPLETO costaria USD 0,44 por caracter / USD 2,22 por unidad (cota
superior), de modo que **medirlo entero exigiria un tope de USD 4,00** — es
decision de la autora y este pre-registro no la presume.
