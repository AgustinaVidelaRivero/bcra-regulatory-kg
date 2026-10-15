"""Re-sellado único de la tanda 0 (mandato firmado el 15/10/2026, 67fe5b14; decisión 1): los cuatro manifiestos nuevos en
data/experiment/reextraccion_v2/manifiestos/, uno por grafo, como copias de su manifiesto r2b de hoy con `nombre` (con el
sufijo _rs1) y `descripcion` nuevos y nada más (el patrón de SC1.1 de U-SINCOLA-T0). Antes de escribir verifica que la
re-serialización de cada original es byte a byte igual al archivo (indent=1, ensure_ascii=False y salto final), y después
que el nuevo difiere del original solo en esas dos claves. No pisa un archivo existente.
Uso: python -I -B manifiestos_rs1.py <raiz>   (la copia primero; el repo recibe los mismos bytes)
"""
import json
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
M = RAIZ / "data/experiment/reextraccion_v2/manifiestos"
BASES = ["tanda0_ens_diez_r2b", "tanda0_ens_desarrollo_r2b", "tanda0_ens_diez_r2b_sincola",
         "tanda0_ens_desarrollo_r2b_sincola"]


def descripcion(base: str, heredada: str) -> str:
    sin_cola = base.endswith("_sincola")
    return (f"Re-sellado único de los grafos r2b de la tanda 0 (mandato firmado el 15/10/2026, 67fe5b14; decisión 1 de su "
            f"§8): copia de {base}.json con `nombre` y `descripcion` nuevos y nada más. El ensamblado corre con el código de "
            f"U-OMISIONES-COD (ded41d50) sobre las salidas de E1 y E3 de la tanda 0 tal como las deja R0 (1d690df3 y "
            f"2d0f5277)"
            + (", con --sin-cola: sin las unidades con estado cola_humana* como última versión en "
               "corpus_tanda0/salida_r2b/*/finales.jsonl después de R0" if sin_cola else "")
            + ". Los sellos de abajo siguen siendo los heredados, porque nada más cambia. Descripción heredada del "
              "original: " + heredada)


def main() -> int:
    for base in BASES:
        p = M / f"{base}.json"
        raw = p.read_text(encoding="utf-8")
        o = json.loads(raw)
        assert json.dumps(o, ensure_ascii=False, indent=1) + "\n" == raw, f"{p.name} no se re-serializa byte a byte"
        assert o["nombre"] == base, f"{p.name}: nombre {o['nombre']}"
        nuevo = dict(o)
        nuevo["nombre"] = base + "_rs1"
        nuevo["descripcion"] = descripcion(base, o["descripcion"])
        assert list(nuevo) == list(o), "el orden de las claves cambió"
        assert {k for k in o if o[k] != nuevo[k]} == {"nombre", "descripcion"}
        q = M / f"{base}_rs1.json"
        assert not q.exists(), f"{q} ya existe"
        q.write_text(json.dumps(nuevo, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print("escrito", q.relative_to(RAIZ))
    return 0


if __name__ == "__main__":
    sys.exit(main())
