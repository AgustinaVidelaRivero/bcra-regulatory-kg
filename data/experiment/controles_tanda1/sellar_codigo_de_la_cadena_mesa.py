"""Mesa, 16/10/2026: sella la lista del código de la cadena de la tanda 1 (E0, E1 a E3, el runner, el ensamblado, los validadores, los
perfiles, shapes y la suite), con el sha256 de cada ruta en el commit del gate final del laudo (47c9f1b3), calculado con git show, y la
compara con HEAD. Todo se lee con git show y git ls-tree: el script no lee el árbol de trabajo ni escribe en el repo.
Cómo arma la lista:
  1. los puntos de entrada de la cadena (ENTRADAS);
  2. la clausura de sus imports locales, por AST: un módulo se resuelve contra los .py rastreados en el commit, primero en la carpeta del
     que importa, después en las carpetas de la cadena y por último contra el único .py del repo con ese nombre (salvo los de la
     biblioteca estándar); si queda más de un candidato en las carpetas de la cadena, el script frena;
  3. los archivos de datos (json, jsonl, csv, txt, yaml) rastreados en las carpetas de la cadena que ese código nombra en sus cadenas (por
     AST, sin docstrings ni comentarios), por su nombre de archivo; nunca salidas;
  4. fuera de esas carpetas, solo las lecturas revisadas a mano, cada una con el renglón que la hace (FUERA); un .py de esa lista entra a
     la clausura de imports;
  5. los que sella el §1 del laudo firmado y no salen de los pasos anteriores (EXTRA).
El grupo de cada ruta sale de su carpeta (GRUPO), no del archivo que la trae.
Uso: python3 -I -B <este> <raíz del repo> <commit> <salida.json>"""
import ast, hashlib, json, re, subprocess, sys
from pathlib import PurePosixPath as PP
R, COMMIT, OUT = sys.argv[1], sys.argv[2], sys.argv[3]
def git(*a): return subprocess.run(["git", "--no-optional-locks", "-C", R, *a], capture_output=True, check=True).stdout
ENTRADAS = {
    "data/experiment/reextraccion_v2/e0_chunking/correr_e0.py": "E0",
    "data/experiment/reextraccion_v2/e0_chunking/healthcheck_e0.py": "E0",
    "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py": "runner (E1 a E3)",
    "data/experiment/tanda0/code/ensamblar_tanda0.py": "ensamblado",
    "scripts/shapes_validator.py": "shapes",
    "scripts/regression_kg.py": "suite",
    "scripts/metricas_intrinsecas.py": "métricas del gate",
}
CARPETAS = ["data/experiment/reextraccion_v2/e0_chunking", "data/experiment/reextraccion_v2/e1_extractor",
            "data/experiment/reextraccion_v2/corpus_v2", "data/experiment/reextraccion_v2/e3_verificador", "data/experiment/pyd_r2/code",
            "data/experiment/pyd_r2/generados", "data/experiment/pyd_r2", "data/experiment/tanda0/code", "data/experiment/catalogo_unico",
            "scripts"]
def GRUPO(f):
    reglas = [("reextraccion_v2/e0_chunking/", "E0"), ("reextraccion_v2/e2_reduce/", "E2"), ("reextraccion_v2/manifiesto_corpus.py", "E0"),
              ("reextraccion_v2/manifiestos/", "runner"), ("b54_catalogo_v3/", "perfiles"), ("esq/code/", "shapes"),
              ("data/experiment/evaluacion/", "cuarteto de evaluación (lo importan E1 y la suite)"), ("grafo_v2/code/", "métricas del gate"), ("e1_extractor/perfil_e1.py", "perfiles"), ("e1_extractor/validador_e1.py", "validadores"),
              ("reextraccion_v2/e1_extractor/", "E1"), ("reextraccion_v2/e3_verificador/", "E3"), ("data/experiment/pyd_r2/", "validadores"),
              ("corpus_v2/runner_corpus.py", "runner"), ("corpus_v2/r1_e4.py", "runner"), ("reextraccion_v2/corpus_v2/", "ensamblado"),
              ("tanda0/code/", "ensamblado"), ("catalogo_unico/", "catálogo del request y alcance"), ("scripts/shapes_validator.py", "shapes"),
              ("scripts/remisiones.py", "shapes"), ("scripts/regression_kg", "suite"), ("scripts/metricas_intrinsecas.py", "métricas del gate")]
    for pref, g in reglas:
        if pref in f: return g
    return "datos que lee la cadena fuera de sus carpetas"

EXTRA = {"scripts/regression_kg_esperado.json": "suite (fixture; laudo §1)"}
FUERA = {
    "data/experiment/esq/code/prompt_congelado.py": "scripts/shapes_validator.py:164 (lo importa por ruta)",
    "data/experiment/escalado_prep/inventario_tos.csv": "data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:562",
    "data/experiment/escalado_prep/inventario_resumen.json": "data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:563",
    "data/experiment/esq_v3_miembros/esquema_v3_clases.json": "data/experiment/tanda0/code/ensamblar_tanda0.py:76",
    "data/experiment/grafo_v2/esquema_v2_clases.json": "data/experiment/reextraccion_v2/corpus_v2/r1_comun.py:32",
    "data/experiment/exploracion/mapa_territorio_quemado_5TOs_5sets.json": "data/experiment/reextraccion_v2/e0_chunking/correr_e0.py:55",
    "data/experiment/reextraccion_v2/manifiestos/desarrollo_5tos.json": "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py:106",
    "data/experiment/evaluacion/judge.py": "data/experiment/evaluacion/llm_cache.py:24 (la versión del código de la caché hashea harness, judge y loader)",
}
SALIDA = re.compile(r"(^|/)(salida[^/]*|resultados|freno[^/]*|selftest_salida[^/]*|reportes?|cache[^/]*|__pycache__)(/|$)", re.I)
todos = git("ls-tree", "-r", "--name-only", COMMIT).decode().splitlines()
STDLIB = set(sys.stdlib_module_names)
por_nombre, por_base = {}, {}
for f in todos:
    por_base.setdefault(PP(f).name, []).append(f)
    if f.endswith(".py"): por_nombre.setdefault(PP(f).stem, []).append(f)
en_carpetas = lambda f: any(str(PP(f).parent) == c or (c != "scripts" and f.startswith(c + "/")) for c in CARPETAS)
def resolver(mod, desde):
    base = mod.split(".")[0]
    cand = por_nombre.get(base, [])
    if not cand or base in STDLIB: return None
    mismo = [c for c in cand if str(PP(c).parent) == str(PP(desde).parent)]
    if len(mismo) == 1: return mismo[0]
    cad = [c for c in cand if str(PP(c).parent) in CARPETAS]
    if len(cad) == 1: return cad[0]
    if len(cad) > 1: raise SystemExit(f"FRENO: {mod} desde {desde} tiene varios candidatos: {cad}")
    return cand[0] if len(cand) == 1 else None
def cadenas(src):
    arbol = ast.parse(src); docs = set()
    for n in ast.walk(arbol):
        if isinstance(n, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and n.body and isinstance(n.body[0], ast.Expr) \
                and isinstance(getattr(n.body[0], "value", None), ast.Constant) and isinstance(n.body[0].value.value, str):
            docs.add(id(n.body[0].value))
    return [n.value for n in ast.walk(arbol) if isinstance(n, ast.Constant) and isinstance(n.value, str) and id(n) not in docs]
def datos_nombrados(src):
    out = set()
    for s in cadenas(src):
        for m in re.findall(r"([A-Za-z0-9_.\-]+\.(?:json|jsonl|txt|yaml|yml|csv))", s):
            out.update(t for t in por_base.get(m, []) if not SALIDA.search(t) and en_carpetas(t))
    return out
lista, cola = {}, list(ENTRADAS) + [f for f in FUERA if f.endswith(".py")]
for f in ENTRADAS: lista[f] = {"entra": "punto de entrada"}
for f, por in FUERA.items(): lista[f] = {"entra": f"lectura revisada: {por}"}
while cola:
    f = cola.pop(0)
    src = git("show", f"{COMMIT}:{f}").decode("utf-8")
    nuevos = []
    for n in ast.walk(ast.parse(src)):
        mods = [a.name for a in n.names] if isinstance(n, ast.Import) else ([n.module] if isinstance(n, ast.ImportFrom) and n.module and n.level == 0 else [])
        for m in mods:
            r = resolver(m, f)
            if r and r not in lista: lista[r] = {"entra": f"importado por {f}"}; nuevos.append(r)
    for d in sorted(datos_nombrados(src)):
        if d not in lista: lista[d] = {"entra": f"nombrado en el código de {f}"}
    cola.extend(nuevos)
for d, g in EXTRA.items():
    if d not in lista: lista[d] = {"entra": "sellado en el §1 del laudo"}
for f in lista: lista[f]["grupo"] = GRUPO(f)
h = lambda b: hashlib.sha256(b).hexdigest()
head = git("rev-parse", "HEAD").decode().strip()
filas = []
for f in sorted(lista):
    s = h(git("show", f"{COMMIT}:{f}"))
    try: sh = h(git("show", f"HEAD:{f}"))
    except subprocess.CalledProcessError: sh = None
    filas.append({"ruta": f, "sha256": s, "grupo": lista[f]["grupo"], "entra": lista[f]["entra"], "igual_en_HEAD": sh == s})
res = {"commit": git("rev-parse", COMMIT).decode().strip(), "metodo": "git show <commit>:<ruta> | sha256", "n": len(filas),
       "por_grupo": {g: sum(1 for x in filas if x["grupo"] == g) for g in sorted({x["grupo"] for x in filas})},
       "head_al_sellar": head, "todas_iguales_en_HEAD": all(x["igual_en_HEAD"] for x in filas), "rutas": filas}
open(OUT, "w", encoding="utf-8").write(json.dumps(res, ensure_ascii=False, indent=1) + "\n")
print(res["n"], "rutas;", res["por_grupo"], "| iguales en HEAD:", res["todas_iguales_en_HEAD"])
