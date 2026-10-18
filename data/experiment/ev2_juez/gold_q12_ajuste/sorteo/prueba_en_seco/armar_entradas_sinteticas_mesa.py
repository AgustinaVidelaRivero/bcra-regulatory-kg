"""Entradas sintéticas con la forma de las de EV2, para la prueba en seco del sorteo antes del sello (mesa, §128).

Uso: python3 -I -B armar_entradas_sinteticas_mesa.py <carpeta>   (escribe un repo falso con los tres archivos que lee el sorteo)
"""
import hashlib
import json
import random
import sys

F = sys.argv[1]
dos = {"ext": 16, "cap": 8, "cla": 6, "ric": 5, "pro": 5}
pq = []; i = 0
for t, n in dos.items():
    for _ in range(n):
        i += 1; pq.append({"id": f"SINT-{i:03d}", "to": t, "to_nombre": t, "pregunta": "x", "gold": {"ancla": [], "criterios": []}})
json.dump({"preguntas": pq}, open(f"{F}/data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json", "w"))
filas = []
for p in pq:
    for g, lab in (("run_3", "ev2_base_run3"), ("v3", "ev2_base_v3"), ("v2", "ev2_base_v2")):
        h = hashlib.sha256(f"{p['id']}|{g}".encode()).hexdigest()
        filas.append({"id_opaco": "SINTR-" + h[:10], "id_pregunta": p["id"], "grafo": g, "label": lab, "sha256_respuesta": h,
                      "respondible_flag": True, "n_criterios": 4})
json.dump({"filas": filas}, open(f"{F}/data/experiment/ev2_fidelidad_eval/desanonimizacion/tabla_id_opaco.json", "w"))
r = random.Random("sintetico")
mues = []
for g in ("run_3", "v3", "v2"):
    mues += [{"id_opaco_base": f["id_opaco"]} for f in r.sample([f for f in filas if f["grafo"] == g], 4)]
json.dump({"muestra": mues}, open(f"{F}/data/experiment/ev2_adjudicacion/adjudicacion/reporte_muestra_simetrica.json", "w"))
print("sintético listo")
