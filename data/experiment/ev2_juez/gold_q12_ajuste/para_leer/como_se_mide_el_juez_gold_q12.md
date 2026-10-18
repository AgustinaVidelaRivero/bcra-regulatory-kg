# Cómo se mide el juez con el gold de Q12, mitad de ajuste (mesa, §128, 16/10/2026)

Fijado antes de que la autora lea. Lo que dice la decisión está marcado como tal. Lo que propone la mesa va como PROPUESTA DE LA MESA, y
la autora lo confirma antes de que se cruce nada.

## Qué se compara

- **Del lado del juez:** sus veredictos de EV2 sobre estas mismas 20 respuestas base, que ya existen y no se pagan. Son el modal de sus
  tres repeticiones por criterio (`modales`), el veredicto de la respuesta (`veredicto_pregunta`) y la clasificación modal
  (`clasificacion_respuesta_modal`), por id opaco (`data/experiment/ev2_fidelidad_eval/out/veredictos_agregados_ciego.json`). El juez es
  `claude-sonnet-4-6` con el prompt v1 congelado (`fd446f8e…`).
- **Del lado de la autora:** las dos planillas de esta carpeta.
- **El cruce:** la mesa lo hace después de que la autora entregue las planillas, abriendo la clave del sorteo
  (`clave_para_despues/sorteo_gold_q12_ajuste_CLAVE_mesa.json`). Antes, nadie mira los veredictos de esas 20.

## Las cifras

1. **Acuerdo por criterio,** sobre los 82 pares (respuesta, criterio): mismo veredicto del juez y de la autora. Se da como fracción,
   con su Wilson al 95 %.
2. **Acuerdo por respuesta,** sobre las 20: mismo veredicto de la respuesta (correcto, parcial o incorrecto). El de la autora sale de sus
   criterios con la misma regla del juez (`data/experiment/ev2_juez/mapping.py:40-54`).
3. **Las dos direcciones del error,** por criterio y por respuesta, como en la muestra simétrica de EV2
   (`data/experiment/ev2_reporte/reporte_ev2.md:291-296`):
   - A: el juez acredita lo que la autora no (juez «cumplido», autora «no_cumplido»);
   - B: el juez no acredita lo que la autora sí (juez «no_cumplido», autora «cumplido»).
4. **La clasificación abstención o contenido:** acuerdo sobre las 20.
5. **Lo que se informa aparte,** con su lista de pares:
   - los criterios marcados «dudosa para mí», «necesita experto del dominio» o «criterio mal planteado»;
   - los errores fuera de los criterios;
   - los minutos.

## Lo que propone la mesa, para confirmar antes del cruce

**PROPUESTA DE LA MESA: el «dudoso» del juez.**
- En el acuerdo por criterio, un «dudoso» del juez cuenta como desacuerdo, y se informa aparte cuántos hubo.
- En el acuerdo por respuesta, su «requiere_adjudicacion» cuenta igual.
- **El porqué:** la vara mide lo que el juez decide solo. En B6.3, lo que deja dudoso va a la autora (registro, §9), así que también se
  da la cifra sin esos pares, para ver cuánto le cuesta a ella.

**PROPUESTA DE LA MESA: las marcas de la autora.**
- La cifra principal va sobre los 82 pares, con todas las marcas adentro.
- Al lado, la misma cifra sin los pares marcados «necesita experto del dominio» o «criterio mal planteado».

## Lo que esta mitad no decide

- **En esta mitad no hay umbral:** sirve para ajustar el juez.
- **El criterio de aceptación rige en la mitad de verificación,** las 20 de A2.2. Es Wilson inferior de al menos 0,85 por criterio y al
  menos 18 de 20 por respuesta; si no se cumple, la mesa frena y la autora decide
  (`docs/registro_decisiones_calidad_y_evaluacion_2026-10-15.md:298-299`).
- **Como referencia, no como criterio:** con 82 criterios, Wilson inferior 0,85 pide 77 de 82 (0,8651); con 76 da 0,8494.

## Cómo se usa para ajustar

- Los desacuerdos se leen por dirección y por criterio.
- **Si el juez cambia,** es una versión nueva del prompt, nunca un ajuste silencioso del v1 (`data/experiment/ev2_juez/prompt_juez_v1.md:1-5`).
  Los calibradores entran solo por laudo de la autora, como casos resueltos (caso, veredicto y porqué), nunca como reglas declarativas
  (`prompt_juez_v1.md:69-73`).
- **El prompt nuevo corre solo sobre estas 20,** con un tope chico y desde la terminal de la autora, con el envoltorio de la clave (diseño
  de la §108, condición 1).
- **Si un calibrador sale de estas 20,** la cifra del juez nuevo sobre ellas ya no es independiente. Por eso la verificación va sobre las
  de A2.2.
- **El juez se congela antes de firmar el pre-registro de A2.2:** el de EV2 tal cual, o el ajustado (diseño de la §108, condición 2).
