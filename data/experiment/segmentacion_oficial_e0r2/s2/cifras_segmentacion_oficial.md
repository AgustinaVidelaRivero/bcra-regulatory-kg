# Cifras de la segmentación oficial (U-SEG-OFICIAL, S2)

Sobre la E0 corregida: el código de E0 de `2374968a` (`e0_lib.py` `d89aab1a…`, `correr_e0.py` `78c54c4c…`, `e0_tablas.py` `ab300a22…`), cuya salida de los 152 da los 768 archivos de `s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json` (`80adbd58…`) con su sha256, 10.478 unidades (`s2/controles/control_e0_S2a.json`). La salida no está en el repo: la regenera `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo1_S2.sh <repo> <trabajo>` en unos 6 minutos, USD 0.

Convenciones:
- Cada cifra lleva el archivo de `s2/cifras/` y la clave de donde sale; el comando de cada archivo está en el §0.
- La cifra legada va al lado, con su diferencia (corregida − legada), cuando el mandato la pide.
- ¹ ri_spi y ri_con se cuentan una sola vez, con la misma regla, en todas las cifras: van por su razón vigente con la E0 corregida, las decisiones 1 y 2 de la enmienda 8 (ri_spi, error de corte confirmado en S1-quater; ri_con, cadenas de encabezados heredados, BKL-0044). En la partición legada eran no segmentables (`docs/protocolo_entre_tandas.md:163-166`). La autora confirmó la regla para las cifras de S2 el 15/10/2026 (mandato, `:1036-1043`; enmienda 8, nota `:165`; protocolo, nota `:529`; `c2b6cb60`). La marca ¹ remite a esta nota.
- Clase de documento (decisión 6, 2A): normativa general (NG) y régimen informativo (RI), `escalado_prep/inventario_tos.csv` para los 152 y `reports/u_insumos_cap/estadisticas_corpus.md:233-237` para los 5 de desarrollo.
- Ningún archivo de `s2/cifras/` guarda texto de unidades ni renglones del PDF: solo ids, páginas y cuentas.

## 0. Archivos y comandos

| archivo de `s2/cifras/` | sha256 | comando |
|---|---|---|
| `resumen_healthcheck_tanda1_S2b.json` | `a6c3dcd4…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B <raíz>/data/experiment/reextraccion_v2/e0_chunking/healthcheck_e0.py --pdf <raíz>/…/pdfs/<to>.pdf … --salida <hc.json>` y `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/resumen_healthcheck_S2.py --hc <hc.json> --e0 <E0> --manifiesto <manifest S0-6b> --out <json>` |
| `comparar_e0_historicas_S2b.json` | `281b9455…` | `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_e0_historicas_S2b.sh <repo> <raíz> <trabajo> 92b45d6 e1c9456 9f6361e6` y `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/comparar_e0_historicas_S2.py --e0 92b45d6=<dir> --e0 e1c9456=<dir> --e0 9f6361e6=<dir> --e0 corregida=<E0> --out <json>` |
| `atribucion_particion_S2b.json` | `1a25468d…` | `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo2_S2b.sh …` (los tres `r5_escalera_particion.py --comparar --atribuir`) y `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/atribuir_particion_S2.py --r5 <r5 corregida> --r5-cierre <r5 e1c9456> --e0 <E0> --e0-cierre <dir> --e0-c2 <dir> --raiz <copia> --out <json>` |
| `escalera_r5_S2b.json` | `c8d9fa86…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/escalera_r5_S2.py --r5-r5 <r5 92b45d6> --r5-cierre <r5 e1c9456> --historicas <comparar_e0_historicas_S2b.json> --out <json>` |
| `cifras_punto3_S2b.json` | `703187ae…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/cifras_punto3_S2.py --e0 <E0> --raiz <copia> --out <json>` |
| `cifras_conjuntos_clases_S2b.json` | `449a4daa…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/cifras_conjuntos_clases_S2.py --e0 <E0> --raiz <copia> --out <json>` |
| `ablacion_b582_S2b.json` | `c90e4295…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/ablacion_b582_S2.py --codigo <raíz> --e0 <E0> --trabajo <dir> --out <json>` |
| `reglas_por_to_S2b.json` | `9742a6e2…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/reglas_por_to_S2.py --e0 <E0> --raiz <copia> --ablacion <json> --out <json>` |
| `p7_en_la_corregida_S2b.json` | `fca80b9c…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/p7_en_la_corregida_S2.py --e0 <E0> --raiz <copia> --trabajo <dir> --out <json>` |
| `roles_pagina_S2b.json` | `d94460b3…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/roles_pagina_S2.py --e0 <E0> --raiz <copia> --out <json>` |
| `censos_S2b.json` | `4313a42c…` | `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo2_S2b.sh …` (caché de renglones, censo de renglones, detector 1.16, censo de sub-documentos) y `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/resumen_censos_S2.py --lote <dir> --e0 <E0> --raiz <copia> --out <json>` |
| `s1quater_S2b.json` | `df66fe28…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/cifras_s1quater_S2.py --raiz <copia> --out <json>` |
| `resumen_healthcheck_tanda_final_S2c.json` | `16843464…` | `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo3_S2c.sh …` (`healthcheck_e0.py` de la raíz sobre los 98 PDFs) y `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/resumen_healthcheck_S2.py --hc <hc.json> --e0 <E0> --manifiesto <manifest S0-6b> --out <json>` |
| `tanda_final_S2c.json` | `ee86fc42…` | `PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/segmentacion_oficial_e0r2/s2/scripts/tanda_final_S2.py --e0 <E0> --raiz <copia> --censos <lote> --hc <resumen> --out <json>` |

`<E0>` es la salida de los 152 de la E0 corregida; `<raíz>`, la raíz mínima de `s0_4/scripts/raiz_minima.sh`; `<copia>`, una copia del repo hecha con el `rsync` de la cláusula de los despachos más `--exclude='NO_ABRIR_*'`.

En orden: `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_e0_historicas_S2b.sh <repo> <raíz> <historicas> 92b45d6 e1c9456 9f6361e6` (la E0 de los 152 con el código de cada commit), `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo2_S2b.sh <repo> <copia> <raíz> <E0> <historicas> <lote>` (los tres controles de R5 y los censos) y `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_cifras_S2b.sh <repo> <copia> <raíz> <E0> <historicas> <lote> <trabajo>` (el health-check, la ablación, todos los resúmenes y este documento). Las salidas crudas de los dos primeros traen texto del PDF y quedan fuera del repo.

El tramo 3 (§7) se suma con `zsh data/experiment/segmentacion_oficial_e0r2/s2/scripts/lote_tramo3_S2c.sh <repo> <copia> <raíz> <E0> <historicas> <lote> <trabajo>`, que corre `lote_cifras_S2b.sh` y después el health-check de la tanda final, su resumen, `tanda_final_S2.py` y este documento. Sin los JSON del tramo 3, el generador da la versión del tramo 2 (`96d7d1ab`).

## 1. Health-check de E0 de los 20 de la tanda 1 (agregado 5 del «seguí»)

Con `healthcheck_e0.py` de la raíz mínima (el código de la E0 corregida), sobre los PDFs de los 20 (`resumen_healthcheck_tanda1_S2b.json`, `filas`). Condición de entrada por documento: `docs/protocolo_entre_tandas.md:149-151` y `:188-190`; checklist `:77-78`.

- **Cobertura no exacta o ids repetidos en la tanda 1:** — (`frena_por_cobertura_o_ids`). Ninguno: no hay freno.
- **El health-check no reproduce `correr_e0` en 15 de 20:** da otras unidades que `unidades_por_to` en cajasc, ceninf, cirmo3, depaho, efemin, manori, nmcief, opefci, ri_ccna, ri_dcpc, ri_mmsef, ri_pgn, ri_rml, snp_cheq, snp_tr (`unidades_distintas`). Corre la escalera de e0_lib (`healthcheck_e0.py:85-206`) sin el driver de e0-r2, que agrega las reglas de U-R2-CODIGO, de C2 y de S0 y la partición por tamaño. Sus señales describen ese parseo, no la E0 que se extrae. Por eso van al lado, con la misma definición, dos señales medidas sobre la E0 corregida (columnas «E0»).
- **Modo de lectura:** el mismo en los 20 (`modo_distinto`: —).

| TO | veredicto | modo | unidades (hc / `unidades_por_to`) | cid (renglones; páginas) | páginas sin sección (hc / E0) | unidades grandes (hc / E0) | cobertura exacta (hc / E0) | ids repetidos (E0) |
|---|---|---|---|---|---|---|---|--:|
| ayccef | sano | `vigente` | 196 / 196 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| expaef | sano | `vigente` | 165 / 165 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| opefci | sano | `vigente` | 77 / 74 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| adrei | sano | `vigente` | 70 / 70 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| ri_ccna | unidades_anomalas_por_tamano | `sin_raiz` | 19 / 169 | 0 | 0 / 0 | 1 (8.2) / 0 | sí / sí | 0 |
| ri_rml | paginas_sin_seccion, unidades_anomalas_por_tamano | `vigente` | 27 / 46 | 0 | 3 / 3 | 1 (S4) / 1 (Sbloque14) | sí / sí | 0 |
| ri_gerc | sano | `vigente` | 15 / 15 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| ri_pgn | sano | `vigente` | 19 / 21 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| snp_cheq | cid | `vigente` | 528 / 265 | 2; 29 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| ceninf | cid | `sin_raiz` | 47 / 39 | 8; 15, 17 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| cirmo3 | paginas_sin_seccion | `vigente` | 240 / 256 | 0 | 15 / 0 | 0 / 0 | sí / sí | 0 |
| snp_tr | sano | `vigente` | 89 / 103 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| lingeef | cid | `vigente` | 613 / 613 | 13; 36, 90, 109, 113, 116, 117, 118 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| depaho | sano | `vigente` | 437 / 442 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| cajasc | sano | `vigente` | 289 / 287 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| manori | cid, unidades_anomalas_por_tamano | `vigente` | 16 / 152 | 57; 33, 36, 40, 80, 82, 84 | 0 / 0 | 2 (S2, 1.5) / 0 | sí / sí | 0 |
| efemin | cid | `vigente` | 121 / 119 | 1; 1 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| nmcief | sano | `sin_raiz` | 40 / 55 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| ri_dcpc | sano | `marcadores` | 129 / 75 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |
| ri_mmsef | sano | `sin_raiz` | 90 / 128 | 0 | 0 / 0 | 0 / 0 | sí / sí | 0 |

Veredictos del health-check: cid 4, cid+unidades_anomalas_por_tamano 1, paginas_sin_seccion 1, paginas_sin_seccion+unidades_anomalas_por_tamano 1, sano 12, unidades_anomalas_por_tamano 1 (`veredictos`). La unidad grande de ri_rml en la E0 (`ri_rml::Sbloque14`, 50.404 caracteres propios) es una de las 3 que la partición por tamaño no parte porque tiene una tabla serializada (§4, unidades partidas). En la tanda 0 las señales `cid`, páginas sin sección y unidades grandes no fueron criterio de exclusión: se registraron (`docs/preregistro_tanda0.md:212-216`). Para la tanda 1 lo decidió la autora el 15/10/2026, antes de ver este documento: se registran y se declaran por TO y no excluyen; la cobertura no exacta y los ids repetidos frenan (mandato, nota del 15/10/2026, `docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:1036-1043`, `c2b6cb60`).

## 2. Punto 1: diferencias contra `b584_particion/`

Con el control de R5 sin editar (`data/experiment/r2_codigo/r5_escalera_particion.py --comparar --atribuir`, `atribucion_particion_S2b.json`, claves `r5` y `r5_cierre`), sobre la E0 corregida y, al lado, sobre la E0 del cierre de U-R2-CODIGO (`e1c9456`), donde ese control no deja nada en «otra» (`r2_codigo/cierre_freno.md:50-72`).

| | E0 corregida | E0 de `e1c9456` (cierre) |
|---|--:|--:|
| TOs comparados | 152 | 152 |
| TOs con los mismos ids | 48 | 129 |
| ids, `ids_desambiguados` | 9 | 69 |
| ids, `otra` | 2.787 | 93 |
| ids, `particion_no_aplicada_por_tabla` | 0 | 8 |
| ids en «otra», causa `K` | 77 | 93 |
| ids en «otra», causa `otra` | 2.710 | 0 |
| chunks con texto distinto, `K` | 16 | 64 |
| chunks con texto distinto, `K (arrastre de un cambio de ids)` | 4 | 1 |
| chunks con texto distinto, `otra` | 424 | 0 |
| chunks con texto distinto, `pies` | 42 | 45 |
| chunks con texto distinto, `pies y K` | 2 | 5 |
| chunks con texto distinto, `tablas` | 124 | 146 |

Modo de lectura distinto del legado (`r5.modo_de_lectura_distinto`): ri_spi¹ (sin_raiz → sin_raiz_letra). TOs que quedan en 0 unidades: —.

**La atribución de «otra».** El `--atribuir` de R5 vuelve a leer el PDF con variantes de K y de pie del código vigente, sin las reglas de S0: lo que cambió S0 le queda en «otra». Entre `e1c9456` y la E0 corregida el código de E0 cambió solo en C2 de U-R2-CODIGO-2 (`9f6361e6`) y en S0 (`26c65024`, `18d9e056`, `af7ffdd4`, `2374968a`; `git log e1c9456..HEAD` de los tres archivos de E0). Cada caso de «otra» se busca en la E0 de esos commits (`atribuir_particion_S2.py`, docstring): «ya en e1c9456» (la diferencia ya estaba en el cierre, con la causa que R5 le da ahí), «C2» o «S0».

| clase por historia | ids | chunks con texto distinto |
|---|--:|--:|
| R5: K | 77 | 0 |
| S0 | 2.663 | 424 |
| ya en e1c9456 (clase de R5 en e1c9456: K) | 10 | 0 |
| ya en e1c9456 (clase de R5 en e1c9456: partición no aplicada por tabla) | 37 | 0 |
| **total** | 2.787 | 424 |

**«Otra» sin explicar: 0 ids y 0 chunks** (`otra_sin_explicar`). Las listas, por TO y por clase, en `ids` y `texto`; los TOs de cada clase, en `tos_por_clase_historica`.
- R5: K: 8 TOs, cirmo3, micemp, plandecuentas, ri_chr, ri_ieccm, ri_pspii, ri_rcl, snp_debin.
- S0: 110 TOs, actgar, adfsp, afiltr, apnf, ayccef, cajasc, cateloc, cedin, ceninf, consyr, convca, cryl, ctacor, ctavis, depaho, depinv, disres, dmrd, efemin, evacre, expaef, fabcra, fgarcp, fimipyme, finsec, garant, garopt, gerc, gescre, gracre, graloc, icmecma, inspag, jafip, lavdin, lingeef, manori, manual, nmaeef, nmcief (y 70 más).
- ya en e1c9456 (clase de R5 en e1c9456: K): 4 TOs, inspag, ri2_cs, ri_iepsp, ri_msrl.
- ya en e1c9456 (clase de R5 en e1c9456: partición no aplicada por tabla): 8 TOs, dmrd, ri2_cs, ri_cc, ri_niif, ri_pnp, ri_rml, ri_transpa, snp_dd.
- Ids desambiguados por L que no estaban en el cierre (`ids_L_posteriores_a_e1c9456`): ri_oc 1, ri_secoexpo 4, ri_transpa 3, ri_tsa 1.

**Qué cambió cada etapa del código, sobre los 152** (`comparar_e0_historicas_S2b.json`, `pares.<par>.totales` y `tos_con_cambios`; ids que salen, ids que entran, chunks comunes con texto distinto y con el mismo texto pero otra herencia):

| etapa | TOs con cambios | ids que salen | ids que entran | texto distinto | solo herencia |
|---|--:|--:|--:|--:|--:|
| K-a′+K-b (`92b45d6` → `e1c9456`) | 4 | 99 | 8 | 43 | 144 |
| C2 de U-R2-CODIGO-2 (`e1c9456` → `9f6361e6`) | 9 | 0 | 0 | 0 | 93 |
| S0 (`9f6361e6` → E0 corregida) | 112 | 830 | 1.923 | 459 | 754 |

C2 no mueve ids ni texto en los 152; cambia solo la herencia de 93 unidades en 9 TOs, que es el punto (h), el tope de la herencia (`data/experiment/r2_codigo2/freno_c2.md:69`: 93 unidades en 9 TOs). El control de R5 compara solo `texto`, así que (h) no le aparece. (f) y (l) actúan solo en ric, que no está en los 152 (`ric_en_los_152`: no), y (n) escribe `pies_<to>.json` sin tocar los chunks (`freno_c2.md:42,68,73`).

## 3. Punto 2: la escalera de R5

El control de R5 sobre la E0 de los 152 con el código de cada commit (`lote_e0_historicas_S2b.sh`, después `r5_escalera_particion.py --comparar --atribuir` con el `e0_lib` de ese commit; `escalera_r5_S2b.json`, claves `obtenido` y `reproduce`). Entre paréntesis, la cifra del FRENO de cada corrida.

| código | TOs con los mismos ids | ids L | partición por tabla | ids K | texto distinto por clase | «otra» (ids / texto) | reproduce |
|---|--:|--:|--:|---|---|---|---|
| `92b45d6` (`r5_freno.md`) | 128 (128) | 69 (69) | 7 (7) | 205 en 19 (205 en 19) | tablas 145 (145), K 72 (72), K (arrastre de un cambio de ids) 32 (32), pies 45 (45), pies y K 5 (5) | 0 / 0 (0 / 0) | sí |
| `e1c9456` (`cierre_freno.md`) | 129 (129) | 69 (69) | 8 (8) | 93 en 16 (93 en 16) | tablas 146 (146), K 64 (64), K (arrastre de un cambio de ids) 1 (1), pies 45 (45), pies y K 5 (5) | 0 / 0 (0 / 0) | sí |

- **Con `e1c9456` se reproduce el cierre, no la corrida de R5.** `e1c9456` ya trae K-a′+K-b; las cifras del FRENO R5 (205 ids de K en 19 TOs) salen con el código de `92b45d6`. Las dos se reproducen: `92b45d6` sí, `e1c9456` sí.
- **Lo que explica K-a′+K-b** (`92b45d6` → `e1c9456`, `comparar_e0_historicas_S2b.json`, `pares["92b45d6 -> e1c9456"]`): cambia 4 TOs, nmaeef, ri_rml, snp_cheq, snp_dd; salen 99 ids, entran 8, cambia el texto de 43 chunks y solo la herencia de 144. Son los cuatro TOs del commit (`git show e1c9456`).
  En qué quedaron en la E0 corregida (`punto_2_ka_kb_en_la_final`):
  - nmaeef: textos que cambió: 1; siguen iguales 0, cambiaron después 0, id que ya no está (lo movió S0) 1.
  - ri_rml: ids que trajo: 1, siguen 1 (1 con el mismo texto); textos que cambió: 2; siguen iguales 0, cambiaron después 1, id que ya no está (lo movió S0) 1.
  - snp_cheq: ids que trajo: 7, siguen 7 (5 con el mismo texto); ids que quitó: 97, siguen fuera 97; textos que cambió: 36; siguen iguales 5, cambiaron después 1, id que ya no está (lo movió S0) 30.
  - snp_dd: ids que quitó: 2, siguen fuera 2; textos que cambió: 4; siguen iguales 3, cambiaron después 1, id que ya no está (lo movió S0) 0.
- **El punto (f):** 0 diferencias en los 152. Solo actúa en ric (`RENUMERACIONES_E0_R2`, `correr_e0.py:86-87`), que es de desarrollo y no está en los 152 (`comparar_e0_historicas_S2b.json`, `ric_en_los_152`).

## 4. Punto 3: las cifras que la tesis va a citar

Archivo: `cifras_punto3_S2b.json`.

**TOs por vía y por modo de lectura** (`via_por_modo`; la vía, de `s1ter/manifiesto/segmentacion_oficial_e0r2_152.json`, `818c3a43`; el modo, de `conteos.json` de la E0 corregida y de `conteos_b584.json`):

| vía | `marcadores` (corregida / legada) | `sin_raiz` (corregida / legada) | `sin_raiz_letra` (corregida / legada) | `vigente` (corregida / legada) | total |
|---|--:|--:|--:|--:|--:|
| fuera | 0 / 0 | 3 / 3 | 0 / 0 | 0 / 0 | 3 |
| por_pagina | 0 / 0 | 9 / 9 | 0 / 0 | 0 / 0 | 9 |
| por_punto | 5 / 5 | 43 / 44 | 1 / 0 | 91 / 91 | 140 |

La legada no tiene `sin_raiz_letra`: es la lectura sin raíz con el marcador de letra (regla 4 de S0), que la E0 corregida usa solo en ri_spi¹ (`correr_e0.py:1561-1571`).

**Páginas y unidades por clase** (`por_clase`; la clase, de `particion_152.json`, `clase`):

| clase | TOs | páginas | unidades | unidades legadas | diferencia |
|---|--:|--:|--:|--:|--:|
| no segmentables declarados | 10 | 134 | 17 | 10 | +7 |
| parciales declarados | 2 | 2.413 | 89 | 46 | +43 |
| reconocidos plenos | 138 | 4.183 | 10.242 | 9.266 | +976 |
| ri_spi¹ y ri_con¹ | 2 | 27 | 130 | 2 | +128 |
| **total** | 152 | 6.757 | 10.478 | 9.324 | +1.154 |

| clase de documento | TOs | páginas | unidades | unidades legadas |
|---|--:|--:|--:|--:|
| normativa general | 99 | 3.322 | 8.645 | 8.348 |
| régimen informativo | 53 | 3.435 | 1.833 | 976 |

**Unidades** (`unidades_totales`, `chunks_terminales`, `mini_chunks`, `total.por_tipo`, `total.mini_por_rol`): 10.478 unidades; 9.095 chunks terminales (7.995 puntos terminales y 1.100 secciones sin puntos) y 1.383 mini-chunks (chapeau_seccion 227, cierre 243, intersticial 131, intro 782).

**Unidades partidas por tamaño** (`partidas_por_tamano`; umbral 26.182 caracteres propios, objetivo 13.091 por parte, `correr_e0.py:74-75`): 6 unidades partidas en 27 partes (0 partes siguen sobre el umbral); 3 quedan sin partir (tabla_serializada 3).
- cateloc: sin partir: `cateloc::Sbloque10` (48.321, tabla_serializada).
- manori: partidas: `manori::Sbloque4` en 5.
- manual: partidas: `manual::Sbloque5::chapeau_seccion` en 4; `manual::Sbloque16` en 6.
- ri_dsf: partidas: `ri_dsf::S10` en 4.
- ri_niif: sin partir: `ri_niif::Sbloque321` (29.873, tabla_serializada).
- ri_pnp: partidas: `ri_pnp::SV::chapeau_seccion` en 3.
- ri_rml: sin partir: `ri_rml::Sbloque14` (50.404, tabla_serializada).
- snp_mep: partidas: `snp_mep::Sbloque1` en 5.

**Tablas** (`tablas`): la lectura de tablas corre en 152 TOs (e0-r2 escribe `tablas_<to>.json` para todos, `correr_e0.py:1744`); encuentra tablas en 124: 916 tablas (e0_tablas 914, r_tc2 2; parseada 907, declarada 9), 467 serializadas en 55 TOs; 324 unidades llevan una tabla serializada (`flags.tablas_e0[].serializada`), en 55 TOs.

**Ids desambiguados y chunks de índice que quedan** (`ids_desambiguados`): 9 ids desambiguados por L en 4 TOs (ri_oc 1, ri_secoexpo 4, ri_transpa 3, ri_tsa 1); de esos chunks, 0 están en páginas de rol índice (`pies_<to>.json`): no queda ningún chunk de índice leído como cuerpo entre los desambiguados. La partición legada repetía 69 ids en 4 TOs, todos por un índice leído como cuerpo (adfsp 9, ceninf 4, cirmo3 52, ri_niif 4; `docs/checklist_pre_escalado.md:149`, R33).

**Encabezados conservados por K** (`encabezados_conservados_K`): 334 renglones en 58 TOs: adfsp 2, apnf 5, cateloc 56, cirmo3 1, inspag 6, manori 23, manual 15, micemp 1, nmaeef 6, nmcief 3, opecam 1, ordcom 2, plandecuentas 4, ri2_ae 1, ri2_cs 10, ri2_pm 20, ri_acsf 1, ri_ai 3, ri_cc 19, ri_ccna 29, ri_ccpnp 10, ri_chr 3, ri_con¹ 1, ri_dcpc 3, ri_esd 2, ri_fcem 1, ri_icpipsp 7, ri_ieccm 1, ri_iepsp 1, ri_iesinap 5, ri_ii_31_12_19 5, ri_itme 1, ri_laft 1, ri_msrl 7, ri_nge 1, ri_oc 4, ri_ot 1, ri_pfmipyme 1, ri_pnp 16, ri_pscpp 1, ri_psp 3, ri_pspapt 1, ri_pspii 1, ri_psprca 1, ri_rem 2, ri_rml 8, ri_secoexpo 11, ri_spi¹ 5, ri_tii 6, ri_transpa 3, ri_tsa 1, ribspc 2, snp_cheq 2, snp_dd 1, snp_debin 1, snp_mep 2, snp_tr 2, traval 2.

**Los no segmentables y los parciales, con sus páginas** (`no_segmentables_y_parciales`):

| TO | grupo | páginas | unidades | tipos | modo |
|---|---|--:|--:|---|---|
| optico | no segmentable | 43 | 1 | seccion_sin_puntos 1 | `sin_raiz` |
| plandecuentas | no segmentable | 77 | 1 | seccion_sin_puntos 1 | `sin_raiz` |
| ri_chr | no segmentable | 1 | 2 | seccion_sin_puntos 2 | `sin_raiz` |
| ri_fcem | no segmentable | 1 | 1 | seccion_sin_puntos 1 | `sin_raiz` |
| ri_itme | no segmentable | 1 | 3 | seccion_sin_puntos 3 | `sin_raiz` |
| ri_pfmipyme | no segmentable | 1 | 2 | seccion_sin_puntos 2 | `sin_raiz` |
| ri_pscpp | no segmentable | 1 | 1 | seccion_sin_puntos 1 | `sin_raiz` |
| ri_pspii | no segmentable | 1 | 3 | seccion_sin_puntos 3 | `sin_raiz` |
| ri_rem | no segmentable | 2 | 2 | seccion_sin_puntos 2 | `sin_raiz` |
| ri_tii | no segmentable | 6 | 1 | seccion_sin_puntos 1 | `sin_raiz` |
| ri_con¹ | fuera por la enmienda 8, decisión 2 | 16 | 34 | seccion_sin_puntos 34 | `sin_raiz` |
| ri_spi¹ | fuera por la enmienda 8, decisión 1 | 11 | 96 | seccion_sin_puntos 4, punto_terminal 87, mini_chunk 5 | `sin_raiz_letra` |
| manual | parcial | 2.037 | 52 | seccion_sin_puntos 27, punto_terminal 15, mini_chunk 10 | `sin_raiz` (vía fuera) |
| ri2_pm | parcial | 376 | 37 | seccion_sin_puntos 7, punto_terminal 24, mini_chunk 6 | `sin_raiz` (vía por_punto) |

En la E0 corregida quedan 10 no segmentables, con 134 páginas y 17 unidades, todas secciones sin puntos; en la partición legada eran 12, con 161 páginas y 12 unidades. Los parciales: 2, con 2.413 páginas y 89 unidades (legadas: 46).

## 5. Punto 4: las cifras que la tesis toma de la segmentación fuera de la sección 4.1

Archivo: `cifras_conjuntos_clases_S2b.json`. Las definiciones son las del reporte legado (`reports/u_insumos_cap/u_insumos_i1.py`, `ded3494`), sin adaptar: unidad, cada elemento de `chunks_<to>.json` (R3); punto de la estructura, cada nodo de tipo punto de `estructura_<to>.json`, terminal si no tiene hijos (R12, `:370-385`). La legada reproduce las cifras del reporte (control abajo). Fuentes de la corregida: la E0 corregida para los 152 y la e0-r2 de la tanda 0 (`salida_tanda0_r2b/`, `9f6361e`) para los 5 de desarrollo; de la legada: `b584_particion/` y `salida_tanda0/` (la del reporte, `u_insumos_i1.py:262-277`).

### 4.a. Las unidades por conjunto (decisión 6, 1A)

Desarrollo: cap, cla, ext, pro, ric. Validación: actgar, adrei, ayccef, cryl, ctacor, expaef, lavdin, opefci, prevmi, traval (`esq/documentos_excluidos_evaluacion_final.json`, origen ESQ-2). Universo a escalar: los 152. Los conjuntos se solapan: la validación está dentro de los 152.

| conjunto | TOs | unidades (corregida / legada / dif.) | `mini_chunk` | `punto_terminal` | `seccion_sin_puntos` |
|---|--:|---|---|---|---|
| desarrollo | 5 | 1.768 / 1.763 / +5 | 287 / 286 | 1.479 / 1.475 | 2 / 2 |
| validación | 10 | 770 / 762 / +8 | 115 / 117 | 640 / 640 | 15 / 5 |
| universo a escalar (los 152) | 152 | 10.478 / 9.324 / +1.154 | 1.383 / 1.550 | 7.995 / 7.430 | 1.100 / 344 |

Mini-chunks por rol, corregida / legada (`4a.<lado>.<conjunto>.mini_por_rol`):
- desarrollo: chapeau_seccion 8 / 8, cierre 57 / 57, intersticial 3 / 3, intro 219 / 218.
- validación: chapeau_seccion 7 / 7, cierre 14 / 12, intersticial 1 / 0, intro 93 / 98.
- universo a escalar (los 152): chapeau_seccion 227 / 121, cierre 243 / 173, intersticial 131 / 446, intro 782 / 810.
- Control de la legada contra el reporte (`estadisticas_corpus.md`): desarrollo 1.763 unidades (1.763), tanda 0 671 (671), 152 9.324 (9.324); puntos terminales 1.475 de 1.810 (1.475 de 1.810), 577 de 710 (577 de 710) y 7.413 de 9.105 (7.413 de 9.105).

### 4.b. Los puntos de la estructura y el porcentaje de terminales, por clase (decisión 6, 2A, sobre los 157)

| clase | TOs | puntos (corregida / legada / dif.) | terminales (corregida / legada) | % terminales (corregida / legada / dif.) |
|---|--:|---|---|---|
| normativa general | 103 | 10.571 / 10.157 / +414 | 8.541 / 8.218 | 80,8 % / 80,9 % / -0,1 |
| régimen informativo | 54 | 1.064 / 758 / +306 | 933 / 670 | 87,7 % / 88,4 % / -0,7 |
| los 157 | 157 | 11.635 / 10.915 / +720 | 9.474 / 8.888 | 81,4 % / 81,4 % / 0,0 |

La legada da las cifras que hoy cita la tesis (10.157 y 758 puntos; 80,9 % y 88,4 %), que no tenían artefacto en el repo: ahora lo tienen, en `4b.legada`. Clase de los 5 de desarrollo: cap, cla, ext y pro NG, ric RI (`categoria_desarrollo`).

### 4.c. El «primer nivel como sección» (decisión 6, 3A, con 3B como control)

| fila | corregida | legada |
|---|--:|--:|
| leídos sin raíz (`sin_raiz` y `sin_raiz_letra`) | 56 | 56 |
| 3A: primer nivel como sección | 44 | 42 |
| 3A, en parte (parciales) | 2 | 2 |
| no segmentables | 10 | 12 |
| 3B: sin unidades `S<n>` | 41 | 34 |
| 3B, segunda lectura: sin secciones no sintéticas en `estructura` | 52 | 53 |

- **3A, corregida** (`4c.corregida.3A.lista`): asomut, cedin, ceninf, consyr, dmrd, micemp, nmaeef, nmcief, ri2_ae, ri2_cs, ri_acsf, ri_ao, ri_bdp, ri_ccna, ri_ccpnp, ri_con¹, ri_cr, ri_dsf, ri_esd, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_laft, ri_mmsef, ri_nge, ri_niif, ri_oc, ri_ot, ri_pnp, ri_pspapt, ri_psprca, ri_rcl, ri_saofe, ri_secoexpo, ri_sef, ri_spi¹, ri_tar, ri_transpa, ri_tvf, ribspc, seggar, verac.
- **3A, legada:** asomut, cedin, ceninf, consyr, dmrd, micemp, nmaeef, nmcief, ri2_ae, ri2_cs, ri_acsf, ri_ao, ri_bdp, ri_ccna, ri_ccpnp, ri_cr, ri_dsf, ri_esd, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_laft, ri_mmsef, ri_nge, ri_niif, ri_oc, ri_ot, ri_pnp, ri_pspapt, ri_psprca, ri_rcl, ri_saofe, ri_secoexpo, ri_sef, ri_tar, ri_transpa, ri_tvf, ribspc, seggar, verac. Con la partición legada, 3A da 42 + 2, como `reports/u_cap3_datos/datos.json` (`D3.particion_de_los_84.modo_lectura_por_clase`; 42 + 2).
- **En parte:** manual, ri2_pm. **No segmentables, corregida:** optico, plandecuentas, ri_chr, ri_fcem, ri_itme, ri_pfmipyme, ri_pscpp, ri_pspii, ri_rem, ri_tii; legada: optico, plandecuentas, ri_chr, ri_con¹, ri_fcem, ri_itme, ri_pfmipyme, ri_pscpp, ri_pspii, ri_rem, ri_spi¹, ri_tii.
- ri_spi¹ (sin_raiz_letra, 96 unidades) y ri_con¹ (sin_raiz, 34 unidades) están en 3A de la corregida: la E0 corregida los lee sin raíz y ya no los deja en una sola unidad; quedan fuera del grafo por la enmienda 8.
- **3B (sin unidades `S<n>`), corregida:** actgar, ayccef, cajasc, ccbcra, cescar, cla, coltit, convca, ctacor, ctacte, ctavis, depaho, efemin, garant, garopt, gescre, gracre, graloc, horari, incuca, nmaeef, nmcief, opefci, pagjub, pimf, pognme, prevmi, regpri, relact, reqcac, retype, ri2_ae, ri_ai, ri_cc, ri_ccna, ri_psp, ri_rcl, servco, snp_tr_nc, supcon, venliq.
- **Difieren 3A y 3B, corregida:** en 3A y no en 3B, asomut, cedin, ceninf, consyr, dmrd, micemp, ri2_cs, ri_acsf, ri_ao, ri_bdp, ri_ccpnp, ri_con¹, ri_cr, ri_dsf, ri_esd, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_laft, ri_mmsef, ri_nge, ri_niif, ri_oc, ri_ot, ri_pnp, ri_pspapt, ri_psprca, ri_saofe, ri_secoexpo, ri_sef, ri_spi¹, ri_tar, ri_transpa, ri_tvf, ribspc, seggar, verac; en 3B y no en 3A, actgar, ayccef, cajasc, ccbcra, cescar, cla, coltit, convca, ctacor, ctacte, ctavis, depaho, efemin, garant, garopt, gescre, gracre, graloc, horari, incuca, opefci, pagjub, pimf, pognme, prevmi, regpri, relact, reqcac, retype, ri_ai, ri_cc, ri_psp, servco, snp_tr_nc, supcon, venliq. La lectura literal de 3B («sin unidades `S<n>`») mete los documentos `vigente` cuyas secciones tienen todas puntos y sin encabezado propio, y saca los sin raíz con una sección sintética que deja una unidad `S<n>`: no mide lo mismo que 3A.
- **3B, segunda lectura (sin secciones no sintéticas en `estructura`), corregida:** asomut, cedin, consyr, manual, micemp, nmaeef, nmcief, optico, plandecuentas, ri2_ae, ri2_cs, ri2_pm, ri_acsf, ri_ao, ri_bdp, ri_ccna, ri_ccpnp, ri_chr, ri_con¹, ri_cr, ri_dsf, ri_esd, ri_fcem, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_laft, ri_mmsef, ri_nge, ri_oc, ri_ot, ri_pfmipyme, ri_pnp, ri_pscpp, ri_pspapt, ri_pspii, ri_psprca, ri_rem, ri_saofe, ri_secoexpo, ri_sef, ri_spi¹, ri_tar, ri_tii, ri_transpa, ri_tvf, ribspc, seggar, verac. Difieren de 3A: en 3A y no aquí, ceninf, dmrd, ri_niif, ri_rcl (leídos sin raíz, con una sección no sintética); aquí y no en 3A, manual, optico, plandecuentas, ri2_pm, ri_chr, ri_fcem, ri_itme, ri_pfmipyme, ri_pscpp, ri_pspii, ri_rem, ri_tii (los no segmentables y los parciales, que 3A excluye por definición). Esta lectura es una interpretación mía del «control por la estructura» de la decisión 6: la dejo al lado, declarada.

### 4.d. Las reglas vigentes, con el lugar del código y los TOs de cada una

Archivo: `reglas_por_to_S2b.json` (y `ablacion_b582_S2b.json` para las tres reglas de B5.8.2). Tres capas, descritas en el docstring de `reglas_por_to_S2.py`. Los TOs son sobre los 152; «en los 84» cuenta los del universo del D3 legado (`segmentacion_84/censo_84.json`), para ponerlo al lado de la cifra legada.

**Capa A: las 21 reglas de la tabla D3 legada, con el mismo criterio** (`capa_a_D3`):

| regla | unidad | criterio | código | TOs (152) | en los 84 | legado (84) | TOs |
|---|---|---|---|--:|--:|--:|---|
| sin_raiz | B5.8.1 | modo_lectura sin_raiz (o sin_raiz_letra, su variante de S0) | `e0_lib.py:1274`; `e0_lib.py:2362` | 56 | 56 | 56 | asomut, cedin, ceninf, consyr, dmrd, manual, micemp, nmaeef, nmcief, optico, plandecuentas, ri2_ae, ri2_cs, ri2_pm, ri_acsf, ri_ao, ri_bdp, ri_ccna, ri_ccpnp, ri_chr, ri_con¹, ri_cr, ri_dsf, ri_esd, ri_fcem, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_laft, ri_mmsef, ri_nge, ri_niif, ri_oc, ri_ot, ri_pfmipyme, ri_pnp, ri_pscpp, ri_pspapt, ri_pspii, ri_psprca, ri_rcl, ri_rem, ri_saofe, ri_secoexpo, ri_sef, ri_spi¹, ri_tar, ri_tii, ri_transpa, ri_tvf, ribspc, seggar, verac |
| raiz_explicita | B5.8.1 | ≥1 sección sintética con número ≠ '0' y título no vacío | `e0_lib.py:2373` | 46 | 46 | 44 | asomut, cedin, consyr, dmrd, manual, micemp, nmaeef, ri2_ae, ri2_cs, ri2_pm, ri_acsf, ri_ao, ri_bdp, ri_ccpnp, ri_chr, ri_con¹, ri_cr, ri_dsf, ri_esd, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_laft, ri_mmsef, ri_nge, ri_niif, ri_oc, ri_ot, ri_pfmipyme, ri_pnp, ri_pspapt, ri_pspii, ri_psprca, ri_rem, ri_saofe, ri_secoexpo, ri_spi¹, ri_tar, ri_transpa, ri_tvf, ribspc, seggar, verac |
| G0 | B5.8.1 | motivo 'raiz_banner_repetido' | `e0_lib.py:2380` | 1 | 1 | 0 | ri_ii_31_12_19 |
| G1 | B5.8.1 | motivo 'raiz_sin_forma_de_titulo' | `e0_lib.py:2382` | 4 | 4 | 4 | manual, nmcief, ri_ccna, ri_saofe |
| G2 | B5.8.1 | motivo 'raiz_<n>_no_sucede_a_<m>' | `e0_lib.py:2384` | 22 | 22 | 28 | ceninf, manual, nmaeef, ri2_ae, ri2_pm, ri_bdp, ri_ccna, ri_cr, ri_dsf, ri_esd, ri_iepsp, ri_nge, ri_niif, ri_pnp, ri_pspapt, ri_psprca, ri_rem, ri_saofe, ri_secoexpo, ri_tar, ri_transpa, ri_tvf |
| G3 | B5.8.1 | motivo 'raiz_en_columna_profunda_…' | `e0_lib.py:2396` | 2 | 2 | 11 | ri2_cs, ri_saofe |
| raiz_implicita | B5.8.1 | ≥1 sección sintética con número ≠ '0' y título vacío | `e0_lib.py:2451` | 0 | 0 | 12 | — |
| preambulo | B5.8.1 | sección sintética con número '0' | `e0_lib.py:2187` | 41 | 40 | 32 | adfsp, ceninf, dmrd, manual, micemp, nmaeef, nmcief, optico, plandecuentas, ri2_ae, ri2_pm, ri_acsf, ri_ao, ri_cc, ri_ccna, ri_chr, ri_con¹, ri_dsf, ri_esd, ri_fcem, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_niif, ri_oc, ri_ot, ri_pfmipyme, ri_pnp, ri_pscpp, ri_pspapt, ri_pspii, ri_psprca, ri_saofe, ri_secoexpo, ri_sef, ri_spi¹, ri_tii, ribspc |
| paginas_de_registro | B5.8.1 | roles_pagina.ficha_registro > 0 | `e0_lib.py:1251` | 5 | 5 | 5 | manual, plandecuentas, ri2_pm, ri_laft, ri_transpa |
| marcadores | B5.8.2 | conteos.marcadores_b582 == true | `correr_e0.py:1552` | 7 | 7 | 7 | consyr, nmaeef, reqcac, ri_dcpc, ri_msrl, ri_psp, seguef |
| indice_variante | B5.8.2 | ablación: anular RE_MARCA_INDICE_B582 cambia el modo o los chunks | `e0_lib.py:356` | 6 | 6 | 6 | consyr, nmaeef, ri_dcpc, ri_msrl, ri_psp, seguef |
| seccion_variante | B5.8.2 | ablación: anular _match_seccion_b582 cambia el modo o los chunks | `e0_lib.py:910` | 3 | 3 | 3 | reqcac, ri_dcpc, ri_psp |
| banner_caja_mixta | B5.8.2 | ablación: anular detectar_banners_texto cambia el modo o los chunks | `e0_lib.py:1230` | 2 | 2 | 3 | reqcac, ri_msrl |
| parser_tablas | B5.8.3 | tablas_<to>.json: conteos_e0_tablas.rinde == true | `e0_tablas.py:340` | 124 | 57 | 29 | actgar, adfsp, adrei, afiltr, apnf, asomut, autenf, ayccef, cajasc, cateloc, ccbcra, cedin, ceninf, cescar, cirmo3, coltit, consyr, convca, cryl, ctacor, ctacte, ctavis, depaho, depinv, disres, dmrd, docvig, efemin, evacre, expaef, fabcra, fclef, fgarcp, fimipyme, finsec, garant, garopt, gerc, gescre, gracre, graloc, horari, icmecma, incuca, inspag, lavdin, lingeef, lingob, manori, manual, micemp, nmcief, opecam, opefci, ordcom, osapsa, pagjub, pfmipyme, pimf, pognme (y 64 más) |
| R-TC | B5.8.3 | conteos_e0_tablas.tablas_logicas > 0 | `e0_tablas.py:146` | 124 | 57 | 29 | actgar, adfsp, adrei, afiltr, apnf, asomut, autenf, ayccef, cajasc, cateloc, ccbcra, cedin, ceninf, cescar, cirmo3, coltit, consyr, convca, cryl, ctacor, ctacte, ctavis, depaho, depinv, disres, dmrd, docvig, efemin, evacre, expaef, fabcra, fclef, fgarcp, fimipyme, finsec, garant, garopt, gerc, gescre, gracre, graloc, horari, icmecma, incuca, inspag, lavdin, lingeef, lingob, manori, manual, micemp, nmcief, opecam, opefci, ordcom, osapsa, pagjub, pfmipyme, pimf, pognme (y 64 más) |
| R-TC sin_contenido | B5.8.3 | descartadas_por_regla_e0_tablas.conteos.sin_contenido > 0 | `e0_tablas.py:366` | 2 | 2 | 2 | manual, ri2_pm |
| R-COL | B5.8.3 | ≥1 tabla de e0_tablas con causa 'alineacion_no_confiable' | `e0_tablas.py:161` | 1 | 1 | 0 | snp_cheq |
| R-COSTURA | B5.8.3 | conteos_e0_tablas.costuras_aplicadas > 0 | `e0_tablas.py:317` | 58 | 28 | 15 | actgar, afiltr, autenf, ayccef, cajasc, ccbcra, cedin, ceninf, cirmo3, coltit, ctacte, ctavis, depaho, depinv, dmrd, efemin, expaef, fabcra, finsec, garant, garopt, gerc, gescre, gracre, inspag, lingeef, manori, opecam, opefci, pagjub, polcre, prevmi, rdbcra, relact, repefe, ri_acsf, ri_cc, ri_ccna, ri_cr, ri_dcpc, ri_dsf, ri_laft, ri_msrl, ri_niif, ri_pnp, ri_rml, ri_sef, ri_tsa, rmgcti, seggar, seguef, servco, snp_cec, snp_cheq, snp_mep, snp_spd, snp_tr, supcon |
| R-ENC | B5.8.3 | ≥1 tabla de e0_tablas con encabezado.estado ≠ 'no_determinado' | `e0_tablas.py:202` | 111 | 44 | 21 | actgar, adfsp, adrei, afiltr, apnf, asomut, autenf, ayccef, cajasc, cateloc, ccbcra, cedin, ceninf, cescar, cirmo3, coltit, consyr, convca, cryl, ctacor, ctacte, ctavis, depaho, depinv, disres, dmrd, docvig, efemin, evacre, expaef, fabcra, fclef, fgarcp, fimipyme, finsec, garant, garopt, gerc, gescre, gracre, graloc, horari, icmecma, incuca, inspag, lavdin, lingeef, lingob, manori, micemp, opecam, opefci, ordcom, osapsa, pagjub, pfmipyme, pimf, pognme, polcre, prevmi (y 51 más) |
| R-VERIF | B5.8.3 | ≥1 tabla de e0_tablas con causa 'perdida_reconstruccion' | `e0_tablas.py:249` | 5 | 3 | 2 | depaho, efemin, nmcief, ri_niif, snp_tr |
| R-NOTA | B5.8.3 | conteos_e0_tablas.notas_pie > 0 | `e0_tablas.py:284` | 14 | 10 | 7 | cajasc, ceninf, cirmo3, dmrd, fabcra, gerc, manori, rdbcra, ri2_cs, ri_cc, ri_niif, ri_pnp, ri_tii, ri_tsa |

Adaptaciones, declaradas en el docstring del script: `conteos.json` de e0-r2 no tiene `tabular` ni `preambulo`; los criterios de tablas leen `conteos_e0_tablas`, `descartadas_por_regla_e0_tablas` y las tablas de origen `e0_tablas`; el índice variante, la sección variante y el banner de caja mixta salen de la ablación (anular la regla y comparar), como el legado hacía con las dos últimas, sobre los 7 TOs con `marcadores_b582`; la corrida sin anular reproduce la E0 corregida en los 7 (`ablacion_b582_S2b.json`, `control_base_reproduce`). Las reglas de tablas corren ahora en los 152: el grupo de las tablas deja de ser propio de los 84.

**Capa B: las reglas de e0-r2 que dejan rastro en la salida** (`capa_b_rastro_en_la_salida`; el lugar del código es la primera línea donde aparece el literal que la salida registra):

| regla (rastro) | tipo de rastro | código | TOs (152) | en los 84 | TOs |
|---|---|---|--:|--:|---|
| `aceptado_con_columna_derivada` | aviso | `e0_lib.py:2590` | 62 | 36 | adfsp, cajasc, ccbcra, ceninf, cescar, cirmo3, ctacte, ctavis, depaho, docvig, efemin, finsec, garant, garopt, gerc, gracre, graloc, inspag, jafip, lavdin, lingeef, lingob, manori, manual, nmaeef, nmcief, pfmipyme, pimf, ratio, ratiofn, rdbcra, relact, retype, ri2_ae, ri2_ci, ri2_pm, ri_ai, ri_cc, ri_ccna, ri_dcpc (y 22 más) |
| `aceptado_fila_de_catalogo_r9` | aviso | `e0_lib.py:2607` | 1 | 0 | rdbcra |
| `aceptado_lista_minuscula` | aviso | `e0_lib.py:2600` | 1 | 1 | ri2_ae |
| `adoptado_a` | aviso | `e0_lib.py:3620` | 27 | 26 | adfsp, manual, nmaeef, nmcief, ri2_ae, ri2_cs, ri2_pm, ri_ao, ri_cc, ri_ccna, ri_ccpnp, ri_esd, ri_icpipsp, ri_iepsp, ri_iesinap, ri_niif, ri_oc, ri_ot, ri_pnp, ri_pspapt, ri_psprca, ri_secoexpo, ri_sef, ri_spi¹, ri_transpa, ri_tvf, ribspc |
| `apartado_de_seccion_ap` | aviso | `e0_lib.py:2508` | 1 | 1 | ri_ai |
| `apartado_letra_apl` | aviso | `correr_e0.py:1575` | 1 | 1 | ri_oc |
| `caratula_j` | aviso | `e0_lib.py:2087` | 2 | 2 | ceninf, optico |
| `cierre_al_margen_r5a` | aviso | `e0_lib.py:3130` | 6 | 4 | adfsp, ri_oc, ri_rml, ri_spi¹, snp_mep, tasint |
| `cuerpo_al_rotulo_m1` | aviso | `e0_lib.py:2682` | 5 | 5 | nmcief, ri2_ae, ri_dcpc, ri_mmsef, snp_cheq |
| `division_a` | aviso | `e0_lib.py:3578` | 55 | 48 | adfsp, afiltr, apnf, cateloc, cryl, depaho, dmrd, gescre, inspag, manori, manual, nmaeef, nmcief, opecam, ri2_cs, ri2_pm, ri_acsf, ri_ai, ri_ao, ri_cc, ri_ccpnp, ri_con¹, ri_dcpc, ri_esd, ri_icpipsp, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_laft, ri_msrl, ri_niif, ri_oc, ri_ot, ri_pfmipyme, ri_pgn, ri_pnp, ri_psp, ri_pspapt, ri_psprca (y 15 más) |
| `encabezado_de_tabla_con_su_tabla_f` | aviso | `e0_lib.py:3701` | 4 | 0 | cajasc, efemin, gerc, rdbcra |
| `encabezado_de_tabla_repetido_f` | aviso | `e0_lib.py:2094` | 4 | 3 | efemin, manual, ri2_pm, ri_msrl |
| `filas_de_catalogo_r9` | aviso | `correr_e0.py:1436` | 1 | 0 | rdbcra |
| `grupo_sin_columna_comun_c` | aviso | `e0_lib.py:3311` | 26 | 21 | adfsp, ayccef, ceninf, depaho, dmrd, fabcra, finsec, inspag, manori, manual, nmaeef, ri2_ae, ri_cc, ri_con¹, ri_gerc, ri_ii_31_12_19, ri_niif, ri_oc, ri_pnp, ri_rml, ri_secoexpo, ri_transpa, snp_cheq, snp_dd, snp_tr, venliq |
| `marcador_letra_r2` | aviso | `correr_e0.py:1570` | 1 | 1 | ri_spi¹ |
| `numero_en_referencia_r5d` | aviso | `e0_lib.py:2287` | 5 | 3 | cirmo3, gescre, lingeef, ri_rml, snp_tr |
| `numero_partido_g` | aviso | `e0_lib.py:1739` | 1 | 0 | lingeef |
| `numero_pegado_h` | aviso | `e0_lib.py:2626` | 4 | 3 | gerc, ri_cc, ri_ccna, snp_dd |
| `padre_reabierto_r2` | aviso | `e0_lib.py:2040` | 3 | 3 | manori, nmaeef, snp_cheq |
| `pagina_cuerpo_sin_seccion` | aviso | `e0_lib.py:2136` | 4 | 4 | reqcac, ri_cc, ri_rml, ri_tsa |
| `parrafo_por_columna_c` | aviso | `e0_lib.py:3306` | 53 | 28 | adfsp, afiltr, apnf, cajasc, cedin, ceninf, consyr, cryl, ctacor, ctavis, depaho, depinv, efemin, evacre, fabcra, fgarcp, fimipyme, finsec, garant, gracre, icmecma, manori, manual, nmaeef, nmcief, opecam, osapsa, prevmi, ratio, regpri, retype, ri2_ae, ri2_pm, ri_cc, ri_ccna, ri_dcpc, ri_icpipsp, ri_niif, ri_oc, ri_pnp (y 13 más) |
| `raiz_g3_subdocumento_sd` | aviso | `e0_lib.py:2428` | 2 | 2 | nmcief, ri2_ae |
| `raiz_m2` | aviso | `e0_lib.py:2420` | 9 | 9 | manual, nmcief, ri2_pm, ri_ao, ri_dsf, ri_icpipsp, ri_tar, seggar, verac |
| `raiz_mayor_a_max_subdocumento_sdmax` | aviso | `e0_lib.py:2432` | 1 | 1 | ri_ccna |
| `raiz_sucesora_e` | aviso | `e0_lib.py:2423` | 4 | 4 | ri_laft, ri_oc, ri_saofe, seggar |
| `recuadro_por_columna_i` | aviso | `e0_lib.py:1807` | 1 | 1 | ri_ccna |
| `rotulo_letra_numero_sdla` | aviso | `e0_lib.py:2305` | 1 | 1 | ri_ccna |
| `rotulo_por_lista_r5f` | aviso | `e0_lib.py:2265` | 1 | 1 | snp_cheq |
| `rotulo_vertical_r5e` | aviso | `e0_lib.py:3750` | 1 | 1 | ri_ccna |
| `seccion_reabierta` | aviso | `e0_lib.py:2152` | 1 | 1 | ri_tsa |
| `segmento_por_columna_c` | aviso | `e0_lib.py:3359` | 5 | 3 | depaho, fimipyme, manori, ratio, snp_cheq |
| `subdocumento_sd` | aviso | `e0_lib.py:2064` | 12 | 11 | adfsp, nmaeef, nmcief, ri2_ae, ri_cc, ri_ccna, ri_icpipsp, ri_iepsp, ri_iesinap, ri_oc, ri_sef, ri_spi¹ |
| `tabla_fundida_en_un_intersticial_r2` | aviso | `correr_e0.py:1455` | 2 | 2 | snp_cheq, snp_dd |
| `fila_de_lista_de_codigos_r<n>` | guarda (rechazos_header) | `e0_lib.py:2360` | 1 | 1 | ri_dsf |
| `fuera_de_seccion_<n>` | guarda (rechazos_header) | `e0_lib.py:2518` | 76 | 41 | actgar, adfsp, afiltr, apnf, ayccef, cajasc, cedin, ceninf, cirmo3, coltit, ctacor, ctacte, ctavis, depaho, depinv, disres, dmrd, efemin, expaef, fabcra, fgarcp, fimipyme, finsec, garant, gerc, gescre, horari, jafip, lingeef, lingob, manori, manual, nmaeef, pognme, polcre, prevmi, pscpp, ratio, ratiofn, regpri (y 36 más) |
| `fuera_de_seccion_III` | guarda (rechazos_header) | `e0_lib.py:2518` | 1 | 1 | ri_psp |
| `indice_l` | guarda (rechazos_header) | `e0_lib.py:239` | 2 | 2 | nmaeef, ri2_ae |
| `lista_de_puntos_r<n>` | guarda (rechazos_header) | `e0_lib.py:2399` | 3 | 3 | manori, nmaeef, ri2_ae |
| `no_sucede_al_hermano_<n>` | guarda (rechazos_header) | `e0_lib.py:2337` | 26 | 10 | afiltr, ayccef, cajasc, ctacor, ctacte, ctavis, depaho, efemin, finsec, gerc, inspag, lingeef, manual, opecam, raapal, ratiofn, rdbcra, regpri, ri2_pm, ri_gerc, ri_oc, ri_pgn, ri_spi¹, seguef, snp_psp, tasint |
| `numero_en_referencia_r<n>d` | guarda (rechazos_header) | `e0_lib.py:2287` | 5 | 3 | cirmo3, gescre, lingeef, ri_rml, snp_tr |
| `numero_pegado_no_sucede_al_hermano_<n>_h` | guarda (rechazos_header) | `e0_lib.py:2552` | 20 | 5 | cajasc, depaho, efemin, expaef, fabcra, gerc, gescre, gracre, incuca, lavdin, lingeef, pimf, ratio, rdbcra, relact, ri2_ae, ri_dcpc, ri_ii_31_12_19, ri_oc, traval |
| `padre_<n>.<n>.<n>_no_abierto` | guarda (rechazos_header) | `e0_lib.py:1702` | 16 | 7 | ayccef, cajasc, ccbcra, cirmo3, depaho, efemin, expaef, opecam, raapal, ri_iesinap, ri_mmsef, ri_msrl, ri_tsa, snp_cec, snp_cheq, snp_tr_nc |
| `padre_<n>.<n>_no_abierto` | guarda (rechazos_header) | `e0_lib.py:1702` | 18 | 6 | cajasc, cescar, cirmo3, depaho, efemin, expaef, gerc, ratiofn, rdbcra, repefe, retype, ri_cc, ri_dsf, ri_msrl, ri_rml, ri_tsa, snp_cec, snp_tr_nc |
| `profundidad_<n>_es_seccion` | guarda (rechazos_header) | `e0_lib.py:2520` | 15 | 10 | afiltr, dmrd, expaef, fabcra, gescre, jafip, manori, prevmi, ri_cc, ri_dcpc, ri_rml, ri_tsa, snp_cheq, snp_dd, snp_tr |
| `raiz_<n>_no_sucede_a_<n>` | guarda (rechazos_header) | `e0_lib.py:206` | 22 | 22 | ceninf, manual, nmaeef, ri2_ae, ri2_pm, ri_bdp, ri_ccna, ri_cr, ri_dsf, ri_esd, ri_iepsp, ri_nge, ri_niif, ri_pnp, ri_pspapt, ri_psprca, ri_rem, ri_saofe, ri_secoexpo, ri_tar, ri_transpa, ri_tvf |
| `raiz_banner_repetido` | guarda (rechazos_header) | `e0_lib.py:2380` | 1 | 1 | ri_ii_31_12_19 |
| `raiz_en_columna_profunda_<n>.<n>_vs_<n>.<n>` | guarda (rechazos_header) | `e0_lib.py:2396` | 2 | 2 | ri2_cs, ri_saofe |
| `raiz_mayor_a_max` | guarda (rechazos_header) | `e0_lib.py:2432` | 17 | 12 | ceninf, cirmo3, convca, ctacte, depinv, horari, manual, polcre, ri_dcpc, ri_dsf, ri_nge, ri_niif, ri_pnp, ri_rml, ri_sef, snp_atm, snp_tr |
| `raiz_sin_forma_de_titulo` | guarda (rechazos_header) | `e0_lib.py:2382` | 4 | 4 | manual, nmcief, ri_ccna, ri_saofe |
| `remision_envuelta_r<n>` | guarda (rechazos_header) | `e0_lib.py:2355` | 2 | 1 | rdbcra, ri_tsa |
| `resto_minuscula_y_columna_<n>.<n>_incompatible_hermanos_en_<n>.<n>` | guarda (rechazos_header) | `e0_lib.py:2613` | 2 | 0 | cescar, depinv |
| `resto_minuscula_y_salto_de_<n>_a_<n>_sin_contexto_de_lista` | guarda (rechazos_header) | `e0_lib.py:2557` | 6 | 3 | efemin, relact, ri_ii_31_12_19, ri_rml, ri_sef, snp_cec |
| `resto_vacio_referencia_envuelta` | guarda (rechazos_header) | `e0_lib.py:2516` | 41 | 15 | actgar, adfsp, autenf, ayccef, cajasc, cirmo3, consyr, cryl, ctacte, ctavis, depaho, docvig, fabcra, finsec, garopt, gerc, gracre, horari, icmecma, inspag, jafip, lingeef, ordcom, pfmipyme, polcre, prevmi, raapal, ratio, ratiofn, rdbcra, repefe, ri_gerc, ri_iesinap, ri_oc, ri_rml, ri_secoexpo, ri_tsa, rmgcti, seguef, snp_cec (y 1 más) |
| `apartado` | clave de nodo de estructura | `e0_lib.py:4892` | 1 | 1 | ri_ai |
| `division_a` | clave de nodo de estructura | `e0_lib.py:4894` | 55 | 48 | adfsp, afiltr, apnf, cateloc, cryl, depaho, dmrd, gescre, inspag, manori, manual, nmaeef, nmcief, opecam, ri2_cs, ri2_pm, ri_acsf, ri_ai, ri_ao, ri_cc, ri_ccpnp, ri_con¹, ri_dcpc, ri_esd, ri_icpipsp, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_laft, ri_msrl, ri_niif, ri_oc, ri_ot, ri_pfmipyme, ri_pgn, ri_pnp, ri_psp, ri_pspapt, ri_psprca (y 15 más) |
| `lineas_previas` | clave de nodo de estructura | `e0_lib.py:4896` | 4 | 0 | cajasc, efemin, gerc, rdbcra |
| `numero_impreso` | clave de nodo de estructura | `e0_lib.py:4888` | 1 | 1 | ri_ai |
| `prefijo` | clave de nodo de estructura | `e0_lib.py:4464` | 12 | 11 | adfsp, nmaeef, nmcief, ri2_ae, ri_cc, ri_ccna, ri_icpipsp, ri_iepsp, ri_iesinap, ri_oc, ri_sef, ri_spi¹ |
| `subdocumentos` | clave de nodo de estructura | `e0_lib.py:4913` | 12 | 11 | adfsp, nmaeef, nmcief, ri2_ae, ri_cc, ri_ccna, ri_icpipsp, ri_iepsp, ri_iesinap, ri_oc, ri_sef, ri_spi¹ |
| `C8 partición por tamaño (sub_chunking.json, particiones)` | agregado | `correr_e0.py:531` | 5 | 5 | manori, manual, ri_dsf, ri_pnp, snp_mep |
| `C8 sin partir (sub_chunking.json, no_particionables)` | agregado | `correr_e0.py:579` | 3 | 3 | cateloc, ri_niif, ri_rml |
| `K (encabezados_conservados.json)` | agregado | `correr_e0.py:1581` | 58 | 53 | adfsp, apnf, cateloc, cirmo3, inspag, manori, manual, micemp, nmaeef, nmcief, opecam, ordcom, plandecuentas, ri2_ae, ri2_cs, ri2_pm, ri_acsf, ri_ai, ri_cc, ri_ccna, ri_ccpnp, ri_chr, ri_con¹, ri_dcpc, ri_esd, ri_fcem, ri_icpipsp, ri_ieccm, ri_iepsp, ri_iesinap, ri_ii_31_12_19, ri_itme, ri_laft, ri_msrl, ri_nge, ri_oc, ri_ot, ri_pfmipyme, ri_pnp, ri_pscpp (y 18 más) |
| `L (ids_desambiguados.json)` | agregado | `e0_lib.py:4797` | 4 | 4 | ri_oc, ri_secoexpo, ri_transpa, ri_tsa |
| `R-TC2 (tablas de origen r_tc2)` | agregado | `correr_e0.py:874` | 2 | 1 | ceninf, snp_spd |
| `regla 1 (continuidad de enumeración; conteos.reasignaciones_continuidad > 0)` | agregado | `e0_lib.py:2847` | 0 | 0 | — |
| `regla 2 (fronteras intra-palabra; conteos.lineas_corridas_por_frontera > 0)` | agregado | `e0_lib.py:3859` | 106 | 52 | adfsp, adrei, afiltr, apnf, autenf, ayccef, cajasc, ccbcra, cedin, ceninf, cescar, cirmo3, consyr, cryl, ctacte, ctavis, depaho, depinv, disres, dmrd, efemin, expaef, fabcra, fgarcp, fimipyme, finsec, garant, gerc, gescre, gracre, graloc, icmecma, incuca, inspag, jafip, lingeef, lingob, manori, manual, nmaeef (y 66 más) |
| `serializacion de tablas (chunks con flags.tablas_e0[].serializada)` | agregado | `correr_e0.py:1384` | 55 | 37 | adfsp, afiltr, apnf, cajasc, cateloc, ceninf, cirmo3, cryl, disres, dmrd, efemin, fabcra, finsec, gerc, inspag, lingeef, manori, opecam, prevmi, ratio, rdbcra, ri2_cs, ri_cc, ri_ccpnp, ri_cr, ri_dcpc, ri_dsf, ri_gerc, ri_laft, ri_msrl, ri_niif, ri_pgn, ri_pnp, ri_psp, ri_pspapt, ri_pspii, ri_psprca, ri_rml, ri_secoexpo, ri_sef (y 15 más) |

**Capa C: las reglas de S0 sin rastro propio** (`capa_c_sin_rastro`, `listas_de_tos_del_codigo`): `REGLAS_S0_3` (`correr_e0.py:117`); `REGLAS_S0_4` (`correr_e0.py:132`); `REGLAS_S0_5` (`correr_e0.py:152`); `REGLAS_S0_6` (`correr_e0.py:218`). Su uso por documento no se lee en la salida: pide una ablación por regla, que S2 no corre. Las que el código limita a una lista de TOs: `TOS_SUBDOCUMENTO_S0_4` (`correr_e0.py:133`): nmcief, ri_cc, ri_ccna, ri_icpipsp, ri_sef; `TOS_SUBDOCUMENTO_R1_S0_4` (`correr_e0.py:134`): ri_oc; `TOS_APARTADO_LETRA_S0_4` (`correr_e0.py:135`): ri_oc; `TOS_LETRA_S0_4` (`correr_e0.py:136`): ri_ccna; `TOS_APARTADOS_S0_4` (`correr_e0.py:137`): ri_ai; `TOS_TANDA0_SIN_4AB` (`correr_e0.py:138`): cap, cla, ctacte, docvig, ext, lingob, pagjub, polcre, pro, ric; `TOS_TITULO_BLOQUE_S0_5` (`correr_e0.py:153`): ri_oc; `TOS_INTERSTICIAL_S0_5` (`correr_e0.py:154`): snp_cheq, snp_dd; `TOS_ROTULO_VERTICAL_S0_5` (`correr_e0.py:155`): ri_ccna; `TOS_TANDA0_SIN_S0_5` (`correr_e0.py:156`): cap, cla, ctacte, docvig, ext, lingob, pagjub, polcre, pro, ric; `TOS_TANDA0_SIN_S0_6` (`correr_e0.py:219`): cap, cla, ctacte, docvig, ext, lingob, pagjub, polcre, pro, ric.

### 4.e. Los tres grupos de documentos, y lo que queda fuera del grafo

Archivo: `cifras_conjuntos_clases_S2b.json`, clave `4e` (los grupos, por `particion_152.json`, `clase`).

| grupo | TOs (corregida / legada) | páginas (corregida / legada) | unidades (corregida / legada / dif.) |
|---|---|---|---|
| escritos en puntos de principio a fin | 138 / 138 | 4.183 / 4.183 | 10.242 / 9.266 / +976 |
| con fichas y listados de registro | 2 / 2 | 2.413 / 2.413 | 89 / 46 / +43 |
| no segmentables | 10 / 12 | 134 / 161 | 17 / 12 / +5 |
| ri_spi¹ y ri_con¹ (en la legada, dentro de los no segmentables) | 2 / — | 27 / — | 130 / — / — |

Los no segmentables de la corregida: optico, plandecuentas, ri_chr, ri_fcem, ri_itme, ri_pfmipyme, ri_pscpp, ri_pspii, ri_rem, ri_tii. Los de fichas y listados: manual, ri2_pm. Las cifras legadas son las de `particion_152.json`, `agregados` (138, 4.183 y 9.266; 2, 2.413 y 46; 12, 161 y 12).

**Lo que queda fuera del grafo según las enmiendas a las adendas 1 y 2 del laudo B5.5** (`docs/enmiendas_adendas_1_y_2_laudo_B5.5_2026-10-04.md`, leídas en `e82e22f`; páginas y unidades de esa fuente):

| qué | páginas | unidades | razón | ancla |
|---|--:|--:|---|---|
| manual | 2.037 | 17 por punto | histórico: «Vigente hasta el 31/12/2017» | Parte III, punto 1 |
| ri_ao | 1 | 5 | derogado por la Com. A 8262 | Parte III, punto 2 |
| optico y plandecuentas | 43 y 77 | — | documentos de referencia, sin contenido prescriptivo | Parte II.2, punto 5 |
| bloque B: ri2_pm, fichas y cuerpo entre fichas | 366 | — | release posterior declarada (fichas y planillas, ESQ-RI-3 y ESQ-RI-4) | Parte II.2, punto 4 |
| bloque B: la planilla de los nueve | 17 | 114 | ídem | Parte II.2, punto 4 |

En `e82e22f` entraban con la tanda 3 la prosa del bloque A (77 unidades, 13 páginas), las 25 unidades por punto de ri2_pm (10 páginas) y ri_spi¹ (11 páginas). Las tres cambiaron después (abajo).

**Lo que deja fuera del grafo evaluado lo decidido después de `e82e22f`** (aparte; unidades de la E0 corregida, `cifras_punto3_S2b.json`, `por_to.<to>.unidades`):

| qué | TOs | unidades | razón | ancla |
|---|--:|--:|---|---|
| enmienda 8, decisión 1 | 6 | 541 | error de corte confirmado en S1-quater: ri_oc, ri_icpipsp, ri_pnp, ri_psprca, gerc, ri_spi¹ | `docs/enmienda8_protocolo_entre_tandas_2026-10-15_calendario_hacia_B6.3.md`, decisión 1 |
| enmienda 8, decisión 2 (sin ri_pnp, que está en la 1) | 9 | 648 | BKL-0044 y los rechazos `raiz_en_columna_profunda` que quedan: dmrd, ri2_cs, ri_cc, ri_ccpnp, ri_con¹, ri_niif, nmaeef, ri_saofe, ri2_ae | ídem, decisión 2 |
| los 15 de la enmienda 8 | 15 | 1.189 | suma de las dos filas | — |
| ri2_pm, parte por punto | 1 | 37 | va con el bloque B, en la release posterior | nota del 15/10/2026 al pie de las enmiendas, `:147-152` |
| U-BLOQUE-A, prosa del bloque A | 9 | 77 | va al grafo corregido del cap. 6 | `docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md:161`; 77 de `cobertura_bloque_a/alcance_nueve.json` |

ri_pnp está en las dos decisiones y cuenta una vez. Los nueve de U-BLOQUE-A son ri_con¹, ri_tii, ri_rem, ri_chr, ri_fcem, ri_itme, ri_pfmipyme, ri_pscpp y ri_pspii; sus 77 unidades no son las de la E0 corregida (son de U-COB-A). ri_con¹ está también en la decisión 2.

### 4.f. La lectura de cortes de S1-quater y el censo de renglones

Fuente: el registro del cierre de la adjudicación (`s1quater/adjudicacion/cierre/registro_cierre_adjudicacion_S1quater_mesa.md`, §4 a §7) y sus salidas en `cierre/corrida/salida/` (`s1quater_S2b.json`, con el sha256 de cada fuente). La lectura es de la E0 corregida.

**Lo medido** (puede ir a la tesis):
- **Etapa 1, las 90 fichas sorteadas** (`etapa_1`): 85 de 90 unidades sin error de corte, 5 con error, 0 dudosas; sin ponderar, intervalo de Wilson al 95 % [0,8765; 0,9760].
  - Por estrato: vigente 40 de 40; marcadores 10 de 10; sin_raiz 35 de 40.
  - **La cifra ponderada por estrato** (la del corpus): 0,9855, tamaño efectivo 51,56, Wilson [0,9057; 0,9979]; es una aproximación que trata la muestra ponderada como una simple de ese tamaño.
  - Errores de corte por subclase, con la adicional: falta_texto_propio 4, numero_equivocado 1, termina_fuera 1, trae_texto_de_otro_punto 1 (7 subclases en 5 errores). Limpieza, aparte: 1.
  - Los casos: E1-036 `ri_icpipsp::A1C2::S1` (sin_raiz; falta_texto_propio); E1-046 `ri_pnp::Sbloque177` (sin_raiz; falta_texto_propio + numero_equivocado); E1-073 `ri_icpipsp::A1C3::Sbloque8` (sin_raiz; falta_texto_propio); E1-075 `ri_pnp::Sbloque210` (sin_raiz; termina_fuera + trae_texto_de_otro_punto); E1-089 `ri_icpipsp::A1C3::S2` (sin_raiz; falta_texto_propio).
- **Etapa 2, la regresión** (`etapa_2`; sin cifra, por diseño): 56 de 60 correctas y 4 errores de corte: E2-041 `ri_oc::Sbloque7` (termina_fuera + trae_texto_de_otro_punto); E2-044 `ri_psprca::SB` (termina_fuera + trae_texto_de_otro_punto); E2-045 `ri_psprca::SC` (termina_fuera + trae_texto_de_otro_punto); E2-046 `ri_psprca::Sbloque2` (termina_fuera + trae_texto_de_otro_punto). Limpieza: 0.
  - Errores confirmados en la unidad que sigue (cuentan como errores de corte del documento, decisión de la autora del 15/10/2026; mandato `:965-968`): E2-045 (fila `ri_psprca::SC`, corte termina_fuera); E2-044 (fila `ri_psprca::SB`, corte termina_fuera); E2-011 (fila `gerc::2.3.1.4`, corte empieza_fuera); E2-048 (fila `ri_spi::C.1::cierre`, corte termina_fuera); E2-040 (fila `ri_oc::Sbloque6`, corte termina_fuera); E2-043 (fila `ri_psprca::S10`, corte termina_fuera).
  - Los documentos con un error de corte confirmado: ri_icpipsp, ri_pnp, ri_psprca y ri_oc por la marca de la fila, y gerc y ri_spi¹ por la unidad que sigue (mandato `:965-968`); la herencia no cuenta.

**Procedimiento interno, no para la tesis** (decisión de la autora del 15/10/2026): el piso y su declaración.
- El piso es 0,90 sobre el límite inferior de Wilson de la etapa 1 (`docs/checklist_pre_escalado.md:81`, condición 7): 0,8765, **no llega** (`procedimiento_interno.llega_al_piso`: False). Rige la rama 2 del plan B: la salida de S1-quater se commitea con su cifra, declarada debajo del piso, S2 se despacha igual, la condición 7 queda declarada, no cumplida, y no hay otra vuelta a S0 antes de la tanda 1 (mandato, nota del 15/10/2026, `:950-959`).
- La cifra de control, sin las 26 fichas cuyo texto vio un modelo en la pasada 1: 62 de 64, Wilson [0,8930; 0,9914], tampoco llega y no decide. La pongo en este bloque porque es un control del procedimiento de la lectura a ciegas; es una lectura mía de la decisión.

**El censo de renglones** (`censos_S2b.json`, `renglones`), con `s1bis/scripts/censo_renglones_S1bis.py` sin editar y su regla (`s1bis/regla_censo_renglones_S1bis.md`), sobre la E0 corregida y un caché de renglones regenerado con su `e0_lib` (`s0_1/scripts/lineas_152.py`). Corre igual: los mismos insumos que en S1-bis (la E0 plana, el manifiesto de los 152, el caché, las dos reglas y `salida_tanda0_r2b` para la calibración), rc 0.
- 326 renglones del PDF que no están en ninguna unidad ni en un rol declarado, en 191 páginas de 86 TOs (de 192.378 renglones del PDF): encabezado_o_pie_no_repetido 269, sin_unidad_ni_rol 57 (`censo_por_clase`). Calibración con `pro::1.1.2.7`: True.
- Al lado, S1-bis, sobre la E0 de S0-4b: 327 renglones en 187 páginas de 91 TOs (encabezado_o_pie_no_repetido 260, sin_unidad_ni_rol 67). Referencia; no reemplaza la cifra de la E0 corregida.
- Por TO (`censo_por_to`): actgar 1, adrei 4, apnf 1, asomut 1, cajasc 2, cateloc 2, ceninf 6, cescar 1, cirmo3 3, coltit 1, cryl 7, ctacor 2, ctacte 3, ctavis 2, disres 1, dmrd 15, efemin 3, expaef 1, fabcra 2, finsec 3, garant 1, gescre 1, gracre 1, horari 2, icmecma 2, incuca 1, inspag 1, lingeef 5, manori 8, manual 46, micemp 5, nmaeef 3, opecam 2, polcre 2, prevmi 1, pscpp 1, ratio 2, rdbcra 2, relact 1, reqcac 3, retype 1, ri2_cs 1, ri2_pm 7, ri_ai 9, ri_ao 5, ri_cc 1, ri_ccna 16, ri_chr 4, ri_dcpc 2, ri_dsf 4, ri_esd 2, ri_fcem 5, ri_gerc 3, ri_icpipsp 7, ri_ieccm 5, ri_iepsp 8, ri_iesinap 4, ri_ii_31_12_19 2, ri_itme 5, ri_msrl 4, ri_nge 2, ri_niif 3, ri_pfmipyme 5, ri_pgn 5, ri_pscpp 5, ri_psp 4, ri_pspii 5, ri_rcl 3, ri_rml 4, ri_tar 1, ri_tsa 1, ribspc 5, rmgcti 1, rmrtsd 6, seggar 1, seguef 1, servco 1, snp_cheq 9, snp_dd 6, snp_debin 1, snp_psp 2, snp_spd 1, supcon 1, tasint 2, venliq 1, verac 4.
- Lo que no tiene explicación (clase `sin_unidad_ni_rol`, 57) se lee según la regla del censo (mandato, S1, punto 8); S2 no lo lee: el despacho pide la cifra.

### 4.g. La tabla de las marcas

Archivo: `marcas_4g_S2b.json`. Las filas 1 a 8 son las mínimas del mandato (`:348-361`); M1 a M3, las marcas de la tesis vigente que da el despacho de S2, con su texto tal cual. No entran las de U-BLOQUE-A.

| fila | a qué se refiere | cifra o dato | archivo | clave | ¿se resuelve con S2? |
|---|---|---|---|---|---|
| 1 | Los párrafos sin numerar que empiezan con un número de punto (36 en la verificación del 03/10/2026; S0, punto 7) | Con el código vigente quedan 0 intersticiales así. Los 36: subpunto (contenedor) 12, subpunto (terminal) 24 (rdbcra \| subpunto (contenedor) 1, rdbcra \| subpunto (terminal) 5, ri_dcpc \| subpunto (terminal) 2, ri_mmsef \| subpunto (contenedor) 11, ri_mmsef \| subpunto (terminal) 16, snp_cheq \| subpunto (terminal) 1). Como límite, los rótulos que la regla no alcanza (rechazados por «padre no abierto» con el padre presente): 8, cirmo3 2, depaho 1, ri_cc 1, ri_mmsef 1, snp_tr_nc 3. | `p7_en_la_corregida_S2b.json` | `censo_p7_corregida.total; los_36.por_destino; censo_p7_resto_corregida` | sí |
| 2 | ri_spi: si quedó segmentado, con qué regla y en cuántas unidades (S0, punto 4) | Sí: 96 unidades (seccion_sin_puntos 4, punto_terminal 87, mini_chunk 5), modo `sin_raiz_letra`, con la regla 4 de S0, el marcador de letra y número (`correr_e0.py:1561-1571`; aviso `marcador_letra_r2`). Queda fuera del grafo evaluado por la decisión 1 de la enmienda 8; en la partición legada era no segmentable, con 1 unidad. | `cifras_punto3_S2b.json; reglas_por_to_S2b.json` | `por_to.ri_spi; capa_b_rastro_en_la_salida (marcador_letra_r2)` | sí |
| 3 | Los documentos no segmentables, uno por uno, con sus páginas | optico 43 pp. y 1 u; plandecuentas 77 pp. y 1 u; ri_chr 1 pp. y 2 u; ri_fcem 1 pp. y 1 u; ri_itme 1 pp. y 3 u; ri_pfmipyme 1 pp. y 2 u; ri_pscpp 1 pp. y 1 u; ri_pspii 1 pp. y 3 u; ri_rem 2 pp. y 2 u; ri_tii 6 pp. y 1 u. Aparte, por su razón vigente (enmienda 8): ri_con¹ 16 pp. y 34 u; ri_spi¹ 11 pp. y 96 u. | `cifras_punto3_S2b.json` | `no_segmentables_y_parciales` | sí |
| 4 | Las cifras y la tabla de los grupos de documentos, con la fila de lo que queda fuera del grafo (4.e) | Escritos en puntos: 138 documentos, 4.183 páginas, 10.242 unidades; con fichas y listados: 2, 2.413 y 89; no segmentables: 10, 134 y 17; ri_spi¹ y ri_con¹: 2, 27 y 130. La fila de lo que queda fuera, en §5, 4.e. | `cifras_conjuntos_clases_S2b.json` | `4e` | sí |
| 5 | La tabla de los conjuntos de la sección 3.6 (4.a) | Desarrollo 5 documentos, 1.768 unidades; validación 10 y 770; universo 152 y 10.478; por tipo, en §5, 4.a. | `cifras_conjuntos_clases_S2b.json` | `4a.corregida` | sí |
| 6 | La tabla de reglas del apéndice: las reglas vigentes, con los documentos que usa cada una (4.d) | Las 21 reglas de la tabla legada, con el mismo criterio, sobre los 152; las 67 de e0-r2 con rastro en la salida; las de S0 sin rastro, declaradas. En §5, 4.d. | `reglas_por_to_S2b.json` | `capa_a_D3; capa_b_rastro_en_la_salida; capa_c_sin_rastro` | sí |
| 7 | Las unidades partidas por tamaño: cuántas, en cuántas partes, y las que quedan sin partir, con su causa | 6 unidades en 27 partes; 3 sin partir (tabla_serializada 3). La lista, en §4. | `cifras_punto3_S2b.json` | `partidas_por_tamano` | sí |
| 8 | La regla de tablas: en cuántos TOs corre, en cuántos encuentra tablas y cuántas unidades llevan una tabla serializada | Corre en 152; encuentra tablas en 124 (916 tablas, 467 serializadas); 324 unidades llevan una tabla serializada, en 55 TOs. | `cifras_punto3_S2b.json` | `tablas` | sí |
| M1 | Cap. 4, al final del párrafo de los no segmentables, sobre el último, el que «tiene normas con una numeración propia»: `% [AL CIERRE: U-SEG-OFICIAL] decir si la reconoce y con qué regla.` | El texto vigente del párrafo está en Overleaf, no en el repo (CLAUDE.md §2): no identifico cuál es ese documento. Para cada uno de los 12 no segmentables de la partición legada, si la E0 corregida lo reconoce (lo lee por puntos) y con qué reglas: optico: 1 u. (seccion_sin_puntos 1), reglas con rastro: caratula_j; plandecuentas: 1 u. (seccion_sin_puntos 1), reglas con rastro: K (encabezados_conservados.json); ri_chr: 2 u. (seccion_sin_puntos 2), reglas con rastro: K (encabezados_conservados.json); ri_fcem: 1 u. (seccion_sin_puntos 1), reglas con rastro: K (encabezados_conservados.json), regla 2 (fronteras intra-palabra; conteos.lineas_corridas_por_frontera > 0); ri_itme: 3 u. (seccion_sin_puntos 3), reglas con rastro: K (encabezados_conservados.json), division_a; ri_pfmipyme: 2 u. (seccion_sin_puntos 2), reglas con rastro: K (encabezados_conservados.json), division_a; ri_pscpp: 1 u. (seccion_sin_puntos 1), reglas con rastro: K (encabezados_conservados.json); ri_pspii: 3 u. (seccion_sin_puntos 3), reglas con rastro: K (encabezados_conservados.json), serializacion de tablas (chunks con flags.tablas_e0[].serializada); ri_rem: 2 u. (seccion_sin_puntos 2), reglas con rastro: K (encabezados_conservados.json), division_a, raiz_<n>_no_sucede_a_<n>, regla 2 (fronteras intra-palabra; conteos.lineas_corridas_por_frontera > 0); ri_tii: 1 u. (seccion_sin_puntos 1), reglas con rastro: K (encabezados_conservados.json), regla 2 (fronteras intra-palabra; conteos.lineas_corridas_por_frontera > 0), serializacion de tablas (chunks con flags.tablas_e0[].serializada); ri_con¹: 34 u. (seccion_sin_puntos 34), reglas con rastro: K (encabezados_conservados.json), division_a, grupo_sin_columna_comun_c; ri_spi¹: 96 u. (seccion_sin_puntos 4, punto_terminal 87, mini_chunk 5), reglas con rastro: K (encabezados_conservados.json), adoptado_a, cierre_al_margen_r5a, division_a, marcador_letra_r2, no_sucede_al_hermano_<n>, prefijo, regla 2 (fronteras intra-palabra; conteos.lineas_corridas_por_frontera > 0), serializacion de tablas (chunks con flags.tablas_e0[].serializada), subdocumento_sd, subdocumentos. Solo ri_spi¹ queda leído por puntos (87 puntos terminales), con la regla 4 de S0; ri_con¹ queda en 34 bloques sin puntos por la regla A de S0-6a; los otros 10 siguen sin puntos. | `cifras_punto3_S2b.json; reglas_por_to_S2b.json` | `por_to.<to>.por_tipo; capa_b_rastro_en_la_salida` | en parte: falta saber de qué documento habla el párrafo |
| M2 | Cap. 3, tabla de las formas del contenido: `% [AL CIERRE: U-SEG-OFICIAL] Comprobar que los roles de página no cambiaron. Si cambiaron, recontar con el script de VERIF-FORMAS-SEG y actualizar juntas esta tabla y la Tabla de las partes de un Texto Ordenado.` | Cambiaron: 12 páginas en 9 TOs, de los roles que usa la tabla (VERIF-FORMAS-SEG) a los de la E0 corregida: adfsp 1 (cuerpo -> indice 1; pp. 3), ceninf 1 (cuerpo -> indice 1; pp. 2), cirmo3 2 (cuerpo -> indice 2; pp. 3, 4), fimipyme 1 (indice -> cuerpo 1; pp. 4), nmaeef 2 (cuerpo -> indice 2; pp. 2, 14), ri2_ae 2 (cuerpo -> indice 2; pp. 3, 13), ri_niif 1 (cuerpo -> indice 1; pp. 1), snp_mep 1 (indice -> cuerpo 1; pp. 3), venliq 1 (indice -> cuerpo 1; pp. 3). Páginas por rol sobre los 157, corregida / legada (`conteos.json`): cuerpo 3.997 / 4.003, ficha_registro 2.281 / 2.281, historial 474 / 474, indice 164 / 158, portada 206 / 206, tabla_norma_origen 199 / 199. El recuento no lo hago: el script de VERIF-FORMAS-SEG reconstruye los roles con el e0_lib legado (`78a757c`) y no tiene opción para leer los de e0-r2 (`recuento_formas_texto_completo.py:200-212, 303-312`); correrlo así recontaría con los roles viejos, y adaptarlo es otra unidad. | `roles_pagina_S2b.json` | `por_to; paginas_de_otro_rol` | no: los roles cambiaron y el recuento pide adaptar el script |
| M3 | Apéndice, tabla de las reglas: `% [AL CIERRE: U-SEG-OFICIAL] Rehacer la tabla con la segmentación oficial e0-r2: en ella la lectura de tablas corre en los 152 documentos, así que el grupo de las tablas deja de ser propio de los 84. Pedido a la otra mesa: el uso de cada regla por documento en el documento de cifras de S2.` | El uso de cada regla por documento está en §5, 4.d: la capa A rehace la tabla legada sobre los 152 (las reglas de tablas corren en los 152 y actúan en hasta 124 TOs); la capa B agrega las reglas de e0-r2 con rastro en la salida. | `reglas_por_to_S2b.json` | `capa_a_D3; capa_b_rastro_en_la_salida` | sí |

## 6. Las detecciones de la release de E0 en la tanda 1 (agregado 3 del «seguí»)

Con el código de la E0 corregida, sobre su salida (`censos_S2b.json`). Son detecciones, no lecturas, con falsos positivos conocidos (mandato, `:670`). Al lado, las cifras de antes de la corrección de E0 que da el mandato para la tanda 1 (`:665-672`, con la lista de trabajo, que tenía a ri_oc y no a ri_mmsef).

| TO | límites de sub-documento (antes) | formas | ¿en la lista de la regla? | en página donde A ya abre | candidatos 1.16, censo (antes) | candidatos 1.16, detector corregido |
|---|---|---|---|--:|---|--:|
| ayccef | 0 (0) | — | — | 0 | 5 (5) | 8 |
| expaef | 0 (0) | — | — | 0 | 0 (0) | 0 |
| opefci | 0 (0) | — | — | 0 | 0 (0) | 1 |
| adrei | 0 (0) | — | — | 0 | 2 (2) | 2 |
| ri_ccna | 16 (en la lista: la regla los aplica) | anexo 8, formulario 6, parte 2 | sí | 0 | 0 (0) | 4 |
| ri_rml | 3 (3) | regimen 1, parte 2 | no | 0 | 0 (1) | 1 |
| ri_gerc | 1 (1) | regimen 1 | no | 0 | 0 (0) | 1 |
| ri_pgn | 1 (1) | regimen 1 | no | 0 | 0 (0) | 0 |
| snp_cheq | 0 (0) | — | — | 0 | 0 (0) | 6 |
| ceninf | 0 (0) | — | — | 0 | 0 (0) | 0 |
| cirmo3 | 0 (0) | — | — | 0 | 1 (1) | 18 |
| snp_tr | 1 (1) | regimen 1 | no | 0 | 1 (1) | 3 |
| lingeef | 0 (0) | — | — | 0 | 7 (8) | 16 |
| depaho | 0 (0) | — | — | 0 | 7 (8) | 13 |
| cajasc | 0 (0) | — | — | 0 | 3 (4) | 5 |
| manori | 8 (8) | parte 8 | no | 0 | 0 (2) | 4 |
| efemin | 0 (0) | — | — | 0 | 1 (1) | 5 |
| nmcief | 10 (en la lista: la regla los aplica) | anexo 6, parte 4 | sí | 0 | 0 (0) | 3 |
| ri_dcpc | 0 (0) | — | — | 0 | 0 (0) | 2 |
| ri_mmsef (sucesor) | 0 (0) | — | — | 0 | 0 (0) | 0 |
| ri_oc (salió) | — (3) | | | | — (0) | |

- **Límites de sub-documento** (`subdocumentos`, de `s0_4/scripts/censo_sd_152.py`): en la tanda 1, 40 en 7 TOs; fuera de la lista de la regla, que son los que quedan como detección, 14 en 5 TOs. Antes: 17 en 6 TOs, todos fuera de la lista. En los 152: 128 límites en 40 TOs; fuera de la lista, 87 en 35 (anexo 18, parte 42, regimen 26, formulario 1), 17 de ellos en una página donde la regla A de S0-6a ya abre una división. cruce_g3 del censo se calcula contra s0_3/censos/g3_raices_sucesoras_rechazadas.json, de S0-3, anterior a la regla E de S0-6a: no lo uso.
- **Candidatos del hallazgo 1.16** con el criterio del censo de renglones (`hallazgo_1_16`, el original): en la tanda 1, 27 en 8 TOs; antes, 33 en 10. En los 152: 99 en 47 TOs. Con el detector corregido de S0-5a (`detector_116`, el que usó S1-ter): 92 en 16 TOs de la tanda 1; en los 152, original 99, corregido 282, union 283.
- **ri_mmsef, el sucesor:** 0 límites de sub-documento y 0 candidatos del 1.16 por el censo (0 por el detector corregido). Las listas, con ids y páginas, en `hallazgo_1_16.tanda1_lista`, `detector_116.tanda1_lista` y `subdocumentos.tanda1`.

## 7. Tramo 3: el re-censo de la release de E0 antes de la tanda final

Archivo: `tanda_final_S2c.json` (y `resumen_healthcheck_tanda_final_S2c.json`). Sobre la E0 corregida. La release de E0 antes de la tanda final sigue igual, sin re-extraer (mandato, `:665-677`; enmienda 8, §1). Los censos de sub-documentos y de renglones son los del tramo 2 (`censos_S2b.json`), con el código de la E0 corregida; acá se cuentan sobre la tanda final. Son detecciones, no lecturas, con falsos positivos conocidos (mandato, `:670`).

**La tanda final** (`tanda_final`, `cascada_disjunta_sobre_los_152`): los candidatos del §5 del protocolo que quedan después de la tanda 1 del tramo 1, sin los de fuera, sin ri2_pm, sin los 15 de las decisiones 1 y 2 de la enmienda 8 y sin rdbcra (enmienda 8, §1; agregados 1 y 6). Cada TO cuenta en el primer motivo que lo saca:

| motivo | TOs | unidades | quedan |
|---|--:|--:|--:|
| los 152 | — | 10.478 | 152 |
| tanda 0 | 5 | 671 | 147 |
| tanda 1 (tramo 1) | 20 | 3.290 | 127 |
| de fuera del §5 sin razón vigente propia (10 no segmentables, manual y ri2_pm) | 12 | 106 | 115 |
| ri_ao, derogado (nota del 04/10/2026 al protocolo, :432-438) | 1 | 13 | 114 |
| los 15 de la enmienda 8, decisiones 1 y 2 (ri_spi y ri_con por su razón vigente) | 15 | 1.189 | 99 |
| rdbcra, cobertura no exacta (agregado 1) | 1 | 258 | 98 |
| **tanda final** | **98** | **4.951** | |

- **98 TOs y 4.951 unidades** (`unidades_por_to` del manifiesto de S0-6b). La mesa contaba 98 y 4.951 (nota del 15/10/2026 a la enmienda 8, `docs/enmienda8_protocolo_entre_tandas_2026-10-15_calendario_hacia_B6.3.md:178`): igual.
- Por clase: normativa general 74 TOs y 4.507 unidades; régimen informativo 24 y 444. Por modo de lectura: `marcadores` 4, `sin_raiz` 26, `vigente` 68.
- ri_ao sale por la nota del 04/10/2026 al protocolo (`docs/protocolo_entre_tandas.md:432-438`: «ri_ao, derogado, que sale de la tanda 3»), que el §5 arrastra a los candidatos. ri_spi¹ y ri_con¹ salen en la fila de la enmienda 8. ri_oc sale ahí también: dejó la tanda 1 por la decisión 1.

**Cobertura exacta e ids de chunk repetidos, en la E0 corregida** (agregado 2; `frena`): cobertura no exacta en —; ids repetidos en —. **Ninguno: no hay freno.** La fila de cada TO, abajo.

**El health-check de la tanda final** (agregado 5; `healthcheck`): corre como en el tramo 2, con `healthcheck_e0.py` de la raíz mínima sobre los 98 PDFs. No reproduce `correr_e0` en **57 de 98** (da otras unidades que `unidades_por_to`; corre la escalera de `e0_lib` sin el driver de e0-r2). La cobertura no exacta según su propio parseo: —; no frena, porque la cobertura y los ids se controlan sobre la E0 corregida (agregado 4 del «seguí» del tramo 3). Las otras señales se registran por TO y no excluyen (mandato, nota del 15/10/2026, `:1036-1043`). Veredictos: cid 15, cid+paginas_sin_seccion 1, paginas_sin_seccion 7, paginas_sin_seccion+unidades_anomalas_por_tamano 1, sano 71, unidades_anomalas_por_tamano 3.

**Los límites de sub-documento** (punto 3 de la release; E0-05; `subdocumento`, del censo de S0-4a, `s0_4/scripts/censo_sd_152.py`, sobre la E0 corregida): **33 límites en 18 TOs** quedan como detección (anexo 5, parte 14, regimen 13, formulario 1); 11 de ellos están en una página donde la regla A de S0-6a ya abre una división. Por TO: adfsp 1, cateloc 6, ri_acsf 3, ri_ai 1, ri_bdp 1, ri_esd 1, ri_iepsp 2, ri_iesinap 2, ri_ii_31_12_19 3, ri_msrl 1, ri_nge 3, ri_ot 1, ri_psp 3, ri_tar 1, ri_transpa 1, ri_tsa 1, ribspc 1, seggar 1. En la lista de la regla de sub-documento, que los aplica: 6 en ri_sef. Antes (`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:665-669`): 19 en 6 TOs de la tanda 2 y 37 en 18 de la tanda 3, con otra E0 y otra tanda 1.

**Los candidatos del hallazgo 1.16** (punto 4; E0-06; `hallazgo_1_16`), con las dos cifras que decidió la autora para el v8 (mandato, nota del 15/10/2026, decisión a): **el censo de renglones, la principal: 51 en 31 TOs**; al lado, el detector corregido de S0-5a: 134 en 60 TOs. Antes, con el censo de S1 (`docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md:670-672`): 68 en 37 TOs de la tanda 2 y 5 en 4 de la tanda 3. Las listas, con ids y páginas, en `hallazgo_1_16.censo.lista` y `hallazgo_1_16.detector.lista`.

**Una regla para el 1.16: no propongo ninguna.** La regla general que ya corre es C de S0-6a (el párrafo sin número asignado por su columna, aviso `parrafo_por_columna_c`; `REGLAS_S0_6`, `correr_e0.py:218`), que reemplazó a R5-a por lista (`REEMPLAZOS_S0_6`, `correr_e0.py:220`); R5-a sigue por lista solo en `LISTAS_R5A_S0_6` (`:225`). Lo que queda son detecciones con falsos positivos conocidos: una regla acotada, como otra lista de cierres, pide leer cada caso para saber que es un error, y medir que no rompe otros; sin esa lectura no puedo decir que sea de bajo riesgo. S2 cuenta detecciones; si se leen los casos, y cuándo, lo decide la autora.

**`nmaeef::2.9` y la «Sección 1.» de ri_niif** (punto 5 de la release): sus dos documentos quedaron fuera de la tanda final y del grafo evaluado por la decisión 2 de la enmienda 8. Solo lo declaro.

**Una fila por TO de la tanda final** (`filas`; hc: health-check; sd: límites de sub-documento como detección; 1.16: censo / detector):

| TO | clase | modo | unidades | cobertura exacta | ids repetidos | hc: veredicto | hc: unidades | sd | 1.16 |
|---|---|---|--:|---|--:|---|--:|--:|---|
| actgar | NG | `vigente` | 60 | sí | 0 | cid | 60 | 0 | 0 / 2 |
| adfsp | NG | `vigente` | 101 | sí | 0 | cid | 101 | 1 | 2 / 2 |
| afiltr | NG | `vigente` | 72 | sí | 0 | cid | 70 | 0 | 0 / 3 |
| apnf | NG | `vigente` | 34 | sí | 0 | sano | 27 | 0 | 1 / 2 |
| asomut | NG | `sin_raiz` | 8 | sí | 0 | sano | 8 | 0 | 0 / 0 |
| autenf | NG | `vigente` | 75 | sí | 0 | sano | 75 | 0 | 0 / 1 |
| cateloc | NG | `vigente` | 11 | sí | 0 | unidades_anomalas_por_tamano | 2 | 6 | 0 / 0 |
| ccbcra | NG | `vigente` | 32 | sí | 0 | sano | 32 | 0 | 0 / 2 |
| cedin | NG | `sin_raiz` | 66 | sí | 0 | sano | 65 | 0 | 3 / 4 |
| cescar | NG | `vigente` | 21 | sí | 0 | sano | 21 | 0 | 0 / 1 |
| coltit | NG | `vigente` | 39 | sí | 0 | cid | 39 | 0 | 0 / 1 |
| consyr | NG | `sin_raiz` | 34 | sí | 0 | cid | 32 | 0 | 0 / 0 |
| convca | NG | `vigente` | 12 | sí | 0 | sano | 13 | 0 | 0 / 1 |
| cryl | NG | `vigente` | 68 | sí | 0 | sano | 64 | 0 | 0 / 3 |
| ctacor | NG | `vigente` | 21 | sí | 0 | cid | 21 | 0 | 0 / 0 |
| ctavis | NG | `vigente` | 271 | sí | 0 | sano | 275 | 0 | 2 / 7 |
| depinv | NG | `vigente` | 203 | sí | 0 | sano | 202 | 0 | 0 / 7 |
| disres | NG | `vigente` | 38 | sí | 0 | cid | 38 | 0 | 0 / 2 |
| evacre | NG | `vigente` | 19 | sí | 0 | cid | 18 | 0 | 0 / 1 |
| fabcra | NG | `vigente` | 42 | sí | 0 | sano | 42 | 0 | 1 / 1 |
| fclef | NG | `vigente` | 28 | sí | 0 | sano | 28 | 0 | 0 / 0 |
| fgarcp | NG | `vigente` | 22 | sí | 0 | sano | 21 | 0 | 0 / 0 |
| fimipyme | NG | `vigente` | 55 | sí | 0 | sano | 51 | 0 | 1 / 1 |
| finsec | NG | `vigente` | 134 | sí | 0 | sano | 131 | 0 | 2 / 5 |
| garant | NG | `vigente` | 106 | sí | 0 | cid | 104 | 0 | 0 / 1 |
| garopt | NG | `vigente` | 55 | sí | 0 | paginas_sin_seccion | 41 | 0 | 0 / 0 |
| gescre | NG | `vigente` | 61 | sí | 0 | sano | 59 | 0 | 0 / 0 |
| gracre | NG | `vigente` | 67 | sí | 0 | sano | 67 | 0 | 4 / 4 |
| graloc | NG | `vigente` | 100 | sí | 0 | sano | 100 | 0 | 1 / 5 |
| horari | NG | `vigente` | 13 | sí | 0 | sano | 13 | 0 | 0 / 0 |
| icmecma | NG | `vigente` | 48 | sí | 0 | sano | 47 | 0 | 0 / 0 |
| incuca | NG | `vigente` | 23 | sí | 0 | cid | 23 | 0 | 1 / 1 |
| inspag | NG | `vigente` | 93 | sí | 0 | paginas_sin_seccion | 71 | 0 | 2 / 2 |
| jafip | NG | `vigente` | 91 | sí | 0 | sano | 91 | 0 | 2 / 3 |
| lavdin | NG | `vigente` | 29 | sí | 0 | cid | 29 | 0 | 0 / 1 |
| micemp | NG | `sin_raiz` | 8 | sí | 0 | cid | 7 | 0 | 0 / 0 |
| opecam | NG | `vigente` | 65 | sí | 0 | paginas_sin_seccion | 56 | 0 | 2 / 2 |
| ordcom | NG | `vigente` | 65 | sí | 0 | sano | 65 | 0 | 1 / 1 |
| osapsa | NG | `vigente` | 13 | sí | 0 | sano | 12 | 0 | 0 / 0 |
| pfmipyme | NG | `vigente` | 52 | sí | 0 | sano | 52 | 0 | 0 / 0 |
| pimf | NG | `vigente` | 165 | sí | 0 | sano | 165 | 0 | 0 / 0 |
| pognme | NG | `vigente` | 17 | sí | 0 | sano | 17 | 0 | 0 / 1 |
| prevmi | NG | `vigente` | 52 | sí | 0 | sano | 52 | 0 | 0 / 3 |
| pscpp | NG | `vigente` | 22 | sí | 0 | sano | 22 | 0 | 0 / 0 |
| raapal | NG | `vigente` | 40 | sí | 0 | sano | 40 | 0 | 2 / 3 |
| ratio | NG | `vigente` | 133 | sí | 0 | sano | 132 | 0 | 0 / 4 |
| ratiofn | NG | `vigente` | 133 | sí | 0 | sano | 133 | 0 | 0 / 2 |
| regpri | NG | `vigente` | 20 | sí | 0 | sano | 19 | 0 | 0 / 0 |
| relact | NG | `vigente` | 38 | sí | 0 | sano | 38 | 0 | 1 / 2 |
| repefe | NG | `vigente` | 87 | sí | 0 | cid | 87 | 0 | 1 / 5 |
| reqcac | NG | `marcadores` | 3 | sí | 0 | paginas_sin_seccion | 3 | 0 | 0 / 0 |
| retype | NG | `vigente` | 41 | sí | 0 | cid | 40 | 0 | 1 / 2 |
| ri2_ci | NG | `vigente` | 45 | sí | 0 | sano | 45 | 0 | 0 / 2 |
| ri_acsf | RI | `sin_raiz` | 6 | sí | 0 | paginas_sin_seccion | 1 | 3 | 0 / 0 |
| ri_ai | RI | `vigente` | 15 | sí | 0 | paginas_sin_seccion | 11 | 1 | 2 / 2 |
| ri_bdp | RI | `sin_raiz` | 3 | sí | 0 | sano | 3 | 1 | 0 / 1 |
| ri_cr | RI | `sin_raiz` | 6 | sí | 0 | sano | 6 | 0 | 0 / 0 |
| ri_dsf | RI | `sin_raiz` | 28 | sí | 0 | sano | 51 | 0 | 1 / 2 |
| ri_esd | RI | `sin_raiz` | 5 | sí | 0 | sano | 3 | 1 | 0 / 0 |
| ri_ieccm | RI | `sin_raiz` | 4 | sí | 0 | sano | 3 | 0 | 0 / 0 |
| ri_iepsp | RI | `sin_raiz` | 13 | sí | 0 | sano | 6 | 2 | 0 / 1 |
| ri_iesinap | RI | `sin_raiz` | 12 | sí | 0 | sano | 6 | 2 | 0 / 1 |
| ri_ii_31_12_19 | RI | `sin_raiz` | 91 | sí | 0 | sano | 86 | 3 | 0 / 1 |
| ri_laft | RI | `sin_raiz` | 26 | sí | 0 | sano | 7 | 0 | 0 / 0 |
| ri_msrl | RI | `marcadores` | 12 | sí | 0 | sano | 11 | 1 | 0 / 0 |
| ri_nge | RI | `sin_raiz` | 30 | sí | 0 | sano | 30 | 3 | 0 / 0 |
| ri_ot | RI | `sin_raiz` | 32 | sí | 0 | sano | 30 | 1 | 1 / 1 |
| ri_psp | RI | `marcadores` | 9 | sí | 0 | sano | 5 | 3 | 0 / 0 |
| ri_pspapt | RI | `sin_raiz` | 16 | sí | 0 | sano | 13 | 0 | 0 / 1 |
| ri_rcl | RI | `sin_raiz` | 4 | sí | 0 | sano | 3 | 0 | 0 / 0 |
| ri_secoexpo | RI | `sin_raiz` | 35 | sí | 0 | sano | 20 | 0 | 0 / 1 |
| ri_sef | RI | `sin_raiz` | 38 | sí | 0 | sano | 27 | 6 (en la lista) | 0 / 0 |
| ri_tar | RI | `sin_raiz` | 18 | sí | 0 | sano | 2 | 1 | 0 / 0 |
| ri_transpa | RI | `sin_raiz` | 11 | sí | 0 | unidades_anomalas_por_tamano | 1 | 1 | 0 / 0 |
| ri_tsa | RI | `vigente` | 17 | sí | 0 | paginas_sin_seccion | 15 | 1 | 0 / 0 |
| ri_tvf | RI | `sin_raiz` | 6 | sí | 0 | sano | 2 | 0 | 0 / 0 |
| ribspc | RI | `sin_raiz` | 7 | sí | 0 | sano | 5 | 1 | 0 / 0 |
| rmgcti | NG | `vigente` | 81 | sí | 0 | sano | 81 | 0 | 0 / 4 |
| rmrtsd | NG | `vigente` | 31 | sí | 0 | sano | 31 | 0 | 0 / 2 |
| rrci | NG | `vigente` | 77 | sí | 0 | sano | 77 | 0 | 3 / 3 |
| secfin | NG | `vigente` | 22 | sí | 0 | sano | 22 | 0 | 0 / 0 |
| seggar | NG | `sin_raiz` | 36 | sí | 0 | sano | 33 | 1 | 0 / 2 |
| seguef | NG | `marcadores` | 101 | sí | 0 | sano | 98 | 0 | 0 / 0 |
| servco | NG | `vigente` | 40 | sí | 0 | sano | 40 | 0 | 0 / 0 |
| snp_atm | NG | `vigente` | 16 | sí | 0 | sano | 16 | 0 | 1 / 1 |
| snp_cec | NG | `vigente` | 122 | sí | 0 | sano | 121 | 0 | 1 / 1 |
| snp_dd | NG | `vigente` | 131 | sí | 0 | paginas_sin_seccion, unidades_anomalas_por_tamano | 53 | 0 | 0 / 2 |
| snp_debin | NG | `vigente` | 71 | sí | 0 | sano | 70 | 0 | 1 / 1 |
| snp_mep | NG | `vigente` | 62 | sí | 0 | unidades_anomalas_por_tamano | 46 | 0 | 1 / 1 |
| snp_psp | NG | `vigente` | 89 | sí | 0 | sano | 88 | 0 | 0 / 1 |
| snp_spd | NG | `vigente` | 130 | sí | 0 | sano | 129 | 0 | 4 / 5 |
| snp_tr_nc | NG | `vigente` | 136 | sí | 0 | sano | 136 | 0 | 3 / 3 |
| socgar | NG | `vigente` | 12 | sí | 0 | sano | 12 | 0 | 0 / 0 |
| supcon | NG | `vigente` | 67 | sí | 0 | sano | 67 | 0 | 1 / 3 |
| tasint | NG | `vigente` | 69 | sí | 0 | cid | 67 | 0 | 1 / 3 |
| traval | NG | `vigente` | 35 | sí | 0 | sano | 28 | 0 | 1 / 1 |
| venliq | NG | `vigente` | 23 | sí | 0 | cid, paginas_sin_seccion | 16 | 0 | 0 / 0 |
| verac | NG | `sin_raiz` | 5 | sí | 0 | sano | 3 | 0 | 0 / 0 |

