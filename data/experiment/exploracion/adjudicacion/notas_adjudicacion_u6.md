# Notas privadas — Adjudicación U6 (25 preguntas, territorio virgen, v3_vigente)

**Estado:** adjudicación completa contra texto normativo en las anclas (corpus congelado por hash).
**Resultado global: 7 correctas · 15 parciales · 3 incorrectas.**
Estas notas son pre-diagnósticos del rol revisor. Los dictámenes de causa son de Motor 3; los laudos, míos.
⚠️ Si algo de esto se commitea al repo: sin nombres de personas reales, redacción en primera persona propia.

## 0. Estatus metodológico de la corrida (registrar ANTES de sellar)

- **Método efectivo, uniforme en las 25:** para cada pregunta se consultó el texto del TO en el ancla antes del veredicto y del feedback. Todos los veredictos son **adjudicación informada contra el ancla** — ninguno es "percepción de usuaria exigente". No hay mezcla de estatus.
- **Incidente de protocolo:** la decisión de adjudicar contra el texto (a falta de respuesta esperada en el archivo de preguntas) se tomó operativamente en U6-001 y quedó convalidada de hecho, **sin laudo formal previo**. El revisor debió frenar para laudo explícito y no lo hizo. Desviación documentada acá.
- **Estatus de los 18 feedbacks enviados al intake:** síntoma de **usuaria experta con la norma a la vista** (contenido normativo casi textual en varios casos), no síntoma orgánico naive. Consecuencias: (a) el diagnóstico de Motor 3 sobre esta cohorte opera con síntomas más informativos que los de producción → cota superior, no proxy del intake real; (b) para el pilot sin-gold, esta cohorte requiere asterisco o cohorte de contraste.
- **Auditoría de fugas en los 18 feedbacks (verificada contra transcript):** cero vocabulario de diagnóstico — sin nodos/IDs, sin tools, sin grafo/KG, sin taxonomía v5.7, sin mecanismos. PERO **5 contienen atribución de fuente del contenido erróneo** en términos normativos ("lo que respondiste corresponde a otro mecanismo/régimen/TO"): **U6-001, U6-003, U6-010, U6-011, U6-019**. Gradiente: síntoma puro < síntoma con atribución de fuente < diagnóstico. En esos 5, si Motor 3 dictamina la familia de contaminación cruzada, no es separable si la halló solo o si el síntoma la insinuó → etiquetarlos "síntoma con atribución de fuente" en la planilla y excluirlos (o analizarlos aparte) al evaluar la capacidad diagnóstica del verificador sobre esa familia. Los otros 13 son síntoma puro. Menor: U6-003 y U6-010 comentan además las citas visibles de la app (superficie de usuario, legítimo, pero contiguo a la capa de recuperación).
- **Laudo pendiente №0 (previo al sellado):** aceptar la desviación con cohorte etiquetada "síntoma informado", y decidir si se agrega mini-cohorte de contraste (4–5 casos re-ingresados con síntoma naive mínimo) para medir sensibilidad de Motor 3 a la informatividad del síntoma. Candidato a consulta con mentores.
- Trazabilidad: la secuencia completa de verificaciones (qué se buscó y qué texto del ancla se usó por pregunta) está en la conversación de esta sesión de revisión.

---

## 1. Registro por pregunta

| ID | TO | Ancla | Veredicto | Síntoma principal | Pre-diagnóstico (hipótesis, no dictamen) |
|---|---|---|---|---|---|
| U6-001 | ext | 2.7 | Incorrecta | No-respondible falso en límites mensuales + condiciones de otro mecanismo (7.3/7.4) bajo el nombre del 2.7 | Chapeau: cómputo a límites y DDJJ viven en párrafos de cierre sin numerar del 2.7; mezcla de vecindad |
| U6-002 | ext | 3.4 | Correcta | — | Labels verbosos con keywords; gemelo 9.3.12 presente sin daño |
| U6-003 | ext | 3.12.1 | Parcial | Plazo 5 días ✓ pero desde nodo de 3.16.2.2 (correcta por coincidencia); compromiso reportado = 3.16.3 genérico; omite DDJJ del mecanismo + nominación de entidad | El nodo correcto (84d7ad) apareció 1º en búsqueda y no se abrió → selección post-búsqueda; atractores semánticos 3.16 |
| U6-004 | ext | 3.16.2 | Correcta | — | Control del atractor: cuando el ancla ES 3.16, traza corta y limpia; umbral USD 100.000 en label |
| U6-005 | ext | 4.3.2 | Parcial severa | Mecanismos sin calificadores (a nombre del cliente, GAFI; excepción BOPREAL presentada como regla general) + "en ningún caso se permite billetes/custodia/terceros" declarado inexistente | Chapeau de cierre + clausura léxica (buscó "efectivo/cheque/vedado"; la norma dice "billetes / no se permite la liquidación") |
| U6-006 | ext | 5.9.5 | Correcta | — | La cláusula negativa SÍ se recuperó: excepción con nodo propio tipado y "90 días" en label, enlazada a la restricción |
| U6-007 | ext | 7.6 | Incorrecta (triple) | Situaciones: circular; vinculadas: **invertida** (dijo sí; la norma dice no salvo control de cambios); plazo: 7.1.1 en vez de "20 días hábiles desde puesta a disposición" | Los tres faltantes viven en el encabezado sin numerar del 7.6 (chapeau). Ante la ausencia, acá **confabuló** (contrastar con U6-012, que abstuvo). Hits léxicos llevaron a nodos procedimentales de Secc. 8 (SECOEXPO) |
| U6-008 | ext | 7.5.3 | Parcial | Quinto día hábil ✓; "no existe límite por servicios de deuda" — el 125% (mes corriente + 6 meses) negado | La cláusula del 125% aparece casi textual en ≥5 lugares (7.5.3, 7.8.5.1, 7.9.5, 7.11.5, 3.11.3.2) → hipótesis sobre-fusión de cláusulas repetidas rompiendo la vecindad local |
| U6-009 | ext | 10.3.2 | Parcial | Enumeración 3/10 requisitos (faltan factura, doc. transporte, consistencia, vencimiento, tope al monto facturado, 10.11) | Hub `d16a55` con **0 salientes / 0 entrantes** → estructural_kg; cobertura acotada por overlap léxico consulta-labels (clausura léxica) |
| U6-010 | ext | 3.3 | Parcial | Núcleos ✓ (vencimiento; conformidad previa salvo VPU-RIGI) + interpolación contradictoria: "intereses devengados antes del vencimiento" (regla de otro régimen) | Repetición inter-régimen (3.3/3.5/3.6/13); citas sin 3.3. Síntoma barato: autocontradicción intra-respuesta |
| U6-011 | cap | 1.4.2.1 | Parcial | Restricciones (depósitos, dividendos) ✓; plazos del 6.7.2 (riesgo de mercado: 10 días háb. + plan en 5) en vez del general (2º mes / 30 días corridos); fraseo de rama SEFyC | Inter-régimen viaja entre TOs. Agravante: remisión explícita 6.7.2→1.4.2.1 posible arista-autopista de contaminación |
| U6-012 | cap | 2.13 | Incorrecta | No-respondible falso: CCF 100/50/20 en la tabla del ancla | Contenido tabular. Buscó con los números correctos; nodo con "100" en label apareció y no se abrió; hub cuasi-huérfano (0 sal./1 entr.). **Abstención honesta** (contrastar U6-007) |
| U6-013 | cap | 5.3.1 | Correcta | — | Tres datos en labels casi textuales. Regla de descalce repetida en 5.1.1 y 5.3.1.1 como nodos SEPARADOS → repetición inofensiva cuando no se fusiona |
| U6-014 | cap | 6.4.2.1 | Parcial leve (laudo pendiente) | Enumeración 4/4 ✓ pero calificadores/modalidad despojados (garantías: ejecución segura+irrecuperables; iv es discrecional; v condicionado a no-simplificado) | Fraseo calca la tabla 4.4.3 del ric → posible provenance inter-TO (versión tabla sin calificadores le ganó a la prosa con calificadores). Verificar provenance de d5accd/3e5b85 |
| U6-015 | cap | 8.4.1.3 | Parcial | Importe: "total del saldo" en vez de "mayor saldo por banco durante el mes"; excepción v) (saldos transitorios) faltante | Regla del mayor saldo = oración intersticial sin numerar entre párrafo y lista i)–v); ítems numerados i–iv con nodo propio. Gemelo inter-TO documentado: cla 6.5.5.8 repite la lista CON variación (calificadores de supervisión consolidada) |
| U6-016 | cla | 4.6 | Parcial | Aseguradora ✓, consumo ✓, referencia ✓; gatillo colapsado: omite "falta de pago del siniestro tras plazos de póliza (180/270), reclamo no rechazado" y adelanta el cómputo | Familia RT-C6: oración con dos anclas temporales, parse plausible-incorrecto. Tokens del gold (siniestro/póliza/180/270) nunca en consultas → clausura léxica. Desempate: properties de 56f7fb |
| U6-017 | cla | 3.6 | Correcta | (matiz: "de la totalidad de los miembros" no explicitado) | Control positivo inter-régimen: variante "2,5% o importe de referencia, de ambos el menor" a centímetros (3.4.2/6.4.4/6.5.5.9) y NO contaminó |
| U6-018 | cla | 7.4 | Parcial | Umbrales 5%/10% ✓; magnitud mal: "incremento de cartera irregular" en vez de la expresión FICCt−FICCt-1−Máx(ΔFICCS;0) (ratio propio neto del sistema) | Fórmula + **anáfora rota**: label del nodo umbral dice "la expresión" y el antecedente (fórmula) no sobrevivió; generación rellenó con lectura ingenua |
| U6-019 | cla | 3.3 | Parcial severa | Aspectos 3/8; "a disposición de quién" no-respondible falso (gold: "a disposición permanente de la SEFyC", oración de cierre); relleno con gobernanza de manuales del TO pro | Triple mecanismo: enumeración incompleta + chapeau de cierre + contaminación inter-TO con fingerprint léxico ("sujeto obligado" en 126b49 = vocabulario pro). Caso ideal para testear si el verificador separa causas |
| U6-020 | ric | 6.1 | Parcial | Fecha ✓; conceptos mayor-saldo 2/3 (falta títulos de gobiernos extranjeros, 21100000); emisor de subordinados despojado | **Colisión por truncamiento de labels**: tres nodos hermanos con prefijo idéntico, diferenciación pasada la truncación; el tercero apareció y no se abrió. Predicción de U6-015 cumplida: asimetría inter-TO (alcanzable desde ric, no desde cap) |
| U6-021 | ric | 4.1.1 | Correcta | (matiz: monedas residuales código 9999 no mencionado, condicional) | Labels-oración casi completos; prosa técnica de instrucción sobrevive perfecta (SISCEN, T0003, SWIFT) |
| U6-022 | ric | 11.2.1 | Parcial | 2ª oración de monedas ✓ (pesos→a, dólares→b, >5%); 1ª oración contradictoria (mezcla coef. de actualización como monedas); dimensión "tipo de tasa" omitida | Sección más tabular del ric: prosa de instrucciones sobrevivió (nodo 96c19d textual), estructura de cuadros murió; chunk tabular visiblemente destrozado ya en extracción del PDF. 1ª oración = reconstrucción generativa sobre fragmentos rotos |
| U6-023 | pro | 2.6 | Correcta (matiz) | Condiciones exactas; omite cláusula de cierre "contratar o no será decisión del sujeto obligado"; mezcla intra-TO benigna con 2.3.12.1 | Chapeau como degradación de matiz (no falla) — el patrón es un continuo de severidad. Mezcla benigna = contraejemplo: el daño requiere repetición-CON-variación |
| U6-024 | pro | 2.7 | Parcial leve | Ubicación ✓ (destacado, visibilidad/tamaño, primer acceso); identificación diluida: "claramente identificables" en vez de leyenda obligatoria "botón de arrepentimiento"/"botón de baja" | Reconstrucción generativa de requisito con contenido específico faltante. Asimetría intra-respuesta: la mitad con contenido en label (ubicación, 34ac87) salió exacta. Vocabulario casi único en corpus → sin atractores, búsquedas con 4–21 matches |
| U6-025 | pro | 3.2.1.1 | Parcial | Jerarquía ✓, frecuencia ✓ (trimestral, Libro de Actas); comité: población invertida (dijo "no alcanzados"; es opción de los alcanzados), condición (dimensión/operatoria/clientela) y composición (≥1 director + cumplimiento + riesgo operativo + legales) omitidas | Gold en párrafo "Alternativamente..." sin numerar tras inciso ix) (chapeau); relleno desde cláusula anafórica "según corresponda" del 3.1.1.8 |

**Por TO:** ext 3/5/2 · cap 1/3/1 · cla 1/3/0 · ric 1/2/0 · pro 1/2/0.

---

## 2. Mecanismos causales hipotetizados (capa KG salvo indicación)

1. **Chapeau perdido** — prosa sin numerar (encabezado, cierre, intersticial) no sobrevive; los sub-puntos numerados sí. Instancias: U6-001, 005, 007, 015, 019, 025 (+ matiz en 023). El mecanismo con más evidencia de la corrida.
2. **Repetición-con-variación inter-régimen / inter-TO** — el corpus BCRA repite cláusulas casi textuales entre regímenes (3.3/3.5/3.6/13; 1.4.2.1 vs 6.7.2) y entre TOs (cap 8.4.1.3 vs cla 6.5.5.8; cap 6.4.2.1 vs ric 4.4.3; manuales cla vs pro). Sin desambiguación por provenance, la recuperación sirve el régimen equivocado → correcto-por-coincidencia (003), contaminado (010, 011, 019), o asimétrico (015/020). **La condición del daño es repetición-CON-variación + fusión/selección indiferente al régimen** — no la repetición per se (controles positivos: 013 duplicados separados inofensivos; 017 variante vecina sin contaminar). Las remisiones internas ("con los efectos del punto X") pueden ser aristas-autopista: tipado remisión ≠ pertenencia.
3. **Hub huérfano / conectividad** (estructural_kg) — preguntas de enumeración colapsan sin hub→satélites: d16a55 (0/0) en U6-009; cuasi en 012; sospecha en 019.
4. **Selección post-búsqueda + colisión por truncamiento de labels** — el nodo correcto aparece en resultados y no se abre (003, 012, 020); en 020 con excusa estructural: hermanos con prefijo idéntico truncados antes del contenido distintivo (pariente de la colisión de chunk_id de v2).
5. **Estructuras no-prosa** — tablas (012 CCF, 022 cuadros, sospecha 014) y fórmulas con **anáfora rota** (018: nodo dice "la expresión", antecedente ausente). Degradación visible ya a nivel chunk (022).
6. **Clausura léxica de la consulta** — el agente no puede buscar lo que no sabe que existe; sin navegación estructural, lo no-nombrado por la pregunta es inalcanzable (005 billetes, 009 factura/transporte, 016 siniestro/póliza, 019 "disposición permanente"). Complemento de BKL-0003.
7. **Capa generación** — (a) ante ausencia de KG: confabulación (007) vs abstención honesta (012) — qué modula la diferencia es pregunta abierta; (b) reconstrucción plausible sobre huecos/anáforas (018, 022, 024, 025); (c) parse de oraciones complejas, familia RT-C6 (016); (d) autocontradicción intra-respuesta como síntoma detectable sin gold (010, 022); (e) calificadores/modalidad despojados (005, 014, 020, 024).

**Regularidad madre de la corrida: sobrevive lo que cabe en un label; muere lo que necesita estructura.** Corolario observado seis veces: dato-clave-en-label ↔ correcta, traza corta.

---

## 3. Correcciones candidatas (para laudo y priorización, post-diagnóstico Motor 3)

- **C-a:** re-extracción dirigida de párrafos no numerados (chapeau) con anclaje explícito al punto contenedor.
- **C-b:** labels de cláusulas plantilla-repetitivas front-loadeando el contenido distintivo (anti-colisión de truncamiento). Barata, medible en re-test.
- **C-c:** régimen/provenance como atributo de primera clase en recuperación; tipado de aristas remisión vs pertenencia.
- **C-d:** extracción dedicada de tablas y fórmulas, o flag "contenido tabular no confiable" para que el agente module su confianza.
- **C-e:** dedup consciente de variación: nunca fusionar cláusulas casi idénticas con valores/modalidad distintos.

## 4. Desempates baratos para el diagnóstico (greps sobre kg.json / corpus)

- "billetes" en nodos con provenance 4.3.2 (¿existe la prohibición?) — U6-005.
- "125" en labels/properties: contar provenances (¿un nodo fusionado o cinco?) — U6-008.
- Aristas de `d16a55` y de `2e1cd5` (hubs) — U6-009 / U6-019.
- Properties de `56f7fb` (¿contienen el gatillo del siniestro?) — U6-016 (extracción vs generación).
- Provenance de `126b49` ("sujeto obligado") — U6-019; de `d5accd`/`3e5b85` — U6-014.
- "FICC" en kg.json — U6-018. Leyenda de botones en properties de `85c056`/`db2439` — U6-024.

## 5. Límite estructural del intake por 👎 (para discusión de Motor 2 en la tesis)

Un usuario real sin gold no marcaría 👎 las respuestas plausibles-completas-pero-erróneas (tipo U6-008, U6-014): el feedback orgánico **subrepresenta la clase de defecto más peligrosa** (plausible-permisiva). Argumento para complementar el circuito con auditoría proactiva sobre territorio virgen — que es exactamente lo que hizo U6.

## 6. Higiene de protocolo (dos incidentes, cero daño)

Dos veces mi prior de dominio contradijo al corpus y el corpus tenía razón (valuación **mensual** en 5.3.1.1; **dos tercios** en cla 3.6). Regla reafirmada: adjudicar únicamente contra el corpus congelado, nunca contra memoria del revisor. También cumplido: feedbacks redactados sin mirar citas/tools más allá de lo visible en superficie de respuesta.

## 7. Laudos pendientes (míos)

1. Criterio de completitud sobre instrumentación/excepciones no preguntadas (afecta U6-002, U6-004, U6-023) — aplicado de facto: no penalizar; formalizar.
2. U6-014: parcial leve vs correcta (modalidad despojada). Recomendación del revisor: parcial.
3. U6-023: correcta con matiz vs parcial leve (cláusula discrecional). Recomendación: correcta.
4. Severidad registrada en planilla aparte del pulgar (el 👎 es compuerta de intake, no métrica): correcta/parcial/incorrecta + qué mitad falló, por pregunta.
5. Formalizar backlog entries de los mecanismos §2 tras dictamen de Motor 3 (no antes: el verificador debe llegar solo).

## 8. Costo/telemetría lateral

Largo de traza correlaciona con dificultad de alcanzabilidad (correctas: 2–8 llamadas; falladas: hasta 12+ búsquedas con miles de matches). Métrica barata candidata para el HTML de revisión.

## Fe de erratas al §0 (2026-08-08)

El §0 declara, en su punto de trazabilidad, que "la secuencia completa de verificaciones (qué se buscó y qué texto del ancla se usó por pregunta) está en la conversación de esta sesión de revisión". Esa traza conversacional de verificación por pregunta no fue persistida a archivo: la referencia quedó apuntando a un material que ya no es recuperable. Los veredictos siguen siendo re-verificables de forma independiente contra el corpus congelado por hash y los desempates determinísticos documentados; la trazabilidad conversacional queda declarada como no disponible.
