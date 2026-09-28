#!/usr/bin/env python3
"""Búsqueda léxica (BM25) sobre los 1.763 fragmentos de E0.

tok_bm25 y bm25 están copiadas sin cambios de reports/u_inv_ejemplo/uinvejemplo_bm25.py
(líneas 22-54 de ese archivo; su sha256 queda en ORIGEN_SHA256), que a su vez las
replica de data/experiment/bakeoff_embeddings/code/e3_medicion.py:56-90:
tokenizador en minúsculas, NFD sin diacríticos combinantes y corte por
[^0-9a-z]+; Okapi BM25 con k1 = 1,2 y b = 0,75; desempate por puntaje
descendente y después por id ascendente. e3_medicion.py no se importa porque al
importarse crea directorios en el repositorio (línea 7) y lee su corpus (líneas
40-41).

cargar_fragmentos() lee los cinco chunks_<to>.json de E0 (salida_enm01), ordena
los fragmentos por id y compone el texto de cada uno como su cadena de
encabezados heredados seguida del texto propio, unidos por salto de línea; antes
de devolverlos comprueba que el sha256 de cada texto compuesto coincida con el
campo sha256_completo del fragmento.

Solo lectura, biblioteca estándar. Uso como módulo:
    ids, textos, shas = cargar_fragmentos()
    orden, rango, aporte, dl, avgdl, terminos, vocab = bm25(ids, textos, pregunta)
"""
import collections, hashlib, json, math, os, re, unicodedata
from pathlib import Path

RAIZ = Path(os.path.abspath(__file__)).parents[3]
E0 = RAIZ / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
TOS = ["cap", "cla", "ext", "pro", "ric"]
N_FRAGMENTOS = 1763
K1, B = 1.2, 0.75
ORIGEN_FUNCIONES = "reports/u_inv_ejemplo/uinvejemplo_bm25.py"
ORIGEN_SHA256 = "de9056c80c9a8b1e828ec6fbb6c712f140015b634c962604408354a5869b7ebe"


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


def cargar_fragmentos():
    """Devuelve (ids, textos, shas): ids ordenados, texto compuesto de cada
    fragmento (encabezados heredados + propio) y sha256 de cada archivo leído."""
    chunks, shas = [], {}
    for to in TOS:
        p = E0 / f"chunks_{to}.json"
        shas[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
        chunks.extend(json.loads(p.read_text(encoding="utf-8")))
    chunks.sort(key=lambda c: c["id"])
    ids = [c["id"] for c in chunks]
    textos = ["\n".join([h["texto"] for h in c["herencia"]] + [c["texto"]]) for c in chunks]
    for c, t in zip(chunks, textos):
        if hashlib.sha256(t.encode()).hexdigest() != c["sha256_completo"]:
            raise SystemExit(f"sha256_completo no coincide: {c['id']}")
    if len(ids) != N_FRAGMENTOS:
        raise SystemExit(f"se leyeron {len(ids)} fragmentos, se esperaban {N_FRAGMENTOS}")
    return ids, textos, shas
