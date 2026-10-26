# La regla de tu adjudicación de A2.2

**Qué es.** Tu decisión A-D8 del pre-registro de A2.2, tal cual: «El disparo de N = 3 usa solo el veredicto del código, y las
requiere_adjudicacion las adjudico al final, sin re-corrida, declarado.» Cada ficha es una respuesta que el juez dejó sin decidir y
de la que depende el veredicto final de su par. Las eligió la mesa por código, con la regla del análisis de A2.2 y el molde de la
adjudicación ciega de la tanda 0 (`docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md`).

**Cómo se marca** (el molde de la tanda 0, decisiones 4 y 5):
1. Ficha por ficha, en el orden de la planilla, contra el PDF del TO (en `fuentes/`) y la cita del gold.
2. Cada criterio, `cumplido` o `no_cumplido`. No hay «dudoso»: la adjudicación decide.
3. La observación es libre.
4. El veredicto de cada ficha no lo ponés vos: sale en código del mapping §2 de EV2 (`ev2_juez/mapping.py`, `veredicto_pregunta`).
   Todos cumplidos da correcto; ninguno, incorrecto; si no, parcial.

**A ciegas:** la ficha no dice el brazo, la repetición, el id ni lo que dijo el juez. Antes de sellar, no abrís la clave del paquete
de la mesa ni ninguna carpeta `SOLO_MESA`.

**Al terminar:** corrés `python3 sellar_planilla_adjudicacion_a2_2.py` en esta carpeta. Sella la planilla con su sha256, sus bytes y su
hora, y no pisa un sello. Después, la mesa convierte tus marcas en los veredictos por id opaco, por código, y el análisis de A2.2
corre con ellos.
