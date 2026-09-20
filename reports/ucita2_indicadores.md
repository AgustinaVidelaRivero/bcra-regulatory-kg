# U-CITA-2 — indicadores de exactitud de cita sobre KG-Reextraído-r1

Validación en desarrollo del componente «exactitud de cita» de B6.3: tres
indicadores determinísticos por respuesta, sin juez ni API (USD 0), sobre las
cuatro tandas de trazas de `data/experiment/ev2_r1/trazas/`. Se reporta por
tanda, sin pool; la base es la tabla principal y las tres re-corridas son
replicación. No es resultado de la tesis, no cruza con veredictos del juez ni
con atribuciones. Este archivo se deriva de `reports/ucita2_indicadores.json`
(generado por `scripts/ucita2_indicadores.py`), nunca al revés; los conteos se
recomputan desde el JSON al renderizar.

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
| digest_ev2_r1_base | `data/experiment/ev2_r1/trazas/ev2_r1_base` (40 archivos) | `d53316edd5082b562d542923d8c799c6355d5e2146f597741c77d5c035b5c25f` | sí |
| digest_ev2_r1_enc_r1 | `data/experiment/ev2_r1/trazas/ev2_r1_enc_r1` (24 archivos) | `4b9499e91bb0b1e186d39ee478e5df23d31d8259e8ec8fff2449c009aba1fadd` | sí |
| digest_ev2_r1_enc_r2 | `data/experiment/ev2_r1/trazas/ev2_r1_enc_r2` (24 archivos) | `de644c9295bd82918b1bd45b4e3c4e078e8c24503f779bee0031e154f984c437` | sí |
| digest_ev2_r1_enc_r3 | `data/experiment/ev2_r1/trazas/ev2_r1_enc_r3` (24 archivos) | `a80cc1fb907d5aaeb510dedde1eac707c6206423033cce408aba10073b772ce7` | sí |
| e0_cap | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cap.json` | `eae830c7640f132986327dd9a065535573bf1c343d804492d272154d700daf55` | sí |
| e0_cla | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_cla.json` | `3cd26083fee7355ef3d8027ac353a744c2f1cfa35830535fe1be2b9505eaf917` | sí |
| e0_ext | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_ext.json` | `0b0137d58decb66d66bbb6f60d0192071d2b2ee0c819ee95658f9f31881c6d53` | sí |
| e0_pro | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_pro.json` | `4126ec9e20b2d53094a1f77dd4d5676e117995c8338ce0883a5a9dd3b5d318ae` | sí |
| e0_ric | `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/estructura_ric.json` | `64cbd27f277f75ab4919863ed3fcd98c93238a8d9e5f7c57dd80c40487230892` | sí |
| gold | `data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json` | `1d58733699c325c90510e1ead5f18eac6c3cd970ee3b0ab7ff141da539162b40` | sí |
| harness | `data/experiment/evaluacion/harness.py` | `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e` | sí |
| manifiesto | `data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json` | `868b301fe800961804b58bf381e925ae76e442863aea8afb432ef4949e1f5ffc` | sí |

Funciones `_cita_fiel` y `_norm_loc` importadas de `data/experiment/evaluacion/harness.py`
(sin modificarlo; ruta y sha verificados en la importación).

## 3. Índice E0 por TO (decisión 5)

| TO | archivo | nodos | `numero` distintos | profundidad máxima |
|---|---|---|---|---|
| cap | `TO_capitales_minimos_actual.pdf` | 519 | 519 | 4 |
| cla | `TO_clasificacion_deudores_actual.pdf` | 162 | 162 | 4 |
| ext | `TO_exterior_cambios_actual.pdf` | 963 | 963 | 4 |
| pro | `TO_proteccion_usuarios_servicios_financieros_actual.pdf` | 113 | 113 | 4 |
| ric | `TO_regimen_informativo_contable_mensual_actual.pdf` | 107 | 107 | 4 |

Anclas del gold que resuelven en el índice E0 de su TO: **40 de 40**.

## 4. Resultados por tanda (decisión 8: tres tablas por tanda; la de contenido es la principal)

### 4.1 Tanda `ev2_r1_base` — 40 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 31 + abstención 9 + sin_json 0 = 40 (N todas = 40).

#### ev2_r1_base · todas las respuestas (N = 40)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 38 de 40 | 2 | 0 | 0 | 0 | 40 |
| 1 · cita fundada (byte-exacta) | 38 de 40 | 2 | 0 | 0 | 0 | 40 |
| 2 · cita existente (índice E0) | 40 de 40 | 0 | 0 | 0 | 0 | 40 |
| 3 · cita al punto de referencia | 32 de 40 | 8 | 0 | 0 | 0 | 40 |
| informativa · cita ancestro del ancla | 0 de 40 | 40 | 0 | 0 | 0 | 40 |

#### ev2_r1_base · solo contenido (respondible true) (N = 31)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 30 de 31 | 1 | 0 | 0 | 0 | 31 |
| 1 · cita fundada (byte-exacta) | 30 de 31 | 1 | 0 | 0 | 0 | 31 |
| 2 · cita existente (índice E0) | 31 de 31 | 0 | 0 | 0 | 0 | 31 |
| 3 · cita al punto de referencia | 28 de 31 | 3 | 0 | 0 | 0 | 31 |
| informativa · cita ancestro del ancla | 0 de 31 | 31 | 0 | 0 | 0 | 31 |

#### ev2_r1_base · solo abstención (respondible false) (N = 9)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 8 de 9 | 1 | 0 | 0 | 0 | 9 |
| 1 · cita fundada (byte-exacta) | 8 de 9 | 1 | 0 | 0 | 0 | 9 |
| 2 · cita existente (índice E0) | 9 de 9 | 0 | 0 | 0 | 0 | 9 |
| 3 · cita al punto de referencia | 4 de 9 | 5 | 0 | 0 | 0 | 9 |
| informativa · cita ancestro del ancla | 0 de 9 | 9 | 0 | 0 | 0 | 9 |

#### ev2_r1_base · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 3
  - EV2F-014: `TO_exterior_cambios_actual.pdf` / `Punto 13.3.1`
  - EV2F-023: `TO_capitales_minimos_actual.pdf` / `Punto 8.3.5`
  - EV2F-023: `TO_capitales_minimos_actual.pdf` / `Punto 8.3.4`
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.2 Tanda `ev2_r1_enc_r1` — 24 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 19 + abstención 5 + sin_json 0 = 24 (N todas = 24).

#### ev2_r1_enc_r1 · todas las respuestas (N = 24)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 1 · cita fundada (byte-exacta) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 2 · cita existente (índice E0) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 3 · cita al punto de referencia | 21 de 24 | 3 | 0 | 0 | 0 | 24 |
| informativa · cita ancestro del ancla | 0 de 24 | 24 | 0 | 0 | 0 | 24 |

#### ev2_r1_enc_r1 · solo contenido (respondible true) (N = 19)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| 1 · cita fundada (byte-exacta) | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| 2 · cita existente (índice E0) | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| 3 · cita al punto de referencia | 17 de 19 | 2 | 0 | 0 | 0 | 19 |
| informativa · cita ancestro del ancla | 0 de 19 | 19 | 0 | 0 | 0 | 19 |

#### ev2_r1_enc_r1 · solo abstención (respondible false) (N = 5)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 1 · cita fundada (byte-exacta) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 2 · cita existente (índice E0) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 3 · cita al punto de referencia | 4 de 5 | 1 | 0 | 0 | 0 | 5 |
| informativa · cita ancestro del ancla | 0 de 5 | 5 | 0 | 0 | 0 | 5 |

#### ev2_r1_enc_r1 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 0.
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

### 4.3 Tanda `ev2_r1_enc_r2` — 24 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 18 + abstención 6 + sin_json 0 = 24 (N todas = 24).

#### ev2_r1_enc_r2 · todas las respuestas (N = 24)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 23 de 24 | 0 | 0 | 1 | 0 | 24 |
| 1 · cita fundada (byte-exacta) | 23 de 24 | 0 | 0 | 1 | 0 | 24 |
| 2 · cita existente (índice E0) | 23 de 24 | 0 | 0 | 1 | 0 | 24 |
| 3 · cita al punto de referencia | 20 de 24 | 3 | 0 | 1 | 0 | 24 |
| informativa · cita ancestro del ancla | 0 de 24 | 23 | 0 | 1 | 0 | 24 |

#### ev2_r1_enc_r2 · solo contenido (respondible true) (N = 18)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 1 · cita fundada (byte-exacta) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 2 · cita existente (índice E0) | 18 de 18 | 0 | 0 | 0 | 0 | 18 |
| 3 · cita al punto de referencia | 15 de 18 | 3 | 0 | 0 | 0 | 18 |
| informativa · cita ancestro del ancla | 0 de 18 | 18 | 0 | 0 | 0 | 18 |

#### ev2_r1_enc_r2 · solo abstención (respondible false) (N = 6)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 5 de 6 | 0 | 0 | 1 | 0 | 6 |
| 1 · cita fundada (byte-exacta) | 5 de 6 | 0 | 0 | 1 | 0 | 6 |
| 2 · cita existente (índice E0) | 5 de 6 | 0 | 0 | 1 | 0 | 6 |
| 3 · cita al punto de referencia | 5 de 6 | 0 | 0 | 1 | 0 | 6 |
| informativa · cita ancestro del ancla | 0 de 6 | 5 | 0 | 1 | 0 | 6 |

#### ev2_r1_enc_r2 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 0.
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 1 — EV2F-026
- Respuestas `sin_json`: 0.

### 4.4 Tanda `ev2_r1_enc_r3` — 24 trazas

Respuestas sin JSON final (`sin_json`, conteo aparte): 0. Contenido 19 + abstención 5 + sin_json 0 = 24 (N todas = 24).

#### ev2_r1_enc_r3 · todas las respuestas (N = 24)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 1 · cita fundada (byte-exacta) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 2 · cita existente (índice E0) | 24 de 24 | 0 | 0 | 0 | 0 | 24 |
| 3 · cita al punto de referencia | 21 de 24 | 3 | 0 | 0 | 0 | 24 |
| informativa · cita ancestro del ancla | 0 de 24 | 24 | 0 | 0 | 0 | 24 |

#### ev2_r1_enc_r3 · solo contenido (respondible true) (N = 19)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| 1 · cita fundada (byte-exacta) | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| 2 · cita existente (índice E0) | 19 de 19 | 0 | 0 | 0 | 0 | 19 |
| 3 · cita al punto de referencia | 17 de 19 | 2 | 0 | 0 | 0 | 19 |
| informativa · cita ancestro del ancla | 0 de 19 | 19 | 0 | 0 | 0 | 19 |

#### ev2_r1_enc_r3 · solo abstención (respondible false) (N = 5)

| indicador | sí | no | fuera_de_indice | sin_citas | sin_json | N |
|---|---|---|---|---|---|---|
| 1 · cita fundada (normalizada, principal) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 1 · cita fundada (byte-exacta) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 2 · cita existente (índice E0) | 5 de 5 | 0 | 0 | 0 | 0 | 5 |
| 3 · cita al punto de referencia | 4 de 5 | 1 | 0 | 0 | 0 | 5 |
| informativa · cita ancestro del ancla | 0 de 5 | 5 | 0 | 0 | 0 | 5 |

#### ev2_r1_enc_r3 · listas una por una

- Citas no fundadas (lectura normalizada, indicador 1): 0.
- Citas no fundadas solo en la lectura byte-exacta (fundadas bajo normalización): 0.
- Citas no existentes en el índice E0 (indicador 2): 0.
- Citas `fuera_de_indice` (más profundas que el índice de su TO): 0.
- Citas no parseables (decisión 3): 0.
- Respuestas `sin_citas`: 0.
- Respuestas `sin_json`: 0.

## 5. Conciliación con U-CITA (criterios b, c, d)

Cifras previas: `reports/inventario_UCITA.md` §4 (trazas, citas parseables,
respuestas con cita parseable, abstenciones de la base) y §5 (citas no vistas).
Las re-corridas no traen cifra previa de abstenciones: se reporta el conteo.

| medida | ev2_r1_base | ev2_r1_enc_r1 | ev2_r1_enc_r2 | ev2_r1_enc_r3 |
|---|---|---|---|---|
| trazas | 40 ✓ | 24 ✓ | 24 ✓ | 24 ✓ |
| citas totales | 98 | 67 | 63 | 62 |
| citas parseables | 98 ✓ | 67 ✓ | 63 ✓ | 62 ✓ |
| respuestas con ≥ 1 cita parseable | 40 ✓ | 24 ✓ | 23 ✓ | 24 ✓ |
| contenido (respondible true) | 31 | 19 | 18 | 19 |
| abstenciones (respondible false) | 9 ✓ | 5 | 6 | 5 |
| sin_json | 0 | 0 | 0 | 0 |
| sin_citas | 0 | 0 | 1 | 0 |
| citas no fundadas (normalizada) | 3 ✓ | 0 ✓ | 0 ✓ | 0 ✓ |
| citas no fundadas (byte-exacta) | 3 | 0 | 0 | 0 |
| citas no existentes | 0 | 0 | 0 | 0 |
| citas fuera_de_indice | 0 | 0 | 0 | 0 |
| citas no parseables | 0 | 0 | 0 | 0 |
| control indicador 1: trazas con discrepancia | 0 | 0 | 0 | 0 |

«✓» = coincide con la cifra de U-CITA; entre paréntesis, la cifra de U-CITA cuando difiere; sin marca, sin cifra previa.

Trazas con citas no fundadas (normalizada), por tanda:
- ev2_r1_base: EV2F-014 (1), EV2F-023 (2)
- ev2_r1_enc_r1: ninguna
- ev2_r1_enc_r2: ninguna
- ev2_r1_enc_r3: ninguna

Diferencias con las cifras de U-CITA: 0.

Control del indicador 1 (recómputo vs. `citations_unseen_normalized` / `citations_unseen_raw` persistidos): **0 discrepancias** en 112 trazas.

## 6. Salidas y reproducción

- `reports/ucita2_indicadores.json` — sha256 `a9d32d3b7fed467e416c6145a5eae397ceedf930d7506bef2432dbdbc42e4355` (este .md se renderiza desde ese archivo).
- Comando (desde la raíz del repo):

```
PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/ucita2_indicadores.py
```

- Selftest de respuesta conocida: `PYTHONDONTWRITEBYTECODE=1 python3 -B scripts/ucita2_indicadores.py --selftest`.
- Determinismo: el JSON no lleva timestamps; dos corridas consecutivas producen el mismo sha256.
