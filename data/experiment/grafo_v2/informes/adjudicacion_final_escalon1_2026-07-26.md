# Informe — Adjudicación humana y tabla final, escalón 1 (2026-07-26)

**Resultado: los laudos humanos del muestreo dirigido de flags volcados literalmente (40 laudos por réplica), mayorías recalculadas y verificadas EXACTAS contra lo esperado, acta actualizada con la sección del muestreo y los dos hallazgos, fichas actualizadas (9 de v2 + 2 de run_3).** Sin API, sin commits, sin re-evaluación de laudos.

## 1. Adjudicación volcada

`adjudicacion_humana_2026-07-26.json`: 40 laudos por réplica (qid, brazo, réplica, veredicto del juez, veredicto humano, causa), volcados literalmente del mandato. EV1-011 y EV1-029 sin cambios (subsumidas en fichas). Cobertura: EV1-007 (4 laudos), EV1-015 (6), EV1-018 (6), EV1-027 (6), EV1-031 (6), EV1-034 (6), EV1-035 (6).

## 2. Verificación (dio exacta — no hubo que frenar)

```
run_3 31/36 · grafo_v2 27/36
b = [EV1-023, EV1-035]
c = [EV1-005, EV1-015, EV1-029, EV1-031, EV1-039, EV1-042]
ambos fallan = [EV1-011, EV1-018, EV1-028]
```

## 3. TABLA FINAL (juez v2.1.1 + adjudicación humana; el humano prevalece donde hay laudo)

### Primaria — % correcto por mayoría

| | run_3 | grafo_v2 |
|---|---|---|
| **Global (36)** | **31 (86.1%)** | **27 (75.0%)** |
| puntual (10) | 9 | 7 |
| enumerativa (12) | 10 | 9 |
| condicional (8) | 7 | 8 |
| sujeto (6) | 5 | 3 |

**Pares discordantes (McNemar descriptivo): b = 2** (run_3✗→v2✓: EV1-023, EV1-035) **· c = 6** (run_3✓→v2✗: EV1-005, EV1-015, EV1-029, EV1-031, EV1-039, EV1-042). **Ambos fallan: 3** (EV1-011, EV1-018, EV1-028).

### Secundaria

| | run_3 | grafo_v2 |
|---|---|---|
| Mayorías 3-0 | 31 | 30 |
| Mayorías 2-1 | 5 | 6 |
| Pasos promedio (tool calls/rep) | 9.60 | 9.71 |
| Réplicas al límite de 15 tools | 38/108 | 36/108 |

(Uso del esqueleto en v2, sin cambios: 26 tool calls a nodos `Sujeto_` en 9/108 trazas; aristas de esqueleto en outputs en 7/108.)

### Delta vs tabla pre-adjudicación (solo juez)

| | run_3 | grafo_v2 |
|---|---|---|
| Solo juez | 33/36 (91.7%) | 30/36 (83.3%) |
| Final adjudicada | 31/36 (86.1%) | 27/36 (75.0%) |

La adjudicación movió 4 mayorías: run_3 pierde EV1-018 y EV1-035; grafo_v2 pierde EV1-015, EV1-031 y EV1-018; y EV1-035 pasa a discordante b (v2 mayoría correcta ratificada).

## 4. Acta

`acta_adjudicacion_EV1.md` actualizada con la sección **"Muestreo dirigido de flags"**: método (piezas esenciales de la key, misma vara ambos brazos), la tabla de laudos, y los dos hallazgos textuales:

(a) "el juez mostró indulgencia con respuestas evasivas en ambas direcciones y bajo flag su veredicto no es confiable — regla resultante: todo veredicto flaggeado requiere muestreo humano antes de integrar tablas"

(b) "en EV1-035 el juez emitió veredictos opuestos (correcta r1 / incorrecta r3) sobre respuestas casi idénticas — evidencia adicional de no-determinismo que motiva la regla N=3+mayoría y el muestreo"

## 5. Fichas

`corridas/fichas_fallas_v2.json` actualizado:

- **9 fichas de v2**: las 6 originales (EV1-005, 011, 028, 029, 039, 042) con falla ratificada por adjudicación humana (atribución causal pendiente de la autora) + 3 nuevas con causa adjudicada: **EV1-015** (1.1 no alcanzado, capturado el vecino 7.1; hit_tool_limit en r1/r2), **EV1-031** (dato no alcanzado, evasivas; hit_tool_limit ×3 — confirmado en trazas), **EV1-018** (no-respuesta, completitud compartida del 4.1.4).
- **2 fichas de run_3** (sección nueva `fichas_run_3`): **EV1-018** (completitud compartida) y **EV1-035** (amputación de condiciones de la excepción — registrada como simétrica inversa; v2 mayoría correcta ratificada).

## Archivos de esta unidad

- `evaluacion_escalon1/adjudicacion_humana_2026-07-26.json` (nuevo)
- `evaluacion_escalon1/resultados_FINALES_2026-07-26.json` (nuevo)
- `evaluacion_escalon1/acta_adjudicacion_EV1.md` (adenda)
- `evaluacion_escalon1/corridas/fichas_fallas_v2.json` (actualizado)
- este informe

**FRENO acá.** El commit del paquete es tuyo.
