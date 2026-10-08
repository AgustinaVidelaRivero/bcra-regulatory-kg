# U-UNION-ESTRECHA, U2-b: hoja de las divergencias para la adjudicación de la autora

Primera lectura: `lectura1_u2.json` (`8b23d250…`, sello de las 10:58:04 del 08/10/2026). Segunda lectura, a ciegas, de la mesa: `lectura2_u2.json` (`7d7cda3a…`, sello de las 14:25:18 del 08/10/2026), escrita y sellada antes de abrir la primera. Las dos con las fichas y el criterio de `sello_fichas_u2.txt` (10:54:03).

## Acuerdo

- Coinciden 29 de 29 fichas.
- Kappa de Cohen: no definido: el acuerdo esperado por azar es 1 (cada lectura usa una sola categoría, la misma en las dos) y kappa = (po - pe) / (1 - pe) queda 0/0.
- La cuenta de correctas no va en esta hoja: sale en el FRENO U2, después de la adjudicación.

Comando: `python3 -I -B comparar_lecturas_U2b.py data/experiment/union_estrecha/u2 data/experiment/union_estrecha/u2`. El script está en el paquete de revisión de U2-b, con copia permanente en `~/INGENIERIA IA/TESIS/fuera_del_repo/scratchpads/839a4403-7812-4d4d-8ebd-f348c03bb676/scratchpad/revision_UUNION_ESTRECHA_FRENO_U2b/`.

## Divergencias

Ninguna: los dos veredictos coinciden en las 29 fichas.

## Declaradas para la adjudicación, sin divergencia

En U28 y U29 las dos lecturas declaran en la nota que el tramo de la Condicion no está en el texto propio del ítem sino en la intro de 10.4.2, que la unidad del ítem hereda: la Condicion es la cláusula que subordina la lista y no el contenido del ítem. El despacho deja ese caso a la autora; van con el mismo campo vacío.

### U28

- Condicion: `Condicion_verificacion_previa_de_cumplimiento_de_requisitos__se_verifica_previamente_que_s_df31a0`
- **Primera lectura:** `correcta`
  - tramo (`ext::10.4.2::intro`): «La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:»
  - nota: El tramo de la Condicion no sale del texto propio del ítem 10.4.2.9 (la convalidación en el sistema online) sino de la cláusula del bloque que abre la lista, que el ítem hereda: «en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos». La Condicion es la de su tramo (precisión 5) y, así leída, es condición de la potestad según el texto. Que la Condicion no recoja el contenido del ítem es un defecto de la extracción, no de la unión (precisión 1).
- **Segunda lectura:** `correcta`
  - tramo (`ext::10.4.2::intro`): «La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos»
  - nota: DECLARADO PARA LA ADJUDICACIÓN: el tramo de la Condicion no está en el texto propio del ítem 10.4.2.9 (la convalidación en el sistema en línea) sino en la intro de 10.4.2 que hereda la unidad del ítem (el tramo declara punto 10.4.2). La Condicion es la cláusula que subordina la lista, no el contenido del ítem. Apliqué el criterio tal cual (precisiones 1 y 6): tal como la identifica su tramo, es, según el texto, condición de la Potestad del nodo destino.

Veredicto de la autora: ______

### U29

- Condicion: `Condicion_verificacion_previa_de_requisitos__la_entidad_debe_verificar_previamente_que_se__9bd7a4`
- **Primera lectura:** `correcta`
  - tramo (`ext::10.4.2::intro`): «La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos:»
  - nota: Igual que U28: el tramo de la Condicion es la cláusula del bloque que abre la lista, heredada por el ítem 10.4.2.5, y no su texto propio (la razonabilidad de los montos y el párrafo de los USD 5 millones). Leída por su tramo, es condición de la potestad según el texto; no recoger el contenido del ítem es un defecto de la extracción, no de la unión (precisión 1).
- **Segunda lectura:** `correcta`
  - tramo (`ext::10.4.2::intro`): «La entidad podrá dar acceso al mercado de cambios para el pago al exterior en la medida que verifique previamente que se cumplen la totalidad de los siguientes requisitos»
  - nota: DECLARADO PARA LA ADJUDICACIÓN: el tramo de la Condicion no está en el texto propio del ítem 10.4.2.5 (la razonabilidad de los montos) sino en la intro de 10.4.2 que hereda la unidad del ítem (el tramo declara punto 10.4.2). La Condicion es la cláusula que subordina la lista, no el contenido del ítem. Apliqué el criterio tal cual (precisiones 1 y 6): tal como la identifica su tramo, es, según el texto, condición de la Potestad del nodo destino. Mismo caso que U28.

Veredicto de la autora: ______

## Notas coincidentes, sin campo de adjudicación

Las dos lecturas señalan, con el mismo veredicto, dos puntos más que la autora puede querer mirar: U24 (el tramo del nodo destino es el encabezado de 5.8.2, heredado, y el boleto global diario sale de la intro de 5.8) y U25 (la Condicion recoge solo el inciso final del ítem 2.7.3, «considerando los límites…», leído con el cierre de 2.7). Sus tramos y notas completas están en `lectura1_u2.json` y `lectura2_u2.json`.
