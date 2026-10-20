"""
derivar_manifiesto_ensamblado_tf.py — B6.1, tanda final, T3, punto 3: un manifiesto de ensamblado cuando el corpus no está en la medición
de `data/experiment/nombres_remision/` (el derivador de la mesa, `derivar_manifiesto_ensamblado_mesa.py`, frena si el corpus de su contraste
no tiene exactamente los TOs del manifiesto). USD 0. Solo lee <raíz>; escribe <salida.json>.

Hace lo mismo que el derivador de la mesa, línea por línea (copia el manifiesto de extracción, con `nombre` y `descripcion` nuevos y, en
cada TO, los `nombres_remision` de la regla aplicada a su título oficial del inventario), con una sola diferencia: la variante de la
regla no sale de un contraste de la medición, sino de la decisión que se le pasa, con su fuente, y queda escrita en la `descripcion`:
  - el acumulado de las tandas 0 y 1 con el tramo 1 (60 TOs): la regla v2 sin la raya, por la enmienda 9, punto 8 (`756a0394:78-84`), que
    da la medición de la mesa del 17/10/2026: con la raya, 23 resoluciones distintas de la referencia, así que la raya no entra;
  - el tramo 1 solo (30 TOs; solo para la prueba de que el grafo no cambia): la regla v2 con la raya, por el mismo punto: 0 distintas, «la
    raya entra, sin cambiar ninguna resolución».
Uso: python3 -I -B derivar_manifiesto_ensamblado_tf.py <raíz> <manifiesto de extracción> <nombre nuevo> <salida.json>
       --regla v2|v2_con_raya --distintas <n> --fuente <texto> [--sin-cola]
"""
import argparse
import csv
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
ap = argparse.ArgumentParser()
ap.add_argument("raiz", type=Path)
ap.add_argument("manifiesto", type=Path)
ap.add_argument("nombre")
ap.add_argument("salida", type=Path)
ap.add_argument("--regla", choices=("v2", "v2_con_raya"), required=True)
ap.add_argument("--distintas", type=int, required=True)
ap.add_argument("--fuente", required=True)
ap.add_argument("--sin-cola", action="store_true")
a = ap.parse_args()
RAIZ, MAN, NOMBRE, OUT, SIN_COLA = a.raiz.resolve(), a.manifiesto, a.nombre, a.salida, a.sin_cola
AQUI = RAIZ / "data/experiment/nombres_remision"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731


def cargar(nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, AQUI / f"{nombre}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = json.loads(MAN.read_text(encoding="utf-8"))
con_raya = a.regla == "v2_con_raya"
if con_raya != (a.distintas == 0):
    raise SystemExit("FRENO: la regla no sigue la condición de la §19 con las distintas que se le pasan")
nombre_regla = "regla_nombres_remision_v2_con_raya_mesa" if con_raya else "regla_nombres_remision_v2_mesa"
regla = cargar(nombre_regla)
INV = RAIZ / "data/experiment/escalado_prep/inventario_tos.csv"
RES = RAIZ / "data/experiment/escalado_prep/inventario_resumen.json"
oficial = {r["id"]: r["titulo_oficial"] for r in csv.DictReader(INV.open(encoding="utf-8"))}
for x in json.loads(RES.read_text(encoding="utf-8"))["subset_excluido"]:
    oficial[x["id_interno"]] = x["titulo"]
m["nombre"] = NOMBRE
m["descripcion"] = (
    f"Manifiesto de ensamblado{' sin cola (el ensamblado corre sin la cola humana)' if SIN_COLA else ''}: copia de {MAN.name} "
    f"(sha256 {sha(MAN)[:8]}…) con `nombre` y `descripcion` nuevos y, en cada TO, `nombres_remision` derivados del título oficial del "
    f"inventario (inventario_tos.csv {sha(INV)[:8]}…) por la regla de data/experiment/nombres_remision/ (decisión de la autora del "
    f"16/10/2026, registro de decisiones, §19): {nombre_regla}.py (sha256 {sha(AQUI / (nombre_regla + '.py'))[:8]}…). La variante con "
    f"la raya entra solo si su contraste contra los 157 títulos, con los TOs de este ensamblado, da 0 resoluciones distintas: aquí da "
    f"{a.distintas} ({a.fuente}), así que {'entra' if con_raya else 'no entra'}. Nada más cambia. Lo derivó "
    f"data/experiment/tanda_final/t3/scripts/derivar_manifiesto_ensamblado_tf.py, porque la medición no tiene un corpus con estos TOs.")
for t in m["tos"]:
    t["nombres_remision"] = regla.nombres(oficial[t["id"]])
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"regla": nombre_regla, "distintas_con_la_raya": a.distintas, "con_raya": con_raya,
                  "tos_con_nombres": sum(1 for t in m["tos"] if t["nombres_remision"]), "tos": len(m["tos"])}, ensure_ascii=False))
