FIRMADO por la autora — 2026-09-26 (re-diagnóstico de B2.1 fase 1 porque el paquete original del 15/09 se perdió con el scratchpad; redactado por la mesa el 26/09 con cotejo de insumos contra HEAD)

MANDATO — U-B2.1 FASE 1 (RE-DIAGNÓSTICO): INVENTARIO PARA LA REGRESSION SUITE.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Costo de API 0.

CONTEXTO (tres líneas). La fila B2.1 del plan (docs/plan_tesis.md, hoy
:324; el ancla es el id de la fila) prevé scripts/regression_kg.py:
convertir cada defecto cerrado del backlog, los tests T1–T7 de r1 y las
reglas declaradas de E4 en tests de respuesta conocida determinísticos,
ejecutables sobre cualquier kg.json. La fase 1 se corrió el 15/09 y su
resultado está asentado en esa fila, pero el paquete con el inventario y
las sondas vivía en un scratchpad que se perdió (docs/mandatos/historico/
guarda el mandato reconstruido). Esta unidad rehace el diagnóstico y lo
deja dentro del repo.

DECISIONES YA TOMADAS. No se re-deciden.
1. Es SOLO diagnóstico. No se implementa nada de la suite; no se edita
   ningún archivo existente del repo.
2. Universo del inventario, tres grupos:
   (i) BKL cerrados: entradas de data/backlog/backlog.jsonl (sha256
       d8473501…, verificalo y mostralo) con estado efectivo aplicado o
       verificado. El archivo es un registro de eventos: 74 líneas para
       29 ids; una entrada tiene varias líneas y solo algunas traen el
       campo estado (la entrada inicial y los eventos cambio_estado); las
       líneas de evento nota, aplicacion y retriage_v3 no lo traen. El
       estado efectivo de un id es el de su última línea que trae estado.
       Reconstruilo con un script guardado en el paquete y mostrá su
       salida: la regla anterior debe dar 12 ids verificado. Sus retests
       están en data/backlog/retests/ (C1 a C7, siete archivos) y sus
       propuestas selladas en data/backlog/propuestas/ (seis archivos).
       BKL-0024 y BKL-0025 tienen estado efectivo triaged; no hay ids RT-
       en el backlog: las preguntas RT son RT-C5-1..5, RT-C6-1..4 y
       RT-C7-1..3 y viven en las propuestas y en el retest C7. Localizá
       cada una con comando; lo que no aparezca, NO ENCONTRADO con el
       comando.
   (ii) Tests T1–T7 de r1: data/experiment/reextraccion_v2/corpus_v2/
       r1_tests.py (sha256 fe1c7476…; T1–T3 delegan en
       ensamblar_corpus.tests_respuesta_conocida, ensamblar_corpus.py:233),
       más las invariantes I1–I5 de r1_invariantes.py (sha256 77123142…,
       enunciados en sus líneas 7–11).
   (iii) Reglas de E4: data/experiment/reextraccion_v2/corpus_v2/r1_e4.py
       (sha256 179db09c…): resolución de propuestos por label exacto,
       alias declarado, slug, singularización por token, sigla
       condicionada; TextoOrdenado canónico desde provenance; filtro de
       conflictos. Leídas del código y de su docstring, con path:línea
       por regla.
3. Un «test de respuesta conocida sobre cualquier kg.json» es una
   comprobación determinística de una de estas formas: nodo presente,
   ancla (punto de provenance) presente, valor de propiedad, arista
   presente o ausente, o rank en buscar_nodos. La última depende de un
   retriever; anotá de cuál (in-memory de
   data/experiment/evaluacion/harness.py o Neo4j) y qué config.
4. Los cuatro grafos sobre los que se sondea, con su sha256 a verificar y
   mostrar: KG-Base data/experiment/run_3_ppf_core/kg.json (12c226e2…),
   KG-Refinado data/experiment/grafo_v2/reensamblado_v3/kg.json
   (26fac8b4…), KG-Reextraído data/experiment/reextraccion_v2/corpus_v2/
   salida/kg.json (8e2eadee…), KG-Reextraído-r1
   data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json
   (0226e947…). Todos son solo lectura.
5. RESULTADO ESPERADO, ya asentado en la fila B2.1 del plan por la
   corrida del 15/09: 46 ítems = 12 BKL cerrados (estado efectivo
   verificado: 0003, 0004, 0005, 0006, 0007, 0017, 0019, 0023, 0026,
   0027, 0028, 0029) + 12 preguntas RT + T1–T7 e I1–I5 + 10 reglas de E4;
   14 convertibles, 28 con condición, 4 no convertibles (BKL-0026 y
   BKL-0027 son conducta del agente; I1 e I2 exigen los grafos
   pre-merge); 15 dependen de retriever; y dos contradicciones: C4
   (subclase_de laudada en KG-Refinado) contra T7 de r1 (padre_sugerido
   flaggeado), y BKL-0024/0025 nombrados «cerrados» en el plan y triaged
   en el backlog. Toda diferencia entre lo que midas y esto se reporta
   como HALLAZGO, con el comando y el artefacto que la sostienen; no se
   ajusta ni el conteo ni la clasificación para que coincidan.

TAREA (una sola unidad): escribir el directorio nuevo
reports/revision_UB21_diag/ con estas piezas.
a. inventario_B21_fase1.md — INVENTARIO, una fila por ítem de los tres
   grupos: id, qué afirma (una oración), sobre qué grafo se verificó
   (path y sha si está registrado), evidencia del cierre (path del retest
   o del test), y qué cambió en el pipeline o en el grafo para cerrarlo.
   En el mismo archivo, CONVERTIBILIDAD por fila: convertible /
   convertible con condición / no convertible, con la forma de test de la
   decisión 3 y la razón; para los convertibles con condición, qué
   necesitaría: cómo se direcciona el objeto cuando los ids de nodo
   cambian entre grafos (por tipo y label, por punto de provenance, por
   conjunto de provenances, nunca por provenance[0] solo), qué fixture
   haría falta, y si el test tiene sentido sobre un grafo que no pasó por
   r1. Y SOLAPAMIENTOS: qué ítems ya cubren T1–T7, las invariantes o una
   shape de scripts/shapes_validator.py (incluido el perfil congelado de
   f4c8e93, S19–S23), con path, para que la suite no duplique.
b. tabla_resumen_B21_fase1.md — conteos: ítems por grupo, convertibles,
   con condición, no convertibles, cuántos dependen del retriever, y la
   comparación fila por fila contra el resultado esperado de la decisión
   5, con la columna «coincide / HALLAZGO». Recomputá cada conteo contra
   la tabla de a antes de escribirlo.
c. lo_que_no_esta_B21_fase1.md — entradas del backlog cuyo estado
   efectivo no es aplicado ni verificado (triaged, sin estado), solo
   contadas y listadas por id; no entran al inventario.
d. estado_backlog_B21_fase1.py y estado_backlog_B21_fase1_salida.txt — el
   script de la decisión 2 (i) y su salida.
e. Las sondas determinísticas con las que verificás lo que el inventario
   afirma, cada una como script más salida:
   sonda_T1_T7_cuatro_grafos_UB21.py y su _salida.txt (T1–T7 sobre los
   cuatro grafos de la decisión 4), sonda_anclas_C1_C7_UB21.py y su
   _salida.txt (anclas de C1 a C7), y una tercera si el diagnóstico la
   necesita, con nombre que diga qué sondea. La fase 1 original tuvo
   tres; el nombre de la tercera no quedó registrado. Ninguna sonda
   escribe fuera del directorio.
f. manifest.txt — sha256 y una línea de descripción por archivo del
   directorio, más el estado del árbol de trabajo (git status --short
   pegado).

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Única escritura en el repo: el directorio nuevo
  reports/revision_UB21_diag/. No editás ningún archivo existente: ni el
  backlog, ni r1_tests.py, ni el plan, ni ningún kg.json. Tu scratchpad
  solo para el checkpoint. No commitees. Costo de API 0. Zonas selladas
  de CLAUDE.md §3 intactas.
- PYTHONDONTWRITEBYTECODE=1 en todo Python que corras; ningún __pycache__
  ni .pyc nuevo en el repo.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO, no
  se infiere. Tu memoria de sesión no es fuente; el plan tampoco lo es
  para los conteos: el plan dice lo esperado, los artefactos dicen lo
  medido.
- Cero nombres propios de personas; los mentores solo por rol; decisiones
  por justificación técnica.
- Reporte al frenar de no más de 40 líneas; lo largo va al directorio.
- Si tu contexto se acerca al límite o vas a compactar, ANTES escribí en
  tu scratchpad checkpoint_UB21_rediag.md con qué piezas (a–f) están
  hechas, qué grupo del inventario va por dónde y qué archivos leíste, y
  reportá la ruta.

CRITERIO DE ACEPTACIÓN, con salida en el reporte: pieza a con una fila
por ítem de los tres grupos y ninguna fila sin evidencia de cierre o sin
la marca NO ENCONTRADO; la suma de la pieza b cierra contra la pieza a y
cada fila de la comparación dice «coincide» o «HALLAZGO» con su
evidencia; cada RT y BKL-0024/0025 resueltos como encontrados o NO
ENCONTRADO con comando; los cuatro sha de los grafos y los cuatro de los
insumos de la decisión 2 iguales a los declarados, pegados; git status
--short muestra solo reports/revision_UB21_diag/ como no rastreado, más
adjudicar.py, preexistente; grep de convenciones sobre el directorio,
pegado aunque dé vacío; ninguna línea de código de la suite escrita.

FRENO al terminar. La autora revisa el directorio antes de commitear; la
fase 2 tiene mandato propio.
