#!/usr/bin/env python3
"""Entregable 2: recuento de truncamiento por modelo, con el AutoTokenizer de
CADA modelo, sobre los 1.763 pasajes de E0 (composicion declarada: completo).
No carga pesos: solo tokenizadores."""
import json, os, collections
from transformers import AutoTokenizer

SP = os.path.dirname(os.path.abspath(__file__))
pasajes = json.load(open(os.path.join(SP, "corpus_pasajes.json")))
textos = [p["texto"] for p in pasajes]

# ventana maxima DECLARADA por cada modelo (fuente citada en el reporte)
MODELOS = [
    ("qwen3",   "Qwen/Qwen3-Embedding-0.6B",                            32768),
    ("granite", "ibm-granite/granite-embedding-311m-multilingual-r2",   32768),
    ("harrier", "microsoft/harrier-oss-v1-0.6b",                        32768),
    ("f2llm",   "codefuse-ai/F2LLM-v2-0.6B",                            40960),
    ("jina",    "jinaai/jina-embeddings-v5-text-small",                 32768),
]

filas = []
for clave, repo, ventana in MODELOS:
    tok = AutoTokenizer.from_pretrained(repo, trust_remote_code=(clave == "jina"))
    largos = [len(tok(t, add_special_tokens=True)["input_ids"]) for t in textos]
    n = len(largos); s = sorted(largos)
    peor = max(range(n), key=lambda i: largos[i])
    fila = {
        "modelo": clave, "repo": repo, "tokenizer_class": type(tok).__name__,
        "vocab_size": tok.vocab_size, "ventana_declarada": ventana,
        "chunks_truncados": sum(1 for x in largos if x > ventana),
        "pct_corpus": round(100 * sum(1 for x in largos if x > ventana) / n, 3),
        "mayor_chunk_tokens": s[-1], "mayor_chunk_id": pasajes[peor]["id"],
        "p50": s[n // 2], "p90": s[int(n * .9)], "p99": s[int(n * .99)],
        "excede_512": sum(1 for x in largos if x > 512),
        "excede_1024": sum(1 for x in largos if x > 1024),
        "excede_4096": sum(1 for x in largos if x > 4096),
        "excede_16384": sum(1 for x in largos if x > 16384),
        "total_tokens_corpus": sum(largos),
    }
    filas.append(fila)
    print(json.dumps(fila, ensure_ascii=False))

json.dump(filas, open(os.path.join(SP, "e2_truncamiento.json"), "w"), ensure_ascii=False, indent=1)
print("\nMAX de mayor_chunk_tokens entre modelos:", max(f["mayor_chunk_tokens"] for f in filas))
