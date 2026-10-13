# U-SEG-OFICIAL — informe de S0-6a-bis (12/10/2026)

**Este archivo nombra unidades con error de corte y de herencia: ninguna lectura a ciegas lo abre, tampoco la de
S1-quater.** Texto de unidades: solo de las 40 filas y de las 286 leídas en S1-ter; de las demás, solo cuentas por regla y
por documento, sin ids. Los ids, el antes y el después de las demás y las salidas de E0 van en los archivos `NO_ABRIR_`
del paquete de revisión, fuera del repo. USD 0, sin API. **Nada commiteado; el parche no se aplicó al repo.** Diseño:
`DISENO_S0-6a-bis.md`. Las rutas `censos/…`, `controles/…`, `parche/…` y `scripts/…` son de `s0_6/bis/`; las de
`../scripts/…`, de `s0_6/scripts/` (los scripts de S0-6a, que reuso sin cambios), y las de `s0_5/…`, `s0_4/…` y
`s0_1/…`, de `segmentacion_oficial_e0r2/`.

## 1. Entrada

- Paso 0: `pwd` = la raíz del repo; HEAD `d32f6db8` («Segmentacion oficial: la correccion de E0 con reglas generales,
  en freno (diseno, parche, censos y controles)»); `git status --porcelain` sobre `s0_6/`, vacío; `s0_6/bis` no existía.
- Mandato `docs/mandatos/USEG_OFICIAL_S0-6a_correccion_E0.md`, leído en HEAD: `5edfd993…`, igual al del despacho; con
  los cambios del «seguí» de S0-6a-bis, que rige donde difieren.
- Del paquete de la mesa, solo los cuatro archivos de `para_la_ejecutora_S0-6a/` (`096cd54f…`, `767ac8bd…`,
  `6e880ab1…`, `5fe8a7dd…`, los del despacho de S0-6a) y `cambios_en_leidas_S0-6a_clasificados_mesa.md` (`b2cb4709…`,
  el del «seguí»). No abrí nada más del paquete ni las carpetas que el «seguí» prohíbe.
- Código de partida, el del repo (S0-5b): `e0_lib.py` `bd2190ad…`, `correr_e0.py` `68bd74b5…`, `selftest_e0.py`
  `789630b5…`, `e0_tablas.py` `ab300a22…`. El de S0-6a, con el que comparo, sale de aplicar
  `../parche/parche_e0_S0-6a.diff` a una copia de esos tres archivos: `6dd42bf3…`, `cd97223a…`, `83ae5576…` (rc 0).
- Foto sha256 del repo entero, sin `.git` y sin ninguna otra exclusión (`scripts/foto_repo_entero_S0-6a-bis.py`): a las
  19:07:27, 50.271 archivos (los enlaces simbólicos, 342, por su destino).
- Todo corrió sobre copias sin enlaces: la de S0-6a (`rsync -a --no-links`, sin `.git`, `.venv`, `.venv-app`,
  `__pycache__` ni `.DS_Store`), para el lote del censo; y una copia nueva del repo en HEAD con el mismo `rsync` (0
  enlaces), con el parche aplicado con `patch -p1`, para los controles finales y los selftests. Entre `e4bb93ce` (la de
  S0-6a) y `d32f6db8` solo cambian `s0_6/`, `data/backlog/backlog.jsonl` y archivos del diseño de S1-quater: ninguna
  entrada de E0. Intérprete: el `.venv` del repo con `-B` y `PYTHONDONTWRITEBYTECODE=1`; los scripts de solo lectura, con
  `/usr/bin/python3 -B`.

## 2. Las seis decisiones: qué hice

El detalle de cada definición, con el caso que la motiva, está en DISENO, §1 a §6. Las definiciones las fijé y las anoté
antes de correr el censo (las notas de trabajo se crearon a las 19:14:22 y se modificaron por última vez a las
19:35:40; el lote del censo arrancó a las 19:41:21), y no las ajusté después; van al paquete como `NO_ABRIR_notas_definiciones_S0-6a-bis.md`, porque citan listas que no son de
diseño.

1. **Los 70 cambios** (la clasificación de la mesa, aceptada): B, D, F, G y la parte de A que mejora quedan como en
   S0-6a; H, I, J, K y E tampoco cambian.
2. **C y A, ajustadas.** C no mueve un párrafo cuyos renglones no comparten columna (a 3,0 pt o menos del x0 del segundo
   renglón, salvo el primero), ni el grupo que ese párrafo arrastra, ni un grupo al que le sigue una tabla; y mide el
   párrafo por la columna que comparten sus renglones, no por el más a la izquierda. La tolerancia sigue en 3,0 pt
   (`TOL_COL_C`). La columna propia de un punto cuyo renglón de rótulo es un título vuelve a ser la de su texto. A no
   abre divisiones en una carátula: la página 1 leída como cuerpo con a lo sumo 8 renglones (el tope de J).
3. **Las 13 listas,** con C ajustada, comparadas con la página (D19, D21, D13 bis): §6.
4. **La herencia:** la política no cambia; su tamaño, en tres corridas, en §9. El efecto en el costo de E1 y en el tope
   de la tanda 1 no lo calculo: lo calcula la mesa, y queda **NO VERIFICADO**.
5. **E1-008:** la regla L (interruptor `l`), de D15: un índice leído como cuerpo no corta la sucesión de números. §4.
6. **E2-002 y E2-098:** la regla M (interruptor `m`): la raíz 0 de un sub-documento que abre A aporta a la herencia solo
   su título; E2-098, R5-a por lista en ri_oc B.1. §4.

## 3. Controles duros (mandato, §6)

| control | resultado | archivo (`controles/`) |
|---|---|---|
| todas las reglas apagadas (prototipo, `S0_6_REGLAS=NINGUNA`) contra el manifiesto de la E0 de S0-5b (`s0_5/b/manifiestos/manifiesto_salida_e0_152_S0-5b.json`) | 768 de 768 iguales; 9.665 unidades | `comparar_NINGUNA_vs_S0-5b_S0-6a-bis.txt` |
| los 152: prototipo con todas, código final sin interruptor, y otra vez el prototipo | 768 de 768 iguales entre las tres; **10.478 unidades** (S0-6a: 10.584) | `comparar_FINAL_vs_TODAS_S0-6a-bis.txt`, `comparar_TODAS_2_vs_TODAS_S0-6a-bis.txt`, `comparar_FINAL_vs_TODAS_2_S0-6a-bis.txt` |
| contra S0-5b | 256 de 768 archivos distintos: chunks 106, estructura 106, tablas 37 y 7 agregados (S0-6a: 265); la diferencia, regla por regla, en §7 y §8 | `comparar_FINAL_vs_S0-5b_S0-6a-bis.txt` |
| corrida de controles con el código del parche, en la copia nueva del repo (`scripts/lote_controles_S0-6a-bis.sh`): los 152 dos veces (21:18:35-21:28:35) | 768 de 768 iguales entre sí y con la final; `por_to/` sin diferencias; 10.478 unidades; manifiesto en `../manifiestos/` | `comparar_c152_1_vs_FINAL_S0-6a-bis.txt`, `comparar_c152_2_vs_c152_1_S0-6a-bis.txt`, `diff_por_to_c152_S0-6a-bis.txt` (vacío), `lote_controles_S0-6a-bis.log` |
| tanda 0 con el código del parche, `s0_1/scripts/correr_tanda0.py`, dos veces (21:28:35-21:32:59), contra `salida_tanda0_r2b/` | **57 de 57** en las dos; 2.439 unidades | `comparar_t0_1_vs_r2b_S0-6a-bis.txt`, `comparar_t0_2_vs_r2b_S0-6a-bis.txt` |
| los 25 archivos de la tanda 0 dentro de los 152 | **25 de 25**; agregados: 20 iguales y 15 ausentes en los dos | `control_tanda0_en_152_S0-6a-bis.txt` |
| censo por regla en la tanda 0 | 0 cambios: ningún TO de la tanda 0 entre los que cambia una regla ni la configuración final | `../censos/censo_por_regla_S0-6a-bis.json` |
| claves de la tanda 0 | **ninguna clave de la tanda 0 se mueve** (0 de 3.122) | `../censos/censo_por_regla_S0-6a-bis.md` |
| selftest de claves de S0-6a-bis | VEREDICTO OK (1.057 creadas, 244 quitadas, 1.821 cambiadas, exactamente las declaradas); con la lista perturbada, VEREDICTO FALLA | `claves_control_S0-6a-bis.json` |
| control de continuidad | antes 88 (igual byte a byte al JSON de S0-5b); después 70 (§10); selftest del control 14/14 | `continuidad_antes_vs_S0-5b_S0-6a-bis.txt`, `continuidad_cuentas_S0-6a-bis.json`, `selftest_control_continuidad_S0-6a-bis.txt` |
| manifiesto de la salida de los 152 (formato de `s1ter/manifest_salida.json`; `scripts/manifest_salida_S0-6a-bis.py`) | 768 archivos `e0/<archivo>`, 10.478 unidades, con el sha256 del código | `../manifiestos/manifest_salida_e0_152_S0-6a-bis.json` (`991ac178…`) |
| `selftest_e0` (sobre la copia nueva del repo con el parche) | **251/251**, rc 0: los 188 de S0-5b (con las reglas de S0-6a y S0-6a-bis apagadas) y 63 de S0-6a y S0-6a-bis (x 6, y 17, y′ 6, z 34; S0-6a tenía 51: x 4, y 17, z 30) | `selftest_e0_S0-6a-bis.txt`, `sha_codigo_selftests_S0-6a-bis.txt` |
| b52, b581, b582, b583 | 39/39, 34/34, 59/59, 33/33, rc 0 | `selftests_b5x_S0-6a-bis.txt` |
| selftest de claves de la caché | **VEREDICTO OK**; salida igual byte a byte a la de S0-6a (`923dd900…`) | `selftest_claves_cache_S0-6a-bis.txt`, `selftest_clave_cache_S0-6a-bis.json` |
| parche en seco sobre una copia de los tres archivos de S0-5b, y el diff contra S0-6a sobre una copia de los de S0-6a | rc 0 los dos; los tres archivos de después, iguales byte a byte a los finales | `prueba_parche_S0-6a-bis.txt` |
| medición de la tanda 0 sin la exclusión (prototipo con `S0_6_TANDA0=1`, solo para medir) | 64 unidades creadas, 25 quitadas y 994 cambiadas en los diez TOs (S0-6a: 73, 25 y 1.055); la exclusión rige y la salida de la tanda 0 no cambia (límite declarado) | `medicion_tanda0_sin_exclusion_cuentas_S0-6a-bis.json` (los ids, en el `NO_ABRIR_`) |

El log del lote (`controles/lote_configuraciones_S0-6a-bis.log`, de `../scripts/lote_configuraciones_S0-6a.sh`): las
cuatro primeras corridas TODAS (19:17:50-19:40:01) son de desarrollo, con las que fijé las definiciones y la decisión 3;
el lote del censo arranca a las 19:41:21 (NINGUNA), y las dos últimas (21:05:41-21:18:25) son las del efecto marginal de
L y de M (§7).

**El código de las corridas.** El censo corrió con un prototipo armado a las 19:35 (`e0_lib.py` `a49376a8…` y el
`correr_e0.py` de esa hora con el interruptor). El código final difiere de él solo en docstrings (el párrafo de S0-6a-bis
en el docstring del módulo de `e0_lib.py`, agregado a las 20:40:26), un comentario y la forma de escribir
`LISTAS_R5A_S0_6` (el mismo diccionario). La corrida FINAL (20:53) ya usó el código final (`e0_lib.py` `d89aab1a…`,
`correr_e0.py` `78c54c4c…`): 768 de 768 iguales al prototipo con todas. El interruptor del parche
(`parche/interruptor_prototipo_S0-6a-bis.diff`) es el mismo, sobre el código final. Los selftests corrieron dos veces,
sobre `a49376a8…` y sobre `d89aab1a…`, con el mismo resultado; el informe da la segunda.

## 4. Las 40 filas (`../scripts/filas_40_S0-6a.py`)

La evidencia completa, con el texto de cada unidad, va en el paquete (`filas40_S0-6a-bis.md` y `.json`). La misma
evidencia, regenerada sobre la salida final de S0-6a, solo difiere en 5 filas: E1-008, E1-010, E2-002 (unidad y
herencia) y E2-098. En las otras 35 la evidencia es igual byte a byte y el veredicto es el de S0-6a
(`../REPORTE_S0-6a.md`, §3).

| ficha | pregunta | regla | en S0-6a | queda |
|---|---|---|---|---|
| E1-008 | unidad | A + L | no corregida | **corregida**: el Anexo IV de nmaeef abre su numeración después del índice: el texto que la unidad leída arrastraba queda en `nmaeef::A4::4.1.4`, `::4.2::intro`, `::4.2.1`, `::4.2.2`, `::4.3.1`, `::4.3.2`, `::4.4.1` y `::4.4.2` (pp. 51-57); 4.4.2 termina antes de 4.5.1 |
| E1-010 | unidad | A | corregida | corregida: el corte es el mismo (`ri_dcpc::3.7.6`, p. 26, 5 renglones); cambia solo su herencia, que vuelve a la de S1-ter (G11) |
| E2-002 | unidad | E + A | corregida | corregida: `ri2_ae::A3::14.3`, dos renglones en la p. 28; además, con L, el Anexo IV de ri2_ae abre sus puntos (1.1 a 3.5) |
| E2-002 | herencia | B + A + M | dudosa | **corregida**: `ri2_ae::A3::14.3` hereda «ANEXO III», el título de la raíz 0 («PROCEDIMIENTOS MINIMOS DE AUDITORÍA»), el 14 entero sin «14.» fabricado y su cierre; ya no el índice ni los bloques de la raíz 0 |
| E2-098 | herencia | D + R5-a por lista | dudosa | **corregida**: `ri_oc::B.1.28` hereda «APARTADO B: POSICIÓN GENERAL DE CAMBIOS: En dólares estadounidenses.» (el rótulo impreso) y el cierre de B.1 («En el punto B.1.24 deben informarse:…», p. 17, termina antes de B.2); ya no las notas de B.2 y B.3 |

Cuenta (40 filas): **39 corregidas** y la de la tanda 0 (E2-055), que sigue con error en la salida, como se espera, y
queda corregida en `selftest_e0` con la exclusión apagada solo ahí. Ninguna dudosa ni no corregida.

## 5. Las unidades leídas en S1-ter y las 70 de la mesa

**Contra S1-ter** (`../scripts/control_leidas_S0-6a.py`; `censos/control_leidas_S0-6a-bis.{json,md}`, con texto,
regla y lo juzgado): de 286 (90 de la etapa 1 y 196 de la etapa 2), 212 iguales y 74 cambian; 28 tienen el cambio en
una pregunta con fila en el TSV (es el que se busca) y **46 van al FRENO**: en 6 cambia el corte que S1-ter juzgó
correcto, en 5 la herencia juzgada correcta y en 41 una herencia que S1-ter no juzgó (una unidad puede estar en más de
una de esas tres cuentas). Por las reglas que, solas, la cambian: D 12, B 10, A 6, A con C 6, C 3, A con B 2, F 2, A con
E 1, A con B y E 1, A con C y E 1, D con E 1, G 1.

**Las 46 son todas de las 70 de la mesa; ningún cambio nuevo en una leída** fuera de ellas: las 36 que mejoran y las 7
neutras siguen; y 3 de las 27 que empeoraban quedan en un tercer estado (abajo). Los 6 cortes juzgados correctos que
cambian son los de S0-6a menos los tres de C, que vuelven a S1-ter: 4 cambian solo de clave (A los pone en un
sub-documento: `ri2_ae::2.1.5`, `ri2_ae::S14::cierre`, `nmaeef::8.2`, `nmaeef::S9`), `ri_ccna::D2A1P1::S0` pasa a la
herencia (A) y `gerc::2.3.2::intro` pasa a su tabla (F2). Las 5 herencias juzgadas correctas que cambian:
`nmaeef::8.2` (A), `cryl::4.2.2` (C), `ri_oc::3.45` (A y C), `ri2_pm::1.6` (D) y `seggar::5.3.5` (D y E); todas entre
las que la mesa juzgó mejora o neutro.

**Las 70, una por una** (`scripts/seguimiento_70_S0-6a-bis.py`; `censos/seguimiento_70_S0-6a-bis.json`; corte y
herencia contra S1-ter y contra la primera corrida):

| veredicto de la mesa | sigue (igual a la primera corrida) | vuelve a S1-ter | otro |
|---|---|---|---|
| mejora (36) | 36 | 0 | 0 |
| neutro (7) | 7 | 0 | 0 |
| empeora (27) | 0 | 23 | 4 |

Aceptación: ninguna de las 27 sigue empeorando como en la primera corrida, y las 36 que mejoran siguen mejorando (70 de
70). Las cuatro «otro»:
- `ri_dcpc::3.7.6` (G11): conserva el corte de E1-010 (la corrección buscada) y su herencia vuelve a la de S1-ter.
- `ri_oc::B.1.5` y `ri_oc::B.1::cierre` (G9): vuelven a S1-ter salvo el rótulo del Apartado B, que ahora es el impreso
  («APARTADO B: …», D, como en la primera corrida): el cambio que pide E2-098 (D6). S1-ter no juzgó su herencia.
- `ri_ii_31_12_19::6.3` (G5): ya no hereda la carátula (A ya no abre divisiones en la p. 1) y la Tabla Nº 1 vuelve a
  6.5, como en S1-ter (C ya no saca el grupo al que sigue una tabla). Su herencia sigue distinta de la de S1-ter en el
  cierre de S6: A abre divisiones en los subtítulos de las tablas de códigos de las pp. 16-21, y esas tablas salen del
  cierre de S6 (A sola da lo mismo). Ya estaba en la primera corrida (la mesa atribuyó el empeoramiento de esta unidad a
  la carátula, G5). S1-ter no juzgó su herencia. Las divisiones de esas tablas me parecen un error de A (§12): lo dejo a
  la decisión de la mesa.

**En tres corridas** (`scripts/leidas_tres_corridas_S0-6a-bis.py`; `censos/leidas_tres_corridas_S0-6a-bis.json`): de
las 286, el corte es igual en las tres en 258, igual a la primera corrida en 25 e igual a S1-ter en 3; la herencia, igual
en las tres en 192, igual a la primera en 66, igual a S1-ter en 24 y distinta de las dos en 4. Cambian contra la primera
corrida 28: 27 de las 70 (las 23 que vuelven y las 4 «otro») y `ri_oc::B.1.28` (la fila E2-098, §4).

## 6. Las 13 listas y R5-a por lista (decisión 3; `scripts/listas_r5a_S0-6a-bis.py`; `censos/listas_r5a_S0-6a-bis.json`)

Por cada lista de `LISTAS_R5A_S0_5` (43), si queda C o R5-a por lista, si es de las 13, si es de diseño (alguna de sus
unidades es de las 286 o de las filas) y si el texto de sus unidades en la E0 de S1-ter (el último ítem o sus partes y el
cierre de la madre) sigue entero en la final. Las tres que no son de diseño, solo por documento (sus ids, en
`NO_ABRIR_listas_r5a_detalle_S0-6a-bis.json`):

| documento | lista | de las 13 | de diseño | queda | texto entero (de las unidades de la lista) |
|---|---|---|---|---|---|
| apnf | 1.3.1.2 | sí | sí | C | 2 de 2 |
| cryl | 4.2.2 | sí | sí | C | 2 de 2 (el cierre pasa a la Sección 4: E2-033) |
| depaho | 3.11.5.5 | sí | sí | C | 2 de 2 |
| manori | 1.1.6.5, 1.4.1.3, 3.4.1.3 | sí | sí | C | 2 de 2 cada una |
| ri2_ae | 14.3 | sí | sí | C | 1 de 4 (A y E rehacen la estructura del Anexo III; el cierre del 14 queda igual) |
| ri_oc | B.1.28 | sí | sí | R5-a | 2 de 2 |
| ri_rml | 1.4.2 | sí | sí | R5-a | 2 de 2 |
| ri_spi | C.1.3 | sí | sí | R5-a | 1 de 2 (A deja fuera los anexos: E2-058) |
| adfsp | (1 lista) | sí | no | R5-a | 2 de 2 |
| ri_oc | (2 listas) | sí | no | R5-a | 2 de 2 cada una |
| snp_mep | 4.6.2 | no | sí | R5-a | 2 de 2 |
| tasint | 3.3.2 | no | sí | R5-a | 2 de 2 |

De las 43: 8 quedan en R5-a por lista (6 de las 13 y las dos de abajo) y 35 en C. De las 13: 7 en C y 6 en R5-a; de
esas 6, 3 no son de diseño (adfsp 1, ri_oc 2). La lista residual se declara en el código (`LISTAS_R5A_S0_6`, en
`correr_e0.py`, escrita sobre `LISTAS_R5A_S0_5` por documento) y en el FRENO, por documento.
- **snp_mep 4.6.2 y tasint 3.3.2** no son de las 13: leídas en S1-ter, con su cierre juzgado correcto con R5-a, C
  ajustada deja de sacarlo (en tasint, el párrafo que presenta las definiciones no comparte columna; en snp_mep, «Además,
  se proporciona información adicional sobre:» se mide por su segundo renglón, una viñeta). En la primera corrida C
  coincidía ahí con R5-a. Les apliqué el criterio de la decisión 3 (donde C no coincide con la página, R5-a por lista), y
  lo declaro: es una extensión del criterio a dos listas que no estaban entre las 13.
- Ninguna otra de las 43 cambia el texto de sus unidades.
- **La bolsa.** Una lista de R5-a es una corrección hecha para su documento (`docs/plan_tesis.md:782`, punto 4: se
  excluyen del sorteo). Busqué, en el código de E0 de S0-6a (`correr_e0.py` del parche de S0-6a;
  `scripts/listas_por_documento_S0-6a-bis.py`, `censos/listas_por_documento_S0-6a-bis.json`), las demás listas por
  documento en que aparecen los seis documentos con una lista que queda (fuera de las de la tanda 0 y de
  `LISTAS_R5A_S0_5`, que C reemplazaba): ri_oc está en `TOS_APARTADO_LETRA_S0_4` y `TOS_SUBDOCUMENTO_R1_S0_4` (y en
  `TOS_TITULO_BLOQUE_S0_5` y `RAICES_POR_LISTA_S0_5`, que A y E reemplazan); snp_mep, en `COLA_TITULO_ESTRICTA_R5` (la
  cola de título estricta de la regla 5 de S0, por páginas). **adfsp, ri_rml, ri_spi y tasint no están en ninguna: con
  R5-a por lista, salen de la bolsa.** Es la cuenta sobre el código; los cortes a mano y los laudos de casos los cuenta
  la mesa al sortear, con los registros de cada lectura.

**Las reglas por lista que se reemplazan** (`../scripts/reemplazos_S0-6a.py`, en cuentas:
`scripts/reemplazos_cuentas_S0-6a-bis.py`, `censos/reemplazos_cuentas_S0-6a-bis.json`): E da lo de R5-g (51 de 51
unidades) y H lo de R5-f (11 de 11), como en S0-6a; A separa el bloque de R5-a′ por sus títulos (0 de 1 con el mismo
id, como en S0-6a); y en las 43 listas de R5-a, la configuración con C (que en las 8 de la lista residual corre R5-a)
da la misma unidad que S0-5b en 172 de 191 (S0-6a: 111), y la final en 116 (en las otras actúan además otras
reglas).

## 7. Censo por regla, generalidad y bolsa (§5 del mandato; `s0_5/scripts/censo_por_regla_S0-5a.py`)

Cada regla sola contra todas apagadas (la salida de S0-5b, 768 de 768), sobre los 152, con el prototipo (`S0_6_REGLAS`).
En cuentas, por regla y por documento, en `censos/censo_por_regla_S0-6a-bis.{json,md}`
(`scripts/resumen_censo_S0-6a-bis.py`); la generalidad, en `censos/generalidad_S0-6a-bis.json`
(`scripts/generalidad_S0-6a-bis.py`). El censo entero, con ids, va en el paquete (`NO_ABRIR_censo_por_regla_S0-6a-bis.json`).

| regla | TOs con unidades que cambian | de esos, donde no se vio su error | unidades (creadas / quitadas / cambiadas) | general | salen de la bolsa |
|---|---|---|---|---|---|
| A | 57 | 48 | 886 / 183 / 528 | sí | — |
| B | 50 | 41 | 0 / 9 / 757 | sí | — |
| C | 32 | 29 | 65 / 23 / 401 | sí | — |
| D | 13 | 11 | 0 / 0 / 270 | sí | — |
| E | 6 | 4 | 98 / 65 / 23 | sí | — |
| F | 6 | 4 | 0 / 8 / 86 | sí | — |
| G | 1 | 0 | 1 / 1 / 9 | no | lingeef |
| H | 3 | 2 | 24 / 13 / 50 | sí | — |
| I | 1 | 0 | 0 / 0 / 40 | no | ri_ccna |
| J | 2 | 1 | 0 / 0 / 2 | sí | — |
| K | 1 | 0 | 0 / 0 / 6 | no | ri_ccna |
| L | 0 (sola) | — | 0 / 0 / 0 | ver abajo | — |
| M | 0 (sola) | — | 0 / 0 / 0 | ver abajo | — |

La configuración final contra todas apagadas: 115 TOs con unidades que cambian (S0-6a: 118); en esos TOs, 7.994 → 8.807
unidades; 1.057 creadas, 244 quitadas, 1.821 cambiadas (3.122 eventos: 2.099 iguales a los de una regla sola, 795 de una
regla sola con otra unidad final y 228 sin ninguna regla sola). Como en S0-6a, **G (solo lingeef), I y K (solo ri_ccna)
no son generales: lingeef y ri_ccna salen de la bolsa** de la evaluación final, y lo declaro.

**L y M solas no cambian nada**: actúan solo dentro de los sub-documentos que abre A (L, en la numeración que vuelve a
empezar después de un índice; M, en la raíz 0 de esos sub-documentos), y sin A no hay ninguno. El censo por regla sola no
mide su generalidad. Agregué, después de ver que el censo daba 0 para las dos, su efecto marginal en la configuración
final: la final contra la final sin esa regla (el prototipo con las otras doce; `scripts/efecto_marginal_S0-6a-bis.py`,
`censos/efecto_marginal_S0-6a-bis.json`). Lo declaro como una medida agregada después del censo, no fijada antes.
- **L** cambia 2 documentos: nmaeef, donde se vio su error (39 unidades creadas, 10 quitadas, 3 cambiadas), y ri2_ae (22,
  5 y 3: su Anexo IV tiene la misma estructura, índice y numeración que vuelve a empezar). **Es general; ningún
  documento sale de la bolsa por L.** La decisión 5 se cumple: E1-008 queda corregida (§4) sin romper unidades leídas
  (§5).
- **M** cambia la herencia (no el corte) de 137 unidades en 6 documentos: nmaeef 72, ri2_ae 43 (donde se vio su error),
  adfsp 9, ri_iepsp 6, ri_iesinap 6 y ri_spi 1. **Es general; ningún documento sale de la bolsa por M.** No corre donde
  los sub-documentos son de la regla de S0-4 (ri_sef, nmcief, ri_ccna, ri_icpipsp, ri_cc y ri_oc): E2-057 no cambia.
- Claves de L y M (los eventos de su efecto marginal, que el censo por regla sola no les atribuye): L, 61 creadas, 15
  quitadas y 6 cambiadas (nmaeef 39/10/3, ri2_ae 22/5/3); M, 137 cambiadas, todas de herencia. De L, las 67 creadas o
  cambiadas están entre las 3.122 declaradas de la final (§8): 60 sin ninguna regla sola y 7 con A sola, que da otra
  unidad; las 15 quitadas son claves que solo existen con A sin L (no están en S0-5b ni en la final). De M, las 137 están
  entre las declaradas: 54 sin ninguna regla sola y 83 con A sola, que da otra herencia.

**Bolsa:** por reglas que no son generales, salen lingeef (G) y ri_ccna (I y K), como en S0-6a; L y M no sacan ningún
documento. Por las listas de R5-a que quedan (decisión 3), salen adfsp, ri_rml, ri_spi y tasint (§6).

## 8. Claves (`s0_5/scripts/claves_S0-5a.py`; cuentas en `censos/censo_por_regla_S0-6a-bis.{json,md}`)

La configuración final contra todas apagadas: **3.122 claves** (1.057 creadas, 244 quitadas, 1.821 cambiadas; S0-6a:
3.825). Por la regla que, sola, da el mismo evento con la misma unidad final: A 1.497, B 740, C 457, D 252, E 94, H 87,
F 68, I 38, G 11, K 6, J 2 (una clave puede tener más de una regla); 1.023 claves sin atribución exacta (795 con una
regla sola que da otra unidad final y 228 que ninguna regla sola da: interacciones entre reglas, entre ellas las de L y
M, que solas no cambian nada, §7). Por documento y evento, en `censos/censo_por_regla_S0-6a-bis.md`. **Ninguna
clave de la tanda 0 se mueve.** La lista entera, clave por clave con su regla, va en el paquete
(`NO_ABRIR_claves_S0-6a-bis.json`).

Selftest de claves (`controles/claves_control_S0-6a-bis.json`): contra la lista declarada, **VEREDICTO OK** (1.057,
244 y 1.821, exactamente las declaradas); con la lista perturbada (una clave cambiada quitada), VEREDICTO FALLA (sobra
una). Política de claves (mandato, §6): las de las unidades que ninguna regla toca no cambian (el control lo cubre: toda
clave que cambia está declarada con su regla o como interacción); las uniones y las claves nuevas siguen la convención
de E0, como en S0-6a.

## 9. El tamaño de la herencia (decisión 4; `scripts/tamano_herencia_S0-6a-bis.py`; `censos/tamano_herencia_S0-6a-bis.json`)

La suma, sobre todas las unidades, de los caracteres de los textos de su `herencia`, en los 152 (por documento, en el
JSON):

| corrida | unidades | caracteres de herencia | por unidad |
|---|---|---|---|
| S0-5b (todas apagadas) | 9.665 | 3.895.361 | 403 |
| S0-6a (primera corrida) | 10.584 | 8.634.124 | 816 |
| S0-6a-bis | 10.478 | 5.546.286 | 529 |

Frente a la primera corrida bajan sobre todo snp_cheq (1.043.125 → 193.449), inspag (445.878 → 33.087), depaho
(387.661 → 122.009), ri_niif (901.180 → 617.851) y ri_ii_31_12_19 (237.695 → 80.961). Frente a S0-5b, 67 documentos
suben y 34 bajan. **Siete documentos llevan 1.170.676 de los 5.546.286** (S0-5b: 57.284): dmrd, ri2_cs, ri_cc,
ri_ccpnp, ri_con, ri_niif y ri_pnp, donde A abre divisiones anidadas (renglones de modelos de estados o de tablas
leídos como títulos) y 247 unidades heredan cadenas de 10 o más encabezados (hasta 196 en ri_niif; ninguna en S0-5b,
278 en la primera corrida; ninguna es de las 40 filas ni de las 286). Sin esos siete, la herencia pasa de 3.838.077 a
4.375.610. Lo cuento como un error de A (§12) y no cambié A. El efecto en el costo de E1 y en el tope de la tanda 1 lo
calcula la mesa: **NO VERIFICADO**.

## 10. Continuidad de la numeración (`s0_5/scripts/control_continuidad_numeracion.py`)

Antes, 88 saltos (16 de la clase i y 72 de la ii), igual byte a byte al JSON de S0-5b
(`s0_5/b/controles/control_continuidad_S0-5b.json`); después, **70** (21 i y 49 ii; la primera corrida, 76). Cierran 28
(ri2_ae 11, nmaeef 6, ri_laft 6, snp_dd 3, ri_cc 2) y aparecen 10, todos ya en la primera corrida: adfsp 4 (i), ri2_ae
1 (i) y ri_saofe 5 (ii); de los 16 nuevos de la primera, los 6 de nmaeef cierran (L abre la numeración del Anexo IV).
Uno de ri_cc sigue y cambia de unidad. En cuentas por documento y clase: `controles/continuidad_cuentas_S0-6a-bis.json`
(`scripts/continuidad_cuentas_S0-6a-bis.py`); la lista para la autora, con rótulos y unidades, en el paquete
(`NO_ABRIR_lista_continuidad_S0-6a-bis.md` y los dos JSON del control). Selftest del control: 14/14
(`controles/selftest_control_continuidad_S0-6a-bis.txt`).

## 11. E y los 87 rechazos (`scripts/rechazos_e_S0-6a-bis.py`; `censos/rechazos_e_S0-6a-bis.json`)

Como en S0-6a: de los 87 rechazos de raíz por la columna de la E0 de S0-5b (7 documentos), E sola abre 36 y siguen 51,
los mismos en la final (manual 22, nmaeef 11, ri_saofe 9, ri2_cs 7, ri2_ae 2). Por documento, en cuentas; rechazo por
rechazo, en el paquete (`NO_ABRIR_rechazos_e_detalle_S0-6a-bis.json`).

## 12. Unidades que no son de las 40 ni de las 286 y me parecen un error de una regla

Solo cuentas por regla y por documento (`scripts/errores_de_regla_cuentas_S0-6a-bis.py`,
`censos/errores_de_regla_cuentas_S0-6a-bis.json`); los ids, con la regla y el motivo, en
`NO_ABRIR_errores_de_regla_S0-6a-bis.json` y `NO_ABRIR_cadenas_de_encabezados_A_S0-6a-bis.json`. No cambié ninguna regla
por ellas. Las 264 existen en la E0 final y ninguna es de diseño (el script lo controla).

| regla | unidades | por documento |
|---|---|---|
| A (títulos o apartados que abren divisiones donde no van) | 10 | adfsp 1, ri_cc 1, ri_ii_31_12_19 5, ri_oc 3 |
| A (cadena de 10 o más encabezados heredados, §9) | 247 | dmrd 3, ri2_cs 8, ri_cc 28, ri_ccpnp 20, ri_con 30, ri_niif 110, ri_pnp 48 |
| E | 6 | ri_saofe 6 |
| I | 1 | ri_ccna 1 |

Frente a la lista de S0-6a: siguen las de A en ri_oc, adfsp y ri_cc, las de E en ri_saofe y la de I; las de A y E en
nmaeef (6) ya no están: L abre la numeración del Anexo IV (E1-008). Son nuevas en la lista, aunque ya estaban en la
primera corrida, las 5 de ri_ii_31_12_19 (las tablas de códigos de la Sección 6, §5) y las 247 de las cadenas.

## 13. Error propio (de S0-6a)

En el §11 del informe de S0-6a y en su FRENO, dos de las entradas de A (ri_ccna, los bloques de dos formularios)
nombran ids que **no existen en la salida final de S0-6a**: vienen de una corrida intermedia, y no los controlé contra
la final. En la final de S0-6a y en la de esta etapa, esos dos formularios son una unidad cada uno. Causa: armé la lista
con ids anotados durante el desarrollo y no la recorrí contra la salida final. Esta vez la lista se controla con un
script contra la E0 final (§12). Los ids, en `NO_ABRIR_errores_de_regla_S0-6a-bis.json`.

## 14. Tabla de reprocesamiento: la fila propuesta

`data/experiment/mantenimiento/tabla_reprocesamiento.md` está fuera de lo que puedo escribir: la fila queda propuesta,
para S0-6b, con anclas al código final (el del parche de esta etapa). Reemplaza a la F19d que propuso S0-6a; cambian las
anclas, no la descripción ni la clase.

| Fila | Cambio | Dónde entra | Qué obliga a recomputar | Clave E1 | Clave E3 | Clase | Principio | Ancla | Variación del selftest |
|---|---|---|---|---|---|---|---|---|---|
| F19d | Release de E0 (e0-r2) con reglas generales antes de una tanda, con la tanda 0 fuera por lista: reglas que crean, quitan o cambian unidades de las tandas siguientes sin cambiar la tanda 0 | E0 e0-r2 de las tandas siguientes; la de la tanda 0, byte a byte igual | en la tanda 0, nada; en las siguientes, las unidades nuevas y las que cambian texto o herencia entran a E1 y E3 por F19b y F01 a F03, cuando esa tanda se extraiga | no cambia en la tanda 0 | no cambia en la tanda 0 | ninguna en la tanda 0 | 9 (como F19b) | `correr_e0.py:207-253` (reglas, exclusión de la tanda 0, reemplazos y listas de R5-a que quedan), `:835-860`, `:1444-1448`, `:1492`, `:1518-1525`, `:1697-1718`; `e0_lib.py:228-244` (docstring), `:550-780` (las trece reglas y sus constantes), `:794-851` (L), `:2067-2073` (carátula de A), `:2273-2274` (L), `:3215-3388` (C), `:3390-3660` (A), `:4572-4589` (M) | ninguna clave de la tanda 0 se mueve (OK); la variación propia la decide S0-6b |

**Anclas que el parche corre** (`controles/anclas_e0_tabla_S0-6a-bis.txt`, `s0_5/b/scripts/anclas_e0_tabla_S0-5b.py`
con la E0 de S0-5b como «antes»): de las 27 citas de la tabla al código de E0, 12 quedan iguales, 14 se mueven (el mismo
bloque, en otro rango) y una no se encuentra entera: `correr_e0.py:140-210` de F19b (el bloque de S0-5, donde el parche
cambia `_r5` para los reemplazos). Es lo mismo que en S0-6a; S0-6b las corrige, como hizo S0-5b.

## 15. Comandos

Sobre copias, nunca sobre el repo. `<TSV>` es `errores_confirmados_S1ter.tsv` (de los extractos de S0-6a); `<mesa70>`,
`cambios_en_leidas_S0-6a_clasificados_mesa.md`; `c_<config>`, las salidas de E0 de cada configuración; `c_FINAL_S0-6a`,
la salida final de S0-6a. Las reglas `--regla a=c_a … --regla m=c_m` van completas.

```
python -B ../scripts/armar_proto_S0-6a.py <correr_e0.py final> <correr_e0.py del prototipo>
../scripts/lote_configuraciones_S0-6a.sh <copia> <raíz prototipo> <raíz final> <corridas> NINGUNA TODAS a b c d e f g h i j k l m FINAL
SUF=_2 ../scripts/lote_configuraciones_S0-6a.sh <copia> <raíz prototipo> <raíz final> <corridas> TODAS
../scripts/lote_configuraciones_S0-6a.sh <copia> <raíz prototipo> <raíz final> <corridas> a,b,c,d,e,f,g,h,i,j,k,m a,b,c,d,e,f,g,h,i,j,k,l
python -B scripts/comparar_con_manifiesto_S0-6a-bis.py c_NINGUNA s0_5/b/manifiestos/manifiesto_salida_e0_152_S0-5b.json
python -B ../scripts/comparar_archivos_S0-6a.py <dir a> <dir b>
python -B s0_5/scripts/censo_por_regla_S0-5a.py --base c_NINGUNA --final c_FINAL --regla a=c_a … --regla m=c_m --out <NO_ABRIR_censo>
python -B s0_5/scripts/claves_S0-5a.py declarar --censo <NO_ABRIR_censo> --out <NO_ABRIR_claves>
python -B s0_5/scripts/claves_S0-5a.py controlar --antes c_NINGUNA --despues c_FINAL --claves <NO_ABRIR_claves> --out <json>
python -B scripts/generalidad_S0-6a-bis.py --censo <NO_ABRIR_censo> --tsv <TSV> --out censos/generalidad_S0-6a-bis.json
python -B scripts/resumen_censo_S0-6a-bis.py --censo <NO_ABRIR_censo> --claves <NO_ABRIR_claves> --generalidad censos/generalidad_S0-6a-bis.json --out-json censos/censo_por_regla_S0-6a-bis.json --out-md censos/censo_por_regla_S0-6a-bis.md
python -B scripts/efecto_marginal_S0-6a-bis.py --final c_FINAL --sin l=c_a+b+c+d+e+f+g+h+i+j+k+m --sin m=c_a+b+c+d+e+f+g+h+i+j+k+l --tsv <TSV> --out censos/efecto_marginal_S0-6a-bis.json
python -B ../scripts/reemplazos_S0-6a.py --codigo <e0_chunking final> --base c_NINGUNA --regla c=c_c --regla a=c_a --regla e=c_e --regla h=c_h --final c_FINAL --out <NO_ABRIR_reemplazos>
python -B scripts/reemplazos_cuentas_S0-6a-bis.py --reemplazos <NO_ABRIR_reemplazos> --out censos/reemplazos_cuentas_S0-6a-bis.json
python -B scripts/listas_r5a_S0-6a-bis.py --codigo <e0_chunking final> --comun s1quater/diseno/scripts --orden s1ter/tramo_b/orden_lectura_S1ter.json --base s1ter/e0 --final c_FINAL --tsv <TSV> --out censos/listas_r5a_S0-6a-bis.json --out-detalle <NO_ABRIR_listas>
python -B scripts/rechazos_e_S0-6a-bis.py --base c_NINGUNA --regla-e c_e --final c_FINAL --out censos/rechazos_e_S0-6a-bis.json --out-detalle <NO_ABRIR_rechazos>
python -B ../scripts/control_leidas_S0-6a.py --comun s1quater/diseno/scripts --orden s1ter/tramo_b/orden_lectura_S1ter.json --base s1ter/e0 --final c_FINAL --regla a=c_a … --tsv <TSV> --out censos/control_leidas_S0-6a-bis.json --md censos/control_leidas_S0-6a-bis.md
python -B scripts/leidas_tres_corridas_S0-6a-bis.py --comun s1quater/diseno/scripts --orden s1ter/tramo_b/orden_lectura_S1ter.json --s1ter s1ter/e0 --primera c_FINAL_S0-6a --nueva c_FINAL --out censos/leidas_tres_corridas_S0-6a-bis.json
python -B scripts/seguimiento_70_S0-6a-bis.py --tabla <mesa70> --s1ter s1ter/e0 --s06a c_FINAL_S0-6a --nueva c_FINAL --out censos/seguimiento_70_S0-6a-bis.json
python -B ../scripts/negativos_leidas_S0-6a.py --comun s1quater/diseno/scripts --orden s1ter/tramo_b/orden_lectura_S1ter.json --base s1ter/e0 --final c_FINAL --regla a=c_a … --tsv <TSV> --tos <TOS_S06> --out censos/negativos_leidas_S0-6a-bis.json
python -B scripts/negativos_al_selftest_S0-6a-bis.py --negativos <json> --selftest <copia de selftest_e0.py> --tos <TOS_S06>
python -B ../scripts/filas_40_S0-6a.py s1quater/diseno/scripts s1ter/e0 c_FINAL <TSV> <json> --fichas <fichas> --md <md>
python -B scripts/listas_por_documento_S0-6a-bis.py --codigo <código de S0-6a> --tos adfsp,ri_oc,ri_rml,ri_spi,snp_mep,tasint --out censos/listas_por_documento_S0-6a-bis.json
python -B scripts/tamano_herencia_S0-6a-bis.py --salida S0-5b=c_NINGUNA --salida S0-6a=c_FINAL_S0-6a --salida S0-6a-bis=c_FINAL --out censos/tamano_herencia_S0-6a-bis.json
python -B scripts/errores_de_regla_cuentas_S0-6a-bis.py --lista <NO_ABRIR_errores> --e0 c_FINAL --leidas <ids de las 286> --tsv <TSV> --out censos/errores_de_regla_cuentas_S0-6a-bis.json
python -B s0_5/scripts/antes_y_despues_S0-5a.py --censo <NO_ABRIR_censo> --claves <NO_ABRIR_claves> --antes c_NINGUNA --despues c_FINAL --out-md <NO_ABRIR_….md> --out-jsonl <NO_ABRIR_….jsonl>
python -B s0_5/scripts/control_continuidad_numeracion.py --e0 <E0> --lineas <caché de renglones> --out <json>
python -B s0_5/scripts/lista_continuidad_S0-5a.py --antes <json> --despues <json> --out <NO_ABRIR_lista>
python -B scripts/continuidad_cuentas_S0-6a-bis.py --antes <json> --despues <json> --primera <json de S0-6a> --out controles/continuidad_cuentas_S0-6a-bis.json
python -B s0_5/scripts/selftest_control_continuidad.py --antes s1bis/e0 --despues c_FINAL --lineas <caché de renglones>
python -B ../scripts/medicion_tanda0_S0-6a.py <tanda 0 con S0_6_TANDA0=1> reextraccion_v2/e0_chunking/salida_tanda0_r2b <NO_ABRIR_medicion>
python -B s0_4/scripts/control_tanda0_en_152.py c152_1 reextraccion_v2/e0_chunking/salida_tanda0_r2b
scripts/lote_controles_S0-6a-bis.sh <trabajo> <copia con el parche> <raíz final> <python>
scripts/selftests_S0-6a-bis.sh <logs> <copia con el parche> <python> <tmp>
scripts/armar_parche_S0-6a-bis.sh <código S0-5b> <código S0-6a> <código final> <prototipo> parche <prueba>
python -B ../scripts/manifest_salida_S0-6a.py --e0 c152_1 --codigo <e0_chunking final> --tiempos … --tiempos2 … --out manifiestos/manifest_salida_e0_152_S0-6a-bis.json
python -B s0_5/b/scripts/anclas_e0_tabla_S0-5b.py mantenimiento/tabla_reprocesamiento.md <código S0-5b> <código final>
python -B scripts/foto_repo_entero_S0-6a-bis.py <repo> <foto.json>; python -B scripts/foto_repo_entero_S0-6a-bis.py --comparar <antes> <después>
```

Los scripts de `../scripts/` son los de S0-6a, sin cambios (iguales byte a byte a los del commit `d32f6db8`).
`reemplazos_S0-6a.py`, `listas_r5a_S0-6a-bis.py` y `listas_por_documento_S0-6a-bis.py` importan `correr_e0`: corren
con el `.venv` del repo.

## 16. Repo, `.pyc` y convenciones

- **Repo** (`scripts/foto_repo_entero_S0-6a-bis.py`, el repo entero sin `.git` y sin ninguna otra exclusión): foto
  antes, a las 19:07:27, 50.271 archivos. Después de escribir `s0_6/bis/`, solo cambia `s0_6/bis/` (archivos nuevos; 0
  borrados y 0 cambiados fuera de ahí); la foto de después y su comparación, en el mensaje del FRENO.
- **`.pyc`** fuera de `.venv/`: los cuento antes y después de escribir `s0_6/bis/` (2.213 en S0-5b y en S0-6a); el
  resultado, en el mensaje del FRENO. Todo corrió con `-B` y `PYTHONDONTWRITEBYTECODE=1`, sobre copias.
- **Grep de convenciones** (`s0_4/scripts/grep_convenciones.py`, sobre todos los archivos de `s0_6/bis/`,
  `controles/grep_convenciones_S0-6a-bis.txt`): control positivo 16 de 16; 0 nombres de personas, 0 términos de origen
  conversacional y 0 rutas absolutas.
- Los logs y salidas que guardo llevan `<scratchpad>` y `<home>` en lugar de las rutas de la sesión.
- No escribí en la memoria ni en `.claude/`, y no usé esperas programadas.
