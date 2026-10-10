"""Calcula la cifra de (e) de U-OMISIONES-COD con la regla de la nota del 10/10/2026 al pie de la v7 (mesa).

Se corre recién con esa nota en el log. Controla el sello de la planilla y la carpeta del lector, cuenta las clases y aplica la regla:
- correcta: clase 1 o 3 (copia real); incorrecta: clase 2 (coincidencia legítima); dudosa: clase 4 (`instrucciones.md` del lector;
  `data/experiment/omisiones_cod/o1/diseno_O1.md:60-63`);
- las dudosas se excluyen; pasa si el límite inferior de Wilson al 95 % de correctas / decididas es 0,75 o más (al menos 12 decididas,
  todas correctas).

Uso: python3 -I -B calcular_e_mesa.py <carpeta del lector> <control_paquete_lector_e_mesa.json> <salida.json>
"""
import hashlib
import json
import math
import os
import sys

Z = 1.959963984540054
CORRECTAS, INCORRECTAS, DUDOSAS = {1, 3}, {2}, {4}


def wilson_inferior(k, n):
    if n == 0:
        return None
    p = k / n
    d = 1 + Z * Z / n
    c = p + Z * Z / (2 * n)
    r = Z * math.sqrt(p * (1 - p) / n + Z * Z / (4 * n * n))
    return (c - r) / d


def sha(p):
    return hashlib.sha256(open(p, "rb").read()).hexdigest()


def main(carpeta, control_p, salida):
    planilla = os.path.join(carpeta, "planilla.jsonl")
    sello = open(os.path.join(carpeta, "sello_planilla.txt"), encoding="utf-8").read().split("\n")
    sello_sha = sello[0].split()[-1]
    if sha(planilla) != sello_sha:
        sys.exit(f"la planilla no es la sellada: {sha(planilla)} frente a {sello_sha}")
    # la carpeta: todo lo del manifiesto de partida igual, salvo la planilla, que es la que llena el lector
    distintos = []
    for linea in open(os.path.join(carpeta, "manifest.txt"), encoding="utf-8"):
        partes = linea.split()
        if len(partes) < 2 or len(partes[0]) != 64:
            continue
        h, ruta = partes[0], partes[-1]
        if ruta == "planilla.jsonl":
            continue
        if not os.path.exists(os.path.join(carpeta, ruta)) or sha(os.path.join(carpeta, ruta)) != h:
            distintos.append(ruta)
    if distintos:
        sys.exit(f"la carpeta del lector cambió: {distintos}")
    control = json.load(open(control_p, encoding="utf-8"))
    mapa = {m["caso"]: m for m in control["mapa_caso_a_deteccion"]}
    filas = [json.loads(x) for x in open(planilla, encoding="utf-8") if x.strip()]
    if sorted(f["caso"] for f in filas) != sorted(mapa):
        sys.exit("los casos de la planilla no son los del mapa")
    por_clase = {c: sorted(f["caso"] for f in filas if f["clase"] == c) for c in (1, 2, 3, 4)}
    k = sum(len(por_clase[c]) for c in CORRECTAS)
    inc = sum(len(por_clase[c]) for c in INCORRECTAS)
    dud = sum(len(por_clase[c]) for c in DUDOSAS)
    n = k + inc
    assert k + inc + dud == len(filas) == len(mapa)
    li = wilson_inferior(k, n)
    pasa = li is not None and li >= 0.75
    out = {
        "sello_planilla_sha256": sello_sha,
        "hora_del_sello": sello[1].replace("hora del sello ", "") if len(sello) > 1 else None,
        "casos": len(filas),
        "por_clase": {str(c): len(v) for c, v in por_clase.items()},
        "correctas": k, "incorrectas": inc, "dudosas_excluidas": dud, "decididas": n,
        "wilson95_inferior": None if li is None else round(li, 4),
        "pasa": pasa,
        "regla": "dudosas excluidas; pasa si Wilson 95 % inferior >= 0,75 sobre las decididas (al menos 12, todas correctas)",
        "incorrectas_para_la_autora": [{"caso": c, **{x: mapa[c][x] for x in ("chunk_id", "local_id", "campo")}}
                                       for c in sorted(por_clase[2])],
        "dudosas": [{"caso": c, **{x: mapa[c][x] for x in ("chunk_id", "local_id", "campo")}} for c in sorted(por_clase[4])],
    }
    json.dump(out, open(salida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(json.dumps({x: out[x] for x in ("casos", "por_clase", "correctas", "incorrectas", "dudosas_excluidas", "decididas",
                                          "wilson95_inferior", "pasa")}, ensure_ascii=False))


if __name__ == "__main__":
    main(*sys.argv[1:4])
