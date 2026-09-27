# Enmienda 2 a la regla de clasificación por tipo — preguntas con dos anclas

**FIRMADO por la autora — 2026-09-27** · Fecha: 2026-09-27.

Enmienda con fecha a `regla_tipo_pregunta_v2.md` (FIRMADA por la autora el
2026-09-26, sellada en `41abf18`, sha256
`ef5c9aa692cb1e1b1de4c56c569864d16f190f52eb441fbdd94ebb7b978b5e0a`). La regla
v2 **no se edita**: esta enmienda vive al lado, como la Enmienda 1 vive dentro
de la v1 y la interpretación v2 al lado de ella, y se lee junto con las dos.

## 1. Lo que la regla dice hoy, transcrito tal como está

Tipos (regla v1 transcrita en la v2, líneas 24-27):

> - dato directo: todos los criterios de la pregunta se satisfacen con el texto del punto ancla.
> - varios puntos: al menos un criterio exige contenido que no está en el punto ancla sino en otro punto, al que el ancla remite o no.
> - abstención: la respuesta correcta, según los criterios, es que la norma no lo prevé o que no hay dato.
> - dudoso: no se puede decidir entre los anteriores con el material permitido; se anota el motivo y no se fuerza.

Enmienda 1 (v1, línea 43): «El punto ancla comprende sus subpuntos: todo
punto cuya numeración empieza con la del ancla seguida de un punto […] forma
parte del texto del punto ancla a los fines de esta regla. «Otro punto» es
todo punto que no cumple esa condición.»

Interpretación v2 (línea 51): «Un criterio que pide una remisión tal como el
ancla la enuncia no exige el contenido remitido. Que el ancla remita a otro
punto no cambia el tipo de la pregunta si ningún criterio pide ese contenido.»

La regla habla siempre de «el punto ancla», en singular. No dice qué es «el
punto ancla» cuando la pregunta declara dos anclas.

## 2. Texto nuevo — decisión de la autora del 27/09/2026

**Enmienda 2.** Cuando una pregunta declara dos anclas, cada ancla es un
punto distinto; la pregunta es de varios puntos si algún criterio exige el
contenido de la segunda.

## 3. Motivación: hallazgo del control U-EV2-TIPO-T0

En la clasificación de las 20 preguntas de la tanda 0 (hoja
`data/experiment/ev2_tanda0/preguntas/tipo_pregunta_hoja_tanda0.csv`, sha256
`e8a7fdfe…`; control `control_v2_tanda0_2026-09-27/tipo_pregunta_control_tanda0.json`,
sellado en `c23897f`; clasificación de la autora sellada en `2231c13`), el
control del modelo bajo la regla v2 acordó con la autora en 14 de 20. Cinco
de los seis desacuerdos son exactamente las cinco preguntas con dos anclas
(T0F-001, T0F-007, T0F-011, T0F-015, T0F-017): la hoja presenta los dos
textos bajo «Ancla» y «Texto del ancla», y el modelo leyó la unión de los dos
como «el punto ancla», con notas del tipo «ambos puntos son anclas
declaradas, por lo que todo el material está en el texto del ancla»; cuatro
las clasificó dato directo y una, dudoso. La autora las clasificó varios
puntos con fundamento en la regla (criterios repartidos entre puntos
hermanos, ninguno subpunto del otro) y la adjudicación
(`tipo_pregunta_adjudicacion_tanda0.csv`) fijó ese tipo final. El sexto
desacuerdo (T0F-013, abstención contra dato directo) es de otra naturaleza y
no motiva esta enmienda.

El desacuerdo es sistemático y explicable por un hueco de la regla, no por
un error del modelo ni del control: la regla se escribió para preguntas de
una sola ancla.

## 4. Alcance

- Rige para la clasificación del **conjunto final de B6.3 (a)** y de todo
  conjunto nuevo que se clasifique después de su firma.
- **La clasificación de la tanda 0 ya está adjudicada y no se recalcula**:
  su tipo final es el de `tipo_pregunta_tanda0.json`, sellado con la
  adjudicación de la autora, y esta enmienda no lo modifica.
- El control del modelo de U-EV2-TIPO-T0 no se re-corre: su resultado queda
  como hallazgo registrado.

## 5. Qué no cambia

- La regla v1, su Enmienda 1 y la interpretación v2, que siguen valiendo
  para preguntas de una sola ancla.
- El procedimiento: hoja a ciegas, clasificación de la autora, control del
  modelo, comparación y adjudicación.
- Las clasificaciones selladas de EV2 (40 dato directo) y de la tanda 0.

## Firma

Firmada por la autora el 2026-09-27.
