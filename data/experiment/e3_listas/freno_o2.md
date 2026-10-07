# FRENO O2 de U-E3-LISTAS (07/10/2026; USD 0, sin API; sin commit)

Mandato firmado en `d9d8888`, con la enmienda 1 (nota al pie del 06/10/2026) y la NOTA v2 (nota del 07/10/2026). O1 está en `5a97e60`, y la base fue HEAD `6e611d6` (L0 y L1 de U-LECTURA-ACEPTADAS, que no tocan esta unidad). Todo corrió primero sobre copias de `6e611d6` armadas con `git archive`, sin enlaces, con las tres bases de la caché y los diez PDF copiados. Después el repo recibió los ocho archivos, iguales byte a byte a la copia, y una reproducción desde cero dio todo igual. Paquete: `revision_UE3_LISTAS_FRENO_O2/`, con `manifest.txt`.

**Qué quedó en el repo (sin commit):**
- `comun_e3.py`: `indices_bloque_lista` (el bloque de `LINEA_ITEM` más los contiguos del mismo tipo y la misma unidad, D2) y el parámetro `bloque_de_lista` en el fuente, en las citas y en `cita_en_fuente`. Sin el parámetro, todo queda igual que hoy.
- `prompt_e3.py`: la NOTA v2, en `notas_r2` y en el fuente del mensaje, solo con la forma r2, y los dos valores del candado (PROPUESTOS). `INSTRUCCIONES`, los calibradores, el tool schema y `PREFIJO_HASH` (`21a836c7de6d`) no cambian.
- `ratchet_e3.py`: solo la línea `:283` (D1).
- `candado_mensaje_e3.json`: 19 casos de 9 unidades, los 13 de hoy más `ext::3.5.6.1`, `cap::6.8.3.1` y `pro::2.3.6.1`, cada uno con y sin la marca.
- Selftests. `selftest_e3.py`: el bloque M, con 19 casos y la NOTA del ítem entre las que frenan; el bloque N nuevo (10 checks); y el check K ajustado. `selftest_clave_cache.py` y su JSON: A3r según D5; R03 y R27 esperan el cambio en los ítems cuyo bloque tocan; R33 y R33b nuevas.
- `tabla_reprocesamiento.md`: la fila F23b (después de F24, como dice el mandato), notas a F03, F21, F23, F23b y F24, la nota de §1 sobre lo que recibe E3, las anclas corridas y §4.

**Valores del candado PROPUESTOS** (los confirma la autora):
- `CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO` = `079d2489f37c4485920e932f8cb2bfd60992ecc68bbb80ba504d04e5a5f8065b`; `MENSAJE_E3_SHA256_ESPERADO` = `66bc865645e99be13cc284f7733f22080612a1342bb2210add71cb122dd15a13`.
- Se reproducen en dos procesos y desde cero. Sobre la fixture nueva, el código de HEAD da `a18b7759…`. Un espacio de más en la NOTA o en cualquiera de sus dos partes variables, o quitar D2, cambia el sha. Con la fixture de hoy, el código nuevo da el sha viejo (`da17c22e…`): ese es el riesgo que la fixture nueva cierra.

**Criterios:**
1. **NOTA.** Es igual byte a byte al texto aprobado, en sus dos variantes. La tabla (18 cláusulas, 11 reglas) la reconstruye byte a byte: 16 cláusulas en una variante y 17 en la otra. Cada fragmento de apoyo está en su regla y en el prefijo `322c5a23e9b7`. Ninguno de los 1.054 mensajes trae un centinela de E1.
2. **Medición.** Cambian los 1.054 ítems.
   - Quedan iguales byte a byte: los 1.386 no ítems; sin la marca, las 2.440 unidades r2b, las 2.427 de v3_b54 y las 1.762 de r1; y los 13 casos viejos del candado.
   - El bloque entra al fuente en 1.015 ítems (intro 982, intersticial 22, chapeau 11). En los 39 de tipo encabezado, el fuente no cambia. D2 suma 43 fragmentos en 23 ítems, con 8.819 caracteres.
   - Total: +2.809.223 caracteres (295.839 del bloque y 2.513.384 de la NOTA), unos 918.107 tokens: unos USD 2,06 por corrida del tamaño de la tanda 0. D4 se aprobó con USD 1,76; la NOTA v2 y D2 lo suben.
3. **Selftests sobre copia.**
   - `selftest_e3`: 111/111 (101 en HEAD). `selftest_clave_cache`: OK. En A3r, las 1.386 claves de no ítems están presentes y las 1.054 ausentes son exactamente los ítems. Corren 44 variaciones, el contraste da OK en 43 filas y el JSON sale igual en tres corridas.
   - Los vecinos dan igual que en HEAD: `selftest_r2` 18/18, `selftest_r3` 116/116 y `selftest_dirigida_tanda0` 28/28.
4. **D3.** El conteo queda diseñado en `ue3_o3_d3_repite_norma.py` (criterio en su docstring; selftest sintético 5/5). No lo corrí: es de O3, sobre las 20 unidades de la lista sellada `cc6b0cd6…`.

**Contradicciones y desvíos declarados (mandan los archivos):**
- La nota del 06/10 dice que el bloque M pasa «de 13 a 18 casos»: son 19 (13 + 6), como cuenta el despacho.
- En F23b, la clave de E3 dice «frena», no «cambia en los ítems» como la pieza 4. Con ítems en la fixture, un cambio de la regla o de la NOTA frena hasta re-sellar (R33 y R33b, como R30 en F23); re-sellado, pagan E3 los afectados. A3r mide el efecto de esta unidad.
- El cambio mueve también F03 (R03: la clave de E3 de 3 ítems de la muestra) y F21 (R27: de 2). Las celdas de E3 pasan a «cambia (solo los ítems…)»; el despacho no las listaba.
- Corrí además las anclas de F04b, F05, F14 y §1; las de §1 ya estaban desactualizadas antes de esta unidad. §4 decía «las 41 variaciones», pero el JSON de `0a3ac81` tiene 42; ahora son 44.
- El check K comparaba el mensaje entero de `pro::2.7.1`, que es un ítem. Ahora compara las NOTAS (la de los flags sigue igual; con la marca se suma la del ítem) y el resto del mensaje. Son ocho archivos y no «los cuatro, la fixture y la tabla»: también `selftest_clave_cache.py` y su JSON, que pide D5.

**Controles.**
- Tomé el sha256 del repo a las 00:39 y a la 01:05. Cambian mis ocho archivos y, ajenos, `docs/insumos_escritura.md` (§7, punto 5, de L2 de U-LECTURA-ACEPTADAS) y 4 archivos nuevos en `lectura_aceptadas/`. Después se suma este freno.
- 2.213 `.pyc`. Grep de convenciones vacío. C1 de U-COMP-E1 corre desde su propia copia y no importa nada del repo.

Commit PENDIENTE de la autora. FRENO: la autora confirma los valores del candado y despacha O3.
