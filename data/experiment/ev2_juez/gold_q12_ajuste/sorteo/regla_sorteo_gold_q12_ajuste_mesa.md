# La regla del sorteo de la mitad de ajuste del gold de Q12 (mesa, §128, 16/10/2026)

Pedido de la autora recibido a las 13:28:14: las 20 respuestas de EV2, con semilla nueva, sellada antes de armar las fichas, y
estratificada como la diseñó la mesa. La decisión de fondo está en el registro, §9 (`docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md:294-299`).
El diseño es el de la mesa del 15/10/2026 (`decisiones_108_mesa/preguntas/gold_del_juez_en_dos_mitades_mesa.md`, condición 1).

Esta regla y su script (`sortear_gold_q12_ajuste_mesa.py`) se sellan antes de correr el sorteo: su sha256 y la hora van a
`sello_sorteo_gold_q12_mesa.txt`, y la copia permanente del paquete los guarda antes de que el script corra sobre los datos reales.

## La población

- Las 120 respuestas base de la fase 2.3 de EV2: 40 preguntas por tres grafos, con N = 1
  (`data/experiment/ev2_fidelidad_eval/desanonimizacion/tabla_id_opaco.json`; trazas en
  `data/experiment/ev2_corrida/trazas/ev2_base_{run3,v3,v2}/`).
- Menos las 12 de la muestra simétrica de EV2, que la autora ya leyó y adjudicó a ciegas
  (`data/experiment/ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.json`). Del archivo se lee solo `id_opaco_base`.
- Quedan 108.
- No entran las re-corridas del encadenamiento (§7 de EV2): son otras respuestas a las mismas preguntas.

## Los estratos

- **Por TO**, con la dosificación de EV2 (ext 16, cap 8, cla 6, ric 5 y pro 5 de 40). Sobre 20, por restos mayores: ext 8, cap 4, cla 3,
  y ric y pro 2,5 cada uno. El empate de restos lo rompe la semilla: uno de los dos recibe 3 y el otro 2.
- **Por grafo:** KG-Base, KG-Refinado y KG-Reextraído, con 7, 7 y 6. El grafo que recibe 6 sale de la semilla.
- **Las celdas:** en cada TO, la cuota se reparte entre los tres grafos lo más parejo posible, con una diferencia de 1 como mucho. Lo
  que sobra de la parte pareja va a los grafos con más cuota pendiente; los empates los rompe la semilla. Los TOs con más sobrante van
  primero.

## Las respuestas

- **Una pregunta entra una sola vez:** son 20 preguntas distintas, la mitad de las 40, y cada una con la respuesta de un solo grafo.
  Así la lectura cubre más preguntas y ninguna se lee dos veces.
- **En cada TO**, los lugares de las celdas se recorren en un orden de la semilla. Cada lugar toma la primera pregunta de una permutación
  de la semilla que todavía no se usó y cuya respuesta en ese grafo no está en la muestra simétrica.

## El orden y los nombres

- Las 20 fichas van en un orden de la semilla, con ids G01 a G20. Ni el id ni el orden dicen el grafo ni el TO.
- La clave (ficha → id opaco, pregunta, grafo) va a `clave_para_despues/`, aparte de lo que la autora lee.

## La semilla

- `gold-q12-ajuste-ev2-v1`. Cada paso usa su propio generador de esa semilla (`random.Random("<semilla>|<paso>")`): el empate de TOs,
  el grafo con 6, las celdas, la permutación de preguntas y el orden de los lugares de cada TO, y el orden de las fichas.

## La prueba en seco

- El script corrió antes del sello sobre entradas sintéticas con la misma forma: 40 preguntas con la misma dosificación, 120 respuestas
  y 12 excluidas, 4 por grafo. Dio 20 fichas con 20 preguntas distintas, y las cuotas y las celdas cumplen la regla.
- Las cuotas por TO, por grafo y por celda dependen solo de la semilla y de la estructura, no de los datos. Por eso la prueba en seco ya
  las mostró: ric 3 y pro 2, y KG-Base con 6. Qué preguntas y qué respuestas entran depende de los datos reales, y eso no se vio antes
  del sello.

## Lo que se declara

- Casi no hay régimen informativo: de los cinco TOs de EV2, solo ric.
- Son respuestas de otro agente y de otros grafos que los de la tanda 1.
- Parte de las 108 pasaron por la adjudicación de la autora en EV2: 21 respuestas base llegaron a ella como `requiere_adjudicacion`
  (`data/experiment/ev2_reporte/reporte_ev2.md:101-105`, `adjudicacion_base`). La regla no las excluye, porque el diseño excluye solo la
  muestra simétrica. No miro cuáles de las 20 son: para saberlo, tendría que abrir las vías de cada respuesta, que vienen del veredicto
  del juez.
