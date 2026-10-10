# U-SEG-OFICIAL — informe de S0-5a-bis (09/10/2026)

Mandato `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md` con sus notas al pie; lista de R5-a v2 de la mesa; el
agregado de ri_oc del 09/10/2026. USD 0, sin API. Nada commiteado; el parche no se aplicó al repo. Diseño:
`DISENO_S0-5a-bis.md`. Salidas de E0: en el paquete de revisión (no entran al repo). Las rutas `censos/…` son de
`s0_5/bis/`; las cifras son de la segunda vuelta (con R5-g), salvo donde digo «vuelta 1».

## 1. Entrada

- `git log`: la segunda nota está en `84695b89` (15:18:30, «U-SEG-OFICIAL: segunda nota de decisiones del 09/10/2026»),
  el único commit que tocó el mandato después de `32c71ca`; HEAD al empezar, `0c271468`.
- Mandato leído en `84695b89`: sha256 `cbe0cb35…` (432 renglones), con las dos notas.
- **Después de empezar** entró la tercera nota (`be88fdf9`, 15:50:24; el mandato en ese commit, `66f3549c…`, 452
  renglones): población (b) de S1-ter, y dos límites medidos de `ri2_ae::14.3` que llevé a la lista de límites (§8). Y
  hay una cuarta nota sin commitear en el archivo (la sección 3 de ri_oc y su lectura en S1-ter), que coincide con el
  agregado que recibí; no la uso como fuente.
- Código de E0 del repo: `65a8c3b8…`, `94d35349…`, `ec186071…` (S0-4b); mi parche de S0-5a, `c6558ea0…`.
- Lista v2: `lista_R5a_por_lista_v2_decision4_mesa.json`, sha256 `5bec1dce…`, igual al del `manifest.txt` del paquete de
  la mesa. Lista de los 88: `lista_88_rechazos_columna_profunda_mesa.json`, `cf6796e7…`, igual a la de su manifest.
- Foto sha256 del repo a las 15:22:15: 48.312 archivos; 2.213 `.pyc` fuera de `.venv/`.

## 2. Controles duros

| control | resultado | respaldo |
|---|---|---|
| todas las reglas apagadas contra S0-4b | 768 de 768 iguales al manifiesto `61ed4bc9…`; 9.625 unidades | `censos/comparar_NINGUNA_vs_S0-4b_S0-5a-bis.txt` |
| los 152 dos veces: prototipo con todas y código final sin interruptor | 768 de 768 iguales; 9.665 unidades; manifiesto `176cbdc0…` | `censos/comparar_TODAS_vs_FINAL_S0-5a-bis.txt`, `censos/manifiesto_salida_e0_152_S0-5a-bis.json` |
| contra S0-4b | 74 archivos distintos: chunks 34, estructura 32, tablas 2 (ri_ccna, snp_tr), 6 agregados | `censos/comparar_FINAL_vs_S0-4b_S0-5a-bis.txt` |
| contra S0-5a | 65 archivos distintos: chunks 18, estructura 40, tablas 4 (gerc, gescre, manori, ri_spi), 3 agregados | `censos/comparar_FINAL_vs_S0-5a_S0-5a-bis.txt` |
| tanda 0, código final, script secuencial, dos veces | 57 de 57 en las dos | `censos/comparar_t0_final_{1,2}_vs_r2b_S0-5a-bis.txt` |
| tanda 0 sin la exclusión (medición) | ninguna regla la cambia: 0 unidades | `censos/limites_s05a_sobre_S0-5a-bis.json` |
| los 25 archivos de la tanda 0 dentro de los 152 | 25 de 25; agregados 20 iguales y 15 ausentes en los dos | `censos/control_tanda0_en_152_S0-5a-bis.txt` |
| `selftest_e0` | 188 de 188 | `censos/selftest_e0_S0-5a-bis.txt` |
| b52, b581, b582, b583 | 39/39, 34/34, 59/59, 33/33 | `censos/selftests_b5x_S0-5a-bis.txt` |
| selftest de claves de la caché | VEREDICTO OK; anclaje r2b OK (2.449 claves); contraste OK; igual byte a byte a `923dd900…` | `censos/selftest_claves_cache_S0-5a-bis.txt` |
| selftest del control de continuidad | 14 de 14 | `censos/selftest_control_continuidad_S0-5a-bis.txt` |
| claves de S0-5a-bis | §5 | `censos/claves_control_S0-5a-bis.json` |

Los selftests corrieron dentro de una copia del repo con el código final (`censos/sha_codigo_del_selftest_e0_S0-5a-bis.txt`).
La primera corrida de `selftest_e0` de la vuelta 1 dio 183 de 184: el recuento de ri_ccna esperaba 159 unidades y son
169, porque R5-f abre 11 puntos y quita el chapeau de `D1A1::S5`; corregí la expectativa con su razón.

## 3. Aceptación (`scripts/aceptacion_S0-5a-bis.py`; `censos/aceptacion_S0-5a-bis.json`)

1. **R5-a por lista**:
   - las 40 enteras sin rango: el último ítem y el cierre del padre, con el texto de S0-5a, 40 de 40;
   - `ri_rml::1.4.2`: el cierre de 1.4 va de «Para el punto 1.4.1.» a «…671000/M-TP.» (19 renglones), y el ítem queda con
     su rótulo y sus dos fórmulas (3 renglones); ítem y cierre juntos son el ítem de S0-4b;
   - los dos mixtos: el cierre es, renglón por renglón, el de `renglones_del_cierre` (11 en `ri_spi::C.1::cierre`, 7 en
     `ri2_ae::S14::cierre`), y el resto del ítem es el de S0-4b sin esos renglones, en el mismo orden. `ri2_ae::14.3` sigue
     partido en tres partes;
   - las 14 que no se tocan: el último ítem y el cierre del padre, con el texto de S0-4b, 14 de 14 (en `manual::2.3.2`
     cambia solo la herencia, por el título de la sección 2 que junta R5-c);
   - ningún evento de R5-a fuera de las 43; ninguna lista sin su rango.
2. **R5-a no mueve renglones de tablas**: 468 tablas serializadas en S0-4b y 468 en la salida, el mismo conjunto, el
   mismo texto de cada bloque y en la misma unidad. La guarda no bloqueó ningún párrafo de las 43 listas (0 eventos
   `r5a_no_mueve_tabla`). En `tablas_<to>.json` cambia solo la lista de unidades que cubren cuatro tablas, por los ids
   nuevos de R5-c y R5-e (ri_ccna 001, 003 y 005) y de R5-d (snp_tr 007) (`censos/tablas_S0-5a-bis.json`).
3. **R5-a′, R5-b, R5-c, R5-d y R5-e como en S0-5a**: `s0_5/scripts/aceptacion_S0-5a.py` sobre S0-4b y la salida de
   S0-5a-bis da lo mismo que en S0-5a: R5-a 9 de 9 casos y 27 de 27 correctos; R5-a′, R5-b, R5-d y R5-e OK; R5-c 9 de 9 y
   4 de 4. Los 4 encabezados de verdad de R5-d tienen ahora la herencia de S0-4b, porque gerc 2.4.3 ya no se toca
   (`censos/aceptacion_S0-5a_sobre_bis.json`).
4. **R5-f**: en ri_ccna abren 2.1.1 a 2.1.8 de D1A1 («2.1.1.no sean socios…», con el texto del renglón sin cambios),
   5.1 y 8.1 de D1A1 y 5.1 de D1A2; `ri_ccna::D1A1::S5::chapeau_seccion` deja de existir (era el texto de 5.1). En
   snp_cheq, `snp_cheq::3.3.6.2` abre con «3.3.6.2. Instrucciones operativas.» y hereda de S3 y de 3.3, sin 3.3.6.
5. **R5-g** (agregado): «3. Aclaraciones» sale del texto propio de `ri_oc::S2`, y las 51 unidades de 3.1 a 3.51 heredan
   «3. Aclaraciones» en lugar de «3.»; S3 no es una clave propia. El rechazo de ri_oc desaparece y los otros 87 de la
   lista de la mesa siguen en la salida, 87 de 87, con el mismo motivo. Con R5-g sola cambian exactamente 52 claves,
   `ri_oc::S2` y las 51, y ningún otro TO.

## 4. Censo por regla (`s0_5/scripts/censo_por_regla_S0-5a.py`; `censos/censo_por_regla_S0-5a-bis.{json,md}`)

Cada regla sola contra todas apagadas (S0-4b), en los 152. El antes y el después de cada clave, en
`censos/antes_y_despues_S0-5a-bis.jsonl`.

| regla sola | TOs | unidades antes → después | creadas | quitadas | cambiadas |
|---|---|---|---|---|---|
| R5-a, por lista | 29 | 3.178 → 3.221 | 43 | 0 | 157 |
| R5-a′ | 1 | 184 → 184 | 1 | 1 | 11 |
| R5-b | 2 | 383 → 362 | 0 | 21 | 20 |
| R5-c | 4 | 327 → 318 | 0 | 9 | 105 |
| R5-d | 2 | 114 → 130 | 17 | 1 | 11 |
| R5-e | 1 | 164 → 164 | 0 | 0 | 2 |
| R5-f | 2 (ri_ccna, snp_cheq) | 417 → 428 | 12 | 1 | 13 |
| R5-g | 1 (ri_oc) | 184 → 184 | 0 | 0 | 52 |
| **todas** | **34** | **3.857 → 3.897** (9.625 → 9.665 en los 152) | **73** | **33** | **366** |

- Las creadas y las quitadas suman lo de la final (43 + 1 + 17 + 12 = 73; 1 + 21 + 9 + 1 + 1 = 33). Las cambiadas suman
  371 regla por regla y 366 en la final: 5 unidades cambian con dos reglas.
- **Sin atribución exacta** (dos reglas sobre la misma unidad): 14 de los 472 eventos. Son R5-f con R5-c en ri_ccna (los
  8 puntos que abre R5-f, 2.1.1 a 2.1.8 de D1A1, heredan el título de dos renglones que junta R5-c; y `2.1.9` y
  `2.1::intro` cambian con las dos) y R5-a con R5-c en ri_spi (`C.1::cierre`, que abre R5-a, y `C.1.1` a `C.1.3`
  heredan el título que junta R5-c). Los otros 458 son iguales a los de una regla sola; ningún evento de una regla sola
  falta en la final.
- R5-a, R5-a′, R5-b, R5-c, R5-d, R5-e y R5-f dan, solas, lo mismo que en la vuelta 1; R5-g suma 52 cambiadas en ri_oc.

## 5. Claves (`s0_5/scripts/claves_S0-5a.py`; `censos/claves_S0-5a-bis.json`)

- **Lista declarada**: 472 claves, 73 creadas, 33 quitadas y 366 cambiadas, cada una con su regla:
  - creadas: R5-a, los 43 cierres de los padres de las 43 listas; R5-a′, `ri_oc::Sbloque1`; R5-d, `ri_rml::1.2.4` y 16
    de snp_tr; R5-f, 11 de ri_ccna y `snp_cheq::3.3.6.2`;
  - quitadas: R5-a′, `ri_oc::SC::cierre`; R5-b, 21 intersticiales; R5-c, 9 chapeaux; R5-d, `snp_tr::1.6::intro`; R5-f,
    `ri_ccna::D1A1::S5::chapeau_seccion`;
  - cambiadas: R5-a 154, R5-c 100, R5-g 52, R5-b 20, R5-a′ 11, R5-d 11, R5-f 11, R5-e 2, y 5 con dos reglas.
- **Selftest de claves** (S0-4b contra S0-5a-bis): VEREDICTO OK, las observadas son exactamente las declaradas. **Control
  negativo**: sin `adfsp::1.1::cierre` y con `actgar::1.2` (que no cambia) agregada, da FALLA y nombra las dos
  (`censos/claves_control_negativo_S0-5a-bis.json`).
- **Contra S0-5a, unidad por unidad** (`scripts/contra_S0-5a_S0-5a-bis.py`; `censos/contra_S0-5a_S0-5a-bis.json`): 150
  unidades distintas en 18 TOs, todas explicadas por las dos listas de claves:
  - 57 revertidas: S0-5a las cambiaba con R5-a y S0-5a-bis las deja como en S0-4b (las listas que no se tocan);
  - 76 nuevas: R5-f 24 y R5-g 52;
  - 17 que cambian en las dos, de otro modo: R5-a en las dos 10 (ri_rml 1.4, los mixtos), R5-a y R5-c en las dos 3, R5-a
    y R5-c en S0-5a y solo R5-c en S0-5a-bis 2 (manual 2.3.1 y 2.3.2), R5-c en S0-5a y R5-c con R5-f en S0-5a-bis 2;
  - ninguna sin explicar.

## 6. Control de continuidad de la numeración (`s0_5/scripts/control_continuidad_numeracion.py`)

- **Antes** (S0-4b): 104 saltos en 15 TOs. **Después** (S0-5a-bis): 88 en 12 TOs, 16 (i) y 72 (ii); 1 con
  `posible_referencia` (la remisión de ctacte). Tanda 1: 5 saltos en 3 TOs, todos (i)
  (`censos/control_continuidad_S0-5a-bis.json`, `censos/lista_continuidad_S0-5a-bis.md`).
- **Se cierran 17**: los 11 de ri_ccna (2.1.1 a 2.1.8, 5.1 y 8.1 de D1A1; 5.1 de D1A2) y los 6 de R5-d (ri_rml 1.2.4;
  snp_tr 1.3.4 a 1.3.6, 1.4 y 1.5).
- **snp_cheq 3.3.6 queda como (i)**, sin descendientes tragados (antes, (i) con 3.3.6.2 tragado en `snp_cheq::3.3.5.1`).
- **Un salto nuevo, snp_cheq 3.3.6.1 (i), hueco**: con 3.3.6.2 abierto, el control ve que falta su hermano anterior. Es el
  salto del PDF que la nota declara («el PDF salta 3.3.6 y 3.3.6.1»), no un error de corte; pero contradice la letra de
  «ningún salto nuevo».
- **Lista para la autora**: 72 saltos, 0 de la tanda 1, 71 fuera de la tanda 1 (grupo 2) y 1 de la tanda 0.

## 7. El detector del 1.16

Sobre la salida de S0-5a-bis: 98 con el de S1-bis, 284 con la corrección, 285 con la unión (265 de listas de puntos y 20
de secciones), contra 317 sobre S0-4b y 277 sobre S0-5a (`censos/detector_116_sobre_S0-5a-bis.json`).

## 8. Límites y residuos, caso por caso (`scripts/limites_S0-5a-bis.py`; `censos/limites_S0-5a-bis.{json,md}`)

209 filas, cada una con su unidad, su página, su mecanismo y su destino:

- **los de los dos mixtos, tal cual de la v2** (3, grupo 2): los anexos I y II dentro de `ri_spi::C.1.3` (pp. 10 y 11);
  los puntos 15 y 16 del Anexo III y el Anexo IV dentro de `ri2_ae::14.3` (pp. 29 y 30 a 43);
- **los dos límites de un caso de la tercera nota** (2, grupo 2): «15. Verificación…» y «16. Cotejo…» (p. 29) dentro de
  `ri2_ae::14.3`, con el motivo que registra E0, `raiz_en_columna_profunda_111.9_vs_83.7`;
- **dos listas que no se tocan con residuo**: `seggar::5.3.5` («6. Instrumentación.» dentro del ítem; grupo 2, PENDIENTE
  de la autora) y `ri_cc::R5::2.2.1.2` (no se toca por decisión de la autora; sin adjudicar). Las otras 12 quedan como en
  S0-4b porque lo que sigue al último ítem es del ítem, y se listan aparte;
- **los candidatos de R5-a′ declarados** (22, grupo 2 si se confirman), con mi lectura de S0-5a;
- **los saltos de numeración** (72 para la autora y 16 (i) de información, entre ellos 3.3.6 y 3.3.6.1 de snp_cheq);
- **los del §3 del mandato de S0-5a** (5): `ri_iepsp::S0` (49 caracteres) y `ri_ieccm::S0` (33), `ri_icpipsp::A1C3::S2`
  (3.206), `ri_secoexpo::S17` (5.271) y `ri_mmsef::2.2::intro` (465, no cambia);
- **los 87 rechazos por columna profunda** que R5-g no toca, con la lectura de la mesa («sin leer»), y que siguen en la
  salida, 87 de 87; entre ellos, «15.» y «16.» de ri2_ae.

**Diferencia de conteo con la nota de la revisión**: dice «los otros 23 candidatos de afuera»; quedan declarados 22 (los
23 de afuera de ri_oc menos `ri_rml::1.2.3`, que la misma nota descarta).

## 9. Comandos

Como en `s0_5/REPORTE_S0-5a.md`, §10, con los scripts de `s0_5/scripts/` sobre las salidas de esta etapa, y:

```
python -B scripts/armar_proto_S0-5a-bis.py <correr_e0.py final> <correr_e0.py del prototipo>
scripts/lote_configuraciones_S0-5a-bis.sh <s05b> <copia> <python> FINAL NINGUNA TODAS r5a r5a2 r5b r5c r5d r5e r5f r5g
python -B scripts/aceptacion_S0-5a-bis.py --s04b <S0-4b> --s05a <S0-5a> --bis c_FINAL --lista-v2 <v2> --lista-88 <88> --solo-r5g c_r5g --out <json>
python -B scripts/contra_S0-5a_S0-5a-bis.py --s04b <S0-4b> --s05a <S0-5a> --bis c_FINAL --claves-s05a s0_5/censos/claves_S0-5a.json --claves-bis <claves> --out <json>
python -B scripts/limites_S0-5a-bis.py --bis c_FINAL --lista-v2 <v2> --candidatos-r5a2 s0_5/censos/lectura_candidatos_r5a2_S0-5a.json --continuidad <json> --limites-s05a <json> --lista-88 <88> --out-json <json> --out-md <md>
python -B s0_5/scripts/censo_por_regla_S0-5a.py --base c_NINGUNA --final c_FINAL --regla r5a=c_r5a … --regla r5g=c_r5g --out <json>
```

## 10. Repo, `.pyc` y convenciones

- **Foto sha256 del repo** (`s0_1/scripts/snapshot_repo.py`): a las 15:22:15, 48.312 archivos; a las 20:45:03, 48.577.
  Comparación: 265 nuevos, 0 borrados, 7 cambiados.
  - De esta sesión: los 43 nuevos de `s0_5/bis/`. Ningún otro archivo del repo.
  - Ajenos a esta sesión, 222 nuevos y 7 cambiados: los nuevos de `conf_matriz/` y `omisiones_cod/` (árbol de trabajo
    de otras unidades) y siete documentos de `docs/`. Cada uno lo explica un commit posterior a `0c271468` (`be88fdf9`,
    `90addb35`, `fdd0414e`, `c52255fb`, `34d83be5`, `6010273e`, `1e13cbdc`) o un cambio del árbol de trabajo sin
    commitear; ninguno queda sin explicar (`atribucion_cambios_repo_S0-5a-bis.txt`, en el paquete). El registro de S0-5a
    entró en `34d83be5` sin cambiar el contenido de `s0_5/` (la foto no lo da como cambiado).
- **`.pyc`** (sin `.git/` ni `.venv/`): 2.213, la misma lista que al empezar; ninguno nuevo en `.venv/`.
- **Grep de convenciones** sobre `s0_5/bis/` y sus subdirectorios (42 archivos; control positivo 16 de 16): 25
  coincidencias, todas en texto del corpus copiado en los censos (prosa de las normas); en el diseño, el informe, el
  FRENO, los scripts y el parche, 0. Ningún nombre de persona, ninguna referencia al origen de una decisión, ninguna
  ruta absoluta (`censos/grep_convenciones_S0-5a-bis.txt`). El log de `selftest_e0` lleva `<scratchpad>` en lugar de la
  ruta del scratchpad.
