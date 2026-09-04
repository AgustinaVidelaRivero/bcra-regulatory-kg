# U-SUJ-FREQ — Frecuencia de `sujeto_propuesto` (insumo de B5.4)

Analisis de frecuencia para el catalogo de sujetos v3 (diseño
`docs/diseno_B5.4_catalogo_sujetos_v3.md` §0.2): que sujetos reales, hoy en
`sujeto_propuesto`, tienen evidencia medida para candidatearse a id del
catalogo. La lista final del catalogo es de la autora con B5.4: este
documento entrega la medicion y NO propone esa lista.

Reproduce todos los numeros de este documento: `python3 data/experiment/esq/code/frecuencia_sujetos_suj_freq.py`
Selftest del agrupador: `python3 data/experiment/esq/code/frecuencia_sujetos_suj_freq.py --selftest`
Costo de API: USD 0 (el script no hace ninguna llamada LLM).

## 0. Universo leido

**Universo primario** (una extraccion por unidad, esquema de produccion):

- **dev / corpus_v2 (5 TOs: cap, cla, ext, pro, ric)** — `data/experiment/reextraccion_v2/corpus_v2/salida/<to>/extracciones_e1.jsonl`: 1769 registros E1, **1763 unidades** (duplicados supersedidos: 6; con error: 1).
- **ESQ-2 / cobertura (10 TOs: actgar, adrei, ayccef, cryl, ctacor, expaef, lavdin, opefci, prevmi, traval)** — `data/experiment/esq/cobertura/<to>/extracciones_e1_<to>.jsonl`: 762 registros E1, **762 unidades** (duplicados supersedidos: 0; con error: 0).

- Regla de dedupe: una extraccion por unidad: ante chunk_id repetido se queda el ultimo registro del archivo (la reextraccion dirigida posterior).
- Unidades dev con reextraccion dirigida (6): `cap::3.1.14.1`, `cap::4.2.1.2`, `cap::4.3.3.1`, `cla::9.2`, `ext::4.7.1`, `ext::8.5.20.3`.
- Capa leida: `validacion.relaciones` (la persistida por produccion). Control:
  - dev: relaciones `aplica_a`/`ejecuta` en `tool_input_crudo`: 3504 (la diferencia con la tabla de abajo son los rechazos del validador; no se juzga aca).
  - esq2: relaciones `aplica_a`/`ejecuta` en `tool_input_crudo`: 768 (la diferencia con la tabla de abajo son los rechazos del validador; no se juzga aca).

**Tabla lateral** (descriptiva, SIN peso en el corte): 43 re-extracciones de ESQ-3b + 27 de la vuelta 2, mismas unidades bajo esquema retocado; capa `tool_input_crudo` (no tienen `validacion`). No se mezcla con el primario en ninguna tabla de este documento.

Los sha256 de todos los archivos de entrada estan en el JSON compañero
(`universo_primario.meta.archivos_sha256` y `lateral.meta.archivos_sha256`).
El script no escribe nada salvo sus dos propias salidas.

## 1. Inventario EXACTO del catalogo vigente de sujetos

Fuente: prompt_e1.TOOL_SCHEMA_E1 -> input_schema.properties.relations.items.properties.sujeto_id.enum — es el enum del tool schema de PRODUCCION, no la
prosa del prompt (la prosa instructiva, sin el bloque del catalogo interpolado,
nombra 5 ids: `Sujeto_banco`, `Sujeto_banco_comercial`, `Sujeto_empresa_no_financiera_emisora_de_tarjetas`, `Sujeto_entidad_financiera`, `Sujeto_pspcp`; el enum tiene **70**).

- Version del catalogo: **2.0** (`data/experiment/grafo_v2/esquema_v2_clases.json`).
- Composicion: **58 clases + 7 instancias + 5 roles de alcance = 70 ids**.
- El enum de `sujeto_propuesto_padre_sugerido` es identico al de `sujeto_id`: si.
- Definiciones: el catalogo (esquema_v2_clases.json) no tiene campo 'definicion': cada entrada trae label, alias, nivel y padre; eso es lo que existe y lo que se lista.
- Coherencia del enum con los prompts posteriores (informativa): congelado: identico; retocado_esq3b: identico; v2_esq3b: identico.

| id | nivel | label | alias | padre |
|---|---|---|---|---|
| `Sujeto_sujeto` | clase | Sujetos | — | — |
| `Sujeto_sujeto_regulado` | clase | Sujetos regulados | — | Sujeto_sujeto |
| `Sujeto_contraparte` | clase | Contrapartes | — | Sujeto_sujeto |
| `Sujeto_organismo_publico` | clase | Organismos públicos | — | Sujeto_sujeto |
| `Sujeto_estructura` | clase | Estructuras y vehículos | — | Sujeto_sujeto |
| `Sujeto_entidad_financiera` | clase | Entidades financieras | Entidades financieras del exterior, Entidad financiera del exterior, Entidades financieras emisoras de tarjetas de crédito y/o compra, Entidad financiera emisora de tarjetas de crédito y/o compra | Sujeto_sujeto_regulado |
| `Sujeto_banco` | clase | Bancos | Bancos del exterior, Banco del exterior | Sujeto_entidad_financiera |
| `Sujeto_banco_comercial` | clase | Bancos comerciales | — | Sujeto_banco |
| `Sujeto_compania_financiera` | clase | Compañías financieras | — | Sujeto_entidad_financiera |
| `Sujeto_caja_de_credito` | clase | Cajas de crédito | — | Sujeto_entidad_financiera |
| `Sujeto_caja_de_credito_cooperativa` | clase | Cajas de crédito cooperativas | — | Sujeto_entidad_financiera |
| `Sujeto_entidad_cambiaria` | clase | Entidades cambiarias | Operador de cambio, Operadores de cambio, Entidades cambiarias del exterior, Compañía cambista del exterior | Sujeto_sujeto_regulado |
| `Sujeto_casa_de_cambio` | clase | Casas de cambio | — | Sujeto_entidad_cambiaria |
| `Sujeto_agencia_de_cambio` | clase | Agencias de cambio | — | Sujeto_entidad_cambiaria |
| `Sujeto_proveedor_de_servicios_de_pago` | clase | Proveedores de servicios de pago | — | Sujeto_sujeto_regulado |
| `Sujeto_pspcp` | clase | Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP) | PSPCP | Sujeto_proveedor_de_servicios_de_pago |
| `Sujeto_psi_billetera_digital` | clase | Proveedores de servicios de pago iniciadores que prestan el servicio de billetera digital (PSI) | PSI | Sujeto_proveedor_de_servicios_de_pago |
| `Sujeto_proveedor_no_financiero_de_credito` | clase | Proveedores no financieros de crédito | PNFC | Sujeto_sujeto_regulado |
| `Sujeto_empresa_no_financiera_emisora_de_tarjetas` | clase | Empresas no financieras emisoras de tarjetas de crédito y/o compra | Empresas emisoras de tarjetas | Sujeto_proveedor_no_financiero_de_credito |
| `Sujeto_pscpp` | clase | Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP) | PSCPP | Sujeto_sujeto_regulado |
| `Sujeto_fiduciario_de_fideicomiso_financiero` | clase | Fiduciarios de fideicomisos financieros | — | Sujeto_sujeto_regulado |
| `Sujeto_sociedad_de_garantia_reciproca` | clase | Sociedades de garantía recíproca | SGR | Sujeto_sujeto_regulado |
| `Sujeto_fondo_de_garantia_publico` | clase | Fondos de garantía de carácter público | — | Sujeto_sujeto_regulado |
| `Sujeto_entidad_de_contraparte_central` | clase | Entidades de contraparte central (CCP) | CCP | Sujeto_sujeto_regulado |
| `Sujeto_ccp_calificada` | clase | Entidades de contraparte central calificadas | QCCP | Sujeto_entidad_de_contraparte_central |
| `Sujeto_ccp_no_calificada` | clase | Entidades de contraparte central no calificadas | — | Sujeto_entidad_de_contraparte_central |
| `Sujeto_miembro_compensador` | clase | Miembros compensadores | — | Sujeto_sujeto_regulado |
| `Sujeto_ecai` | clase | Agentes de calificación externa (ECAI) | ECAI | Sujeto_sujeto_regulado |
| `Sujeto_sujeto_del_perimetro_consolidado` | clase | Sujetos del perímetro de supervisión consolidada | — | Sujeto_sujeto_regulado |
| `Sujeto_aseguradora` | clase | Aseguradoras | — | Sujeto_sujeto_del_perimetro_consolidado |
| `Sujeto_entidad_bursatil` | clase | Entidades bursátiles | — | Sujeto_sujeto_del_perimetro_consolidado |
| `Sujeto_empresa_de_servicios_complementarios` | clase | Empresas de servicios complementarios de la actividad financiera | — | Sujeto_sujeto_del_perimetro_consolidado |
| `Sujeto_cliente` | clase | Clientes | — | Sujeto_contraparte |
| `Sujeto_persona_humana` | clase | Personas humanas | — | Sujeto_cliente |
| `Sujeto_persona_juridica` | clase | Personas jurídicas | — | Sujeto_cliente |
| `Sujeto_universalidad` | clase | Patrimonios y otras universalidades | — | Sujeto_cliente |
| `Sujeto_deudor` | clase | Deudores | — | Sujeto_cliente |
| `Sujeto_usuario_de_servicios_financieros` | clase | Usuarios de servicios financieros | — | Sujeto_contraparte |
| `Sujeto_importador` | clase | Importadores | — | Sujeto_contraparte |
| `Sujeto_importador_de_bienes` | clase | Importadores de bienes | — | Sujeto_importador |
| `Sujeto_importador_de_servicios` | clase | Importadores de servicios | — | Sujeto_importador |
| `Sujeto_exportador` | clase | Exportadores | — | Sujeto_contraparte |
| `Sujeto_mipyme` | clase | MiPyMEs | — | Sujeto_contraparte |
| `Sujeto_emisor_de_titulos_de_deuda` | clase | Emisores de títulos de deuda | — | Sujeto_contraparte |
| `Sujeto_vpu_rigi` | clase | Vehículos de Proyecto Único (VPU) adheridos al RIGI | VPU | Sujeto_contraparte |
| `Sujeto_beneficiario_economia_conocimiento` | clase | Beneficiarios del Régimen de Promoción de la Economía del Conocimiento | — | Sujeto_contraparte |
| `Sujeto_sector_publico_no_financiero` | clase | Sector público no financiero | — | Sujeto_contraparte |
| `Sujeto_sector_privado_no_financiero` | clase | Sector privado no financiero | — | Sujeto_contraparte |
| `Sujeto_acreedor_del_exterior` | clase | Acreedores del exterior | — | Sujeto_contraparte |
| `Sujeto_fideicomiso` | clase | Fideicomisos | — | Sujeto_estructura |
| `Sujeto_fideicomiso_financiero` | clase | Fideicomisos financieros | — | Sujeto_fideicomiso |
| `Sujeto_sociedad_de_proposito_especial` | clase | Entes de propósito especial (SPE) | SPE, Sociedad de propósito especial | Sujeto_estructura |
| `Sujeto_fondo_comun_de_inversion` | clase | Fondos comunes de inversión | FCI | Sujeto_estructura |
| `Sujeto_gobierno_local` | clase | Gobiernos locales | — | Sujeto_organismo_publico |
| `Sujeto_organismo_internacional` | clase | Organismos internacionales | — | Sujeto_organismo_publico |
| `Sujeto_banco_multilateral_de_desarrollo` | clase | Bancos multilaterales de desarrollo | BMD | Sujeto_organismo_internacional |
| `Sujeto_agencia_oficial_de_credito` | clase | Agencias oficiales de crédito | — | Sujeto_organismo_publico |
| `Sujeto_autoridad_nacional_de_aplicacion` | clase | Autoridad Nacional de Aplicación | — | Sujeto_organismo_publico |
| `Sujeto_bcra` | instancia | BCRA (Banco Central de la República Argentina) | — | Sujeto_organismo_publico |
| `Sujeto_sefyc` | instancia | SEFyC (Superintendencia de Entidades Financieras y Cambiarias) | Superintendencia de Entidades Financieras y Cambiarias | Sujeto_organismo_publico |
| `Sujeto_arca` | instancia | ARCA (Agencia de Recaudación y Control Aduanero) | AFIP, Agencia de Recaudación y Control Aduanero | Sujeto_organismo_publico |
| `Sujeto_ministerio_de_economia` | instancia | Ministerio de Economía | — | Sujeto_organismo_publico |
| `Sujeto_secretaria_de_energia` | instancia | Secretaría de Energía | — | Sujeto_organismo_publico |
| `Sujeto_secretaria_de_comercio` | instancia | Secretaría de Comercio | — | Sujeto_organismo_publico |
| `Sujeto_secretaria_de_transporte` | instancia | Secretaría de Transporte | — | Sujeto_organismo_publico |
| `Sujeto_rol_sujeto_obligado_proteccion` | rol | Sujetos obligados (Protección de usuarios) | — | rol del TO TO_proteccion_usuarios_servicios_financieros_actual.pdf |
| `Sujeto_rol_entidad_autorizada_exterior` | rol | Entidades autorizadas a operar en cambios (Exterior) | — | rol del TO TO_exterior_cambios_actual.pdf |
| `Sujeto_rol_obligado_a_clasificar_clasificacion` | rol | Obligados a clasificar deudores (Clasificación) | — | rol del TO TO_clasificacion_deudores_actual.pdf |
| `Sujeto_rol_entidad_comprendida_reginf` | rol | Entidades comprendidas (Régimen Informativo) | — | rol del TO TO_regimen_informativo_contable_mensual_actual.pdf |
| `Sujeto_rol_alcance_capmin` | rol | Entidades alcanzadas (Capitales Mínimos) | — | rol del TO TO_capitales_minimos_actual.pdf |

## 2. Relaciones con sujeto del universo primario

- Relaciones `aplica_a`/`ejecuta` (validadas): **4029** (aplica_a: 3899, ejecuta: 130).
- Con `sujeto_id` del catalogo: **3905**. Con `sujeto_propuesto`: **124**. Con ambos (violacion de exclusion mutua): 0. Sin ninguno: 0.
  - dev: 3302 relaciones con sujeto — `sujeto_id` 3248, `sujeto_propuesto` 54.
  - esq2: 727 relaciones con sujeto — `sujeto_id` 657, `sujeto_propuesto` 70.

### 2.a Distribucion de `sujeto_id` (catalogo)

| # | sujeto_id | n | dev | ESQ-2 | unidades | TOs |
|---:|---|---:|---:|---:|---:|---:|
| 1 | `Sujeto_rol_entidad_autorizada_exterior` | 1079 | 1069 | 10 | 653 | 3 |
| 2 | `Sujeto_rol_alcance_capmin` | 972 | 970 | 2 | 378 | 2 |
| 3 | `Sujeto_entidad_financiera` | 571 | 148 | 423 | 315 | 15 |
| 4 | `Sujeto_rol_obligado_a_clasificar_clasificacion` | 254 | 253 | 1 | 101 | 2 |
| 5 | `Sujeto_rol_entidad_comprendida_reginf` | 243 | 242 | 1 | 71 | 2 |
| 6 | `Sujeto_rol_sujeto_obligado_proteccion` | 236 | 232 | 4 | 83 | 2 |
| 7 | `Sujeto_cliente` | 49 | 46 | 3 | 34 | 4 |
| 8 | `Sujeto_sujeto_regulado` | 45 | 0 | 45 | 24 | 6 |
| 9 | `Sujeto_bcra` | 36 | 18 | 18 | 21 | 8 |
| 10 | `Sujeto_persona_humana` | 36 | 11 | 25 | 23 | 7 |
| 11 | `Sujeto_sefyc` | 35 | 6 | 29 | 32 | 8 |
| 12 | `Sujeto_exportador` | 30 | 30 | 0 | 27 | 1 |
| 13 | `Sujeto_persona_juridica` | 26 | 6 | 20 | 15 | 4 |
| 14 | `Sujeto_ecai` | 23 | 23 | 0 | 12 | 1 |
| 15 | `Sujeto_entidad_cambiaria` | 21 | 13 | 8 | 15 | 6 |
| 16 | `Sujeto_miembro_compensador` | 21 | 21 | 0 | 3 | 1 |
| 17 | `Sujeto_empresa_no_financiera_emisora_de_tarjetas` | 20 | 20 | 0 | 14 | 3 |
| 18 | `Sujeto_vpu_rigi` | 19 | 19 | 0 | 14 | 1 |
| 19 | `Sujeto_banco` | 18 | 4 | 14 | 12 | 5 |
| 20 | `Sujeto_casa_de_cambio` | 13 | 7 | 6 | 8 | 2 |
| 21 | `Sujeto_fiduciario_de_fideicomiso_financiero` | 12 | 11 | 1 | 5 | 3 |
| 22 | `Sujeto_importador` | 11 | 11 | 0 | 6 | 1 |
| 23 | `Sujeto_proveedor_no_financiero_de_credito` | 11 | 11 | 0 | 6 | 2 |
| 24 | `Sujeto_banco_comercial` | 10 | 6 | 4 | 8 | 4 |
| 25 | `Sujeto_empresa_de_servicios_complementarios` | 10 | 1 | 9 | 5 | 2 |
| 26 | `Sujeto_pspcp` | 9 | 9 | 0 | 3 | 1 |
| 27 | `Sujeto_fondo_comun_de_inversion` | 8 | 3 | 5 | 4 | 4 |
| 28 | `Sujeto_proveedor_de_servicios_de_pago` | 7 | 1 | 6 | 4 | 2 |
| 29 | `Sujeto_contraparte` | 6 | 1 | 5 | 5 | 4 |
| 30 | `Sujeto_entidad_de_contraparte_central` | 6 | 1 | 5 | 3 | 2 |
| 31 | `Sujeto_mipyme` | 6 | 4 | 2 | 5 | 3 |
| 32 | `Sujeto_deudor` | 5 | 4 | 1 | 4 | 3 |
| 33 | `Sujeto_gobierno_local` | 5 | 5 | 0 | 2 | 1 |
| 34 | `Sujeto_sector_publico_no_financiero` | 5 | 4 | 1 | 4 | 2 |
| 35 | `Sujeto_agencia_de_cambio` | 3 | 3 | 0 | 2 | 1 |
| 36 | `Sujeto_aseguradora` | 3 | 3 | 0 | 3 | 2 |
| 37 | `Sujeto_banco_multilateral_de_desarrollo` | 3 | 3 | 0 | 2 | 1 |
| 38 | `Sujeto_beneficiario_economia_conocimiento` | 3 | 3 | 0 | 3 | 1 |
| 39 | `Sujeto_caja_de_credito_cooperativa` | 3 | 0 | 3 | 3 | 2 |
| 40 | `Sujeto_ccp_calificada` | 3 | 3 | 0 | 1 | 1 |
| 41 | `Sujeto_fideicomiso` | 3 | 3 | 0 | 2 | 1 |
| 42 | `Sujeto_psi_billetera_digital` | 3 | 3 | 0 | 2 | 1 |
| 43 | `Sujeto_compania_financiera` | 2 | 1 | 1 | 2 | 2 |
| 44 | `Sujeto_emisor_de_titulos_de_deuda` | 2 | 2 | 0 | 2 | 1 |
| 45 | `Sujeto_fondo_de_garantia_publico` | 2 | 2 | 0 | 2 | 2 |
| 46 | `Sujeto_importador_de_bienes` | 2 | 2 | 0 | 2 | 1 |
| 47 | `Sujeto_organismo_internacional` | 2 | 1 | 1 | 2 | 2 |
| 48 | `Sujeto_pscpp` | 2 | 2 | 0 | 1 | 1 |
| 49 | `Sujeto_sociedad_de_garantia_reciproca` | 2 | 2 | 0 | 2 | 2 |
| 50 | `Sujeto_sujeto_del_perimetro_consolidado` | 2 | 0 | 2 | 1 | 1 |
| 51 | `Sujeto_universalidad` | 2 | 2 | 0 | 1 | 1 |
| 52 | `Sujeto_agencia_oficial_de_credito` | 1 | 1 | 0 | 1 | 1 |
| 53 | `Sujeto_entidad_bursatil` | 1 | 0 | 1 | 1 | 1 |
| 54 | `Sujeto_importador_de_servicios` | 1 | 1 | 0 | 1 | 1 |
| 55 | `Sujeto_sector_privado_no_financiero` | 1 | 1 | 0 | 1 | 1 |
| 56 | `Sujeto_sujeto` | 1 | 0 | 1 | 1 | 1 |

Ids del catalogo SIN uso en el universo primario (14 de 70): `Sujeto_acreedor_del_exterior`, `Sujeto_arca`, `Sujeto_autoridad_nacional_de_aplicacion`, `Sujeto_caja_de_credito`, `Sujeto_ccp_no_calificada`, `Sujeto_estructura`, `Sujeto_fideicomiso_financiero`, `Sujeto_ministerio_de_economia`, `Sujeto_organismo_publico`, `Sujeto_secretaria_de_comercio`, `Sujeto_secretaria_de_energia`, `Sujeto_secretaria_de_transporte`, `Sujeto_sociedad_de_proposito_especial`, `Sujeto_usuario_de_servicios_financieros`.

### 2.b Distribucion cruda de `sujeto_propuesto` (los 25 textos mas frecuentes)

| texto (libre, tal como se emitio) | n | unidades |
|---|---:|---:|
| Entidades financieras del grupo 1 | 7 | 1 |
| agencia complementaria de servicios financieros | 5 | 2 |
| promotores y fundadores de entidades financieras | 4 | 2 |
| titulares del 5% o más de capital social y/o votos | 3 | 1 |
| Banco Central Europeo | 2 | 1 |
| Banco de Pagos Internacionales | 2 | 1 |
| Centrales Depositarias de Valores | 2 | 1 |
| Compañía de seguros de crédito a la exportación | 2 | 1 |
| Cámaras Electrónicas de Compensación | 2 | 1 |
| Fondo Monetario Internacional | 2 | 1 |
| Futuros fundadores, accionistas, socios, integrantes de órganos de gobierno, administración y fiscalización de nuevas entidades financieras | 2 | 1 |
| Mercados de Valores | 2 | 1 |
| PSTV (prestadoras de servicios de transporte de valores) | 2 | 1 |
| Personas jurídicas que tengan a su cargo la provisión de medicamentos a pacientes | 2 | 1 |
| Sucursales y subsidiarias locales de entidades financieras del exterior | 2 | 1 |
| TV (transportadoras de valores) | 2 | 1 |
| accionistas | 2 | 2 |
| empresas del grupo económico de la procesadora de pagos, incluyendo la subsidiaria local | 2 | 1 |
| entidad nominada | 2 | 1 |
| entidad resultante de la fusión | 2 | 1 |
| entidades | 2 | 1 |
| entidades del Grupo A | 2 | 2 |
| nuevas entidades financieras autorizadas | 2 | 1 |
| originante | 2 | 1 |
| restantes obligados | 2 | 1 |

Textos distintos: **87**; la lista
completa esta en el JSON compañero (`distribucion_propuestos_cruda`).

## 3. Agrupacion mecanica de los `sujeto_propuesto`

Regla del agrupador (sin LLM, todas las reglas visibles en el codigo; el
normalizador y el recorte de raiz son los de U-R9-FREQ, copiados sin cambios):

1. Normalizacion: minusculas, sin diacriticos, solo letras, espacios colapsados.
2. Nucleo NOMINAL: las **dos primeras palabras de contenido** de la frase (los
   sujetos son frases nominales cuya cabeza suele ser generica — 'empresas',
   'entidades', 'proveedores' — y lo que distingue es el primer modificador).
   Palabras funcionales y marcadores se saltean por lista cerrada.
3. Cada palabra se reduce a raiz (enclitico + un sufijo + vocal tematica, raiz
   minima de 4). Clave del grupo: `raiz1+raiz2` (o `raiz1` si hay una sola).
4. **No hay tabla semantica de sinonimos**: sujetos sinonimos caen en grupos
   distintos y los grupos imperfectos quedan a la vista (columna de formas de
   superficie). Los conteos por grupo son **cota inferior** de la frecuencia del
   contenido.

- `sujeto_propuesto` agrupados: **124**
- Grupos formados: **70**
- Suma de los grupos: **124** (consistente: si)

## 4. Criterio de corte aplicado

Criterio **sellado en el mandato antes de mirar distribucion alguna** (no
calibrado): un grupo se candidatea a id del catalogo si aparece en
**>= 20 unidades** Y en **>= 5 TOs**, de los cuales
**>= 2 son TOs de ESQ-2**. Pasan o no pasan; orden entre los que
pasan por conteo descendente. Sin techo: la lista final es de la autora con B5.4.

Grupos que pasan: **0** de 70.

### 4.a Grupos que PASAN

(ninguno: ningun grupo de `sujeto_propuesto` alcanza el criterio sellado)

| # | clave | etiqueta | n | dev | ESQ-2 | unidades | TOs | TOs ESQ-2 | padre sugerido mas frecuente |
|---:|---|---|---:|---:|---:|---:|---:|---:|---|

### 4.b Grupos que NO pasan (los 30 mayores)

| clave | etiqueta | n | unidades | TOs | TOs ESQ-2 | falla por |
|---|---|---:|---:|---:|---:|---|
| `entidad+financier` | Entidades financieras del grupo 1 | 10 | 4 | 2 | 0 | unidades 4 < 20; TOs 2 < 5; TOs ESQ-2 0 < 2 |
| `person+juridic` | Personas jurídicas que tengan a su cargo la provisión de medicamentos a pacientes | 6 | 4 | 2 | 1 | unidades 4 < 20; TOs 2 < 5; TOs ESQ-2 1 < 2 |
| `agenc+complementar` | agencia complementaria de servicios financieros | 5 | 2 | 1 | 1 | unidades 2 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `promot+fundad` | promotores y fundadores de entidades financieras | 5 | 3 | 1 | 1 | unidades 3 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `nuev+entidad` | nuevas entidades financieras autorizadas | 4 | 3 | 1 | 1 | unidades 3 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `transportad+valor` | TV (transportadoras de valores) | 4 | 3 | 1 | 1 | unidades 3 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `banc+centr` | Banco Central Europeo | 3 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `entidad+grup` | entidades del Grupo A | 3 | 3 | 1 | 0 | unidades 3 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `entidad+nomin` | entidad nominada | 3 | 2 | 1 | 0 | unidades 2 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `titular+capit` | titulares del 5% o más de capital social y/o votos | 3 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `accionist` | accionistas | 2 | 2 | 1 | 1 | unidades 2 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `banc+pago` | Banco de Pagos Internacionales | 2 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `camar+electronic` | Cámaras Electrónicas de Compensación | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `centr+depositar` | Centrales Depositarias de Valores | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `compan+segur` | Compañía de seguros de crédito a la exportación | 2 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `empres+grup` | empresas del grupo económico de la procesadora de pagos, incluyendo la subsidiaria local | 2 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `entidad` | entidades | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `entidad+resultant` | entidad resultante de la fusión | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `fond+monetar` | Fondo Monetario Internacional | 2 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `futur+fundad` | Futuros fundadores, accionistas, socios, integrantes de órganos de gobierno, administración y fiscalización de nuevas entidades financieras | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `merc+valor` | Mercados de Valores | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `originant` | originante | 2 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `prestad+servic` | Prestadoras de Servicios de Transporte de Valores (PSTV) | 2 | 2 | 1 | 1 | unidades 2 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `pstv+prestad` | PSTV (prestadoras de servicios de transporte de valores) | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `representant+legal` | representante legal de la entidad | 2 | 2 | 2 | 2 | unidades 2 < 20; TOs 2 < 5 |
| `restant+oblig` | restantes obligados | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `solicitant+autoriz` | solicitantes de autorización | 2 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `sucurs+subsidiar` | Sucursales y subsidiarias locales de entidades financieras del exterior | 2 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |
| `accionist+soci` | accionistas, socios o equivalentes, directores, consejeros, autoridades equivalentes, síndicos e integrantes del Consejo de Vigilancia o equivalentes | 1 | 1 | 1 | 1 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 1 < 2 |
| `administrad+proveed` | administradores y proveedores de servicios auxiliares | 1 | 1 | 1 | 0 | unidades 1 < 20; TOs 1 < 5; TOs ESQ-2 0 < 2 |

Los 70 grupos que no pasan estan completos, con sus ejemplos
verbatim, sus TOs y sus padres sugeridos, en el JSON compañero, campo `grupos`.

### 4.c Sensibilidad del umbral (informativa — NO se aplica)

El criterio aplicado es el sellado. Esta tabla solo muestra cuan cerca del
borde quedo el resultado; no reemplaza ni recalibra el corte.

| umbral unidades | umbral TOs | umbral TOs ESQ-2 | grupos que pasarian |
|---:|---:|---:|---|
| 10 | 3 | 1 | 0: (ninguno) |
| 15 | 4 | 2 | 0: (ninguno) |
| 20 | 4 | 2 | 0: (ninguno) |
| 20 **(sellado)** | 5 | 2 | 0: (ninguno) |
| 25 | 5 | 2 | 0: (ninguno) |
| 20 | 6 | 3 | 0: (ninguno) |

## 5. Tabla LATERAL — los mismos grupos sobre las 70 re-extracciones retocadas

Descriptiva y SIN peso en el corte: son las mismas unidades del primario,
re-extraidas bajo el prefijo retocado (ESQ-3b) y su vuelta 2 (v2). Pregunta que
responde: ¿los propuestos persisten bajo el prefijo retocado? Capa
`tool_input_crudo` (sin validacion), no comparable 1:1 con las tablas de arriba.

- Relaciones `aplica_a`/`ejecuta`: 76 (aplica_a: 75, ejecuta: 1); con `sujeto_id`: 60; con `sujeto_propuesto`: **16**; sin ninguno: 0.

| clave | etiqueta | n | 3b | v2 | unidades | TOs | ¿clave presente en el primario? |
|---|---|---:|---:|---:|---:|---:|---|
| `banc+public` | Bancos públicos de segundo grado | 4 | 4 | 0 | 1 | 1 | no (grupo nuevo del retocado) |
| `agenc+complementar` | agencias complementarias de servicios financieros | 3 | 3 | 0 | 1 | 1 | si — no pasa el corte |
| `representant+entidad` | Representantes de entidades financieras del exterior no autorizadas | 3 | 3 | 0 | 1 | 1 | si — no pasa el corte |
| `director+entidad` | Directorio de entidades financieras | 2 | 0 | 2 | 1 | 1 | no (grupo nuevo del retocado) |
| `cryl` | CRyL | 1 | 1 | 0 | 1 | 1 | si — no pasa el corte |
| `cuent+registr` | cuentas de registro | 1 | 1 | 0 | 1 | 1 | no (grupo nuevo del retocado) |
| `director+alta` | Directorio y Alta Gerencia de entidades financieras | 1 | 0 | 1 | 1 | 1 | no (grupo nuevo del retocado) |
| `entidad+financier` | Entidades financieras obligadas a provisionar | 1 | 1 | 0 | 1 | 1 | si — no pasa el corte |

## 6. Alcance

Este documento entrega la medicion. **No propone ni decide** la lista final del
catalogo de sujetos: eso es de la autora con B5.4 (las dos variantes del diseño
la reciben como insumo comun).

Limitaciones conocidas del agrupador, declaradas antes de leer la tabla:

- Sin tabla de sinonimos: sujetos sinonimos ('aseguradoras' / 'empresas de
  seguros') quedan en grupos distintos — los conteos por grupo son cota inferior.
- La clave ve solo las dos primeras palabras de contenido: un tercer modificador
  ('… del exterior' en tercera posicion) no separa grupos. Las formas de
  superficie del JSON dejan esos matices a la vista.
- El recorte morfologico es de un solo sufijo con raiz minima de 4: pares
  morfologicamente lejanos no se funden. Se deja asi, no se fuerza.
