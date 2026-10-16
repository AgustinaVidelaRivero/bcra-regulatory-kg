"""
lanzar_t2.py — B6.1, tanda 1, T2: el lanzamiento único de la extracción E1 a E3 de los 20 TOs (pre-registro firmado en
95b18217, §2, §3, §4.2 y §7). El modelo es `data/experiment/reext_t0/t2bis/lanzar_t2bis.py`.

Lo que hace, en orden:
  1. controles previos (si uno falla, para sin correr nada):
     - el piso de espacio: 30 GB libres o más en el volumen del repo (31.457.280 KB; §7);
     - las 78 rutas del código de la cadena, en HEAD y en el árbol (data/experiment/tanda1/t1/t1_paso0_rutas.py);
     - el SDK del python con el que corre el runner: anthropic.__version__ = 0.100.0 (§2);
     - el manifiesto de la tanda 1, con su sha256 y su tope (100,7291);
     - que la copia de trabajo de las bases esté fuera del repo y no exista todavía;
  2. el freno por id de modelo (freno_modelo_t2.py) antes del primer TO, sobre las etiquetas de los 20;
  3. para cada TO, en el orden del manifiesto y con la misma --salida (ahí quedan el estado y el presupuesto
     compartido, así que el tope es uno solo para toda la tanda; runner_corpus.py:1377, :1384), desde la raíz del
     repo:
       <python> -B -u data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py \
         --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json \
         --salida data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b --tos <TO> --autorizado-tope 100.7291
     con PYTHONDONTWRITEBYTECODE=1 y SIGINT en su acción por defecto (un proceso lanzado en segundo plano por un shell
     no interactivo lo recibe ignorado; lanzar_t2bis.py:3-5, :40). Después de cada TO, el freno por modelo sobre las
     etiquetas de ese TO;
  4. para si el freno da FRENO o si el runner sale con un código distinto de 0 (0 corrida completa; 3 freno; 4 ids
     repetidos; 1 y 2, la clave o el tope: runner_corpus.py:1369, :1374, :1455, :1460, :1466), sin empezar el TO
     siguiente;
  5. borra la copia de trabajo de las bases al terminar, también cuando para (solo si la creó esta corrida: una
     carpeta que ya existía hace fallar el control previo y no se toca).

No lee la clave: la carga el runner (runner_corpus.py:1370-1371); el lanzador saca ANTHROPIC_API_KEY del entorno del
runner, como lanzar_t2bis.py:36, para que valga la del .env del pipeline. Interrumpirlo con SIGINT (Ctrl-C, o
`kill -INT <pid del lanzador>`) le pasa el SIGINT al runner, espera que termine, lo deja en el registro y no empieza el
TO siguiente: el freno manual del §7.

El cegamiento de U-MED-VERIF (§7): toda la salida de pantalla del runner, que mezcla E1 y E3, se agrega a
`data/experiment/tanda1/t2/NO_ABRIR_salida_e3_tanda1.txt`, que crece TO por TO; el lanzador solo escribe en ese
archivo (una línea `### lanzar_t2: <TO> <hora>` antes de cada TO) y nunca lo lee. El registro de avance,
`data/experiment/tanda1/t2/avance_t2.jsonl`, lleva por TO la hora de inicio y de fin, el código de salida, el resultado
del freno por modelo (con los ids) y el gasto global contra el tope, calculado como Estado.gasto_global
(runner_corpus.py:373-378) sobre `estado_corpus.json` de la --salida. Relanzado, recorre otra vez los 20 y agrega
líneas: el runner saltea las fases cerradas y retoma la abierta, y lo ya pagado sale de la caché.

Uso (desde la raíz del repo; quién lo lanza lo fija el «seguí» de T2):
  caffeinate -i <repo>/.venv/bin/python -B data/experiment/tanda1/t2/lanzar_t2.py --trabajo-bases <dir fuera del repo>
Solo para las pruebas: --solo-tos a,b (limita los TOs), --stub (agrega --stub al runner) y --git-repo <repo> (de dónde
salen los objetos de HEAD para el control de las 78 rutas cuando el lanzador corre en una copia sin .git).
Salida: 0 los TOs pedidos completos; el código del runner si salió distinto de 0; 10 freno por modelo; 2 control
previo; 130 interrumpido.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import signal
import subprocess
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(AQUI))
import freno_modelo_t2 as FM          # noqa: E402

RUNNER_REL = "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py"
MANIFIESTO_REL = "data/experiment/reextraccion_v2/manifiestos/tanda1_20tos_r2b.json"
MANIFIESTO_SHA256 = "4dd025053fec11aabaa9f35e54a9da78912f86c1a11f11abd6aa3e2cc764897a"
SALIDA_REL = "data/experiment/reextraccion_v2/corpus_tanda1/salida_r2b"
TOPE = "100.7291"
SDK = "0.100.0"
PISO_KB = 31457280                      # 30 GB (§7)
RUTAS = REPO / "data" / "experiment" / "tanda1" / "t1" / "t1_paso0_rutas.py"
CONSOLA = AQUI / "NO_ABRIR_salida_e3_tanda1.txt"
AVANCE = AQUI / "avance_t2.jsonl"


def ahora() -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%S%z")


def avance(reg: dict) -> None:
    with AVANCE.open("a", encoding="utf-8") as f:
        f.write(json.dumps(reg, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())
    print(json.dumps(reg, ensure_ascii=False), flush=True)


def gasto_global(salida: Path) -> float | None:
    """Estado.gasto_global (runner_corpus.py:373-378) sobre estado_corpus.json."""
    p = salida / "estado_corpus.json"
    if not p.exists():
        return None
    d = json.loads(p.read_text(encoding="utf-8"))
    g = sum(f["gasto_usd"] for f in d["fases_cerradas"].values())
    fa = d.get("fase_actual")
    if fa:
        g += fa["gasto_previo_usd"] + fa["gasto_proceso_usd"]
    return round(g, 6)


def controles_previos(python: str, git_repo: Path, trabajo: Path) -> dict:
    st = os.statvfs(REPO)
    libres_kb = st.f_bavail * st.f_frsize // 1024
    r = subprocess.run([python, "-B", str(RUTAS), "--repo", str(REPO), "--git-repo", str(git_repo)],
                       capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    v = subprocess.run([python, "-B", "-c", "import anthropic; print(anthropic.__version__)"],
                       capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    man = REPO / MANIFIESTO_REL
    man_sha = hashlib.sha256(man.read_bytes()).hexdigest() if man.exists() else None
    tope_man = json.loads(man.read_text(encoding="utf-8"))["limites"]["tope_global_usd"] if man.exists() else None
    c = {"libres_kb": libres_kb, "piso_kb": PISO_KB, "piso_ok": libres_kb >= PISO_KB,
         "rutas_78_ok": r.returncode == 0, "rutas_78": [x for x in r.stdout.splitlines() if x.startswith(("HEAD", "árbol"))],
         "sdk": v.stdout.strip(), "sdk_ok": v.returncode == 0 and v.stdout.strip() == SDK,
         "manifiesto_sha256_ok": man_sha == MANIFIESTO_SHA256, "tope_ok": tope_man is not None and str(tope_man) == TOPE,
         "trabajo_fuera_del_repo": not trabajo.resolve().is_relative_to(REPO),
         "trabajo_nuevo": not trabajo.exists(),
         "pythondontwritebytecode_del_runner": "1"}
    c["ok"] = all(c[k] for k in ("piso_ok", "rutas_78_ok", "sdk_ok", "manifiesto_sha256_ok", "tope_ok",
                                 "trabajo_fuera_del_repo", "trabajo_nuevo"))
    return c


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo-bases", type=Path, required=True)
    ap.add_argument("--solo-tos", default=None, help="solo para las pruebas")
    ap.add_argument("--stub", action="store_true", help="solo para las pruebas")
    ap.add_argument("--git-repo", type=Path, default=None, help="solo para las pruebas sobre una copia")
    a = ap.parse_args()
    # lanzado en segundo plano por un shell no interactivo, el SIGINT llega ignorado: se restablece el de Python,
    # para que la interrupción manual levante KeyboardInterrupt acá
    signal.signal(signal.SIGINT, signal.default_int_handler)
    python = sys.executable
    trabajo = a.trabajo_bases.resolve()
    borrar = not trabajo.exists()       # solo se borra la carpeta que crea esta corrida, nunca una que ya estaba
    man = json.loads((REPO / MANIFIESTO_REL).read_text(encoding="utf-8"))
    tos = list(man["orden_corrida"])
    if a.solo_tos:
        pedidos = [t.strip() for t in a.solo_tos.split(",") if t.strip()]
        assert all(t in tos for t in pedidos), pedidos
        tos = [t for t in tos if t in pedidos]
    salida = REPO / SALIDA_REL
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ANTHROPIC_API_KEY", None)

    avance({"evento": "inicio_lanzador", "ts": ahora(), "tos": tos, "stub": a.stub, "pid": os.getpid()})
    rc_final = 0
    try:
        c = controles_previos(python, (a.git_repo or REPO).resolve(), trabajo)
        avance({"evento": "controles_previos", "ts": ahora(), **c})
        if not c["ok"]:
            avance({"evento": "parada", "ts": ahora(), "motivo": "control previo"})
            return 2
        f = FM.controlar(REPO, trabajo, tos)
        avance({"evento": "freno_modelo_antes", "ts": ahora(), "tos": tos, **f})
        if f["resultado"] != "OK":
            avance({"evento": "parada", "ts": ahora(), "motivo": "freno por id de modelo antes del primer TO"})
            return 10
        for to in tos:
            cmd = [python, "-B", "-u", RUNNER_REL, "--manifiesto", MANIFIESTO_REL, "--salida", SALIDA_REL,
                   "--tos", to, "--autorizado-tope", TOPE] + (["--stub"] if a.stub else [])
            ini = ahora()
            avance({"evento": "to_inicio", "to": to, "inicio": ini, "comando": cmd[1:]})
            with CONSOLA.open("a", encoding="utf-8") as out:
                out.write(f"### lanzar_t2: {to} {ini}\n")
                out.flush()
                runner = subprocess.Popen(cmd, cwd=REPO, env=env, stdout=out, stderr=subprocess.STDOUT,
                                          preexec_fn=lambda: signal.signal(signal.SIGINT, signal.SIG_DFL))
                try:
                    rc = runner.wait()
                except KeyboardInterrupt:
                    runner.send_signal(signal.SIGINT)
                    rc = runner.wait()
                    f = FM.controlar(REPO, trabajo, [to])
                    avance({"evento": "to_fin", "to": to, "inicio": ini, "fin": ahora(), "rc": rc,
                            "freno_modelo": f["resultado"], "ids_e1": f["ids_e1"], "ids_e3": f["ids_e3"],
                            "gasto_global_usd": gasto_global(salida), "tope_usd": float(TOPE)})
                    avance({"evento": "parada", "ts": ahora(), "motivo": "interrupción manual (SIGINT)"})
                    return 130
            f = FM.controlar(REPO, trabajo, [to])
            avance({"evento": "to_fin", "to": to, "inicio": ini, "fin": ahora(), "rc": rc,
                    "freno_modelo": f["resultado"], "ids_e1": f["ids_e1"], "ids_e3": f["ids_e3"],
                    "gasto_global_usd": gasto_global(salida), "tope_usd": float(TOPE)})
            if f["resultado"] != "OK":
                avance({"evento": "parada", "ts": ahora(), "motivo": f"freno por id de modelo después de {to}"})
                return 10
            if rc != 0:
                avance({"evento": "parada", "ts": ahora(), "motivo": f"el runner salió con {rc} en {to}"})
                return rc if rc > 0 else 1
        return rc_final
    except KeyboardInterrupt:
        avance({"evento": "parada", "ts": ahora(), "motivo": "interrupción manual (SIGINT) fuera de un TO"})
        return 130
    finally:
        if borrar and trabajo.exists() and not trabajo.is_relative_to(REPO):
            shutil.rmtree(trabajo)
        avance({"evento": "fin_lanzador", "ts": ahora(), "copia_de_las_bases_borrada": not trabajo.exists()})


if __name__ == "__main__":
    sys.exit(main())
