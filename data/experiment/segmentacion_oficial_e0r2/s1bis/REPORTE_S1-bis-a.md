# U-SEG-OFICIAL — S1-bis-a: manifiesto, corrida de los 152 con el código de S0-4, controles, censo y herencia, sin sortear

Tramo a de S1-bis del mandato FIRMADO en `e543cb2` (texto firmado `44cf30ca0d82…`; S1, `:133-162`), con sus notas al pie:
lectura de cortes y censo de renglones (`2faff14`, `:275-341`), resultado de S1 y decisión S0-3 (`:488-504`), S0-4 antes de
S1-bis (`:524-530`) y las semillas de S1-bis (`a757b32`, `:745-748`). USD 0, sin API. Código de E0: el de `18d9e05`, sin
editar. Escribí solo esta carpeta (`s1bis/`) y el scratchpad. Ningún commit. No sorteé, no leí y no marqué ninguna unidad:
la población de la muestra depende de decisiones de la autora sobre este freno (`:494-495`).

## 0. Entrada (`precondiciones_S1bis.txt`)

- `git log`: `18d9e05` (S0-4b) es ancestro de HEAD (`3c35486`); las tres semillas de S1-bis están en el mandato desde
  `a757b32` (`git log -S` con `"U-SEG-OFICIAL:cortes:S1-bis"`, `"U-SEG-OFICIAL:cortes:S1-bis:revision"` y
  `"U-SEG-OFICIAL:1_16:S1-bis:revision"`: las tres dan `a757b32`); el último commit
  de `e0_chunking/` es `18d9e05` y no hay cambios sin commit en esa carpeta ni en esta (solo `s1/e0/`, sin rastrear).
- Código de E0 del repo: `e0_lib.py` `65a8c3b8…`, `correr_e0.py` `94d35349…`, `selftest_e0.py` `ec186071…`, los del parche
  final de S0-4a-ter; `e0_tablas.py` `ab300a22…`, `healthcheck_e0.py` `179da6ad…`.
- Texto firmado del mandato en `e543cb2`: `44cf30ca…3f617c24`. Ninguna corrida de E0 ajena viva (`pgrep`, código 1).
- Foto sha256 del repo antes (`s0_1/scripts/snapshot_repo.py`, 47.361 archivos, 16:15:57) y 2.213 `.pyc` fuera de `.venv`.
- Copia de trabajo en el scratchpad: el árbol del repo con `rsync -a --no-links`, sin `.git`, `.venv`, `.venv-app`, el
  volumen de Neo4j, `corpus_tanda0/`, las bases de datos (`*.db`, `*.sqlite`) ni `__pycache__`; 0 enlaces (se saltearon
  336 enlaces simbólicos de `ev2_corrida/navegabilidad/trazas_nav/`, ajenos a E0). El código de E0 de la copia y
  `manifiesto_corpus.py` dan los mismos sha256 que el repo. Todo Python con `PYTHONDONTWRITEBYTECODE=1` y `.venv/bin/python
  -B`; la copia terminó con 0 `__pycache__`.

## 1. Manifiesto (`manifiesto/segmentacion_oficial_e0r2_152.json`, `98669cd6…`)

- Lo arma `scripts/armar_manifiesto_S1bis.py`, copia de `s1/scripts/armar_manifiesto_S1.py` con cuatro cambios, todos en el
  bloque final de `main` y declarados en su docstring: `rutas.e0_salida` (`…/s1/e0` → `…/s1bis/e0`, S1 `:150`),
  `sellos.commit_codigo_e0` (`26c6502` → `18d9e05`, S1 `:156-157`), `sellos.unidad` (S1 → S1-bis) y el comienzo de
  `descripcion` (S1-bis.1, notas al pie hasta `a757b32`).
- Control (`comparacion_manifiestos_S1bis.json`, `scripts/comparar_manifiestos_S1bis.py`): contra el manifiesto de S1
  (`0957daf5…`) difieren exactamente esos cuatro campos; las 152 filas de `tos` son iguales campo por campo (vía, clase,
  modo de lectura, sha256 de cada PDF, vigencia, rol de alcance). `manifiesto_corpus.cargar` lo carga (152 TOs, salida
  `s1bis/e0`).
- Cifras, iguales a S1: 152 TOs; sha256 igual al de la descarga en 152 de 152; clase 138 / 2 / 12; modo de lectura 91 / 5 /
  56; vía por punto 140, por página 9, fuera 3; manual y ri_ao no vigentes; 66 TOs con rol de alcance.
- **Rol de alcance null, declarado** (U-ALCANCE-E1, nota del 08/10/2026, decisión (c): la corrección del perfil entra en A2,
  después de S2; E0 no lo lee). Precisión: los documentos con alcance decidido en
  `catalogo_unico/registro_alcance_por_tanda.md` y `rol_alcance` null en el manifiesto son **10**, no 9: los 9 de la tabla de
  la tanda 1 (ri_ccna, ri_rml, ri_gerc, ri_pgn, ri_dcpc, snp_cheq, snp_tr, manori, nmcief) y ri_cc, de la tabla «Tanda 3
  (anticipada)». Los 3 sin alcance declarado de la tanda 1 (ri_oc, ceninf, cirmo3) también van null, como corresponde.

## 2. Corrida doble (`sellos_S1bis.txt`; `scripts/lanzar_doble_corrida_S1bis.sh`)

```
cd data/experiment/reextraccion_v2/e0_chunking
PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B correr_e0.py --version-e0 e0-r2 \
    --manifiesto <copia>/data/experiment/segmentacion_oficial_e0r2/s1bis/manifiesto/segmentacion_oficial_e0r2_152.json \
    --salida <dir>
```
Dos corridas a la vez sobre la copia, en directorios distintos, de 16:18:34 a 16:36:38 y 16:36:43, código 0, stderr
vacío. `e0/` es la corrida 1: 768 archivos, 47.207.498 bytes (el mayor, `chunks_lingeef.json`, 1.494.060), sin rastrear,
como `s1/e0/`; su tar.gz va en el paquete del freno.

## 3. Controles (`controles_S1bis.json`, `scripts/controles_S1bis.py`)

`controles_S1bis.py` es copia de `s1/scripts/controles_S1.py` con un cambio declarado: el control de los 26 TOs de S0-2
(`cmp_9f6361e_vs_S0-2.json`, que comparaba contra el código de S0-2) se reemplaza por la comparación contra los 768 de
S0-4b.
- **Doble corrida: 768 y 768 archivos, 0 distintos, 0 en una sola.**
- **Contra el manifiesto de la salida de S0-4b** (`manifiesto_salida_e0_152_S0-4b.json`, `61ed4bc9…`, del paquete
  `revision_USEG_OFICIAL_FRENO_S0-4b`, copia permanente): **768 de 768 iguales por sha256**, 0 distintos, 0 en una sola;
  **9.625 unidades**, iguales por TO en los 152.
- **Tanda 0** (ctacte, lingob, polcre, pagjub, docvig contra `e0_chunking/salida_tanda0_r2b/`): 25 de 25 archivos por TO
  byte a byte; 35 de 35 entradas de agregados iguales como valor y como texto (20 presentes en los dos y 15 ausentes en los
  dos: 5 en `encabezados_conservados`, 5 en `sub_chunking` y 5 en `ids_desambiguados`); `version_e0.json` igual; ningún id
  desambiguado de la tanda 0.
- **Health-check** con las cuatro señales de `healthcheck_e0.py` calculadas sobre la salida de e0-r2 (como en S1): 107 sanos
  y 45 con señales (S1: 106 y 46). cid en 26 TOs; páginas sin sección en 13 (los 8 no segmentables con esa señal, ri_acsf,
  reqcac, ri_rml, ri_tsa y ri_cc); unidades de más de 26.182 caracteres propios en 8 TOs, 9 unidades, las 9 declaradas sin
  partir por tabla serializada (`cateloc::S2`, `ri2_cs::S3`, `ri_cc::RIP::S0`, `ri_niif::S4` y `S7`, `ri_pnp::S6`,
  `ri_rml::S4`, `ri_secoexpo::S19`, `ri_transpa::S14`). El único veredicto que cambia frente a S1 es ri_ai, de páginas sin
  sección a sano (su sección 2 la abre el mecanismo 5 de S0-3).
- Ningún TO de la vía por punto en 0 chunks; ningún id repetido; cobertura exacta en 152 de 152.
- Unidades por tipo: 7.896 puntos terminales, 519 secciones sin puntos y 1.210 mini-chunks (794 intro, 164 cierre, 135
  chapeaux y 117 intersticiales).
- Modo de lectura de e0-r2 igual al de la partición en 151 TOs; distinto en ri_spi (`sin_raiz` → `sin_raiz_letra`), como
  en S1.
- Fuera de los plenos, contra la partición: igual que en S1 salvo manual 19 → 45 (S1: 43) y ri_spi 1 → 93 (S1: 95).
- ri2_pm, con la regla de `no_segmentables_limite/l2_regla_parciales.md`: 345 páginas de ficha; 27 unidades, **25 por
  punto** (pp. 1-3 y 35-41, los mismos 25 ids de S1) y 2 que cruzan fichas (`ri2_pm::2.2::intro`, `ri2_pm::S5`).
- Contra S1 (`comparacion_salida_S1_S1bis.json`, `scripts/comparar_salida_S1_S1bis.py`): 87 TOs con sus cinco archivos
  byte a byte iguales y 65 distintos; 33 con otra cantidad de unidades; 9.554 → 9.625. Fuera de los plenos cambian solo
  manual, ri2_pm y ri_spi.

## 4. Censo de vigencia (`censo_vigencia_S1bis.json`, con `../s1/scripts/censo_vigencia_S1.py` sin cambios)

Igual que en S1: manual (p. 1, r. 6, «Vigente hasta el 31/12/2017», y el índice del sitio «…vigente al 31/12/17.»), ri_ao
(p. 1, r. 4, «RI Derogado por la Com. A 8262») y la coincidencia de **ri_tar, p. 1, r. 10**, «…estadounidense difundido
por el BCRA, vigente al cierre de las operaciones del último día hábil del…». Ninguna marca en otras páginas de portada.

## 5. Censo de renglones (`censo_renglones_S1bis.json`, `scripts/censo_renglones_S1bis.py`)

- Regla: la v2 de S1 sin cambios (`../s1/regla_censo_renglones_S1.md`, `0b939475…`) más el cambio declarado en
  `regla_censo_renglones_S1bis.md`, **sellado a las 16:21:08 (`7f42f91f…`), antes de correr el censo**: en el hallazgo 1.16,
  el id del ítem lleva el prefijo de sub-documento de su raíz (`<to>::<prefijo>::<numero>`; en S1, `<to>::<numero>`,
  `../s1/scripts/censo_renglones_S1.py:69`). Además se cuentan aparte las listas con algún ítem sin chunk de ese id.
- Caché de renglones regenerado con el `e0_lib` de la copia (`../s0_1/scripts/lineas_152.py`, 152 TOs).
- 192.378 renglones del PDF, como en S1: en una unidad 106.190 (texto propio 95.205, títulos heredados 2.258, tablas
  8.720 y 7 en otra página); rol de página 59.740; encabezado o pie repetido 19.712; páginas de portada o de índice que
  no son la primera 6.409; y **el censo: 327 renglones** (260 de encabezado o pie que no se repiten y 67 sin unidad ni rol)
  **en 187 páginas de 91 TOs**. La suma cierra en 192.378.
- Páginas de portada o de índice que no son la primera: 246 de 101 TOs (140 de índice, 106 de portada), 6.409 renglones,
  ninguno en una unidad; las 7 de S0-2, en la lista.
- **Anotación posterior** (`explicacion_censo_S1bis.json`, con `../s1/scripts/explicar_censo_S1.py` sin cambios): **22 sin
  explicación, en 17 TOs**. Contra los 28 de S1 (`comparacion_censos_S1bis.json`, `scripts/comparar_censos_S1bis.py`):
  **quedan 20, salen 8** (fimipyme p. 4, 2 renglones; ri2_ci p. 5, 2; ri_cc p. 60, 2, y p. 62, 1; snp_cheq p. 71, 1) **y
  entran 2**, de ri_oc: los rótulos «APARTADO B: POSICIÓN GENERAL DE CAMBIOS: En dólares estadounidenses.» (p. 16) y
  «APARTADO C: COMPOSICIÓN DE LA POSICIÓN GENERAL DE CAMBIOS:» (p. 18).
- **Hallazgo 1.16: 121 candidatos en 56 TOs** (S1: 118 en 55), sobre 1.516 listas (S1: 1.497; las 19 de más son de los
  sub-documentos). Entran `ri_ai::2.2`, `ri_cc::R4::1.2.2`, `ri_cc::R5::2.2.1.2`, `ri_oc::B.1.28` y `ri_oc::C.11`; salen
  `ri_cc::1.2.2` y `ri_cc::2.2.1.2` (los mismos dos, ahora con prefijo); de los 116 comunes, 115 con el mismo cierre y las
  mismas páginas (`ri_ai::1.2.2` pasa de pp. 2-3 a p. 2). Dos listas con un ítem partido por tamaño
  (`nmaeef::21.3::parte1…8`, `ri2_ae::14.3::parte1…3`) no se evalúan, como en S1, donde no se contaban. Calibración: en
  `pro` encuentra `pro::1.1.2.7` (y `pro::2.2.4.3`).
- **Tanda 1** (los 20 del ejemplo del §7 del protocolo, con ri_pgn en lugar de ri_cc): **35 candidatos en 11 TOs** (adrei
  2, ayccef 5, cajasc 4, cirmo3 1, depaho 8, efemin 1, lingeef 8, manori 2, ri_oc 2, ri_rml 1, snp_tr 1), en 50 páginas, con
  34.284 caracteres propios; los 33 de S1 siguen y entran `ri_oc::B.1.28` y `ri_oc::C.11`.
- En la población de la muestra caen 120 de los 121 (110 vigente, 2 marcadores, 8 sin raíz; fuera, `ri_spi::C.1.3`): se
  esperan 0,915 en las 90 y 0,23 de la tanda 1, como dice el mandato.

## 6. Herencia (`herencia_S1bis.json`, `scripts/herencia_S1bis.py`)

Copia de `s1/scripts/herencia_S1.py` con la cifra de S1 como segunda referencia (y la clave de la diferencia con C2
renombrada de `s1` a `s1bis`). Tope (13.091, 2.000). Herencia máxima 8.308 (`lingeef::1.3.2.1`; S1: 9.951 en
`nmcief::3.2.3`); ninguna sobre 13.091. **35 unidades con recorte en 5 TOs**, ninguna parte: nmaeef 5, ri_dsf 2, snp_cheq
13, snp_dd 8 y snp_tr 7. Contra S1 (52 en 8): salen manual 5, nmcief 7 y ri_ccna 5 (las 5 partes de `ri_ccna::8.2`); no
entra ninguna.

## 7. La población de la muestra, sin sortear (`poblacion_muestra_S1bis.json`, `scripts/poblacion_muestra_S1bis.py`)

Criterio de la nota de `2faff14` con las precisiones de `26c6502`, como en `s1/scripts/muestra_cortes_S1.py`; con cada
estrato, el sha256 de su lista de ids ordenados, para que el sorteo del tramo b se controle contra la población fijada.
- **Primer grupo, 138 TOs, 9.446 unidades**: vigente 91 TOs y **8.034** (peso 0,8505; la tanda 0 entera está acá),
  marcadores 5 y **190** (0,0201), sin raíz 42 y **1.222** (0,1294); 40 / 10 / 40.
- **Segundo grupo**: las **25** unidades por punto de ri2_pm, las mismas de S1.
- **Tercer grupo: 11 juicios**, uno por no segmentable salvo ri_spi.
- **ri_spi: 93 unidades**; si sigue no segmentable, 10 aparte, fuera del piso (136 lecturas en total).
- **Variante ri_spi reconocido pleno**: sus 93 unidades entran a sin raíz (su `modo_lectura` en `conteos_b584.json`):
  8.034 / 190 / **1.315**, pesos 0,8422 / 0,0199 / 0,1379; desaparece el grupo aparte (126 lecturas).
- **Los dudosos de S1 salen iguales**: ri_pspii (3 unidades, p. 1) y ri_tii (`ri_tii::S0`, pp. 1-6, 9.596 caracteres) con
  sus cinco archivos byte a byte iguales a S1; `ri2_pm::3.5.3` con el mismo texto, las mismas páginas (38-39) y la misma
  herencia (1.893 caracteres). Si no se deciden, la lectura de S1-bis se encuentra lo mismo.
- **Límites declarados en la población** (FRENO S0-4b): las 13 de corte que nombra el mandato son `nmaeef::2.9`, las 10 de
  solo rótulo, `ri_ccna::D1A3L1::S0` y `ri_oc::B.2::intro`, las 13 en sin raíz: 13 × 40 / 1.222 = **0,43** esperadas en la
  muestra (identificación mía, porque reproduce la cifra del mandato; la confirma la mesa). Aparte: 4 de tamaño o de herencia
  (`ri_cc::RIP::S0` y `manori::1.5.1` en vigente; `ri_oc::SC::cierre` y `nmcief::A6::S0` en sin raíz; 0,08) y los dos de ri2_ae
  (`3.3` y `5.3`, sin raíz; 0,07).

## 8. Para las decisiones del freno (hechos, sin lectura)

- **ri_spi.** 93 unidades (S1: 95): salen `ri_spi::B.1::intro` y `ri_spi::B.3::intro` (colas de títulos envueltos; S0-4a) y
  15 unidades de B.1 y B.3 cambian solo la herencia. Siguen, con el texto de S1, `ri_spi::SB::chapeau_seccion` (49
  caracteres) y `SC::chapeau_seccion` (10), y los ítems «.0. Sin información.» leídos como intro (`A.3.6::intro`,
  `B.5.8::intro`, 25 cada una), que la revisión de S1 marcó para declarar o corregir. En S1, 9 de sus 10 cortes leídos
  fueron correctos. Un candidato del 1.16 (`ri_spi::C.1.3`); 3 renglones en el censo (uno sin explicación, p. 9, el rótulo
  del Apartado C).
- **ri2_pm.** 14 de sus 27 unidades cambian respecto de S1, por la regla 2b de S0-3 («N- TÍTULO»): 12 solo la herencia (de
  «1.» a «1. INTRODUCCIÓN», etc.); `ri2_pm::S0` pasa de 48 a 32 caracteres sin «1- INTRODUCCIÓN» y `ri2_pm::1.6` de 1.078 a
  1.005 sin el título de la sección 2 (sigue con el párrafo «Las casas de cambio y agencias de cambio con sucursales…»).
  Son dos de las tres unidades no correctas de S1 (filas 91 y 97); la tercera es `3.5.3`, igual. ri2_pm sigue fuera de la
  regla de sub-documento por lista: el Manual de Cuentas (pp. 35-41) reinicia la numeración del Plan.
- **ri_tar.** La coincidencia de la p. 1, r. 10 es la de S1; mi lectura es la de S1 y de su revisión: texto de la norma (el
  tipo de cambio «vigente al cierre de las operaciones del último día hábil del mes»), no marca de vigencia del TO.

## 9. Errores propios y precisiones

- Al correr la herencia vi que la diferencia con C2 heredaba de S1 la clave `s1` para la cifra de esta corrida; la renombré a
  `s1bis` en el script y volví a correr (la cifra no cambia; declarado en el docstring).
- El mandato dice 9 documentos con alcance del registro y rol de alcance null; son 10 (§1).

## 10. Límites

- El censo de renglones ve el texto que extrae pdfplumber; lo demás lo cubre la lectura de cortes, en su muestra.
- La regla del hallazgo 1.16 da candidatos, no casos; y no evalúa una lista cuyo último ítem está partido por tamaño.
- La identificación de las 13 unidades de corte (§7) es mía y reproduce la cifra del mandato.
