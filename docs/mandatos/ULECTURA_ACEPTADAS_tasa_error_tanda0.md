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

## Notas posteriores a la firma

El texto firmado (las 76 líneas anteriores a esta sección, `9502ca4`) no se edita; estas notas se leen junto con él.

- **06/10/2026 — revisión del FRENO L1 y segunda lectura de la mesa (L0 y L1 sin commit al escribir esta nota).** La mesa leyó a ciegas las
  60 fichas de `fichas_l1.md` (sin los veredictos de la instancia) con el criterio del §1 y después comparó: el mismo veredicto en las 60
  (ítems 6 de 30 con error: `cap::5.4.5`, `ext::3.17.3.4`, `ctacte::6.1.2.5`, `ext::7.9.1.1`, `ctacte::6.1.2.7`, `lingob::2.3.2.1`; no ítems 4
  de 30: `ext::7.3.11`, `ext::10.2.4::cierre`, `ctacte::1.5.2.9`, `ctacte::9.1.3`), sin divergencias; un matiz en `ext::3.17.3.4` (la mesa señala
  A1 y la instancia A2: las dos aristas quedan sin sostén). Los cuatro casos límite que la instancia declaró se leen igual (`cap::5.4.5`,
  `lingob::2.3.2.1` y `ctacte::9.1.3` con error; `ext::14.2.1.6` sin error, con observación de mención). Decisiones de la autora: (1) tres
  cifras en el reporte y en la vigilancia por tanda: la tasa de la unidad con el criterio de T4 (la extracción), comparable con los 12 de 30 de
  la cola; aparte, la de las `remite_a` por cita y destino (hoy 0 de 167 en 11 unidades); y los tipos documentales mal asignados
  (`Comunicacion` para un punto del mismo TO o para una ley) como observación, no como error, como en T4; (2) `cla::1.2.1`, vista por la
  instancia antes del sello, se declara en el reporte de L2 con la coincidencia de las dos lecturas y no se reemplaza (la semilla la fija la
  firma y el sorteo no depende de lo que se mire). La adjudicación de la autora sobre las 10 con error y las dudas es el hueco del «seguí» de
  L2; L2 computa los estimadores con ella.
- **07/10/2026 — revisión del FRENO L2 por la mesa (L2 sin commit al escribir esta nota; L0 y L1 en `6e611d6`).** Reproducido sobre
  una copia sin enlaces con un script propio, desde `veredictos_l1.jsonl`, `adjudicacion_autora_l2.json` y `sellos_l0.json`: las 48 cifras
  de `estimadores_l2.json` coinciden a 1e-6 (ítems 6 de 30 [0,0951; 0,3731]; no ítems 4 de 30 [0,0531; 0,2968]; W₁ = 1.003/2.366;
  ponderada 0,1616 ± 0,0927 = [0,0689; 0,2543], intervalo de Wald sobre el estimador estratificado como dice el §5; conservador
  [0,0709; 0,3291] = la combinación de los límites de Wilson por estrato; cola de T4 12 de 30 [0,2459; 0,5768]; `remite_a` 0 de 167 en 11
  unidades; 4 nodos `Comunicacion` en 2 unidades). La adjudicación volcada es exactamente la de las 10 unidades con error de la primera
  lectura, y agrega la arista A1 de `ext::3.17.3.4` con la razón de la segunda lectura; los 15 elementos están en sus fichas. Dos corridas de
  `l2_estimadores.py` sobre la copia, iguales salvo la hora; `docs/insumos_escritura.md` §7, ítem 5: 11 líneas agregadas, cifras iguales a
  las del JSON. El repo no cambió durante la verificación (sha256 antes y después; 2.213 `.pyc`).
  - **Vigilancia (reporte §8): observación de la mesa para el pre-registro de la tanda 1, no para este mandato.** La regla «LI de Wilson de
    la tanda por encima del LS de la tanda 0» dispara con 17 de 30 ítems o 14 de 30 no ítems: si la tasa real de una tanda duplicara la
    línea de base (0,40 y 0,27), la probabilidad de disparar sería 0,05 y 0,29 (binomial exacta). La mesa propone al pre-registro dos
    niveles por estrato con la misma muestra: atención con el test binomial exacto unilateral contra la tasa de la tanda 0 al 5 %
    (11 de 30 ítems, 8 de 30 no ítems; potencia 0,71 y 0,96 si la tasa se duplica), que amplía la lectura con 30 unidades más del
    estrato, y freno con la regla de los intervalos disjuntos o con la atención confirmada sobre las 60; y el mismo test sobre el
    acumulado de las tandas desde la tanda 2. La ponderada se reporta con el intervalo del §5; el conservador no se usa como umbral,
    porque es una envolvente de los límites por estrato y no un intervalo de confianza. Cálculo y tabla:
    `hoja_de_ruta_tanda1_mesa/analisis_vigilancia_lectura_aceptadas_L2_mesa.md` (scratchpad de la mesa). Decide la autora al firmar el
    pre-registro.
  - L2 es la última etapa: el commit de L2 cierra la unidad. Commit PENDIENTE de la autora.
- **07/10/2026 — L2 commiteada en `86324cc`: la unidad queda CERRADA. Decisión de la autora sobre la vigilancia:** la regla por
  tanda es la de dos niveles por estrato propuesta por la mesa (atención con el test binomial exacto unilateral contra la tasa de
  la tanda 0 al 5 %: 11 de 30 ítems, 8 de 30 no ítems, que amplía la lectura con 30 unidades más del estrato; freno con los
  intervalos disjuntos o con la atención confirmada sobre las 60; el mismo test sobre el acumulado desde la tanda 2; la
  ponderada se reporta con el intervalo del §5 y el conservador no es umbral). Se asienta en el pre-registro de la tanda 1 (A4),
  no en este mandato ni en el reporte de L2, que quedan como están.
