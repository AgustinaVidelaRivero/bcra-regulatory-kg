# Lectura de los 45 casos de copia de la nota de E3 (P3b-2)

04/10/2026. USD 0. La regla es `regla_lectura_copia_nota.md` (sha256 `1427b16c61f4…`). La fijé antes de generar la
lista para leer: el registro con la hora y el sha está en el paquete de revisión. La lista lado a lado sale de
`lista_copia_nota.py` y lee `p3b/salida/lazo_e3_p3b.json`, corrida `salida_dirigida`.

## Resultado

| Clase | Casos | Unidades |
|---|---|---|
| Copia real | 11 | 11 |
| Coincidencia legítima | 34 | 29 |
| Dudosa | 0 | 0 |
| **Total** | **45** | **40** |

Las 11 copias reales están en 11 unidades distintas, y ninguna de ellas tiene también una coincidencia legítima. Los
34 casos legítimos están en 29 unidades: `cla::4.4`, `ext::13.4.1`, `ext::3.3.3.4`, `ext::8.5.17.5` y
`ctacte::5.1.2.1` tienen dos cada una. Los conteos salen de la tabla de abajo, recomputados en
`clasificacion_copia_nota.json`.

- Ninguna copia real lleva metalenguaje del verificador. La regla 1 no se cumplió en ningún caso.
- La ayuda del script marcó «entidad» en el caso 14, pero ahí es «entidad financiera», el término de la norma.
- **Lo que traen de la nota las 11 copias reales:**
  - 4 traen contenido de la nota (casos 4, 15, 24 y 44): una paráfrasis interpretativa, una frase sobre la estructura
    del texto, la sustitución de un régimen y un marcador de posición que la nota citaba de la primera extracción;
  - 7 agregan a palabras de la norma solo un verbo o una nominalización (casos 13, 19, 27, 35, 36, 37 y 41).
- La regla marca palabras. No mide si el contenido cambia: las 11 son copias según la regla, no errores de contenido.
- La defensa 2 marca los 45 casos. Que 34 sean coincidencias legítimas está previsto: la marca no rechaza, y su
  lectura es la de este reporte.

## Caso por caso

Clase: R = copia real, L = coincidencia legítima, D = dudosa. «Ausente» es una palabra de contenido de las ventanas
que no está en el texto de la unidad. Las flexiones cuentan como presentes, como manda la regla 2.

| # | Unidad | Entidad, campo | Clase | Razón |
|---|---|---|---|---|
| 1 | `cla::2.2.4::intro` | e1 Excepcion, descripción | L | «sucursales locales de entidades financieras»: lee la rama de «sucursales y subsidiarias locales…» |
| 2 | `cla::4.4` | e1 Operacion, etiqueta | L | «evaluación de capacidad de repago» = «la evaluación de la capacidad de repago» sin artículo |
| 3 | `cla::4.4` | e2 Definicion, descripción | L | la misma frase que el caso 2 |
| 4 | `cla::6.3.3` | c2 Condicion, descripción | R | «distintos de los cubiertos en otros puntos de 6.3»: paráfrasis de la nota; la norma dice «en los demás casos» |
| 5 | `cla::6.5.5.8` | e2 Condicion, etiqueta | L | «puntos 3.1/3.2»: la norma dice «los puntos 3.1. y 3.2.» y «cumplimiento de los citados puntos» |
| 6 | `cap::12.3` | e4 Definicion, etiqueta | L | compresión de «promedio de los últimos 36 meses… en moneda homogénea» |
| 7 | `cap::2.12.10::intro` | d1 Definicion, descripción | L | «la parte no deducible de» = «(parte no deducible de la RPC» |
| 8 | `cap::8.3.5::intro` | e1 Operacion, descripción | L | reordena «computables como capital… en poder de terceros» |
| 9 | `cap::8.4.1.6` | e2 Excepcion, etiqueta | L | «contemplados en 8.4.1.19 y 8.4.2» = «no contemplados en los puntos 8.4.1.19. y 8.4.2.» |
| 10 | `ext::13.2.7::cierre` | cond1 Condicion, etiqueta | L | «no comprendido en 13.2.1 a 13.2.5» = «no comprendido en los puntos 13.2.1. a 13.2.5.» |
| 11 | `ext::13.4.1` | e2 Condicion, descripción | L | «servicios… prestados o devengados hasta el 12/12/23», del título 13.4, sin «de no residentes» |
| 12 | `ext::13.4.1` | e2 Condicion, etiqueta | L | la misma frase que el caso 11 |
| 13 | `ext::14.2.1.10` | e3 Condicion, descripción | R | «que rigen el acceso al mercado» viene de la nota; ausente: «rigen» |
| 14 | `ext::2.6.2.1` | e1 Obligacion, etiqueta | L | «nominar única entidad financiera local» = «nominar una única entidad financiera local» |
| 15 | `ext::3.18.3::intro` | e3 Operacion, descripción | R | «La tabla de coeficientes… continúa en la enumeración siguiente»: frase de la nota sobre el texto; ausente: «tabla» |
| 16 | `ext::3.3.3.2` | e4 Excepcion, descripción | L | «el requisito de conformidad previa del BCRA» une «Este requisito» y «la conformidad previa del BCRA» del 3.3.3 |
| 17 | `ext::3.3.3.4` | e2 Operacion, descripción | L | «el acreedor es una contraparte vinculada» = «el acreedor sea una contraparte vinculada» |
| 18 | `ext::3.3.3.4` | e3 Excepcion, descripción | L | la misma frase que el caso 16 |
| 19 | `ext::3.5.4.2` | cond1 Condicion, etiqueta | R | «Vigencia del requisito…» es la frase de la nota; ausente: «vigencia» (la norma dice «vigente») |
| 20 | `ext::3.5.6::cierre` | e2 Operacion, descripción | L | «endeudamientos financieros con el exterior» completa el título cortado del 3.5 |
| 21 | `ext::3.6.1.4` | e4 Excepcion, descripción | L | «de acceso al mercado de [cambios]»: la norma dice «el acceso al mercado de cambios» |
| 22 | `ext::4.4.1` | op1 Operacion, etiqueta | L | «Suscripción de bonos BOPREAL por [parte de] deudores de importaciones», del título 4.4 |
| 23 | `ext::4.8.6::intro` | e1 Condicion, etiqueta | L | compresión de «venta con obligación de recompra… bonos BOPREAL… suscripción primaria» |
| 24 | `ext::7.1.1::intro` | e4 Excepcion, descripción | R | «en lugar del régimen general de plazos» viene de la nota; ausentes: «lugar», «general» |
| 25 | `ext::7.10.1.1` | e3 Operacion, etiqueta | L | «Pago de capital e intereses de deudas por importación» = texto propio sin «a partir del vencimiento» |
| 26 | `ext::7.10.1.4` | e2 Potestad, etiqueta | L | «de cobros de exportaciones para»: la norma dice «aplicación de cobros de exportaciones» y «para las siguientes operaciones» |
| 27 | `ext::7.11::intro` | e3 Potestad, descripción | R | el título con el verbo de la nota; ausente: «quedan» |
| 28 | `ext::7.9.3.2` | e3 Condicion, etiqueta | L | «Exportadores que opten por el mecanismo» = «Los exportadores que opten por este mecanismo» |
| 29 | `ext::8.5.17.5` | e2 Excepcion, descripción | L | «seguimiento de [las] negociaciones de divisas», del título de la sección 8 |
| 30 | `ext::8.5.17.5` | e2 Excepcion, etiqueta | L | «operaciones bajo régimen de muestras»: «Régimen de muestras» y «Operaciones aduaneras exceptuadas» |
| 31 | `ext::8.5.17.7` | e1 Excepcion, descripción | L | «seguimiento de [las] negociaciones de divisas por exportaciones», del título de la sección 8 |
| 32 | `ext::9.3.7` | e3 Condicion, descripción | L | «ha solicitado la aplicación a permisos» = «ha solicitado su aplicación a permisos» |
| 33 | `ctacte::10.2.1.3` | e1 Obligacion, descripción | L | «requisito común de contenido mínimo» une los títulos «Contenido mínimo» y «Requisitos comunes» |
| 34 | `ctacte::10.2.1.4` | o1 Obligacion, descripción | L | «el carácter con el que [fue impuesto]» es el texto propio |
| 35 | `ctacte::10.2.4.2` | e1 Obligacion, descripción | R | «Informar el saldo de la cuenta»: el verbo de la nota; ausente: «informar» |
| 36 | `ctacte::3.2.1.2` | e2 Restriccion, descripción | R | «determina que el título carece de valor como cheque» es la frase de la nota; ausente: «determina» |
| 37 | `ctacte::3.2.1.7` | e3 Excepcion, descripción | R | «determina la carencia de valor como cheque» es la frase de la nota; ausentes: «determina», «carencia» |
| 38 | `ctacte::5.1.2.1` | e3 Operacion, descripción | L | «endoso a favor de entidades [financieras]» une «transmisible por endoso» y el texto propio |
| 39 | `ctacte::5.1.2.1` | e3 Operacion, etiqueta | L | la misma frase que el caso 38 |
| 40 | `ctacte::6.2.5` | e2 Excepcion, descripción | L | «no son susceptibles de rechazo» = «Casos no susceptibles de rechazo» |
| 41 | `ctacte::6.4.1.1` | e1 Obligacion, etiqueta | R | «Consignar todos los motivos del rechazo»: el verbo de la nota; ausente: «consignar» (la norma dice «con expresa mención de») |
| 42 | `ctacte::8.2.1.1` | e4 Operacion, descripción | L | «Inclusión en la Central de cheques rechazados» = «Motivos de inclusión» y «En la “Central de cheques rechazados”» |
| 43 | `lingob::4.1` | e3 Condicion, etiqueta | L | «integrante con experiencia contable/financiera» = «integrantes posea amplia experiencia en temas contables y/o financieros» |
| 44 | `pagjub::2.8.2::intro` | e3 Obligacion, descripción | R | copia el marcador «[acciones de liquidación de la rendición de cuentas]» que la nota citaba de la primera extracción; ausente: «acciones» |
| 45 | `docvig::3.1.4` | e3 Operacion, etiqueta | L | «Modificación del número de DNI», del título del punto |
