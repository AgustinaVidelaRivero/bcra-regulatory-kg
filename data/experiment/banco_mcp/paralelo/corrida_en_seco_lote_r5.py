#!/usr/bin/env python3
"""corrida_en_seco_lote_r5.py — La corrida en seco de agentes/lanzar_lote_paralelo_r5.py (U-BANCO-R5-a), a USD 0: sin API, sin
Neo4j, sin Docker y sin el denso.

Importa el lanzador r5 por su ruta (sin tocar el sys.path por fuera: el módulo agrega las suyas, como en la corrida real) y llama
a su `main`, en modo real, en este proceso (como lo hace b63/correr_b63.py con el lote) o como proceso aparte, con el CLI falso
(paralelo/cli_falso/claude_falso.py, por el envoltorio de --cli-falso) primero en el PATH, una clave de relleno que no es una
clave y ANTHROPIC_BASE_URL en un puerto cerrado. El lote corre el mismo camino que el real (el lanzador de una sesión, el de N6 de
prueba con una configuración de juguete, paralelo/seco_r5/; LA.preparar_sesion, LA.env_sesion, `claude`, el servidor MCP de
fragmentos BM25, que no carga ningún modelo ni el driver del grafo; LA.copiar_sesion, LA.armar_meta), y ninguna petición sale.

Cada llamada al lanzador lleva --patron-de-prueba con el token TOKEN, y cada guarda que corre esta prueba, el patrón de prueba
`<TOKEN>\\.py|<TOKEN>_b63\\.py` (la forma del real: el de un paso, más el de B6.3): ningún `pgrep` de la prueba lleva el patrón
real. Las ramas:
  D0  el CLI del PATH es el falso; el token de prueba se rechaza sin un CLI falso en el PATH o con un nombre de un paso pago;
  D1  entrada A y sesiones con R5 A: el lote corre (0), con presupuesto 1,80 por sesión, que sale de la entrada; cada sesión, con
      --max-turns 32, --max-budget-usd 1.8 y el tope 30 en su prompt y su meta;
  D2  entrada B y sesiones con R5 B: el lote corre (0), con presupuesto 3,30; cada sesión, con 47, 3.3 y 45;
  D3  entrada C (un tercer R5): frena con el 5 sin lanzar ninguna sesión;
  D4  otro sha256 de la entrada: el lote inválido (3), sin registro y sin lanzar nada;
  D5  una sesión cuyo R5 no es el de la entrada (entrada A y sesiones con R5 B, y al revés): frena con el 5 al terminar la
      primera, y la segunda no se lanza;
  D6  --presupuesto-sesion distinto del de la entrada: el 3; igual: corre;
  D7  la guarda frena (7) sin lanzar nada con un proceso hermano vivo con un nombre del patrón (`<TOKEN>.py` o `<TOKEN>_b63.py`),
      en el lote y en la línea de comandos de guardas_lote_r5.py; el pgrep para esperar lo ve; al cerrarle la entrada, deja pasar;
  D8  la guarda no frena por sus ancestros: un runner con un nombre del patrón que corre el lote en su proceso (como correr_b63.py)
      y uno que lo lanza como proceso hijo; `pgrep -a` los ve a los dos (sin -a, el pgrep de macOS deja fuera al que lo llama y a
      sus ancestros), y la tabla de ps, con el filtro de la guarda, ve al primero como un proceso del patrón;
  D9  la guarda no frena por el pgrep de otra guarda que corre a la vez (un proceso que se presenta como `pgrep -f <patrón>`), por
      un Python que espera con el patrón como argumento ni por un shell que lo nombra; pgrep los ve a todos.
La espera es la del proceso padre sobre sus hijos (Popen.wait): sin sleep. El resultado, solo cuentas, sha256 y banderas, va a
--resultado; ninguna salida de tool se imprime ni se escribe ahí.

Uso: corrida_en_seco_lote_r5.py --cli-falso <dir con `claude`> --entradas <dir> --out <dir> --sesiones <dir> --pruebas <dir>
     --resultado <json>
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import importlib.util
import io
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
LANZADOR = "paralelo/seco_r5/lanzar_agente_r5_prueba.py"
CFG = {"A": "paralelo/seco_r5/config_agentes_r5_A.json", "B": "paralelo/seco_r5/config_agentes_r5_B.json"}
TOKEN = "rcinco_prueba_paso"
CLAVE_DE_RELLENO = "sin-clave-corrida-en-seco"
URL_CERRADA = "http://127.0.0.1:9"
BRAZO = "fragmentos_bm25"


def importar(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = m
    spec.loader.exec_module(m)
    return m


R5L = importar("lanzar_lote_paralelo_r5", BANCO_DIR / "agentes" / "lanzar_lote_paralelo_r5.py")
BASE = sys.modules["lanzar_lote_paralelo"]
G = sys.modules["guardas_lote_r5"]
LA = R5L.LA
PATRON = R5L.patron_de_prueba(TOKEN)
R5 = {"A": R5L.R5_ADMITIDOS[0], "B": R5L.R5_ADMITIDOS[1]}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_archivo(p: Path) -> str:
    return sha(p.read_bytes())


def escribir_lote(p: Path, prefijo: str, planes: list[str]) -> Path:
    ses = [{"id": f"{prefijo}-{k + 1:02d}", "brazo": BRAZO, "bloque": f"{prefijo}-{k + 1:02d}",
            "pregunta": f"Pregunta {k + 1} de la corrida en seco del lote r5 [[seco:{pl}]]"} for k, pl in enumerate(planes)]
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"sesiones": ses}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return p


def argv_lote(entrada: Path, lote: Path, out: Path, ses: Path, cfg: str, P: int = 1, tope: float = 12, freno: float = 10,
              sha_entrada: str | None = None, extra: tuple = ()) -> list[str]:
    return ["--entrada", str(entrada), "--sha256-entrada", sha_entrada or sha_archivo(entrada), "--lote", str(lote),
            "--out", str(out), "--sesiones", str(ses), "-P", str(P), "--modo", "real", "--tope", str(tope), "--freno", str(freno),
            "--lanzador", LANZADOR, "--config-agentes", CFG[cfg], "--patron-de-prueba", TOKEN, *extra]


def leer_registro(out: Path) -> dict | None:
    p = out / "registro_lote.json"
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None


def en_proceso(cfg: str, argv: list[str]) -> dict:
    """El lanzador r5 en este proceso, como lo corre b63/correr_b63.py."""
    os.environ["RCINCO_CONFIG_AGENTES"] = CFG[cfg]
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = R5L.main(argv)
    out = Path(argv[argv.index("--out") + 1])
    return {"rc": rc, "registro": leer_registro(out), "salida": buf.getvalue().splitlines(), "patron_vigente": G.PATRON_PAGO}


def subproceso(cfg: str, argv: list[str], prefijo: list[str] | None = None) -> dict:
    """El lanzador r5 como proceso aparte (así los procesos de prueba, hijos de esta corrida, no son de su árbol)."""
    env = dict(os.environ) | {"RCINCO_CONFIG_AGENTES": CFG[cfg]}
    cmd = (prefijo or []) + [sys.executable, "-B", str(BANCO_DIR / "agentes" / "lanzar_lote_paralelo_r5.py"), *argv]
    r = subprocess.run(cmd, capture_output=True, text=True, env=env)
    out = Path(argv[argv.index("--out") + 1])
    return {"rc": r.returncode, "registro": leer_registro(out),
            "salida": [l for l in r.stdout.splitlines() if l.startswith(("FRENO", "LOTE INVÁLIDO"))]}


def resumen(corrida: dict, ses_raiz: Path) -> dict:
    reg = corrida["registro"]
    r = {"rc": corrida["rc"], "lineas_freno": [l for l in corrida["salida"] if l.startswith(("FRENO", "LOTE INVÁLIDO"))]}
    cfgs = sorted(p.name for p in (ses_raiz / "config").glob("*")) if (ses_raiz / "config").is_dir() else []
    r["carpetas_de_configuracion_creadas"] = len(cfgs)
    if reg is None:
        return r | {"registro": None}
    ses = reg["sesiones"]
    lanzas = [e for e in reg["eventos"] if e["evento"] == "lanza"]
    r |= {"codigo": reg["codigo"], "freno": reg["freno"],
          "R5_de_la_entrada": reg["R5"]["entrada"]["R5"], "clave": reg["R5"]["entrada"]["clave"], "admitido": reg["R5"]["admitido"],
          "presupuesto_por_sesion_usd": reg["presupuesto_por_sesion_usd"],
          "presupuesto_efectivo_de_la_guarda_usd": reg["presupuesto_efectivo_de_la_guarda_usd"],
          "estados": {e: sum(1 for s in ses if s["estado"] == e) for e in sorted({s["estado"] for s in ses})},
          "lanzadas": sum(1 for s in ses if s["estado"] not in ("no lanzada", "pendiente")),
          "r5_por_sesion": {s["id"]: s.get("r5") for s in ses if s.get("r5")},
          "guardas_de_otro_paso_pago": [{"tanda": e["antes_de_la_tanda"], "hallados": [h["script"] for h in e["hallados"]]}
                                        for e in reg["eventos"] if e["evento"] == "guarda de otro paso pago"],
          "maximo_a_la_vez": max((e["corriendo_con_ella"] for e in lanzas), default=0),
          "lanzador_del_lote": [x["ruta"] for x in reg["lanzador_del_lote"]],
          "lanzador_r5": [x["ruta"] for x in reg["R5"]["lanzador_r5"]],
          "acumulado_R9_usd": reg["acumulado_R9_usd"]}
    return r


def sesiones_con_r5(out: Path, reg: dict, k: str, lote: Path) -> dict:
    """Por sesión: el R5 de su comando (--max-turns, --max-budget-usd) y de su meta (tope del prompt), y su prompt, que es el de la
    configuración de juguete k (LA.construir_prompt)."""
    cfg = LA.cargar(BANCO_DIR / CFG[k])
    res = {}
    for s in reg["sesiones"]:
        d = out / s["id"]
        com = json.loads((d / f"comando_{s['id']}.json").read_text(encoding="utf-8"))
        meta = json.loads((d / f"meta_{s['id']}.json").read_text(encoding="utf-8"))
        argv = com["argv"]
        pregunta = next(x for x in json.loads(lote.read_text(encoding="utf-8"))["sesiones"] if x["id"] == s["id"])["pregunta"]
        prompt = (d / f"prompt_{s['id']}.txt").read_text(encoding="utf-8")
        res[s["id"]] = {"max_turns": argv[argv.index("--max-turns") + 1], "max_budget_usd": argv[argv.index("--max-budget-usd") + 1],
                        "tope_en_la_meta": meta["corte_R5"]["tope_tool_calls_prompt"],
                        "prompt_es_el_de_la_config": prompt == LA.construir_prompt(cfg, BRAZO, pregunta),
                        "completa_R3": meta["completitud_R3"]["completa"], "r5_del_lote": s.get("r5")}
    return res


class Prueba:
    """Un proceso propio que solo espera su entrada estándar (sin sleep); al cerrarla, termina y el padre lo espera."""

    def __init__(self, argv: list[str], executable: str | None = None):
        self.p = subprocess.Popen(argv, executable=executable, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL,
                                  stderr=subprocess.DEVNULL)

    def cerrar(self) -> int:
        self.p.stdin.close()
        return self.p.wait()


def guion(p: Path, texto: str = "import sys\nsys.stdin.read()\n") -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(texto, encoding="utf-8")
    return p


def guarda_cli() -> dict:
    """guardas_lote_r5.py como proceso aparte (el comando de una guarda), con el patrón de prueba."""
    r = subprocess.run([sys.executable, "-I", "-B", str(AQUI / "guardas_lote_r5.py"), "pago", "--patron", PATRON],
                       capture_output=True, text=True)
    return {"rc": r.returncode, "lineas": [l.split(": pid ")[0] + " (" + l.rsplit("(", 1)[-1] if "pid" in l else l
                                           for l in r.stdout.splitlines()]}


# El pgrep de macOS deja fuera, sin -a, al proceso que lo llama y a sus ancestros (man pgrep, -a): los runners de D8 se ven a sí
# mismos con `pgrep -a -f` y, el que corre el lote en su proceso, también por la tabla de ps con el filtro de la guarda.
RUNNER_EN_PROCESO = '''import importlib.util, json, os, re, subprocess, sys
from pathlib import Path
ruta, salida, token = sys.argv[1], Path(sys.argv[2]), sys.argv[3]
spec = importlib.util.spec_from_file_location("lanzar_lote_paralelo_r5", ruta)
m = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = m
spec.loader.exec_module(m)
m.fijar_patron_de_prueba(token)
G = sys.modules["guardas_lote_r5"]
yo = os.getpid()
guion = G.script_python(G.tabla_procesos()[yo][1])
del_patron = bool(guion) and re.search(G.PATRON_PAGO, G.BASE._nombre(guion)) is not None
con_a = str(yo) in subprocess.run(["pgrep", "-a", "-f", G.PATRON_PAGO], capture_output=True, text=True).stdout.split()
sin_a = yo in G.pgrep()
rc = m.main(sys.argv[4:])
salida.write_text(json.dumps({"es_un_proceso_del_patron": del_patron, "pgrep_a_lo_ve": con_a, "pgrep_sin_a_lo_ve": sin_a,
                              "rc": rc}) + "\\n", encoding="utf-8")
sys.exit(rc)
'''

RUNNER_PADRE = '''import json, os, subprocess, sys
from pathlib import Path
salida, patron = Path(sys.argv[1]), sys.argv[2]
yo = str(os.getpid())
con_a = yo in subprocess.run(["pgrep", "-a", "-f", patron], capture_output=True, text=True).stdout.split()
sin_a = yo in subprocess.run(["pgrep", "-f", patron], capture_output=True, text=True).stdout.split()
rc = subprocess.run(sys.argv[3:]).returncode
salida.write_text(json.dumps({"pgrep_a_lo_ve": con_a, "pgrep_sin_a_lo_ve": sin_a, "rc": rc}) + "\\n", encoding="utf-8")
sys.exit(rc)
'''


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--cli-falso", type=Path, required=True)
    ap.add_argument("--entradas", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--sesiones", type=Path, required=True)
    ap.add_argument("--pruebas", type=Path, required=True)
    ap.add_argument("--resultado", type=Path, required=True)
    a = ap.parse_args()
    if not os.environ.get("BANCO_VENV_VECTOR"):
        raise SystemExit("falta BANCO_VENV_VECTOR en el entorno")
    path0 = os.environ["PATH"]
    ent = {k: a.entradas / f"entrada_juguete_{k}.json" for k in ("A", "B", "C")}
    res = {"unidad": "U-BANCO-R5-a — corrida en seco del lanzador del lote r5 (USD 0)", "patron_de_prueba": PATRON,
           "entradas": {k: {"ruta": LA.rel_repo(p), "sha256": sha_archivo(p)} for k, p in ent.items()},
           "configs": {k: {"ruta": c, "sha256": sha_archivo(BANCO_DIR / c), "corte_R5": LA.cargar(BANCO_DIR / c)["corte_R5"]}
                       for k, c in CFG.items()},
           "modulos": {n: {"ruta": LA.rel_repo(m.__file__), "sha256": sha_archivo(Path(m.__file__))}
                       for n, m in (("lanzar_lote_paralelo_r5", R5L), ("lanzar_lote_paralelo", BASE), ("guardas_lote_r5", G),
                                    ("guardas_lote", sys.modules["guardas_lote"]), ("lanzar_agente", LA))}}

    # D0. El CLI falso y el token de prueba
    os.environ["PATH"] = "/usr/bin:/bin"
    sin_cli = None
    try:
        R5L.fijar_patron_de_prueba(TOKEN)
    except SystemExit as ex:
        sin_cli = str(ex)
    os.environ["PATH"] = f"{a.cli_falso.resolve()}:{path0}"
    os.environ["ANTHROPIC_API_KEY"] = CLAVE_DE_RELLENO
    os.environ["ANTHROPIC_BASE_URL"] = URL_CERRADA
    quien = shutil.which("claude")
    version = subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
    if Path(quien or "").resolve() != (a.cli_falso / "claude").resolve() or "falso" not in version:
        raise SystemExit("ABORTO: el `claude` del PATH no es el CLI falso")
    rechazos = {}
    for t in ("correr_b63", "rcinco_correr_prueba", "rcinco_juez_prueba", "Rcinco_prueba_paso", "corto", "xrun_posthoc",
              "ensamblar_tanda0"):
        try:
            R5L.fijar_patron_de_prueba(t)
            rechazos[t] = None
        except SystemExit as ex:
            rechazos[t] = str(ex)
    res["D0"] = {"claude_del_PATH": LA.rel_repo(quien), "version_cli": version, "ANTHROPIC_BASE_URL": URL_CERRADA,
                 "sin_cli_falso": sin_cli, "tokens_rechazados": rechazos, "patron_vigente_tras_los_rechazos": G.PATRON_PAGO,
                 "OK": bool(sin_cli) and all(rechazos.values()) and G.PATRON_PAGO == G.PATRON_PAGO_REAL}

    out, ses = a.out, a.sesiones
    # D1 y D2. Los dos R5 admitidos
    for k, planes in (("A", ["S01-fragmentos", "S02-fragmentos", "S04-fragmentos"]),
                      ("B", ["S05-fragmentos", "S06-fragmentos", "S01-fragmentos"])):
        lote = escribir_lote(a.pruebas / "lotes" / f"lote_{k}.json", k, planes)
        c = en_proceso(k, argv_lote(ent[k], lote, out / k, ses / k, k, P=3))
        r = resumen(c, ses / k)
        r5s = sesiones_con_r5(out / k, c["registro"], k, lote) if c["registro"] else {}
        esperado = R5[k]
        r |= {"por_sesion": r5s, "patron_vigente": c["patron_vigente"]}
        r["OK"] = (c["rc"] == 0 and r["codigo"] == 0 and r["R5_de_la_entrada"] == esperado and r["admitido"] is True
                   and r["clave"] == "R5" and r["presupuesto_por_sesion_usd"] == esperado["max_budget_usd"]
                   and r["presupuesto_efectivo_de_la_guarda_usd"] == esperado["max_budget_usd"]
                   and r["estados"] == {"terminada": 3} and r["maximo_a_la_vez"] == 3
                   and all(v == esperado for v in r["r5_por_sesion"].values()) and len(r["r5_por_sesion"]) == 3
                   and all(x["max_turns"] == str(esperado["max_turns"]) and x["max_budget_usd"] == str(esperado["max_budget_usd"])
                           and x["tope_en_la_meta"] == esperado["tope_tool_calls_prompt"] and x["prompt_es_el_de_la_config"]
                           and x["completa_R3"] for x in r5s.values())
                   and r["guardas_de_otro_paso_pago"] == [{"tanda": 1, "hallados": []}]
                   and "data/experiment/banco_mcp/paralelo/guardas_lote_r5.py" in r["lanzador_del_lote"]
                   and r["lanzador_r5"] == ["data/experiment/banco_mcp/agentes/lanzar_lote_paralelo_r5.py"]
                   and c["patron_vigente"] == PATRON)
        res[f"D{1 if k == 'A' else 2}_{k}"] = r

    # D3. Un tercer R5
    lote = escribir_lote(a.pruebas / "lotes" / "lote_C.json", "C", ["S01-fragmentos", "S02-fragmentos"])
    c = en_proceso("A", argv_lote(ent["C"], lote, out / "C", ses / "C", "A", P=2))
    r = resumen(c, ses / "C")
    r["carpetas_de_salida_de_sesiones"] = sorted(p.name for p in (out / "C").iterdir() if p.is_dir()) if (out / "C").is_dir() else []
    r["OK"] = (c["rc"] == 5 and r["codigo"] == 5 and r["admitido"] is False and r["R5_de_la_entrada"] != R5["A"]
               and r["lanzadas"] == 0 and r["estados"] == {"no lanzada": 2} and r["carpetas_de_configuracion_creadas"] == 0
               and not r["carpetas_de_salida_de_sesiones"] and "no es uno de los admitidos" in (r["freno"] or ""))
    res["D3_C"] = r

    # D4. Otro sha256 de la entrada
    c = en_proceso("A", argv_lote(ent["A"], lote, out / "sha", ses / "sha", "A", sha_entrada=sha_archivo(ent["B"])))
    r = resumen(c, ses / "sha")
    r["OK"] = c["rc"] == 3 and r["registro"] is None and not (out / "sha").exists() and r["carpetas_de_configuracion_creadas"] == 0 \
        and any("sha256" in l for l in r["lineas_freno"])
    res["D4_otro_sha256"] = r

    # D5. Una sesión con otro R5 que el de la entrada
    for k, cfg in (("A", "B"), ("B", "A")):
        nombre = f"entrada_{k}_sesiones_{cfg}"
        lote = escribir_lote(a.pruebas / "lotes" / f"lote_{nombre}.json", f"M{k}", ["S02-fragmentos", "S04-fragmentos"])
        c = en_proceso(cfg, argv_lote(ent[k], lote, out / nombre, ses / nombre, cfg, P=1))
        r = resumen(c, ses / nombre)
        r["OK"] = (c["rc"] == 5 and r["codigo"] == 5 and r["R5_de_la_entrada"] == R5[k] and r["admitido"] is True
                   and r["estados"] == {"no lanzada": 1, "terminada": 1}
                   and list(r["r5_por_sesion"].values()) == [R5[cfg]] and "distinto de" in (r["freno"] or "")
                   and (k == "B" or "pasa el presupuesto" in (r["freno"] or "")))
        res[f"D5_{nombre}"] = r

    # D6. --presupuesto-sesion explícito
    lote = escribir_lote(a.pruebas / "lotes" / "lote_presupuesto.json", "P", ["S05-fragmentos"])
    c1 = en_proceso("B", argv_lote(ent["B"], lote, out / "pres_1_8", ses / "pres_1_8", "B", extra=("--presupuesto-sesion", "1.8")))
    c2 = en_proceso("B", argv_lote(ent["B"], lote, out / "pres_3_3", ses / "pres_3_3", "B", extra=("--presupuesto-sesion", "3.3")))
    r1, r2 = resumen(c1, ses / "pres_1_8"), resumen(c2, ses / "pres_3_3")
    res["D6_presupuesto"] = {"distinto_1_8": r1, "igual_3_3": r2,
                             "OK": c1["rc"] == 3 and r1["registro"] is None and r1["carpetas_de_configuracion_creadas"] == 0
                             and c2["rc"] == 0 and r2["presupuesto_por_sesion_usd"] == 3.3 and r2["estados"] == {"terminada": 1}}

    # D7. Un hermano vivo con un nombre del patrón
    proc = a.pruebas / "procesos"
    lote = escribir_lote(a.pruebas / "lotes" / "lote_guarda.json", "G", ["S01-fragmentos"])
    d7 = {}
    for nombre in (f"{TOKEN}.py", f"{TOKEN}_b63.py"):
        g = guion(proc / "hermanos" / nombre)
        pr = Prueba([sys.executable, "-B", str(g)])
        pid = pr.p.pid
        vivo = {"pgrep_para_esperar_lo_ve": pid in G.pgrep(PATRON), "guarda_cli": guarda_cli()}
        sub = subproceso("A", argv_lote(ent["A"], lote, out / f"vivo_{nombre[:-3]}", ses / f"vivo_{nombre[:-3]}", "A"))
        vivo["lote"] = resumen(sub, ses / f"vivo_{nombre[:-3]}")
        rc = pr.cerrar()
        cerrado = {"rc_del_hermano_al_cerrarle_la_entrada": rc, "pgrep_para_esperar_lo_ve": pid in G.pgrep(PATRON),
                   "guarda_cli": guarda_cli()}
        d7[nombre] = {"vivo": vivo, "cerrado": cerrado,
                      "OK": (vivo["pgrep_para_esperar_lo_ve"] and vivo["guarda_cli"]["rc"] == 7
                             and any(nombre in l for l in vivo["guarda_cli"]["lineas"])
                             and vivo["lote"]["rc"] == 7 and vivo["lote"]["codigo"] == 7 and vivo["lote"]["lanzadas"] == 0
                             and vivo["lote"]["carpetas_de_configuracion_creadas"] == 0
                             and vivo["lote"]["guardas_de_otro_paso_pago"] == [{"tanda": 1, "hallados": [nombre]}]
                             and rc == 0 and not cerrado["pgrep_para_esperar_lo_ve"] and cerrado["guarda_cli"]["rc"] == 0)}
    sub = subproceso("A", argv_lote(ent["A"], lote, out / "cerrados", ses / "cerrados", "A"))
    d7["despues_de_cerrarlos"] = resumen(sub, ses / "cerrados")
    d7["OK"] = (all(d7[n]["OK"] for n in (f"{TOKEN}.py", f"{TOKEN}_b63.py")) and d7["despues_de_cerrarlos"]["rc"] == 0
                and d7["despues_de_cerrarlos"]["estados"] == {"terminada": 1})
    res["D7_hermano"] = d7

    # D8. Los ancestros con un nombre del patrón
    d8 = {}
    en_su_proceso = guion(proc / "ancestros" / f"{TOKEN}_b63.py", RUNNER_EN_PROCESO)
    padre = guion(proc / "ancestros" / f"{TOKEN}.py", RUNNER_PADRE)
    s1 = a.pruebas / "salida_runner_en_su_proceso.json"
    argv1 = argv_lote(ent["A"], lote, out / "ancestro_en_su_proceso", ses / "ancestro_en_su_proceso", "A")
    r = subprocess.run([sys.executable, "-B", str(en_su_proceso), str(BANCO_DIR / "agentes" / "lanzar_lote_paralelo_r5.py"),
                        str(s1), TOKEN, *argv1], capture_output=True, text=True, env=dict(os.environ) | {"RCINCO_CONFIG_AGENTES": CFG["A"]})
    d8["runner_que_corre_el_lote_en_su_proceso"] = {"rc": r.returncode, **(json.loads(s1.read_text()) if s1.is_file() else {}),
                                                    "lote": resumen({"rc": r.returncode, "registro": leer_registro(out / "ancestro_en_su_proceso"),
                                                                     "salida": r.stdout.splitlines()}, ses / "ancestro_en_su_proceso")}
    s2 = a.pruebas / "salida_runner_padre.json"
    argv2 = argv_lote(ent["A"], lote, out / "ancestro_padre", ses / "ancestro_padre", "A")
    sub = subproceso("A", argv2, prefijo=[sys.executable, "-B", str(padre), str(s2), PATRON])
    d8["runner_que_lanza_el_lote_como_hijo"] = {"rc": sub["rc"], **(json.loads(s2.read_text()) if s2.is_file() else {}),
                                                "lote": resumen(sub, ses / "ancestro_padre")}
    d8["OK"] = (all(x["rc"] == 0 and x.get("pgrep_a_lo_ve") is True and x["lote"]["estados"] == {"terminada": 1}
                    and x["lote"]["guardas_de_otro_paso_pago"] == [{"tanda": 1, "hallados": []}] for x in d8.values())
                and d8["runner_que_corre_el_lote_en_su_proceso"].get("es_un_proceso_del_patron") is True)
    res["D8_ancestros"] = d8

    # D9. Otras guardas y otros procesos que nombran el patrón
    espera = guion(proc / "otros" / "espera_otra_guarda.py")
    sin_escape = PATRON.replace("\\", "")
    otros = {"pgrep_de_otra_guarda": Prueba(["pgrep", "-c", "import sys; sys.stdin.read()", "-f", sin_escape], executable=sys.executable),
             "python_que_espera_con_el_patron": Prueba([sys.executable, "-B", str(espera), "--patron", sin_escape]),
             "shell_que_lo_nombra": Prueba(["/bin/sh", "-c", "read x", f"{TOKEN}_b63.py"])}
    vistos = G.pgrep(PATRON)
    d9 = {"pgrep_ve": {k: p.p.pid in vistos for k, p in otros.items()}, "guarda_cli": guarda_cli()}
    sub = subproceso("A", argv_lote(ent["A"], lote, out / "otras_guardas", ses / "otras_guardas", "A"))
    d9["lote"] = resumen(sub, ses / "otras_guardas")
    d9["rc_al_cerrarles_la_entrada"] = {k: p.cerrar() for k, p in otros.items()}
    d9["OK"] = (all(d9["pgrep_ve"].values()) and d9["guarda_cli"]["rc"] == 0 and d9["lote"]["rc"] == 0
                and d9["lote"]["estados"] == {"terminada": 1} and d9["lote"]["guardas_de_otro_paso_pago"] == [{"tanda": 1, "hallados": []}])
    res["D9_otras_guardas"] = d9

    os.environ["PATH"] = path0
    ok = {k: v["OK"] for k, v in res.items() if k.startswith("D")}
    res["resumen"] = {"OK": sum(ok.values()), "FALLA": [k for k, v in ok.items() if not v], "total": len(ok),
                      "acumulado_R9_usd_de_juguete": round(sum(v.get("acumulado_R9_usd", 0) or 0 for k, v in res.items()
                                                              if k.startswith(("D1", "D2"))), 6)}
    a.resultado.parent.mkdir(parents=True, exist_ok=True)
    a.resultado.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in ok.items():
        print(f"{k}: {'OK' if v else 'FALLA'}")
    print(f"corrida en seco: {res['resumen']['OK']}/{res['resumen']['total']} OK")
    return 0 if not res["resumen"]["FALLA"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
