FIRMADO por la autora — 2026-09-27 (gate 6 de la fase 2 de B6.0)

MANDATO — U-GATE6-INTR-CITA (GATE 6 DE LA FASE 2 DE B6.0): MÉTRICAS
INTRÍNSECAS SOBRE GENERACIÓN 3 Y PARAMETRIZACIÓN DE LOS INDICADORES DE CITA.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Costo de API 0.

CONTEXTO (tres líneas). El pre-registro de la tanda 0
(docs/preregistro_tanda0.md, sellado en c80b03f, A5) declara dos
instrumentos PENDIENTES que esta unidad cierra: las métricas intrínsecas,
cuyo script scripts/metricas_intrinsecas.py (sha256 d5a88b79…, commit
c6f808e) está cableado a tres grafos de generaciones 1 y 2 y no mide
ninguno de generación 3; y los indicadores de cita de U-CITA-2, cuyo script
scripts/ucita2_indicadores.py (sha256 bdd00cf7…, commit fb6ef69) tiene
cableados el gold, el manifiesto, el índice E0, las trazas y las tandas de
r1. En la fase 2 los dos deben correr sobre los ensamblados de la tanda 0
(A3.5) y sobre las trazas de las celdas C2 a C4 y de las preguntas nuevas.
La fase 2 no arranca con instrumentos PENDIENTES. Leé la spec
docs/spec_evaluacion_intrinseca.md (sellada en cdf90e6; sha256 8bedc633…)
§4 y §9, la fila de U-CITA-2 bajo B6.3 del plan, y los dos scripts
completos antes de escribir.

DECISIONES YA TOMADAS. No se re-deciden.
1. Nada de lo que hoy producen los dos scripts cambia. Los tres JSON de
   data/experiment/metricas_intrinsecas/ (grafo_v2, reensamblado_v3,
   run_3_ppf_core) y reports/ucita2_indicadores.{json,md} (JSON sha256
   a9d32d3b…) no se reescriben ni se regeneran. Toda extensión es aditiva:
   modo nuevo o argumentos nuevos con default igual al comportamiento
   actual.
2. Fórmulas de la spec intactas. M1, M2, M4, M5, M6, M8 y M9 dependen solo
   del kg.json y se computan sobre generación 3 con el mismo código. M3,
   M7 y M10 dependen de la atribución mención→nodo y del rol documental
   del chunk; para generación 3 se computan solo si el ejecutor declara en
   el JSON, con path:línea, de qué campo del kg.json o de la salida de E0
   sale cada insumo (candidatos a verificar, no a asumir: la lista
   provenances de cada nodo para las menciones fusionadas;
   provenance.rol_documental y el tipo o los flags del chunk en
   chunks_<to>.json para el rol; los chunks de E0 del manifiesto para el
   denominador de M10). Si un insumo no tiene equivalente verificable en
   generación 3, la métrica se reporta no_computable con el motivo, como
   ya hace run_3 (metricas_intrinsecas.py:417-425). Ningún mapeo se
   inventa para que la métrica salga.
3. Custodia en generación 3 (spec §9, método U0): el grafo se acepta para
   medir solo si su sha256 coincide con el que el ejecutor declara en el
   JSON y con el registrado en el repo para ese grafo (r1: 0226e947…). Si
   además ensamblar_r1.py admite re-ensamblar a un directorio fuera del
   repo sin editarlo (r1_comun.py:27-28 fija salida y salida_r1 como
   constantes: mostrá si se pueden redirigir sin tocar el archivo), se
   re-ensambla y se compara por igualdad de ids de nodos y triplas, como
   hacen custodia_v2 y custodia_v3 (:271-292). Si no, la custodia queda
   declarada como «por sha256» en el JSON y se reporta como limitación,
   sin editar ensamblar_r1.py ni r1_comun.py.
4. Interfaz nueva de metricas_intrinsecas.py: sin argumentos,
   comportamiento idéntico al actual (los tres grafos cableados en :64-66
   y :666-670). Con --gen3 --kg RUTA --nombre NOMBRE --e0 DIRECTORIO
   [--manifiesto RUTA] mide un solo grafo de generación 3 y escribe
   data/experiment/metricas_intrinsecas/<NOMBRE>.json con la misma
   estructura de claves que los JSON existentes (spec,
   spec_commit_sellado, spec_sha256, script_sha256, rapidfuzz_version,
   umbral_similitud, fecha, custodia, grafo, kg_path, nodos_totales,
   metricas) más una clave adaptador_gen3 con las declaraciones de la
   decisión 2. Dos corridas con los mismos argumentos deben dar JSON
   idénticos salvo fecha y script_sha256; la comparación se hace
   excluyendo esas dos claves.
5. Interfaz nueva de ucita2_indicadores.py: sin argumentos, comportamiento
   idéntico al actual. Argumentos nuevos, cada uno con default igual a la
   constante que reemplaza: --gold (:70), --manifiesto (:71), --e0 (:72),
   --trazas (:73), --tandas (lista; :78), --out-json y --out-md (:74-75).
   Los TOs se leen del manifiesto en vez de la tupla de :77. Los candados
   de sha de insumos (:81-91) y de digest de tandas (:93-99) rigen solo
   cuando los argumentos son los defaults; con argumentos distintos, el
   script registra en el JSON el sha256 de cada insumo y el digest de cada
   tanda como «medidos, sin esperado» y no frena por ellos. La
   conciliación con las cifras de U-CITA (:103-111) rige solo con las
   tandas default; con otras, la sección se emite vacía y rotulada «sin
   conciliación». Las funciones importadas del harness congelado
   (cita_fiel, norm_loc) no se tocan; el harness no se edita.
6. Salidas de prueba de esta unidad: (a)
   data/experiment/metricas_intrinsecas/kg_reextraido_r1.json, medición de
   r1 con --gen3, que queda como LÍNEA DE BASE de generación 3 para la
   lectura de intrínsecas en la fase 2 (A9 paso 7); (b) para los
   indicadores de cita, ninguna salida nueva en el repo: la prueba de la
   parametrización es que la corrida con argumentos explícitos iguales a
   los defaults reproduce reports/ucita2_indicadores.json, comparado
   excluyendo la clave script.

TAREA (una sola unidad):
A. Extender scripts/metricas_intrinsecas.py según las decisiones 2, 3 y 4.
   Antes de editar, corré el script actual sin argumentos con OUT_DIR
   redirigido a tu scratchpad (sin tocar el repo: mostrá cómo lo
   redirigiste) y guardá los tres JSON como línea de base pre-edición;
   después de editar, volvé a correrlo igual y compará los tres contra la
   línea de base excluyendo fecha y script_sha256: deben ser idénticos.
   Los tres JSON del repo no se tocan.
B. Correr --gen3 sobre r1
   (data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json, sha256
   0226e947…; --e0 data/experiment/reextraccion_v2/e0_chunking/salida_enm01;
   --manifiesto data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json)
   dos veces; comparar excluyendo fecha y script_sha256; dejar el JSON de
   la decisión 6 (a). Reportá M1 a M10 tal como den, con cuáles quedaron
   no_computable y por qué.
C. Extender scripts/ucita2_indicadores.py según la decisión 5. Correrlo
   (i) sin argumentos, con las salidas redirigidas a tu scratchpad por
   --out-json y --out-md, y (ii) con todos los argumentos explícitos
   iguales a los defaults; las dos salidas JSON deben ser idénticas entre
   sí y a reports/ucita2_indicadores.json excluyendo la clave script (cmp
   sobre versiones sin esa clave; sha256 de las tres). Después (iii) una
   corrida con --tandas reducida a ev2_r1_base sola y --out al scratchpad,
   para probar que la lista de tandas es parámetro: los agregados de
   ev2_r1_base deben ser iguales a los del reporte sellado (cita fundada
   38 de 40, existente 40 de 40, al ancla 32 de 40 en todas; 31, 30 y 28
   en contenido N=31).
D. Selftest scripts/selftest_gate6.py, solo stdlib en su propio código
   (invoca los dos scripts por subprocess con .venv/bin/python y
   PYTHONDONTWRITEBYTECODE=1): (i) metricas sin argumentos contra la línea
   de base pre-edición de A; (ii) --gen3 sobre un grafo sintético mínimo
   de generación 3 escrito en el selftest, con provenances,
   rol_documental y un E0 sintético de dos chunks, que verifica M4, M8 y
   M9 a mano y la byte-identidad de dos corridas; (iii) ucita2 con
   argumentos explícitos contra el reporte sellado, excluyendo script.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Escrituras permitidas: scripts/metricas_intrinsecas.py y
  scripts/ucita2_indicadores.py (ediciones aditivas),
  scripts/selftest_gate6.py (nuevo),
  data/experiment/metricas_intrinsecas/kg_reextraido_r1.json (nuevo), y tu
  scratchpad. Nada más: ni los tres JSON existentes de intrínsecas, ni
  reports/ucita2_indicadores.*, ni el harness, ni ensamblar_r1.py, ni
  r1_comun.py, ni ningún kg.json ni archivo de E0, ni docs/, ni el plan.
  No commitees. Costo de API 0. Zonas selladas de CLAUDE.md §3 intactas.
- PYTHONDONTWRITEBYTECODE=1 en todo Python que corras; ningún __pycache__
  ni .pyc nuevo en el repo. Los scripts de intrínsecas corren con
  .venv/bin/python (rapidfuzz 3.14.5 está en el .venv; anotá la versión en
  el reporte).
- Los artefactos de custodia van a /tmp o al scratchpad, nunca al repo
  (spec §9).
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO, no
  se infiere.
- Cero nombres propios de personas; los mentores solo por rol.
- Paquete de revisión revision_GATE6/ en tu scratchpad con manifest.txt
  (sha256 y una línea por archivo): la línea de base pre-edición de A, las
  salidas de B y C, el diff completo de los dos scripts editados, la
  salida del selftest y el estado del árbol. Reporte al frenar de no más
  de 40 líneas.
- Si tu contexto se acerca al límite o vas a compactar, ANTES escribí en
  tu scratchpad checkpoint_GATE6.md con qué piezas (A–D) están hechas y
  qué corridas hiciste, y reportá la ruta.

CRITERIO DE ACEPTACIÓN, con salida en el reporte: git diff --stat de los
dos scripts editados y git status --short mostrando solo los dos scripts
modificados, el selftest y el JSON de r1 como nuevos, más adjudicar.py
preexistente; los tres JSON existentes de intrínsecas y
reports/ucita2_indicadores.* sin cambio (git diff vacío sobre ellos);
pieza A: tres comparaciones pre y post idénticas excluyendo fecha y
script_sha256; pieza B: dos corridas de r1 idénticas con la misma
exclusión, tabla M1 a M10 con valor o no_computable y motivo, custodia
declarada; pieza C: las tres comparaciones de (i), (ii) y (iii) con
sha256; selftest en verde con la cuenta de casos; grep de convenciones
sobre los cuatro archivos, pegado aunque dé vacío.

FRENO al terminar. La autora revisa el diff antes de commitear; el gate 6
se cierra en el plan con el commit.
