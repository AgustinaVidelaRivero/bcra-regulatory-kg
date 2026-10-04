"""
proyeccion_p4.py — U-PROMPT-R2, P4 (USD 0, sin API): la proyección del costo de la pareada con todos sus casos, antes de
correr, con la fórmula de caching (decisión 2 de docs/decisiones_caching_extraccion.md) y las tarifas del runner
(runner_corpus.py:18-19).

Llamadas que pagan:
  - brazo nuevo (perfil r2b, prefijo `3817de475c93`, e0-r2): los 40 sorteados, los 9 fijos, las 8 listas, los 3
    encabezados de ctacte de la pata de E3, los 8 de F1 y los 8 fuera de muestra;
  - brazo sellado por la API (perfil v3_b54, E0 legada): los 8 de F1 y los 8 fuera de muestra;
  - pata de E3: las 4 verificaciones y, en el escenario alto, un reintento de E1 r2b y una re-verificación por unidad.
El brazo sellado de los demás sale de la caché (USD 0).

Estimación por llamada:
  - prefijo: el tamaño de cada perfil por la recta de 3 parámetros de P1 (p1/salida/censo_p1.json); una escritura por
    corrida secuencial y lectura en las demás (decisión 4);
  - entrada sin caché: en la tanda 0, la del crudo sellado (`usage.input_tokens`) más la diferencia de largo entre el
    mensaje r2b y el sellado por los tokens por carácter de mensaje de P1; fuera de la tanda 0, la recta de mensaje de
    P1 sobre el largo del mensaje de cada perfil;
  - salida: en la tanda 0, la del crudo sellado por el crecimiento del escenario B central de P1 (+33,55 %); fuera de la
    tanda 0, una recta de salida contra el texto propio ajustada sobre los 2.434 crudos de la tanda 0 (y el
    crecimiento, en el brazo nuevo). Una salida proyectada de más de 8.192 tokens suma el intento cortado;
  - pata de E3: las bases de P1 (`estimacion_p4.total.pata_e3_base`).
Escenario alto: 1,4 veces lo variable (el factor del precedente de los topes).

Escribe solo en --salida (proyeccion_p4.json). Uso (desde la raíz de una COPIA del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4/proyeccion_p4.py \
      --muestra DIR/muestra_p4.json --e0-fuera DIR --salida DIR
"""
from __future__ import annotations

import argparse
import json
import statistics as st
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e1_extractor"))
import perfil_e1  # noqa: E402

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
CRUDO = REX / "corpus_tanda0" / "salida_dirigida"
E0_LEG = REX / "e0_chunking" / "salida_tanda0"
E0_R2 = REX / "e0_chunking" / "salida_tanda0_r2"
CENSO = AQUI.parent / "p1" / "salida" / "censo_p1.json"
P = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}            # E1 (runner_corpus.py:18)
MODELO = "claude-haiku-4-5"
CRECIMIENTO = 0.3355                                              # censo_p1, escenarios_salida.B_central
ALTO = 1.4
CORTE = 8192


def jl_last_wins(p: Path) -> dict:
    out = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


def chunks(d: Path, to: str) -> dict:
    return {c["id"]: c for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8"))}


def recta(xs, ys):
    mx, my = st.mean(xs), st.mean(ys)
    b = sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / sum((x - mx) ** 2 for x in xs)
    return my - b * mx, b


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--muestra", type=Path, required=True)
    ap.add_argument("--e0-fuera", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    m = json.loads(a.muestra.read_text(encoding="utf-8"))
    censo = json.loads(CENSO.read_text(encoding="utf-8"))
    c3 = censo["calibracion"]["prefijo"]["recta_3p"]
    a_msg, k_msg = censo["calibracion"]["mensaje"]["a"], censo["calibracion"]["mensaje"]["tokens_por_caracter"]
    pe3 = censo["estimacion_p4"]["total"]["pata_e3_base"]
    nuevo, sellado = perfil_e1.perfil("r2b"), perfil_e1.perfil("v3_b54")

    def pref_tokens(perfil, c) -> float:
        k = perfil.build_request_kwargs(c, model=MODELO)
        s = "".join(b["text"] for b in k["system"])
        return c3[0] + c3[1] * len(s) + c3[2] * len(json.dumps(k["tools"][0], ensure_ascii=False))

    def msg_len(perfil, c) -> int:
        return len(perfil.build_request_kwargs(c, model=MODELO)["messages"][0]["content"])

    leg, r2, crudo = {}, {}, {}
    for to in TOS:
        leg.update(chunks(E0_LEG, to))
        r2.update(chunks(E0_R2, to))
        crudo.update(jl_last_wins(CRUDO / to / "extracciones_e1.jsonl"))
    # recta de salida contra el texto propio, sobre los crudos válidos de la tanda 0
    xs, ys = [], []
    for cid, r in crudo.items():
        if r.get("error") is None and cid in leg and r.get("usage"):
            xs.append(len(leg[cid].get("texto") or ""))
            ys.append(r["usage"]["output_tokens"])
    a_out, b_out = recta(xs, ys)
    w = a.e0_fuera.resolve()
    fleg, fr2 = {}, {}
    for to in ("ayccef", "expaef", "opefci", "adrei"):
        fleg.update(chunks(w / "e0_legada", to))
        fr2.update(chunks(w / "e0_r2", to))

    def llamada(inp, out) -> dict:
        partes = {"entrada": inp * P["in"] / 1e6, "salida": out * P["out"] / 1e6}
        if out > CORTE:                                           # intento cortado y reintento
            partes["intento_cortado"] = (inp * P["in"] + CORTE * P["out"]) / 1e6
        return partes

    t0 = ([c for e in m["sorteo"] for c in m["sorteo"][e]["elegidos"]] + m["fijos"]
          + [c for v in m["listas_excepciones"].values() for c in v["tomados"]] + m["pata_e3"][:3])
    fuera = m["f1"] + [c for v in m["fuera_de_muestra"].values() for c in v]
    filas = []
    for cid in t0:
        u = crudo[cid]["usage"]
        inp = u["input_tokens"] + k_msg * (msg_len(nuevo, r2[cid]) - msg_len(sellado, leg[cid]))
        out = u["output_tokens"] * (1 + CRECIMIENTO)
        filas.append({"chunk_id": cid, "brazo": "nuevo", "entrada": round(inp), "salida": round(out),
                      **{k: round(v, 5) for k, v in llamada(inp, out).items()}})
    for cid in fuera:
        out_s = max(a_out + b_out * len(fleg[cid].get("texto") or ""), 200)
        for brazo, perfil, c, out in (("sellado_api", sellado, fleg[cid], out_s),
                                      ("nuevo", nuevo, fr2[cid], out_s * (1 + CRECIMIENTO))):
            inp = a_msg + k_msg * msg_len(perfil, c)
            filas.append({"chunk_id": cid, "brazo": brazo, "entrada": round(inp), "salida": round(out),
                          **{k: round(v, 5) for k, v in llamada(inp, out).items()}})
    n_nuevo = sum(1 for f in filas if f["brazo"] == "nuevo")
    n_sell = sum(1 for f in filas if f["brazo"] == "sellado_api")
    tok_nuevo, tok_sell = pref_tokens(nuevo, r2[t0[0]]), pref_tokens(sellado, leg[t0[0]])
    prefijo = {"nuevo": (tok_nuevo * P["cw"] + (n_nuevo - 1) * tok_nuevo * P["cr"]) / 1e6,
               "sellado_api": (tok_sell * P["cw"] + (n_sell - 1) * tok_sell * P["cr"]) / 1e6}
    por_brazo = {}
    for b in ("nuevo", "sellado_api"):
        fs = [f for f in filas if f["brazo"] == b]
        por_brazo[b] = round(sum(f.get(k, 0) for f in fs for k in ("entrada", "salida", "intento_cortado")
                                 if isinstance(f.get(k), float)), 4)
    pata_central = pe3["escritura_usd"] + 3 * pe3["lectura_usd"] + 4 * pe3["llamada_usd"]
    pata_alto = pata_central + 4 * (pe3["reintento_e1_r2_usd"] + pe3["lectura_usd"] + pe3["llamada_usd"])
    central = prefijo["nuevo"] + prefijo["sellado_api"] + sum(por_brazo.values()) + pata_central
    alto = prefijo["nuevo"] + prefijo["sellado_api"] + ALTO * sum(por_brazo.values()) + pata_alto
    res = {"comando": "data/experiment/prompt_r2/p4/proyeccion_p4.py --muestra M --e0-fuera DIR --salida DIR",
           "llamadas": {"e1_nuevo": n_nuevo, "e1_sellado_api": n_sell, "e3_pata": 4, "e1_sellado_cache_usd0": len(t0)},
           "prefijo_tokens": {"nuevo": round(tok_nuevo), "sellado": round(tok_sell)},
           "recta_salida_tanda0": {"a": round(a_out, 1), "tokens_por_caracter_de_texto_propio": round(b_out, 4),
                                   "n": len(xs)},
           "usd": {"prefijo": {k: round(v, 4) for k, v in prefijo.items()}, "variable_por_brazo": por_brazo,
                   "pata_e3": {"central": round(pata_central, 4), "alto": round(pata_alto, 4)},
                   "central": round(central, 4), "alto": round(alto, 4), "tope": 2.0},
           "intentos_cortados_proyectados": [f["chunk_id"] for f in filas if "intento_cortado" in f],
           "por_llamada": filas}
    (sal / "proyeccion_p4.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("llamadas", "prefijo_tokens", "recta_salida_tanda0", "usd",
                                          "intentos_cortados_proyectados")}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
