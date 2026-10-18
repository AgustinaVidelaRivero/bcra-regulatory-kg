# FRENO T3 — tanda 1 de B6.1: el gate pasa con las decisiones del 18/10/2026; registro, Neo4j, lo contado y la preparación de T4 (USD 0, sin API, sin commit)

Rigen el pre-registro firmado (`docs/preregistro_tanda1.md`, firma en `95b18217`, con su nota del 17/10/2026 en `ca5b39fd`), el «seguí» de
T3 y lo que decidió la autora el 18/10/2026 sobre el FRENO parcial (va a la §29 del registro de decisiones). HEAD `0c927ebb`. Este FRENO
sigue al parcial, que quedó renombrado sin cambios (`t3/FRENO_T3_parcial.md`, sha256 `63abc417…`).

**Resultado:**
- **El gate, con las decisiones 1 a 3, pasa en los cuatro grafos** (sección 3, tabla V2): shapes con la E0 con las partes da PASA en los
  cuatro; la suite da 0 regresiones no declaradas que cuenten; la reproducibilidad y los selftests, de las tablas del parcial, en verde.
- **El registro y Neo4j** (sección 4): dos entradas nuevas en `grafos.py` y el registro de la vista. La carga, con el envoltorio del
  cargador que la autora indicó, da gate 5 OK en los dos grafos, la paridad 147/147
  en cada uno y 0 nodos con la marca de la cola en el sin cola.
- **Lo que se cuenta sin leer** (sección 5): las observaciones (10) y (11), las vigilancias (4), (5), (8) y (9), la cola, el catálogo al
  cierre y la columna «Tanda 1» del tablero. De L-02 y de L-04, solo si sus pozos llegan a 30: llegan los dos.
- **La preparación de T4** (sección 6): las poblaciones por celda, los pesos reales, los umbrales, seis sorteos, el material
  (154 fichas) y `unidades_a_la_vista_T4.json`. No leí ninguna muestra ni marqué nada.
- Toda cifra sale por script de sus archivos. Las tablas que copio de una salida van tal cual; mis aclaraciones van fuera de las tablas.
- Nada commiteado y ningún mensaje de commit preparado: los commits son de la autora y quedan PENDIENTES.

## 1. Paso 0 (18/10/2026, 09:09:43)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git log -1 --format='%h %s'
0c927ebb Mandato firmado: las filas de alcance de la tanda final en el mensaje del extractor, con su nota al laudo y a la enmienda
$ git status --porcelain --untracked-files=no
 M scripts/regression_kg_esperado.json
$ shasum -a 256 scripts/regression_kg_esperado.json
574169f961c9cdd1925b25ccf1feacd56068a117e38cad98c9b5ffd3db194bc7  scripts/regression_kg_esperado.json
$ shasum -a 256 <los cuatro kg.json>
22e83a62cb88e5bbe31b64a0f2322194bc2ffd2622ea7adc2c07310d8a02c7c7  data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b/r2/kg.json
384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e  data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola/r2/kg.json
e63536d15bd8f575f1b7680921e3ca0d4956bdc5e38dc3f2fea27bb67bd71769  data/experiment/tanda1/t3/acumulado/ens_treinta_r2b/r2/kg.json
0435d41f9c7b45ea10cc87e8121fcfb8b3d2b089af837fff377a3460ced9636c  data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola/r2/kg.json
$ pgrep -fl "runner_corpus.py|ensamblar_tanda0.py|regression_kg.py|shapes_validator.py"
(rc=1)
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py . <scratchpad>/t3f/foto_repo_antes_T3f_cruda.json
2026-10-18 09:09:57 2026-10-18 09:10:09 52306 entradas
$ python3 -B data/experiment/tanda1/t2/foto_repo_tanda1_t2.py --comparar <foto de después del parcial> <esta foto>
antes 52304 despues 52306 nuevos ['data/experiment/escalado_prep/.DS_Store', 'data/experiment/tanda1/t3/FRENO_T3.md'] borrados [] cambiados []
$ stat (sin abrir) data/experiment/escalado_prep/.DS_Store
2026-10-18 09:01:34  6148 bytes; ignorado por .gitignore:25
```

- `pgrep` salió vacío. Los `.pyc`: 11.236 líneas, iguales a las del cierre del parcial.
- **El `.DS_Store` de `escalado_prep/`** no es de esta unidad: lo creó el Finder a las 09:01:34, al abrir la autora esa carpeta. Lo pregunté
  antes de escribir nada; la autora indicó seguir y declararlo, sin abrirlo, y no frenar por otro `.DS_Store` bajo `escalado_prep/`.

## 2. Lo decidido el 18/10/2026 y cómo lo apliqué

1. **S31 con la E0 con las partes por corte.** Es la que rige para el gate; la del repo se informa al lado (tabla V2). Es una precisión del
   gate tomada con el resultado a la vista, y vale igual para la tanda final. La rearmé fuera del repo (sección 3) y su sha256 va en la
   tabla V0.
2. **E4-a1 y E4-a4, declaradas como regresiones de la tanda 1.** No frenaron el resto de T3. No toqué el backlog: la entrada la escribe la
   mesa.
3. **La suite se juzga sobre el acumulado.** En la tanda 1 sola, la clase «fuera del grafo» la da `scripts/fuera_del_grafo_t3f.py`:
   - las anclas de cada ítem salen de su definición en `scripts/regression_kg.py`: el cierre de llamadas de su función en `TESTS`,
     recorrido por AST (las constantes de TO, las cadenas `<to>::<punto>` y los ids de TO del inventario), las `anclas` de
     `DEF_IDS_NUEVOS` en los ítems ID y, en T5, las anclas de `MUESTRA30`, que su código lee. El `direccionamiento` del registro hace de
     control: todo TO que nombra lo da también el código;
   - la fixture no trae anclas estructuradas: sus `nota` son texto libre y no se usaron;
   - 30 de los 68 ítems tienen anclas; los otros 38 son generales y valen en todo grafo;
   - no quedó ningún ítem sin anclas sacadas por script;
   - el cruce con `clasificar_regresiones_t3.py` da los mismos 15 ítems en los dos grafos de la tanda 1.
4. **Los `nombres_remision` de la tanda 0 en el acumulado** son los de la regla v2 (`222a0614`), como confirmó la mesa en el grafo.
5. **Las cuatro entradas nuevas de la fixture** quedan, para el commit de T3; las selladas no cambiaron.
6. **Las salidas de shapes y de la suite de los dos grafos de la tanda 1** quedan donde están, como en el re-sellado (sección 7).
7. **El clon de git del parcial** (su error propio 1) queda declarado (sección 7).
8. **Siguen las decisiones A y B:** las cuentas de E3 en cegamiento y toda cifra por script.
9. **`unidades_a_la_vista_T4.json`** registra, por muestra, toda unidad cuya extracción aparece en el material, en cualquier versión, y
   cuál (sección 6).

## 3. La E0 con las partes y el gate (punto 4)

**La E0 con las partes** (`scripts/e0_partes_t3f.py`, sobre una copia nueva del repo):
- La entrada del acumulado no está en el repo. La rearmé en la copia con `armar_acumulado_t3.py`, y lo rearmado es lo del repo:
  557 archivos y 297.695.212 bytes.
- `reext_t0/t3/e0_con_partes.py`, sin cambios, corrió dos veces por E0, cada vez en un proceso aparte. Las dos corridas dan los mismos
  bytes, iguales a las de ayer (tabla V0). El sha256 de cada archivo está en `gate_decisiones/e0_con_partes_t3f.json`.
- **El control de shapes.**
  - El intento 1 frenó: el `.md` y el `.json` difieren de los del parcial en las rutas y en la línea de la fecha de corrida.
  - Lo pregunté. La autora indicó normalizar solo la línea «Fecha:» del `.md` y el campo `"fecha"` del `.json`, además de las rutas, poner el
    diff crudo en el FRENO y frenar ante cualquier otra diferencia.
  - El intento 2, sobre una copia nueva, da el control OK en los cuatro grafos (tabla V1).
  - El intento 1 está en `gate_decisiones/intento1_control_e0/`.

**El diff crudo de los cuatro grafos, antes de normalizar** (`gate_decisiones/shapes_con_partes/<grafo>/diff_crudo_*.txt`; el scratchpad
escrito `<SCRATCHPAD>`; la consola da 0 líneas en los cuatro):

```
--- parcial/ens_veinte_r2b/shapes_perfil_r2_fase_r2b.md
+++ hoy/ens_veinte_r2b/shapes_perfil_r2_fase_r2b.md
@@ -5 +5 @@
-- **Fecha:** 2026-10-17
+- **Fecha:** 2026-10-18
@@ -9,3 +9,3 @@
-- **Vocabulario:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
-- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
-- **Lista de S15:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
+- **Vocabulario:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
+- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
+- **Lista de S15:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
@@ -13 +13 @@
-- **E0 (S31):** `<SCRATCHPAD>/t3/e0_tanda1_r2b_con_partes`
+- **E0 (S31):** `<SCRATCHPAD>/t3f/e0p/e0_con_partes/tanda1_corrida1`
--- parcial/ens_veinte_r2b/shapes_perfil_r2_fase_r2b.json
+++ hoy/ens_veinte_r2b/shapes_perfil_r2_fase_r2b.json
@@ -6 +6 @@
-  "fecha": "2026-10-17",
+  "fecha": "2026-10-18",
@@ -10 +10 @@
-    "modulo": "<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json",
+    "modulo": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json",
@@ -20 +20 @@
-    "ruta": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
+    "ruta": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
@@ -24 +24 @@
-  "excepciones_s15": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
+  "excepciones_s15": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
@@ -26 +26 @@
-  "e0": "<SCRATCHPAD>/t3/e0_tanda1_r2b_con_partes",
+  "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/tanda1_corrida1",
@@ -269 +269 @@
-        "e0": "<SCRATCHPAD>/t3/e0_tanda1_r2b_con_partes"
+        "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/tanda1_corrida1"
--- parcial/ens_veinte_r2b_sincola/shapes_perfil_r2_fase_r2b.md
+++ hoy/ens_veinte_r2b_sincola/shapes_perfil_r2_fase_r2b.md
@@ -5 +5 @@
-- **Fecha:** 2026-10-17
+- **Fecha:** 2026-10-18
@@ -9,3 +9,3 @@
-- **Vocabulario:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
-- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
-- **Lista de S15:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
+- **Vocabulario:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
+- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
+- **Lista de S15:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
@@ -13 +13 @@
-- **E0 (S31):** `<SCRATCHPAD>/t3/e0_tanda1_r2b_con_partes`
+- **E0 (S31):** `<SCRATCHPAD>/t3f/e0p/e0_con_partes/tanda1_corrida1`
--- parcial/ens_veinte_r2b_sincola/shapes_perfil_r2_fase_r2b.json
+++ hoy/ens_veinte_r2b_sincola/shapes_perfil_r2_fase_r2b.json
@@ -6 +6 @@
-  "fecha": "2026-10-17",
+  "fecha": "2026-10-18",
@@ -10 +10 @@
-    "modulo": "<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json",
+    "modulo": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json",
@@ -20 +20 @@
-    "ruta": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
+    "ruta": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
@@ -24 +24 @@
-  "excepciones_s15": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
+  "excepciones_s15": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
@@ -26 +26 @@
-  "e0": "<SCRATCHPAD>/t3/e0_tanda1_r2b_con_partes",
+  "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/tanda1_corrida1",
@@ -269 +269 @@
-        "e0": "<SCRATCHPAD>/t3/e0_tanda1_r2b_con_partes"
+        "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/tanda1_corrida1"
--- parcial/ens_treinta_r2b/shapes_perfil_r2_fase_r2b.md
+++ hoy/ens_treinta_r2b/shapes_perfil_r2_fase_r2b.md
@@ -5 +5 @@
-- **Fecha:** 2026-10-17
+- **Fecha:** 2026-10-18
@@ -9,3 +9,3 @@
-- **Vocabulario:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
-- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
-- **Lista de S15:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
+- **Vocabulario:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
+- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
+- **Lista de S15:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
@@ -13 +13 @@
-- **E0 (S31):** `<SCRATCHPAD>/t3/e0_acumulado_r2b_con_partes`
+- **E0 (S31):** `<SCRATCHPAD>/t3f/e0p/e0_con_partes/acumulado_corrida1`
--- parcial/ens_treinta_r2b/shapes_perfil_r2_fase_r2b.json
+++ hoy/ens_treinta_r2b/shapes_perfil_r2_fase_r2b.json
@@ -6 +6 @@
-  "fecha": "2026-10-17",
+  "fecha": "2026-10-18",
@@ -10 +10 @@
-    "modulo": "<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json",
+    "modulo": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json",
@@ -20 +20 @@
-    "ruta": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
+    "ruta": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
@@ -24 +24 @@
-  "excepciones_s15": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
+  "excepciones_s15": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
@@ -26 +26 @@
-  "e0": "<SCRATCHPAD>/t3/e0_acumulado_r2b_con_partes",
+  "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/acumulado_corrida1",
@@ -283 +283 @@
-        "e0": "<SCRATCHPAD>/t3/e0_acumulado_r2b_con_partes"
+        "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/acumulado_corrida1"
--- parcial/ens_treinta_r2b_sincola/shapes_perfil_r2_fase_r2b.md
+++ hoy/ens_treinta_r2b_sincola/shapes_perfil_r2_fase_r2b.md
@@ -5 +5 @@
-- **Fecha:** 2026-10-17
+- **Fecha:** 2026-10-18
@@ -9,3 +9,3 @@
-- **Vocabulario:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
-- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
-- **Lista de S15:** `<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
+- **Vocabulario:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json` (sha256 `abd197ac8bbb818f680dc80d1b9c9df3e1f1f733fce3fd46b35e7440e7ce4241`); marcas de nodo de `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/code/modelos_r2.py`: ['cola_humana', 'cola_chunks', 'estado_e3', 'colision_cross_to']
+- **Catálogo único (S19, S29):** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json` — 110 ids
+- **Lista de S15:** `<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json`
@@ -13 +13 @@
-- **E0 (S31):** `<SCRATCHPAD>/t3/e0_acumulado_r2b_con_partes`
+- **E0 (S31):** `<SCRATCHPAD>/t3f/e0p/e0_con_partes/acumulado_corrida1`
--- parcial/ens_treinta_r2b_sincola/shapes_perfil_r2_fase_r2b.json
+++ hoy/ens_treinta_r2b_sincola/shapes_perfil_r2_fase_r2b.json
@@ -6 +6 @@
-  "fecha": "2026-10-17",
+  "fecha": "2026-10-18",
@@ -10 +10 @@
-    "modulo": "<SCRATCHPAD>/t3/copia_t3/data/experiment/pyd_r2/generados/enums_r2.json",
+    "modulo": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/pyd_r2/generados/enums_r2.json",
@@ -20 +20 @@
-    "ruta": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
+    "ruta": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/ids_s19_r2.json",
@@ -24 +24 @@
-  "excepciones_s15": "<SCRATCHPAD>/t3/copia_t3/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
+  "excepciones_s15": "<SCRATCHPAD>/t3f/copia_t3f/data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json",
@@ -26 +26 @@
-  "e0": "<SCRATCHPAD>/t3/e0_acumulado_r2b_con_partes",
+  "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/acumulado_corrida1",
@@ -283 +283 @@
-        "e0": "<SCRATCHPAD>/t3/e0_acumulado_r2b_con_partes"
+        "e0": "<SCRATCHPAD>/t3f/e0p/e0_con_partes/acumulado_corrida1"
```

Normalizadas las rutas y esa línea, en los cuatro no queda ninguna diferencia (`distintas_despues_de_normalizar` vacío en
`e0_con_partes_t3f.json`).

**La tabla del veredicto** (`scripts/veredicto_gate_t3f.py` → `gate_decisiones/veredicto_gate_t3f.md`, tal cual):

#### Tabla V0. La E0 con las partes (`gate_decisiones/e0_con_partes_t3f.json`)

| E0 | archivos | dos corridas iguales | sha256 del conjunto |
|---|---:|---|---|
| tanda1 | 107 | True | `f079c1ff1b680eb7c766e8bebf05da489f474dd39e68ad228266296e8bd52028` |
| acumulado | 150 | True | `a9ff9b7b6e6228ca1db6dbcfebd63894e7d57e3c95d0652b7c47a4d981667c05` |

El acumulado rearmado en la copia, igual al del repo: True; su entrada, 557 archivos y 297695212 bytes.

#### Tabla V1. El control de shapes con esa E0, contra el FRENO parcial (`gate_decisiones/e0_con_partes_t3f.json`, `shapes`)

| grafo | archivo | byte a byte | líneas del diff crudo | igual con rutas y fecha normalizadas | control |
|---|---|---|---:|---|---|
| ens_veinte_r2b | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_veinte_r2b | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_veinte_r2b | consola_shapes.txt | True | 0 | True | True |
| ens_veinte_r2b_sincola | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_veinte_r2b_sincola | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_veinte_r2b_sincola | consola_shapes.txt | True | 0 | True | True |
| ens_treinta_r2b | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_treinta_r2b | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_treinta_r2b | consola_shapes.txt | True | 0 | True | True |
| ens_treinta_r2b_sincola | shapes_perfil_r2_fase_r2b.md | False | 10 | True | True |
| ens_treinta_r2b_sincola | shapes_perfil_r2_fase_r2b.json | False | 12 | True | True |
| ens_treinta_r2b_sincola | consola_shapes.txt | True | 0 | True | True |

#### Tabla V2. El veredicto del gate por grafo

| grafo | shapes, E0 con las partes (rige) | shapes, E0 del repo (informada) | suite: resuelto / persiste / no aplica | regresiones | declaradas (laudo) | declaradas (autora) | fuera del grafo | no declaradas que cuentan |
|---|---|---|---|---:|---:|---:|---:|---|
| veinte | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 31 / 16 / 21 | 20 | 3 | 2 | 18 | 0 |
| veinte_sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 31 / 16 / 21 | 20 | 3 | 2 | 18 | 0 |
| acumulado | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |
| acumulado_sincola | PASA (22 / 2 / 4) | NO PASA (21 / 3 / 4; bloqueantes en FAIL: S31) | 46 / 13 / 9 | 5 | 3 | 2 | — (no se aplica) | 0 |

Las columnas de shapes dan PASS / FAIL / WARN. «Fuera del grafo» cuenta las regresiones con todas sus anclas en TOs que el grafo no tiene; en el acumulado no se aplica (decisión 3). Las declaradas del laudo, en la tanda 1 sola, también caen fuera del grafo.

- **veinte, «fuera del grafo»:** 18 regresiones (BKL-0001, BKL-0002, BKL-0005, BKL-0006, BKL-0023, EJ-cla-5.1.1.1, ID-alta_gerencia, ID-comite_de_auditoria, ID-directorio, RT-C5-3, RT-C6-1, RT-C6-2, RT-C7-1, RT-C7-2, RT-C7-3, T1, T2, T3); de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con `clasificar_regresiones_t3.py`: 15 y 15 ítems, iguales: True.

- **veinte_sincola, «fuera del grafo»:** 18 regresiones (BKL-0001, BKL-0002, BKL-0005, BKL-0006, BKL-0023, EJ-cla-5.1.1.1, ID-alta_gerencia, ID-comite_de_auditoria, ID-directorio, RT-C5-3, RT-C6-1, RT-C6-2, RT-C7-1, RT-C7-2, RT-C7-3, T1, T2, T3); de los 68 ítems, 30 fuera del grafo, 38 generales y 0 en el grafo. Cruce con `clasificar_regresiones_t3.py`: 15 y 15 ítems, iguales: True.

#### Tabla V3. Reproducibilidad, selftests, intrínsecas y contadores (de las tablas 2, 6, 7 y 8 del FRENO parcial)

- **Reproducibilidad:** 6 cadenas, todas iguales: True; veredicto OK.
- **Selftests:** catalogo_unico rc=1, catalogo_unico_en_clon_git rc=0, clave_cache rc=0, e0 rc=0, ensamblado_omisiones rc=0, metrica_condiciones rc=0, pyd_r2 rc=0, r3 rc=0, regression_kg_1 rc=0, regression_kg_2 rc=0, shapes_congelado rc=0; el de claves, OK. El del catálogo pide git: rc=1 en la copia y rc=0 en el clon de git del parcial (error propio 1, declarado por la decisión 7).
- **Intrínsecas de generación 3, con la E0 con las partes (informativas):**
  - KG-Tanda1-Veinte-r2b: M4 4.945095, M9 16 nodos aislados, M10 0 / 3294.
  - KG-Tanda1-Veinte-r2b-sincola: M4 4.548667, M9 16 nodos aislados, M10 42 / 3294.
  - KG-Acumulado-Tandas0y1-r2b: M4 5.626325, M9 23 nodos aislados, M10 0 / 5734.
  - KG-Acumulado-Tandas0y1-r2b-sincola: M4 5.314453, M9 23 nodos aislados, M10 111 / 5734.
- **Contadores de E1 (informativos):** {'tipo_obligacion_requisito_de_estructura': 0, 'tipo_obligacion_normalizados': 1}.

**Veredicto del gate, con las decisiones 1 a 3: PASA.**

## 4. El registro y Neo4j (punto 5)

- **`grafos.py`:** `scripts/editar_grafos_t3f.py` agregó, en la copia, solo dos entradas al final de `GRAFOS`:
  - las claves `KG_Tanda1_Veinte_r2b` y `KG_Tanda1_Veinte_r2b_sincola`, con label, índice y `ev2_key` propios y `commit_sellado` «PENDIENTE»;
  - el sha256, `n_nodos` y `n_aristas`, de `salidas/doble_corrida_t3.json`.
  Las 13 selladas son iguales a las de HEAD (corrida en seco). En el repo, `grafos.py` cambia solo por
  esas dos entradas.
- **El registro de la vista:** `t3/registro_vista_r2b_tanda1.py`, con el patrón de `resellado_t0/registro_vista_r2b_rs1.py`.
  - La cola humana de la tanda 1: 42 unidades (`neo4j/consola_editar_grafos_t3f.txt`).
  - El desglose de «punto sin nodos» del sin cola: 169 en total,
    0 con destino en una unidad excluida y 169 netas. El completo
    da 173.
- **La corrida en seco** (`scripts/dry_registro_t3f.py`, por el camino de imports del cargador) da OK:
  los sha256, la vista con 12.731 / 31.478
  y 12.452 / 28.320,
  igual al registro, y el desglose igual a lo declarado.
- **El cargador.** `cargar_neo4j_tanda0.py` acepta en `--grafo` solo las claves `KG_Tanda0_*`. Frené y lo pregunté. La autora indicó
  el envoltorio en memoria, con condiciones:
  - `scripts/cargar_neo4j_t3f.py` importa el cargador sin editarlo, deja en memoria `CLAVES_TANDA0` con exactamente las dos claves de la
    tanda 1 y llama a su `main()` una vez por clave, con `--grafo <clave>`, nunca con «todos»;
  - el sha256 del cargador es `e51a3a148e8d9f65…` antes de la carga y `e51a3a148e8d9f65…` después, igual a HEAD
    (`neo4j/sha_cargador_antes.txt` y `_despues.txt`);
  - las salidas heredan los rótulos de la tanda 0: `carga_neo4j_tanda0.json`, «U-TANDA0-2A E3.c» y «PARIDAD (tanda 0)». No se corrigen.
- **Docker:**
  - Docker Desktop tenía el backend corriendo y el motor respondía 500, también después de abrirlo y esperar 5 minutos. Lo reinicié
    (`docker desktop restart`) y levanté el contenedor del repo (`docker compose up -d --wait`) (`neo4j/consolas/consola_docker_arranque.txt`).
  - Al reiniciarse, Docker levantó por su cuenta contenedores de otros proyectos de la máquina. No los toqué.
  - Al terminar detuve el contenedor del repo y pedí el cierre de Docker. El backend siguió corriendo y el motor volvió a responder 500,
    como estaba a la mañana (`neo4j/consolas/consola_docker_cierre.txt` y `consola_docker_estado_final.txt`).
- **La carga** (`neo4j/<clave>/carga_neo4j_tanda0.json`), desde la copia:
  - KG_Tanda1_Veinte_r2b: sha256 verificado antes de cargar; vista 12.731 / 31.478; dos cargas con la misma huella: True; `verificar_carga`: True; `KG_Meta.kg_sha256` igual al archivo: True, `commit_sellado` «PENDIENTE»; paridad 147/147; **gate 5: OK**.
  - KG_Tanda1_Veinte_r2b_sincola: sha256 verificado antes de cargar; vista 12.452 / 28.320; dos cargas con la misma huella: True; `verificar_carga`: True; `KG_Meta.kg_sha256` igual al archivo: True, `commit_sellado` «PENDIENTE»; paridad 147/147; **gate 5: OK**.
- **El control de la cola** (`scripts/control_cola_neo4j_t3f.py`, copia de `control_cola_neo4j_rs1.py` con las claves cambiadas):
  OK. En el sin cola, 0 nodos con
  la marca en Neo4j y 0 en el `kg.json`. En el completo, llegan las
  313 marcas del `kg.json`.

## 5. Lo que se cuenta sin leer (punto 6)

`scripts/contado_sin_leer_t3f.py`, sobre la copia, importa sin editarlas las funciones de la tanda 0 y del re-sellado:
- `resellado_t0/condicion_4/medicion_tablero_r2b_rs1_mesa.py`, con sus rutas apuntadas en memoria a la E0 y a la salida de cada grafo;
- `medir` de `udiag_e_aisladas.py`, tomada del árbol sintáctico como en el re-sellado;
- `medir_umbral` de `reresolucion_catalogo/r2_1_medicion.py`;
- y, para L-02, `omisiones_cod/o1/scripts/medir_e.py`, con su manifiesto y su entrada apuntados a la tanda 1.

Las reglas de las vigilancias son las de `vigilancias_contables_rs1_mesa.py`, con los TOs de cada grafo. **El control:** las mismas
funciones sobre el diez re-sellado reproducen su medición en las 11 filas controladas.

**El cegamiento** (punto 8): estas cuentas van solo a `t3/NO_ABRIR_conteos_t3.json`, sin abrirlo:
- la fila del crudo del reintento de E3;
- las claves de `properties_no_definidas`, que cuentan `copia_nota_e3` y la marca de L-04;
- los pozos de L-02 y de L-04.
Su sha256 está en la sección 9. La consola imprime solo los nombres de los archivos, el control y si los pozos llegan a 30.

#### Tabla C1. Observaciones (10) y (11) contra sus líneas de base re-selladas (pre-registro, §5.2)

| grafo | unidades de E0 | (10) aristas de extracción | (10) por unidad | (11) `remite_a` entre documentos | menciones |
|---|---:|---:|---:|---:|---:|
| veinte | 3.290 | 18.887 | 5,74 | 1.541 | 1.272 |
| veinte sin cola | 3.290 | 18.483 | 5,62 | 299 | 1.224 |
| acumulado | 5.729 | 32.138 | 5,61 | 3.628 | 2.783 |
| acumulado sin cola | 5.729 | 31.348 | 5,47 | 2.061 | 2.698 |
| base re-sellada: diez | 2.439 | 13.251 | 5,43 | 642 | 1.510 |
| base re-sellada: desarrollo | 1.768 | 10.304 | 5,83 | 497 | 1.289 |

#### Tabla C2. Vigilancias (4), (5), (8) y (9) contra sus líneas de base re-selladas (§5.3)

| grafo | (4) un TextoOrdenado por TO | (5) requisito_de_estructura / normalizados | (8) sujeto_propuesto / sujeto_id (tasa %) | (9) emisiones en E1 / aristas en el kg |
|---|---|---|---|---|
| veinte | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| veinte sin cola | True | 0 / 1 | 434 / 3.950 (9,90) | 7 / 20 |
| acumulado | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| acumulado sin cola | True | 0 / 1 | 626 / 6.300 (9,04) | 7 / 27 |
| base re-sellada: diez | True | 0 / 0 (los diez TOs) | 192 / 2.350 (7,55) | 0 (los diez TOs) / 8 |
| base re-sellada: desarrollo | True | 0 / 0 (los diez TOs) | 138 / 1.641 (7,76) | 0 (los diez TOs) / 8 |

#### Tabla C3. La cola (§5.4 b), contra los 69 de 2.439 del re-sellado

| grafo | cola | de unidades de E0 | % | por estado | aceptadas (los tres estados juntos) | en el grafo |
|---|---:|---:|---:|---|---:|---|
| veinte | 42 | 3.290 | 1,3 | cola_humana 18, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 22 | 3.252 | 313 nodos y 408 aristas con la marca |
| veinte sin cola | 42 | 3.290 | 1,3 | cola_humana 18, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 22 | 3.252 | 42 descartadas por el ensamblado |
| acumulado | 111 | 5.729 | 1,9 | cola_humana 43, cola_humana_reextraccion_invalida 4, cola_humana_veredicto_inutilizable 64 | 5.623 | 627 nodos y 793 aristas con la marca |
| acumulado sin cola | 111 | 5.729 | 1,9 | cola_humana 43, cola_humana_reextraccion_invalida 4, cola_humana_veredicto_inutilizable 64 | 5.623 | 111 descartadas por el ensamblado |
| base re-sellada (diez) | 69 | 2.439 | 2,8 | cola_humana 25, cola_humana_reextraccion_invalida 2, cola_humana_veredicto_inutilizable 42 | — | — |

El umbral de atención es 6 % (§5.4 b). Las unidades en `finales.jsonl` son veinte 3.294, veinte sin cola 3.294, acumulado 5.734, acumulado sin cola 5.734 (las partes por corte cuentan aparte); otros estados: veinte ninguno, veinte sin cola ninguno, acumulado ninguno, acumulado sin cola ninguno.

La cola por TO (veinte): cajasc 3, cirmo3 2, depaho 6, efemin 3, lingeef 10, manori 4, ri_ccna 6, ri_dcpc 1, ri_pgn 1, ri_rml 3, snp_cheq 1, snp_tr 2.

#### Tabla C4. El catálogo al cierre (§5.5): claves con la mención verificada en cuarentena en 2 unidades o más

| registro | filas en cuarentena | verificadas | claves | claves con 2 unidades o más | en 2 TOs o más |
|---|---:|---:|---:|---:|---:|
| veinte | 703 | 570 | 237 | 38 | 8 |
| veinte sin cola | 693 | 561 | 233 | 37 | 8 |
| acumulado | 851 | 713 | 320 | 56 | 13 |
| acumulado sin cola | 839 | 702 | 315 | 54 | 12 |
| base de la tanda 0: diez (r2_1_medicion.json) | 164 | 145 | 87 | 14 | 1 |
| base de la tanda 0: diez_sincola (r2_1_medicion.json) | 162 | 143 | 85 | 14 | 1 |

Las claves y sus formas están en `contado_sin_leer_t3f.json` (`catalogo_al_cierre`). Su lectura y aprobación es de la autora (enmienda 4, §1, punto 3); cuántas relaciones resuelve cada versión del catálogo se mide después de la re-resolución (punto 5).

#### Tabla C5. Los pozos de L-02 y L-04 (§5.4 d; cegamiento, punto 8: solo si llegan a 30)

- L-02 (detecciones de la tanda 1 (veinte, con la cola)): llega a 30: True.
- L-04 (nodos Comunicacion con `tipo_no_derivable`): veinte llega a 30: True; veinte sin cola llega a 30: True.
- Las cuentas, en `NO_ABRIR_conteos_t3.json`.

Control de las funciones importadas (las del re-sellado sobre KG-Tanda0-Diez-r2b-rs1 contra su medición): True en las 11 filas controladas.

**La columna «Tanda 1» del tablero** (26 filas, `:49` a `:74`): `conteos_sin_leer/columna_tanda1_tablero_t3f.md`, por
`scripts/tablas_contado_t3f.py`. Cada fila tiene su cifra o la causa por la que no se midió:
- 4 filas (56, 57, 58, 60) necesitan el agente (EV2), que nunca se corre;
- la (12) es una lectura de T4;
- la de las líneas en mayúsculas lee la E0 legada, que la tanda 1 no tiene;
- la del crudo del reintento está bajo cegamiento.
El tablero del repo no se tocó.

## 6. La preparación de T4 (punto 7)

Scripts: `poblaciones_t4_t3f.py`, `celdas_t4_t3f.py` (las cuotas y la regla de las celdas y de las clases chicas), `umbrales_t4_t3f.py`,
`sorteos_t4_t3f.py`, `material_t4_t3f.py`, `unidades_a_la_vista_t3f.py` y `tablas_t4_t3f.py`, que genera las tablas. Las tablas, tal cual:

#### Tabla T1. La población de cada muestra, por celda (`muestras/poblaciones_t4.json`, 2026-10-18T10:06:19-03:00)

| muestra | elemento | N | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | se lee entera, sin celdas |
|---|---|---:|---:|---:|---:|---:|---|
| cola | unidad | 42 | 6 | 5 | 0 | 31 | False |
| aceptadas:items | unidad | 1.136 | 147 | 13 | 25 | 951 | False |
| aceptadas:no_items | unidad | 2.116 | 144 | 143 | 69 | 1.760 | False |
| vigilancia:2 | unidad | 198 | 81 | 7 | 4 | 106 | False |
| vigilancia:7 | arista | 4 | 1 | 0 | 1 | 2 | True |
| observacion:12 | arista | 28.062 | 1.021 | 5.030 | 830 | 21.181 | False |

Unidades en `finales.jsonl`: 3.294; la cola, 42; las aceptadas (los tres estados juntos), 3.252. Las partes por corte de E1 que usan el chunk de su unidad: ri_rml::Sbloque14::parte1, ri_rml::Sbloque14::parte2, ri_rml::Sbloque14::parte3, ri_rml::Sbloque14::parte4, ri_rml::Sbloque14::parte5.

#### Tabla T2. Cuántos se sortean por celda, y lo que se declara (`celdas_t4_t3f.asignar`)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto | total | notas |
|---|---:|---:|---:|---:|---:|---|
| cola | 6 | 5 | 0 | 19 | 30 | la clase RI tiene 11 de su cuota de 15: entran todos; faltan 4, que salen de la otra clase: 1 a NG:sin_raiz y 3 a NG:resto; la celda NG:sin_raiz tiene 0 de su cuota de 6: entran todos; NG:resto sortea 6 más |
| aceptadas:items | 10 | 5 | 5 | 10 | 30 | — |
| aceptadas:no_items | 10 | 5 | 5 | 10 | 30 | — |
| vigilancia:2 | 10 | 5 | 4 | 11 | 30 | la celda NG:sin_raiz tiene 4 de su cuota de 5: entran todos; NG:resto sortea 1 más |
| vigilancia:7 | 1 | 0 | 1 | 2 | 4 | 4 elementos: se lee entera, sin celdas |
| observacion:12 | 10 | 5 | 5 | 10 | 30 | — |

#### Tabla T3. Los pesos reales por celda (w_c = N_c / N de la población de cada muestra)

| muestra | RI:sin_raiz | RI:resto | NG:sin_raiz | NG:resto |
|---|---:|---:|---:|---:|
| aceptadas:items | 0,1294 | 0,0114 | 0,0220 | 0,8371 |
| aceptadas:no_items | 0,0681 | 0,0676 | 0,0326 | 0,8318 |
| cola | 0,1429 | 0,1190 | 0,0000 | 0,7381 |
| vigilancia:2 | 0,4091 | 0,0354 | 0,0202 | 0,5354 |
| vigilancia:7 | 0,2500 | 0,0000 | 0,2500 | 0,5000 |
| observacion:12 | 0,0364 | 0,1792 | 0,0296 | 0,7548 |
| proyección de la E0 (pre-registro) | 0,0903 | 0,0477 | 0,0286 | 0,8334 |

#### Tabla T4. Los umbrales, con los pesos reales (`muestras/umbrales_t4_reales.json`) y la proyección del pre-registro

| estrato | n efectivo | atención desde (p) | freno por intervalos desde | atención sobre las 60 desde | errores en una sola celda para la atención |
|---|---:|---|---:|---:|---|
| items (reales) | 13,912 | 0,383 (0,0489) | 0,627 | 0,331 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 5 de 10 |
| items (proyección) | 14,105 | 0,380 (0,0493) | 0,626 | 0,330 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 5 de 10 |
| no_items (reales) | 14,130 | 0,284 (0,0492) | 0,536 | 0,242 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 4 de 10 |
| no_items (proyección) | 14,105 | 0,286 (0,0497) | 0,535 | 0,242 | RI:sin_raiz no alcanza sola, RI:resto no alcanza sola, NG:sin_raiz no alcanza sola, NG:resto 4 de 10 |

- **Tasa ponderada total:** n efectivo 25,817 (proyección 27,572); pesos de los estratos ítems 0,3493 y no ítems 0,6507. La tanda 0 con el mismo método: 0,1616, Wilson [0.0888, 0.276].
- **Atención de RI** (447 unidades RI aceptadas): salta desde una tasa ponderada de RI de 0,291 (p 0,0500); bajo H0, 0,1572; n efectivo 23,906; potencia con la tasa de RI duplicada 0,5971. Proyección: 0,278, 0,1616, 29,301 y 0,6940.
- **La cola, regla del 25 %:** n efectivo 28,646; límite superior de Wilson con 0 errores 0,1182; con 1 error en cada celda sola: RI:sin_raiz 0,1570, RI:resto 0,1570, NG:resto 0,1793. Es cifra y vigilancia, no freno.
- **Los controles:** la importación del script de la mesa reproduce su JSON byte a byte: True; las tres cuentas con los pesos proyectados dan sus cifras: True.

#### Tabla T5. Los sorteos (`muestras/sorteos_t4.json`; base `33a3c34b…`; poblaciones `3dce23d7…`)

| muestra | archivo | elementos | sha256 | hora |
|---|---|---:|---|---|
| cola | `muestras/cola.json` | 30 | `89305f3ffa8bc22d60b46fcfecf35c6efe4eb01347277b1f47d5813f1852740b` | 2026-10-18T10:09:26-03:00 |
| aceptadas:items | `muestras/aceptadas_items.json` | 30 | `35622d640abb2d3997f2c39b321537a74025713ad1e5605b75d63eae790189d9` | 2026-10-18T10:09:26-03:00 |
| aceptadas:no_items | `muestras/aceptadas_no_items.json` | 30 | `41d2f3ea8a42c82db07cfa47c0b237014579b965ff994ccd462ad3dcbc36e3e1` | 2026-10-18T10:09:26-03:00 |
| vigilancia:2 | `muestras/vigilancia_2.json` | 30 | `68776dd00d4c49d4fee1a04837cafaf1de4312262f05b358121abd4c6f265d73` | 2026-10-18T10:09:26-03:00 |
| vigilancia:7 | `muestras/vigilancia_7.json` | 4 | `5e30a60b1c8c2fc076ef521217f8ec795921a880aefcf73b62d7681986e2b7d0` | 2026-10-18T10:09:26-03:00 |
| observacion:12 | `muestras/observacion_12.json` | 30 | `84151a2772d0edb87f79cadad91e5d3207d543b6d55eaf0761fb067ae58eb446` | 2026-10-18T10:09:26-03:00 |

La segunda corrida (`muestras/segunda_corrida_de_los_sorteos/`) da las seis muestras byte a byte iguales, y el índice igual salvo las horas (`consola_sorteos_corrida2.txt`). Las vigilancias (1) y (3) no se sortean; las cadenas de la ampliación no se usan.

#### Tabla T6. El material (`muestras/material/material_t4.json`, 2026-10-18T10:12:10-03:00)

| muestra | fichas | fichas (.jsonl) | fichas (.md) | planilla (.csv) |
|---|---:|---|---|---|
| cola | 30 | `5f348167cd038cf1…` | `0fe36f519804fe76…` | `05ca58fcc2a212f7…` |
| aceptadas:items | 30 | `c81f6f8cbc33a6ab…` | `7723ee4bf788d356…` | `15e7f9e21c98dbaa…` |
| aceptadas:no_items | 30 | `30a64bcfa1484b3b…` | `ac880d955f8af72a…` | `188fae5b29d329f4…` |
| vigilancia:2 | 30 | `eab2d878b510f4c7…` | `524f0c3abd1981c3…` | `760b7af10b75c6ed…` |
| vigilancia:7 | 4 | `4957839fd5aa97bc…` | `6975a645e75c5c4e…` | `11cb97845b9978bb…` |
| observacion:12 | 30 | `6075d991a2ce1ae4…` | `a4dd2d2eee6137b0…` | `fd04235baf84a33a…` |

#### Tabla T7. Las unidades a la vista (`muestras/unidades_a_la_vista_T4.json`, 2026-10-18T10:13:10-03:00)

| muestra | fichas | unidades a la vista | por versión | de ellas, solo por un TextoOrdenado o un Sujeto (información) |
|---|---:|---:|---|---:|
| cola | 30 | 30 | {'primera': 30} | 0 |
| aceptadas:items | 30 | 2.189 | {'final': 2189} | 2.155 |
| aceptadas:no_items | 30 | 2.579 | {'final': 2579} | 2.545 |
| vigilancia:2 | 30 | 2.161 | {'final': 2161} | 2.131 |
| vigilancia:7 | 4 | 156 | {'final': 156} | 152 |
| observacion:12 | 30 | 2.144 | {'final': 2144} | 2.110 |
| todas | — | 3.019 | {'primera': 30, 'final': 2989} | — |

#### Tabla T8. Las vigilancias (1) y (3): la población de la definición propuesta (información; no se sortean)

- (1): nodos Condicion del grafo evaluado: 1.401, por celda {'NG:resto': 1163, 'RI:sin_raiz': 94, 'NG:sin_raiz': 42, 'RI:resto': 102}.
- (3): grupos de 2 nodos o más de contenido con la misma unidad de procedencia primaria y el mismo tramo normalizado (espacios y mayúsculas): 181 grupos con 373 nodos, por celda del nodo de id menor {'NG:resto': 133, 'RI:resto': 42, 'RI:sin_raiz': 5, 'NG:sin_raiz': 1}.

**Las definiciones de las poblaciones, tal como las apliqué** (docstring de `poblaciones_t4_t3f.py`):
- la clase sale de `categoria` del manifiesto (RI y no-RI) y el modo, de `modo_lectura` (`sin_raiz`, en ceninf, nmcief, ri_ccna y
  ri_mmsef, lo mismo que en `lista_tanda1_S2.json`);
- el grafo es el evaluado (el sin cola), salvo la cola;
- la (2) son las unidades aceptadas cuya extracción final no tiene relaciones: la cifra que el código de la tanda 0 da como total
  (`lectura_e6_tanda0.py:231-252`);
- la (12) es el universo de A4.1 tal cual: todas las aristas menos `referencia` y menos el esqueleto.

**El material:**
- el texto de cada unidad es `comun_e3.fuente_integro(chunk, bloque_de_lista=ratchet_e3._forma_r2(validacion))`, con el chunk de la E0 con
  las partes en las 4 fichas de partes por corte;
- sin el estado de E3 ni sus marcas: el control por script da 0 claves vedadas en las 154 fichas (`muestras/control_material_t4.txt`);
- la hora del material, 10:12:10, es posterior a la de los sorteos, 10:09:26;
- las planillas en blanco van en CSV, con las columnas del veredicto de cada lectura.

**Las vigilancias (1) y (3): las definiciones que propongo** como regla general. No las sorteé: decide la autora antes del sorteo.
- **(1), migraciones a Condicion contra la guarda de modalidad.**
  - Elementos: los nodos Condicion del grafo evaluado.
  - Muestra: 30 con las celdas y la cadena `tanda1:vigilancia:1:<celda>:<base>`.
  - Pregunta: ¿la Condicion expresa un deber explícito (debe, deberá, está obligado a) que el texto de su unidad formula como obligación, y
    no como condición? Respuestas: sí (migración), no o no decidible.
  - Tasa ponderada por celda, con Wilson.
- **(3), duplicación entre cajas.**
  - Elementos: los grupos de 2 nodos o más de contenido con la misma unidad de procedencia primaria y el mismo tramo normalizado (espacios y
    mayúsculas). La celda es la del nodo de id menor (§5.4 bis, punto 2, v8c).
  - Muestra: 30 grupos con la cadena `tanda1:vigilancia:3:<celda>:<base>`.
  - Pregunta: ¿los nodos del grupo repiten el mismo contenido normativo (duplicación), o son contenidos distintos sobre el mismo pasaje?
  - Tasa ponderada por celda, con Wilson.
- Las poblaciones de las dos definiciones están en la tabla T8 (información).

## 7. Lo declarado por las decisiones 1, 2, 3, 6 y 7

1. **La E0 que rige para S31** es la E0 con las partes por corte. Es una precisión del gate tomada con el resultado a la vista, y vale
   igual para la tanda final. Se informan las dos corridas: con la E0 del repo, S31 falla en los cuatro grafos; con la E0 con las partes,
   pasa.
2. **E4-a1 y E4-a4 son regresiones de la tanda 1**, declaradas por la autora: dos sujetos propuestos que tienen candidato en el catálogo
   y que E4 no resolvió. La mesa diagnostica la causa en la ronda siguiente, sin gastar.
3. **En la tanda 1 sola**, los ítems con todas sus anclas en TOs que el grafo no tiene se informan aparte, como «fuera del grafo», y no
   cuentan: son 18 regresiones en cada grafo de la tanda 1, las 15 del cruce y las
   declaradas del laudo que caen fuera del grafo. Vale también para los
   grafos de los tramos de la tanda final.
4. **Las salidas de shapes y de la suite de los dos grafos de la tanda 1** quedan en `corpus_tanda1/ens_veinte_r2b/` y `_sincola/`, como
   en el re-sellado, y no en `t3/`. Es el error propio 4 del parcial.
5. **El selftest del catálogo** corrió en un `git clone` del repo que trajo cuatro archivos `.env` o `NO_ABRIR_`. Los borré por nombre,
   sin abrirlos; la mesa mostró con un grep que ningún selftest de la cadena lee esas rutas. Es el error propio 1 del parcial. En esta
   parte no hice ningún `git clone`.

## 8. Para la autora

1. **Los pozos de L-02 y de L-04 llegan a 30** (tabla C5). Por el §5.4 d, sus lecturas son al cierre de la tanda 1. Quién lee y con qué
   regla se decidió el 15/10/2026. Las semillas se sellan antes de leer, y yo no las sorteé.
2. **`unidades_a_la_vista_T4.json`, con la regla tal cual, deja a la vista
   3.019 de las 3.294 unidades.**
   - Las fichas de unidad muestran sus aristas `establecida_en` hacia el TextoOrdenado y `aplica_a` hacia sujetos fusionados. La
     procedencia de esos nodos es la del TO entero o la de todas las menciones del sujeto.
   - Solo por esos dos tipos están a la vista 2.155 unidades en las aceptadas ítems y
     2.545 en las no ítems (tabla T7, información).
   - Si para U-MED-VERIF esos nodos no deben contar, cambia la regla; la información para recalcularla ya está en el archivo.
3. **La población de la vigilancia (2)** la tomé de la extracción final del grafo evaluado (198 unidades).
   El código de la tanda 0 mide también la del primer intento.
4. **El universo de la observación (12)** es el de A4.1 tal cual: 28.062 aristas. De ellas,
   11.900 son `establecida_en` y 8.838 `remite_a`. En
   la muestra de 30 hay 14 `establecida_en` y 7 `remite_a`
   (`muestras/composicion_obs12_t3f.json`). La nota de equivalencia del §5.2 habla solo de `remite_a`.
5. **Las definiciones de (1) y (3)** que propongo (sección 6), antes de su sorteo.
6. **La cola de la muestra:** la clase RI tiene 11 unidades en la cola y NG `sin_raiz`, 0.
   Por las reglas de las clases chicas, entran las 11 de RI y NG resto sortea 19 (tabla T2).

## 9. La foto del repo, los .pyc y el grep de convenciones

Lo genera `scripts/freno_t3f_foto.py` desde la foto del paso 0 y la de después (las dos van en el paquete).

- **La foto** (`t2/foto_repo_tanda1_t2.py`). Paso 0: 09:09:57 a 09:10:09 del 2026-10-18, 52.306 entradas. Después: 10:26:08 a 10:26:20 del 2026-10-18, 52.448 entradas, 15 sin abrir y 342 enlaces.
  - **157 nuevos:** 28 la base de Neo4j (neo4j/volumen/, fuera de git); 2 en `tanda1/t3/, lo demás`; 1 en `tanda1/t3/FRENO_T3_parcial.md (el renombre)`; 4 en `tanda1/t3/conteos_sin_leer/`; 36 en `tanda1/t3/gate_decisiones/`; 49 en `tanda1/t3/muestras/`; 16 en `tanda1/t3/neo4j/`; 21 en `tanda1/t3/scripts/`.
  - **15 borrados:** 14 la base de Neo4j (neo4j/volumen/, fuera de git); 1 en `tanda1/t3/FRENO_T3.md (renombrado al parcial; el final se escribe después de la foto)`.
  - **76 cambiados:** 75 la base de Neo4j (neo4j/volumen/, fuera de git); 1 en `neo4j/grafos.py`.
  - **Fuera de lo admitido:** 0.
  - `grafos.py`: `2ac82a4826b65597…` (HEAD) → `204c17351299e919…`, de 16.742 a 19.052 bytes.
- **Los `.pyc`:** 11.236 líneas en el paso 0 y 11.236 después; listas iguales: True.

**El sha256 de los archivos clave, de la foto de después** (el del `NO_ABRIR_`, de la escritura):

| archivo | sha256 |
|---|---|
| `data/experiment/neo4j/grafos.py` | `204c17351299e91984868f7a6ad9a00f319b5a3cc01348ad78e514b3d0c877a8` |
| `data/experiment/tanda1/t3/registro_vista_r2b_tanda1.py` | `3de14f5301977fd8550b8426875cba0406690d78f507283fbcd44160ee6bd190` |
| `data/experiment/tanda1/t3/FRENO_T3_parcial.md` | `63abc417dfb3737e84d25c7c22623f1f3528218f923aa01a9f78299b6301e664` |
| `data/experiment/tanda1/t3/gate_decisiones/veredicto_gate_t3f.json` | `7b76363e9a25a8b631b71b65b17957157a832819f90836b29142b294cf5397f3` |
| `data/experiment/tanda1/t3/conteos_sin_leer/contado_sin_leer_t3f.json` | `226a404154c2458e5c750c8cb59cdc458dbe3880f4cf9c1282d5cb9f6a5a4944` |
| `data/experiment/tanda1/t3/muestras/poblaciones_t4.json` | `3dce23d7e9de8a3a68762347f8b6c323116395e2ddc1acd3d3d596427c802115` |
| `data/experiment/tanda1/t3/muestras/umbrales_t4_reales.json` | `687c760a13a854194dc91ae82b7b5110e860dfcd52c39bea65d6d8faf6b4691f` |
| `data/experiment/tanda1/t3/muestras/sorteos_t4.json` | `b401f900419c644294229a9242527041c14830c7f02e2234b659ff8d0c1d9c2e` |
| `data/experiment/tanda1/t3/muestras/material/material_t4.json` | `b90a7c5ba48384784b8ca70644e41dc271898adb124ec71734aae758cec26196` |
| `data/experiment/tanda1/t3/muestras/unidades_a_la_vista_T4.json` | `1e775850e94457c4d5e356c27bd247dbb8ba76731f302580ab7b2762306bfc12` |
| `data/experiment/tanda1/t3/NO_ABRIR_conteos_t3.json` | `446b67726bbf09a43fceeaf3782a2686eb7c66b7e4314af24a715477484585c8` |

**Los scripts nuevos de esta parte** (`t3/scripts/`, sha256 de la foto de después):

| script | sha256 |
|---|---|
| `cargar_neo4j_t3f.py` | `c020eb5e88aac555dd89ce8ee6a5bb5c7d7350c22534e0ea6d95956b9764edab` |
| `celdas_t4_t3f.py` | `f0082e3cd588e855e65d024fc360d669abba6da134199bc0b06bfc2a63e40c29` |
| `composicion_obs12_t3f.py` | `03b52371d8e288fc8a7ce0424376adbe0be95568149b1bc15ba2c138bd1133d2` |
| `contado_sin_leer_t3f.py` | `d16088af5733a2c11e1eef9882c422bd64e70ece34eb12d4c0cb9fd663f8e3a5` |
| `control_cola_neo4j_t3f.py` | `177bcfcb3fdb151476682a903a1220363dc2c16878ee42b0b74d8997942f06eb` |
| `dry_registro_t3f.py` | `b82635bf4e9af5b988bd64994f432c2093295159ec6c4622ea68d286d5f3e7f5` |
| `e0_partes_t3f.py` | `73dbd479854c9682918216b5cd9f3b3af56b88b3669364bd834a927a3669222a` |
| `editar_grafos_t3f.py` | `119ae5e1a3bd678f4cccb353b07d507e7188078ed1344d4f5921f2625696d537` |
| `escribir_en_el_repo_t3f.py` | `042227b6cc461cb72d964c325953d87954228023f25f9de8303553456792ae28` |
| `freno_t3f_armar.py` | `d3c12c255f748d930c35b4f64e459671988cc167e8172e78cbc2d3481f028472` |
| `freno_t3f_foto.py` | `d75d721d7fd862084c96c140fac9b087b5d089d460794531501995bcb95942ce` |
| `fuera_del_grafo_t3f.py` | `cec68a56cd78b45f9491d27e805cebdf30f23f76d77bd74249da7c080cf035a4` |
| `material_t4_t3f.py` | `905937e5d501fa0c7c5567e6c4e871318a75fe9bf097fa76d5b0ec52f9338167` |
| `poblaciones_t4_t3f.py` | `e713b0145614c1811ef697ec47963fc1de576b29e21378adda5ede0dcc7f2324` |
| `poner_saneado_t3f.py` | `cbb8deb888088daa25d836d5c4db447abcbf9cc7af574f7396e066bb369ffdd3` |
| `sorteos_t4_t3f.py` | `0bb32368619cd8f24e5f0e0c5129a26d8bb868b014176c22371d99a27404eb85` |
| `tablas_contado_t3f.py` | `9812e06474457c2ae671ef2228cd8f79e9a1651c808cf7e092412ccdcdee22a5` |
| `tablas_t4_t3f.py` | `08af683171b5b415c98e88d625976a0b1bb3f30bc310446eedc8bba76b009130` |
| `umbrales_t4_t3f.py` | `31bc8adeff8155c58c921b528139c0ef400a0787353904d9a2aa9b8e5c1f9aed` |
| `unidades_a_la_vista_t3f.py` | `5ca7fe5d81630b1148379d3dfee05e1e117be3dc06d875e4995b4c502894de13` |
| `veredicto_gate_t3f.py` | `9479a16e1f82d81a592b572d724a548a774616cce6b1d2f4bb76328e53c847c3` |

Los 16 scripts del FRENO parcial no cambiaron: True.

- **La base de Neo4j** (`data/experiment/neo4j/volumen/`) cambia con la carga del punto 5. Está fuera de git
  (`data/experiment/neo4j/.gitignore:4`) y no va al commit.
- **Escrito después de la foto:** solo este FRENO.
- **El grep de convenciones** (`grep_convenciones_t3f.py` y su salida, en el paquete) busca las palabras del `user.name` de git y las de
  origen conversacional en los 233 archivos nuevos o cambiados de esta parte, sin la base de Neo4j ni el `NO_ABRIR_`. El
  control positivo da su línea 2.
  - **En lo que redacté:** `FRENO_T3_parcial.md`, `freno_t3f_armar.py`: las líneas que citan palabras de la
    norma (el FRENO parcial, y la plantilla de este FRENO en su armado).
  - **Tokens del nombre:** 0.
  - **En las salidas de los generadores y en el material,** las coincidencias son texto de la norma (como «correo electrónico»).
  - **Rutas absolutas:** 2 archivos, los dos scripts que las nombran como literales de su control.
  - Sobre este FRENO, el grep corre después de escribirlo, y su resultado va en el mensaje del FRENO.
- **La escritura al repo** (`scripts/escribir_en_el_repo_t3f.py`, en seco y de verdad): 102 archivos nuevos y 1
  que cambia (`grafos.py`, igual a HEAD antes); 103 de 103
  iguales al staging. Después escribí, con control, `muestras/tablas_t4_t3f.md`, su consola y `muestras/composicion_obs12_t3f.json`.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna. No abrí ningún `.env` ni `NO_ABRIR_`; las copias del repo se hicieron
  con el `rsync` de la cláusula y su control dio 0 (`rsync_copia_t3f*.log` en el paquete). Ningún `git clone`.

## 10. Errores propios, con su causa

1. **Una regla de partes que no servía para la E0 de manori.** La primera corrida de `poblaciones_t4_t3f.py` cortó con un error: tomé
   como parte por corte de E1 todo id con `::parte`, y `manori::Sbloque4::parte3` es un chunk de la propia E0.
   - La causa: generalicé la regla de la tanda 0 sin mirar los ids de la E0 de la tanda 1.
   - La corregí antes de escribir nada: el id va tal cual si está en la E0, y si no, se usa su unidad, quitando solo el último `::parteN`.
2. **Dos anclas de línea mal puestas en un docstring.** En `poblaciones_t4_t3f.py` puse primero `lectura_e6_tanda0.py:246-263` y `:291-300`.
   Las verifiqué con `grep -n` antes de correrlo y las corregí: son `:231-252` y `:286-294`.

FRENO T3. Espero la revisión de la autora.
