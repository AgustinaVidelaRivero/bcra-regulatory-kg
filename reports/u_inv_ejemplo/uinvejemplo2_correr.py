#!/usr/bin/env python3
"""U-INV-EJEMPLO-2 — mismas funciones de cálculo que U-INV-EJEMPLO, preguntas nuevas.

Importa tok_bm25, bm25, E0, TOS, K1 y B de uinvejemplo_bm25.py (sin modificarlo:
sha256 de9056c8…) y repite su carga de fragmentos línea por línea. Antes de
correr P1 y P2 reproduce la pregunta original y la compara contra
uinvejemplo_resultado_bm25.json; si no coincide, se detiene.
Uso: PYTHONDONTWRITEBYTECODE=1 python3 uinvejemplo2_correr.py <raíz del repo>
"""
import hashlib, json, sys
from pathlib import Path

sys.path.insert(0, "/tmp/u_inv_ejemplo")
import uinvejemplo_bm25 as base  # noqa: E402  (lee sys.argv[1] como raíz del repo)

OUT = Path("/tmp/u_inv_ejemplo")
PREGUNTAS = {
    "P1": ("Una petrolera que obtuvo la certificación del régimen de acceso a divisas por "
           "producción incremental quiere usarla para pagar dividendos a sus accionistas del "
           "exterior. ¿Qué requisitos debe cumplir?"),
    "P2": ("¿Qué requisitos debe cumplir una empresa con certificación por producción "
           "incremental de petróleo o gas para pagar dividendos a accionistas no "
           "residentes?"),
}
SEGUIDOS = ["ext::3.17.1.4", "ext::3.4.1", "ext::3.4.2", "ext::3.4.3", "ext::3.4::intro", "ext::3.18.1.2"]
TOPK = 10


def cargar():  # mismas líneas que base.main()
    chunks = []
    shas = {}
    for to in base.TOS:
        p = base.E0 / f"chunks_{to}.json"
        shas[p.name] = hashlib.sha256(p.read_bytes()).hexdigest()
        chunks.extend(json.loads(p.read_text(encoding="utf-8")))
    chunks.sort(key=lambda c: c["id"])
    ids = [c["id"] for c in chunks]
    completo = ["\n".join([h["texto"] for h in c["herencia"]] + [c["texto"]]) for c in chunks]
    for c, t in zip(chunks, completo):
        assert hashlib.sha256(t.encode()).hexdigest() == c["sha256_completo"], c["id"]
    propio = [c["texto"] for c in chunks]
    return ids, completo, propio, shas


def correr(ids, docs, q):
    orden, rango, aporte, dl, avgdl, terminos, vocab = base.bm25(ids, docs, q)
    idx = {x: i for i, x in enumerate(ids)}
    top = [{"rango": r, "chunk_id": ids[i], "puntaje": round(s, 4), "puntaje_exacto": repr(s)}
           for r, (i, s) in enumerate(orden[:TOPK], 1)]
    punt = {ids[i]: s for i, s in orden}
    seg = [{"chunk_id": c, "rango": rango.get(c), "puntaje": round(punt[c], 4) if c in punt else 0.0,
            "puntaje_exacto": repr(punt[c]) if c in punt else None,
            "aporte_por_termino": {w: round(v, 4) for w, v in sorted(aporte[idx[c]].items(), key=lambda kv: -kv[1])}}
           for c in SEGUIDOS]
    s5 = orden[4][1]
    borde = [{"rango": r, "chunk_id": ids[i], "puntaje_exacto": repr(s)}
             for r, (i, s) in enumerate(orden, 1) if s == s5]
    return {"avgdl": round(avgdl, 2), "n_con_puntaje_positivo": len(orden), "terminos_pregunta": terminos,
            "top10": top, "seguidos": seg,
            "seguidos_en_top5": [c for c in SEGUIDOS if rango.get(c) is not None and rango[c] <= 5],
            "empate_en_rango_5": borde if len(borde) > 1 else []}


def main():
    ids, completo, propio, shas = cargar()
    variantes = (("A_con_encabezados", completo), ("B_solo_propio", propio))
    # Control: la pregunta original debe reproducir U-INV-EJEMPLO.
    previo = json.loads((OUT / "uinvejemplo_resultado_bm25.json").read_text(encoding="utf-8"))
    for nombre, docs in variantes:
        orden, rango, *_ = base.bm25(ids, docs, base.PREGUNTA)
        top = [{"rango": r, "chunk_id": ids[i], "puntaje": round(s, 4), "puntaje_exacto": repr(s)}
               for r, (i, s) in enumerate(orden[:TOPK], 1)]
        pv = previo["variantes"][nombre]
        if top != pv["top10"] or any(rango.get(o["chunk_id"]) != o["rango"] for o in pv["objetivos"]):
            raise SystemExit(f"CONTROL FALLIDO en {nombre}: no reproduce U-INV-EJEMPLO")
    salida = {"control_pregunta_original": "reproduce top-10 y rangos de U-INV-EJEMPLO en A y B",
              "sha256_script_base": hashlib.sha256(Path(base.__file__).read_bytes()).hexdigest(),
              "k1": base.K1, "b": base.B, "n_fragmentos": len(ids), "sha256_insumos": shas, "preguntas": {}}
    for pid, q in PREGUNTAS.items():
        salida["preguntas"][pid] = {"texto": q, "tokens": base.tok_bm25(q),
                                    "variantes": {n: correr(ids, d, q) for n, d in variantes}}
    (OUT / "uinvejemplo2_resultado_bm25.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1),
                                                          encoding="utf-8")
    print(json.dumps(salida, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
