# Hallazgos acumulados para la tesis — registro vivo

Convención: cada entrada lleva **Estado** (validado / pendiente / hipótesis),
**Evidencia** (archivo o corrida de origen, verificable en el repo),
**Alcance** (sobre qué datos vale la afirmación) y **Destino probable** en el
documento final. Solo lo *validado* puede convertirse en prosa de tesis; lo
*pendiente* sobrevive como hueco marcado hasta verificarse.

Última actualización: 2026-07-06 (era verificador v4 / Fase 2.4).

---

## H1. Grounded ≠ correct (hallazgo central)

- **Estado:** validado (documentado en Fases 2.2–2.4).
- **Evidencia:** adjudicación humana de 200 claims del frozen (8 falsos con
  cita real); trazas de la Fase 2.3 (turno exacto donde el agente convierte
  contenido real del grafo en afirmación falsa).
- **Alcance:** eval set de 23 preguntas, 5 grafos, corpus de 5 TOs del BCRA.
- **Destino:** contribución central; Resultados + Conclusiones.

## H2. Techo de la atribución automática en la frontera grafo-vs-agente

- **Estado:** validado y **reforzado por v4**.
- **Evidencia:** calibraciones v1 (2/5), v2 (1/5), v3 (2/5) y v4 (0/0/4+1
  con lectura pre-registrada), en `posthoc_run/calibracion_verificador*/`.
  Cuatro diseños de prompt distintos (incluido el rediseño completo con
  esquema, procedimiento guiado, abstención y anclaje) no pasan el umbral;
  el error cambia de forma pero no desaparece.
- **Alcance:** 5 casos-control de run_3; verificador Opus.
- **Destino:** Resultados (sección verificador) + conclusión de diseño
  (human-in-the-loop).

## H3. Perfil "investiga bien, etiqueta mal" — confirmado con instrumentación

- **Estado:** validado.
- **Evidencia:** v4: 0 quotes inventados sobre 37 verificados contra
  kg.json/PDFs/trazas (checker corregido); búsquedas documentadas correctas;
  A3 declaró correctamente "el agente actuó bien" donde correspondía
  (CQ-034); y aun así 4 etiquetas erradas. En v3 ya: CQ-020 escribió la
  evidencia correcta y etiquetó mal.
- **Alcance:** calibración v4 (5 casos), corroborado con v1–v3.
- **Destino:** Resultados; es el argumento empírico del diseño asistente-no-juez.

## H4. Sesgo de causa próxima al etiquetar (v4)

- **Estado:** validado como patrón en v4; **hipótesis** en cuanto al
  mecanismo (pregunta guía + veredictos por-claim del juez).
- **Evidencia:** CQ-020 (`calibracion_verificador_v4/CQ-020.json`): buscó el
  nodo de frecuencia, no lo encontró, y usó el no-hallazgo como prueba de
  glosa del agente (generación-de-más) en vez de prueba de dato faltante
  (completitud_kg). El razonamiento nunca evalúa si el grafo TIENE el nodo.
  Patrón consistente en CQ-017 y CQ-031 (etiquetas lado agente donde el GT
  es lado grafo).
- **Alcance:** calibración v4.
- **Destino:** Resultados (análisis de modos de fallo del verificador);
  también insumo directo de la consulta a Juan.

## H5. Dilución de instrucciones: más reglas, menos cumplimiento (v4)

- **Estado:** validado como correlación observada; hipótesis como causa.
- **Evidencia:** prompt 6.9K → 17.4K chars y: instrucción del esquema sin
  rastro en trayectorias ni razonamientos (CQ-017 verificado explícitamente);
  reglas de CONFIANZA ignoradas (alta en 4/4 contra las condiciones del
  prompt); abstención (feature central) usada 0 veces; CQ-034 rompió el
  contrato JSON con campos inventados.
- **Alcance:** calibración v4 (una corrida, 5 casos).
- **Destino:** Discusión metodológica (límites del prompting); consulta a Juan.

## H6. CQ-031: el dato existe pero es léxicamente inalcanzable

- **Estado:** validado el hecho mecánico; **pendiente** la decisión de
  taxonomía y la re-adjudicación del GT (decisión de la autora + mentores).
- **Evidencia:** el nodo `Restriccion_los_deudores_cuyas_financiaciones...`
  existe en run_3 con la description verbatim del Punto 4.5 del PDF; las 10
  búsquedas reales del agente y 3 consultas razonables mínimas dan 0 hits;
  solo consultas formuladas con palabras del propio nodo lo alcanzan. Causa:
  `buscar_nodos` indexa label e id (no description); el label no comparte
  vocabulario con la pregunta y el id se trunca antes de "garantías".
- **Alcance:** run_3, pregunta CQ-031; el mecanismo (indexación léxica sobre
  label/id) aplica a todo el sistema.
- **Destino:** doble — (a) explica con causa mecánica el modo de fallo
  "hedging por info inalcanzable" de la Fase 2.3; (b) palanca concreta de
  refinamiento para el Paso 4 (labels/ids que expongan contenido, o indexar
  descriptions). Pregunta abierta para mentores: ¿la taxonomía necesita
  distinguir "existe pero inalcanzable" de completitud y de navegación?

## H7. El ground-truth humano también falla en la frontera (3 casos)

- **Estado:** validado (2 casos documentados en Fase 2.4; el tercero,
  CQ-031, con el hecho verificado y la re-adjudicación pendiente).
- **Evidencia:** CQ-025 no era "fuera de corpus" (confusión de nombre de
  documento); CQ-020/CQ-017 resultaron mixtos al investigarse a fondo;
  CQ-031: el barrido manual de ~4.050 nodos no encontró el nodo portador que
  el verificador sí encontró.
- **Alcance:** hoja de respuestas de los 5 casos-control.
- **Destino:** Resultados + argumento central de human-in-the-loop: humano y
  verificador se corrigen mutuamente; juntos > cualquiera solo, demostrado
  en datos propios.

## H8. La dificultad de frontera se reproduce en cada capa de verificación automática

- **Estado:** validado como patrón observado; redactar con alcance acotado
  (4 instrumentos, 1–2 instancias documentadas cada uno — es un patrón, no
  un teorema).
- **Evidencia:** (1) el juez: falso positivo en CQ-034 detectado por el
  verificador de la Fase 2.3; (2) el pilot: etiquetó completitud_kg con
  confianza alta teniendo el nodo en su propia evidencia del claim central
  (run_1/CQ-010, `verificador_scale_full.json`); (3) el verificador v1–v4:
  etiqueta mal con la evidencia correcta juntada; (4) el checker de quotes:
  2 falsos positivos por artefactos de extracción del PDF, corregidos por
  re-verificación humano-dirigida.
- **Alcance:** los cuatro instrumentos del proyecto, sobre el corpus BCRA.
- **Destino:** Discusión — cada capa de verificación automática reproduce,
  en su propia frontera, el tipo de error que audita; la supervisión humana
  no es un parche de una capa sino una propiedad necesaria del sistema.

## H9. Ruido de atribución medible en el mapa de defectos de la Fase 2.3

- **Estado:** validado en instancias puntuales; **pendiente** cuantificar si
  se quiere afirmar un porcentaje.
- **Evidencia:** claims secundarios de run_1/CQ-010 etiquetados
  completitud_kg cuando el nodo portador existía (desactualizado →
  contenido_kg); el caso de confianza alta de H8(2).
- **Alcance:** instancias detectadas al construir los ejemplos resueltos; el
  split 38/49/12 del mapa de defectos debe citarse con esta salvedad.
- **Destino:** nota de límites en Resultados de la Fase 2.3.

## H10. El anclaje textual funciona a nivel contenido (v4)

- **Estado:** validado.
- **Evidencia:** 37 quotes verificados programáticamente: 0 invenciones.
  Las 15 "violaciones" formales son elisiones marcadas, renders condensados,
  comillas tipográficas y artefactos del extractor de PDF (guionado, espacios
  intra-palabra).
- **Alcance:** calibración v4.
- **Destino:** Resultados (el requisito de quote verbatim es exigible y el
  modelo lo cumple en sustancia); metodológico: la verificación automática
  de quotes necesita matching tolerante a artefactos de extracción (H8-4).

## H11. Thinking del agente: material empíricamente ralo

- **Estado:** validado.
- **Evidencia:** trazas ON de run_3: Haiku 4.5 sin interleaved thinking solo
  emite bloques en el turno 0 (CQ-017 ON: 1 bloque de ~457 chars en 9
  turnos). El acceso al thinking quedó cableado en v4 pero los 5
  casos-control son trazas OFF (sin thinking) — camino no ejercitado en
  calibración.
- **Alcance:** harness congelado (Haiku 4.5, config del frozen).
- **Destino:** nota metodológica; matiza el pedido de acceso al thinking
  (está implementado; el material casi no existe con este modelo/config).

## H12. Calibradores con ejemplos resueltos vs. reglas declarativas — matiz nuevo

- **Estado:** la parte del juez, validada (saga v1–v2.1.1). El matiz de v4
  es **hipótesis**: los ejemplos pueden anclar hacia el patrón superficial
  (ejemplo de generación-de-más para claims no_soportado → v4 etiquetó
  generación-de-más en los dos casos donde el GT era completitud).
- **Evidencia:** calibraciones del juez (documentadas); coincidencia
  ejemplo-error en v4 (CQ-020, CQ-017).
- **Alcance:** hipótesis a testear (o a consultar con Juan) antes de afirmarse.
- **Destino:** Discusión metodológica, solo si se confirma.

## H13. Costos de calibración como restricción de diseño

- **Estado:** validado.
- **Evidencia:** corrida v4: 1.352.378 tokens in / 41.854 out (Opus) para 5
  casos; CQ-017 solo: 385K in (contexto con 108 nodos íntegros).
- **Alcance:** verificador v4 sobre run_3.
- **Destino:** nota metodológica (por qué no se itera el prompt a ciegas;
  presupuesto de la fase de refinamiento).

---

## Pendientes que bloquean prosa

- Re-adjudicación de CQ-031 (autora + mentores) → afecta H6, H7 y la tabla
  v1→v4.
- Decisión de taxonomía "existe pero inalcanzable" (mentores) → H6.
- Respuesta de Juan → H4, H5, H12.
- Cuantificación del ruido del mapa de defectos, si se decide hacerla → H9.
