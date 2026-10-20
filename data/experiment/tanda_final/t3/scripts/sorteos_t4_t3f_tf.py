"""B6.1, tanda final, T3, punto 7.4: los sorteos de la cola, de las aceptadas (ítems y no ítems) y de las vigilancias (2) y (7), con
data/experiment/tanda1/t3/scripts/sorteos_t4_t3f.py copiado y adaptado a la tanda final, con las reglas de las celdas y las clases chicas
de la tanda 1 (celdas_t4_t3f.asignar, sin cambios; su sha256 se controla). Solo lee poblaciones_t4_t3f_tf.py y dos versiones del
pre-registro de la tanda final; no lee ninguna unidad ni marca nada.
  - Cada celda: random.Random(f"tandafinal:{muestra}:{celda}:{base}").sample(sorted(ids_de_la_celda), cuota) (pre-registro de la tanda
    final, §6), con la base 0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b. Controles: la base es el sha256 de la
    versión para firmar commiteada en 5289b02f (git show 5289b02f:docs/preregistro_tanda_final.md, a una copia), y el texto firmado
    (git show 4de7f2a7, sha256 b760edf7…) nombra esa base y trae la cadena tal cual. La tanda final no enumera las cadenas: se arman con
    la plantilla.
  - Si una celda entra entera (su cuota es todo lo que tiene), no se sortea; si la población tiene 30 elementos o menos, entra entera,
    sin celdas. Las cadenas de la ampliación no se usan ahora.
  - Cada muestra va a <salida>/<muestra>.json (los «:» del nombre, como «_»; frena si alguno ya existe), sin la hora para que dos corridas den los mismos bytes; la
    hora y el sha256 de cada archivo van en <salida>/sorteos_t4_t3f_tf.json.
Uso: python3 -I -B sorteos_t4_t3f_tf.py <poblaciones_t4_t3f_tf.json> <versión para firmar (5289b02f)> <versión firmada (4de7f2a7)>
       <salida>
"""
import hashlib
import json
import random
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
POB, PARA_FIRMAR, FIRMADO, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3]), Path(sys.argv[4])
RAIZ = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(RAIZ / "data/experiment/tanda1/t3/scripts"))
import celdas_t4_t3f as CT  # noqa: E402

CT_SHA = "f0082e3cd588e855e65d024fc360d669abba6da134199bc0b06bfc2a63e40c29"
BASE = "0897d609851ae712768f0c1b68c2a485d5d8d91903aca84f3b54df58664d488b"
FIRMADO_SHA = "b760edf7d341290ad910de993f8a868be426abcf2cfd14459240ad5a2b940cc2"
PLANTILLA = 'random.Random(f"tandafinal:{muestra}:{celda}:{base}").sample(sorted(ids_de_la_celda), cuota)'
MUESTRAS = ["cola", "aceptadas:items", "aceptadas:no_items", "vigilancia:2", "vigilancia:7"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


assert sha(Path(CT.__file__).read_bytes()) == CT_SHA, "celdas_t4_t3f.py no es el de la tanda 1"
assert sha(PARA_FIRMAR.read_bytes()) == BASE, "la base no es el sha256 de la versión para firmar"
fb = FIRMADO.read_bytes()
assert sha(fb) == FIRMADO_SHA, "el texto firmado no da su sha256"
ft = fb.decode("utf-8")
assert PLANTILLA in ft and BASE in ft, "el texto firmado no trae la plantilla o la base"
pb = POB.read_bytes()
pob = json.loads(pb)
ya = [f for f in [m.replace(":", "_") + ".json" for m in MUESTRAS] + ["sorteos_t4_t3f_tf.json"] if (OUT / f).exists()]
if ya:
    raise SystemExit(f"FRENO: ya existen en {OUT}: {ya}")
OUT.mkdir(parents=True, exist_ok=True)
indice = {"base": BASE, "version_para_firmar_sha256": sha(PARA_FIRMAR.read_bytes()), "preregistro_firmado_sha256": FIRMADO_SHA,
          "poblaciones_sha256": sha(pb), "poblaciones_hora": pob["hora"], "grafo": pob["grafo"],
          "celdas_t4_t3f_sha256": sha(Path(CT.__file__).read_bytes()), "muestras": {}}
for m in MUESTRAS:
    p = pob["muestras"][m]
    ids = {c: [tuple(x) if isinstance(x, list) else x for x in v] for c, v in p["ids_por_celda"].items()}
    a = CT.asignar(p["N_por_celda"])
    out = {"muestra": m, "elemento": p["elemento"], "base": BASE, "N": p["N"], "N_por_celda": p["N_por_celda"],
           "sha256_ids_por_celda": p["sha256_ids_por_celda"], "entera_sin_celdas": a["entera_sin_celdas"], "n_por_celda": a["n"],
           "notas": a["notas"], "celdas": {}}
    for c in CT.CELDAS:
        cadena = f"tandafinal:{m}:{c}:{BASE}"
        pobl = sorted(ids[c])
        if a["entera_sin_celdas"] or a["n"][c] == len(pobl):
            sel, como = pobl, "entran todos"
        else:
            sel, como = random.Random(cadena).sample(pobl, a["n"][c]), "sorteo"
        out["celdas"][c] = {"cadena": cadena, "N": len(pobl), "n": len(sel), "como": como,
                            "elementos": [list(x) if isinstance(x, tuple) else x for x in sel]}
    out["n"] = sum(x["n"] for x in out["celdas"].values())
    f = OUT / f"{m.replace(':', '_')}.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    indice["muestras"][m] = {"archivo": f.name, "sha256": sha(f.read_bytes()), "n": out["n"], "n_por_celda": out["n_por_celda"],
                             "hora": datetime.now().astimezone().isoformat(timespec="seconds")}
indice["no_se_usan"] = "las cadenas de la ampliación"
indice["las_arma_sorteos_t4t1_tf"] = ["vigilancia:1", "vigilancia:3", "observacion:12"]
(OUT / "sorteos_t4_t3f_tf.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in indice["muestras"].items():
    print(f"{m}: {x['n']} elementos {x['n_por_celda']}, {x['archivo']} {x['sha256']} {x['hora']}")
