# Estimación previa — re-corrida del control P1″ (U-ESQ-1e, USD 0)

Generada 2026-08-31T19:59:40. Tope parcial **USD 0.50** (mandato U-ESQ-1e.c). Tarifas runner_corpus.py:76-78.

## Ancla (medida, no supuesta)
- usage real de la corrida P1' (extracciones_control_esq_p1bis.jsonl): mismas 20 unidades, mismo modo
- input 20 u (P1′ medido): 24487 tok; output 20 u (P1′ medido): 25075 tok
- prefijo P1″: 10718 tok medidos (P1′) + 67 tok (delta cierres) = **10785 tok**

## Cuenta
```
in_p1bis×1,00/1e6 + out_p1bis×mult×5,00/1e6 + 19×pref×0,10/1e6 + 1×pref×1,25/1e6
TOTAL (mult ×1,0)             USD 0.1838
```

## Sensibilidad (multiplicador sobre el output medido en P1′)

| mult out | total USD |
|---|--:|
| ×1.0 | 0.1838 |
| ×1.1 | 0.1964 |
| ×1.3 | 0.2214 |
| ×1.5 | 0.2465 |

Bajo el tope 0,50 hasta ×1,5: **True**
