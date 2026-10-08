"""U-MED-UMBRALES: elementos vacíos del validador y bases resueltas por origen (solo lectura, sin juicio).

Uso: python -B vacios_y_resueltas_UMEDUMBRALES.py <kg.json> [<kg.json> ...]
Vacío: sin valor, sin base y con comparacion no_determinada. Autor como en estratos_umbrales_UMEDUMBRALES.py.
"""
import collections
import json
import sys

for ruta in sys.argv[1:]:
    g = json.load(open(ruta))
    vac, res, to_grupo = collections.Counter(), collections.Counter(), collections.Counter()
    for n in g["nodes"]:
        for el in (n.get("properties", {}).get("umbrales") or []):
            a = "validador" if str(el.get("regla_comparacion", "")).startswith("limite_relativo:") else "ensamblado"
            vacio = el.get("valor") is None and el.get("base") is None and el.get("comparacion") == "no_determinada"
            vac[(a, "vacio" if vacio else "con_contenido")] += 1
            to_grupo["desarrollo" if n["provenance"].get("to") in ("cap", "cla", "ext", "pro", "ric") else "nuevos"] += 1
            if el.get("base_via"):
                res[(el.get("origen"), el.get("base_via"), n["provenance"].get("to"))] += 1
    nombre = ruta.rsplit("/", 1)[-1]
    print(nombre, "vacios", dict(sorted(vac.items())), sum(vac.values()))
    print(nombre, "resueltas", dict(sorted(res.items())), sum(res.values()))
    print(nombre, "elementos por grupo de TOs", dict(sorted(to_grupo.items())), sum(to_grupo.values()))
