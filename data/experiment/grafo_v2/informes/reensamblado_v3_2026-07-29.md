# Informe — Re-ensamblado v3 del grafo v2 desde el caché de extracción (2026-07-29)

**Resultado: re-ensamblé el grafo v2 consumiendo el MISMO caché de extracción
(`cache_v2/full`, biyección 508↔508 verificada), con cero llamadas a la API y
`grafo_v2/kg.json` intacto como baseline sellado. El delta es atribuible a una sola
variable (misma extracción, distinta lógica de ensamblado): v2 3.872 nodos / 7.231
aristas → v3 4.458 / 8.044; `Operacion` 855 → 1.201. La salida vive en
`reensamblado_v3/` (fuera del alcance de descubrimiento de la app) y NO está
promovida: queda pendiente de medición (escalón 1b).**

Nota de registro: escribo este informe retroactivamente a partir de la auditoría de
custodia U0 (29-07), porque la sesión de trabajo que produjo el re-ensamblado no dejó
informe de unidad. Es una excepción a la regla de un informe por unidad, documentada
como tal. Todos los números de este informe son los verificados por esa auditoría; los
números de la sesión original que la auditoría no reprodujo no entran acá (quedan
anotados en el backlog con su etiqueta de reproducibilidad).

## 1. Origen

Una pregunta hecha vía la app local (sesión `6e633685-56d1-41fb-8c6f-c38493169666`)
sobre el tope mensual de compra de moneda extranjera de personas humanas residentes
(punto 3.9 del TO de Exterior y Cambios) terminó en abstención: el dato no estaba en
el grafo v2. El diagnóstico recorrió el pipeline completo (PDF → chunks → caché de
extracción → `kg.json`) y localizó la pérdida en el ENSAMBLADO, no en la extracción:
el dato estaba en el caché ya pagado y el ensamblado v2 lo descartaba.

## 2. Los defectos

El registro canónico es `docs/backlog_reextraccion.md` (entradas RX-01 a RX-09, cada
una con su etiqueta de reproducibilidad); no duplico las entradas acá. Para este
re-ensamblado importan dos grupos:

- **Corregibles sin re-extraer** (defectos del ensamblado): la colisión de `chunk_id`
  con desempate ciego (RX-01), el colapso de `Operacion` por dedup sobre un campo
  categórico, la colisión de prefijo a 80 chars, la evidencia descartada en merges y
  el reporte de cobertura sobre denominador de sobrevivientes.
- **No corregibles sin re-extraer** (quedaron congelados en el texto y la `location`
  con que los chunks fueron a la API): RX-02, RX-03, RX-04, RX-05, RX-06, RX-09.

La magnitud del primer grupo, medida sobre el v2 vigente: de 508 resultados de
extracción, el desempate por `chunk_id` descartaba **102** (35 de índice, 14 de tabla,
53 de articulado — estos últimos con 95.226 chars y 429 entidades pagadas que no
aportaban un solo nodo). La cobertura real del ensamblado v2 era **79,9% (406/508)**,
mientras el reporte declaraba `coverage_by_doc: 100%` porque computaba el porcentaje
sobre el denominador de los 406 sobrevivientes.

## 3. Lo ejecutado

Re-ensamblado v3 (`code/assemble_v3.py` + `code/chunk_roles.py`), desde el caché
existente:

- **Cero llamadas a la API.** El driver es `cache_v2/chunks_all.json` y cada chunk se
  resuelve a su archivo de caché por hash: biyección 508↔508, sin faltantes ni
  archivos huérfanos, 0 resultados con error.
- **Rol documental como discriminador.** Los 508 chunks se clasifican por evidencia
  del propio PDF (pie de índice, encabezado de la tabla de norma de origen):
  508 = 48 de índice + 460 activos (368 cuerpo + 92 tabla). El índice queda excluido
  del ensamblado; cuerpo y tabla entran por separado, sin desempate.
- **Una sola variable.** Misma extracción, distinta lógica de ensamblado: todo el
  delta v2→v3 es atribuible al ensamblado.
- **Salida aislada.** `reensamblado_v3/` (kg.json, cuarentena.json,
  assemble_v3_report.json). La app no lo descubre (su glob de grafos es de un nivel
  bajo `data/experiment/`), y `grafo_v2/kg.json` queda intacto como baseline sellado
  para el side-by-side.

## 4. Números (verificados por la auditoría U0)

| Métrica | v2 | v3 |
|---|---|---|
| Nodos | 3.872 | 4.458 |
| Aristas | 7.231 | 8.044 |
| `Operacion` | 855 | 1.201 |

- El punto 3.9 de Exterior y Cambios está presente en v3 con ambos umbrales: la
  restricción de **USD 200** mensuales por conjunto de conceptos y la de **USD 100**
  para operaciones en efectivo (dos nodos `Restriccion` con provenance en el
  punto 3.9).
- **440 de los 460 chunks activos aportan ≥1 nodo nuevo, y los 460 dejan ≥1 rastro**
  (nodo nuevo, arista nueva o provenance agregada a un nodo existente); 0 chunks
  mudos.
- Los **25 nodos-cáscara** heredados del índice en v2 están ausentes de v3 por id
  (0 de 25); 3 reaparecen por (type, label) porque la misma entidad también fue
  extraída desde chunks activos y en v3 entra por esa vía — esperado, no residuo del
  defecto.

## 5. Estado

- **v3 NO está promovido.** Queda pendiente de medición (escalón 1b) antes de
  cualquier decisión de promoción, que es explícita y registrada, no una edición
  silenciosa.
- El residuo RX-02 / RX-05 / RX-06 (locations desplazadas por coalescing, chunks que
  mezclan roles, contexto cortado por el hard cap) no lo arregla ningún re-ensamblado:
  queda para la decisión de re-extracción única del backlog.

## Alcance

Solo lectura del caché y de los PDFs del subset; escrituras únicamente en
`reensamblado_v3/`. Sin API, sin commits. Números de parseo real, verificados por la
auditoría de custodia U0 (29-07).

**FRENO acá.**
