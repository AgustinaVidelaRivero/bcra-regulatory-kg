### Regla R2 — n = 100 casos (50 literal + 50 anti-lexica)

| modelo | lit@1 | lit@5 | lit@10 | anti@1 | anti@5 | anti@10 | brecha @1 | brecha @10 | ambas@1 |
|---|---|---|---|---|---|---|---|---|---|
| bm25 *(control)* | 72% | 86% | 86% | 16% | 34% | 46% | +56 pp | +40 pp | 44% |
| granite | 46% | 60% | 68% | 22% | 36% | 44% | +24 pp | +24 pp | 34% |
| qwen3 | 44% | 64% | 68% | 24% | 46% | 48% | +20 pp | +20 pp | 34% |
| harrier | 52% | 72% | 76% | 36% | 50% | 56% | +16 pp | +20 pp | 44% |
| f2llm | 46% | 58% | 68% | 16% | 38% | 46% | +30 pp | +22 pp | 31% |
| jina *(no elegible)* | 46% | 66% | 70% | 28% | 42% | 50% | +18 pp | +20 pp | 37% |

### Regla control — n = 30 casos (15 literal + 15 anti-lexica)

| modelo | lit@1 | lit@5 | lit@10 | anti@1 | anti@5 | anti@10 | brecha @1 | brecha @10 | ambas@1 |
|---|---|---|---|---|---|---|---|---|---|
| bm25 *(control)* | 60% | 73% | 73% | 0% | 13% | 13% | +60 pp | +60 pp | 30% |
| granite | 40% | 53% | 53% | 27% | 33% | 40% | +13 pp | +13 pp | 33% |
| qwen3 | 33% | 53% | 60% | 20% | 40% | 47% | +13 pp | +13 pp | 27% |
| harrier | 40% | 60% | 60% | 20% | 40% | 40% | +20 pp | +20 pp | 30% |
| f2llm | 40% | 53% | 60% | 13% | 40% | 47% | +27 pp | +13 pp | 27% |
| jina *(no elegible)* | 33% | 60% | 67% | 20% | 33% | 33% | +13 pp | +33 pp | 27% |

### Truncamiento, tiempo de indexacion, licencia, ventana

| modelo | licencia | params | ventana declarada | chunks truncados | % corpus | mayor chunk (tok de ESE tokenizador) | t. indexacion (s) | dim |
|---|---|---|---|---|---|---|---|---|
| bm25 *(control lexico)* | — | — | — | no aplica | — | — | 0.2 | — |
| granite | Apache-2.0 | 312M | 32.768 | 0 | 0.0% | 7498 | 103.8 | 768 |
| qwen3 | Apache-2.0 | 596M | 32.768 | 0 | 0.0% | 8233 | 804.3 | 1024 |
| harrier | MIT | 596M | 32.768 | 0 | 0.0% | 8233 | 427.9 | 1024 |
| f2llm | Apache-2.0 | 596M | 40.960 | 0 | 0.0% | 8233 | 435.8 | 1024 |
| jina | CC-BY-NC-4.0 | 596M | 32.768 | 0 | 0.0% | 8232 | 491.9 | 1024 |

### Determinismo (doble corrida del pipeline de consulta)

| modelo | embeddings de consulta byte-identicos | rankings identicos |
|---|---|---|
| granite | si | si |
| qwen3 | si | si |
| harrier | si | si |
| f2llm | si | si |
| jina | si | si |
| bm25 | no aplica (sin modelo) | deterministico por construccion |

### Criterio de lectura declarado ex ante

- **recall@1 ambas** — orden bajo R2: `bm25=harrier > granite=qwen3 > f2llm`
  orden bajo control: `granite > bm25=harrier > f2llm=qwen3`
  parejas invertidas entre reglas: **2** → bm25 vs granite (+10 pp R2 / -3 pp control); granite vs harrier (-10 pp R2 / +3 pp control)
- **recall@1 literal** — orden bajo R2: `bm25 > harrier > f2llm=granite > qwen3`
  orden bajo control: `bm25 > f2llm=granite=harrier > qwen3`
  parejas invertidas entre reglas: **0**
- **recall@1 antilexica** — orden bajo R2: `harrier > qwen3 > granite > bm25=f2llm`
  orden bajo control: `granite > harrier=qwen3 > f2llm > bm25`
  parejas invertidas entre reglas: **2** → granite vs qwen3 (-2 pp R2 / +7 pp control); granite vs harrier (-14 pp R2 / +7 pp control)
