# FRENO T1 — tanda 1 de B6.1: la corrida en seco (16/10/2026, USD 0, sin API, sin commit)

Pre-registro FIRMADO: `docs/preregistro_tanda1.md`, firma en `95b18217` (sha256 `2a64cae8…`), versión para firmar en `3b61f154`
(`33a3c34b…`). Rigen el §1.2, el §2, el §3, el §4.1, el §4.2 y el §7. HEAD `73f86f4b`. T1 corrió de 13:28 a 14:22 (−03).
Todo lo que escribí está en `data/experiment/tanda1/`, en `data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/` y en
`data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json`. Nada commiteado y ningún mensaje de commit preparado: los commits
son de la autora y quedan PENDIENTES.

**Resultado:** los criterios de aceptación de T1 están en verde. Tengo tres cosas para la autora (al final) y tres errores propios,
todos corregidos antes de este freno. T2 espera la revisión y el «seguí».

## 0. Paso 0 (13:28:15)

```
$ pwd
$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
$ git rev-parse --abbrev-ref HEAD
main
$ git status --porcelain --untracked-files=no
$ pgrep -fl runner_corpus
$ git log -1 --format='%h %s' -- docs/preregistro_tanda1.md
95b18217 Pre-registro de la primera tanda firmado por la autora
$ git merge-base --is-ancestor 95b18217 HEAD; echo $?
0
$ git show HEAD:docs/preregistro_tanda1.md | shasum -a 256
2a64cae84c5862f174e7a89e92f1fb1274b6446a9e1d09d8ac59273a208ce4ae  -
$ git log --format='%h %s' 95b18217..HEAD
73f86f4b Registro de decisiones: la etapa corta del sistema por fragmentos y las firmas del laudo y del pre-registro de la primera tanda
```

- `git status` salió vacío, y `pgrep` también (rc 1): no había ninguna corrida en curso.
- `git show 95b18217:docs/preregistro_tanda1.md | shasum -a 256` da `2a64cae8…`, y el de `3b61f154`, `33a3c34b897f…`.
- **Las 78 rutas** (`t1_paso0_rutas.py`, que lee `controles_tanda1/codigo_de_la_cadena_47c9f1b3_mesa.json`): `HEAD: 78 de 78`,
  `árbol: 78 de 78`, rc 0.
- **El espacio** (`df -k .`): 210.552.896 KB libres en `/System/Volumes/Data`, más que el piso de 31.457.280 KB.
- **Las cuatro rutas de T1** no existían: `data/experiment/tanda1/`, `e0_chunking/salida_tanda1_r2b/`, `manifiestos/tanda1_20tos_r2b.json`
  y `corpus_tanda1/`.
- **La foto del repo antes** (13:29:09 a 13:29:19, `foto_repo_tanda1_t1.py`, copia de `s2/scripts/foto_repo_S2.py`): 51.046 entradas, 8 sin
  abrir y 342 enlaces. La línea de base de `.pyc` y `__pycache__` tiene 11.236 líneas.
- La versión del repo de `t1_paso0_rutas.py` suma `--git-repo` (para la prueba del lanzador sobre una copia sin `.git`). Sin esa opción, la
  lógica es la misma que corrió en el paso 0.

## 1. La consulta de deprecaciones (13:30:08)

`consulta_deprecaciones_t1.txt` (sha256 `3d769265…`). La leí con WebFetch, sin iniciar sesión, en
`https://platform.claude.com/docs/en/about-claude/model-deprecations`. La lectura no dio error.
- `claude-haiku-4-5-20251001`: Active; Deprecated N/A; retiro tentativo «Not sooner than October 15, 2026».
- `claude-sonnet-5`: Active; Deprecated N/A; retiro tentativo «Not sooner than June 30, 2027».
- El historial no trae ningún aviso para ninguno de los dos.
- La sección «Notifications» dice que el aviso llega con al menos 60 días de anticipación.
- **No hay retiro anunciado: no corresponde el freno del §4.2.** La fecha tentativa de Haiku 4.5 ya pasó, pero sin aviso al 16/10/2026 el
  retiro no llega antes del 15/12/2026. Es lo mismo que registró el §2 [v8] con la consulta de las 09:18:37.

## 2. La E0 de los 20, con el código del gate (13:33:05 a 13:44:48)

`lote_e0_tanda1_t1.sh` corre todo sobre una copia hecha con la cláusula, con el python del `.venv` del repo. Los controles están en `t1/e0/`.
- **La copia y la raíz.** 0 `.env` y 0 `NO_ABRIR_` por nombre, y 0 enlaces. La raíz la armó `s0_4/scripts/raiz_minima.sh`, y también da
  0 enlaces.
- **El código** (`control_codigo_raiz_t1.json`): `e0_lib.py`, `correr_e0.py` y `e0_tablas.py` de la raíz dan los tres `codigo_sha256` del
  manifiesto de S0-6b (`80adbd58…`): OK.
- **Los 152** (`correr_152.py --workers 9`, de 13:33:41 a 13:40:11; `control_e0_152_t1.json`, con el control de S2): 768 de 768 iguales,
  0 distintos, 0 que faltan, 0 que sobran y 10.478 unidades: OK.
- **Los 20, dos veces** (`--tos` con los 20; 13:40:12 a 13:41:34 y 13:41:34 a 13:43:13; `control_e0_20_t1.json`, con
  `control_e0_tanda1_t1.py e0`):
  - las dos corridas dan los mismos 317 archivos, byte a byte (`por_to/` incluido);
  - los 100 archivos por TO dan su entrada del manifiesto: 100 de 100;
  - los 6 agregados que escribe dan, como JSON leído, los de los 152 restringidos a los 20, con las claves en el mismo orden;
    `ids_desambiguados.json` falta, y el de los 152 restringido da vacío;
  - `version_e0.json` da su entrada del manifiesto;
  - el primer nivel tiene 107 archivos, con 0 que faltan y 0 que sobran;
  - **3.290 unidades**, y cada TO da su `unidades_por_to`;
  - **los 20 PDF** dan el `sha256_pdf` de S1-ter (`f59cdea0…`), en `escalado_prep/pdfs/` del repo y en la raíz: 40 de 40.
- **El control de salud** (`healthcheck_e0.py` con un `--pdf` por TO, y `resumen_healthcheck_S2.py` sobre mi E0):
  - en verde: `frena_por_cobertura_o_ids` vacío;
  - el resumen (`resumen_healthcheck_tanda1_t1.json`, `a6c3dcd4…`) es **byte a byte el de S2b** (`comparacion_resumen_hc_t1.json`:
    0 diferencias);
  - el `hc_sha256` (`e6f78f2f…`) también es el mismo. Las otras señales quedan como las registra el §6.8. El JSON crudo del health-check
    no lo llevé al repo ni al paquete, porque trae muestras de texto (`senales.cid.muestras`): solo su sha256, que es ese mismo `e6f78f2f…`.
- **Al repo** fueron los 107 archivos del primer nivel de la corrida 1, sin `por_to/`, a `e0_chunking/salida_tanda1_r2b/`. Controlé las
  107 líneas de sha256 del repo contra la corrida 1: iguales.
- `control_e0_20_t1.json` es el de una segunda pasada de `control_e0_tanda1_t1.py e0` sobre las mismas carpetas. Esa versión del script
  saca la carpeta personal de las rutas (`sin_usuario`). La salida es la misma que la del lote, salvo `carpetas_pdfs`, y pisó a la del lote
  en el scratchpad.

## 3. El manifiesto de la tanda 1

`manifiestos/tanda1_20tos_r2b.json`, **sha256 `4dd025053fec11aabaa9f35e54a9da78912f86c1a11f11abd6aa3e2cc764897a`**. Lo armó
`t1_manifiesto.py` en una copia, y de ahí lo llevé al repo (el sha256 es el mismo en los dos). `--verificar` da «igual».
- **`tos`:** las entradas de S1-ter de los 20, en el orden de corrida, con `rol_alcance` del perfil `r2b` vigente:
  - 18 con alcance: 8 de la tabla de la release y 10 del derivado;
  - `ceninf` y `cirmo3` en null (§1.4);
  - las listas exactas de `clase_ids` en `nmcief` y `snp_cheq`.
- **`orden_corrida`:** ri_gerc, ri_pgn, ceninf, ri_rml, nmcief, adrei, opefci, ri_dcpc, snp_tr, efemin, ri_mmsef, manori, expaef,
  ri_ccna, ayccef, cirmo3, snp_cheq, cajasc, depaho, lingeef. Es el del despacho, que el script controla.
- **`limites`:**
  - `tope_global_usd` 100.7291 (1,45 × 3.290 × 0,021115 = 100,7291075);
  - `margen_unidad_usd` 0.35;
  - `checkpoint_cada` 150 en lingeef y depaho;
  - `chequeos_hits` vacío;
  - `estimado_usd` por TO: **suma 69,659193, que a 4 decimales da 69,6592**. Ver «Para la autora», 2.
- **`sellos`:**
  - el commit del código `47c9f1b3`;
  - la E0, con su ruta, 107 archivos y «PENDIENTE (lo fija el commit de la autora)»;
  - el prefijo de E1 `322c5a23e9b7` (`ccffa4e3…`, 59.909 caracteres, `66cde30`, parche `5e3761c1…`, base `8d84364f…`);
  - el tool schema `0c391f2b…`;
  - los namespaces de E1, del reintento por forma y de E3;
  - las temperaturas 0 y 1;
  - el prefijo de E3 `21a836c7de6d`;
  - los `candados`: tablas forzadas `98cc96b2…`, candado del mensaje de E1 `6b758517…`, mensaje `eeb11b9a…`, candado del mensaje de E3
    `079d2489…` y mensaje `66bc8656…`. Sumé una clave a la forma de la tanda 0, `registro_alcance_r2b_json_sha256` (`e06933e7…`),
    porque el §2 sella el mensaje de E1 con tres valores.
- **`nombres_remision`:** vacíos en los 20. Ver «Para la autora», 1.
- **La carga:** `manifiesto_corpus.cargar`, con sus valores por defecto (sha256 de los PDF y roles), lo carga sin error: 20 TOs, perfil
  r2b.
- **El control en contra:** el de S1-ter frena al cargarse con el perfil de A2. El mensaje es «TO 'manori': rol_alcance null pero el
  catálogo declara 'Sujeto_entidad_financiera' para manori.pdf».

## 4. El control de entradas (`t1_control_entradas.py`; salidas en `t1/entradas/`)

13 de 13 en OK (`control_entradas_t1.json`, veredicto OK), sobre la copia 2:
- **a–d.** El prefijo, el tool schema, los namespaces de E1 (`-rforma1` y `-rforma2`) y el prefijo y el namespace de E3. Los modelos del
  runner son `claude-haiku-4-5` y `claude-sonnet-5`.
- **e.** Los 100 archivos por TO de la E0 contra S0-6b: 100 de 100, y los 107 archivos que dicen los sellos.
- **f.** El candado del catálogo y los insumos del prefijo.
- **g.** La temperatura: 0 en las 2.439 unidades de la tanda 0 y en las 3.290 de la tanda 1, y 1 en el reintento por forma, con el resto
  del pedido igual.
- **h.** Las tablas forzadas, el candado del mensaje en el valor de A2 (`6b758517…` / `eeb11b9a…`), el derivado (`e06933e7…`) y el
  candado de E3. Además, `selftest_clave_cache` en **OK** (`selftest_clave_cache_t1.json`), con R29, R29b, R30 y R32 frenando y con el
  anclaje r2b: las 2.449 claves de E1 de la tanda 0 están en la base copiada.
- **i.** **Los mensajes de E1 de las 2.439 unidades de la tanda 0 salen byte a byte iguales a los de HEAD**, y los de las 3.290 de la
  tanda 1 también. Los comparé con un árbol armado con `git archive HEAD` de las 78 rutas, más la E0 y el manifiesto de la tanda 0, y la
  E0 y el manifiesto de la tanda 1 copiados. El sha256 del mensaje y el del pedido canónico salen iguales por unidad
  (`mensajes_e1_head.json` = `mensajes_e1_copia.json`, `824e5c3c…`).
- **j.** El recorte de herencia en la tanda 1: 13 unidades de snp_cheq (7.1.1 a 7.1.13), con la línea una vez cada una y en ninguna otra.
- **k.** El rol de alcance de los 20, igual al del perfil.
- **l.** Los sellos del manifiesto, controlados contra lo que carga el código, incluidos el tope y el estimado.
- **m.** La carga y el control en contra del punto 3.

## 5. La corrida en seco (`t1_corrida_en_seco.py`; salidas en `t1/seco/`)

Corrió sobre la copia 3 (la cláusula; 0 `.env`, 0 `NO_ABRIR_` y 0 enlaces), con `--stub`, desde la raíz de la copia.
- **El camino.**
  - Importo `runner_corpus.py` desde su archivo y llamo a su `main()` con `--manifiesto …/tanda1_20tos_r2b.json --salida <salida> --stub`
    (los 20, sin `--tos`).
  - Del `sys.path` solo pongo en `sys.path[0]` la carpeta del runner, que es lo que hace `python runner_corpus.py`; el resto lo arma el
    runner. No llamo a `configurar` ni a ninguna fase por fuera.
  - Reemplazo las dos clases stub del runner por subclases que registran cada pedido y devuelven las respuestas de cada rama. El stub de
    E1 tiene además `crear_reintento_forma`, como el cliente real, y por eso `cliente_e1.crear_reintento_forma` toma la rama del cliente
    real.
- **Las guardas** (`corrida_en_seco_t1.json`, `guardas`):
  - el constructor de `ClienteE1Real` y el de `ClienteE3Real`, y `anthropic.Anthropic`, quedan tapados por una función que cuenta y
    frena;
  - la red, bloqueada;
  - la clave, fuera del entorno.
  - Resultado: **0 conexiones, 0 clientes de la API y 0 clientes reales: 0 llamadas a la API.**
- **El runner:** salida 0, «corrida completa: gasto global=USD 0.0000».
- **Las cinco ramas, recorridas sin forzar ninguna.** Con la hipótesis de la salida p90 (1,5051 tokens por carácter), un pedido corta si
  `chars_propio × 1,5051` pasa su max_tokens:
  - **corte y reintento por corte:** 40 unidades cortan en 8.192 y salen en 16.384;
  - **partición:** `lingeef::5.4.2.3` (2 partes), `ri_rml::Sbloque14` (5) y `snp_cheq::7.2.4` (2);
  - **tercer escalón:** `manori::1.5.1`, `manori::Sbloque5` y tres partes de `ri_rml::Sbloque14` (1, 2 y 4), con 0 que cortan también;
  - **salida mal formada:**
    - `ri_gerc::S1`: el `-rforma1` sale bien;
    - `ri_pgn::2.1.1`: `-rforma1` y `-rforma2` sin `relations`, y se repara (T2-ter);
    - `ceninf::S0`: el `-rforma2` trae `entities` que no es lista, y queda con `salida_mal_formada_tras_reintento`;
  - **reintento del ratchet de E3:** `ri_gerc::2.2`, con un faltante sintético de severidad alta y una cita verificable. Dos verificaciones
    y una re-extracción de E1.
- **Los pedidos** (`pedidos_por_etapa`; un renglón por pedido en `pedidos_t1.jsonl`, sin el mensaje):
  - **E1:** 3.352, todos a `claude-haiku-4-5` con temperatura 0, en `…p322c5a23e9b7|think=0`, con **3.352 claves distintas**. Por
    max_tokens: 3.299 en 8.192, 48 en 16.384 y 5 en 40.960. Los 3.299 primeros intentos son las 3.290 unidades, menos las 3 partidas, más
    sus 9 partes, y dan 3.299 claves distintas.
  - **Reintento por forma:** 5, a `claude-haiku-4-5` en 8.192 con temperatura 1: 3 en `-rforma1` y 2 en `-rforma2`.
  - **Ratchet:** 1 (16.384, temperatura 0).
  - **E3:** 3.296 a `claude-sonnet-5`, sin temperatura, con 4.096, y 3.295 claves distintas. La re-verificación del ratchet repite el
    pedido porque el stub de E1 devuelve la misma salida. Las claves de E3 dependen de la salida de E1, así que en seco son sintéticas.
- **Claves ya en las bases de la copia** (abiertas `mode=ro&immutable=1`): 0 de 3.357 de E1, 0 de 1 del ratchet y 0 de 3.295 de E3. Ningún
  pedido de la tanda 1 está pagado de antes.
- **La consola del runner** (sintética) es `consola_runner_corrida_en_seco_t1.txt`.
- **La reproducción.** Corrí la versión final dos veces seguidas (14:03:30 a 14:03:42), entre dos fotos del repo (14:03:20 y 14:03:53).
  - Las fotos dan 0 cambios.
  - Mis cuatro salidas y la consola salen iguales byte a byte.
  - De los 378 archivos del runner, 73 difieren: 52 checkpoints y `ultimo_checkpoint.json` por su hora, y 20 `reporte_e2_<TO>.json` solo
    por la ruta de la salida.

## 6. La clase A y el censo de unidades grandes (`seco/censo_unidades_grandes_t1.json`)

La capacidad está recalculada con la salida por carácter de la tanda 0 (`reext_t0/freno_t2.md:12`):
- el reintento (16.384) cubre 14.146 caracteres con la mediana 1,1582 y **10.886 con la p90 1,5051**, que es la de la decisión 4;
- el tercer escalón (40.960) cubre 35.365 y **27.214** (la constante de `correr_e0.CAPACIDAD_ESCALON_3_R6`).

| unidad | caracteres | se parte | mecanismo, y lo que hizo el runner en seco |
|---|---:|---|---|
| ri_rml::Sbloque14 | 50.404 | sí, 5 partes (11.736, 12.742, 6.991, 11.981, 6.950) | partición por corte; las partes 1, 2 y 4 pasan los 10.886 y van al tercer escalón, que las cubre |
| manori::Sbloque5 | 24.352 | no (`sin_items_detectables`) | **clase A**: tercer escalón 40.960 (24.352 < 27.214) |
| snp_cheq::7.2.4 | 18.367 | sí, 2 partes (10.105, 8.261) | partición por corte; las dos partes caben en el reintento |
| manori::1.5.1 | 15.949 | no (`sin_items_detectables`) | **clase A**: tercer escalón 40.960 |
| lingeef::5.4.2.3 | 13.393 | sí, 2 partes (9.696, 3.696) | partición por corte; las dos partes caben en el reintento |

- **El censo:** 5 unidades pasan los 10.886 caracteres (4 pasan los 14.146 de la mediana), y **ninguna queda sin declarar**.
- **La clase A** (sin partición posible y sobre la capacidad del reintento): **2, `manori::1.5.1` y `manori::Sbloque5`**. Las dos pasan
  también la capacidad de la mediana, y las cubre el tercer escalón.
- **Sobre el tercer escalón con la p90:** ninguna unidad ni parte.
- Otras 35 unidades, entre 5.443 y 10.886 caracteres, cortarían en 8.192 con la p90 y saldrían en 16.384.
- Los mecanismos no son una lista: los ejecutó el runner en la corrida en seco (columna «en_la_corrida_en_seco»).
- `ri_rml::Sbloque14` es la unidad grande que el §6.8 llama «la de ri_rml, que lleva una tabla serializada» (`e0_unidades_grandes_ids`
  del resumen del health-check). Tiene 10 bloques de tabla y 47 ítems `num`, y la partición por corte la parte sin partir ningún bloque
  (`particion` del censo).

## 7. El estimado por TO (`seco/estimado_por_to_t1.json`)

Con los clientes stub, el gasto es 0. La tarifa es la del §3: 0,021115 por unidad, más las líneas de alcance de A2.

| TO | unid. | USD | cortes p90 | | TO | unid. | USD | cortes p90 |
|---|---:|---:|---:|---|---|---:|---:|---:|
| ri_gerc | 15 | 0,319465 | 0 | | ri_mmsef | 128 | 2,726105 | 0 |
| ri_pgn | 21 | 0,447252 | 1 | | manori | 152 | 3,236057 | 12 |
| ceninf | 39 | 0,823485 | 0 | | expaef | 165 | 3,483975 | 0 |
| ri_rml | 46 | 0,979694 | 16 | | ri_ccna | 169 | 3,597377 | 1 |
| nmcief | 55 | 1,172434 | 4 | | ayccef | 196 | 4,138540 | 1 |
| adrei | 70 | 1,478050 | 0 | | cirmo3 | 256 | 5,405440 | 1 |
| opefci | 74 | 1,562510 | 0 | | snp_cheq | 265 | 5,648652 | 5 |
| ri_dcpc | 75 | 1,596739 | 4 | | cajasc | 287 | 6,060005 | 0 |
| snp_tr | 103 | 2,194403 | 3 | | depaho | 442 | 9,332830 | 0 |
| efemin | 119 | 2,512685 | 0 | | lingeef | 613 | 12,943495 | 8 |

- **Total:** 3.290 unidades y **USD 69,659193**, igual al manifiesto en los 20 TOs (e1 y e3). A 4 decimales, 69,6592. El runner lo
  redondea a 69,659 (`estimado_total_usd` de `estado_corpus.json`).
- **Tope:** USD 100,7291, con un margen de 31,069907 (1,4460 veces el estimado).
- **La salida de los cortes con la p90:** la cota es USD 2,6215. Son las 56 llamadas que cortan, a su max_tokens, a USD 5 por millón,
  sin la entrada ni el tercer escalón que responde. Es lo que la tarifa por unidad no incluye si la salida real fuera la del p90. El
  freno por proyección lo controla con el gasto real.

## 8. T2, preparada y probada en seco (`data/experiment/tanda1/t2/`)

**Los scripts y su sha256:**

```
5a53e88d9483f27b1d3d1acc4d26eb2f73c46f30b98094fecd59bcf80a1f11c4  data/experiment/tanda1/t2/lanzar_t2.py
b384bd15b3846750a6d293e89c01f0a3b7f18efd82ec60b3ed71a07a484637de  data/experiment/tanda1/t2/freno_modelo_t2.py
06171f405007bfaab3b23a9f30236cf263fec36a21d210df74f69ee738ea29aa  data/experiment/tanda1/t2/resumen_t2.py
082c743edfd52ea59383dc20452d4f99846872f2063a01c87f75dc53cd222396  data/experiment/tanda1/t2/conteos_t2.py
fbb1e064567afd8237d5c12ff2e0ffe07a7823a604cf5304f3766c298edd661f  data/experiment/tanda1/t2/caso_en_contra_t2.py
36db11c97f6cf54a9ab9d1f93f05a1bf092d9e56947e73012c528126e6a470cb  data/experiment/tanda1/t1/t1_paso0_rutas.py
```

### 8.1 Qué hace cada uno

- **`lanzar_t2.py`.**
  - **Los controles previos**, antes de la corrida real; si uno falla, para con salida 2:
    - el piso de 30 GB (`os.statvfs` del volumen del repo);
    - las 78 rutas, con `t1_paso0_rutas.py`;
    - el SDK del python que corre el runner, que tiene que dar `0.100.0`;
    - el sha256 y el tope del manifiesto;
    - la copia de trabajo de las bases, fuera del repo y nueva.
  - **El freno por modelo**, antes del primer TO sobre las etiquetas de los 20, y después de cada TO sobre las de ese TO.
  - **Los 20 TOs**, en el orden del manifiesto y con la misma `--salida`. Cada uno con el comando del despacho, desde la raíz del repo, con
    `PYTHONDONTWRITEBYTECODE=1`, `-B` y SIGINT en su acción por defecto.
  - **Cuándo para:** si el freno da FRENO (salida 10) o si el runner sale distinto de 0 (devuelve ese código). En los dos casos, sin
    empezar el TO siguiente.
  - **La interrupción manual:** restablece su propio SIGINT, porque en segundo plano llega ignorado. Interrumpido, le pasa el SIGINT al
    runner, espera, lo registra y sale con 130.
  - **La copia de las bases:** una sola, que pisa en cada control y borra al terminar, también cuando para. Solo borra la carpeta que
    creó él.
  - **La clave:** no la lee. Saca `ANTHROPIC_API_KEY` del entorno del runner, como `lanzar_t2bis.py:36`, y el runner la carga de su `.env`.
  - **La salida de pantalla del runner** se agrega a `t2/NO_ABRIR_salida_e3_tanda1.txt`, con una línea `### lanzar_t2: <TO> <hora>`
    antes de cada TO. El lanzador nunca lo lee.
  - **El registro** `t2/avance_t2.jsonl` lleva:
    - por TO, la hora de inicio y de fin, el código de salida, el freno (con los conjuntos de ids) y el gasto global (como
      `Estado.gasto_global`) contra el tope;
    - los controles previos, las paradas y el fin.
  - **Relanzado**, recorre otra vez los 20 y agrega líneas.
  - **Solo para las pruebas:** `--solo-tos`, `--stub` y `--git-repo`.
- **`freno_modelo_t2.py`.**
  - Copia las tres bases (con `-wal` y `-shm` si existen) a una sola copia de trabajo. Las bases del repo no se abren ni se escriben.
  - Cruza `access_log.run_label` (`corpus_<TO>_e1`, `corpus_<TO>_reintentos_e1` y `corpus_<TO>_e3`) con `cache.model`.
  - Imprime solo los conjuntos de ids y OK o FRENO, sin cantidades. FRENO si un id de E1 no es `claude-haiku-4-5-20251001`.
  - Con `--etiquetas-existentes`, dice qué etiquetas de los TOs pedidos ya están en las bases.
- **`resumen_t2.py`.**
  - Por TO y en total: las unidades (y con las partes), las aceptadas (los tres estados juntos), la cola, los errores, los ids repetidos,
    la cobertura y el gasto contra el tope.
  - De la consola toma solo las líneas `FRENO:`, `ERROR:` y `corrida completa`, con su TO.
- **`conteos_t2.py`.** Escribe el desglose en `t2/NO_ABRIR_conteos_reextracciones_tanda1.json`:
  - los estados de E3 y `n_reintentos`;
  - los renglones de `reintentos_e3.jsonl` y de `copias_nota_e3.jsonl`;
  - las `marcas_e3`;
  - el gasto del verificador y el de los reintentos de E1.
  Imprime solo su sha256 y la vigilancia `integridad_e3` en OK o FRENO: todo estado en `ratchet_e3.ESTADOS`, y toda unidad aceptada en
  E1 con expediente. Ninguna vigilancia del §5.3 frena durante la corrida: son mediciones de cierre.
- **`caso_en_contra_t2.py`** es solo de la prueba: rehúsa una base del repo (lo probé: salida 2 y la base del repo con el mismo sha256).

### 8.2 Las pruebas (evidencia en `t1/pruebas_t2/`)

- **El SDK:** `<repo>/.venv/bin/python -c "import anthropic; print(anthropic.__version__)"` da `0.100.0` (Python 3.10.13). El lanzador lo
  controla también.
- **El freno sobre la tanda 0** (con las bases del repo copiadas a una carpeta de trabajo; `freno_modelo_tanda0.txt`):
  - `ids de E1 (con sus reintentos): ['claude-haiku-4-5-20251001']`, `ids de E3: ['claude-sonnet-5']`, `RESULTADO: OK`. Son los ids
    de su T2 (`freno_t2.md:8`);
  - las etiquetas de los 20 de la tanda 1 ya en las bases: **ninguna** (`etiquetas_tanda1.txt`);
  - las tres bases del repo dan el mismo sha256 antes y después.
- **De punta a punta**, sobre la copia 4 (la cláusula; 0, 0 y 0), lanzado como la corrida real (en segundo plano, `caffeinate -i …
  lanzar_t2.py --trabajo-bases … --stub --solo-tos ri_gerc,ri_pgn --git-repo <repo>`, de 14:10:57 a 14:11:01;
  `lanzador_prueba_1.log`):
  - los controles previos en OK: 185.539.852 KB libres, `HEAD: 78 de 78`, `árbol: 78 de 78`, SDK 0.100.0, y el sha256 y el tope del
    manifiesto;
  - el freno OK antes del primer TO, entre los dos y después del último;
  - ri_gerc y ri_pgn con salida 0;
  - el registro (`avance_t2_pruebas_copia4.jsonl`);
  - la copia de las bases, borrada (`copia_de_las_bases_borrada: true`). El lanzador salió con 0.
- **El caso en contra.** Agregué a la `e1_extraccion.db` de la copia 4 una fila de `corpus_ri_gerc_e1` (en `access_log` y en `cache`,
  con el esquema de `llm_cache.py:133-157` y el id `claude-haiku-4-5-caso-en-contra`). Relanzado con los mismos dos TOs (14:12:00 a
  14:12:02; `lanzador_prueba_2_caso_en_contra.log`):
  - `freno_modelo_antes`: **FRENO**, con `ids_e1: ["claude-haiku-4-5-caso-en-contra"]`;
  - «parada: freno por id de modelo antes del primer TO», sin ningún `to_inicio`;
  - la copia, borrada, y salida 10.
- **Los scripts del cegamiento.**
  - Sobre la salida sintética de la corrida en seco: `resumen_prueba_seco.txt` (3.296 unidades con partes, cobertura completa, la línea
    `corrida completa`) y `conteos_prueba_seco.txt` (`sha256 b1d6ed1a…`, `vigilancia integridad_e3: OK`).
  - Sobre la de la prueba de punta a punta: atribuye cada `corrida completa` a su TO por la línea del lanzador, y los conteos dan
    `14e37a35…` y OK.
  - Los `NO_ABRIR_` de las pruebas los escribieron los scripts, y no los abrí. Su sha256 está en `sha256_no_abrir_de_las_pruebas.txt`.
- **No probé** la interrupción manual en vivo: hubiera necesitado una espera, y el despacho las prohíbe. El camino está en el código
  (`lanzar_t2.py`, `except KeyboardInterrupt`).

### 8.3 Cómo se lanza, y la duración y el costo estimados

Desde la raíz del repo y en segundo plano; quién lo lanza lo fija el «seguí» de T2:

```
caffeinate -i "$HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg/.venv/bin/python" -B data/experiment/tanda1/t2/lanzar_t2.py --trabajo-bases <carpeta nueva fuera del repo>
```

- **Duración:** la tanda 0 corrió 2.439 unidades en 481,4 min (de 14:38 a 22:39, `freno_t2.md:3`), 11,84 s por unidad. A ese ritmo, las
  3.290 de la tanda 1 son unos **649 min (≈ 10 h 50 min)**, más unos 35 s de los 21 controles del freno. Es una proyección con la tasa de
  la tanda 0, no una medición.
- **Costo:** el estimado es USD 69,6592, con un tope de USD 100,7291.

## 9. El sha256 del manifiesto y de la E0 de los 20, para `shasum -a 256 -c`

Está también en `data/experiment/tanda1/t1/sha256_para_T2.txt` (sha256 `1793a70e…`, 108 líneas, controlado con `shasum -a 256 -c`: 108 OK).
Desde la raíz del repo: `shasum -a 256 -c data/experiment/tanda1/t1/sha256_para_T2.txt`.

```
4dd025053fec11aabaa9f35e54a9da78912f86c1a11f11abd6aa3e2cc764897a  data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json
fad86c47c9cb2a2a097f04f90830c0d44f2264336ac9fba031558da9548f331f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_adrei.json
78b2bd32b7fd41c2384e40acfa011f0389f8139d779e2a3b5ce6a6d7302622d7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ayccef.json
68758bb6b2437a1d8bd2f0e670bab279dea18b4485e688e5ac422468bedae2fc  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_cajasc.json
5024532270c2302f962577c0ac02191106ae5c7d1bdec4b76b9e288d20f2bd0a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ceninf.json
2c6407e113d83520f196b877f981f7a7172704b5fa7f279f60a0bb3d441f8087  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_cirmo3.json
d366bad60414d9ab92483ae3d1363a94af341ee0ac38857313984f66e5d2a730  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_depaho.json
fe1a29f82f4d80638c894f205b59b4768d6aab8c8d4c6ff1850e2d820e01744e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_efemin.json
f5dcbda425f6d1208a2e1d438de173a9401b69698ba3c9ee04dd74ca58aacb0c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_expaef.json
1dccc4d570218b4540ad9e323f2d2b79a07b74c8aaa41f94da48de28610a571b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_lingeef.json
18db947cd3793054757311b721092094621d0e03d303956b27126037a90f6761  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_manori.json
d44fbe51e12b9acbddf814e2f08b445ed0633cd696acc85a653390a430751499  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_nmcief.json
8b4ee0fc3152b4b0b4bd6c7bb0f62c3f10ac464ea37128ffae50b022f60efec6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_opefci.json
29af8e8ef97274d701f09d1a51cef9a9cb0594db043c6fb9ccb457d91eba2c89  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ri_ccna.json
8cc337167edd047d12476ac7b870c7221cfc8f13ff993f096596f3ca57f23b49  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ri_dcpc.json
9ec87c500b447b7dcc23cb49f2bcee14aa6fe9d36185d0d746f51be45c0d1984  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ri_gerc.json
01de100960d8f18d591c6a03e7ec87421b119bf2a913adf42ae3901068e77fc8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ri_mmsef.json
8f96617821cb05524cb8f5904610d3eeeef7af72bfa1d279cefed3427f13e898  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ri_pgn.json
2201258e7b84269f23e7b0df0f6a29a9995f165e0264f3273888d5e430958af0  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_ri_rml.json
405239ea7491f07daec8d5346d1436bcb935933373f00025c543258f5b98e348  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_snp_cheq.json
c037da5bac65bb962247a0590a91e854f7b24abdaaf0572f7fdb4ba1c6bd2feb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/chunks_snp_tr.json
74f46d18ec2b30c3bee6d67aef9777a8353458873b79ef8f4873c7f1d9a9e03a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/cobertura.json
306bf8a48de5c653a6fab85c3a462944141980fc36cc862b9455e7c45d3a0cd4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/conteos.json
da6dbf94177848eb71d81985a1e58e9bcdbb31ef7b91010e7230c12710bed35f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/correcciones.json
c36ee93d312af9b0af541ee12ecf14ee6ecf4c3be3923fc39ccf980013117668  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/divergencias_indice_cuerpo.json
8d6fafe0cda3eac5f43d83536fe6ccebfaef3044887179a40fc00ca3b653c4b8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/encabezados_conservados.json
0fae68bd9129de59572c780ad15f792ade9eab44d28d198085aa614824d98462  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_adrei.json
c0e0c87ef788f0b010dc2fbfbb471fa3e4b6abb137df3cd77ca54de82e7340f6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ayccef.json
f1ef1c60150b80f1d49eb183ad9f3abfc28f26b1ca94bbf88ab400d824db2cbf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_cajasc.json
8907ff62c7dc596c80c10ffe14ce7f3bd73278668d414d3cf1e48af1d44981ca  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ceninf.json
96fc0a0f9f193add595ac30646ec61400ef9306195f127f440b76cd0f75e21c2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_cirmo3.json
690ebee6edbc91a0d5e30b5a30cdc09ab7d645fe480e1bd60684bf1c6483775c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_depaho.json
63dc92e071b99f038f77a81c86cf2e7de323df1028f93311e2ed7e08b419a8fb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_efemin.json
812db7cc930d743f2c0f480fa4b7cf43cbab23f5eed5365181840de3bee5f66d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_expaef.json
b0db61e3481ab19706e5f5d53a1f5250983533727da776820d58a3297731ce8a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_lingeef.json
072897ca1fdab3e42657fa25b9ed7ab9471348242e0d0fa6ac42732508b07c16  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_manori.json
acea0a0de54a4da8592b2c54c68ab1f0e5d6b60a5672f51f09aefd33a0d472e5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_nmcief.json
bf7fae5cd5cb367a81388918c8f05059d52d0d658d77bc3dfeb8c9f13a154fca  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_opefci.json
78d6889d5567fb9bc3f7f86d27c3c7ba351a59a128b397a3c80535476809035a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ri_ccna.json
c55771ef28ea8ef80554aca5de1b1c93deecb8a024fb38f53375af5996a72c15  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ri_dcpc.json
bcc5529371910de06a2d61a65866788d4355ecd2a0e5743296d919fc2af5b6b8  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ri_gerc.json
615b16a36b5df9ad1f9a4afc595b223fbd8c3c568be3c9ccc5995bca9e1d5306  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ri_mmsef.json
301e40bb495a13d9165b6bd3dcb9a86932ea0d69ff8abe0d376abe94ed78fbe2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ri_pgn.json
74925829ffda57cdb628551e2a5aa1b556abf12103495416eecb204d4cdbf191  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_ri_rml.json
2e67aac3d20a2de4eac2c61c79a2829ef06096ae40dbc7cfa86c6b65cf862fc6  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_snp_cheq.json
ed7a871027a91249c3dcf5203f4ff9cf610b89a43ace855e88b372393e7ded1d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/estructura_snp_tr.json
741d0c5653bfe8536845fe104b4a0a093c46b21173703fc16d5777e217d4a24c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_adrei.json
83772205732864113b426fa2aae4d542cacea189ab627fa3b9a1fea42ecb0bb1  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ayccef.json
ce335972826d07304d0b71c77862fc60bac23f5ae098aa439f81a011626f0a60  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_cajasc.json
77a487c2354a327e33556e39dae19f09b13280ef01027a6283dee6433cd519c9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ceninf.json
1c4680efeea824102bc738909831d8e87ad0d1c76e7993e84f4c2b146e7304ec  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_cirmo3.json
e496e3b62d19febe2ac22d4bf863706b6d329ebdc47e79979facf490c09aacaa  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_depaho.json
a0f52349609507b9aaa54d14aaef3e44560ea4986ed2c55cc2ca52c6be190afb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_efemin.json
70d213b5f9fc271a47bebbc77d4a96ff87b89329422945b7804a63d013930edf  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_expaef.json
73138493b8f5e2544a548d1ab0118a49b4727f6b20f9de2280707d38517a9490  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_lingeef.json
77a73b43d144125c52d52fd4aabe46fe06f20271cea8c1b56cc0424f390e65d0  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_manori.json
825fcf76b6668566c035c03098725bf0568f00ba313b71a8d65e356292348ed4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_nmcief.json
4f8c05047e650ce571916b9f07fd24dd36e20a57d385b582295b6ca85ebc1d6c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_opefci.json
0c63398573877f43eaaae5d425fe072587b220a89cf9b242fdaf24954d3fce81  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ri_ccna.json
81f7559e9dc4d624ff44eca3dee2704716e93daeaf658910d1e76b8c3389a02f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ri_dcpc.json
57121d3195efe02b5c23c5eb8d0f36d82b94ad972a8f44700e83e0c5a1f65537  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ri_gerc.json
4f53cda18c2baa0c0354bb5f9a3ecbe5ed12ab4d8e11ba873c2f11161202b945  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ri_mmsef.json
b5476657cd4dbba005524f4a7eb0f61147bb90cd4010b804cbd6607a202da416  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ri_pgn.json
b9a4da45b99c6667ffb9a9e63b144d6cc8e6902bbd45481d359aab5021e8e2d2  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_ri_rml.json
b4c004e0dd6aa854cfc95f3406e8d49750dc795796676110773de8a1d5dce99a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_snp_cheq.json
3bb3affd4b786f4c66ac34dc5eb0e51af2d473ef6b427a71785b0e7df05c7944  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/indice_snp_tr.json
5b190c20679f14f92581f4be37eab321d0ee894a118ef7f4dbb5be7baa97ee9a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_adrei.json
3b7f9f8d7fec28faf036f16225d5ea6a0a3ff68a664c2c95cc84e77ef625c46f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ayccef.json
52197800d292b4223abf956875d8e71ba42a6ed5b20cc1694c030408f80c4d8d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_cajasc.json
a05d0dd7cc64fbfe4e7f9d07b9bcdc44ff8c4fe7eb94a635784ffbe2ef8ae05f  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ceninf.json
95686283c802b57f5c33f22c92c93baecaf136ec4ceabba53f8c3fe1e622e4de  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_cirmo3.json
a33322b99fed9582a04e6eb3e99c7dd51d2e55439a543315c29587960c2a8a34  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_depaho.json
1405c212db0e76daddd1370cb0d906c88eff6737e97cc864787f108c57339239  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_efemin.json
e9e373abf1a576ae52398cc64af696bfea298542685278eda304569efcd02e0d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_expaef.json
eb121fe24358fb4d4ccb13eabf9cbc4330428aef5b1bfe497ab101817165cac4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_lingeef.json
57e0609743aa4c926d45feafe9f892ce7856bf04acddef9e47b8e440cfa0dc6b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_manori.json
b123b1bc91aaacd5ac2a84685dee71635024b7c069ba0a7ca9d2adfaa5cd4242  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_nmcief.json
4c7258205aa314dffb0b17d08560cf60da8d5c3f41c82c75d4779313f2ff771c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_opefci.json
4b3a4e0249859bb5e8e240f6c47309dc6fce5fdd15cd786db66ad75e53eaa229  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ri_ccna.json
c546878a13aad79260d383af50ed691101632f94306593deb38c9eaeea88369a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ri_dcpc.json
36827504cb0fced40774a2bb23f5f9d25ba56e42b36ecda7eb9db876bc1117ff  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ri_gerc.json
3a66c7beffea63f204fe2e3e18b4812092fe65b906e0d6b5ea13ffff3d9f8dc4  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ri_mmsef.json
2ff4beed23ae940af2d21c5eedb3813711555a7a5f26c1331039f8660e72d60a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ri_pgn.json
11a9c1c070cdf92b9c27f7a2456e6e0768811b34fd2e1021409357457066c1ed  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_ri_rml.json
72e76acd9cc485488e4dcaf3f4dc732afd58efd6d3335a6c33951ad649b1b363  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_snp_cheq.json
774c29ae05c39553b7611a6ebf7728c5f21a86303fe9228196d5c7fd588acda5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/pies_snp_tr.json
df74e45b669f9ae548652145b5d433ec9c47617d8316d151d231ae32e16d2440  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/sub_chunking.json
ef2f00272045c12ad4100e0acabd4bc95ce30a842144965f2b3d7925bfd4c9d5  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_adrei.json
77926de14bb33aea0207ce83812e39e381c43a966a250a36c15e7dcc1d093f6e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ayccef.json
6b523b10ab647da516a0aa047ac5cfa5516885386f99fad30ff7e90f01c7c3cd  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_cajasc.json
42de13684389272ea9abc9f6bf1d8b0bb2cb1fde178a7453c110a71f3ffad04e  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ceninf.json
c359f4dbfb3b1f44827b77848d672c957db06f9a5857ea02961a1e2bb910403d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_cirmo3.json
10e64de5f88530faadee78a9e1b90e3a7402cd6b31bf8b4e643d872656ef6122  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_depaho.json
5c18c5be10921d80c7f0f21d875c331a9552ff12661e0e3bc8302d17ba930482  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_efemin.json
07fe9b33b4d7e4a98055fe6ecbb4eefe6ce7067a655cab20a36965445b3a587b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_expaef.json
df48488f13ad10afdd12ff6074a664716f4563034791e165c0ae3111b8b61478  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_lingeef.json
9992132f56a962b65abd5650d7d7398cf1648556be413ec253891454806c00b7  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_manori.json
8b8615e56300af29baccdee4f1134d60b3e5e60e1a935d99c5ce641ebb62d2ba  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_nmcief.json
18b094ce60df26bdcadcaf710d052435d54847b0352b57c57991b815b990de8a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_opefci.json
d3254ac3683e5647b66bbc61bd2fb576649bf881eeae372389f79182b1a0278d  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ri_ccna.json
85de30b453767a0937ac9eb9f67cc01f1a09c5ab7005a75d70bb1a29fa5ac32a  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ri_dcpc.json
8a11cc049a6f24b1894274631dcd943d310e68774652b9aa736da67faf285aed  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ri_gerc.json
c832f37307981ffb2fe599fc15a6f92e5b32386f44d34df7a9181b77f15859b9  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ri_mmsef.json
73033366b19dd655542ff4555de73c3987e36217d0c4bfa862f1c552c0781797  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ri_pgn.json
b589fb93fa1d537911d906cce3acffd043447ca4f3548ff50ce3c5621a82aceb  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_ri_rml.json
5fa77d1325195561fdb8ce0ac97b46bc0ee4dcf0cac160a42b6229fc713ce93b  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_snp_cheq.json
e55919b5a428d8b61ff96564ee9226a9f5081a8bf71d02831533804c5dd99b8c  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/tablas_snp_tr.json
7838b09619e2416f6f5a8b2ba7f24f4bf85d2b7d71edb0926c429ad5201f7f66  data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b/version_e0.json
```

## 10. La foto del repo, los .pyc y el grep de convenciones

- **La foto sha256 del repo entero** (`foto_repo_tanda1_t1.py`: sin `.git`; los `.env*` y los `NO_ABRIR_`, solo por tamaño y fecha; los
  enlaces, por su destino). Antes: 13:29:09 a 13:29:19, 51.046 entradas. Después: 14:16:57 a 14:17:10, 51.196 entradas.
  - Comparación (`--comparar`): **150 nuevos, 0 borrados y 0 cambiados**.
  - Los 150 nuevos: 107 en `reextraccion_v2/e0_chunking/salida_tanda1_r2b/`, 1 en `reextraccion_v2/manifiestos/tanda1_20tos_r2b.json`
    y 42 en `data/experiment/tanda1/` (37 en `t1/` y 5 en `t2/`). Ninguno en otra ruta.
  - Los 8 sin abrir, con el mismo tamaño y la misma fecha antes y después.
  - `git status --porcelain --untracked-files=no` sigue vacío.
  - Las fotos y su comparación están en el paquete (`foto_repo_antes_T1.json`, `foto_repo_despues_T1.json` y
    `comparacion_fotos_T1.json`).
  - Este FRENO es uno de los 42 y lo completé después de la foto: su sha256 final no es el de la foto, y la ruta sí.
- **Las copias.** Las cuatro copias (`copia`, `copia2`, `copia3`, `copia4`) se hicieron con la cláusula. Las cuatro dieron 0 `.env`, 0
  `NO_ABRIR_` y 0 enlaces, y quedan sin el `.env.example` de `run_2_papers/code/` ni el `NO_ABRIR_` del repo. Ningún control comparó una
  copia con el repo archivo por archivo, salvo los scripts de la sección 11, punto 3. El árbol de HEAD (`git archive`) dio 0 enlaces.
- **Los `.pyc`** (`find . -path ./.git -prune -o \( -name '*.pyc' -o -name '__pycache__' \) -print | sort`): 11.236 líneas antes y
  11.236 después, iguales (`diff` vacío). Todo Python corrió con `-B` y `PYTHONDONTWRITEBYTECODE=1`, y los scripts nuevos fijan además
  `sys.dont_write_bytecode`.
- **El grep de convenciones**, sobre los 42 archivos de `data/experiment/tanda1/` y el manifiesto, sin los `NO_ABRIR_`. Los tokens del
  nombre salen de `git config user.name`, más `slack|e-?mail|correo|whatsapp|reuni[oó]n con|como dijo|pedido por|seg[uú]n (el|la)
  (mail|mensaje|reuni)`, con `grep -c -i -E`. Los archivos con una cuenta distinta de 0: **ninguno**. Las rutas con la carpeta personal
  (`grep -l -E '/Users/|/private/tmp'`): **ninguna**. El control positivo y la pasada sobre el paquete están en el mensaje del FRENO.
- **Las carpetas vedadas:** no abrí, no listé ni copié ninguna. Ninguna búsqueda mía las recorre: las copias salen del repo, y la carpeta
  de la copia permanente es la de esta sesión. Ningún `NO_ABRIR_` apareció en una salida. Los `NO_ABRIR_` de las pruebas los escribieron
  scripts, y de ellos doy solo el sha256.

## 11. Errores propios, con su causa

1. **`REPO` con un nivel de menos** en `t1_manifiesto.py` y `t1_control_entradas.py`: `parents[3]` y `parents[2]`, en lugar de `parents[4]`
   y `parents[3]`, para un script en `data/experiment/tanda1/t1/`. El armado del manifiesto falló con `FileNotFoundError` en la copia 2
   antes de escribir nada, y lo corregí.
2. **La guarda de la primera corrida en seco** reemplazaba `ClienteE1Real` por una función. Así se rompió el
   `isinstance(cliente, ClienteE1Real)` de `cliente_e1._crear`. El runner tomó cada `TypeError` como un error de API, reintentó con sus
   propias esperas (20 y 60 s, `runner_corpus.py:589-605`) y frenó con salida 3 en ri_gerc, a los 8 minutos («más de 5 errores de API
   consecutivos»). Fueron 0 llamadas a la API. Lo corregí: tapo el constructor y no la clase, y un error dentro de un stub sale ahora
   enseguida, como `BaseException`. La salida de esa corrida quedó en el paquete (`seco_fallido_1`). Las esperas fueron del runner y no
   mías, pero las causó mi error.
3. **Una comparación de scripts con zsh** (`set -- $p` sin partir la variable) dio «DISTINTO» en todos. La rehíce en Python: los doce
   scripts que corrieron en copias son iguales a los del repo. No afectó ninguna salida.

## 12. Para la autora

1. **`nombres_remision`.** El despacho pide el método de `reext_t0/t1_manifiestos.py`, pero ese script no los deriva: los deja como vienen
   en el manifiesto de origen (`t1_manifiestos.py:6-8`). Apliqué eso, con la entrada de S1-ter, que los trae vacíos («lo fija el
   ensamblado»), y lo declaré en la `descripcion`. Los de la tanda 0 salieron en U-TANDA0-2A, a mano, del título de portada más una variante
   corta (`docs/plan_tesis.md:765`, decisión 4). El runner no los lee (`grep nombres_remision runner_corpus.py` vacío): los lee el
   ensamblado (`r1_referencias.titulos_de_inventario`, que suma el título oficial del inventario). No cambian T2. Si el ensamblado de la
   tanda 1 los necesita, se fijan antes de ensamblar. Decide la autora.
2. **El estimado por TO, con 6 decimales.** Redondeados a 4 por TO, los 40 valores suman 69,6596 y no 69,6592. Dejé los valores exactos
   (6 decimales), que suman 69,659193 y a 4 decimales dan 69,6592.
   - Contra el 69,659191 del §3 hay 0,000002 de diferencia. Viene de A2: en la tabla de `alcance_e1/a2/freno_a2.md:68-80`, la columna de
     tokens por documento suma 190.843, no los 190.841 del total, y la de USD suma 0,190843, no 0,190841, porque cada documento redondea
     sus tokens.
   - Es un tally de un FRENO ya revisado cuya suma no cierra. Lo reporto y no lo toqué.
3. **La interrupción manual del lanzador no la probé en vivo** (8.2). Si la autora quiere esa prueba antes de T2, necesita una espera
   autorizada.

## 13. El paquete

`revision_tanda1_FRENO_T1/`, en el scratchpad de la sesión (`4723b63d-a0d7-4fc7-b109-c2febdabe540`), con su `manifest.txt`. Su copia con
`ditto` está en `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/4723b63d-a0d7-4fc7-b109-c2febdabe540/scratchpad/revision_tanda1_FRENO_T1/`.
La verificación de la copia contra el manifiesto va en el mensaje del FRENO.

FRENO T1. Espero la revisión de la autora y el «seguí» de T2.
