BORRADOR — PENDIENTE DE FIRMA DE LA AUTORA

MANDATO — U-LISTAS-NOMAP: INVENTARIO DE LAS LISTAS CERRADAS Y DISEÑO DEL PROCESO PARA LO NO MAPEABLE.
Repo bcra-regulatory-kg. Leé CLAUDE.md antes de empezar.
- Unidad en DOS ETAPAS, con FRENO obligatorio al final de cada una: reporte corto
  (no más de 40 líneas) y espera de la revisión y del «seguí» escrito de la autora.
  Ninguna etapa arranca sin él.
- Costo de API: USD 0. Ninguna llamada a la API; Neo4j no se usa.
- Corre en paralelo con U-UMBRAL y U-INSUMOS-CAP, con directorios de escritura
  disjuntos: no leas ni escribas en reports/u_umbral/ ni en reports/u_insumos_cap/.

CONTEXTO. Plan, fila B2.11, unidad 4 (docs/plan_tesis.md:392); checklist X12 y
X13; absorbe X6, X7 y X9.
- Decisiones de la autora del 30/09:
  - (2) todas las listas cerradas se validan en código con Pydantic (U-PYD,
    unidad 7);
  - (3) lo que no se puede mapear se reprocesa por programa, con la información
    necesaria extraída; por ejemplo, la mención textual del sujeto.
- Esta unidad mide y diseña. Es insumo de L-ESQ-R2 (política por campo y campos
  nuevos del tool schema, unidad 5), de U-PYD y de U-PROMPT-R2. No implementa nada
  en el pipeline.

Leé completos, antes de escribir una línea:
- tool schema de E1:
  - data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py:270-333;
  - `TOOL_SCHEMA_V3` por import (data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py:411-414);
- validador de E1: data/experiment/reextraccion_v2/e1_extractor/validador_e1.py
  :89-123, :196-230 (normalización de Obligacion.tipo) y :281-360 (sujetos);
- E2: data/experiment/reextraccion_v2/e2_reduce/e2_lib.py:110-124 (slug),
  :340-352 (conflictos de properties) y :362-465 (nodos de sujeto, propuestos y
  aristas);
- E4: data/experiment/reextraccion_v2/corpus_v2/r1_e4.py:1-36, :73-117 (índice y
  reglas) y :121-202;
- esqueleto y aristas `padre_sugerido`: data/experiment/tanda0/code/ensamblar_tanda0.py
  :136-142 y :229-313;
- catálogos:
  - el bloque v3: prompt_v3_b54.py:97-114, :150-189 y :396-414;
  - los labels que se derivan del bloque: data/experiment/reextraccion_v2/e1_extractor/perfil_e1.py:101-131;
  - data/experiment/esq_v3_miembros/esquema_v3_clases.json;
- la regla 9 del prefijo (contenido meta-normativo) y la regla de omisiones
  (prompt_e1.py:158-165). El texto vigente de la regla 9 se obtiene importando
  `prompt_v3_b54.PREFIJO_SISTEMA_V3`;
- el canal abierto de tipos, probado y retirado: docs/plan_tesis.md:467-496 y
  :631-641;
- docs/tablero_correcciones.md: las filas «Valores fuera de lista cerrada»,
  «Mención del sujeto sin guardar; sujetos no mapeables», «Catálogo de sujetos en
  dos fuentes» y «Omisiones sin registro fuera de los chunks marcados», con los
  comandos [c11] a [c13] y [c15].

Entradas:
- crudo de E1 de la tanda 0, con el que se armaron los ensamblados:
  data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida/<to>/extracciones_e1_compact.jsonl,
  campo `tool_input_crudo`, de los diez TOs;
- crudo de E1 de r1: data/experiment/reextraccion_v2/corpus_v2/salida/<to>/extracciones_e1_compact.jsonl;
- crudo de los reintentos de E3: data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db,
  solo con file:…?immutable=1, como en reports/u_pre_r2/d2_ausencias.md:24;
- E0: data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_<to>.json;
- tablas de E4: `e4_propuestos.json` de cada ensamblado.

DECISIONES YA TOMADAS. No se re-deciden.
1. La unidad mide y diseña. No implementa en el pipeline ni decide la política:
   la política por campo y los campos nuevos los lauda la autora en L-ESQ-R2. Toda
   propuesta se rotula como propuesta.
2. Listas cerradas en alcance: tipos de entidad (9), predicados (13), catálogo de
   sujetos (102 ids del bloque v3), Obligacion.tipo (enum de 6), Restriccion.tipo,
   Comunicacion.tipo y las claves de properties por tipo, tal como las define el
   prefijo (comando [c11] del tablero). Operacion.tipo es texto libre: queda fuera
   como lista, pero se describe.
3. El inventario se hace sobre el crudo (`tool_input_crudo`), antes del validador,
   y se contrasta con lo validado y con el grafo. La brecha entre los tres es un
   dato.
4. Principio 12 del plan (:299): el diseño prioriza lo que se re-aplica en código
   sobre la salida guardada. Todo lo que obligue a cambiar el prompt de E1 se marca
   como tal.
5. «Posible forzado» (un `sujeto_id` cuyo label y alias no aparecen en el texto
   del chunk) es un indicador, no un veredicto. Esta unidad no lee textos para
   confirmarlo: prepara una muestra sellada para lectura posterior; quién lee lo
   decide la autora (checklist P15 y Q12).

N1 — Inventario y mediciones. USD 0.
a. Script nuevo reports/u_listas_nomap/u_listas_n1.py, de solo lectura.
b. **Inventario por lista cerrada**, en el crudo de los diez TOs de la tanda 0 y de
   los cinco de r1:
   - valores emitidos y sus conteos; valores fuera de lista;
   - claves de properties fuera de la definición de cada tipo;
   - cuántos rechazó el validador, cuántos normalizó (Obligacion.tipo → «otra»,
     con su contador) y cuántos dejó pasar;
   - cuántos llegan al grafo (tablero [c11]);
   - motivos de rechazo del validador por lista (`validacion.rechazos`).
c. **Sujetos.**
   - Relaciones `aplica_a` y `ejecuta` con `sujeto_id` y con `sujeto_propuesto`.
   - Propuestos con y sin padre sugerido; padres anulados por estar fuera de
     catálogo.
   - Posibles forzados, con la regla declarada antes: label o alias del bloque v3,
     normalizado, presente en el texto propio o heredado del chunk. Por id de
     catálogo, los más frecuentes.
   - Muestra sellada de 30 posibles forzados en
     reports/u_listas_nomap/muestra_forzados_30.csv: semilla 20260930 y
     procedimiento declarado antes; columnas vacías para la lectura.
d. **Re-resolución por programa, contrafáctica.**
   - Correr `r1_e4.resolver_label`, por import y sin editarlo, sobre los
     propuestos de los tres ensamblados de la tanda 0 (`e4_propuestos.json`).
   - Dos catálogos: (i) el JSON actual; (ii) el JSON más los seis ids del bloque
     que le faltan, con la misma construcción que R-CAT
     (reports/u_pre_r2/d1_suite.md:10).
   - Salida: cuántos resuelven con cada catálogo. Es un contrafáctico, no un
     resultado.
e. **Omisiones.** Chunks con `omisiones_no_prosa` no vacío, por marca de E0
   (tabla, fórmula, sin marca); chunks marcados sin ninguna omisión registrada.
f. **Catálogo.** Diferencia entre el bloque v3 y esquema_v3_clases.json (ids,
   labels, alias, nivel y padre), recomputada.
g. Salidas: reports/u_listas_nomap/n1_inventario.json y n1_inventario.md, y
   muestra_forzados_30.csv; doble corrida byte a byte idéntica.
FRENO N1: tabla por lista y por medición, con conteos y su comando; sha256 de lo
escrito.

N2 — Diseño. USD 0.
Documento reports/u_listas_nomap/diseno_listas_nomap.md, con cada propuesta
rotulada como tal:
a. **Política por campo** ante un valor fuera de lista: rechazar el elemento,
   normalizar con contador o registrar sin cambiar. Con la evidencia de N1 y la
   consecuencia de cada opción sobre el grafo y sobre la re-aplicación en código.
b. **Mención textual del sujeto**:
   - campo nuevo del tool schema (nombre y obligatoriedad);
   - verificación en el validador: subcadena normalizada del chunk, y qué pasa si
     falla;
   - relación con `sujeto_id` como sugerencia del modelo.
c. **Resolución en código (E4 generalizado)**: orden de las reglas, papel de la
   sugerencia del modelo y del padre, y registro del método y de los desacuerdos
   entre regla y modelo.
d. **Registro de no mapeados**, con el nombre de archivo que se proponga:
   - sus campos y en qué punto del pipeline se escribe;
   - cómo se re-resuelve por programa cuando crece el catálogo;
   - cómo se mide.
e. **Omisiones con categoría y tramo literal en todo chunk**:
   - categorías: meta-normativo, tabla, fórmula, fuera de tipos;
   - cómo se valida el tramo;
   - qué reproceso dirigido habilita.
f. Una tabla: qué de todo esto se re-aplica sin re-extraer y qué exige el prompt
   nuevo (U-PROMPT-R2).
g. Qué tests de la suite y qué shapes harían falta. Es una propuesta; no se
   escriben.
FRENO N2, final: resumen del diseño y la tabla del punto f; sha256 de lo escrito.
Commit de la autora.

REQUISITOS TRANSVERSALES (CLAUDE.md §4 a–j), en todas las etapas.
- Escrituras: solo reports/u_listas_nomap/ (se crea) y tu scratchpad.
  - No se editan el plan, el checklist, el tablero, el laudo, la fixture, la
    suite, el backlog ni nada bajo data/experiment/.
  - Nada sellado se toca (CLAUDE.md §3).
  - No commitees.
- Python:
  - PYTHONDONTWRITEBYTECODE=1 y .venv/bin/python -B en todo Python.
  - Ningún __pycache__ ni .pyc nuevo: línea de base al inicio (conteo de .pyc) y
    control al cierre.
  - Las dbs de caché, solo con file:…?immutable=1.
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
  - Paquete de revisión revision_ULISTAS_NOMAP_N<n>/ por etapa, con manifest.txt
    (sha256 y una línea por archivo) y nombres únicos.
  - Checkpoint checkpoint_ULISTAS_NOMAP.md en el scratchpad, actualizado al
    cierre de cada etapa y antes de cualquier compactación.
- Shell zsh: variables entre comillas o como arrays; ningún comentario con # dentro
  de los bloques de comandos para copiar.

CRITERIO DE ACEPTACIÓN por etapa:
- el reporte corto con las salidas pedidas;
- git status --short con solo reports/u_listas_nomap/ como nuevo;
- sha256 de los grafos y de los jsonl leídos, iguales al inicio y al cierre;
- doble corrida byte a byte idéntica;
- el inventario reproduce, sobre KG-Tanda0-Desarrollo-r1, las cifras del tablero:
  Restriccion.tipo 4, Comunicacion.tipo 6, claves fuera 9 ([c11]); 22 propuestos,
  3 resueltos y 19 en cuarentena ([c12]); 6 ids solo en el bloque y 5 solo en el
  JSON ([c13]);
- el grep de convenciones, pegado aunque dé vacío.
Criterio final: el inventario completo con conteo y comando; el diseño con las
siete partes, cada propuesta rotulada.

FRENO al final de cada etapa.
