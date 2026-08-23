# Estimación de costo — fase B de U-B1.8 (desde archivos sellados)

Generado 2026-08-23T17:22:30. Tope propuesto por el mandato: **USD 6.00**. La auditoría simétrica se supone 4 correctos → ceil(10 %) = 1 par (regla min. 1).

## Insumos (todos citados de archivos sellados)

- agente por traza de fidelidad (KG-Reextraído, pariente de r1): USD 0.03513 (ev2_corrida/trazas/ev2_base_v2/resumen_ev2_base_v2.json (casos eje=fidelidad), 40 trazas, total 1.4053); v3 0.03384, run3 0.03747
- juez base por llamada: USD 0.01206 (ev2_fidelidad_eval/out/resumen_corrida.json: 4.3405 / 360)
- agente §7 por re-corrida: USD 0.03269 (ev2_encadenamiento/reporte/resumen_agente.json: 6.4732 / 198)
- juez §7 por llamada nominal: USD 0.01135 (ev2_encadenamiento/juez_out/resumen_corrida_juez.json: 6.7441 / 594)

Margen de tamaño: r1 tiene 6.529 nodos / 17.772 aristas contra 6.178 / 11.415 del sellado (+5,7 % nodos, +55,7 % aristas): los outputs de `ver_vecinos` crecen → escenario 1,2× sobre las etapas de agente.

## Escenarios (el §7 es proporcional a los parciales de la corrida base de r1)

| parciales | pares §7 | margen | agente base | juez base | agente §7 | juez §7 | TOTAL USD | ≤ tope 6 |
|---|---|---|---|---|---|---|---|---|
| 10 | 11 | 1.0 | 1.405 | 1.447 | 1.079 | 1.124 | **5.05** | sí |
| 15 | 16 | 1.0 | 1.405 | 1.447 | 1.569 | 1.634 | **6.05** | NO |
| 20 | 21 | 1.0 | 1.405 | 1.447 | 2.059 | 2.145 | **7.06** | NO |
| 23 | 24 | 1.0 | 1.405 | 1.447 | 2.354 | 2.452 | **7.66** | NO |
| 28 | 29 | 1.0 | 1.405 | 1.447 | 2.844 | 2.962 | **8.66** | NO |
| 10 | 11 | 1.2 | 1.686 | 1.447 | 1.295 | 1.124 | **5.55** | sí |
| 15 | 16 | 1.2 | 1.686 | 1.447 | 1.883 | 1.634 | **6.65** | NO |
| 20 | 21 | 1.2 | 1.686 | 1.447 | 2.471 | 2.145 | **7.75** | NO |
| 23 | 24 | 1.2 | 1.686 | 1.447 | 2.824 | 2.452 | **8.41** | NO |
| 28 | 29 | 1.2 | 1.686 | 1.447 | 3.413 | 2.962 | **9.51** | NO |

## Lectura para el laudo del tope (la decisión es de la autora)

- Con los parciales de KG-Reextraído en la base (23) el total central es USD 7.66–8.41: supera el tope propuesto de USD 6 en ambos márgenes.
- El tope de USD 6 entra solo si los parciales de r1 son ≤ 14 (margen 1,0) / ≤ 12 (margen 1,2).
- Alternativas para el laudo: mantener USD 6 (freno por proyección activo; riesgo de detención a mitad del §7, retomable), subir el tope, o autorizar por etapas (agente base + juez base ≈ USD 2.85–3.13; el §7 con tope propio una vez conocidos los parciales — la opción que evita frenos a ciegas).
