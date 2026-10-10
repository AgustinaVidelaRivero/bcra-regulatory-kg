"""Mesa, 10/10/2026, USD 0: resultado de la C4 de C2-bis de U-CONF-MATRIZ. Toma las marcas de la planilla sellada y les aplica las
adjudicaciones del acta de la autora (las 15 fichas de la lista de C4), sin cambiar ninguna otra marca; cuenta por par con el criterio del
§2 del mandato: el par se confirma si el límite inferior de Wilson al 95 % de correctas / (correctas + incorrectas) es al menos 0,75, con
las no decidibles excluidas, y si hay a lo sumo 6 no decidibles.
Uso: python3 -I -B c4_C2bis_mesa.py <planilla_C2bis_sellada.jsonl> <acta_C4_C2bis.md> <acta_c1.json> <c3_C2bis.json> <salida.json>"""
import hashlib, json, re, sys
from math import sqrt
pn, actap, c1p, c3p, out = sys.argv[1:6]
assert hashlib.sha256(open(pn, "rb").read()).hexdigest() == "abfde990d566533e7a78b21022b6564c466d6b8d24c92a611b49df135203e5b6"
marcas = {json.loads(x)["ficha"]: json.loads(x)["marca"] for x in open(pn, encoding="utf-8") if x.strip()}
par_de = {f["ficha"]: f["par"] for f in json.load(open(c1p))["orden_de_lectura"]["fichas"]}
assert set(marcas) == set(par_de) and len(marcas) == 60
c3 = json.load(open(c3p))
adj, par = {}, None
for l in open(actap, encoding="utf-8").read().split("\n"):
    if l.startswith("→ "):
        par = l[2:].strip()
    m = re.match(r"^- (F\d\d): (correcta|incorrecta|no decidible|no_decidible)\b", l)
    if m:
        adj[m.group(1)] = (par, m.group(2).replace(" ", "_"))
lista = {p: set(v["incorrectas"]) | set(v["no_decidibles"]) | set(v["correctas_sorteadas"]) for p, v in c3["lista_autora"].items()}
assert set(adj) == lista["Operacion"] | lista["Potestad"] and len(adj) == 15, "las fichas del acta no son las de la lista"
assert all(par_de[f] == p for f, (p, _) in adj.items()), "una ficha del acta está en otro par"
final = dict(marcas)
cambios = []
for f, (_, m) in adj.items():
    if m != final[f]:
        cambios.append((f, final[f], m))
    final[f] = m
def wilson_inf(k, n, z=1.959964):
    if n == 0:
        return None
    p = k / n
    return (p + z * z / (2 * n) - z * sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / (1 + z * z / n)
res = {"planilla_sha256": "abfde990…", "fichas_adjudicadas": len(adj), "marcas_cambiadas_por_la_autora": cambios, "por_par": {}}
for p in ("Operacion", "Potestad"):
    fs = [f for f in final if par_de[f] == p]
    c = sum(final[f] == "correcta" for f in fs); i = sum(final[f] == "incorrecta" for f in fs); nd = sum(final[f] == "no_decidible" for f in fs)
    assert c + i + nd == len(fs)
    li = wilson_inf(c, c + i)
    res["por_par"][p] = {"n": len(fs), "correctas": c, "incorrectas": i, "no_decidibles": nd,
                         "wilson95_inferior": None if li is None else round(li, 4), "decidible": nd <= 6,
                         "confirma": bool(nd <= 6 and li is not None and li >= 0.75)}
json.dump(res, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False))
