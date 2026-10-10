"""Sella la planilla: controla las 60 filas y escribe sello_planilla.txt con su sha256 y la hora. No cuenta marcas.
Uso, desde esta carpeta: python3 -I -B sellar_planilla.py"""
import json, hashlib, os, sys, datetime
AQUI = os.path.dirname(os.path.abspath(__file__))
P, S, F = (os.path.join(AQUI, x) for x in ("planilla.jsonl", "sello_planilla.txt", "fichas.jsonl"))
if os.path.exists(S):
    sys.exit("ya hay un sello: la planilla no se vuelve a sellar")
fichas = {json.loads(x)["ficha"]: json.loads(x) for x in open(F, encoding="utf-8") if x.strip()}
filas = [json.loads(x) for x in open(P, encoding="utf-8") if x.strip()]
errores = []
if sorted(r["ficha"] for r in filas) != sorted(fichas):
    errores.append("las fichas de la planilla no son las 60, una vez cada una")
for r in filas:
    if r.get("marca") not in ("correcta", "incorrecta", "no_decidible"):
        errores.append(f"{r.get('ficha')}: marca inválida")
    elif r["marca"] != "correcta" and not str(r.get("nota", "")).strip():
        errores.append(f"{r['ficha']}: falta la nota")
    if r.get("ficha") in fichas and not set(r.get("paginas_vistas", [])) <= set(fichas[r["ficha"]]["paginas_render"]):
        errores.append(f"{r['ficha']}: una página vista no es de la ficha")
if errores:
    sys.exit("no se sella:\n" + "\n".join(errores))
h = hashlib.sha256(open(P, "rb").read()).hexdigest()
hora = datetime.datetime.now().astimezone().isoformat(timespec="seconds")
open(S, "w").write(f"planilla.jsonl sha256 {h}\nhora del sello {hora}\nfilas {len(filas)}\n")
print(f"sellada: sha256 {h}, {hora}, {len(filas)} filas")
