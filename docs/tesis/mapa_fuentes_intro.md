# Mapa de fuentes para la introducción (C1.1-prep, 2026-08-23; filas 15–20 y precisión de la fila 2 agregadas en la unidad de redacción de la Introducción, 2026-09-01)

Regla (main.tex + skill latex-udesa): en la prosa entra un número solo si está
en esta tabla, parseado del archivo citado. Si al redactar aparece un número
sin fila acá, va primero a §«No verificables» y no se usa hasta resolverse.

**Excepción registrada (04/09):** los números que la prosa atribuye a
trabajos citados (cifras de iKraph, GPTKB, PrimeKG, etc.) no llevan fila en
esta tabla: se respaldan en la fuente citada y en su verificación registrada
en el mapa de related work y en releases_kg_post_llm.md. Esta tabla rige los
números del propio proyecto.

## Convenciones — excepción registrada

La portada de `main.tex` lleva los nombres de la autora y de los mentores por
requisito del formato institucional del Informe de PF. Es la ÚNICA excepción a
la convención de cero nombres propios (CLAUDE.md §5); el grep de convenciones
del cierre de unidades debe excluir la portada.

## Tabla de números citables

| # | Número exacto | Archivo (repo) | Commit |
|---|---|---|---|
| 1 | Fidelidad EV2 definitiva: KG-Base 3/20/17 · KG-Reextraído 4/27/9 · KG-Refinado 5/26/9 (correcto/parcial/incorrecto sobre 40) | `data/experiment/ev2_adjudicacion/adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.md` | `64de678` |
| 2 | Juez de fidelidad validado sobre una muestra ciega de 12 respuestas: acuerdo exacto 11/12; por criterio 52/53 (98,1 %) | `data/experiment/ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.md` | `64de678` |
| 3 | Clase modal `generacion`: 17/25/21 por grafo (sobre 40); navegación dominante en incorrectos de KG-Base (10/17); techo de retrieval 14/7/6 | `data/experiment/ev2_reporte/salida/atribucion_fallas.md` (tabla de clases por grafo) | `85d9fdb` |
| 4 | Grounded ≠ correct (frozen): 8 falsas con cita real sobre 200 adjudicadas (172 V / 8 F / 4 P / 16 NV) | `data/experiment/evaluacion/frozen_run/reporte_final.md` (línea 5) | tandas `fb685a7`/`7942ead` |
| 5 | Alucinación con retrieval perfecto: RT-C6-1 incorrecta 3/3 con `ver_nodo` byte-idéntico | `data/backlog/backlog.jsonl` (BKL-0026) | `24432a4` |
| 6 | Tamaños: KG-Base 4.050/6.634 (12 rel.) · KG-Refinado 4.469/8.073 (16) · KG-Reextraído 6.178/11.415 (11) · KG-Reextraído-r1 6.529/17.772 (16) | los cuatro `kg.json` (conteo por parseo) | `58581b6` / `05984e1` / `5273c0c` / `185e042` (+ fe de erratas `6c5507b`) |
| 7 | Referencias norma→norma en r1: 5.645 aristas `referencia` con evidencia | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/reporte_ensamblado_r1.json` | `185e042` |
| 8 | Banco de evaluación: 43/43 tool calls correlacionadas al log del servidor; replay estándar y fuerte 4/4; R9 == CLI 12/12 | `data/experiment/banco_mcp/smoke/resultados/faseB_corrida2/reporte_faseB_corrida2.md` | `1fa79de` |
| 9 | Ablación de retrieval: recall consultada literal 0,887→0,981 (IC95 excluye 0); la brecha anti-léxica NO se cierra (de 20 fallas: 7 de búsqueda, 13 de selección del agente) | `data/experiment/ablacion_retrieval/corrida/resultados/analisis_ablacion.json` | `ffc6ff6` |
| 10 | Head-to-head KG-RAG vs RAG | **PENDIENTE de A2.2** — en la prosa: hueco `[TODO: A2.2]` | — |
| 11 | Censo de fidelidad de r1: 31/40 anclas presentes (única recuperada `cla:3.5`; 7 granularidad + 2 contenedor, H24) | `data/experiment/ev2_r1/censo/censo_anclas_fidelidad_r1.json` | `6c5507b` |
| 12 | Bake-off de embeddings: harrier 52/36 vs BM25 72/16 (literal@1/anti-léxica@1); modelo no elegible por licencia no supera al elegido | `data/experiment/bakeoff_embeddings/bakeoff_embeddings.md` §3 | `df9da34` |
| 13 | Tabla definitiva de KG-Reextraído-r1: 6/26/8 (correcto/parcial/incorrecto sobre 40; vías 11 juez_base / 21 juez_enc / 5 adjudicación base / 3 adjudicación §7); dentro de la banda de no-señal vs KG-Refinado (5/26/9); P1–P5 6/6; juez vs autora 4/4 y 15/15 (con salvedades de `nota_episodios_adjudicacion.md`) | `data/experiment/ev2_r1/cierre/reporte_final_r1.md` | `774acac` |
| 14 | Laudo de promoción: KG-Reextraído-r1 (`0226e947`) es el grafo VIGENTE — promoción del entregable con banda de no-señal declarada; costo anotado cobertura 69 vs 73; migración declarada por `plan_carga_r1.md` | `docs/laudo_promocion_r1_vigente.md` | `81587f9` |
| 15 | Corpus: 157 Textos Ordenados vigentes en el índice oficial al momento del relevamiento (157 URLs únicas; 158 entradas con 1 duplicado) y 7.321 páginas = 6.757 (corpus escalado) + 564 (conjunto de desarrollo) | `data/experiment/escalado_prep/inventario_resumen.json` + `indice_oficial_raw.json` (157); `data/experiment/escalado_prep/resumen_escalado.md` línea 43 (6.757); `data/experiment/escalado_prep/referencia_subset.json` (564) — inventario_recurso.md §G.4, §B.1 y §B.2 | `111ed19` |
| 16 | Conjunto de evaluación de fidelidad: 40 preguntas / 164 criterios de clave, sellado antes de toda corrida; dosificación ext 16 / cap 8 / cla 6 / ric 5 / pro 5 | `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` + manifest `data/experiment/exploracion/ev2_sellado/manifest_ev2.txt` — inventario_recurso.md §D, fila «EV2 — fidelidad» | sello `9c44516`; cierre `64de678` |
| 17 | Atribución causal completa por grafo (ausencia en el grafo / no alcanzado / visto sin consultar / generación): KG-Base 6/11/3/17 · KG-Refinado 4/6/1/25 · KG-Reextraído 9/1/5/21, sobre 37/36/36 trazas atribuibles (base 120 trazas) | `data/experiment/ev2_reporte/salida/atribucion_fallas.md` §1.a (líneas 15–17); regla en `data/experiment/ev2_reporte/regla_atribucion.md` §4 — inventario_recurso.md fila 5 y §G.2 | salida `85d9fdb`; regla `40603a9` |
| 18 | Procedencia del grafo de desarrollo: 6.510/6.529 nodos y 17.690/17.772 aristas con punto+unidad+páginas; 19 nodos y 82 aristas solo de esqueleto; 0 sin ninguna (partición exacta) | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` (parseo de provenance) — inventario_recurso.md §G.3 | `185e042` |
| 19 | Remisiones entre puntos del grafo de desarrollo: 5.680 aristas `referencia` totales (5.645 nuevas con evidencia + 35 previas) | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` (parseo) — inventario_recurso.md fila 19 | `185e042` |
| 20 | Esquema: 6 tipos de entidad (`ENTITY_TYPES`, líneas 24–31), 12 predicados (`PREDICATES`, líneas 41–54), 5 relaciones de ensamblado (4 de `RELACIONES_ESQUELETO`, líneas 76–81, más `padre_sugerido`, línea 234) | `data/experiment/grafo_v2/code/schema.py` — inventario_recurso.md §G.1 y §A.1 (nota de la release vigente) | `fac503f` |
| 21 | Ejemplo de la Figura 1 («de la norma al grafo»): 6 nodos, 5 aristas, 3 resaltadas «remite a» | `docs/tesis/figuras/LEEME_figura_norma_a_grafo.md` §§6–7 y §10 (caso y correspondencia verificados contra `salida_r1/kg.json`) | working tree — entra en el commit de esta unidad (LEEME whitelisteado acá) |
| 22 | Conjunto de desarrollo: cinco Textos Ordenados | `data/experiment/escalado_prep/referencia_subset.json` — inventario_recurso.md §B.2 | `111ed19` |
| 23 | Las tres operaciones del agente (buscar nodos, abrir un nodo, listar vecinos) | `data/experiment/evaluacion/harness.py` (constante `TOOLS`: buscar_nodos / ver_nodo / ver_vecinos) | `7e8b91e` |

## No verificables

(vacía — todo número propuesto hasta ahora tiene fila arriba; esta sección
existe para recibir lo que no la tenga.)

## Figuras candidatas (decisión de la autora)

1. Subgrafo real de r1 (propuesta: la cláusula del 125 % con sus 6 nodos en 5
   puntos y las aristas `referencia`; o el 3.9 de ext con su excepción) —
   generable $0 desde `salida_r1/kg.json`; PNG/SVG a `figuras/`.
2. Diagrama del pipeline E0→E5→releases (TikZ/SVG propio).
3. Tabla de clases causales por grafo (booktabs, desde la fila 3 de esta tabla).
4. Tabla del bake-off léxico vs denso (si la Discusión la pide).
