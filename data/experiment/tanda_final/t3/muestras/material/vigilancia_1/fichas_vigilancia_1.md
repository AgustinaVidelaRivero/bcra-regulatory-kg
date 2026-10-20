# Material de T4 — vigilancia:1 (30 fichas; B6.1, tanda final, T3, punto 7.5)

Sorteo: `vigilancia_1.json` (1ec9d44f…, 2026-10-20T14:08:58-03:00); material armado a las 2026-10-20T14:09:15-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `Condicion_entidad_cambiaria_posee_sucursales__cuando_la_entidad_cambiaria_posea_sucursales_5763b9` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ii_31_12_19::3.5` (e0, bloque de lista True; págs. 7, 8):

```
[encabezado | punto S3]
3. GERENTES
[texto propio | punto 3.5]
3.5. Cargo: Se ingresará el código de la Tabla Nº 4 que corresponda, según se trate de
una entidad financiera o cambiaria, respectivamente.
Para las entidades financieras la información del “responsable del área de sucursales”
dependerá de la existencia de filiales en la entidad, en tal sentido se consignará el ge-
rente o responsable de todas las sucursales. Asimismo, los códigos correspondientes a
los cargos de “responsable de la gerencia general” y “responsable de la subgerencia
general” podrán no ser informados cuando la entidad financiera no contemple la cobertu-
ra de tales cargos.
Para las entidades cambiarias el “responsable de sucursal” deberá ser informado cuan-
do las mismas posean sucursales, en dicho caso, se informará el gerente general o car-
go equivalente de cada sucursal. Los “responsables de otras gerencias” se informarán
respecto de aquellas áreas gerenciales no contempladas en la referida Tabla Nº 4 y que
resulten de relevancia para la operatoria de la entidad.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_entidad_cambiaria_posee_sucursales__cuando_la_entidad_cambiaria_posea_sucursales_5763b9` — Entidad cambiaria posee sucursales
  - propiedades: {"descripcion": "Cuando la entidad cambiaria posea sucursales"}
  - tramo: cuando las mismas posean sucursales
- **Aristas** (3):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_para_las_entidades_cambiarias_se_informara_el_gerente_general_o_cargo_equivalent_85b64a` — Información responsable sucursal — entidades cambiarias
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ii_31_12_19_pdf` — Información Institucional de Entidades Financieras y Cambiarias · {"rol_fuente": "derivada_de_procedencia"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_proporcionar_respecto_de_las_areas_gerenciales_detalladas_en_la_tabla_no_4_geren_839304` — Informar datos de responsables de áreas gerenciales · {"alcance": "interna", "destino": "ri_ii_31_12_19::3.5", "evidencia": "Tabla Nº 4 –Gerentes-,\nlas informaciones que se indican en los puntos 3.1. a 3.10. y 3.12. correspondientes a"}

## 2. `Condicion_operaciones_inconsistentes_con_practicas_habituales__supuesto_que_activa_el_repo_896e05` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_laft::S3::cierre` (e0, bloque de lista True; págs. 10):

```
[encabezado | punto S3]
3. Reportes de operaciones sospechosas
[bloque cierre | punto S3]
Clientes no residentes en el país, con excepción de aquellos que tengan el carácter de turistas y realicen operaciones de compra y venta de divisa
02
extranjera para tales fines.
Cuando el cliente exhibe una inusual despreocupación respecto de los riesgos que asume y/o costos de las transacciones incompatible con el perfil
03
económico del mismo.
04 Cuando el cliente no da cumplimiento a la presente Resolución u otras normas de aplicación en la materia.
Cuando existiera el mismo domicilio en cabeza de distintas personas jurídicas o cuando las mismas personas físicas revistieren el carácter de autori-
05 zadas y/o apoderadas en diferentes personas de existencia ideal, y no existiere razón económica o legal para ello, teniendo especial consideración
cuando alguna de las compañías u organizaciones estén ubicadas en paraísos fiscales y su actividad principal sea la operatoria off shore.
Cuando existieren operaciones de distintas cuentas asociadas o vinculadas con un mismo dispositivo electrónico o cuando existiera una cuenta aso-
06
ciada a varios dispositivos electrónicos, sin justificación aparente.
Cuando existieran operaciones inconsistentes con las prácticas habituales, teniendo en especial consideración si su actividad principal está vinculada
07
con la operatoria “off shore” y/o con países determinados como de baja o nula tributación por las autoridades competentes.
08 Cuando existan discrepancias entre la información aportada por el cliente y la información detectada por los sistemas de monitoreo.
Cuando las operaciones involucren países o jurisdicciones considerados paraísos fiscales o identificados como no cooperativos por el Grupo de Ac-
09
ción Financiera Internacional.
10 Cuando los clientes intenten realizar operaciones con dinero falso.
11 Cuando los clientes se nieguen a proporcionar datos o documentos requeridos por los Sujetos Obligados
12 Cuando se detecte que la información y/o documentación suministrada por los clientes se encuentre alterada.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_operaciones_inconsistentes_con_practicas_habituales__supuesto_que_activa_el_repo_896e05` — Operaciones inconsistentes con prácticas habituales
  - propiedades: {"descripcion": "Supuesto que activa el reporte: operaciones inconsistentes con prácticas habituales, especialmente si la actividad principal está vinculada con operatoria off shore o países de baja/nula tributación."}
  - tramo: Cuando existieran operaciones inconsistentes con las prácticas habituales, teniendo en especial consideración si su actividad principal está vinculada con la operatoria "off shore" y/o con países determinados como de baja o nula tributación por las autoridades competentes.
- **Aristas** (1):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_laft_pdf` — Régimen Informativo LAFT

## 3. `Condicion_plazos_de_notificacion_y_aplicacion_de_tarifas__la_presentacion_de_altas_y_aumen_5b5f39` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_transpa::SA::intersticial` (e0, bloque de lista True; págs. 15):

```
[encabezado | punto Sbloque1]
RÉGIMEN INFORMATIVO CONTABLE MENSUAL
[encabezado | punto SA]
Apartado A: “Información sobre tarifario nomenclado”.
[bloque intersticial | punto SA]
A través de los siguientes Apartados, los sujetos obligados informarán acerca de las altas -
comisiones de nuevos productos y/o servicios que deseen comercializar- y los aumen-
tos/reducciones en las comisiones que deseen implementar respecto de los usuarios de servicios
financieros. También deberán informar las modificaciones de los cargos.
Los sujetos obligados deberán presentar las altas y aumentos referidos en el párrafo anterior,
considerando los plazos establecidos por el Texto Ordenado de “Protección de los usuarios de
servicios financieros” para la notificación a los usuarios y la aplicación de las nuevas tarifas.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_plazos_de_notificacion_y_aplicacion_de_tarifas__la_presentacion_de_altas_y_aumen_5b5f39` — Plazos de notificación y aplicación de tarifas
  - propiedades: {"descripcion": "La presentación de altas y aumentos debe considerar los plazos establecidos por el Texto Ordenado de Protección de los usuarios de servicios financieros para la notificación a los usuarios y la aplicación de las nuevas tarifas."}
  - tramo: considerando los plazos establecidos por el Texto Ordenado de "Protección de los usuarios de servicios financieros" para la notificación a los usuarios y la aplicación de las nuevas tarifas
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_los_sujetos_obligados_deben_presentar_las_altas_y_aumentos_de_comisiones_conside_c2e7fb` — Presentar altas y aumentos con plazos de notificación
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_transpa_pdf` — Régimen Informativo de Transparencia

## 4. `Condicion_remision_conforme_seccion_76_to_presentacion_informaciones__la_remision_debe_cum_48bafa` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_iesinap::S3` (e0, bloque de lista True; págs. 1):

```
[texto propio | punto S3]
3. Periodicidad y vencimiento.
El requerimiento tendrá frecuencia anual, y abarcará el período comprendido entre el 1/1 y el
31/12 de cada año.
El informe correspondiente al año en que se produce la autorización para funcionar como “Admi-
nistradores de esquemas de pago de transferencias electrónicas de fondos” se presentará si el
período sujeto a revisión es igual o mayor a 6 meses. Si el periodo fuera menor a 6 meses, el
primer informe a presentar será el correspondiente al 31/12 del año siguiente al de la correspon-
diente autorización.
El vencimiento para la presentación operará el día 20/2 (o día hábil siguiente si éste fuese inhá-
bil).
Para su remisión se tendrán en cuenta las especificaciones establecidas en la Sección 76. del
texto ordenado de “Presentación de informaciones al Banco Central”.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_remision_conforme_seccion_76_to_presentacion_informaciones__la_remision_debe_cum_48bafa` — Remisión conforme Sección 76 TO Presentación informaciones
  - propiedades: {"descripcion": "La remisión debe cumplir con las especificaciones establecidas en la Sección 76 del Texto Ordenado de Presentación de informaciones al Banco Central"}
  - tramo: Para su remisión se tendrán en cuenta las especificaciones establecidas en la Sección 76. del texto ordenado de "Presentación de informaciones al Banco Central".
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_presentacion_anual_de_informe__ri_iesinap_s3_f28efe` — Presentación anual de informe
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_iesinap_pdf` — Régimen Informativo IESINAP

## 5. `Condicion_consideracion_diferente_perimetro_consolidacion_regimenes__la_consistencia_respe_679f24` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_esd::Sbloque1::chapeau_seccion` (e0, bloque de lista True; págs. 1, 2):

```
[encabezado | punto Sbloque1]
NORMAS DE PROCEDIMIENTO
[bloque chapeau_seccion | punto Sbloque1]
A- Instrucciones para su integración
Las entidades financieras deberán presentar el estado de situación de deudores consolidado con
filiales y subsidiarias significativas en el país y en el exterior, en el caso que estas últimas sean
entidades financieras.
Los importes se registrarán en miles de pesos, sin decimales.
A los fines del redondeo de las magnitudes se incrementarán los valores en una unidad cuando el
primer dígito de las fracciones sea igual o mayor que 5, desechando las que resulten inferiores.
La metodología para la conversión a moneda nacional detallada en el “Manual de Cuentas” para el
rubro “Filiales en el exterior”, se aplicará también para las financiaciones otorgadas en el exterior
por filiales y/o subsidiarias que deban consolidarse.
Comprende a las financiaciones según los conceptos definidos en las normas sobre “Clasificación
de deudores”.
No se deberán incluir los códigos correspondientes a la Diferencia por adquisición de cartera.
Los totales de Asistencia Crediticia y Responsabilidades Eventuales deberán ser consistentes con
los respectivos saldos declarados en la columna “Balance Consolidado Total” del “Estado de con-
solidación de entidades locales con filiales y subsidiarias en el país y en el exterior”.
La calidad de las financiaciones estará determinada en función de las citadas normas.
Aquellos deudores que no sean objeto de clasificación, por estar sus financiaciones totalmente
cubiertas con garantías preferidas “A” se expondrán en Situación Normal.
B- Disposiciones transitorias
- De corresponder, se incluirán las operaciones con los entes a que refieren los incisos ii) y
iii) del primer párrafo del punto 6.2. de las normas sobre “Supervisión consolidada”.
- La consistencia respecto del Estado de consolidación a que alude el séptimo párrafo del
apartado A- precedente, tendrá en cuenta el diferente perímetro de consolidación de am-
bos regímenes.
8 – Estado de Situación de Deudores Consolidado con Filiales y Subsidiarias Significativas en el País y
en el Exterior (R.I. – E.S.D.C.)
CON SEGUIMIENTO CON PROBLEMAS CON ALTO RIESGO DE
IRRECU-
SITUACIÓN
ESPECIAL INSOLVENCIA
PERABLE
EN EN-
CONCEPTO NORMAL
NEGOC. TRAT.
NO VENCI-
EN OBS. O ESPE VENCIDA NO VENCIDA VENCIDA
DA
C/AC. DE CIAL
REFIN.
CARTERA COMERCIAL
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_consideracion_diferente_perimetro_consolidacion_regimenes__la_consistencia_respe_679f24` — Consideración diferente perímetro consolidación regímenes
  - propiedades: {"descripcion": "La consistencia respecto del Estado de consolidación tendrá en cuenta el diferente perímetro de consolidación de ambos regímenes."}
  - tramo: La consistencia respecto del Estado de consolidación a que alude el séptimo párrafo del apartado A- precedente, tendrá en cuenta el diferente perímetro de consolidación de ambos regímenes.
- **Aristas** (1):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_esd_pdf` — Subsidiarias significativas en el país y exterior

## 6. `Condicion_provision_inmediata_de_numero_de_reclamo__para_reclamos_iniciados_por_telefono_i_d86aa2` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_iesinap::A::S4` (e0, bloque de lista True; págs. 3, 4, 5):

```
[encabezado | punto A]
-ANEXO-
[encabezado | punto A::Sbloque1]
CUIT N° [completar]
[texto propio | punto A::S4]
4. Tarea profesional
Nuestra tarea profesional fue desarrollada de conformidad con las normas sobre informes especia-
les establecidas por la Resolución Técnica N° 37 de la Federación Argentina de Consejos Profesio-
nales de Ciencias Económicas (en adelante “RT 37”) y consistió en la aplicación de ciertos procedi-
mientos necesarios para verificar el cumplimiento por parte de la Sociedad de los requerimientos
del BCRA en relación con ciertas normas sobre “Sistema Nacional de Pagos – Transferencias –
normas complementarias”. La RT37 exige que cumplamos los requerimientos de ética, así como
que planifiquemos y ejecutemos nuestra tarea de tal forma que nos permita emitir el presente infor-
me especial.
En un encargo para emitir un informe especial, el contador aplica una serie de procedimientos para
verificar el cumplimiento por parte de la Entidad de determinados requerimientos del organismo de
control, y se limita a dar una manifestación de hallazgos sobre la base de los resultados obtenidos
de esos procedimientos. Este servicio mejora la confiabilidad de la información objeto del trabajo, al
estar acompañada por una manifestación profesional independiente. En consecuencia, nuestro tra-
bajo no constituye una auditoría, una revisión de estados contables ni otro encargo de aseguramien-
to.
[En caso de que este informe lo emita el auditor, se puede agregar el párrafo siguiente:
En nuestro carácter de auditores externos de la Sociedad, hemos auditado los estados financieros
de la misma al __ de _____ de 20__, preparados de acuerdo con el [indicar el marco de información
contable], respecto de los cuales hemos emitido con fecha __ de ______ de 20__ nuestro informe
del auditor independiente sin salvedades [o con salvedades, adaptar según sea el caso], al cual nos
remitimos. No hemos efectuado ninguna auditoría sobre ningún estado financiero de la Sociedad, a
ninguna fecha y por ningún período posterior al __ de ______ de 20__.]
Los procedimientos detallados a continuación, en lo que es materia de nuestra competencia y en
ciertos casos efectuados sobre bases selectivas, han sido aplicados sobre los registros y documen-
tación que nos fueron suministrados por la Sociedad. Adicionalmente, para la ejecución de dichos
procedimientos hemos tenido en cuenta nuestro entendimiento del entorno de control interno de la
Sociedad en lo vinculado con los aspectos revisados y otros aspectos.
A. Verificar la existencia de una base de reclamos y quejas y que las políticas y procedimientos
sobre el particular establecidas por la Sociedad prevean que dicha base sea administrada de
acuerdo con los siguientes atributos prescriptos en el punto .5.5.9. de las normas sobre “Sis-
tema Nacional de Pagos – Transferencias – normas complementarias”:
i. Que se hayan habilitado canales para que los participantes y comercios puedan efec-
tuar quejas o reclamos.
ii. Que la Sociedad efectivamente registre en una base de datos única y centralizada to-
das las presentaciones recibidas por quejas y reclamos.
iii. Que esa base de datos consigne, como mínimo, los siguientes datos: número de re-
clamo, fecha y canal, CUIT/CUIL del presentante, causal, otros participantes involu-
crados -tales como adquirentes y proveedores de cuentas- y el estado del trámite, el
cual deberá mantenerse actualizado (pendiente de respuesta, con respuesta provisoria
o definitiva al presentante, etc.) junto con la respuesta brindada.
iv. Que los números asignados a las presentaciones sean correlativos.
v. Que el proceso de generación de la base de datos incluya controles de seguridad que
establezcan que dicha información solo puede ser modificada para la incorporación de
nuevos reclamos o para el agregado de nueva información sobre el estado actualizado
de los trámites.
vi. Que el proceso de captura de reclamos y quejas establezca que para el caso de re-
clamos iniciados vía telefónica o a través de una página de Internet o aplicación móvil
habilitadas para ese fin, el número de reclamo sea provisto en el acto al presentante,
respetando la correlatividad indicada en el punto iv. precedente.
vii. Que para el caso en que la confirmación del número de reclamo no opere en forma au-
tomática, el procedimiento debe disponer la notificación del número o código que le
sea asignado dentro de los tres (3) días hábiles de iniciada la presentación ante el ad-
ministrador del esquema.
B. Verificar la elaboración y puesta a consideración del Directorio del reporte referido en los dos
últimos párrafos del punto 1.5.5.9. de las normas sobre “Sistema Nacional de Pagos – Trans-
ferencias – normas complementarias” con las características allí establecidas en relación con
su frecuencia y contenido.
C. Verificar que la Sociedad cuente con políticas y procedimientos que aseguren el cumplimiento
de los aspectos mencionados a continuación, según lo establecido por las normas sobre “Sis-
tema Nacional de Pagos – Transferencias – normas complementarias”:
a. Que no se cursen más rápidamente las operaciones de aceptadores vinculados.
b. El establecimiento de multas en virtud de lo dispuesto en el punto 1.5.5.1. de las normas so-
bre “Sistema Nacional de Pagos – Transferencias – normas complementarias”.
c. Que los precios aplicados por el administrador/procesador a los aceptadores sean aplicados
de igual manera y sin discriminación de acuerdo con lo establecido en el punto 1.5.5.3. de
las normas sobre “Sistema Nacional de Pagos – Transferencias – normas complementarias”,
sin discriminar a los aceptadores no vinculados respecto de los vinculados.
D. Obtener un listado de multas cobradas en virtud de lo dispuesto en el punto 1.5.5.1. de las nor-
mas sobre “Sistema Nacional de Pagos – Transferencias – normas complementarias”, con iden-
tificación de la causa, a fin de constatar para una muestra de ellas que su determinación no im-
plica discriminación y/o actitud arbitraria en perjuicio de ciertos adquirentes.
E. Verificar que el proceso formalizado por la Sociedad para la comunicación a los participantes
prevea que la información sea notificada en forma simultánea y por la misma vía, sin discrimi-
nación de ningún actor, de acuerdo con lo previsto en el punto 1.5.5.6. de las normas sobre
“Sistema Nacional de Pagos – Transferencias – normas complementarias”.
F. Verificar, a partir de la revisión de información contractual y/u otra documentación provista por
la Sociedad, que se hayan definido reglas comerciales, técnicas y/u operativas para esquema
de transferencias inmediatas, y que los convenios suscriptos con los participantes establezcan
la obligación de cumplir con esas reglas del esquema y fijen multas y sanciones en caso de in-
cumplimientos.
G. Verificar que los administradores cuenten con un control que permita asegurar que los precios
que los aceptadores participantes cobran a los comercios se ajusten a lo establecido en los
puntos 5.2.3.1. y 5.2.3.2. de las normas sobre “Sistema Nacional de Pagos – Transferencias –
normas complementarias”.
H. Verificar que cuando los administradores den curso a pagos con transferencia iniciados median-
te la lectura de códigos QR, estos pagos sean ordenados desde billeteras digitales inscriptas en
el “Registro de billeteras digitales interoperables”, conforme a lo reglamentado en el punto 5.3.
de las normas sobre “Sistema Nacional de Pagos – Servicios de pago".
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_provision_inmediata_de_numero_de_reclamo__para_reclamos_iniciados_por_telefono_i_d86aa2` — Provisión inmediata de número de reclamo
  - propiedades: {"descripcion": "Para reclamos iniciados por teléfono, Internet o aplicación móvil, el número de reclamo debe ser provisto inmediatamente al presentante respetando correlatividad"}
  - tramo: Que el proceso de captura de reclamos y quejas establezca que para el caso de reclamos iniciados vía telefónica o a través de una página de Internet o aplicación móvil habilitadas para ese fin, el número de reclamo sea provisto en el acto al presentante, respetando la correlatividad
- **Aristas** (2):
  - (extraccion) —condicion_de→ Operacion `Operacion_verificacion_existencia_base_de_reclamos_y_quejas__ri_iesinap_a_s4_4a2357` — Verificación existencia base de reclamos y quejas
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_iesinap_pdf` — Régimen Informativo IESINAP

## 7. `Condicion_alcance_punto_6_3_capitales_minimos__instrumentos_alcanzados_por_el_punto_6_3_de_2109f0` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_tvf::S14` (e0, bloque de lista True; págs. 5):

```
[encabezado | punto Sbloque4]
Tasa Fija: fecha de vencimiento
[encabezado | punto Sbloque5]
Tasa Variable: fecha del próximo ajuste de interés
[texto propio | punto S14]
14. Mercado: para aquellos instrumentos que se encuentran alcanzados por el punto 6.3. de
las normas sobre “Capitales mínimos de las entidades financieras”, se deberá informar
código SWIFT del país correspondiente al mercado en que operó el instrumento.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_alcance_punto_6_3_capitales_minimos__instrumentos_alcanzados_por_el_punto_6_3_de_2109f0` — Alcance punto 6.3. Capitales mínimos
  - propiedades: {"descripcion": "Instrumentos alcanzados por el punto 6.3. de las normas sobre Capitales mínimos de las entidades financieras"}
  - tramo: para aquellos instrumentos que se encuentran alcanzados por el punto 6.3. de las normas sobre "Capitales mínimos de las entidades financieras"
- **Aristas** (2):
  - (extraccion) —condicion_de→ Operacion `Operacion_informacion_de_codigo_swift_del_mercado__ri_tvf_s14_4a51f3` — Información de código SWIFT del mercado
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_tvf_pdf` — Régimen Informativo Títulos Valores

## 8. `Condicion_condicion_operacion_en_bcbain_dol_domay_o_byma__cuando_el_ambito_de_negociacion__a87d97` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ot::Sbloque2::chapeau_seccion` (e0, bloque de lista True; págs. 2, 3):

```
[encabezado | punto Sbloque2]
Instrucciones Particulares
[bloque chapeau_seccion | punto Sbloque2]
Deberán informarse las compras y ventas a término y opciones de moneda extranjera identificando
la fecha de concertación de cada operación, el ámbito de negociación o contraparte y el vencimiento
de la operación.
Los movimientos deberán informarse totalizando las operaciones de cada día de la semana estadís-
tica que tengan en común los atributos solicitados.
Como cantidad de activo subyacente deberá informarse el importe en la moneda correspondiente a
ese activo.
Se informarán como Bajas las operaciones rescindidas o ejercidas con anterioridad a la fecha de
vencimiento. Para las operaciones sin vencimiento, siempre se informará su Baja cuando se cance-
len.
Las operaciones de swaps de moneda se informarán desagregando la transacción en tantas opera-
ciones a término como pagos se hayan pactado.
En los casos en que el ámbito de negociación en el que se concerte la operación sea la BCBAIN-
DOL, el DOMAY y BYMA, no deberán consignarse los campos identificación fiscal y denominación
de la contraparte.
Cuando se trate de operaciones realizadas en “A3 Mercados” y pueda identificarse la contra-
parte de la operación, se deberán consignar los datos “Número de identificación de la con-
traparte” y “Denominación de la contraparte”.
Datos Solicitados
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condicion_operacion_en_bcbain_dol_domay_o_byma__cuando_el_ambito_de_negociacion__a87d97` — Condición: operación en BCBAIN-DOL, DOMAY o BYMA
  - propiedades: {"descripcion": "Cuando el ámbito de negociación sea BCBAIN-DOL, DOMAY o BYMA."}
  - tramo: En los casos en que el ámbito de negociación en el que se concerte la operación sea la BCBAIN-DOL, el DOMAY y BYMA
- **Aristas** (2):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_prohibicion_de_consignar_los_campos_identificacion_fiscal_y_denominacion_de_la_c_de47dd` — No consignar identificación fiscal y denominación en BCBAIN-DOL, DOMAY y BYMA
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ot_pdf` — Régimen Informativo — Normas de Procedimiento

## 9. `Condicion_domicilio_sin_numero__cuando_el_domicilio_de_la_unidad_de_servicio_no_posea_nume_27df05` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_sef::P1::11.2` (e0, bloque de lista True; págs. 2):

```
[encabezado | punto P1]
I. Información solicitada
[encabezado | punto P1::S11]
11. Domicilio y teléfono:
[texto propio | punto P1::11.2]
11.2. Número: en el caso que el domicilio no posea número debe informarse entre que calles
(“Calle 1” y “Calle 2”) o “Esquina” se encuentra la unidad de servicio.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_domicilio_sin_numero__cuando_el_domicilio_de_la_unidad_de_servicio_no_posea_nume_27df05` — Domicilio sin número
  - propiedades: {"descripcion": "Cuando el domicilio de la unidad de servicio no posea número."}
  - tramo: en el caso que el domicilio no posea número
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_cuando_el_domicilio_no_posea_numero_debe_informarse_entre_que_calles_o_en_que_es_3e665d` — Informar número de domicilio o calles
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_sef_pdf` — Régimen Informativo Expansión Entidades Financieras

## 10. `Condicion_correspondencia_punto_b_2_3_ventas_a_termino_pesos__el_punto_b_2_3_debe_correspo_e87f2f` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ot::13.4` (e0, bloque de lista True; págs. 4, 5, 6):

```
[encabezado | punto Sbloque2]
Instrucciones Particulares
[encabezado | punto S13]
13. Concepto
[texto propio | punto 13.4]
13.4. Baja de Ventas
Criterios de consistencia
La presentación se considerará validada cuando todas las categorías establecidas en los Apartados
B.2. y B.3. del Régimen informativo Contable Mensual de Operaciones de Cambios se correspon-
dan con los totales que a continuación se detallan:
 Concertaciones de compras a término en moneda extranjera:
- el punto B.2.1. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Compras” menos las operaciones de
“Baja de Compras”, que afecten únicamente a las operaciones a término de moneda
extranjera liquidables en pesos concertadas en cada fecha.
- el punto B.3.1. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Compras” menos las operaciones de
“Baja de Compras”, que afecten únicamente a las operaciones a término de moneda
extranjera realizadas y liquidables en el exterior concertadas en cada fecha.
 Vencimientos de compras a término de moneda extranjera:
- el punto B.2.2. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de compras concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera liquidables en pesos.
- el punto B.3.2. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de compras concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera realizadas y liquidables en el exterior.
 Concertaciones de ventas a término en moneda extranjera:
- el punto B.2.3. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Ventas” menos las operaciones de
“Baja de Ventas”, que afecten únicamente a las operaciones a término de moneda
extranjera liquidables en pesos concertadas en cada fecha.
- el punto B.3.3. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente de las operaciones de “Alta de Ventas” menos las operaciones de
“Baja de Ventas”, que afecten únicamente a las operaciones a término de moneda
extranjera realizadas y liquidables en el exterior concertadas en cada fecha.
 Vencimientos de ventas a término de moneda extranjera:
- el punto B.2.4. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de ventas concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera liquidables en pesos.
- el punto B.3.4. debe corresponderse con el total equivalente en dólares estadounidenses
del activo subyacente del conjunto de las operaciones de ventas concertadas, cuyo
vencimiento coincida con el de la fecha respectiva, que afecten únicamente a las
operaciones a término de moneda extranjera realizadas y liquidables en el exterior.
Se aclara que a los fines de los cruces indicados, se tendrán en cuenta, de corresponder, los tipos
de pase a ser aplicados para la conversión de otras monedas extranjeras a dólares
estadounidenses informados diariamente por el Banco Central.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_correspondencia_punto_b_2_3_ventas_a_termino_pesos__el_punto_b_2_3_debe_correspo_e87f2f` — Correspondencia punto B.2.3. — ventas a término pesos
  - propiedades: {"descripcion": "El punto B.2.3. debe corresponder al total equivalente en dólares estadounidenses del activo subyacente de operaciones de Alta de Ventas menos Baja de Ventas, afectando únicamente operaciones a término de moneda extranjera liquidables en pesos concertadas en cada fecha."}
  - tramo: el punto B.2.3. debe corresponderse con el total equivalente en dólares estadounidenses del activo subyacente de las operaciones de "Alta de Ventas" menos las operaciones de "Baja de Ventas", que afecten únicamente a las operaciones a término de moneda extranjera liquidables en pesos concertadas en cada fecha
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_la_presentacion_se_considerara_validada_cuando_todas_las_categorias_establecidas_003793` — Validación presentación — consistencia categorías
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ot_pdf` — Régimen Informativo — Normas de Procedimiento

## 11. `Condicion_informacion_consolidada_nivel_2_con_operaciones_holding_no_financiera__la_inform_3499e7` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_tsa::5.1` (e0, bloque de lista True; págs. 75):

```
[encabezado | punto S5]
Sección 5. Disposiciones transitorias
[texto propio | punto 5.1]
5.1. Suspensión de la observancia de las regulaciones técnicas sobre base consolidada trimestral
(punto 6.1. de las normas sobre “Supervisión consolidada”, vigencia a partir de abril/24).
La información consolidada (nivel 2) incluirá, de corresponder, las operaciones de la compañía
holding no financiera de la entidad, conforme a lo previsto en el primer párrafo, inciso i) y se-
gundo párrafo “in fine” del punto 6.2. de las normas sobre “Supervisión consolidada”.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_informacion_consolidada_nivel_2_con_operaciones_holding_no_financiera__la_inform_3499e7` — Información consolidada nivel 2 con operaciones holding no financiera
  - propiedades: {"descripcion": "La información consolidada (nivel 2) debe incluir, de corresponder, las operaciones de la compañía holding no financiera de la entidad, conforme a lo previsto en el punto 6.2. de las normas sobre Supervisión consolidada"}
  - tramo: La información consolidada (nivel 2) incluirá, de corresponder, las operaciones de la compañía holding no financiera de la entidad, conforme a lo previsto en el primer párrafo, inciso i) y segundo párrafo "in fine" del punto 6.2. de las normas sobre "Supervisión consolidada"
- **Aristas** (9):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_tsa_pdf` — Ratio de Cobertura de Liquidez
  - (remision_derivada) —remite_a→ Condicion `Condicion_supuesto_entes_en_acapites_ii_y_iii__cuando_se_trate_de_entes_contemplados_en_lo_0647e5` — Supuesto: entes en acápites ii) y iii) · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}
  - (remision_derivada) —remite_a→ Excepcion `Excepcion_se_exceptua_la_aplicacion_de_los_puntos_5_2_1_6_limite_maximo_de_financiaciones__139be7` — Excepción relaciones técnicas para entes ii) y iii) · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_las_entidades_financieras_deberan_presentar_en_las_informaciones_mensuales_que_r_bc1d29` — Presentar informaciones mensuales consolidadas · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_las_relaciones_tecnicas_cuya_base_de_observancia_sea_unicamente_consolidada_trim_d2868b` — Observancia relaciones técnicas base consolidada mensual · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_compania_holding_no_entidad_financiera__supcon_6_2_ab485b` — Compañía holding no entidad financiera · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_inclusion_o_exclusion_de_entes_en_consolidacion__supcon_6_2_74dee9` — Inclusión o exclusión de entes en consolidación · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_participacion_en_entidades_financieras_del_exterior__supcon_6_2_da2af6` — Participación en entidades financieras del exterior · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_presentacion_informaciones_mensuales_consolidadas__supcon_6_2_f5f159` — Presentación informaciones mensuales consolidadas · {"alcance": "externa", "destino": "supcon::6.2", "evidencia": "punto 6.2. de las normas sobre “Supervisión consolidada"}

## 12. `Condicion_control_de_razonabilidad_de_saldos__verificacion_de_que_el_saldo_total_de_fondos_276da5` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_psp::SIII::chapeau_seccion` (e0, bloque de lista True; págs. 5, 6, 7, 8, 9, 10, 11):

```
[encabezado | punto SIII]
Sección III. APARTADO B: INFORMACIÓN ESTADÍSTICA – SISTEMA NACIONAL DE PAGOS
[bloque chapeau_seccion | punto SIII]
III.1. Instrucciones particulares
Se deberán integrar los siguientes datos agrupados en forma mensual de acuerdo con los atributos
detallados en los puntos a, b y d del presente apartado y según el “Modelo de información” del
punto III.2.:
1. Cantidad de operaciones
2. Monto total
Asimismo, se deberán integrar las cantidades respecto de los datos adicionales detallados en el
punto c.
a. Para todas las transacciones realizadas
Se clasificarán en función de si corresponden a créditos y/o débitos realizados por el
PSPCP, el tipo de cuenta a acreditar, el tipo de titular (cuando se refieran a “Cuenta de
pago propia”) y el método de iniciación, según el detalle de partidas incluido en el “Modelo
de información” del punto III.2.
A su vez, cada una esas partidas se agruparán de acuerdo con el medio de pago y el
esquema de pago correspondientes a las Tablas 1 y 2, respectivamente, detalladas en el
punto III.3.
Se deberán informar las transacciones en el momento en que fueron liquidadas
independientemente de su fecha de concertación.
Los créditos y/o débitos se informarán cuando haya afectación de una cuenta de pago
de los clientes del PSPCP. Esto incluye los movimientos de los fondos que se
invierten y se rescatan, así como los intereses obtenidos.
Los créditos se deberán informar netos de comisiones e impuestos. Solo deben
informarse los montos efectivamente ingresados en las cuentas de pago de los
clientes.
En el caso de los débitos, se deberán informar los montos efectivamente egresados
de las cuentas de pago de los clientes.
b. Para las transferencias
Se clasificarán en función del detalle de partidas incluido en el “Modelo de información” del
punto III.2. según correspondan a:
b.1. De CVU a CBU
b.2. De CBU a CVU
b.3. De CVU a CVU enviadas
b.4. De CVU a CVU recibidas
La información incluida en el presente punto (partidas 500X000 de Transferencias)
también deberá ser reportada en forma desagregada dentro de las partidas 10XXXXX
(créditos) y 20XXXXX (débitos), según corresponda, y de acuerdo con las tablas 1
“Medios de pago” (transferencias inmediatas “push” o “pull”) y 2 “Esquemas de
pago” (transferencias bancarias desde/hacia CBU o CVU).
Debe ser completado con las transferencias que se realicen a través de la CVU y no
son administradas por el PSPCP. Es decir, quedan excluidas del presente punto todas
aquellas otras transferencias realizadas mediante algún esquema propio del PSPCP
que no hubieran sido cursadas a través de una CVU, por ejemplo: número de teléfono,
correo electrónico, etc. Las transferencias efectuadas mediante esquemas de pago
propio deben ser incluidas en las partidas 10XXXXX (créditos) y 20XXXXX (débitos),
según corresponda, como transferencias “push” / “pull”.
c. Información adicional sobre clientes y cuentas (por tipo de titular)
c.1. Cantidad total de clientes involucrados en los puntos a y b del presente Apartado,
desagregados por uso comercial o personal/no comercial.
c.2. Cantidad total de cuentas de pago involucradas en los puntos a y b del presente
Apartado, desagregadas por uso comercial o personal/no comercial.
c.3. Cantidad total de clientes, desagregados por uso comercial o personal/no comercial.
c.4. Cantidad total de cuentas de pago, desagregadas por uso comercial o personal/no
comercial.
d. Préstamos
En los casos de aquellos PSPCP que a su vez se encuentren habilitados
normativamente para el otorgamiento de financiaciones en su carácter de
proveedores no financieros de crédito, deberán informar los datos de los préstamos
otorgados y cancelados que se hubieran acreditado o debitado -respectivamente- en
las cuentas de pago de sus clientes durante el mes bajo informe.
La información incluida en el presente punto (partidas 70XX000 de Préstamos)
también deberá ser reportada de forma desagregada dentro de las partidas 10XXXXX
(créditos) y 20XXXXX (débitos) según corresponda y de acuerdo con las tablas 1
(Medios de pago) y 2 (Esquemas de pago).
e. Control de razonabilidad respecto de los saldos informados en el Apartado A
El saldo total de los fondos acreditados en las cuentas de pago de los clientes
correspondiente al último día del mes bajo informe reportado en el Apartado A, debe
ser igual al que se haya remitido para el último día del mes anterior al bajo informe en
dicho Apartado A más la suma de los créditos y menos la suma de los débitos del
Apartado B correspondientes al mes bajo informe.
III.2. Modelo de información
[TABLA ri_psp::tabla001 | página 7 | e0_tablas | posicional]
Fila 1: col1 = Código Partida | col2 = Concepto | col4 = Medios | col7 = Esquema | col10 = Cantidad | col12 = Monto total ⟨abarca hasta col14⟩
Fila 2: col4 = de Pago | col7 = de pago | col10 = de
Fila 3: col4 = Tabla 1 | col7 = Tabla 2 | col10 = operac.
Fila 4: col2 = CREDITOS EN
Fila 5: col2 = Cuenta de pago propia – Comercial
Fila 6: col1 = 10101XX | col2 = ApMovil-Cercanía Sin Contacto
Fila 7: col1 = 10102XX | col2 = ApMovil-QR
Fila 8: col1 = 10103XX | col2 = ApMovil-Botón de pago
Fila 9: col1 = 10104XX | col2 = ApWeb-Botón de pago
Fila 10: col1 = 10105XX | col2 = TPV/TPVMovil-Banda magnética
Fila 11: col1 = 10106XX | col2 = TPV/TPVMovil-Cercanía Sin Contacto
Fila 12: col1 = 10107XX | col2 = TPV/TPVMovil-Chip
Fila 13: col1 = 10108XX | col2 = Sucursal/Agente/Comercio
Fila 14: col1 = 10109XX | col2 = Cajero automático
Fila 15: col1 = 10199XX | col2 = No disponible/No conocida
Fila 16: col2 = Cuenta de pago propia – Personal/No co- mercial
Fila 17: col1 = 10201XX | col2 = ApMovil-Cercanía Sin Contacto
Fila 18: col1 = 10202XX | col2 = ApMovil-QR
Fila 19: col1 = 10203XX | col2 = ApMovil-Botón de pago
Fila 20: col1 = 10204XX | col2 = ApWeb-Botón de pago
Fila 21: col1 = 10205XX | col2 = TPV/TPVMovil-Banda magnética
Fila 22: col1 = 10206XX | col2 = TPV/TPVMovil-Cercanía Sin Contacto
Fila 23: col1 = 10207XX | col2 = TPV/TPVMovil-Chip
Fila 24: col1 = 10208XX | col2 = Sucursal/Agente/Comercio
Fila 25: col1 = 10209XX | col2 = Cajero automático
Fila 26: col1 = 10299XX | col2 = No disponible/No conocida
[FIN TABLA ri_psp::tabla001]
XX: 10 = personas humanas; 20 = personas jurídicas.
III.2. Modelo de información (continuación)
[TABLA ri_psp::tabla002 | página 8 | e0_tablas | posicional]
Fila 1: col1 = Código Partida | col2 = Concepto | col4 = Medios | col7 = Esquema | col10 = Cantidad | col12 = Monto total ⟨abarca hasta col14⟩
Fila 2: col4 = de Pago | col7 = de pago | col10 = de
Fila 3: col4 = Tabla 1 | col7 = Tabla 2 | col10 = operac.
Fila 4: col2 = DEBITOS A
Fila 5: col2 = Cuenta de pago propia – Comercial
Fila 6: col1 = 20101XX | col2 = ApMovil-Cercanía Sin Contacto
Fila 7: col1 = 20102XX | col2 = ApMovil-QR
Fila 8: col1 = 20103XX | col2 = ApMovil-Botón de pago
Fila 9: col1 = 20104XX | col2 = ApWeb-Botón de pago
Fila 10: col1 = 20105XX | col2 = TPV/TPVMovil-Banda magnética
Fila 11: col1 = 20106XX | col2 = TPV/TPVMovil–Cercanía Sin Contacto
Fila 12: col1 = 20107XX | col2 = TPV/TPVMovil–Chip
Fila 13: col2 = Cuenta de pago propia – Personal/No co- mercial
Fila 14: col1 = 20201XX | col2 = ApMovil-Cercanía Sin Contacto
Fila 15: col1 = 20202XX | col2 = ApMovil-QR
Fila 16: col1 = 20203XX | col2 = ApMovil-Botón de pago
Fila 17: col1 = 20204XX | col2 = ApWeb-Botón de pago
Fila 18: col1 = 20205XX | col2 = TPV/TPVMovil-Banda magnética
Fila 19: col1 = 20206XX | col2 = TPV/TPVMovil-Cercanía Sin Contacto
Fila 20: col1 = 20207XX | col2 = TPV/TPVMovil-Chip
Fila 21: col2 = Cuenta de otro PSPCP
Fila 22: col1 = 2030100 | col2 = ApMovil-Cercanía Sin Contacto
Fila 23: col1 = 2030200 | col2 = ApMovil-QR
Fila 24: col1 = 2030300 | col2 = ApMovil-Botón de pago
Fila 25: col1 = 2030400 | col2 = ApWeb-Botón de pago
Fila 26: col1 = 2030500 | col2 = TPV/TPVMovil-Banda magnética
Fila 27: col1 = 2030600 | col2 = TPV/TPVMovil-Cercanía Sin Contacto
Fila 28: col1 = 2030700 | col2 = TPV/TPVMovil-Chip
Fila 29: col2 = Cuenta de EF
Fila 30: col1 = 2040100 | col2 = ApMovil-Cercanía Sin Contacto
Fila 31: col1 = 2040200 | col2 = ApMovil-QR
Fila 32: col1 = 2040300 | col2 = ApMovil-Botón de pago
Fila 33: col1 = 2040400 | col2 = ApWeb-Botón de pago
Fila 34: col1 = 2040500 | col2 = TPV/TPVMovil-Banda magnética
Fila 35: col1 = 2040600 | col2 = TPV/TPVMovil-Cercanía Sin Contacto
Fila 36: col1 = 2040700 | col2 = TPV/TPVMovil-Chip
Fila 37: col2 = Otros
Fila 38: col1 = 2050100 | col2 = Sucursal/Agente/Comercio
Fila 39: col1 = 2050200 | col2 = Cajero automático
[FIN TABLA ri_psp::tabla002]
XX: 10 = personas humanas; 20 = personas jurídicas.
III.2. Modelo de información (continuación)
[TABLA ri_psp::tabla003 | página 9 | e0_tablas | posicional]
Fila 1: col1 = Código Partida | col2 = Concepto | col4 = Medios de | col7 = Esquema | col9 = Cantidad de operaciones ⟨abarca hasta col11⟩ | col12 = Monto total ⟨abarca hasta col14⟩
Fila 2: col4 = Pago | col7 = de pago
Fila 3: col4 = Tabla 1 | col7 = Tabla 2
Fila 4: col2 = TRANSFERENCIAS
Fila 5: col1 = 5001000 | col2 = De CVU a CBU
Fila 6: col1 = 5002000 | col2 = De CBU a CVU
Fila 7: col1 = 5003000 | col2 = De CVU a CVU acreditadas
Fila 8: col1 = 5004000 | col2 = De CVU a CVU debitadas
[FIN TABLA ri_psp::tabla003]
[TABLA ri_psp::tabla004 | página 9 | e0_tablas | posicional]
Fila 1: col1 = Código Partida | col2 = Concepto | col4 = Medios de | col7 = Esquema | col9 = Cantidad ⟨abarca hasta col11⟩ | col12 = Monto total ⟨abarca hasta col14⟩
Fila 2: col4 = Pago | col7 = de pago
Fila 3: col4 = Tabla 1 | col7 = Tabla 2
Fila 4: col2 = CLIENTES Y CUENTAS
Fila 5: col2 = Total de clientes involucrados en transacciones
Fila 6: col1 = 60110XX | col2 = Comercial
Fila 7: col1 = 60120XX | col2 = Personal/No comercial
Fila 8: col2 = Total de clientes involucrados en transferencias
Fila 9: col1 = 60130XX | col2 = Comercial
Fila 10: col1 = 60140XX | col2 = Personal/No comercial
Fila 11: col2 = Total de cuentas de pago involucra- das en transacciones
Fila 12: col1 = 60210XX | col2 = Comercial
Fila 13: col1 = 60220XX | col2 = Personal/No comercial
Fila 14: col2 = Total de cuentas de pago involucra- das en transferencias
Fila 15: col1 = 60230XX | col2 = Comercial
Fila 16: col1 = 60240XX | col2 = Personal/No comercial
Fila 17: col2 = Total de clientes
Fila 18: col1 = 60310XX | col2 = Comercial
Fila 19: col1 = 60320XX | col2 = Personal/No comercial
Fila 20: col2 = Total de cuentas de pago
Fila 21: col1 = 60410XX | col2 = Comercial
Fila 22: col1 = 60420XX | col2 = Personal/No comercial
[FIN TABLA ri_psp::tabla004]
XX: 10 = personas humanas; 20 = personas jurídicas.
[TABLA ri_psp::tabla005 | página 9 | e0_tablas | posicional]
Fila 1: col1 = Código Partida ⟨abarca hasta col3⟩ | col4 = Concepto ⟨abarca hasta col6⟩ | col8 = Medios de | col11 = Esquema | col13 = Cantidad de operaciones ⟨abarca hasta col15⟩ | col16 = Monto total ⟨abarca hasta col18⟩
Fila 2: col8 = Pago | col11 = de pago
Fila 3: col8 = Tabla 1 | col11 = Tabla 2
Fila 4: col5 = PRÉSTAMOS
Fila 5: col1 = 7011000 ⟨abarca hasta col3⟩ | col4 = Otorgados a clientes ⟨abarca hasta col6⟩
Fila 6: col1 = 7012000 ⟨abarca hasta col3⟩ | col4 = Cancelados por parte de clientes ⟨abarca hasta col6⟩
[FIN TABLA ri_psp::tabla005]
III.3. Tablas complementarias
TABLA 1: Medios de pago
[TABLA ri_psp::tabla006 | página 10 | e0_tablas | columnas]
Columnas: col1 | Código | col3 | col4 | Descripción | col6
Fila 1: col1 = 1 ⟨abarca hasta col3⟩ | col4 = Tarjeta de crédito ⟨abarca hasta col6⟩
Fila 2: col1 = 2 ⟨abarca hasta col3⟩ | col4 = Tarjeta de débito ⟨abarca hasta col6⟩
Fila 3: col1 = 3 ⟨abarca hasta col3⟩ | col4 = Tarjeta prepaga ⟨abarca hasta col6⟩
Fila 4: col1 = 5 ⟨abarca hasta col3⟩ | col4 = Efectivo ⟨abarca hasta col6⟩
Fila 5: col1 = 6 ⟨abarca hasta col3⟩ | col4 = Transferencias inmediatas “push” ⟨abarca hasta col6⟩
Fila 6: col1 = 7 ⟨abarca hasta col3⟩ | col4 = Transferencias inmediatas “pull” ⟨abarca hasta col6⟩
Fila 7: col1 = 8 ⟨abarca hasta col3⟩ | col4 = Pagos con transferencia (PCT) ⟨abarca hasta col6⟩
Fila 8: col1 = 9 ⟨abarca hasta col3⟩ | col4 = Débito inmediato – Spot ⟨abarca hasta col6⟩
Fila 9: col1 = 10 ⟨abarca hasta col3⟩ | col4 = Débito inmediato – Recurrente ⟨abarca hasta col6⟩
[FIN TABLA ri_psp::tabla006]
TABLA 2: Esquemas de pago
De haberse consignado como medio de pago: tarjeta de crédito / tarjeta de débito / tarjeta prepaga,
se deberá integrar el código de marca asignado en la tabla denominada “Tabla marcas de tarjetas”
disponible en el sitio exclusivo de Internet del BCRA (https://www3.bcra.gob.ar). En los demás ca-
sos, se completará según se trate de:
[TABLA ri_psp::tabla007 | página 10 | e0_tablas | columnas]
Columnas: col1 | Código | col3 | col4 | Descripción | col6
Fila 1: col1 = 00007 ⟨abarca hasta col3⟩ | col4 = Transferencias bancarias desde/hacia CBU ⟨abarca hasta col6⟩
Fila 2: col1 = 00008 ⟨abarca hasta col3⟩ | col4 = Transferencias bancarias desde/hacia CVU ⟨abarca hasta col6⟩
Fila 3: col1 = 00009 ⟨abarca hasta col3⟩ | col4 = Esquema de pago propio ⟨abarca hasta col6⟩
[FIN TABLA ri_psp::tabla007]
III.4. Descripción de conceptos solicitados
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_control_de_razonabilidad_de_saldos__verificacion_de_que_el_saldo_total_de_fondos_276da5` — Control de razonabilidad de saldos
  - propiedades: {"descripcion": "Verificación de que el saldo total de fondos acreditados al último día del mes bajo informe sea igual al saldo del mes anterior más créditos menos débitos del Apartado B"}
  - tramo: El saldo total de los fondos acreditados en las cuentas de pago de los clientes correspondiente al último día del mes bajo informe reportado en el Apartado A, debe ser igual al que se haya remitido para el último día del mes anterior al bajo informe en dicho Apartado A más la suma de los créditos y menos la suma de los débitos del Apartado B correspondientes al mes bajo informe
- **Aristas** (1):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_psp_pdf` — Régimen Informativo PSPCP

## 13. `Condicion_pasivos_en_moneda_extranjera_significativa__cuando_los_pasivos_agregados_denomin_967bc9` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_tsa::S3` (e0, bloque de lista True; págs. 66, 67, 68, 69, 70, 71, 72):

```
[texto propio | punto S3]
Sección 3. Concentración del fondeo
A- Concentración del fondeo por contrapartes significativas
Se identificarán las fuentes de fondeo de la entidad, segregadas conforme a sus contrapartes
significativas, de acuerdo al esquema inserto en el Cuadro 3 anexo a la presente sección.
Se define como contraparte significativa -considerada a nivel de grupo económico- a aquella
que en términos agregados origina un fondeo igual o superior al 1% medido respecto del pasivo
total de la entidad al último día del trimestre informado.
El porcentaje de significatividad se calculará teniendo en cuenta el saldo al cierre del trimestre
por cada contraparte y grupo económico, considerando la suma de todos los productos
informados.
Deberá indicarse si la contraparte conforma grupo económico, consignando en tal caso la
denominación del grupo al que pertenece o su controlante.
Para aquellas contrapartes que integran más de un grupo económico, se informará únicamente
la denominación del grupo económico controlante, en su caso, determinado en función del
conocimiento que la entidad tenga de esa contraparte.
De resultar inferior a 50, el presente listado de contrapartes significativas, deberá completarse
hasta alcanzar esa cantidad, considerando un orden decreciente en el nivel de fondeo.
Cuando una contraparte no pueda determinarse (por ej. tenedores de certificados de emisión
de deuda que se negocia en los mercados secundarios), se imputará al último tenedor
conocido, o en su defecto, a los tenedores primarios.
Se efectúan las siguientes precisiones adicionales respecto de los datos a consignar en el
referido Cuadro 3:
1. Identificación de la contraparte significativa:
Clave Única de Identificación Tributaria (C.U.I.T.).
Código Único de Identificación Laboral (C.U.I.L.).
Clave de Identificación (C.D.I.).
Cuando la contraparte significativa resulte ser un Fondo Común de Inversión, se identificará
con el número asignado por la Comisión Nacional de Valores.
Para los depósitos judiciales, de corresponder, se utilizará como número de identificación
aquel con el que se encuentre registrado en los sistemas de cada entidad.
2. Denominación de la contraparte:
- Personas físicas y sociedades de hecho: se consignarán apellidos y nombres, en forma
completa;
- Restantes personas jurídicas: razón social o denominación, en forma completa.
Es responsabilidad de la entidad financiera que la “Denominación” del titular se corresponda
con la del “Padrón de Personas Físicas y Jurídicas”, toda vez que, en caso de diferir, el
Banco Central procederá a reemplazarla por la que figure en él para los datos de
identificación (tipo y número) informados.
Cuando el titular no esté incluido en dicho padrón, deberá informarse según la identificación
y denominación provista por la Agencia de Regulación y Control Aduanero (ARCA), según
corresponda.
Los depósitos judiciales se imputarán bajo la denominación de la causa a cuya orden se
encuentra el depósito.
3. Vinculación: se indicará si la contraparte es vinculada o no a la entidad financiera
4. Producto: se codificarán los productos conforme a la Tabla 1 anexa a la presente sección.
5. Saldo al cierre del trimestre: refiere al saldo de los contratos vigentes al cierre del trimestre,
respecto de cada contraparte, desagregado por producto.
6. Bandas temporales: se informará el importe para las siguientes bandas temporales tomando
como base el saldo al último día del trimestre informado y se asignarán a las distintas
bandas según su vencimiento contractual (aplicando los mismos criterios descriptos en la
Sección 2. de la presente): 1 mes, 1 a 3 meses, 4 a 6 meses, 7 a 12 meses y más de 12
meses.
B- Concentración del fondeo por producto significativo
Se define como productos significativos a aquellos que en términos agregados representan más
del 1% del pasivo total de la entidad al cierre del trimestre informado, de acuerdo con el esquema
inserto en el Cuadro 4 anexo a la presente sección, considerando los códigos de producto
descriptos en la Tabla 2.
Respecto de cada producto significativo, se proporcionarán el saldo al cierre del trimestre, el
porcentaje de significatividad y su correspondiente distribución en las distintas bandas según su
vencimiento contractual.
En su caso, deberá detallarse por cada producto significativo, cada uno de los paquetes de
productos que integra, hasta completar un máximo de 10, informándose asimismo respecto de
cada paquete el saldo al último día del trimestre informado, y su correspondiente distribución en
las distintas bandas según su vencimiento contractual (aplicando los mismos criterios descriptos
en la Sección 2.): 1 mes, 1 a 3 meses, 4 a 6 meses, 7 a 12 meses y más de 12 meses.
A tal fin, los paquetes de productos se codificarán según se indica en la Tabla 3. Los códigos
serán autodefinidos por cada entidad -según se especifique en las Normas de presentación-,
consignando la denominación comercial de los paquetes incluidos en el cuadro.
C- Concentración en activos y pasivos en moneda extranjera significativa
Cuando los pasivos agregados denominados en una moneda extranjera representen más del 5%
del total del pasivo, se informarán los importes registrados en las cuentas de activos, pasivos y
orden para esa moneda al cierre del trimestre, utilizando a estos efectos los códigos previstos en
el Plan y manual de cuentas para entidades financieras, conforme al modelo inserto en el Cuadro
5.
Cabe destacar las siguientes particularidades de integración:
1. Moneda: el código de moneda se consignará siguiendo las disposiciones del quinto párrafo
de Instrucciones particulares; el total del pasivo de la entidad (todas las monedas) se
identificará con el código de moneda 999.
2. Importes: corresponderá distribuir el saldo al cierre del trimestre por bandas temporales
según su estructura de vencimientos contractual, acorde con las instrucciones de la Sección
2.;
3. Bandas temporales: se informará el saldo para las siguientes bandas temporales: 1 mes, 1 a
3 meses, 4 a 6 meses, 7 a 12 meses y más de 12 meses.
Cuadro 3
[TABLA ri_tsa::tabla018 | página 69 | e0_tablas | posicional]
Fila 1: col1 = Contraparte significati- va ⟨abarca hasta col2⟩ | col3 = Nivel de conso- lidación | col4 = Vinculada (SI / NO) | col5 = Integra grupo económico (SI / NO) | col6 = Denomina- ción del Gru- po Económi- co controlan- te | col7 = Producto | col8 = Saldo al cierre del trimestre | col9 = % Significati- vidad | col10 = Bandas Temporales ⟨abarca hasta col15⟩
Fila 2: col1 = Identifi- cación | col2 = Denomina- ción | col10 = Primer mes | col11 = 1 a 3 meses | col12 = 4 a 6 meses | col13 = 7 a 12 meses | col14 = Más de 12 meses | col15 = No defi- nido
Fila 3: col7 = Tabla 1
[FIN TABLA ri_tsa::tabla018]
Tabla 1
[TABLA ri_tsa::tabla019 | página 69 | e0_tablas | columnas]
Columnas: Producto | Código Producto
Fila 1: Producto = Depósitos a la vista | Código Producto = 100
Fila 2: Producto = Depósitos a plazo | Código Producto = 200
Fila 3: Producto = Líneas de asistencia crediticia locales | Código Producto = 301
Fila 4: Producto = Préstamos interfinancieros | Código Producto = 302
Fila 5: Producto = Obligaciones Negociables | Código Producto = 303
Fila 6: Producto = Pases de Títulos Públicos | Código Producto = 304
Fila 7: Producto = Cauciones | Código Producto = 305
Fila 8: Producto = Otros | Código Producto = 900
[FIN TABLA ri_tsa::tabla019]
Cuadro 4
[TABLA ri_tsa::tabla020 | página 69 | e0_tablas | posicional]
Fila 1: col1 = Producto | col2 = Paquete de productos | col3 = Nivel de Consolidación | col4 = Saldo al cierre del trimestre | col5 = % Significatividad | col6 = Bandas Temporales ⟨abarca hasta col11⟩
Fila 2: col6 = Primer mes | col7 = 1 a 3 meses | col8 = 4 a 6 meses | col9 = 7 a 12 meses | col10 = Más de 12 | col11 = No definido
Fila 3: col1 = Tabla 2 | col2 = Tabla 3 | col6 = Importe | col7 = Importe | col8 = Importe | col9 = Importe | col10 = Importe | col11 = Importe
[FIN TABLA ri_tsa::tabla020]
Tabla 2
[TABLA ri_tsa::tabla021 | página 70 | e0_tablas | columnas]
Columnas: Producto Depósitos a la vista | Código
Fila 1: Producto Depósitos a la vista = Cuenta Corriente | Código = 101
Fila 2: Producto Depósitos a la vista = Caja de ahorros | Código = 102
Fila 3: Producto Depósitos a la vista = Cuenta sueldo / de la seguridad social | Código = 103
Fila 4: Producto Depósitos a la vista = Cuenta básica | Código = 104
Fila 5: Producto Depósitos a la vista = Cuenta gratuita universal | Código = 105
Fila 6: Producto Depósitos a la vista = Fondo de cese laboral para los trabajadores de la industria de la construcción | Código = 106
Fila 7: Producto Depósitos a la vista = Círculos cerrados | Código = 107
Fila 8: Producto Depósitos a la vista = Usuras pupilares | Código = 108
Fila 9: Producto Depósitos a la vista = Corriente para personas jurídicas | Código = 109
Fila 10: Producto Depósitos a la vista = Cuenta a la vista especial en moneda extranjera | Código = 110
Fila 11: Producto Depósitos a la vista = Cuenta especial para garantía de operaciones de futuros y opciones | Código = 111
Fila 12: Producto Depósitos a la vista = Caja de ahorro para el pago de planes o programas de ayuda social | Código = 112
Fila 13: Producto Depósitos a la vista = Cuenta a la vista para uso judicial | Código = 113
Fila 14: Producto Depósitos a la vista = Caja de ahorros Com. “A” 5526 | Código = 114
Fila 15: Producto Depósitos a la vista = Depósitos e inversiones a plazo
Fila 16: Producto Depósitos a la vista = Plazo fijo | Código = 201
Fila 17: Producto Depósitos a la vista = Inversiones a plazo constante | Código = 202
Fila 18: Producto Depósitos a la vista = Inversiones con opción de cancelación anticipada | Código = 203
Fila 19: Producto Depósitos a la vista = Inversiones con opción de renovación por plazo determinado | Código = 204
Fila 20: Producto Depósitos a la vista = Inversiones a plazo con retribución variable | Código = 205
Fila 21: Producto Depósitos a la vista = Cuentas especiales vinculadas al ingreso de fondos del exterior (Dec. 616/05) | Código = 206
Fila 22: Producto Depósitos a la vista = Otros Productos
Fila 23: Producto Depósitos a la vista = Líneas de asistencia crediticia locales | Código = 301
Fila 24: Producto Depósitos a la vista = Préstamos interfinancieros | Código = 302
Fila 25: Producto Depósitos a la vista = Obligaciones Negociables | Código = 303
Fila 26: Producto Depósitos a la vista = Pases de títulos públicos | Código = 304
Fila 27: Producto Depósitos a la vista = Cauciones | Código = 305
Fila 28: Producto Depósitos a la vista = Otros (1) | Código = 9XX
[FIN TABLA ri_tsa::tabla021]
(1) Detallar en forma secuencial a partir del 901 inclusive en adelante.
Tabla 3
[TABLA ri_tsa::tabla022 | página 71 | e0_tablas | posicional]
Fila 1: col1 = Denominación comercial del paquete de productos | col2 = Código
Fila 2: col1 = AAAAA | col2 = Numérico Autodefinido- Longitud máxima: 4
Fila 3: col1 = BBBBB
Fila 4: col1 = ….
Fila 5: col1 = ….
Fila 6: col1 = ….
Fila 7: col1 = XXXXX
[FIN TABLA ri_tsa::tabla022]
Cuadro 5
[TABLA ri_tsa::tabla023 | página 72 | e0_tablas | posicional]
Fila 1: col1 = Código partida | col2 = Concepto | col3 = Moneda | col4 = Nivel de Consolidación | col5 = Saldo al cierre del trimestre | col6 = Bandas Temporales ⟨abarca hasta col11⟩
Fila 2: col6 = Primer mes | col7 = 1 a 3 meses | col8 = 4 a 6 meses | col9 = 7 a 12 meses | col10 = Más de 12 meses | col11 = No definido
Fila 3: col2 = Activo
Fila 4: col1 = 115001 | col2 = Efectivo en caja
Fila 5: col1 = (...) | col2 = (...)
Fila 6: col2 = Pasivo
Fila 7: col1 = 315106 | col2 = Cuentas corrientes sin interés
Fila 8: col1 = (...) | col2 = (...)
Fila 9: col2 = Cuentas de orden
Fila 10: col1 = 715013 | col2 = Créditos obtenidos
Fila 11: col1 = (...) | col2 = (...)
Fila 12: col1 = 400000 | col2 = TOTAL PASIVO | col3 = 999
[FIN TABLA ri_tsa::tabla023]
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_pasivos_en_moneda_extranjera_significativa__cuando_los_pasivos_agregados_denomin_967bc9` — Pasivos en moneda extranjera significativa
  - propiedades: {"descripcion": "Cuando los pasivos agregados denominados en una moneda extranjera representen más del 5% del total del pasivo.", "umbrales": [{"tramo": "más del 5%", "valor": "5", "unidad": "porcentaje", "comparacion": "minimo_estricto", "regla_comparacion": "simple:mas_de", "origen": "e1", "tramo_verificado": "exacta", "verificado_en_tabla": false}]}
  - tramo: Cuando los pasivos agregados denominados en una moneda extranjera representen más del 5% del total del pasivo
- **Aristas** (3):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_informar_los_importes_registrados_en_las_cuentas_de_activos_pasivos_y_orden_para_89eb4d` — Información de activos, pasivos y orden en moneda extranjera significativa
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_tsa_pdf` — Ratio de Cobertura de Liquidez
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_deber_de_desagregar_los_saldos_y_flujos_utilizando_los_codigos_de_partidas_previ_dc6a7d` — Desagregar saldos y flujos con códigos de partidas del régimen · {"alcance": "interna", "destino": "ri_tsa::S3", "evidencia": "pertinente, las instrucciones de integración descriptas en las\nsecciones 3. a 5. de ese régimen"}

## 14. `Condicion_excesos_admitidos_si_conciliacion_evidencia_no_exceso_al_100__los_excesos_se_con_6a5884` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_ai::6.1` (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S6]
Sección 6. Disposiciones transitorias
[texto propio | punto 6.1]
6.1. Tratamiento de los excesos originados en el cómputo del 50 % -en lugar del 100 %- de los re-
sultados provenientes de los ajustes NIIF por primera vez dentro de la RPC (Período enero –
marzo 2018).
Estos excesos se consideran admitidos (es decir que no constituirán incumplimientos) de veri-
ficarse las siguientes condiciones:
c) surjan de la última conciliación de los estados contables trimestrales en el marco de la
convergencia a NIIF que cuente con informe de auditor externo;
d) dicha conciliación evidencie que de haberse considerado los resultados positivos al
100 % -en lugar de al 50 %- no se hubiera registrado tal exceso.
De reunir los requisitos citados, se consignará en la partida 401 la porción pertinente para la
neutralización del exceso generado.
A tal fin, se consignará como “número” y “fecha de Resolución” la de la presente comunica-
ción.
También se agregará una descripción detallada del cálculo del importe para el período in-
formado.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_excesos_admitidos_si_conciliacion_evidencia_no_exceso_al_100__los_excesos_se_con_6a5884` — Excesos admitidos si conciliación evidencia no exceso al 100%
  - propiedades: {"descripcion": "Los excesos se consideran admitidos si la conciliación evidencia que de haberse considerado los resultados positivos al 100% en lugar del 50% no se hubiera registrado tal exceso", "umbrales": [{"tramo": "al 100 % -en lugar de al 50 %-", "valor": "100", "unidad": "porcentaje", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}, {"tramo": "al 100 % -en lugar de al 50 %-", "valor": "50", "unidad": "porcentaje", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}
  - tramo: dicha conciliación evidencie que de haberse considerado los resultados positivos al 100 % -en lugar de al 50 %- no se hubiera registrado tal exceso
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_de_reunir_los_requisitos_citados_se_consignara_en_la_partida_401_la_porcion_pert_149af4` — Consignar en partida 401 porción para neutralización
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ai_pdf` — Régimen Informativo sobre Bases Consolidadas

## 15. `Condicion_trimestre_finalizado_el_31_de_diciembre__el_trimestre_reportado_es_el_finalizado_1e69e0` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_psp::SVI` (e0, bloque de lista True; págs. 14):

```
[texto propio | punto SVI]
Sección VI. APARTADO C: INFORMACION TRIMESTRAL
Se deberá remitir un Informe especial de auditor externo que certifique el cumplimiento de las nor-
mas establecidas por el BCRA que resulten aplicables a los “Proveedores de servicios de pago que
ofrecen cuentas de pago" y la integridad de la información contenida en el Apartado A del presente
régimen informativo, con la pertinente certificación por el Consejo Profesional de Ciencias Económi-
cas en el que se encuentren matriculados.
Cuando se trate del trimestre finalizado el 31 de diciembre, deberá contener además la opinión so-
bre el cumplimiento de las normas sobre “Protección de los usuarios de servicios financieros”.
El informe deberá realizarse conforme al modelo y procedimientos establecidos en el T.O. "Informe
de Contadores Públicos Independientes sobre el cumplimiento de las Normas del BCRA por parte
de los Proveedores de Servicios de Pago".
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_trimestre_finalizado_el_31_de_diciembre__el_trimestre_reportado_es_el_finalizado_1e69e0` — Trimestre finalizado el 31 de diciembre
  - propiedades: {"descripcion": "El trimestre reportado es el finalizado el 31 de diciembre."}
  - tramo: Cuando se trate del trimestre finalizado el 31 de diciembre
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_el_informe_debe_contener_la_opinion_sobre_el_cumplimiento_de_las_normas_sobre_pr_961f55` — Incluir opinión sobre Protección de usuarios
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_psp_pdf` — Régimen Informativo PSPCP

## 16. `Condicion_suspension_total_o_parcial_de_operaciones_o_revocacion_de_autorizacion__se_verif_986e53` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `seggar::8.1` (e0, bloque de lista True; págs. 9):

```
[encabezado | punto S8]
8. Legislación aplicable.
[texto propio | punto 8.1]
8.1. Ley 24.485 (*).
Artículo 1°: Créase el Sistema de Seguro de Garantía de los Depósitos que será limitado,
obligatorio y oneroso, con el objeto de cubrir los riesgos de los depósitos banca-
rios, en forma subsidiaria y complementaria al sistema de privilegios y protección
de depósitos establecido por la Ley de Entidades Financieras, sin comprometer
los recursos del Banco Central de la República Argentina ni del Tesoro Nacional.
Cuando el Banco Central de la República Argentina dispusiera la suspensión total
o parcial de las operaciones o la revocación de la autorización para funcionar de
una entidad financiera, el Sistema de Seguro de Garantía de los Depósitos debe-
rá disponer el reintegro a sus titulares de las sumas depositadas en las cuentas
especiales para la acreditación de remuneraciones, habilitadas en virtud de las
disposiciones contenidas en el artículo 124 de la Ley 20.744 (texto ordenado en
1976), en un plazo no mayor de cinco (5) días hábiles desde la fecha de la sus-
pensión o revocación de la autorización para funcionar.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_suspension_total_o_parcial_de_operaciones_o_revocacion_de_autorizacion__se_verif_986e53` — Suspensión total o parcial de operaciones o revocación de autorización
  - propiedades: {"descripcion": "Se verifica cuando el Banco Central de la República Argentina dispone la suspensión total o parcial de las operaciones o la revocación de la autorización para funcionar de una entidad financiera"}
  - tramo: Cuando el Banco Central de la República Argentina dispusiera la suspensión total o parcial de las operaciones o la revocación de la autorización para funcionar de una entidad financiera
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_el_sistema_de_seguro_de_garantia_de_los_depositos_debe_disponer_el_reintegro_a_s_cf1e3d` — Reintegro de depósitos en cuentas especiales para remuneraciones
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_seggar_pdf` — Seguro de Depósitos

## 17. `Condicion_condicion_prestacion_de_ayuda_economica_excluida__la_prestacion_del_servicio_de__5af448` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `asomut::2.5` (e0, bloque de lista True; págs. 4):

```
[encabezado | punto S2]
2. Excepciones.
[chapeau_seccion | punto S2]
La prestación del servicio de ayuda económica queda excluida de ese encuadramiento cuando
se verifiquen la totalidad de las siguientes características:
[texto propio | punto 2.5]
2.5. Tasa de interés.
Los importes recibidos son retribuidos a una tasa que, por todo concepto, no excede de la
establecida por el Banco de la Nación Argentina para los depósitos a plazo fijo de 30 días.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condicion_prestacion_de_ayuda_economica_excluida__la_prestacion_del_servicio_de__5af448` — Condición — prestación de ayuda económica excluida
  - propiedades: {"descripcion": "La prestación del servicio de ayuda económica queda excluida cuando se verifican todas las características enumeradas, entre ellas la tasa de interés conforme al punto 2.5"}
  - tramo: La prestación del servicio de ayuda económica queda excluida de ese encuadramiento cuando se verifiquen la totalidad de las siguientes características
- **Aristas** (2):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_la_tasa_de_retribucion_de_los_importes_recibidos_no_puede_exceder_la_tasa_establ_b47a27` — Tope tasa de interés — depósitos a plazo fijo
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_asomut_pdf` — Texto Ordenado ASOMUT · {"rol_fuente": "derivada_de_procedencia"}

## 18. `Condicion_cheques_presentados_electronicamente_con_imagen_capturada__el_supuesto_es_que_se_a8bda4` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `consyr::S2` (e0, bloque de lista True; págs. 5, 6):

```
[texto propio | punto S2]
2. Conservación de documentos.
Las entidades financieras pueden, bajo su exclusiva responsabilidad, optar por los procedimien-
tos y términos que estimen más convenientes para la conservación, guarda o archivo de los
comprobantes vinculados a su operatoria.
Toda documentación original en papel cuya reproducción se admite o admita, que efectivamente
haya sido realizada según lo establecido en el presente régimen, previo a su destrucción física
deberá ser puesta a disposición de los interesados, mediante notificación fehaciente o con alguna
de las modalidades previstas en las normas sobre “Comunicación por medios electrónicos para el
cuidado del medio ambiente” –en este último caso, sujeto a la observancia de las condiciones
establecidas en esas normas–, por el plazo de 6 meses a contar desde dicha notificación.
En el caso de los cheques, los libradores podrán solicitar el documento físico –en las sedes,
sucursales, o agencias donde los libradores tengan abiertas sus cuentas corrientes– por un plazo
de 60 días corridos desde la fecha de pago.
Sin perjuicio de ello, cuando se trate de cheques presentados electrónicamente al cobro y cuya
imagen haya sido capturada por los clientes las entidades financieras podrán –bajo su responsa-
bilidad– prever en los contratos celebrados con esos clientes que estos últimos deban conservar
los documentos originales por el plazo antes citado y mantenerlos a su disposición en caso de
requerimiento.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_cheques_presentados_electronicamente_con_imagen_capturada__el_supuesto_es_que_se_a8bda4` — Cheques presentados electrónicamente con imagen capturada
  - propiedades: {"descripcion": "El supuesto es que se trate de cheques presentados electrónicamente al cobro y cuya imagen haya sido capturada por los clientes."}
  - tramo: cuando se trate de cheques presentados electrónicamente al cobro y cuya imagen haya sido capturada por los clientes
- **Aristas** (3):
  - (extraccion) —condicion_de→ Potestad `Potestad_facultad_entidades_prever_conservacion_documentos_por_clientes__las_entidades_fi_03df20` — Facultad entidades prever conservación documentos por clientes
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_consyr_pdf` — Instrumentación de documentos
  - (remision_derivada) —remite_a→ TextoOrdenado `TextoOrdenado_icmecma_pdf` — Comunicación por medios electrónicos · {"alcance": "to_entero", "destino": "icmecma::TO", "evidencia": "normas sobre “Comunicación por medios electrónicos para el\ncuidado del medio ambiente"}

## 19. `Condicion_causal_de_impedimento_del_bcra__cuando_surge_de_la_consulta_al_bcra_alguna_otra__8646dd` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `cedin::6.5` (e0, bloque de lista True; págs. 8):

```
[encabezado | punto S6]
6. Verificación del certificado.
[chapeau_seccion | punto S6]
La entidad financiera deberá realizar las siguientes acciones:
[texto propio | punto 6.5]
6.5. En el caso de constatar que el certificado no cumple con alguna de las características de
seguridad definidas y/o de los requisitos antes enunciados, exista inconsistencia en sus
datos o surja de la consulta al BCRA alguna otra causal de impedimento para el pago o
endoso, la entidad financiera procederá a retener el CEDIN -rechazando el pago o endo-
so, en su caso- dejando constancia en el mismo de la causa del rechazo e informando es-
ta situación al BCRA.
Sin perjuicio de dar intervención a las autoridades policiales cuando las circunstancias
hagan suponer una posible maniobra defraudatoria, en todos los casos se deberá levan-
tar un Acta de Retención con medios mecanográficos o informáticos. En ella se asentarán
todas las características y datos que contribuyan a identificar el certificado y demás cir-
cunstancias relevantes, causa del rechazo y los datos de la persona que lo haya presen-
tado (nombre completo, tipo y número de documento y domicilio), que será invitada a
suscribirla.
El acta será suscripta por el funcionario que haya efectuado el rechazo y por otro que de-
berá haber estado presente durante su confección. Dichos funcionarios procederán a ex-
traer copias de la documentación identificatoria del presentante, las que certificarán con
su firma y sello aclaratorio.
El certificado, Acta de Retención y copia certificada de la documentación de identificación
presentada se remitirán con todo elemento que se entienda relevante al BCRA, conforme
a lo previsto en el punto 11.
La entidad entregará al presentante fotocopia de ambas caras del CEDIN rechazado y
una copia del Acta de Retención suscripta por los funcionarios intervinientes, bajo recibo.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_causal_de_impedimento_del_bcra__cuando_surge_de_la_consulta_al_bcra_alguna_otra__8646dd` — Causal de impedimento del BCRA
  - propiedades: {"descripcion": "Cuando surge de la consulta al BCRA alguna otra causal de impedimento para el pago o endoso"}
  - tramo: surja de la consulta al BCRA alguna otra causal de impedimento para el pago o endoso
- **Aristas** (3):
  - (extraccion) —condicion_de→ Operacion `Operacion_retencion_de_cedin_por_incumplimiento__cedin_6_5_60c20f` — Retención de CEDIN por incumplimiento
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_cedin_pdf` — Texto Ordenado CEDIN
  - (remision_derivada) ←remite_a— Condicion `Condicion_situaciones_previstas_en_punto_6_5__se_activa_cuando_se_verifican_las_situacione_60f1d0` — Situaciones previstas en punto 6.5 · {"alcance": "interna", "destino": "cedin::6.5", "evidencia": "13.1. Ante las situaciones previstas en el punto 6.5., el Banco Central -"}

## 20. `Condicion_verificacion_pericial_de_autoria_y_autenticidad__la_firma_olografa_en_documentos_52a054` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `consyr::1.2` (e0, bloque de lista True; págs. 3):

```
[encabezado | punto S1]
1. Instrumentación de documentos.
[texto propio | punto 1.2]
1.2. Firma.
Se admiten las firmas ológrafas efectuadas originalmente sobre documentos electrónicos u
otras tecnologías similares en la medida que puedan efectuarse sobre aquéllas verificacio-
nes periciales que permitan probar su autoría y autenticidad.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_verificacion_pericial_de_autoria_y_autenticidad__la_firma_olografa_en_documentos_52a054` — Verificación pericial de autoría y autenticidad
  - propiedades: {"descripcion": "La firma ológrafa en documentos electrónicos se admite cuando sea posible efectuar verificaciones periciales que permitan probar su autoría y autenticidad."}
  - tramo: en la medida que puedan efectuarse sobre aquéllas verificaciones periciales que permitan probar su autoría y autenticidad
- **Aristas** (2):
  - (extraccion) —condicion_de→ Potestad `Potestad_admision_de_firmas_olografas_en_documentos_electronicos__se_admiten_las_firmas_o_fb71af` — Admisión de firmas ológrafas en documentos electrónicos
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_consyr_pdf` — Instrumentación de documentos

## 21. `Condicion_simultaneidad_con_habilitacion_punto_3_1__la_apertura_de_cuentas_corrientes_debe_2d9e7b` — NG:resto · vigilancia:1

Texto que vio E3 de `cryl::3.2::intro` (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S3]
Sección 3. Habilitaciones.
[encabezado | punto 3.2]
3.2. Apertura de cuentas corrientes.
[bloque intro | punto 3.2]
Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar la liquidación de las
operaciones “DVP”, el BCRA procederá a la apertura de cuentas corrientes con actividad res-
tringida, a nombre de los titulares de cuentas de registro que no sean entidades financieras, en
los términos de la Ley de Entidades Financieras.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_simultaneidad_con_habilitacion_punto_3_1__la_apertura_de_cuentas_corrientes_debe_2d9e7b` — Simultaneidad con habilitación punto 3.1
  - propiedades: {"descripcion": "La apertura de cuentas corrientes debe realizarse simultáneamente con la habilitación del punto 3.1"}
  - tramo: Simultáneamente con la habilitación del punto 3.1.
- **Aristas** (9):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_el_bcra_procedera_a_la_apertura_de_cuentas_corrientes_con_actividad_restringida__70df93` — BCRA procederá a apertura de cuentas corrientes
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_cryl_pdf` — Texto Ordenado CRyL
  - (remision_derivada) —remite_a→ Condicion `Condicion_autorizacion_previa_del_bcra_entidades_financieras__las_entidades_financieras_co_060872` — Autorización previa del BCRA — entidades financieras · {"alcance": "interna", "destino": "cryl::3.1", "evidencia": "Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar"}
  - (remision_derivada) —remite_a→ Condicion `Condicion_residencia_de_cuotapartistas_fci__los_fondos_comunes_de_inversion_deben_tener_cu_300ed6` — Residencia de cuotapartistas — FCI · {"alcance": "interna", "destino": "cryl::3.1", "evidencia": "Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_la_solicitud_de_apertura_de_cuentas_corrientes_monetarias_debe_realizarse_confor_f53762` — Cumplimiento de procedimiento — solicitud de cuentas corrientes · {"alcance": "interna", "destino": "cryl::3.1", "evidencia": "Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_los_interesados_deben_presentar_una_nota_solicitando_la_apertura_de_cuenta_s_de__acd7aa` — Presentación de nota — solicitud de apertura de cuenta de registro · {"alcance": "interna", "destino": "cryl::3.1", "evidencia": "Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_para_llevar_adelante_sus_operaciones_los_sujetos_habilitados_deben_solicitar_la__ebbf43` — Solicitud de cuentas corrientes monetarias — operaciones · {"alcance": "interna", "destino": "cryl::3.1", "evidencia": "Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_apertura_de_cuentas_de_registro__cryl_3_1_162ead` — Apertura de cuentas de registro · {"alcance": "interna", "destino": "cryl::3.1", "evidencia": "Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar"}
  - (remision_derivada) —remite_a→ Potestad `Potestad_discrecion_del_bcra_habilitacion_de_otras_instituciones__el_bcra_y_o_el_organo_c_321919` — Discreción del BCRA — habilitación de otras instituciones · {"alcance": "interna", "destino": "cryl::3.1", "evidencia": "Simultáneamente con la habilitación del punto 3.1., a efectos de posibilitar"}

## 22. `Condicion_denuncia_de_extravio_sustraccion_o_adulteracion__el_titular_o_tenedor_desposeido_39c497` — NG:resto · vigilancia:1

Texto que vio E3 de `ctavis::7.2.3.1` (e0, bloque de lista True; págs. 30):

```
[encabezado | punto S7]
Sección 7. Central de letras de cambio rechazadas, Central de libradores de letras de cambio inhabilitados y Central de letras de cambio denunciadas como extraviadas, sustraídas o adulteradas.
[encabezado | punto 7.2]
7.2. Motivos de inclusión.
[encabezado | punto 7.2.3]
7.2.3. En la “Central de letras de cambio denunciadas como extraviadas, sustraídas o adultera-
das”.
[texto propio | punto 7.2.3.1]
7.2.3.1. Haber denunciado el titular o tenedor desposeído a la entidad el extravío, la sus-
tracción o la adulteración de los documentos mencionados en el punto 6.1., ex-
cepto la fórmula especial para solicitar cuadernos de letras de cambio.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_denuncia_de_extravio_sustraccion_o_adulteracion__el_titular_o_tenedor_desposeido_39c497` — Denuncia de extravío, sustracción o adulteración
  - propiedades: {"descripcion": "El titular o tenedor desposeído debe haber denunciado a la entidad el extravío, la sustracción o la adulteración de los documentos de cambio referidos en el punto 6.1."}
  - tramo: Haber denunciado el titular o tenedor desposeído a la entidad el extravío, la sustracción o la adulteración de los documentos mencionados en el punto 6.1.
- **Aristas** (3):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ctavis_pdf` — Cuentas a la vista con letras de cambio
  - (remision_derivada) —remite_a→ Condicion `Condicion_alcance_a_letras_de_cambio_y_sus_formulas__las_normas_de_la_seccion_6_se_aplican_2e05af` — Alcance a letras de cambio y sus fórmulas · {"alcance": "interna", "destino": "ctavis::6.1", "evidencia": "sus-\ntracción o la adulteración de los documentos mencionados en el punto 6.1., ex-\ncepto la fórmula"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_letras_de_cambio_extravio_sustraccion_adulteracion__ctavis_6_1_cb364a` — Letras de cambio — extravío, sustracción, adulteración · {"alcance": "interna", "destino": "ctavis::6.1", "evidencia": "sus-\ntracción o la adulteración de los documentos mencionados en el punto 6.1., ex-\ncepto la fórmula"}

## 23. `Condicion_correspondencia_con_lineas_de_financiamiento_asignadas__las_financiaciones_se_co_19eb6c` — NG:resto · vigilancia:1

Texto que vio E3 de `finsec::3.1.9` (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S3]
Sección 3. Operaciones comprendidas.
[encabezado | punto 3.1]
3.1. Conceptos incluidos.
[intersticial | punto 3.1]
Además, se considerarán las siguientes operaciones:
[texto propio | punto 3.1.9]
3.1.9. Financiaciones, en todas sus modalidades, otorgadas por y/o a través de bancos del ex-
terior sobre los que la entidad local ejerce el control en los términos previstos en el pun-
to 1.2.2.1. de las normas sobre “Grandes exposiciones al riesgo de crédito” y no se
hallen sujetos a supervisión consolidada, cuando se correspondan con líneas de finan-
ciamiento asignadas a ellos por la entidad financiera local.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_correspondencia_con_lineas_de_financiamiento_asignadas__las_financiaciones_se_co_19eb6c` — Correspondencia con líneas de financiamiento asignadas
  - propiedades: {"descripcion": "Las financiaciones se corresponden con líneas de financiamiento asignadas a los bancos del exterior por la entidad financiera local."}
  - tramo: cuando se correspondan con líneas de financiamiento asignadas a ellos por la entidad financiera local
- **Aristas** (2):
  - (extraccion) —condicion_de→ Operacion `Operacion_financiaciones_otorgadas_por_a_traves_de_bancos_del_exterior__finsec_3_1_9_abd1a2` — Financiaciones otorgadas por/a través de bancos del exterior
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_finsec_pdf` — Texto Ordenado Sector Público No Financiero · {"rol_fuente": "derivada_de_procedencia"}

## 24. `Condicion_periodo_de_6_meses__durante_un_periodo_de_6_meses__fimipyme_11_1_3_8e1b07` — NG:resto · vigilancia:1

Texto que vio E3 de `fimipyme::11.1.3` (e0, bloque de lista True; págs. 19):

```
[encabezado | punto S11]
Sección 11. Incumplimientos.
[encabezado | punto 11.1]
11.1. Incremento de la exigencia de efectivo mínimo.
[intro | punto 11.1]
El defecto de aplicación de los cupos de la Sección 2. generará un incremento en la exi-
gencia de efectivo mínimo en promedio en pesos, de acuerdo con lo siguiente:
[texto propio | punto 11.1.3]
11.1.3. A partir de la exigencia del 1.4.22 por un importe equivalente al defecto del cupo
2021/2022 incrementado en un 10 % y por un período de 6 meses.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_periodo_de_6_meses__durante_un_periodo_de_6_meses__fimipyme_11_1_3_8e1b07` — Período de 6 meses
  - propiedades: {"descripcion": "Durante un período de 6 meses", "umbrales": [{"tramo": "por un período de 6 meses", "valor": "6", "unidad": "meses", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador_plazo", "origen": "e1", "tramo_verificado": "exacta"}]}
  - tramo: por un período de 6 meses
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_a_partir_de_la_exigencia_del_1_4_22_se_incrementa_la_exigencia_de_efectivo_minim_798d1c` — Aplicación incremento exigencia efectivo mínimo — defecto cupo
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_fimipyme_pdf` — Plataformas para el financiamiento MiPyME

## 25. `Condicion_requerimiento_de_la_sefyc__cuando_la_superintendencia_de_entidades_financieras_y_db0b9f` — NG:resto · vigilancia:1

Texto que vio E3 de `prevmi::5.1.7::intro` (e0, bloque de lista True; págs. 17):

```
[encabezado | punto S5]
Sección 5. Disposiciones transitorias.
[encabezado | punto 5.1.7]
5.1.7. Requerimientos de la Superintendencia de Entidades Financieras y Cambiarias.
[bloque intro | punto 5.1.7]
Ante requerimiento que formule la SEFyC, las entidades financieras deberán constituir
previsiones por riesgo de incobrabilidad en los porcentajes que se establezcan cuando:
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_requerimiento_de_la_sefyc__cuando_la_superintendencia_de_entidades_financieras_y_db0b9f` — Requerimiento de la SEFyC
  - propiedades: {"descripcion": "Cuando la Superintendencia de Entidades Financieras y Cambiarias formule un requerimiento."}
  - tramo: Ante requerimiento que formule la SEFyC
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_las_entidades_financieras_deberan_constituir_previsiones_por_riesgo_de_incobrabi_7aa442` — Constituir previsiones por riesgo de incobrabilidad
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_prevmi_pdf` — Prevención del Lavado de Activos

## 26. `Condicion_fondos_revisten_caracter_de_responsabilidades_eventuales__los_fondos_revistan_el_8743e4` — NG:resto · vigilancia:1

Texto que vio E3 de `fimipyme::4.1::cierre` (e0, bloque de lista True; págs. 10):

```
[encabezado | punto S4]
Sección 4. Financiaciones elegibles.
[encabezado | punto 4.1]
4.1. Financiación de proyectos de inversión.
[bloque cierre | punto 4.1]
No podrán encuadrarse como aplicación elegible las financiaciones que se acuerden con-
forme a otros regímenes especiales de crédito en la medida en que los fondos para dichas
asistencias sean provistos a la entidad con ese fin específico o revistan el carácter de res-
ponsabilidades eventuales.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_fondos_revisten_caracter_de_responsabilidades_eventuales__los_fondos_revistan_el_8743e4` — Fondos revisten carácter de responsabilidades eventuales
  - propiedades: {"descripcion": "Los fondos revistan el carácter de responsabilidades eventuales"}
  - tramo: o revistan el carácter de responsabilidades eventuales
- **Aristas** (10):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_no_pueden_encuadrarse_como_aplicacion_elegible_las_financiaciones_acordadas_conf_c226e7` — Exclusión financiaciones otros regímenes especiales
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_fimipyme_pdf` — Plataformas para el financiamiento MiPyME · {"rol_fuente": "derivada_de_procedencia"}
  - (remision_derivada) ←remite_a— Definicion `Definicion_entidades_alcanzadas_grupo_a_y_agentes_financieros__las_entidades_financieras_co_02c06e` — Entidades alcanzadas — Grupo A y agentes financieros · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "Autoridades de entidades financieras”, para lo cual el indicador del\npunto 4.1. de esas normas deberá"}
  - (remision_derivada) ←remite_a— Excepcion `Excepcion_quedan_excluidas_de_los_destinos_de_los_puntos_4_1_y_4_2_las_mipyme_con_activida_063483` — Exclusión MiPyME agrícola — destinos 4.1 y 4.2 · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "3.1.1. de los destinos de los puntos 4.1. y 4.2.: las MiPyME con actividad"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_las_financiaciones_del_punto_4_1_deben_ser_denominadas_en_pesos__fimipyme_5_2_be220d` — Denominación en pesos — financiaciones punto 4.1 · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "5.2. Moneda y plazos.\nLas financiaciones del punto 4.1. deberán ser denominadas"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_las_financiaciones_del_punto_4_1_deben_tener_al_momento_del_desembolso_un_plazo__6b448b` — Plazo promedio mínimo 24 meses — financiaciones punto 4.1 · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "5.2. Moneda y plazos.\nLas financiaciones del punto 4.1. deberán ser denominadas"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_incorporacion_mediante_cesion_o_descuento_de_financiaciones__fimipyme_4_3_3_428da9` — Incorporación mediante cesión o descuento de financiaciones · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "mediante cesión o descuento de las financiaciones previstas en los\npuntos 4.1. y/o 4.2. otorgadas"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_al_menos_el_30_de_los_cupos_debera_destinarse_a_lo_previsto_en_el_punto_4_1__fim_9324c1` — Mínimo 30 % destino cupo — punto 4.1 · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "el 30 % de los cupos deberá destinarse a lo previsto en el punto 4.1."}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_el_plazo_total_de_las_financiaciones_del_punto_4_1_no_sera_inferior_a_36_meses___1b166a` — Plazo total mínimo 36 meses — financiaciones punto 4.1 · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "5.2. Moneda y plazos.\nLas financiaciones del punto 4.1. deberán ser denominadas"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_la_tasa_de_interes_maxima_para_los_destinos_del_punto_4_1_es_del_112_nominal_anu_6fd544` — Tasa máxima 112 % nominal anual fija · {"alcance": "interna", "destino": "fimipyme::4.1", "evidencia": "5.1.1. Destinos del punto 4.1.: 112 % nominal anual"}

## 27. `Condicion_calibracion_de_montos_estabilidad_y_liquidez_esperadas__los_montos_disponibles_y_0da97d` — NG:resto · vigilancia:1

Texto que vio E3 de `ratiofn::1.3` (e0, bloque de lista True; págs. 3, 4):

```
[encabezado | punto S1]
Sección 1. Consideraciones generales.
[texto propio | punto 1.3]
1.3. Determinación del NSFR.
El NSFR se define como el cociente entre el monto disponible de fondeo estable y el monto re-
querido de fondeo estable:
donde:
MDFE (Monto disponible de fondeo estable): es la parte del capital y de los pasivos de la enti-
dad financiera –computados conforme a lo previsto en la Sección 2.– que se espera es-
tén disponibles durante un período de un año.
MRFE (Monto requerido de fondeo estable): es el monto de fondeo necesario durante ese pe-
ríodo –computado conforme a lo previsto en la Sección 3.–, que está en función de la li-
quidez y plazo residual de los activos de la entidad y de sus compromisos fuera de ba-
lance.
Los montos disponibles y requeridos de fondeo estable determinados conforme a estas dispo-
siciones están calibrados para reflejar la estabilidad esperada de los pasivos y la liquidez espe-
rada de los activos de la entidad financiera durante el período de un año.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_calibracion_de_montos_estabilidad_y_liquidez_esperadas__los_montos_disponibles_y_0da97d` — Calibración de montos — estabilidad y liquidez esperadas
  - propiedades: {"descripcion": "Los montos disponibles y requeridos de fondeo estable están calibrados para reflejar la estabilidad esperada de los pasivos y la liquidez esperada de los activos durante un período de un año", "umbrales": [{"tramo": "un año", "valor": "1", "unidad": "anios", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador_plazo", "origen": "descripcion", "tramo_verificado": "exacta"}]}
  - tramo: Los montos disponibles y requeridos de fondeo estable determinados conforme a estas disposiciones están calibrados para reflejar la estabilidad esperada de los pasivos y la liquidez esperada de los activos de la entidad financiera durante el período de un año
- **Aristas** (1):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ratiofn_pdf` — Ratio de fondeo neto estable

## 28. `Condicion_fallo_del_sistema_principal_de_apertura__la_puerta_de_emergencia_o_el_mecanismo__3217b2` — NG:resto · vigilancia:1

Texto que vio E3 de `seguef::2.4.5` (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S2]
Sección 2. Dispositivos mínimos de seguridad para entidades financieras bancarias.
[encabezado | punto 2.4]
2.4. Tesoro blindado
[texto propio | punto 2.4.5]
2.4.5. Deberá contar con una puerta de emergencia o un mecanismo alternativo de doble co-
mando en la puerta principal para asegurar su apertura en caso de fallar el sistema prin-
cipal.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_fallo_del_sistema_principal_de_apertura__la_puerta_de_emergencia_o_el_mecanismo__3217b2` — Fallo del sistema principal de apertura
  - propiedades: {"descripcion": "La puerta de emergencia o el mecanismo alternativo de doble comando debe asegurar la apertura cuando falla el sistema principal."}
  - tramo: en caso de fallar el sistema principal
- **Aristas** (2):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_seguef_pdf` — Medidas mínimas de seguridad · {"rol_fuente": "derivada_de_procedencia"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_resultan_aplicables_las_disposiciones_de_los_puntos_2_4_2_al_2_4_6_a_los_tesoros_6ab4e9` — Aplicabilidad de disposiciones de puntos 2.4.2. al 2.4.6. · {"alcance": "interna", "destino": "seguef::2.4.5", "evidencia": "del punto 2.4.1.\nResultan aplicables las disposiciones de los puntos 2.4.2. al 2.4.6."}

## 29. `Condicion_plazo_minimo_180_dias__el_deposito_debe_tener_un_plazo_minimo_de_180_dias__depin_8062ea` — NG:resto · vigilancia:1

Texto que vio E3 de `depinv::2.3.1.3` (e0, bloque de lista True; págs. 18):

```
[encabezado | punto S2]
Sección 2. Inversiones a plazo.
[encabezado | punto 2.3]
2.3. Con opción de cancelación anticipada.
[encabezado | punto 2.3.1]
2.3.1. Plazo mínimo.
[texto propio | punto 2.3.1.3]
2.3.1.3. Otros: 180 días, con posibilidad de cancelación anticipada.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_plazo_minimo_180_dias__el_deposito_debe_tener_un_plazo_minimo_de_180_dias__depin_8062ea` — Plazo mínimo 180 días
  - propiedades: {"descripcion": "El depósito debe tener un plazo mínimo de 180 días", "umbrales": [{"tramo": "180 días", "valor": "180", "unidad": "dias", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador_plazo", "origen": "e1", "tramo_verificado": "exacta"}]}
  - tramo: 180 días
- **Aristas** (2):
  - (extraccion) —condicion_de→ Operacion `Operacion_deposito_de_inversion_a_plazo_otros__depinv_2_3_1_3_a17e3d` — Depósito de inversión a plazo — otros
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_depinv_pdf` — Depósitos de inversión · {"rol_fuente": "derivada_de_procedencia"}

## 30. `Condicion_incumplimiento_regularizado_duracion_en_meses__una_vez_regularizado_el_incumplim_c36ced` — NG:resto · vigilancia:1

Texto que vio E3 de `incuca::2.3.3` (e0, bloque de lista True; págs. 7):

```
[encabezado | punto S2]
Sección 2. Excesos a las relaciones técnicas y posiciones de derivados.
[encabezado | punto 2.3]
2.3. Incumplimientos detectados por la Superintendencia de Entidades Financieras y Cambiarias.
[texto propio | punto 2.3.3]
2.3.3. Tratamiento del incumplimiento determinado.
Originará el incremento de la exigencia de capital mínimo por riesgo de crédito por un im-
porte equivalente al 150 % del exceso a la relación a partir del mes en que quede firme,
mientras subsista el incumplimiento y, adicionalmente una vez regularizado, por una can-
tidad de meses igual al número de períodos durante los cuales se verificó el incumpli-
miento detectado por la SEFyC.
El cómputo del apartamiento se efectuará considerando el mayor importe de exceso re-
gistrado en los mencionados períodos y en los siguientes, en tanto se mantenga el in-
cumplimiento y aun cuando la información de los siguientes períodos sea ingresada en
tiempo y forma.
En el caso de las relaciones crediticias, dicho cómputo se realizará considerando el ma-
yor importe diario de exceso, respecto de los clientes que lo originaron, registrado en ta-
les períodos.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_incumplimiento_regularizado_duracion_en_meses__una_vez_regularizado_el_incumplim_c36ced` — Incumplimiento regularizado — duración en meses
  - propiedades: {"descripcion": "Una vez regularizado el incumplimiento, el incremento de capital se mantiene por una cantidad de meses igual al número de períodos durante los cuales se verificó el incumplimiento detectado por la SEFyC."}
  - tramo: adicionalmente una vez regularizado, por una cantidad de meses igual al número de períodos durante los cuales se verificó el incumplimiento detectado por la SEFyC
- **Aristas** (2):
  - (extraccion) —condicion_de→ Operacion `Operacion_incremento_de_exigencia_de_capital_minimo_por_riesgo_de_credito__incuca_2_3_3_eb4fe0` — Incremento de exigencia de capital mínimo por riesgo de crédito
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_incuca_pdf` — Incumplimientos de capital mínimo

