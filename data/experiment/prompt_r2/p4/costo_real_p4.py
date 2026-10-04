"""
costo_real_p4.py — U-PROMPT-R2, P4 (USD 0): el costo real de la pareada contra el tope y la proyección, y la
re-estimación de U-REEXT-T0 con lo que midió la pareada, para la recomendación del tope (hoy USD 72).

Costo real: `gasto_p4.json` de la corrida (fórmula de caching de cada cliente, decisión 2).
Re-estimación de U-REEXT-T0 (2.434 unidades), sobre la base sellada de P1 (p1/salida/censo_p1.json) y los deltas de
P3b-2 (p3b2/salida/costo_p3b2.json), cambiando solo lo que la pareada midió:
  - el prefijo nuevo: los tokens de escritura de caché de la primera llamada del brazo nuevo (en lugar de la recta);
  - la entrada sin caché: el cociente nuevo/sellado de `input_tokens` en los 60 chunks de la tanda 0;
  - la salida: el cociente nuevo/sellado de `output_tokens`, de dos maneras: sin ponderar (los 60 chunks) y ponderado
    por estrato con el tamaño de cada estrato en la tanda 0 (los 40 sorteados). Los dos son cotas: la muestra está
    estratificada y el estrato sin marca, que domina la tanda 0, tiene 8 chunks;
  - E3 y los reintentos del ratchet escalan con la salida, como en P1; la NOTA de E3 y los demás deltas de P3b-2 quedan
    como estaban (cota alta).

Escribe solo en --salida (costo_real_p4.json).
Uso: .venv/bin/python -B costo_real_p4.py --trabajo DIR --muestra M --proyeccion P --salida DIR
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
CENSO = AQUI.parent / "p1" / "salida" / "censo_p1.json"
COSTO_P3B2 = AQUI.parent / "p3b2" / "salida" / "costo_p3b2.json"
PREC = {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10}
N = 2434


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--muestra", type=Path, required=True)
    ap.add_argument("--proyeccion", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    gasto = json.loads((a.trabajo / "gasto_p4.json").read_text(encoding="utf-8"))
    m = json.loads(a.muestra.read_text(encoding="utf-8"))
    proy = json.loads(a.proyeccion.read_text(encoding="utf-8"))["usd"]
    res = {r["chunk_id"]: r for r in map(json.loads, (a.trabajo / "resultados_p4.jsonl").read_text(encoding="utf-8").splitlines())}
    censo = json.loads(CENSO.read_text(encoding="utf-8"))
    p3b2 = json.loads(COSTO_P3B2.read_text(encoding="utf-8"))
    t0 = ([c for v in m["sorteo"].values() for c in v["elegidos"]] + m["fijos"]
          + [c for v in m["listas_excepciones"].values() for c in v["tomados"]] + m["pata_e3"][:3])

    def suma(ids, brazo, k):
        return sum(res[f"{c}|{brazo}"]["usage"][k] for c in ids)
    g_in = suma(t0, "nuevo", "input_tokens") / suma(t0, "sellado", "input_tokens")
    g_out = suma(t0, "nuevo", "output_tokens") / suma(t0, "sellado", "output_tokens")
    num = den = 0.0
    for e, v in m["sorteo"].items():
        num += v["pool"] * suma(v["elegidos"], "nuevo", "output_tokens")
        den += v["pool"] * suma(v["elegidos"], "sellado", "output_tokens")
    g_out_pond = num / den
    pref = gasto["e1_nuevo"]["cache_stats"]["cache_write"]          # una escritura: el prefijo medido
    fc = censo["tanda0_fases_cerradas"]
    u = censo["usage_crudo_total"]
    base_in, base_out = u["input_tokens"] * PREC["in"] / 1e6, u["output_tokens"] * PREC["out"] / 1e6
    e3v, e1r = fc["e3_verificador_usd"], fc["e3_reintentos_e1_usd"]
    render_p1 = censo["costos"]["B_central"]["e3_extra_por_render_usd"]
    crec_p1 = censo["escenarios_salida"]["B_central"]["crecimiento_salida"]
    deltas = p3b2["u_reext_t0"]["componentes_usd"]
    p3b_resto = sum(v for k, v in deltas.items() if k not in ("e1_prefijo_lecturas", "e1_prefijo_escrituras"))
    escenarios = {}
    for nombre, g in (("salida_sin_ponderar", g_out), ("salida_ponderada_por_estrato", g_out_pond)):
        e1 = (N - 5) * pref * PREC["cr"] / 1e6 + 5 * pref * PREC["cw"] / 1e6 + base_in * g_in + base_out * g
        e3 = e3v + render_p1 * max(0.0, g - 1) / crec_p1 + e1r * g
        total = e1 + e3 + p3b_resto
        escenarios[nombre] = {"crecimiento_salida": round(g, 3), "e1_usd": round(e1, 2), "e3_usd": round(e3, 2),
                              "deltas_p3b2_usd": round(p3b_resto, 2), "central_usd": round(total, 2),
                              "por_1_4_usd": round(total * 1.4, 2)}
    out = {"comando": "data/experiment/prompt_r2/p4/costo_real_p4.py --trabajo DIR --muestra M --proyeccion P --salida DIR",
           "costo_real": {"total_usd": gasto["gasto_compartido_usd"], "tope_usd": gasto["tope_usd"],
                          "e1_nuevo_usd": gasto["e1_nuevo"]["gasto_usd_real"],
                          "e1_sellado_api_usd": gasto["e1_sellado_api"]["gasto_usd_real"],
                          "e3_pata_usd": gasto["pata_e3"]["e3"]["gasto_usd_real"],
                          "e1_reintentos_pata_usd": gasto["pata_e3"]["e1_reintentos"]["gasto_usd_real"],
                          "proyeccion_central_usd": proy["central"], "proyeccion_alta_usd": proy["alto"]},
           "medido": {"prefijo_tokens": pref, "prefijo_tokens_recta_p1": 28568,
                      "entrada_nuevo_sobre_sellado": round(g_in, 3), "salida_nuevo_sobre_sellado": round(g_out, 3),
                      "salida_ponderada_por_estrato": round(g_out_pond, 3),
                      "salida_supuesta_p1": round(1 + crec_p1, 4)},
           "u_reext_t0": escenarios, "tope_vigente_usd": 72}
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "costo_real_p4.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
