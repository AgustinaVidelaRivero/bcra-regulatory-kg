# Estimación fase B — fidelidad EV2 (120 × N=3 = 360 llamadas al juez v1)

- Mensajes reales medidos: 120 (chars system 3199; usuario total 246706, mediana 2038.5, máx 3638); criterios por mensaje {2: 9, 3: 9, 4: 63, 5: 39}.
- Calibración (75 llamadas reales, mismo prompt/modelo: True): chars/token de entrada mediana 3.2563 [3.102, 3.3933]; salida ≈ 86.0 + 119.88·K tokens; máx observado por K {2: 303, 3: 632, 4: 732, 5: 811}.
- Tokens estimados (360 llamadas): entrada central 580953 [557498, 609851]; salida central 207903 (cota máx observada 258480).
- Fórmula: input_total/1e6 × precio_in + output_total/1e6 × precio_out. Sin precios en este archivo.
