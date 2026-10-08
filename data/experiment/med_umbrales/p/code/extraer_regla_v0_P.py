"""
extraer_regla_v0_P.py — U-MED-UMBRALES, etapa P, tramo P-a, punto 9: la regla de calificación v0 es el §2 de la
enmienda firmada (a0f9815), sin cambios. Copia el §2 (desde «## 2. Unidad y campos» hasta antes de «## 3.») del archivo
del commit de la firma, que en la copia del repo es docs/enmienda1_…_umbrales.md (preparar_espejo_P.py lo toma con
`git show a0f9815:…`), y escribe --salida/regla_calificacion_v0.md con una cabecera y el sha256 del texto copiado.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/med_umbrales/p/code/extraer_regla_v0_P.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_P as C  # noqa: E402


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    lineas = (C.REPO / C.ENMIENDA).read_text(encoding="utf-8").split("\n")
    firmado = "\n".join(lineas[:lineas.index("## Firma")]) + "\n"
    if hashlib.sha256(firmado.encode("utf-8")).hexdigest() != C.SHA_TEXTO_FIRMADO:
        raise SystemExit("la enmienda de la copia no es la del commit de la firma")
    ini = lineas.index("## 2. Unidad y campos")
    fin = next(i for i in range(ini + 1, len(lineas)) if lineas[i].startswith("## 3."))
    seccion = "\n".join(lineas[ini:fin]).rstrip("\n") + "\n"
    s = hashlib.sha256(seccion.encode("utf-8")).hexdigest()
    cab = ["# Regla de calificación v0 (U-MED-UMBRALES, etapa P)", "",
           f"Es el §2 de la enmienda 1 al pre-registro de tripletas, FIRMADA en `{C.COMMIT_FIRMA}` "
           f"(`{C.ENMIENDA}`, líneas {ini + 1} a {fin} del archivo de ese commit), sin cambios. sha256 del texto copiado "
           f"(desde «## 2. Unidad y campos» hasta la línea anterior a «## 3.», con salto final): `{s}`.", "",
           "El piloto la ajusta en el FRENO del lote 1 (v1) y la sella al cerrar el piloto (§5.4); esta versión no se "
           "edita: las versiones siguientes van en archivos aparte.", "", "---", ""]
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "regla_calificacion_v0.md").write_text("\n".join(cab) + seccion, encoding="utf-8")
    print(s, ini + 1, fin)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
