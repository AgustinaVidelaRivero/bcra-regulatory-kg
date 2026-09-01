# Adjudicación de la autora — U-ESQ-2-cal (control del instrumento de descubrimiento)

**Unidad:** U-ESQ-2-cal · **Fecha de adjudicación:** 31/08/2026 · **Adjudica:** la autora,
fila por fila. **Regla aplicada:** pre-registro `bca863f` §4 — una detección VALE si el
reporte identifica la materia de la cláusula plantada; **ante la duda, NO cuenta**; cruces
aparte; en C es espuria toda detección que señale como fuera-de-esquema contenido que el
esquema sí captura. **Interpretación declarada por mesa ANTES de adjudicar:** en C, la
duda cuenta como ESPURIA (el sesgo apunta contra el resultado que revive el censo, en
ambos brazos).

Material adjudicado: `tabla_adjudicacion_descubrimiento_cal.md` (outputs verbatim de las
20 unidades + concepto plantado esperado en las dopadas). Corrida sellada:
`descubrimiento_cal.jsonl`, USD 0,129671, modelo resuelto `claude-haiku-4-5-20251001` en
las 20 llamadas.

## Las 20 marcas (verbatim de la autora)

### Dopadas (1–10) — ¿encontró la trampa?

| # | unidad | marca | por qué |
|---|---|---|---|
| 1 | dop::tipo::cap::8.3.2.4 | VALE | cita la multa y la explica como consecuencia sancionatoria; pide tipo de entidad para Sanciones |
| 2 | dop::predicado::cap::2.5.5 | VALE | cita "se considerarán equivalentes" y nombra la falta de predicado Operacion→Operacion |
| 3 | dop::tipo::cla::6.5.2.1 | VALE | cita "se presumirá, sin admitir prueba en contrario" y la llama presunción legal |
| 4 | dop::predicado::cla::6.5.3.3 | VALE | cita "complementará… sin sustituirla" y pide predicado de complementariedad |
| 5 | dop::tipo::ext::3.17.3.5 | VALE | cita "se entiende por 'valor de referencia ajustado'" y la llama precisión de significado |
| 6 | dop::predicado::ext::6.5.2 | VALE | cita "quedan asimiladas a" y nombra la falta de predicado de asimilación |
| 7 | dop::tipo::pro::1.1.1 | NO VALE | cero hallazgos: detección imposible |
| 8 | dop::predicado::pro::3.2.3.6 | VALE | cita "acreditará el cumplimiento de la obligación" y la llama relación causal-evidentiva |
| 9 | dop::tipo::ric::8.1.2 | VALE | cita "queda facultada para adecuar" y pide tipo para facultades/potestades |
| 10 | dop::predicado::ric::10.1.1 | VALE | cita "se computará conjuntamente con" y pide predicado de agregación |

Sin cruces: en las cinco de tipo el hallazgo encuadra como tipo faltante y en las cinco
de predicado como predicado faltante. Ninguna me quedó en duda.

### Limpias (11–20) — ¿inventó problemas?

| # | unidad | marca | cuál |
|---|---|---|---|
| 11 | cap::1.4.2.1 | ESPURIA | H1 plazo de regularización (es property), H2 límite condicionado (limite_cualitativo), H4 prohibiciones con salvedad (Restriccion + Excepcion), H5 prohibición de dividendos (Restriccion). H3 (potestad SEFYC de designar veedor) no es espuria |
| 12 | cap::5.2.1.3 | ESPURIA | H1 "no deberá existir correlación" y H2 "no son admisibles": ambas son Restriccion cualitativa |
| 13 | cla::2.2.1.7 | SIN ESPURIAS | cero hallazgos |
| 14 | cla::4.4 | ESPURIA | "no corresponderá la evaluación" es una Excepcion con exceptua_obligacion |
| 15 | ext::7.6.2::cierre | SIN ESPURIAS | cero hallazgos |
| 16 | ext::7.5.7::intro | SIN ESPURIAS | "podrá extender el plazo" es una facultad — misma familia que plantaste en la fila 9, o sea descubrimiento verdadero |
| 17 | pro::2.3.11 | ESPURIA | H1 "la denominación deberá ajustarse" es Obligacion tipo=otra. H2 (permiso adicional) no es espuria |
| 18 | pro::2.4::cierre | ESPURIA (+ malformada) | deberes de evitar prácticas en publicidad: Obligacion/Restriccion cualitativa. Ver nota abajo |
| 19 | ric::11.1::intro | ESPURIA | H1 "se incluirán" (Obligacion presentacion_informativa), H2 exclusiones (Excepcion), H3 frecuencia trimestral (property), H5 remisión de plazos (referencia). H4 (códigos de consolidación) no es espuria |
| 20 | ric::8.1.4 | ESPURIA | frecuencia mensual + deber de informar: Obligacion presentacion_informativa con frecuencia |

*(Nota de transcripción de mesa: en la fila 11 la autora escribió «SEFyC»; el resto,
verbatim sin edición.)*

## Cómputo contra P-cal (pre-registro `bca863f` §4)

| condición | umbral | observado | veredicto |
|---|---|---|---|
| A′ total | ≥7/10 | **9/10** | pasa |
| A′ mitad tipo | ≥3/5 | **4/5** (falla solo la vigencia diferida, cero hallazgos) | pasa |
| A′ mitad predicado | ≥3/5 | **5/5** | pasa |
| Cruces | se reportan aparte | **0** | — |
| C (limpias con espurias) | ≤1/10 | **7/10** (filas 11, 12, 14, 17, 18, 19, 20) | **NO pasa** |

**P-cal FALSADA por su segunda mitad («no inventa sobre las limpias»).**

## Declaración de la rama (árbol sellado, pre-registro §6)

**RAMA (b): ESQ-2 protocolizada es la única vía. El censo por LLM queda CERRADO con este
modelo** — final de un solo tiro, sin retoque, como estaba escrito antes de correr.

## Notas de lectura

**(i) Capacidad sí / precisión no.** El mismo modelo que deformó las 10 cláusulas al
extraer (escalera P1/P1′/P1″) las ve y las nombra cuando descubrir es la única tarea:
9/10 sobre lo plantado, con la cita textual y la explicación correcta del desajuste. Pero
inunda de falsos positivos el texto limpio: 7/10 limpias con al menos una detección de
contenido que el esquema sí captura (properties, Restricciones cualitativas, Excepciones,
Obligaciones informativas). **Un censo corrido con este instrumento habría sobrecontado
la deriva** — el brazo C existía exactamente para esto, y esta vez fue el que atrapó.

**(ii) Hallazgos genuinos en limpias — el hueco de potestades existe en el corpus real.**
Entre los falsos positivos aparecieron detecciones verdaderas sobre texto de producción:
facultades discrecionales REALES de la SEFyC (fila 11-H3, veedor; fila 16, extensión de
plazo), un permiso adicional (fila 17-H2) y los códigos de consolidación (fila 19-H4).
La categoría «facultad/potestad» que se plantó como hipótesis en la dopada 9 **está en el
corpus real**: pasa de hipótesis plantada a hallazgo en producción → insumo directo de
C1.7 y de ESQ-3.

**Nota de la malformada (fila 18):** `pro::2.4::cierre` devolvió los hallazgos con doble
serialización (JSON dentro de string); se adjudicó desde el crudo verbatim persistido en
la tabla — desvío declarado del instrumento, no invalida la fila.
