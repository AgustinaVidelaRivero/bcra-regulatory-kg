# Agregar una clave a RUN_FILES — procedimiento e implicancias sobre la caché

> **Estado verificado:** citas `archivo:línea` verificadas contra el repo el
> 2026-07-06 (HEAD `454bd9d`, 2026-06-28, más working tree sin commitear).
> Si `loader.py` se editó después de esa fecha, ejecutar primero el paso 6 del
> checklist antes de confiar en los números de línea.

Sub-procedimiento compartido: lo citan la skill `llm-capture` y la skill
`kg-refinement` (preparación de la copia de refinamiento). Aplica cada vez que se
incorpora una fuente de datos nueva al pipeline (una copia de trabajo de un grafo,
un grafo re-extraído, un corpus expandido).

## Por qué hace falta tocar loader.py

`load_graph(run_key)` solo acepta claves declaradas: tira `KeyError` para
cualquier otra (`data/experiment/evaluacion/loader.py:253-255`).
Las claves viven en dos dicts que hay que editar JUNTOS:

- `RUN_FILES` — clave → ruta del `kg.json` (`data/experiment/evaluacion/loader.py:57-64`).
- `ADAPTERS` — clave → config de provenance extra por run (`data/experiment/evaluacion/loader.py:68-79`).
  Para una copia byte-idéntica de un run existente, copiá el adapter del run de
  origen (p. ej. para una copia de run_3: `{"node_extra": ("top", "additional_provenance"), "edge_extra": None}`,
  `data/experiment/evaluacion/loader.py:73-74`).

## Implicancia 1 — editar loader.py invalida TODA la caché automática

`loader.py` integra `_SOURCE_FILES`, cuyo hash compone `code_version`
(`data/experiment/evaluacion/llm_cache.py:49`, `data/experiment/evaluacion/llm_cache.py:58-68`).
Cualquier edición — incluso agregar una clave — cambia `cv=` en el namespace y
**rota los namespaces de los dominios `agent` y `judge` completos**: todo lo
cacheado queda stale y una re-corrida re-paga desde cero. Es una decisión firmada
("se prefiere re-pagar ante un cambio cosmético antes que comer un hit stale",
`data/experiment/evaluacion/llm_cache.py:24-26`), no un bug.

**Regla operativa:** la edición se hace UNA vez, planificada, ANTES de acumular
corridas caras sobre el estado actual del código — nunca "de paso" en medio de una
fase de corridas. Las entradas viejas no se borran de la `.db` (quedan bajo su
namespace anterior); no limpiar sin decisión de la autora.

## Implicancia 2 — dominios con CODE_VER manual NO rotan

El verificador usa `CODE_VER = "verificador-v3"` manual, no el hash
(`data/experiment/evaluacion/verificador.py:49`): editar
`loader.py` NO invalida `verificador.db`. Simétricamente, editar `verificador.py`
tampoco — ahí el bump del string es responsabilidad de quien edita.

## Implicancia 3 — LOADER_VERSION solo si cambia la normalización

`graph_fingerprint = sha256(LOADER_VERSION + bytes del kg.json)`
(`data/experiment/evaluacion/llm_cache.py:71-81`). `LOADER_VERSION`
se bumpea SOLO si cambia la normalización en memoria (merges, descarte de campos —
`data/experiment/evaluacion/llm_cache.py:42-45`). **Agregar una
clave NO es un cambio de normalización**: no bumpear.

## Implicancia 4 — una copia byte-idéntica COMPARTE fingerprint con el original

Mientras la copia no difiera del original ni en un byte, su `graph_fingerprint` es
idéntico → el dominio `agent` de ambas cae en el MISMO namespace. Consecuencias:

- A favor: correr sobre la copia recién creada replaya gratis lo ya cacheado del
  original.
- En contra: hasta el primer cambio real de contenido, un "side-by-side
  original vs copia" compara literalmente los mismos bytes de respuesta — no
  afirmar diferencias (ni igualdades "demostradas") sobre esa base.

Recién cuando la copia se edita, su fingerprint diverge y nace el namespace
separado que la comparación baseline/refinado necesita.

## Efectos colaterales de agregar la clave (verificados)

`RUN_KEYS = list(RUN_FILES.keys())` (`data/experiment/evaluacion/loader.py:64`),
así que la clave nueva entra automáticamente en todo lo que itera `RUN_KEYS`:

- `runners/validate_loader.py` la valida con los checks C1–C8 en su próxima corrida
  (`data/experiment/evaluacion/runners/validate_loader.py:180`) — deseable.
- `runners/run_posthoc.py --run all` ahora la INCLUYE (`data/experiment/evaluacion/runners/run_posthoc.py:542`) —
  ojo con corridas "all" que asumían 5 grafos.
- `run_frozen.py` NO se ve afectado: usa `GRAPH_ORDER` hardcodeado a los 5 runs
  (`data/experiment/evaluacion/run_frozen.py:106`).

## Checklist de ejecución

1. Crear la carpeta y copiar el `kg.json` fuente; registrar sha256 de origen y
   copia (deben coincidir) y fecha, en un log dentro de la carpeta nueva.
2. Editar `RUN_FILES` + `ADAPTERS` en el mismo cambio (adapter del run de origen).
3. Correr `python runners/validate_loader.py` desde `data/experiment/evaluacion/`:
   la clave nueva debe pasar C1–C8 (exit code 0).
4. Smoke barato del cableado: `python runners/run_posthoc.py --selftest` (offline; carga
   run_3 pero verifica que loader+cadena siguen sanos tras la edición).
5. Registrar en el reporte de la sesión: diff de `loader.py`, nuevo `code_version`
   (`python -c "import llm_cache as lc; print(lc.code_version())"`), y qué
   namespaces quedaron invalidados.
6. **Mantenimiento de citas (obligatorio tras editar `loader.py`):** actualizar
   las citas `archivo:línea` que apunten a `loader.py` en esta reference y en el
   `SKILL.md` de `llm-capture` (la edición corre los números de línea), y
   actualizar la nota de "Estado verificado" del encabezado con la fecha y el
   commit del nuevo estado.
