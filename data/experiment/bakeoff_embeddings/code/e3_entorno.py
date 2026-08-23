#!/usr/bin/env python3
"""Captura del entorno de ejecucion y de las revisiones exactas de cada repo
de modelo. Se corre al final, con el cache ya poblado."""
import json, os, platform, subprocess, sys
SP = os.path.dirname(os.path.abspath(__file__))
import torch, transformers, sentence_transformers, numpy, peft, tokenizers
from huggingface_hub import HfApi

REPOS = {"qwen3": "Qwen/Qwen3-Embedding-0.6B",
         "granite": "ibm-granite/granite-embedding-311m-multilingual-r2",
         "harrier": "microsoft/harrier-oss-v1-0.6b",
         "f2llm": "codefuse-ai/F2LLM-v2-0.6B",
         "jina": "jinaai/jina-embeddings-v5-text-small"}
api = HfApi()
cache = os.path.expanduser("~/.cache/huggingface")
du = subprocess.run(["du", "-sh", cache], capture_output=True, text=True).stdout.split()[0]
info = {
  "maquina": {"platform": platform.platform(), "machine": platform.machine(),
              "python": sys.version.split()[0],
              "mps_disponible": torch.backends.mps.is_available(),
              "mps_construido": torch.backends.mps.is_built()},
  "librerias": {"torch": torch.__version__, "transformers": transformers.__version__,
                "sentence_transformers": sentence_transformers.__version__,
                "tokenizers": tokenizers.__version__, "peft": peft.__version__,
                "numpy": numpy.__version__},
  "venv": os.path.join(SP, "venv_bakeoff"),
  "cache_huggingface": {"ruta": cache, "fuera_del_repo": True, "peso": du},
  "modelos": {k: {"repo": r, "revision_sha": api.model_info(r).sha,
                  "licencia": (api.model_info(r).cardData or {}).get("license")}
              for k, r in REPOS.items()},
  "costo_api_usd": 0.0,
}
json.dump(info, open(os.path.join(SP, "e3_entorno.json"), "w"), ensure_ascii=False, indent=1)
print(json.dumps(info, ensure_ascii=False, indent=1))
