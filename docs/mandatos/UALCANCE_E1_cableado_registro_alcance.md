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
