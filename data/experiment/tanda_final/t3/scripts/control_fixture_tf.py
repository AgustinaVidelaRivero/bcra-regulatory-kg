"""B6.1, tanda final, T3, punto 4: el control de la fixture de la precisión de la firma, punto 3 (pre-registro de la tanda final): todo
lo que trae la versión de HEAD de scripts/regression_kg_esperado.json sigue igual, clave por clave (cada ruta de hoja con su valor), y
lo nuevo son solo entradas de `estado_esperado` con los nombres de los grafos de la tanda final. Solo lee: la versión de HEAD sale de
`git show HEAD:scripts/regression_kg_esperado.json` sobre el repo, y la nueva, de la copia.
Uso: python3 -I -B control_fixture_tf.py <repo> <fixture nueva> <salida.json>
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

R, NUEVA, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]), Path(sys.argv[3])
NOMBRES = ["KG-TandaFinal-r2b", "KG-TandaFinal-r2b-sincola", "KG-TandaFinal-Tramo1-r2b", "KG-TandaFinal-Tramo1-r2b-sincola",
           "KG-Acumulado-Tandas0y1yFinal-r2b", "KG-Acumulado-Tandas0y1yFinal-r2b-sincola", "KG-Acumulado-Tandas0y1yTramo1-r2b",
           "KG-Acumulado-Tandas0y1yTramo1-r2b-sincola"]


def hojas(x, p=()):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from hojas(v, p + (k,))
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from hojas(v, p + (i,))
    else:
        yield p, x


hb = subprocess.run(["git", "-C", str(R), "show", "HEAD:scripts/regression_kg_esperado.json"], capture_output=True, check=True).stdout
nb = NUEVA.read_bytes()
h, n = json.loads(hb), json.loads(nb)
hh, hn = dict(hojas(h)), dict(hojas(n))
quitadas = [k for k in hh if k not in hn]
cambiadas = [k for k in hh if k in hn and hh[k] != hn[k]]
nuevas = [k for k in hn if k not in hh]
fuera = [k for k in nuevas if not (len(k) >= 2 and k[0] == "estado_esperado" and k[1] in NOMBRES)]
entradas = sorted({k[1] for k in nuevas if k[0] == "estado_esperado"})
res = {"head_sha256": hashlib.sha256(hb).hexdigest(), "nueva_sha256": hashlib.sha256(nb).hexdigest(),
       "claves_de_HEAD": len(hh), "quitadas": len(quitadas), "cambiadas": len(cambiadas), "claves_nuevas": len(nuevas),
       "nuevas_fuera_de_las_ocho_entradas": [list(map(str, k)) for k in fuera[:20]], "entradas_nuevas": entradas,
       "son_las_ocho": entradas == sorted(NOMBRES),
       "orden_de_las_selladas_igual": list(n["estado_esperado"])[:len(h["estado_esperado"])] == list(h["estado_esperado"])}
res["ok"] = not quitadas and not cambiadas and not fuera and res["son_las_ocho"] and res["orden_de_las_selladas_igual"]
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
sys.exit(0 if res["ok"] else 1)
