#!/usr/bin/env python3
"""U-MED-EJEMPLO, Paso 1 — BM25 de la pregunta fijada sobre los 1.763 fragmentos de E0.

tok_bm25 y bm25 se IMPORTAN sin cambios de /tmp/u_inv_ejemplo/uinvejemplo_bm25.py
(k1=1,2 y b=0,75 son las constantes K1, B de ese módulo). La carga de fragmentos
replica main() de ese módulo (líneas 58-68), que no es importable como función.
Solo lectura del repositorio; escribe únicamente en /tmp/u_med_ejemplo/.
Uso: PYTHONDONTWRITEBYTECODE=1 python3 umed_paso1_bm25.py <REPO>
"""
import hashlib, json, sys
from pathlib import Path

sys.path.insert(0, "/tmp/u_inv_ejemplo")
import uinvejemplo_bm25 as base  # noqa: E402  (lee sys.argv[1] = REPO a nivel de módulo)
from uinvejemplo_bm25 import tok_bm25, bm25  # noqa: E402

REPO = Path(sys.argv[1])
OUT = Path("/tmp/u_med_ejemplo")
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
TOS = ["cap", "cla", "ext", "pro", "ric"]
PREGUNTA = ("Una persona que tiene un comercio pidió un préstamo personal y lo va a pagar con lo "
            "que gana el comercio. ¿A partir de qué monto el banco tiene que tratarlo como un "
            "crédito comercial y no de consumo?")
FICHAS = ["cla::5.1.1.1", "cla::3.7", "cla::3.3.3", "cla::5.1.2.3", "cla::5.1.2.4"]
TEXTOS = ["cla::5.1.1.1", "cla::3.7"]
PREVIO = Path("/tmp/u_inv_ejemplo/uinvejemplo_resultado_bm25.json")
TOPK = 10


def main():
    assert (base.K1, base.B) == (1.2, 0.75), (base.K1, base.B)
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

    # ---- pregunta fijada ----
    orden, rango, aporte, dl, avgdl, terminos, vocab = bm25(ids, completo, PREGUNTA)
    top = [{"rango": r, "chunk_id": ids[i], "puntaje": round(s, 4), "puntaje_exacto": repr(s)}
           for r, (i, s) in enumerate(orden[:TOPK], 1)]

    def ficha(cid):
        i = idx[cid]
        return {"chunk_id": cid, "rango": rango.get(cid),
                "puntaje": round(sum(aporte[i].values()), 4) if cid in rango else 0.0,
                "puntaje_exacto": repr(sum(aporte[i].values())) if cid in rango else "0.0",
                "largo_tokens": dl[i],
                "aporte_por_termino": {w: round(v, 4) for w, v in sorted(aporte[i].items(), key=lambda kv: -kv[1])}}

    fichas = [ficha(c) for c in FICHAS]
    r511, r37 = rango.get("cla::5.1.1.1"), rango.get("cla::3.7")
    puerta = {"cla::5.1.1.1_en_top5": r511 is not None and r511 <= 5,
              "cla::3.7_en_top5": r37 is not None and r37 <= 5}
    puerta["pasa"] = puerta["cla::5.1.1.1_en_top5"] and not puerta["cla::3.7_en_top5"]

    salida = {"pregunta": PREGUNTA, "tokens_pregunta": tok_bm25(PREGUNTA), "k1": base.K1, "b": base.B,
              "n_fragmentos": len(ids), "sha256_insumos": shas, "control": control,
              "avgdl": round(avgdl, 2), "vocab": vocab, "n_con_puntaje_positivo": len(orden),
              "terminos_pregunta": terminos, "top10": top, "fichas": fichas, "puerta": puerta}
    (OUT / "umed_paso1_resultado.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1), encoding="utf-8")
    with open(OUT / "umed_paso1_fragmentos.txt", "w", encoding="utf-8") as fh:
        for cid in TEXTOS:
            i = idx[cid]
            fh.write(f"===== {cid} (texto completo = encabezados + propio; rango {rango.get(cid)}) =====\n{completo[i]}\n\n")
        for r, (i, s) in enumerate(orden[:TOPK], 1):
            fh.write(f"===== top-10 · rango {r} · {ids[i]} · {s!r} =====\n{completo[i]}\n\n")
    print(json.dumps(salida, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
