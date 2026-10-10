"""U-OMISIONES-COD, O1 — diferencia entre dos salidas `r2/` del ensamblado (antes y después de un cambio de código):
nodos y aristas que entran, salen o cambian, con los campos que cambian, y los archivos del directorio que difieren.
Solo lee. Uso: python -B diff_grafos.py <dir r2 antes> <dir r2 después> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path


def cargar(p: Path) -> dict:
    return json.loads((p / "kg.json").read_text(encoding="utf-8"))


def campos_distintos(a: dict, b: dict, prefijo: str = "") -> list[str]:
    out = []
    for k in sorted(set(a) | set(b)):
        va, vb = a.get(k, "<ausente>"), b.get(k, "<ausente>")
        if va == vb:
            continue
        if isinstance(va, dict) and isinstance(vb, dict):
            out += campos_distintos(va, vb, f"{prefijo}{k}.")
        else:
            out.append(f"{prefijo}{k}")
    return out


def comparar(da: Path, db: Path) -> dict:
    A, B = cargar(da), cargar(db)
    na, nb = {n["id"]: n for n in A["nodes"]}, {n["id"]: n for n in B["nodes"]}
    ka = lambda e: (e["source"], e["relation"], e["target"])  # noqa: E731
    ea, eb = {ka(e): e for e in A["edges"]}, {ka(e): e for e in B["edges"]}
    nodos_cambian = {i: campos_distintos(na[i], nb[i]) for i in na if i in nb and na[i] != nb[i]}
    aristas_cambian = {"|".join(k): campos_distintos(ea[k], eb[k]) for k in ea if k in eb and ea[k] != eb[k]}
    archivos = OrderedDict()
    for p in sorted({x.relative_to(da) for x in da.rglob("*") if x.is_file()}
                    | {x.relative_to(db) for x in db.rglob("*") if x.is_file()}):
        fa, fb = da / p, db / p
        ha = hashlib.sha256(fa.read_bytes()).hexdigest() if fa.exists() else None
        hb = hashlib.sha256(fb.read_bytes()).hexdigest() if fb.exists() else None
        if ha != hb:
            archivos[str(p)] = [ha and ha[:12], hb and hb[:12]]
    return OrderedDict([
        ("sha256_antes", hashlib.sha256((da / "kg.json").read_bytes()).hexdigest()),
        ("sha256_despues", hashlib.sha256((db / "kg.json").read_bytes()).hexdigest()),
        ("nodos", [len(A["nodes"]), len(B["nodes"])]), ("aristas", [len(A["edges"]), len(B["edges"])]),
        ("nodos_que_entran", sorted(set(nb) - set(na))), ("nodos_que_salen", sorted(set(na) - set(nb))),
        ("aristas_que_entran", sorted("|".join(k) for k in set(eb) - set(ea))),
        ("aristas_que_salen", sorted("|".join(k) for k in set(ea) - set(eb))),
        ("nodos_que_cambian", len(nodos_cambian)),
        ("nodos_que_cambian_por_campo", dict(Counter(c for cs in nodos_cambian.values() for c in cs))),
        ("aristas_que_cambian", len(aristas_cambian)),
        ("aristas_que_cambian_por_campo", dict(Counter(c for cs in aristas_cambian.values() for c in cs))),
        ("nodos_que_cambian_lista", nodos_cambian), ("aristas_que_cambian_lista", aristas_cambian),
        ("archivos_distintos", archivos)])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("antes", type=Path)
    ap.add_argument("despues", type=Path)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    r = comparar(a.antes, a.despues)
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in r.items() if not k.endswith("_lista")}, ensure_ascii=False)[:4000])
    return 0


if __name__ == "__main__":
    sys.exit(main())
