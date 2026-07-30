# Backlog de re-extracción — defectos del pipeline que solo se arreglan re-computando

**Estado:** abierto, en acumulación. No ejecutar hasta que la autora lo cierre.

## Qué es esto y por qué está separado del backlog de refinamiento

`data/backlog/backlog.jsonl` (spec `docs/spec_backlog_refinamiento.md`) registra
**defectos de nodos de un grafo**: tienen `nodos_objetivo`, una especie del bestiario
cerrado, y se corrigen editando el grafo. Este archivo registra otra cosa: **defectos
del instrumento que produce el grafo**. No tienen nodo objetivo —tienen chunks, regex
y reglas de segmentación— y no se corrigen editando nada, se corrigen volviendo a
extraer.

Se acumulan acá en vez de ejecutarse de a uno porque **re-extraer cuesta plata y
rompe comparabilidad**: la corrida completa del v2 costó **USD 10,716** por 508 chunks
(informe `data/experiment/grafo_v2/informes/U5_2026-07-26.md`), y cada re-extracción
produce un instrumento nuevo contra el cual las mediciones selladas (escalón 1: 216
corridas, USD 19,24, run_3 31/36 vs grafo_v2 27/36) dejan de ser comparables. La
disciplina es: acumular todo, re-extraer **una sola vez**, con todos los arreglos
juntos.

## Cómo se llegó a esta lista

Auditoría de reconciliación PDF → chunks → caché de extracción → `kg.json` sobre
`grafo_v2`, disparada por una falla real de la app: la sesión
`6e633685-56d1-41fb-8c6f-c38493169666` preguntó por el tope mensual de compra de
moneda extranjera de personas humanas residentes (punto 3.9 del TO de Exterior y
Cambios: USD 200, o USD 100 en efectivo) y el agente abstuvo porque el dato no estaba
en el grafo. El dato **sí se había extraído**: se perdió al ensamblar.

Lo que era defecto de ensamblado ya se corrigió sin gastar un peso
(`data/experiment/grafo_v2/reensamblado_v3/`, ver §"Ya resuelto"). Lo que queda acá es
lo que quedó congelado en el texto y la `location` con que los chunks se mandaron a la
API, y que ningún ensamblado puede deshacer.

Los números son de parseo real, no estimaciones. Scripts de la auditoría: no
commiteados (vivieron en el scratchpad de la sesión); los conteos se reproducen desde
`cache_v2/chunks_all.json` + `chunk_roles.py`.

---

## Entradas

### RX-01 — `chunk_id` no identifica un pasaje

**Defecto.** `chunker.py:137` arma `chunk_id = f"{doc}::{numbering}"`. La misma
numeración aparece hasta tres veces en un TO (índice, articulado, tabla "norma de
origen"), así que el id colisiona por construcción: **81 chunk_ids compartidos por 183
chunks**, sobre 508.

**Consecuencia medida.** El ensamblado v2 desempataba por "el que más entidades
extrajo" y descartaba el resto: **102 resultados de extracción tirados (20% del
corpus)**, incluidos **53 chunks de articulado — 95.226 chars, 429 entidades ya
pagadas — que no aportaban un solo nodo**. Entre ellos el 3.9 que originó esta
auditoría.

**Fix.** Id único por construcción (numeración + ordinal de aparición u offset) y rol
documental como campo del chunk, no como inferencia posterior.

**Estado.** Mitigado en el re-ensamblado v3 (el driver es `chunks_all.json` y no hay
desempate). El fix de raíz sigue pendiente porque el id sigue siendo ambiguo para
cualquier consumidor futuro.

Reproducibilidad: MEDIDO — replicación del dedup v2 sobre el caché (auditoría U0,
29-07): reproduce los seis números exactos (81 ids / 183 chunks / 102 descartados /
53 cuerpo / 95.226 chars / 429 entidades).

---

### RX-02 — Location desplazada por el coalescing

**Defecto.** `chunker.py:144-163` fusiona chunks menores a `MIN_CHUNK_CHARS` con el
siguiente **conservando el id y la location del primero**. El contenido del segundo
punto queda declarado bajo el título del primero.

**Consecuencia medida.** **21 chunks de rol cuerpo** con **26.308 chars de articulado
bajo una location ajena**. Ejemplos: `clasificacion_deudores::3.2` dice "Punto 3.2.
Periodicidad de clasificación" y contiene también el 3.3 (2.744 chars);
`exterior_cambios::14.5` dice "Punto 14.5. Otras disposiciones" y contiene 14.6, 15.1
y 15.2. Los hechos entran al grafo con la cita equivocada.

Es la especie `provenance_desplazada` del bestiario, pero de origen mecánico: no la
generó el extractor, la generó el chunker.

**Fix.** Al fusionar, o bien conservar la lista de puntos cubiertos y emitir provenance
múltiple, o bien no fusionar y aceptar chunks chicos.

**Estado.** No mitigable en ensamblado: la `location` es lo que se le declaró al modelo
en el prompt y lo que quedó grabado en el caché.

Reproducibilidad: MEDIDO — replicación del coalescing del chunker registrando
absorciones (auditoría U0, 29-07): 21 chunks / 26.308 chars exactos.

---

### RX-03 — Falsos headers por referencias cruzadas

**Defecto.** `NUMBERED_HEADER` (`chunker.py:39`) matchea cualquier línea que empiece
con `N.N.` seguido de texto. Una referencia cruzada que cae a principio de renglón
—"4.3. –con excepción de los casos contemplados en el punto 4.1.–"— se toma por
título de punto y abre un chunk.

**Consecuencia medida.** **17 chunks de rol cuerpo, 47.813 chars**, bajo una location
que no es un título. Los peores: `capitales_minimos::2.6__p0` (6.876 chars, "Punto
2.6. de las citadas normas"), `exterior::3.17__p0` (6.843, "Punto 3.17. ii) el resto
del capital que vencía fue…"), `exterior::3.5` (6.572, "Punto 3.5. en el marco de lo
previsto en el punto 14.2.1."). Daño doble: la provenance es inútil como cita, **y**
el chunk espurio compite por el `chunk_id` del punto real (RX-01).

**Fix.** Exigir que el header sea un título: mayúscula o comilla inicial, y/o validar
contra la lista de puntos que declara el índice del propio documento.

**Estado.** No mitigable en ensamblado.

Reproducibilidad: DECLARADO — falta la regla exacta de "falso header"; una heurística
independiente (título que no empieza en mayúscula/comilla/dígito) encontró 15 puntos
de corte que incluyen los 3 ejemplos citados, pero no reproduce ni 17 ni 47.813.

---

### RX-04 — Puntos anunciados en el índice sin articulado propio

**Defecto.** Consecuencia de RX-02 + RX-03: el cuerpo de algunos puntos nunca llegó a
tener chunk propio y quedó absorbido en un vecino.

**Consecuencia medida.** **3 puntos**: `clasificacion_deudores` 1.1 y 4.5,
`exterior_cambios` 9.2. Su texto está en el corpus (la cobertura de chars del chunker
es 99,91%), pero no existe como pasaje con nombre. En el v3, al excluir el índice,
estos puntos pierden hasta el nodo-título que los nombraba.

**Fix.** El mismo de RX-03: reconciliar los puntos detectados contra los que declara el
índice, y fallar ruidosamente cuando falte uno.

**Estado.** No mitigable en ensamblado.

Reproducibilidad: MEDIDO — spot-check de los 3 puntos declarados (ningún chunk de rol
cuerpo con esos ids exactos; auditoría U0, 29-07); la exhaustividad ("son exactamente
3") queda DECLARADA — reproducirla exige la reconciliación índice↔cuerpo completa.

---

### RX-05 — Chunks que mezclan roles documentales en un mismo prompt

**Defecto.** Un chunk puede abarcar páginas de articulado y de la tabla de
correspondencias, y se le declara una sola `Ubicación:`.

**Consecuencia medida.** **13 chunks mixtos**, dos de ellos enormes:
`capitales_minimos::12` (41.785 chars, cuerpo+tabla) y `clasificacion_deudores::10.3`
(22.835 chars, cuerpo+tabla). Al modelo se le pidió extraer norma de una mezcla de
norma y tabla de referencias.

**Fix.** Cortar por frontera de rol antes de cortar por punto: el rol es una propiedad
de la página, y las páginas de índice y de tabla se detectan de forma determinística
(pie `-Índice -`, encabezado `NORMA DE ORIGEN` — implementado y validado en
`chunk_roles.py`, 508/508 clasificados).

**Estado.** No mitigable en ensamblado.

Reproducibilidad: DECLARADO — la unidad de conteo del 13 no es reproducible; una
medición pre-split da 7 chunks que cruzan roles, incluidos los 2 ejemplos graves.

---

### RX-06 — Contexto cortado por `HARD_CAP_CHARS`

**Defecto.** Los chunks mayores a 7.000 chars se parten por párrafos
(`_split_by_paragraphs`). Una restricción que cae en la parte 2 no puede vincularse a
la operación definida en la parte 1: la relación no se extrae porque el modelo nunca
vio los dos extremos juntos.

**Consecuencia medida.** **51 chunks partidos** (exterior 22, capitales mínimos 16,
régimen informativo 5, clasificación deudores 4, protección usuarios 4).

**Fix.** Solapamiento entre partes, o pasar el encabezado del punto padre a cada parte,
o subir el cap ahora que Haiku 4.5 tiene más ventana. Requiere medir: subir el cap sube
el costo.

**Estado.** No mitigable en ensamblado. **Sin cuantificar el daño**: no sé cuántas
relaciones se perdieron por esto, solo cuántos chunks están expuestos. Medirlo exige
gold por chunk, que no existe.

Reproducibilidad: MEDIDO — 51 ids padre distintos con sufijo `__p` en
`chunks_all.json`; desglose por doc exacto (auditoría U0, 29-07).

---

### RX-07 — Se paga extracción de contenido que no aporta hechos

**Defecto.** Los 48 chunks de índice se extraen y se pagan. El índice es la lista de
títulos del propio articulado: no aporta un solo hecho normativo.

**Consecuencia medida.** 48 de 508 llamadas, pero son chunks chicos: **17.516 chars,
1,3% del texto enviado a la API**. El ahorro real es marginal (del orden de USD 0,15
sobre los 10,716 por el lado del input; el output no es proporcional al input, así que
el número es un piso, no una cuenta cerrada). El motivo para saltearlos **no es el
ahorro sino la contaminación**: son la fuente de RX-01 y de los 25 nodos cáscara de
RX-08. Los 92 chunks de tabla (124.647 chars, 9,4% del texto) sí aportan —qué
Comunicación originó cada punto— pero convendría extraerlos con un prompt propio en
vez del prompt de norma.

**Fix.** Saltear el rol `indice` en el chunker.

**Estado.** Mitigado en el v3 (se excluyen del ensamblado), pero el gasto ya se hizo y
se volvería a hacer en una re-extracción sin este fix.

Reproducibilidad: MEDIDO — en chunks y chars (48 / 17.516 / 1,3% índice; 92 /
124.647 / 9,4% tabla; auditoría U0, 29-07); el ahorro estimado en USD queda DECLARADO
como piso.

---

### RX-08 — Nodos cáscara heredados del índice (registro, no acción)

**Consecuencia medida.** **25 nodos de `grafo_v2` provienen de chunks de índice**, 19 de
ellos sin `properties.descripcion`: son títulos sin norma. Desaparecen en el v3:
**0 de los 25 están en v3 por id exacto**; 3 reaparecen por (type, label) porque la
misma entidad también fue extraída desde chunks activos (cuerpo/tabla) y en v3 entra
por esa vía — eso es esperado, no un residuo del defecto. No es pérdida de contenido
normativo —son `cascara` del bestiario— pero queda registrado porque explica parte del
delta v2→v3 y porque 3 de ellos (los de RX-04) eran la única mención de puntos cuyo
articulado no tiene chunk.

Nota de corrección: el conteo original de esta entrada (23 nodos, 9 sin descripción)
provino de scripts de scratchpad no commiteados y NO es reproducible; los valores
vigentes (25/19) son los de la replicación de la atribución v2 de la auditoría U0
(29-07): mismo orden `sorted(glob)`, mismo slug, mismo desempate.

**Estado.** Sin acción propia; se resuelve con RX-04.

Reproducibilidad: MEDIDO — replicación de la atribución v2 (auditoría U0, 29-07): 25
nodos creados por chunks de rol índice, 19 sin `properties.descripcion`, 0 presentes
en v3 por id exacto.

---

### RX-09 — Preámbulo descartado por tamaño

**Defecto.** `chunker.py:121` descarta el preámbulo si mide menos de
`MIN_CHUNK_CHARS`. **1.207 chars** en los 5 PDFs (230+213+283+228+253, preámbulos
post-strip menores a `MIN_CHUNK_CHARS`; 0,09% del corpus): son portadas.
Impacto despreciable, se lista para que la cobertura del chunker pueda declararse 100%
y no 99,91%.

Nota de corrección: el valor original de esta entrada era 1.212; la medición de la
auditoría U0 (29-07) da 1.207. El desvío de 5 chars queda sin explicar (la hipótesis
de que el original midió longitudes pre-strip —1 char por PDF— no fue confirmada).

Reproducibilidad: MEDIDO — replicación del chunker sobre los 5 PDFs: 1.207 chars
(230+213+283+228+253), con desvío −5 respecto del valor original, registrado sin
causa confirmada.

---

## Ya resuelto sin re-extraer (no entra a esta lista)

Corregido en `data/experiment/grafo_v2/reensamblado_v3/` (USD 0, mismo caché de
extracción, `grafo_v2/kg.json` intacto):

- Los 53 chunks de articulado que no aportaban nodos: recuperados.
- Colapso de `Operacion` por dedupear con un campo categórico (`properties.tipo`): 56
  operaciones distintas caían en `Operacion_presentacion_informativa` y 30 en
  `Operacion_calculo`. Disuelto: 855 → 1.201 nodos `Operacion`.
- Colisión de prefijo a 80 chars en Restricción/Obligación/Excepción.
- Evidencia descartada en merges (1.729 nodos y 1.227 aristas conservaban una sola
  cita): ahora se acumula `provenances`.
- Reporte que declaraba 100% de cobertura calculándola sobre los sobrevivientes del
  desempate.

## Criterio de cierre

Este backlog se cierra cuando la autora decida re-extraer. En ese momento:

1. Los fixes RX-01 a RX-07 y RX-09 se aplican **juntos** al chunker.
2. La re-extracción invalida `cache_v2/` entero (cambian los textos de los chunks) y
   cuesta del orden de la corrida original, menos el ahorro de RX-07.
3. El grafo resultante es un **instrumento nuevo**: el escalón 1 y cualquier medición
   sellada contra `grafo_v2` no se comparan directamente con él sin re-correr.
