# Registro de alcance por tanda (lectura humana)

Registro que solo agrega, previsto por la enmienda 4 al protocolo entre tandas (§4; BORRADOR) y por R1 de U-RERESOL-CAT
(`data/experiment/reresolucion_catalogo/freno_r1.md`, §4). Una fila por documento y por tanda; las entradas de clase no van a
`catalogo_sujetos_r2.json` (candados). R2-2 de U-RERESOL-CAT define el formato legible por código y lo carga desde acá, sin
cambiar las decisiones. Regla del paso de lectura: solo clases que ya existen, nombradas de forma exacta por el pasaje (una o
dos); el título vale como pasaje cuando el cuerpo no tiene frase de alcance y nombra exactamente una clase (enmienda 4, §2,
punto 7); una sección de un régimen informativo cuyo rol existe reutiliza ese rol (§2, punto 8, acotado: no decide ESQ-RI-3).
Fichas con los pasajes completos: paquete de la mesa `hoja_de_ruta_tanda1_mesa/fichas_alcance_12_documentos_tanda1_mesa.md`
(06/10/2026). Catálogo: `catalogo_sujetos_r2.json` (115 entradas; 80 clases e instancias, 35 roles).

## Tanda 1 — decisiones de la autora del 06/10/2026 (los 12 documentos del ejemplo del §7 del protocolo sin alcance)

| TO | título (inventario) | decisión | id(s) del catálogo | base | pasaje (chunk de la partición legada, página) |
|---|---|---|---|---|---|
| ri_ccna | RI para Cajas de Crédito - Normas de Auditoría | clase | `Sujeto_caja_de_credito` | pasaje | `ri_ccna::S1`, pp. 2-3: «Las Cajas de Crédito deberán informar al Banco Central…» |
| ri_cc | RI para Cajas de Crédito - contable | clase | `Sujeto_caja_de_credito` | título (regla §2.7) | cuerpo sin frase de alcance (`ri_cc::1.1`, p. 49; `ri_cc::S1`, p. 71); el título nombra una sola clase |
| ri_rml | RI Cont. Mensual - Efectivo mínimo y aplicación de recursos | rol reutilizado | `Sujeto_rol_entidad_comprendida_reginf` | sección del mismo régimen (§2.8) | `ri_rml::1.1`, p. 2: «…entidades comprendidas en el Grupo “A”… o las restantes entidades» |
| ri_gerc | RI Cont. Mensual - Grandes exposiciones al riesgo de crédito | rol reutilizado | `Sujeto_rol_entidad_comprendida_reginf` | sección del mismo régimen (§2.8) | `ri_gerc::2.3` y `::2.4::intro`, p. 4 |
| ri_oc | RI Cont. Mensual - Operaciones de Cambio | sin alcance declarado | — | los informantes (entidades autorizadas a operar en cambios, incluidas casas y agencias) no son los del régimen general | `ri_oc::S0`, pp. 1-2; `::3.3`, p. 6 |
| ri_dcpc | RI - Disposiciones complementarias al plan de cuentas | clase | `Sujeto_entidad_financiera` | pasaje | `ri_dcpc::S1`, pp. 3-4: «El presente marco contable… para las entidades financieras» |
| snp_cheq | Sistema Nacional de Pagos - Cheques y otros instrumentos compensables | clase (dos) | `Sujeto_entidad_financiera`, `Sujeto_camara_electronica_de_compensacion` | pasaje | `snp_cheq::2.4`, p. 11 (ámbito); `::2.2.2.3`, pp. 6-7 (participantes) |
| ceninf | Centrales de información | sin alcance declarado | — | el pasaje nombra seis sujetos, uno sin clase (rol nuevo en la release) | `ceninf::1.1::intro`, p. 3 |
| cirmo3 | Circulación monetaria | sin alcance declarado | — | el pasaje nombra tres clases y un rol de otro documento, variables por sección (rol nuevo en la release) | `cirmo3::4.1::intro`, p. 30; `::1.3.1`, pp. 24-29 |
| snp_tr | Sistema Nacional de Pagos - Transferencias | rol reutilizado | `Sujeto_rol_alcance_snp_tr_nc` | remisión del propio texto a las normas complementarias | `snp_tr::S1::chapeau_seccion`, p. 3; `::1.1.3`, p. 5 |
| manori | Manuales de originación y administración de préstamos | clase | `Sujeto_entidad_financiera` | pasaje | `manori::S1::chapeau_seccion`, p. 3: «…que las entidades financieras pueden seguir…» |
| nmcief | Normas mínimas sobre controles internos para entidades financieras | clase (dos) | `Sujeto_entidad_financiera`, `Sujeto_sujeto_del_perimetro_consolidado` | pasaje | `nmcief::S0`, p. 2: «…también deberán observarse en las filiales y subsidiarias que consolidan…» |

Resumen: 6 clase, 3 rol reutilizado, 3 sin alcance declarado. Con los 8 del ejemplo que ya tenían alcance, los 20 del ejemplo
quedan cubiertos para el pre-registro de la tanda 1 (la lista real sale de la segmentación oficial).

## Candidatos a la regla del título en el resto del universo (no decididos; lectura del cuerpo pendiente)

Recómputo del 06/10/2026 sobre `escalado_prep/inventario_tos.csv` contra los labels y alias del catálogo (singular y plural):
86 de los 152 TOs no tienen alcance; en 25 de ellos el título nombra exactamente una clase (3 son ri_ccna, ri_cc y nmcief, ya
decididos) y en 5 nombra dos («casas y agencias de cambio»: ri2_ae, reqcac, ri2_cs, ri2_pm, ri_itme), que la regla del título no
cubre. Los 22 restantes son candidatos para la lectura de su tanda: la regla exige además que el cuerpo no tenga frase de
alcance, y conviene exigir que la clase nombrada sea el sujeto obligado o informante, no el objeto del régimen.

| TO | clase que nombra el título | ¿la clase es el sujeto obligado o informante? (lectura del título) |
|---|---|---|
| inspag, cateloc, horari, seguef, nmaeef, ri_ii_31_12_19, ri_mmsef, ri_sef | `Sujeto_entidad_financiera` | sí |
| ri_ccpnp | `Sujeto_caja_de_credito` | sí |
| ri_pspapt, ri_pspii (no segmentable), ri_psprca, ri_psp | `Sujeto_proveedor_de_servicios_de_pago` | sí |
| opecam | `Sujeto_entidad_cambiaria` | sí |
| regpri | `Sujeto_banco` | dudoso: bancos provinciales y municipales en privatización |
| ri_icpipsp, ri_iepsp | `Sujeto_proveedor_de_servicios_de_pago`, `Sujeto_proveedor_no_financiero_de_credito` | dudoso: informes de contadores sobre el cumplimiento de esos sujetos |
| fimipyme, ri_fcem (no segmentable), ri_pfmipyme (no segmentable) | `Sujeto_mipyme` | no: la MiPyME es destinataria; obligan a las entidades o a las plataformas |
| ri_dsf, ri_esd | `Sujeto_deudor` | no: el deudor es el objeto informado; informan las entidades financieras |
