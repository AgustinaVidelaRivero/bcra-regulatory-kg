"""U-ALCANCE-E1, A3 (USD 0, sin API; solo lee lo que se le pasa): selftest_clave_cache cuenta las claves de las bases de la caché
de E1 y de E3 (e1_extractor/cache/e1_extraccion.db y e3_verificador/cache/e3_verificacion.db), que desde T2 de la tanda 1
tienen también las llamadas de su extracción. Esas cuentas (los campos cuya ruta lleva «claves_db», y el renglón «claves r2b
en la db» de la consola) no van a ningún artefacto de A3 (cegamiento de U-MED-VERIF; mandato de A3, §6, PROHIBIDO).

  comparar A.json B.json: dice si los dos JSON son iguales sin esos campos, y qué rutas difieren, sin valores;
  retirar ENTRADA SALIDA: copia un JSON o una consola con esos valores cambiados por «<retirado>».
Uso: python3 -I -B clave_cache_sin_cuentas_a3.py comparar A B | retirar ENTRADA SALIDA
"""
import json
import re
import sys
from pathlib import Path

RETIRADO = "<retirado: cuenta de claves de la caché, que incluye la extracción de la tanda 1>"


def rutas(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from rutas(v, f"{p}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from rutas(v, f"{p}[{i}]")
    else:
        yield p, x


def retirar(x, p=""):
    if isinstance(x, dict):
        return {k: (RETIRADO if "claves_db" in k else retirar(v, f"{p}/{k}")) for k, v in x.items()}
    if isinstance(x, list):
        return [retirar(v, f"{p}[{i}]") for i, v in enumerate(x)]
    return x


if sys.argv[1] == "comparar":
    a, b = (json.loads(Path(p).read_text(encoding="utf-8")) for p in sys.argv[2:4])
    ra, rb = dict(rutas(a)), dict(rutas(b))
    difieren = [k for k in sorted(set(ra) | set(rb)) if ra.get(k) != rb.get(k)]
    fuera = [k for k in difieren if "claves_db" not in k]
    print(f"sin las cuentas de claves de la caché: {'iguales' if not fuera else 'DISTINTOS'}; rutas que difieren: "
          f"{len(difieren)} ({len(difieren) - len(fuera)} de cuentas de claves de la caché: "
          f"{[k for k in difieren if 'claves_db' in k]}; otras: {fuera})")
    sys.exit(0 if not fuera else 1)
entrada, salida = Path(sys.argv[2]), Path(sys.argv[3])
texto = entrada.read_text(encoding="utf-8")
if entrada.suffix == ".json":
    salida.write_text(json.dumps(retirar(json.loads(texto)), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
else:
    salida.write_text(re.sub(r"(claves r2b en la db de E1: )\d+", lambda m: m.group(1) + RETIRADO, texto), encoding="utf-8")
