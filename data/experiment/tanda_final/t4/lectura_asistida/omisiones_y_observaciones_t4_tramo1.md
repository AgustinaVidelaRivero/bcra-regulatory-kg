# Omisiones y observaciones de la lectura asistida, T4 de la tanda final, primer tramo

Lo que va aparte del veredicto: no cambia ninguna propuesta (las propuestas y sus criterios están en `lectura_asistida_t4_tramo1.json`). Las omisiones son contenido del texto sin nodo o sin relación; las observaciones, lo que noté en la ficha y no decide la propuesta. Por muestra y por ficha, con el número del encabezado «## n.» de su `.md`.

## cola (30 fichas; `cola.csv`)

- **2.** `ri_dsf::S8::chapeau_seccion` — omisión: 2.1.6 (los saldos de capital e intereses por tipo de garantía), 2.1.7 (la deuda vencida en situación 3 o 4) y 6.3 (el incremento de previsión) no tienen nodo. observación: El bloque chapeau de S8 trae el texto de B. «Datos sobre la asistencia al deudor» (puntos 1 a 8 de otra sección): la extracción lo sigue.
- **3.** `ri_iepsp::A::S4` — observación: Quien ejecuta las verificaciones es el contador que emite el informe; la extracción no tiene ese sujeto y modela los procedimientos como operaciones que aplican a la Sociedad.
- **4.** `ri_ii_31_12_19::2.20` — omisión: El dato a informar (el domicilio especial de los directivos) no tiene nodo; la extracción lo deja al encabezado S2.
- **6.** `ri_tar::4.1.2` — observación: La omisión que anota el extractor («la totalidad de marcas») no está en el texto que muestra la ficha.
- **7.** `ri_msrl::6.2` — omisión: Las filas de los subcódigos (212100 a 212300, 221100 a 221230, 231100 a 231300, 250910 a 250960, 251100, 251200, 252100 a 252220, 252231 a 252233, 253100 a 253300) quedan solo dentro de las descripciones.
- **8.** `ri_msrl::S1` — observación: e2 lee «El presente requerimiento deberá ser cumplido por las entidades… “internacionalmente activas”» como cumplimiento del LCR; el requerimiento es el informativo.
- **9.** `cedin::12.1` — observación: La subclase `comunicacion_a_cliente` de e1 y e4 no es la dirección del aviso (del tenedor a la entidad, de la entidad a la autoridad); la tomo como la más cercana del vocabulario.
- **11.** `consyr::3.4.4` — observación: e2 no tiene aplica_a (el texto no nombra al obligado más que por «los funcionarios designados»).
- **12.** `seggar::3.3.2` — observación: e1 describe la operación como «Determinación del capital mínimo exigido»; el texto da un indicador de la calidad de la cartera (activos ponderados respecto de los activos totales).
- **13.** `seggar::8.2` — observación: Las exclusiones de la cobertura del artículo 12 van como Restriccion con subclase `prohibicion`; el texto las formula como alcance («No están alcanzados por la cobertura»), no como prohibición de una conducta.
- **17.** `ratiofn::5.1.6` — omisión: El factor del 90 % no tiene propiedad ni nodo.
- **20.** `cateloc::Sbloque6` — omisión: La categoría de cada localidad del cuadro no tiene nodo.
- **23.** `raapal::2.2.3.1` — observación: c6 a c8 describen cada supuesto de «E* será igual a 0 si:» como suficiente por sí solo; el texto los enumera sin decir si se suman.
- **28.** `ctavis::2.1.1.1` — omisión: El dato que deben contener las boletas no tiene nodo; la extracción lo deja a la introducción de 2.1.1.
- **29.** `cateloc::Sbloque5` — omisión: La categoría de cada localidad del cuadro no tiene nodo.
- **30.** `finsec::6.3.3.2` — omisión: Las fórmulas del VaR y los ponderadores A, B y C no tienen nodo. observación: e3, e5 y e7 son Condicion para requisitos que el texto escribe con «deberá» («deberá cumplirse al concertarse la operación», «Deberán corresponder a un período de 30 días»); los tomo como requisitos de elegibilidad de los activos y de las tasas, no como deberes de conducta.

## aceptadas ítems (30 fichas; `aceptadas_items.csv`)

- **2.** `ri_sef::P1::S14` — observación: La mención «las entidades» no está en el texto (mención no verificada, en cuarentena).
- **3.** `ri_sef::P1::11.11` — observación: N1 (Definicion) y N2 (Obligacion) salen del mismo tramo y dicen lo mismo.
- **4.** `ri_sef::P1::11.5` — omisión: El dato a informar (la esquina del domicilio) no tiene nodo.
- **5.** `ri_sef::P1::11.13` — observación: «Integrar en la solicitud… de la unidad de servicio» sale del encabezado de la sección, que esta ficha no muestra.
- **9.** `ri_dsf::2.1` — omisión: «otros entes mencionados en el último párrafo del punto precedente» no tiene aplica_a: la mención va solo a las entidades financieras.
- **10.** `ri_sef::P1::11.8` — omisión: El dato a informar (la localidad del domicilio) no tiene nodo.
- **11.** `ri_sef::P1::11.1` — omisión: El dato a informar (la calle del domicilio) no tiene nodo.
- **20.** `cedin::13.2.3` — observación: La descripción de N1 («Pago por el desempeño de tareas vinculadas a los CEDIN») se lee como la comisión; el concepto es el pago del certificado.
- **22.** `snp_spd::5.5.4.3` — omisión: La responsabilidad de la billetera por el fraude en pagos con QR, que la excepción exceptúa, no tiene nodo ni relación.
- **25.** `depinv::1.17.1.1` — observación: La mención resuelta («otras entidades financieras») es la del depositante; la prohibición es de la entidad que recibe el depósito, que también es entidad financiera.
- **27.** `snp_psp::5.1.2.4` — observación: La mención resuelta («Todo PSP que deba inscribirse como aceptador») no está en el texto que muestra la ficha.

## aceptadas no ítems (30 fichas; `aceptadas_no_items.csv`)

- **1.** `ri_acsf::Sbloque2` — observación: La mención «las entidades» no está en el texto (mención no verificada, en cuarentena).
- **2.** `ri_ii_31_12_19::1.2` — omisión: El dato a informar (el CUIT de la entidad) no tiene nodo.
- **4.** `ri_iesinap::S2` — omisión: «Los sujetos referidos» no tiene aplica_a, y la excepción no tiene la relación con el deber que exceptúa.
- **5.** `ri_secoexpo::Sbloque8` — observación: N1 es una Condicion para «el número de destinación y/o CUIT a consignarse son aquellos que constan en el Reporte»: es una especificación del dato, sin deber explícito ni supuesto.
- **6.** `ri_ii_31_12_19::2.1` — observación: Las tres Definicion dan, por clase de persona, con qué documento se identifica; no definen la clase.
- **14.** `ri_tsa::3.3.2` — observación: N2 dice que el FER es «Componente de la categoría FED»: lo toma del encabezado de la columna, que el texto pone igual para las dos filas.
- **15.** `ri_ai::6.1` — omisión: La admisión de los excesos («no constituirán incumplimientos») no tiene nodo.
- **20.** `seggar::5.2.7` — observación: La etiqueta («post-compresión regulatoria») no es del texto; la descripción sí.
- **22.** `ratio::6.2.5.2` — omisión: Las cinco exclusiones no tienen relación con la operación que exceptúan.
- **27.** `adfsp::4.2.4` — omisión: «el plazo máximo… comenzará a partir de la fecha de la primera acreditación» queda solo en la descripción de N2, sin nodo propio; «dejando constancia de ello en el legajo» no tiene nodo.
- **28.** `retype::1.6` — observación: N1 (Obligacion) y N2 (Operacion) tienen la misma descripción.

## vigilancia (2) (30 fichas; `vigilancia_2.csv`)

- Ninguna.

## vigilancia (7) (6 fichas; `vigilancia_7.csv`)

- **1.** `Sujeto_rol_alcance_snp_tr_nc | ejecuta | Operacion_suspension_preventiva_de_procedimientos…` — observación: El rol de alcance es más amplio que el ejecutor que nombra el texto (el administrador del esquema).
- **6.** `Sujeto_rol_alcance_snp_spd | ejecuta | Operacion_solicitud_de_autorizacion_de_viaje_a_bill…` — observación: El rol de alcance es más amplio que el ejecutor que nombra el texto (el administrador QR).

## vigilancia (1) (30 fichas; `vigilancia_1.csv`)

- **17.** `Condicion_condicion_prestacion_de_ayuda_economica_excluida__la_prestacion_del_servicio_de_…` — observación: La relación va de la exclusión al tope de la tasa; en el texto el tope es una de las características de las que depende la exclusión.
- **21.** `Condicion_simultaneidad_con_habilitacion_punto_3_1__la_apertura_de_cuentas_corrientes_debe…` — observación: La descripción de la Condicion la reescribe como deber («debe realizarse simultáneamente»).
- **22.** `Condicion_denuncia_de_extravio_sustraccion_o_adulteracion__el_titular_o_tenedor_desposeido…` — observación: La descripción lo reescribe como deber («debe haber denunciado»).
- **24.** `Condicion_periodo_de_6_meses__durante_un_periodo_de_6_meses__fimipyme_11_1_3_8e1b07` — observación: Es un plazo, no un supuesto.
- **27.** `Condicion_calibracion_de_montos_estabilidad_y_liquidez_esperadas__los_montos_disponibles_y…` — observación: Tampoco es un supuesto: no es condición de ningún nodo.
- **28.** `Condicion_fallo_del_sistema_principal_de_apertura__la_puerta_de_emergencia_o_el_mecanismo_…` — observación: La Condicion no tiene la relación de condición con el deber de contar con la puerta.
- **29.** `Condicion_plazo_minimo_180_dias__el_deposito_debe_tener_un_plazo_minimo_de_180_dias__depin…` — observación: Es un requisito de plazo (una restricción), no un supuesto; la descripción lo reescribe como «debe tener».
- **30.** `Condicion_incumplimiento_regularizado_duracion_en_meses__una_vez_regularizado_el_incumplim…` — observación: Es una duración, no un supuesto.

## vigilancia (3) (30 fichas; `vigilancia_3.csv`)

- **6.** `Operacion_compra_a_termino_moneda_extranjera_liquidable_en_pesos__ri_ot_13_4_5fdf5f|Operac…` — observación: Las dos descripciones son iguales; solo la etiqueta dice cuál es cuál.
- **18.** `Operacion_presentacion_del_cedin_ante_entidad_financiera__cedin_s5_9c8698|Potestad_present…` — observación: Las dos etiquetas son iguales.
- **26.** `Operacion_fondo_de_riesgo_disponible__socgar_2_1_1_c55b13|Restriccion_el_fondo_de_riesgo_d…` — observación: La descripción de N1 lleva también el 25 %.

## observación (12) (30 fichas; `observacion_12.csv`)

- **10.** `Obligacion_se_debe_informar_el_pais_de_residencia_del_accionista_ingresando_el_codigo_swif…` — observación: Las entidades cambiarias, que el encabezado también nombra, no tienen arista.
- **28.** `Restriccion_el_importe_de_la_inversion_a_plazo_no_podra_superar_2_veces_el_valor_total_de_…` — observación: Las personas jurídicas, que el texto también nombra, no tienen arista.
