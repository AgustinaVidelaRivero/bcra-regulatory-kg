# Tablero de correcciones: síntomas de la tanda 0, su corrección y su prueba

Tablero único que conecta cada síntoma medido en la tanda 0 con la corrección
que lo ataca y con la forma de volver a medirlo. Lo escribí el 29/09/2026
sobre HEAD `05465e9`. Es condición de la tanda 1: la columna «después de r2»
completa, con cada meta cumplida o su residuo declarado (laudo de r2, §3.1,
punto 8; `docs/checklist_pre_escalado.md`, «Orden y condiciones de la tanda
1»). Las columnas «después de r2» y «tanda 1» se llenan al cerrar esas
unidades, con el mismo comando.

**Actualización del 30/09/2026** (decisiones de la autora del 30/09; plan, fila
B2.11). La columna «después de r2» se parte en dos: **r2a**, solo código sobre la
salida guardada de la tanda 0, antes de re-extraer; y **r2b**, prompt nuevo y
re-extracción de la tanda 0. Así se separa lo que corrige el código de lo que corrige
el prompt. Se suman siete filas (desde la afirmación falsa de `cap::1.2`) y una tabla
de requisitos de mantenimiento, que no son síntomas de la tanda 0. Actualizado otra vez
el 30/09 con los resultados de U-PRE-R2-DIAG (`159c1e2`): la fila de clases de falla
A0.2 lleva la lectura de D2 y se suma la fila de pérdidas por tablas. La fila de
`cap::1.2` corrige su etiqueta: el defecto es el de `BKL-0006` (`BKL-0023`, su rastro en
el nodo de compañías financieras, no reaparece). Se suma la fila de colisiones de ids de
chunk en E0 (`BKL-0037`). Correcciones de la mesa del 30/09: las filas de omisiones y de
crudo del reintento leen `salida_dirigida/`, la salida de la que salen los ensamblados; la
nota de Obligacion.tipo de desarrollo; la prosa de [c14], que no declaraba la cifra entre
paréntesis; y la detección de tablas en la fila de pérdidas por tablas. La fila del test
del ejemplo `cla::5.1.1.1` suma la meta explícita de U-REEXT-T0.

**Grafos y celdas.**

| Nombre | Grafo | sha256 | Celdas |
|---|---|---|---|
| r1 | KG-Reextraído-r1 | `0226e947…` | C1 (memoria) y C2 (Neo4j) |
| desarrollo | KG-Tanda0-Desarrollo-r1 | `eab2fdd0…` | C3 (memoria) y C4 (Neo4j) |
| cinco | ensamblado de la tanda 0 sola | `4097d4fd…` | — |
| diez | KG-Tanda0-Diez-r1 | `dd42d6d9…` | C5 (memoria) |

**Reglas.**
- Las corridas del agente sobre preguntas de desarrollo son diagnóstico, no
  resultado: EV2 no se re-mide como resultado (principio 7; plan, fila A1.8),
  y el gate de r2 nunca usa EV2 (laudo §3.1, punto 7).
- Toda cifra sale del comando indicado entre corchetes (sección
  «Comandos»).
- Donde no hay meta definida, dice «DECISIÓN ABIERTA de la autora».

## Tablero

| Síntoma | Métrica y cómo se calcula | Valor en r1 | Valor en la tanda 0 | Meta | Corrección que lo ataca | Cómo se re-mide y costo | Después de r2: r2a (solo código) | Después de r2: r2b (prompt y re-extracción) | Tanda 1 |
|---|---|---|---|---|---|---|---|---|---|
| **Observación (10):** extracción más magra | Aristas de extracción por unidad, solo las que emite el extractor: (total − `referencia` − `rol_fuente` esqueleto − `establecida_en` derivadas por el ensamblado) / unidades del `kg.json` [c1]. Las `establecida_en` derivadas (si esa corrección entra en r2) se identifican por el `rol_fuente` propio que declare la unidad que las derive; hoy no existen y los valores no cambian. Como en el pre-registro, la resta incluye las `cuarentena_flaggeada` (`padre_sugerido` de E5): 41 en r1, 18 en desarrollo, 11 en cinco y 29 en diez. **Decisión de la autora del 29/09/2026:** el tablero usa la resta del pre-registro, por comparabilidad con las bandas y la línea de base; la variante estricta, sin las `cuarentena_flaggeada`, queda como dato secundario (valores en [c1]) | 6,81 (12.010 / 1.763) | desarrollo 6,03 (10.634 / 1.763); cinco 4,99 (3.345 / 671); diez 5,74 (13.979 / 2.434) | Referencia: las bandas pre-registradas, 6,81 a 8,0 en desarrollo y 5,0 a 8,0 en cinco (predicciones, no metas). Meta para r2: DECISIÓN ABIERTA de la autora. **Propuesta, a confirmar con los mentores (no es meta):** volver al nivel de r1 en desarrollo, 6,81 | Matriz congelada (checklist X1, X11; plan `:748`); `establecida_en` derivada (laudo §4, nodos aislados); cambios de prompt (X4, X5; en el ciclo B2.11 desde el 30/09) | Matriz y `establecida_en`: revalidación desde el crudo y re-ensamblado, USD 0 (re-verificar en E3, cota del orden de USD 4, plan `:748`). Prompt: re-extracción (referencia: E2 de la tanda 0, USD 40,35) | | | |
| **Observación (11):** menos remisiones entre documentos | `aristas_cross_to` del reporte de ensamblado, y menciones [c2] | 188 (1.089 menciones) | desarrollo 124 (783); cinco 3 (169); diez 186 (952) | Referencia: desarrollo 188 ± 20; diez mayor que 188 (predicciones). Meta para r2: DECISIÓN ABIERTA de la autora. **Propuesta, a confirmar con los mentores (no es meta):** volver al nivel de r1 en desarrollo, 188 | H1 y H4, remisiones por paráfrasis y procedencia de las remisiones (laudo §4) | Re-ensamblado, USD 0 | | | |
| **Aristas `referencia` por tipo de origen:** ninguna sale de Condicion, Potestad ni Definicion | Aristas `referencia` cuyo origen es de esos tres tipos [c3] | 0 (r1 no tiene nodos Condicion) | 0 en desarrollo, cinco y diez | Laudo §4, H1 y H4: re-ensamblar el desarrollo da +3.687 aristas, 0 perdidas, y la remisión de `cla::5.1.1.1` al `cla::3.7` | H1 y H4 (laudo §4) | Re-ensamblado, USD 0 | | | |
| **Condiciones aisladas** | Nodos Condicion sin ninguna arista, y aislados por tipo [c3] | No aplica: 0 nodos Condicion. Aislados de todo tipo: 105 | desarrollo 35 de 1.178 Condicion (94 aislados en total); cinco 7 de 205 (38); diez 42 de 1.383 (120) | Laudo §4: cero nodos de contenido sin `establecida_en`; el resto de los aislados, declarado por causa | `establecida_en` derivada de la procedencia (laudo §4, decisión abierta); matriz, rango de `condicion_de` (X1, X11) | Re-ensamblado, USD 0; la matriz, como en la observación (10) | | | |
| **Remisiones falsas por paráfrasis** | Aristas `referencia` de `cap::8.2.3.3` hacia nodos de `cap::6.5.1` [c3] | 0 | desarrollo 9; diez 9; cinco no aplica (no tiene cap) | Laudo §4: detección sobre el texto de E0; `cap::8.2.3.3` llega a `cla::6.5.1` y `cla::7.2.1`; cuántas remisiones cambian de destino en diez | Remisiones falsas por paráfrasis (laudo §4; plan `:387`, punto 3) | Re-ensamblado, USD 0 | | | |
| **Test del ejemplo `cla::5.1.1.1`** | La Operacion con sus dos condiciones unidas y la remisión al `cla::3.7`; test nuevo de la suite, todavía no escrito [c4] | Se cumple (recorrido de la mesa en U-CONS-EJEMPLO-Y-BUSQUEDA, A3) | desarrollo: persiste (ídem); diez: NO MEDIDO | Laudo §4: «resuelto» sobre el grafo de r2. **Meta explícita de U-REEXT-T0 (decisión de la autora del 30/09):** el ejemplo queda representado en el grafo re-extraído, con la condición conjunta, su relación con la operación y la remisión al 3.7, porque es el ejemplo de toda la tesis. Hoy, en desarrollo, el punto son 2 Condicion, 1 Definicion y 1 Operacion, sin `limita` ni remisión al 3.7 (`reports/u_insumos_cap/recorrido_prestamo.md`, `f32f20c`; recomputado por la mesa) | Test nuevo, con entrada de la fixture sellada por la autora (laudo §4); H1 y H4; condiciones aisladas | Suite, USD 0. **Seguimiento opcional, después de U-REEXT-T0:** re-correr `reports/u_insumos_cap/u_insumos_i2.py` sobre el grafo de r2, parametrizando la ruta del grafo (USD 0) | | | |
| **Regresiones de la suite contra r1** | Estados de los 46 ítems (resuelto / persiste / no aplica) contra la entrada de r1 de la fixture (`696f3f94…`) [c4] | Entrada de r1: 27 / 10 / 9 | desarrollo 22 / 16 / 8, con 6 ítems de resuelto a persiste (E4-a7, E4-a8, T2, T4, T5, T7); cinco 11 / 22 / 13 y diez 20 / 18 / 8, informativos | Laudo §3.1, punto 2: 0 regresiones contra la entrada de r2 sellada por la autora | U-PRE-R2-DIAG, D1 (checklist R27; `docs/mandatos/UPRE_R2_diagnostico.md`), commiteado en `159c1e2`; propuestas de D1 en U-R2-CODIGO (plan, B2.11, unidad 8) | Suite sobre el `kg.json` de r2, USD 0 | | | |
| **Patrón de navegación (a):** ancla vista por `referencia` sin abrir | Trazas y nodos en que un nodo que porta el ancla aparece como vecino por `referencia` y nunca recibe `ver_nodo` (trazas base y §7) [c5] | C2: 4 trazas y 20 nodos de 112 trazas; C1: NO MEDIDO | C3 0 de 96; C4 2 trazas y 5 nodos de 101; C5 0 de 43 | DECISIÓN ABIERTA de la autora (criterio de aceptación de A1.8) | A1.8: instrucción de abrir los destinos de las remisiones (checklist N5) | Corrida del agente sobre preguntas de desarrollo: agente base, entre USD 1,21 y 1,30 por celda de 40 preguntas (E5) | | | |
| **Patrón de navegación (b):** vecinos solo salientes sobre una Operacion con restricciones entrantes | Llamadas a `ver_vecinos` salientes sobre esa Operacion, y trazas con esa llamada [c5] | C2: 22 llamadas en 19 trazas; C1: NO MEDIDO | C3 12 en 11; C4 16 en 12; C5 4 en 4 | DECISIÓN ABIERTA de la autora; el patrón se declaró sistemático el 29/09 | A1.8: vecinos en las dos direcciones o entrantes normativas marcadas, e instrucciones (checklist N3, N5) | Corrida del agente, como en (a) | | | |
| **Tope de herramientas alcanzado** | Trazas base con `hit_tool_limit` (tope de 15) [c6] | C1 28 de 40; C2 23 de 40 | C3 27 de 40; C4 17 de 40; C5 11 de 20 | DECISIÓN ABIERTA de la autora | A1.8: tope de llamadas y herramientas (checklist N5) | Corrida del agente, como en (a) | | | |
| **Incorrectas de la observación (12), por capa** | Muestra de 30 aristas de extracción leídas contra el texto; lectura asistida, instancia de modelo revisada por la autora [c7] | Sin línea de base | cinco: 25 correctas de 30 (Wilson 0,664–0,927); incorrectas: 4 `E1-prompt` y 1 `catálogo` | DECISIÓN ABIERTA de la autora | `E1-prompt`: `BKL-0032`, `BKL-0033`, `BKL-0035` y `BKL-0036`, en el ciclo B2.11 desde el 30/09 (X5, U-PROMPT-R2). `catálogo`: `BKL-0034` (X6). En r2: muestra de precisión sobre r2 (laudo §5, decisión 7; checklist R24) | Nueva muestra de 30 aristas con el método de (12); quién lee se decide antes (checklist P15, Q12); USD 0 si lee una persona | | | |
| **Clases de falla A0.2** | Clase de la traza representativa de cada par definitivo parcial o incorrecto: ausencia / estaba y no se navegó / generación [c8] | C1 8 / 8 / 18; C2 6 / 2 / 23 | C3 8 / 7 / 15; C4 9 / 3 / 17; C5 0 / 4 / 8 | DECISIÓN ABIERTA de la autora | Ausencias, según D2 de U-PRE-R2-DIAG (`159c1e2`; lectura aceptada por la autora el 30/09): de las 31 de C1 a C4, 23 son contenido presente bajo puntos descendientes del ancla (categoría P, 7 preguntas; la regla de A0.2 es de coincidencia exacta), que no son pérdida del pipeline y pasan a A1.8 (el agente tiene que bajar de un punto padre a sus hijos; checklist N9) y a la sensibilidad declarada de la atribución (W14); las 8 restantes son pérdidas reales asociadas a tablas (fila «Pérdidas de contenido por tablas»); la matriz no es causa principal de ninguna (3 como secundaria). Navegación: A1.8 (N3, N5). Generación: instrucciones de respuesta (N8) | Corrida del agente con juez N=3 y §7 sobre preguntas de desarrollo, entre USD 6,14 y 6,66 por celda de 40 (E5); atribución, USD 0 | | | |
| **Unidades cortadas o mudas** | M10, chunks mudos sobre unidades de E0 [c9] | 1 de 1.763 | desarrollo 3 de 1.763; cinco 1 de 671; diez 4 de 2.434 | `BKL-0030`: cero unidades con error definitivo por corte; M10 en 0 sobre los TOs de desarrollo | Reintento por corte y partición (laudo §1.1, `BKL-0030`) | Re-extracción dirigida de las unidades afectadas; menos de USD 1 (laudo §1, resumen) | | | |
| **Afirmación falsa por tabla no detectada (`cap::1.2`, `BKL-0006`)** | Montos de las dos Restricciones de `cap::1.2` con `umbral`, contra el PDF (bancos 5.000; restantes entidades 2.500; `data/backlog/propuestas/C2_montos_12.md:31-32`); estado de `BKL-0006` y `BKL-0023` en la suite [c10] | Invertido: bancos 2.500, restantes 5.000. Suite: `BKL-0006` persiste, `BKL-0023` no aplica (entrada de r1, `696f3f94…`) | desarrollo y diez: invertido, con los mismos valores; en desarrollo la suite da no aplica en los dos ítems, un falso negativo; cinco: no aplica (no tiene cap). E0 no marca `cap::1.2` como tabla | Los dos montos iguales al PDF, o el valor omitido con omisión registrada, sin afirmación falsa; `BKL-0006` y `BKL-0023` aplicables y en «resuelto» | U-R2-CODIGO: detección de tablas en E0 (RX-10, `BKL-0006`) y matchers de la suite por punto y monto (plan, B2.11, unidad 8; decisión de la autora del 30/09) | r2a: detección y marca en código sobre lo guardado, USD 0; r2b: re-extracción del chunk marcado, dentro de U-REEXT-T0 | | | |
| **Pérdidas de contenido por tablas** | Ausencias de C1 a C4 (pares definitivos parciales o incorrectos de clase A0.2 ausencia) cuya categoría primaria en D2 es E-tabla, o G con la secundaria E-tabla-no-marcada [c17] | C1 2 y C2 2: EV2F-031 (`ric:7.2`, tabla marcada por E0 y sin extracción) y EV2F-032 (`ric:9.2`, cuadro de códigos que E0 no marca) en cada celda | C3 2 y C4 2: las mismas dos preguntas en cada celda; C5 no medido (D2 cubre C1 a C4). Detección de tablas en la E0 de la tanda 0 (U-UMBRAL U1, `reports/u_umbral/u1_mediciones.json`, `medicion_2`): 4 chunks de ponderadores de cap que ni E0 ni `e0_tablas` detectan (`cap::2.12.2.5`, `2.12.2.6`, `2.12.2.8` y `2.12.3.2`, 6 nodos con `umbral` cada uno en desarrollo) y 12 donde `e0_tablas` detecta tabla sin marca de E0 (entre ellos `ric::9.2.1` y `cap::4.2.1.1`) | DECISIÓN ABIERTA de la autora | Tratamiento de tablas, primera prioridad de U-R2-CODIGO: `BKL-0006`, RX-10 y detección en E0, incluidos los cuadros de códigos que E0 no marca (plan, B2.11, unidad 8; decisión de la autora del 30/09). Conectar `e0_tablas` a las marcas de E0 cubre los doce; los cuatro necesitan detección propia | Presencia de la cita de esos criterios en el grafo de r2 con las reglas de D2 (R-CITA y R-PRES), sin correr el agente, USD 0 | | | |
| **Valores fuera de lista cerrada** | Nodos con valor fuera de la lista del prefijo, por campo (Restriccion.tipo, Comunicacion.tipo, Obligacion.tipo contra el enum de 6), y claves de properties fuera de la definición de cada tipo [c11] | Restriccion.tipo 0; Comunicacion.tipo 14 (11 valores distintos); Obligacion.tipo 1 (`verificacion_informativa`); claves fuera 12 | desarrollo: Restriccion.tipo 4 (`limite_temporal` 3, `obligacion_cualitativa` 1), Comunicacion.tipo 6, Obligacion.tipo 0 (el crudo de desarrollo no tiene valores fuera del enum; las 3 normalizaciones de E1 a «otra» son de cinco), claves fuera 9; cinco: 0 / 2 / 0 y claves 4; diez: 4 / 8 / 0 y claves 13 | Cero valores fuera de lista sin tratar: cada uno rechazado, normalizado con contador o registrado, según la política por campo de L-ESQ-R2. La política: DECISIÓN ABIERTA de la autora | U-PYD con la política de L-ESQ-R2 (plan, B2.11, unidades 5 y 7) | r2a: validación sobre el crudo guardado, USD 0 | | | |
| **Mención del sujeto sin guardar; sujetos no mapeables** | Relaciones `aplica_a` y `ejecuta` extraídas (sin las de esqueleto) con la mención textual del sujeto guardada; propuestos de E4 resueltos y en cuarentena [c12] | 0 de 3.341 con mención (el campo no existe); propuestos 44: 3 resueltos y 41 en cuarentena | desarrollo 0 de 3.019, propuestos 22: 3 y 19; cinco 0 de 1.025, 12: 1 y 11; diez 0 de 4.044, 34: 4 y 30 | Toda relación con sujeto lleva su mención, verificada contra el chunk; los no mapeados, registrados y re-resueltos por programa al crecer el catálogo. Meta de resueltos: DECISIÓN ABIERTA de la autora | U-LISTAS-NOMAP, L-ESQ-R2, U-PROMPT-R2 (mención) y E4 generalizado (plan, B2.11, unidades 4, 5 y 10) | Mención: r2b (requiere el prompt). Re-resolución: E4 sobre lo guardado, USD 0 | | | |
| **Catálogo de sujetos en dos fuentes** | Ids del bloque de catálogo del prompt contra ids del JSON que usan E4 y el esqueleto [c13] | 0 / 0: el enum y E4 salen del mismo `esquema_v2_clases.json` (`data/experiment/grafo_v2/code/schema.py:86-100`) | perfil v3: 102 contra 101; 6 ids solo en el bloque y 5 solo en el JSON | Una sola fuente: 0 / 0, con el bloque del prompt regenerado byte a byte desde el JSON | U-CAT-UNICO (plan, B2.11, unidad 6) | Selftest, USD 0 | | | |
| **Cuantías sin campo estructurado** | Nodos Restriccion, Condicion, Obligacion y Excepcion con cuantía en la descripción (regex estricta: porcentaje, «veces», plazo o monto) y sin `umbral` ni `plazo` [c14] | 218 sin campo de 639 con cuantía (Restriccion 63, Obligacion 106, Excepcion 49; r1 no tiene Condicion) | desarrollo 287 de 606 (Restriccion 34, Condicion 134, Obligacion 76, Excepcion 43); cinco 36 de 77; diez 323 de 683 | DECISIÓN ABIERTA de la autora (U-UMBRAL y L-ESQ-R2) | U-UMBRAL y L-ESQ-R2; según la opción elegida, U-PYD o U-PROMPT-R2 (plan, B2.11, unidades 3, 5, 7 y 10) | Conteo, USD 0 | | | |
| **Omisiones sin registro fuera de los chunks marcados** | Unidades con `omisiones_no_prosa` no vacío en la salida final de E1 a E3; la regla 9 del prefijo (contenido meta-normativo) omite sin dejar registro [c15] | 81 de 1.763 | desarrollo 78 de 1.763; cinco 7 de 671; diez 85 de 2.434, sobre `salida_dirigida/` (la versión anterior de esta fila leía `salida/` y daba 77 y 84) | DECISIÓN ABIERTA de la autora (L-ESQ-R2: omisiones con categoría y tramo literal en todo chunk) | U-LISTAS-NOMAP, L-ESQ-R2 y U-PROMPT-R2 (plan, B2.11, unidades 4, 5 y 10) | r2b (requiere el prompt) | | | |
| **Crudo del reintento de E3 sin persistir** | Unidades aceptadas tras reintento en E3, cuyo crudo del reintento no está en `finales.jsonl` [c16] | 330 de 1.763 finales | desarrollo 168 de 1.760; cinco 52 de 670; diez 220 de 2.430, sobre `salida_dirigida/` (la versión anterior de esta fila leía `salida/` y daba 167 de 1.757 y 219 de 2.427) | Cero unidades sin el crudo del reintento persistido, en las corridas de r2 | U-R2-CODIGO (plan, B2.11, unidad 8) | Conteo sobre las salidas de U-REEXT-T0, USD 0 | | | |
| **Colisiones de ids de chunk en E0 (`BKL-0037`)** | Ids de chunk repetidos dentro de un mismo TO, en la E0 de cada conjunto [c18] | 0 en la E0 de r1 (1.763 chunks) | 0 en la E0 de la tanda 0 (2.434 chunks). En la partición del corpus escalado, que alimenta las tandas siguientes: 69 ids repetidos en 4 TOs (adfsp 9, ceninf 4, cirmo3 52, ri_niif 4) | 0 ids repetidos en la E0 de toda tanda, y el runner se detiene ante un id repetido | U-R2-CODIGO: ids únicos en E0 y runner que se detiene (plan, B2.11, unidad 8; decisión de la autora del 30/09). Ningún TO con ids repetidos entra a una tanda sin la corrección (fila B6.1) | Conteo sobre `chunks_<to>.json` y selftest del runner, USD 0 | | | |

## Requisitos de mantenimiento (30/09/2026)

No son síntomas de la tanda 0: son requisitos de la tesis y del repo (plan, fila
B2.11, unidades 12 y 13; checklist P17 y P18). Se llenan al cerrar cada unidad.

| Requisito | Métrica | Estado al 30/09 | Meta | Unidad | Cómo se mide y costo | Al cierre de la unidad |
|---|---|---|---|---|---|---|
| **Control de los supuestos del sitio del BCRA, con aviso** | Supuestos declarados con línea de base y aviso ante cambios | 0: U-JOB-ACT se hizo sin avisos por mandato (plan, fila U-JOB-ACT, cota (a), revocada el 30/09) | Control operable, con aviso, sobre los supuestos que declare U-MANT (endpoint del índice y sus claves, cantidad de TOs, patrones de URL, acierto de las regex de portada y pie, marcadores de página de E0) | U-MANT | Corrida del control, USD 0 | |
| **Tabla de qué obliga a reprocesar todo y qué no** | Tabla escrita en el repo y verificada contra la clave de caché de E1 | No existe en el repo | Tabla en el repo, citada por la tesis | U-MANT | USD 0 | |
| **Actualización solo del subgrafo afectado** | Procedimiento de empalme demostrado; unidades re-extraídas contra unidades totales de los TOs que cambiaron en el sitio | No hay procedimiento escrito | Demostrado sobre cap, cla y ric con costo solo de las unidades cambiadas | U-SUBGRAFO | Re-extracción de las unidades cambiadas; costo NO VERIFICADO | |

## Comandos

Todos con `PYTHONDONTWRITEBYTECODE=1`, desde la raíz del repo.

- **[c1]** Observación (10), para cada `kg.json` de la tabla de grafos. `DERIVADAS`
  es el conjunto de valores de `rol_fuente` que la unidad de r2 declare para las
  `establecida_en` derivadas por el ensamblado; hoy está vacío:
  `python3 -c "import json;DERIVADAS=set();k=json.load(open(RUTA));E=k['edges'];rf=lambda e:e.get('rol_fuente') or (e.get('properties') or {}).get('rol_fuente');print(sum(1 for e in E if e.get('relation')!='referencia' and rf(e)!='esqueleto' and not (e.get('relation')=='establecida_en' and rf(e) in DERIVADAS)))"`,
  dividido por las unidades de E0 (1.763, 671 y 2.434). Con `DERIVADAS` vacío
  da los mismos valores que la resta del pre-registro (r1: 12.010, línea de base
  de `docs/preregistro_tanda0.md:481`). La variante estricta, que deja fuera
  también las `cuarentena_flaggeada`, daría 11.969 en r1 (6,79), 10.616 en
  desarrollo (6,02), 3.334 en cinco (4,97) y 13.950 en diez (5,73).
- **[c2]** Observación (11): la clave `referencias` de
  `reporte_ensamblado_r1.json` de cada ensamblado (en r1,
  `corpus_v2/salida_r1/`), con el comando de `docs/preregistro_tanda0.md`
  §A4.2.
- **[c3]** Sobre cada `kg.json`: aristas `referencia` por tipo del nodo de
  origen; nodos sin ninguna arista, por tipo; y aristas `referencia` cuyo
  origen tiene procedencia en `cap::8.2.3.3` y cuyo destino la tiene en
  `cap::6.5.1` o debajo. Recomputado por la mesa el 29/09/2026 con un script
  de una sola pasada; se reescribe tal cual al llenar las columnas nuevas.
- **[c4]** Suite: `scripts/regression_kg.py` sin `--esperado`, con salida en
  `reports/tanda0/regression_ens_*.json`; entrada de r1 en
  `scripts/regression_kg_esperado.json`, clave
  `estado_esperado.KG-Reextraido-r1`; comparación en
  `reports/tanda0/lectura_e6_tanda0.md`. El test de `cla::5.1.1.1` no existe
  todavía: sus valores vienen del recorrido de la mesa, fuente citada en el
  laudo §4.
- **[c5]** `reports/tanda0/atribucion_tanda0.json`, clave
  `celdas.C<n>.patrones_plan_punto_4`; para C1 la clave no existe (NO MEDIDO).
- **[c6]** Trazas base, `trace.hit_tool_limit`: C2 a C5 en
  `data/experiment/ev2_tanda0/trazas/ev2_c*_*/`; C1 en
  `data/experiment/ev2_r1/trazas/ev2_r1_base/`.
- **[c7]** `reports/tanda0/obs12_lectura/veredictos_obs12.csv` y
  `fila_obs12.md`.
- **[c8]** `reports/tanda0/atribucion_tanda0.json`, claves
  `c1.lectura_plan_punto_3` y `celdas.C<n>.pares_definitivos.lectura_plan_punto_3`.
- **[c9]** `reports/tanda0/lectura_e6_tanda0.json`, clave
  `intrinsecas.<grafo>.M10_chunks_mudos`, multiplicada por las unidades.
- **[c10]** En cada `kg.json`: Restricciones con `umbral` y alguna procedencia con
  `to` = `cap` y `punto` = `1.2`. Suite: ítems `BKL-0006` y `BKL-0023` de
  `reports/tanda0/regression_ens_*.json` y de la entrada de r1 en
  `scripts/regression_kg_esperado.json`. Marca de E0:
  `e0_chunking/salida_tanda0/chunks_cap.json`, `cap::1.2`, `flags.contenido_tabular`.
- **[c11]** Listas del prefijo: Restriccion.tipo ∈ {prohibicion,
  limite_cuantitativo, limite_cualitativo}; Comunicacion.tipo ∈ {A, B, C};
  Obligacion.tipo ∈ enum de 6 del laudo congelado. Claves admitidas por tipo, según
  la definición del prefijo: Comunicacion {codigo, tipo, numero}; TextoOrdenado
  {materia, archivo, version}; Operacion {tipo, descripcion}; Restriccion
  {descripcion, tipo, umbral}; Excepcion, Potestad y Condicion {descripcion};
  Obligacion {descripcion, tipo, plazo, frecuencia}; Definicion {termino,
  descripcion}. Se excluyen los nodos Sujeto y las claves que agrega el pipeline
  (`cola_humana`, `cola_chunks`, `estado_e3`, `colision_cross_to`,
  `materia_variantes`, `version_variantes`). Un valor vacío cuenta como fuera de
  lista.
- **[c12]** Aristas `aplica_a` y `ejecuta` con `rol_fuente` distinto de
  `esqueleto`; `e4_propuestos.json` del ensamblado, campo `estado`.
- **[c13]** `perfil_e1.perfil('v3_b54').esquema.sujetos_catalogo_set` contra los
  ids de `clases` y `roles` de `data/experiment/esq_v3_miembros/esquema_v3_clases.json`.
- **[c14]** Sobre `properties.descripcion` (NFC, sin distinguir mayúsculas):
  - porcentaje: `\d+([.,]\d+)?\s*%` o «por ciento»;
  - `\bveces\b`;
  - plazo: un número en cifras o en letras (un, una, dos, tres, cuatro, cinco, seis,
    siete, ocho, nueve, diez, once, doce, quince, veinte, treinta, cuarenta,
    sesenta, noventa, ciento, cien), **opcionalmente seguido de una cifra entre
    paréntesis** («diez (10) años»), y después día, mes, año, hora o semana, en
    singular o plural; o «días hábiles/corridos»;
  - monto: `$`, `US$`, `U$S` o `USD` seguidos de cifra, o una cifra seguida (con
    «millones de» o «mil» opcionales) de pesos, dólares, USD o UVA. **«€» y «EUR» no
    están incluidos.**
  «Con campo»: `umbral` o `plazo` no vacío.
  **Versión anterior (hasta el 30/09/2026), declarada:** no nombraba la cifra entre
  paréntesis ni la lista de números en letras («un, una, dos… cien»). Implementada al
  pie de la letra da un nodo menos en el total con cuantía (605 en desarrollo, 638 en
  r1, 682 en diez; las cifras «sin campo» no cambian), porque no cuenta «diez (10)
  años». Lo detectó U-UMBRAL U1 (`reports/u_umbral/u1_mediciones.md`) y la mesa lo
  recomputó nodo por nodo; la variante con «€» llega al mismo total por coincidencia,
  porque suma otro nodo.
- **[c15]** Registros de `extracciones_finales_<to>.jsonl` de cada TO con
  `validacion.omisiones_no_prosa` no vacío (r1 en `corpus_v2/salida/`; la tanda 0
  en `corpus_tanda0/salida_dirigida/`, la salida de la que salen los ensamblados),
  sobre las unidades de E0 (1.763, 671 y 2.434). Hasta el 30/09 la tanda 0 se leía
  en `corpus_tanda0/salida/`, que no incluye la re-extracción dirigida de
  `cap::4.2.1.2`; la diferencia la detectó U-LISTAS-NOMAP N1.
- **[c16]** `finales.jsonl` de cada TO, `estado` = `aceptado_tras_reintento`; el
  registro guarda `validacion_final` y no el crudo del reintento. Carpetas: r1 en
  `corpus_v2/salida/`; la tanda 0 en `corpus_tanda0/salida_dirigida/` (hasta el
  30/09 se leía `corpus_tanda0/salida/`).
- **[c17]** `reports/u_pre_r2/d2_ausencias.json`, `filas[]`: `categoria_primaria` =
  `E-tabla`, o `G` con `E-tabla-no-marcada` en `categorias_secundarias`; por `celda`,
  `id_pregunta` y `ancla`. Recomputado por la mesa el 30/09/2026: 4 E-tabla y 4 G, 8 en
  total (2 preguntas en 4 celdas).
- **[c18]** Ids repetidos por TO: `collections.Counter` de los `id` de `chunks_<to>.json`,
  sumando las apariciones de más. E0 de r1 en `e0_chunking/salida_enm01/`, de la tanda 0 en
  `e0_chunking/salida_tanda0/` y del corpus escalado en `segmentacion_84/b584_particion/<to>/`.
  Recomputado por la mesa el 30/09/2026; coincide con `reports/u_insumos_cap/estadisticas_corpus.md`
  §6 (`ded3494`).
- [c10] a [c16] los recomputó la mesa el 30/09/2026 con un script de una sola pasada,
  con doble corrida byte a byte idéntica; se reescribe tal cual al llenar las
  columnas nuevas.
- **Costos citados:** `reports/tanda0/tabla_celdas_E5.json`,
  `celdas.C<n>.gasto`; en la columna de las corridas del agente, el rango es
  el del gasto `agente_base` de C2 a C4.
