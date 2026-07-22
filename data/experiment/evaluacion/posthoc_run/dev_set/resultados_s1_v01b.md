# B4.2 — Correcciones determinísticas al fetch de S1 + re-corrida sobre el DEV

Fecha: 2026-07-17. Motivación: los MECANISMOS de `resultados_s1_v01.md` (vocabulario del
kg con ids anidados; provenances de preámbulo que parsean pero no localizan; hueco de
usage) — no los casos. Archivos tocados: SOLO `s1_fuentes.py` y `s1_fuentes_test.py`.
**S1_PROMPT y el esquema de salida: INTACTOS** (el juicio corrido es el mismo v0.1).
Sin commits. **PROHIBIDO comparar contra `casos_dev_v7.md`** — extracción sin scoring.

## Qué cambió en el fetch (semántica actualizada en el docstring)

1. **Match MAXIMAL de portador** — extractor PROPIO de S1 (`_extraer_portador_s1`, sin
   tocar capa_deterministica): con múltiples ids matcheados, si UN id contiene a todos los
   demás como substrings → ese es el portador; si no → `sin_portador_extraible` como la
   regla de D2. La anidación de ids es propiedad del VOCABULARIO de los grafos (run_4:
   `comision` ⊂ `comision_por_precancelacion`); la regla resuelve anidación, no
   ambigüedad real.
2. **Provenances en CASCADA:** se recorren las parseables EN ORDEN y se usa la primera que
   LOCALIZA; cada intento queda registrado (`provenances_intentadas`); solo si ninguna
   localiza → `localizacion_fallida`.
3. **Instrumentación:** usage REAL de la API por llamada en `capa_s1.usage_s1` + agregado
   `tokens_in_s1`/`tokens_out_s1` en `resumen_s1`.

## pytest (verde completo: 77 = 72 previos + 5 de B4.2)

```
.....                                                                    [100%]
77 passed in 7.12s
```

Tests nuevos: maximal único resuelve anidación (unit + paquete); matches genuinamente
distintos siguen sin desempate; cascada 1ª-falla→2ª-localiza (con registro de intentos);
ninguna localiza → fallido; usage persistido (mock con usage). Determinismo y suite previo
intactos.

## RE-CORRIDA sobre el dev (mismo S1_PROMPT v0.1, N=1 → salidas `_s1b.json`; las
`_s1.json` de B4.1 quedan CONGELADAS como registro)

### Agregado comparativo B4.1 → B4.2

| Caso | fetch_fallido | juzgadas | corregidas | no_determinable | usage medido (in/out) |
|---|---|---|---|---|---|
| run_2/CQ-021 | 6 → **6** (sin cambio) | 0 → 0 | 0 | 0 | 0/0 |
| run_4/CQ-008 | 2 → **1** | 1 → **2** | 0 | 0 → 1 | 6.755/1.031 |
| run_4/CQ-021 | 0 → 0 | 3 → 3 | 0 | 0 | 10.385/1.167 |
| run_4/CQ-028 | 3 → **0** | 0 → **3** | 0 → **2** | 0 → 1 | 10.850/1.444 |
| **TOTAL** | **11 → 7** | **4 → 8** | **0 → 2** | **0 → 2** | **27.990/3.642** |

- **4 fetch que fallaban ahora RESUELVEN** (los 3 de CQ-028 vía maximal `comision` ⊂
  `comision_por_precancelacion`; 1 de CQ-008 vía maximal sobre `legajo_del_cliente`).
- Los 6 de r2/CQ-021 siguen fallando: 4 `sin_portador_extraible` son ubicaciones con
  matches genuinamente distintos o negativas (la regla NO desempata ambigüedad real, por
  diseño) y 2 `localizacion_fallida` son portadores cuya ÚNICA provenance es el preámbulo
  de Sección 3 (la cascada no tiene adónde seguir — registrado en
  `provenances_intentadas`).
- **8/8 llamadas con JSON válido**; cero reintentos; cero formato_invalido.
- **Primer voto_s1 DIVIDIDO del dev: run_4/CQ-028** — post-S1 el conteo queda 1×
  completitud (no_determinable, causa intacta) · 1× (context_recall, contenido_kg) · 1×
  (faithfulness, contenido_kg) → sin mayoría (las 2 correcciones difieren en el par
  síntoma). voto_capa_d preservado intacto.
- Costo REAL ahora medido por instrumentación: **27.990 tok in / 3.642 tok out** (8
  llamadas; ≈3.5K in por llamada — la estimación de B4.1 por chars/4 subestimaba ~1,8×).


---

# run_2/CQ-021

- resumen_s1 (B4.2): {"gatilladas": 6, "juzgadas_llm": 0, "corregidas": 0, "no_determinable": 0, "fetch_fallido": 6, "tokens_in_s1": 0, "tokens_out_s1": 0, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable'] · flags=['S1: rep1_atrib1 — fetch sin_portador_extraible', 'S1: rep1_atrib2 — fetch sin_portador_extraible', 'S1: rep2_atrib1 — fetch localizacion_fallida', 'S1: rep2_atrib2 — fetch sin_portador_extraible', 'S1: rep3_atrib1 — fetch localizacion_fallida', 'S1: rep3_atrib2 — fetch sin_portador_extraible']
- **voto_capa_d:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]
- **voto_s1 (B4.2):** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]

## Por atribución: transición de fetch B4.1→B4.2 + paquete + salida íntegra

### rep1_atrib1 — B4.1: `sin_portador_extraible` · B4.2: `sin_portador_extraible` (igual)

- n_ids_detectados=3 · portador=None

### rep1_atrib2 — B4.1: `sin_portador_extraible` · B4.2: `sin_portador_extraible` (igual)

- n_ids_detectados=2 · portador=None

### rep2_atrib1 — B4.1: `localizacion_fallida` · B4.2: `localizacion_fallida` (igual)

- n_ids_detectados=1 · portador=procedimiento:comunicacion_de_cambio_negativo_de_clasificacion
- provenance intentada [0] `Sección 3 > Sección 3 — preámbulo` → fallida (Punto/Sección 3 (mejor score=-60 < 6))

### rep2_atrib2 — B4.1: `sin_portador_extraible` · B4.2: `sin_portador_extraible` (igual)

- n_ids_detectados=0 · portador=None

### rep3_atrib1 — B4.1: `localizacion_fallida` · B4.2: `localizacion_fallida` (igual)

- n_ids_detectados=1 · portador=obligacion:comunicar_cambios_negativos_en_clasificacion
- provenance intentada [0] `Sección 3 > Sección 3 — preámbulo` → fallida (Punto/Sección 3 (mejor score=-60 < 6))

### rep3_atrib2 — B4.1: `sin_portador_extraible` · B4.2: `sin_portador_extraible` (igual)

- n_ids_detectados=0 · portador=None


---

# run_4/CQ-008

- resumen_s1 (B4.2): {"gatilladas": 3, "juzgadas_llm": 2, "corregidas": 0, "no_determinable": 1, "fetch_fallido": 1, "tokens_in_s1": 6755, "tokens_out_s1": 1031, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable'] · flags=['S1: rep2_atrib1 — no_determinable (0/1 decididas)', 'S1: rep3_atrib1 — fetch sin_portador_extraible']
- **voto_capa_d:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg']]
- **voto_s1 (B4.2):** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (3) · conteo=3×[['context_recall', 'completitud_kg']]

## Por atribución: transición de fetch B4.1→B4.2 + paquete + salida íntegra

### rep1_atrib1 — B4.1: `completo` · B4.2: `completo` (igual)

- n_ids_detectados=1 · portador=cambio_negativo_en_clasificacion
- provenance intentada [0] `p.9-12 / Punto 3.4.2` → ok (Punto/Sección 3.4.2 (PDF pág 11))
- pasaje: Punto/Sección 3.4.2 (PDF pág 11) · comparativos: seccion_madre:3[omitido], punto_general_un_nivel_arriba:3.4[localizado], referencia_interna:4.4[localizado], referencia_interna:1.1.3.2[fallido]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "8.1. Informaciones a suministrar. A solicitud de cada cliente, dentro de los 10 días corridos del pedido, la entidad financiera deberá comunicarle la última clasificación que le ha asignado, junto con los fundamentos que la justifican según la evaluación realizada por la entidad, el importe total de deudas con el sistema financiero y las clasificaciones asignadas que surjan de la última información disponible en la 'Central de deudores del sistema financiero'.",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "no",
 "causa_confirmada_o_corregida": "completitud_kg",
 "justificacion_breve": "La fuente (Sección 8.1) declara la obligación de comunicar al cliente, a su solicitud, la última clasificación asignada dentro de 10 días corridos; el único nodo cercano trata un alcance distinto (reclasificación desfavorable comunicada dentro de 45 días, punto 3.4.2). Los pasajes verbatim del portador confirman que su provenance cubre el legajo/cambios negativos (3.4.x), no la Sección 8.1, por lo que no existe nodo para el plazo de 10 días que la pata pregunta: falta de completitud confirmada."
}
```

- usage medido: [{"input_tokens": 3598, "output_tokens": 508}] · corrigio=False · causa_post_s1=completitud_kg

### rep2_atrib1 — B4.1: `sin_portador_extraible` · B4.2: `completo` → **RESUELVE**

- n_ids_detectados=2 · portador=legajo_del_cliente
- provenance intentada [0] `p.1-8 / Sección 1.2.1` → ok (Punto/Sección 1.2.1 (PDF pág 4))
- pasaje: Punto/Sección 1.2.1 (PDF pág 4) · comparativos: seccion_madre:1[omitido], punto_general_un_nivel_arriba:1.2[localizado], referencia_interna:1[fallido]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "1.2. Criterios especiales de imputación. \n1.2.1. Créditos incorporados por cesión sin responsabilidad.",
 "alcance_en_el_nodo": "Legajo que debe llevar la entidad para cada deudor de su cartera, conteniendo todos los elementos de juicio para realizar evaluaciones y clasificaciones, dejando constancia de las revisiones efectuadas y la clasificación asignada.",
 "coinciden": "no_determinable",
 "causa_confirmada_o_corregida": "completitud_kg",
 "justificacion_breve": "Los pasajes fuente entregados (Punto 1.2 y 1.2.1/1.2.2, sobre criterios especiales de imputación de deudores) NO contienen la disposición sobre comunicación al cliente ni el plazo a solicitud del cliente; el quote fuente citado en la atribución (Punto 3.4.2, sobre cambios negativos en 45 días) no aparece en el material recuperado desde la provenance del portador. La atribución afirma correctamente que el nodo sólo cubre comunicación de cambios negativos en 45 días y no la última clasificación a pedido del cliente, pero con el material entregado no puedo transcribir un pasaje fuente que declare el alcance de la 'última clasificación a solicitud', por lo que la coincidencia de alcances no es determinable; la ausencia del contenido buscado en el grafo es consistente con completitud_kg."
}
```

- usage medido: [{"input_tokens": 3157, "output_tokens": 523}] · corrigio=False · causa_post_s1=None

### rep3_atrib1 — B4.1: `sin_portador_extraible` · B4.2: `sin_portador_extraible` (igual)

- n_ids_detectados=3 · portador=None


---

# run_4/CQ-021

- resumen_s1 (B4.2): {"gatilladas": 3, "juzgadas_llm": 3, "corregidas": 0, "no_determinable": 0, "fetch_fallido": 0, "tokens_in_s1": 10385, "tokens_out_s1": 1167, "exoneracion_con_sintoma": true}
- triage_s1: triage=False · motivos=[] · flags=[]
- **voto_capa_d:** mayoria · dividido=False · ganadores=[] (3) · conteo=3×[]
- **voto_s1 (B4.2):** mayoria · dividido=False · ganadores=[] (3) · conteo=3×[]

## Por atribución: transición de fetch B4.1→B4.2 + paquete + salida íntegra

### rep1_atrib1 — B4.1: `completo` · B4.2: `completo` (igual)

- n_ids_detectados=1 · portador=cambio_negativo_en_clasificacion
- provenance intentada [0] `p.9-12 / Punto 3.4.2` → ok (Punto/Sección 3.4.2 (PDF pág 11))
- pasaje: Punto/Sección 3.4.2 (PDF pág 11) · comparativos: seccion_madre:3[omitido], punto_general_un_nivel_arriba:3.4[localizado], referencia_interna:4.4[localizado], referencia_interna:1.1.3.2[fallido]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          monto establecido en el punto 2.",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "si",
 "causa_confirmada_o_corregida": "sin_defecto",
 "justificacion_breve": "La fuente declara la obligación general de comunicar los cambios negativos de clasificación a los deudores, con carácter optativo cuando el saldo es inferior al monto del punto 2, y remisión dentro de los 45 días por los medios listados en 3.4.2. El nodo reproduce ese mismo alcance (comunicación al deudor, 45 días, medios especificados, excepción según saldo) sin generalizar ni sobre-scopear. Los alcances coinciden y la causa 'sin_defecto' queda confirmada."
}
```

- usage medido: [{"input_tokens": 3419, "output_tokens": 403}] · corrigio=False · causa_post_s1=sin_defecto

### rep2_atrib1 — B4.1: `completo` · B4.2: `completo` (igual)

- n_ids_detectados=1 · portador=cambio_negativo_en_clasificacion
- provenance intentada [0] `p.9-12 / Punto 3.4.2` → ok (Punto/Sección 3.4.2 (PDF pág 11))
- pasaje: Punto/Sección 3.4.2 (PDF pág 11) · comparativos: seccion_madre:3[omitido], punto_general_un_nivel_arriba:3.4[localizado], referencia_interna:4.4[localizado], referencia_interna:1.1.3.2[fallido]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          monto establecido en el punto 2.",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "si",
 "causa_confirmada_o_corregida": "sin_defecto",
 "justificacion_breve": "La fuente declara que comunicar el cambio negativo es obligatorio en general y sólo optativo cuando el saldo de deuda es inferior al monto del punto 2; el nodo recoge exactamente ese alcance ('con excepciones según el saldo de deuda'). La atribución 'sin_defecto' que apunta al claim no-central sobre los medios de comunicación queda confirmada: el nodo trata el contenido con el mismo alcance scopeado que la fuente."
}
```

- usage medido: [{"input_tokens": 3477, "output_tokens": 385}] · corrigio=False · causa_post_s1=sin_defecto

### rep3_atrib1 — B4.1: `completo` · B4.2: `completo` (igual)

- n_ids_detectados=1 · portador=cambio_negativo_en_clasificacion
- provenance intentada [0] `p.9-12 / Punto 3.4.2` → ok (Punto/Sección 3.4.2 (PDF pág 11))
- pasaje: Punto/Sección 3.4.2 (PDF pág 11) · comparativos: seccion_madre:3[omitido], punto_general_un_nivel_arriba:3.4[localizado], referencia_interna:4.4[localizado], referencia_interna:1.1.3.2[fallido]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          monto establecido en el punto 2.",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "si",
 "causa_confirmada_o_corregida": "sin_defecto",
 "justificacion_breve": "La fuente declara que la comunicación es obligatoria salvo que sea optativa cuando el saldo de deuda es inferior al monto del punto 2; el nodo recoge exactamente ese alcance al mencionar la comunicación con 'excepciones según el saldo de deuda'. La atribución trata el claim sobre medios como no central y no imputa defecto, lo cual queda confirmado porque el nodo no generaliza ni omite el scope del saldo."
}
```

- usage medido: [{"input_tokens": 3489, "output_tokens": 379}] · corrigio=False · causa_post_s1=sin_defecto


---

# run_4/CQ-028

- resumen_s1 (B4.2): {"gatilladas": 3, "juzgadas_llm": 3, "corregidas": 2, "no_determinable": 1, "fetch_fallido": 0, "tokens_in_s1": 10850, "tokens_out_s1": 1444, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable'] · flags=['S1: rep1_atrib1 — no_determinable (0/1 decididas)']
- **voto_capa_d:** mayoria · dividido=False · ganadores=[['context_recall', 'completitud_kg']] (2) · conteo=2×[['context_recall', 'completitud_kg']] · 1×[['faithfulness', 'completitud_kg']]
- **voto_s1 (B4.2):** frontera_no_determinada · dividido=True · ganadores=None (None) · conteo=1×[['context_recall', 'completitud_kg']] · 1×[['context_recall', 'contenido_kg']] · 1×[['faithfulness', 'contenido_kg']]

## Por atribución: transición de fetch B4.1→B4.2 + paquete + salida íntegra

### rep1_atrib1 — B4.1: `sin_portador_extraible` · B4.2: `completo` → **RESUELVE**

- n_ids_detectados=2 · portador=comision_por_precancelacion
- provenance intentada [0] `p.12-14 / Punto 2.3.2.1, párrafo segundo` → ok (Punto/Sección 2.3.2.1 (PDF pág 11))
- pasaje: Punto/Sección 2.3.2.1 (PDF pág 11) · comparativos: seccion_madre:2[omitido], punto_general_un_nivel_arriba:2.3.2[localizado], referencia_interna:2[localizado]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "En el caso de precancelación total, no se admitirá la aplicación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor.",
 "alcance_en_el_nodo": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
 "coinciden": "no_determinable",
 "causa_confirmada_o_corregida": "completitud_kg",
 "justificacion_breve": "El texto de la fuente citado en la atribución ('2.3.2.1, párrafo segundo') NO aparece en los pasajes verbatim entregados: el pasaje recuperado del portador es 2.3.2.1 'Admitidos' (párrafo primero, sobre origen en costo real y prestación de servicios), no el párrafo que regula la precancelación total. Por lo tanto no puedo transcribir desde el material entregado el alcance fuente que la atribución invoca ni confirmar contra él; falta el pasaje que trata la restricción de precancelación."
}
```

- usage medido: [{"input_tokens": 3617, "output_tokens": 446}] · corrigio=False · causa_post_s1=None

### rep2_atrib1 — B4.1: `sin_portador_extraible` · B4.2: `completo` → **RESUELVE**

- n_ids_detectados=2 · portador=comision_por_precancelacion
- provenance intentada [0] `p.12-14 / Punto 2.3.2.1, párrafo segundo` → ok (Punto/Sección 2.3.2.1 (PDF pág 11))
- pasaje: Punto/Sección 2.3.2.1 (PDF pág 11) · comparativos: seccion_madre:2[omitido], punto_general_un_nivel_arriba:2.3.2[localizado], referencia_interna:2[localizado]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "En el caso de precancelación total, no se admitirá la aplicación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor.",
 "alcance_en_el_nodo": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
 "coinciden": "no",
 "causa_confirmada_o_corregida": "contenido_kg",
 "justificacion_breve": "La fuente establece el criterio temporal como 'de ambos el mayor' (el plazo que resulte más largo entre la cuarta parte del plazo original y los 180 días), mientras que la afirmación de la respuesta final dice 'lo que ocurra primero' (el menor). El nodo, por su parte, omite por completo el criterio de desempate ('de ambos el mayor'), dejando ambiguo cuál prevalece. La atribución imputa completitud_kg (nodo incompleto), pero el defecto real es que la respuesta final invierte el criterio temporal de la fuente ('el mayor' vs 'lo que ocurra primero'), lo que corresponde a contenido_kg: el contenido presente distorsiona el sentido de la fuente, más allá de una mera omisión."
}
```

- usage medido: [{"input_tokens": 3615, "output_tokens": 517}] · corrigio=True · causa_post_s1=contenido_kg

### rep3_atrib1 — B4.1: `sin_portador_extraible` · B4.2: `completo` → **RESUELVE**

- n_ids_detectados=2 · portador=comision_por_precancelacion
- provenance intentada [0] `p.12-14 / Punto 2.3.2.1, párrafo segundo` → ok (Punto/Sección 2.3.2.1 (PDF pág 11))
- pasaje: Punto/Sección 2.3.2.1 (PDF pág 11) · comparativos: seccion_madre:2[omitido], punto_general_un_nivel_arriba:2.3.2[localizado], referencia_interna:2[localizado]

**Salida S1 íntegra:**

```json
{
 "alcance_declarado_en_fuente": "En el caso de precancelación total, no se admitirá la aplicación de comisiones cuando al momento de efectuarla haya transcurrido al menos la cuarta parte del plazo original de la financiación o 180 días corridos desde su otorgamiento, de ambos el mayor.",
 "alcance_en_el_nodo": "Comisión que puede aplicarse por precancelación total o parcial de financiaciones, con restricción en precancelación total cuando haya transcurrido al menos la cuarta parte del plazo original o 180 días.",
 "coinciden": "no",
 "causa_confirmada_o_corregida": "contenido_kg",
 "justificacion_breve": "La fuente fija el criterio decisorio como 'de ambos el mayor' (se toma el plazo más largo entre la cuarta parte del plazo original y los 180 días), mientras que la respuesta final invierte el criterio a 'lo que ocurra primero' (el menor). El nodo portador omite por completo el criterio decisorio ('la cuarta parte del plazo original o 180 días', sin especificar cuál prevalece), por lo que el defecto no es una ausencia de nodo (completitud) sino que el contenido del nodo está incompleto/impreciso respecto de la fuente que sí lo tiene; la causa se corrige de completitud_kg a contenido_kg."
}
```

- usage medido: [{"input_tokens": 3618, "output_tokens": 481}] · corrigio=True · causa_post_s1=contenido_kg


---

# APÉNDICE — paquetes de fuentes ÍNTEGROS del fetch B4.2 (regenerados por --solo-fetch)

## Paquete run_2/CQ-021
```json
{
 "id_falla": "run_2/CQ-021",
 "run": "run_2",
 "version_s1": "s1-v0.1-dev",
 "gatillo_caso": {
  "exoneracion_con_sintoma": false,
  "sintoma_F_n": 0,
  "sintoma_P_n": 2
 },
 "atribuciones": [
  {
   "id_atribucion": "rep1_atrib1",
   "rep": 1,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": null,
   "n_ids_detectados": 3,
   "estado": "sin_portador_extraible"
  },
  {
   "id_atribucion": "rep1_atrib2",
   "rep": 1,
   "atrib_idx": 2,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": null,
   "n_ids_detectados": 2,
   "estado": "sin_portador_extraible"
  },
  {
   "id_atribucion": "rep2_atrib1",
   "rep": 2,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": "procedimiento:comunicacion_de_cambio_negativo_de_clasificacion",
   "n_ids_detectados": 1,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "Sección 3 > Sección 3 — preámbulo",
     "ref": "Punto/Sección 3 (mejor score=-60 < 6)",
     "localizacion_pdf": "fallida"
    }
   ],
   "estado": "localizacion_fallida"
  },
  {
   "id_atribucion": "rep2_atrib2",
   "rep": 2,
   "atrib_idx": 2,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": null,
   "n_ids_detectados": 0,
   "estado": "sin_portador_extraible"
  },
  {
   "id_atribucion": "rep3_atrib1",
   "rep": 3,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": "obligacion:comunicar_cambios_negativos_en_clasificacion",
   "n_ids_detectados": 1,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "Sección 3 > Sección 3 — preámbulo",
     "ref": "Punto/Sección 3 (mejor score=-60 < 6)",
     "localizacion_pdf": "fallida"
    }
   ],
   "estado": "localizacion_fallida"
  },
  {
   "id_atribucion": "rep3_atrib2",
   "rep": 3,
   "atrib_idx": 2,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": null,
   "n_ids_detectados": 0,
   "estado": "sin_portador_extraible"
  }
 ]
}
```
## Paquete run_4/CQ-008
```json
{
 "id_falla": "run_4/CQ-008",
 "run": "run_4",
 "version_s1": "s1-v0.1-dev",
 "gatillo_caso": {
  "exoneracion_con_sintoma": false,
  "sintoma_F_n": 0,
  "sintoma_P_n": 1
 },
 "atribuciones": [
  {
   "id_atribucion": "rep1_atrib1",
   "rep": 1,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": "cambio_negativo_en_clasificacion",
   "n_ids_detectados": 1,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.9-12 / Punto 3.4.2",
     "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p.9-12 / Punto 3.4.2"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "3.4.2",
   "pasaje_portador": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location_consultada": "p.9-12 / Punto 3.4.2",
    "metodo": "punto",
    "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
    "pasaje": "3.4.2. Contenido. \n \nEn el legajo se reunirán t odos los elementos de juicio que se tengan en cuenta para re a-\nlizar las evaluaciones y clasificaciones y se dejará constancia de las revisiones efectu a-\ndas y de la clasificación asignada. \n \nCuando no corresponda evaluar la capacidad de repago del deudor por e ncontrarse la \ndeuda cubierta con garantías preferidas “A”, según lo previsto en el punto 4.4., no será \nobligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda \notra información necesaria para efectuar ese análisis. \n \nA los fines de la actualización del legajo del cliente, se admitirá que la clasificación asi g-\nnada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que \ndeberá estar descripto en el “Manual de procedimientos de clasificación y previsi ón”– \npermita la identificación precisa de la clasificación asignada a cada cliente desde la plani-\nlla al legajo y viceversa. \n \nDicho legajo deberá contar con información acerca de los márgenes crediticios, d iscrimi-\nnado –de corresponder– por tipo o línea, con forme al punto 1.1.3.2., acápite ii) de l TO \nsobre Gestión Crediticia. \n \nLas entidades financieras deberán comunicar a los deudores los cambios negativos en la \nclasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          \nmonto establecido en el punto 2. “D",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "3",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "3.4",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 3.4",
     "metodo": "punto",
     "ref": "Punto/Sección 3.4 (PDF pág 10)",
     "pasaje": "3.4. Legajo del cliente.\n3.4.1. Apertura.\nLa entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno\nde sus corresponsales, de acuerdo con lo establecido en las normas sobre “Cuentas de \ncorresponsalía”.\nEn los casos de créditos cedidos a favor de la entidad sin responsabilidad para el cedente\n–unidad económica receptora de los fondos –, deberá abrirse el legajo del firmante, libr a-\ndor, deudor, codeudor o aceptante de los respectivos instrumentos, constituidos cons e-\ncuentemente en principales y directos pagadores, al que se hayan imputado las acree n-\ncias.\nNo será obligatoria la apertura del legajo en los casos de deudores por servicios públicos\no por tarjetas de crédito considerados a los fines de la clasificación por haber sido cedidos\nlos respectivos créditos por deudores en concurso preventivo.\nB.C.R.A. CLASIFICACIÓN DE DEUDORES\nSección 3. Tarea de clasificación.\nVersión: 8a. COMUNICACIÓN  “A”  7443 Vigencia:\n01/01/2020 Página 2",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "4.4",
     "mencion_verbatim": "punto 4.4.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 4.4",
     "metodo": "punto",
     "ref": "Punto/Sección 4.4 (PDF pág 2)",
     "pasaje": "4.4. Financiaciones cubiertas con garantías preferidas “A”. \n4.5. Deudores que no deben ser objeto de clasificación. \n4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de \ncrédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de \ncomprador público”. \nSección 5. Categorías de carteras. \n5.1. Categorías. \nSección 6. Clasificación de los deudores de la cartera comercial. \n6.1. Información básica. \n6.2. Criterio de clasificación. \n6.3. Periodicidad mínima de clasificación. \n6.4. Reconsideración obligatoria de la clasificación. \n6.5. Niveles de clasificación. \n6.6. Recategorización obligatoria. \nB.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE \n“CLASIFICACION DE DEUDORES” \nVersión: 6a. COMUNICACIÓN  “A”  6558 Vig encia: \n5/9/2018 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "1.1.3.2",
     "mencion_verbatim": "punto 1.1.3.2.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 1.1.3.2",
     "metodo": "punto",
     "ref": "Punto/Sección 1.1.3.2 (mejor score=n/a < 6)",
     "pasaje": null,
     "localizacion_pdf": "fallida",
     "estado": "fallido"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  },
  {
   "id_atribucion": "rep2_atrib1",
   "rep": 2,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": "legajo_del_cliente",
   "n_ids_detectados": 2,
   "provenances_total": 3,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.1-8 / Sección 1.2.1",
     "ref": "Punto/Sección 1.2.1 (PDF pág 4)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p.1-8 / Sección 1.2.1"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "1.2.1",
   "pasaje_portador": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location_consultada": "p.1-8 / Sección 1.2.1",
    "metodo": "punto",
    "ref": "Punto/Sección 1.2.1 (PDF pág 4)",
    "pasaje": "1.2.1. Créditos incorporados por cesión sin responsabilidad. \nLos créditos cedidos a favor de la entidad sin responsabilidad para el cedente -unidad \neconómica receptora de los fondos- se imputarán al firmante, librador, deudor, codeudor \no\naceptante de los respectivos instrumentos, constituidos consecuentemente en principa-\nles y directos pagadores, realizando respecto de ellos su evaluación como sujetos de\ncrédito \ncon la pertinente apertura del legajo. En caso de no efectuarse la evaluación,\ncualquiera sea el motivo, estos clientes se clasificarán en categoría “irrecuperable”.\n1.2.2. Deudores en con\ncurso preventivo. \nEn el caso de deudores que hayan solicitado su concurso preventivo, los créditos que les \nsean otorgados con posterioridad a ese pedido, en la medida que cuenten con garantías \nde terceros que permitan su cobro al vencimiento sin necesidad de la intervención del \ncliente en concurso, a los fines de esta clasificación podrán imputarse -a opción de la \nentidad- al tercero constituido en principal o directo pagador o avalista o codeudor que \nhaya renunciado al beneficio de excusión. \nCLASIFICACIÓN DE DEUDORES \nB.C.R.A. Sección 1. Deudores comprendidos. \nVersión: 1a. COMUNICACIÓN “A“ 2729 Vigencia: \n06/07/1998 Página 1",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "1",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "1.2",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 1.2",
     "metodo": "punto",
     "ref": "Punto/Sección 1.2 (PDF pág 4)",
     "pasaje": "1.2. Criterios especiales de imputación. \n1.2.1. Créditos incorporados por cesión sin responsabilidad. \nLos créditos cedidos a favor de la entidad sin responsabilidad para el cedente -unidad \neconómica receptora de los fondos- se imputarán al firmante, librador, deudor, codeudor \no\naceptante de los respectivos instrumentos, constituidos consecuentemente en principa-\nles y directos pagadores, realizando respecto de ellos su evaluación como sujetos de\ncrédito \ncon la pertinente apertura del legajo. En caso de no efectuarse la evaluación,\ncualquiera sea el motivo, estos clientes se clasificarán en categoría “irrecuperable”.\n1.2.2. Deudores en con\ncurso preventivo. \nEn el caso de deudores que hayan solicitado su concurso preventivo, los créditos que les \nsean otorgados con posterioridad a ese pedido, en la medida que cuenten con garantías \nde terceros que permitan su cobro al vencimiento sin necesidad de la intervención del \ncliente en concurso, a los fines de esta clasificación podrán imputarse -a opción de la \nentidad- al tercero constituido en principal o directo pagador o avalista o codeudor que \nhaya renunciado al beneficio de excusión. \nCLASIFICACIÓN DE DEUDORES \nB.C.R.A. Sección 1. Deudores comprendidos. \nVersión: 1a. COMUNICACIÓN “A“ 2729 Vigencia: \n06/07/1998 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "1",
     "mencion_verbatim": "Sección 1.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 1",
     "metodo": "punto",
     "ref": "Punto/Sección 1 (mejor score=-76 < 6)",
     "pasaje": null,
     "localizacion_pdf": "fallida",
     "estado": "fallido"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  },
  {
   "id_atribucion": "rep3_atrib1",
   "rep": 3,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": null,
   "n_ids_detectados": 3,
   "estado": "sin_portador_extraible"
  }
 ]
}
```
## Paquete run_4/CQ-021
```json
{
 "id_falla": "run_4/CQ-021",
 "run": "run_4",
 "version_s1": "s1-v0.1-dev",
 "gatillo_caso": {
  "exoneracion_con_sintoma": true,
  "sintoma_F_n": 1,
  "sintoma_P_n": 2
 },
 "atribuciones": [
  {
   "id_atribucion": "rep1_atrib1",
   "rep": 1,
   "atrib_idx": 1,
   "tipo_gatillo": "exoneracion_con_sintoma",
   "sintoma_capa1": "noise_sensitivity",
   "causa_capa2": "sin_defecto",
   "jerarquia": "sin_par",
   "portador_id": "cambio_negativo_en_clasificacion",
   "n_ids_detectados": 1,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.9-12 / Punto 3.4.2",
     "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p.9-12 / Punto 3.4.2"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "3.4.2",
   "pasaje_portador": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location_consultada": "p.9-12 / Punto 3.4.2",
    "metodo": "punto",
    "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
    "pasaje": "3.4.2. Contenido. \n \nEn el legajo se reunirán t odos los elementos de juicio que se tengan en cuenta para re a-\nlizar las evaluaciones y clasificaciones y se dejará constancia de las revisiones efectu a-\ndas y de la clasificación asignada. \n \nCuando no corresponda evaluar la capacidad de repago del deudor por e ncontrarse la \ndeuda cubierta con garantías preferidas “A”, según lo previsto en el punto 4.4., no será \nobligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda \notra información necesaria para efectuar ese análisis. \n \nA los fines de la actualización del legajo del cliente, se admitirá que la clasificación asi g-\nnada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que \ndeberá estar descripto en el “Manual de procedimientos de clasificación y previsi ón”– \npermita la identificación precisa de la clasificación asignada a cada cliente desde la plani-\nlla al legajo y viceversa. \n \nDicho legajo deberá contar con información acerca de los márgenes crediticios, d iscrimi-\nnado –de corresponder– por tipo o línea, con forme al punto 1.1.3.2., acápite ii) de l TO \nsobre Gestión Crediticia. \n \nLas entidades financieras deberán comunicar a los deudores los cambios negativos en la \nclasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          \nmonto establecido en el punto 2. “D",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "3",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "3.4",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 3.4",
     "metodo": "punto",
     "ref": "Punto/Sección 3.4 (PDF pág 10)",
     "pasaje": "3.4. Legajo del cliente.\n3.4.1. Apertura.\nLa entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno\nde sus corresponsales, de acuerdo con lo establecido en las normas sobre “Cuentas de \ncorresponsalía”.\nEn los casos de créditos cedidos a favor de la entidad sin responsabilidad para el cedente\n–unidad económica receptora de los fondos –, deberá abrirse el legajo del firmante, libr a-\ndor, deudor, codeudor o aceptante de los respectivos instrumentos, constituidos cons e-\ncuentemente en principales y directos pagadores, al que se hayan imputado las acree n-\ncias.\nNo será obligatoria la apertura del legajo en los casos de deudores por servicios públicos\no por tarjetas de crédito considerados a los fines de la clasificación por haber sido cedidos\nlos respectivos créditos por deudores en concurso preventivo.\nB.C.R.A. CLASIFICACIÓN DE DEUDORES\nSección 3. Tarea de clasificación.\nVersión: 8a. COMUNICACIÓN  “A”  7443 Vigencia:\n01/01/2020 Página 2",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "4.4",
     "mencion_verbatim": "punto 4.4.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 4.4",
     "metodo": "punto",
     "ref": "Punto/Sección 4.4 (PDF pág 2)",
     "pasaje": "4.4. Financiaciones cubiertas con garantías preferidas “A”. \n4.5. Deudores que no deben ser objeto de clasificación. \n4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de \ncrédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de \ncomprador público”. \nSección 5. Categorías de carteras. \n5.1. Categorías. \nSección 6. Clasificación de los deudores de la cartera comercial. \n6.1. Información básica. \n6.2. Criterio de clasificación. \n6.3. Periodicidad mínima de clasificación. \n6.4. Reconsideración obligatoria de la clasificación. \n6.5. Niveles de clasificación. \n6.6. Recategorización obligatoria. \nB.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE \n“CLASIFICACION DE DEUDORES” \nVersión: 6a. COMUNICACIÓN  “A”  6558 Vig encia: \n5/9/2018 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "1.1.3.2",
     "mencion_verbatim": "punto 1.1.3.2.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 1.1.3.2",
     "metodo": "punto",
     "ref": "Punto/Sección 1.1.3.2 (mejor score=n/a < 6)",
     "pasaje": null,
     "localizacion_pdf": "fallida",
     "estado": "fallido"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  },
  {
   "id_atribucion": "rep2_atrib1",
   "rep": 2,
   "atrib_idx": 1,
   "tipo_gatillo": "exoneracion_con_sintoma",
   "sintoma_capa1": "noise_sensitivity",
   "causa_capa2": "sin_defecto",
   "jerarquia": "sin_par",
   "portador_id": "cambio_negativo_en_clasificacion",
   "n_ids_detectados": 1,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.9-12 / Punto 3.4.2",
     "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p.9-12 / Punto 3.4.2"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "3.4.2",
   "pasaje_portador": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location_consultada": "p.9-12 / Punto 3.4.2",
    "metodo": "punto",
    "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
    "pasaje": "3.4.2. Contenido. \n \nEn el legajo se reunirán t odos los elementos de juicio que se tengan en cuenta para re a-\nlizar las evaluaciones y clasificaciones y se dejará constancia de las revisiones efectu a-\ndas y de la clasificación asignada. \n \nCuando no corresponda evaluar la capacidad de repago del deudor por e ncontrarse la \ndeuda cubierta con garantías preferidas “A”, según lo previsto en el punto 4.4., no será \nobligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda \notra información necesaria para efectuar ese análisis. \n \nA los fines de la actualización del legajo del cliente, se admitirá que la clasificación asi g-\nnada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que \ndeberá estar descripto en el “Manual de procedimientos de clasificación y previsi ón”– \npermita la identificación precisa de la clasificación asignada a cada cliente desde la plani-\nlla al legajo y viceversa. \n \nDicho legajo deberá contar con información acerca de los márgenes crediticios, d iscrimi-\nnado –de corresponder– por tipo o línea, con forme al punto 1.1.3.2., acápite ii) de l TO \nsobre Gestión Crediticia. \n \nLas entidades financieras deberán comunicar a los deudores los cambios negativos en la \nclasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          \nmonto establecido en el punto 2. “D",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "3",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "3.4",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 3.4",
     "metodo": "punto",
     "ref": "Punto/Sección 3.4 (PDF pág 10)",
     "pasaje": "3.4. Legajo del cliente.\n3.4.1. Apertura.\nLa entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno\nde sus corresponsales, de acuerdo con lo establecido en las normas sobre “Cuentas de \ncorresponsalía”.\nEn los casos de créditos cedidos a favor de la entidad sin responsabilidad para el cedente\n–unidad económica receptora de los fondos –, deberá abrirse el legajo del firmante, libr a-\ndor, deudor, codeudor o aceptante de los respectivos instrumentos, constituidos cons e-\ncuentemente en principales y directos pagadores, al que se hayan imputado las acree n-\ncias.\nNo será obligatoria la apertura del legajo en los casos de deudores por servicios públicos\no por tarjetas de crédito considerados a los fines de la clasificación por haber sido cedidos\nlos respectivos créditos por deudores en concurso preventivo.\nB.C.R.A. CLASIFICACIÓN DE DEUDORES\nSección 3. Tarea de clasificación.\nVersión: 8a. COMUNICACIÓN  “A”  7443 Vigencia:\n01/01/2020 Página 2",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "4.4",
     "mencion_verbatim": "punto 4.4.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 4.4",
     "metodo": "punto",
     "ref": "Punto/Sección 4.4 (PDF pág 2)",
     "pasaje": "4.4. Financiaciones cubiertas con garantías preferidas “A”. \n4.5. Deudores que no deben ser objeto de clasificación. \n4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de \ncrédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de \ncomprador público”. \nSección 5. Categorías de carteras. \n5.1. Categorías. \nSección 6. Clasificación de los deudores de la cartera comercial. \n6.1. Información básica. \n6.2. Criterio de clasificación. \n6.3. Periodicidad mínima de clasificación. \n6.4. Reconsideración obligatoria de la clasificación. \n6.5. Niveles de clasificación. \n6.6. Recategorización obligatoria. \nB.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE \n“CLASIFICACION DE DEUDORES” \nVersión: 6a. COMUNICACIÓN  “A”  6558 Vig encia: \n5/9/2018 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "1.1.3.2",
     "mencion_verbatim": "punto 1.1.3.2.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 1.1.3.2",
     "metodo": "punto",
     "ref": "Punto/Sección 1.1.3.2 (mejor score=n/a < 6)",
     "pasaje": null,
     "localizacion_pdf": "fallida",
     "estado": "fallido"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  },
  {
   "id_atribucion": "rep3_atrib1",
   "rep": 3,
   "atrib_idx": 1,
   "tipo_gatillo": "exoneracion_con_sintoma",
   "sintoma_capa1": "noise_sensitivity",
   "causa_capa2": "sin_defecto",
   "jerarquia": "sin_par",
   "portador_id": "cambio_negativo_en_clasificacion",
   "n_ids_detectados": 1,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.9-12 / Punto 3.4.2",
     "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "p.9-12 / Punto 3.4.2"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "3.4.2",
   "pasaje_portador": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location_consultada": "p.9-12 / Punto 3.4.2",
    "metodo": "punto",
    "ref": "Punto/Sección 3.4.2 (PDF pág 11)",
    "pasaje": "3.4.2. Contenido. \n \nEn el legajo se reunirán t odos los elementos de juicio que se tengan en cuenta para re a-\nlizar las evaluaciones y clasificaciones y se dejará constancia de las revisiones efectu a-\ndas y de la clasificación asignada. \n \nCuando no corresponda evaluar la capacidad de repago del deudor por e ncontrarse la \ndeuda cubierta con garantías preferidas “A”, según lo previsto en el punto 4.4., no será \nobligatorio incorporar al legajo del cliente el flujo de fondos, los estados contables ni toda \notra información necesaria para efectuar ese análisis. \n \nA los fines de la actualización del legajo del cliente, se admitirá que la clasificación asi g-\nnada se mantenga en planillas separadas, siempre que el procedimiento adoptado –que \ndeberá estar descripto en el “Manual de procedimientos de clasificación y previsi ón”– \npermita la identificación precisa de la clasificación asignada a cada cliente desde la plani-\nlla al legajo y viceversa. \n \nDicho legajo deberá contar con información acerca de los márgenes crediticios, d iscrimi-\nnado –de corresponder– por tipo o línea, con forme al punto 1.1.3.2., acápite ii) de l TO \nsobre Gestión Crediticia. \n \nLas entidades financieras deberán comunicar a los deudores los cambios negativos en la \nclasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          \nmonto establecido en el punto 2. “D",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "3",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "3.4",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 3.4",
     "metodo": "punto",
     "ref": "Punto/Sección 3.4 (PDF pág 10)",
     "pasaje": "3.4. Legajo del cliente.\n3.4.1. Apertura.\nLa entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno\nde sus corresponsales, de acuerdo con lo establecido en las normas sobre “Cuentas de \ncorresponsalía”.\nEn los casos de créditos cedidos a favor de la entidad sin responsabilidad para el cedente\n–unidad económica receptora de los fondos –, deberá abrirse el legajo del firmante, libr a-\ndor, deudor, codeudor o aceptante de los respectivos instrumentos, constituidos cons e-\ncuentemente en principales y directos pagadores, al que se hayan imputado las acree n-\ncias.\nNo será obligatoria la apertura del legajo en los casos de deudores por servicios públicos\no por tarjetas de crédito considerados a los fines de la clasificación por haber sido cedidos\nlos respectivos créditos por deudores en concurso preventivo.\nB.C.R.A. CLASIFICACIÓN DE DEUDORES\nSección 3. Tarea de clasificación.\nVersión: 8a. COMUNICACIÓN  “A”  7443 Vigencia:\n01/01/2020 Página 2",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "4.4",
     "mencion_verbatim": "punto 4.4.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 4.4",
     "metodo": "punto",
     "ref": "Punto/Sección 4.4 (PDF pág 2)",
     "pasaje": "4.4. Financiaciones cubiertas con garantías preferidas “A”. \n4.5. Deudores que no deben ser objeto de clasificación. \n4.6. Financiaciones –sin responsabilidad para el cedente– amparadas con seguros de \ncrédito por riesgo comercial y con seguros de riesgo de crédito “con alcance de \ncomprador público”. \nSección 5. Categorías de carteras. \n5.1. Categorías. \nSección 6. Clasificación de los deudores de la cartera comercial. \n6.1. Información básica. \n6.2. Criterio de clasificación. \n6.3. Periodicidad mínima de clasificación. \n6.4. Reconsideración obligatoria de la clasificación. \n6.5. Niveles de clasificación. \n6.6. Recategorización obligatoria. \nB.C.R.A. TEXTO ORDENADO DE LAS NORMAS SOBRE \n“CLASIFICACION DE DEUDORES” \nVersión: 6a. COMUNICACIÓN  “A”  6558 Vig encia: \n5/9/2018 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "1.1.3.2",
     "mencion_verbatim": "punto 1.1.3.2.",
     "regla": "referencia_interna",
     "source_doc": "TO_clasificacion_deudores_actual.pdf",
     "location_consultada": "Punto 1.1.3.2",
     "metodo": "punto",
     "ref": "Punto/Sección 1.1.3.2 (mejor score=n/a < 6)",
     "pasaje": null,
     "localizacion_pdf": "fallida",
     "estado": "fallido"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  }
 ]
}
```
## Paquete run_4/CQ-028
```json
{
 "id_falla": "run_4/CQ-028",
 "run": "run_4",
 "version_s1": "s1-v0.1-dev",
 "gatillo_caso": {
  "exoneracion_con_sintoma": false,
  "sintoma_F_n": 2,
  "sintoma_P_n": 0
 },
 "atribuciones": [
  {
   "id_atribucion": "rep1_atrib1",
   "rep": 1,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": "comision_por_precancelacion",
   "n_ids_detectados": 2,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo",
     "ref": "Punto/Sección 2.3.2.1 (PDF pág 11)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "2.3.2.1",
   "pasaje_portador": {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location_consultada": "p.12-14 / Punto 2.3.2.1, párrafo segundo",
    "metodo": "punto",
    "ref": "Punto/Sección 2.3.2.1 (PDF pág 11)",
    "pasaje": "2.3.2.1. Admitidos.\nTodas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con-\ncepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre-\ntendan percibir de los usuarios de servicios financieros (com isiones y cargos),\ndeben tener origen en un costo real, directo y demostrable y estar debidamente\njustificados desde el punto de vista técnico y económico.\nLa aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva\nprestación de un servicio que haya sido previamente solicitado, pactado y/o au-\ntorizado por el usuario.\nLas comisiones obedecen a servicios que prestan los sujetos obligados y, en\ntal sentido, pueden incluir retribuciones a su favor que excedan el costo de la\nprestación.\nLos cargos obedecen a servicios que prestan terceros, por lo que solamente\npueden ser transferidos al costo a los usuarios.\nAsimismo, el importe de los cargos que el sujeto obligado transfiera a los usua-\nrios no podrá ser superior al que el tercero prestador  perciba de particulares,\nsin intermediarios y en similares condiciones (servicios postales, compañía de\nseguros, escribanía y registros de propiedad, u otros de índole similar).\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 9a. COMUNICACIÓN  “A”  8203 Vigencia:\n27/02/2025 Página 7",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "2",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "2.3.2",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location_consultada": "Punto 2.3.2",
     "metodo": "punto",
     "ref": "Punto/Sección 2.3.2 (PDF pág 11)",
     "pasaje": "2.3.2. Comisiones y cargos.\n2.3.2.1. Admitidos.\nTodas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con-\ncepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre-\ntendan percibir de los usuarios de servicios financieros (com isiones y cargos),\ndeben tener origen en un costo real, directo y demostrable y estar debidamente\njustificados desde el punto de vista técnico y económico.\nLa aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva\nprestación de un servicio que haya sido previamente solicitado, pactado y/o au-\ntorizado por el usuario.\nLas comisiones obedecen a servicios que prestan los sujetos obligados y, en\ntal sentido, pueden incluir retribuciones a su favor que excedan el costo de la\nprestación.\nLos cargos obedecen a servicios que prestan terceros, por lo que solamente\npueden ser transferidos al costo a los usuarios.\nAsimismo, el importe de los cargos que el sujeto obligado transfiera a los usua-\nrios no podrá ser superior al que el tercero prestador  perciba de particulares,\nsin intermediarios y en similares condiciones (servicios postales, compañía de\nseguros, escribanía y registros de propiedad, u otros de índole similar).\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 9a. COMUNICACIÓN  “A”  8203 Vigencia:\n27/02/2",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "2",
     "mencion_verbatim": "Sección 2.",
     "regla": "referencia_interna",
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location_consultada": "Punto 2",
     "metodo": "punto",
     "ref": "Punto/Sección 2 (PDF pág 5)",
     "pasaje": "2. Personas con dificultades visuales.\nLos caj\neros automáticos destinados a los usuarios de s ervicios financieros con dificu l-\ntades visuales deberán co ntar con “software” reproductor de tex to-a-voz, auriculares\ncon su respectivo conector estándar, teclado con sistema Braille o estándar con relieve\nresaltado y mecanismo audible y perceptible destinado a alertar el olvido de la tarjeta\ny/o del dinero dispensado por el equipo.\nLos suj\netos obligados enumerados en el punto 1.1.2., en la medida en que correspon-\nda, deberán alcanzar la cobertura del servicio con esos cajeros automáticos en al me-\nnos el 10 % del total de los equipos instalados, comenzando con aquellos emplazados\nen las localidades de mayor población, sin perjuicio de las mayores obligaciones a fa-\nvor de tales personas que pueda imponer la normativa local.\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 5a. COMUNICACIÓN  “A”  7744 Vigencia:\n28/02/2023 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  },
  {
   "id_atribucion": "rep2_atrib1",
   "rep": 2,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "faithfulness",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": "comision_por_precancelacion",
   "n_ids_detectados": 2,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo",
     "ref": "Punto/Sección 2.3.2.1 (PDF pág 11)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "2.3.2.1",
   "pasaje_portador": {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location_consultada": "p.12-14 / Punto 2.3.2.1, párrafo segundo",
    "metodo": "punto",
    "ref": "Punto/Sección 2.3.2.1 (PDF pág 11)",
    "pasaje": "2.3.2.1. Admitidos.\nTodas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con-\ncepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre-\ntendan percibir de los usuarios de servicios financieros (com isiones y cargos),\ndeben tener origen en un costo real, directo y demostrable y estar debidamente\njustificados desde el punto de vista técnico y económico.\nLa aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva\nprestación de un servicio que haya sido previamente solicitado, pactado y/o au-\ntorizado por el usuario.\nLas comisiones obedecen a servicios que prestan los sujetos obligados y, en\ntal sentido, pueden incluir retribuciones a su favor que excedan el costo de la\nprestación.\nLos cargos obedecen a servicios que prestan terceros, por lo que solamente\npueden ser transferidos al costo a los usuarios.\nAsimismo, el importe de los cargos que el sujeto obligado transfiera a los usua-\nrios no podrá ser superior al que el tercero prestador  perciba de particulares,\nsin intermediarios y en similares condiciones (servicios postales, compañía de\nseguros, escribanía y registros de propiedad, u otros de índole similar).\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 9a. COMUNICACIÓN  “A”  8203 Vigencia:\n27/02/2025 Página 7",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "2",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "2.3.2",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location_consultada": "Punto 2.3.2",
     "metodo": "punto",
     "ref": "Punto/Sección 2.3.2 (PDF pág 11)",
     "pasaje": "2.3.2. Comisiones y cargos.\n2.3.2.1. Admitidos.\nTodas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con-\ncepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre-\ntendan percibir de los usuarios de servicios financieros (com isiones y cargos),\ndeben tener origen en un costo real, directo y demostrable y estar debidamente\njustificados desde el punto de vista técnico y económico.\nLa aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva\nprestación de un servicio que haya sido previamente solicitado, pactado y/o au-\ntorizado por el usuario.\nLas comisiones obedecen a servicios que prestan los sujetos obligados y, en\ntal sentido, pueden incluir retribuciones a su favor que excedan el costo de la\nprestación.\nLos cargos obedecen a servicios que prestan terceros, por lo que solamente\npueden ser transferidos al costo a los usuarios.\nAsimismo, el importe de los cargos que el sujeto obligado transfiera a los usua-\nrios no podrá ser superior al que el tercero prestador  perciba de particulares,\nsin intermediarios y en similares condiciones (servicios postales, compañía de\nseguros, escribanía y registros de propiedad, u otros de índole similar).\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 9a. COMUNICACIÓN  “A”  8203 Vigencia:\n27/02/2",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "2",
     "mencion_verbatim": "Sección 2.",
     "regla": "referencia_interna",
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location_consultada": "Punto 2",
     "metodo": "punto",
     "ref": "Punto/Sección 2 (PDF pág 5)",
     "pasaje": "2. Personas con dificultades visuales.\nLos caj\neros automáticos destinados a los usuarios de s ervicios financieros con dificu l-\ntades visuales deberán co ntar con “software” reproductor de tex to-a-voz, auriculares\ncon su respectivo conector estándar, teclado con sistema Braille o estándar con relieve\nresaltado y mecanismo audible y perceptible destinado a alertar el olvido de la tarjeta\ny/o del dinero dispensado por el equipo.\nLos suj\netos obligados enumerados en el punto 1.1.2., en la medida en que correspon-\nda, deberán alcanzar la cobertura del servicio con esos cajeros automáticos en al me-\nnos el 10 % del total de los equipos instalados, comenzando con aquellos emplazados\nen las localidades de mayor población, sin perjuicio de las mayores obligaciones a fa-\nvor de tales personas que pueda imponer la normativa local.\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 5a. COMUNICACIÓN  “A”  7744 Vigencia:\n28/02/2023 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  },
  {
   "id_atribucion": "rep3_atrib1",
   "rep": 3,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "context_recall",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": "comision_por_precancelacion",
   "n_ids_detectados": 2,
   "provenances_total": 1,
   "provenances_intentadas": [
    {
     "idx": 0,
     "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo",
     "ref": "Punto/Sección 2.3.2.1 (PDF pág 11)",
     "localizacion_pdf": "ok"
    }
   ],
   "provenance": {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location": "p.12-14 / Punto 2.3.2.1, párrafo segundo"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "2.3.2.1",
   "pasaje_portador": {
    "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "location_consultada": "p.12-14 / Punto 2.3.2.1, párrafo segundo",
    "metodo": "punto",
    "ref": "Punto/Sección 2.3.2.1 (PDF pág 11)",
    "pasaje": "2.3.2.1. Admitidos.\nTodas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con-\ncepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre-\ntendan percibir de los usuarios de servicios financieros (com isiones y cargos),\ndeben tener origen en un costo real, directo y demostrable y estar debidamente\njustificados desde el punto de vista técnico y económico.\nLa aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva\nprestación de un servicio que haya sido previamente solicitado, pactado y/o au-\ntorizado por el usuario.\nLas comisiones obedecen a servicios que prestan los sujetos obligados y, en\ntal sentido, pueden incluir retribuciones a su favor que excedan el costo de la\nprestación.\nLos cargos obedecen a servicios que prestan terceros, por lo que solamente\npueden ser transferidos al costo a los usuarios.\nAsimismo, el importe de los cargos que el sujeto obligado transfiera a los usua-\nrios no podrá ser superior al que el tercero prestador  perciba de particulares,\nsin intermediarios y en similares condiciones (servicios postales, compañía de\nseguros, escribanía y registros de propiedad, u otros de índole similar).\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 9a. COMUNICACIÓN  “A”  8203 Vigencia:\n27/02/2025 Página 7",
    "localizacion_pdf": "ok"
   },
   "comparativos": [
    {
     "tipo": "seccion_madre",
     "punto": "2",
     "regla": "encabezado de la sección madre: primer nivel del punto del portador",
     "estado": "omitido",
     "nota": "seccion_madre omitida: encabezado de primer nivel = carátula sin prosa — sondeo en los 4 TOs, reporte_b3_s1.md hecho b"
    },
    {
     "tipo": "punto_general_un_nivel_arriba",
     "punto": "2.3.2",
     "regla": "mismo prefijo, un nivel arriba (padre inmediato del punto del portador)",
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location_consultada": "Punto 2.3.2",
     "metodo": "punto",
     "ref": "Punto/Sección 2.3.2 (PDF pág 11)",
     "pasaje": "2.3.2. Comisiones y cargos.\n2.3.2.1. Admitidos.\nTodas las comisiones, cargos, costos, gastos, seguros y/o cualquier otro con-\ncepto –excluyendo la tasa de interés– que los sujetos obligados perciban o pre-\ntendan percibir de los usuarios de servicios financieros (com isiones y cargos),\ndeben tener origen en un costo real, directo y demostrable y estar debidamente\njustificados desde el punto de vista técnico y económico.\nLa aplicación de comisiones y/o cargos debe quedar circunscripta a la efectiva\nprestación de un servicio que haya sido previamente solicitado, pactado y/o au-\ntorizado por el usuario.\nLas comisiones obedecen a servicios que prestan los sujetos obligados y, en\ntal sentido, pueden incluir retribuciones a su favor que excedan el costo de la\nprestación.\nLos cargos obedecen a servicios que prestan terceros, por lo que solamente\npueden ser transferidos al costo a los usuarios.\nAsimismo, el importe de los cargos que el sujeto obligado transfiera a los usua-\nrios no podrá ser superior al que el tercero prestador  perciba de particulares,\nsin intermediarios y en similares condiciones (servicios postales, compañía de\nseguros, escribanía y registros de propiedad, u otros de índole similar).\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 9a. COMUNICACIÓN  “A”  8203 Vigencia:\n27/02/2",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    },
    {
     "tipo": "referencia_interna",
     "punto": "2",
     "mencion_verbatim": "Sección 2.",
     "regla": "referencia_interna",
     "source_doc": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
     "location_consultada": "Punto 2",
     "metodo": "punto",
     "ref": "Punto/Sección 2 (PDF pág 5)",
     "pasaje": "2. Personas con dificultades visuales.\nLos caj\neros automáticos destinados a los usuarios de s ervicios financieros con dificu l-\ntades visuales deberán co ntar con “software” reproductor de tex to-a-voz, auriculares\ncon su respectivo conector estándar, teclado con sistema Braille o estándar con relieve\nresaltado y mecanismo audible y perceptible destinado a alertar el olvido de la tarjeta\ny/o del dinero dispensado por el equipo.\nLos suj\netos obligados enumerados en el punto 1.1.2., en la medida en que correspon-\nda, deberán alcanzar la cobertura del servicio con esos cajeros automáticos en al me-\nnos el 10 % del total de los equipos instalados, comenzando con aquellos emplazados\nen las localidades de mayor población, sin perjuicio de las mayores obligaciones a fa-\nvor de tales personas que pueda imponer la normativa local.\nB.C.R.A. PROTECCIÓN DE LOS USUARIOS DE SERVICIOS FINANCIEROS\nSección 2. Derechos básicos de los usuarios de servicios financieros.\nVersión: 5a. COMUNICACIÓN  “A”  7744 Vigencia:\n28/02/2023 Página 1",
     "localizacion_pdf": "ok",
     "estado": "localizado"
    }
   ],
   "notas_regla": [],
   "estado": "completo"
  }
 ]
}
```

---

*Fin de B4.2. Fetch corregido por mecanismo y re-corrido con el MISMO juicio v0.1; las
salidas de B4.1 quedan congeladas al lado. Frenado para revisión.*
