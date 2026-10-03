"""Censo estructural USD 0 de la exposicion a F1 en una salida de E0.
Uso: python -B censo_encabezados.py <dir_con_subdirs_por_to_o_chunks> <salida.json> [--plano]
Clases, por punto NO terminal (su linea de titulo viaja solo como tramo `encabezado`):
  A  titulo terminado en ':' y sin mini-chunk intro  -> el contenido de la linea no tiene unidad
  B  titulo cortado (no termina en '.', ':' ni ';') -> la oracion empieza en la linea de titulo
  T  titulo terminado en '.' (titulo puro, presumible)
Por unidad terminal: C = item de lista (su ultimo bloque heredado termina en ':').
Por mini-chunk intro/chapeau: D = el bloque termina en ':'."""
import json, sys, re
from pathlib import Path
from collections import Counter, defaultdict
base = Path(sys.argv[1]); out = Path(sys.argv[2]); plano = "--plano" in sys.argv
def cargar(p):
    d = json.loads(p.read_text(encoding="utf-8")); return d["chunks"] if isinstance(d, dict) else d
archivos = sorted(base.glob("chunks_*.json")) if plano else sorted(base.glob("*/chunks_*.json"))
res = {"por_to": {}, "total": Counter(), "ejemplos": defaultdict(list)}
def fin(t):
    t = t.rstrip()
    return t[-1] if t else ""
for a in archivos:
    to = a.stem[len("chunks_"):]
    cs = cargar(a)
    ids = {c["id"] for c in cs}
    cnt = Counter(); cnt["unidades"] = len(cs)
    vistos = {}
    for c in cs:
        her = c.get("herencia") or []
        for h in her:
            if h["tipo"] == "encabezado" and not str(h["unidad_origen"]).startswith("S"):
                vistos.setdefault(h["unidad_origen"], h["texto"])
        if c.get("tipo") == "punto_terminal" and her:
            ult = her[-1]
            if fin(ult["texto"]) == ":":
                cnt["C_item_de_lista"] += 1
        if c.get("tipo") == "mini_chunk" and c.get("rol_bloque") in ("intro", "chapeau_seccion"):
            if fin(c["texto"]) == ":":
                cnt["D_chapeau_unidad_propia_con_dos_puntos"] += 1
    for u, tx in vistos.items():
        tiene_intro = f"{to}::{u}::intro" in ids
        f_ = fin(tx)
        if f_ == ":" and not tiene_intro:
            k = "A_titulo_con_dos_puntos_sin_intro"
        elif f_ == ":":
            k = "A2_titulo_con_dos_puntos_con_intro"
        elif f_ not in (".", ";"):
            k = "B_titulo_cortado"
        else:
            k = "T_titulo_con_punto"
        cnt[k] += 1
        if len(res["ejemplos"][k]) < 12:
            res["ejemplos"][k].append(f"{to}::{u} | {tx[:120]}")
    cnt["no_terminales_con_titulo"] = len(vistos)
    res["por_to"][to] = dict(cnt)
    res["total"].update(cnt)
res["total"] = dict(res["total"]); res["ejemplos"] = dict(res["ejemplos"])
res["n_tos"] = len(archivos)
out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"n_tos": res["n_tos"], "total": res["total"]}, ensure_ascii=False, indent=1))
