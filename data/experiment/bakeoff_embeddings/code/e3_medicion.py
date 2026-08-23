#!/usr/bin/env python3
"""Entregable 3: indexacion y medicion. Un modelo por invocacion (checkpoint en
disco por modelo). Uso: e3_medicion.py <clave_modelo|bm25>"""
import json, os, sys, time, hashlib, unicodedata, re, math, collections

SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SP, "e3_resultados"); os.makedirs(OUT, exist_ok=True)

# ---------------- constantes igualadas entre modelos (declaradas) ----------
MAX_SEQ = 16384        # unica politica de truncado: > pasaje mas largo (8.233 tok)
                       # y < ventana declarada mas chica (32.768) => 0 truncamientos
# Agrupamiento por PRESUPUESTO DE TOKENS, no por cantidad fija de textos: los
# grupos se arman ordenando por longitud (con el tokenizador de CADA modelo) de
# modo que len(grupo) * max_len(grupo) <= TOKEN_BUDGET y len(grupo) <= GRUPO_MAX.
# Un texto mas largo que el presupuesto va solo. Motivo: con batch fijo de 16 el
# pasaje de 8.233 tokens hace estallar la memoria de MPS (medido: intento de
# reservar 4,04 GiB sobre 18,13 GiB permitidos, con qwen3). El agrupamiento es
# determinista y el MISMO criterio para los cinco modelos; el padding no cambia
# la salida de un transformer con mascara de atencion correcta, solo el tiempo.
TOKEN_BUDGET = 8448
GRUPO_MAX = 32
BATCH = "token_budget=8448, grupo_max=32"
TOPK = 10
DTYPE = "float32"      # precision numerica unica para los 5 modelos

MODELOS = {
  "qwen3":   dict(repo="Qwen/Qwen3-Embedding-0.6B",
                  q=dict(prompt_name="query"), d=dict(prompt_name="document"), trc=False),
  "granite": dict(repo="ibm-granite/granite-embedding-311m-multilingual-r2",
                  q=dict(prompt_name="query"), d=dict(prompt_name="document"), trc=False),
  "harrier": dict(repo="microsoft/harrier-oss-v1-0.6b",
                  q=dict(prompt_name="web_search_query"), d=dict(), trc=False),
  "f2llm":   dict(repo="codefuse-ai/F2LLM-v2-0.6B",
                  q=dict(prompt_name="query"), d=dict(prompt_name="document"), trc=False),
  "jina":    dict(repo="jinaai/jina-embeddings-v5-text-small",
                  q=dict(task="retrieval", prompt_name="query"),
                  d=dict(task="retrieval", prompt_name="document"), trc=True),
}

pasajes = json.load(open(os.path.join(SP, "corpus_pasajes.json")))
casos = json.load(open(os.path.join(SP, "casos_gold.json")))
ids = [p["id"] for p in pasajes]
docs = [p["texto"] for p in pasajes]
queries = [c["consulta"] for c in casos]


def sha_arr(a):
    return hashlib.sha256(a.astype("float32").tobytes(order="C")).hexdigest()


# ---------------- BM25 (control lexico, sin modelo) ------------------------
# Tokenizador declarado: minusculas, NFD + descarte de diacriticos combinantes,
# split por [^0-9a-z]+ . Sin stemming ni stopwords (el corpus es normativo y las
# stopwords castellanas no estan calibradas para el; no stemming evita introducir
# una variable no declarada). Okapi BM25 con k1=1.2, b=0.75.
def tok_bm25(t):
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    return [w for w in re.split(r"[^0-9a-z]+", t) if w]


def correr_bm25():
    t0 = time.perf_counter()
    docs_tok = [tok_bm25(d) for d in docs]
    N = len(docs_tok)
    dl = [len(d) for d in docs_tok]
    avgdl = sum(dl) / N
    df = collections.Counter()
    tf = []
    for d in docs_tok:
        c = collections.Counter(d); tf.append(c)
        for w in c: df[w] += 1
    idf = {w: math.log(1 + (N - n + 0.5) / (n + 0.5)) for w, n in df.items()}
    inv = collections.defaultdict(list)
    for i, c in enumerate(tf):
        for w, f in c.items(): inv[w].append((i, f))
    t_idx = time.perf_counter() - t0
    k1, b = 1.2, 0.75
    rankings = []
    for q in queries:
        sc = collections.defaultdict(float)
        for w in tok_bm25(q):
            if w not in inv: continue
            iw = idf[w]
            for i, f in inv[w]:
                sc[i] += iw * f * (k1 + 1) / (f + k1 * (1 - b + b * dl[i] / avgdl))
        # desempate declarado: score desc, luego id ascendente
        top = sorted(sc.items(), key=lambda kv: (-kv[1], ids[kv[0]]))[:TOPK]
        rankings.append([ids[i] for i, _ in top])
    return rankings, t_idx, {"k1": k1, "b": b, "avgdl": round(avgdl, 2), "vocab": len(df)}


# ---------------- denso ---------------------------------------------------
def correr_denso(clave):
    import torch, numpy as np
    from sentence_transformers import SentenceTransformer
    cfg = MODELOS[clave]
    t0 = time.perf_counter()
    m = SentenceTransformer(cfg["repo"], device="mps", trust_remote_code=cfg["trc"],
                            model_kwargs={"dtype": torch.float32})
    m.max_seq_length = MAX_SEQ
    t_load = time.perf_counter() - t0
    tok = m.tokenizer

    def grupos(textos):
        largos = [len(tok(t, add_special_tokens=True)["input_ids"]) for t in textos]
        orden = sorted(range(len(textos)), key=lambda i: (largos[i], i))
        gs, cur, curmax = [], [], 0
        for i in orden:
            nm = max(curmax, largos[i])
            if cur and (len(cur) + 1) * nm > TOKEN_BUDGET or len(cur) >= GRUPO_MAX:
                gs.append(cur); cur, curmax = [i], largos[i]
            else:
                cur.append(i); curmax = nm
        if cur: gs.append(cur)
        return gs

    def encode(textos, kw):
        gs = grupos(textos)
        E = np.zeros((len(textos), 0), dtype="float32")
        partes = {}
        for g in gs:
            v = m.encode([textos[i] for i in g], batch_size=len(g), convert_to_numpy=True,
                         normalize_embeddings=True, show_progress_bar=False, **kw)
            for j, i in enumerate(g): partes[i] = v[j]
            # Liberacion explicita del allocator de MPS entre grupos. Es una
            # sugerencia al asignador de memoria: NO toca ningun calculo ni
            # ningun valor. Se agrego porque jina (adaptador LoRA de
            # task="retrieval") acumulaba memoria a lo largo de los 93 grupos
            # hasta dejar la maquina en swap (medido: 16 GB residentes, swap
            # 16,5/17,4 GB, proceso bloqueado en waitUntilCompleted). Su
            # inocuidad numerica se verifica re-corriendo granite y comparando
            # el sha256 de la matriz de embeddings contra la corrida previa.
            torch.mps.empty_cache()
        return np.stack([partes[i] for i in range(len(textos))]).astype("float32"), len(gs)

    t0 = time.perf_counter()
    E, n_grupos_docs = encode(docs, cfg["d"])
    t_idx = time.perf_counter() - t0
    t0 = time.perf_counter()
    Q, _ = encode(queries, cfg["q"])
    t_q = time.perf_counter() - t0
    # segunda corrida de consultas: determinismo
    Q2, _ = encode(queries, cfg["q"])
    S = Q @ E.T
    rankings = []
    for r in range(S.shape[0]):
        idx = np.argsort(-S[r], kind="stable")[:TOPK * 3]
        top = sorted(((int(i), float(S[r][i])) for i in idx),
                     key=lambda kv: (-kv[1], ids[kv[0]]))[:TOPK]
        rankings.append([ids[i] for i, _ in top])
    S2 = Q2 @ E.T
    rankings2 = []
    for r in range(S2.shape[0]):
        idx = np.argsort(-S2[r], kind="stable")[:TOPK * 3]
        top = sorted(((int(i), float(S2[r][i])) for i in idx),
                     key=lambda kv: (-kv[1], ids[kv[0]]))[:TOPK]
        rankings2.append([ids[i] for i, _ in top])
    det = {"sha_Q1": sha_arr(Q), "sha_Q2": sha_arr(Q2),
           "embeddings_byte_identicos": sha_arr(Q) == sha_arr(Q2),
           "rankings_identicos": rankings == rankings2}
    extra = {"t_carga_s": round(t_load, 1), "t_consultas_s": round(t_q, 1),
             "dim": int(E.shape[1]), "sha_docs": sha_arr(E), "determinismo": det,
             "max_seq_length_efectivo": m.max_seq_length, "n_grupos_docs": n_grupos_docs}
    del m
    return rankings, t_idx, extra


# ---------------- puntuacion ---------------------------------------------
def puntuar(rankings):
    res = {}
    for regla, filtro in (("R2", lambda c: True), ("control", lambda c: c["en_control"])):
        for var in ("literal", "antilexica", "ambas"):
            sel = [(c, r) for c, r in zip(casos, rankings)
                   if filtro(c) and (var == "ambas" or c["variante"] == var)]
            n = len(sel)
            for k in (1, 5, 10):
                aciertos = sum(1 for c, r in sel if set(r[:k]) & set(c["gold"]))
                res[f"{regla}|{var}|@{k}"] = {"n": n, "aciertos": aciertos,
                                              "recall": round(aciertos / n, 4) if n else None}
    return res


if __name__ == "__main__":
    clave = sys.argv[1]
    if clave == "bm25":
        rankings, t_idx, extra = correr_bm25()
    else:
        rankings, t_idx, extra = correr_denso(clave)
    out = {"modelo": clave, "t_indexacion_s": round(t_idx, 1),
           "batch": BATCH, "max_seq": MAX_SEQ, "dtype": DTYPE, "topk": TOPK,
           "extra": extra, "metricas": puntuar(rankings),
           "rankings": {c["caso_id"]: r for c, r in zip(casos, rankings)}}
    json.dump(out, open(os.path.join(OUT, f"{clave}.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in out.items() if k != "rankings"}, ensure_ascii=False, indent=1))
