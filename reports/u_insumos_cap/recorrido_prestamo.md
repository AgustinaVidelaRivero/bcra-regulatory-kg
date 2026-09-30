# U-INSUMOS-CAP · I2 — Recorrido del ejemplo del préstamo por componente

Insumo citable para el capítulo 4 (mesa de escritura). No es prosa de la tesis.

Regenerar (desde la raíz del repo; doble corrida byte a byte idéntica):

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i2.py
```

Ejemplo: `cla::5.1.1.1` → `cla::3.7` sobre KG-Reextraído-r1 (`0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a`). Pregunta: la de `docs/tesis/figuras/ejemplo_prestamo_datos.json` → `pregunta`. Solo artefactos existentes: lo que no existe queda NO ENCONTRADO y no se genera. Los extractos son verbatim, con los saltos de línea como espacio, las palabras partidas por guion reunidas y cortados con «…».

**Declaración (decisión 5 del mandato).** Después de la re-extracción de la tanda 0 (U-REEXT-T0), todos los datos de este recorrido quedan como datos de KG-Reextraído-r1: describen la corrida que produjo r1, no el pipeline vigente en ese momento.

## 0. Tabla de componentes

| componente | estado | artefacto principal |
|---|---|---|
| E0 (chunks) | ENCONTRADO | data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json:2677 (id `cla::5.1.1.1`) |
| E1 (salida cruda y validación) | ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_e1.jsonl:61 (`cla::5.1.1.1`, primer intento) |
| E3 (veredicto y reintento) | ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida/cla/veredictos.jsonl:68 (intento 0, `faltantes_detectados`) |
| Extracción final | ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_finales_cla.jsonl:61 (`cla::5.1.1.1`, estado_e3 `aceptado_tras_reintento`) |
| E2 | ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida/cla/grafo_cla.json: nodes [113], [298], [357], [438], [494] |
| E4 | NO ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida_r1/e4_propuestos.json: 0 menciones de los 5 ids o de los 2 chunks |
| Esqueleto | ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json: edges [17583], [17592], [17597], [17662], [17665], [17720] |
| Referencias y procedencia de r1 | ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_remisiones.json: [984], [985] |
| Grafo final | ENCONTRADO | data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json:170780 (nodo operacion) |
| Agente (trazas umed2) | ENCONTRADO | reports/u_med_ejemplo/umed2_analista_paso4_traza_c1.json |
| Juez | NO ENCONTRADO | reports/u_med_ejemplo/umed2_analista_paso4_agente.py:3 («sin juez») |
| Atribución A0.2 | NO ENCONTRADO | data/experiment/ev2_reporte/regla_atribucion.md:28 (la regla atribuye contra el veredicto de cada traza) |
| Indicadores de cita | NO ENCONTRADO | scripts/ucita2_indicadores.py:5 (corre sobre las 112 trazas de EV2 de r1) |

## 1. E0 (chunks) — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json:2677 (id `cla::5.1.1.1`)
- data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json:2315 (id `cla::3.7`)

Extracto:

- cla::5.1.1.1: «5.1.1.1. Los créditos para consumo o vivienda. Los créditos de esta clase que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7. y…»
- cla::3.7: «3.7. Importe de referencia. El importe a considerar será el nivel máximo del valor de ventas totales anuales para la categoría “Micro” correspondiente al sector “Comerci…»

**Lo que muestra el ejemplo:** 5.1.1.1 es una unidad propia (punto_terminal, página 16, 354 caracteres) que hereda el encabezado y el intro de 5.1.1 («Abarca todas las financiaciones comprendidas, con excepción de las siguientes:»); 3.7 es otra unidad (punto_terminal, página 14). La remisión «punto 3.7.» está solo en `texto`: ningún otro campo del chunk la registra. Flags de tabla o fórmula en True en los dos chunks: 0 de 4.

Control: chunks_cla.json de salida_enm01 y de salida_tanda0 byte-idénticos: sí.

## 2. E1 (salida cruda y validación) — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_e1.jsonl:61 (`cla::5.1.1.1`, primer intento)
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_e1.jsonl:51 (`cla::3.7`)
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/resumen_e1.json → cliente.cache_stats.namespace = `e1_extraccion|cv=e1-extractor-v1-p4793d6152608|think=0`

Extracto:

- Operacion «Créditos para consumo o vivienda»
- Restriccion «Exclusión de cartera comercial — créditos consumo/vivienda con repago no vinculado a ingresos fijos»
- Restriccion «Inclusión cartera comercial — créditos consumo/vivienda superiores a dos veces referencia»
- relaciones: Operacion establecida_en TextoOrdenado, Restriccion establecida_en TextoOrdenado, Restriccion establecida_en TextoOrdenado, Restriccion limita Operacion, Restriccion limita Operacion, Restriccion aplica_a Sujeto(catálogo), Restriccion aplica_a Sujeto(catálogo)
- validación: rechazos 0, advertencias ['label_largo'], métricas 4→4 entidades, 7→7 relaciones

**Lo que muestra el ejemplo:** El primer intento sobre 5.1.1.1 emitió 3 entidades de contenido (Operacion, Restriccion, Restriccion) y 7 relaciones, con `aplica_a` desde las dos Restriccion; la validación aceptó 7 de 7 (advertencias: 1). Sobre 3.7 emitió Obligacion con 2 relaciones.

## 3. E3 (veredicto y reintento) — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida/cla/veredictos.jsonl:68 (intento 0, `faltantes_detectados`)
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/veredictos.jsonl:69 (intento 1, `completo_ok`)
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/veredictos.jsonl:58 (`cla::3.7`, `completo_ok`)
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/finales.jsonl:61 (estado `aceptado_tras_reintento`, reintentos 1)
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/finales.jsonl:51 (`cla::3.7`, estado `completo_ok_directo`)
- data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db, fila de `cache` con key `cd6115a9b442c4a1…` (created_at 2026-08-11T14:26:08, claude-haiku-4-5-20251001; archivo fuera de git, data/experiment/reextraccion_v2/e3_verificador/.gitignore:1; leído con immutable=1)

Extracto:

- nota del veredicto (intento 0): «el fuente exige AMBAS condiciones conjuntamente (superar el umbral Y repago no vinculado a ingresos fijos) para incluir el crédito en cartera comercial; lo extraído las partió en dos restricciones independientes (e2 e3), cada una suficiente por sí sola, lo que altera el criterio de inclusión: la norma es una condición compuesta, no dos alternativas»
- severidad alta, bloqueante sí
- rechazo de la validación del reintento: firma_invalida «relations[5]: Operacion --aplica_a--> Sujeto»

**Lo que muestra el ejemplo:** E3 objetó el primer intento (bloqueante); tras 1 reintento la re-verificación dio `completo_ok`. El reintento cambió la etiqueta de la Operacion («Créditos para consumo o vivienda» → «Inclusión en cartera comercial — créditos consumo/vivienda») y quitó «se incluirán dentro de la cartera comercial» de las descripciones de las Restriccion (presente en 2 de 2 → 0 de 2); la forma quedó igual: 2 `limita` Restriccion→Operacion antes (2) y después (2, iguales: sí). La validación del reintento rechazó `aplica_a` Operacion→Sujeto (firma_invalida), así que 5.1.1.1 queda sin `aplica_a`. 3.7 pasó sin reintento (`completo_ok_directo`). En la caché, el crudo del reintento trae ese `aplica_a`: sí; mismas etiquetas que la validación final: sí.

## 4. Extracción final — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_finales_cla.jsonl:61 (`cla::5.1.1.1`, estado_e3 `aceptado_tras_reintento`)
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_finales_cla.jsonl:51 (`cla::3.7`, estado_e3 `completo_ok_directo`)

Extracto:

- cla::5.1.1.1: Operacion establecida_en TextoOrdenado, Restriccion establecida_en TextoOrdenado, Restriccion establecida_en TextoOrdenado, Restriccion limita Operacion, Restriccion limita Operacion
- cla::3.7: Obligacion establecida_en TextoOrdenado, Obligacion aplica_a Sujeto(catálogo)

**Lo que muestra el ejemplo:** La validación guardada es la misma que `validacion_final` de finales.jsonl: sí. 5.1.1.1 entra a E2 con 3 nodos de contenido y 5 relaciones, ninguna `aplica_a`; 3.7 entra con `aplica_a` al sujeto de catálogo `Sujeto_rol_obligado_a_clasificar_clasificacion`, sin `sujeto_propuesto`.

## 5. E2 — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida/cla/grafo_cla.json: nodes [113], [298], [357], [438], [494]
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/grafo_cla.json: edges [805], [591], [229]
- data/experiment/reextraccion_v2/corpus_v2/salida/cla/reporte_e2_cla.json → `fanin`, `stats`, `edges_by_relation`
- data/experiment/reextraccion_v2/corpus_v2/r1_comun.py:97 (r1 lee grafo_<to>.json)

Extracto:

- limita restriccion_monto → operacion: edges[805]
- limita restriccion_repago → operacion: edges[591]
- referencia restriccion_monto → obligacion_3_7: ausente
- aplica_a obligacion_3_7 → sujeto: edges[229]
- fanin cla: 140 aceptados de 143; merges_exactos 165; aristas referencia en el grafo del TO: 1

**Lo que muestra el ejemplo:** E2 ya tiene los 5 nodos con los mismos ids que r1 y 3 de las 4 aristas del ejemplo; falta la `referencia`, que agrega r1.

## 6. E4 — NO ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida_r1/e4_propuestos.json: 0 menciones de los 5 ids o de los 2 chunks
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/e4_conflictos.json: 0 menciones de los 5 ids o de los 2 chunks
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/e4_texto_ordenado.json: 0 menciones de los 5 ids o de los 2 chunks

Extracto:

- e4_texto_ordenado.json → canonicos.cla = `TextoOrdenado_to_clasificacion_deudores_actual_pdf` (destino de las `establecida_en` del punto; no es nodo del ejemplo)

**Lo que muestra el ejemplo:** Ningún nodo ni chunk del ejemplo pasa por E4: el sujeto es de catálogo (no hay `sujeto_propuesto`) y ningún nodo del ejemplo figura en conflictos ni en propuestos.

## 7. Esqueleto — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json: edges [17583], [17592], [17597], [17662], [17665], [17720]
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/e5_esqueleto.json → `aristas_esqueleto_agregadas` = 82 (total de r1)
- data/experiment/reextraccion_v2/corpus_v2/r1_e5_esqueleto.py:12 (procedencia `esqueleto`)

Extracto:

- edges[17583]: Sujeto_entidad_financiera miembro_de Sujeto_rol_obligado_a_clasificar_clasificacion · punto «Secciones 1 y 10»
- edges[17592]: Sujeto_fiduciario_de_fideicomiso_financiero miembro_de Sujeto_rol_obligado_a_clasificar_clasificacion · punto «Secciones 1 y 10»
- … y 4 más con la misma forma

**Lo que muestra el ejemplo:** El sujeto del ejemplo recibe 6 aristas `miembro_de` del esqueleto, sin chunk; los cuatro nodos de contenido del ejemplo tienen 0 aristas de esqueleto.

## 8. Referencias y procedencia de r1 — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_remisiones.json: [984], [985]
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json: edges [15773] (referencia_cruzada)
- data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:73 (`_texto`: label + propiedades del nodo)
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/provenance_verificacion.json → `resumen`, `inconsistencias`

Extracto:

- [984] clase interna, evidencia «ente a dos veces el importe de referencia establecido en el punto 3.7. | 2x importe refere», destino cla::3.7 (1 nodo)
- [985] clase interna, evidencia «rencia establecido en el punto 3.7. | 2x importe referencia punto 3.7», destino cla::3.7 (1 nodo)
- procedencia de la restricción del monto: chunk cla::5.1.1.1, páginas [16], ancestros ['S5', '5.1', '5.1.1']

**Lo que muestra el ejemplo:** El detector de r1 leyó la paráfrasis del nodo, no el texto de E0: 2 detecciones sobre `descripcion` y `umbral` de la restricción del monto, 1 arista `referencia` en kg.json. La Operacion y la restricción del repago no tienen `referencia` (0). provenance_verificacion: inconsistencias de estructura 0; menciones de los ids del ejemplo en `inconsistencias`: 0.

## 9. Grafo final — ENCONTRADO

Artefactos:

- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json:170780 (nodo operacion)
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json:245421 (nodo restriccion_monto)
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json:210159 (nodo restriccion_repago)
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json:48743 (nodo obligacion_3_7)
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json:288632 (nodo sujeto)
- data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json: edges [15772], [12389], [15773], [3941]
- reports/u_med_ejemplo/umed2_analista_paso2_resultado.json → `comparacion`

Extracto:

- edges[15772]: restriccion_monto limita operacion · rol_fuente None · chunk cla::5.1.1.1
- edges[12389]: restriccion_repago limita operacion · rol_fuente None · chunk cla::5.1.1.1
- edges[15773]: restriccion_monto referencia obligacion_3_7 · rol_fuente referencia_cruzada · chunk cla::5.1.1.1
- edges[3941]: obligacion_3_7 aplica_a sujeto · rol_fuente None · chunk cla::3.7

**Lo que muestra el ejemplo:** En r1 el ejemplo son 5 nodos y 4 aristas: 2 `limita` y 1 `aplica_a` de extracción, 1 `referencia` de r1. Las 681 aristas incidentes a los nodos del ejemplo son iguales en kg.json y en Neo4j: sí.

## 10. Agente (trazas umed2) — ENCONTRADO

Artefactos:

- reports/u_med_ejemplo/umed2_analista_paso4_traza_c1.json
- reports/u_med_ejemplo/umed2_analista_paso4_traza_c2.json
- reports/u_med_ejemplo/umed2_analista_paso4_traza_c3.json
- reports/u_med_ejemplo/umed2_analista_paso4_analisis.json (corridas 1–3)
- reports/u_med_ejemplo/umed2_analista_paso4_analisis_consola.txt:29,73,117 («abrio 3.7: False»)
- reports/u_med_ejemplo/umed2_analista_paso4_resumen.json → `costo_total_usd` = 0.064962

Extracto:

- corrida 1, ítem 3 de la respuesta: «**Superación del umbral**: Los créditos para consumo o vivienda que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7 deben ser clasificados en la cartera comercial.»
- corrida 2, ítem 3 de la respuesta: «**Restricción por monto**: Los créditos para consumo o vivienda que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7 no se incluyen en la cartera comercial.»
- corrida 3, ítem 3 de la respuesta: «**Restricción por monto**: Los créditos para consumo o vivienda que superen el equivalente a dos veces el importe de referencia establecido en el punto 3.7 no se incluyen en la cartera comercial bajo estas condiciones de agrupamiento.»

**Lo que muestra el ejemplo:** Tres corridas de 12 llamadas; secuencia idéntica en las tres: sí. Abren nodos de 5.1.1.1 y ven la Obligacion del 3.7 como vecina por `referencia` en las llamadas 6, 12 (corrida 1), sin abrirla en ninguna corrida (3 de 3). Respuestas que mencionan el repago: 0 de 3; que mencionan «Micro» o «ventas» (contenido del 3.7): 0 de 3. El ítem 3 dice que esos créditos van a la cartera comercial en la corrida 1 y que no se incluyen en las corridas 2 y 3 (extracto). Citas: Punto 5.1.1.1, Punto 5.1.1.2.

## 11. Juez — NO ENCONTRADO

Artefactos:

- reports/u_med_ejemplo/umed2_analista_paso4_agente.py:3 («sin juez»)
- claves de veredicto en las tres trazas: 0

**Lo que muestra el ejemplo:** No hay veredicto del juez sobre ninguna de las tres respuestas.

## 12. Atribución A0.2 — NO ENCONTRADO

Artefactos:

- data/experiment/ev2_reporte/regla_atribucion.md:28 (la regla atribuye contra el veredicto de cada traza)
- menciones de «umed2» en data/experiment/ev2_reporte/salida, data/experiment/ev2_tanda0: 0

**Lo que muestra el ejemplo:** La regla A0.2 pide el veredicto de la traza, que no existe; no se aplicó a estas trazas.

## 13. Indicadores de cita — NO ENCONTRADO

Artefactos:

- scripts/ucita2_indicadores.py:5 (corre sobre las 112 trazas de EV2 de r1)
- reports/ucita2_indicadores.json: menciones de «umed2» = 0

Extracto:

- reports/u_med_ejemplo/umed2_analista_paso4_analisis.json → `citas_no_vistas_normalizadas` = [[], [], []] (campo del harness, no un indicador de U-CITA-2)

**Lo que muestra el ejemplo:** Los tres indicadores de cita no se computaron sobre estas trazas; el indicador 3 necesita el ancla de una clave de EV2, que esta pregunta no tiene.

## 14. Dependencias con las figuras

Las cuatro figuras del ejemplo leen `docs/tesis/figuras/ejemplo_prestamo_datos.json` (sha256 `25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2`), que escribe `docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py` (sha256 `4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7`). Las otras figuras de `docs/tesis/figuras/` no usan el ejemplo. Los LEEME tienen cambios sin commit desde antes de esta unidad; se leyó el working tree (sha256 abajo).

| figura | LEEME (sha256 del working tree) | datos del ejemplo que usa | candado |
|---|---|---|---|
| 1.1 norma a grafo | `docs/tesis/figuras/LEEME_figura_norma_a_grafo.md` (`0ef695f0a51c…`) | textos de 5.1.1, 5.1.1.1 y 3.7; frase resaltada; 5 nodos; 4 aristas | `docs/tesis/figuras/generar_figura_norma_a_grafo.py:239` compara el sha de kg.json con el del JSON y cada nodo y arista contra kg.json |
| 1.2 fragmentos vs grafo | `docs/tesis/figuras/LEEME_figura_fragmentos_vs_grafo.md` (`9d61809efc43…`) | pregunta; textos; puestos 2 y 1.523 y top-5 de BM25; nodos y aristas | `docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py:565` importa la carga de 1.1; con `--verificar-busqueda`, `:539` exige el sha de los cinco chunks_*.json y los puestos |
| 1.3 proceso de extracción | `docs/tesis/figuras/LEEME_figura_proceso_extraccion.md` (`077b60990827…`) | 3 nodos (restricción del monto, obligación del 3.7, operación); aristas 15772 y 15773 | `docs/tesis/figuras/generar_figura_proceso_extraccion.py:53` (KG_SHA256 fijo) |
| 2.1 tripleta | `docs/tesis/figuras/LEEME_figura_tripleta.md` (`010f8012c1ba…`) | 2 nodos (restricción del monto, operación); arista 15772 | `docs/tesis/figuras/generar_figura_tripleta.py:65` (KG_SHA256 fijo) |

En el extractor, los candados son: el sha256 de r1 (`docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py:48`); la ruta de E0 `salida_enm01` (`:49`); los nodos buscados por tipo y etiqueta literal (`:75`); las aristas por (origen, relación, destino) (`:87`); los puestos esperados de BM25 (`:97`); y el sha de los resultados de U-MED-EJEMPLO-2 (`:55`).

**Qué cambiaría después de U-REEXT-T0.** El mandato de U-REEXT-T0 es NO ENCONTRADO en `docs/mandatos/` al redactar esto; su alcance está en `docs/plan_tesis.md:399` (HEAD `ded3494`): E0 a E5 de los diez TOs con el prefijo nuevo, sobre el corpus congelado. Hechos:

- Las figuras leen r1 por ruta y sha fijos (`docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py:47-48`): U-REEXT-T0 no las cambia por sí mismo, porque r1 está sellado y no se reescribe. Para mostrar el grafo nuevo hay que re-apuntar el extractor; entonces fallan por diseño el candado de sha, la búsqueda por etiqueta literal y los índices de arista, que son salida de la extracción y del ensamblado de r1.
- El único grafo existente con el esquema congelado sobre esos dos puntos es KG-Tanda0-Desarrollo-r1 (`data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json`, `eab2fdd01dec…`, prompt v3; no es U-REEXT-T0). Allí los nodos de contenido son: cla::3.7 Definicion «Importe de referencia»; cla::5.1.1.1 Condicion «Monto supera dos veces importe referencia 3.7»; cla::5.1.1.1 Condicion «Repago vinculado a actividad productiva/comercial»; cla::5.1.1.1 Definicion «Cartera comercial — créditos consumo/vivienda»; cla::5.1.1.1 Operacion «Clasificación de crédito en cartera comercial». No hay Restriccion ni `limita`; aristas `referencia` de 5.1.1.1 hacia 3.7: 0; Condicion del ejemplo sin ninguna arista: 2 de 2. Con ese grafo, las figuras 1.1, 1.3 y 2.1 (Restriccion, `limita` y `referencia`) no se reproducen. Ya está registrado en `docs/laudo_release_r2_pipeline.md:332` (Condicion sin aristas) y `:334` (el ejemplo como test de la suite, que hoy daría «persiste» en ese grafo), en HEAD `ded3494`.
- Los textos y la búsqueda BM25 salen de los cinco chunks_*.json de `salida_enm01`, por ruta fija. Los puestos 2 y 1.523 dependen de los 1.763 fragmentos (idf y largo medio): si U-REEXT-T0 cambia algún fragmento de los cinco TOs y las figuras pasan a leer esa salida, los puestos se recalculan.
- Las trazas del agente, el Paso 2 y el Paso 3 de U-MED-EJEMPLO-2 son de r1 y no se rehacen. La figura 1.2 no dibuja una traza del agente: lo declara `docs/tesis/figuras/LEEME_figura_fragmentos_vs_grafo.md:22` (working tree).

## 15. Fuentes (sha256)

| archivo | sha256 |
|---|---|
| `data/experiment/reextraccion_v2/e0_chunking/salida_enm01/chunks_cla.json` | `98808886a406d8321c678836a55f92eea983d594d95358dd21ceb537487ac0b1` |
| `data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_e1.jsonl` | `3346f7fbd6fff7869fb07baafa2497af90b4047a597169337b547f6f6d825f45` |
| `data/experiment/reextraccion_v2/corpus_v2/salida/cla/veredictos.jsonl` | `92712cf9ae07509c65d6aaf04f1ea97fdedf20e814d18eb71476b4aac0ae8ba9` |
| `data/experiment/reextraccion_v2/corpus_v2/salida/cla/finales.jsonl` | `961d99689bd007f73ad76a4944a623910d0605778ca060deed854929e5c9d893` |
| `data/experiment/reextraccion_v2/corpus_v2/salida/cla/extracciones_finales_cla.jsonl` | `dfcb4643ecd24d63869430f954db459bd0bdb6c3bba6244f4c7d758fa3382dcf` |
| `data/experiment/reextraccion_v2/corpus_v2/salida/cla/grafo_cla.json` | `7163397791b1d75901f1224ccfd7ce3cdd091043accc21d02c6ff1f7d0ae9934` |
| `data/experiment/reextraccion_v2/corpus_v2/salida/cla/reporte_e2_cla.json` | `6d35771942a89f792a2d7db56018dcc01e74c9ee83a5f8d815ff4d14fee70db5` |
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` |
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/e5_esqueleto.json` | `831b1314b382135decf61687cf84014a21f0cf6098bf67803fd680fed91886bb` |
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_remisiones.json` | `038efe4b5dee71f20d94f5acc4691ae822faa8f9780ff5c0945fd8dfc68da5d4` |
| `data/experiment/reextraccion_v2/corpus_v2/salida_r1/provenance_verificacion.json` | `b5154ba2d42804bf5350f8a9247a2671dd34e408317ba2031bfc0083bd124987` |
| `data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json` | `eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef` |
| `reports/u_med_ejemplo/umed2_analista_paso4_traza_c1.json` | `e8170ccbd5770fe8c259bf7a6f855c76eb316b8dbbd2d56d43f618fe3c812736` |
| `reports/u_med_ejemplo/umed2_analista_paso4_traza_c2.json` | `ce90dd4725305a2251c2154e329b82a67f1cce5fc5d0b9b93e2658c9591facab` |
| `reports/u_med_ejemplo/umed2_analista_paso4_traza_c3.json` | `e340f9c5fb910fc70c7bed19dfd22b7dc3d3ef20a2a46330fda78b7b48ac874e` |
| `reports/u_med_ejemplo/umed2_analista_paso4_analisis.json` | `b6cab1c6e47041960abacf65071dbd4b4be3917a3a5c188b2128e2a41b798f2a` |
| `reports/u_med_ejemplo/umed2_analista_paso4_resumen.json` | `add0f683bb0d8057f84ea0ba784ec6dfb43023eb6a4a3e61dc710ad2d3014718` |
| `reports/u_med_ejemplo/umed2_analista_paso2_resultado.json` | `3d120f6dc2a756738414ef25c823678851c84b73316b9e529eff2b26cf0b6402` |
| `docs/tesis/figuras/ejemplo_prestamo_datos.json` | `25ab7b4c0d76fd735244fe0fecc17ceaba1b0e8bfd2312e7aa3cbd5c849672a2` |
| `docs/tesis/figuras/extraer_datos_ejemplo_prestamo.py` | `4c3a441972d27304b6d58d0664dbc15b893bce7ad3e7d2d49afad947f51eeea7` |
| `docs/tesis/figuras/generar_figura_norma_a_grafo.py` | `9b0e45a299a0a078d250ccc999d192cbb83038bd8c00baa6bd8972d021b73f3d` |
| `docs/tesis/figuras/generar_figura_fragmentos_vs_grafo.py` | `0e7c379d71e4cda0192e26320d4f24ad4a26dc35a3da047bcbac8309412d43ad` |
| `docs/tesis/figuras/generar_figura_proceso_extraccion.py` | `6a91931abeb9927842f76fa50471497e926c69fc56617c62ef7f05ddf6c010d6` |
| `docs/tesis/figuras/generar_figura_tripleta.py` | `0bd7ba14c8460d8c033f57511b4ccefef051f7b81743309cea49ef9809ba5c4f` |
| `docs/tesis/figuras/LEEME_figura_norma_a_grafo.md` | `0ef695f0a51cf70f1989b5a612753f93006af1ff34e6d1db9ca61231a7930e7f` |
| `docs/tesis/figuras/LEEME_figura_fragmentos_vs_grafo.md` | `9d61809efc43ea9194e32f1a8178b7617764f19ff8bf7147f42200662eddec43` |
| `docs/tesis/figuras/LEEME_figura_proceso_extraccion.md` | `077b609908279c3dee0dbd8b23290224355f54310d305c5e606f1fc2e7d2edab` |
| `docs/tesis/figuras/LEEME_figura_tripleta.md` | `010f8012c1baf9bc3fb57f956722d30e296e86e388b0c9cc595b862126741d16` |

La caché `data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db` no está en git (`data/experiment/reextraccion_v2/e3_verificador/.gitignore:1`) y cambia con corridas posteriores; se cita por la key de la fila, no por el sha del archivo.

