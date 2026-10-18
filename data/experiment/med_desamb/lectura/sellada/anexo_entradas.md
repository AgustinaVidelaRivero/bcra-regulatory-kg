# Anexo: las entradas de la planilla

Las 18 entradas distintas que aparecen en la planilla (sello de la lista `811bd20fb31a78bcd7a0d331c6447d46ccf66c80cef214441f465c9b8d13e3bf`), en orden alfabético. Solo datos del catálogo; no dice en qué ítem ni por qué aparece cada una.

## `Sujeto_alta_gerencia`

- **Etiqueta:** Alta Gerencia
- **Alias:** sin alias
- **Definición:** ES la Gerencia General y los gerentes que tienen poder decisorio y dependen directamente de ella o del presidente del Directorio.
- **Padre:** Sujeto_instancia_de_gobierno_societario

## `Sujeto_banco`

- **Etiqueta:** Bancos
- **Alias:** sin alias
- **Definición:** ES la entidad financiera autorizada como banco (comercial, de inversión o hipotecario).
- **Padre:** Sujeto_entidad_financiera
- **Es el alcance de:** ctacte.pdf

## `Sujeto_cliente`

- **Etiqueta:** Clientes
- **Alias:** sin alias
- **Definición:** ES la unidad económica receptora de fondos de la entidad o titular de una garantía a su favor, residente o no.
- **Padre:** Sujeto_contraparte

## `Sujeto_comite_de_auditoria`

- **Etiqueta:** Comité de auditoría
- **Alias:** sin alias
- **Definición:** ES el comité, integrado por miembros del Directorio, que asiste al Directorio o autoridad equivalente en el monitoreo de los controles internos, la gestión de riesgos y el cumplimiento de normas, del proceso de emisión de los estados financieros, de la idoneidad e independencia del auditor externo y del desempeño de las auditorías interna y externa.
- **Padre:** Sujeto_instancia_de_gobierno_societario

## `Sujeto_directorio`

- **Etiqueta:** Directorio
- **Alias:** Consejo de Administración
- **Definición:** ES el Directorio de la entidad financiera o el órgano o autoridad que cumpla funciones semejantes, independientemente de la designación que utilice la entidad.
- **Padre:** Sujeto_instancia_de_gobierno_societario

## `Sujeto_ecai`

- **Etiqueta:** Agentes de calificación externa (ECAI)
- **Alias:** ECAI
- **Definición:** sin definición
- **Padre:** Sujeto_sujeto_regulado

## `Sujeto_entidad_financiera`

- **Etiqueta:** Entidades financieras
- **Alias:** Entidades financieras emisoras de tarjetas de crédito y/o compra, Entidad financiera emisora de tarjetas de crédito y/o compra
- **Definición:** ES el intermediario autorizado por el BCRA a operar bajo la Ley de Entidades Financieras (bancos, compañías financieras, cajas de crédito cooperativas). Quien no tiene esa autorización (aseguradoras, PSP, PNFC, transportadoras de valores) no es entidad financiera.
- **Padre:** Sujeto_sujeto_regulado
- **Es el alcance de:** actgar.pdf, adfsp.pdf, afiltr.pdf, ayccef.pdf, cescar.pdf, coltit.pdf, depinv.pdf, disres.pdf, evacre.pdf, expaef.pdf, finsec.pdf, gerc.pdf, gescre.pdf, gracre.pdf, graloc.pdf, incuca.pdf, lingeef.pdf, lingob.pdf, opefci.pdf, pognme.pdf, polcre.pdf, prevmi.pdf, raapal.pdf, relact.pdf, secfin.pdf, tasint.pdf

## `Sujeto_entidad_girada`

- **Etiqueta:** Entidades giradas
- **Alias:** entidad girada, banco girado
- **Definición:** ES la entidad sobre la cual está girado el cheque u otro instrumento compensable, obligada a su pago o rechazo.
- **Padre:** Sujeto_sujeto_regulado

## `Sujeto_persona_humana`

- **Etiqueta:** Personas humanas
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** Sujeto_cliente

## `Sujeto_proveedor_no_financiero_de_credito`

- **Etiqueta:** Proveedores no financieros de crédito
- **Alias:** PNFC
- **Definición:** ES la persona jurídica que, sin ser entidad financiera, oferta crédito al público de manera habitual (incluye mutuales, cooperativas y empresas emisoras de tarjetas).
- **Padre:** Sujeto_sujeto_regulado
- **Es el alcance de:** apnf.pdf

## `Sujeto_rol_alcance_capmin`

- **Etiqueta:** Entidades alcanzadas (Capitales Mínimos)
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** sin padre
- **Es un rol; sus miembros:** Entidades financieras
- **Es el alcance de:** TO_capitales_minimos_actual.pdf

## `Sujeto_rol_alcance_pagjub`

- **Etiqueta:** Entidades participantes (Pago de beneficios ANSES)
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** sin padre
- **Es el alcance de:** pagjub.pdf

## `Sujeto_rol_entidad_autorizada_exterior`

- **Etiqueta:** Entidades autorizadas a operar en cambios (Exterior)
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** sin padre
- **Es un rol; sus miembros:** Entidades financieras, Entidades cambiarias
- **Es el alcance de:** TO_exterior_cambios_actual.pdf

## `Sujeto_rol_entidad_comprendida_reginf`

- **Etiqueta:** Entidades comprendidas (Régimen Informativo)
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** sin padre
- **Es un rol; sus miembros:** Entidades financieras
- **Es el alcance de:** TO_regimen_informativo_contable_mensual_actual.pdf

## `Sujeto_rol_obligado_a_clasificar_clasificacion`

- **Etiqueta:** Obligados a clasificar deudores (Clasificación)
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** sin padre
- **Es un rol; sus miembros:** Entidades financieras, Proveedores no financieros de crédito, Fiduciarios de fideicomisos financieros, Sociedades de garantía recíproca, Fondos de garantía de carácter público, Proveedores de servicios de créditos entre particulares a través de plataformas (PSCPP)
- **Es el alcance de:** TO_clasificacion_deudores_actual.pdf

## `Sujeto_rol_sujeto_obligado_proteccion`

- **Etiqueta:** Sujetos obligados (Protección de usuarios)
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** sin padre
- **Es un rol; sus miembros:** Entidades financieras, Entidades cambiarias, Fiduciarios de fideicomisos financieros, Empresas no financieras emisoras de tarjetas de crédito y/o compra, Proveedores no financieros de crédito, Proveedores de servicios de pago que ofrecen cuentas de pago (PSPCP), Proveedores de servicios de pago iniciadores que prestan el servicio de billetera digital (PSI)
- **Es el alcance de:** TO_proteccion_usuarios_servicios_financieros_actual.pdf

## `Sujeto_sujeto`

- **Etiqueta:** Sujetos
- **Alias:** sin alias
- **Definición:** sin definición
- **Padre:** sin padre

## `Sujeto_usuario_de_servicios_financieros`

- **Etiqueta:** Usuarios de servicios financieros
- **Alias:** sin alias
- **Definición:** ES la persona (humana o jurídica) destinataria final de un servicio financiero, en los términos de las normas de Protección de los usuarios.
- **Padre:** Sujeto_contraparte
