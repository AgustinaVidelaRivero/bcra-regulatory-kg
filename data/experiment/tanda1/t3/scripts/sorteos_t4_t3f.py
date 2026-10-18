"""B6.1, tanda 1, T3, punto 7.4: los sorteos de T4 con las cadenas del pre-registro firmado (95b18217:1019-1062) y sus reglas para las
celdas y las clases chicas (§5.4 y §5.4 bis, punto 2; celdas_t4_t3f.asignar). Solo lee poblaciones_t4.json y el texto firmado;
no lee ninguna unidad ni marca nada.
  - Cada celda: random.Random(f"tanda1:{muestra}:{celda}:{base}").sample(sorted(ids_de_la_celda), cuota), con la base
    33a3c34b897f59881860c10642084536929931f3fe94ded25f1e382693832059 (el sha256 de la tercera versión para firmar, 3b61f154). Cada
    cadena se controla contra las del texto firmado, que se lee de una copia (git show 95b18217, sha256 2a64cae8…).
  - Si una celda entra entera (su cuota es todo lo que tiene), no se sortea; si la población tiene 30 elementos o menos, entra entera,
    sin celdas. Las cadenas de la ampliación no se usan.
  - Las vigilancias (1) y (3) no se sortean (dicen «a definir»; la autora decide antes del sorteo).
  - Cada muestra va a <salida>/<muestra>.json (los «:» del nombre, como «_»), sin la hora para que dos corridas den los mismos bytes; la
    hora y el sha256 de cada archivo van en <salida>/sorteos_t4.json.
Uso: python3 -I -B sorteos_t4_t3f.py <poblaciones_t4.json> <preregistro firmado> <salida>
"""
import hashlib
import json
import random
import sys
from datetime import datetime
from pathlib import Path

POB, PRE, OUT = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
sys.path.insert(0, str(Path(__file__).resolve().parent))
import celdas_t4_t3f as CT  # noqa: E402

BASE = "33a3c34b897f59881860c10642084536929931f3fe94ded25f1e382693832059"
PRE_SHA = "2a64cae84c5862f174e7a89e92f1fb1274b6446a9e1d09d8ac59273a208ce4ae"
MUESTRAS = ["cola", "aceptadas:items", "aceptadas:no_items", "vigilancia:2", "vigilancia:7", "observacion:12"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


pre = PRE.read_bytes()
assert sha(pre) == PRE_SHA, "el texto firmado no da su sha256"
firmadas = {x.strip() for x in pre.decode("utf-8").splitlines()[1018:1062] if x.strip().startswith("tanda1:")}
assert len(firmadas) == 40, len(firmadas)
pb = POB.read_bytes()
pob = json.loads(pb)
if OUT.exists() and any(OUT.iterdir()):
    raise SystemExit(f"FRENO: {OUT} no está vacío")
OUT.mkdir(parents=True, exist_ok=True)
indice = {"base": BASE, "preregistro_firmado_sha256": PRE_SHA, "poblaciones_t4_sha256": sha(pb), "poblaciones_t4_hora": pob["hora"],
          "muestras": {}}
for m in MUESTRAS:
    p = pob["muestras"][m]
    ids = {c: [tuple(x) if isinstance(x, list) else x for x in v] for c, v in p["ids_por_celda"].items()}
    a = CT.asignar(p["N_por_celda"])
    out = {"muestra": m, "elemento": p["elemento"], "base": BASE, "N": p["N"], "N_por_celda": p["N_por_celda"],
           "entera_sin_celdas": a["entera_sin_celdas"], "n_por_celda": a["n"], "notas": a["notas"], "celdas": {}}
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
    f = OUT / f"{m.replace(':', '_')}.json"
    f.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    indice["muestras"][m] = {"archivo": f.name, "sha256": sha(f.read_bytes()), "n": out["n"],
                             "hora": datetime.now().astimezone().isoformat(timespec="seconds")}
indice["no_se_sortean"] = {"vigilancia:1": "dice «a definir» (preregistro_tanda0.md:594-602): la autora decide antes del sorteo",
                           "vigilancia:3": "ídem", "ampliacion": "las cadenas de la ampliación no se usan ahora"}
(OUT / "sorteos_t4.json").write_text(json.dumps(indice, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for m, x in indice["muestras"].items():
    print(f"{m}: {x['n']} elementos, {x['archivo']} {x['sha256']} {x['hora']}")
