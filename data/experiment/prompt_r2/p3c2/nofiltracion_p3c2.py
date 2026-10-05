"""
nofiltracion_p3c2.py — U-PROMPT-R2, P3c-2 (USD 0): la no-filtración de P3c-1 (p3c/nofiltracion_p3c.py, misma regla y
misma población, sin editarlo) re-corrida sobre el texto implementado:
  - el prefijo re-congelado (prompt_r2b.PREFIJO_SISTEMA_R2B) contra el de P3b-2 (PREFIJO_SISTEMA_R2B_P3B): el script de
    P3c-1 toma el viejo de prompt_r2b.PREFIJO_SISTEMA_R2B, que tras el re-congelado es el nuevo; acá se lo apunta al de
    P3b-2 antes de correrlo, y la línea de alcance vieja (la de P1) a la de antes del punto e;
  - los literales, tomados del código: la línea de alcance (prompt_r2b.LINEA_ALCANCE), la NOTA de las omisiones y la
    oración nueva de la NOTA del encabezado de lista (prompt_e3). Se controla que sean los del borrador aprobado de
    P3c-1 (p3c/salida/literales_mensaje_p3c.txt).
Escribe solo en --salida. Sobre una copia del repo (regla l).

Uso (desde la raíz de la copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c2/nofiltracion_p3c2.py --salida DIR
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
sys.path.insert(0, str(AQUI.parent / "p1"))
import prompt_r2b as P  # noqa: E402
import prompt_e3  # noqa: E402
import mensaje_r2_borrador as MB  # noqa: E402  (la línea de alcance de P1, la de antes del punto e)

P3C = AQUI.parent / "p3c"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    sal.mkdir(parents=True, exist_ok=True)
    encabezado_nuevo = prompt_e3.NOTA_E3_ENCABEZADO_LISTA[prompt_e3.NOTA_E3_ENCABEZADO_LISTA.index("Sí es faltante"):]
    lit = [P.LINEA_ALCANCE.format(sug=""), prompt_e3.NOTA_E3_OMISIONES, encabezado_nuevo]
    aprobados = (P3C / "salida" / "literales_mensaje_p3c.txt").read_text(encoding="utf-8")
    if "\n".join(lit) + "\n" != aprobados:
        raise SystemExit("los literales implementados no son los del borrador aprobado de P3c-1")
    (sal / "prefijo_r2b_p3c2.txt").write_text(P.PREFIJO_SISTEMA_R2B, encoding="utf-8")
    (sal / "literales_p3c2.txt").write_text("\n".join(lit) + "\n", encoding="utf-8")
    P.PREFIJO_SISTEMA_R2B = P.PREFIJO_SISTEMA_R2B_P3B     # el «viejo» de la regla: el prefijo de P3b-2
    P.linea_alcance = MB.linea_alcance                    # y la línea de alcance de antes del punto e
    sys.argv = [str(P3C / "nofiltracion_p3c.py"), str(sal / "prefijo_r2b_p3c2.txt"), str(sal / "literales_p3c2.txt"),
                str(AQUI.parent / "p4" / "salida" / "muestra_p4.json"), str(sal / "nofiltracion_p3c2.json")]
    runpy.run_path(str(P3C / "nofiltracion_p3c.py"), run_name="__main__")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
