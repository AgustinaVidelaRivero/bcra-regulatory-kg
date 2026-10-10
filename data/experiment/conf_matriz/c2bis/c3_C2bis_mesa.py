"""Mesa, 09/10/2026, USD 0: C3 de la repetición de C2 de U-CONF-MATRIZ (C2-bis). Corre SOLO después del sello de la planilla nueva.
- Verifica el sello de la planilla nueva (sha256) y el del acta y las fichas de C1.
- El par de cada ficha sale del acta sellada de C1 (orden_de_lectura); la planilla nueva no lo trae.
- Por par: correctas, incorrectas y no decidibles; límite inferior de Wilson al 95 % de correctas / (correctas + incorrectas); el par
  se confirma si es ≥ 0,75 y hay a lo sumo 6 no decidibles (criterio del §2 del mandato firmado, que el lector no vio).
- La lista para la autora (C4): las incorrectas y las no decidibles de la lectura nueva (precisión del 10/10/2026); 5 correctas por par, sorteadas con la semilla sellada en la nota
  del mandato (`random.Random(semilla).sample(sorted(correctas por (origen, destino)), 5)`, todas si son menos); y toda ficha en la que
  la lectura nueva y la primera (contaminada) no coinciden.
Uso: python3 -B c3_C2bis_mesa.py <repo> <planilla_nueva.jsonl> <sello_planilla.txt> <planilla_primera.jsonl> <semilla_Operacion>
     <semilla_Potestad> <salida.json>"""
import json, sys, hashlib, random
from math import sqrt
repo, pn, sn, pp, sop, spo, out = sys.argv[1:8]
C1 = f"{repo}/data/experiment/conf_matriz/c1"
assert hashlib.sha256(open(f"{C1}/fichas_c1.jsonl", "rb").read()).hexdigest() == \
    "ebe7dd72bcd04b8c1781c1756f4048540d432c458adb35af7cf328bb17d3e8a3"
sello = open(sn).read()
h = hashlib.sha256(open(pn, "rb").read()).hexdigest()
assert h in sello, "la planilla nueva no es la sellada"
acta = json.load(open(f"{C1}/acta_c1.json"))
par_de = {f["ficha"]: f for f in acta["orden_de_lectura"]["fichas"]}
nueva = {json.loads(x)["ficha"]: json.loads(x) for x in open(pn, encoding="utf-8") if x.strip()}
primera = {json.loads(x)["ficha"]: json.loads(x) for x in open(pp, encoding="utf-8") if x.strip()}
assert set(nueva) == set(par_de) == set(primera)
def wilson_inf(k, n, z=1.959964):
    if n == 0:
        return None
    p = k / n
    return (p + z * z / (2 * n) - z * sqrt(p * (1 - p) / n + z * z / (4 * n * n))) / (1 + z * z / n)
semillas = {"Operacion": int(sop), "Potestad": int(spo)}
res = {"planilla_nueva_sha256": h, "por_par": {}, "lista_autora": {}}
for par in ("Operacion", "Potestad"):
    del_par = sorted((f for f in par_de.values() if f["par"] == par), key=lambda f: (f["origen"], f["destino"]))
    m = {k: [f["ficha"] for f in del_par if nueva[f["ficha"]]["marca"] == k] for k in ("correcta", "incorrecta", "no_decidible")}
    c, i, nd = len(m["correcta"]), len(m["incorrecta"]), len(m["no_decidible"])
    li = wilson_inf(c, c + i)
    res["por_par"][par] = {"n": len(del_par), "correctas": c, "incorrectas": i, "no_decidibles": nd,
                           "wilson95_inferior": None if li is None else round(li, 4),
                           "decidible": nd <= 6, "confirma": bool(nd <= 6 and li is not None and li >= 0.75)}
    corr = m["correcta"]
    sorteadas = random.Random(semillas[par]).sample(corr, 5) if len(corr) > 5 else list(corr)
    res["lista_autora"][par] = {"incorrectas": m["incorrecta"], "no_decidibles": m["no_decidible"],
                                "correctas_sorteadas": sorted(sorteadas), "semilla": semillas[par]}
res["discrepancias_con_la_primera"] = sorted(f for f in nueva if nueva[f]["marca"] != primera[f]["marca"])
json.dump(res, open(out, "w"), ensure_ascii=False, indent=1)
print(json.dumps({p: {k: v for k, v in d.items()} for p, d in res["por_par"].items()}, ensure_ascii=False))
print("discrepancias:", len(res["discrepancias_con_la_primera"]))
