# U-DIAG-VINCULO — FRENO V1 (04/10/2026, USD 0, sin commit)

1. Tarea 1, el ejemplo. En KG-Tanda0-Desarrollo-r2a (sha `93a7af72…` verificado, `f8dedd4`) no hay **ninguna** arista entre los nodos de contenido de `cla::5.1.1::intro` (1 Definicion, «Cartera comercial — alcance») y los de `cla::5.1.1.1` (2 Condicion, 1 Definicion, 1 Operacion). El único camino tiene 2 saltos y pasa por el TextoOrdenado de cla (`establecida_en`; ese nodo tiene procedencia en 143 unidades). Sin TextoOrdenado ni Sujeto, no hay camino. Además, la excepción misma (que los créditos para consumo o vivienda quedan fuera) no tiene nodo: el 5.1.1.1 trae solo la contraexcepción (los que vuelven a la cartera comercial). El crudo es `v3_b54` (`reporte_ensamblado_r2.json:144`). Salida: `salidas/tarea1_ejemplo.txt`.
2. Respuesta: **no**. Ninguna dirección viable exige cambiar el prompt ni el tool schema de E1.
   - (a) es código del ensamblado sobre lo guardado. Lo aprobado ya deja los dos extremos: con el ajuste de R8, la Condicion del ítem queda sin `condicion_de` (`UPROMPT_R2_prefijo_nuevo.md@10629b3:412-413`); R30 deja en la unidad del encabezado la norma principal y «una excepción a la lista entera» (`diseno_prefijo_r2.md@fca019d:487`, `:498`).
   - (b) es la única que lo exige: el prompt y el tool schema (hoy `target` es el «local_id de la entidad target», `tool_schema_r2.json@HEAD:538`), además del validador de E1 y de E3. No la considero viable antes del escalado.
   - (c) es otra pasada, con su propio prompt; no toca E1.
3. Condición sobre el ejemplo: en la matriz vigente ningún predicado tipado llega a una Definicion (`modelos_r2.py@HEAD:108-128`). Si el contenedor sale como Definicion, como en r2a, solo `remite_a` puede unir esos nodos (56 firmas, `5f9a731`, enmienda 2, §2). Usarla para el anuncio «las siguientes» no cambia los tipos, los predicados ni la matriz, pero amplía qué afirma `remite_a` (§1, «cita un punto»), y eso pide una enmienda. Lo detallo en V2.
4. Opcional, no exigido: R30 no nombra las listas de excepciones. Cómo tipa E1 esos ítems (Excepcion o no) decide cuánto cubre la variante tipada de (a). P4 lo muestra en `cla::5.1.1.1`, que es caso fijo; no propongo cambiar el texto.

---
Nota del 04/10/2026, posterior a la entrega de V1 (el texto de arriba no se edita). «@HEAD» en V1 es `966c2bc`,
el HEAD de ese momento. Después entró `20b7f60` (P2 de U-PROMPT-R2), que movió la descripción de `target` de
`tool_schema_r2.json:538` a `:550`, sin cambiar su texto. `modelos_r2.py:108-128` no cambió (`395fc0b`).
