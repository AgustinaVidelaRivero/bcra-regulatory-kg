# Estimación previa — control de instrumento de ESQ-1 (U-ESQ-1c, USD 0)

Generada 2026-08-30T09:46:56. Presupuesto **USD 0.32** (scoping §5.3), tope parcial **USD 0.50** (mandato).
Tarifas: runner_corpus.py:76-78 — in 1,00 / out 5,00 / cache write 1,25 / cache read 0,10 USD/MTok.

## 1. Estimación sellada (scoping §5.3 «Control de instrumento»)
```
corrida    40 × 0,00771679                = USD 0.308672
escritura   1 × 10.383 × 1,25/1e6         = USD 0.012979
                                            ─────────
                                            USD 0.3217
```

## 2. Estimación anclada en el usage real de las 40 unidades

Input y output de esas 40 unidades en la corrida cerrada de producción (sus registros en `corpus_v2/salida/*/extracciones_e1.jsonl`): 58683 tok in, 57660 tok out (40 unidades con usage). Supuestos del scoping §5.2.1 encima: output +10 %, prefijo abierto 10.383 tok.
```
input       58683 × 1,00/1e6          = USD 0.058683
output      57660 × 1,10 × 5,00/1e6  = USD 0.317130
cache read  39 × 10.383 × 0,10/1e6        = USD 0.040494
cache write  1 × 10.383 × 1,25/1e6        = USD 0.012979
                                            ─────────
                                            USD 0.4293
```

## 3. Sensibilidad del supuesto de output (estimación anclada)

| output supuesto | total USD |
|---|--:|
| +0 % | 0.4005 |
| +10 % | 0.4293 |
| +20 % | 0.4581 |
| +30 % | 0.4869 |

## 4. Contra el presupuesto

- sellada ≤ 0,32: **True**
- anclada ≤ 0,32: **False**
- ambas < tope parcial 0,50: **True**

Discrepancia a decidir en el freno de autorización: la estimación sellada del scoping (0,32) presupone unidades de output promedio; las 40 del control son output-pesadas por construcción (se eligieron por omisiones y presión de firma). La anclada supera el presupuesto y queda bajo el tope parcial 0,50 hasta output +30 %. La decisión de gasto es de la autora.

Selección: {"por_brazo": {"A": 20, "B": 10, "C": 10}, "por_to": {"cap": 13, "cla": 3, "ext": 12, "pro": 2, "ric": 10}} — lista completa con brazo en `orden/seleccion_control_esq.json`.
