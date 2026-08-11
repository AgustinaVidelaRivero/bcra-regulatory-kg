# Informe E3 fase A — verificador de completitud intra-unidad (construcción + selftest offline + estimación)

Unidad del pipeline de re-extracción v2, etapa E3 de
`docs/diseno_reextraccion_v2.md` §3-E3, fase A: todo offline, cero llamadas a
APIs de LLM (los únicos clientes instanciados son los stubs). Gasto de API:
USD 0,00. Fase B (calibración sobre pro) requiere autorización con precios de
modelo fuerte resueltos.

## 1. Insumos (solo lectura)

- Salida de E0: `../e0_chunking/salida/chunks_{cap,cla,ext,pro,ric}.json` —
  texto fuente por unidad (punto propio + herencia con `unidad_origen`).
- Salida de E1 fase B: `../e1_extractor/salida/faseB_pro/extracciones.jsonl` —
  lo extraído por unidad, con validación por elemento. Universo de la
  calibración E3: las **87 unidades aceptadas** (fan-in de E2: 88 recibidas −
  1 rechazada, `pro::3.1.1.2`; el rechazado va por el carril del fan-in de E2,
  no por E3 — no tiene extracción que verificar).
- Salida de E2: `../e2_reduce/salida/reporte_e2_pro.json` (fan-in de
  referencia).
- Backlog (`data/backlog/backlog.jsonl` + retests C5/C6/C7): SOLO para
  construir los calibradores.
- Módulos de E1 (`prompt_e1`, `validador_e1`, `cliente_e1`): importados para
  la mecánica de re-inyección del ratchet, jamás editados.
- `docs/decisiones_caching_extraccion.md` (5 decisiones vinculantes) y
  `data/experiment/evaluacion/llm_cache.py` (se envuelve, jamás se edita).

## 2. Entregables (todo bajo `e3_verificador/`)

| Archivo | Rol |
|---|---|
| `comun_e3.py` | paths, carga E0/E1, fuente íntegro, render legible, normalización de citas |
| `calibradores_e3.py` | T1: los 4 calibradores resueltos derivados del backlog |
| `prompt_e3.py` | T1: prefijo estable (instrucciones + contrato + calibradores) + mensaje variable |
| `cliente_e3.py` | T3: stub offline + cliente real fase B sobre llm_cache (envuelto), db y namespace propios |
| `ratchet_e3.py` | T2: capa determinística del veredicto + prompt de reintento + ciclo con tope + persistencia |
| `generar_fixtures_e3.py` / `fixtures/fixtures_e3.json` | T4: fixtures (amputación a mano de un chunk real de pro + stubs) |
| `selftest_e3.py` | T4: 51 checks offline |
| `estimacion_e3.py` / `salida/estimacion_e3.json` | T5: estimación calibración/corpus, fórmulas parametrizadas |
| `.gitignore` | `cache/` (patrón E1) y `salida/selftest_out/` (artefacto regenerable del selftest) |

## 3. T1 — Prompt del verificador

**Contexto fresco por construcción** (principio 2.c): el request de E3 se arma
SOLO desde datos — el texto fuente íntegro del chunk (herencia con unidad de
origen + punto propio, de E0) y los elementos extraídos post-validación (de
E1, renderizados legibles: entidades con properties, relaciones con extremos y
sujetos, omisiones no-prosa declaradas). El selftest verifica por centinelas
que ninguna instrucción del prompt del extractor (system, tool, mensaje) entra
al request del verificador.

**Prefijo estable** (un solo bloque `system` con `cache_control ephemeral`;
los tools estables integran el prefijo cacheado): tarea (identificar contenido
normativo del fuente NO representado; blanco: amputaciones), definición de
"representado" (sustancia normativa en descripcion/label/relación; paráfrasis
válida; anclaje a punto propio o unidad heredada), los 6 tipos de faltante
(`enumeracion_incompleta`, `calificador_despojado`, `excepcion_ausente`,
`modalidad_perdida`, `contenido_tabular_no_declarado`, `otro`), qué NO es
faltante (labels cortos, jerarquía documental, granularidad de sujetos,
omisiones tabulares DECLARADAS, paráfrasis), severidad (alta/media/baja con
sesgo a marcar en la duda), contrato de salida, y la regla dura: **el
verificador jamás corrige** — detecta y documenta.

**Contrato de salida** (`verificar_completitud_e3`, tool_choice forzado):
`veredicto ∈ {completo_ok, faltantes_detectados}` + lista de faltantes con
`{tipo, cita_textual_del_fuente (VERBATIM, se verifica contra el fuente),
ubicacion, severidad, nota?}`. Un faltante por omisión.

**Calibradores** (hallazgo H12: los jueces honran ejemplos resueltos y
circunvalan reglas), cada uno con fuente + extracción + veredicto correcto +
porqué; los fuentes salen de la salida sellada de E0 y la extracción real del
CAL-4 de la salida sellada de E1 fase B:

- **CAL-1 · calificador_despojado** — BKL-0005/C7 (`ric::7.1`): extracción con
  la `descripcion` ANTES laudada del retest C7; veredicto: 2 faltantes (RPC
  sin "informada en el mes n", Franquicia sin "calculada según datos del mes
  n"), citas = renglones íntegros del esquema.
- **CAL-2 · excepcion_ausente** — BKL-0003/C6 (`pro::1.1.2.5`): extracción que
  reproduce la amputación histórica (alcance sin el "excepto ..."); veredicto:
  1 faltante con cita "excepto que se trate de asociaciones mutuales o
  cooperativas".
- **CAL-3 · enumeracion_incompleta** — BKL-0004/C5 (`cla::6.5.1.1`):
  extracción que representa el punto propio y los demás párrafos del intro
  heredado del 6.5 pero omite la cláusula que ordena la enumeración de los
  cinco niveles; la cita cruza un guion de corte de línea del PDF
  ("si-\nguientes") y verifica igual gracias a la normalización.
- **CAL-4 · completo_ok** — par mínimo de CAL-2: misma fuente, y la extracción
  REAL de E1 fase B (byte a byte), que capturó la salvedad como descripcion +
  nodo Excepcion + `exceptua_obligacion`. Enseña además qué NO marcar
  (encabezados heredados, labels cortos).

Prefijo completo: 26.837 chars (system 25.393 + tool schema); hash
`21a836c7de6d` (`prompt_e3.PREFIJO_HASH`, impreso por selftest y estimación).

## 4. T2 — Mecánica del mini-ratchet

`ratchet_e3.ciclo_ratchet()`: verificación → (si faltantes) re-extracción →
re-validación E1 → re-verificación E3 → aceptación o cola humana. **Tope: 1
reintento** (`TOPE_REINTENTOS = 1`, laudo del mandato de esta unidad; resuelve
§7.a del diseño para la calibración — re-laudable con datos reales).

- **Capa determinística sobre el veredicto** (principio 2.b, mismo patrón que
  la capa determinística de la Fase 2.4): coherencia del contrato
  (completo_ok ⇔ faltantes vacío; incoherente jamás cuenta como ok) y
  verificación de cada cita contra el fuente real con la normalización del
  precedente C7 (des-guionado + sin espacios + casefold + sin acentos). Una
  cita que no verifica NO se inyecta al reintento (una cita fabricada
  envenenaría la re-extracción); si NINGUNA verifica, el veredicto es
  inutilizable y el chunk va a cola humana con flag propio.
- **Prompt de reintento**: el request E1 canónico del chunk ÍNTEGRO + bloque
  de feedback estructurado ANEXADO al mensaje de usuario, marcado
  (`# REINTENTO DE EXTRACCIÓN — feedback del verificador...`), con un ítem por
  faltante (tipo, ubicación, severidad, cita) y la instrucción de re-extraer
  el chunk COMPLETO. **El bloque va después del breakpoint de caché**: el
  selftest verifica que system + tools + tool_choice del reintento son
  byte-idénticos al request original (el prefijo E1 cacheado no se invalida) y
  que el mensaje original es prefijo estricto del mensaje del reintento.
- **Cola humana**: faltantes persistentes tras el reintento → estado
  `cola_humana`, flag + TODO persistidos en `cola_humana.jsonl`;
  `validacion_final = None` — **nunca ingreso silencioso al grafo**. Estados
  adicionales: `cola_humana_veredicto_inutilizable` y
  `cola_humana_reextraccion_invalida` (reintento no parseable o rechazado a
  nivel chunk por el validador E1).
- **Persistencia total**: `RegistroE3` appendea TODOS los veredictos
  (verificaciones y re-verificaciones, con crudo, incoherencias y flags de
  cita) a `veredictos.jsonl`.

Ejemplo de fixture (T4): a la extracción real aceptada de `pro::2.3.1.2`
(Contratos multiproducto) se le amputó a mano el calificador **"cuando el
sujeto obligado así lo disponga"** (el que vuelve facultativa la pérdida de
beneficios por revocación). Flujo verificado con stubs: veredicto
`calificador_despojado` (cita verificada contra el fuente) → reintento con
feedback → el stub extractor devuelve la extracción real completa →
re-validación E1 ok → re-verificación `completo_ok` → estado
`aceptado_tras_reintento`, con la extracción final conteniendo el calificador
y los 2 veredictos persistidos.

## 5. T3 — Cliente inyectable + caché

Patrón E1 calcado: `StubClienteE3` (selftest, offline) y `ClienteE3Real`
(fase B) comparten `verificar_chunk()` sobre el request canónico. El real:
`llm_cache.CachingClient` (envuelto, jamás editado) con **db propia**
`cache/e3_verificacion.db`, **namespace propio**
`e3_verificacion|cv=e3-verificador-v1-p21a836c7de6d|think=0` (code-version
manual + hash del prompt del verificador como doble candado), contabilidad
con la fórmula de caching (D2), log por response real a `logs/cache_usage.jsonl`
con `component="reextraccion_v2_e3"` (D3), tope duro con proyección
pre-llamada dimensionada al prefijo E3, construcción imposible sin precios y
tope explícitos, y corridas secuenciales (D4; cliente sincrónico). Los precios
que recibe son los del MODELO FUERTE (D3 del diseño).

## 6. T4 — Selftest offline: 51 ok, 0 FAIL

Reproduce: `python3 selftest_e3.py`. Cobertura: [A] prefijo estable idéntico
en las 87 unidades, breakpoint ephemeral, un solo bloque, variable tras el
breakpoint (8); [B] contexto fresco por 5 centinelas del prompt E1 ausentes +
fuente y extracción presentes como datos (7); [C] determinismo byte a byte +
re-parseo + bloque de flags E0 (4); [D] calibradores: 4, tipos correctos,
citas verificadas contra fuente real, guion de PDF, CAL-4 == extracción real
byte a byte, par mínimo CAL-2/CAL-4, amputación C7 exacta (7); [E] capa de
citas: positivo con guiones, negativo fabricado, insensible a
espacios/saltos, vacía (4); [F] ratchet completo con stubs: detección,
reintento con prefijo E1 intacto y feedback post-breakpoint marcado, aceptado
tras reintento, completa directa, tope 1 → cola humana con flag y TODO,
incoherente, cita fabricada → sin re-extracción, persistencia 6 veredictos +
2 cola (14); [G] keys/namespace propios, hash E3 ≠ hash E1 (4); [H]
estimación reproducible, 87/1.477 (2). Fixtures generadas determinísticamente
por `generar_fixtures_e3.py` desde las salidas selladas.

## 7. T5 — Estimación (sin precios)

Reproduce: `python3 estimacion_e3.py`. Supuestos V1-V8 numerados en el JSON:
V1 ratio prosa 3,471 chars/token (ancla empírica E1, 508 pares reales); V2
render de extracción a 2,5 chars/token (conservador); V3 prefijo E3 =
26.837 chars → ≈10.735 tokens (se mide exacto en la primera llamada real); V4
output 200 (ok) / 700 (faltantes); **V5 tasa de faltantes 15 % — supuesto SIN
base empírica propia; fijar la tasa real es objetivo de la calibración**
(sensibilidad 5/15/30 % en el JSON); V6 reintento con tokens REALES de E1
fase B (variable medio 1.246, output medio 1.182, prefijo read 9.698) + 300 de
feedback; V7 un write de prefijo por corrida; V8 render de TOs no extraídos
por ratio real render/fuente = 1,857 medido en los 87 pares de pro.

| | calibración (pro) | corpus (5 TOs) |
|---|---|---|
| unidades a verificar | 87 | 1.477 |
| llamadas E3 (incl. re-verificaciones) | 100 | 1.699 |
| prefijo E3 (tokens, una vez) | 10.735 | 10.735 |
| variable E3 total (tokens) | 158.393 | 3.036.706 |
| variable E3 medio por llamada (tokens) | 1.584 | 1.787 |
| output E3 total (tokens) | 26.525 | 450.575 |
| input SIN caching (tokens) | 1.231.893 | 21.275.471 |
| input no cacheado (tokens) | 158.393 | 3.036.706 |
| cache write / cache read (tokens) | 10.735 / 1.062.765 | 10.735 / 18.228.030 |
| input equivalente CON caching | 278.088 | 4.872.928 |
| ahorro componente input | 77,4 % | 77,1 % |
| reintentos E1 (n al 15 %) | 13 | 222 |
| reintentos E1: input no cacheado / cache read / output | 20.098 / 126.074 / 15.366 | 343.212 / 2.152.956 / 262.404 |

Fórmulas parametrizadas (precios NO consultados; P\*_E3 = modelo fuerte,
P\*_E1 = modelo chico; se resuelven en la autorización de fase B):

- Calibración E3: `costo_E3 = 158.393/1e6×P_in_E3 + 10.735/1e6×P_cache_write_E3 + 1.062.765/1e6×P_cache_read_E3 + 26.525/1e6×P_out_E3`
- Calibración reintentos: `+ 20.098/1e6×P_in_E1 + 126.074/1e6×P_cache_read_E1 + 15.366/1e6×P_out_E1`
- Corpus E3: `costo_E3 = 3.036.706/1e6×P_in_E3 + 10.735/1e6×P_cache_write_E3 + 18.228.030/1e6×P_cache_read_E3 + 450.575/1e6×P_out_E3`
- Corpus reintentos: `+ 343.212/1e6×P_in_E1 + 2.152.956/1e6×P_cache_read_E1 + 262.404/1e6×P_out_E1`

**E3 es más caro por llamada que E1**, por dos vías multiplicativas: (i) más
input variable por unidad — 1.584 tokens medios (fuente ÍNTEGRO con herencia +
extracción completa renderizada) contra 1.246 reales de E1 (solo el chunk); el
prefijo leído también es mayor (≈10.735 vs 9.698); (ii) precios de modelo
fuerte en cada token. El output va en sentido contrario (veredicto ≈275 medio
vs extracción 1.182), pero no compensa el multiplicador de precios.

## 8. Límites declarados

- V4 (output) y V5 (tasa de faltantes) no tienen ancla empírica propia: la
  calibración fase B los mide; la sensibilidad de V5 está tabulada.
- Los ratios V2/V3 (2,5 chars/token para render y prefijo) son elección
  conservadora entre prosa (3,47) y JSON (2,0); el prefijo exacto se mide en
  la primera llamada real (`cache_creation_input_tokens`).
- La capa determinística verifica ANCLAJE de citas, no juicio: un faltante
  con cita real pero criterio errado (falso positivo del verificador) solo se
  detecta en la calibración con revisión humana de veredictos — es
  exactamente lo que la fase B debe medir antes del corpus.
- `ClienteE3Real` está escrito pero NO ejercitado contra la API (prohibición
  de fase A); el runner de la calibración (recorrido de los 87 pares +
  ratchet) se escribe en la fase B con la autorización.
- El tope de 1 reintento queda como constante laudada (`TOPE_REINTENTOS`);
  si la calibración muestra que un segundo reintento rescata unidades, se
  re-lauda con datos.

---

## Enmienda 01 (2026-08-11) — blanco propio por unidad + mini-recalibración pro

Implementación de `docs/enmienda_01_diseno_reextraccion_v2.md` §2.d-e y
corrida completa E0→E3 sobre pro con la arquitectura enmendada
(`salida/faseB_pro_enm01/`; la calibración sellada queda intacta).

**Cambio de armado del fuente** (`comun_e3.fuente_integro` /
`fuente_para_citas`): el blanco de completitud del hijo es su TEXTO PROPIO;
el del mini-chunk, su bloque. Del contexto heredado solo viajan los tramos
`encabezado` (títulos). **El prompt del verificador NO cambió**: los
calibradores se congelaron con `_fuente_estilo_calibracion` (réplica del
render de la calibración) y el hash del prefijo E3 quedó **INTACTO**
(`21a836c7de6d`, == `resumen_faseB_e3.json → prefijo_hash_e3` sellado). Las
keys de la caché local igual rotan (fuente y extracciones nuevas): la
verificación se pagó completa, con 1 write de prefijo de API (11.637 tok).
`TOPE_REINTENTOS = 1` sin cambio (§2.e cierra la pregunta §7.a).

**Resultados contra las predicciones de la enmienda §3** (comandos: 
`analisis_enm01.py` → `salida/faseB_pro_enm01/analisis_enm01.json`):

1. **P1 — la familia desaparece del veredicto de los hijos: CONFIRMADA.**
   0 faltantes base de hijos verifican solo-en-prosa-heredada (sellado:
   60/117 en 27 unidades). En los MINI-CHUNKS la familia NO reaparece como
   tal: 6 faltantes base en 5 de los 13 minis, y son hallazgos de completitud
   del propio bloque (no las 60 normas heredadas). Caso caracterizado:
   `pro::2.7::intro` — el extractor representó la obligación del bloque, pero
   E3 objeta (con razón formal) que la enumeración que el «:» abre no está en
   el fuente del mini: los ítems son los puntos hijos 2.7.1/2.7.2. Modo
   residual estructural de los bloques ordenadores, a laudar.
2. **P2 — cola < 10 %: REFUTADA (mejora sin perforar la meta).** Cola real
   22/101 = **21,8 %** (referencia sellada 29,9 %; caída de 8 pts = 27 %
   relativo). Composición: 19 de las 26 unidades de la cola sellada ahora
   aceptadas; solo 7 persisten; **15 unidades NUEVAS entraron en cola** (churn
   del verificador: en 18 de las 22 el último veredicto tiene SOLO faltantes
   media/baja — E3 encuentra faltantes marginales nuevos en cada pasada,
   blanco móvil). La enmienda eliminó la familia dominante pero destapó cola
   marginal que antes quedaba enmascarada.
3. **P3 — costo baja: CONFIRMADA.** Fase B total **USD 2,4823** (E1 0,775 +
   E3 1,2321 + reintentos E1 0,4752) vs sellado 2,87 (0,73 + 2,14) y vs
   estimación 2,60 (`estimacion_enm01.json`; tasa de reintentos declarada
   32/87 = 36,8 % — real: 41/101 = 40,6 %).

**Distribución por tipo de unidad** (`resumen_faseB_e3.json →
estados_por_clase`): hijos 50 ok directo / 19 aceptados tras reintento /
18+1 cola; minis 8 ok directo / 2 aceptados tras reintento / 2+1 cola.
Veredicto base: 38/88 hijos y 5/13 minis con faltantes (total 60 faltantes:
54 hijos + 6 minis; tipo dominante `otro` 26 — sellado: 58/117).
**Reintentos:** 41, todos con tope 1; 21 convirtieron (51 %). **Citas:**
92 reportadas, 7 no verificadas — tasa de fabricación 7,6 % con la capa
corregida. **Caching:** E1 re-extracción 101 misses / 1 write 9.983 /
100 reads exactos; E3 142 misses / 1 write 11.637 / reads exactos
(`cache_read` total 1.640.817 = 141×11.637); reintentos E1 41 misses /
0 writes (prefijo caliente de la corrida E1, mismo namespace rotado).

**Muestra para revisión humana**: `salida/faseB_pro_enm01/
muestra_revision_humana.txt` — extracción + veredictos completos de
`pro::2.3.1::intro` (norma de Caja de ahorros: ok directo), `pro::2.7::intro`
(cola, caso caracterizado), `pro::S3::chapeau_seccion` (ok directo),
`pro::3.1.1::intro` (aceptado tras reintento), `pro::2.4::cierre` (ok
directo), y el veredicto nuevo de `pro::2.3.1.1` (con vii)–x) en su propio:
los faltantes de la familia desaparecieron; E3 ahora marca calificadores del
texto propio y la unidad quedó en cola por blanco móvil del verificador).
