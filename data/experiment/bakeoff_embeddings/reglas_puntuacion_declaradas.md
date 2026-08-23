# Reglas de puntuación — U-A2.0b-bakeoff, entregables 2-4

DECLARADAS ANTES DE PUNTUAR (y antes de indexar). Este archivo se sella por
sha256; los scripts de medición lo leen para hashearlo y no lo modifican.
Sustituyen a la regla R1 del entregable 1, descartada como regla principal.

## 0. Un solo índice, dos reglas de puntuación

Se indexa UNA vez por modelo el mismo universo de 1.763 pasajes y se ejecutan
las mismas 100 consultas. Las dos reglas difieren solo en qué conjunto gold se
compara contra el ranking y sobre qué casos se promedia. Ningún resultado de
la medición participa de la definición de las reglas.

## 1. Regla PRINCIPAL — R2 (subárbol completo del ancla)

Para cada ancla `(to, u)` del gold de A1.3:

    gold(to,u) = { c : c.to == to y c.unidad == u }              (exacta)
               ∪ { c : c.to == to y c.unidad empieza con u+"." } (descendientes)

La unión se toma SIEMPRE, exista o no chunk exacto. Incluye los `mini_chunk`
(`intro`/`cierre`) de la unidad y de sus descendientes: son texto propio de
esos puntos.

Gold del par = unión sobre sus anclas. Gold del caso = gold del par (las dos
variantes, literal y anti-léxica, comparten gold). 100 casos = 50 pares × 2.

Un caso ACIERTA en @k si al menos uno de sus chunks gold aparece en las
primeras k posiciones del ranking. recall@k = casos que aciertan / casos.

Se reportan @1, @5 y @10, pero el análisis se ancla en **recall@1** y en la
**brecha literal − anti-léxica**: con gold de mediana 11 y máximo 49 sobre
1.763 pasajes, @10 satura y deja de discriminar entre modelos.

## 2. Regla de CONTROL — "gold bien formado"

Subconjunto de pares cuyo gold es sustantivo y unívoco. Un ancla es **bien
formada** si:

- (i) su resolución exacta (`unidad == u`) es no vacía, y
- (ii) esa resolución NO está compuesta exclusivamente por chunks de
  `tipo == "mini_chunk"` — es decir, el punto tiene cuerpo propio y no solo
  un arranque de prosa de contenedor;

o bien, si su resolución exacta es vacía, si

- (iii) sus descendientes son no vacíos (el punto existe solo como
  sub-puntos: el gold es sustantivo aunque repartido).

Un **par entra al control** si TODAS sus anclas son bien formadas Y el tamaño
de su gold es ≤ 10 (mismo corte que la regla sellada del censo de EV2,
"contenedores >10 anclas excluidos").

Gold del control = el MISMO conjunto gold que usa R2. Esto no es una
coincidencia sino una propiedad verificable de la construcción: para un ancla
con resolución exacta no vacía y `punto_terminal` propio, los descendientes
son vacíos (un punto terminal es terminal), de modo que R1 y R2 coinciden;
para un ancla que entra por descendientes, la resolución exacta es vacía y R1
y R2 vuelven a coincidir. El script verifica esta igualdad par por par sobre
el subconjunto de control y aborta si falla. El control es, por lo tanto, un
puro submuestreo de casos del principal: mismas consultas, mismo índice,
mismo gold, menos casos.

## 3. Criterio de lectura, declarado ex ante

Si las dos reglas producen el MISMO orden de modelos, la elección es robusta
y se declara así. Si difieren, NO se elige: se reportan ambas tablas y la
unidad frena para laudo. En ninguno de los dos casos esta unidad recomienda
un ganador — la elección es laudo de la autora.

El orden de modelos se lee por **recall@1** bajo cada regla, calculado sobre
los 100 (resp. n_control) casos, es decir promediando las dos variantes;
adicionalmente se reportan los órdenes por recall@1 literal y por recall@1
anti-léxica por separado. `jinaai/jina-embeddings-v5-text-small` NO participa
del ordenamiento: es referencia no elegible por licencia (CC-BY-NC-4.0) y va
en fila aparte. BM25 sí participa de la lectura como piso de referencia.

## 4. Empates

Dos modelos empatan en una regla si su recall@1 coincide exactamente. Un
empate no rompe el "mismo orden": se compara el orden como preorden (lista de
clases de empate). Si dos modelos empatan en una regla y no en la otra, el
orden se considera COMPATIBLE mientras ninguna pareja se invierta.
