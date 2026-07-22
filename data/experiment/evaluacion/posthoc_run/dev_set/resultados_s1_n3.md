# B4.4 — Cierre de B4: varianza de S1 v0.3 sobre el dev (N=3) — extracción SIN scoring

Fecha: 2026-07-17. **Sin cambios de código**: s1-v0.3-dev tal como quedó en la ronda 2
(aún no commiteada — hash de objeto del archivo corrido:
`6354114802f1bf4f5c337b81db3ebc4efdbc00ed`, `S1_VERSION = "s1-v0.3-dev"`). Llamadas API
frescas sobre el dev (permitido, diseño §4). Salidas `_s1_n3.json`; TODAS las previas
(`_s1`, `_s1b`, `_s1c`, `_s1d`) congeladas. **Prohibido comparar contra casos_dev_v7.md.**

## Corrida y costo medido

```
$ .venv/bin/python s1_fuentes.py --caso ..._capa_d.json --run {run} --out ..._s1_n3.json --n 3   (×4)
```

**Costo real medido (usage de la API, persistido): 90.429 tokens in / 11.102 out**
(esperado ~90-100K in — dentro del rango). 24 llamadas (8 atribuciones juzgables × 3).

## Tabla de estabilidad — atribución × 3 veredictos lado a lado

| Atribución | esquema | muestra 1 | muestra 2 | muestra 3 | Estabilidad | voto_atrib |
|---|---|---|---|---|---|---|
| CQ-008 rep1_atrib1 | causa | no·(context_recall, completitud) | ídem | ídem | **3/3** | mayoría 3/3, confirma |
| CQ-008 rep2_atrib1 | causa | no_determinable | no_determinable | no_determinable | **3/3 (abstención ESTABLE)** | no_determinable |
| r4/CQ-021 rep1 | exon | no·completitud·quote | ídem | ídem | **3/3** | mayoría, corrige |
| r4/CQ-021 rep2 | exon | ídem | ídem | ídem | **3/3** | mayoría, corrige |
| r4/CQ-021 rep3 | exon | ídem | ídem | ídem | **3/3** | mayoría, corrige |
| CQ-028 rep1_atrib1 | causa | no·(noise, contenido) | no·(noise, contenido) | ERROR json_no_parseable | **2/1** | mayoría 2/3, corrige |
| CQ-028 rep2_atrib1 | causa | no_det·causa="context_recall"(!) | no_det·completitud | no·(noise, contenido) | **1/1/1 DISPERSA** | no_determinable |
| CQ-028 rep3_atrib1 | causa | no·(noise, contenido) | no_det·completitud | no·(noise, contenido) | **2/1** | mayoría 2/3, corrige |

**Agregado: 6/8 atribuciones estables 3/3 (5 idénticas + 1 abstención estable); 2/8 con
varianza (2/1), 1/8 dispersa (1/1/1) — las tres con varianza son de CQ-028.**

## Foco pedido — la atribución de CQ-028 que dio no_determinable con N=1

En v0.2/v0.3 con N=1, la no-determinable era **rep3_atrib1**. Con 3 muestras: **2× el par
completo (noise_sensitivity, contenido_kg) con coinciden=no + 1 no_determinable → mayoría
2/3, ahora CORRIGE.** El N=3 resuelve esa abstención por varianza de sampling. La otra
cara: **rep2_atrib1** (que con N=1 había corregido) ahora sale **dispersa 1/1/1** →
no_determinable → triage. La varianza de sampling mueve atribuciones individuales de
CQ-028 en AMBAS direcciones; el voto por caso, no (ver abajo).

**Hechos de formato de las muestras de CQ-028 (material de ronda 3 si se abre):**
- El ERROR de rep1 muestra 3: salida cortada a MITAD del JSON (`texto_crudo` termina
  "…la cuarta parte del plazo " sin cerrar; 1.184 tok out, bajo el tope de 2.048) — el
  modelo cerró el turno sin terminar el JSON. Contado como no-decidida, sin reintento.
- La muestra 1 de rep2 puso un SÍNTOMA en el campo de causa
  (`causa_confirmada_o_corregida: "context_recall"`): la validación de esquema solo
  restringe `sintoma_del_par` y `coinciden` — el campo de causa es texto libre. Pasó como
  "decidida=no_determinable" (no votó por coinciden), pero el hueco de validación queda
  documentado.

## Votos_s1 finales por caso bajo N=3

| Caso | voto_capa_d | voto_s1 N=3 |
|---|---|---|
| run_2/CQ-021 | 2×{context_recall, completitud_kg} 3-0 | ídem (0 juzgables — fetch) |
| run_4/CQ-008 | {context_recall, completitud_kg} 3-0 | **ídem, confirmado 3/3** |
| run_4/CQ-021 | [] (clave vacía) 3-0 | **{context_recall, completitud_kg} 3-0** (las 3 exoneraciones corregidas 3/3 y promovidas) |
| run_4/CQ-028 | {context_recall, completitud_kg} 2-1 | **{noise_sensitivity, contenido_kg} 2-1** (reps 1 y 3 corregidas por mayoría propia; rep 2 no_determinable retiene su emisión) |

**Los votos por caso de N=3 son IDÉNTICOS a los de v0.3/N=1 (replay _s1d) en los 4
casos** — la varianza de muestra individual de CQ-028 no movió ningún voto.

## Determinismo del fetch (verificación pedida)

Dos corridas `--solo-fetch` por caso, SHA-256:

```
run_2/CQ-021: A=6c9254ff… B=6c9254ff… → IDÉNTICOS
run_4/CQ-008: A=a1a321b2… B=a1a321b2… → IDÉNTICOS
run_4/CQ-021: A=24b20390… B=24b20390… → IDÉNTICOS
run_4/CQ-028: A=9a12d150… B=9a12d150… → IDÉNTICOS
```

**4/4 byte-idénticos** — el fetch es puro; toda la varianza observada es del componente
LLM.

---

*Fin de B4.4. Cierre de la medición de B4: estabilidad 6/8, varianza concentrada en
CQ-028 (la frontera), votos por caso invariantes entre N=1 y N=3, fetch determinístico
verificado, costo medido 90.429/11.102. Frenado para revisión.*
