"""U-OMISIONES-COD, O1 — grupo D: (h) las aristas de extracción separadas de las derivadas y (i) los nodos que pasan de
la ventana de 40 vecinos, sobre uno o más kg.json. Solo lee.

(h): la clasificación de la observación 10 del tablero (`reext_t0/t3/medicion_tablero_r2b.py`, `obs10`): remisión
(`remite_a`, o `referencia` con rol_fuente referencia_cruzada), otra `referencia`, esqueleto, `establecida_en`
derivada (rol_fuente derivada_de_procedencia) y el resto, de extracción.
(i): dos definiciones, con la lista de nodos de cada una:
  - «ventana del agente»: `ver_vecinos(id, direccion="ambas", limite=40)` (`evaluacion/harness.py:197-235`) corta
    por dirección: un nodo pasa si tiene más de 40 aristas salientes o más de 40 entrantes; con todas las relaciones
    («con remite_a») y sin `remite_a` («sin remite_a»);
  - «grado total» (la de las cifras 43 y 22 de la v6, reconstruida): más de 40 aristas entre entrantes y salientes,
    contando solo `remite_a`, y contando todas menos `remite_a`; y también con todas.
Uso: python -B medir_h_i.py --kg nombre=ruta [--kg nombre=ruta ...] --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

LIMITE = 40


def rf(e):
    return e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")


def obs10(kg: dict) -> dict:
    c = Counter()
    for e in kg["edges"]:
        if e["relation"] == "remite_a" or (e["relation"] == "referencia" and rf(e) == "referencia_cruzada"):
            c["remite_a"] += 1
        elif e["relation"] == "referencia":
            c["referencia_texto_ordenado_comunicacion"] += 1
        elif rf(e) == "esqueleto":
            c["esqueleto"] += 1
        elif e["relation"] == "establecida_en" and rf(e) == "derivada_de_procedencia":
            c["establecida_en_derivada"] += 1
        else:
            c["extraccion"] += 1
    return dict(sorted(c.items()))


def navegacion(kg: dict) -> dict:
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    sal, ent = Counter(), Counter()
    sal_r, ent_r = Counter(), Counter()
    for e in kg["edges"]:
        sal[e["source"]] += 1
        ent[e["target"]] += 1
        if e["relation"] == "remite_a":
            sal_r[e["source"]] += 1
            ent_r[e["target"]] += 1
    ids = sorted(tipo)

    def lista(pred):
        xs = [i for i in ids if pred(i)]
        return {"n": len(xs), "por_tipo": dict(Counter(tipo[i] for i in xs)),
                "lista": [{"id": i, "type": tipo[i], "salientes": sal[i], "entrantes": ent[i],
                           "salientes_remite_a": sal_r[i], "entrantes_remite_a": ent_r[i]} for i in xs]}
    return OrderedDict([
        ("ventana_del_agente_con_remite_a", lista(lambda i: sal[i] > LIMITE or ent[i] > LIMITE)),
        ("ventana_del_agente_sin_remite_a", lista(lambda i: sal[i] - sal_r[i] > LIMITE or ent[i] - ent_r[i] > LIMITE)),
        ("grado_total_solo_remite_a", lista(lambda i: sal_r[i] + ent_r[i] > LIMITE)),
        ("grado_total_sin_remite_a", lista(lambda i: sal[i] + ent[i] - sal_r[i] - ent_r[i] > LIMITE)),
        ("grado_total_todas", lista(lambda i: sal[i] + ent[i] > LIMITE))])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--kg", action="append", required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    res = OrderedDict()
    for x in a.kg:
        nom, ruta = x.split("=", 1)
        b = Path(ruta).read_bytes()
        kg = json.loads(b)
        nav = navegacion(kg)
        res[nom] = OrderedDict([("sha256", hashlib.sha256(b).hexdigest()), ("aristas", len(kg["edges"])),
                                ("h_obs10", obs10(kg)), ("i_navegacion", nav)])
        print(nom, res[nom]["sha256"][:8], res[nom]["h_obs10"],
              {k: v["n"] for k, v in nav.items()})
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
