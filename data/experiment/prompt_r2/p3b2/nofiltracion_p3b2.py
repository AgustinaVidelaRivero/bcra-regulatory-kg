"""
nofiltracion_p3b2.py — U-PROMPT-R2, P3b-2 (USD 0): la no-filtración de P3b-1 (p3b/nofiltracion_p3b.py, misma regla y
misma población, sin editarlo) re-corrida sobre los textos implementados:
  - el prefijo re-congelado (prompt_r2b.PREFIJO_SISTEMA_R2B) contra el de P2 (PREFIJO_SISTEMA_R2B_P2): el script de
    P3b-1 toma el viejo de prompt_r2b.PREFIJO_SISTEMA_R2B, que tras el re-congelado es el nuevo; acá se lo apunta al
    de P2 antes de correrlo;
  - los literales tomados del código: las líneas del mensaje de E1 (g, h y la del recorte de E0), la NOTA de E3 (i) y
    el aviso del reintento. Se controla que los cuatro de P3b-1 sean los del borrador aprobado.
Escribe solo en --salida. Sobre una copia del repo (regla l).

Uso (desde la raíz de la copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3b2/nofiltracion_p3b2.py --salida DIR
"""
from __future__ import annotations

import argparse
import runpy
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador"):
    sys.path.insert(0, str(REX / sub))
import prompt_r2b as P  # noqa: E402
import prompt_e3  # noqa: E402
import ratchet_e3  # noqa: E402

P3B = AQUI.parent / "p3b"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    lit = [P.LINEA_ITEM.format(tipo="", unidad="", cierres=P.CIERRES), P.LINEA_MINI_MITAD,
           prompt_e3.NOTA_E3_OMISIONES, ratchet_e3.AVISO_NOTA_REINTENTO]
    aprobados = (P3B / "salida" / "literales_mensaje_p3b.txt").read_text(encoding="utf-8")
    if "\n".join(lit) + "\n" != aprobados:
        raise SystemExit("los literales implementados no son los del borrador aprobado de P3b-1")
    (sal / "prefijo_r2b_p3b2.txt").write_text(P.PREFIJO_SISTEMA_R2B, encoding="utf-8")
    (sal / "literales_p3b2.txt").write_text("\n".join(lit[:2] + [P.LINEA_RECORTE] + lit[2:]) + "\n", encoding="utf-8")
    P.PREFIJO_SISTEMA_R2B = P.PREFIJO_SISTEMA_R2B_P2      # el «viejo» de la regla: el prefijo de P2
    sys.argv = [str(P3B / "nofiltracion_p3b.py"), str(sal / "prefijo_r2b_p3b2.txt"), str(sal / "literales_p3b2.txt"),
                str(sal / "nofiltracion_p3b2.json")]
    runpy.run_path(str(P3B / "nofiltracion_p3b.py"), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
