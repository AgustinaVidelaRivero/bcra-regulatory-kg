**VERIF-UNION-OPERACIONES, FRENO** (04/10/2026). USD 0, solo lectura, sin commit, sin Neo4j. Anexos: `anexo_t2_uniones_VERIF_UNION_OPS.md` (sha256 `994427a1…`) y `anexo_t3_pares_VERIF_UNION_OPS.md` (`52894b83…`); manifiesto en este paquete.
- **Base:** KG-Tanda0-Desarrollo-r2a, `…/ens_desarrollo_r2a/r2/kg.json`, sha256 `93a7af72…07e8dd`, igual en `f8dedd4`, en HEAD y en disco (`controles_git_VERIF_UNION_OPS.txt`). Clave: `e2_lib.py:118-121` (Operacion por etiqueta normalizada), vía `entity_slug_r2` (`:839-860`). El nodo guarda la etiqueta y las propiedades de la primera unidad (`:993`); las demás van a conflictos (`:903-924`). `e2_lib.py` no cambió entre `f8dedd4` y HEAD.
- **Cifras:** `verif_union_ops.py` (salida en el paquete); las calificaciones las cuenta `anexos_union_ops.py`. Reconstruí las 1.613 instancias desde el crudo validado (`salida_dirigida/<to>/finales.jsonl`; la cola, de `extracciones_e1_compact.jsonl`; selección de `runner_corpus.py@f8dedd4:903-943`). Cada procedencia tiene su instancia y no sobra ninguna.

**1. Por documento** (instancias / nodos = etiquetas distintas / nodos con más de un punto): pro 55/55/0; cla 88/84/3; ric 109/109/0; cap 478/473/5; ext 883/834/29; total 1.613/1.555/37.
- Etiquetas distintas = nodos por construcción. En crudo son 1.561: 5 nodos juntan variantes de mayúsculas o guiones. Un nodo de cap lleva `__cap` por colisión con ric (`adjudicacion_cross_to.json`).
- **Contradicción con el mandato:** 37 son nodos, no uniones. De las 58 uniones, 52 son entre puntos distintos y caen en esos 37 nodos. Las otras 6 son del mismo `punto`, en 5 nodos de ext donde la procedencia por herencia de encabezado lleva el punto del encabezado. Contados por unidad (`chunk_id`), son 42 nodos.

**2. Uniones de más** (`anexo_t2_uniones_VERIF_UNION_OPS.md`, criterio declarado ahí): de 37, correctas 18, incorrectas 8, dudosas 11. Por TO (c/i/d): cla 3/0/0, cap 4/1/0, ext 11/7/11.
- Incorrectas: una etiqueta genérica junta actos con objeto distinto. Ejemplos: acceso para pagar deudas financieras y servicios (01); liquidación de tres fondos distintos (24); certificaciones para financiaciones de exportación y de importación (15).
- Dudosas: 6 por régimen, modalidad o fecha que el TO separa; 4 porque la etiqueta nombra un medio común (canje, débito en cuenta) de pagos distintos; 1 que junta una regla general con un caso particular.
- Efecto lateral: queda la descripción de la primera unidad. En la 08 dice «grupo 1», aunque el nodo también lleva la procedencia del grupo 2 (cap::2.11.2).

**3. Uniones de menos** (`anexo_t3_pares_VERIF_UNION_OPS.md`)
- **Regla:** mismo TO y nodos distintos; las palabras significativas compartidas son mayoría estricta de cada etiqueta (sin 35 palabras vacías, con el plural plegado). Da 2.852 pares (pro 6, cla 25, ric 77, cap 283, ext 2.461), lista completa en `t3_pares_todos_VERIF_UNION_OPS.json`. 97 tienen el mismo conjunto de palabras.
- **Muestra:** 20 pares, `random.Random(20261004)`. Mismo acto: sí 3, no 12, dudoso 5 (4 regla general con caso particular, 1 por régimen). Ninguno de los 20 está entre los 97.
- **Partidos vistos en la lectura:** ext::7.1.1.1 quedó en otro nodo («…de divisas en mercado de cambios», unido a 3.5.1) y no con 7.1.1.2 y 7.1.1.4 (uniones 22 y 23 del anexo t2). Entre los 97 hay, por ejemplo, «Emisión de certificación de aplicación» / «…certificaciones…» y «Emisión certificaciones de aplicación de divisas» / «Emisión de certificaciones…». Esos 97 no los leí: NO MEDIDO.

**4. Ejemplo** (salida, bloque [t4])
- La unidad del párrafo sin numerar es `cla::5.1.1::intro` (mini_chunk). No tiene Operacion ni en el grafo ni en el crudo: da solo la Definicion «Cartera comercial — alcance».
- cla::5.1.1.1 tiene una: «Clasificación de crédito en cartera comercial» (tipo `clasificacion_de_cartera`; «inclusión de créditos para consumo o vivienda en la cartera comercial»).
- Según el texto, el párrafo y 5.1.1.1 regulan el mismo acto, el encuadre en la cartera comercial (regla y excepción). En el grafo no hay dos Operacion que unir, y la regla de la tarea 3 no forma ningún par con esa Operacion.

**5. Juicio**
La regla no funciona como unión de actos. Acierta en 18 de 37, pero con una etiqueta genérica junta actos distintos (8 incorrectas y 11 dudosas, todas en ext). Además, deja partido el mismo acto si el modelo cambia una palabra o un plural (3 de 20 en la muestra).
Alternativa sin modelo, NO MEDIDA: etiqueta plegada (sin palabras vacías, con el plural plegado) más un ancla en la estructura. Unir dentro del mismo encabezado ancestro de E0; entre encabezados distintos, solo si una unidad remite a la otra o las dos remiten al mismo punto (así son las correctas 17, 27, 30 y 32). Lo demás va a revisión.

**Cierre**
- Durante la sesión entraron `4aa92c7` y `8d01b04`, ajenos a esta unidad. No tocan `e2_reduce`, `tanda0/code`, `corpus_tanda0` ni `e0_chunking`.
- `git status --short` y sha256 del repo contra el inicio: ningún cambio mío. Cambiaron 5 archivos de `docs/` y aparecieron 3: `docs/enmienda2_…catalogo.md`, `docs/mandatos/URERESOL_CAT_…md` y `prompt_r2/p3b/lazo_e3_p3b.py`. Los scripts de esta unidad solo escriben en el scratchpad.
- Error propio, corregido antes del freno: la primera corrida dio una procedencia sin instancia porque mi script cortaba el id en su primer `__`. Un id truncado a 80 caracteres también lleva `__`. Ahora quita solo el sufijo `__<to>` final.
- `.pyc`: 11.236 entradas (con `.venv`) al inicio y al cierre, iguales. Grep de convenciones y manifiesto en el paquete.
