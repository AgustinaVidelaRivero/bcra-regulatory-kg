"""Arma segunda_lectura_c2.jsonl desde lectura_m1.txt y lectura_m2.txt (lectura de la mesa) y material.json.
Uso: python3 armar_jsonl.py <salida.jsonl>"""
import collections
import json
import re
import sys

M = json.load(open("material.json", encoding="utf-8"))
PREVIAS = {"cap::2.1", "cap::3.1.11.2", "cap::3.1.11.3"}  # leídas antes de recibir las cuatro reglas
M1 = {"CR": "condicion_con_relacion", "DN": "dentro_de_norma", "FU": "fusionado", "OM": "omitido", "SR": "sin_relacion"}
SUB = {"nh": "norma_en_heredado", "np": "norma_presente", "ne": "norma_no_emitida"}
M2 = {"V": "extraida_tramo_verificado", "NV": "extraida_tramo_no_verificable", "O": "omision_otra_vez", "AU": "ausente"}
BORDE = re.compile(r"alternativa de lectura|caso de borde|cubierto entre dos entidades|cobertura parcial|extendida de la regla 4")


def leer(path, med):
    cur = None
    anc = collections.defaultdict(dict)
    filas = []
    for ln in open(path, encoding="utf-8"):
        ln = ln.rstrip("\n")
        if not ln:
            continue
        if ln.startswith("U "):
            cur = ln[2:]
            continue
        m = re.match(r"^T (\S+) (.+)$", ln)
        if m:
            anc[cur][m.group(1)] = m.group(2)
            continue
        m = re.match(r"^([A-Z]) (\S+) (\S+) \| (.+)$", ln)
        assert m, ln
        filas.append((cur, m.group(2), m.group(1), m.group(3), m.group(4)))
    out = []
    for u, item, cod, cl, a_sal in filas:
        d = {"medicion": med, "unidad": u, "item": item, "codigo": cod}
        if med == "M1":
            n = int(item)
            s = next(x for x in M[u]["supuestos"] if x["n"] == n)
            d["item"] = n
            d["fragmento_fase_a"] = s["frase"]
            d["miembro"] = s["miembro"].replace("(miembros ", "").rstrip(")") if s["miembro"] else None
            base, _, sub = cl.partition(":")
            d["clase"] = M1[base]
            d["subtipo_sin_relacion"] = SUB[sub] if sub else None
        else:
            o = next(x for x in M[u]["omisiones_t4"] if x["clave"] == item)
            d["omision_t4"] = {"atributos": o["attrs"], "tramo": o["frase"]}
            base, _, cat = cl.partition(":")
            d["clase"] = M2[base]
            d["categoria_omision"] = cat or None
        d["ancla_salida"] = a_sal
        d["ancla_texto"] = anc[u][str(item)]
        d["caso_de_borde"] = bool(BORDE.search(a_sal))
        d["cobertura_segun_solapamiento_del_material"] = ("solapamiento por código" in a_sal)
        d["leida_antes_de_las_reglas"] = (med == "M1" and u in PREVIAS)
        out.append(d)
    return out


def main():
    filas = leer("lectura_m1.txt", "M1") + leer("lectura_m2.txt", "M2")
    orden = {u: i for i, u in enumerate(M)}
    filas.sort(key=lambda d: (orden[d["unidad"]], d["medicion"], str(d["item"]).zfill(4), d["codigo"]))
    with open(sys.argv[1], "w", encoding="utf-8") as f:
        for d in filas:
            f.write(json.dumps(d, ensure_ascii=False, sort_keys=True) + "\n")
    c = collections.Counter((d["medicion"]) for d in filas)
    print(len(filas), dict(c), "borde", sum(d["caso_de_borde"] for d in filas), "solap_material", sum(d["cobertura_segun_solapamiento_del_material"] for d in filas))


main()
