# U-UMBRAL · U2 — Muestra de `limita`, trazas y dimensionamientos

Mandato: `docs/mandatos/UUMBRAL_investigacion.md` (firmado el 30/09/2026), con las precisiones de la autora al aprobar U1 (`e81ed69`). USD 0: sin API y sin Neo4j. EV2 y las trazas son material de desarrollo: la medición 5 es un diagnóstico, no un resultado (principio 7).

Comando que reproduce este archivo, `u2_muestra_trazas.json` y `muestra_limita_30.csv`:

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u2.py
```

## Entradas

| Grafo | Ruta | sha256 |
|---|---|---|
| KG-Tanda0-Desarrollo-r1 | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` | `eab2fdd01dec4dad…` |
| KG-Reextraído-r1 | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d…` |
| KG-Tanda0-Diez-r1 | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json` | `dd42d6d9c0c8379d…` |

Preguntas: `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` (sha256 `1d58733699c325c9…`). Trazas base: `data/experiment/ev2_tanda0/trazas/ev2_c3_dev_mem/` y `data/experiment/ev2_tanda0/trazas/ev2_c4_dev_neo4j/` (40 cada una; sha256 del conjunto, concatenando los sha de los archivos en orden: C3 `00b236886ecab744…`, C4 `5f890dd38c01888a…`). E0: `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0`.

## Declaraciones previas a la medición

- **D-SORTEO.** Medición 4. Población: aristas con relation = "limita" de KG-Tanda0-Desarrollo-r1, en el orden de `edges` del kg.json, ordenadas con sort estable por la clave (source, target). Se comprueba que no hay pares (source, target) repetidos. Sorteo: random.Random(20260930).sample(range(N), 30) sobre los índices de esa lista ordenada, sin reemplazo (Python del .venv del repo, 3.10). Las filas de la planilla van en el orden del sorteo, con su índice en la lista ordenada. Texto de E0: el `texto` propio y la `herencia` de cada chunk_id de las procedencias de la arista, en orden de aparición.
- **D-C14.** Regex de cuantía: la de U1 (comando [c14] del tablero tal como está escrito), sin cambios, importada de u_umbral_u1.VARIANTES["c14"].
- **D-C14PAR.** Variante con nombre propio «c14_par», declarada antes de aplicarla (precisión 1 de la autora): idéntica a c14 salvo en el plazo, que admite entre el número y la unidad un número entre paréntesis, en cifras o en letras de la lista LETRAS de U1 («2 (dos) años», «diez (10) años»). Sin paréntesis, exige el mismo espacio que c14. c14_eur de U1 se reporta solo como variante informativa.
- **D-CRIT.** Medición 5. Un criterio de preguntas_ev2_fidelidad.json tiene cuantía según una regex si la regex encuentra algo en su `criterio` o en su `cita_textual`. El diagnóstico se corre sobre los criterios con cuantía según c14 o según c14_par; cada fila dice con cuál de las dos (o las dos).
- **D-VALOR.** Valor de un criterio: los triples del prototipo P6 de U1 (extraer_p6) sobre `criterio` y sobre `cita_textual` (unión), más los «literales»: los tramos que encuentra c14_par en esos dos textos y que tienen al menos un dígito, normalizados con D-N1. Un criterio con cuantía sin triples ni literales queda como «valor no extraíble» y no se diagnostica.
- **D-CONTIENE.** Un texto contiene el valor si sus triples P6 comparten al menos uno con los del criterio, o si algún literal del criterio es subcadena del texto normalizado con D-N1. Un nodo contiene el valor si lo contiene su `descripcion`, su `umbral` o su `plazo`. Se excluyen TextoOrdenado, Sujeto y Comunicacion.
- **D-ANCLA.** Un nodo está en el ancla de la pregunta («to:punto») si alguna de sus procedencias tiene ese `to` y un `punto` igual al del ancla o que empieza con el del ancla seguido de «.» (puntos descendientes).
- **D-RECIBIDO.** En una traza base (C3, `ev2_c3_dev_mem`; C4, `ev2_c4_dev_neo4j`), un nodo fue recibido si su id aparece en algún resultado de `buscar_nodos`, como vecino en algún resultado de `ver_vecinos` (salientes o entrantes) o como id de una salida de `ver_nodo` sin error (`steps_full`).
- **D-VISIBLE.** El valor fue visible para el agente desde un nodo del ancla si ese nodo aparece en un resultado de `buscar_nodos` cuyo `label` o `resumen_propiedades` contiene el valor (D-CONTIENE), o como vecino en `ver_vecinos` con `vecino_label` que lo contiene, o si el agente le hizo `ver_nodo` (la salida trae las properties completas).
- **D-RESPUESTA.** El valor está en la respuesta si `trace.final_json.respuesta` (o `trace.final_raw` si no hay final_json) lo contiene según D-CONTIENE. Es un control léxico: no dice si la respuesta cumple el criterio.
- **D-CLASE.** Cadena, en orden: «grafo» si ningún nodo del ancla contiene el valor; «búsqueda» si hay nodos del ancla con el valor y el agente no recibió ninguno; «navegación» si recibió alguno pero el valor no le fue visible; «visible» en otro caso. Cruce con D-RESPUESTA: visible y en la respuesta → «llega»; visible y no en la respuesta → «generación»; grafo, búsqueda o navegación con el valor en la respuesta → «en la respuesta por otra vía»; sin el valor en la respuesta → la clase de la cadena. Es un diagnóstico por reglas sobre material de desarrollo, no un resultado sobre EV2.
- **D-TABLA-1.2.** Demostración puntual (precisión 2.ii), no un verificador general: para cada Restriccion con umbral anclada en cap::1.2, la clase del sujeto se toma de su descripción («restantes entidades» → columna «Restantes entidades», si no «bancos» → columna «Bancos»), y el monto esperado es el de esa columna en la tabla de e0_tablas asignada a cap::1.2 (cap::tabla000: fila de encabezados y última fila de cifras). Se compara con el monto del umbral (primer número con puntos o dígitos del campo).
- **D-ESTIM.** Dimensionamiento del llenado por un modelo (decisión 6): ESTIMACIÓN NO VERIFICADA. Subconjuntos: nodos de los cuatro tipos con cuantía según c14, y de ellos los sin campo. Una llamada por chunk distinto del subconjunto. Tokens de entrada variables = (caracteres del texto propio y heredado de cada chunk + caracteres de las descripciones del subconjunto) / 3,471 (ratio de prosa de INFORME_E1_FASEA.md:141). Supuestos NO VERIFICADOS: prompt fijo de 1.500 tokens (escritura de caché en la primera llamada, lectura en las demás) y 60 tokens de salida por nodo. Tarifas USD/MTok: entrada 1,00; salida 5,00; escritura de caché 1,25; lectura 0,10 (runner_faseB_e1.py:41). Referencia aparte: USD 0,0166 por unidad de E1+E3 (docs/laudo_release_r2_pipeline.md:46) por el número de chunks.
- **D-REL-DIM.** Dimensionamiento de los umbrales relacionales (precisión 2.iv): nodos de los cuatro tipos con cuantía según c14 en los que dispara D-REL o A-REL de U1 (u_umbral_u1.RE_REL) o la regla de «equivalente»; se cuentan por forma (base con «de/del/sobre», «veces» + artículo, «equivalente» antes de un monto), por tipo, con y sin campo.
- **D-COB.** Cobertura de aristas de los demás portadores de valor (eje de esquema), por grafo: Obligacion con `plazo` y sin arista saliente `regula` ni `condiciona` (las Obligacion→Operacion del prefijo); Obligacion con cuantía según c14, sin campo, y sin esas aristas; Excepcion con cuantía según c14 y sin `exceptua` ni `exceptua_obligacion` saliente. Declarada antes de computarla, después de la corrida de prueba del resto de U2.

### Agregados tras la corrida de prueba (rotulados como posteriores)

- **A-P6PAR.** En la corrida de prueba, EV2F-015#3 («180 días corridos», ancla ext:3.13.1) salió «grafo», pero el ancla tiene el nodo Condicion_plazo_minimo_180_dias… con «180 (ciento ochenta) días corridos»: P6 no reconoce un número en letras de varias palabras entre paréntesis. En U2, y solo para el valor de la medición 5, se suman a los triples P6 dos formas de plazo: cifra seguida de paréntesis sin dígitos (hasta 40 caracteres) y unidad («180 (ciento ochenta) días»), y cifra entre paréntesis seguida de unidad («ciento ochenta (180) días»). El prototipo P6 de U1 no se cambia.

## Medición 4 — Muestra de 30 aristas `limita`

Población: 284 aristas `limita` de KG-Tanda0-Desarrollo-r1; pares (source, target) repetidos: 0. Semilla 20260930, n = 30, Python 3.10.13. Índices sorteados (en la lista ordenada): [236, 207, 113, 157, 256, 214, 11, 25, 141, 239, 220, 13, 20, 254, 43, 90, 272, 178, 39, 192, 164, 33, 206, 23, 124, 3, 258, 142, 227, 262].

Planilla `muestra_limita_30.csv`: 30 filas más la de encabezados; sha256 `8e9818173100ac880c7bdc34121a4f4e66916e42b16636421f5e4e993512b2a9`. La columna «el destino es el objeto del tope (sí / no / no decidible)» va vacía. Nadie la lee en esta unidad; quién lee lo decide la autora (checklist P15 y Q12).

## Medición 5 — Dónde se pierde el valor en las trazas (diagnóstico)

Criterios: 164 en 40 preguntas. Con cuantía según c14: **8** (en 7 preguntas); según c14_par: 8 (0 solo por c14_par). Informativo, c14_eur: 8 (0 solo por c14_eur).

| Criterios | Celda | llega | generación | navegación | búsqueda | grafo | en la respuesta por otra vía | valor no extraíble | Total |
|---|---|---|---|---|---|---|---|---|---|
| c14 | C3 | 3 | 1 | 0 | 4 | 0 | 0 | 0 | 8 |
| c14 | C4 | 3 | 0 | 1 | 4 | 0 | 0 | 0 | 8 |
| solo c14_par | C3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| solo c14_par | C4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

La misma tabla sin A-P6PAR (solo con lo declarado antes de la corrida de prueba):

| Criterios | Celda | llega | generación | navegación | búsqueda | grafo | en la respuesta por otra vía | valor no extraíble | Total |
|---|---|---|---|---|---|---|---|---|---|
| c14 | C3 | 3 | 1 | 0 | 3 | 1 | 0 | 0 | 8 |
| c14 | C4 | 3 | 0 | 1 | 3 | 1 | 0 | 0 | 8 |
| solo c14_par | C3 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
| solo c14_par | C4 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

Por criterio (valor = triples P6 o literales; «ancla» = nodos del ancla con el valor; fuera = nodos con el valor fuera del ancla):

| Criterio | Ancla | Regex | Valor | Nodos ancla | Fuera | C3 | C4 | C3 / C4 sin A-P6PAR |
|---|---|---|---|---|---|---|---|---|
| EV2F-004#3 | ext:2.6 | c14 | porcentaje:30 % | 1 | 13 | búsqueda | llega | búsqueda / llega |
| EV2F-011#1 | ext:5.8 | c14 | plazo:2 día | 3 | 3 | búsqueda | búsqueda | búsqueda / búsqueda |
| EV2F-014#3 | ext:13.5 | c14 | plazo:15 día | 2 | 18 | llega | llega | llega / llega |
| EV2F-015#3 | ext:3.13.1 | c14 | plazo:180 día | 1 | 29 | búsqueda | búsqueda | grafo / grafo |
| EV2F-022#0 | cap:6.11 | c14 | porcentaje:25 % | 3 | 13 | llega | navegación | llega / navegación |
| EV2F-022#2 | cap:6.11 | c14 | porcentaje:3 % | 1 | 7 | búsqueda | búsqueda | búsqueda / búsqueda |
| EV2F-023#3 | cap:8.3.2 | c14 | plazo:5 año | 2 | 9 | generación | búsqueda | generación / búsqueda |
| EV2F-039#3 | pro:2.5 | c14 | plazo:30 día | 1 | 15 | llega | llega | llega / llega |

## Demostración puntual: `cap::1.2` contra el parser de tablas (D-TABLA-1.2)

Tabla asignada: `cap::tabla000`; encabezados ['bancos', 'restantes entidades (salvo cajas de crédito cooperativas)']; cifras ['5.000', '2.500'].

| Restriccion | Clase según la descripción | umbral | Monto en la tabla | Coincide |
|---|---|---|---|---|
| `Restriccion_las_restantes_entidades_salvo_bancos_y_cajas_de_…` | restantes | 5.000 millones de pesos | 2.500 | NO |
| `Restriccion_los_bancos_salvo_cajas_de_credito_cooperativas_d…` | bancos | 2.500 millones de pesos | 5.000 | NO |

## Dimensionamiento de los umbrales relacionales (D-REL-DIM)

| Grafo | Tipo | Con cuantía (c14) | Relacional | Relacional con campo | Relacional sin campo | Forma: % o veces + de/del/sobre | Forma: veces + artículo | Forma: equivalente + monto |
|---|---|---|---|---|---|---|---|---|
| desarrollo | Restriccion | 258 | 57 | 51 | 6 | 43 | 2 | 12 |
| desarrollo | Condicion | 134 | 31 | 0 | 31 | 20 | 3 | 8 |
| desarrollo | Obligacion | 170 | 31 | 9 | 22 | 27 | 1 | 3 |
| desarrollo | Excepcion | 43 | 3 | 0 | 3 | 3 | 1 | 0 |
| desarrollo | **total** | 605 | 122 | 60 | 62 | 93 | 7 | 23 |
| r1 | Restriccion | 361 | 86 | 75 | 11 | 59 | 8 | 19 |
| r1 | Obligacion | 228 | 44 | 16 | 28 | 40 | 4 | 2 |
| r1 | Excepcion | 49 | 5 | 0 | 5 | 4 | 0 | 1 |
| r1 | **total** | 638 | 135 | 91 | 44 | 103 | 12 | 22 |
| diez | Restriccion | 280 | 62 | 56 | 6 | 47 | 3 | 12 |
| diez | Condicion | 156 | 32 | 0 | 32 | 21 | 3 | 8 |
| diez | Obligacion | 202 | 31 | 9 | 22 | 27 | 1 | 3 |
| diez | Excepcion | 44 | 3 | 0 | 3 | 3 | 1 | 0 |
| diez | **total** | 682 | 128 | 65 | 63 | 98 | 8 | 23 |

Las formas no son excluyentes: un nodo puede tener más de una.

## Cobertura de aristas de los demás portadores de valor (D-COB)

| Grafo | Obligacion con plazo | …sin regula ni condiciona | Obligacion con cuantía sin campo | …sin regula ni condiciona | Excepcion con cuantía | …sin exceptua(_obligacion) |
|---|---|---|---|---|---|---|
| desarrollo | 248 | 170 | 76 | 51 | 43 | 21 |
| r1 | 288 | 135 | 106 | 38 | 49 | 10 |
| diez | 348 | 251 | 87 | 56 | 44 | 22 |

## Dimensionamiento del llenado por un modelo (D-ESTIM) — ESTIMACIÓN NO VERIFICADA

| Grafo | Subconjunto | Nodos | Llamadas (chunks) | Tokens de entrada variables | Tokens de salida | USD estimado (NO VERIFICADO) | Referencia E1+E3 × chunks (USD) |
|---|---|---|---|---|---|---|---|
| desarrollo | con_cuantia | 605 | 310 | 227492 | 36300 | 0.4572 | 5.146 |
| desarrollo | con_cuantia_sin_campo | 287 | 169 | 133290 | 17220 | 0.2465 | 2.8054 |
| diez | con_cuantia | 682 | 364 | 245758 | 40920 | 0.5067 | 6.0424 |
| diez | con_cuantia_sin_campo | 323 | 195 | 142724 | 19380 | 0.2706 | 3.237 |

Supuestos NO VERIFICADOS: prompt fijo de 1.500 tokens y 60 tokens de salida por nodo. La fórmula y las tarifas están en D-ESTIM.

