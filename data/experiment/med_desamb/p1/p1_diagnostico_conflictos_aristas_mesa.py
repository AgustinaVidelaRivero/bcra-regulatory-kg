"""Mesa, §140 (17/10/2026), U-MED-DESAMB, P1 como diagnóstico aparte (decisión de la autora): los conflictos de marcas de arista que el
ensamblado no registra, sobre grafos sellados y sin tocar el ensamblado. USD 0, sin API. Lee el reporte y el kg sellados y no escribe
fuera de --salida.

Dos cuentas:
  1. dentro de cada documento: `stats.aristas_con_marcas_distintas` del reporte sellado (e2_lib.py:981-982 la cuenta al unir dos
     aristas iguales con marcas distintas; el detalle no se guarda, así que la cifra es solo un conteo);
  2. entre documentos: las aristas del kg cuya procedencia viene de más de un documento. El merge sellado deja la primera y no registra
     las marcas de las demás (ensamblar_corpus.py:193-205): es la cota de los conflictos posibles, no su cuenta.
Lo que no se puede sin volver a ensamblar: los valores perdidos. Eso queda para el grafo corregido del cap. 6.
Uso: python3 -I -B p1_diagnostico_conflictos_aristas_mesa.py --ens <dir r2 del ensamblado> [--ens ...] --salida <dir>
     python3 -I -B p1_diagnostico_conflictos_aristas_mesa.py --selftest"""
import argparse
import collections
import hashlib
import json
import sys
from pathlib import Path


def diagnostico(rep, kg):
    intra = {to: (v.get("stats") or {}).get("aristas_con_marcas_distintas") for to, v in (rep.get("e2_por_to") or {}).items()}
    entre = collections.Counter()
    for e in kg["edges"]:
        tos = {p.get("to") for p in e.get("provenances") or [] if p.get("to")}
        if len(tos) > 1:
            entre[e["relation"]] += 1
    return {"dentro_de_cada_documento": intra, "dentro_total": sum(v or 0 for v in intra.values()),
            "entre_documentos_aristas_con_procedencia_de_mas_de_un_documento": dict(entre.most_common()),
            "entre_total": sum(entre.values()), "merge_del_reporte": rep.get("merge")}


def _selftest():
    rep = {"e2_por_to": {"a": {"stats": {"aristas_con_marcas_distintas": 2}}, "b": {"stats": {"aristas_con_marcas_distintas": 0}}}}
    kg = {"edges": [{"relation": "aplica_a", "provenances": [{"to": "a"}, {"to": "b"}]}, {"relation": "aplica_a", "provenances": [{"to": "a"}]},
                    {"relation": "miembro_de", "provenances": [{"to": "a"}, {"to": "b"}, {"to": "c"}]}]}
    d = diagnostico(rep, kg)
    ok = d["dentro_total"] == 2 and d["entre_total"] == 2 and d["entre_documentos_aristas_con_procedencia_de_mas_de_un_documento"] == {"aplica_a": 1, "miembro_de": 1}
    print(("OK   " if ok else "FALLA") + " P1: 2 dentro de los documentos y 2 aristas con procedencia de más de un documento")
    print("FALLAS:", 0 if ok else 1)
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ens", action="append")
    ap.add_argument("--salida")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        raise SystemExit(_selftest())
    out = {}
    for d in a.ens:
        d = Path(d)
        b = (d / "kg.json").read_bytes()
        rep = json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
        r = diagnostico(rep, json.loads(b))
        out[hashlib.sha256(b).hexdigest()[:8]] = {"ensamblado": d.parent.name, **r}
        print(f"{hashlib.sha256(b).hexdigest()[:8]} {d.parent.name}: dentro {r['dentro_total']} {r['dentro_de_cada_documento']} | entre {r['entre_total']} "
              f"{r['entre_documentos_aristas_con_procedencia_de_mas_de_un_documento']} | merge {r['merge_del_reporte']}")
    S = Path(a.salida)
    S.mkdir(parents=True, exist_ok=True)
    (S / "p1_diagnostico.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
