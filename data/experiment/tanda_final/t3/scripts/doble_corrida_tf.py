"""B6.1, tanda final, T3, punto 3: la doble corrida de los ocho ensamblados, la reproducibilidad de los sellados, la prueba de la raya
en el tramo 1 y la comparación del acumulado de 60 con la prueba de la mesa. Es `data/experiment/tanda1/t3/scripts/doble_corrida_t3.py`
con ocho grafos y tres comparaciones más. Solo lee.
  - Doble corrida: para cada grafo, compara archivo por archivo la primera corrida (en la copia, en su carpeta final) con la segunda
    (otro proceso, fuera de la copia): byte a byte, salvo reporte_ensamblado_r2.json, que guarda en `redirecciones` la ruta de su
    --salida y las rutas absolutas de la raíz donde corrió; ese archivo se compara con esas rutas normalizadas y se declara. El
    `kg.json.gz` y su sello no entran en la comparación: los agrega después comprimir_kg_tf.py en la primera corrida.
  - Reproducibilidad (laudo de la release r2, §3, punto 4): las seis cadenas de la tanda 0 dan sus sha256 sellados
    (resellado_t0/FRENO_resellado_T0.md:68-71 y las dos r2a por su prefijo) y las cuatro de la tanda 1, los de
    tanda1/t3/FRENO_T3.md:32-35.
  - El tramo 1 va con la variante con la raya (decisión de la autora sobre el FRENO T3 parcial: la regla de la §19 con la enmienda 9,
    punto 8; manifiestos de t3/prueba_raya_tramo1/manifiestos/): su primera corrida, en la carpeta final; la segunda, la de la prueba de
    la raya (otro proceso, <corridas>/raya/). La variante con los manifiestos de T1, sin la raya (la del FRENO parcial,
    <corridas>/manifiestos_T1/run1 y run2), se compara archivo por archivo con la que rige, y su propia doble corrida, aparte.
  - El acumulado de 60 contra la prueba de la mesa (registro de decisiones, §43: 23.671 nodos y 67.006 aristas; sin cola, 22.930 y
    59.354), que usó los `nombres_remision` de cada manifiesto de origen (el del acumulado de la tanda 1 y el del tramo 1 de T1); aquí
    van los del manifiesto derivado en T3 (regla v2 sin la raya). Se listan los TOs cuyos `nombres_remision` difieren entre los dos.
Uso: python3 -I -B doble_corrida_tf.py <copia> <dir de corridas> <salida.json> <salida.tsv>
"""
import hashlib
import json
import sys
from pathlib import Path

C, K, OUT, TSV = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
X = "data/experiment/reextraccion_v2/corpus_tanda_final"
A = "data/experiment/tanda_final/t3/acumulado"
CARP = {"acum128": f"{A}/ens_128_r2b", "acum128_sincola": f"{A}/ens_128_r2b_sincola",
        "tf98": f"{X}/ens_98_r2b", "tf98_sincola": f"{X}/ens_98_r2b_sincola",
        "acum60": f"{A}/ens_60_tramo1_r2b", "acum60_sincola": f"{A}/ens_60_tramo1_r2b_sincola",
        "tf_tramo1": f"{X}/ens_tramo1_r2b", "tf_tramo1_sincola": f"{X}/ens_tramo1_r2b_sincola"}
ESPERADO = {"r2a_diez": "70d51e42", "r2a_desarrollo": "fa4c1043",
            "r2b_diez": "fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea",
            "r2b_desarrollo": "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31",
            "r2b_sincola_diez": "61dd1b69ba03e40499845c40a6a8bec4c22d892ebe95823c7d5a569110f08738",
            "r2b_sincola_desarrollo": "66e745f57397ab754cde09eb641e9f0d9ef6259ea7e6445d086ecbf1c36dcc6c",
            "t1_veinte": "22e83a62cb88e5bbe31b64a0f2322194bc2ffd2622ea7adc2c07310d8a02c7c7",
            "t1_veinte_sincola": "384a6d5bc139cd7b74d86840c68e7034b7a9bcb4bc26da7c61567f3f053e624e",
            "acum_treinta": "e63536d15bd8f575f1b7680921e3ca0d4956bdc5e38dc3f2fea27bb67bd71769",
            "acum_treinta_sincola": "0435d41f9c7b45ea10cc87e8121fcfb8b3d2b089af837fff377a3460ced9636c"}
RUN2 = {"tf_tramo1": "raya/tf_tramo1_raya", "tf_tramo1_sincola": "raya/tf_tramo1_raya_sincola"}   # las demás, run2/<grafo>
VARIANTE_T1 = {"tf_tramo1_raya": "tf_tramo1", "tf_tramo1_raya_sincola": "tf_tramo1_sincola"}
MESA = {"acum60": (23671, 67006), "acum60_sincola": (22930, 59354)}
MAN60 = f"{A}/manifiestos/tanda_final_acumulado_ens_60_tramo1_r2b.json"
ORIGEN60 = ("data/experiment/tanda1/t3/acumulado/manifiestos/acumulado_ens_treinta_r2b.json",
            "data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_tramo1_r2b.json")


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


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


DESPUES = ("kg.json.gz", "kg.json.gz.sello.json")     # los agrega comprimir_kg_tf.py, después de la doble corrida


def comparar(a: Path, b: Path) -> dict:
    fa = sorted(p.relative_to(a).as_posix() for p in a.rglob("*") if p.is_file() and p.name not in DESPUES)
    fb = sorted(p.relative_to(b).as_posix() for p in b.rglob("*") if p.is_file() and p.name not in DESPUES)
    distintos = [f for f in sorted(set(fa) & set(fb)) if sha(a / f) != sha(b / f)]
    return {"archivos": [len(fa), len(fb)], "mismos_nombres": fa == fb, "distintos": distintos,
            "kg_sha256": [sha(a / "kg.json"), sha(b / "kg.json")], "doble_corrida_interna": [interna(a), interna(b)]}


res = {"doble_corrida": {}, "cadenas": [], "raya_tramo1": {}, "acumulado_60_contra_la_mesa": {}}
for g, carp in CARP.items():
    a, b = C / carp / "r2", K / RUN2.get(g, f"run2/{g}") / "r2"
    v = comparar(a, b)
    v["reporte_igual_con_las_rutas_normalizadas"] = (norm_reporte(a / "reporte_ensamblado_r2.json", str(C))
                                                     == norm_reporte(b / "reporte_ensamblado_r2.json", str(C)))
    kg = json.loads((a / "kg.json").read_text(encoding="utf-8"))
    v.update({"carpeta": carp, "nodos": len(kg["nodes"]), "aristas": len(kg["edges"]), "kg_bytes": (a / "kg.json").stat().st_size})
    res["doble_corrida"][g] = v
for g, esp in ESPERADO.items():
    d = K / "repro" / g / "r2"
    s = sha(d / "kg.json")
    res["cadenas"].append({"corrida": "repro", "grafo": g, "kg_sha256": s, "esperado": esp,
                           "igual": s == esp if len(esp) == 64 else s.startswith(esp), "doble_corrida_interna": interna(d)})
MAN_RAYA = {"tf_tramo1_raya": ("data/experiment/tanda_final/t3/prueba_raya_tramo1/manifiestos/tanda_final_ens_tramo1_r2b_raya.json",
                               "data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_tramo1_r2b.json"),
            "tf_tramo1_raya_sincola": ("data/experiment/tanda_final/t3/prueba_raya_tramo1/manifiestos/tanda_final_ens_tramo1_r2b_raya_sincola.json",
                                       "data/experiment/tanda_final/t1/ensamblado/manifiestos/tanda_final_ens_tramo1_r2b_sincola.json")}
for g, ref in VARIANTE_T1.items():
    # la que rige (la raya, en la carpeta final) contra la variante con los manifiestos de T1 (su primera corrida)
    v = comparar(C / CARP[ref] / "r2", K / "manifiestos_T1/run1" / ref / "r2")
    v["contra"] = f"{ref} con los manifiestos de T1"
    v["kg_igual"] = v["kg_sha256"][0] == v["kg_sha256"][1]
    d1 = comparar(K / "manifiestos_T1/run1" / ref / "r2", K / "manifiestos_T1/run2" / ref / "r2")
    v["variante_T1_doble_corrida"] = {"kg_sha256": d1["kg_sha256"], "distintos": d1["distintos"], "mismos_nombres": d1["mismos_nombres"]}
    mr, mt = ({t["id"]: t.get("nombres_remision") for t in json.loads((C / p).read_text(encoding="utf-8"))["tos"]} for p in MAN_RAYA[g])
    v["manifiestos"] = list(MAN_RAYA[g])
    v["tos_con_nombres_distintos_entre_los_manifiestos"] = sorted(t for t in mr if mr[t] != mt.get(t))
    res["raya_tramo1"][g] = v
m60 = {t["id"]: t.get("nombres_remision") for t in json.loads((C / MAN60).read_text(encoding="utf-8"))["tos"]}
origen = {}
for p in ORIGEN60:
    for t in json.loads((C / p).read_text(encoding="utf-8"))["tos"]:
        origen[t["id"]] = t.get("nombres_remision")
nombres_distintos = sorted(t for t in m60 if m60[t] != origen.get(t))
for g, (n, e) in MESA.items():
    v = res["doble_corrida"][g]
    res["acumulado_60_contra_la_mesa"][g] = {"nodos": [v["nodos"], n], "aristas": [v["aristas"], e],
                                            "igual": (v["nodos"], v["aristas"]) == (n, e)}
res["acumulado_60_contra_la_mesa"]["nombres_remision"] = {
    "manifiesto_t3": MAN60, "manifiestos_de_la_mesa": list(ORIGEN60), "tos": len(m60),
    "tos_en_los_de_la_mesa": sum(1 for t in m60 if t in origen), "tos_con_nombres_distintos": nombres_distintos}
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
    for g, v in res["raya_tramo1"].items():
        f.write(f"raya\t{g}\t{v['kg_sha256'][0]}\t{v['kg_sha256'][1]}\n")
for g, v in res["doble_corrida"].items():
    print(g, v["archivos"], "distintos:", v["distintos"], "| reporte normalizado igual:", v["reporte_igual_con_las_rutas_normalizadas"],
          "| kg:", v["kg_sha256"][0], "| nodos/aristas:", v["nodos"], v["aristas"], "| interna:", v["doble_corrida_interna"])
print("reproducibilidad:", [(c["grafo"], c["kg_sha256"][:8], c["igual"]) for c in res["cadenas"]])
print("raya:", {g: (v["kg_igual"], v["distintos"]) for g, v in res["raya_tramo1"].items()})
print("acumulado 60 contra la mesa:", json.dumps(res["acumulado_60_contra_la_mesa"], ensure_ascii=False))
print("OK" if res["ok"] else "CON FALLAS")
