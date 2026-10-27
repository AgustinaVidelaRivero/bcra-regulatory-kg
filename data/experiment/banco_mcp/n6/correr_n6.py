#!/usr/bin/env python3
"""correr_n6.py — El corredor de N6 de U-NAV-DISENO (protocolo de N4, sellado en f69e95ea): las ablaciones de la navegación
del agente. NO corre sin la entrada sellada y su sha256, y la corrida real solo con el tope de USD 130 y el freno de 100.

Lo que corre (N4, §2 y §6): las 30 preguntas de N3 en las 8 configuraciones del grafo (B tres veces) y en las 2 de F1 (BM25 de
A2.2 tres veces y la híbrida una), 420 sesiones (300 del grafo y 120 de F1), cada una con el agente del banco y R5 de A2.2
(30, 32 y 1,80), y el juez de EV2 encadenado, 3 repeticiones por respuesta, con el veredicto modal por criterio.

Cómo:
  · la entrada sellada (`entrada`, n6/entrada_n6.json): las preguntas (ruta y sha256, leídas solo por código), la configuración
    de agentes, el lanzador de una sesión, R5 (el campo «R5» que lee el lanzador del lote), el tope y el freno, el orden de las
    corridas (sus semillas y la lista de ids, sin texto), el juez (prompt por sha256, modelo y precios) y los sha256 de la lista
    de la familia 5 y su sello. Toda corrida, y toda reanudación, controla que la entrada sea la misma y que lo que nombra dé su
    sha256;
  · el agente (`agente`), en dos lotes (decisiones de la autora del 27/10/2026, puntos 1 y 8; cambio de orden declarado): primero
    las sesiones de las configuraciones que no cargan el codificador de consultas (config_agentes_n6.json, carga_codificador: B,
    BM25 de F1 y T−F1), con su P (--P-sin-codificador); después las que lo cargan (T, T−F2 a T−F6 y la híbrida de F1), con la
    suya (--P-con-codificador). Cada uno, en el orden sellado restringido a sus sesiones (la entrada trae los dos, con sus ids),
    por lotes del lanzador, con agentes/lanzar_lote_paralelo_r5.py de HEAD importado sin editarlo, P sesiones a la vez. Su guarda
    de otro paso pago es paralelo/guardas_lote_n6.py (el patrón de HEAD más lanzar_lote_paralelo_r5.py y correr_n6.py). Cada lote
    del lanzador, en <salida>/agente/lote_<k>/, con su registro;
  · la memoria y Docker (control_memoria_n6.py): al lanzar, lo fijo (la memoria en uso, sin ninguna sesión) y el swap, si entran
    las dos P (la del lote sin codificador, con 0,381 GB por sesión hasta que el primer lote mida la suya; la del lote con
    codificador, con la regla de la decisión 7), el tope de la VM de Docker y la salud del contenedor de N6; antes del lote con
    codificador, su P con la huella de CLI más alta del primer lote más 4,565 GB por sesión; antes de cada tanda (la guarda que
    el lote de HEAD corre antes de cada tanda: GuardaTanda), lo fijo (la memoria en uso menos la de las sesiones que corren) más
    P huellas de una sesión del lote, hasta 14,5 GB, y Docker otra vez. La huella de cada sesión (su lanzador, su CLI con su
    Node y sus servidores, por `footprint -p`), cada INTERVALO_HUELLAS_S y antes de cada tanda, va al registro de su lote
    (`huellas_n6`), y lo de cada tanda (lo fijo, el swap y `docker stats`), también (`guarda_tanda_n6`). Si una P no entra frena
    (13) y dice cuál entra; si Docker no está bien, frena (14). Antes de una tanda, frena sin lanzarla, sin cortar las sesiones
    que corren y sin cambiar la P; el lote de HEAD lo anota como su guarda de otro paso pago (con el pid 0 y el motivo), y este
    corredor lo traduce al 13 o al 14. El swap se registra y no frena. La acción `controles` hace lo de «al lanzar», sin lanzar
    nada y sin la clave;
  · cada sesión se clasifica por su meta y su stream (CLASES): completa, cortada por R5, salida mal formada (sin JSON final),
    falla de infraestructura (sin meta, sin `result`, un servidor que no llegó a connected, un error de la API o un log R1 que
    no cierra), configuración (el inventario de herramientas no es el de su configuración: frena) o forma desconocida. Una
    falla de infraestructura se re-corre una vez, como su intento 2 (id con «-i2»), en el lote siguiente, con su gasto dentro del
    mismo tope y el mismo freno; si vuelve a fallar queda incompleta y se declara. Una forma desconocida queda incompleta (no
    cuenta como correcta en el análisis principal, sale del de sensibilidad y se declara) y el corredor frena al juntar 3 (la
    regla (d) que la autora fijó para B6.3, que acá se propone);
  · el gasto, uno para el agente y el juez juntos, con R9 (tokens × agentes/precios_sellados.json, nunca total_cost_usd) para el
    agente y los tokens del juez por sus precios (comun_a2_2: precios_sellados.json no trae el modelo del juez). Cada lote corre
    con el freno y el tope que quedan: los de la entrada menos lo gastado (el R9 de las sesiones con meta; el presupuesto entero
    de las que lanzaron el CLI y no tienen `result`, como el lote; y el juez) y menos la reserva del juez para las respuestas que
    faltan juzgar (RESERVA_JUEZ_POR_RESPUESTA cada una). El juez, antes de cada respuesta, mira lo gastado más el costo mayor de
    una respuesta ya juzgada contra el freno y el tope;
  · después de cada lote, el control del disco de A2.1 (correr_a2_1.control_disco, sin editarlo) sobre cada sesión: un resultado
    de herramienta que llegó como referencia a disco frena;
  · el juez (`juez`), con el de EV2 tal cual (ev2_juez/juez.py, prompt v1 por sha256; juez_a2_2.controlar_instrumento y
    control_sdk, sin editarlos): solo las sesiones completas con respuesta; a ciegas (al juez viajan la pregunta, la respuesta y
    los criterios con su cita, y nada más), con un id opaco por respuesta y el orden por una semilla propia; su caché, en
    <salida>/juez/cache/; la tabla de los ids opacos, en desanonimizacion_SOLO_MESA/;
  · `todo`: el agente y, si terminó sin freno, el juez;
  · retomar: con la misma entrada y la misma salida, ninguna sesión terminada se repite (las que tienen meta con `result`, en
    cualquiera de sus intentos) y el juez sigue desde su caché y sus veredictos;
  · la foto del repo, al empezar y al terminar (sha256 de cada archivo, sin .git, .venv, las zonas vedadas ni
    data/experiment/banco_mcp/b63/, donde puede estar escribiendo la etapa b del runner de B6.3), va al registro.
Las salidas van fuera del repo (por defecto, ~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n6/). Imprime solo cuentas y costos:
ninguna pregunta, ningún criterio, ninguna respuesta. El registro (<salida>/registro_n6.json) lleva los ids.

Códigos: 0 terminó; 2 freno del gasto; 3 lote inválido; 4 el cwd compartido no está vacío; 5 aislamiento o R5; 6 la versión del
CLI; 7 otro paso pago corriendo; 8 precondición (la entrada, las configuraciones, el Neo4j, la lista de la familia 5); 9 una
extracción corriendo; 10 el control del disco; 11 freno del juez; 12 tres formas desconocidas; 13 la memoria (una P que no entra,
al lanzar, antes del lote con codificador o antes de una tanda); 14 Docker (la VM de más o el contenedor de N6 no sano).

Uso (lo corre la autora; la clave del agente la pone el envoltorio de A2.1 y la del juez la toma el juez de EV2):
  .venv/bin/python -B data/experiment/banco_mcp/n6/correr_n6.py {controles|todo} --entrada data/experiment/banco_mcp/n6/entrada_n6.json \\
      --sha256-entrada <hex> --P-sin-codificador <P> --P-con-codificador <P> [--salida <dir>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import re
import sqlite3
import subprocess
import sys
import threading
from collections import Counter
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(BANCO_DIR), str(BANCO_DIR / "agentes"), str(BANCO_DIR / "paralelo"), str(BANCO_DIR / "a2_1"),
           str(BANCO_DIR / "a2_2"), str(AQUI)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import lanzar_lote_paralelo_r5 as R5            # noqa: E402  (HEAD: solo import)
import guardas_lote_n6 as G                     # noqa: E402
import correr_a2_1 as CR                        # noqa: E402  (A2.1: control_disco, solo import)
import juez_a2_2 as JA                          # noqa: E402  (A2.2: controlar_instrumento y control_sdk, solo import)
import control_memoria_n6 as CM                 # noqa: E402  (lo fijo, las P, las huellas y Docker)
from comun_banco import rel_repo, sha256_file   # noqa: E402

R5.BASE.G = G                                   # la guarda de otro paso pago del lote, con el patrón de N6
LA = R5.LA
J, M, K = JA.J, JA.M, JA.K
REPO_DIR = LA.REPO_DIR
FDR = Path.home() / "INGENIERIA IA" / "TESIS" / "fuera_del_repo"
SALIDA_DEFAULT = FDR / "banco_n6"
ENTRADA_DEFAULT = AQUI / "entrada_n6.json"
PREGUNTAS_N3 = FDR / "unav_n3" / "preguntas_N3.json"
SHA_PREGUNTAS_N3 = "6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b"
SELLO_N3 = FDR / "unav_n3" / "sello_N3.txt"
SHA_SELLO_N3 = "dfb660fc82e15444c8cfc3cf74f6c5b5c44451bf1f4d89a53a363c72bf0d653a"
CONFIG_AGENTES = AQUI / "config_agentes_n6.json"
LANZADOR = AQUI / "lanzar_agente_n6.py"
LISTA_F5, SELLO_F5 = AQUI / "lista_familia5_N6.json", AQUI / "sello_lista_familia5_N6.txt"

TOPE, FRENO = 130.0, 100.0                       # N4, §7 y §8, punto 4: para el agente y el juez juntos
SEMILLA_ORDEN = "N6:orden_corridas:v1"
SEMILLA_ORDEN_JUEZ = "N6:orden_juez:v1"
SAL_ID_OPACO = "N6:id_opaco_juez:v1"
PREFIJO_ID = "N6J-"
DB_PREFIX = "n6_juez"
REPS_JUEZ = (1, 2, 3)
RESERVA_JUEZ_POR_RESPUESTA = K.COSTO_RESPUESTA_INICIAL      # 0,0378: la de A2.2 para una respuesta sin juzgar
PRECIO_JUEZ_IN, PRECIO_JUEZ_OUT = K.PRECIO_JUEZ_IN, K.PRECIO_JUEZ_OUT
MAX_INTENTOS = 2
MAX_FORMAS_DESCONOCIDAS = 3
CORTES_R5 = ("error_max_turns", "error_max_budget_usd")
FRENO_GASTO, LOTE_INVALIDO, CWD_NO_VACIO, AISLAMIENTO, VERSION_CLI, OTRO_PASO_PAGO = 2, 3, 4, 5, 6, 7
PRECONDICION, EXTRACCION, DISCO, FRENO_JUEZ, FORMAS_DESCONOCIDAS = 8, 9, 10, 11, 12
MEMORIA, DOCKER = 13, 14
# Los dos lotes (decisiones de la autora del 27/10/2026, puntos 1 y 8): primero las sesiones que no cargan el codificador, con
# su P; después las que lo cargan, con la suya. Cada lote, en el orden sellado restringido a sus sesiones.
LOTES = (("sin_codificador", False, "N6_P_SIN_CODIFICADOR"), ("con_codificador", True, "N6_P_CON_CODIFICADOR"))
PYTHON_CITAS = Path.home() / "INGENIERIA IA" / "TESIS" / "venvs" / "banco_vector_py312" / "bin" / "python"
INTERVALO_HUELLAS_S = 5.0           # cada cuánto se toma la huella de las sesiones que corren (la de memoria_n6.py)
CLASES = ("completa", "corte_R5", "mal_formada", "infraestructura", "configuracion", "desconocida")
# La foto del repo poda lo que no es de esta unidad o está vedado (y b63/, donde puede escribir la etapa b del runner).
PODAR_RUTAS = (".git", ".venv", ".venv-app", "data/experiment/segmentacion_oficial_e0r2/s1ter/adjudicacion",
               "data/experiment/segmentacion_oficial_e0r2/s1quater/adjudicacion", "data/experiment/banco_mcp/b63",
               "data/experiment/banco_mcp/a2_2/adjudicacion", "data/experiment/evaluacion/queries",
               "data/experiment/evaluacion_escalon1", "data/experiment/exploracion/ev2_fidelidad",
               "data/experiment/ev2_tanda0/preguntas", "data/experiment/neo4j/volumen")
# Los volúmenes de los Neo4j propios (volumen_n6, volumen_banco_paralelo, …), que escribe su contenedor.
PODAR_VOLUMENES = re.compile(r"^data/experiment/neo4j/volumen[^/]*$")
PODAR_NOMBRES = re.compile(r"^(NO_ABRIR_.*|.*_SOLO_MESA.*|\.env|\.env\..*|.*\.env|.*eval_?set.*)$", re.IGNORECASE)


class Freno(Exception):
    def __init__(self, codigo: int, motivo: str):
        super().__init__(motivo)
        self.codigo, self.motivo = codigo, motivo


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def ahora() -> str:
    return datetime.now().astimezone().isoformat(timespec="seconds")


def cli_falso() -> bool:
    return "falso" in (R5.cli_del_path()["version"] or "")


# --------------------------------------------------------------------------- #
# Preguntas y orden                                                            #
# --------------------------------------------------------------------------- #
def ancla_to_punto(a: dict) -> str:
    """«to::punto» para el instrumento de citas: el punto de N3 sin el punto final («5.1.1.» da «5.1.1»; «Sección 3.», «Sección 3»)."""
    punto = re.sub(r"\.+$", "", a["punto"].strip())
    return f"{a['to']}::{punto}"


def cargar_preguntas(ruta: Path, sha_esperado: str) -> dict:
    """{id: {pregunta, criterios [{criterio, cita_textual}], anclas ["to::punto"], conjunto, tipo, subtipo, necesidad, to}}, leído
    por código (no imprime nada). Frena si el archivo no da su sha256."""
    b = Path(ruta).read_bytes()
    if hashlib.sha256(b).hexdigest() != sha_esperado:
        raise Freno(PRECONDICION, "el archivo de preguntas no da el sha256 de la entrada")
    out = {}
    for p in json.loads(b)["preguntas"]:
        crits = [{"criterio": c["criterio"], "cita_textual": c["cita"]} for c in p["gold"]["criterios"]]
        if not crits or any(not c["criterio"].strip() or not c["cita_textual"].strip() for c in crits) or p["id"] in out:
            raise Freno(PRECONDICION, "una pregunta sin criterios, con un criterio o una cita vacíos, o un id repetido")
        out[p["id"]] = {"pregunta": p["pregunta"], "criterios": crits, "anclas": [ancla_to_punto(a) for a in p["gold"]["anclas"]],
                        "conjunto": p.get("conjunto"), "tipo": p.get("tipo"), "subtipo": p.get("subtipo"),
                        "necesidad": p.get("necesidad"), "to": p.get("to")}
    return out


def corridas_por_pregunta(cfg_agentes: dict) -> list[dict]:
    """Las corridas de una pregunta: cada configuración con sus repeticiones (B y F1_bm25, 3; las demás, 1)."""
    out = []
    for cid, c in cfg_agentes["configuraciones_n6"].items():
        for r in range(1, c["repeticiones"] + 1):
            out.append({"configuracion": cid, "brazo": c["brazo"], "rep": r})
    return out


def id_sesion(qid: str, cid: str, rep: int) -> str:
    return f"N6-{qid}-{cid}-r{rep}"


def armar_orden(ids: list[str], cfg_agentes: dict, semilla: str = SEMILLA_ORDEN) -> dict:
    """Las preguntas en el orden de `random.Random(semilla).shuffle` sobre sus ids ordenados y, por pregunta, sus corridas en el
    orden de `random.Random(f"{semilla}:{id}")` sobre la lista ordenada por (configuración, repetición): las de una pregunta
    van seguidas. Solo ids y nombres."""
    preg = sorted(ids)
    random.Random(semilla).shuffle(preg)
    base = sorted(corridas_por_pregunta(cfg_agentes), key=lambda c: (c["configuracion"], c["rep"]))
    sesiones = []
    for q in preg:
        cs = list(base)
        random.Random(f"{semilla}:{q}").shuffle(cs)
        sesiones += [{"id": id_sesion(q, c["configuracion"], c["rep"]), "qid": q, **c} for c in cs]
    return {"semilla": semilla, "regla_preguntas": f"random.Random('{semilla}').shuffle sobre los ids ordenados",
            "regla_corridas": f"random.Random(f'{semilla}:{{id}}').shuffle sobre las corridas ordenadas por (configuración, repetición)",
            "preguntas_en_orden": preg, "n_sesiones": len(sesiones), "sesiones": sesiones,
            "sha256_ids_ordenados": sha256_texto("".join(x + "\n" for x in sorted(ids)))}


# --------------------------------------------------------------------------- #
# La entrada sellada                                                           #
# --------------------------------------------------------------------------- #
def armar_lotes(orden: dict, cfg: dict) -> list[dict]:
    """Los dos lotes: las configuraciones por si cargan el codificador (config_agentes_n6.json, carga_codificador) y, en cada uno,
    las sesiones en el orden sellado."""
    out = []
    for nombre, con, var in LOTES:
        confs = sorted(c for c, x in cfg["configuraciones_n6"].items() if bool(x.get("carga_codificador")) == con)
        ids = [s["id"] for s in orden["sesiones"] if s["configuracion"] in confs]
        out.append({"nombre": nombre, "carga_codificador": con, "variable_P": var, "configuraciones": confs,
                    "n_sesiones": len(ids), "por_configuracion": dict(Counter(s["configuracion"] for s in orden["sesiones"]
                                                                              if s["configuracion"] in confs)),
                    "ids": ids})
    if sum(x["n_sesiones"] for x in out) != orden["n_sesiones"]:
        raise Freno(PRECONDICION, "los lotes no cubren las sesiones de la entrada")
    return out


def interprete_citas(python: Path) -> dict:
    """La ruta y la versión (sys.version) del intérprete con que corre el instrumento de citas (Python 3.12 o más nuevo). La ruta
    es la del python del venv, sin seguir su enlace (rel_repo lo resolvería al intérprete base, que no tiene los paquetes del venv),
    con el home colapsado a `~`."""
    r = subprocess.run([str(python), "-I", "-c", "import sys; print(sys.version); print(sys.version_info >= (3, 12))"],
                       capture_output=True, text=True)
    lineas = r.stdout.strip().splitlines()
    if r.returncode or len(lineas) != 2 or lineas[1] != "True":
        raise Freno(PRECONDICION, "el intérprete del instrumento de citas no es un Python 3.12 o más nuevo")
    p = Path(os.path.abspath(python))
    ruta = (str(p.relative_to(REPO_DIR)) if p.is_relative_to(REPO_DIR) else
            "~/" + str(p.relative_to(Path.home())) if p.is_relative_to(Path.home()) else str(p))
    return {"ruta": ruta, "version": lineas[0]}


def armar_entrada(modo: str, preguntas: Path, sha_preguntas: str, config_agentes: Path, lanzador: Path,
                  tope: float, freno: float, python_citas: Path = PYTHON_CITAS) -> dict:
    cfg = json.loads(config_agentes.read_text(encoding="utf-8"))
    ps = cargar_preguntas(preguntas, sha_preguntas)
    orden = armar_orden(list(ps), cfg)
    r5 = cfg["R5"]
    corte = cfg["corte_R5"]
    if r5 != {"tope_tool_calls_prompt": corte["tope_tool_calls_en_prompt"], "max_turns": corte["max_turns"],
              "max_budget_usd": corte["max_budget_usd_por_sesion"]}:
        raise Freno(PRECONDICION, "el R5 de la configuración no es su corte_R5")
    e = {"unidad": "U-NAV-DISENO, N6 — la entrada sellada del corredor (correr_n6.py)",
         "modo": modo,
         "preguntas": {"ruta": rel_repo(preguntas), "sha256": sha_preguntas, "n": len(ps),
                       "sello_N3": {"ruta": rel_repo(SELLO_N3), "sha256": SHA_SELLO_N3} if modo == "real" else None},
         "config_agentes": {"ruta": str(config_agentes.relative_to(BANCO_DIR)), "sha256": sha256_file(config_agentes)},
         "lanzador": {"ruta": str(lanzador.relative_to(BANCO_DIR)), "sha256": sha256_file(lanzador)},
         "guarda": {"ruta": rel_repo(Path(G.__file__)), "sha256": sha256_file(Path(G.__file__)), "patron": G.PATRON_PAGO_REAL},
         "R5": r5, "tope_usd": tope, "freno_usd": freno, "presupuesto_por_sesion_usd": r5["max_budget_usd"],
         "modelo": cfg["modelo"], "claude_code_version_sellada": cfg["claude_code_version_sellada"],
         "juez": {"ruta": rel_repo(Path(J.__file__)), "prompt_version": J.PROMPT_VERSION, "prompt_sha256": J.PROMPT_SHA256,
                  "modelo": J.MODELO, "temperatura": J.TEMPERATURE, "repeticiones": len(REPS_JUEZ),
                  "precios_usd_por_millon": {"entrada": PRECIO_JUEZ_IN, "salida": PRECIO_JUEZ_OUT},
                  "semilla_orden": SEMILLA_ORDEN_JUEZ, "sal_id_opaco": SAL_ID_OPACO,
                  "reserva_por_respuesta_usd": RESERVA_JUEZ_POR_RESPUESTA},
         "reintentos": {"max_intentos": MAX_INTENTOS, "max_formas_desconocidas": MAX_FORMAS_DESCONOCIDAS},
         "citas": {"instrumento": "scripts/ucita2_indicadores_banco.py", "python": interprete_citas(python_citas)},
         "memoria": {"limite_gb": CM.LIMITE_GB, "huella_sesion_sin_codificador_gb_inicial": CM.HUELLA_SESION_SIN_CODIFICADOR_GB,
                     "huella_servidor_con_codificador_gb": CM.HUELLA_SERVIDOR_CON_CODIFICADOR_GB,
                     "P_con_codificador_umbrales_gb": {str(k): v for k, v in CM.UMBRALES_P_CON_CODIFICADOR.items()},
                     "intervalo_huellas_s": INTERVALO_HUELLAS_S},
         "docker": {"mem_total_max_bytes": CM.DOCKER_MEM_TOTAL_MAX, "contenedor": CM.CONTENEDOR},
         "lotes": armar_lotes(orden, cfg),           # los dos lotes, en este orden: primero el sin codificador
         "orden": orden}
    if modo == "real":
        e["lista_familia5"] = {"ruta": rel_repo(LISTA_F5), "sha256": sha256_file(LISTA_F5),
                               "sello": {"ruta": rel_repo(SELLO_F5), "sha256": sha256_file(SELLO_F5)}}
    return e


def cargar_entrada(ruta: Path, sha: str, modo_esperado: str | None = None) -> dict:
    """La entrada, si da su sha256 y si lo que nombra da el suyo; y su orden, si es el que se recomputa."""
    p = Path(ruta)
    if not p.is_file() or sha256_file(p) != sha:
        raise Freno(PRECONDICION, "la entrada no existe o no da el sha256 pasado")
    e = json.loads(p.read_text(encoding="utf-8"))
    if modo_esperado and e["modo"] != modo_esperado:
        raise Freno(PRECONDICION, f"la entrada es de modo {e['modo']!r}")
    for k in ("config_agentes", "lanzador"):
        if sha256_file(BANCO_DIR / e[k]["ruta"]) != e[k]["sha256"]:
            raise Freno(PRECONDICION, f"{e[k]['ruta']} no da el sha256 de la entrada")
    if sha256_file(Path(G.__file__)) != e["guarda"]["sha256"] or G.PATRON_PAGO_REAL != e["guarda"]["patron"]:
        raise Freno(PRECONDICION, "la guarda no es la de la entrada")
    if (J.PROMPT_SHA256, J.MODELO, J.TEMPERATURE) != (e["juez"]["prompt_sha256"], e["juez"]["modelo"], e["juez"]["temperatura"]):
        raise Freno(PRECONDICION, "el juez no es el de la entrada")
    if e["modo"] == "real":
        if (e["tope_usd"], e["freno_usd"]) != (TOPE, FRENO):
            raise Freno(PRECONDICION, "la corrida real usa el tope 130 y el freno 100 de N4")
        if sha256_file(SELLO_N3) != SHA_SELLO_N3:
            raise Freno(PRECONDICION, "el sello de N3 no da su sha256")
        lf = e["lista_familia5"]
        if sha256_file(REPO_DIR / lf["ruta"]) != lf["sha256"] or sha256_file(REPO_DIR / lf["sello"]["ruta"]) != lf["sello"]["sha256"]:
            raise Freno(PRECONDICION, "la lista de la familia 5 o su sello no dan su sha256")
    cfg = json.loads((BANCO_DIR / e["config_agentes"]["ruta"]).read_text(encoding="utf-8"))
    ps = cargar_preguntas(ruta_de(e["preguntas"]["ruta"]), e["preguntas"]["sha256"])
    if armar_orden(list(ps), cfg) != e["orden"]:
        raise Freno(PRECONDICION, "el orden de la entrada no es el que se recomputa")
    if cfg["R5"] != e["R5"]:
        raise Freno(PRECONDICION, "el R5 de la entrada no es el de la configuración")
    if armar_lotes(e["orden"], cfg) != e["lotes"]:
        raise Freno(PRECONDICION, "los lotes de la entrada no son los que se recomputan")
    if interprete_citas(ruta_de(e["citas"]["python"]["ruta"])) != e["citas"]["python"]:
        raise Freno(PRECONDICION, "el intérprete del instrumento de citas no es el de la entrada (ruta o versión)")
    if (e["memoria"]["limite_gb"], e["docker"]["mem_total_max_bytes"]) != (CM.LIMITE_GB, CM.DOCKER_MEM_TOTAL_MAX):
        raise Freno(PRECONDICION, "el límite de 14,5 GB o el tope de la VM de Docker no es el de la entrada")
    e["_preguntas"], e["_cfg"] = ps, cfg
    return e


def ruta_de(r: str) -> Path:
    return R5.ruta_de_rel(r) if not r.startswith("$HOME/") else Path.home() / r[len("$HOME/"):]


def precondiciones(e: dict, con_neo4j: bool = True) -> dict:
    """La configuración de N6 armada byte a byte (armar_configuraciones_n6 --verificar), el Neo4j propio (control_neo4j_n6),
    ninguna extracción corriendo y ningún otro paso pago corriendo, antes de lanzar nada."""
    import armar_configuraciones_n6 as AC               # noqa: PLC0415
    out = {}
    if e["modo"] == "real":
        dist = [rel for rel, txt in AC.armar().items() if (BANCO_DIR / rel).read_bytes() != txt.encode("utf-8")]
        out["configuraciones"] = {"iguales_a_lo_que_se_arma": not dist, "distintas": dist}
        if dist:
            raise Freno(PRECONDICION, f"configuraciones de N6 distintas de las que se arman: {dist}")
    if con_neo4j:
        import control_neo4j_n6 as CN                   # noqa: PLC0415
        try:
            n = CN.estado()
        except SystemExit as x:
            raise Freno(PRECONDICION, str(x))
        out["neo4j"] = {k: n.get(k) for k in ("NEO4J_URI", "kg_meta_sha256", "huellas_de_la_carga", "ok")} | {
            "hubs": (n.get("navegador") or {}).get("hubs")}
        if not n.get("ok"):
            raise Freno(PRECONDICION, f"el Neo4j propio de N6: {n.get('motivo')}")
    ext = G.extraccion_corriendo()
    out["extraccion"] = ext
    if ext:
        raise Freno(EXTRACCION, f"una extracción corriendo: {ext}")
    otro = G.otro_paso_pago()
    out["otro_paso_pago"] = otro
    if otro:
        raise Freno(OTRO_PASO_PAGO, f"otro paso pago corriendo: {otro}")
    return out


# --------------------------------------------------------------------------- #
# La foto del repo                                                             #
# --------------------------------------------------------------------------- #
def foto_repo(raiz: Path = REPO_DIR) -> dict:
    """sha256 de cada archivo del repo fuera de PODAR_RUTAS y PODAR_NOMBRES (con b63/ afuera), y el de la lista."""
    podar = {raiz / r for r in PODAR_RUTAS}
    filas = []
    for d, subdirs, archivos in os.walk(raiz):
        dp = Path(d)
        subdirs[:] = sorted(s for s in subdirs if dp / s not in podar and not PODAR_NOMBRES.match(s)
                            and not PODAR_VOLUMENES.match(str((dp / s).relative_to(raiz))))
        for f in sorted(archivos):
            p = dp / f
            if PODAR_NOMBRES.match(f) or p.is_symlink() or not p.is_file():
                continue
            filas.append(f"{sha256_file(p)}  {p.relative_to(raiz)}")
    filas.sort(key=lambda x: x.split("  ", 1)[1])
    return {"n_archivos": len(filas), "sha256": sha256_texto("\n".join(filas) + "\n"),
            "podadas": list(PODAR_RUTAS) + [PODAR_VOLUMENES.pattern], "_filas": filas}


# --------------------------------------------------------------------------- #
# Las sesiones: intentos, clases y gasto                                       #
# --------------------------------------------------------------------------- #
def result_del_stream(p: Path) -> dict | None:
    """Del stream, solo el subtype y el is_error del evento result (o None si no hay)."""
    if not p.is_file():
        return None
    r = None
    for linea in p.read_text(encoding="utf-8", errors="replace").splitlines():
        if '"type":"result"' not in linea.replace(" ", ""):
            continue
        try:
            d = json.loads(linea)
        except json.JSONDecodeError:
            continue
        if d.get("type") == "result":
            r = {"subtype": d.get("subtype"), "is_error": bool(d.get("is_error"))}
    return r


def clasificar(d: Path, pid: str, presupuesto: float) -> dict:
    """La clase de un intento, por su carpeta, y lo que cuenta para el gasto."""
    meta_p, cmd_p = d / f"meta_{pid}.json", d / f"comando_{pid}.json"
    if not meta_p.is_file():
        lanzo = cmd_p.is_file()
        return {"clase": "infraestructura", "motivo": "sin meta", "costo_R9_usd": 0.0,
                "costo_guarda_usd": presupuesto if lanzo else 0.0, "con_result": False}
    m = json.loads(meta_p.read_text(encoding="utf-8"))
    r9 = LA.costo_desde_tokens(m["modelos_R8"]["uso_por_modelo"], LA.cargar(LA.PRECIOS))
    sin_result = m["modelos_R8"]["uso_por_modelo"] is None
    costo = {"costo_R9_usd": r9["total_usd"],
             "costo_guarda_usd": presupuesto if (sin_result or r9["modelos_sin_precio_sellado"]) else r9["total_usd"]}
    res = result_del_stream(d / f"stream_{pid}.jsonl")
    init = (m.get("servidores_mcp") or {}).get("en_init") or []
    conectado = bool(init) and all(s.get("status") == "connected" for s in init)
    r6 = (m.get("inventario_tools_R6") or {}).get("coincide")
    completa = (m.get("completitud_R3") or {}).get("completa")
    motivos = (m.get("completitud_R3") or {}).get("motivos_incompleta") or []
    hb2 = m.get("hb2") or {}
    out = {**costo, "con_result": res is not None, "llamadas_log_r1": hb2.get("n_llamadas_log_r1"),
           "subtype": (res or {}).get("subtype"), "is_error": (res or {}).get("is_error"), "completa_R3": completa}
    if res is None or sin_result:
        return out | {"clase": "infraestructura", "motivo": "sin result"}
    if not conectado:
        return out | {"clase": "infraestructura", "motivo": "un servidor MCP no llegó a connected"}
    if r6 is False:
        return out | {"clase": "configuracion", "motivo": "el inventario de herramientas no es el de su configuración"}
    if res["subtype"] in CORTES_R5:
        return out | {"clase": "corte_R5", "motivo": res["subtype"]}
    if res["is_error"]:
        return out | {"clase": "infraestructura", "motivo": "error de la API (is_error)"}
    if res["subtype"] == "success":
        if completa:
            return out | {"clase": "completa", "motivo": None}
        if any("JSON" in x for x in motivos):
            return out | {"clase": "mal_formada", "motivo": "; ".join(motivos)}
        return out | {"clase": "infraestructura", "motivo": "; ".join(motivos) or "incompleta por R3"}
    return out | {"clase": "desconocida", "motivo": f"result.subtype={res['subtype']}"}


def intentos(salida: Path, base: str) -> list[tuple[Path, str]]:
    """Las carpetas de los intentos de una sesión, en todos los lotes, en orden de intento: (carpeta, id del intento)."""
    out = []
    for k, suf in enumerate([""] + [f"-i{i}" for i in range(2, MAX_INTENTOS + 1)], 1):
        pid = base + suf
        ds = sorted((salida / "agente").glob(f"lote_*/{pid}"))
        if len(ds) > 1:
            raise Freno(PRECONDICION, f"el intento {pid} está en más de un lote")
        if ds:
            out.append((ds[0], pid))
    return out


def estado(e: dict, salida: Path) -> dict:
    """Por sesión de la entrada: sus intentos con su clase, la clase final y si falta correrla; y el gasto del agente."""
    pres = e["presupuesto_por_sesion_usd"]
    por = {}
    gasto_r9 = gasto_guarda = 0.0
    for s in e["orden"]["sesiones"]:
        its = []
        for d, pid in intentos(salida, s["id"]):
            c = clasificar(d, pid, pres)
            its.append({"id": pid, "carpeta": str(d), **c})
            gasto_r9 += c["costo_R9_usd"]
            gasto_guarda += c["costo_guarda_usd"]
        final = its[-1] if its else None
        pendiente = final is None or (final["clase"] == "infraestructura" and len(its) < MAX_INTENTOS)
        por[s["id"]] = {"sesion": s, "intentos": its, "final": final, "pendiente": pendiente,
                        "siguiente_id": None if not pendiente else (s["id"] if not its else f"{s['id']}-i{len(its) + 1}")}
    return {"por_sesion": por, "gasto_agente_R9_usd": round(gasto_r9, 6), "gasto_agente_guarda_usd": round(gasto_guarda, 6),
            "clases_finales": dict(Counter(v["final"]["clase"] if v["final"] else "sin correr" for v in por.values())),
            "pendientes": sum(1 for v in por.values() if v["pendiente"])}


# --------------------------------------------------------------------------- #
# El gasto del juez                                                            #
# --------------------------------------------------------------------------- #
def db_juez(rep: int, cache_dir: Path) -> Path:
    return J.db_path_rep(rep, cache_dir, DB_PREFIX)


def gasto_juez(cache_dir: Path) -> dict:
    """Una fila por llamada pagada en las tres cachés del juez de N6, con los tokens por sus precios."""
    tin = tout = filas = 0
    for rep in REPS_JUEZ:
        p = db_juez(rep, cache_dir)
        if not p.exists():
            continue
        conn = sqlite3.connect(str(p))
        try:
            n, i, o = conn.execute("SELECT COUNT(*), COALESCE(SUM(input_tokens),0), COALESCE(SUM(output_tokens),0) "
                                   "FROM cache").fetchone()
        except sqlite3.OperationalError:
            n, i, o = 0, 0, 0
        conn.close()
        filas += n; tin += i; tout += o
    return {"filas": filas, "input_tokens": tin, "output_tokens": tout,
            "usd": round(tin / 1e6 * PRECIO_JUEZ_IN + tout / 1e6 * PRECIO_JUEZ_OUT, 6)}


def leer_jsonl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def juzgadas(juez_dir: Path) -> set[str]:
    """Los ids opacos con sus tres repeticiones (veredicto o error) ya registradas."""
    hechos = [{r["id_opaco"] for r in leer_jsonl(juez_dir / f"veredictos_r{rep}.jsonl")}
              | {r["id_opaco"] for r in leer_jsonl(juez_dir / f"errores_r{rep}.jsonl")} for rep in REPS_JUEZ]
    return set.intersection(*hechos) if hechos else set()


# --------------------------------------------------------------------------- #
# El registro                                                                  #
# --------------------------------------------------------------------------- #
class Registro:
    def __init__(self, salida: Path, sha_entrada: str):
        self.p = salida / "registro_n6.json"
        if self.p.exists():
            self.d = json.loads(self.p.read_text(encoding="utf-8"))
            if self.d.get("entrada_sha256") != sha_entrada:
                raise Freno(PRECONDICION, "la salida ya tiene un registro de otra entrada: no se mezclan corridas")
        else:
            self.d = {"unidad": "U-NAV-DISENO, N6", "entrada_sha256": sha_entrada, "corridas": []}
        self.c = {"inicio": ahora(), "eventos": []}
        self.d["corridas"].append(self.c)

    def evento(self, **kw) -> None:
        self.c["eventos"].append({"hora": ahora(), **kw})
        self.guardar()

    def guardar(self) -> None:
        self.p.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.p.with_suffix(".tmp")
        tmp.write_text(json.dumps(self.d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        tmp.replace(self.p)


# --------------------------------------------------------------------------- #
# El agente                                                                    #
# --------------------------------------------------------------------------- #
def numero_de_lote(salida: Path) -> int:
    ks = [int(p.name.split("_")[1]) for p in (salida / "agente").glob("lote_*") if p.name.split("_")[1].isdigit()]
    return max(ks, default=0) + 1


class GuardaTanda:
    """La guarda que el lote del HEAD corre antes de cada tanda (lanzar_lote_paralelo.G.otro_paso_pago): la de otro paso pago
    (guardas_lote_n6) y, si no halla ninguno, la memoria (lo fijo más P huellas de una sesión del lote, hasta 14,5 GB) y Docker
    (la VM topeada y el contenedor de N6 sano). Si algo no entra, devuelve un hallado con el motivo: el lote no lanza esa tanda,
    no corta ninguna sesión que corre y no cambia la P; correr_agente lo traduce al código 13 (memoria) o 14 (Docker). El swap
    se registra en cada tanda y no frena."""

    def __init__(self, nombre: str, P: int, huella_por_sesion):
        self.nombre, self.P, self.huella_por_sesion = nombre, P, huella_por_sesion
        self.lote, self.registros, self.freno = None, [], None

    def otro_paso_pago(self, raiz_lote=None, patron=None):
        h = G.otro_paso_pago(raiz_lote=raiz_lote, patron=patron)
        if h:
            return h
        corriendo = self.lote.corriendo() if self.lote is not None else {}
        mem = CM.control_tanda(self.P, self.huella_por_sesion(), corriendo)
        if self.lote is not None:
            self.lote.anotar(mem["huellas"])
        dk = CM.docker()
        self.registros.append({"hora": ahora(), "lote": self.nombre, **{k: v for k, v in mem.items() if k != "huellas"},
                               "docker": dk})
        if not mem["entra"]:
            self.freno = (MEMORIA, f"lote {self.nombre}: lo fijo {mem['lo_fijo_gb']} GB más {self.P} sesiones de "
                                   f"{mem['huella_por_sesion_gb']} GB pasa de {CM.LIMITE_GB} GB antes de una tanda")
        elif not dk["ok"]:
            self.freno = (DOCKER, f"Docker antes de una tanda: VM {dk['mem_total_bytes']} bytes (tope {dk['mem_total_max_bytes']}), "
                                  f"contenedor {dk['salud']}")
        return [{"pid": 0, "script": self.freno[1]}] if self.freno else []

    def __getattr__(self, nombre):
        return getattr(G, nombre)


class LoteN6(R5.Lote):
    """El lote de lanzar_lote_paralelo_r5 (HEAD) con, mientras corre, la huella de cada sesión (su lanzador, su CLI con su Node y
    sus servidores, por `footprint -p`), tomada cada INTERVALO_HUELLAS_S y antes de cada tanda, y la guarda de la tanda en su
    registro (`huellas_n6` y `guarda_tanda_n6`)."""

    def __init__(self, a, guarda: GuardaTanda):
        super().__init__(a)
        self.guarda, guarda.lote = guarda, self
        self.huellas: dict[str, dict] = {}
        self._lock, self._fin = threading.Lock(), threading.Event()

    def corriendo(self) -> dict:
        return {x["id"]: x["pid_lanzador"] for x in list(self.sesiones) if x.get("estado") == "corriendo" and x.get("pid_lanzador")}

    def anotar(self, hs: dict) -> None:
        with self._lock:
            for sid, h in hs.items():
                m = self.huellas.setdefault(sid, {"muestras": 0})
                m["muestras"] += 1
                for k, v in h.items():
                    if k.endswith("_gb"):
                        m[k] = max(m.get(k, 0.0), v)

    def _muestrear(self) -> None:
        while not self._fin.wait(INTERVALO_HUELLAS_S):     # la única espera con plazo: entre muestras, y corta al terminar
            try:
                self.anotar(CM.huellas_de_sesiones(self.corriendo()))
            except Exception as x:                          # una muestra que falla no frena el lote; queda anotada
                with self._lock:
                    self.huellas.setdefault("_errores", {}).setdefault(type(x).__name__, 0)

    def correr(self) -> int:
        t = threading.Thread(target=self._muestrear, daemon=True)
        t.start()
        try:
            return super().correr()
        finally:
            self._fin.set()
            t.join()
            self.escribir_registro()                        # con las últimas muestras de la huella

    def resumenes(self) -> dict:
        with self._lock:
            h = json.loads(json.dumps(self.huellas))
        return super().resumenes() | {"huellas_n6": h, "guarda_tanda_n6": list(self.guarda.registros)}


def huellas_medidas(salida: Path, ids: set) -> dict:
    """Las huellas que los lotes ya corridos midieron para esas sesiones (de sus registros): {id: {..._gb}}."""
    out = {}
    for r in sorted((salida / "agente").glob("lote_*/registro_lote.json")):
        for sid, h in (json.loads(r.read_text(encoding="utf-8")).get("huellas_n6") or {}).items():
            base = re.sub(r"-i\d+$", "", sid)
            if base in ids and isinstance(h, dict):
                m = out.setdefault(sid, {})
                for k, v in h.items():
                    if k.endswith("_gb"):
                        m[k] = max(m.get(k, 0.0), v)
    return out


def correr_agente(e: dict, salida: Path, reg: Registro, P_sin: int, P_con: int, via: str, timeout_s: float) -> int:
    ps = e["_preguntas"]
    sesiones_root = salida / "sesiones"
    lotes = {x["nombre"]: x for x in e["lotes"]}
    ids_sin, ids_con = set(lotes["sin_codificador"]["ids"]), set(lotes["con_codificador"]["ids"])
    P_de = {"sin_codificador": P_sin, "con_codificador": P_con}

    def huella_sin() -> float:
        hs = huellas_medidas(salida, ids_sin)
        return max([CM.HUELLA_SESION_SIN_CODIFICADOR_GB] + [h.get("total_gb", 0.0) for h in hs.values()])

    def cli_max() -> float:
        return max([0.0] + [h.get("cli_gb", 0.0) for h in huellas_medidas(salida, ids_sin).values()])

    def huella_con() -> float:
        hs = huellas_medidas(salida, ids_con)
        return max([CM.HUELLA_SERVIDOR_CON_CODIFICADOR_GB + cli_max()] + [h.get("total_gb", 0.0) for h in hs.values()])

    al = CM.control_al_lanzar(P_sin, P_con, huella_sin())
    dk = CM.docker()
    reg.evento(evento="memoria y Docker al lanzar", memoria=al, docker=dk)
    print(f"al lanzar: lo fijo {al['lo_fijo_gb']} GB, swap {al['swap_gb']} GB; sin codificador P = {P_sin} "
          f"({'entra' if al['sin_codificador']['entra'] else 'NO entra'}; entra hasta {al['sin_codificador']['P_que_entra']}); "
          f"con codificador P = {P_con} ({'entra' if al['con_codificador']['entra'] else 'NO entra'}; entra hasta "
          f"{al['con_codificador']['P_que_entra']}); Docker: VM {dk['mem_total_bytes']} bytes, {dk['salud']}", flush=True)
    if not al["entra"]:
        raise Freno(MEMORIA, f"al lanzar no entra la P: sin codificador entra hasta {al['sin_codificador']['P_que_entra']} y con "
                             f"codificador hasta {al['con_codificador']['P_que_entra']} (lo fijo {al['lo_fijo_gb']} GB)")
    if not dk["ok"]:
        raise Freno(DOCKER, f"Docker al lanzar: VM {dk['mem_total_bytes']} bytes (tope {dk['mem_total_max_bytes']}), contenedor {dk['salud']}")
    for nombre in ("sin_codificador", "con_codificador"):
        L, P = lotes[nombre], P_de[nombre]
        ids = set(L["ids"])
        controlado = False
        while True:
            st = estado(e, salida)
            desconocidas = [k for k, v in st["por_sesion"].items() if v["final"] and v["final"]["clase"] == "desconocida"]
            config_mal = [k for k, v in st["por_sesion"].items() if v["final"] and v["final"]["clase"] == "configuracion"]
            if config_mal:
                raise Freno(PRECONDICION, f"{len(config_mal)} sesiones con un inventario de herramientas que no es el de su configuración")
            if len(desconocidas) >= MAX_FORMAS_DESCONOCIDAS:
                raise Freno(FORMAS_DESCONOCIDAS, f"{len(desconocidas)} formas desconocidas")
            pend = [v for k, v in st["por_sesion"].items() if v["pendiente"] and k in ids]
            if not pend:
                reg.evento(evento=f"lote {nombre} terminado", clases_finales=st["clases_finales"])
                break
            if nombre == "con_codificador" and not controlado:
                c = CM.control_lote_con(P, cli_max())
                reg.evento(evento="memoria antes del lote con codificador", memoria=c)
                print(f"antes del lote con codificador: lo fijo {c['lo_fijo_gb']} GB, swap {c['swap_gb']} GB, CLI más alto "
                      f"{c['cli_max_gb']} GB; P = {P} ({'entra' if c['entra'] else 'NO entra'}; entra hasta {c['P_que_entra']})",
                      flush=True)
                if not c["entra"]:
                    raise Freno(MEMORIA, f"antes del lote con codificador no entra P = {P}: entra hasta {c['P_que_entra']} "
                                         f"(lo fijo {c['lo_fijo_gb']} GB, {c['huella_por_sesion_gb']} GB por sesión)")
                controlado = True
            gj = gasto_juez(salida / "juez" / "cache")["usd"]
            por_juzgar = sum(1 for v in st["por_sesion"].values() if not v["final"] or v["final"]["clase"] in ("completa", "infraestructura"))
            reserva = round(por_juzgar * RESERVA_JUEZ_POR_RESPUESTA, 6)
            gastado = st["gasto_agente_guarda_usd"] + gj
            freno_l, tope_l = round(e["freno_usd"] - gastado - reserva, 6), round(e["tope_usd"] - gastado - reserva, 6)
            if freno_l < e["presupuesto_por_sesion_usd"]:
                reg.evento(evento="freno del gasto antes del lote", gastado=gastado, reserva_juez=reserva, freno_del_lote=freno_l)
                raise Freno(FRENO_GASTO, f"gastado {gastado:.4f} + reserva del juez {reserva:.4f}: no entra otra sesión antes del freno")
            k = numero_de_lote(salida)
            out = salida / "agente" / f"lote_{k:02d}"
            lote_p = salida / "agente" / f"lote_{k:02d}.json"
            lote_p.parent.mkdir(parents=True, exist_ok=True)
            lote_p.write_text(json.dumps({"lote_n6": nombre, "sesiones": [
                {"id": v["siguiente_id"], "brazo": v["sesion"]["brazo"], "pregunta": ps[v["sesion"]["qid"]]["pregunta"],
                 "bloque": v["sesion"]["qid"]} for v in pend]}, ensure_ascii=False) + "\n", encoding="utf-8")
            a = argparse.Namespace(entrada=Path(e["_ruta"]), sha256_entrada=e["_sha"], lote=lote_p, out=out, sesiones=sesiones_root,
                                   paralelo=P, modo="real", via=via, tope=tope_l, freno=freno_l, presupuesto_sesion=None,
                                   lanzador=e["lanzador"]["ruta"], timeout_s=timeout_s, config_agentes=e["config_agentes"]["ruta"])
            guarda = GuardaTanda(nombre, P, huella_sin if nombre == "sin_codificador" else huella_con)
            reg.evento(evento="lanza el lote", lote=k, lote_n6=nombre, sesiones=len(pend),
                       reintentos=sum(1 for v in pend if v["intentos"]), gastado=round(gastado, 6), reserva_juez=reserva,
                       freno_del_lote=freno_l, tope_del_lote=tope_l, P=P)
            print(f"lote {k} ({nombre}): {len(pend)} sesiones ({sum(1 for v in pend if v['intentos'])} reintentos), P = {P}; "
                  f"gastado USD {gastado:.4f}, reserva del juez {reserva:.4f}, freno del lote {freno_l:.4f}", flush=True)
            previa = R5.BASE.G
            R5.BASE.G = guarda
            try:
                lote = LoteN6(a, guarda)
                codigo = lote.correr()
            except SystemExit as x:
                if isinstance(x.code, int) or x.code is None:
                    raise
                raise Freno(LOTE_INVALIDO, str(x))
            finally:
                R5.BASE.G = previa
            disco = []
            for v in pend:
                d = out / v["siguiente_id"]
                if (d / f"meta_{v['siguiente_id']}.json").is_file():
                    cd = CR.control_disco(d, v["siguiente_id"])
                    if cd["FRENA"]:
                        disco.append(v["siguiente_id"])
            reg.evento(evento="terminó el lote", lote=k, lote_n6=nombre, codigo=codigo, freno=lote.motivo_freno,
                       freno_de_la_guarda_de_la_tanda=guarda.freno and guarda.freno[1],
                       acumulado_R9_usd=round(lote.acumulado, 6), sesiones={x: sum(1 for s in lote.sesiones if s["estado"] == x)
                                                                           for x in sorted({s["estado"] for s in lote.sesiones})},
                       control_disco_frena=disco)
            print(f"lote {k} ({nombre}): código {codigo}; R9 del lote USD {lote.acumulado:.4f}", flush=True)
            if disco:
                raise Freno(DISCO, f"{len(disco)} sesiones con un resultado de herramienta como referencia a disco")
            if codigo and guarda.freno:
                raise Freno(*guarda.freno)
            if codigo:
                raise Freno(codigo, f"el lote {k} frenó: {lote.motivo_freno}")
    st = estado(e, salida)
    reg.evento(evento="agente terminado", clases_finales=st["clases_finales"], gasto_agente_R9_usd=st["gasto_agente_R9_usd"])
    print(f"agente: las {len(st['por_sesion'])} sesiones terminadas; clases {st['clases_finales']}; "
          f"R9 USD {st['gasto_agente_R9_usd']:.4f}", flush=True)
    return 0


def controles(e: dict, P_sin: int, P_con: int, salida: Path) -> int:
    """La acción `controles` (USD 0, antes de cargar la clave): lo fijo y el swap, las dos P y Docker, impresos."""
    ids_sin = set(next(x for x in e["lotes"] if x["nombre"] == "sin_codificador")["ids"])
    hs = huellas_medidas(salida, ids_sin) if (salida / "agente").exists() else {}
    huella = max([CM.HUELLA_SESION_SIN_CODIFICADOR_GB] + [h.get("total_gb", 0.0) for h in hs.values()])
    al = CM.control_al_lanzar(P_sin, P_con, huella)
    dk = CM.docker()
    print(json.dumps({"lo_fijo_gb": al["lo_fijo_gb"], "swap_gb": al["swap_gb"], "sin_codificador": al["sin_codificador"],
                      "con_codificador": al["con_codificador"], "docker": dk}, ensure_ascii=False))
    if not al["entra"]:
        print(f"FRENO (código {MEMORIA}): no entra la P; sin codificador entra hasta {al['sin_codificador']['P_que_entra']} y con "
              f"codificador hasta {al['con_codificador']['P_que_entra']}")
        return MEMORIA
    if not dk["ok"]:
        print(f"FRENO (código {DOCKER}): Docker: VM {dk['mem_total_bytes']} bytes (tope {dk['mem_total_max_bytes']}), "
              f"contenedor {dk['salud']}")
        return DOCKER
    return 0


# --------------------------------------------------------------------------- #
# El juez                                                                      #
# --------------------------------------------------------------------------- #
def id_opaco(qid: str, cid: str, rep: int, sha_resp: str) -> str:
    return PREFIJO_ID + sha256_texto(f"{SAL_ID_OPACO}|{qid}|{cid}|{rep}|{sha_resp}")[:10]


def casos_del_juez(e: dict, salida: Path) -> tuple[list[dict], list[dict]]:
    """(casos, faltantes): un caso por sesión con su intento final completo y una respuesta no vacía, en el orden ciego."""
    st = estado(e, salida)
    ps = e["_preguntas"]
    casos, faltan = [], []
    for k, v in st["por_sesion"].items():
        s, f = v["sesion"], v["final"]
        base = {"id_sesion": k, "qid": s["qid"], "configuracion": s["configuracion"], "rep": s["rep"]}
        if f is None or v["pendiente"]:
            faltan.append(base | {"motivo": "sin correr"}); continue
        if f["clase"] != "completa":
            faltan.append(base | {"motivo": f["clase"], "intento": f["id"]}); continue
        m = json.loads((Path(f["carpeta"]) / f"meta_{f['id']}.json").read_text(encoding="utf-8"))
        r = (m.get("final_json_R4") or {}).get("respuesta")
        if not isinstance(r, str) or not r.strip():
            faltan.append(base | {"motivo": "sin respuesta en el JSON final", "intento": f["id"]}); continue
        sha = sha256_texto(r)
        casos.append(base | {"intento": f["id"], "respuesta": r, "sha256_respuesta": sha,
                             "id_opaco": id_opaco(s["qid"], s["configuracion"], s["rep"], sha),
                             "pregunta": ps[s["qid"]]["pregunta"], "criterios": ps[s["qid"]]["criterios"],
                             "respondible_flag": (m.get("final_json_R4") or {}).get("respondible")})
    casos.sort(key=lambda c: (c["qid"], c["sha256_respuesta"], c["configuracion"], c["rep"]))
    if len({c["id_opaco"] for c in casos}) != len(casos):
        raise Freno(PRECONDICION, "colisión de ids opacos")
    random.Random(SEMILLA_ORDEN_JUEZ).shuffle(casos)
    return casos, faltan


def verificar_ceguera(casos: list[dict], cfg: dict) -> list[str]:
    """El pedido es el del juez de EV2 (construir_kwargs) con la pregunta, la respuesta y los criterios, y nada más: sin la
    respuesta (que no se edita), no trae un id de sesión, de configuración ni de brazo."""
    marcas = [PREFIJO_ID, "N6-", "id_opaco", "respondible"] + sorted(cfg["configuraciones_n6"]) + sorted(cfg["brazos"])
    fugas = []
    for c in casos:
        kw = J.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        if set(kw) != {"model", "max_tokens", "temperature", "system", "messages"} or kw["system"] != J.PROMPT_JUEZ:
            fugas.append("estructura del pedido")
        sin_resp = J.construir_mensaje_usuario(c["pregunta"], "<respuesta>", c["criterios"])
        fugas += [f"marca {x}" for x in marcas if x in sin_resp and not re.fullmatch(r"[A-Z]", x)]
    return fugas


def factory_real(cache_dir: Path):
    def f(rep: int, label: str):
        return J.construir_cliente_real(rep, run_label=label, cache_dir=cache_dir, db_prefix=DB_PREFIX)
    return f


def factory_juez_falso(cache_dir: Path):
    """Solo para una entrada seca: el cliente falso del juez de la corrida en seco de A2.2 (corrida_en_seco_a2_2.ClienteJuezFalso,
    sin editarlo), envuelto en la caché sellada como el real, con la base y el espacio de nombres de cada repetición."""
    import corrida_en_seco_a2_2 as CS            # noqa: PLC0415  (A2.2: solo import)
    lc = J.lc

    def f(rep: int, label: str):
        cache_dir.mkdir(parents=True, exist_ok=True)
        return lc.CachingClient(CS.ClienteJuezFalso(rep), domain="juez_ev2", db_path=db_juez(rep, cache_dir),
                                namespace=lc.make_namespace(f"juez_ev2_r{rep}", code_ver=J.CODE_VER, thinking=False),
                                thinking_enabled=False, run_label=label)
    return f


def costo_mayor(juez_dir: Path) -> float:
    por: dict[str, dict] = {}
    for rep in REPS_JUEZ:
        for r in leer_jsonl(juez_dir / f"veredictos_r{rep}.jsonl"):
            por.setdefault(r["id_opaco"], {})[rep] = (r["meta"]["input_tokens"] / 1e6 * PRECIO_JUEZ_IN
                                                     + r["meta"]["output_tokens"] / 1e6 * PRECIO_JUEZ_OUT)
    completas = [sum(v.values()) for v in por.values() if len(v) == len(REPS_JUEZ)]
    return max(completas) if completas else RESERVA_JUEZ_POR_RESPUESTA


def correr_juez(e: dict, salida: Path, reg: Registro, client_factory=None, python_sdk: str | None = None,
                cada_guarda: int = 25) -> int:
    juez_dir, cache_dir = salida / "juez", salida / "juez" / "cache"
    if e["modo"] == "seco" and client_factory is None:
        raise Freno(PRECONDICION, "una entrada seca nunca llama al juez real (--juez-falso)")
    resumen = {"inicio": ahora(), "instrumento": JA.controlar_instrumento()}
    resumen["sdk"] = JA.control_sdk(python_sdk)
    casos, faltan = casos_del_juez(e, salida)
    sin_correr = [f for f in faltan if f["motivo"] == "sin correr"]
    if sin_correr:
        raise Freno(PRECONDICION, f"faltan {len(sin_correr)} sesiones del agente: el juez corre después del agente entero")
    fugas = verificar_ceguera(casos, e["_cfg"])
    if fugas:
        raise Freno(PRECONDICION, f"fuga en los pedidos del juez (nada se llamó): {sorted(set(fugas))}")
    juez_dir.mkdir(parents=True, exist_ok=True)
    des = juez_dir / "desanonimizacion_SOLO_MESA"
    des.mkdir(exist_ok=True)
    for p, obj in ((juez_dir / "orden_juez_n6.json", {"semilla": SEMILLA_ORDEN_JUEZ, "n": len(casos),
                                                      "ids_opacos_en_orden": [c["id_opaco"] for c in casos]}),
                   (des / "tabla_id_opaco_n6_SOLO_MESA.json",
                    {"SOLO_MESA": True, "sal_id_opaco": SAL_ID_OPACO, "prefijo": PREFIJO_ID, "n": len(casos),
                     "filas": sorted(({k: c[k] for k in ("id_opaco", "id_sesion", "intento", "qid", "configuracion", "rep",
                                                         "sha256_respuesta", "respondible_flag")} for c in casos),
                                     key=lambda f: f["id_opaco"])})):
        nuevo = json.dumps(obj, ensure_ascii=False, indent=1) + "\n"
        if p.exists() and p.read_text(encoding="utf-8") != nuevo:
            raise Freno(PRECONDICION, f"{p.name} ya existe y difiere de lo recomputado")
        p.write_text(nuevo, encoding="utf-8")
    gasto_ag = estado(e, salida)["gasto_agente_guarda_usd"]
    factory = client_factory or factory_real(cache_dir)
    clientes = {rep: factory(rep, f"n6_juez_r{rep}") for rep in REPS_JUEZ}
    hechos = {rep: {r["id_opaco"] for r in leer_jsonl(juez_dir / f"veredictos_r{rep}.jsonl")}
             | {r["id_opaco"] for r in leer_jsonl(juez_dir / f"errores_r{rep}.jsonl")} for rep in REPS_JUEZ}
    llamadas = errores = 0
    freno = None
    try:
        for k, c in enumerate(casos, 1):
            pend = [rep for rep in REPS_JUEZ if c["id_opaco"] not in hechos[rep]]
            if not pend:
                continue
            if k % cada_guarda == 1:
                otro = G.otro_paso_pago()
                if otro:
                    freno = (OTRO_PASO_PAGO, f"otro paso pago corriendo antes de la respuesta {k} del juez: {otro}")
                    break
            g = gasto_ag + gasto_juez(cache_dir)["usd"]
            mayor = costo_mayor(juez_dir)
            if g + mayor > e["freno_usd"] or g + mayor > e["tope_usd"]:
                freno = (FRENO_JUEZ, f"gastado {g:.4f} + {mayor:.4f} > freno {e['freno_usd']} (tope {e['tope_usd']}) antes "
                                     f"de la respuesta {k} de {len(casos)}")
                break
            for rep in pend:
                with (juez_dir / f"veredictos_r{rep}.jsonl").open("a", encoding="utf-8") as fh, \
                        (juez_dir / f"errores_r{rep}.jsonl").open("a", encoding="utf-8") as fe:
                    try:
                        r = J.juzgar(clientes[rep], c["pregunta"], c["respuesta"], c["criterios"])
                    except ValueError as x:
                        fe.write(json.dumps({"id_opaco": c["id_opaco"], "rep": rep, "error": str(x), "ts": ahora()},
                                            ensure_ascii=False) + "\n")
                        errores += 1
                        continue
                    fh.write(json.dumps({"id_opaco": c["id_opaco"], "rep": rep,
                                         "clasificacion_respuesta": r["veredicto"]["clasificacion_respuesta"],
                                         "criterios": r["veredicto"]["criterios"], "meta": r["meta"]}, ensure_ascii=False) + "\n")
                    llamadas += 1
            if k % 20 == 0:
                print(f"juez: {k} de {len(casos)} respuestas; gasto total USD {gasto_ag + gasto_juez(cache_dir)['usd']:.4f}",
                      flush=True)
    finally:
        for cl in clientes.values():
            if hasattr(cl, "close"):
                cl.close()
    agg = agregar(juez_dir, casos)
    (juez_dir / "agregados_n6_ciego.json").write_text(json.dumps(agg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (juez_dir / "faltantes_n6.json").write_text(json.dumps(faltan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    resumen |= {"n_respuestas": len(casos), "faltantes_del_agente": dict(Counter(f["motivo"] for f in faltan)),
                "llamadas_nuevas": llamadas, "errores_nuevos": errores, "gasto_juez": gasto_juez(cache_dir),
                "gasto_agente_guarda_usd": gasto_ag, "n_agregados": agg["n_agregados"], "n_incompletas": len(agg["incompletas"]),
                "freno": None if freno is None else freno[1], "fin": ahora()}
    (juez_dir / "resumen_juez_n6.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    reg.evento(evento="juez", **{k: resumen[k] for k in ("n_respuestas", "faltantes_del_agente", "llamadas_nuevas",
                                                        "errores_nuevos", "gasto_juez", "n_agregados", "n_incompletas", "freno")})
    print(f"juez: {len(casos)} respuestas, {agg['n_agregados']} agregadas, {len(agg['incompletas'])} incompletas, "
          f"{errores} errores nuevos; juez USD {resumen['gasto_juez']['usd']:.4f}", flush=True)
    if freno:
        raise Freno(*freno)
    return 0


def agregar(juez_dir: Path, casos: list[dict]) -> dict:
    """Por id opaco, el veredicto modal de cada criterio (mapping.veredicto_modal) y el de la pregunta, con las tres repeticiones;
    las que no tienen las tres, aparte."""
    por_rep = {rep: {r["id_opaco"]: r for r in leer_jsonl(juez_dir / f"veredictos_r{rep}.jsonl")} for rep in REPS_JUEZ}
    agregados, incompletas = [], []
    for c in casos:
        regs = [por_rep[rep].get(c["id_opaco"]) for rep in REPS_JUEZ]
        if any(r is None for r in regs):
            incompletas.append({"id_opaco": c["id_opaco"], "reps_faltantes": [rep for rep, r in zip(REPS_JUEZ, regs) if r is None]})
            continue
        n = len(c["criterios"])
        modales = [M.veredicto_modal([r["criterios"][i]["veredicto"] for r in regs]) for i in range(n)]
        clas = [r["clasificacion_respuesta"] for r in regs]
        v, nv = Counter(clas).most_common(1)[0]
        agregados.append({"id_opaco": c["id_opaco"], "n_criterios": n, "modales": modales,
                          "veredicto_pregunta": M.veredicto_pregunta(modales),
                          "veredictos_reps": [[r["criterios"][i]["veredicto"] for r in regs] for i in range(n)],
                          "clasificacion_respuesta_modal": v if nv > len(clas) / 2 else "sin_consenso",
                          "tokens_reps": [{k: r["meta"][k] for k in ("input_tokens", "output_tokens")} for r in regs]})
    return {"semilla_orden": SEMILLA_ORDEN_JUEZ, "reps": len(REPS_JUEZ), "n_casos": len(casos), "n_agregados": len(agregados),
            "incompletas": incompletas, "agregados": agregados}


# --------------------------------------------------------------------------- #
def fijar_patron_de_prueba(token: str) -> dict:
    """Solo con un CLI falso en el PATH: la guarda de otro paso pago busca un token propio con la forma del patrón real, así
    ningún `pgrep` de una prueba lleva en su línea de comandos el nombre de un paso pago."""
    if not cli_falso():
        raise Freno(PRECONDICION, "el patrón de prueba solo corre con un CLI falso en el PATH")
    if not re.fullmatch(r"[a-z][a-z0-9_]{11,}", token) or re.search(r"lanzar|correr|juez", token) \
            or any(re.search(G.PATRON_PAGO_REAL, token + s) for s in (".py", "_b63.py", "_r5.py", "_n6.py")):
        raise Freno(PRECONDICION, "el token de prueba no es un token propio")
    G.PATRON_PAGO = "|".join(re.escape(token) + s for s in (r"\.py", r"_b63\.py", r"_r5\.py", r"_n6\.py"))
    return {"patron_de_prueba": G.PATRON_PAGO}


def main(argv: list[str] | None = None, client_factory=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("accion", choices=("entrada", "agente", "juez", "todo", "estado", "controles"))
    ap.add_argument("--entrada", type=Path, default=ENTRADA_DEFAULT)
    ap.add_argument("--sha256-entrada", default=None)
    ap.add_argument("--salida", type=Path, default=SALIDA_DEFAULT)
    ap.add_argument("--P-sin-codificador", type=int, default=None, help="la P del lote sin codificador (la decide la autora)")
    ap.add_argument("--P-con-codificador", type=int, default=None, help="la P del lote con codificador (la decide la autora)")
    ap.add_argument("--via", choices=("api", "bedrock"), default="api")
    ap.add_argument("--timeout-s", type=float, default=1800.0)
    ap.add_argument("--patron-de-prueba", default=None, help="solo con un CLI falso: el token de la guarda")
    ap.add_argument("--sin-neo4j", action="store_true", help="solo con un CLI falso y una entrada seca: sin el control del Neo4j")
    ap.add_argument("--juez-falso", action="store_true", help="solo con un CLI falso y una entrada seca: el juez falso de A2.2")
    # Solo para `entrada`:
    ap.add_argument("--modo-entrada", choices=("real", "seco"), default="real")
    ap.add_argument("--preguntas", type=Path, default=PREGUNTAS_N3)
    ap.add_argument("--sha-preguntas", default=SHA_PREGUNTAS_N3)
    ap.add_argument("--config-agentes", type=Path, default=CONFIG_AGENTES)
    ap.add_argument("--lanzador", type=Path, default=LANZADOR)
    ap.add_argument("--tope", type=float, default=TOPE)
    ap.add_argument("--freno", type=float, default=FRENO)
    ap.add_argument("--python-citas", type=Path, default=PYTHON_CITAS)
    a = ap.parse_args(argv)
    try:
        if a.accion == "entrada":
            e = armar_entrada(a.modo_entrada, a.preguntas.resolve(), a.sha_preguntas, a.config_agentes.resolve(),
                              a.lanzador.resolve(), a.tope, a.freno, a.python_citas)
            nuevo = json.dumps(e, ensure_ascii=False, indent=1) + "\n"
            if a.entrada.exists() and a.entrada.read_text(encoding="utf-8") != nuevo:
                raise Freno(PRECONDICION, "la entrada ya existe y difiere de la que se arma")
            a.entrada.write_text(nuevo, encoding="utf-8")
            print(f"entrada ({e['modo']}): {e['orden']['n_sesiones']} sesiones de {e['preguntas']['n']} preguntas")
            print(f"{sha256_file(a.entrada)}  {rel_repo(a.entrada)}")
            return 0
        if not a.sha256_entrada:
            raise Freno(PRECONDICION, "sin --sha256-entrada no se corre nada")
        e = cargar_entrada(a.entrada, a.sha256_entrada)
        e["_ruta"], e["_sha"] = str(a.entrada.resolve()), a.sha256_entrada
        falso = cli_falso()
        if (e["modo"] == "seco") != falso:
            raise Freno(PRECONDICION, "una entrada seca corre solo con el CLI falso, y la real solo con el CLI real")
        if a.patron_de_prueba:
            fijar_patron_de_prueba(a.patron_de_prueba)
        if a.sin_neo4j and e["modo"] != "seco":
            raise Freno(PRECONDICION, "--sin-neo4j es solo para una entrada seca")
        if (client_factory is not None or a.juez_falso) and e["modo"] != "seco":
            raise Freno(PRECONDICION, "un cliente del juez distinto del real es solo para una entrada seca")
        salida = a.salida.resolve()
        if a.juez_falso:
            client_factory = factory_juez_falso(salida / "juez" / "cache")
        if salida.is_relative_to(REPO_DIR):
            raise Freno(PRECONDICION, "la salida está dentro del repo")
        if a.accion in ("agente", "todo", "controles") and not all(isinstance(x, int) and x >= 1 for x in
                                                                    (a.P_sin_codificador, a.P_con_codificador)):
            raise Freno(PRECONDICION, "faltan las dos P (--P-sin-codificador y --P-con-codificador): las decide la autora")
        if a.accion == "controles":
            return controles(e, a.P_sin_codificador, a.P_con_codificador, salida)
        if a.accion == "estado":
            st = estado(e, salida)
            print(json.dumps({"clases_finales": st["clases_finales"], "pendientes": st["pendientes"],
                              "gasto_agente_R9_usd": st["gasto_agente_R9_usd"],
                              "gasto_juez": gasto_juez(salida / "juez" / "cache")}, ensure_ascii=False))
            return 0
        reg = Registro(salida, a.sha256_entrada)
        reg.c["accion"], reg.c["P"] = a.accion, {"sin_codificador": a.P_sin_codificador, "con_codificador": a.P_con_codificador}
        foto = foto_repo()
        reg.c["foto_repo_al_empezar"] = {k: v for k, v in foto.items() if k != "_filas"}
        reg.guardar()
        try:
            reg.c["precondiciones"] = precondiciones(e, con_neo4j=not a.sin_neo4j)
            reg.guardar()
            if a.accion in ("agente", "todo"):
                correr_agente(e, salida, reg, a.P_sin_codificador, a.P_con_codificador, a.via, a.timeout_s)
            if a.accion in ("juez", "todo"):
                correr_juez(e, salida, reg, client_factory=client_factory)
            reg.c["codigo"] = 0
        finally:
            f2 = foto_repo()
            reg.c["foto_repo_al_terminar"] = {k: v for k, v in f2.items() if k != "_filas"}
            reg.c["repo_igual"] = f2["sha256"] == foto["sha256"]
            if not reg.c["repo_igual"]:
                a_ = set(foto["_filas"]); b_ = set(f2["_filas"])
                reg.c["repo_cambios"] = {"solo_al_empezar": len(a_ - b_), "solo_al_terminar": len(b_ - a_)}
            reg.c["fin"] = ahora()
            reg.guardar()
        st = estado(e, salida)
        print(f"N6: código 0; clases {st['clases_finales']}; agente R9 USD {st['gasto_agente_R9_usd']:.4f}, juez USD "
              f"{gasto_juez(salida / 'juez' / 'cache')['usd']:.4f}; repo igual: {reg.c['repo_igual']}")
        return 0
    except Freno as f:
        try:
            reg.c["codigo"], reg.c["freno"] = f.codigo, f.motivo
            reg.guardar()
        except NameError:
            pass
        print(f"FRENO (código {f.codigo}): {f.motivo}", flush=True)
        return f.codigo


if __name__ == "__main__":
    raise SystemExit(main())
