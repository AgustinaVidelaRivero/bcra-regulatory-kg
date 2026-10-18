# Material de T4 — vigilancia:1 (30 fichas; B6.1, tanda 1, T4, primer tramo, punto 4)

Sorteo: `vigilancia_1.json` (484cf14e…, 2026-10-18T12:01:47-03:00); material armado a las 2026-10-18T12:03:34-03:00. Sin el estado de E3 ni las marcas de E3.

## 1. `Condicion_condena_con_inhabilitacion_de_cargos_publicos__persona_condenada_con_accesoria_d_7197b7` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1F6::3.1.3` (e0, bloque de lista True; págs. 41):

```
[encabezado | punto D1F6]
DECLARACIÓN JURADA DEL SOCIO RESPONSABLE
[encabezado | punto D1F6::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a continua-
ción:
[encabezado | punto D1F6::3.1]
3.1. Los afectados por las inhabilidades o incompatibilidades establecidas por el artículo 264 de la Ley Nº 19.550, a saber:
[texto propio | punto D1F6::3.1.3]
3.1.3. Los condenados con accesoria de inhabilitación de ejercer cargos públicos; los condenados por hurto, robo, defrauda-
ción, cohecho, emisión de cheques sin fondos y delitos contra la fe pública; los condenados por delitos cometidos en
la constitución, funcionamiento y liquidación de sociedades. En todos los casos hasta después de diez años de cum-
plida la condena.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condena_con_inhabilitacion_de_cargos_publicos__persona_condenada_con_accesoria_d_7197b7` — Condena con inhabilitación de cargos públicos
  - propiedades: {"descripcion": "Persona condenada con accesoria de inhabilitación de ejercer cargos públicos", "umbrales": [{"tramo": "hasta después de diez años de cumplida la condena", "valor": "10", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta", "verificado_en_tabla": true}]}
  - tramo: Los condenados con accesoria de inhabilitación de ejercer cargos públicos
- **Aristas** (2):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_el_socio_responsable_no_puede_ser_persona_condenada_con_inhabilitacion_de_cargos_2400b7` — Inhabilitación de Socio Responsable por condenas
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"rol_fuente": "derivada_de_procedencia"}

## 2. `Condicion_cuando_corresponda_remision_de_informacion__la_remision_de_informacion_a_la_inst_1df00c` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1A4::3.2` (e0, bloque de lista True; págs. 29):

```
[encabezado | punto D1A4]
ANEXO IV
[texto propio | punto D1A4::3.2]
3.2. Verificación, mediante procedimientos de auditoria, del cumplimiento de las nor-
mas del Banco Central de la República Argentina, en materia de prevención del
lavado de dinero proveniente de actividades ilícitas, poniendo especial énfasis
en que la entidad haya generado, almacenado y, cuando correspondiese, cum-
plido con la remisión -en tiempo y forma- a esta Institución de la información es-
tablecida.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_cuando_corresponda_remision_de_informacion__la_remision_de_informacion_a_la_inst_1df00c` — Cuando corresponda remisión de información
  - propiedades: {"descripcion": "La remisión de información a la Institución procede cuando corresponda según las normas aplicables"}
  - tramo: cuando correspondiese
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_la_entidad_debe_haber_generado_almacenado_y_cuando_correspondiese_cumplido_con_l_dd9cd4` — Énfasis en generación y almacenamiento de información
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable

## 3. `Condicion_exposicion_de_causas_de_salvedades_en_notas_a_estados_contables__cuando_las_caus_5e11f9` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1A4::S1` (e0, bloque de lista True; págs. 22, 23, 24):

```
[encabezado | punto D1A4]
ANEXO IV
[chapeau_seccion | punto D1A4::S0]
INFORMES DE LOS AUDITORES EXTERNOS
[chapeau_seccion | punto D1A4::S0]
Como conclusión de la tarea realizada, los auditores externos deberán enviar a las
cajas de crédito los informes que se detallan a continuación:
[texto propio | punto D1A4::S1]
1. Informe sobre los estados contables al cierre del ejercicio, el cual deberá
contener como mínimo lo siguiente:
- Título
- Destinatario
- Identificación completa de los estados contables examinados, de la entidad a
la cual corresponden y de la fecha o período a que se refieren.
- Alcance del trabajo efectuado, el cual deberá realizarse de acuerdo con lo
estipulado en los Anexos II y III.
- Aclaraciones especiales previas al dictamen que permitan interpretar en forma
adecuada la información o remisión, en su caso, a la exposición que de ellas
se haya efectuado mediante nota a los estados contables.
El auditor no debe incluir en este apartado manifestaciones que en realidad
representaren salvedades o excepciones que no reciban el tratamiento
correspondiente en el párrafo del dictamen o de la opinión.
- Dictamen u opinión sobre si los estados contables examinados presentan
razonablemente la situación patrimonial de la entidad a la fecha
correspondiente y los resultados de sus operaciones por el ejercicio terminado
en esa fecha, de conformidad con las normas contables profesionales y las
establecidas por el Banco Central de la República Argentina.
- Su opinión sobre si los estados contables concuerdan con las anotaciones
efectuadas en los registros contables de la entidad y si estos últimos son
llevados de conformidad con las disposiciones legales vigentes y las normas
reglamentarias del Banco Central de la República Argentina.
- Los datos especiales requeridos para cumplir con disposiciones legales, tales
como las del Art. 10 de la Ley Nº 17.250.
- Lugar y fecha de emisión.
- Firma del contador público, con la pertinente aclaración y certificación por el
Consejo Profesional de Ciencias Económicas en el que se encuentre
matriculado. Cuando se trate de sociedades de profesionales inscriptas en los
consejos profesionales, su denominación podrá colocarse debajo de la firma
del contador público que suscriba el dictamen, haciéndose constar su carácter
de socio y consignando si esa firma compromete o no a la citada sociedad.
El dictamen favorable puede ser acotado con salvedades o excepciones,
siempre que se trate de importes o aspectos que, por su significación, no
justifiquen la emisión de un dictamen adverso o una abstención de opinión.
Las salvedades a la opinión principal, o sea sobre la razonabilidad de los
estados contables, pueden hacer referencia a alguna de las siguientes
circunstancias:
- que el auditor discrepa concretamente con cierto tratamiento (de valuación o
exposición) dispensado en los estados contables (salvedad determinada) o
- que el auditor no emite opinión sobre una parte de la información contenida
en los estados contables examinados (salvedad indeterminada).
Se entiende que constituyen salvedades determinadas:
a) diferencia de opinión en materia de valuación, tales como sobre o
subvaluación de activos y/o pasivos, partidas no registradas
contablemente, etc.
b) falta de exposición o exposición inadecuada de ciertos datos en los
estados contables.
Por su parte, se entiende que constituyen salvedades indeterminadas:
a) carencia de elementos de juicio suficientes para formarse una opinión
sobre un rubro o concepto. Por ejemplo: falta de documentación de
respaldo de operaciones efectuadas, deficiencias significativas de
control interno que no le ofrezcan seguridades razonables sobre la
confiabilidad de ciertos datos contables, etc.
b) incertidumbre respecto de ciertos hechos futuros, de cuya realización
depende la razonabilidad de la valuación de un rubro. Es dable
destacar que en estos casos puede no necesariamente haber
discrepancias entre la entidad financiera y el auditor externo, sino que
determinados problemas potenciales deben exponerse en el dictamen,
pues de ocurrir podrían afectar la situación patrimonial y los resultados
de las operaciones de la entidad. Casos de este tipo lo constituyen la
resolución de los juicios pendientes, sumarios en proceso de
sustanciación en la Superintendencia de Entidades Financieras y
Cambiarias, diferencias de interpretación sobre cuestiones impositivas,
dudas sobre la cobrabilidad de préstamos, etc.
Las salvedades deberán fundamentarse adecuadamente, precisando las
cuentas o rubros involucrados, la naturaleza de la excepción y su monto.
Cuando haya imposibilidad de cuantificar razonablemente los montos
correspondientes, el auditor externo deberá explicar los motivos de ello en
su dictamen. La exposición de las causas de las salvedades en notas a
los estados contables de la entidad excusará su repetición en el dictamen,
pero éste deberá indicar clara y expresamente la existencia de la
salvedad y remitirse a las respectivas notas. Independientemente de ello
el auditor en su dictamen hará referencia a las notas y determinará cuál
es la influencia que en su opinión o dictamen tienen las salvedades
correspondientes.
Cuando corresponda formular salvedad por falta de uniformidad, con
respecto a las pautas o a los criterios contables utilizados en el ejercicio
anterior, se incluirá un párrafo específico que describa con claridad el
cambio, las causas que lo originaron, sus efectos cuantitativos y la
opinión que merezca para el auditor externo la modificación realizada,
excepto que la situación haya sido expuesta en nota a los estados
contables.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_exposicion_de_causas_de_salvedades_en_notas_a_estados_contables__cuando_las_caus_5e11f9` — Exposición de causas de salvedades en notas a estados contables
  - propiedades: {"descripcion": "Cuando las causas de las salvedades se exponen en notas a los estados contables, se excusa su repetición en el dictamen, pero este debe indicar clara y expresamente la existencia de la salvedad y remitirse a las respectivas notas"}
  - tramo: La exposición de las causas de las salvedades en notas a los estados contables de la entidad excusará su repetición en el dictamen, pero éste deberá indicar clara y expresamente la existencia de la salvedad y remitirse a las respectivas notas
- **Aristas** (1):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable

## 4. `Condicion_condena_por_delitos_en_constitucion_funcionamiento_y_liquidacion_de_sociedades___c732a3` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1F6::3.1.3` (e0, bloque de lista True; págs. 41):

```
[encabezado | punto D1F6]
DECLARACIÓN JURADA DEL SOCIO RESPONSABLE
[encabezado | punto D1F6::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a continua-
ción:
[encabezado | punto D1F6::3.1]
3.1. Los afectados por las inhabilidades o incompatibilidades establecidas por el artículo 264 de la Ley Nº 19.550, a saber:
[texto propio | punto D1F6::3.1.3]
3.1.3. Los condenados con accesoria de inhabilitación de ejercer cargos públicos; los condenados por hurto, robo, defrauda-
ción, cohecho, emisión de cheques sin fondos y delitos contra la fe pública; los condenados por delitos cometidos en
la constitución, funcionamiento y liquidación de sociedades. En todos los casos hasta después de diez años de cum-
plida la condena.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condena_por_delitos_en_constitucion_funcionamiento_y_liquidacion_de_sociedades___c732a3` — Condena por delitos en constitución, funcionamiento y liquidación de sociedades
  - propiedades: {"descripcion": "Persona condenada por delitos cometidos en la constitución, funcionamiento y liquidación de sociedades", "umbrales": [{"tramo": "hasta después de diez años de cumplida la condena", "valor": "10", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta", "verificado_en_tabla": true}]}
  - tramo: los condenados por delitos cometidos en la constitución, funcionamiento y liquidación de sociedades
- **Aristas** (2):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_el_socio_responsable_no_puede_ser_persona_condenada_con_inhabilitacion_de_cargos_2400b7` — Inhabilitación de Socio Responsable por condenas
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"rol_fuente": "derivada_de_procedencia"}

## 5. `Condicion_condena_por_hurto_robo_defraudacion_cohecho_cheques_sin_fondos__persona_condenad_2e9c8c` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1F6::3.1.3` (e0, bloque de lista True; págs. 41):

```
[encabezado | punto D1F6]
DECLARACIÓN JURADA DEL SOCIO RESPONSABLE
[encabezado | punto D1F6::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a continua-
ción:
[encabezado | punto D1F6::3.1]
3.1. Los afectados por las inhabilidades o incompatibilidades establecidas por el artículo 264 de la Ley Nº 19.550, a saber:
[texto propio | punto D1F6::3.1.3]
3.1.3. Los condenados con accesoria de inhabilitación de ejercer cargos públicos; los condenados por hurto, robo, defrauda-
ción, cohecho, emisión de cheques sin fondos y delitos contra la fe pública; los condenados por delitos cometidos en
la constitución, funcionamiento y liquidación de sociedades. En todos los casos hasta después de diez años de cum-
plida la condena.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condena_por_hurto_robo_defraudacion_cohecho_cheques_sin_fondos__persona_condenad_2e9c8c` — Condena por hurto, robo, defraudación, cohecho, cheques sin fondos
  - propiedades: {"descripcion": "Persona condenada por hurto, robo, defraudación, cohecho o emisión de cheques sin fondos", "umbrales": [{"tramo": "hasta después de diez años de cumplida la condena", "valor": "10", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta", "verificado_en_tabla": true}]}
  - tramo: los condenados por hurto, robo, defraudación, cohecho, emisión de cheques sin fondos
- **Aristas** (2):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_el_socio_responsable_no_puede_ser_persona_condenada_con_inhabilitacion_de_cargos_2400b7` — Inhabilitación de Socio Responsable por condenas
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"rol_fuente": "derivada_de_procedencia"}

## 6. `Condicion_desempeno_relacionado_con_objeto_de_la_sociedad__la_inhabilidad_aplica_cuando_el_c3e441` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1F2::3.1.4` (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[encabezado | punto D1F2::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a conti-
nuación:
[encabezado | punto D1F2::3.1]
3.1 Los afectados por las inhabilidades o incompatibilidades establecidas por el artículo 264 de la Ley Nº 19.550, a saber:
[texto propio | punto D1F2::3.1.4]
3.1.4 Los funcionarios de la administración pública cuyo desempeño se relacione con el objeto de la sociedad, hasta dos
años después del cese de sus funciones.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_desempeno_relacionado_con_objeto_de_la_sociedad__la_inhabilidad_aplica_cuando_el_c3e441` — Desempeño relacionado con objeto de la sociedad
  - propiedades: {"descripcion": "La inhabilidad aplica cuando el desempeño del funcionario se relaciona con el objeto de la sociedad."}
  - tramo: cuyo desempeño se relacione con el objeto de la sociedad
- **Aristas** (2):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_los_funcionarios_de_la_administracion_publica_cuyo_desempeno_se_relacione_con_el_51154e` — Inhabilidad funcionarios públicos — hasta 2 años post-cese
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable

## 7. `Condicion_vigencia_a_fecha_de_firma_del_dictamen__la_exclusion_debe_estar_vigente_a_la_fec_6a7bce` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1A1::2.1.9` (e0, bloque de lista True; págs. 4):

```
[encabezado | punto D1A1]
ANEXO I
[encabezado | punto D1A1::S2]
2. Condiciones para el ejercicio de la función de auditor externo, inscripción y
permanencia en el "Registro de auditores":
[intro | punto D1A1::2.1]
2.1. Podrán prestar tales servicios a nombre propio o a través de estudios profesionales,
los Contadores Públicos Nacionales que:
[texto propio | punto D1A1::2.1.9]
2.1.9. no figuren en la nómina prevista en el punto 4.1. -cuarto párrafo-, o en su
eventual actualización -punto 4.3., tercer párrafo-, de los estudios contables
que se encuentren expresamente excluidos del “Registro de Asociaciones de
Profesionales Universitarios”, por aplicación de las disposiciones del punto
4.2., vigente a la fecha de la firma del dictamen y/o informe especial, que
diera lugar a la sanción pecuniaria, y/o a la fecha del vencimiento del plazo
para efectivizarla y/o, en su caso, a la fecha del incumplimiento que determine
la caducidad del plan de facilidades para su pago.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_vigencia_a_fecha_de_firma_del_dictamen__la_exclusion_debe_estar_vigente_a_la_fec_6a7bce` — Vigencia a fecha de firma del dictamen
  - propiedades: {"descripcion": "La exclusión debe estar vigente a la fecha de la firma del dictamen y/o informe especial que dio lugar a la sanción pecuniaria."}
  - tramo: vigente a la fecha de la firma del dictamen y/o informe especial
- **Aristas** (1):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable

## 8. `Condicion_condena_con_inhabilitacion_de_cargos_publicos__haber_sido_condenado_con_accesori_05fe48` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1F2::3.1.3` (e0, bloque de lista True; págs. 32):

```
[encabezado | punto D1F2]
DECLARACIÓN JURADA DE AUDITORES EXTERNOS
[encabezado | punto D1F2::S3]
3. No me alcanza ninguna de las siguientes inhabilidades previstas por el artículo 10 de la Ley Nº 21.526, según se detalla a conti-
nuación:
[encabezado | punto D1F2::3.1]
3.1 Los afectados por las inhabilidades o incompatibilidades establecidas por el artículo 264 de la Ley Nº 19.550, a saber:
[texto propio | punto D1F2::3.1.3]
3.1.3 Los condenados con accesoria de inhabilitación de ejercer cargos públicos; los condenados por hurto, robo, defrau-
dación, cohecho, emisión de cheques sin fondos y delitos contra la fe pública; los condenados por delitos cometidos
en la constitución, funcionamiento y liquidación de sociedades. En todos los casos hasta después de diez años de
cumplida la condena.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condena_con_inhabilitacion_de_cargos_publicos__haber_sido_condenado_con_accesori_05fe48` — Condena con inhabilitación de cargos públicos
  - propiedades: {"descripcion": "Haber sido condenado con accesoria de inhabilitación de ejercer cargos públicos", "umbrales": [{"tramo": "hasta después de diez años de cumplida la condena", "valor": "10", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "compuesta:hasta", "origen": "e1", "tramo_verificado": "exacta", "verificado_en_tabla": true}]}
  - tramo: Los condenados con accesoria de inhabilitación de ejercer cargos públicos
- **Aristas** (2):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_el_auditor_externo_no_debe_estar_afectado_por_inhabilidades_o_incompatibilidades_811ac0` — Inhabilitación por condenas — artículo 264 Ley 19.550
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable · {"rol_fuente": "derivada_de_procedencia"}

## 9. `Condicion_confianza_control_interno_procedimientos_auditoria__el_auditor_puede_depositar_c_488410` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1A4::3.1.1` (e0, bloque de lista True; págs. 26, 27, 28, 29):

```
[encabezado | punto D1A4]
ANEXO IV
[encabezado | punto D1A4::3.1]
3.1. Verificación de los deudores de las Cajas de Crédito
[texto propio | punto D1A4::3.1.1]
3.1.1. El auditor deberá emitir una opinión acerca de la razonabilidad de las
previsiones por riesgo de incobrabilidad de los clientes, efectuando
como mínimo los siguientes procedimientos:
A - Reproceso de la clasificación de los prestatarios
Reprocesar la clasificación de los prestatarios, sobre la base de la fecha
de primer vencimiento impago que arrojan los sistemas de la caja de
crédito. Esta prueba deberá efectuarse para la totalidad de los
prestatarios de la caja de crédito.
B - Refinanciaciones
Detección de las refinanciaciones otorgadas por la caja de crédito. A tal
efecto, entre otros procedimientos, deberá realizarse una comparación
de bases de datos sobre las siguientes pautas:
- tomar la totalidad de los prestatarios a una fecha determinada y
compararla con otra de un período anterior (la diferencia entre
ambas debe ser de por lo menos 6 meses y no superior a 9 meses),
- segmentar a los prestatarios del acápite anterior en por lo menos
tres universos homogéneos:
1) los que mejoran su clasificación,
2) los que mantienen constante o creciente su saldo de deuda, sin
que se registre un empeoramiento en su clasificación y,
3) los que han disminuido su deuda o empeorado su situación.
En aquellos casos en los que ciertos prestatarios no se encuentren
incorporados en las bases de datos, sino que por ejemplo son llevados
en planillas de cálculo o en sistemas externos, el auditor deberá
obtener dicha información para efectuar la comparación pertinente.
Además, el auditor deberá extremar los recaudos a efectos de verificar
que los procedimientos de traspaso de información de planillas o
sistemas externos a la base de datos utilizada para la comparación no
permitan que se produzcan corrimientos de la morosidad ni una
asignación de clasificación al deudor distinta de la peor.
C - Segmentación de deudores
Segmentar los prestatarios sobre la base de universos homogéneos, a los
fines de la determinación de muestras destinadas a la verificación con do-
cumentación de respaldo de la correcta imputación de la fecha de último
pago y la fecha de primer vencimiento impago que arrojan los sistemas de
la caja de crédito. A tal efecto pueden utilizarse, entre otros, los universos
homogéneos definidos para el punto de refinanciaciones, o los que surjan
de agrupar clasificaciones similares, excluyendo –siempre- los prestata-
rios totalmente previsionados.
D - Tasaciones y Garantías
Verificar la existencia y tasación de las garantías preferidas recibidas,
debiendo segmentarse los prestatarios al elegir la muestra en al menos
dos universos, por una parte aquellos clasificados en situación 1 y 2, y
por otra parte aquellos clasificados en situación 3, 4 y 5. Se podrá
considerar como valor de tasación el valor por el que esté asegurado el
bien recibido en garantía. En el caso de universos atomizados la muestra
deberá ser elegida con criterios estadísticos o de aproximación
estadística.
E - Métodos estadísticos de selección
Aplicar, en aquellos casos en que se trate de universos atomizados, mé-
todos estadísticos de selección que permitan proyectar las conclusiones
que se obtengan de la muestra analizada al resto del universo no analiza-
do. Para seleccionar la muestra mencionada deberá existir un adecuado
sustento del grado de confianza, error tolerable y error esperado y, ade-
más, una estrecha relación entre ellos y la confianza depositada en el sis-
tema de control interno. Adicionalmente, deberá expresarse el criterio de
selección de los casos objeto de revisión, debiendo aplicarse metodologí-
as que permitan que cualquier componente del universo tenga la misma
posibilidad de ser elegido.
Cabe señalar que para que el auditor pueda depositar confianza en el
control interno, deberá haber efectuado todos los procedimientos previstos
en tal sentidos en las normas mínimas sobre auditorías externas, los cua-
les no podrán tener una antigüedad mayor a un año.
F - Central de Deudores
Comparar, para la totalidad de los prestatarios, la clasificación asignada
por la caja de crédito con la que surge de la Central de Deudores, como
así también la de deudores morosos en entidades liquidadas.
G – Saldos sin asignación
Verificar que no existan sin asignación específica a los prestatarios de la
caja de crédito.
H – Previsiones proyectadas
Proyectar los defectos de previsión que surjan de la cartera analizada.
I - Aplicativo de prestatarios
Evaluar el sistema aplicativo de prestatarios y sus interfases con el conta-
ble.
J - Consolidación de deuda
Verificar la existencia de un adecuado sistema de consolidación de deuda
por prestatario.
K - Análisis individual de los 50 principales prestatarios
Independientemente de lo expresado en el primer párrafo, el auditor ex-
terno deberá emitir una opinión expresa deudor por deudor respecto de
las eventuales diferencias entre los datos suministrados por la caja de
crédito y los obtenidos de la documentación obrante u otros elementos
que estime corresponder vinculados con los apartados A y B –excepto
punto 1- de la información sobre “Deudores del Sistema Financiero” para
cada uno de los 50 principales prestatarios de la caja de crédito.
El auditor deberá analizar a los prestatarios en forma correlativa, comen-
zando por el primer prestatario en función a su deuda, no pudiendo dejar
de analizar ninguno hasta llegar al alcance fijado.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_confianza_control_interno_procedimientos_auditoria__el_auditor_puede_depositar_c_488410` — Confianza control interno procedimientos auditoria
  - propiedades: {"descripcion": "El auditor puede depositar confianza en el control interno si ha efectuado todos los procedimientos previstos en normas mínimas sobre auditorías externas con antigüedad no mayor a un año", "umbrales": [{"tramo": "no podrán tener una antigüedad mayor a un año", "valor": "1", "unidad": "anios", "comparacion": "maximo_inclusivo", "regla_comparacion": "negacion:mayor", "origen": "e1", "tramo_verificado": "exacta"}]}
  - tramo: para que el auditor pueda depositar confianza en el control interno, deberá haber efectuado todos los procedimientos previstos en tal sentidos en las normas mínimas sobre auditorías externas, los cuales no podrán tener una antigüedad mayor a un año.
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_aplicar_metodos_estadisticos_de_seleccion_en_universos_atomizados_que_permitan_p_13b79b` — Aplicación métodos estadísticos universos atomizados
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable

## 10. `Condicion_vigencia_a_fecha_de_vencimiento_de_plazo_de_sancion__la_exclusion_debe_estar_vig_965e2f` — RI:sin_raiz · vigilancia:1

Texto que vio E3 de `ri_ccna::D1A1::2.1.9` (e0, bloque de lista True; págs. 4):

```
[encabezado | punto D1A1]
ANEXO I
[encabezado | punto D1A1::S2]
2. Condiciones para el ejercicio de la función de auditor externo, inscripción y
permanencia en el "Registro de auditores":
[intro | punto D1A1::2.1]
2.1. Podrán prestar tales servicios a nombre propio o a través de estudios profesionales,
los Contadores Públicos Nacionales que:
[texto propio | punto D1A1::2.1.9]
2.1.9. no figuren en la nómina prevista en el punto 4.1. -cuarto párrafo-, o en su
eventual actualización -punto 4.3., tercer párrafo-, de los estudios contables
que se encuentren expresamente excluidos del “Registro de Asociaciones de
Profesionales Universitarios”, por aplicación de las disposiciones del punto
4.2., vigente a la fecha de la firma del dictamen y/o informe especial, que
diera lugar a la sanción pecuniaria, y/o a la fecha del vencimiento del plazo
para efectivizarla y/o, en su caso, a la fecha del incumplimiento que determine
la caducidad del plan de facilidades para su pago.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_vigencia_a_fecha_de_vencimiento_de_plazo_de_sancion__la_exclusion_debe_estar_vig_965e2f` — Vigencia a fecha de vencimiento de plazo de sanción
  - propiedades: {"descripcion": "La exclusión debe estar vigente a la fecha del vencimiento del plazo para efectivizar la sanción pecuniaria."}
  - tramo: a la fecha del vencimiento del plazo para efectivizarla
- **Aristas** (1):
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_ccna_pdf` — Régimen de Información Contable

## 11. `Condicion_disponibilidad_de_datos_del_tercer_mes_anterior__la_informacion_utilizada_debe_c_c7619a` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_rml::Sbloque4` (e0, bloque de lista True; págs. 30):

```
[encabezado | punto S2]
Sección 2. Metodología de cálculo del aporte al Fondo de Garantía de los Depósitos
[chapeau_seccion | punto S2]
Base de cálculo * 0,015% * Ic * 1000
[chapeau_seccion | punto S2]
donde:
Base de cálculo = 101078/M + 101079/M + 101081/M + 101082/M + 10140X/M a 10144X/M +
10147X/001 + 101470/M + 101460/M + 10146X/001 + 101490/001 + 10160X/001 + 10161X/001
+ 10162X/001 + 10163X/001 + 10164X/001 + 101650/001 + 10171X/001 + 10175X/001 +
102010/M a 102055/M + 102190/001 + 102200/001 + 102300/001 + 102350/010 + 102360/001 +
801000/M
La información será la del segundo mes anterior al del ingreso del aporte.
Los importes en dólares estadounidenses se convertirán a pesos utilizando el tipo de cambio de
referencia correspondiente al último día hábil del mes anterior al que corresponda la liquidación
del aporte.
Ic = [ (Ipr/f + Iar/a + 2 * Icamels) / 4] - Irpc/Kmin
[chapeau_seccion | punto S2]
La calificación asignada se considerará para el cálculo del aporte exigible el tercer mes si-
guiente al de notificación.
En tanto no se disponga de la calificación de la SEFyC (“CAMELS”) el cálculo del índice de
corrección surgirá de la siguiente expresión: Ic = ((Ipr/f + Iar/a)/2) - Irpc/Kmin
[chapeau_seccion | punto S2]
Ipr/f (*) = [(Previsiones mínimas / Financiaciones y Garantías) / 0,04] ** 1,2
[chapeau_seccion | punto S2]
Previsiones mínimas: se considerarán las determinadas de acuerdo con las normas so-
bre previsiones mínimas por riesgo de incobrabilidad, sobre los conceptos informados
en la Sección B, punto 2. del Régimen Informativo de Deudores del Sistema Financiero.
Financiaciones y garantías: la correspondiente información se obtendrá de la Sección B,
punto 2. del Régimen Informativo de Deudores del Sistema Financiero.
(El valor del índice estará acotado entre 1 y 2,5)
[chapeau_seccion | punto S2]
Iar/a (*) = {[APRc / (A + (PFB x CCF))] / 0,70} ** 1,3
[chapeau_seccion | punto S2]
APRc = ∑Códigos 11000000 a 12800000 (excepto 11100000) + 12550000 + [∑Código
13X00000 + Código 14000000 + Código 86300000] * 12,5 + 15000000.
Los importes de las mencionadas partidas (detalladas en Sección 3. del régimen de
Exigencia e Integración de capitales mínimos) se considerarán por su valor ponderado.
A = Σ Códigos 11000000 a 12500000, 12600000 a 12800000 (excepto 11100000,
1221000/CCF, 1222000/CCF y 12300000) del régimen informativo sobre Capitales mí-
nimos (Importes sin ponderar).
[chapeau_seccion | punto S2]
(*) Los importes considerados para el cálculo de las relaciones corresponderán al tercer mes anterior a la fecha de
vencimiento de los aportes.
[chapeau_seccion | punto S2]
PFB x CCF = Códigos 1221000/CCF y 1222000/CCF (importes multiplicados por el Factor
de Con-versión Crediticia).
(El valor del índice estará acotado entre 1 y 2)
[chapeau_seccion | punto S2]
Irpc / Kmin = (Integración de capitales mínimos + Previsiones por riesgo de incobrabilidad consti-
tui-das en exceso sobre los mínimos establecidos) / Exigencia de capitales mínimos (por riesgo de
crédito, de mercado para las posiciones al último día del mes y operacional).
(El resultado del indicador se tomará de la tabla consignada en el punto 7.1. de las normas sobre
“Aplicación del sistema de seguro de garantía de depósitos”).
Para obtener la relación antes mencionada, deberán considerarse los siguientes conceptos:
[chapeau_seccion | punto S2]
Régimen Informativo de Capitales Mínimos:
[texto propio | punto Sbloque4]
Irpc
· Código 70200000: tercer mes anterior a la fecha de vencimiento de los aportes.
más:
· Previsiones constituidas en exceso de los mínimos establecidos en las normas sobre “Cla-
sificación de deudores”, determinada según el siguiente cálculo:
· Cuentas del balance de saldos:
121135, 125135, 126135, 131601 / 901, 132301, 135601 / 901, 136301, 141301,
142301, 145301, 146301, 151312, 155312, 171302, 175302, 176302, 340018.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_disponibilidad_de_datos_del_tercer_mes_anterior__la_informacion_utilizada_debe_c_c7619a` — Disponibilidad de datos del tercer mes anterior
  - propiedades: {"descripcion": "La información utilizada debe corresponder al tercer mes anterior a la fecha de vencimiento de los aportes.", "umbrales": [{"tramo": "tercer mes anterior a la fecha de vencimiento de los aportes", "comparacion": "no_determinada", "regla_comparacion": "limite_relativo:sin_marcador", "origen": "e1", "tramo_verificado": "exacta"}]}
  - tramo: Código 70200000: tercer mes anterior a la fecha de vencimiento de los aportes.
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_deber_de_considerar_para_obtener_la_relacion_irpc_kmin_los_conceptos_del_regimen_680289` — Considerar conceptos del Régimen Informativo de Capitales Mínimos
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual

## 12. `Condicion_plazo_fijo_en_moneda_extranjera_aplicar_estructura_del_mes_anterior__cuando_se_t_b008f3` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_rml::1.2.3` (e0, bloque de lista True; págs. 3, 4, 5, 6):

```
[encabezado | punto S1]
Sección 1. Efectivo mínimo
[encabezado | punto 1.2]
1.2. Exigencia
[texto propio | punto 1.2.3]
1.2.3. Conceptos comprendidos
El código 100000/M incluirá los depósitos y obligaciones por intermediación financiera a
la vista y a plazo en pesos y moneda extranjera, de acuerdo con los términos de la Sec-
ción 1. de las normas sobre “Efectivo mínimo”.
El código 300000/TP incluirá los depósitos a plazo fijo de títulos públicos nacionales o
instrumentos de regulación monetaria del BCRA teniendo en cuenta lo establecido en
las normas citadas.
Se informará un subcódigo por cada moneda o instrumento de deuda en que se en-
cuentren denominadas las obligaciones considerando las disposiciones del punto 1.1.
Los depósitos y obligaciones a plazo se informarán teniendo en cuenta sus plazos resi-
duales.
Plazos residuales
Los depósitos y obligaciones a plazo se clasificarán según los tramos de plazos residua-
les establecidos. Para ello, se tendrá en cuenta lo siguiente:
[TABLA ri_rml::tabla000 | página 3 | e0_tablas | posicional]
Fila 1: col1 = Pesos | col2 = Moneda extranjera
Fila 2: col1 = x = 1 a 5, donde: | col2 = x = 1 a 6, donde:
Fila 3: col1 = 1= Hasta 29 días | col2 = 1= Hasta 29 días
Fila 4: col1 = 2= 30 - 59 días | col2 = 2= 30 - 59 días
Fila 5: col1 = 3= 60 - 89 días | col2 = 3= 60 - 89 días
Fila 6: col1 = 4= 90 - 179 días | col2 = 4= 90 - 179 días
Fila 7: col1 = 5= 180 días o más | col2 = 5= 180 a 365 días
Fila 8: col2 = 6= más de 365 días.
[FIN TABLA ri_rml::tabla000]
Dichos plazos se calcularán computando la cantidad de días que restan hasta el venci-
miento de las obligaciones, contados desde cada uno de los días del mes, determinan-
do finalmente el promedio de las aludidas obligaciones así desagregadas.
Cuando se trate de plazo fijos en moneda extranjera (partida 10140X/M) se aplicará la
estructura de plazos residuales del mes anterior (n - 1).
En consecuencia, se efectuarán los siguientes cálculos:
Se sumarán los tramos de plazos informados en la posición del mes anterior (n-1) y se
determinarán los porcentajes de cada tramo sobre el total.
Se sumarán los tramos de plazos informados en la posición del mes bajo informe (n) y
se le aplicarán los porcentajes determinados en el mes anterior (n-1).
Dicho procedimiento se aplicará considerando en forma conjunta los depósitos a plazo
fijo (códigos 10140X/M, donde M = moneda extranjera).
Para los plazos fijos y para las restantes operaciones a plazo en pesos, se considerarán
para el cálculo de la exigencia del mes bajo informe, los tramos de plazos y promedios
informados en el periodo anterior y las tasas del periodo bajo informe.
Código 10141X/M
En el caso de extensión automática de plazo, se considerará en forma constante el plazo ex-
tendido (180 días o más, según lo pactado). Si el cliente opta por la revocación de la exten-
sión, se computará el plazo remanente hasta el vencimiento.
Código 101490/001
Se incluirán las inversiones a plazo instrumentadas en certificados nominativos intransferibles,
en pesos, correspondientes a titulares del sector público que cuenten con el derecho a ejercer
la opción de cancelación anticipada en un plazo inferior a 30 días contados desde su constitu-
ción.
Código 10145X/M
Se consignarán las obligaciones por líneas financieras del exterior instrumentadas me-
diante depósitos a plazo o adquisición de títulos valores de deuda de personas vincula-
das -punto 1.2.2. del TO sobre Grandes Exposiciones al Riesgo de Crédito- a las cuales
les corresponde la exigencia prevista en el punto 1.3.5. de las normas sobre “Efectivo
mínimo”.
Código 10171X/001
Se incluirá el importe de los depósitos reprogramados “CEDROS” y el correspondiente CER
devengado. Los plazos residuales de cada servicio de amortización se determinarán en forma
independiente.
Código 10180X/M
Se incluirán Títulos Valores de Deuda, comprendiendo las obligaciones negociables y las obli-
gaciones reestructuradas, a excepción de los saldos que corresponda imputar en la partida
10166X/001.
Los plazos residuales de las obligaciones de pago en cuotas de capital se computarán en for-
ma independiente para cada servicio de amortización con vencimiento dentro del año, contado
desde cada uno de los días de la posición al que corresponde el efectivo mínimo.
Código 10190X/001
Se informarán las cauciones bursátiles tomadoras -pasivas- en pesos, de acuerdo con lo previs-
to en el punto 1.3.13. de las normas sobre “Efectivo mínimo”.
Código 10206X/M
Se informará las obligaciones por líneas financieras del exterior no instrumentadas me-
diante depósitos a plazo o adquisición de títulos valores de deuda, de personas vincula-
das, -punto 1.2.2. del TO sobre Grandes Exposiciones al Riesgo de Crédito- a las cuales
les corresponde la exigencia prevista en el punto 1.3.6. de las normas sobre “Efectivo
mínimo”.
Las obligaciones originadas en líneas financieras del exterior que reúnan los requisitos
previstos en el punto 1.3.6., formalizadas hasta el 5/2 se informarán en la partida
102062/M, mientras que las formalizadas a partir del 6/2, se informarán en las partidas
102061/M y/ó 102062/M, según el plazo que corresponda.
Código 102100/M
Se consignarán los saldos sin utilizar de adelantos en cuenta corriente que correspondan a
acuerdos formalizados que no contengan cláusulas que habiliten a la entidad a disponer discre-
cional y unilateralmente la anulación de la posibilidad de uso de dichos márgenes.
Código 102150/M
Los bancos comerciales informarán el total de depósitos a la orden de entidades financieras no
bancarias.
Código 102090/010
Se incluirán las obligaciones a la vista por transferencias del exterior pendientes de liquidación
que excedan las 72 hs. hábiles de la fecha de su acreditación.
Códigos 101500/M, 102160/M y 300700/TP
Se informarán las obligaciones respecto de las cuales se hayan dispuesto aumentos puntuales
de exigencia por concentración de pasivos. Para su cómputo debe aplicarse la siguiente metodo-
logía:
a) En los códigos previstos para los depósitos (a la vista y a plazo) y otras obligaciones se regis-
trará el promedio mensual de saldos diarios incluyendo los depósitos que verifiquen una con-
centración excesiva de pasivos (en titulares y/o plazos), sobre los que se calculará la tasa de
efectivo mínimo normal para el período considerado.
b) En los códigos 101500/M, 102160/M y 300700/TP se consignará el promedio mensual de sal-
dos diarios de los depósitos y otras obligaciones que verifiquen alguno de los factores des-
criptos en el punto 1.6. de las normas sobre “Efectivo mínimo”. La exigencia a aplicar será la
que resulte de la diferencia entre la determinada para estas obligaciones y la normal calcula-
da según el apartado a). La entidad informará esas partidas con la exigencia incremental ya
calculada, con lo cual se considerará de esa manera para el cálculo de la exigencia total del
período.
Códigos 10160X/001 a 101650/001
- Códigos 10160X/001 y 10163X/001: se consignarán los importes correspondientes a las im-
posiciones en “UVA” y “UVI”, según corresponda, expresados en pesos en función del valor
de esas unidades calculado conforme lo establecido en el punto 1.9. de las normas sobre
“Depósitos e inversiones a plazo”.
- Código 10161X/001: inversiones a plazo de “UVA” para las modalidades previstas en los pun-
tos 2.2. a 2.5. de las normas sobre “Depósitos e inversiones a plazo”;
- Códigos 10162X/001 y 10164X/001: cuentas de ahorro en “UVA” y “UVI”, respectivamente,
según lo previsto en los puntos 2.6. y 2.7. de las citadas normas;
- Código 101650/001: depósitos a plazo fijo e inversiones a nombre de menores de edad por
fondos que reciban a título gratuito.
Código 10166X/001
Se informarán las colocaciones de títulos de deuda (incluidas las obligaciones negociables) cu-
yos instrumentos se encuentren denominados en Unidades de Vivienda actualizables por “ICC” -
Ley 27.271 (“UVI”) o en Unidades de Valor Adquisitivo actualizables por “CER” - Ley 25.827
(“UVA”).
Código 102400/M
Se informará el importe del defecto de aplicación de la capacidad prestable correspondiente a
los depósitos en moneda extranjera, determinado en el código 400/M.
Códigos 10120X/M, 11010X/M y 110500/M
Identificarán los depósitos a plazo fijo de títulos privados y públicos (excepto nacionales) y sus
saldos inmovilizados según lo previsto en las normas sobre “Efectivo mínimo”. Se admitirá su in-
tegración total o parcial con títulos públicos nacionales con cotización normal y habitual por im-
portes significativos en mercados del país; dicha aplicación se informará en el código 210100/TP
-cuando se trate de especies en pesos, de acuerdo con el procedimiento descripto en el punto
1.3. “Integración” de las presentes normas- o 210200/TP -cuando se trate de especies en dólares
estadounidenses-.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_plazo_fijo_en_moneda_extranjera_aplicar_estructura_del_mes_anterior__cuando_se_t_b008f3` — Plazo fijo en moneda extranjera — aplicar estructura del mes anterior
  - propiedades: {"descripcion": "Cuando se trate de plazo fijos en moneda extranjera (partida 10140X/M), aplicar la estructura de plazos residuales del mes anterior (n-1)."}
  - tramo: Cuando se trate de plazo fijos en moneda extranjera (partida 10140X/M) se aplicará la estructura de plazos residuales del mes anterior (n - 1).
- **Aristas** (39):
  - (remision_derivada) ←remite_a— Condicion `Condicion_codigo_tp_corresponda_a_especie_en_dolares_estadounidenses__condicion_que_requie_ffeaea` — Código TP corresponda a especie en dólares estadounidenses · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_codigo_tp_corresponda_a_especie_en_pesos__condicion_que_requiere_que_el_codigo_t_02e2be` — Código TP corresponda a especie en pesos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_concurrencia_codigos_10120x_m_11010x_m_110500_m__condicion_que_requiere_la_concu_f70c2a` — Concurrencia códigos 10120X/M, 11010X/M, 110500/M · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_depositos_spnf_1_del_total_modelo_informacion__condicion_para_que_las_entidades__0ecc86` — Depósitos SPNF ≥ 1% del total — modelo información · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_01_11_a_08_11_lineas_financieras_exterior__periodo_temporal_para_el_cual_a1574b` — Período 01/11 a 08/11 — líneas financieras exterior · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_09_11_a_30_11_lineas_financieras_exterior__periodo_temporal_para_el_cual_6912f3` — Período 09/11 a 30/11 — líneas financieras exterior · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_19_09_a_30_09_exigencia_minima_diaria__periodo_temporal_para_el_cual_se__84d2b5` — Período 19/09 a 30/09 — exigencia mínima diaria · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual
  - (remision_derivada) ←remite_a— Excepcion `Excepcion_las_entidades_que_sean_sucursales_o_subsidiarias_de_entidades_g_sib_quedan_excep_6dddd1` — Excepción sucursales/subsidiarias G-SIB — enero/2019 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_durante_septiembre_y_meses_subsiguientes_se_considerara_el_incremento_de_exigenc_3a24b5` — Considerar incremento exigencia — conceptos en pesos 31/08 vs 01/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_durante_septiembre_y_meses_subsiguientes_se_considerara_el_incremento_de_exigenc_e4cd27` — Considerar incremento exigencia — conceptos en pesos 18/09 vs 19/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_en_el_codigo_903200_001_exigencia_del_mes_sobre_depositos_y_obligaciones_a_plazo_f423e0` — Incluir partidas en código 903200/001 — depósitos y obligaciones a plazo · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_en_el_codigo_903200_m_se_deberan_incluir_las_partidas_101450_m_y_10145x_m_corres_f0cc79` — Incluir partidas 101450/M y 10145X/M — código 903200/M · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_las_entidades_deberan_considerar_los_numerales_del_periodo_01_09_a_18_09_dividid_64e2ba` — Considerar numerales divididos por 30 — período 01/09 a 18/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_las_entidades_que_cumplan_la_condicion_de_depositos_spnf_deberan_computar_los_nu_8d823a` — Considerar numerales divididos por 30 — período 19/09 a 30/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_las_partidas_informadas_deberan_mantener_las_correlaciones_con_cuentas_de_balanc_17494b` — Mantener correlaciones con cuentas de balance · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_para_determinar_la_estructura_de_plazos_residuales_de_depositos_a_plazo_fijo_de__034b95` — Considerar conceptos informados en agosto/18 — plazos residuales · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_para_el_calculo_de_la_posicion_bimestral_se_debera_considerar_el_promedio_result_5da448` — Calcular promedio — suma numerales posiciones mensuales · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_para_el_calculo_del_aporte_al_fondo_de_garantia_de_los_depositos_se_deberan_cons_3e6ae1` — Considerar códigos equivalentes — Aporte Fondo de Garantía · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_calculo_exigencia_promedio_grupo_a__ri_rml_sbloque14_10d0da` — Cálculo exigencia promedio — Grupo A · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_calculo_posicion_001_por_moneda__ri_rml_1_9_2_1934f9` — Cálculo Posición/001 por moneda · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_calculo_posicion_m_por_moneda_extranjera__ri_rml_1_9_2_31400e` — Cálculo Posición/M por moneda extranjera · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_calculo_posicion_tpnyrm_tp__ri_rml_1_9_2_94d5bd` — Cálculo Posición (TPNyRM)/TP · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_exigencia_minima_diaria_periodo_01_09_a_18_09__ri_rml_sbloque14_b04530` — Exigencia mínima diaria — período 01/09 a 18/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_exigencia_minima_diaria_periodo_19_09_a_30_09__ri_rml_sbloque14_a431d1` — Exigencia mínima diaria — período 19/09 a 30/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_exigencia_minima_diaria_sobre_depositos_y_obligaciones_a_plazo_periodo_01_09_a_1_88934d` — Exigencia mínima diaria sobre depósitos y obligaciones a plazo — período 01/09 a 18/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_exigencia_minima_diaria_sobre_depositos_y_obligaciones_a_plazo_periodo_19_09_a_3_e559c3` — Exigencia mínima diaria sobre depósitos y obligaciones a plazo — período 19/09 a 30/09 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_posicion_promedio_lineas_financieras_exterior_noviembre_18__ri_rml_sbloque14_ce5a6b` — Posición promedio — líneas financieras exterior noviembre/18 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_posicion_unificada_bimestral_efectivo_minimo_moneda_extranjera__ri_rml_sbloque14_385db1` — Posición unificada bimestral — efectivo mínimo moneda extranjera · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Potestad `Potestad_autorizacion_modalidades_integracion_grupo_a_a_partir_febrero_2019__a_partir_de__7237a2` — Autorización modalidades integración Grupo A — a partir febrero/2019 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Potestad `Potestad_facultad_informar_codigo_210200_tp__facultad_de_informar_el_codigo_210200_tp_cua_84dacf` — Facultad informar Código 210200/TP · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Potestad `Potestad_integracion_con_leliq_y_o_nobac_incrementos_exigencia__se_autoriza_a_las_entidad_663475` — Integración con LELIQ y/o NOBAC — incrementos exigencia · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_el_codigo_210100_tp_no_podra_superar_la_posicion_tpnyrm_tp_cuando_tp_identifica__da9d78` — Límite Código 210100/TP ≤ Posición (TPNyRM)/TP · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_el_codigo_210200_tp_no_podra_superar_la_posicion_tpnyrm_tp_cuando_tp_identifica__fa5460` — Límite Código 210200/TP ≤ Posición (TPNyRM)/TP · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_el_importe_del_codigo_210100_tp_no_podra_superar_la_exigencia_determinada_expres_1d6735` — Límite Código 210100/TP sobre exigencia · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_el_importe_del_codigo_210200_tp_no_podra_superar_la_exigencia_determinada_expres_ffe923` — Límite Código 210200/TP sobre exigencia · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_las_entidades_del_grupo_b_no_podran_hacer_uso_de_la_integracion_con_bote_2020_de_444bab` — Prohibición integración BOTE 2020 — Grupo B desde enero/2019 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_las_entidades_del_grupo_b_no_podran_hacer_uso_de_la_integracion_con_leliq_y_o_no_611082` — Prohibición integración LELIQ/NOBAC código 826000/001-TP — Grupo B desde enero/2019 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_las_entidades_del_grupo_b_no_podran_informar_las_partidas_824000_001_tp_826000_0_d3d4bb` — Prohibición información partidas específicas — Grupo B desde enero/2019 · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "A efectos de determinar la estructura de plazos residuales (punto 1.2.3.) aplicable a\nlos depósitos"}

## 13. `Condicion_conversion_a_pesos_cuando_corresponda__cuando_corresponda_la_conversion_a_pesos__ed0582` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_dcpc::3.4.4.1` (e0, bloque de lista True; págs. 17):

```
[encabezado | punto S3]
Sección 3. CRITERIOS GENERALES
[encabezado | punto 3.4]
3.4. Criterios específicos para determinados instrumentos financieros.
[encabezado | punto 3.4.4]
3.4.4. Operaciones de Pase
[intro | punto 3.4.4]
De acuerdo con los principios de baja en cuentas de la NIIF 9, estas operaciones se consideran
como financiaciones con garantía y, por tanto las registraciones deben realizarse de acuerdo con
las siguientes pautas:
[texto propio | punto 3.4.4.1]
3.4.4.1. Pases Activos
Las financiaciones otorgadas instrumentadas mediante pases activos se registrarán en las cuentas
de “Otros Créditos por Intermediación Financiera – Deudores por pases activos”, clasificándolas
según quien sea la contraparte en deudores financieros, BCRA y no financieros y atendiendo el
activo recibido en garantía.
Al cierre de cada mes, los intereses devengados a cobrar se imputarán en la cuenta “Otros créditos
por intermediación financiera - Intereses devengados a cobrar por pases activos” o “Intereses
devengados a cobrar por pases activos con el B.C.R.A.” con contrapartida en “Ingresos Financieros
- Intereses por pases activos del Sector Financiero”, “Intereses por pases activos con el B.C.R.A.” o
“Intereses por otros pases activos”, según corresponda.
Los activos subyacentes recibidos por las operaciones de pases activo se registrarán en partidas
fuera de balance. En estas cuentas se mostrarán al cierre de cada mes los valores nocionales de
las operaciones vigentes medidos a valor razonable, y convertidos a su equivalente en pesos, de
corresponder. No se deducirán los activos recibidos que hayan sido vendidos por la entidad, sino
que se darán de baja solo cuando finalice la operación de pase.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_conversion_a_pesos_cuando_corresponda__cuando_corresponda_la_conversion_a_pesos__ed0582` — Conversión a pesos cuando corresponda
  - propiedades: {"descripcion": "Cuando corresponda la conversión a pesos de los valores nocionales"}
  - tramo: convertidos a su equivalente en pesos, de corresponder
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_en_las_cuentas_de_partidas_fuera_de_balance_se_mostraran_al_cierre_de_cada_mes_l_604171` — Presentación valores nocionales a valor razonable mensualmente
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_dcpc_pdf` — Marco Contable

## 14. `Condicion_concurrencia_codigos_10120x_m_11010x_m_110500_m__condicion_que_requiere_la_concu_f70c2a` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_rml::1.9.2` (e0, bloque de lista True; págs. 19, 20):

```
[encabezado | punto S1]
Sección 1. Efectivo mínimo
[encabezado | punto 1.9]
1.9. Totales de control
[texto propio | punto 1.9.2]
1.9.2. Posiciones
[TABLA ri_rml::tabla003 | página 19 | e0_tablas | posicional]
Fila 1: col1 = Posición (Exceso/Defecto) | col2 = Definiciones y consistencias
Fila 2: col1 = A- Partidas comprendidas por moneda ⟨abarca hasta col2⟩
Fila 3: col1 = Posición/001 = (904000/001 + 661000/001) - (903000/001 + 750000/001 (n-1) –700000/001 – 651000/001) –671000/001 | col2 = Código 903000/001 = ∑ [Código 10XXXX/001 ) (excluyendo (n) (n-1 partida 102200 * ep ] + Partida 102200 *ep + Exigencias (n-1) (n) (n) (n) adicionales vigentes s/ Modelo de Información (n-1). - Código 700000/001 (n) con límite en el importe registrado en el código 903000/001 (n) - Código 210100/TP (n) : a)su importe no podrá superar la exigencia determinada sobre esos conceptos, es decir: ∑Código 210100/TP – Código 210104/TP - Código (n) (n) 210105/TP - Código 210106/TP – Código 210109/TP (n)) (n) (n) ≤ (∑ Código 11010X/001 * ep + ∑Código 10120X/001 (n-1) (n) * ep + Código 110500/001 * ep ) (n-1) (n) (n-1) (n) b)Se requerirá que el código TP corresponda a una especie en pesos c)El código 210100/TP se computa dentro del total de control (n) de la partida 904000/001 . (n)
Fila 4: col1 = Posición/M = (904000/M + 661000/M) - (903000/M + 750000/M (n-1) –700000/M – 651000/M) –671000/M M = moneda extranjera | col2 = - Código 903000/M (n) = ∑ (Código 10XXXX/M (n) * ep (n) ) + Exigen- cias adicionales vigentes s/ Modelo de Información (n) - Código 700000/M (n) con límite en el importe registrado en el código 903000/M (n) - Código 210200/TP (n) : d) Podrá informarse el código 210200/TP cuando concurren- (n) temente se informe por lo menos uno de los códigos siguien- tes: 10120X/M , 11010X/M y/o 110500/M ; (n) (n) (n) e)En tal caso, su importe no podrá superar la exigencia deter- minada sobre esos conceptos, es decir: ∑Código 210200/TP ≤ (∑ Código 11010X/M * ep + (n) (n) (n) ∑Código10120X/M * ep + Código 110500/M * ep ) (n) (n) (n) (n) f) Se requerirá que el código TP corresponda a una especie en dólares estadounidenses g)El código 210200/TP se computa dentro del total de control (n) de la partida 904000/M . (n)
[FIN TABLA ri_rml::tabla003]
[TABLA ri_rml::tabla004 | página 20 | e0_tablas | posicional]
Fila 1: col1 = B- Depósitos de títulos valores públicos nacionales e instrumentos de regulación monetaria del BCRA (coti- zación normal y habitual por importes significativos en mercados del país) ⟨abarca hasta col2⟩
Fila 2: col1 = Posición (TPNyRM)/TP = (906000/TP + 661000/TP) – (905000/TP – 651000/TP + 750000/TP(n-1) – 671000/TP) | col2 = - Código 905000/TP = ∑ (Código 300XXX/TP * ep(n)) - Código 906000/TP = valor a consignar de acuerdo a la especie de que se trate: Especie Cálculo 9132 500000/9132 – 210100/9132 9166 500000/9166 – 210100/9166 13000 500000/130000 – 210100/13000 14000 500000/14000 – 210100/14000 Otros TP 500000/TP – (210100/TP o 210200/TP) (*) Partidas 210109 solo para TP nacionales en pesos previstos en el punto 1.3.17. de las normas sobre “Efectivo mínimo”. - Código 210100/TP ≤ Posición (TPNyRM)/TP (donde TP identifica una especie en pesos) - Código 210200/TP ≤ Posición (TPNyRM)/TP (donde TP identifica una especie en dólares estadounidenses)
Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X/ y 10120X, ya sean en pesos o mone- da extranjera. M = moneda extranjera ep(n) = exigencia de efectivo mínimo del período para ese concepto. ⟨abarca hasta col2⟩
[FIN TABLA ri_rml::tabla004]
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_concurrencia_codigos_10120x_m_11010x_m_110500_m__condicion_que_requiere_la_concu_f70c2a` — Concurrencia códigos 10120X/M, 11010X/M, 110500/M
  - propiedades: {"descripcion": "Condición que requiere la concurrencia de al menos uno de los códigos 10120X/M, 11010X/M o 110500/M para habilitar la información del código 210200/TP."}
  - tramo: cuando concurrentemente se informe por lo menos uno de los códigos siguientes: 10120X/M , 11010X/M y/o 110500/M
- **Aristas** (49):
  - (extraccion) —condicion_de→ Potestad `Potestad_facultad_informar_codigo_210200_tp__facultad_de_informar_el_codigo_210200_tp_cua_84dacf` — Facultad informar Código 210200/TP
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual
  - (remision_derivada) —remite_a→ Condicion `Condicion_depositos_a_plazo_fijo_en_moneda_extranjera_aplicar_procedimiento_conjunto__el_p_bdf736` — Depósitos a plazo fijo en moneda extranjera — aplicar procedimiento conjunto · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Condicion `Condicion_obligaciones_de_lineas_financieras_formalizadas_hasta_5_2_informar_en_102062_m___6a707b` — Obligaciones de líneas financieras formalizadas hasta 5/2 — informar en 102062/M · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Condicion `Condicion_plazo_fijo_en_moneda_extranjera_aplicar_estructura_del_mes_anterior__cuando_se_t_b008f3` — Plazo fijo en moneda extranjera — aplicar estructura del mes anterior · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_100000_m_depositos_y_obligaciones__incluye_depositos_y_obligaciones_por_i_127313` — Código 100000/M — depósitos y obligaciones · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10141x_m_extension_automatica_de_plazo__en_extension_automatica_de_plazo__75b1f5` — Código 10141X/M — extensión automática de plazo · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10145x_m_obligaciones_por_lineas_financieras_del_exterior__incluye_obliga_b6323e` — Código 10145X/M — obligaciones por líneas financieras del exterior · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_101490_001_inversiones_en_certificados_nominativos_intransferibles__inclu_ed690c` — Código 101490/001 — inversiones en certificados nominativos intransferibles · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10161x_001_inversiones_a_plazo_de_uva__incluye_inversiones_a_plazo_de_uva_e146de` — Código 10161X/001 — inversiones a plazo de UVA · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_101650_001_depositos_a_plazo_fijo_de_menores_de_edad__incluye_depositos_a_432517` — Código 101650/001 — depósitos a plazo fijo de menores de edad · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10166x_001_colocaciones_de_titulos_de_deuda_en_uvi_y_uva__incluye_colocac_5e2ac4` — Código 10166X/001 — colocaciones de títulos de deuda en UVI y UVA · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10171x_001_depositos_reprogramados_cedros__incluye_importe_de_depositos_r_a0c6ba` — Código 10171X/001 — depósitos reprogramados CEDROS · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10180x_m_titulos_valores_de_deuda__incluye_titulos_valores_de_deuda_compr_b76ad9` — Código 10180X/M — títulos valores de deuda · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10190x_001_cauciones_bursatiles_tomadoras__incluye_cauciones_bursatiles_t_1af4a2` — Código 10190X/001 — cauciones bursátiles tomadoras · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_10206x_m_obligaciones_por_lineas_financieras_del_exterior_no_instrumentad_919e76` — Código 10206X/M — obligaciones por líneas financieras del exterior no instrumentadas · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_102090_010_obligaciones_a_la_vista_por_transferencias_del_exterior__inclu_011a74` — Código 102090/010 — obligaciones a la vista por transferencias del exterior · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_102100_m_saldos_sin_utilizar_de_adelantos_en_cuenta_corriente__incluye_sa_6129e5` — Código 102100/M — saldos sin utilizar de adelantos en cuenta corriente · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_102400_m_defecto_de_aplicacion_de_capacidad_prestable__incluye_importe_de_2e05fc` — Código 102400/M — defecto de aplicación de capacidad prestable · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigo_300000_tp_depositos_a_plazo_fijo_de_titulos_publicos__incluye_depositos_a_cb1dd7` — Código 300000/TP — depósitos a plazo fijo de títulos públicos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigos_10120x_m_11010x_m_y_110500_m_depositos_a_plazo_fijo_de_titulos__identifi_e0a405` — Códigos 10120X/M, 11010X/M y 110500/M — depósitos a plazo fijo de títulos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigos_10160x_001_y_10163x_001_imposiciones_en_uva_y_uvi__incluye_importes_de_i_aeb460` — Códigos 10160X/001 y 10163X/001 — imposiciones en UVA y UVI · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_codigos_10162x_001_y_10164x_001_cuentas_de_ahorro_en_uva_y_uvi__incluye_cuentas__240076` — Códigos 10162X/001 y 10164X/001 — cuentas de ahorro en UVA y UVI · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Definicion `Definicion_plazos_residuales_tramos_en_pesos__los_depositos_y_obligaciones_a_plazo_se_clasi_6f00f1` — Plazos residuales — tramos en pesos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_calcular_plazos_residuales_computando_la_cantidad_de_dias_que_restan_hasta_el_ve_db4b21` — Calcular plazos residuales por días hasta vencimiento · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_computar_plazos_residuales_de_obligaciones_de_pago_en_cuotas_de_capital_en_forma_6de0a2` — Computar plazos residuales de obligaciones de pago en cuotas de capital · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_consignar_promedio_mensual_de_saldos_diarios_de_depositos_y_obligaciones_que_ver_e943bc` — Consignar promedio mensual de saldos con factores de concentración de pasivos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_informar_depositos_y_obligaciones_a_plazo_considerando_sus_plazos_residuales__ri_ea10ee` — Informar depósitos y obligaciones a plazo según plazos residuales · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_informar_el_total_de_depositos_a_la_orden_de_entidades_financieras_no_bancarias__84182b` — Bancos comerciales informarán depósitos a la orden de entidades financieras no bancarias · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_informar_obligaciones_respecto_de_las_cuales_se_hayan_dispuesto_aumentos_puntual_5b18a1` — Informar obligaciones con aumentos puntuales de exigencia por concentración de pasivos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_informar_un_subcodigo_por_cada_moneda_o_instrumento_de_deuda_en_que_se_encuentre_f6d5fe` — Informar subcódigo por moneda o instrumento de deuda · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_para_plazos_fijos_y_restantes_operaciones_a_plazo_en_pesos_considerar_para_el_ca_338d28` — Considerar tramos y promedios anteriores y tasas del período para plazos fijos en pesos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_registrar_promedio_mensual_de_saldos_diarios_incluyendo_depositos_que_verifiquen_f734c8` — Registrar promedio mensual de saldos diarios con concentración excesiva de pasivos · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_sumar_los_tramos_de_plazos_informados_en_la_posicion_del_mes_anterior_n_1_y_dete_6cebb0` — Sumar tramos de plazos del mes anterior y determinar porcentajes · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_sumar_los_tramos_de_plazos_informados_en_la_posicion_del_mes_bajo_informe_n_y_ap_539ab5` — Sumar tramos del mes bajo informe y aplicar porcentajes anteriores · {"alcance": "interna", "destino": "ri_rml::1.2.3", "evidencia": "Fila 3: col1 = X = código de tramo de plazo residual según punto 1.2.3. en los códigos 11010X"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_integracion_de_exigencia_en_pesos_con_activos_elegibles__efemin_1_3_17_dc13e5` — Integración de exigencia en pesos con activos elegibles · {"alcance": "externa", "destino": "efemin::1.3.17", "evidencia": "punto 1.3.17. de las normas sobre “Efectivo mínimo"}
  - (remision_derivada) —remite_a→ Potestad `Potestad_facultad_de_integrar_exigencia_con_activos_elegibles__las_entidades_financieras__2f4154` — Facultad de integrar exigencia con activos elegibles · {"alcance": "externa", "destino": "efemin::1.3.17", "evidencia": "punto 1.3.17. de las normas sobre “Efectivo mínimo"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_01_06_18_a_20_06_18_junio__periodo_comprendido_entre_el_1_de_junio_de_20_4aa136` — Período 01/06/18 a 20/06/18 junio · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_01_07_18_julio__periodo_del_1_de_julio_de_2018__ri_rml_sbloque11_a2f021` — Período 01/07/18 julio · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_02_07_18_al_17_07_18_julio__periodo_comprendido_entre_el_2_de_julio_de_2_08b861` — Período 02/07/18 al 17/07/18 julio · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_21_06_18_a_30_06_18_junio__periodo_comprendido_entre_el_21_de_junio_de_2_082de9` — Período 21/06/18 a 30/06/18 junio · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_consignar_en_codigo_824000_001_el_incremento_en_la_exigencia_proveniente_del_aum_155daf` — Consignar incremento de exigencia código 824000/001 · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_informar_la_porcion_de_los_saldos_promedio_de_bonos_del_tesoro_nacional_en_pesos_13a538` — Informar porción de saldos promedio código 210105/TP · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_las_partidas_4520xx_incluiran_a_partir_del_21_06_18_de_corresponder_la_aplicacio_29b3dc` — Incluir aplicación de integración en Bonos partidas 4520XX · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_los_conceptos_que_no_registren_incrementos_de_tasas_de_exigencia_se_informaran_u_fb15aa` — Informar conceptos sin incremento de tasas período junio-julio 2018 · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_los_conceptos_que_registren_incrementos_en_las_tasas_se_trataran_conforme_al_pun_ee49bd` — Informar conceptos con incremento de tasas período junio-julio 2018 · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_deposito_de_bonos_del_tesoro_en_cryl__ri_rml_sbloque11_030bd3` — Depósito de Bonos del Tesoro en CRyL · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_el_saldo_del_codigo_210105_tp_no_podra_exceder_el_saldo_del_codigo_824000_001__r_18f09f` — Límite código 210105/TP ≤ código 824000/001 · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_para_efectuar_el_control_sobre_la_partida_210100_a_partir_de_junio_18_se_detraer_32863e` — Control código 210100/TP detraído 210105 · {"alcance": "interna", "destino": "ri_rml::1.9.2", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}

## 15. `Condicion_condicion_codigo_210100_mayor_que_suma_de_codigos_especificos__se_aplica_la_rest_c60382` — RI:resto · vigilancia:1

Texto que vio E3 de `ri_rml::1.3` (e0, bloque de lista True; págs. 7, 8, 9, 10):

```
[encabezado | punto S1]
Sección 1. Efectivo mínimo
[texto propio | punto 1.3]
1.3. Integración del período
Código 205030/001
Se incluirán los saldos acreedores registrados en las cuentas corrientes abiertas en el BCRA,
en pesos
Código 205035/M
Se incluirán los saldos acreedores de las cuentas a la vista de las entidades financieras abiertas
en el BCRA en dólares estadounidenses o en otras monedas extranjeras.
Código 205040/M
Se consignarán los saldos acreedores de las cuentas especiales de garantía a favor de las cá-
maras electrónicas de compensación, según el punto 2.1.3. del texto ordenado sobre Efectivo
Mínimo, y de las demás cuentas especiales abiertas en el BCRA (operatoria vinculada con tar-
jetas de crédito, cajeros automáticos, etc.).
Código 205050/M
Se incluirán los saldos acreedores de las cuentas corrientes de las entidades financieras no
bancarias abiertas en bancos comerciales para la integración de la exigencia de efectivo míni-
mo.
Código 205055/001
Se informarán los saldos acreedores que registren las cuentas corrientes especiales abiertas en
el BCRA, vinculadas con la atención de los beneficios previsionales a cargo de la Administra-
ción Nacional de la Seguridad Social.
Código 210100/TP
Se informará la porción de los saldos promedio de los títulos públicos nacionales en pesos de-
positados en la “Subcuenta 60 de efectivo mínimo” habilitada en la “Central de Registro y Liqui-
dación de Pasivos Públicos y Fideicomisos Financieros -CRyL-” y los importes correspondien-
tes a las LELIQ efectivamente utilizadas para integrar las garantías para cubrir los saldos netos
deudores que surgen en los procesos de compensación de las operatorias en pesos de las cá-
maras electrónicas de compensación -sin superar el 50 % de las garantías exigidas por cada
producto-, que se destine a integrar el efectivo mínimo en pesos en los casos previstos en los
puntos 1.2. (párrafo 8), 1.3.16. y 1.3.17. de las normas sobre Efectivo mínimo, identificados por
especie de título público nacional.
Por consiguiente, el importe a consignar en este código incluirá los importes que se informen en
los códigos 210104/TP, 210105/TP, 210106/TP y 210109/TP, y aquellos importes que se desti-
nen a integrar los depósitos de títulos públicos (no nacionales) y privados en pesos.
Si el Código 210100 > ∑ (Códigos 210104/TP , 210105/TP , 210106/TP y 210109/TP
(n) (n) (n) (n)
), se requerirá que ese importe remanente no supere las exigencias que se determinen sobre
(n
los depósitos en pesos de títulos privados y públicos (excepto nacionales):
∑Código 210100/TP - ∑ (Códigos 210104/TP , 210105/TP , 210106/TP y 210109/TP ) ≤
(n) (n) (n) (n) (n)
(∑ Código 11010X/001 * ep + ∑Código 10120X/001 * ep + Código 110500/001 *
(n-1) (n) (n-1) (n) (n-1)
ep ).
(n)
El saldo consignado en el código 210100/TP es una aplicación específica del total de las te-
nencias informadas en la partida 500000/TP para especies en pesos, y por tanto, su saldo se
encuentra incluido en dicha partida, y el código TP informado deberá corresponder a una es-
pecie en pesos.
Códigos 210200/TP
Se utilizará este código para informar la porción de los saldos promedio depositados en la
“Subcuenta 60 efectivo mínimo”, habilitada en la CRyL cuando se apliquen a integrar el efecti-
vo mínimo por depósitos en títulos privados y públicos (excepto nacionales) en dólares esta-
dounidenses, identificados por especie de título público nacional.
El importe consignado en el código 210200/TP no podrá superar el importe de las exigencias
que se determinen sobre los depósitos de títulos privados y públicos (excepto nacionales), en
sus respectivas monedas.
∑Código 210200/TP(n) ≤ (∑ Código 11010X/010(n-1) * ep (n) + ∑Código 10120X/010(n-1) *
ep(n) + Código 110500/010(n-1) * ep(n))
Los saldos consignados en esta partida son una aplicación específica del total de las tenen-
cias informadas en las partidas 500000/TP, y por tanto, sus saldos se encuentran incluidos en
dicha partida.
El código TP informado en la partida 210200/TP deberá corresponder a una especie en dóla-
res estadounidenses.
Integración en dólares estadounidenses de exigencias en otras monedas extranjeras.
Código 255035/M
Se informará la porción pertinente de los saldos informados en la partida 205035/010, destinada
a integrar la exigencia en la moneda extranjera M (para M ≠ 010).
∑ 255035/M ≤ Partida 205035/010.
Código 255040/M
Se informará la porción pertinente de los saldos informados en la partida 205040/010, destinada
a integrar la exigencia en la moneda extranjera M (para M ≠ 010).
∑ 255040/M ≤ Partida 205040/010
Código 255050/M
Se informará la porción pertinente de los saldos informados en la partida 205050/010, destinada
a integrar la exigencia en la moneda extranjera M (para M ≠ 010).
∑ 255050/M ≤ Partida 205050/010
Integración con BOTE, LELIQ, NOBAC y/o TPN en pesos permitidos
Se utilizarán las siguientes partidas para informar los importes admitidos que se apliquen a in-
tegrar la exigencia en pesos del período y diaria, conforme lo indicado en los puntos 1.3.16. y
1.3.17. de las normas sobre “Efectivo mínimo”.
Código 210104/TP
Se informará la porción pertinente de los saldos promedio de los “Bonos del Tesoro Nacional en
pesos a tasa fija” (BOTE) depositados en la “Subcuenta 60 efectivo mínimo”, habilitada en la
“Central de registro y liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros” (CRyL)” que se aplique a integrar la exigencia en pesos correspondien-
te a los depósitos en cuentas de los proveedores de servicios de pago que ofrecen cuentas de
pago (PSPOCP) (Apartado c) del punto 1.3.16. de las normas sobre “Efectivo mínimo”).
Esta partida se identificará con el código TP correspondiente a los bonos citados. Para el caso
de los BOTE 2027 se utilizarán los códigos 9132 y 9166, según corresponda.
Los saldos consignados en el código 210104 son una aplicación específica del total de las te-
nencias informadas en la partida 210100 para estos bonos y, por tanto, sus saldos se encuen-
tran incluidos en esta última partida, así como también en el correspondiente código 500000.
El importe máximo a integrar por este concepto se calculará en esta Institución:
Código 210104/TP ≤ Código 102200/001(n) * 45%
Código 210105/TP
Se informará la porción pertinente de los saldos promedio de los “Bonos del Tesoro Nacional en
pesos a tasa fija” (BOTE) depositados en la “Subcuenta 60 efectivo mínimo”, habilitada en la
“Central de registro y liquidación de instrumentos de deuda pública, regulación monetaria y fi-
deicomisos financieros” (CRyL)” que se aplique a integrar la exigencia en pesos que correspon-
da a los conceptos previstos en los apartados a), b) y d) del punto 1.3.16.
Esta partida se identificará con el código TP correspondiente a los bonos citados. Para el caso
de los BOTE 2027 se utilizarán los códigos 9132 y 9166, según corresponda.
Los saldos consignados en el código 210105 son una aplicación específica del total de las te-
nencias informadas en la partida 210100 para estos bonos y, por tanto, sus saldos se encuen-
tran incluidos en esta última partida, así como también en el correspondiente código 500000.
∑Código 210105/TP ≤ 824100/001 + 824200/001
Código 210106/TP
Las entidades comprendidas informarán la porción de los saldos promedio de las LELIQ y/o
NOBAC depositadas en la CRyL que se aplique a integrar los importes admitidos.
Esta partida se identificará con el código TP correspondiente a los instrumentos citados. En es-
ta partida se incluirán, de corresponder, los importes de las LELIQ efectivamente utilizadas para
integrar las garantías para cubrir los saldos netos deudores que surgen en los procesos de
compensación de las operatorias en pesos de las cámaras electrónicas de compensación, sin
superar el 50 % de las garantías exigidas por cada producto. Para el caso de las LELIQ se in-
formará con el código 13000, en tanto que para las NOBAC se utilizará el código 14000.
Los saldos consignados en el código 210106 son una aplicación específica del total de las te-
nencias informadas en la partida 210100 para estos instrumentos y, por tanto, sus saldos se
encuentran incluidos en esta última partida, así como también en el correspondiente código
500000.
Código 210109/TP
Se informará la porción pertinente de los saldos promedio de los títulos públicos nacionales en
pesos previstos en el punto 1.3.17. de las normas sobre “Efectivo mínimo”, depositados en la
“Subcuenta 60 efectivo mínimo”, habilitada en la CRyL que se aplique a integrar la exigencia en
pesos.
Esta partida se identificará con el código TP correspondiente a los títulos citados.
Los saldos consignados en el código 210109 son una aplicación específica del total de las te-
nencias informadas en la partida 210100 para estos títulos y, por tanto, sus saldos se encuen-
tran incluidos en esta última partida, así como también en el correspondiente código 500000.
Código 500000/TP
Se incluirán los saldos de la citada subcuenta 60 de los títulos valores públicos nacionales e
instrumentos de regulación monetaria del BCRA valuados a su valor de mercado. Asimismo, se
incluirán, de corresponder, los importes de las LELIQ efectivamente utilizadas para integrar las
garantías para cubrir los saldos netos deudores que surgen en los procesos de compensación
de las operatorias en pesos de las cámaras electrónicas de compensación, sin superar el 50 %
de las garantías exigidas por cada producto.
Su saldo por cada especie TP se aplicará a integrar las exigencias determinadas sobre los có-
digos 300000/TP. También podrá aplicarse, de corresponder, a cubrir total o parcialmente las
exigencias determinadas sobre los códigos 10120X/M, 11010X/M y 110500/M. Dichas aplica-
ciones se informarán utilizando los códigos 210100/TP y 210200/TP.
Para las especies BOTE, LELIQ y NOBAC y los títulos públicos nacionales en pesos previstos
en el punto 1.3.17. de las normas sobre “Efectivo mínimo” (TP), se verificará que la sumatoria
de los importes utilizados para integrar posiciones en pesos no exceda el importe consig-
nado en la partida 500000 de cada una de estas especies:
500000/13000 ≥ 500000/14000 ≥ 500000/TP ≥
500000/9132 ≥ 500000/9166 ≥
210100/13000 210100/14000 210100/TP (*)
210100/9132 210100/9166
(*) Partidas 210109 solo para TP nacionales en pesos previstos en el punto 1.3.17. de las normas sobre
“Efectivo mínimo”.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condicion_codigo_210100_mayor_que_suma_de_codigos_especificos__se_aplica_la_rest_c60382` — Condición: Código 210100 mayor que suma de códigos específicos
  - propiedades: {"descripcion": "Se aplica la restricción sobre importe remanente cuando el Código 210100/TP es mayor que la suma de Códigos 210104/TP, 210105/TP, 210106/TP y 210109/TP"}
  - tramo: Si el Código 210100 > ∑ (Códigos 210104/TP , 210105/TP , 210106/TP y 210109/TP
- **Aristas** (22):
  - (extraccion) —condicion_de→ Restriccion `Restriccion_el_importe_remanente_del_codigo_210100_tp_que_exceda_la_suma_de_codigos_210104_t_3a9c22` — Límite importe remanente Código 210100 depósitos títulos privados públicos
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ri_rml_pdf` — Régimen Informativo Contable Mensual
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_las_cuentas_especiales_de_garantias_seran_consideradas_como_integracion_del_efec_83d6b7` — Consideración de cuentas especiales de garantías · {"alcance": "externa", "destino": "efemin::2.1.3", "evidencia": "punto 2.1.3. del texto ordenado sobre Efectivo\nMínimo, y de las demás cuentas especiales abiertas en el BCRA (operatoria vinculada"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_cuentas_especiales_de_garantias_para_cec__efemin_2_1_3_2380d7` — Cuentas especiales de garantías para CEC · {"alcance": "externa", "destino": "efemin::2.1.3", "evidencia": "punto 2.1.3. del texto ordenado sobre Efectivo\nMínimo, y de las demás cuentas especiales abiertas en el BCRA (operatoria vinculada"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_obligaciones_de_lineas_financieras_formalizadas_hasta_5_2_informar_en_102062_m___6a707b` — Obligaciones de líneas financieras formalizadas hasta 5/2 — informar en 102062/M · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "especies en pesos, de acuerdo con el procedimiento descripto en el punto\n1.3. “Integración” de las"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_01_06_18_a_20_06_18_junio__periodo_comprendido_entre_el_1_de_junio_de_20_4aa136` — Período 01/06/18 a 20/06/18 junio · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_01_07_18_julio__periodo_del_1_de_julio_de_2018__ri_rml_sbloque11_a2f021` — Período 01/07/18 julio · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_02_07_18_al_17_07_18_julio__periodo_comprendido_entre_el_2_de_julio_de_2_08b861` — Período 02/07/18 al 17/07/18 julio · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_09_11_a_30_11_lineas_financieras_exterior__periodo_temporal_para_el_cual_6912f3` — Período 09/11 a 30/11 — líneas financieras exterior · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "de integración admitidas para las entidades del grupo “A” (punto 1.3.- In-\ntegración con BOTE"}
  - (remision_derivada) ←remite_a— Condicion `Condicion_periodo_21_06_18_a_30_06_18_junio__periodo_comprendido_entre_el_21_de_junio_de_2_082de9` — Período 21/06/18 a 30/06/18 junio · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Definicion `Definicion_codigo_10145x_m_obligaciones_por_lineas_financieras_del_exterior__incluye_obliga_b6323e` — Código 10145X/M — obligaciones por líneas financieras del exterior · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "especies en pesos, de acuerdo con el procedimiento descripto en el punto\n1.3. “Integración” de las"}
  - (remision_derivada) ←remite_a— Definicion `Definicion_codigo_10190x_001_cauciones_bursatiles_tomadoras__incluye_cauciones_bursatiles_t_1af4a2` — Código 10190X/001 — cauciones bursátiles tomadoras · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "especies en pesos, de acuerdo con el procedimiento descripto en el punto\n1.3. “Integración” de las"}
  - (remision_derivada) ←remite_a— Definicion `Definicion_codigo_10206x_m_obligaciones_por_lineas_financieras_del_exterior_no_instrumentad_919e76` — Código 10206X/M — obligaciones por líneas financieras del exterior no instrumentadas · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "especies en pesos, de acuerdo con el procedimiento descripto en el punto\n1.3. “Integración” de las"}
  - (remision_derivada) ←remite_a— Definicion `Definicion_codigos_10120x_m_11010x_m_y_110500_m_depositos_a_plazo_fijo_de_titulos__identifi_e0a405` — Códigos 10120X/M, 11010X/M y 110500/M — depósitos a plazo fijo de títulos · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "especies en pesos, de acuerdo con el procedimiento descripto en el punto\n1.3. “Integración” de las"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_consignar_en_codigo_824000_001_el_incremento_en_la_exigencia_proveniente_del_aum_155daf` — Consignar incremento de exigencia código 824000/001 · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_informar_la_porcion_de_los_saldos_promedio_de_bonos_del_tesoro_nacional_en_pesos_13a538` — Informar porción de saldos promedio código 210105/TP · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_las_partidas_4520xx_incluiran_a_partir_del_21_06_18_de_corresponder_la_aplicacio_29b3dc` — Incluir aplicación de integración en Bonos partidas 4520XX · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_los_conceptos_que_no_registren_incrementos_de_tasas_de_exigencia_se_informaran_u_fb15aa` — Informar conceptos sin incremento de tasas período junio-julio 2018 · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_los_conceptos_que_registren_incrementos_en_las_tasas_se_trataran_conforme_al_pun_ee49bd` — Informar conceptos con incremento de tasas período junio-julio 2018 · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_deposito_de_bonos_del_tesoro_en_cryl__ri_rml_sbloque11_030bd3` — Depósito de Bonos del Tesoro en CRyL · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_el_saldo_del_codigo_210105_tp_no_podra_exceder_el_saldo_del_codigo_824000_001__r_18f09f` — Límite código 210105/TP ≤ código 824000/001 · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_para_efectuar_el_control_sobre_la_partida_210100_a_partir_de_junio_18_se_detraer_32863e` — Control código 210100/TP detraído 210105 · {"alcance": "interna", "destino": "ri_rml::1.3", "evidencia": "partir de junio/18.\nPara efectuar el control previsto en los puntos 1.3. y 1.9.2. sobre la partida\n210100"}

## 16. `Condicion_informacion_comunicada_o_plazo_de_5_anos__el_cheque_debe_haber_sido_informado_po_a15956` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `ceninf::1.3` (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S1]
Sección 1. Central de Cheques Rechazados.
[texto propio | punto 1.3]
1.3. Criterios de difusión.
Los cheques cancelados dentro de los 15 días corridos de la fecha de rechazo se-
rán dados de baja dentro de los 2 días hábiles en que la entidad comunicare la can-
celación.
Los cheques cancelados entre los 16 y 90 días corridos de la fecha de rechazo, se-
rán dados de baja al año de la fecha de pago, en la medida en que hubieren sido in-
formados por la entidad.
Los cheques pagados a partir de los 91 días corridos de la fecha de rechazo serán
dados de baja a los dos años de la fecha de cancelación, en la medida en que hu-
bieren sido informados por la entidad o a los 5 años de la fecha de rechazo, lo que
ocurriere primero.
Los cheques no cancelados serán dados de baja a los 5 años de la fecha de recha-
zo.
Los cheques rechazados serán dados de baja de acuerdo con los criterios estable-
cidos en los dos primeros párrafos, en la medida que la entidad hubiere comunicado
el pago de multas.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_informacion_comunicada_o_plazo_de_5_anos__el_cheque_debe_haber_sido_informado_po_a15956` — Información comunicada o plazo de 5 años
  - propiedades: {"descripcion": "El cheque debe haber sido informado por la entidad o debe haber transcurrido el plazo de 5 años de la fecha de rechazo, lo que ocurra primero", "umbrales": [{"tramo": "a los 5 años de la fecha de rechazo", "valor": "5", "unidad": "anios", "comparacion": "no_determinada", "regla_comparacion": "sin_marcador_plazo", "origen": "e1", "tramo_verificado": "exacta"}]}
  - tramo: en la medida en que hubieren sido informados por la entidad o a los 5 años de la fecha de rechazo, lo que ocurriere primero
- **Aristas** (2):
  - (extraccion) —condicion_de→ Operacion `Operacion_baja_de_cheques_pagados_91_dias_o_mas__ceninf_1_3_eb169c` — Baja de cheques pagados — 91 días o más
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ceninf_pdf` — Centrales de Información · {"rol_fuente": "derivada_de_procedencia"}

## 17. `Condicion_servicios_delegados_de_criticidad_alta_o_relevantes__servicios_procesos_y_o_acti_332a13` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `nmcief::A6::Sbloque13` (e0, bloque de lista True; págs. 33):

```
[encabezado | punto A6]
Anexo VI
[intersticial | punto A6::S0]
Procedimientos mínimos de auditoría a aplicar en oportunidad de la revisión del ciclo para
cada ejercicio:
[texto propio | punto A6::Sbloque13]
Gestión de la relación con terceras partes
Evaluar las condiciones generales para las delegaciones de procesos, servicios y/o activi-
dades vinculadas con los procesos de tecnología y seguridad de la información y verificar
el establecimiento de un sector o una función responsable de la gestión de la relación con
las terceras partes, en función de los operaciones, procesos y estructura de la entidad.
Evaluar la política y el marco de gestión de procesos, servicios y/o actividades delegadas
en terceras partes.
Con respecto a la formalización de la relación, evaluar que la entidad formalice las relacio-
nes con terceras partes que brinden procesos, servicios y/o actividades delegadas de
acuerdo con los procedimientos establecidos. Para ello se evaluará el funcionamiento de
este control aplicado a aquellos servicios, procesos y/o actividades delegadas que la audi-
toría interna determine como de criticidad alta o relevantes para el negocio, en función de
los resultados de la gestión de riesgos de tecnología y seguridad de la información aplica-
dos a este tipo de activos.
En relación con los aspectos del control y monitoreo de estas actividades, evaluar el proce-
so de control que permita realizar un seguimiento y evaluación de los procesos, servicios y
actividades de tecnología y seguridad de la información delegados en terceras partes.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_servicios_delegados_de_criticidad_alta_o_relevantes__servicios_procesos_y_o_acti_332a13` — Servicios delegados de criticidad alta o relevantes
  - propiedades: {"descripcion": "Servicios, procesos y/o actividades delegadas que la auditoría interna determine como de criticidad alta o relevantes para el negocio, en función de los resultados de la gestión de riesgos de tecnología y seguridad de la información"}
  - tramo: aquellos servicios, procesos y/o actividades delegadas que la auditoría interna determine como de criticidad alta o relevantes para el negocio
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_evaluar_el_funcionamiento_del_control_de_formalizacion_aplicado_a_aquellos_servi_d51eff` — Evaluación de funcionamiento de control en servicios críticos
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos

## 18. `Condicion_informacion_comunicada_por_la_entidad__el_cheque_debe_haber_sido_informado_por_l_460ea7` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `ceninf::1.3` (e0, bloque de lista True; págs. 6):

```
[encabezado | punto S1]
Sección 1. Central de Cheques Rechazados.
[texto propio | punto 1.3]
1.3. Criterios de difusión.
Los cheques cancelados dentro de los 15 días corridos de la fecha de rechazo se-
rán dados de baja dentro de los 2 días hábiles en que la entidad comunicare la can-
celación.
Los cheques cancelados entre los 16 y 90 días corridos de la fecha de rechazo, se-
rán dados de baja al año de la fecha de pago, en la medida en que hubieren sido in-
formados por la entidad.
Los cheques pagados a partir de los 91 días corridos de la fecha de rechazo serán
dados de baja a los dos años de la fecha de cancelación, en la medida en que hu-
bieren sido informados por la entidad o a los 5 años de la fecha de rechazo, lo que
ocurriere primero.
Los cheques no cancelados serán dados de baja a los 5 años de la fecha de recha-
zo.
Los cheques rechazados serán dados de baja de acuerdo con los criterios estable-
cidos en los dos primeros párrafos, en la medida que la entidad hubiere comunicado
el pago de multas.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_informacion_comunicada_por_la_entidad__el_cheque_debe_haber_sido_informado_por_l_460ea7` — Información comunicada por la entidad
  - propiedades: {"descripcion": "El cheque debe haber sido informado por la entidad"}
  - tramo: en la medida en que hubieren sido informados por la entidad
- **Aristas** (2):
  - (extraccion) —condicion_de→ Operacion `Operacion_baja_de_cheques_cancelados_16_a_90_dias__ceninf_1_3_2693b9` — Baja de cheques cancelados — 16 a 90 días
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_ceninf_pdf` — Centrales de Información · {"rol_fuente": "derivada_de_procedencia"}

## 19. `Condicion_esquemas_de_autorizacion_acordes_a_politica_de_control_de_accesos__que_existan_e_9fce33` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `nmcief::A6::Sbloque12` (e0, bloque de lista True; págs. 33):

```
[encabezado | punto A6]
Anexo VI
[intersticial | punto A6::S0]
Procedimientos mínimos de auditoría a aplicar en oportunidad de la revisión del ciclo para
cada ejercicio:
[texto propio | punto A6::Sbloque12]
Desarrollo, adquisición y mantenimiento de “software”
Evaluar los Requisitos para los sistemas y aplicaciones, considerando la verificación de los
siguientes aspectos:
- Controles automatizados definidos en la normativa vigente.
- Controles para la identificación única del cliente y el registro de los datos obligatorios.
Asimismo, evaluar que se realicen procesos periódicos de control y depuración.
- Esquemas de autorización acordes a la política de control de accesos para el ingreso,
modificación y baja de operaciones y parámetros.
- Funcionalidad para la gestión de usuarios y perfiles, y la asignación de permisos sobre
las funciones del sistema.
- Funciones que permitan ejercer un control sobre la asignación de perfiles de acuerdo
con los roles y funciones establecidos por la entidad.
- Registros de auditoría que permitan asegurar la trazabilidad de cada una de las acciones
realizadas.
- Documentación funcional, técnica y de usuario actualizadas de los sistemas de
información.
Evaluar los requisitos para la generación de los regímenes informativos. Verificar los sis-
temas o procesos automatizados para la generación de los regímenes informativos requeri-
dos por el BCRA.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_esquemas_de_autorizacion_acordes_a_politica_de_control_de_accesos__que_existan_e_9fce33` — Esquemas de autorización acordes a política de control de accesos
  - propiedades: {"descripcion": "Que existan esquemas de autorización acordes a la política de control de accesos para el ingreso, modificación y baja de operaciones y parámetros."}
  - tramo: Esquemas de autorización acordes a la política de control de accesos para el ingreso, modificación y baja de operaciones y parámetros.
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_evaluar_los_requisitos_para_los_sistemas_y_aplicaciones_considerando_la_verifica_decc49` — Evaluar requisitos sistemas y aplicaciones
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos

## 20. `Condicion_controles_automatizados_definidos_en_normativa_vigente__que_existan_controles_au_1aab0a` — NG:sin_raiz · vigilancia:1

Texto que vio E3 de `nmcief::A6::Sbloque12` (e0, bloque de lista True; págs. 33):

```
[encabezado | punto A6]
Anexo VI
[intersticial | punto A6::S0]
Procedimientos mínimos de auditoría a aplicar en oportunidad de la revisión del ciclo para
cada ejercicio:
[texto propio | punto A6::Sbloque12]
Desarrollo, adquisición y mantenimiento de “software”
Evaluar los Requisitos para los sistemas y aplicaciones, considerando la verificación de los
siguientes aspectos:
- Controles automatizados definidos en la normativa vigente.
- Controles para la identificación única del cliente y el registro de los datos obligatorios.
Asimismo, evaluar que se realicen procesos periódicos de control y depuración.
- Esquemas de autorización acordes a la política de control de accesos para el ingreso,
modificación y baja de operaciones y parámetros.
- Funcionalidad para la gestión de usuarios y perfiles, y la asignación de permisos sobre
las funciones del sistema.
- Funciones que permitan ejercer un control sobre la asignación de perfiles de acuerdo
con los roles y funciones establecidos por la entidad.
- Registros de auditoría que permitan asegurar la trazabilidad de cada una de las acciones
realizadas.
- Documentación funcional, técnica y de usuario actualizadas de los sistemas de
información.
Evaluar los requisitos para la generación de los regímenes informativos. Verificar los sis-
temas o procesos automatizados para la generación de los regímenes informativos requeri-
dos por el BCRA.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_controles_automatizados_definidos_en_normativa_vigente__que_existan_controles_au_1aab0a` — Controles automatizados definidos en normativa vigente
  - propiedades: {"descripcion": "Que existan controles automatizados definidos en la normativa vigente aplicable."}
  - tramo: Controles automatizados definidos en la normativa vigente.
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_evaluar_los_requisitos_para_los_sistemas_y_aplicaciones_considerando_la_verifica_decc49` — Evaluar requisitos sistemas y aplicaciones
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_nmcief_pdf` — Normas de Capitales Mínimos

## 21. `Condicion_proporcionalidad_a_dimension_e_importancia_economica__el_marco_debe_ser_proporci_287672` — NG:resto · vigilancia:1

Texto que vio E3 de `lingeef::2.4.1` (e0, bloque de lista True; págs. 36):

```
[encabezado | punto S2]
Sección 2. Gestión del riesgo de crédito.
[encabezado | punto 2.4]
2.4. Gestión del riesgo de crédito de contraparte.
[intro | punto 2.4]
A los efectos de gestionar de manera eficaz e integral el riesgo de crédito de contraparte, las
entidades financieras deben:
[texto propio | punto 2.4.1]
2.4.1. Contar con un marco que incluya políticas, prácticas, procedimientos y estructura organi-
zacional para una adecuada gestión de este riesgo. Dicho marco debe ser proporcional a
la dimensión e importancia económica de la entidad financiera y a la naturaleza y com-
plejidad de las exposiciones que generen el riesgo de crédito de contraparte.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_proporcionalidad_a_dimension_e_importancia_economica__el_marco_debe_ser_proporci_287672` — Proporcionalidad a dimensión e importancia económica
  - propiedades: {"descripcion": "El marco debe ser proporcional a la dimensión e importancia económica de la entidad financiera y a la naturaleza y complejidad de las exposiciones que generen el riesgo de crédito de contraparte"}
  - tramo: proporcional a la dimensión e importancia económica de la entidad financiera y a la naturaleza y complejidad de las exposiciones que generen el riesgo de crédito de contraparte
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_las_entidades_financieras_deben_contar_con_un_marco_que_incluya_politicas_practi_85ba2e` — Marco de gestión del riesgo de crédito de contraparte
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos

## 22. `Condicion_condicion_monedas_extranjeras_distintas_del_usd__cuando_se_trate_de_monedas_extr_72aacd` — NG:resto · vigilancia:1

Texto que vio E3 de `efemin::2.1::intro` (e0, bloque de lista True; págs. 17):

```
[encabezado | punto S2]
Sección 2. Integración.
[encabezado | punto 2.1]
2.1. Conceptos admitidos.
[bloque intro | punto 2.1]
La integración deberá efectuarse en la misma moneda y/o títulos e instrumentos de regulación
monetaria que corresponda a la exigencia pudiendo integrarse, de tratarse de monedas extran-
jeras distintas del dólar estadounidense, en esa moneda, salvo los casos de excepción previs-
tos en el punto 1.2.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_condicion_monedas_extranjeras_distintas_del_usd__cuando_se_trate_de_monedas_extr_72aacd` — Condición: monedas extranjeras distintas del USD
  - propiedades: {"descripcion": "Cuando se trate de monedas extranjeras distintas del dólar estadounidense"}
  - tramo: de tratarse de monedas extranjeras distintas del dólar estadounidense
- **Aristas** (4):
  - (extraccion) —condicion_de→ Potestad `Potestad_opcion_de_integracion_en_monedas_extranjeras_distintas_del_usd__las_entidades_pu_66366f` — Opción de integración en monedas extranjeras distintas del USD
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_efemin_pdf` — Texto Ordenado Efectivo Mínimo
  - (remision_derivada) ←remite_a— Excepcion `Excepcion_se_exceptua_de_la_prohibicion_de_compensacion_lo_previsto_en_el_primer_parrafo_d_5c3f86` — Excepción a prohibición de compensación · {"alcance": "interna", "destino": "efemin::2.1", "evidencia": "diferentes exigencias, excepto lo previsto en el primer párrafo del punto 2.1."}
  - (remision_derivada) ←remite_a— Restriccion `Restriccion_se_prohibe_la_compensacion_de_posiciones_deficitarias_con_posiciones_excedentari_8509a7` — Prohibición de compensación entre exigencias diferentes · {"alcance": "interna", "destino": "efemin::2.1", "evidencia": "diferentes exigencias, excepto lo previsto en el primer párrafo del punto 2.1."}

## 23. `Condicion_regimen_del_punto_1_5_1_1_condicion__las_obligaciones_de_indicacion_aplican_dent_26534d` — NG:resto · vigilancia:1

Texto que vio E3 de `expaef::1.5.1.3` (e0, bloque de lista True; págs. 7):

```
[encabezado | punto S1]
Sección 1. Sucursales en el país y en el exterior.
[encabezado | punto 1.5]
1.5. Habilitación.
[encabezado | punto 1.5.1]
1.5.1. Sucursales en el país.
[texto propio | punto 1.5.1.3]
1.5.1.3. Sucursales móviles. En el régimen citado en el punto 1.5.1.1. se deberá indicar
las actividades que proyectan desarrollar, la sucursal o, en su caso, la casa cen-
tral de la cual la sucursal móvil dependerá operativamente y los períodos en los
que operará.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_regimen_del_punto_1_5_1_1_condicion__las_obligaciones_de_indicacion_aplican_dent_26534d` — Régimen del punto 1.5.1.1 — condición
  - propiedades: {"descripcion": "Las obligaciones de indicación aplican dentro del régimen establecido en el punto 1.5.1.1"}
  - tramo: En el régimen citado en el punto 1.5.1.1.
- **Aristas** (7):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_debera_indicarse_la_sucursal_o_en_su_caso_la_casa_central_de_la_cual_la_sucursal_b8e8b5` — Indicación de sucursal o casa central — sucursal móvil
  - (extraccion) —condicion_de→ Obligacion `Obligacion_debera_indicarse_las_actividades_que_la_sucursal_movil_proyecta_desarrollar__exp_c9de93` — Indicación de actividades proyectadas — sucursal móvil
  - (extraccion) —condicion_de→ Obligacion `Obligacion_debera_indicarse_los_periodos_en_los_que_la_sucursal_movil_operara__expaef_1_5_1_ad7f3d` — Indicación de períodos de operación — sucursal móvil
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_expaef_pdf` — Autorización de sucursales
  - (remision_derivada) —remite_a→ Condicion `Condicion_plazo_previo_a_habilitacion__la_comunicacion_debe_realizarse_con_una_antelacion__aae5bb` — Plazo previo a habilitación · {"alcance": "interna", "destino": "expaef::1.5.1.1", "evidencia": "1.5.1.3. Sucursales móviles. En el régimen citado en el punto 1.5.1.1. se deberá indicar\nlas"}
  - (remision_derivada) —remite_a→ Obligacion `Obligacion_comunicar_la_iniciacion_de_actividades_mediante_la_integracion_del_regimen_infor_5f9127` — Comunicación de iniciación mediante régimen informativo · {"alcance": "interna", "destino": "expaef::1.5.1.1", "evidencia": "1.5.1.3. Sucursales móviles. En el régimen citado en el punto 1.5.1.1. se deberá indicar\nlas"}
  - (remision_derivada) —remite_a→ Operacion `Operacion_iniciacion_de_actividades_de_sucursal__expaef_1_5_1_1_6f254b` — Iniciación de actividades de sucursal · {"alcance": "interna", "destino": "expaef::1.5.1.1", "evidencia": "1.5.1.3. Sucursales móviles. En el régimen citado en el punto 1.5.1.1. se deberá indicar\nlas"}

## 24. `Condicion_prestamos_hipotecarios_en_uva__cuando_se_trata_de_prestamos_hipotecarios_expresa_aa26ff` — NG:resto · vigilancia:1

Texto que vio E3 de `manori::S2::chapeau_seccion` (e0, bloque de lista True; págs. 43):

```
[encabezado | punto S2]
Sección 2. Pautas mínimas del contrato de crédito con garantía hipotecaria con creación y emisión de Letras Hipotecarias.
[bloque chapeau_seccion | punto S2]
En la presente sección se establece un modelo de contrato de crédito con las pautas mínimas
que debe contener. Las cláusulas del contrato que no estén allí previstas deberán ajustarse a
las disposiciones contenidas en las normas sobre “Protección de los usuarios de servicios fi-
nancieros”.
En los casos de préstamos hipotecarios expresados en Unidades de Valor Adquisitivo actuali-
zables por “CER” - Ley 25.827 (“UVA”) y en Unidades de Vivienda actualizables por “ICC” -
Ley 27.271 (“UVI”) las cláusulas deberán adecuarse en función de lo establecido en las nor-
mas sobre “Política de crédito”.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_prestamos_hipotecarios_en_uva__cuando_se_trata_de_prestamos_hipotecarios_expresa_aa26ff` — Préstamos hipotecarios en UVA
  - propiedades: {"descripcion": "Cuando se trata de préstamos hipotecarios expresados en Unidades de Valor Adquisitivo (UVA) actualizables por CER conforme a la Ley 25.827."}
  - tramo: En los casos de préstamos hipotecarios expresados en Unidades de Valor Adquisitivo actualizables por "CER" - Ley 25.827 ("UVA")
- **Aristas** (3):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_las_clausulas_del_contrato_deberan_adecuarse_en_funcion_de_lo_establecido_en_las_d4f828` — Adecuación de cláusulas según Política de crédito
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_manori_pdf` — Manual de Originación y Administración de Préstamos Hipotecarios
  - (remision_derivada) ←remite_a— Operacion `Operacion_instrumentacion_y_desembolso_de_prestamo_hipotecario__manori_1_2_8_1_e155bf` — Instrumentación y desembolso de préstamo hipotecario · {"alcance": "interna", "destino": "manori::S2", "evidencia": "hipotecaria y creación de Letras\nHipotecarias establecido en la Sección 2."}

## 25. `Condicion_entidad_acreedora_en_todos_los_grados__la_entidad_debe_ser_la_acreedora_en_todos_d2d0eb` — NG:resto · vigilancia:1

Texto que vio E3 de `cajasc::5.2.1` (e0, bloque de lista True; págs. 36):

```
[encabezado | punto S5]
Sección 5. Garantías.
[encabezado | punto 5.2]
5.2. Preferidas “B”.
[intro | punto 5.2]
Están constituidas por derechos reales sobre bienes o compromisos de terceros que, feha-
cientemente instrumentados, aseguren que la entidad podrá disponer de los fondos en con-
cepto de cancelación de la obligación contraída por el cliente, cumpliendo previamente los
procedimientos establecidos para la ejecución de las garantías, y por las garantías definidas
en el punto 5.1. con excepción de las comprendidas en el punto 5.1.1., en tanto el plazo resi-
dual de las operaciones supere el término de 6 meses.
[intro | punto 5.2]
Se incluyen en esta categoría, con el carácter de enumeración taxativa, las siguientes:
[texto propio | punto 5.2.1]
5.2.1. Hipoteca en primer grado sobre inmuebles o cualquiera sea su grado de prelación
siempre que la entidad sea la acreedora en todos los grados.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_entidad_acreedora_en_todos_los_grados__la_entidad_debe_ser_la_acreedora_en_todos_d2d0eb` — Entidad acreedora en todos los grados
  - propiedades: {"descripcion": "La entidad debe ser la acreedora en todos los grados de la hipoteca."}
  - tramo: siempre que la entidad sea la acreedora en todos los grados
- **Aristas** (4):
  - (remision_derivada) ←remite_a— Condicion `Condicion_entidad_acreedora_en_todos_los_grados__la_entidad_debe_ser_la_acreedora_en_todos_04f21c` — Entidad acreedora en todos los grados · {"alcance": "interna", "destino": "cajasc::5.2.1", "evidencia": "siempre que la entidad sea la acreedora en todos los grados (punto 5.2.1.):"}
  - (extraccion) —condicion_de→ Operacion `Operacion_hipoteca_en_primer_grado_sobre_inmuebles__cajasc_5_2_1_01cf08` — Hipoteca en primer grado sobre inmuebles
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_cajasc_pdf` — Cajas de crédito cooperativas
  - (remision_derivada) ←remite_a— Operacion `Operacion_hipoteca_en_primer_grado_sobre_inmuebles__cajasc_5_5_10_72bdd0` — Hipoteca en primer grado sobre inmuebles · {"alcance": "interna", "destino": "cajasc::5.2.1", "evidencia": "siempre que la entidad sea la acreedora en todos los grados (punto 5.2.1.):"}

## 26. `Condicion_pertenencia_al_grupo_a_segun_normas_de_autoridades__la_entidad_debe_pertenecer_a_87fb34` — NG:resto · vigilancia:1

Texto que vio E3 de `lingeef::3.5.1` (e0, bloque de lista True; págs. 63):

```
[encabezado | punto S3]
Sección 3. Gestión del riesgo de liquidez.
[encabezado | punto 3.5]
3.5. Aplicación de herramientas de seguimiento de liquidez intradiaria. Escenarios de estrés.
[texto propio | punto 3.5.1]
3.5.1. Alcance.
Las entidades financieras que pertenezcan al Grupo “A” según lo previsto en el punto
4.1. de las normas sobre “Autoridades de entidades financieras”, deberán utilizar las
herramientas previstas en el punto 3.5.3. a los fines de identificar y hacer el seguimien-
to del riesgo de liquidez intradiaria al que se encuentran expuestas en condiciones
normales.
Adicionalmente, deberán evaluar el modo en que su perfil de liquidez intradiaria en si-
tuaciones de estrés cambiaría respecto del observado en condiciones normales, con-
forme a lo establecido en el punto 3.5.4.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_pertenencia_al_grupo_a_segun_normas_de_autoridades__la_entidad_debe_pertenecer_a_87fb34` — Pertenencia al Grupo A según normas de Autoridades
  - propiedades: {"descripcion": "La entidad debe pertenecer al Grupo A conforme a lo establecido en el punto 4.1 de las normas sobre Autoridades de entidades financieras."}
  - tramo: Las entidades financieras que pertenezcan al Grupo "A" según lo previsto en el punto 4.1. de las normas sobre "Autoridades de entidades financieras"
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_las_entidades_financieras_del_grupo_a_deberan_utilizar_las_herramientas_prevista_0171f4` — Deber de utilizar herramientas de seguimiento de liquidez intradiaria
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos

## 27. `Condicion_gestion_rtici_inadecuada_o_riesgo_excesivo__la_condicion_se_activa_cuando_la_sef_a5ea13` — NG:resto · vigilancia:1

Texto que vio E3 de `lingeef::5.6` (e0, bloque de lista True; págs. 117):

```
[encabezado | punto S5]
Sección 5. Gestión del riesgo de tasa de interés en la cartera de inversión.
[texto propio | punto 5.6]
5.6. Supervisión por parte de la Superintendencia de Entidades Financieras y Cambiarias.
Cuando la SEFyC concluya que la gestión del RTICI de una entidad financiera es inadecuada
o que ésta asume demasiado riesgo en relación con su capital o resultados, o con su perfil
general de riesgo, se le exigirá adoptar alguna/s de las siguientes medidas:
i) reducir sus exposiciones al RTICI;
ii) aumentar la integración de capital;
iii) revisar los parámetros internos de riesgo utilizados por la entidad; y/o
iv)mejorar su marco de gestión del riesgo.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_gestion_rtici_inadecuada_o_riesgo_excesivo__la_condicion_se_activa_cuando_la_sef_a5ea13` — Gestión RTICI inadecuada o riesgo excesivo
  - propiedades: {"descripcion": "La condición se activa cuando la SEFyC concluye que: (i) la gestión del RTICI es inadecuada, o (ii) la entidad asume demasiado riesgo en relación con su capital, resultados o perfil general de riesgo."}
  - tramo: Cuando la SEFyC concluya que la gestión del RTICI de una entidad financiera es inadecuada o que ésta asume demasiado riesgo en relación con su capital o resultados, o con su perfil general de riesgo
- **Aristas** (3):
  - (extraccion) —condicion_de→ Potestad `Potestad_exigir_medidas_de_gestion_rtici__la_sefyc_esta_facultada_para_exigir_a_la_entida_7b6fcf` — Exigir medidas de gestión RTICI
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_lingeef_pdf` — Lineamientos para la gestión de riesgos
  - (remision_derivada) ←remite_a— Potestad `Potestad_sefyc_puede_exigir_medidas_a_entidades_atipicas__la_sefyc_tiene_la_facultad_de_e_fd2de9` — SEFyC puede exigir medidas a entidades atípicas · {"alcance": "interna", "destino": "lingeef::5.6", "evidencia": "SEFyC les podrá exigir alguna/s de\nlas medidas previstas en el punto 5.6."}

## 28. `Condicion_registraciones_contables_no_reflejan_realidad_economica_y_juridica__condicion_qu_37e7b8` — NG:resto · vigilancia:1

Texto que vio E3 de `cajasc::9.10.2` (e0, bloque de lista True; págs. 57):

```
[encabezado | punto S9]
Sección 9. Previsiones por riesgo de incobrabilidad.
[encabezado | punto 9.10]
9.10. Requerimientos de la Superintendencia de Entidades Financieras y Cambiarias.
[intro | punto 9.10]
Ante requerimiento que formule la Superintendencia de Entidades Financieras y Cambiarias,
las entidades financieras deberán constituir previsiones por riesgo de incobrabilidad en los
porcentajes que se establezcan cuando:
[texto propio | punto 9.10.2]
9.10.2. de los elementos puestos a disposición de los inspectores actuantes surja que las re-
gistraciones contables efectuadas por las entidades no reflejan en forma precisa la
realidad económica y jurídica de las operaciones o que se han llevado a cabo accio-
nes o ardides para desnaturalizar o disimular el verdadero carácter o alcance de las
operaciones, con efectividad a la fecha que en cada caso se indique.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_registraciones_contables_no_reflejan_realidad_economica_y_juridica__condicion_qu_37e7b8` — Registraciones contables no reflejan realidad económica y jurídica
  - propiedades: {"descripcion": "Condición que se verifica cuando los elementos puestos a disposición de los inspectores actuantes demuestran que las registraciones contables efectuadas por las entidades no reflejan en forma precisa la realidad económica y jurídica de las operaciones."}
  - tramo: de los elementos puestos a disposición de los inspectores actuantes surja que las registraciones contables efectuadas por las entidades no reflejan en forma precisa la realidad económica y jurídica de las operaciones
- **Aristas** (8):
  - (remision_derivada) ←remite_a— Condicion `Condicion_ingreso_fuera_del_termino_fijado__condicion_ingreso_de_cargos_fuera_del_termino__e57fc5` — Ingreso fuera del término fijado · {"alcance": "interna", "destino": "cajasc::9.10.2", "evidencia": "2.7.10. Importes de los activos comprendidos en el punto 9.10.2. (-). Ante requerimiento"}
  - (extraccion) —condicion_de→ Obligacion `Obligacion_las_entidades_financieras_deberan_constituir_previsiones_por_riesgo_de_incobrabi_124ce5` — Constituir previsiones por riesgo de incobrabilidad ante requerimiento
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_cajasc_pdf` — Cajas de crédito cooperativas
  - (remision_derivada) ←remite_a— Condicion `Condicion_requerimiento_sefyc_con_elementos_de_inspeccion__condicion_requerimiento_de_la_s_8d901b` — Requerimiento SEFyC con elementos de inspección · {"alcance": "interna", "destino": "cajasc::9.10.2", "evidencia": "2.7.10. Importes de los activos comprendidos en el punto 9.10.2. (-). Ante requerimiento"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_obligacion_de_abonar_los_pertinentes_intereses_por_mora_cuando_el_ingreso_de_car_aab95f` — Pago de intereses por mora en ingreso fuera de plazo · {"alcance": "interna", "destino": "cajasc::9.10.2", "evidencia": "2.7.10. Importes de los activos comprendidos en el punto 9.10.2. (-). Ante requerimiento"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_obligacion_de_ingresar_los_cargos_resultantes_de_la_verificacion_de_encuadramien_7ce96d` — Ingreso de cargos dentro de 10 días hábiles · {"alcance": "interna", "destino": "cajasc::9.10.2", "evidencia": "2.7.10. Importes de los activos comprendidos en el punto 9.10.2. (-). Ante requerimiento"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_obligacion_de_verificar_el_encuadramiento_de_las_distintas_normas_que_utilicen_c_09fd89` — Verificación de encuadramiento normativo tras afectación RPC · {"alcance": "interna", "destino": "cajasc::9.10.2", "evidencia": "2.7.10. Importes de los activos comprendidos en el punto 9.10.2. (-). Ante requerimiento"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_deduccion_rpc_por_registraciones_contables_imprecisas__cajasc_2_7_10_a8056d` — Deducción RPC por registraciones contables imprecisas · {"alcance": "interna", "destino": "cajasc::9.10.2", "evidencia": "2.7.10. Importes de los activos comprendidos en el punto 9.10.2. (-). Ante requerimiento"}

## 29. `Condicion_cliente_de_riesgo_bajo_con_medidas_de_inclusion_financiera__supuesto_en_que_el_c_ed91d4` — NG:resto · vigilancia:1

Texto que vio E3 de `depaho::1.3::cierre` (e0, bloque de lista True; págs. 5, 6):

```
[encabezado | punto S1]
Sección 1. Caja de ahorros.
[encabezado | punto 1.3]
1.3. Identificación y situación fiscal del titular.
[bloque cierre | punto 1.3]
Será suficiente la sola presentación de los documentos de identidad previstos en las normas
sobre “Documentos de identificación en vigencia” para la acreditación de los datos previstos en
los puntos 1.3.1. a 1.3.3. y una declaración jurada del titular –o quien lo represente– para acre-
ditar los datos detallados en los puntos 1.3.4. a 1.3.6. Las presentaciones o actualizaciones,
tanto de los datos como de las declaraciones juradas, podrán ser realizadas presencialmente o
a través de medios electrónicos de comunicación, siendo de aplicación en este último caso lo
previsto en el punto 4.16.
Ello, sin perjuicio del cumplimiento en todos los casos de la normativa en materia de prevención
del lavado de activos y del financiamiento del terrorismo –especialmente en lo referido a la
identificación y conocimiento del cliente–.
No obstante, la apertura y el posterior mantenimiento de la cuenta podrán basarse en las medi-
das de Debida Diligencia Simplificada reconocidas por la Unidad de Información Financiera
(UIF) para clientes de riesgo bajo alcanzados por medidas que tengan por objetivo promover
y/o ampliar la inclusión financiera.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_cliente_de_riesgo_bajo_con_medidas_de_inclusion_financiera__supuesto_en_que_el_c_ed91d4` — Cliente de riesgo bajo con medidas de inclusión financiera
  - propiedades: {"descripcion": "Supuesto en que el cliente es de riesgo bajo y está alcanzado por medidas que tengan por objetivo promover y/o ampliar la inclusión financiera."}
  - tramo: para clientes de riesgo bajo alcanzados por medidas que tengan por objetivo promover y/o ampliar la inclusión financiera
- **Aristas** (8):
  - (extraccion) —condicion_de→ Potestad `Potestad_debida_diligencia_simplificada_para_clientes_de_riesgo_bajo__la_apertura_y_el_po_68d4bd` — Debida Diligencia Simplificada para clientes de riesgo bajo
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_depaho_pdf` — Depósitos de ahorro
  - (remision_derivada) ←remite_a— Condicion `Condicion_solicitud_de_apertura_por_personas_humanas__cuando_la_solicitud_de_apertura_prov_cfe3ab` — Solicitud de apertura por personas humanas · {"alcance": "interna", "destino": "depaho::1.3", "evidencia": "de apli-\ncación lo previsto para la “Caja de ahorros” en los puntos 1.3. y 1.4."}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_aplicar_en_lo_pertinente_los_puntos_1_3_o_3_4_2_segun_se_trate_de_personas_human_aab026` — Aplicación de puntos 1.3, 3.4.2, 1.6, 1.14, 3.1.2, 3.1.3, 3.1.4 · {"alcance": "interna", "destino": "depaho::1.3", "evidencia": "tiempo posible.\nSerán de aplicación –en lo pertinente– los puntos 1.3. o 3.4.2. (según se trate de personas\nhumanas o jurídicas), 1.6., 1.14., 3.1.2. (último párrafo), 3.1.3. y 3.1.4.\nSe admitirán únicamente"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_los_inversores_nacionales_considerados_sujetos_obligados_de_actividad_financiera_35de47` — Cumplimiento requisitos personas humanas — inversores nacionales · {"alcance": "interna", "destino": "depaho::1.3", "evidencia": "cumplimentarse\nlos requisitos establecidos para las personas humanas (punto 1.3.).\nii) Inversores extranjeros"}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_respecto_de_la_nomina_de_autoridades_y_de_los_representantes_autorizados_para_ut_8f5881` — Cumplimiento requisitos personas humanas — nómina de autoridades · {"alcance": "interna", "destino": "depaho::1.3", "evidencia": "cumplimentarse los requisitos establecidos\npara las personas humanas (punto 1.3.)."}
  - (remision_derivada) ←remite_a— Obligacion `Obligacion_se_aplicaran_las_normas_establecidas_para_los_depositos_en_caja_de_ahorros_en_lo_c8bd6d` — Aplicación de normas de depósitos en caja de ahorros · {"alcance": "interna", "destino": "depaho::1.3", "evidencia": "normas establecidas para los depósitos en caja de ahorros en los puntos 1.2.,\n1.3. (sólo identificación), 1.5. a 1.7., 1.9., 1.12. y 1.14. a 1.16.\nLa tasa de interés"}
  - (remision_derivada) ←remite_a— Operacion `Operacion_depositos_en_caja_de_ahorros__depaho_3_3_e5e4b4` — Depósitos en caja de ahorros · {"alcance": "interna", "destino": "depaho::1.3", "evidencia": "normas establecidas para los depósitos en caja de ahorros en los puntos 1.2.,\n1.3. (sólo identificación), 1.5. a 1.7., 1.9., 1.12. y 1.14. a 1.16.\nLa tasa de interés"}

## 30. `Condicion_no_se_oponen_disposiciones_precedentes__supuesto_en_el_que_las_disposiciones_gen_4b4fb8` — NG:resto · vigilancia:1

Texto que vio E3 de `depaho::3.7.8` (e0, bloque de lista True; págs. 42):

```
[encabezado | punto S3]
Sección 3. Especiales.
[encabezado | punto 3.7]
3.7. Caja de ahorros destinada a menores de edad autorizados.
[texto propio | punto 3.7.8]
3.7.8. En cuanto no se encuentre previsto y en la medida en que no se opongan a lo detallado
en los puntos precedentes, son de aplicación las disposiciones establecidas para los
depósitos en caja de ahorros.
```

Versión: final (grafo sin cola).
- **Nodo** Condicion `Condicion_no_se_oponen_disposiciones_precedentes__supuesto_en_el_que_las_disposiciones_gen_4b4fb8` — No se oponen disposiciones precedentes
  - propiedades: {"descripcion": "Supuesto en el que las disposiciones generales de depósitos en caja de ahorros no se oponen a lo establecido en los puntos precedentes sobre caja de ahorros para menores."}
  - tramo: en la medida en que no se opongan a lo detallado en los puntos precedentes
- **Aristas** (2):
  - (extraccion) —condicion_de→ Obligacion `Obligacion_cuando_no_se_encuentre_previsto_en_los_puntos_precedentes_y_en_la_medida_en_que__7835e8` — Aplicación disposiciones depósitos caja de ahorros
  - (estructural) —establecida_en→ TextoOrdenado `TextoOrdenado_depaho_pdf` — Depósitos de ahorro

