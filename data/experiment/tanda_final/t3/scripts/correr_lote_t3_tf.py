"""Corre un lote de cadenas (copia de data/experiment/tanda1/t3/scripts/correr_lote_t3.py, sin cambios de lógica) (una por renglón, campos separados por «|»: script, python, copia, grafo, salida, consola) de a
--workers, con bash, y escribe el código de salida de cada una. Las rutas pueden llevar espacios. USD 0, sin API.
Uso: python3 -I -B correr_lote_t3.py <lote.txt> <salida.json> [--workers 4]"""
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

LOTE, OUT = sys.argv[1], sys.argv[2]
W = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 4
filas = [x.rstrip("\n").split("|") for x in open(LOTE, encoding="utf-8") if x.strip()]


def uno(f):
    t0 = time.strftime("%Y-%m-%d %H:%M:%S")
    rc = subprocess.run(["bash", *f]).returncode
    return {"grafo": f[3], "salida": f[4].split("/scratchpad/")[-1], "rc": rc, "inicio": t0, "fin": time.strftime("%Y-%m-%d %H:%M:%S")}


with ThreadPoolExecutor(W) as ex:
    res = list(ex.map(uno, filas))
json.dump(res, open(OUT, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(json.dumps(res, ensure_ascii=False, indent=1))
