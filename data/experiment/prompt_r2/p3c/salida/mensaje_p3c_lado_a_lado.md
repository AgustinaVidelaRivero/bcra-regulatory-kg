# Mensaje de E1 y NOTAS de E3: congelado y P3c, en unidades de control

## e: la línea «Alcance de este TO» (mensaje de E1)

### ric::4.1.1.1

Congelado:

```text
Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_entidad_comprendida_reginf en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.
```

P3c:

```text
Alcance de este TO: Sujeto_rol_entidad_comprendida_reginf = {Entidades financieras}. Cuando el texto (el de tu unidad o el heredado) nombre al colectivo del TO con una expresión genérica ('las entidades', 'los sujetos obligados'), sugerí Sujeto_rol_entidad_comprendida_reginf en `sujeto_id`, con esa expresión copiada del texto como `sujeto_mencion`. Si el texto no nombra a ningún sujeto, no emitas la relación: este alcance no reemplaza la mención. Es el sujeto de aplica_a cuando el texto se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.
```

### cap::8.5.1

Congelado:

```text
Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando la norma se dirija genéricamente a 'las entidades' / 'los sujetos obligados' / el colectivo del TO, sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con la expresión del texto como `sujeto_mencion`. Es el sujeto de aplica_a cuando la norma se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.
```

P3c:

```text
Alcance de este TO: Sujeto_rol_alcance_capmin = {Entidades financieras}. Cuando el texto (el de tu unidad o el heredado) nombre al colectivo del TO con una expresión genérica ('las entidades', 'los sujetos obligados'), sugerí Sujeto_rol_alcance_capmin en `sujeto_id`, con esa expresión copiada del texto como `sujeto_mencion`. Si el texto no nombra a ningún sujeto, no emitas la relación: este alcance no reemplaza la mención. Es el sujeto de aplica_a cuando el texto se dirige al colectivo; NO es el ejecutor por defecto en ejecuta.
```

### docvig::3.3::cierre

Congelado:

```text
(sin línea de alcance)
```

P3c:

```text
(sin línea de alcance)
```

## a: NOTA de E3 de las omisiones de esquema

Congelado:

```text
NOTA: el extractor declaró, en las omisiones, tramos que el esquema deja afuera a propósito: [meta_normativo] (contenido sobre el sentido, el alcance, el objetivo o la vigencia de una norma, que no prescribe la conducta de nadie), [fuera_de_tipos] (contenido normativo que ningún tipo del esquema representa) y [relacion_sin_predicado] (un vínculo que ningún predicado del esquema representa). Un tramo declarado así no es un faltante: no lo reclames. Sí es un faltante si lo declarado no es lo que dice su categoría (por ejemplo, un deber o una prohibición declarados como meta-normativos).
```

P3c:

```text
NOTA: el extractor declaró, en las omisiones, tramos que el esquema deja afuera a propósito: [meta_normativo] (contenido sobre el sentido, el objetivo o la entrada en vigencia de una norma, que no prescribe la conducta de nadie ni dice a quién o a qué se aplica), [fuera_de_tipos] (contenido normativo que ningún tipo del esquema representa) y [relacion_sin_predicado] (un vínculo que ningún predicado del esquema representa). Un tramo declarado así no es un faltante: no lo reclames. Sí es un faltante si lo declarado no es lo que dice su categoría: un deber, una prohibición, una facultad, una condición, una excepción, un alcance o una modalidad declarados como meta-normativos.
```

## b: última oración de la NOTA de E3 del encabezado de lista

Congelado:

```text
Sí es faltante, si no fue extraído, lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista entera, o la norma principal cuando los ítems son sus supuestos o condiciones.
```

P3c:

```text
Sí es faltante, si no fue extraído, lo que el encabezado enuncia aparte de la lista: una norma propia, una excepción a la lista entera, la norma principal cuando los ítems son sus supuestos o condiciones, o la norma y su excepción cuando los ítems son las condiciones de esa excepción.
```

## f: `cap::tabla037` a residual

### cap::6.2.2.6: bloque de tablas del mensaje de E1

Congelado:

```text
TABLAS SERIALIZADAS POR E0 en el texto (CONFIABLES: leelas y copiá sus valores, ver CONTENIDO NO-PROSA del sistema):
- `cap::tabla037` (posicional): sin encabezado de columnas reconocido: las claves son colN y el nombre de cada columna está en las primeras filas del bloque; 18 celdas con un valor propagado desde otra fila (⟨combinada con fila n⟩); 3 celdas que abarcan varias columnas (⟨abarca hasta c⟩). ATENCIÓN, 1 fila de subtítulo: no es un dato; califica a las filas que la siguen. ATENCIÓN, 20 celdas combinadas que E0 no asignó a sus filas: el valor de cada una puede valer para varias filas y el bloque no indica cuáles. Si el texto no lo aclara, no lo asocies a ninguna fila: registrá la omisión `tabla` con su tramo.
```

P3c:

```text
FLAGS E0: este chunk contiene contenido tabular (detección determinística). Ese contenido está declarado NO-CONFIABLE: aplicá la sección CONTENIDO NO-PROSA del sistema (no reconstruir, no forzar extracción, registrar en `omisiones` con categoría `tabla`).
Tablas serializadas por E0 que se tratan como contenido NO-CONFIABLE (`cap::tabla037`): no copies sus valores; registrá la omisión `tabla` con su tramo.
```

### cap::6.2.2.6: NOTA de E3

Congelado:

```text
NOTA: esta unidad tiene tablas serializadas por E0 (bloques [TABLA …] … [FIN TABLA …] del texto fuente, verificados contra el documento): su contenido es texto confiable y su omisión se evalúa como la de cualquier otro contenido. E0 dejó sin resolver parte de la estructura de cap::tabla037 (20 celdas combinadas sin asignar a sus filas y 1 fila de subtítulo): la omisión `tabla` que el extractor declare sobre esa tabla no es faltante.
```

P3c:

```text
NOTA: esta unidad tiene contenido tabular detectados determinísticamente (flag de E0). El extractor tenía instrucción de NO reconstruir ese contenido y declarar las omisiones. Evaluá el tratamiento: contenido tabular/fórmula normativo ni extraído ni declarado es faltante tipo contenido_tabular_no_declarado; declarado, no.
```
