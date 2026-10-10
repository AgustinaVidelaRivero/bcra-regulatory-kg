"""U-OMISIONES-COD, O2 — la salida de cada cadena r2b con el código de O1 (HEAD + o1/parche/parche_O1_completo.diff) contra la
de O2, archivo por archivo: qué cambia del agrupamiento sin el rol (lo único que O2 cambia en el código de la cadena). Solo lee.
Uso: python3 -I o1_contra_o2.py nombre=<r2 O1>,<r2 O2> [...] --out <json>"""
import argparse, hashlib, json, sys
from collections import Counter
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("par", nargs="+"); ap.add_argument("--out", type=Path, required=True); a = ap.parse_args()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
res = {}
for x in a.par:
    nom, rutas = x.split("=", 1); d1, d2 = [Path(r) for r in rutas.split(",")]
    k1, k2 = json.loads((d1 / "kg.json").read_text(encoding="utf-8")), json.loads((d2 / "kg.json").read_text(encoding="utf-8"))
    e1 = {(e["source"], e["relation"], e["target"]): e for e in k1["edges"]}; e2 = {(e["source"], e["relation"], e["target"]): e for e in k2["edges"]}
    f1 = {str(p.relative_to(d1)) for p in d1.rglob("*") if p.is_file()}; f2 = {str(p.relative_to(d2)) for p in d2.rglob("*") if p.is_file()}
    r1 = json.loads((d1 / "reporte_ensamblado_r2.json").read_text(encoding="utf-8")); r2 = json.loads((d2 / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    res[nom] = {"sha256_o1": sha(d1 / "kg.json"), "sha256_o2": sha(d2 / "kg.json"), "nodos_iguales": k1["nodes"] == k2["nodes"],
                "aristas_salen": dict(Counter(k[1] for k in set(e1) - set(e2))), "aristas_entran": dict(Counter(k[1] for k in set(e2) - set(e1))),
                "aristas_cambian": dict(Counter(k[1] for k in set(e1) & set(e2) if e1[k] != e2[k])),
                "archivos_distintos": sorted(f for f in f1 & f2 if sha(d1 / f) != sha(d2 / f)), "archivos_solo_en_uno": sorted(f1 ^ f2),
                "claves_del_reporte_que_cambian": sorted(k for k in set(r1) | set(r2) if r1.get(k) != r2.get(k) and k != "redirecciones")}
    print(nom, json.dumps(res[nom], ensure_ascii=False))
a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
