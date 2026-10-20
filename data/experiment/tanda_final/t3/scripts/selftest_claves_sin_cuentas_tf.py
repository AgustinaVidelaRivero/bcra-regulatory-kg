"""
selftest_claves_sin_cuentas_tf.py — B6.1, tanda final, T3, punto 4 (registro de decisiones, §38): el retiro de las cuentas
de claves de las bases de la caché de las salidas de `selftest_clave_cache`, y el control de que el retiro las cubre, sin
mirarlas. Es t1/selftest_claves_sin_cuentas_t1.py con los nombres de T3. USD 0, sin API. Solo lee las entradas y escribe en
--salida.

`selftest_clave_cache` cuenta las claves de las bases de la caché de E1 y de E3, que incluyen las extracciones de las tandas 1 y final.
Las salidas originales no se abren: el retiro lo hace `data/experiment/alcance_e1/a3/scripts/clave_cache_sin_cuentas_a3.py`
(el mismo que usó A3), en un proceso aparte, y este script:
  1. escribe el sha256 de las dos originales (JSON y consola) en `sha256_selftest_clave_cache_originales_t3.txt`;
  2. corre el retiro sobre cada una;
  3. compara cada salida sin cuentas con la de A3 sin cuentas (`alcance_e1/a3/salidas/*_a3_sin_cuentas_a3.*`), que sale del
     mismo código (el de A3 es el de HEAD): si son iguales byte a byte, el retiro cubre toda cuenta (lo que cambia entre las
     dos corridas son solo las cuentas de las bases). Si una difiere, el retiro puede no cubrir una cuenta nueva: esa
     salida sin cuentas se renombra a `NO_ABRIR_<nombre>` y se da solo su sha256; del JSON se dan, además, las rutas de los
     campos que difieren (sin valores).
Imprime solo veredictos, rutas de campos y sha256; nunca un valor de las salidas.
Uso: python3 -I -B selftest_claves_sin_cuentas_t1.py --json <original> --consola <original> --retiro <script de A3>
       --json-a3 <A3 sin cuentas> --consola-a3 <A3 sin cuentas> --salida <dir>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rutas(x, p=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from rutas(v, f"{p}/{k}")
    elif isinstance(x, list):
        for i, v in enumerate(x):
            yield from rutas(v, f"{p}[{i}]")
    else:
        yield p, x


def main() -> int:
    ap = argparse.ArgumentParser()
    for k in ("--json", "--consola", "--retiro", "--json-a3", "--consola-a3", "--salida"):
        ap.add_argument(k, type=Path, required=True)
    a = ap.parse_args()
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "sha256_selftest_clave_cache_originales_t3.txt").write_text(
        f"{sha(a.json)}  selftest_clave_cache_t3.json (original, con las cuentas; no se abre)\n"
        f"{sha(a.consola)}  consola_selftest_clave_cache_t3.txt (original, con las cuentas; no se abre)\n", encoding="utf-8")
    sj = a.salida / "selftest_clave_cache_t3_sin_cuentas.json"
    sc = a.salida / "consola_selftest_clave_cache_t3_sin_cuentas.txt"
    for ent, sal in ((a.json, sj), (a.consola, sc)):
        subprocess.run([sys.executable, "-I", "-B", str(a.retiro), "retirar", str(ent), str(sal)], check=True)
    res = {"json_igual_al_de_a3_sin_cuentas": sj.read_bytes() == a.json_a3.read_bytes(),
           "consola_igual_a_la_de_a3_sin_cuentas": sc.read_bytes() == a.consola_a3.read_bytes()}
    if not res["json_igual_al_de_a3_sin_cuentas"]:
        ra, rb = dict(rutas(json.loads(a.json_a3.read_text(encoding="utf-8")))), dict(rutas(json.loads(sj.read_text(encoding="utf-8"))))
        res["json_rutas_que_difieren"] = [k for k in sorted(set(ra) | set(rb)) if ra.get(k) != rb.get(k)]
    for ok, p in ((res["json_igual_al_de_a3_sin_cuentas"], sj), (res["consola_igual_a_la_de_a3_sin_cuentas"], sc)):
        if not ok:
            p.rename(p.with_name("NO_ABRIR_" + p.name))
    res["salidas"] = {p.name: sha(p) for p in sorted(a.salida.iterdir()) if p.name != "resumen_sin_cuentas_t3.json"}
    res["veredicto_del_selftest"] = (json.loads(sj.read_text(encoding="utf-8")).get("veredicto")
                                     if res["json_igual_al_de_a3_sin_cuentas"] else "no se lee: el JSON va a un NO_ABRIR_")
    (a.salida / "resumen_sin_cuentas_t3.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))
    return 0 if res["json_igual_al_de_a3_sin_cuentas"] and res["consola_igual_a_la_de_a3_sin_cuentas"] else 1


if __name__ == "__main__":
    sys.exit(main())
