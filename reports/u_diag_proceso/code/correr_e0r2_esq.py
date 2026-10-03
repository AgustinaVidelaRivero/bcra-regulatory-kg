"""Corrida de control U-DIAG-PROCESO: E0 e0-r2 sobre los diez TOs de ESQ-2, en el espejo
copiado del scratchpad (regla l). Sin API. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B correr_e0r2_esq.py <espejo> <salida>
"""
import sys
from pathlib import Path

espejo = Path(sys.argv[1]).resolve()
salida = Path(sys.argv[2]).resolve()
sys.dont_write_bytecode = True
sys.path.insert(0, str(espejo / "data/experiment/reextraccion_v2/e0_chunking"))
import correr_e0  # noqa: E402

assert Path(correr_e0.__file__).resolve().is_relative_to(espejo), correr_e0.__file__

TOS = ["actgar", "adrei", "ayccef", "cryl", "ctacor", "expaef", "lavdin", "opefci", "prevmi", "traval"]
PDFS = espejo / "data/experiment/escalado_prep/pdfs"


class Man:
    ids = TOS
    tiene_oraculo = False
    mapa_territorio = None

    @staticmethod
    def archivo_de(t):
        return f"{t}.pdf"

    @staticmethod
    def pdf_de(t):
        return PDFS / f"{t}.pdf"


conteos = correr_e0.correr(salida, manifiesto=Man, version_e0="e0-r2")
print({t: conteos.get(t, {}).get("chunks") if isinstance(conteos.get(t), dict) else conteos.get(t)
       for t in TOS})
