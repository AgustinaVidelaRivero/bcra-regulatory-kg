"""Corre el MISMO driver en seco sobre los 5 TOs del subset congelado.

Sirve para dos cosas: (i) verificar que el driver de escalado_prep reproduce
byte a byte los chunks sellados de E0 (salida_enm01), o sea que invoca E0 sin
alterarlo; (ii) fijar la banda de referencia de las señales de diagnóstico
sobre TOs que el pipeline YA digirió, contra la cual se juzga a los TOs nuevos.

Lee el subset en modo solo lectura. Escribe únicamente bajo
escalado_prep/e0_dry_subset_ref/ y escalado_prep/referencia_subset.json.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import correr_e0_seco as D  # noqa: E402

PREP = D.PREP
SUBSET = D.REPO / "data" / "experiment" / "subset"
REF_SELLADA = D.E0_DIR / "salida_enm01"

ARCHIVOS = {
    "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
    "cla": "TO_clasificacion_deudores_actual.pdf",
    "ric": "TO_regimen_informativo_contable_mensual_actual.pdf",
    "cap": "TO_capitales_minimos_actual.pdf",
    "ext": "TO_exterior_cambios_actual.pdf",
}


def sha_canon(obj) -> str:
    return hashlib.sha256(
        json.dumps(obj, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


def main() -> None:
    D.SALIDA = PREP / "e0_dry_subset_ref"
    D.SALIDA.mkdir(parents=True, exist_ok=True)
    out = {}
    for to, arch in ARCHIVOS.items():
        r = D.correr_uno(to, SUBSET / arch)
        mios = json.loads((D.SALIDA / to / f"chunks_{to}.json").read_text(encoding="utf-8"))
        sellados = json.loads((REF_SELLADA / f"chunks_{to}.json").read_text(encoding="utf-8"))
        r["paridad_con_salida_enm01"] = {
            "n_chunks_driver": len(mios),
            "n_chunks_sellados": len(sellados),
            "sha256_canonico_driver": sha_canon(mios),
            "sha256_canonico_sellado": sha_canon(sellados),
            "identicos": sha_canon(mios) == sha_canon(sellados),
        }
        out[to] = r
        p = r["paridad_con_salida_enm01"]
        print(f"{to:4s} chunks={p['n_chunks_driver']:4d} identico_a_sellado={p['identicos']}")

    (PREP / "referencia_subset.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print("paridad total:", all(v["paridad_con_salida_enm01"]["identicos"] for v in out.values()))


if __name__ == "__main__":
    main()
