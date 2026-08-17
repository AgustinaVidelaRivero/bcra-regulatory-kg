# Estimación parametrizada — fase B encadenamiento EV2 (sin precios)

Generado: 2026-08-16T18:01:15. Población: 66 pares {'run_3': 19, 'v2': 24, 'v3': 23} × 3 = 198 corridas de agente; × 3 reps del juez = 594 llamadas al juez.

## Agente (tokens medidos en las trazas base de los mismos 66 pares, × 3)

| grafo | corridas | mediana in/out/cw/cr por corrida (base) | máx in/out/cw/cr | harness cost medio base (USD) |
|---|---|---|---|---|
| v2 | 72 | 1549.0/1908.5/14726.5/57494.5 | 5587/2523/26277/137178 | 0.03513 |
| v3 | 69 | 1533.0/1818.5/14556.0/50316.0 | 5614/2390/23085/111068 | 0.03384 |
| run_3 | 57 | 5187.0/1808.0/14990.5/55264.0 | 9497/2297/22776/141022 | 0.03747 |

- Central (tokens de la base de cada par × 3): in 594,843 / out 342,291 / cache_write 2,549,520 / cache_read 9,440,781.
- Banda mediana-grafo: {'tokens_in': 512964.0, 'tokens_out': 365944.5, 'cache_read': 10761456.0, 'cache_write': 2919130.5}; banda máx-grafo: {'tokens_in': 1330959, 'tokens_out': 477495, 'cache_read': 25578762, 'cache_write': 4783041}.
- Referencia harness.cost_usd (precios hardcodeados del harness congelado) de las trazas base × 3: USD 6.4373.
- Fórmula: `USD_agente = (in·P_in + out·P_out + cw·P_cache_write + cr·P_cache_read) / 1e6`.

## Juez (594 llamadas; chars→tokens y salida por K medidos en las 360 llamadas reales de la base)

- Medición base: 360 llamadas, mismo prompt/modelo True; chars/token in mediana 3.2267 [3.0287, 3.3696]; salida ≈ 139.87 + 82.55·K; máx por K {2: 332, 3: 576, 4: 640, 5: 698}.
- Entrada estimada: central 994,000 [951,846, 1,216,871] (stand-in: respuesta base del mismo par; banda máx con la respuesta más larga del grafo).
- Salida estimada: central 288,880 (cota máx observada 384,894).
- Fórmula: `USD_juez = (input_total·P_in_juez + output_total·P_out_juez) / 1e6`.

