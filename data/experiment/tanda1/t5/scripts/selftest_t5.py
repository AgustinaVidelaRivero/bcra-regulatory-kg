"""B6.1, tanda 1, T5, punto 10: el selftest de claves de la tanda 0 (data/experiment/mantenimiento/code/selftest_clave_cache.py), tal cual,
sobre una copia del repo y dos veces. Controla que la tanda 1 no tocó las claves de la tanda 0; para la tanda 1 no se adapta.
  - Cada corrida: `<python> -B selftest_clave_cache.py --out <trabajo>/selftest_corrida_<k>.json`, con la copia como directorio de
    trabajo y PYTHONDONTWRITEBYTECODE=1, como dice su docstring. La consola va a <trabajo>/NO_ABRIR_consola_selftest_<k>.txt, que este
    script no abre: trae conteos.
  - A <salida.json> va solo el veredicto de cada bloque y el general, y si las dos corridas dan el mismo JSON byte a byte.
  - Los conteos (los anclajes enteros, cuántas variaciones y cuáles discrepan) y las dos salidas del selftest van a
    <trabajo>/NO_ABRIR_parte_selftest_t5.json, que el script no imprime.
Uso: python3 -I -B selftest_t5.py <copia> <python del venv> <trabajo> <salida.json>
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
COPIA, PY, TRABAJO, OUT = Path(sys.argv[1]).resolve(), sys.argv[2], Path(sys.argv[3]).resolve(), Path(sys.argv[4]).resolve()
assert not TRABAJO.exists()
TRABAJO.mkdir(parents=True)
assert not (COPIA / ".git").exists(), "la copia no tiene que ser un clon"
SELF = "data/experiment/mantenimiento/code/selftest_clave_cache.py"
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
salidas, rcs = [], []
for k in (1, 2):
    out = TRABAJO / f"selftest_corrida_{k}.json"
    with open(TRABAJO / f"NO_ABRIR_consola_selftest_{k}.txt", "w", encoding="utf-8") as fh:
        rcs.append(subprocess.run([PY, "-B", SELF, "--out", str(out)], cwd=COPIA, env=env, stdout=fh, stderr=subprocess.STDOUT).returncode)
    salidas.append(out)
b1, b2 = (p.read_bytes() for p in salidas)
r = json.loads(b1)
r2b = r["perfil_r2b"]


def ok_var(vs: list) -> str:
    return "OK" if all(v["ok"] for v in vs) else "FRENO"


inv = r["inventario_del_armado"]
inv2 = r2b["inventario_del_armado"]
veredictos = {
    "selftest": SELF, "sha256_del_selftest": hashlib.sha256((COPIA / SELF).read_bytes()).hexdigest(),
    "codigos_de_salida": rcs,
    "las_dos_corridas_dan_el_mismo_json_byte_a_byte": b1 == b2,
    "bloques": {
        "A, anclaje del perfil sellado (v3_b54), E1": r["anclaje"]["e1"]["estado"],
        "A, anclaje del perfil sellado (v3_b54), E3": r["anclaje"]["e3"]["estado"],
        "B, variaciones del perfil sellado": ok_var(r["variaciones"]),
        "inventario del armado del perfil sellado": "OK" if inv["control_reproduce_claves_del_padre"] and not inv["modulos_solo_codigo_cargados"] else "FRENO",
        "A', anclaje del perfil r2b, E1": r2b["anclaje"]["e1"]["estado"],
        "A', anclaje del perfil r2b, E3": r2b["anclaje"]["e3"]["estado"],
        "B', variaciones del perfil r2b": ok_var(r2b["variaciones"]),
        "inventario del armado del perfil r2b": "OK" if inv2["control_reproduce_claves_del_padre"]
        and not inv2["modulos_solo_codigo_cargados_al_armar"] else "FRENO",
        "C, contraste con la tabla de reprocesamiento": r["contraste_tabla"]["estado"],
    },
    "veredicto_general": r["veredicto"],
    "declarado": "es el selftest de la tanda 0, tal cual: controla que la tanda 1 no tocó sus claves; para la tanda 1 no se adaptó",
    "conteos": "en NO_ABRIR_conteos_t5.json",
}
OUT.write_text(json.dumps(veredictos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
parte = {"que_es": "los conteos del selftest de claves (los anclajes enteros, las variaciones y las discrepancias) y sus dos salidas",
         "anclaje_v3_b54": r["anclaje"], "anclaje_r2b": r2b["anclaje"],
         "variaciones": {"v3_b54": len(r["variaciones"]), "r2b": len(r2b["variaciones"]), "con_discrepancia": r["variaciones_con_discrepancia"]},
         "sha256_de_las_dos_salidas": [hashlib.sha256(b).hexdigest() for b in (b1, b2)],
         "salida_del_selftest": r}
(TRABAJO / "NO_ABRIR_parte_selftest_t5.json").write_text(json.dumps(parte, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
for p in salidas:
    p.unlink()
print(json.dumps(veredictos, ensure_ascii=False, indent=1))
