# Leer los crudos capturados (usage, stop_reason, thinking blocks)

Cómo recuperar de las `.db` de `data/experiment/evaluacion/cache/` lo que la capa
de captura persistió. Todo lo de abajo es lectura pura: no toca la caché.

## Esquema (verificado en `data/experiment/evaluacion/llm_cache.py:132-159`)

Tabla `cache` — una fila por llamada única:

| Columna | Contenido |
|---|---|
| `key` | sha256(namespace + request canónico) |
| `namespace` | `dominio\|[gfp=…\|]cv=…\|think=0/1` |
| `domain` | `agent` / `judge` / `verificador` / … |
| `input_tokens`, `output_tokens`, `cache_read_tokens`, `cache_write_tokens` | los 4 campos, tipados |
| `stop_reason` | de la respuesta cruda |
| `request_json` | el request canónico completo (lo que se mandó) |
| `raw_json` | **`resp.model_dump()` íntegro** — acá viven los thinking blocks |

Tabla `access_log` — una fila por acceso (hit o miss), en orden de ejecución:
`ts, key, domain, hit, run_label`.

## Dónde están los thinking blocks

En `raw_json → content[]`: los bloques con `"type": "thinking"` traen `thinking`
(el texto del razonamiento) y `signature`. Solo existen en llamadas hechas con
thinking ON, es decir bajo namespaces `…|think=1`.

## Patrón 1 — turnos de una corrida en curso (en proceso Python)

El patrón canónico es `_max_access_rowid` + `_turns_since`
(`data/experiment/evaluacion/run_posthoc.py:163-180`): tomar el
rowid máximo de `access_log` ANTES de la operación, y después leer los accesos
posteriores del dominio, resolviendo cada `key` contra `cache.raw_json`. Así
`run_posthoc` arma `raw_turns_agent` / `raw_turns_judge` por repetición
(`data/experiment/evaluacion/run_posthoc.py:186-217`).

## Patrón 2 — lectura post-hoc por SQL (db existente)

```python
import sqlite3, json
conn = sqlite3.connect("cache/calls.db"); conn.row_factory = sqlite3.Row

# llamadas de una corrida etiquetada, en orden:
rows = conn.execute("""
    SELECT a.rowid, a.hit, c.stop_reason, c.raw_json
    FROM access_log a JOIN cache c ON c.key = a.key
    WHERE a.run_label = ? AND a.domain = ? ORDER BY a.rowid""",
    ("off", "agent")).fetchall()

for r in rows:
    raw = json.loads(r["raw_json"])
    thinking = [b["thinking"] for b in raw["content"] if b.get("type") == "thinking"]
```

Filtro por condición thinking sin depender del `run_label`: el sufijo del
namespace. Precedente real en `data/experiment/evaluacion/verifier_pilot.py:103-104`:

```sql
SELECT request_json FROM cache
WHERE domain='agent' AND namespace LIKE 'agent|gfp=<gfp>|%think=1'
```

(`<gfp>` sale de `lc.graph_fingerprint(load_graph("run_X"))`.)

## Patrón 3 — lectores de alto nivel ya construidos (no reimplementar)

- `verifier_pilot.load_rep(label, run, qid)` — carga la repetición completa de una
  pregunta desde `posthoc_run/traces/{label}/{run}/{qid}.json`
  (`data/experiment/evaluacion/verifier_pilot.py:78`).
- `verifier_pilot.recover_seen(run, label, pregunta)` — reconstruye desde
  `calls.db` el contenido ÍNTEGRO (sin truncar) de los nodos que el agente vio,
  filtrando por el `think` correcto (`data/experiment/evaluacion/verifier_pilot.py:97`).
  Es lo que consume el verificador (`data/experiment/evaluacion/verificador.py:37`).

## Advertencias

- `request_json`/`raw_json` de trazas con `think=1` contienen razonamiento del
  modelo: tratarlos como material de análisis interno, no pegarlos enteros en
  reportes sin necesidad.
- Los hits reconstruyen el MISMO objeto `anthropic.types.Message` que un miss
  (`data/experiment/evaluacion/llm_cache.py:205-211`): aguas
  arriba no se distingue — para saber si algo se pagó o se replayó, mirar
  `access_log.hit`, no la respuesta.
- Cada dominio puede vivir en una `.db` distinta (`calls.db`, `verificador.db`,
  `verifier_pilot.db`) — verificá contra el script que la escribió antes de asumir
  dónde buscar.
