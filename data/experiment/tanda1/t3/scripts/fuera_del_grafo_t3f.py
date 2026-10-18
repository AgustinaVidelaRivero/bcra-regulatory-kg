"""B6.1, tanda 1, T3 (desde el punto 4, decisión 3 de la autora del 18/10/2026): las anclas de cada ítem de la suite, sacadas de su
definición en scripts/regression_kg.py, y la clase «fuera del grafo» en los grafos de la tanda sola. Solo lee; corre sobre una copia.

Las anclas de un ítem son los TOs que nombra su definición:
  - el código: el cierre de llamadas de su función en el registro TESTS (las funciones del módulo que llama, y los métodos de Grafo,
    Contexto y Catalogo que usa), recorrido por AST. Cuentan las constantes de TO (CLA, CAP, PRO, RIC y EXT, por TO_PREFIJO), las
    cadenas «<to>::<punto>» (también por una constante del módulo, como EJ_DESTINO) y las cadenas que son el id de un TO del inventario
    (data/experiment/escalado_prep/inventario_tos.csv);
  - los datos que el código lee como anclas: `anclas` de DEF_IDS_NUEVOS (los ítems ID-*) y, si el cierre usa Contexto.muestra30, los
    TOs de las anclas de esa muestra (MUESTRA30);
  - el campo `direccionamiento` del registro, como control: un TO que nombra y el código no, es FRENO (no se pueden sacar por script).
Un ítem sin anclas es general: vale en todo grafo. En un grafo de una tanda sola, un ítem con anclas, todas de TOs que el grafo no
tiene (los `tos` de su manifiesto de ensamblado), es «fuera del grafo»: se informa aparte y no cuenta. El detalle de la suite no se usa.
Cruce: en los dos grafos de la tanda 1, las regresiones fuera del grafo, sin las declaradas, tienen que ser los 15 ítems que
clasificar_regresiones_t3.py dio como «no declarada, solo sin los TOs de la tanda 0»; si no, FRENO.
Uso: python3 -I -B fuera_del_grafo_t3f.py <raíz> <salida.json>
"""
import ast
import csv
import importlib.util
import json
import re
import sys
from pathlib import Path

RAIZ, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
X = "data/experiment/reextraccion_v2"
A = "data/experiment/tanda1/t3/acumulado"
GRAFOS = {
    "veinte": {"suite": f"{X}/corpus_tanda1/ens_veinte_r2b/suite_perfil_r2.json", "manifiesto": f"{X}/manifiestos/tanda1_ens_veinte_r2b.json",
               "tanda_sola": True},
    "veinte_sincola": {"suite": f"{X}/corpus_tanda1/ens_veinte_r2b_sincola/suite_perfil_r2.json",
                       "manifiesto": f"{X}/manifiestos/tanda1_ens_veinte_r2b_sincola.json", "tanda_sola": True},
    "acumulado": {"suite": f"{A}/ens_treinta_r2b/suite_perfil_r2.json", "manifiesto": f"{A}/manifiestos/acumulado_ens_treinta_r2b.json",
                  "tanda_sola": False},
    "acumulado_sincola": {"suite": f"{A}/ens_treinta_r2b_sincola/suite_perfil_r2.json",
                          "manifiesto": f"{A}/manifiestos/acumulado_ens_treinta_r2b_sincola.json", "tanda_sola": False}}
DECLARADAS_LAUDO = ("RT-C5-3", "RT-C6-1", "RT-C6-2")      # docs/laudo_release_r2_pipeline.md:70-72
DECLARADAS_AUTORA = ("E4-a1", "E4-a4")                    # decisión 2 de la autora del 18/10/2026
CLASIFICACION_T3 = "data/experiment/tanda1/t3/salidas/clasificacion_regresiones_t3.json"
RE_CHUNK = re.compile(r"^([a-z][a-z0-9_]*)::\d")
RE_CHUNK_TXT = re.compile(r"\b([a-z][a-z0-9_]*)::\d")
RE_TO_CONST = re.compile(r"\bTO_[a-z_]+")

src_path = RAIZ / "scripts/regression_kg.py"
spec = importlib.util.spec_from_file_location("regression_kg", src_path)
RK = importlib.util.module_from_spec(spec)
sys.modules["regression_kg"] = RK
spec.loader.exec_module(RK)
arbol = ast.parse(src_path.read_text(encoding="utf-8"))
inventario = {f["id"] for f in csv.DictReader((RAIZ / "data/experiment/escalado_prep/inventario_tos.csv").open(encoding="utf-8"))}
to_de_const = {v: k for k, v in RK.TO_PREFIJO.items()}          # "TO_capitales" → "cap"
nombre_const = {n: v for n, v in vars(RK).items() if isinstance(v, str) and v in to_de_const}   # CAP → "TO_capitales"
str_mod = {n: v for n, v in vars(RK).items() if isinstance(v, str)}
funcs = {n.name: n for n in arbol.body if isinstance(n, ast.FunctionDef)}
metodos = {}
for c in arbol.body:
    if isinstance(c, ast.ClassDef) and c.name in ("Grafo", "Contexto", "Catalogo"):
        for m in c.body:
            if isinstance(m, ast.FunctionDef):
                metodos.setdefault(m.name, []).append(m)


def cierre(nombre: str) -> dict:
    vistos, pila = set(), [funcs[nombre]]
    out = {"funciones": set(), "constantes_de_to": set(), "chunks": set(), "ids_de_to": set(), "usa_muestra30": False}
    while pila:
        f = pila.pop()
        if id(f) in vistos:
            continue
        vistos.add(id(f))
        out["funciones"].add(f.name)
        for nd in ast.walk(f):
            if isinstance(nd, ast.Name):
                if nd.id in funcs and funcs[nd.id] is not f:
                    pila.append(funcs[nd.id])
                if nd.id in nombre_const:
                    out["constantes_de_to"].add(nd.id)
                elif nd.id in str_mod and RE_CHUNK.match(str_mod[nd.id]):
                    out["chunks"].add(str_mod[nd.id])
            elif isinstance(nd, ast.Attribute):
                if nd.attr == "muestra30":
                    out["usa_muestra30"] = True
                for m in metodos.get(nd.attr, []):
                    pila.append(m)
            elif isinstance(nd, ast.Constant) and isinstance(nd.value, str):
                if RE_CHUNK.match(nd.value):
                    out["chunks"].add(nd.value)
                elif nd.value in inventario:
                    out["ids_de_to"].add(nd.value)
    return out


def tos_de_muestra30() -> set:
    filas = json.loads(RK.MUESTRA30.read_text(encoding="utf-8"))
    tos = set()
    for f in filas:
        for k in ("source_ancla", "target_ancla", "destino"):
            m = RE_CHUNK.match(str(f.get(k) or ""))
            if m:
                tos.add(m.group(1))
        for a in f.get("target_anclas_todas") or []:
            m = RE_CHUNK.match(str(a))
            if m:
                tos.add(m.group(1))
    return tos


items, freno = {}, []
for t in RK.TESTS:
    iid, fn = t["id"], t["fn"].__name__
    reg = {"funcion": fn, "direccionamiento": t["direccionamiento"]}
    if fn.startswith("t_id_"):
        s = "Sujeto_" + fn.removeprefix("t_id_")
        d = RK.DEF_IDS_NUEVOS[s]
        c = cierre("t_id_nuevo")
        reg["fuente"] = "DEF_IDS_NUEVOS[...]['anclas'] y el cierre de t_id_nuevo"
        de_datos = {x[0] for x in d["anclas"]}
    elif fn in funcs:
        c = cierre(fn)
        reg["fuente"] = "cierre de la función"
        de_datos = tos_de_muestra30() if c["usa_muestra30"] else set()
        if c["usa_muestra30"]:
            reg["fuente"] += " y MUESTRA30"
    else:
        freno.append(f"{iid}: la función {fn} no está en el módulo")
        continue
    tos = ({to_de_const[nombre_const[n]] for n in c["constantes_de_to"]} | {RE_CHUNK.match(x).group(1) for x in c["chunks"]}
           | c["ids_de_to"] | de_datos)
    dir_tos = {to_de_const[x] for x in RE_TO_CONST.findall(t["direccionamiento"]) if x in to_de_const} | set(
        RE_CHUNK_TXT.findall(t["direccionamiento"]))
    reg.update({"anclas": sorted(tos), "constantes_de_to": sorted(c["constantes_de_to"]), "chunks": sorted(c["chunks"]),
                "ids_de_to_literales": sorted(c["ids_de_to"]), "de_datos": sorted(de_datos), "funciones_del_cierre": len(c["funciones"]),
                "direccionamiento_nombra": sorted(dir_tos), "direccionamiento_no_cubierto_por_el_codigo": sorted(dir_tos - tos)})
    if dir_tos - tos:
        freno.append(f"{iid}: el direccionamiento nombra {sorted(dir_tos - tos)} y el código no")
    items[iid] = reg

res = {"items": items, "grafos": {}, "freno_anclas": freno}
for g, cfg in GRAFOS.items():
    su = json.loads((RAIZ / cfg["suite"]).read_text(encoding="utf-8"))
    tos_g = {t["id"] for t in json.loads((RAIZ / cfg["manifiesto"]).read_text(encoding="utf-8"))["tos"]}
    ids_suite = [i["id"] for i in su["items"]]
    if set(ids_suite) != set(items):
        freno.append(f"{g}: los ítems de la suite no son los del registro ({sorted(set(ids_suite) ^ set(items))})")
    estado = {i["id"]: i["estado"] for i in su["items"]}
    regres = [r["item"] for r in (su.get("regresion") or {}).get("regresiones", [])]
    fila = {}
    for iid, reg in items.items():
        an = set(reg["anclas"])
        alcance = "general" if not an else ("fuera del grafo" if not (an & tos_g) else "en el grafo")
        fila[iid] = {"alcance": alcance, "anclas_en_el_grafo": sorted(an & tos_g), "estado": estado.get(iid)}
    cl = {}
    for r in regres:
        fuera = cfg["tanda_sola"] and fila[r]["alcance"] == "fuera del grafo"
        if r in DECLARADAS_LAUDO:
            c = "declarada (laudo)"
        elif r in DECLARADAS_AUTORA:
            c = "declarada (autora, 18/10/2026)"
        else:
            c = "no declarada"
        cl[r] = {"clase": c, "fuera_del_grafo": fuera, "cuenta": (c == "no declarada" and not fuera)}
    res["grafos"][g] = {
        "manifiesto": cfg["manifiesto"], "tos": len(tos_g), "tanda_sola": cfg["tanda_sola"], "resumen_suite": su.get("resumen"),
        "entrada": (su.get("regresion") or {}).get("entrada"), "regresiones": len(regres), "por_regresion": cl,
        "no_declaradas_que_cuentan": sorted(r for r, v in cl.items() if v["cuenta"]),
        "regresiones_fuera_del_grafo": sorted(r for r, v in cl.items() if v["fuera_del_grafo"]),
        "items_fuera_del_grafo": (sorted(i for i, v in fila.items() if v["alcance"] == "fuera del grafo") if cfg["tanda_sola"] else None),
        "items_por_alcance": {k: sum(1 for v in fila.values() if v["alcance"] == k) for k in ("general", "en el grafo", "fuera del grafo")},
        "por_item": fila}

cla = json.loads((RAIZ / CLASIFICACION_T3).read_text(encoding="utf-8"))
cruce = {}
for g in ("veinte", "veinte_sincola"):
    quince = sorted(f["item"] for f in cla[g]["filas"] if f["clase"] == "no declarada, solo sin los TOs de la tanda 0")
    mio = sorted(r for r in res["grafos"][g]["regresiones_fuera_del_grafo"] if r not in DECLARADAS_LAUDO + DECLARADAS_AUTORA)
    cruce[g] = {"de_clasificar_regresiones_t3": quince, "de_este_script": mio, "iguales": quince == mio, "cuantos": [len(quince), len(mio)]}
    if quince != mio:
        freno.append(f"{g}: el cruce con clasificar_regresiones_t3.py no da los mismos ítems")
res["cruce"] = cruce
res["ok"] = not freno
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for iid, reg in items.items():
    print(f"{iid:<28} {reg['anclas']} ({reg['fuente']}; dir: {reg['direccionamiento_nombra']})")
for g, v in res["grafos"].items():
    print(f"{g}: {v['tos']} TOs; regresiones {v['regresiones']}; fuera del grafo {len(v['regresiones_fuera_del_grafo'])}; "
          f"no declaradas que cuentan {v['no_declaradas_que_cuentan']}; ítems por alcance {v['items_por_alcance']}")
for g, v in cruce.items():
    print(f"cruce {g}: {v['cuantos']} iguales {v['iguales']}")
print("FRENO: " + " | ".join(freno) if freno else "OK")
sys.exit(1 if freno else 0)
