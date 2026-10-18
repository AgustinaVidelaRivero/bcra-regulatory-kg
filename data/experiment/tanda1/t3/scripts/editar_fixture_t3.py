"""B6.1, tanda 1, T3, punto 4 (la suite): las entradas nuevas de scripts/regression_kg_esperado.json, con el patrón de
data/experiment/resellado_t0/scripts/editar_fixture_grafos_rs1.py, sobre una raíz (la copia del repo; el repo recibe después los
mismos bytes). USD 0, sin API.

SOLO cuatro entradas nuevas al final de `estado_esperado`, copias de la entrada sellada del grafo anterior (expectativas sin cambiar
ninguna), con el kg, el kg_sha256 y el registro_dir del ensamblado nuevo y un rótulo propio:
  - KG-Tanda1-Veinte-r2b                  ← KG-Tanda0-Diez-r2b-rs1
  - KG-Tanda1-Veinte-r2b-sincola          ← KG-Tanda0-Diez-r2b-sincola-rs1
  - KG-Acumulado-Tandas0y1-r2b            ← KG-Tanda0-Diez-r2b-rs1
  - KG-Acumulado-Tandas0y1-r2b-sincola    ← KG-Tanda0-Diez-r2b-sincola-rs1
El grafo anterior de los cuatro es el de la tanda 0 re-sellado (el de diez, completo o sin la cola): la suite se mide contra él
(docs/protocolo_entre_tandas.md:43-46). Antes de escribir verifica que la re-serialización del archivo es byte a byte igual (indent=1,
ensure_ascii=False) y, después, que las entradas selladas quedan iguales (texto canónico de cada una).
Uso: python3 -I -B editar_fixture_t3.py <raiz>
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
FIX = RAIZ / "scripts/regression_kg_esperado.json"
# (ruta del ensamblado, nombre en la suite, entrada sellada del grafo anterior, sin cola, qué es)
NUEVAS = [
    ("data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b", "KG-Tanda1-Veinte-r2b", "KG-Tanda0-Diez-r2b-rs1", False,
     "el grafo completo de la tanda 1 (sus 20 TOs solos)"),
    ("data/experiment/reextraccion_v2/corpus_tanda1/ens_veinte_r2b_sincola", "KG-Tanda1-Veinte-r2b-sincola",
     "KG-Tanda0-Diez-r2b-sincola-rs1", True, "el grafo de la tanda 1 sin la cola humana, el grafo evaluado (enmienda 5)"),
    ("data/experiment/tanda1/t3/acumulado/ens_treinta_r2b", "KG-Acumulado-Tandas0y1-r2b", "KG-Tanda0-Diez-r2b-rs1", False,
     "el acumulado de las tandas 0 y 1 (30 TOs), completo"),
    ("data/experiment/tanda1/t3/acumulado/ens_treinta_r2b_sincola", "KG-Acumulado-Tandas0y1-r2b-sincola",
     "KG-Tanda0-Diez-r2b-sincola-rs1", True, "el acumulado de las tandas 0 y 1 (30 TOs), sin la cola humana"),
]
ORIGEN = ("tanda 1 de B6.1, T3 (pre-registro firmado en 95b18217, §5.1): ensamblado con el código de la release r2 (el del re-sellado "
          "de la tanda 0) sobre las salidas de E1 y E3 de la tanda 1 de T2")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


raw = FIX.read_text(encoding="utf-8")
fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + "\n" == raw, "la fixture no se re-serializa byte a byte"
ee = fx["estado_esperado"]
canon_antes = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in ee.items()}
for carpeta, suite, base, sin_cola, que in NUEVAS:
    assert suite not in ee, f"{suite} ya existe"
    kg = RAIZ / carpeta / "r2" / "kg.json"
    e = copy.deepcopy(ee[base])
    e_nuevo = {
        "_rotulo": (f"TANDA 1 DE B6.1: {que}, {ORIGEN}" + (" (ensamblar_tanda0.py --sin-cola)" if sin_cola else "")
                    + f". Las expectativas son las de la entrada sellada del grafo anterior, {base}, sin cambiar ninguna. Rótulo "
                    + "heredado: " + e["_rotulo"]),
        "kg": f"{carpeta}/r2/kg.json",
        "kg_sha256": sha(kg),
        "_kg_sha256": ("sha256 del ensamblado: dos corridas en procesos distintos, byte a byte, sobre una copia del repo; el archivo "
                       "del repo es byte a byte el de la copia."),
        "registro_dir": f"{carpeta}/r2",
        "_registro_dir": ("el registro del ensamblado nuevo (no_mapeados_sujetos.jsonl, omisiones.jsonl, reporte_ensamblado_r2.json): "
                          "se pasa a la suite con --registro-dir."),
    }
    for k, v in e.items():
        if k not in e_nuevo:
            e_nuevo[k] = v
    e_nuevo["evidencia"] = f"Expectativas heredadas de {base}. " + e["evidencia"]
    ee[suite] = e_nuevo
canon_despues = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in ee.items() if k in canon_antes}
assert canon_antes == canon_despues, "una entrada sellada cambió"
FIX.write_text(json.dumps(fx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"fixture_sha256": sha(FIX), "entradas_nuevas": {s: ee[s]["kg_sha256"] for _, s, _, _, _ in NUEVAS},
                  "selladas_iguales": True}, ensure_ascii=False))
