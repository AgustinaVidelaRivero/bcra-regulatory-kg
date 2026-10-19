# FRENO T1 — tanda final de B6.1: la corrida en seco (18/10/2026, USD 0, sin API, sin commit)

Pre-registro FIRMADO: `docs/preregistro_tanda_final.md` (sha256 en HEAD `b760edf7…`), con su versión derivada de T1
(`data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T1.md`, `e6ee519a…`, y su `.huecos.json`, `9c86ae1f…`).
Rigen el §1, el §2, el §3, el §4.1, el §4.2, el §5 y el §8, y lo que del pre-registro de la tanda 1 (firma en `95b18217`) el de la tanda
final no reemplaza. HEAD `5d8cb917`. T1 corrió de 19:56 a 22:55 (−03). Todo lo que escribí está en `data/experiment/tanda_final/t1/`,
`data/experiment/tanda_final/t2/`, `data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/` y
`data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json`. Nada commiteado y ningún mensaje de commit preparado: los
commits son de la autora y quedan PENDIENTES.

**Resultado:** los criterios de aceptación de T1 están en verde, con dos cosas que decide la autora antes de T2 (sección 13): qué
estimado por TO lleva el manifiesto (el plano del despacho, que dejé en el repo, o el repartido por caracteres que el registro de
decisiones, §21, dejó pendiente para esta tanda, que dejé preparado) y si el ensamblado del tramo 1, que corre con una salida stub que
suma el `TextoOrdenado`, alcanza para el sello del tramo 1. Hubo un incidente externo (un Neo4j que se apagó y reescribió su volumen,
ignorado por git) y siete errores propios, todos corregidos antes de este freno. T2 espera la revisión y el «seguí».

**Las cifras:** todas salen de `freno_t1_cifras.py` → `freno_t1_cifras.md` (las tablas, numeradas) y `freno_t1_cifras.json`, desde los
archivos de `t1/`. Cada sección nombra su tabla. Desde la raíz del repo:
`python3 -I -B data/experiment/tanda_final/t1/freno_t1_cifras.py --repo "$PWD" --md <md> --json <json>`.

## 0. Paso 0 (19:56 a 19:58)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git rev-parse --abbrev-ref HEAD
main
$ git status --porcelain --untracked-files=no
$ pgrep -fl "runner_corpus.py|ensamblar_tanda0.py|regression_kg.py|shapes_validator.py"; echo "pgrep_rc=$?"
pgrep_rc=1
$ git log --format='%h %s' -6
5d8cb917 Pre-registro de la tanda final: la revision entre tandas y la version derivada con los huecos de antes de la primera etapa
4de7f2a7 Pre-registro de la tanda final firmado por la autora, con su precision sobre la fixture de la suite y las fuentes de sus huecos
27f02a4d Pre-registro de la tanda final: el codigo de la cadena re-sellado sobre el cableado, los valores de sus huecos y el registro de decisiones
c66c7ecd Alcance de la tanda final en el mensaje del extractor: el derivado con sus filas, su candado, el selftest y las anclas al dia
0c2befad Primera tanda: el reporte final de la quinta etapa, con su costo, sus modelos, sus hallazgos y las propuestas para el backlog
b8147b59 Registro de decisiones: el control del commit del cableado, el cegamiento de las cuentas de la cache, las anclas y la fixture
$ git show HEAD:docs/preregistro_tanda_final.md | head -5
# Pre-registro — B6.1 tanda final: la última tanda del escalado con la release r2

**FIRMADO por la autora el 18/10/2026** (firma por mensaje recibido a las 19:40:51; hoja de ruta de la mesa, §171), sobre la v3
para firmar (sha256 `0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b`, commiteada en `5289b02f`), con la precisión de la firma que la autora aceptó el 18/10/2026
a las 19:15:01 (sección «Precisión de la firma», al final). Rige desde esta firma.
$ python3 -I -B data/experiment/tanda_final/preregistro/completar_preregistro_tanda_final_mesa.py docs/preregistro_tanda_final.md \
    <scratchpad>/paso0/vacia data/experiment/tanda_final/preregistro/huecos_preregistro_tanda_final.json \
    <scratchpad>/paso0/derivada_T1.md --momento T1 --repo "$PWD"
completo hasta T1: 7 huecos; esperan 7; derivada_T1.md sha256 e6ee519a63e9004318bfa9718ca9e5db8e8b452fabbc477dae607dd3321f1f61
$ cmp <scratchpad>/paso0/derivada_T1.md data/experiment/tanda_final/preregistro/preregistro_tanda_final_derivada_T1.md     → iguales
$ cmp <scratchpad>/paso0/derivada_T1.huecos.json …/preregistro_tanda_final_derivada_T1.huecos.json                        → iguales
e6ee519a63e9004318bfa9718ca9e5db8e8b452fabbc477dae607dd3321f1f61  (los dos .md)
9c86ae1fe42373b38cefddf2a85408612f92c1e532da44ff1472159f7c1e1420  (los dos .huecos.json)
$ grep -c -E '⟦(A3|codigo_cadena|revision)\.' <scratchpad>/paso0/derivada_T1.md
0
$ git show HEAD:docs/preregistro_tanda_final.md | shasum -a 256
b760edf7d341290ad910de993f8a868be426abcf2cfd14459240ad5a2b940cc2  -
  (la sección final de la derivada nombra «El pre-registro:** sha256 `b760edf7d341290ad910de993f8a868be426abcf2cfd14459240ad5a2b940cc2`»)
$ python3 -I -B t1_paso0_rutas_tanda_final.py --repo .
sello: data/experiment/tanda_final/preregistro/codigo_de_la_cadena_c66c7ecd_mesa.json (n declarado = 78, commit = c66c7ecdfae0d1b47cc5cbc4b4c43c18aede9fa9)
rutas leídas: 78
HEAD:  78 de 78
árbol: 78 de 78
$ df -k "$PWD" | tail -1
/dev/disk3s1   971350180 748868468 168953772    82% 7039484 1689537720    0%   /System/Volumes/Data
$ ls -d data/experiment/tanda_final/t1 …/salida_tanda_final_r2b …/tanda_final_98tos_r2b.json …/corpus_tanda_final
  (las cuatro: No such file or directory)
```

- `pgrep` dio rc 1 y salida vacía. La comparación de la derivada regenerada con la commiteada está también en la tabla 12. 168.953.772 KB libres, más que el piso de 31.457.280.
- **Las cifras con las que corre la tanda** (sección final de la derivada; tabla 1): documentos fuera, ninguno; 98 TOs y U = 4.951; el
  estimado, USD 104,5404 (U × 0,021115); el tope, USD 151,58 (escrito a dos decimales); el tramo 1, 30 TOs y 601 unidades (estimado
  12,6901); el tramo 2, 68 y 4.350 (91,8502); las bases del control entre tramos, 0,026331 de costo por unidad (umbral 0,03423) y
  0,020073 de cola (umbral 0,030109). La U es la del despacho, así que el tope del manifiesto es el del punto 1.3 a cuatro decimales,
  151,5835 (sección 13, punto 4).
- **El script de las 78 rutas** es `t1_paso0_rutas_tanda_final.py`: el de la tanda 1 con el sello de `c66c7ecd` y `sys.dont_write_bytecode`.
  En el paso 0 corrió desde el scratchpad, antes de escribir nada en el repo; después lo llevé a `t1/`, igual byte a byte.
- **La foto del repo antes** (19:57:30 a 19:57:43, `foto_repo_tanda_final_t1.py`, el de la tanda 1 con los `*_SOLO_MESA*` también sin
  abrir): 52.693 entradas, 40 sin abrir y 342 enlaces. La línea de base de `.pyc` y `__pycache__` tiene 11.236 líneas.

## 1. La consulta de deprecaciones (19:58:01 a 19:58:03)

`consulta_deprecaciones_t1.txt`. La leí con WebFetch, sin iniciar sesión, en `https://platform.claude.com/docs/en/about-claude/model-deprecations`,
sin error.
- `claude-haiku-4-5-20251001`: «Active»; Deprecated «N/A»; retiro tentativo «Not sooner than October 15, 2026».
- `claude-sonnet-5`: «Active»; Deprecated «N/A»; retiro tentativo «Not sooner than June 30, 2027».
- El historial no trae ningún aviso para ninguno de los dos; el más reciente es del 2026-09-30 y es de `claude-sonnet-4-5-20250929`.
- «Notifications»: el aviso llega con «at least 60 days' notice».
- **Contra la consulta del 18/10/2026 de las 11:45 (pre-registro, §2): sin cambios. No hay retiro anunciado: no corresponde el freno
  del §4.2 ni el procedimiento (c).** Sin aviso al 18/10/2026, E1 no se retira antes del 17/12/2026.

## 2. La E0 de los 98, con el código del gate (20:02:46 a 20:13:33; tabla 2)

`lote_e0_tanda_final_t1.sh` corre los pasos de `lote_tramo1_S2.sh` (no el lote entero: su rsync, renglón 11, no excluye `tanda1/t4/` ni
`t5/`) sobre una copia hecha con `copia_clausula_tanda_final_t1.sh` (la cláusula del despacho, más `tanda_final/preregistro/`), con el
python del `.venv` del repo. Los controles están en `t1/e0/`.
- **La copia y la raíz:** 0 archivos por nombre (`.env`, `NO_ABRIR_`, `*_SOLO_MESA*`) y 0 enlaces; la raíz de `raiz_minima.sh`, 0 enlaces.
- **El código** (`control_codigo_raiz_t1.json`): `e0_lib.py`, `correr_e0.py` y `e0_tablas.py` dan los tres `codigo_sha256` de S0-6b
  (`80adbd58…`): OK.
- **Los 152** (`correr_152.py --workers 9`, 20:03:28 a 20:09:21; `control_e0_152_t1.json`): 768 de 768 iguales, 152 TOs, 10.478 unidades.
- **Los 98, dos veces** (`--tos`; 20:09:21 a 20:10:40 y 20:10:40 a 20:11:54; `control_e0_98_t1.json`, con `control_e0_tanda_final_t1.py e0`):
  - las dos corridas dan los mismos 1.512 archivos, byte a byte (`por_to/` incluido);
  - los 490 archivos por TO dan el sha256 y los bytes de su entrada del manifiesto: 490 de 490;
  - los 7 agregados, como JSON leído, dan los de los 152 restringidos a los 98, con las claves en el mismo orden; `version_e0.json` da su
    entrada del manifiesto;
  - el primer nivel tiene 498 archivos, con 0 que faltan y 0 que sobran;
  - **4.951 unidades**, y cada TO da su `unidades_por_to`;
  - **los 98 PDF** dan el `sha256_pdf` de S1-ter (`f59cdea0…`), en `escalado_prep/pdfs/` del repo y en la raíz: 196 de 196.
- **El control de salud** (`healthcheck_e0.py` con un `--pdf` por TO, y `resumen_healthcheck_S2.py` sobre mi E0): en verde
  (`frena_por_cobertura_o_ids` vacío), y el resumen (`resumen_healthcheck_tanda_final_t1.json`, `16843464…`) es **byte a byte el de S2c**
  (`comparacion_resumen_hc_t1.json`: 0 diferencias). El JSON crudo del health-check no lo llevé al repo ni al paquete, porque trae
  muestras de texto: su sha256 es `5ef831d0…`, el `hc_sha256` que nombra el resumen de S2c.
- **Al repo** fueron los 498 archivos del primer nivel de la corrida 1, sin `por_to/`, a `e0_chunking/salida_tanda_final_r2b/`: los 498
  dan el sha256 y los bytes de la corrida 1 (tabla 12).
- El primer intento del lote (20:00:31) frenó en el rsync, con rc 23: el incidente de la sección 11. Lo rehice en una carpeta nueva.

## 3. El manifiesto de la tanda final (tabla 3)

`manifiestos/tanda_final_98tos_r2b.json`, **sha256 `23654ef8a43900b2547c2de6dac3e86f2d29c91d6b380ca4439b102468f63740`**. Lo armó
`t1_manifiesto_tanda_final.py` sobre una copia (la cláusula, ya con la E0 de los 98 del repo), y de ahí lo llevé al repo; `--verificar`
contra el del repo da «igual», y el primer armado es byte a byte el del repo (tabla 12).
- **El perfil:** el `r2b` de A3, después de su commit (`rol_por_to` con la tabla de la release y el derivado `c8dea08a…`): 85 TOs con
  alcance (52 de la tabla y 33 del derivado) y 13 en null (tabla 3).
- **`tos`:** las entradas de los 98 en el manifiesto de los 152 de S1-ter, con solo `rol_alcance` cambiado.
- **`nombres_remision`:** el método de `reext_t0/t1_manifiestos.py`, que no los deriva: vacíos, como en la entrada de S1-ter (lo declara
  la `descripcion`). El runner no los lee; el ensamblado sí (sección 8).
- **`rutas.e0_salida`:** `data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b`.
- **`orden_corrida`:** los 30 del tramo 1 y después los 68 del tramo 2, cada tramo de menor a mayor por unidades, con desempate por id
  (tabla 3, al pie). El script controla que los tramos sean los de `tramos_tanda_final.json` y que la E0 dé sus unidades.
- **`limites`:** `tope_global_usd` 151.5835 (1,45 × 4.951 × 0,021115 = 151,58352925); `margen_unidad_usd` 0.35; `checkpoint_cada` 150 en
  ctavis, depinv y pimf; `chequeos_hits` vacío; `estimado_usd` por TO con la fórmula del despacho: e1 = unidades × 0,010135 más las
  líneas de alcance del TO de A3, y e3 = unidades × 0,010980, a seis decimales (tabla 8).
- **La suma del estimado: USD 104,749803**, que es exactamente U × 0,021115 más las líneas de A3 por documento (0,209438). Contra
  U × 0,021115 más el costo de las líneas de A3 de la derivada (0,209440) hay **−0,000002**: las líneas de A3 redondean sus tokens por
  documento y suman 0,209438 (`FRENO_A3.md`, al pie de su tabla de costo). A cuatro decimales, las dos dan 104,7498. Es la misma
  diferencia de redondeo que la tanda 1 declaró con A2.
- **`sellos`:** la forma de los de la tanda 1, con el commit del código `c66c7ecd`, la E0 (498 archivos, «PENDIENTE (lo fija el commit de la
  autora)»), el prefijo de E1 `322c5a23e9b7` (`ccffa4e3…`, 59.909 caracteres), el tool schema `0c391f2b…`, los namespaces, las
  temperaturas 0 y 1, el prefijo de E3 `21a836c7de6d` y los candados: tablas forzadas `98cc96b2…`, candado del mensaje `6b758517…`, mensaje
  `eeb11b9a…`, derivado `c8dea08a…`, candado del mensaje de E3 `079d2489…` y mensaje `66bc8656…`. El control de entradas (l) los controla
  contra lo que carga el código.
- **La carga:** `manifiesto_corpus.cargar`, con sus valores por defecto, lo carga sin error (98 TOs, perfil r2b, el orden igual).
- **El control en contra:** el mismo manifiesto armado con el perfil anterior a A3 (en la copia, `prompt_r2b.py` y el derivado `e06933e7…`
  de `5289b02f`, restaurados después y controlados por sha256) difiere solo en `rol_alcance` (null en los 33) y **frena al cargarse en
  ri_bdp**, uno de los 33: «TO 'ri_bdp': rol_alcance null pero el catálogo declara 'Sujeto_rol_entidad_comprendida_reginf' para
  ri_bdp.pdf — una entrada del catálogo no se silencia por manifiesto». Está en `t1/manifiesto/…_contra_perfil_anterior_a3.json`
  (`aeb00464…`).
- **La alternativa con el reparto** (sección 13, punto 1): `t1/manifiesto/tanda_final_98tos_r2b_reparto_alternativa.json`
  (`e9993b9d…`), con el mismo total repartido por caracteres de la E0; carga sin error y suma lo mismo.

## 4. El control de entradas (`t1_control_entradas_tanda_final.py`; salidas en `t1/entradas/`; tabla 4)

**13 de 13 en OK** (`control_entradas_t1.json`, veredicto OK), sobre la copia del manifiesto:
- **a–d.** El prefijo, el tool schema, los namespaces de E1 (`-rforma1` y `-rforma2`) y el prefijo y el namespace de E3. Los modelos del
  runner son `claude-haiku-4-5` y `claude-sonnet-5`.
- **e.** Los 490 archivos por TO de la E0 contra S0-6b: 490 de 490, y los 498 archivos que dicen los sellos.
- **f.** El candado del catálogo y los insumos del prefijo.
- **g.** La temperatura: 0 en las 2.439 unidades de la tanda 0, en las 3.290 de la tanda 1 y en las 4.951 de la tanda final, y 1 en el
  reintento por forma, con el resto del pedido igual.
- **h.** Las tablas forzadas, el candado y el mensaje (`6b758517…` / `eeb11b9a…`), el derivado (`c8dea08a…`) y el candado de E3. Y
  `selftest_clave_cache` en OK (sección 4.1).
- **i. Los mensajes de E1 contra el código de la base de A3 (`5289b02f`)**, por el camino del runner (como `mensajes_runner_a3.py`:
  solo la carpeta del runner en el `sys.path`, `runner_corpus.configurar` con el manifiesto de la tanda 0; ningún módulo de
  `data/experiment` de fuera del árbol):
  - **tanda 0: 2.439 de 2.439 iguales byte a byte; tanda 1: 3.290 de 3.290** (el mensaje y el pedido canónico, por unidad);
  - **tanda final: cambian 1.178 unidades, las de los 33 documentos con entrada nueva del derivado, y solo en la línea de alcance**: sin
    esa línea y su renglón vacío, cada una es el mensaje de la base; los otros 65 documentos, iguales byte a byte;
  - el árbol de la base es `git archive 5289b02f` de las 78 rutas, más las E0 de las tres tandas, los tres manifiestos, los PDF y dos
    carpetas de datos que lee `runner_corpus` al importarse (`e0_chunking/salida/` y `e1_extractor/salida/faseB_pro/`, sin cambios entre
    `5289b02f` y HEAD; `arbol_base_a3_datos_agregados.txt`). Su derivado es `e06933e7…` (10 entradas); el de la copia, `c8dea08a…` (43).
- **j.** El recorte de herencia en la tanda final: 21 unidades (ri_dsf 2, ri_transpa 8, snp_dd 11), con la línea una vez cada una y en
  ninguna otra.
- **k.** El rol de alcance de los 98, igual al del perfil.
- **l.** Los sellos del manifiesto, contra lo que carga el código, el tope y el estimado (exacto contra las líneas por documento y a
  cuatro decimales contra el total de A3).
- **m.** La carga y el control en contra de la sección 3.

### 4.1 El selftest de claves, sin las cuentas

`selftest_clave_cache --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b` corrió en la copia, con su JSON y su consola
a archivos (nunca a la pantalla), rc 0. `selftest_claves_sin_cuentas_t1.py` les sacó las cuentas con
`alcance_e1/a3/scripts/clave_cache_sin_cuentas_a3.py`, en otro proceso, y comparó: **las dos salidas sin cuentas son byte a byte las de
A3 sin cuentas** (`selftest_clave_cache_a3_sin_cuentas_a3.json` y su consola), así que el retiro cubre toda cuenta y no hubo que mandar
nada a un `NO_ABRIR_`. Veredicto del selftest: OK. No miré las cuentas.

```
2f7e8f60e6d4847c7f5fcc870f9f8a087089a0d371e6df41649f58b8ec42cdc8  t1/entradas/selftest_clave_cache_t1_sin_cuentas.json
b4789268a7aa5d6db71f8e2a732e570de7716fae0450a8aa603f553792e618d1  t1/entradas/consola_selftest_clave_cache_t1_sin_cuentas.txt
5dd75621c659f0ca275826759fede37f81c22b0e270f4f297d6bc713f5931235  selftest_clave_cache_t1.json (original, con las cuentas; no se abre)
e4d74d17efa5e12a5955a35bf4e78693eb2f239e9241c694d7b7130b62e51e88  consola_selftest_clave_cache_t1.txt (original, con las cuentas; no se abre)
```

## 5. La corrida en seco (`t1_corrida_en_seco_tanda_final.py`; salidas en `t1/seco/`; tablas 5 y 6)

Sobre una copia hecha con la cláusula (0, 0 y 0), con `--stub`. El script es el de la tanda 1 con la raíz por `--raiz` (la cláusula
excluye `tanda_final/`, así que el script no está en la copia).
- **El camino:** importa `runner_corpus.py` desde su archivo y llama a su `main()` con `--manifiesto …/tanda_final_98tos_r2b.json
  --salida <salida> --stub` (los 98, sin `--tos`). Del `sys.path` solo pone en `sys.path[0]` la carpeta del runner, como
  `python runner_corpus.py`; el resto lo arma el runner. No llama a ninguna fase por fuera. Los stubs son subclases de los del runner
  que registran cada pedido y devuelven las respuestas de cada rama.
- **Las guardas:** el constructor de `ClienteE1Real` y el de `ClienteE3Real`, y `anthropic.Anthropic`, tapados; la red, bloqueada; la
  clave, fuera del entorno. **0 conexiones, 0 clientes de la API y 0 clientes reales: 0 llamadas a la API.** El runner sale con 0.
- **Las cinco ramas, sin forzar ninguna** (con la hipótesis de la salida p90, 1,5051 tokens por carácter; tabla 6):
  - corte y reintento por corte: 28 unidades o partes salen en 16.384;
  - partición: `cateloc::Sbloque10` (5 partes) y `ri_transpa::Sbloque1::chapeau_seccion` (2);
  - tercer escalón: 17 (16 unidades y una parte), con 0 que cortan también;
  - salida mal formada: `ri_bdp::S1` (el `-rforma1` sale bien), `ri_rcl::1.2` (se repara) y `ri_esd::S1` (queda con
    `salida_mal_formada_tras_reintento`);
  - el ratchet de E3: `ri_bdp::S2`, con dos verificaciones y una re-extracción de E1.
- **Los pedidos** (tabla 5): **E1**, 5.022 a `claude-haiku-4-5` con temperatura 0 (4.958 en 8.192, 47 en 16.384 y 17 en 40.960);
  **reintento por forma**, 5 con temperatura 1 (3 en `-rforma1` y 2 en `-rforma2`); **ratchet**, 1; **E3**, 4.956 a `claude-sonnet-5`, sin
  temperatura, con 4.096. Los 4.958 primeros intentos (las 4.951 unidades más las 7 partes) dan 4.951 claves distintas: ver abajo.
- **Las claves que se repiten:** 13 unidades de `snp_dd`, intersticiales de S7 con el mismo texto (`sha256_propio`), dan 6 pedidos de E1
  idénticos entre sí (5 pares y un trío; tabla 6). En T2, el segundo pedido de cada grupo sale de la caché: 7 unidades sin costo de E1 ni
  de E3, con la misma extracción que su gemela. El runner no frena por eso (`IdsRepetidos` mira ids de chunk, `runner_corpus.py:155-175`).
  En la tanda 1 no pasó (3.299 claves de 3.299 primeros intentos).
- **Claves ya en las bases de la copia** (abiertas `mode=ro&immutable=1`): 0 de 5.020 de E1, 0 de 1 del ratchet y 0 de 4.948 de E3.
- **La reproducción** (`comprobaciones_t1.py` → `comprobaciones_t1.json`; tabla 12): dos corridas seguidas dan mis cuatro salidas, la
  consola y el resumen iguales byte a byte; de los 1.775 archivos del runner, 301 difieren: 203 checkpoints (con `ultimo_checkpoint.json`)
  por su hora, y 98 `reporte_e2` solo por la ruta de la salida (iguales con la ruta normalizada). La de `t1/seco/` es una tercera corrida,
  con la versión final del script: sus salidas, la consola y el resumen son los de las dos primeras, más la clave
  `stub_con_texto_ordenado: false` en `corrida_en_seco_t1.json`.

## 6. Las unidades que no entran en una llamada (`seco/censo_unidades_grandes_t1.json`; tabla 7)

La capacidad es la de la tanda 1: el reintento (16.384) cubre 10.886 caracteres con la p90 (14.146 con la mediana), y el tercer escalón
(40.960), 27.214 (`correr_e0.CAPACIDAD_ESCALON_3_R6`).
- **18 unidades pasan los 10.886 caracteres** (9 pasan también los 14.146 de la mediana), y **ninguna queda sin declarar**.
- **16 no se pueden partir** (`sin_items_detectables`): las cubre el tercer escalón, todas debajo de su capacidad (la mayor,
  `seggar::8.2`, 19.998). En la corrida en seco las 16 fueron al tercer escalón.
- **2 se parten por corte:** `cateloc::Sbloque10` (48.321, 5 partes, todas debajo de 10.886) y `ri_transpa::Sbloque1::chapeau_seccion`
  (21.712, 2 partes; la primera, 13.705, va al tercer escalón).
- Sobre el tercer escalón con la p90: ninguna unidad ni parte. Otras 22 unidades cortarían en 8.192 con la p90 y saldrían en 16.384.

## 7. El estimado por TO (`seco/estimado_por_to_t1.json`; tabla 8)

Con los clientes stub el gasto es 0. Con la tarifa del §3 y las líneas de alcance de A3: **98 de 98 TOs dan el estimado del manifiesto**
(e1 y e3), **USD 104,749803** en total (104,7498 a cuatro decimales; el runner lo lee como 104,75). **Tope 151,5835: margen 46,833697,
1,4471 veces el estimado.** La cota de la salida de los pedidos que cortan con la p90 es USD 3,4818 (lo que la tarifa por unidad no
incluye si la salida real fuera la del p90; el freno por proyección lo controla con el gasto real). La tabla 8 trae, al lado, el
estimado de cada TO con el reparto (sección 13, punto 1).

## 8. El ensamblado de un subconjunto: corre (`ensamblado_tramo1_t1.py`; evidencia en `t1/ensamblado/`; tabla 9)

- **La salida:** la stub de los 30 del tramo 1 (`t1_corrida_en_seco_tanda_final.py --tos <los 30>`, rc 0, 0 llamadas, las cinco ramas).
- **Los manifiestos de ensamblado:** los de los 98, de `nombres_remision/derivar_manifiesto_ensamblado_mesa.py` (el método del T3 de la
  tanda 1, con el corpus «tanda_final» de su contraste: rige la regla v2; la variante con la raya da 3 distintas y no entra; 31 de 98 TOs
  con nombres), restringidos a los 30 (`estimado_usd` y `checkpoint_cada` también: `manifiesto_corpus.cargar` pide una clave por id). El
  derivador frena con un corpus que no está en su medición, y no hay uno con los 30. 25 de los 30 tienen `nombres_remision`.
- **El ensamblado de la tanda 1:** `ensamblar_tanda0.py --manifiesto … --entrada <salida stub> --e0-r2 <E0 de la tanda final> --salida …`,
  y el sin cola con `--sin-cola`, como `tanda1/t3/scripts/cadena_t3.sh`, desde la raíz de la copia.
- **Primer intento, con la salida stub del runner: frena en el invariante I4** («576 aristas colgantes»: aristas `establecida_en` hacia
  `TextoOrdenado_<doc>_pdf`). La causa: `derivar_establecida_en` (`ensamblar_tanda0.py:600-625`) agrega a cada nodo de contenido una
  arista hacia el `TextoOrdenado` canónico de su TO, y el stub del runner (`runner_corpus.py:268-276`) emite solo un `Obligacion` por unidad,
  sin el `TextoOrdenado` que E1 real emite. Es un artefacto del stub, no del ensamblado (consolas en `ensamblado/intento1_stub_del_runner/`).
- **Con la salida stub que suma el `TextoOrdenado`** (`--stub-con-texto-ordenado`: cada respuesta suma
  `{"type": "TextoOrdenado", "properties": {"archivo": <pdf>}}`, la clave con la que E2 lo identifica, `e2_lib.py:116`): **los dos
  ensamblados salen con 0**, 716 nodos y 855 aristas cada uno, con la doble corrida interna byte a byte igual, y el mismo `kg.json`
  (`ac284ffd…`) en dos procesos distintos (tabla 12). El sin cola sale igual al completo porque la salida stub no tiene cola.
- **Lo que no probé:** el acumulado de las tandas 0 y 1 con el tramo 1 (el otro grafo del sello del tramo 1, §5): necesita las salidas
  reales de T2 de la tanda 1, que T1 no abre. Su mecanismo es el del T3 de la tanda 1 (`armar_acumulado_t3.py`).
- **Lo que deja:** por el §4.1, punto 5, si corre, hay sello del tramo 1 como respaldo. Corre, con la salida stub declarada arriba.
  Si eso alcanza lo decide la autora (sección 13, punto 2).

## 9. T2, preparada y probada en seco (`data/experiment/tanda_final/t2/`; evidencia en `t1/pruebas_t2/`; tabla 10)

```
96a022db316ca355956812fe48b135264cfd2e018b09ee8d271c5fec68467eec  data/experiment/tanda_final/t2/lanzar_t2.py
35ee2094d28454f9c2bdd0ce52e5305226bbf833413eba2bfe4bb8ac9d4d43b4  data/experiment/tanda_final/t2/freno_modelo_t2.py
efd7b3ba6ad6e61c35d1d172594b917c110211b8b20e6dfbe98f4cc11eb49026  data/experiment/tanda_final/t2/resumen_t2.py
35147781df10f89be101037aa3be95bc384e9626cda69a610466bec9a06853ee  data/experiment/tanda_final/t2/conteos_t2.py
0f46c3c804a9857dd439b4d09ae988c3a558cd54ae038d633d582db398be6b2c  data/experiment/tanda_final/t2/caso_en_contra_t2.py
97973e9cbd6de30c0e593b7b729c224e0069ae3c3472ed1f8b88c5be0447e541  data/experiment/tanda_final/t1/t1_paso0_rutas_tanda_final.py
```

### 9.1 Qué hace cada uno

- **`lanzar_t2.py`** (el de la tanda 1, con los dos tramos):
  - **controles previos**, y si uno falla para con 2: el piso de 30 GB; las 78 rutas (`t1_paso0_rutas_tanda_final.py`); el SDK 0.100.0;
    el sha256 (`23654ef8…`) y el tope (151.5835) del manifiesto; que los primeros 30 de `orden_corrida` sean el tramo 1 y los otros 68
    el tramo 2 de `tramos_tanda_final.json`; la copia de trabajo, fuera del repo y nueva;
  - **el freno por modelo** antes del primer TO sobre las etiquetas de los 98, y después de cada TO sobre las de ese TO
    (`corpus_<TO>_e1`, `corpus_<TO>_reintentos_e1` y `corpus_<TO>_e3`). Imprime solo OK o FRENO y los conjuntos de ids;
  - **el tramo 1:** los 30 en el orden del manifiesto, de a uno, con la misma `--salida` (`corpus_tanda_final/salida_r2b`) y
    `--autorizado-tope 151.5835`: es correr `--tos <los 30>` con el freno después de cada TO, como en la tanda 1. El tope es uno solo,
    el del estado del runner en esa `--salida`;
  - **el control entre tramos**, al cerrar el tramo 1: copia (archivos, sin enlaces ni archivos que no se abren) `resumen_t2.py` de la
    tanda 1, el manifiesto, la E0, la `--salida` y `tanda_final/preregistro/`, y corre ahí `control_entre_tramos_tanda_final_mesa.py` con
    las bases del pre-registro y la lista de los 30. Su JSON queda en `t2/control_entre_tramos_tanda_final.json`. Con OK sigue con el
    tramo 2 sin leer nada; con FRENO para con 11 y decide la autora; si no corre, para con 12;
  - **el tramo 2:** los 68, igual;
  - **para** si el freno da FRENO (10) o si el runner sale distinto de 0 (su código), sin empezar el TO siguiente;
  - **la pausa entre documentos:** antes de lanzar cada TO, desde el viernes 23/10/2026 a las 18:00 (−03), no lo lanza y para con 20; el
    que corría ya terminó. Mientras corre el lanzador la tanda no está sellada;
  - **el registro** `t2/avance_t2.jsonl`: por TO, inicio, fin, tramo, código, freno (con los ids) y gasto global contra el tope; los
    controles, el control entre tramos, las paradas y el fin. Nada del desglose de E3;
  - corre con `PYTHONDONTWRITEBYTECODE=1` y `-B`; no lee la clave (la saca del entorno del runner, que la carga de su `.env`); la salida de
    pantalla del runner va a `t2/NO_ABRIR_salida_e3_tanda_final.txt`, que el lanzador nunca lee; el SIGINT manual pasa al runner y para con
    130; borra la copia de trabajo al terminar, también cuando para;
  - **dos opciones para decisiones de la autora, y solo con ellas:** `--autorizado-tramo-2` (sigue con el tramo 2 aunque el control dé
    FRENO, que igual corre y queda en el registro) y `--retomar-tras-pausa` (para retomar después de B6.3 y las tripletas T). Sección 13,
    punto 5. Solo para las pruebas: `--solo-tos-tramo-1`, `--solo-tos-tramo-2`, `--stub`, `--git-repo` y `--hora-simulada`.
- **`freno_modelo_t2.py`, `resumen_t2.py`, `conteos_t2.py` y `caso_en_contra_t2.py`:** los de la tanda 1, con las rutas de la tanda final
  (el manifiesto, `corpus_tanda_final/salida_r2b`, `t2/NO_ABRIR_salida_e3_tanda_final.txt` y `t2/NO_ABRIR_conteos_reextracciones_tanda_final.json`)
  y sin otro cambio. `conteos_t2.py` arma el desglose del cegamiento y da solo su sha256 y la vigilancia `integridad_e3`.

### 9.2 Las pruebas

- **Las bases reales**, copiadas a una carpeta de trabajo (`etiquetas_tanda_final.txt`, `freno_modelo_tanda1.txt`): las etiquetas de los
  98 ya en las bases, **ninguna**; el freno sobre los 20 de la tanda 1 da `['claude-haiku-4-5-20251001']` y `['claude-sonnet-5']`, OK.
  Las tres bases del repo dan el mismo sha256 antes y después de todas las pruebas del freno (tabla 12). Una corrida del freno tarda entre 0,72 y 1,62 s (`tiempo_freno_modelo.txt`).
- **De punta a punta** (prueba 1), sobre una copia hecha con la cláusula (0, 0 y 0) a la que sumé después los scripts de `t1/` y `t2/` que
  usa el lanzador (la cláusula excluye `tanda_final/`), lanzado como la corrida real (en segundo plano, `caffeinate -i … lanzar_t2.py
  --trabajo … --stub --solo-tos-tramo-1 ri_bdp,ri_ieccm --solo-tos-tramo-2 reqcac --git-repo <repo>`): controles previos en OK (78 de 78,
  SDK 0.100.0, sha256 y tope del manifiesto, tramos); el freno OK antes, entre y después; **el control entre tramos OK entre los dos
  tramos**; salida 0, y la copia de trabajo, borrada.
- **Los casos en contra:**
  - prueba 2: con `umbral_errores` en −1 en la copia de las bases del pre-registro, **el control da FRENO y el lanzador para con 11 sin
    arrancar el tramo 2**. Después restauré las bases de la copia (iguales a las del repo);
  - prueba 4: una fila de `corpus_ri_bdp_e1` con el id `claude-haiku-4-5-caso-en-contra` en la copia de la base de E1 → **FRENO antes del
    primer TO**, con `ids_e1: ["claude-haiku-4-5-caso-en-contra"]`, salida 10, sin ningún TO.
- **La pausa** (pruebas 3 y 3b, con `--hora-simulada`): a las 18:00:00 del 23/10, no lanza ningún TO y para con 20; a las 17:59:59, corre
  los tres TOs y sale con 0.
- **Los scripts del cegamiento** sobre la salida sintética de la corrida en seco (`resumen_prueba_seco.txt`: 4.951 unidades, 4.956 con
  partes, sus destinos completos) y sobre la de las pruebas (`resumen_prueba_lanzador.txt`, que atribuye cada «corrida completa» a su TO).
  Los `NO_ABRIR_` los escribieron los scripts y no los abrí; su sha256, en `sha256_no_abrir_de_las_pruebas.txt`, y la vigilancia
  `integridad_e3` en OK.
- **No probé la interrupción manual en vivo:** necesita una espera, y el despacho las prohíbe. El camino está en `correr_to`
  (`except KeyboardInterrupt`).

### 9.3 Cómo se lanza, y la duración y el costo estimados (`estimaciones_t2_t1.py` → `t1/estimaciones/`; tabla 11)

Desde la raíz del repo y en segundo plano; quién lo lanza lo fija el «seguí» de T2:

```
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda_final/t2/lanzar_t2.py --trabajo <carpeta nueva fuera del repo>
```

- **Duración:** los tres lanzamientos de la tanda 1 suman 813,25 min en su `avance_t2.jsonl` (13,5 + 42,78 + 756,97; su FRENO T2 dice
  813,2), 14,83 s por unidad. **Por unidades, las 4.951 de la tanda final son 1.223,8 min (20,4 h)**: 148,6 el tramo 1 y 1.075,3 el
  tramo 2. Por caracteres de la E0 (información), 995,5 min (16,59 h): 183,5 y 812,0. El freno por modelo suma 99 corridas, unos 2,7
  min. Son proyecciones con la tasa de la tanda 1, no mediciones.
- **Costo:** el estimado es USD 104,7498 (106,7505 con la razón de la tanda 1, 1,0191), con un tope de USD 151,5835.

## 10. El sha256 del manifiesto y de la E0 de los 98, para `shasum -a 256 -c`

Está también en `data/experiment/tanda_final/t1/sha256_para_T2.txt` (sha256 `1cd0dd38…`, 499 líneas; `shasum -a 256 -c` da 499 OK).
Desde la raíz del repo: `shasum -a 256 -c data/experiment/tanda_final/t1/sha256_para_T2.txt`.

```
23654ef8a43900b2547c2de6dac3e86f2d29c91d6b380ca4439b102468f63740  data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json
ee3d64eee336d551fb6840274b299826d21893eac6599eecc73119c6458e5bcb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_actgar.json
5d132b538b8e34dda990ca07fdb77b1e877cc8be5cf7fdfc358459891ebb55b6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_adfsp.json
a7aab066dd264a73561465db01a8ea65363fb45f0630f09f2b0477808dbc1609  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_afiltr.json
08fc41a09bf9c7c94cedd59fb8e90df0614ab5e6024c19cb6f2ee617e7dee22a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_apnf.json
48fd07b551dc5daf3a8536313003cb7c497927f3c96ea5b67d1677699a3b34e7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_asomut.json
fac3a3d9fb77dc3e7cbdd2a2f9f950c74934fca50fca66038972961ff02189e7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_autenf.json
51044059bc7ffaeaac0d0db587ef1cd45be53a019965cb7a56f2e9980fd3ae35  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_cateloc.json
2d45b38c2b1f7534a95cd64195fd590ac9da1cefc85931f4aff06873e5be95bf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ccbcra.json
44de44a996ea0bf7453cf3d2ddaabed9c1c1c5e44a46b848a23d251f492fd82a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_cedin.json
3ba47e3cdd684b142caa8129569dc8b29107023325222927a2179f0a5fb15bdd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_cescar.json
815d982359699e9513df85e5d7336835d555e0be00c3320eda369f14e44a0a50  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_coltit.json
c6b39ef9dbb319552c98b379742aca35a113d039149552920b1827e5224998bd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_consyr.json
66ff260d403ebcbec28facaca20944e88465b97c203b0436e05fdda37eb8e433  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_convca.json
da8ce647cadf5d05963fab8e7b82925904ae31524cf84d02a6be2cca103b8d17  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_cryl.json
bdfaa7388b7e1e33554b7e5ba84982b05c4cd7feaf5fb6af1784dbd156233c5b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ctacor.json
e3d636d298daf4e2bfc68f3073ead84342dbd55356e6bdf3ccf5276e2008ce0d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ctavis.json
055b1c4e9d5744c0af5058dd6372933880ea72051cdc1eabe912133ebb7e99f1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_depinv.json
c6effd0271c8547b42d44b6a514ba4051d88df08d27791c353721dfb84c6199e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_disres.json
b21ed26fb8983c8fb75b66d8021842ed12bf4005426f4b1e7bf723d598dd470f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_evacre.json
209041ce1bdb3e435656568e150fa6f2d55d2965170a89fbd45bab53160e3835  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_fabcra.json
80d5bfb435fccc71139bc0bc4b756e6d7b7a48c61b28e7b590b9047e3972a138  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_fclef.json
6e26a12de2eda5425a1eaf8045dc60fdebfec9a9fb560624c348df0022470815  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_fgarcp.json
40bb6e5ba8037bcf9227da391979f2eb28f3d41510a846bf8f28ee8789910581  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_fimipyme.json
af824d1f42fd40dbe65b030cf2059bb1f550c358183ba187b8e7f036a617bcfc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_finsec.json
2dcbddc2cf2e179eb205e4db9c442aa60aaa227eff2eef1e8129e63490644b73  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_garant.json
9bed2d40590c00cca9ee5a817cfcd37d371caf4338e4eef76403c7d7949918cf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_garopt.json
d68b359a535c48a98b35f0950eb69a5eaee2a5a75cd16293218431a5bb5eab9b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_gescre.json
e8d2de9c58d85d35e679491f1c141547c6450c5397fbe51aec8c356df0343225  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_gracre.json
567e39bf36e56c18b0f48a07518d4927bbdb44bc7a0d6725b87f4957aef895c3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_graloc.json
77d4924383e44fe1e665b8d8b78d481c54466bb98642c8c45ee2c90c1b988fcf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_horari.json
a36edc4042e73a8d0597a1f9eda45ce152be36147b6783a558ac59e4ccadd6b2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_icmecma.json
2a2e6a3065bc63f4fa3f343c6bb1baf3178acdd9cc32322228bc6c6362583f03  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_incuca.json
1256c1cde42de4ed3a2e75b7c9b110517005105f3cd6417656654a5b72f19194  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_inspag.json
7be49906bfaa43bb9e00a5347a3ee08613b43817271c32bb6bdb363bbf93ff45  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_jafip.json
2c9821e3dbd879e54fb75df7f92d6ed3a5e558712b2c3ebefca9d350bc30a6ea  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_lavdin.json
e524fcaae7fb31433c3a4e6d1f7104684cc4ad754842b4f3f3e5688a5e299429  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_micemp.json
32edd67c5b8f95f83e4fab38834ecdc2b789848466a8d6a895ce649db75513aa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_opecam.json
8c51a65a2001690b9b189d35ce96960f9047e956f62728d1e682a6cff293b524  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ordcom.json
7c6b2e34587e762e5e16571fdeacc1ce98c5c63c220246141baea05c85a45f65  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_osapsa.json
27126cd89df6a6f945bdb9fd81bbffff95989fc8d61356503392eb6032ce5214  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_pfmipyme.json
3e007ed7f7ad7034c6293d089468eb9c6ad981270372be2e74815e9daf203f84  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_pimf.json
dc687c60e20591d479ce791d7cf9789667efcd323d9e2ab70215635d41494a34  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_pognme.json
d89a4e3ee2710d83b93e97f6e5d315b630d1ac28765f25ffc51d1f91cc00c4de  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_prevmi.json
91a51c1cfe3ab2cf6393e4edf5c394171a39025681dfdc4dcbe0fc56e1178cec  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_pscpp.json
7512662b10f33ae75d2324b6e78a88f3cdd37f962386a1181243487617dad17f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_raapal.json
2d07e564aabd594d2e398d82e85cde80bf22609b9e236d4190c2e1e625150ae3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ratio.json
e583c42d18b0be8081a593cefc187a351b57fed04c6e5b37721fb4ce5fa9e84f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ratiofn.json
e7e6520dbf0394b9f83aa192054aba8fdc6b3ea4d22582f92dc70edffa987031  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_regpri.json
f0b8107d43187d3954883857162dd0a2055ca927dda3212863215bba171a0801  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_relact.json
3b5ee7e85c8a0b0f117ecda4232c7c91e7bf82250e32b61630c23f56872ca693  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_repefe.json
85de7cf61434f2696c8cc565c5740491425dc60c98762147fe344d441569b87c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_reqcac.json
c87fc83efff9e70ca6ba5b21a1528c284bd62bb9117dccbc5dc85e4159589fec  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_retype.json
cd329627a39163c808bcc0e3957657712708196943dcc736ac98f414a2511683  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri2_ci.json
8d6239dc955ecc86042640e29157a3f516dc461c89d09e1f88a2ba9de4e7eea5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_acsf.json
35ca610f5279290123259a75fe4072a5f11baa762450eb3b9229f0d169f6812b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_ai.json
4adbab5f7e5fbf5744cebebce6da0e7303d28609576834c468c1a43dd85a3e9d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_bdp.json
2c08ba6288bde7a452f2f6154015bddcb0e0511dfdc64655a9f91a13a947e0d7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_cr.json
5fc720e82bc1eb5451fec3a30c84452275b58ce68a43ba1bc37a8a8771d9aabc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_dsf.json
8e2489efd26af9aa93b21ae50c027f5de44b5a245c585e40a683d672a9c1196f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_esd.json
9d104f6ba5d457d12d574085606881c4280e0089162f5486886cfc360b3031e0  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_ieccm.json
267cb0588962c09ef02eb4e3cdf01464e08c3ede42ab3f9bb55b284ea12fb988  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_iepsp.json
851505c0952556e81aeb439e612d6c646d6082087ca600c3e717b1412b33d7b5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_iesinap.json
30f8cabac87d10dbfa9a9a5f7fac0c3a0fdef1e53b2bd344b74b7810f047fff6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_ii_31_12_19.json
6d3e4a0b107499ec942197739979b6e642fb7467d46057bca1d0404dfeb73d85  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_laft.json
94d9e297483890c11b1570f7bd33b3ac0718f6934f327b5b15c222a005d5359e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_msrl.json
fa655bdfb5c45aea9d1b6140729bca359d488007ce4bcf4e44bbbe8913107cb1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_nge.json
969ce538d04b70a8a68ac335f0e60d48689014f59b02bd4b8f2a63ff4b0a69cd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_ot.json
44db4ef6415f94be20de1d2c90b6147da480f774e6cb27c34fbec670ac31ad19  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_psp.json
d1b395f8f33a662df636f0c1e52320725179a2e964e8db2be56b5e5c0cd2cf99  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_pspapt.json
9d546d528f5d7b4b6e473784c6abb792daaaa9347d3a47feadf8f09e4f1c76ec  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_rcl.json
4946e322ae49dfdea7732c15156f9ae47bcaf26999c3185af3b26122ffdad150  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_secoexpo.json
04f83257790497f4b950a57de98733468736ebeccda0894a4b965156c1e7c3bb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_sef.json
06b26feca62803d3ac161892045be5e8917b153fbf3dd7f632a8600da168bfa4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_tar.json
6176874c691f70fbb540c43aa96dab4cf0136820c37c808f1c282131c444d860  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_transpa.json
dd454a1e580b20520b96eec2e2d813c8afba40b88f72638cad8735e99b032d1e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_tsa.json
5819b33b117f1b966d8184954e959790bacd320f1d6a63c1984a72e1ac4711fa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ri_tvf.json
80e1ff88e4559aab74c6c1fd888996f739be02a426d188db56a0306264dd76aa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_ribspc.json
7b28265ddcc4c58b250f5dc9f14d8a801a064065899d2bab69b39098fbd01493  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_rmgcti.json
e27be20edb54997b449c7c4eab94132d54096bdf83b048dceaf42e96b2e2eb72  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_rmrtsd.json
38808b17d76bf55a8cd02b60a4190d59f684e1adfa52dbf3337533bd885c7ce3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_rrci.json
287b620c03f6f3143be025915a9d5e097da46beb2df749261dcc26fb20b20351  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_secfin.json
a42ed77fe89418d6682ef52dfac8168618a80da8c868a32a1470f953ff2b4bea  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_seggar.json
9b6f6ddbada626595b005a23a1ea5a9e8215858bc7e96c1346667f3af6d6eae7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_seguef.json
430aecd1e64c0f4559d7e97e02b1d578e351d18e89bfe0974b10a280a7838ca5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_servco.json
ad9068d2f9c51905a0a75c85caebe0ead4b1415f7b5a6cbe52a62b9d7d87bb9f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_atm.json
f743108e8d7e498fd90e4c061a9cdeb76f538940641ab7ed878dac93e5e2c8ab  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_cec.json
72f46c2c29aaca44e5dc96a6675e0afa54c4fc03d1f3cee381c2d8992a9a0ce1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_dd.json
2edc16777cd347a3bcbf7af99dfe947eed5050c23423f0dc67532b29734166bb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_debin.json
7cd1710e37055340cf642b588605d388e1f63897a3646a8a38deeb36cd466a5e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_mep.json
d1ad1f38dfd9f35605e6237a8bbc8798085e386db6f1369d5f73acbd8933c799  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_psp.json
4ff9744a053e072a47cac8becac43f3ea7097a53f801b57d1e6d8f7a17c46b1d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_spd.json
0193bfc619f245e890c60b6cb2295ef5eae8a328dadc4055173a4ef83855583c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_snp_tr_nc.json
88cfb91785bfb133f472b91f45e19195691a44e31a72c0759f1020f93809d37f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_socgar.json
1f382c9167f4aa4befafe4e419c3f1f5172145dc47c821829782d3e41b274d65  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_supcon.json
725cf031bcbe73c61aacc72400e03c36c28dfa6f98aa6b15bb69b63a2319a96d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_tasint.json
a25ac11c4e0ab2f06f6f5f7aea5a07ad5f1970542053c64e242662f389a19f88  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_traval.json
fc5f7873960db674b00efc3ead7bf5a54bb318d9957827707a9103200544d97f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_venliq.json
cfd7b6cd7306e15c0864600af057d8d4ae139205d016c57142b15d0b84be6e84  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/chunks_verac.json
da5f0ba13d5cbeba184dd0cefadb56f0e2fc9871f9ebb3a311ce46d07d3efad9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/cobertura.json
a66fafe83ce15452444e3e3ee8cd98f69258abe790424e6fb9283781905de352  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/conteos.json
228590a02122d690a56208966703193377c26b9c57d3503091e5ff73c5b35af9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/correcciones.json
248df3077873eeee247499c07aca1ffb3531b3d3a3a024010c6eae16f0c399ae  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/divergencias_indice_cuerpo.json
fe1e823ee7021e183451b63e199f2ed385bfc9486769a586ba79d13bd5dfeab1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/encabezados_conservados.json
5cbda45970553482d58d2e09bbdb8d87621fa2fb781024e82171e894b1c0a8db  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_actgar.json
9009888481c83d97fcc420c797ab1cd6751b6c69a933017d8ad19f233cf39a09  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_adfsp.json
c71d198e4560064d784ef147e975c25663b15be62b89d7676268c2868f080c5e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_afiltr.json
8c715f61687c18312ef05ed07e2cb10a47c71c7389cb397719935629c68b5859  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_apnf.json
6b0a0ed4f8a557262918133e8cc45c2e282176e5835a206e245817a803a8ddb3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_asomut.json
1d598fdf92d4ae9e32f4dc756bf009cdffd8d801c1272766d4f4eb651a63e04d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_autenf.json
027f1bfc44f7ef2eccec8aef154aa12cf6fd2b027be9598af65e83dbe9614a26  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_cateloc.json
a5846aa84c25740b74c1c842045dcf18285e73223a9705dcfccf31dfcbad2e86  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ccbcra.json
74ae2e9ca405636625892c9b17eec168d46745405672876a76a6a811754c311a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_cedin.json
b347f6b46fe8b4dab601c7995123e3605dbd4446203bbf8839ec5fbce2fea1b7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_cescar.json
3acb1943e7a7275a78e7edd8b5dc249adc2a8ed7bf762007a9c4f15ebbb079fe  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_coltit.json
1c5f8236aa8a1ce32b9870b08dbe7c3ac33ad0dde0088cb825b7d88a13404e93  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_consyr.json
a12e4cec417ed94bbc4f991abd4574625778cd841d2f25bafda5641dd821ebde  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_convca.json
cfe686ab06bd287e6a7dbd7f67c06511ae83a7f5389b793d3f2250265975c469  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_cryl.json
abb21f6cbf90f5ebc3aa83ffae7a1d7df11d1f70caffacd3c59f5d28f9fc0875  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ctacor.json
c93cf2ac582536777b0ce0e61f33db9c498f8a26a46379df1667b106f8838524  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ctavis.json
d2bf2e92aeed81ff95308d4484c2cc6221e4ad6423c13c1640c5a66f3b6b7efd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_depinv.json
85328481d89123b9073dde5e48b5b049a41df4bb99712968d1a0fe99e092a675  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_disres.json
70eb46710fdff22d29bc61f4b48b6fe3429a87242b8bee2485bad6a768d39747  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_evacre.json
c35b7fdf3ee7f508e9474098a321f7df203402b5423161acc79c91b3464afe40  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_fabcra.json
11f9bfc253b560c3dbf8f00d87d3d43b30f421ce5138f0b7a2bc967f65cec53d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_fclef.json
cf7af7efaf5f70efcc773436558b322ea284dccc32b7678f634042082491ac46  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_fgarcp.json
beac804a5b1c6645a9d19e0a754ff77779a187a97eaee6e8289e86dc11018986  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_fimipyme.json
0842990c2e959d434a95d54777ac474d64f2157efca84ad589cd5f88f706a590  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_finsec.json
7108edecab37676bfea1a039b61dbc6682b961431b054342999ef4cee21beb0b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_garant.json
8896dfbd841333f762a47e7d8347a2748c1f6d27975f7b594d997d4da362c930  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_garopt.json
d992b7b46eff1f0cd44534d8653a1a4d9fbc241117ce7f943af99f51f9dee43b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_gescre.json
864bcc02bc72571ac3735adb3650b0cae371635d2003a5945d77a6204d15ccaf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_gracre.json
95998cd1b7ca5937f10a18c12c8cd23e9ca0172b8e7e64dcf83b9c6936998bf7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_graloc.json
52178dc4c8f4b45cc8e1887a5b556f3f4d25199b5bcefa5ffe17f85636ab241f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_horari.json
acd9d4969f8b8b417af78b2463110befdf4bc12dc211ea56c5ae5a177a2cf0a0  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_icmecma.json
5d6076daf2df3d045c5365ae61a8441772e7f3c1d382ab2e64f355e3a63e1339  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_incuca.json
c3bc4732913dd6e4110b97e475a18fe71414cc98dbe6d55ad6d85865842408f3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_inspag.json
6ccfb909277ef86ddfa350d9ef5e18b485ff3a019bd1d4bad97de5834c6720d7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_jafip.json
c39d79da826fca7f6517a79b9c5e90739410c4cdcfb71fe76ed07831b64fbd52  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_lavdin.json
dd2ebb979b65392c6bee68c0e272cea637d041f3d6f844df46d807e53f95c179  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_micemp.json
dfaef72b84333dbf0411f4a6ae84999ad8695bc38338f23fccb93adb9f035315  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_opecam.json
c8352e918f125d6d86bb90bcddd5d77e573bb79902d433ede785578f7a834966  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ordcom.json
926dd74a93ae3ac9faa91f5dbc46160de541d957c5c2135be3a257a15b6f5aac  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_osapsa.json
9581fa88a304941ecad9e0d1acbfc63d7473de91266d076bd02d9245e1affb06  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_pfmipyme.json
67800f6fbf41ffff207f7c5c496d6d0cbb4684dcf5de997c18969cd0e20b06ff  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_pimf.json
6aa334292d638f45abf223af4185b04d3c08432da716c3e1472a9b622004b3b7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_pognme.json
6c448707f385110c7dbd958f03cc2d0ab23efee24cc43145d0c7940e3cdaee11  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_prevmi.json
273af7419061b3def384aee979682124b6d5af98954bb8f302bcef097797e8ae  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_pscpp.json
53520b5d8ff702af21469601c9f43e54a351607127517e3a33e3590e9aa51cc6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_raapal.json
a5ca297cbc422e9440e662c4e03decb3b6167eb9d751e9167715bc4dc8fe97b9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ratio.json
3ef76dcab58c1fa33dcf363e423f7aede61c774d598b60517808382ba9a7d3e4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ratiofn.json
25140f9b4f583f676efd6e0566048c2b34322c5e729f90e1d157a40ed22f9cc6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_regpri.json
c742e57050d2ab25e916710e479475274055ebbf738ebe6c2dfdd3645b8283bc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_relact.json
e50c754c2f39a200e1f81690548462efa59afbb03da18fe7dd2b7986019c1c97  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_repefe.json
3fbba807f540a98c6c2d949a7f76691c1b9327dacdcc9093e721977f9e695bc8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_reqcac.json
7e45d16316acb4e70c2ab7e908748cf49a06ff460bac94ebcf6dcdf6aa97d4bf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_retype.json
0f8c7f76ef71858f84b0bead3333cc69b311f5aaba5b7db8685df5bc564e4402  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri2_ci.json
1a874461f32c71ce0f2b3a3c27bdc7655e856561a205a98850855cb138fb9bbc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_acsf.json
edf366af8424d140fa87bb7ca437feb28a306be5c6b779e5481a991c51eccaeb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_ai.json
31344e7fb122a0cf4609f3d3cfc5ef3c7f3fcfbbfffc09f5baa6821d19d26875  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_bdp.json
41cf9c16d4510469eccfbdfc07dbb735a6e9bb05f2781528c32a6c764b328dcc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_cr.json
13bef9e73ecac70bb639a714e1977572094d55bdc52d8229173ddd8adce55360  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_dsf.json
983b9bbae9e8155e90158ff9e6e64b8c2325976ec33246ac24b75d80a02c0971  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_esd.json
e9f55a85c7335d9803e44632ce41d8055c86fd0adf79757ed9477c0295883baf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_ieccm.json
f69720bab5ed0da79bce19623b5c58399ac4c4b87c99515fcc5b93876a95cdcb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_iepsp.json
3f7807c503e68cdf011c01abe47003c7f51e0fb0573cfbc7ce7efe394362eef4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_iesinap.json
65cd5683c63fefdc618dca4037d4be029f56d6944782c13dd62b16f089098a44  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_ii_31_12_19.json
f680e7683e0b9b40c4da26f11ae23dbe1cd488d2271eeb104f60d530ab747cfd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_laft.json
8cfa0a2df53c419ab3a6b820b1d0b4501c194ce1ff7ae10ed276e05107f7c6d2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_msrl.json
e8c57ee30b53e261efa42b08a53f74807245be0976a57b95e0632ccd193ba57c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_nge.json
9db4508d6550033e79b073823a6b4ceedc56470eec7288c4fab7402e1b1d6b84  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_ot.json
79518e53b459b84aebc1c26a12da7130d4d6120ebffa6c0c4f09c207bcdcc1f6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_psp.json
86de3b8794831ffd1558876fe217559fcf4e2caa88607a2dd5eb6711d5700f3f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_pspapt.json
d01211f42105c4d8e1af839b2146aa141f85a23609440f1cac09a691ceae6d14  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_rcl.json
5c61e60cf91692f3120f4ef1bdad122af02fe33c846567bd08513fbc0c4a5b66  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_secoexpo.json
235006c9325d2937c2d97cee9dd1cb0a4711826cb16d84b3f0a65aed9db55341  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_sef.json
55af8dfe8ca0e860f6a440c532bb580240160ccd8f660dec0ef63864dede6269  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_tar.json
954f95947865a8989c149d9a8e538760a078048d9f757a828984966fa4d662bc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_transpa.json
a5614121e0f0d4d6b9a937ba4a2d2e4181acba46a3346dfe35084b3cd5619a5d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_tsa.json
858b22b5dde19094bac7459d3c594f007974ea43880574a7e83fdb19d659611d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ri_tvf.json
7555440908648621b1c73abbfd38bea3da204cabe25c859920b71e7152d86322  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_ribspc.json
7728dfadd2ba26d48cc099c0f576c335b8c2930377cc2b3ab71bbb244f0e0675  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_rmgcti.json
425d112c461d5083c465c74389a588b731457e4d67b7b979308289fd7d7a8b5c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_rmrtsd.json
df2a97098ca66de6ebf46727b543d885ee2cb0c5a9ac57126d938aa943ea900c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_rrci.json
fb58592b75c247b540370b770771524df0c0c0b80ade9de2cf6b92ae2bd38a8a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_secfin.json
014b49c2478ade09935387d07dd68ec61bd266c1ca9c1016dbd7be89b74398c1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_seggar.json
b1bc23dc80460fd1ee5728f8e970861dab8ff967ee703f1ae3b992c41007f805  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_seguef.json
959f29d5ef94358c902ea2ffbd3dad25c4f11f0492b1339d0533a7de6bd3042d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_servco.json
d84965ac47f2156753ecd0ca5ab1633bfa774f78c8b518568b3b6ea03b5b5101  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_atm.json
1b3c1beb34ae6db807e077fd2249ae5d92abc765a40392fb2e3c308450ff855f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_cec.json
0e5f7deb845542abb992e596e7e4086885d4d8f3ee9801b5b5335dfb19e4b347  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_dd.json
6c486da944012370b48782aeea90f058a546b349a6bf9ac83547b98b5821052e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_debin.json
34e1ee8fe1876d8ff8ce6690cfa351f0d4077ec186e8bf23a3228c4ce50cd4c9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_mep.json
4e7910fc7bdcead400a89c31f67a56ee21d4079e539d146e79438de815e01c3f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_psp.json
0468c34a022b7ae88893d485764e2204a30a3e4e25f1de0611b5eee768ed9f94  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_spd.json
0c423fb87c01063b3ab230bfe2206c2def9205b155c81959bf6ff244a9cc38d7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_snp_tr_nc.json
19eb2e9c179eac0a45f03903f63e5f7e42156131a247f966c2582f76383e68a4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_socgar.json
2327a714289dc03791c040b6075961849cfa572a5ee9b917dae7083df4092fb8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_supcon.json
0c1e25e6498adafdab05a513846e6b38ddfe7799be33768d9e6fdbbfb3293cd7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_tasint.json
a55afe3401b323d47d30f697f60863da29ee67cf1e0c7f2f4bb02002bd412078  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_traval.json
f78ff814b0fd01e52006582a5ca754f3aef751a26b4086e5e3d5473a3b7450ef  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_venliq.json
996d74a81d41929b1370e80cdf5b6c40c217d358d69fc1ea969bfb899d6763c4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/estructura_verac.json
e3df9784cd3cb2e6ee18c2da65e177aed8bbfb96d2266231e4de5541645f6d56  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/ids_desambiguados.json
3f450bb70161471a6f535d34b660aa58fcbf1df284bb9e1d40420165a0208144  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_actgar.json
f8fc8a2c7b95ea91c8e478c9df2f1d69cf8f9af2e80f4b8e5df978486be42902  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_adfsp.json
926c8a072e6d05fcde7937247d50d3acecbe3eead2e813e8e62fe43c8887bebb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_afiltr.json
d882be2a089e5ea7c27d9164108f62261956689813d6b7872b4cecb55a97c035  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_apnf.json
1e1486785d9b30fffd6ffecbd6aa4582e2d6625a61cc5c3c23062089ba685e45  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_asomut.json
e070db53ef803350228c2c6ce4c13dd5b1826fb638bc8e84d4676af17874e41e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_autenf.json
2a250bff274860bf4a36a459045ad150c1e869eb1a9034c14579676097ab44fd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_cateloc.json
8859ab3dfee578425f165af37fc59eac93e4f60fe6d1cb00440bff93059ffe40  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ccbcra.json
e91b14ad5af8c685e034f543747c91bce379769a39b82439ebf23f5e54ecda1e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_cedin.json
eb0a600eb97ab1f2e6320bf1200eb8b333743730ae2774408dda6158705be38b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_cescar.json
696833bbaf1b0ac441d28aacb747210a57bbc5e13f2de4a39855d18326b0c219  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_coltit.json
63674cddeb58e03bca02cd641f2343c2f3747b6c288ffeb562e6a3ebc033030d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_consyr.json
79d762556614e83c3c90aa534f564af72f3582ea79094a268fdb9c05de9c1232  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_convca.json
2ef7763d25d21d5b9617562c577fa08bc758f51bdf2c71af0dbd1c410f1c9e55  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_cryl.json
3edc40fdb7950cfd05a566be862045c9cb3be03953f88f63a9c1fd520ae76e6c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ctacor.json
b3238757c4965b27d4c3656c03ff9c2af513dde5a3760acf1b61b1e498b0714a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ctavis.json
a2b5b17f11fe8e94ece940fa1f3a262a3cfec967145b27f037941d7d553f4ba8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_depinv.json
c142a9e691f9758029bae275e486adb1687efa36fe1406a1f78a33c85b48f988  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_disres.json
80e4a598a6c615d7e72aedb684b0d9d9e5d2c60824768ca5915e043a18a3c644  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_evacre.json
efbfa81333d5b2d1ec22e88e654a1c160441d63525ef177586bfafa91bff7e81  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_fabcra.json
81e545c0dd633937701120c20f9646ed909347ce97e294a4be9c9391bb2ec703  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_fclef.json
b12b5105cf4c9a47e86c91c12b557b82d8ef033049836eda41fa1ab8a958f97d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_fgarcp.json
d779842a09fd2d8f1a42a99d760a75ccf4fcc408bab185e5ca3fb2c40830e780  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_fimipyme.json
f220204fc900e9475a14f3dd1fe14c196f152f3a2c32e08549f07dd1f69abe3c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_finsec.json
e3ab0485c2886ab953b886689366e0517ee45ccca696c8afde5da87d9454c95d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_garant.json
f6a4d633d4cbb7bf9e58da846dbbae2e67782cf9c1369ef8bc34a10a44398d62  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_garopt.json
9b6a414a06a4d8b3586652f9154206e33ef78a4ec1b2ab31bbb5cf981401f4fa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_gescre.json
eb861c4a221a3b6dfda19a87230a16d5fa0c104d112190f792a4fe778fbf89dc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_gracre.json
63dbc1dd167b0308972c758efb59cd1fcb5a93dd2204c8d9732c0f28148c8719  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_graloc.json
b4c16281b43dd2ea1cf2835e7bebad8508452104827dff34e5523169c6ea7115  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_horari.json
3a86a5086adf497df8f8fa6fbf9ad52f87b44b44bf40af739b3977b667392d73  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_icmecma.json
722b9d95577d3fd4d3acb4a0307b15d46873ea224ff43db3e031e63135f5d357  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_incuca.json
2b40cc21b6c56cf65af30dd69a7f985ebf98575461100882c37ca66acb04e7b2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_inspag.json
0445b63afaf97bfa920b94d1b6a2fab17d178df3b816315aaab5e9d083dae87c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_jafip.json
74b0fef5d5cb7141a937f22f2a53aa2a1a087744d59e2fa8006558fa5f5696b9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_lavdin.json
9cc18393d7f2dc48fcb1fc24914ff204ff8c6e80b71e5f946c4831bb3143c300  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_micemp.json
b9947cdcf53827093888759208d7d89d8926796bac712ae3d79aa9a95783ee66  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_opecam.json
91949783ec5014ed0b8a32e0ceb1781d228bdc4ee4f7dc1810961ed3bd231bef  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ordcom.json
91483eedae2163bf9751b0d50fb7b22f4ecf3f1fc4517e00d51759aaf7721c5a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_osapsa.json
f701ca79568b362d5f1506ec2859d1ad97f812fae462eddc9bbd9e43c404482d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_pfmipyme.json
551fbeba9209b76d6317ef0cc729f35b3acbd2c2f9c3bb3be8e428bb4492570b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_pimf.json
0ad24008ed75b229ac955780de0a214f6f012316a3bca62953fedfe12d77c2aa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_pognme.json
c78aea5d3ead7e94f1b638e79d7cfaacd46d2e429930f75820bdf22f6a6d4dfb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_prevmi.json
20f55d463fb0abe87ad6fcb52430bce5adc93fe99771ecf429a126b524c097f7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_pscpp.json
74a3dc8db6e59f49a150ccc0801edaa8697a31491597e5b1b2017f303b6f2920  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_raapal.json
3426e85abff7908f5eb9f9d4e4309ed7b47bbdf507c56adc6aaf485d2e5551ee  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ratio.json
062a38e0b62faa9edfede2b8e338d055bdf532bea1b0c28a937b2f61eb41fe70  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ratiofn.json
9ca0ac7adc90fbe9df3f3fcfe0cc3a9c1a0bd74d4b1390587e3eb868329c9e1c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_regpri.json
22ecbcf04def103e82ba6123bedc621ccc1e0ada2f1f01f013f0a0f023779b9e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_relact.json
f604b29c29a0acc93d4891effea800bad11e7258bd9bac00c5b41be60b3228ce  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_repefe.json
2777c523dfcf3f0896eaf00c6ae0f4d2a7cbb270cbb41559f7aab48abfcb0c12  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_reqcac.json
ade5bb14e22100a82cea58ac8f17a293fe2a72882ee7c0ea435ae1598036b839  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_retype.json
b403f8f8e01f0ff134bdfbbd0dbcbec9651c9c9762d9d7132615271a56dd06c5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri2_ci.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_acsf.json
87034f7eaba8d32b32a2cd598945a875db16f7343cc18f74cb4b255ad16642e7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_ai.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_bdp.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_cr.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_dsf.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_esd.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_ieccm.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_iepsp.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_iesinap.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_ii_31_12_19.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_laft.json
0a9a06577b52731f1cc4d756d8d670859763b31bcae608c460dacacd7c7d6f8b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_msrl.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_nge.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_ot.json
e5620a458c6388db7fad907112039ddb9ff30fdb32110605ede91b1423692637  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_psp.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_pspapt.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_rcl.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_secoexpo.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_sef.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_tar.json
23473ee9c360ef0712a87a805078589d58e42b11b1ba85d663e26e43ca6d4321  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_transpa.json
e6ad904900c66426c7534964d8619ec63e6c564d00ea5946c64221627143e9e8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_tsa.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ri_tvf.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_ribspc.json
e9adf0d4142d2ecc7620712537ed04336a66dc9dae7f042ce867820d6a1cbb2b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_rmgcti.json
219b3e2e1dd13c3c82b4810bf32e327f111a5958f08845adbdf6bfa5d15c3cda  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_rmrtsd.json
63266022a38042f628ffdc280166f2fb77f0037b86b16d5595a4eb87d73cbedf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_rrci.json
320f253e906caa65aa87eb5037363b9ebb3f68e37fbdb08f0d4f6a220686f2dc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_secfin.json
c06058e3ae05512fb796214c6bd8aadd37be4fd750d8d3d24fdcef56e0a04af3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_seggar.json
310ee4a2ceb6f108e60f8aef4b3cadd00d6ff177cc210a528c25847156c63ff5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_seguef.json
8ae46211e0f7f3b6cb5c4583f9f5057a2936ff7ec5220ec212ac927e47083b93  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_servco.json
20e91d694945a71ba68ce8cacc4a0fc8ebec25359f1fa34c14fa481137d233a4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_atm.json
6585726de7520d8c0e35a2f2a1ea001e2efb2b866be1bec743f7a02d70e7ed15  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_cec.json
71716a98bcf477489f95f771c0dfa98395f81566335b90f84ae54f92716ae540  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_dd.json
0d39c665a367a3b5cbcebe232526d21f673284277490d1b4fee038c7357fe090  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_debin.json
8fc3c5e5965a178aa6fcae76f0936b0761313f0294d30bb4e1c083f76f40a0c3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_mep.json
68a7a50956f8f92254c480d10e58aeb0c7a6ede5db27221487480eff690f08bf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_psp.json
5fba78e0326ecc8eadff68dce56081f61b110aea6d248f76dc061705f0f0e024  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_spd.json
a9004a7e260bb697d4ded9b18ad2caf071038c360180029b2da92b2a7b74881c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_snp_tr_nc.json
7074e8769d1fd39041c382ba03bc5225de3c72d33e9aee1f3bf6206ed4338341  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_socgar.json
8cffb17b9827ded3d957cdd6d6ab1adbe91fc01137c5aeaf2357966c171d70a4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_supcon.json
38aadbfe8330b0d92b74fc0fdf421a9bfb19b1f4c2f781d0177ffc39cfb7732f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_tasint.json
696517ef73cd84b053f44c790455bd6c2feb833d65eacfa943da35b95f482462  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_traval.json
aed9fd5301451ff8f6530a97ed558db484d6a83ba6bdd8069a46b7ed018ac4a5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_venliq.json
8f62b8e158b43a7a9e29c9261b6bfc2f3a4fe17ef2db13f23a1bc679e04dc302  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/indice_verac.json
222a27268886ed3149533ed88e88dfc168b4ca42d5fcf297e07c3f0f0c83e092  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_actgar.json
6bd227fb42438c1ccf58d7a47186ef96e01c60aadef72c3fa85f9976599c5c1b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_adfsp.json
f2376e9b592c3ef6d146c91d0851be28345b3c68effa069c453adf71300614eb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_afiltr.json
9feb582099392ab848d005d5f37f62af4a979e4f954415b683752f35a05f8c7a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_apnf.json
f9c6bbb397311fe76d69bd1bcfeaf7a73802519f3e8ba45a5e946d385f1ea55e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_asomut.json
1baedb4405f38ce82159af81e8809ebbe17a605a51d8756d921296e02c061d5e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_autenf.json
658e5c1c87d498fbf109a74cfd2fbbe11fda2f64f811aa47ffc7d0c2cff6bdc6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_cateloc.json
15f41589144103196c4da74cb12ba524f2cf05eaa7c5809d4888fd9c31e18e21  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ccbcra.json
7e932b88f6f6ac722c173d86a17bc772712e77c70b82e732f497b7a11974af40  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_cedin.json
866a2c20aacb25c36bd3f500770a92701b71a57d580089eed1ad1d92f9cc0fda  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_cescar.json
b8d47ba22378ca444023269ac35d567951e6d0ab90f0ceebb90221f6b9f25c2b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_coltit.json
618f99047739965d77cb3b8cee859597dc694555662bc661119301a4198459be  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_consyr.json
d25aff16cfa2f5f790682c37a57127285d9ee139ecd5c52a05308910bd51db3e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_convca.json
a4f14933a904f48358d586fe9c82ed25e0a1ae770c0a272074c9a87156dde329  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_cryl.json
f1bdf21913ef6887637940c99fecac8ce3f2c6e0cf19d8ad08ebb7ef4ce0261c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ctacor.json
340166aacd2854e0bc9ade970bb815b494289772335b053ff8481b21328310f8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ctavis.json
0a0684513158d15aa255c02909645f55697a5d5cc88c6ea8649aa07b54e9e805  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_depinv.json
f7dd6dd2c8a2d90441a1178e7c1fe5fb4235ef19c7f9b3c5cfec745d225a774f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_disres.json
22339dcbdb091740995a02b2f3c030244e54da88416fe3d49494d860a9b44c95  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_evacre.json
abd982cfbecebcb88e637ee65666c688e0b05e36cfcfc9455a0575d20ed50938  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_fabcra.json
3357513a592786dc65d45c86d1cb9e85059c58409fbd6e8dd188d88e4bc2dd27  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_fclef.json
c1aa86e9ca8149bf425eb7bf048b913bb619fb6955acf55dee0a491185f461b0  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_fgarcp.json
048c8d510a433b7e95a0cdfad5830fcf4f7c6a7896dad1f6bafead92f02d8599  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_fimipyme.json
ec5043a09c6361f61d1f3c29dd3e1a9e37ee4ff78672e62ecf300ad0536b7227  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_finsec.json
d71d6efa85ead37b0bf3ed7cb0297f120ad156ccfaefab56a48aeb85a41f1912  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_garant.json
344a476623120360be0308dc60e43352b34495aeda58737fedd3ed5ecfff8854  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_garopt.json
4003f9bc82aa5038b06914e25645ff6af8d25e546077e04cf05f59c404a52cc3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_gescre.json
e4e0f3ec8c4bd2c7cea15f5dad06a1a79a11c61fcaf4e8601f96147dfbd9df47  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_gracre.json
122369c795ddb2b9af0ca24762f6d48e62ef631851c5fd5a6c9a984dcfe3104e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_graloc.json
c1b893e16ac87de1a235b20e690c48294adb538cadfa9e776936d1fd6f9c2bfd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_horari.json
8ed8104208bc3ae5cdef8299f4cd70f2e1d5806b4b0e3c69c46dfb2ccd9654f5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_icmecma.json
13cbf8e1e1acb01a8bc391ddabdd03d34879b4c37c80b54b63ccfdfe3fade12d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_incuca.json
205e68865b1b178d67b82b93b8468576abae447a8cf5e42d61ec589c47d83015  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_inspag.json
9afc2861676ff00e385af68f2492324325801a263fe9475aadfe9152361b0370  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_jafip.json
9df7dc5d5bddf3c28988184741acc7d49f8901b6d2442cc8b5aa8bc10a497616  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_lavdin.json
5e6723ae93535e8c02f3972cac34ecce06719983c12a1e8bcff3afb3851626f3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_micemp.json
f72c5d2c1b3aab57804e734c048b7b55f9b5198eb5ff5992cb4b91d6e3f9e0d5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_opecam.json
ad6ff5f47bafea6c9b220bf164cb0f400acdf49c892ac7ddfb1c22033d48144a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ordcom.json
03dced38ba23bc583fae8ea0e65e50792929be253f932764d72222b49711f6bd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_osapsa.json
4a42752a1a159d7fb451c1a6a4274025b2e425d5ece9479ec2d20ba3a3516327  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_pfmipyme.json
25821b9698ba0414de7c371ac359358a781959541b54dd0d8798d8d9e1cb79c6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_pimf.json
96c32119533b42f8a491558a7e253e7744abe14f3659b4465db8633e0a8dbebf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_pognme.json
ccd422e686439bf0ff84dddf6cbf64c5bc69d47b59c929ece25d298cb97155e1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_prevmi.json
a243753057d2baa60d788b54481467c1b09ef490ee408c60b3fe5a2a9b336e3e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_pscpp.json
dc62526d2ac9692f00c00408fb541d6ea3a9f15e76b6f688db922a88d11be954  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_raapal.json
2867e82b45a2997f8a8250a58c0d86b906e0ac0f64449c7058b38d2a7cc98ce7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ratio.json
6dea4bc6b90fe6c1a85a060b46ad1750622daeecba2581f3d6ed58c2ae6805ab  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ratiofn.json
19efbe87ec032fd976f46a0b86f1a96d28681ee380ca8c19b2df95fd9848278c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_regpri.json
107a46fc4edbd9d0a8a4fab197ea86c7854e14603568263d10e8232db8ba9eda  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_relact.json
fa265f897e7b42d44022d667512afd32a7576a17bbcf2ae4ee621a8c134d0aa3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_repefe.json
822bbf25aaed35ed0e844c5a995415187849665782133c99c3a4fd4983c973c6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_reqcac.json
1e942e2d634ee9e6f913894a24f8f4bd56211d6eab10cde509870668c4fedb87  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_retype.json
9403416c50174cc9370c9c41eefaf2444faf64ede5495fe9bd8df1254abb20c6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri2_ci.json
44fda9ee296eea1123d2e6fccddd8a250ea6342f0064f851c7d67c40305ffc38  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_acsf.json
65f95f96c01a20d6268838ccec915b6e6ea66f5c3c55ca893e386da5d02d7d87  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_ai.json
918642572774f8c1c76b19b1a2a96b8101fd47cbc7ec028b3eaa88eb2c2818c9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_bdp.json
a8cc6e47cab7d95ded6d1b74c57f31dcdcdf4d9a9c3e797f2c2b8418eaaf555e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_cr.json
d35f3a46a85c5c0028bd0173c275f94b57d49ce0423823aa891d5ac72633ded3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_dsf.json
b1783b8688634d7fb1b1111163be6ae71f845ef8f3d533651d12641853ab2122  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_esd.json
d28eb6de48825dec9748e3ad70d6e66b9736492ae01abcde2eaf803bd7af1150  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_ieccm.json
109b2969eef089145a834b346abed2485772b4f89b7157b4e322f632e3022e81  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_iepsp.json
97e05666d181c48d0a032a940963e77d89c92e992fe28e352a280d8112bcfcaa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_iesinap.json
ff382b255026a4b358d5f1299ade0f2861286009e6aeaf33e8e2496562576a0c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_ii_31_12_19.json
f92851be8b4586acef9f49ea1008fe7a8d258f8da51614802f926f86ff9a824c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_laft.json
71e540be81f9f0974f7f7e46204875676e88af14d26bd8e981a6f59ee5465cf3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_msrl.json
7c7c12f7d6125e5dc6fe1bb6e9f314bfc5f81503fa93f671433c948338150a8f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_nge.json
9e3705b32720e159ac11fd755fd7b035176941a2236f63bd94db1dc35b4df7a0  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_ot.json
323b3bebc54fa2d79ba3ede0995ee7c3065294fecf742b11d3c36828ee2d8c04  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_psp.json
49334b4c7a62a5cc34825ed56b71e7692d6844bb8fa51722bb244e427b6e5a95  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_pspapt.json
e665a14f9398ad9a7b5cb75511d8b93427e36debdc130e8dec77417d87f95f88  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_rcl.json
e18095267d54c5ea0b7a251c9722624238126b4c3962c75d68bf89065f7621af  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_secoexpo.json
a9830bcad7e15b709dcd8c15a9d7274d7e1a1991c953fda4b80b48804d599905  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_sef.json
97bddabc6cbfe0326922c43375014410a9c7e97461d65e8bea82de1d8340ac94  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_tar.json
4b223f59b0180daceaac41bee528646942cd70cb27c322867f3f505d84128676  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_transpa.json
f2aa25f869ecd6c9a9dcfd391e4b56bf5d86de11a995fa0f232be468f0ca2bcd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_tsa.json
753b4b4afbc734b0de224c261f6d49da229c08cb371396d35175cdea171daf6c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ri_tvf.json
9dea649ed6865eaa6460981b70cbc3b18589456a818e5bd4eecd875a45400e93  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_ribspc.json
6b27074162d05156cffacb7366347c0b7a13bd94a45c9b9e1ff3cbfafd5e3062  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_rmgcti.json
3ae24dffdfaeeb0158510fa374fe5001570e70565068e7a0615d52fc5514d188  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_rmrtsd.json
f32c2f36cc703ceb5f948f3721eff9321f3efa6e2b3a7c7c041c50f7566e70e2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_rrci.json
ead66f6eec43dd87ec706a92ac717b0983111fbbe45adb07ddf6080c5698a272  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_secfin.json
7f16a2d0f11be80e558009b6725ce2a04322c7374e3f5907f2236aa0d3ca7d5d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_seggar.json
905f0a49089c4eac2dbe7e84e3536e997ee1b05fc129ad448c3d94ad0ef85557  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_seguef.json
59b87ac4334589a95537a5c4ec1691325309af63a0beb152a449075f13632866  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_servco.json
dad0bbfbff8342371a135a59d5e63f522facf22c6a556d8153c1384b64cd5573  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_atm.json
d9648c58ac24c8a0c33407aeea05ed8bd4c058dc14e95c5e6baabea4f76ff97b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_cec.json
25b1440591f7d990b20b42b4a3156003b1781026224080f2273e323589c2761b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_dd.json
523adb040063376df11582a3ca8c76537bb71556379772c4be2c638234c1f447  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_debin.json
3c8ad471530643472ac860f9bc8a2a41272825333b48a8df933355d0effd80b5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_mep.json
0b2a5b9afa8d43f1b41f36400474adceb2c2ef3cb125c6a33218853abf5dccf8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_psp.json
182a5dc202430993790eb299f719dbde1148560164aaacfc3ee6009694b4315b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_spd.json
6e750fe5220fe9952365593ca55ac3cc295d1ebe10cc7f2e228ba954ad4765c8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_snp_tr_nc.json
2ae987c31d7cc482a37298f8992a492efb2cb8fbe9e1dedc8a2f48f141b05a80  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_socgar.json
11255d5f9d62f411620ff02f7be325ef3104fbf828ec1c575035f0d292a4e9c7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_supcon.json
d2223cb6e6683030c36b5c69ea7160f1420e0719dfc4c6265a7af54aeab2b6e6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_tasint.json
59bca72b1dfab55ffdc80882dea222c44afeb5601d4ce9a552d5d11e3cf83ed6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_traval.json
d7a345830507fc03d996cd32646106464744e5511216b32d94c99a7cb713a2fa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_venliq.json
85dabfbab299dfdddcdcf631e4cdfec4518914062f7c5eaf764d6dc851d07901  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/pies_verac.json
f31d9e268f54ec18e6fe60d70b3699bf7e192a545d5abcbbd6569a9b4b36871c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/sub_chunking.json
f9e0143ef903da83f5881c89e18ea468380341b97a182891882a35856b0556cd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_actgar.json
da3770f5672fb15771e66481c89490a8ad99045908f1e02d5e29c4b36412d127  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_adfsp.json
601e3c9de902999036945ae0a121bbff2ecca82e60e959ac07772fad8905918d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_afiltr.json
bbd43b65f242472bedaf4c76801626f021370862992d0f8fcbf2093a5b69b400  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_apnf.json
b3b1e41037f9e56287239d20dce11895bec10bdabe3d9eb0fcbc32d9dcc7824c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_asomut.json
36142b6abb992867d31b12690c4f4d4c8ea4f2045a579de35be90cf3e7103e55  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_autenf.json
e74bd3a295890520591be2eb5a7da255a2c34f0932679b1fff27ebe0a3254058  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_cateloc.json
c9f16a5f8bd6c3aafeae893b8fc3c5d47cf9042977e4d5761192d423306d6503  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ccbcra.json
8a30bd98c8c54656f6d120ced57c62d05879b181a53d811715f718c3a983ca0e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_cedin.json
52602573d9d604a1cf5c1cb785a4e30991477d1ec59c4d2fc3d0c2411571037f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_cescar.json
ed72252cc6be048e39db07feb3de7c3a4b4bd36816db4459a39abf64de562df5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_coltit.json
e7e7e12a1c9afa42cc8512a3926635380234702c08f78e336ca0a7745c43a7c8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_consyr.json
1be929bb097c42fb7f9686970075f93b64e9125ef5fe99c949e19d866b7cb4ac  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_convca.json
6a2acf241de7b08a86c19909c32081a5647204ded89c0b22b591787af754c905  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_cryl.json
40110bf082905b9e466ed52f28d8adaeeefd26bcae54e9633480f503806ffeb8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ctacor.json
7508e4f1abaf03d917c2220806fecfb73db966b55a0788e403889af0c49b0d7c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ctavis.json
a7b2bdb3433ac9dba08846b7a8dd435a42c5fc2b07e0f0f74512b117e09bf46d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_depinv.json
4fa893376a0af7eaf3ab3c27cb6fc379ca66e267e24b3256bec64fbf8592e229  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_disres.json
ddab737553b8a1bc50245ea3835b954226c8304bff2f836bb092e59739db81f5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_evacre.json
7ec45ee264ffdb7e91984cf190e9e90dce2fc1ad20ae526fff8d4b5d3cff1aec  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_fabcra.json
f71f8b952a9441e04336d7587a6cffe7bce1bfcbbb487d1b09c1a15c87b72c03  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_fclef.json
b9ee96f4889daa4763f817f3b063b418a9b2e86850edd52ddf2b3ce5403c6028  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_fgarcp.json
db48e30e9aa485053378292777f33c4dbb382f110f9d429d1b5bbb325642e00a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_fimipyme.json
af1e7a52ceeb90151b9fc47c8cb56ab5979bbe80480315e7823c2e4cf8e01c05  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_finsec.json
0851c0b746d7a9a7e7cc2454c2c491cbfab3be1945666cdc4155f92b56596ac3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_garant.json
5381eb02ff509137f49defb8489e25a474de22c028d300b458e2f765ba290d05  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_garopt.json
66a1c7cd27927514507be94d8b6a50fc757911a11eddea36fb5c218977590454  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_gescre.json
e697ab1f12e72b1da5b9e93683955924cade314d2b6952e5b17d6fe0d6a27fe3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_gracre.json
9ef2b6691d636423438668116fc1c24b680d44e28c716a58969295ac0dc96e84  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_graloc.json
9b4950c2f8e9ce2c5878afdfa15d0bd1a771dfa9d53f679d8070e98c6ca0403f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_horari.json
1ae2780a2e8972c9af5d16507fe05c72eb372337ae53317e969720e6196b8f2f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_icmecma.json
e0161da437f3fd2cc0bacc738f3373133a78a1b150c464d804cd29da6728fb7c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_incuca.json
90f6030a919882fa783935d1d19399bb16562a08183159e0e1a7d961c2d8635c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_inspag.json
3a4e425fdc8388b5ffc0c25b4357afd0da0b361eeaba9d2a9df903931a6b7954  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_jafip.json
0352363052838455c4e65336d7faa47e4fc9fae4c907eedcd70bc518cc4d4b54  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_lavdin.json
8766bd97fa054cab17478582572e7a451df61a1f90e4b33fccf0aa575e656fed  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_micemp.json
d477ef498d40b4e6732ec15ec95e996671fca2687a1e96d8a396e12c8d07fc9b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_opecam.json
ac04803a66267a9b1ebaf23d47956dcf5b4a6a1c7a909498e39797b7703522a8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ordcom.json
85327d4c7fa62777d5fb8fcc2e5e0d25df11ce66861e99098e959b2a630552d7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_osapsa.json
719da5c9da7419bfcd15ec7c1144d345998eb79ace2f43436d5326e8818c1ae6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_pfmipyme.json
f16e6b1c2ad8a6a464d433535515b2d159a3d880a8394857be97fc8b1afd3e0f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_pimf.json
4ee1c7bd74236204d35dac0f84344eeee9ea2fdc1e9528378887d78d07e8c773  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_pognme.json
6508e9bd273240a3e0496fdd279265ab318e35b3b52f5a3f4dc640dd17a8fc14  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_prevmi.json
45cc4bdf79526b8b79a3b4fa52717f98c488e5018dc30826851fc83191f1ed2a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_pscpp.json
264cbae62acc6540ee8a2a4c46b76502416dee03637d7ea64a5e1f936b96c099  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_raapal.json
7a29c7347784c41ac62db6b6f058d9f57e2e88c669db24a9c888e413ba0e500a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ratio.json
c8b63e079da480c80d81eec728c6f301de9b725f7138daccee093024be38b9c9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ratiofn.json
f9bce8632ebbbb225a7cb4e77c7e1d4f1062015ae5500f70c16249cf2d7a0309  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_regpri.json
87d2a66e5b2aeb233e61850af9c3a580a10c0d2af790a5464c683d361eac9f08  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_relact.json
4fa35c9a61abc221b69635ff2417ac77b97ff6b0f8dadfab407ff647da4fff7d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_repefe.json
1876ab64b61ffd3ae676a3671921743e896a09df18d6ae647ca7c4341f6af919  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_reqcac.json
b76eff63970454280d3b70498f27f918cb1b6cf684442a52d0f7a86357009cb4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_retype.json
9d4b670d64972649809f147d2d53925528917cbb1fd96cca6d3d5fe4d3e52b82  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri2_ci.json
3136aa9bd58ebe2398c199c08fb72f93644520832528b6137642519ba10aeb9c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_acsf.json
6fd82f333eb395f7745ff43a416e270118a985a14cf191ec8f0984a0deaa551c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_ai.json
249289885b4c0e2ee2360434939257bb2307ddd1d296111832591f7cd41b5de4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_bdp.json
48abdb6411ed93ca317acc4d09cbe20897bc19acc7feaf4b43b520753c560319  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_cr.json
e24daa2f632c5b7ffecae706ba10475d01ce926a6cdbcaff08eecdc5bb1480db  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_dsf.json
127e901045605c0b51d20ac20a06dad4cc6bd6068482c2df448e625e205818bf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_esd.json
24bf41024e4d6d876db9eb50978aade2923441d40bcd2e8f4a15cd73ebf65204  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_ieccm.json
aa82fefd3c397419c9882563faa94ae2505518299252554521d725217602c7a1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_iepsp.json
df51dd038f6cca82ecacf78c13df320966ef1ca27ea907c5637463222bb3e924  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_iesinap.json
92a92d13c0693a773ea4621542547684f214be29c4f4bb3303a5a7449501a96b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_ii_31_12_19.json
dfe641bede159aa5d9ceb0dab7c81e02416f353cb53856af9d6cc038e156b37f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_laft.json
b9e0f38586b895f7c1832dcf652eb569a8993723d3ca60431c5b9eb5a3479087  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_msrl.json
91e3a2e974c6640b4f2516a15891ed853acc11f95e91dcfd909afa046be61a2b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_nge.json
ede3986dbcd96210483f79214e1b4830b2c9227ac3c43dcd6d0ac6a16423dcb1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_ot.json
7d32c220d693c50e25851f669156878ef1d4bb504d848d215d176cdf0880e154  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_psp.json
45464c1f27bc6c1412bb4c8696bc22eb18924dc409500c130cbb12ac325b85e9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_pspapt.json
37f755d31875127afae69bdd26d4e50028a8e5806672ddf290ec4d0245e093bb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_rcl.json
aa21c4729266d7e900a71e9120243dfbfbbf3d0219d0ad4ca3e5b2985910309b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_secoexpo.json
223453c11308ad7d682212fadf2b794d779dd8f5eed716b4e37d19cf1dad0a99  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_sef.json
41a90714602141fe030194276cdc813a94b5688b81abbc0040fe501631f366dc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_tar.json
5818e5270953206d6f9307cbb72e0345c0b668eef0a516a0be8dabea16ab10ea  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_transpa.json
4a21fc90d5e3ed1a4f1831f1cc4144e709d445ab0608311290c882abbabb8321  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_tsa.json
630b63d817d1f8fb145228e5aa2542e4db99be1f156294539c60366572f7479c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ri_tvf.json
037601cf5ea885892e2dba2bf6487004fe24622515e1986255090c725177eebc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_ribspc.json
6a03521fd4e941a56eeeb5336973706c8b45c7b58530d3a1f2384dbb6630fe9f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_rmgcti.json
64cc29bea7bb5f6a55d05bd552c763dd2f2b61c872f23e6e3de7a68f57a8c029  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_rmrtsd.json
c2fa93f03eeb6d26a7e0881f6703d5f98cff3d5174268ea1d1d165f84d4a78c2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_rrci.json
ebf11d171a8358c11a7b1f73fadab06a63f47c69d6bbd968b210f9f4f70aea3a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_secfin.json
392177212a1c9c5c5640fe6220a0388e650cf4424afe3122beff1f77165c2a12  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_seggar.json
16ebdc28575a2984b69dd8fca99ddd93978f980eea7a538f0e4860d53852589e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_seguef.json
d64a890df22a3b7e1adf14243566246a83ab40c7b2af448e3d0166183a1a80c3  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_servco.json
9e4c7358ed3129e872e2b6ad7388dc9a36ce7e1378ac52df503041cd3de4e801  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_atm.json
d5a994b71280c35aa6b0747201415c450c7ea8d6f67f39091d1cbc44731488bc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_cec.json
21f69fc5be2cce24e2a7ba557dd3d58ff05ea4bd28d0ae2c7532b651bb0e376a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_dd.json
236e87766c098c4a4a6dfe69979a723703d43d271ef251ba14f5032f7cba6b5b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_debin.json
0f7adfe2c2ff34a9d676546192a3a0c9b569b1d6a6001af4cf96eec7d667d2e5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_mep.json
d24322e830e169d539379b473af3b5f6f5fdeeafef91f175d9536a4b602c0fd5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_psp.json
50ced181b5757855c93e744b0b39ccc1dc2f406a877eea3d37e8543aaa8b5d75  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_spd.json
360bebe5e6117aad286308309e29a225fcd1d905b9f2171062fdc81729492878  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_snp_tr_nc.json
028348d7a6fd586aa0e9991a79de9592f2df66d7d80ff79131a0cbf380f22e3f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_socgar.json
75506ba1c7d3136088f130a0660bab51e735b03defff4736eb1683b1a1a47229  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_supcon.json
a146533406f8a5f4ad947fddc47222dd27c966dc9fd963fc26f3a5d38f1503d5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_tasint.json
326ba86063758c5d86ba6b4db43b7fe75cd8ef1b171b0f56a61e2916e00770a2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_traval.json
8c664ad3a33d79b1867cc009a74dc507330dc5a9e081107b0a8b6b20692dec68  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_venliq.json
bba224ec0d847c406f7efe5cfd7ea8af529fb4aa6747c1d1853f60d5d09b816b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/tablas_verac.json
7838b09619e2416f6f5a8b2ba7f24f4bf85d2b7d71edb0926c429ad5201f7f66  data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b/version_e0.json
```

## 11. La foto del repo, los .pyc, el grep de convenciones y el incidente externo

- **La foto sha256 del repo entero** (`foto_repo_tanda_final_t1.py`: sin `.git`; los `.env*`, los `NO_ABRIR_` y los `*_SOLO_MESA*`, solo
  por tamaño y fecha; los enlaces, por su destino). Antes: 19:57:30 a 19:57:43, 52.693 entradas. Después: 22:42:40 a 22:42:52, 53.275.
  - Comparación (`--comparar`): **591 nuevos, 9 borrados y 17 cambiados**.
  - Los 591 nuevos: 498 en `reextraccion_v2/e0_chunking/salida_tanda_final_r2b/`, 1 en `reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json`,
    78 en `data/experiment/tanda_final/t1/` y 5 en `data/experiment/tanda_final/t2/`, más 9 en `data/experiment/neo4j/volumen/`.
  - Los 9 borrados y los 17 cambiados son todos de `data/experiment/neo4j/volumen/` (el incidente de abajo). Fuera de eso, ninguna ruta
    cambió ni se borró.
  - Los 40 sin abrir, con el mismo tamaño y la misma fecha antes y después; los 342 enlaces, iguales.
  - `git status --porcelain --untracked-files=no` sigue vacío.
  - Las comparaciones están en el paquete, con un resumen de las tres fotos (su sha256, sus horas y sus conteos). Las fotos enteras no
    van al paquete: listan todas las rutas del repo, con carpetas de las sesiones de la app que llevan nombres de personas y destinos de
    enlaces con la carpeta personal.
  - Este FRENO es uno de los 78 de `t1/` y lo completé después de la foto: su sha256 final no es el de la foto, y la ruta sí.
- **El incidente externo (Neo4j).** A las 20:00:32, justo cuando arrancaba el rsync del primer lote de E0 (20:00:31), un servidor Neo4j
  que corría en Docker se apagó («Neo4j Server shutdown initiated by request», según su `logs/neo4j.log`, que había arrancado a las
  19:05) y reescribió archivos de su volumen, `data/experiment/neo4j/volumen/`, que `data/experiment/neo4j/.gitignore` excluye. El rsync
  salió con rc 23 (archivos que desaparecieron mientras copiaba) y el lote frenó. No lo causé yo: ningún comando mío toca Docker ni
  Neo4j; cuando lo miré, antes de la foto intermedia, el socket de Docker ya no estaba y no quedaba ningún proceso de Neo4j. Una foto intermedia (20:02:09 a 20:02:25)
  separó las dos cosas: 35 cambios de Neo4j (9 nuevos, 9 borrados y 17 cambiados) y mis 4 archivos de `t1/` de ese momento. **Desde esa
  foto, el volumen de Neo4j no cambió más** (sus 229 entradas son iguales en la foto intermedia y en la de después). Rehíce el lote en
  una carpeta nueva.
- **Las copias.** Todas se hicieron con `copia_clausula_tanda_final_t1.sh` (la cláusula, más `tanda_final/preregistro/`), y todas dieron 0
  archivos por nombre y 0 enlaces: la del lote de E0, la del manifiesto y el control de entradas, las dos de la corrida en seco y la de
  las pruebas de T2. Ninguna lleva el `.env.example` de `run_2_papers/code/` ni los `NO_ABRIR_` del repo. A la de las pruebas de T2 le
  sumé después los scripts de `t1/` y `t2/` que usa el lanzador. A la del manifiesto le cambié dos archivos para el control en contra y
  los restauré (sha256 controlado); la usé después para el control de entradas, y sus 78 rutas dan 78 de 78 contra HEAD. El árbol de la
  base de A3 (`git archive`) dio 0 enlaces. Ningún control comparó una copia con el repo archivo por archivo. Al terminar, borré las
  copias del scratchpad.
- **Los `.pyc`** (`find . -path ./.git -prune -o \( -name '*.pyc' -o -name '__pycache__' \) -print | sort`): 11.236 líneas antes y 11.236
  después, iguales (`diff` vacío). Todo Python corrió con `-B` y `PYTHONDONTWRITEBYTECODE=1`, y los scripts nuevos fijan además
  `sys.dont_write_bytecode` (los cuatro de `t2/` que vienen de la tanda 1 lo heredan del lanzador o de `-B`).
- **El grep de convenciones**, sobre los 84 archivos de `data/experiment/tanda_final/t1/`, `t2/` y el manifiesto (no hay `NO_ABRIR_` en el
  repo). Los tokens del nombre salen de `git config user.name` en la consola (no quedan escritos en ningún archivo), más
  `slack|e-?mail|correo|whatsapp|reuni[oó]n con|como dijo|pedido por|seg[uú]n (el|la) (mail|mensaje|reuni)`, con `grep -c -i -E`.
  Los archivos con una cuenta distinta de 0: **ninguno**. Las rutas con la carpeta personal (`grep -l -E '/Users/|/private/tmp'`):
  **ninguna**. El control positivo (un renglón con el primer token y «slack») da 1. Ese grep corrió antes de completar este FRENO; sobre
  el FRENO final, las únicas coincidencias son los renglones de este punto, que citan el patrón y la ruta que busca. La pasada sobre el
  paquete va en el mensaje del FRENO.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna. Ninguna búsqueda mía las recorre: las copias salen del repo, y la carpeta
  de la copia permanente es la de esta sesión. Ningún `NO_ABRIR_` apareció en una salida, salvo los que escribieron mis scripts de
  prueba, de los que doy solo el sha256. Ninguna salida mostró contenido de una extracción de la tanda 1, ni el desglose de E3.

## 12. Errores propios, con su causa

1. **La salida de rsync en la consola.** En el primer lote de E0, la copia mandaba la salida de rsync al log del lote, que miré: trajo 16
   renglones «skipping non-regular file» con rutas de enlaces bajo `data/experiment/ev2_corrida/navegabilidad/trazas_nav/` (solo nombres;
   rsync no los copia y no abrí nada). Causa: `copia_clausula_tanda_final_t1.sh` no separaba esa salida. Desde el segundo lote va a
   `<copia>.rsync.log`, que no abrí.
2. **El control l del manifiesto comparaba a cinco decimales**, y la diferencia de redondeo de A3 (−0,000002) cruzaba el redondeo: dio
   FALLA con el manifiesto bien. Lo cambié por la comparación exacta contra las líneas por documento y a cuatro decimales contra el total
   de A3, y el control quedó 13 de 13.
3. **El script del ensamblado del subconjunto falló dos veces antes de correr:** el manifiesto restringido no restringía `estimado_usd`
   (`manifiesto_corpus.cargar` frenó), y buscaba el `kg.json` en el primer nivel en lugar de `r2/`. Los dos, corregidos; las salidas de
   esos intentos no se usan.
4. **Un `sleep 0`** quedó al principio de un comando de la consola (el que corrió `resumen_t2.py` sobre la corrida en seco). No espera
   nada, pero el despacho prohíbe `sleep`, y lo declaro.
5. **Las salidas de las pruebas 2 a 4 del lanzador** quedaron al principio solo en la consola de la sesión, no en sus logs. Repetí las
   cuatro con el código de salida en cada log (restaurando antes la base de E1 de la copia desde el repo); los resultados fueron los
   mismos, y son los de `t1/pruebas_t2/`.
6. **Una cita equivocada** en `consulta_deprecaciones_t1.txt`: atribuí «E3 no manda temperature» al punto g del control de entradas de la
   tanda 1, que es de E1. La corregí antes de este FRENO: lo respalda mi corrida en seco (E3, temperatura «sin fijar» en los 4.956
   pedidos).
7. **`freno_t1_cifras.py` falló en sus dos primeras corridas:** leía las listas de los tramos con una clave que las cifras del
   pre-registro no tienen (`documentos` en lugar de `tos`), y esperaba el código de salida en los logs de las pruebas 2 a 4 (el error 5).
   Los dos, corregidos; las tablas de este FRENO son las de la corrida final.

## 13. Para la autora

1. **El estimado por TO: plano en el repo, el reparto preparado.** El despacho (punto 2.3) da la fórmula plana por unidad, y el §3 del
   pre-registro firmado da el estimado por tramo con la tarifa plana (12,6901 y 91,8502); así está el manifiesto del repo (`23654ef8…`).
   Pero el registro de decisiones, §21, dejó esto para el pre-registro de la tanda final: «que su estimado se reparta igual desde el
   principio: su tramo 1 tiene los regímenes informativos y va primero». El texto firmado no lo recogió. Es lo que hizo la tanda 1 desde
   el 17/10/2026, después de dos frenos por proyección con el estimado plano (nota al pie de `docs/preregistro_tanda1.md`).
   - **Lo dejé preparado:** `t1/manifiesto/tanda_final_98tos_r2b_reparto_alternativa.json` (`e9993b9d…`), con `--estimado reparto` del
     mismo script. El método reproduce, TO por TO, el manifiesto commiteado de la tanda 1 (20 de 20 iguales).
   - **Lo que cambia:** el tramo 1 pasa de 12,778594 a 19,310012 y el tramo 2, de 91,971209 a 85,439791; el total, el tope, la U y la
     tarifa, no. El tramo 1 tiene el 18,4 % de los caracteres y el 12,1 % de las unidades (tablas 3 y 8).
   - **Para cambiarlo:** copiar ese archivo sobre `manifiestos/tanda_final_98tos_r2b.json`, poner su sha256 en `MANIFIESTO_SHA256` de
     `lanzar_t2.py` y en el primer renglón de `sha256_para_T2.txt`, y repetir los controles l y m (los dos pasan con cualquiera de los
     dos manifiestos: la suma es la misma, y la alternativa carga). Decide la autora.
2. **El sello del tramo 1.** El ensamblado de los 30 corre y reproduce, pero con una salida stub que suma el `TextoOrdenado`; con la del
   runner frena en I4 por un artefacto del stub. El acumulado de las tandas 0 y 1 con el tramo 1 no lo probé. Si esto habilita el sello
   del tramo 1 (§5) lo decide la autora. El stub del runner sin `TextoOrdenado` puede ir al backlog (una prueba de ensamblado con él no
   corre).
3. **Las 13 unidades de `snp_dd::S7` con el mismo pedido** (sección 5): en T2, 7 salen de la caché, sin costo, con la extracción de su
   gemela. No frena nada; queda declarado para la lectura y el ensamblado.
4. **El tope a cuatro decimales.** La sección final de la derivada lo escribe a dos (151,58); el manifiesto lleva 151,5835, la regla del
   punto 1.3 del despacho y de la tanda 1, y `--autorizado-tope` va con ese valor.
5. **Las dos opciones nuevas del lanzador** (`--autorizado-tramo-2` y `--retomar-tras-pausa`) existen para que un relanzamiento después de
   un FRENO del control o de la pausa no vuelva a frenar solo. No las pide el despacho: se usan solo con la decisión de la autora, y si no
   las quiere, se sacan.
6. **La interrupción manual del lanzador no la probé en vivo** (9.2). Si la quiere antes de T2, necesita una espera autorizada.
7. **El incidente de Neo4j** (sección 11): no fue mío, pero la foto lo muestra en `data/experiment/neo4j/volumen/`, ignorado por git.

## 14. El paquete

`revision_tanda_final_FRENO_T1/`, en el scratchpad de la sesión (`afadde2e-6298-47fb-9777-7fcb43152d50`), con su `manifest.txt` (sha256 y
una línea por archivo; los nombres llevan la unidad y la ruta del repo, para que no colisionen). Su copia con `ditto` está en
`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/afadde2e-6298-47fb-9777-7fcb43152d50/scratchpad/revision_tanda_final_FRENO_T1/`. La
verificación de la copia contra el manifiesto va en el mensaje del FRENO. El paquete no lleva la E0 de los 98 (está en el repo, con
`sha256_para_T2.txt`), ni los `NO_ABRIR_` de las pruebas, ni las salidas originales del selftest de claves, ni el JSON crudo del
health-check.

FRENO T1. Espero la revisión de la autora y el «seguí» de T2.
