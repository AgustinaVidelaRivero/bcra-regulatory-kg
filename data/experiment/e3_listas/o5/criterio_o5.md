# U-E3-LISTAS, O5: criterio de la re-verificación con los casos resueltos (sellado antes de la primera llamada)

Decisión de la autora del 07/10/2026 (noche), nota al pie del mandato en `4f738ed`: el residuo de O3 se cierra con un caso
resuelto en la NOTA del ítem; `ext::3.16.2.1` es el control del otro lado de la frontera; tope USD 0,50.

**Población.** Las 20 unidades de la lista sellada de O1 (`lista_unidades_afectadas_tanda0.json`, sha256 `cc6b0cd6…`), las
mismas de O3.

**Entrada.** La validación del intento 0 de E1 de la tanda 0 (`extracciones_e1.jsonl`), la que vio E3. El código de E3 sale
de una copia de HEAD `0ea2d74` con el cambio de O5 (`NOTA_E3_ITEM_CASOS` al final de la NOTA del ítem; nada más cambia en
el código de E3). Modelo y precios de E3 de la tanda 0 (`runner_corpus.py`, `MODEL_E3` y `P_E3`). Base propia
`data/experiment/e3_listas/cache_o5/e3_listas_o5.db`. Primera verificación sin ratchet: el veredicto se evalúa con
`ratchet_e3.evaluar_veredicto`, sin reintento. Una sola corrida por unidad (N = 1).

**Mensajes.** Antes de toda llamada, cada mensaje es el de la medición en seco de O5 y, sin el párrafo nuevo, el de O3
(control del runner; la corrida en seco dio 20 de 20 en los dos).

**Contra qué se compara.** O3: `o3/a/evaluacion_e3_o3.jsonl`, `o3/a/respuestas_e3_o3.jsonl`, `o3/a/hoja_de_lectura.json` y la
lectura sellada `o3/a/lectura_o3.json`, con la adjudicación de la autora de `ext::3.16.2.1` (reclamo B fundado, `4f738ed`).

**Lectura.** Antes de computar, leo todos los faltantes nuevos de las 20 unidades y les asigno la categoría del diagnóstico
(P, C, B, B2, M, E, O), con las definiciones de O3. Es B el faltante que pide en el ítem la norma del encabezado o reclama
que el texto del bloque que abre la lista, declarado `[meta_normativo]`, debía extraerse en el ítem; en `ext::3.16.2.1`, es B
el reclamo sobre la facultad del texto propio declarada `[meta_normativo]` (el que la autora adjudicó fundado). La lectura se
vuelca en `a/lectura_o5.json` y se sella (hora y sha256) antes de correr las cifras.

**Mismo reclamo (la regla de O3).** Misma categoría por la lectura, y citas que comparten al menos una ventana de 5 tokens
normalizados (`validador_r2.norm_tokens`) o una contiene a la otra (`comun_e3.normalizar_para_cita`).

**(i) El residuo desaparece.** En `ext::3.6.4.1` y en `ext::3.6.4.2`, ningún faltante nuevo es el mismo reclamo que el B que
persistía en O3. Se cumple si no persiste en ninguna de las dos. Se informan aparte los faltantes nuevos que citan el bloque
que abre la lista con otra categoría (por ejemplo, un control de lo compuesto).

**(ii) El control sigue.** En `ext::3.16.2.1`, algún faltante nuevo es el mismo reclamo que el B de O3 (cita con ventana
compartida con «la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se
excede tal monto»). Se informa además su severidad y si bloquea, frente a O3 (alta, bloqueante): si baja o deja de bloquear,
se informa como un corrimiento parcial de la frontera, aunque (ii) se cumpla. Si (ii) no se cumple, freno sin proponer los
valores del candado y sin escribir el código en el repo.

**(iii) Nada bloqueante nuevo en las otras 17.** Ningún faltante bloqueante nuevo (el `bloqueante` de la evaluación del
ratchet) sin un faltante bloqueante de O3 en la misma unidad cuya cita comparta una ventana de 5 tokens o la contenga, de
cualquier categoría. Los que coinciden con un faltante de O3 que no bloqueaba cuentan como nuevos bloqueantes y se informan
aparte. Se cumple si la cuenta es 0.

**Informe por unidad contra O3.** Faltantes, bloqueantes y camino del ratchet (aceptada, reintento, cola por veredicto
inutilizable); de los reclamos de O3, cuáles persisten, cuáles desaparecen y cuáles son nuevos, por la regla y por la lectura.

**Límite.** N = 1 por unidad: una diferencia con O3 puede ser variación entre muestras y no efecto de la NOTA (la misma
unidad varía entre corridas del mismo modelo, U-COMP-E1 C1). No se corre una segunda vez: no lo pide el despacho.
