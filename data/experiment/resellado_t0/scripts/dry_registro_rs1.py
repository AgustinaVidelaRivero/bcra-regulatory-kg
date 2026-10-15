"""Re-sellado único de la tanda 0, §3.3: corrida en seco (sin Neo4j) de las cuatro entradas nuevas de grafos.py y del
registro de la vista, por el mismo camino de imports que la carga: importa el cargador
(data/experiment/tanda0/code/cargar_neo4j_tanda0.py, que importa comun_tanda0, grafos, cargar_kg, indices y
test_equivalencia) desde <raiz>, y llama a lo que cargar_y_verificar hace antes de tocar Neo4j: grafos.verificar_sha y
cargar_kg.cargar_kg (la vista runtime, que importa resellado_t0/registro_vista_r2b_rs1). Compara los conteos con n_nodos y
n_aristas; comprueba que las entradas selladas de grafos.py y de la fixture no cambiaron (texto canónico de cada una),
que hay exactamente cuatro entradas más en cada uno, y recomputa el desglose declarado de «punto sin nodos».
Patrón: sincola_t0/sc2/dry_registro_sc2.py. Solo lee.
Uso: python -I -B dry_registro_rs1.py <raiz> <fixture original> <grafos.py original> --out X.json
"""
import argparse
import hashlib
import importlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ap = argparse.ArgumentParser()
ap.add_argument("raiz")
ap.add_argument("fixture_original")
ap.add_argument("grafos_original")
ap.add_argument("--out", required=True)
a = ap.parse_args()
RAIZ = Path(a.raiz).resolve()
spec = importlib.util.spec_from_file_location("cargar_neo4j_tanda0", RAIZ / "data/experiment/tanda0/code/cargar_neo4j_tanda0.py")
CN = importlib.util.module_from_spec(spec)
spec.loader.exec_module(CN)
G, CK = CN.G, CN.CK
assert Path(G.__file__).resolve().is_relative_to(RAIZ) and Path(CK.__file__).resolve().is_relative_to(RAIZ)

NUEVAS = ["KG_Tanda0_Desarrollo_r2b_rs1", "KG_Tanda0_Diez_r2b_rs1", "KG_Tanda0_Desarrollo_r2b_sincola_rs1",
          "KG_Tanda0_Diez_r2b_sincola_rs1"]
SUITE = {"KG_Tanda0_Desarrollo_r2b_rs1": ("KG-Tanda0-Desarrollo-r2b-rs1", "KG-Tanda0-Desarrollo-r2b"),
         "KG_Tanda0_Diez_r2b_rs1": ("KG-Tanda0-Diez-r2b-rs1", "KG-Tanda0-Diez-r2b"),
         "KG_Tanda0_Desarrollo_r2b_sincola_rs1": ("KG-Tanda0-Desarrollo-r2b-sincola-rs1", "KG-Tanda0-Desarrollo-r2b-sincola"),
         "KG_Tanda0_Diez_r2b_sincola_rs1": ("KG-Tanda0-Diez-r2b-sincola-rs1", "KG-Tanda0-Diez-r2b-sincola")}
res = {"claves_tanda0_del_cargador": CN.CLAVES_TANDA0, "n_claves": len(G.CLAVES), "grafos": {}}
res["claves_nuevas_en_el_cargador"] = all(k in CN.CLAVES_TANDA0 for k in NUEVAS)
for k in NUEVAS:
    g = G.GRAFOS[k]
    sha = G.verificar_sha(k)
    kg = CK.cargar_kg(k)
    res["grafos"][k] = {"label": g["label"], "nombre_canonico": g["nombre_canonico"], "sha256_ok": sha == g["sha256"],
                        "commit_sellado": g["commit_sellado"], "n_nodos_registro": g["n_nodos"],
                        "n_aristas_registro": g["n_aristas"], "vista_nodos": len(kg.nodes), "vista_aristas": len(kg.edges),
                        "merges": len(kg.merges), "conteos_iguales": len(kg.nodes) == g["n_nodos"] and len(kg.edges) == g["n_aristas"],
                        "requiere_registro_modulo": g["requiere_registro_modulo"], "indice_fulltext": g["indice_fulltext"],
                        "ev2_key": g["ev2_key"], "kg_path": G.rel_repo(g["path"])}
spec = importlib.util.spec_from_file_location("grafos_original_mod", a.grafos_original)
GO = importlib.util.module_from_spec(spec)
spec.loader.exec_module(GO)


def canon(d):
    return json.dumps(d, ensure_ascii=False, sort_keys=True, default=str)


# las Path de cada módulo llevan su propia raíz (EXPERIMENT_DIR sale de __file__): se comparan relativizadas
res["grafos_py_selladas_iguales"] = {k: canon(G.GRAFOS[k]).replace(str(G.EXPERIMENT_DIR), "<EXP>")
                                     == canon(GO.GRAFOS[k]).replace(str(GO.EXPERIMENT_DIR), "<EXP>") for k in GO.CLAVES}
res["grafos_py_solo_cuatro_nuevas"] = set(G.CLAVES) - set(GO.CLAVES) == set(NUEVAS) and G.CLAVES[:len(GO.CLAVES)] == GO.CLAVES
fx = json.loads((RAIZ / "scripts/regression_kg_esperado.json").read_text(encoding="utf-8"))
fo = json.loads(Path(a.fixture_original).read_text(encoding="utf-8"))
ee, eo = fx["estado_esperado"], fo["estado_esperado"]
res["fixture_solo_cuatro_nuevas"] = (set(ee) - set(eo) == {v[0] for v in SUITE.values()}
                                     and list(ee)[:len(eo)] == list(eo))
res["fixture_selladas_iguales"] = {k: canon(ee[k]) == canon(eo[k]) for k in eo}
res["fixture_resto_igual"] = {k: canon(fx[k]) == canon(fo[k]) for k in fo if k != "estado_esperado"}
for k, (nuevo, base) in SUITE.items():
    e, b = ee[nuevo], ee[base]
    res[f"fixture_{nuevo}"] = {
        "kg_sha256_igual_archivo": hashlib.sha256((RAIZ / e["kg"]).read_bytes()).hexdigest() == e["kg_sha256"],
        "kg_sha256_igual_grafos_py": e["kg_sha256"] == G.GRAFOS[k]["sha256"],
        "items_iguales_a_la_sellada": canon(e["items"]) == canon(b["items"]),
        "ranks_sellados_iguales": canon(e.get("ranks_sellados")) == canon(b.get("ranks_sellados")),
        "parametros_iguales": all(e.get(x) == b.get(x) for x in ("generacion", "politica_cuarentena", "catalogo",
                                                                 "catalogo_sha256", "perfil")),
        "registro_dir": e.get("registro_dir"), "registro_dir_existe": (RAIZ / e.get("registro_dir", "")).is_dir()}
R = importlib.import_module("registro_vista_r2b_rs1")
assert Path(R.__file__).resolve().is_relative_to(RAIZ)
res["desglose"] = R.verificar_desglose()
res["ok"] = (res["claves_nuevas_en_el_cargador"] and all(v["sha256_ok"] and v["conteos_iguales"] for v in res["grafos"].values())
             and all(res["grafos_py_selladas_iguales"].values()) and res["grafos_py_solo_cuatro_nuevas"]
             and res["fixture_solo_cuatro_nuevas"] and all(res["fixture_selladas_iguales"].values())
             and all(res["fixture_resto_igual"].values())
             and all(all(v for v in res[f"fixture_{n}"].values() if isinstance(v, bool)) for n, _ in SUITE.values())
             and all(v["igual_a_lo_declarado"] for v in res["desglose"].values()))
Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k not in ("desglose", "claves_tanda0_del_cargador",
                                                            "grafos_py_selladas_iguales", "fixture_selladas_iguales")},
                 ensure_ascii=False, indent=1, default=str)[:4000])
print("selladas iguales: grafos.py", all(res["grafos_py_selladas_iguales"].values()), "| fixture",
      all(res["fixture_selladas_iguales"].values()))
print("desglose igual a lo declarado:", {k: v["igual_a_lo_declarado"] for k, v in res["desglose"].items()})
print("DRY RS1:", "OK" if res["ok"] else "CON FALLAS")
