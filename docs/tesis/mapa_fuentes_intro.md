# Mapa de fuentes para la introducción (C1.1-prep, 2026-08-23)

Regla (main.tex + skill latex-udesa): en la prosa entra un número solo si está
en esta tabla, parseado del archivo citado. Si al redactar aparece un número
sin fila acá, va primero a §«No verificables» y no se usa hasta resolverse.

## Convenciones — excepción registrada

La portada de `main.tex` lleva los nombres de la autora y de los mentores por
requisito del formato institucional del Informe de PF. Es la ÚNICA excepción a
la convención de cero nombres propios (CLAUDE.md §5); el grep de convenciones
del cierre de unidades debe excluir la portada.

## Tabla de números citables

| # | Número exacto | Archivo (repo) | Commit |
|---|---|---|---|
| 1 | Fidelidad EV2 definitiva: KG-Base 3/20/17 · KG-Reextraído 4/27/9 · KG-Refinado 5/26/9 (correcto/parcial/incorrecto sobre 40) | `data/experiment/ev2_adjudicacion/adjudicacion_SOLO_MESA/cruce_definitivo_por_grafo_SOLO_MESA.md` | `64de678` |
| 2 | Juez de fidelidad validado: acuerdo exacto 11/12; por criterio 52/53 (98,1 %) | `data/experiment/ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.md` | `64de678` |
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
