# Estimación previa — calibración del descubrimiento (U-ESQ-2-cal, USD 0)

Generada 2026-08-31T21:27:57. Tope parcial **USD 0.50** (mandato U-ESQ-2-cal.c). Tarifas runner_corpus.py:76-78.

## Anclas (medidas donde las hay)
- input 20 u (P1′ medido, cota superior): 24487 tok — cota superior: el user message del descubrimiento es más corto que el de extracción P1'
- prefijo del instrumento: 6029 chars ≈ **1723 tok** (len/3,5) — si < 4096 tok, Haiku 4.5 no cachea: escenario sin caché paga el prefijo como input x20
- output: sin ancla (instrumento nuevo) → escenarios

## Cuenta
```
in_p1bis×1,00/1e6 + 20×out×5,00/1e6 + prefijo (cacheado: 1×1,25 + 19×0,10; sin caché: 20×1,00) /1e6
```

| out tok/u | prefijo cacheado | total USD |
|--:|:--:|--:|
| 100 | sí | 0.0399 |
| 100 | no | 0.0689 |
| 300 | sí | 0.0599 |
| 300 | no | 0.0889 |
| 600 | sí | 0.0899 |
| 600 | no | 0.1189 |
| 1000 | sí | 0.1299 |
| 1000 | no | 0.1589 |

Peor escenario: **USD 0.1589** — bajo el tope 0,50: **True**
