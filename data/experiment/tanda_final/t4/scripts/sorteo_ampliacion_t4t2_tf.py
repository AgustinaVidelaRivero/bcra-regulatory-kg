"""B6.1, tanda final, T4, segundo tramo, punto 5 del «seguí»: el sorteo de la ampliación del estrato cuya atención saltó (las aceptadas no
ítems: tasas_t4t2_tf.py, `ampliacion`). Sigue t3/scripts/sorteos_t4_t3f_tf.py, con las mismas cuotas y reglas de celda de la tanda 1
(tanda1/t3/scripts/celdas_t4_t3f.py, `asignar`, sin cambios; su sha256 se controla), sobre las unidades del estrato que no se leyeron.
  - La población: las unidades de aceptadas:no_items de t3/muestras/poblaciones_t4_t3f_tf.json, por celda, menos las 30 de la muestra
    leída (t3/muestras/aceptadas_no_items.json). Controles: la muestra leída está toda en la población, y las sorteadas no están en ella.
  - Las cuotas: asignar() sobre lo que queda en cada celda.
  - Cada celda: random.Random(f"tandafinal:{muestra}:{celda}:ampliacion:{base}").sample(sorted(ids_que_quedan), cuota), con
    muestra = aceptadas:no_items (la cadena del «seguí», punto 5; pre-registro, §6: «las ampliaciones con `:ampliacion:`») y la base
    0897d609…: el sha256 de la versión para firmar commiteada en 5289b02f, como en T3. Controles: la base es ese sha256, y el texto
    firmado (4de7f2a7, sha256 b760edf7…) nombra la base, trae la plantilla de la cadena tal cual y la marca «`:ampliacion:`».
  - Si una celda entra entera (su cuota es todo lo que le queda), no se sortea.
  - La muestra va a <salida>/aceptadas_no_items_ampliacion.json, sin la hora, para que dos corridas den los mismos bytes (frena si ya
    existe); la hora y su sha256 van en <salida>/sorteo_ampliacion_t4t2_tf.json.
Uso: python3 -I -B sorteo_ampliacion_t4t2_tf.py <raíz> <versión para firmar (5289b02f)> <versión firmada (4de7f2a7)> <tasas.json> <salida>
"""
import hashlib
import json
import random
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, PARA_FIRMAR, FIRMADO, TASAS, OUT = (Path(x) for x in sys.argv[1:6])
RAIZ = RAIZ.resolve()
sys.path.insert(0, str(RAIZ / "data/experiment/tanda1/t3/scripts"))
import celdas_t4_t3f as CT  # noqa: E402

CT_SHA = "f0082e3cd588e855e65d024fc360d669abba6da134199bc0b06bfc2a63e40c29"
BASE = "0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b"
FIRMADO_SHA = "b760edf7d341290ad910de993f8a868be426abcf2cfd14459240ad5a2b940cc2"
PLANTILLA = 'random.Random(f"tandafinal:{muestra}:{celda}:{base}").sample(sorted(ids_de_la_celda), cuota)'
M = "aceptadas:no_items"
TF = RAIZ / "data/experiment/tanda_final"
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731

assert sha(Path(CT.__file__).read_bytes()) == CT_SHA, "celdas_t4_t3f.py no es el de la tanda 1"
assert sha(PARA_FIRMAR.read_bytes()) == BASE, "la base no es el sha256 de la versión para firmar"
fb = FIRMADO.read_bytes()
assert sha(fb) == FIRMADO_SHA, "el texto firmado no da su sha256"
ft = fb.decode("utf-8")
assert PLANTILLA in ft and BASE in ft and "`:ampliacion:`" in ft, "el texto firmado no trae la plantilla, la base o «:ampliacion:»"
tasas = json.loads(TASAS.read_text(encoding="utf-8"))
assert tasas["ampliacion"]["salta"] == {"aceptadas:items": False, "aceptadas:no_items": True, "RI": False}, tasas["ampliacion"]["salta"]
POB = TF / "t3/muestras/poblaciones_t4_t3f_tf.json"
LEIDA = TF / "t3/muestras/aceptadas_no_items.json"
pob = json.loads(POB.read_text(encoding="utf-8"))["muestras"][M]
leida = json.loads(LEIDA.read_text(encoding="utf-8"))
f = OUT / "aceptadas_no_items_ampliacion.json"
if f.exists() or (OUT / "sorteo_ampliacion_t4t2_tf.json").exists():
    raise SystemExit(f"FRENO: ya existe la salida en {OUT}")
quedan, ctrl = {}, {}
for c in CT.CELDAS:
    todos = set(pob["ids_por_celda"][c])
    leidos = set(leida["celdas"][c]["elementos"])
    ctrl[f"{c}: la muestra leída está en la población"] = leidos <= todos and len(leidos) == leida["celdas"][c]["n"]
    quedan[c] = sorted(todos - leidos)
assert all(ctrl.values()), ctrl
Nq = {c: len(quedan[c]) for c in CT.CELDAS}
a = CT.asignar(Nq)
assert not a["entera_sin_celdas"]
out = {"muestra": f"{M}:ampliacion", "estrato": M, "elemento": pob["elemento"], "base": BASE, "N_del_estrato": pob["N"],
       "N_por_celda_del_estrato": pob["N_por_celda"], "leidas_por_celda": {c: leida["celdas"][c]["n"] for c in CT.CELDAS},
       "N_por_celda_que_quedan": Nq, "n_por_celda": a["n"], "notas": a["notas"], "celdas": {}}
for c in CT.CELDAS:
    cadena = f"tandafinal:{M}:{c}:ampliacion:{BASE}"
    if a["n"][c] == len(quedan[c]):
        sel, como = list(quedan[c]), "entran todos"
    else:
        sel, como = random.Random(cadena).sample(quedan[c], a["n"][c]), "sorteo"
    assert not set(sel) & set(leida["celdas"][c]["elementos"])
    out["celdas"][c] = {"cadena": cadena, "N": len(quedan[c]), "n": len(sel), "como": como, "elementos": sel}
out["n"] = sum(x["n"] for x in out["celdas"].values())
assert out["n"] == 30
OUT.mkdir(parents=True, exist_ok=True)
f.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
indice = {"hora": datetime.now().astimezone().isoformat(timespec="seconds"), "archivo": f.name, "sha256": sha(f.read_bytes()), "n": out["n"],
          "n_por_celda": out["n_por_celda"], "base": BASE, "version_para_firmar_sha256": sha(PARA_FIRMAR.read_bytes()),
          "preregistro_firmado_sha256": FIRMADO_SHA, "celdas_t4_t3f_sha256": CT_SHA, "poblaciones_sha256": sha(POB.read_bytes()),
          "muestra_leida_sha256": sha(LEIDA.read_bytes()), "tasas_sha256": sha(TASAS.read_bytes()), "controles": ctrl}
(OUT / "sorteo_ampliacion_t4t2_tf.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"{out['muestra']}: {out['n']} unidades {out['n_por_celda']} (quedan {Nq}); {f.name} {indice['sha256']} {indice['hora']}")
