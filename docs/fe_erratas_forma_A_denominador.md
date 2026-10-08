# Fe de erratas — el denominador de la forma A («42 de 715»)

**Estado: aprobada por la autora el 08/10/2026** (decisión sobre el barrido de límites declarados de la mesa). Redactada por la mesa
revisora, que originó el error y lo asume. Detectado por el barrido de límites del 08/10/2026 y verificado por la mesa contra el código
que produce la cifra.

## El hecho

Desde el 06/10/2026, la forma A del vínculo entre unidades (Condicion de ítem que conserva la norma que condiciona en el encabezado de
un ancestro, sin arista hacia ella) figura como **42 de 715 Condicion de ítem (0,059; Wilson al 95 % [0,044; 0,078])**. El denominador
está contado dos veces.

La fuente es el control 3.e de T3 de U-REEXT-T0 (`data/experiment/reext_t0/t3bis/salida/controles_t3bis.json`, `e_forma_A.conteos`):
`condicion_de_item` 601, `sin_condicion_de` 114, `forma_A_encabezado_con_nodos_destino` 42. El código que cuenta
(`e_forma_A` de `controles_t3.py`, el mismo que `data/experiment/sincola_t0/sc1/controles_sc1.py:292-327`) suma 1 a
`condicion_de_item` por cada Condicion de ítem y, dentro de ese conjunto, 1 a `sin_condicion_de` si no tiene la relación. Las 114 son un
subconjunto de las 601, y la partición cierra adentro: 42 + 31 + 2 = 75 sin `condicion_de` ni rechazo, y 75 + 39 rechazadas = 114. El
715 es 601 + 114.

La cifra correcta, con Wilson al 95 %:

| grafo | forma A | Condicion de ítem | fracción | Wilson al 95 % |
|---|---|---|---|---|
| diez r2b completo (`a9631a64`) | 42 | 601 | 0,070 | [0,052; 0,093] |
| diez r2b sin cola (`e22fae1a`) | 42 | 575 | 0,073 | [0,054; 0,097] |

El 575 sale de la nota del 06/10/2026 al pie de `docs/mandatos/USINCOLA_T0_grafo_evaluado_sin_cola.md` (revisión del FRENO SC1-bis), que
da para el grafo sin cola los mismos dos contadores, 575 y 113, con los mismos 42 casos. El FRENO T3 de la instancia informaba la forma A
sobre otra base, «42 de 75» (las Condicion de ítem sin `condicion_de` ni rechazo; `data/experiment/reext_t0/freno_t3.md:19`), que es
correcta.

## Cómo se originó

El «715» entró con los asientos de la mesa del cierre de U-REEXT-T0 (`0a3ac81`, 06/10/2026), que sumaron los dos contadores del JSON
como si fueran disjuntos. Ese mismo día, la nota de la mesa sobre el FRENO SC1-bis explicó el 715 como esa suma sin advertir que uno
contiene al otro. Error propio de la mesa: una cifra con ancla, pero con la suma de dos campos que no se leyó contra el código que los
produce.

## Dónde se propagó y cómo se corrige

- `docs/insumos_escritura.md` §7, ítem 3 (`:323-324`) y ítem 6 (`:407`): corregido en el lugar, con la marca de la corrección.
- `docs/checklist_pre_escalado.md`, condición 6 (`:81`): corregido en el lugar, con la marca. La condición sigue cumplida: se declaró
  límite con la cifra, y la cifra corregida no cambia la decisión.
- `docs/mandatos/UDIAG_vinculo.md` (nota del 06/10/2026, `:45-46`): nota fechada al pie.
- `docs/mandatos/USINCOLA_T0_grafo_evaluado_sin_cola.md` (texto firmado, `:94`, y nota del 06/10/2026, `:189-191`): nota fechada al pie;
  el texto firmado no se edita.
- `reports/u_diag_cap3_grafo/REPORTE_UDIAG_CAP3_GRAFO.md:145`: es el reporte de una unidad cerrada (`df59e79`) y no se edita; vale esta
  fe de erratas.

## Qué no cambia

La decisión de la autora del 06/10/2026 (la forma A, límite declarado, sin mandato propio antes de la tanda 1) y la causa (i) de
U-DIAG-CAP3-GRAFO (60 de 953 Condicion de ítem, con otra base) no cambian. La lectura de precisión de los 42 casos sigue pendiente, sin
plazo.
