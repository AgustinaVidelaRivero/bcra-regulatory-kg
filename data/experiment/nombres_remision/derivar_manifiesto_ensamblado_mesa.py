"""Deriva un manifiesto de ensamblado a partir de un manifiesto de extracción, con los `nombres_remision` de la regla y nada más
(mesa, §132, 16/10/2026; decisión de la autora del 16/10/2026, registro de decisiones, §19). USD 0. Solo lee; escribe la salida que se
le pide, que no tiene que estar en el repo hasta que la suba un commit.

Uso: python3 -I -B derivar_manifiesto_ensamblado_mesa.py <raíz> <manifiesto de extracción> <nombre nuevo> <salida.json>
         --contraste <contraste.json> --corpus <nombre del corpus en el contraste> [--sin-cola]

Qué hace:
  - copia el manifiesto de extracción, con `nombre` y `descripcion` nuevos y, en cada TO, `nombres_remision` de la regla aplicada a su
    título oficial del inventario (`inventario_tos.csv`; los cinco de desarrollo, de `inventario_resumen.json`). Como en la tanda 0
    (`tanda0_ens_diez_r2b_rs1.json` es una copia de `tanda0_10tos_r2b.json` con `nombre` y `descripcion` nuevos), nada más cambia;
  - la regla es `regla_nombres_remision_v2_mesa.py`. La variante con la raya (`regla_nombres_remision_v2_con_raya_mesa.py`) se usa solo si
    el contraste de esa variante contra los 157 títulos del inventario, con los TOs de ese ensamblado (`--contraste`, salida de
    `contrastar_con_inventario_completo_mesa.py` sobre la medición de la variante; `--corpus`), da 0 resoluciones distintas de la
    referencia. Es la condición que decidió la autora;
  - frena si el corpus del contraste no tiene exactamente los TOs del manifiesto.
El manifiesto de extracción no se toca: el lanzador de la extracción lo controla por su sha256.
"""
import csv
import hashlib
import importlib.util
import json
import sys
from pathlib import Path

RAIZ, MAN, NOMBRE, OUT = Path(sys.argv[1]), Path(sys.argv[2]), sys.argv[3], Path(sys.argv[4])
CONTRASTE = Path(sys.argv[sys.argv.index("--contraste") + 1])
CORPUS = sys.argv[sys.argv.index("--corpus") + 1]
SIN_COLA = "--sin-cola" in sys.argv
AQUI = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()  # noqa: E731


def cargar(nombre: str):
    spec = importlib.util.spec_from_file_location(nombre, AQUI / f"{nombre}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


m = json.loads(MAN.read_text(encoding="utf-8"))
ids = [t["id"] for t in m["tos"]]
c = json.loads(CONTRASTE.read_text(encoding="utf-8"))
medicion = json.loads((AQUI / "medicion" / "medicion_final_regla_nombres_remision_v2_con_raya_mesa.json").read_text(encoding="utf-8"))
if sorted(medicion["corpus"][CORPUS]["tos"]) != sorted(ids):
    raise SystemExit(f"FRENO: el corpus {CORPUS} del contraste no tiene los TOs del manifiesto")
distintas = len(c[CORPUS]["regla"]["distintas_de_la_referencia"])
con_raya = distintas == 0
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
    f"{distintas} (corpus «{CORPUS}» de {CONTRASTE.name}), así que {'entra' if con_raya else 'no entra'}. Nada más cambia.")
for t in m["tos"]:
    t["nombres_remision"] = regla.nombres(oficial[t["id"]])
OUT.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"regla": nombre_regla, "distintas_con_la_raya": distintas, "con_raya": con_raya,
                  "tos_con_nombres": sum(1 for t in m["tos"] if t["nombres_remision"]), "tos": len(m["tos"])}, ensure_ascii=False))
