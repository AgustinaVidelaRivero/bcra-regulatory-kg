# Report — Run 5 — Híbrido core + emergente

> **Estado del documento.** Esqueleto pre-full-run. El log de iteración del schema queda **congelado acá** (sección A) antes de re-correr el smoke v2. Las métricas finales del KG (sección B en adelante) se completan después del full run + ensamblaje.

---

## A. Log de iteración del schema (v1 → v2)

> Esta sección queda escrita ANTES del smoke v2 para que el resultado del smoke v2 pueda refutar o confirmar la motivación declarada acá. No se reescribe a posteriori.

### A.1 Cuándo ocurrió la iteración

Después del **smoke test v1** sobre `TO_proteccion_usuarios_servicios_financieros_actual.pdf` (48 chunks, USD 0.5426, 0 errores de API), antes del full run. La autora del experimento revisó el reporte de 4 análisis del smoke v1 (candidatos `Concepto → EntidadFinanciera`, dedup post-smoke, estructura del grafo, calidad de labels) y autorizó una iteración acotada del schema.

### A.2 Cambio principal — Refinamiento de Regla 3.3

**Motivación.** El smoke v1 mostró un desbalance llamativo en la distribución de tipos core: `EntidadFinanciera = 1 / 505 entidades (0.2%)` contra `Concepto = 128 (25.3%)`. La inspección de los 35 Conceptos candidatos a `EntidadFinanciera` reveló que **el problema no era un modelo siendo demasiado estricto**, sino una **inconsistencia interna del schema v1**:

- El schema v1 §3.5 declaraba 10 `categoria` reconocidas en el vocabulario controlado de `EntidadFinanciera`: `banco_comercial`, `banco_inversion`, `compania_financiera`, `caja_credito`, `casa_cambio`, `agencia_cambio`, `fideicomiso_financiero`, `sgr`, `proveedor_no_financiero_credito`, `otra`.
- El schema v1 §3.3 decía simultáneamente que "categoría genérica como clase regulatoria → `Concepto`".
- Resultado: las categorías reconocidas (`casa_cambio`, `fideicomiso_financiero`, `proveedor_no_financiero_credito`, etc.), cuando aparecían en el corpus como tipificación general (que es como aparecen casi siempre en TOs normativos), **caían sistemáticamente en `Concepto`**. El vocabulario controlado de §3.5 quedaba sin sujetos reales que clasificar.

Esa contradicción interna no es decisión defendible, es un bug del schema. La iteración la resuelve.

**Cambio aplicado (v2).** Criterio de cruce: la categoría reconocida ya no basta para clasificar; tampoco es la sola "genericidad" la que descarta. La regla v2 cruza dos condiciones:

1. La mención encaja en alguna de las 10 `categoria` del vocabulario controlado de §3.5.
2. El texto le atribuye **rol de sujeto activo** de una obligación, autorización o restricción concreta ("los operadores de cambio deben…", "las cajas de crédito pueden…").

Solo si las dos se cumplen → `EntidadFinanciera`. En cambio:

- Supratipos agregados sin categoría única ("Sujeto obligado", "Entidad financiera" como término-glosario que agrupa varias categorías heterogéneas) → `Concepto`.
- Contrapartes de la operación regulada (Usuario, Deudor, Cliente, Beneficiario, Cedente, Tomador) → `Concepto`.
- Conceptos jurídicos/técnicos abstractos (el sistema financiero, la solvencia, la liquidez, la posición global neta) → `Concepto`.

Esta no es una inversión completa de v1: es una corrección quirúrgica que mantiene `Concepto` para los tres patrones que v1 sí capturaba bien (supratipo, contraparte, abstracción) y solo recupera `EntidadFinanciera` para los casos donde la categoría reconocida cumple rol de sujeto.

### A.3 Refuerzos operativos a Reglas 5 y 6

**Refuerzo Regla 5 (label).** El smoke v1 mostró 13 labels >8 palabras (2.6%), concentrados en `Restriccion`: el modelo metía el cuerpo normativo dentro del label en lugar de en `properties.description`. Ejemplo: `"Atención en condiciones de igualdad a usuarios con discapacidad auditiva"` (10w). v2 agrega al SYSTEM_PROMPT un **par de ejemplos MAL/BIEN** que muestra el mismo concepto bien resuelto (`label: "Atención a usuarios con discapacidad auditiva"` + cuerpo en description). La regla declarada no cambia; el refuerzo es pedagógico.

**Refuerzo Regla 6 (jerarquía documental).** El smoke v1 mostró referencias documentales filtradas al label como paréntesis ("Sujetos obligados (punto 1.1.2)", "Régimen informativo (Anexo I)"). El reporte de dedup las detectó como duplicados sospechosos contra el label limpio ("Sujetos obligados"). v2 agrega al SYSTEM_PROMPT una **prohibición explícita de paréntesis documentales en label** con ejemplos MAL/BIEN. La regla declarada (no modelar jerarquía documental) no cambia; el refuerzo cierra un loophole que el modelo había encontrado.

### A.4 Lo que NO se cambia

Decisiones explícitas de la autora del experimento, registradas acá para que el smoke v2 las respete:

- **Restricciones huérfanas (12/176 en v1):** no se fuerza al modelo a generar `aplica_a` o `recae_sobre` cuando el chunk no contiene esa información. Las restricciones sin enlace dentro del chunk quedan como nodos sueltos que el ensamblaje conecta a posteriori solo por dedup, no por inferencia. Documentado en sección C como característica esperada del corpus.
- **Duplicados léxicos no resueltos por el dedup determinístico (15 parejas sospechosas en v1):** las parejas refinamiento-vs-duplicado (ej. `"Entidad financiera"` vs `"Entidad financiera emisora de tarjetas"`) **no se resuelven con LLM**, son limitación declarada de §3.6 (resolución 100% determinística sin Sonnet).
- **Forma morfológica de predicados emergentes (99.3% cumplimiento en v1):** ruido aceptable, no se toca el prompt.

### A.5 Resultado esperado del smoke v2

Si la motivación de la iteración es correcta:

- `EntidadFinanciera` debería **subir significativamente** (probablemente al rango 5–15% del total de entidades del TO de Protección al Usuario), capturando "operador de cambio", "fiduciario de fideicomiso financiero", "proveedor no financiero de crédito", "empresa no financiera emisora de tarjeta", etc., con `categoria` poblada del vocabulario controlado.
- `Concepto` debería **bajar correspondientemente**, conservando solo supratipos, contrapartes y abstracciones.
- Labels > 8 palabras debería caer **por debajo del 1%**.
- Paréntesis documentales en label deberían **desaparecer** (caer a 0).
- `categoria` faltante en `EntidadFinanciera` debería caer a 0 (refuerzo de obligatoriedad).
- El ratio total core/emergente y la distribución de predicados deberían quedar **estables** (el cambio v1→v2 es interno a la división core ↔ Concepto, no a la división core ↔ resto).

Si el smoke v2 no confirma estas predicciones, queda documentado como **hallazgo del experimento**: el schema híbrido con vocabulario controlado tiene un techo inherente sobre el tipo `EntidadFinanciera` en corpus regulatorio normativo (donde los sujetos aparecen tipificados, no nominados).

### A.6 Resultado observado del smoke v2 (post-corrida)

| Predicción | Resultado | ¿Cumplida? |
|---|---|:---:|
| `EntidadFinanciera` sube al rango 5–15% | de **0.2% a 5.4%** (+29 nodos absolutos) | ✅ piso del rango |
| `Concepto` baja correspondientemente | subió 24 nodos en absoluto pero quedó proporcional (+1.8pp) | ⚠️ parcial — el total creció, los movimientos individuales sí ocurrieron |
| Labels > 8 palabras < 1% | quedó en **2.5%** (vs 2.6% en v1) | ❌ refuerzo pedagógico no movió la aguja |
| Paréntesis documentales en label = 0 | de **1 a 0** | ✅ |
| `categoria` faltante = 0 | de **1 a 0** | ✅ |
| Ratio core/emergente estable | sí — el movimiento fue interno a Concepto ↔ EntidadFinanciera | ✅ |

**Movimientos Concepto → EntidadFinanciera (9 promotions confirmadas):** "Operadores de cambio" (→`casa_cambio`/`agencia_cambio`), "Fiduciario de fideicomiso acreedor" (→`fideicomiso_financiero`), "Proveedor no financiero de crédito" (→`proveedor_no_financiero_credito`), "Entidades financieras" (→`otra`), "Cajas de crédito cooperativas" (→`caja_credito`), "Casas, agencias y oficinas de cambio" (→`casa_cambio`), "Empresas no financieras emisoras de tarjetas" (→`empresa_no_financiera_emisora_tarjeta` ⚠️ no canónica). 0 demotions inversas.

**6 EntidadFinanciera nuevas que solo aparecen en v2** — refinamientos que la regla v2 hizo visibles: PSPCP, PSI, "Proveedor de servicios de inversión", "Empresa emisora de tarjeta de crédito".

**Problema nuevo descubierto:** una categoría no canónica (`empresa_no_financiera_emisora_tarjeta`, 3 instancias) que el modelo inventó fuera del vocabulario controlado de §3.5. Se resuelve en post-procesamiento (sección B abajo), NO como cuarta iteración del schema.

**Conclusión:** las predicciones críticas se cumplieron. Las 2 que no cumplieron son limitación del modelo Haiku (labels-frase) y problema de adherencia al vocabulario, ambos resolubles fuera del schema. **Schema v2 queda CONGELADO** después de este smoke. No hay iteración v3.

---

## B. Post-procesamiento determinístico (NO iteración del schema)

> Esta sección documenta operaciones que se aplican **después** de la extracción del modelo, sobre el output ya emitido. **No son iteración del schema** y no requieren re-correr el modelo. Análogamente a la dedup determinística de §3.6, son funciones de Python puras que canonicalizan el output crudo. Esta distinción metodológica es importante para la defensa del experimento: el schema queda congelado en v2 post-smoke; el ensamblaje es una capa de procesamiento aparte.

### B.1 `canonicalize_categoria`

**Decisión.** Si `EntidadFinanciera.properties.categoria` no pertenece al vocabulario controlado declarado en §3.5, se mapea a `"otra"`. **NUNCA** se mapea a un superset interpretado.

**Por qué `"otra"` y no un superset.** El vocabulario controlado de §3.5 declara 10 categorías. La regulación BCRA trata varias de esas categorías como tradicionalmente distintas (p. ej., empresas emisoras de tarjeta no son lo mismo que proveedores no financieros de crédito a efectos regulatorios). Mapear a un superset interpretado introduciría una decisión regulatoria post-hoc debatible. El vocabulario declara `"otra"` precisamente para casos no canónicos: es la opción honesta.

**Implementación.** En `code/assemble.py`:

```python
CONTROLLED_VOCAB = {
    "banco_comercial", "banco_inversion", "compania_financiera",
    "caja_credito", "casa_cambio", "agencia_cambio",
    "fideicomiso_financiero", "sgr", "proveedor_no_financiero_credito", "otra",
}

def canonicalize_categoria(cat: str | None) -> str:
    if not cat:
        return "otra"
    return cat if cat in CONTROLLED_VOCAB else "otra"
```

Se aplica solo a nodos con `type=EntidadFinanciera`. Las remapeo se cuentan en `stats.categoria_remap_sources` (Counter), reportado abajo en sección C.

### B.2 Dedup determinístico

Reglas §3.5 implementadas en `code/assemble.py`:
- Normalización del label: `lowercase` + sin acentos (NFD + strip combining marks) + colapso de espacios.
- Heurística simple de plurales: prueba quitar `'es'` y `'s'` si el restante tiene ≥ 4 caracteres.
- Clave de dedup:
  - `EntidadFinanciera`: `(type, plural_canon, categoria)` — misma normalización con categoría distinta son nodos distintos (refinamiento legítimo).
  - Otros tipos: `(type, plural_canon)`.
- Edges con `(source, target, relation)` idénticos post-mapeo colapsan a 1 edge.

### B.3 Filtro post-hoc de jerarquía documental

Refuerzo de Regla 6: nodos cuyo label matchea `^(Punto|Sección|Capítulo|Anexo|Artículo|Art\.) ` se descartan. Reportado en `stats.filtered_doc_hierarchy`.

### B.4 Filtro de self-loops y edges cross-chunk

- Edges con `source == target` post-dedup se descartan.
- Edges que referencian un `source` o `target` que vive en otro chunk (intra-chunk-only) se descartan a la entrada — esto ya estaba en la extracción.

---

## C. Limitaciones declaradas del Run 5

Documentación honesta de las limitaciones conocidas del output. No se itera sobre ellas.

### C.1 Labels-frase en Restricciones (2.5%)

El modelo Haiku tiende a comprimir el cuerpo normativo dentro del `label` en lugar de en `properties.description`, especialmente para `Restriccion`. Tras el refuerzo pedagógico de Regla 5 v2 (par MAL/BIEN explícito en el SYSTEM_PROMPT), la tasa se mantuvo en 2.5% (vs 2.6% en v1). El refuerzo no movió la aguja. Queda como **limitación del modelo de extracción**, no del schema.

Ejemplos persistentes: `"Conservación de constancia de ejercicio del derecho a documentación Braille"` (10w), `"Acceso fácil y directo a contratos desde página de inicio"` (10w).

### C.2 `EntidadFinanciera` huérfanas (5 en el smoke v2)

Algunas `EntidadFinanciera` aparecen en el grafo sin `realiza (→Operacion)` ni reciben `recae_sobre (←Restriccion)`. Esto refleja chunks donde el sujeto se menciona sin que el chunk local explicite la operación o restricción asociada. **Característica esperada** del corpus regulatorio fragmentado por chunks de 2–6K caracteres; **no se fuerzan relaciones** que el modelo no extrajo.

### C.3 Categoría no canónica mapeada a `"otra"`

El modelo emitió `empresa_no_financiera_emisora_tarjeta` (3 instancias en el smoke v2) fuera del vocabulario controlado. El ensamblaje aplica `canonicalize_categoria → "otra"` (B.1) para mantener la pureza del vocabulario declarado. **Es post-procesamiento determinístico, no iteración del schema.** El conteo de remapeos se reporta en las métricas del KG final.

### C.4 Duplicados léxicos no resueltos por la heurística

La heurística de plurales + lowercase + sin-acentos de §3.5 deja ~15 parejas léxicas no fusionadas en el smoke v2 (proporcionalmente similar a v1). Ejemplos: `"Servicio de atención al usuario"` vs `"Servicio de atención al usuario de servicios financieros"`. Esto es **limitación declarada en §3.6** (resolución 100% determinística sin Sonnet). Las parejas son mezcla de duplicados reales y refinamientos legítimos; la decisión de la estrategia es no usar LLM para distinguirlos.

---

# Report — Run 5 Híbrido core + emergente — sección final

> Las secciones A (log de iteración v1→v2) y B (post-procesamiento determinístico) y C (limitaciones declaradas) viven arriba. Lo de abajo es el análisis del KG final.

---

## Identificación del run

- **NOMBRE_RUN:** `Run 5 — Híbrido core + emergente`
- **Carpeta:** `data/experiment/run_5_hybrid/`
- **Estrategia:** núcleo cerrado de 4 tipos de entidad + 5 relaciones core↔core; resto del espacio de tipos y predicados emergente schema-light. Vocabulario controlado de 10 categorías para `EntidadFinanciera`. Resolución de entidades 100% determinística (sin LLM en post-procesamiento). Schema final: v2 (post-smoke iteración).

## Métricas del protocolo §d

| Métrica | Valor |
|---|---:|
| Tiempo de construcción (cómputo puro) | ~35 min (smoke v1: 2.5 min · smoke v2: 2.6 min · full extract: 29.5 min · ensamblaje: <1 min) |
| Costo (USD inferencia) | $7.8759 (smoke v1: $0.5426 · smoke v2: $0.5832 · full: $6.7501) |
| Tokens consumidos | full extract: in=$2.04, out=$4.71 |
| Modelo de extracción | `claude-haiku-4-5` (Haiku 4.5) |
| Nodos del KG | **6 095** |
| Edges del KG | **5 764** |
| Densidad (edges/nodos) | **0.946** |
| Tipos de entidad únicos | **20** (4 core + 16 emergentes) |
| Tipos de relación únicos | **511** (5 core + 506 emergentes) |
| Cobertura por TO | 5/5 = 100% (todos generaron tripletas) |

Distribución de nodos por TO:

| TO | Nodos | Edges |
|---|---:|---:|
| TO_capitales_minimos | 2 159 | 1 826 |
| TO_exterior_cambios | 2 319 | 2 340 |
| TO_clasificacion_deudores | 601 | 548 |
| TO_proteccion_usuarios | 426 | 504 |
| TO_regimen_informativo | 590 | 546 |

---

## D. Análisis cualitativo del KG final (las 7 lentes originales)

### D.1 Lente 1 — Consistencia core vs emergente

**Pregunta:** ¿hay nodos donde la misma entidad léxica aparece como `EntidadFinanciera` en un chunk y como `Concepto` (u otro emergente) en otro chunk distinto?

**Resultado:** **176 grupos** de nodos con label normalizado idéntico pero `type` distinto entre miembros. Sobre 179 grupos de labels repetidos en total, eso es 98% inconsistencia — alto.

**Casos prominentes (más severos):**

| Label canónico | Distribución de tipos en el KG |
|---|---|
| "Supervisión consolidada" | Concepto 1, Restriccion 1, Operacion 1, RegimenInformativo 1 |
| "Clasificación de deudores" | Operacion 1, Restriccion 1, RegimenInformativo 1, Concepto 1 |
| "Cobertura del riesgo de crédito" | Restriccion 1, Concepto 1, Operacion 1 |
| "Gestión crediticia" | Concepto 1, Restriccion 1, Operacion 1 |
| "Cajas de Crédito Cooperativas" | Restriccion 1, EntidadFinanciera 2 |
| "Sociedades de garantía recíproca" | Restriccion 1, EntidadFinanciera 2 |
| "Conformidad previa del BCRA" | Restriccion 1, Concepto 1, Excepcion 1 |
| "Fondos de garantía de carácter público" | Restriccion 1, EntidadFinanciera 1, Concepto 1 |

**Lectura.** El schema-light + chunking + extracción independiente por chunk producen ambigüedad de tipo cuando la misma entidad léxica cumple roles distintos en chunks distintos. "Clasificación de deudores" es legítimamente operación (cuando una entidad la realiza), restricción (cuando el TO impone criterios), régimen informativo (cuando es lo que se reporta) y concepto (cuando se define). El modelo lo refleja correctamente chunk-por-chunk; el costo es que la entidad léxica termina representada 4 veces en el grafo final, una por cada rol. Es un trade-off de la estrategia híbrida con dedup determinístico que no resuelve por type.

**Es señal estructural, no error del modelo.** Para fines del experimento queda documentado: la estrategia híbrida tiene multi-instanciación por rol como característica emergente.

### D.2 Lente 2 — Cierre core↔core

**Pregunta:** ¿hay edges donde `type(source)` y `type(target)` son ambos core pero el predicado NO está en el cierre {realiza, aplica_a, recae_sobre, excepciona_a, exime_a}? ¿Y direcciones invertidas?

**Resultado:**

| | |
|---|---:|
| Total edges core→core | 2 449 |
| Edges core→core con predicado NO canónico | **554 (22.6%)** |

**Top 10 predicados ofensores del cierre:**

| Predicado | Conteo | Ejemplo |
|---|---:|---|
| `requiere` | 85 | Operacion→Restriccion |
| `comprende` | 71 | Restriccion→Restriccion |
| `especifica` | 47 | Restriccion→Excepcion |
| `condiciona` | 37 | Restriccion→Restriccion |
| `integra` | 33 | Restriccion→Restriccion |
| `regula` | 22 | Restriccion→Restriccion |
| `modifica` | 13 | Restriccion→Operacion |
| `complementa` | 13 | Restriccion→Restriccion |
| `incluye` | 13 | Operacion→Restriccion |
| `define` | 9 | Restriccion→Restriccion |

**Validación de dominio/rango de los 5 canónicos:**

| Predicado | OK | Invertidos | Dom mal | Rng mal | Total | % OK |
|---|---:|---:|---:|---:|---:|---:|
| `realiza` (EF → Operacion) | 146 | 2 | 0 | 6 | 154 | 94.8% |
| `aplica_a` (Restriccion → Operacion) | 928 | **105** | 24 | 46 | 1 103 | 84.1% |
| `recae_sobre` (Restriccion → EF) | 264 | 39 | 2 | 1 | 306 | 86.3% |
| `excepciona_a` (Excepcion → Restriccion) | 246 | 2 | 20 | 23 | 291 | 84.5% |
| `exime_a` (Excepcion → {EF, Operacion}) | 37 | 0 | 4 | 0 | 41 | 90.2% |

**Lectura.** El modelo usa predicados libres dentro de core↔core en 22.6% de los casos a pesar de la Regla 4. Los predicados ofensores son emergentes legítimos (`requiere`, `comprende`, `especifica`) que el modelo recurrió en lugar de las 5 canónicas cuando la semántica no era clara. La Regla 4 no fue respetada con disciplina; **es la regla del schema con menor adherencia del experimento.**

Sobre dominio/rango: el modelo invierte `aplica_a` el 9.5% de las veces (Operacion→Restriccion en lugar de Restriccion→Operacion). Las inversiones son consistentes con el orden gramatical de la oración fuente ("La operación X aplica la restricción Y" vs. "La restricción Y aplica a la operación X"). El modelo no normaliza la dirección.

**Implicaciones para el experimento.** Las consultas downstream sobre cierre core↔core necesitarán tratar predicados invertidos como equivalentes. No se corrige en post-procesamiento porque el schema declara dirección y corregir sería reinterpretar la oración fuente.

### D.3 Lente 3 — Familias semánticas de predicados emergentes

**506 predicados emergentes únicos.** El top 100 (por frecuencia) cubre **77.1% de edges emergentes** (2 133 / 2 765).

**10/10 familias declaradas se poblaron:**

| Familia | Predicados | Edges en familia |
|---|---:|---:|
| definición / inclusión | 8 | 605 |
| obligación / requerimiento | 10 | 351 |
| regulación / normativa | 8 | 268 |
| referencia / vínculo | 6 | 119 |
| información / reporte | 6 | 82 |
| modificación / actualización | 3 | 54 |
| alcance / aplicabilidad | 3 | 39 |
| cálculo / cuantificación | 4 | 33 |
| atribución / propiedad | 2 | 15 |
| exclusión / excepción | 1 | 9 |

Top predicados por familia:
- **definición / inclusión** — `comprende` (316), `integra` (106), `define` (69), `incluye` (69).
- **obligación / requerimiento** — `requiere` (252), `condiciona` (47), `debe_cumplir` (10).
- **regulación / normativa** — `regula` (124), `autoriza` (48), `establece` (31), `determina` (29).
- **referencia / vínculo** — `referencia` (38), `refiere_a` (35).

**Predicados del top 100 NO clasificables en ninguna familia:** 49 (`especifica` 61, `utiliza` 59, `clasifica` 33, `pertenece_a` 28, `considera` 19, `cumple` 16, `constituye` 15, `complementa` 15, etc.). Son predicados emergentes "puros" sin familia obvia.

**Potencial de colapso:** si cada familia se canonicalizara a 1 predicado representativo, el top 100 caería de **51 predicados a 10** (reducción de 41 únicos). Esa reducción NO se aplica al KG actual (queda como dato para la fase 2.3 de evaluación comparativa).

### D.4 Lente 4 — Tipos emergentes: near-dups y `Concepto` como cajón de sastre

**16 tipos emergentes únicos** (inventario completo abajo). **Near-dups detectados:**

- `Concepto` (1 417) ↔ `ConceptoInformativo` (3) — sub-tipo legítimo (régimen informativo).
- `Concepto` (1 417) ↔ `ConceptoContable` (20) — sub-tipo legítimo (contabilidad regulatoria).
- **Typo:** `NormaSuprior` (4 instancias) — debería ser "Norma Superior". Se deja como salió del modelo (schema-light permite tipos libres en PascalCase; corregir sería interpretar).

**¿`Concepto` es cajón de sastre?** Muestra aleatoria de 20 labels de tipo `Concepto`:

| Label muestra | Categoría implícita |
|---|---|
| "FC - Componente financiero" | concepto contable |
| "Nocional efectivo derivados tipo de cambio" | concepto de cálculo regulatorio |
| "Exposiciones de corto plazo" | categoría de cartera |
| "Evaluación de emisión particular" | proceso |
| "Primas de emisión COn1" | concepto contable |
| "Componente ILDC (intereses, arrendamientos y dividendos)" | componente contable |
| "Cámara de Compensación y Liquidación" | infraestructura del mercado |
| "Entidades" | supratipo regulado |
| "Activos deducibles del capital ordinario nivel 1" | concepto contable |
| "Violador Productor Usuario" | ruido del modelo |
| "Exposición riesgo crédito contraparte" | concepto técnico |
| "Reclamo" | objeto de proceso |
| "Deudas elegibles" | categoría regulatoria |
| "Personas humanas" / "Persona humana" | contraparte (duplicado léxico) |
| "CCP - Contraparte central" | infraestructura |
| "Dealing room" | unidad organizativa |
| "Capital por riesgo operacional" | métrica regulatoria |
| "Insumos y equipos para hidrocarburos offshore" | bien |
| "Ajustes por aplicación de NIIF" | proceso contable |

**Lectura honesta.** `Concepto` SÍ está actuando como cajón de sastre. Agrupa al menos 7 sub-roles heterogéneos: conceptos contables, métricas regulatorias, infraestructura del mercado, supratipos regulados, contrapartes, bienes/insumos, procesos. El schema-light no estratificó esto. En una iteración futura del schema convendría introducir sub-tipos emergentes específicos (`ConceptoMetrica`, `Infraestructura`, `Contraparte`, etc.) o usar `properties.subtype` para discriminar dentro de `Concepto`.

**Para este experimento queda documentado:** el tipo `Concepto` agrupa 23.2% del grafo y es semánticamente heterogéneo.

### D.5 Lente 5 — Duplicados léxicos de nodos post-dedup

**1 391 parejas sospechosas** (substring + mismo tipo, plural-canon distinto). Las parejas se clasificaron en tres categorías mutuamente excluyentes con `code/lens5_quantify.py` (output crudo en `code/cache/logs/lens5_quantify.log`):

- **`substring_strict`** — un label es prefijo o sufijo exacto del otro (a nivel palabras enteras) con palabras adicionales reales en el más largo. **Lectura: refinamiento legítimo** (el nodo más largo es una versión especializada/subtipo del más corto). NO son duplicados a resolver.
- **`norm_equivalent`** — al normalizar más allá de la heurística declarada en §3.5 (paréntesis residuales, siglas/abreviaturas, variantes de plural internas fuera de la heurística sufijal), los labels son equivalentes. **Lectura: duplicado real no fusionado por la heurística determinística.**
- **`ambiguous`** — no encaja claramente en ninguna de las dos. Son parejas con relación semántica difusa que la heurística de substring marcó por coincidencia parcial sin ser ni prefijo/sufijo limpio ni normalizables a equivalencia.

**Distribución global:**

| Categoría | Parejas | % | Lectura |
|---|---:|---:|---|
| `substring_strict` | **902** | **64.8%** | Refinamientos legítimos — NO son problema, son nodos distintos por diseño |
| `norm_equivalent` | **28** | **2.0%** | Duplicados reales — la heurística determinística no los fusionó |
| `ambiguous` | **461** | **33.1%** | Relación semántica difusa — no clasificable mecánicamente |
| **Total** | **1 391** | 100% | |

**Desglose interno de `norm_equivalent`:**

| Sub-categoría | Parejas | Ejemplos |
|---|---:|---|
| Paréntesis residual | 19 | `"Banco Central de la República Argentina"` ↔ `"Banco Central de la República Argentina (BCRA)"`; `"Superintendencia de Entidades Financieras y Cambiarias"` ↔ `"Superintendencia de Entidades Financieras y Cambiarias (SEFyC)"`; `"Exposición"` ↔ `"Exposición (EAD)"` |
| Plural interno (fuera de heurística sufijal) | 9 | `"Contrapartes"` ↔ `"Contraparte"`; `"Mipyme"` ↔ `"MiPyMEs"`; `"Cliente"` ↔ `"Clientes"` |
| Sigla / abreviatura pura | 0 | (no se detectaron — las siglas aparecen siempre con su forma expandida entre paréntesis, capturadas por la sub-categoría 1) |

**Distribución por tipo de nodo:**

| Tipo | substring_strict | norm_equivalent | ambiguous | total |
|---|---:|---:|---:|---:|
| Concepto | 459 | 22 | 321 | 802 |
| Operacion (CORE) | 170 | 0 | 80 | 250 |
| Restriccion (CORE) | 177 | 3 | 24 | 204 |
| InstrumentoFinanciero | 34 | 0 | 21 | 55 |
| EntidadFinanciera (CORE) | 43 | 0 | 10 | 53 |
| Autoridad | 5 | 3 | 2 | 10 |
| RegimenInformativo | 6 | 0 | 0 | 6 |
| Documento | 4 | 0 | 2 | 6 |
| Plazo | 2 | 0 | 1 | 3 |
| Excepcion (CORE) | 2 | 0 | 0 | 2 |

**Lectura cuantificada.** El 64.8% de las "parejas sospechosas" son refinamientos legítimos (el modelo emitió correctamente nodos especializados), no errores. Los duplicados reales son solo **28 parejas = 2.0% del total**, concentrados en `Concepto` (22) y `Autoridad` (3) — siglas con paréntesis y plurales internos. Esto es **el costo real de la resolución 100% determinística**: 28 duplicados léxicos no fusionados sobre 6 095 nodos = **0.46% del KG**. El 33.1% restante es relación semántica difusa que requeriría entendimiento de dominio para resolver.

**Posición declarada.** La **limitación §3.6** queda materializada con números: 28 duplicados reales identificables que un Sonnet o una heurística más agresiva habría fusionado. Este Run no los fusiona — la decisión de la estrategia es no usar LLM en post-procesamiento, y la heurística sufijal de plurales + lowercase + sin-acentos no captura paréntesis residuales ni plurales internos como "Persona humana" ↔ "Personas humanas".

### D.6 Lente 6 — Fragmentación profundizada

**Componente principal: 3 819 nodos = 62.7% del grafo.**

**Distribución por TO en el principal:**

| TO | Nodos en principal | Total nodos | % en principal |
|---|---:|---:|---:|
| TO_proteccion_usuarios | 307 | 426 | 72.1% |
| TO_exterior_cambios | 1 586 | 2 319 | 68.4% |
| TO_regimen_informativo | 353 | 590 | 59.8% |
| TO_clasificacion_deudores | 346 | 601 | 57.6% |
| TO_capitales_minimos | 1 227 | 2 159 | 56.8% |

**Lectura.** **El componente principal conecta los 5 TOs.** Cada uno aporta >56% de sus nodos al principal, y proporcionalmente Protección al Usuario y Exterior y Cambios son los más conectados (72.1% y 68.4%). Eso refleja que comparten muchas entidades atravesando dominios (BCRA, autoridades, conceptos cruzados como "Entidad financiera", "Operación de cambio").

**Por qué cayó de 67.3% (smoke v2 sobre 1 TO) a 62.7% (full sobre 5 TOs):** al sumar los 4 TOs nuevos aparecen **325 componentes no triviales** (vs 24 del smoke) — cada TO trae sub-grafos temáticos chicos (políticas internas, regímenes específicos) que no se conectan al principal porque no comparten entidades léxicamente con los otros TOs.

**Top 5 componentes no triviales (post-principal):**

- #2 (28 nodos, todos de Capitales Mínimos): titulizaciones — 22 Restricciones, 3 Excepciones, 2 Conceptos, 1 Operación.
- #3 (26 nodos, todos de Clasificación Deudores): financiación de comercio exterior con bancos del exterior — mezcla de 5 EntidadFinanciera, 9 Excepciones, etc.
- #4 (26 nodos, todos de Exterior y Cambios): documentación de imputación de cobros y certificaciones.
- #5 (23 nodos, todos de Capitales Mínimos): swaps de incumplimiento crediticio.
- #6 (20 nodos, todos de Exterior y Cambios): restricciones a giros de divisas.

Todos los demás componentes no triviales son mono-TO. **Eso indica que el cross-TO se concentra en el principal**; las islas son nichos temáticos específicos de cada TO. Razonable para un corpus regulatorio fragmentado.

### D.7 Lente 7 — Calidad de labels por tipo

| Tipo | n | min | median | mean | p95 | max | >8w | %>8w |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **Restriccion (CORE)** | 2 671 | 1 | 6 | 5.9 | 9 | 14 | **140** | **5.2%** |
| Concepto | 1 417 | 1 | 4 | 3.9 | 7 | 11 | 8 | 0.6% |
| **Operacion (CORE)** | 921 | 1 | 5 | 5.4 | 8 | 12 | **37** | **4.0%** |
| **Excepcion (CORE)** | 294 | 3 | 6 | 6.1 | 9 | 11 | **18** | **6.1%** |
| Documento | 240 | 2 | 3 | 3.6 | 7 | 10 | 3 | 1.2% |
| InstrumentoFinanciero | 210 | 1 | 4 | 4.0 | 7 | 9 | 2 | 1.0% |
| EntidadFinanciera (CORE) | 123 | 1 | 5 | 4.6 | 7 | 9 | 1 | 0.8% |
| RegimenInformativo | 82 | 1 | 4 | 3.9 | 7 | 8 | 0 | 0.0% |
| Autoridad | 64 | 1 | 4 | 4.2 | 7 | 9 | 1 | 1.6% |
| Plazo | 26 | 1 | 5 | 4.4 | 7 | 9 | 1 | 3.8% |
| ConceptoContable | 20 | 2 | 6 | 5.7 | 8 | 8 | 0 | 0.0% |
| Moneda | 6 | 1 | 2 | 2.0 | 3 | 3 | 0 | 0.0% |
| Sancion | 5 | 2 | 5 | 4.6 | 7 | 7 | 0 | 0.0% |
| Resto (7 tipos) | 14 | 1 | 2 | 2.5 | 6 | 6 | 0 | 0.0% |

**Hallazgos:**

1. **Restriccion** es el outlier esperado: 5.2% labels >8w (140 absolutos), max 14 palabras.
2. **Excepcion** (6.1%) y **Operacion** (4.0%) también son outliers — co-outliers con Restriccion. La autora ya intuía que Restriccion no estaría sola; confirmado.
3. **Labels-frase fuera de Restriccion sí existen** y son no triviales: 37 en Operacion, 18 en Excepcion, 8 en Concepto, 3 en Documento, 2 en InstrumentoFinanciero, 1 en EntidadFinanciera (única: "Proveedor de servicios de pago con cuentas de pago", 9 palabras), 1 en Autoridad, 1 en Plazo.
4. **Total labels-frase en el KG: 211 (3.5%).** Por encima del 2.5% del smoke v2 que era solo Protección al Usuario.

**Ejemplos de outliers fuera de Restriccion:**

- Operacion: `"Pago de capital e intereses de títulos con registro público en exterior"` (12w), `"Acceso al mercado de cambios para bienes de tiendas libres de impuestos"` (12w).
- Excepcion: `"Reducción a 11% y 8% con calificación 1, 2 o 3"` (11w), `"Exclusión de reservas de liquidez en cálculo A y D"` (10w).
- Concepto: `"Régimen de acceso a divisas para producción incremental de gas natural"` (11w).

**Confirmación de limitación C.1.** El refuerzo pedagógico de Regla 5 v2 no movió la aguja: persiste en Restriccion y se extiende a Excepcion y Operacion. Es limitación sistémica del modelo Haiku con restricciones operativas detalladas del corpus regulatorio.

---

## E. Apéndice — métricas complementarias

> Lentes adicionales que ya tenía generadas (no parte de las 7 originales). Se mantienen como información complementaria.

### E.1 Densidad del grafo

`edges / nodes = 5 764 / 6 095 = 0.946`. Por debajo de 1: grafo levemente esparso. Esperable para corpus regulatorio donde muchas Restricciones son aristas terminales (no se reúsan).

### E.2 Distribución de predicados core vs emergente (5 764 edges totales)

| | Conteo | % |
|---|---:|---:|
| Edges CORE (5 predicados) | 2 999 | 52.0% |
| Edges EMERGENT (506 predicados) | 2 765 | 48.0% |

Top 10 predicados (todos los tipos):

| Predicado | Conteo | % | Tipo |
|---|---:|---:|---|
| `aplica_a` | 1 506 | 26.1% | CORE |
| `recae_sobre` | 781 | 13.5% | CORE |
| `realiza` | 324 | 5.6% | CORE |
| `comprende` | 316 | 5.5% | emergente |
| `excepciona_a` | 316 | 5.5% | CORE |
| `requiere` | 252 | 4.4% | emergente |
| `regula` | 124 | 2.2% | emergente |
| `integra` | 106 | 1.8% | emergente |
| `exime_a` | 72 | 1.2% | CORE |
| `define` | 69 | 1.2% | emergente |

### E.3 `EntidadFinanciera` por `categoria`

123 nodos totales, distribución:

| Categoria | Conteo | % de EF |
|---|---:|---:|
| otra | 94 | 76.4% |
| fideicomiso_financiero | 6 | 4.9% |
| banco_comercial | 5 | 4.1% |
| casa_cambio | 5 | 4.1% |
| proveedor_no_financiero_credito | 4 | 3.3% |
| agencia_cambio | 3 | 2.4% |
| caja_credito | 2 | 1.6% |
| banco_inversion | 2 | 1.6% |
| compania_financiera | 1 | 0.8% |
| sgr | 1 | 0.8% |

Las 10 categorías del vocabulario se usaron. **76.4% caen en `otra`** — el modelo prefiere no comprometerse con categoría específica cuando el texto es genérico. **4 de los 94 `otra` son remapeos** desde `empresa_no_financiera_emisora_tarjeta` (post-procesamiento B.1).

### E.4 Canonicalización post-hoc de predicados (case + plurales)

| Métrica | Valor |
|---|---:|
| Predicados únicos crudos | 511 |
| Post-normalización (lowercase + sin acentos) | 510 |
| Post-plural-canónica | 509 |
| Reducción potencial | 0.4% |

**El modelo emitió formas casi perfectamente canónicas.** Solo 1 par case (`evalua` / `evalúa`), 1 par plural (`referencia` / `referencias`).

### E.5 Predicados con morfología sospechosa (no 3ra persona singular)

48 predicados con sufijo `_por` (pasivos) o prefijo `debe_` (perífrasis):

| Predicado | Conteo |
|---|---:|
| `debe_cumplir` | 10 |
| `es_otorgada_por` | 4 |
| `debe_garantizar` | 4 |
| `diferencia_por` | 5 |
| `calcula_por` | 2 |
| `determina_por` | 2 |
| `ajusta_por` | 1 |
| (otros 41) | 1-2 c/u |

**Total instancias afectadas: ~80 edges = 1.4%.** Cumple ampliamente la regla con tolerancia razonable.

---

## F. Inventario del directorio `code/`

| Archivo | Propósito |
|---|---|
| `prompts.py` | `SYSTEM_PROMPT` v2 + `USER_PROMPT_TEMPLATE`. Codifica el schema híbrido (4 core + 5 relaciones core↔core + 6 reglas no negociables) y las decisiones de modelado §3.1–§3.6. Sincronizado con `schema.md`. |
| `models.py` | Modelos Pydantic. Dos capas: `ChunkExtraction` (lo que devuelve Haiku, sin provenance) y `KGNode`/`KGEdge`/`KnowledgeGraph` (lo que va al `kg.json` final, con provenance inyectada). `relations: list = Field(default_factory=list)` por lección Run 1. |
| `chunker.py` | Pipeline `PDF → texto → corte por puntos numerados (MAX_CUT_DEPTH=2) → merge de chunks chicos → hard-split en cascada (párrafos → oraciones → líneas → bruto) con `HARD_CHUNK_CHAR_LIMIT=6000``. Produce `Chunk(chunk_id, source_doc, location, text)`. |
| `extract.py` | Pipeline asyncio principal. `concurrency=3`, backoff conservador (3 retries, base 2.0), cache por chunk individual. `ProgressTracker` con `flush=True` (lección Run 2). **Función `hydrate_with_provenance(extraction, chunk)` que inyecta `provenance` desde el contexto del chunk a cada entity/edge** (decisión §3.7 del schema). |
| `assemble.py` | Ensamblador del KG final. Aplica `canonicalize_categoria → "otra"` (B.1), dedup determinístico §3.5, filtro de jerarquía documental (refuerzo Regla 6), descarta self-loops y edges cross-chunk. Produce `kg.json`. |
| `visualize.py` | Visualización pyvis. Colores por tipo (CORE con paleta saturada, emergentes atenuada), labels en hover (con `description`, `categoria`, `provenance`), barnes-hut layout. Produce `kg_visual.html`. |
| `analyze_smoke.py` | Análisis post-smoke. 5 reportes: candidatos `Concepto → EntidadFinanciera`, dedup, estructura del grafo, calidad de labels, comparativo v1 vs v2 (post-iteración del schema). |
| `lenses.py` | Las 7 lentes originales sobre el `kg.json` final. Insumo de la sección D de este reporte. |
| `final_metrics.py` | Métricas adicionales (densidad, cobertura por TO, EntidadFinanciera por categoria, canonicalización predicados). Insumo de la sección E. |
| `cache/chunks/` | 528 archivos JSON, uno por chunk extraído. Reanudación incremental: re-corre `extract.py` y solo procesa los pendientes. |
| `cache/chunks_v1/` | 48 archivos JSON del smoke v1 (preservados para la comparativa v1 vs v2 del reporte 5). NO contribuyen al `kg.json` final. |
| `cache/logs/` | Logs de runs: `smoke_run.log`, `smoke_v2_run.log`, `full_run.log`, `lenses.log`, `final_metrics.log`. |
| `.env` | `ANTHROPIC_API_KEY` (gitignored). |

---

## G. Resumen del experimento

- **5 TOs procesados**, 528 chunks, 7 536 nodos crudos → **6 095 nodos finales** + **5 764 edges**, **densidad 0.946**, **20 tipos de entidad únicos**, **511 predicados únicos** (5 CORE + 506 emergentes).
- **Cobertura: 5/5 TOs** generan tripletas. Componente principal aglutina **62.7%** del grafo y conecta los 5 TOs.
- **Costo total: USD 7.88** (28% bajo el límite de USD 11). Cero fails y cero throttles 429 en 528 chunks.
- **Una iteración del schema** (v1 → v2) durante el smoke, motivada por inconsistencia interna entre §3.3 y el vocabulario controlado de §3.5. Iteración acotada (no inversión total), congelada después del smoke v2.
- **Decisiones de post-procesamiento determinístico** (B.1–B.4): canonicalización de `categoria` a `"otra"`, dedup determinístico, filtro post-hoc de jerarquía documental, descarte de self-loops y cross-chunk edges. **No tocan el schema.**
- **Limitaciones declaradas honestamente** (C.1–C.4): labels-frase 3.5% del KG en core; `EntidadFinanciera` huérfanas (10 nodos); 4 remapeos `empresa_no_financiera_emisora_tarjeta → otra`; 1 391 parejas léxicas no fusionadas por la heurística determinística.

### Hallazgos cualitativos centrales del experimento

Más allá de las métricas agregadas, dos observaciones estructurales que definen lo que Run 5 mostró:

1. **Adherencia desigual al schema declarado.** La Regla 4 (cierre core↔core) fue la regla con menor adherencia: **22.6% de los edges entre dos nodos core usan predicados emergentes libres** en lugar de las 5 canónicas (`realiza`, `aplica_a`, `recae_sobre`, `excepciona_a`, `exime_a`), y **`aplica_a` se invierte el 9.5% de las veces** (Operacion→Restriccion en lugar de Restriccion→Operacion, siguiendo el orden gramatical de la oración fuente). Esto cuestiona empíricamente cuán "rígido" puede ser un núcleo cerrado cuando convive en el mismo prompt con libertad schema-light en el resto: la combinación de criterios cerrados (5 predicados, dominios y rangos fijos) y abiertos (libertad para todo lo demás) genera una zona ambigua donde el modelo opta por la flexibilidad incluso para conexiones core↔core. Ver §D.2 para el desglose por predicado y direcciones invertidas.

2. **Multi-instanciación por rol.** **176 grupos de labels normalizados aparecen con `type` distinto según el rol que cumplen en cada chunk fuente** ("Clasificación de deudores" como `Operacion`/`Restriccion`/`RegimenInformativo`/`Concepto`; "Supervisión consolidada" en cuatro tipos; "Cobertura del riesgo de crédito" en tres). Esta es **característica emergente del schema-light + chunking + extracción intra-chunk**: el modelo procesa cada chunk independientemente y, sin contexto global, elige el tipo que mejor refleja el rol local del término, lo cual puede variar entre chunks. La consecuencia operacional concreta para consultas downstream es que cualquier query sobre una entidad léxica con multi-rol va a requerir **multi-hop entre representaciones del mismo concepto léxico**: el nodo `Restriccion("Clasificación de deudores")` y el nodo `Operacion("Clasificación de deudores")` son nodos distintos en el grafo, no conectados entre sí salvo por el ensamblaje de aristas heredadas de sus chunks de origen. Ver §D.1 para los 8 casos más severos.

Estos dos hallazgos son lo que la estrategia híbrida produjo de no-obvio cuando se la materializa sobre un corpus regulatorio normativo de escala mediana. No son fallas del modelo Haiku ni del prompt v2 — son consecuencias del diseño del schema en interacción con el corpus.

Termina acá. **NO se evalúa el KG** — eso es la FASE 2.3 del proyecto. NO se hacen commits.
