# FRENO O5 de U-E3-LISTAS: casos resueltos en la NOTA del ítem, final de la unidad (07/10/2026; USD 0,241453 de 0,50; sin commit)

Mandato firmado en `d9d8888`; decisión y tope en la nota al pie del 07/10/2026 (noche), `4f738ed`; O3 en `6dde4b9`, O4 en `d007be8`. Empecé sobre HEAD `1190a8a`; la autora commiteó `53bbd6f`, `9e84741` y `0ea2d74` (tabla y docs, no el código de E3), y rehice copia, parches y selftests sobre `0ea2d74`: mismos archivos de E3, mismo candado. Copias con `git archive`, sin enlaces. Paquete: `revision_UE3_LISTAS_FRENO_O5/`, con `manifest.txt`.

**Texto propuesto** (último párrafo de la NOTA del ítem; constante `NOTA_E3_ITEM_CASOS`, `prompt_e3.py:495-510`, que `nota_item_lista` agrega; 904 caracteres):
> Casos resueltos de omisiones [meta_normativo] en un ítem (una omisión es del texto propio de la unidad; el contexto heredado se extrae en su unidad):
> - el bloque que abre la lista dice «Se requerirá la conformidad previa del BCRA para … excepto cuando … la entidad verifique que:», el ítem lleva su supuesto como Condicion y el extractor declaró [meta_normativo] texto de ese bloque, con la glosa de que se compone en los ítems: no es faltante, porque el tramo no es del texto propio del ítem; la declaración solo deja constancia de la composición, aunque el bloque enuncie la norma y su salvedad;
> - el texto propio del ítem dice «Los deudores excluidos precedentemente deberán ser clasificados y sus deudas previsionadas conforme a las disposiciones de carácter general», el extractor lo declaró [meta_normativo] y ninguna entidad lo lleva: es faltante, porque está en el texto del ítem y dice un deber.

- Tabla cláusula → regla (`o5/nota/nota_tabla_clausula_regla_o5.md`): 8 cláusulas que cubren el texto entero, con apoyos verbatim del prefijo de E1 r2b (R26 `:385` y `:387`, R28 `:3`, R19 `:323`, P3C-a3 `:324`, P3C-b1, b2 y d2) y de las NOTAS de E3. K4 (la forma de la declaración) no tiene regla: describe lo observado. Declarar texto heredado va contra R26 (`:387`): es un defecto de E1, no un faltante del ítem.
- Ejemplos de la tanda 0, fuera de las 20 y de sus listas, con citas verbatim y sin citar ni parafrasear el control. «No es faltante»: `ext::10.11.5`, de la misma forma que el residuo, que E3 no reclamó. «Sí»: `cla::6.5.5.8`, un deber del texto propio; en la tanda 0 también estaba extraído (e12), así que el ejemplo enuncia el caso sin extraer. Descarté `ext::4.3.2.3` («También se podrán…»), demasiado parecido al control. Con el residuo comparten la fórmula «requerirá la conformidad previa del BCRA».

**Candado PROPUESTO** (lo confirma la autora): la fixture queda en `079d2489…`, sin cambio (19 casos); el mensaje pasa a `e39341cef06b1c4ee223ecbb9f7c7c141cfea1165c0792973c77125be949c20b`. Lo recomputé en dos procesos desde cero, con el mismo resultado; HEAD da `66bc8656…`; un espacio en `NOTA_E3_ITEM_CASOS` o en `NOTA_E3_ITEM_LISTA` lo cambia.

**Medición en seco:**
- Cambian los 1.054 ítems con la marca, +905 caracteres cada uno; sin el párrafo, los 1.054 son el mensaje de HEAD. Quedan iguales los 1.386 no ítems, los 2.440 sin la marca, los 2.427 de v3_b54, los 1.762 de r1 y 16 de los 19 casos del candado.
- Costo agregado: unos 311.743 tokens (953.870 caracteres), USD 0,62 por corrida del tamaño de la tanda 0, o 0,70 con las 128 re-verificaciones de ítems.
- Sobre copia: `selftest_e3` da 114/114 (el check M suma la constante nueva) y `selftest_clave_cache` da OK (A3r: 1.386 presentes y 1.054 ausentes, que son los ítems; contraste OK). Los vecinos dan igual que en HEAD. F23b cambia solo sus anclas y una oración de su nota, sin fila nueva.

**Con API**: criterio sellado a las 20:50:35 (`82f2740e…`) y lectura sellada a las 20:57:08 (`933a8e50…`). 20 llamadas, todas `tool_use`, por USD 0,241453 (estimado: 0,2273); los 20 mensajes son los de la medición y, sin el párrafo, los de O3.
- (i) Por la regla se cumple: el B de O3 no persiste y ningún faltante cita el bloque declarado. **Por la lectura, no**: en `ext::3.6.4.1` aparece un B nuevo, alto y bloqueante, que pide la excepción compuesta citando el texto propio (falsa alarma contra C5b y C7).
- (ii) Se cumple: `ext::3.16.2.1` conserva su reclamo, alto y bloqueante. (iii) Se cumple: 0 bloqueantes nuevos en las otras 17.
- Además, `ext::3.6.4.2` suma un P alto y bloqueante, falsa alarma ajena a la lista: los umbrales copian «podrá superar…», pero la descripción dice «no podrá superar».
- Totales: 9 faltantes (O3: 14) y 5 bloqueantes (O3: 5); leídos, 3 son falsas alarmas y 2 fundados (O3: 2 y 3). Se aceptan 15 de 20 (O3: 16).

**Para la decisión de la autora:** el caso resuelto saca la objeción a la omisión, pero el bloqueante falso de `ext::3.6.4.1` sigue, por la frontera entre miembros y supuestos, que C7 ya resuelve y E3 no aplica. Con una sola corrida no se separa el efecto de la NOTA de la variación entre muestras, e iterar contra estas tres unidades sería ajustar el verificador a su propio control. Las dos salidas razonables: adoptar la NOTA con ese residuo declarado como límite, o no adoptarla.

**Declaraciones:**
- La app se cerró a las 20:37. Al retomar, `ps` no mostró ningún proceso de esta unidad y ninguna corrida había quedado a medias; el estado, verificado por las salidas, está en el paquete.
- Error propio: el armado del literal agregaba un salto de línea de más, y la aserción lo frenó antes de escribir.
- `cache_o5/` (20 filas, sin claves) no está en `.gitignore`; `logs/cache_usage.jsonl` tiene 20 líneas nuevas. En insumos agregué una oración en §7, ítem 4, porque la pide el despacho (el texto firmado autorizaba ahí solo las cifras de O3).

**Controles:** sha256 del repo a las 20:07, 20:41 y 21:01. Lo mío: `prompt_e3`, `selftest_e3`, la tabla, el JSON de claves, insumos, la base, el log y 36 archivos en `e3_listas/o5/`. Ajenos: los tres commits y 9 documentos sin commit de otra sesión. Los 65 `kg.json` y las 171 `.db` siguen iguales; 2.213 `.pyc`; el grep de convenciones da 0 nombres y 0 rutas.

Commit PENDIENTE de la autora: con él cierra la unidad. FRENO O5.
