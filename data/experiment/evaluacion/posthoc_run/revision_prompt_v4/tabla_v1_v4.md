# Calibración del verificador — comparación v1→v4 por caso

Corrida v4: commit `e35fe21`, trazas OFF de run_3, namespace `cv=verificador-v4`, salidas en
`posthoc_run/calibracion_verificador_v4/`. Se listan las atribuciones PRIMARIAS de cada versión.

**Lectura pre-registrada** (definida antes de ver los outputs):
- **Acierto**: las primarias del verificador coinciden con las primarias del ground-truth.
- **Abstención válida**: `frontera_no_determinada` cuyo campo `entre` incluye la categoría del GT, con `busquedas` poblado.
- **Abstención inválida / Error**: abstención cuyo `entre` no incluye el GT, o etiqueta firme distinta del GT.
- El resultado se reporta en tres columnas (aciertos / abstenciones válidas / errores), no como score único.
  0 errores es la meta principal; los aciertos se maximizan; las abstenciones van a la cola humana por diseño.

| Caso | GT (primarias requeridas) | v1 | v2 | v3 | v4 |
|---|---|---|---|---|---|
| CQ-017 | estructural_kg **y** provenance_imprecisa | ✓ provenance+estructural | ✗ sin_defecto | ✗ generación-de-más ×2 + provenance (falta estructural) | ✗ generación-de-más ×2 + provenance (falta estructural) |
| CQ-020 | completitud_kg | ✗ provenance+navegación | ✗ provenance+navegación | ✗ generación-de-más + navegación | ✗ generación-de-más ×2 |
| CQ-025 | contenido_kg | ✗ navegación | ✗ navegación | ✗ navegación | ✗ navegación |
| CQ-031 \* | completitud_kg | ✓ completitud | ✓ completitud | ✗ navegación | ✗ navegación ×2 |
| CQ-034 | completitud_kg | ✗ sin_defecto | ✗ sin_defecto | ✓ completitud | ⚠ falla operativa \*\* |
| **Totales (aciertos / abstenciones válidas / errores)** | | **2 / – / 3** | **1 / – / 4** | **1 / – / 4** | **0 / 0 / 4** (+1 falla operativa) |

(v1–v3 no tenían abstención disponible; su columna de abstenciones va con "–".
En v4, `frontera_no_determinada` estaba disponible y no se usó en ningún caso.)

---

\* **CQ-031 — GT en re-adjudicación.** El nodo que respondería la pata 1 existe en run_3
(`Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti`,
contenido fiel al Punto 4.5 del PDF), pero es **léxicamente inalcanzable** para el agente:
`buscar_nodos` indexa **label e id, no `description`**; las 10 búsquedas reales del agente en su
traza y 3 consultas razonables mínimas no lo devuelven (0 hits). Las consultas que sí lo
encuentran son las que reutilizan las palabras del propio id/description del nodo. La etiqueta
GT (completitud_kg) vs la del v4 (navegación) queda pendiente de re-adjudicación humana con este
dato.

\*\* **CQ-034 (v4) — falla de formato con sustancia correcta.** El JSON final es inválido
(error de sintaxis + campos fuera de contrato), por lo que bajo la lectura pre-registrada no
clasifica. Pero el `final_raw` diagnostica en sustancia **completitud_kg, primaria, en ambas
patas fallidas** (omisión del punto 3.9 del TO de Exterior y cambios en el grafo), es decir la
categoría que el GT esperaba. Detalle en `caso_CQ-034.md`.
