"""Re-sellado único de la tanda 0, §3.1 y §3.2: la tabla de lo que cambia en las shapes y en la suite de cada grafo
re-sellado contra el de O2 (reproducido sobre una copia) y contra el sellado (las salidas del gate guardadas en su
ensamblado). Solo lee los JSON de shapes_validator.py y regression_kg.py.
Uso: python -I -B tablas_gate_rs1.py --par <nombre>=<dir gate nuevo>,<dir gate O2>,<dir gate sellado> [...] --out <json>
"""
import argparse
import json
import sys
from pathlib import Path


def leer(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def tab_shapes(d: Path) -> dict:
    sh = leer(d / "shapes_perfil_r2_fase_r2b.json")
    return {"veredicto": sh["veredicto"], "bloqueantes_en_fail": sh["bloqueantes_en_fail"],
            "por_resultado": {r: sum(1 for v in sh["shapes"].values() if v.get("result") == r) for r in ("PASS", "FAIL", "WARN")},
            "shapes": {k: (v.get("result"), v.get("severidad"), v.get("conteos")) for k, v in sh["shapes"].items()}}


def tab_suite(d: Path) -> dict:
    su = leer(d / "suite_perfil_r2.json")
    reg = su.get("regresion") or {}
    return {"resumen": su["resumen"], "entrada": reg.get("entrada"), "n_regresiones": reg.get("n_regresiones"),
            "regresiones": [x["item"] for x in reg.get("regresiones", [])], "coinciden": reg.get("coinciden"),
            "no_verificadas": len(reg.get("no_verificadas", [])),
            "items": {i["id"]: (i["estado"], i.get("detalle")) for i in su["items"]}}


def comparar(a: dict, b: dict) -> dict:
    sh = {k: {"antes": a["shapes"]["shapes"].get(k), "despues": v} for k, v in b["shapes"]["shapes"].items()
          if a["shapes"]["shapes"].get(k) != v}
    est = {i: [a["suite"]["items"][i][0], v[0]] for i, v in b["suite"]["items"].items()
           if i in a["suite"]["items"] and a["suite"]["items"][i][0] != v[0]}
    det = sorted(i for i, v in b["suite"]["items"].items() if i in a["suite"]["items"] and a["suite"]["items"][i][1] != v[1])
    return {"shapes_que_cambian_de_resultado": {k: [(x["antes"] or [None])[0], x["despues"][0]] for k, x in sh.items()
                                               if (x["antes"] or [None])[0] != x["despues"][0]},
            "shapes_que_cambian_solo_de_conteos": sorted(k for k, x in sh.items() if x["antes"] and x["antes"][0] == x["despues"][0]),
            "conteos_que_cambian": {k: {"antes": (x["antes"] or [None, None, None])[2], "despues": x["despues"][2]} for k, x in sh.items()},
            "suite_items_que_cambian_de_estado": est, "suite_items_que_cambian_de_detalle": det}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--par", action="append", required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    res = {}
    for p in a.par:
        nom, rutas = p.split("=", 1)
        dn, do, ds = [Path(x) for x in rutas.split(",")]
        g = {k: {"shapes": tab_shapes(d), "suite": tab_suite(d)} for k, d in (("nuevo", dn), ("o2", do), ("sellado", ds))}
        res[nom] = {"nuevo": {"shapes": {k: v for k, v in g["nuevo"]["shapes"].items() if k != "shapes"},
                              "suite": {k: v for k, v in g["nuevo"]["suite"].items() if k != "items"}},
                    "o2": {"shapes": {k: v for k, v in g["o2"]["shapes"].items() if k != "shapes"},
                           "suite_resumen": g["o2"]["suite"]["resumen"]},
                    "sellado": {"shapes": {k: v for k, v in g["sellado"]["shapes"].items() if k != "shapes"},
                                "suite_resumen": g["sellado"]["suite"]["resumen"],
                                "suite_regresiones": g["sellado"]["suite"]["regresiones"]},
                    "contra_o2": comparar(g["o2"], g["nuevo"]), "contra_sellado": comparar(g["sellado"], g["nuevo"])}
        r = res[nom]
        print(nom, "| shapes", r["nuevo"]["shapes"]["veredicto"], r["nuevo"]["shapes"]["por_resultado"],
              "bloq en fail", r["nuevo"]["shapes"]["bloqueantes_en_fail"], "| suite", r["nuevo"]["suite"]["resumen"],
              "regresiones", r["nuevo"]["suite"]["regresiones"])
        for c in ("contra_o2", "contra_sellado"):
            x = r[c]
            print(f"   {c}: shapes cambian de resultado {x['shapes_que_cambian_de_resultado']}; solo conteos "
                  f"{x['shapes_que_cambian_solo_de_conteos']}; suite estados {x['suite_items_que_cambian_de_estado']}; "
                  f"detalle {x['suite_items_que_cambian_de_detalle']}")
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
