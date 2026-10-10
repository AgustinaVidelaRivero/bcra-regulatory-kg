"""U-OMISIONES-COD, O2 — sha256 de kg.json de cada cadena (HEAD, O2 corrida 1, O2 corrida 2 en otro proceso, O2 con la pieza
(e)), la doble corrida interna del ensamblado (`doble_corrida_byte_identica` del reporte) y la comparación archivo por archivo
de las dos corridas de O2. Solo lee. Uso: python3 -I cadenas_y_doble_corrida.py <dir corridas> --tsv <tsv> --out <json>"""
import argparse, hashlib, json, sys
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("corridas", type=Path); ap.add_argument("--tsv", type=Path, required=True)
ap.add_argument("--out", type=Path, required=True); a = ap.parse_args()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
filas, res = [], {"doble_corrida_interna": {}, "corrida_1_contra_corrida_2": {}}
for cod in ("head", "o2_1", "o2_2", "pieza_e"):
    for d in sorted((a.corridas / cod).glob("r2*")):
        k = d / "r2" / "kg.json"
        if not k.exists():
            continue
        rep = json.loads((d / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
        rc = [l for l in (a.corridas / cod / f"consola_{d.name}.txt").read_text(encoding="utf-8").splitlines() if l.startswith("rc=")]
        filas.append((cod, d.name, sha(k), rep.get("doble_corrida_byte_identica"), rc[-1] if rc else None))
        res["doble_corrida_interna"][f"{cod}/{d.name}"] = rep.get("doble_corrida_byte_identica")
for d in sorted((a.corridas / "o2_2").glob("r2*")):
    d1 = a.corridas / "o2_1" / d.name
    f1 = {str(p.relative_to(d1)) for p in d1.rglob("*") if p.is_file()}
    f2 = {str(p.relative_to(d)) for p in d.rglob("*") if p.is_file()}
    dist = sorted(f for f in f1 & f2 if sha(d1 / f) != sha(d / f))
    rep_sin = None
    if "r2/reporte_ensamblado_r2.json" in dist:
        r1 = json.loads((d1 / "r2/reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
        r2 = json.loads((d / "r2/reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
        rep_sin = sorted(k for k in set(r1) | set(r2) if r1.get(k) != r2.get(k))
    res["corrida_1_contra_corrida_2"][d.name] = {"archivos": len(f1), "solo_en_una": sorted(f1 ^ f2), "distintos": dist,
                                                 "claves_del_reporte_que_difieren": rep_sin}
a.tsv.write_text("corrida\tcadena\tsha256_kg\tdoble_corrida_interna\trc\n" +
                 "".join(f"{c}\t{n}\t{s}\t{b}\t{r}\n" for c, n, s, b, r in filas), encoding="utf-8")
a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(a.tsv.read_text(encoding="utf-8")); print(json.dumps(res["corrida_1_contra_corrida_2"], ensure_ascii=False))
