# Resumen final — re-corrida del control de instrumento (P1′, U-ESQ-1d)

Corrida del 31/08/2026 bajo la adenda sellada
`adenda_prerregistro_esq1_P1bis.md` (commit e68e861), con el manifiesto de
dopadas aprobado por la autora en el freno (b) — un reemplazo respecto de la
versión presentada (la cláusula de `ext::3.17.3.5` pasó de definir una
categoría de persona a definir un valor, para eliminar el canal vecino
`sujeto_propuesto`). Selftest previo 37/37 PASS
(`code/selftest_control_esq_p1bis.py`). Modelo `claude-haiku-4-5`, prefijo
abierto nuevo `d923bf876580` (description del tool corregida), namespace
`e1_extraccion|cv=e1-extractor-v1-pd923bf876580|think=0`, db propia
`cache/esq_control_p1bis.db`.

## 1. Resultado contra P1′ — FALSADA

| Brazo | Conteo | Umbral (adenda §4) | Veredicto |
|---|---|---|---|
| A′ total | **0/10** | ≥7 de 10 | **NO pasa** |
| A′ mitad tipo | **0/5** | ≥3 de 5 | NO pasa |
| A′ mitad predicado | **0/5** | ≥3 de 5 | NO pasa |
| C (tipo propuesto) | **0/10** | ≤1 de 10 | pasa |

Recomputo independiente (lectura directa del jsonl, sin comun_control_esq):
0 `tipo_propuesto`, 0 `predicado_propuesto`, 0 `sujeto_propuesto`, 0
contenedores no-lista, 0 errores, `stop_reason=tool_use` en las 20.

```
.venv/bin/python3 -B data/experiment/esq/code/runner_control_esq_p1bis.py --solo-resumen
```

## 2. Qué emitió cada dopada (todas: forzada al esquema, ni una omisión)

En las 10/10 el modelo LEYÓ la cláusula plantada y la extrajo — encajándola
en el esquema cerrado; el canal no disparó ni una vez.

Mitad tipo — qué tipo recibió el contenido plantado:

| dopada | concepto plantado | destino en el crudo |
|---|---|---|
| dop::tipo::cap::8.3.2.4 | sanción de multa | **Excepcion** «Incumplimiento condiciones punto» |
| dop::tipo::cla::6.5.2.1 | presunción legal | **Restriccion** «Presunción capacidad pago — atrasos menores 30 días» |
| dop::tipo::ext::3.17.3.5 | definición de un valor | **Obligacion** «Valor referencia ajustado — promedio cambios» |
| dop::tipo::pro::1.1.1 | vigencia diferida | **Obligacion** «Entrada en vigencia — ciento ochenta días» |
| dop::tipo::ric::8.1.2 | facultad discrecional | **Obligacion** «SEFyC adecúa porcentaje — evolución mercado» |

Mitad predicado — el patrón es uniforme: la relación plantada se
**nominaliza** como entidad (Obligacion) y se conecta con predicados VÁLIDOS:

| dopada | relación plantada | destino en el crudo |
|---|---|---|
| dop::predicado::cap::2.5.5 | equivalencia Op→Op | Obligacion «Equivalencia — pase pasivo…» + establecida_en, aplica_a |
| dop::predicado::cla::6.5.3.3 | complementa (deber→deber) | Obligacion «Revisión clasificación — complementa sin sustituir…» + establecida_en |
| dop::predicado::ext::6.5.2 | asimilación Op→Op | Obligacion «Asimilación operaciones cambio sucursales» + establecida_en, regula |
| dop::predicado::pro::3.2.3.6 | acredita cumplimiento | Obligacion «Conservación documentación acredita…» + establecida_en, aplica_a |
| dop::predicado::ric::10.1.1 | cómputo conjunto | Obligacion «Cómputo conjunto con régimen de Supervisión» + establecida_en |

Sobre las tres observaciones registradas por la mesa en el freno: (1) la
sanción efectivamente se re-expresó dentro del esquema — el hallazgo del
brazo B repitiéndose — aunque no como Obligacion condicionada sino como
Excepcion (tipado semánticamente erróneo, no solo caja vecina); (2) la
facultad NO cruzó de canal (no emitió `predicado_propuesto`): forzó
Obligacion; (3) equivalencia y asimilación se comportaron idéntico
(nominalización), consistente con su correlación declarada — pero las otras
tres sondas de predicado, no correlacionadas, hicieron exactamente lo mismo.

Este documento no interpreta más allá del conteo; consecuencia sellada en la
adenda §4: con A′ fallado y la description corregida, la hipótesis viva es la
competencia del lenguaje de cierre, y el paso siguiente declarado es O2
(neutralizar los tres cierres en modo abierto) — **otra unidad, otra
decisión**. Los umbrales no se ajustan post-hoc.

## 3. Gasto — dentro del tope, fuentes cruzadas

- Estimación anclada previa: USD 0,1868 (`estimacion_control_esq_p1bis.md`).
- Gasto real: **USD 0,183624** — idéntico desde la db (20 misses, namespace
  único `…pd923bf876580…`) y desde el jsonl (`fuentes_cruzan: true`;
  `code/gasto_control_esq_p1bis.py`). Tope parcial 0,50: no tocado.
- Tokens: in 24.487 / out 25.075 / cache write 10.718 (una escritura) /
  cache read 203.642.

## 4. Recargo D7 re-medido bajo el prefijo nuevo y re-presupuesto de ESQ-1

Sobre las 20 unidades de esta corrida (sesgo declarado en el resumen json:
el pareado usa el usage cerrado de las 20 unidades BASE, y las 10 dopadas
exceden a su base en la cláusula plantada; pool distinto del control
original — 10 limpias + 10 limpias dopadas, no 40 por patología):

- r_open medido: 0,0085113 USD/u · prefijo abierto medido: **10.718 tok**
  (cerrado: 9.983).
- Recargo **global** (vs r_marg producción 0,0071768): **+0,0013345 USD/u**
  (+18,6 %). Re-presupuesto ESQ-1 (762 u): **USD 6,51**.
- Recargo **pareado** (vs las mismas 20 en cerrado, 0,0082002):
  **+0,0003111 USD/u** (+3,8 %; Δout pareado +43,25 tok/u).
  Re-presupuesto: **USD 5,73**.
- Ambas lecturas quedan bajo el tope D6 de USD 9,00. La elección de lectura
  es de la autora (D7).

## 5. Producción intacta

Post-corrida: `git status` limpio en `corpus_v2/salida/`, `grafo_v2/kg.json`,
`evaluacion/`, runs sellados y `posthoc_run/`/`frozen_run/`. La db del
control original (`cache/esq_control.db`) no recibió escrituras (la
re-corrida usó db propia); el modo cerrado sigue byte-idéntico por los
candados sha256 del selftest.

Artefactos primarios: `extracciones_control_esq_p1bis.jsonl` (20 líneas),
`resumen_control_esq_p1bis.json`, `orden/seleccion_control_esq_p1bis.json`,
`dopadas_p1bis.json` (aprobación registrada), `manifiesto_dopadas_p1bis.md`.
