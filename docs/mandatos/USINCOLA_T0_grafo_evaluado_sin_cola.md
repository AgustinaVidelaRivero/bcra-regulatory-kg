# Mandato U-SINCOLA-T0 — el grafo evaluado de la tanda 0 sin la cola humana

**VERSIÓN PARA FIRMAR (06/10/2026) — PENDIENTE DE FIRMA DE LA AUTORA.** Redactado por la mesa a partir de las decisiones de la
autora del 06/10/2026 (nota al pie del mandato de U-REEXT-T0, `c9d4c40`, decisiones 1 y 3; plan B2.11, sub-fila 11b). La firma
es por mensaje de la autora y se asienta en esta línea con su commit.

QUÉ ES. La lectura de la cola humana de la tanda 0 (U-REEXT-T0, T4; `889b2f9`) dio 12 de 30 unidades con error (Wilson al 95 %
[0,246; 0,577]) y disparó la regla del 25 % de la enmienda al protocolo del 04/10/2026 (`docs/enmienda_protocolo_entre_tandas_2026-10-04_cola_humana.md`,
§1, punto 6). La autora decidió que las 74 unidades de la cola salen del grafo evaluado de la tanda 0 por la forma (a): un
ensamblado nuevo sin la cola, sellado como versión posterior del grafo r2b (principio 9 del plan, `:277`). Esta unidad lo
produce, lo sella y lo registra. USD 0: ninguna llamada a la API; ensamblado, shapes, suite y Neo4j locales.

PRECONDICIONES (pegar la salida de cada comando en el freno; si una falla, frenar sin escribir).
a. U-REEXT-T0 cerrada: `git log --oneline -1 -- data/experiment/reext_t0` da `0a3ac81` (T5, correcciones y nota de cierre).
b. Los grafos sellados: `shasum -a 256` de `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json` empieza con
   `a9631a64` y el de `ens_desarrollo_r2b/r2/kg.json` con `6e756043`; `scripts/regression_kg_esperado.json` tiene esos dos
   `kg_sha256` en `estado_esperado`; `data/experiment/neo4j/grafos.py` tiene `commit_sellado` `bbc38dc` en las dos entradas r2b.
c. El código del ensamblado es el del sello: `git diff --stat bbc38dc HEAD -- data/experiment/tanda0/code
   data/experiment/reextraccion_v2/corpus_v2 data/experiment/reextraccion_v2/e2_reduce data/experiment/pyd_r2/code
   scripts/shapes_validator.py scripts/regression_kg.py` vacío. Esta unidad no cambia código: si un control falla por el
   código, se reporta.
d. La cola: 74 unidades con estado `cola_humana*` como última versión en `corpus_tanda0/salida_r2b/*/finales.jsonl`
   (29 `cola_humana`, 43 `cola_humana_veredicto_inutilizable`, 2 `cola_humana_reextraccion_invalida`), con `cap::4.2.1.2::parte1`.
e. La E0 r2b de la tanda 0 es la sellada: `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b/` tiene 57 archivos
   (manifiesto `tanda0_ens_diez_r2b.json`, `sellos.e0`: commit `9f6361e`, 57 archivos); `git diff --quiet 9f6361e HEAD -- <ese
   directorio>` y `git status --short -- <ese directorio>` vacíos.

DECISIONES YA TOMADAS POR LA AUTORA. No se vuelven a decidir.
1. Salen las 74 unidades, enteras, incluidas las 18 leídas sin error y `cap::4.2.1.2::parte1`.
2. El criterio es el del ensamblador con `--sin-cola` (función `aristas_derivadas_de_cola`): un nodo sale si toda su
   procedencia está en unidades de la cola; los 21 nodos marcados con procedencia fuera de la cola (11 Sujeto de catálogo, 9
   TextoOrdenado, 1 Restriccion) se quedan, recomputados sin esa procedencia. Referencia de la revisión y de T5 sobre un
   filtro equivalente (`t5/salida/anexo_cifras_t5.json`, `cola`): salen 313 nodos y 1.503 aristas (411 con la marca y 1.092
   derivadas: `remite_a` 1.004, `establecida_en` 86, `padre_sugerido` 2); quedan 8.503 nodos y 26.129 aristas, 0 colgantes.
   El ensamblado recomputa registros, derivadas y fusiones, así que las cifras pueden diferir: se declaran.
3. El grafo r2b completo (`a9631a64`, sello `c9540c0`) sigue sellado como medición del pipeline (gate, suite, 3 regresiones
   declaradas). El nuevo es el grafo evaluado de la tanda 0; sirve a las medidas intrínsecas, a la suite, a las shapes y a
   A1.8, no a EV2.
4. La entrada de la suite del grafo nuevo lleva las expectativas de la entrada r2b sellada sin cambiar ninguna; lo que
   difiera por la salida de la cola se declara ítem por ítem (la simulación de T5 dio un solo cambio, LN-5, por el registro
   de sujetos no mapeados, que el ensamblado regenera). La entrada la sella la autora.
5. La forma A del vínculo y el hallazgo 2.13 se declaran límite (decisiones del 06/10/2026): esta unidad solo los cuenta.

CONVIVENCIA CON S0-2 DE U-SEG-OFICIAL, QUE CORRE EN PARALELO. S0-2 edita `data/experiment/reextraccion_v2/e0_chunking/e0_lib.py`
y `correr_e0.py` y escribe en `data/experiment/segmentacion_oficial_e0r2/`; tiene prohibido tocar `corpus_tanda0/`,
`salida_tanda0_r2b/`, las bases de caché y `reext_t0/`. Esta unidad no importa ese código: `ensamblar_tanda0.py` lee la E0
como archivos (`--e0-r2`, `salida_tanda0_r2b/`) y sus imports son `corpus_v2`, `e2_reduce`, `pyd_r2` y `assemble`; las shapes,
la suite y `controles_t3.py` también leen archivos. Reglas:
1. Esta unidad no toca `e0_chunking/` ni `segmentacion_oficial_e0r2/`; S0-2 no toca nada de las ESCRITURAS de abajo.
2. Al inicio, `git status --short` completo: los archivos modificados o nuevos de S0-2 se listan como ajenos y no se tocan ni
   se agregan a ningún comando; no son motivo de freno. La copia se arma con rsync sin enlaces desde el repo; que incluya el
   `e0_lib.py` editado por S0-2 no afecta a esta unidad porque no se importa, y se deja dicho en el freno.
3. La precondición e protege la lectura compartida: los 57 archivos de la E0 r2b iguales al sello antes y después de cada
   corrida.
4. `.pyc` fuera de `.venv`: 2.213 al inicio; si al cierre difiere, se listan los archivos nuevos con su ruta (pueden ser de
   S0-2) y se declara; no se borran.
5. Neo4j lo usa solo esta unidad (SC2). El contenedor está corriendo y escribe su `debug.log`, que git ignora.

ETAPAS.
SC1. ENSAMBLADO SIN COLA (sobre una copia sin enlaces, con el sha256 de las carpetas tocables del repo antes y después).
1. Manifiesto `data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez_r2b_sincola.json`: copia de `tanda0_ens_diez_r2b.json`
   con `nombre` nuevo y una descripción que remita a esta unidad y a `c9d4c40`; nada más cambia (diff pegado en el freno).
2. Comprobación en seco: `--sin-cola` excluye exactamente las 74 unidades `cola_humana*` y ninguna otra (lista contra
   `finales.jsonl`); el resto de la cadena es la de T3-bis (mismo código, precondición c).
3. Corrida: `ensamblar_tanda0.py --manifiesto <nuevo> --entrada corpus_tanda0/salida_r2b --salida corpus_tanda0/ens_diez_r2b_sincola
   --sin-cola` más los argumentos que usó T3-bis (`--e0-r2 salida_tanda0_r2b`, perfil r2), en dos directorios de la copia:
   byte a byte iguales; después, en el repo, igual a la copia salvo las rutas absolutas del reporte (P20, punto 6), declaradas.
4. Shapes: `scripts/shapes_validator.py --kg <nuevo kg> --perfil r2 --fase r2b --e0 salida_tanda0_r2b --registro-dir <nuevo>/r2
   --excepciones data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json --out <copia>`: todas las bloqueantes en
   PASS; las informativas que cambien, listadas con la cifra antes y después.
5. Suite: `scripts/regression_kg.py --kg <nuevo kg> --perfil r2 --generacion 3 --catalogo
   data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json --politica-cuarentena flaggeada --registro-dir <nuevo>/r2
   --esperado <copia de la fixture con la entrada nueva> --out <copia>`: los 68 ítems, con la lista de los que cambian de estado
   respecto de la entrada r2b sellada y la causa de cada uno. La fixture del repo no se toca en SC1.
6. Qué salió: nodos y aristas que salen, por tipo y relación; las derivadas que salen y las nuevas si las hay; los 21
   compartidos antes y después (procedencias); 0 colgantes y 0 nodos con la marca de la cola en el grafo nuevo; el ejemplo de
   la tesis (18 unidades) y las 15 preguntas de control sin ninguna unidad ni ancla en la cola (0 y 0), y las 15 preguntas
   corridas sobre el grafo nuevo con `reext_t0/t1_preguntas_control.py` (T5 sobre la simulación: iguales).
7. La condición 10 del checklist (`:81`), sobre el grafo nuevo y sin agente, con el código de T3
   (`data/experiment/reext_t0/t3/controles_t3.py`, controles b y c) apuntado al kg de SC1, sobre la copia: (i) el nodo de la
   Excepcion de `cla::5.1.1.1` presente y no proveniente de la cola (en T3-bis,
   `Excepcion_los_creditos_para_consumo_o_vivienda_quedan_exceptuados_de_la_cartera_comercial__956a9c`, `cola: false`); (ii) desde
   cada nodo con procedencia en `cla::5.1.1::intro` se llega, por la jerarquía de la procedencia (chunk padre → chunks hijos, sin
   arista), a los nodos de `cla::5.1.1.1` y `cla::5.1.1.2`, con la lista de nodos alcanzados por hijo; (iii) se reporta si
   `cla::5.1.1::intro` conserva la Definicion de alcance y los tipos de `cla::5.1.1.1` (T3-bis: 2 Condicion, 1 Excepcion,
   1 Operacion, 1 TextoOrdenado); (iv) X17 (condición 2): al menos una `remite_a` desde un nodo anclado en `cla::5.1.1.1` hacia
   uno anclado en `cla::3.7` (T3-bis: 2). Si (i), (ii) o (iv) falla, se reporta y la condición vuelve a la autora; nada se
   re-extrae acá.
8. Dos conteos declarados como límite (decisión 5): la forma A, con el control 3.e de T3 (`e_forma_A` de `controles_t3.py`) sobre
   el grafo nuevo (en r2b completo: 42 de 715 Condicion de ítem); y el hallazgo 2.13 de U-REVISION-LIBRE, las citas del detector
   de remisiones irresolubles por «punto sin nodos» en el ensamblado nuevo, con la clave del registro de remisiones que
   `data/experiment/medicion_r2a/m1_freno.md:86` desglosa (en r2a de diez: 205 de 510 irresolubles), al lado de la cifra del
   grafo r2b completo y con las otras causas. Solo conteos; el detector no se toca.
FRENO SC1.

SC2. SELLO Y CARGA (con el «seguí» de la autora, que trae la entrada de la suite sellada).
1. `scripts/regression_kg_esperado.json`: solo la entrada nueva (`KG-Tanda0-Diez-r2b-sincola`, o el nombre que fije la autora),
   con el `kg_sha256` del grafo de SC1 y las expectativas de la decisión 4 (lo que difiera, con su nota).
2. `data/experiment/neo4j/grafos.py`: solo la entrada nueva (`KG_Tanda0_Diez_r2b_sincola`, label e índice fulltext propios,
   `ev2_key` propia, `commit_sellado` PENDIENTE hasta el sello); el registro de la vista en
   `data/experiment/sincola_t0/registro_vista_r2b_sincola.py`, con el patrón de `reext_t0/t3bis/registro_vista_r2b.py`.
3. Carga en Neo4j (`data/experiment/tanda0/code/cargar_neo4j_tanda0.py --grafo <clave> --out-dir data/experiment/sincola_t0/salida/neo4j`):
   gate 5 OK; ningún nodo cargado con la marca de la cola.
4. Suite y shapes sobre el repo tal como queda, con la fixture del repo: 0 regresiones nuevas respecto de la entrada sellada.
FRENO SC2, final. El sello (`commit_sellado` en `grafos.py`) va en el commit siguiente de la autora, como en `c9540c0`.

CRITERIOS DE ACEPTACIÓN (cada uno con su comando y su salida).
- Las 74 unidades excluidas, listadas, y ninguna otra.
- Doble corrida byte a byte; shapes bloqueantes en PASS; suite con la lista de cambios declarada.
- Los 21 nodos compartidos presentes, sin procedencia de la cola; 0 colgantes; 0 nodos con la marca de la cola.
- El ejemplo de la tesis y las 15 preguntas intactos (0 unidades y 0 anclas en la cola; las 15 respuestas iguales).
- Condición 10 sobre el grafo nuevo: Excepcion presente y fuera de la cola; alcance por jerarquía a `cla::5.1.1.1` y `cla::5.1.1.2`
  con la lista de nodos; X17 con al menos una `remite_a` hacia `cla::3.7`.
- Los dos conteos de SC1.8 con su cifra y su comando.
- `grafos.py` y la fixture solo con la entrada nueva; los sellados `a9631a64` y `6e756043` byte a byte intactos; los 57 archivos
  de la E0 r2b iguales al sello antes y después.

ESCRITURAS: `data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez_r2b_sincola.json` (nuevo);
`data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b_sincola/` (nuevo); `data/experiment/sincola_t0/` (se crea: frenos,
scripts de control, registro de la vista, salidas); en SC2, `scripts/regression_kg_esperado.json` y `data/experiment/neo4j/grafos.py`,
solo la entrada nueva; y el scratchpad.
PROHIBIDO: cambiar `ensamblar_tanda0.py`, los validadores, las shapes, la suite o cualquier código; tocar `ens_diez_r2b/`,
`ens_desarrollo_r2b/`, `salida_r2b/`, `salida_tanda0_r2b/`, `e0_chunking/`, `segmentacion_oficial_e0r2/`, `reext_t0/`, las entradas
selladas de la fixture y de `grafos.py`; correr EV2 o cualquier celda con agente; usar la API; commitear.
REQUISITOS: los de CLAUDE.md §4 (a a l): copia sin enlaces con el sha256 del repo antes y después; nunca un generador sobre el
repo; `PYTHONDONTWRITEBYTECODE=1` y `.venv/bin/python -B`; todo conteo recomputado contra su archivo; ninguna acción de la autora
como hecha; cero nombres de personas; grep de convenciones al cierre; paquetes `revision_USINCOLA_T0_FRENO_SC1/` y `_SC2/` con
`manifest.txt`.
DECISIONES DE LA AUTORA AL FIRMAR: (1) el nombre de la unidad y de la entrada de la suite y de `grafos.py`; (2) si
KG-Tanda0-Desarrollo-r2b también se rehace sin la cola, con un segundo manifiesto y una segunda entrada (recomendación de la
mesa: sí, para que el grafo donde se afina A1.8 tenga la misma política que el evaluado; costo marginal, una corrida más).
