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

Decisión de la autora del 29/09/2026, asentada en las filas B6.1 (`:743`) y
B2.10 (`:382`). Cerrada la tanda 0 (adjudicación ciega de C2 a C5 con el
anexo E5.c, P1, y E6, P2), las unidades de r2 sin cambio de prefijo (canal 1)
y A1.8 (canal 3) pueden avanzar en paralelo con la lectura del capítulo por
los mentores. La tanda 1 depende de tres condiciones:

1. La validación escrita del capítulo, registrada (P6).
2. B2.10 cerrada: r2 versionada con su gate en verde (R26, con lo que el
   laudo firmado incluya del canal 1).
3. La decisión de la autora con los mentores sobre el cambio de prefijo: X1
   (matriz), X2 (prompt), X3 (ventana del §7) y X4 (cuándo va la release de
   prompt).

## 0. Precondiciones y operación del escalado

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| P1 | Adjudicación ciega de C2 a C5, antes de E6 | anexo E5.c `docs/mandatos/UTANDA0_2A_E5c_adjudicacion.md` (firmado, `0488a9b`); `:724` | decidido; despacho del anexo PENDIENTE (no confirmado) | No: marcas de la autora en E5.c.2 |
| P2 | E6: lectura de observaciones y vigilancias y reporte de 2a, puntos (1) a (6) de la lectura | mandato 2a, E6 (`docs/mandatos/UTANDA0_2A_corrida.md:216-234`); `:728` | registrado | No |
| P3 | **HUECO** — punto (6) de E6: aristas entre documentos distintos, por relación, en los tres ensamblados | `:728` (6) | registrado | No |
| P4 | Posición sobre la ventana del §7 por la vía de A8, en el reporte de 2a | mandato 2a, E6 c; `docs/preregistro_tanda0.md:832` (A8) | registrado | Sí |
| P5 | Mentor informado con el reporte de 2a | `:724` | registrado | No: acción de la autora |
| P6 | Gate del capítulo: validación escrita de los mentores sobre el capítulo 3; rige para la tanda 1 y el escalado. **Condición (1) de la tanda 1** | `:137-142`, `:1071` (actualización del 29/09 en los dos) | registrado; PENDIENTE: los mentores leen el capítulo (declaración de la autora del 29/09); la tanda 0 corrió por la decisión del 25/09 (entrada de estado del 11/09) | No: registrar la validación cuando llegue |
| P7 | Decisiones abiertas del gate del capítulo: (1) los ocho límites de la Tabla 4 con destino; (2) principio de gobierno de la enmienda; ítem (a), adenda al laudo congelado por sus nueve filas | `:143-152` | registrado; sin cierre encontrado | Sí |
| P8 | U-COB-A: laudo sobre las 77 unidades del bloque A y `cifras_vigentes.md` (ítem (b), «reemplaza 11» contra «las diez») | `:152-155`, `:708` | registrado | Sí |
| P9 | B5.7: costos con tarifas reales, manifiesto del corpus escalado con `perfil_e1: "v3_b54"`, re-presupuesto de los no-RI antes de la tanda 2 | `:711` | registrado | Sí: presupuesto |
| P10 | Mandato de B6.1: tasas y muestreo de las vigilancias (1) a (9), sellados antes de correr | `:743` | registrado | Sí |
| P11 | Gate de la tanda 1: esqueleto v3 inyectado y S15 en PASS | `:744` | registrado (en la tanda 0, S15 PASS en `cf6ca42`) | No |
| P12 | Gate de la tanda 1: retiro de las tres `aplica_a` de U-COB-A si sus TOs entran | `:745` | registrado (en la tanda 0, 0 de 3 porque sus TOs no estaban) | No |
| P13 | La tanda 1 pasa por r1: mecánica a fijar en el mandato | `:746`; precedente, gate 1 de la tanda 0 (`47c9283`) | registrado | No |
| P14 | Observaciones (10), (11) y (12) de la tanda 1 contra sus líneas de base | `:747`, `:748` | registrado | No |

## 1. r2 sin prefijo

Avanza en paralelo con la lectura del capítulo una vez cerrada la tanda 0.

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| R1 | Firma del laudo de release r2 | laudo, «Firma»; `:382` paso (1) | registrado (BORRADOR) | Sí |
| R2 | `BKL-0030`: reintento por corte y partición; (a) sola o (a) con partición | laudo §1.1 y §4 (fila de `cap::4.2.1.2`); `BKL-0030`; `:383` (1) | registrado | Sí |
| R3 | Doble conteo del checkpoint de cierre del runner | laudo §1.6 (recomendación: entra con R2) | registrado | Sí (laudo §5, 1) |
| R4 | `BKL-0031`: detector de duplicados y fusión solo de forma; umbral del paso 3 | laudo §1.2 y §5 (3); `BKL-0031`; `:383` (2) | registrado | Sí |
| R5 | RX-10 / `BKL-0006`: cablear el parser de tablas a E0; censo en USD 0 antes de costear | laudo §1.3 y §5 (5) | registrado | Sí: tope |
| R6 | `cuarentena` booleana contra `"true"` en T7; su entrada de backlog se escribe al firmar | laudo §1.4 | registrado; sin entrada de backlog | Sí (laudo §5, 6) |
| R7 | Test de la cláusula de mutuales (RT-C6), opción (c) | laudo §1.5 y §5 (2) | registrado | Sí |
| R8 | Completar `esquema_v3_clases.json` con los seis ids del perfil | laudo §1.6 (recomendación: entra); `:725` | registrado | Sí (laudo §5, 1) |
| R9 | Pendientes de U-B1a: rangos, 196 conflictos de properties, 5 cross-TO, 41 `padre_sugerido`, política de cola | laudo §1.6; cola 8 | registrado | Sí |
| R10 | Guarda de modalidad (deber emitido como Condicion) | laudo §1.6; cola 12 | registrado; no entra salvo que la vigilancia (1) lo pida | Sí, tras E6 |
| R11 | H1 y H4: remisiones desde Condicion, Potestad y Definicion, y lectura de `termino` | laudo §4 | registrado | Sí |
| R12 | Remisiones falsas por paráfrasis: detectar sobre el texto de E0, no sobre la descripción | laudo §4; `:383` (3) | registrado; corrección previa a la tanda 1 | Sí |
| R13 | H2: fusión por label de Condicion, Definicion y Potestad (cambia ids y la fixture) | laudo §4 | registrado | Sí |
| R14 | Nodos aislados: derivar `establecida_en` de la procedencia en el ensamblado | laudo §4 | registrado | Sí |
| R15 | Procedencia de las remisiones: resolver desde cada procedencia; vista del agente | laudo §4 (dos filas) | registrado; alcance a definir | Sí |
| R16 | Test de la suite: el ejemplo `cla::5.1.1.1` | laudo §4 (entra con el gate) | registrado | No: la autora sella la entrada de la fixture |
| R17 | Control de aristas entre nodos con la misma descripción (M50, idéntica y correcta) | laudo §4 (fila del 29/09) | registrado; alcance a medir | Sí |
| R18 | B2.9: detector de huérfanos de label | `:381`; no figura en el laudo de r2 | registrado | Sí: si entra |
| R19 | Entrada de r2 en la fixture, sellada antes del gate, con su política de cuarentena | laudo §3.1 (2) y §5 (6) | registrado | Sí |
| R20 | Corpus sobre el que se materializa r2: los cinco de desarrollo o los diez | laudo §5 (4) | registrado | Sí |
| R21 | Tope de gasto de la release | laudo §5 (5) | registrado | Sí |
| R22 | Copia de resguardo de las dbs de caché, fuera del repo, antes de la corrida de r2 | laudo §2 y §3.2 (6) | registrado | No |
| R23 | Proyección de misses antes de pagar; un miss de más es FRENO | laudo §3.2 (5) | registrado | No |
| R24 | **HUECO** — muestra de precisión de aristas sobre r2 con el método de (12), como evidencia que no usa EV2 | laudo §5 (7) | registrado | Sí |
| R25 | Tests de la observación (12): se revisan después de r2, direccionados por (chunk_id, relación, tipo de destino) | `:729` | decidido (28/09) | No |
| R26 | Gate de release y versionado de KG-Reextraído-r2. **Condición (2) de la tanda 1** | laudo §3.1; `:382` pasos (3) y (4) | registrado | No |

## 2. Cambio de prefijo con enmienda

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| X1 | Enmienda de la matriz congelada: → Operacion cumple el criterio (27 de 29, piso 0,780); → Potestad no (27 de 30, piso 0,744) | `:727`; `reports/u_estudio_matriz/lectura/resultado_lectura_matriz.md` | registrado; resultado del protocolo, sin decidir la enmienda | Sí, con los mentores; condición (3) de la tanda 1 |
| X2 | Si se amplía la matriz: cambiar el prompt (rota el prefijo; la tanda 0 se re-extrae o se revalida declarando la mezcla) o ampliar solo el validador | `:727` | registrado | Sí, con los mentores; condición (3) de la tanda 1 |
| X3 | Ventana única del §7: si se usa después de la tanda 0, la tanda 1 ya no la tiene y los cinco de la tanda 0 salen del conjunto final de B6.3 | `:727`; `docs/preregistro_tanda0.md:832` (A8, decisión 4) | registrado | Sí; condición (3) de la tanda 1 |
| X4 | Cuándo va la release de prompt: antes o después de la tanda 1 (la §3.2 del laudo de r2 no admite cambios al prefijo) | `:727`; laudo §3.2 (1) | registrado | Sí, con los mentores; condición (3) de la tanda 1 |
| X5 | `BKL-0032`, `BKL-0033`, `BKL-0035`, `BKL-0036`: incorrectas `E1-prompt` de la observación (12) | backlog; `:729` | registrado | Sí (con X4) |
| X6 | `BKL-0034`: el catálogo v3 no tiene sujeto de nivel órgano | backlog; laudo §4 (fila del 29/09) | registrado | Sí (con X4) |
| X7 | `BKL-0028` y `BKL-0029`: cambios del catálogo v3 del prefijo | backlog; laudo §1.6 (no entran a r2) | registrado | Sí (con X4) |
| X8 | Remedio de raíz de la cláusula de mutuales: regla de calificadores en E1 | laudo §1.5 (a) | registrado; fuera de r2 | Sí (con X4) |
| X9 | B2.4: laudo de los 15 `triaged`; nueve de asignación de sujeto piden una corrección sistemática vía prompt o validador de E1 | `:376` | registrado | Sí |
| X10 | R6b: residuo del esquema | laudo §1.6 (solo por la vía de A8) | registrado | Sí |

## 3. Búsqueda y navegación (A1.8)

A1.8 avanza en paralelo con r2 y con la lectura del capítulo una vez cerrada
la tanda 0, y va antes de A2.1 y B6.3 (`:323`, `:743`); no es condición de la
tanda 1.

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| N1 | Diagnóstico sin API en cuatro capas (entrada, alcance, navegación, respuesta) sobre preguntas de desarrollo y trazas de C1 a C5 | `:323` | registrado | No |
| N2 | **HUECO** — tope de 15 herramientas: 23 de 40, 27 de 40, 17 de 40 y 11 de 20 respuestas base de C2 a C5; 28 de 40 en C1 | `:323` | registrado | No |
| N3 | Patrón de navegación en las trazas de la tanda 0 y atribución de la respuesta invertida | `:728` (4) y (5) | registrado | Sí, si resulta sistemático |
| N4 | H3: el índice full-text no incluye `termino` | `:323` | registrado | Sí (entra entre las mejoras) |
| N5 | Qué mejoras entran: búsqueda, herramientas, instrucciones, tope de llamadas | `:323` | registrado | Sí |
| N6 | Criterio de aceptación de A1.8 | `:323` | registrado | Sí |
| N7 | Configuración del agente congelada y declarada antes del pre-registro de B6.3 | `:323`, `:750` | registrado | No |

## 4. Pre-registro de A2.1 y B6.3

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| Q1 | A2.1: prerrequisito H-B2 (`num_turns` contra `--max-turns`; criterio de corte R5) | `:331` | registrado | No |
| Q2 | Mismo analizador y modo en las dos búsquedas léxicas, o la diferencia declarada | `:323`, `:331`, `:750` | registrado | Sí: declarar |
| Q3 | Vocabulario de las preguntas de B6.3 | `:323`, `:750` | registrado | Sí |
| Q4 | Cuotas de preguntas de varios puntos y de abstención en el conjunto final | `:753` | registrado | Sí, con los mentores |
| Q5 | **HUECO** — tamaño del conjunto final por potencia y análisis pareado; con 40 preguntas, los intervalos de C1 a C4 se solapan | `:750` | registrado | Sí: cálculo |
| Q6 | Costo del agente medido en A2.2 antes de sellar B6.3 | `:750` (fórmula del brazo) | registrado | No |
| Q7 | Inconsistencia B4.2 contra B6.3 (d): instrumento de tripletas «ya validado» con su adjudicación abierta | `:424` | registrado; sin resolver | Sí |
| Q8 | Unidad de calibración del juez antes de B6.3 | cola 13 | registrado | No |
| Q9 | Regla de cegado en lecturas humanas y entrada de textos largos del instrumento de lectura | cola 10 y 11 | registrado | No |
| Q10 | Disjunción del conjunto final con desarrollo y con los diez de ESQ; también con la tanda 0 si se usa la ventana | `:750` (a); `:727` | registrado | Sí (depende de X3) |
| Q11 | Ciclo de corrección de esquema de la tanda 1, siempre antes del pre-registro de B6.3 | `:743` | registrado | No |

## 5. Escritura

| # | Qué es | Registro | Estado | Decisión |
|---|---|---|---|---|
| W1 | Tabla de reproducibilidad: modelo, versión con fecha, temperatura, vía (API o Claude Code), por medición y por etapa | `:832` (precisión por etapa del 29/09); `docs/registro_modelos.md` NO ENCONTRADO | registrado | Sí: aprobar el documento |
| W2 | B2.5: spec del backlog con `capa_pipeline` obligatorio y dos vías; huecos del catálogo de especies (cola 17; especies provisionales de `BKL-0032`, `BKL-0033` y `BKL-0035`) | `:377`; cola 17; backlog | registrado | Sí: ampliar el catálogo |
| W3 | B2.6: protocolo de releases escrito; `docs/protocolo_ciclo_refinamiento.md` NO ENCONTRADO | `:378` | registrado | Sí: antes o después de r2 |
| W4 | B2.8: método de construcción y refinamiento, «el que se sigue en B6»; `docs/metodo_construccion_refinamiento_kg.md` NO ENCONTRADO | `:380`, `:743` | registrado | Sí: antes o después de la tanda 1 |
| W5 | **HUECO** — la fila B2.10 citaba el laudo como «commit PENDIENTE» | `:382` | hecho (sin commit) | No |
| W6 | Pase de higiene: cola 14 (antes del cierre de la tanda 1), 15 y 16; cola 18 (antes de B6.1) | cola 14, 15, 16 y 18 | registrado | No |
| W7 | **HUECO** — rutas absolutas en los resúmenes del runner de EV2 sobre Neo4j | cola 19 | registrado | No |
| W8 | Línea sobre M50 en el resultado de la lectura de la matriz | `resultado_lectura_matriz.md` | hecho (sin commit) | No |

## Revisado y fuera de esta lista

No figuran como condición de la tanda 1 ni del escalado en lo registrado:
A0.3, A1.5, A1.7, A2.2 a A2.5 (A2.2 aporta el costo de Q6), B2.3, B2.7 (con
la restricción H5 sobre el verificador), B3.1 a B3.4 (las intrínsecas son
informativas en el gate hasta B3.1, `:378`), B4.1 a B4.4 (salvo Q7), B6.2,
B6.4, C1 y C2, ESQ-RI-2 a ESQ-RI-4 y U-COB-B.

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
