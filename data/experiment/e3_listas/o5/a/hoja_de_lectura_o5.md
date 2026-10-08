# U-E3-LISTAS, O5: hoja de lectura (veredictos con los casos resueltos contra los de O3)

## docvig::3.3.2 — O3: 1 faltantes (1 bloq) | O5: 1 (1 bloq), completo_ok=False
- O3 [0] C otro, alta, bloq True: «No es obligatoria la entrega de constancias del CUIT/CUIL por rectificación en nombre, apellido u otros datos de identificación, excepto en modificaciones del n» — esta Excepcion (e5) y la Condicion (e6) no corresponden a ningún contenido del texto fuente de 3.3.2: el punto no menciona CUIT/CUIL ni distingue entre nombre/apellido y número de documento; parecen contenido de otra unidad (posiblemente 3.3.1 o 3.3.3) incorporado erróneamente aquí
- O5 [0] CANDIDATO otro, alta, bloq True, cita verificada False: «No es obligatoria la entrega de constancias del CUIT/CUIL por rectificación en nombre, apellido u otros datos de identificación, excepto en modificaciones del número de documento de identidad» — esta cita no existe en el texto fuente del punto 3.3.2; la entidad e5 (Excepcion) y su relación exceptua_obligacion introducen contenido normativo (sobre CUIT/CUIL) que no figura en el texto fuente provisto para esta unidad, no representando una omisión sino una fabricación de contenido no presente

## ext::2.6.1.1 — O3: 1 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True
- O3 [0] - calificador_despojado, media, bloq False: «en la medida que se cumpla la
totalidad de las siguientes condiciones:» — el cuantificador 'totalidad' (se exigen todas las condiciones, no basta una) no quedó reflejado en la descripción de la Condicion extraída

## ext::2.6.1.2 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.3.3.1 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.3.3.2 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.5.3.5 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.5.4.3 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.5.6.1 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.5.6.2 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.5.6.7 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.6.1.1 — O3: 2 faltantes (0 bloq) | O5: 1 (0 bloq), completo_ok=False
- O3 [0] B2 calificador_despojado, media, bloq False: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses» — la excepción compuesta (e2) omite el calificador temporal 'a partir de su vencimiento' que condiciona cuándo procede la cancelación de capital e intereses
- O3 [1] - otro, baja, bloq False: «3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y» — encabezado truncado del punto 3.6 que podría contener alcance normativo adicional sobre títulos de deuda, no representado ni declarado
- O5 [0] CANDIDATO calificador_despojado, media, bloq False, cita verificada True: «excepto la cancelación de giros en descubierto en cuentas corrientes en dólares estadounidenses que sólo podrá efectuarse con fondos en esa moneda de libre disponibilidad del cliente.» — e3 está tipificada como Restriccion/prohibicion pero el fuente dice 'que sólo podrá efectuarse con...': es una facultad condicionada (modalidad de permiso restringido a un medio de pago), no una prohibición pura; la modalidad deóntica del fragmento quedó invertida/perdida

## ext::3.6.1.2 — O3: 1 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True
- O3 [0] B excepcion_ausente, baja, bloq False: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses» — la excepción está capturada como entidad (e2), pero no hay relación exceptua_obligacion entre e2 y una entidad que represente la prohibición principal (e1 es Operacion, no la Prohibicion); la relación entre e2 y la norma que exceptúa quedó sin modelar explícitamente como vínculo de excepción

## ext::3.6.1.6 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.6.4.1 — O3: 1 faltantes (1 bloq) | O5: 1 (1 bloq), completo_ok=False
- O3 [0] B otro, alta, bloq True: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la» — El ítem es de tipo 'contenidos' (supuesto/excepción que exime la conformidad previa), por lo que debía llevar la norma compuesta con sujeto, modalidad y cuantificador del encabezado: que el acceso al mercado de cambios para esta operación NO requiere conformidad previa del BCRA por encuadrar en esta
- O5 [0] CANDIDATO otro, alta, bloq True, cita verificada True: «La deuda se origina en financiaciones en moneda extranjera otorgadas por
entidades financieras locales por los consumos en moneda extranjera
efectuados mediante tarjetas de crédito o de compra.» — Según la regla de composición, al tratarse de una excepción (miembro que queda afuera de la exigencia de conformidad previa), el ítem debería llevar la norma compuesta con el encabezado: que el acceso al mercado de cambios para esta operación NO requiere conformidad previa del BCRA (la excepción misma). Lo extraído solo modela la Operación y su Condición, pero ninguna entidad ni relación expresa que esta situación queda exceptuada de la conformidad previa — no hay nodo Excepcion que conecte esta situación con la norma del encabezado 3.6.4.

## ext::3.6.4.2 — O3: 2 faltantes (0 bloq) | O5: 2 (1 bloq), completo_ok=False
- O3 [0] B otro, media, bloq False: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
conformidad previa del BCRA excepto que la operación encuadre en alguna de las
sigu» — El extractor declaró este tramo como meta_normativo, pero en realidad fija la norma troncal (exigencia de conformidad previa del BCRA, con la excepción general que habilita los supuestos del 3.6.4.x) y el cuantificador 'totalidad de las condiciones' que rige el ítem; no es mero sentido u objetivo si
- O3 [1] O calificador_despojado, baja, bloq False: «canceladas en forma simultánea con la liquidación
de fondos desde el exterior por nuevos endeudamientos» — la cláusula final de la excepción interna (sobre giros en descubierto) está presente casi verbatim en e1, por lo que no hay pérdida sustancial; se marca baja solo porque el matiz 'por nuevos endeudamientos' podría leerse como recorte frente a 'nuevo endeudamiento financiero' de e2, aunque la sustanc
- O5 [0] calificador_despojado, media, bloq False, cita verificada True: «el monto acumulado de los vencimientos de capital del nuevo
endeudamiento en ningún momento, hasta la fecha de vencimiento de la
deuda que se cancela, podrá superar el monto que hubieran acumulado
los vencimientos de cap» — la Restriccion e4 perdió el calificador temporal 'en ningún momento, hasta la fecha de vencimiento de la deuda que se cancela' que fija cuándo rige el límite acumulado; la descripción y el campo umbrales quedaron con el verbo invertido ('podrá superar' en vez de 'no podrá superar')
- O5 [1] modalidad_perdida, alta, bloq True, cita verificada True: «podrá superar el monto que hubieran acumulado los vencimientos de capital de la financiación a precancelar» — el campo 'umbrales' de e4 copia la cláusula sin la negación ('no podrá superar'), invirtiendo la modalidad prohibitiva del fuente a una facultativa

## ext::3.13.1.1 — O3: 0 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True

## ext::3.13.1.6 — O3: 0 faltantes (0 bloq) | O5: 1 (0 bloq), completo_ok=False
- O5 [0] CANDIDATO otro, baja, bloq False, cita verificada True: «requerirá la conformidad previa del BCRA, excepto para las operaciones de:» — el ítem debería estar representado como Excepcion (queda afuera de la exigencia de conformidad previa) y no como Operacion con Condicion; el extractor declaró la relación como relacion_sin_predicado pero no capturó que e1 es en sustancia una excepción al régimen de conformidad previa, lo cual es parte del encabezado compuesto que corresponde al ítem según las reglas de composición

## ext::3.13.1.10 — O3: 2 faltantes (0 bloq) | O5: 0 (0 bloq), completo_ok=True
- O3 [0] - enumeracion_incompleta, media, bloq False: «el acceso se concrete en forma simultánea con la liquidación de
fondos ingresados desde el exterior por endeudamientos financieros
comprendidos en el punto 3.5.» — la condición e2 omite que los endeudamientos financieros deben estar 'comprendidos en el punto 3.5', un calificador que precisa a cuáles endeudamientos se refiere (no cualquier endeudamiento, solo los del punto 3.5)
- O3 [1] - calificador_despojado, media, bloq False: «o fondos
provenientes de un préstamo
financiero en moneda extranjera otorgada por una entidad financiera
local a partir de una línea de crédito de entidad finan» — la descripción de e2 habla genéricamente de 'préstamos financieros en moneda extranjera' pero omite que deben provenir de una entidad financiera LOCAL a partir de una línea de crédito de una entidad financiera DEL EXTERIOR, un calificador que precisa el origen y canal del financiamiento

## ext::3.16.2.1 — O3: 2 faltantes (1 bloq) | O5: 1 (1 bloq), completo_ok=False
- O3 [0] B modalidad_perdida, alta, bloq True: «la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto» — el extractor declaró este tramo como meta_normativo (omisión no-prosa), pero en realidad es la norma que habilita la facultad de la entidad de aceptar una declaración jurada alternativa cuando el cliente supera el umbral de USD 100.000; esa facultad (modalidad 'podrá') no quedó representada en ningu
- O3 [1] - enumeracion_incompleta, media, bloq False: «En esta última declaración jurada del cliente deberá constar expresamente
el valor de sus activos externos líquidos disponibles al inicio del día y los
montos q» — la obligación o1 representa esta cláusula pero su calificador 'en esta última declaración jurada' (la del segundo párrafo, no la del primer párrafo) no queda claro en la descripción extraída, que no distingue a cuál de las dos declaraciones juradas se refiere
- O5 [0] CANDIDATO modalidad_perdida, alta, bloq True, cita verificada True: «la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto al considerar que, parcial o totalmente, los activos externos líquidos:» — el fuente enmarca las excepciones e1-e7 como una facultad ('también podrá aceptar') de la entidad, no como una aceptación automática; ese carácter facultativo fue declarado por el extractor como [meta_normativo] pero en realidad es la modalidad deóntica que rige las siete excepciones extraídas, y ninguna descripción de e1-e7 lo recoge

## ext::3.18.1.1 — O3: 2 faltantes (2 bloq) | O5: 2 (1 bloq), completo_ok=False
- O3 [0] - modalidad_perdida, alta, bloq True: «podrá acceder al mercado de cambios por hasta el monto de la certificación para realizar» — el ítem debía componerse con la modalidad facultativa ('podrá acceder') y el cuantificador ('hasta el monto de la certificación') del encabezado; lo extraído solo modela la operación y una restricción, sin representar la facultad de acceso ni el límite cuantitativo del monto certificado que el encab
- O3 [1] - calificador_despojado, alta, bloq True: «Los clientes que cuenten con una “Certificación de aumento de las exportaciones de bienes en el año 2021” o “Certificación de aumento de las exportaciones de bi» — el sujeto habilitado (clientes con alguna de las certificaciones de aumento de exportaciones) que el encabezado fija para la norma compuesta no está representado en ninguna entidad ni relación del ítem
- O5 [0] modalidad_perdida, alta, bloq True, cita verificada True: «podrá acceder al mercado de cambios por hasta el monto de la certificación para realizar:» — el ítem compone con el encabezado la facultad 'podrá acceder' y el límite cuantitativo 'por hasta el monto de la certificación'; lo extraído modela e1 como Operacion simple sin la modalidad de facultad ni el tope cuantitativo que el encabezado fija para cada ítem
- O5 [1] calificador_despojado, media, bloq False, cita verificada True: «Los clientes que cuenten con una "Certificación de aumento de las exportaciones de bienes en el año 2021" o "Certificación de aumento de las exportaciones de bienes en el año 2022" o "Certificación de aumento de las expo» — el sujeto que el encabezado fija (clientes con alguna de las tres certificaciones) no quedó compuesto en ninguna entidad del ítem
