# `code/` — Run 1: Cookbook de Anthropic

Pipeline de 6 etapas (5 ejecutadas en este run, multi-hop omitido por protocolo).

## Estructura

| Script | Etapa del cookbook | Modelo | Output |
|---|---|---|---|
| `01_load_corpus.py` | 1. Document Corpus Building | — | `cache/chunks.jsonl` |
| `02_extract.py` | 2. Entity & Relation Extraction | Haiku 4.5 | `cache/raw_extractions.jsonl` + `cache/cost_extraction.json` |
| `03_resolve.py` | 3. Entity Resolution | Sonnet 4.6 | `cache/alias_to_canonical.json` + `cache/canonical_info.json` + `cache/cost_resolution.json` |
| `04_assemble.py` | 4. Graph Assembly | — | `../kg.json` (versión sin hub summaries) |
| `05_hub_summarize.py` | 5. Hub Summarization | Sonnet 4.6 | enriquece `../kg.json` con `properties.summary` y `properties.key_facts` en nodos hub + `cache/cost_summarization.json` |
| `06_validate_and_report.py` | — (build-side) | — | `../report.md` |
| `07_visualize.py` | — (fuera del cookbook, ayuda de inspección) | — | `../kg_visual.html` (pyvis, force-directed, nodos por type) |

Multi-hop querying (etapa 6 del cookbook) NO se ejecuta. Es evaluación, va a la FASE 2.3.

## Cómo ejecutar

```bash
cd data/experiment/run_1_cookbook/code
pip install -r requirements.txt
export ANTHROPIC_API_KEY=sk-ant-...

python 01_load_corpus.py
python 02_extract.py            # gasta API
python 03_resolve.py            # gasta API
python 04_assemble.py
python 05_hub_summarize.py      # gasta API
python 06_validate_and_report.py
python 07_visualize.py          # local, abrí kg_visual.html en el browser
```

Todos los scripts son **idempotentes**: re-correrlos no duplica trabajo si `cache/*` ya está poblado, salvo que se pase `--force`.

## Presupuesto

Presupuesto duro: **USD 5** (regla del protocolo). El acumulador vive en `cache/cost_*.json` por etapa; `common.py:assert_under_budget()` aborta cualquier script si el total supera USD 4.50 (margen de seguridad).
