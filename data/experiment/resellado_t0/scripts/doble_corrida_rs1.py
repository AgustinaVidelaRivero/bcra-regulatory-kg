"""Re-sellado único de la tanda 0, §2.1: las seis cadenas y la doble corrida. Para cada cadena r2b, compara archivo por
archivo la primera corrida (en la copia, en corpus_tanda0/ens_<g>_rs1/r2) con la segunda (otro proceso, fuera de la copia):
byte a byte, salvo reporte_ensamblado_r2.json, que guarda en `redirecciones` la ruta de su --salida y las rutas absolutas de
la raíz donde corrió; ese archivo se compara con esas rutas normalizadas y se declara. Además, la tabla de sha256 de los
kg.json de todas las corridas, con lo esperado: las r2a, byte a byte las del laudo de la release r2 (§3); O2 y antes de O2,
las de FRENO_O2.md:80-83 y las de su línea de base. Solo lee.
Uso: python -I -B doble_corrida_rs1.py <copia> <dir de corridas> <salida.json> <salida.tsv>
"""
import hashlib
import json
import sys
from pathlib import Path

C, K, OUT, TSV = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
T0 = C / "data/experiment/reextraccion_v2/corpus_tanda0"
CARP = {"r2b_diez": "ens_diez_r2b_rs1", "r2b_sincola_diez": "ens_diez_r2b_sincola_rs1",
        "r2b_desarrollo": "ens_desarrollo_r2b_rs1", "r2b_sincola_desarrollo": "ens_desarrollo_r2b_sincola_rs1"}
ESPERADO = {("r2a", "r2a_diez"): "70d51e42", ("r2a", "r2a_desarrollo"): "fa4c1043",
            ("o2", "r2b_diez"): "710664e9", ("o2", "r2b_sincola_diez"): "a50210b4",
            ("o2", "r2b_desarrollo"): "18a2747d", ("o2", "r2b_sincola_desarrollo"): "9f49d62d",
            ("preO2", "r2b_diez"): "40c54830", ("preO2", "r2b_sincola_diez"): "8d747e57",
            ("preO2", "r2b_desarrollo"): "6e756043", ("preO2", "r2b_sincola_desarrollo"): "2922b72d"}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def norm_reporte(p: Path, raiz: str) -> dict:
    r = json.loads(p.read_text(encoding="utf-8"))
    for x in r.get("redirecciones", []):
        if isinstance(x["valor"], str):
            x["valor"] = x["valor"].replace(raiz, "<RAIZ>")
            if x["atributo"] == "SALIDA_R1":
                x["valor"] = "<SALIDA>/r2"
    return r


res = {"doble_corrida": {}, "cadenas": []}
for g, carp in CARP.items():
    a, b = T0 / carp / "r2", K / "run2" / g / "r2"
    fa = sorted(p.relative_to(a).as_posix() for p in a.rglob("*") if p.is_file())
    fb = sorted(p.relative_to(b).as_posix() for p in b.rglob("*") if p.is_file())
    distintos = [f for f in sorted(set(fa) & set(fb)) if (a / f).read_bytes() != (b / f).read_bytes()]
    rep_igual_normalizado = (norm_reporte(a / "reporte_ensamblado_r2.json", str(C))
                             == norm_reporte(b / "reporte_ensamblado_r2.json", str(C)))
    res["doble_corrida"][g] = {"archivos": [len(fa), len(fb)], "mismos_nombres": fa == fb, "distintos": distintos,
                               "reporte_igual_con_las_rutas_normalizadas": rep_igual_normalizado,
                               "kg_sha256": [sha(a / "kg.json"), sha(b / "kg.json")],
                               "doble_corrida_interna": [json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))["doble_corrida_byte_identica"] for d in (a, b)]}
    for corrida, d in (("run1", a), ("run2", b)):
        res["cadenas"].append({"corrida": corrida, "grafo": g, "kg_sha256": sha(d / "kg.json"), "esperado": None})
for (corrida, g), esp in ESPERADO.items():
    d = K / corrida / g / "r2"
    s = sha(d / "kg.json")
    res["cadenas"].append({"corrida": corrida, "grafo": g, "kg_sha256": s, "esperado": esp, "igual": s.startswith(esp),
                           "doble_corrida_interna": json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))["doble_corrida_byte_identica"]})
res["ok"] = (all(v["mismos_nombres"] and v["distintos"] in ([], ["reporte_ensamblado_r2.json"])
                 and v["reporte_igual_con_las_rutas_normalizadas"] and v["kg_sha256"][0] == v["kg_sha256"][1]
                 and all(v["doble_corrida_interna"]) for v in res["doble_corrida"].values())
             and all(c.get("igual", True) for c in res["cadenas"]))
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
with TSV.open("w", encoding="utf-8") as f:
    f.write("corrida\tgrafo\tkg_sha256\tesperado\n")
    for c in res["cadenas"]:
        f.write(f"{c['corrida']}\t{c['grafo']}\t{c['kg_sha256']}\t{c['esperado'] or '-'}\n")
for g, v in res["doble_corrida"].items():
    print(g, v["archivos"], "distintos:", v["distintos"], "| reporte normalizado igual:", v["reporte_igual_con_las_rutas_normalizadas"],
          "| kg:", v["kg_sha256"][0][:8], "| interna:", v["doble_corrida_interna"])
print("cadenas con esperado:", [(c["corrida"], c["grafo"], c["kg_sha256"][:8], c["igual"]) for c in res["cadenas"] if c["esperado"]])
print("OK" if res["ok"] else "CON FALLAS")
