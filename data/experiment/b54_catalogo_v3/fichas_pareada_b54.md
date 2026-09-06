# Fichas de adjudicación — pareada U-B5.4 (solo juicio semántico)

Orden aleatorizado con semilla declarada `b54-pareada-v1` (9 fichas).
**REGISTRO DE TRANSCRIPCIÓN (06/09):** las marcas y notas de abajo son la
adjudicación de la autora, adoptada por ella sobre la lectura ficha por
ficha de la sesión de asistencia y transcripta verbatim al archivo por la
instancia del plan desde el mensaje de esa sesión (las casillas del
archivo estaban vacías al recibirlo — discrepancia reportada). La sesión
de asistencia verificó la transcripción contra su propio mensaje (06/09):
nueve marcas fieles al mensaje fuente, tally recomputado, y tres
compresiones inmateriales declaradas — f. 2 y f. 6 pierden cláusulas de
consejo a la autora ya consumidas por la marca elegida; en f. 9 se repone
abajo la oración omitida. La confirmación de la autora queda PENDIENTE
para la firma del laudo de cierre. Tally: 6 correcto-v3 (f. 1, 2, 3, 5,
6, 9) · 1 correcto-antes (f. 4) · 2 otro (f. 7, 8) — recomputado contra
las marcas de abajo.

La adjudicación es de la autora; la predicción sellada NO se fuerza sobre
estos casos. Cada ficha: qué decía el texto, qué emitió el prefijo congelado
(antes) y qué emitió el v3 (después), y la pregunta a adjudicar.

## Ficha 1 — `ayccef::4.1` (brazo D)

**Texto del punto (recortado):** 4.1. Exigencia de autorización previa. Para cambiar de clase, las entidades financieras deberán contar con la autorización previa del BCRA.

**Antes (validación):** ids=['Sujeto_bcra', 'Sujeto_entidad_financiera'] propuestos=[]
**Antes (crudo, informativo):** ids=['Sujeto_bcra', 'Sujeto_entidad_financiera'] propuestos=[]
**Después (crudo v3):** ids=['Sujeto_entidad_financiera'] propuestos=[]

**Detalle mecánico:** ejecuta=[]; ids=['Sujeto_entidad_financiera']

**Adjudicación de la autora:** [x] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [ ] otro: ______
**Nota de la autora:** El obligado es la entidad financiera que quiere cambiar de clase; el BCRA aparece como autoridad que otorga, no como destinatario de la norma. Sacarlo de los ids es la anti-atracción funcionando — es exactamente el caso que la lectura de ESQ señaló como riesgo («el regulador figurando como sujeto alcanzado»). ejecuta=[] es coherente: no hay operación con ejecutor acá.

## Ficha 2 — `cap::3.1.14::intro` (brazo F)

**Texto del punto (recortado):** A los fines de establecer el ponderador de riesgo a aplicar de acuerdo con el enfoque estandarizado –punto 3.1.11.–, una titulización se considerará simple, transparente y comparable (STC) si: -se trata de una titulización tradicional que no constituye un programa ABCP; - involucra una transferencia real de activos –en los términos del acápite v) del punto 3.1.14.1.–; y - cumple con la totalidad de los criterios previstos en el presente punto (en adelante, “criterios STC”). El originante/fiduciario deberá divulgar toda la información necesaria respecto de la transacción que permita a los inver

**Antes (validación):** ids=['Sujeto_rol_alcance_capmin', 'Sujeto_sefyc'] propuestos=['inversor', 'inversores y tenedores de posiciones de titulización', 'originante', 'originante/fiduciario']
**Antes (crudo, informativo):** ids=['Sujeto_rol_alcance_capmin', 'Sujeto_sefyc'] propuestos=['inversor', 'inversores y tenedores de posiciones de titulización', 'originante', 'originante/fiduciario']
**Después (crudo v3):** ids=['Sujeto_entidad_originante', 'Sujeto_fiduciario_de_fideicomiso_financiero', 'Sujeto_rol_alcance_capmin', 'Sujeto_sefyc'] propuestos=['inversor']

**Detalle mecánico:** MIGRÓ a Sujeto_entidad_originante (violación de la guarda)

**Adjudicación de la autora:** [x] correcto v3 (en lo semántico, que es lo que esta pareada juzga; la violación mecánica va aparte como hallazgo de proceso) · [ ] correcto antes · [ ] ambos defendibles · [ ] otro: ______
**Nota de la autora:** «El originante/fiduciario deberá divulgar» — los obligados son esos dos, y el v3 los resuelve a Sujeto_entidad_originante y Sujeto_fiduciario_de_fideicomiso_financiero, consolidando cuatro propuestos redundantes del antes y dejando «inversor» (que es beneficiario de la divulgación, no obligado) en el canal correcto. La violación de la guarda es un hecho mecánico real y ya está registrada en el detalle: va al laudo como hallazgo de proceso, separada de la marca semántica.

## Ficha 3 — `traval::S2::cierre` (brazo C)

**Texto del punto (recortado):** DEL CAPITAL SOCIAL Y/O VOTOS DE LA PRESTADORA DE SERVICIOS DE TRANSPORTE DE VALORES Infor- Capital suscripto: $ Cantidad de acciones: Votos: mación Persona jurídica: al / / Domicilio Domicilio Participación accio- real legal Fecha Fecha naria CUIT/ Nombres y (calle, Nº, (calle, Nº, de de CUIL/CDI apellidos Votos localidad, localidad, alta baja Capital % % Provincia) Provincia) Lugar y fecha: Representante legal/apoderado Firma y aclaración DE LA PRESTADORA DE SERVICIOS DE TRANSPORTE DE VALORES Sociedad: Informa- ción al / / Domicilio Domicilio real legal Fecha Fecha CUIT/CUIL/ Nombres y (calle

**Antes (validación):** ids=['Sujeto_sujeto_regulado'] propuestos=['PSTV (prestadoras de servicios de transporte de valores)', 'TV (transportadoras de valores)']
**Antes (crudo, informativo):** ids=['Sujeto_sujeto_regulado'] propuestos=['PSTV (prestadoras de servicios de transporte de valores)', 'TV (transportadoras de valores)']
**Después (crudo v3):** ids=['Sujeto_rol_alcance_traval'] propuestos=['PSTV']

**Detalle mecánico:** predicción sellada: FICHA en ambos sentidos — ids=['Sujeto_rol_alcance_traval'] props=['PSTV']

**Adjudicación de la autora:** [x] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [ ] otro: ______
**Nota de la autora:** El formulario versa sobre la PSTV; rol_alcance_traval captura el universo del TO y «PSTV» queda como propuesto específico. Corrige los dos defectos del antes: el id genérico Sujeto_sujeto_regulado (el del token duplicado que ESQ anotó dos veces) y el doble propuesto redundante. Coincide con la predicción sellada.

## Ficha 4 — `cryl::1.3` (brazo D)

**Texto del punto (recortado):** 1.3. Características de la operatoria. Los títulos escriturales colectivos representativos de los Instrumentos de Deuda Pública (IDP), cuya colocación primaria sea instruida por el Ministerio de Hacienda, quedarán depositados en custodia en el BCRA. Los certificados escriturales colectivos representativos de los Instrumentos de Regulación Mo- netaria (IRM), cuya colocación primaria sea instruida por la Subgerencia General de Operacio- nes del BCRA, quedaran depositados en custodia en dicha Institución. Los registros de fideicomisos financieros y la aceptación de depósitos en custodia de instru

**Antes (validación):** ids=['Sujeto_bcra'] propuestos=[]
**Antes (crudo, informativo):** ids=['Sujeto_bcra'] propuestos=[]
**Después (crudo v3):** ids=['Sujeto_bcra', 'Sujeto_rol_alcance_cryl'] propuestos=[]

**Detalle mecánico:** ejecuta=['Sujeto_bcra', 'Sujeto_rol_alcance_cryl']; ids=['Sujeto_bcra', 'Sujeto_rol_alcance_cryl']

**Adjudicación de la autora:** [ ] correcto v3 · [x] correcto antes · [ ] ambos defendibles · [ ] otro: ______
**Nota de la autora:** El actor de este punto es el BCRA como custodio; quienes instruyen son Hacienda y la Subgerencia. rol_alcance_cryl como ejecutor de la operatoria no tiene apoyo en este texto — los sujetos del alcance no hacen nada en 1.3 (las órdenes de titulares están en 1.2). Es el reverso de las fichas 1 y 8: el rol de alcance mostrando su propia atracción — se adjunta a la unidad por pertenecer al TO, no por el texto. Exactamente lo que el brazo anti-atracción debía cazar, pero en el sentido inverso al del BCRA.

## Ficha 5 — `traval::2.3` (brazo C)

**Texto del punto (recortado):** 2.3. Si ya ha cerrado su primer ejercicio económico, copia del último balance general anual con in- forme de auditor externo y certificación del correspondiente consejo profesional. Cuando se tra- te de una PSTV respecto de la cual no haya transcurrido un ejercicio económico completo, de- berá presentar al BCRA un estado de situación patrimonial o manifestación de bienes con certi- ficación de contador público independiente con firma legalizada por el correspondiente consejo profesional.

**Antes (validación):** ids=[] propuestos=['Prestadoras de servicios de transporte de valores', 'Transportadoras de valores']
**Antes (crudo, informativo):** ids=[] propuestos=['Prestadoras de servicios de transporte de valores', 'Transportadoras de valores']
**Después (crudo v3):** ids=['Sujeto_rol_alcance_traval'] propuestos=[]

**Detalle mecánico:** predicción sellada: FICHA en ambos sentidos — ids=['Sujeto_rol_alcance_traval'] props=[]

**Adjudicación de la autora:** [x] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [ ] otro: ______
**Nota de la autora:** El obligado a presentar el balance o el estado patrimonial es la transportadora solicitante — el universo exacto de rol_alcance_traval — y los dos propuestos del antes eran irresolubles por diseño. Coincide con la predicción sellada. Junto con la ficha 3, es el pago directo del catálogo v3 sobre el hallazgo más persistente de las lecturas ESQ: la resolución de PSTV, que en dos iteraciones cayó en ids de pagos (proveedor_de_servicios_de_pago, psi_billetera_digital), acá cae por primera vez en el sujeto correcto.

## Ficha 6 — `pro::1.1.1` (brazo A)

**Texto del punto (recortado):** 1.1.1. Usuario de servicios financieros. A los efectos de la presente reglamentación, este concepto comprende a las personas humanas y jurídicas que en beneficio propio o de su grupo familiar o social y en carácter de destinatarios finales hacen uso de los servicios ofrecidos por los sujetos obligados que se enuncian en el punto 1.1.2., como a quienes de cualquier otra manera están expues- tos a una relación de consumo con tales sujetos. A los fines de que los sujetos obligados hagan operativa la individualización de los usua- rios de servicios financieros, se considerará que revisten ese cará

**Antes (validación):** ids=['Sujeto_rol_sujeto_obligado_proteccion'] propuestos=[]
**Antes (crudo, informativo):** ids=['Sujeto_rol_sujeto_obligado_proteccion'] propuestos=[]
**Después (crudo v3):** ids=[] propuestos=[]

**Detalle mecánico:** rol propio Sujeto_rol_sujeto_obligado_proteccion AUSENTE

**Adjudicación de la autora:** [x] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [ ] otro: ______
**Nota de la autora:** La más ajustada de las nueve, y «ambos defendibles» es razonable. La unidad define un término, y la regla que sostuve en las dos lecturas ESQ es que las definiciones no tienen sujeto obligado: la ausencia es correcta, y el rol del antes es atracción sobre una unidad definicional (consultar deberes de los sujetos obligados recuperaría una definición). La defendibilidad del antes está en el segundo párrafo, que operacionaliza el criterio «a los fines de que los sujetos obligados hagan operativa la individualización».

## Ficha 7 — `cap::6.2.1.1` (brazo C)

**Texto del punto (recortado):** 6.2.1.1. Las exigencias de capital por riesgo específico en concepto de riesgo de emisor serán las siguientes: Exigencia de capital Emisor por riesgo específico BCRA, Gobierno Nacional, gobiernos Plazo residual 0,25% provinciales, municipales y de la CABA ≤ 6 meses en pesos, cuando su fuente de fondos sea en esa moneda. Plazo residual 1% > 6 meses y ≤ Banco de Pagos Internacionales, Fondo 24 meses Monetario Internacional, Banco Central Europeo y Comunidad Europea y Bancos multilaterales de desarrollo del punto Plazo residual 1,6% 2.12.3.1. > 24 meses BCRA y sector público no financiero. 8% Dem

**Antes (validación):** ids=['Sujeto_aseguradora', 'Sujeto_banco_multilateral_de_desarrollo', 'Sujeto_bcra', 'Sujeto_entidad_cambiaria', 'Sujeto_entidad_financiera', 'Sujeto_fiduciario_de_fideicomiso_financiero', 'Sujeto_sector_privado_no_financiero', 'Sujeto_sector_publico_no_financiero'] propuestos=['Agentes regulados por la CNV', 'Banco Central Europeo', 'Banco de Pagos Internacionales', 'Bancos centrales', 'Empresas y otras personas jurídicas del país y del exterior', 'Fondo Monetario Internacional', 'Otros soberanos']
**Antes (crudo, informativo):** ids=['Sujeto_aseguradora', 'Sujeto_banco_multilateral_de_desarrollo', 'Sujeto_bcra', 'Sujeto_entidad_cambiaria', 'Sujeto_entidad_financiera', 'Sujeto_fiduciario_de_fideicomiso_financiero', 'Sujeto_sector_privado_no_financiero', 'Sujeto_sector_publico_no_financiero'] propuestos=['Agentes regulados por la CNV', 'Banco Central Europeo', 'Banco de Pagos Internacionales', 'Bancos centrales', 'Empresas y otras personas jurídicas del país y del exterior', 'Fondo Monetario Internacional', 'Otros soberanos']
**Después (crudo v3):** ids=['Sujeto_aseguradora', 'Sujeto_banco_central_del_exterior', 'Sujeto_banco_multilateral_de_desarrollo', 'Sujeto_bcra', 'Sujeto_entidad_cambiaria', 'Sujeto_entidad_financiera', 'Sujeto_fiduciario_de_fideicomiso_financiero', 'Sujeto_fmi', 'Sujeto_rol_alcance_capmin', 'Sujeto_sector_privado_no_financiero', 'Sujeto_sector_publico_no_financiero'] propuestos=[]

**Detalle mecánico:** BIS no quedó en propuesto

**Adjudicación de la autora:** [ ] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [x] otro: ids correctos y mejores que antes; BIS (y otros soberanos) debían sobrevivir como propuestos y desaparecieron
**Nota de la autora:** Lo ganado es real: FMI resuelto a su instancia nueva, BCE y bancos centrales a banco_central_del_exterior, más el rol de alcance. Lo perdido también: el BIS está nombrado en la tabla, NO entró al catálogo por decisión del laudo de fase 1, y por eso debía quedar en propuesto — la válvula existe para eso — y el v3 lo deja sin representación alguna, junto con «otros soberanos».

## Ficha 8 — `ayccef::2.1` (brazo D)

**Texto del punto (recortado):** 2.1. Exigencia de autorización previa. Para operar como entidad financiera deberá contarse con la autorización previa del Banco Central de la República Argentina (BCRA). También quedan sujetas a esa exigencia las que tengan carácter de entidades públicas o mixtas de la Nación, de las provincias, de las municipalidades o de la Ciudad Autónoma de Buenos Aires, en cuyo caso las normas pertinentes se aplicarán en cuanto sean compatibles con su naturaleza.

**Antes (validación):** ids=['Sujeto_bcra', 'Sujeto_entidad_financiera'] propuestos=[]
**Antes (crudo, informativo):** ids=['Sujeto_bcra', 'Sujeto_entidad_financiera'] propuestos=[]
**Después (crudo v3):** ids=['Sujeto_entidad_financiera', 'Sujeto_sector_publico_no_financiero'] propuestos=[]

**Detalle mecánico:** ejecuta=[]; ids=['Sujeto_entidad_financiera', 'Sujeto_sector_publico_no_financiero']

**Adjudicación de la autora:** [ ] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [x] otro: BCRA fuera correcto; sector_publico_no_financiero contradice el término que resuelve
**Nota de la autora:** Sacar al BCRA es correcto (misma anti-atracción de la ficha 1). Pero Sujeto_sector_publico_no_financiero para «las que tengan carácter de entidades públicas o mixtas» es mis-resolución: esas son entidades que van a operar como entidades financieras de carácter público — lo contrario del sector público no financiero. La cobertura correcta era entidad_financiera solo (las públicas son subclase) o un propuesto.

## Ficha 9 — `traval::1.1::intro` (brazo C)

**Texto del punto (recortado):** Comprende a las personas jurídicas que desempeñen la actividad de transporte terrestre de va- lores –Transportadoras de Valores (TV)–. Se entienden comprendidas dentro de dicha defini- ción a las empresas Prestadoras de Servicios de Transporte de Valores (PSTV) y a las Trans- portadoras de Valores Propias de las entidades financieras (TVP). A esos efectos, se conside- rarán valores al dinero –billetes y monedas de curso legal, y billetes y monedas extranjeros– y al oro.

**Antes (validación):** ids=['Sujeto_persona_juridica'] propuestos=['Prestadoras de Servicios de Transporte de Valores (PSTV)', 'Transportadoras de Valores Propias de entidades financieras (TVP)']
**Antes (crudo, informativo):** ids=['Sujeto_persona_juridica'] propuestos=['Prestadoras de Servicios de Transporte de Valores (PSTV)', 'Transportadoras de Valores Propias de entidades financieras (TVP)']
**Después (crudo v3):** ids=[] propuestos=[]

**Detalle mecánico:** predicción sellada: FICHA en ambos sentidos — ids=[] props=[]

**Adjudicación de la autora:** [x] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [ ] otro: ______
**Nota de la autora:** Es la definición del alcance del TO: no impone nada a nadie, delimita el universo. Vacío es la lectura consistente con la regla de definiciones sin sujeto, y el universo que esta unidad define queda capturado donde corresponde — en el rol de alcance que las fichas 3 y 5 muestran operando sobre las unidades prescriptivas. El antes sumaba un id sobre-genérico y propuestos redundantes con el propio definiens. Coincide con la predicción sellada.

