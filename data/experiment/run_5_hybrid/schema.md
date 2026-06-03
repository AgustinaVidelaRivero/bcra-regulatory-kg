# Schema — Run 5: Híbrido core + emergente

> **Estado del documento.** Esta es la versión **pre-smoke**: contiene el núcleo rígido (core) y las decisiones de modelado declaradas antes de extraer. Los tipos y predicados **emergentes** se completan post-hoc, después del full run, en las secciones marcadas como *(a completar post-extracción)*.

---

## 1. Estrategia

Híbrido **schema-based en el núcleo crítico** + **schema-light en todo lo demás**:

- Un **core cerrado** de **4 tipos de entidad** y **5 tipos de relación** entre ellos. Estos tipos son no negociables, tienen definición fija y son los que el LLM debe usar siempre que la mención lo permita.
- **Schema-light para el resto**: cualquier mención que no encaje en los 4 tipos core se clasifica con un **tipo emergente** elegido libremente por el LLM. Los predicados entre core ↔ emergente y emergente ↔ emergente son libres (lenguaje natural en español), pero con **una sola forma morfológica obligatoria**: tercera persona singular del presente del indicativo, `snake_case`, sin sujeto (ejemplos del lexicón guía: `regula`, `define`, `requiere`, `autoriza`, `supervisa`, `comprende`, `vence_en`, `expresa_en`). Esta restricción reduce la explosión léxica que el `report.md` mide post-hoc.

El objetivo es maximizar consistencia donde más importa (los sujetos regulados, las operaciones, las restricciones, las excepciones) y conservar cobertura sobre el resto del dominio (autoridades, conceptos, plazos, instrumentos, sanciones, etc.) sin forzar prematuramente un schema cerrado sobre material que aún no entendemos.

---

## 2. Core (cerrado, no negociable)

### 2.1 Tipos de entidad core (4)

| # | Tipo | Definición | Qué SÍ es | Qué NO es |
|---|---|---|---|---|
| 1 | `EntidadFinanciera` | Sujeto regulado por el BCRA: persona jurídica autorizada o comprendida en la regulación cuyo comportamiento queda sujeto a obligaciones, límites o autorización del BCRA. | Bancos comerciales, bancos de inversión, compañías financieras, cajas de crédito, casas y agencias de cambio, fideicomisos financieros, sociedades de garantía recíproca, proveedores no financieros de crédito, etc. — siempre como nombre propio o tipificación inequívoca. | **NO** son entidades financieras: el BCRA, la Superintendencia, otros reguladores (Autoridad). Las **categorías genéricas** ("entidades comprendidas en la LEF", "bancos comerciales" como clase) van como `Concepto` (ver §3.3). |
| 2 | `Operacion` | Acción regulada que una `EntidadFinanciera` realiza o puede realizar dentro del sistema financiero, sobre la que el BCRA impone obligaciones, requisitos o límites. | Otorgar financiaciones, recibir depósitos, transferir fondos, comprar/vender divisas, otorgar garantías, clasificar deudores, presentar regímenes informativos, integrar capitales mínimos, etc. | NO son operaciones los conceptos abstractos sin acción (ej. "el sistema financiero" como entidad teórica). |
| 3 | `Restriccion` | Norma operativa específica que limita, condiciona o exige conducta sobre una `Operacion` o sobre una `EntidadFinanciera`. Es la unidad mínima de obligación regulatoria. | Topes cuantitativos (importes máx/mín), requisitos (capital mínimo, documentación), prohibiciones, plazos obligatorios, criterios de clasificación, condiciones de elegibilidad. | NO son restricciones los enunciados puramente declarativos sin contenido normativo. |
| 4 | `Excepcion` | Norma que **modifica** una `Restriccion` existente: la atenúa, la suspende o exime a un sujeto o a una operación específica de su cumplimiento. | "Quedan exceptuadas las operaciones X de la prohibición Y", "no se aplica el tope A a la entidad B", "no rige el plazo Z cuando…". | NO es excepción una restricción menos estricta — es excepción solo cuando el texto la marca como exclusión/exención respecto de otra norma. |

### 2.2 Relaciones core ↔ core (cerradas, 5)

| Predicado | Dominio | Rango | Semántica |
|---|---|---|---|
| `realiza` | `EntidadFinanciera` | `Operacion` | El sujeto regulado lleva a cabo (o está autorizado a llevar a cabo) la operación. |
| `aplica_a` | `Restriccion` | `Operacion` | La restricción regula esa operación específica. |
| `recae_sobre` | `Restriccion` | `EntidadFinanciera` | La restricción es subjetiva: regula directamente al sujeto, no a una operación. |
| `excepciona_a` | `Excepcion` | `Restriccion` | La excepción modifica/atenúa esa restricción. |
| `exime_a` | `Excepcion` | `EntidadFinanciera` ∪ `Operacion` | La excepción excluye explícitamente a un sujeto o a una operación del alcance de la restricción que excepciona. |

**Cierre.** Estas 5 son las **únicas** relaciones permitidas core↔core. Si el LLM detecta una conexión entre dos nodos core que no encaja en ninguna de estas 5, **no debe inventar un predicado core↔core nuevo**: o bien la modela mediada por un nodo emergente, o bien la descarta.

---

## 3. Decisiones de modelado explícitas

Las seis decisiones que cierran ambigüedad operacional de la estrategia híbrida.

### 3.1 Prioridad CORE sobre EMERGENTE

Si una mención **puede** clasificarse como tipo core (`EntidadFinanciera`, `Operacion`, `Restriccion`, `Excepcion`) **o** como tipo emergente, **siempre se prefiere el tipo core**.

Si la mención es ambigua entre dos tipos core, se elige el más específico al rol que cumple en la oración:

- Una "obligación" que **describe lo que un sujeto debe hacer** → `Restriccion` (no `Operacion`).
- Una "exención" que **modifica otra norma** → `Excepcion` (no `Restriccion`).
- Una "actividad" descrita como acción concreta del sujeto → `Operacion`.
- Un "tipo de entidad" referido como sujeto que actúa → `EntidadFinanciera` (si es nombre propio o tipificación inequívoca; si es categoría genérica, ver §3.3).

### 3.2 BCRA y otras autoridades regulatorias

**El BCRA, la Superintendencia de Entidades Financieras y Cambiarias (SEFyC), y cualquier otra autoridad regulatoria mencionada NO son `EntidadFinanciera`.** Son reguladores, no sujetos regulados.

→ Se modelan como tipo emergente **`Autoridad`** (con la misma convención de `label` y `properties` que cualquier otro emergente). Conectan con los nodos core con predicados libres (típicamente `regula`, `autoriza`, `supervisa`, `recibe_de`).

Esta decisión protege la semántica del tipo `EntidadFinanciera` (= "sujeto regulado"). Sin ella, el BCRA aparecería como nodo regulado de sí mismo, lo cual es absurdo y contamina las consultas downstream sobre sujetos del sistema financiero.

### 3.3 Conceptos abstractos vs. entidades concretas (v2 — post-smoke)

> **Iteración v1 → v2.** La v1 ("categoría genérica como clase regulatoria → Concepto") generaba inconsistencia interna con el vocabulario controlado de `EntidadFinanciera.categoria` declarado en §3.5: las propias categorías reconocidas (`casa_cambio`, `fideicomiso_financiero`, `proveedor_no_financiero_credito`, etc.) caían sistemáticamente en `Concepto` cuando aparecían como tipificación general en el corpus, vaciando el tipo core `EntidadFinanciera` (smoke v1: 1/505 = 0.2%). La v2 resuelve la contradicción con un criterio de cruce: categoría reconocida + rol de sujeto activo en la oración → `EntidadFinanciera`; supratipo agregado / contraparte / abstracción → `Concepto`.

Para distinguir `EntidadFinanciera` de `Concepto` (emergente) sobre la misma superficie léxica:

- **Nombre propio** ("Banco de la Nación Argentina", "Banco Santander") → `EntidadFinanciera` con `properties.categoria` aplicable.

- **Tipificación de un rol regulado con CATEGORÍA RECONOCIDA del vocabulario controlado de §3.5** ("operador de cambio", "casa de cambio", "agencia de cambio", "fiduciario de fideicomiso financiero", "proveedor no financiero de crédito", "empresa no financiera emisora de tarjeta", "compañía financiera", "caja de crédito", "banco comercial", "banco de inversión", "SGR / sociedad de garantía recíproca"), **cuando aparece como SUJETO de una obligación, autorización o restricción concreta** ("los operadores de cambio deben…", "las cajas de crédito pueden…", "los fiduciarios presentarán…") → `EntidadFinanciera` con `properties.categoria` del vocabulario controlado.

- **Supratipos agregados sin categoría única** ("Sujeto obligado", "Entidad financiera" como término definido del glosario que agrupa varias categorías heterogéneas) → `Concepto`. No tienen una `categoria` del vocabulario porque son uniones de categorías.

- **Contrapartes de la operación regulada** (Usuario, Deudor, Cliente, Beneficiario, Cedente, Tomador) → `Concepto`. No son sujetos regulados aunque participen en la operación.

- **Conceptos jurídicos/técnicos abstractos** ("el sistema financiero", "el régimen cambiario", "la solvencia", "la liquidez", "la posición global neta") → `Concepto`.

**Heurística operativa:** si la mención encaja en alguna de las 10 `categoria` del vocabulario controlado de §3.5 Y el texto le atribuye obligación/autorización/restricción como sujeto → `EntidadFinanciera`. Si es término-glosario que agrupa varias categorías, o contraparte, o concepto abstracto → `Concepto`.

### 3.4 Cierre completo de relaciones core↔core

`exime_a` se incluye en el cierre con rango unión `EntidadFinanciera ∪ Operacion`, porque las excepciones del corpus alternan entre eximir sujetos ("no aplica a las cajas de crédito") y eximir operaciones específicas ("quedan exceptuadas las financiaciones de comercio exterior"). Es un caso muy común en los 5 TOs del subset, lo dejamos cubierto.

Por convención, las uniones en rango se permiten **solo** para `exime_a`. Las otras 4 relaciones core↔core tienen rango simple.

### 3.5 Reglas de `label`, propiedades y dedup (v2 — post-smoke)

> **Iteración v1 → v2.** El smoke v1 reveló dos patrones recurrentes: (a) `Restriccion` con labels-frase que incluían el cuerpo normativo dentro del propio label (2.6% del corpus), (b) referencias documentales entre paréntesis filtradas al label ("Sujetos obligados (punto 1.1.2)"). v2 agrega ejemplos negativos concretos en el prompt para frenar esos patrones, sin cambiar la regla declarada.

**`label`:**
- Forma canónica corta, **máximo 8 palabras**.
- Sin numeración de puntos ("3.16.3.4") ni referencias documentales — eso va exclusivamente en `provenance.location`, inyectado por el pipeline.
- **NUNCA referencias documentales entre paréntesis dentro del `label`.** Ejemplos:
  - ❌ MAL — `"Sujetos obligados (punto 1.1.2)"`, `"Régimen informativo (Anexo I)"`, `"Restricción cambiaria (sección 3)"`.
  - ✅ BIEN — `"Sujetos obligados"`, `"Régimen informativo"`, `"Restricción cambiaria"`. La ubicación va a `provenance.location`.
- **El cuerpo de la obligación NUNCA va en el label.** El label es el título corto identificatorio; el cuerpo normativo va a `properties.description`. Ejemplos:

  - ❌ MAL — `label: "Atención en condiciones de igualdad a usuarios con discapacidad auditiva"` (10w, contiene el cuerpo).
  - ✅ BIEN — `label: "Atención a usuarios con discapacidad auditiva"` (6w), `description: "Las entidades deben atender a personas con discapacidad auditiva en condiciones de igualdad que al resto de los usuarios."`

  Aplica especialmente al tipo `Restriccion`.

- Texto largo y descriptivo va en `properties.description` (sin límite estricto, ideal ≤ 300 caracteres).

**Desempaquetado:**
- Si una mención **enumera N elementos** ("las cajas de crédito, las casas de cambio y las compañías financieras"), se generan **N nodos** separados, no uno solo agrupado.
- Si la enumeración comparte una restricción/operación común, se generan N edges (uno por nodo desempaquetado).

**Dedup determinístico (paso de ensamblaje):**
- Normalización del `label` antes de hashear: `lowercase` + sin acentos (NFD + strip combining marks) + colapso de espacios + recorte.
- Heurística simple de plurales: se prueba quitar sufijos `es` y `s` solo si el restante tiene ≥ 4 caracteres y coincide con otro `label` ya visto.
- **`EntidadFinanciera`** lleva además `properties.categoria` (vocabulario controlado: `banco_comercial`, `banco_inversion`, `compania_financiera`, `caja_credito`, `casa_cambio`, `agencia_cambio`, `fideicomiso_financiero`, `sgr`, `proveedor_no_financiero_credito`, `otra`). El campo es **OBLIGATORIO** cuando `type=EntidadFinanciera`; si no se infiere con seguridad desde el texto, se usa `"otra"`. Dos `EntidadFinanciera` con `label` distinto pero misma `categoria` y misma normalización colapsan al mismo nodo.

### 3.6 Resolución 100% determinística

**No se usa Sonnet (ni ningún LLM) en ninguna etapa de resolución de entidades.** Toda la deduplicación, fusión y canonicalización se hace por reglas determinísticas (las del §3.5). Los **clusters ambiguos** que las reglas no resuelven **quedan tal cual** (como nodos separados, posiblemente duplicados semánticamente), y se documentan en `report.md` como **limitación conocida de la estrategia**.

Esto mantiene la comparabilidad con la estrategia declarada en la propuesta (híbrido = core rígido + emergente libre + dedup automático, sin segundo paso semántico costoso) y aísla el costo de inferencia a la sola extracción Haiku.

---

## 3.7 Decisión sobre `provenance` y `version`

**`provenance` se inyecta en el ensamblaje, no lo emite el modelo.** Cada PDF se chunkea con `(source_doc, location)` conocidos por el pipeline (nombre del archivo + ruta jerárquica del punto/sección). El extractor le pasa el `location` al modelo en el `USER_PROMPT_TEMPLATE` solo como contexto, pero el modelo NO devuelve `provenance` en su JSON. En el ensamblaje, el pipeline anexa `provenance = {"source_doc": chunk.source_doc, "location": chunk.location}` a cada entity y a cada relation extraída de ese chunk. Razones:

1. Evita alucinaciones de ubicación: el modelo podría parafrasear, truncar o inventar referencias documentales.
2. Reduce tokens de salida (menos costo).
3. Mantiene `provenance` 100% trazable al chunk de origen.

**`properties.version` no se emite.** El protocolo (§c.2) explicita "para este experimento basta con la versión vigente". Como los 5 TOs del subset son **todos** versión vigente, agregar `"version": "vigente"` a todos los nodos sería redundancia constante: inflaría el JSON sin información discriminativa. Si en una extensión futura del corpus se agregaran versiones históricas, ahí se introduce el campo (y se modela como nodo separado con `version` distinto, como dice el protocolo).

---

## 4. Tipos emergentes encontrados (post-extracción)

El schema-light permitió 16 tipos emergentes únicos sobre 6 095 nodos del KG final. Inventario completo por conteo:

| # | Tipo emergente | Conteo | % del grafo | Notas |
|---|---|---:|---:|---|
| 1 | `Concepto` | 1 417 | 23.2% | **Cajón de sastre confirmado**: agrupa conceptos contables, métricas regulatorias, infraestructura del mercado, supratipos regulados, contrapartes, bienes/insumos, procesos. Ver report.md §D.4. |
| 2 | `Documento` | 240 | 3.9% | Manuales de procedimientos, normas referidas, comunicaciones citadas. |
| 3 | `InstrumentoFinanciero` | 210 | 3.4% | Derivados, títulos, bonos, swaps, ABS, MBS, etc. |
| 4 | `RegimenInformativo` | 82 | 1.3% | Regímenes de reporte (clasificación de deudores, SECOEXPO, etc.). |
| 5 | `Autoridad` | 64 | 1.1% | BCRA, SEFyC, CNV, Aduana, etc. (decisión §3.2). |
| 6 | `Plazo` | 26 | 0.4% | "5 días hábiles", "90 días corridos", etc. |
| 7 | `ConceptoContable` | 20 | 0.3% | Sub-tipo de Concepto que el modelo introdujo para conceptos del balance/contabilidad regulatoria. |
| 8 | `Moneda` | 6 | 0.1% | Pesos, USD, EUR, etc. |
| 9 | `Sancion` | 5 | 0.1% | Sanciones aplicables, multas. |
| 10 | `NormaSuprior` | 4 | 0.1% | **Typo del modelo** ("Norma Superior"). Se deja como salió porque el schema-light no obliga corrección. |
| 11 | `InstrumentoLegal` | 3 | <0.1% | Convenios, contratos modelo. |
| 12 | `RegimenNormativo` | 3 | <0.1% | Sub-tipo emergente del régimen regulatorio. |
| 13 | `ConceptoInformativo` | 3 | <0.1% | Sub-tipo de Concepto introducido por el modelo. |
| 14 | `SistemaOperativo` | 1 | <0.1% | "Banca por Internet" (uso técnico, no S.O. computacional). |
| 15 | `NormaExterna` | 1 | <0.1% | Norma de otro organismo (Ley citada). |
| 16 | `CuentaBancaria` | 1 | <0.1% | Una mención específica como tipo. |

**Total emergente: 2 086 nodos = 34.2% del grafo.**

**Near-dups detectados:**
- `Concepto` (1 417) ↔ `ConceptoContable` (20) ↔ `ConceptoInformativo` (3) — sub-tipos legítimos que el modelo introdujo, no son duplicados.
- `NormaSuprior` (4) es typo de "NormaSuperior". No fusionado.

**Conclusión §4.** El schema-light produjo 16 tipos emergentes naturales. El más problemático es `Concepto` por su heterogeneidad interna; el resto son específicos y útiles. La estrategia híbrida cumplió su objetivo de descubrir tipos sin pre-declararlos.

---

## 5. Relaciones emergentes encontradas (post-extracción)

506 predicados emergentes únicos sobre 2 765 edges emergentes (48% del KG). El top 100 cubre 77.1% de los edges emergentes.

### 5.1 Familias semánticas

Los predicados emergentes se agruparon manualmente en 10 familias (ver report.md §D.3 para detalles):

| Familia | Predicados ejemplo | Edges en familia |
|---|---|---:|
| Definición / inclusión | `comprende`, `integra`, `define`, `incluye`, `agrupa` | 605 |
| Obligación / requerimiento | `requiere`, `condiciona`, `debe_cumplir`, `exige` | 351 |
| Regulación / normativa | `regula`, `autoriza`, `establece`, `determina` | 268 |
| Referencia / vínculo | `referencia`, `refiere_a`, `emite`, `vincula_a` | 119 |
| Información / reporte | `informa_a`, `registra`, `publica`, `presenta_a` | 82 |
| Modificación / actualización | `modifica`, `actualiza` | 54 |
| Alcance / aplicabilidad | `aplica`, `afecta`, `afecta_a` | 39 |
| Cálculo / cuantificación | `expresa_en`, `calcula`, `diferencia_por` | 33 |
| Atribución / propiedad | `otorga`, `mantiene` | 15 |
| Exclusión / excepción | `excluye` | 9 |

**Predicados emergentes sin familia obvia** (top 5): `especifica` (61), `utiliza` (59), `clasifica` (33), `pertenece_a` (28), `considera` (19). Son emergentes "puros".

### 5.2 Adherencia a la forma morfológica declarada (3ra persona singular del presente)

- **Predicados que cumplen la forma:** ~98.6% de los edges emergentes.
- **Predicados con morfología sospechosa** (sufijo `_por`, perífrasis con `debe_`): 48 predicados únicos, ~80 instancias = **1.4% del KG**.
- Los top ofensores son `debe_cumplir` (×10), `es_otorgada_por` (×4), `debe_garantizar` (×4). Aceptable.

### 5.3 Reducción potencial post-hoc

Si cada familia colapsara a 1 predicado canónico, el top 100 emergentes pasaría de **51 a 10 predicados** (reducción 41 únicos). **Esta normalización NO se aplicó al KG** — se reporta como métrica comparativa para la FASE 2.3.

### 5.4 Cierre core↔core (sección 2.2)

**El cierre no se respetó al 100%.** 554/2 449 edges core↔core (22.6%) usan predicados emergentes no canónicos (`requiere`, `comprende`, `especifica`, `condiciona`). Ver report.md §D.2 para la validación completa y direcciones invertidas en los 5 canónicos.

---

## 6. Cómo se conectaron core y emergente

**Patrón general.** El modelo conectó tipos core con emergentes mayoritariamente con predicados de las familias *definición/inclusión* (`comprende`, `integra`, `define`) y *regulación/normativa* (`regula`, `establece`). Las familias *referencia/vínculo* e *información/reporte* aparecen específicamente para conectar `Documento`, `RegimenInformativo` y `Autoridad` con los nodos core.

### 6.1 Cada tipo core y sus emergentes complementarios

**`EntidadFinanciera` (123 nodos)** se conecta principalmente con:
- `Concepto` (categorías regulatorias agregadas, supratipos como "Sujeto obligado", contrapartes como "Usuario").
- `Autoridad` (BCRA, SEFyC) — vía `regulada_por`, `supervisada_por`, `autorizada_por`.
- `Documento` (régimen normativo, comunicaciones) — vía `cumple`, `aplica`.
- `InstrumentoFinanciero` — vía `emite`, `otorga`, `administra`.

**`Operacion` (921 nodos)** se conecta con:
- `InstrumentoFinanciero` — vía `utiliza`, `involucra`, `referencia`. Captura operaciones sobre instrumentos.
- `Plazo` — vía `vence_en`, `tiene_plazo_de`. Plazos asociados.
- `Moneda` — vía `expresa_en`, `denominada_en`.
- `Concepto` y `ConceptoContable` — vía `integra`, `comprende`, `define`.

**`Restriccion` (2 671 nodos)** se conecta con:
- `Concepto`, `ConceptoContable` — vía `requiere`, `condiciona`, `establece`. La gran mayoría de las restricciones definen condiciones sobre conceptos.
- `Documento` — vía `referencia`, `se_basa_en`. La restricción cita normas vinculadas.
- `Autoridad` — vía `recibe_de`, `informa_a`. El destinatario regulatorio.
- `Plazo`, `Moneda`, `InstrumentoFinanciero` — atributos cuantitativos de la restricción.

**`Excepcion` (294 nodos)** se conecta con:
- `Concepto` — vía `aplica_si`, `excluye`. Condiciones de aplicabilidad de la excepción.
- `Documento` — vía `referencia`, `prevista_en`.
- `Plazo` — excepciones temporales.

### 6.2 Casos donde el límite core/emergente quedó borroso

**Lectura honesta de hallazgos del KG final** (cruz con report.md §D.1):

1. **Mismo término léxico con tipo distinto según chunk:** 176 grupos de labels con tipos múltiples (ver report.md §D.1). El más severo: "Supervisión consolidada" como `Concepto`, `Restriccion`, `Operacion` Y `RegimenInformativo` simultáneamente. Esto es característica emergente de la estrategia híbrida sobre corpus regulatorio donde el mismo término cumple roles distintos contextualmente.

2. **`Concepto` cajón de sastre:** 23.2% del grafo. Conviene en una iteración futura introducir sub-tipos emergentes (`ConceptoMetrica`, `Infraestructura`, `Contraparte`) o usar `properties.subtype`. Para este Run queda documentado.

3. **`EntidadFinanciera` vs `Concepto` para "Sujeto obligado", "Entidades financieras":** la regla v2 §3.3 resolvió la mayor parte de los casos, pero algunas menciones como categoría agregada siguen apareciendo como `Concepto` cuando el chunk no le atribuye explícitamente un rol de sujeto. Es comportamiento esperado del cruce de condiciones (categoría reconocida + rol de sujeto).

4. **`Restriccion` vs `Excepcion`:** la regla v2 funcionó bien — el modelo solo emite `Excepcion` cuando el texto marca explícitamente exención/exclusión respecto de otra norma. 294 `Excepcion` vs 2 671 `Restriccion` (ratio 1:9) parece razonable para el corpus.

5. **Cierre core↔core relajado:** 22.6% de edges core↔core usan predicados libres en lugar de los 5 canónicos. La Regla 4 fue la menos respetada del schema. Eso pone en evidencia que un schema con relaciones cerradas requiere disciplina del modelo que el prompt de un solo paso no garantiza completamente.

---
