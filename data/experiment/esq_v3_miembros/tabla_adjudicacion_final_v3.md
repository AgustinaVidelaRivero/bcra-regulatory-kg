# U-ESQ-V3 fase 2 — Adjudicación FINAL de los miembros de los 30 roles v3

Los laudos aplicados fila por fila. Cada decisión lleva su fundamento; ninguna se resolvió por conveniencia del número.

**34 aristas `miembro_de` · 12 roles sin miembro adjudicable (6 sin_id_en_catalogo / 5 aplanamiento_rechazado / 1 instancia_rechazada).**

Filas por decisión, recomputadas contra `adjudicacion_final_v3.json`: `aceptado_enumeracion_parcial` 1 · `aceptado_identico` 25 · `aceptado_recorte_declarado` 8 · `rechazado_aplanamiento` 7 · `rechazado_instancia` 2 · `sin_id_en_catalogo` 26 · **total 69**.

## Las 69 filas

| # | TO | rol_id | colectivo que el pasaje nombra | id | decisión | fundamento |
|---:|---|---|---|---|---|---|
| 1 | adrei | `Sujeto_rol_alcance_adrei` | Entidades financieras de importancia sistémica local (D-SIB) | `Sujeto_entidad_financiera` | ✘ `rechazado_aplanamiento` | laudo (a): el candidato es la clase madre del colectivo; por la regla de herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la regla 1, sobre cada subclase — falsedad en campo estructu… |
| 2 | autenf | `Sujeto_rol_alcance_autenf` | Personas que ejercen cargos de administración, fiscalización o gerencia en enti… | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 3 | ccbcra | `Sujeto_rol_alcance_ccbcra` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 4 |  |  | Cajas de crédito (Ley 25.782) | `Sujeto_caja_de_credito` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 5 |  |  | Entidades cambiarias | `Sujeto_entidad_cambiaria` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 6 | convca | `Sujeto_rol_alcance_convca` | Entidades financieras y otras habilitadas a conversión cambiaria | `Sujeto_entidad_financiera` | ✔ `aceptado_enumeracion_parcial` | laudo (a), excepción: no es aplanamiento sino enumeración parcial — el colectivo pertenece sin condición y lo que falta son las «otras», que no tienen id; omisión con residuo declarado, que el princi… |
| 7 | cryl | `Sujeto_rol_alcance_cryl` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 8 |  |  | Mercados de Valores del país | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 9 |  |  | Fondos comunes de inversión | `Sujeto_fondo_comun_de_inversion` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 10 |  |  | Centrales depositarias de valores | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 11 |  |  | Cámaras electrónicas de compensación (CEC) | `Sujeto_camara_electronica_de_compensacion` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 12 | ctacor | `Sujeto_rol_alcance_ctacor` | Entidades financieras del país | `Sujeto_entidad_financiera` | ✘ `rechazado_aplanamiento` | laudo (a): el candidato es la clase madre del colectivo; por la regla de herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la regla 1, sobre cada subclase — falsedad en campo estructu… |
| 13 |  |  | Casas de cambio (Sección 3) | `Sujeto_casa_de_cambio` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 14 | depaho | `Sujeto_rol_alcance_depaho` | Bancos comerciales de primer grado | `Sujeto_banco_comercial` | ✘ `rechazado_aplanamiento` | laudo (a): el candidato es la clase madre del colectivo; por la regla de herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la regla 1, sobre cada subclase — falsedad en campo estructu… |
| 15 |  |  | Compañías financieras | `Sujeto_compania_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 16 |  |  | Cajas de crédito | `Sujeto_caja_de_credito` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 17 |  |  | Sociedades de ahorro y préstamo para la vivienda u otros inmuebles | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 18 | efemin | `Sujeto_rol_alcance_efemin` | Entidades financieras (filiales del país) | `Sujeto_entidad_financiera` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 19 | fabcra | `Sujeto_rol_alcance_fabcra` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 20 |  |  | Operadores de cambio | `Sujeto_entidad_cambiaria` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 21 |  |  | Cámaras electrónicas de compensación | `Sujeto_camara_electronica_de_compensacion` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 22 |  |  | Cajas de valores | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 23 |  |  | Mercados | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 24 |  |  | Compañías financieras | `Sujeto_compania_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 25 |  |  | Agentes de liquidación y compensación | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 26 |  |  | Ministerio de Economía | `Sujeto_ministerio_de_economia` | ✘ `rechazado_instancia` | laudo (b): miembro_de es Clase → Rol; admitir una instancia cambia la firma del esquema congelado y eso es laudo de la autora sobre el esquema |
| 27 |  |  | ANSES | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 28 | icmecma | `Sujeto_rol_alcance_icmecma` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 29 |  |  | Empresas no financieras emisoras de tarjetas de crédito y/o compra | `Sujeto_empresa_no_financiera_emisora_de_tarjetas` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 30 |  |  | Fiduciarios de fideicomisos financieros | `Sujeto_fiduciario_de_fideicomiso_financiero` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 31 |  |  | Administradores de carteras crediticias de ex-entidades financieras | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 32 |  |  | Otros proveedores no financieros de crédito | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 33 | lavdin | `Sujeto_rol_alcance_lavdin` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 34 |  |  | Entidades cambiarias | `Sujeto_entidad_cambiaria` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 35 | ordcom | `Sujeto_rol_alcance_ordcom` | BCRA (emisor) | `Sujeto_bcra` | ✘ `rechazado_instancia` | laudo (b): miembro_de es Clase → Rol; admitir una instancia cambia la firma del esquema congelado y eso es laudo de la autora sobre el esquema |
| 36 |  |  | Destinatarios de Comunicaciones (entidades financieras, cajas de crédito cooper… | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 37 | osapsa | `Sujeto_rol_alcance_osapsa` | Entidades financieras (Secciones 2, 4 y 5) | `Sujeto_entidad_financiera` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 38 |  |  | Empresas no financieras emisoras de tarjetas (Secciones 3 y 5) | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 39 |  |  | Operadores de cambio y empresas de cobranzas extrabancarias (Sección 5) | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 40 | pagjub | `Sujeto_rol_alcance_pagjub` | Entidades financieras participantes del pago de beneficios ANSES | `Sujeto_entidad_financiera` | ✘ `rechazado_aplanamiento` | laudo (a): el candidato es la clase madre del colectivo; por la regla de herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la regla 1, sobre cada subclase — falsedad en campo estructu… |
| 41 | pfmipyme | `Sujeto_rol_alcance_pfmipyme` | Plataformas para el financiamiento MiPyME (PFM) | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 42 | pimf | `Sujeto_rol_alcance_pimf` | Infraestructuras del mercado financiero (IMF) nominadas en la Sección 5 | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 43 | ratiofn | `Sujeto_rol_alcance_ratiofn` | Entidades financieras D-SIB | `Sujeto_entidad_financiera` | ✘ `rechazado_aplanamiento` | laudo (a): el candidato es la clase madre del colectivo; por la regla de herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la regla 1, sobre cada subclase — falsedad en campo estructu… |
| 44 |  |  | Sucursales o subsidiarias de bancos del exterior G-SIB | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 45 | rdbcra | `Sujeto_rol_alcance_rdbcra` | Personas jurídicas y humanas sometidas al ámbito de la Ley de Entidades Financi… | `Sujeto_persona_juridica` | ✘ `rechazado_aplanamiento` | laudo (a): el candidato es la clase madre del colectivo; por la regla de herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la regla 1, sobre cada subclase — falsedad en campo estructu… |
| 46 | repefe | `Sujeto_rol_alcance_repefe` | Representantes de entidades financieras del exterior no autorizadas | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 47 | retype | `Sujeto_rol_alcance_retype` | Banco de la Nación Argentina | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 48 |  |  | Otros bancos públicos participantes (IAF) | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 49 | rmrtsd | `Sujeto_rol_alcance_rmrtsd` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 50 |  |  | Proveedores de servicios de pago (PSP) | `Sujeto_proveedor_de_servicios_de_pago` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 51 | rrci | `Sujeto_rol_alcance_rrci` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 52 |  |  | PSP incluidos en el Registro del BCRA | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 53 |  |  | Infraestructuras del mercado financiero de importancia sistémica | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 54 | servco | `Sujeto_rol_alcance_servco` | Entidades financieras (Sección 2: bancos comerciales y compañías financieras) | `Sujeto_entidad_financiera` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 55 | snp_atm | `Sujeto_rol_alcance_snp_atm` | Entidades financieras que ofrezcan cuentas a la vista | `Sujeto_entidad_financiera` | ✘ `rechazado_aplanamiento` | laudo (a): el candidato es la clase madre del colectivo; por la regla de herencia 2 el grafo afirmaría la norma sobre toda la clase y, por la regla 1, sobre cada subclase — falsedad en campo estructu… |
| 56 |  |  | Empresas no financieras operadoras de cajeros automáticos | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 57 | snp_debin | `Sujeto_rol_alcance_snp_debin` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 58 |  |  | PSPCP | `Sujeto_pspcp` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 59 | snp_psp | `Sujeto_rol_alcance_snp_psp` | Proveedores de servicios de pago (PSP) | `Sujeto_proveedor_de_servicios_de_pago` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 60 |  |  | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 61 | snp_spd | `Sujeto_rol_alcance_snp_spd` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 62 |  |  | PSP (según el servicio) | `Sujeto_proveedor_de_servicios_de_pago` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 63 | snp_tr_nc | `Sujeto_rol_alcance_snp_tr_nc` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 64 |  |  | Proveedores de servicios de pago (PSP) | `Sujeto_proveedor_de_servicios_de_pago` | ✔ `aceptado_recorte_declarado` | el núcleo del colectivo coincide con el del id; la aclaración que el colectivo trae no recorta el sujeto (sección, ley que lo define, o base de observancia), verificada contra el pasaje |
| 65 | supcon | `Sujeto_rol_alcance_supcon` | Entidades financieras | `Sujeto_entidad_financiera` | ✔ `aceptado_identico` | el colectivo y el label del id coinciden |
| 66 |  |  | Empresas del perímetro de supervisión consolidada | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 67 | traval | `Sujeto_rol_alcance_traval` | Transportadoras de valores (TV) | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 68 |  |  | Prestadoras de Servicios de Transporte de Valores (PSTV) | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |
| 69 |  |  | Transportadoras de Valores Propias (TVP) | — | ✘ `sin_id_en_catalogo` | el colectivo que el pasaje nombra no tiene id en el catálogo v3; el matcheo no sube al padre porque eso sería colapsar a la madre |

## Los 30 roles y sus miembros

| TO | rol_id | miembros | cita |
|---|---|---|---|
| adrei | `Sujeto_rol_alcance_adrei` | **— sin miembro adjudicable** (`aplanamiento_rechazado`) | `adrei::1.1` |
| autenf | `Sujeto_rol_alcance_autenf` | **— sin miembro adjudicable** (`sin_id_en_catalogo`) | `autenf::1.1::intro` |
| ccbcra | `Sujeto_rol_alcance_ccbcra` | `Sujeto_caja_de_credito`<br>`Sujeto_entidad_cambiaria`<br>`Sujeto_entidad_financiera` | `ccbcra::1.1` |
| convca | `Sujeto_rol_alcance_convca` | `Sujeto_entidad_financiera` | `convca::1.1` |
| cryl | `Sujeto_rol_alcance_cryl` | `Sujeto_camara_electronica_de_compensacion`<br>`Sujeto_entidad_financiera`<br>`Sujeto_fondo_comun_de_inversion` | `cryl::3.1` |
| ctacor | `Sujeto_rol_alcance_ctacor` | `Sujeto_casa_de_cambio` | `ctacor::1.1` |
| depaho | `Sujeto_rol_alcance_depaho` | `Sujeto_caja_de_credito`<br>`Sujeto_compania_financiera` | `depaho::1.1.1` |
| efemin | `Sujeto_rol_alcance_efemin` | `Sujeto_entidad_financiera` | `efemin::4.1` |
| fabcra | `Sujeto_rol_alcance_fabcra` | `Sujeto_camara_electronica_de_compensacion`<br>`Sujeto_compania_financiera`<br>`Sujeto_entidad_cambiaria`<br>`Sujeto_entidad_financiera` | `fabcra::S1::chapeau_seccion` |
| icmecma | `Sujeto_rol_alcance_icmecma` | `Sujeto_empresa_no_financiera_emisora_de_tarjetas`<br>`Sujeto_entidad_financiera`<br>`Sujeto_fiduciario_de_fideicomiso_financiero` | `icmecma::1.1.1` |
| lavdin | `Sujeto_rol_alcance_lavdin` | `Sujeto_entidad_cambiaria`<br>`Sujeto_entidad_financiera` | `lavdin::1.1::intro` |
| ordcom | `Sujeto_rol_alcance_ordcom` | **— sin miembro adjudicable** (`instancia_rechazada`) | `ordcom::1.5::intro` |
| osapsa | `Sujeto_rol_alcance_osapsa` | `Sujeto_entidad_financiera` | `osapsa::1.1` |
| pagjub | `Sujeto_rol_alcance_pagjub` | **— sin miembro adjudicable** (`aplanamiento_rechazado`) | `pagjub::1.1` |
| pfmipyme | `Sujeto_rol_alcance_pfmipyme` | **— sin miembro adjudicable** (`sin_id_en_catalogo`) | `pfmipyme::1.1.1` |
| pimf | `Sujeto_rol_alcance_pimf` | **— sin miembro adjudicable** (`sin_id_en_catalogo`) | `pimf::5.1` |
| ratiofn | `Sujeto_rol_alcance_ratiofn` | **— sin miembro adjudicable** (`aplanamiento_rechazado`) | `ratiofn::1.1` |
| rdbcra | `Sujeto_rol_alcance_rdbcra` | **— sin miembro adjudicable** (`aplanamiento_rechazado`) | `rdbcra::1.1.1.1` |
| repefe | `Sujeto_rol_alcance_repefe` | **— sin miembro adjudicable** (`sin_id_en_catalogo`) | `repefe::1.1` |
| retype | `Sujeto_rol_alcance_retype` | **— sin miembro adjudicable** (`sin_id_en_catalogo`) | `retype::1.1.2` |
| rmrtsd | `Sujeto_rol_alcance_rmrtsd` | `Sujeto_entidad_financiera`<br>`Sujeto_proveedor_de_servicios_de_pago` | `rmrtsd::1.1.1` |
| rrci | `Sujeto_rol_alcance_rrci` | `Sujeto_entidad_financiera` | `rrci::1.2` |
| servco | `Sujeto_rol_alcance_servco` | `Sujeto_entidad_financiera` | `servco::1.1` |
| snp_atm | `Sujeto_rol_alcance_snp_atm` | **— sin miembro adjudicable** (`aplanamiento_rechazado`) | `snp_atm::1.1.1` |
| snp_debin | `Sujeto_rol_alcance_snp_debin` | `Sujeto_entidad_financiera`<br>`Sujeto_pspcp` | `snp_debin::2.1` |
| snp_psp | `Sujeto_rol_alcance_snp_psp` | `Sujeto_entidad_financiera`<br>`Sujeto_proveedor_de_servicios_de_pago` | `snp_psp::1.1.2` |
| snp_spd | `Sujeto_rol_alcance_snp_spd` | `Sujeto_entidad_financiera`<br>`Sujeto_proveedor_de_servicios_de_pago` | `snp_spd::S1::chapeau_seccion` |
| snp_tr_nc | `Sujeto_rol_alcance_snp_tr_nc` | `Sujeto_entidad_financiera`<br>`Sujeto_proveedor_de_servicios_de_pago` | `snp_tr_nc::1.2.1` |
| supcon | `Sujeto_rol_alcance_supcon` | `Sujeto_entidad_financiera` | `supcon::2.2::intro` |
| traval | `Sujeto_rol_alcance_traval` | **— sin miembro adjudicable** (`sin_id_en_catalogo`) | `traval::1.1::intro` |

## Lista declarada de excepciones de S15

Doce roles, tres deudas distintas con tres remedios distintos. No se agrupan: una lista sin causa dice cuántos faltan, no qué hacer para achicarla.

### `sin_id_en_catalogo` — 6 roles

**Remedio:** abrir id en el catálogo, que es re-sello del prefijo v3 y unidad propia

| TO | rol_id | colectivo(s) que el pasaje nombra |
|---|---|---|
| autenf | `Sujeto_rol_alcance_autenf` | Personas que ejercen cargos de administración, fiscalización o gerencia en entidades fina… |
| pfmipyme | `Sujeto_rol_alcance_pfmipyme` | Plataformas para el financiamiento MiPyME (PFM) |
| pimf | `Sujeto_rol_alcance_pimf` | Infraestructuras del mercado financiero (IMF) nominadas en la Sección 5 |
| repefe | `Sujeto_rol_alcance_repefe` | Representantes de entidades financieras del exterior no autorizadas |
| retype | `Sujeto_rol_alcance_retype` | Banco de la Nación Argentina<br>Otros bancos públicos participantes (IAF) |
| traval | `Sujeto_rol_alcance_traval` | Transportadoras de valores (TV)<br>Prestadoras de Servicios de Transporte de Valores (PSTV)<br>Transportadoras de Valores Propias (TVP) |

### `aplanamiento_rechazado` — 5 roles

**Remedio:** una clase más específica en el catálogo

| TO | rol_id | colectivo(s) que el pasaje nombra |
|---|---|---|
| adrei | `Sujeto_rol_alcance_adrei` | Entidades financieras de importancia sistémica local (D-SIB) |
| pagjub | `Sujeto_rol_alcance_pagjub` | Entidades financieras participantes del pago de beneficios ANSES |
| ratiofn | `Sujeto_rol_alcance_ratiofn` | Entidades financieras D-SIB<br>Sucursales o subsidiarias de bancos del exterior G-SIB |
| rdbcra | `Sujeto_rol_alcance_rdbcra` | Personas jurídicas y humanas sometidas al ámbito de la Ley de Entidades Financieras |
| snp_atm | `Sujeto_rol_alcance_snp_atm` | Entidades financieras que ofrezcan cuentas a la vista<br>Empresas no financieras operadoras de cajeros automáticos |

### `instancia_rechazada` — 1 roles

**Remedio:** cambiar la firma de miembro_de, que es laudo de la autora sobre el esquema congelado

| TO | rol_id | colectivo(s) que el pasaje nombra |
|---|---|---|
| ordcom | `Sujeto_rol_alcance_ordcom` | BCRA (emisor)<br>Destinatarios de Comunicaciones (entidades financieras, cajas de crédito cooperativas, et… |

