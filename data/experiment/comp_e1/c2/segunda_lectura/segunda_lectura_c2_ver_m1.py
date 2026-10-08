"""Visor condensado del material parseado (material.json). Uso: python3 ver.py <unidad> [m1|m2|full]"""
import json
import re
import sys

M = json.load(open("material.json", encoding="utf-8"))


def props_corto(e):
    p = e.get("props")
    if not p:
        return ""
    try:
        d = json.loads(p.strip("`"))
    except Exception:
        return " props=" + p[:120]
    d.pop("umbrales", None)
    return (" " + json.dumps(d, ensure_ascii=False)) if d else ""


def main():
    u = M[sys.argv[1]]
    modo = sys.argv[2] if len(sys.argv) > 2 else "full"
    print("#", u["unidad"], "—", u["titulo"])
    print(u.get("cabecera", ""))
    for k, t in u["texto"]:
        print(f"[{k}] {t}")
    for s in u["supuestos"]:
        print(f"SUP {s['n']}. «{s['frase']}» {s['miembro']}")
    for o in u["omisiones_t4"]:
        print(f"OMI {o['clave']} [{o['attrs']}] «{o['frase']}»")
    for cod, c in u["codigos"].items():
        print(f"\n=== {cod} ===")
        for e in c["entidades"]:
            desc = e["desc"] if modo != "m2" else ""
            um = f" | umbral {e['umbral']}" if e.get("umbral") else ""
            print(f"  {e['id']} {e['tipo']} «{e['label']}»{props_corto(e)} — {desc}{um} | tramo[{e['tramo_nivel']}] «{e['tramo']}»")
        for r in c["relaciones"]:
            print("  R", r)
        for o in c["omisiones"]:
            print(f"  OMIS {o['cat']} [{o['nivel']}] «{o['tramo']}» — {o['nota']}")
        for x in c["otros"]:
            print("  OTRO", x)
        for n, v in c["cand_sup"].items():
            print(f"  >S{n} {v['cand']}")
        for k, v in c["cand_omi"].items():
            print(f"  >O {k} ent: {v['ent']} | omi: {v['omi']}")


main()
