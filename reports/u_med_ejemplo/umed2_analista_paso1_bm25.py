#!/usr/bin/env python3
"""U-MED-EJEMPLO-2, Paso 1 — BM25 de la pregunta del analista sobre los 1.763 fragmentos de E0,
en dos variantes de análisis de texto.

(A) tok_bm25 y bm25 IMPORTADAS sin cambios de /tmp/u_inv_ejemplo/uinvejemplo_bm25.py
    (k1=1,2 y b=0,75 son las constantes K1, B de ese módulo).
(B) misma fórmula (la misma función bm25 importada) sobre texto pre-tokenizado:
    1. límites de token idénticos a tok_bm25 (se verifica: plegar acentos de los
       tokens de B reproduce tok_bm25 en todo el corpus y en las preguntas);
    2. se descartan los tokens presentes en la lista de palabras vacías de Snowball
       para español (corpus stopwords de nltk, README: origen pgsql/src/backend/snowball/stopwords/);
    3. cada token restante se reduce con SnowballStemmer('spanish') de nltk;
    4. se pliegan los acentos de la raíz, como hace tok_bm25.
    Palabras vacías y raíz se aplican antes del plegado porque la lista y el algoritmo
    están definidos sobre formas acentuadas. Los tokens resultantes son [0-9a-z]+ unidos
    por espacios, así que el tok_bm25 interno de bm25 los devuelve intactos (se verifica).
    Aproximación al analizador spanish de Lucene, no el mismo.
Sensibilidad (fuera de la puerta): orden alternativo de B, plegando acentos primero.

La carga de fragmentos replica main() de uinvejemplo_bm25.py (líneas 58-68).
Solo lectura del repositorio; escribe únicamente en /tmp/u_med_ejemplo/.
Uso: PYTHONDONTWRITEBYTECODE=1 umed2_analista_venv/bin/python umed2_analista_paso1_bm25.py <REPO>
"""
import hashlib, json, sys, unicodedata
from pathlib import Path

sys.path.insert(0, "/tmp/u_inv_ejemplo")
import uinvejemplo_bm25 as base  # noqa: E402  (lee sys.argv[1] = REPO a nivel de módulo)
from uinvejemplo_bm25 import tok_bm25, bm25  # noqa: E402

import nltk  # noqa: E402
NLTK_DATA = "/tmp/u_med_ejemplo/umed2_analista_nltk_data"
nltk.data.path.insert(0, NLTK_DATA)
from nltk.corpus import stopwords  # noqa: E402
from nltk.stem.snowball import SnowballStemmer  # noqa: E402

REPO = Path(sys.argv[1])
OUT = Path("/tmp/u_med_ejemplo")
PFX = "umed2_analista_"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
TOS = ["cap", "cla", "ext", "pro", "ric"]
PREGUNTA = ("Para una entidad financiera, ¿qué condiciones hacen que los créditos para consumo o "
            "vivienda deban clasificarse en la cartera comercial?")
FICHAS = ["cla::5.1.1.1", "cla::3.7", "cla::5.1.1.2", "cla::3.3.3", "cla::5.1.2.3", "cla::5.1.2.4"]
PREVIO = Path("/tmp/u_inv_ejemplo/uinvejemplo_resultado_bm25.json")
STOP_FILE = Path(NLTK_DATA) / "corpora/stopwords/spanish"
STOP_SHA = "6125eadf28ba664a60bf4296147bcbd40b80be93670056fdb229960ac15e2310"
TOPK = 10
AZ = set("0123456789abcdefghijklmnopqrstuvwxyz")

STOP = set(stopwords.words("spanish"))
STEM = SnowballStemmer("spanish")


def plegar(s):  # mismo plegado que tok_bm25 (NFD + descarte de combinantes)
    s = unicodedata.normalize("NFD", s)
    return "".join(ch for ch in s if not unicodedata.combining(ch))


def tok_crudo(t):  # minúsculas con acentos; límites de token iguales a tok_bm25
    t = unicodedata.normalize("NFC", t.lower())
    out, cur = [], []
    for ch in t:
        p = plegar(ch)
        if p and all(c in AZ for c in p):
            cur.append(ch)
        elif cur:
            out.append("".join(cur)); cur = []
    if cur:
        out.append("".join(cur))
    return out


def tok_b(t, detalle=False):
    crudo = tok_crudo(t)
    vacias, raices = [], []
    for w in crudo:
        if w in STOP:
            vacias.append(w); continue
        r = plegar(STEM.stem(w))
        if r:
            raices.append(r)
    return (crudo, vacias, raices) if detalle else raices


STOP_PLEGADA = {plegar(s) for s in STOP}


def tok_b_alt(t):  # sensibilidad: plegar primero (tok_bm25), después vacías plegadas y raíz
    return [r for r in (plegar(STEM.stem(w)) for w in tok_bm25(t) if w not in STOP_PLEGADA) if r]


def correr(ids, docs, q, idx):
    orden, rango, aporte, dl, avgdl, terminos, vocab = bm25(ids, docs, q)
    top = [{"rango": r, "chunk_id": ids[i], "puntaje": round(s, 4), "puntaje_exacto": repr(s)}
           for r, (i, s) in enumerate(orden[:TOPK], 1)]

    def ficha(cid):
        i = idx[cid]
        return {"chunk_id": cid, "rango": rango.get(cid),
                "puntaje": round(sum(aporte[i].values()), 4) if cid in rango else 0.0,
                "puntaje_exacto": repr(sum(aporte[i].values())) if cid in rango else "0.0",
                "largo_tokens": dl[i],
                "aporte_por_termino": {w: round(v, 4) for w, v in sorted(aporte[i].items(), key=lambda kv: -kv[1])}}

    r511, r37 = rango.get("cla::5.1.1.1"), rango.get("cla::3.7")
    puerta = {"cla::5.1.1.1_en_top5": r511 is not None and r511 <= 5,
              "cla::3.7_en_top5": r37 is not None and r37 <= 5}
    puerta["pasa"] = puerta["cla::5.1.1.1_en_top5"] and not puerta["cla::3.7_en_top5"]
    return {"avgdl": round(avgdl, 2), "vocab": vocab, "n_con_puntaje_positivo": len(orden),
            "terminos_pregunta": terminos, "top10": top, "fichas": [ficha(c) for c in FICHAS],
            "puerta": puerta}, orden


def main():
    assert (base.K1, base.B) == (1.2, 0.75), (base.K1, base.B)
    assert hashlib.sha256(STOP_FILE.read_bytes()).hexdigest() == STOP_SHA
    chunks, shas = [], {}
    for to in TOS:
        p = E0 / f"chunks_{to}.json"
        shas[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
        chunks.extend(json.loads(p.read_text(encoding="utf-8")))
    chunks.sort(key=lambda c: c["id"])
    ids = [c["id"] for c in chunks]
    completo = ["\n".join([h["texto"] for h in c["herencia"]] + [c["texto"]]) for c in chunks]
    for c, t in zip(chunks, completo):
        assert hashlib.sha256(t.encode()).hexdigest() == c["sha256_completo"], c["id"]
    idx = {x: i for i, x in enumerate(ids)}

    # ---- control: pregunta original, variante A_con_encabezados ----
    previo = json.loads(PREVIO.read_text(encoding="utf-8"))
    orden0, *_ = bm25(ids, completo, base.PREGUNTA)
    top0 = [{"rango": r, "chunk_id": ids[i], "puntaje_exacto": repr(s)} for r, (i, s) in enumerate(orden0[:TOPK], 1)]
    top_prev = [{"rango": t["rango"], "chunk_id": t["chunk_id"], "puntaje_exacto": t["puntaje_exacto"]}
                for t in previo["variantes"]["A_con_encabezados"]["top10"]]
    control = {"pregunta_original": base.PREGUNTA,
               "sha256_insumos_coinciden_con_previo": shas == previo["sha256_insumos"],
               "top10_reproducido": top0 == top_prev,
               "top10_recalculado": top0}

    # ---- verificaciones de la tokenización B ----
    textos = completo + [PREGUNTA, base.PREGUNTA]
    limites_ok = all([plegar(w) for w in tok_crudo(t)] == tok_bm25(t) for t in textos)
    docs_b = [" ".join(tok_b(t)) for t in completo]
    q_b = " ".join(tok_b(PREGUNTA))
    idempotente_ok = all(tok_bm25(d) == d.split() for d in docs_b + [q_b])
    assert limites_ok and idempotente_ok, (limites_ok, idempotente_ok)

    # ---- variante A ----
    res_a, orden_a = correr(ids, completo, PREGUNTA, idx)
    res_a["tokens_pregunta"] = tok_bm25(PREGUNTA)
    # ---- variante B ----
    res_b, orden_b = correr(ids, docs_b, q_b, idx)
    crudo, vacias, raices = tok_b(PREGUNTA, detalle=True)
    res_b["tokens_pregunta"] = raices
    res_b["tokens_pregunta_detalle"] = {"crudo": crudo, "descartadas_por_vacias": vacias,
                                        "raices": [[w, plegar(STEM.stem(w))] for w in crudo if w not in STOP]}
    # ---- sensibilidad al orden de B (fuera de la puerta) ----
    docs_alt = [" ".join(tok_b_alt(t)) for t in completo]
    res_alt, _ = correr(ids, docs_alt, " ".join(tok_b_alt(PREGUNTA)), idx)
    sens = {"tokens_pregunta": tok_b_alt(PREGUNTA), "top5": res_alt["top10"][:5],
            "cla::5.1.1.1": next(f for f in res_alt["fichas"] if f["chunk_id"] == "cla::5.1.1.1")["rango"],
            "cla::3.7": next(f for f in res_alt["fichas"] if f["chunk_id"] == "cla::3.7")["rango"],
            "puerta": res_alt["puerta"]}

    salida = {"pregunta": PREGUNTA, "k1": base.K1, "b": base.B, "n_fragmentos": len(ids),
              "sha256_insumos": shas, "control": control,
              "variante_B_entorno": {"nltk": nltk.__version__, "stemmer": "nltk.stem.snowball.SnowballStemmer('spanish')",
                                     "stopwords_archivo": str(STOP_FILE), "stopwords_sha256": STOP_SHA,
                                     "stopwords_n_lineas_unicas": len(STOP),
                                     "verif_limites_iguales_a_tok_bm25": limites_ok,
                                     "verif_tok_bm25_idempotente_sobre_B": idempotente_ok},
              "variantes": {"A": res_a, "B": res_b}, "sensibilidad_B_orden_alternativo": sens,
              "puerta_global_pasa": res_a["puerta"]["pasa"] and res_b["puerta"]["pasa"]}
    (OUT / f"{PFX}paso1_resultado.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(OUT / f"{PFX}paso1_fragmentos.txt", "w", encoding="utf-8") as fh:
        for nombre, orden in (("A", orden_a), ("B", orden_b)):
            for r, (i, s) in enumerate(orden[:TOPK], 1):
                fh.write(f"===== variante {nombre} · rango {r} · {ids[i]} · {s!r} =====\n{completo[i]}\n\n")
    print(json.dumps(salida, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
