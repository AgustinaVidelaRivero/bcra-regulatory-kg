# U-OMISIONES-COD, O2 — límites y residuos, caso por caso

Generado por `scripts/limites_md_O2.py` desde `salidas/`. Páginas: las de la unidad en la E0 r2b. Todo sale del grafo de diez de O2 (`710664e9`) salvo donde se dice. «sin leer»: no leí el caso. Ninguno sale de los grupos de la v7: los que quedan fuera de lo que corrige esta unidad van, como límite medido, al grupo 2.

## Grupo L: elementos que conservan la cuantía (6)

Decidido en la nota del 10/10/2026 al pie de la v7 (decisión 4): se conserva la cuantía y quedan como límite. El mecanismo es la lectura de esa nota.

| unidad | páginas | cuantía | tramo de E1 | mecanismo |
|---|---|---|---|---|
| `ext::3.5.3::intro` | [23] | «3 (tres) días hábiles» | «no mayor a los 3 (tres) días hábiles» | E0 corta el texto en «…a los 3» |
| `ext::7.8.5.2` | [94] | «2 (dos) años» | «vida promedia no inferior a 2 (dos) años» | «promedia» donde el texto dice «promedio» |
| `pro::2.3.5.1` | [15, 16] | «cinco (5) días hábiles» | «dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia» | E1 une el «dentro de:» del encabezado con el segundo guion |
| `cap::3.2.4` | [61, 62] | «1250 %» | «no podrá superar 1250 %» | la fórmula intercala «fondo» y el literal pierde el «%» |
| `ext::4.2::cierre` | [58] | «360 (trescientos sesenta) días corridos» | «no podrá tener un plazo de pago que exceda a los 360 (trescientos sesenta) días corridos» | «podrá» donde el texto dice «podrán» |
| `cap::5.3.2.1` | [106, 107] | «tres meses» | «plazo residual no mayor a tres meses» | E1 omite palabras |

## Grupo B, f: menciones que verifican sin el artículo inicial y siguen sin verificar (17 de 64)

El conjunto de R2-1, reconstruido, da 64 relaciones; pasan 47 (257 → 210 menciones sin verificar en `resolucion_sujetos.jsonl`). La expansión de contracciones solo alcanza al artículo «el» («del», «al»). «las entidades» es la expresión colectiva de R3.

| unidad | páginas | relación | mención | mecanismo |
|---|---|---|---|---|
| `ric::5.1.1` | [21, 22] | 16 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ric::5.1.1` | [21, 22] | 17 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ric::5.1.1` | [21, 22] | 18 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ric::5.1.1` | [21, 22] | 19 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `cap::8.6.1` | [169] | 7 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `cap::8.6.1` | [169] | 8 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `cap::8.6.1` | [169] | 9 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `cap::8.6.2` | [169] | 5 | «las entidades» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ext::7.9.3.1` | [97] | 3 | «la entidad financiera local» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ext::7.9.3.4` | [97] | 1 | «la entidad financiera local» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ext::7.9.3.5` | [98] | 6 | «la entidad financiera local» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ext::7.10.2.4` | [100, 101] | 22 | «La entidad financiera» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ext::7.10.2.4` | [100, 101] | 23 | «La entidad financiera» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ext::7.10.2.4` | [100, 101] | 24 | «La entidad financiera» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ctacte::3.1` | [20] | 3 | «los cheques» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `ctacte::3.1` | [20] | 4 | «los cheques» | artículo «la»/«las»/«los»: sin contracción que expandir |
| `lingob::2.3.2::intro` | [7] | 1 | «el Directorio» | sin leer |

## Grupo A, a: omisiones con el tramo en el orden de lectura, sin la marca (8)

| unidad | páginas | categoría | tramo | mecanismo |
|---|---|---|---|---|
| `ric::4.4::intro` | [16] | meta_normativo | «Información complementaria vinculada al cálculo de la exigencia por riesgo de mercado - Modelos de información» | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |
| `cap::2.12.10::intro` | [27] | meta_normativo | «conforme a lo previsto en la Sección 8.» | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |
| `cap::5.2.3::intro` | [100] | meta_normativo | «Requisitos para la aplicación de la técnica de cobertura mediante garantías (y contragarantías) personales y derivados de crédito» | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |
| `ext::3.4.4::intro` | [18] | meta_normativo | «El cliente encuadra en algunas de las siguientes situaciones y cumple la totalidad de las condiciones estipuladas en cada caso:» | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |
| `ext::7.9::intro` | [94] | meta_normativo | «Operaciones financieras habilitadas para aplicar cobros de exportaciones de bienes y servicios.» | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |
| `ext::9.3.10::intro` | [127] | meta_normativo | «Repatriaciones de aportes de inversión directa de no residentes en empresas que no controlantes de entidades financieras locales admitidas en los puntos 7.9. o » | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |
| `ext::14.2.1::intro` | [176] | meta_normativo | «En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2., según corresponda» | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |
| `pagjub::2.8.1::intro` | [9] | meta_normativo | «Presentación realizada y aceptada hasta el vencimiento del período de presentación y sin inconsistencias» | el tramo cruza el título y el texto propio del mini-chunk; no está solo en el heredado |

## Grupo A, d: entidades de T4 con un supuesto dentro que la marca no detecta (10)

| unidad | entidad | páginas | supuestos de T4 | mecanismo |
|---|---|---|---|---|
| `cap::2.1` | e19 | [7, 8, 9] | el cronograma opera desde que las obras se usan económicamente | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `cap::2.1` | e20 | [7, 8, 9] |  | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `cap::2.1` | e21 | [7, 8, 9] | el cronograma opera desde que las obras se usan económicamente | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `cap::3.1.11.3` | e6 | [44, 45] | mínimos por STC; look-through menor que el mínimo | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `cap::3.1.11.3` | e7 | [44, 45] | look-through menor que el mínimo | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `cap::3.1.11.3` | e8 | [44, 45] | mínimos por STC; look-through menor que el mínimo | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `cap::3.1.14.1` | e11 | [48, 49, 50, 51, 52, 53] | salvo el período de 2 años; condiciones a) a d); condiciones a) a d); condiciones a) a d); condiciones a) a d) | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `pro::2.3.5.1` | e10 | [15, 16] | por constatación | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `pro::2.3.5.1` | e9 | [15, 16] | plazo por reclamo | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |
| `pro::3.1.3` | e8 | [25, 26] | presentante que no recibe el número automáticamente | el supuesto no lleva un conector de la lista cerrada en la descripción ni en el tramo |

## Grupo A, e: la pieza aparte

No está aplicada (`pieza_e/`). Entra solo si la lectura a ciegas de sus 16 detecciones fuera de las 64 unidades de T4 llega al piso: límite inferior de Wilson al 95 % de 0,75 o más sobre las decididas, con las dudosas excluidas (al menos 12 decididas, todas correctas). Si no llega, (e) queda como límite declarado. Mientras tanto, en el conjunto de diseño de T4:

| caso T4 | unidad | páginas | clase de T4 | razón de T4 | mecanismo |
|---|---|---|---|---|---|
| 3 | `pro::2.3.1.1` | [7, 8, 9] | copia real | ausente «cómputo» (la unidad no tiene ninguna forma de computar) | la palabra que trae la nota es una derivación que la tolerancia de flexión toma como presente |
| 29 | `ext::2.7::cierre` | [14] | copia real | ausente «cómputo» («computados» es otra palabra, derivada) | la palabra que trae la nota es una derivación que la tolerancia de flexión toma como presente |
| 44 | `ext::3.5.4::intro` | [25] | copia real | ausente «vigencia» (la norma dice «vigente»): el mismo caso que el 19 de P3b-2 | la palabra que trae la nota es una derivación que la tolerancia de flexión toma como presente |
| 5 | `cla::3.3.2` | — | coincidencia legítima | «el manual de procedimientos de» es la frase de la norma | sin leer |
| 43 | `ext::3.5.4.3` | — | coincidencia legítima | remite al 3.5.4 por su número, como su encabezado («3.5.4. En la medida que…») | sin leer |
| 52 | `ext::4.6.1::intro` | — | coincidencia legítima | «el equivalente en moneda local», de la norma | sin leer |
| 57 | `ext::7.1.1.3` | — | coincidencia legítima | «los capítulos 26 y 71», literal | sin leer |

## Grupo H: Comunicacion con `tipo_no_derivable` (26 en diez)

Quedan como error de extracción declarado (v7). El código y la etiqueta no nombran una Comunicación ni una norma externa (una remisión a un punto o una sección, o el nombre de un TO u otro documento). En el sin cola de diez son 25 (todas menos `Comunicacion_grandes_exposiciones_al_riesgo_de_credito`); en desarrollo, con y sin cola, 18, todas de esta lista.

| nodo | código | unidades |
|---|---|---|
| `Comunicacion_5_3_2_3` | «5.3.2.3» | cap::5.3.2::intro |
| `Comunicacion_6_6_2` | «6.6.2» | cap::6.1.4.2 |
| `Comunicacion_6_6_3` | «6.6.3» | cap::6.1.4.2 |
| `Comunicacion_8_3_5_1` | «8.3.5.1» | cap::8.3.5.3 |
| `Comunicacion_8_3_5_2` | «8.3.5.2» | cap::8.3.5.3 |
| `Comunicacion_autorizacion_y_composicion_del_capital_de_entidades_financieras` | «Autorización y composición del capital de entidades financieras» | cap::8.6::cierre |
| `Comunicacion_capitales_minimos_de_las_entidades_financieras` | «Capitales mínimos de las entidades financieras» | ric::4.1.1.2 |
| `Comunicacion_distribucion_de_resultados` | «Distribución de resultados» | cap::8.3.2.8 |
| `Comunicacion_financiamiento_al_sector_publico_no_financiero` | «Financiamiento al sector público no financiero» | polcre::4.1 |
| `Comunicacion_grandes_exposiciones_al_riesgo_de_credito` | «Grandes exposiciones al riesgo de crédito» | lingob::7.1.8 |
| `Comunicacion_normas_minimas_sobre_auditorias_externas` | «Normas Mínimas sobre Auditorías Externas» | cap::8.7 |
| `Comunicacion_normas_reglamentarias_dictadas_por_el_bcra` | «Normas reglamentarias dictadas por el BCRA» | ctacte::2.4, ctacte::2.5 |
| `Comunicacion_normas_sobre_grandes_exposiciones_al_riesgo_de_credito` | «Normas sobre Grandes exposiciones al riesgo de crédito» | polcre::7.1::cierre |
| `Comunicacion_previsiones_minimas_por_riesgo_de_incobrabilidad` | «Previsiones mínimas por riesgo de incobrabilidad» | cap::8.4.1.13 |
| `Comunicacion_principios_para_las_infraestructuras_del_mercado_financiero` | «Principios para las Infraestructuras del Mercado Financiero» | ctacte::12.8.2 |
| `Comunicacion_proteccion_de_los_usuarios_de_servicios_financieros` | «Protección de los usuarios de servicios financieros» | ctacte::1.5.2.10 |
| `Comunicacion_punto_3_1` | «Punto 3.1» | cap::5.4.3 |
| `Comunicacion_punto_3_5` | «punto 3.5» | ext::2.2.4 |
| `Comunicacion_punto_7_9` | «punto 7.9» | ext::2.2.4 |
| `Comunicacion_puntos_3_6_1_3_a_3_6_1_5` | «puntos 3.6.1.3. a 3.6.1.5» | ext::2.2.4 |
| `Comunicacion_seccion_2` | «Sección 2» | cap::5.3.2::intro |
| `Comunicacion_seccion_5` | «Sección 5» | cap::2.5.11, cap::6.1.3.4 |
| `Comunicacion_seccion_6` | «Sección 6» | ctacte::3.5.4 |
| `Comunicacion_sefyc` | «SEFyC» | cla::3.6 |
| `Comunicacion_standard_for_automatic_exchange_of_financial_account_information_common_reporting_standard` | «Standard for Automatic Exchange of Financial Account Information-Common Reporting Standard» | ctacte::12.7.1::cierre |
| `Comunicacion_to_sobre_comunicacion_por_medios_electronicos_para_el_cuidado_del_medio_ambiente` | «TO sobre Comunicación por Medios Electrónicos para el Cuidado del Medio Ambiente» | pro::2.7.2 |

## Grupo C: los 264 elementos con base (11 resueltas, 177 marcadas y 76 sin base)

Por estado y origen: {'marcada|descripcion': 19, 'marcada|e1': 80, 'marcada|validador': 78, 'resuelta|descripcion': 1, 'resuelta|e1': 7, 'resuelta|validador': 3, 'sin_base|validador': 76}. Las marcadas quedan como límite declarado de la v7 (base no resuelta); las sin base son los límites relativos del validador cuya «base» no es una base (g1), sin marca.

### Las resueltas

| unidad | origen | destino | vía | lectura |
|---|---|---|---|---|
| `cla::3.3.3` | e1 | `cla::3.7` | remision | una de las 7 correctas de la v7 |
| `cla::5.1.1.1` | e1 | `cla::3.7` | remision | una de las 7 correctas de la v7 |
| `cla::6.3.2` | e1 | `cla::3.7` | remision | una de las 7 correctas de la v7 |
| `ext::13.4.6` | descripcion | `ext::4.4` | remision | leído en O2: la base es «total pendiente por sus deudas elegibles para los puntos 4.4. y 4.5.» (p. 172). Resuelve al primero de los dos puntos y la base es un monto, no la unidad citada: correcta solo en parte. Ya estaba así en `a9631a64`; queda como límite medido, para el grupo 2 |
| `ext::3.14.4` | validador | `ext::3.8` | remision | nueva (g), caso positivo de la v7 |
| `cap::3.2.1.1` | e1 | `Definicion_ponderador_de_riesgo__porcentaje_de_ponderacion_de_riesgo_aplicable_a_conceptos__669a3d` | definicion | una de las 7 correctas de la v7 |
| `ext::14.2.3` | validador | `ext::14.2.2` | remision | nueva (g), caso positivo de la v7 |
| `cla::5.1.2.3` | e1 | `cla::3.7` | remision | una de las 7 correctas de la v7 |
| `ext::3.18.2.4` | validador | `ext::3.18.3` | remision | nueva (g), caso positivo de la v7 |
| `cap::4.2.1.2::parte1` | e1 | `Definicion_epf_exposicion_potencial_futura__exposicion_potencial_futura_calculada_de_acuerd_c22b93` | definicion | una de las 7 correctas de la v7 |
| `polcre::2.1.9` | e1 | `Definicion_capacidad_de_prestamo_determinacion__se_determinara_por_cada_moneda_extranjera_c_230df1` | definicion | una de las 7 correctas de la v7 |

### Las marcadas (177)

| unidad | origen | base en HEAD | cuantía |
|---|---|---|---|
| `ext::3.11.2.3` | e1 | «monto que se cancelará» | 20 porcentaje |
| `ext::3.11.2.3` | e1 | «monto que se cancelará» | 10 porcentaje |
| `ext::8.4.4` | validador | «alcanzar el total del monto a ingresar y liquidar» | None None |
| `ext::3.18.2.1` | validador | «valor FOB de sus exportaciones para ese mismo conjunto de bienes embarcadas en todo el año t-1» | None None |
| `ext::10.10.2::cierre` | e1 | «valor FOB total» | 90 porcentaje |
| `cla::6.5::intro` | validador | «importe resultante de aplicar sobre el saldo de deuda registrado en el sistema financiero» | None None |
| `cap::8.3.2.12` | e1 | «APR» | 5.125 porcentaje |
| `cap::6.11` | e1 | «RPC registrada al último día del segundo mes anterior» | 25 porcentaje |
| `cla::6.3.2` | descripcion | «importe total de la cartera comercial comprendida» | 50 porcentaje |
| `ext::7.1.1.3` | validador | «monto indicado en el punto precedente» | None None |
| `cla::6.5.4.5` | descripcion | «obligaciones refinanciadas y totalidad de intereses)» | 10 porcentaje |
| `ext::10.10.2.2` | e1 | «valor FOB» | 80 porcentaje |
| `ext::10.10.2.2` | e1 | «valor FOB» | 30 porcentaje |
| `cla::7.2.3` | e1 | «importe involucrado en el citado acuerdo» | 10 porcentaje |
| `ext::3.5.1.6` | descripcion | «valor de capital canjeado o recomprado» | 5 porcentaje |
| `ext::7.5.2` | validador | «porcentaje mínimo requerido del anticipo» | None None |
| `ric::11.1.1` | e1 | «activos o pasivos de la cartera de inversión» | 5 porcentaje |
| `cap::5.4.2` | validador | «monto de la exposición al riesgo» | None None |
| `cla::7.1` | validador | «asignado por la entidad» | None None |
| `ext::7.3.11` | validador | «porcentaje mínimo requerido de la operación» | None None |
| `ext::9.3.1.2` | validador | «saldo liquidado pendiente de aplicación» | None None |
| `ext::14.3.1` | validador | «suma de sus aportes de inversión directa» | None None |
| `ext::3.6.4.6` | validador | «monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela» | None None |
| `ext::8.5.8` | validador | «valor indicado» | None None |
| `ext::4.8.5` | e1 | «total pendiente por sus deudas elegibles» | 25 porcentaje |
| `ext::3.4.2` | validador | «monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas» | None None |
| `ext::9.3.12.2` | validador | «monto en moneda local que les corresponda según la distribución determinada por la asamblea de accionistas» | None None |
| `cla::6.5.4.7` | e1 | «patrimonio» | 20 porcentaje |
| `cla::6.5.4.7` | e1 | «patrimonio» | 20 porcentaje |
| `ext::4.8.2` | validador | «monto adquirido en la suscripción primaria» | None None |
| `cla::6.5.5.2` | e1 | «obligaciones refinanciadas» | 15 porcentaje |
| `cla::6.5.3.5` | e1 | «obligaciones refinanciadas» | 5 porcentaje |
| `ext::10.6.1` | validador | «valor del bien importado» | None None |
| `cla::7.2.3` | e1 | «sus obligaciones refinanciadas (por capital)» | 5 porcentaje |
| `ext::7.5.5.1` | e1 | «valor del permiso de embarque provisorio» | 85 porcentaje |
| `ext::14.5.3` | validador | «monto total de la financiación» | None None |
| `ric::8.1.2` | e1 | «nivel de capital 1» | 15 porcentaje |
| `ext::3.13.1.10` | e1 | «capital» | 10 porcentaje |
| `ext::7.10.6` | validador | «previsto en el presente punto» | None None |
| `ext::4.8.2` | validador | «diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos» | None None |
| `cap::6.6.1` | e1 | «su RPC del mes anterior» | 5 porcentaje |
| `ext::9.3.3.2` | descripcion | «valor de las nuevas liquidaciones» | 75 porcentaje |
| `ext::7.10.2.1` | descripcion | «monto en divisas del permiso de exportación» | 20 porcentaje |
| `ext::3.6.4.5` | validador | «vida promedio remanente» | None None |
| `ext::3.6.4.6` | validador | «vida promedio remanente» | None None |
| `ext::3.13.1.12` | validador | «equivalente de ese monto» | None None |
| `cla::7.1` | validador | «límite de la asistencia máxima que le haya sido acordada por todo concepto» | None None |
| `ext::7.9.1.9` | validador | «excedente» | None None |
| `ext::7.9.1.9` | validador | «excedente» | None None |
| `ext::7.9.1.9` | validador | «excedente» | None None |
| `ext::7.9.1.9` | validador | «excedente» | None None |
| `ext::13.4.7` | descripcion | «deudas elegibles antes del 31/01/24» | 25 porcentaje |
| `ext::3.5.1.12` | validador | «excedente» | None None |
| `ext::7.7` | validador | «que se precancela a la entidad financiera local» | None None |
| `cla::6.5.5.2` | descripcion | «obligaciones refinanciadas)» | 15 porcentaje |
| `ric::12.3` | descripcion | «resultados provenientes de los ajustes NIIF no constituirán incumplimientos si se verifican las condiciones especificadas» | 100 porcentaje |
| `ext::3.3.3.4` | validador | «monto de intereses» | None None |
| `cap::2.9.2.3` | validador | «valor considerado en oportunidad del otorgamiento del crédito debidamente actualizado» | None None |
| `ext::14.5.3` | e1 | «valor FOB total pagado» | 90 porcentaje |
| `cap::5.2.3.3` | e1 | «valor de la cobertura» | 60 porcentaje |
| `cap::5.2.3.3` | e1 | «valor de la obligación subyacente» | 60 porcentaje |
| `cap::8.2.1.6` | descripcion | «resultados registrados hasta el último estado financiero trimestral o anual» | 100 porcentaje |
| `cap::6.11` | e1 | «exigencia» | 3 porcentaje |
| `cla::6.4.1` | e1 | «responsabilidad patrimonial computable de la entidad o del activo del fideicomiso financiero» | 1 porcentaje |
| `cla::6.4.4` | descripcion | «total informado» | 40 porcentaje |
| `cla::6.4.2` | descripcion | «total informado» | 10 porcentaje |
| `ext::7.10.6` | validador | «previsto en el presente punto» | None None |
| `cap::9.2` | descripcion | «propiedad» | 100 porcentaje |
| `cla::6.4.3` | e1 | «responsabilidad patrimonial computable» | 1 porcentaje |
| `cla::7.3` | validador | «en la categoría inmediata superior» | None None |
| `cla::7.3` | e1 | «total informado por todos los acreedores» | 40 porcentaje |
| `cla::3.4.4` | e1 | «responsabilidad patrimonial computable» | 1 porcentaje |
| `pro::2.3.5.1` | e1 | «tasa promedio» | 1.5 veces |
| `ext::3.4.4.4` | descripcion | «monto liquidado» | 30 porcentaje |
| `ext::10.9.4` | validador | «valor de los pagos realizados por la obligación con el exterior» | None None |
| `ext::8.5.19.1` | e1 | «valor facturado» | 25 porcentaje |
| `ctacte::5.5.8` | validador | «tanto el girado preste conformidad al cheque librado a su cargo» | None None |
| `cla::6.6` | validador | «en la categoría inmediata superior» | None None |
| `cla::3.5.2` | e1 | «responsabilidad patrimonial computable de la entidad del mes anterior al de la clasificación» | 1 porcentaje |
| `cla::3.5.2` | e1 | «cartera activa total» | 20 porcentaje |
| `cap::6.5.3.2` | e1 | «posición bruta» | 3 porcentaje |
| `cap::6.11` | descripcion | «RPC deben definir las responsabilidades en el manejo de la política de administración del riesgo de mercado» | 25 porcentaje |
| `ext::4.8.2` | validador | «diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de bonos BOPREAL adquiridos» | None None |
| `ext::4.8.2` | validador | «monto adquirido en la suscripción primaria» | None None |
| `ext::7.9.5` | descripcion | «servicios por capital e intereses deben ser ingresados y liquidados en el mercado de cambios dentro de los plazos previstos» | 125 porcentaje |
| `pro::2.2.2` | e1 | «total de los equipos instalados» | 10 porcentaje |
| `cla::7.2.3` | e1 | «garantías adicionales» | 50 porcentaje |
| `cla::6.5.4.5` | e1 | «obligaciones refinanciadas» | 10 porcentaje |
| `lingob::S8` | validador | «alcanzar la paridad de género» | None None |
| `cap::2.9.2.3` | validador | «valor considerado en oportunidad del otorgamiento del crédito debidamente actualizado» | None None |
| `ext::7.9.1.2` | validador | «monto que surge de restar el valor de los beneficios del Decreto 277/22» | None None |
| `cap::5.2.3.3` | e1 | «valor de la cobertura» | 60 porcentaje |
| `cap::5.2.3.3` | e1 | «valor de la obligación subyacente» | 60 porcentaje |
| `ext::4.1.3.1` | validador | «tipo de cambio vendedor» | None None |
| `ric::8.1.2` | e1 | «nivel de capital 1» | 15 porcentaje |
| `cap::8.4.1.19` | e1 | «ganancias» | 50 porcentaje |
| `ext::3.17.1::intro` | validador | «monto de la certificación» | None None |
| `ext::3.18.1::intro` | validador | «monto de la certificación» | None None |
| `pro::2.3.12.2` | validador | «que la compañía de seguros elegida perciba por operaciones con particulares y sin la intervención del sujeto obligado» | None None |
| `cla::6.5.4.7` | descripcion | «patrimonio» | 20 porcentaje |
| `cla::6.5.4.7` | descripcion | «patrimonio cuando persista el pedido de quiebra luego de» | 20 porcentaje |
| `polcre::2.1.14` | validador | «importe equivalente a un tercio del total de las aplicaciones realizadas» | None None |
| `pro::2.3.2.1` | validador | «que el tercero prestador perciba de particulares» | None None |
| `cap::1.4.2.1` | validador | «nivel que haya alcanzado durante el mes en que se originó el incumplimiento» | None None |
| `ext::9.3.10.5` | validador | «monto del aporte oportunamente ingresado y liquidado en el mercado de cambios» | None None |
| `ext::3.6.4.3` | validador | «monto que hubieran acumulado los vencimientos de capital del título canjeado» | None None |
| `ext::3.6.4.2` | validador | «monto que hubieran acumulado los vencimientos de capital de la financiación a precancelar» | None None |
| `ext::3.6.4.5` | validador | «monto que hubieran acumulado los vencimientos de capital del título de deuda que se cancela» | None None |
| `ext::7.10.5` | e1 | «monto bruto de las divisas ingresadas» | 60 porcentaje |
| `ext::7.10.4` | e1 | «monto bruto de las divisas ingresadas» | 40 porcentaje |
| `ext::7.10.2.1` | e1 | «monto en divisas que corresponden al permiso de exportación» | 20 porcentaje |
| `ext::7.10.5` | e1 | «valor de los permisos embarcados» | 60 porcentaje |
| `ext::13.1.4` | validador | «monto de la deuda pendiente de pago» | None None |
| `ext::7.9.1.9` | e1 | «monto del capital que vencía» | 40 porcentaje |
| `cap::8.3.2.12` | e1 | «APR» | 5.125 porcentaje |
| `ext::3.17.3.3` | validador | «monto que surge de considerar el monto acumulado de los beneficios totales reconocidos al cliente por la Secretaría de Energía» | None None |
| `ext::4.8.4.3` | e1 | «monto total de los anticipos que se encuadraron en este mecanismo» | 10 porcentaje |
| `ext::11.1.1.2` | validador | «monto facturado según la condición de compra pactada» | None None |
| `ext::4.6.2::intro` | validador | «equivalente al monto en moneda local de las utilidades y dividendos cobrados desde el 01/09/19» | None None |
| `ext::3.4::cierre` | validador | «equivalente al monto en moneda local de las utilidades y dividendos pendientes de pago a accionistas no residentes» | None None |
| `ext::4.6.1::intro` | validador | «equivalente al monto en moneda local de las utilidades y dividendos pendientes de pago a accionistas no residentes» | None None |
| `ext::4.5::intro` | validador | «monto de la deuda pendiente de pago» | None None |
| `ext::4.7::intro` | validador | «suma adeudada a la fecha de la suscripción» | None None |
| `ext::3.13.3` | validador | «equivalente al monto en moneda local de las utilidades y dividendos cobrados a partir del 01/09/19» | None None |
| `ext::7.10.4` | e1 | «valor de los permisos embarcados» | 40 porcentaje |
| `ext::3.11.1.4` | e1 | «monto previsto en el punto anterior» | 20 porcentaje |
| `ext::8.5.6` | validador | «monto proporcional a la relación entre el monto FOB total en divisas que figura en el despacho de reimportación de» | None None |
| `ext::4.8.4.1` | e1 | «monto suscripto de BOPREAL Serie 1» | 5 porcentaje |
| `ext::4.8.5` | e1 | «monto liquidado simultáneamente en concepto de cobros anticipados de exportaciones de bienes que serán cancelados con embarques cuyos cobros hubiera» | 50 porcentaje |
| `pro::2.3.13` | validador | «importe que la compañía de seguros elegida perciba por operaciones con particulares y sin la intervención del sujeto obligado» | None None |
| `cap::11.3` | e1 | «valor así obtenido» | 90 porcentaje |
| `cap::6.5.3.1` | e1 | «posición neta» | 15 porcentaje |
| `cap::2.11.3.5` | validador | «que le hubiera correspondido de haber permanecido en la cartera de créditos» | None None |
| `cap::8.4.1.2` | e1 | «PNb correspondiente al mes anterior» | 10 porcentaje |
| `ext::10.3.2.1` | validador | «monto facturado en la condición de compra pactada» | None None |
| `cap::2.8.3.4` | e1 | «ingresos del deudor» | 30 porcentaje |
| `cap::2.9.2.3` | validador | «precio de mercado» | None None |
| `ext::4.3.2.3` | validador | «diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de los bonos BOPREAL» | None None |
| `ext::4.8.3` | validador | «diferencia entre el valor obtenido por la venta con liquidación en moneda extranjera en el exterior de los bonos BOPREAL» | None None |
| `cap::2.9.2.3` | validador | «precio de adquisición» | None None |
| `cap::6.3.2.2` | e1 | «posición neta» | 2 porcentaje |
| `ext::7.9.5` | e1 | «servicios por capital e intereses a abonar en el mes corriente y los siguientes» | 125 porcentaje |
| `ext::7.8.5.1` | e1 | «servicios por capital e intereses a abonar en el mes corriente y los siguientes» | 125 porcentaje |
| `ext::7.11.5` | e1 | «capital e intereses a abonar en el mes corriente y los siguientes» | 125 porcentaje |
| `polcre::2.1::cierre` | validador | «valor que resulte de la siguiente expresión» | None None |
| `polcre::2.1.7` | validador | «valor que resulte de la siguiente expresión» | None None |
| `polcre::2.1.6` | validador | «valor que resulte de la siguiente expresión» | None None |
| `ext::7.10.2.3` | validador | «monto que surge de restar el valor de los beneficios del Decreto 277/22» | None None |
| `cla::6.5.5.9` | e1 | «responsabilidad patrimonial computable de la entidad del último día del mes anterior» | 2.5 porcentaje |
| `cap::3.1.12` | validador | «que le correspondería observar si mantuviera la totalidad de las exposiciones subyacentes» | None None |
| `cap::6.4.3` | e1 | «posición neta total» | 8 porcentaje |
| `cap::6.3.1` | e1 | «cada riesgo» | 8 porcentaje |
| `cap::6.3.1` | e1 | «cada riesgo» | 8 porcentaje |
| `cap::2.8.3.2` | e1 | «total de las exposiciones minoristas normativas de la entidad» | 0.2 porcentaje |
| `ext::10.10.2.2` | e1 | «valor FOB» | 80 porcentaje |
| `ext::10.10.2.2` | e1 | «valor FOB» | 30 porcentaje |
| `cap::2.12.2.3` | e1 | «ingresos del deudor» | 30 porcentaje |
| `ext::3.11.1.3` | validador | «valor a pagar en el próximo vencimiento de servicios» | None None |
| `cap::8.2.3.3` | e1 | «activos ponderados por riesgo de crédito» | 1.25 porcentaje |
| `polcre::2.6` | validador | «importe de dicho defecto» | None None |
| `ctacte::11.3` | e1 | «Tasa Mayorista de Argentina (TAMAR) total de bancos» | 1.5 veces |
| `ext::10.11.7.3` | validador | «equivalente al monto declarado en el referido padrón» | None None |
| `ext::4.8.5` | e1 | «monto total de los anticipos que se encuadraron en este mecanismo» | 10 porcentaje |
| `ctacte::6.5.1` | e1 | «valor rechazado» | 4 porcentaje |
| `cap::2.12.8.2` | e1 | «valor del inmueble» | 55 porcentaje |
| `cap::2.12.8.2` | e1 | «valor del inmueble» | 55 porcentaje |
| `cap::2.12.8.1` | e1 | «valor del inmueble» | 55 porcentaje |
| `cap::2.8.3.3` | e1 | «Salario Mínimo» | 75 veces |
| `cap::2.12.9.2` | e1 | «saldo pendiente» | 50 porcentaje |
| `cap::2.12.9.2` | e1 | «saldo pendiente» | 20 porcentaje |
| `cap::2.12.8.1` | e1 | «valor del inmueble» | 55 porcentaje |
| `cap::2.12.9.2` | e1 | «saldo pendiente» | 50 porcentaje |
| `polcre::6.2.1.4` | e1 | «ingresos computables» | 30 porcentaje |
| `cap::2.3.1` | descripcion | «previsión por riesgo de incobrabilidad correspondiente a las financiaciones que se encuentran cubiertas con garantías preferidas A» | 100 porcentaje |
| `cap::2.3.1` | descripcion | «importe de la previsión por riesgo de incobrabilidad correspondiente a la cartera de deudores clasificados en situación normal (puntos 6.5.1» | 100 porcentaje |
| `cap::6.2.2.5` | e1 | «menor de las posiciones compensadas» | 10 porcentaje |
| `ctacte::7.3.2.3` | validador | «dar cumplimiento a la obligación de presentar constancia de haber denunciado el hecho como delito» | None None |

### Las sin base (g1) (76)

| unidad | origen | base en HEAD | cuantía |
|---|---|---|---|
| `ext::3.3.3.4` | validador | «04/07/24» | None None |
| `ext::8.5.19.2` | validador | «30/09/23» | None None |
| `polcre::5.2` | validador | «"AA"» | None None |
| `docvig::3.5` | validador | «fecha de entrega de la primera chequera con los datos rectificados» | None None |
| `ext::8.5.19.2` | validador | «30/09/23» | None None |
| `cla::6.6` | validador | «un nivel» | None None |
| `cla::6.6` | validador | «otras dos entidades o fideicomisos financieros» | None None |
| `cap::6.2.1.2` | validador | «12» | None None |
| `ext::4.5::intro` | validador | «12/12/23» | None None |
| `cap::2.9.2.2` | validador | «4 unidades» | None None |
| `ext::13.2.5` | validador | «13/04/25» | None None |
| `ext::7.9.2.1` | validador | «dos tercios del incremento» | None None |
| `cla::7.3` | validador | «un nivel» | None None |
| `cla::7.3` | validador | «otras dos entidades» | None None |
| `polcre::2.2` | validador | «dos escenarios» | None None |
| `cap::10.3.2.3` | validador | «dos calificaciones» | None None |
| `ext::8.5.19::intro` | validador | «30/09/23» | None None |
| `ext::7.11.2.2` | validador | «12/12/23» | None None |
| `cap::11.5` | validador | «31/10/24» | None None |
| `cap::11.5` | validador | «10/04/26» | None None |
| `pagjub::2.7::cierre` | validador | «fecha límite» | None None |
| `ext::10.3.2.5` | validador | «12/12/23» | None None |
| `ext::11.1.1.5` | validador | «31/10/19» | None None |
| `ext::4.7::intro` | validador | «04/07/24» | None None |
| `ext::4.7::intro` | validador | «31/12/24» | None None |
| `ext::4.4::intro` | validador | «12/12/23» | None None |
| `cap::2.12.16` | validador | «25/11/21» | None None |
| `cap::4.2.1.2::parte2` | validador | «5.000» | None None |
| `ext::4.8.1.2` | validador | «12/12/23» | None None |
| `ext::3.14.5.1` | validador | «12/12/23» | None None |
| `ext::4.8.1.1` | validador | «12/12/23» | None None |
| `ext::13.1.4` | validador | «12/12/23» | None None |
| `ext::3.17.1.2` | validador | «12/12/23» | None None |
| `pro::2.3.2.1` | validador | «cuarta parte del plazo original de la financiación» | None None |
| `docvig::3.5` | validador | «plazos legales para su cobro» | None None |
| `ext::3.3.3.1` | validador | «04/07/24» | None None |
| `cap::12.2` | validador | «31/12/25» | None None |
| `ctacte::6.4.6.5` | validador | «día anterior a la fecha de presentación de la solicitud de apertura» | None None |
| `cap::4.3.3.1` | validador | «5.000 operaciones» | None None |
| `ext::7.8.4::intro` | validador | «plazos normativos establecidos» | None None |
| `polcre::5.3` | validador | «"AA"» | None None |
| `pro::3.2.1.3` | validador | «una vez al año» | None None |
| `pro::3.1.1.8` | validador | «trimestral» | None None |
| `pro::3.1.1.8` | validador | «trimestral» | None None |
| `pro::3.1.1.8` | validador | «trimestral» | None None |
| `cla::7.3` | validador | «un nivel» | None None |
| `cla::7.3` | validador | «otras dos entidades» | None None |
| `pro::3.2.1.1` | validador | «trimestralmente» | None None |
| `ctacte::3.5.3` | validador | «fecha de vencimiento del plazo previsto en el artículo 25 de la Ley de Cheques» | None None |
| `ctacte::1.5.2.3` | validador | «tres de sus titulares» | None None |
| `cap::8.4.1.8` | validador | «mes anterior al de regularización de aquella situación» | None None |
| `cap::4.2.1.2::parte2` | validador | «dos disputas» | None None |
| `cap::4.2.1.2::parte2` | validador | «doble que el mínimo establecido» | None None |
| `ext::11.1.1.8` | validador | «12/12/23» | None None |
| `cap::6.10.1.2` | validador | «con periodicidad mensual» | None None |
| `ric::12.4` | validador | «31/03/24» | None None |
| `ctacte::13.3` | validador | «01/12/25» | None None |
| `cla::6.6` | validador | «un nivel» | None None |
| `cla::6.6` | validador | «otras dos entidades o fideicomisos financieros» | None None |
| `pagjub::1.4` | validador | «dos funcionarios» | None None |
| `cla::6.2` | validador | «dos escenarios» | None None |
| `ric::1.2` | validador | «que 5» | None None |
| `ext::3.3.3.1` | validador | «04/07/24» | None None |
| `ext::10.11::intro` | validador | «12/12/23» | None None |
| `cap::6.2.1.2` | validador | «12» | None None |
| `ext::3.5.3.4` | validador | «fecha de vencimiento de la deuda que se cancela» | None None |
| `ctacte::1.5.2.11` | validador | «una vez el importe de las multas de que se trate» | None None |
| `pagjub::2.7::intro` | validador | «uno» | None None |
| `pro::2.3.2.1` | validador | «cuarta parte del plazo original de la financiación» | None None |
| `cap::12.3` | validador | «30/06/26» | None None |
| `ctacte::4.2::intro` | validador | «día anterior a su vencimiento» | None None |
| `ctacte::5.1.1.1` | validador | «un endoso» | None None |
| `ctacte::5.1.1.2` | validador | «2 (dos) endosos» | None None |
| `ctacte::1.5.1.8` | validador | «3 firmas» | None None |
| `ctacte::5.1.1::intro` | validador | «31.12.27 inclusive» | None None |
| `cap::6.2.3.5` | validador | «un margen de 15 puntos básicos» | None None |

## Ítem (i): los nodos que pasan la ventana del agente (insumo de U-NAV-DISENO)

La ventana real: `ver_vecinos(limite=40)` corta 40 por dirección (`evaluacion/harness.py:230-235`). Con el código nuevo, 49 nodos con `remite_a` y 20 sin ella, los mismos nodos que en `a9631a64`. La definición de la v6 (más de 40 entre entrantes y salientes) queda como referencia: 41 y 22 (43 y 22 en `a9631a64`).

### Con `remite_a` (49)

| nodo | tipo | salientes | entrantes | salientes `remite_a` | entrantes `remite_a` |
|---|---|---|---|---|---|
| `Condicion_acceso_previo_al_mercado_de_cambios__las_entidades_deben_cumplir_esta_condicion__8ea27a` | Condicion | 50 | 0 | 48 | 0 |
| `Condicion_otras_imputaciones_admitidas_en_cumplimiento_de_seguimiento__se_verifica_cuando__bb4a77` | Condicion | 76 | 0 | 74 | 0 |
| `Condicion_otras_imputaciones_admitidas_segun_puntos_8_5_1_al_8_5_18__el_resto_del_valor_fa_5afa1c` | Condicion | 76 | 0 | 74 | 0 |
| `Condicion_suscripcion_primaria_bopreal_elegible__la_venta_debe_ser_de_bonos_bopreal_adquir_b7256a` | Condicion | 46 | 2 | 44 | 2 |
| `Condicion_venta_de_bonos_bopreal_adquiridos_en_suscripcion_primaria__la_venta_debe_ser_de__e99254` | Condicion | 46 | 0 | 44 | 0 |
| `Condicion_verificacion_de_condiciones_9_3_1_a_9_3_13__se_verifiquen_las_condiciones_previs_5585e4` | Condicion | 58 | 0 | 56 | 0 |
| `Condicion_verificacion_de_condiciones_siguientes__la_facultad_de_acceso_al_mercado_de_camb_2287e2` | Condicion | 2 | 121 | 0 | 121 |
| `Definicion_acciones_cotizadas_en_bolsas_reguladas__acciones_y_bonos_convertibles_en_accione_12a5e7` | Definicion | 1 | 41 | 0 | 41 |
| `Definicion_activos_admitidos_metodo_integral__incluye_los_activos_admitidos_en_el_metodo_si_a819b8` | Definicion | 9 | 41 | 8 | 41 |
| `Definicion_cuotapartes_de_fondos_de_inversion_y_certificados__cuotapartes_de_fondos_comunes_d6906d` | Definicion | 1 | 41 | 0 | 41 |
| `Definicion_epf_exposicion_potencial_futura__exposicion_potencial_futura_calculada_de_acuerd_c22b93` | Definicion | 76 | 12 | 75 | 12 |
| `Definicion_exposicion_potencial_futura_epf__exposicion_potencial_futura_calculada_de_acuerd_6a5287` | Definicion | 79 | 1 | 78 | 1 |
| `Definicion_titulizacion_simple_transparente_y_comparable_stc__una_titulizacion_que_cumple_t_9d6ec0` | Definicion | 42 | 12 | 41 | 12 |
| `Obligacion_activos_constituidos_en_garantia_estan_sujetos_al_requisito_de_riesgo_de_credito_53c52c` | Obligacion | 69 | 2 | 67 | 2 |
| `Obligacion_costo_de_reposicion_total_de_contratos_relevantes_puede_calcularse_como_costo_de_de6414` | Obligacion | 53 | 2 | 52 | 2 |
| `Obligacion_el_activo_ponderado_por_riesgo_se_calculara_como_la_diferencia_entre_el_importe__a85fad` | Obligacion | 41 | 3 | 39 | 3 |
| `Obligacion_la_entidad_debera_cumplimentar_el_resto_del_valor_facturado_segun_la_condicion_d_8092d1` | Obligacion | 76 | 3 | 74 | 0 |
| `Obligacion_la_entidad_financiera_cliente_y_el_miembro_compensador_deben_dar_a_la_transaccio_f31662` | Obligacion | 46 | 0 | 43 | 0 |
| `Obligacion_los_conjuntos_de_neteo_aplicables_a_las_entidades_financieras_que_actuen_como_mi_e4736d` | Obligacion | 45 | 1 | 43 | 1 |
| `Operacion_emision_de_certificaciones_de_aplicacion__ext_9_3_81e1ab` | Operacion | 58 | 1 | 56 | 0 |
| `Operacion_otras_ventas_de_titulos_valores_a_partir_de_01_04_24__ext_4_3_2_3_57ce01` | Operacion | 45 | 3 | 44 | 2 |
| `Operacion_pago_de_titulos_de_deuda_y_endeudamientos_financieros_con_el_exterior__ext_3_5_9b8054` | Operacion | 1 | 121 | 0 | 121 |
| `Operacion_suscripcion_bopreal_por_importadores_de_servicios__ext_4_5_9d04d1` | Operacion | 2 | 41 | 0 | 36 |
| `Operacion_suscripcion_de_bopreal_por_deudores_de_importaciones__ext_4_4_fefb25` | Operacion | 28 | 42 | 26 | 39 |
| `Operacion_venta_de_bonos_bopreal_contra_cable__ext_4_3_2_3_f31d38` | Operacion | 45 | 4 | 44 | 2 |
| `Potestad_acceso_al_mercado_de_cambios_pagos_de_titulos_y_endeudamientos__las_entidades_es_8f2af3` | Potestad | 2 | 122 | 0 | 121 |
| `Potestad_acceso_al_mercado_de_cambios_para_pagos_de_titulos_y_endeudamientos__las_entidad_8994a6` | Potestad | 2 | 122 | 0 | 121 |
| `Potestad_cr_no_se_ve_afectado_por_garantias_en_exceso__el_cr_no_se_ve_afectado_cuando_la__479369` | Potestad | 76 | 5 | 75 | 5 |
| `Restriccion_el_valor_de_mercado_de_las_otras_ventas_de_titulos_valores_no_debe_superar_la_di_c1d421` | Restriccion | 46 | 2 | 44 | 2 |
| `Sujeto_alta_gerencia` | Sujeto | 1 | 45 | 0 | 0 |
| `Sujeto_banco` | Sujeto | 2 | 267 | 0 | 0 |
| `Sujeto_cliente` | Sujeto | 1 | 63 | 0 | 0 |
| `Sujeto_directorio` | Sujeto | 1 | 95 | 0 | 0 |
| `Sujeto_entidad_financiera` | Sujeto | 24 | 538 | 0 | 0 |
| `Sujeto_rol_alcance_capmin` | Sujeto | 0 | 245 | 0 | 0 |
| `Sujeto_rol_entidad_autorizada_exterior` | Sujeto | 1 | 536 | 0 | 0 |
| `Sujeto_rol_entidad_comprendida_reginf` | Sujeto | 0 | 95 | 0 | 0 |
| `Sujeto_rol_obligado_a_clasificar_clasificacion` | Sujeto | 1 | 75 | 0 | 0 |
| `Sujeto_rol_sujeto_obligado_proteccion` | Sujeto | 1 | 188 | 0 | 0 |
| `TextoOrdenado_ctacte_pdf` | TextoOrdenado | 16 | 1067 | 0 | 0 |
| `TextoOrdenado_docvig_pdf` | TextoOrdenado | 3 | 101 | 0 | 18 |
| `TextoOrdenado_lingob_pdf` | TextoOrdenado | 2 | 278 | 0 | 0 |
| `TextoOrdenado_pagjub_pdf` | TextoOrdenado | 1 | 139 | 0 | 6 |
| `TextoOrdenado_polcre_pdf` | TextoOrdenado | 3 | 208 | 0 | 4 |
| `TextoOrdenado_to_capitales_minimos_actual_pdf` | TextoOrdenado | 12 | 2187 | 0 | 2 |
| `TextoOrdenado_to_clasificacion_deudores_actual_pdf` | TextoOrdenado | 2 | 567 | 0 | 12 |
| `TextoOrdenado_to_exterior_cambios_actual_pdf` | TextoOrdenado | 27 | 3086 | 0 | 3 |
| `TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf` | TextoOrdenado | 8 | 376 | 0 | 2 |
| `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf` | TextoOrdenado | 6 | 548 | 0 | 0 |

### Sin `remite_a` (20)

| nodo | tipo | salientes | entrantes | salientes `remite_a` | entrantes `remite_a` |
|---|---|---|---|---|---|
| `Sujeto_alta_gerencia` | Sujeto | 1 | 45 | 0 | 0 |
| `Sujeto_banco` | Sujeto | 2 | 267 | 0 | 0 |
| `Sujeto_cliente` | Sujeto | 1 | 63 | 0 | 0 |
| `Sujeto_directorio` | Sujeto | 1 | 95 | 0 | 0 |
| `Sujeto_entidad_financiera` | Sujeto | 24 | 538 | 0 | 0 |
| `Sujeto_rol_alcance_capmin` | Sujeto | 0 | 245 | 0 | 0 |
| `Sujeto_rol_entidad_autorizada_exterior` | Sujeto | 1 | 536 | 0 | 0 |
| `Sujeto_rol_entidad_comprendida_reginf` | Sujeto | 0 | 95 | 0 | 0 |
| `Sujeto_rol_obligado_a_clasificar_clasificacion` | Sujeto | 1 | 75 | 0 | 0 |
| `Sujeto_rol_sujeto_obligado_proteccion` | Sujeto | 1 | 188 | 0 | 0 |
| `TextoOrdenado_ctacte_pdf` | TextoOrdenado | 16 | 1067 | 0 | 0 |
| `TextoOrdenado_docvig_pdf` | TextoOrdenado | 3 | 101 | 0 | 18 |
| `TextoOrdenado_lingob_pdf` | TextoOrdenado | 2 | 278 | 0 | 0 |
| `TextoOrdenado_pagjub_pdf` | TextoOrdenado | 1 | 139 | 0 | 6 |
| `TextoOrdenado_polcre_pdf` | TextoOrdenado | 3 | 208 | 0 | 4 |
| `TextoOrdenado_to_capitales_minimos_actual_pdf` | TextoOrdenado | 12 | 2187 | 0 | 2 |
| `TextoOrdenado_to_clasificacion_deudores_actual_pdf` | TextoOrdenado | 2 | 567 | 0 | 12 |
| `TextoOrdenado_to_exterior_cambios_actual_pdf` | TextoOrdenado | 27 | 3086 | 0 | 3 |
| `TextoOrdenado_to_proteccion_usuarios_servicios_financieros_actual_pdf` | TextoOrdenado | 8 | 376 | 0 | 2 |
| `TextoOrdenado_to_regimen_informativo_contable_mensual_actual_pdf` | TextoOrdenado | 6 | 548 | 0 | 0 |
