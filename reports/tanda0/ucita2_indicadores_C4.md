# Indicadores de exactitud de cita — corrida parametrizada

Tres indicadores determinísticos por respuesta, sin juez ni API (USD 0), sobre
las tandas `ev2_c4_dev_neo4j`, `ev2_c4_dev_neo4j_enc_r1`, `ev2_c4_dev_neo4j_enc_r2`, `ev2_c4_dev_neo4j_enc_r3` de `data/experiment/ev2_tanda0/trazas`.
Se reporta por tanda, sin pool. No es resultado de la tesis, no cruza con
veredictos del juez ni con atribuciones. Este archivo se deriva de
`reports/tanda0/ucita2_indicadores_C4.json` (generado por `scripts/ucita2_indicadores.py`, sha256
`5379c2f201643947777be5a061e270bf3a2528b82b900dc5f4041747b9d53572`), nunca al revés; los conteos se recomputan desde el JSON.

Régimen de candados: medidos, sin esperado (argumentos distintos de los defaults); harness congelado verificado. Conciliación: sin conciliación (tandas distintas de las default).

## 1. Definiciones aplicadas

- **agregación**: fracción cruda «n de N» por indicador; sin porcentajes, sin pool entre tandas, sin intervalos; sin cruce con veredictos del juez ni con atribuciones.
- **cita parseable**: source_doc ~ ^TO_[a-z_]+_actual\.pdf$ y location ~ ^Punto (\d+(?:\.\d+)*)\.?$ o ^Sección (\d+)$; punto normalizado = grupo capturado; TO = el que el manifiesto asocia al source_doc. Toda cita no parseable se lista y cuenta como «no» en los indicadores 2 y 3.
- **columna informativa**: «sí» si alguna cita es ancestro del ancla (mismo TO y el ancla empieza con el punto citado seguido de «.»).
- **grupos**: abstención = respondible == false; contenido = el resto con JSON; tres tablas por tanda (todas / contenido / abstención).
- **indicador 1 · cita fundada**: «sí» si TODA cita de la respuesta es fiel a alguna entrada de trace.seen_provenances de la misma traza según _cita_fiel/_norm_loc del harness (normalizada, principal); lectura byte-exacta al lado: tupla (source_doc, location) idéntica a alguna entrada.
- **indicador 2 · cita existente**: «sí» si TODA cita parseable resuelve a un `numero` del índice E0 de su TO; precedencia: alguna inexistente o no parseable → «no»; si no, alguna fuera_de_indice → «fuera_de_indice» (más niveles que la profundidad máxima del índice y prefijo a esa profundidad existente; se cuenta aparte); si no → «sí».
- **indicador 3 · cita al punto de referencia**: «sí» si ALGUNA cita tiene el TO del ancla y su punto es el ancla o empieza con el ancla seguido de «.»; los ancestros NO cuentan.
- **sin_citas / sin_json**: lista de citas vacía o ausente → «sin_citas» en los tres indicadores (nunca «sí» por vacuidad); parse_ok falso → «sin_json» en los tres y conteo aparte.

## 2. Insumos (sha256 verificados al inicio y al cierre de la corrida)

| clave | ruta | sha256 | inicio = cierre |
|---|---|---|---|
| digest_ev2_c4_dev_neo4j | `data/experiment/ev2_tanda0/trazas/ev2_c4_dev_neo4j` (40 archivos) | `77f1ab36f2b3dbc66d8c867f642f74e816938cb8e904cf7d663661d7f4905d86` | sí (medido, sin esperado) |
| digest_ev2_c4_dev_neo4j_enc_r1 | `data/experiment/ev2_tanda0/trazas/ev2_c4_dev_neo4j_enc_r1` (21 archivos) | `64e60522242bb7d9fbd4a8f42d1d8f3a6983e0d495ad2a7ad745a7a9c3464d96` | sí (medido, sin esperado) |
| digest_ev2_c4_dev_neo4j_enc_r2 | `data/experiment/ev2_tanda0/trazas/ev2_c4_dev_neo4j_enc_r2` (21 archivos) | `78c9d49193d66422295869db60a73a1c684da8f26cbf7a6d71d6b228473821cc` | sí (medido, sin esperado) |
| digest_ev2_c4_dev_neo4j_enc_r3 | `data/experiment/ev2_tanda0/trazas/ev2_c4_dev_neo4j_enc_r3` (21 archivos) | `1ca8e5332f95c364182ba341048d51fb520fab4ffbaa38ef69b0cd8010df110e` | sí (medido, sin esperado) |
| e0_cap | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_cap.json` | `eae830c7640f132986327dd9a065535573bf1c343d804492d272154d700daf55` | sí (medido, sin esperado) |
| e0_cla | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_cla.json` | `3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917` | sí (medido, sin esperado) |
| e0_ctacte | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_ctacte.json` | `e0b503155f6cc4068326b26f78ee6412874e0c23517bd934158a355c3c98518c` | sí (medido, sin esperado) |
| e0_docvig | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_docvig.json` | `007396183c651c6cf5191b60627ab878dca171b395f62c0b5b1a8f6a21a524e0` | sí (medido, sin esperado) |
| e0_ext | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_ext.json` | `0b0137d58decb66d66bbb6f60d0192071d2b2ee0c819ee95658f9f31881c6d53` | sí (medido, sin esperado) |
| e0_lingob | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_lingob.json` | `97e94f968b8b894b15cb57658c9697816e1a022d008161748efa10f8b2538a22` | sí (medido, sin esperado) |
| e0_pagjub | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_pagjub.json` | `e299e736a61f1851940a0575749679e0d11a634fcc23966e0d887058ced82572` | sí (medido, sin esperado) |
| e0_polcre | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_polcre.json` | `a914ce9e6b3159c48744d7ef125ffb9faf602f075b0cd05da5508fe502179341` | sí (medido, sin esperado) |
| e0_pro | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_pro.json` | `4126ec9e20b2d53094a1f77dd4d5676e117995c8338ce0883a5a9dd3b5d318ae` | sí (medido, sin esperado) |
| e0_ric | `data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/estructura_ric.json` | `64cbd27f277f75ab4919863ed3fcd98c93238a8d9e5f7c57dd80c40487230892` | sí (medido, sin esperado) |
| gold | `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` | `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40` | sí (medido, sin esperado) |
| harness | `data/experiment/evaluacion/harness.py` | `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e` | sí |
| manifiesto | `data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json` | `5299340cc5fb8bd22c9a382cf8daf320fc57d7c7441e6748a8bdf49ab32461c7` | sí (medido, sin esperado) |

Funciones `_cita_fiel` y `_norm_loc` importadas de `data/experiment/evaluacion/harness.py`
(sin modificarlo; ruta y sha verificados en la importación).

## 3. Índice E0 por TO (decisión 5)

| TO | archivo | nodos | `numero` distintos | profundidad máxima |
|---|---|---|---|---|
| cap | `TO_capitales_minimos_actual.pdf` | 519 | 519 | 4 |
| cla | `TO_clasificacion_deudores_actual.pdf` | 162 | 162 | 4 |
| ctacte | `ctacte.pdf` | 432 | 432 | 4 |
| docvig | `docvig.pdf` | 42 | 42 | 4 |
| ext | `TO_exterior_cambios_actual.pdf` | 963 | 963 | 4 |
| lingob | `lingob.pdf` | 146 | 146 | 4 |
| pagjub | `pagjub.pdf` | 57 | 57 | 4 |
| polcre | `polcre.pdf` | 71 | 71 | 4 |
| pro | `TO_proteccion_usuarios_servicios_financieros_actual.pdf` | 113 | 113 | 4 |
| ric | `TO_regimen_informativo_contable_mensual_actual.pdf` | 107 | 107 | 4 |

Anclas del gold que resuelven en el índice E0 de su TO: **40 de 40**.

## 4. Resultados por tanda (decisión 8: tres tablas por tanda; la de contenido es la principal)

### 4.1 Tanda `ev2_c4_dev_neo4j` — 40 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 33 + abstención 7 + sin_json 0 = 40 (N todas = 40).

#### ev2_c4_dev_neo4j · todas las respuestas (N = 40)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 40 de 40 | 0 | 0 | 0 | 0 | 40 |
| 1 · cita fundada (byte-exacta) | 40 de 40 | 0 | 0 | 0 | 0 | 40 |
| 2 · cita existente (índice E0) | 40 de 40 | 0 | 0 | 0 | 0 | 40 |
| 3 · cita al punto de referencia | 36 de 40 | 4 | 0 | 0 | 0 | 40 |
| informativa · cita ancestro del ancla | 0 de 40 | 40 | 0 | 0 | 0 | 40 |

#### ev2_c4_dev_neo4j · solo contenido (respondible true) (N = 33)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 33 de 33 | 0 | 0 | 0 | 0 | 33 |
| 1 · cita fundada (byte-exacta) | 33 de 33 | 0 | 0 | 0 | 0 | 33 |
| 2 · cita existente (índice E0) | 33 de 33 | 0 | 0 | 0 | 0 | 33 |
| 3 · cita al punto de referencia | 31 de 33 | 2 | 0 | 0 | 0 | 33 |
| informativa · cita ancestro del ancla | 0 de 33 | 33 | 0 | 0 | 0 | 33 |

#### ev2_c4_dev_neo4j · solo abstención (respondible false) (N = 7)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 7 de 7 | 0 | 0 | 0 | 0 | 7 |
| 1 · cita fundada (byte-exacta) | 7 de 7 | 0 | 0 | 0 | 0 | 7 |
| 2 · cita existente (índice E0) | 7 de 7 | 0 | 0 | 0 | 0 | 7 |
| 3 · cita al punto de referencia | 5 de 7 | 2 | 0 | 0 | 0 | 7 |
| informativa · cita ancestro del ancla | 0 de 7 | 7 | 0 | 0 | 0 | 7 |

#### ev2_c4_dev_neo4j · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 0.
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.2 Tanda `ev2_c4_dev_neo4j_enc_r1` — 21 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 18 + abstención 3 + sin_json 0 = 21 (N todas = 21).

#### ev2_c4_dev_neo4j_enc_r1 · todas las respuestas (N = 21)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 1 · cita fundada (byte-exacta) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 2 · cita existente (índice E0) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 3 · cita al punto de referencia | 19 de 21 | 2 | 0 | 0 | 0 | 21 |
| informativa · cita ancestro del ancla | 0 de 21 | 21 | 0 | 0 | 0 | 21 |

#### ev2_c4_dev_neo4j_enc_r1 · solo contenido (respondible true) (N = 18)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 1 · cita fundada (byte-exacta) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 2 · cita existente (índice E0) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 3 · cita al punto de referencia | 17 de 18 | 1 | 0 | 0 | 0 | 18 |
| informativa · cita ancestro del ancla | 0 de 18 | 18 | 0 | 0 | 0 | 18 |

#### ev2_c4_dev_neo4j_enc_r1 · solo abstención (respondible false) (N = 3)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 3 de 3 | 0 | 0 | 0 | 0 | 3 |
| 1 · cita fundada (byte-exacta) | 3 de 3 | 0 | 0 | 0 | 0 | 3 |
| 2 · cita existente (índice E0) | 3 de 3 | 0 | 0 | 0 | 0 | 3 |
| 3 · cita al punto de referencia | 2 de 3 | 1 | 0 | 0 | 0 | 3 |
| informativa · cita ancestro del ancla | 0 de 3 | 3 | 0 | 0 | 0 | 3 |

#### ev2_c4_dev_neo4j_enc_r1 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 0.
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.3 Tanda `ev2_c4_dev_neo4j_enc_r2` — 21 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 18 + abstención 3 + sin_json 0 = 21 (N todas = 21).

#### ev2_c4_dev_neo4j_enc_r2 · todas las respuestas (N = 21)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 1 · cita fundada (byte-exacta) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 2 · cita existente (índice E0) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 3 · cita al punto de referencia | 19 de 21 | 2 | 0 | 0 | 0 | 21 |
| informativa · cita ancestro del ancla | 0 de 21 | 21 | 0 | 0 | 0 | 21 |

#### ev2_c4_dev_neo4j_enc_r2 · solo contenido (respondible true) (N = 18)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 1 · cita fundada (byte-exacta) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 2 · cita existente (índice E0) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 3 · cita al punto de referencia | 17 de 18 | 1 | 0 | 0 | 0 | 18 |
| informativa · cita ancestro del ancla | 0 de 18 | 18 | 0 | 0 | 0 | 18 |

#### ev2_c4_dev_neo4j_enc_r2 · solo abstención (respondible false) (N = 3)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 3 de 3 | 0 | 0 | 0 | 0 | 3 |
| 1 · cita fundada (byte-exacta) | 3 de 3 | 0 | 0 | 0 | 0 | 3 |
| 2 · cita existente (índice E0) | 3 de 3 | 0 | 0 | 0 | 0 | 3 |
| 3 · cita al punto de referencia | 2 de 3 | 1 | 0 | 0 | 0 | 3 |
| informativa · cita ancestro del ancla | 0 de 3 | 3 | 0 | 0 | 0 | 3 |

#### ev2_c4_dev_neo4j_enc_r2 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 0.
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.4 Tanda `ev2_c4_dev_neo4j_enc_r3` — 21 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 17 + abstención 4 + sin_json 0 = 21 (N todas = 21).

#### ev2_c4_dev_neo4j_enc_r3 · todas las respuestas (N = 21)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 1 · cita fundada (byte-exacta) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 2 · cita existente (índice E0) | 21 de 21 | 0 | 0 | 0 | 0 | 21 |
| 3 · cita al punto de referencia | 20 de 21 | 1 | 0 | 0 | 0 | 21 |
| informativa · cita ancestro del ancla | 0 de 21 | 21 | 0 | 0 | 0 | 21 |

#### ev2_c4_dev_neo4j_enc_r3 · solo contenido (respondible true) (N = 17)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 17 de 17 | 0 | 0 | 0 | 0 | 17 |
| 1 · cita fundada (byte-exacta) | 17 de 17 | 0 | 0 | 0 | 0 | 17 |
| 2 · cita existente (índice E0) | 17 de 17 | 0 | 0 | 0 | 0 | 17 |
| 3 · cita al punto de referencia | 17 de 17 | 0 | 0 | 0 | 0 | 17 |
| informativa · cita ancestro del ancla | 0 de 17 | 17 | 0 | 0 | 0 | 17 |

#### ev2_c4_dev_neo4j_enc_r3 · solo abstención (respondible false) (N = 4)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 4 de 4 | 0 | 0 | 0 | 0 | 4 |
| 1 · cita fundada (byte-exacta) | 4 de 4 | 0 | 0 | 0 | 0 | 4 |
| 2 · cita existente (índice E0) | 4 de 4 | 0 | 0 | 0 | 0 | 4 |
| 3 · cita al punto de referencia | 3 de 4 | 1 | 0 | 0 | 0 | 4 |
| informativa · cita ancestro del ancla | 0 de 4 | 4 | 0 | 0 | 0 | 4 |

#### ev2_c4_dev_neo4j_enc_r3 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 0.
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

## 5. Conciliación con U-CITA: sin conciliación

las cifras de U-CITA (reports/inventario_UCITA.md §4-§5) solo aplican a las tandas default ['ev2_r1_base', 'ev2_r1_enc_r1', 'ev2_r1_enc_r2', 'ev2_r1_enc_r3']; tandas de esta corrida: ['ev2_c4_dev_neo4j', 'ev2_c4_dev_neo4j_enc_r1', 'ev2_c4_dev_neo4j_enc_r2', 'ev2_c4_dev_neo4j_enc_r3'].

### 5.1 Resumen descriptivo por tanda (sin cifra esperada)

| medida | ev2_c4_dev_neo4j | ev2_c4_dev_neo4j_enc_r1 | ev2_c4_dev_neo4j_enc_r2 | ev2_c4_dev_neo4j_enc_r3 |
|---|---|---|---|---|
| trazas | 40 | 21 | 21 | 21 |
| citas totales | 94 | 59 | 60 | 60 |
| citas parseables | 94 | 59 | 60 | 60 |
| respuestas con ≥ 1 cita parseable | 40 | 21 | 21 | 21 |
| contenido (respondible true) | 33 | 18 | 18 | 17 |
| abstenciones (respondible false) | 7 | 3 | 3 | 4 |
| sin_json | 0 | 0 | 0 | 0 |
| sin_citas | 0 | 0 | 0 | 0 |
| citas no fundadas (normalizada) | 0 | 0 | 0 | 0 |
| citas no fundadas (byte-exacta) | 0 | 0 | 0 | 0 |
| citas no existentes | 0 | 0 | 0 | 0 |
| citas fuera_de_indice | 0 | 0 | 0 | 0 |
| citas no parseables | 0 | 0 | 0 | 0 |
| control indicador 1: trazas con discrepancia | 0 | 0 | 0 | 0 |

Trazas con citas no fundadas (normalizada), por tanda:
- ev2_c4_dev_neo4j: ninguna
- ev2_c4_dev_neo4j_enc_r1: ninguna
- ev2_c4_dev_neo4j_enc_r2: ninguna
- ev2_c4_dev_neo4j_enc_r3: ninguna

Control del indicador 1 (recómputo vs. `citations_unseen_normalized` / `citations_unseen_raw` persistidos): **0 discrepancias** en 103 trazas.

## 6. Salidas y reproducción

- `reports/tanda0/ucita2_indicadores_C4.json` — sha256 `789b05fb88c0c604fcfc7a4ac95f0713efd2e920ee95827f66792f37ac800f03` (este .md se renderiza desde ese archivo).
- Comando (desde la raíz del repo):

```
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/ucita2_indicadores.py --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json --e0 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0 --trazas data/experiment/ev2_tanda0/trazas --tandas ev2_c4_dev_neo4j ev2_c4_dev_neo4j_enc_r1 ev2_c4_dev_neo4j_enc_r2 ev2_c4_dev_neo4j_enc_r3 --out-json reports/tanda0/ucita2_indicadores_C4.json --out-md reports/tanda0/ucita2_indicadores_C4.md
```

- Selftest de respuesta conocida: `PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/ucita2_indicadores.py --selftest`.
- Determinismo: el JSON no lleva timestamps; dos corridas consecutivas producen el mismo sha256.
