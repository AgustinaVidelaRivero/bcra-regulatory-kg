# Mandato U-LECTURA-ACEPTADAS — tasa de error de las unidades aceptadas de la tanda 0

**FIRMADO por la autora el 06/10/2026** (firma por mensaje de la autora; la versión para firmar, del mismo día, no tuvo commit propio:
este archivo entra al repo ya firmado). **Decisiones al firmar:** (1) nombre U-LECTURA-ACEPTADAS; (2) vigilancia por tanda de 60 unidades
aceptadas en dos estratos (ítems y no ítems), con el mismo sorteo y criterio; (3) semilla del sorteo `U-LECTURA-ACEPTADAS:sorteo:2026-10-06`,
sellada por la firma antes de leer. Diseño aprobado por la autora el 06/10/2026 (propuesta de la mesa del mismo día). Se despacha con los
dos grafos evaluados sin la cola sellados: SC2 de U-SINCOLA-T0 en `dde9f44` y su sello en `235a295` (U-SINCOLA-T0 CERRADA). USD 0, sin API.

## 1. Qué mide y por qué

La tasa de unidades aceptadas con error en la tanda 0. Hoy la tanda 0 tiene medida la cola (T4 de U-REEXT-T0: 12 de 30) y la
precisión de aristas aceptadas (observación 12), pero no una tasa de error por unidad sobre las aceptadas, que son 2.366 de 2.440
(los diez TOs). Esa tasa es la línea de base del error del pipeline para la tesis y para la vigilancia por tanda del pre-registro
de la tanda 1.

Criterio, el del punto 1 de T4 de U-REEXT-T0 (`docs/mandatos/UREEXT_T0_reextraccion_tanda0.md:284-285`): una unidad tiene error si al
menos un nodo o una relación suya no se sostiene en el texto de la unidad (propio o heredado); las omisiones se reportan aparte y no
cuentan como error.

## 2. Población y estratos

Las unidades aceptadas del grafo evaluado de los diez TOs sin la cola: las que tienen como última versión en
`data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/<to>/finales.jsonl` el estado `completo_ok_directo` (1.337),
`aceptado_con_residuales` (813) o `aceptado_tras_reintento` (216): 2.366 (recomputado el 06/10/2026 sobre `01046b6`; L0 lo recomputa y
lo sella). La unidad es el chunk de la E0 r2b (`e0_chunking/salida_tanda0_r2b/`, 57 archivos, sello `9f6361e`) con sus nodos y
aristas en `ens_diez_r2b_sincola/r2/kg.json` (`e22fae1a…`). `cap::4.2.1.2::parte2`, aceptada, es parte de una partición por corte y
usa el chunk de `cap::4.2.1.2` (su `::parte1` está en la cola).

Dos estratos, por `es_item` de `data/experiment/reextraccion_v2/e1_extractor/prompt_r2b.py:323` sobre el chunk: ítems de lista,
N₁ = 1.003; no ítems, N₂ = 1.363. La razón de estratificar: la hipótesis en curso sobre los ítems (U-DIAG-E3-LISTAS: 1.015 de 1.054
ítems sin el bloque que abre la lista en E3) y el desglose de la cola (33 de los 43 veredictos inutilizables son ítems).

## 3. Muestra y sello previo

n₁ = n₂ = 30, sorteo simple dentro de cada estrato con `random.Random(f"{semilla}:{estrato}").sample(ids, 30)`, `ids` ordenados y
`estrato` ∈ {`item`, `no_item`}. Las unidades leídas en T4 (grupo c, P4b, omisiones) no se excluyen; el solapamiento se reporta. L0 sella
antes de abrir una unidad: la lista de la población con su sha256, la semilla, la hora y el sha256 de la muestra, con el patrón de
`data/experiment/reext_t0/t1_sellos_t4.py` y `sellos_t4.json`.

## 4. Lectura

Ficha por unidad: id, TO, páginas, texto propio y heredado, nodos y aristas con su tramo, veredicto (con error / sin error), lo no
sostenido (nodo o arista y por qué), omisiones aparte. Tres lecturas: la primera, de la instancia de la unidad (sin API; lectura
asistida de las 60 fichas); la segunda, completa e independiente, de la mesa que revisa el FRENO L1, sobre las fichas sin el veredicto
de la primera; la adjudicación de la autora sobre las divergencias, como en T4. Valen las marcas que queden después de la
adjudicación.

## 5. Estimadores (escritos antes de leer)

- Por estrato: k_h de n_h, con el intervalo de Wilson al 95 %.
- Ponderado, la tasa del grafo: p̂ = W₁·p̂₁ + W₂·p̂₂, con W₁ = N₁/N y W₂ = N₂/N (1.003/2.366 = 0,424 y 1.363/2.366 = 0,576; L0 los
  recomputa). Intervalo al 95 %: p̂ ± 1,96·√(W₁²·p̂₁(1−p̂₁)/n₁ + W₂²·p̂₂(1−p̂₂)/n₂). Si un estrato da 0 o 30 de 30, ese intervalo colapsa:
  se reporta además el conservador por combinación de los límites de Wilson de cada estrato (W₁·LI₁ + W₂·LI₂; W₁·LS₁ + W₂·LS₂). Las
  dos cifras van al reporte, con la ponderada como la tasa del grafo.
- Descriptivo, sin inferencia: desglose por estado de aceptación y por TO.

## 6. Etapas y escrituras

- L0: población, estratos, sorteo sellado (`data/experiment/lectura_aceptadas/sellos_l0.json`). L1: las 60 fichas con la primera lectura
  (`fichas_l1.jsonl` sin veredictos; `veredictos_l1.jsonl` aparte, para la lectura cegada de la mesa). FRENO L1.
- Revisión del FRENO L1: segunda lectura de la mesa; adjudicación de la autora sobre las divergencias.
- L2: cifras con la adjudicación, estimadores, reporte (`reporte_l2.md`); registro en `docs/insumos_escritura.md` §7 como línea de base
  de la tasa de error por unidad (con autorización en el «seguí» de L2); en el pre-registro de la tanda 1, la vigilancia: por tanda, 30
  unidades aceptadas en un estrato ponderado o 60 en dos estratos (decisión 2), mismo sorteo y criterio; umbral de atención: el límite
  inferior de Wilson de la tanda por encima del límite superior de la tanda 0 (decisión 2 al firmar: 60 en dos estratos). FRENO final.
- Escrituras: `data/experiment/lectura_aceptadas/` (se crea) y el scratchpad; en L2, la línea de `docs/insumos_escritura.md`.

## 7. Precondiciones, prohibiciones y convivencia

- Precondiciones: SC2 de U-SINCOLA-T0 y su sello commiteados (`dde9f44` y `235a295`; `grafos.py` con `commit_sellado` `dde9f44` en las
  dos claves sincola);
  `finales.jsonl` y la E0 r2b iguales al sello (sha256 antes y después); ninguna extracción corriendo sobre `salida_r2b/`.
- Prohibido: la API; tocar los grafos, el crudo, las bases de caché, el código del pipeline; commitear.
- Requisitos, los de CLAUDE.md §4 (a a l): copia sin enlaces para toda corrida; sha256 del repo antes y después; conteos recomputados;
  ninguna acción de la autora como hecha; cero nombres de personas; grep de convenciones al cierre.
- Convivencia: puede correr en paralelo con S1 de U-SEG-OFICIAL, C1 de U-COMP-E1, O1 de U-E3-LISTAS y R2 de U-RERESOL-CAT; no comparte
  archivos con ninguna.
- Esfuerzo: 60 fichas; del orden de 2 h de la instancia, 4 h de la mesa y 1 h de la autora.
