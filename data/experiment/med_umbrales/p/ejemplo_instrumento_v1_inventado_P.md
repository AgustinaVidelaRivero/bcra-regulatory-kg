# Ejemplo inventado del instrumento v1 (no es del marco)

Un nodo, un texto y un elemento inventados, para ver el formato: la ficha del paso 1, su bloque del formulario, el bloque de la pertinencia y el de las diferencias. La página del PDF no existe.

---

# Ficha L9-01 (lote 9, 1 de 1)

- Id de la ficha: `bpynkg`

## Texto de la unidad de E0 (la referencia)

Unidad `inv::9.9.9`, «Punto inventado», páginas [1]. PDF: `data/experiment/escalado_prep/pdfs/inventado.pdf`.

La cuantía a juzgar va entre ⟦ ⟧.

**Texto propio** (páginas [1])

> 9.9.9. Las entidades inventadas no podrán superar el ⟦5 %⟧ de su capital inventado, salvo lo previsto en el punto 6.3.2.2. El plazo será de 30 días corridos y el importe mínimo es 5 veces el importe de referencia.

## Página del PDF

![inv, página 1](../paginas/inv_p1.png)

## Paso 1

Se responde en el formulario del lote (`formulario_paso1_lote9.md`), bloque L9-01 · `bpynkg`: los campos de la cuantía resaltada, sin la pertinencia, que se juzga primero en el paso 2 (C7).

---

# Formulario del paso 1 (ejemplo)

Paso 1 (regla v1, §5): se responde desde la norma, con la ficha del mismo número, sin ver los campos del grafo. Se califican los campos de la cuantía resaltada; la pertinencia no va en este paso, porque se juzga primero en el paso 2 (C7). Se llena reemplazando «______». La regla de calificación es la v1 (`regla_calificacion_v1.md`). Un campo que no se puede decidir va en `no_decidible`, con su motivo; la nota es libre (C26).

## L9-01 · `bpynkg`

- valor [número con punto decimal y sin separador de miles («1.25», «5000000000»), o «sin valor»]: ______
- unidad [porcentaje | moneda | dias | meses | anios | veces | uva | horas | semanas | sin unidad | otra: <cuál>]: ______
- moneda [ARS | USD | EUR | no nombra | no aplica]: ______
- tipo_de_dias [habiles | corridos | sin tipo | no aplica]: ______
- comparacion [maximo_inclusivo | maximo_estricto | minimo_inclusivo | minimo_estricto | igual | coeficiente | no_determinada]: ______
- palabras_de_la_comparacion [las palabras de la norma que fijan el sentido, literales, o «ninguna»]: ______
- base [el tramo exacto de la base, o «sin base»]: ______
- destino_de_la_base [<to>::<punto> | definicion: <término> | remision generica | destino multiple: <uno>; <otro> | no remite | no aplica]: ______
- no_decidible [no | sí: <motivo>]: ______
- nota [libre]: ______
- hora_inicio [hh:mm]: ______
- hora_fin [hh:mm]: ______

---

# Paso 2, lote 9, primera parte: la pertinencia (U-MED-UMBRALES, etapa P, regla v1)

Se juzga primero (C7), con lo que muestra cada bloque: la etiqueta del nodo, los tramos de E1, lo que la ficha resaltó y la cuantía guardada de cada elemento del nodo. Los valores del grafo de los demás campos llegan después, en la segunda parte, con la pertinencia ya sellada. Se llena reemplazando «______»; la nota es libre (C26). Los elementos vacíos (§2.5) no tienen esta parte.

## L9-01 · `bpynkg`

- Etiqueta del nodo: «Regla inventada para el selftest»
- Tramos de umbral que E1 devolvió para el nodo:
  1. «no podrán superar el 5 % de su capital inventado» ← el del elemento
- Lo que la ficha resaltó: «5 %»
- Elementos del nodo, en el orden del grafo (la cuantía guardada de cada uno):
  1. «5 %» ← este elemento
  2. «30 días»
- pertinencia [pertinente | no pertinente | inexistente | duplicado]: ______
- nota [libre]: ______

---

# Paso 2, lote 9, segunda parte: diferencias entre la lectura y el grafo (U-MED-UMBRALES, etapa P, regla v1)

Solo las diferencias, con el valor del grafo a la vista. En cada una: la clasificación con el §2.3 (correcto | contradicho | omitido | espurio | parcial | no aplica | no decidible); en una comparación omitida, también de implementación | de la definición; si la diferencia es un error del paso 1, `corrijo_mi_paso_uno_<campo>: sí: <motivo>`, que se registra y se cuenta. Cada fila lleva su nota, y cada ficha una nota más (C26).

## L9-01 · `bpynkg`
- **valor**: grafo «5», paso 1 «6»
  - clasificacion_valor [correcto | contradicho | omitido | espurio | parcial | no aplica | no decidible]: ______
  - corrijo_mi_paso_uno_valor [no | sí: <motivo>]: ______
  - nota_valor [libre]: ______
- **unidad**: grafo «porcentaje», paso 1 «horas»
  - clasificacion_unidad [correcto | contradicho | omitido | espurio | parcial | no aplica | no decidible]: ______
  - corrijo_mi_paso_uno_unidad [no | sí: <motivo>]: ______
  - nota_unidad [libre]: ______
- nota_de_la_ficha [libre]: ______

