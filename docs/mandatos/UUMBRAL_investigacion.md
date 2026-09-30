BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA

MANDATO — U-UMBRAL: INVESTIGACIÓN DE LAS OPCIONES PARA MODELAR UMBRALES.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en DOS ETAPAS, con FRENO obligatorio al final de cada una: reporte corto
  (no más de 40 líneas) y espera de la revisión y del «seguí» escrito de la autora.
  Ninguna etapa arranca sin él.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- Corre en paralelo con U-LISTAS-NOMAP y U-INSUMOS-CAP, con directorios de
  escritura disjuntos: no leas ni escribas en reports/u_listas_nomap/ ni en
  reports/u_insumos_cap/.

CONTEXTO. Plan, fila B2.11, unidad 3 (docs/plan_tesis.md:391); checklist X14.
- La autora decide cómo se modelan los umbrales (porcentajes, plazos, montos,
  «veces»). Es una decisión de esquema.
- Tres opciones: (A) propiedad del nodo; (B) atributo de la relación; (C) paso
  posterior, en código, sobre el nodo ya extraído.
- La unidad mide y presenta evidencia; no decide. La decisión va a L-ESQ-R2
  (plan, B2.11, unidad 5).
- Rige el principio 12 del plan (:299): adaptar en código antes que reprocesar.

Leé completos, antes de escribir una línea:
- docs/tablero_correcciones.md: las filas «Cuantías sin campo estructurado» y
  «Afirmación falsa por tabla no detectada (`cap::1.2`, `BKL-0006`)», y los
  comandos [c10] y [c14];
- docs/esquema_v2_diseño.md:250, :323 y :392 (S18, `umbral` y `limita`);
- data/experiment/esq/laudo_ESQ-3a_retoques.md:18-27 y :204-211 (escalón 3,
  properties en relaciones, diferido);
- docs/plan_tesis.md:697 (el modelo de datos no admite hechos con valor);
- docs/laudo_release_r2_pipeline.md: la §1.3 (RX-10) y la fila de `cap::1.2` de
  la §4;
- las herramientas del agente:
  - data/experiment/evaluacion/harness.py:108-117 (resumen de `buscar_nodos`),
    :134-138 (tokens de búsqueda), :179-190 (`ver_nodo`) y :210-225
    (`ver_vecinos`);
  - data/experiment/neo4j/indices.py:6-14 (campos del índice full-text);
- el prefijo de E1 vigente: definiciones de Restriccion y Obligacion y reglas
  sobre tablas. Obtené el texto importando `perfil_e1.perfil('v3_b54')` y
  `prompt_v3_b54.PREFIJO_SISTEMA_V3`, sin editar nada;
- data/experiment/reextraccion_v2/e0_chunking/e0_tablas.py y las marcas `flags`
  de los chunks de E0.

Grafos. Verificá su sha256 al inicio y al cierre.
- KG-Tanda0-Desarrollo-r1, el grafo principal:
  data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json
  (eab2fdd0…).
- KG-Reextraído-r1: data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json
  (0226e947…).
- KG-Tanda0-Diez-r1: data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json
  (dd42d6d9…).
E0: data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_<to>.json,
de los diez TOs. Para los cinco de desarrollo es idéntico a salida_enm01
(reports/u_pre_r2/d1_suite.md:46).

DECISIONES YA TOMADAS. No se re-deciden.
1. La unidad investiga y propone; no decide. Toda propuesta se rotula como
   propuesta. La elección es de la autora.
2. EV2 y las trazas de C1 a C5 son material de desarrollo: se usan para
   diagnosticar. Nada de esta unidad se reporta como resultado sobre EV2
   (principio 7 del plan).
3. La regex de cuantía es la del comando [c14] del tablero, sin cambios. Si hace
   falta una variante, se declara aparte, con nombre propio, antes de aplicarla, y
   se reportan las dos.
4. Esta unidad no lee textos para juzgarlos; por ejemplo, no decide si el destino
   de una `limita` es el objeto del tope. Prepara la muestra y la planilla; quién
   lee lo decide la autora después (checklist P15 y Q12). Si una medición exige
   juicio sobre texto y no se puede evitar, se rotula «clasificación asistida» y
   queda para revisión de la autora.
5. No se modifica ningún archivo del pipeline, del grafo, de la suite ni de la
   evaluación. El prototipo del paso (C) es un script de la unidad, en su
   directorio.

U1 — Mediciones sobre los grafos y E0. USD 0.
a. Script nuevo reports/u_umbral/u_umbral_u1.py, de solo lectura.
b. **Medición 1, literalidad.**
   - Para cada nodo con `umbral` o `plazo` no vacío: si el valor aparece literal en
     la descripción del nodo y en el texto de E0 de su unidad (propio y heredado).
   - La normalización (espacios, mayúsculas, NFC) se declara antes de aplicarla.
   - Salida: conteos por tipo y por grafo, y la lista de los valores no literales.
c. **Medición 2, tablas no marcadas.**
   - Barrido de los chunks de E0 de los diez TOs que no están marcados como tabla
     (`flags.contenido_tabular` falso), con un patrón declarado de tabla
     linealizada (por ejemplo, líneas de encabezado seguidas de una línea solo de
     cifras).
   - Por cada chunk que dispare: si algún nodo de ese chunk tiene `umbral` o una
     cuantía en la descripción.
   - Contrastá el resultado con lo que detecta `e0_tablas.py` sobre esos mismos
     chunks, por import y sin editarlo.
   - Caso de control: el patrón tiene que dispararse en `cap::1.2`.
d. **Medición 3, cuantías sin campo.**
   - Con la regex de [c14]: nodos Restriccion, Condicion, Obligacion y Excepcion
     con cuantía en la descripción, con y sin `umbral` o `plazo`, por tipo y por
     grafo. Tiene que reproducir las cifras del tablero (en desarrollo, 287 sin
     campo de 606).
   - Descripciones con dos o más cuantías.
   - Cuantías que empiezan después del carácter 160 de la descripción, que el
     resumen de `buscar_nodos` no muestra.
e. **Medición 6, prototipo del paso (C).**
   - Extracción por regex de valores estructurados (tipo de cuantía, valor,
     unidad) desde la descripción.
   - Acuerdo contra `umbral` y `plazo` donde existen: coincide, difiere o el
     prototipo no extrae. La regla de coincidencia se declara antes.
   - Contá los casos que la regex no cubre: números en letras, varios valores,
     umbrales relacionales.
f. **Aristas `limita`, insumo de la opción (B).**
   - Cuántas hay y desde qué tipo de Restriccion salen; cuántas salen de una
     Restriccion con `umbral`.
   - Restricciones con `umbral` y sin `limita`.
   - Condiciones con cuantía y sin `condicion_de`.
   - Restricciones con más de una `limita`.
g. Salidas: reports/u_umbral/u1_mediciones.json y u1_mediciones.md, con doble
   corrida byte a byte idéntica.
FRENO U1: tabla por medición, con conteos y su comando; sha256 de lo escrito.

U2 — Muestra, trazas y evidencia por opción. USD 0.
a. Script nuevo reports/u_umbral/u_umbral_u2.py, de solo lectura.
b. **Medición 4, muestra de `limita`.**
   - Sorteo de 30 aristas `limita` de KG-Tanda0-Desarrollo-r1: semilla 20260930,
     sin reemplazo, sobre la lista ordenada por (source, target). El
     procedimiento se declara antes de sortear.
   - Planilla reports/u_umbral/muestra_limita_30.csv. Por arista:
     - ids y labels;
     - descripción y `umbral` de la Restriccion;
     - descripción de la Operacion;
     - chunk y texto de E0 de la unidad;
     - una columna vacía: «el destino es el objeto del tope (sí / no / no
       decidible)».
   - La planilla se sella con su sha256 en el reporte. Nadie la lee en esta
     unidad.
c. **Medición 5, trazas.**
   - Identificá los criterios con cuantía en
     data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json, con la
     regex de [c14], declarada.
   - En las celdas C3 y C4 (trazas base,
     data/experiment/ev2_tanda0/trazas/ev2_c3_dev_mem/ y ev2_c4_dev_neo4j/), por
     criterio:
     - qué nodos del grafo de desarrollo contienen el valor, en la descripción o
       en un campo;
     - si el agente los recibió en algún resultado de `buscar_nodos` o de
       `ver_vecinos`;
     - si les hizo `ver_nodo`.
   - Es un diagnóstico de dónde se pierde el valor (grafo, búsqueda, navegación o
     generación), no un resultado.
d. **Reporte** reports/u_umbral/reporte_u_umbral.md. Para cada opción, (A), (B) y
   (C):
   - qué dice la evidencia de U1 y U2 a favor y en contra, con conteos y
     comandos;
   - qué cambia en el pipeline: prompt de E1, tool schema, E2, herramientas del
     agente (algunas selladas), suite y shapes;
   - si obliga a re-extraer (principio 12);
   - cómo queda el caso `cap::1.2`.
   Al final, una PROPUESTA rotulada como tal, con su alternativa.
e. Salidas: u2_muestra_trazas.json y u2_muestra_trazas.md, muestra_limita_30.csv
   y reporte_u_umbral.md; doble corrida byte a byte idéntica de todo lo que genera
   un script.
FRENO U2, final: la tabla de opciones con la evidencia; sha256 de lo escrito.
Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo reports/u_umbral/ (se crea) y tu scratchpad.
  - No se editan el plan, el checklist, el tablero, el laudo, la fixture, la
    suite, el backlog ni nada bajo data/experiment/.
  - Nada sellado se toca (CLAUDE.md §3).
  - No commitees.
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio (conteo de .pyc) y
    control al cierre.
  - Si hiciera falta abrir una db de caché, solo con file:…?immutable=1.
- Afirmaciones y citas:
  - Toda afirmación lleva path:línea o comando.
  - Los conteos se recomputan antes de escribirse (§4 i).
  - Lo que no esté en un artefacto es NO ENCONTRADO.
  - La tesis no se cita por línea de docs/tesis/main.tex, que está
    desactualizado; la fuente es Overleaf, y se cita por sección y frase.
  - Los mentores solo por rol; cero nombres propios.
- Si algo de este mandato contradice un archivo del repo, mandan los archivos y se
  reporta la contradicción.
- Revisión y checkpoint:
  - Paquete de revisión revision_UUMBRAL_U<n>/ por etapa, con manifest.txt
    (sha256 y una línea por archivo) y nombres únicos.
  - Checkpoint checkpoint_UUMBRAL.md en el scratchpad, actualizado al cierre de
    cada etapa y antes de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro
  de los bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas;
- git status --short con solo reports/u_umbral/ como nuevo;
- sha256 de los tres grafos iguales al inicio y al cierre;
- doble corrida byte a byte idéntica;
- la medición 3 reproduce las cifras del tablero ([c14]);
- el patrón de la medición 2 dispara en `cap::1.2`;
- el grep de convenciones, pegado aunque dé vacío.
Criterio final: las seis mediciones con conteo y comando; la tabla de opciones con
evidencia; la propuesta rotulada.

FRENO al final de cada etapa.
