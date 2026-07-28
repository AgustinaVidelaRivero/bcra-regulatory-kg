#!/usr/bin/env python3
"""PASO 4 — mapping de anonimización (registro de cumplimiento).

El protocolo pide juzgar con el grafo anonimizado (etiqueta neutral por
pregunta, semilla registrada, mapping en archivo separado). El juez v2.1.1
es ciego por construcción: su payload (judge.py:274-297) contiene pregunta,
categoria, referente, descomposición, citas y respuesta — NUNCA la identidad
del grafo ni el run_key. La anonimización queda así garantizada
estructuralmente; este mapping se genera igual (semilla 20260726) como
registro auditable de qué brazo es A y cuál B por pregunta, para cualquier
lectura posterior a ciegas de las respuestas.
"""
import json
import random
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
RUNTIME = HERE / "EV1_runtime.json"
OUT = HERE / "corridas" / "mapping_anonimizacion.json"
SEED = 20260726

qids = [q["id"] for q in json.load(open(RUNTIME, encoding="utf-8"))["preguntas"]]
rng = random.Random(SEED)
mapping = {}
for q in sorted(qids):
    par = ["run_3", "grafo_v2"]
    rng.shuffle(par)
    mapping[q] = {"A": par[0], "B": par[1]}

out = {
    "fecha": "2026-07-26",
    "semilla": SEED,
    "nota": "El juez v2.1.1 no recibe la identidad del grafo en ningún campo "
            "de su payload (judge.py:274-297): la ceguera es estructural y no "
            "requirió pasada separada. Este mapping (A/B por pregunta, semilla "
            "registrada) queda como registro para lecturas humanas a ciegas.",
    "mapping": mapping,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
json.dump(out, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(f"OK mapping de {len(mapping)} preguntas (semilla {SEED}) en {OUT}")
