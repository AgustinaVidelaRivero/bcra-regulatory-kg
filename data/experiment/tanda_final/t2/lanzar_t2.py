"""
lanzar_t2.py — B6.1, tanda final, T2: el lanzamiento único de la extracción E1 a E3 de los 98 TOs, en dos tramos con el
control entre tramos (pre-registro firmado de la tanda final, §2, §3, §4.2, §5 y §8, que siguen al de la tanda 1). El
modelo es el de la tanda 1, `data/experiment/tanda1/t2/lanzar_t2.py`.

Lo que hace, en orden:
  1. controles previos (si uno falla, para sin correr nada; salida 2):
     - el piso de espacio: 30 GB libres o más en el volumen del repo (31.457.280 KB; pre-registro, §4.1, punto 6);
     - las 78 rutas del código de la cadena, en HEAD y en el árbol
       (data/experiment/tanda_final/t1/t1_paso0_rutas_tanda_final.py; §2 y §8);
     - el SDK del python con el que corre el runner: anthropic.__version__ = 0.100.0 (§2);
     - el manifiesto de la tanda final, con su sha256 y su tope (151,5835);
     - los dos tramos: los primeros 30 de `orden_corrida` son los del tramo 1 y los otros 68 los del tramo 2
       (data/experiment/tanda_final/preregistro/tramos_tanda_final.json);
     - que la copia de trabajo (de las bases y del control entre tramos) esté fuera del repo y no exista todavía;
  2. el freno por id de modelo (freno_modelo_t2.py) antes del primer TO, sobre las etiquetas de los 98;
  3. el tramo 1: sus 30 TOs, en el orden del manifiesto y con la misma --salida (ahí quedan el estado y el presupuesto
     compartido, así que el tope es uno solo para los dos tramos; runner_corpus.py:1377, :1384), cada uno desde la raíz
     del repo con
       <python> -B -u data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py \
         --manifiesto data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json \
         --salida data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b --tos <TO> --autorizado-tope 151.5835
     con PYTHONDONTWRITEBYTECODE=1 y SIGINT en su acción por defecto. Correr los 30 de a uno, con la misma --salida, es
     correr `--tos <los 30>` (§5) con el freno por modelo después de cada TO, como en la tanda 1. Después de cada TO, el
     freno por modelo sobre las etiquetas de ese TO (`corpus_<TO>_e1`, `corpus_<TO>_reintentos_e1` y `corpus_<TO>_e3`);
  4. al cerrar el tramo 1, el control entre tramos (data/experiment/tanda_final/preregistro/
     control_entre_tramos_tanda_final_mesa.py, sellado con el pre-registro) sobre una copia: copia (archivos, sin enlaces,
     sin .env, NO_ABRIR_ ni *_SOLO_MESA*) de resumen_t2.py de la tanda 1, el manifiesto, la E0 de la tanda final, la
     --salida del runner y data/experiment/tanda_final/preregistro/; lo corre con las bases del pre-registro
     (salida_cifras_preregistro_tanda_final.json) y la lista de los 30, y deja su JSON en
     data/experiment/tanda_final/t2/control_entre_tramos_tanda_final.json. Con OK (salida 0) sigue con el tramo 2 sin leer
     nada; con FRENO (salida 3) para con salida 11 y decide la autora; con otra salida, para con 12;
  5. el tramo 2: sus 68 TOs, igual que el tramo 1;
  6. para si el freno da FRENO (salida 10) o si el runner sale con un código distinto de 0 (devuelve ese código), sin
     empezar el TO siguiente;
  7. la pausa entre documentos (§4.2; registro de decisiones, §27): desde el viernes 23/10/2026 a las 18:00 (−03), antes de
     lanzar cada TO, si la tanda no está sellada (mientras corre este lanzador no lo está), no lanza el TO y para con
     salida 20: el que estaba corriendo ya terminó. Relanzado para retomar después de B6.3 y de las tripletas T (decisión
     de la autora), va con --retomar-tras-pausa;
  8. borra la copia de trabajo al terminar, también cuando para (solo si la creó esta corrida).

No lee la clave: la carga el runner (runner_corpus.py:1370-1371); el lanzador saca ANTHROPIC_API_KEY del entorno del
runner, como el de la tanda 1, para que valga la del .env del pipeline. Interrumpirlo con SIGINT (Ctrl-C, o
`kill -INT <pid del lanzador>`) le pasa el SIGINT al runner, espera que termine, lo deja en el registro y no empieza el
TO siguiente: el freno manual (§4.2).

El cegamiento de U-MED-VERIF (§4.1; pre-registro de la tanda 1, §7): toda la salida de pantalla del runner, que mezcla
E1 y E3, se agrega a `data/experiment/tanda_final/t2/NO_ABRIR_salida_e3_tanda_final.txt`; el lanzador solo escribe en
ese archivo (una línea `### lanzar_t2: <TO> <hora>` antes de cada TO) y nunca lo lee. El registro de avance,
`data/experiment/tanda_final/t2/avance_t2.jsonl`, lleva por TO la hora de inicio y de fin, el tramo, el código de
salida, el resultado del freno por modelo (con los ids) y el gasto global contra el tope (Estado.gasto_global,
runner_corpus.py:373-378, sobre `estado_corpus.json` de la --salida); los controles previos, el control entre tramos,
las paradas y el fin. Relanzado, recorre otra vez los TOs y agrega líneas: el runner saltea las fases cerradas y retoma
la abierta, y lo ya pagado sale de la caché. Con el tramo 1 ya cerrado, el control entre tramos vuelve a correr y vale
el mismo criterio.

Uso (desde la raíz del repo; quién lo lanza lo fija el «seguí» de T2):
  caffeinate -i <repo>/.venv/bin/python -B data/experiment/tanda_final/t2/lanzar_t2.py --trabajo <dir fuera del repo>
Con la decisión de la autora, y solo con ella: --autorizado-tramo-2 (sigue con el tramo 2 aunque el control entre tramos
dé FRENO, que igual corre y queda en el registro) y --retomar-tras-pausa (no aplica la pausa entre documentos).
Solo para las pruebas: --solo-tos-tramo-1 a,b y --solo-tos-tramo-2 c (limitan los TOs de cada tramo), --stub (agrega
--stub al runner), --git-repo <repo> (de dónde salen los objetos de HEAD para el control de las 78 rutas cuando el
lanzador corre en una copia sin .git) y --hora-simulada <ISO> (la hora con la que se evalúa la pausa).
Salida: 0 los TOs pedidos completos; el código del runner si salió distinto de 0; 10 freno por modelo; 11 FRENO del
control entre tramos; 12 el control entre tramos no corrió; 20 pausa entre documentos; 2 control previo; 130
interrumpido.
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
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(AQUI))
import freno_modelo_t2 as FM          # noqa: E402

RUNNER_REL = "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py"
MANIFIESTO_REL = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
MANIFIESTO_SHA256 = "23654ef8a43900b2547c2de6dac3e86f2d29c91d6b380ca4439b102468f63740"
SALIDA_REL = "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b"
E0_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
PREREG_REL = "data/experiment/tanda_final/preregistro"
TRAMOS_REL = f"{PREREG_REL}/tramos_tanda_final.json"
CONTROL_REL = f"{PREREG_REL}/control_entre_tramos_tanda_final_mesa.py"
BASES_REL = f"{PREREG_REL}/salida_cifras_preregistro_tanda_final.json"
RESUMEN_T2_TANDA1_REL = "data/experiment/tanda1/t2/resumen_t2.py"   # el que importa el control entre tramos
TOPE = "151.5835"
SDK = "0.100.0"
PISO_KB = 31457280                      # 30 GB (pre-registro de la tanda final, §4.1, punto 6)
N_TRAMO_1, N_TRAMO_2 = 30, 68
PAUSA = datetime(2026, 10, 23, 18, 0, tzinfo=timezone(timedelta(hours=-3)))   # registro de decisiones, §27
RUTAS = REPO / "data" / "experiment" / "tanda_final" / "t1" / "t1_paso0_rutas_tanda_final.py"
CONSOLA = AQUI / "NO_ABRIR_salida_e3_tanda_final.txt"
AVANCE = AQUI / "avance_t2.jsonl"
CONTROL_OUT = AQUI / "control_entre_tramos_tanda_final.json"


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


def controles_previos(python: str, git_repo: Path, trabajo: Path, man: dict) -> dict:
    st = os.statvfs(REPO)
    libres_kb = st.f_bavail * st.f_frsize // 1024
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([python, "-B", str(RUTAS), "--repo", str(REPO), "--git-repo", str(git_repo)],
                       capture_output=True, text=True, env=env)
    v = subprocess.run([python, "-B", "-c", "import anthropic; print(anthropic.__version__)"],
                       capture_output=True, text=True, env=env)
    mp = REPO / MANIFIESTO_REL
    man_sha = hashlib.sha256(mp.read_bytes()).hexdigest()
    tramos = json.loads((REPO / TRAMOS_REL).read_text(encoding="utf-8"))
    orden = man["orden_corrida"]
    c = {"libres_kb": libres_kb, "piso_kb": PISO_KB, "piso_ok": libres_kb >= PISO_KB,
         "rutas_78_ok": r.returncode == 0, "rutas_78": [x for x in r.stdout.splitlines() if x.startswith(("HEAD", "árbol"))],
         "sdk": v.stdout.strip(), "sdk_ok": v.returncode == 0 and v.stdout.strip() == SDK,
         "manifiesto_sha256_ok": man_sha == MANIFIESTO_SHA256,
         "tope_ok": str(man["limites"]["tope_global_usd"]) == TOPE,
         "tramos_ok": (len(orden) == N_TRAMO_1 + N_TRAMO_2 and set(orden[:N_TRAMO_1]) == set(tramos["tramo_1_tos"])
                       and set(orden[N_TRAMO_1:]) == set(tramos["tramo_2_tos"])),
         "trabajo_fuera_del_repo": not trabajo.resolve().is_relative_to(REPO),
         "trabajo_nuevo": not trabajo.exists(),
         "pythondontwritebytecode_del_runner": "1"}
    c["ok"] = all(c[k] for k in ("piso_ok", "rutas_78_ok", "sdk_ok", "manifiesto_sha256_ok", "tope_ok", "tramos_ok",
                                 "trabajo_fuera_del_repo", "trabajo_nuevo"))
    return c


def _sin_abrir(nombre: str) -> bool:
    return (nombre == ".env" or nombre.startswith(".env.") or nombre.endswith(".env") or nombre.startswith("NO_ABRIR_")
            or "_SOLO_MESA" in nombre)


def control_entre_tramos(python: str, trabajo: Path, tramo1: list[str]) -> dict:
    """Corre el control entre tramos sellado sobre una copia de lo que lee. Devuelve su salida y su resultado."""
    d = trabajo / "control_entre_tramos"
    if d.exists():
        shutil.rmtree(d)
    copia = d / "copia"
    ignorar = lambda _dir, nombres: [n for n in nombres if _sin_abrir(n) or n == "__pycache__"]  # noqa: E731
    for rel in (RESUMEN_T2_TANDA1_REL, MANIFIESTO_REL, E0_REL, SALIDA_REL, PREREG_REL):
        o, x = REPO / rel, copia / rel
        x.parent.mkdir(parents=True, exist_ok=True)
        if o.is_dir():
            shutil.copytree(o, x, symlinks=False, ignore=ignorar)
        else:
            shutil.copy2(o, x)
    malos = [str(p.relative_to(copia)) for p in copia.rglob("*") if p.is_symlink() or _sin_abrir(p.name)]
    if malos:
        return {"resultado": "NO CORRIÓ", "motivo": "la copia del control trae enlaces o archivos que no se abren",
                "rutas": malos}
    (d / "tramo_1.json").write_text(json.dumps(tramo1), encoding="utf-8")
    cmd = [python, "-I", "-B", str(copia / CONTROL_REL), "--repo", str(copia), "--manifiesto", MANIFIESTO_REL,
           "--salida", str(copia / SALIDA_REL), "--tramo", str(d / "tramo_1.json"), "--bases", str(copia / BASES_REL),
           "--out", str(CONTROL_OUT)]
    r = subprocess.run(cmd, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    res = {"rc": r.returncode, "salida": r.stdout.strip().splitlines(), "error": r.stderr.strip().splitlines()[-3:],
           "resultado": {0: "OK", 3: "FRENO"}.get(r.returncode, "NO CORRIÓ"),
           "control_sha256": hashlib.sha256((REPO / CONTROL_REL).read_bytes()).hexdigest(),
           "control_en_la_copia_igual": (copia / CONTROL_REL).read_bytes() == (REPO / CONTROL_REL).read_bytes()}
    shutil.rmtree(d)
    return res


def correr_to(python: str, to: str, tramo: int, stub: bool, env: dict, trabajo: Path, salida: Path) -> tuple[int, dict]:
    cmd = [python, "-B", "-u", RUNNER_REL, "--manifiesto", MANIFIESTO_REL, "--salida", SALIDA_REL,
           "--tos", to, "--autorizado-tope", TOPE] + (["--stub"] if stub else [])
    ini = ahora()
    avance({"evento": "to_inicio", "to": to, "tramo": tramo, "inicio": ini, "comando": cmd[1:]})
    interrumpido = False
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
            interrumpido = True
    f = FM.controlar(REPO, trabajo, [to])
    avance({"evento": "to_fin", "to": to, "tramo": tramo, "inicio": ini, "fin": ahora(), "rc": rc,
            "freno_modelo": f["resultado"], "ids_e1": f["ids_e1"], "ids_e3": f["ids_e3"],
            "gasto_global_usd": gasto_global(salida), "tope_usd": float(TOPE)})
    if interrumpido:
        raise KeyboardInterrupt
    return rc, f


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True, help="carpeta nueva fuera del repo (bases y control)")
    ap.add_argument("--autorizado-tramo-2", action="store_true", help="solo con la decisión de la autora")
    ap.add_argument("--retomar-tras-pausa", action="store_true", help="solo con la decisión de la autora")
    ap.add_argument("--solo-tos-tramo-1", default=None, help="solo para las pruebas")
    ap.add_argument("--solo-tos-tramo-2", default=None, help="solo para las pruebas")
    ap.add_argument("--stub", action="store_true", help="solo para las pruebas")
    ap.add_argument("--git-repo", type=Path, default=None, help="solo para las pruebas sobre una copia")
    ap.add_argument("--hora-simulada", default=None, help="solo para las pruebas: ISO con zona, p. ej. 2026-10-23T18:00:00-03:00")
    a = ap.parse_args()
    # lanzado en segundo plano por un shell no interactivo, el SIGINT llega ignorado: se restablece el de Python,
    # para que la interrupción manual levante KeyboardInterrupt acá
    signal.signal(signal.SIGINT, signal.default_int_handler)
    python = sys.executable
    trabajo = a.trabajo.resolve()
    bases = trabajo / "bases"
    borrar = not trabajo.exists()       # solo se borra la carpeta que crea esta corrida, nunca una que ya estaba
    man = json.loads((REPO / MANIFIESTO_REL).read_text(encoding="utf-8"))
    orden = list(man["orden_corrida"])
    tramos = {1: orden[:N_TRAMO_1], 2: orden[N_TRAMO_1:]}
    for k, sel in ((1, a.solo_tos_tramo_1), (2, a.solo_tos_tramo_2)):
        if sel is not None:
            pedidos = [t.strip() for t in sel.split(",") if t.strip()]
            assert all(t in tramos[k] for t in pedidos), (k, pedidos)
            tramos[k] = [t for t in tramos[k] if t in pedidos]
    tos = tramos[1] + tramos[2]
    salida = REPO / SALIDA_REL
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ANTHROPIC_API_KEY", None)

    def en_pausa() -> bool:
        if a.retomar_tras_pausa:
            return False
        h = datetime.fromisoformat(a.hora_simulada) if a.hora_simulada else datetime.now(timezone.utc)
        return h >= PAUSA

    avance({"evento": "inicio_lanzador", "ts": ahora(), "tramo_1": tramos[1], "tramo_2": tramos[2], "stub": a.stub,
            "autorizado_tramo_2": a.autorizado_tramo_2, "retomar_tras_pausa": a.retomar_tras_pausa,
            "hora_simulada": a.hora_simulada, "pid": os.getpid()})
    try:
        c = controles_previos(python, (a.git_repo or REPO).resolve(), trabajo, man)
        avance({"evento": "controles_previos", "ts": ahora(), **c})
        if not c["ok"]:
            avance({"evento": "parada", "ts": ahora(), "motivo": "control previo"})
            return 2
        trabajo.mkdir(parents=True)
        f = FM.controlar(REPO, bases, tos)
        avance({"evento": "freno_modelo_antes", "ts": ahora(), "tos": len(tos), **f})
        if f["resultado"] != "OK":
            avance({"evento": "parada", "ts": ahora(), "motivo": "freno por id de modelo antes del primer TO"})
            return 10
        for tramo in (1, 2):
            if tramo == 2:
                ct = control_entre_tramos(python, trabajo, tramos[1])
                avance({"evento": "control_entre_tramos", "ts": ahora(), **ct})
                if ct["resultado"] == "NO CORRIÓ":
                    avance({"evento": "parada", "ts": ahora(), "motivo": "el control entre tramos no corrió"})
                    return 12
                if ct["resultado"] == "FRENO" and not a.autorizado_tramo_2:
                    avance({"evento": "parada", "ts": ahora(), "motivo": "FRENO del control entre tramos: decide la autora"})
                    return 11
            for to in tramos[tramo]:
                if en_pausa():
                    avance({"evento": "parada", "ts": ahora(), "motivo": "pausa entre documentos (viernes 23/10/2026, "
                            "18:00): no se lanza el TO siguiente", "to_no_lanzado": to})
                    return 20
                rc, f = correr_to(python, to, tramo, a.stub, env, bases, salida)
                if f["resultado"] != "OK":
                    avance({"evento": "parada", "ts": ahora(), "motivo": f"freno por id de modelo después de {to}"})
                    return 10
                if rc != 0:
                    avance({"evento": "parada", "ts": ahora(), "motivo": f"el runner salió con {rc} en {to}"})
                    return rc if rc > 0 else 1
        return 0
    except KeyboardInterrupt:
        avance({"evento": "parada", "ts": ahora(), "motivo": "interrupción manual (SIGINT)"})
        return 130
    finally:
        if borrar and trabajo.exists() and not trabajo.is_relative_to(REPO):
            shutil.rmtree(trabajo)
        avance({"evento": "fin_lanzador", "ts": ahora(), "copia_de_trabajo_borrada": not trabajo.exists()})


if __name__ == "__main__":
    sys.exit(main())
