# U-SEG-OFICIAL — informe de S0-5a (09/10/2026)

Mandato `docs/mandatos/USEG_OFICIAL_S0-5a_reglas_de_corte_E0.md` en `b60e2fc9` (`4f4ca6c9…`), con la nota del control de
continuidad. USD 0, sin API. Nada commiteado. Diseño: `DISENO_S0-5a.md`. Salidas de E0, en el paquete de revisión (no
entran al repo). Las rutas `salidas/…` y `corridas/…` son del scratchpad de la sesión; `censos/…`, de `s0_5/`.

## 1. Entrada

- `git log`: `b60e2fc9` (HEAD al empezar, 11:15:45) trae el mandato con la nota del control; la nota de U-SEG-OFICIAL
  del 09/10/2026 (mediodía) está en `bbcfb457`, ancestro de HEAD (`censos/precondiciones_S0-5a.txt`).
- Mandato leído en `b60e2fc9`: sha256 `4f4ca6c954252100…`.
- Código de E0 del repo: `e0_lib.py` `65a8c3b8…`, `correr_e0.py` `94d35349…`, `selftest_e0.py` `ec186071…`, los del
  mandato; último commit en `e0_chunking/`: `18d9e056` (S0-4b).
- Foto sha256 del repo a las 11:15:57: 48.242 archivos (`s0_1/scripts/snapshot_repo.py`); 2.213 `.pyc`.

## 2. Controles duros

| control | resultado | respaldo |
|---|---|---|
| todas las reglas apagadas (`S0_5_REGLAS=NINGUNA`) contra S0-4b | 768 de 768 iguales al manifiesto `61ed4bc9…`; 9.625 unidades | `censos/comparar_NINGUNA_vs_S0-4b_S0-5a.txt` |
| los 152 con todas las reglas, dos veces | 768 de 768 iguales entre sí; 9.665 unidades | `censos/comparar_TODAS_vs_TODAS2_S0-5a.txt` |
| los 152 con el código final, sin el interruptor del prototipo | 768 de 768 iguales a la de todas las reglas; manifiesto `92911aa3…` | `censos/comparar_FINAL_vs_TODAS_S0-5a.txt`, `censos/manifiesto_salida_e0_152_S0-5a.json` |
| todas las reglas contra S0-4b | 94 archivos distintos, 674 iguales | `censos/comparar_TODAS_vs_S0-4b_S0-5a.txt` |
| tanda 0, código final, script secuencial, dos veces | 57 de 57 iguales a `salida_tanda0_r2b/` en las dos | §2.1 |
| los 25 archivos de la tanda 0 dentro de los 152 | 25 de 25; agregados: 20 iguales y 15 ausentes en los dos | `censos/control_tanda0_en_152_S0-5a.txt` |
| `selftest_e0` | 169 de 169 | `censos/selftest_e0_S0-5a.txt` (la ruta del scratchpad, cambiada por `<scratchpad>`, como en S0-4) |
| b52, b581, b582, b583 | 39/39, 34/34, 59/59, 33/33 | `censos/selftests_b5x_S0-5a.txt` |
| selftest de claves de la caché (desde la raíz de la copia) | VEREDICTO OK; anclaje r2b OK (2.449 claves de E1); contraste con la tabla OK; salida igual byte a byte a `923dd900…` del repo | `censos/selftest_claves_cache_S0-5a.txt` |
| selftest del control de continuidad | 14 de 14 | `censos/selftest_control_continuidad_S0-5a.txt` |
| selftest de las claves de S0-5a | §5 | `censos/claves_control_S0-5a.json` |

### 2.1 La tanda 0

- `s0_1/scripts/correr_tanda0.py --codigo <raíz con el código final>`, dos veces (13:00 a 13:05): 57 de 57 archivos
  iguales byte a byte a `salida_tanda0_r2b/` de la copia, en las dos (`censos/comparar_t0_final_{1,2}_vs_r2b_S0-5a.txt`).
- Con la exclusión de la tanda 0 apagada (raíz `proto_t0`, solo para medir; no va al repo): solo cambia lo que hace
  R5-a, en 7 TOs (§8).
- Los cinco TOs de la tanda 0 que están en los 152 no aparecen en el censo de ninguna regla sola ni en el de la final
  (§4).

## 3. Aceptación, regla por regla (`scripts/aceptacion_S0-5a.py`; `censos/aceptacion_S0-5a.json`)

- **R5-a**: los 9 casos del mecanismo 1 quedan con el párrafo al margen en el cierre del padre (9 de 9: `adfsp::1.1.10`,
  `cajasc::11.4.4`, `cajasc::4.2.2.3`, `depaho::3.11.5.5`, `manori::1.4.1.3`, `manori::3.4.1.3`, `ri_oc::B.1.28`,
  `ri_oc::B.2.4`, `ri_oc::B.3.4`); en `cajasc::4.2.2.3` pasa el segundo párrafo. Los 27 candidatos marcados correctos en
  S1-bis (`s1bis/lectura_cortes/planilla_1_16_S1-bis-b_mesa.tsv`) tienen el mismo sha256 propio antes y después: 27
  de 27.
- **R5-a′** (ri_oc): de los 77 renglones de `ri_oc::C.11` y de `ri_oc::SC::cierre` de antes, 2 quedan en `ri_oc::C.11`
  (su texto) y 75 van a `ri_oc::Sbloque1` («Criterios de validación», «Validación del Apartado A – Operaciones de
  cambios» y lo que sigue, pp. 19-21; 5.388 caracteres). `ri_oc::SC::cierre` deja de existir; ninguna herencia de
  C.1 a C.11 tiene tramos del bloque: `ri_oc::C.1` pasa de 5.604 a 290 caracteres con la herencia. El límite (d) de
  S0-4a-ter deja de serlo para ri_oc.
- **R5-b**: se unen 13+14, 7+8+9 y los pares de rótulo y descripción; desaparecen las intersticiales 8, 9, 14, 18, 20,
  24, 30, 32, 34, 36, 38, 40, 42, 44, 49, 53 y 55 de snp_dd y 12, 14, 17 y 19 de snp_cheq. Los pares son exactamente
  los del censo de la mesa (17 en snp_dd: 2 por (i), 1 por (i′) y 14 por (ii); 4 en snp_cheq por (ii)); ninguna otra
  intersticial cambia. El mandato dice 19 pares (ii), 15 en snp_dd: el censo de la mesa lista 18 (`DISENO_S0-5a.md`,
  §3.6).
- **R5-c**: los 9 títulos de dos renglones quedan enteros en la herencia y sin chapeau (9 de 9; el de `ri_spi::SC`
  entero); los 4 chapeaux de verdad no cambian (4 de 4).
- **R5-d**: `ri_rml::1.2.3` recupera «…descripto en el punto» / «1.3. “Integración”…» y termina en «…estadounidenses-.»;
  existen `ri_rml::1.2.4` y el 1.3 verdadero, que abre en «1.3. Integración del período». `snp_tr::1.3.3` recupera la
  remisión y los cinco renglones que siguen y termina en «El siguiente gráfico presenta el esquema de compensación
  entre CEC:»; existen 1.3.4 a 1.3.6 con sus hijos, 1.4, 1.4.1 a 1.4.4, 1.5, 1.5.1, 1.5.2, 1.5.2.1 y 1.5.2.2; el 1.6
  abre en «1.6. Transacciones.» y `snp_tr::1.6::intro` ya no existe. Ninguna unidad queda formada solo por los
  renglones de la remisión. Los 4 encabezados de verdad siguen siendo encabezados, con el mismo texto propio y el mismo
  título; `gerc::2.4.2` cambia la herencia porque hereda el cierre nuevo `gerc::2.4::cierre` que abre R5-a (§4).
- **R5-e**: un rótulo vertical en ri_ccna («CODIGO», p. 39, seis letras); `ri_ccna::D1F3::S0` termina en «Fórm. 4368 C
  (II-2006)», y `ri_ccna::D1F4::S0` tiene «CODIGO» y ninguna letra suelta.

## 4. Censo por regla (`scripts/censo_por_regla_S0-5a.py`; `censos/censo_por_regla_S0-5a.{json,md}`)

Cada regla sola contra todas apagadas (la salida de S0-4b, 768 de 768), en los 152; unidades de `chunks_<to>.json`. El
antes y el después de cada unidad está en `censos/antes_y_despues_S0-5a.jsonl` (una línea por clave).

| regla sola | TOs | unidades antes → después | creadas | quitadas | cambiadas |
|---|---|---|---|---|---|
| R5-a | 38 | 3.861 → 3.915 | 57 | 3 | 211 |
| R5-a′ | 1 (ri_oc) | 184 → 184 | 1 | 1 | 11 |
| R5-b | 2 (snp_dd, snp_cheq) | 383 → 362 | 0 | 21 | 20 |
| R5-c | 4 (manual, ri2_ae, ri_ccna, ri_spi) | 327 → 318 | 0 | 9 | 105 |
| R5-d | 2 (ri_rml, snp_tr) | 114 → 130 | 17 | 1 | 11 |
| R5-e | 1 (ri_ccna) | 164 → 164 | 0 | 0 | 2 |
| **todas** | **42** | **4.495 → 4.535** (9.625 → 9.665 en los 152) | **75** | **35** | **343** |

- Las creadas y las quitadas suman lo de la final (57 + 1 + 17 = 75; 3 + 1 + 21 + 9 + 1 = 35). Las cambiadas suman 360
  regla por regla y 343 en la final: 17 unidades cambian con dos reglas (C.1 a C.11 de ri_oc con R5-a y R5-a′; 2.3.1 y
  2.3.2 de manual y C.1.1 a C.1.3 de ri_spi con R5-a y R5-c).
- **Atribución**: de los 453 eventos de la final (creada, quitada o cambiada, por clave), 446 son iguales a los de una
  regla sola (R5-a 252, R5-c 109, R5-b 41, R5-d 29, R5-a′ 13, R5-e 2). Las **7 interacciones** son R5-a con R5-c en
  `manual::2.3` y `ri_spi::C.1`: el cierre que abre R5-a (`manual::2.3::cierre`, `ri_spi::C.1::cierre`) y los ítems
  heredan el título de sección entero que junta R5-c. Ningún evento de una regla sola falta en la final.
- **R5-c y R5-d tocan solo sus casos**: R5-c, los 9 títulos de dos renglones (los 9 chapeaux quitados y las 105
  unidades que heredan el título); R5-d, las dos remisiones (ri_rml y snp_tr). R5-b, solo las 21 intersticiales unidas
  y las 20 unidades a las que se unen; R5-e, las dos unidades de ri_ccna.
- **R5-a**, fuera de los 9 casos, cambia 48 listas más: `censos/lectura_r5a_S0-5a.md` (§4 del FRENO).
- **Archivos que difieren de S0-4b: 94** = 88 por TO (`chunks` en 42 TOs; `estructura` en 40, todos menos snp_dd y
  snp_cheq, donde R5-b actúa al armar los chunks; `tablas` en 6: gerc, gescre, manori y ri_spi por R5-a, ri_ccna por
  R5-c y R5-e, snp_tr por R5-d) más 6 agregados (`cobertura`, `conteos`, `correcciones`, `divergencias_indice_cuerpo`,
  `encabezados_conservados`, `sub_chunking`). Ningún `pies_<to>.json` ni `indice_<to>.json` cambia.
- **Tablas** (`scripts/tablas_S0-5a.py`; `censos/tablas_S0-5a.json`): de 468 tablas serializadas en el texto, quedan 465.
  R5-a mueve renglones de tablas de `e0_tablas` en manori 3.5.2 (las dos tablas del formulario, `tabla014` y
  `tabla015`, dejan de serializarse y van como renglones sueltos, repartidas entre el ítem y `manori::3.5::cierre`),
  ri_spi C.1.3 (`tabla001` deja de serializarse; `tabla000` pasa a `ri_spi::C.1::cierre`), gescre 1.2.8.2 (`tabla001`,
  que estaba entera en el ítem, queda repartida entre el ítem y `gescre::1.2.8::cierre`) y gerc 2.4.3 (`tabla004`, que
  ya cubría siete unidades, suma `gerc::2.4::cierre`). En ri_ccna (3) y snp_tr (1) solo cambian los ids de las
  unidades que cubren las tablas, por R5-c, R5-e y R5-d. **R5-a no excluye los renglones de una tabla**: no lo
  corregí después del censo; va a la decisión (FRENO, §4).

## 5. Claves (`scripts/claves_S0-5a.py`; `censos/claves_S0-5a.json`)

- **Lista declarada**: 453 claves (75 creadas, 35 quitadas, 343 cambiadas), cada una con su regla.
  - Creadas: R5-a, 56 cierres `<padre>::cierre` (o `S<n>::cierre`) y `ri2_ae::14.3`, que vuelve a ser una unidad
    porque sin los párrafos que salen ya no se parte (quitadas `ri2_ae::14.3::parte1` a `::parte3`); R5-a′,
    `ri_oc::Sbloque1`; R5-d, `ri_rml::1.2.4` y 16 de snp_tr (1.3.4.1, 1.3.4.2, 1.3.5.1 a 1.3.5.3, 1.3.6.1, 1.3.6.2, 1.4::intro,
    1.4.1 a 1.4.4, 1.5::intro, 1.5.1, 1.5.2.1 y 1.5.2.2).
  - Quitadas: R5-a′, `ri_oc::SC::cierre`; R5-b, 17 intersticiales de snp_dd y 4 de snp_cheq; R5-c, los 9
    `::chapeau_seccion`; R5-d, `snp_tr::1.6::intro`; R5-a, las tres partes de `ri2_ae::14.3`.
  - Política del mandato: las unidades que ninguna regla toca no cambian de clave; las uniones de R5-b conservan la clave
    de la primera y no renumeran; las nuevas siguen la convención de E0 (`ri_oc::Sbloque1`, propuesta en el diseño).
- **Selftest de claves** (`claves_S0-5a.py controlar`, S0-4b contra S0-5a): **VEREDICTO OK**, las 75, 35 y 343 observadas
  son exactamente las declaradas (`censos/claves_control_S0-5a.json`). **Control negativo**: con la lista sin
  `adfsp::1.1::cierre` y con `actgar::1.2` (que no cambia) agregada, da **FALLA** y nombra las dos
  (`censos/claves_control_negativo_S0-5a.json`).

## 6. Control de continuidad de la numeración (`scripts/control_continuidad_numeracion.py`)

- **Antes de las reglas** (salida de S0-4b): 104 saltos en 15 TOs, 15 (i) y 89 (ii), 0 (iii); 9 (ii) con
  `posible_referencia`; por modo de lectura, 25 en TOs de lectura vigente y 79 en 6 TOs sin raíz (ri_dsf 42, ri2_ae
  11, ri_ccna 11, nmaeef 6, ri_laft 6, ri_ot 3). Tanda 1: 21 saltos en 6 TOs (`censos/control_continuidad_antes_S0-5a.json`).
- **Contra el prototipo de la mesa** (25 saltos en 9 TOs, 12 (i) y 13 (ii)): los 25 están, con la misma clase y la misma
  forma; los 79 de más son de los 6 TOs sin raíz, que el prototipo no recorre
  (`scripts/contraste_prototipo_continuidad_S0-5a.py`; `censos/contraste_prototipo_continuidad_S0-5a.txt`).
- **Aceptación**: antes, `ri_rml::1.2.4` es (ii), cola, en `ri_rml::1.3`; 1.3.4, 1.3.5, 1.3.6, 1.4 y 1.5 de snp_tr son (ii)
  en `snp_tr::1.6::intro`, con sus 19 descendientes, todos ahí. **Después de las reglas, ninguno es un salto.**
- **Después de las reglas**: 98 saltos en 13 TOs, 15 (i) y 83 (ii); se cierran los 6 de la aceptación, no aparece
  ninguno nuevo, y 4 de ri2_ae cambian de unidad porque R5-a los mueve con el párrafo que los tiene (3.5 a
  `ri2_ae::S14::cierre`, 5.2 a `ri2_ae::S3::cierre`; 3.1 y 3.4 pasan de `ri2_ae::14.3::parte3` a `ri2_ae::14.3`).
  Tanda 1: 15 saltos en 4 TOs (`censos/control_continuidad_despues_S0-5a.json`).
- **Lista para la autora** (`censos/lista_continuidad_S0-5a.md`): 84 saltos, 83 (ii) y 1 (i) con un descendiente
  tragado:
  - **tanda 1, regla por lista en S0-5: 12.** ri_ccna 11: en `D1A1`, 2.1.1 a 2.1.8, rótulos pegados al texto que
    empieza con minúscula («2.1.1.no sean socios…»), dentro de `ri_ccna::D1A1::2.1::intro`, y 5.1 y 8.1, pegados al
    título, dentro de los chapeaux de las secciones 5 y 8; en `D1A2`, 5.1, igual. snp_cheq 1: 3.3.6, (i), con 3.3.6.2
    tragado en `snp_cheq::3.3.5.1`;
  - **fuera de la tanda 1, límite declarado y grupo 2: 71** (ri_dsf 42, ri2_ae 11, nmaeef 6, ri_laft 6, ri_cc 3,
    snp_dd 3);
  - **tanda 0: 1**, la remisión 1.3.1.9 de ctacte (`posible_referencia`), fuera de S0-5.
- **El control que ya existía, y por qué no vio estos casos.** Corrí una copia de `s0_1/scripts/censo_p7_resto.py` (el
  censo del punto 7 de S0-1) sobre las dos salidas: 12 sobre S0-4b (cirmo3 2, depaho 1, ri_cc 1, ri_mmsef 1, ri_rml 1,
  snp_tr 3, snp_tr_nc 3), la cifra de la nota; 8 después de las reglas (salen 1.2.4 de ri_rml y 1.3.4 a 1.3.6 de
  snp_tr). Ese censo lista solo los rótulos con título en mayúscula que E0 rechazó por «padre no abierto»: por eso ve
  1.3.4 a 1.3.6 de snp_tr pero no 1.4 ni 1.5, que E0 rechaza por no seguir al último hermano (el 1.6 falso ya estaba
  aceptado). E0 registra el salto de snp_tr en `saltos_numeracion` (`salto_hermano`, padre 1, de 3 a 6, p. 11, en
  `estructura_snp_tr.json` de S0-4b), y ningún script de `segmentacion_oficial_e0r2/` lee ese campo (`git grep
  saltos_numeracion` en HEAD: 0 archivos). El de ri_rml no es un salto para E0, porque el «1.3.» falso sigue a 1.2.3.
  Y el censo del punto 7 corrió en S0-1 y S0-1 bis (`s0_1/DISENO_S0-1.md:271`, `s0_1bis/DISENO_S0-1bis.md:111`), no
  después: no era un control fijo. Los otros siete de los 12 los da el control de la nota como (i) o no son saltos; no
  los releí uno por uno.
- **Control fijo**: el script vive en `s0_5/scripts/`, con `selftest_control_continuidad.py` (los casos de la
  aceptación, el (i) de pimf, la remisión de ctacte, y un caso sintético con hueco, rótulo pegado, (i) y cola con
  `posible_referencia`). Pasa a `e0_chunking/` en S0-5b.

## 7. El detector del 1.16 y los candidatos de R5-a′

- **Detector corregido** (`scripts/detector_116.py`) sobre S0-4b: 121 con el de S1-bis, 316 con la corrección, 317 con
  la unión (el mismo conjunto que la mesa). **Sobre la salida de S0-5a: 97, 276 y 277** (257 de listas de puntos y 20
  de secciones). Salen 44 y entran 4: 42 de las que salen son listas que R5-a cambió (su último ítem ya no tiene el
  párrafo de más); las otras dos, `ri_oc::C.11` (R5-a′) y `ri_rml::1.2.3` (R5-d). Entran `manori::3.5.2` y
  `ri2_ae::14.3` (R5-a les sacó párrafos y les quedó otro corte) y `snp_tr::1.3.4.2` y `snp_tr::1.3.6.2` (listas que
  R5-d hace existir).
- **Candidatos de R5-a′** (`censos/lectura_candidatos_r5a2_S0-5a.md`): 24 sobre S0-4b, 23 fuera de ri_oc, en 20 TOs;
  los 27 de la mesa no se reproducen (`DISENO_S0-5a.md`, §3.7). Mi lectura, sin abrir la página: 7 títulos de bloque
  (ri_oc C.11, el caso por lista; `apnf::1.3.2.5` y `traval::2.5`, «FÓRMULA I»; `gescre::1.2.8.2`, un modelo de
  declaración jurada; `ri_ot::13.4`, «Criterios de consistencia»; `ri_pnp::5.7`, «II – INSTRUCCIONES GENERALES»;
  `ri_spi::C.1.3`, «Anexo I»); 2 bloques sin título (modelos de nota de cryl e inspag); 3 dudosos; 12 falsos positivos
  (tablas, fórmulas, ejemplos, prosa). En la tanda 1, fuera de ri_oc: `ri_rml::1.2.3` dudoso y tres falsos
  positivos. Con la regla como está, solo los de padre sección tendrían adónde ir. Y R5-a, que fuera de ri_oc no cede
  el paso a R5-a′, lleva al cierre del padre el bloque de 12 de los 26 (24 sobre S0-4b y 2 que aparecen sobre S0-5a).

## 8. Límites declarados del §3 (`scripts/limites_S0-5a.py`; `censos/limites_S0-5a.json`)

- `ri_iepsp::S0` y `ri_ieccm::S0`: el tercer renglón del recuadro sigue como texto del preámbulo (grupo 2).
- `ri_icpipsp::A1C3::S2` (3.206 caracteres, pp. 11-12): «Requerimiento normativo Procedimiento aplicado» repetido;
  aparece en 7 unidades de ri_icpipsp (grupo 2).
- `ri_secoexpo::S17`: 5.271 caracteres, pp. 3-8, con el bloque A.2 (grupo 2; si sale en S1-ter, cuenta como error).
- `ri_mmsef::2.2::intro`: una sola unidad de 465 caracteres; no cambia.
- La tanda 0, fuera por lista: sin la exclusión, R5-a crearía 15 cierres en 7 TOs (cap 3, ctacte 4, docvig 1, ext 3,
  polcre 1, pro 2, ric 1) y cambiaría 63 unidades; ninguna otra regla la toca.

## 9. Tabla de reprocesamiento: la fila propuesta

`data/experiment/mantenimiento/tabla_reprocesamiento.md` está fuera de lo que puedo escribir: la fila queda propuesta,
para S0-5b. Las anclas son al código final (el del parche).

| Fila | Cambio | Dónde entra | Qué obliga a recomputar | Clave E1 | Clave E3 | Clase | Principio | Ancla | Variación del selftest |
|---|---|---|---|---|---|---|---|---|---|
| F19c | Release de E0 (e0-r2) antes de una tanda, con las tandas ya extraídas fuera por lista: reglas de corte que crean, quitan o cambian unidades de las tandas siguientes sin cambiar las extraídas | E0 e0-r2 de las tandas siguientes; la de las extraídas, byte a byte igual | en las tandas extraídas, nada; en las siguientes, las unidades nuevas y las que cambian texto o herencia entran a E1 y E3 por F19b y F01 a F03, cuando esa tanda se extraiga | no cambia en las extraídas | no cambia en las extraídas | ninguna en las extraídas | 9 (como F19b) | `correr_e0.py:147-156` (reglas, listas y exclusión de la tanda 0), `:1318-1319`, `:1382-1383`, `:1557-1562`; `e0_lib.py:468` (tolerancia de R5-a), `:2474`, `:2536`, `:2622`, `:1824`, `:3212`, `:3223`, `:3281` | PENDIENTE: el contraste del selftest de claves pide una variación por fila; con la tanda 0 fuera, ninguna clave de la tanda 0 se mueve (OK en S0-5a), y la variación propia la decide S0-5b |

## 10. Comandos

Sobre la copia del repo en el scratchpad (`<copia>`) y el directorio de trabajo de la sesión (`<s05>`); intérprete, el
`.venv` del repo con `-B` y `PYTHONDONTWRITEBYTECODE=1` (los scripts de solo lectura, con `/usr/bin/python3 -B`).

```
# código final y prototipo (raíces mínimas de la copia)
s0_4/scripts/raiz_minima.sh <copia> <s05>/raices/final <s05>/codigo/final
scripts/armar_proto_S0-5a.sh <s05> <repo>
# los 152, por configuración (NINGUNA, TODAS, TODAS@2, r5a, r5a2, r5b, r5c, r5d, r5e)
scripts/lote_configuraciones_S0-5a.sh <s05> <python> NINGUNA TODAS TODAS@2 r5a r5a2 r5b r5c r5d r5e
# los 152 con el código final (sin interruptor) y la tanda 0 dos veces
python -B s0_1/scripts/correr_152.py --codigo <s05>/raices/final --salida <s05>/corridas/c_FINAL --workers 7
python -B s0_1/scripts/correr_tanda0.py --codigo <s05>/raices/final --salida <s05>/corridas/t0_final_<k>
# comparaciones
python -B scripts/comparar_salidas_S0-5a.py <dir> --manifiesto manifiesto_salida_e0_152_S0-4b.json
python -B scripts/comparar_salidas_S0-5a.py <dir> --otra <dir2>
python -B s0_4/scripts/control_tanda0_en_152.py <s05>/corridas/c_TODAS <copia>/…/e0_chunking/salida_tanda0_r2b
# selftests (dentro de la copia)
cd <copia>/data/experiment/reextraccion_v2/e0_chunking && python -B selftest_e0.py   # y b52, b581, b582, b583
cd <copia> && python -B data/experiment/mantenimiento/code/selftest_clave_cache.py \
    --salida-r2b data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b --out <json>
python -B scripts/selftest_control_continuidad.py --antes c_NINGUNA --despues c_TODAS --lineas <caché de renglones>
# censos y controles
python -B scripts/censo_por_regla_S0-5a.py --base c_NINGUNA --final c_TODAS --regla r5a=c_r5a … --regla r5e=c_r5e --out <json>
python -B scripts/claves_S0-5a.py declarar --censo <censo> --out <claves>
python -B scripts/claves_S0-5a.py controlar --antes c_NINGUNA --despues c_TODAS --claves <claves> --out <json>
python -B scripts/antes_y_despues_S0-5a.py --censo <censo> --claves <claves> --antes c_NINGUNA --despues c_TODAS --out-md <md> --out-jsonl <jsonl>
python -B scripts/aceptacion_S0-5a.py --antes c_NINGUNA --despues c_TODAS --planilla-116 s1bis/lectura_cortes/planilla_1_16_S1-bis-b_mesa.tsv --out <json>
python -B scripts/control_continuidad_numeracion.py --e0 <c_NINGUNA | c_TODAS> --lineas <caché de renglones> --out <json>
python -B scripts/lista_continuidad_S0-5a.py --antes <json> --despues <json> --out <md>
python -B scripts/detector_116.py --e0 <c_NINGUNA | c_TODAS> --out <json>
python -B scripts/candidatos_r5a2_S0-5a.py --e0 <c_NINGUNA | c_TODAS> --out <json>
python -B scripts/lectura_r5a_S0-5a.py --antes c_NINGUNA --despues c_TODAS --planilla-116 <planilla> --out-json <json> --out-md <md>
python -B scripts/lectura_candidatos_r5a2_S0-5a.py --antes <json> --despues <json> --lectura-r5a <json> --out-json <json> --out-md <md>
python -B scripts/tablas_S0-5a.py --antes c_NINGUNA --despues c_TODAS --out <json>
python -B scripts/limites_S0-5a.py --e0 c_TODAS --t0-ref <copia>/…/e0_chunking/salida_tanda0_r2b --t0-sin <s05>/corridas/t0_sin_exclusion --out <json>
python -B <copia>/…/s0_1/scripts/censo_p7_resto.py <c_NINGUNA | c_TODAS> <json>
```

La caché de renglones es la de S1-bis: `s0_1/scripts/lineas_152.py <copia> <caché> --workers 4` (`extraer_lineas` de
E0 sobre los 152 PDF; 152 archivos).

## 11. Repo, `.pyc` y convenciones

- **Foto sha256 del repo** (`s0_1/scripts/snapshot_repo.py`, con sus exclusiones): a las 11:15:57, 48.242 archivos; a las
  13:09:09, 48.307. Comparación (`--comparar`): 65 nuevos, 0 borrados, 3 cambiados.
  - De esta sesión: los 64 nuevos de `s0_5/`.
  - Ajenos a esta sesión: `docs/mandatos/UOMISIONES_COD_release_codigo_ensamblado.md` (nuevo, 12:56) y
    `docs/laudo_B2.4_sujetos.md`, `docs/plan_tesis.md` y `docs/tablero.md` (cambiados, 11:22). En el registro de la
    sesión solo hay lecturas de esos archivos.
    Los cuatro entraron en commits que no son de esta sesión: `3be6ebc3` (12:46:39, los tres de `docs/`) y
    `39e2994f` (13:12:15, el mandato); HEAD es ahora `39e2994f`.
- **`.pyc`** (`find . -name "*.pyc"` sin `.git/` ni `.venv/`, como al empezar): 2.213, la misma lista; ninguno nuevo en
  `.venv/` después de la foto inicial.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py` sobre `s0_5/` y sus tres subdirectorios): control
  positivo 16 de 16; 69 coincidencias, todas en texto del corpus copiado en los censos (campos de formularios y
  prosa de las normas); ningún nombre de persona, ninguna referencia al origen de una decisión,
  ninguna ruta absoluta (`censos/grep_convenciones_S0-5a.txt`). El log de `selftest_e0` lleva `<scratchpad>` en lugar
  de la ruta del scratchpad.
