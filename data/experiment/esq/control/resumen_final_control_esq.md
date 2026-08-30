# Resumen final — control de instrumento de ESQ-1 (U-ESQ-1c, FASE 2)

Corrida del 2026-08-30, 40/40 unidades, sin freno (wall 517,9 s). Fuente de
todo número: `control/resumen_control_esq.json` y
`control/extracciones_control_esq.jsonl` (crudo y validado por unidad, claves
de producción), regenerables con
`runner_control_esq.py --solo-resumen` y `gasto_control_esq.py`.

## 1. Los tres conteos contra sus umbrales sellados

Los umbrales son los de P1 del pre-registro (`prerregistro_esq1.md:31-33`).
**Este documento no interpreta**: la lectura es de la autora con la mesa
(pre-registro §6; mandato U-ESQ-1c.g).

| brazo | resultado | umbral sellado | ¿alcanza? |
|---|---|---|---|
| A (20 con `omisiones_no_prosa`) | **0/20** emiten algún propuesto (0 tipo, 0 predicado) | ≥10 de 20 | **NO** |
| B (10 con presión dominio/rango) | **3/10** reportan la relación | ≥7 de 10 | **NO** |
| C (10 limpias, control negativo) | **0/10** emiten tipo propuesto (0 con cualquier propuesto) | ≤1 de 10 | **SÍ** |

Componentes del brazo B (operacionalización declarada en
`comun_control_esq.reporta_relacion_b`): firma_registrada 3, crudo_aplica_a 3
(las mismas 3 unidades), canal_abierto 0.

Verificación de instrumento (no diagnóstico), hecha con recomputo
independiente del jsonl sin el módulo de conteo:
- 0 disparos de `tipo_propuesto` y 0 de `predicado_propuesto` en el crudo de
  las 40 — los ceros no son un artefacto del contador.
- Las 40 requests salieron con el flag encendido (guardas pre-gasto del
  runner: system = prefijo abierto `bca492bbf7c8`, tool schema con los dos
  campos) y el validado de las 40 lleva la clave `tipo_propuesto` (solo
  existe con `canal_abierto=True`, `validador_e1.py:192-197`).
- Datos observados en la misma corrida, se registran sin leerlos: 19/40
  unidades declararon `omisiones_no_prosa`; 1 disparo de `sujeto_propuesto`
  (canal preexistente). Insumo para la distinción del pre-registro §6
  (canal-no-poblado vs modelo-no-lo-usó), que se hace en revisión, no acá.

## 2. Recargo medido del modo abierto (el dato de D7)

Usage agregado de la corrida (40 llamadas, 0 hits, 1 escritura de prefijo):
in 58.683 · out 61.822 · cache_write 10.583 · cache_read 412.737 tok.

```
r_open_medido = (58.683×1,00 + 61.822×5,00 + 412.737×0,10)/40/1e6
              = (58.683 + 309.110 + 41.273,7)/40e6      = 0,01022667 USD/u

r_marg (producción, 1.769 llamadas, scoping §5.2 recomputado)
                                                        = 0,00717677 USD/u
r_prod_40 (las MISMAS 40 unidades en la corrida cerrada:
           in 58.683, out 57.660, cr 40×9.983=399.320)  = 0,00967288 USD/u

recargo GLOBAL   = 0,01022667 − 0,00717677              = 0,00304989 USD/u
recargo PAREADO  = 0,01022667 − 0,00967288              = 0,00055379 USD/u
```

Descomposición exacta del pareado (misma factorización que scoping §5.2.1):
```
Δoutput   = (1.545,55 − 1.441,50) = 104,05 tok/u × 5,00/1e6 = 0,00052025
Δprefijo  = (10.318,425 − 9.983)  = 335,425 tok/u × 0,10/1e6 = 0,00003354
                                                    suma      0,00055379 ✓
```

Prefijo abierto MEDIDO: **10.583 tok** (una escritura; el supuesto era
10.383, o sea +400 sobre 9.983 — el real es +600). El global arrastra además
el sesgo de selección de las 40 (elegidas por patología, no al azar):
r_prod_40 (0,00967) ya está 35 % sobre r_marg **en modo cerrado**. Se
reportan los dos; cuál usar para D7 es decisión de la autora.

## 3. Re-presupuesto de la corrida de ESQ-1 (D7, 762 unidades)

```
con recargo PAREADO: 762 × (0,00717677 + 0,00055379) + 2 × 10.583×1,25/1e6
                   = 762 × 0,00773057 + 0,02646      = USD 5,9171
con recargo GLOBAL : 762 × 0,01022667 + 0,02646      = USD 7,8192
```
Referencia sellada con el supuesto +10 %: USD 5,9061 (scoping §5.3). Ambas
variantes quedan bajo el tope de D6 (USD 9,00). Vigencia condicionada: el
pre-registro §6 declara el control fallido como resultado NULO del
instrumento; si se rediseña el modo, el recargo se re-mide.

## 4. Gasto real, recomputado desde el usage

```
costo = (58.683×1,00 + 61.822×5,00 + 10.583×1,25 + 412.737×0,10)/1e6
      = (58.683 + 309.110 + 13.228,75 + 41.273,7)/1e6 = USD 0,422295
```
Tarifas: `runner_corpus.py:76-78`; fórmula D2
(`decisiones_caching_extraccion.md:32-42`). Cruce entre fuentes primarias
(`gasto_control_esq.py`): db `esq_control.db` (40 misses) y jsonl dan
tokens idénticos y el mismo USD 0,422295 — `fuentes_cruzan: true`. Contra lo
autorizado: estimación anclada 0,4293 (desvío −1,6 %), presupuesto sellado
0,32 (desvío +32 %, declarado y autorizado antes de correr), tope parcial
0,50 no tocado. Contador del cliente: 0,4223 (redondeo a 4 decimales).

## 5. Contenedores no-lista

**0 de 40.** Ningún registro de la corrida trae `entities`/`relations`
no-lista ni error (`con_error: []`, `stop_reason` = tool_use en las 40).
La regla de reporte (decisión del 28/08) no tuvo nada que reportar.

## 6. Aislamiento verificado post-corrida

- Caché de producción `e1_extraccion.db`: mismos dos namespaces y conteos
  que antes de la corrida (1.769 en `p4793d6152608`, 88 en `p4dd055a4c5e8`);
  cero filas nuevas.
- La corrida entera vive en `esq/cache/esq_control.db`, namespace
  `e1_extraccion|cv=e1-extractor-v1-pbca492bbf7c8|think=0`.
- Log D3: 40 líneas con component `esq_control_e1` en `logs/cache_usage.jsonl`.
