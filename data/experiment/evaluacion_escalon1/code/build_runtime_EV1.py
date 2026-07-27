#!/usr/bin/env python3
"""Deriva `EV1_runtime.json` de la key sellada `answer_key_EV1.json`.

Mapeo al contrato del juez (judge.py:270-297), sin tocar la key:
  - respuesta_esperada      = key_adjudicada
  - ground_truth_secciones  = puntos_citados  (mismo formato lista que CQN2)
  - categoria               = familia  (el juez solo bifurca en 'unanswerable',
                              familia que EV1 no contiene → abstencion/especulacion
                              quedan en null para las 36, por construcción)
  - cita_textual            = None  (el formato sellado del protocolo §2 no porta
                              cita verbatim separada: vive dentro de la respuesta
                              adjudicada; no se fabrica una. Simétrico entre brazos.)
Se conservan además los campos originales (tos_fuente habilita la guarda de
dominio del verificador; familia alimenta la tabla por familia).

Orden de ejecución: shuffle con random.Random(20260726) — semilla registrada
en el propio archivo (_meta) y en el informe de la unidad.
"""
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
KEY = HERE / "answer_key_EV1.json"
OUT = HERE / "EV1_runtime.json"
SEED = 20260726

k = json.load(open(KEY, encoding="utf-8"))
entries = k["preguntas"] if isinstance(k, dict) else k
assert len(entries) == 36, f"esperaba 36, hay {len(entries)}"

runtime = []
for q in entries:
    assert q.get("estado") == "verificada" and q.get("key_adjudicada"), q["id"]
    runtime.append({
        "id": q["id"],
        "pregunta": q["pregunta"],
        "categoria": q["familia"],
        "familia": q["familia"],
        "tos_fuente": q["tos_fuente"],
        "respuesta_esperada": q["key_adjudicada"],
        "cita_textual": None,
        "ground_truth_secciones": q["puntos_citados"],
    })

rng = random.Random(SEED)
rng.shuffle(runtime)

out = {
    "_meta": {
        "derivado_de": "answer_key_EV1.json (sellada; no modificada)",
        "fecha": "2026-07-26",
        "semilla_orden": SEED,
        "orden": [q["id"] for q in runtime],
        "mapeo": "respuesta_esperada=key_adjudicada | ground_truth_secciones="
                 "puntos_citados | categoria=familia | cita_textual=None "
                 "(formato sellado sin cita verbatim separada; simétrico entre brazos)",
    },
    "preguntas": runtime,
}
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"OK {OUT.name}: {len(runtime)} preguntas | semilla {SEED}")
print("orden:", " ".join(q["id"].replace("EV1-", "") for q in runtime))
