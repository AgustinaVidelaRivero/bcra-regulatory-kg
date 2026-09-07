#!/usr/bin/env python3
"""U-B5.4 F1 — genera tabla_to_rol_post_f1.md y mide los deltas de las
opciones del mecanismo de rol. Solo escribe en el paquete de revisión.
Datos adjudicados a mano contra los chunks de e0_dry (sesión F1)."""
import csv
import json
import os
from pathlib import Path

# Salidas junto al script; raíz del repo sin ruta absoluta embebida (por
# defecto el cwd; se puede fijar con la variable de entorno BCRA_KG_REPO).
OUT = Path(__file__).resolve().parent
REPO = Path(os.environ.get("BCRA_KG_REPO", ".")).resolve()

# (to, sujetos_del_alcance, mapping, cita_chunk_id, verbatim_corto, nota)
# mapping: 'clase:<id>' = el alcance ES exactamente una clase existente (opción A2: sin id nuevo)
#          'clases:<id,id>' = dos clases exactas
#          'rol' = necesita id de rol (subconjunto, multi-sujeto o sujeto fuera de catálogo)
#          'hueco' = alcance no legible en las unidades E0
TABLA = [
 ("actgar", "entidades financieras (vía LEF)", "clase:Sujeto_entidad_financiera", "actgar::1.1",
  "Conforme a lo establecido en la Ley de Entidades Financieras, tales intermediarios no podrán afectar sus activos en garantía sin previa autorización del BCRA",
  "referencia elíptica («tales intermediarios»); sujeto inferido de la LEF"),
 ("adfsp", "entidades financieras", "clase:Sujeto_entidad_financiera", "adfsp::S1::chapeau_seccion",
  "El Banco Central podrá otorgar adelantos a las entidades financieras en el marco de lo previsto por el inciso f) del artículo 17 de su Carta Orgánica", ""),
 ("adrei", "EF de importancia sistémica local (D-SIB)", "rol", "adrei::1.1",
  "Las presentes normas rigen para las entidades financieras que sean consideradas por el BCRA como de importancia sistémica a nivel local (D-SIB)",
  "subconjunto de EF"),
 ("afiltr", "entidades financieras", "clase:Sujeto_entidad_financiera", "afiltr::S1::chapeau_seccion",
  "adelantos en cuenta y los redescuentos en pesos […] con destino a las entidades financieras para la atención de necesidades emergentes de situaciones de iliquidez transitoria", ""),
 ("apnf", "proveedores no financieros de crédito", "clase:Sujeto_proveedor_no_financiero_de_credito", "apnf::1.1",
  "Son considerados proveedores no financieros de crédito aquellas personas jurídicas que, sin ser entidades financieras […] realicen —como actividad principal o accesoria— oferta de crédito al público en general", ""),
 ("autenf", "autoridades de entidades financieras (personas en cargos)", "rol", "autenf::1.1::intro",
  "Las normas sobre “Autoridades de entidades financieras” son aplicables a las personas que ejercen los siguientes cargos",
  "sujeto humano-rol, fuera del catálogo de clases"),
 ("ayccef", "entidades financieras (todas las clases)", "clase:Sujeto_entidad_financiera", "ayccef::1.1.3",
  "Las restantes clases de entidades financieras previstas en la Ley de Entidades Financieras […] podrán realizar las operaciones activas, pasivas y de servicios que las disposiciones legales y las normas les autorizan",
  "sección 1 = «Clases y denominaciones de entidades financieras»"),
 ("cajasc", "cajas de crédito cooperativas", "clase:Sujeto_caja_de_credito_cooperativa", "cajasc::1.2.1",
  "para poder actuar como cajas de crédito cooperativas, las interesadas deberán constituirse como cooperativas y contar con autorización del Banco Central […] con ajuste a las previsiones contenidas en el presente ordenamiento", ""),
 ("ccbcra", "EF + cajas de crédito (L25.782) + entidades cambiarias", "rol", "ccbcra::1.1",
  "Las entidades financieras deberán mantener abierta en el BCRA una cuenta corriente en pesos. Dicha cuenta tendrá carácter optativo para las cajas de crédito (Ley 25.782) y las entidades cambiarias",
  "multi-sujeto"),
 ("cescar", "entidades financieras (cedentes)", "clase:Sujeto_entidad_financiera", "cescar::1.1",
  "Quedan comprendidas las ventas o cesiones, con o sin responsabilidad para la entidad financiera cedente, que se efectúen respecto de créditos otorgados a terceros", ""),
 ("coltit", "entidades financieras", "clase:Sujeto_entidad_financiera", "coltit::1.1",
  "Las entidades financieras, cualquiera sea su naturaleza jurídica, podrán emitir títulos valores representativos de deuda […] con ajuste a las presentes normas", ""),
 ("convca", "EF y otras habilitadas a conversión cambiaria", "rol", "convca::1.1",
  "Son operaciones de conversión cambiaria las que realiza el Banco Central a solicitud de las entidades financieras y otras habilitadas",
  "«otras habilitadas» excede la clase EF"),
 ("cryl", "EF + Mercados de Valores + FCI + Centrales Depositarias + CEC + otras a juicio del BCRA", "rol", "cryl::3.1",
  "Dispondrán de cuentas de registro: a) Las entidades comprendidas en la Ley 21.526 […] b) Mercados de Valores del país. c) Fondos Comunes de Inversión […] d) Centrales Depositarias […] e) Cámaras Electrónicas de Compensación (CEC)",
  "multi-sujeto"),
 ("ctacor", "EF del país (secc. 3: también casas de cambio)", "rol", "ctacor::1.1",
  "Las entidades financieras del país se encuentran facultadas para ofrecer la apertura de cuentas y la provisión de sus servicios relacionados a otras entidades financieras del país",
  "multi-sujeto (EF + casas de cambio en secc. 3.2.1)"),
 ("ctacte", "bancos (captación de cuenta corriente)", "clase:Sujeto_banco", "ctacte::1.1",
  "Los bancos explicitarán en un manual de procedimientos las condiciones que observarán para la apertura, funcionamiento y cierre de las cuentas corrientes", ""),
 ("ctavis", "cajas de crédito cooperativas", "clase:Sujeto_caja_de_credito_cooperativa", "ctavis::1.1",
  "Las cajas de crédito cooperativas que opten por prestar este servicio explicitarán en un manual de procedimientos las condiciones […] para la apertura, funcionamiento y cierre de las cuentas a la vista", ""),
 ("depaho", "bancos comerciales 1er grado + compañías financieras + cajas de crédito + sociedades de ahorro y préstamo", "rol", "depaho::1.1.1",
  "1.1.1. Bancos comerciales de primer grado. / 1.1.2. Compañías financieras. / 1.1.3. Cajas de crédito. / 1.1.4. Sociedades de ahorro y préstamo para la vivienda u otros inmuebles.",
  "punto 1.1 del índice: «Entidades intervinientes.»; multi-sujeto"),
 ("depinv", "entidades financieras", "clase:Sujeto_entidad_financiera", "depinv::1.1",
  "Las entidades financieras podrán captar fondos a plazo bajo la modalidad de depósitos […] únicamente con ajuste a las disposiciones establecidas en estas normas", ""),
 ("disres", "entidades financieras", "clase:Sujeto_entidad_financiera", "disres::S1",
  "Para distribuir resultados las entidades financieras deberán cumplir las presentes normas", ""),
 ("docvig", "HUECO", "hueco", "—",
  "—",
  "el TO enumera documentos de identificación válidos; ninguna unidad E0 declara el sujeto obligado (inferible: entidades que reciben los documentos). Secciones: «Para argentinos», «Para extranjeros», «Rectificación», «Verificación»"),
 ("efemin", "entidades financieras (filiales del país, base individual)", "rol", "efemin::4.1",
  "Las entidades financieras (comprendidas exclusivamente sus filiales en el país) observarán las normas en materia de efectivo mínimo en forma individual",
  "recorte de base de observancia; secc. 6.1 define además un subconjunto por listado (Anexo II Com. A 7859)"),
 ("evacre", "entidades financieras", "clase:Sujeto_entidad_financiera", "evacre::S1",
  "pautas básicas para evaluar adecuadamente el riesgo de crédito que las entidades financieras deberán observar", ""),
 ("expaef", "entidades financieras", "clase:Sujeto_entidad_financiera", "expaef::1.1.1",
  "Están autorizadas a instalar sucursales en el país las entidades financieras que, previamente, den cumplimiento a las exigencias de habilitación establecidas en el punto 1.5.1.", ""),
 ("fabcra", "EF, operadores de cambio, CEC, cajas de valores, mercados, compañías financieras, ALyC, Ministerio de Economía, ANSES («entidades»)", "rol", "fabcra::S1::chapeau_seccion",
  "La fórmula 2570 es el soporte utilizado por las entidades financieras, operadores de cambio, cámaras electrónicas de compensación, cajas de valores, mercados, compañías financieras, agentes de liquidación y compensación, Ministerio de Economía y ANSES —en adelante, también “entidades”—",
  "multi-sujeto amplio"),
 ("fclef", "fideicomisos financieros comprendidos en la LEF", "clase:Sujeto_fideicomiso_financiero", "fclef::S1",
  "Están comprendidos en la Ley de Entidades Financieras y sujetos a las normas del BCRA los fideicomisos financieros entre cuyos activos fideicomitidos se encuentren créditos originados por entidades financieras",
  "evidencia directa para MANTENER Sujeto_fideicomiso_financiero (hoy sin uso)"),
 ("fgarcp", "fondos de garantía de carácter público", "clase:Sujeto_fondo_de_garantia_publico", "fgarcp::1.1::intro",
  "Los fondos nacionales, provinciales o de la Ciudad Autónoma de Buenos Aires interesados en que las garantías que otorguen […] gocen del carácter de preferida deberán gestionar su inscripción ante el BCRA", ""),
 ("fimipyme", "HUECO", "hueco", "—",
  "—",
  "la sección 1 del índice se titula «Entidades alcanzadas. Las entidades financier…» pero E0 no produjo ninguna unidad de la sección 1 (las unidades del TO arrancan en 2.1); inferible: EF alcanzadas"),
 ("finsec", "entidades financieras (incl. sucursales y subsidiarias)", "clase:Sujeto_entidad_financiera", "finsec::2.1",
  "Las entidades financieras, comprendidas sus sucursales y sus subsidiarias del país y del exterior, no podrán refinanciar u otorgar asistencia financiera al sector público no financiero, salvo […]", ""),
 ("gerc", "entidades financieras", "clase:Sujeto_entidad_financiera", "gerc::1.1",
  "limitar la pérdida máxima que una entidad financiera podría experimentar […] deberán ser aplicadas en forma permanente respecto de las exposiciones al riesgo de crédito frente a toda contraparte", ""),
 ("gescre", "entidades financieras (implícito)", "clase:Sujeto_entidad_financiera", "gescre::1.1.2",
  "La entidad deberá llevar un legajo de cada deudor de su cartera, así como de cada uno de sus corresponsales",
  "sujeto implícito («la entidad»); sin pasaje de alcance explícito"),
 ("gracre", "entidades financieras", "clase:Sujeto_entidad_financiera", "gracre::7.1",
  "Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las normas en materia de graduación del crédito en forma individual", ""),
 ("graloc", "entidades financieras", "clase:Sujeto_entidad_financiera", "graloc::1.1",
  "Las presentes disposiciones regulan la gestión de los riesgos a los que están expuestas las entidades financieras desde la negociación de las operaciones de cambio hasta su liquidación final", ""),
 ("icmecma", "EF + ENFETC + fiduciarios de FF + administradores de carteras de ex-EF + otros PNFC", "rol", "icmecma::1.1.1",
  "1.1.1. Entidades financieras. / 1.1.2. Empresas no financieras emisoras de tarjetas […] / 1.1.3. Fiduciarios de fideicomisos financieros […] / 1.1.4. Administradores de carteras crediticias de ex-entidades financieras. / 1.1.5. Otros proveedores no financieros de crédito",
  "punto 1.1 del índice: «Sujetos alcanzados.»; multi-sujeto"),
 ("incuca", "entidades financieras (implícito)", "clase:Sujeto_entidad_financiera", "incuca::1.1",
  "La entidad deberá encuadrarse en la exigencia a más tardar en el segundo mes siguiente a aquel en que se registre el incumplimiento",
  "sujeto implícito («la entidad»)"),
 ("lavdin", "entidades financieras y cambiarias", "rol", "lavdin::1.1::intro",
  "Las entidades financieras y cambiarias deberán observar lo establecido en la legislación vigente en estas materias […] y en la presente reglamentación",
  "multi-sujeto (EF + entidades cambiarias)"),
 ("lingeef", "entidades financieras", "clase:Sujeto_entidad_financiera", "lingeef::1.1",
  "Las entidades financieras deben contar con un proceso integral para la gestión de riesgos, que incluya la vigilancia por parte del Directorio y de la Alta Gerencia", ""),
 ("lingob", "entidades financieras", "clase:Sujeto_entidad_financiera", "lingob::1.1",
  "las entidades financieras implementarán efectivamente en su organización un código de gobierno societario que comprenda a toda la entidad", ""),
 ("opefci", "entidades financieras", "clase:Sujeto_entidad_financiera", "opefci::1.1",
  "Las entidades financieras no podrán efectuar operaciones en mercados autorizados por la CNV del país o institucionalizados del exterior a menos de 30 días que directa o indirectamente impliquen una captación de fondos", ""),
 ("ordcom", "BCRA (emisor) y destinatarios de Comunicaciones (EF, cajas de crédito coop., etc.)", "rol", "ordcom::1.5::intro",
  "En los encabezamientos de las comunicaciones “A”, “B”, “C” y “D” se establecerán las denominaciones de los destinatarios, los cuales pueden ser uno o varios de los siguientes: [1.5.1. Entidades financieras. 1.5.2. Cajas de crédito cooperativas …]",
  "TO sobre la operatoria del propio BCRA; sujeto por defecto atípico"),
 ("osapsa", "EF (secc. 2,4,5) + ENFETC (secc. 3,5) + otros por sección", "rol", "osapsa::1.1",
  "1.1. Entidades financieras. Serán de aplicación las disposiciones contenidas en las Secciones 2., 4. y 5. / 1.2. Empresas no financieras emisoras de tarjetas de crédito y/o compra. Serán de aplicación las disposiciones contenidas en la Secciones 3. y 5.",
  "multi-sujeto con mapeo por sección (secc. 5 suma operadores de cambio y empresas de cobranzas extrabancarias)"),
 ("pagjub", "EF participantes del pago de beneficios ANSES", "rol", "pagjub::1.1",
  "Las entidades financieras que participen del servicio de pago de beneficios por cuenta de la ANSES deberán utilizar los instrumentos de pago y la metodología que ese ente administrador establezca",
  "subconjunto (participantes)"),
 ("pfmipyme", "plataformas para el financiamiento MiPyME (PFM)", "rol", "pfmipyme::1.1.1",
  "Se consideran plataformas para el financiamiento MiPyME (PFM) a las personas jurídicas que facilitan —como actividad principal o accesoria de su objeto social—, a través de herramientas y/o sistemas informáticos, la concertación de operaciones con facturas de crédito electrónicas MiPyME",
  "sujeto fuera del catálogo, definido por el propio TO"),
 ("pimf", "infraestructuras del mercado financiero (IMF) nominadas", "rol", "pimf::5.1",
  "Las siguientes IMF deberán cumplir con la aplicación de los principios […]: MEP — Cámara de Alto Valor (INTERBANKING) — Cámara de Bajo Valor (COELSA) — Redes de cajeros automáticos (Red Link, Newpay) — Administradores de esquemas de pago",
  "sujeto fuera del catálogo (IMF); def. en pimf::1.1.1"),
 ("pognme", "entidades financieras (implícito)", "clase:Sujeto_entidad_financiera", "pognme::1.2.2",
  "Los conceptos incluidos que registre la entidad financiera en sus sucursales en el exterior",
  "sujeto implícito; la sección 2 «Alcance» refiere a la posición, no al sujeto"),
 ("polcre", "entidades financieras", "clase:Sujeto_entidad_financiera", "polcre::1.1",
  "La asistencia crediticia que otorguen las entidades financieras deberá estar orientada a financiar la inversión, la producción, la comercialización, el consumo", ""),
 ("prevmi", "entidades financieras", "clase:Sujeto_entidad_financiera", "prevmi::1.1",
  "Estas normas mantendrán un alcance “regulatorio” […] sin perjuicio de que los estados financieros de las entidades financieras se ajustarán al marco contable vigente", ""),
 ("pscpp", "proveedores de servicios de créditos entre particulares (PSCPP)", "clase:Sujeto_pscpp", "pscpp::1.1",
  "Se consideran proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP) a aquellas personas jurídicas que ofrezcan […] el servicio de acercar y poner en contacto a uno o más oferentes con demandantes de crédito", ""),
 ("raapal", "entidades financieras", "clase:Sujeto_entidad_financiera", "raapal::3.1",
  "Las entidades financieras (comprendidas sus filiales en el país y en el exterior) observarán las presentes normas en forma individual", ""),
 ("ratiofn", "EF D-SIB + sucursales/subsidiarias de G-SIB", "rol", "ratiofn::1.1",
  "Las entidades financieras calificadas por el BCRA como de importancia sistémica a nivel local (D-SIB) y las sucursales o subsidiarias de bancos del exterior calificados como de importancia sistémica global (G-SIB) deberán cumplir las presentes disposiciones",
  "subconjunto de EF"),
 ("rdbcra", "personas jurídicas y humanas sometidas al ámbito de la LEF (sumariables)", "rol", "rdbcra::1.1.1.1",
  "Las personas jurídicas y humanas sometidas al ámbito de aplicación de la citada ley y/o alcanzadas según sus disposiciones, incluidas aquellas respecto de las cuales se hubiere decidido hacer extensivos sus términos, conforme al artículo 3 de la LEF",
  "alcance más amplio que cualquier clase del catálogo"),
 ("relact", "entidades financieras", "clase:Sujeto_entidad_financiera", "relact::6.1",
  "Las entidades financieras (casa central o matriz y filiales en el país y en el exterior) observarán las normas en materia de la relación para los activos inmovilizados […] en forma individual", ""),
 ("repefe", "representantes de EF del exterior no autorizadas", "rol", "repefe::1.1",
  "Es representante de entidad financiera del exterior no autorizada para operar en el país, la persona física autorizada por el BCRA —SEFyC— para actuar localmente en nombre y representación de tal entidad",
  "sujeto fuera del catálogo, definido por el propio TO"),
 ("retype", "Banco de la Nación Argentina + otros bancos públicos participantes (IAF)", "rol", "retype::1.1.2",
  "Las entidades bancarias participantes efectuarán el pago de los beneficios que el Instituto de Ayuda Financiera para Pago de Retiros y Pensiones Militares (IAF) les indique, por intermedio de todas sus casas",
  "subconjunto (bancos públicos participantes; 1.1.1 nombra al BNA)"),
 ("ri2_ci", "casas y agencias de cambio", "clases:Sujeto_casa_de_cambio,Sujeto_agencia_de_cambio", "ri2_ci::1.1.1::intro",
  "El control interno es un proceso efectuado por el Directorio o autoridad equivalente y el resto de los miembros de una casa o agencia de cambio",
  "dos clases exactas del catálogo"),
 ("rmrtsd", "EF + PSPs («sujetos obligados»)", "rol", "rmrtsd::1.1.1",
  "1.1.1. Entidades financieras. / 1.1.2. PSPs.",
  "punto 1.1 del índice: «Sujetos obligados.»; multi-sujeto"),
 ("rrci", "EF + PSP registrados + IMF sistémicas", "rol", "rrci::1.2",
  "Sujetos alcanzados. - Entidades financieras. - Proveedores de servicios de pago (PSP) incluidos en el Registro de PSP del BCRA. - Infraestructuras del mercado financiero conocidas como sistemas de pago de importancia sistémica",
  "multi-sujeto"),
 ("secfin", "entidades comprendidas en la LEF", "clase:Sujeto_entidad_financiera", "secfin::S1",
  "Las entidades comprendidas en la Ley de Entidades Financieras no pueden revelar las operaciones pasivas que realicen", ""),
 ("servco", "entidades financieras (secc. 2: bancos comerciales y compañías financieras)", "rol", "servco::1.1",
  "Las entidades financieras no se encuentran facultadas a efectuar —cualquiera sea su modalidad— operaciones ajenas a la intermediación financiera",
  "alcance por sección (secc. 2.1 restringe a bancos comerciales y compañías financieras)"),
 ("snp_atm", "EF que ofrezcan cuentas a la vista (+ empresas no financieras operadoras de cajeros)", "rol", "snp_atm::1.1.1",
  "Las entidades financieras que ofrezcan cuentas a la vista deberán permitir que sus clientes realicen operaciones a través de cajeros automáticos instalados en el país y operados por empresas no financieras",
  "subconjunto + segundo sujeto fuera de catálogo"),
 ("snp_cec", "cámaras electrónicas de compensación (CEC)", "rol", "snp_cec::S1::chapeau_seccion",
  "El servicio de compensación de cheques y otros valores (instrumentos compensables) solo podrá ser prestado por las cámaras de compensación que se ajusten a las condiciones que se establecen en las presentes normas",
  "sujeto fuera del catálogo (CEC)"),
 ("snp_debin", "EF y PSPCP (titulares de cuentas como ordenantes)", "rol", "snp_debin::2.1",
  "Los DEBIN podrán ser ordenados por personas humanas y jurídicas, titulares de cuentas a la vista en entidades financieras o de cuentas de pago en PSPCP […] o por cuenta propia de las entidades financieras",
  "multi-sujeto (EF + PSPCP)"),
 ("snp_psp", "PSP y EF (enfoque funcional)", "rol", "snp_psp::1.1.2",
  "tanto las entidades financieras como los PSP deberán observar las mismas reglas para funciones iguales que desarrollen en la provisión de servicios de pago en el marco del sistema nacional de pagos",
  "multi-sujeto (EF + PSP)"),
 ("snp_spd", "EF (+ PSP en los servicios de la Sección 3 en adelante)", "rol", "snp_spd::S1::chapeau_seccion",
  "Las entidades financieras deben asignarle una Clave Bancaria Uniforme (CBU) a toda cuenta a la vista, e informarla a sus clientes",
  "multi-sujeto (EF + PSP según servicio)"),
 ("snp_tr_nc", "EF y PSP (enfoque funcional)", "rol", "snp_tr_nc::1.2.1",
  "la presente reglamentación se aplicará por función dentro de un esquema de pago, de manera que sea homogénea para diferentes tipos de entidades que cumplan una misma función y por lo tanto compitan, ya sean entidades financieras o proveedores de servicios de pago (PSP)",
  "multi-sujeto (EF + PSP)"),
 ("socgar", "sociedades de garantía recíproca inscriptas", "clase:Sujeto_sociedad_de_garantia_reciproca", "socgar::1.1",
  "Las sociedades de garantía recíproca interesadas en que las garantías que otorguen […] gocen, por parte de las entidades financieras, del carácter de garantía preferida, deberán gestionar su inscripción ante el BCRA", ""),
 ("supcon", "EF y empresas del perímetro de supervisión consolidada", "rol", "supcon::2.2::intro",
  "Las definiciones precedentes se aplicarán a entidades y empresas de las siguientes clases",
  "multi-sujeto (EF + perímetro consolidado)"),
 ("tasint", "entidades financieras", "clase:Sujeto_entidad_financiera", "tasint::1.1",
  "Las tasas de interés compensatorio se concertarán libremente entre las entidades financieras y los clientes", ""),
 ("traval", "transportadoras de valores (TV: PSTV y TVP)", "rol", "traval::1.1::intro",
  "Comprende a las personas jurídicas que desempeñen la actividad de transporte terrestre de valores —Transportadoras de Valores (TV)—. Se entienden comprendidas […] las empresas Prestadoras de Servicios de Transporte de Valores (PSTV) y las Transportadoras de Valores Propias de las entidades financieras (TVP)",
  "sujeto fuera del catálogo; la confusión PSTV→id ajeno está medida (ESQ-2)"),
]

LABELS_ROL = {
 "adrei": "Entidades alcanzadas (Agregación de datos sobre riesgos: D-SIB)",
 "autenf": "Autoridades comprendidas (Autoridades de entidades financieras)",
 "ccbcra": "Entidades alcanzadas (Cuentas a la vista en el BCRA)",
 "convca": "Entidades habilitadas (Conversión cambiaria)",
 "cryl": "Sujetos habilitados (CRyL)",
 "ctacor": "Entidades intervinientes (Cuentas de corresponsalía)",
 "depaho": "Entidades intervinientes (Depósitos de ahorro)",
 "efemin": "Entidades alcanzadas (Efectivo mínimo)",
 "fabcra": "Entidades registrantes de firmas (Firmas autorizadas ante el BCRA)",
 "icmecma": "Sujetos alcanzados (Comunicación por medios electrónicos)",
 "lavdin": "Entidades alcanzadas (Prevención del lavado de activos)",
 "ordcom": "Destinatarios de Comunicaciones (Ordenamiento de Comunicaciones)",
 "osapsa": "Sujetos alcanzados (Otros servicios y actividades)",
 "pagjub": "Entidades participantes (Pago de beneficios ANSES)",
 "pfmipyme": "Plataformas para el financiamiento MiPyME (PFM)",
 "pimf": "Infraestructuras del mercado financiero alcanzadas (PIMF)",
 "ratiofn": "Entidades alcanzadas (Ratio de fondeo neto estable: D-SIB y suc. G-SIB)",
 "rdbcra": "Personas sumariables (Régimen disciplinario del BCRA)",
 "repefe": "Representantes de entidades financieras del exterior (Representantes)",
 "retype": "Entidades bancarias participantes (Pago de retiros y pensiones militares)",
 "rmrtsd": "Sujetos obligados (Servicios financieros digitales)",
 "rrci": "Sujetos alcanzados (Respuesta y recuperación ante ciberincidentes)",
 "servco": "Entidades alcanzadas (Servicios complementarios)",
 "snp_atm": "Entidades alcanzadas (SNP - Cajeros automáticos)",
 "snp_cec": "Cámaras electrónicas de compensación (SNP - CEC)",
 "snp_debin": "Entidades y PSPCP alcanzados (SNP - Débito Inmediato)",
 "snp_psp": "Sujetos alcanzados (SNP - Proveedores de servicios de pago)",
 "snp_spd": "Sujetos alcanzados (SNP - Servicios de pago)",
 "snp_tr_nc": "Sujetos alcanzados (SNP - Transferencias - Normas complementarias)",
 "supcon": "Entidades y empresas alcanzadas (Supervisión consolidada)",
 "docvig": "Sujetos obligados (Documentos de identificación) [HUECO]",
 "fimipyme": "Entidades alcanzadas (Financiamiento MiPyME) [HUECO]",
}

def main():
    assert len(TABLA) == 68, f"la tabla tiene {len(TABLA)} filas, no 68"
    ver = json.loads((REPO / "data/experiment/escalado_prep/veredictos_generalizacion.json").read_text())["por_to"]
    dig = sorted(t for t, v in ver.items() if v["veredicto"] == "digerible")
    assert [t for t, *_ in TABLA] == dig, "las filas no coinciden con los 68 digeribles"
    titulos = {}
    with open(REPO / "data/experiment/escalado_prep/inventario_tos.csv") as f:
        for row in csv.DictReader(f):
            titulos[row["id"]] = row["titulo_oficial"]

    n_clase = sum(1 for r in TABLA if r[2].startswith("clase"))
    n_rol = sum(1 for r in TABLA if r[2] == "rol")
    n_hueco = sum(1 for r in TABLA if r[2] == "hueco")
    assert n_clase + n_rol + n_hueco == 68

    lines = [
        "# U-B5.4 F1 — Tabla TO → rol de alcance (68 TOs digeribles, tandas 1–2)",
        "",
        "Fuente de los pasajes: `data/experiment/escalado_prep/e0_dry/<to>/chunks_<to>.json` (SOLO LECTURA).",
        "Adjudicación de esta unidad (F1): el pasaje citado es el que declara quiénes están comprendidos/alcanzados;",
        "cuando el TO no lo declara en ninguna unidad E0, la fila se reporta como HUECO (no se inventa).",
        "",
        f"Resumen (recomputado por `gen_tabla_to_rol_f1.py`): **{n_clase} TOs con alcance = clase(s) exacta(s) del catálogo** · "
        f"**{n_rol} TOs que requieren id de rol** (subconjunto, multi-sujeto o sujeto fuera de catálogo) · **{n_hueco} HUECOS** (docvig, fimipyme).",
        "",
        "| # | TO | título oficial | sujeto(s) del alcance | mapping propuesto | cita (chunk_id) | pasaje (recortado) | nota |",
        "|---:|---|---|---|---|---|---|---|",
    ]
    for i, (to, suj, mapping, cita, verb, nota) in enumerate(TABLA, 1):
        titulo = titulos.get(to, "?")
        if len(titulo) > 60:
            titulo = titulo[:57] + "…"
        v = verb if len(verb) <= 260 else verb[:257] + "…"
        lines.append(f"| {i} | {to} | {titulo} | {suj} | {mapping} | `{cita}` | «{v}» | {nota} |")
    lines += [
        "",
        "## Huecos (mandato F1.1: se reportan, no se inventan)",
        "",
        "- **docvig** — ninguna unidad E0 declara el sujeto obligado; el TO lista documentos válidos (secciones «Para argentinos», «Para extranjeros», …). Sujeto inferible: las entidades receptoras de los documentos. Decisión del rol: de la autora.",
        "- **fimipyme** — la sección 1 se titula «Entidades alcanzadas. Las entidades financier…» en el índice del PDF, pero E0 no produjo ninguna unidad de la sección 1 (las unidades del TO arrancan en 2.1). El pasaje existe en el PDF y no es legible en las unidades: hueco por definición del mandato.",
        "",
        "## Filas con sujeto implícito (pasaje débil, no hueco)",
        "",
        "- actgar (referencia elíptica «tales intermediarios», resuelta por la LEF), gescre, incuca, pognme («la entidad» sin declaración de alcance). Se citan con su mejor pasaje disponible y quedan marcadas en la columna nota.",
    ]
    (OUT / "tabla_to_rol_post_f1.md").write_text("\n".join(lines))
    print(f"tabla_to_rol_post_f1.md: {len(TABLA)} filas | clase(s) exacta(s): {n_clase} | rol: {n_rol} | huecos: {n_hueco}")

    # ---- medición de deltas por opción ----
    import sys
    sys.path.insert(0, str(REPO / "data/experiment/esq/code"))
    import prompt_congelado as pc
    prefijo_chars = len(pc.PREFIJO_SISTEMA_CONGELADO)
    tool_chars = len(json.dumps(pc.TOOL_SCHEMA_CONGELADO, ensure_ascii=False))
    total_chars = prefijo_chars + tool_chars
    CW_ESQ2 = 9983  # tokens de cache write medidos en ESQ-2 (laudo B5.5 §3)
    ratio = total_chars / CW_ESQ2

    def rol_id(to):
        return f"Sujeto_rol_alcance_{to}"

    # bloque A1: una línea por TO (los 68)
    lineas_a1 = []
    enum_a1 = []
    for to, suj, mapping, cita, verb, nota in TABLA:
        label = LABELS_ROL.get(to) or f"Entidades alcanzadas ({titulos.get(to,'?')[:40]})"
        lineas_a1.append(f"{rol_id(to)} — {label} [rol del TO {to}.pdf]")
        enum_a1.append(rol_id(to))
    bloque_a1 = "\n".join(lineas_a1)
    enum_a1_chars = sum(len(e) + 4 for e in enum_a1)  # comillas+coma+espacio en el JSON del schema
    a1_chars = len(bloque_a1) + enum_a1_chars

    # bloque A2: solo los 'rol' (+2 huecos si la autora les asigna rol)
    tos_a2 = [r[0] for r in TABLA if r[2] == "rol"]
    lineas_a2 = [l for l, r in zip(lineas_a1, TABLA) if r[2] == "rol"]
    enum_a2_chars = sum(len(rol_id(t)) + 4 for t in tos_a2)
    a2_chars = len("\n".join(lineas_a2)) + enum_a2_chars

    # opción B: un único id deíctico
    linea_b = "Sujeto_rol_alcance_to — Sujetos alcanzados por el TO del chunk (se resuelve por procedencia) [rol deíctico]"
    b_chars = len(linea_b) + len("Sujeto_rol_alcance_to") + 4

    UNIDADES = 6340
    RATE_IN, RATE_CW, RATE_CR = 1.0e-6, 1.25e-6, 0.10e-6  # USD/token claude-haiku-4-5

    def costo(delta_chars, escrituras=1):
        toks = delta_chars / ratio
        cw = toks * RATE_CW * escrituras
        cr = toks * RATE_CR * UNIDADES
        return toks, cw, cr

    res = {}
    for nombre, chars in [("A1 (68 ids)", a1_chars), (f"A2 ({len(tos_a2)} ids)", a2_chars), ("B (1 id deíctico)", b_chars)]:
        toks, cw, cr = costo(chars)
        res[nombre] = (chars, toks, cw, cr)
        print(f"{nombre}: +{chars} chars ≈ +{toks:.0f} tokens | cache write +USD {cw:.4f} | reads {UNIDADES} unidades +USD {cr:.2f}")
    # opción C: enum dinámico por TO → 68 escrituras del prefijo completo
    prefijo_toks = CW_ESQ2
    c_extra_writes = 67 * prefijo_toks * RATE_CW
    print(f"C (enum por TO): +1 línea por namespace (~{costo(95)[0]:.0f} tok) | 67 escrituras extra del prefijo ≈ +USD {c_extra_writes:.2f}/corrida")
    print(f"ratio usado: {total_chars} chars (sistema {prefijo_chars} + tools {tool_chars}) / {CW_ESQ2} tok = {ratio:.2f} chars/token")

    with open(OUT / "medicion_deltas_rol_f1.json", "w") as f:
        json.dump({
            "ratio_chars_por_token": ratio,
            "base": {"prefijo_chars": prefijo_chars, "tool_schema_chars": tool_chars, "cw_esq2_tokens": CW_ESQ2},
            "unidades_corrida": UNIDADES,
            "tarifas_usd_por_token": {"input": RATE_IN, "cache_write": RATE_CW, "cache_read": RATE_CR, "modelo": "claude-haiku-4-5"},
            "opciones": {k: {"delta_chars": v[0], "delta_tokens": round(v[1]), "cache_write_usd": round(v[2], 4), "cache_reads_usd": round(v[3], 2)} for k, v in res.items()},
            "opcion_C_escrituras_extra_usd": round(c_extra_writes, 2),
            "n_tos_por_mapping": {"clase_exacta": n_clase, "rol": n_rol, "hueco": n_hueco},
        }, f, ensure_ascii=False, indent=1)
    (OUT / "bloque_borrador_roles_A1_f1.txt").write_text(bloque_a1 + "\n")

if __name__ == "__main__":
    main()
