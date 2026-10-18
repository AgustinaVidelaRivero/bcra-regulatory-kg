"""B6.1, tanda 1, T3, punto 4: las tablas del gate (shapes y suite) de cada grafo nuevo contra el grafo anterior, el de la tanda 0
re-sellado (sus salidas del gate guardadas en su ensamblado), con el modelo de data/experiment/resellado_t0/scripts/tablas_gate_rs1.py.
Solo lee los JSON de shapes_validator.py y regression_kg.py.
Uso: python3 -I -B tablas_gate_t3.py --par <nombre>=<dir gate nuevo>,<dir gate del grafo anterior> [...] [--extra <nombre>=<dir>] --out <json>
  --extra: otra corrida de shapes del mismo grafo (p. ej., con otra E0), que se tabula aparte.
"""
import argparse
import json
from pathlib import Path


def leer(p: Path) -> dict:
    return json.loads(p.read_text(encoding="utf-8"))


def tab_shapes(d: Path) -> dict:
    sh = leer(d / "shapes_perfil_r2_fase_r2b.json")
    return {"veredicto": sh["veredicto"], "bloqueantes_en_fail": sh["bloqueantes_en_fail"],
            "por_resultado": {r: sum(1 for v in sh["shapes"].values() if v.get("result") == r) for r in ("PASS", "FAIL", "WARN")},
            "no_pass": {k: [v.get("result"), v.get("severidad")] for k, v in sh["shapes"].items() if v.get("result") != "PASS"},
            "S31": sh["shapes"]["S31"].get("resumen"), "e0": sh.get("e0"),
            "shapes": {k: (v.get("result"), v.get("severidad"), v.get("conteos")) for k, v in sh["shapes"].items()}}


def tab_suite(d: Path) -> dict | None:
    p = d / "suite_perfil_r2.json"
    if not p.exists():
        return None
    su = leer(p)
    reg = su.get("regresion") or {}
    return {"resumen": su["resumen"], "entrada": reg.get("entrada"), "n_regresiones": reg.get("n_regresiones"),
            "regresiones": [{k: x.get(k) for k in ("item", "esperado", "medido", "detalle") if k in x} for x in reg.get("regresiones", [])],
            "coinciden": reg.get("coinciden"), "no_verificadas": len(reg.get("no_verificadas", [])),
            "items": {i["id"]: (i["estado"], i.get("detalle")) for i in su["items"]}}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--par", action="append", required=True)
    ap.add_argument("--extra", action="append", default=[])
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    res = {"grafos": {}, "extra": {}}
    for p in a.par:
        nom, rutas = p.split("=", 1)
        dn, da = [Path(x) for x in rutas.split(",")]
        n, an = {"shapes": tab_shapes(dn), "suite": tab_suite(dn)}, {"shapes": tab_shapes(da), "suite": tab_suite(da)}
        cambio_sh = {k: [an["shapes"]["shapes"].get(k, [None])[0], v[0]] for k, v in n["shapes"]["shapes"].items()
                     if an["shapes"]["shapes"].get(k, [None])[0] != v[0]}
        est = ({i: [an["suite"]["items"][i][0], v[0]] for i, v in n["suite"]["items"].items()
                if i in an["suite"]["items"] and an["suite"]["items"][i][0] != v[0]} if n["suite"] and an["suite"] else None)
        res["grafos"][nom] = {
            "nuevo": {"shapes": {k: v for k, v in n["shapes"].items() if k != "shapes"},
                      "suite": {k: v for k, v in (n["suite"] or {}).items() if k != "items"} or None},
            "anterior": {"shapes": {k: v for k, v in an["shapes"].items() if k != "shapes"},
                         "suite_resumen": (an["suite"] or {}).get("resumen")},
            "shapes_que_cambian_de_resultado_contra_el_anterior": cambio_sh,
            "suite_items_que_cambian_de_estado_contra_el_anterior": est}
    for p in a.extra:
        nom, ruta = p.split("=", 1)
        res["extra"][nom] = {k: v for k, v in tab_shapes(Path(ruta)).items() if k != "shapes"}
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for nom, g in res["grafos"].items():
        s, su = g["nuevo"]["shapes"], g["nuevo"]["suite"] or {}
        print(f"{nom}: shapes {s['veredicto']} {s['por_resultado']} bloqueantes en FAIL {s['bloqueantes_en_fail']} | suite "
              f"{su.get('resumen')} entrada {su.get('entrada')} regresiones {su.get('n_regresiones')}")
    for nom, s in res["extra"].items():
        print(f"{nom} (extra): shapes {s['veredicto']} {s['por_resultado']} bloqueantes en FAIL {s['bloqueantes_en_fail']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
