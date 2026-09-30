# Checklist previo a la tanda 1 y al escalado

Lista única de lo que tiene que estar resuelto o decidido antes de la tanda 1
(B6.1) y del escalado. La escribí el 29/09/2026 consolidando cuatro fuentes:
`docs/plan_tesis.md`, las §1 a §5 de `docs/laudo_release_r2_pipeline.md`,
`data/backlog/backlog.jsonl` (BKL-0028 a BKL-0036 y las entradas con
`release_candidata` r2, que son BKL-0030 y BKL-0031) y
`docs/cola_mejoras_diferidas.md`. Base: HEAD `0488a9b`, más los registros de
huecos de este mismo pase (sin commit al escribir esta lista). Actualizada el
29/09/2026 sobre HEAD `a0a6200`: orden y condiciones de la tanda 1, y P6
(decisión de la autora del 29/09/2026).
Actualizada otra vez el 29/09/2026: desvíos declarados por la autora sobre quién
leyó y adjudicó (P1, P15, X11, Q12).
Actualizada el 29/09/2026 con el cierre de la fase 2a (P1 a P5, P10, P16, N3, N8,
R27).
Actualizada el 29/09/2026: fase 2b cerrada (P16) y tablero de correcciones como
condición (4) de la tanda 1 (R28).
Actualizada el 30/09/2026 con las decisiones de la autora del 30/09: el cambio de
prefijo queda decidido y se hace en el ciclo B2.11 (`:388-404`), con la ventana única
del §7 (X2 a X5 y X8 decididos; X6, X7 y X9 entran al ciclo con el remedio por
decidir; X1, X10 y X11 se deciden en L-ESQ-R2); ítems nuevos
P17 a P19, R29 a R31, X12 a X16 y W9 a W13; P4, Q10, Q11, R1, R5, R8, R20, R21 y R27
actualizados. Las anclas `:n` se remapearon a la v16 del plan.
Actualizada otra vez el 30/09/2026: resultados de U-PRE-R2-DIAG (`159c1e2`; R19, R4, R5,
R13, R27, R29 y X1; nuevos R32, N9 y W14) y mandatos en borrador de U-UMBRAL,
U-LISTAS-NOMAP y U-INSUMOS-CAP (X12 a X14 y W12). R29 corrige la etiqueta: el defecto de
`cap::1.2` es el de `BKL-0006`.
Actualizada otra vez el 30/09/2026: R33 (colisiones de ids de chunk, `BKL-0037`); X3, X12,
X13, X14, X16 y W12 pasan a firmado (`30f106c`).
Actualizada otra vez el 30/09/2026: R30 con las cifras de `salida_dirigida/` y W2 con
`deteccion_determinista`.
Actualizada otra vez el 30/09/2026: W12 pasa a hecho (U-INSUMOS-CAP cerrada, `f32f20c`).
Actualizada otra vez el 30/09/2026: X14 con el resultado de U-UMBRAL (cerrada, `e4d053b`) y la
orientación de la autora para L-ESQ-R2; anclas `:n` remapeadas por la unidad 4b del plan.
Actualizada otra vez el 30/09/2026: U-LISTAS-NOMAP cerrada (`acc310e`): X12 y X13 con el resultado
disponible; X6, X7 y X9 absorbidos en el diseño, con el remedio pendiente del laudo.

**Convenciones.**
- Registro: `:n` es la línea de `docs/plan_tesis.md`; «laudo §x» es la sección
  del laudo de r2; `BKL-nnnn` es la entrada del backlog; «cola n» es la
  entrada de la cola de mejoras.
- Estado: **registrado** (escrito en el repo, sin decisión tomada),
  **decidido** (la autora decidió y está escrito) o **hecho** (ejecutado y en
  el repo).
- Decisión: «Sí» si falta una decisión de la autora; «No» si solo falta
  ejecutar.
- **HUECO**: se discutió y no estaba registrado; lo registré en el lugar
  indicado el 29/09/2026.
- Canal 0 no es uno de los cinco canales pedidos: agrupa las precondiciones
  (cierre de la tanda 0) y la operación del escalado, que no caben en ninguno.

## Orden y condiciones de la tanda 1

Decisión de la autora del 29/09/2026, asentada en las filas B6.1 (`:765`) y
B2.10 (`:386`). Cerrada la tanda 0 (adjudicación ciega de C2 a C5 con el
anexo E5.c, P1, y E6, P2), las unidades de r2 sin cambio de prefijo (canal 1)
y A1.8 (canal 3) pueden avanzar en paralelo con la lectura del capítulo por
los mentores. La tanda 1 depende de tres condiciones:

1. La validación escrita del capítulo, registrada (P6).
2. B2.10 cerrada: r2 versionada con su gate en verde (R26, con lo que el
   laudo firmado incluya del canal 1). **[30/09/2026]** Se lee: B2.10 y B2.11
   cerradas hasta U-REEXT-T0 (`:400`), con el gate de r2 en verde sobre los
   grafos re-extraídos.
3. La decisión de la autora con los mentores sobre el cambio de prefijo: X1
   (matriz), X2 (prompt), X3 (ventana del §7) y X4 (cuándo va la release de
   prompt), con X11 (si la lectura asistida de la matriz alcanza). **[30/09/2026]**
   Decidida: el prefijo cambia en el ciclo B2.11 y la ventana del §7 se usa ahí
   (X2 a X4). Queda L-ESQ-R2 firmado (`:394`), que resuelve X1, X10 y X11.
4. El tablero de correcciones (`docs/tablero_correcciones.md`) con la columna
   «después de r2» completa y cada meta cumplida o con su residuo declarado (R28;
   laudo de r2, §3.1, punto 8). Agregada el 29/09/2026. **[30/09/2026]** Con dos
   columnas: r2a (solo código, antes de re-extraer) y r2b (prompt y re-extracción).

**Desde el 30/09/2026 la tanda 1 corre sin ventana de corrección** (X3, P19): una
falla de esquema que revele va a release posterior declarada. Orden de trabajo hasta
la tanda 1: fila B2.11 del plan (`:388-404`).

## 0. Precondiciones y operación del escalado

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| P1 | Adjudicación ciega de C2 a C5, antes de E6 | anexo E5.c `docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md` (firmado, `0488a9b`); `:746` | hecho: cierre recomputado en `ecd102c` sobre las marcas de `8e0597c` (instancia adjudicadora, desvío declarado); definitivas sin cambio | No; la autora confirma modelo y versión de la instancia |
| P2 | E6: lectura de observaciones y vigilancias y reporte de 2a, puntos (1) a (6) de la lectura | mandato 2a, E6 (`docs/mandatos/UTANDA0_2A_corrida.md:216-234`); `:750` | hecho: `2399eb7`, `reports/tanda0/reporte_fase2a.md`; el cruce de ausencias del punto (3) pasa a R27 | No |
| P3 | **HUECO** — punto (6) de E6: aristas entre documentos distintos, por relación, en los tres ensamblados | `:750` (6) | hecho: reporte de 2a, §4, punto 6 | No |
| P4 | Posición sobre la ventana del §7 por la vía de A8, en el reporte de 2a | mandato 2a, E6 c; `docs/preregistro_tanda0.md:832` (A8); `:746` | decidido (29/09): se acepta la posición propuesta; la ventana queda intacta para la tanda 1, salvo que la use la decisión sobre la matriz (X1 a X4, X11). **Superado el 30/09:** la ventana se usa en el ciclo B2.11 (X3) | No |
| P5 | Mentor informado con el reporte de 2a (`reports/tanda0/reporte_fase2a.md`) | `:746` | registrado | No: acción de la autora |
| P6 | Gate del capítulo: validación escrita de los mentores sobre el capítulo 3; rige para la tanda 1 y el escalado. **Condición (1) de la tanda 1** | `:139-144`, `:1095` (actualización del 29/09 en los dos) | registrado; PENDIENTE: los mentores leen el capítulo (declaración de la autora del 29/09); la tanda 0 corrió por la decisión del 25/09 (entrada de estado del 11/09) | No: registrar la validación cuando llegue |
| P7 | Decisiones abiertas del gate del capítulo: (1) los ocho límites de la Tabla 4 con destino; (2) principio de gobierno de la enmienda; ítem (a), adenda al laudo congelado por sus nueve filas | `:145-154` | registrado; sin cierre encontrado | Sí |
| P8 | U-COB-A: laudo sobre las 77 unidades del bloque A y `cifras_vigentes.md` (ítem (b), «reemplaza 11» contra «las diez») | `:154-157`, `:729` | registrado | Sí |
| P9 | B5.7: costos con tarifas reales, manifiesto del corpus escalado con `perfil_e1: "v3_b54"`, re-presupuesto de los no-RI antes de la tanda 2 | `:732` | registrado | Sí: presupuesto |
| P10 | Mandato de B6.1: tasas y muestreo de las vigilancias (1) a (9), sellados antes de correr; incluye (1) y (3) y la lectura de (2) y (7), no medidas en la tanda 0 (decisión del 29/09) | `:765` | registrado | Sí |
| P11 | Gate de la tanda 1: esqueleto v3 inyectado y S15 en PASS | `:766` | registrado (en la tanda 0, S15 PASS en `cf6ca42`) | No |
| P12 | Gate de la tanda 1: retiro de las tres `aplica_a` de U-COB-A si sus TOs entran | `:767` | registrado (en la tanda 0, 0 de 3 porque sus TOs no estaban) | No |
| P13 | La tanda 1 pasa por r1: mecánica a fijar en el mandato | `:768`; precedente, gate 1 de la tanda 0 (`47c9283`) | registrado | No |
| P14 | Observaciones (10), (11) y (12) de la tanda 1 contra sus líneas de base | `:769`, `:770` | registrado | No |
| P15 | Tanda 1: definir de antemano quién lee y adjudica (vigilancias, observaciones y muestras): modelo con muestra humana de control de tamaño suficiente y declarada, o experto del dominio | esta lista (29/09); antecedente, desvíos declarados en `:746`, `:749` y `:751` | registrado | Sí, con los mentores |
| P16 | Cierre formal de 2b: segunda emisión del paso 8 (reporte de 2b), según la enmienda `a551c57` §2.2 | `:751`; `reports/tanda0/reporte_fase2b.md` | hecho: `05465e9`; fase 2b cerrada | No |
| P17 | U-MANT: tabla de qué obliga a reprocesar todo y qué no, procedimiento de empalme de un subgrafo re-extraído y control de los supuestos del sitio del BCRA con aviso ante cambios; revoca la exclusión de avisos del mandato de U-JOB-ACT | `:401`; `:1138` | decidido (30/09) | No |
| P18 | U-SUBGRAFO: actualización solo del subgrafo afectado en los tres TOs de desarrollo que cambiaron en el sitio; cubre la exigencia 6 | `:402` | registrado; costo NO VERIFICADO | Sí: tope |
| P19 | El pre-registro de la tanda 1 declara que corre sin ventana de corrección | `:765` | decidido (30/09) | No |

## 1. r2 sin prefijo

Avanza en paralelo con la lectura del capítulo una vez cerrada la tanda 0.

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| R1 | Firma del laudo de release r2 | laudo, «Firma»; `:386` paso (1) | registrado (BORRADOR); desde el 30/09 r2 incluye el cambio de prompt y el laudo se reescribe antes de la firma (notas del 30/09 en «Qué no es», §1.6, §3.2 y §4) | Sí |
| R2 | `BKL-0030`: reintento por corte y partición; (a) sola o (a) con partición | laudo §1.1 y §4 (fila de `cap::4.2.1.2`); `BKL-0030`; `:387` (1) | registrado | Sí |
| R3 | Doble conteo del checkpoint de cierre del runner | laudo §1.6 (recomendación: entra con R2) | registrado | Sí (laudo §5, 1) |
| R4 | `BKL-0031`: detector de duplicados y fusión solo de forma; umbral del paso 3 | laudo §1.2 y §5 (3); `BKL-0031`; `:387` (2) | registrado; se decide junto con R32 (T2) y R13 (H2) | Sí |
| R5 | RX-10 / `BKL-0006`: cablear el parser de tablas a E0; censo en USD 0 antes de costear | laudo §1.3 y §5 (5) | registrado; entra a U-R2-CODIGO (`:397`) como **primera prioridad** (decisión de la autora del 30/09: D2 atribuye a tablas las 8 pérdidas reales de contenido de C1 a C4), con la detección de tablas en E0 y la afirmación falsa de `cap::1.2` (R29) | Sí: tope |
| R6 | `cuarentena` booleana contra `"true"` en T7; su entrada de backlog se escribe al firmar | laudo §1.4 | registrado; sin entrada de backlog | Sí (laudo §5, 6) |
| R7 | Test de la cláusula de mutuales (RT-C6), opción (c) | laudo §1.5 y §5 (2) | registrado | Sí |
| R8 | Completar `esquema_v3_clases.json` con los seis ids del perfil | laudo §1.6 (recomendación: entra); `:747` | absorbido por X15 (U-CAT-UNICO, `:395`) el 30/09 | No |
| R9 | Pendientes de U-B1a: rangos, 196 conflictos de properties, 5 cross-TO, 41 `padre_sugerido`, política de cola | laudo §1.6; cola 8 | registrado | Sí |
| R10 | Guarda de modalidad (deber emitido como Condicion) | laudo §1.6; cola 12 | registrado; no entra salvo que la vigilancia (1) lo pida | Sí, tras E6 |
| R11 | H1 y H4: remisiones desde Condicion, Potestad y Definicion, y lectura de `termino` | laudo §4 | registrado | Sí |
| R12 | Remisiones falsas por paráfrasis: detectar sobre el texto de E0, no sobre la descripción | laudo §4; `:387` (3) | registrado; corrección previa a la tanda 1 | Sí |
| R13 | H2: fusión por label de Condicion, Definicion y Potestad (cambia ids y la fixture) | laudo §4 | registrado; se decide junto con R32 (T2) y R4 (`BKL-0031`) | Sí |
| R14 | Nodos aislados: derivar `establecida_en` de la procedencia en el ensamblado | laudo §4 | registrado | Sí |
| R15 | Procedencia de las remisiones: resolver desde cada procedencia; vista del agente | laudo §4 (dos filas) | registrado; alcance a definir | Sí |
| R16 | Test de la suite: el ejemplo `cla::5.1.1.1` | laudo §4 (entra con el gate) | registrado | No: la autora sella la entrada de la fixture |
| R17 | Control de aristas entre nodos con la misma descripción (M50, idéntica y correcta) | laudo §4 (fila del 29/09) | registrado; alcance a medir | Sí |
| R18 | B2.9: detector de huérfanos de label | `:385`; no figura en el laudo de r2 | registrado | Sí: si entra |
| R19 | Entrada de r2 en la fixture, sellada antes del gate, con su política de cuarentena | laudo §3.1 (2) y §5 (6) | decidido (30/09): sigue las propuestas de D1 de U-PRE-R2-DIAG: T4, T5 y E4-a8 re-direccionados en U-R2-CODIGO (`:397`); T7 y E4-a7 pasan con el catálogo único (`:395`); T2 queda en persiste salvo que entre R32. La sella la autora antes del gate | Sí: el sellado y la política de cuarentena |
| R20 | Corpus sobre el que se materializa r2: los cinco de desarrollo o los diez | laudo §5 (4) | decidido (30/09): los diez de la tanda 0, re-extraídos (U-REEXT-T0, `:400`) | No |
| R21 | Tope de gasto de la release | laudo §5 (5) | registrado; desde el 30/09 incluye la prueba pareada de U-PROMPT-R2 y la re-extracción de la tanda 0 (`:399`, `:400`) | Sí |
| R22 | Copia de resguardo de las dbs de caché, fuera del repo, antes de la corrida de r2 | laudo §2 y §3.2 (6) | registrado | No |
| R23 | Proyección de misses antes de pagar; un miss de más es FRENO | laudo §3.2 (5) | registrado | No |
| R24 | **HUECO** — muestra de precisión de aristas sobre r2 con el método de (12), como evidencia que no usa EV2 | laudo §5 (7) | registrado | Sí |
| R25 | Tests de la observación (12): se revisan después de r2, direccionados por (chunk_id, relación, tipo de destino) | `:751` | decidido (28/09) | No |
| R26 | Gate de release y versionado de KG-Reextraído-r2. **Condición (2) de la tanda 1** | laudo §3.1; `:386` pasos (3) y (4) | registrado | No |
| R27 | Unidad previa a la firma de r2: diagnóstico de los seis ítems de la suite que pasan de resuelto a persiste (E4-a7, E4-a8, T2, T4, T5, T7) y cruce de cada ausencia de C1 a C4 con los candidatos del §4 y con los rechazos de la matriz | `docs/mandatos/UPRE_R2_diagnostico.md`; `:386`; firmado en `6daf63f` | hecho: D1 y D2 commiteados en `159c1e2`; cerrada por decisión de la autora del 30/09 (categoría P y desvío de reglas aceptados; `:390`); resultados en R19, R29, R32, N9, W14 y X1 | No |
| R28 | Tablero de correcciones: la columna «después de r2» completa, con cada meta cumplida o su residuo declarado. **Condición (4) de la tanda 1** | `docs/tablero_correcciones.md`; laudo §3.1, punto 8 | registrado; metas abiertas en siete filas | Sí: las metas marcadas DECISIÓN ABIERTA |
| R29 | `BKL-0006`: afirmación falsa por tabla no detectada en `cap::1.2` (asentada primero como `BKL-0023`, que es el rastro de esa inversión en el nodo de compañías financieras y no reaparece en la generación 3). En r1, desarrollo y diez, bancos 2.500 y restantes entidades 5.000; el PDF dice bancos 5.000 y restantes 2.500 (`data/backlog/propuestas/C2_montos_12.md:31-32`). E0 no marca el chunk como tabla, y la suite da `no_aplicable` en desarrollo (en r1, `BKL-0006` persiste) | `:397`; tablero, fila propia; evento `nota` en `BKL-0006` (`data/backlog/backlog.jsonl:87`, 30/09) | decidido (30/09); etiqueta corregida el 30/09 | No |
| R30 | Persistencia del crudo del reintento de E3: `finales.jsonl` no lo guarda (en desarrollo, 168 de 1.760 finales aceptados tras reintento, sobre `corpus_tanda0/salida_dirigida/`; antes decía 167 de 1.757, leído en `salida/`) | `:397`; tablero | decidido (30/09) | No |
| R31 | Medición r2a: re-ensamblado solo en código sobre la salida guardada de la tanda 0, antes de re-extraer | `:398`; tablero, columna r2a | decidido (30/09) | No |
| R32 | T2, regresión real: la fusión por descripción de E2 juntó reglas distintas con igual redacción (`ext::7.5.3` y `ext::7.8.5.1`). Candidato del §4 del laudo, junto con H2 (R13) y `BKL-0031` (R4): la fusión no junta nodos de puntos distintos por igualdad de descripción | laudo §4 (fila del 30/09); `reports/u_pre_r2/d1_suite.md:62-79`; `:397` | registrado | Sí: al firmar |
| R33 | `BKL-0037`: colisiones de ids de chunk en E0. En la partición del corpus escalado hay 69 ids repetidos en 4 TOs (adfsp 9, ceninf 4, cirmo3 52, ri_niif 4); el runner indexa por `chunk_id` con last-wins y pierde sin aviso una extracción de cada par. Remedio en U-R2-CODIGO: ids únicos en E0 y un runner que se detiene ante repetidos. Ningún TO con ids repetidos entra a una tanda sin la corrección | `:397`; `:765`; tablero, fila propia; `reports/u_insumos_cap/estadisticas_corpus.md` §6 (`ded3494`) | decidido (30/09) | No |

## 2. Cambio de prefijo con enmienda

Desde el 30/09/2026 el cambio de prefijo está decidido: se hace en el ciclo B2.11
(`:388-404`), con la ventana única del §7 (X3).

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| X1 | Enmienda de la matriz congelada: → Operacion cumple el criterio (27 de 29, piso 0,780); → Potestad no (27 de 30, piso 0,744) | `:749`; `reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md` | registrado; resultado del protocolo, sin decidir la enmienda; desde el 30/09 se decide en L-ESQ-R2 (`:394`). D2: la matriz no es causa principal de ninguna ausencia (3 como secundaria); su valor es de completitud del grafo (lectura de la autora del 30/09; `:749`) | Sí, en L-ESQ-R2; condición (3) de la tanda 1 |
| X11 | ¿La lectura asistida de la matriz (instancia de modelo, revisada por la autora) alcanza para la enmienda, o se pide una validación adicional, por ejemplo de alguien del dominio? | `:749`; `reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md` | registrado; desde el 30/09 se decide en L-ESQ-R2 (`:394`) | Sí, en L-ESQ-R2; condición (3) de la tanda 1 |
| X2 | Si se amplía la matriz: cambiar el prompt (rota el prefijo; la tanda 0 se re-extrae o se revalida declarando la mezcla) o ampliar solo el validador | `:749` | decidido (30/09): se cambia el prompt (U-PROMPT-R2, `:399`) y la tanda 0 se re-extrae (U-REEXT-T0, `:400`) | No |
| X3 | Ventana única del §7: si se usa después de la tanda 0, la tanda 1 ya no la tiene y los cinco de la tanda 0 salen del conjunto final de B6.3 | `:749`; `docs/preregistro_tanda0.md:832` (A8, decisión 4) | decidido (30/09): este ciclo usa la ventana; la tanda 1 corre sin ventana y los cinco de la tanda 0 salen del conjunto de B6.3 (a). Enmiendas firmadas en `30f106c` (X16) | No |
| X4 | Cuándo va la release de prompt: antes o después de la tanda 1 (la §3.2 del laudo de r2 no admite cambios al prefijo) | `:749`; laudo §3.2 (1) | decidido (30/09): antes de la tanda 1, en el ciclo B2.11 | No |
| X5 | `BKL-0032`, `BKL-0033`, `BKL-0035`, `BKL-0036`: incorrectas `E1-prompt` de la observación (12) | backlog; `:751` | decidido (30/09): entran a U-PROMPT-R2 (`:399`) | No |
| X6 | `BKL-0034`: el catálogo v3 no tiene sujeto de nivel órgano | backlog; laudo §4 (fila del 29/09) | decidido (30/09): entra al ciclo; absorbido en el diseño de U-LISTAS-NOMAP (`acc310e`), con el remedio pendiente del laudo (L-ESQ-R2, `:394`), que aplica U-CAT-UNICO (`:395`) | Sí: el remedio, en L-ESQ-R2 |
| X7 | `BKL-0028` y `BKL-0029`: cambios del catálogo v3 del prefijo | backlog; laudo §1.6 (no entran a r2) | decidido (30/09): entran al ciclo; absorbidos en el diseño de U-LISTAS-NOMAP (`acc310e`), con el remedio pendiente del laudo (L-ESQ-R2, `:394`), que aplica U-CAT-UNICO (`:395`) | Sí: cuáles, en L-ESQ-R2 |
| X8 | Remedio de raíz de la cláusula de mutuales: regla de calificadores en E1 | laudo §1.5 (a) | decidido (30/09): entra a U-PROMPT-R2 (`:399`) | No |
| X9 | B2.4: laudo de los 15 `triaged`; nueve de asignación de sujeto piden una corrección sistemática vía prompt o validador de E1 | `:380` | la corrección sistemática entra al ciclo, absorbida en el diseño de U-LISTAS-NOMAP (`acc310e`; `:392`) y aplicada por U-PROMPT-R2 (`:399`), con el remedio pendiente del laudo; el laudo de los 15 de B2.4 sigue pendiente | Sí: el laudo de B2.4 |
| X10 | R6b: residuo del esquema | laudo §1.6 (solo por la vía de A8) | registrado; con la ventana usada, se decide en L-ESQ-R2 (`:394`) | Sí, en L-ESQ-R2 |
| X12 | Validación en código con Pydantic de todas las listas cerradas (tipos de nodo, predicados, catálogo de sujetos y valores de propiedades), con una política por campo ante un valor fuera de lista | `:396` (U-PYD); `:394` (L-ESQ-R2) | decidido (30/09); resultado disponible: tabla de modos por campo en el diseño de U-LISTAS-NOMAP (N2, `acc310e`); orientación de la autora registrada en la unidad 5 (`:394`); decisión formal en L-ESQ-R2 | Sí: la política, en L-ESQ-R2 |
| X13 | Lo no mapeable: reproceso por programa, con la mención textual del sujeto extraída; omisiones con categoría y tramo literal | `:392` (U-LISTAS-NOMAP) | decidido (30/09) que se define el proceso; resultado disponible: diseño de la mención, la resolución en código, el registro de no mapeados y las omisiones (N2, `acc310e`); orientación de la autora registrada en la unidad 5 (`:394`); decisión formal en L-ESQ-R2 | Sí: el diseño, en L-ESQ-R2 |
| X14 | Umbrales: propiedad del nodo, atributo de la relación o paso posterior sobre el nodo (decisión de esquema) | `:391` (U-UMBRAL) | hecho: resultado disponible (U1 `e81ed69`, U2 `e4d053b`; `reports/u_umbral/reporte_u_umbral.md`); orientación de la autora del 30/09 registrada en la unidad 5 (`:394`); la muestra de `limita` se lee antes (unidad 4b, `:393`); decisión formal en L-ESQ-R2 | Sí, en L-ESQ-R2 |
| X15 | Catálogo de sujetos en una sola fuente: hoy 102 ids en el bloque del prompt y 101 en `esquema_v3_clases.json` (6 solo en el bloque, 5 solo en el JSON); absorbe R8 | `:395` (U-CAT-UNICO); `:747` (hallazgo E1) | decidido (30/09) | No |
| X16 | Firma de las dos enmiendas de uso de la ventana (`data/experiment/esq/enmienda_uso_ventana_2026-09-30.md` y `docs/enmienda_preregistro_tanda0_2026-09-30_ventana.md`) | `:388` | hecho: firmadas en `30f106c` | No |

## 3. Búsqueda y navegación (A1.8)

A1.8 avanza en paralelo con r2 y con la lectura del capítulo una vez cerrada
la tanda 0, y va antes de A2.1 y B6.3 (`:327`, `:765`); no es condición de la
tanda 1.

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| N1 | Diagnóstico sin API en cuatro capas (entrada, alcance, navegación, respuesta) sobre preguntas de desarrollo y trazas de C1 a C5 | `:327` | registrado | No |
| N2 | **HUECO** — tope de 15 herramientas: 23 de 40, 27 de 40, 17 de 40 y 11 de 20 respuestas base de C2 a C5; 28 de 40 en C1 | `:327` | registrado | No |
| N3 | Patrón de navegación en las trazas de la tanda 0 y atribución de la respuesta invertida | `:750` (4) y (5); `:327` | decidido (29/09): el patrón de vecinos salientes es sistemático y pasa a A1.8 como candidato; la respuesta invertida no aplica a EV2 ni a C5 | No (entra en N5) |
| N4 | H3: el índice full-text no incluye `termino` | `:327` | registrado | Sí (entra entre las mejoras) |
| N5 | Qué mejoras entran: búsqueda, herramientas, instrucciones, tope de llamadas | `:327` | registrado | Sí |
| N6 | Criterio de aceptación de A1.8 | `:327` | registrado | Sí |
| N7 | Configuración del agente congelada y declarada antes del pre-registro de B6.3 | `:327`, `:772` | registrado | No |
| N8 | Instrucciones de respuesta del agente: la generación es la clase modal de falla | `:327` | decidido (29/09): A1.8 las suma | Sí: qué instrucciones (N5) |
| N9 | El agente tiene que bajar de un punto padre a sus hijos: 23 de las 31 ausencias de C1 a C4 son contenido presente bajo puntos descendientes del ancla (D2 de U-PRE-R2-DIAG) | `:327`; `reports/u_pre_r2/d2_ausencias.md:46-58` | decidido (30/09): requisito de navegación de A1.8 | Sí: cómo (entra en N5) |

## 4. Pre-registro de A2.1 y B6.3

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| Q1 | A2.1: prerrequisito H-B2 (`num_turns` contra `--max-turns`; criterio de corte R5) | `:335` | registrado | No |
| Q2 | Mismo analizador y modo en las dos búsquedas léxicas, o la diferencia declarada | `:327`, `:335`, `:772` | registrado | Sí: declarar |
| Q3 | Vocabulario de las preguntas de B6.3 | `:327`, `:772` | registrado | Sí |
| Q4 | Cuotas de preguntas de varios puntos y de abstención en el conjunto final | `:775` | registrado | Sí, con los mentores |
| Q5 | **HUECO** — tamaño del conjunto final por potencia y análisis pareado; con 40 preguntas, los intervalos de C1 a C4 se solapan | `:772` | registrado | Sí: cálculo |
| Q6 | Costo del agente medido en A2.2 antes de sellar B6.3 | `:772` (fórmula del brazo) | registrado | No |
| Q7 | Inconsistencia B4.2 contra B6.3 (d): instrumento de tripletas «ya validado» con su adjudicación abierta | `:445` | registrado; sin resolver | Sí |
| Q8 | Unidad de calibración del juez antes de B6.3 | cola 13 | registrado | No |
| Q9 | Regla de cegado en lecturas humanas y entrada de textos largos del instrumento de lectura | cola 10 y 11 | registrado | No |
| Q10 | Disjunción del conjunto final con desarrollo y con los diez de ESQ; también con la tanda 0 si se usa la ventana | `:772` (a); `:749` | decidido (30/09): los cinco de la tanda 0 salen del conjunto de B6.3 (a) (X3); el pre-registro de B6.3 lo declara (`:772`) | No |
| Q11 | Ciclo de corrección de esquema de la tanda 1, siempre antes del pre-registro de B6.3 | `:765` | decidido (30/09): no hay ciclo de corrección de esquema en la tanda 1; la ventana se usó en B2.11 | No |
| Q12 | B6.3: definir de antemano quién lee y adjudica (casos a adjudicación del juez, muestra de control, tripletas de B4): modelo con muestra humana de control de tamaño suficiente y declarada, o experto del dominio | esta lista (29/09); antecedente, desvíos declarados en `:746`, `:749` y `:751` | registrado | Sí, con los mentores |

## 5. Escritura

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| W1 | Tabla de reproducibilidad: modelo, versión con fecha, temperatura, vía (API o Claude Code), por medición y por etapa | `:854` (precisión por etapa del 29/09); `docs/registro_modelos.md` NO ENCONTRADO | registrado | Sí: aprobar el documento |
| W2 | B2.5: spec del backlog con `capa_pipeline` obligatorio y dos vías; huecos del catálogo de especies (cola 17; especies provisionales de `BKL-0032`, `BKL-0033` y `BKL-0035`) | `:381`; cola 17; backlog; `docs/spec_backlog_refinamiento.md` | registrado; en la spec: `lectura_asistida` y el evento `correccion_diagnostico` (enmienda 2026-09-29) y `deteccion_determinista` (enmienda 2026-09-30, `31e0d38`) en el vocabulario de `diagnostico`; el resto de B2.5 sigue pendiente | Sí: ampliar el catálogo de especies |
| W3 | B2.6: protocolo de releases escrito; `docs/protocolo_ciclo_refinamiento.md` NO ENCONTRADO | `:382` | registrado | Sí: antes o después de r2 |
| W4 | B2.8: método de construcción y refinamiento, «el que se sigue en B6»; `docs/metodo_construccion_refinamiento_kg.md` NO ENCONTRADO | `:384`, `:765` | registrado | Sí: antes o después de la tanda 1 |
| W5 | **HUECO** — la fila B2.10 citaba el laudo como «commit PENDIENTE» | `:386` | hecho (sin commit) | No |
| W6 | Pase de higiene: cola 14 (antes del cierre de la tanda 1), 15 y 16; cola 18 (antes de B6.1) | cola 14, 15, 16 y 18 | registrado | No |
| W7 | **HUECO** — rutas absolutas en los resúmenes del runner de EV2 sobre Neo4j | cola 19 | registrado | No |
| W8 | Línea sobre M50 en el resultado de la lectura de la matriz | `resultado_lectura_matriz.md` | hecho (sin commit) | No |
| W9 | Estructura de los capítulos 3 y 4: el 3, del documento a su análisis y al esquema; el 4, el pipeline componente por componente y la construcción por etapas, con la tanda 0 como primera etapa | `:856` (C1.11) | decidido (30/09) | No |
| W10 | La tesis se cita desde Overleaf, por sección y frase; `docs/tesis/main.tex` del repo está desactualizado. Pendiente de escritura: sincronizar el repo con Overleaf cuando la mesa de escritura cierre una versión | `:856-857` | registrado (pendiente de escritura) | No |
| W11 | Fe de erratas en la fila U-JOB-ACT: lo que cambió en los cinco documentos que no anuncian su cambio son listas de Comunicaciones, no la tabla de origen | `:1163` | hecho (sin commit) | No |
| W12 | U-INSUMOS-CAP: estadísticas descriptivas del corpus desde el segmentador y recorrido del préstamo por componente, para la mesa de escritura | `:403` | hecho: mandato firmado en `30f106c`; I1 en `ded3494` e I2 en `f32f20c`; unidad cerrada; insumos indexados en `docs/insumos_escritura.md` | No |
| W13 | Corregir en la tesis el párrafo de la sección 3.4 según el cual las listas de valores de propiedad no las verifica ningún control, con lo que implemente U-PYD | `:396`; `:856` | registrado | No |
| W14 | Sensibilidad declarada de la atribución A0.2: con la regla exacta, 23 de las 31 ausencias de C1 a C4 son contenido presente bajo puntos descendientes del ancla; la tesis lo declara junto a las clases | `:314`; `reports/u_pre_r2/d2_ausencias.md:46-58` | decidido (30/09) | No |

## Revisado y fuera de esta lista

No figuran como condición de la tanda 1 ni del escalado en lo registrado:
A0.3, A1.5, A1.7, A2.2 a A2.5 (A2.2 aporta el costo de Q6), B2.3, B2.7 (con
la restricción H5 sobre el verificador), B3.1 a B3.4 (las intrínsecas son
informativas en el gate hasta B3.1, `:382`), B4.1 a B4.4 (salvo Q7), B6.2,
B6.4, C1 y C2 (salvo C1.11, en W9, W10 y W13), ESQ-RI-2 a ESQ-RI-4 y U-COB-B.

## Conteos

Cómo recontar: cada fila de las tablas de arriba cuenta como un ítem; el
comando del final de esta sección da el total, los ítems por canal, los que
llevan decisión «Sí» y los HUECO.

```bash
python3 -c "
import re
t=open('docs/checklist_pre_escalado.md',encoding='utf-8').read()
filas=re.findall(r'^\| ([PRXNQW])(\d+) \|(.*)$',t,re.M)
from collections import Counter
print(len(filas),dict(Counter(f[0] for f in filas)))
print('decisión Sí:',sum(1 for f in filas if f[2].rstrip(' |').split('|')[-1].strip().startswith('Sí')))
print('HUECO:',sum(1 for f in filas if 'HUECO' in f[2]))
"
```
