# U-CONF-MATRIZ, C3: anexo de la sensibilidad (fuera de la lista del §5; informativo)

Las correctas con anotación cuyo pase a «incorrecta» cambiaría el resultado de algún par (tabla de `clases_c3.md`). Cada entrada lleva la marca, la nota y las anotaciones de C2 y la ficha de C1.

## F23 — correcta (→ Operacion)

- Nota de C2: 3.12.2: «Las restantes operaciones de derivados financieros que quieran ser cursadas con acceso al mercado de cambios por parte de residentes que no sean entidades autorizadas a operar en cambios se regirán por lo dispuesto en los puntos 3.9. y 3.10.». La Condicion restringe el alcance subjetivo del destino y reformula parte de su propia definición (anotación: condición de alcance, cercana a un Sujeto); la relación es cierta como supuesto de aplicación.
- Anotaciones: alcance: la Condicion reformula parte de la definición del destino
- Origen: Condicion — «Residentes no autorizados a operar en cambios» (`Condicion_residentes_no_autorizados_a_operar_en_cambios__la_operacion_se_aplica_a_resident_dfb0b3`)
  - descripción (salida del extractor): La operación se aplica a residentes que no sean entidades autorizadas a operar en cambios
  - tramo de E1 (salida del extractor): 'residentes que no sean entidades autorizadas a operar en cambios'
- Destino: Operacion — «Operaciones derivados financieros — residentes no autorizados» (`Operacion_operaciones_derivados_financieros_residentes_no_autorizados__ext_3_12_2_43d4fc`)
  - descripción (salida del extractor): Operaciones de derivados financieros cursadas con acceso al mercado de cambios por residentes que no sean entidades autorizadas a operar en cambios
  - tramo de E1 (salida del extractor): 'Las restantes operaciones de derivados financieros que quieran ser cursadas con acceso al mercado de cambios por parte de residentes que no sean entidades autorizadas a operar en cambios'
- Unidad `ext::3.12.2` (ext, punto 3.12.2), páginas [36]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p16.png`, `c1/paginas/ext_p36.png`
- Texto heredado: [encabezado S3] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / [chapeau_seccion S3] Las entidades previamente a dar acceso al mercado de cambio por las operaciones comprendidas en los puntos 3.1. a 3.15. –incluyendo aquellas que se concreten a través de canjes o arbitrajes–, adicionalmente a los requisitos y condiciones específicas detalladas en cada punto, deberán cumplimentar los requisitos complementarios que constan en el punto 3.16. que resulten aplicables. / [encabezado 3.12] 3.12. Compra de moneda extranjera para operaciones con derivados financieros.
- Texto propio:

```text
3.12.2. Las restantes operaciones de derivados financieros que quieran ser cursadas con
acceso al mercado de cambios por parte de residentes que no sean entidades
autorizadas a operar en cambios se regirán por lo dispuesto en los puntos 3.9. y
3.10., según corresponda.
```

## F24 — correcta (→ Potestad)

- Nota de C2: 3.11.3: «podrán dar acceso al mercado de cambios a los residentes con endeudamientos […] para la compra de moneda extranjera para la constitución de las garantías […], en las siguientes condiciones:». La Condicion es la finalidad que restringe el acceso y reformula parte de la definición del destino (anotación: condición de alcance por finalidad; las condiciones enumeradas 3.11.3.1 y 3.11.3.2 están en otras unidades); la relación es cierta como restricción.
- Anotaciones: alcance: la Condicion es la finalidad que define el destino
- Origen: Condicion — «Compra de moneda extranjera para garantías» (`Condicion_compra_de_moneda_extranjera_para_garantias__el_acceso_se_condiciona_a_que_la_com_c8c356`)
  - descripción (salida del extractor): El acceso se condiciona a que la compra de moneda extranjera sea para la constitución de garantías en cuentas en moneda extranjera
  - tramo de E1 (salida del extractor): 'para la compra de moneda extranjera para la constitución de las garantías en cuentas en moneda extranjera'
- Destino: Potestad — «Facultad de dar acceso al mercado de cambios» (`Potestad_facultad_de_dar_acceso_al_mercado_de_cambios__las_entidades_tienen_la_facultad_d_db79ee`)
  - descripción (salida del extractor): Las entidades tienen la facultad de dar acceso al mercado de cambios a los residentes con endeudamientos o prefinanciaciones de exportaciones para la compra de moneda extranjera destinada a la constitución de garantías en cuentas en moneda extranjera
  - tramo de E1 (salida del extractor): 'Las entidades podrán dar acceso al mercado de cambios a los residentes'
- Unidad `ext::3.11.3::intro` (ext, punto 3.11.3), páginas [35]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p35.png`
- Texto heredado: [encabezado S3] Sección 3. Disposiciones específicas para los egresos por el mercado de cambios / [encabezado 3.11] 3.11. Otras compras de moneda extranjera por parte de residentes con aplicación específica. / [encabezado 3.11.3] 3.11.3. Las entidades podrán dar acceso al mercado de cambios a los residentes con
- Texto propio:

```text
endeudamientos comprendidos en el punto 7.9. originados a partir del 07/01/21
(únicamente originados a partir del 08/08/25 en el caso de aquellos comprendidos en
el punto 7.9.1.4.) o prefinanciaciones de exportaciones comprendidas en el punto
7.8.5., para la compra de moneda extranjera para la constitución de las garantías en
cuentas en moneda extranjera abiertas en entidades financieras locales o en el
exterior –cuando se trate de un endeudamiento financiero comprendido en el punto
3.5. o las prefinanciaciones admitidas–, por los montos exigibles en los contratos de
endeudamiento, en las siguientes condiciones:
```

## F27 — correcta (→ Operacion)

- Nota de C2: 2.2.3: «En el caso de que los cobros sean ingresados a través del sistema de monedas locales se considerará cumplimentada la liquidación por el monto acreditado en moneda nacional». El supuesto (ingreso por el sistema de monedas locales) es antecedente del tratamiento que el destino describe («Se considera cumplimentada la liquidación por el monto acreditado…», en su descripción). Anotación: el destino tiene el mismo tramo que la Condicion, así que por etiqueta y tramo la arista es circular; leído por etiqueta, descripción y tramo, la relación es cierta. Con una lectura estricta del nodo por su etiqueta sería incorrecta: queda para la adjudicación.
- Anotaciones: circular: el destino tiene el mismo tramo que la Condicion; la consecuencia del texto está solo en su descripción
- Origen: Condicion — «Cobros ingresados por sistema de monedas locales» (`Condicion_cobros_ingresados_por_sistema_de_monedas_locales__supuesto_en_que_los_cobros_de__af0c92`)
  - descripción (salida del extractor): Supuesto en que los cobros de exportación de servicios se ingresan a través del sistema de monedas locales
  - tramo de E1 (salida del extractor): 'En el caso de que los cobros sean ingresados a través del sistema de monedas locales'
- Destino: Operacion — «Ingreso de cobros por sistema de monedas locales» (`Operacion_ingreso_de_cobros_por_sistema_de_monedas_locales__ext_2_2_3_b672e2`)
  - descripción (salida del extractor): Ingreso de cobros de exportaciones de servicios a través del sistema de monedas locales. Se considera cumplimentada la liquidación por el monto acreditado en moneda nacional en la cuenta del exportador.
  - tramo de E1 (salida del extractor): 'los cobros sean ingresados a través del sistema de monedas locales'
- Unidad `ext::2.2.3` (ext, punto 2.2.3), páginas [11]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p11.png`
- Texto heredado: [encabezado S2] Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios. / [encabezado 2.2] 2.2. Cobros de exportaciones de servicios.
- Texto propio:

```text
2.2.3. En el caso de que los cobros sean ingresados a través del sistema de monedas
locales se considerará cumplimentada la liquidación por el monto acreditado en
moneda nacional en la cuenta del exportador. En caso de que se trate de servicios
prestados a residentes paraguayos o uruguayos facturados en la moneda del país de
destino de la exportación se computará el equivalente en dicha moneda del monto
acreditado.
```

## F33 — correcta (→ Operacion)

- Nota de C2: 2.12.2.3 (tabla de ponderadores, 0 %): «financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos […], en la medida que dichas operaciones estén denominadas en pesos, la fuente de fondos sea en esa moneda y las cuotas […] no excedan […] del 30 %». La condición delimita qué financiaciones entran en el renglón; la consecuencia del texto es el ponderador, que no es nodo de la arista (anotación).
- Anotaciones: consecuencia fuera de la arista: el texto asigna un ponderador, que no es nodo
- Origen: Condicion — «Denominación en pesos y fondos en pesos» (`Condicion_denominacion_en_pesos_y_fondos_en_pesos__las_operaciones_deben_estar_denominadas_03e0d7`)
  - descripción (salida del extractor): Las operaciones deben estar denominadas en pesos y la fuente de fondos debe ser en esa moneda.
  - tramo de E1 (salida del extractor): 'en la medida que dichas operaciones estén denominadas en pesos, la fuente de fondos sea en esa moneda'
- Destino: Operacion — «Financiación a beneficiarios seguridad social o empleados públicos» (`Operacion_financiacion_a_beneficiarios_seguridad_social_o_empleados_publicos__cap_2_12_2_3_47c5fe`)
  - descripción (salida del extractor): Financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos, con código de descuento, denominadas en pesos, con fondos en esa moneda, donde las cuotas de todas las financiaciones de la entidad con sistema de amortización periódica no excedan del 30% de los ingresos del deudor y/o codeudores.
  - tramo de E1 (salida del extractor): 'financiaciones otorgadas a beneficiarios de la seguridad social o a empleados públicos'
- Unidad `cap::2.12.2.3` (cap, punto 2.12.2.3), páginas [23]; PDF `data/experiment/subset/TO_capitales_minimos_actual.pdf`; render `c1/paginas/cap_p7.png`, `c1/paginas/cap_p22.png`, `c1/paginas/cap_p23.png`
- Texto heredado: [encabezado S2] Sección 2. Capital mínimo por riesgo de crédito. / [chapeau_seccion S2] A los efectos de la aplicación de las disposiciones de la presente sección, las entidades financieras se clasificarán en: i)Grupo 1: entidades calificadas por el BCRA como de importancia sistémica a nivel local / [chapeau_seccion S2] (D-SIB) y sucursales o subsidiarias de bancos del exterior calificados como de impor- tancia sistémica global (G-SIB). / [chapeau_seccion S2] ii) Grupo 2: entidades financieras no comprendidas en el acápite i). En aquellos casos en que no se establezcan disposiciones específicas para cada uno de los citados grupos de entidades financieras, deberá aplicarse el mismo tratamiento a ambos grupos. Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto en los acápites precedentes–, contarán con un plazo de 6 meses para aplicar las disposiciones específicas correspondientes al nuevo grupo al que pertenezcan. / [encabezado 2.12] 2.12. Tabla de ponderadores de riesgo. / [intro 2.12] Concepto Ponderador / [intro 2.12] –en %– / [encabezado 2.12.2] 2.12.2. Exposición a gobiernos y bancos centrales.
- Texto propio:

```text
2.12.2.3. Al sector público no financiero por financiaciones otorgadas a
beneficiarios de la seguridad social o a empleados públicos –en
ambos casos, con código de descuento–, en la medida que di-
chas operaciones estén denominadas en pesos, la fuente de
fondos sea en esa moneda y las cuotas de todas las financia-
ciones de la entidad que cuenten con sistema de amortización
periódica no excedan, al momento de los acuerdos, del 30% de
los ingresos del deudor y/o, en su caso, de los codeudores. 0
```

## F34 — correcta (→ Operacion)

- Nota de C2: 2.2.3: «En caso de que se trate de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación se computará el equivalente en dicha moneda del monto acreditado». El supuesto es antecedente del tratamiento que el destino describe («Se computa el equivalente en dicha moneda del monto acreditado», en su descripción). Anotación: mismo tramo en la Condicion y en el destino (circular por etiqueta y tramo), mismo patrón y misma unidad que otra ficha de la muestra; con una lectura estricta del nodo por su etiqueta sería incorrecta: queda para la adjudicación.
- Anotaciones: circular: el destino tiene el mismo tramo que la Condicion; la consecuencia del texto está solo en su descripción
- Origen: Condicion — «Servicios a residentes paraguayos o uruguayos en moneda de destino» (`Condicion_servicios_a_residentes_paraguayos_o_uruguayos_en_moneda_de_destino__supuesto_en__1ff0ec`)
  - descripción (salida del extractor): Supuesto en que se trata de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación
  - tramo de E1 (salida del extractor): 'En caso de que se trate de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación'
- Destino: Operacion — «Ingreso de cobros servicios a residentes paraguayos o uruguayos» (`Operacion_ingreso_de_cobros_servicios_a_residentes_paraguayos_o_uruguayos__ext_2_2_3_c85cb5`)
  - descripción (salida del extractor): Ingreso de cobros de servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación. Se computa el equivalente en dicha moneda del monto acreditado.
  - tramo de E1 (salida del extractor): 'servicios prestados a residentes paraguayos o uruguayos facturados en la moneda del país de destino de la exportación'
- Unidad `ext::2.2.3` (ext, punto 2.2.3), páginas [11]; PDF `data/experiment/subset/TO_exterior_cambios_actual.pdf`; render `c1/paginas/ext_p11.png`
- Texto heredado: [encabezado S2] Sección 2. Disposiciones específicas para los ingresos por el mercado de cambios. / [encabezado 2.2] 2.2. Cobros de exportaciones de servicios.
- Texto propio:

```text
2.2.3. En el caso de que los cobros sean ingresados a través del sistema de monedas
locales se considerará cumplimentada la liquidación por el monto acreditado en
moneda nacional en la cuenta del exportador. En caso de que se trate de servicios
prestados a residentes paraguayos o uruguayos facturados en la moneda del país de
destino de la exportación se computará el equivalente en dicha moneda del monto
acreditado.
```

## F45 — correcta (→ Operacion)

- Nota de C2: 8.2.1 y 8.2.1.1: motivo de inclusión en la Central, «Haber incurrido en uno o varios rechazos de cheques […] por: Falta de fondos suficientes disponibles en cuenta o de autorización para girar en descubierto». La falta de autorización es la causa del rechazo y el texto la enuncia como tal. Anotación: el consecuente que regula el texto es la inclusión en la Central, que no es nodo de la arista; la Condicion toma solo uno de los dos términos («fondos» o «autorización»).
- Anotaciones: consecuencia fuera de la arista: el texto regula la inclusión en la Central; condicion parcial: uno de dos términos
- Origen: Condicion — «Falta de autorización para girar en descubierto» (`Condicion_falta_de_autorizacion_para_girar_en_descubierto__supuesto_de_inclusion_en_la_cen_d4a9c1`)
  - descripción (salida del extractor): Supuesto de inclusión en la Central de cheques rechazados: falta de autorización para girar en descubierto
  - tramo de E1 (salida del extractor): 'falta de autorización para girar en descubierto'
- Destino: Operacion — «Rechazo de cheques por falta de fondos o autorización» (`Operacion_rechazo_de_cheques_por_falta_de_fondos_o_autorizacion__ctacte_8_2_1_1_6433fa`)
  - descripción (salida del extractor): Rechazo de cheques comunes o de pago diferido por falta de fondos suficientes disponibles en cuenta o por falta de autorización para girar en descubierto
  - tramo de E1 (salida del extractor): 'rechazos de cheques -comunes o de pago diferido- por: [...] Falta de fondos suficientes disponibles en cuenta o de autorización para girar en descubierto'
- Unidad `ctacte::8.2.1.1` (ctacte, punto 8.2.1.1), páginas [44]; PDF `data/experiment/escalado_prep/pdfs/ctacte.pdf`; render `c1/paginas/ctacte_p44.png`
- Texto heredado: [encabezado S8] Sección 8. “Central de cheques rechazados”, “Central de cuentacorrentistas inhabili- tados” y “Central de cheques denunciados como extraviados, sustraídos o adulterados”. / [encabezado 8.2] 8.2. Motivos de inclusión. / [encabezado 8.2.1] 8.2.1. En la “Central de cheques rechazados”. / [intro 8.2.1] Haber incurrido en uno o varios rechazos de cheques -comunes o de pago diferido- por:
- Texto propio:

```text
8.2.1.1. Falta de fondos suficientes disponibles en cuenta o de autorización para girar en
descubierto.
```

## F60 — correcta (→ Potestad)

- Nota de C2: 5.2: «Las entidades financieras podrán mantener en bancos del exterior […] certificados de depósito a plazo fijo en entidades que cuenten con calificación internacional no inferior a “AA”». La calificación restringe en qué entidades rige la facultad; reformula parte de la definición del destino (anotación, como en las condiciones de alcance).
- Anotaciones: alcance: la Condicion reformula parte de la definición del destino
- Origen: Condicion — «Calificación internacional mínima AA» (`Condicion_calificacion_internacional_minima_aa__las_entidades_en_las_que_se_colocan_certif_90e08f`)
  - descripción (salida del extractor): Las entidades en las que se colocan certificados de depósito a plazo fijo deben contar con calificación internacional no inferior a AA.
  - tramo de E1 (salida del extractor): 'entidades que cuenten con calificación internacional no inferior a "AA"'
- Destino: Potestad — «Mantener certificados de depósito a plazo fijo en entidades calificadas» (`Potestad_mantener_certificados_de_deposito_a_plazo_fijo_en_entidades_calificadas__las_ent_1f6417`)
  - descripción (salida del extractor): Las entidades financieras quedan autorizadas a mantener certificados de depósito a plazo fijo en entidades que cuenten con calificación internacional no inferior a AA.
  - tramo de E1 (salida del extractor): 'certificados de depósito a plazo fijo en entidades que cuenten con calificación internacional no inferior a "AA"'
- Unidad `polcre::5.2` (polcre, punto 5.2), páginas [13]; PDF `data/experiment/escalado_prep/pdfs/polcre.pdf`; render `c1/paginas/polcre_p13.png`
- Texto heredado: [encabezado S5] Sección 5. Financiamiento a residentes en el exterior.
- Texto propio:

```text
5.2. Colocaciones en bancos del exterior.
Las entidades financieras podrán mantener en bancos del exterior cuentas de corresponsalía y
cuentas a la vista necesarias para sus operaciones, de acuerdo con lo establecido en las nor-
mas sobre “Cuentas de corresponsalía” y certificados de depósito a plazo fijo en entidades que
cuenten con calificación internacional no inferior a “AA”.
```

