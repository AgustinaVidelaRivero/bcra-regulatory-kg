"""VERIF-UMBRALES, tarea 3: conteos de los elementos de umbral de un kg.json.

Uso: python -B conteo_umbrales.py <kg.json>
Autor del elemento: validador si regla_comparacion empieza con «limite_relativo:»
(validador_r2.elemento_umbral_relativo); ensamblado en otro caso
(ensamblar_tanda0.llenar_umbrales_r2). Solo lectura.
"""
import collections
import hashlib
import json
import sys

ruta = sys.argv[1]
datos = open(ruta, "rb").read()
print("sha256", hashlib.sha256(datos).hexdigest())
g = json.loads(datos)

C = collections.Counter
nodos_tipo, elem_tipo, autor, origen, autor_origen = C(), C(), C(), C(), C()
tv, tv_autor, base, base_autor, fuera, fuera_campo = C(), C(), C(), C(), C(), C()
comp, unidad, otras = C(), C(), C()
claves = C()
for n in g["nodes"]:
    us = n.get("properties", {}).get("umbrales")
    if n.get("properties_no_definidas", {}).get("umbral_no_cuantificable"):
        otras["nodo_umbral_no_cuantificable"] += 1
    if not us:
        continue
    nodos_tipo[n["type"]] += 1
    for el in us:
        claves.update(el.keys())
        a = "validador" if str(el.get("regla_comparacion", "")).startswith("limite_relativo:") else "ensamblado"
        elem_tipo[(n["type"], a)] += 1
        autor[a] += 1
        origen[el.get("origen")] += 1
        autor_origen[(a, el.get("origen"))] += 1
        tv[el.get("tramo_verificado")] += 1
        tv_autor[(a, el.get("tramo_verificado"))] += 1
        if el.get("base") is None:
            b = "sin_base"
        elif el.get("base_via"):
            b = "resuelta_" + el["base_via"]
        elif el.get("base_no_resuelta"):
            b = "marcada_base_no_resuelta"
        else:
            b = "con_base_sin_resolver_ni_marca"
        base[b] += 1
        base_autor[(a, b)] += 1
        fl = el.get("fuera_de_lista") or []
        fuera["con_marca" if fl else "sin_marca"] += 1
        for f in fl:
            fuera_campo[f] += 1
        comp[el.get("comparacion")] += 1
        unidad[(el.get("unidad"), "con_valor" if el.get("valor") is not None else "sin_valor")] += 1
        if el.get("comparacion_asumida"):
            otras["comparacion_asumida"] += 1
        otras["verificado_en_tabla=" + str(el.get("verificado_en_tabla"))] += 1
        if el.get("originales"):
            otras["con_originales"] += 1


def p(nombre, c):
    print(nombre, dict(sorted(c.items(), key=lambda kv: str(kv[0]))), "total", sum(c.values()))


p("nodos_con_lista_por_tipo", nodos_tipo)
p("elementos_por_tipo_y_autor", elem_tipo)
p("elementos_por_autor", autor)
p("elementos_por_origen", origen)
p("autor_x_origen", autor_origen)
p("tramo_verificado", tv)
p("tramo_verificado_x_autor", tv_autor)
p("base", base)
p("base_x_autor", base_autor)
p("fuera_de_lista", fuera)
p("fuera_de_lista_por_campo", fuera_campo)
p("comparacion", comp)
p("unidad_x_valor", unidad)
p("otras", otras)
p("claves_presentes", claves)
