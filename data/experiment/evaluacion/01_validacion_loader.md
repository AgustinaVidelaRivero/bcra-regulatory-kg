# Validación del loader — Fase 2.3

Generado por `evaluacion/validate_loader.py` cargando los 5 grafos vía `evaluacion/loader.py`. Los conteos crudos se recomputan de forma independiente reabriendo cada `kg.json` con `json.load`. Los `kg.json` no se modifican.

**Resultado global: ✅ TODOS LOS CHECKS PASAN**

## Resumen por run

| Run | Nodos cargados | Edges cargados | Merges (grupos / instancias) | Provenances nodo | Provenances edge | Checks |
|-----|---------------:|---------------:|------------------------------|-----------------:|-----------------:|:------:|
| run_1 | 4014 | 4287 | 0 / 0 | 6980 | 4330 | ✅ |
| run_2 | 6214 | 5680 | 0 / 0 | 7304 | 5728 | ✅ |
| run_3 | 4050 | 6634 | 0 / 0 | 4064 | 6634 | ✅ |
| run_4 | 3298 | 3434 | 0 / 0 | 4393 | 3434 | ✅ |
| run_5 | 5932 | 5764 | 145 / 163 | 6093 | 5764 | ✅ |

## Verificación de conteos post-normalización vs. crudos

| Run | Nodos crudos (json) | Ids únicos | Instancias absorbidas | Nodos finales | Identidad verificada |
|-----|--------------------:|-----------:|----------------------:|--------------:|----------------------|
| run_1 | 4014 | 4014 | 0 | 4014 | 4014 − 0 = 4014 ✅ |
| run_2 | 6214 | 6214 | 0 | 6214 | 6214 − 0 = 6214 ✅ |
| run_3 | 4050 | 4050 | 0 | 4050 | 4050 − 0 = 4050 ✅ |
| run_4 | 3298 | 3298 | 0 | 3298 | 3298 − 0 = 3298 ✅ |
| run_5 | 6095 | 5932 | 163 | 5932 | 6095 − 163 = 5932 ✅ |

> Run 5 es el único con merges: **6.095 − 163 = 5.932** nodos esperados, que coincide con los 5.932 `id` únicos del json crudo.

## Detalle de checks por run

| Run | C1 | C2 | C3 | C4 | C5 | C6 | C7 | C8 |
|-----|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| run_1 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| run_2 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| run_3 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| run_4 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| run_5 | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |

Leyenda de checks:
- `C1 raw_node_count==json`
- `C2 raw_edge_count==json`
- `C3 len(nodes)==ids_unicos`
- `C4 len(nodes)==raw-absorbidas`
- `C5 len(edges)==raw_edges`
- `C6 edges_sin_colgantes`
- `C7 nodos_con_provenance`
- `C8 edges_con_provenance`

## Logs de merge

- **run_5**: 145 grupos mergeados, 163 instancias absorbidas → `experiment/evaluacion/logs/run5_merges.json`

## Provenances

Provenances totales normalizadas (source_doc + location, deduplicadas): **28834** en nodos y **25890** en edges, sumando los 5 grafos. Todos los nodos finales tienen ≥1 provenance (C7) y todos los edges finales tienen ≥1 provenance (C8).
