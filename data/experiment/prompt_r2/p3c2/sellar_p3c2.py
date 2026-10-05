"""
sellar_p3c2.py — U-PROMPT-R2, P3c-2 (USD 0): calcula los valores que se sellan en los candados de P3c-2, sobre el código
y los datos de la copia en la que corre (regla l). No escribe en el repo: imprime y guarda en --salida un JSON con los
valores, que se copian a mano a las constantes.

  - PARCHE_P3C_SHA256_ESPERADO: sha256 de e1_extractor/prompt_r2b_parche_p3c.json;
  - PREFIJO_SHA256_R2B_ESPERADO y PREFIJO_HASH_R2B_ESPERADO: el prefijo armado con los parches de P3b y P3c;
  - TABLAS_FORZADAS_SHA256_ESPERADO: sha256 de tablas_residuales_forzadas_r2b.json;
  - CANDADO_MENSAJE_JSON_SHA256_ESPERADO y MENSAJE_R2B_SHA256_ESPERADO: la fixture de E1 y el sha256 de sus mensajes;
  - CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO y MENSAJE_E3_SHA256_ESPERADO: la fixture de E3 y el de sus mensajes.

Para calcular un valor que el propio candado compara, el módulo se ejecuta desde su fuente con las comparaciones que
dependen de ese valor neutralizadas (en memoria, nunca en el archivo). Con --verificar, en cambio, importa los dos
módulos tal como están y controla que los valores sellados coincidan.

Uso (desde la raíz de una copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c2/sellar_p3c2.py --salida DIR [--verificar]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
import types
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
E1 = REPO / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"
E3 = REPO / "data" / "experiment" / "reextraccion_v2" / "e3_verificador"
for d in (E1, E3):
    sys.path.insert(0, str(d))


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def ejecutar(nombre: str, ruta: Path, cambios: list[tuple[str, str]]) -> types.ModuleType:
    src = ruta.read_text(encoding="utf-8")
    for a, b in cambios:
        if src.count(a) != 1:
            raise SystemExit(f"{nombre}: el fragmento a neutralizar aparece {src.count(a)} veces")
        src = src.replace(a, b)
    mod = types.ModuleType(nombre)
    mod.__file__ = str(ruta)
    sys.modules[nombre] = mod
    exec(compile(src, str(ruta), "exec"), mod.__dict__)
    return mod


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--verificar", action="store_true")
    a = ap.parse_args()
    sal = a.salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    v = {"PARCHE_P3C_SHA256_ESPERADO": sha(E1 / "prompt_r2b_parche_p3c.json"),
         "TABLAS_FORZADAS_SHA256_ESPERADO": sha(E1 / "tablas_residuales_forzadas_r2b.json"),
         "CANDADO_MENSAJE_JSON_SHA256_ESPERADO": sha(E1 / "candado_mensaje_r2b.json"),
         "CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO": sha(E3 / "candado_mensaje_e3.json")}
    if a.verificar:
        import prompt_r2b as R  # noqa: PLC0415 — con sus candados
        import prompt_e3  # noqa: PLC0415 — con los suyos
        res = {"prefijo_sha256": R.PREFIJO_SHA256_R2B, "prefijo_hash": R.PREFIJO_HASH_R2B,
               "prefijo_caracteres": len(R.PREFIJO_SISTEMA_R2B),
               "mensaje_r2b": R.sha256_mensajes(json.loads((E1 / "candado_mensaje_r2b.json").read_text())["chunks"]),
               "mensaje_e3": prompt_e3.sha256_mensajes_e3(json.loads((E3 / "candado_mensaje_e3.json").read_text())["casos"]),
               "constantes_iguales": {
                   k: getattr(R if hasattr(R, k) else prompt_e3, k) == val for k, val in v.items()},
               "importan_sin_frenar": True}
    else:
        R = ejecutar("prompt_r2b", E1 / "prompt_r2b.py", [
            ('PARCHE_P3C_SHA256_ESPERADO = "@@PARCHE_P3C@@"',
             f'PARCHE_P3C_SHA256_ESPERADO = "{v["PARCHE_P3C_SHA256_ESPERADO"]}"'),
            ('TABLAS_FORZADAS_SHA256_ESPERADO = "@@TABLAS@@"',
             f'TABLAS_FORZADAS_SHA256_ESPERADO = "{v["TABLAS_FORZADAS_SHA256_ESPERADO"]}"'),
            ('CANDADO_MENSAJE_JSON_SHA256_ESPERADO = "@@FIXTURE@@"',
             f'CANDADO_MENSAJE_JSON_SHA256_ESPERADO = "{v["CANDADO_MENSAJE_JSON_SHA256_ESPERADO"]}"'),
            ("if PREFIJO_SHA256_R2B != PREFIJO_SHA256_R2B_ESPERADO or PREFIJO_HASH_R2B != PREFIJO_HASH_R2B_ESPERADO:",
             "if False:"),
            ("\n_candado_mensaje()\n", "\n"),
        ])
        v["PREFIJO_SHA256_R2B_ESPERADO"] = R.PREFIJO_SHA256_R2B
        v["PREFIJO_HASH_R2B_ESPERADO"] = R.PREFIJO_HASH_R2B
        v["prefijo_caracteres"] = len(R.PREFIJO_SISTEMA_R2B)
        v["MENSAJE_R2B_SHA256_ESPERADO"] = R.sha256_mensajes(
            json.loads((E1 / "candado_mensaje_r2b.json").read_text(encoding="utf-8"))["chunks"])
        E = ejecutar("prompt_e3", E3 / "prompt_e3.py", [("\n_candado_mensaje_e3()\n", "\n")])
        v["MENSAJE_E3_SHA256_ESPERADO"] = E.sha256_mensajes_e3(
            json.loads((E3 / "candado_mensaje_e3.json").read_text(encoding="utf-8"))["casos"])
        res = v
    sal.mkdir(parents=True, exist_ok=True)
    nombre = "verificacion_sellos_p3c2.json" if a.verificar else "sellos_p3c2.json"
    (sal / nombre).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
