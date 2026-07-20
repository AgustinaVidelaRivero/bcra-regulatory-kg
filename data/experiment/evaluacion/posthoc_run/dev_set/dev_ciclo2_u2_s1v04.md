# Dev ciclo 2 — Unidad 2: S1 v0.4 — reporte

Fecha: 2026-07-18. Spec: `docs/diseno_ciclo2.md` §3-§4 (commit `b84668e`, releída).
Material de dev: gate CQN quemado (productos `_capa_d62` de la unidad 1). Congelados
intactos: s1_fuentes.py (v0.3.1 baseline), capa_deterministica.py,
capa_deterministica_v62.py (`7cef0ba`), verificador, juez, harness — diff vacío en todos.

## 1. Implementación — `s1_fuentes_v04.py` (módulo nuevo al lado)

**Qué importa (congelado) y qué replica (declarado en el docstring):** importa el fetch
v0.3.1 entero (`construir_paquete_fuentes`), los prompts, `_llamada_s1` (con las guardas
de dominio de vocabulario de B4.5), el voto por atribución y las utilidades de la casa;
REPLICA el loop de juicio de `aplicar_s1` — los estados nuevos y las dos guardas no caben
en el congelado sin editarlo — conservando política conservadora, regla de jerarquía v0.3
e instrumentación de usage.

- **Guarda de dominio (§3):** territorio = `tos_fuente` del eval set SELLADO
  (`data/experiment/evaluacion/queries/eval_set_cqn.json`, ruta desde la raíz;
  `--eval-set` parametrizable). `source_doc` del portador ∉ territorio → estado
  `fuente_cross_doc`, triage con la anotación par documento/territorio, **cero llamadas
  LLM** (guarda a nivel fetch).
- **Portador robusto (§4):** fallback por contenido para
  sin_portador_extraible/provenance_no_parseable/localizacion_fallida (candidatos = los
  ids citados que el extractor no pudo desambiguar) + pasaje EXTRA
  `portador_por_contenido` en completos cuando localiza único y distinto. Tres guardas:
  umbral de longitud, unicidad, y "nunca exonera por sí solo" (voto sin_defecto con
  portador solo-por-contenido → triage `exoneracion_solo_por_contenido`). Búsqueda
  restringida al territorio (la guarda §3 aplica también acá).

## 2. Iteraciones registradas (dev — iteración libre sobre material quemado)

1. **Literal completo → ventanas de palabras con ancla + extensión.** El literal entero
   del contenido (p. ej. los 435 chars del nodo de CQN-006) NO matchea el corpus: nodo y
   PDF divergen en conectores a mitad de cláusula ("al usuario **por conceptos como**" vs
   "al usuario **de servicios financieros por los siguientes conceptos: i)**"). Mecanismo
   refinado: ancla de VENTANA_PALABRAS=8 palabras + extensión greedy; unicidad sobre el
   ANCLA, umbral sobre el SPAN.
2. **Fix del solapamiento de ventanas.** La extensión buscaba la ventana siguiente al
   FINAL del ancla, pero las ventanas solapan con paso 1 palabra (la siguiente arranca
   ~una palabra después del INICIO) → la extensión moría al primer paso y el span quedaba
   bajo el umbral. Corregido: expectativa = posición previa + primera palabra + 1
   (± SLACK_EXTENSION=40).
3. **Unicidad por UBICACIÓN, no por número de candidatos.** Con ventanas, los DOS
   candidatos de CQN-014 (los nodos n=0 de CAP 7.2 y del RI) pasaron a localizar — en la
   MISMA cláusula del 7.2 → `contenido_no_unico` espurio. Regla refinada: candidatos
   múltiples que localizan en el mismo doc a |Δidx| ≤ ventana/2 corroboran UN portador
   textual; se elige el de span más largo (desempate por id).

## 3. Umbral del portador por contenido — calibración documentada (punto 4 del pedido)

**Valores elegidos:** `UMBRAL_CONTENIDO = 60` chars normalizados (sobre el SPAN),
`VENTANA_PALABRAS = 8`, `SLACK_EXTENSION = 40`, `MAX_UBICACIONES = 3`,
`K_LITERALES = 3`, ventana de pasaje 1.400 chars.

**Con qué se calibró:** CQN-014 (match EXACTO de 110 chars — camino 1, holgado) y
CQN-006 (camino de ventanas: **span = 61**, apenas sobre el umbral — la divergencia de
conectores corta la coincidencia justo después de "…de cualquier forma al usuario").
**El borde es real y queda documentado:** si la divergencia nodo↔corpus llegara UNA
palabra antes, el span caería bajo 60 y el fallback no fundaría (→ estado original /
triage — nunca falso portador). El umbral favorece precisión sobre rescate; **es el
número que CQN2 va a testear de verdad.**

## 4. Corrida (N=3, política conservadora) → productos `_s1v04_n3`

10/10 exit 0. **Costo real S1 v0.4: 216.435 in / 24.052 out** (medido, usage real).
Cero errores de formato.

## 5. Tabla a tres columnas (solo cambios marcados)

| Caso | v6.1-D (congelada) | v6.2-D | v7' (v6.2-D + S1 v0.4) |
|---|---|---|---|
| CQN-001 | DIVIDIDO [1,1,1] | ídem | ídem (S1 corrigió causas por rep; el voto sigue dividido) |
| CQN-006 | [] 3-0 · R1 | ídem | **ídem, ahora DECIDIDO** (exoneración sostenida con la cláusula 2.3.5.1 en mano — antes no_determinable ×3) |
| CQN-007 | alcanzabilidad_kg 3-0 | **navegación 3-0 (D7)** | navegación 3-0 (S1 sin gatillo — el flip SOBREVIVE) |
| CQN-008 (ilustrativa) | navegación 3-0 | ídem | ídem (2 secundarias corregidas, voto intacto) |
| CQN-009 | completitud_kg 3-0 | ídem | ídem (confirmado 3/3; rep1 rescatada por contenido y confirma) |
| CQN-010 | [] 3-0 · R1 | ídem | ídem (sin gatillo) |
| CQN-011 | DIVIDIDO [1,1,1] | ídem | **MAYORÍA 2-1** {[context_recall, completitud], [noise, contenido]} **◀ CAMBIO DE CATEGORÍA** |
| CQN-012 | completitud_kg 3-0 | ídem | completitud_kg **2-1** (misma clave; 3 atribuciones cross-doc BLOQUEADAS — el portador RI 7.1 fuera del territorio CAP) |
| CQN-013 | aplicacion_erronea 2-1 | ídem | **ídem — cross_doc ×3, CERO llamadas, el flip NO ocurre** |
| CQN-014 | navegación 2-1 · R3 | ídem | ídem (rep estructural juzgada por contenido: confirma estructural_kg 3/3) |

## 6. Criterios pre-registrados del diseño §5 — veredicto

- **(b) CQN-013 no degrada: CUMPLIDO.** `fuente_cross_doc` en las 3 atribuciones, **cero
  llamadas LLM en ellas** (usage 0/0), voto de v6.2-D intacto. El flip a
  {faithfulness, contenido_kg} no ocurre.
- **(c) CQN-014: CUMPLIDO.** De `sin_portador_extraible` a `completo_por_contenido`:
  el fallback resolvió los DOS candidatos citados al portador del territorio (la
  cláusula n=0 del **7.2 de Capitales, pág 151, match exacto, 1 ocurrencia** — nota fiel:
  el retro del diseño imaginaba el 12.3; el fallo real citaba los nodos n=0 y el
  contenido localizó su cláusula fuente) y el juicio DECIDIÓ: confirma estructural_kg
  3/3 con `coinciden=si`. **CQN-006: CUMPLIDO.** De no_determinable ×3 a DECIDIBLE: con
  el pasaje extra del 2.3.5.1 (pág 15) las 3 exoneraciones votan mayoría
  `sin_defecto` — **la exoneración se sostiene ahora con la cláusula en mano** (reps:
  2/3, 2/3 y 3/3 sin_defecto).
- **(d) Cero regresiones: NO CUMPLIDO EN 1 DE 10 — CQN-011.** 006/009 (aciertos) ✓,
  001 (triage) ✓, 007 (el flip de v6.2-D sobrevive) ✓, 008/010/012/013/014 ✓ (012
  conserva clave y categoría con conteo 3-0→2-1). **CQN-011: dividido → mayoría 2-1**:
  la corrección de S1 en rep3_a2 (aplicacion_erronea → contenido_kg, 2/3) igualó la
  clave de rep3 con la de rep2 y el voto dejó de estar dividido. Cambio de categoría NO
  esperado por (b)/(c) — queda como hallazgo de dev para la lectura del ciclo (¿la
  convergencia post-S1 es señal o ruido? no lo decide esta unidad).

## 7. Estados de fetch por caso

| Caso | por numeral (completo) | por contenido | extra contenido | cross-doc bloqueadas | fallidos restantes |
|---|---|---|---|---|---|
| CQN-001 | 1 | 2 | 0 | 0 | 0 |
| CQN-006 | 3 | 0 | 3 | 0 | 0 |
| CQN-007 | 0 (sin gatillo) | 0 | 0 | 0 | 0 |
| CQN-008 | 2 | 0 | 0 | 0 | 0 |
| CQN-009 | 2 | 1 | 0 | 0 | 0 |
| CQN-010 | 0 (sin gatillo) | 0 | 0 | 0 | 0 |
| CQN-011 | 5 | 0 | 0 | 0 | 0 |
| CQN-012 | 1 | 0 | 0 | **3** | 0 |
| CQN-013 | 0 | 0 | 0 | **3** | 0 |
| CQN-014 | 0 | 1 | 0 | 0 | 0 |

**Cero `fuente_no_verificable` remanentes en toda la corrida** (v0.3.1 tenía 11 en su
primera pasada por el dev y 2+1 en el gate): el fallback por contenido rescató todos los
fallos rescatables y la guarda cross-doc convirtió el resto en derivación informada.

## 8. Sello

- Fecha: 2026-07-18 · HEAD: `7cef0ba572087154b71336fcf202028f3cdaabdb`
- Spec: `docs/diseno_ciclo2.md` @ `b84668e` · unidad 1 @ `7cef0ba`.
- Congelados: diff vacío (s1_fuentes.py, capa_deterministica.py,
  capa_deterministica_v62.py, verificador.py, judge.py, harness.py).
- Escrituras: `s1_fuentes_v04.py`, 10 `_s1v04_n3.json`, este reporte. Costo API:
  216.435/24.052.
