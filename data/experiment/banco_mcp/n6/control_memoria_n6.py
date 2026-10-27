#!/usr/bin/env python3
"""control_memoria_n6.py — Los controles de memoria y de Docker del paso pago de N6 de U-NAV-DISENO (decisiones de la autora del
27/10/2026: los dos lotes, la VM de Docker topeada en 2,5 GB, lo fijo medido después del reinicio y antes de lanzar, y la P del
lote con codificador). USD 0. Los usa el corredor (correr_n6.py): al lanzar, antes del lote con codificador y antes de cada tanda.

  · lo fijo y el swap: memoria_n6.memoria_maquina (vm_stat y sysctl), lo fijo es la memoria en uso de la máquina sin ninguna
    sesión corriendo; con sesiones corriendo, la memoria en uso menos la huella de sus árboles;
  · la huella de una sesión: la de su árbol de procesos, desde su lanzador, por `footprint -p` (memoria_n6.huella), en tres
    partes: el lanzador, el CLI con su Node (todo lo que no es un servidor del banco) y los servidores (los procesos de
    `servidor_mcp_*` y sus hijos, el codificador de consultas incluido). Lee de `ps` solo pid, ppid y la línea de sus propios
    descendientes, para clasificarlos; no la guarda ni la imprime;
  · las P: al lanzar, el lote sin codificador entra si lo fijo más P huellas de una sesión sin codificador llega a 14,5 GB como
    mucho (la huella vale 0,381 GB, la del servidor sin el codificador medida a las 11:09, hasta que el primer lote mida la suya,
    con su CLI); el lote con codificador, con la regla de la decisión 7: P = 2 si lo fijo es de 5,37 GB o menos, y P = 1 si es de
    9,935 o menos. Antes del lote con codificador, otra vez: lo fijo más P veces 4,565 GB (el servidor con el codificador) más la
    huella de CLI más alta del primer lote, hasta 14,5. Antes de cada tanda: lo fijo más P huellas de una sesión del lote;
  · Docker: `docker info --format '{{.MemTotal}}'` hasta 2.684.354.560 bytes, `docker inspect` del contenedor de N6 en
    `healthy`, y `docker stats --no-stream` de ese contenedor, que se registra. No lista nada más de Docker.
Ninguna función frena ni cambia una P: devuelven lo medido y si entra; el corredor decide.
"""
from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
for _p in (str(AQUI), str(AQUI.parent / "paralelo")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import memoria_n6 as MEM                         # noqa: E402
import guardas_lote_n6 as G                      # noqa: E402  (la tabla de procesos de HEAD)

LIMITE_GB = 14.5
HUELLA_SESION_SIN_CODIFICADOR_GB = 0.381         # el servidor sin el codificador, medido a las 11:09 (memoria_N6.json)
HUELLA_SERVIDOR_CON_CODIFICADOR_GB = 4.565       # el servidor con el codificador listo, el pico de memoria_N6.json
UMBRALES_P_CON_CODIFICADOR = {2: 5.37, 1: 9.935}  # la decisión 7: lo fijo hasta el que entra cada P
DOCKER_MEM_TOTAL_MAX = 2_684_354_560
CONTENEDOR = "neo4j-bcra-kg-n6"
GB = 1e9


def maquina() -> dict:
    return MEM.memoria_maquina()


def P_con_que_entra(fijo: float) -> int:
    return max([p for p, u in UMBRALES_P_CON_CODIFICADOR.items() if fijo <= u], default=0)


def P_que_entra(fijo: float, huella: float) -> int:
    return max(0, math.floor((LIMITE_GB - fijo) / huella + 1e-12)) if huella > 0 else 0


def control_al_lanzar(P_sin: int, P_con: int, huella_sin: float = HUELLA_SESION_SIN_CODIFICADOR_GB) -> dict:
    """Lo fijo y el swap, y si entran las dos P (antes de lanzar nada)."""
    m = maquina()
    fijo = m["en_uso_gb"]
    sin = {"P": P_sin, "huella_por_sesion_gb": huella_sin, "necesita_gb": round(fijo + P_sin * huella_sin, 3),
           "P_que_entra": P_que_entra(fijo, huella_sin)}
    sin["entra"] = P_sin >= 1 and sin["necesita_gb"] <= LIMITE_GB
    con = {"P": P_con, "regla": "decisión 7: P = 2 si lo fijo es de 5,37 GB o menos; P = 1 si es de 9,935 o menos",
           "P_que_entra": P_con_que_entra(fijo)}
    con["entra"] = 1 <= P_con <= con["P_que_entra"]
    return {"cuando": "al lanzar", "maquina": m, "lo_fijo_gb": fijo, "swap_gb": m["swap_usado_gb"],
            "sin_codificador": sin, "con_codificador": con, "entra": sin["entra"] and con["entra"]}


def control_lote_con(P_con: int, cli_max: float) -> dict:
    """Antes del lote con codificador, sin ninguna sesión corriendo: lo fijo más P veces el servidor con el codificador más la
    huella de CLI más alta del primer lote."""
    m = maquina()
    fijo = m["en_uso_gb"]
    huella = HUELLA_SERVIDOR_CON_CODIFICADOR_GB + cli_max
    return {"cuando": "antes del lote con codificador", "maquina": m, "lo_fijo_gb": fijo, "swap_gb": m["swap_usado_gb"],
            "P": P_con, "cli_max_gb": cli_max, "huella_por_sesion_gb": round(huella, 3),
            "necesita_gb": round(fijo + P_con * huella, 3), "P_que_entra": min(P_que_entra(fijo, huella), max(UMBRALES_P_CON_CODIFICADOR)),
            "entra": fijo + P_con * huella <= LIMITE_GB}


def control_tanda(P: int, huella_por_sesion: float, corriendo: dict) -> dict:
    """Antes de una tanda: lo fijo (la memoria en uso menos la de las sesiones que corren) más P huellas de una sesión del lote."""
    hs = huellas_de_sesiones(corriendo)
    m = maquina()
    en_sesiones = sum(h["total_gb"] for h in hs.values())
    fijo = round(m["en_uso_gb"] - en_sesiones, 3)
    return {"cuando": "antes de una tanda", "maquina": m, "swap_gb": m["swap_usado_gb"], "sesiones_corriendo": len(corriendo),
            "en_las_sesiones_que_corren_gb": round(en_sesiones, 3), "lo_fijo_gb": fijo, "P": P,
            "huella_por_sesion_gb": round(huella_por_sesion, 3), "necesita_gb": round(fijo + P * huella_por_sesion, 3),
            "entra": fijo + P * huella_por_sesion <= LIMITE_GB, "huellas": hs}


# --------------------------------------------------------------------------- #
# La huella de las sesiones                                                    #
# --------------------------------------------------------------------------- #
def partes_del_arbol(raiz: int, tabla: dict) -> dict[str, set[int]]:
    """Los pids del árbol de una sesión, desde su lanzador: el lanzador, los servidores (procesos `servidor_mcp_*` y sus hijos) y
    el CLI con su Node (lo demás)."""
    todos = G.descendientes(raiz, tabla)
    serv = set()
    for p in todos:
        if p in tabla and "servidor_mcp" in tabla[p][1]:
            serv |= {p} | G.descendientes(p, tabla)
    return {"lanzador": {raiz} if raiz in tabla else set(), "servidores": serv & todos, "cli": todos - serv}


def huellas_de_sesiones(raices: dict) -> dict:
    """{id: {lanzador_gb, cli_gb, servidores_gb, total_gb}} de las sesiones que corren ({id: pid del lanzador})."""
    if not raices:
        return {}
    tabla = G.tabla_procesos()
    out = {}
    for sid, pid in raices.items():
        partes = partes_del_arbol(pid, tabla)
        h = {f"{k}_gb": round(MEM.huella(v) / GB, 3) for k, v in partes.items()}
        h["total_gb"] = round(sum(h.values()), 3)
        h["procesos"] = sum(len(v) for v in partes.values())
        out[sid] = h
    return out


# --------------------------------------------------------------------------- #
# Docker                                                                       #
# --------------------------------------------------------------------------- #
def docker() -> dict:
    """El tope de la VM de Docker, la salud del contenedor de N6 y sus cifras (`docker stats`), sin listar nada más."""
    def run(args):
        r = subprocess.run(["docker", *args], capture_output=True, text=True)
        return r.returncode, r.stdout.strip()
    rc1, mem = run(["info", "--format", "{{.MemTotal}}"])
    rc2, salud = run(["inspect", "-f", "{{.State.Health.Status}}", CONTENEDOR])
    rc3, stats = run(["stats", "--no-stream", "--format", "{{json .}}", CONTENEDOR])
    try:
        mem_total = int(mem)
    except ValueError:
        mem_total = None
    try:
        st = json.loads(stats) if rc3 == 0 else None
        st = {k: st.get(k) for k in ("Name", "MemUsage", "MemPerc", "CPUPerc", "PIDs")} if isinstance(st, dict) else None
    except json.JSONDecodeError:
        st = None
    tope_ok = rc1 == 0 and mem_total is not None and mem_total <= DOCKER_MEM_TOTAL_MAX
    sano = rc2 == 0 and salud == "healthy"
    return {"mem_total_bytes": mem_total, "mem_total_max_bytes": DOCKER_MEM_TOTAL_MAX, "vm_topeada": tope_ok,
            "contenedor": CONTENEDOR, "salud": salud if rc2 == 0 else None, "sano": sano, "stats": st,
            "ok": tope_ok and sano}
