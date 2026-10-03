# Ejemplos del mensaje de E1 y de la NOTA de E3 (borrador r2b)

Generado por `p1/ejemplos_mensaje_r2.py`. El sellado sale de `perfil_e1.perfil('v3_b54')` sobre la E0 legada; el nuevo, de `p1/mensaje_r2_borrador.py` sobre la E0 e0-r2 (`f8dedd4`).

## cap::1.2

Mensaje de E1, sellado:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 1.2 — Exigencia básica.
Puntos admitidos para `punto`: 1.2, S1

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_alcance_capmin como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S1]
Sección 1. Capital mínimo.

Texto del punto 1.2:
```
1.2. Exigencia básica.
Según la clase de entidad, serán las siguientes exigencias básicas:
Restantes entidades
Bancos
(salvo Cajas de Crédito Cooperativas)
-En millones de pesos-
5.000 2.500
Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior
deberán observar las exigencias establecidas para los bancos.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 1.2 — Exigencia básica.
Puntos admitidos para `punto`: 1.2, S1

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S1]
Sección 1. Capital mínimo.

TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `cap::tabla000` (columnas): confiable, sin celdas combinadas.

Texto del punto 1.2:
```
1.2. Exigencia básica.
Según la clase de entidad, serán las siguientes exigencias básicas:
[TABLA cap::tabla000 | página 4 | e0_tablas | columnas]
Rótulo: -En millones de pesos-
Columnas: Bancos | Restantes entidades (salvo Cajas de Crédito Cooperativas)
Fila 1: Bancos = 5.000 | Restantes entidades (salvo Cajas de Crédito Cooperativas) = 2.500
[FIN TABLA cap::tabla000]
Las compañías financieras que realicen, en forma directa, operaciones de comercio exterior
deberán observar las exigencias establecidas para los bancos.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: (sin NOTA)

NOTA de E3, nueva: NOTA: esta unidad tiene tablas serializadas por E0 (bloques [TABLA …] … [FIN TABLA …] del texto fuente, verificados contra el documento): su contenido es texto confiable y su omisión se evalúa como la de cualquier otro contenido.

## ric::9.2.1

Mensaje de E1, sellado:

```text
Documento fuente: TO_regimen_informativo_contable_mensual_actual.pdf
TO: ric
Tipo de unidad: chunk de punto
Punto del chunk: 9.2.1 — Incrementos de exigencia
Puntos admitidos para `punto`: 9.2.1, S9, 9.2

Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_entidad_comprendida_reginf como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S9]
Sección 9. Incrementos de exigencia por riesgo de crédito
[encabezado | punto 9.2]
9.2. Modelo de Información

Texto del punto 9.2.1:
```
9.2.1. Incrementos de exigencia
Código Concepto Importe
83100000 Incremento de la exigencia por riesgo de crédito por exceso en la relación
de activos inmovilizados. Información en término
83200000 Incremento de la exigencia por riesgo de crédito por exceso en la relación
de activos inmovilizados. Información fuera de término
83300000 Incremento de la exigencia por riesgo de crédito por exceso en la relación
de activos inmovilizados. Incumplimientos reiterados
83400000 Incremento de la exigencia por riesgo de crédito por exceso en la relación
de activos inmovilizados. Determinado por la SEFyC
83500000 Incremento de la exigencia por riesgo de crédito por exceso en Grandes
Exposiciones al Riesgo de Crédito. Información en término
83600000 Incremento de la exigencia por riesgo de crédito por exceso en Grandes
Exposiciones al Riesgo de Crédito. Información fuera de término
83700000 Incremento de la exigencia por riesgo de crédito por exceso en Grandes
Exposiciones al Riesgo de Crédito. Incumplimientos reiterados
83800000 Incremento de la exigencia por riesgo de crédito por exceso en Grandes
Exposiciones al Riesgo de Crédito. Determinado por la SEFyC
84300000 Incremento de la exigencia por riesgo de crédito por exceso en gradua-
ción del crédito. Información en término
84400000 Incremento de la exigencia por riesgo de crédito por exceso en gradua-
ción del crédito. Información fuera de término
84500000 Incremento de la exigencia por riesgo de crédito por exceso en gradua-
ción del crédito. Incumplimientos reiterados.
84600000 Incremento de la exigencia por riesgo de crédito por exceso en gradua-
ción del crédito. Determinado por la SEFyC.
85600000 Incremento de la exigencia por riesgo de crédito por la tenencia de certifi-
cados o títulos de deuda de fideicomisos financieros. (25 %)
85700000 Incremento de la exigencia por riesgo de crédito por la tenencia de certifi-
cados o títulos de deuda de fideicomisos financieros. (50 %)
85800000 Incremento de la exigencia por riesgo de crédito por la tenencia de certifi-
cados o títulos de deuda de fideicomisos financieros. (100 %)
Incremento de la exigencia por riesgo de crédito por excesos en las parti-
86300000
cipaciones en el capital de empresas (INC )
(Inversiones significativas en empresas)
87100000 Incremento de la exigencia por riesgo de crédito por exceso en financia-
miento al sector público no financiero. Información en término
87200000 Incremento de la exigencia por riesgo de crédito por exceso en financia-
miento al sector público no financiero. Información fuera de término
87300000 Incremento de la exigencia por riesgo de crédito por exceso en financia-
miento al sector público no financiero. Incumplimientos reiterados
87400000 Incremento de la exigencia por riesgo de crédito por exceso en financia-
miento al sector público no financiero. Determinado por la SEFyC
87500000 Incremento de la exigencia por riesgo de crédito por exceso en posicio-
nes de derivados sobre “commodities”. Información en término
87600000 Incremento de la exigencia por riesgo de crédito por exceso en posicio-
nes de derivados sobre “commodities”. Información fuera de término
87700000 Incremento de la exigencia por riesgo de crédito por exceso en posicio-
nes de derivados sobre “commodities”. Incumplimientos reiterados
87800000 Incremento de la exigencia por riesgo de crédito por exceso en posicio-
nes de derivados sobre “commodities”. Determinado por la SEFyC
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_regimen_informativo_contable_mensual_actual.pdf
TO: ric
Tipo de unidad: chunk de punto
Punto del chunk: 9.2.1 — Incrementos de exigencia
Puntos admitidos para `punto`: 9.2.1, S9, 9.2

Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_entidad_comprendida_reginf en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S9]
Sección 9. Incrementos de exigencia por riesgo de crédito
[encabezado | punto 9.2]
9.2. Modelo de Información

TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `ric::tabla022` (columnas): confiable, sin celdas combinadas.
- `ric::tabla023` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque.

Texto del punto 9.2.1:
```
9.2.1. Incrementos de exigencia
[TABLA ric::tabla022 | página 41 | e0_tablas | columnas]
Columnas: Código | Concepto | Importe
Fila 1: Código = 83100000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información en término
Fila 2: Código = 83200000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Información fuera de término
Fila 3: Código = 83300000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Incumplimientos reiterados
Fila 4: Código = 83400000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en la relación de activos inmovilizados. Determinado por la SEFyC
Fila 5: Código = 83500000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información en término
Fila 6: Código = 83600000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Información fuera de término
Fila 7: Código = 83700000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Incumplimientos reiterados
Fila 8: Código = 83800000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en Grandes Exposiciones al Riesgo de Crédito. Determinado por la SEFyC
Fila 9: Código = 84300000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Información en término
Fila 10: Código = 84400000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Información fuera de término
Fila 11: Código = 84500000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Incumplimientos reiterados.
Fila 12: Código = 84600000 | Concepto = Incremento de la exigencia por riesgo de crédito por exceso en gradua- ción del crédito. Determinado por la SEFyC.
Fila 13: Código = 85600000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (25 %)
Fila 14: Código = 85700000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (50 %)
Fila 15: Código = 85800000 | Concepto = Incremento de la exigencia por riesgo de crédito por la tenencia de certifi- cados o títulos de deuda de fideicomisos financieros. (100 %)
Fila 16: Código = 86300000 | Concepto = Incremento de la exigencia por riesgo de crédito por excesos en las parti- cipaciones en el capital de empresas (INC ) (Inversiones significativas en empresas)
[FIN TABLA ric::tabla022]
[TABLA ric::tabla023 | página 42 | e0_tablas | posicional]
Fila 1: col1 = 87100000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Información en término
Fila 2: col1 = 87200000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Información fuera de término
Fila 3: col1 = 87300000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Incumplimientos reiterados
Fila 4: col1 = 87400000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en financia- miento al sector público no financiero. Determinado por la SEFyC
Fila 5: col1 = 87500000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Información en término
Fila 6: col1 = 87600000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Información fuera de término
Fila 7: col1 = 87700000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Incumplimientos reiterados
Fila 8: col1 = 87800000 | col2 = Incremento de la exigencia por riesgo de crédito por exceso en posicio- nes de derivados sobre “commodities”. Determinado por la SEFyC
[FIN TABLA ric::tabla023]
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: (sin NOTA)

NOTA de E3, nueva: NOTA: esta unidad tiene tablas serializadas por E0 (bloques [TABLA …] … [FIN TABLA …] del texto fuente, verificados contra el documento): su contenido es texto confiable y su omisión se evalúa como la de cualquier otro contenido.

## cap::6.2.2.6

Mensaje de E1, sellado:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 6.2.2.6 — Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
Puntos admitidos para `punto`: 6.2.2.6, S6, 6.2, 6.2.2

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_alcance_capmin como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S6]
Sección 6. Capital mínimo por riesgo de mercado.
[encabezado | punto 6.2]
6.2. Exigencia de capital por riesgo de tasa de interés.
[intro | punto 6.2]
La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la
emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones.
La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por
el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o com-
prada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de
interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendi-
das en diferentes instrumentos.
Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el pun-
to 6.2.3.
[encabezado | punto 6.2.2]
6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.

FLAGS E0: este chunk contiene contenido tabular (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar omisiones en `omisiones_no_prosa`).
  evidencia: Banda dentro entre entre
  evidencia: de zonas zonas
  evidencia: zona adyacentes 1 y 3

Texto del punto 6.2.2.6:
```
6.2.2.6. Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
posiciones netas compradas, un conjunto de posiciones netas vendidas y las
desestimaciones verticales. Luego, las entidades podrán realizar dos series de
compensaciones horizontales: primero, entre las posiciones netas dentro de
cada una de las tres zonas en las que se agrupan las bandas temporales y,
luego, entre las posiciones netas de las tres zonas. Dichas compensaciones
estarán sujetas a la siguiente escala de desestimaciones horizontales
-exigencias adicionales- expresadas como porcentajes de las posiciones que
se compensan:
Porcentaje de desestimación
aplicable:
Banda dentro entre entre
Zona
de zonas zonas
zona adyacentes 1 y 3
Meses*
0-1
1-3
1 40%
3-6
6-12
Años* 40%
1-2
2 2-3 30% 100%
3-4
Años* 40%
4-5
5-7
7-10
3 30%
10-15
15-20
Más de 20
ei se puede simplificar menciones a “meses” y “años”ese
*
Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que
resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, correspon-
derá realizar la imputación a la banda temporal más próxima a la fecha de cálculo.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 6.2.2.6 — Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
Puntos admitidos para `punto`: 6.2.2.6, S6, 6.2, 6.2.2

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S6]
Sección 6. Capital mínimo por riesgo de mercado.
[encabezado | punto 6.2]
6.2. Exigencia de capital por riesgo de tasa de interés.
[intro | punto 6.2]
La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la
emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones.
La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por
el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o com-
prada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de
interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendi-
das en diferentes instrumentos.
Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el pun-
to 6.2.3.
[encabezado | punto 6.2.2]
6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.

TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `cap::tabla037` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque; 18 celdas con un valor propagado desde otra fila (⟨combinada con fila n⟩); 3 celdas que abarcan varias columnas (⟨abarca hasta c⟩). ATENCIÓN, 1 fila de subtítulo: no es un dato; califica a las filas que la siguen. ATENCIÓN, 20 celdas combinadas que E0 no asignó a sus filas: el valor de cada una puede valer para varias filas y el bloque no indica cuáles. Si el texto no lo aclara, no lo asocies a ninguna fila: registrá la omisión `tabla` con su tramo.

Texto del punto 6.2.2.6:
```
6.2.2.6. Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
posiciones netas compradas, un conjunto de posiciones netas vendidas y las
desestimaciones verticales. Luego, las entidades podrán realizar dos series de
compensaciones horizontales: primero, entre las posiciones netas dentro de
cada una de las tres zonas en las que se agrupan las bandas temporales y,
luego, entre las posiciones netas de las tres zonas. Dichas compensaciones
estarán sujetas a la siguiente escala de desestimaciones horizontales
-exigencias adicionales- expresadas como porcentajes de las posiciones que
se compensan:
[TABLA cap::tabla037 | página 125 | e0_tablas | posicional]
Fila 1: col1 = Zona | col2 = Banda | col3 = Porcentaje de desestimación aplicable: ⟨abarca hasta col5⟩
Fila 2: col3 = dentro de zona | col4 = entre zonas adyacentes | col5 = entre zonas 1 y 3
Fila 3: col2 = Meses*
Fila 4: col1 = 1 | col2 = 0-1 | col3 = 40%
Fila 5: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 1-3 | col3 = 40% ⟨combinada con fila 4⟩
Fila 6: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 3-6 | col3 = 40% ⟨combinada con fila 4⟩
Fila 7: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 6-12 | col3 = 40% ⟨combinada con fila 4⟩
Fila 8: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 9: col1 = 2 | col2 = 1-2 | col3 = 30%
Fila 10: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 2-3 | col3 = 30% ⟨combinada con fila 9⟩ | col5 = 100%
Fila 11: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 3-4 | col3 = 30% ⟨combinada con fila 9⟩
Fila 12: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 13: col1 = 3 | col2 = 4-5 | col3 = 30%
Fila 14: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 5-7 | col3 = 30% ⟨combinada con fila 13⟩
Fila 15: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 7-10 | col3 = 30% ⟨combinada con fila 13⟩
Fila 16: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 10-15 | col3 = 30% ⟨combinada con fila 13⟩
Fila 17: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 15-20 | col3 = 30% ⟨combinada con fila 13⟩
Fila 18: col2 = Más de 20
[FIN TABLA cap::tabla037]
ei se puede simplificar menciones a “meses” y “años”ese
*
Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que
resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, correspon-
derá realizar la imputación a la banda temporal más próxima a la fecha de cálculo.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: NOTA: esta unidad tiene contenido tabular detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.

NOTA de E3, nueva: NOTA: esta unidad tiene tablas serializadas por E0 (bloques [TABLA …] … [FIN TABLA …] del texto fuente, verificados contra el documento): su contenido es texto confiable y su omisión se evalúa como la de cualquier otro contenido. E0 dejó sin resolver parte de la estructura de cap::tabla037 (20 celdas combinadas sin asignar a sus filas y 1 fila de subtítulo): la omisión `tabla` que el extractor declare sobre esa tabla no es faltante.

## cap::4.2.1.2

Mensaje de E1, sellado:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 4.2.1.2 — Cálculo de la EPF.
Puntos admitidos para `punto`: 4.2.1.2, S4, 4.2, 4.2.1

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_alcance_capmin como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S4]
Sección 4. Capital mínimo por riesgo de crédito de contraparte.
[encabezado | punto 4.2]
4.2. Exigencia de capital por riesgo de crédito de contraparte en operaciones con derivados
[intro | punto 4.2]
–OTC o negociados en mercados regulados– y con liquidación diferida.
La exigencia computada en este punto –basada en el Enfoque Estándar para la medición de
la exigencia por capital por riesgo de crédito de contraparte (“Standardised Approach for
measuring Counterparty Credit Risk”, SA-CCR)– se aplicará a operaciones con derivados
–OTC o negociados en mercados regulados– y con liquidación diferida, ya que las operacio-
nes de financiación con títulos valores (“Securities Financing Transactions”, SFT) –tales co-
mo operaciones de pase– cuyo valor depende de las valuaciones de mercado y están co-
múnmente sujetas a acuerdos de márgenes, se encuentran contempladas en la Sección 5.
Las operaciones de liquidación diferida son aquellas en las que la contraparte se comprome-
te a entregar un título valor, “commodity” o moneda extranjera contra efectivo, otro activo fi-
nanciero o “commodities” o viceversa, en una fecha contractual de liquidación o entrega su-
perior al plazo más corto entre el plazo habitual en el mercado para el vencimiento de ese ti-
po de instrumento y 5 días hábiles a partir de la fecha en que la entidad entró en la opera-
ción.
[encabezado | punto 4.2.1]
4.2.1. Exposición al riesgo de crédito de contraparte.
[intro | punto 4.2.1]
La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el CR representa la pérdida que ocurriría
[intro | punto 4.2.1]
ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo.
[intro | punto 4.2.1]
− Operaciones con margen de variación: el CR representa la pérdida que ocurriría
[intro | punto 4.2.1]
ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período.
[intro | punto 4.2.1]
En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite
[intro | punto 4.2.1]
superior la EAD que resultaría para el mismo conjunto si no los tuviera.
[intro | punto 4.2.1]
− La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá
[intro | punto 4.2.1]
ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones
no estén comprendidas en acuerdos de neteo que incluyan otros productos o la
constitución de márgenes.

FLAGS E0: este chunk contiene contenido tabular y fórmulas (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar omisiones en `omisiones_no_prosa`).
  evidencia: po de cambio, crédito, acciones y productos básicos
  evidencia:  + 1 - 1
  evidencia:  Comprada* Vendida*
  evidencia: mercado negativo de las operaciones, conforme a la siguiente expresión:
  evidencia: EPF = multiplicador x AdicionalTotal
  evidencia: donde:

Texto del punto 4.2.1.2:
```
4.2.1.2. Cálculo de la EPF.
Resultará del producto entre:
- la suma de los adicionales correspondientes a cada clase de activos; y
- un multiplicador que permite reconocer la garantía en exceso o el valor de
mercado negativo de las operaciones, conforme a la siguiente expresión:
EPF = multiplicador x AdicionalTotal
donde:
es la suma de los adicionales correspondientes a cada clase de activos
–no se reconocen beneficios por diversificación–, calculados de acuerdo con
la metodología expuesta en los acápites viii) a xii) de este punto, y el multi-
plicador se define como:
El multiplicador se reduce a medida que se incrementa la tenencia de garan-
tías en exceso –sujeto a un mínimo de 5 % de la EPF– y operará de la si-
guiente manera:
− Cuando el costo de reposición corriente sea positivo –esto es, cuando el
valor de los activos en garantía sea inferior al valor de mercado neto de los
contratos de derivados– el multiplicador será igual a uno –esto es, el com-
ponente EPF será igual al valor del AdicionalTotal–.
− Cuando el valor de los activos en garantía supere el valor de mercado neto
de los contratos de derivados –garantías en exceso–, el multiplicador será
inferior a la unidad –esto es, el componente EPF será menor que el valor
del AdicionalTotal –.
− El multiplicador se activará –es decir, tomará un valor inferior a la unidad–
también cuando el valor corriente de las operaciones con derivados sea
negativo.
Para determinar el cálculo de la EPF, las operaciones se ajustarán a lo si-
guiente:
− Cada derivado se asignará a una clase de activo sobre la base de su factor
de riesgo principal –que en la mayoría de los casos será el único, definido
por la referencia a un instrumento subyacente, tal como una curva de tasas
de interés en el caso de un “swap” de tasas de interés o un tipo de cambio
para una opción sobre monedas–, conforme a lo siguiente:
 Cuando sea posible identificar claramente el factor principal, la operación
se imputará a una de las siguientes clases de activos: tasa de interés, ti-
po de cambio, crédito, acciones y productos básicos
–“commodities”–.
 Cuando se trate de operaciones más complejas –tales como derivados hí-
bridos– en las que exista más de un factor de riesgo, las entidades deberán
tomar en consideración la sensibilidad y volatilidad de los subyacentes para
determinar el factor de riesgo principal.
El área de Supervisión y Seguimiento de la SEFyC podrá requerir que las ope-
raciones más complejas se asignen a más de una clase de activos, en cuyo
caso se deberá asignar la posición a múltiples clases y determinar, para cada
una, el signo y el ajuste delta para el factor de riesgo relevante.
− El adicional para cada clase de activo se computará usando fórmulas específi-
cas que calculan la correspondiente EPE efectiva. Independientemente de la
clase de activo de que se trate, las operaciones se ajustarán conforme a lo si-
guiente:
a) A partir del nocional real o del precio de cada operación se calculará un no-
cional ajustado. Para los derivados sobre tasas de interés y créditos, el
monto nocional ajustado incorporará una medición del plazo –“duration”–
establecida en el acápite ii) del presente punto.
b) También para cada operación se calculará un factor plazo (“maturity factor”)
MF(tipo) para reflejar el horizonte temporal adecuado al tipo de la operación
i
–acápite vi)– que se aplicará al nocional ajustado, de los cuales hay dos ti-
pos: uno para operaciones con márgenes MF(con margen) y otro para operacio-
i
nes sin márgenes MF(sin margen).
i
c) Al efecto de obtener el nocional efectivo se aplicará al nocional ajustado de
cada operación un ajuste delta –acápite iii)– según el tipo de posición –larga
o corta– y dependiendo de si se trata de una opción, de un segmento de
una titulización estructurada de deudas (“Collateralized Debt Obligation”,
CDO) o de otro tipo.
d) A cada nocional efectivo se le aplicará un factor que refleja su volatilidad
–acápite iv)–.
e) Las operaciones dentro de cada clase de activo se separarán por conjunto
de cobertura –acápite v)–. Seguidamente, se aplicará un método para su-
mar los datos de las operaciones dentro de cada conjunto y, luego, los da-
tos de cada conjunto para obtener un total por clase de activo. En este pro-
ceso, cuando se trate de derivados de crédito, acciones y productos bási-
cos, se emplearán parámetros de correlación a fin de capturar el efecto de
los riesgos de base (“basis risks”) y de la diversificación.
i) Parámetros de tiempo.
Se emplearán cuatro parámetros para representar períodos de tiempo conta-
dos desde el presente –la fecha de cálculo de la exigencia por riesgo de crédi-
to de contraparte–:
a) M: vencimiento. Para todas las clases de activos, será la última fecha hasta
i
la que podría estar activo el contrato. Esta fecha se utiliza en el factor plazo
–definido en el acápite vi)– para reducir el nocional ajustado de las opera-
ciones sin márgenes de todas las clases de activos. Si un contrato de deri-
vados tiene por subyacente otro contrato de derivados –tal es el caso de un
“swaption”; es decir, una opción cuyo subyacente es un “swap”– y se puede
ejercer entrando en el contrato subyacente –esto es, de ejercer la opción la
entidad financiera asumiría una posición en el contrato subyacente– el ven-
cimiento del contrato será la fecha de liquidación final del contrato derivado
subyacente.
b) S:en los derivados sobre tasas de interés y créditos, será la fecha de inicio
i
del período referenciado por el contrato. Si el derivado hace referencia al
valor de otro instrumento de crédito o a tasa de interés –tal como un “swap-
tion” o “bond option”– el período se determinará en base al instrumento
subyacente. Esta fecha se utilizará en la definición del plazo regulatorio de-
finido en el acápite ii).
c) E:en los derivados sobre tasas de interés y créditos, será la fecha de finali-
i
zación del período referenciado por el contrato. Si el derivado hace referen-
cia al valor de otro instrumento de crédito o a tasa de interés, el período se
determinará en base al instrumento subyacente. Esta fecha se utilizará en
la definición del plazo regulatorio definido en el acápite ii) y para determinar
la categoría de los contratos a tasa de interés en función de sus plazos que
se especifica en el acápite viii).
d) T: para las opciones, cualquiera sea la clase del activo, será la última fecha
i
de ejercicio según se estipula en el contrato. Se utilizará en el acápite iii)
para determinar el delta de la opción.
ii) Nocional ajustado a nivel de operación (para la operación i de la clase de acti-
vo a): d(a)
i
a) Para los derivados de tasa de interés y créditos, el nocional ajustado a nivel
de operación será el producto del nocional de la operación, convertido a
pesos, y el plazo regulatorio (“supervisory duration”, SD). El SD estará da-
i i
do por la siguiente expresión:
donde:
S: fecha de inicio del período referenciado por el derivado.
i
E: fecha de finalización del período referenciado por el derivado.
i
Cuando el derivado haga referencia al valor de otro instrumento de tasa de
interés o crédito, el período se determinará en base al instrumento subya-
cente. Si la fecha de inicio ya ha tenido lugar –tal como el caso de un
“swap” de tasa de interés en curso–, S será igual a cero.
i
El período no podrá ser menor que 10 días hábiles.
b) Para los derivados de tipo de cambio, el nocional ajustado se definirá
como el nocional del lado “leg” del contrato expresado en moneda ex-
tranjera, convertido a pesos. Si ambos lados del derivado están denomi-
nados en monedas extranjeras, se tomará el mayor de ambos nocionales
una vez convertidos a pesos.
c) Para los derivados sobre acciones y “commodities”, el nocional ajustado
será el producto del precio corriente de una unidad de la acción o pro-
ducto por el número de unidades referenciado por la operación. En el ca-
so de las operaciones sobre la volatilidad de las acciones y productos
básicos –tal como “equity volatility swaps”– mencionadas en el apartado
c) del acápite v) del presente punto el nocional ajustado será el producto
de la volatilidad o la varianza referenciadas en la operación y el nocional
contractual.
d) Cuando se trate de operaciones en las que el nocional no está claramen-
te definido o no se mantiene fijo hasta el vencimiento, para determinarlo
se deberá observar lo siguiente:
- Para las operaciones con retribuciones (“payoff”) múltiples y contin-
gentes respecto de un estado o situación –tal como las opciones digi-
tales (“digital option”)– se calculará un nocional para cada estado y
tomará el que resulte mayor. A tal efecto, la mayor retribución (equi-
valente a la EPF máxima) se convertirá en nocional regulatorio em-
pleando los factores definidos en el acápite xiii) y los ajustes MF y
delta.
- Cuando el nocional sea una fórmula en base a valores de mercado,
se tomarán los valores de mercado corrientes para determinar el no-
cional de la operación.
- En el caso de los derivados de tasa de interés o crédito con nociona-
les variables –tales como los “swaps” de nocional variable (“amorti-
sing swaps” y “accreting swaps”)–, se empleará el promedio, ponde-
rado por el tiempo, del nocional durante la vida residual del instru-
mento. Esta regla no será aplicable a las operaciones en las que el
nocional varía debido a cambios en los precios –tales como los deri-
vados FX, y sobre acciones o “commodities”–.
- Los “swaps” apalancados se convertirán a los nocionales de “swaps”
no apalancados equivalentes. Cuando todas las tasas en un “swap”
se multipliquen por un factor, el nocional establecido también se mul-
tiplicará por ese factor para determinar el nocional de la operación.
- En el caso de un derivado con intercambios múltiples del principal, el
nocional se multiplicará por el número de intercambios previstos en el
contrato.
- Cuando un derivado esté estructurado de tal manera que en las fe-
chas predeterminadas se cancele la exposición vigente y se reformu-
len las condiciones de modo que el valor razonable (“fair value”) del
contrato sea cero, el plazo residual será el plazo hasta la próxima fe-
cha de reformulación.
iii) Ajustes delta regulatorios: .
i
El parámetro  se aplicará a los correspondientes nocionales ajustados de
i
cada operación y se calculará conforme a lo siguiente:
a) Posiciones en instrumentos derivados que no son opciones ni segmentos
de CDO.
Posición Posición
Larga* Corta**
en el factor de riesgo primario
 + 1 - 1
i
* El valor de mercado del instrumento crece cuando aumenta el valor del factor de
riesgo principal y viceversa.
** El valor de mercado del instrumento decrece cuando aumenta el valor del factor de
riesgo principal y viceversa.
b) Posiciones en opciones.
 Comprada* Vendida*
i
“call”
“put”
* El símbolo ᶲ representa la función de distribución normal estándar.
Las entidades calcularán los siguientes parámetros:
P: precio del subyacente –contado, “forward”, promedio, etc.–. Cuando
i
sea posible, se empleará el precio “forward” y no el precio contado
del subyacente, a fin de tomar en consideración el efecto tanto de la
tasa de interés libre de riesgo como de los flujos de efectivo –tales
como los dividendos– anteriores a la expiración de la opción.
K: precio de ejercicio.
i
T: última fecha contractual para el ejercicio de la opción.
i
La volatilidad  de la opción se especificará en base al factor regulatorio
i
aplicable a la operación, conforme a la tabla del acápite xiii).
c) Posiciones en segmentos de CDO.
Comprada Vendida
(cobertura larga) (cobertura corta)

i
Las entidades calcularán los siguientes parámetros:
A: punto de unión del segmento CDO.
i
D: punto de separación del segmento CDO.
i
iv) Factores regulatorios: SF(a)
i
En base a la medición de la volatilidad de cada clase de activo, se aplicarán
uno o más factores específicos –acápite xiii)– al nocional efectivo a fin de
obtener la EPE efectiva.
v) Conjuntos de cobertura (“hedging sets”, HS).
a) Los conjuntos de cobertura en las diferentes clases de activos se defini-
rán conforme al siguiente criterio (excepto por lo establecido en los apar-
tados b) y c) de este mismo acápite):
- Derivados sobre tasas de interés: un conjunto de cobertura para
cada moneda.
- Derivados FX: un conjunto de cobertura para cada par de mone-
das.
- Derivados de crédito: un único conjunto de cobertura.
- Derivados sobre acciones: un único conjunto de cobertura.
- Derivados sobre “commodities”: cuatro conjuntos de cobertura,
uno para cada categoría: energía, metales, productos agrícolas y
otros productos básicos.
b) Los derivados que referencian la base (“basis”) entre dos factores de
riesgo y están denominados en una sola moneda (operaciones sobre
base, “basis transactions”) se deberán asignar a conjuntos de cobertura
específicos dentro de la clase de activo correspondiente. Este tratamien-
to no se aplicará a los derivados con dos lados flotantes denominados en
monedas diferentes –tales como los “cross-currency swaps”: acuerdos
para intercambiar pagos de principal e intereses de préstamos denomi-
nados en dos monedas diferentes–, los que recibirán el tratamiento apli-
cable a los contratos FX ordinarios. Hay un conjunto de cobertura para
cada par de factores de riesgo –para cada base específica– dentro del
cual las posiciones se clasificarán en largas o cortas respecto de dicha
base. Cuando se aplique a conjuntos de cobertura de derivados sobre
bases, el SF correspondiente a la clase se multiplicará por 0,5.
c) Los derivados referidos a la volatilidad de un factor de riesgo
–operaciones sobre la volatilidad, tales como los “swaps” de varianza y
volatilidad y las opciones sobre la volatilidad real o implícita– se asigna-
rán a conjuntos específicos dentro de la clase de activo correspondiente.
Los conjuntos de cobertura de volatilidades se formarán siguiendo lo
previsto en el punto a) de este acápite. Cuando se aplique a conjuntos
de cobertura de operaciones sobre la volatilidad, el SF correspondiente a
la clase se multiplicará por 5.
vi) Factor de plazo.
a) Operaciones sin margen de variación: su horizonte temporal mínimo será
el menor entre un año y el plazo residual del contrato de derivados, con
un mínimo de 10 días hábiles.
El nocional ajustado a nivel de operación se multiplicará por un factor de
plazo (“maturity factor”):
donde el numerador es el horizonte temporal mínimo y M es el plazo re-
i
sidual de la operación i –con un mínimo de 10 días hábiles–.
Las unidades del numerador y denominador se expresarán en la misma
unidad de tiempo.
b) Operaciones con margen de variación: el período de riesgo de margen
(“MPOR”) mínimo será el que corresponda conforme a lo siguiente:
− Al menos 10 días hábiles para las operaciones de derivados que no
se liquidan en forma centralizada y están sujetas a acuerdos de már-
genes diarios.
− 5 días hábiles para las operaciones de derivados que se liquidan en
forma centralizada y están sujetas a acuerdos de márgenes diarios
entre el miembro compensador y sus clientes.
− 20 días hábiles para los conjuntos de neteo –excepto aquellos con
una contraparte central– cuyo número de operaciones supere las
5.000 en cualquier momento del trimestre calendario anterior.
− El doble del período de riesgo de margen para los conjuntos de neteo
con disputas pendientes. Si la entidad ha experimentado más de dos
disputas sobre requerimientos de márgenes (“margin calls”) respecto
de algún conjunto de neteo durante los dos trimestres calendario an-
teriores, que se hayan prolongado durante períodos más extensos
que el período de riesgo de margen –que hubiera correspondido sin
tomar en consideración esta regla–, deberá reflejar este antecedente
mediante el uso, durante los dos trimestres calendario posteriores,
de un período de riesgo de margen que sea por lo menos el doble
que el mínimo establecido para ese conjunto de neteo.
El nocional ajustado a nivel de operación se multiplicará por:
donde:
MPOR: período de riesgo de margen correspondiente al acuerdo sobre
i
márgenes aplicable a la operación i. Los mínimos referidos en
este apartado se deberán incrementar cuando la frecuencia de
reposición de márgenes no sea diaria: MPOR = mínimo + N - 1,
i
donde N es la cantidad de días entre reposiciones.
Las unidades del numerador y denominador se deberán expre-
sar en la misma unidad de tiempo. La cantidad de días hábiles
en un año se deberá determinar en función de las convenciones
en el mercado relevante.
vii) Parámetros de correlación regulatorios: (a)
i
Se utilizan sólo en el cálculo de la EPF de los derivados sobre acciones,
créditos y “commodities” –no se aplican a los derivados de tasa de interés o
tipo de cambio– para ponderar los componentes sistemáticos e idiosincrási-
cos y, de esa forma, determinar el grado de compensación entre las opera-
ciones individuales, ya que las coberturas imperfectas sólo permiten una
compensación parcial de los riesgos –acápite xiii)–.
viii) Adicional para los derivados de tasa de interés.
Este adicional captura el riesgo que surge de la correlación imperfecta entre
derivados con plazos diferentes.
Para su cómputo, los derivados se dividirán en tres categorías de plazo
–bandas temporales o “buckets”– sobre la base de la fecha de finalización
de las operaciones, conforme a lo dispuesto en los acápites i) y ii): menos de
un año, entre uno y cinco años y más de cinco años. Se permitirá la com-
pensación total de las posiciones dentro de cada categoría y una compen-
sación parcial entre categorías.
El adicional para los derivados de tasa de interés será la suma del adicional
para cada conjunto de cobertura de derivados sobre tasa de interés con una
contraparte dentro de un conjunto de neteo. El adicional para un conjunto de
cobertura de derivados sobre tasa de interés se computará en dos pasos:
1. Se calculará un nocional efectivo D (IR) por banda temporal k dentro del
jk
conjunto de cobertura (moneda) j:
Donde i{Ccy, MB } se refiere a las operaciones en la moneda j incluidas
j k
en la banda temporal k. El nocional efectivo por banda temporal y mone-
da es la suma de los nocionales ajustados a nivel de operación –acápite
ii)– multiplicados por los ajustes delta regulatorios –acápite iii)– y el factor
por plazo residual –acápite vi)–.
2. La suma entre bandas temporales de un mismo conjunto de cobertura se
calculará conforme a la siguiente expresión:
Las entidades podrán no reconocer las compensaciones entre bandas
temporales, en cuyo caso la fórmula se reducirá a:
El adicional a nivel de conjunto de cobertura será el producto del nocional
efectivo y el factor regulatorio para tasas de interés:
El adicional para todos los conjuntos de cobertura se obtendrá por suma
simple:
ix) Adicional para los derivados de tipo de cambio.
El nocional efectivo de un conjunto de cobertura se computará como la su-
ma de todos los nocionales ajustados a nivel de operación multiplicados por
sus deltas regulatorios.
El adicional para un conjunto de cobertura será el producto de:
- el valor absoluto de su nocional efectivo; y
- el factor regulatorio –que es idéntico para todos los conjuntos de cober-
tura de tipo de cambio–.
El nocional ajustado estará dado por la cantidad de moneda extranjera a la
que hace referencia el contrato, expresada en pesos, conforme a la siguien-
te expresión:
donde se suman todos los conjuntos de cobertura HS incluidos en el conjun-
j
to de neteo. El adicional y el nocional efectivo de cada conjunto de cobertura
HS estarán dados, respectivamente, por:
j
donde iHS refiere a las operaciones en el conjunto de cobertura HS. El
j j
nocional efectivo para cada par de monedas será la sumatoria de los nocio-
nales ajustados a nivel de operación –acápite ii)– multiplicados por los ajus-
tes delta regulatorios –acápite iii)– y el factor plazo –acápite vi)–.
x) Adicional para los derivados de crédito.
Las exposiciones originadas en derivados de crédito estarán sujetas a dos
niveles de compensación:
1. Todos los derivados de crédito que hagan referencia a una misma enti-
dad (un único deudor o un índice) se compensarán plenamente entre sí
y determinarán un nocional efectivo único a nivel de entidad.
donde iEntidad refiere a las operaciones respecto de la entidad k. El
k
nocional efectivo para cada entidad será la sumatoria de los nocionales
ajustados a nivel de operación –acápite ii)– multiplicados por los ajustes
delta regulatorios –acápite iii)– y el factor plazo –acápite vi)–.
El adicional para todas las posiciones que hagan referencia a esta enti-
dad será el producto del nocional efectivo y el factor regulatorio
SF (Crédito):
k
Cuando se referencie a un único deudor, SF (Crédito) se determinará en
k
función de su calificación crediticia. Cuando se trate de un índice,
SF (Crédito) dependerá de si el índice es grado de inversión o especulativo.
k
2. Los adicionales de todas las entidades se agruparán en un único conjun-
to de cobertura –excepto los que correspondan a operaciones sobre ba-
ses y volatilidades– dentro del cual los adicionales de entidades diferen-
tes no se podrán compensar totalmente. Se permitirá una compensación
parcial de los adicionales a nivel de entidad, en base a un modelo de
factor único que permitirá separar el riesgo de esta clase de derivados
en sus componentes sistemático e idiosincrásico.
Los componentes sistemáticos de los adicionales a nivel de entidad se
podrán compensar íntegramente entre sí pero la compensación no esta-
rá disponible para los componentes idiosincrásicos. Ambos componen-
tes se ponderarán por un factor de correlación que determinará el grado
de compensación/cobertura dentro de esta clase de activo. Los deriva-
dos que hagan referencia a índices de crédito se considerarán como si
hicieran referencia a entidades determinadas (“single names”) pero se
les aplicará un mayor factor de correlación:
donde  (Crédito) es el factor de correlación correspondiente a la entidad k.
k
xi) Adicional para los derivados sobre acciones.
Se utilizará un modelo de factor único para dividir el riesgo de cada entidad
de referencia (entidad o índice) en sus componentes sistemático e idiosin-
crásico. Los derivados que hagan referencia a un índice de acciones se tra-
tarán como si hicieran referencia a entidades determinadas pero con un fac-
tor de correlación más alto para el componente sistemático.
Aunque se permitirá la compensación íntegra de las operaciones correspon-
dientes a una entidad, sólo se permitirá la compensación del componente
sistemático del adicional de diferentes entidades. Los adicionales a nivel de
entidad serán proporcionales al producto entre el nocional efectivo y el SF
que corresponde a cada entidad.
donde  (Acción) será el factor de correlación correspondiente a la entidad k. El
k
adicional para todas las posiciones que hagan referencia a la entidad k y su
nocional efectivo estarán dados, respectivamente, por:
y
donde iEntidad referirá a las operaciones respecto de la entidad k. El no-
k
cional efectivo para cada entidad será la sumatoria de los nocionales ajusta-
dos a nivel de operación –acápite ii)–, multiplicados por los ajustes delta re-
gulatorios –acápite iii)– y el factor plazo –acápite vi)–.
xii) Adicional para los derivados sobre “commodities”.
El adicional será la suma para todos los HS:
Se empleará un modelo de un único factor dentro de cada conjunto de co-
bertura para dividir el riesgo correspondiente a un mismo tipo de “commo-
dity” en sus componentes sistemático e idiosincrásico. La compensación o
cobertura total estarán permitidas entre todas las operaciones de derivados
que hagan referencia al mismo tipo de “commodity” –tal como las que se re-
fieran al “petróleo crudo” dentro del conjunto de cobertura “energía”– a fin de
determinar un nocional efectivo a nivel de tipo de “commodity”. La compen-
sación o la cobertura parciales estarán permitidas entre los tipos de “com-
modities” que integran cada conjunto de cobertura –por ejemplo, entre petró-
leo, gas natural, carbón y electricidad– pero se definirán factores regulato-
rios para cada uno. No se permitirá la compensación o cobertura entre con-
juntos de cobertura –tal como energía, metales y productos agrícolas–:
donde (Com) será el factor de correlación correspondiente al conjunto de co-
j
bertura j. El adicional y el nocional efectivo del tipo k de “commodity” estarán
dados, respectivamente, por:
y
donde iTipoj referirá a las operaciones respecto del tipo k de “commodity”
k
dentro del conjunto j. El nocional efectivo para cada tipo de “commodity” se-
rá la suma de los nocionales ajustados a nivel de operación –acápite ii)–,
multiplicados por los ajustes delta regulatorios –acápite iii)– y el factor plazo
–acápite vi)–.
No se podrán hacer coberturas entre las cuatro grandes categorías de deri-
vados sobre “commodities”.
La definición de los conjuntos de cobertura por tipo de “commodity” no toma-
rá en consideración características tales como la calidad o la ubicación. No
obstante, el área de Supervisión y Seguimiento de la SEFyC podrá requerir
el uso de definiciones más precisas si alguna entidad tuviera una exposición
muy significativa al riesgo de base de productos diferentes dentro de deter-
minado tipo de “commodity”.
xiii) Factores regulatorios, correlaciones y adicionales regulatorios por la volatili-
dad de las opciones.
Factor
Volatilidad
Clase aplicable Correlación
Subclase opción
de activo (a)
i
SF (a) σ (a)
i i
tasa de
0,50 % N/A 50 %
interés
tipo de
4 % N/A 15 %
cambio
AAA 0,38 % 50 % 100 %
AA 0,38 % 50 % 100 %
crédito, único A 0,42 % 50 % 100 %
deudor BBB 0,54 % 50 % 100 %
BB 1,06 % 50 % 100 %
B 1,6 % 50 % 100 %
CCC 6 % 50 % 100 %
crédito grado de
0,38 % 80 % 80 %
inversión
índice especulativo 1,06 % 80 % 80 %
acción, único
32 % 50 % 120 %
emisor
acción,
20 % 80 % 75 %
índice
“commodity” electricidad 40 % 40 % 150 %
petróleo/gas 18 % 40 % 70 %
metales 18 % 40 % 70 %
prod. agrícolas 18 % 40 % 70 %
otros 18 % 40 % 70 %
El SF a aplicar a un conjunto de cobertura de operaciones sobre bases será
el que corresponda a la clase de activo pertinente multiplicado por 0,5. El
factor a aplicar a un conjunto de operaciones sobre volatilidades será el que
corresponda a la clase de activo multiplicado por 5 –acápite v)–.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 4.2.1.2 — Cálculo de la EPF.
Puntos admitidos para `punto`: 4.2.1.2, S4, 4.2, 4.2.1

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S4]
Sección 4. Capital mínimo por riesgo de crédito de contraparte.
[encabezado | punto 4.2]
4.2. Exigencia de capital por riesgo de crédito de contraparte en operaciones con derivados
[intro | punto 4.2]
–OTC o negociados en mercados regulados– y con liquidación diferida.
La exigencia computada en este punto –basada en el Enfoque Estándar para la medición de
la exigencia por capital por riesgo de crédito de contraparte (“Standardised Approach for
measuring Counterparty Credit Risk”, SA-CCR)– se aplicará a operaciones con derivados
–OTC o negociados en mercados regulados– y con liquidación diferida, ya que las operacio-
nes de financiación con títulos valores (“Securities Financing Transactions”, SFT) –tales co-
mo operaciones de pase– cuyo valor depende de las valuaciones de mercado y están co-
múnmente sujetas a acuerdos de márgenes, se encuentran contempladas en la Sección 5.
Las operaciones de liquidación diferida son aquellas en las que la contraparte se comprome-
te a entregar un título valor, “commodity” o moneda extranjera contra efectivo, otro activo fi-
nanciero o “commodities” o viceversa, en una fecha contractual de liquidación o entrega su-
perior al plazo más corto entre el plazo habitual en el mercado para el vencimiento de ese ti-
po de instrumento y 5 días hábiles a partir de la fecha en que la entidad entró en la opera-
ción.
[encabezado | punto 4.2.1]
4.2.1. Exposición al riesgo de crédito de contraparte.
[intro | punto 4.2.1]
La exposición al riesgo de crédito de contraparte (EAD) se calculará por separado para
cada conjunto de neteo (“netting set”, NS) y se determinará del siguiente modo:
donde:
α = 1,40.
CR: costo de reposición calculado de acuerdo con el punto 4.2.1.1.
EPF: exposición potencial futura calculado de acuerdo con el punto 4.2.1.2.
El cálculo del CR y de la EPF diferirá según que los conjuntos de neteo estén sujetos o
no al intercambio de márgenes de variación:
− Operaciones sin margen de variación: el CR representa la pérdida que ocurriría
[intro | punto 4.2.1]
ante el incumplimiento de la contraparte y la liquidación inmediata de sus opera-
ciones y la EPF adicionará el incremento probable de la exposición, calculado de
modo conservador, en el horizonte temporal de un año a partir de la fecha de
cálculo.
[intro | punto 4.2.1]
− Operaciones con margen de variación: el CR representa la pérdida que ocurriría
[intro | punto 4.2.1]
ante el incumplimiento de la contraparte –en el presente o en el futuro– si la liqui-
dación y reposición de las operaciones fueran instantáneas. Dado que puede ha-
ber un lapso –período de riesgo de margen (“MPOR”)– entre el último intercambio
de garantías antes del incumplimiento y la reposición, el adicional por la EPF re-
presenta el potencial cambio de valor de las operaciones durante ese período.
[intro | punto 4.2.1]
En ambos casos, y a los efectos de determinar el costo de reposición, el aforo de los
activos recibidos en garantía (excepto efectivo) representará el cambio potencial del
valor de dicha garantía durante el período relevante –un año, para las operaciones sin
márgenes, y el período de riesgo de margen, para las operaciones con márgenes–.
Además:
− La EAD para un conjunto de neteo con márgenes de variación tendrá como límite
[intro | punto 4.2.1]
superior la EAD que resultaría para el mismo conjunto si no los tuviera.
[intro | punto 4.2.1]
− La EAD de un conjunto de neteo que sólo comprende opciones vendidas podrá
[intro | punto 4.2.1]
ser cero cuando hayan sido cobradas todas las primas y en tanto dichas opciones
no estén comprendidas en acuerdos de neteo que incluyan otros productos o la
constitución de márgenes.

TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `cap::tabla016` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque; 3 celdas que abarcan varias columnas (⟨abarca hasta c⟩).
- `cap::tabla017` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque; 2 celdas que abarcan varias columnas (⟨abarca hasta c⟩).
- `cap::tabla018` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque.
FLAGS E0: este chunk contiene contenido tabular fuera de los bloques confiables y fórmulas (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar en `omisiones` con categoría `tabla` o `formula`).
E0 detectó tablas que no pudo serializar (`cap::tabla031`): su contenido quedó como texto linealizado, no confiable.
  evidencia: po de cambio, crédito, acciones y productos básicos
  evidencia:  + 1 - 1
  evidencia: mercado negativo de las operaciones, conforme a la siguiente expresión:
  evidencia: EPF = multiplicador x AdicionalTotal
  evidencia: donde:

Texto del punto 4.2.1.2:
```
4.2.1.2. Cálculo de la EPF.
Resultará del producto entre:
- la suma de los adicionales correspondientes a cada clase de activos; y
- un multiplicador que permite reconocer la garantía en exceso o el valor de
mercado negativo de las operaciones, conforme a la siguiente expresión:
EPF = multiplicador x AdicionalTotal
donde:
es la suma de los adicionales correspondientes a cada clase de activos
–no se reconocen beneficios por diversificación–, calculados de acuerdo con
la metodología expuesta en los acápites viii) a xii) de este punto, y el multi-
plicador se define como:
El multiplicador se reduce a medida que se incrementa la tenencia de garan-
tías en exceso –sujeto a un mínimo de 5 % de la EPF– y operará de la si-
guiente manera:
− Cuando el costo de reposición corriente sea positivo –esto es, cuando el
valor de los activos en garantía sea inferior al valor de mercado neto de los
contratos de derivados– el multiplicador será igual a uno –esto es, el com-
ponente EPF será igual al valor del AdicionalTotal–.
− Cuando el valor de los activos en garantía supere el valor de mercado neto
de los contratos de derivados –garantías en exceso–, el multiplicador será
inferior a la unidad –esto es, el componente EPF será menor que el valor
del AdicionalTotal –.
− El multiplicador se activará –es decir, tomará un valor inferior a la unidad–
también cuando el valor corriente de las operaciones con derivados sea
negativo.
Para determinar el cálculo de la EPF, las operaciones se ajustarán a lo si-
guiente:
− Cada derivado se asignará a una clase de activo sobre la base de su factor
de riesgo principal –que en la mayoría de los casos será el único, definido
por la referencia a un instrumento subyacente, tal como una curva de tasas
de interés en el caso de un “swap” de tasas de interés o un tipo de cambio
para una opción sobre monedas–, conforme a lo siguiente:
 Cuando sea posible identificar claramente el factor principal, la operación
se imputará a una de las siguientes clases de activos: tasa de interés, ti-
po de cambio, crédito, acciones y productos básicos
–“commodities”–.
 Cuando se trate de operaciones más complejas –tales como derivados hí-
bridos– en las que exista más de un factor de riesgo, las entidades deberán
tomar en consideración la sensibilidad y volatilidad de los subyacentes para
determinar el factor de riesgo principal.
El área de Supervisión y Seguimiento de la SEFyC podrá requerir que las ope-
raciones más complejas se asignen a más de una clase de activos, en cuyo
caso se deberá asignar la posición a múltiples clases y determinar, para cada
una, el signo y el ajuste delta para el factor de riesgo relevante.
− El adicional para cada clase de activo se computará usando fórmulas específi-
cas que calculan la correspondiente EPE efectiva. Independientemente de la
clase de activo de que se trate, las operaciones se ajustarán conforme a lo si-
guiente:
a) A partir del nocional real o del precio de cada operación se calculará un no-
cional ajustado. Para los derivados sobre tasas de interés y créditos, el
monto nocional ajustado incorporará una medición del plazo –“duration”–
establecida en el acápite ii) del presente punto.
b) También para cada operación se calculará un factor plazo (“maturity factor”)
MF(tipo) para reflejar el horizonte temporal adecuado al tipo de la operación
i
–acápite vi)– que se aplicará al nocional ajustado, de los cuales hay dos ti-
pos: uno para operaciones con márgenes MF(con margen) y otro para operacio-
i
nes sin márgenes MF(sin margen).
i
c) Al efecto de obtener el nocional efectivo se aplicará al nocional ajustado de
cada operación un ajuste delta –acápite iii)– según el tipo de posición –larga
o corta– y dependiendo de si se trata de una opción, de un segmento de
una titulización estructurada de deudas (“Collateralized Debt Obligation”,
CDO) o de otro tipo.
d) A cada nocional efectivo se le aplicará un factor que refleja su volatilidad
–acápite iv)–.
e) Las operaciones dentro de cada clase de activo se separarán por conjunto
de cobertura –acápite v)–. Seguidamente, se aplicará un método para su-
mar los datos de las operaciones dentro de cada conjunto y, luego, los da-
tos de cada conjunto para obtener un total por clase de activo. En este pro-
ceso, cuando se trate de derivados de crédito, acciones y productos bási-
cos, se emplearán parámetros de correlación a fin de capturar el efecto de
los riesgos de base (“basis risks”) y de la diversificación.
i) Parámetros de tiempo.
Se emplearán cuatro parámetros para representar períodos de tiempo conta-
dos desde el presente –la fecha de cálculo de la exigencia por riesgo de crédi-
to de contraparte–:
a) M: vencimiento. Para todas las clases de activos, será la última fecha hasta
i
la que podría estar activo el contrato. Esta fecha se utiliza en el factor plazo
–definido en el acápite vi)– para reducir el nocional ajustado de las opera-
ciones sin márgenes de todas las clases de activos. Si un contrato de deri-
vados tiene por subyacente otro contrato de derivados –tal es el caso de un
“swaption”; es decir, una opción cuyo subyacente es un “swap”– y se puede
ejercer entrando en el contrato subyacente –esto es, de ejercer la opción la
entidad financiera asumiría una posición en el contrato subyacente– el ven-
cimiento del contrato será la fecha de liquidación final del contrato derivado
subyacente.
b) S:en los derivados sobre tasas de interés y créditos, será la fecha de inicio
i
del período referenciado por el contrato. Si el derivado hace referencia al
valor de otro instrumento de crédito o a tasa de interés –tal como un “swap-
tion” o “bond option”– el período se determinará en base al instrumento
subyacente. Esta fecha se utilizará en la definición del plazo regulatorio de-
finido en el acápite ii).
c) E:en los derivados sobre tasas de interés y créditos, será la fecha de finali-
i
zación del período referenciado por el contrato. Si el derivado hace referen-
cia al valor de otro instrumento de crédito o a tasa de interés, el período se
determinará en base al instrumento subyacente. Esta fecha se utilizará en
la definición del plazo regulatorio definido en el acápite ii) y para determinar
la categoría de los contratos a tasa de interés en función de sus plazos que
se especifica en el acápite viii).
d) T: para las opciones, cualquiera sea la clase del activo, será la última fecha
i
de ejercicio según se estipula en el contrato. Se utilizará en el acápite iii)
para determinar el delta de la opción.
ii) Nocional ajustado a nivel de operación (para la operación i de la clase de acti-
vo a): d(a)
i
a) Para los derivados de tasa de interés y créditos, el nocional ajustado a nivel
de operación será el producto del nocional de la operación, convertido a
pesos, y el plazo regulatorio (“supervisory duration”, SD). El SD estará da-
i i
do por la siguiente expresión:
donde:
S: fecha de inicio del período referenciado por el derivado.
i
E: fecha de finalización del período referenciado por el derivado.
i
Cuando el derivado haga referencia al valor de otro instrumento de tasa de
interés o crédito, el período se determinará en base al instrumento subya-
cente. Si la fecha de inicio ya ha tenido lugar –tal como el caso de un
“swap” de tasa de interés en curso–, S será igual a cero.
i
El período no podrá ser menor que 10 días hábiles.
b) Para los derivados de tipo de cambio, el nocional ajustado se definirá
como el nocional del lado “leg” del contrato expresado en moneda ex-
tranjera, convertido a pesos. Si ambos lados del derivado están denomi-
nados en monedas extranjeras, se tomará el mayor de ambos nocionales
una vez convertidos a pesos.
c) Para los derivados sobre acciones y “commodities”, el nocional ajustado
será el producto del precio corriente de una unidad de la acción o pro-
ducto por el número de unidades referenciado por la operación. En el ca-
so de las operaciones sobre la volatilidad de las acciones y productos
básicos –tal como “equity volatility swaps”– mencionadas en el apartado
c) del acápite v) del presente punto el nocional ajustado será el producto
de la volatilidad o la varianza referenciadas en la operación y el nocional
contractual.
d) Cuando se trate de operaciones en las que el nocional no está claramen-
te definido o no se mantiene fijo hasta el vencimiento, para determinarlo
se deberá observar lo siguiente:
- Para las operaciones con retribuciones (“payoff”) múltiples y contin-
gentes respecto de un estado o situación –tal como las opciones digi-
tales (“digital option”)– se calculará un nocional para cada estado y
tomará el que resulte mayor. A tal efecto, la mayor retribución (equi-
valente a la EPF máxima) se convertirá en nocional regulatorio em-
pleando los factores definidos en el acápite xiii) y los ajustes MF y
delta.
- Cuando el nocional sea una fórmula en base a valores de mercado,
se tomarán los valores de mercado corrientes para determinar el no-
cional de la operación.
- En el caso de los derivados de tasa de interés o crédito con nociona-
les variables –tales como los “swaps” de nocional variable (“amorti-
sing swaps” y “accreting swaps”)–, se empleará el promedio, ponde-
rado por el tiempo, del nocional durante la vida residual del instru-
mento. Esta regla no será aplicable a las operaciones en las que el
nocional varía debido a cambios en los precios –tales como los deri-
vados FX, y sobre acciones o “commodities”–.
- Los “swaps” apalancados se convertirán a los nocionales de “swaps”
no apalancados equivalentes. Cuando todas las tasas en un “swap”
se multipliquen por un factor, el nocional establecido también se mul-
tiplicará por ese factor para determinar el nocional de la operación.
- En el caso de un derivado con intercambios múltiples del principal, el
nocional se multiplicará por el número de intercambios previstos en el
contrato.
- Cuando un derivado esté estructurado de tal manera que en las fe-
chas predeterminadas se cancele la exposición vigente y se reformu-
len las condiciones de modo que el valor razonable (“fair value”) del
contrato sea cero, el plazo residual será el plazo hasta la próxima fe-
cha de reformulación.
iii) Ajustes delta regulatorios: .
i
El parámetro  se aplicará a los correspondientes nocionales ajustados de
i
cada operación y se calculará conforme a lo siguiente:
a) Posiciones en instrumentos derivados que no son opciones ni segmentos
de CDO.
[TABLA cap::tabla016 | página 73 | e0_tablas | posicional]
Fila 1: col4 = Posición Larga* ⟨abarca hasta col6⟩ | col7 = Posición Corta** ⟨abarca hasta col9⟩
Fila 2: col4 = en el factor de riesgo primario ⟨abarca hasta col9⟩
Fila 3: col2 =  i | col5 = + 1 | col8 = - 1
[FIN TABLA cap::tabla016]
* El valor de mercado del instrumento crece cuando aumenta el valor del factor de
riesgo principal y viceversa.
** El valor de mercado del instrumento decrece cuando aumenta el valor del factor de
riesgo principal y viceversa.
b) Posiciones en opciones.
[TABLA cap::tabla017 | página 73 | e0_tablas | posicional]
Fila 1: col2 =  i | col5 = Comprada* | col7 = Vendida*
Fila 2: col1 = “call” ⟨abarca hasta col3⟩
Fila 3: col1 = “put” ⟨abarca hasta col3⟩
[FIN TABLA cap::tabla017]
* El símbolo ᶲ representa la función de distribución normal estándar.
Las entidades calcularán los siguientes parámetros:
P: precio del subyacente –contado, “forward”, promedio, etc.–. Cuando
i
sea posible, se empleará el precio “forward” y no el precio contado
del subyacente, a fin de tomar en consideración el efecto tanto de la
tasa de interés libre de riesgo como de los flujos de efectivo –tales
como los dividendos– anteriores a la expiración de la opción.
K: precio de ejercicio.
i
T: última fecha contractual para el ejercicio de la opción.
i
La volatilidad  de la opción se especificará en base al factor regulatorio
i
aplicable a la operación, conforme a la tabla del acápite xiii).
c) Posiciones en segmentos de CDO.
[TABLA cap::tabla018 | página 74 | e0_tablas | posicional]
Fila 1: col3 = Comprada | col5 = Vendida (cobertura corta)
Fila 2: col3 = (cobertura larga)
Fila 3: col1 =  i
[FIN TABLA cap::tabla018]
Las entidades calcularán los siguientes parámetros:
A: punto de unión del segmento CDO.
i
D: punto de separación del segmento CDO.
i
iv) Factores regulatorios: SF(a)
i
En base a la medición de la volatilidad de cada clase de activo, se aplicarán
uno o más factores específicos –acápite xiii)– al nocional efectivo a fin de
obtener la EPE efectiva.
v) Conjuntos de cobertura (“hedging sets”, HS).
a) Los conjuntos de cobertura en las diferentes clases de activos se defini-
rán conforme al siguiente criterio (excepto por lo establecido en los apar-
tados b) y c) de este mismo acápite):
- Derivados sobre tasas de interés: un conjunto de cobertura para
cada moneda.
- Derivados FX: un conjunto de cobertura para cada par de mone-
das.
- Derivados de crédito: un único conjunto de cobertura.
- Derivados sobre acciones: un único conjunto de cobertura.
- Derivados sobre “commodities”: cuatro conjuntos de cobertura,
uno para cada categoría: energía, metales, productos agrícolas y
otros productos básicos.
b) Los derivados que referencian la base (“basis”) entre dos factores de
riesgo y están denominados en una sola moneda (operaciones sobre
base, “basis transactions”) se deberán asignar a conjuntos de cobertura
específicos dentro de la clase de activo correspondiente. Este tratamien-
to no se aplicará a los derivados con dos lados flotantes denominados en
monedas diferentes –tales como los “cross-currency swaps”: acuerdos
para intercambiar pagos de principal e intereses de préstamos denomi-
nados en dos monedas diferentes–, los que recibirán el tratamiento apli-
cable a los contratos FX ordinarios. Hay un conjunto de cobertura para
cada par de factores de riesgo –para cada base específica– dentro del
cual las posiciones se clasificarán en largas o cortas respecto de dicha
base. Cuando se aplique a conjuntos de cobertura de derivados sobre
bases, el SF correspondiente a la clase se multiplicará por 0,5.
c) Los derivados referidos a la volatilidad de un factor de riesgo
–operaciones sobre la volatilidad, tales como los “swaps” de varianza y
volatilidad y las opciones sobre la volatilidad real o implícita– se asigna-
rán a conjuntos específicos dentro de la clase de activo correspondiente.
Los conjuntos de cobertura de volatilidades se formarán siguiendo lo
previsto en el punto a) de este acápite. Cuando se aplique a conjuntos
de cobertura de operaciones sobre la volatilidad, el SF correspondiente a
la clase se multiplicará por 5.
vi) Factor de plazo.
a) Operaciones sin margen de variación: su horizonte temporal mínimo será
el menor entre un año y el plazo residual del contrato de derivados, con
un mínimo de 10 días hábiles.
El nocional ajustado a nivel de operación se multiplicará por un factor de
plazo (“maturity factor”):
donde el numerador es el horizonte temporal mínimo y M es el plazo re-
i
sidual de la operación i –con un mínimo de 10 días hábiles–.
Las unidades del numerador y denominador se expresarán en la misma
unidad de tiempo.
b) Operaciones con margen de variación: el período de riesgo de margen
(“MPOR”) mínimo será el que corresponda conforme a lo siguiente:
− Al menos 10 días hábiles para las operaciones de derivados que no
se liquidan en forma centralizada y están sujetas a acuerdos de már-
genes diarios.
− 5 días hábiles para las operaciones de derivados que se liquidan en
forma centralizada y están sujetas a acuerdos de márgenes diarios
entre el miembro compensador y sus clientes.
− 20 días hábiles para los conjuntos de neteo –excepto aquellos con
una contraparte central– cuyo número de operaciones supere las
5.000 en cualquier momento del trimestre calendario anterior.
− El doble del período de riesgo de margen para los conjuntos de neteo
con disputas pendientes. Si la entidad ha experimentado más de dos
disputas sobre requerimientos de márgenes (“margin calls”) respecto
de algún conjunto de neteo durante los dos trimestres calendario an-
teriores, que se hayan prolongado durante períodos más extensos
que el período de riesgo de margen –que hubiera correspondido sin
tomar en consideración esta regla–, deberá reflejar este antecedente
mediante el uso, durante los dos trimestres calendario posteriores,
de un período de riesgo de margen que sea por lo menos el doble
que el mínimo establecido para ese conjunto de neteo.
El nocional ajustado a nivel de operación se multiplicará por:
donde:
MPOR: período de riesgo de margen correspondiente al acuerdo sobre
i
márgenes aplicable a la operación i. Los mínimos referidos en
este apartado se deberán incrementar cuando la frecuencia de
reposición de márgenes no sea diaria: MPOR = mínimo + N - 1,
i
donde N es la cantidad de días entre reposiciones.
Las unidades del numerador y denominador se deberán expre-
sar en la misma unidad de tiempo. La cantidad de días hábiles
en un año se deberá determinar en función de las convenciones
en el mercado relevante.
vii) Parámetros de correlación regulatorios: (a)
i
Se utilizan sólo en el cálculo de la EPF de los derivados sobre acciones,
créditos y “commodities” –no se aplican a los derivados de tasa de interés o
tipo de cambio– para ponderar los componentes sistemáticos e idiosincrási-
cos y, de esa forma, determinar el grado de compensación entre las opera-
ciones individuales, ya que las coberturas imperfectas sólo permiten una
compensación parcial de los riesgos –acápite xiii)–.
viii) Adicional para los derivados de tasa de interés.
Este adicional captura el riesgo que surge de la correlación imperfecta entre
derivados con plazos diferentes.
Para su cómputo, los derivados se dividirán en tres categorías de plazo
–bandas temporales o “buckets”– sobre la base de la fecha de finalización
de las operaciones, conforme a lo dispuesto en los acápites i) y ii): menos de
un año, entre uno y cinco años y más de cinco años. Se permitirá la com-
pensación total de las posiciones dentro de cada categoría y una compen-
sación parcial entre categorías.
El adicional para los derivados de tasa de interés será la suma del adicional
para cada conjunto de cobertura de derivados sobre tasa de interés con una
contraparte dentro de un conjunto de neteo. El adicional para un conjunto de
cobertura de derivados sobre tasa de interés se computará en dos pasos:
1. Se calculará un nocional efectivo D (IR) por banda temporal k dentro del
jk
conjunto de cobertura (moneda) j:
Donde i{Ccy, MB } se refiere a las operaciones en la moneda j incluidas
j k
en la banda temporal k. El nocional efectivo por banda temporal y mone-
da es la suma de los nocionales ajustados a nivel de operación –acápite
ii)– multiplicados por los ajustes delta regulatorios –acápite iii)– y el factor
por plazo residual –acápite vi)–.
2. La suma entre bandas temporales de un mismo conjunto de cobertura se
calculará conforme a la siguiente expresión:
Las entidades podrán no reconocer las compensaciones entre bandas
temporales, en cuyo caso la fórmula se reducirá a:
El adicional a nivel de conjunto de cobertura será el producto del nocional
efectivo y el factor regulatorio para tasas de interés:
El adicional para todos los conjuntos de cobertura se obtendrá por suma
simple:
ix) Adicional para los derivados de tipo de cambio.
El nocional efectivo de un conjunto de cobertura se computará como la su-
ma de todos los nocionales ajustados a nivel de operación multiplicados por
sus deltas regulatorios.
El adicional para un conjunto de cobertura será el producto de:
- el valor absoluto de su nocional efectivo; y
- el factor regulatorio –que es idéntico para todos los conjuntos de cober-
tura de tipo de cambio–.
El nocional ajustado estará dado por la cantidad de moneda extranjera a la
que hace referencia el contrato, expresada en pesos, conforme a la siguien-
te expresión:
donde se suman todos los conjuntos de cobertura HS incluidos en el conjun-
j
to de neteo. El adicional y el nocional efectivo de cada conjunto de cobertura
HS estarán dados, respectivamente, por:
j
donde iHS refiere a las operaciones en el conjunto de cobertura HS. El
j j
nocional efectivo para cada par de monedas será la sumatoria de los nocio-
nales ajustados a nivel de operación –acápite ii)– multiplicados por los ajus-
tes delta regulatorios –acápite iii)– y el factor plazo –acápite vi)–.
x) Adicional para los derivados de crédito.
Las exposiciones originadas en derivados de crédito estarán sujetas a dos
niveles de compensación:
1. Todos los derivados de crédito que hagan referencia a una misma enti-
dad (un único deudor o un índice) se compensarán plenamente entre sí
y determinarán un nocional efectivo único a nivel de entidad.
donde iEntidad refiere a las operaciones respecto de la entidad k. El
k
nocional efectivo para cada entidad será la sumatoria de los nocionales
ajustados a nivel de operación –acápite ii)– multiplicados por los ajustes
delta regulatorios –acápite iii)– y el factor plazo –acápite vi)–.
El adicional para todas las posiciones que hagan referencia a esta enti-
dad será el producto del nocional efectivo y el factor regulatorio
SF (Crédito):
k
Cuando se referencie a un único deudor, SF (Crédito) se determinará en
k
función de su calificación crediticia. Cuando se trate de un índice,
SF (Crédito) dependerá de si el índice es grado de inversión o especulativo.
k
2. Los adicionales de todas las entidades se agruparán en un único conjun-
to de cobertura –excepto los que correspondan a operaciones sobre ba-
ses y volatilidades– dentro del cual los adicionales de entidades diferen-
tes no se podrán compensar totalmente. Se permitirá una compensación
parcial de los adicionales a nivel de entidad, en base a un modelo de
factor único que permitirá separar el riesgo de esta clase de derivados
en sus componentes sistemático e idiosincrásico.
Los componentes sistemáticos de los adicionales a nivel de entidad se
podrán compensar íntegramente entre sí pero la compensación no esta-
rá disponible para los componentes idiosincrásicos. Ambos componen-
tes se ponderarán por un factor de correlación que determinará el grado
de compensación/cobertura dentro de esta clase de activo. Los deriva-
dos que hagan referencia a índices de crédito se considerarán como si
hicieran referencia a entidades determinadas (“single names”) pero se
les aplicará un mayor factor de correlación:
donde  (Crédito) es el factor de correlación correspondiente a la entidad k.
k
xi) Adicional para los derivados sobre acciones.
Se utilizará un modelo de factor único para dividir el riesgo de cada entidad
de referencia (entidad o índice) en sus componentes sistemático e idiosin-
crásico. Los derivados que hagan referencia a un índice de acciones se tra-
tarán como si hicieran referencia a entidades determinadas pero con un fac-
tor de correlación más alto para el componente sistemático.
Aunque se permitirá la compensación íntegra de las operaciones correspon-
dientes a una entidad, sólo se permitirá la compensación del componente
sistemático del adicional de diferentes entidades. Los adicionales a nivel de
entidad serán proporcionales al producto entre el nocional efectivo y el SF
que corresponde a cada entidad.
donde  (Acción) será el factor de correlación correspondiente a la entidad k. El
k
adicional para todas las posiciones que hagan referencia a la entidad k y su
nocional efectivo estarán dados, respectivamente, por:
y
donde iEntidad referirá a las operaciones respecto de la entidad k. El no-
k
cional efectivo para cada entidad será la sumatoria de los nocionales ajusta-
dos a nivel de operación –acápite ii)–, multiplicados por los ajustes delta re-
gulatorios –acápite iii)– y el factor plazo –acápite vi)–.
xii) Adicional para los derivados sobre “commodities”.
El adicional será la suma para todos los HS:
Se empleará un modelo de un único factor dentro de cada conjunto de co-
bertura para dividir el riesgo correspondiente a un mismo tipo de “commo-
dity” en sus componentes sistemático e idiosincrásico. La compensación o
cobertura total estarán permitidas entre todas las operaciones de derivados
que hagan referencia al mismo tipo de “commodity” –tal como las que se re-
fieran al “petróleo crudo” dentro del conjunto de cobertura “energía”– a fin de
determinar un nocional efectivo a nivel de tipo de “commodity”. La compen-
sación o la cobertura parciales estarán permitidas entre los tipos de “com-
modities” que integran cada conjunto de cobertura –por ejemplo, entre petró-
leo, gas natural, carbón y electricidad– pero se definirán factores regulato-
rios para cada uno. No se permitirá la compensación o cobertura entre con-
juntos de cobertura –tal como energía, metales y productos agrícolas–:
donde (Com) será el factor de correlación correspondiente al conjunto de co-
j
bertura j. El adicional y el nocional efectivo del tipo k de “commodity” estarán
dados, respectivamente, por:
y
donde iTipoj referirá a las operaciones respecto del tipo k de “commodity”
k
dentro del conjunto j. El nocional efectivo para cada tipo de “commodity” se-
rá la suma de los nocionales ajustados a nivel de operación –acápite ii)–,
multiplicados por los ajustes delta regulatorios –acápite iii)– y el factor plazo
–acápite vi)–.
No se podrán hacer coberturas entre las cuatro grandes categorías de deri-
vados sobre “commodities”.
La definición de los conjuntos de cobertura por tipo de “commodity” no toma-
rá en consideración características tales como la calidad o la ubicación. No
obstante, el área de Supervisión y Seguimiento de la SEFyC podrá requerir
el uso de definiciones más precisas si alguna entidad tuviera una exposición
muy significativa al riesgo de base de productos diferentes dentro de deter-
minado tipo de “commodity”.
xiii) Factores regulatorios, correlaciones y adicionales regulatorios por la volatili-
dad de las opciones.
Factor
Volatilidad
Clase aplicable Correlación
Subclase opción
de activo (a)
i
SF (a) σ (a)
i i
tasa de
0,50 % N/A 50 %
interés
tipo de
4 % N/A 15 %
cambio
AAA 0,38 % 50 % 100 %
AA 0,38 % 50 % 100 %
crédito, único A 0,42 % 50 % 100 %
deudor BBB 0,54 % 50 % 100 %
BB 1,06 % 50 % 100 %
B 1,6 % 50 % 100 %
CCC 6 % 50 % 100 %
crédito grado de
0,38 % 80 % 80 %
inversión
índice especulativo 1,06 % 80 % 80 %
acción, único
32 % 50 % 120 %
emisor
acción,
20 % 80 % 75 %
índice
“commodity” electricidad 40 % 40 % 150 %
petróleo/gas 18 % 40 % 70 %
metales 18 % 40 % 70 %
prod. agrícolas 18 % 40 % 70 %
otros 18 % 40 % 70 %
El SF a aplicar a un conjunto de cobertura de operaciones sobre bases será
el que corresponda a la clase de activo pertinente multiplicado por 0,5. El
factor a aplicar a un conjunto de operaciones sobre volatilidades será el que
corresponda a la clase de activo multiplicado por 5 –acápite v)–.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: NOTA: esta unidad tiene contenido tabular y fórmulas detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.

NOTA de E3, nueva: NOTA: esta unidad tiene tablas serializadas por E0 (bloques [TABLA …] … [FIN TABLA …] del texto fuente, verificados contra el documento): su contenido es texto confiable y su omisión se evalúa como la de cualquier otro contenido. Además, E0 detectó en esta unidad contenido tabular fuera de los bloques confiables y fórmulas (flag determinístico): el extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones; ese contenido normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.

## ric::S2

Mensaje de E1, sellado:

```text
Documento fuente: TO_regimen_informativo_contable_mensual_actual.pdf
TO: ric
Tipo de unidad: chunk de punto
Punto del chunk: S2 — Entidades comprendidas.
Puntos admitidos para `punto`: S2

Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_entidad_comprendida_reginf como sujeto.

Texto del punto S2:
```
Sección 2. Entidades comprendidas.
0 Entidad que no consolida, con filiales en el país y en el exterior.
1 Entidad que consolida, con filiales en el país y en el exterior.
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país
y en el exterior) – (con el alcance definido en el punto 6.2. de las normas sobre “Su-
2
pervisión consolidada”)
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y
9 en el exterior -que no consolida con otras entidades financieras-) - (con el alcance defini-
do en el punto 6.2. de las normas sobre “Supervisión consolidada”)
Consolidado trimestral (entidad financiera con filiales, subsidiarias significativas y otros
3
entes en el país y en el exterior) – (código de consolidación suspendido desde
abril/24 según punto 6.1. de las normas sobre “Supervisión consolidada”, excepto
para Ratio de apalancamiento, -Sección 10.- que continuará presentado código 3
con el alcance definido en el punto 6.2. de las normas citadas).
Código 9
No se presentará la información consolidada mensual, debiendo consignar en su lugar una decla-
ración conteniendo los siguientes datos:
- Exigencia por riesgo de crédito (código 70100000).
- Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estan-
darizada (sólo para el último mes del trimestre) (código 70500000).
- Exigencia por riesgo de mercado para las posiciones del último día del mes (código
70800000).
- Exigencia por riesgo operacional (código 70300000).
- Responsabilidad patrimonial computable.
- En los casos que corresponda:
a) Defecto de integración por riesgos de crédito, de mercado y operacional.
b) Incremento de la exigencia de capitales mínimos por excesos en la relación de activos in-
movilizados y otros conceptos, grandes exposiciones al riesgo de crédito, financiamiento al
sector público no financiero, posiciones de derivados no cubiertos, financiaciones a clientes
vinculados y graduación del crédito, por excesos verificados en las posiciones no cubiertas
por “commodities” y por excesos a los límites ampliados de financiamiento al sector público
no financiero por financiaciones o tenencias de instrumentos de deuda de fideicomisos fi-
nancieros o fondos fiduciarios.
c) Detalle de las eventuales franquicias otorgadas y otras facilidades en caso de existir.
d) Reducción de exigencia de riesgo operacional y los datos para su determinación.
Código 3 (consolidación trimestral suspendida desde abril/24 aplicable según lo especifi-
cado en cada caso)
- La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre ba-
jo informe.
- Se incluirán los datos previstos para los códigos 0, 1 y 2, excepto en el caso de riesgo de
mercado y riesgo operacional, donde se informarán únicamente las partidas 70800000 y
70300000 y, de corresponder, 3600000Y y 37000000.
- Para determinar las citadas exigencias se tendrán en cuenta las instrucciones establecidas
para el cómputo mensual, en lo que resulte pertinente.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_regimen_informativo_contable_mensual_actual.pdf
TO: ric
Tipo de unidad: chunk de punto
Punto del chunk: S2 — Entidades comprendidas.
Puntos admitidos para `punto`: S2

Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_entidad_comprendida_reginf en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

FLAGS E0: este chunk contiene contenido tabular (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar en `omisiones` con categoría `tabla`).
E0 detectó tablas que no pudo serializar (`ric::tabla000`): su contenido quedó como texto linealizado, no confiable.

Texto del punto S2:
```
Sección 2. Entidades comprendidas.
CONSOLIDACIÓN
COD CASOS
0 Entidad que no consolida, con filiales en el país y en el exterior.
1 Entidad que consolida, con filiales en el país y en el exterior.
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país
y en el exterior) – (con el alcance definido en el punto 6.2. de las normas sobre “Su-
2
pervisión consolidada”)
Consolidado mensual (entidad financiera con filiales y subsidiarias significativas en el país y
9 en el exterior -que no consolida con otras entidades financieras-) - (con el alcance defini-
do en el punto 6.2. de las normas sobre “Supervisión consolidada”)
Consolidado trimestral (entidad financiera con filiales, subsidiarias significativas y otros
3
entes en el país y en el exterior) – (código de consolidación suspendido desde
abril/24 según punto 6.1. de las normas sobre “Supervisión consolidada”, excepto
para Ratio de apalancamiento, -Sección 10.- que continuará presentado código 3
con el alcance definido en el punto 6.2. de las normas citadas).
Código 9
No se presentará la información consolidada mensual, debiendo consignar en su lugar una decla-
ración conteniendo los siguientes datos:
- Exigencia por riesgo de crédito (código 70100000).
- Cálculo del riesgo de tasa de interés en la cartera de inversión - Medida de riesgo EVE estan-
darizada (sólo para el último mes del trimestre) (código 70500000).
- Exigencia por riesgo de mercado para las posiciones del último día del mes (código
70800000).
- Exigencia por riesgo operacional (código 70300000).
- Responsabilidad patrimonial computable.
- En los casos que corresponda:
a) Defecto de integración por riesgos de crédito, de mercado y operacional.
b) Incremento de la exigencia de capitales mínimos por excesos en la relación de activos in-
movilizados y otros conceptos, grandes exposiciones al riesgo de crédito, financiamiento al
sector público no financiero, posiciones de derivados no cubiertos, financiaciones a clientes
vinculados y graduación del crédito, por excesos verificados en las posiciones no cubiertas
por “commodities” y por excesos a los límites ampliados de financiamiento al sector público
no financiero por financiaciones o tenencias de instrumentos de deuda de fideicomisos fi-
nancieros o fondos fiduciarios.
c) Detalle de las eventuales franquicias otorgadas y otras facilidades en caso de existir.
d) Reducción de exigencia de riesgo operacional y los datos para su determinación.
Código 3 (consolidación trimestral suspendida desde abril/24 aplicable según lo especifi-
cado en cada caso)
- La información tendrá frecuencia trimestral y se integrará con saldos al cierre del trimestre ba-
jo informe.
- Se incluirán los datos previstos para los códigos 0, 1 y 2, excepto en el caso de riesgo de
mercado y riesgo operacional, donde se informarán únicamente las partidas 70800000 y
70300000 y, de corresponder, 3600000Y y 37000000.
- Para determinar las citadas exigencias se tendrán en cuenta las instrucciones establecidas
para el cómputo mensual, en lo que resulte pertinente.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: (sin NOTA)

NOTA de E3, nueva: NOTA: esta unidad tiene contenido tabular detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.

## cap::2.13

Mensaje de E1, sellado:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 2.13 — Partidas fuera de balance. Factores de conversión crediticia (CCF).
Puntos admitidos para `punto`: 2.13, S2

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_alcance_capmin como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S2]
Sección 2. Capital mínimo por riesgo de crédito.
[chapeau_seccion | punto S2]
A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
[chapeau_seccion | punto S2]
(D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB).
[chapeau_seccion | punto S2]
ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezcan.

FLAGS E0: este chunk contiene contenido tabular (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar omisiones en `omisiones_no_prosa`).
  evidencia: rantías financieras– y las aceptaciones y endosos con responsabilidad. 100
  evidencia: obligaciones comerciales–. 50
  evidencia: en función de la contraparte. 20

Texto del punto 2.13:
```
2.13. Partidas fuera de balance. Factores de conversión crediticia (CCF).
Las partidas fuera de balance –incluidos los compromisos por financiaciones y líneas de co-
rresponsalía a entidades del exterior, las garantías otorgadas, los avales otorgados sobre
cheques de pago diferido, los créditos documentarios y aceptaciones, los documentos re-
descontados en otras entidades financieras y otros acuerdos de crédito– se convertirán en
equivalentes crediticios utilizando los siguientes CCF, aplicándose luego los ponderadores
de riesgo establecidos en el punto 2.12. y teniendo en cuenta, de corresponder, las disposi-
ciones establecidas en la Sección 5.:
Concepto CCF
-en %-
i) Sustitutos crediticios directos, tales como las garantías generales de en-
deudamiento –incluidas las cartas de crédito stand-by utilizadas como ga-
rantías financieras– y las aceptaciones y endosos con responsabilidad. 100
ii) Partidas contingentes relacionadas con operaciones comerciales del
cliente –tales como las que se derivan de garantías de cumplimiento de
obligaciones comerciales–. 50
iii) Cartas de crédito comercial de corto plazo –es decir, con plazo residual
de hasta un año– autoliquidables que amparan el movimiento de bienes
–tales como créditos documentarios garantizados mediante la documen-
tación subyacente–. Tanto al banco emisor como al confirmante se les
aplicará el CCF previsto en este acápite y el ponderador que corresponda
en función de la contraparte. 20
iv) Ventas de activos con pacto de recompra –incluso en operaciones de pa-
se– o con responsabilidad para el cedente y, en general, las operaciones
de naturaleza similar, en las que la entidad retiene el riesgo de crédito del
activo (se ponderarán según el activo y no en función de la contraparte).
Se excluye de este tratamiento a los títulos entregados en garantía de las
operaciones con derivados previstos en el punto 4.2. 100
v) Compromisos de adquisición de activos no contabilizados en el balance
de saldos (se ponderarán según el activo y no en función de la contrapar-
te). 100
vi) Líneas de emisión de títulos valores de corto plazo (note issuance facility,
NIF) y líneas rotativas de suscripción de títulos valores (revolving
underwriting facility, RUF), con independencia del plazo de la facilidad
subyacente. 50
vii) Líneas de crédito comprometidas, con independencia del vencimiento de
la facilidad subyacente. 40
viii) Compromisos pasibles de ser cancelados discrecional y unilateralmente
por la entidad financiera, o que se cancelen automáticamente en caso de
deterioro de la solvencia del deudor. 10
Las partidas fuera de balance que refieran a compromisos estarán sujetas al menor de los
CCF que resulten aplicables.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 2.13 — Partidas fuera de balance. Factores de conversión crediticia (CCF).
Puntos admitidos para `punto`: 2.13, S2

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S2]
Sección 2. Capital mínimo por riesgo de crédito.
[chapeau_seccion | punto S2]
A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras
se clasificarán en:
i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local
[chapeau_seccion | punto S2]
(D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor-
tancia sistémica global (G-SIB).
[chapeau_seccion | punto S2]
ii) Grupo 2: entidades financieras no comprendidas en el acápite i).
En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados
grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los
acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezcan.

FLAGS E0: este chunk contiene contenido tabular (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar en `omisiones` con categoría `tabla`).
  evidencia: rantías financieras– y las aceptaciones y endosos con responsabilidad. 100
  evidencia: obligaciones comerciales–. 50
  evidencia: en función de la contraparte. 20

Texto del punto 2.13:
```
2.13. Partidas fuera de balance. Factores de conversión crediticia (CCF).
Las partidas fuera de balance –incluidos los compromisos por financiaciones y líneas de co-
rresponsalía a entidades del exterior, las garantías otorgadas, los avales otorgados sobre
cheques de pago diferido, los créditos documentarios y aceptaciones, los documentos re-
descontados en otras entidades financieras y otros acuerdos de crédito– se convertirán en
equivalentes crediticios utilizando los siguientes CCF, aplicándose luego los ponderadores
de riesgo establecidos en el punto 2.12. y teniendo en cuenta, de corresponder, las disposi-
ciones establecidas en la Sección 5.:
Concepto CCF
-en %-
i) Sustitutos crediticios directos, tales como las garantías generales de en-
deudamiento –incluidas las cartas de crédito stand-by utilizadas como ga-
rantías financieras– y las aceptaciones y endosos con responsabilidad. 100
ii) Partidas contingentes relacionadas con operaciones comerciales del
cliente –tales como las que se derivan de garantías de cumplimiento de
obligaciones comerciales–. 50
iii) Cartas de crédito comercial de corto plazo –es decir, con plazo residual
de hasta un año– autoliquidables que amparan el movimiento de bienes
–tales como créditos documentarios garantizados mediante la documen-
tación subyacente–. Tanto al banco emisor como al confirmante se les
aplicará el CCF previsto en este acápite y el ponderador que corresponda
en función de la contraparte. 20
iv) Ventas de activos con pacto de recompra –incluso en operaciones de pa-
se– o con responsabilidad para el cedente y, en general, las operaciones
de naturaleza similar, en las que la entidad retiene el riesgo de crédito del
activo (se ponderarán según el activo y no en función de la contraparte).
Se excluye de este tratamiento a los títulos entregados en garantía de las
operaciones con derivados previstos en el punto 4.2. 100
v) Compromisos de adquisición de activos no contabilizados en el balance
de saldos (se ponderarán según el activo y no en función de la contrapar-
te). 100
vi) Líneas de emisión de títulos valores de corto plazo (note issuance facility,
NIF) y líneas rotativas de suscripción de títulos valores (revolving
underwriting facility, RUF), con independencia del plazo de la facilidad
subyacente. 50
vii) Líneas de crédito comprometidas, con independencia del vencimiento de
la facilidad subyacente. 40
viii) Compromisos pasibles de ser cancelados discrecional y unilateralmente
por la entidad financiera, o que se cancelen automáticamente en caso de
deterioro de la solvencia del deudor. 10
Las partidas fuera de balance que refieran a compromisos estarán sujetas al menor de los
CCF que resulten aplicables.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: NOTA: esta unidad tiene contenido tabular detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.

NOTA de E3, nueva: NOTA: esta unidad tiene contenido tabular detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no. (igual)

## ric::11.2.3

Mensaje de E1, sellado:

```text
Documento fuente: TO_regimen_informativo_contable_mensual_actual.pdf
TO: ric
Tipo de unidad: chunk de punto
Punto del chunk: 11.2.3 — Cálculo de la medida de riesgo EVE estandarizada.
Puntos admitidos para `punto`: 11.2.3, S11, 11.2

Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_entidad_comprendida_reginf como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S11]
Sección 11. Información complementaria vinculada al cálculo del riesgo de tasa de interés en cartera de inversión.
[encabezado | punto 11.2]
11.2. Modelos de información.
[intro | punto 11.2]
Cuadros 11.2.1. a)
[intro | punto 11.2]
Coef. de CONCEPTOS COMPRENDIDOS B a n d a s T e m p o r a l e s
[intro | punto 11.2]
Escenarios Margen Código
[intro | punto 11.2]
actualización En pesos no actualizables y pesos actualizables 0 1 2 … 19
[intro | punto 11.2]
1/2/3 0 1/2 10101 Activos susceptibles de estandarización a tasa de interés fija
[intro | punto 11.2]
1 0 1/2 10102 Activos susceptibles de estandarización a tasa de interés variable
1 0 1/2 10103 Activos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
1 0 1/2 10104 Activos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
[intro | punto 11.2]
1/2/3 0 1/2 10105 Partidas fuera de Balance a tasa de Interes fija
[intro | punto 11.2]
1 0 1/2 10106 Partidas fuera de Balance a tasa de Interes Variable
[intro | punto 11.2]
0 1/2 10100 Activos susceptibles de estandarización
[intro | punto 11.2]
1/2/3 0 a 6 1/2 20101 Préstamos a tasa fija sujetos al riesgo de cancelación anticipada
[intro | punto 11.2]
Activos no susceptibles de estandarización
[intro | punto 11.2]
1/2/3 0 1/2 30101 Pasivos susceptibles de estandarización a tasa de interés fija
[intro | punto 11.2]
1 0 1/2 30102 Pasivos susceptibles de estandarización a tasa de interés variable
[intro | punto 11.2]
1/2/3 0 1/2 30103 Pasivos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
[intro | punto 11.2]
1 0 1/2 30104 Pasivos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
[intro | punto 11.2]
1/2/3 0 1/2 30105 Partidas fuera de Balance a tasa de Interes fija
[intro | punto 11.2]
1 0 1/2 30106 Partidas fuera de Balance a tasa de Interes Variable
[intro | punto 11.2]
0 1/2 30100 Pasivos susceptibles de estandarización
[intro | punto 11.2]
1 0 1/2 40111 Depósitos sin vencimiento minorista transaccional básicos
1 0 1/2 40112 Depósitos sin vencimiento minorista transaccional no básicos
1 0 1/2 40113 Depósitos sin vencimiento minorista no transaccional básicos
1 0 1/2 40114 Depósitos sin vencimiento minorista no transaccional no básicos
1 0 1/2 40115 Depósitos sin vencimiento mayoristas básicos
1 0 1/2 40116 Depósitos sin vencimiento mayoristas no básicos
[intro | punto 11.2]
0 1/2 40110 Subtotal
[intro | punto 11.2]
1/2/3 0 a 6 1/2 40120 Depósito a plazo sujetos a riesgo de retiro anticipado
[intro | punto 11.2]
Pasivos no susceptibles de estandarización
[intro | punto 11.2]
0 a 6 1/2 50100 FF Netos (CF(k) o CF(tk)) = 10100(0)+20100(x)-30100(0)-40110(0)-40120(x) x=0 a 6 (escenario)
0 a 6 1/2 60100 Factor de descuento compuesto continuo
[intro | punto 11.2]
Cuadro 11.2.1. b)
[intro | punto 11.2]
CONCEPTOS COMPRENDIDOS B a n d a s T e m p o r a l e s
[intro | punto 11.2]
Escenarios Margen Código
[intro | punto 11.2]
En dólares estadounidenses 0 1 2 … 19
[intro | punto 11.2]
0 1/2 10201 Activos susceptibles de estandarización a tasa de interés fija
0 1/2 10202 Activos susceptibles de estandarización a tasa de interés variable
0 1/2 10203 Activos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
0 1/2 10204 Activos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
0 1/2 10205 Partidas fuera de Balance a tasa de Interes fija
0 1/2 10206 Partidas fuera de Balance a tasa de Interes Variable
0 1/2 10200 Activos susceptibles de estandarización
[intro | punto 11.2]
0 a 6 1/2 20201 Préstamos a tasa fija sujetos al riesgo de cancelación anticipada
[intro | punto 11.2]
Activos no susceptibles de estandarización
[intro | punto 11.2]
0 1/2 30201 Pasivos susceptibles de estandarización a tasa de interés fija
0 1/2 30202 Pasivos susceptibles de estandarización a tasa de interés variable
0 1/2 30203 Pasivos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
0 1/2 30204 Pasivos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
0 1/2 30205 Partidas fuera de Balance a tasa de Interes fija
0 1/2 30206 Partidas fuera de Balance a tasa de Interes Variable
0 1/2 30200 Pasivos susceptibles de estandarización
0 1/2 40211 Depósitos sin vencimiento minorista transaccional básicos
0 1/2 40212 Depósitos sin vencimiento minorista transaccional no básicos
0 1/2 40213 Depósitos sin vencimiento minorista no transaccional básicos
0 1/2 40214 Depósitos sin vencimiento minorista no transaccional no básicos
0 1/2 40215 Depósitos sin vencimiento mayoristas básicos
0 1/2 40216 Depósitos sin vencimiento mayoristas no básicos
0 1/2 40210 Subtotal
[intro | punto 11.2]
0 a 6 1/2 40220 Depósito a plazo sujetos a riesgo de retiro anticipado
[intro | punto 11.2]
Pasivos no susceptibles de estandarización
[intro | punto 11.2]
0 a 6 1/2 50200 FF Netos (CF(k) o CF(tk)) = 10200(0)+20200(x)-30200(0)-40210(0)-40220(x) x=0 a 6 (escenario)
0 a 6 1/2 60200 Factor de descuento compuesto continuo
Coef. de CONCEPTOS COMPRENDIDOS B a n d a s T e m p o r a l e s
[intro | punto 11.2]
Escenarios Margen Código
[intro | punto 11.2]
actualización En pesos no actualizables y pesos actualizables 0 1 2 … 19
[intro | punto 11.2]
ACTIVOS
[intro | punto 11.2]
1/2/3 0 a 6 1/2 101010000 Préstamos
1/2/3 0 a 6 1/2 101010100 Sector privado no financiero y residentes en el exterior
1/2/3 0 a 6 1/2 101010101 Hipotecarios sobre la vivienda
1/2/3 0 a 6 1/2 101010102 Con otras garantías hipotecarias
1/2/3 0 a 6 1/2 101010103 Prendarios sobre automotores
1/2/3 0 a 6 1/2 101010104 Con otras garantías prendarias
1/2/3 0 a 6 1/2 101010105 Personales
1/2/3 0 a 6 1/2 101010106 Adelantos
1/2/3 0 a 6 1/2 101010107 Tarjetas de Crédito
1/2/3 0 a 6 1/2 101010108 Sola Firma
1/2/3 0 a 6 1/2 101010109 Documentos descontados
1/2/3 0 a 6 1/2 101010110 Otros
1/2/3 0 a 6 1/2 101010200 Sector público
1/2/3 0 a 6 1/2 101010300 Sector financiero
1/2/3 0 1/2 101020000 Otros créditos por intermediación financiera
1/2/3 0 1/2 101030000 Posición neta compradora de activos financieros no sujetos a riesgo de mercado.
1/2/3 0 1/2 101040000 Otros activos
1/2/3 0 1/2 101050000 Partidas fuera de balance no sujetos a riesgo de mercado.
[intro | punto 11.2]
0 1/2 101000099 Subtotal Activos excluyendo prestamos
[intro | punto 11.2]
0 a 6 1/2 101000000 Subtotal Activos (1)= 101010000(x)+101000099(0) x=0 a 6 (escenario)
[intro | punto 11.2]
PASIVOS
[intro | punto 11.2]
1/2/3 0 a 6 1/2 201010000 Depósitos
[intro | punto 11.2]
1 0 a 6 1/2 201010100 A la vista
[intro | punto 11.2]
1/2/3 0 a 6 1/2 201010200 Otros Depositos
1/2/3 0 a 6 1/2 201010201 Deposito Plazo Fijo Sector Público no Financiero
1/2/3 0 a 6 1/2 201010202 Deposito Plazo Fijo Sector Prívado no Financiero
1/2/3 0 a 6 1/2 201010203 Otros
1/2/3 0 1/2 201020000 Otras obligaciones intermediación financiera
1/2/3 0 1/2 201020100 Obligaciones Negociables
1/2/3 0 1/2 201020200 Otras
1/2/3 0 1/2 201020300 Asistencia del B.C.R.A.
1/2/3 0 1/2 201030000 Posición neta vendedora de activos financieros no sujetos a riesgo de mercado
1/2/3 0 1/2 201040000 Otros pasivos
1/2/3 0 1/2 201050000 Partidas fuera de balance no sujetos a riesgo de mercado.
[intro | punto 11.2]
0 1/2 201000099 Subtotal Pasivos excluyendo depósitos
[intro | punto 11.2]
0 a 6 1/2 201000000 Subtotal Pasivos (2)= 201010000(x)+201000099(0) x=0 a 6 (escenario)
0 a 6 1/2 501000000 FF Netos (1) - (2)
[intro | punto 11.2]
Cuadro 11.2.2. b)
[intro | punto 11.2]
CONCEPTOS COMPRENDIDOS B a n d a s T e m p o r a l e s
[intro | punto 11.2]
Escenarios Margen Código
[intro | punto 11.2]
En dólares estadounidenses 0 1 2 … 19
[intro | punto 11.2]
ACTIVOS
[intro | punto 11.2]
0 a 6 1/2 102010000 Préstamos
0 a 6 1/2 102010100 Sector privado no financiero y residentes en el exterior
0 a 6 1/2 102010101 Hipotecarios sobre la vivienda
0 a 6 1/2 102010102 Con otras garantías hipotecarias
0 a 6 1/2 102010103 Prendarios sobre automotores
0 a 6 1/2 102010104 Con otras garantías prendarias
0 a 6 1/2 102010105 Personales
0 a 6 1/2 102010106 Adelantos
0 a 6 1/2 102010107 Tarjetas de Crédito
0 a 6 1/2 102010108 Sola Firma
0 a 6 1/2 102010109 Documentos descontados
0 a 6 1/2 102010110 Otros
0 a 6 1/2 102010200 Sector público
0 a 6 1/2 102010300 Sector financiero
[intro | punto 11.2]
0 1/2 102020000 Otros créditos por intermediación financiera
0 1/2 102030000 Posición neta compradora de activos financieros no sujetos a riesgo de mercado.
0 1/2 102040000 Otros activos
0 1/2 102050000 Partidas fuera de balance no sujetos a riesgo de mercado.
0 1/2 102000099 Subtotal Activos excluyendo prestamos
[intro | punto 11.2]
0 a 6 1/2 102000000 Subtotal Activos (1)= 101010000(x)+101000099(0) x=0 a 6 (escenario)
[intro | punto 11.2]
PASIVOS
[intro | punto 11.2]
0 a 6 1/2 202010000 Depósitos
0 a 6 1/2 202010100 A la vista
0 a 6 1/2 202010200 Otros Depositos
0 a 6 1/2 202010201 Deposito Plazo Fijo Sector Público no Financiero
0 a 6 1/2 202010202 Deposito Plazo Fijo Sector Prívado no Financiero
0 a 6 1/2 202010203 Otros
[intro | punto 11.2]
0 1/2 202020000 Otras obligaciones intermediación financiera
0 1/2 202020100 Obligaciones Negociables
0 1/2 202020200 Otras
0 1/2 202020300 Asistencia del B.C.R.A.
0 1/2 202030000 Posición neta vendedora de activos financieros no sujetos a riesgo de mercado
0 1/2 202040000 Otros pasivos
0 1/2 202050000 Partidas fuera de balance no sujetos a riesgo de mercado.
0 1/2 202000099 Subtotal Pasivos excluyendo depósitos
[intro | punto 11.2]
0 a 6 1/2 202000000 Subtotal Pasivos (2)= 202010000(x)+202000099(0) x=0 a 6 (escenario)
0 a 6 1/2 502000000 FF Netos (1) - (2)

FLAGS E0: este chunk contiene contenido tabular y fórmulas (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar omisiones en `omisiones_no_prosa`).
  evidencia: Código Concepto Cálculo
  evidencia: 3650000X Suma de pérdidas por escenario ∑ 3610000X/M si es > 0
  evidencia: 3613000X/M KAO
  evidencia: Criterio de asignación de flujos de 1 = Bandas temporales
  evidencia: fondos 2 = Puntos medios
  evidencia: Donde:

Texto del punto 11.2.3:
```
11.2.3. Cálculo de la medida de riesgo EVE estandarizada.
Código Concepto Cálculo
de partida
Medida total del riesgo por opciones
3613000X/M KAO
automáticas
Valor económico del patrimonio
∑ 50100 * 60100
banda k banda k
3612000X/M en pesos
Valor económico del patrimonio
∑ 50200 * 60200
banda k banda k
en ME
Valor económico del patrimonio
∑ 50100 * 60100
banda k banda k
para el escenario 0 en pesos
36110000/M
Valor económico del patrimonio
∑ 50200 * 60200
banda k banda k
para el escenario 0 en ME
Variación del valor económico del 36110000/M – 3612000X/M +
3610000X/M
patrimonio 3613000X/M
3650000X Suma de pérdidas por escenario ∑ 3610000X/M si es > 0
Criterio de asignación de flujos de 1 = Bandas temporales
38000000
fondos 2 = Puntos medios
Donde:
X = Escenarios: de 1 a 6
M = Moneda:
001 = pesos
010 = dólares estadounidenses
k = Banda: de 1 a 19
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_regimen_informativo_contable_mensual_actual.pdf
TO: ric
Tipo de unidad: chunk de punto
Punto del chunk: 11.2.3 — Cálculo de la medida de riesgo EVE estandarizada.
Puntos admitidos para `punto`: 11.2.3, S11, 11.2

Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_entidad_comprendida_reginf en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S11]
Sección 11. Información complementaria vinculada al cálculo del riesgo de tasa de interés en cartera de inversión.
[encabezado | punto 11.2]
11.2. Modelos de información.
[intro | punto 11.2]
Cuadros 11.2.1. a)
[intro | punto 11.2]
[TABLA ric::tabla028 | página 52 | e0_tablas | posicional]
Fila 1: col1 = Coef. de actualización | col2 = Escenarios | col3 = Margen | col4 = Código | col5 = CONCEPTOS COMPRENDIDOS En pesos no actualizables y pesos actualizables | col6 = B a n d a s T e m p o r a l e s ⟨abarca hasta col10⟩
Fila 2: col6 = 0 | col7 = 1 | col8 = 2 | col9 = … | col10 = 19
Fila 3: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 10101 | col5 = Activos susceptibles de estandarización a tasa de interés fija
Fila 4: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10102 | col5 = Activos susceptibles de estandarización a tasa de interés variable
Fila 5: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10103 | col5 = Activos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
Fila 6: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10104 | col5 = Activos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
Fila 7: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 10105 | col5 = Partidas fuera de Balance a tasa de Interes fija
Fila 8: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 10106 | col5 = Partidas fuera de Balance a tasa de Interes Variable
Fila 9: col2 = 0 | col3 = 1/2 | col4 = 10100 | col5 = Activos susceptibles de estandarización
Fila 10: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 20101 | col5 = Préstamos a tasa fija sujetos al riesgo de cancelación anticipada
Fila 11: col5 = Activos no susceptibles de estandarización
Fila 12: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 30101 | col5 = Pasivos susceptibles de estandarización a tasa de interés fija
Fila 13: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 30102 | col5 = Pasivos susceptibles de estandarización a tasa de interés variable
Fila 14: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 30103 | col5 = Pasivos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
Fila 15: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 30104 | col5 = Pasivos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
Fila 16: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 30105 | col5 = Partidas fuera de Balance a tasa de Interes fija
Fila 17: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 30106 | col5 = Partidas fuera de Balance a tasa de Interes Variable
Fila 18: col2 = 0 | col3 = 1/2 | col4 = 30100 | col5 = Pasivos susceptibles de estandarización
Fila 19: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40111 | col5 = Depósitos sin vencimiento minorista transaccional básicos
Fila 20: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40112 | col5 = Depósitos sin vencimiento minorista transaccional no básicos
Fila 21: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40113 | col5 = Depósitos sin vencimiento minorista no transaccional básicos
Fila 22: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40114 | col5 = Depósitos sin vencimiento minorista no transaccional no básicos
Fila 23: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40115 | col5 = Depósitos sin vencimiento mayoristas básicos
Fila 24: col1 = 1 | col2 = 0 | col3 = 1/2 | col4 = 40116 | col5 = Depósitos sin vencimiento mayoristas no básicos
Fila 25: col2 = 0 | col3 = 1/2 | col4 = 40110 | col5 = Subtotal
Fila 26: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 40120 | col5 = Depósito a plazo sujetos a riesgo de retiro anticipado
Fila 27: col5 = Pasivos no susceptibles de estandarización
Fila 28: col2 = 0 a 6 | col3 = 1/2 | col4 = 50100 | col5 = FF Netos (CF(k) o CF(tk)) = 10100(0)+20100(x)-30100(0)-40110(0)-40120(x) x=0 a 6 (escenario)
Fila 29: col2 = 0 a 6 | col3 = 1/2 | col4 = 60100 | col5 = Factor de descuento compuesto continuo
[FIN TABLA ric::tabla028]
[intro | punto 11.2]
Cuadro 11.2.1. b)
[intro | punto 11.2]
[TABLA ric::tabla029 | página 53 | e0_tablas | posicional]
Fila 1: col1 = Escenarios | col2 = Margen | col3 = Código | col4 = CONCEPTOS COMPRENDIDOS En dólares estadounidenses | col5 = B a n d a s T e m p o r a l e s ⟨abarca hasta col9⟩
Fila 2: col5 = 0 | col6 = 1 | col7 = 2 | col8 = … | col9 = 19
Fila 3: col1 = 0 | col2 = 1/2 | col3 = 10201 | col4 = Activos susceptibles de estandarización a tasa de interés fija
Fila 4: col1 = 0 | col2 = 1/2 | col3 = 10202 | col4 = Activos susceptibles de estandarización a tasa de interés variable
Fila 5: col1 = 0 | col2 = 1/2 | col3 = 10203 | col4 = Activos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
Fila 6: col1 = 0 | col2 = 1/2 | col3 = 10204 | col4 = Activos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
Fila 7: col1 = 0 | col2 = 1/2 | col3 = 10205 | col4 = Partidas fuera de Balance a tasa de Interes fija
Fila 8: col1 = 0 | col2 = 1/2 | col3 = 10206 | col4 = Partidas fuera de Balance a tasa de Interes Variable
Fila 9: col1 = 0 | col2 = 1/2 | col3 = 10200 | col4 = Activos susceptibles de estandarización
Fila 10: col1 = 0 a 6 | col2 = 1/2 | col3 = 20201 | col4 = Préstamos a tasa fija sujetos al riesgo de cancelación anticipada
Fila 11: col4 = Activos no susceptibles de estandarización
Fila 12: col1 = 0 | col2 = 1/2 | col3 = 30201 | col4 = Pasivos susceptibles de estandarización a tasa de interés fija
Fila 13: col1 = 0 | col2 = 1/2 | col3 = 30202 | col4 = Pasivos susceptibles de estandarización a tasa de interés variable
Fila 14: col1 = 0 | col2 = 1/2 | col3 = 30203 | col4 = Pasivos susceptibles de estandarización a tasa de interés fija con opciones automáticas implícitas
Fila 15: col1 = 0 | col2 = 1/2 | col3 = 30204 | col4 = Pasivos susceptibles de estandarización a tasa de interés variable con opciones automáticas implícitas
Fila 16: col1 = 0 | col2 = 1/2 | col3 = 30205 | col4 = Partidas fuera de Balance a tasa de Interes fija
Fila 17: col1 = 0 | col2 = 1/2 | col3 = 30206 | col4 = Partidas fuera de Balance a tasa de Interes Variable
Fila 18: col1 = 0 | col2 = 1/2 | col3 = 30200 | col4 = Pasivos susceptibles de estandarización
Fila 19: col1 = 0 | col2 = 1/2 | col3 = 40211 | col4 = Depósitos sin vencimiento minorista transaccional básicos
Fila 20: col1 = 0 | col2 = 1/2 | col3 = 40212 | col4 = Depósitos sin vencimiento minorista transaccional no básicos
Fila 21: col1 = 0 | col2 = 1/2 | col3 = 40213 | col4 = Depósitos sin vencimiento minorista no transaccional básicos
Fila 22: col1 = 0 | col2 = 1/2 | col3 = 40214 | col4 = Depósitos sin vencimiento minorista no transaccional no básicos
Fila 23: col1 = 0 | col2 = 1/2 | col3 = 40215 | col4 = Depósitos sin vencimiento mayoristas básicos
Fila 24: col1 = 0 | col2 = 1/2 | col3 = 40216 | col4 = Depósitos sin vencimiento mayoristas no básicos
Fila 25: col1 = 0 | col2 = 1/2 | col3 = 40210 | col4 = Subtotal
Fila 26: col1 = 0 a 6 | col2 = 1/2 | col3 = 40220 | col4 = Depósito a plazo sujetos a riesgo de retiro anticipado
Fila 27: col4 = Pasivos no susceptibles de estandarización
Fila 28: col1 = 0 a 6 | col2 = 1/2 | col3 = 50200 | col4 = FF Netos (CF(k) o CF(tk)) = 10200(0)+20200(x)-30200(0)-40210(0)-40220(x) x=0 a 6 (escenario)
Fila 29: col1 = 0 a 6 | col2 = 1/2 | col3 = 60200 | col4 = Factor de descuento compuesto continuo
[FIN TABLA ric::tabla029]
[intro | punto 11.2]
[TABLA ric::tabla030 | página 54 | e0_tablas | posicional]
Fila 1: col1 = Coef. de actualización | col2 = Escenarios | col3 = Margen | col4 = Código | col5 = CONCEPTOS COMPRENDIDOS En pesos no actualizables y pesos actualizables | col6 = B a n d a s T e m p o r a l e s ⟨abarca hasta col10⟩
Fila 2: col6 = 0 | col7 = 1 | col8 = 2 | col9 = … | col10 = 19
Fila 3: col5 = ACTIVOS
Fila 4: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010000 | col5 = Préstamos
Fila 5: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010100 | col5 = Sector privado no financiero y residentes en el exterior
Fila 6: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010101 | col5 = Hipotecarios sobre la vivienda
Fila 7: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010102 | col5 = Con otras garantías hipotecarias
Fila 8: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010103 | col5 = Prendarios sobre automotores
Fila 9: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010104 | col5 = Con otras garantías prendarias
Fila 10: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010105 | col5 = Personales
Fila 11: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010106 | col5 = Adelantos
Fila 12: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010107 | col5 = Tarjetas de Crédito
Fila 13: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010108 | col5 = Sola Firma
Fila 14: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010109 | col5 = Documentos descontados
Fila 15: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010110 | col5 = Otros
Fila 16: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010200 | col5 = Sector público
Fila 17: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 101010300 | col5 = Sector financiero
Fila 18: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101020000 | col5 = Otros créditos por intermediación financiera
Fila 19: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101030000 | col5 = Posición neta compradora de activos financieros no sujetos a riesgo de mercado.
Fila 20: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101040000 | col5 = Otros activos
Fila 21: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 101050000 | col5 = Partidas fuera de balance no sujetos a riesgo de mercado.
Fila 22: col2 = 0 | col3 = 1/2 | col4 = 101000099 | col5 = Subtotal Activos excluyendo prestamos
Fila 23: col2 = 0 a 6 | col3 = 1/2 | col4 = 101000000 | col5 = Subtotal Activos (1)= 101010000(x)+101000099(0) x=0 a 6 (escenario)
Fila 24: col5 = PASIVOS
Fila 25: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010000 | col5 = Depósitos
Fila 26: col1 = 1 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010100 | col5 = A la vista
Fila 27: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010200 | col5 = Otros Depositos
Fila 28: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010201 | col5 = Deposito Plazo Fijo Sector Público no Financiero
Fila 29: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010202 | col5 = Deposito Plazo Fijo Sector Prívado no Financiero
Fila 30: col1 = 1/2/3 | col2 = 0 a 6 | col3 = 1/2 | col4 = 201010203 | col5 = Otros
Fila 31: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020000 | col5 = Otras obligaciones intermediación financiera
Fila 32: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020100 | col5 = Obligaciones Negociables
Fila 33: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020200 | col5 = Otras
Fila 34: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201020300 | col5 = Asistencia del B.C.R.A.
Fila 35: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201030000 | col5 = Posición neta vendedora de activos financieros no sujetos a riesgo de mercado
Fila 36: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201040000 | col5 = Otros pasivos
Fila 37: col1 = 1/2/3 | col2 = 0 | col3 = 1/2 | col4 = 201050000 | col5 = Partidas fuera de balance no sujetos a riesgo de mercado.
Fila 38: col2 = 0 | col3 = 1/2 | col4 = 201000099 | col5 = Subtotal Pasivos excluyendo depósitos
Fila 39: col2 = 0 a 6 | col3 = 1/2 | col4 = 201000000 | col5 = Subtotal Pasivos (2)= 201010000(x)+201000099(0) x=0 a 6 (escenario)
Fila 40: col2 = 0 a 6 | col3 = 1/2 | col4 = 501000000 | col5 = FF Netos (1) - (2)
[FIN TABLA ric::tabla030]
[intro | punto 11.2]
Cuadro 11.2.2. b)
[intro | punto 11.2]
[TABLA ric::tabla031 | página 55 | e0_tablas | posicional]
Fila 1: col1 = Escenarios | col2 = Margen | col3 = Código | col4 = CONCEPTOS COMPRENDIDOS En dólares estadounidenses | col5 = B a n d a s T e m p o r a l e s ⟨abarca hasta col9⟩
Fila 2: col5 = 0 | col6 = 1 | col7 = 2 | col8 = … | col9 = 19
Fila 3: col4 = ACTIVOS
Fila 4: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010000 | col4 = Préstamos
Fila 5: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010100 | col4 = Sector privado no financiero y residentes en el exterior
Fila 6: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010101 | col4 = Hipotecarios sobre la vivienda
Fila 7: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010102 | col4 = Con otras garantías hipotecarias
Fila 8: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010103 | col4 = Prendarios sobre automotores
Fila 9: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010104 | col4 = Con otras garantías prendarias
Fila 10: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010105 | col4 = Personales
Fila 11: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010106 | col4 = Adelantos
Fila 12: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010107 | col4 = Tarjetas de Crédito
Fila 13: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010108 | col4 = Sola Firma
Fila 14: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010109 | col4 = Documentos descontados
Fila 15: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010110 | col4 = Otros
Fila 16: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010200 | col4 = Sector público
Fila 17: col1 = 0 a 6 | col2 = 1/2 | col3 = 102010300 | col4 = Sector financiero
Fila 18: col1 = 0 | col2 = 1/2 | col3 = 102020000 | col4 = Otros créditos por intermediación financiera
Fila 19: col1 = 0 | col2 = 1/2 | col3 = 102030000 | col4 = Posición neta compradora de activos financieros no sujetos a riesgo de mercado.
Fila 20: col1 = 0 | col2 = 1/2 | col3 = 102040000 | col4 = Otros activos
Fila 21: col1 = 0 | col2 = 1/2 | col3 = 102050000 | col4 = Partidas fuera de balance no sujetos a riesgo de mercado.
Fila 22: col1 = 0 | col2 = 1/2 | col3 = 102000099 | col4 = Subtotal Activos excluyendo prestamos
Fila 23: col1 = 0 a 6 | col2 = 1/2 | col3 = 102000000 | col4 = Subtotal Activos (1)= 101010000(x)+101000099(0) x=0 a 6 (escenario)
Fila 24: col4 = PASIVOS
Fila 25: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010000 | col4 = Depósitos
Fila 26: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010100 | col4 = A la vista
Fila 27: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010200 | col4 = Otros Depositos
Fila 28: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010201 | col4 = Deposito Plazo Fijo Sector Público no Financiero
Fila 29: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010202 | col4 = Deposito Plazo Fijo Sector Prívado no Financiero
Fila 30: col1 = 0 a 6 | col2 = 1/2 | col3 = 202010203 | col4 = Otros
Fila 31: col1 = 0 | col2 = 1/2 | col3 = 202020000 | col4 = Otras obligaciones intermediación financiera
Fila 32: col1 = 0 | col2 = 1/2 | col3 = 202020100 | col4 = Obligaciones Negociables
Fila 33: col1 = 0 | col2 = 1/2 | col3 = 202020200 | col4 = Otras
Fila 34: col1 = 0 | col2 = 1/2 | col3 = 202020300 | col4 = Asistencia del B.C.R.A.
Fila 35: col1 = 0 | col2 = 1/2 | col3 = 202030000 | col4 = Posición neta vendedora de activos financieros no sujetos a riesgo de mercado
Fila 36: col1 = 0 | col2 = 1/2 | col3 = 202040000 | col4 = Otros pasivos
Fila 37: col1 = 0 | col2 = 1/2 | col3 = 202050000 | col4 = Partidas fuera de balance no sujetos a riesgo de mercado.
Fila 38: col1 = 0 | col2 = 1/2 | col3 = 202000099 | col4 = Subtotal Pasivos excluyendo depósitos
Fila 39: col1 = 0 a 6 | col2 = 1/2 | col3 = 202000000 | col4 = Subtotal Pasivos (2)= 202010000(x)+202000099(0) x=0 a 6 (escenario)
Fila 40: col1 = 0 a 6 | col2 = 1/2 | col3 = 502000000 | col4 = FF Netos (1) - (2)
[FIN TABLA ric::tabla031]

TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `ric::tabla032` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque; 6 celdas que abarcan varias columnas (⟨abarca hasta c⟩). ATENCIÓN, 2 filas de subtítulo: no son datos; cada una califica a las filas que la siguen.
FLAGS E0: este chunk contiene fórmulas (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar en `omisiones` con categoría `formula`).
  evidencia: Criterio de asignación de flujos de 1 = Bandas temporales
  evidencia: fondos 2 = Puntos medios
  evidencia: Donde:

Texto del punto 11.2.3:
```
11.2.3. Cálculo de la medida de riesgo EVE estandarizada.
[TABLA ric::tabla032 | página 56 | e0_tablas | posicional]
Fila 1: col2 = Código | col4 = Concepto | col5 = Cálculo
Fila 2: col2 = de partida
Fila 3: col1 = 3613000X/M ⟨abarca hasta col3⟩ | col4 = Medida total del riesgo por opciones automáticas | col5 = KAO
Fila 4: col1 = 3612000X/M ⟨abarca hasta col3⟩ | col4 = Valor económico del patrimonio en pesos | col5 = ∑ 50100 * 60100 banda k banda k
Fila 5: col4 = Valor económico del patrimonio en ME | col5 = ∑ 50200 * 60200 banda k banda k
Fila 6: col1 = 36110000/M ⟨abarca hasta col3⟩ | col4 = Valor económico del patrimonio para el escenario 0 en pesos | col5 = ∑ 50100 * 60100 banda k banda k
Fila 7: col4 = Valor económico del patrimonio para el escenario 0 en ME | col5 = ∑ 50200 * 60200 banda k banda k
Fila 8: col1 = 3610000X/M ⟨abarca hasta col3⟩ | col4 = Variación del valor económico del patrimonio | col5 = 36110000/M – 3612000X/M + 3613000X/M
Fila 9: col1 = 3650000X ⟨abarca hasta col3⟩ | col4 = Suma de pérdidas por escenario | col5 = ∑ 3610000X/M si es > 0
Fila 10: col1 = 38000000 ⟨abarca hasta col3⟩ | col4 = Criterio de asignación de flujos de fondos | col5 = 1 = Bandas temporales 2 = Puntos medios
[FIN TABLA ric::tabla032]
Donde:
X = Escenarios: de 1 a 6
M = Moneda:
001 = pesos
010 = dólares estadounidenses
k = Banda: de 1 a 19
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: NOTA: esta unidad tiene contenido tabular y fórmulas detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.

NOTA de E3, nueva: NOTA: esta unidad tiene tablas serializadas por E0 (bloques [TABLA …] … [FIN TABLA …] del texto fuente, verificados contra el documento): su contenido es texto confiable y su omisión se evalúa como la de cualquier otro contenido. E0 dejó sin resolver parte de la estructura de ric::tabla032 (2 filas de subtítulo): la omisión `tabla` que el extractor declare sobre esa tabla no es faltante. Además, E0 detectó en esta unidad fórmulas (flag determinístico): el extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones; ese contenido normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.

## cla::5.1.1.1

Mensaje de E1, sellado:

```text
Documento fuente: TO_clasificacion_deudores_actual.pdf
TO: cla
Tipo de unidad: chunk de punto
Punto del chunk: 5.1.1.1 — Los créditos para consumo o vivienda.
Puntos admitidos para `punto`: 5.1.1.1, S5, 5.1, 5.1.1

Alcance de este TO: Sujeto_rol_obligado_a_clasificar_clasificacion = {Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP)}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_obligado_a_clasificar_clasificacion como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S5]
Sección 5. Categorías de carteras.
[encabezado | punto 5.1]
5.1. Categorías.
[intro | punto 5.1]
La cartera se agrupará en dos categorías básicas:
[encabezado | punto 5.1.1]
5.1.1. Cartera comercial.
[intro | punto 5.1.1]
Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

Texto del punto 5.1.1.1:
```
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_clasificacion_deudores_actual.pdf
TO: cla
Tipo de unidad: chunk de punto
Punto del chunk: 5.1.1.1 — Los créditos para consumo o vivienda.
Puntos admitidos para `punto`: 5.1.1.1, S5, 5.1, 5.1.1

Alcance de este TO: Sujeto_rol_obligado_a_clasificar_clasificacion = {Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP)}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_obligado_a_clasificar_clasificacion en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (contexto y anclaje; NO extraigas contenido normativo de estos bloques, salvo un caso: el último bloque abre la lista de la que este punto es un ítem, así que la norma del ítem se compone con ese encabezado — ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA):
[encabezado | punto S5]
Sección 5. Categorías de carteras.
[encabezado | punto 5.1]
5.1. Categorías.
[intro | punto 5.1]
La cartera se agrupará en dos categorías básicas:
[encabezado | punto 5.1.1]
5.1.1. Cartera comercial.
[intro | punto 5.1.1]
Abarca todas las financiaciones comprendidas, con excepción de las siguientes:

Texto del punto 5.1.1.1:
```
5.1.1.1. Los créditos para consumo o vivienda.
Los créditos de esta clase que superen el equivalente a dos veces el importe de
referencia establecido en el punto 3.7. y cuyo repago no se encuentre vinculado
a ingresos fijos o periódicos del cliente sino a la evolución de su actividad pro-
ductiva o comercial se incluirán dentro de la cartera comercial.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: (sin NOTA)

NOTA de E3, nueva: (sin NOTA) (igual)

## ctacte::2.3.4.1

Mensaje de E1, sellado:

```text
Documento fuente: ctacte.pdf
TO: ctacte
Tipo de unidad: chunk de punto
Punto del chunk: 2.3.4.1 — Tasa de interés anual contractualmente pactada, en tanto por ciento con dos
Puntos admitidos para `punto`: 2.3.4.1, S2, 2.3, 2.3.4

Alcance de este TO: Sujeto_banco = {Bancos}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_banco como sujeto. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S2]
Sección 2. Movimiento de las cuentas.
[encabezado | punto 2.3]
2.3. Intereses.
[encabezado | punto 2.3.4]
2.3.4. Se deberá especificar:

Texto del punto 2.3.4.1:
```
2.3.4.1. Tasa de interés anual contractualmente pactada, en tanto por ciento con dos
decimales.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: ctacte.pdf
TO: ctacte
Tipo de unidad: chunk de punto
Punto del chunk: 2.3.4.1 — Tasa de interés anual contractualmente pactada, en tanto por ciento con dos
Puntos admitidos para `punto`: 2.3.4.1, S2, 2.3, 2.3.4

Alcance de este TO: Sujeto_banco = {Bancos}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_banco en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (contexto y anclaje; NO extraigas contenido normativo de estos bloques, salvo un caso: el último bloque abre la lista de la que este punto es un ítem, así que la norma del ítem se compone con ese encabezado — ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA):
[encabezado | punto S2]
Sección 2. Movimiento de las cuentas.
[encabezado | punto 2.3]
2.3. Intereses.
[encabezado | punto 2.3.4]
2.3.4. Se deberá especificar:

Texto del punto 2.3.4.1:
```
2.3.4.1. Tasa de interés anual contractualmente pactada, en tanto por ciento con dos
decimales.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: (sin NOTA)

NOTA de E3, nueva: (sin NOTA) (igual)

## ext::4.8.6::intro

Mensaje de E1, sellado:

```text
Documento fuente: TO_exterior_cambios_actual.pdf
TO: ext
Tipo de unidad: MINI-CHUNK de bloque estructural (intro del punto 4.8.6)
Unidad de origen: 4.8.6 — [bloque intro] En el caso de que un cliente haya concretado una operación de venta con obligación
Puntos admitidos para `punto`: 4.8.6

Alcance de este TO: Sujeto_rol_entidad_autorizada_exterior = {Entidades financieras, Entidades cambiarias}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_entidad_autorizada_exterior como sujeto.

Cadena de títulos (ubica el bloque; NO es contenido a extraer):
[encabezado | punto S4]
Sección 4. Otras disposiciones específicas.
[encabezado | punto 4.8]
4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
[encabezado | punto 4.8.6]
4.8.6. En el caso de que un cliente haya concretado una operación de venta con obligación

Texto del bloque intro del punto 4.8.6 (TU unidad de extracción):
```
de recompra utilizando los bonos BOPREAL adquiridos en una suscripción primaria
complementariamente será aplicable lo siguiente:
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_exterior_cambios_actual.pdf
TO: ext
Tipo de unidad: MINI-CHUNK de bloque estructural (intro del punto 4.8.6)
Unidad de origen: 4.8.6 — [bloque intro] En el caso de que un cliente haya concretado una operación de venta con obligación
Puntos admitidos para `punto`: 4.8.6

Alcance de este TO: Sujeto_rol_entidad_autorizada_exterior = {Entidades financieras, Entidades cambiarias}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_entidad_autorizada_exterior en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Cadena de títulos (ubica el bloque; NO es contenido a extraer):
[encabezado | punto S4]
Sección 4. Otras disposiciones específicas.
[encabezado | punto 4.8]
4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
[encabezado | punto 4.8.6]
4.8.6. En el caso de que un cliente haya concretado una operación de venta con obligación

Texto del bloque intro del punto 4.8.6 (TU unidad de extracción):
```
de recompra utilizando los bonos BOPREAL adquiridos en una suscripción primaria
complementariamente será aplicable lo siguiente:
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: (sin NOTA)

NOTA de E3, nueva: NOTA: esta unidad es el encabezado de una lista (su texto termina en «:»); los ítems son los puntos que siguen, cada uno con su propia unidad. En esta extracción se componen en cada ítem el sujeto, la modalidad y el cuantificador del encabezado, y también lo que el encabezado fija para cada ítem (un plazo, un ámbito, una condición que vale para todos los ítems). Esta unidad no emite un nodo por el solo anuncio de la lista ni repite lo que se compone en los ítems: que falten aquí no es faltante. Sí es faltante, si no fue extraído, lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista entera, o la norma principal cuando los ítems son sus supuestos o condiciones.

## ext::4.8.6.1

Mensaje de E1, sellado:

```text
Documento fuente: TO_exterior_cambios_actual.pdf
TO: ext
Tipo de unidad: chunk de punto
Punto del chunk: 4.8.6.1 — la venta de los títulos en el origen de la operación no deberá tenerse en
Puntos admitidos para `punto`: 4.8.6.1, S4, 4.8, 4.8.6

Alcance de este TO: Sujeto_rol_entidad_autorizada_exterior = {Entidades financieras, Entidades cambiarias}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, usá Sujeto_rol_entidad_autorizada_exterior como sujeto.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S4]
Sección 4. Otras disposiciones específicas.
[encabezado | punto 4.8]
4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
[intro | punto 4.8]
Argentina Libre (BOPREAL).
[encabezado | punto 4.8.6]
4.8.6. En el caso de que un cliente haya concretado una operación de venta con obligación
[intro | punto 4.8.6]
de recompra utilizando los bonos BOPREAL adquiridos en una suscripción primaria
complementariamente será aplicable lo siguiente:

Texto del punto 4.8.6.1:
```
4.8.6.1. la venta de los títulos en el origen de la operación no deberá tenerse en
cuenta a los efectos de la confección de las declaraciones juradas previstas
en los puntos 3.16.3.1. y 3.16.3.2., en línea con lo previsto en el primer
párrafo del punto 4.8.2.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to', todo elemento con `punto` de la lista admitida.
```

Mensaje de E1, nuevo:

```text
Documento fuente: TO_exterior_cambios_actual.pdf
TO: ext
Tipo de unidad: chunk de punto
Punto del chunk: 4.8.6.1 — la venta de los títulos en el origen de la operación no deberá tenerse en
Puntos admitidos para `punto`: 4.8.6.1, S4, 4.8, 4.8.6

Alcance de este TO: Sujeto_rol_entidad_autorizada_exterior = {Entidades financieras, Entidades cambiarias}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_entidad_autorizada_exterior en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (contexto y anclaje; NO extraigas contenido normativo de estos bloques, salvo un caso: el último bloque abre la lista de la que este punto es un ítem, así que la norma del ítem se compone con ese encabezado — ver COMPOSICIÓN CON EL ENCABEZADO DE UNA LISTA):
[encabezado | punto S4]
Sección 4. Otras disposiciones específicas.
[encabezado | punto 4.8]
4.8. Disposiciones complementarias asociadas a los Bonos para la Reconstrucción de una
[intro | punto 4.8]
Argentina Libre (BOPREAL).
[encabezado | punto 4.8.6]
4.8.6. En el caso de que un cliente haya concretado una operación de venta con obligación
[intro | punto 4.8.6]
de recompra utilizando los bonos BOPREAL adquiridos en una suscripción primaria
complementariamente será aplicable lo siguiente:

Texto del punto 4.8.6.1:
```
4.8.6.1. la venta de los títulos en el origen de la operación no deberá tenerse en
cuenta a los efectos de la confección de las declaraciones juradas previstas
en los puntos 3.16.3.1. y 3.16.3.2., en línea con lo previsto en el primer
párrafo del punto 4.8.2.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, sellada: (sin NOTA)

NOTA de E3, nueva: (sin NOTA) (igual)

## cap::6.2.2.6 con `cap::tabla037` en la lista de tablas forzadas a residual (demostración)

Mensaje de E1, nuevo, con la tabla forzada:

```text
Documento fuente: TO_capitales_minimos_actual.pdf
TO: cap
Tipo de unidad: chunk de punto
Punto del chunk: 6.2.2.6 — Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
Puntos admitidos para `punto`: 6.2.2.6, S6, 6.2, 6.2.2

Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.

Contexto estructural heredado (SOLO contexto y anclaje: NO extraigas contenido normativo de estos bloques — cada uno tiene su propia unidad de extracción; ver PROVENANCE):
[encabezado | punto S6]
Sección 6. Capital mínimo por riesgo de mercado.
[encabezado | punto 6.2]
6.2. Exigencia de capital por riesgo de tasa de interés.
[intro | punto 6.2]
La exigencia de capital por el riesgo de tasa de interés se deberá calcular respecto de los títu-
los de deuda y otros instrumentos imputados a la cartera de negociación, incluidas las accio-
nes preferidas no convertibles.
Un título valor vendido y recomprado a término en una operación de pase pasivo o en otro tipo
de operación de financiación con títulos valores se tratará como si todavía fuese propiedad de
la entidad cedente; es decir, recibirá el mismo tratamiento que un título en cartera.
Las acciones preferidas convertibles a un precio predeterminado en acciones ordinarias de la
emisora se tratarán según cómo se negocien, como títulos de deuda o como acciones.
La exigencia se obtendrá como la suma de dos exigencias calculadas por separado: una por
el riesgo específico de cada instrumento, ya sea que se trate de una posición vendida o com-
prada, y otra por el riesgo general de mercado –vinculado al efecto de cambios en la tasa de
interés sobre la cartera–, en la que se podrán compensar las posiciones compradas y vendi-
das en diferentes instrumentos.
Para los instrumentos derivados, serán de aplicación las disposiciones establecidas en el pun-
to 6.2.3.
[encabezado | punto 6.2.2]
6.2.2. Exigencia de capital por riesgo general de mercado: método de los plazos residuales.

FLAGS E0: este chunk contiene contenido tabular (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar en `omisiones` con categoría `tabla`).
Tablas serializadas por E0 que se tratan como contenido NO-CONFIABLE (`cap::tabla037`): no copies sus valores; registrá la omisión `tabla` con su tramo.

Texto del punto 6.2.2.6:
```
6.2.2.6. Como resultado de lo previsto en el punto 6.2.2.5. se obtendrá un conjunto de
posiciones netas compradas, un conjunto de posiciones netas vendidas y las
desestimaciones verticales. Luego, las entidades podrán realizar dos series de
compensaciones horizontales: primero, entre las posiciones netas dentro de
cada una de las tres zonas en las que se agrupan las bandas temporales y,
luego, entre las posiciones netas de las tres zonas. Dichas compensaciones
estarán sujetas a la siguiente escala de desestimaciones horizontales
-exigencias adicionales- expresadas como porcentajes de las posiciones que
se compensan:
[TABLA cap::tabla037 | página 125 | e0_tablas | posicional]
Fila 1: col1 = Zona | col2 = Banda | col3 = Porcentaje de desestimación aplicable: ⟨abarca hasta col5⟩
Fila 2: col3 = dentro de zona | col4 = entre zonas adyacentes | col5 = entre zonas 1 y 3
Fila 3: col2 = Meses*
Fila 4: col1 = 1 | col2 = 0-1 | col3 = 40%
Fila 5: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 1-3 | col3 = 40% ⟨combinada con fila 4⟩
Fila 6: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 3-6 | col3 = 40% ⟨combinada con fila 4⟩
Fila 7: col1 = 1 ⟨combinada con fila 4⟩ | col2 = 6-12 | col3 = 40% ⟨combinada con fila 4⟩
Fila 8: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 9: col1 = 2 | col2 = 1-2 | col3 = 30%
Fila 10: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 2-3 | col3 = 30% ⟨combinada con fila 9⟩ | col5 = 100%
Fila 11: col1 = 2 ⟨combinada con fila 9⟩ | col2 = 3-4 | col3 = 30% ⟨combinada con fila 9⟩
Fila 12: col1 = Años* ⟨abarca hasta col3⟩ | col4 = 40%
Fila 13: col1 = 3 | col2 = 4-5 | col3 = 30%
Fila 14: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 5-7 | col3 = 30% ⟨combinada con fila 13⟩
Fila 15: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 7-10 | col3 = 30% ⟨combinada con fila 13⟩
Fila 16: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 10-15 | col3 = 30% ⟨combinada con fila 13⟩
Fila 17: col1 = 3 ⟨combinada con fila 13⟩ | col2 = 15-20 | col3 = 30% ⟨combinada con fila 13⟩
Fila 18: col2 = Más de 20
[FIN TABLA cap::tabla037]
ei se puede simplificar menciones a “meses” y “años”ese
*
Al efecto de imputar una posición a la escala de vencimientos cuando el plazo residual o el plazo que
resta hasta el siguiente ajuste del interés, según el caso, es igual al límite entre dos bandas, correspon-
derá realizar la imputación a la banda temporal más próxima a la fecha de cálculo.
```

Extraé las entidades y relaciones según el schema. Recordá: nodo TextoOrdenado con local_id='to'; todo elemento con `punto` de la lista admitida; toda entidad con su `tramo`; toda relación de sujeto con su `sujeto_mencion`; `omisiones` siempre (vacía si no omitiste nada).
```

NOTA de E3, nueva, con la tabla forzada: NOTA: esta unidad tiene contenido tabular detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.
