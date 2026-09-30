# U-UMBRAL · U1 — Mediciones sobre los grafos y E0

Mandato: `docs/mandatos/UUMBRAL_investigacion.md` (firmado el 30/09/2026). USD 0: sin API y sin Neo4j. Material de desarrollo: nada de esto es un resultado sobre EV2 (principio 7). Esta etapa mide; no propone ni decide.

Comando que reproduce todo este archivo y `u1_mediciones.json`:

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_umbral/u_umbral_u1.py
```

## Entradas y sellos

| Grafo | Ruta | sha256 |
|---|---|---|
| KG-Tanda0-Desarrollo-r1 | `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` | `eab2fdd01dec4dad…` |
| KG-Reextraído-r1 | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d…` |
| KG-Tanda0-Diez-r1 | `data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/kg.json` | `dd42d6d9c0c8379d…` |

E0: `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_<to>.json` de los diez TOs (2434 chunks). Para los cinco de desarrollo, idéntico byte a byte a `data/experiment/reextraccion_v2/e0_chunking/salida_enm01` (comprobado: True). PDFs del manifiesto `data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json`, sha256 comprobado contra `sha256_pdf`: True. `e0_tablas.py` importado sin editar (sha256 `ab300a22b41f99e8…`). Resumen de `buscar_nodos`: `data/experiment/evaluacion/harness.py:110` (`max_len=160`, comprobado en el fuente: True).

## Declaraciones previas a la medición

- **D-N1.** Normalización de la medición 1: NFC, después minúsculas (str.lower), después toda secuencia de espacios en blanco (incluidos los saltos de línea de E0) a un solo espacio, y strip. Nada más: no se quitan tildes, puntuación ni guiones de corte de línea. «Literal» = el valor normalizado es subcadena del texto normalizado.
- **D-C14.** Regex de cuantía del comando [c14] de docs/tablero_correcciones.md:136-141, implementada tal como la describe la prosa, sobre properties.descripcion en NFC y sin distinguir mayúsculas: porcentaje (`\d+([.,]\d+)?\s*%` o «por ciento»), `\bveces\b`, plazo (número en cifras o en letras de la lista LETRAS seguido de día, mes, año, hora o semana, en singular o plural, o «días hábiles/corridos») y monto ($, US$, U$S o USD seguidos de cifra, o cifra seguida, con «millones de» o «mil» opcionales, de pesos, dólares, USD o UVA). «Con campo»: `umbral` o `plazo` no vacío.
- **D-C14EUR.** Variante con nombre propio «c14_eur», declarada ANTES de aplicarla (decisión 3 del mandato): idéntica a c14 más «€» entre los prefijos de moneda seguidos de cifra. Motivo: c14 literal reproduce los «sin campo» del tablero pero da un nodo menos en el total con cuantía de r1, desarrollo y diez; el nodo es la Restriccion de cap::2.8.3.3 («equivalente en pesos €1.000.000»). Se reportan las dos.
- **D-PTL.** Patrón de tabla linealizada (medición 2), sobre el texto propio del chunk (`texto`, sin la herencia) partido en líneas: dispara en una línea con dos o más tokens separados por espacios, todos cifras (regex RE_TOKEN_CIFRA: signo o paréntesis opcional, prefijo de moneda opcional, dígitos con puntos o comas, % opcional), cuando las DOS líneas anteriores no están vacías, no tienen ningún dígito y tienen 60 caracteres o menos (encabezados cortos). Barrido principal: chunks con flags.contenido_tabular falso; los marcados se barren aparte, como dato informativo de sensibilidad del patrón.
- **D-NODOS-CHUNK.** Nodos de un chunk: los nodos con alguna procedencia cuyo chunk_id es el del chunk, excluidos TextoOrdenado, Sujeto y Comunicacion (nodos documentales o de catálogo que llevan procedencia en muchos chunks).
- **D-TAB.** Asignación de las tablas de e0_tablas.parsear_to a chunks: cada segmento de tabla (página p) se compara con los chunks del mismo TO cuyo campo `paginas` contiene p; puntaje = tamaño de la intersección de multiconjuntos entre los tokens de las celdas y los tokens del texto propio del chunk, dividido por los tokens de las celdas. El segmento se asigna al chunk de puntaje máximo si ese puntaje es 0,5 o más; con empate, a todos los empatados, y el empate se registra.
- **D-P6.** Prototipo del llenado por paso posterior en código (medición 6): regex propias, distintas de c14, que extraen triples (tipo, valor, unidad): porcentaje (cifra con % o cifra/letras con «por ciento»), veces (cifra/letras + «veces»), plazo (cifra/letras, con número entre paréntesis opcional, + día, mes, año, hora o semana; «hábiles/corridos» se guarda como calificador y no entra en la comparación) y monto (prefijo $, US$, U$S, USD, EUR o € + cifra con «millones»/«mil» opcional, o cifra + «millones de»/«mil millones de»/«mil» opcional + pesos, dólares, USD, UVA o euros). Moneda canónica: $ y pesos → ARS; US$, U$S, USD y dólares → USD; €, EUR y euros → EUR; UVA. Número: con coma, la coma es decimal y los puntos son de miles; sin coma, `\d{1,3}(\.\d{3})+` es de miles y cualquier otro punto es decimal; se quitan puntos y comas finales. Letras: las de LETRAS_VALOR, de una sola palabra; una palabra numérica precedida de otra (o de «y» tras otra) es un número compuesto: no se extrae y se cuenta como no cubierto. Multiplicadores: mil 10^3, millones 10^6, mil millones 10^9.
- **D-COINC.** Regla de coincidencia de la medición 6, fijada antes de comparar. F = triples que el prototipo extrae del valor del campo (`umbral` o `plazo`); D = triples que extrae de la descripción. Se evalúa en orden: «no extrae» si D está vacío; «campo sin cuantía» si F está vacío (el campo no tiene un valor que el prototipo reconozca, por ejemplo «mensual»); «coincide» si F ⊆ D; «coincide parcial» si F ∩ D no es vacío y F ⊄ D; «difiere» si F ∩ D es vacío. La comparación es exacta sobre (tipo, valor normalizado como Decimal, unidad canónica).
- **D-REL.** Umbral relacional (detección léxica, no lectura): la descripción tiene un porcentaje o «veces» seguido de «de», «del» o «sobre» y una palabra (con artículo o posesivo opcional), o la palabra «equivalente» a 40 caracteres o menos antes de un monto. Marca que el triple no captura la base del cálculo.

### Agregados tras la corrida de prueba (informativos, rotulados como posteriores)

Los agregué después de una corrida de prueba, antes de reportar. No reemplazan ninguna declaración previa y se reportan en columnas propias.

- **A-REL.** Ampliación de D-REL tras una prueba sintética, antes de reportar: «dos veces el patrimonio» no disparaba porque D-REL exige «de» después de «veces». Se suma «veces» seguido de artículo o posesivo (el, la, los, las, su, sus) y una palabra. La columna «relacional» usa D-REL más A-REL.
- **A-N1S.** Sensibilidad de la medición 1: además de D-N1, se eliminan TODOS los espacios en blanco en el valor y en el texto antes de comparar (caso visto en la corrida de prueba: «1%» en el campo, «1 %» en E0). Se reporta en columnas propias; la literalidad de referencia sigue siendo D-N1.
- **A-RELLENO.** Valores de relleno (detección léxica, no lectura): el valor del campo, normalizado con D-N1, es exactamente «n/a», «na», «no aplica», «permanente», o empieza con «no especificad», «sin especificar», «sin plazo» o «no se especifica».

## Medición 1 — Literalidad de `umbral` y `plazo`

Pares (nodo, campo) con valor no vacío. «E0» = texto propio o heredado del chunk de alguna procedencia del nodo. Normalización D-N1.

| Grafo | Tipo.campo | Total | En descripción | En E0 | E0 propio | E0 solo heredado | Desc. y E0 | Solo desc. | Solo E0 | Ninguno | Sin chunk |
|---|---|---|---|---|---|---|---|---|---|---|---|
| desarrollo | Obligacion.plazo | 248 | 80 | 88 | 82 | 6 | 76 | 4 | 12 | 156 | 0 |
| desarrollo | Obligacion.umbral | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| desarrollo | Potestad.umbral | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| desarrollo | Restriccion.umbral | 248 | 181 | 144 | 142 | 2 | 141 | 40 | 3 | 64 | 0 |
| desarrollo | **total** | 498 | 263 | 234 | 226 | 8 | 219 | 44 | 15 | 220 | 0 |
| r1 | Obligacion.plazo | 288 | 98 | 109 | 103 | 6 | 93 | 5 | 16 | 174 | 0 |
| r1 | Obligacion.umbral | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
| r1 | Restriccion.umbral | 363 | 225 | 192 | 191 | 1 | 190 | 35 | 2 | 136 | 0 |
| r1 | **total** | 652 | 323 | 301 | 294 | 7 | 283 | 40 | 18 | 311 | 0 |
| diez | Obligacion.plazo | 348 | 138 | 147 | 134 | 13 | 130 | 8 | 17 | 193 | 0 |
| diez | Obligacion.umbral | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| diez | Potestad.umbral | 1 | 1 | 1 | 1 | 0 | 1 | 0 | 0 | 0 | 0 |
| diez | Restriccion.umbral | 275 | 198 | 160 | 158 | 2 | 156 | 42 | 4 | 73 | 0 |
| diez | **total** | 625 | 338 | 309 | 294 | 15 | 288 | 50 | 21 | 266 | 0 |

Informativo (A-N1S, sin espacios; A-RELLENO, valores de relleno):

| Grafo | Tipo.campo | Total | En desc. (D-N1) | En desc. (A-N1S) | En E0 (D-N1) | En E0 (A-N1S) | Desc. y E0 (D-N1) | Desc. y E0 (A-N1S) | Relleno (A-RELLENO) |
|---|---|---|---|---|---|---|---|---|---|
| desarrollo | Obligacion.plazo | 248 | 80 | 80 | 88 | 88 | 76 | 76 | 28 |
| desarrollo | Obligacion.umbral | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| desarrollo | Potestad.umbral | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| desarrollo | Restriccion.umbral | 248 | 181 | 205 | 144 | 183 | 141 | 181 | 0 |
| desarrollo | **total** | 498 | 263 | 287 | 234 | 273 | 219 | 259 | 28 |
| r1 | Obligacion.plazo | 288 | 98 | 98 | 109 | 109 | 93 | 93 | 14 |
| r1 | Obligacion.umbral | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
| r1 | Restriccion.umbral | 363 | 225 | 270 | 192 | 245 | 190 | 244 | 0 |
| r1 | **total** | 652 | 323 | 369 | 301 | 355 | 283 | 338 | 14 |
| diez | Obligacion.plazo | 348 | 138 | 138 | 147 | 147 | 130 | 130 | 36 |
| diez | Obligacion.umbral | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| diez | Potestad.umbral | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 0 |
| diez | Restriccion.umbral | 275 | 198 | 224 | 160 | 202 | 156 | 199 | 0 |
| diez | **total** | 625 | 338 | 364 | 309 | 351 | 288 | 331 | 36 |

La lista completa de valores no literales (no están en la descripción, o no están en E0) está en `u1_mediciones.json`, clave `medicion_1.<grafo>.no_literales`.

## Medición 2 — Tablas no marcadas por E0

Chunks de los diez TOs: 2434 (2403 con `contenido_tabular` falso, 31 marcados). El patrón D-PTL dispara en **5** chunks no marcados, por TO: {'cap': 5}. En los marcados (informativo, sensibilidad del patrón): dispara en 3 de 31.

**Caso de control `cap::1.2`:** dispara = True; línea de cifras «5.000 2.500» tras «(salvo Cajas de Crédito Cooperativas)» / «-En millones de pesos-». `e0_tablas` le asigna: cap::tabla000 (p. 4, parseada, puntaje 1.0).

Cruce patrón × `e0_tablas` (regla D-TAB) sobre los chunks no marcados:

| Celda | Chunks |
|---|---|
| dispara|sin_tabla_e0_tablas | 4 |
| dispara|tabla_e0_tablas | 1 |
| no_dispara|sin_tabla_e0_tablas | 2386 |
| no_dispara|tabla_e0_tablas | 12 |

Mismo cruce sobre los chunks marcados (informativo):

| Celda | Chunks |
|---|---|
| dispara|sin_tabla_e0_tablas | 1 |
| dispara|tabla_e0_tablas | 2 |
| no_dispara|sin_tabla_e0_tablas | 6 |
| no_dispara|tabla_e0_tablas | 22 |

Nodos de los chunks no marcados que disparan (D-NODOS-CHUNK), por grafo:

| Grafo | Chunks | Sin nodos | Con nodo con umbral | Con cuantía c14 | Con cuantía c14_eur | Umbral o cuantía c14 | Nodos | Nodos con umbral | Nodos con cuantía c14 |
|---|---|---|---|---|---|---|---|---|---|
| desarrollo | 5 | 0 | 5 | 5 | 5 | 5 | 34 | 26 | 26 |
| r1 | 5 | 0 | 4 | 5 | 5 | 5 | 31 | 14 | 20 |
| diez | 5 | 0 | 5 | 5 | 5 | 5 | 34 | 26 | 26 |

Chunks no marcados que disparan:

| Chunk | Primera línea de cifras | Disparos | Tabla de e0_tablas | Nodos por grafo |
|---|---|---|---|---|
| `cap::1.2` | «5.000 2.500» | 1 | cap::tabla000(parseada) | desarrollo: 5 n, 2 umb, 2 cuant; r1: 3 n, 2 umb, 2 cuant; diez: 5 n, 2 umb, 2 cuant |
| `cap::2.12.2.5` | «0% 20% 50% 100% 150% 100%» | 1 | — | desarrollo: 7 n, 6 umb, 6 cuant; r1: 7 n, 6 umb, 6 cuant; diez: 7 n, 6 umb, 6 cuant |
| `cap::2.12.2.6` | «20% 50% 100% 100% 150% 100%» | 1 | — | desarrollo: 7 n, 6 umb, 6 cuant; r1: 6 n, 5 umb, 5 cuant; diez: 7 n, 6 umb, 6 cuant |
| `cap::2.12.2.8` | «20% 50% 100% 150% 200% 200%» | 1 | — | desarrollo: 8 n, 6 umb, 6 cuant; r1: 3 n, 1 umb, 1 cuant; diez: 8 n, 6 umb, 6 cuant |
| `cap::2.12.3.2` | «20% 30% 50% 100% 150% 50%» | 1 | — | desarrollo: 7 n, 6 umb, 6 cuant; r1: 12 n, 0 umb, 6 cuant; diez: 7 n, 6 umb, 6 cuant |

Chunks no marcados a los que `e0_tablas` asigna tabla sin que el patrón dispare (informativo): 12.

| Chunk | Tablas de e0_tablas | Nodos por grafo |
|---|---|---|
| `ric::S2` | ric::tabla000(parseada) | desarrollo: 8 n, 0 umb, 0 cuant; r1: 16 n, 0 umb, 0 cuant; diez: 8 n, 0 umb, 0 cuant |
| `ric::4.2` | ric::tabla003(parseada) | desarrollo: 5 n, 0 umb, 0 cuant; r1: 1 n, 0 umb, 0 cuant; diez: 5 n, 0 umb, 0 cuant |
| `ric::8.2` | ric::tabla021(parseada) | desarrollo: 1 n, 0 umb, 0 cuant; r1: 10 n, 0 umb, 0 cuant; diez: 1 n, 0 umb, 0 cuant |
| `ric::9.2.1` | ric::tabla022(parseada);ric::tabla023(parseada) | desarrollo: 0 n, 0 umb, 0 cuant; r1: 7 n, 1 umb, 1 cuant; diez: 0 n, 0 umb, 0 cuant |
| `ric::10.2` | ric::tabla025(parseada) | desarrollo: 1 n, 0 umb, 0 cuant; r1: 5 n, 0 umb, 0 cuant; diez: 1 n, 0 umb, 0 cuant |
| `cap::4.2.1.1` | cap::tabla003(parseada);cap::tabla004(parseada);cap::tabla005(parseada);cap::tabla006(parseada);cap::tabla007(parseada);cap::tabla008(parseada) | desarrollo: 20 n, 0 umb, 0 cuant; r1: 12 n, 0 umb, 0 cuant; diez: 20 n, 0 umb, 0 cuant |
| `cap::6.2.1.1` | cap::tabla035(parseada) | desarrollo: 11 n, 8 umb, 9 cuant; r1: 13 n, 8 umb, 8 cuant; diez: 11 n, 8 umb, 9 cuant |
| `cap::12.1` | cap::tabla039(parseada) | desarrollo: 6 n, 1 umb, 3 cuant; r1: 5 n, 1 umb, 3 cuant; diez: 6 n, 1 umb, 3 cuant |
| `cap::12.2` | cap::tabla040(parseada) | desarrollo: 3 n, 0 umb, 1 cuant; r1: 4 n, 2 umb, 3 cuant; diez: 3 n, 0 umb, 1 cuant |
| `ext::12.1` | ext::tabla000(parseada) | desarrollo: 3 n, 0 umb, 0 cuant; r1: 2 n, 0 umb, 0 cuant; diez: 3 n, 0 umb, 0 cuant |
| `ctacte::13.2` | ctacte::tabla000(parseada) | diez: 4 n, 0 umb, 0 cuant |
| `polcre::1.5` | polcre::tabla000(parseada) | diez: 4 n, 0 umb, 0 cuant |

Resumen por grafo de esos chunks (informativo):

| Grafo | Chunks | Sin nodos | Con nodo con umbral | Con cuantía c14 | Umbral o cuantía c14 | Nodos | Nodos con umbral | Nodos con cuantía c14 |
|---|---|---|---|---|---|---|---|---|
| desarrollo | 10 | 1 | 2 | 3 | 3 | 58 | 9 | 13 |
| r1 | 10 | 0 | 4 | 4 | 4 | 75 | 12 | 15 |
| diez | 12 | 1 | 2 | 3 | 3 | 66 | 9 | 13 |

Segmentos de `e0_tablas` sin chunk asignado: 43; de ellos, 40 en páginas que ningún chunk declara en `paginas`, y 3 con candidatos y puntaje menor que 0,5 (lista en el JSON).

## Medición 3 — Cuantías sin campo ([c14] y variante c14_eur)

Reproducción de la fila «Cuantías sin campo estructurado» del tablero (`docs/tablero_correcciones.md:61`):

| Grafo | Variante | Medido (sin campo de con cuantía) | Tablero | Sin campo reproduce | Total reproduce |
|---|---|---|---|---|---|
| desarrollo | c14 | 287 de 605 | 287 de 606 | sí | NO |
| desarrollo | c14_eur | 287 de 606 | 287 de 606 | sí | sí |
| r1 | c14 | 218 de 638 | 218 de 639 | sí | NO |
| r1 | c14_eur | 218 de 639 | 218 de 639 | sí | sí |
| diez | c14 | 323 de 682 | 323 de 683 | sí | NO |
| diez | c14_eur | 323 de 683 | 323 de 683 | sí | sí |

Nodos que solo detecta c14_eur en desarrollo: `Restriccion_la_exposicion_maxima_frente_a_una_misma_contrapa…` (Restriccion, con campo True, ['cap::2.8.3.3']).
Nodos que solo detecta c14_eur en r1: `Restriccion_la_exposicion_maxima_frente_a_una_misma_contrapa…` (Restriccion, con campo True, ['cap::2.8.3.3']).
Nodos que solo detecta c14_eur en diez: `Restriccion_la_exposicion_maxima_frente_a_una_misma_contrapa…` (Restriccion, con campo True, ['cap::2.8.3.3']).

| Grafo | Variante | Tipo | Con cuantía | Con campo | Sin campo | ≥2 cuantías | ≥2 y sin campo | Todas desde 160 | Todas desde 160 y sin campo | Alguna desde 160 | Cuantía en label | Cuantía en label y sin campo |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| desarrollo | c14 | Restriccion | 258 | 224 | 34 | 64 | 2 | 53 | 14 | 61 | 222 | 25 |
| desarrollo | c14 | Condicion | 134 | 0 | 134 | 28 | 28 | 36 | 36 | 40 | 101 | 101 |
| desarrollo | c14 | Obligacion | 170 | 94 | 76 | 17 | 11 | 55 | 31 | 62 | 92 | 35 |
| desarrollo | c14 | Excepcion | 43 | 0 | 43 | 11 | 11 | 13 | 13 | 14 | 22 | 22 |
| desarrollo | c14 | **total** | 605 | 318 | 287 | 120 | 52 | 157 | 94 | 177 | 437 | 183 |
| desarrollo | c14_eur | Restriccion | 259 | 225 | 34 | 64 | 2 | 53 | 14 | 61 | 222 | 25 |
| desarrollo | c14_eur | Condicion | 134 | 0 | 134 | 28 | 28 | 36 | 36 | 40 | 101 | 101 |
| desarrollo | c14_eur | Obligacion | 170 | 94 | 76 | 17 | 11 | 55 | 31 | 62 | 92 | 35 |
| desarrollo | c14_eur | Excepcion | 43 | 0 | 43 | 11 | 11 | 13 | 13 | 14 | 22 | 22 |
| desarrollo | c14_eur | **total** | 606 | 319 | 287 | 120 | 52 | 157 | 94 | 177 | 437 | 183 |
| r1 | c14 | Restriccion | 361 | 298 | 63 | 87 | 14 | 68 | 14 | 84 | 315 | 43 |
| r1 | c14 | Obligacion | 228 | 122 | 106 | 34 | 18 | 83 | 39 | 96 | 109 | 42 |
| r1 | c14 | Excepcion | 49 | 0 | 49 | 10 | 10 | 20 | 20 | 22 | 29 | 29 |
| r1 | c14 | **total** | 638 | 420 | 218 | 131 | 42 | 171 | 73 | 202 | 453 | 114 |
| r1 | c14_eur | Restriccion | 362 | 299 | 63 | 87 | 14 | 69 | 14 | 85 | 315 | 43 |
| r1 | c14_eur | Obligacion | 228 | 122 | 106 | 34 | 18 | 83 | 39 | 96 | 109 | 42 |
| r1 | c14_eur | Excepcion | 49 | 0 | 49 | 10 | 10 | 20 | 20 | 22 | 29 | 29 |
| r1 | c14_eur | **total** | 639 | 421 | 218 | 131 | 42 | 172 | 73 | 203 | 453 | 114 |
| diez | c14 | Restriccion | 280 | 244 | 36 | 66 | 2 | 54 | 14 | 62 | 239 | 26 |
| diez | c14 | Condicion | 156 | 0 | 156 | 32 | 32 | 39 | 39 | 46 | 116 | 116 |
| diez | c14 | Obligacion | 202 | 115 | 87 | 19 | 12 | 64 | 36 | 72 | 106 | 36 |
| diez | c14 | Excepcion | 44 | 0 | 44 | 11 | 11 | 13 | 13 | 14 | 22 | 22 |
| diez | c14 | **total** | 682 | 359 | 323 | 128 | 57 | 170 | 102 | 194 | 483 | 200 |
| diez | c14_eur | Restriccion | 281 | 245 | 36 | 66 | 2 | 54 | 14 | 62 | 239 | 26 |
| diez | c14_eur | Condicion | 156 | 0 | 156 | 32 | 32 | 39 | 39 | 46 | 116 | 116 |
| diez | c14_eur | Obligacion | 202 | 115 | 87 | 19 | 12 | 64 | 36 | 72 | 106 | 36 |
| diez | c14_eur | Excepcion | 44 | 0 | 44 | 11 | 11 | 13 | 13 | 14 | 22 | 22 |
| diez | c14_eur | **total** | 683 | 360 | 323 | 128 | 57 | 170 | 102 | 194 | 483 | 200 |

«Todas desde 160»: la primera cuantía empieza en el carácter 160 o después, así que el resumen de `buscar_nodos` (`harness.py:110-124`, `descripcion[:160]`) no muestra ninguna. Posiciones sobre la descripción en NFC; descripciones que cambian con NFC: desarrollo 0, r1 0, diez 0.

## Medición 6 — Prototipo del llenado por paso posterior en código (D-P6, D-COINC)

Acuerdo del prototipo contra `umbral` y `plazo` donde existen:

| Grafo | Tipo.campo | Total | Coincide | Coincide y único | Coincide parcial | Difiere | Campo sin cuantía | No extrae | No extrae, con cuantía en el campo |
|---|---|---|---|---|---|---|---|---|---|
| desarrollo | Obligacion.plazo | 248 | 74 | 71 | 0 | 0 | 18 | 156 | 6 |
| desarrollo | Obligacion.umbral | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| desarrollo | Potestad.umbral | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| desarrollo | Restriccion.umbral | 248 | 219 | 183 | 0 | 0 | 7 | 22 | 7 |
| desarrollo | **total** | 498 | 295 | 256 | 0 | 0 | 25 | 178 | 13 |
| r1 | Obligacion.plazo | 288 | 97 | 92 | 0 | 0 | 23 | 168 | 9 |
| r1 | Obligacion.umbral | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| r1 | Restriccion.umbral | 363 | 303 | 260 | 0 | 0 | 8 | 52 | 16 |
| r1 | **total** | 652 | 401 | 353 | 0 | 0 | 31 | 220 | 25 |
| diez | Obligacion.plazo | 348 | 95 | 91 | 0 | 0 | 18 | 235 | 7 |
| diez | Obligacion.umbral | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| diez | Potestad.umbral | 1 | 1 | 1 | 0 | 0 | 0 | 0 | 0 |
| diez | Restriccion.umbral | 275 | 239 | 201 | 0 | 0 | 7 | 29 | 7 |
| diez | **total** | 625 | 336 | 294 | 0 | 0 | 25 | 264 | 14 |

«Coincide y único»: la descripción da un solo triple y es el del campo. «No extrae, con cuantía en el campo»: desglose de «no extrae» (D-COINC no cambia).


Cobertura sobre los nodos de los cuatro tipos con cuantía (universo c14_eur, que contiene al de c14 literal), y casos no cubiertos:

| Grafo | Grupo | Nodos | En c14 literal | Extrae 0 | Extrae 1 | Extrae ≥2 (varios valores) | Letras compuestas | Relacional (D-REL y A-REL) | Cifra ≠ letras |
|---|---|---|---|---|---|---|---|---|---|
| desarrollo | con_campo | 319 | 318 | 10 | 267 | 42 | 5 | 61 | 0 |
| desarrollo | fuera_de_c14_eur_con_campo | 10 | — | — | 10 | 0 | — | — | — |
| desarrollo | fuera_de_c14_eur_sin_campo | 30 | — | — | 25 | 5 | — | — | — |
| desarrollo | sin_campo | 287 | 287 | 13 | 240 | 34 | 1 | 62 | 0 |
| r1 | con_campo | 421 | 420 | 18 | 348 | 55 | 6 | 92 | 0 |
| r1 | fuera_de_c14_eur_con_campo | 29 | — | — | 27 | 2 | — | — | — |
| r1 | fuera_de_c14_eur_sin_campo | 19 | — | — | 16 | 3 | — | — | — |
| r1 | sin_campo | 218 | 218 | 4 | 185 | 29 | 2 | 44 | 0 |
| diez | con_campo | 360 | 359 | 10 | 305 | 45 | 5 | 66 | 0 |
| diez | fuera_de_c14_eur_con_campo | 10 | — | — | 10 | 0 | — | — | — |
| diez | fuera_de_c14_eur_sin_campo | 30 | — | — | 25 | 5 | — | — | — |
| diez | sin_campo | 323 | 323 | 18 | 267 | 38 | 1 | 63 | 0 |

Grupos «fuera_de_c14_eur_*»: nodos de los cuatro tipos sin cuantía según c14_eur de los que el prototipo sí extrae un valor (por ejemplo, la forma «2 (dos) años», con el número en letras entre paréntesis, que c14 no reconoce). Es un dato del prototipo; c14 no se modifica. Ejemplos y la lista de «difiere» y «coincide parcial» en el JSON, clave `medicion_6.<grafo>`.

## Aristas `limita` (insumo del atributo de la relación)

| Grafo | `limita` | Desde Restriccion con umbral | Restricciones | Con umbral | Con umbral y sin `limita` | Con `limita` | Con `limita` y sin umbral (S18) | Con más de una `limita` |
|---|---|---|---|---|---|---|---|---|
| desarrollo | 284 | 189 | 632 | 248 | 62 | 278 | 92 | 6 |
| r1 | 1041 | 333 | 1397 | 363 | 52 | 964 | 653 | 51 |
| diez | 336 | 219 | 796 | 275 | 64 | 324 | 113 | 10 |

- **desarrollo.** Origen de `limita` por tipo: {'Restriccion': 284}; destino: {'Operacion': 284}; por `Restriccion.tipo`: {'limite_cualitativo': 76, 'limite_cuantitativo': 201, 'limite_temporal': 3, 'prohibicion': 4}. Con umbral y sin `limita`, por tipo: {'limite_cualitativo': 1, 'limite_cuantitativo': 61}; sus relaciones hacia Operacion: {'(ninguna hacia Operacion)': 54, 'referencia': 8}. Con `limita` y sin umbral, por tipo: {'limite_cualitativo': 75, 'limite_cuantitativo': 14, 'prohibicion': 3}. `limita` por Restriccion: {1: 272, 2: 6}. Condiciones con cuantía y sin `condicion_de`: c14: 77 de 134 con cuantía (1178 Condicion); c14_eur: 77 de 134 con cuantía (1178 Condicion).
- **r1.** Origen de `limita` por tipo: {'Restriccion': 1041}; destino: {'Operacion': 1041}; por `Restriccion.tipo`: {'limite_cualitativo': 670, 'limite_cuantitativo': 368, 'prohibicion': 3}. Con umbral y sin `limita`, por tipo: {'limite_cualitativo': 4, 'limite_cuantitativo': 47, 'prohibicion': 1}; sus relaciones hacia Operacion: {'(ninguna hacia Operacion)': 43, 'referencia': 4, 'regula': 5}. Con `limita` y sin umbral, por tipo: {'limite_cualitativo': 608, 'limite_cuantitativo': 42, 'prohibicion': 3}. `limita` por Restriccion: {1: 913, 2: 37, 3: 4, 4: 8, 5: 2}. Condiciones con cuantía y sin `condicion_de`: c14: 0 de 0 con cuantía (0 Condicion); c14_eur: 0 de 0 con cuantía (0 Condicion).
- **diez.** Origen de `limita` por tipo: {'Restriccion': 336}; destino: {'Operacion': 336}; por `Restriccion.tipo`: {'limite_cualitativo': 100, 'limite_cuantitativo': 229, 'limite_temporal': 3, 'prohibicion': 4}. Con umbral y sin `limita`, por tipo: {'limite_cualitativo': 1, 'limite_cuantitativo': 63}; sus relaciones hacia Operacion: {'(ninguna hacia Operacion)': 56, 'referencia': 8}. Con `limita` y sin umbral, por tipo: {'limite_cualitativo': 96, 'limite_cuantitativo': 14, 'prohibicion': 3}. `limita` por Restriccion: {1: 314, 2: 8, 3: 2}. Condiciones con cuantía y sin `condicion_de`: c14: 87 de 156 con cuantía (1383 Condicion); c14_eur: 87 de 156 con cuantía (1383 Condicion).

