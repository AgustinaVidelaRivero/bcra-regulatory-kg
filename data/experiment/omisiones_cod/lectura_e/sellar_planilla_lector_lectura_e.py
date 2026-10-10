"""Sella la planilla: controla las 16 filas y escribe sello_planilla.txt con su sha256 y la hora. No cuenta clases.
Uso, desde esta carpeta: python3 -I -B sellar_planilla.py"""
import json, hashlib, os, sys, datetime
AQUI = os.path.dirname(os.path.abspath(__file__))
P, S, F = (os.path.join(AQUI, x) for x in ("planilla.jsonl", "sello_planilla.txt", "casos.jsonl"))
if os.path.exists(S):
    sys.exit("ya hay un sello: la planilla no se vuelve a sellar")
casos = {json.loads(x)["caso"]: json.loads(x) for x in open(F, encoding="utf-8") if x.strip()}
filas = [json.loads(x) for x in open(P, encoding="utf-8") if x.strip()]
errores = []
if sorted(r["caso"] for r in filas) != sorted(casos):
    errores.append("los casos de la planilla no son los 16, una vez cada uno")
for r in filas:
    if r.get("clase") not in (1, 2, 3, 4):
        errores.append(f"{r.get('caso')}: clase inválida")
    if not str(r.get("razon", "")).strip():
        errores.append(f"{r.get('caso')}: falta la razón")
    if r.get("caso") in casos and not set(r.get("paginas_vistas", [])) <= set(casos[r["caso"]]["paginas_render"]):
        errores.append(f"{r['caso']}: una página vista no es del caso")
if errores:
    sys.exit("no se sella:\n" + "\n".join(errores))
h = hashlib.sha256(open(P, "rb").read()).hexdigest()
hora = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
open(S, "w").write(f"planilla.jsonl sha256 {h}\nhora del sello {hora}\nfilas {len(filas)}\n")
print(f"sellada: sha256 {h}, {hora}, {len(filas)} filas")
