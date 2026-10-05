"""
proyeccion_p5.py — U-PROMPT-R2, P5 (USD 0, sin API): la proyección del costo de la medición, antes de correr. Si la
alta pasa del tope de USD 1,5, P5 frena y lo reporta (el tope no se sube solo).

Base: lo medido en P4b con el mismo prefijo (`322c5a23e9b7`) y las mismas 27 unidades (p4b/salida/resultados_p4b.jsonl,
brazo «p3c»), que corrió sin temperatura fijada; la temperatura no agrega tokens al pedido.
  - E1, por corrida: el `usage` de P4b por unidad, a las tarifas de runner_corpus.P_E1 (decisión 2 de caching).
    Central: la corrida a escribe el prefijo (27.840 tokens) y la b lo lee de la caché de la API. Alta: la salida por
    1,5 y las dos corridas escriben el prefijo.
  - El reintento forzado (`ctacte::3.2.4`): central, el `usage` de esa unidad en P4b con el prefijo leído; alto, con
    el prefijo escrito y la salida de la llamada del tercer escalón de P4b (582) por 1,5.
  - E3, por corrida y unidad: la entrada sin caché sale de una recta tokens = a + b × caracteres del mensaje de E3,
    ajustada sobre las 6 llamadas de E3 de P4b (su base, copia fuera del repo, `--db-e3-p4b`), con el mensaje que
    arma prompt_e3 sobre la validación de E1 de P4b; el prefijo de E3 (11.637 tokens) leído, salvo una escritura por
    corrida en la alta y una sola en la central; salida, 200 tokens en la central y 600 en la alta, con la entrada por 1,5.

Escribe solo --salida. Uso (desde la raíz de una copia con el código de P5):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/proyeccion_p5.py \
      --seleccion S --db-e3-p4b DB --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
import prompt_e3  # noqa: E402
import runner_corpus as RC  # noqa: E402 — tarifas y modelos, solo import

TOPE_USD = 1.5
RES_P4B = AQUI.parent / "p4b" / "salida" / "resultados_p4b.jsonl"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
PREFIJO_E1 = 27840
SALIDA_ESCALON_P4B = 582


def usd(p: dict, inp=0, out=0, cw=0, cr=0) -> float:
    return (inp * p["precio_in_por_mtok"] + out * p["precio_out_por_mtok"] + cw * p["precio_cache_write_por_mtok"]
            + cr * p["precio_cache_read_por_mtok"]) / 1e6


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--seleccion", type=Path, required=True)
    ap.add_argument("--db-e3-p4b", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sel = json.loads(a.seleccion.read_text(encoding="utf-8"))
    res = {}
    for x in RES_P4B.read_text(encoding="utf-8").splitlines():
        r = json.loads(x)
        if r.get("brazo") == "p3c":
            res[r["id"]] = r
    ids = [u["id"] for u in sel["unidades"]]
    assert set(ids) <= set(res), sorted(set(ids) - set(res))
    p1, p3 = RC.P_E1, RC.P_E3

    # E1
    def corrida(factor_salida: float, escribe: bool) -> float:
        t = 0.0
        for i, cid in enumerate(ids):
            u = res[cid]["usage"]
            pref = dict(cw=PREFIJO_E1) if (i == 0 and escribe) else dict(cr=PREFIJO_E1)
            t += usd(p1, inp=u["input_tokens"], out=u["output_tokens"] * factor_salida, **pref)
        return t
    e1 = {"central": {"a": corrida(1.0, True), "b": corrida(1.0, False)},
          "alto": {"a": corrida(1.5, True), "b": corrida(1.5, True)}}
    uf = sel["reintento_forma"]["unidad"]
    uu = res[uf]["usage"]
    forma = {"central": usd(p1, inp=uu["input_tokens"], out=uu["output_tokens"], cr=PREFIJO_E1),
             "alto": usd(p1, inp=uu["input_tokens"], out=SALIDA_ESCALON_P4B * 1.5, cw=PREFIJO_E1)}

    # E3: recta sobre las llamadas de P4b
    con = sqlite3.connect(f"file:{a.db_e3_p4b.resolve()}?mode=ro&immutable=1", uri=True)
    puntos, pref_e3 = [], 0
    for inp, cr, cw, req in con.execute("SELECT input_tokens, cache_read_tokens, cache_write_tokens, request_json "
                                        "FROM cache"):
        msg = json.loads(req)["messages"][0]["content"]
        puntos.append((len(msg), inp))
        pref_e3 = max(pref_e3, cr, cw)
    con.close()
    n = len(puntos)
    mx, my = sum(x for x, _ in puntos) / n, sum(y for _, y in puntos) / n
    b = sum((x - mx) * (y - my) for x, y in puntos) / sum((x - mx) ** 2 for x, _ in puntos)
    a0 = my - b * mx
    ch = {}
    for to in TOS:
        ch.update({c["id"]: c for c in json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))})
    e3_unidades = {}
    for cid in sel["e3"]["todas"]:
        kw = prompt_e3.build_request_kwargs(ch[cid], res[cid]["validacion_e1"], model=RC.MODEL_E3)
        chars = len(kw["messages"][0]["content"])
        e3_unidades[cid] = {"chars_mensaje_con_la_salida_de_p4b": chars, "tokens_entrada": round(a0 + b * chars)}

    def e3_corrida(salida: int, factor_in: float, escribe: bool) -> float:
        t = 0.0
        for i, (cid, x) in enumerate(e3_unidades.items()):
            pref = dict(cw=pref_e3) if (i == 0 and escribe) else dict(cr=pref_e3)
            t += usd(p3, inp=x["tokens_entrada"] * factor_in, out=salida, **pref)
        return t
    e3 = {"central": {"a": e3_corrida(200, 1.0, True), "b": e3_corrida(200, 1.0, False)},
          "alto": {"a": e3_corrida(600, 1.5, True), "b": e3_corrida(600, 1.5, True)}}
    total = {k: round(sum(e1[k].values()) + forma[k] + sum(e3[k].values()), 4) for k in ("central", "alto")}
    out = {"comando": "data/experiment/prompt_r2/p5/proyeccion_p5.py --seleccion S --db-e3-p4b DB --salida DIR",
           "base": "P4b, brazo p3c (resultados_p4b.jsonl), mismo prefijo y mismas unidades",
           "e1_usd": {k: {c: round(v, 4) for c, v in d.items()} for k, d in e1.items()},
           "reintento_forma_usd": {k: round(v, 4) for k, v in forma.items()},
           "e3": {"recta": {"a": round(a0, 2), "b": round(b, 4), "n": n}, "prefijo_tokens": pref_e3,
                  "unidades": e3_unidades, "usd": {k: {c: round(v, 4) for c, v in d.items()} for k, d in e3.items()}},
           "total_usd": total, "tope_usd": TOPE_USD,
           "dentro_del_tope": {k: v <= TOPE_USD for k, v in total.items()}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "proyeccion_p5.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("e1_usd", "reintento_forma_usd", "total_usd", "dentro_del_tope")},
                     ensure_ascii=False))
    print(json.dumps(out["e3"]["usd"], ensure_ascii=False), json.dumps(out["e3"]["recta"]))
    return 0 if out["dentro_del_tope"]["alto"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
