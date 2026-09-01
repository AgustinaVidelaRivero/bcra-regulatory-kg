# Estimación anclada — extracción E1-solo ESQ-2 (762 unidades)

Generado: 2026-09-01T10:08:56 · Modelo: claude-haiku-4-5 · Tarifas:
1,00 / 5,00 / 1,25 / 0,10 USD/MTok (`runner_corpus.py:76-78`).

## Anclas (producción, 1769 usages reales)

| factor | valor |
|---|---|
| t_in (tok/u) | 1203.17 |
| t_out (tok/u) | 995.51 |
| t_cr (tok/u) | 9960.43 |
| prefijo (tok/escritura) | 9983 |
| escrituras en producción | 4 de 1769 llamadas |

## Ajuste por tamaño (chars reales del mensaje de usuario)

media producción 2332 chars → media ESQ-2
1289 chars → **ratio 0.5530**.
t_in × ratio; t_out × max(1, ratio) (cota conservadora); t_cr sin escalar.

## Aritmética (fórmula D2)

- marginal/u = (665.3×1,00 + 995.5×5,00 + 9960.4×0,10)/1e6
  = USD 0.006639
- 762 × marginal/u = **USD 5.0589**
- escrituras: tasa producción 0.00226 × 762 → 2 escrituras
  × 9983 tok × 1,25/1e6 = **USD 0.0250**

## Resultado

| | USD |
|---|---|
| estimado | **5.0838** |
| estimado × margen 1.2 | **6.1006** |
| estimación gruesa del laudo | 5,50 |
| tope duro de la unidad | 6.50 |

Cabe en el tope: **SÍ**.
El freno real durante el gasto es el tope duro cableado en el cliente
(proyección pre-llamada) más el chequeo de proyección por TO del runner.
