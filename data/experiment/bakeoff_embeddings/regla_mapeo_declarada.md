# Regla de mapeo gold → chunk — U-A2.0b-bakeoff, entregable 1

DECLARADA ANTES DE APLICARLA. Este archivo se escribe y se sella (sha256)
antes de ejecutar el script de mapeo; el script no la modifica.

## Insumos (solo lectura)

- Gold: `data/experiment/ablacion_retrieval/pares/pares_v3.json` (50 pares,
  sellado en 68c79dc). Cada par trae `gold.anclas`: lista de objetos
  `{to, ancla, source_doc, location_ejemplo}`. 47 pares tienen 1 ancla, 3
  tienen 2. Anclas distintas: 37, todas de forma `N.M`.
- Pasajes: `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_{cap,cla,ext,pro,ric}.json`,
  1.763 chunks (cap 462, cla 143, ext 973, pro 101, ric 84). Cada chunk trae
  `id`, `to`, `unidad`, `tipo` ∈ {punto_terminal, mini_chunk, seccion_sin_puntos},
  `texto` (propio) y `herencia`.

## Hechos estructurales que la regla debe contemplar

1. `unidad` NO es clave única del chunk: 1.703 unidades distintas para 1.763
   chunks (1.644 unidades con 1 chunk, 58 con 2, 1 con 3). Un punto que abre
   con prosa antes de sus sub-puntos genera un `mini_chunk` de rol `intro`
   (y a veces `cierre`) con la MISMA `unidad` que su `punto_terminal`.
   Por lo tanto el mapeo es ancla → CONJUNTO de chunks, nunca ancla → chunk.
2. Hay unidades no numéricas (`S2`, `S3`, `S5`, `S6`, `S7`, `S14`, `S15`):
   son secciones sin puntos. Ningún ancla del gold tiene esa forma, así que
   no participan del mapeo bajo (a); sí podrían aparecer bajo (b) y no lo
   harán porque el prefijo de descendencia es numérico.

## Regla

Para cada ancla `(to, u)` del gold:

- **(a) primaria — coincidencia exacta de unidad.** Chunks con
  `chunk.to == to` y `chunk.unidad == u` (comparación de strings, exacta).
  Incluye los `mini_chunk` de esa misma unidad: son texto propio de ese
  punto, no de otro.
- **(b) descendientes — solo si (a) da 0 chunks.** Chunks con
  `chunk.to == to` y `chunk.unidad` que empieza con `u + "."`. La condición
  "solo si (a) da 0" es deliberada: cuando el punto tiene chunk propio, ese
  chunk es el pasaje que contiene la respuesta y agregarle la descendencia
  inflaría el conjunto gold y haría más fácil el recall.
  Fundamento del caso (b): es el mismo fenómeno que el censo de EV2 registró
  como granularidad de ancla en
  `data/experiment/ev2_corrida/censo/ausencias_diagnostico.json` — "crudo=0 y
  desc>0 => el punto existe solo como sub-puntos (patrón de extracción por
  bloques)". Allí el objeto era el grafo; acá es el chunking, pero la causa
  es la misma: el ancla que la generación citó es un punto contenedor cuyo
  contenido vive en sus hijos.

Conjunto gold del PAR = unión de los conjuntos de todas sus anclas.
Conjunto gold del CASO = el del par (las dos variantes, literal y
anti-léxica, comparten gold: son dos redacciones de la misma pregunta).
100 casos = 50 pares × 2 variantes.

## Clasificación de cada caso

- **mapeado**: su conjunto gold tiene ≥ 1 chunk.
- **no mapeado**: conjunto gold vacío (ninguna ancla resolvió ni por (a) ni
  por (b)).
- **ambiguo (marca, no excluye)**: caso mapeado cuyo conjunto gold tiene
  MÁS DE 10 chunks. El corte 10 no es arbitrario: es el mismo que la regla
  sellada del censo de EV2 usó para excluir contenedores
  ("contenedores >10 anclas excluidos"). Un caso ambiguo sigue contando como
  mapeado a los efectos del umbral, pero se reporta aparte porque en él
  recall@k mide "¿cayó algo del bloque?" y no "¿recuperó el pasaje?".
  Se reporta además, para todo caso mapeado, el tamaño del conjunto gold.
- **parcialmente resuelto**: caso con 2 anclas donde una resuelve y la otra
  no. Se reporta aparte; cuenta como mapeado.

## Umbral (freno del mandato)

Se evalúa sobre el conteo de casos **mapeados bajo (a)+(b)**. Si son menos
de 80 de 100, la unidad frena antes del entregable 2.
