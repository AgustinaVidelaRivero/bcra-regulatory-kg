# U-ESQ-V3 fase 1 — Adjudicación de MIEMBROS de los 30 roles de alcance v3

**Esto es una PROPUESTA mecánica en freno. Nada se escribió en ningún artefacto.**
La adjudicación es de la autora, fila por fila: la última columna está vacía a propósito.

Colectivos que los pasajes nombran: **69** en 30 roles · con candidato mecánico: **43** (idénticos 26, recorte declarado 9, **más amplios (aplanan) 8**) · **sin id en el catálogo v3: 26** · candidatos de nivel `instancia`: **2** · roles sin ninguna marca: **2** de 30.

Fuente de los colectivos: `prompt_v3_b54.ROLES_V3` (módulo SELLADO, solo lectura) — ya adjudicados por U-B5.4 fase 1 con su pasaje. Fuente de los pasajes: `data/experiment/escalado_prep/e0_dry/<to>/chunks_<to>.json`.

**Criterio (fijado por el mandato, no se re-decide):** el miembro de un rol es la clase que el pasaje NOMBRA, a la granularidad en que la nombra — ni expandida a sus subclases ni colapsada a su clase madre. Un pasaje que enumera tres colectivos da tres miembros.

**Columna `relacion`** — qué tan literal es el candidato respecto del colectivo: `identico` = coinciden · `recorte_declarado` = coinciden sus núcleos y el colectivo trae una aclaración que el candidato no porta (puede ser inocua —una sección, la ley que define al sujeto— o restrictiva; distinguirlas es juicio) · **`mas_amplio` = el candidato cubre MÁS que el colectivo: es el padre, y adoptarlo ES aplanar a la madre**, que el criterio prohíbe.

**Marcas:** `MULTI_SUJETO` = el pasaje enumera más de un colectivo (pide juicio, no matcheo) · `SIN_ID_EN_CATALOGO` = algún colectivo nombrado no tiene id en el catálogo v3 (el matcheo NO sube al padre por su cuenta) · `APLANA_A_LA_MADRE` = algún candidato es `mas_amplio` · `CANDIDATO_INSTANCIA` = algún candidato es nivel `instancia`, no `clase` (los 17 miembros vigentes del grafo son los 17 de nivel `clase`).

| # | TO | rol_id | colectivo que el pasaje nombra | candidato mecánico | regla | relacion | nivel | marcas del rol | cita | **adjudicación de la autora** |
|---:|---|---|---|---|---|---|---|---|---|---|
| 1 | adrei | `Sujeto_rol_alcance_adrei` | Entidades financieras de importancia sistémica local (D-SIB) | `Sujeto_entidad_financiera` ⚠ | R5_madre_APLANA | mas_amplio | clase | APLANA_A_LA_MADRE | `adrei::1.1` |  |
| 2 | autenf | `Sujeto_rol_alcance_autenf` | Personas que ejercen cargos de administración, fiscalización o gerencia en entidades financier… | **— (sin id)** | NINGUNO | — | — | SIN_ID_EN_CATALOGO | `autenf::1.1::intro` |  |
| 3 | ccbcra | `Sujeto_rol_alcance_ccbcra` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO | `ccbcra::1.1` |  |
| 4 |  |  | Cajas de crédito (Ley 25.782) | `Sujeto_caja_de_credito` | R3_nucleo | recorte_declarado | clase |  |  |  |
| 5 |  |  | Entidades cambiarias | `Sujeto_entidad_cambiaria` | R1_label_exacto | identico | clase |  |  |  |
| 6 | convca | `Sujeto_rol_alcance_convca` | Entidades financieras y otras habilitadas a conversión cambiaria | `Sujeto_entidad_financiera` ⚠ | R5_madre_APLANA | mas_amplio | clase | APLANA_A_LA_MADRE | `convca::1.1` |  |
| 7 | cryl | `Sujeto_rol_alcance_cryl` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO | `cryl::3.1` |  |
| 8 |  |  | Mercados de Valores del país | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 9 |  |  | Fondos comunes de inversión | `Sujeto_fondo_comun_de_inversion` | R1_label_exacto | identico | clase |  |  |  |
| 10 |  |  | Centrales depositarias de valores | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 11 |  |  | Cámaras electrónicas de compensación (CEC) | `Sujeto_camara_electronica_de_compensacion` | R1_label_exacto | identico | clase |  |  |  |
| 12 | ctacor | `Sujeto_rol_alcance_ctacor` | Entidades financieras del país | `Sujeto_entidad_financiera` ⚠ | R5_madre_APLANA | mas_amplio | clase | MULTI_SUJETO, APLANA_A_LA_MADRE | `ctacor::1.1` |  |
| 13 |  |  | Casas de cambio (Sección 3) | `Sujeto_casa_de_cambio` | R3_nucleo | recorte_declarado | clase |  |  |  |
| 14 | depaho | `Sujeto_rol_alcance_depaho` | Bancos comerciales de primer grado | `Sujeto_banco_comercial` ⚠ | R5_madre_APLANA | mas_amplio | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO, APLANA_A_LA_MADRE | `depaho::1.1.1` |  |
| 15 |  |  | Compañías financieras | `Sujeto_compania_financiera` | R1_label_exacto | identico | clase |  |  |  |
| 16 |  |  | Cajas de crédito | `Sujeto_caja_de_credito` | R1_label_exacto | identico | clase |  |  |  |
| 17 |  |  | Sociedades de ahorro y préstamo para la vivienda u otros inmuebles | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 18 | efemin | `Sujeto_rol_alcance_efemin` | Entidades financieras (filiales del país) | `Sujeto_entidad_financiera` | R3_nucleo | recorte_declarado | clase |  | `efemin::4.1` |  |
| 19 | fabcra | `Sujeto_rol_alcance_fabcra` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO, CANDIDATO_INSTANCIA | `fabcra::S1::chapeau_seccion` |  |
| 20 |  |  | Operadores de cambio | `Sujeto_entidad_cambiaria` | R2_alias_exacto | identico | clase |  |  |  |
| 21 |  |  | Cámaras electrónicas de compensación | `Sujeto_camara_electronica_de_compensacion` | R1_label_exacto | identico | clase |  |  |  |
| 22 |  |  | Cajas de valores | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 23 |  |  | Mercados | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 24 |  |  | Compañías financieras | `Sujeto_compania_financiera` | R1_label_exacto | identico | clase |  |  |  |
| 25 |  |  | Agentes de liquidación y compensación | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 26 |  |  | Ministerio de Economía | `Sujeto_ministerio_de_economia` | R1_label_exacto | identico | instancia |  |  |  |
| 27 |  |  | ANSES | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 28 | icmecma | `Sujeto_rol_alcance_icmecma` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO | `icmecma::1.1.1` |  |
| 29 |  |  | Empresas no financieras emisoras de tarjetas de crédito y/o compra | `Sujeto_empresa_no_financiera_emisora_de_tarjetas` | R1_label_exacto | identico | clase |  |  |  |
| 30 |  |  | Fiduciarios de fideicomisos financieros | `Sujeto_fiduciario_de_fideicomiso_financiero` | R1_label_exacto | identico | clase |  |  |  |
| 31 |  |  | Administradores de carteras crediticias de ex-entidades financieras | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 32 |  |  | Otros proveedores no financieros de crédito | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 33 | lavdin | `Sujeto_rol_alcance_lavdin` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO | `lavdin::1.1::intro` |  |
| 34 |  |  | Entidades cambiarias | `Sujeto_entidad_cambiaria` | R1_label_exacto | identico | clase |  |  |  |
| 35 | ordcom | `Sujeto_rol_alcance_ordcom` | BCRA (emisor) | `Sujeto_bcra` | R3_nucleo | recorte_declarado | instancia | MULTI_SUJETO, SIN_ID_EN_CATALOGO, CANDIDATO_INSTANCIA | `ordcom::1.5::intro` |  |
| 36 |  |  | Destinatarios de Comunicaciones (entidades financieras, cajas de crédito cooperativas, etc.) | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 37 | osapsa | `Sujeto_rol_alcance_osapsa` | Entidades financieras (Secciones 2, 4 y 5) | `Sujeto_entidad_financiera` | R3_nucleo | recorte_declarado | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO | `osapsa::1.1` |  |
| 38 |  |  | Empresas no financieras emisoras de tarjetas (Secciones 3 y 5) | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 39 |  |  | Operadores de cambio y empresas de cobranzas extrabancarias (Sección 5) | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 40 | pagjub | `Sujeto_rol_alcance_pagjub` | Entidades financieras participantes del pago de beneficios ANSES | `Sujeto_entidad_financiera` ⚠ | R5_madre_APLANA | mas_amplio | clase | APLANA_A_LA_MADRE | `pagjub::1.1` |  |
| 41 | pfmipyme | `Sujeto_rol_alcance_pfmipyme` | Plataformas para el financiamiento MiPyME (PFM) | **— (sin id)** | NINGUNO | — | — | SIN_ID_EN_CATALOGO | `pfmipyme::1.1.1` |  |
| 42 | pimf | `Sujeto_rol_alcance_pimf` | Infraestructuras del mercado financiero (IMF) nominadas en la Sección 5 | **— (sin id)** | NINGUNO | — | — | SIN_ID_EN_CATALOGO | `pimf::5.1` |  |
| 43 | ratiofn | `Sujeto_rol_alcance_ratiofn` | Entidades financieras D-SIB | `Sujeto_entidad_financiera` ⚠ | R5_madre_APLANA | mas_amplio | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO, APLANA_A_LA_MADRE | `ratiofn::1.1` |  |
| 44 |  |  | Sucursales o subsidiarias de bancos del exterior G-SIB | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 45 | rdbcra | `Sujeto_rol_alcance_rdbcra` | Personas jurídicas y humanas sometidas al ámbito de la Ley de Entidades Financieras | `Sujeto_persona_juridica` ⚠ | R5_madre_APLANA | mas_amplio | clase | APLANA_A_LA_MADRE | `rdbcra::1.1.1.1` |  |
| 46 | repefe | `Sujeto_rol_alcance_repefe` | Representantes de entidades financieras del exterior no autorizadas | **— (sin id)** | NINGUNO | — | — | SIN_ID_EN_CATALOGO | `repefe::1.1` |  |
| 47 | retype | `Sujeto_rol_alcance_retype` | Banco de la Nación Argentina | **— (sin id)** | NINGUNO | — | — | MULTI_SUJETO, SIN_ID_EN_CATALOGO | `retype::1.1.2` |  |
| 48 |  |  | Otros bancos públicos participantes (IAF) | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 49 | rmrtsd | `Sujeto_rol_alcance_rmrtsd` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO | `rmrtsd::1.1.1` |  |
| 50 |  |  | Proveedores de servicios de pago (PSP) | `Sujeto_proveedor_de_servicios_de_pago` | R3_nucleo | recorte_declarado | clase |  |  |  |
| 51 | rrci | `Sujeto_rol_alcance_rrci` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO | `rrci::1.2` |  |
| 52 |  |  | PSP incluidos en el Registro del BCRA | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 53 |  |  | Infraestructuras del mercado financiero de importancia sistémica | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 54 | servco | `Sujeto_rol_alcance_servco` | Entidades financieras (Sección 2: bancos comerciales y compañías financieras) | `Sujeto_entidad_financiera` | R3_nucleo | recorte_declarado | clase |  | `servco::1.1` |  |
| 55 | snp_atm | `Sujeto_rol_alcance_snp_atm` | Entidades financieras que ofrezcan cuentas a la vista | `Sujeto_entidad_financiera` ⚠ | R5_madre_APLANA | mas_amplio | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO, APLANA_A_LA_MADRE | `snp_atm::1.1.1` |  |
| 56 |  |  | Empresas no financieras operadoras de cajeros automáticos | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 57 | snp_debin | `Sujeto_rol_alcance_snp_debin` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO | `snp_debin::2.1` |  |
| 58 |  |  | PSPCP | `Sujeto_pspcp` | R2_alias_exacto | identico | clase |  |  |  |
| 59 | snp_psp | `Sujeto_rol_alcance_snp_psp` | Proveedores de servicios de pago (PSP) | `Sujeto_proveedor_de_servicios_de_pago` | R3_nucleo | recorte_declarado | clase | MULTI_SUJETO | `snp_psp::1.1.2` |  |
| 60 |  |  | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase |  |  |  |
| 61 | snp_spd | `Sujeto_rol_alcance_snp_spd` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO | `snp_spd::S1::chapeau_seccion` |  |
| 62 |  |  | PSP (según el servicio) | `Sujeto_proveedor_de_servicios_de_pago` | R4_sigla_acronimo | identico | clase |  |  |  |
| 63 | snp_tr_nc | `Sujeto_rol_alcance_snp_tr_nc` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO | `snp_tr_nc::1.2.1` |  |
| 64 |  |  | Proveedores de servicios de pago (PSP) | `Sujeto_proveedor_de_servicios_de_pago` | R3_nucleo | recorte_declarado | clase |  |  |  |
| 65 | supcon | `Sujeto_rol_alcance_supcon` | Entidades financieras | `Sujeto_entidad_financiera` | R1_label_exacto | identico | clase | MULTI_SUJETO, SIN_ID_EN_CATALOGO | `supcon::2.2::intro` |  |
| 66 |  |  | Empresas del perímetro de supervisión consolidada | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 67 | traval | `Sujeto_rol_alcance_traval` | Transportadoras de valores (TV) | **— (sin id)** | NINGUNO | — | — | MULTI_SUJETO, SIN_ID_EN_CATALOGO | `traval::1.1::intro` |  |
| 68 |  |  | Prestadoras de Servicios de Transporte de Valores (PSTV) | **— (sin id)** | NINGUNO | — | — |  |  |  |
| 69 |  |  | Transportadoras de Valores Propias (TVP) | **— (sin id)** | NINGUNO | — | — |  |  |  |

## Los 26 colectivos SIN id en el catálogo v3

El pasaje los nombra y el catálogo v3 no los tiene. El matcheo **no los sube al padre**: hacerlo sería colapsar a la madre. Las tres salidas posibles —dejar el rol con menos miembros que los que su pasaje nombra, aceptar el aplanamiento declarándolo, o abrir el catálogo (que es re-sello del prefijo v3 y por lo tanto otra unidad)— son adjudicación de la autora, no de esta tabla.

La columna **pista** NO es un candidato: es la entrada del catálogo con mayor solapamiento de palabras (≥ 0,34), ofrecida solo para que el juicio tenga a mano lo más cercano que hay. Vacía = ni siquiera hay algo cercano.

| # | TO | colectivo que el pasaje nombra | pista (no es candidato) | solapamiento |
|---:|---|---|---|---|
| 1 | autenf | Personas que ejercen cargos de administración, fiscalización o gerencia en entidades financier… | — | — |
| 2 | cryl | Mercados de Valores del país | — | — |
| 3 | cryl | Centrales depositarias de valores | — | — |
| 4 | depaho | Sociedades de ahorro y préstamo para la vivienda u otros inmuebles | — | — |
| 5 | fabcra | Cajas de valores | — | — |
| 6 | fabcra | Mercados | — | — |
| 7 | fabcra | Agentes de liquidación y compensación | — | — |
| 8 | fabcra | ANSES | — | — |
| 9 | icmecma | Administradores de carteras crediticias de ex-entidades financieras | — | — |
| 10 | icmecma | Otros proveedores no financieros de crédito | `Sujeto_proveedor_no_financiero_de_credito` — Proveedores no financieros de crédito | 0.8 |
| 11 | ordcom | Destinatarios de Comunicaciones (entidades financieras, cajas de crédito cooperativas, etc.) | `Sujeto_caja_de_credito_cooperativa` — Cajas de crédito cooperativas | 0.38 |
| 12 | osapsa | Empresas no financieras emisoras de tarjetas (Secciones 3 y 5) | `Sujeto_empresa_no_financiera_emisora_de_tarjetas` — Empresas no financieras emisoras de tarjetas de crédito y/o compra | 0.5 |
| 13 | osapsa | Operadores de cambio y empresas de cobranzas extrabancarias (Sección 5) | — | — |
| 14 | pfmipyme | Plataformas para el financiamiento MiPyME (PFM) | — | — |
| 15 | pimf | Infraestructuras del mercado financiero (IMF) nominadas en la Sección 5 | — | — |
| 16 | ratiofn | Sucursales o subsidiarias de bancos del exterior G-SIB | — | — |
| 17 | repefe | Representantes de entidades financieras del exterior no autorizadas | — | — |
| 18 | retype | Banco de la Nación Argentina | — | — |
| 19 | retype | Otros bancos públicos participantes (IAF) | — | — |
| 20 | rrci | PSP incluidos en el Registro del BCRA | — | — |
| 21 | rrci | Infraestructuras del mercado financiero de importancia sistémica | — | — |
| 22 | snp_atm | Empresas no financieras operadoras de cajeros automáticos | — | — |
| 23 | supcon | Empresas del perímetro de supervisión consolidada | `Sujeto_sujeto_del_perimetro_consolidado` — Sujetos del perímetro de supervisión consolidada | 0.6 |
| 24 | traval | Transportadoras de valores (TV) | — | — |
| 25 | traval | Prestadoras de Servicios de Transporte de Valores (PSTV) | — | — |
| 26 | traval | Transportadoras de Valores Propias (TVP) | — | — |

## Pasajes de alcance (verbatim de e0_dry, uno por rol)

### adrei — `Sujeto_rol_alcance_adrei`
**Label del rol:** Entidades alcanzadas (Agregación de datos sobre riesgos: D-SIB)  
**Cita:** `adrei::1.1` · página(s) [3] · unidad «Ámbito de aplicación.»  
**Marcas:** APLANA_A_LA_MADRE

```
1.1. Ámbito de aplicación.
Las presentes normas rigen para las entidades financieras que sean consideradas por el Banco
Central de la República Argentina como de importancia sistémica a nivel local (D-SIB), luego de
transcurridos 3 años contados a partir del primer día hábil del mes siguiente al de la fecha de la
notificación de su designación como tales.
Sus disposiciones son de aplicación a los procesos de gestión de riesgos –incluso los que se
subcontraten a terceros– tanto a nivel individual como del grupo económico, sin perjuicio de que
puedan aplicarse también a otros procesos –tales como financieros y operativos– y a la elabo-
ración de informes con fines de control interno.
```

### autenf — `Sujeto_rol_alcance_autenf`
**Label del rol:** Autoridades comprendidas (Autoridades de entidades financieras)  
**Cita:** `autenf::1.1::intro` · página(s) [4] · unidad «[bloque intro] Autoridades comprendidas.»  
**Marcas:** SIN_ID_EN_CATALOGO

```
Las normas sobre “Autoridades de entidades financieras” son aplicables a las personas que
ejercen los siguientes cargos:
```

### ccbcra — `Sujeto_rol_alcance_ccbcra`
**Label del rol:** Entidades alcanzadas (Cuentas a la vista en el BCRA)  
**Cita:** `ccbcra::1.1` · página(s) [3] · unidad «Entidades alcanzadas.»  
**Marcas:** MULTI_SUJETO

```
1.1. Entidades alcanzadas.
Las entidades financieras deberán mantener abierta en el Banco Central de la República Ar-
gentina una cuenta corriente en pesos. Dicha cuenta tendrá carácter optativo para las cajas de
crédito (Ley 25.782) y las entidades cambiarias.
Sin perjuicio de ello, todas las entidades antes mencionadas podrán mantener cuentas a la vis-
ta en dólares estadounidenses u otras monedas extranjeras, cuando -dentro de las
modalidades legal y reglamentariamente admitidas para ellas- reciban depósitos en esas espe-
cies.
```

### convca — `Sujeto_rol_alcance_convca`
**Label del rol:** Entidades habilitadas (Conversión cambiaria)  
**Cita:** `convca::1.1` · página(s) [3] · unidad «Concepto de conversión cambiaria.»  
**Marcas:** APLANA_A_LA_MADRE

```
1.1. Concepto de conversión cambiaria.
Son operaciones de conversión cambiaria las que realiza el Banco Central a solicitud de las en-
tidades financieras y otras habilitadas, mediante la emisión y recepción de transferencias de dó-
lares estadounidenses entre sus cuentas corrientes abiertas en el Banco Central y otras cuen-
tas propias o de terceros radicadas en bancos de plaza Nueva York.
```

### cryl — `Sujeto_rol_alcance_cryl`
**Label del rol:** Sujetos habilitados (CRyL)  
**Cita:** `cryl::3.1` · página(s) [6] · unidad «Sujetos habilitados.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO

```
3.1. Sujetos habilitados.
Dispondrán de cuentas de registro:
a) Las entidades comprendidas en la Ley 21.526 – “Ley de Entidades Financieras”, que se en-
cuentren debidamente autorizadas por el BCRA.
b) Mercados de Valores del país.
c) Fondos Comunes de Inversión cuyos cuotapartistas sean residentes en el país.
d) Centrales Depositarias de Valores Nacionales e Internacionales.
e) Cámaras Electrónicas de Compensación (CEC).
f) Toda aquella institución que a juicio del BCRA y/o del Órgano Coordinador de los Sistemas
de Administración Financiera, resulte conveniente darle participación.
A tal fin, los interesados deberán presentar una nota solicitando la apertura de cuenta/s de
registro ante la Gerencia de Operaciones con Títulos y Divisas.
En el mismo sentido, para llevar adelante sus operaciones deberán solicitar la apertura de las
cuentas corrientes monetarias que considere necesarias. A tal efecto, deberán realizar dicha
solicitud según lo que establezca la Gerencia de Cuentas Corrientes.
```

### ctacor — `Sujeto_rol_alcance_ctacor`
**Label del rol:** Entidades intervinientes (Cuentas de corresponsalía)  
**Cita:** `ctacor::1.1` · página(s) [3] · unidad «Entidades intervinientes.»  
**Marcas:** MULTI_SUJETO, APLANA_A_LA_MADRE

```
1.1. Entidades intervinientes.
Las entidades financieras del país se encuentran facultadas para ofrecer la apertura de
cuentas y la provisión de sus servicios relacionados a otras entidades financieras del país para
la realización de transacciones locales admitidas, a fin de dar curso a las operaciones que
estas últimas efectúen por cuenta de terceros, relativas a: liquidación de cobros y pagos,
gestión de liquidez, de préstamos, recaudación, transferencias y compensación, con
observancia de lo dispuesto por las normas sobre “Política de crédito”.
Estas normas no serán de aplicación respecto de la apertura de cuentas de custodia a
entidades financieras del país y del exterior y para aquellas cuentas a la vista abiertas en
entidades financieras del país por casas de cambio locales y/o por entidades financieras
locales y del exterior, siempre que sean utilizadas exclusivamente para la realización por
cuenta propia de transacciones locales de cobros y pagos.
```

### depaho — `Sujeto_rol_alcance_depaho`
**Label del rol:** Entidades intervinientes (Depósitos de ahorro)  
**Cita:** `depaho::1.1.1` · página(s) [5] · unidad «Bancos comerciales de primer grado.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO, APLANA_A_LA_MADRE

```
1.1.1. Bancos comerciales de primer grado.
```

### efemin — `Sujeto_rol_alcance_efemin`
**Label del rol:** Entidades alcanzadas (Efectivo mínimo)  
**Cita:** `efemin::4.1` · página(s) [23] · unidad «Base individual.»  
**Marcas:** —

```
4.1. Base individual.
Las entidades financieras (comprendidas exclusivamente sus filiales en el país) observarán las
normas en materia de efectivo mínimo en forma individual.
```

### fabcra — `Sujeto_rol_alcance_fabcra`
**Label del rol:** Entidades registrantes de firmas (Firmas autorizadas ante el BCRA)  
**Cita:** `fabcra::S1::chapeau_seccion` · página(s) [3] · unidad «[bloque chapeau_seccion] Registro de firmas autorizadas»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO, CANDIDATO_INSTANCIA

```
La fórmula 2570 es el soporte utilizado por las entidades financieras, operadores de cambio, cáma-
ras electrónicas de compensación, cajas de valores, mercados, compañías financieras, agentes de
liquidación y compensación, Ministerio de Economía y Administración Nacional de la Seguridad So-
cial (ANSES) –en adelante, también “entidades”– para registrar ante el Banco Central de la Repúbli-
ca Argentina (BCRA) a las personas autorizadas a operar sus cuentas corrientes y/u otras abiertas
en el BCRA.
```

### icmecma — `Sujeto_rol_alcance_icmecma`
**Label del rol:** Sujetos alcanzados (Comunicación por medios electrónicos)  
**Cita:** `icmecma::1.1.1` · página(s) [3] · unidad «Entidades financieras.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO

```
1.1.1. Entidades financieras.
```

### lavdin — `Sujeto_rol_alcance_lavdin`
**Label del rol:** Entidades alcanzadas (Prevención del lavado de activos)  
**Cita:** `lavdin::1.1::intro` · página(s) [3] · unidad «[bloque intro] Normativa aplicable.»  
**Marcas:** MULTI_SUJETO

```
Las entidades financieras y cambiarias deberán observar lo establecido en la legislación vigen-
te en estas materias (leyes y decretos reglamentarios), en las normas relacionadas emitidas
por la Unidad de Información Financiera (UIF) y en la presente reglamentación. Ello incluye los
decretos del Poder Ejecutivo Nacional con referencia a las decisiones adoptadas por el Conse-
jo de Seguridad de las Naciones Unidas en la lucha contra el terrorismo y dar cumplimiento a
las Resoluciones (con sus respectivos Anexos) dictadas por el Ministerio de Relaciones Exte-
riores y Culto.
Tales disposiciones también deberán ser observadas por los representantes de entidades fi-
nancieras del exterior no autorizadas para operar en el país.
```

### ordcom — `Sujeto_rol_alcance_ordcom`
**Label del rol:** Destinatarios de Comunicaciones (Ordenamiento de Comunicaciones)  
**Cita:** `ordcom::1.5::intro` · página(s) [5] · unidad «[bloque intro] Destinatarios.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO, CANDIDATO_INSTANCIA

```
En los encabezamientos de las comunicaciones “A”, “B”, “C” y “D” se establecerán las denomi-
naciones de los destinatarios, los cuales pueden ser uno o varios de los siguientes:
```

### osapsa — `Sujeto_rol_alcance_osapsa`
**Label del rol:** Sujetos alcanzados (Otros servicios y actividades)  
**Cita:** `osapsa::1.1` · página(s) [3] · unidad «Entidades financieras.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO

```
1.1. Entidades financieras.
Serán de aplicación las disposiciones contenidas en las Secciones 2., 4. y 5.
```

### pagjub — `Sujeto_rol_alcance_pagjub`
**Label del rol:** Entidades participantes (Pago de beneficios ANSES)  
**Cita:** `pagjub::1.1` · página(s) [3] · unidad «Entidades participantes.»  
**Marcas:** APLANA_A_LA_MADRE

```
1.1. Entidades participantes.
Las entidades financieras que participen del servicio de pago de beneficios por cuenta de la
Administración Nacional de la Seguridad Social (ANSES) deberán utilizar los instrumentos de
pago y la metodología que ese ente administrador establezca.
```

### pfmipyme — `Sujeto_rol_alcance_pfmipyme`
**Label del rol:** Plataformas para el financiamiento MiPyME (PFM)  
**Cita:** `pfmipyme::1.1.1` · página(s) [3] · unidad «Se consideran plataformas para el financiamiento MiPyME (PFM) a las personas jurídi-»  
**Marcas:** SIN_ID_EN_CATALOGO

```
1.1.1. Se consideran plataformas para el financiamiento MiPyME (PFM) a las personas jurídi-
cas que facilitan –como actividad principal o accesoria de su objeto social–, a través de
herramientas y/o sistemas informáticos, la concertación de operaciones con facturas de
crédito electrónicas MiPyME (FCEM) en los términos previstos en el artículo 13 de la
Ley 27.440 de Financiamiento Productivo, así como de otros instrumentos que la regla-
mentación determine como admisibles.
```

### pimf — `Sujeto_rol_alcance_pimf`
**Label del rol:** Infraestructuras del mercado financiero alcanzadas (PIMF)  
**Cita:** `pimf::5.1` · página(s) [27] · unidad «Nómina»  
**Marcas:** SIN_ID_EN_CATALOGO

```
5.1. Nómina
Las siguientes IMF deberán cumplir con la aplicación de los principios en el marco de una
revisión integral periódica y teniendo en cuenta los lineamientos establecidos en estas nor-
mas:
– Medio Electrónico de Pagos (MEP)
– Cámara de Alto Valor –INTERBANKING–
– Cámara de Bajo Valor –Compensadora Electrónica SA (COELSA)–
– Redes de cajeros automáticos –Red Link SA y Newpay SAU–
– Administradores de esquemas de pago de transferencias electrónicas de fondos – IN-
TERBANKING, COELSA, Red Link SA y Newpay SAU–
– Central de Registro y Liquidación de Instrumentos de Endeudamiento Público (CRYL)
– Caja de Valores SA (CVSA)
– Argentina Clearing y Registro SA (ACyRSA)
– Mercado Argentino de Valores SA (MAV)
```

### ratiofn — `Sujeto_rol_alcance_ratiofn`
**Label del rol:** Entidades alcanzadas (Ratio de fondeo neto estable: D-SIB y suc. G-SIB)  
**Cita:** `ratiofn::1.1` · página(s) [3] · unidad «Alcance.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO, APLANA_A_LA_MADRE

```
1.1. Alcance.
Las entidades financieras calificadas por el Banco Central de la República Argentina (BCRA)
como de importancia sistémica a nivel local (D-SIB) y las sucursales o subsidiarias de bancos
del exterior calificados como de importancia sistémica global (G-SIB) deberán cumplir las pre-
sentes disposiciones.
Las entidades financieras que presenten cambios en su calificación –conforme a lo previsto
precedentemente– contarán con un plazo de 3 meses para aplicar las disposiciones específicas
correspondientes al nuevo grupo al que pertenezcan.
Las entidades financieras que pertenezcan al grupo A –según lo previsto en el punto 4.1. del
TO sobre Autoridades de Entidades Financieras– no alcanzadas por estas normas deberán
presentar el régimen informativo que corresponda.
La Superintendencia de Entidades Financieras y Cambiarias (SEFYC) podrá requerir informa-
ción adicional a las entidades financieras cuando ello resulte necesario para evaluar su situa-
ción de liquidez.
A los efectos de estas normas, el término “sector financiero” comprende a las entidades finan-
cieras, cambiarias, aseguradoras, agentes regulados por la Comisión Nacional de Valores
(CNV) –o autoridad equivalente del exterior– y los fiduciarios de fideicomisos no financieros.
```

### rdbcra — `Sujeto_rol_alcance_rdbcra`
**Label del rol:** Personas sumariables (Régimen disciplinario del BCRA)  
**Cita:** `rdbcra::1.1.1.1` · página(s) [3] · unidad «Las personas jurídicas y humanas sometidas al ámbito de aplicación de la cita-»  
**Marcas:** APLANA_A_LA_MADRE

```
1.1.1.1. Las personas jurídicas y humanas sometidas al ámbito de aplicación de la cita-
da ley y/o alcanzadas según sus disposiciones, incluidas aquellas respecto de
las cuales se hubiere decidido hacer extensivos sus términos, conforme al ar-
tículo 3 de la LEF.
```

### repefe — `Sujeto_rol_alcance_repefe`
**Label del rol:** Representantes de entidades financieras del exterior (Representantes)  
**Cita:** `repefe::1.1` · página(s) [3] · unidad «Concepto.»  
**Marcas:** SIN_ID_EN_CATALOGO

```
1.1. Concepto.
Es representante de entidad financiera del exterior no autorizada para operar en el país, la
persona física autorizada por el Banco Central de la República Argentina -Superintendencia de
Entidades Financieras y Cambiarias- para actuar localmente en nombre y representación de tal
entidad, ya sea como apoderado, agente o cualquier otro carácter, a fin de desarrollar las
operaciones permitidas en el punto 1.4. de la presente sección.
A los efectos de esta reglamentación se considerarán entidades financieras del exterior a
aquellas que, constituidas de acuerdo con el derecho extranjero aplicable, tengan por actividad
permitida desarrollar en las plazas del exterior en que operen, la intermediación habitual entre
la oferta y la demanda de recursos financieros -depósitos del público- en los términos de la Ley
de Entidades Financieras argentina y su reglamentación independientemente del tipo social
que adopten y/o de su carácter público, privado o mixto.
El Banco Central de la República Argentina no dará curso a solicitudes para actuar como
representantes en el país de entidades financieras del exterior constituidas en países
calificados como de baja o nula tributación, según los términos del Decreto 1037/00 y sus
modificatorios.
```

### retype — `Sujeto_rol_alcance_retype`
**Label del rol:** Entidades bancarias participantes (Pago de retiros y pensiones militares)  
**Cita:** `retype::1.1.2` · página(s) [3] · unidad «Otros bancos públicos.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO

```
1.1.2. Otros bancos públicos.
Las entidades bancarias participantes efectuarán el pago de los beneficios que el Instituto
de Ayuda Financiera para Pago de Retiros y Pensiones Militares (IAF) les indique, por in-
termedio de todas sus casas.
```

### rmrtsd — `Sujeto_rol_alcance_rmrtsd`
**Label del rol:** Sujetos obligados (Servicios financieros digitales)  
**Cita:** `rmrtsd::1.1.1` · página(s) [3] · unidad «Entidades financieras.»  
**Marcas:** MULTI_SUJETO

```
1.1.1. Entidades financieras.
```

### rrci — `Sujeto_rol_alcance_rrci`
**Label del rol:** Sujetos alcanzados (Respuesta y recuperación ante ciberincidentes)  
**Cita:** `rrci::1.2` · página(s) [3] · unidad «Sujetos alcanzados.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO

```
1.2. Sujetos alcanzados.
- Entidades financieras.
- Proveedores de servicios de pago (PSP) incluidos en el Registro de PSP del BCRA.
- Infraestructuras del mercado financiero conocidas como sistemas de pago de importancia
sistémica.
Los sujetos alcanzados analizarán efectivamente la implementación de los lineamientos pu-
diendo elegir implementar las prácticas que sean adecuadas para sus modelos de negocios,
teniendo en cuenta su tamaño, complejidad o riesgos en relación con el ecosistema financiero.
Se dejará constancia escrita de los fundamentos de los criterios de implementación adoptados,
los que deberán ser puestos a disposición de la Superintendencia de Entidades Financieras y
Cambiarias (SEFYC), cuando esta lo solicite.
```

### servco — `Sujeto_rol_alcance_servco`
**Label del rol:** Entidades alcanzadas (Servicios complementarios)  
**Cita:** `servco::1.1` · página(s) [3] · unidad «Prohibición.»  
**Marcas:** —

```
1.1. Prohibición.
Las entidades financieras no se encuentran facultadas a efectuar –cualquiera sea su modali-
dad– operaciones ajenas a la intermediación financiera, conforme a las previsiones contenidas
en el Título II de la Ley de Entidades Financieras.
Las entidades financieras no pueden realizar ni facilitar a sus clientes la realización de opera-
ciones con activos digitales –incluidos los criptoactivos y aquellos cuyos rendimientos se de-
terminen en función de las variaciones que ésos registren– que no se encuentren autorizados
por una autoridad reguladora nacional competente ni por el Banco Central de la República Ar-
gentina (BCRA).
Consecuentemente, se encuentra prohibida la explotación por cuenta propia de todas las acti-
vidades industriales, agropecuarias, comerciales y de cualquier otra índole no financiera salvo
las específicamente admitidas por el BCRA.
```

### snp_atm — `Sujeto_rol_alcance_snp_atm`
**Label del rol:** Entidades alcanzadas (SNP - Cajeros automáticos)  
**Cita:** `snp_atm::1.1.1` · página(s) [3] · unidad «Las entidades financieras que ofrezcan cuentas a la vista deberán permitir que sus»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO, APLANA_A_LA_MADRE

```
1.1.1. Las entidades financieras que ofrezcan cuentas a la vista deberán permitir que sus
clientes realicen operaciones a través de cajeros automáticos instalados en el país y
operados por empresas no financieras.
```

### snp_debin — `Sujeto_rol_alcance_snp_debin`
**Label del rol:** Entidades y PSPCP alcanzados (SNP - Débito Inmediato)  
**Cita:** `snp_debin::2.1` · página(s) [5] · unidad «Alcance»  
**Marcas:** MULTI_SUJETO

```
2.1. Alcance
Los DEBIN podrán ser ordenados por personas humanas y jurídicas, titulares de cuentas a la
vista en entidades financieras o de cuentas de pago en PSPCP que, de acuerdo con la presen-
te normativa, estén habilitadas a efectuar órdenes de débito en cuenta, o por cuenta propia de
las entidades financieras.
```

### snp_psp — `Sujeto_rol_alcance_snp_psp`
**Label del rol:** Sujetos alcanzados (SNP - Proveedores de servicios de pago)  
**Cita:** `snp_psp::1.1.2` · página(s) [3] · unidad «Bajo este enfoque funcional, tanto las entidades financieras como los PSP deberán ob-»  
**Marcas:** MULTI_SUJETO

```
1.1.2. Bajo este enfoque funcional, tanto las entidades financieras como los PSP deberán ob-
servar las mismas reglas para funciones iguales que desarrollen en la provisión de ser-
vicios de pago en el marco del sistema nacional de pagos.
```

### snp_spd — `Sujeto_rol_alcance_snp_spd`
**Label del rol:** Sujetos alcanzados (SNP - Servicios de pago)  
**Cita:** `snp_spd::S1::chapeau_seccion` · página(s) [4] · unidad «[bloque chapeau_seccion] Clave Bancaria Uniforme»  
**Marcas:** MULTI_SUJETO

```
Las entidades financieras deben asignarle una Clave Bancaria Uniforme (CBU) a toda cuenta a la
vista, e informarla a sus clientes para que la puedan utilizar en las operatorias que la requieran.
```

### snp_tr_nc — `Sujeto_rol_alcance_snp_tr_nc`
**Label del rol:** Sujetos alcanzados (SNP - Transferencias - Normas complementarias)  
**Cita:** `snp_tr_nc::1.2.1` · página(s) [3] · unidad «Enfoque funcional: la presente reglamentación se aplicará por función dentro de un es-»  
**Marcas:** MULTI_SUJETO

```
1.2.1. Enfoque funcional: la presente reglamentación se aplicará por función dentro de un es-
quema de pago, de manera que sea homogénea para diferentes tipos de entidades que
cumplan una misma función y por lo tanto compitan, ya sean entidades financieras o
proveedores de servicios de pago (PSP). Las entidades financieras y los PSP podrán
cumplir múltiples funciones dentro de un esquema de pago en tanto las presentes nor-
mas no las limiten expresamente.
```

### supcon — `Sujeto_rol_alcance_supcon`
**Label del rol:** Entidades y empresas alcanzadas (Supervisión consolidada)  
**Cita:** `supcon::2.2::intro` · página(s) [5] · unidad «[bloque intro] Clases de entidades y empresas alcanzadas.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO

```
Las definiciones precedentes se aplicarán a entidades y empresas de las siguientes clases:
```

### traval — `Sujeto_rol_alcance_traval`
**Label del rol:** Sujetos comprendidos (Transportadoras de valores)  
**Cita:** `traval::1.1::intro` · página(s) [3] · unidad «[bloque intro] Alcance.»  
**Marcas:** MULTI_SUJETO, SIN_ID_EN_CATALOGO

```
Comprende a las personas jurídicas que desempeñen la actividad de transporte terrestre de va-
lores –Transportadoras de Valores (TV)–. Se entienden comprendidas dentro de dicha defini-
ción a las empresas Prestadoras de Servicios de Transporte de Valores (PSTV) y a las Trans-
portadoras de Valores Propias de las entidades financieras (TVP). A esos efectos, se conside-
rarán valores al dinero –billetes y monedas de curso legal, y billetes y monedas extranjeros– y
al oro.
```

