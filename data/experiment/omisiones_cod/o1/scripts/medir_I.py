"""U-OMISIONES-COD, O1 — grupo I: «Condiciones sin regla» sobre uno o más kg.json (solo lee). Condicion sin ninguna
arista de contenido: ninguna arista, entrante o saliente, fuera de `establecida_en` y `remite_a` (en un grafo r1, la
remisión es `referencia` con rol_fuente referencia_cruzada); la variante: Condicion sin `condicion_de` saliente. Y
los nodos de grado 0 (M9) por tipo.
Uso: python -B medir_I.py --kg nombre=ruta [...] --out <json>"""
import argparse, hashlib, json, sys
from collections import Counter, OrderedDict
from pathlib import Path

def rf(e):
    return e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")

def no_contenido(e):
    return e["relation"] in ("establecida_en", "remite_a") or (e["relation"] == "referencia" and rf(e) == "referencia_cruzada")

def medir(kg):
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    con_contenido, con_cond_de, grado = set(), set(), Counter()
    for e in kg["edges"]:
        grado[e["source"]] += 1; grado[e["target"]] += 1
        if not no_contenido(e):
            con_contenido |= {e["source"], e["target"]}
        if e["relation"] == "condicion_de":
            con_cond_de.add(e["source"])
    cond = sorted(i for i, t in tipo.items() if t == "Condicion")
    sin_c = [i for i in cond if i not in con_contenido]
    sin_cd = [i for i in cond if i not in con_cond_de]
    ais = [i for i in tipo if grado[i] == 0]
    return OrderedDict([("condicion", len(cond)), ("sin_arista_de_contenido", len(sin_c)),
                        ("sin_condicion_de_saliente", len(sin_cd)), ("mismos_nodos", sin_c == sin_cd),
                        ("aislados", len(ais)), ("aislados_por_tipo", dict(Counter(tipo[i] for i in ais))),
                        ("lista_sin_arista_de_contenido", sin_c)])

ap = argparse.ArgumentParser(); ap.add_argument("--kg", action="append", required=True); ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args(); res = OrderedDict()
for x in a.kg:
    nom, ruta = x.split("=", 1); b = Path(ruta).read_bytes(); r = medir(json.loads(b))
    res[nom] = OrderedDict([("sha256", hashlib.sha256(b).hexdigest())] + list(r.items()))
    print(nom, res[nom]["sha256"][:8], {k: v for k, v in r.items() if k != "lista_sin_arista_de_contenido"})
a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
