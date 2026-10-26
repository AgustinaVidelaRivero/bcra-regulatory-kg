"""Mesa, §277 (26/10/2026): el cruce del gold de Q12, mitad de verificación, con los juicios del juez de A2.2. USD 0, sin API.

Es `data/experiment/ev2_juez/gold_q12_ajuste/cruce/cruce_gold_q12_ajuste_mesa.py` (§145), como pide Q8 (§4: «El cruce, después del
sello de la autora, con el script de la mitad de ajuste»), con estos cambios:
  - del lado del juez, sus juicios de N = 1 de A2.2 (`data/experiment/banco_mcp/a2_2/juez/n1/agregados_n1_ciego.json`), con el sha256
    que fijó la clave del sorteo; no hay veredictos definitivos de EV2, así que sale la cifra por vía;
  - el control de las planillas va adentro: el sha256 y los bytes de su sello, las columnas y los renglones de
    `estructura_planillas.json`, y cada valor obligatorio, con la lectura del sello de la autora (acepta «,» o «;» y el BOM;
    mayúsculas, tildes y «_» no importan);
  - el criterio de aceptación (Q8, §1; registro, §9, `:298-299`): Wilson inferior de al menos 0,85 por criterio y al menos 18 de 20 por
    respuesta, sobre la cifra principal, con todas las marcas adentro. El Wilson se compara sin redondear;
  - lo que se informa aparte (`como_se_mide_el_juez_gold_q12_verificacion.md`, punto 5): las marcas, los errores fuera de los
    criterios (solo cuántos y en qué fichas) y los minutos (solo los que son un número).
Mide lo que fija `como_se_mide_el_juez_gold_q12_verificacion.md`, con las dos propuestas de la §145: un «dudoso» del juez (o un
«sin_consenso») cuenta como desacuerdo, con la cifra sin esos pares al lado; y la cifra sin «necesita experto del dominio» ni
«criterio mal planteado», al lado de la principal. El criterio i de la ficha es el i del juez: los dos siguen el orden del gold
(`armar_fichas_gold_q12_verificacion_mesa.py`, `enumerate(crits, 1)`; `a2_2/comun_a2_2.py`, `cargar_preguntas`).
No lee ni guarda la nota, el fragmento ni «cuál». Imprime solo cifras.
Uso: python3 -I -B cruce_gold_q12_verificacion_mesa.py <carpeta con las planillas de la autora> <clave> <repo o clon> <salida.json>"""
import csv
import hashlib
import io
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

A, CLAVE, CL, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
PC, PR = "planilla_criterios_gold_q12_verificacion.csv", "planilla_respuestas_gold_q12_verificacion.csv"
AGR = "data/experiment/banco_mcp/a2_2/juez/n1/agregados_n1_ciego.json"
UMBRAL_WILSON, UMBRAL_RESPUESTAS = 0.85, 18


def plegar(s):
    s = unicodedata.normalize("NFD", (s or "").strip().lower())
    return " ".join("".join(c for c in s if unicodedata.category(c) != "Mn").replace("_", " ").split())


def leer(p):
    t = p.read_bytes().decode("utf-8-sig")
    pr = t.splitlines()[0] if t else ""
    d = ";" if pr.count(";") > pr.count(",") else ","
    filas = [f for f in csv.reader(io.StringIO(t), delimiter=d) if any(x.strip() for x in f)]
    cols = [c.strip() for c in filas[0]]
    return cols, [dict(zip(cols, [c.strip() for c in f] + [""] * (len(cols) - len(f)))) for f in filas[1:]]


# --- el sello y la estructura ---
sello = [ln for ln in (A / "sello_gold_q12_verificacion.txt").read_text(encoding="utf-8").splitlines() if ln and not ln.startswith("#")]
sel = {ln.split()[-1]: (ln.split()[0], int(ln.split()[1])) for ln in sello}
assert sorted(sel) == sorted([PC, PR]), "el sello no trae las dos planillas"
for n, (sha, b) in sel.items():
    x = (A / n).read_bytes()
    assert hashlib.sha256(x).hexdigest() == sha and len(x) == b, f"{n} no da el sha256 o los bytes de su sello"
est = json.loads((A / "estructura_planillas.json").read_text(encoding="utf-8"))
cab, crit = leer(A / PC)
cab_r, filas_r = leer(A / PR)
assert cab == est["criterios"]["columnas"] and cab_r == est["respuestas"]["columnas"], "las columnas no son las de la plantilla"
assert [[c["ficha"], c["criterio"]] for c in crit] == est["criterios"]["renglones"], "los renglones de criterios no son los de la plantilla"
assert [[r["ficha"]] for r in filas_r] == est["respuestas"]["renglones"], "los renglones de respuestas no son los de la plantilla"
VER, DUD, EXP, MAL = cab[2], cab[4], cab[5], cab[6]
CLAS, ERR, MIN = cab_r[1], cab_r[2], cab_r[4]
resp = {r["ficha"]: r for r in filas_r}
VALOR = {"cumplido": "cumplido", "no cumplido": "no_cumplido"}
SINO = {"": False, "no": False, "si": True}
for c in crit:
    assert plegar(c[VER]) in VALOR, f"{c['ficha']}-{c['criterio']}: veredicto fuera de la plantilla"
    assert all(plegar(c[k]) in SINO for k in (DUD, EXP, MAL)), f"{c['ficha']}-{c['criterio']}: marca fuera de la plantilla"
for r in filas_r:
    assert plegar(r[CLAS]) in ("abstencion", "contenido") and plegar(r[ERR]) in ("si", "no"), f"{r['ficha']}: valor fuera de la plantilla"
# Las observaciones de formato: cuántas celdas no traen la forma de la plantilla tal cual y se leyeron igual (sin mostrar ninguna).
CANON = {VER: {"cumplido", "no_cumplido"}, DUD: {"sí", "no", ""}, EXP: {"sí", "no", ""}, MAL: {"sí", "no", ""},
         CLAS: {"abstencion", "contenido"}, ERR: {"sí", "no"}}
_b = {n: (A / n).read_bytes() for n in (PC, PR)}
_t = {n: b.decode("utf-8-sig") for n, b in _b.items()}
_d = {n: ";" if t.splitlines()[0].count(";") > t.splitlines()[0].count(",") else "," for n, t in _t.items()}
_crudo = {n: [f for f in csv.reader(io.StringIO(t), delimiter=_d[n]) if any(x.strip() for x in f)][1:] for n, t in _t.items()}
formato = {"delimitador": _d, "bom": {n: b.startswith(b"\xef\xbb\xbf") for n, b in _b.items()},
           "celdas_con_otra_forma_leidas_igual": {k: sum(fila[k] not in v for fila in (crit if k in (VER, DUD, EXP, MAL) else filas_r))
                                                  for k, v in CANON.items()},
           "celdas_con_espacios_de_mas": {PC: sum(f[i] != f[i].strip() for f in _crudo[PC] for i in (0, 1, 2, 4, 5, 6) if i < len(f)),
                                          PR: sum(f[i] != f[i].strip() for f in _crudo[PR] for i in (0, 1, 2, 4) if i < len(f))}}

clave_d = json.loads(CLAVE.read_text(encoding="utf-8"))
clave = clave_d["fichas"]
agr_b = (CL / AGR).read_bytes()
assert hashlib.sha256(agr_b).hexdigest() == clave_d["sha256_entradas"]["agregados"], "los agregados del juez no son los del sorteo"
agr = {x["id_opaco"]: x for x in json.loads(agr_b.decode("utf-8"))["agregados"]}
ORD = {"incorrecto": 0, "parcial": 1, "correcto": 2}


def wilson(k, n, z=1.959964):
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    r = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return [(c - r) / d, (c + r) / d]


def w4(k, n):
    w = wilson(k, n)
    return None if w is None else [round(w[0], 4), round(w[1], 4)]


def veredicto(marcas):
    if all(m == "cumplido" for m in marcas):
        return "correcto"
    if all(m == "no_cumplido" for m in marcas):
        return "incorrecto"
    return "parcial"


pares, respuestas = [], []
for f in clave:
    a = agr[f["id_opaco"]]
    assert a["n_criterios"] == f["n_criterios"] == len(a["modales"]), f["ficha"]
    mias = [c for c in crit if c["ficha"] == f["ficha"]]
    assert [int(c["criterio"]) for c in mias] == list(range(1, f["n_criterios"] + 1)), f["ficha"]
    for c, j in zip(mias, a["modales"]):
        pares.append({"par": f"{f['ficha']}-{c['criterio']}", "ficha": f["ficha"], "juez": j, "autora": VALOR[plegar(c[VER])],
                      "dudosa": SINO[plegar(c[DUD])], "experto": SINO[plegar(c[EXP])], "mal_planteado": SINO[plegar(c[MAL])]})
    va = veredicto([p["autora"] for p in pares if p["ficha"] == f["ficha"]])
    respuestas.append({"ficha": f["ficha"], "juez": a["veredicto_pregunta"], "autora": va, "clas_juez": a["clasificacion_respuesta_modal"],
                       "clas_autora": plegar(resp[f["ficha"]][CLAS]), "error_fuera": plegar(resp[f["ficha"]][ERR]) == "si",
                       "brazo": f["brazo"], "clase_del_sorteo": f["clase"], "to": f["to"]})


def cifras_criterio(ps):
    n = len(ps)
    acu = [p for p in ps if p["juez"] == p["autora"]]
    dud = [p for p in ps if p["juez"] in ("dudoso", "sin_consenso")]
    A_ = [p["par"] for p in ps if p["juez"] == "cumplido" and p["autora"] == "no_cumplido"]
    B_ = [p["par"] for p in ps if p["juez"] == "no_cumplido" and p["autora"] == "cumplido"]
    sin_d = [p for p in ps if p not in dud]
    k2 = sum(p["juez"] == p["autora"] for p in sin_d)
    return {"n": n, "acuerdo": len(acu), "fraccion": round(len(acu) / n, 4) if n else None, "wilson95": w4(len(acu), n),
            "direccion_A_juez_acredita": len(A_), "pares_A": A_, "direccion_B_juez_no_acredita": len(B_), "pares_B": B_,
            "dudoso_del_juez": len(dud), "pares_dudoso_del_juez": [p["par"] for p in dud],
            "sin_dudosos_del_juez": {"n": len(sin_d), "acuerdo": k2, "fraccion": round(k2 / len(sin_d), 4) if sin_d else None,
                                     "wilson95": w4(k2, len(sin_d))}}


def cifras_respuesta(rs):
    n = len(rs)
    acu = sum(r["juez"] == r["autora"] for r in rs)
    adj = [r["ficha"] for r in rs if r["juez"] == "requiere_adjudicacion"]
    A_ = [r["ficha"] for r in rs if r["juez"] in ORD and ORD[r["juez"]] > ORD[r["autora"]]]
    B_ = [r["ficha"] for r in rs if r["juez"] in ORD and ORD[r["juez"]] < ORD[r["autora"]]]
    sin = [r for r in rs if r["juez"] != "requiere_adjudicacion"]
    k2 = sum(r["juez"] == r["autora"] for r in sin)
    return {"n": n, "acuerdo": acu, "fraccion": round(acu / n, 4) if n else None, "wilson95": w4(acu, n),
            "direccion_A_juez_mas_favorable": len(A_), "fichas_A": A_, "direccion_B_juez_menos_favorable": len(B_), "fichas_B": B_,
            "requiere_adjudicacion": len(adj), "fichas_requiere_adjudicacion": adj,
            "sin_requiere_adjudicacion": {"n": len(sin), "acuerdo": k2, "fraccion": round(k2 / len(sin), 4) if sin else None}}


def minutos(r):
    s = r[MIN].strip().lower()
    m = re.fullmatch(r"(\d+(?:[.,]\d+)?)\s*(?:min|minutos|')?", s)
    return float(m.group(1).replace(",", ".")) if m else None


sin_marcas = [p for p in pares if not p["experto"] and not p["mal_planteado"]]
pc = cifras_criterio(pares)
pr = cifras_respuesta(respuestas)
w_inf = wilson(pc["acuerdo"], pc["n"])[0]
mins = {r["ficha"]: minutos(r) for r in filas_r}
out = {
 "insumos": {"sello": {n: s for n, (s, _) in sel.items()}, "clave_sha256": hashlib.sha256(CLAVE.read_bytes()).hexdigest(),
             "agregados_sha256": hashlib.sha256(agr_b).hexdigest()},
 "formato_de_las_planillas": formato,
 "criterio_de_aceptacion": {"wilson_inferior_por_criterio": round(w_inf, 4), "umbral_wilson": UMBRAL_WILSON,
                            "cumple_por_criterio": w_inf >= UMBRAL_WILSON, "acuerdo_por_respuesta": pr["acuerdo"],
                            "umbral_respuestas": UMBRAL_RESPUESTAS, "cumple_por_respuesta": pr["acuerdo"] >= UMBRAL_RESPUESTAS,
                            "cumple": w_inf >= UMBRAL_WILSON and pr["acuerdo"] >= UMBRAL_RESPUESTAS},
 "criterio": {f"principal_{len(pares)}": pc, "sin_experto_ni_mal_planteado": cifras_criterio(sin_marcas)},
 "respuesta": {"principal_20": pr},
 "clasificacion_abstencion_contenido": {"n": len(respuestas), "acuerdo": sum(r["clas_juez"] == r["clas_autora"] for r in respuestas),
                                        "desacuerdos": [r["ficha"] for r in respuestas if r["clas_juez"] != r["clas_autora"]]},
 "marcas_de_la_autora": {"dudosa": [p["par"] for p in pares if p["dudosa"]], "experto": [p["par"] for p in pares if p["experto"]],
                         "mal_planteado": [p["par"] for p in pares if p["mal_planteado"]]},
 "errores_fuera_de_los_criterios": {"n": sum(r["error_fuera"] for r in respuestas),
                                    "fichas": [r["ficha"] for r in respuestas if r["error_fuera"]]},
 "minutos": {"con_numero": sum(v is not None for v in mins.values()), "vacios": sum(not r[MIN].strip() for r in filas_r),
             "sin_numero_legible": sum(v is None and bool(r[MIN].strip()) for r, v in zip(filas_r, mins.values())),
             "total": round(sum(v for v in mins.values() if v is not None), 1)},
 "marcas_de_la_autora_por_criterio": dict(Counter(p["autora"] for p in pares)),
 "veredictos_de_la_autora_por_respuesta": dict(Counter(r["autora"] for r in respuestas)),
 "clasificacion_de_la_autora": dict(Counter(r["clas_autora"] for r in respuestas)),
 "veredictos_del_juez_por_respuesta": dict(Counter(r["juez"] for r in respuestas)),
 "modales_del_juez_por_criterio": dict(Counter(p["juez"] for p in pares)),
 "pares": pares, "respuestas": respuestas,
}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
c, s, ca = pc, out["criterio"]["sin_experto_ni_mal_planteado"], out["criterio_de_aceptacion"]
print(f"por criterio ({c['n']}): {c['acuerdo']} de {c['n']} ({c['fraccion']}; Wilson {c['wilson95']}); "
      f"A {c['direccion_A_juez_acredita']} {c['pares_A']}, B {c['direccion_B_juez_no_acredita']} {c['pares_B']}, "
      f"dudoso del juez {c['dudoso_del_juez']}; sin dudosos {c['sin_dudosos_del_juez']['acuerdo']} de {c['sin_dudosos_del_juez']['n']}")
print(f"  sin experto ni mal planteado: {s['acuerdo']} de {s['n']} ({s['fraccion']}; Wilson {s['wilson95']})")
print(f"por respuesta (20): {pr['acuerdo']} de 20 ({pr['fraccion']}; Wilson {pr['wilson95']}); A {pr['direccion_A_juez_mas_favorable']} "
      f"{pr['fichas_A']}, B {pr['direccion_B_juez_menos_favorable']} {pr['fichas_B']}, requiere adjudicación {pr['requiere_adjudicacion']}")
print(f"abstención o contenido: {out['clasificacion_abstencion_contenido']['acuerdo']} de 20 "
      f"{out['clasificacion_abstencion_contenido']['desacuerdos']}")
print(f"criterio de aceptación: Wilson inferior {ca['wilson_inferior_por_criterio']} (>= 0.85: {ca['cumple_por_criterio']}); "
      f"{ca['acuerdo_por_respuesta']} de 20 (>= 18: {ca['cumple_por_respuesta']}); cumple: {ca['cumple']}")
print(f"aparte: marcas {json.dumps(out['marcas_de_la_autora'], ensure_ascii=False)}; errores fuera {out['errores_fuera_de_los_criterios']}; "
      f"minutos {out['minutos']}")
print(f"formato: {json.dumps(formato, ensure_ascii=False)}")
print(f"de la autora: {out['marcas_de_la_autora_por_criterio']}, {out['veredictos_de_la_autora_por_respuesta']}, "
      f"{out['clasificacion_de_la_autora']}; del juez: {out['veredictos_del_juez_por_respuesta']}, {out['modales_del_juez_por_criterio']}")
