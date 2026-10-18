# FRENO A3 — U-ALCANCE-E1: las filas de alcance de la tanda final en el mensaje de E1

18/10/2026, base `5289b02f`. Mandato FIRMADO (`docs/mandatos/UALCANCE_E1_A3_filas_de_la_tanda_final.md`), leído en el commit de la
firma, `0c927ebb` (sha256 `dad23156cd26…`, igual en la base), con la precisión de la autora del 18/10/2026 a su condición 1 (en HEAD
desde `bd60f6c0`, nota al pie y registro de decisiones, §36). USD 0, sin API. **No escribí nada en el repo:** lo que el mandato manda
escribir va en el paquete, entero y con su diff. Nada commiteado, ningún mensaje de commit preparado, nada en la memoria, en `.claude/`
ni en `.gitignore`.

## Paso 0 (carpeta personal como `$HOME`; 17:44, antes de copiar)
```
pwd                                                     → $HOME/INGENIERIA IA/TESIS/bcra-regulatory-kg
git --no-optional-locks log -1 --format='%h %s'         → 5289b02f Pre-registro de la tanda final: version para firmar, con sus
                                                          scripts, sus pruebas y los huecos que se completan por momento
git --no-optional-locks log --oneline | grep -nE '^(764768a4|0c927ebb)'
                                                        → 12:764768a4 Alcance de la tanda final: la lectura de la autora, sellada y controlada, en el registro
                                                          16:0c927ebb Mandato firmado: las filas de alcance de la tanda final en el mensaje del extractor, con su nota al laudo y a la enmienda
git merge-base --is-ancestor <c> HEAD                   → rc 0 para los dos
git --no-optional-locks status --porcelain --untracked-files=no → (vacío)
```
**La base de la copia es `5289b02f6457…`.** HEAD siguió ahí hasta el fin de la reproducción (18:15:59). A las 18:18 entraron a HEAD
`d728e7b0` (T4, segundo tramo, solo `tanda1/t4/`) y `bd60f6c0` (la nota al mandato y el §36): ver «El control del commit».

## Las condiciones (§4) y la precisión
- 1: arranqué con T4 y T5 corriendo, sobre copias sin enlaces y sin `t4/` ni `t5/`; no escribí en el repo. 2 y 3: `764768a4` y
  `0c927ebb`, en la historia. 4: arranqué el 18/10/2026 a las 17:44, antes del martes 20 a las 21:15, y no falta la fila de ningún
  documento (criterio 3), así que no sale ninguno.

## Para el repo (PREPARADO: lo commitea la autora, después del commit de T5)
En `para_el_repo/` del paquete, cada uno entero (`*_post_A3.*`) y con su diff contra la base (`*_A3.diff`), y un parche único,
`parche_A3_contra_5289b02f.diff` (sha256 `f13b07f7c2fa…`). `git apply --check` y `git apply` sobre un clon de la copia de la base dan
rc 0 y los cuatro archivos byte a byte iguales a los probados.
1. `catalogo_unico/registro_alcance_r2b.json`: `--tandas 1,final`, 43 entradas: las 10 de la tanda 1, byte a byte, y 33 de la tanda
   final. Contra el de HEAD, 399 renglones agregados y 0 quitados.
2. `reextraccion_v2/e1_extractor/prompt_r2b.py`: un renglón de comentario de A3 (`:476`) y el sha del derivado, que pasa de `:477` a
   `:478`. `:97-98` no cambian.
3. `reextraccion_v2/e1_extractor/selftest_prompt_r2b.py`: un caso nuevo y dos reescritos (hallazgo 5); 67 casos → 68.
4. `mantenimiento/tabla_reprocesamiento.md`, fila F13c (`:167`): una oración de A3 en «Dónde entra» y dos anclas al día (`:476-478` →
   `:477-479`, `:481-487` → `:482-488`). La fila sigue siendo un renglón (546 renglones antes y después).
5. `data/experiment/alcance_e1/a3/` (se crea): este FRENO, `scripts/` y `salidas/`, con la misma ruta en el paquete.

## PROPUESTOS (los confirma la autora)
- `REGISTRO_ALCANCE_R2B_SHA256_ESPERADO` = `c8dea08a2ffe2eeb401855f952cc80f26542da8ea2489eac7a6f83530b6857ca`.
- `CANDADO_MENSAJE_JSON_SHA256_ESPERADO` = `6b758517cee0f2e36c26c54f0f6738b3d49d11d0cf3141c26cff166ce6820325`, **el de HEAD**.
- `MENSAJE_R2B_SHA256_ESPERADO` = `eeb11b9a3bf699d5535fcf2bbe79541ba746ae7bdae3341af962840990a97362`, **el de HEAD**.

Los dos del candado salen iguales a los de HEAD, como prevé el §3.3: la fixture (17 unidades) usa nueve documentos (cap, ric, ext,
docvig, ri2_ci, ri_ccna, snp_cheq, ri_rml y ri_oc) y ninguno tiene entrada nueva. Para el pre-registro de la tanda final (§1.3, sin
firmar): derivado `c8dea08a…`, candado `6b758517…`, mensaje `eeb11b9a…` y costo de las líneas nuevas USD 0,209440, los cuatro PROPUESTOS.

## Los once criterios (`scripts/bateria_a3.sh`, 18:05 a 18:09; consola en `salidas/bateria_a3.txt`)
1. **Tanda 0, igual:** por el camino del runner (`runner_corpus.configurar(manifiesto_corpus.cargar(tanda0_10tos_r2b.json))` →
   `perfil_e1.perfil("r2b")`), 2.439 unidades, 0 distintas; sha de los mensajes `48fdec197658…` con HEAD y con A3, el de A2.
2. **Tanda 1, igual:** los 20 de `lista_final`, 3.290 unidades, 0 distintas contra HEAD. La E0 se regeneró en la copia
   (`scripts/correr_lote_e0_a3.sh`, 17:49 a 17:55: los renglones 13 a 24 de `lote_tramo1_S2.sh`, tal cual, hallazgo 3): 768 de 768
   archivos iguales al manifiesto de S0-6b (`80adbd58…`; 152 TOs, 10.478 unidades). Ningún proceso abrió nada bajo
   `corpus_tanda1/` ni `tanda1/t2/` a `t5/` (registro de lecturas). El manifiesto de la tanda 1, de T1, carga con el perfil de A3.
3. **Tanda final:** los 98 de `cifras/tanda_final_S2c.json`, 4.951 unidades. 52 con entrada en la release y 46 con fila (33 con
   alcance y 13 sin alcance declarado). **Sin fila ni rol: ninguno** (lista vacía). Cambian los 33 documentos con entrada nueva,
   1.178 unidades, todas y solo en la línea de alcance (el mensaje de A3 sin «línea + salto + salto» es el de HEAD); los otros 65
   (3.773 unidades), sin cambios. Costo, abajo.
4. **Derivado:** dos corridas iguales byte a byte entre sí y al archivo; con `--tandas 1`, el de HEAD byte a byte; contra el de HEAD,
   399 renglones agregados y 0 quitados, en un bloque (`120a121,519`). Un parser propio de la tabla (`filas_tanda_final_a3.py`, sin el
   lector de R2-2) da 46 filas de 6 columnas (17 clase, 3 clase (dos), 13 rol reutilizado y 13 sin alcance declarado), y las 33
   entradas nuevas en el orden del registro y con los ids de su fila.
5. **`selftest_prompt_r2b`:** HEAD sobre HEAD, 67 ok y 0 FAIL; A3, 68 ok y 0 FAIL; el de A3 con el código de HEAD (la copia de la base
   con solo el selftest de A3), 67 ok y 1 FAIL, **exactamente el caso nuevo** («10 entradas; 0 después de las de la tanda 1»;
   `salidas/control_negativo_selftest_prompt_r2b_a3.json`). Además, `prompt_r2b.py` de HEAD con el derivado de A3 no importa:
   «candado r2b: registro_alcance_r2b.json con sha256 c8dea08a2ffe… (esperado e06933e77a1a…) — se frena».
6. **`selftest_clave_cache --salida-r2b`:** OK con HEAD y con A3; las dos corridas de A3, iguales byte a byte (JSON y consola), y el JSON
   de A3 igual byte a byte al de HEAD: 45 variaciones, ninguna nueva, A1r y A3r OK e iguales, tokens iguales, contraste OK en 45 filas.
   Ver el hallazgo 1 y el error propio 1.
7. **Vecinos, consolas iguales byte a byte con HEAD y con A3:** `selftest_catalogo_unico` 60/60 (con el `.git` del repo en solo
   lectura, como A2), `selftest_reresolver_catalogo` 66/66, `selftest_cablev3` 45/45 y `selftest_manifiesto` 44/49 (sus 5 fallos son
   los de P5 con `reporte=False`, los que anticipa CLAUDE.md §4.l).
8. **Los tres valores con `--verificar` sobre la copia final:** `sellar_a2.py` de la copia (sha256 `5a0893bce27f…`) sobre `copia_a3`:
   coinciden los tres e importa sin frenar. Dos procesos dan lo mismo; el mismo método sobre HEAD da los dos del candado iguales.
9. **Foto sha256 del repo** antes y después de cada paso: 51.401 renglones (los archivos, más las cuatro carpetas de salidas de la tanda
   1 como un renglón cada una, por `stat`, sin abrirlas); 0 nuevos, 0 quitados y 0 cambiados en el lote de la E0, en los 8 pasos de la
   batería y en la reproducción; **243 `.pyc`** en todas. Del inicio (17:44:58) al cierre (18:19:08), 0 nuevos, 0 quitados y 2
   cambiados, los dos documentos de `bd60f6c0` (`salidas/foto_repo_inicio_contra_cierre_a3.json`).
10. **La corrida en seco importa `prompt_r2b` por el camino del runner:** `mensajes_runner_a3.py` agrega al `sys.path` solo `corpus_v2`,
    como al ejecutar el runner, importa `runner_corpus` y llama a `configurar`; queda cargado `e1_extractor/prompt_r2b.py` de la copia,
    y ningún módulo de `data/experiment` viene de fuera (`modulos_de_data_experiment_fuera_de_la_copia: []`, en
    `salidas/resumen_mensajes_runner_*.json`). La batería oficial corre sin el registro de lecturas; la reproducción, con él.
11. **Grep de convenciones** (`scripts/grep_convenciones_a3.py`, sobre todo el paquete; los tres archivos con texto de otras etapas,
    solo en sus renglones agregados; `NOMBRES_EXTRA` vacío): control positivo 16 de 16; 0 nombres y 0 de la cuenta; 64 de
    conversación: 54 «mensaje de», todos técnicos («mensaje de E1», «mensaje de commit»), y los 10 términos de la lista del
    propio script (`salidas/grep_convenciones_a3.txt`).

**La reproducción desde cero** (`scripts/reproduccion_a3.sh`, 18:10 a 18:16): una copia nueva con el rsync del despacho (16.098
blobs iguales a la base, 0 distintos), el parche del paquete con `git apply` y la batería entera con el registro de lecturas. De 41
salidas, 40 iguales byte a byte a las de la oficial y 1 igual con la carpeta de trabajo reemplazada (la traza del candado escribe una
ruta); 0 distintas (`salidas/comparacion_reproduccion_con_la_oficial_a3.json`). El registro de lecturas es un audit hook
(`scripts/registro_lecturas/sitecustomize_registro_lecturas_a3.py`, que corre como `sitecustomize.py` por `PYTHONPATH`) y anota cada
archivo que abre un proceso de Python, imports incluidos.

## Costo por documento de las líneas nuevas (`salidas/medicion_mensajes_tres_tandas_a3.json`, `tanda_final`)
Medido en seco con la razón marginal de E1 (3,0598 caracteres por token, `e3_listas/o3/razon_tokens_e1.json`) a USD 1 por millón de
tokens de entrada de `claude-haiku-4-5` (`runner_corpus.py`, `P_E1`), una llamada por unidad:

| documento | decisión | unidades | caracteres por unidad | caracteres | tokens | USD |
|---|---|---|---|---|---|---|
| ri_acsf | rol reutilizado | 6 | 559 | 3.354 | 1.096 | 0,001096 |
| ri_ai | rol reutilizado | 15 | 559 | 8.385 | 2.740 | 0,002740 |
| ri_bdp | rol reutilizado | 3 | 559 | 1.677 | 548 | 0,000548 |
| ri_esd | rol reutilizado | 5 | 559 | 2.795 | 913 | 0,000913 |
| ri_ii_31_12_19 | clase (dos) | 91 | 575 | 52.325 | 17.101 | 0,017101 |
| ri_msrl | rol reutilizado | 12 | 559 | 6.708 | 2.192 | 0,002192 |
| ri_nge | rol reutilizado | 30 | 559 | 16.770 | 5.481 | 0,005481 |
| ri_ot | rol reutilizado | 32 | 559 | 17.888 | 5.846 | 0,005846 |
| ri_rcl | rol reutilizado | 4 | 559 | 2.236 | 731 | 0,000731 |
| ri_secoexpo | rol reutilizado | 35 | 559 | 19.565 | 6.394 | 0,006394 |
| ri_sef | rol reutilizado | 38 | 559 | 21.242 | 6.942 | 0,006942 |
| ri_tar | rol reutilizado | 18 | 559 | 10.062 | 3.288 | 0,003288 |
| ri_tvf | rol reutilizado | 6 | 559 | 3.354 | 1.096 | 0,001096 |
| ribspc | rol reutilizado | 7 | 559 | 3.913 | 1.279 | 0,001279 |
| cateloc | clase | 11 | 535 | 5.885 | 1.923 | 0,001923 |
| horari | clase | 13 | 535 | 6.955 | 2.273 | 0,002273 |
| inspag | clase | 93 | 535 | 49.755 | 16.261 | 0,016261 |
| opecam | clase | 65 | 532 | 34.580 | 11.301 | 0,011301 |
| reqcac | clase (dos) | 3 | 563 | 1.689 | 552 | 0,000552 |
| ri_iepsp | clase (dos) | 13 | 677 | 8.801 | 2.876 | 0,002876 |
| ri_psp | clase | 9 | 556 | 5.004 | 1.635 | 0,001635 |
| seguef | clase | 101 | 535 | 54.035 | 17.660 | 0,017660 |
| cedin | clase | 66 | 535 | 35.310 | 11.540 | 0,011540 |
| consyr | clase | 34 | 535 | 18.190 | 5.945 | 0,005945 |
| garant | clase | 106 | 535 | 56.710 | 18.534 | 0,018534 |
| garopt | clase | 55 | 535 | 29.425 | 9.617 | 0,009617 |
| jafip | clase | 91 | 535 | 48.685 | 15.911 | 0,015911 |
| ri_ieccm | clase | 4 | 532 | 2.128 | 695 | 0,000695 |
| ri_tsa | clase | 17 | 535 | 9.095 | 2.972 | 0,002972 |
| seggar | clase | 36 | 535 | 19.260 | 6.295 | 0,006295 |
| snp_dd | clase | 131 | 535 | 70.085 | 22.905 | 0,022905 |
| venliq | clase | 23 | 535 | 12.305 | 4.022 | 0,004022 |
| verac | clase | 5 | 535 | 2.675 | 874 | 0,000874 |
| **total** | | **1.178** | | **640.846** | **209.440** | **0,209440** |

- El total se calcula sobre los caracteres sumados (640.846 / 3,0598); la suma de los redondeos por documento da 209.438 tokens y
  USD 0,209438. El orden es el del registro; los 33 son 17 clase, 3 clase (dos) y 13 rol reutilizado.
- Contra la tarifa de E1 de la tabla (USD 0,010135 por unidad, §5), es el 1,75 % del E1 de esas 1.178 unidades (USD 11,9390) y el
  0,42 % del de la tanda final (4.951 unidades, USD 50,1784). Los reintentos de E1 reenvían el mensaje y suman lo suyo; no los estimo.
- Si la revisión entre tandas saca un documento, se resta su renglón (precisión, punto 4); si cambia una fila de alcance, A3 se rehace.

## El control del commit (precisión, punto 3; `salidas/archivos_leidos_base_a3.json`)
611 rutas, cada una con su sha256 en la base y el de HEAD al armar la lista (`bd60f6c0`, 18:2x), y de dónde sale:
- **586 entradas de los valores:** 427 rastreadas (lo que abrió un proceso de Python, según el registro de lecturas de la
  reproducción y del lote de la E0, y lo que leyó la consola), entre ellas las 78 rutas de la cadena, todas abiertas por algún
  proceso; los 157 PDFs (no se rastrean: los 152 contra `escalado_prep/manifest_pdfs.sha256` y los 5 del subset contra la tabla de
  `INFORME_E0.md`, iguales); y las dos bases de la caché (hallazgo 1). Están todos los grupos del punto 5 del despacho.
  **Ninguna rastreada difiere de la base en `bd60f6c0`.**
- **25 leídas solo en la sesión, para entender el trabajo** (`scripts/lecturas_de_la_sesion_a3.tsv`). Dos difieren en `bd60f6c0`: el
  mandato y el registro de decisiones, por la nota y el §36 de la autora. No son entradas de los valores (§36).
- Ningún proceso abrió una ruta del repo fuera del `.venv`, ni nada bajo las carpetas de salidas de la tanda 1, ni escribió dentro de
  una copia. De las 611, las que A3 cambia: `prompt_r2b.py` y el derivado, que están entre las 78 (la re-sellada del commit de A3, §2
  del pre-registro de la tanda final); `selftest_prompt_r2b.py` y la tabla no están entre las 78.

## Hallazgos y contradicciones (para la autora y la mesa)
1. **El criterio 6 y el §6 (PROHIBIDO) chocan.** `selftest_clave_cache` abre en solo lectura `e1_extractor/cache/e1_extraccion.db` y
   `e3_verificador/cache/e3_verificacion.db`, que `.gitignore` excluye (no tienen blob en la base) y que desde T2 tienen las llamadas
   de la extracción de la tanda 1, y cuenta sus claves por namespace. El JSON trae esas cuentas (seis campos `claves_db…`) y la consola,
   una. Por eso el JSON de HEAD ya no sale igual al commiteado en la base: difieren solo cuatro de esos campos, una cuenta de E3 y tres
   de E1, y nada más (`clave_cache_sin_cuentas_a3.py comparar`). Corrí el criterio porque el mandato lo pide; en el paquete esas
   salidas van sin las cuentas (`*_sin_cuentas_a3.*`) y los originales, por su sha256. Las dos bases tienen el mismo sha256 en las
   cuatro copias (17:45 y 18:10), y las fotos del repo no las ven cambiar. El despacho dice que un archivo usado sin rastrear frena;
   no frené por estas ni por los PDFs: lo marco para que la mesa decida.
2. **El renglón de A3 corre en +1 los renglones de `prompt_r2b.py` desde el 476.** Quedan con el ancla vieja, fuera de mis escrituras
   y sin tocar: la nota del 17/10 al pie del laudo (`:548`) y de la enmienda 4 (`:187`), que dicen `:477` (ahora `:478`), y F11b de la
   tabla (`:163`), que dice `:476-478` (ahora `:477-479`). Ya en HEAD, F22 y F22b dicen «candado `:464-484`», y el del mensaje está en
   `:490-512` (`:491-513` con A3).
3. **El rsync de `lote_tramo1_S2.sh` (renglón 11) toma el repo y no excluye `t4/` ni `t5/`.** Por eso corrí sus renglones 13 a 24, tal
   cual, sobre un clon de la copia controlada; la E0 da 768 de 768 igual a S0-6b.
4. **Los PDFs no se rastrean;** los controlé contra los dos archivos rastreados que dan su sha256 (criterio de arriba).
5. **El selftest: «suma un caso» y «falla exactamente el caso nuevo».** Dos casos de HEAD daban por hecho un derivado solo de la tanda
   1 (`regenera`, con `--tandas 1`, y `solo_agrega`, con las 10 entradas exactas): con A3 fallaban, y si los ponía al día fallaban con
   HEAD. Los reescribí para mirar las 10 primeras entradas (pasan con HEAD y con A3), y el caso nuevo carga todo lo de la tanda final.
6. **F13c «suma un renglón»:** la fila es un renglón físico; uno nuevo sería otra fila. Lo sumé como una oración en su celda.
7. **La lista que regenera el lote** difiere de la commiteada en el sha del registro (`ce402aad…` → `a4b52cd2…`) y en la fila de
   ri_mmsef; `lista_final` y U, iguales (como en A2).
8. **En la base, `scripts/regression_kg_esperado.json` ya difiere del sha sellado en la lista de las 78** (la de `47c9f1b3`). A3 no lo
   toca.
9. **Un `git fetch` ajeno durante la batería:** `.git/FETCH_HEAD`, a las 18:09:33. Ningún comando mío hace `fetch`.
10. **El manifiesto de la tanda final** se tiene que armar con el perfil de A3, después de su commit: uno armado antes declara el rol
    anterior de los 33 y frena al cargarse (F13c).

## Errores propios, con su causa
1. **Vi cifras que cubre el cegamiento de U-MED-VERIF.** Para saber por qué el JSON de `selftest_clave_cache` de HEAD no era el de la
   base, corrí `diff` sobre los dos JSON enteros antes de mirar qué campos traían. En la consola de la sesión aparecieron las cuatro
   cuentas del hallazgo 1, una de ellas de E3, que incluyen las llamadas de la tanda 1, con sus valores en la base y hoy. No las copié
   a ningún archivo ni calculé nada con ellas. La de la consola del selftest no la vi: la miré con los dígitos tapados. Desde ahí la
   batería compara esos JSON sin mirarlas. La mesa decide si esto toca el cegamiento.
2. **La primera batería de prueba** rotulaba «clase» las de dos clases y buscaba «FAIL» en `selftest_manifiesto`, que escribe «FALLO».
   Lo corregí y volví a correr la batería entera; la oficial es la segunda.
3. **El primer control de blobs** listó en la consola de la sesión carpetas de segundo nivel de las sesiones de la app, con nombres de
   personas. Lo cambié para agrupar por la carpeta de primer nivel y reescribí su salida antes de que nada fuera al paquete.
4. Dos llamadas al intérprete del `.venv` sin `-B` (versión y `sitecustomize`), que importan solo biblioteca estándar: 243 `.pyc`
   antes y después. Usé `sleep` en la consola para esperar el fin de dos corridas (no es una espera programada; no escribe nada). Y
   el renglón de inicio de la batería con el registro de lecturas escribe «sí» pegado a la ruta del registro (formato del log; no
   cambia nada). La primera verificación de la copia del paquete escribió su salida en un archivo de `/tmp`, fuera del scratchpad;
   lo borré en el mismo comando y repetí la verificación en el scratchpad.

## Copias, carpetas vedadas y cegamiento
- Copias: la del rsync del despacho y sus clones (`cp -cR`: copias, no enlaces) para A3, la E0, los controles y la prueba del parche;
  y una copia nueva para la reproducción. 0 `.env`, `.env.*`, `*.env` y `NO_ABRIR_` y 0 enlaces en cada una (el rsync saltea 336, todos
  en `ev2_corrida/navegabilidad/trazas_nav/`). Ningún `git clone`.
- No abrí, listé ni copié nada de las carpetas vedadas ni del paquete de la mesa; ninguna búsqueda las recorrió.
- No abrí salidas de T2 a T5 ni `NO_ABRIR_`: la foto las registra por `stat`, agregadas por carpeta. Para saber qué carpetas no abrir,
  listé con `git show --name-only` las carpetas que tocaron los commits de T2 y T4, y miré el `--stat` de `d728e7b0` para saber qué
  había cambiado; no abrí ninguno de sus archivos. La foto y el control de blobs calculan el sha256 de las bases de la caché, sin leer
  su contenido.

Commit PENDIENTE de la autora; los tres valores, PROPUESTOS. FRENO A3.
