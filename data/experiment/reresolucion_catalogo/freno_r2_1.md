# U-RERESOL-CAT — FRENO R2-1: script, prueba, medición de la enmienda 6 y lectura de la parte B (06/10/2026)

Mandato: `docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md`, texto firmado leído en `f87ec4a` (105 líneas, sha256
`c8ee13822dfc…`, igual a las primeras 105 líneas del archivo actual) y sus notas (`0a3ac81`); «seguí» de R2 despachado
el 06/10/2026 en dos pasos. Precondición: HEAD `01046b6` (SC1-bis de U-SINCOLA-T0) y `git diff --stat 01046b6 HEAD --
data/experiment/tanda0/code/ensamblar_tanda0.py` vacío al empezar. Fuentes en BORRADOR leídas en su último commit: enmienda 6
a L-ESQ-R2 (`0583e7f`), enmienda 4 al protocolo (`2c77050`). USD 0; sin API ni Neo4j.

Todo corrió sobre una copia del repo sin enlaces (`rsync --no-links`, 0 enlaces, 0 `.pyc`; sin `.git`, `.venv`,
`data/raw`, `docs/literatura`, `neo4j/volumen`, `segmentacion_oficial_e0r2` ni `comp_e1`). Cada cifra lleva su clave en
`salidas/` (§8). Error propio, corregido antes de leer: la primera corrida de `r2_1_medicion.py` tomó el orden de los TOs
fuera de las redirecciones (los cinco de desarrollo) y armó la población de la parte B sobre esos cinco; la descarté sin
abrir sus fichas y la rehíce con el orden del manifiesto (la semilla estaba fijada antes de las dos). Otro, en los
controles: la primera fase de la suite con el código de HEAD corrió con los argumentos en otro orden y no ejecutó nada;
la relancé.

## 0. Diferencias entre el despacho y los archivos, y decisiones de la autora en la sesión (regla d)

1. **Las candidatas de la prueba.** En el registro de KG-Tanda0-Diez-r2b ninguna de las dos está en cuarentena con la
   mención verificada: «el cuentacorrentista» tiene 10 filas en cuarentena, las 10 con la mención no verificada, y
   «integrantes de la Alta Gerencia» no tiene filas (sus 2 relaciones con la mención verificada las resolvió el modelo a
   `Sujeto_alta_gerencia`). Lo reporté antes de elegir. **Decisión de la autora (06/10/2026):** se mantienen T1 y T2 y se
   suman, con el criterio del mandato (cuarentena, mención verificada, `sin_match`), T3, id nuevo «entidad encargada del
   seguimiento», y T4, alias «empresas no financieras emisoras de tarjetas locales» de
   `Sujeto_empresa_no_financiera_emisora_de_tarjetas`.
2. **W1 a W3 y SC2.** La nota del 06/10 al pie del mandato pone las tres escrituras «después de U-SINCOLA-T0»; el
   despacho corre R2-1 en paralelo con SC2. **Decisión de la autora (06/10/2026):** se desarrollan y verifican en la
   copia y se aplican al repo solo con SC2 commiteado (git log de `data/experiment/sincola_t0/` y git status limpio de la
   fixture, `grafos.py` y `sincola_t0/`); si no, van como parches al paquete. Estado al cierre en §9.
3. **La población de la parte B** está definida en la enmienda 6, §B.2, sobre KG-Tanda0-Diez-r2b. El grafo evaluado de
   la tanda 0 es el sin cola: seguí el texto de la enmienda y declaro la cola (71 de 1.592 en la población; 2 de 30 en la
   muestra).
4. `selftest_catalogo_unico.py` lee un commit con `git show`; la copia no tiene `.git`. Lo corrí en la copia con
   `GIT_DIR` apuntando al `.git` del repo, solo lectura, con el código de HEAD y con el nuevo.

## 1. Escrituras (W1 a W3: desarrolladas en la copia; ver §9)

- **W1**, `data/experiment/tanda0/code/ensamblar_tanda0.py` (+39/−11): parámetro opcional `cat_resolucion` en
  `correr_cadena_r2` y `ensamblar_manifiesto_r2`, que reemplaza al catálogo del request en E4, en E2 (labels y conjunto de
  ids), en la normalización de los propuestos y en las redirecciones (esqueleto y `INV.SUJETOS_CATALOGO_SET`); función
  `sujetos_de_resolucion` (sin el catálogo de resolución devuelve `M.SUJETOS_R2_SET`, el mismo objeto); el resumen y el
  reporte llevan las tres versiones solo con el parámetro; opción `--catalogo-resolucion <dir>`, solo de la cadena r2.
  Convive con `con_cola` en las mismas firmas.
- **W2**, `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py` (+70/−3): (a) `reresolver_registro` escribe el método como
  la cadena (`R1_` y `R2_` con sus criterios; el calificador y R3 con el nombre de la regla); (b)
  `catalogo_resolucion_r2(dir)`, junto a `catalogo_r2()`, con su candado: el manifiesto deriva del sha del catálogo del
  request de `modelos_r2`; la lista de ampliaciones, el compuesto y cada generado dan el sha del manifiesto; los ids del
  request están todos.
- **W3**, `scripts/regression_kg.py` (+29/−7): opción `--generados-resolucion <dir>`; con ella, LN-6 toma índice,
  `rol_por_to` y sha del catálogo de resolución por el cargador de W2; sin ella, las rutas fijas y la salida de siempre
  (el parámetro solo se escribe con la opción).
- En `data/experiment/reresolucion_catalogo/`: `reresolver_catalogo.py`, `selftest_reresolver_catalogo.py`,
  `r2_1_medicion.py`, `r2_1_fichas.py`, `r2_1_resumen_controles.py`, `controles_r2_1.sh`,
  `procedimiento_crecimiento_catalogo.md`, este freno y `salidas/` (§8).

## 2. El script y su selftest

`reresolver_catalogo.py componer` arma el catálogo de resolución (request más ampliaciones que solo agregan: alta de id
con su padre, alta de alias) y escribe sus generados con el manifiesto; frena ante una expresión colectiva, un label o
alias que ya existe, un id existente o un padre que no es clase. `correr` hace (a), (a+) y (b) por el camino del
ensamblador (W1), contrasta, escribe el registro acumulado y corre shapes, suite y LN-6 sobre la salida y la anterior.
Los tres huecos del freno R1:
- **Registro acumulativo:** el anterior actualizado por (a) y (a+), con el `id_nodo` de (b) en lo que sigue en cuarentena,
  más las filas de (b) que el anterior no tiene; `catalogo_sha256` es la versión de entrada y no cambia,
  `catalogo_sha256_resolucion` la de resolución. Reemplaza al de la cadena en `r2/no_mapeados_sujetos.jsonl`; el de la
  cadena queda en `no_mapeados_sujetos_cadena.jsonl`. Tres controles (sin resolver = (b) salvo la versión; destino de cada
  resuelta = (b); filas de (b) fuera del anterior, listadas).
- **Un solo nombre de método:** W2 (a).
- **(a+):** la regla de decisión re-aplicada a toda relación de `resolucion_sujetos.jsonl`; control: reproduce la decisión
  guardada (2.622 de 2.622 en diez); lista lo que cambia por tipo (destino, método, calificador, desacuerdo).

`selftest_reresolver_catalogo.py`: 51/51, en nueve grupos sintéticos (S1 componer, S2 generados y candado, S3 método,
S4 decisión, S5 (a+), S6 registro acumulado, S7 contraste, S8 W1 en las redirecciones y en E2, S9 W3), importando el
script por su propio camino de imports.

## 3. Controles (mandato R2.3; decisiones 3 y 4 del despacho) — `salidas/r2_1_controles.json`

- **Cadenas por la línea de comando, código nuevo, sin `--catalogo-resolucion`** (`cadenas_sin_parametro`): r2a diez
  `70d51e42…` y desarrollo `fa4c1043…`, los del cierre de C2 (los sellados `99fe2bfa…` y `93a7af72…` se citan con
  `f8dedd4`, decisión e de la tercera nota); r2b diez `a9631a64…` y desarrollo `6e756043…`; sin cola, con `--sin-cola`,
  `e22fae1a…` y `2922b72d…`. En los cuatro r2b, los archivos de `r2/` son byte a byte los sellados (33 y 23) salvo el
  reporte del ensamblador (rutas y las dos claves de SC1-bis); `declaracion_partes_y_reparadas.json` no lo escribe el
  ensamblador.
- **Línea de comando con `--catalogo-resolucion` y el catálogo sin ampliaciones** (`cli_con_catalogo_sin_ampliaciones`):
  r2b diez `a9631a64…` y, con `--sin-cola`, `e22fae1a…`; 33 archivos iguales; el reporte lleva las tres versiones
  (compuesto = request, `c3ad1581…`). W1 convive con `con_cola`.
- **Suite sobre las seis entradas selladas** (diez y desarrollo; r2a, r2b y sin cola), código de HEAD contra el nuevo sin
  la opción: `.json` y `.md` byte a byte iguales en las seis (`suite_head_contra_nuevo`).
- **Selftests**, HEAD y nuevo: `selftest_r3` 116/116, `selftest_regression_kg` 184/184, `selftest_prompt_r2b` 55 sin
  fallas, `selftest_catalogo_unico` 60/60; la salida difiere solo en el orden en que se imprimen dos conjuntos.
  `selftest_reresolver_catalogo` 51/51 (`selftests`).
- **El script con el catálogo sin ampliaciones** (`corridas_del_script.vacia_*`), sobre los cuatro sellados: grafo,
  registro acumulado y resolución byte a byte iguales al anterior (diez, desarrollo y los dos sin cola); 0 sin explicar;
  shapes PASA; LN-6 resuelto; suite sin cambios de estado.
- **Doble corrida de la prueba, en dos directorios** (`doble_corrida_prueba`): diez, 38 archivos iguales y 4 iguales con
  la ruta de salida normalizada (los reportes del ensamblador y del gate); desarrollo, 28 y 4; 0 distintos.
- **Cero relaciones rechazadas sin registro:** 0 rechazos de E2 en las ocho corridas del script, también con T1 a T4
  (S8d muestra el rechazo `sujeto_id_fuera_de_catalogo` sin el conjunto de resolución).

## 4. La prueba (punto 2): T1 a T4 sobre el crudo r2b — `salidas/r2_1_prueba_reporte_{diez,desarrollo}.json`

Catálogo de resolución de prueba `b9aced1f…` (4 ampliaciones), solo en el scratchpad; ninguna clave del índice pasa a
ambigua ni cambia de id (`r2_1_prueba_reporte_composicion.json`).

| | diez | desarrollo |
|---|---|---|
| (a) filas que resuelven | 15: 13 a T3 (R1 alias 6, R1 label 1, calificador 6) y 2 a T4 | 15, las mismas |
| (a+) relaciones del modelo que cambian de destino | 9 (3 a T1, 6 a T3) | 6 (a T3) |
| (a+) cambian de método, mismo destino | 7 (5 por T4, 2 por T2) | 5 (por T4) |
| (a+) cambia solo la marca de desacuerdo (calificador a T3, gana el modelo) | 14 | 14 |
| (b) grafo | `0ca3b825…` 8.809 / 27.625 (antes 8.816 / 27.632) | `107c9bce…` 6.983 / 23.438 (antes 6.990 / 23.445) |
| nodos | −9 propuestos, +2 ids nuevos (T1, T3) | −9, +2 |
| resolución de (b) = (a+), relación por relación | sí (2.622; todas con el sha `b9aced1f…`) | sí |
| rechazos de E2 | 0 | 0 |
| registro acumulado | 294 = 149 cuarentena + 128 a clase + 15 resueltas + 2 descartadas | 189 = 99 + 73 + 15 + 2 |
| sin explicar | 0 | 0 |
| gate | shapes PASA; LN-6 resuelto con `--generados-resolucion`; suite sin cambios de estado | ídem |

Las 10 filas de «el cuentacorrentista» en cuarentena (mención no verificada) no resuelven: el límite declarado se cumple.
Las 9 relaciones del modelo que cambian de destino, leídas (todas): las 3 de T1 (`ctacte::1.5.1.10`, `::2.2.2`,
`::6.4.6.1`) pasan de `Sujeto_banco` o `Sujeto_titular_de_cuenta_corriente_en_el_bcra` (cuentas en el BCRA, otro sujeto) a
T1: el texto nombra al cuentacorrentista del banco, y el destino nuevo es mejor; las 6 de T3 pasan del rol de alcance de
ext a T3: el texto nombra a «la entidad encargada del seguimiento», que es una entidad del rol, más precisa.
**Hallazgo:** las 6 filas que (a) resuelve por calificador quedan en estado `resuelto`; la cadena, para las mismas
relaciones, escribe `resuelto_a_clase` (`registro_acumulado.estado_distinto_de_b`). El destino coincide; el estado no. Se
corrige con una línea en `reresolver_registro` (fuera de W2: decide la autora).

## 5. Medición de la enmienda 6, §A.2, sobre el crudo r2b — `salidas/r2_1_medicion.json`

Control: la entrada de la cadena armada en memoria reproduce `resolucion_sujetos.jsonl` de KG-Tanda0-Diez-r2b (2.622 de
2.622). En la tanda 0 el único documento sin alcance es docvig: 17 relaciones de sujeto, las 17 con la mención
verificada (8 por el modelo, 7 por R1, 2 en cuarentena).

| Qué se mide (documentos sin alcance) | Pasan de la sugerencia del modelo a cuarentena | Ids que sugería el modelo |
|---|---|---|
| Regla 1, con la lista de hoy | 4 («las entidades») | `Sujeto_sujeto_regulado` (4) |
| Regla 1, con el singular y con «cada», «esta(s)», «dicha(s)» y «tal(es)» | 4 (las mismas) | ídem |
| Regla 2, relaciones sin mención | 0 | — |
| Regla 2, relaciones con una mención que no verifica | 0 | — |

- **Menciones que no verifican, en todos los documentos** (`no_verifican`): 257 (238 resueltas por el modelo, 19 en
  cuarentena). Expresión colectiva de la lista de hoy: 143; con el singular: 145. Nombran otra cosa: 112, con la lista en
  la salida; de ellas, 51 están en el texto de la unidad o en el heredado si se quita el artículo inicial: la verificación
  compara por tokens contra el texto propio más el heredado (`validador_r2.py:830`, `:1250`) y falla con «del» o «al»
  («el cuentacorrentista» contra «Obligaciones del cuentacorrentista», «el Comité de auditoría» contra «del Comité de
  auditoría»). Es el límite de A.4: la regla 2 trataría igual a esas 51 que a las 61 que el texto no trae.
- **En los documentos con alcance, si la lista de R3 se amplía** (`r3_ampliada`): con el singular, R3 alcanza 435
  relaciones («la entidad»); cambian 19 decisiones (cuarentena → R3; ext 14, cap 4, ctacte 1) y 15 marcas de desacuerdo
  (el modelo sugirió `Sujeto_entidad_financiera` donde el rol es otro: cap 8, ext 7); en 401 el modelo ya sugería el rol.
  Con los determinantes: 445, 20 decisiones, 15 marcas. Esas 19 son las filas de la clave «entidad», la más frecuente de
  la cuarentena (punto g del despacho).
- **Umbral** (`umbral`): en diez, 145 filas en cuarentena con la mención verificada, en 87 claves; 14 claves llegan a 2
  unidades y 5 a 3, todas de un solo TO salvo «entidad» (cap, ctacte, ext). Con la regla del colectivo (A.1.6), «entidad»
  no puede entrar como label ni alias. Sin la cola: 143 filas, 85 claves, las mismas 14 con 2 unidades o más.
- **Una relación sin mención en cuarentena** (A.4, segundo punto). Hoy E2 nombra el propuesto con la mención o, sin
  ella, con el id crudo (`e2_lib.py:959`); sin las dos, el label queda vacío y el nodo sería `Sujeto_propuesto_` (no pasa
  en r2b: 0 filas `sin_mencion`). Propongo una fila del registro sin nodo y sin arista (la norma queda sin `aplica_a`,
  como cuando el modelo no emite la relación), con LN-5 y S28 contándola aparte; un nodo por documento sería un sujeto
  sin nombre en el grafo. Toca `e2_lib.py`, LN-5 y S28: fuera de las escrituras aprobadas.

## 6. Parte B (§B.2): población, caso abierto y lectura — FRENO para la adjudicación

Población por simulación (`parte_b`): de 3.603 normas de unidades aceptadas en los nueve documentos con alcance, **1.592**
no tienen `aplica_a` con la mención verificada: 1.362 sin ninguna `aplica_a` y 230 con una cuya mención no verifica; 0 con
una relación sin mención (el prefijo de P3c la pide siempre); 29 con una sugerencia distinta del rol; 71 en la cola. Por
TO: cap 628, ext 353, ctacte 256, cla 126, ric 106, pro 43, polcre 36, lingob 26, pagjub 18.

**Caso abierto** (norma con una `aplica_a` con la mención verificada y otra sin mención o que no verifica): 5 (lingob 4,
ext 1), y en las 5 la segunda va a otro destino. En lingob es el co-sujeto «el Comité de auditoría» de «el Directorio, a
través de la intervención del Comité de auditoría y la Alta Gerencia» (no verifica por el «del»); en ext, «entidades
cambiarias», que el texto no trae. **Propuesta:** la norma no recibe la derivada (ya tiene sujeto) y la segunda relación
sigue como hoy (R4), con su marca de mención; ni cuarentena ni rol, porque nombra a un co-sujeto.

**Muestra:** 30, semilla 20261006 fijada en `r2_1_medicion.py` antes de sortear y de leer; 25 sin `aplica_a` y 5 con
mención que no verifica; 2 en la cola. **Mi lectura** (asistida y declarada; criterio en las fichas): **18 correctas, 5
incorrectas, 7 dudosas.** Las incorrectas ponen la norma en otro sujeto que el texto nombra: el exportador (F20, F21, F24),
el originante o fiduciario (F09) y el cuentacorrentista (F25). Las dudosas son impersonales o condiciones de una operación
que verifica la entidad (F10, F11, F19, F22, F23, F27) y una del órgano Alta Gerencia (F28). De las 5 con mención que no
verifica: 2 correctas, 2 incorrectas, 1 dudosa; en las 2 incorrectas, la mención del modelo nombraba al sujeto correcto
(«los exportadores», «el cuentacorrentista») y la derivada la reemplazaría por el rol.
- Wilson al 95 % con 18 de 30: 0,423. Aun con las 7 dudosas adjudicadas correctas, 25 de 30: 0,664. El piso (28 de 30)
  pide a lo sumo 2 incorrectas: **con mi lectura, la parte B no llega**, salvo que la adjudicación revierta al menos 3 de
  las 5 incorrectas además de las 7 dudosas.
- Fichas completas (texto de la unidad, heredado, rol, relaciones del modelo y lectura): `salidas/r2_1_fichas_parte_b.md`.
  **La adjudicación es de la autora** (campo «Adjudicación de la autora: PENDIENTE» en cada ficha).
- Si la parte B rigiera, dónde va (B.5): una función en `ensamblar_tanda0.py`, después de `resolver_relaciones_r2` y antes
  de E2, que agrega a la entrada la relación derivada por norma, con su marca en `rol_fuente` y `metodo_resolucion`
  propios; exige ampliar el enum de `rol_fuente` en `modelos_r2.py` (con su candado y G9 de `selftest_pyd_r2`) y mueve S11
  y la suite. Lo aprueba la autora en el «seguí» de R2-2.

## 7. Para R2-2 (sin implementar)

1. Parte A, regla 1, y el crecimiento del alcance: con la regla, la fila guarda la sugerencia del modelo. Si el
   documento recibe alcance, A.1.5 dice que `reresolver_registro` la resuelve por R3; la cadena, ya con alcance, haría ganar
   la sugerencia del modelo (R4 va antes que R3). (a) y (b) darían destinos distintos, y el control de §2 lo marcaría.
   Hay que decidir cuál vale.
2. El estado de las filas resueltas por calificador (§4).
3. La fila sin mención en cuarentena (§5).

## 8. Salidas (`data/experiment/reresolucion_catalogo/salidas/`)

Cada una se reproduce con su script desde la raíz de una copia (las de la prueba, con `reresolver_catalogo.py` y los
generados de `componer`; la medición y las fichas, en doble corrida, byte a byte):

| archivo | sha256 | qué es |
|---|---|---|
| `r2_1_medicion.json` | `9a25c3f7…` | umbral, parte A (§A.2), menciones que no verifican, R3 ampliada, población y muestra de la parte B |
| `r2_1_fichas_parte_b.json` | `ec33611e…` | las 30 fichas sorteadas (semilla 20261006) |
| `r2_1_lectura_parte_b.json` | `f3ea5a1e…` | mi lectura de las 30, con el criterio |
| `r2_1_fichas_parte_b.md` | `9d37c64b…` | fichas con el texto completo y la lectura, para la adjudicación |
| `r2_1_controles.json` | `62aa1faa…` | resumen de los controles (§3) |
| `r2_1_prueba_ampliaciones_T1_T4.json` | `bf620c72…` | la lista de prueba (T1 a T4) |
| `r2_1_ampliaciones_vacia.json` | `f975cfda…` | la lista sin ampliaciones (controles) |
| `r2_1_prueba_reporte_composicion.json` | `4da169eb…` | composición del catálogo de prueba (`b9aced1f…`) |
| `r2_1_prueba_reporte_diez.json` | `c3e76194…` | `reporte_reresolucion.json` de la prueba en diez |
| `r2_1_prueba_reporte_desarrollo.json` | `c281b99e…` | ídem en desarrollo |

Las rutas que llevan los reportes son relativas a la raíz de la copia (`_r2_1/…` es el directorio de trabajo de la
copia). Los grafos de la prueba (`kg.json`, 47 MB) no van al repo: el sha de cada uno está en su reporte.

## 9. Cierre

- **W1 a W3 no están en el repo.** Al cierre, SC2 de U-SINCOLA-T0 no está commiteado: el último commit de
  `data/experiment/sincola_t0/` es `01046b6`, y la fixture, `grafos.py` y `sincola_t0/` tienen cambios de SC2 sin commit
  (con su `freno_sc2.md`). Por la decisión de la autora (§0.2), los tres cambios van como parches en el paquete
  (`W1_ensamblar_tanda0.patch`, `W2_r1_e4.patch`, `W3_regression_kg.patch`), que aplican limpio sobre HEAD
  (`git apply --check`). Mientras no se apliquen, `reresolver_catalogo.py` y su selftest no corren sobre el repo (piden
  `catalogo_resolucion_r2` y el parámetro de W1). Con SC2 commiteado: aplicar, correr `controles_r2_1.sh` (cadenas,
  catálogo sin ampliaciones y suite, contra el código de HEAD) sobre una copia nueva y frenar.
- HEAD pasó durante la sesión de `01046b6` a `26c6502` (U-SEG-OFICIAL S0-2). `git diff --stat 01046b6 26c6502` sobre las
  rutas que usa esta unidad (ensamblador, `corpus_v2`, `e2_reduce`, `pyd_r2/code`, shapes, suite, `catalogo_unico`, E0
  r2b, `corpus_tanda0`, `reresolucion_catalogo`): vacío.
- **Escrituras en el repo:** solo archivos nuevos en `data/experiment/reresolucion_catalogo/`: 8 en el directorio
  (`reresolver_catalogo.py`, `selftest_reresolver_catalogo.py`, `r2_1_medicion.py`, `r2_1_fichas.py`,
  `r2_1_resumen_controles.py`, `controles_r2_1.sh`, `procedimiento_crecimiento_catalogo.md`, este freno) y 10 en
  `salidas/`. Ningún archivo existente cambió por esta unidad.
- **sha256 del repo** (todos los archivos salvo `.git` y `.venv`): antes 22.854 archivos, después 22.934: cambian 45, aparecen 87 y
  desaparecen 7. De esta unidad, solo los 18 nuevos. El resto es de otras sesiones en paralelo, clasificado por ruta: SC2
  de U-SINCOLA-T0 (la fixture y `grafos.py`, 39 nuevos en `sincola_t0/` y 8 en `ens_*_r2b_sincola/`), el volumen de Neo4j
  (41, 21 y 7; esta unidad no usa Neo4j, y la carga es de SC2), el commit `26c6502` (2) y U-E3-LISTAS (1). Ningún
  ensamblado sellado ni ninguna ruta que leyó esta unidad cambió (`URERESOL_CAT_R2-1_sha_diff_repo_antes_despues.txt`, en el paquete).
- `.pyc` fuera de `.venv`: 2.213 al empezar y al cerrar; en la copia, 0.
- **Grep de convenciones** sobre los 18 archivos nuevos y sobre el paquete; las coincidencias en este punto, que enumera
  los términos buscados, no cuentan. Nombres propios y origen conversacional (los nombres no se transcriben; «mentor»,
  «tutor», «profesor», «reunión», «slack», «mail», «correo», «whatsapp», «como dijo», «según dijo/pidió», «pedido por»,
  «me/nos pidió»): solo «correo» en dos labels de normas del corpus (`r2_1_medicion.json`: «Utilización de correo
  electrónico para notificación», «… cambios de domicilio o correo»); ningún nombre ni origen conversacional. Primera
  persona del plural («nosotros», «hicimos», «tenemos», «nuestro/a», «decidimos», «corrimos», «vamos a», «encontramos»,
  «medimos», «proponemos»): ninguna coincidencia.
- Paquete `revision_URERESOL_CAT_FRENO_R2-1/`, con `manifest.txt`, en el scratchpad de la sesión.
- **Commit: PENDIENTE de la autora. FRENO R2-1.** Espero la adjudicación de las 30 fichas, la firma de la enmienda 6 y el
  «seguí» de R2-2; la aplicación de W1 a W3, con SC2 commiteado.
