DESPACHADO 15/09/2026 (copia de la mesa; sin cambios respecto del texto aprobado)

MANDATO — U-B2.1 FASE 1: DIAGNÓSTICO PARA LA REGRESSION SUITE.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar. Solo lectura;
costo de API 0; ninguna escritura fuera de tu scratchpad.

CONTEXTO (dos líneas). La fila B2.1 del plan (docs/plan_tesis.md :313)
prevé scripts/regression_kg.py: convertir cada defecto cerrado del
backlog, los tests T1–T7 de r1 y las reglas declaradas de E4 en tests de
respuesta conocida determinísticos, ejecutables sobre cualquier kg.json.
Antes de escribir una línea hay que saber qué es convertible y qué
necesita cada conversión.

DECISIONES YA TOMADAS.
1. Fase 1 es SOLO diagnóstico. No se implementa nada; no se edita ningún
   archivo del repo.
2. Universo del inventario, tres grupos:
   (i) BKL cerrados: entradas de data/backlog/backlog.jsonl con estado
       aplicado o verificado (el archivo es un registro de eventos: una
       entrada puede tener varias líneas; reconstruí el estado efectivo
       por id y mostrá el comando), con sus retests en
       data/backlog/retests/ (C1 a C7) y sus propuestas selladas en
       data/backlog/propuestas/. La fila del plan nombra además
       BKL-0024/0025 y RT-*: localizalos; si alguno no existe con ese
       nombre, escribí NO ENCONTRADO con el comando que lo buscó.
   (ii) Tests T1–T7 de r1: data/experiment/reextraccion_v2/corpus_v2/
       r1_tests.py (T1–T3 delegan en ensamblar_corpus.tests_respuesta_conocida),
       más las invariantes I1–I5 de r1_invariantes.py.
   (iii) Reglas de E4: data/experiment/reextraccion_v2/corpus_v2/r1_e4.py
       (resolución de propuestos por label exacto, alias declarado, slug,
       singularización por token, sigla condicionada; TextoOrdenado
       canónico desde provenance; filtro de conflictos), leídas del código
       y de su docstring, con path:línea por regla.
3. Un «test de respuesta conocida sobre cualquier kg.json» es una
   comprobación determinística de una de estas formas: nodo presente,
   ancla (punto de provenance) presente, valor de propiedad, arista
   presente o ausente, o rank en buscar_nodos. La última depende de un
   retriever; anotá de cuál (in-memory o Neo4j) y qué config.

TAREA (una sola unidad): escribir en tu scratchpad inventario_B21_fase1.md
con estas piezas.
a. INVENTARIO, una fila por ítem de los tres grupos: id, qué afirma
   (una oración), sobre qué grafo se verificó (path y sha si está
   registrado), evidencia del cierre (path del retest o del test), y qué
   cambió en el pipeline o en el grafo para cerrarlo.
b. CONVERTIBILIDAD, por fila: convertible / convertible con condición /
   no convertible, con la forma de test de la decisión 3 y la razón. Para
   los convertibles con condición, qué necesitaría: cómo se direcciona el
   objeto cuando los ids de nodo cambian entre grafos (por tipo y label,
   por punto de provenance, por conjunto de provenances, nunca por
   provenance[0] solo), qué fixture haría falta, y si el test tiene
   sentido sobre un grafo que no pasó por r1.
c. SOLAPAMIENTOS: qué ítems ya están cubiertos por T1–T7, por las
   invariantes o por una shape del validador de shapes, con path, para
   que la suite no duplique.
d. TABLA RESUMEN con los conteos: ítems por grupo, convertibles,
   con condición, no convertibles, y cuántos dependen del retriever.
   Recomputá cada conteo contra la tabla de a antes de escribirlo.
e. LO QUE NO ESTÁ: entradas del backlog cuyo estado efectivo no es
   aplicado ni verificado (triaged, nuevo, sin estado), solo contadas y
   listadas por id; no entran al inventario.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j).
- Única escritura: tu scratchpad. No editás nada del repo. No commitees.
  Costo de API 0. Zonas selladas de CLAUDE.md §3 intactas; todo kg.json
  es solo lectura.
- Toda afirmación con path:línea o comando; conteos recomputados antes de
  escribirse (§4.i); lo que no esté en un artefacto es NO ENCONTRADO, no
  se infiere. Tu memoria de sesión no es fuente.
- Cero nombres propios de personas; decisiones por justificación técnica.
- Paquete de revisión revision_UB21_diag/ con manifest.txt (sha256 y una
  línea por archivo): el inventario, el script o comando con que
  reconstruiste el estado efectivo del backlog y su salida, y el estado
  del árbol de trabajo (archivos modificados y nuevos, con el comando que
  uses y su salida pegada; debe mostrar solo lo preexistente). Reporte al
  frenar de no más de 40 líneas; lo largo va al paquete.
- Si tu contexto se acerca al límite o vas a compactar, ANTES escribí en
  el scratchpad checkpoint_UB21.md con qué piezas (a–e) están hechas, qué
  grupo del inventario va por dónde y qué archivos leíste, y reportá la
  ruta.

CRITERIO DE ACEPTACIÓN. Pieza a con una fila por ítem de los tres grupos
y ninguna fila sin evidencia de cierre o sin la marca NO ENCONTRADO; la
suma de la pieza d cierra contra la pieza a; cada ítem de BKL-0024/0025 y
RT-* resuelto como encontrado o NO ENCONTRADO con comando; grep de
convenciones sobre el paquete pegado aunque dé vacío; ninguna línea de
código de la suite escrita.

FRENO al terminar el inventario. La fase 2 tiene mandato propio.
