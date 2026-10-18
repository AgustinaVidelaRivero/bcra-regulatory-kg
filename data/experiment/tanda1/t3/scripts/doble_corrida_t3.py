"""B6.1, tanda 1, T3, puntos 3 y 4: la doble corrida de los cuatro ensamblados nuevos y la reproducibilidad de los sellados, con el
modelo de data/experiment/resellado_t0/scripts/doble_corrida_rs1.py. Solo lee.
  - Doble corrida: para cada grafo nuevo, compara archivo por archivo la primera corrida (en la copia, en su carpeta final) con la
    segunda (otro proceso, fuera de la copia): byte a byte, salvo reporte_ensamblado_r2.json, que guarda en `redirecciones` la ruta de
    su --salida y las rutas absolutas de la raíz donde corrió; ese archivo se compara con esas rutas normalizadas y se declara.
  - Reproducibilidad (laudo de la release r2, §3, punto 4): las cadenas r2a dan 70d51e42… y fa4c1043…, y las cuatro r2b de la tanda 0
    con los manifiestos _rs1 dan los re-sellados byte a byte (sha256 enteros de resellado_t0/FRENO_resellado_T0.md:68-71).
Uso: python3 -I -B doble_corrida_t3.py <copia> <dir de corridas> <salida.json> <salida.tsv>
"""
import hashlib
import json
import sys
from pathlib import Path

C, K, OUT, TSV = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
X = "data/experiment/reextraccion_v2"
CARP = {"t1_veinte": f"{X}/corpus_tanda1/ens_veinte_r2b", "t1_veinte_sincola": f"{X}/corpus_tanda1/ens_veinte_r2b_sincola",
        "acum_treinta": "data/experiment/tanda1/t3/acumulado/ens_treinta_r2b",
        "acum_treinta_sincola": "data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola"}
ESPERADO = {"r2a_diez": "70d51e42", "r2a_desarrollo": "fa4c1043",
            "r2b_diez": "fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea",
            "r2b_desarrollo": "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31",
            "r2b_sincola_diez": "61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738",
            "r2b_sincola_desarrollo": "66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c"}


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


def interna(d: Path):
    return json.loads((d / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))["doble_corrida_byte_identica"]


res = {"doble_corrida": {}, "cadenas": []}
for g, carp in CARP.items():
    a, b = C / carp / "r2", K / "run2" / g / "r2"
    fa = sorted(p.relative_to(a).as_posix() for p in a.rglob("*") if p.is_file())
    fb = sorted(p.relative_to(b).as_posix() for p in b.rglob("*") if p.is_file())
    distintos = [f for f in sorted(set(fa) & set(fb)) if (a / f).read_bytes() != (b / f).read_bytes()]
    rep = norm_reporte(a / "reporte_ensamblado_r2.json", str(C)) == norm_reporte(b / "reporte_ensamblado_r2.json", str(C))
    kg = json.loads((a / "kg.json").read_text(encoding="utf-8"))
    res["doble_corrida"][g] = {"carpeta": carp, "archivos": [len(fa), len(fb)], "mismos_nombres": fa == fb, "distintos": distintos,
                               "reporte_igual_con_las_rutas_normalizadas": rep,
                               "kg_sha256": [sha(a / "kg.json"), sha(b / "kg.json")],
                               "nodos": len(kg["nodes"]), "aristas": len(kg["edges"]),
                               "doble_corrida_interna": [interna(a), interna(b)]}
for g, esp in ESPERADO.items():
    d = K / "repro" / g / "r2"
    s = sha(d / "kg.json")
    res["cadenas"].append({"corrida": "repro", "grafo": g, "kg_sha256": s, "esperado": esp,
                           "igual": s == esp if len(esp) == 64 else s.startswith(esp), "doble_corrida_interna": interna(d)})
res["ok"] = (all(v["mismos_nombres"] and v["distintos"] in ([], ["reporte_ensamblado_r2.json"])
                 and v["reporte_igual_con_las_rutas_normalizadas"] and v["kg_sha256"][0] == v["kg_sha256"][1]
                 and all(v["doble_corrida_interna"]) for v in res["doble_corrida"].values())
             and all(c["igual"] and c["doble_corrida_interna"] for c in res["cadenas"]))
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
with TSV.open("w", encoding="utf-8") as f:
    f.write("corrida\tgrafo\tkg_sha256\tesperado\n")
    for g, v in res["doble_corrida"].items():
        for i, corrida in enumerate(("run1", "run2")):
            f.write(f"{corrida}\t{g}\t{v['kg_sha256'][i]}\t-\n")
    for c in res["cadenas"]:
        f.write(f"{c['corrida']}\t{c['grafo']}\t{c['kg_sha256']}\t{c['esperado']}\n")
for g, v in res["doble_corrida"].items():
    print(g, v["archivos"], "distintos:", v["distintos"], "| reporte normalizado igual:", v["reporte_igual_con_las_rutas_normalizadas"],
          "| kg:", v["kg_sha256"][0], "| nodos/aristas:", v["nodos"], v["aristas"], "| interna:", v["doble_corrida_interna"])
print("reproducibilidad:", [(c["grafo"], c["kg_sha256"][:8], c["igual"]) for c in res["cadenas"]])
print("OK" if res["ok"] else "CON FALLAS")
