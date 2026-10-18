"""U-ALCANCE-E1, A3 (USD 0, sin API; solo lectura): las 78 rutas del código de la cadena de la tanda 1
(data/experiment/controles_tanda1/codigo_de_la_cadena_47c9f1b3_mesa.json), cada una con su sha256 en la base (git show
<base>:<ruta>), en la copia de HEAD y en la de A3, y si A3 la cambia. Da también si en la base ya difería del sellado en la
lista (el de 47c9f1b3), para que la re-sellada del commit de A3 (pre-registro de la tanda final, §2) sepa qué toca A3 y qué
no. No re-sella la lista: eso lo hace el commit de A3 con el script de la mesa.
Uso: python3 -I -B cadena_78_a3.py <repo> <base> <copia_head> <copia_a3> <salida.json>
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

repo, base, ch, ca, salida = sys.argv[1], sys.argv[2], Path(sys.argv[3]), Path(sys.argv[4]), Path(sys.argv[5])
LISTA = "data/experiment/controles_tanda1/codigo_de_la_cadena_47c9f1b3_mesa.json"


def git_show(ruta: str) -> bytes:
    return subprocess.run(["git", "--no-optional-locks", "-C", repo, "show", f"{base}:{ruta}"], capture_output=True,
                          check=True).stdout


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


lista = json.loads(git_show(LISTA))
filas = []
for r in lista["rutas"]:
    b = sha(git_show(r["ruta"]))
    h = sha((ch / r["ruta"]).read_bytes())
    a = sha((ca / r["ruta"]).read_bytes())
    filas.append({"ruta": r["ruta"], "grupo": r["grupo"], "sha256_sellado_en_47c9f1b3": r["sha256"], "sha256_base": b,
                  "base_igual_al_sellado": b == r["sha256"], "copia_head_igual_a_la_base": h == b,
                  "sha256_a3": a, "cambia_con_a3": a != b})
res = {"lista": LISTA, "lista_sha256_en_la_base": sha(git_show(LISTA)), "n": len(filas),
       "copia_head_igual_a_la_base_en_las_78": all(f["copia_head_igual_a_la_base"] for f in filas),
       "en_la_base_distintas_del_sellado": [f["ruta"] for f in filas if not f["base_igual_al_sellado"]],
       "cambian_con_a3": [f["ruta"] for f in filas if f["cambia_con_a3"]], "rutas": filas}
salida.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "rutas"}, ensure_ascii=False, indent=1))
