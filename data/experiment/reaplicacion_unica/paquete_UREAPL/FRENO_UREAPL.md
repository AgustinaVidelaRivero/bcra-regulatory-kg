# FRENO U-REAPL: la re-aplicación única del código al acumulado de las tres tandas

23/10/2026. USD 0: no llamé a la API, no escribí en el repo ni en la memoria y no commiteé. Corrí todo sobre una copia del repo en
`fuera_del_repo/reaplicacion_unica/copia_repo/` (CLAUDE.md, §4.l). Rigen el mandato U-REAPL (`docs/mandatos/UREAPL_reaplicacion_unica.md`,
firmado en `7cbf3525`, con las cinco precisiones de su «Firma») y el de las remisiones
(`docs/mandatos/UREMISIONES_SUBPUNTOS_remision_a_punto_padre.md`, opción B), leídos con `git show HEAD:<ruta>`.

Las rutas relativas de este FRENO son relativas a `fuera_del_repo/reaplicacion_unica/` (la carpeta de trabajo), salvo las que empiezan
con `data/`, `docs/` o `scripts/` del repo, que son del repo (o de su copia, idéntica); `scripts/` a secas, cuando nombra un script mío
(`scripts/medir_paso.py`, …), es la carpeta de trabajo. En el paquete, cada archivo va como `ureapl_` más su ruta relativa con `/`
cambiada por `__` (por ejemplo, `mediciones/paso2/sin_cola/medicion.json` → `ureapl_mediciones__paso2__sin_cola__medicion.json`).

## 0. Resumen

- **Paso 0, copia y foto:** todo da. La foto del repo es la misma al principio y al final (`7d01a251…`, 30.456 entradas).
- **Controles:** R19 rc 0 con las dos bases iguales; los tres selftests del 163, 66/66, 67/67 y 39/39 PASS.
- **Paso 1 = el sello,** byte a byte, en los dos grafos (`kg.json`, el registro de sujetos y el de remisiones; también todos los demás
  archivos, salvo el reporte, que es igual con las rutas normalizadas).
- **Las cuatro piezas entran.** En cada paso, cada pieza toca solo lo suyo, en los dos grafos; ningún caso de freno del §5: ninguna
  tripla de un predicado ajeno, ninguna regla de shapes cambia de resultado, ningún ítem de la suite cambia de estado y la regresión
  contra el sello es la misma (las 5 del T3) en los cinco pasos. Ninguna `remite_a` cambia por D y por las remisiones a la vez.
- **Un apartamiento del despacho, decidido por la autora:** el label y el alias de las claves van sin su artículo inicial (§4).
- **Lo que declaro sin que sea caso de freno:** 20 relaciones sin cola (21 con cola) de claves sin veredicto que entre (3 de una clave
  «no entra» y 17/18 de 16/17 claves fuera de los veredictos) se re-resuelven por el calificador o el slug con los labels nuevos (§6.3).
- **Las remisiones:** 765 citas y 24.301 `remite_a` nuevas sin cola, 783 y 27.133 con cola; la diferencia con las cuentas sobre las
  tandas 0 y 1 queda explicada cita por cita (§7).
- **El censo de C1:** las colisiones del paso 2 son las del paso 1, y el sello da 472 / 32 / 120 / 0, sus cuentas; las 32 uniones son
  las 32 colisiones.
- **El grafo evaluado** (el del paso 5), armado dos veces, byte a byte igual: con cola `1bd5ffcd…`, sin cola `576c9725…` (§9).
- **El cegamiento:** ninguna salida trae contenido de nodos ni una unidad de la muestra; casos en espera: no (§10).

## 1. El paso 0 (`controles/paso0.txt`, `ureapl_paso0.txt`)

- `pwd`: `$HOME/INGENIERIA IA/TESIS/fuera_del_repo/reaplicacion_unica`, y la carpeta vacía (`ls -A` sin salida).
- `git log -5`: `2db79462` (HEAD), `4ee44c51`, `f619128d`, `896223dd`, `e9481002`; `merge-base --is-ancestor 4ee44c51 HEAD`: rc 0;
  `status --porcelain --untracked-files=no`: vacío.
- El código de las cinco piezas en HEAD es el de `0765be9a`: el `diff --name-only 0765be9a HEAD` de las cinco carpetas, vacío.
- El sello del acumulado (`data/experiment/tanda_final/t3/FRENO_T3.md:143-144`): `kg.json` con cola `c43d66e5…` y sin cola `398459a8…`,
  los dos iguales a la tabla; `no_mapeados_sujetos.jsonl` sin cola `25ba55c8…`.
- Los insumos, por sha256: `no_unir_c1_desde_el_censo_marcado.json` `aa6aa007…`, `conteos_acumulado_tres_tandas_sin_cola.json`
  `5e609b56…`, `veredictos_claves_catalogo_segunda_pasada.json` `e1be9926…`, `material_claves.jsonl` `5fcca72a…` y el sorteo de las
  FICHAS `e27796ce…`: los cinco dan.
- El control del SDK (`.venv/bin/python -I -B scripts/control_sdk_anthropic_juez_y_banco.py`, desde la raíz del repo): los cinco OK, rc 0.
- El script del censo de la mesa (`censo_c1_con_control_de_la_muestra_mesa.py`) da `c9d41233…`; lo controla `scripts/muestra_memoria.py`
  antes de tomar de él `ids_en`, `listas_de_ids` e `ID`.

## 2. La copia y la foto del repo

- La copia: `rsync -a --no-links` con los once `--exclude` del despacho, de 11:53:50 a 11:54:44 (54 s). Saltó 336 enlaces (todos en
  `data/experiment/ev2_corrida/navegabilidad/trazas_nav/`). En la copia, `find -type l`: 0, y 0 archivos o carpetas con los nombres vedados
  (`NO_ABRIR_*`, `*_SOLO_MESA*`, `.env`, `.env.*`, `*.env`, `.git`, `.venv`, `.venv-app`, `__pycache__`, `.DS_Store`, `.claude.json`);
  29.806 archivos. Nunca un `git clone`.
- La foto (`controles/foto_repo.py`: sha256 de cada archivo del árbol de trabajo del repo, sin `.git`, `.venv` ni `.venv-app`; los
  enlaces, marcados): al principio, a las 11:53:33, antes de la copia y antes del control del SDK, 30.456 entradas (336 enlaces) y
  `7d01a251f8b96ce59cd72abec3680c4f7dbf2a81d673740a40d24c749483318a`; al final, a las 13:35:25, la misma (`cmp` sin diferencias).
  HEAD sigue en `2db79462` y `status --porcelain --untracked-files=no`, vacío. Las dos fotos enteras quedan en `controles/` (no van al
  paquete: listan las rutas de todos los archivos del repo); al paquete va su resumen (`ureapl_controles__foto_repo_resumen.txt`).

## 3. Los primeros controles, sobre la copia

- **R19** (`data/experiment/mantenimiento/code/selftest_clave_cache.py --out controles/r19_selftest_clave_cache.json`, desde la raíz de la
  copia, con el python del `.venv` del repo; `controles/r19_consola.txt`, `ureapl_r19_consola.txt`): rc 0, «contraste con la tabla: OK»,
  «VEREDICTO: OK», la R23 y la V23 «e1=cambia» con `gerc::1.1`, 7,45 s. Las dos bases de la caché de la copia, con el mismo sha256 antes
  y después: `e1_extraccion.db` `d95510f6…` y `e3_verificacion.db` `3579d464…` (`controles/r19_bases_{antes,despues}.txt`).
- **Los tres selftests del 163** (`controles/selftest_*.txt`), con las referencias que piden:
  - `proc_herencia/selftest_procedencia_heredada.py --ensamblar-head --referencias-head`, con los dos archivos de `0765be9a^` (blobs
    `2f40f6ef…` y `6ba07577…`, los de antes del 163): **66/66 PASS**;
  - `med_desamb/c1_cadena/selftest_union_comunicaciones.py --invariantes-head`, con el `r1_invariantes.py` de `0765be9a^` (sha256
    `77123142…`, que el selftest controla), y `--trabajo controles/trabajo_c1/`: **67/67 PASS**;
  - `remisiones_subpuntos/selftest_remisiones_a_subpuntos.py --referencias-segunda-pasada`: **39/39 PASS**. La referencia es el
    `r1_referencias.py` de la segunda pasada de D (blob `84e8831f`), que no está en git (el 163 entró con D y las remisiones juntas). No
    abrí el paquete de esa unidad: la reconstruí desde el de HEAD quitando solo lo de la opción B (`controles/reconstruir_ref_d.py`), y
    la acepté porque su blob da `84e8831f32bae22ca10d28271238e72c035b70db`, el sellado en los dos mandatos.
  - Son las cifras del registro de decisiones, §92 (66, 67 y 39).

## 4. Las entradas de las piezas

- **La entrada del acumulado** (la del sello, que no está en el repo): en la copia aparté la E0, el manifiesto de extracción y el registro
  del armado (que sí están) y corrí `tanda_final/t3/scripts/armar_acumulados_tf.py <copia> 128` (2,64 s; rc 0). Su
  `armado_acumulado_128_tf.json` es byte a byte el del repo: 2.295 archivos, 530.323.665 bytes, la lista `e19d926a…`, todos iguales a su
  origen; la E0 (640 archivos) y el manifiesto (`7a17222c…`), iguales a los del repo.
- **D:** la bandera `--procedencia-heredada`.
- **Las claves** (`scripts/armar_ampliaciones_claves.py`): la lista de ampliaciones desde los 105 veredictos y el material (que controla
  por sha256, con su clave reproducida en las 595 filas y las 172 formas del material: `_norm_sing(_sin_parentesis(...))` de r1_e4 sin el
  artículo inicial): 35 `alta_id`, 12 `alta_alias`, 58 «no entra»; 230 filas de evidencia del registro sellado (cuarentena, mención
  verificada, solo de las unidades del material); 6 altas esperan a que exista su id (4 con padre nuevo, 7 alias de un id nuevo), y el
  orden lo resuelve. `componer` aceptó las 47.
  - **Apartamiento del despacho, decidido por la autora:** 32 de las 47 formas elegidas empiezan con artículo. E4 saca el artículo de la
    mención antes de comparar («la mención se copia con artículos; el catálogo no los lleva», `r1_e4.py:344`), así que con el label o el
    alias tal cual no se iguala ninguna de sus menciones. Lo medí en memoria con la regla de E4 sobre las filas de evidencia
    (`scripts/probar_resolucion_ampliaciones.py`):

    | variante | lista | catálogo compuesto | altas que re-resuelven todas / algunas / ninguna | alias todas / algunas / ninguna | filas al id |
    |---|---|---|---|---|---|
    | literal (la del despacho) | `49591601…` | `d24e8283…` | 23 / 3 / 9 | 5 / 0 / 7 | 174 de 230 |
    | sin el artículo inicial (la que entra) | `23f027af…` | `54147015…` | 35 / 0 / 0 | 10 / 2 / 0 | 227 de 230 |

    Le pregunté a la autora antes de seguir y decidió, tal cual: «Sin artículo. Sacá del label y del alias el artículo inicial con la
    misma regla con que E4 lo saca de la mención antes de comparar (r1_e4.py:344), y después poné la primera letra en mayúscula.
    Declaralo en el FRENO como apartamiento del despacho, con las cuentas de las dos variantes (la literal y la sin artículo), los
    sha256 de los dos catálogos (d24e8283… y 54147015…) y los dos alias que quedan resolviendo solo algunas de sus filas, por su clave y
    su código. Seguí con los pasos 3 a 5 con el catálogo sin artículo.» El artículo se saca con `r1_e4.RE_ARTICULO_INICIAL`.
  - **Los dos alias que resuelven solo algunas filas** (`scripts/alias_que_resuelven_a_medias.py`, `claves/alias_que_resuelven_a_medias.jsonl`):
    la clave «auditor interno», `alias:Sujeto_auditoria_interna`, 1 fila sí y 1 no; la clave «prestatario», `alias:Sujeto_deudor`, 3 sí y
    2 no. La causa es del índice de E4: un alias entra solo como `alias_exacto` (`C.norm`), sin la forma singularizada que sí tiene un
    label, así que una mención en otro número no lo iguala.
  - G: `reresolver_catalogo.py componer --ampliaciones claves/ampliaciones_resolucion_r2_ureapl.json --salida claves/G_catalogo_resolucion_ureapl`
    (sin `--registro-alcance`), con el manifiesto `0a5ed1fc…` (47 ampliaciones, 0 alcances, catálogo `54147015…`, request `c3ad1581…`). A la
    cadena va su copia byte a byte dentro de la copia del repo (`ureapl/claves/G_catalogo_resolucion_ureapl`, `diff -r` vacío), para que
    los reportes lleven una ruta relativa.
- **C1:** `--union-comunicaciones ureapl/c1/no_unir_c1_desde_el_censo_marcado.json --union-comunicaciones-sha256 aa6aa00741ca2b5ae59cc6cd043d7f4516b6af67d8e16c1c0ada8041ddcc1c44
  --union-comunicaciones-nodos ureapl/c1/nodos_no_unir_c1.json --union-comunicaciones-nodos-sha256 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`.
  La lista de nodos la escribí con `printf '[]\n'`, y da `37517e5f…`; la de códigos es la copia del insumo (`aa6aa007…`, `{"no_unir": []}`).
- **Las remisiones:** la bandera `--remisiones-a-subpuntos`.

## 5. Los cinco pasos: comandos, rc, tiempos y sha256

- **El camino:** el de `cadena_t3_tf.sh` (`acum128` y `acum128_sincola`: el mismo manifiesto de ensamblado y la misma E0, con
  `--entrada data/experiment/tanda_final/t3/acumulado/entrada_acumulado_128_r2b`), con el python del `.venv` del repo, `-B`,
  `PYTHONDONTWRITEBYTECODE=1` y `unset ANTHROPIC_API_KEY`, desde la raíz de la copia. El paso 1 corrió con `cadena_t3_tf.sh` de la copia
  tal cual; los pasos 2 a 5, con `scripts/cadena_ureapl.sh`, que es ese script con un solo agregado (las banderas, después de los cinco
  argumentos, van al final del comando, antes de `--salida`; su `diff` contra el original son las tres líneas del encabezado, la que
  toma las banderas y la del comando). Los lotes, con `tanda_final/t3/scripts/correr_lote_t3_tf.py --workers 4`
  (`corridas/lote_pasos_1_y_2.txt` y `corridas/lote_pasos_3_a_5.txt`, con sus `_rc.json`). Las salidas, en
  `copia_repo/ureapl/paso<n>/ens_128_r2b{,_sincola}/r2/`.
- **Las banderas:** paso 1, ninguna; paso 2, `--procedencia-heredada`; paso 3, + `--catalogo-resolucion ureapl/claves/G_catalogo_resolucion_ureapl`;
  paso 4, + las cuatro de C1 del §4; paso 5, + `--remisiones-a-subpuntos`. El paso 5 se armó dos veces (`ureapl/paso5_bis/`).

| paso | grafo | inicio – fin | minutos | rc | nodos | aristas | `kg.json` (sha256) | sujetos | remisiones |
|---|---|---|---:|---:|---:|---:|---|---|---|
| 1 | con cola | 12:03:24 – 12:27:33 | 24,2 | 0 | 38.324 | 114.925 | `c43d66e5…` (= sello) | `e293b3b6` (= sello) | `2b3515e3` (= sello) |
| 1 | sin cola | 12:03:24 – 12:25:38 | 22,2 | 0 | 37.321 | 104.279 | `398459a8…` (= sello) | `25ba55c8` (= sello) | `9ee8295c` (= sello) |
| 2 | con cola | 12:03:24 – 12:27:47 | 24,4 | 0 | 38.324 | 114.998 | `ab6896c5…` | `e293b3b6` | `6b71abc3` |
| 2 | sin cola | 12:03:24 – 12:26:27 | 23,0 | 0 | 37.321 | 104.317 | `f7cec446…` | `25ba55c8` | `2b4966e5` |
| 3 | con cola | 12:29:00 – 12:55:03 | 26,0 | 0 | 38.257 | 114.930 | `2072e03c…` | `c2af74d4` | `6b71abc3` |
| 3 | sin cola | 12:29:00 – 12:53:15 | 24,3 | 0 | 37.256 | 104.251 | `c0619237…` | `a83b9d9b` | `2b4966e5` |
| 4 | con cola | 12:29:00 – 12:55:16 | 26,3 | 0 | 38.169 | 114.930 | `5fe5d085…` | `c2af74d4` | `6b71abc3` |
| 4 | sin cola | 12:29:00 – 12:53:21 | 24,3 | 0 | 37.168 | 104.251 | `27aae35c…` | `a83b9d9b` | `2b4966e5` |
| 5 | con cola | 12:53:16 – 13:20:45 | 27,5 | 0 | 38.169 | 142.063 | `1bd5ffcd…` | `c2af74d4` | `411984d6` |
| 5 | sin cola | 12:53:21 – 13:18:09 | 24,8 | 0 | 37.168 | 128.552 | `576c9725…` | `a83b9d9b` | `fa5983b3` |
| 5 bis | con cola | 12:55:03 – 13:22:02 | 27,0 | 0 | 38.169 | 142.063 | `1bd5ffcd…` | `c2af74d4` | `411984d6` |
| 5 bis | sin cola | 12:55:16 – 13:20:45 | 25,5 | 0 | 37.168 | 128.552 | `576c9725…` | `a83b9d9b` | `fa5983b3` |

(`mediciones/tiempos_corridas.json`, de las consolas de `corridas/`, con `scripts/doble_y_tiempos.py tiempos`; los sha256 enteros y los
bytes, en `mediciones/sha256_por_paso.txt`.) En los doce, la doble corrida interna da byte a byte, y la validación de los modelos r2,
0 nodos y 0 aristas fuera del modelo. La memoria máxima, entre 1,66 y 2,71 GB.

- **El paso 1 contra el sello:** los tres archivos del despacho dan el sha256 del sello, en los dos grafos; `diff -rq` contra el
  ensamblado del repo da distintos solo `reporte_ensamblado_r2.json` (y solo en el repo, `kg.json.gz` y su sello, que la cadena no
  escribe); el reporte, con las rutas de su salida y de la raíz normalizadas (`scripts/reporte_normalizado.py`), da igual.

## 6. Las mediciones, paso por paso (`scripts/medir_paso.py`, sha256 `6d294c91…`; `mediciones/paso<n>/<grafo>/`)

Cada paso contra el anterior, en los dos grafos: nodos por tipo, aristas por predicado, la tabla de ids del paso, las triplas de cada
predicado con la tabla aplicada, los nodos que cambian por tipo y campo, las aristas de tripla igual con otros atributos, el
aislamiento, las `remite_a` que cambian (una por una, por código, con su causa: `remite_a_que_cambian.json`), lo propio de la pieza y el
cegamiento. La suite y las shapes, con `scripts/gate_ureapl.py` (shapes con la E0 del grafo y con la E0 con las partes por corte, que
rige para S30 y S31; la suite con los argumentos de `gate_tf.sh` y, desde el paso 3, el catálogo de la suite de G y
`--generados-resolucion G`) y `scripts/comparar_gates.py` (`mediciones/gates_por_paso.json`, `36a00987…`). La E0 con las partes la
rearmé en la copia con `reext_t0/t3/e0_con_partes.py` sin cambios, dos veces: 640 archivos iguales, conjunto `8c2471dd…`, el sellado
en `tanda_final/t3/gate_decisiones/e0_partes_tf.json`.

**La suite y las shapes, en los cinco pasos y los dos grafos:** shapes con la E0 del grafo, NO PASA solo por S31 (como el sello); con la
E0 con partes, PASA. La suite, 68 ítems: 46 resueltos, 13 persisten, 9 no aplicables, en todos. La regresión contra la entrada del sello
en la fixture (`computar_regresion`, el método del registro, §62 y §75, porque la suite solo la computa sola cuando el sha256 del grafo
es el de una entrada): 5 en todos los pasos, E4-a1, E4-a4, RT-C5-3, RT-C6-1 y RT-C6-2, las del sello (T3). Ningún ítem cambia de estado
de un paso a otro, ninguna regla cambia de resultado (bloqueante o informativa) y no aparece ninguna regresión nueva. El paso 1 da el
gate sellado de T3 regla por regla (con la E0 del grafo) e ítem por ítem.

### 6.1 Paso 2: D (`--procedencia-heredada`)

| | con cola | sin cola |
|---|---:|---:|
| C1 de procedencia (procedencias), tanda 0 / 1 / final | 115 (31 / 40 / 44) | 99 (28 / 34 / 37) |
| C2 (procedencias), tanda 0 / 1 / final | 236 (76 / 75 / 85) | 210 (65 / 69 / 76) |
| uniones evitadas, tanda 0 / 1 / final | 19 (7 / 5 / 7) | 14 (4 / 5 / 5) |
| C1 sin las otras dos (no ubicado / compuesto en texto propio / texto propio / cruza título y párrafo / párrafo) | 2.135 (1.201 / 690 / 217 / 26 / 1) | 2.031 (1.128 / 675 / 205 / 22 / 1) |
| nodos renombrados (tabla de D: par único por tipo, label y chunk_id) | 115, todos con procedencia de C1 | 99, todos con procedencia de C1 |
| `remite_a` que entran / salen | 196 / 123 | 157 / 119 |

- **Las uniones evitadas:** las de las tandas 0 y 1 son las 12 del mandato con cola (7 y 5) y las 9 sin cola (4 y 5) (precisión 3 de la
  firma); las de la tanda final, 7 con cola y 5 sin cola, las mide este paso y se declaran igual. Causa: `nodo_existente` (14 sin cola;
  16 con cola) y `c1_en_otra_entidad` (3, con cola). Por unidad, código y punto: `d_uniones_evitadas.json`.
- **Cada procedencia que tocó C1,** con la unidad, el código del nodo, el punto y el rol de antes y de después: `d_c1_procedencias.json`
  (cada una con un solo nodo candidato).
- **Aislamiento:** OK en los dos grafos. Los nodos son los mismos con la tabla (0 sin par); los renombrados son todos de TIPOS_G_R; las
  triplas de todos los predicados salvo `remite_a` quedan iguales (`establecida_en` y `aplica_a` incluidas, como pide el registro, §49);
  cada `remite_a` que cambia tiene un extremo en un nodo de C1 (todas por el destino; una con cola, por los dos).
- **C2 marca todo tipo** (mandato de U-PROC-HERENCIA, §9, decisión 1): fuera de C1, 5 Comunicacion y 101 (sin cola) / 111 (con cola)
  entidades de TIPOS_G_R cambian solo por la marca `tramo_fuera_del_texto_de_e3`. Las aristas que cambian de atributos con la tripla
  igual (12 `establecida_en` y 265 / 328 `remite_a`) tienen un extremo en un nodo de C1 o, si no, cambian solo por la marca, que la
  arista copia de la procedencia de su nodo (5 y 229 sin cola; 5 y 254 con cola). Sin explicar: 0.
- **La suite y las shapes:** cambian solo los conteos de S1 a S5, S21, S30 y S31, por las 38 / 73 `remite_a` más; S21 sigue con 1.200 /
  1.342 incoherentes (sin cola / con cola) y S31, con la E0 plana, con las mismas 997 / 3.528 violaciones que el sello, en los cinco
  pasos (`gate_paquete/gate_paso<n>_<grafo>.json`).

### 6.2 Paso 3: las claves (`--catalogo-resolucion G`)

| | con cola | sin cola |
|---|---:|---:|
| relaciones de sujeto que cambian (de destino / solo de método) | 460 (455 / 5) | 453 (448 / 5) |
| de un veredicto que entra (47 de 47 con cambios) | 439 | 433 |
| Sujetos propuestos que salen (todos con un solo destino: la tabla de las claves) | 102 | 100 |
| Sujetos del catálogo que entran (las 35 altas, con su `subclase_de`) | 35 | 35 |
| `aplica_a` entran / salen; `ejecuta`; `padre_sugerido` salen; `subclase_de` entran | 192 / 193; 11 / 11; 67; 35 | 188 / 189; 11 / 11; 67; 35 |

- Por método: de cuarentena a R1 (label o alias), 222 / 220; de la sugerencia del modelo (R4) a R1, 210 / 206 (R1 le gana, como en
  U-RERESOL-CAT); de cuarentena a R2 (calificador, slug, singular), 28 / 27 (con cola / sin cola).
- **Por clave** (veredicto, su código, relaciones, de y a qué Sujeto por código): `claves_sujetos_re_resueltos_por_clave.json`.
- **Aislamiento:** OK. Solo Sujetos: los nodos tocados, los que salen y los que entran son Sujetos, y toda tripla que cambia tiene un
  extremo en un Sujeto de la pieza. Ninguna `remite_a` cambia.
- **La suite y las shapes:** cambian solo conteos (S1–S5, S19, S22, S23, S27, S28, S29, S6, S7): por ejemplo, S28 de 2.662 a 2.435 filas
  del registro sin cola; S19 con 145 ids de catálogo.

### 6.3 Lo que declaro de las claves, sin que sea caso de freno

Con los labels y alias nuevos, 20 relaciones sin cola (21 con cola) cuya clave no es la de un veredicto que entra se re-resuelven a un
Sujeto del catálogo: 3 de la clave del veredicto 99 («no entra», código `5ebf7389d6d1`) y 17 / 18 de 16 / 17 claves que no están entre
los 105 veredictos. Todas eran cuarentena y van por el calificador (19 / 20: la mención empieza con un label o alias nuevo y sigue con
texto) o por el slug del id (1), a 9 Sujetos. Las listo por el código de su clave en `claves_sujetos_re_resueltos_por_clave.json`
(`veredicto` nulo o 99). Tocan solo Sujetos, sin regresión ni cambio de shapes: no es un caso del §5, pero es un efecto de las claves que
la lectura no vio.

### 6.4 Paso 4: C1 (`--union-comunicaciones`)

- 32 códigos se unen, con 120 nodos; −88 Comunicacion en los dos grafos (482 → 394 con cola, 472 → 384 sin cola). Las listas: 0 códigos
  y 0 nodos (las dos, vacías; el resumen del ensamblado da sus sha256, `aa6aa007…` y `37517e5f…`), así que ninguna colisión queda sin
  unir por decisión de la autora.
- **Las uniones contra el censo** (`scripts/censo_c1_pasos.py --uniones`): las 32 uniones son las 32 colisiones del censo, código por
  código y nodo por nodo, en los dos grafos. Por código (sha256[:12] del código normalizado, documentos y códigos de nodos):
  `c1_uniones_por_codigo.json`.
- **Aislamiento:** OK. Solo Comunicacion (32 nodos cambian, por las procedencias que suman; 88 salen, todos con par en la tabla). Ninguna
  tripla cambia con la tabla aplicada: se re-apuntan 81 `referencia` y no se junta ninguna arista.
- **La suite y las shapes:** cambian solo los conteos de nodos (S4, S5, S7, S25, S26).

### 6.5 Paso 5: las remisiones (`--remisiones-a-subpuntos`)

- **Solo se agregan `remite_a`:** 24.301 sin cola y 27.133 con cola; ninguna sale, ningún otro predicado cambia, ningún nodo cambia y
  ninguna arista existente cambia de atributos. Toda arista nueva sale de una cita con destino B del registro, y toda cita B era
  `punto_sin_nodos` en el paso 4 (0 y 0).
- **Las que D ya cambió en el paso 2** (llevadas al paso 4 con las tablas de las claves y de C1): ninguna arista nueva es una de ellas
  (0 en los dos grafos), así que ninguna cambia por las dos piezas. Aparte: 243 nuevas sin cola y 358 con cola tienen un extremo en un
  nodo de C1 de D.
- **Aislamiento:** OK en los dos grafos.
- **La suite y las shapes:** S21 sube exactamente en las `remite_a` nuevas (de 1.200 a 25.501 sin cola, +24.301; de 1.342 a 28.475 con
  cola, +27.133), la subida por construcción que declaró el registro para la opción B (la regla 1.5 deja como destino la unidad citada).
  S30 y S31, con la E0 con partes, siguen en PASS con todas las `remite_a` en un tramo; con la E0 plana, S31 sigue con las mismas 997
  violaciones sin cola y 3.528 con cola. Los demás, solo conteos.

## 7. Las cuentas de las remisiones y la diferencia, explicada

(`mediciones/paso5/<grafo>/medicion.json`, `scripts/explicar_remisiones.py`, `mediciones/explicacion_remisiones_{con,sin}_cola.json`.)

- **El resumen del ensamblado del paso 5:** con cola, 783 citas que resuelve, 27.133 `remite_a` nuevas, 432 pares que ya existían y 0 a
  una unidad excluida; sin cola, 765, 24.301, 414 y 117.
- **Contra el acumulado de las tandas 0 y 1,** corrí la cadena con el código de HEAD sobre ese acumulado (su entrada, rearmada en la copia
  con `tanda1/t3/scripts/armar_acumulado_t3.py`, da su `armado_acumulado_t3.json` byte a byte, y la E0 y el manifiesto, iguales a los del
  repo), con `scripts/cadena_t3_ureapl.sh` (el `cadena_t3.sh` de la tanda 1 con el mismo agregado), de 13:22:54 a 13:33:32, rc 0 en los
  cuatro (`corridas/lote_explicacion_30*`):
  - con D y B: **368 citas y 14.133 nuevas con cola; 366 y 13.940 sin cola**, las cuentas del registro con D (§62). Sin D, la etapa a
    midió 14.047 y 13.854 (con D-3), y la firma, 14.049 y 13.856 (sin D-3);
  - con las cuatro piezas: lo mismo (las claves y C1 no mueven B en ese acumulado).
- **Sobre las tres tandas, por tanda del origen y del destino** (la tanda de cada TO, de los manifiestos de extracción):

| celda | citas con cola | nuevas con cola | citas sin cola | nuevas sin cola |
|---|---:|---:|---:|---:|
| tandas 0 y 1 → tandas 0 y 1 | 371 | 14.136 | 368 | 13.942 |
| tandas 0 y 1 → tanda final | 42 | 1.088 | 42 | 1.008 |
| tanda final → cualquiera | 370 | 11.909 | 355 | 9.351 |
| total | 783 | 27.133 | 765 | 24.301 |

- **La celda de las tandas 0 y 1, cita por cita:** tiene las 368 / 366 citas del acumulado de las tandas 0 y 1, cada una con los mismos
  pares, más 3 con cola y 2 sin cola, de 1 arista cada una: de ahí los +3 y +2 sobre 14.133 y 13.940. Esas citas nombran una norma; en
  el acumulado de las tandas 0 y 1 quedaban como «norma fuera del inventario», y con las tres tandas el detector la reconoce
  (`via_norma`) como un TO de la tanda 1 cuyo punto citado no tiene nodos, que B resuelve. Por código: `fda146f7b500` (solo con cola),
  `cced0b06b555` y `28d44ecb80d3`.
- **El resto de la diferencia** es la tanda final: 42 citas de las tandas 0 y 1 a un TO de la tanda final (que en el acumulado de las
  tandas 0 y 1 no estaba) y 370 / 355 citas desde la tanda final.
- Mi cuenta de citas con la procedencia entera en la clave da 787 / 769: 4 más, porque el detector las cuenta por chunk_id, evidencia y
  destino (`r1_referencias.py:1397`); uso la suya.

### 7.1 Los hubs, con la regla de la familia 5

`familias_nav.py` del 142 no está en el repo: reimplementé la regla (grado, entrantes más salientes, en el 1 % más alto del grafo
servido: el umbral es el grado del nodo en el puesto ⌈1 % de los nodos⌉, y hub es grado ≥ umbral, `medir_paso.hubs`) y la calibré contra
el registro, §62: sobre el acumulado sellado de las tandas 0 y 1 da 38 y 216 sin cola, y 42 y 226 con cola, las cifras registradas.

| | umbral (paso 4 → 5) | hubs | entran | salen | entran solo como origen de las nuevas | entran como destino |
|---|---|---|---:|---:|---:|---:|
| con cola | 52 → 61 | 382 → 383 | 69 | 68 | 34 | 35 |
| sin cola | 40 → 51 | 384 → 376 | 118 | 126 | 57 | 61 |

Por tipo: `hubs` en `mediciones/paso5/<grafo>/medicion.json` (entran sobre todo Obligacion, Operacion y Condicion; salen también
Sujeto y TextoOrdenado). Con C1 (paso 4 contra 3), el umbral sin cola queda en 40 y con cola pasa de 51 a 52. N6 se midió sin estas
`remite_a` (D-5 de las remisiones).

## 8. El censo de C1 (`scripts/censo_c1_pasos.py`; `mediciones/censo_c1/censo_c1_pasos.json`, `3bbc2f14…`)

- Con `cuenta_C` y `codigo_normalizado` de `med_desamb/parte2/tamanos_desamb_mesa.py` y `e2_lib` de la copia (el código de HEAD), y la
  regla de la muestra del script del censo de la mesa, en memoria.
- **El sello sin cola da las cuentas de `conteos_acumulado_tres_tandas_sin_cola.json`, campo por campo:** 472 Comunicacion, 32
  colisiones, 120 nodos en colisiones, 32 con 2 nodos o más, hasta 25 documentos y 25 nodos por colisión, 0 que tocan la muestra, 0 que
  no se pueden decidir, 0 nodos que no se unen por la muestra y 32 para leer. Con cola: 482 Comunicacion, 32 colisiones y 120 nodos.
- **Las colisiones del paso 2 son las del paso 1** (código y nodos), en los dos grafos.

## 9. Las tablas de ids y el grafo evaluado

- **Las tablas de cada pieza, por grafo** (`mediciones/paso<n>/<grafo>/tabla_ids_<pieza>_por_codigo.json`, código viejo → código nuevo, y
  `NO_ABRIR_tabla_ids_<pieza>.json` con los ids): D, 115 / 99 pares; las claves, 102 / 100 (el propuesto → el Sujeto del catálogo); C1,
  88 / 88 (la Comunicacion → el nodo de su código).
- **La tabla compuesta** (`scripts/tablas_compuestas.py`), id del sello → id del grafo evaluado con la pieza: con cola 305 filas (D 115,
  claves 102, C1 88), sin cola 287 (99, 100, 88); ningún id del sello queda sin nodo en el evaluado. Los ids, solo en
  `NO_ABRIR_tabla_ids_compuesta_{con,sin}_cola.json` (sha256 `e2ec497f…` y `39bae006…`); por código, `tabla_ids_compuesta_*_por_codigo.json`.
  En las listas por código, el nodo con alguna procedencia en una unidad de la muestra va como «cegado» (2 filas por grafo en la
  compuesta y en la de las claves; los ids, solo en los `NO_ABRIR_`).
- **Las dos listas del censo, reexpresadas con la tabla compuesta:** la de los códigos que no se unen y la de los nodos que no se unen
  estaban vacías y quedan vacías.
- **El grafo evaluado** es el del paso 5, el último que entra (precisión 4 de la firma). Sus dos armadas (`ureapl/paso5/` y
  `ureapl/paso5_bis/`, en `copia_repo/`) dan los 274 archivos de `r2/` byte a byte iguales, salvo el reporte, igual con las rutas
  normalizadas (`scripts/doble_y_tiempos.py doble`; `mediciones/doble_evaluado_*.json`):
  - **con cola** (`KG-Acumulado-Tandas0y1yFinal-r2b`): `kg.json` `1bd5ffcdada9688873b06c0efe8d03b4a39bde15ce10fb66993d1f4219fb7ce6`,
    266.179.134 bytes, 38.169 nodos y 142.063 aristas;
  - **sin cola** (`-sincola`, el evaluado): `kg.json` `576c97256185a0d5741cb2c35a2a85e91412f3e1119ad7a85d960b7d60c35ad3`, 238.061.282
    bytes, 37.168 nodos y 128.552 aristas.
- **Lo que queda fuera de la carpeta temporal del sistema, en `fuera_del_repo/reaplicacion_unica/copia_repo/`:** los doce ensamblados de los pasos
  (`ureapl/paso{1..5,5_bis}/`), la entrada del acumulado (`data/experiment/tanda_final/t3/acumulado/entrada_acumulado_128_r2b/`, 2.295
  archivos, lista `e19d926a…`), G (`ureapl/claves/`), las dos listas de C1 (`ureapl/c1/`), la E0 con partes (`ureapl/e0_con_partes/`) y
  las cuatro corridas de la explicación (`ureapl/t30_*`). Lo que va al repo (los dos grafos evaluados, su sello y sus tablas) lo
  commitea la autora: no escribí nada en el repo.
- **Las 78 rutas** (pre-registro de la tanda final, §8): las re-sellé con su script, `data/experiment/controles_tanda1/sellar_codigo_de_la_cadena_mesa.py`
  (lee el repo solo con `git show` y `git ls-tree`), sobre HEAD `2db79462`: `rutas78/codigo_de_la_cadena_HEAD_2db79462_ureapl.json`,
  **sha256 `cfed608d727a78a1035170098886d3030ecd1db9711ffadef4f6e33d31edbdca`**, el que va al sello del grafo evaluado. Son las mismas 78
  rutas de la lista sellada (`codigo_de_la_cadena_c66c7ecd_mesa.json`, `40de829c…`), con los mismos grupos; cambian de sha256 cuatro:
  `r1_invariantes.py`, `r1_referencias.py` y `ensamblar_tanda0.py` (el 163) y `scripts/regression_kg_esperado.json`, que cambió en el
  commit del T3 de la tanda final (`71cb9305`, el registro de sus grafos en la fixture). Declaro esta última porque no la nombra el
  mandato.

## 10. El cegamiento (mandato, §7; §7 bis de U-PROC-HERENCIA)

- La muestra de las FICHAS vive solo en memoria (`scripts/muestra_memoria.py`): el orden del sorteo (el único `NO_ABRIR_` que abrí, con
  su sha256 controlado), la lista de exclusión del despacho (los ids de `unidades_a_la_vista_T4.json` en `0c2befad`, `5ec9753d…`, leído
  con `git show`, más las 7 unidades) y las 30 primeras que no están en ella, con `ids_en` y `listas_de_ids` tomadas de la fuente del
  script del censo de la mesa. No la escribí ni la imprimí, y no doy su tamaño ni sus ids.
- **Un nodo de una unidad de la muestra que una pieza renombra sigue cegado con su id nuevo:** sí, en las tres tablas y en la compuesta,
  en los dos grafos. D no renombra ningún nodo de una unidad de la muestra.
- **Casos en espera:** no. Ninguna procedencia de C1 ni ninguna unión evitada es de una unidad de la muestra.
- **Las listas:** las `remite_a` con un extremo en un nodo con alguna procedencia en la muestra no se listan (106 por grafo en el paso 5);
  en las demás listas por código, ese nodo va como «cegado».
- **El control sobre las salidas** (`scripts/control_cegamiento_salidas.py`, sobre los archivos del paquete sin los `NO_ABRIR_`): dos grupos, con los cuatro grafos (el sello y el evaluado, con
  y sin cola) y la muestra en memoria:
  - **el paquete sin el material de las claves** (128 archivos): 0 unidades de la muestra, 0 códigos de nodos con alguna procedencia
    en la muestra, 0 ids de nodos de una extracción y 0 labels de 25 caracteres o más;
  - **el material de las claves** (la lista de ampliaciones, G en sus dos variantes y las dos consolas de `componer`; 25 archivos): 0
    unidades de la muestra y 0 códigos de nodos cegados. Sus labels y alias coinciden con labels de nodos (Sujetos propuestos, y
    labels del catálogo del request que también son de nodos): es el catálogo de resolución, armado desde las formas del material, que el
    despacho manda al paquete; la evidencia lleva unidades del material, ninguna de la muestra.
- La consola llevó solo cuentas y sha256, salvo lo que la autora pidió ver de las claves (las dos claves y sus códigos del §4), que
  son del catálogo. Nada por estado de E3 ni de los reintentos.

## 11. Los criterios de aceptación

1. Paso 0, copia sin `.env`, `NO_ABRIR_` ni enlaces, y la foto igual al principio y al final: **cumple** (§1, §2).
2. R19 en rc 0 con las bases iguales y los tres selftests en PASS: **cumple** (§3).
3. El paso 1 da el sello byte a byte, con y sin cola: **cumple** (§5).
4. En cada paso, cada pieza toca solo lo suyo: **cumple**, sin casos de freno (§6).
5. Las cuentas de las remisiones, con la diferencia explicada, y las del censo de C1: **cumple** (§7, §8).
6. El grafo evaluado, con y sin cola, armado dos veces, byte a byte igual, con su sha256: **cumple** (§9).
7. Ninguna salida trae contenido de nodos ni una unidad de la muestra: **cumple** (§10).

## 12. Mis errores, con su causa

1. **Dos carpetas sin crear:** la primera corrida del gate de los pasos 1 y 2 y la primera medición del paso 2 dieron rc 1 porque
   redirigí sus consolas a una carpeta que no existía; no escribieron nada. Las creé y las corrí de nuevo.
2. **El script de medición, corregido mientras medía:** la primera versión contaba como «sin explicar» las aristas que solo copian la
   marca C2 de su nodo, comparaba un propuesto con el Sujeto del catálogo al que se une como si fuera el mismo nodo, rotulaba las
   `remite_a` de B como «sin extremo de la pieza» y contaba las citas B con otra clave que el detector. Ninguna cambió una corrida de la
   cadena; todas las mediciones del FRENO salen de la versión final (`6d294c91…`), corrida de nuevo para los cuatro pasos.
3. **Contenido en una salida antes de empacar:** los resúmenes de las shapes (S18, S20, S24 y S25 listan ids o labels) y 20 códigos de
   Sujetos con alguna procedencia en la muestra estaban en salidas de mi carpeta de trabajo; los encontró el control del cegamiento antes
   de armar el paquete. Al paquete van los resúmenes del gate sin esos textos (`scripts/gate_sin_resumenes.py`: las listas, por su
   cantidad y su sha256) y esos códigos como «cegado». Las salidas crudas del gate y de la suite quedan fuera del paquete.
4. **Dos `cd` en la sesión** cambiaron su carpeta de trabajo por un momento (a la copia); no escribí nada por eso y volví.
5. **Una hora mal puesta en el checkpoint** del scratchpad («12:05» para lo que terminó a las 11:57); no está en ninguna salida.

## 13. El grep de convenciones (`LC_ALL=en_US.UTF-8`)

Con `tanda_final/t3/scripts/grep_convenciones_tf.py` (el del T3, sin cambios: los tokens del nombre de la cuenta, en memoria; su lista
de términos de origen conversacional; las rutas absolutas) sobre el paquete entero, sin los `NO_ABRIR_`
(`ureapl_controles__grep_convenciones.json`): 154 archivos de texto (0 binarios), 0 renglones con un token del nombre o un término, 0 tokens fuera o dentro de rutas absolutas y 0 archivos con rutas absolutas. El control positivo da 2.
- Antes de esta versión, el grep encontró 3 renglones con tokens del nombre en cada foto del repo (rutas de archivos del repo) y una
  mención de la carpeta temporal del sistema en este FRENO, y después dos renglones de esta sección que citaban la lista de términos:
  las fotos enteras quedaron fuera del paquete (va su resumen) y reescribí esas frases.
- Revisé además todo lo que escribí buscando nombres propios de personas y referencias al origen conversacional de una decisión: no hay.
  La autora y la mesa van por su rol.

## 14. El paquete y su copia

- **El paquete:** `revision_UREAPL/` en el scratchpad de esta sesión (`3c31470d-2025-4b0b-9d08-45974d2970a2`), armado con
  `scripts/armar_paquete.py` desde una lista (origen, nombre único, descripción): 161 archivos más `manifest.txt` (su sha256 no va acá, porque
  este FRENO está en él). Cada línea del manifest lleva el sha256, el nombre y una descripción; los 8 `NO_ABRIR_` (las tablas de ids
  con los ids tal cual: las de cada pieza y las dos compuestas) van solo con su sha256 y su nombre.
- **Su copia permanente:** `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/3c31470d-2025-4b0b-9d08-45974d2970a2/scratchpad/revision_UREAPL/`,
  con `ditto`; en la copia recalculé el sha256 de cada archivo del `manifest.txt`: 161 de 161 iguales, y el `manifest.txt` de la copia es
  byte a byte el del scratchpad.
- **Fuera del paquete, en la carpeta de trabajo:** los grafos y la entrada (§9), las salidas crudas del gate y de la suite (`gate/`),
  las tablas de trabajo con ids (`trabajo/`), las fotos enteras (`controles/`) y la copia del repo (`copia_repo/`, 9,4 GB más lo que
  escribieron las corridas). Nada de eso está en el repo.

FRENO: espero la revisión de la mesa.
