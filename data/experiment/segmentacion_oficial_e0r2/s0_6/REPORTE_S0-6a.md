# U-SEG-OFICIAL — informe de S0-6a (12/10/2026)

**Este archivo nombra unidades con error de corte y de herencia: ninguna lectura a ciegas lo abre, tampoco la de
S1-quater.** Texto de unidades: solo de las 40 filas y de las 286 leídas en S1-ter (mandato, §5); de las demás, ids y
cuentas. USD 0, sin API. **Nada commiteado; el parche no se aplicó al repo** (se aplica en S0-6b). Diseño:
`DISENO_S0-6a.md`. Las salidas de E0 y el antes y el después de las unidades que no son de las 40 ni de las 286 están
en el paquete de revisión (archivos `NO_ABRIR_`), no en el repo. Las rutas `censos/…`, `controles/…`, `parche/…` y
`scripts/…` son de `s0_6/`.

## 1. Entrada

- Paso 0: `pwd` = la raíz del repo; HEAD `e4bb93ce` («Segmentacion oficial: las fichas de la tanda 0 de la lectura,
  declaradas»).
- Mandato `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md`, leído en HEAD: `git show HEAD:… | shasum -a 256` =
  `5edfd993…`, igual al del despacho.
- Los cuatro archivos de `para_la_ejecutora_S0-6a/`, con el sha256 del despacho: `096cd54f…`, `767ac8bd…`, `6e880ab1…`
  y `5fe8a7dd…` (TSV de 40 filas). Del paquete de la mesa no abrí nada más, ni las carpetas que el mandato prohíbe.
- Código de partida, el del repo (S0-5b): `e0_lib.py` `bd2190ad…`, `correr_e0.py` `68bd74b5…`, `selftest_e0.py`
  `789630b5…`, `e0_tablas.py` `ab300a22…`.
- Foto sha256 del repo a las 10:20:57: 49.651 archivos (`s0_1/scripts/snapshot_repo.py`); 2.213 `.pyc` fuera de
  `.venv/`.
- Todo corrió sobre copias sin enlaces (`rsync -a` del repo al scratchpad, 0 enlaces): la de trabajo, una segunda para
  los selftests y raíces mínimas (`s0_4/scripts/raiz_minima.sh`). Intérprete: el `.venv` del repo con `-B` y
  `PYTHONDONTWRITEBYTECODE=1`; los scripts de solo lectura, con `/usr/bin/python3 -B`.

## 2. Controles duros

| control | resultado | archivo (`controles/`) |
|---|---|---|
| todas las reglas apagadas (prototipo, `S0_6_REGLAS=NINGUNA`) contra la E0 de S0-5b | 768 de 768 iguales; 9.665 unidades | `comparar_NINGUNA_vs_S0-5b_S0-6a.txt` |
| los 152: prototipo con todas, código final sin interruptor, y otra vez el prototipo | 768 de 768 iguales entre las tres; `por_to/` sin diferencias; **10.584 unidades** | `comparar_FINAL_vs_TODAS_S0-6a.txt`, `comparar_TODAS_2_vs_TODAS_S0-6a.txt`, `comparar_FINAL_vs_TODAS_2_S0-6a.txt` |
| contra S0-5b | 265 de 768 archivos distintos: chunks 110, estructura 109, tablas 39 y 7 agregados; la diferencia, clave por clave, en §6 | `comparar_FINAL_vs_S0-5b_S0-6a.txt` |
| corrida de controles con el código del parche (`scripts/lote_controles_S0-6a.sh`): los 152 dos veces (14:13:54–14:22:54) | 768 de 768 iguales entre sí y con la final; `por_to/` sin diferencias; 10.584 unidades; manifiesto en `../manifiestos/` | `comparar_c152_1_vs_FINAL_S0-6a.txt`, `comparar_c152_2_vs_c152_1_S0-6a.txt`, `diff_por_to_c152_S0-6a.txt`, `lote_controles_S0-6a.log` |
| tanda 0 con el código del parche, `s0_1/scripts/correr_tanda0.py`, dos veces (14:22:54–14:27:23), contra `salida_tanda0_r2b/` | **57 de 57** en las dos; 2.439 unidades | `comparar_t0_1_vs_r2b_S0-6a.txt`, `comparar_t0_2_vs_r2b_S0-6a.txt` |
| los 25 archivos de la tanda 0 dentro de los 152 | 25 de 25; agregados: 20 iguales y 15 ausentes en los dos | `control_tanda0_en_152_S0-6a.txt` |
| censo por regla en la tanda 0 | 0 cambios: ningún TO de la tanda 0 entre los que cambia una regla ni la configuración final | `../censos/censo_por_regla_S0-6a.json` |
| claves de la tanda 0 | ninguna clave de la tanda 0 se mueve (0 de 3.825) | `../censos/claves_S0-6a.json` |
| `selftest_e0` (sobre una segunda copia del repo con el código del parche) | **239/239**, rc 0: los 188 de S0-5b (con las reglas de S0-6a apagadas) y 51 de S0-6a | `selftest_e0_S0-6a.txt`, `sha_codigo_selftests_S0-6a.txt` |
| b52, b581, b582, b583 | 39/39, 34/34, 59/59, 33/33, rc 0 | `selftests_b5x_S0-6a.txt` |
| selftest de claves de la caché | **VEREDICTO OK**; anclaje r2b OK (2.449 claves); contraste con la tabla OK; salida igual byte a byte a `923dd900…` | `selftest_claves_cache_S0-6a.txt`, `selftest_clave_cache_S0-6a.json` |
| selftest de claves de S0-6a | VEREDICTO OK (creadas 1.168, quitadas 249, cambiadas 2.408, exactamente las declaradas); con la lista perturbada (una clave cambiada quitada), VEREDICTO FALLA | `../censos/claves_control_S0-6a.json`, `../censos/claves_control_negativo_S0-6a.json` |
| control de continuidad | antes 88 saltos (igual byte a byte al JSON de S0-5b); después 76 (§9) | `control_continuidad_{antes,despues}_S0-6a.json`, `lista_continuidad_S0-6a.md` |
| selftest del control de continuidad (S0-4b contra la corregida) | 14/14 | `selftest_control_continuidad_S0-6a.txt` |
| parche en seco sobre una copia de los tres archivos de S0-5b | rc 0; los tres archivos de después, iguales byte a byte a los finales | `../parche/LEEME.md` |

La medición sin la exclusión de la tanda 0 (`S0_6_TANDA0=1`, solo para medir) da lo que las reglas cambiarían ahí:
73 unidades creadas, 25 quitadas y 1.055 cambiadas en los diez TOs (`medicion_tanda0_sin_exclusion_S0-6a.json`, ids y
cuentas). Es el límite declarado de la tanda 0: la exclusión rige y su salida no cambia.

## 3. Lo que corrige cada fila (evidencia de las 40 filas; `scripts/filas_40_S0-6a.py`)

La evidencia completa, con el texto de cada unidad, va en el paquete (`filas40_S0-6a.md` y `.json`). Resumen con la
tabla del §5 de la nota (la fila de la tanda 0, por la adenda 2, §2, punto 3):

| ficha | pregunta | regla | se espera | queda |
|---|---|---|---|---|
| E1-008 | unidad | A | corregida | **no corregida** (abajo) |
| E1-010 | unidad | A | corregida | corregida: `ri_dcpc::3.7.6` termina en la p. 26 (5 renglones); la tabla es una división de la Sección 3 |
| E1-047 | unidad | J | corregida si la causa es general | corregida: `ceninf::S0` lleva el título y la fecha de la carátula, sin «Preámbulo»; la causa es general (DISENO, §4) |
| E1-081 | unidad | B | corregida | corregida: la intro empieza en «Bajo la supervisión…»; el título de dos renglones va entero en el encabezado |
| E1-090 | unidad | B | corregida | corregida: el título de tres renglones de 8.4.4 va entero en el encabezado; no queda intro |
| E2-002 | unidad | E + A | corregida | corregida: `ri2_ae::A3::14.3`, dos renglones en la p. 28; 15 y 16 abren |
| E2-002 | herencia | B + A | corregida | **dudosa**: hereda «ANEXO III» y el 14 entero sin «14.» fabricado; además hereda el texto de la raíz 0 del Anexo III (su título, su índice interno y dos bloques intersticiales) |
| E2-005 | unidad | H | corregida | corregida: «1.2.3.Conceptos…» abre; 1.2.2 son cinco renglones |
| E2-006 | unidad | C + A + K | corregida | corregida: termina en «…normas reglamentarias.», sin el cierre de la declaración, los rótulos de firma ni el código del formulario |
| E2-006 | herencia | I + A | corregida | corregida: «DECLARACIÓN JURADA DEL SOCIO RESPONSABLE» y «Declaro bajo juramento…», no el membrete |
| E2-007 | herencia | A | corregida | corregida: «APARTADO A: OPERACIONES DE CAMBIOS» |
| E2-008 | herencia | C + A | corregida | corregida |
| E2-011, E2-016, E2-028, E2-034, E2-040, E2-043 | herencia | B | corregida | corregidas: sin encabezado fabricado; la intro lleva el texto entero con su número |
| E2-033 | la que sigue | C | corregida | corregida: la que sigue a `cryl::4.2.2` es `cryl::S4::cierre` |
| E2-039 | unidad y herencia | A | corregida | corregidas: `ribspc::S4` termina en la p. 1; hereda «NORMAS DE PROCEDIMIENTO» e «Instrucciones generales» |
| E2-045 | la que sigue | C | corregida | corregida: `snp_spd::5.5.3` termina en su texto; el párrafo pasa a la intersticial de 5.5 |
| E2-045 | herencia | B | corregida | corregida |
| E2-046 | unidad (limpieza) | F | corregida | corregida: `efemin::1.3.7.2` es un renglón |
| E2-046 | herencia | B + F | corregida | corregida |
| E2-055 | herencia | B | sigue con error (tanda 0 fuera) | sigue con error en la salida; en `selftest_e0`, con la exclusión apagada solo ahí, queda corregida |
| E2-056 | unidad y herencia | A | corregida | corregidas: `ri_psprca::S10` es un renglón; hereda la banda, «Apartado A: ATMs en Argentina» y su introducción hasta «Datos solicitados:» |
| E2-057 | herencia | A | corregida | corregida: «ANEXO II», el título del anexo y su introducción |
| E2-058 | unidad | A | corregida | corregida: `ri_spi::C.1.3` es un renglón; los anexos quedan fuera |
| E2-058 | herencia | D (con A) | corregida | corregida: «APARTADO C: … CON EL» y «APARTADO B», el título entero que R5-c deja |
| E2-065 | unidad | E | corregida | corregida: `seggar::5.3.5` termina en la p. 6; «6. Instrumentación.» abre |
| E2-066 | herencia | F | corregida | corregida: «Exposiciones Límite» no es intro del 2.3.1 |
| E2-094 | la que sigue y herencia | G | corregida | corregidas: abre 6.2.1.10; sin fragmentos del número |
| E2-096, E2-097 | herencia | C | corregida | corregidas |
| E2-098 | herencia | D | corregida | **dudosa**: el rótulo heredado es el impreso; pero C lleva al Apartado B las notas que siguen a B.1, B.2 y B.3 (en la columna de los rótulos de B.1 a B.3), y B.1.28 hereda las tres |
| E2-099 | la que sigue | A | corregida | corregida: la que sigue a C.11 es el bloque «Validación del Apartado A – …», que termina antes de «Validación del Apartado B» |
| E2-099 | herencia | D | corregida | corregida |

Cuenta (40 filas): 36 corregidas, 2 dudosas (E2-002 y E2-098, en la herencia), 1 no corregida (E1-008) y 1 de la tanda 0
(E2-055), que sigue con error en la salida, como se espera.

**E1-008, no corregida.** A abre el Anexo III y el Anexo IV de nmaeef como sub-documentos, y E abre las raíces 12 a 24
del Anexo III: el 21.3 queda dentro de la raíz 21, en la p. 31, y el Anexo III termina en la p. 35. Pero en el Anexo IV
la numeración vuelve a empezar después de su índice (1 a 6 en la p. 36) y E0 rechaza las raíces que siguen por la
sucesión: el texto de la p. 37 en adelante queda como cierre de la raíz 0 del anexo, partido en seis partes
(`nmaeef::A4::S0::cierre::parte1` a `::parte6`). El texto de la parte leída en S1-ter queda en `…::parte5`, que sigue
llevando 4.2 a 4.4 de los informes. Ninguna regla de la nota cubre el reinicio de la numeración después de un índice
dentro de un anexo; no diseñé una.

## 4. Censo por regla y generalidad (`censos/censo_por_regla_S0-6a.{json,md}`, `censos/generalidad_S0-6a.json`)

Cada regla sola contra todas apagadas (la salida de S0-5b), sobre los 152 (`s0_5/scripts/censo_por_regla_S0-5a.py`).
La generalidad es por documentos con unidades que cambian (creadas, quitadas o cambiadas), contra los documentos de las
filas de su letra en la nota (§3), con las de segunda causa.

| regla | TOs con archivos distintos | TOs con unidades que cambian | de esos, donde no se vio | unidades (creadas / quitadas / cambiadas) | general | salen de la bolsa | filas que corrige |
|---|---|---|---|---|---|---|---|
| a | 58 | 58 | 49 | 890 / 183 / 627 | sí | — | E1-010, E2-007, E2-039 (2), E2-056 (2), E2-057, E2-058 unidad, E2-099 la que sigue; con otra regla, E2-002 unidad, E2-006 (2), E2-008, E2-096 |
| b | 50 | 50 | 41 | 0 / 9 / 757 | sí | — | E1-081, E1-090, E2-011, E2-016, E2-028, E2-034, E2-040, E2-043, E2-045 herencia; con F, E2-046 herencia; E2-055 solo en el selftest |
| c | 60 | 49 | 46 | 130 / 31 / 1.077 | sí | — | E2-033, E2-045 la que sigue, E2-097; con A, E2-006 unidad, E2-008, E2-096 |
| d | 13 | 13 | 11 | 0 / 0 / 270 | sí | — | E2-058 y E2-099 herencia |
| e | 7 | 6 | 4 | 98 / 65 / 23 | sí | — | E2-065; con A, E2-002 unidad |
| f | 7 | 6 | 4 | 0 / 8 / 86 | sí | — | E2-046 unidad, E2-066 |
| g | 1 | 1 | 0 | 1 / 1 / 9 | **no** | **lingeef** | E2-094 (2) |
| h | 43 | 3 | 2 | 24 / 13 / 50 | sí | — | E2-005 |
| i | 1 | 1 | 0 | 0 / 0 / 40 | **no** | **ri_ccna** | E2-006 herencia (con A) |
| j | 2 | 2 | 1 | 0 / 0 / 2 | sí | — | E1-047 |
| k | 1 | 1 | 0 | 0 / 0 / 6 | **no** | **ri_ccna** | E2-006 unidad, la limpieza (con C y A) |

- **Salen de la bolsa** de la evaluación final (`docs/plan_tesis.md:782`, punto 4), y lo declaro: **lingeef** (G solo
  cambia lingeef, como anticipa la nota) y **ri_ccna** (I y K solo cambian ri_ccna). I no alcanza los límites declarados
  de ri_iepsp ni de ri_ieccm: no cambia ninguna unidad de esos documentos.
- **Configuración final** contra todas apagadas: 118 TOs con archivos distintos; 3.825 eventos (1.168 claves creadas, 249
  quitadas, 2.408 cambiadas). 2.178 son iguales a lo que da una regla sola (atribución exacta); 1.377 los produce al
  menos una regla sola (el mismo evento sobre la misma clave), pero la unidad final no es la de ninguna regla sola
  porque otra regla también la cambia (en 946 de ellos una sola regla produce el evento: A en 623, C en 311, otras en
  12); y 270 no los produce ninguna regla sola (210 claves creadas y 60 cambiadas): nacen de la combinación de reglas.
  194 eventos de una regla sola no están en la final (A 86, E 73, C 35: otra regla deshace o cambia lo que esa hace).
  Todo, clave por clave, en `censos/claves_S0-6a.json` (con `reglas`,
  `atribucion_exacta` y `campos`) y en el `NO_ABRIR_` del antes y el después.

## 5. Las reglas por lista que se reemplazan (`scripts/reemplazos_S0-6a.py`; `censos/reemplazos_S0-6a.json`)

Por lista, las unidades que tocaba en la E0 de S0-5b (DISENO, §1) y qué da la regla general sola:

- **R5-g → E** (ri_oc, «3. Aclaraciones»): las 51 unidades, iguales. E da el mismo resultado, como pide el mandato.
- **R5-f → H** (ri_ccna, 11 rótulos): las 11 unidades, iguales.
- **R5-a′ → A** (ri_oc): el bloque `ri_oc::Sbloque1` de S0-5b (pp. 19-21) no existe con ese id: A lo separa en los
  bloques de cada título (el de E2-099), con otra numeración de `Sbloque`.
- **R5-a → C** (43 listas, 191 unidades): 30 listas dan lo mismo (111 unidades iguales). En 13 cambia algo:
  - el corte, en 6: `cryl` 4.2.2 (el cierre pasa a la Sección 4: es la corrección de E2-033); `ri2_ae` 14.3 (con C sola
    el 14.3 vuelve a extenderse; en la final lo cortan A y E); `ri_spi` C.1.3 (con C sola el cierre sale, como con
    R5-a, pero los anexos siguen en C.1.3; en la final los saca A); `adfsp` 1.1.10 (el cierre de 1.1 vuelve al
    ítem); `ri_rml` 1.4.2 (el párrafo «Para el punto 1.4.1. …» corre en 90,3, entre las columnas de 1.4 —95,8 y 83,7— y
    la del texto del 1.4.2 —97,8—: con la tolerancia fijada la columna no discrimina y queda en el ítem); y `ri_oc`
    B.1.28, B.2.4 y B.3.4 (las notas que siguen a cada lista corren en la columna de los rótulos de B.1 a B.3, la de
    los hijos del Apartado B: C las lleva al apartado, y las heredan todos sus puntos);
  - solo la herencia, en 7 (`apnf` 1.3.1.2, `depaho` 3.11.5.5, `manori` 1.1.6.5, 1.4.1.3 y 3.4.1.3, y las de arriba
    que también cambian herencia): por otros párrafos que C mueve en el mismo documento.

  Los documentos que salieron de la bolsa por esas correcciones siguen afuera (mandato, §2).

## 6. Claves (`s0_5/scripts/claves_S0-5a.py`; `censos/claves_S0-6a.json`)

3.825 claves: 1.168 creadas, 249 quitadas y 2.408 cambiadas; por regla (atribución, una clave puede tener varias):
A 1.609, B 739, C 1.166, D 249, E 94, F 68, G 11, H 87, I 38, J 2, K 6. Las de las unidades que ninguna regla toca no
cambian (el control da exactamente las declaradas). Las claves nuevas siguen la convención de E0: `<to>::Sbloque<k>` y
`<to>::S<letra>` para las divisiones de A (la de R5-a′); el prefijo de sub-documento (`<to>::A<n>::…`) para los anexos
que A abre en los TOs donde no los había (por eso cambian de clave unidades cuyo texto no cambia, como
`ri2_ae::A1::2.1.5` o `nmaeef::A1::8.2`); `<unidad>::cierre`, `::intersticial` y `::chapeau_seccion` para los
segmentos que C y A mueven. Una unión conserva la clave de la primera unidad (R5-a′ y G: `lingeef::6.2.1.10` abre y
`lingeef::6.2.1::cierre` deja de existir). La lista entera, con su regla, está en `censos/claves_S0-6a.json`; el
selftest de claves da OK solo con esa lista.

## 7. Las unidades leídas en S1-ter (§4 del mandato; `scripts/control_leidas_S0-6a.py`)

De las 286 (90 de la etapa 1 y 196 de la etapa 2), en la E0 corregida: 189 iguales (corte y herencia) y 97 cambian.
De las que cambian, 27 tienen el cambio en una pregunta con fila en el TSV (es el que se busca) y **70 van al FRENO**:
en 9 cambia el corte que S1-ter juzgó correcto, en 15 la herencia juzgada correcta, y en 55 una herencia que S1-ter no
juzgó (una unidad puede estar en más de una de esas tres cuentas). Por la regla que, sola, cambia cada una: C 23, B 10,
D 9, A 6, F 2, G 1; varias reglas 18 (A con C 8, C con D 3, A con B 2, A con E 1, A con B y E 1, A con C y E 1, C con D
y E 1); y 2 que ninguna regla sola cambia (`snp_tr::1.3.1.3` y `snp_tr::1.6.2.1`: C con otra). El detalle, unidad por unidad, con
el texto antes y después, lo que se juzgó y la regla, está en `censos/control_leidas_S0-6a.md`; los ids, campos y
reglas, en `censos/control_leidas_S0-6a.json`. Lo que pesa:

- **Cortes juzgados correctos que cambian (9):** 4 cambian solo de clave (el mismo texto, en el sub-documento que A
  abre: `ri2_ae::2.1.5` → `ri2_ae::A1::2.1.5`, `ri2_ae::S14::cierre` → `ri2_ae::A3::S14::cierre`, `nmaeef::8.2` →
  `nmaeef::A1::8.2`, `nmaeef::S9` → `nmaeef::A1::S9`); `ri_ccna::D2A1P1::S0` (la que sigue de E2-006, un renglón, «I -
  CONCEPTOS BÁSICOS») deja de ser unidad: A lo toma como título de la raíz del sub-documento y lo heredan
  `ri_ccna::D2A1P1::S1` y `::S2`; `gerc::2.3.2::intro` (la que sigue de E2-066, «Exposiciones Límite») pasa a la
  unidad de la tabla, `gerc::2.3.2.1` (F2: es el encabezado de columnas, H7); y 3 de C: `ri_rml::1.4.2` y
  `ri_rml::1.4::cierre` (la tolerancia no discrimina, §5) y `ri_oc::B.1::cierre` (sus notas pasan al Apartado B, §5).
- **Herencias que cambian con C (36 de las 70 tienen a C entre sus reglas):** C lleva a la sección (o al apartado) párrafos que corren en la columna de
  la sección, y E0 hace heredar las intersticiales y el cierre de un ancestro a todas sus unidades: aparecen en la
  herencia de unidades leídas de la misma sección (por ejemplo, rótulos y renglones de formularios en depaho, apnf y
  ayccef; las notas del Apartado B en ri_oc; un párrafo del 1.4 de ri_rml en la Sección 1).
- **B (10), D (9), F, G:** son el efecto buscado en unidades vecinas de las filas: el número sin encabezado fabricado
  en los cierres e intros que heredan del mismo punto (B), el rótulo impreso en las unidades de los apartados de ri_spi
  y en ri2_pm (D), etc.

Ningún ajuste del §3 del DISENO se hizo por una unidad que no sea de las 40 ni de las 286.

## 8. Lo que la nota deja en mis manos

En DISENO, §4: la tolerancia de C (3,0 pt, sin cambios), el motivo de E2-065 (`raiz_en_columna_profunda_83.7_vs_76.6`,
el de E), la causa de J (general), «Ello, siempre que…» de E1-081 (en `seguef::2.13::cierre`) y la aceptación de R5-e
actualizada por K (`selftest_e0`, z: ninguna unidad de D1F3 lleva el código del pie ni termina en la «C» suelta; D1F4
sin letras sueltas y con su «CODIGO»). La declaración del reemplazo en E2-007 y E2-058 (la adenda 1, §1), en DISENO, §5.

## 9. Continuidad de la numeración (`s0_5/scripts/control_continuidad_numeracion.py`)

Antes, 88 saltos (16 de la clase i y 72 de la ii), igual byte a byte al JSON de S0-5b; después, 76 (21 i y 55 ii).
Cierran 28 (ri2_ae 11, nmaeef 6, ri_laft 6, snp_dd 3, ri_cc 2); uno de ri_cc sigue y cambia de unidad (1.8.1, ahora en
el bloque que A abre, `ri_cc::R4::Sbloque1`); y aparecen 16 nuevos: adfsp 6.1 a 6.4 en el sub-documento A (i: A abre un
sub-documento de anexo a mitad de la Sección 6), nmaeef 4.1 a 4.6 del Anexo IV (ii: la numeración que E0 no abre,
E1-008), ri2_ae 3.1 del sub-documento A1 (ii) y ri_saofe 1.12 a 1.16 (ii: E abre raíces que se tragan esos puntos). La
lista para la autora, con su clase y su unidad, está en `controles/lista_continuidad_S0-6a.md` (sin el renglón citado:
el antes y el después con texto va en el `NO_ABRIR_`).

## 10. E y los 87 rechazos (`scripts/rechazos_e_S0-6a.py`; `censos/rechazos_e_S0-6a.json`)

En la E0 de S0-5b hay 87 rechazos de raíz por la columna en 7 documentos. Con E sola se abren 36 (nmaeef 13, ri2_ae 13,
ri_saofe 6, ri_laft 2, manual 1, seggar 1) y siguen 51: 13 por la columna y 38 que pasan a rechazo por la sucesión
(después de abrirse la raíz anterior, la que sigue no la sucede). En la corregida, lo mismo.

## 11. Unidades que no son de las 40 ni de las 286 y me parecen un error de una regla

Solo su id y la regla (mandato, §2); no cambié ninguna regla por ellas:

- A: `ri_oc::SA`, `ri_oc::SB` y `ri_oc::SC::chapeau_seccion` (renglones «Apartado X: …» del preámbulo que abren
  apartados); los bloques de los formularios D1F3 y D1F4 de ri_ccna (`ri_ccna::D1F3::Sbloque6` a `::Sbloque18`,
  `ri_ccna::D1F4::Sbloque19` a `::Sbloque30`); `adfsp::A::S0::chapeau_seccion` (el sub-documento que corta la Sección
  6); `ri_cc::R4::Sbloque1`.
- A y E: `nmaeef::A4::S0::cierre::parte1` a `::parte6` (la numeración del Anexo IV).
- E: `ri_saofe::S2` a `ri_saofe::S7`.
- I: el rótulo de `ri_ccna::D1F4` («C O D I G O», letras separadas).

## 12. Tabla de reprocesamiento: la fila propuesta

`data/experiment/mantenimiento/tabla_reprocesamiento.md` está fuera de lo que puedo escribir: la fila queda propuesta,
para S0-6b, con anclas al código final (el del parche).

| Fila | Cambio | Dónde entra | Qué obliga a recomputar | Clave E1 | Clave E3 | Clase | Principio | Ancla | Variación del selftest |
|---|---|---|---|---|---|---|---|---|---|
| F19d | Release de E0 (e0-r2) con reglas generales antes de una tanda, con la tanda 0 fuera por lista: reglas que crean, quitan o cambian unidades de las tandas siguientes sin cambiar la tanda 0 | E0 e0-r2 de las tandas siguientes; la de la tanda 0, byte a byte igual | en la tanda 0, nada; en las siguientes, las unidades nuevas y las que cambian texto o herencia entran a E1 y E3 por F19b y F01 a F03, cuando esa tanda se extraiga | no cambia en la tanda 0 | no cambia en la tanda 0 | ninguna en la tanda 0 | 9 (como F19b) | `correr_e0.py:207-231` (reglas, exclusión de la tanda 0 y reemplazos), `:830-845`, `:1423-1425`, `:1469`, `:1495-1498`, `:1681-1689`; `e0_lib.py:228-238` (docstring), `:544-650` (las once reglas y sus constantes), `:3092`, `:3147`, `:3261`, `:3532`, `:4195` | ninguna clave de la tanda 0 se mueve (OK); la variación propia la decide S0-6b |

**Anclas que el parche corre** (`controles/anclas_e0_tabla_S0-6a.txt`, `s0_5/b/scripts/anclas_e0_tabla_S0-5b.py` con la
E0 de S0-5b como «antes»): de las 27 citas de la tabla al código de E0, 12 quedan iguales, 14 se mueven (el mismo
bloque, en otro rango) y una no se encuentra entera: `correr_e0.py:140-210` de F19b (el bloque de S0-5, donde el parche
cambia `_r5` para los reemplazos). S0-6b las corrige, como hizo S0-5b.

## 13. Comandos

```
python -B scripts/armar_proto_S0-6a.py <correr_e0.py final> <correr_e0.py del prototipo>
scripts/lote_configuraciones_S0-6a.sh <copia> <raíz prototipo> <raíz final> <corridas> NINGUNA TODAS a b c d e f g h i j k FINAL
SUF=_2 scripts/lote_configuraciones_S0-6a.sh <copia> <raíz prototipo> <raíz final> <corridas> TODAS
python -B scripts/comparar_archivos_S0-6a.py <dir a> <dir b>
python -B s0_5/scripts/censo_por_regla_S0-5a.py --base c_NINGUNA --final c_FINAL --regla a=c_a … --regla k=c_k --out censos/censo_por_regla_S0-6a.json
python -B s0_5/scripts/claves_S0-5a.py declarar --censo censos/censo_por_regla_S0-6a.json --out censos/claves_S0-6a.json
python -B s0_5/scripts/claves_S0-5a.py controlar --antes c_NINGUNA --despues c_FINAL --claves censos/claves_S0-6a.json --out censos/claves_control_S0-6a.json
python -B scripts/generalidad_S0-6a.py --censo censos/censo_por_regla_S0-6a.json --tsv <TSV> --out censos/generalidad_S0-6a.json
python -B scripts/resumen_censo_S0-6a.py --censo … --claves … --generalidad … --out censos/censo_por_regla_S0-6a.md
python -B scripts/reemplazos_S0-6a.py --codigo <e0_chunking final> --base c_NINGUNA --regla c=c_c --regla a=c_a --regla e=c_e --regla h=c_h --final c_FINAL --out censos/reemplazos_S0-6a.json
python -B scripts/rechazos_e_S0-6a.py --base c_NINGUNA --regla-e c_e --final c_FINAL --out censos/rechazos_e_S0-6a.json
python -B scripts/control_leidas_S0-6a.py --comun s1quater/diseno/scripts --orden s1ter/tramo_b/orden_lectura_S1ter.json --base s1ter/e0 --final c_FINAL --regla a=c_a … --tsv <TSV> --out censos/control_leidas_S0-6a.json --md censos/control_leidas_S0-6a.md
python -B scripts/negativos_leidas_S0-6a.py --comun … --orden … --base s1ter/e0 --final c_FINAL --regla a=c_a … --tsv <TSV> --tos <los de TOS_S06> --out censos/negativos_leidas_S0-6a.json
python -B scripts/filas_40_S0-6a.py s1quater/diseno/scripts s1ter/e0 c_FINAL <TSV> <json> --fichas <fichas> --md <md>
python -B scripts/medicion_tanda0_S0-6a.py <tanda 0 con S0_6_TANDA0=1> <salida_tanda0_r2b> controles/medicion_tanda0_sin_exclusion_S0-6a.json
python -B s0_5/scripts/antes_y_despues_S0-5a.py --censo … --claves … --antes c_NINGUNA --despues c_FINAL --out-md <NO_ABRIR_….md> --out-jsonl <NO_ABRIR_….jsonl>
python -B s0_5/scripts/control_continuidad_numeracion.py --e0 <E0> --lineas <caché> --out <json>
python -B s0_5/scripts/lista_continuidad_S0-5a.py --antes <json> --despues <json> --out <md>
python -B s0_5/scripts/selftest_control_continuidad.py --antes s1bis/e0 --despues c_FINAL --lineas <caché>
python -B s0_4/scripts/control_tanda0_en_152.py c_FINAL <salida_tanda0_r2b>
scripts/lote_controles_S0-6a.sh <trabajo> <copia> <raíz final> <python>
scripts/selftests_S0-6a.sh <logs> <copia con el parche> <python> <tmp>
scripts/armar_parche_S0-6a.sh <código S0-5b> <código final> <prototipo> parche <prueba>
python -B scripts/manifest_salida_S0-6a.py --e0 <c152_1> --codigo <e0_chunking final> --tiempos … --tiempos2 … --out manifiestos/manifest_salida_e0_152_S0-6a.json
python -B s0_5/b/scripts/anclas_e0_tabla_S0-5b.py mantenimiento/tabla_reprocesamiento.md <código S0-5b> <código final>
```

`scripts/solapes_S0_6a.py` es el módulo de solapes de texto que usan `control_leidas_S0-6a.py` y `filas_40_S0-6a.py`. Del
diseño sellado de S1-quater importo, sin cambios, `mostradas_S1ter`, con la clase `E0` y `leer_sellado` del mismo módulo,
que esa función necesita (la E0 que leyó S1-ter y el orden sellado, con su sha256); no escribí nada en `s1quater/`.

## 14. Repo, `.pyc` y convenciones

- **Repo** (`s0_1/scripts/snapshot_repo.py`): foto antes, a las 10:20:57, 49.651 archivos; después de escribir `s0_6/`,
  49.711: los 60 nuevos están todos en `s0_6/`; 0 borrados y 0 cambiados. Con este informe completo y el grep de abajo,
  `s0_6/` tiene 61 archivos; la última foto, en el mensaje del FRENO.
- **`.pyc`** fuera de `.venv/`: 2.213 antes y 2.213 después, la misma lista.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py`, sobre los 60 archivos de `s0_6/` que no son su salida,
  `controles/grep_convenciones_S0-6a.txt`): control positivo 16 de 16; 0 nombres de personas y 0 rutas absolutas; 4
  coincidencias de un término de la lista de origen conversacional, las cuatro dentro del rótulo de un campo de un
  formulario de la norma, en el texto heredado de unidades leídas que muestra
  `censos/control_leidas_S0-6a.md`: no es el origen de una decisión.
- Los logs y salidas que guardo llevan `<scratchpad>` y `<home>` en lugar de las rutas de la sesión.
