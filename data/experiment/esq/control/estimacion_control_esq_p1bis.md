# Estimación previa — re-corrida del control P1′ (U-ESQ-1d, USD 0)

Generada 2026-08-31T18:59:17. Tope parcial **USD 0.50** (mandato U-ESQ-1d.d). Tarifas runner_corpus.py:76-78.

## Anclas (medidas, no supuestas)
- ratio output abierto/cerrado medido: **1.0722** (40 unidades pareadas del control original: 61822 tok abierto / 57660 tok cerrado)
- prefijo abierto nuevo: 10583 tok medidos + 111 tok (delta description) = **10694 tok**

## Cuenta
```
A' input (bases + cláusulas)  14492 tok
A' output (base × ratio)      15479 tok
C  input (abierto medido)     10035 tok
C  output (abierto medido)    10247 tok
(a_in+c_in)×1,00/1e6 + (a_out+c_out)×5,00/1e6 + 19×pref×0,10/1e6 + 1×pref×1,25/1e6
TOTAL                         USD 0.1868
```

## Sensibilidad (multiplicador extra sobre el output estimado)

| mult out | total USD |
|---|--:|
| ×1.0 | 0.1868 |
| ×1.1 | 0.1997 |
| ×1.2 | 0.2126 |
| ×1.3 | 0.2254 |

Bajo el tope 0,50 hasta ×1,3: **True**
