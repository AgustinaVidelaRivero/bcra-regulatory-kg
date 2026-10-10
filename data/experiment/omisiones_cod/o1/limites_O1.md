# U-OMISIONES-COD, O1 — límites y residuos, caso por caso

Generado por `scripts/limites_md.py` desde `salidas/limites_O1.json` (de `scripts/limites_O1.py`). Páginas: las de la unidad en la E0 r2b. «sin leer»: no leí el caso; el mecanismo es una hipótesis o falta.

## Grupo L: elementos que conservan la cuantía (6)

| unidad | páginas | cuantía | tramo de E1 | mecanismo |
|---|---|---|---|---|
| `ext::3.5.3::intro` | [23] | «3 (tres) días hábiles» | «no mayor a los 3 (tres) días hábiles» | el tramo de E1 no es literal: no verifica contra el texto de E0 del nodo |
| `ext::7.8.5.2` | [94] | «2 (dos) años» | «vida promedia no inferior a 2 (dos) años» | el tramo de E1 no es literal: no verifica contra el texto de E0 del nodo |
| `pro::2.3.5.1` | [15, 16] | «cinco (5) días hábiles» | «dentro de los cinco (5) días hábiles siguientes al momento de constatarse tal circunstancia» | el tramo de E1 no es literal: no verifica contra el texto de E0 del nodo |
| `cap::3.2.4` | [61, 62] | «1250 %» | «no podrá superar 1250 %» | el tramo de E1 verifica «tokens» y su literal mínimo pierde la cuantía (o su valor y unidad) |
| `ext::4.2::cierre` | [58] | «360 (trescientos sesenta) días corridos» | «no podrá tener un plazo de pago que exceda a los 360 (trescientos sesenta) días corridos» | el tramo de E1 no es literal: no verifica contra el texto de E0 del nodo |
| `cap::5.3.2.1` | [106, 107] | «tres meses» | «plazo residual no mayor a tres meses» | el tramo de E1 no es literal: no verifica contra el texto de E0 del nodo |

## Grupo B, f: menciones que verifican sin el artículo inicial y siguen sin verificar (17 de 64)

El conjunto lo reconstruí con la definición de R2-1 (mención que no verifica y verifica sin su artículo inicial): da 64 relaciones, no 51. Pasan 47. La expansión de contracciones solo alcanza al artículo «el» (en «del» y «al»): con «la» y «los» no hay contracción, y por construcción esas menciones no pasan. «las entidades» es la expresión colectiva de R3, que R2-1 dejó fuera de sus 51.

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

## Grupo A, e: en el conjunto de diseño de T4, copias reales no detectadas (3) y detecciones que T4 no leyó como copia (4)

| caso T4 | unidad | páginas | clase de T4 | razón de T4 | mecanismo |
|---|---|---|---|---|---|
| 3 | `pro::2.3.1.1` | [7, 8, 9] | copia real | ausente «cómputo» (la unidad no tiene ninguna forma de computar) | la palabra que trae la nota es una derivación que la tolerancia de flexión toma como presente |
| 29 | `ext::2.7::cierre` | [14] | copia real | ausente «cómputo» («computados» es otra palabra, derivada) | la palabra que trae la nota es una derivación que la tolerancia de flexión toma como presente |
| 44 | `ext::3.5.4::intro` | [25] | copia real | ausente «vigencia» (la norma dice «vigente»): el mismo caso que el 19 de P3b-2 | la palabra que trae la nota es una derivación que la tolerancia de flexión toma como presente |
| 5 | `cla::3.3.2` | — | coincidencia legítima | «el manual de procedimientos de» es la frase de la norma | sin leer |
| 43 | `ext::3.5.4.3` | — | coincidencia legítima | remite al 3.5.4 por su número, como su encabezado («3.5.4. En la medida que…») | sin leer |
| 52 | `ext::4.6.1::intro` | — | coincidencia legítima | «el equivalente en moneda local», de la norma | sin leer |
| 57 | `ext::7.1.1.3` | — | coincidencia legítima | «los capítulos 26 y 71», literal | sin leer |

## Grupo H: Comunicacion con `tipo_no_derivable` (26)

Quedan como error de extracción declarado (v7). Mecanismo de las 26: el código y la etiqueta no nombran una Comunicación ni una norma externa (remisión a un punto o una sección, o el nombre de un TO u otro documento).

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

## Grupo C: lo que queda marcado o sin base (la cifra de la v7; lista entera en `salidas/grupos_C_L_diez.json`, `C.lista`)

De los 264 elementos con base: {'marcada': 177, 'sin_base': 76, 'resuelta': 11}. Las 160 que cambian, por motivo: {'g1': 76, 'g': 81, 'g3': 2, 'g2': 1}. Las 177 marcadas quedan como límite declarado de la v7 (base no resuelta), y las 76 sin base, sin marca. Entre las 11 resueltas está `ext::13.4.6` → `ext::4.4`, que no es de las 7 correctas que nombra la v7: sin leer.

