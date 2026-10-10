"""U-OMISIONES-COD, O2 — el grupo J aislado con el código de O2: la misma cadena con la procedencia propia apagada
(`procedencia_propia=False`, el resto igual: una copia con esa sola línea cambiada en `ensamblar_tanda0.py`) contra la de
O2. La aceptación de J (v7): las mismas aristas, con el mismo origen, destino y evidencia; cambia solo la procedencia, con la
lista de cambios por causa. Solo lee.

Causas, por arista `remite_a` que cambia:
  tramo_del_propio_origen  la procedencia principal pasa a la del propio origen, con su tramo;
  marca_sin_tramo          la cita del texto heredado: procedencia sin tramo, con `tramo_verificado` «ausente»;
  solo_provenances         la principal no cambia y cambia la lista `provenances`;
  otro                     cualquier otro campo (el control es que no haya ninguna).
Uso: python3 -I j_aislado.py <r2 sin J> <r2 O2> --out <json>
"""
import argparse
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("sin_j", type=Path)
    ap.add_argument("o2", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    ka = json.loads((a.sin_j / "kg.json").read_text(encoding="utf-8"))
    kb = json.loads((a.o2 / "kg.json").read_text(encoding="utf-8"))
    ea = {(e["source"], e["relation"], e["target"]): e for e in ka["edges"]}
    eb = {(e["source"], e["relation"], e["target"]): e for e in kb["edges"]}
    causas, filas, otros = Counter(), [], []
    for k in sorted(set(ea) & set(eb)):
        x, y = ea[k], eb[k]
        if x == y:
            continue
        campos = sorted(f for f in set(x) | set(y) if x.get(f) != y.get(f))
        if k[1] != "remite_a" or set(campos) - {"provenance", "provenances"}:
            otros.append({"arista": "|".join(k), "campos": campos})
            continue
        if x["provenance"] != y["provenance"]:
            p = y["provenance"]
            if p.get("tramo") is None and p.get("tramo_verificado") == "ausente":
                c = "marca_sin_tramo"
            else:
                c = "tramo_del_propio_origen"
        else:
            c = "solo_provenances"
        causas[c] += 1
        filas.append({"arista": "|".join(k), "causa": c, "campos": campos})
    fa = {str(p.relative_to(a.sin_j)) for p in a.sin_j.rglob("*") if p.is_file()}
    fb = {str(p.relative_to(a.o2)) for p in a.o2.rglob("*") if p.is_file()}
    sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
    res = OrderedDict([
        ("sha256_sin_j", sha(a.sin_j / "kg.json")), ("sha256_o2", sha(a.o2 / "kg.json")),
        ("nodos_iguales", ka["nodes"] == kb["nodes"]),
        ("mismas_aristas", sorted(ea) == sorted(eb)), ("aristas", len(eb)),
        ("remite_a", sum(1 for k in eb if k[1] == "remite_a")),
        ("misma_evidencia_y_destino", all(ea[k]["properties"] == eb[k]["properties"] for k in eb if k[1] == "remite_a")),
        ("resto_del_kg_igual", {x: ka[x] == kb[x] for x in ka if x not in ("nodes", "edges")}),
        ("remite_a_que_cambian", len(filas)), ("por_causa", dict(sorted(causas.items()))),
        ("cambios_fuera_de_la_procedencia", otros),
        ("archivos_distintos", sorted(f for f in fa & fb if sha(a.sin_j / f) != sha(a.o2 / f))),
        ("archivos_solo_en_uno", sorted(fa ^ fb)),
        ("lista", filas)])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in res.items() if k != "lista"}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
