# Acta de las adjudicaciones de A2.2 de la autora (A-D8)

26/10/2026. Mesa, §279 de su hoja de ruta; registro de decisiones del 15/10/2026, §121. USD 0, sin API.

**Qué es.** La decisión A-D8 del pre-registro de A2.2: el juez deja en `requiere_adjudicacion` las respuestas que no decide, y la autora
las adjudica al final, sin re-corrida, declarado. Esta carpeta trae su adjudicación y lo que la hace reproducible.

**El material** (`para_leer/`), armado por la mesa el 26/10/2026 a las 11:02:50 con `codigo/armar_adjudicaciones_a2_2_mesa.py`, desde HEAD
y con el molde de la adjudicación ciega de la tanda 0: 8 fichas y 33 criterios. La ficha no dice el brazo, la repetición, el id opaco ni lo
que dijo el juez. Las fuentes de las fichas, los PDF de los TOs, no se copian: sus sha256 están en la clave.

**La lectura** (`lectura/`): la autora marcó cada criterio, cumplido o no cumplido, contra el PDF y la cita del gold, y selló su planilla
el 26/10/2026 a las 14:28:58 con `para_leer/sellar_planilla_adjudicacion_a2_2.py`. Lo declaró, tal cual: «Las marcas son mías, decididas a
ciegas.» La clave (`clave/`), que dice qué respuestas lleva cada ficha, quedó en el paquete de la mesa hasta ese sello.

**La conversión** (`codigo/convertir_marcas_adjudicacion_a2_2_mesa.py`): el veredicto de cada ficha sale de sus marcas por el mapping §2
de EV2 (`ev2_juez/mapping.py`, `veredicto_pregunta`, el de HEAD), y va a cada id opaco de la ficha. Sale `veredictos_adjudicacion_a2_2.json`
(`{id_opaco: veredicto}`), que lee `analizar_a2_2.py --adjudicaciones`.

**Los controles de la mesa** (`codigo/controlar_y_convertir_adjudicaciones_a2_2_mesa.py` y su consola, 7 de 7), sin abrir ninguna marca ni
ninguna observación:
- el sello da el sha256 y los bytes de la planilla, y su hora es la que dio la autora;
- el material de la carpeta de la autora es, byte a byte, el que rehace el armador desde HEAD, y la clave rehecha es la de la mesa;
- 8 ids opacos, de las 8 fichas; cada uno es una respuesta que el juez dejó en `requiere_adjudicacion` en los agregados ciegos de HEAD,
  que traen 9. La que queda no lleva ficha por la regla del armador: su par se decide sin ella;
- el repo, igual antes y después.

**El manifiesto** (`manifest_adjudicacion_a2_2_mesa.txt`) da el sha256 de cada archivo de la carpeta.
