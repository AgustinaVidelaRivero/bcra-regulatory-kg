# U-REEXT-T0, T2: criterio de objeción de E3 a una omisión `meta_normativo`, declarado antes de contar

Escrito el 05/10/2026, con la corrida de T2 en curso y antes de leer ninguna salida de E3 de esa corrida (mandato
firmado en e2027dd, T2: «El criterio con que se cuenta una objeción se declara antes de contar»). No cambia después
de contar; si hiciera falta otro, se agrega aparte, fechado, y se cuentan los dos.

**Qué se cuenta.** Por unidad, las omisiones de categoría `meta_normativo` de la salida de E1 que vio la primera
verificación de E3 (la validación del primer intento, `vistos_por_e3`), y los faltantes de esa primera verificación.

**Normalización de un texto.** NFD sin diacríticos, minúsculas, el guion de corte de línea («-\n») quitado, comillas
tipográficas a rectas, todo lo que no es letra ni dígito a espacio, espacios colapsados. Palabras = la secuencia que
queda, separada por espacios.

**Objeción.** Una omisión `meta_normativo` cuenta como objetada por E3 si algún faltante de la primera verificación de
E3 de su unidad (cualquier tipo y severidad) tiene una `cita_textual_del_fuente` que, normalizada:
1. contiene el tramo normalizado de la omisión, o está contenida en él; o
2. comparte con él una secuencia de al menos 8 palabras seguidas.
Una omisión con tramo de menos de 8 palabras solo cuenta por 1.

**Recuperación por el reintento.** Una omisión objetada cuenta como recuperada si la unidad tuvo al menos un reintento
del ratchet de E3 y, en la extracción final de la unidad (la que entra al E2 r2):
1. ninguna omisión `meta_normativo` cumple, con el tramo de la omitida, el mismo criterio de solapamiento; y
2. algún nodo de la unidad (label o descripción) comparte con el tramo una secuencia de al menos 8 palabras seguidas o
   lo contiene, normalizado (con un tramo de menos de 8 palabras, solo si lo contiene).
Las que cumplen 1 y no 2 se cuentan aparte («dejó de declararse sin que aparezca el contenido»).

**Límite declarado.** El criterio es textual: un faltante que describe la omisión con otras palabras, sin citar su
tramo, no cuenta como objeción; un nodo que parafrasea el tramo sin 8 palabras seguidas en común no cuenta como
recuperación. Las dos cifras son cotas inferiores.
