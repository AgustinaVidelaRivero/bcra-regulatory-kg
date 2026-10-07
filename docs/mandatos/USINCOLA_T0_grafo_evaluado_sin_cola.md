# Mandato U-SINCOLA-T0 — el grafo evaluado de la tanda 0 sin la cola humana

**FIRMADO por la autora el 06/10/2026** (firma por mensaje de la autora; versión para firmar en `cc98075`). **Decisiones al
firmar:** (1) nombres: entradas de la suite `KG-Tanda0-Diez-r2b-sincola` y `KG-Tanda0-Desarrollo-r2b-sincola`; claves de
`grafos.py` `KG_Tanda0_Diez_r2b_sincola` y `KG_Tanda0_Desarrollo_r2b_sincola`; (2) KG-Tanda0-Desarrollo-r2b también se rearma
sin la cola, con su manifiesto (`tanda0_ens_desarrollo_r2b_sincola.json`), su salida (`ens_desarrollo_r2b_sincola/`) y su
entrada: todo lo que abajo se dice del grafo de diez vale para los dos grafos. Redactado por la mesa a partir de las decisiones
de la autora del 06/10/2026 (nota al pie del mandato de U-REEXT-T0, `c9d4c40`, decisiones 1 y 3; plan B2.11, sub-fila 11b).

QUÉ ES. La lectura de la cola humana de la tanda 0 (U-REEXT-T0, T4; `889b2f9`) dio 12 de 30 unidades con error (Wilson al 95 %
[0,246; 0,577]) y disparó la regla del 25 % de la enmienda al protocolo del 04/10/2026 (`docs/enmienda_protocolo_entre_tandas_2026-10-04_cola_humana.md`,
§1, punto 6). La autora decidió que las 74 unidades de la cola salen del grafo evaluado de la tanda 0 por la forma (a): un
ensamblado nuevo sin la cola, sellado como versión posterior del grafo r2b (principio 9 del plan, `:277`). Esta unidad lo
produce para los dos grafos de la tanda 0 (diez y desarrollo), los sella y los registra. USD 0: ninguna llamada a la API; ensamblado, shapes, suite y Neo4j locales.

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
1. Manifiestos `data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez_r2b_sincola.json` y `tanda0_ens_desarrollo_r2b_sincola.json`:
   copias de `tanda0_ens_diez_r2b.json` y `tanda0_ens_desarrollo_r2b.json` con `nombre` nuevo y una descripción que remita a esta
   unidad y a `c9d4c40`; nada más cambia (diff de cada uno pegado en el freno).
2. Comprobación en seco: `--sin-cola` excluye exactamente las 74 unidades `cola_humana*` y ninguna otra (lista contra
   `finales.jsonl`); el resto de la cadena es la de T3-bis (mismo código, precondición c).
3. Corrida, para cada grafo (g = diez, desarrollo): `ensamblar_tanda0.py --manifiesto <nuevo de g> --entrada corpus_tanda0/salida_r2b
   --salida corpus_tanda0/ens_<g>_r2b_sincola --sin-cola` más los argumentos que usó T3-bis (`--e0-r2 salida_tanda0_r2b`, perfil r2), en dos directorios de la copia:
   byte a byte iguales; después, en el repo, igual a la copia salvo las rutas absolutas del reporte (P20, punto 6), declaradas.
4. Shapes, en los dos grafos: `scripts/shapes_validator.py --kg <nuevo kg> --perfil r2 --fase r2b --e0 salida_tanda0_r2b --registro-dir <nuevo>/r2
   --excepciones data/experiment/catalogo_unico/generados_r2/entrada_esqueleto_r2.json --out <copia>`: todas las bloqueantes en
   PASS; las informativas que cambien, listadas con la cifra antes y después.
5. Suite, en los dos grafos (una entrada nueva por grafo en la copia de la fixture): `scripts/regression_kg.py --kg <nuevo kg> --perfil r2 --generacion 3 --catalogo
   data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json --politica-cuarentena flaggeada --registro-dir <nuevo>/r2
   --esperado <copia de la fixture con la entrada nueva> --out <copia>`: los 68 ítems, con la lista de los que cambian de estado
   respecto de la entrada r2b sellada y la causa de cada uno. La fixture del repo no se toca en SC1.
6. Qué salió, por grafo: nodos y aristas que salen, por tipo y relación; las derivadas que salen y las nuevas si las hay; los 21
   compartidos antes y después (procedencias); 0 colgantes y 0 nodos con la marca de la cola en el grafo nuevo; el ejemplo de
   la tesis (18 unidades) y las 15 preguntas de control sin ninguna unidad ni ancla en la cola (0 y 0), y las 15 preguntas
   corridas sobre el grafo nuevo con `reext_t0/t1_preguntas_control.py` (T5 sobre la simulación: iguales).
7. La condición 10 del checklist (`:81`), sobre los dos grafos nuevos (el ejemplo es de cla, que está en los dos) y sin agente, con el código de T3
   (`data/experiment/reext_t0/t3/controles_t3.py`, controles b y c) apuntado al kg de SC1, sobre la copia: (i) el nodo de la
   Excepcion de `cla::5.1.1.1` presente y no proveniente de la cola (en T3-bis,
   `Excepcion_los_creditos_para_consumo_o_vivienda_quedan_exceptuados_de_la_cartera_comercial__956a9c`, `cola: false`); (ii) desde
   cada nodo con procedencia en `cla::5.1.1::intro` se llega, por la jerarquía de la procedencia (chunk padre → chunks hijos, sin
   arista), a los nodos de `cla::5.1.1.1` y `cla::5.1.1.2`, con la lista de nodos alcanzados por hijo; (iii) se reporta si
   `cla::5.1.1::intro` conserva la Definicion de alcance y los tipos de `cla::5.1.1.1` (T3-bis: 2 Condicion, 1 Excepcion,
   1 Operacion, 1 TextoOrdenado); (iv) X17 (condición 2): al menos una `remite_a` desde un nodo anclado en `cla::5.1.1.1` hacia
   uno anclado en `cla::3.7` (T3-bis: 2). Si (i), (ii) o (iv) falla, se reporta y la condición vuelve a la autora; nada se
   re-extrae acá.
8. Dos conteos declarados como límite (decisión 5), en los dos grafos: la forma A, con el control 3.e de T3 (`e_forma_A` de `controles_t3.py`) sobre
   el grafo nuevo (en r2b completo: 42 de 715 Condicion de ítem); y el hallazgo 2.13 de U-REVISION-LIBRE, las citas del detector
   de remisiones irresolubles por «punto sin nodos» en el ensamblado nuevo, con la clave del registro de remisiones que
   `data/experiment/medicion_r2a/m1_freno.md:86` desglosa (en r2a de diez: 205 de 510 irresolubles), al lado de la cifra del
   grafo r2b completo y con las otras causas. Solo conteos; el detector no se toca.
FRENO SC1.

SC2. SELLO Y CARGA (con el «seguí» de la autora, que trae la entrada de la suite sellada).
1. `scripts/regression_kg_esperado.json`: solo las dos entradas nuevas (`KG-Tanda0-Diez-r2b-sincola` y `KG-Tanda0-Desarrollo-r2b-sincola`),
   cada una con el `kg_sha256` de su grafo de SC1 y las expectativas de la decisión 4 (lo que difiera, con su nota).
2. `data/experiment/neo4j/grafos.py`: solo las dos entradas nuevas (`KG_Tanda0_Diez_r2b_sincola` y `KG_Tanda0_Desarrollo_r2b_sincola`,
   label e índice fulltext propios cada una, `ev2_key` propia, `commit_sellado` PENDIENTE hasta el sello); el registro de la vista en
   `data/experiment/sincola_t0/registro_vista_r2b_sincola.py`, con el patrón de `reext_t0/t3bis/registro_vista_r2b.py`.
3. Carga en Neo4j (`data/experiment/tanda0/code/cargar_neo4j_tanda0.py --grafo <clave> --out-dir data/experiment/sincola_t0/salida/neo4j`, una vez
   por grafo): gate 5 OK en los dos; ningún nodo cargado con la marca de la cola.
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
- Todo criterio vale para los dos grafos. `grafos.py` y la fixture solo con las dos entradas nuevas; los sellados `a9631a64` y `6e756043` byte a byte intactos; los 57 archivos
  de la E0 r2b iguales al sello antes y después.

ESCRITURAS: `data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez_r2b_sincola.json` y `tanda0_ens_desarrollo_r2b_sincola.json`
(nuevos); `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b_sincola/` y `ens_desarrollo_r2b_sincola/` (nuevos); `data/experiment/sincola_t0/` (se crea: frenos,
scripts de control, registro de la vista, salidas); en SC2, `scripts/regression_kg_esperado.json` y `data/experiment/neo4j/grafos.py`,
solo las dos entradas nuevas; y el scratchpad.
PROHIBIDO: cambiar `ensamblar_tanda0.py`, los validadores, las shapes, la suite o cualquier código; tocar `ens_diez_r2b/`,
`ens_desarrollo_r2b/`, `salida_r2b/`, `salida_tanda0_r2b/`, `e0_chunking/`, `segmentacion_oficial_e0r2/`, `reext_t0/`, las entradas
selladas de la fixture y de `grafos.py`; correr EV2 o cualquier celda con agente; usar la API; commitear.
REQUISITOS: los de CLAUDE.md §4 (a a l): copia sin enlaces con el sha256 del repo antes y después; nunca un generador sobre el
repo; `PYTHONDONTWRITEBYTECODE=1` y `.venv/bin/python -B`; todo conteo recomputado contra su archivo; ninguna acción de la autora
como hecha; cero nombres de personas; grep de convenciones al cierre; paquetes `revision_USINCOLA_T0_FRENO_SC1/` y `_SC2/` con
`manifest.txt`.
DECISIONES TOMADAS AL FIRMAR (06/10/2026; están en la cabecera): (1) los nombres de las entradas y de las claves; (2) sí,
KG-Tanda0-Desarrollo-r2b también se rearma sin la cola, para que el grafo donde se afina A1.8 tenga la misma política que el
evaluado; costo marginal, una corrida más.

NOTAS POSTERIORES A LA FIRMA. El texto firmado son las 135 líneas de arriba (`723680e`, sha256 `da78aa8b0f7098ee…`) y no cambia.

- **06/10/2026 — ENMIENDA 1: la cadena r2 recibe `con_cola` (decisión de la autora tras el FRENO SC1: salida (A)).**
  1. **Hecho que la motiva** (`data/experiment/sincola_t0/freno_sc1.md`, SC1.2): `--sin-cola` solo actúa en la cadena r1
     (`ensamblar_tanda0.py` `main()`, `:1536-1537` → `ensamblar_manifiesto` → `etapa_e2`); la rama r2 de `main()` (`:1527-1530`)
     llama a `ensamblar_manifiesto_r2` (`:1403`) sin la bandera, y ni esa función ni `correr_cadena_r2` (`:1163`) la reciben. Con la
     bandera, el grafo r2b sale byte a byte igual al sellado (diez `a9631a64`, desarrollo `6e756043`) y entran las 74 unidades de
     la cola (59 en desarrollo). SC1.1 quedó hecho (manifiestos `fdfb5bf6…` y `031e164c…`); SC1.3 a SC1.8 no corrieron.
  2. **Error de la revisión, registrado.** La comparación de la mesa del 06/10/2026 (paquete del FRENO T4, segundo tramo) y la
     decisión 2 del texto firmado describieron al ensamblador con `--sin-cola` como el que «recomputa registros, derivadas y
     fusiones» en r2; eso no se verificó en la cadena r2 (el reporte de T5, §6, repitió la afirmación). La decisión 2 sigue
     valiendo como criterio (toda la procedencia en la cola; los 21 compartidos se quedan, recomputados), no como descripción
     del código.
  3. **Qué se autoriza** (levanta, solo para este cambio, la precondición c y el PROHIBIDO «cambiar `ensamblar_tanda0.py`»): en
     `data/experiment/tanda0/code/ensamblar_tanda0.py`, (a) `main()` pasa `con_cola=not args.sin_cola` también a la rama r2;
     (b) `ensamblar_manifiesto_r2` recibe `con_cola: bool = True` y lo pasa a sus dos corridas de `correr_cadena_r2`; (c)
     `correr_cadena_r2` recibe `con_cola` y, cuando es False, descarta los registros con `cola_humana` que devuelve
     `runner_corpus.entrada_r2` (`:1200`) antes de `resolver_relaciones_r2` y de `ensamblar_r2`, en ese único punto (el plan de
     redirecciones, `:582`, no lee registros). Con eso el registro de omisiones, el conteo de paso por E3, `cola_estados`,
     `flaggear_cola_r2` y `aristas_derivadas_de_cola` se computan sobre lo que queda, y el reporte del ensamblado declara
     `con_cola` y las unidades descartadas por TO. Nada más cambia: ni las reglas de E2, ni la resolución de sujetos, ni las
     derivadas, ni la fase. El criterio es el de la decisión 2.
  4. **Condiciones.** (i) Sin la bandera, byte a byte: la cadena r1 (su doble corrida y `--selftest-dev`), los dos r2a
     (`70d51e42…`, `fa4c1043…`) y los dos r2b sellados (`a9631a64`, `6e756043`): el control de T3-bis. (ii) Con la bandera: salen
     exactamente las 74 (diez) y las 59 (desarrollo: cap 10, cla 3, ext 43, pro 2, ric 1) y ninguna otra; 0 nodos y 0 aristas
     con la marca de la cola; `aristas_derivadas_de_cola` en 0; los 21 compartidos presentes, sin procedencia de la cola. (iii)
     Selftest: un caso nuevo en `data/experiment/r2_codigo/selftest_r3.py`, que ya tiene registros sintéticos de la cola
     (`:301-348`): con `con_cola=False`, la unidad en cola no aporta nodos ni aristas, un nodo con procedencia en ella y en otra
     unidad queda solo con la otra, y el registro de omisiones no lleva las suyas; con `con_cola=True`, la salida de hoy. (iv)
     Tabla de reprocesamiento: nota a la fila F15 (E2 r2 y ensamblado): parámetro `con_cola` de la cadena r2, solo código sobre lo
     guardado, no mueve claves de E1 ni de E3; `selftest_clave_cache` sigue en verde.
  5. **Convivencia con R2-1 de U-RERESOL-CAT.** W1 toca las mismas funciones (`plan_redirecciones_r2`, `correr_cadena_r2`,
     `ensamblar_manifiesto_r2`: parámetro opcional del catálogo de resolución). Orden: primero esta enmienda (SC1-bis),
     commiteada; R2-1 se despacha después y parte de ese commit. Los dos parámetros son independientes y conviven en las
     mismas firmas.
  6. **Etapas.** SC1-bis: el cambio sobre una copia, el selftest y los controles (i) a (iv); después, SC1.3 a SC1.8 del texto
     firmado para los dos grafos, con el código nuevo; FRENO SC1 completo. SC2 no cambia.
  7. **Escrituras agregadas:** `data/experiment/tanda0/code/ensamblar_tanda0.py`, `data/experiment/r2_codigo/selftest_r3.py`,
     `data/experiment/mantenimiento/tabla_reprocesamiento.md` (nota a F15). Lo demás, como en el texto firmado.
- **06/10/2026 — SC2 en espera (decisión de la autora).** El FRENO de U-DIAG-E3-LISTAS mostró que el verificador de E3 no recibe el bloque
  que abre la lista y reclama en falso sobre los ítems (17 reintentos y 7 unidades de la cola por esos reclamos en la tanda 0). Hasta que la
  autora decida qué se hace con la tanda 0 (re-verificar con E3 corregido o declarar el límite), U-SINCOLA-T0 termina SC1-bis y frena
  antes de SC2 (sello y carga). La lectura de muestra de las unidades aceptadas, prevista tras SC2, también espera.
- **06/10/2026 — la tanda 0 no se re-verifica: opción (ii) con (iii) (decisión de la autora); se levanta la espera de SC2.** La
  tanda 0 queda como está: el límite del verificador sobre los ítems de lista se declara con sus cifras (`docs/insumos_escritura.md`
  §7, ítem 4) y se mide aparte, sin re-sellar, cuántos reclamos desaparecen con E3 corregido (O3 de U-E3-LISTAS). Los grafos de esta
  unidad son los evaluados de la tanda 0, con la exclusión de la cola y ese límite declarados. Cuando llegue el FRENO de SC1-bis, la
  mesa lo revisa y la autora despacha SC2 (sello y carga). La lectura de muestra de las unidades aceptadas se despacha tras SC2.
- **06/10/2026 — revisión del FRENO SC1-bis: las dos cifras NO VERIFICADA y la declaración de los «punto sin nodos».** (1) El «18
  unidades» del ejemplo de la tesis (SC1.6 del texto firmado) era una cifra de la mesa sin ancla: sale de contar los ids `cla::…` de
  `docs/tesis/figuras/ejemplo_prestamo_datos.json`, que son 18 porque incluyen dos rótulos de búsqueda (`cla::3.7_en_top5`,
  `cla::5.1.1.1_en_top5`); las unidades del ejemplo son 16 ids, 15 con chunk en la E0 r2b (`cla::5.1.1` es el punto contenedor, sin
  chunk propio), y 0 están en la cola: el control de SC1.6 vale con esa definición. (2) El «715» de la forma A es `condicion_de_item`
  (601) más `sin_condicion_de` (114) de `reext_t0/t3bis/salida/controles_t3bis.json`, `e_forma_A.conteos`; en el grafo sin cola los
  denominadores son 575 y 113 (688) con los mismos 42 casos. (3) El aumento de las citas irresolubles por «punto sin nodos» en el grafo
  sin cola (diez: 213 de 495 → 255 de 530 en el reporte) se explica entero por la exclusión: en el registro de remisiones, 45 de las 257
  entradas «punto sin nodos» del grafo sin cola apuntan a una unidad de la cola (0 en el completo); sin ellas quedan 212 de 495, lo
  mismo que en el completo (213 de 503 por entradas). Cuando se reporte la cobertura del grafo evaluado, la cifra se declara
  desglosada: «citas a un punto sin nodos: N; de ellas, con destino en una unidad excluida del grafo evaluado por la regla de la cola:
  M, irresolubles por construcción y no por el detector; netas: N − M», con la cifra del grafo completo al lado. SC2 lo incorpora al
  registro de la vista y a su freno; la causa «destino en unidad excluida» como categoría propia del detector queda para una unidad
  de código posterior (U-OMISIONES-COD).
- **06/10/2026 — revisión del FRENO SC2 (final de la unidad) y nota de cierre (SC2 sin commit al escribir esta nota; la nota
  anterior quedó en 01046b6).**
  - La revisión independiente reprodujo SC2 sobre una copia sin enlaces: las siete entradas selladas de la fixture, iguales en
    su texto canónico a las de HEAD, y las dos nuevas copian su entrada r2b salvo `kg`, `kg_sha256`, `registro_dir`, el rótulo y
    la evidencia (diff +848/−0); `grafos.py` con exactamente dos claves más (+34/−0) y las selladas iguales; la suite sobre la copia
    con la fixture del repo da en los dos grafos los mismos 68 estados que el r2b sellado (56 coinciden, 9 NO VERIFICADAS, 3
    regresiones declaradas: RT-C5-3, RT-C6-1, RT-C6-2) y los mismos archivos que dejó SC2 en cada ensamblado; las shapes PASA con
    resultados y conteos iguales; `selftest_regression_kg` 184/184 y `selftest_shapes_congelado` 84/84; la corrida en seco de SC2
    (`sincola_t0/sc2/dry_registro_sc2.py`) OK con 9 claves; el desglose de «punto sin nodos» recomputado igual a lo declarado en los
    dos grafos; el control de Neo4j, en solo lectura, OK (8.503 / 26.129 y 6.723 / 22.084, 0 nodos y 0 aristas con la marca de
    la cola, `KG_Meta.kg_sha256` igual al sha256 del archivo, `commit_sellado` PENDIENTE); sha256 de 449 archivos del repo igual
    antes y después; 2.213 `.pyc`.
  - Conciliación de «punto sin nodos» (cuatro cifras, dos unidades de conteo). El registro de remisiones cuenta ítems de
    `irresolubles` (uno por entrada del registro; una misma cita puede estar en dos entradas); el reporte del ensamblado cuenta
    citas distintas por (chunk de origen, tramo, unidad citada), la `unidad_de_cita` que declara. En el grafo sin cola de los diez,
    257 ítems son 255 citas distintas: `ext::7.1.1.3` cita a `ext::7.1.1.1` y a `ext::7.1.1.2` con el mismo tramo en dos
    entradas; en desarrollo, 217 son 215 por las mismas dos. Lo mismo explica 503 contra 495 y 540 contra 530 (repeticiones en
    todas las causas); en el grafo completo no hay repetición entre las de «punto sin nodos» (213 = 213; 175 = 175). Las netas
    (212 en diez, 174 en desarrollo, iguales en las dos unidades de conteo) no coinciden con el grafo completo (213 y 175): la
    diferencia es una cita cuyo ORIGEN es una unidad de la cola (`ext::8.5.19.2` → `ext::8.5.17`), que el grafo completo cuenta y
    el grafo sin cola no tiene porque la unidad que cita quedó excluida. Las 45 (diez) y 43 (desarrollo) «con destino en una
    unidad excluida» del registro son 43 y 41 citas distintas: 36 y 34 con destino en una unidad de la cola, y 7 con destino en
    `cap::6.3`, cuyo único bloque con nodos (`cap::6.3::intro`) está en la cola; sin ellas, las 43 y 41 citas que el grafo sin cola
    suma respecto del completo se explican enteras por la exclusión.
  - Fe de erratas de la nota de la revisión de SC1-bis (01046b6, punto 3): decía «sin ellas quedan 212 de 495, lo mismo que en el
    completo (213 de 503 por entradas)». No es lo mismo: 212 = 213 − 1, por la cita con origen en la cola; y «212 de 495» mezclaba
    la unidad del registro (ítems) con la del reporte (citas distintas). La fórmula de declaración de esa nota sigue vigente, con
    la unidad de conteo dicha en cada cifra.
  - Propuesta de la mesa para la cifra que cita la tesis (la decisión es de la autora y se asienta con el sello): la del reporte
    del ensamblado, citas distintas, que es la unidad que la sección 4.5 ya usa para `remite_a`: en el grafo evaluado de los diez,
    255 citas a un punto sin nodos de 530 irresolubles, 43 con destino en una unidad excluida por la regla de la cola, netas 212;
    grafo completo 213 de 495, una de ellas con origen en la cola. Desarrollo: 215 de 446, 41, 174; completo 175 de 411.
  - Pasos siguientes. El sello (`commit_sellado` en `grafos.py`) va en el commit siguiente de la autora, con la decisión anterior;
    con él la unidad queda CERRADA. R2-1 de U-RERESOL-CAT, en FRENO con W1 a W3 como parches, los aplica al repo cuando su «seguí»
    siguiente le traiga el hash del commit de SC2 (la instancia no lo detecta sola: su despacho fijó la condición, no el aviso).
    La lectura de muestra de las unidades aceptadas, prevista tras SC2, queda en su mandato en versión para firmar
    (`docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md`, unidad U-LECTURA-ACEPTADAS).
- **06/10/2026 — sello de los dos grafos sin la cola y cifra de «punto sin nodos» para la tesis (decisión de la autora).** SC2
  quedó commiteada en `dde9f44`; este commit pone ese hash en `commit_sellado` de `KG_Tanda0_Diez_r2b_sincola` y
  `KG_Tanda0_Desarrollo_r2b_sincola` (`data/experiment/neo4j/grafos.py`). La cifra de «punto sin nodos» que cita la tesis es
  la del reporte del ensamblado (citas distintas por chunk de origen, tramo y unidad citada, la unidad de cita que ya usa la sección 4.5): diez 255 de 530 citas irresolubles, 43 con destino en una unidad excluida por la regla de la cola, netas 212, grafo completo 213 de 495 (una con origen en la cola); desarrollo 215 de 446, 41, 174, completo 175 de 411. Con este commit, U-SINCOLA-T0 queda CERRADA.
- **07/10/2026 — nombres de los dos grafos de cada tanda (decisión D13 de la autora, RECONC-DISENO-EVAL).** Donde este mandato y su
  nota de cierre dicen «grafo evaluado de la tanda 0» (o «grafo evaluado sin la cola»), léase **«grafo sin cola de la tanda 0»**: los
  dos grafos sellados en `dde9f44` y `235a295` (KG-Tanda0-Diez-r2b-sincola `e22fae1a…` y KG-Tanda0-Desarrollo-r2b-sincola
  `2922b72d…`); el ensamblado con la cola adentro y marcada es **«grafo completo de la tanda 0»**. «El grafo evaluado», a secas, queda
  reservado al escalado sellado antes del pre-registro de B6.3 (laudo 3 del 20/09/2026, `docs/plan_tesis.md`, principio 9) y «el grafo
  corregido» a la release posterior a la evaluación (`docs/protocolo_dos_grafos.md`, BORRADOR). El texto firmado no se edita.
