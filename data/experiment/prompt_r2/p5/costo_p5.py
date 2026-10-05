"""
costo_p5.py — U-PROMPT-R2, P5 (USD 0): el costo real contra el tope y la proyección, por paso, y la re-estimación de
U-REEXT-T0 con la salida medida con temperatura 0.

Costo real: `gasto_p5.jsonl` de la corrida (una línea por modo, con el resumen de su cliente: la fórmula de caching,
decisión 2) y el presupuesto compartido (`presupuesto_p5.json`).
U-REEXT-T0 (2.434 unidades): el método de P4b (`p4b/costo_p4b.py`), con los cocientes de entrada y de salida de E1 de
cada corrida de P5 contra el brazo «anterior» de P4b (el prefijo `3817de475c93`, el de los cocientes de P4), en lugar
de los de P4b. Las unidades se eligieron por lectura en P4b: los cocientes son una cota, no una estimación de la tanda.

Escribe solo en --salida (costo_p5.json). Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/costo_p5.py --trabajo DIR --salida DIR
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
PR2 = AQUI.parent
CENSO = PR2 / "p1" / "salida" / "censo_p1.json"
COSTO_P3B2 = PR2 / "p3b2" / "salida" / "costo_p3b2.json"
COSTO_P4 = PR2 / "p4" / "salida" / "costo_real_p4.json"
COSTO_P3C2 = PR2 / "p3c2" / "salida" / "costo_p3c2.json"
RES_P4B = PR2 / "p4b" / "salida" / "resultados_p4b.jsonl"
PROY = AQUI / "salida" / "proyeccion_p5.json"
PREC = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}
N = 2434
PREFIJO_P3C = 27840


def jl(p: Path) -> dict:
    out = {}
    for x in p.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[r["chunk_id"]] = r
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    gastos = [json.loads(x) for x in (a.trabajo / "gasto_p5.jsonl").read_text(encoding="utf-8").splitlines()
              if x.strip()]
    pres = json.loads((a.trabajo / "presupuesto_p5.json").read_text(encoding="utf-8"))
    proy = json.loads(PROY.read_text(encoding="utf-8"))
    real: dict = {}
    for g in gastos:
        for cli in ("e1", "forma", "e3"):
            if cli in g:
                k = f"{g['modo']}_{g['corrida']}" if g.get("corrida") else g["modo"]
                d = real.setdefault(k, {"usd": 0.0, "llamadas": 0, "llamadas_api": 0})
                d["usd"] += g[cli]["gasto_usd_real"]
                d["llamadas"] += g[cli]["llamadas"]
                d["llamadas_api"] += g[cli]["llamadas"] - g[cli]["hits_cache_local"]
    real = {k: {**v, "usd": round(v["usd"], 4)} for k, v in real.items()}
    p5 = jl(a.trabajo / "resultados_p5.jsonl")
    p4b = jl(RES_P4B)
    ids = sorted({r["id"] for r in p4b.values() if r.get("brazo") == "anterior"})
    cocientes = {}
    for c in ("a", "b"):
        ok = [i for i in ids if (p5.get(f"{i}|{c}") or {}).get("usage") and p4b[f"{i}|anterior"].get("usage")]

        def suma(src, sufijo, k):
            return sum(src[f"{i}|{sufijo}"]["usage"][k] for i in ok)
        cocientes[c] = {"unidades": len(ok),
                        "entrada_sobre_anterior": suma(p5, c, "input_tokens") / suma(p4b, "anterior", "input_tokens"),
                        "salida_sobre_anterior": suma(p5, c, "output_tokens") / suma(p4b, "anterior", "output_tokens")}
    censo = json.loads(CENSO.read_text(encoding="utf-8"))
    p3b2 = json.loads(COSTO_P3B2.read_text(encoding="utf-8"))
    p4 = json.loads(COSTO_P4.read_text(encoding="utf-8"))
    c3c2 = json.loads(COSTO_P3C2.read_text(encoding="utf-8"))
    fc, u = censo["tanda0_fases_cerradas"], censo["usage_crudo_total"]
    base_in, base_out = u["input_tokens"] * PREC["in"] / 1e6, u["output_tokens"] * PREC["out"] / 1e6
    e3v, e1r = fc["e3_verificador_usd"], fc["e3_reintentos_e1_usd"]
    render_p1 = censo["costos"]["B_central"]["e3_extra_por_render_usd"]
    crec_p1 = censo["escenarios_salida"]["B_central"]["crecimiento_salida"]
    deltas = p3b2["u_reext_t0"]["componentes_usd"]
    p3b_resto = sum(v for k, v in deltas.items() if k not in ("e1_prefijo_lecturas", "e1_prefijo_escrituras"))
    esc3 = {k: v for k, v in c3c2["u_reext_t0"]["tercer_escalon_usd"].items() if k.startswith("nuevo")}
    esc3_min = min(v["sin_ratchet"] for v in esc3.values())
    esc3_max = max(v["sin_ratchet"] for v in esc3.values())
    esc3_ratchet = max(v["con_ratchet"] for v in esc3.values())
    escenarios = {}
    for c, q in cocientes.items():
        for nombre, v in p4["u_reext_t0"].items():
            g_out = v["crecimiento_salida"] * q["salida_sobre_anterior"]
            g_in = p4["medido"]["entrada_nuevo_sobre_sellado"] * q["entrada_sobre_anterior"]
            e1 = (N - 5) * PREFIJO_P3C * PREC["cr"] / 1e6 + 5 * PREFIJO_P3C * PREC["cw"] / 1e6 + base_in * g_in \
                + base_out * g_out
            e3 = e3v + render_p1 * max(0.0, g_out - 1) / crec_p1 + e1r * g_out
            total = e1 + e3 + p3b_resto
            escenarios[f"corrida_{c}_p4_{nombre}"] = {
                "crecimiento_salida_sobre_sellado": round(g_out, 3), "e1_usd": round(e1, 2), "e3_usd": round(e3, 2),
                "deltas_p3b2_usd": round(p3b_resto, 2), "central_usd": round(total, 2),
                "con_tercer_escalon_usd": [round(total + esc3_min, 2), round(total + esc3_max, 2)],
                "con_tercer_escalon_y_ratchet_max_usd": round(total + esc3_ratchet, 2),
                "por_1_4_usd": round((total + esc3_max) * 1.4, 2)}
    out = {"comando": "data/experiment/prompt_r2/p5/costo_p5.py --trabajo DIR --salida DIR",
           "costo_real": {"por_paso": real, "total_compartido_usd": pres["gasto_usd"], "tope_usd": pres["tope_usd"],
                          "suma_por_paso_usd": round(sum(v["usd"] for v in real.values()), 4),
                          "proyeccion_central_usd": proy["total_usd"]["central"],
                          "proyeccion_alta_usd": proy["total_usd"]["alto"]},
           "medido": {c: {k: round(v, 3) if isinstance(v, float) else v for k, v in q.items()}
                      for c, q in cocientes.items()},
           "u_reext_t0": escenarios,
           "tercer_escalon_p3c1_usd": {"sin_ratchet": [esc3_min, esc3_max], "con_ratchet_max": esc3_ratchet},
           "tope_vigente_usd": 72}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "costo_p5.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
