"""Lanzador de la corrida real de T2-bis de U-REEXT-T0 con su vigilante externo.

Arranca el runner desde la raíz del repo con el comando de T2-bis (con --autorizado-tope 80.0, el tope del manifiesto,
que el runner exige) y SIGINT en su acción por defecto (un proceso lanzado en segundo plano por un shell no
interactivo lo recibe ignorado, y Python lo deja así: el SIGINT del vigilante no tendría efecto). Después arranca el
vigilante con el pid del runner y espera a los dos. No lee la clave de la API: la carga el runner.

Uso: <repo>/.venv/bin/python -B lanzar_t2bis.py <repo> <dir_t2bis>   (escribe corrida_t2bis.log, vigilante.log y lanzador.json)
Para las pruebas en seco: python -B lanzar_t2bis.py <copia> <dir> --comando-seco <variante> <umbral>
"""
import json
import os
import signal
import subprocess
import sys
import time
from pathlib import Path

RAIZ, DIR = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
SECO = sys.argv[3:5] if len(sys.argv) > 3 and sys.argv[3] == "--comando-seco" else None
REPO_VENV = Path(sys.executable)          # el python del .venv del repo, con el que se corre este lanzador
PRESUPUESTO = "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/presupuesto_compartido.json"
UMBRAL = 49.659786 + 3.0
if SECO:
    variante = sys.argv[4]
    UMBRAL = float(sys.argv[5])
    cmd = [str(REPO_VENV), "-B", "-u", str(DIR / "seco_t2bis.py"), str(RAIZ), variante, str(DIR / f"seco_vigilado_{variante.replace('+', '_')}.json")]
    nombre = "seco_vigilado"
else:
    cmd = [str(REPO_VENV), "-B", "-u", "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py",
           "--manifiesto", "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos_r2b.json",
           "--salida", "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b",
           "--perfil-r2", "--tos", "cap", "--reabrir-fase", "cap:e1,cap:e3", "--autorizado-tope", "80.0"]
    nombre = "corrida_t2bis"
env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
env.pop("ANTHROPIC_API_KEY", None)
ini = time.strftime("%Y-%m-%dT%H:%M:%S%z")
with open(DIR / f"{nombre}.log", "w", encoding="utf-8") as out:
    runner = subprocess.Popen(cmd, cwd=RAIZ, env=env, stdout=out, stderr=subprocess.STDOUT,
                              preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_DFL))
    vig = subprocess.Popen([str(REPO_VENV), "-B", str(DIR / "vigilante_t2bis.py"), "--pid", str(runner.pid),
                            "--presupuesto", str(RAIZ / PRESUPUESTO), "--umbral", f"{UMBRAL:.6f}",
                            "--log", str(DIR / f"vigilante_{nombre}.log")], env=env)
    rc_r = runner.wait()
    rc_v = vig.wait()
res = {"inicio": ini, "fin": time.strftime("%Y-%m-%dT%H:%M:%S%z"), "comando": cmd[1:], "pid_runner": runner.pid,
       "rc_runner": rc_r, "rc_vigilante": rc_v, "umbral_usd": round(UMBRAL, 6)}
(DIR / f"lanzador_{nombre}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
