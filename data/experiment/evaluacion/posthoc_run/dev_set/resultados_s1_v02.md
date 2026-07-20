# B4.3 ronda 1/3 — Iteración de S1 contra el dev (s1-v0.2-dev) — extracción SIN scoring

Fecha: 2026-07-17. **Iteración LEGÍTIMA por diseño §4** (el dev existe para esto).
Cambios: SOLO S1_PROMPT, esquema de salida y ensamblado del input — **el fetch
determinístico quedó INTACTO** (idéntico al commiteado de B4.2; git diff del módulo
muestra solo la sección de juicio). Archivos tocados: s1_fuentes.py + su test. Sin
commits. **PROHIBIDO comparar contra `casos_dev_v7.md`** — extracción sin scoring.

## Qué cambió (s1-v0.1 → s1-v0.2-dev)

1. **SÍNTOMA EN EL INPUT:** cada llamada presenta las marcas del juez
   (claims reprobados con veredicto y centralidad + patas no cubiertas, vía
   `_sintoma_de_trace`) — lo que el verificador vio y S1 hasta v0.1 no.
2. **SÍNTOMA EN LA SALIDA:** el esquema del gatillo por causas exige `sintoma_del_par`
   ∈ {context_recall, noise_sensitivity, faithfulness} DERIVADO de las marcas
   presentadas (pata no cubierta → context_recall; claim falso → noise_sensitivity;
   no_soportado → faithfulness), no de la emisión original. El voto propio y las
   correcciones pasan a ser por PAR (síntoma, causa); la corrección reescribe
   sintoma_capa1 Y causa_capa2 (emisión preservada en capa_s1).
3. **RAMA DE COMPLETITUD para el gatillo de exoneración:** prompt propio
   (S1_PROMPT_EXONERACION) que presenta la pata no cubierta + la respuesta del agente
   (trace.final_json) + el contenido del portador citado + los pasajes fuente del fetch —
   **el GT del eval set está PROHIBIDO como input y NO viaja**. Esquema:
   `respuesta_en_fuente` (quote verbatim o null) / `presente_en_grafo` ∈
   {si, no, no_determinable} / `causa_confirmada_o_corregida`. Una corrección de
   exoneración fija sintoma_capa1=context_recall (la rama se define por la pata).

## pytest (verde completo: 83 = 77 previos + 6 de B4.3)

```
...........                                                              [100%]
83 passed in 7.51s
```

## RE-CORRIDA sobre el dev (N=1 → `_s1c.json`; `_s1.json` y `_s1b.json` congeladas)

### Agregado comparativo v0.1b → v0.2

| Caso | juzgadas | corregidas | no_det | usage (in/out) | voto_s1 v0.1b → v0.2 |
|---|---|---|---|---|---|
| run_2/CQ-021 | 0 → 0 (fetch 6 fallidos, sin cambio — fetch intacto) | 0 | 0 | 0/0 | sin cambios |
| run_4/CQ-008 | 2 → 2 | 0 | 1 → 1 | 7.285/1.048 | sin cambios (confirmación con par completo) |
| run_4/CQ-021 | 3 → 3 | 0 → **3** | 0 | 11.024/417 | [] → [] (ver hecho de jerarquía abajo) |
| run_4/CQ-028 | 3 → 3 | 2 → 2 | 1 → 1 | 11.834/1.969 | **DIVIDIDO → mayoría 2-1 {noise_sensitivity, contenido_kg}** |
| **TOTAL** | 8 | **5** | 2 | **30.143/3.434** | — |

### Los dos focos pedidos

**a. Los pares completos de CQ-028.** Con el síntoma a la vista, las 2 reps que corrigen
emiten el MISMO par completo: **(noise_sensitivity, contenido_kg)** con `coinciden=no` y
`sintoma_del_par=noise_sensitivity` derivado del claim central falso presentado. El voto_s1
que en v0.1b quedaba DIVIDIDO (1×completitud · 1×(context_recall, contenido) ·
1×(faithfulness, contenido)) ahora da **mayoría 2-1 sobre el par completo**; la tercera rep
sale `no_determinable` → triage (la política conservadora la retiene).

**b. La rama de completitud en r4/CQ-021.** Las 3 exoneraciones gatilladas salen
**corregidas sin_defecto → completitud_kg** con `presente_en_grafo=no` y
`respuesta_en_fuente` citando VERBATIM la cláusula optativa del 3.4.2 ("Las entidades
financieras deberán comunicar a los deudores los cambios negativos en la clasificación…
siendo optativo cuando el saldo de deuda sea inferior…") — el pasaje del portador del fetch
contiene la respuesta de la pata y el contenido del grafo presentado no. **HECHO de
mecánica del voto:** el voto_s1 del caso sigue vacío ([]) porque las atribuciones
corregidas tienen jerarquía `sin_par`/no-primaria — el recomputo del protocolo solo cuenta
pares PRIMARIOS. La corrección quedó anotada por atribución (capa_s1 + causa_capa2
reescrita) pero no mueve el voto: decisión de diseño a resolver en las rondas siguientes o
en la lectura de B4 (¿jerarquía de una exoneración corregida?) — se reporta, no se decide.

- **10/10 llamadas con JSON válido en las 2 corridas de hoy** (v0.2: 8 llamadas, 0
  errores de formato, 0 reintentos).
- CQ-008: rep1 confirma el par (context_recall, completitud_kg) con coinciden=no; rep2
  vuelve a salir no_determinable (mismo comportamiento que v0.1b).


---

# run_2/CQ-021

- resumen_s1 (v0.2): {"gatilladas": 6, "juzgadas_llm": 0, "corregidas": 0, "no_determinable": 0, "fetch_fallido": 6, "tokens_in_s1": 0, "tokens_out_s1": 0, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable'] · flags=['S1: rep1_atrib1 — fetch sin_portador_extraible', 'S1: rep1_atrib2 — fetch sin_portador_extraible', 'S1: rep2_atrib1 — fetch localizacion_fallida', 'S1: rep2_atrib2 — fetch sin_portador_extraible', 'S1: rep3_atrib1 — fetch localizacion_fallida', 'S1: rep3_atrib2 — fetch sin_portador_extraible']
- **voto_capa_d:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]
- **voto_s1 v0.1b (referencia congelada):** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]
- **voto_s1 v0.2:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]

## Atribuciones juzgadas — salidas ÍNTEGRAS


---

# run_4/CQ-008

- resumen_s1 (v0.2): {"gatilladas": 3, "juzgadas_llm": 2, "corregidas": 0, "no_determinable": 1, "fetch_fallido": 1, "tokens_in_s1": 7285, "tokens_out_s1": 1048, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable'] · flags=['S1: rep2_atrib1 — no_determinable (0/1 decididas)', 'S1: rep3_atrib1 — fetch sin_portador_extraible']
- **voto_capa_d:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg']]
- **voto_s1 v0.1b (referencia congelada):** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg']]
- **voto_s1 v0.2:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg']]

## Atribuciones juzgadas — salidas ÍNTEGRAS

### rep1_atrib1 — esquema `causa` · emisión (context_recall, completitud_kg) · jerarquía primaria

```json
{
 "alcance_declarado_en_fuente": "8.1. Informaciones a suministrar. A solicitud de cada cliente, dentro de los 10 días corridos del pedido, la entidad financiera deberá comunicarle la última clasificación que le ha asignado, junto con los fundamentos que la justifican según la evaluación realizada por la entidad, el importe total de deudas con el sistema financiero y las clasificaciones asignadas que surjan de la última información disponible en la 'Central de deudores del sistema financiero'.",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "no",
 "sintoma_del_par": "context_recall",
 "causa_confirmada_o_corregida": "completitud_kg",
 "justificacion_breve": "La fuente pregunta por el plazo de 10 días corridos de la Sección 8.1 (comunicación de la última clasificación a solicitud del cliente), mientras que el único nodo cercano trata el plazo de 45 días del punto 3.4.2 (comunicación de cambios negativos en la clasificación): son alcances distintos. Como no existe nodo que cubra la Sección 8.1 y el material fuente confirma que esa disposición existe en la normativa pero no en el grafo, la falta es de completitud_kg."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "causa", "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "context_recall", "causa_ganadora": "completitud_kg", "votos_ganadores": 1}
- corrigio=False · par_post_s1=['context_recall', 'completitud_kg'] · usage=[{"input_tokens": 3863, "output_tokens": 504}]

### rep2_atrib1 — esquema `causa` · emisión (context_recall, completitud_kg) · jerarquía primaria

```json
{
 "alcance_declarado_en_fuente": "1.2. Criterios especiales de imputación. 1.2.1. Créditos incorporados por cesión sin responsabilidad.",
 "alcance_en_el_nodo": "Legajo que debe llevar la entidad para cada deudor de su cartera, conteniendo todos los elementos de juicio para realizar evaluaciones y clasificaciones, dejando constancia de las revisiones efectuadas y la clasificación asignada.",
 "coinciden": "no_determinable",
 "sintoma_del_par": "context_recall",
 "causa_confirmada_o_corregida": "completitud_kg",
 "justificacion_breve": "Los pasajes fuente recuperados desde la provenance del portador (Sección 1.2, imputación de créditos por cesión y concurso preventivo) no contienen NADA sobre el plazo de comunicación al cliente de la última clasificación a su pedido; el nodo legajo_del_cliente sólo describe el contenido del legajo, sin mencionar plazos de comunicación a solicitud del cliente. La disposición citada en la atribución (Punto 3.4.2, 45 días para cambios negativos) NO aparece en ningún pasaje entregado, por lo que no puedo transcribir verbatim un alcance que cubra la pata reclamada; la ausencia total de la información sobre comunicación a pedido en el material entregado es consistente con completitud_kg (falta el nodo/contenido específico), pero el material fuente disponible no permite verificar el alcance, de ahí no_determinable."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "causa", "decididas": 0, "no_decididas": 1, "resultado": "no_determinable", "sintoma_ganador": null, "causa_ganadora": null, "votos_ganadores": null}
- corrigio=False · par_post_s1=None · usage=[{"input_tokens": 3422, "output_tokens": 544}]


---

# run_4/CQ-021

- resumen_s1 (v0.2): {"gatilladas": 3, "juzgadas_llm": 3, "corregidas": 3, "no_determinable": 0, "fetch_fallido": 0, "tokens_in_s1": 11024, "tokens_out_s1": 417, "exoneracion_con_sintoma": true}
- triage_s1: triage=False · motivos=[] · flags=[]
- **voto_capa_d:** mayoria · dividido=False · ganadores=[] (3) · conteo=3×[]
- **voto_s1 v0.1b (referencia congelada):** mayoria · dividido=False · ganadores=[] (3) · conteo=3×[]
- **voto_s1 v0.2:** mayoria · dividido=False · ganadores=[] (3) · conteo=3×[]

## Atribuciones juzgadas — salidas ÍNTEGRAS

### rep1_atrib1 — esquema `exoneracion` · emisión (noise_sensitivity, sin_defecto) · jerarquía sin_par

```json
{
 "respuesta_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al monto establecido en el punto 2. \"D",
 "presente_en_grafo": "no",
 "causa_confirmada_o_corregida": "completitud_kg"
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "exoneracion", "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": null, "causa_ganadora": "completitud_kg", "votos_ganadores": 1}
- corrigio=True · par_post_s1=['context_recall', 'completitud_kg'] · usage=[{"input_tokens": 3632, "output_tokens": 139}]

### rep2_atrib1 — esquema `exoneracion` · emisión (noise_sensitivity, sin_defecto) · jerarquía sin_par

```json
{
 "respuesta_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          monto establecido en el punto 2. “D",
 "presente_en_grafo": "no",
 "causa_confirmada_o_corregida": "completitud_kg"
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "exoneracion", "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": null, "causa_ganadora": "completitud_kg", "votos_ganadores": 1}
- corrigio=True · par_post_s1=['context_recall', 'completitud_kg'] · usage=[{"input_tokens": 3690, "output_tokens": 139}]

### rep3_atrib1 — esquema `exoneracion` · emisión (noise_sensitivity, sin_defecto) · jerarquía sin_par

```json
{
 "respuesta_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          monto establecido en el punto 2. “D",
 "presente_en_grafo": "no",
 "causa_confirmada_o_corregida": "completitud_kg"
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "exoneracion", "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": null, "causa_ganadora": "completitud_kg", "votos_ganadores": 1}
- corrigio=True · par_post_s1=['context_recall', 'completitud_kg'] · usage=[{"input_tokens": 3702, "output_tokens": 139}]


---

# run_4/CQ-028

- resumen_s1 (v0.2): {"gatilladas": 3, "juzgadas_llm": 3, "corregidas": 2, "no_determinable": 1, "fetch_fallido": 0, "tokens_in_s1": 11834, "tokens_out_s1": 1969, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable'] · flags=['S1: rep3_atrib1 — no_determinable (0/1 decididas)']
- **voto_capa_d:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (2) · conteo=2×[['context_recall', 'completitud_kg']] · 1×[['faithfulness', 'completitud_kg']]
- **voto_s1 v0.1b (referencia congelada):** frontera_no_determinada · dividido=True · ganadores=None (None) · conteo=1×[['context_recall', 'completitud_kg']] · 1×[['context_recall', 'contenido_kg']] · 1×[['faithfulness', 'contenido_kg']]
- **voto_s1 v0.2:** mayoria · dividido=False · ganadores=[['noise_sensitivity', 'contenido_kg']] (2) · conteo=2×[['noise_sensitivity', 'contenido_kg']] · 1×[['context_recall', 'completitud_kg']]

## Atribuciones juzgadas — salidas ÍNTEGRAS

### rep1_atrib1 — esquema `causa` · emisión (context_recall, completitud_kg) · jerarquía primaria

```json
{
 "alcance_declarado_en_fuente": "En el caso de precancelación total, no se admitirá la aplicación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor.",
 "alcance_en_el_nodo": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
 "coinciden": "no",
 "sintoma_del_par": "noise_sensitivity",
 "causa_confirmada_o_corregida": "contenido_kg",
 "justificacion_breve": "La fuente declara el criterio como 'de ambos el mayor' (lo que ocurra ÚLTIMO, la condición más protectora del usuario), mientras que el nodo omite el operador de selección y la respuesta lo invirtió a 'lo que ocurra primero'. El defecto no es ausencia de información en el grafo (el nodo existe y fue recuperado), sino que el contenido del nodo está incompleto/impreciso respecto de la fuente: no transcribe el 'de ambos el mayor', habilitando la inversión. Por eso la causa se corrige de completitud_kg a contenido_kg, coherente con el claim central reprobado como falso (noise_sensitivity)."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "causa", "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "noise_sensitivity", "causa_ganadora": "contenido_kg", "votos_ganadores": 1}
- corrigio=True · par_post_s1=['noise_sensitivity', 'contenido_kg'] · usage=[{"input_tokens": 3945, "output_tokens": 507}]

### rep2_atrib1 — esquema `causa` · emisión (faithfulness, completitud_kg) · jerarquía primaria

```json
{
 "alcance_declarado_en_fuente": "En el caso de precancelación total, no se admitirá la aplicación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor.",
 "alcance_en_el_nodo": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
 "coinciden": "no",
 "sintoma_del_par": "noise_sensitivity",
 "causa_confirmada_o_corregida": "contenido_kg",
 "justificacion_breve": "La fuente fija el criterio como 'de ambos el mayor' (lo que ocurra último), pero la respuesta lo invierte a 'lo que ocurra primero', motivo del verdict=falso. El nodo omite la especificación 'de ambos el mayor' y arrastra una restricción imprecisa; el defecto no es de completitud del grafo (la fuente sí fue recuperada y el nodo existe con el contenido), sino de contenido erróneo/inexacto del nodo respecto de lo que dice la fuente, por lo que la causa se corrige de completitud_kg a contenido_kg."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "causa", "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "sintoma_ganador": "noise_sensitivity", "causa_ganadora": "contenido_kg", "votos_ganadores": 1}
- corrigio=True · par_post_s1=['noise_sensitivity', 'contenido_kg'] · usage=[{"input_tokens": 3943, "output_tokens": 663}]

### rep3_atrib1 — esquema `causa` · emisión (context_recall, completitud_kg) · jerarquía primaria

```json
{
 "alcance_declarado_en_fuente": "no_determinable",
 "alcance_en_el_nodo": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
 "coinciden": "no_determinable",
 "sintoma_del_par": "noise_sensitivity",
 "causa_confirmada_o_corregida": "contenido_kg",
 "justificacion_breve": "Los pasajes fuente verbatim recuperados (2.3.2.1 Admitidos, 2.3.2 Comisiones y cargos, y referencia interna) NO contienen el texto sobre precancelación total ni el criterio temporal, por lo que no puedo transcribir el alcance declarado en fuente. Sin embargo, el claim central fue reprobado como 'falso' (no 'no cubierto'): el contenido existe en el grafo pero contradice la fuente citada, que dice 'de ambos el mayor' mientras el nodo/respuesta dice 'lo que ocurra primero'. Esto es un defecto de contenido (valor incorrecto en el nodo), no de completitud (ausencia); se corrige de completitud_kg a contenido_kg."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "esquema": "causa", "decididas": 0, "no_decididas": 1, "resultado": "no_determinable", "sintoma_ganador": null, "causa_ganadora": null, "votos_ganadores": null}
- corrigio=False · par_post_s1=None · usage=[{"input_tokens": 3946, "output_tokens": 799}]


---

*Fin de B4.3 ronda 1/3. Iteración solo de prompt/esquema/ensamblado; fetch intacto;
salidas previas congeladas al lado. Frenado para revisión.*
