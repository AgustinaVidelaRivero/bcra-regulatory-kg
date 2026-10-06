"""U-SINCOLA-T0, SC2: corrida en seco (sin Neo4j) de las dos entradas nuevas de grafos.py y del registro de la vista, por
el mismo camino de imports que el cargador: importa grafos desde <raiz>/data/experiment/neo4j, verifica el sha de cada
clave nueva, carga la vista runtime (grafos.cargar_vista_runtime → importa sincola_t0/registro_vista_r2b_sincola →
comun_ev2.cargar_runtime) y compara los conteos con n_nodos y n_aristas; comprueba que las entradas selladas no
cambiaron (texto canónico de cada una) y que la fixture tiene exactamente dos entradas más, con las selladas iguales
(texto canónico). Recomputa además el desglose declarado de «punto sin nodos». Uso: python -B dry_registro_sc2.py <raiz> <fixture original (git show)> <grafos.py original> --out X.json
"""
import argparse
import hashlib
import importlib
import json
import sys
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("raiz")
ap.add_argument("fixture_original")
ap.add_argument("grafos_original")
ap.add_argument("--out", required=True)
a = ap.parse_args()
RAIZ = Path(a.raiz).resolve()
sys.path.insert(0, str(RAIZ / "data/experiment/neo4j"))
import grafos as G  # noqa: E402

res = {"raiz": str(RAIZ), "grafos": {}}
NUEVAS = ["KG_Tanda0_Desarrollo_r2b_sincola", "KG_Tanda0_Diez_r2b_sincola"]
res["claves"] = G.CLAVES
res["claves_nuevas_presentes"] = all(k in G.GRAFOS for k in NUEVAS)
res["n_claves"] = len(G.CLAVES)
for k in NUEVAS:
    g = G.GRAFOS[k]
    sha = G.verificar_sha(k)
    kg = G.cargar_vista_runtime(k)
    res["grafos"][k] = {"label": g["label"], "sha256_ok": sha == g["sha256"], "commit_sellado": g["commit_sellado"],
                        "n_nodos_registro": g["n_nodos"], "n_aristas_registro": g["n_aristas"],
                        "vista_nodos": len(kg.nodes), "vista_aristas": len(kg.edges),
                        "conteos_iguales": len(kg.nodes) == g["n_nodos"] and len(kg.edges) == g["n_aristas"],
                        "requiere_registro_modulo": g["requiere_registro_modulo"], "indice_fulltext": g["indice_fulltext"],
                        "ev2_key": g["ev2_key"]}
# entradas selladas de grafos.py: texto canónico igual al original (módulo original importado desde un archivo temporal)
import importlib.util  # noqa: E402
spec = importlib.util.spec_from_file_location("grafos_original_mod", a.grafos_original)
GO = importlib.util.module_from_spec(spec)
sys.path.insert(0, str(Path(a.grafos_original).resolve().parent))
spec.loader.exec_module(GO)


def canon(d):
    return json.dumps(d, ensure_ascii=False, sort_keys=True, default=str)


# las Path de cada módulo llevan su propia raíz (EXPERIMENT_DIR sale de __file__): se comparan relativizadas
res["grafos_py_selladas_iguales"] = {k: canon(G.GRAFOS[k]).replace(str(G.EXPERIMENT_DIR), "<EXP>") == canon(GO.GRAFOS[k]).replace(str(GO.EXPERIMENT_DIR), "<EXP>") for k in GO.CLAVES}
res["grafos_py_solo_dos_nuevas"] = set(G.CLAVES) - set(GO.CLAVES) == set(NUEVAS) and set(GO.CLAVES) <= set(G.CLAVES)
# fixture
fx = json.loads((RAIZ / "scripts/regression_kg_esperado.json").read_text(encoding="utf-8"))
fo = json.loads(Path(a.fixture_original).read_text(encoding="utf-8"))
ee, eo = fx["estado_esperado"], fo["estado_esperado"]
res["fixture_entradas"] = list(ee.keys())
res["fixture_solo_dos_nuevas"] = set(ee) - set(eo) == {"KG-Tanda0-Diez-r2b-sincola", "KG-Tanda0-Desarrollo-r2b-sincola"} and set(eo) <= set(ee)
res["fixture_selladas_iguales"] = {k: canon(ee[k]) == canon(eo[k]) for k in eo}
res["fixture_resto_igual"] = {k: canon(fx[k]) == canon(fo[k]) for k in fo if k != "estado_esperado"}
for k, G_ in (("KG-Tanda0-Diez-r2b-sincola", "Diez"), ("KG-Tanda0-Desarrollo-r2b-sincola", "Desarrollo")):
    e, b = ee[k], ee[f"KG-Tanda0-{G_}-r2b"]
    kgp = RAIZ / e["kg"]
    res[f"fixture_{k}"] = {"kg_sha256_igual_archivo": hashlib.sha256(kgp.read_bytes()).hexdigest() == e["kg_sha256"],
                           "items_iguales_a_r2b": canon(e["items"]) == canon(b["items"]),
                           "ranks_sellados_iguales": canon(e.get("ranks_sellados")) == canon(b.get("ranks_sellados")),
                           "parametros_iguales": all(e.get(x) == b.get(x) for x in ("generacion", "politica_cuarentena", "catalogo", "catalogo_sha256", "perfil")),
                           "registro_dir": e.get("registro_dir"), "registro_dir_existe": (RAIZ / e.get("registro_dir", "")).is_dir()}
# desglose
sys.path.insert(0, str(RAIZ / "data/experiment/sincola_t0"))
R = importlib.import_module("registro_vista_r2b_sincola")
res["desglose"] = R.verificar_desglose()
res["ok"] = (res["claves_nuevas_presentes"] and all(v["sha256_ok"] and v["conteos_iguales"] for v in res["grafos"].values())
             and all(res["grafos_py_selladas_iguales"].values()) and res["grafos_py_solo_dos_nuevas"]
             and res["fixture_solo_dos_nuevas"] and all(res["fixture_selladas_iguales"].values()) and all(res["fixture_resto_igual"].values())
             and all(all(v for kk, v in res[f"fixture_{k}"].items() if isinstance(v, bool)) for k in ("KG-Tanda0-Diez-r2b-sincola", "KG-Tanda0-Desarrollo-r2b-sincola"))
             and all(v["igual_a_lo_declarado"] for v in res["desglose"].values()))
Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k not in ("desglose", "claves", "fixture_entradas")}, ensure_ascii=False, indent=1, default=str)[:3000])
print("desglose igual a lo declarado:", {k: v["igual_a_lo_declarado"] for k, v in res["desglose"].items()})
print("DRY SC2:", "OK" if res["ok"] else "CON FALLAS")
