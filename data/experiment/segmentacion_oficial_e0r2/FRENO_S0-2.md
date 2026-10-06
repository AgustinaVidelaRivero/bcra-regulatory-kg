# U-SEG-OFICIAL — FRENO S0-2 (06/10/2026)
Implementación en e0-r2 de las nueve reglas de S0 y el acompañamiento T, con las decisiones del despacho y de las notas al pie (hasta `0b92a06`). USD 0, sin API. Escribí solo `e0_chunking/e0_lib.py`, `correr_e0.py` y `selftest_e0.py`, `s0_2/` y este freno; nada commiteado. Detalle: `s0_2/REPORTE_S0-2.md`; salidas de los comandos en `s0_2/censos/`.

**Precondiciones** (`s0_2/censos/precondiciones_S0-2.txt`):
- a. `git log --oneline -1 -- docs/mandatos/USEG_OFICIAL_segmentacion_e0r2.md` da `0a3ac81`, el cierre de U-REEXT-T0, que sumó una nota al pie. El texto firmado (`git show e543cb2:…`) da `44cf30ca0d82…`.
- b. `git log --oneline -1 -- data/experiment/reext_t0` da `0a3ac81`. c. `pgrep -fl runner_corpus` no devuelve nada (código 1) y `git status --short` de `reextraccion_v2` y `reext_t0` sale vacío.
- d. `git diff --stat 9f6361e HEAD` de los tres archivos de E0 sale vacío. e. El parche completo da `81c3409851ba82a3…` y `f737028b1918cce0…`.

**Criterios** (`s0_2/censos/condiciones_S0-2.txt`):
- Tanda 0: 57 de 57 iguales a `salida_tanda0_r2b/`, en dos corridas. Corte de la tanda 0: `435af2fe…`, igual a `9f6361e`; `cap::4.2.1.2` da 15.056 y 11.669 con los dos códigos.
- 152 TOs: cambian 26 y 126 salen iguales byte a byte, en archivos y agregados. Cobertura exacta; 9.554 unidades. Sobre el umbral: 10 partidas, 9 declaradas por tabla, ninguna salteada. Doble corrida: 0 de 768 archivos distintos.
- Atribución: 1.430 eventos (553 ids nuevos, 384 que desaparecen, 491 chunks que cambian, 2 de orden), cada uno atribuido a una regla o a T. Hay 2 «otra», `ri_dsf::S10::parte3` y `parte4`; los leí y son interacción de las reglas 2 y 6.
- Conciliación: las corridas reproducen los dos `ids_que_cambian` (25 de 25 TOs). S0-2 difiere de S0-1 bis en 11 TOs y 41 eventos: 21 por la decisión 8 y 20 por la 5. rdbcra: 119 de 119 filas limpias.
- Selftests sobre la copia, en verde: `selftest_e0` 84/84 (27 casos nuevos), `b52` 39/39, `b581` 34/34, `b582` 59/59, `b583` 33/33. Selftest de claves con las bases: OK, con el contraste en OK y salida igual a la de `0a3ac81`; ninguna clave de la tanda 0 se mueve.

**Decisiones del despacho** (reporte §2):
- 8: la regla tal como está escrita alcanza 4 de las 6 páginas. Admití tres formas: rótulo pegado (adfsp p. 3), palabra partida y título antes del primer rótulo (nmaeef p. 2). Pasan a índice las 6 y, además, nmaeef p. 14 y ri2_ae p. 13: 178 renglones, 152 en las 6. ceninf p. 1 sigue siendo cuerpo. Límite declarado: «Sección 1.» de ri_niif está en mitad de la p. 2.
- 9: no adopté el orden por celda. En las 119 filas el número, la gravedad y las multas comparten renglón, y en 63 ese renglón lleva además un tramo de la descripción. Partirlo deja el texto fuera de los renglones del PDF y el control por renglones no puede dar limpia ninguna fila.
- 4: con 1,5051, las clases quedan A 14, B 7, C 49 y D 8; 21 unidades llegan al tercer escalón y ninguna queda sin salida. Solo por la razón, `ri2_cs::S3` pasa de B a D. `ri_cc::S3` cambia de partición pero sigue en B (precisión al despacho, que la daba como cambio de clase).
- 5: `manori::S2` y `snp_mep::S7` pasan de 4 a 5 partes; `cateloc::S2` y `ri_niif::S7` pasan a D. 7: corregí el comentario; las 12 listas se siguen detectando, 8 de sus páginas son índice y la regla veta 10 renglones, todos en manori.

**Tabla de reprocesamiento:** la fila de cada regla está en el reporte §5. Propongo, sin escribirla, una fila F19b para la unidad que agrega o retira una regla de segmentación de E0.

**Decisiones de la autora (PENDIENTES):** (1) las tres formas de la decisión 8, o la regla escrita (4 páginas); (2) la fila F19b.

**Convivencia:**
- La copia de trabajo no tiene enlaces: borré de ella los 339 enlaces absolutos al repo que trae el árbol. Lleva las bases de caché, que el selftest de claves necesita.
- Durante la unidad entraron 9 commits de otras unidades (`0a3ac81..d9d8888`) y quedaron archivos ajenos modificados sin commit, entre ellos `tabla_reprocesamiento.md`. No los toqué; el selftest leyó la tabla de `0a3ac81`.
- Foto sha256 del repo antes y después, sin exclusiones salvo el volumen de Neo4j: lo mío son los 3 archivos de `e0_chunking` y 25 nuevos (`s0_2/` y el freno); de otras unidades, 134 nuevos y 23 cambiados, ninguno en `e0_chunking/` ni en esta carpeta. `.pyc` fuera de `.venv`: 2.213 antes y después, con la misma lista.

**Errores propios:** (1) el lanzador de la atribución tenía la ruta del python sin comillas y no corrió nada; lo corregí y relancé. (2) El borrador del reporte decía «seis unidades» para la decisión 5; eran cinco.

**Paquete:** `<scratchpad>/revision_USEG_OFICIAL_FRENO_S0-2/`, con `manifest.txt`. **Grep de convenciones** (patrones de un archivo del scratchpad, sobre `s0_2/`, este freno, las líneas que agregué al código y el paquete): sin coincidencias.

FRENO. Espero el «seguí» escrito de la autora; no empiezo S1.
