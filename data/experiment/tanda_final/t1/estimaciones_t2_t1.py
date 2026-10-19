"""
estimaciones_t2_t1.py — B6.1, tanda final, T1, punto 2.9: la duración y el costo estimados de T2. USD 0, sin API. Solo lee.

- **La duración:** la de los tres lanzamientos de T2 de la tanda 1, sumada desde su registro de avance
  (`data/experiment/tanda1/t2/avance_t2.jsonl`: de cada `inicio_lanzador` a su `fin_lanzador`; su FRENO T2, §7, dice
  813,2 min), escalada a la tanda final de dos maneras: por unidades (3.290 → U de la tanda final) y, como información, por
  caracteres de la E0 completa (`chars_completo` de la E0 de cada tanda). Las dos son proyecciones, no mediciones. Por tramo,
  con la misma regla. El freno por id de modelo corre 1 + 98 veces (antes del primer TO y después de cada uno); su costo de
  tiempo se suma con la duración medida de una corrida de --segundos-freno.
- **El costo:** el estimado del manifiesto de la tanda final (la suma de `limites.estimado_usd`), el mismo con la razón de la
  tanda 1 (`salida_cifras_preregistro_tanda_final.json`, `costo.razon_tanda1`) y el tope, con el margen.
Uso: python3 -I -B estimaciones_t2_t1.py --repo <raíz> --segundos-freno <s> --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.dont_write_bytecode = True
AVANCE_T1 = "data/experiment/tanda1/t2/avance_t2.jsonl"
MAN_T1 = "data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json"
MAN_TF = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
CIFRAS = "data/experiment/tanda_final/preregistro/salida_cifras_preregistro_tanda_final.json"
N_TRAMO_1 = 30


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def e0(repo: Path, man: dict) -> dict[str, tuple[int, int]]:
    d = repo / man["rutas"]["e0_salida"]
    out = {}
    for to in man["orden_corrida"]:
        ch = leer(d / f"chunks_{to}.json")
        out[to] = (len(ch), sum(c["chars_completo"] for c in ch))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--segundos-freno", type=float, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    ev = [json.loads(x) for x in (r / AVANCE_T1).read_text(encoding="utf-8").splitlines() if x.strip()]
    ini = [datetime.strptime(e["ts"], "%Y-%m-%dT%H:%M:%S%z") for e in ev if e["evento"] == "inicio_lanzador"]
    fin = [datetime.strptime(e["ts"], "%Y-%m-%dT%H:%M:%S%z") for e in ev if e["evento"] == "fin_lanzador"]
    assert len(ini) == len(fin) == 3
    lanz = [(f - i).total_seconds() / 60 for i, f in zip(ini, fin)]
    min_t1 = sum(lanz)
    m1, mf = leer(r / MAN_T1), leer(r / MAN_TF)
    e1, ef = e0(r, m1), e0(r, mf)
    u1, c1 = sum(x[0] for x in e1.values()), sum(x[1] for x in e1.values())
    tramos = {"tramo_1": mf["orden_corrida"][:N_TRAMO_1], "tramo_2": mf["orden_corrida"][N_TRAMO_1:]}
    uf, cf = sum(x[0] for x in ef.values()), sum(x[1] for x in ef.values())
    s_por_unidad = min_t1 * 60 / u1
    s_por_caracter = min_t1 * 60 / c1
    freno_min = (1 + len(mf["orden_corrida"])) * a.segundos_freno / 60
    dur = {"tanda_1_lanzamientos_min": [round(x, 2) for x in lanz], "tanda_1_total_min": round(min_t1, 2),
           "tanda_1_unidades": u1, "tanda_1_chars_completo": c1, "segundos_por_unidad": round(s_por_unidad, 2),
           "por_unidades": {"tanda_final_unidades": uf, "min": round(uf * s_por_unidad / 60, 1),
                            "horas": round(uf * s_por_unidad / 3600, 2),
                            **{k: {"unidades": sum(ef[t][0] for t in v),
                                   "min": round(sum(ef[t][0] for t in v) * s_por_unidad / 60, 1)} for k, v in tramos.items()}},
           "por_caracteres_informacion": {"tanda_final_chars_completo": cf, "min": round(cf * s_por_caracter / 60, 1),
                                          "horas": round(cf * s_por_caracter / 3600, 2),
                                          **{k: {"chars_completo": sum(ef[t][1] for t in v),
                                                 "min": round(sum(ef[t][1] for t in v) * s_por_caracter / 60, 1)}
                                             for k, v in tramos.items()}},
           "freno_por_modelo": {"corridas": 1 + len(mf["orden_corrida"]), "segundos_por_corrida_medidos": a.segundos_freno,
                                "min": round(freno_min, 1)}}
    est = sum(Decimal(str(v["e1"])) + Decimal(str(v["e3"])) for v in mf["limites"]["estimado_usd"].values())
    razon = Decimal(str(leer(r / CIFRAS)["costo"]["razon_tanda1"]))
    tope = Decimal(str(mf["limites"]["tope_global_usd"]))
    q4 = lambda x: str(x.quantize(Decimal("0.0001"), ROUND_HALF_UP))  # noqa: E731
    costo = {"estimado_usd": str(est), "estimado_a_4_decimales": q4(est), "razon_tanda1": str(razon),
             "estimado_con_la_razon_de_la_tanda_1_usd": q4(est * razon), "tope_usd": str(tope),
             "margen_sobre_el_estimado_usd": q4(tope - est), "tope_sobre_estimado": q4(tope / est),
             **{f"{k}_estimado_usd": str(sum(Decimal(str(mf["limites"]["estimado_usd"][t]["e1"]))
                                              + Decimal(str(mf["limites"]["estimado_usd"][t]["e3"])) for t in v))
                for k, v in tramos.items()}}
    res = {"duracion": dur, "costo": costo}
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
