# Informe E1 fase A — extractor por chunk (construcción + selftest offline + estimación)

Unidad del pipeline de re-extracción v2 (issue #8), etapa E1 de
`docs/diseno_reextraccion_v2.md` §3-E1, fase A: todo offline, cero llamadas a
APIs de LLM (el entorno ni siquiera tiene `anthropic` instalado; el único
cliente instanciado es el stub). Gasto de API: USD 0,00.

## 1. Insumos y fuente del esquema

- Salida de E0: `../e0_chunking/salida/chunks_{cap,cla,ext,pro,ric}.json` —
  1.477 chunks (401+127+783+88+78), 59 flaggeados tabular/fórmula, herencia
  estructural con `unidad_origen` por bloque.
- **Esquema v2 vigente**: se localizaron dos documentos candidatos
  (`docs/esquema_v2_diseño.md`, diseño del árbol laudado, y
  `docs/spec_extraccion_v2.md`, spec de implementación) que NO compiten: son
  el linaje diseño→spec de la misma implementación vigente, que es la fuente
  única usada acá: `data/experiment/grafo_v2/code/schema.py` (6 entity types,
  12 predicados, matriz de firmas `DOMAIN_RANGE`, sistema de sujetos con
  catálogo cerrado + cuarentena) cargando
  `data/experiment/grafo_v2/esquema_v2_clases.json` v2.0 (65 clases + 5 roles
  por-TO). E1 la IMPORTA (solo lectura), no la duplica.
- `docs/decisiones_caching_extraccion.md` (5 decisiones vinculantes) y patrón
  fase A de `data/experiment/exploracion/sinteticas/` (cliente inyectable +
  stub + estimación parametrizada).
- `data/experiment/evaluacion/llm_cache.py`: se envuelve, jamás se edita.

## 2. Entregables (todo bajo `e1_extractor/`)

| Archivo | Rol |
|---|---|
| `comun_e1.py` | paths, carga E0, `puntos_admitidos()` y rol documental por punto |
| `prompt_e1.py` | T1: prefijo estable + tool schema + mensaje variable por chunk |
| `cliente_e1.py` | T2: stub offline + cliente real fase B sobre llm_cache (envuelto) |
| `validador_e1.py` | T3: validación determinística con rechazos con motivo |
| `selftest_e1.py` | T4: 40 checks offline |
| `estimacion_e1.py` | T5: estimación calibración vs corpus, con y sin caching |
| `fixtures/fixtures_e1.json` | fixtures buenas/malas/flaggeado del selftest |
| `salida/estimacion_e1.json` | estimación persistida |

## 3. T1 — Prompt de extracción

**Prefijo estable** (un solo bloque `system` con
`cache_control {"type": "ephemeral"}` como breakpoint; los tools —también
estables— forman parte del prefijo cacheado): instrucciones + los 6 tipos +
la tabla de los 12 predicados con dominio→rango + el sistema de sujetos
completo (catálogo compacto `SUJETOS_PROMPT` + reglas de elección/cuarentena,
heredadas del prompt v2 probado) + las reglas E1 nuevas:

- **Provenance por elemento**: toda entidad y toda relación llevan `punto`,
  restringido al conjunto cerrado "puntos admitidos" del chunk (punto propio +
  unidades de origen de la herencia). El contenido de un chapeau/encabezado
  heredado se extrae anclado a SU unidad de origen (ataca el mecanismo
  "chapeau perdido", U6-001/005/007/015/019/025). El `to`/`archivo` y el rol
  documental NO los emite el LLM: los estampa el validador determinísticamente
  desde E0 (split mecánico/juicio, principio 2.b del diseño).
- **Anti-fusión** (regla 5): cláusulas casi idénticas con valores,
  calificadores, sujetos o modalidad distintos son entidades separadas con
  provenance separada; prohibido resumir u omitir "porque ya extraje una
  parecida" (caso rector U6-008, cláusula del 125 %).
- **Labels front-loadeados** (diseño §3-E5, anti-colisión por truncamiento
  U6-020): ≤8 palabras, contenido distintivo AL PRINCIPIO, con ejemplos ✓/✗ de
  hermanos con prefijo común.
- **Completitud intra-chunk** (regla 8): calificadores, salvedades e ítems de
  enumeración obligatorios (especie dominante del backlog).

**Único contenido variable, después del breakpoint** (mensaje de usuario):
documento, TO, punto y título, lista de puntos admitidos, alcance del TO (rol
por-TO del catálogo), bloques de herencia `[tipo | punto unidad_origen]`,
bloque `FLAGS E0` si corresponde, y el texto del punto. Función pura del dict
del chunk: mismo chunk → mismo mensaje byte a byte.

**Tratamiento de flaggeados** (59 chunks): el mensaje declara el flag con la
evidencia determinística de E0; el prefijo instruye contenido NO-CONFIABLE: no
reconstruir tablas/fórmulas, no copiar valores de celdas/coeficientes salvo
que la prosa los enuncie, registrar cada omisión en `omisiones_no_prosa`
(campo del contrato de salida). El validador registra advertencia si un chunk
flaggeado extrae sin declarar omisiones. Resuelve la pregunta abierta §7.d del
diseño por la vía "flag de contenido no-confiable" (mandato de esta unidad),
no extracción estructurada dedicada.

**Contrato de salida** (`extraer_kg_e1`, tool_choice forzado): entities
(local_id, type∈6, label, `punto`, properties), relations (predicate∈12,
`punto`, source/target o sujeto_id⊕sujeto_propuesto con enum duro del
catálogo), `omisiones_no_prosa`. Hash del prefijo completo:
`prompt_e1.PREFIJO_HASH` (se imprime en selftest y estimación).

## 4. T2 — Cliente inyectable + caché

`StubClienteE1` (selftest, offline) y `ClienteE1Real` (fase B) comparten el
camino `extraer_chunk()` sobre el request canónico de
`build_request_kwargs()`. El real: `llm_cache.CachingClient` (envuelto, jamás
editado) con **db propia** `cache/e1_extraccion.db`, **namespace propio**
`e1_extraccion|cv=e1-extractor-v1-p<hash_prefijo>|think=0` (code-version
manual + hash del prefijo como doble candado), contabilidad con la fórmula de
caching (Decisión 2), log de usage por response real a `logs/cache_usage.jsonl`
con `component="reextraccion_v2_e1"` (Decisión 3), tope duro con proyección
pre-llamada, y construcción imposible sin precios y tope explícitos (la
autorización de fase B). Corridas secuenciales (Decisión 4) — el cliente es
sincrónico. El pipeline de evaluación no se toca (Decisión 5).

## 5. T3 — Validador

Determinístico, por elemento (un elemento inválido no tumba el chunk; una
salida no parseable sí). Valida: estructura (con coerciones defensivas
heredadas del v2: listas como string JSON, ""→None, properties→str, target
espurio en aplica_a anulado), types contra `ENTITY_TYPES`, predicados y firmas
contra `DOMAIN_RANGE` (extremo sujeto como pseudo-tipo), sujeto_id contra el
catálogo (padre sugerido inválido se anula, no invalida), exclusión mutua
sujeto_id/sujeto_propuesto, referencias no colgantes, y **provenance en todo
elemento**: `punto` presente y dentro de los admitidos; el aceptado sale
normalizado con `{to, archivo, punto, rol_documental}`. Todo rechazo queda
registrado con motivo estable (12 motivos distintos ejercitados en el
selftest) — insumo del mini-ratchet de E3, acá solo registro. Advertencias
(no rechazo): labels >12 palabras, flags sin omisiones declaradas.

## 6. T4 — Selftest offline: 40 ok, 0 FAIL

Reproduce: `python3 selftest_e1.py`. Cobertura:

- **[A] Prefijo estable (8)**: system+tools+tool_choice byte-idénticos en los
  1.477 chunks; breakpoint ephemeral en el último (único) bloque; nada del
  texto variable antes del breakpoint; catálogo embebido; los 5 TOs con rol.
- **[B] Determinismo (2)**: mismo chunk → request byte a byte; chunk
  re-parseado desde JSON → idéntico.
- **[C] Flaggeados (5)**: bloque FLAGS exactamente en los 59; evidencia E0 en
  el mensaje; instrucción no-prosa presente.
- **[D] Stub→parseo→validación (17)**: 2 fixtures buenas aceptadas íntegras
  (incl. provenance de herencia con `rol_documental=herencia_encabezado` y
  cuarentena con padre sugerido); 10 malas rechazadas con el motivo exacto;
  flaggeado conforme vs sin declarar; el stub recibe el request canónico.
- **[E] Keys de caché (3)**: determinísticas, distintas por chunk, namespace
  con code-version y hash de prefijo.
- **[F] Estimación (3)**: reproducible; 88 y 1.477.

## 7. T5 — Estimación (sin precios)

Reproduce: `python3 estimacion_e1.py`. Ancla empírica: los 508 resultados
reales sellados de `grafo_v2/code/cache_v2/full/` (solo lectura) con el
mensaje v2 reconstruido byte a byte; el ajuste `in = A + B·chars` separa el
costo fijo por request (A≈9.415 tok: en esa corrida el prefijo se facturó
como input) de la tarifa variable (r = 3,471 chars/token). El ancla del
harness (≈2,0 chars/token) se descartó para prosa: ese prefijo es JSON de
tools. Supuestos S1–S7 numerados en el JSON y en el docstring.

| | calibración (pro) | corpus (5 TOs) |
|---|---|---|
| chunks | 88 | 1.477 |
| prefijo (tokens, una vez) | 10.553 | 10.553 |
| variable total (tokens) | 62.227 | 1.008.042 |
| output total (tokens) | 150.585 | 2.471.656 |
| input SIN caching (tokens) | 990.891 | 16.594.823 |
| input no cacheado (tokens) | 62.227 | 1.008.042 |
| cache write (tokens) | 10.553 | 10.553 |
| cache read (tokens) | 918.111 | 15.576.228 |
| input equivalente CON caching (tokens) | 167.229 | 2.578.856 |
| ahorro componente input | 83,1 % | 84,5 % |

Cuenta equivalente (multiplicadores 1,25 write / 0,10 read sobre P_in):
`no_cacheado + 1,25×write + 0,10×read` → calibración
`62.227 + 1,25×10.553 + 0,10×918.111 = 167.229` vs `990.891` sin caching.

Fórmulas parametrizadas (precios NO consultados; se resuelven en la
autorización de fase B):

- Calibración: `costo = 62.227/1e6×P_in + 10.553/1e6×P_cache_write + 918.111/1e6×P_cache_read + 150.585/1e6×P_out`
- Corpus: `costo = 1.008.042/1e6×P_in + 10.553/1e6×P_cache_write + 15.576.228/1e6×P_cache_read + 2.471.656/1e6×P_out`

Nota never-pay-twice: si el corpus corre tras la calibración con el mismo
prefijo y namespace, los 88 chunks de pro son hits de la caché local; el
incremental real es 1.389 chunks (la tabla no descuenta eso).

## 8. Límites declarados

- La estimación de output extrapola un ajuste lineal medido sobre chunks v1
  (más grandes) a chunks E0 (más chicos): el piso de 627 tok/chunk domina en
  chunks cortos y puede sobreestimar el output total. Es el sesgo conservador
  elegido.
- El prefijo E1 en tokens escala el intercepto real por tamaño relativo de
  chars; el número exacto se mide en la primera llamada real de la
  calibración (campo `cache_creation_input_tokens`).
- La regla de labels front-loadeados es de prompt; el validador solo advierte
  por longitud. Su cumplimiento se evalúa en la calibración.
- `ClienteE1Real` está escrito pero NO ejercitado contra la API (prohibición
  de fase A); su primera prueba real es parte de la fase B.
