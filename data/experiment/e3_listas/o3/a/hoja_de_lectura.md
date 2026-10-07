# U-E3-LISTAS, O3 (a): hoja de lectura (veredictos nuevos contra los reclamos viejos del intento 0)

## docvig::3.3.2 — bloque [intro | punto 3.3]; tanda 0: reintento=False, cola=cola_humana_veredicto_inutilizable
- VIEJO C (otro, alta, bloq True): «Excepción — constancia CUIT/CUIL no obligatoria» — la entidad e5 y la condición e6 introducen contenido (excepción de CUIT/CUIL, supuestos de nombre/apellido/número de documento) que no aparece en el texto fuente de este punto; el fuente de 3.3.2 no menciona CUIT/CUIL ni describe los supuestos de 3.1.2/3.1.3/3.1.4, por lo que no es verificable contra el fuente dado
- NUEVO: completo_ok=False aceptable=False faltantes=1
  - [0] CANDIDATO otro, alta, bloq True, cita verificada False: «No es obligatoria la entrega de constancias del CUIT/CUIL por rectificación en nombre, apellido u otros datos de identificación, excepto en modificaciones del número de documento de identidad» — esta Excepcion (e5) y la Condicion (e6) no corresponden a ningún contenido del texto fuente de 3.3.2: el punto no menciona CUIT/CUIL ni distingue entre nombre/apellido y número de documento; parecen contenido de otra unidad (posiblemente 3.3.1 o 3.3.3) incorporado erróneamente aquí

## ext::2.6.1.1 — bloque [intro | punto 2.6.1]; tanda 0: reintento=False, cola=cola_humana
- VIEJO B (otro, media, bloq False): «2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los» — El encabezado heredado 2.6 enuncia el objeto normativo (una excepción de liquidación de cobros de exportaciones) del cual depende el punto propio; su sustancia (que existe una excepción a la obligación de liquidar cobros de exportaciones) no está representada por ninguna entidad, solo referenciada como nota textual en la omisión declarada.
- NUEVO: completo_ok=False aceptable=True faltantes=1
  - [0] calificador_despojado, media, bloq False, cita verificada True: «en la medida que se cumpla la
totalidad de las siguientes condiciones:» — el cuantificador 'totalidad' (se exigen todas las condiciones, no basta una) no quedó reflejado en la descripción de la Condicion extraída

## ext::2.6.1.2 — bloque [intro | punto 2.6.1]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «2.6. Excepción de liquidación de cobros de exportaciones de bienes y servicios para los» — el encabezado heredado 2.6 enuncia que se trata de una excepción a la obligación de liquidación de cobros de exportaciones; este marco normativo (qué se exceptúa y para quién) no está representado: lo extraído solo captura la condición puntual del inciso 2.6.1.2 sin la excepción que la contiene
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.3.3.1 — bloque [intro | punto 3.3.3]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «Se requerirá la conformidad previa del BCRA cuando el acreedor sea una contraparte» — la obligación troncal (conformidad previa del BCRA cuando el acreedor sea una contraparte) que el punto 3.3.3.1 condiciona/excepciona no está representada como entidad propia (ni Obligacion ni Restriccion) en la unidad ni en el contexto heredado; solo se modela la Excepcion, pero la norma exceptuada no figura en ningún nodo
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.3.3.2 — bloque [intro | punto 3.3.3]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «3.3.3. Se requerirá la conformidad previa del BCRA cuando el acreedor sea una contraparte» — El requisito troncal de conformidad previa del BCRA, respecto del cual el punto 3.3.3.2 opera como excepción/condición, no está representado por ninguna entidad propia en lo extraído de esta unidad (la descripción de e1 lo menciona tangencialmente como 'supuesto en que no se requiere', pero no hay nodo Obligacion/Restriccion que porte el mandato del encabezado 3.3.3 en esta unidad ni en otra decla
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.5.3.5 — bloque [intro | punto 3.5.3]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «3.5.3. El acceso al mercado de cambios se produce con una anterioridad no mayor a los 3» — el encabezado heredado 3.5.3 enuncia la condición temporal troncal (anterioridad no mayor a 3 ... días/meses, texto cortado) respecto de la cual el punto 3.5.3.5 es una excepción; esa norma de base no está representada por ninguna entidad ni descripción, lo que impide entender a qué requisito se excepciona exactamente el VPU-RIGI
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.5.4.3 — bloque [intro | punto 3.5.4]; tanda 0: reintento=True, cola=None
- VIEJO B2 (excepcion_ausente, alta, bloq True): «3.5.4. En la medida que se encuentre vigente el requisito de conformidad previa del BCRA» — la cláusula condicional que enmarca todo el punto 3.5.4.3 (la vigencia del requisito de conformidad previa del BCRA, cuya suspensión depende del cumplimiento de las condiciones enumeradas) no está representada en ninguna entidad ni descripción de esta unidad; el extractor la declaró como relacion_sin_predicado pero el contenido de la condición/excepción en sí (de qué depende la vigencia del requis
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.5.6.1 — bloque [intro | punto 3.5.6]; tanda 0: reintento=True, cola=cola_humana
- VIEJO B (modalidad_perdida, alta, bloq True): «3.5.6. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios» — el extractor reconstruyó la norma exceptuada ('requisito de conformidad previa del BCRA para cancelación de capital e intereses de endeudamientos financieros cuando el acreedor sea contraparte vinculada') en la descripcion de la Excepcion, pero esa descripción no coincide con el texto del encabezado 3.5.6 que realmente rige esta unidad ('para el acceso al mercado de cambios'); el mandato propio de
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.5.6.2 — bloque [intro | punto 3.5.6]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «3.5.6. Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios» — el encabezado heredado 3.5.6 enuncia la norma troncal (conformidad previa requerida salvo las excepciones listadas en sus incisos); el punto 3.5.6.2 es solo uno de los supuestos que exceptúan esa exigencia, pero el mandato general no figura representado en ninguna entidad ni descripción
- VIEJO C (otro, alta, bloq True): «cuando el acreedor sea contraparte vinculada» — la descripción de e1 agrega la condición 'cuando el acreedor sea contraparte vinculada' que no aparece en el texto fuente del punto 3.5.6.2; esto sugiere que el extractor incorporó contenido de otro punto (posiblemente 3.5.6.1) no presente en esta unidad, lo cual indica que el contexto que define a qué excepción se refiere este inciso no está debidamente respaldado por el fuente de esta unidad
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.5.6.7 — bloque [intro | punto 3.5.6]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «Se requerirá la conformidad previa del BCRA para el acceso al mercado de cambios» — La norma troncal heredada (la obligación de conformidad previa del BCRA que el punto 3.5.6.7 exceptúa) no está representada por ninguna entidad propia; solo existe el nodo Excepcion, sin la Obligacion exceptuada conectada mediante exceptua_obligacion.
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.6.1.1 — bloque [intro | punto 3.6.1]; tanda 0: reintento=True, cola=cola_humana
- VIEJO C (otro, alta, bloq True): «3.6.1.1. las financiaciones en moneda extranjera otorgadas por entidades financieras
locales, incluyendo los pagos por los consumos en moneda extranjera
efectua» — El punto 3.6.1.1 es en sí mismo un ítem de la enumeración de excepciones a la prohibición general del 3.6.1 (acceso al mercado de cambios para pago de deudas), según el encabezado heredado declarado como omisión 'excepto para la cancelación en el país ... de:'. La extracción invierte la estructura: modela 3.6.1.1 como si el acceso para financiaciones estuviera prohibido (e2 lo presenta como 'excep
- NUEVO: completo_ok=False aceptable=True faltantes=2
  - [0] CANDIDATO calificador_despojado, media, bloq False, cita verificada True: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses» — la excepción compuesta (e2) omite el calificador temporal 'a partir de su vencimiento' que condiciona cuándo procede la cancelación de capital e intereses
  - [1] otro, baja, bloq False, cita verificada True: «3.6. Pagos de títulos de deuda u otros valores representativos de deuda denominados y» — encabezado truncado del punto 3.6 que podría contener alcance normativo adicional sobre títulos de deuda, no representado ni declarado

## ext::3.6.1.2 — bloque [intro | punto 3.6.1]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras» — la norma troncal que establece la prohibición (encabezado heredado del 3.6.1) no está representada como entidad propia (Prohibicion/Obligacion); solo aparece referenciada en la descripcion de la Excepcion y en una relación declarada como 'relacion_sin_predicado' que menciona un (e3) que no existe entre las entidades extraídas — la prohibición en sí carece de nodo que la porte
- NUEVO: completo_ok=False aceptable=True faltantes=1
  - [0] CANDIDATO excepcion_ausente, baja, bloq False, cita verificada True: «excepto para la cancelación en el país a partir de su vencimiento de capital e intereses» — la excepción está capturada como entidad (e2), pero no hay relación exceptua_obligacion entre e2 y una entidad que represente la prohibición principal (e1 es Operacion, no la Prohibicion); la relación entre e2 y la norma que exceptúa quedó sin modelar explícitamente como vínculo de excepción

## ext::3.6.1.6 — bloque [intro | punto 3.6.1]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «3.6.1. Se prohíbe el acceso al mercado de cambios para el pago de deudas y otras» — la obligación troncal que la excepción recorta (prohibición de acceso al mercado de cambios para pago de deudas) no está representada por ninguna entidad propia; e1 la menciona de forma incidental en su descripcion pero no existe un nodo Prohibicion establecido en 3.6.1 al cual e1 exceptúe mediante exceptua_obligacion
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.6.4.1 — bloque [intro | punto 3.6.4]; tanda 0: reintento=True, cola=None
- VIEJO B (modalidad_perdida, alta, bloq True): «3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la» — El encabezado de la lista establece que el acceso anticipado 'requerirá la conformidad previa del BCRA' excepto que encuadre en alguno de los ítems listados (entre ellos 3.6.4.1). El extractor lo declaró como meta_normativo, pero en realidad es la modalidad deóntica (requisito de conformidad previa, con excepción si se cumplen las condiciones del ítem) que rige al ítem 3.6.4.1: no es un tramo sobr
- NUEVO: completo_ok=False aceptable=False faltantes=1
  - [0] CANDIDATO otro, alta, bloq True, cita verificada True: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la» — El ítem es de tipo 'contenidos' (supuesto/excepción que exime la conformidad previa), por lo que debía llevar la norma compuesta con sujeto, modalidad y cuantificador del encabezado: que el acceso al mercado de cambios para esta operación NO requiere conformidad previa del BCRA por encuadrar en esta situación. En cambio, la extracción solo representa la operación (e1) y una Condicion (e2) sin ninguna entidad que porte la dispensa/excepción de conformidad previa resultante; el extractor declaró el encabezado como meta_normativo, pero en realidad contiene la norma principal (requisito de conform

## ext::3.6.4.2 — bloque [intro | punto 3.6.4]; tanda 0: reintento=True, cola=cola_humana
- VIEJO B (otro, alta, bloq True): «3.6.4. El acceso al mercado de cambios con anterioridad al vencimiento requerirá la» — el extractor declaró esta cláusula como meta_normativo, pero en realidad es la norma troncal que establece el requisito de conformidad previa del BCRA y la excepción general que habilita que los ítems del 3.6.4.2 (incisos i-iv) operen como condiciones liberatorias; no es contenido sobre el sentido u objetivo de la norma sino un mandato con sujeto y condición propios, no representado en ninguna ent
- NUEVO: completo_ok=False aceptable=True faltantes=2
  - [0] CANDIDATO otro, media, bloq False, cita verificada True: «El acceso al mercado de cambios con anterioridad al vencimiento requerirá la
conformidad previa del BCRA excepto que la operación encuadre en alguna de las
siguientes situaciones y se cumplan la total» — El extractor declaró este tramo como meta_normativo, pero en realidad fija la norma troncal (exigencia de conformidad previa del BCRA, con la excepción general que habilita los supuestos del 3.6.4.x) y el cuantificador 'totalidad de las condiciones' que rige el ítem; no es mero sentido u objetivo sino la norma compuesta que el ítem hereda. Su mala categorización puede ocultar que la condición de 'cumplimiento de la totalidad' no quedó explícita como cuantificador de las Condiciones e2/e3/e4.
  - [1] CANDIDATO calificador_despojado, baja, bloq False, cita verificada True: «canceladas en forma simultánea con la liquidación
de fondos desde el exterior por nuevos endeudamientos» — la cláusula final de la excepción interna (sobre giros en descubierto) está presente casi verbatim en e1, por lo que no hay pérdida sustancial; se marca baja solo porque el matiz 'por nuevos endeudamientos' podría leerse como recorte frente a 'nuevo endeudamiento financiero' de e2, aunque la sustancia se conserva.

## ext::3.13.1.1 — bloque [intro | punto 3.13.1]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no» — el encabezado heredado 3.13.1 está truncado en el fuente mismo (corte de página/texto incompleto); no es posible verificar si la norma troncal que regula el acceso al mercado de cambios para repatriación de inversiones de no residentes fue representada, ya que su texto completo no figura en el fuente ni en lo extraído más allá de la excepción del punto propio
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.13.1.6 — bloque [intro | punto 3.13.1]; tanda 0: reintento=True, cola=None
- VIEJO B (otro, alta, bloq True): «3.13.1. El acceso al mercado de cambios para la repatriación de inversiones de no» — el encabezado 3.13.1 está truncado en el fuente pero enuncia la norma troncal (conformidad previa del BCRA) de la cual 3.13.1.6 es una excepción; ninguna entidad representa esa norma madre ni la excepción que el punto 3.13.1.6 constituye respecto de ella, más allá de que el extractor haya declarado que la relación no se puede emitir por no estar la norma exceptuada en el chunk — lo que falta no es
- NUEVO: completo_ok=True aceptable=True faltantes=0

## ext::3.13.1.10 — bloque [intro | punto 3.13.1]; tanda 0: reintento=False, cola=cola_humana_veredicto_inutilizable
- VIEJO B (otro, alta, bloq True): «El acceso al mercado de cambios para la repatriación de inversiones de no
residentes y otras compras de moneda extranjera por parte de clientes no residentes re» — el extractor declaró este tramo como meta_normativo, pero en realidad establece la regla general (conformidad previa del BCRA) y la excepción que habilita que el punto 3.13.1.10 liste operaciones exceptuadas de esa conformidad previa; es contenido normativo (modalidad y alcance) no meramente de sentido/vigencia, y no está representado en ninguna entidad ni relación
- NUEVO: completo_ok=False aceptable=True faltantes=2
  - [0] enumeracion_incompleta, media, bloq False, cita verificada True: «el acceso se concrete en forma simultánea con la liquidación de
fondos ingresados desde el exterior por endeudamientos financieros
comprendidos en el punto 3.5.» — la condición e2 omite que los endeudamientos financieros deben estar 'comprendidos en el punto 3.5', un calificador que precisa a cuáles endeudamientos se refiere (no cualquier endeudamiento, solo los del punto 3.5)
  - [1] calificador_despojado, media, bloq False, cita verificada True: «o fondos
provenientes de un préstamo
financiero en moneda extranjera otorgada por una entidad financiera
local a partir de una línea de crédito de entidad financiera del exterior» — la descripción de e2 habla genéricamente de 'préstamos financieros en moneda extranjera' pero omite que deben provenir de una entidad financiera LOCAL a partir de una línea de crédito de una entidad financiera DEL EXTERIOR, un calificador que precisa el origen y canal del financiamiento

## ext::3.16.2.1 — bloque [intro | punto 3.16.2]; tanda 0: reintento=True, cola=None
- VIEJO B (modalidad_perdida, alta, bloq True): «la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto al considerar que, parcial o totalmente» — este tramo fue declarado como omisión 'meta_normativo' por el extractor, pero en realidad establece una facultad (la entidad 'podrá aceptar') y la condición marco que habilita las siete excepciones (i a vii); no es meta-normativo (no habla del sentido u objetivo de la norma) sino que prescribe quién puede hacer qué y bajo qué marco. Al quedar fuera, las excepciones e1-e7 quedan huérfanas de la fac
- NUEVO: completo_ok=False aceptable=False faltantes=2
  - [0] CANDIDATO modalidad_perdida, alta, bloq True, cita verificada True: «la entidad también podrá aceptar una declaración jurada del cliente en la que deje constancia que no se excede tal monto» — el extractor declaró este tramo como meta_normativo (omisión no-prosa), pero en realidad es la norma que habilita la facultad de la entidad de aceptar una declaración jurada alternativa cuando el cliente supera el umbral de USD 100.000; esa facultad (modalidad 'podrá') no quedó representada en ninguna entidad extraída, y las excepciones e1-e7 quedaron sin el nodo que las conecta ni la facultad que las origina
  - [1] enumeracion_incompleta, media, bloq False, cita verificada True: «En esta última declaración jurada del cliente deberá constar expresamente
el valor de sus activos externos líquidos disponibles al inicio del día y los
montos que asigna a cada una de las situaciones » — la obligación o1 representa esta cláusula pero su calificador 'en esta última declaración jurada' (la del segundo párrafo, no la del primer párrafo) no queda claro en la descripción extraída, que no distingue a cuál de las dos declaraciones juradas se refiere

## ext::3.18.1.1 — bloque [intro | punto 3.18.1]; tanda 0: reintento=True, cola=cola_humana
- VIEJO B2 (otro, alta, bloq True): «3.18.1. Los clientes que cuenten con una "Certificación de aumento de las exportaciones de» — el intro heredado del 3.18.1 define el sujeto habilitado (clientes con 'Certificación de aumento de las exportaciones') al que se aplica la restricción del listado de excepciones/no-accesos del punto 3.18.1.1; sin esta cláusula no se sabe a quién alcanza la prohibición sobre pago de intereses
- NUEVO: completo_ok=False aceptable=False faltantes=2
  - [0] modalidad_perdida, alta, bloq True, cita verificada True: «podrá acceder al mercado de cambios por hasta el monto de la certificación para realizar» — el ítem debía componerse con la modalidad facultativa ('podrá acceder') y el cuantificador ('hasta el monto de la certificación') del encabezado; lo extraído solo modela la operación y una restricción, sin representar la facultad de acceso ni el límite cuantitativo del monto certificado que el encabezado fija para cada ítem
  - [1] calificador_despojado, alta, bloq True, cita verificada True: «Los clientes que cuenten con una “Certificación de aumento de las exportaciones de bienes en el año 2021” o “Certificación de aumento de las exportaciones de bienes en el año 2022” o “Certificación de» — el sujeto habilitado (clientes con alguna de las certificaciones de aumento de exportaciones) que el encabezado fija para la norma compuesta no está representado en ninguna entidad ni relación del ítem
