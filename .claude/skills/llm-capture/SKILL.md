---
name: llm-capture
description: Patrón obligatorio de este repo para llamar a la API Anthropic capturando el crudo íntegro (incluidos thinking blocks) y sin pagar dos veces la misma llamada, vía CachingClient + namespace versionado (llm_cache.py, Fase 2.3+). Usala SIEMPRE que (1) vayas a escribir un script nuevo que llame a la API dentro del proyecto — el script nace envuelto en la caché, no se agrega después; (2) el usuario diga "capturá el thinking", "guardá los crudos", "quiero ver el razonamiento del modelo", "prendé thinking"; (3) pregunte "¿por qué no veo los thinking blocks?", "¿esto se está cacheando?", "¿cuánto costó re-correr?"; (4) haya que agregar un dominio nuevo a la caché (otro agente, otro juez, otro verificador) o extender RUN_FILES a una fuente nueva; (5) algo parezca re-pagar llamadas ya hechas o la caché dé hits stale. Disparala aunque el pedido suene chico ("hacé un scriptcito que le pregunte X al modelo"): en este repo NO existen llamadas a la API sin captura.
---

# Captura de outputs LLM + caché persistente (Fase 2.3+)

Todo lo que llama a la API Anthropic en este proyecto pasa por la capa de
`data/experiment/evaluacion/llm_cache.py`. Garantiza dos cosas
(docstring, `data/experiment/evaluacion/llm_cache.py:9-19`):

1. **Nothing-dropped**: se persiste el objeto crudo completo de cada respuesta
   (`resp.model_dump(mode="json")` — usage con los 4 campos de tokens, stop_reason,
   `content[]` incluidos thinking blocks con su `signature`), capturado ANTES de
   que cualquier código aguas arriba recorte (`data/experiment/evaluacion/llm_cache.py:311`).
2. **Never-pay-twice**: caché SQLite write-through; la key es un hash del request
   real canónico, namespaced. Un kill no pierde lo pagado (`data/experiment/evaluacion/llm_cache.py:313-320`).

**Regla dura del repo:** un script nuevo que llama a la API nace envuelto en
`CachingClient`. No se escribe "primero sin caché y después la agrego" — eso ya
costó dinero real en el proyecto. El precedente a imitar es
`data/experiment/evaluacion/verificador.py` (Fase 2.4), que nació cableado así.

## Entorno (prerrequisitos verificados)

- Python: el venv de la raíz del repo (`.venv/bin/python`, Python 3.10).
- API key: `ANTHROPIC_API_KEY` en `data/experiment/evaluacion/.env`
  (los scripts la cargan con `load_dotenv(EVAL_DIR / ".env")` y abortan si falta,
  p. ej. `data/experiment/evaluacion/runners/run_posthoc.py:283-285`).
- Directorio de trabajo de todos los comandos de esta skill:
  `data/experiment/evaluacion/`.

## El patrón canónico (cadena de clientes)

Referencia: `build_clients` en `data/experiment/evaluacion/runners/run_posthoc.py:123-155`.

```
código de negocio ─▶ ParamOverrideClient ─▶ CachingClient ─▶ cliente real (SDK, retries)
                     (solo si hay overrides)  (caché+captura)   anthropic.Anthropic(max_retries=3)
```

```python
import llm_cache as lc

real  = anthropic.Anthropic(max_retries=3)          # retry nativo del SDK
cache = lc.CachingClient(
    real,
    domain="mi_dominio",
    db_path=DB_PATH,                                # ver "Dominio nuevo" abajo
    namespace=lc.make_namespace("mi_dominio", code_ver=..., graph_fp=..., thinking=...),
    thinking_enabled=..., run_label="...")
client = cache                                      # drop-in: expone .messages.create(**kwargs)
```

Reglas de orden que NO se alteran:

- **El override va POR ENCIMA de la caché**, nunca abajo: así la key refleja el
  request REAL que viaja por el cable (`data/experiment/evaluacion/runners/run_posthoc.py:16-22`).
- **La caché va POR FUERA del retry**: un hit ni siquiera entra a la red
  (`data/experiment/evaluacion/llm_cache.py:230-231`).
- **Los errores NO se cachean**: un miss que falla propaga la excepción sin
  guardar nada (`data/experiment/evaluacion/llm_cache.py:310`).
- **NO importar `run_frozen.RetryingClient`** para esto: su import aplica un
  monkeypatch global a `judge._call` (`data/experiment/evaluacion/runners/run_posthoc.py:287-290`).
  Usá el retry nativo del SDK.

## Reglas de namespace (qué invalida qué)

`make_namespace(domain, code_ver, graph_fp, thinking)` particiona la caché
(`data/experiment/evaluacion/llm_cache.py:84-91`):

| Componente | Regla | Fuente |
|---|---|---|
| `domain` | uno por rol ("agent", "judge", "verificador", …) | `data/experiment/evaluacion/llm_cache.py:26` |
| `cv=` (code_version) | hash automático de `harness.py`+`judge.py`+`loader.py`: **editar cualquiera de los tres invalida TODA la caché** de los dominios que lo usan | `data/experiment/evaluacion/llm_cache.py:49`, `data/experiment/evaluacion/llm_cache.py:58-68` |
| `gfp=` (graph_fingerprint) | sha256(kg.json) + `LOADER_VERSION`; SOLO para dominios que consumen grafo (el juez no lo lleva) | `data/experiment/evaluacion/llm_cache.py:71-81`, `data/experiment/evaluacion/runners/run_posthoc.py:142-145` |
| `think=0/1` | siempre presente; cachés thinking-ON y OFF nunca se cruzan | `data/experiment/evaluacion/llm_cache.py:21-22` |

Implicancia operativa: **planificá las ediciones a harness/judge/loader ANTES de
acumular corridas caras** — un cambio cosmético re-paga todo (decisión firmada:
"se prefiere re-pagar antes que comer un hit stale", `data/experiment/evaluacion/llm_cache.py:24-25`).
El caso concreto "agregar una clave a RUN_FILES" está en
`references/extender-run-files.md` — leelo antes
de tocar `loader.py`.

## Checklist: dominio nuevo (imitar verificador.py)

Cuando aparece un rol nuevo que llama a la API:

1. **`.db` propia** si el volumen/ciclo de vida difiere del pipeline principal:
   `calls.db` (agente+juez), `verificador.db`, `verifier_pilot.db` conviven en
   `evaluacion/cache/` (`data/experiment/evaluacion/verificador.py:48`, `data/experiment/evaluacion/verifier_pilot.py:36`).
2. **`CODE_VER` manual versionado a mano** si el comportamiento del dominio lo
   define el script nuevo y no los fuentes hasheados: el verificador usa
   `CODE_VER = "verificador-v3"` y documenta cada bump en el propio string
   (`data/experiment/evaluacion/verificador.py:49`). Ojo: con CODE_VER manual,
   **editar tu script NO invalida la caché solo** — bumpeá vos al cambiar prompts/lógica.
3. **`graph_fp` solo si consume grafo**, con guard de `kg.path` que aborta
   ruidosamente si falta (`data/experiment/evaluacion/verificador.py:392-396`).
4. Factory dedicada tipo `build_verificador_client`
   (`data/experiment/evaluacion/verificador.py:390-400`).

## Thinking ON

No se tocan los módulos congelados: se intercala `ParamOverrideClient` con
`make_thinking_transform(budget)` (`data/experiment/evaluacion/runners/run_posthoc.py:88-99`), que:

- agrega `thinking={"type": "enabled", "budget_tokens": budget}`,
- **quita `temperature`** (thinking clásico en Haiku 4.5 no admite temperature custom),
- sube `max_tokens` a `base + budget` (garantiza budget < max_tokens sin comerle
  espacio a la respuesta).

Presupuestos vigentes (tunables, se validan con `--preflight`):
`AGENT_THINK_BUDGET = 4000`, `JUDGE_THINK_BUDGET = 6000`
(`data/experiment/evaluacion/runners/run_posthoc.py:67-68`).

Peculiaridades por modelo YA pagadas (no redescubrir):

- **Opus 4.8 rechaza `temperature`** — no pasarla nunca (`data/experiment/evaluacion/verificador.py:43`, `data/experiment/evaluacion/verificador.py:324`).
- **Prompt-cache de Haiku 4.5: mínimo cacheable 4096 tokens** — un prefijo menor
  da `cache_read+cache_write = 0` legítimo, no es bug (`data/experiment/evaluacion/harness.py:401-404`, y el preflight lo reporta como INFO/WARN, `data/experiment/evaluacion/runners/run_posthoc.py:333-336`).
- Criterio de corrida sana con thinking: `stop_reason == "end_turn"`; si sale
  `max_tokens` el JSON final se cortó → subir budget/base y repetir preflight
  (`data/experiment/evaluacion/runners/run_posthoc.py:297-306`).

## Recuperar los crudos capturados (incl. thinking)

Los thinking blocks viven en la columna `raw_json` de la tabla `cache`; el orden
de llamadas por corrida está en `access_log`. El patrón de lectura por turno es
`_max_access_rowid` + `_turns_since` (`data/experiment/evaluacion/runners/run_posthoc.py:163-180`).
Detalle (esquema SQL, queries listas, filtro por `think=0/1`) en
`references/leer-crudos.md`.

## Non-goals

- **`harness.py`, `judge.py` y `run_frozen.py` no se modifican NUNCA.**
  `loader.py` únicamente vía el procedimiento de
  `references/extender-run-files.md`, una sola
  vez, con aprobación explícita de la autora. Cualquier override de parámetros va
  por `ParamOverrideClient`, no por edición de los módulos.
- **NO decide presupuestos de thinking nuevos**: documenta los vigentes; cambiarlos
  es decisión de la autora, validada con `--preflight`.
- **NO analiza ni interpreta** los crudos capturados (eso es trabajo del
  verificador / del análisis de trazas, no de esta skill).
- **NO borra ni migra `.db` existentes**: la invalidación es por namespace (las
  entradas viejas quedan; no se limpian sin decisión de la autora).
- **NO commits** — los maneja la autora.

## Self-check (ejecutable, sin API)

Desde `data/experiment/evaluacion/`, con el venv de la raíz:

```bash
python tests/test_llm_cache.py          # capa de caché: 32 checks (7 tests), PASS/FAIL por check
python runners/run_posthoc.py --selftest  # cadena completa + replay multi-turno: 14 checks, cliente falso
```

Ambos son offline y gratis; terminan con `RESULTADO: PASS ✅` y exit code 0
(`data/experiment/evaluacion/tests/test_llm_cache.py:299-325`, `data/experiment/evaluacion/runners/run_posthoc.py:503-509`).
Si el cableado nuevo involucra thinking real, el paso siguiente (con API, ~centavos)
es `python runners/run_posthoc.py --preflight --run run_3 --thinking` y
`python runners/run_posthoc.py --verify-replay --thinking` (usa una caché temporal aislada,
no ensucia producción — `data/experiment/evaluacion/runners/run_posthoc.py:376-384`).
