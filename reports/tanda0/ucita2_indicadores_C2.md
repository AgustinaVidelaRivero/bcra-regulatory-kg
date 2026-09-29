# Indicadores de exactitud de cita — corrida parametrizada

Tres indicadores determinísticos por respuesta, sin juez ni API (USD 0), sobre
las tandas `ev2_c2_r1_neo4j`, `ev2_c2_r1_neo4j_enc_r1`, `ev2_c2_r1_neo4j_enc_r2`, `ev2_c2_r1_neo4j_enc_r3` de `data/experiment/ev2_tanda0/trazas`.
Se reporta por tanda, sin pool. No es resultado de la tesis, no cruza con
veredictos del juez ni con atribuciones. Este archivo se deriva de
`reports/tanda0/ucita2_indicadores_C2.json` (generado por `scripts/ucita2_indicadores.py`, sha256
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
| digest_ev2_c2_r1_neo4j | `data/experiment/ev2_tanda0/trazas/ev2_c2_r1_neo4j` (40 archivos) | `5eba24de4f4fd7dfe3acb851c56f1f22a90258dcbce22011d0e7516d5f2db158` | sí (medido, sin esperado) |
| digest_ev2_c2_r1_neo4j_enc_r1 | `data/experiment/ev2_tanda0/trazas/ev2_c2_r1_neo4j_enc_r1` (24 archivos) | `1e5d108205d4251ba0366ce50c7c74a1bc2a4698a95989a4450a86afe7a6fcbd` | sí (medido, sin esperado) |
| digest_ev2_c2_r1_neo4j_enc_r2 | `data/experiment/ev2_tanda0/trazas/ev2_c2_r1_neo4j_enc_r2` (24 archivos) | `3634f88045700187f3a8dec4f4c02808ac721a7b8950b1a473ffee02e7fd53cc` | sí (medido, sin esperado) |
| digest_ev2_c2_r1_neo4j_enc_r3 | `data/experiment/ev2_tanda0/trazas/ev2_c2_r1_neo4j_enc_r3` (24 archivos) | `9fbd604014579df0f682b1a01258f6482dd1951284f3dc8d072c998a31d00693` | sí (medido, sin esperado) |
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

### 4.1 Tanda `ev2_c2_r1_neo4j` — 40 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 33 + abstención 7 + sin_json 0 = 40 (N todas = 40).

#### ev2_c2_r1_neo4j · todas las respuestas (N = 40)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 38 de 40 | 2 | 0 | 0 | 0 | 40 |
| 1 · cita fundada (byte-exacta) | 38 de 40 | 2 | 0 | 0 | 0 | 40 |
| 2 · cita existente (índice E0) | 40 de 40 | 0 | 0 | 0 | 0 | 40 |
| 3 · cita al punto de referencia | 35 de 40 | 5 | 0 | 0 | 0 | 40 |
| informativa · cita ancestro del ancla | 0 de 40 | 40 | 0 | 0 | 0 | 40 |

#### ev2_c2_r1_neo4j · solo contenido (respondible true) (N = 33)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 31 de 33 | 2 | 0 | 0 | 0 | 33 |
| 1 · cita fundada (byte-exacta) | 31 de 33 | 2 | 0 | 0 | 0 | 33 |
| 2 · cita existente (índice E0) | 33 de 33 | 0 | 0 | 0 | 0 | 33 |
| 3 · cita al punto de referencia | 32 de 33 | 1 | 0 | 0 | 0 | 33 |
| informativa · cita ancestro del ancla | 0 de 33 | 33 | 0 | 0 | 0 | 33 |

#### ev2_c2_r1_neo4j · solo abstención (respondible false) (N = 7)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 7 de 7 | 0 | 0 | 0 | 0 | 7 |
| 1 · cita fundada (byte-exacta) | 7 de 7 | 0 | 0 | 0 | 0 | 7 |
| 2 · cita existente (índice E0) | 7 de 7 | 0 | 0 | 0 | 0 | 7 |
| 3 · cita al punto de referencia | 3 de 7 | 4 | 0 | 0 | 0 | 7 |
| informativa · cita ancestro del ancla | 0 de 7 | 7 | 0 | 0 | 0 | 7 |

#### ev2_c2_r1_neo4j · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 4
  - EV2F-015: `TO_exterior_cambios_actual.pdf` / `Punto 14.2.3`
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.1`
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.2`
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.3`
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.2 Tanda `ev2_c2_r1_neo4j_enc_r1` — 24 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 22 + abstención 2 + sin_json 0 = 24 (N todas = 24).

#### ev2_c2_r1_neo4j_enc_r1 · todas las respuestas (N = 24)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| 1 · cita fundada (byte-exacta) | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| 2 · cita existente (índice E0) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 3 · cita al punto de referencia | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| informativa · cita ancestro del ancla | 0 de 24 | 24 | 0 | 0 | 0 | 24 |

#### ev2_c2_r1_neo4j_enc_r1 · solo contenido (respondible true) (N = 22)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 21 de 22 | 1 | 0 | 0 | 0 | 22 |
| 1 · cita fundada (byte-exacta) | 21 de 22 | 1 | 0 | 0 | 0 | 22 |
| 2 · cita existente (índice E0) | 22 de 22 | 0 | 0 | 0 | 0 | 22 |
| 3 · cita al punto de referencia | 22 de 22 | 0 | 0 | 0 | 0 | 22 |
| informativa · cita ancestro del ancla | 0 de 22 | 22 | 0 | 0 | 0 | 22 |

#### ev2_c2_r1_neo4j_enc_r1 · solo abstención (respondible false) (N = 2)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 2 de 2 | 0 | 0 | 0 | 0 | 2 |
| 1 · cita fundada (byte-exacta) | 2 de 2 | 0 | 0 | 0 | 0 | 2 |
| 2 · cita existente (índice E0) | 2 de 2 | 0 | 0 | 0 | 0 | 2 |
| 3 · cita al punto de referencia | 1 de 2 | 1 | 0 | 0 | 0 | 2 |
| informativa · cita ancestro del ancla | 0 de 2 | 2 | 0 | 0 | 0 | 2 |

#### ev2_c2_r1_neo4j_enc_r1 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 3
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.1`
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.2`
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.3`
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.3 Tanda `ev2_c2_r1_neo4j_enc_r2` — 24 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 19 + abstención 5 + sin_json 0 = 24 (N todas = 24).

#### ev2_c2_r1_neo4j_enc_r2 · todas las respuestas (N = 24)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| 1 · cita fundada (byte-exacta) | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| 2 · cita existente (índice E0) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 3 · cita al punto de referencia | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| informativa · cita ancestro del ancla | 0 de 24 | 24 | 0 | 0 | 0 | 24 |

#### ev2_c2_r1_neo4j_enc_r2 · solo contenido (respondible true) (N = 19)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 18 de 19 | 1 | 0 | 0 | 0 | 19 |
| 1 · cita fundada (byte-exacta) | 18 de 19 | 1 | 0 | 0 | 0 | 19 |
| 2 · cita existente (índice E0) | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| 3 · cita al punto de referencia | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| informativa · cita ancestro del ancla | 0 de 19 | 19 | 0 | 0 | 0 | 19 |

#### ev2_c2_r1_neo4j_enc_r2 · solo abstención (respondible false) (N = 5)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 1 · cita fundada (byte-exacta) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 2 · cita existente (índice E0) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 3 · cita al punto de referencia | 4 de 5 | 1 | 0 | 0 | 0 | 5 |
| informativa · cita ancestro del ancla | 0 de 5 | 5 | 0 | 0 | 0 | 5 |

#### ev2_c2_r1_neo4j_enc_r2 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 1
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.2`
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.4 Tanda `ev2_c2_r1_neo4j_enc_r3` — 24 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 22 + abstención 2 + sin_json 0 = 24 (N todas = 24).

#### ev2_c2_r1_neo4j_enc_r3 · todas las respuestas (N = 24)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| 1 · cita fundada (byte-exacta) | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| 2 · cita existente (índice E0) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 3 · cita al punto de referencia | 23 de 24 | 1 | 0 | 0 | 0 | 24 |
| informativa · cita ancestro del ancla | 0 de 24 | 24 | 0 | 0 | 0 | 24 |

#### ev2_c2_r1_neo4j_enc_r3 · solo contenido (respondible true) (N = 22)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 21 de 22 | 1 | 0 | 0 | 0 | 22 |
| 1 · cita fundada (byte-exacta) | 21 de 22 | 1 | 0 | 0 | 0 | 22 |
| 2 · cita existente (índice E0) | 22 de 22 | 0 | 0 | 0 | 0 | 22 |
| 3 · cita al punto de referencia | 22 de 22 | 0 | 0 | 0 | 0 | 22 |
| informativa · cita ancestro del ancla | 0 de 22 | 22 | 0 | 0 | 0 | 22 |

#### ev2_c2_r1_neo4j_enc_r3 · solo abstención (respondible false) (N = 2)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 2 de 2 | 0 | 0 | 0 | 0 | 2 |
| 1 · cita fundada (byte-exacta) | 2 de 2 | 0 | 0 | 0 | 0 | 2 |
| 2 · cita existente (índice E0) | 2 de 2 | 0 | 0 | 0 | 0 | 2 |
| 3 · cita al punto de referencia | 1 de 2 | 1 | 0 | 0 | 0 | 2 |
| informativa · cita ancestro del ancla | 0 de 2 | 2 | 0 | 0 | 0 | 2 |

#### ev2_c2_r1_neo4j_enc_r3 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 1
  - EV2F-019: `TO_capitales_minimos_actual.pdf` / `Punto 4.2.1.2`
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

## 5. Conciliación con U-CITA: sin conciliación

las cifras de U-CITA (reports/inventario_UCITA.md §4-§5) solo aplican a las tandas default ['ev2_r1_base', 'ev2_r1_enc_r1', 'ev2_r1_enc_r2', 'ev2_r1_enc_r3']; tandas de esta corrida: ['ev2_c2_r1_neo4j', 'ev2_c2_r1_neo4j_enc_r1', 'ev2_c2_r1_neo4j_enc_r2', 'ev2_c2_r1_neo4j_enc_r3'].

### 5.1 Resumen descriptivo por tanda (sin cifra esperada)

| medida | ev2_c2_r1_neo4j | ev2_c2_r1_neo4j_enc_r1 | ev2_c2_r1_neo4j_enc_r2 | ev2_c2_r1_neo4j_enc_r3 |
|---|---|---|---|---|
| trazas | 40 | 24 | 24 | 24 |
| citas totales | 94 | 55 | 57 | 54 |
| citas parseables | 94 | 55 | 57 | 54 |
| respuestas con ≥ 1 cita parseable | 40 | 24 | 24 | 24 |
| contenido (respondible true) | 33 | 22 | 19 | 22 |
| abstenciones (respondible false) | 7 | 2 | 5 | 2 |
| sin_json | 0 | 0 | 0 | 0 |
| sin_citas | 0 | 0 | 0 | 0 |
| citas no fundadas (normalizada) | 4 | 3 | 1 | 1 |
| citas no fundadas (byte-exacta) | 4 | 3 | 1 | 1 |
| citas no existentes | 0 | 0 | 0 | 0 |
| citas fuera_de_indice | 0 | 0 | 0 | 0 |
| citas no parseables | 0 | 0 | 0 | 0 |
| control indicador 1: trazas con discrepancia | 0 | 0 | 0 | 0 |

Trazas con citas no fundadas (normalizada), por tanda:
- ev2_c2_r1_neo4j: EV2F-015 (1), EV2F-019 (3)
- ev2_c2_r1_neo4j_enc_r1: EV2F-019 (3)
- ev2_c2_r1_neo4j_enc_r2: EV2F-019 (1)
- ev2_c2_r1_neo4j_enc_r3: EV2F-019 (1)

Control del indicador 1 (recómputo vs. `citations_unseen_normalized` / `citations_unseen_raw` persistidos): **0 discrepancias** en 112 trazas.

## 6. Salidas y reproducción

- `reports/tanda0/ucita2_indicadores_C2.json` — sha256 `780ff1c340f5992364ca4acb059b3febcc5d538dced09c413ba43d9f54175bc3` (este .md se renderiza desde ese archivo).
- Comando (desde la raíz del repo):

```
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/ucita2_indicadores.py --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json --e0 data/experiment/reextraccion_v2/e0_chunking/salida_tanda0 --trazas data/experiment/ev2_tanda0/trazas --tandas ev2_c2_r1_neo4j ev2_c2_r1_neo4j_enc_r1 ev2_c2_r1_neo4j_enc_r2 ev2_c2_r1_neo4j_enc_r3 --out-json reports/tanda0/ucita2_indicadores_C2.json --out-md reports/tanda0/ucita2_indicadores_C2.md
```

- Selftest de respuesta conocida: `PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/ucita2_indicadores.py --selftest`.
- Determinismo: el JSON no lleva timestamps; dos corridas consecutivas producen el mismo sha256.
