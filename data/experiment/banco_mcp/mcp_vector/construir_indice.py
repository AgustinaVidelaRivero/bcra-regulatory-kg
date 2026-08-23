#!/usr/bin/env python3
"""construir_indice.py — Índice vectorial local y determinístico del brazo RAG
(U-A2.0-banco, pieza ii), con `microsoft/harrier-oss-v1-0.6b` según el laudo
`docs/decision_modelo_embeddings.md` §7-§8.

Qué hace, en orden:
  1. Reconstruye los 1.763 pasajes de E0 en composición PROPIO + HERENCIA, con
     la expresión exacta de `bakeoff_embeddings/code/construir_gold_y_corpus.py`
     ("\\n".join([herencia...] + [propio]), orden canónico por id) y verifica
     cada uno contra `sha256_completo` del chunk y el corpus entero contra
     `sha256_corpus` de `resultados/meta_gold_corpus.json`. (Ese script no se
     importa porque su código corre a nivel de módulo y escribe archivos en su
     propio directorio —sellado—; la expresión de tres líneas se replica y se
     verifica por hash, que es una prueba más fuerte que el import.)
  2. Codifica los pasajes SIN prompt (asimetría declarada por los autores del
     modelo), `float32`, pooling y normalización del propio repo del modelo
     (SentenceTransformer carga 1_Pooling/2_Normalize de la revisión pinneada),
     con la MISMA agrupación por presupuesto de tokens del bake-off
     (`e3_medicion.py`: TOKEN_BUDGET=8448, GRUPO_MAX=32, batch=len(grupo),
     device MPS), para que la matriz sea byte-idéntica a la del bake-off.
  3. Persiste `indice/embeddings_docs.npy` (float32, C-order, 1763x1024),
     `indice/pasajes.json` (id, to, unidad, tipo, titulo, paginas, texto, chars,
     sha256_completo) y `indice/manifiesto_indice.json` con todos los sha.

Parámetros sellados (no son flags: cambiarlos es otra config):
  revisión f9b9dc8d367d443f2479d27aa5d8d2850c0774ee · dtype float32 ·
  max_seq_length 32768 · documentos sin prompt · consultas con prompt
  `web_search_query` (lo aplica el servidor, no este script).

El sha esperado de la matriz (`sha_docs` del bake-off para harrier) es
12d284d5bce0d1d58f1e4437c47f2177b3145813586069ca72f9103309b28b65.

Uso (venv del bake-off / requirements_vector.txt):
    python3 -B construir_indice.py [--out indice] [--max-seq 32768]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
EXPERIMENT_DIR = BANCO_DIR.parent
REPO_DIR = EXPERIMENT_DIR.parents[1]
if str(BANCO_DIR) not in sys.path:
    sys.path.insert(0, str(BANCO_DIR))
from comun_banco import rel_repo, sha256_bytes, sha256_file, versiones_entorno  # noqa: E402

E0 = EXPERIMENT_DIR / "reextraccion_v2" / "e0_chunking" / "salida_enm01"
META_BAKEOFF = EXPERIMENT_DIR / "bakeoff_embeddings" / "resultados" / "meta_gold_corpus.json"
HARRIER_BAKEOFF = EXPERIMENT_DIR / "bakeoff_embeddings" / "resultados" / "harrier.json"
TOS = ["cap", "cla", "ext", "pro", "ric"]

MODELO = "microsoft/harrier-oss-v1-0.6b"
REVISION = "f9b9dc8d367d443f2479d27aa5d8d2850c0774ee"
DTYPE = "float32"
MAX_SEQ_DEFAULT = 32768
PROMPT_CONSULTA = "web_search_query"     # SOLO consultas (servidor); documentos: ninguno
TOKEN_BUDGET = 8448                      # e3_medicion.py (bake-off), igualado
GRUPO_MAX = 32
N_ESPERADO = 1763


def sha_arr(a) -> str:
    """Misma expresión que `e3_medicion.sha_arr`."""
    return hashlib.sha256(a.astype("float32").tobytes(order="C")).hexdigest()


def construir_pasajes() -> tuple[list[dict], dict]:
    chunks = []
    insumos = {}
    for to in TOS:
        p = E0 / f"chunks_{to}.json"
        insumos[f"chunks_{to}.json"] = sha256_file(p)
        chunks.extend(json.loads(p.read_text(encoding="utf-8")))
    chunks.sort(key=lambda c: c["id"])          # orden canónico (bake-off)
    pasajes, pasajes_bakeoff = [], []
    for c in chunks:
        txt = "\n".join([h["texto"] for h in c["herencia"]] + [c["texto"]])
        if sha256_bytes(txt.encode()) != c["sha256_completo"]:
            raise SystemExit(f"ABORTO: composición propio+herencia no reproduce sha256_completo en {c['id']}")
        # forma exacta del bake-off (para verificar sha256_corpus)
        pasajes_bakeoff.append({"id": c["id"], "to": c["to"], "unidad": c["unidad"],
                                "tipo": c["tipo"], "texto": txt, "chars": len(txt)})
        pasajes.append({"id": c["id"], "to": c["to"], "archivo": c["archivo"],
                        "unidad": c["unidad"], "titulo": c["titulo"], "tipo": c["tipo"],
                        "paginas": c["paginas"], "texto": txt, "chars": len(txt),
                        "sha256_completo": c["sha256_completo"]})
    if len(pasajes) != N_ESPERADO:
        raise SystemExit(f"ABORTO: {len(pasajes)} pasajes != {N_ESPERADO}")
    sha_corpus = hashlib.sha256(json.dumps(pasajes_bakeoff, ensure_ascii=False,
                                           sort_keys=True).encode()).hexdigest()
    meta_bk = json.loads(META_BAKEOFF.read_text(encoding="utf-8"))
    if sha_corpus != meta_bk["sha256_corpus"]:
        raise SystemExit(f"ABORTO: sha256_corpus {sha_corpus} != bake-off {meta_bk['sha256_corpus']}")
    for k, v in meta_bk["insumos"].items():
        if k.startswith("chunks_") and insumos[k] != v:
            raise SystemExit(f"ABORTO: {k} cambió respecto del bake-off")
    return pasajes, {"insumos_e0": insumos, "sha256_corpus": sha_corpus,
                     "sha256_corpus_bakeoff": meta_bk["sha256_corpus"],
                     "composicion": "\"\\n\".join([herencia...] + [propio]) = E0 'completo'",
                     "verificado_contra_sha256_completo": True}


def cargar_modelo(max_seq: int):
    import torch
    from sentence_transformers import SentenceTransformer
    m = SentenceTransformer(MODELO, revision=REVISION, device="mps", trust_remote_code=False,
                            model_kwargs={"dtype": torch.float32})
    m.max_seq_length = max_seq
    return m


def grupos_por_presupuesto(tok, textos: list[str]) -> list[list[int]]:
    """Réplica exacta de `grupos` en e3_medicion.py (bake-off)."""
    largos = [len(tok(t, add_special_tokens=True)["input_ids"]) for t in textos]
    orden = sorted(range(len(textos)), key=lambda i: (largos[i], i))
    gs, cur, curmax = [], [], 0
    for i in orden:
        nm = max(curmax, largos[i])
        if cur and (len(cur) + 1) * nm > TOKEN_BUDGET or len(cur) >= GRUPO_MAX:
            gs.append(cur); cur, curmax = [i], largos[i]
        else:
            cur.append(i); curmax = nm
    if cur:
        gs.append(cur)
    return gs, largos


def codificar(m, textos: list[str], kw: dict):
    """Réplica de `encode` en e3_medicion.py: batch = grupo, normalize, float32."""
    import numpy as np
    import torch
    gs, largos = grupos_por_presupuesto(m.tokenizer, textos)
    partes = {}
    for g in gs:
        v = m.encode([textos[i] for i in g], batch_size=len(g), convert_to_numpy=True,
                     normalize_embeddings=True, show_progress_bar=False, **kw)
        for j, i in enumerate(g):
            partes[i] = v[j]
        torch.mps.empty_cache()
    return np.stack([partes[i] for i in range(len(textos))]).astype("float32"), len(gs), largos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=AQUI / "indice")
    ap.add_argument("--max-seq", type=int, default=MAX_SEQ_DEFAULT)
    a = ap.parse_args()
    import numpy as np

    t0 = time.perf_counter()
    pasajes, ver = construir_pasajes()
    print(f"pasajes: {len(pasajes)} | sha256_corpus OK ({ver['sha256_corpus'][:12]}…) | "
          f"{time.perf_counter()-t0:.1f}s")

    t0 = time.perf_counter()
    m = cargar_modelo(a.max_seq)
    t_carga = time.perf_counter() - t0
    t0 = time.perf_counter()
    E, n_grupos, largos = codificar(m, [p["texto"] for p in pasajes], {})   # SIN prompt
    t_idx = time.perf_counter() - t0
    sha_docs = sha_arr(E)
    esperado = json.loads(HARRIER_BAKEOFF.read_text(encoding="utf-8"))["extra"]["sha_docs"]
    print(f"matriz {E.shape} sha={sha_docs} | esperado bake-off {esperado} | "
          f"{'COINCIDE' if sha_docs == esperado else 'DIFIERE'} | {t_idx:.1f}s, {n_grupos} grupos")

    a.out.mkdir(parents=True, exist_ok=True)
    np.save(a.out / "embeddings_docs.npy", E)
    (a.out / "pasajes.json").write_text(json.dumps(pasajes, ensure_ascii=False), encoding="utf-8")
    prompts = dict(getattr(m, "prompts", {}) or {})
    man = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "unidad": "U-A2.0-banco — entregable 2 (índice vectorial)",
        "modelo": {"repo": MODELO, "revision": REVISION, "dtype": DTYPE,
                   "max_seq_length": m.max_seq_length, "dim": int(E.shape[1]),
                   "prompt_consultas": PROMPT_CONSULTA,
                   "prompt_consultas_texto": prompts.get(PROMPT_CONSULTA),
                   "prompt_documentos": None, "pooling_y_normalizacion": "del repo del modelo (módulos 1_Pooling / 2_Normalize), normalize_embeddings=True",
                   "device": "mps", "trust_remote_code": False},
        "agrupacion": {"token_budget": TOKEN_BUDGET, "grupo_max": GRUPO_MAX, "n_grupos": n_grupos,
                       "max_tokens_pasaje": max(largos), "n_truncados": sum(1 for L in largos if L > m.max_seq_length)},
        "entorno": versiones_entorno(["torch", "transformers", "sentence-transformers", "tokenizers", "numpy"]),
        "corpus": ver | {"n_pasajes": len(pasajes), "sha256_pasajes_json": sha256_file(a.out / "pasajes.json")},
        "matriz": {"shape": list(E.shape), "sha256_matriz": sha_docs,
                   "sha256_archivo_npy": sha256_file(a.out / "embeddings_docs.npy"),
                   "sha_docs_bakeoff": esperado, "coincide_con_bakeoff": sha_docs == esperado},
        "tiempos_s": {"carga_modelo": round(t_carga, 1), "indexacion": round(t_idx, 1)},
    }
    (a.out / "manifiesto_indice.json").write_text(json.dumps(man, ensure_ascii=False, indent=2) + "\n",
                                                  encoding="utf-8")
    print(json.dumps({k: man[k] for k in ("modelo", "agrupacion", "entorno", "matriz")}, ensure_ascii=False, indent=1))
    return 0 if sha_docs == esperado else 2


if __name__ == "__main__":
    raise SystemExit(main())
