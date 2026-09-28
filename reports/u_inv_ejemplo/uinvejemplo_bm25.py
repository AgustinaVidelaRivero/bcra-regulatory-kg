#!/usr/bin/env python3
"""U-INV-EJEMPLO — BM25 de la pregunta del ejemplo sobre los 1.763 fragmentos de E0.

Solo lectura del repositorio; escribe únicamente en /tmp/u_inv_ejemplo/.
Tokenizador y fórmula replicados de
data/experiment/bakeoff_embeddings/code/e3_medicion.py:56-90 (no se importa:
el módulo hace os.makedirs en el repo en la línea 7 y lee corpus_pasajes.json
a nivel de módulo en las líneas 40-41).
"""
import collections, hashlib, json, math, re, sys, unicodedata
from pathlib import Path

REPO = Path(sys.argv[1])
OUT = Path("/tmp/u_inv_ejemplo")
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
TOS = ["cap", "cla", "ext", "pro", "ric"]
PREGUNTA = "¿Puede una empresa pagar dividendos a accionistas del exterior? ¿Qué requisitos debe cumplir?"
OBJETIVOS = ["ext::3.17.1.4", "ext::3.4.1", "ext::3.4.2", "ext::3.4.3"]
K1, B, TOPK = 1.2, 0.75, 10


def tok_bm25(t):  # e3_medicion.py:56-59, verbatim
    t = unicodedata.normalize("NFD", t.lower())
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    return [w for w in re.split(r"[^0-9a-z]+", t) if w]


def bm25(ids, docs, q):  # e3_medicion.py:62-88, misma fórmula e idf; devuelve el ranking completo
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
    sc = collections.defaultdict(float)
    aporte = collections.defaultdict(dict)
    for w in tok_bm25(q):
        if w not in df: continue
        iw = idf[w]
        for i, c in enumerate(tf):
            f = c.get(w, 0)
            if not f: continue
            v = iw * f * (K1 + 1) / (f + K1 * (1 - B + B * dl[i] / avgdl))
            sc[i] += v
            aporte[i][w] = aporte[i].get(w, 0) + v
    orden = sorted(sc.items(), key=lambda kv: (-kv[1], ids[kv[0]]))  # desempate declarado
    rango = {ids[i]: r for r, (i, _) in enumerate(orden, 1)}
    q_tok = tok_bm25(q)
    terminos = {w: {"df": df.get(w, 0), "idf": round(idf[w], 6) if w in idf else None} for w in dict.fromkeys(q_tok)}
    return orden, rango, aporte, dl, avgdl, terminos, len(df)


def main():
    chunks = []
    shas = {}
    for to in TOS:
        p = E0 / f"chunks_{to}.json"
        shas[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
        chunks.extend(json.loads(p.read_text(encoding="utf-8")))
    chunks.sort(key=lambda c: c["id"])
    ids = [c["id"] for c in chunks]
    completo = ["\n".join([h["texto"] for h in c["herencia"]] + [c["texto"]]) for c in chunks]
    for c, t in zip(chunks, completo):
        assert hashlib.sha256(t.encode()).hexdigest() == c["sha256_completo"], c["id"]
    propio = [c["texto"] for c in chunks]
    contenedor = [c["id"] for c in chunks if c["to"] == "ext" and (c["unidad"] == "3.4" or c["unidad"].startswith("3.4."))]
    salida = {"pregunta": PREGUNTA, "tokens_pregunta": tok_bm25(PREGUNTA), "k1": K1, "b": B,
              "n_fragmentos": len(ids), "sha256_insumos": shas, "variantes": {}}
    for nombre, docs in (("A_con_encabezados", completo), ("B_solo_propio", propio)):
        orden, rango, aporte, dl, avgdl, terminos, vocab = bm25(ids, docs, PREGUNTA)
        idx = {x: i for i, x in enumerate(ids)}
        top = [{"rango": r, "chunk_id": ids[i], "puntaje": round(s, 4), "puntaje_exacto": repr(s)} for r, (i, s) in enumerate(orden[:TOPK], 1)]
        with open(OUT / "uinvejemplo_textos_top10.txt", "a", encoding="utf-8") as fh:
            for r, (i, s) in enumerate(orden[:TOPK], 1):
                fh.write(f"===== variante {nombre} · rango {r} · {ids[i]} · {s!r} =====\n{docs[i]}\n\n")
        def ficha(cid):
            i = idx[cid]
            return {"chunk_id": cid, "rango": rango.get(cid), "puntaje": round(sum(aporte[i].values()), 4) if cid in rango else 0.0,
                    "largo_tokens": dl[i], "aporte_por_termino": {w: round(v, 4) for w, v in sorted(aporte[i].items(), key=lambda kv: -kv[1])}}
        salida["variantes"][nombre] = {
            "avgdl": round(avgdl, 2), "vocab": vocab, "n_con_puntaje_positivo": len(orden),
            "terminos_pregunta": terminos, "top10": top,
            "objetivos": [ficha(c) for c in OBJETIVOS],
            "contenedor_ext_3_4": [ficha(c) for c in contenedor]}
    (OUT / "uinvejemplo_resultado_bm25.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    # textos de los cuatro fragmentos, tal como los compone el índice del banco (herencia + propio)
    with open(OUT / "uinvejemplo_fragmentos_objetivo.txt", "w", encoding="utf-8") as fh:
        for cid in OBJETIVOS:
            i = ids.index(cid)
            fh.write(f"===== {cid} (texto completo = herencia + propio) =====\n{completo[i]}\n\n")
            fh.write(f"----- {cid} (solo propio) -----\n{propio[i]}\n\n")
    print(json.dumps(salida, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
