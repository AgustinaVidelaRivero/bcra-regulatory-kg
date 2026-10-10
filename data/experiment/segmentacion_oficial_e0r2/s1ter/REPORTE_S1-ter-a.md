# U-SEG-OFICIAL — S1-ter-a: manifiesto, corrida de los 152 con el código de S0-5b, controles, censos, herencia y poblaciones, sin sortear

Tramo a de S1-ter del mandato FIRMADO en `e543cb2` (S1, `:133-162`), con sus notas al pie hasta `bbcfb45` (las del 09/10/2026,
`:817-924`: semillas, piso, ri_spi, ri_secoexpo y el censo del 1.16) y las notas al pie del mandato de S0-5a, leídas en sus commits
(`32c71ca`, `84695b8`, `be88fdf`, `06110c5`, `3c5f003` y `521e220`). USD 0, sin API. Código de E0: el de `af7ffdd` (S0-5b), sin
editar. Escribí solo esta carpeta (`s1ter/`) y el scratchpad. Ningún commit. No sorteé, no leí y no marqué ninguna unidad.

## 0. Entrada (`precondiciones_S1ter.txt`)

- `af7ffdd` (S0-5b) y `521e220` (plan B) están en el log y son ancestros de HEAD (`c080914`); también `32c71ca`, `84695b8`,
  `be88fdf`, `06110c5` y `3c5f003`.
- Los dos mandatos dan en el árbol el mismo sha256 que en su último commit: el de la unidad, `034be6da…` en `bbcfb45`; el de S0-5a,
  `67529a71…` en `521e220`.
- Semillas (`git log -S`): `U-SEG-OFICIAL:cortes:S1-ter`, `…:cortes:S1-ter:revision`, `…:1_16:S1-ter` y `…:1_16:S1-ter:revision`
  entran en `1548843`; `…:1_16:S1-ter:R5-a`, en `32c71ca`; `…:1_16:S1-ter:ri_oc`, en `06110c5`; las dos de S1-quater, en `521e220`.
- Código de E0 del repo: `e0_lib.py` `bd2190ad…`, `correr_e0.py` `68bd74b5…`, `selftest_e0.py` `789630b5…` (los de S0-5b);
  `e0_tablas.py` `ab300a22…`. El último commit de `e0_chunking/` es `af7ffdd`, sin cambios sin commit.
- Archivos de la mesa, con la ruta del despacho (`~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/d0348a29-…/scratchpad/hoja_de_ruta_tanda1_mesa/`):
  `S0-5_evidencia_detector_116_corregido_salida.json` da `a81ebf65…` y `revision_S0-5a/lista_R5a_por_lista_v2_decision4_mesa.json`
  da `5bec1dce…`, los dos del despacho.
- Ninguna corrida de E0 ajena viva (`pgrep`, código 1). Foto sha256 del repo antes (`s0_1/scripts/snapshot_repo.py`, 48.762
  archivos, 13:56:43) y 2.213 `.pyc` fuera de `.venv`.
- Copia de trabajo en el scratchpad con `rsync -a --no-links`, sin `.git`, `.venv`, `.venv-app`, el volumen de Neo4j,
  `corpus_tanda0/`, las bases de datos ni `__pycache__`: 0 enlaces (se saltearon 336 enlaces simbólicos de
  `ev2_corrida/navegabilidad/trazas_nav/`, ajenos a E0). El código de E0 de la copia da los mismos sha256 que el repo. Todo Python
  con `PYTHONDONTWRITEBYTECODE=1` y `.venv/bin/python -B`.

## 1. Manifiesto (`manifiesto/segmentacion_oficial_e0r2_152.json`, `f59cdea0…`)

- `scripts/armar_manifiesto_S1ter.py`, copia de `s1bis/scripts/armar_manifiesto_S1bis.py` con cuatro cambios declarados en su
  docstring: `rutas.e0_salida` (`s1bis/e0` → `s1ter/e0`), `sellos.commit_codigo_e0` (`18d9e05` → `af7ffdd`), `sellos.unidad` y el
  comienzo de `descripcion`.
- Control (`comparacion_manifiestos_S1ter.json`, `scripts/comparar_manifiestos_S1ter.py`): contra el de S1-bis (`98669cd6…`)
  difieren exactamente esos cuatro campos; las 152 filas de `tos` son iguales campo por campo. `manifiesto_corpus.cargar` lo carga.
  Rol de alcance null en los mismos 10 documentos que en S1-bis.
- La clase de ri_spi sigue siendo la de `particion_152.json` (no segmentable): el despacho pide que el resto salga igual, y su
  reclasificación como reconocido pleno rige en la población de la lectura de cortes (§7).

## 2. Corrida doble (`sellos_S1ter.txt`; `scripts/lanzar_doble_corrida_S1ter.sh`)

```
cd data/experiment/reextraccion_v2/e0_chunking
PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B correr_e0.py --version-e0 e0-r2 \
    --manifiesto <copia>/data/experiment/segmentacion_oficial_e0r2/s1ter/manifiesto/segmentacion_oficial_e0r2_152.json \
    --salida <dir>
```
Dos corridas a la vez sobre la copia, de 13:58:52 a 14:17:20 y 14:17:22, código 0, stderr vacío, stdout iguales. `e0/` es la
corrida 1: 768 archivos, sin rastrear, como `s1/e0/` y `s1bis/e0/`; su tar.gz va en el paquete del freno.

## 3. Controles (`controles_S1ter.json`, `scripts/controles_S1ter.py`)

Copia de `s1bis/scripts/controles_S1bis.py` con un cambio declarado: la comparación contra los 768 de S0-4b pasa a ser contra el
manifiesto de la salida final de S0-5a-bis y contra el de S0-5b.
- **Doble corrida: 768 y 768 archivos, 0 distintos, 0 en una sola.**
- **Contra S0-5a-bis** (`s0_5/bis/censos/manifiesto_salida_e0_152_S0-5a-bis.json`, `176cbdc0…`) **y contra S0-5b**
  (`s0_5/b/manifiestos/manifiesto_salida_e0_152_S0-5b.json`, `28494c3a…`): 768 de 768 iguales por sha256 y bytes en los dos, 0
  distintos, 0 en una sola; **9.665 unidades**, iguales por TO en los 152.
- **Tanda 0 dentro de los 152** (ctacte, lingob, polcre, pagjub, docvig contra `e0_chunking/salida_tanda0_r2b/`): 25 de 25 archivos
  por TO byte a byte; 35 de 35 entradas de agregados iguales como valor y como texto; `version_e0.json` igual; ningún id
  desambiguado de la tanda 0.
- **Tanda 0 completa** (`../s0_1/scripts/correr_tanda0.py --codigo <copia>`, 14:05:07 a 14:08:19, código 0): 57 de 57 archivos
  iguales a `salida_tanda0_r2b/` (`controles/tanda0_57_vs_salida_tanda0_r2b_S1ter.txt`, con `../s0_4/scripts/cmp_dirs.py`) y 57
  de 57 iguales al manifiesto de la tanda 0 de S0-5b (`manifiesto_salida_e0_tanda0_S0-5b.json`).
- **Health-check**: 107 sanos y 45 con señales, el mismo veredicto que en S1-bis en los 152 TOs. cid en 26 TOs; páginas sin sección
  en 13; 9 unidades de más de 26.182 caracteres propios en 8 TOs, las 9 declaradas sin partir por tabla serializada (las de S1-bis).
- Ningún TO de la vía por punto en 0 chunks; ningún id repetido; cobertura exacta en 152 de 152. Modo de lectura igual al de la
  partición en 151 TOs; distinto en ri_spi (`sin_raiz` → `sin_raiz_letra`), como en S1 y S1-bis.
- Unidades por tipo: 7.923 puntos terminales, 520 secciones sin puntos y 1.222 mini-chunks (795 intro, 206 cierre, 125 chapeaux y
  96 intersticiales). Contra S1-bis (9.625): +40, en 33 TOs con otra cantidad de unidades.
- Fuera de los plenos, contra S1-bis: manual 45 → 44, ri2_pm 27 → 28 (nueva `ri2_pm::S1::cierre`; las por punto pasan de 25 a 26) y
  ri_spi 93 → 92; los otros 11, con sus cinco archivos byte a byte iguales a S0-4b (`poblaciones_S1ter.json`, `fuera_de_la_lectura`).

## 4. Censo de vigencia (`censo_vigencia_S1ter.json`, con `../s1/scripts/censo_vigencia_S1.py` sin cambios)

Byte a byte igual a `s1bis/censo_vigencia_S1bis.json`: manual y ri_ao, y la coincidencia de ri_tar, p. 1, r. 10, que sigue
vigente por la decisión de la autora en S1-bis (`s1bis/acta_sorteo_S1bis.md:25-27`).

## 5. Censos de renglones y del 1.16

**Renglones** (`censo_renglones_S1ter.json`, `scripts/censo_renglones_S1ter.py`): la regla v2 de S1
(`../s1/regla_censo_renglones_S1.md`, `0b939475…`) con el cambio de S1-bis (`../s1bis/regla_censo_renglones_S1bis.md`,
`7f42f91f…`); S1-ter no cambia la regla. Caché de renglones regenerado con el `e0_lib` de la copia (152 TOs).
- 192.378 renglones del PDF, como en S1 y S1-bis; la suma de las clases cierra en 192.378.
- **El censo: 333 renglones** (260 de encabezado o pie que no se repiten y 73 sin unidad ni rol) **en 188 páginas de 92 TOs**.
- Contra S1-bis (`comparacion_censos_S1ter.json`, `scripts/comparar_censos_S1ter.py`): los 327 de S1-bis siguen y **entran 6**, todos
  de ri_ccna, p. 39: «C», «O», «D», «I», «G» y «O».
- **Anotación posterior** (`explicacion_censo_S1ter.json`, con `../s1/scripts/explicar_censo_S1.py` sin cambios): **28 sin
  explicación, en 18 TOs**: los 22 de S1-bis y esos 6.
- **Límite medido del censo, caso por caso:** los 6 son las letras del rótulo vertical «CODIGO» del formulario de la p. 39. En S0-4b,
  la «C» cerraba `ri_ccna::D1F3::S0` y las otras cinco quedaban sueltas en `ri_ccna::D1F4::S0`. R5-e las junta como un renglón
  «CODIGO» dentro de `ri_ccna::D1F4::S0`, y la regla del censo compara renglón contra renglón: el renglón «CODIGO» del chunk no es par
  de ninguna de las seis letras del PDF. No es texto perdido.

**1.16 con el criterio original** (la clave `hallazgo_1_16` del censo, solo para compararla con S1-bis): 98 candidatos en 47 TOs (S1-bis:
121 en 56). Salen 23 y no entra ninguno; de los 98, 96 con el mismo cierre y las mismas páginas. Tanda 1: 28 en 8 TOs (S1-bis: 35 en 11).

**1.16 con el detector corregido** (`../s0_5/scripts/detector_116.py`, `fdf0647a…`, sin cambios):
- **Sobre la salida de S0-4b** (`../s1bis/e0`, 768 de 768 iguales a su `manifest_salida.json`): **317** (121 del criterio original y
  316 del corregido). El control (`censos/control_detector_116_S0-4b.json`, `scripts/control_detector_116_S1ter.py`) lee la evidencia
  de la mesa después de controlar su sha256 (`a81ebf65…`): los mismos 121, los mismos 316 y la misma unión, sin ids de un solo lado,
  y los 316 con los mismos campos (padre, origen, párrafos, ítems y páginas).
- **Sobre la salida de S0-5b** (`censos/detector_116_sobre_S0-5b.json`): **285 candidatos en 98 TOs** (98 del criterio original, 284 del
  corregido, 1 solo del original; 265 de listas de puntos y 20 de secciones numeradas).

## 6. Herencia (`herencia_S1ter.json`, `scripts/herencia_S1ter.py`)

Copia de `s1bis/scripts/herencia_S1bis.py` con la cifra de S1-bis como segunda referencia. Tope (13.091, 2.000). Herencia máxima 8.308
(`lingeef::1.3.2.1`, como en S1-bis); ninguna sobre 13.091. **28 unidades con recorte en 4 TOs**, ninguna parte: nmaeef 5, ri_dsf 2,
snp_cheq 13 y snp_dd 8. Contra S1-bis (35 en 5) salen las 7 de snp_tr (`snp_tr::1.6.1` y `1.6.2.1` a `1.6.2.6`), que heredaban la
intro fantasma que R5-d corrigió; no entra ninguna.

## 7. Las poblaciones, sin sortear (`poblaciones_S1ter.json`, `a1313bd6…`; `scripts/poblaciones_S1ter.py`)

Cada población lleva el sha256 de su lista de ids ordenados (`sorted` de Python), para que el sorteo del tramo b se controle contra ella.

**Lectura de cortes** (tres estratos por el `modo_lectura` literal de `conteos_b584.json`; semilla del tramo b
`U-SEG-OFICIAL:cortes:S1-ter:{estrato}` con ese nombre literal):

| estrato | TOs | unidades | peso | n | sha256 de los ids |
|---|---|---|---|---|---|
| `vigente` | 91 | 8.063 | 0,8417 | 40 | `733cd66b…` |
| `marcadores` | 5 | 192 | 0,0200 | 10 | `6637ad1d…` |
| `sin_raiz` | 43 (42 + ri_spi) | 1.324 (1.232 + 92 de ri_spi) | 0,1382 | 40 | `7e1419dc…` |

Total 9.579 = 9.665 − 86 de los 13 TOs que no entran (manual 44, ri2_pm 28 y 14 de los 11 no segmentables salvo ri_spi). Contra S1-bis, sin ri_spi:
+29, +2 y +10. La tanda 0 entera está en `vigente`.

- **ri_spi, la condición** (decisión 5 de la autora del 09/10/2026): S0-5 corrigió el título partido de su apartado C, y también el
  del B, con R5-c (`titulo_seccion_envuelto`). R5-c sola quita `ri_spi::SB::chapeau_seccion` y `ri_spi::SC::chapeau_seccion`
  (`../s0_5/bis/censos/censo_por_regla_S0-5a-bis.md:67`, 93 → 91). En la salida de S1-ter no hay chapeau en SB ni en SC, y las cuatro
  unidades de C (`C.1.1` a `C.1.3` y `C.1::cierre`) heredan el título entero, «C. DENUNCIAS POR INCUMPLIMIENTOS RELACIONADOS CON EL /
  APARTADO B» (S0-4b: «… CON EL» y el chapeau «APARTADO B»); las 53 de B (51 puntos y 2 intros), «B. SEGUIMIENTO DE PAGOS DE
  IMPORTACIONES REALIZADOS CON ANTE- / RIORIDAD AL REGISTRO DE INGRESO ADUANERO DEL BIEN». Quedan 92 unidades (34 de A, 53 de B, 4
  de C y 1 de sección), todas en `sin_raiz`; la que se suma es `ri_spi::C.1::cierre` (R5-a, mixto).
- **Límites declarados en la población** (FRENO de S0-4b y `../s0_5/bis/censos/limites_S0-5a-bis.json`): 56 unidades, 23 en `vigente`
  y 33 en `sin_raiz`; se esperan 1,11 en la muestra (las 13 de corte de S0-4b, 0,39). `ri_secoexpo::S17`, el de la decisión del
  09/10/2026, está en `sin_raiz` (0,030).
- **Candidatos del detector en la población:** 280 (242, 2 y 36); se esperan 2,39 en la muestra.
- **Repetición de S1-bis (declarado):** de las 100 unidades que leyó S1-bis (90 de los estratos y 10 de ri_spi), 99 están en la
  población de S1-ter (40, 10 y 49); falta `ri2_ae::S2::chapeau_seccion`, que R5-c une al título. De las 99, 84 tienen la unidad igual
  a S0-4b y 15 cambiaron. Se esperan 2,20 repetidas en la muestra de 90.

**1.16, población (a):** 285 candidatos − 28 de los 35 de S1-bis que siguen siendo candidatos − 0 de los tres de diseño (ninguno sigue
siendo candidato) = **257 en 97 TOs**, `c52f688b…`; 68 de la tanda 1 y 21 de la tanda 0; n = 30, semilla `U-SEG-OFICIAL:1_16:S1-ter`.
- 9 son también listas de (b): `apnf::1.3.1.2`, `cedin::7.1.3.2`, `depinv::1.9.2`, `efemin::2.3.2`, `evacre::2.1.2`, `finsec::5.1.2`,
  `finsec::5.2.5`, `gracre::6.7.2` y `ri_spi::C.1.3`. Sin ellas, 248 (`a2737e04…`).
- 5 no están en la población de cortes: `manual::2.3.2` y `manual::S4::parte1` (vía fuera), `ri_pspii::S2` (vía por página) y
  `ri2_pm::2.2.3` y `ri2_pm::3.5.5` (parcial, entre sus 26 unidades por punto). Sin las 9 de (b) ni las 3 de vía fuera o por
  página, 245 (`23a8f605…`).

**1.16, población (b): 36** (`c116_b`):
- La lista de la mesa da su sha256 (`5bec1dce…`, controlado en el script): 43 por lista, 9 casos, 32 cierres y 2 mixtos
  (`ri_spi::C.1.3` y `ri2_ae::14.3`). Las 34, como las dejó S0-5b: las 34 tienen el cierre del padre (`<padre>::cierre`), que no
  existía en S0-4b; 33 últimos ítems cambiaron desde S0-4b. Tres son de la tanda 1: `efemin::2.3.2`, `manori::1.1.6.5` y
  `ri_rml::1.4.2`.
- `ri2_ae::14.3` no tiene chunk con ese id: el último ítem está partido por tamaño en tres partes (pp. 28-43). Lo que movió R5-a sale
  de `ri2_ae::14.3::parte1` (5.556 → 5.131 caracteres) al cierre nuevo `ri2_ae::S14::cierre` (424, pp. 28-29); `parte2` (12.483) y
  `parte3` (10.253) conservan su texto y dentro queda el resto del Anexo IV, límite medido.
- `ri_oc::S2` ya no termina en «3. Aclaraciones» (396 → 380 caracteres; pp. 5-6 → 5) y las 51 unidades de `ri_oc::3.1` a
  `ri_oc::3.51` (números 1 a 51, consecutivos) heredan «3. Aclaraciones» (en S0-4b, «3.»); sus ids, `cb6fd691…`; semilla de la
  elección, `U-SEG-OFICIAL:1_16:S1-ter:ri_oc`.
- El id de cada entrada de (b): el del último ítem de la lista (campo `lista` de la lista de la mesa), `ri_oc::S2` y la unidad que
  elija el tramo b. Los 35 fijos (34 listas y `ri_oc::S2`), `1df09dea…`.

**Regresión:** los 35 de S1-bis están en la salida; 27 iguales a S0-4b y 8 cambiadas (los 6 casos de R5-a que estaban entre los 35,
`ri_oc::C.11` y `ri_rml::1.2.3`); 28 siguen siendo candidatos del detector.

**Cruces:** (b) y los 35, 0; (a) y los 35, 0; (a) y la sección 3 de ri_oc, 0; (a) y (b), los 9 de arriba.

**Fuera de la lectura de S1-ter** (el despacho lee solo los tres estratos): los 11 no segmentables salvo ri_spi y los 2 parciales.
Los 11 tienen sus cinco archivos byte a byte iguales a S0-4b; cambian manual y ri2_pm (§3).
