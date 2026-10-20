"""B6.1, tanda final, T3, punto 4 (la suite): las entradas nuevas de scripts/regression_kg_esperado.json, con el patrón de
data/experiment/tanda1/t3/scripts/editar_fixture_t3.py, sobre una raíz (la copia del repo; el repo recibe después los mismos bytes).
USD 0, sin API.

SOLO ocho entradas nuevas al final de `estado_esperado`, copias de la entrada sellada del grafo anterior (expectativas sin cambiar
ninguna), con el kg, el kg_sha256 y el registro_dir del ensamblado nuevo y un rótulo propio. El grafo anterior es el de la tanda 1 del
mismo tipo (docs/protocolo_entre_tandas.md:43-46):
  - KG-TandaFinal-r2b, KG-TandaFinal-Tramo1-r2b                     ← KG-Tanda1-Veinte-r2b
  - KG-TandaFinal-r2b-sincola, KG-TandaFinal-Tramo1-r2b-sincola     ← KG-Tanda1-Veinte-r2b-sincola
  - KG-Acumulado-Tandas0y1yFinal-r2b, KG-Acumulado-Tandas0y1yTramo1-r2b                  ← KG-Acumulado-Tandas0y1-r2b
  - KG-Acumulado-Tandas0y1yFinal-r2b-sincola, KG-Acumulado-Tandas0y1yTramo1-r2b-sincola  ← KG-Acumulado-Tandas0y1-r2b-sincola
Control de que la elección no cambia nada: las expectativas (todas las claves salvo el rótulo, el kg, su sha256, el registro_dir, sus
notas y la evidencia) de esas cuatro entradas y de las dos de diez de la tanda 0 re-sellada son iguales; si no, frena.
Antes de escribir verifica que la re-serialización del archivo es byte a byte igual (indent=1, ensure_ascii=False) y, después, que las
entradas selladas quedan iguales (texto canónico de cada una) y en el mismo orden, y que lo nuevo son solo esas ocho claves.
Uso: python3 -I -B editar_fixture_tf.py <raiz>
"""
import copy
import hashlib
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
FIX = RAIZ / "scripts/regression_kg_esperado.json"
X = "data/experiment/reextraccion_v2/corpus_tanda_final"
A = "data/experiment/tanda_final/t3/acumulado"
# (ruta del ensamblado, nombre en la suite, entrada sellada del grafo anterior, sin cola, qué es)
NUEVAS = [
    (f"{X}/ens_98_r2b", "KG-TandaFinal-r2b", "KG-Tanda1-Veinte-r2b", False, "el grafo completo de la tanda final (sus 98 TOs solos)"),
    (f"{X}/ens_98_r2b_sincola", "KG-TandaFinal-r2b-sincola", "KG-Tanda1-Veinte-r2b-sincola", True,
     "el grafo de la tanda final sin la cola humana"),
    (f"{X}/ens_tramo1_r2b", "KG-TandaFinal-Tramo1-r2b", "KG-Tanda1-Veinte-r2b", False,
     "el grafo completo del tramo 1 de la tanda final (sus 30 TOs solos)"),
    (f"{X}/ens_tramo1_r2b_sincola", "KG-TandaFinal-Tramo1-r2b-sincola", "KG-Tanda1-Veinte-r2b-sincola", True,
     "el grafo del tramo 1 de la tanda final sin la cola humana"),
    (f"{A}/ens_128_r2b", "KG-Acumulado-Tandas0y1yFinal-r2b", "KG-Acumulado-Tandas0y1-r2b", False,
     "el acumulado de las tandas 0, 1 y final (128 TOs), completo"),
    (f"{A}/ens_128_r2b_sincola", "KG-Acumulado-Tandas0y1yFinal-r2b-sincola", "KG-Acumulado-Tandas0y1-r2b-sincola", True,
     "el acumulado de las tandas 0, 1 y final (128 TOs), sin la cola humana"),
    (f"{A}/ens_60_tramo1_r2b", "KG-Acumulado-Tandas0y1yTramo1-r2b", "KG-Acumulado-Tandas0y1-r2b", False,
     "el acumulado de las tandas 0 y 1 con el tramo 1 de la tanda final (60 TOs), completo"),
    (f"{A}/ens_60_tramo1_r2b_sincola", "KG-Acumulado-Tandas0y1yTramo1-r2b-sincola", "KG-Acumulado-Tandas0y1-r2b-sincola", True,
     "el acumulado de las tandas 0 y 1 con el tramo 1 de la tanda final (60 TOs), sin la cola humana"),
]
ORIGEN = ("tanda final de B6.1, T3 (pre-registro firmado en 4de7f2a7, §2 y §7): ensamblado con el código de la release r2 (el de la "
          "tanda 1) sobre las salidas de E1 y E3 de la tanda final de T2")
NO_EXPECTATIVA = {"_rotulo", "kg", "kg_sha256", "_kg_sha256", "registro_dir", "_registro_dir", "evidencia"}
COMPARADAS = ("KG-Tanda1-Veinte-r2b", "KG-Tanda1-Veinte-r2b-sincola", "KG-Acumulado-Tandas0y1-r2b", "KG-Acumulado-Tandas0y1-r2b-sincola",
              "KG-Tanda0-Diez-r2b-rs1", "KG-Tanda0-Diez-r2b-sincola-rs1")


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


raw = FIX.read_text(encoding="utf-8")
fx = json.loads(raw)
assert json.dumps(fx, ensure_ascii=False, indent=1) + "\n" == raw, "la fixture no se re-serializa byte a byte"
ee = fx["estado_esperado"]
expect = {k: json.dumps({a: b for a, b in ee[k].items() if a not in NO_EXPECTATIVA}, ensure_ascii=False, sort_keys=True) for k in COMPARADAS}
if len(set(expect.values())) != 1:
    raise SystemExit(f"FRENO: las expectativas de {COMPARADAS} no son iguales")
orden_antes = list(ee)
canon_antes = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in ee.items()}
otras_antes = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in fx.items() if k != "estado_esperado"}
for carpeta, suite, base, sin_cola, que in NUEVAS:
    assert suite not in ee, f"{suite} ya existe"
    kg = RAIZ / carpeta / "r2" / "kg.json"
    e = copy.deepcopy(ee[base])
    e_nuevo = {
        "_rotulo": (f"TANDA FINAL DE B6.1: {que}, {ORIGEN}" + (" (ensamblar_tanda0.py --sin-cola)" if sin_cola else "")
                    + f". Las expectativas son las de la entrada sellada del grafo anterior, {base}, sin cambiar ninguna. Rótulo "
                    + "heredado: " + e["_rotulo"]),
        "kg": f"{carpeta}/r2/kg.json",
        "kg_sha256": sha(kg),
        "_kg_sha256": ("sha256 del ensamblado: dos corridas en procesos distintos, byte a byte, sobre una copia del repo; el archivo "
                       "del repo es byte a byte el de la copia (si pasa de 100 MB, va comprimido con scripts/kg_gz.py y manda este "
                       "sha256, el del kg.json sin comprimir)."),
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
otras_despues = {k: json.dumps(v, ensure_ascii=False, sort_keys=True) for k, v in fx.items() if k != "estado_esperado"}
assert canon_antes == canon_despues, "una entrada sellada cambió"
assert otras_antes == otras_despues, "cambió algo fuera de estado_esperado"
assert list(ee)[:len(orden_antes)] == orden_antes and list(ee)[len(orden_antes):] == [s for _, s, _, _, _ in NUEVAS], "el orden cambió"
FIX.write_text(json.dumps(fx, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({"fixture_sha256": sha(FIX), "entradas_antes": len(orden_antes), "entradas_despues": len(ee),
                  "entradas_nuevas": {s: ee[s]["kg_sha256"] for _, s, _, _, _ in NUEVAS},
                  "expectativas_iguales_en": list(COMPARADAS), "selladas_iguales": True}, ensure_ascii=False, indent=1))
