"""Mesa, §406 (02/11/2026): qué trae cada JSON que podría entrar al 258, contra el precedente commiteado (analisis_validacion_v3.json):
textos largos, refs de fichas (como claves o como valores), listas o mapas por ficha, veredictos ficha por ficha, y agregados de una
sola ficha (que dejan ver un veredicto). Imprime cuentas y rutas de claves; ningún valor de texto.
  python3 -I -B que_trae_cada_json_mesa.py <nombre=ruta> ..."""
import json
import re
import sys
from collections import Counter

REF = re.compile(r"^[TV]\d{3}$")
REF_EN = re.compile(r"\b[TV]\d{3}\b")
VER = {"correcta", "incorrecta", "sostenido", "contradicho", "no_consta", "adjudicacion", "sin_consenso"}


def generalizar(ruta):
    return re.sub(r"\.[TV]\d{3}\b", ".<ref>", re.sub(r"\[\d+\]", "[]", ruta))


def recorrer(x, ruta, c):
    if isinstance(x, dict):
        if any(REF.match(k) for k in x):
            c["mapas_por_ref"][generalizar(ruta)] += 1
        if "fichas" in x and "k" in x and x.get("fichas") == 1 or ("n" in x and "k" in x and x.get("n") == 1):
            c["agregados_de_una_ficha"][generalizar(ruta)] += 1
        for k, v in x.items():
            recorrer(v, f"{ruta}.{k}", c)
    elif isinstance(x, list):
        if x and all(isinstance(e, dict) and ("ref" in e or "ficha" in e) for e in x):
            c["listas_por_ficha"][generalizar(ruta)] += 1
        for i, v in enumerate(x):
            recorrer(v, f"{ruta}[{i}]", c)
    elif isinstance(x, str):
        c["textos"][len(x) > 120] += 1
        if len(x) > 120:
            c["textos_largos"][generalizar(ruta)] += 1
        if REF.match(x):
            c["refs_como_valor"][generalizar(ruta)] += 1
        elif REF_EN.search(x):
            c["refs_dentro_de_un_texto"][generalizar(ruta)] += 1
        if x in VER:
            c["veredictos_como_valor"][generalizar(ruta)] += 1


for arg in sys.argv[1:]:
    nombre, ruta = arg.split("=", 1)
    d = json.load(open(ruta, encoding="utf-8"))
    c = {k: Counter() for k in ("textos", "textos_largos", "refs_como_valor", "refs_dentro_de_un_texto", "mapas_por_ref",
                                 "listas_por_ficha", "veredictos_como_valor", "agregados_de_una_ficha")}
    recorrer(d, "", c)
    print(f"== {nombre}: textos {sum(c['textos'].values())} (de más de 120 caracteres: {c['textos'][True]})")
    for k in ("textos_largos", "refs_como_valor", "refs_dentro_de_un_texto", "mapas_por_ref", "listas_por_ficha", "veredictos_como_valor",
              "agregados_de_una_ficha"):
        v = c[k]
        print(f"   {k}: {sum(v.values())}" + (f" en {dict(v.most_common(6))}" if v else ""))
