#!/bin/bash
# sha256 de las carpetas que SC1-bis puede tocar o leer de forma compartida (ESCRITURAS del texto firmado + enmienda 1 + lecturas protegidas), ordenado.
cd "$1" || exit 1
{
  find data/experiment/reextraccion_v2/corpus_tanda0 data/experiment/reextraccion_v2/manifiestos \
       data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b data/experiment/tanda0/code \
       data/experiment/reextraccion_v2/corpus_v2 data/experiment/reextraccion_v2/e2_reduce \
       data/experiment/pyd_r2/code data/experiment/reext_t0 data/experiment/catalogo_unico/generados_r2 \
       data/experiment/sincola_t0 data/experiment/r2_codigo data/experiment/mantenimiento -type f 2>/dev/null
  ls scripts/*.py scripts/regression_kg_esperado.json data/experiment/neo4j/grafos.py docs/mandatos/USINCOLA_T0_grafo_evaluado_sin_cola.md
} | grep -v "/__pycache__/" | grep -v "\.pyc$" | LC_ALL=C sort | xargs -I{} shasum -a 256 "{}"
