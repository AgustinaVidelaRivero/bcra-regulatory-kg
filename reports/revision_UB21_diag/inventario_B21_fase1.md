# Inventario para la regression suite — U-B2.1 fase 1 (re-diagnóstico), pieza a

Mandato: `docs/mandatos/UB21_fase1_rediagnostico.md` (firmado 2026-09-26, commit `610f655`).
Ejecutado el 2026-09-26 sobre HEAD `610f655`, costo de API 0, solo lectura del repo
salvo este directorio. Nada de la suite se implementa acá.

## 0. Insumos verificados (sha256, `shasum -a 256`)

| Insumo | Path | sha256 medido | Declarado (mandato) |
|---|---|---|---|
| backlog | `data/backlog/backlog.jsonl` | `d8473501b442432ec7b2f698cbb4d2d618e3db1f0947698407b311ac1a07e2a4` | `d8473501…` OK |
| tests r1 | `data/experiment/reextraccion_v2/corpus_v2/r1_tests.py` | `fe1c747652820ac9341851f2fb95ce2b4e3100125f6aacbdfe5e0204405dd2c2` | `fe1c7476…` OK |
| invariantes | `data/experiment/reextraccion_v2/corpus_v2/r1_invariantes.py` | `771231420d7fd3eaa6056ae1c910a1f94cf7055eb5042320a1b0aba6734f29e0` | `77123142…` OK |
| E4 | `data/experiment/reextraccion_v2/corpus_v2/r1_e4.py` | `179db09c2e87dd733f609a626033fdcf3727a75b32cf70dcd645c5fb13bedd64` | `179db09c…` OK |
| KG-Base | `data/experiment/run_3_ppf_core/kg.json` | `12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410` | `12c226e2…` OK |
| KG-Refinado | `data/experiment/grafo_v2/reensamblado_v3/kg.json` | `26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571` | `26fac8b4…` OK |
| KG-Reextraído | `data/experiment/reextraccion_v2/corpus_v2/salida/kg.json` | `8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581` | `8e2eadee…` OK |
| KG-Reextraído-r1 | `data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json` | `0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a` | `0226e947…` OK |

Otros insumos leídos (sha256 medido en esta unidad): retriever in-memory
`data/experiment/evaluacion/harness.py` `fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e`;
`data/experiment/evaluacion/loader.py` `5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b`;
`scripts/shapes_validator.py` `972cefa37cd1c2e3c6a10d27c1416e732a765e631ed86190a151223ba1e2e28c`
(commit `f4c8e93`, perfil congelado S19–S23); muestra de T5
`data/experiment/reextraccion_v2/corpus_v2/salida_r1/referencias_muestra30_inspeccionada_A2.json`
`4dbc2d306df867dedc4464c54b56bf6f7224ee6d820577ffe83141b6cbba8da4`; catálogo v2
`data/experiment/grafo_v2/esquema_v2_clases.json` `2672af5216e095bee2a4888e18d85930d7b0149263b87763daacc5fd21814d4d`
(65 clases + 5 roles, 18 clases con alias).

Fila B2.1 del plan: `git show HEAD:docs/plan_tesis.md | grep -n "^- \[~\] B2.1 (I"` → `:324`
(HEAD); en el árbol de trabajo está en `:326` porque `docs/plan_tesis.md` tiene una
modificación local preexistente de +2 líneas (`git diff --stat docs/plan_tesis.md`
→ `6 ++++--`), ajena a esta unidad. El ancla es el id de la fila.

## 1. Criterios de esta unidad (declarados antes de clasificar)

**Formas de test admitidas** (mandato, decisión 3): (F1) nodo presente/ausente,
(F2) ancla (punto de provenance) presente, (F3) valor de propiedad, (F4) arista
presente/ausente, (F5) rank en `buscar_nodos` (depende del retriever).

**Direccionamiento sin id.** Toda fila se direcciona por (archivo del TO, punto ∈
CONJUNTO de provenances, tipo, cadena normalizada en label o properties) o por id
de catálogo de Sujetos (`Sujeto_<slug>` de `esquema_v2_clases.json`, estable
entre generaciones). Nunca por `provenance[0]` solo ni por id de nodo de
contenido: los ids de contenido derivan del slug de la descripción y cambian
entre generaciones (medido: de los 7 ids de C1–C7 solo `…_e1946e` (C1) sobrevive
en gen 3; el sufijo `_5f95b9` de C6 reaparece en gen 3 con tipo `Obligacion`,
`sonda_anclas_C1_C7_UB21_salida.txt`, filas `C6.id_5f95b9`).

**Adaptador de provenance.** Gen 1 (KG-Base) y gen 2 (KG-Refinado) llevan
`{source_doc, location}` con el punto dentro de `location` («Punto 1.2. …»); gen 3
lleva `{to, archivo, punto, rol_documental}` (r1 agrega `chunk_id, paginas,
ancestros`). Formatos medidos en `sonda_anclas_C1_C7_UB21_salida.txt` («formato
de provenance detectado») y en la exploración de la sesión. **Se cuenta como
infraestructura de la suite, no como condición de la fila**, porque la fila B2.1
del plan ya asienta la decisión (2) de la fase 2 (adaptador dentro de la suite) y
porque sin él ninguna fila anclada correría sobre gen 1/2. Donde un test TAL COMO
ESTÁ ESCRITO falla por formato, se dice en la fila.

**Convertibilidad.**
- `convertible`: tiene una o más formas F1–F5 y su objeto se direcciona con lo
  anterior; el valor esperado es el único dato que la suite necesita sellar.
- `con condición`: además necesita algo que hoy no está en el repo o no es un
  kg.json: una fixture (grafo de referencia, snapshot, lista de archivos), un
  catálogo parametrizado, una política por generación, o consultas que la
  evidencia de cierre no registró (no se re-derivan).
- `no convertible`: lo que se afirma no es observable con F1–F5 sobre un kg.json.
- Sub-comprobaciones «byte-idéntico a HEAD/pre» de los retests son controles de
  aplicación contra un snapshot, no una forma F1–F5: se declaran «fuera de forma»
  y no cuentan ni como condición ni como conversión.

**Depende del retriever** = alguna comprobación que SOSTIENE el PASS del cierre es
un rank en `buscar_nodos` o una posición en `ver_vecinos`. Un rank registrado como
informativo sin criterio de corte (C2 paso 5) no cuenta.

**Retriever de referencia.** `GraphIndex` de `data/experiment/evaluacion/harness.py`
(`harness.py:130-176`): tokens `[a-z0-9]+` sin acentos sobre `label + id`, score =
tokens en común, orden `(-score, len(label), id)`, `limite` con tope 50
(`:159`); `ver_vecinos` ventana 40 por dirección en orden de lista (`:197-236`).
Carga: `loader.load_graph_from_path(path, adapter_key=None)` (`loader.py:325`);
el loader normaliza provenance a `{source_doc, location}` (`loader.py:132-140`),
lo que deja vacías las provenances de gen 3 en su vista, sin efecto sobre ranks
ni vecinos. Ningún rank de esta unidad usa Neo4j.

## 2. Inventario (una fila por ítem; 46 filas)

Columnas: **Afirma** (una oración) · **Grafo** donde se verificó (sha256 registrado
en la evidencia) · **Evidencia** del cierre · **Cambió** (pipeline o grafo) ·
**Forma** (F1–F5) · **Conv.** (convertibilidad) · **Retr.** (depende del retriever) ·
**Condición / direccionamiento** (para `con condición`: qué necesita; para todas:
cómo se direcciona y si tiene sentido sobre un grafo que no pasó por r1) ·
**Medido en esta unidad** (sondas; grafos en orden KG-Base / KG-Refinado /
KG-Reextraído / r1).

### 2.i Grupo (i) — BKL cerrados (12) y preguntas RT (12)

| Id | Afirma | Grafo (sha) | Evidencia | Cambió | Forma | Conv. | Retr. | Condición / direccionamiento | Medido |
|---|---|---|---|---|---|---|---|---|---|
| BKL-0017 (C1) | El criterio general 1.1 de Clasificación existe como `Obligacion` con descripción verbatim del PDF, provenance Sección 1 / punto 1.1, y 2 aristas (`establecida_en` → TextoOrdenado cla; `aplica_a` → `Sujeto_rol_obligado_a_clasificar_clasificacion`). | KG-Refinado post-C1 `b23e8ad4…` (`C1_retest_2026-07-31.md:30-31`); hoy `26fac8b4` | `data/backlog/retests/C1_retest_2026-07-31.md:33-44` (4/4 PASS); backlog líneas 39-41 | Grafo editado in-place: 1 nodo + 2 aristas `rol_fuente: restauracion_manual`, commit `af75f70`; pipeline sin cambio | F1 + F4 + F5 (3 consultas, ranks 1/1/3, `:42-44`) | convertible | sí | (TO_clasificacion, 1.1, Obligacion, descripción empieza «Los clientes de la entidad (tanto residentes en el país»). Sentido sin r1: sí, mide si el pipeline extrae el 1.1. | anclas: FAIL / PASS / PASS / PASS (gen 3 lo extrae con el mismo id); ranks KG-Refinado 1/1/3 coinciden; gen 3: —/—/2 |
| BKL-0006 (C2) | La correspondencia entidad-monto del 1.2 de CapMin es la de la tabla del PDF (Bancos 5.000 sin paréntesis; Restantes 2.500 con «salvo Cajas…»), la `Excepcion` de cajas apunta a Restantes y los tres ids viejos no tienen referencias. | KG-Refinado post-C2 `ddf7ff8a…` (`C2_retest:49`) | `C2_retest_2026-07-31.md:51-58` ((1)-(4) PASS; (5) ranks informativos `:61-63`); backlog 43-45 | Grafo: 3 nodos renombrados (opción A) + 7 aristas remapeadas, commit `a2e3bb8` | F3 (montos/`umbral`) + F4 (`exceptua` → restantes) + F1 (ids viejos ausentes) + F5 informativo | convertible | no (paso 5 «informativo, sin criterio de corte» `:59`) | (TO_capitales, 1.2, Restriccion, «exigencia básica» + «bancos» / «restantes entidades»); Excepcion por (cap, 1.2, Excepcion, «cajas de crédito cooperativas»). Sentido sin r1: sí, es la regresión RX-10 del pipeline. | anclas: PASS / PASS / **FAIL(invertido)** / **FAIL(invertido)** (gen 3: bancos `umbral` 2.500, restantes 5.000; coincide con la nota (1) de la fila B2.1 del plan); ranks KG-Refinado 1/3/4 y 1/2/13 coinciden |
| BKL-0023 (C3) | `properties.umbral` del nodo de compañías financieras con comercio exterior (cap 1.2) vale «5.000 millones de pesos»; descripción e id intactos. | KG-Refinado post-C3 `d673dd72…` (`C3_retest:28`) | `C3_retest_2026-08-02.md:30-37` ((a)-(d) 4/4); backlog 49-51 | Grafo: 1 propiedad, commit `c51b96a` | F3 | convertible | no | (TO_capitales, 1.2, Restriccion, descripción contiene «compañías financieras que realicen, en forma directa, operaciones de comercio exterior»). Regla explícita: sin nodo o sin `umbral` → no aplicable, nunca PASS vacuo. Sentido sin r1: solo si el pipeline emite `umbral`. | anclas: N/A(sin nodo) / PASS / N/A(sin nodo) / N/A(sin nodo): en gen 3 ninguna Restriccion anclada en 1.2 porta esa oración |
| BKL-0019 (C4) | Ocho sujetos propuestos de cuarentena tienen arista `subclase_de` hacia su padre laudado (`rol_fuente: cuarentena_laudada`), la DUDOSA (`…originante_acreedor_inicial`) no la tiene, y `…grupo_2` es navegable desde `Sujeto_entidad_financiera` en la ventana de 40 de `ver_vecinos` (posición 6 de 145). | KG-Refinado post-C4 `0161be69…` (`C4_retest:44`) | `C4_retest_2026-08-02.md:52-58` ((a)-(e) 5/5); backlog 52-54 | Grafo: 8 aristas en bloque contiguo idx 57-64, commit `2c71e3f` | F4 ×8 + F4 ausente (excluida) + posición en `ver_vecinos` (F5) | con condición | sí ((e) sostiene el PASS) | Necesita: política de cuarentena por generación (gen 2 «laudada»: `subclase_de`; gen 3 «flaggeada»: `padre_sugerido`, que T7 exige y que prohíbe `subclase_de` desde propuesto) y fixture de las 8 (label del sujeto, padre): los ids `Sujeto_propuesto_*` derivan del label y no son de catálogo (gen 3: 4/8 presentes por label, 3/8 con `padre_sugerido` en r1). La forma «posición en ventana» se reduce a arista presente. Sentido sin r1: sí, con política flaggeada. | anclas: FAIL / PASS (8/8, excluida sin `subclase_de`) / FAIL / FAIL; ranks: `ver_vecinos` KG-Refinado posición 6 de 145 coincide; gen 3: hijo ausente. **Contradicción 1 con T7** (ver T7). |
| BKL-0004 (C5) | La enumeración del 6.5 de Clasificación existe como 9 nodos (enumerador `Obligacion` + 8 `Operacion` de niveles y situaciones) con descripciones verbatim y 17 aristas (9 `establecida_en`, 8 `regula`); los 39 nodos del 7.2 no cambian. | KG-Refinado post-C5 `04a50081…` (`C5_retest:50`) | `C5_retest_2026-08-02.md:56-66` (32/32); backlog 60-61; corrida real RT-C5 5/5 (ver RT) | Grafo: 9 nodos + 17 aristas `restauracion_manual`, commit `d9e7e9b` | F1 ×9 + F4 ×17 + F5 (7 consultas `E4_enumeracion_65.md:281-289`) | convertible | sí ((c) 7/7 sostiene el PASS) | (TO_clasificacion, 6.5 / 6.5.1 / 6.5.2 / 6.5.2.1 / 6.5.2.2 / 6.5.2.3 / 6.5.3 / 6.5.4 / 6.5.5, frase del título o del encabezado). «39 nodos byte-idénticos» fuera de forma. Sentido sin r1: sí. | anclas: FAIL / PASS (9/9, 8 `regula` + 9 `establecida_en`) / FAIL (5/9) / FAIL (5/9: N3, N5, N6, N7 sin nodo anclado con la frase; N9 con 6 nodos); ranks KG-Refinado 7/7 consultas coinciden; gen 3: objetivos ausentes o fuera del top-10 |
| BKL-0003 (C6) | La salvedad del 1.1.2.5 de Protección existe como `Excepcion` con descripción verbatim, label C_mixta y `nota_fuente`, con 2 aristas (`establecida_en`; `exceptua_obligacion` → Obligacion del 1.3), sin aristas a Sujeto, y con rank 1 en las consultas falladas. | KG-Refinado post-C6 `fe5f6b69…` (`C6_retest:46`) | `C6_retest_2026-08-03.md:52-62` (38/38) y deslinde `:73-113`; backlog 62-63 y 66 | Grafo: 1 nodo + 2 aristas, commit `756d6ec` | F1 + F4 ×2 + F4 ausente (a Sujeto) + F5 (11 consultas `E3_salvedad_mutuales.md:288-298`) | convertible | sí ((c) 14/14 sostiene el PASS) | (TO_proteccion, 1.1.2.5, Excepcion, «mutuales o cooperativas»). Sentido sin r1: sí. | anclas: FAIL / PASS / PASS-parcial / PASS-parcial (gen 3 tiene la Excepcion extraída por el pipeline, id y label distintos, pero sin `establecida_en`: `C6.aristas` FAIL); ranks KG-Refinado 11/11 coinciden (N1, rol y PNFC) |
| BKL-0005 (C7) | La descripción del nodo del 7.1 de RegInf contiene los dos calificadores («Responsabilidad Patrimonial Computable informada en el mes n»; «Franquicia … calculada según datos del mes n»), nada más cambia, y el portador tiene rank 1 en 3 consultas. | KG-Refinado post-C7 `26fac8b4…` = KG-Refinado actual (`C7_retest:64`) | `C7_retest_2026-08-03.md:67-78` (27/27); backlog 64-65 | Grafo: 1 propiedad, commit `05984e1` | F3 + F5 (3 consultas `:78`) | convertible | sí ((d) sostiene el PASS) | (TO_regimen_informativo, 7.1, Obligacion, «para el cálculo del importe correspondiente al mes n»). Sentido sin r1: sí, mide si el pipeline amputa. | anclas: N/A(sin portador) / PASS / PASS / PASS (gen 3 extrae los dos calificadores); ranks KG-Refinado 1/1/1 coinciden; gen 3: 1/6/1 y 1/7/1 |
| BKL-0007 | La falla EV1-015 (alcanzabilidad, tras v3 ausencia) queda cerrada por referencia porque C1 restauró el material que la definía. | = C1 | backlog líneas 42 y 46 («cerrada por referencia … verificación = re-test C1 contra PDF»; laudo de la adjudicadora); `C1_retest` | Ninguno propio | La de BKL-0017 | convertible | no (propio) | Sin test propio: dedupe con BKL-0017 (mismo objeto). | = C1 |
| BKL-0026 | Defecto de capa generación del agente: paráfrasis invertida del verbatim con `ver_nodo` byte-idéntico (RT-C6-1 vs RT-C6-2), sistemático 3/3 en N=3. | KG-Refinado (corrida `rt_c5_c6`, `graph_fingerprint` `91573e01c7135581`, 2026-08-04; `rt_c6_n3_r1..3`) | backlog 67-68 y 71; `C6_retest:99-103`; `docs/resultado_piloto_singold_u6.md` (referencia del evento) | Ninguno (`aplicado_en: null`; especie `alucinacion_agente`) | ninguna F1–F5 | no convertible | no | Conducta del agente: no es observable con una comprobación determinística sobre un kg.json. El nodo objetivo sí se testea (= C6). | — |
| BKL-0027 | Defecto de navegación del agente: pidió `ver_vecinos` salientes de un rol que solo tiene `miembro_de` entrantes y declaró la pregunta no respondible (RT-C6-3). | KG-Refinado (misma corrida) | backlog 69-70; `C6_retest:104-108` | Ninguno (`aplicado_en: null`; especie `navegación`) | ninguna F1–F5 | no convertible | no | Conducta del agente. La estructura subyacente (rol con 7 `miembro_de` entrantes y 0 salientes) es F4, pero no es el defecto; está cubierta en RT-C6-3. | — |
| BKL-0028 | Tres ids del catálogo v3 (`Sujeto_entidad_financiera`, `Sujeto_banco`, `Sujeto_entidad_cambiaria`) llevan definición doméstica y alias «del exterior»; el remedio es abrir ids separados. | catálogo v3: `data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py` (BLOQUE_CATALOGO_V3, sellado) | backlog línea 73 (`condicion_de_cierre`: el barrido de `data/experiment/esq_v3_miembros/code/` debe devolver cero) | Ninguno (remedio pendiente; exige re-sello del prefijo v3) | F1 (ids nuevos «del exterior» presentes; ids domésticos sin alias del exterior) sobre el catálogo, no sobre el grafo | con condición | no | Necesita: catálogo v3 parametrizado (`data/experiment/esq_v3_miembros/esquema_v3_clases.json`) y un grafo extraído con ese catálogo (perfil `v3_b54`): hoy ninguno en el repo (fila B2.2 del plan, fe de erratas 3). Sobre los cuatro grafos: no aplicable. Sentido sin r1: solo sobre tanda ≥ 1. | — (no sondeable en los cuatro grafos) |
| BKL-0029 | El colectivo «titulares de cuenta corriente en el BCRA» no tiene id en el catálogo v3; `Sujeto_rol_alcance_convca` quedó adjudicado por aproximación a `Sujeto_entidad_financiera`. | catálogo v3 (ídem) | backlog línea 74 (`condicion_de_cierre`: el rol tiene como miembro el id nuevo y su `residuo_declarado` pierde `colectivo_operativo_sin_id`) | Ninguno | F4 (`miembro_de` del rol de convca → id nuevo) | con condición | no | Ídem BKL-0028; además convca no es uno de los 5 TOs del subset (`data/experiment/subset/`): no aplicable en los cuatro grafos ni en la tanda de desarrollo. | — |
| RT-C5-1 | «¿En cuántas categorías debe incluirse cada cliente de la cartera comercial según el 6.5 y cómo se denomina cada una?» — gold (cinco; los cinco nombres) presente en el portador N1 y N1 alcanzable en top-10. | KG-Refinado post-C5; corrida real sobre `reensamblado_v3` (`rt_c5_c6`, 2026-08-04) | pregunta `E4_enumeracion_65.md:227-230`; `C5_retest:66` ((d) 5/5); traza `data/experiment/evaluacion/posthoc_run/traces/rt_c5_c6/reensamblado_v3/RT-C5-1.json` (`judge.verdict.correctitud` = correcta) | C5 | F3 (enumeración/label de N1 contiene las 5 categorías) + F5 | con condición | sí | Consulta del proxy NO ENCONTRADA: `grep -n "RT-[1-5]" data/backlog/retests/C5_retest_2026-08-02.md` → `:66,:68-74` sin texto de consulta salvo la de RT-4. No se re-deriva (fila B2.1 del plan, decisión (5)): entra solo como test de valor. Direccionamiento = N1 de C5. | valor: presente en KG-Refinado (N1 PASS); gen 3: N1 anclado en 6.5 existe pero sin la enumeración de C5 |
| RT-C5-2 | «¿Qué situaciones comprende la categoría 'con seguimiento especial'?» — gold (en observación; en negociación o con acuerdos de refinanciación; en tratamiento especial) presente en N3 y N3 alcanzable. | ídem | `E4_enumeracion_65.md:231-234`; `C5_retest:66`; traza `RT-C5-2.json` (correcta) | C5 | F3 + F5 | con condición | sí | Consulta NO ENCONTRADA (mismo grep). Direccionamiento = N3 de C5. | valor: KG-Refinado PASS; gen 3: N3 ausente |
| RT-C5-3 | «¿Dentro de qué plazo debe manifestarse la intención de refinanciar…?» — gold («antes de los 60 días … desde la mora») presente en N5 y N5 alcanzable. | ídem | `E4_enumeracion_65.md:235-238`; `C5_retest:66`; traza `RT-C5-3.json` (correcta) | C5 | F3 + F5 | con condición | sí | Consulta NO ENCONTRADA. Direccionamiento = N5. | valor: KG-Refinado PASS; gen 3: N5 ausente |
| RT-C5-4 | «¿Bajo qué condiciones y cuántas veces puede reclasificarse … 'en tratamiento especial'?» — gold («primera vez dentro del año calendario, cancelada la primera cuota; por única vez») presente en N6 y N6 alcanzable (consulta mínima, rank 4). | ídem | `E4_enumeracion_65.md:239-242`; `C5_retest:66` y observación `:68-74` (consulta «reclasificación en tratamiento especial refinanciación» → rank 4); traza `RT-C5-4.json` (correcta) | C5 | F3 + F5 (consulta proxy registrada) | convertible | sí | Direccionamiento = N6. Sentido sin r1: sí. | ranks: KG-Refinado rank 4 coincide; gen 3: objetivo ausente |
| RT-C5-5 | «¿El nivel 'Riesgo medio' pertenece a la clasificación de la cartera comercial?» — gold: no, es del 7.2; el nodo de riesgo medio sigue anclado en 7.2 y N1 no importa niveles del 7.2. | ídem | `E4_enumeracion_65.md:243-247`; `C5_retest:66` ((d): 39 nodos del 7.2 byte-idénticos, `…riesgo_medio_61a12e` intacto con provenance 7.2, N1 sin niveles del 7.2); traza `RT-C5-5.json` (correcta) | C5 | F2 (nodo con «riesgo medio» anclado en cla 7.2) + F3 (N1 sin «riesgo medio/bajo/alto») | convertible | no | «39 nodos byte-idénticos» fuera de forma. Direccionamiento: (TO_clasificacion, 7.2 exacto, cualquier tipo, «riesgo medio»). Sentido sin r1: sí. | anclas `C5.7_2_riesgo_medio` PASS / PASS (39 en 7.2, 3 con riesgo medio) / FAIL (0 nodos con punto exacto 7.2) / FAIL; `C5.N1_sin_niveles_7_2` N/A / PASS / PASS / PASS |
| RT-C6-1 | «Según el 1.1.2.5, ¿qué sujetos quedan exceptuados … y respecto de qué operaciones?» — gold (mutuales o cooperativas, por las financiaciones que otorguen) presente en N1 y N1 en top-10 (rank 1). | KG-Refinado post-C6; corrida real `rt_c5_c6` (incorrecta) y N=3 `rt_c6_n3_r1..3` (incorrecta 3/3) | `E3_salvedad_mutuales.md:151-156`; `C6_retest:62` ((d) RT-1 rank 1); traza `RT-C6-1.json` (incorrecta); backlog 66 y 71 | C6 (capa KG); residuo → BKL-0026 | F3 (descripción verbatim en N1) + F5 | con condición | sí | Consulta del proxy NO ENCONTRADA (`grep -n "RT-[1-4]" data/backlog/retests/C6_retest_2026-08-03.md` → `:62,:69` sin texto); las 11 consultas de la propuesta sí están y se miden en la fila de BKL-0003. Entra solo como test de valor. | valor: N1 PASS en KG-Refinado y gen 3 (descripción verbatim en la Excepcion extraída) |
| RT-C6-2 | «Una cooperativa alcanzada por las normas de PNFC, ¿reviste el carácter de sujeto obligado…?» — gold: no; presente en N1; rank 1. | ídem | `E3_salvedad_mutuales.md:157-164`; `C6_retest:62` (RT-2 rank 1); traza `RT-C6-2.json` (correcta) | C6 | F3 + F5 | con condición | sí | Consulta NO ENCONTRADA. Direccionamiento = N1 de C6. | = RT-C6-1 |
| RT-C6-3 | «¿Qué sujetos enumera el 1.1.2 como sujetos obligados…?» — el rol `Sujeto_rol_sujeto_obligado_proteccion` sigue con sus 7 `miembro_de` entrantes y alcanzable (rank 7). | ídem (corrida real: parcial → BKL-0027) | `E3_salvedad_mutuales.md:165-174`; `C6_retest:62` (RT-3: rol byte-idéntico, 7 `miembro_de`, rank 7); traza `RT-C6-3.json` (parcial) | C6 (no-regresión) | F4 ×7 (ids de catálogo) + F5 | con condición | sí | Consulta NO ENCONTRADA (rank 7 sin texto). El conteo 7 depende del esqueleto v2 (catálogo parametrizado: `roles[0].miembros` de `esquema_v2_clases.json`). «Byte-idéntico» fuera de forma. Sentido sin r1: solo sobre grafos con esqueleto (r1 sí; KG-Reextraído no). | anclas `C6.rol_7_miembro_de`: N/A(rol ausente) / PASS / FAIL (0: sin esqueleto) / PASS |
| RT-C6-4 | «¿Una empresa no financiera emisora de tarjetas es sujeto obligado…?» — gold: sí; el nodo de emisoras sigue `miembro_de` del rol y N1 no tiene aristas hacia/desde sujetos. | ídem (corrida real: correcta) | `E3_salvedad_mutuales.md:175-179`; `C6_retest:62` (RT-4); traza `RT-C6-4.json` (correcta) | C6 (no-regresión) | F4 (`Sujeto_empresa_no_financiera_emisora_de_tarjetas --miembro_de--> rol`, ids de catálogo) + F4 ausente (N1 ↔ Sujeto) | convertible | no | «Byte-idéntico» fuera de forma. Sentido sin r1: la arista exige esqueleto; la ausencia no. | anclas: N/A / PASS / FAIL (sin `miembro_de`) / PASS; `C6.N1_sin_aristas_a_Sujeto` N/A / PASS / PASS / PASS |
| RT-C7-1 | Consulta «esquema cálculo importe mes n disminución exigencia franquicia» → el portador del 7.1 con los calificadores tiene rank 1 y `ver_nodo` devuelve la descripción corregida. | KG-Refinado post-C7 (`26fac8b4`) | `C7_retest:78` ((d) 7/7). Corrida real con agente+juez: **NO ENCONTRADA** (`grep -rln "RT-C7" --exclude-dir=.git .` → solo `docs/plan_tesis.md` y el mandato; `ls data/experiment/evaluacion/posthoc_run/traces/rt_c5_c6/reensamblado_v3/` → solo RT-C5-*/RT-C6-*); `C7_retest:90-92` la deja pendiente | C7 | F3 (= C7) + F5 | convertible | sí | Direccionamiento = portador de C7. Sentido sin r1: sí. | ranks: 1 / 1 / 1 en KG-Refinado (coincide), 1 en gen 3 |
| RT-C7-2 | Consulta «responsabilidad patrimonial computable cálculo importe correspondiente al mes» → rank 1. | ídem | `C7_retest:78`; corrida real NO ENCONTRADA (ídem) | C7 | F3 + F5 | convertible | sí | ídem | rank 1 KG-Refinado (coincide); 6 KG-Reextraído; 7 r1 |
| RT-C7-3 | Consulta «franquicia importe correspondiente al mes n cálculo esquema» → rank 1. | ídem | `C7_retest:78`; corrida real NO ENCONTRADA | C7 | F3 + F5 | convertible | sí | ídem | rank 1 en los tres grafos con portador |

### 2.ii Grupo (ii) — tests T1–T7 de r1 e invariantes I1–I5 (12)

| Id | Afirma | Grafo (sha) | Evidencia | Cambió | Forma | Conv. | Retr. | Condición / direccionamiento | Medido |
|---|---|---|---|---|---|---|---|---|---|
| T1 | El punto 3.9 (y 3.9.x) de Exterior tiene nodos de contenido y alguno menciona «200» (tope USD 200; caso BKL-0024). `r1_tests.py:3-4`; código `ensamblar_corpus.py:237-249`. | r1 `0226e947` (21 anclados) y KG-Reextraído `8e2eadee` (16) | `salida_r1/tests_respuesta_conocida_r1.json` y `salida/tests_respuesta_conocida.json` (pass true); `reporte_ensamblado_r1.json` «tests»; recomputados idénticos por `sonda_T1_T7_cuatro_grafos_UB21_salida.txt` | Pipeline gen 3 (E0–E3 con Enmienda 01, commit `5273c0c`) extrae el 3.9; r1 lo hereda | F2 + F3 | convertible | no | Tal como está escrito lee `provenances[].archivo/punto` (gen 3): sobre gen 1/2 falla por formato (0 anclados), aunque el adaptador encuentra 24 nodos anclados en ext 3.9* y 1 con «200» en KG-Refinado (`X.BKL-0024`). Sentido sin r1: sí. Solapa BKL-0024 (triaged). | T1: FAIL / FAIL / PASS / PASS |
| T2 | Las variantes casi idénticas del tope «125 %» de Exterior son ≥ 5 nodos separados con ≥ 4 puntos distintos (caso rector anti-fusión U6-008). `r1_tests.py:4`; `ensamblar_corpus.py:251-265`. | ídem | ídem | ídem | F1 (conteo) + F2 (conteo de puntos) | convertible | no | Mismo formato gen 3 (`p.get("to") == "ext"`): falla por formato en gen 1/2. Sentido sin r1: sí. | T2: FAIL / FAIL / PASS (5 nodos, 4 puntos) / PASS (6, 5) |
| T3 | Protección 1.1.2.5 tiene un nodo con «mutual» o «cooperativ» (la salvedad). `r1_tests.py:5`; `ensamblar_corpus.py:267-280`. | ídem | ídem | ídem | F2 + F3 | convertible | no | Mismo formato gen 3. Solapa C6/BKL-0003 (misma ancla; T3 acepta cualquier tipo, C6 exige Excepcion + aristas). Sentido sin r1: sí. | T3: FAIL / FAIL / PASS / PASS |
| T4 | Los 70 nodos y las 82 triplas `rol_fuente = esqueleto` de KG-Refinado están en el grafo, y el grafo tiene exactamente 82 aristas de relaciones de esqueleto. `r1_tests.py:6-7,30-42`. | r1 `0226e947` | `tests_respuesta_conocida_r1.json` (T4 pass, 82) | r1: E5 esqueleto (`ensamblar_r1.py`, commit `185e042`) | F1 + F4 (paridad) | con condición | no | Necesita: grafo de referencia como fixture (hoy `r1_comun.KG_REFINADO`, `r1_comun.py:33`) y parametrizar el 82 (`r1_tests.py:40`). **HALLAZGO:** sobre KG-Refinado mismo T4 FAIL: cuenta 90 aristas de relaciones de esqueleto (82 + las 8 `subclase_de` de C4, `rol_fuente: cuarentena_laudada`) porque en el grafo bajo prueba filtra por relación y no por `rol_fuente` (`:35-36`). Sentido sin r1: solo grafos con esqueleto v2. Solapa S15. | T4: FAIL (70 faltan) / FAIL (90 ≠ 82) / FAIL (20 faltan, 0 aristas) / PASS |
| T5 | Las 30 aristas `referencia` de la muestra sellada del freno A2 existen con la misma evidencia verbatim. `r1_tests.py:8-9,44-54`; muestra `salida_r1/referencias_muestra30_inspeccionada_A2.json` (`4dbc2d30…`). | r1 | `tests_respuesta_conocida_r1.json` (T5 pass 30/30) | r1: referencias nodo→nodo (`r1_referencias.py`, `185e042`) | F4 + F3 (`properties.evidencia`) | con condición | no | Necesita: fixture con direccionamiento por (ancla origen `source_ancla`, ancla destino `target_ancla`, `evidencia_verbatim`) en vez de `source`/`target` (ids de nodo de r1). Sentido sin r1: solo grafos con `rol_fuente: referencia_cruzada`; en los otros tres 30/30 ausentes. Solapa S21. | T5: FAIL (30 ausentes) / FAIL / FAIL / PASS |
| T6 | Hay exactamente 5 `TextoOrdenado`, uno por TO, con id `TextoOrdenado_<slugify_full(archivo)>` y archivo leído de E0. `r1_tests.py:10,56-61`. | r1 | `tests_respuesta_conocida_r1.json` (T6 pass) | r1: E4-b canonización (`r1_e4.py:213-250`) | F1 | con condición | no | Necesita: fixture de los 5 archivos (hoy `r1_comun.archivo_de_to` lee `e0_chunking/salida_enm01/chunks_<to>.json`, `r1_comun.py:138-140`) y `e2_lib.slugify_full` importado (`e2_reduce/e2_lib.py:90`). Pasa tal cual sobre gen 1/2 (mismos ids). Es el test de E4-b; solapa S6. | T6: PASS / PASS / FAIL (6: espurio `…normas_sobre_capitales_minimos…`) / PASS |
| T7 | Todo Sujeto propuesto tiene `nivel = propuesto` y `cuarentena == "true"`, ninguno usa id de catálogo; toda arista `padre_sugerido` apunta al catálogo; ningún `subclase_de` sale de un propuesto; ningún Sujeto fuera del catálogo que no sea propuesto. `r1_tests.py:11-14,63-82`. | r1 (41 propuestos, 41 `padre_sugerido`) | `tests_respuesta_conocida_r1.json` (T7 pass) | r1: E4-a + E5 (`padre_sugerido` flaggeado, `ensamblar_r1.py`) | F3 + F4 + F4 ausente | con condición | no | Necesita: catálogo parametrizado (`schema.SUJETOS_CATALOGO_SET` desde `esquema_v2_clases.json`, `grafo_v2/code/schema.py:86-97`) y política de cuarentena por generación. **Contradicción 1 (coincide):** sobre KG-Refinado T7 FAIL con 19 malos = 8 «subclase_de desde propuesto» (las aristas laudadas de C4) + 11 «sin cuarentena=true» (matiz nuevo: gen 2 guarda `cuarentena` como booleano `True`; `r1_tests.py:68` compara con la string `"true"`). Sentido sin r1: sí, con política por generación. Solapa S19, S22, S23, E4-a7. | T7: PASS (vacuo: 0 Sujetos) / FAIL (19 malos) / PASS (43 propuestos, 0 `padre_sugerido`) / PASS (41/41) |
| I1 | Conservación de nodos: Σ nodos pre-merge − merges = nodos finales. `r1_invariantes.py:7,62-68`. | r1 (cadena de merge) | `reporte_ensamblado_r1.json` «invariantes_final» (`ok: true`); selftest `r1_invariantes.py:171-222` | r1: guarda de merge cross-TO (`merge_grafos_guardado`, `:113-160`) | ninguna sobre un kg.json solo | no convertible | no | Exige los grafos pre-merge (`salida/<to>/grafo_<to>.json`) y los conteos de merge: solo existen para la cadena r1. | I1: N/A en los 4 (omitida por `grafos_pre=None`) |
| I2 | Conservación de aristas: Σ aristas pre-merge − merges = aristas finales. `:8,69-70`. | ídem | ídem | ídem | ninguna | no convertible | no | Ídem I1. | N/A |
| I3 | Unicidad de ids de nodo y de triplas (source, relation, target). `:9,72-77`. | r1 | ídem | — | F1 (conteo) | convertible | no | Sin condición. Solapa: ninguna shape (S7 es unicidad por (type, label), `shapes_validator.py:402`); `loader.py:180` `_merge_nodes` funde ids duplicados en silencio → la suite debe leer el JSON crudo, no el loader. | I3: PASS en los 4 |
| I4 | Cero aristas colgantes. `:10,79-81`. | r1 | ídem | — | F4 | convertible | no | Sin condición. Solapa S2 (`shapes_validator.py:383`). | I4: PASS en los 4 |
| I5 | Todo nodo y toda arista tienen `provenances` no vacío y `provenance` presente. `:11-12,83-90`. | r1 | ídem | r1: provenance rica (`r1_provenance.py`) | F2 (presencia) | convertible | no | Tal como está escrito exige la clave `provenances`, que gen 1 no emite (solo `provenance`): FAIL 4.050/6.634 sobre KG-Base por formato; con el adaptador la comprobación es «al menos una provenance por objeto». Solapa S4/S5/S6 (v0 `:1208/:1230/:1249`; congelado `:664/:701/:724`). | I5: FAIL / PASS / PASS / PASS |

### 2.iii Grupo (iii) — reglas declaradas de E4 (`r1_e4.py`, 10)

Numeración de esta unidad, leída del docstring (`r1_e4.py:5-36`) y del código: cinco
criterios de igualdad (a1–a5), la regla de ambigüedad (a6), la de no creación /
cuarentena tal cual (a7), la del merge aditivo (a8), la canonización de
`TextoOrdenado` (b) y el filtro de conflictos (c). El mandato nombra los 5
criterios, TextoOrdenado y el filtro; a6–a8 salen del mismo docstring (`:7-9`,
`:18-19`, `:20-24`) y son las que hacen 10.

Evidencia común del grupo (r1, `data/experiment/reextraccion_v2/corpus_v2/salida_r1/`):
`e4_propuestos.json` (44 filas: 3 `resuelto`, 41 `cuarentena`; motivos:
`sin_match_en_catalogo` 41, `resuelto_por_alias_en_parentesis+label_singularizado` 1,
`resuelto_por_id_slug+label_singularizado` 1,
`resuelto_por_alias_en_parentesis+label_exacto+label_singularizado` 1),
`e4_texto_ordenado.json` (5 canónicos, 1 eliminado: `…normas_sobre_capitales_minimos…`
de ric 4.1.1.4), `e4_conflictos.json` (`n_total` 2321, `n_variantes_to` 2125,
`n_reales` 196), `reporte_ensamblado_r1.json` «e4». Comando de verificación de
esta unidad (importa `r1_e4.indice_catalogo` y `r1_e4.resolver_label`, sin
copiarlos; salida pegada en §4): sobre r1 los 41 propuestos residuales dan
`sin_match_en_catalogo` 41; sobre KG-Reextraído (pre-E4) 43 propuestos, 3
resuelven (los mismos tres de `e4_propuestos.json`); sobre KG-Refinado 11
propuestos, 0 resuelven; `alias_resueltos` presente en 3 nodos de r1 y en 0 de
los otros grafos; índice del catálogo: 237 claves, 0 ambiguas.

| Id | Afirma | Grafo (sha) | Evidencia | Cambió | Forma | Conv. | Retr. | Condición / direccionamiento | Medido |
|---|---|---|---|---|---|---|---|---|---|
| E4-a1 | Un propuesto resuelve al id del catálogo si `norm(label) == norm(label del catálogo)` (`label_exacto`). `r1_e4.py:10`, índice `:89`, resolución `:101`. | r1 | `e4_propuestos.json` (1 fila con `label_exacto` entre sus candidatos: `…vpu_adheridos_al_rigi` → `Sujeto_vpu_rigi`); §4 | r1: E4 determinístico (`185e042`) | F1 ausente: ningún Sujeto `nivel = propuesto` residual cuyo `norm(label)` esté en las claves `label_exacto` del índice | con condición | no | Necesita: catálogo parametrizado (`esquema_v2_clases.json` / v3) e importar `r1_e4.indice_catalogo` / `resolver_label`; vacuo sin propuestos (KG-Base). Sentido sin r1: sí como test de «E4 corrió» (KG-Reextraído: FAIL esperado, 3 resolubles). | §4: r1 0 resolubles (PASS); KG-Reextraído 3 (FAIL); KG-Refinado 0 (PASS) |
| E4-a2 | … si `norm(label) == norm(alias declarado)` (`alias_exacto`). `:11`, `:92-93`, `:102`. | r1 | ídem (0 filas resueltas por `alias_exacto` solo) | ídem | F1 ausente | con condición | no | ídem a1 | ídem |
| E4-a3 | … si `slug(label) == slug del id del catálogo` (`id_slug`). `:12`, `:90`, `:103`; `slugify_full` en `e2_reduce/e2_lib.py:90`. | r1 | `e4_propuestos.json` (`Sujeto_propuesto_importador` → `Sujeto_importador`, `id_slug+label_singularizado`) | ídem | F1 ausente | con condición | no | ídem a1; además importa `e2_lib.slugify_full`. | ídem |
| E4-a4 | … si el label sin paréntesis, singularizado por token, iguala el del catálogo (`label_singularizado`). `:13-14`, `_singular` `:53-58`, `:91`, `:104`. | r1 | `e4_propuestos.json` (3 filas con `label_singularizado`) | ídem | F1 ausente | con condición | no | ídem a1 | ídem |
| E4-a5 | … si la sigla entre paréntesis del label es alias declarado y el `padre_sugerido` coincide con ese id o no hay padre (`alias_en_parentesis`). `:15-17`, `:108-112`. | r1 | `e4_propuestos.json` (`…contraparte_central_ccp` → `Sujeto_entidad_de_contraparte_central`; `…vpu…`) | ídem | F1 ausente + F3 (`padre_sugerido`) | con condición | no | ídem a1; la condición sobre el padre exige leer `properties.padre_sugerido`. | ídem |
| E4-a6 | Si dos criterios apuntan a ids distintos, o una clave del índice colisiona entre entradas del catálogo, no se resuelve (cuarentena «ambiguo» / clave `__AMBIGUO__`). `:7-9`, `:79-84`, `:113-117`. | r1 | `e4_propuestos.json` motivos (0 «ambiguo»); §4 (0 claves ambiguas en el índice v2) | ídem | F1 ausente (ningún propuesto residual con candidatos a ids distintos resuelto) | con condición | no | ídem a1; el caso «ambiguo» no ocurre en r1 ni en el catálogo v2: el test sería vacuo hasta que un catálogo lo produzca (fixture sintética en el selftest). | §4: 0 ambiguas |
| E4-a7 | Lo no resuelto queda en cuarentena tal cual (`nivel = propuesto`, `cuarentena = true`, `padre_sugerido` si lo hubo); nunca se crea una clase (`RuntimeError` si resuelve fuera del catálogo). `:18-19`, `:141-147`. | r1 | `tests_respuesta_conocida_r1.json` T7 (41 propuestos, 0 fuera de catálogo); `e4_propuestos.json` 41 `cuarentena` | ídem | F3 + F1 (todo Sujeto no propuesto ∈ catálogo) | con condición | no | ídem a1 (catálogo). Solapa T7 («fuera») y S19 (`shapes_validator.py:785`). | = T7 |
| E4-a8 | Al resolver, el merge es aditivo y registrado: el nodo del catálogo acumula las provenances del propuesto (dedup), recibe `alias_resueltos` y las aristas se re-apuntan con dedup de triplas (5 re-apuntadas en r1). `:20-24`, `:152-171`, `_reapuntar` `:178-202`. | r1 | `e4_propuestos.json` `remap` (3); `reporte_ensamblado_r1.json` «e4» (`aristas_reapuntadas: 5`); §4 (`alias_resueltos` en `Sujeto_entidad_de_contraparte_central`, `Sujeto_importador`, `Sujeto_vpu_rigi`) | ídem | F3 (`alias_resueltos` en los ids de catálogo esperados) + F4 (aristas re-apuntadas) | con condición | no | Necesita: fixture por grafo de los alias esperados (F3, directa por id de catálogo) y, para la acumulación de provenances y el dedup, el grafo pre-E4 (solo cadena r1). Sentido sin r1: el F3 da «ausente» en todo grafo sin E4 (KG-Reextraído 0/3). | §4: r1 3/3; otros 0 |
| E4-b | Un único `TextoOrdenado` por TO, con id y `archivo` derivados de la provenance (archivo del PDF según E0); todo otro `TextoOrdenado` de ese TO se elimina y sus aristas se re-apuntan. `:26-30`, `:208-250`. | r1 | `e4_texto_ordenado.json` (5 canónicos, 1 eliminado); T6 | ídem | F1 (= T6) + F3 (`properties.archivo` ∈ archivos de E0) | con condición | no | = T6 (fixture de archivos + `slugify_full`). Sentido sin r1: sí (KG-Reextraído es el caso negativo: 6, 1 fuera). Solapa T6, S6. | §4: 5/5 KG-Base, KG-Refinado, r1; 5/6 KG-Reextraído |
| E4-c | `materia`/`version` de `TextoOrdenado` salen del registro de conflictos como VARIANTES; el resto (`Operacion.tipo`, `*.descripcion`, …) se persiste como conflictos reales sin resolver. `:32-36`, `:256-291`. | r1 | `e4_conflictos.json` (2321 / 2125 / 196; `reales_por_tipo_property` `Operacion.tipo` 104, `Obligacion.descripcion` 45, …) | ídem | ninguna directa: los conflictos no se persisten en el kg.json | con condición | no | Necesita: el artefacto `e4_conflictos.json` (o los grafos pre-E4 y el reporte E2) como insumo; sobre el kg.json solo existe un proxy débil (F3: cada `TextoOrdenado` tiene un solo valor de `materia`/`version`), que no es la regla. Sentido sin r1: ninguno sin el artefacto. | — (no sondeado sobre los grafos) |

## 3. Solapamientos (para que la suite no duplique)

| Ítem | Ya cubierto por | Path | Alcance del solapamiento |
|---|---|---|---|
| BKL-0007 | BKL-0017 (C1) | backlog líneas 42, 46 | total: mismo objeto, sin test propio |
| BKL-0003 (C6) | T3 | `ensamblar_corpus.py:267-280` | parcial: T3 acepta cualquier tipo con «mutual/cooperativ» en pro 1.1.2.5; C6 exige `Excepcion` + 2 aristas + rank |
| BKL-0003 (C6), aristas | S10 (toda unidad regulatoria tiene `establecida_en`), S12 (toda Excepcion tiene `exceptua`/`exceptua_obligacion`) | `scripts/shapes_validator.py:467`, `:507` | parcial: la Excepcion de gen 3 sin `establecida_en` es exactamente lo que S10 reporta |
| BKL-0019 (C4) | T7 (`subclase_de` desde propuesto prohibido) y S22 (`padre_sugerido` coherente con la property) | `r1_tests.py:75-76`; `shapes_validator.py:890` | contradictorio con T7 en gen 2; S22 cubre la política flaggeada de gen 3 |
| BKL-0028 / BKL-0029 | S15 (roles con `miembro_de` o declarados en `--excepciones`) y S19 (catálogo) | `shapes_validator.py:566`, `:785` | parcial: S15 hoy lista convca como `aplanamiento_rechazado` (backlog línea 73, `verificacion`) |
| RT-C6-3 / RT-C6-4 (estructura del rol) | S15 | `shapes_validator.py:566` | parcial: S15 exige `miembro_de` no vacío, no el número 7 |
| RT-C5-1..4 (valor) | BKL-0004 (C5) | esta tabla | total en la parte de valor: el gold vive en N1/N3/N5/N6 de C5 |
| RT-C6-1 / RT-C6-2 (valor) | BKL-0003 (C6) | esta tabla | total en la parte de valor |
| RT-C7-1..3 (valor) | BKL-0005 (C7) | esta tabla | total en la parte de valor; el rank es propio |
| T1 | BKL-0024 (triaged, fuera del inventario) | backlog líneas 56-57; `X.BKL-0024` en la sonda de anclas | T1 es el test que el backlog prevé como «caso de prueba para la re-extracción» |
| T4 | S15; E5 (`ensamblar_r1.py`) | `shapes_validator.py:566` | parcial: S15 mira roles/miembros, T4 paridad completa |
| T5 | S21 (coherencia de referencias nodo→nodo) | `shapes_validator.py:858` | parcial: S21 mira la coherencia punto/destino, T5 la evidencia verbatim de 30 |
| T6 / E4-b | S6 (`source_doc` ∈ archivos de `TextoOrdenado`) | `shapes_validator.py:1249` (v0), `:724` (congelado) | parcial; T6 y E4-b se solapan entre sí por completo |
| T7 / E4-a7 | S19 (catálogo, nivel, cuarentena, `padre_sugerido`), S22, S23 | `shapes_validator.py:785`, `:890`, `:915` | parcial: S19 no exige `cuarentena == "true"` como string ni prohíbe `subclase_de` desde propuesto |
| I3 | — (ninguna shape de unicidad de id) | `shapes_validator.py:402` (S7 es por `(type, label)`) | sin cobertura; el loader del harness funde ids duplicados (`loader.py:180`) |
| I4 | S2 | `shapes_validator.py:383` | total |
| I5 | S4, S5, S6 | `shapes_validator.py:1208/1230/1249` (v0), `:664/:701/:724` (congelado) | total en presencia; las shapes además validan campos |
| I1 / I2 | `reporte_ensamblado_r1.json` «invariantes_final» y selftest de `r1_invariantes.py:171-222` | — | fuera de la suite: solo cadena r1 |
| E4-a1..a6 | `r1_e4.py` (importado) | `r1_e4.py:74-118` | la suite importa, no reimplementa (fila B2.1 del plan, borrador de fase 2, pieza c) |

## 4. Verificación de las reglas E4 sobre los cuatro grafos (comando y salida verbatim)

Comando (desde la raíz del repo; importa `r1_comun` y `r1_e4` sin copiarlos; solo lectura):

```
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python3 - <<'PY'
import sys, json, collections
sys.path.insert(0, "data/experiment/reextraccion_v2/corpus_v2")
import r1_comun as C, r1_e4 as E4
cat = C.cargar_catalogo(); idx = E4.indice_catalogo(cat)
arch = {C.archivo_de_to(to) for to in C.TOS_ORDEN}
print("catalogo:", C.CATALOGO_PATH.relative_to(C.REPO), "| clases", len(cat["clases"]), "roles", len(cat["roles"]), "| claves del indice", len(idx), "| ambiguas", sum(1 for v in idx.values() if v == "__AMBIGUO__"))
for nombre, ruta in [("KG-Base","data/experiment/run_3_ppf_core/kg.json"),("KG-Refinado","data/experiment/grafo_v2/reensamblado_v3/kg.json"),("KG-Reextraido","data/experiment/reextraccion_v2/corpus_v2/salida/kg.json"),("KG-Reextraido-r1","data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json")]:
    kg = json.load(open(ruta, encoding="utf-8"))
    prop = [n for n in kg["nodes"] if n["type"]=="Sujeto" and (n.get("properties") or {}).get("nivel")=="propuesto"]
    mot = collections.Counter(); res = []
    for n in prop:
        rid, motivo, cands = E4.resolver_label(n["label"], (n.get("properties") or {}).get("padre_sugerido"), idx)
        mot[motivo] += 1
        if rid: res.append((n["id"][:60], rid, motivo))
    print(f"{nombre}: propuestos={len(prop)} motivos={dict(mot)}")
    for r in res: print("   resuelve:", r)
    ar = [(n["id"], (n.get("properties") or {}).get("alias_resueltos")) for n in kg["nodes"] if n["type"]=="Sujeto" and (n.get("properties") or {}).get("alias_resueltos")]
    print(f"   nodos con properties.alias_resueltos: {len(ar)} -> {ar}")
    tos = [(n["id"], (n.get("properties") or {}).get("archivo")) for n in kg["nodes"] if n["type"]=="TextoOrdenado"]
    print(f"   TextoOrdenado: {len(tos)}; con properties.archivo en el conjunto de archivos de E0: {sum(1 for _, a in tos if a in arch)}/{len(tos)}; fuera: {[(i, a) for i, a in tos if a not in arch]}")
PY
```

Salida (verbatim, 2026-09-26):

```
catalogo: data/experiment/grafo_v2/esquema_v2_clases.json | clases 65 roles 5 | claves del indice 237 | ambiguas 0
KG-Base: propuestos=0 motivos={}
   nodos con properties.alias_resueltos: 0 -> []
   TextoOrdenado: 5; con properties.archivo en el conjunto de archivos de E0: 5/5; fuera: []
KG-Refinado: propuestos=11 motivos={'sin_match_en_catalogo': 11}
   nodos con properties.alias_resueltos: 0 -> []
   TextoOrdenado: 5; con properties.archivo en el conjunto de archivos de E0: 5/5; fuera: []
KG-Reextraido: propuestos=43 motivos={'sin_match_en_catalogo': 40, 'resuelto_por_alias_en_parentesis+label_singularizado': 1, 'resuelto_por_id_slug+label_singularizado': 1, 'resuelto_por_alias_en_parentesis+label_exacto+label_singularizado': 1}
   resuelve: ('Sujeto_propuesto_entidad_de_contraparte_central_ccp', 'Sujeto_entidad_de_contraparte_central', 'resuelto_por_alias_en_parentesis+label_singularizado')
   resuelve: ('Sujeto_propuesto_importador', 'Sujeto_importador', 'resuelto_por_id_slug+label_singularizado')
   resuelve: ('Sujeto_propuesto_vehiculos_de_proyecto_unico_vpu_adheridos_a', 'Sujeto_vpu_rigi', 'resuelto_por_alias_en_parentesis+label_exacto+label_singularizado')
   nodos con properties.alias_resueltos: 0 -> []
   TextoOrdenado: 6; con properties.archivo en el conjunto de archivos de E0: 5/6; fuera: [('TextoOrdenado_normas_sobre_capitales_minimos_de_las_entidades_financieras', 'normas sobre Capitales mínimos de las entidades financieras')]
KG-Reextraido-r1: propuestos=41 motivos={'sin_match_en_catalogo': 41}
   nodos con properties.alias_resueltos: 3 -> [('Sujeto_entidad_de_contraparte_central', ['Entidad de contraparte central (CCP)']), ('Sujeto_importador', ['importador']), ('Sujeto_vpu_rigi', ['Vehículos de Proyecto Único (VPU) adheridos al RIGI'])]
   TextoOrdenado: 5; con properties.archivo en el conjunto de archivos de E0: 5/5; fuera: []
```

Lectura: KG-Base no tiene Sujetos (test vacuo); en KG-Refinado ninguno de los 11
propuestos de cuarentena resuelve por los cinco criterios; en KG-Reextraído
(pre-E4) resuelven exactamente los 3 que `e4_propuestos.json` registra; en r1
ninguno de los 41 residuales resuelve y los 3 nodos de catálogo llevan
`alias_resueltos`. La canonización de `TextoOrdenado` (E4-b) deja 5/5 en tres
grafos y 5/6 en KG-Reextraído.

## 5. Hallazgos adicionales de esta unidad (no previstos por la decisión 5; van a la tabla resumen)

1. **T4 falla sobre KG-Refinado, el grafo que le sirve de referencia**: 90 aristas de relaciones de esqueleto contra el 82 cableado (`r1_tests.py:40`); las 8 de más son las `subclase_de` de C4 con `rol_fuente: cuarentena_laudada`, que el test no filtra en el grafo bajo prueba (`:35-36`). Consecuencia para la suite: leer el conjunto del esqueleto de la referencia por `rol_fuente` y contar en el grafo bajo prueba con el mismo filtro, o declarar el 82 como parámetro por política de cuarentena.
2. **Contradicción C4/T7 con un matiz de formato**: además de las 8 `subclase_de`, T7 marca 11 «sin cuarentena=true» en KG-Refinado porque gen 2 guarda `cuarentena` como booleano y `r1_tests.py:68` compara con la string `"true"`. El adaptador debe normalizar el booleano.
3. **RX-10 persiste en gen 3** (KG-Reextraído y r1): bancos `umbral` 2.500 / restantes 5.000 (`C2.tabla_1_2`). Coincide con la nota (1) de la fila B2.1 del plan; el test convertido de C2 dará «persiste» hasta que el parser de tablas esté cableado al pipeline.
4. **C1, C6 y C7 están resueltos por el pipeline gen 3** sin edición manual (nodo del 1.1 presente con el mismo id; Excepcion de mutuales extraída; descripción del 7.1 con los dos calificadores), pero C6 en gen 3 no tiene `establecida_en` (lo que S10 reporta) y C3/C5 quedan sin nodo (C3) o parciales 5/9 (C5). BKL-0024/0025 tienen anclas en gen 3 (21 nodos en ext 3.9*, 5 en pro 1.1.1 con 4 que mencionan «usuario») y siguen `triaged` (coincide con la nota (2) de la fila B2.1 del plan).
5. **Direccionar por id de contenido no es viable entre generaciones**: de los ids de C1–C7, solo `…_e1946e` sobrevive en gen 3; `_5f95b9` reaparece con tipo `Obligacion` (mismo slug de descripción, otro tipo). Direccionar por (archivo, punto, tipo, cadena) encuentra el objeto en los cuatro grafos cuando existe.
6. **Ranks fuera del top-10 se reproducen**: el «bancos 13» del retest C2 exige `limite ≥ 13` (tope 50 del harness); un test de rank debe declarar el límite pedido, no solo «top-10».
7. **En gen 3 el punto 7.2 de Clasificación no tiene nodos con `punto == "7.2"`** (0 en KG-Reextraído y r1 contra 39 en KG-Refinado): el proxy de RT-C5-5 (`riesgo medio` anclado en 7.2) falla por ancla, no por contenido; la sonda no exploró 7.2.x.
8. **Corrida real de RT-C7-1..3 con agente+juez: NO ENCONTRADA** en el repo (solo el retest determinístico); las de RT-C5 (5/5 correcta) y RT-C6 (2/4) sí están en `posthoc_run/traces/rt_c5_c6/reensamblado_v3/`.
9. **Cinco ids `verificado` sin evento `aplicacion`** (BKL-0007, 0026, 0027, 0028, 0029; `estado_backlog_B21_fase1_salida.txt`, última línea): para 0026–0029 «verificado» significa defecto confirmado, no corrección aplicada (`aplicado_en: null`); entran al inventario por la regla del mandato y se clasifican por lo que afirman.
10. **El criterio de clasificación de la corrida del 15/09 no está registrado** en ningún archivo del repo (el paquete se perdió; la fila B2.1 solo asienta los totales); por eso la comparación 14/28/4 contra esta unidad se hace contra el criterio declarado en §1, y la diferencia se reporta sin ajustar (tabla resumen).
