BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA (redactado 15/09; NO despachado)

MANDATO — U-B2.1 FASE 2: LA REGRESSION SUITE scripts/regression_kg.py.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.

CONTEXTO (dos líneas). La fase 1 (paquete revision_UB21_diag/, inventario
inventario_B21_fase1.md) inventarió 46 ítems —12 BKL cerrados, 12 preguntas
RT, T1–T7 e I1–I5, 10 reglas de E4— y clasificó 14 convertibles, 28 con
condición y 4 no convertibles, con sondas determinísticas sobre cuatro
grafos. Esta fase escribe la suite que convierte cada ítem en un test de
respuesta conocida sobre cualquier kg.json y produce la tabla defecto →
resuelto / persiste / no aplicable por grafo.

DECISIONES YA TOMADAS (autora, 15/09). No se re-deciden.
1. Direccionamiento sin ids: todo objeto se localiza por (archivo del TO,
   punto ∈ conjunto de provenances, tipo, cadena normalizada en label o
   properties). Nunca por provenance[0] ni por id de nodo.
2. Adaptador de provenance gen 2 / gen 3 dentro de la suite, como módulo
   propio: gen 2 lee source_doc y location («Punto 1.2.» → 1.2); gen 3
   lee provenances[].archivo y provenances[].punto. No se comparte código
   con el perfil de B2.2 en scripts/shapes_validator.py; sí la regla.
3. Política de cuarentena como parámetro por generación:
   --politica-cuarentena laudada espera subclase_de desde los propuestos
   (KG-Refinado, laudo C4); flaggeada espera padre_sugerido (r1, T7). El
   laudo (d) pendiente de U-B1a decide el final; la suite no lo anticipa.
4. Tests de rank (RK) solo con el retriever in-memory GraphIndex de
   data/experiment/evaluacion/harness.py, que es el que selló los ranks,
   con limite y query declarados en cada test. Ningún test usa Neo4j. La
   forma «posición en la ventana de ver_vecinos» (C4 paso e) se reduce a
   arista presente.
5. Las queries de los proxies RT de C5 y C6 no están en el repo y NO se
   re-derivan: RT-C5-1..4 y RT-C6-1..3 entran solo como tests de valor
   (gold textual presente en el portador), sin RK.
6. Salida: tabla defecto → estado por grafo, con tres estados posibles:
   resuelto / persiste / no_aplicable, en .md y en .json por grafo.
6bis. El estado esperado por grafo se sella como FIXTURE de la suite
   (scripts/regression_kg_esperado.json). «Regresión» = un ítem cuyo
   estado medido difiere del esperado en la fixture, nunca respecto de la
   corrida anterior. El código de salida es distinto de 0 solo si hay
   regresión; «persiste» esperado no es fallo.
7. Catálogo como parámetro leído del artefacto: --catalogo
   data/experiment/grafo_v2/esquema_v2_clases.json o
   data/experiment/esq_v3_miembros/esquema_v3_clases.json. Nunca copiado
   en la suite.

TAREA (una sola unidad): escribir scripts/regression_kg.py, su fixture y
su selftest.
a. Un test por ítem del inventario (46), con el id del inventario como
   nombre. Los 4 no convertibles (BKL-0026, BKL-0027, I1, I2) figuran en
   la suite con estado fijo no_aplicable y la razón del inventario; no se
   inventa un test para ellos.
b. Formas de test: nodo presente/ausente, ancla presente, valor de
   propiedad, arista presente/ausente, rank en buscar_nodos (solo
   in-memory). Cada test declara su forma, su direccionamiento (decisión
   1) y su evidencia de origen (retest, propuesta o r1_tests.py, con
   path:línea).
c. Reglas de E4: los tests importan r1_e4.indice_catalogo y
   r1_e4.resolver_label y e2_lib.slugify_full en lugar de reimplementar
   los criterios; lo que solo es observable con el grafo pre-E4 (parte de
   E4-a8, E4-c) se declara no_aplicable con la razón.
d. T1–T7: la suite NO edita r1_tests.py ni ensamblar_corpus.py; reescribe
   los siete tests sobre el adaptador (decisión 2) para que corran sobre
   gen 2 sin FAIL por formato. T4 lee el conjunto del esqueleto del grafo
   de referencia (--esqueleto-referencia, default KG-Refinado) en vez de
   cablear 82. T5 direcciona por (ancla origen, ancla destino, evidencia
   verbatim) desde referencias_muestra30_inspeccionada_A2.json, no por
   ids.
e. BKL-0023: sin umbral en el nodo, estado no_aplicable (no pass vacuo).
   BKL-0029: no_aplicable en todo grafo que no cubra convca. BKL-0007:
   dedupe con BKL-0017, sin test propio.
f. Fixture scripts/regression_kg_esperado.json, en dos partes rotuladas:
   (f.1) ESTADO ESPERADO, solo para KG-Refinado reensamblado_v3
   (26fac8b4…) y KG-Reextraído-r1 salida_r1 (0226e947…): se escribe
   ANTES de correr la suite por primera vez, desde el inventario de la
   fase 1 (columna «sentido sobre r1» y evidencia de cierre), los retests
   C1–C7 y las tres sondas, con path:línea por valor. Mostrá el sha256
   de la fixture antes de la primera corrida y después de la última:
   deben coincidir. Si la suite mide distinto de lo esperado, es
   HALLAZGO y FRENO, no ajuste de la fixture.
   (f.2) LÍNEA DE BASE OBSERVADA, solo para KG-Base run_3 (12c226e2…) y
   KG-Reextraído salida (8e2eadee…): se registra DESPUÉS de correr, tal
   como dio, rotulada «línea de base observada» en cada valor, y no
   participa del cómputo de regresión en esta fase. La autora decide si
   se promueve a esperado al sellar la fixture.
g. Selftest scripts/selftest_regression_kg.py, solo stdlib, con fixtures
   sintéticos mínimos escritos en el propio selftest: por cada forma de
   test un caso que pasa y un contraejemplo; el adaptador sobre un nodo
   gen 2 y uno gen 3; la política de cuarentena en sus dos valores; y un
   caso de regresión contra una fixture sintética que devuelve código de
   salida distinto de 0.
h. Interfaz: python3 scripts/regression_kg.py --kg RUTA --generacion
   {2,3} --catalogo RUTA --politica-cuarentena {laudada,flaggeada}
   --esperado RUTA --out RUTA.md (escribe también RUTA.json). Sin --out
   no escribe nada. Sin --esperado, reporta estados y no computa
   regresión.

BATERÍA (corrida completa antes de frenar; todo --out al scratchpad, nunca
al repo):
1. Sobre r1 con generación 3, catálogo v2, política flaggeada: T1–T7 dan
   los mismos siete valores que salida_r1/tests_respuesta_conocida_r1.json
   (7/7 pass); C2 persiste (Bancos 2.500 / Restantes 5.000); C7 resuelto;
   T4 82 triplas; T5 30/30; T7 41/41. Estos valores están en la fase 1
   (sonda_T1_T7_cuatro_grafos_UB21_salida.txt y
   sonda_anclas_C1_C7_UB21_salida.txt).
2. Sobre KG-Refinado con generación 2, catálogo v2, política laudada: C1
   a C7 resueltos (son el grafo donde se verificaron); T1, T2, T3 e I5
   ya NO fallan por formato; T4 con esqueleto de referencia = él mismo;
   T7 en su lectura laudada.
3. Sobre KG-Base y KG-Reextraído: se reporta tal como dé, sin ajustar, y
   se registra como línea de base observada (pieza f.2).
4. r1 y KG-Refinado contra la parte f.1 de la fixture: 0 regresiones
   esperadas, porque la fixture se escribió de las mismas sondas y
   retests antes de correr. Cualquier regresión es HALLAZGO y FRENO:
   reportá ítem, grafo, esperado, medido y la evidencia de la fase 1 que
   sostenía el esperado.
5. Determinismo: doble corrida sobre r1 con .json byte-idéntico (cmp y
   sha256 pegados).
6. Selftest en verde con la cuenta de casos.
Cualquier diferencia en 1 o 2 respecto de lo documentado en la fase 1 es
FRENO, no ajuste del test ni de la fixture.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Escrituras permitidas: scripts/regression_kg.py,
  scripts/regression_kg_esperado.json y scripts/selftest_regression_kg.py
  (los tres nuevos) y tu scratchpad. Nada más: ni r1_tests.py, ni
  ensamblar_corpus.py, ni harness.py, ni el backlog, ni docs/, ni el
  plan, ni ningún kg.json. No commitees. Costo de API: 0.
- Toda corrida de Python con PYTHONDONTWRITEBYTECODE=1 (las sondas de la
  fase 1 dejaron .pyc bajo __pycache__/).
- Zonas selladas de CLAUDE.md §3 intactas; todo kg.json es solo lectura;
  el retriever in-memory se importa, no se copia ni se edita.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO.
- Paquete de revisión revision_UB21_fase2/ con manifest.txt (sha256 y una
  línea por archivo): los cuatro reportes .md con sus .json, la salida
  del selftest, la fixture, el diff completo de los tres archivos nuevos
  y el estado del árbol de trabajo (archivos modificados y nuevos, con el
  comando que uses y su salida pegada). Reporte al frenar de no más de 40
  líneas; lo largo va al paquete.
- Cero nombres propios; decisiones por justificación técnica.
- Si tu contexto se acerca al límite o vas a compactar, ANTES escribí en
  el scratchpad checkpoint_UB21_fase2.md con qué piezas (a–h) están
  hechas, qué tests faltan y qué puntos de la batería ya corriste, y
  reportá la ruta.

CRITERIO DE ACEPTACIÓN. 46 ítems en la suite, cada uno con forma,
direccionamiento y evidencia; batería 1–6 completa con salidas pegadas;
la fixture con evidencia por valor, su sha256 idéntico antes y después de las corridas, y la línea de base observada rotulada; 0 regresiones o el FRENO con su
hallazgo; doble corrida byte-idéntica demostrada; el estado del árbol con
solo los tres archivos nuevos de scripts/ (más lo preexistente,
enumerado); grep de convenciones sobre el paquete, pegado aunque dé vacío.

FRENO al terminar. La autora revisa el diff y sella la fixture antes de
que la suite entre al gate de B2.6.
