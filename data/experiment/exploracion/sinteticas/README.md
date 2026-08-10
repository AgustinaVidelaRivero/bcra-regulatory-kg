# Pipeline de queries sintéticas — Fase A (issue #3)

Implementación de la fase A del pipeline diseñado en
`docs/diseno_queries_sinteticas.md` (documento VINCULANTE): construcción +
selftest offline + estimación. **Cero llamadas LLM en esta fase**: toda pieza
que en producción llama un modelo está implementada con el llamado stubbeado e
inyectable (patrón del harness), probada offline. El gasto de generación es de
la fase B, con autorización y tope explícitos.

Insumos (solo lectura):
- Grafo vigente: `data/experiment/grafo_v2/reensamblado_v3/kg.json`
  (sha256 `26fac8b4…bff3571`, verificado en cada carga por `comun.load_kg_raw`).
- Mapa de territorio quemado de 5 sets:
  `data/experiment/exploracion/mapa_territorio_quemado_5TOs_5sets.json`.
- Regla laudada de anclas: importada de
  `data/experiment/exploracion/validar_anclas.py` (no se reimplementa).
- Tools determinísticas: importadas de `data/experiment/evaluacion/harness.py`
  (intocable; solo import).

## Archivos

| archivo | tarea | qué hace |
|---|---|---|
| `comun.py` | — | rutas, sha256, parseo location→ancla, tokenización, índice de quemado |
| `sampler.py` | T1 | muestreo estratificado determinístico (E-A…E-E) con exclusión de quemado |
| `generador.py` | T2 | prompts de generación + evolución anti-léxica; cliente inyectable; stub offline |
| `validador.py` | T3 | puertas a/b/c/d; descarte con motivo; flags `requiere_llm` |
| `metrica.py` | T4 | visto/consultado/brecha por re-ejecución determinística de tools; agregado por ancla |
| `resolucion.py` | T5 | censo ancla→nodos por grafo, con filtro de contenedores |
| `selftest.py` | T6 | selftest integral offline (37 checks) |
| `estimacion.py` | T7 | tokens medidos sobre prompts reales; fórmula parametrizada en precio/Mtok |
| `fixtures/` | T6 | golds fabricados a mano (métrica), anclas conocidas (resolución) |
| `out/` | — | `samples.json` (semilla `sinteticas-faseA-v1`), `estimacion.json` |

Correr: `python3 sampler.py` · `python3 selftest.py` · `python3 estimacion.py`
(desde este directorio; sin red).

## Decisiones de implementación (las que el diseño dejaba abiertas)

1. **Gold y censo sobre provenances completas del kg.json crudo.** La vista
   runtime del harness (adaptador nulo, patrón `run_escalon1b.py`) expone solo
   la provenance primaria; el censo usa la lista `provenances` completa. No
   afecta la métrica primaria (por ids resueltos localmente, no por citas).

2. **Parseo de ancla**: primer `Punto x.y…` del location (cobertura medida:
   6.063/6.081 provenances PDF, 99,7 %); `Sección N` → `SN`; resto sin ancla.

3. **Poblaciones de los estratos dirigidos (A-D)** excluyen: `TextoOrdenado`
   (contenedores; sus aristas `establecida_en`/`referencia`/`modificada_por`
   son estructurales — 46 % de las aristas del grafo), `Comunicacion` (anclas
   multi-punto ruidosas, hasta >20 puntos dispersos por nodo) y
   `rol_fuente == esqueleto` (sin provenance PDF). **E-E no excluye nada**:
   control uniforme sobre el grafo completo, con descartes registrados.

4. **Regla de quemado estricta**: TODAS las anclas de TODOS los nodos del
   subgrafo deben ser aptas (regla laudada incluida la de parciales-que-
   abarcan); si no, descarte con motivo registrado.

5. **Hub (E-C): grado total >= 10**, justificado con la distribución real
   (mediana 2, p95 = 4, p99 = 11; ver `distribucion_grados` en
   `out/samples.json`). Familia enumerable = mayor grupo (relation, dirección)
   con 3–25 vecinos elegibles.

6. **Cuasi-duplicados (E-D)**: mismo type, Jaccard >= 0,5 sobre tokens de
   contenido de label+descripcion (bloqueo por token con df <= 200), y
   variación de valor/calificador (token con dígito en la diferencia
   simétrica, o diferencia <= 8 tokens).

7. **Solape léxico** (puerta d y variable continua §5):
   `|tokens_contenido(pregunta) ∩ prohibidos| / |tokens_contenido(pregunta)|`,
   umbral 0,15. Tokens prohibidos = label completo de los nodos respuesta +
   tokens de descripcion con df <= 50 en el grafo (alta señal).

8. **HALLAZGO — granularidad de ancla gruesa y sus consecuencias.** Tras
   excluir contenedores, la mediana del censo es 29 nodos por ancla
   (`cap:3.1` → 212): muchas locations solo registran el punto de primer o
   segundo nivel. Consecuencias de diseño:
   - la métrica primaria agrega **por ancla** (un ancla está vista/consultada
     si algún nodo que la porta lo está): `metrica.evaluar_por_anclas`;
   - el detalle nodo a nodo queda disponible (`evaluar_traza`) para
     diagnóstico local;
   - la puerta (a) NO impone un gate de unicidad nodal (descartaría ~83 % de
     los golds por artefacto de extracción): verifica resolución y unidad de
     mapa, y reporta `censo_grande` como diagnóstico;
   - **contenedores** (nodos con >10 anclas distintas: los 5 `TextoOrdenado`,
     18–125 anclas, y 15 `Comunicacion`, 12–65) se excluyen del censo por
     defecto — incluirlos haría trivialmente "vista" cualquier ancla del TO.

9. **Métrica por re-ejecución determinística.** Las trazas persistidas
   truncan outputs de tool a 1.200 chars; las tres tools del harness son
   funciones puras del grafo y el input, así que la métrica re-ejecuta cada
   step con `harness.GraphIndex` sobre el mismo kg.json. La premisa se
   verificó contra las 25 trazas reales de `u6_exploracion/reensamblado_v3`:
   replay byte-exacto en prefijo y `output_chars` en todas (`verificar_replay`
   lo re-chequea en cada corrida).

## Qué queda para la fase B (con autorización de gasto)

- Cliente real envuelto en la caché del proyecto (skill `llm-capture` /
  `llm_cache.py`) implementando `generador.ClienteLLM`.
- Generación literal + evolución anti-léxica sobre `out/samples.json`.
- Checks LLM flaggeados por el validador (V1 autocontención, V2 unicidad del
  gold, V3 mismo-gold del par) — prompts borrador en `estimacion.py`.
- Estimación de tokens: `out/estimacion.json` (fórmula parametrizada en
  precio/Mtok; el precio se resuelve en la autorización).
