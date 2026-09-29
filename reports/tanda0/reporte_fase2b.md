# Reporte de la fase 2b de la tanda 0 (B6.0): segunda emisión del paso 8

Validación de diseño, no resultado de la tesis. Segunda emisión del paso 8 de
A9, que la enmienda de partición 2a/2b emite dos veces, un reporte de 2a y
uno de 2b (`docs/enmienda_preregistro_tanda0_2026-09-27_fase2a2b.md`, §2.2;
`a551c57`). El reporte de 2a es `reports/tanda0/reporte_fase2a.md`
(`2399eb7`). Este reporte no corre nada nuevo: reúne lo que 2b contiene,
desde artefactos commiteados, con el comando o la ruta de cada cifra.
Redactado el 29/09/2026; commit PENDIENTE de la autora.

## 0. Desvíos declarados que condicionan la lectura

- **Lectura de la observación (12).** La hizo una instancia de modelo y la
  autora la revisó (lectura asistida). La enmienda `8e13be3`, §2.1, fijaba
  lectura de la autora
  (`docs/enmienda_preregistro_tanda0_2026-09-27_observacion12.md:91`).
  Declarado en `reports/tanda0/obs12_lectura/fila_obs12.md`, «Desvío
  declarado» (`aa7ee11`).
- **Adjudicación de C5.** La ejecutó la instancia adjudicadora, con
  calibración parcial de la autora. Es un desvío del pre-registro
  (`docs/preregistro_tanda0.md:308-309`) y del anexo E5.c (decisión 5); ver
  el reporte de 2a, §0.
- Modelo y versión de las instancias: a confirmar por la autora.

## 1. Qué contiene 2b

Según la enmienda `a551c57`, §2.1:
- **Preguntas nuevas sobre los cinco documentos** (ctacte, lingob, polcre,
  pagjub y docvig), generadas por una instancia aislada a partir de los PDF,
  aprobadas por la autora, clasificadas con la regla v2 y selladas antes de
  correrlas.
- **Su evaluación.** Entró como celda C5 en la fase 2a, porque las preguntas
  llegaron selladas antes de E5 (enmienda, §2.3; plan, fila B6.0 fase 2a).
  No queda evaluación pendiente en 2b.
- **La lectura de las 30 aristas de la observación (12).**

## 2. Preguntas nuevas

| Paso | Commit | Resultado |
|---|---|---|
| Generación por instancia aislada, aprobación de la autora tras revisión contra los PDF | `fd03a0f` | 20 preguntas, 4 por documento, 60 criterios |
| Clasificación de la autora a ciegas, regla v2 (`41abf18`) | `2231c13` | 13 dato directo / 5 varios puntos / 2 abstención / 0 dudoso |
| Control del modelo, `claude-sonnet-4-6` | `c23897f` | 18 / 0 / 1 / 1; USD 0,149475 |
| Comparación | `ba54c59` | modelo contra autora 14 de 20; modelo contra previsto 14 de 20; autora contra previsto 20 de 20 |
| Adjudicación y tipo final; enmienda 2 a la regla | `23e9d20` | tipo final 13 / 5 / 2, con 6 adjudicadas |

Cuotas de la decisión del 25/09 (al menos una pregunta de varios puntos por
documento y dos de abstención en total): cumplidas con el tipo final (plan,
fila B6.0 fase 2b). Las preguntas quedaron selladas en `fd03a0f`, antes de
que corriera su celda (E5, `7f3b207`).

## 3. Evaluación: celda C5

C5: las 20 preguntas sobre KG-Tanda0-Diez-r1 (`dd42d6d9…`), GraphIndex en
memoria, juez v1 N=3 y §7. Aparte de C1 a C4: no se cruza con ellas.

| Qué | Valor | Fuente |
|---|---|---|
| Tabla pre-adjudicación, correcto / parcial / incorrecto / a adjudicar | 8 / 6 / 2 / 4 | `reports/tanda0/tabla_celdas_E5.json` (`7f3b207`) |
| Tabla definitiva, correcto / parcial / incorrecto | 8 / 8 / 4 | `reports/tanda0/tabla_celdas_definitiva_E5c.json` (`ecd102c`) |
| Wilson al 95 %, correcto / incorrecto | 0,219–0,613 / 0,081–0,416 | ídem |
| Acuerdo entre el juez y la instancia adjudicadora en la muestra de control | 1 de 2 fichas; 5 de 6 criterios; 1 sub-acreditación | ídem, clave `acuerdo_juez_instancia_adjudicadora` |
| Criterios sin cita (T0F-008, criterios 1 y 3; T0F-013, criterio 1), decisión (a) | 9 veredictos, los 9 «cumplido» | `tabla_celdas_E5.json`, `veredictos_criterios_sin_cita` |
| Atribución A0.2 de los pares parciales o incorrectos | ausencia en el grafo 0; estaba y no se navegó 4; se consultó y la respuesta falló 8 | `reports/tanda0/atribucion_tanda0.json` (`2399eb7`) |
| Exactitud de cita, respuestas de contenido, lectura extendida | N 18; fundada 18; existente 18; al ancla 15 (alguna ancla) · 14 (todas) | `reports/tanda0/ucita2_indicadores_C5.json` (`2399eb7`) |
| Patrón de vecinos salientes sobre una Operacion con restricciones entrantes | 4 llamadas en 4 trazas | `atribucion_tanda0.json`, `patrones_plan_punto_4` |
| Tope de 15 herramientas alcanzado, trazas base | 11 de 20 | trazas `data/experiment/ev2_tanda0/trazas/ev2_c5_diez_mem/` |
| Gasto | USD 2,2451 (en la cuenta de 2a) | `tabla_celdas_E5.json` |

Notas de lectura:
- Con n = 20, los intervalos son anchos; no se leen como señal.
- **Criterios sin cita.** Los tres criterios quedan fuera del dominio de
  calibración del juez, y T0F-008 y T0F-013 quedaron fuera del marco de la
  muestra de control de C5 (anexo E5.c, decisión 2).
- **Citas.** Los scripts sellados de cita y de anclas no reconocen los PDF de
  los cinco documentos nuevos. C5 se midió con extensiones declaradas, sin
  editar los sellados. La lectura estricta da 0 en los indicadores de cita
  existente y al ancla por esa causa (reporte de 2a, §5).

## 4. Observación (12)

Fila del reporte, en el formato de la enmienda `8e13be3` (§2.1 y §2.3):

| Observación | Predicción | Observado | Veredicto |
|---|---|---|---|
| (12) Aristas de extracción correctas contra el texto, ensamblado de la tanda 0 sola (`ens_cinco/r1/kg.json`, `4097d4fd…`; universo 3.345; k 30; semilla 20260927) | SIN LÍNEA DE BASE | **Lectura asistida** (instancia de modelo, revisada por la autora; desvío de la enmienda §2.1): **25 correctas de 30**; 0 no decidibles; Wilson al 95 % 0,664–0,927; 5 incorrectas: 4 `E1-prompt` y 1 `catálogo` | Sin veredicto: sin umbral ni banda (decisión 6) |

- **Muestra y lectura:** sorteo sellado en `e6a3169` (`muestra_obs12.md`,
  sha256 `247beeac…`); veredictos sellados en `f51bb1f`; fila y desvío
  declarado en `reports/tanda0/obs12_lectura/fila_obs12.md` (`c671b52`,
  `aa7ee11`).
- **Destino de las incorrectas:** `BKL-0032` a `BKL-0036`, una por arista.
  Los eventos `correccion_diagnostico` pasan su diagnóstico de
  `adjudicado_humano` a `lectura_asistida` (`aa7ee11`; spec del backlog,
  enmienda 2026-09-29).
  - Las cuatro `E1-prompt` quedan fuera de r2, porque tocan el prompt
    congelado. Se agrupan con los demás cambios de prompt y con la decisión
    sobre la matriz.
  - La de `catálogo` (`BKL-0034`) está en el §4 del laudo de r2 y cae en el
    mismo prefijo de E1.
  - Ninguna es falsedad de esquema en campo estructurado, así que ninguna se
    lee por la vía de A8.
- **Tests de la regression suite:** las 30 aristas no se sellan como tests en
  esta lectura; se revisa después de r2, con direccionamiento por
  (chunk_id, relación, tipo de destino)
  (`reports/tanda0/obs12_lectura/decision_tests.txt`, `f51bb1f`).

## 5. Costo de 2b

- **Evaluación de C5:** USD 2,2451, contada en E5 de 2a (reporte de 2a, §7).
- **Control de tipo:** USD 0,149475 (`c23897f`).
- **Generación de las preguntas y lecturas asistidas:** las hicieron
  instancias fuera de la API del repo; su costo es NO ENCONTRADO en el repo.

## 6. Qué deja 2b para después

- Los tests de la observación (12): se revisan después de r2 (sección 4).
- Las incorrectas `E1-prompt` y `catálogo`: canal de cambio de prefijo, con la
  decisión sobre la matriz (`docs/checklist_pre_escalado.md`, X1 a X7 y X11).
- Quién lee y adjudica en la tanda 1 y en B6.3 (checklist P15 y Q12), con los
  mentores.
- Modelo y versión de las instancias: a confirmar por la autora.

Con esta segunda emisión, la fase 2b queda cerrada en lo formal (enmienda
`a551c57`, §2.2), una vez que la autora la commitee.
