# Control de continuidad de la numeración: antes y después de las reglas de S0-5a

Generado por `s0_5/scripts/lista_continuidad_S0-5a.py` desde las dos salidas de `control_continuidad_numeracion.py` (sobre S0-4b y sobre S0-5a, con los renglones de `extraer_lineas`).

- **Antes:** {"saltos": 104, "por_clase": {"i": 15, "ii": 89}, "ii_posible_referencia": 9, "tos_con_saltos": 15, "por_modo": {"vigente": 25, "sin_raiz": 79}, "tanda1": {"saltos": 21, "tos": 6, "por_clase": {"i": 4, "ii": 17}}}
- **Después:** {"saltos": 98, "por_clase": {"i": 15, "ii": 83}, "ii_posible_referencia": 9, "tos_con_saltos": 13, "por_modo": {"vigente": 19, "sin_raiz": 79}, "tanda1": {"saltos": 15, "tos": 4, "por_clase": {"i": 4, "ii": 11}}}
- **Por TO, después:** {"cirmo3": {"i": 2}, "ctacte": {"ii": 1}, "expaef": {"i": 1}, "nmaeef": {"ii": 6}, "pimf": {"i": 7}, "ri2_ae": {"ii": 11}, "ri_cc": {"ii": 3}, "ri_ccna": {"ii": 11}, "ri_dsf": {"ii": 42}, "ri_laft": {"ii": 6}, "ri_ot": {"i": 3}, "snp_cheq": {"i": 1}, "snp_dd": {"i": 1, "ii": 3}}

## Saltos que las reglas cierran

- `ri_rml` 1.2.4 (ii, cola), antes en `ri_rml::1.3`, con 0 descendientes tragados
- `snp_tr` 1.3.4 (ii, cola), antes en `snp_tr::1.6::intro`, con 2 descendientes tragados
- `snp_tr` 1.3.5 (ii, cola), antes en `snp_tr::1.6::intro`, con 3 descendientes tragados
- `snp_tr` 1.3.6 (ii, cola), antes en `snp_tr::1.6::intro`, con 2 descendientes tragados
- `snp_tr` 1.4 (ii, hueco), antes en `snp_tr::1.6::intro`, con 4 descendientes tragados
- `snp_tr` 1.5 (ii, hueco), antes en `snp_tr::1.6::intro`, con 4 descendientes tragados

Saltos nuevos después de las reglas: 0.
Saltos que siguen y cambian de unidad: 4.
- `ri2_ae` 3.1: de `ri2_ae::14.3::parte3` a `ri2_ae::14.3`
- `ri2_ae` 3.4: de `ri2_ae::14.3::parte3` a `ri2_ae::14.3`
- `ri2_ae` 3.5: de `ri2_ae::14.3::parte3` a `ri2_ae::S14::cierre`
- `ri2_ae` 5.2: de `ri2_ae::3.3` a `ri2_ae::S3::cierre`

## Lista para la autora (después de las reglas)

84 saltos: {"ii": 83, "i": 1}.

### tanda 1: regla por lista en S0-5: 12 ({"ri_ccna": 11, "snp_cheq": 1})

| TO | subdoc. | rótulo | clase | forma | en la unidad | renglón | fin del anterior | posible ref. | descendientes tragados |
|---|---|---|---|---|---|---|---|---|---|
| ri_ccna | D1A1 | 2.1.1 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.1.no sean socios o administradores de la Caja de Crédito» | «los Contadores Públicos Nacionales que:» | sí |  |
| ri_ccna | D1A1 | 2.1.2 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.2.no se desempeñen en relación de dependencia en la Caja» | «presas económicamente vinculadas a ella,» | sí |  |
| ri_ccna | D1A1 | 2.1.3 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.3.no se encuentren alcanzados por alguna de las inhabili» | «presas económicamente vinculadas a ella,» | sí |  |
| ri_ccna | D1A1 | 2.1.4 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.4.no hayan sido expresamente excluidos del "Registro de » | «. 10 de la Ley 21.526 para los síndicos,» | sí |  |
| ri_ccna | D1A1 | 2.1.5 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.5.no hayan sido expresamente inhabilitados para ejercer » | «de las disposiciones vigentes,» | sí |  |
| ri_ccna | D1A1 | 2.1.6 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.6.tengan la independencia requerida por las normas de au» | «ionales de Ciencias Económicas del país,» | sí |  |
| ri_ccna | D1A1 | 2.1.7 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.7.tengan una antigüedad en la matricula igual o mayor a » | «as por las Cajas de crédito que auditen,» | sí |  |
| ri_ccna | D1A1 | 2.1.8 | ii | hueco | `ri_ccna::D1A1::2.1::intro` | «2.1.8. cuenten con una experiencia de dos (2) años o más en » | «tricula igual o mayor a tres (3) años, y» | sí |  |
| ri_ccna | D1A1 | 5.1 | ii | hueco | `ri_ccna::D1A1::S5::chapeau_seccion` | «5.1.Designación.» | «» |  |  |
| ri_ccna | D1A1 | 8.1 | ii | hueco | `ri_ccna::D1A1::S8::chapeau_seccion` | «8.1.Informes.» | «la actividad de la entidad auditada.» |  |  |
| ri_ccna | D1A2 | 5.1 | ii | hueco | `ri_ccna::D1A2::S5::chapeau_seccion` | «5.1.Perfil de la Caja de crédito y su negocio.» | «siguientes aspectos fundamentales:» |  |  |
| snp_cheq |  | 3.3.6 | i | hueco | `` | «» | «» |  | 3.3.6.2 en `snp_cheq::3.3.5.1` |

### fuera de la tanda 1: límite declarado y grupo 2: 71 ({"nmaeef": 6, "ri2_ae": 11, "ri_cc": 3, "ri_dsf": 42, "ri_laft": 6, "snp_dd": 3})

| TO | subdoc. | rótulo | clase | forma | en la unidad | renglón | fin del anterior | posible ref. | descendientes tragados |
|---|---|---|---|---|---|---|---|---|---|
| nmaeef |  | 4.4 | ii | cola | `nmaeef::21.3::parte1` | «4.4 Verificación de la información sobre empresas o entidade» | «bre los estados financieros consolidados» |  | 4.4.1 en `nmaeef::21.3::parte5`, 4.4.2 en `nmaeef::21.3::parte5` |
| nmaeef |  | 4.5 | ii | cola | `nmaeef::21.3::parte1` | «4.5. Sobre la capitalización de pasivos.» | «ón sobre empresas o entidades vinculadas» |  | 4.5.1 en `nmaeef::21.3::parte6`, 4.5.2 en `nmaeef::21.3::parte6` |
| nmaeef |  | 4.6 | ii | cola | `nmaeef::21.3::parte1` | «4.6 Sobre los requisitos establecidos en el TO sobre Financi» | «4.5. Sobre la capitalización de pasivos.» |  | 4.6.1 en `nmaeef::21.3::parte6`, 4.6.2 en `nmaeef::21.3::parte6` |
| nmaeef |  | 4.7 | ii | cola | `nmaeef::21.3::parte1` | «4.7 Sobre la Aplicación de fondos a las financiaciones compr» | «por ellos.» |  | 4.7.1 en `nmaeef::21.3::parte6`, 4.7.2 en `nmaeef::21.3::parte6` |
| nmaeef |  | 4.8 | ii | cola | `nmaeef::21.3::parte1` | «4.8. Sobre el otorgamiento de financiaciones en el marco del» | «peratoria de Swaps OCT-MAE – Licitación)» |  | 4.8.1 en `nmaeef::21.3::parte6`, 4.8.2 en `nmaeef::21.3::parte6` |
| nmaeef |  | 4.9 | ii | cola | `nmaeef::21.3::parte1` | «4.9 Cualquier otro informe que el Banco Central de la Repúbl» | «ordenado de Efectivo Mínimo.» |  |  |
| ri2_ae |  | 2.3 | ii | cola | `ri2_ae::S9::parte2` | «2.3. Identificación de las áreas de riesgo y materialidad.» | «auditoría y supervisar su trabajo.» |  |  |
| ri2_ae |  | 2.4 | ii | cola | `ri2_ae::S9::parte2` | «2.4. Evaluación del riesgo de fraude (incluye el cohecho tra» | «de capitales mínimos.» |  |  |
| ri2_ae |  | 2.5 | ii | cola | `ri2_ae::S9::parte2` | «2.5. Identificación y evaluación de riesgos específicos.» | «na geográfica de su ámbito de actuación.» |  |  |
| ri2_ae |  | 2.6 | ii | cola | `ri2_ae::S9::parte3` | «2.6. Plan de auditoría.» | «» |  |  |
| ri2_ae |  | 2.7 | ii | cola | `ri2_ae::S9::parte3` | «2.7. Auditorías Iniciales» | «e los controles que realiza la entidad).» |  |  |
| ri2_ae |  | 2.8 | ii | cola | `ri2_ae::S9::parte3` | «2.8. Emisión de informes» | «de la República Argentina.» |  |  |
| ri2_ae |  | 3.1 | ii | hueco | `ri2_ae::14.3` | «3.1. El objetivo de este informe es que el auditor, sobre la» | «cambio» |  |  |
| ri2_ae |  | 3.4 | ii | cola | `ri2_ae::14.3` | «3.4. El Directorio o autoridad equivalente, según el caso, s» | « de publicación al cierre del ejercicio.» |  |  |
| ri2_ae |  | 3.5 | ii | cola | `ri2_ae::S14::cierre` | «3.5. Si el auditor externo no hubiera observado deficiencias» | «comendaciones efectuadas.» |  |  |
| ri2_ae |  | 5.1 | ii | hueco | `ri2_ae::3.3` | «5.1. Inscripción.» | «iaciones de Profesionales Universitarios» |  |  |
| ri2_ae |  | 5.2 | ii | hueco | `ri2_ae::S3::cierre` | «5.2. Exclusión.» | «festando tal circunstancia.» |  | 5.2.1 en `ri2_ae::S3::cierre`, 5.2.2 en `ri2_ae::S3::cierre` |
| ri_cc | R4 | 1.2.3 | ii | cola | `ri_cc::R4::1.2.2` | «1.2.3.Conceptos comprendidos» | «del período de cómputo bajo informe.» |  |  |
| ri_cc | R4 | 1.8.1 | ii | hueco | `ri_cc::R4::1.7` | «1.8.1. Exigencia» | «consignará la integración total del mes.» |  |  |
| ri_cc | R5 | 2.8 | ii | hueco | `ri_cc::R5::2.7` | «2.8.Código 11» | «peración se les incorporará el dígito O.» |  |  |
| ri_dsf |  | 2.3 | ii | cola | `ri_dsf::S8::chapeau_seccion` | «2.3. Responsabilidades eventuales:» | «otorgadas, individualmente consideradas.» |  | 2.3.1 en `ri_dsf::S8::chapeau_seccion`, 2.3.1.1 en `ri_dsf::S8::chapeau_seccion`, 2.3.1.2 en `ri_dsf::S8::chapeau_seccion`, 2.3.1.3 en `ri_dsf::S8::chapeau_seccion`, 2.3.2 en `ri_dsf::S8::chapeau_seccion`, 2.3.2.1 en `ri_dsf::S8::chapeau_seccion`, 2.3.2.2 en `ri_dsf::S8::chapeau_seccion`, 2.3.2.3 en `ri_dsf::S8::chapeau_seccion` |
| ri_dsf |  | 2.4 | ii | cola | `ri_dsf::S10::parte2` | «2.4. Hipotecarios sobre la vivienda» | «os a sola firma, descontados y comprados» |  |  |
| ri_dsf |  | 2.5 | ii | cola | `ri_dsf::S10::parte2` | «2.5. Con otras garantías hipotecarias» | «2.4. Hipotecarios sobre la vivienda» |  |  |
| ri_dsf |  | 2.6 | ii | cola | `ri_dsf::S10::parte2` | «2.6. Prendarios sobre automotores» | «2.5. Con otras garantías hipotecarias» |  |  |
| ri_dsf |  | 2.7 | ii | cola | `ri_dsf::S10::parte2` | «2.7. Con otras garantías prendarias» | «2.6. Prendarios sobre automotores» |  |  |
| ri_dsf |  | 2.8 | ii | cola | `ri_dsf::S10::parte2` | «2.8. Personales» | «2.7. Con otras garantías prendarias» |  |  |
| ri_dsf |  | 2.9 | ii | cola | `ri_dsf::S10::parte2` | «2.9. Personales de monto reducido» | «2.8. Personales» |  |  |
| ri_dsf |  | 2.10 | ii | cola | `ri_dsf::S10::parte2` | «2.10. Tarjetas de crédito» | «2.9. Personales de monto reducido» |  |  |
| ri_dsf |  | 2.11 | ii | cola | `ri_dsf::S10::parte2` | «2.11. Otros préstamos» | «2.10. Tarjetas de crédito» |  |  |
| ri_dsf |  | 2.12 | ii | cola | `ri_dsf::S10::parte2` | «2.12. Créditos Adicionales» | «2.11. Otros préstamos» |  |  |
| ri_dsf |  | 2.13 | ii | cola | `ri_dsf::S10::parte2` | «2.13. Préstamos a Instituciones de Microcrédito» | «2.12. Créditos Adicionales» |  |  |
| ri_dsf |  | 2.14 | ii | cola | `ri_dsf::S10::parte2` | «2.14. Préstamos a Microemprendedores» | «réstamos a Instituciones de Microcrédito» |  |  |
| ri_dsf |  | 2.15 | ii | cola | `ri_dsf::S10::parte2` | «2.15. Créditos por arrendamientos financieros» | «2.14. Préstamos a Microemprendedores» |  |  |
| ri_dsf |  | 2.16 | ii | cola | `ri_dsf::S10::parte2` | «2.16. Préstamos para prefinanciación y financiación de expor» | « Créditos por arrendamientos financieros» |  |  |
| ri_dsf |  | 2.17 | ii | cola | `ri_dsf::S10::parte2` | «2.17. Hipotecarios sobre la vivienda de Unidades de Valor Ad» | «nciación y financiación de exportaciones» |  |  |
| ri_dsf |  | 2.18 | ii | cola | `ri_dsf::S10::parte2` | «2.18. Con otras garantías hipotecarias de Unidades de Valor » | «ivienda de Unidades de Valor Adquisitivo» |  |  |
| ri_dsf |  | 2.19 | ii | cola | `ri_dsf::S10::parte2` | «2.19. Prendarios sobre automotores de Unidades de Valor Adqu» | «ecarias de Unidades de Valor Adquisitivo» |  |  |
| ri_dsf |  | 2.20 | ii | cola | `ri_dsf::S10::parte2` | «2.20. Con otras garantías prendarias sobre automotores de Un» | «motores de Unidades de Valor Adquisitivo» |  |  |
| ri_dsf |  | 2.21 | ii | cola | `ri_dsf::S10::parte2` | «2.21. Otros préstamos de Unidades de Valor Adquisitivo» | «motores de Unidades de Valor Adquisitivo» |  |  |
| ri_dsf |  | 2.22 | ii | cola | `ri_dsf::S10::parte2` | «2.22. Documentos a sola firma de Unidades de Valor Adquisiti» | «éstamos de Unidades de Valor Adquisitivo» |  |  |
| ri_dsf |  | 2.23 | ii | cola | `ri_dsf::S10::parte2` | «2.23. Hipotecarios sobre la vivienda de Unidades de Vivienda» | «a firma de Unidades de Valor Adquisitivo» |  |  |
| ri_dsf |  | 2.24 | ii | cola | `ri_dsf::S10::parte2` | «2.24. Personales de Unidades de Valor Adquisitivo» | «obre la vivienda de Unidades de Vivienda» |  |  |
| ri_dsf |  | 2.25 | ii | cola | `ri_dsf::S10::parte2` | «2.25. Cuentas por cobrar por arrendamientos financieros de U» | «sonales de Unidades de Valor Adquisitivo» |  |  |
| ri_dsf |  | 3.4 | ii | cola | `ri_dsf::S10::parte2` | «3.4. Fecha de origen» | «odificación de Currency Codes del SWIFT.» |  |  |
| ri_dsf |  | 3.5 | ii | cola | `ri_dsf::S10::parte2` | «3.5. Monto original» | «3.4. Fecha de origen» |  |  |
| ri_dsf |  | 3.6 | ii | cola | `ri_dsf::S10::parte2` | «3.6. Saldo de deuda» | «al a la fecha de origen de la operación.» |  | 3.6.1 en `ri_dsf::S10::parte2`, 3.6.1.1 en `ri_dsf::S10::parte2`, 3.6.2 en `ri_dsf::S10::parte2`, 3.6.2.1 en `ri_dsf::S10::parte2`, 3.6.2.2 en `ri_dsf::S10::parte2`, 3.6.3 en `ri_dsf::S10::parte2`, 3.6.3.1 en `ri_dsf::S10::parte2`, 3.6.3.2 en `ri_dsf::S10::parte2` |
| ri_dsf |  | 3.7 | ii | cola | `ri_dsf::S10::parte2` | «3.7. Plazo original» | «informarse el monto de deuda vencida.» |  |  |
| ri_dsf |  | 3.8 | ii | cola | `ri_dsf::S10::parte2` | «3.8. Tipo de tasa de interés» | «informadas.» |  | 3.8.1 en `ri_dsf::S10::parte2`, 3.8.2 en `ri_dsf::S10::parte2`, 3.8.3 en `ri_dsf::S10::parte2` |
| ri_dsf |  | 3.9 | ii | cola | `ri_dsf::S10::parte2` | «3.9. Tasa de interés nominal anual contractual» | «3. Deudores del Sistema Financiero.» |  |  |
| ri_dsf |  | 3.10 | ii | cola | `ri_dsf::S10::parte2` | «3.10. Fecha de último repacto de tasa de interés» | «al pactada en el formulario de préstamo.» |  |  |
| ri_dsf |  | 3.11 | ii | cola | `ri_dsf::S10::parte2` | «3.11. Frecuencia de actualización de la tasa» | «del último ajuste de la tasa de interés.» |  |  |
| ri_dsf |  | 3.12 | ii | cola | `ri_dsf::S10::parte2` | «3.12. Tasa de interés nominal anual vigente a la fecha a la » | «Se informará en meses.» |  |  |
| ri_dsf |  | 3.13 | ii | cola | `ri_dsf::S10::parte2` | «3.13. Costo financiero total vigente a la fecha a la que se » | «ones correspondientes a una misma marca.» |  |  |
| ri_dsf |  | 3.14 | ii | cola | `ri_dsf::S10::parte2` | «3.14. Sistema de amortización» | «crédito”.» |  | 3.14.1 en `ri_dsf::S10::parte2`, 3.14.2 en `ri_dsf::S10::parte2`, 3.14.3 en `ri_dsf::S10::parte2`, 3.14.4 en `ri_dsf::S10::parte2` |
| ri_dsf |  | 3.15 | ii | cola | `ri_dsf::S10::parte2` | «3.15. Frecuencia de amortización» | «3.14.4. Otros» |  | 3.15.1 en `ri_dsf::S10::parte2`, 3.15.2 en `ri_dsf::S10::parte2`, 3.15.3 en `ri_dsf::S10::parte2`, 3.15.4 en `ri_dsf::S10::parte2`, 3.15.5 en `ri_dsf::S10::parte2` |
| ri_dsf |  | 3.16 | ii | cola | `ri_dsf::S10::parte2` | «3.16. Monto original aplicado a cada uno de los siguientes d» | «3.15.5. Otros» |  | 3.16.1 en `ri_dsf::S10::parte2`, 3.16.2 en `ri_dsf::S10::parte2`, 3.16.3 en `ri_dsf::S10::parte2`, 3.16.3.1 en `ri_dsf::S10::parte2`, 3.16.3.2 en `ri_dsf::S10::parte2`, 3.16.3.3 en `ri_dsf::S10::parte2`, 3.16.3.4 en `ri_dsf::S10::parte2`, 3.16.4 en `ri_dsf::S10::parte2` |
| ri_dsf |  | 3.17 | ii | cola | `ri_dsf::S10::parte2` | «3.17. Se deberá detallar la apertura de las cuatro principal» | «3.16.4. Otros destinos» |  |  |
| ri_dsf |  | 3.18 | ii | cola | `ri_dsf::S10::parte2` | «3.18. Fecha primer vencimiento impago» | «cuales se aplique el monto original.» |  |  |
| ri_dsf |  | 3.19 | ii | cola | `ri_dsf::S10::parte2` | «3.19. Fecha de interrupción del devengamiento» | «3.18. Fecha primer vencimiento impago» |  |  |
| ri_dsf |  | 3.20 | ii | cola | `ri_dsf::S10::parte2` | «3.20. Se deberá indicar si la operación se encuentra alcanza» | «3.Deudores del Sistema Financiero.» |  |  |
| ri_dsf |  | 3.21 | ii | cola | `ri_dsf::S10::parte2` | «3.21. Se deberá identificar si la financiación es otorgada e» | «ue impliquen un tratamiento diferencial.» |  |  |
| ri_dsf |  | 3.22 | ii | cola | `ri_dsf::S10::parte2` | «3.22. Se informará para cada una de las operaciones garantiz» | «ión de micro, pequeña o mediana empresa.» |  |  |
| ri_laft |  | 3.1 | ii | hueco | `ri_laft::1.5` | «3.1. Importe» | «dando precisiones sobre el particular.» |  |  |
| ri_laft |  | 3.2 | ii | hueco | `ri_laft::1.5` | «3.2. Tipo de persona» | «dos a la UIF.» |  |  |
| ri_laft |  | 3.3 | ii | hueco | `ri_laft::1.5` | «3.3. Condición de PEP» | «[FIN TABLA ri_laft::tabla001]» |  |  |
| ri_laft |  | 3.4 | ii | hueco | `ri_laft::1.5` | «3.4. Actividad» | «en caso de que lo sea.» |  |  |
| ri_laft |  | 3.5 | ii | hueco | `ri_laft::1.5` | «3.5. Producto donde se registró la inusualidad» | «Anexo I.» |  |  |
| ri_laft |  | 3.6 | ii | hueco | `ri_laft::1.5` | «3.6. Región Geográfica» | «[FIN TABLA ri_laft::tabla002]» |  |  |
| snp_dd |  | 7.4 | ii | hueco | `snp_dd::7.3` | «7.4.Registro adicional de órdenes de Débito (opcional).» | «án ser siempre informados en mayúsculas.» |  |  |
| snp_dd |  | 7.5 | ii | hueco | `snp_dd::7.3` | «7.5.Registro adicional de Reversiones.» | «án ser siempre informados en mayúsculas.» |  |  |
| snp_dd |  | 7.12 | ii | cola | `snp_dd::7.11` | «7.12.Información a incluir en el extracto bancario.» | «án ser siempre informados en mayúsculas.» |  |  |

### tanda 0 (fuera de S0-5): 1 ({"ctacte": 1})

| TO | subdoc. | rótulo | clase | forma | en la unidad | renglón | fin del anterior | posible ref. | descendientes tragados |
|---|---|---|---|---|---|---|---|---|---|
| ctacte |  | 1.3.1.9 | ii | cola | `ctacte::1.5.2.8` | «1.3.1.9., deberán consignarse al dorso del documento.» | «ponda conforme a lo previsto en el punto» | sí |  |
