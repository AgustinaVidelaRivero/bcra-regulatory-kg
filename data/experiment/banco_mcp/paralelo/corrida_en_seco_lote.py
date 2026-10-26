#!/usr/bin/env python3
"""corrida_en_seco_lote.py — La corrida en seco del lanzador en paralelo (U-BANCO-PARALELO, punto 4.c), a USD 0.

Importa agentes/lanzar_lote_paralelo.py (por su ruta, sin tocar el sys.path por fuera: el módulo agrega las suyas, como
en la corrida real) y llama a su `main`, en modo real, con el CLI falso (paralelo/cli_falso/claude) primero en el PATH y
una clave de relleno que no es una clave: el lote corre el mismo camino que el real (el lanzador de una sesión de N6,
LA.preparar_sesion, LA.env_sesion, `claude`, el servidor MCP de cada brazo con sus llamadas reales, LA.copiar_sesion,
LA.armar_meta), y ninguna petición sale a la API.

  A. un lote de 12 sesiones (6 por brazo: 6 del grafo con el servidor de navegación y 6 de fragmentos, 3 BM25 y 3
     híbridas), intercalado por pregunta con los dos brazos seguidos en cada bloque, con P = 3. Una sesión (S03, BM25)
     falla a mitad por su plan; la fecha de cada sesión es la del reloj del lanzador al empezarla, y acá ese reloj se
     fija (LOTE.RELOJ_FECHA) para que cruce la medianoche en la octava, dentro del bloque S04;
  B. el mismo lote con P = 1: las mismas salidas por sesión (por sha256, desde el log R1 y la meta);
  C. el mismo lote con la guarda del gasto, que corta antes del freno (P = 3, presupuesto 1,80, freno 2,00, tope 2,50);
  D. la guarda de otro paso pago, en el lote y en el humo: con un proceso de prueba propio vivo
     (`python3 <tmp>/correr_prueba_T_v2.py`, y otro con un nombre del patrón de A2.2, `correr_a2_2.py`) que solo espera su
     entrada estándar, frenan sin lanzar nada; al cerrarles la entrada, dejan pasar; un shell, un `grep` o un editor que
     nombren el script no los hacen frenar;
  E. el control de la extracción, con el patrón de la §198: con `python3 <tmp>/runner_corpus.py` vivo, frena, y con
     `python3 "<tmp>/con espacio/runner_corpus.py"` también; al cerrarles la entrada, deja pasar; un shell, un `grep`, un
     editor y `python3 <tmp>/otro.py <tmp>/runner_corpus.py` no lo hacen frenar;
  F. el patrón de la guarda de otro paso pago es el del renglón 16 de a2_2/guardas_a2_2.zsh más correr_prueba_T_v2\\.py;
  G. la guarda de la versión del CLI: con el falso que no cambia (A y B) deja pasar; frena (código 6) con el que cambia la
     versión de su system/init a mitad del lote, con uno cuyo `--version` no es la sellada y con uno cuyo enlace `claude`
     cambia de destino a mitad del lote;
  H. el humo, de punta a punta (comandos/humo_lote_paralelo.zsh, con tope USD 8 y freno USD 6, su Neo4j propio y una
     clave de relleno en un archivo de entorno de --tmp), con el CLI falso y su lote con la marca de un plan de unos
     USD 0,90 por sesión: lanza tres a la vez y la guarda del gasto corta antes del freno.

La espera es la del proceso padre sobre sus hijos (Popen.wait): sin sleep. El resultado, solo cuentas, sha256 y
banderas, va a --resultado; ninguna salida de tool se imprime ni se escribe ahí.

Uso: corrida_en_seco_lote.py --out <dir> --sesiones <dir> --tmp <dir> --resultado <json> --humo <humo.zsh>
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
CLI_FALSO = AQUI / "cli_falso"
LANZADOR_N6 = "paralelo/lanzar_agente_n6_prueba.py"
CLAVE_DE_RELLENO = "sin-clave-corrida-en-seco"


def importar(nombre: str, ruta: Path):
    spec = importlib.util.spec_from_file_location(nombre, ruta)
    m = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = m
    spec.loader.exec_module(m)
    return m


LOTE = importar("lanzar_lote_paralelo", BANCO_DIR / "agentes" / "lanzar_lote_paralelo.py")
G = sys.modules["guardas_lote"]
LA = sys.modules["lanzar_agente"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def lote_seco() -> list[dict]:
    ses = []
    for k in range(1, 7):
        b = f"S{k:02d}"
        fr = "fragmentos_bm25" if k % 2 else "fragmentos_hibrida"
        ses.append({"id": f"{b}-kg", "brazo": "kg", "bloque": b,
                    "pregunta": f"Pregunta {b} de la corrida en seco [[seco:{b}-kg]]"})
        ses.append({"id": f"{b}-{fr}", "brazo": fr, "bloque": b,
                    "pregunta": f"Pregunta {b} de la corrida en seco [[seco:{b}-fragmentos]]"})
    return ses


def escribir_lote(p: Path, ses: list[dict]) -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps({"sesiones": ses}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return p


def reloj_que_cruza_la_medianoche(n_cambio: int):
    """Un reloj para la fecha de cada sesión: las primeras n_cambio-1 que empiezan, el 26/10/2026 a las 23:59 (hora
    local); desde la n_cambio, el 27/10/2026 a las 00:01."""
    antes, despues, k = datetime(2026, 10, 26, 23, 59).timestamp(), datetime(2026, 10, 27, 0, 1).timestamp(), [0]

    def reloj() -> float:
        k[0] += 1
        return antes if k[0] < n_cambio else despues
    return reloj


def correr_lote(lote: Path, out: Path, sesiones: Path, P: int, tope: float, freno: float) -> tuple[int, dict]:
    rc = LOTE.main(["--lote", str(lote), "--out", str(out), "--sesiones", str(sesiones), "-P", str(P), "--modo", "real",
                    "--tope", str(tope), "--freno", str(freno), "--lanzador", LANZADOR_N6])
    return rc, json.loads((out / "registro_lote.json").read_text(encoding="utf-8"))


def salidas_por_sesion(out: Path, ids: list[str], reg: dict) -> dict:
    """Por sesión, lo que tiene que dar igual con cualquier P: las llamadas del log R1 (tool, input, sha256 y largo de la
    salida, error), si el log cerró, R3, el JSON final, el costo R9 y la fecha. Solo sha256 y cuentas."""
    res = {}
    fecha = {s["id"]: s.get("fecha") for s in reg["sesiones"]}
    for i in ids:
        d = out / i
        lg = d / f"log_r1_{i}.jsonl"
        lineas = [json.loads(x) for x in lg.read_text(encoding="utf-8").splitlines() if x.strip()] if lg.exists() else []
        llamadas = [[x["n"], x["tool"], x["input"], x["output_sha256"], x["output_chars"], x["error"]]
                    for x in lineas if x["evento"] == "llamada"]
        mp = d / f"meta_{i}.json"
        m = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {}
        res[i] = {"llamadas_sha256": sha(json.dumps(llamadas, ensure_ascii=False, sort_keys=True).encode()),
                  "n_llamadas": len(llamadas), "log_con_fin": any(x["evento"] == "fin" for x in lineas),
                  "completa_R3": (m.get("completitud_R3") or {}).get("completa"),
                  "motivos_R3": (m.get("completitud_R3") or {}).get("motivos_incompleta"),
                  "mapa_R7_ok": all(x["coincide_tool_input"] for x in m.get("mapa_R7", [])) if m else None,
                  "final_json_sha256": sha(json.dumps(m.get("final_json_R4"), sort_keys=True).encode()) if m else None,
                  "costo_R9_usd": ((m.get("tokens_R9") or {}).get("costo_recomputado") or {}).get("total_usd"),
                  "fecha": fecha.get(i)}
    return res


def controles_registro(reg: dict, P: int) -> dict:
    ses = reg["sesiones"]
    lanzas = [e for e in reg["eventos"] if e["evento"] == "lanza"]
    cwd = [e for e in reg["eventos"] if e["evento"] == "control del cwd compartido"]
    cfgs = [s.get("carpeta_configuracion") for s in ses if s.get("carpeta_configuracion")]
    fuera = all(not LOTE.ruta_de_rel(c).resolve().is_relative_to(LA.REPO_DIR)
                and LA.dentro_de_git(LOTE.ruta_de_rel(c).resolve()) is None for c in cfgs)
    return {"codigo": reg["codigo"], "n_sesiones": len(ses),
            "estados": {e: sum(1 for s in ses if s["estado"] == e) for e in sorted({s["estado"] for s in ses})},
            "orden_de_lanzamiento_es_el_de_la_lista": [e["id"] for e in lanzas] == [s["id"] for s in ses][:len(lanzas)],
            "orden_de_fin": reg["orden_de_fin"],
            "maximo_a_la_vez": max((e["corriendo_con_ella"] for e in lanzas), default=0),
            "workers_usados": sorted({s["worker"] for s in ses if s.get("worker")}),
            "n_superposiciones": len(reg["superposiciones"]),
            "superposiciones_grafo_fragmentos": sum(1 for x in reg["superposiciones"]
                                                    if ("kg" in x["brazos"]) and any(b.startswith("fragmentos") for b in x["brazos"])),
            "controles_del_cwd": [{"cuando": e["cuando"], "vacio": e["vacio"]} for e in cwd],
            "cwd_vacio_en_todos": bool(cwd) and all(e["vacio"] for e in cwd),
            "carpetas_de_configuracion": len(cfgs), "carpetas_distintas": len(set(cfgs)) == len(cfgs),
            "carpetas_fuera_del_repo_y_de_git": fuera,
            "fechas": reg["fechas"]["cambio_de_fecha"],
            "bloques_con_fechas_distintas": reg["fechas"]["bloques_con_fechas_distintas_entre_brazos"],
            "acumulado_R9_usd": reg["acumulado_R9_usd"], "acumulado_de_la_guarda_usd": reg["acumulado_de_la_guarda_usd"],
            "sin_result": [s["id"] for s in ses if s.get("sin_result")],
            "version_cli": {"sellada": reg["cli"]["version_sellada"], "controles": len(reg["cli"]["controles"]),
                            "todos_bien": all(c["ok"] for c in reg["cli"]["controles"]),
                            "version_init_por_sesion": sorted({str(s.get("version_cli_init")) for s in ses if s.get("t_fin")})},
            "R3_por_sesion": {s["id"]: s.get("completa_R3") for s in ses}}


class Prueba:
    """Un proceso propio que solo espera su entrada estándar (sin sleep); al cerrarla, termina y el padre lo espera."""

    def __init__(self, argv: list[str]):
        self.argv = argv
        self.p = subprocess.Popen(argv, stdin=subprocess.PIPE, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def cerrar(self) -> int:
        self.p.stdin.close()
        return self.p.wait()


def guion_de_prueba(tmp: Path, nombre: str) -> Path:
    p = tmp / nombre
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("import sys\nsys.stdin.read()\n", encoding="utf-8")
    return p


def lote_un_fragmento(out: Path, nombre: str) -> Path:
    return escribir_lote(out / f"lote_{nombre}.json", [{"id": f"G-{nombre}", "brazo": "fragmentos_bm25", "bloque": "G",
                                                        "pregunta": "Pregunta de la guarda [[seco:S01-fragmentos]]"}])


def lote_subproceso(lote: Path, out: Path, sesiones: Path) -> dict:
    """El lote como proceso aparte (así los procesos de prueba, hijos de esta corrida, no son de su árbol)."""
    r = subprocess.run([sys.executable, "-B", str(BANCO_DIR / "agentes" / "lanzar_lote_paralelo.py"), "--lote", str(lote),
                        "--out", str(out), "--sesiones", str(sesiones), "-P", "1", "--modo", "real", "--tope", "2.5",
                        "--freno", "2", "--lanzador", LANZADOR_N6], capture_output=True, text=True)
    reg = json.loads((out / "registro_lote.json").read_text(encoding="utf-8")) if (out / "registro_lote.json").exists() else {}
    guardas = [e for e in reg.get("eventos", []) if e["evento"] == "guarda de otro paso pago"]
    return {"rc": r.returncode, "lanzadas": sum(1 for s in reg.get("sesiones", []) if s["estado"] != "no lanzada"),
            "sesiones_creadas": len(list((sesiones / "config").glob("*"))) if (sesiones / "config").exists() else 0,
            "hallados": [h["script"] for e in guardas for h in e["hallados"]],
            "salida_frena": [l for l in r.stdout.splitlines() if l.startswith("FRENO")]}


def humo_subproceso(humo: Path, *args: str) -> dict:
    r = subprocess.run(["/bin/zsh", str(humo), *args], capture_output=True, text=True)
    return {"rc": r.returncode, "lineas": [l for l in r.stdout.splitlines() if l.startswith(("FRENO", "guarda", "control", "solo"))]}


def guarda_cli(cual: str) -> dict:
    """La guarda como proceso aparte (la CLI que usa el humo): su código y sus líneas (pid y nombre del script)."""
    r = subprocess.run([sys.executable, "-I", "-B", str(AQUI / "guardas_lote.py"), cual], capture_output=True, text=True)
    return {"rc": r.returncode, "lineas": r.stdout.splitlines()}


def docker_estado() -> list[str]:
    r = subprocess.run(["docker", "ps", "-a", "--format", "{{.Names}}\t{{.State}}"], capture_output=True, text=True)
    return sorted(r.stdout.splitlines())


def prueba_guardas(a, out: Path, ses_raiz: Path) -> dict:
    tmp = a.tmp
    res = {}
    humo_dirs_antes = sorted(p.name for p in (a.humo.parent.parent / "salidas").glob("humo_*"))
    dk_antes = docker_estado()
    # D. otro paso pago: el del registro (§118) y uno del patrón de A2.2
    for nombre in ("correr_prueba_T_v2.py", "correr_a2_2.py"):
        g = guion_de_prueba(tmp, nombre)
        pr = Prueba(["python3", str(g)])
        con = {"lote": lote_subproceso(lote_un_fragmento(out, f"vivo_{nombre[:-3]}"), out / f"vivo_{nombre[:-3]}",
                                       ses_raiz / f"vivo_{nombre[:-3]}"),
               "humo": humo_subproceso(a.humo, "/no/existe/entorno_de_la_clave"),
               "humo_solo_guardas": humo_subproceso(a.humo, "--solo-guardas"),
               "pid_de_prueba": pr.p.pid}
        rc = pr.cerrar()
        sin = {"rc_del_proceso_de_prueba_al_cerrarle_la_entrada": rc,
               "lote": lote_subproceso(lote_un_fragmento(out, f"cerrado_{nombre[:-3]}"), out / f"cerrado_{nombre[:-3]}",
                                       ses_raiz / f"cerrado_{nombre[:-3]}"),
               "humo_solo_guardas": humo_subproceso(a.humo, "--solo-guardas")}
        res[nombre] = {"con_el_proceso_vivo": con, "despues_de_cerrarlo": sin,
                       "OK": (con["lote"]["rc"] == G.CODIGO_PAGO and con["lote"]["lanzadas"] == 0
                              and con["lote"]["sesiones_creadas"] == 0 and nombre in con["lote"]["hallados"]
                              and con["humo"]["rc"] == G.CODIGO_PAGO and con["humo_solo_guardas"]["rc"] == G.CODIGO_PAGO
                              and sin["lote"]["rc"] == 0 and sin["lote"]["lanzadas"] == 1
                              and sin["humo_solo_guardas"]["rc"] == 0)}
    # un shell, un grep y un editor que nombran el script
    g = guion_de_prueba(tmp, "correr_prueba_T_v2.py")
    nombran = [Prueba(["/bin/sh", "-c", "read x; : correr_prueba_T_v2.py", "sh"]),
               Prueba(["/bin/zsh", "-c", "read x; : correr_a2_2.py"]),
               Prueba(["/usr/bin/grep", "correr_prueba_T_v2.py"]),
               Prueba(["/bin/ed", "-s", str(g)])]
    pg = subprocess.run(["pgrep", "-f", G.PATRON_PAGO], capture_output=True, text=True).stdout.split()
    pids_nombran = [x.p.pid for x in nombran]
    cli = guarda_cli("pago")
    lt = lote_subproceso(lote_un_fragmento(out, "nombran"), out / "nombran", ses_raiz / "nombran")
    hm = humo_subproceso(a.humo, "--solo-guardas")
    rcs = [x.cerrar() for x in nombran]
    res["shell_grep_editor_que_nombran_el_script"] = {
        "procesos": ["sh -c (nombra correr_prueba_T_v2.py)", "zsh -c (nombra correr_a2_2.py)", "grep correr_prueba_T_v2.py",
                     "ed -s <tmp>/correr_prueba_T_v2.py"],
        "pgrep_ve_de_ellos": sum(1 for q in pg if int(q) in pids_nombran), "guarda_cli": cli, "lote": lt,
        "humo_solo_guardas": hm, "rc_al_cerrarlos": rcs,
        "OK": (sum(1 for q in pg if int(q) in pids_nombran) == len(nombran) and cli["rc"] == 0 and lt["rc"] == 0
               and lt["lanzadas"] == 1 and hm["rc"] == 0)}
    res["humo_no_lanzo_nada"] = {
        "carpetas_de_salida_del_humo_antes": humo_dirs_antes,
        "carpetas_de_salida_del_humo_despues": sorted(p.name for p in (a.humo.parent.parent / "salidas").glob("humo_*")),
        "docker_igual": docker_estado() == dk_antes}
    res["humo_no_lanzo_nada"]["OK"] = (res["humo_no_lanzo_nada"]["carpetas_de_salida_del_humo_antes"]
                                       == res["humo_no_lanzo_nada"]["carpetas_de_salida_del_humo_despues"]
                                       and res["humo_no_lanzo_nada"]["docker_igual"])
    return res


def prueba_extraccion(a) -> dict:
    tmp = a.tmp
    cli = [sys.executable, "-I", "-B", str(AQUI / "guardas_lote.py"), "extraccion"]
    g = guion_de_prueba(tmp, "runner_corpus.py")
    pr = Prueba(["python3", str(g)])
    con = {"hallados": G.extraccion_corriendo(), "rc_cli": subprocess.run(cli, capture_output=True, text=True).returncode}
    rc = pr.cerrar()
    sin = {"hallados": G.extraccion_corriendo(), "rc_cli": subprocess.run(cli, capture_output=True, text=True).returncode}
    # la ruta con un espacio, como la del repo (el patrón de la §198 la ve)
    ge = guion_de_prueba(tmp / "con espacio", "runner_corpus.py")
    pe = Prueba(["python3", str(ge)])
    esp = {"hallados": G.extraccion_corriendo(), "control_de_la_extraccion": guarda_cli("extraccion"),
           "guarda_de_otro_paso_pago": guarda_cli("pago"), "pid_de_prueba": pe.p.pid}
    esp["rc_al_cerrarle_la_entrada"] = pe.cerrar()
    esp["despues_de_cerrarlo"] = guarda_cli("extraccion")
    # los que no tienen que frenar: un shell, un grep, un editor y un python con otro script que nombra runner_corpus.py
    otro = guion_de_prueba(tmp, "otro.py")
    nombran = [Prueba(["/bin/sh", "-c", "read x; : runner_corpus.py", "sh"]), Prueba(["/usr/bin/grep", "runner_corpus.py"]),
               Prueba(["/bin/ed", "-s", str(g)]), Prueba(["python3", str(otro), str(g)])]
    t = G.tabla_procesos()
    nom = {"procesos": ["sh -c (nombra runner_corpus.py)", "grep runner_corpus.py", "ed -s <tmp>/runner_corpus.py",
                        "python3 <tmp>/otro.py <tmp>/runner_corpus.py"],
           "los_cuatro_nombran_runner_corpus": all("runner_corpus.py" in t.get(x.p.pid, (0, ""))[1] for x in nombran),
           "hallados": G.extraccion_corriendo(), "rc_cli": subprocess.run(cli, capture_output=True, text=True).returncode}
    nom["rc_al_cerrarlos"] = [x.cerrar() for x in nombran]
    return {"patron": G.PATRON_EXTRACCION, "con_el_proceso_vivo": con | {"pid_de_prueba": pr.p.pid},
            "rc_del_proceso_al_cerrarle_la_entrada": rc, "despues_de_cerrarlo": sin, "ruta_con_espacio": esp,
            "que_no_tienen_que_frenar": nom,
            "OK": (len(con["hallados"]) == 1 and con["hallados"][0]["script"] == "runner_corpus.py"
                   and con["rc_cli"] == G.CODIGO_EXTRACCION and not sin["hallados"] and sin["rc_cli"] == 0
                   and len(esp["hallados"]) == 1 and esp["control_de_la_extraccion"]["rc"] == G.CODIGO_EXTRACCION
                   and esp["despues_de_cerrarlo"]["rc"] == 0
                   and nom["los_cuatro_nombran_runner_corpus"] and not nom["hallados"] and nom["rc_cli"] == 0)}


def prueba_version(a, out: Path, ses_raiz: Path, ses: list[dict]) -> dict:
    """G. La guarda de la versión del CLI: frena con el falso que cambia (de versión en su system/init, de `--version` o
    del destino de su enlace) y no con el que no cambia (los lotes A y B)."""
    tmp, res, path0 = a.tmp, {}, os.environ["PATH"]
    # G1. la versión de system/init cambia a mitad del lote (S03-kg)
    ses1 = [s | {"pregunta": s["pregunta"].replace("[[seco:S03-kg]]", "[[seco:S03-kg-version]]")} for s in ses]
    rc, reg = correr_lote(escribir_lote(out / "lote_version_init.json", ses1), out / "version_init", ses_raiz / "version_init",
                          3, 12, 10)
    est = {e: sum(1 for x in reg["sesiones"] if x["estado"] == e) for e in {x["estado"] for x in reg["sesiones"]}}
    res["cambia_en_system_init"] = {"rc": rc, "freno": reg["freno"], "estados": est,
                                    "OK": rc == LOTE.VERSION_CLI and "S03-kg" in (reg["freno"] or "")
                                    and est.get("no lanzada", 0) > 0}
    # G2. `claude --version` no es la sellada desde el comienzo
    b = tmp / "bin_otra_version"
    b.mkdir(parents=True, exist_ok=True)
    (b / "claude").write_text('#!/bin/sh\nif [ "$1" = "--version" ]; then echo "2.1.250 (CLI falso de prueba de la guarda)"; '
                              f'else exec "{CLI_FALSO / "claude"}" "$@"; fi\n', encoding="utf-8")
    (b / "claude").chmod(0o755)
    os.environ["PATH"] = f"{b}:{path0}"
    try:
        rc, reg = correr_lote(lote_un_fragmento(out, "otra_version"), out / "otra_version", ses_raiz / "otra_version", 1, 2.5, 2)
    finally:
        os.environ["PATH"] = path0
    res["version_distinta_al_empezar"] = {"rc": rc, "freno": reg["freno"],
                                          "lanzadas": sum(1 for x in reg["sesiones"] if x["estado"] != "no lanzada"),
                                          "OK": rc == LOTE.VERSION_CLI and all(x["estado"] == "no lanzada" for x in reg["sesiones"])}
    # G3. el destino del enlace `claude` cambia a mitad del lote (lo cambia S02-kg, por su plan)
    e1, e2 = tmp / "bin_enlace", tmp / "bin_enlace_alt"
    for d in (e1, e2):
        d.mkdir(parents=True, exist_ok=True)
        if (d / "claude").is_symlink() or (d / "claude").exists():
            (d / "claude").unlink()
        (d / "claude").symlink_to(CLI_FALSO / "claude")
    ses3 = [s | {"pregunta": s["pregunta"].replace("[[seco:S02-kg]]", "[[seco:S02-kg-repunta]]")} for s in ses[:4]]
    os.environ["PATH"] = f"{e1}:{path0}"
    try:
        rc, reg = correr_lote(escribir_lote(out / "lote_enlace.json", ses3), out / "enlace", ses_raiz / "enlace", 1, 12, 10)
    finally:
        os.environ["PATH"] = path0
    res["cambia_el_destino_del_enlace"] = {"rc": rc, "freno": reg["freno"],
                                           "lanzadas": sum(1 for x in reg["sesiones"] if x["estado"] != "no lanzada"),
                                           "OK": rc == LOTE.VERSION_CLI and "destino" in (reg["freno"] or "")
                                           and sum(1 for x in reg["sesiones"] if x["estado"] == "no lanzada") == 1}
    return res


def prueba_humo(a, out: Path) -> dict:
    """H. El humo, de punta a punta, con el CLI falso: su lote con la marca de un plan caro, su Neo4j propio (que baja al
    terminar) y una clave de relleno en un archivo de entorno de --tmp."""
    base = json.loads((a.humo.parent / "lote_humo.json").read_text(encoding="utf-8"))["sesiones"]
    ses = [s | {"pregunta": s["pregunta"] + (" [[seco:HUMO-kg]]" if s["brazo"] == "kg" else " [[seco:HUMO-fragmentos]]")}
           for s in base]
    lote = escribir_lote(out / "lote_humo_seco.json", ses)
    entorno = a.tmp / "entorno_de_relleno_humo.txt"
    entorno.write_text(f"ANTHROPIC_API_KEY={CLAVE_DE_RELLENO}\n", encoding="utf-8")
    salidas = a.humo.parent.parent / "salidas"
    antes = {p.name for p in salidas.glob("humo_*")}
    env = {"PATH": os.environ["PATH"], "HOME": os.environ["HOME"], "BANCO_VENV_VECTOR": os.environ["BANCO_VENV_VECTOR"],
           "HUMO_LOTE": str(lote)}
    r = subprocess.run(["/bin/zsh", str(a.humo), str(entorno)], env=env, capture_output=True, text=True)
    nuevas = sorted({p.name for p in salidas.glob("humo_*")} - antes)
    reg = json.loads((salidas / nuevas[0] / "registro_lote.json").read_text(encoding="utf-8")) if nuevas else {}
    lanzas = [e for e in reg.get("eventos", []) if e["evento"] == "lanza"]
    pres = reg.get("presupuesto_efectivo_de_la_guarda_usd", 0)
    peor = [round(e["acumulado"] + pres * e["corriendo_con_ella"], 6) for e in lanzas]
    guarda = [e["decision"] for e in reg.get("eventos", []) if e["evento"] == "guarda del gasto"]
    arriba = subprocess.run(["docker", "ps", "--format", "{{.Names}}"], capture_output=True, text=True).stdout.split()
    return {"rc": r.returncode, "salida": nuevas, "tope": reg.get("tope_usd"), "freno": reg.get("freno_usd"),
            "codigo_del_lote": reg.get("codigo"), "freno_del_lote": reg.get("freno"),
            "maximo_a_la_vez": max((e["corriendo_con_ella"] for e in lanzas), default=0), "lanzadas": len(lanzas),
            "peor_caso_al_lanzar_cada_una": peor, "decisiones_de_la_guarda": guarda,
            "acumulado_de_la_guarda_usd": reg.get("acumulado_de_la_guarda_usd"),
            "lineas": [l for l in r.stdout.splitlines() if l.startswith(("lote:", "humo terminado", "total:", "guarda", "control"))],
            "neo4j_propio_bajado": "neo4j-bcra-kg-banco-paralelo" not in arriba,
            "OK": (bool(nuevas) and reg.get("tope_usd") == 8 and reg.get("freno_usd") == 6
                   and max((e["corriendo_con_ella"] for e in lanzas), default=0) == 3 and all(x <= 6 for x in peor)
                   and (reg.get("acumulado_de_la_guarda_usd") or 0) <= 6 and "espera a que termine una" in guarda
                   and "neo4j-bcra-kg-banco-paralelo" not in arriba)}


def patron_renglon_16() -> dict:
    linea = (BANCO_DIR / "a2_2" / "guardas_a2_2.zsh").read_text(encoding="utf-8").splitlines()[15]
    pat = linea.split("=", 1)[1].strip().strip("'")
    return {"renglon_16": linea, "patron_de_la_guarda": G.PATRON_PAGO,
            "OK": linea.startswith("PATRON=") and G.PATRON_PAGO == pat + r"|correr_prueba_T_v2\.py"}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--sesiones", type=Path, required=True)
    ap.add_argument("--tmp", type=Path, required=True)
    ap.add_argument("--resultado", type=Path, required=True)
    ap.add_argument("--humo", type=Path, required=True)
    ap.add_argument("--solo", choices=["lotes", "guardas", "humo"], default=None)
    a = ap.parse_args()
    for v in ("NEO4J_URI", "BANCO_VENV_VECTOR"):
        if not os.environ.get(v):
            raise SystemExit(f"falta {v} en el entorno")
    os.environ["PATH"] = f"{CLI_FALSO}:{os.environ['PATH']}"
    os.environ["ANTHROPIC_API_KEY"] = CLAVE_DE_RELLENO
    quien = shutil.which("claude")
    version = subprocess.run(["claude", "--version"], capture_output=True, text=True).stdout.strip()
    if Path(quien or "").resolve() != (CLI_FALSO / "claude").resolve() or "falso" not in version:
        raise SystemExit("ABORTO: el `claude` del PATH no es el CLI falso")
    res = {"unidad": "U-BANCO-PARALELO — corrida en seco del lanzador en paralelo (USD 0)",
           "claude_del_PATH": LOTE.rel_repo(quien), "version_cli": version,
           "modulos": {"lanzar_lote_paralelo": LOTE.rel_repo(LOTE.__file__), "lanzar_agente": LOTE.rel_repo(LA.__file__),
                       "guardas_lote": LOTE.rel_repo(G.__file__)},
           "F_patron": patron_renglon_16()}
    ses = lote_seco()
    ids = [s["id"] for s in ses]
    if a.solo in (None, "lotes"):
        lote = escribir_lote(a.out / "lote_seco.json", ses)
        res["lote"] = {"ruta": LOTE.rel_repo(lote), "sha256": sha(lote.read_bytes()), "ids": ids}
        LOTE.RELOJ_FECHA = reloj_que_cruza_la_medianoche(8)
        rcA, regA = correr_lote(lote, a.out / "P3", a.sesiones / "P3", 3, 12, 10)
        LOTE.RELOJ_FECHA = reloj_que_cruza_la_medianoche(8)
        rcB, regB = correr_lote(lote, a.out / "P1", a.sesiones / "P1", 1, 12, 10)
        LOTE.RELOJ_FECHA = None
        sA, sB = salidas_por_sesion(a.out / "P3", ids, regA), salidas_por_sesion(a.out / "P1", ids, regB)
        dist = [i for i in ids if sA[i] != sB[i]]
        cA, cB = controles_registro(regA, 3), controles_registro(regB, 1)
        falla = "S03-fragmentos_bm25"
        res["A_P3"] = cA | {"rc": rcA}
        res["B_P1"] = cB | {"rc": rcB}
        res["A_igual_B"] = {"sesiones_comparadas": len(ids), "distintas": dist, "salidas_por_sesion_P3": sA,
                            "OK": not dist}
        res["sesion_que_falla"] = {"id": falla, "P3": sA[falla], "P1": sB[falla],
                                   "las_otras_completas_P3": sum(1 for i in ids if i != falla and sA[i]["completa_R3"]),
                                   "las_otras_completas_P1": sum(1 for i in ids if i != falla and sB[i]["completa_R3"]),
                                   "OK": (sA[falla]["completa_R3"] is False and sB[falla]["completa_R3"] is False
                                          and all(sA[i]["completa_R3"] and sB[i]["completa_R3"] for i in ids if i != falla))}
        rcC, regC = correr_lote(lote, a.out / "guarda", a.sesiones / "guarda", 3, 2.5, 2.0)
        cC = controles_registro(regC, 3)
        lanzas = [e for e in regC["eventos"] if e["evento"] == "lanza"]
        peor = [round(e["acumulado"] + regC["presupuesto_efectivo_de_la_guarda_usd"] * e["corriendo_con_ella"], 6) for e in lanzas]
        res["C_guarda_del_gasto"] = cC | {"rc": rcC, "freno": regC["freno"], "peor_caso_al_lanzar_cada_una": peor,
                                          "eventos_de_la_guarda": [{k: e[k] for k in ("antes_de", "acumulado", "corriendo",
                                                                                          "con_la_nueva", "decision")}
                                                                   for e in regC["eventos"] if e["evento"] == "guarda del gasto"],
                                          "acumulado_de_la_guarda_usd": regC["acumulado_de_la_guarda_usd"],
                                          "OK": (rcC == LOTE.FRENO_GASTO and regC["acumulado_de_la_guarda_usd"] <= 2.0
                                                 and all(x <= 2.0 for x in peor)
                                                 and cC["estados"].get("no lanzada", 0) > 0)}
        res["A_P3"]["OK"] = (rcA == 0 and cA["maximo_a_la_vez"] == 3 and cA["workers_usados"] == [1, 2, 3]
                             and cA["version_cli"]["todos_bien"] and cA["version_cli"]["version_init_por_sesion"] == ["2.1.241"]
                             and cA["superposiciones_grafo_fragmentos"] > 0 and cA["cwd_vacio_en_todos"]
                             and cA["carpetas_distintas"] and cA["carpetas_fuera_del_repo_y_de_git"]
                             and cA["orden_de_lanzamiento_es_el_de_la_lista"]
                             and (cA["fechas"] or {}).get("bloque") == "S04" and cA["bloques_con_fechas_distintas"] == ["S04"])
        res["B_P1"]["OK"] = (rcB == 0 and cB["maximo_a_la_vez"] == 1 and cB["workers_usados"] == [1]
                             and cB["version_cli"]["todos_bien"]
                             and cB["n_superposiciones"] == 0 and cB["cwd_vacio_en_todos"] and cB["carpetas_distintas"]
                             and (cB["fechas"] or {}).get("bloque") == "S04" and cB["bloques_con_fechas_distintas"] == ["S04"])
    if a.solo in (None, "lotes"):
        res["G_version_del_cli"] = prueba_version(a, a.out / "version", a.sesiones / "version", ses)
    if a.solo in (None, "guardas"):
        res["D_guarda_de_otro_paso_pago"] = prueba_guardas(a, a.out / "guardas", a.sesiones / "guardas")
        res["E_control_de_la_extraccion"] = prueba_extraccion(a)
    if a.solo in (None, "humo"):
        res["H_humo"] = prueba_humo(a, a.out / "humo")
    oks = {k: v["OK"] for k, v in res.items() if isinstance(v, dict) and "OK" in v}
    for grupo, letra in (("D_guarda_de_otro_paso_pago", "D"), ("G_version_del_cli", "G")):
        if grupo in res:
            oks |= {f"{letra}:{k}": v["OK"] for k, v in res[grupo].items()}
    res["OKs"] = oks
    res["OK"] = all(oks.values())
    a.resultado.parent.mkdir(parents=True, exist_ok=True)
    a.resultado.write_text(json.dumps(res, ensure_ascii=False, indent=1).replace(str(a.tmp.resolve()), "<tmp>")
                           .replace(str(a.tmp), "<tmp>").replace(str(Path.home()), "$HOME") + "\n",
                           encoding="utf-8")
    for k, v in oks.items():
        print(f"{k}: {'OK' if v else 'FALLA'}")
    print("TOTAL:", "OK" if res["OK"] else "FALLA")
    return 0 if res["OK"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
