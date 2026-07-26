# Informe — Cierre de la key EV1 (2026-07-26)

**Resultado: swap hecho (sale EV1-037 — cuarto descarte, laudo registrado — entra EV1-040 en la misma posición, con `key_adjudicada` y `estado: "verificada"`); acta actualizada con el cuarto descarte, el laudo de EV1-039 y la nota de adjudicación textual de EV1-040; verificaciones OK.** Sin API, sin commits.

## Swap y verificaciones

```
swap OK en posición 33: sale EV1-037, entra EV1-040 [puntual]
[OK] 36 entradas (hay 36)
[OK] ids únicos
[OK] todas con key_adjudicada + estado=verificada
Mezcla final real: condicional 8 / enumerativa 12 / puntual 10 / sujeto 6
```

La mezcla final queda idéntica a la sellada del protocolo §2 (EV1-037 y EV1-040 son ambas puntuales).

## Mini anti-solapamiento de EV1-040 (top 3)

| top | Score (tok/tri) | Quemada |
|---|---|---|
| 1 | 0.233 (0.108/0.358) | CQ_v2:CQ-047 |
| 2 | 0.225 (0.143/0.306) | CQ_v1:CQ-024 |
| 3 | 0.199 (0.083/0.315) | CQN2:CQN2-010 |

**Registro que requiere tu mirada (evidencia, no veredicto):** la `cita_textual` sellada de CQ-047 contiene VERBATIM el dato de la key de EV1-040 ("discrepancia de más de un nivel … al menos otras dos entidades o fideicomisos … 40 % o más del total informado", 6.6), su primera pata pregunta el mismo interrogante (casos de recategorización obligatoria y consecuencia según proporción), y CQ-047 cubre además el hermano 6.4.4 (banda 20-<40%) que tu nota de adjudicación declara como territorio de sondeo de EV1-040. Diferencia: EV1-040 pide solo los umbrales del 6.6; CQ-047 la cadena completa. Es el tercer caso consecutivo donde la paráfrasis vence al comparador léxico (0.233). Quedó registrado en la adenda del acta; nada se descartó.

## Acta

`acta_adjudicacion_EV1.md` actualizada con la adenda del cierre: cuarto descarte (EV1-037, causa: solapamiento real con CQ-024/CQN2-010b), laudo EV1-039 CONSERVADA (limítrofe-bajo + sonda pre-registrada del control P3), nota de adjudicación de EV1-040 copiada textual ("verificada contra el 6.6; se registra que el corpus contiene el instituto hermano 6.4 (reconsideración, banda 20-<40%) — la pregunta sondea la distinción entre ambos"), y el registro del comparador sobre CQ-047.

**FRENO acá.** Pendientes tuyos: laudo sobre el registro EV1-040↔CQ-047, y el commit de sellado del §7.3.
