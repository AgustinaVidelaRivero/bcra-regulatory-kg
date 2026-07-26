# Protocolo de medición — Escalón 1: run_3 vs grafo_v2

**Estado:** para sellado por commit previo a toda corrida. Al sellarse, predicciones y reglas de lectura quedan congeladas.
**Pregunta:** ¿el esquema v2 (catálogo cerrado de sujetos + jerarquía + roles por TO) mejora la fidelidad de las respuestas del agente respecto del esquema v1 (run_3), todo lo demás constante?

## 0. Custodia de los brazos (precondición de sellado)

- Brazo v1: `run_3_ppf_core/kg.json` (baseline congelado de siempre).
- Brazo v2: `grafo_v2/kg.json` **con su séquito commiteado en la rama**: cuarentena.json, sujetos_sospechosos.json, triage_sospechosos_U5.json (adjudicación firmada — misma jerarquía documental que un FIRMADO) e informes U5. **HASH del commit del brazo v2: `11f0d4a` (completar al sellar; sin hash no hay sellado).**
- Laudo A ratificado y su fundamento: se mide el grafo CRUDO del extractor, sin ninguna corrección del backlog (31 VP adjudicados viajan como anexo, no como ediciones). Esto preserva el refinamiento como etapa propia y medible dentro del marco de calidad por etapas — cada mejora, su experimento. La comparación de esquemas no se contamina con correcciones manuales.

## 1. Variable única y congelamientos

Cambia solo el grafo. Congelados e idénticos para ambos brazos: corpus (subset byte-idéntico), harness y sus 3 tools (incluidos índice léxico actual y límite 40 de ver_vecinos — defectos H1-H4 documentados, NO se corrigen), agente (mismo modelo y prompt), juez congelado (v2.1.1 con calibradores), presupuesto de pasos. Ninguna iteración de prompts durante la medición; fallas técnicas se reparan, se registran, y la pregunta afectada se re-corre completa.

## 2. Conjunto de evaluación EV1: nuevo, ciego, formato CQN2, sellado

- CQ/CQN/CQN2 quemadas; no se reutilizan.
- Generación ciega: instancia separada con acceso únicamente a los 5 TOs (sha256 de cada PDF verificado contra el subset congelado, seed registrada), sin acceso a repo, grafos, esquemas ni este protocolo.
- **Formato = formato CQN2**: cada entrada del set sellado contiene {id, pregunta, tos_fuente, familia, respuesta_propuesta_del_generador (con punto/cita)}. El tos_fuente habilita la guarda de dominio del verificador exploratorio y alimenta las fichas de adjudicación manual.
- **N = 36, mezcla sellada:** 10 puntuales · 12 enumerativas · 8 condicionales/con cláusulas · 6 de sujeto específico ("¿a quién aplica X?").
- Chequeo anti-solapamiento: EV1 se compara determinísticamente (similitud de texto) contra los conjuntos quemados; los solapados se descartan y regeneran, con registro del conteo.
- Answer key: mi adjudicación contra los PDF ANTES de toda corrida (la respuesta del generador es propuesta, no key) → commit de sellado (key + este protocolo con el hash del §0).

## 3. Corridas

- Por pregunta × grafo: N=3 réplicas del agente, voto de mayoría (la no-determinación a temperatura 0 se maneja con réplicas, no con reglas). Total: 36 × 2 × 3 = 216 corridas.
- **Presupuesto:** estimación previa con el tracker (histórico ≈ USD 0,05/pregunta agente+juez → ≈ USD 11-13 + generación EV1). **Tope duro: USD 25.**
- Juez ciego al grafo: respuestas anonimizadas, orden aleatorizado con seed registrada.
- **Chequeo anti-fuga previo al juez:** verificación de que las respuestas anonimizadas no contienen identificadores de esquema (prefijos `Sujeto_`, ids del catálogo, vocabulario estructural del esqueleto). Si un caso los contiene: NO se edita la respuesta — se registra el riesgo de fuga y se reporta junto al resultado.

## 4. Métricas y análisis (pre-registrados)

- **Primaria:** % correcto por mayoría, global y por familia; comparación apareada por pregunta (pares run_3✗→v2✓ vs run_3✓→v2✗; McNemar descriptivo — N=36 busca dirección y concentración, no significancia).
- **Secundarias:** estabilidad de la mayoría (3-0 vs 2-1); pasos por pregunta; uso de aristas de esqueleto en las trazas de v2.
- **Atribución de fallas:** el verificador diagnóstico opera con evidencia SOLO sobre run_3 (calibración intra-esquema; lección 0/6 fuera de familia). Sobre grafo_v2 sus salidas son exploratorias, etiquetadas como tales (la guarda de dominio usa el tos_fuente del set). La atribución con peso de evidencia en v2: adjudicación manual mía de TODAS las fallas de v2, con ficha por caso (traza + PDF + tos_fuente) y ramas pre-registradas.

## 5. Predicciones selladas

- **P1:** fidelidad global v2 ≥ run_3, con mejora CONCENTRADA en "sujeto específico" y "enumerativas".
- **P2:** en preguntas que run_3 falla por causas tratadas (genérico mudo, sujeto inalcanzable), v2 mejora; las trazas de v2 muestran navegación por aristas de esqueleto.
- **P3 (controles negativos, con umbral operativo):** fabricación, quimera y fallas H1 (description no indexada) — diferencia ≤1 caso por especie entre grafos = sin diferencia material. >1 caso en cualquier especie → válvula: variable no controlada, investigar antes de concluir.
- **P4 (atribución candidata pre-registrada):** si las enumerativas NO mejoran, candidata = límite-40 sin orden de ver_vecinos (H4). Verificación: grado de los nodos rol visitados en trazas fallidas.
- **P5:** regresiones nuevas propias de v2 (p. ej., distracción por nodos de esqueleto) se documentan como hallazgo.

## 6. Reglas de lectura y válvula

Todo resultado fuera de P1-P5 fuerza volver a discusión antes de cualquier acción. El resultado se reporta completo gane quien gane; empate o derrota de v2 es resultado legítimo con análisis de causas. Nada de lo aprendido modifica retroactivamente EV1 ni re-corre brazos sueltos.

## 7. Secuencia operativa

1. Paso 0: verificar/completar el commit del brazo v2 en la rama; registrar el hash en §0.
2. Generación ciega de EV1 (instancia separada) + chequeo anti-solapamiento.
3. Adjudicación de la key contra PDF → commit de sellado (protocolo con hash + EV1 + key).
4. Estimación de presupuesto con tracker → corridas (216) → anti-fuga → juez anonimizado.
5. Tabla primaria + secundarias; adjudicación manual de fallas de v2 con fichas.
6. Lectura contra P1-P5; informe de fase. **Merge a main: después de medir e informar** (laudo registrado: el paquete cerrado — grafo + protocolo + set + key + corridas + lectura — entra a main como historia completa).
