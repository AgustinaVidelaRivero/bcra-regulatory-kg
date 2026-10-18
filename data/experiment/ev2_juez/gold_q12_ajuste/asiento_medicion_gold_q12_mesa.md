# Cómo se mide el juez con el gold de Q12: lo que confirmó la autora y la cifra que sumó (mesa, §129, 16/10/2026)

Decisiones recibidas a las 14:04:04, antes de que la autora lea. Completan `decisiones_128_mesa/gold/para_leer/como_se_mide_el_juez_gold_q12.md`
(sha256 en el manifiesto del gold, `decisiones_128_mesa/gold/manifest_gold_q12_ajuste_mesa.txt`), que no se edita: la autora ya copió la
carpeta de lectura.

## Las dos propuestas, confirmadas tal cual

«Confirmo las dos propuestas de como_se_mide_el_juez_gold_q12.md, tal cual: el «dudoso» del juez cuenta como desacuerdo, con la cifra sin
esos pares al lado; y la cifra principal va con todas mis marcas, con la misma cifra sin las marcadas «necesita experto del dominio» o
«criterio mal planteado» al lado.»

## La cifra que suma la autora

«después de que entregue las planillas, decí cuántas de las 20 respuestas llegaron a mi adjudicación en EV2 y da las cifras principales
también sin ellas. Se calcula después de mi lectura, así que no me sesga.»

Cómo la calculo, fijado ahora, antes de la lectura:
- **Cuáles cuentan:** una de las 20 llegó a la adjudicación de la autora si su veredicto definitivo en EV2 salió por la vía
  `adjudicacion_base`: el juez la dejó para adjudicar, y la autora adjudicó esa misma respuesta. Son 21 de las 120
  (`data/experiment/ev2_reporte/reporte_ev2.md:101-105`). La vía de cada respuesta sale de los veredictos definitivos de EV2
  (`data/experiment/ev2_adjudicacion/adjudicacion/veredictos_definitivos_ciego.json`, `definitivos`, por `id_opaco_base`). Se toma con la
  regla del recómputo del reporte (`data/experiment/ev2_reporte/code/recomputo_ev2.py:132`, `:176`, `:218`), corrido sobre una copia.
- **Aparte, sin restarlas:** las de la vía `adjudicacion_s7`. Ahí la autora adjudicó re-corridas de la misma pregunta y el mismo
  grafo, no la respuesta de la ficha.
- **Las cifras principales sin ellas:** el acuerdo por criterio y el acuerdo por respuesta, con sus dos direcciones, sobre las que
  quedan. Cada una va al lado de la de las 20.
- **Cuándo:** la vía se abre después de que la autora entregue las planillas llenas y selladas, junto con la clave del sorteo. Antes, nadie
  la mira.

## Dónde llena las planillas

- En una copia, en `~/INGENIERIA IA/TESIS/fuera_del_repo/gold_q12_ajuste/`, para no tocar el paquete de la mesa.
- La autora avisa cuando estén llenas y selladas. Hasta entonces, la mesa no abre esa carpeta.

## El commit

- Va cuando el repo esté libre. Si llega el FRENO T1 antes, va primero.
