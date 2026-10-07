# U-SEG-OFICIAL — S1: manifiesto y corrida de e0-r2 sobre los 152 TOs

Etapa S1 del mandato FIRMADO en `e543cb2` (texto firmado `44cf30ca0d82…`; bloque «S1. MANIFIESTO Y CORRIDA»,
`:133-162` en HEAD), con las notas al pie que la completan: `d59921f` (ri_cc y ri_tsa como páginas de norma sin unidad;
páginas de portada o de índice que no son la primera, a la lista del censo), `2faff14` (lectura de cortes y censo de
renglones, puntos 7 y 8), `0a3ac81` (el hallazgo 1.16 entra al censo), `0b92a06` y `26c6502` (decisiones sobre S0-1 bis
y S0-2). USD 0: ninguna llamada a la API. Código de E0: el de `26c6502`, sin editar. Escribí solo esta carpeta (`s1/`) y
`../FRENO_S1.md`. Ningún commit.

## 0. Método y precondiciones

- Precondiciones a–d del despacho, con su salida, en `precondiciones_S1.txt`: E0 en `26c6502` y sin cambios, texto
  firmado `44cf30ca…`, sello de la muestra en `2faff14`, ninguna corrida de E0 ajena, `.venv/bin/python` presente y
  2.213 `.pyc` fuera de `.venv`.
- Copia de trabajo: el árbol del repo copiado con `rsync -a --no-links`, sin `.git`, `.venv`, `.venv-app`, el volumen
  de Neo4j, `corpus_tanda0/`, las bases de caché ni `__pycache__`; 0 enlaces en la copia. El código de E0 de la copia
  (`e0_lib.py`, `correr_e0.py`, `e0_tablas.py`, `healthcheck_e0.py`, `selftest_e0.py`) y `manifiesto_corpus.py` dan el
  mismo sha256 que en `26c6502`.
- Todo Python con `PYTHONDONTWRITEBYTECODE=1` y el python de `.venv` con `-B`; la copia terminó con 0 `__pycache__`.
- Foto sha256 del repo antes y después con `../s0_1/scripts/snapshot_repo.py` (resultado en el freno).

## 1. S1.1 — Manifiesto (`manifiesto/segmentacion_oficial_e0r2_152.json`)

En el formato de `manifiesto_corpus`; `manifiesto_corpus.cargar` lo carga y lo valida (sha256 de cada PDF, roles contra
el catálogo, límites). Lo arma `scripts/armar_manifiesto_S1.py`. Por TO: id, archivo, PDF, sha256 del PDF de
`escalado_prep/pdfs/` y el de la descarga (`escalado_prep/descarga_log.json`), clase (`particion_152.json`), modo de
lectura (`conteos_b584.json`, `modo_lectura`), vía, vigencia y, donde corresponde, destino y causa.

- 152 TOs; sha256 igual al de la descarga en 152 de 152. Clase: 138 reconocidos plenos, 2 parciales y 12 no
  segmentables. Modo de lectura: 91 vigente, 5 marcadores y 56 sin raíz.
- Vía: **por punto 140** (los 138 plenos, ri_spi y ri2_pm), **por página 9** (ri_chr, ri_con, ri_fcem, ri_itme,
  ri_pfmipyme, ri_pscpp, ri_pspii, ri_rem y ri_tii, con su fuente en U-COB-A, `cobertura_bloque_a/chunks_a2.json`,
  sin regenerarla: 191 unidades, 77 de prosa y 114 de planilla, por TO y por brazo) y **fuera 3** (manual, histórico;
  optico y plandecuentas, referencia pura).
- Lecturas mías de la decisión 2 al firmar (la vía de los 14 la fijan las enmiendas de `e82e22f`), para confirmar:
  - ri2_pm: el texto firmado pone a los parciales en «fuera»; las enmiendas (Parte II.2, puntos 3 y 4) dan vía por
    punto a sus 25 unidades y dejan el resto como release posterior. Lo declaré `por_punto`, con `alcance_via` y
    `via_resto` (fuera, con su causa).
  - ri_spi: no segmentable declarado; e0-r2 lo segmenta por la escalera (regla 4 de S0), que es la definición de la
    vía por punto. Queda con su clase declarada y el hallazgo al lado (`hallazgo_clase`); la decisión es de la autora.
- ri_cc (pp. 2 a 47) y ri_tsa (pp. 3 a 61): `paginas_de_norma_sin_unidad`, con destino la vía por página de la tanda 3
  (U-BLOQUE-A), según la nota de `d59921f`; las dos cotas coinciden con `s0_1/censos/censo_r3b.json`.
- Vigencia: manual y ri_ao no vigentes (enmiendas, Parte III); los demás, vigentes salvo lo que diga el censo (§5).
- `rol_alcance` sale del catálogo del perfil r2b (66 de 152 con rol), porque la carga lo valida; `nombres_remision`
  va vacío y `limites` en cero: es un manifiesto de E0, sin extracción.

## 2. S1.2 — Corrida

```
cd data/experiment/reextraccion_v2/e0_chunking
PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B correr_e0.py --version-e0 e0-r2 \
    --manifiesto <copia>/data/experiment/segmentacion_oficial_e0r2/s1/manifiesto/segmentacion_oficial_e0r2_152.json \
    --salida <dir>
```
La interfaz de `correr_e0.py` es la del mandato (`--version-e0`, `--manifiesto`, `--salida`): no hay diferencia que
reportar. Dos corridas a la vez, en directorios distintos (`scripts/lanzar_doble_corrida.sh`), de 18:32:25 a 18:55:15
y 18:55:19, código de salida 0, stderr vacío (`sellos_S1.txt`). **Doble corrida: 768 y 768 archivos, 0 distintos, 0
en una sola** (`controles_S1.json`, `doble_corrida`). Una tercera corrida, de 19:02:54 a 19:21:19, con el manifiesto
corregido (§9, error propio 1), da los 768 archivos iguales a las otras dos (`diff -rq` vacío).

## 3. S1.3 — Salida versionada

- `e0/`: la salida de la corrida 1 (igual a la 2 y a la 3), 768 archivos (5 por TO —chunks, estructura, índice,
  pies y tablas— y 8 agregados: conteos, cobertura, correcciones, divergencias, sub_chunking,
  encabezados_conservados, ids_desambiguados y version_e0), **47.293.405 bytes (47,3 MB)**.
- `manifiesto/`, los controles y censos de esta etapa, `scripts/`, `sellos_S1.txt` y `manifest_salida.json` (sha256
  de cada archivo de `s1/`, commit `26c6502`, sha256 del código, comando de la corrida y de los controles). La cuenta
  y el tamaño de toda la carpeta están en el freno.
- El alcance del commit (la salida entera o solo el manifiesto con los sha256) lo decide la autora en este freno
  (decisión 3 al firmar).

## 4. S1.4 — Controles (`controles_S1.json`, `scripts/controles_S1.py`)

- **Tanda 0** (ctacte, lingob, polcre, pagjub y docvig contra `e0_chunking/salida_tanda0_r2b/`, igual a `9f6361e`):
  25 de 25 archivos por TO byte a byte; 35 de 35 entradas de los 7 agregados por TO iguales como valor y como texto
  serializado (`ids_desambiguados` no tiene entrada en ninguno de los dos); `version_e0.json` igual; ningún id
  desambiguado de la tanda 0.
- **Health-check por TO**, con las cuatro señales de `healthcheck_e0.py` calculadas sobre la salida de e0-r2 (la
  herramienta corre la versión legada de E0, así que no la usé sobre esta salida; la definición está en el script):
  106 sanos y 46 con señales: cid en 26, páginas sin sección en 14 y unidades de más de 26.182 caracteres propios en
  8 TOs (9 unidades: `cateloc::S2`, `ri2_cs::S3`, `ri_cc::S3`, `ri_niif::S4` y `S7`, `ri_pnp::S6`, `ri_rml::S4`,
  `ri_secoexpo::S19` y `ri_transpa::S14`, las 9 declaradas sin partir por tabla serializada en `sub_chunking.json`).
  Frente al veredicto de B5.8.4 (`conteos_b584.json`): igual en 138 TOs; en 13 desaparece una señal (cirmo3, dmrd,
  garopt, inspag, manori, nmaeef, opecam, ri2_ae, ri_ccna, ri_spi, snp_dd, snp_mep y venliq, los 13 entre los 26 TOs
  que cambian con S0-2) y en 1 aparece (ri_secoexpo, por `ri_secoexpo::S19`, declarada).
- Ningún TO de la vía por punto en 0 chunks; ningún id repetido; cobertura exacta en 152 de 152.
- **9.554 unidades**: 7.773 puntos terminales, 347 secciones sin puntos y 1.434 mini-chunks (818 intro, 204 cierre,
  287 intersticiales y 125 chapeaux). Partición por tamaño: 10 unidades partidas y 9 declaradas, como en S0-2.
- **Los 26 TOs de `s0_2/censos/cmp_9f6361e_vs_S0-2.json`: 26 de 26 con el conteo igual a su `chunks[1]`.** Ninguna
  diferencia con la corrida de S0-2.
- Modo de lectura de e0-r2 igual al de la partición en 151 TOs; distinto en ri_spi (`sin_raiz` → `sin_raiz_letra`).
- **Hallazgo de clase:** ri_spi, no segmentable declarado, sale con 95 unidades (ya conocido de S0-2). Queda con su
  clase en el manifiesto; la decisión es de la autora. Entre los otros 13 fuera de los plenos, el conteo difiere del
  de la partición en cuatro, sin cambio de clase a mi juicio: manual 19 → 43 (`manual::S2::cierre` partida en 25 por
  la regla 6), plandecuentas 0 → 1, ri_chr 1 → 2 y ri_pspii 2 → 3 (cada uno suma una unidad de preámbulo `S0`, de
  100, 46 y 264 caracteres). Su atribución es de S2, punto 1.
- ri2_pm, con la regla de `no_segmentables_limite/l2_regla_parciales.md`: 345 páginas de ficha; 27 unidades, 25 por
  punto (pp. 1 a 3 y 35 a 41) y 2 que cruzan fichas (`ri2_pm::2.2::intro` y `ri2_pm::S5`), como en la partición.

## 5. S1.5 — Censo de vigencia (`censo_vigencia_S1.json`, `scripts/censo_vigencia_S1.py`)

Marcas «derogad…», «vigente hasta» y «vigente al», sin mayúsculas ni tildes, en la página 1 de cada PDF (renglón de
`extraer_lineas`), en las demás páginas con rol de portada y en el título del índice del sitio
(`escalado_prep/indice_oficial_raw.json`, por el archivo oficial de `inventario_tos.csv`; los 152 tienen entrada).
- Las dos conocidas: `manual`, p. 1, renglón 6, «Vigente hasta el 31/12/2017», y en el índice del sitio
  (`regimenes_informativos`, posición 11) «RI - Manual de Cuentas vigente al 31/12/17.»; `ri_ao`, p. 1, renglón 4,
  «RI Derogado por la Com. A 8262».
- **Una coincidencia nueva, hallazgo:** `ri_tar`, p. 1, renglón 10: «…tipo de cambio de referencia del dólar
  estadounidense difundido por el BCRA, vigente al cierre de las operaciones…». La p. 1 de ri_tar es de cuerpo (el TO
  no tiene carátula) y la frase es texto de la norma, no una marca de vigencia del TO. No cambié el manifiesto; la
  decisión es de la autora.
- Ninguna marca en otras páginas con rol de portada.

## 6. S1.6 — Herencia (`herencia_S1.json`, `scripts/herencia_S1.py`)

- Tope `correr_e0.TOPE_HERENCIA_E0_R2` = (13.091, 2.000), leído del código de la copia.
- Herencia máxima: 9.951 caracteres (`nmcief::3.2.3`, 36 de texto propio); ninguna unidad con herencia sobre 13.091.
  Máximo por TO en el archivo.
- **52 unidades con recorte en 8 TOs, 5 de ellas partes** (las 5 de ri_ccna): manual 5, nmaeef 5, nmcief 7, ri_ccna 5,
  ri_dsf 2, snp_cheq 13, snp_dd 8 y snp_tr 7. De cada una: TO, texto propio, herencia antes y después, bloque recortado
  mayor (el mayor es el cierre de `manual::S2`, 251.166 caracteres omitidos en las unidades de manual) y tramo
  heredado mayor.
- **Contra el FRENO C2 (93 unidades en 9 TOs; `r2_codigo2/freno_c2.md:69`, por TO en `r2_codigo2/salidas/c2_e0.json`):
  −41**, en cinco TOs: inspag 29 → 0, manori 12 → 0, ri_dsf 11 → 2, ri_ccna 4 → 5 y snp_dd 0 → 8. Los cinco son TOs que
  cambian reglas de S0 (`s0_2/censos/atribucion_S0-2.json`: inspag y snp_dd, regla 1; manori, reglas 6, 7 y 8; ri_dsf,
  regla 2; ri_ccna, regla 6). No atribuí la diferencia unidad por unidad. Los otros cinco TOs de C2 (manual, nmaeef,
  nmcief, snp_cheq y snp_tr) dan la misma cifra.

## 7. Punto 7 — Muestra sellada de la lectura de cortes (`muestra_cortes_S1.json`)

Sorteo con `scripts/muestra_cortes_S1.py`, después de la corrida y antes del freno: **18:56:41, sha256
`6ed0889159c433f547074c2265b8c20dc49526aaf8aaf04a298f6f06e2c1b1e7`** (`sellos_S1.txt`). No leí ni marqué ninguna unidad.

- Semilla `U-SEG-OFICIAL:cortes:2026-10-05`; estrato = valor literal de `modo_lectura` de `conteos_b584.json`; `ids` =
  todos los chunks de los TOs del estrato (terminales, secciones sin puntos, partes y mini-chunks: intro, cierre,
  chapeau e intersticial), ordenados con `sorted`; `random.Random(f"{semilla}:{estrato}").sample(ids, n)`.
- Primer grupo, 138 TOs y 9.375 unidades: vigente 91 TOs, 8.166 unidades, peso 0,8710, 40 leídas; marcadores 5 TOs,
  233 unidades, peso 0,0249, 10 leídas; sin raíz 42 TOs, 976 unidades, peso 0,1041, 40 leídas. Total **90**. Dos son
  de la tanda 0 (`polcre::S8` y `lingob::6.2.4.7`).
- Segundo grupo: las **25** unidades por punto de ri2_pm.
- Tercer grupo: **11 juicios**, uno por no segmentable salvo ri_spi, con las unidades de e0-r2 de cada uno.
- ri_spi: **10** de sus 95 unidades, con `random.Random(f"{semilla}:ri_spi")`.
- En el paquete del freno, 299 páginas renderizadas (`pdftoppm -r 110 -png`, una por página, `<to>_p<página>.png`):
  las de cada unidad de la muestra y todas las de los 11 no segmentables.

## 8. Punto 8 — Censo de renglones (`censo_renglones_S1.json`)

- Regla de comparación: `regla_censo_renglones_S1.md`, **versión 2, sellada a las 18:37:49 (`0b939475…`), antes de
  correr el censo**. La versión 1 (18:34:22, `636cf3ff…`) la reemplacé antes de correr: recorría los renglones en una
  sola pasada y un renglón del índice podía consumir la entrada del renglón de cuerpo con el mismo texto (error propio,
  detectado al escribir el script; el reemplazo está declarado en la regla).
- 192.378 renglones del PDF en los 152 TOs (`extraer_lineas`): en una unidad 106.184 (texto propio 95.176, títulos
  heredados 2.288, tablas serializadas 8.719 y 1 en otra página); rol de página 59.740 (ficha 38.879, historial 12.914,
  tabla de origen 7.261, portada 466 y índice 220, de la p. 1); encabezado o pie repetido 19.737; páginas de portada o
  de índice que no son la primera 6.391; y **el censo: 326 renglones** (267 de encabezado o pie que no se repiten y 59
  sin unidad ni rol) **en 186 páginas de 94 TOs**. La suma cierra en 192.378. Total por TO y lista de páginas con sus
  renglones en `por_to`.
- **Páginas de portada o de índice que no son la primera:** 245 páginas de 101 TOs (139 de índice; 106 de portada,
  todas de ri_cc, 46, y ri_tsa, 60), 6.391 renglones, ninguno en una unidad. Las 7 páginas que pasaron a índice en S0-2
  y no son la primera (adfsp 3, ceninf 2, cirmo3 3 y 4, nmaeef 2 y 14, ri2_ae 13) están en la lista. Límite: el
  criterio de texto corrido (55 caracteres o más, sin huecos de columna) marca 191 de las 245 páginas (1.104
  renglones), entre ellas 119 de los 139 índices, porque no separa una entrada larga de índice de un renglón de prosa.
- **Hallazgo 1.16:** 1.497 listas revisadas; **118 candidatos en 55 TOs** (id, página y cierre candidato en
  `hallazgo_1_16.lista`). Calibración: en `pro` la regla encuentra `pro::1.1.2.7` y además `pro::2.2.4.3`. Son
  candidatos, no casos confirmados: la regla no tiene piso y la revisión los lee.
- Anotación POSTERIOR al censo (`explicacion_censo_S1.json`, `scripts/explicar_censo_S1.py`), escrita después de ver
  la lista y sin cambiar su cifra: de los 326, 298 tienen una explicación (197 con forma de encabezado o pie, 78 iguales
  a un renglón de unidad o a un título heredado salvo la puntuación —E0 escribe el título como «N. Título»—, 14 parte de
  un título heredado envuelto y 9 contenidos en una unidad de la misma página) y **28, en 19 TOs, no tienen ninguna**:
  esos los lee la revisión. Entre ellos hay texto de norma tomado como encabezado (fimipyme p. 4, ri2_ci p. 5, ri_cc
  p. 60) y títulos de sección escritos de otra forma («Seccón 3.» de opecam).
- Aparte: 76 renglones del texto de las unidades sin renglón del PDF; son títulos que escribe E0 («Preámbulo»,
  «Sección N. Título» unido de dos renglones).

## 9. Errores propios

1. El primer manifiesto contaba la planilla de U-COB-A con un nombre de brazo que no existe (`planilla`; el de
   `chunks_a2.json` es `planilla_ficha`) y daba 0 en los 9 TOs. Lo vi al recomputar las cifras del reporte, después de
   las dos corridas. Corregí el armador, regeneré el manifiesto (solo cambia ese campo: `diff` en el paquete) y corrí
   E0 una tercera vez con el manifiesto corregido: 768 archivos iguales a la corrida 1 (`sellos_S1.txt`). Los seis
   productos derivados (controles, vigencia, herencia, muestra, censo y anotación) salen byte a byte iguales con el
   manifiesto corregido; la muestra conserva su sha256. El manifiesto de `manifiesto/` es el corregido.
2. La versión 1 de la regla del censo de renglones (§8), reemplazada antes de correr.

## 10. Decisiones de la autora que este freno deja PENDIENTES

1. El alcance del commit de la salida (decisión 3 al firmar), con el tamaño medido.
2. La clase de ri_spi (95 unidades con e0-r2).
3. La coincidencia de `ri_tar` en el censo de vigencia (mi lectura: no es marca de vigencia).
4. La vía de ri2_pm en el manifiesto (por punto con el resto fuera) y la de ri_spi (por punto), como las leí.

## 11. Límites

- El censo de renglones ve el texto que extrae pdfplumber; lo que no extrae lo cubre solo la lectura de cortes, en su
  muestra.
- El criterio de texto corrido de la lista de páginas de portada o de índice no separa las entradas largas del índice.
- La regla del hallazgo 1.16 da candidatos; su cifra no es la de casos.
- La anotación posterior del censo es una ayuda de lectura, no un control: su cifra no reemplaza la del censo.
