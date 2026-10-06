# Lectura de los casos de copia de la nota de E3 (U-REEXT-T0, T4, punto 3)

Regla `regla_lectura_copia_nota.md` (sha256 `1427b16c61f4…`), sin ajustes. 86 casos en 64 unidades: copia real 29, coincidencia legítima 54, dudosa 3, metalenguaje 0. Unidades con al menos una copia real: 27. Referencia (r2a): 11 de 45.

| # | Unidad | Entidad, campo | Clase | Razón |
|---|---|---|---|---|
| 1 | `pro::1.1.2.1` | to TextoOrdenado, label | copia real | ausentes «protección», «usuarios», «servicios»: son el título del TO (label del TextoOrdenado), no texto de la unidad |
| 2 | `pro::1.1.2.1` | e1 Definicion, descripcion | copia real | ausentes «protección», «usuarios», «servicios»: la frase de la nota, que es el título del TO |
| 3 | `pro::2.3.1.1` | e11 Condicion, label | copia real | ausente «cómputo» (la unidad no tiene ninguna forma de computar) |
| 4 | `pro::2.3.4` | c2 Condicion, descripcion | copia real | ausente «basta»: «no basta con alguna» es la frase de la nota |
| 5 | `cla::3.3.2` | e7 Obligacion, descripcion | coincidencia legítima | «el manual de procedimientos de» es la frase de la norma |
| 6 | `cla::3.4.1` | e1 Operacion, label | coincidencia legítima | «llevar un legajo de cada deudor», sin el artículo |
| 7 | `cla::3.4.1` | e4 Obligacion, label | copia real | ausente «obligación»: nominalización que agrega la nota; «abrir» está en la unidad («abrirse») |
| 8 | `cla::3.4.1` | e6 Condicion, descripcion | coincidencia legítima | «cedidos por deudores en concurso preventivo», literal |
| 9 | `cla::3.4.1` | e6 Condicion, label | coincidencia legítima | ídem caso 8 |
| 10 | `cla::6.5.5.2` | e8 Restriccion, descripcion | copia real | ausente «anterior»: «el porcentaje del párrafo anterior» es la frase de la nota |
| 11 | `cla::6.5.5.2` | e9 Condicion, descripcion | coincidencia legítima | «en los términos del punto 2.2.5.», literal |
| 12 | `ric::5.1.3::intro` | e2 Condicion, descripcion | coincidencia legítima | «Grupos A, B o C», literal |
| 13 | `ric::5.1.3::intro` | e2 Condicion, label | coincidencia legítima | ídem caso 12 |
| 14 | `cap::2.2.1` | e1 Excepcion, descripcion | copia real | ausentes «cómputo», «excluidas», «quedan»: la exclusión del cómputo es la lectura de la nota |
| 15 | `cap::2.2.3.3` | e2 Obligacion, descripcion | copia real | ausente «exclusivamente»: la nota glosa «sólo» |
| 16 | `cap::2.2.3.3` | e2 Obligacion, label | coincidencia legítima | «con fondos de líneas asignadas», literal |
| 17 | `cap::4.1::intro` | e4 Excepcion, label | coincidencia legítima | «no se incluyen las operaciones de pase que no hayan podido liquidarse»: «liquidadas», flexión |
| 18 | `cap::5.3.1.2` | e1 Operacion, descripcion | coincidencia legítima | «garantía bajo el método simple», de la norma |
| 19 | `cap::8.3.5::intro` | e1 Definicion, descripcion | copia real | ausente «integra» |
| 20 | `cap::8.6::intro` | e4 Excepcion, descripcion | copia real | ausente «régimen» |
| 21 | `ext::10.3.5::intro` | e3 Excepcion, descripcion | copia real | ausente «quedan»: «quedan reemplazados» es la frase de la nota |
| 22 | `ext::10.3.6` | e3 Excepcion, label | coincidencia legítima | «requisitos de acceso del cliente», de la norma |
| 23 | `ext::11.1.3.7` | e1 Obligacion, descripcion | copia real | ausente «operación» |
| 24 | `ext::13.2.6` | e1 Operacion, label | coincidencia legítima | «no comprendido en los puntos 13.2.1. a 13.2.5.» sin «los puntos» |
| 25 | `ext::13.2.6` | e2 Condicion, label | coincidencia legítima | ídem caso 24 |
| 26 | `ext::2.2.2.1` | c1 Condicion, descripcion | coincidencia legítima | «códigos de concepto» y los servicios de la lista, de la norma |
| 27 | `ext::2.2.2.1` | c1 Condicion, label | dudosa | las palabras están («específicas» solo en «disposiciones específicas»), pero «servicios específicos» es la frase de la nota y no reformula la norma, que dice «los siguientes códigos de concepto» |
| 28 | `ext::2.6.1.2` | d1 Definicion, label | copia real | ausente «sujeto»; «alcanzado» es flexión de «alcanzadas» |
| 29 | `ext::2.7::cierre` | e5 Condicion, descripcion | copia real | ausente «cómputo» («computados» es otra palabra, derivada) |
| 30 | `ext::3.11.1::intro` | e1 Potestad, descripcion | coincidencia legítima | «podrán dar acceso al mercado de cambios», de la norma |
| 31 | `ext::3.11.1::intro` | e1 Potestad, label | coincidencia legítima | ídem caso 30 |
| 32 | `ext::3.11.2.1` | e1 Potestad, label | coincidencia legítima | ídem caso 30 |
| 33 | `ext::3.11.3.1` | e2 Potestad, label | coincidencia legítima | ídem caso 30 |
| 34 | `ext::3.3.3.3` | e1 Excepcion, descripcion | coincidencia legítima | «el requisito de conformidad previa del BCRA», de la norma (como los casos 16 y 18 de P3b-2) |
| 35 | `ext::3.4.4.2` | e3 Condicion, descripcion | copia real | ausentes «basta» y «supuesto» |
| 36 | `ext::3.4.4.7` | c1 Condicion, descripcion | dudosa | frase sobre la estructura del texto («de las cuales la situación del punto 3.4.4.7 es una»), que está en la nota; la norma la dice con otras palabras («alguna de las siguientes situaciones») |
| 37 | `ext::3.5.1.7` | c2 Condicion, descripcion | coincidencia legítima | «el acceso al mercado de cambios», de la norma |
| 38 | `ext::3.5.1.7` | c3 Condicion, descripcion | coincidencia legítima | «no registren vencimientos de capital»: «deben registrar», flexión |
| 39 | `ext::3.5.1.7` | c4 Condicion, descripcion | coincidencia legítima | «en los primeros 2 (dos) años por el endeudamiento», literal |
| 40 | `ext::3.5.1.7` | c5 Condicion, descripcion | coincidencia legítima | ídem caso 39 |
| 41 | `ext::3.5.1.7` | c6 Condicion, descripcion | coincidencia legítima | ídem caso 39 |
| 42 | `ext::3.5.3.5` | c1 Condicion, descripcion | coincidencia legítima | «con una anterioridad no mayor a 3», de la norma |
| 43 | `ext::3.5.4.3` | e1 Excepcion, descripcion | coincidencia legítima | remite al 3.5.4 por su número, como su encabezado («3.5.4. En la medida que…») |
| 44 | `ext::3.5.4::intro` | e1 Condicion, descripcion | copia real | ausente «vigencia» (la norma dice «vigente»): el mismo caso que el 19 de P3b-2 |
| 45 | `ext::3.5.6.11` | p1 Potestad, descripcion | dudosa | «incluido el presente punto 3.5.6.11» es una frase de la nota sobre la estructura; «incluido» está como «incluyendo» en otra oración |
| 46 | `ext::3.5.6.8` | e3 Excepcion, descripcion | coincidencia legítima | ídem caso 34 |
| 47 | `ext::3.6.1.6` | e3 Excepcion, descripcion | copia real | ausente «prohibición» (la norma dice «Se prohíbe»: nominalización de la nota) |
| 48 | `ext::3.6.1.6` | e6 Excepcion, descripcion | copia real | ídem caso 47 |
| 49 | `ext::4.4.1` | e3 Condicion, label | copia real | ausente «calificación» |
| 50 | `ext::4.4.2` | e1 Operacion, descripcion | coincidencia legítima | «BOPREAL por deudores de importaciones», del título 4.4 (como el caso 22 de P3b-2) |
| 51 | `ext::4.4.2` | e1 Operacion, label | coincidencia legítima | ídem caso 50 |
| 52 | `ext::4.6.1::intro` | e1 Operacion, descripcion | coincidencia legítima | «el equivalente en moneda local», de la norma |
| 53 | `ext::4.6.1::intro` | e2 Restriccion, descripcion | coincidencia legítima | ídem caso 52 |
| 54 | `ext::4.8.4.2` | e1 Condicion, descripcion | coincidencia legítima | «haber suscripto BOPREAL Serie 1», de la norma |
| 55 | `ext::4.8.6::intro` | e1 Operacion, label | coincidencia legítima | «venta con obligación de recompra de BOPREAL», de la norma (como el caso 23 de P3b-2) |
| 56 | `ext::4.8.6::intro` | e2 Condicion, descripcion | coincidencia legítima | ídem caso 55 |
| 57 | `ext::7.1.1.3` | e2 Obligacion, descripcion | coincidencia legítima | «los capítulos 26 y 71», literal |
| 58 | `ext::7.10.2.2` | e1 Excepcion, descripcion | coincidencia legítima | «en caso de no disponerla… la documentación que avale la capitalización»: flexiones |
| 59 | `ext::7.3.11` | e2 Potestad, descripcion | coincidencia legítima | «al cumplimiento de las condiciones», de la norma |
| 60 | `ext::7.9.2::intro` | e1 Operacion, label | coincidencia legítima | «operaciones 7.9.1.1», de la norma |
| 61 | `ext::7.9.3.3` | e4 Obligacion, descripcion | copia real | ausentes «1» y «x»: «7.9.3.1 a 7.9.3.x» es el marcador de posición de la nota (como el caso 44 de P3b-2) |
| 62 | `ext::8.5.18.3` | e2 Potestad, descripcion | copia real | ausente «facultad» |
| 63 | `ext::9.1.7` | e1 Operacion, descripcion | copia real | ausente «régimen»; «comprendidos», flexión |
| 64 | `ctacte::1.3.1.3` | e1 Obligacion, descripcion | coincidencia legítima | «estado civil» y «titulares»: flexión |
| 65 | `ctacte::1.3.2.3` | e1 Obligacion, descripcion | coincidencia legítima | «personas jurídicas titulares de cuentas corrientes», de la norma |
| 66 | `ctacte::1.3.2.3` | e1 Obligacion, label | coincidencia legítima | «contrato o estatuto, objeto social y», de la norma |
| 67 | `ctacte::3.2.1.3` | e1 Operacion, label | coincidencia legítima | «carecen de valor como cheques»: flexión |
| 68 | `ctacte::3.2.1.3` | e3 Restriccion, descripcion | coincidencia legítima | «de valor como cheque», de la norma |
| 69 | `ctacte::3.2.1.4` | e3 Restriccion, label | copia real | ausente «carencia» (nominalización de «carecen») |
| 70 | `ctacte::3.2.1.6` | e2 Restriccion, descripcion | coincidencia legítima | ídem caso 67 |
| 71 | `ctacte::3.2.1.6` | e2 Restriccion, label | copia real | ídem caso 69 |
| 72 | `ctacte::3.2.1::intro` | e1 Restriccion, label | copia real | ídem caso 69 |
| 73 | `ctacte::5.1.2.1` | e2 Condicion, label | coincidencia legítima | «a persona determinada sin cláusula “no a la orden”», de la norma |
| 74 | `ctacte::5.1.2.3` | e1 Operacion, label | coincidencia legítima | «a favor de persona determinada», de la norma |
| 75 | `ctacte::6.4.6.5` | e4 Excepcion, descripcion | coincidencia legítima | «los rechazos de los puntos 6.4.6.2. a 6.4.6.4.», de la norma |
| 76 | `ctacte::6.4.7::cierre` | e1 Condicion, descripcion | coincidencia legítima | «efectuadas con sujeción a», de la norma |
| 77 | `ctacte::6.4.7::cierre` | e2 Operacion, label | copia real | ausente «modificación» (la norma dice «modificar») |
| 78 | `ctacte::6.4.7::intro` | e1 Condicion, label | copia real | ausente «necesidad» (la norma dice «sea necesario») |
| 79 | `ctacte::8.2.1.2` | e1 Definicion, descripcion | coincidencia legítima | «inclusión en la Central de», de la norma |
| 80 | `ctacte::8.2.2.1` | e1 Condicion, descripcion | coincidencia legítima | «falta de pago de la multa», de la norma |
| 81 | `lingob::2.3.2.2` | e1 Obligacion, descripcion | coincidencia legítima | «el Directorio se asegurará de que», de la norma |
| 82 | `lingob::2.3::intro` | e1 Obligacion, descripcion | copia real | ausente «recomendación»: «una recomendación de buena práctica» es la lectura de la nota |
| 83 | `lingob::6.2.4.9` | e1 Condicion, descripcion | coincidencia legítima | «esté condicionado al resultado de», flexión |
| 84 | `polcre::2.1.8` | e1 Operacion, descripcion | coincidencia legítima | «préstamos de organismos multilaterales de crédito», de la norma |
| 85 | `pagjub::1.6` | e1 Potestad, descripcion | coincidencia legítima | «para los aspectos no previstos», de la norma |
| 86 | `pagjub::2.1` | e2 Condicion, descripcion | copia real | ausente «obligación»: nominalización de la nota |
