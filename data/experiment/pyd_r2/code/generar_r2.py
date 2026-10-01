"""
generar_r2.py — U-PYD: genera el tool schema de E1 y los enums del perfil r2
desde `modelos_r2` y el catálogo r2 (bd2122d).

Escribe solo en data/experiment/pyd_r2/generados/:
  - tool_schema_r2.json (nombre, descripción e input_schema de SalidaE1R2);
  - enums_r2.json (listas cerradas, matriz, claves por tipo, sujeto_id);
  - manifest_generados_r2.json (sha256 de cada archivo, de la política y de
    los módulos de los que sale).
Salida determinística, sin fechas ni rutas absolutas: dos corridas dan los
mismos bytes.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/generar_r2.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import modelos_r2 as M  # noqa: E402

GENERADOS = M.PYD_R2 / "generados"
POLITICA = M.PYD_R2 / "politica_campos_r2.json"


def serializar(obj) -> bytes:
    return (json.dumps(obj, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def contenidos() -> dict[str, bytes]:
    return {"tool_schema_r2.json": serializar(M.tool_schema_e1_r2()),
            "enums_r2.json": serializar(M.enums_r2())}


def manifiesto(cont: dict[str, bytes]) -> bytes:
    rel = lambda p: str(p.relative_to(M.REPO))  # noqa: E731
    return serializar({
        "generador": rel(AQUI / "generar_r2.py"),
        "modelos": {"ruta": rel(AQUI / "modelos_r2.py"), "sha256": M.sha256_archivo(AQUI / "modelos_r2.py")},
        "politica": {"ruta": rel(POLITICA), "sha256": M.sha256_archivo(POLITICA)},
        "catalogo_r2": {"ruta": rel(M.CATALOGO_R2), "commit": M.CATALOGO_R2_COMMIT,
                        "sha256": M.CATALOGO_R2_SHA256},
        "archivos": {k: hashlib.sha256(v).hexdigest() for k, v in cont.items()},
    })


def main() -> None:
    GENERADOS.mkdir(parents=True, exist_ok=True)
    cont = contenidos()
    cont_man = dict(cont)
    cont_man["manifest_generados_r2.json"] = manifiesto(cont)
    for nombre, b in cont_man.items():
        (GENERADOS / nombre).write_bytes(b)
        print(f"{hashlib.sha256(b).hexdigest()}  {GENERADOS.relative_to(M.REPO) / nombre}")


if __name__ == "__main__":
    main()
