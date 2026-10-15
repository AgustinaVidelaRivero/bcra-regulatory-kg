"""Mesa, §102: los documentos que tienen una constante por documento en el código de E0 (los tres archivos del manifiesto de S0-6b).
Recorre el árbol sintáctico de cada archivo (sin los docstrings) y junta las constantes de texto que son un id de documento de los 152, o
que empiezan con «<id>::» (un id de unidad). Comentarios y docstrings no cuentan. Imprime solo ids de documentos y cuentas.
Uso: python3 -I -B <este> <carpeta e0_chunking> <inventario_tos.csv> <json de salida nuevo>"""
import ast, csv, json, sys
from collections import defaultdict
from pathlib import Path
D, INV, OUT = Path(sys.argv[1]), sys.argv[2], Path(sys.argv[3])
if OUT.exists(): sys.exit("FRENO: la salida ya existe")
tos = {r["id"] for r in csv.DictReader(open(INV, encoding="utf-8"))}
hall = defaultdict(lambda: defaultdict(int))
for f in ("e0_lib.py", "correr_e0.py", "e0_tablas.py"):
    arbol = ast.parse((D / f).read_text(encoding="utf-8"))
    docs = set()
    for n in ast.walk(arbol):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.body and isinstance(n.body[0], ast.Expr) \
           and isinstance(getattr(n.body[0], "value", None), ast.Constant) and isinstance(n.body[0].value.value, str):
            docs.add(id(n.body[0].value))
    for n in ast.walk(arbol):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs:
            v = n.value
            t = v if v in tos else (v.split("::", 1)[0] if "::" in v and v.split("::", 1)[0] in tos else None)
            if t: hall[t][f] += 1
res = {t: dict(v) for t, v in sorted(hall.items())}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(len(res), "documentos con constantes por documento:", sorted(res))
