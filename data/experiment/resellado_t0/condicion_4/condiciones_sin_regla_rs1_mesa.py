"""Mesa, §120: «condiciones sin regla» (definición del 07/10/2026, A de reports/u_diag_cap3_grafo/scripts/udiag_e_aisladas.py) sobre los
cuatro grafos re-sellados. Importa `medir` de ese script sin editarlo. Corre desde la raíz de una copia del repo.
Uso: python -I -B <este> --raiz <copia> --kg nombre=ruta=sha256 [...] --out <json>"""
import argparse, hashlib, json, sys
ap = argparse.ArgumentParser(); ap.add_argument("--raiz", required=True); ap.add_argument("--kg", action="append", required=True)
ap.add_argument("--out", required=True); A = ap.parse_args()
# El módulo importa udiag_comun, que lee una copia de código que no está en el repo. Para usar la regla sin editarla, se toman del
# árbol sintáctico del script solo NO_CONTENIDO, es_remision_r1 y medir, y se ejecutan con collections.
import ast, collections, types  # noqa: E402
_src = open(f"{A.raiz}/reports/u_diag_cap3_grafo/scripts/udiag_e_aisladas.py", encoding="utf-8").read()
_arbol = ast.parse(_src)
_nodos = [n for n in _arbol.body if (isinstance(n, ast.FunctionDef) and n.name in ("es_remision_r1", "medir")) or
          (isinstance(n, ast.Assign) and any(getattr(x, "id", "") == "NO_CONTENIDO" for x in n.targets))]
assert len(_nodos) == 3, "no encuentro las tres definiciones"
U = types.SimpleNamespace(); _ns = {"collections": collections}
exec(compile(ast.Module(body=_nodos, type_ignores=[]), "udiag_e_aisladas.py", "exec"), _ns)
U.medir = _ns["medir"]
out = {"regla": "reports/u_diag_cap3_grafo/scripts/udiag_e_aisladas.py, medir (A: sin regla; vigente: sin ninguna arista)", "grafos": []}
for x in A.kg:
    nombre, ruta, esp = x.split("=")
    b = open(ruta, "rb").read()
    if hashlib.sha256(b).hexdigest() != esp: sys.exit(f"FRENO: {nombre} no da su sha256")
    m = U.medir(json.loads(b))
    out["grafos"].append({"grafo": nombre, "sha256": esp, **m})
    print(f"{nombre}: Condicion {m['condicion']} | sin ninguna arista {m['vigente_condicion_sin_ninguna_arista']} | aislados {m['vigente_aislados_de_todo_tipo']} | sin regla {m['A_condicion_sin_arista_de_contenido']}")
json.dump(out, open(A.out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
