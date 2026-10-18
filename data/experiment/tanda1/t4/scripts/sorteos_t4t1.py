"""B6.1, tanda 1, T4, primer tramo, punto 3: los sorteos de las vigilancias (1) y (3) y de la observación (12) rehecha, con las cadenas
del pre-registro firmado (95b18217:1019-1062) y sus reglas para las celdas y las clases chicas (§5.4 y §5.4 bis, punto 2), con
celdas_t4_t3f.asignar de T3, sin cambios. Solo lee poblaciones_t4_tramo1.json y el texto firmado; no lee ninguna unidad ni marca nada.
  - Cada celda: random.Random(f"tanda1:{muestra}:{celda}:{base}").sample(sorted(ids_de_la_celda), cuota), con la base
    33a3c34b897f59881860c10642084536929931f3fe94ded25f1e382693832059 (el sha256 de la tercera versión para firmar, 3b61f154). Cada
    cadena se controla contra las del texto firmado, que se lee de una copia (git show 95b18217, sha256 2a64cae8…).
  - Los ids: (1), el id del nodo Condicion; (3), el id del grupo (sus ids de nodo ordenados y unidos con «|»); la (12), la tripla
    (source, relation, target), ordenada como lista, como en T3.
  - Si una celda entra entera (su cuota es todo lo que tiene), no se sortea. Las cadenas de la ampliación no se usan.
  - Las otras cinco muestras (las de T3) no se tocan.
  - Cada muestra va a <salida>/<muestra>.json (los «:» del nombre, como «_»), sin la hora para que dos corridas den los mismos bytes; la
    hora y el sha256 de cada archivo van en <salida>/sorteos_t4_tramo1.json.
Uso: python3 -I -B sorteos_t4t1.py <poblaciones_t4_tramo1.json> <preregistro firmado> <salida>
"""
import hashlib
import json
import random
import sys
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
POB, PRE, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "t3" / "scripts"))
import celdas_t4_t3f as CT  # noqa: E402

CT_SHA = "f0082e3cd588e855e65d024fc360d669abba6da134199bc0b06bfc2a63e40c29"  # celdas_t4_t3f.py en HEAD (FRENO T3, §9)
BASE = "33a3c34b897f59881860c10642084536929931f3fe94ded25f1e382693832059"
PRE_SHA = "2a64cae84c5862f174e7a89e92f1fb1274b6446a9e1d09d8ac59273a208ce4ae"
MUESTRAS = ["vigilancia:1", "vigilancia:3", "observacion:12"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


assert sha(Path(CT.__file__).read_bytes()) == CT_SHA, "celdas_t4_t3f.py no es el de T3"
pre = PRE.read_bytes()
assert sha(pre) == PRE_SHA, "el texto firmado no da su sha256"
firmadas = {x.strip() for x in pre.decode("utf-8").splitlines()[1018:1062] if x.strip().startswith("tanda1:")}
assert len(firmadas) == 40, len(firmadas)
pb = POB.read_bytes()
pob = json.loads(pb)
if OUT.exists() and any(OUT.iterdir()):
    raise SystemExit(f"FRENO: {OUT} no está vacío")
OUT.mkdir(parents=True, exist_ok=True)
indice = {"base": BASE, "preregistro_firmado_sha256": PRE_SHA, "poblaciones_t4_tramo1_sha256": sha(pb),
          "poblaciones_t4_tramo1_hora": pob["hora"], "celdas_t4_t3f_sha256": sha(Path(CT.__file__).read_bytes()), "muestras": {}}
for m in MUESTRAS:
    p = pob["muestras"][m]
    ids = {c: [tuple(x) if isinstance(x, list) else x for x in v] for c, v in p["ids_por_celda"].items()}
    a = CT.asignar(p["N_por_celda"])
    out = {"muestra": m, "elemento": p["elemento"], "base": BASE, "N": p["N"], "N_por_celda": p["N_por_celda"],
           "sha256_ids_por_celda": p["sha256_ids_por_celda"], "entera_sin_celdas": a["entera_sin_celdas"], "n_por_celda": a["n"],
           "notas": a["notas"], "celdas": {}}
    for c in CT.CELDAS:
        cadena = f"tanda1:{m}:{c}:{BASE}"
        assert cadena in firmadas, cadena
        pobl = sorted(ids[c])
        if a["entera_sin_celdas"] or a["n"][c] == len(pobl):
            sel, como = pobl, "entran todos"
        else:
            sel, como = random.Random(cadena).sample(pobl, a["n"][c]), "sorteo"
        out["celdas"][c] = {"cadena": cadena, "N": len(pobl), "n": len(sel), "como": como,
                            "elementos": [list(x) if isinstance(x, tuple) else x for x in sel]}
    out["n"] = sum(x["n"] for x in out["celdas"].values())
    if m == "vigilancia:3":
        out["grupos"] = {g: pob["muestras"][m]["grupos"][g] for c in CT.CELDAS for g in out["celdas"][c]["elementos"]}
    f = OUT / f"{m.replace(':', '_')}.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    indice["muestras"][m] = {"archivo": f.name, "sha256": sha(f.read_bytes()), "n": out["n"],
                             "hora": datetime.now().astimezone().isoformat(timespec="seconds")}
indice["no_se_tocan"] = ["cola", "aceptadas:items", "aceptadas:no_items", "vigilancia:2", "vigilancia:7"]
indice["no_se_usan"] = "las cadenas de la ampliación"
(OUT / "sorteos_t4_tramo1.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
assert indice["celdas_t4_t3f_sha256"] == CT_SHA, "celdas_t4_t3f.py no es el de T3"
for m, x in indice["muestras"].items():
    print(f"{m}: {x['n']} elementos, {x['archivo']} {x['sha256']} {x['hora']}")
print("celdas_t4_t3f.py", indice["celdas_t4_t3f_sha256"])
