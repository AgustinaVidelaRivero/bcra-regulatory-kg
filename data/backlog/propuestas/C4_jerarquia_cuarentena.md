# Propuesta C4 — Aristas de jerarquía para los sujetos de cuarentena

Entrada del backlog: **BKL-0019** (fuente: `vara`, diagnóstico
`adjudicado_humano`, especie `alcanzabilidad`; laudo de triage ya tomado:
las 9 aristas `subclase_de` según los `padres_sugeridos` de
`data/experiment/grafo_v2/reensamblado_v3/cuarentena.json`).
BKL-0020/0021 (los dos sujetos sin padre sugerido) y BKL-0022 (seguimiento
del huérfano léxico) NO son de esta unidad; BKL-0022 queda mitigado por
navegación si entra la arista de `…grupo_2` (su verificación propia es
post-BKL-0019).
Formato: `.claude/skills/kg-refinement/references/formato_propuesta.md`.
Estado: PROPUESTA — la aplicación es otra unidad (Fase 2 de C4, post-laudo
y commit de la adjudicadora).

## 1. Estado real re-verificado en el vigente (post-C1/C2/C3)

Los conteos del expediente de retriage eran pre-C1/C2/C3; re-verificado en
esta unidad contra el vigente
`data/experiment/grafo_v2/reensamblado_v3/kg.json` (4.459 nodos / 8.046
aristas): **nada cambió para esta entrada** —

- Los 11 sujetos de `cuarentena.json` existen como nodos (`rol_fuente:
  cuerpo`), **ninguno** tiene arista `subclase_de` (ni ninguna otra
  saliente), y todos tienen **solo `aplica_a` entrantes** (inversor 4,
  grupo_1 2, el resto 1 cada uno).
- Los 9 con `padres_sugeridos` siguen siendo los mismos 9 de BKL-0019; los
  5 padres sugeridos distintos existen todos en el vigente con
  `rol_fuente: esqueleto`.
- `subclase_de` pre: **57** aristas (las 57 con ambos endpoints en el set
  de clases del `data/experiment/grafo_v2/esquema_v2_clases.json`; cero
  excepciones). Los roles del schema (nivel `rol`) reciben exclusivamente
  `miembro_de` (17 aristas).

Reproduce:
`python3 -c "import json; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); print(len(kg['nodes']), len(kg['edges']), sum(1 for e in kg['edges'] if e['relation']=='subclase_de'))"`
→ `4459 8046 57`.

## 2. Las 9 aristas propuestas (tabla del laudo)

Cada fila: sujeto (id verbatim) → padre sugerido (id verbatim, verificado
EXISTENTE en el esqueleto del vigente) + validación semántica contra el
árbol de sujetos del schema v2 (vocabulario cerrado de
`esquema_v2_clases.json`: 65 clases / 5 roles).

| # | Sujeto (source, verbatim) | Padre sugerido (target, verbatim) | Validación semántica |
|---|---|---|---|
| 1 | `Sujeto_propuesto_inversor` | `Sujeto_contraparte` | OK — en CapMin 3.1 (titulizaciones, criterios STC) el inversor es contraparte de la operación; `Sujeto_contraparte` es clase del vocabulario, padre directo de figuras análogas (`Sujeto_acreedor_del_exterior`, `Sujeto_emisor_de_titulos_de_deuda`); sin disyunciones violadas. |
| 2 | `Sujeto_propuesto_entidades_financieras_del_grupo_1` | `Sujeto_entidad_financiera` | OK — partición regulatoria de entidades financieras (CapMin 2.11); subclase directa, hermana de `Sujeto_banco` / `Sujeto_compania_financiera`. |
| 3 | `Sujeto_propuesto_beneficiarios_de_radpip_y_o_radpign` | `Sujeto_contraparte` | OK — beneficiarios de regímenes de acceso al mercado de cambios (Exterior 3.17); análogo directo del hijo existente `Sujeto_beneficiario_economia_conocimiento` ("beneficiario de régimen" bajo contraparte). |
| 4 | `Sujeto_propuesto_entidades_del_grupo_a` | `Sujeto_entidad_financiera` | OK — el "Grupo A" del Régimen Informativo (RegInf 4) clasifica entidades financieras; consistente con que el rol `Sujeto_rol_entidad_comprendida_reginf` tiene como único miembro a `Sujeto_entidad_financiera`. |
| 5 | `Sujeto_propuesto_entidades_financieras_del_grupo_2` | `Sujeto_entidad_financiera` | OK — ídem fila 2 (CapMin 2.11). Además resuelve por navegación la orfandad léxica de BKL-0022 (§4). |
| 6 | `Sujeto_propuesto_inversores_y_tenedores_de_titulizacion` | `Sujeto_contraparte` | OK — ídem fila 1 (CapMin 3.1). |
| 7 | `Sujeto_propuesto_originante_acreedor_inicial` | `Sujeto_rol_alcance_capmin` | **DUDOSA** — ver §3; no la doy por buena. |
| 8 | `Sujeto_propuesto_originante_fiduciario` | `Sujeto_fiduciario_de_fideicomiso_financiero` | OK — clase del vocabulario (bajo `Sujeto_sujeto_regulado`); el binomio del 3.1 designa al fiduciario en rol de originante; subclase directa coherente. |
| 9 | `Sujeto_propuesto_personas_juridicas_beneficiarias_del_regimen_de_economia_del_conocimiento` | `Sujeto_beneficiario_economia_conocimiento` | OK — match léxico y semántico directo con la clase homónima del vocabulario (Exterior 3.18). |

Verificación de existencia de los 5 padres (todas las filas):
`python3 -c "import json; kg=json.load(open('data/experiment/grafo_v2/reensamblado_v3/kg.json')); ids={n['id'] for n in kg['nodes']}; print([p in ids for p in ['Sujeto_contraparte','Sujeto_entidad_financiera','Sujeto_rol_alcance_capmin','Sujeto_fiduciario_de_fideicomiso_financiero','Sujeto_beneficiario_economia_conocimiento']])"`
→ `[True, True, True, True, True]`.

## 3. La DUDOSA (fila 7) — motivos; el laudo fino es de la adjudicadora

`Sujeto_propuesto_originante_acreedor_inicial → Sujeto_rol_alcance_capmin`:

- **Motivo estructural:** `Sujeto_rol_alcance_capmin` NO es clase del
  vocabulario cerrado — es nivel `rol` en `esquema_v2_clases.json`
  ("Entidades alcanzadas (Capitales Mínimos)", `properties.nivel: "rol"`
  en el nodo del vigente). Las 57 `subclase_de` existentes conectan
  exclusivamente clases; los roles reciben `miembro_de` (convención
  verificada: 0 excepciones). Una `subclase_de` hacia un rol sería la
  primera ruptura de esa convención del esqueleto.
- **Motivo semántico:** en CapMin 3.1 el "originante/acreedor inicial" es
  un rol dentro de la operación de titulización (su única arista entrante:
  `aplica_a` desde "Experiencia del originante en financiaciones", Punto
  3.1 parte 8), no una subclase de "las entidades alcanzadas por CapMin".
  El binomio hermano (fila 8, `originante_fiduciario`) sí recibió una
  clase como padre.
- **Alternativas para el laudo** (no las aplico sin orden):
  `Sujeto_entidad_financiera` (si se lee que el originante del 3.1 es la
  entidad que origina los activos) o `Sujeto_contraparte` (si se lee como
  tercero cedente — cf. el nodo "cuando los activos hayan sido adquiridos
  a terceros, el originante…"). Es la misma cuestión de modelado que
  BKL-0020 (`Sujeto_propuesto_originante`, sin padre sugerido, fuera de
  esta unidad); conviene laudarlas de forma consistente.

## 4. Alcanzabilidad por navegación de `…grupo_2` — la posición de inserción DECIDE

Contrato real de la tool (cuarteto hasheado,
`data/experiment/evaluacion/harness.py:197`): `ver_vecinos` trunca a
**40 vecinos por dirección**, en el **orden de aparición de las aristas en
`kg['edges']`** (`in_edges`/`out_edges` se construyen por append en ese
orden, `harness.py:141-145`), y el schema expuesto a la API **no expone
`limite`** (`harness.py:271` ss.) — el agente siempre opera con la ventana
de 40.

`Sujeto_entidad_financiera` tiene **142 entrantes** en el vigente. Réplica
del contrato contra el kg aplicado en memoria (script
`sim_c4.py`, scratchpad de la sesión):

- **Apendeadas al final** (patrón de C1, que agregó sus 2 aristas en idx
  8044-8045): la arista de `…grupo_2` cae en posición ~144 de los
  entrantes → **TRUNCADA: NO navegable** desde su padre. Ídem grupo_1 y
  grupo_a.
- **Insertadas contiguas al bloque `subclase_de` del esqueleto** (tras el
  último `subclase_de`, hoy idx global 56; los 4 hijos actuales de
  `Sujeto_entidad_financiera` ocupan las posiciones 0-3 de sus entrantes):
  `…grupo_2` queda en **posición 6** de la ventana → **navegable**. Las 9
  quedan visibles desde su padre (grupo_1 pos 4, grupo_a pos 5, grupo_2
  pos 6; las de padres chicos — contraparte 14 entrantes, fiduciario 10,
  beneficiario 2 — visibles en cualquier posición; la de la DUDOSA pos 0
  incluso con los 686 entrantes de `rol_alcance_capmin`).

**Propuesta de aplicación:** insertar el bloque de aristas laudadas
inmediatamente después del último `subclase_de` existente (recalcular el
índice al aplicar), NO apendear. La inserción intermedia no altera ningún
otro objeto (verificado: el resto de la lista queda byte-idéntico, §6).

**Fragilidad (registrada al aplicar, por laudo):** la navegabilidad de
`…grupo_2` es dependiente del orden de la lista de aristas bajo la ventana
de 40 de `ver_vecinos` — cualquier futura inserción que empuje el bloque
fuera de la ventana la rompe en silencio. El fix durable pertenece a la
capa de retrieval (migración de backend, en cola del tablero §5). BKL-0022
queda vigente con esta nota (evento `nota` en el backlog, no cierre).

## 5. Decisiones de forma propuestas (requieren laudo junto con la tabla)

- **`rol_fuente` de las 9 aristas: `cuarentena_laudada`** (traza al origen
  real: sugerencia de cuarentena del reensamblado v3 + laudo humano).
  Nota para el laudo abierto de M7 (tablero §6): valor fuera del
  vocabulario de roles que M7 usa como numerador, misma situación ya
  flaggeada para `restauracion_manual` (C1); alternativa: reutilizar
  `restauracion_manual`. No lo decido yo.
- **Provenance por arista:** `{source_doc, location}` derivados del
  `chunk_ids` de `cuarentena.json`, con `location` en el formato canónico
  del cuerpo (`"Punto 2.11."`, `"Punto 3.1."`, `"Punto 3.17."`,
  `"Punto 3.18."`, `"Punto 4."`; el sufijo `__pN` del chunk_id es marca de
  split, se descarta). Con este formato el delta S5 del validador es 0
  (§6); con el chunk_id crudo como location, S5 sumaría +9.
- Estructura de cada arista idéntica a las existentes:
  `{source, target, relation: "subclase_de", provenance, provenances:
  [provenance], rol_fuente}`.

## 6. RE-TEST pre-especificado (corrido ya en simulación, USD 0)

Simulación completa en memoria + kg simulado en scratchpad
(`sim_c4.py`; el repo no se tocó). Resultado con las 9:

- **(a)** Las 9 aristas existen post con endpoints exactos (source, target,
  `subclase_de` según §2): **PASS**.
- **(b)** Cero otros cambios: nodos **4.459** intactos (lista
  byte-idéntica), aristas **8.046 → 8.055**, y el resto de la lista de
  aristas (quitando las 9 insertadas) byte-idéntico al pre: **PASS**.
- **(c)** `subclase_de` total **57 → 66** (pre+9): **PASS**.
- **(d)** Shapes (stdout capturado; `--out` SIEMPRE explícito al
  scratchpad, NUNCA el default → escribe en `reports/` sin autorización,
  incidente documentado en C3_retest): **desviación reportada, no
  silenciosa** — el delta estricto 0 es IMPOSIBLE para S1 tal como está la
  matriz v0: S1 no incluye `subclase_de` entre las relaciones válidas, por
  lo que las 82 aristas del esqueleto YA fallan S1 en el vigente y las 9
  nuevas se suman a esa misma clase de FAIL pre-existente (82 → 91,
  +9 exactos, 100 % atribuibles). La matriz-a-schema-v2 es unidad aparte
  ya en cola (tablero §5, ítem 2). **Criterio propuesto para el laudo:**
  (d') = "S1 +N exactos (N = aristas laudadas) y TODO el resto de shapes
  sin cambio". Verificado en simulación: S2 PASS, S3 violaciones 2121 =
  2121 (las 9 conformes a firma Sujeto→Sujeto), S4 PASS, S5 violaciones
  30 = 30, S6-S12 idénticos byte a byte. Con ese criterio: **PASS**.
- **(e)** `…grupo_2` navegable vía `ver_vecinos` desde
  `Sujeto_entidad_financiera` (réplica del contrato, ventana 40): posición
  6 de los entrantes → **PASS** (condicional a la inserción del §4; el
  contrafáctico apendeado FALLA este punto).

Si el laudo excluye la DUDOSA (entran 8): aristas 8.046 → **8.054**,
`subclase_de` 57 → **65**, S1 82 → **90**; (a), (b), (d'), (e) idénticos
con N=8. El re-test de Fase 2 se corre con el N laudado.

Reproduce la simulación:
`python3 <scratchpad>/sim_c4.py` (imprime (a)-(e) + contrafáctico) y
`python3 scripts/shapes_validator.py --kg <scratchpad>/kg_post_sim.json --out <scratchpad>/shapes_post.md`
vs `--kg data/experiment/grafo_v2/reensamblado_v3/kg.json --out <scratchpad>/shapes_pre.md`.

## 7. Bloque de propuesta (formato fijo)

```yaml
id_falla: "BKL-0019 (vara / expediente de retriage v3, candidata C) — 9 sujetos de cuarentena sin arista de jerarquía, alcanzables solo por léxico"
categoria_defecto: estructural_kg   # especie del backlog: alcanzabilidad (laudada en triage)
palanca: grafo/esquema
cambio_exacto: >
  Insertar en data/experiment/grafo_v2/reensamblado_v3/kg.json, en bloque
  contiguo inmediatamente después de la última arista subclase_de existente
  (hoy idx 56; recalcular al aplicar), las aristas laudadas de la tabla §2
  (9, u 8 si se excluye la DUDOSA de la fila 7), cada una con
  relation: "subclase_de", source/target verbatim de la tabla,
  provenance/provenances según §5 y rol_fuente según laudo de §5.
  Ningún nodo se crea, modifica ni borra; ninguna otra arista se toca.
cita_pdf: >
  El cambio no transcribe texto normativo nuevo: materializa la jerarquía
  ya laudada en triage sobre sujetos extraídos de los TOs. Anclas de los
  sujetos (chunk_ids de cuarentena.json): CapMin 2.11 (grupos 1 y 2),
  CapMin 3.1 parte 8 (inversor, inversores y tenedores, originante/acreedor
  inicial, originante/fiduciario), Exterior 3.17 (RADPIP/RADPIGN),
  Exterior 3.18 (economía del conocimiento), RegInf 4 (Grupo A).
como_se_verificaria: >
  RE-TEST pre-especificado §6: (a) aristas laudadas presentes con endpoints
  exactos; (b) cero otros cambios (4.459 nodos byte-idénticos; resto de
  aristas byte-idéntico; total 8.046 -> 8.046+N); (c) subclase_de 57 -> 57+N;
  (d') shapes: S1 +N exactos y atribuibles, resto de shapes byte-idéntico
  (stdout capturado, --out explícito fuera del repo); (e) …grupo_2 en la
  ventana de 40 de ver_vecinos desde Sujeto_entidad_financiera (réplica del
  contrato del harness sobre el kg aplicado).
categoria_riesgo: alto
justificacion_riesgo: >
  Creación de estructura nueva (aristas) — alto por criterio fijo del
  formato, sin excepción. Además: una fila DUDOSA (subclase_de hacia un
  nivel rol rompería la convención 57/57 del esqueleto), decisión de
  rol_fuente con implicancia en M7 (laudo abierto), y posición de
  inserción que decide la navegabilidad (§4). Todo va a laudo humano antes
  de aplicar; nada es automático.
```

## 8. Qué queda para la Fase 2 (post-laudo)

Aplicar SOLO las aristas laudadas (con el padre que fije el laudo para la
fila 7, si entra), re-test (a)-(e) con N laudado, eventos `aplicacion` +
`cambio_estado` al `data/backlog/backlog.jsonl` (patrón C3) y retest en
`data/backlog/retests/`. BKL-0022 se verifica en su propia entrada
post-aplicación (réplica del índice léxico + `ver_vecinos`), no acá.
