"""B6.1, tanda 1, T3, punto 5: corrida en seco (sin Neo4j) de las dos entradas nuevas de grafos.py y del registro de la vista, por el
mismo camino de imports que la carga (patrón de resellado_t0/scripts/dry_registro_rs1.py): importa el cargador
(data/experiment/tanda0/code/cargar_neo4j_tanda0.py) desde <raiz> como lo hace cargar_neo4j_t3f.py, reemplaza en memoria
CLAVES_TANDA0 por las dos claves de la tanda 1, y llama a lo que cargar_y_verificar hace antes de tocar Neo4j: grafos.verificar_sha y
cargar_kg.cargar_kg (la vista runtime, que importa tanda1/t3/registro_vista_r2b_tanda1). Compara los conteos con n_nodos y n_aristas;
comprueba que las entradas selladas de grafos.py no cambiaron (texto canónico de cada una) y que hay exactamente dos más; recomputa el
desglose declarado de «punto sin nodos». Solo lee.
Uso: python -I -B dry_registro_t3f.py <raiz> <grafos.py original> --out X.json
"""
import argparse
import importlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ap = argparse.ArgumentParser()
ap.add_argument("raiz")
ap.add_argument("grafos_original")
ap.add_argument("--out", required=True)
a = ap.parse_args()
RAIZ = Path(a.raiz).resolve()
NUEVAS = ["KG_Tanda1_Veinte_r2b", "KG_Tanda1_Veinte_r2b_sincola"]
spec = importlib.util.spec_from_file_location("cargar_neo4j_tanda0", RAIZ / "data/experiment/tanda0/code/cargar_neo4j_tanda0.py")
CN = importlib.util.module_from_spec(spec)
sys.modules["cargar_neo4j_tanda0"] = CN
spec.loader.exec_module(CN)
G, CK = CN.G, CN.CK
assert Path(G.__file__).resolve().is_relative_to(RAIZ) and Path(CK.__file__).resolve().is_relative_to(RAIZ)
res = {"claves_tanda0_del_cargador_al_importar": CN.CLAVES_TANDA0, "n_claves": len(G.CLAVES), "grafos": {}}
CN.CLAVES_TANDA0 = list(NUEVAS)
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
res["grafos_py_solo_dos_nuevas"] = set(G.CLAVES) - set(GO.CLAVES) == set(NUEVAS) and G.CLAVES[:len(GO.CLAVES)] == GO.CLAVES
R = importlib.import_module("registro_vista_r2b_tanda1")
assert Path(R.__file__).resolve().is_relative_to(RAIZ)
res["desglose"] = R.verificar_desglose()
res["ok"] = (all(v["sha256_ok"] and v["conteos_iguales"] for v in res["grafos"].values())
             and all(res["grafos_py_selladas_iguales"].values()) and res["grafos_py_solo_dos_nuevas"]
             and all(v["igual_a_lo_declarado"] for v in res["desglose"].values()))
Path(a.out).write_text(json.dumps(res, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k not in ("desglose", "grafos_py_selladas_iguales")}, ensure_ascii=False,
                 indent=1, default=str)[:4000])
print("selladas iguales: grafos.py", all(res["grafos_py_selladas_iguales"].values()), f"({len(res['grafos_py_selladas_iguales'])})")
print("desglose igual a lo declarado:", {k: v["igual_a_lo_declarado"] for k, v in res["desglose"].items()})
print("DRY T3:", "OK" if res["ok"] else "CON FALLAS")
