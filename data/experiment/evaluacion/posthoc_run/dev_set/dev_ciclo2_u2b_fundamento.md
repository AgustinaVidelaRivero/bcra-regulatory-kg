# Dev ciclo 2 — Unidad 2b: requisito de fundamento (§4bis) — reporte

Fecha: 2026-07-19. Spec: enmienda §4bis de `docs/diseno_ciclo2.md` (commit `56bc5aa`,
releída — manda). Editado SOLO `s1_fuentes_v04.py` (dev del ciclo); congelados intactos
(los de siempre + `capa_deterministica_v62.py`). Versión: `s1-v0.4b-dev`.

## 1. Implementación

- `_pasaje_funda(nodo, entrada)`: el contenido del nodo debe localizar DENTRO del pasaje
  por numeral **o de su página** con la maquinaria existente (ancla+extensión, span ≥
  `UMBRAL_CONTENIDO`=60). A nivel FETCH: si no funda → estado `fuente_no_funda` con la
  anotación del span máximo; en el loop de juicio → triage con ese motivo, **sin llamada
  LLM**. Exentos: `portador_por_contenido` y los completos CON pasaje extra por contenido
  (fundan por construcción).
- Tests sintéticos nuevos (`test_s1v04_fundamento.py`): pasaje que funda / que no funda /
  `fuente_no_funda` → triage con CERO llamadas (cliente que falla si se lo llama).
  **3/3 PASSED; suite completo de la casa 97/97.**

## 2. HALLAZGO PREVIO A LA CORRIDA (registrado): la premisa del criterio (e) estaba mal atribuida

Antes de correr, verifiqué con la maquinaria calibrada el supuesto de la enmienda ("la
corrección de rep3_atrib2 no ocurre: su pasaje no funda"): **es FALSO**. El contenido del
nodo `Obligacion_informar_riesgo_tasa_interes_eve` **SÍ funda** en el pasaje del 1.1
(**span 245, match completo**: su description ES el texto del listado trimestral del 1.1 —
la provenance de ESE nodo no está desplazada; la atribución de mecanismo de mi reporte u2
§6d queda corregida por esta medición). Las que NO fundan son las otras **4** atribuciones
de CQN-011 (portador `Obligacion_informacion_base_individual_y_consolidada…`, spans
vacíos contra su pasaje). Implementé la regla EXACTAMENTE como está escrita y corrí igual:
el resultado empírico decide.

## 3. Corrida → productos `_s1v04b_n3` (10/10, N=3)

**Costo real: 133.269 in / 15.172 out** (u2 costó 216.435 — el fundamento ahorra ~38%:
menos llamadas). Cero errores de formato.

## 4. Tabla a tres columnas (v6.2-D / v7'-u2 / v7'-u2b; solo cambios)

| Caso | v6.2-D | v7' (u2) | v7' (u2b) |
|---|---|---|---|
| CQN-001 | DIVIDIDO [1,1,1] | ídem | ídem |
| CQN-006 | [] 3-0 | ídem (decidido) | ídem (decidible; ver §6 nota de varianza) |
| CQN-007 | navegación 3-0 (D7) | ídem | ídem — **el flip de D7 sobrevive** |
| CQN-008 | navegación 3-0 | ídem | ídem |
| CQN-009 | completitud 3-0 | ídem | ídem (**no_funda ×2**: dos confirmaciones pasan a triage — el precio) |
| CQN-010 | [] 3-0 | ídem | ídem |
| CQN-011 | DIVIDIDO [1,1,1] | **mayoría 2-1 (regresión u2)** | **DIVIDIDO [1,1,1] ◀ RESTAURADO** (no_funda ×4 + la juzgada no_determinable) |
| CQN-012 | completitud 3-0 | completitud 2-1 (cross ×3) | **completitud 3-0 ◀ vuelve al conteo de v6.2-D** (cross ×3 + no_funda ×1: la corrección de u2 ya no ocurre; usage 0) |
| CQN-013 | aplicacion_erronea 2-1 | ídem (cross ×3) | ídem (cross ×3, cero llamadas) |
| CQN-014 | navegación 2-1 | ídem | ídem (juzgada por contenido, confirma) |

## 5. Criterios — veredicto

- **(e) CQN-011 vuelve a DIVIDIDO/triage: CUMPLIDO — con el mecanismo REAL documentado.**
  La regla bloqueó las 4 atribuciones que no fundan (`fuente_no_funda` ×4, cero llamadas
  en ellas); **rep3_atrib2 — cuyo pasaje SÍ funda (span 245) — fue juzgada igual y salió
  `no_determinable` (0 mayoría en 3 muestras)**: la corrección no ocurrió por VARIANZA
  del juicio en la frontera, no por la guarda. El voto quedó DIVIDIDO con triage
  (`fuente_no_funda` + `fuente_no_verificable`). **Honestidad pre-registrada: si CQN2
  presenta el mismo patrón (pasaje que funda + juicio inestable), el resultado puede
  oscilar — la regla NO cubre ese residuo; lo cubre la política de N y el triage.**
- **(b) CQN-013: CUMPLIDO** — cross_doc ×3, cero llamadas, sin flip.
- **(c) CQN-006 sigue decidible: CUMPLIDO** (3 juzgadas con mayoría; voto y categoría
  intactos — nota de varianza en §6). **CQN-014 confirmado: CUMPLIDO** (juzgada por
  contenido, estructural 3/3, voto intacto).
- **(d') cero cambios adicionales contra la tabla de u2 salvo los exigidos: CUMPLIDO** —
  los únicos casos que difieren de u2 son CQN-011 (lo que (e) exige) y CQN-012 (efecto
  directo de la regla: su única corrección de u2 cayó en `fuente_no_funda` y el conteo
  VUELVE al de v6.2-D — restauración, no regresión).

## 6. El precio en triages del endurecimiento (`fuente_no_funda` por caso)

| Caso | fuente_no_funda | Nota |
|---|---|---|
| CQN-009 | 2 | dos confirmaciones correctas de u2 pasan a triage (patrón E4: veredicto correcto pagando revisión) |
| CQN-011 | 4 | el objetivo de la regla |
| CQN-012 | 1 | anula la corrección de u2 |
| resto (7 casos) | 0 | — |
| **TOTAL** | **7** | |

**Nota de varianza (CQN-006, registrada):** en u2 las 3 exoneraciones confirmaron
sin_defecto; en u2b dos reps votaron mayoría `completitud_kg` y la regla de jerarquía las
acotó a SECUNDARIA (el síntoma de CQN-006 no tiene patas y su único claim es secundario) —
por eso el voto y la categoría no se mueven. Es la frontera semántica oscilando entre
muestras frescas; el voto la contiene.

## 7. Iteraciones

**Cero iteraciones de código** (la regla §4bis se implementó tal como está escrita y pasó
tests y corrida a la primera). **Un hallazgo registrado** (§2): la premisa fáctica del
criterio (e) estaba mal atribuida en mi reporte u2 §6d — la medición del fundamento la
corrige; queda para la lectura del ciclo.

## 8. Sello

- Fecha: 2026-07-19 · HEAD: `56bc5aa7ad132ca2013af3abb95d41ed78a3b0ff` · enmienda §4bis @ `56bc5aa`.
- Congelados: diff vacío (capa_deterministica.py, capa_deterministica_v62.py,
  s1_fuentes.py, verificador.py, judge.py, harness.py).
- Escrituras: `s1_fuentes_v04.py` (editado, dev), `test_s1v04_fundamento.py`, 10
  `_s1v04b_n3.json`, este reporte. Costo API: 133.269/15.172.
