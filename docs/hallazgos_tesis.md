# Hallazgos acumulados para la tesis — registro vivo

Convención: cada entrada lleva **Estado** (validado / pendiente / hipótesis),
**Evidencia** (archivo o corrida de origen, verificable en el repo),
**Alcance** (sobre qué datos vale la afirmación) y **Destino probable** en el
documento final. Solo lo *validado* puede convertirse en prosa de tesis; lo
*pendiente* sobrevive como hueco marcado hasta verificarse.

Última actualización: 2026-08-23 (H14–H26 del ciclo escalón 1 → EV2 → ablaciones → banco;
los H1–H13 conservan su redacción de 2026-07-06 — era verificador v4 — y sus matices
posteriores se anotan en el hallazgo nuevo que corresponda).

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
  también insumo directo de la consulta al revisor externo.

## H5. Dilución de instrucciones: más reglas, menos cumplimiento (v4)

- **Estado:** validado como correlación observada; hipótesis como causa.
- **Evidencia:** prompt 6.9K → 17.4K chars y: instrucción del esquema sin
  rastro en trayectorias ni razonamientos (CQ-017 verificado explícitamente);
  reglas de CONFIANZA ignoradas (alta en 4/4 contra las condiciones del
  prompt); abstención (feature central) usada 0 veces; CQ-034 rompió el
  contrato JSON con campos inventados.
- **Alcance:** calibración v4 (una corrida, 5 casos).
- **Destino:** Discusión metodológica (límites del prompting); consulta al revisor externo.

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
- **Alcance:** hipótesis a testear (o a consultar con el revisor externo) antes de afirmarse.
- **Destino:** Discusión metodológica, solo si se confirma.

## H13. Costos de calibración como restricción de diseño

- **Estado:** validado.
- **Evidencia:** corrida v4: 1.352.378 tokens in / 41.854 out (Opus) para 5
  casos; CQ-017 solo: 385K in (contexto con 108 nodos íntegros).
- **Alcance:** verificador v4 sobre run_3.
- **Destino:** nota metodológica (por qué no se itera el prompt a ciegas;
  presupuesto de la fase de refinamiento).

---

## H14. Inversión de las métricas intrínsecas publicadas (P-b)

- **Estado:** validado (predicción crux pre-registrada y confirmada).
- **Evidencia:** `docs/spec_evaluacion_intrinseca.md` (predicciones selladas antes del
  script); `data/experiment/metricas_intrinsecas/pasada1_resumen.md`: M1 (duplicación,
  protocolo publicado) da **peor** al grafo corregido (v3 0,6377 > v2 0,6010) siendo v3
  mejor extrínsecamente; M10 chunks mudos 53/368 → 0/368.
- **Alcance:** grafo_v2 vs reensamblado_v3 vs KG-Base; corpus de 5 TOs.
- **Destino:** Resultados + Discusión (las métricas intrínsecas estándar para KGs con LLM
  son ciegas o favorables a la sobre-fusión, que es el modo de falla que importa en un
  corpus regulatorio).

## H15. El juez bajo flag no es confiable

- **Estado:** validado.
- **Evidencia:** `data/experiment/evaluacion_escalon1/lectura_P1P5_escalon1.md` — el
  muestreo humano movió 4 mayorías del juez (evasivas y no-respuestas aprobadas,
  amputación aprobada). Regla operativa vigente: todo veredicto flaggeado pasa por
  muestreo humano antes de integrar tablas.
- **Alcance:** juez v2.1.1 sobre EV1 (36 preguntas, N=3, dos brazos).
- **Destino:** Metodología (limitaciones del juez) + justificación del human-in-the-loop.

## H16. Alucinación sistemática con retrieval perfecto (BKL-0026)

- **Estado:** validado (N=3, sistematicidad confirmada).
- **Evidencia:** RT-C6-1 incorrecta 3/3 (labels `rt_c6_n3_r{1,2,3}`, 0 hits de caché) con
  `ver_nodo` byte-idéntico entre trazas: el nodo correcto estaba en contexto y el agente
  invirtió la norma igual. `data/backlog/backlog.jsonl` (BKL-0026), tablero §3.
- **Alcance:** agente Haiku congelado sobre KG-Refinado; un caso, replicado 3/3.
- **Destino:** Resultados (grounded ≠ correct en su forma más pura: falla de generación
  con retrieval perfecto); insumo del techo de H19.

## H17. Mecanismo presente, no operante (tres instancias medidas)

- **Estado:** validado como patrón (tres instancias independientes).
- **Evidencia:** (i) escalón 1: el esqueleto navegable existía y el agente lo usó en 9 de
  108 trazas (8,3 %) — `lectura_P1P5_escalon1.md` P2; (ii) ablación A1.4 (`ffc6ff6`): la
  paginación de tools v2 no se usó en 0 de 275 llamadas y el factor tools no movió la
  métrica (P4 no cumplida); (iii) banco A2.0 (corrida 1): ante tools descriptas pero no
  conectadas, el agente operó como si las tuviera (ver H25).
- **Alcance:** agentes Haiku congelado y Claude Code; capacidades estructurales del grafo
  y de las tools.
- **Destino:** Discusión — capacidad agregada al sistema ≠ capacidad usada por el agente;
  motiva la ablación de política (A1.7) y el co-diseño grafo–navegador.

## H18. El defecto de ensamblado y el denominador aguas arriba

- **Estado:** validado (medido y corregido).
- **Evidencia:** RX-01: 102 resultados de extracción pagados y descartados por desempate
  de `chunk_id` (el criterio "más entidades" premiaba la tabla de referencias sobre el
  articulado); la métrica de cobertura reportaba 100 % porque su denominador eran los
  sobrevivientes del propio desempate (real: 406/508 = 79,9 %). Re-ensamblado v3: +2
  puntos netos medidos sobre EV1 (27→29/36), `docs/lectura_escalon1b.md`.
- **Alcance:** ensamblador del linaje grafo_v2; EV1 sellado.
- **Destino:** Metodología (regla del denominador aguas arriba, M10) + Resultados.

## H19. Clausura léxica: la brecha anti-léxica sobrevive a tres retrievers

- **Estado:** validado (tres instrumentos, diseño apareado).
- **Evidencia:** EV2 navegabilidad (`5b02d22`): recall consultada literal→anti-léxica
  0,958→0,620 (KG-Refinado), 0,716→0,493 (KG-Base), 0,396→0,271 (KG-Reextraído);
  ablación A1.4 (`ffc6ff6`): BM25 no cierra la brecha (P2 refutada; mejora lo literal por
  ranking, 52→52 vistas y brecha vista-sin-consultar 6→1) — de 20 fallas anti-léxicas,
  **7 son de búsqueda y 13 de selección del agente**; bake-off (`df9da34`): tampoco el
  mejor embedding denso la cierra (36 % anti vs 52 % literal en el mismo modelo).
- **Alcance:** pares sintéticos apareados (EV2 y v3), 3 grafos, 3 familias de retriever.
- **Destino:** Resultados + Discusión (el techo del retrieval es bajo: lo léxico/denso
  compra lo literal; lo semántico exige política de agente o representación distinta).

## H20. Arquitectura > prompt (enmienda 01)

- **Estado:** validado (experimento natural + predicciones refutables).
- **Evidencia:** `docs/enmienda_01_diseno_reextraccion_v2.md`: 60/117 faltantes
  verificaban solo en bloques heredados; 21 reintentos con feedback correcto fueron
  byte-idénticos y no convirtieron — un defecto que sobrevive al feedback correcto no es
  de prompt sino de arquitectura. Mini-chunks: P1 confirmada (60→0 por construcción),
  P2 refutada y publicada (cola 21,8 % vs <10 %), P3 confirmada (USD 2,48 < 2,87).
- **Alcance:** pipeline E0–E3 sobre `pro`; corpus completo en `5273c0c`.
- **Destino:** Metodología del pipeline + Discusión (los ciclos de reintento no corrigen
  defectos de asignación de responsabilidad).

## H21. El esquema reduce los incorrectos a la mitad; el pipeline sin parches empata con el refinado a mano

- **Estado:** validado (EV2 cerrado con adjudicación humana).
- **Evidencia:** `64de678` + `data/experiment/ev2_reporte/reporte_ev2.md`: KG-Base 3/20/17,
  KG-Refinado 5/26/9, KG-Reextraído 4/27/9 (correcto/parcial/incorrecto sobre 40); juez
  validado 11/12 contra adjudicación (98,1 % por criterio). Ambos grafos del esquema v2
  reducen los incorrectos casi a la mitad (9 y 9 contra 17); KG-Reextraído lo logra sin
  ninguna corrección manual.
- **Alcance:** EV2 (40 preguntas ciegas, 164 criterios), tres grafos, harness congelado.
- **Destino:** Resultados (tabla central de fidelidad) + Conclusiones.

## H22. El empate esconde perfiles de falla distintos; generación es la clase modal

- **Estado:** validado (atribución determinística, replay 120/120 + 191/191).
- **Evidencia:** `85d9fdb` (`atribucion_fallas.md`): KG-Refinado falla por navegación con
  ancla presente (5/9), KG-Reextraído por granularidad de ancla (4/9, contenido en
  sub-puntos 3/4); generación es la clase modal en los tres grafos (17/25/21) — grounded
  ≠ correct cuantificado; techo de retrieval 14/7/6.
- **Alcance:** las 120 respuestas base de EV2 (+191 del §7), regla sellada pre-cómputo.
- **Destino:** Resultados (mapa causal) + Discusión.

## H23. Complementariedad léxico/denso, y el costo de la licencia es cero

- **Estado:** validado (bake-off propio sobre el corpus).
- **Evidencia:** `df9da34` (`bakeoff_embeddings.md`): BM25 gana literal@1 por 20 pp sobre
  el mejor denso (72 vs 52) y pierde anti-léxica@1 por 20 pp (16 vs 36) — no miden lo
  mismo; la referencia no elegible por licencia (CC-BY-NC) no supera al mejor elegible en
  ninguna columna.
- **Alcance:** 1.763 pasajes de E0, 100 consultas apareadas, 5 modelos + control BM25.
- **Destino:** Metodología (elección del modelo con criterio ex ante declarado y elección
  bajo criterio no resuelto) + motivación medida del brazo híbrido.

## H24. La frontera ancla/chunk (cuarta aparición)

- **Estado:** validado como propiedad del corpus (cuatro apariciones independientes).
- **Evidencia:** censo EV2 (`ausencias_diagnostico.json`); sensibilidad por descendientes
  de A0.2 (`85d9fdb`, donde la política de descendientes cambia la clase causal);
  mapeo del bake-off (26/50 pares con gold solo-mini_chunk bajo match exacto); referencias
  de r1 (149 irresolubles por «contenido solo en descendientes», `185e042`).
- **Alcance:** toda medición que cruce anclas normativas con unidades de chunk.
- **Destino:** Metodología (regla: toda medición cross-capa declara su política de
  descendientes antes de medir) + Discusión.

## H25. Fabricación bajo contradicción de configuración

- **Estado:** validado (corrida 1 de fase B del banco, 12/12 sesiones).
- **Evidencia:** `data/experiment/banco_mcp/smoke/resultados/faseB/diagnostico_corrida1.md`:
  con el prompt describiendo tools que el harness no había conectado (init `pending`,
  `tools=[]`), el agente simuló llamadas como texto en 7/8 sesiones y en una **fabricó la
  respuesta completa de la tool** (JSON con 5 pasajes y similitudes inventadas, con forma
  que no es la del servidor); solo 1/8 respondió `respondible:false`. Los servidores no
  recibieron ninguna llamada.
- **Alcance:** **encuadre obligatorio**: fabricación inducida por contradicción de
  configuración (tools descriptas y ausentes), NO medida de propensión a fabricar en
  condiciones normales. Claude Code 2.1.196, dos brazos.
- **Destino:** Discusión (un agente sin fuente produce la forma de la evidencia sin la
  evidencia — grounded ≠ correct en el límite); justificación de la regla de honestidad
  en el prompt del banco y del gate de arranque por versión.

## H26. La semántica del corte no es la del contrato (H-B2)

- **Estado:** pendiente (a caracterizar antes del pre-registro de A2.1).
- **Evidencia:** `banco_mcp/smoke/resultados/faseB_corrida2/reporte_faseB_corrida2.md`:
  `--max-turns 12` no disparó con `num_turns=14` (sesión exitosa); el tope instructivo del
  prompt (10 tool calls) se excedió una vez (13). El criterio de corte R5 de cualquier
  medición sobre el banco debe apoyarse en una señal verificada, no en el nombre del flag.
- **Alcance:** Claude Code 2.1.241, modo `--bare`, 12 sesiones.
- **Destino:** nota metodológica del banco; prerrequisito del pre-registro de A2.1.

---

## Pendientes que bloquean prosa (actualizado 2026-08-23)

- ~~Re-adjudicación de CQ-031~~ — RESUELTO: re-adjudicada en el ciclo v5/v5.1 del
  verificador (`docs/especificacion_verificador_v57.md`); H6 y H7 quedan desbloqueados.
- ~~Decisión de taxonomía "existe pero inalcanzable"~~ — RESUELTO: `alcanzabilidad_kg`
  es categoría de primera clase desde la taxonomía v2.1
  (`.claude/skills/kg-refinement/references/taxonomia.md`); H6 desbloqueado.
- Respuesta pendiente del revisor externo sobre los comentarios de la Fase 2.4 → H4, H5,
  H12 (sigue abierta).
- Cuantificación del ruido del mapa de defectos, si se decide hacerla → H9 (sigue
  abierta).
- D-f (secuencia de la evaluación de tripletas, `docs/plan_tesis.md`) → condiciona la
  fecha de los números de H24 aplicados a B4.
