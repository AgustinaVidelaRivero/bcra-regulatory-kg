"""U-MED-UMBRALES: recuento estructural del marco de muestreo de los elementos de umbral (solo lectura, sin juicio).

Uso: python -B estratos_umbrales_UMEDUMBRALES.py <kg.json> [<kg.json> ...]
Autor: validador si regla_comparacion empieza con «limite_relativo:» (validador_r2.elemento_umbral_relativo);
ensamblado en otro caso (ensamblar_tanda0.llenar_umbrales_r2). Mismo criterio que conteo_umbrales.py de
VERIF-UMBRALES. No juzga ningún campo: cuenta cuántos elementos caen en cada estrato propuesto.
"""
import collections
import hashlib
import json
import sys

PRED_CONTENIDO = ("aplica_a", "condicion_de", "limita", "regula", "requiere", "condiciona",
                  "exceptua_obligacion", "exceptua", "prohibe", "ejecuta")
DEV = ("cap", "cla", "ext", "pro", "ric")


def autor(el):
    return "validador" if str(el.get("regla_comparacion", "")).startswith("limite_relativo:") else "ensamblado"


def estado_base(el):
    if el.get("base") is None:
        return "sin_base"
    if el.get("base_via"):
        return "base_resuelta"
    return "base_sin_resolver"


def estrato(el):
    a = autor(el)
    o = el.get("origen")
    b = "con_base" if el.get("base") is not None else "sin_base"
    if a == "validador":
        return f"V-{b}"
    return f"E-{o}-{b}"


def p(nombre, c):
    print(nombre, dict(sorted(c.items(), key=lambda kv: str(kv[0]))), "total", sum(c.values()))


for ruta in sys.argv[1:]:
    datos = open(ruta, "rb").read()
    print("==", ruta.rsplit("/", 1)[-1], "sha256", hashlib.sha256(datos).hexdigest())
    g = json.loads(datos)
    C = collections.Counter
    est, est_unidad, est_comp, por_to, to_est, base3, mon, dias = C(), C(), C(), C(), C(), C(), C(), C()
    nodos_con = set()
    for n in g["nodes"]:
        us = n.get("properties", {}).get("umbrales")
        if not us:
            continue
        nodos_con.add(n["id"])
        to = (n.get("provenance") or {}).get("to")
        for el in us:
            e = estrato(el)
            est[e] += 1
            est_unidad[(e, el.get("unidad"))] += 1
            est_comp[(autor(el), el.get("comparacion"))] += 1
            por_to[to] += 1
            to_est[("dev" if to in DEV else "nuevo", e)] += 1
            base3[(autor(el), estado_base(el))] += 1
            if el.get("unidad") == "moneda":
                mon[el.get("moneda")] += 1
            if el.get("unidad") == "dias":
                dias[el.get("dias_tipo")] += 1
    print("nodos_con_lista", len(nodos_con), "nodos", len(g["nodes"]), "aristas", len(g["edges"]))
    p("estrato", est)
    p("estrato_x_unidad", est_unidad)
    p("autor_x_comparacion", est_comp)
    p("autor_x_estado_base", base3)
    p("moneda", mon)
    p("dias_tipo_en_unidad_dias", dias)
    p("elementos_por_to", por_to)
    p("dev_o_nuevo_x_estrato", to_est)
    cont = [e for e in g["edges"] if e.get("relation") in PRED_CONTENIDO]
    con_umbral = [e for e in cont if e.get("source") in nodos_con or e.get("target") in nodos_con]
    origen_umbral = [e for e in cont if e.get("source") in nodos_con]
    print("aristas_contenido", len(cont), "con_extremo_con_umbral", len(con_umbral),
          "con_origen_con_umbral", len(origen_umbral))
    p("aristas_contenido_con_extremo_con_umbral_por_predicado", C(e["relation"] for e in con_umbral))
