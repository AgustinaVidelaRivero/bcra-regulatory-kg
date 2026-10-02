# U-R2-CODIGO — reglas (a) a (i) de las remisiones, tras el freno posterior a R3

Decisiones de la autora sobre el freno posterior a R3 (`r3_ajustes_freno.md`), con la corrección posterior de (e) y
(g), aplicadas solo en el perfil r2. La cadena r1 sigue reproduciendo lo sellado. USD 0, sin API ni Neo4j. Los números
salen de `r3d_remisiones.py`, `r3_perdidas_remisiones.py` y `reglas_remisiones_censos.py` con `--e0-r2` sobre la
salida de e0-r2 de la tanda 0, en doble corrida idéntica. Los archivos están en el paquete de revisión.

## Qué hace cada regla y dónde

Todo está en `corpus_v2/r1_referencias.py`, sección «Detector del perfil r2» (`detectar_menciones_r2`). Con las nueve
reglas apagadas da exactamente `detectar_menciones` de la cadena r1. Lo controlo en los 9.324 chunks de la partición, y
con `--reglas ""` se reproduce el desglose del freno anterior (119, 132, 128 y 245, con las mismas causas).

- (a) `normalizar_e0(…, tolerar_linea_suelta=True)`: deja fuera del texto que se lee una línea de uno o dos caracteres
  alfanuméricos que queda entre una línea terminada en «punto(s)» o «apartado(s)» y una que empieza con un número. La
  evidencia sale del original y conserva esa línea. Que la «i» de `cap::7.1` sea un subíndice queda NO VERIFICADO
  contra el PDF.
- (b) El ensamblado recibe la salida de e0-r2 con `ensamblar_tanda0.py --e0-r2 <dir>`, alias del `--tablas-e0-r2` de
  R3. Con ella, el texto de cada procedencia sale de ese chunk (`chunks_e0_r2`). Los ids coinciden 1 a 1 con los de la
  E0 legada en los diez TOs: 1.801 procedencias en desarrollo y 2.477 en diez, ninguna con texto legado.
- (c) Se admite un paréntesis entre los elementos de una lista o de un rango (`_re_puntos_r2`). Lo que está dentro del
  paréntesis no entra en la lista.
- (d) De la ventana de una norma se toma solo la mención de puntos más cercana. Una mención seguida de otra mención de
  puntos no queda tomada por la norma que viene después.
- (e) Anáfora de la norma (`RE_ANAFORA_NORMA`). Cubre las siete formas de la lista («de las citadas normas», «de dichas
  normas», «del citado ordenamiento», «del citado TO», «dicho TO», «de la citada norma», «de las citadas
  disposiciones»), las de R3 («de dicho/ese/este ordenamiento o texto ordenado») y variantes («de las normas
  citadas»). Resuelve a la última norma nombrada antes en el texto del punto. Si no hay ninguna: «anáfora sin
  antecedente». Si la hay y está fuera del inventario: «norma fuera del inventario». Nunca es interna. Con (e), la
  ventana de la anáfora toma también las secciones, como la de una norma nombrada: «la Sección 4. de dichas normas»
  resuelve a la sección y no al TO entero. Una mención de puntos seguida de «de las presentes normas», «de las
  presentes disposiciones» o «del presente régimen» (`RE_PROPIO_TO`) es interna aunque después se nombre otra norma.
- (f) «Apartado» con número de punto es forma de cita.
- (g) `resolver_norma_r2`: la norma resuelve a un TO si el título del inventario, normalizado, es prefijo del texto
  capturado normalizado y termina en límite de palabra. Si calzan varios, gana el más largo (en los 157, «garantias» es
  prefijo de garopt y «sistema nacional de pagos - transferencias» de snp_tr_nc). El texto capturado es lo que está
  entre comillas (incluidas ‘ ’) o, sin comillas, todo lo que toma el patrón. Títulos: `inventario_tos.csv`, más
  `inventario_resumen.json` para los cinco de desarrollo; 157, sin repetidos. «TO sobre», «texto ordenado sobre» y
  «normas sobre» nombran la norma igual (selftest T7g), y «texto ordenado de las normas sobre “X”» es una sola cita a
  X.
- (h) «Este punto», «el presente punto» y «dicho punto» sin número quedan en el registro con causa «anáfora sin
  número», sin arista.
- (i) Cita del texto que el chunk hereda de otra unidad: cada unidad citada va a los nodos de la procedencia cuyo
  texto guardado la nombra (`nombra_unidad`, límite estricto: «3.5» no se nombra en «3.5.1.6»). La evidencia es
  literal del tramo heredado y la procedencia es la del bloque heredado (`herencia_<tipo>`, punto del bloque).

## Diferencia entre la (g) anterior y la nueva

La (g) anterior tomaba como nombre sin comillas lo previo a la primera coma, raya, « -», paréntesis o dos puntos.
Resolvía con el título completo o con el comienzo de un único título. Comparación mención por mención, con todas las
reglas: `comparar_g.py` (paquete), la versión anterior desde una copia de `r1_referencias.py`.
- Desarrollo: ningún cambio.
- Diez: `polcre::9.1` y `polcre::9.2` pasan de irresolubles a `polcre` («TO sobre Política de Crédito en forma
  individual», «… sobre base consolidada mensual»).
- Partición (informativo): 45 citas pasan a resueltas (nombres sin comillas seguidos de texto corrido: cap 8, autenf
  4, cla 3, supcon 3, polcre 3…). 41 pasan a irresolubles: el texto capturado es más corto que el título, así que el
  título no puede ser su prefijo. Son incuca 8, rdbcra 8, lavdin 4, cajasc 3, cap 3, cryl 2, rrci 2, depaho 2 y uno
  en micemp, opefci, seggar, pro, ccbcra, fimipyme, gracre, pognme y rmgcti. Por lectura de la muestra, el patrón corta
  la captura en el punto de «… técnicas. Criterios aplicables», en el tope de 90 caracteres o en «(Ley 26.173)», y
  hay citas con el nombre abreviado («Capitales Mínimos»). Ninguna de las 41 está en los diez TOs con su TO en el
  inventario.

## Aristas y citas antes y después de cada regla (acumuladas)

Cita resuelta = (chunk de origen, tramo, unidad), §5 de la enmienda 2. Fuente: `r3d_remisiones.py`, `G_reglas_*`.

| paso | desarrollo: aristas / resueltas / irresolubles | diez: aristas / resueltas / irresolubles |
|---|---|---|
| R3 | 12.647 / 1.203 / 354 | 13.807 / 1.363 / 432 |
| +a | 12.654 / 1.205 / 354 | 13.814 / 1.365 / 432 |
| +b | 12.658 / 1.207 / 355 | 13.818 / 1.367 / 433 |
| +c | 12.664 / 1.209 / 355 | 13.824 / 1.369 / 433 |
| +d | 12.604 / 1.210 / 354 | 13.764 / 1.370 / 432 |
| +e | 12.463 / 1.207 / 356 | 13.629 / 1.368 / 433 |
| +f | 12.463 / 1.207 / 356 | 13.633 / 1.369 / 433 |
| +g | 12.459 / 1.204 / 358 | 13.624 / 1.365 / 436 |
| +h | 12.459 / 1.204 / 400 | 13.624 / 1.365 / 484 |
| +i | 12.581 / 1.300 / 417 | 13.746 / 1.464 / 503 |

En cada uno de los 20 pasos, todas las citas resueltas tienen la evidencia como tramo literal del texto de E0 de su
chunk, y la unidad de destino sale de la evidencia: 0 fuera (`en_el_texto`). No hay remisiones que no estén en el
texto.

Lectura por regla, en desarrollo. Diez agrega lo que se indica.
- a: +2 citas, `cap::7.1::intro` → `cap::7.1.2` y `cap::8.2.2.3` → `cap::8.3.5`.
- b: +1, `cap::6.2.1.1` → `cap::2.12.3.1`. Dos citas irresolubles cambian: ver «Límites declarados».
- c: +2, `ext::7.9.1.3` → `ext::3.6.1.4` y `ext::3.6.1.5`.
- d: +1, `cla::5.1.2.3` → `cla::3.7`. −1, `ric::3.1.3` → `cap::3.1.4`, que era falsa: el 3.1.4 es el del modelo de
  información de ric, nombrado antes de otro punto (−62 pares).
- e: +2, `ric::3.1.2` → `cap::4.1.1` y `ric::3.1.6` → `cap::4.2.1.3`; en diez, además, `ctacte::1.3.1.7` →
  `docvig::S4`. −4 remisiones internas falsas (−154 pares):
  - `cap::2.1` → `cap::3.2.4` («del citado ordenamiento»: Financiamiento al Sector Público no Financiero);
  - `ric::10.1.2` → `ric::1.2` (anáfora sin antecedente: la norma está en el punto anterior);
  - `ric::12.4` → `ric::6.2` y `ric::S2` → `ric::6.2` («Supervisión consolidada»).
- f: en diez, +1, `ctacte::12.2.3.1` → `ctacte::12.2.3.2`.
- g: pasan de resueltas a irresolubles `cap::2.1` (2 citas), `cap::8.5::cierre` y `ric::9.1.1`. Citan «Incumplimientos de
  capitales mínimos y relaciones técnicas», otra norma fuera del inventario, que la cadena r1 resolvía a cap por
  subcadena: es una corrección. En diez, además, `pagjub::2.2` cita el TO propio por su nombre completo y el título del
  inventario está abreviado («seg. soc.», «Adm.»), así que el título no es prefijo del nombre: es una pérdida, por la
  regla. Ninguna cita pasa de irresoluble a resuelta ni cambia de TO.
- h: +42 citas «anáfora sin número» en desarrollo y +48 en diez, sin arista.
- i: +22 citas resueltas y +122 aristas. De 2.870 menciones en texto heredado, 91 tienen algún nodo que nombra la
  unidad. Muestra leída: «14.2.1. En el marco de lo dispuesto en los puntos 3.3., 3.5., 3.6. y 10.3.2.» llega a los
  nodos de 14.2.1.2, 14.2.1.4 y 14.2.1.10 que nombran esos puntos.

## Formas de la (e) en los diez TOs

Conteo en la E0 congelada (`salida_tanda0`, texto propio de cada chunk, `reglas_remisiones_censos.py`, clave `E`), y
cómo queda cada cita en diez (`G_reglas_diez.e_formas`):
- «de las citadas normas», 5:
  - `ric::3.1.2` → `cap::4.1.1`;
  - `cap::2.1` (Sección 9.), `cap::8.4.1.13` (punto 2.6., Previsiones mínimas) y `ric::10.1.1` (sección 3., Ratio de
    apalancamiento): «norma fuera del inventario»;
  - `ric::10.1.2` (punto 1.2.): «anáfora sin antecedente».
- «de dichas normas», 2: `ctacte::1.3.1.7` → `docvig::S4`; `cla::3.3.8` (punto 1.5.5., Gestión crediticia): fuera del
  inventario.
- «del citado ordenamiento», 1: `cap::2.1` (punto 3.2.4.), fuera del inventario.
- «de las citadas disposiciones», 1: `ric::3.1.6` → `cap::4.2.1.3`.
- «del citado TO», «dicho TO» y «de la citada norma»: 0. En la partición hay 3, 0 y 1.
- Variante «de las normas citadas», 3: `ric::12.4` (2) y `ric::S2`, «Supervisión consolidada», fuera del inventario.
  De R3, «de dicho ordenamiento», 1: `ric::3.1.6` → `cap::4.2.1.2`.
- Propio TO: «de las presentes normas» 1, «de las presentes disposiciones» 3 y «del presente régimen» 2 en la E0. Solo
  una sigue a una mención de puntos: `ric::4.3::intro`, «los puntos 4.1.1.1. a 4.1.1.8. del presente régimen», que
  queda interna (8 puntos).
- «De estas normas» (10 en la E0) no está en la lista y el detector no la trata. Por eso sigue la pérdida de
  `cap::8.5::cierre`, más abajo.

Citas de norma sin comillas, sobre el texto propio de la E0 congelada: 60 de 248 en los diez TOs y 324 de 1.464 en la
partición. La corrección hablaba de unas 62 y 339; los míos salen de `RE_NORMA_R2` sin comilla de apertura.

## Error propio, con su causa

En el freno posterior a R3 dije que la regla firmada creaba `ric::9.1.1` → `cap::S2` como «destino nuevo falso». No es
así: el mismo punto cita también «la Sección 2. de las normas sobre “Capitales mínimos de las entidades financieras”»,
y esa remisión es real. Lo falso era que la cita a «Incumplimientos…» se resolviera a cap. Leí la primera cita del
punto y no las demás. La arista `ric::9.1.1` → `cap::S2` queda, con la evidencia de la cita real (`G_reglas_*.controles`).

## Desglose A y B recomputado (`r3_perdidas_remisiones.py --e0-r2`)

| veredicto | A desarrollo | A diez | A r1 | B desarrollo |
|---|--:|--:|--:|--:|
| queda desde otro punto | 47 / 9 | 47 / 9 | 13 / 2 | 47 / 9 |
| corrección | 18 / 3 | 27 / 4 | 36 / 5 | 41 / 7 |
| no es una cita del texto | 4 / 1 | 4 / 1 | 22 / 7 | 13 / 2 |
| límite declarado (h) | 5 / 1 | 5 / 1 | — | 5 / 1 |
| **pérdida real, declarada** | **1 / 1** | **1 / 1** | **1 / 1** | **1 / 1** |
| total de pares perdidos | 75 | 84 | 72 | 107 |

Pares / citas. Referencias: 4.242, 4.819 y 5.645 aristas selladas, y 7.929 pares de la paráfrasis (7.940 con cada
procedencia y `termino`, también 107).

La única pérdida real es `cap::8.5::cierre` → `cap::1.4`: «lo previsto por el punto 1.4. de estas normas y la Sección
1. de las normas sobre “Incumplimientos de capitales mínimos…”». El 1.4 es de cap («de estas normas»). La regla (d)
solo mira puntos, y la mención más cercana a la norma es una sección, así que el 1.4 queda atribuido a Incumplimientos,
que con (g) está fuera del inventario. La cadena r1 acertaba por la subcadena. Propuesta, no implementada: que «de
estas normas» sea marca del propio TO, como «de las presentes normas», o que en (d) cuente también una mención de
sección.

## Límites declarados

- (a): el subíndice que E0 extrae como línea suelta no se corrige en E0.
- (b): con la tabla serializada aparecen dos citas irresolubles nuevas, sin arista.
  - `ric::4.3.3`: una celda de varias líneas queda en dos filas («“Ca-» / «Fila 10: col4 = pitales mínimos…»), el
    nombre de la norma se lee partido y la cita a `cap::2.6.3.1` (inexistente en la E0 de cap) queda «norma fuera del
    inventario».
  - `ric::6.2`: la fila «… observen los requisitos del punto 8.3.3. no incluidos…» deja el número junto a «punto», y
    la cita se lee como interna a `ric::8.3.3`, inexistente en la E0 de ric. El punto sin norma nombrada se trata
    como interno desde la cadena r1.
- (g): el título tiene que entrar entero en el texto capturado. Las citas cuyo patrón corta antes, o con el nombre
  abreviado, quedan irresolubles: `pagjub::2.2` en diez y las 41 de la partición de arriba. En la partición, además,
  17 de 1.491 menciones tienen un título contenido en el nombre pero no al comienzo: un artículo antes de las comillas
  («sobre la “Relación para los activos inmovilizados…”») o celdas de tabla pegadas («n1 “Capitales mínimos…»). La
  muestra está en `censos`, `ejemplos_titulo_contenido_que_g_no_toma`.
- (h): el registro cuenta la anáfora sin número y no crea remisión.
- (i): los nodos que no nombran la unidad no reciben la arista. Informativo: con el límite estricto de (i), la
  atribución D1 del punto propio daría otros nodos en 27 menciones de desarrollo y 30 de diez. D1 sigue como está
  firmada (`_contiene_unidad`).

## Mediciones informativas (`reglas_remisiones_censos.py`)

- Censo de (f) en los diez TOs, sobre el texto de e0-r2: «inciso», «acápite», «ítem» y «numeral» seguidos de un
  número con puntos aparecen 0 veces; «punto», 1.107; «apartado», 1. Sin casos no hay muestra, y la lista de formas
  queda en «punto» y «apartado».
- Partición del corpus escalado: 152 TOs y 9.324 chunks. Citas cambiadas por paso acumulado: a 1; c 13; d 52; e 71;
  f 13; g 1.548, porque antes de (g) la cadena r1 resuelve con el inventario de cinco TOs; h 79. Con los mismos 157
  títulos, (g) resuelve 1.166 de 1.491 menciones de norma. No mido (b), porque la partición no tiene salida de e0-r2
  (agregado 9), ni (i), porque no hay grafo.
