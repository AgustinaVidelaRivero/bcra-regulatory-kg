# Mandato U-ALCANCE-E1 — el registro de alcance por tanda entra al mensaje de E1

**FIRMADO por la autora el 07/10/2026** (firma por mensaje de la autora; versión para firmar en `9e84741`, redactada por la mesa el
07/10/2026, noche), con sus dos decisiones al firmar. Origen: la enmienda 4 al protocolo entre
tandas, FIRMADA el 07/10/2026 (`docs/enmienda4_protocolo_entre_tandas_2026-10-04_crecimiento_del_catalogo_y_alcance.md`), §7, punto 1, y
su decisión 3 al firmar. Es la condición 11-bis del checklist (`docs/checklist_pre_escalado.md`, línea de las condiciones de la tanda 1).
USD 0, sin API.

QUÉ FALTA. El mensaje de E1 lleva la línea «Alcance de este TO» solo para los documentos que tienen entrada en la tabla de la release:
`build_user_message_r2b` llama a `linea_alcance(ROL_POR_TO_R2.get(chunk["archivo"]))` (`reextraccion_v2/e1_extractor/prompt_r2b.py:409`;
la tabla, `catalogo_unico/generados_r2/rol_por_to_r2.json`, con candado `ROL_POR_TO_R2_SHA256_ESPERADO`, `:81` y `:161`). Los documentos
nuevos de una tanda reciben su alcance en el registro de alcance por tanda (`data/experiment/catalogo_unico/registro_alcance_por_tanda.md`,
sha256 `ce402aad7c84…` al 07/10/2026; formato `registro_alcance_por_tanda/1`, lector de R2-2 en
`reresolucion_catalogo/reresolver_catalogo.py:159` y `:235`). Hoy el ensamblado lo lee y el mensaje no: R2-2 midió el mensaje igual en las
2.439 unidades de la tanda 0 y en los 13 casos del candado (fila F13c de `data/experiment/mantenimiento/tabla_reprocesamiento.md`).
En la tanda 1 (lista del ejemplo del §7 del protocolo, con ri_pgn en lugar de ri_cc), 8 documentos tienen entrada en la tabla de la
release y 12 tienen fila en el registro: 9 con alcance (ri_ccna, ri_rml, ri_gerc, ri_pgn, ri_dcpc, snp_cheq, snp_tr, manori, nmcief) y 3
con alcance declarado como inexistente (ri_oc, ceninf, cirmo3). Sin esta unidad, los 9 se extraerían sin la línea de alcance que la autora
les asignó.

LO QUE CAMBIA.
1. **Un derivado del registro, con candado.** Un script genera, desde el registro y con el lector de R2-2 (un solo intérprete del
   formato), `catalogo_unico/generados_r2/registro_alcance_r2b.json`: archivo → la misma estructura que una entrada de `rol_por_to_r2.json`
   (rol con sus miembros, o una o dos clases), solo para las filas con alcance. `prompt_r2b.py` lo lee al importarse con
   `_leer_con_candado` y su sha esperado como literal del módulo, igual que la tabla de la release.
2. **La regla de lectura.** Primero, la tabla de la release; si el documento no tiene entrada ahí, el derivado del registro; si no figura
   en ninguno, o figura «sin alcance declarado», no lleva línea, como hoy. `build_user_message_r2b` sigue siendo función pura del chunk. La
   línea sale de la misma `linea_alcance`, sin texto nuevo.
3. **El candado del mensaje.** `candado_mensaje_r2b.json` suma casos sintéticos para las ramas nuevas: una entrada de clase, una de dos
   clases, un rol reutilizado y un documento sin alcance declarado. Se recomputan `CANDADO_MENSAJE_JSON_SHA256_ESPERADO` y
   `MENSAJE_R2B_SHA256_ESPERADO` (`prompt_r2b.py:97-98`). Los valores quedan PROPUESTOS hasta la confirmación de la autora.
4. **La tabla de reprocesamiento.** La fila F13c deja de decir «hoy el mensaje no lo lee» y dice qué lee y desde cuándo. Un cambio del
   registro con documentos ya extraídos es E1 y E3 de las afectadas, como F12. No se crea fila nueva.

ETAPAS.
- **A1. Diseño e implementación, con el registro de hoy** (12 filas de la tanda 1), sobre una copia.
  - El script del derivado, la lectura en `prompt_r2b.py` y los casos sintéticos.
  - `selftest_prompt_r2b` en verde, con casos nuevos por rama, y su control negativo: el código de HEAD falla exactamente los casos nuevos.
  - Los mensajes de todas las unidades de `salida_tanda0_r2b/` iguales byte a byte.
  - `selftest_clave_cache --salida-r2b` OK, con A1r sin cambios.
  - Los dos valores del candado propuestos.
  - FRENO A1.
- **A2. Sello, cuando la lista de la tanda 1 quede fijada** (U-SEG-OFICIAL, después de S2, y la lectura del §2 de la enmienda 4 para todo
  documento nuevo de la lista sin fila).
  - Regenerar el derivado desde el registro final y fijar su sha.
  - Confirmar los dos valores del candado con la autora.
  - Medición en seco, sin API, sobre las unidades de la lista final: por documento con línea nueva, unidades, caracteres y tokens
    agregados y su costo a la tarifa de E1 de la tabla (como O2 de U-E3-LISTAS).
  - FRENO A2, final.
  - Así el código cambia una sola vez.

CRITERIOS DE ACEPTACIÓN. Cada uno con su comando y su salida:
- los mensajes de la tanda 0, iguales;
- cambian solo los mensajes de los documentos con alcance en el registro, con la lista;
- `selftest_prompt_r2b` y su control negativo;
- `selftest_clave_cache` OK;
- doble corrida del derivado, byte a byte;
- sha256 del repo antes y después de cada corrida;
- 2.213 `.pyc`;
- grep de convenciones.

ESCRITURAS: `reextraccion_v2/e1_extractor/prompt_r2b.py` (lectura del derivado, candado del derivado y los dos valores del candado del
mensaje), `candado_mensaje_r2b.json`, `selftest_prompt_r2b.py`, el script del derivado y `catalogo_unico/generados_r2/registro_alcance_r2b.json`,
la fila F13c de la tabla de reprocesamiento, `data/experiment/alcance_e1/` (se crea: frenos y mediciones) y el scratchpad.
PROHIBIDO: el prefijo de E1 y sus parches; el tool schema; `bloque_catalogo_r2.txt`; `rol_por_to_r2.json`; `catalogo_sujetos_r2.json`; el
registro de alcance (solo se lee: lo escribe la autora con la mesa); E3; el ensamblado; los grafos sellados; la API; commitear.
REQUISITOS: CLAUDE.md §4 (a a l). La corrida en seco importa `prompt_r2b` por el mismo camino que el runner (regla l, último párrafo).
CONVIVENCIA: después de la firma de la enmienda 4 (hecha). En paralelo con U-OMISIONES-COD, O5 de U-E3-LISTAS y S0-4 de U-SEG-OFICIAL,
que no tocan estos archivos. A2 espera la lista final. Todo, antes de la extracción de la tanda 1.
DECISIONES DE LA AUTORA AL FIRMAR (tomadas el 07/10/2026):
1. **El candado del derivado.** Opciones: (a) en el código, como hoy la tabla de la release; (b) en el manifiesto de cada tanda.
   **Decidido: (a).** Era la recomendación de la mesa. El derivado crece por tanda, con un cambio declarado entre tandas (F13c), y todo lo que entra al mensaje
   lleva candado en el módulo.
2. **Si A2 espera la lista final.** **Decidido: sí**, para que el código cambie una sola vez.

## Firma

FIRMADO por la autora el 07/10/2026 (versión para firmar en `9e84741`). Rige desde esta firma. A1 puede empezar ya; A2 espera la lista
final de la tanda 1 (U-SEG-OFICIAL, después de S2).

## Notas posteriores a la firma

- **08/10/2026 — FRENO A1 revisado por la mesa sobre una copia, y decisiones de la autora.**
  - **Revisión de la mesa.** Copias sin enlaces del árbol de `7788e52`; repo sin cambios fuera de `docs/` (sha256 antes y después), 2.213
    `.pyc`, USD 0. Se reproduce todo:
    - el parche `data/experiment/alcance_e1/parche_UALCANCE_E1_A1.diff`: 5 archivos, +657 −13, `git apply --check` limpio; en
      `prompt_r2b.py` las líneas 1 a 463 cambian solo en 95, 97, 98 y 409, y las 45 anclas de la tabla de reprocesamiento siguen en su línea;
    - el derivado: dos corridas iguales byte a byte, 9 entradas, sha256 `68ac5c084a17…`, desde el registro `ce402aad7c84…`;
    - la tanda 0: los mensajes de las 2.439 unidades, por el camino del runner y por un cálculo propio, 0 distintos; sha `48fdec197658…`
      con HEAD y con el parche, el de R2-2;
    - `selftest_prompt_r2b`: 55/55 con HEAD y 66/66 con el parche; el selftest nuevo con el código de HEAD da 55 ok y 11 FAIL, los 11
      nuevos;
    - `selftest_clave_cache --salida-r2b`: OK; con HEAD, el JSON es el del repo (`923dd900…`); con el parche cambian 6 líneas (dos
      inventarios y el texto de error de R29 y R29b);
    - el candado: `6b758517cee0…` y `eeb11b9a3bf6…` en dos procesos; las 13 unidades de P3c-2 siguen en `a9cb702c0d24…`;
    - la tanda 1 de ejemplo: 3.275 unidades en la partición vigente, 892 cambian, solo en la línea de alcance;
    - K2: con el derivado en `catalogo_unico/generados_r2/`, `selftest_catalogo_unico` da 59/60 (falla K2); en `catalogo_unico/`, 60/60.
  - **Decisiones de la autora (08/10/2026):**
    1. **(a) El derivado va en `catalogo_unico/registro_alcance_r2b.json`**, por la regla d de CLAUDE.md §4, que el mandato exige (mandan los archivos): en
       `generados_r2/`, la ruta de las ESCRITURAS de este mandato, falla K2. A2 lo escribe ahí.
    2. **(b) F13c, variante A** («cambia», como F12): el mensaje cambia en las unidades con alcance. A2 queda autorizada a agregar la
       variación R34 en `selftest_clave_cache.py` y a regenerar `selftest_clave_cache.json`, y a poner al día los pasajes de la tabla que
       quedan viejos: el inventario del §1 (`:73-80`), «No los abre…» (`:86-88`), la lista de F11b (`:163`) y la nota de F13 (`:253-261`).
       La revisión de la mesa encontró, por la misma causa, tres más: «R00 a R33b» y «44 variaciones» (`:361`, `:391`) y el pie (`:401`); y
       la variante A cambia la columna «Principio» de F13c de 12 a 9, como F12. Entran en la misma autorización, salvo que la autora diga
       otra cosa. Prototipo de la mesa en la copia: R34 como variación en memoria, igual que R11, con una entrada del derivado; da «cambia»
       solo en `docvig::3.3.1` y «no cambia» en E3, y el contraste da OK con 45 variaciones.
    3. **(c) El manifiesto dice lo que se le manda al modelo, y se corrige en A2.** Hoy `perfil_e1.py:236` expone `rol_por_to =
       ROL_POR_TO_R2`, y el manifiesto de la tanda 1 declararía `rol_alcance` null para los 9 documentos aunque el mensaje lleve la línea.
       Cambio, probado por la mesa en una copia: una línea en `perfil_e1.py:236`, que compone la tabla de la release con las entradas del
       derivado, la release primero; `manifiesto_corpus.py:162` y `armar_manifiesto_S1.py:55` no se tocan. No cambia ninguna clave de caché
       (el JSON de `selftest_clave_cache` queda igual al del parche) ni los manifiestos de la tanda 0; los selftests (`selftest_prompt_r2b`,
       `selftest_manifiesto`, `cablev3`, `catalogo_unico`) pasan. Costo: USD 0, una a dos horas. Requiere sumar `perfil_e1.py` (y un caso en
       el selftest) a las escrituras de A2. Lo que hay que coordinar: el manifiesto de S1 de los 152, ya sellado (`0957daf5…`,
       `segmentacion_oficial_e0r2/s1/sellos_S1.txt:32`), declara null para esos 9 y dejaría de cargar con el perfil nuevo
       (`correr_e0.py:1627`). El manifiesto de la tanda 1 se arma después de A2, con la lista final; los de S1 y S1-bis quedan como
       registro anterior a A2 o se regeneran y re-sellan en U-SEG-OFICIAL si se los vuelve a cargar (unos 30 minutos).
    4. **(d) Los dos valores del candado y el sha del derivado quedan PROPUESTOS** hasta A2, con la lista final.
    5. **(e)** La cita de la firma en las plantillas de despacho de la mesa queda corregida: `21e55a0`, no el commit de los asientos (lo
       mismo en U-UNION-ESTRECHA). Error de la mesa.
    6. **(f) El commit de A1** entra como registro (`data/experiment/alcance_e1/`), sin tocar el código del repo: el parche lo aplica A2,
       una sola vez.
- **08/10/2026 (tarde) — decisiones de la autora que amplían las escrituras de A2.**
  1. **Los pasajes de la tabla de reprocesamiento** que la revisión de la mesa encontró viejos además de los cuatro del FRENO A1 quedan
     aceptados: «R00 a R33b» y «44 variaciones» (`:361`, `:391`) y el pie (`:401`), y el cambio de la columna «Principio» de F13c de 12 a 9,
     como F12. A2 los pone al día junto con F13c (variante A), R34 y `selftest_clave_cache.json`.
  2. **`reextraccion_v2/e1_extractor/perfil_e1.py` entra en las escrituras de A2**, para la corrección del manifiesto (decisión (c) de la
     nota anterior): una línea en `:236`, que compone la tabla de la release con las entradas del derivado, la release primero, y un caso
     en el selftest. El manifiesto de la tanda 1 se arma después de A2; el de S1 de los 152, ya sellado, queda como registro anterior a A2 o
     se regenera en U-SEG-OFICIAL si se lo vuelve a cargar.
  Con esto, las ESCRITURAS de A2 son las del texto firmado, con el derivado en `catalogo_unico/registro_alcance_r2b.json` (decisión (a)),
  más `selftest_clave_cache.py`, `selftest_clave_cache.json`, los pasajes de la tabla nombrados y `perfil_e1.py` con su caso de selftest.
