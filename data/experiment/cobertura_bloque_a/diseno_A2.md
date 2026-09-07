# Diseño de la fase A.2 — piloto pago del bloque A

Unidad U-COB-A, entregable 6 de la fase A.1. **Este documento no autoriza
gasto**: propone el piloto para el laudo de la autora y su mandato propio.

## 1. Qué documentos, y por qué esos

Criterio de seleccion declarado: **cubrir las tres formas medidas en el censo
con el minimo de paginas**, e incluir al menos un documento donde el modelo de
unidad tenga que convivir con planilla, porque ese es el riesgo que A.1
descubrio y que ninguna extraccion previa del proyecto midio.

| documento | paginas | unidades del piloto | forma que aporta | por que entra |
|---|--:|--:|---|---|
| `ri_tii` | 6 | **36** (25 prosa + 11 planilla) | prosa + planilla en un mismo documento, con 5 tablas logicas que B5.8.3 SI detecta | unico de los diez donde el parser tabular sellado ve algo: permite contrastar las dos lecturas sobre el mismo material |
| `ri_itme` | 1 | **11** (prosa pura) | prosa pura de una pagina, sin numeracion, 27 % de bloques con sujeto nombrado | el caso limpio y barato: mide el modelo sin ruido tabular |
| `ri_con` (solo p.1–2) | 2 de 16 | **14** (prosa pura) | prosa de instrucciones del documento mas planillero del bloque | mide si la prosa se extrae bien en un documento cuyo 87 % es planilla |

**Total del piloto: 61 unidades / 13.661 caracteres** (recomputado:
`python3 code/costo_a2.py`, bloque `por_to`; 36 + 11 + 14 = 61).

**Quedan FUERA del piloto y a la espera de su resultado**: las 102 unidades de
planilla de `ri_con` p.3–16, `ri_spi` entero (141 unidades, el caso de
numeracion propia — ver §5) y los seis restantes.

## 2. Tope de gasto propuesto

| via de proyeccion | monto |
|---|--:|
| por caracter (la pertinente; tarifa `usd_por_char_agregado` E1+E3) | **USD 0,44** |
| por unidad (COTA SUPERIOR; tarifa calibrada sobre unidades 3,4× mas largas) | **USD 1,19** |
| **tope propuesto para el mandato de A.2** | **USD 2,00** |

El tope propone ~1,7× sobre la cota superior. Tarifas ancladas en
`escalado_prep/proyeccion_costo.json` §`tarifas` (gasto real de la corrida
`corpus_v2`, `pro` excluido por ser el TO de calibracion con gasto 0).

## 3. Con qué se corre

El prefijo congelado tal cual (sha
`e69feaaa04779bd6347cc9e3974d2c1749519f1230e70a0459e66f46517cd720`, hash
`1be8304e3d77`), integrado por el cableado v3, **sin una sola regla de esquema
nueva** — la guarda 2 de A.1 concluyo que el material cabe. Toda llamada va
envuelta en `CachingClient` con namespace versionado, por la regla del
repositorio sobre captura de crudos.

## 4. Predicciones verificables (PRE-REGISTRADAS: se sellan antes de correr)

Cada una con su ancla y su forma de falsarse. Una prediccion fallada no aborta
A.2: se reporta y se lauda.

**P1 — el vocabulario congelado alcanza.** Cero emisiones de tipo o predicado
fuera de los 9 y los 13. *Falsable*: cualquier emision fuera de lista.
*Ancla*: guarda 2 de A.1, 10/10 muestras cubiertas.

**P2 — `aplica_a` se degrada, y se degrada de forma acotada.** La fraccion de
unidades con al menos una arista `aplica_a` sera **menor que en el corpus de
desarrollo** y **mayor que la fraccion de unidades que nombran un sujeto de
forma literal**. Es decir, caera en el intervalo **(27,9 % ; 53,1 %)**.
*Falsable*: si cae por debajo de 27,9 % el extractor no esta recuperando
ningun sujeto heredado y la procedencia de pagina rompe `aplica_a`; si supera
53,1 % esta inventando sujetos, que es peor. *Ancla*: `senal_sujeto.json` y su
baseline sobre los 1.763 del dev.

**P3 — el vaciamiento sube.** La tasa de unidades con extraccion vacia cuyo
texto porta contenido normativo sera **≥ 7,4 %** (la tasa v2 del laudo del
esquema congelado §3: 2/27). *Falsable*: si es menor, las unidades cortas no
vacian tanto como el diseño teme y la mediana de 93,5 caracteres no es un
problema. *Ancla*: laudo del esquema congelado §3, fila «Vaciamiento».

**P4 — testigo RX-10.** Entre las 11 unidades de planilla de `ri_tii`
aparecera **al menos una** cuyo texto linealiza una grilla mezclando
encabezado de columna con valor de otra columna. *Falsable*: cero casos.
*Ancla*: el defecto RX-10 declarado (`docs/backlog_reextraccion.md` §RX-10) y
la razon por la que B5.8.3 preserva filas y columnas en vez de linealizar.
**Esta es la prediccion que decide si la planilla del bloque A se extrae o se
declara**, y por eso el piloto la incluye en vez de evitarla.

**P5 — la palabra partida se paga.** Al menos una unidad emitira una entidad
cuyo `label` contenga una palabra cortada por guion de particion
(«obli- gacion»). *Falsable*: cero casos. *Ancla*: 79 de los 332 bloques
(23,8 %) contienen al menos una palabra partida —`python3 code/palabra_partida.py`—
porque el modelo de unidad de pagina **no hereda** la correccion de fronteras
intra-palabra que el camino vigente si aplica (`e0_lib.corregir_fronteras_intra_palabra`;
en `cap` la llevo de 200 a 0, `conteos.json` §cap).

## 5. Lo que A.2 NO hace, y por qué

- **No extrae `ri_spi`.** Es el unico de los diez con numeracion propia en el
  71 % de sus bloques (`A.1.`, `B.5.8.3.`): asignarle procedencia de pagina
  seria degradar una granularidad que el documento **si tiene**. Su tratamiento
  es laudo de la autora (§4 del reporte de A.1), y hasta ese laudo no se toca.
- **No extrae las 102 unidades de planilla de `ri_con`.** Su suerte depende de
  P4.
- **No toca ningun modulo de segmentacion.** El modelo de unidad vive en el
  codigo propio de la unidad; `e0_lib` y `e0_tablas` se importan como
  bibliotecas de solo lectura, verificado en A.1 por `git diff --quiet HEAD`.

## 6. Criterio de aceptacion de A.2 (para su freno)

A.2 pasa si: P1 se cumple; P2 cae en su intervalo; y hay adjudicacion de la
autora sobre una muestra de las unidades emitidas. P3, P4 y P5 son
**mediciones informativas**: su resultado alimenta el laudo sobre la masa
(A.3) y sobre la planilla, y ninguna de las tres aborta la fase por si sola.
