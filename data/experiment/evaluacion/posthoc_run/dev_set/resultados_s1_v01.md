# B4.1 — Primera corrida de S1 sobre el DEV (s1-v0.1-dev) — extracción SIN scoring

Fecha: 2026-07-17. **PROHIBIDO en este reporte: comparar contra `casos_dev_v7.md`.**
Versión corrida: `s1-v0.1-dev` tal como está commiteada (`60152eb`) — `git diff HEAD`
vacío sobre s1_fuentes.py antes de correr; **sin iteración**. Material: los 4 JSONs
`_capa_d` congelados de `posthoc_run/dev_v7/`. N=1 (pre-registrado para la iteración; la
política final de N se decide al cierre de B4 midiendo varianza sobre el dev).

```
$ .venv/bin/python s1_fuentes.py --caso posthoc_run/dev_v7/off_{run}_{qid}_capa_d.json \
    --run {run} --out posthoc_run/dev_v7/off_{run}_{qid}_s1.json --n 1     (×4 casos)
```

## Agregado de la corrida

| Caso | gatilladas | juzgadas (LLM) | fetch_fallido | corregidas | no_determinable | triage_s1 |
|---|---|---|---|---|---|---|
| run_2/CQ-021 | 6 | 0 | 6 | 0 | 0 | fuente_no_verificable ×6 |
| run_4/CQ-008 | 3 | 1 | 2 | 0 | 0 | fuente_no_verificable ×2 |
| run_4/CQ-021 | 3 (exoneración c/síntoma) | 3 | 0 | 0 | 0 | SIN triage |
| run_4/CQ-028 | 3 | 0 | 3 | 0 | 0 | fuente_no_verificable ×3 |
| **TOTAL** | **15** | **4** | **11** | **0** | **0** | — |

- **4 llamadas LLM en total; 4/4 con JSON válido y esquema completo** — cero
  formato_invalido, cero reintentos (ni transitorios ni de otro tipo).
- **Cero correcciones:** las 4 salidas confirmaron la causa emitida (1× completitud_kg
  con coinciden=no; 3× sin_defecto con coinciden=si).
- `version_capa_s1: s1-v0.1-dev` en los 4; votos previos (voto/voto_pre_d6/voto_capa_d)
  preservados intactos en los 4 JSONs `_s1.json`.
- **voto_s1 = voto_capa_d en los 4 casos** (sin correcciones no hay recomputo distinto).

## Costo real de S1 — CON HUECO DE INSTRUMENTACIÓN (documentado)

**Hallazgo de instrumentación:** `s1-v0.1-dev` NO persiste el usage de la API (la salida
guarda el JSON parseado, no `resp.usage`) — **ítem para la iteración de B4**. Estimación
determinística (prompt reconstruido por código puro, chars/4; salida almacenada, chars/4):

| Llamada | prompt (chars) | ~tok in | salida (chars) | ~tok out |
|---|---|---|---|---|
| run_4/CQ-008 rep1_atrib1 | 8.127 | ~2.031 | 1.230 | ~307 |
| run_4/CQ-021 rep1_atrib1 | 7.628 | ~1.907 | 1.223 | ~305 |
| run_4/CQ-021 rep2_atrib1 | 7.785 | ~1.946 | 919 | ~229 |
| run_4/CQ-021 rep3_atrib1 | 7.814 | ~1.953 | 857 | ~214 |
| **TOTAL (4 llamadas)** | — | **~7.8K** | — | **~1.1K** |

(Órdenes de magnitud: el incremental de S1 fue ≈0,1% del costo de la corrida v6.1-D del
dev — 5,50M tok in.)

## Mecanismos de los 11 fetch fallidos (hechos para el diagnóstico de B4 — sin arreglar)

1. **Ids anidados del kg (8 de los 11):** `_extraer_portador` (el extractor pre-registrado
   de D2, regla "más de un id distinto → sin_portador, sin desempate") cae en TODOS los
   casos donde otro id del kg es SUBSTRING del citado o donde la ubicación cita varios
   nodos:
   - run_4 tiene un nodo con id **`comision`**, substring de `comision_por_precancelacion`
     → las 3 atribuciones de CQ-028 (portador claramente citado y abierto en paso 3)
     quedan `sin_portador_extraible` con n_ids=2.
   - run_2: `concepto_definido:deudor` es substring de
     `concepto_definido:deudor_en_situacion_3_4_o_5` (r2/CQ-021 rep1, n_ids=3 con dos
     nodos citados de verdad).
   - Ubicaciones "negativas" del verificador (citan lo que NO existe, sin id, o con
     varios ids descriptivos): n_ids=0 o >1 (r2/CQ-021 rep2_atrib2/rep3_atrib2;
     r4/CQ-008 reps 2-3).
2. **Provenance de preámbulo (2):** los portadores de run_2 con location
   `"Sección 3 > Sección 3 — preámbulo"` parsean a "3" y `localize` falla (carátula,
   score −60) → `localizacion_fallida` (r2/CQ-021 rep2_atrib1/rep3_atrib1). Es el patrón
   de encabezados de primer nivel ya medido en B3 — acá aparece vía provenance, no vía
   comparativo.
3. Comparativo `referencia_interna 1.1.3.2` [fallido] en los paquetes completos de run_4:
   NO bloqueó (política B3b), la llamada se hizo igual.


---

# run_2/CQ-021

- gatillo_caso: {"exoneracion_con_sintoma": false, "sintoma_F_n": 0, "sintoma_P_n": 2}
- resumen_s1: {"gatilladas": 6, "juzgadas_llm": 0, "corregidas": 0, "no_determinable": 0, "fetch_fallido": 6, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable']
  - S1: rep1_atrib1 — fetch sin_portador_extraible
  - S1: rep1_atrib2 — fetch sin_portador_extraible
  - S1: rep2_atrib1 — fetch localizacion_fallida
  - S1: rep2_atrib2 — fetch sin_portador_extraible
  - S1: rep3_atrib1 — fetch localizacion_fallida
  - S1: rep3_atrib2 — fetch sin_portador_extraible
- **voto_capa_d:** mayoria · ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] (3 votos) · conteo=3×[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]
- **voto_s1:** mayoria · ganadores=[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']] (3 votos) · conteo=3×[['context_recall', 'completitud_kg'], ['context_recall', 'completitud_kg']]

## Por atribución gatillada (paquete resumido + salida S1 íntegra)

### rep1_atrib1 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=3 → triage fuente_no_verificable (sin llamada)

### rep1_atrib2 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=2 → triage fuente_no_verificable (sin llamada)

### rep2_atrib1 — gatillo `causa_gatillada` · fetch `localizacion_fallida`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- portador `procedimiento:comunicacion_de_cambio_negativo_de_clasificacion` · provenance: `Sección 3 > Sección 3 — preámbulo` → Punto/Sección 3 (mejor score=-60 < 6) → triage fuente_no_verificable (sin llamada)

### rep2_atrib2 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=0 → triage fuente_no_verificable (sin llamada)

### rep3_atrib1 — gatillo `causa_gatillada` · fetch `localizacion_fallida`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- portador `obligacion:comunicar_cambios_negativos_en_clasificacion` · provenance: `Sección 3 > Sección 3 — preámbulo` → Punto/Sección 3 (mejor score=-60 < 6) → triage fuente_no_verificable (sin llamada)

### rep3_atrib2 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=0 → triage fuente_no_verificable (sin llamada)


---

# run_4/CQ-008

- gatillo_caso: {"exoneracion_con_sintoma": false, "sintoma_F_n": 0, "sintoma_P_n": 1}
- resumen_s1: {"gatilladas": 3, "juzgadas_llm": 1, "corregidas": 0, "no_determinable": 0, "fetch_fallido": 2, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable']
  - S1: rep2_atrib1 — fetch sin_portador_extraible
  - S1: rep3_atrib1 — fetch sin_portador_extraible
- **voto_capa_d:** mayoria · ganadores=[['context_recall', 'completitud_kg']] (3 votos) · conteo=3×[['context_recall', 'completitud_kg']]
- **voto_s1:** mayoria · ganadores=[['context_recall', 'completitud_kg']] (3 votos) · conteo=3×[['context_recall', 'completitud_kg']]

## Por atribución gatillada (paquete resumido + salida S1 íntegra)

### rep1_atrib1 — gatillo `causa_gatillada` · fetch `completo`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- portador `cambio_negativo_en_clasificacion` · provenance verbatim: `p.9-12 / Punto 3.4.2` → Punto/Sección 3.4.2 (PDF pág 11) (ok)
- comparativo seccion_madre (Punto 3): **omitido**
- comparativo punto_general_un_nivel_arriba (Punto 3.4): **localizado**
- comparativo referencia_interna (Punto 4.4): **localizado** · mención: `punto 4.4.`
- comparativo referencia_interna (Punto 1.1.3.2): **fallido** · mención: `punto 1.1.3.2.`

**Salida S1 (íntegra):**

```json
{
 "alcance_declarado_en_fuente": "8.1. Informaciones a suministrar. A solicitud de cada cliente, dentro de los 10 días corridos del pedido, la entidad financiera deberá comunicarle la última clasificación que le ha asignado, junto con los fundamentos que la justifican según la evaluación realizada por la entidad, el importe total de deudas con el sistema financiero y las clasificaciones asignadas que surjan de la última información disponible en la 'Central de deudores del sistema financiero'.",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "no",
 "causa_confirmada_o_corregida": "completitud_kg",
 "justificacion_breve": "La fuente (Sección 8.1) declara la obligación de comunicar al cliente, a su solicitud, la última clasificación dentro de 10 días corridos. El único nodo cercano cubre un alcance distinto: la comunicación de cambios negativos/reclasificación desfavorable dentro de 45 días (punto 3.4.2), que no responde la pata. No existe nodo que capture la disposición de la Sección 8.1, por lo que la falta de ese contenido en el grafo confirma completitud_kg."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "causa_ganadora": "completitud_kg", "votos_ganadores": 1} · corrigio=False · causa_post_s1=completitud_kg

### rep2_atrib1 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=2 → triage fuente_no_verificable (sin llamada)

### rep3_atrib1 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=3 → triage fuente_no_verificable (sin llamada)


---

# run_4/CQ-021

- gatillo_caso: {"exoneracion_con_sintoma": true, "sintoma_F_n": 1, "sintoma_P_n": 2}
- resumen_s1: {"gatilladas": 3, "juzgadas_llm": 3, "corregidas": 0, "no_determinable": 0, "fetch_fallido": 0, "exoneracion_con_sintoma": true}
- triage_s1: triage=False · motivos=[]
- **voto_capa_d:** mayoria · ganadores=[] (3 votos) · conteo=3×[]
- **voto_s1:** mayoria · ganadores=[] (3 votos) · conteo=3×[]

## Por atribución gatillada (paquete resumido + salida S1 íntegra)

### rep1_atrib1 — gatillo `exoneracion_con_sintoma` · fetch `completo`

- emisión v6.1-D: (noise_sensitivity, sin_defecto) · sin_par
- portador `cambio_negativo_en_clasificacion` · provenance verbatim: `p.9-12 / Punto 3.4.2` → Punto/Sección 3.4.2 (PDF pág 11) (ok)
- comparativo seccion_madre (Punto 3): **omitido**
- comparativo punto_general_un_nivel_arriba (Punto 3.4): **localizado**
- comparativo referencia_interna (Punto 4.4): **localizado** · mención: `punto 4.4.`
- comparativo referencia_interna (Punto 1.1.3.2): **fallido** · mención: `punto 1.1.3.2.`

**Salida S1 (íntegra):**

```json
{
 "alcance_declarado_en_fuente": "Tal información deberá ser remitida a los deudores comprendidos dentro de los 45 días de realizada la reclasificación mediante alguno de los siguientes medios: a) junto con el resumen impreso que se envíe al deudor con los movimientos de alguna de las cuentas que se vinculen a las financiaciones que le hayan sido otorgadas, b) junto con el resumen de cuenta mensual correspondiente a tarjetas de crédito,",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "si",
 "causa_confirmada_o_corregida": "sin_defecto",
 "justificacion_breve": "La fuente establece la obligación de comunicar los cambios negativos en la clasificación a los deudores comprendidos dentro de 45 días mediante medios especificados, con carácter optativo cuando el saldo es inferior al monto establecido; el nodo reproduce fielmente ese alcance (45 días, medios especificados, excepciones según saldo) sin generalizarlo ni restringirlo indebidamente. La atribución trata la afirmación como no central y correctamente scopeada, por lo que sin_defecto queda confirmada."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "causa_ganadora": "sin_defecto", "votos_ganadores": 1} · corrigio=False · causa_post_s1=sin_defecto

### rep2_atrib1 — gatillo `exoneracion_con_sintoma` · fetch `completo`

- emisión v6.1-D: (noise_sensitivity, sin_defecto) · sin_par
- portador `cambio_negativo_en_clasificacion` · provenance verbatim: `p.9-12 / Punto 3.4.2` → Punto/Sección 3.4.2 (PDF pág 11) (ok)
- comparativo seccion_madre (Punto 3): **omitido**
- comparativo punto_general_un_nivel_arriba (Punto 3.4): **localizado**
- comparativo referencia_interna (Punto 4.4): **localizado** · mención: `punto 4.4.`
- comparativo referencia_interna (Punto 1.1.3.2): **fallido** · mención: `punto 1.1.3.2.`

**Salida S1 (íntegra):**

```json
{
 "alcance_declarado_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al monto establecido en el punto 2. \"D",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "si",
 "causa_confirmada_o_corregida": "sin_defecto",
 "justificacion_breve": "La fuente declara que la comunicación es obligatoria en general pero OPTATIVA cuando el saldo de deuda es inferior al monto del punto 2; el nodo captura exactamente esa condicionalidad al decir 'con excepciones según el saldo de deuda'. El alcance del nodo coincide con el de la fuente (no generaliza ni sobre-limita el carácter optativo), por lo que la causa sin_defecto queda confirmada."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "causa_ganadora": "sin_defecto", "votos_ganadores": 1} · corrigio=False · causa_post_s1=sin_defecto

### rep3_atrib1 — gatillo `exoneracion_con_sintoma` · fetch `completo`

- emisión v6.1-D: (noise_sensitivity, sin_defecto) · sin_par
- portador `cambio_negativo_en_clasificacion` · provenance verbatim: `p.9-12 / Punto 3.4.2` → Punto/Sección 3.4.2 (PDF pág 11) (ok)
- comparativo seccion_madre (Punto 3): **omitido**
- comparativo punto_general_un_nivel_arriba (Punto 3.4): **localizado**
- comparativo referencia_interna (Punto 4.4): **localizado** · mención: `punto 4.4.`
- comparativo referencia_interna (Punto 1.1.3.2): **fallido** · mención: `punto 1.1.3.2.`

**Salida S1 (íntegra):**

```json
{
 "alcance_declarado_en_fuente": "Las entidades financieras deberán comunicar a los deudores los cambios negativos en la clasificación que se les asigne, siendo optativo cuando el saldo de deuda sea inferior al          monto establecido en el punto 2.",
 "alcance_en_el_nodo": "Reclasificación desfavorable del deudor que debe ser comunicada al deudor dentro de 45 días mediante medios especificados, con excepciones según el saldo de deuda.",
 "coinciden": "si",
 "causa_confirmada_o_corregida": "sin_defecto",
 "justificacion_breve": "La fuente declara que la comunicación es obligatoria pero optativa cuando el saldo de deuda es inferior al monto del punto 2; el nodo recoge exactamente ese alcance al mencionar 'con excepciones según el saldo de deuda'. El nodo no generaliza ni sobre-scopea el contenido, por lo que la causa sin_defecto queda confirmada."
}
```

- voto_s1_atrib: {"n": 1, "umbral": 1, "decididas": 1, "no_decididas": 0, "resultado": "mayoria", "causa_ganadora": "sin_defecto", "votos_ganadores": 1} · corrigio=False · causa_post_s1=sin_defecto


---

# run_4/CQ-028

- gatillo_caso: {"exoneracion_con_sintoma": false, "sintoma_F_n": 2, "sintoma_P_n": 0}
- resumen_s1: {"gatilladas": 3, "juzgadas_llm": 0, "corregidas": 0, "no_determinable": 0, "fetch_fallido": 3, "exoneracion_con_sintoma": false}
- triage_s1: triage=True · motivos=['fuente_no_verificable']
  - S1: rep1_atrib1 — fetch sin_portador_extraible
  - S1: rep2_atrib1 — fetch sin_portador_extraible
  - S1: rep3_atrib1 — fetch sin_portador_extraible
- **voto_capa_d:** mayoria · ganadores=[['context_recall', 'completitud_kg']] (2 votos) · conteo=2×[['context_recall', 'completitud_kg']] · 1×[['faithfulness', 'completitud_kg']]
- **voto_s1:** mayoria · ganadores=[['context_recall', 'completitud_kg']] (2 votos) · conteo=2×[['context_recall', 'completitud_kg']] · 1×[['faithfulness', 'completitud_kg']]

## Por atribución gatillada (paquete resumido + salida S1 íntegra)

### rep1_atrib1 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=2 → triage fuente_no_verificable (sin llamada)

### rep2_atrib1 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (faithfulness, completitud_kg) · primaria
- n_ids_detectados=2 → triage fuente_no_verificable (sin llamada)

### rep3_atrib1 — gatillo `causa_gatillada` · fetch `sin_portador_extraible`

- emisión v6.1-D: (context_recall, completitud_kg) · primaria
- n_ids_detectados=2 → triage fuente_no_verificable (sin llamada)


---

# APÉNDICE — paquetes de fuentes ÍNTEGROS (regenerados por --solo-fetch, determinístico)

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
   "provenances_total": 1,
   "provenance": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Sección 3 > Sección 3 — preámbulo"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "3",
   "pasaje_portador": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location_consultada": "Sección 3 > Sección 3 — preámbulo",
    "metodo": "punto",
    "ref": "Punto/Sección 3 (mejor score=-60 < 6)",
    "pasaje": null,
    "localizacion_pdf": "fallida"
   },
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
   "provenances_total": 1,
   "provenance": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location": "Sección 3 > Sección 3 — preámbulo"
   },
   "provenance_usada_idx": 0,
   "punto_parseado": "3",
   "pasaje_portador": {
    "source_doc": "TO_clasificacion_deudores_actual.pdf",
    "location_consultada": "Sección 3 > Sección 3 — preámbulo",
    "metodo": "punto",
    "ref": "Punto/Sección 3 (mejor score=-60 < 6)",
    "pasaje": null,
    "localizacion_pdf": "fallida"
   },
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
   "provenances_total": 1,
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
   "portador_id": null,
   "n_ids_detectados": 2,
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
   "provenances_total": 1,
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
   "provenances_total": 1,
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
   "provenances_total": 1,
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
   "portador_id": null,
   "n_ids_detectados": 2,
   "estado": "sin_portador_extraible"
  },
  {
   "id_atribucion": "rep2_atrib1",
   "rep": 2,
   "atrib_idx": 1,
   "tipo_gatillo": "causa_gatillada",
   "sintoma_capa1": "faithfulness",
   "causa_capa2": "completitud_kg",
   "jerarquia": "primaria",
   "portador_id": null,
   "n_ids_detectados": 2,
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
   "portador_id": null,
   "n_ids_detectados": 2,
   "estado": "sin_portador_extraible"
  }
 ]
}
```

---

*Fin de B4.1. Corrida de la versión commiteada sin iterar; los hechos de fetch (ids
anidados, provenances de preámbulo, hueco de usage) son el insumo del diagnóstico de la
iteración. Frenado para revisión.*
