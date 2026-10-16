#!/usr/bin/env python3
"""prueba_envoltorio_a2_1.py — Prueba de con_clave_del_entorno.py con un archivo FALSO
(USD 0). El archivo se crea en un directorio temporal con un nombre que no es `.env` ni
termina en `.env`, y se borra al terminar. Ningún valor se imprime: el comando hijo
informa solo si la variable llegó y el sha256 de su valor, que se compara con el del
valor falso.

Casos:
  1. archivo con ANTHROPIC_API_KEY: el hijo la recibe íntegra (sha256 igual), aunque el
     entorno del padre traiga otra; el código de salida es el del hijo (7);
  2. archivo inexistente: código 3, y stderr sin ningún valor;
  3. archivo sin la variable: código 4;
  4. uso incorrecto: código 2;
  5. en ningún caso el valor falso aparece en stdout ni en stderr del envoltorio.

Uso: .venv/bin/python -B prueba_envoltorio_a2_1.py [--out <json>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import secrets
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
if str(BANCO_DIR) not in sys.path:
    sys.path.insert(0, str(BANCO_DIR))
from comun_banco import rel_repo, sha256_file  # noqa: E402

ENVOLTORIO = AQUI / "con_clave_del_entorno.py"
HIJO = ("import hashlib, os, sys; v = os.environ.get('ANTHROPIC_API_KEY'); "
        "print('presente', v is not None, 'sha256', hashlib.sha256((v or '').encode()).hexdigest()); sys.exit(7)")


def correr(args: list[str], env_extra: dict | None = None) -> subprocess.CompletedProcess:
    import os
    env = dict(os.environ)
    env.pop("ANTHROPIC_API_KEY", None)
    env.update(env_extra or {})
    return subprocess.run([sys.executable, "-I", "-B", str(ENVOLTORIO)] + args, capture_output=True, text=True, env=env)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=AQUI / "controles" / "prueba_envoltorio.json")
    a = ap.parse_args()
    falso = "sk-ant-FALSO-" + secrets.token_hex(16)
    sha_falso = hashlib.sha256(falso.encode()).hexdigest()
    casos = []
    with tempfile.TemporaryDirectory() as td:
        con = Path(td) / "entorno_falso_prueba.txt"
        con.write_text(f"OTRA=1\nANTHROPIC_API_KEY={falso}\n", encoding="utf-8")
        sin = Path(td) / "entorno_falso_sin_clave.txt"
        sin.write_text("OTRA=1\n", encoding="utf-8")
        hijo = [sys.executable, "-I", "-c", HIJO]
        r1 = correr(["--entorno", str(con), "--"] + hijo, {"ANTHROPIC_API_KEY": "sk-ant-del-padre"})
        casos.append({"caso": "1 archivo con la variable (el padre trae otra)", "returncode": r1.returncode, "esperado": 7,
                      "llego": "presente True" in r1.stdout, "sha256_igual_al_falso": sha_falso in r1.stdout,
                      "ok": r1.returncode == 7 and "presente True" in r1.stdout and sha_falso in r1.stdout})
        r2 = correr(["--entorno", str(Path(td) / "no_existe.txt"), "--"] + hijo)
        casos.append({"caso": "2 archivo inexistente", "returncode": r2.returncode, "esperado": 3,
                      "stderr": r2.stderr.strip(), "ok": r2.returncode == 3 and r2.stdout == ""})
        r3 = correr(["--entorno", str(sin), "--"] + hijo)
        casos.append({"caso": "3 archivo sin la variable", "returncode": r3.returncode, "esperado": 4,
                      "stderr": r3.stderr.strip(), "ok": r3.returncode == 4 and r3.stdout == ""})
        r4 = correr(["--entorno", str(con)] + hijo)
        casos.append({"caso": "4 uso incorrecto (sin --)", "returncode": r4.returncode, "esperado": 2,
                      "stderr": r4.stderr.strip(), "ok": r4.returncode == 2})
        fuga = any(falso in (r.stdout + r.stderr) for r in (r1, r2, r3, r4))
        casos.append({"caso": "5 el valor no aparece en ninguna salida", "ok": not fuga})
        rutas_temporales = [con.name, sin.name]
    borrado = not Path(td).exists()
    res = {"generado": datetime.now().isoformat(timespec="seconds"), "unidad": "A2.1, tramo 1 — prueba del envoltorio",
           "envoltorio": rel_repo(ENVOLTORIO), "sha256_envoltorio": sha256_file(ENVOLTORIO),
           "sha256_esperado": "83527b334ca6c6be6ec3ce277bb43f60c6679347a9da237253e9cf6beb06a397",
           "archivos_falsos": rutas_temporales, "archivos_falsos_borrados": borrado,
           "nota": "el valor falso se genera al azar en cada corrida y no se persiste; se persiste solo si llegó y si su sha256 coincidió",
           "casos": casos}
    res["PASS"] = (all(c["ok"] for c in casos) and borrado and res["sha256_envoltorio"] == res["sha256_esperado"])
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    for c in casos:
        print(("OK  " if c["ok"] else "FALLA ") + c["caso"])
    print("TOTAL:", "PASS" if res["PASS"] else "FAIL", "->", rel_repo(a.out))
    return 0 if res["PASS"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
