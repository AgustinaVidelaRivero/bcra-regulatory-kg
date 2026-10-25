#!/usr/bin/env python3
"""corrida_en_seco_a2_2.py — La corrida en seco de A2.2 (USD 0, sin API), por el mismo camino de imports y de código que la
corrida real (CLAUDE.md, §4.l): importa correr_a2_2 y juez_a2_2 como los importa Python al correrlos (este archivo vive en la
misma carpeta), sin tocar sys.path por fuera, y llama a sus funciones. Corre sobre una copia del repo.

  1. Las ramas del runner y del juez, con sesiones sintéticas (la Corrida del runner con `lanzar` reemplazado, como en A2.1) y
     el cliente falso del juez (un cliente que arma la respuesta del modelo en memoria, envuelto en la caché sellada de
     `evaluacion/llm_cache.py`, con su base propia en una carpeta temporal): las pruebas en verde y con una que falla R6; N = 1
     sin las pruebas; el corte del agente; el freno del disco y su reanudación; una sesión cortada por `error_max_turns` y una
     salida mal formada del agente; una meta de otro modo; el juez con una respuesta mal formada y una `requiere_adjudicacion`;
     el corte del juez y su reanudación desde la caché; la población, las re-corridas con un voto `requiere_adjudicacion`, su
     juicio y el análisis; y el enmascarado de las sesiones.
  2. Los cinco comandos zsh de punta a punta, con un archivo de clave FALSO (A22_ENTORNO, borrado al terminar), A22_MODO=init (el
     lanzador corre cada sesión en modo init: ninguna petición llega a la API), A22_JUEZ_MODO=seco (el cliente falso), preguntas
     sintéticas con su orden (las sesiones init van a la raíz del banco, fuera del repo, como en A2.1), el intérprete del .venv del repo (A22_PYTHON y
     A22_BANCO_PYTHON_KG: la copia no lleva .venv) y un patrón de pgrep propio (A22_PATRON_PGREP, que solo rige en modo init:
     la guarda no frena por otros pasos pagos reales de la máquina). Entre paso y paso, las metas init (incompletas por R3) se reemplazan por
     sintéticas donde la rama lo pide. También las guardas: un sha256 que no da (código 6) y otro paso pago corriendo (código 7).

Imprime un renglón por rama. Uso (en la copia): BANCO_VENV_VECTOR=<venv 3.12> .venv/bin/python -B \\
  data/experiment/banco_mcp/a2_2/corrida_en_seco_a2_2.py [--sin-zsh]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

import comun_a2_2 as K                       # por su propio camino de imports (la carpeta de este archivo)
import correr_a2_2 as CR2
import juez_a2_2 as JA
import poblacion_a2_2 as PB
import analizar_a2_2 as AN

AQUI = Path(__file__).resolve().parent
REPO_DIR = K.REPO_DIR
RES = []


def rama(nombre: str, ok: bool, det: str = "") -> None:
    RES.append(bool(ok))
    print(("PASS " if ok else "FAIL ") + nombre + (f" — {det}" if det else ""), flush=True)


# --------------------------------------------------------------------------- #
# El cliente falso del juez                                                    #
# --------------------------------------------------------------------------- #
class _Mensajes:
    def __init__(self, rep: int):
        self.rep = rep

    def create(self, **kw):
        from anthropic.types import Message
        u = kw["messages"][0]["content"]
        resp = u.split("RESPUESTA:", 1)[1].split("CRITERIOS (", 1)[0]
        n = int(u.split("CRITERIOS (", 1)[1].split(")", 1)[0])
        if "[MALFORMADA]" in resp:
            texto = "no es un JSON"
        else:
            vs = []
            for i in range(n):
                if "[CORRECTA]" in resp:
                    v = "cumplido"
                elif "[INCORRECTA]" in resp:
                    v = "no_cumplido"
                elif "[DUDOSA]" in resp and i == 0:
                    v = "dudoso"
                elif "[PARCIAL]" in resp:
                    v = "cumplido" if i == 0 else "no_cumplido"
                else:
                    h = int(hashlib.sha256(f"{resp}|{i}|{self.rep}".encode()).hexdigest(), 16)
                    v = ("cumplido", "no_cumplido")[h % 2]
                vs.append({"indice": i + 1, "veredicto": v, "fragmento": None, "justificacion": "sintética"})
            clas = "abstencion" if "[ABSTENCION]" in resp else "contenido"
            texto = json.dumps({"clasificacion_respuesta": clas, "criterios": vs})
        return Message.model_validate({"id": f"msg_falso_{self.rep}", "type": "message", "role": "assistant",
                                       "model": kw["model"], "content": [{"type": "text", "text": texto}],
                                       "stop_reason": "end_turn", "stop_sequence": None,
                                       "usage": {"input_tokens": 1000, "output_tokens": 200}})


class ClienteJuezFalso:
    """Un cliente con `.messages.create` que arma en memoria la respuesta del modelo (no sale a la red). Marcas en la respuesta
    del agente: [CORRECTA], [INCORRECTA], [PARCIAL], [DUDOSA] (el primer criterio dudoso), [MALFORMADA], [ABSTENCION]."""

    def __init__(self, rep: int):
        self.messages = _Mensajes(rep)


def factory_falsa(cache_dir: Path):
    """La fábrica de clientes del juez para el modo seco: el cliente falso envuelto en la caché sellada, con la misma base por
    repetición y el mismo espacio de nombres que el cliente real del juez de EV2."""
    lc = JA.J.lc

    def f(rep: int, label: str):
        return lc.CachingClient(ClienteJuezFalso(rep), domain="juez_ev2", db_path=JA.db_path(rep, cache_dir),
                                namespace=lc.make_namespace(f"juez_ev2_r{rep}", code_ver=JA.J.CODE_VER, thinking=False),
                                thinking_enabled=False, run_label=label)
    return f


# --------------------------------------------------------------------------- #
# Sesiones sintéticas                                                          #
# --------------------------------------------------------------------------- #
def meta_sintetica(pid: str, brazo: str, modo: str, costo: float = 0.05, respuesta: str | None = "respuesta [CORRECTA]",
                   completa: bool = True, r6: bool = True, subtype: str = "success", llamadas: int = 3,
                   motivos: list | None = None) -> dict:
    return {"pregunta_id": pid, "brazo": brazo, "modo": modo, "origen": "sintetico_corrida_en_seco", "generado": "sintético",
            "tokens_R9": {"costo_recomputado": {"total_usd": costo}, "total_cost_usd_cli_solo_para_contraste": costo},
            "completitud_R3": {"completa": completa, "motivos_incompleta": motivos or ([] if completa else ["sintética"])},
            "inventario_tools_R6": {"coincide": r6}, "permission_denials": [], "duracion_s": 10.0,
            "final_json_R4": ({"respuesta": respuesta, "citas": [], "respondible": True} if respuesta is not None else None),
            "hb2": {"n_llamadas_log_r1": llamadas, "subtype": subtype, "hay_result": subtype is not None,
                    "n_mensajes_asistente": 2, "num_turns": llamadas + 1},
            "control_disco": {"FRENA": False, "largo_mayor_utf16": 10, "carpeta_tool_results": "no existe"},
            "valor_remoto_por_tool": {"archivo": "existe", "existe": True, "tools_del_banco_con_numero": []}}


class CorridaSintetica(CR2.Corrida):
    """La Corrida del runner con `lanzar` reemplazado: escribe el comando (su session_id), la meta sintética del escenario y, si
    el escenario lo pide, la transcripción con la referencia a disco y el `.claude.json` de su carpeta de configuración. El resto
    (corte, reanudación, control del disco, valor remoto, registro) es el código real."""

    def __init__(self, a, out, escenarios=None, costo=0.05):
        super().__init__(a, out)
        self.escenarios, self.costo, self.lanzadas = escenarios or {}, costo, []

    def lanzar(self, brazo, pid, pregunta, out):
        self.lanzadas.append(pid)
        sid = f"sintetica-{pid}"
        out.mkdir(parents=True, exist_ok=True)
        (out / f"comando_{pid}.json").write_text(json.dumps({"session_id": sid}), encoding="utf-8")
        e = self.escenarios.get(pid, {})
        if "transcripcion" in e:
            (out / f"sesion_{pid}.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in e["transcripcion"])
                                                    + "\n", encoding="utf-8")
        cfg = self.sesiones / "config" / sid
        cfg.mkdir(parents=True, exist_ok=True)
        (cfg / ".claude.json").write_text(json.dumps({"tengu_velvet_ibis": {}}), encoding="utf-8")
        m = meta_sintetica(pid, brazo, self.a.modo, self.costo, **e.get("meta", {}))
        (out / f"meta_{pid}.json").write_text(json.dumps(m), encoding="utf-8")
        return m


def args(td: Path, etapa: str, tope=93.0, freno=69.75, preguntas=None, sha=None, orden=None) -> argparse.Namespace:
    return argparse.Namespace(etapa=etapa, autorizado_tope=tope, freno=freno, modo="init", via="api",
                              preguntas=preguntas, sha_preguntas=sha, orden=orden, poblacion=td / "poblacion.json",
                              out_pruebas=td / "pruebas", out_n1=td / "n1", out_recorridas=td / "recorridas",
                              sesiones=td / "sesiones", timeout_s=60.0, sin_controles_externos=True)


def preguntas_sinteticas(td: Path, n: int = 4) -> tuple[Path, str]:
    p = td / "preguntas_sinteticas.json"
    p.write_text(json.dumps({"preguntas": [
        {"id": f"SINT-{i:02d}", "pregunta": f"¿Pregunta sintética número {i}?", "to": "cap",
         "gold": {"criterios": [{"criterio": f"criterio {j}", "cita_textual": f"cita {j}"} for j in range(1 + i % 2 + 1)],
                  "ancla": ["cap:1.1"]}} for i in range(1, n + 1)]}, ensure_ascii=False), encoding="utf-8")
    return p, K.sha256_file(p)


def correr_etapa(c: CorridaSintetica, a, orden, preguntas):
    try:
        CR2.correr(c, a, orden, preguntas)
        return None
    except CR2.Freno as e:
        return e


# --------------------------------------------------------------------------- #
def ramas_python() -> None:
    with tempfile.TemporaryDirectory() as tdd:
        td = Path(tdd)
        pq, sha = preguntas_sinteticas(td)
        preguntas = K.cargar_preguntas(pq, sha, real=False)
        orden = K.armar_orden(sorted(preguntas))
        a = args(td, "pruebas")
        # pruebas en verde
        c = CorridaSintetica(a, a.out_pruebas)
        e = correr_etapa(c, a, orden, preguntas)
        rama("pruebas: las tres en verde (R3 y R6)", e is None and c.registro["PASS"] and len(c.lanzadas) == 3)
        # pruebas con una que falla R6
        a2 = args(td / "x", "pruebas")
        c2 = CorridaSintetica(a2, a2.out_pruebas, {"PRB-kg": {"meta": {"r6": False}}})
        e2 = correr_etapa(c2, a2, orden, preguntas)
        rama("pruebas: una que falla R6 frena con FrenoPruebas (código 4)", isinstance(e2, CR2.FrenoPruebas))
        # N = 1 sin las pruebas
        a3 = args(td / "y", "n1")
        e3 = correr_etapa(CorridaSintetica(a3, a3.out_n1), a3, orden, preguntas)
        rama("N = 1 sin las pruebas: FrenoPrecondicion (código 5)", isinstance(e3, CR2.FrenoPrecondicion))
        rama("N = 1 con las pruebas de otra carpeta en rojo: FrenoPrecondicion",
             isinstance(correr_etapa(CorridaSintetica(args(td / "x", "n1"), args(td / "x", "n1").out_n1),
                                     args(td / "x", "n1"), orden, preguntas), CR2.FrenoPrecondicion))
        # N = 1 con escenarios: cortada, mal formada, parcial, dudosa, malformada para el juez
        an1 = args(td, "n1")
        esc = {}
        q = orden["preguntas_en_orden"]
        esc[f"N1-{q[0]}-kg"] = {"meta": {"respuesta": None, "completa": False, "subtype": "error_max_turns", "llamadas": 31,
                                         "motivos": ["result.subtype=error_max_turns", "el resultado no contiene un bloque JSON"]}}
        esc[f"N1-{q[0]}-fragmentos_bm25"] = {"meta": {"respuesta": "texto sin JSON", "completa": False,
                                                      "motivos": ["el resultado no contiene un bloque JSON"]}}
        for i, qq in enumerate(q):
            for b in K.BRAZOS:
                esc.setdefault(f"N1-{qq}-{b}", {"meta": {"respuesta": ["respuesta [PARCIAL] de los fragmentos",
                                                                       "respuesta [CORRECTA]", "respuesta [DUDOSA]",
                                                                       "respuesta [MALFORMADA]"][(i + K.BRAZOS.index(b)) % 4]}})
        cn1 = CorridaSintetica(an1, an1.out_n1, esc)
        e4 = correr_etapa(cn1, an1, orden, preguntas)
        rama("N = 1: las 12 sesiones, en el orden del pre-registro", e4 is None and cn1.lanzadas == [s["id"] for s in K.secuencia(orden, "n1")])
        # meta de otro modo
        an1b = args(td, "n1"); an1b.modo = "real"
        try:
            CorridaSintetica(an1b, an1b.out_n1).sesion(K.secuencia(orden, "n1")[0], "q", 1, 1)
            rama("una meta de otro modo aborta la corrida", False)
        except SystemExit as ex:
            rama("una meta de otro modo aborta la corrida", "ABORTO" in str(ex))
        # el corte del agente: 68 de acumulado + 1,80 > 69,75
        ac = args(td / "corte", "pruebas")
        ac.out_n1.mkdir(parents=True, exist_ok=True)
        (ac.out_n1 / "meta_previa.json").write_text(json.dumps(meta_sintetica("previa", "kg", "init", 68.0)), encoding="utf-8")
        cc = CorridaSintetica(ac, ac.out_pruebas)
        e5 = correr_etapa(cc, ac, orden, preguntas)
        rama("el corte del agente: 68,00 + 1,80 > 69,75 frena sin lanzar, sumando las metas de las tres carpetas",
             isinstance(e5, CR2.Freno) and not isinstance(e5, (CR2.FrenoDisco, CR2.FrenoPruebas)) and cc.lanzadas == [])
        (ac.out_n1 / "meta_previa.json").write_text(json.dumps(meta_sintetica("previa", "kg", "init", 67.92)), encoding="utf-8")
        cc2 = CorridaSintetica(ac, ac.out_pruebas)
        e5b = correr_etapa(cc2, ac, orden, preguntas)
        rama("el corte del agente: con 67,92 la primera se lanza (69,72 ≤ 69,75) y frena la segunda (69,77)",
             isinstance(e5b, CR2.Freno) and len(cc2.lanzadas) == 1, f"{len(cc2.lanzadas)} lanzadas")
        # el freno del disco y su reanudación
        ad = args(td / "disco", "pruebas")
        ref = {"type": "user", "message": {"content": [{"type": "tool_result", "tool_use_id": "t1",
                                                        "content": "<persisted-output>ruta con un espacio/x.txt</persisted-output>"}]}}
        cd = CorridaSintetica(ad, ad.out_pruebas, {"PRB-fragmentos_bm25": {"transcripcion": [ref]}})
        e6 = correr_etapa(cd, ad, orden, preguntas)
        cd2 = CorridaSintetica(ad, ad.out_pruebas)
        e6b = correr_etapa(cd2, ad, orden, preguntas)
        rama("el freno del disco: una referencia a disco frena (código 3), y al reanudar vuelve a frenar sin lanzar",
             isinstance(e6, CR2.FrenoDisco) and isinstance(e6b, CR2.FrenoDisco) and cd2.lanzadas == [])
        # el juez de N = 1 con el cliente falso
        jd = td / "juez"
        rj = JA.etapa("n1", modo="seco", preguntas=preguntas, orden=orden, resultados_dir=an1.out_n1, juez_dir=jd,
                      cache_dir=jd / "cache", poblacion=None, freno=18.75, tope=25.0, client_factory=factory_falsa(jd / "cache"))
        rama("juez N = 1: la cortada y la mal formada del agente quedan fuera (incompletas por R3)",
             rj["faltantes_por_motivo"] == {"incompleta por R3": 2} and rj["n_respuestas"] == 10)
        agg = json.loads((jd / "n1" / "agregados_n1_ciego.json").read_text(encoding="utf-8"))
        dist = agg["distribucion"]
        rama("juez N = 1: una salida mal formada del juez queda incompleta y una dudosa da requiere_adjudicacion",
             len(agg["incompletas"]) > 0 and dist.get("requiere_adjudicacion", 0) > 0 and sum(agg["errores_por_rep"].values()) > 0,
             json.dumps(dist))
        rama("juez N = 1: el control del SDK corrió primero y dio OK", rj["sdk"]["control_sdk"] == "OK")
        tab = json.loads((jd / "n1" / "desanonimizacion_SOLO_MESA" / "tabla_id_opaco_n1_SOLO_MESA.json").read_text(encoding="utf-8"))
        orden_j = json.loads((jd / "n1" / "orden_juez_n1.json").read_text(encoding="utf-8"))
        rama("juez N = 1: la tabla de desanonimización aparte y el orden ciego sin brazos ni preguntas",
             tab["n"] == 10 and not any(b in json.dumps(orden_j) for b in K.BRAZOS + tuple(preguntas)))
        # el corte del juez y su reanudación desde la caché
        jd2 = td / "juez_corte"
        shutil.copytree(an1.out_n1, td / "n1_copia")
        f2 = factory_falsa(jd2 / "cache")
        r1 = JA.etapa("n1", modo="seco", preguntas=preguntas, orden=orden, resultados_dir=td / "n1_copia", juez_dir=jd2,
                      cache_dir=jd2 / "cache", poblacion=None, freno=0.05, tope=25.0, client_factory=f2)
        r2 = JA.etapa("n1", modo="seco", preguntas=preguntas, orden=orden, resultados_dir=td / "n1_copia", juez_dir=jd2,
                      cache_dir=jd2 / "cache", poblacion=None, freno=18.75, tope=25.0, client_factory=f2)
        f1 = r1["gasto_juez_a2_2"]["filas"]
        rama("el corte del juez: con freno 0,05 frena antes de pasarlo (acumulado más el mayor juzgado, 0,0378 sin ninguno)",
             bool(r1["FRENO_JUEZ"]) and 0 < f1 < rj["gasto_juez_a2_2"]["filas"] and f1 % 3 == 0
             and r1["gasto_juez_a2_2"]["usd"] <= 0.05, f"{f1} llamadas, USD {r1['gasto_juez_a2_2']['usd']}")
        rama("el juez sigue desde lo hecho: la reanudación no repite ninguna llamada",
             r2["FRENO_JUEZ"] is None and r2["gasto_juez_a2_2"]["filas"] == rj["gasto_juez_a2_2"]["filas"]
             and r2["n_agregados"] == rj["n_agregados"])
        # la población y las re-corridas
        pob = PB.derivar(PB.veredictos_por_par(jd, "n1"), sorted(preguntas))
        (td / "poblacion.json").write_text(json.dumps(pob), encoding="utf-8")
        rama("población: derivada del juez de N = 1", pob["n_pares"] > 0, f"{pob['n_pares']} pares")
        arc = args(td, "recorridas")
        escr = {}
        for s in K.secuencia(orden, "recorridas", pob):
            escr[s["id"]] = {"meta": {"respuesta": "respuesta [DUDOSA]" if s["rep"] == 2 else "respuesta [CORRECTA]"}}
        crc = CorridaSintetica(arc, arc.out_recorridas, escr)
        e7 = correr_etapa(crc, arc, orden, preguntas)
        rama("re-corridas: 3 por par de la población, por repetición", e7 is None and len(crc.lanzadas) == 3 * pob["n_pares"])
        JA.etapa("recorridas", modo="seco", preguntas=preguntas, orden=orden, resultados_dir=arc.out_recorridas, juez_dir=jd,
                 cache_dir=jd / "cache", poblacion=pob, freno=18.75, tope=25.0, client_factory=factory_falsa(jd / "cache"))
        ag = PB.agregar_recorridas(pob, PB.veredictos_por_par(jd, "recorridas"))
        rama("re-corridas: un voto requiere_adjudicacion entre dos correctos deja el par decidido (invariante)",
             ag["n_agregados"] == pob["n_pares"] and all(p["final"] == "correcto" and p["via"] == "invariante_con_pendiente"
                                                         for p in ag["pares"]))
        # el análisis sobre todo eso
        cola = set(json.loads(K.COLA.read_text(encoding="utf-8"))["ids"])
        res = AN.analizar(preguntas=preguntas, juez_dir=jd, poblacion=pob, dirs_agente={"n1": an1.out_n1, "recorridas": arc.out_recorridas},
                          cola_ids=cola, e0=AN.cargar_e0(), adjudicaciones={})
        rama("análisis: corre sobre la salida sintética, con lo sin veredicto final listado y R5 por brazo",
             res["n_preguntas"] == 4 and res["n_sin_veredicto_final"] > 0 and res["r5_por_brazo"]["kg"]["pasan_de_30"] == 1
             and res["r5_por_brazo"]["kg"]["cortadas"] == 1, f"{res['n_sin_veredicto_final']} sin final")
        # el enmascarado de las sesiones sintéticas (una carpeta personal de prueba)
        casa = "/home/usuario_de_prueba"
        raiz = td / "raiz"
        d = raiz / "data/experiment/banco_mcp/a2_2/resultados/recorridas"
        d.mkdir(parents=True)
        cwd = casa + "/INGENIERIA IA/TESIS/fuera_del_repo/banco_sesiones/cwd"
        (d / "stream_RC1-x-kg.jsonl").write_text(json.dumps({"type": "system", "subtype": "init", "cwd": cwd}) + "\n", encoding="utf-8")
        sc = AQUI / "enmascarar_cwd_a2_2.py"
        js = td / "enm.json"
        ok = all(subprocess.run([sys.executable, "-B", str(sc), *x], capture_output=True, text=True).returncode == 0 for x in
                 (["--calcular", str(raiz), str(js)], ["--probar", str(raiz), str(js)],
                  ["--aplicar", str(raiz), str(js), "--originales", str(td / "orig")]))
        rama("enmascarado de las sesiones: calcular, probar y aplicar con los originales fuera de la raíz",
             ok and "usuario_de_prueba" not in (d / "stream_RC1-x-kg.jsonl").read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# Los cinco comandos, de punta a punta                                         #
# --------------------------------------------------------------------------- #
def zsh(paso: str, env: dict) -> subprocess.CompletedProcess:
    return subprocess.run(["zsh", str(AQUI / paso)], env=env, capture_output=True, text=True, timeout=3600)


def reemplazar(out: Path, ids: list[str], escenario) -> None:
    """Reemplaza las metas init de esas sesiones por sintéticas (modo init), donde la rama pide una respuesta."""
    for i, pid in enumerate(ids):
        m = json.loads((out / f"meta_{pid}.json").read_text(encoding="utf-8"))
        nueva = meta_sintetica(pid, m["brazo"], "init", 0.0, **escenario(i, pid))
        (out / f"meta_{pid}.json").write_text(json.dumps(nueva), encoding="utf-8")


def ramas_zsh() -> None:
    sha_list = AQUI / "sha256_tramo1_a2_2.txt"
    if not sha_list.exists():
        rama("los comandos: falta a2_2/sha256_tramo1_a2_2.txt", False); return
    with tempfile.TemporaryDirectory() as tdd:
        td = Path(tdd)
        clave = td / "clave_falsa.env"
        clave.write_text("ANTHROPIC_API_KEY=sk-ant-clave-falsa-de-la-corrida-en-seco\n", encoding="utf-8")
        pq, sha = preguntas_sinteticas(td, n=2)
        preguntas = K.cargar_preguntas(pq, sha, real=False)
        orden = K.armar_orden(sorted(preguntas))
        po = td / "orden_sintetico.json"
        po.write_text(json.dumps(orden, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        py = sys.executable          # el python del .venv del repo con que corre esta corrida en seco (la copia no lleva .venv)
        env = {"PATH": os.environ["PATH"], "HOME": os.environ["HOME"], "A22_ENTORNO": str(clave), "A22_MODO": "init",
               "A22_JUEZ_MODO": "seco", "A22_PYTHON": py, "A22_BANCO_PYTHON_KG": os.environ.get("BANCO_PYTHON_KG", py),
               "A22_PREGUNTAS": str(pq), "A22_SHA_PREGUNTAS": sha, "A22_ORDEN": str(po),
               "BANCO_VENV_VECTOR": os.environ["BANCO_VENV_VECTOR"],
               # el patrón de pgrep de la corrida en seco: su propio proceso testigo y los pasos de A2.2 (rige solo con A22_MODO=init)
               "A22_PATRON_PGREP": r"correr_juez_v2_de_la_corrida_en_seco\.py|correr_a2_2\.py|juez_a2_2\.py"}
        for d in (K.OUT_PRUEBAS, K.OUT_N1, K.OUT_RECORRIDAS, K.JUEZ_DIR, K.POBLACION.parent):
            if d.exists():
                shutil.rmtree(d)
        # las guardas
        guardado = sha_list.read_text(encoding="utf-8")
        mal = guardado.replace(guardado.split()[0], "0" * 64, 1)
        sha_list.write_text(mal, encoding="utf-8")
        g6 = zsh("paso1_pruebas.zsh", env)
        sha_list.write_text(guardado, encoding="utf-8")
        rama("guardas: un sha256 que no da frena con el código 6", g6.returncode == 6 and "FRENO" in g6.stdout, g6.stdout.strip()[-80:])
        p = subprocess.Popen([sys.executable, "-c", "import sys; sys.stdin.read()", "correr_juez_v2_de_la_corrida_en_seco.py"],
                             stdin=subprocess.PIPE)
        try:
            g7 = zsh("paso1_pruebas.zsh", env)
        finally:
            p.stdin.close(); p.wait(timeout=30)
        rama("guardas: otro paso pago corriendo frena con el código 7", g7.returncode == 7 and "FRENO" in g7.stdout)
        # paso 1: las pruebas en modo init (sin resultado del modelo) fallan R3 y frenan con el código 4
        p1 = zsh("paso1_pruebas.zsh", env)
        rama("paso 1 (init): las tres pruebas sin resultado fallan R3 y el comando frena con el código 4",
             p1.returncode == 4 and len(list(K.OUT_PRUEBAS.glob("meta_*.json"))) == 3, (p1.stdout + p1.stderr).strip()[-160:])
        p2a = zsh("paso2_n1.zsh", env)
        rama("paso 2 con las pruebas en rojo: frena con el código 5", p2a.returncode == 5, p2a.stdout.strip()[-120:])
        reemplazar(K.OUT_PRUEBAS, [s["id"] for s in K.secuencia(orden, "pruebas")], lambda i, pid: {})
        p2 = zsh("paso2_n1.zsh", env)
        rama("paso 2 (init): las 6 sesiones de N = 1 de las 2 preguntas sintéticas", p2.returncode == 0
             and len(list(K.OUT_N1.glob("meta_*.json"))) == 6, (p2.stdout + p2.stderr).strip()[-160:])
        ids1 = [s["id"] for s in K.secuencia(orden, "n1")]
        reemplazar(K.OUT_N1, ids1, lambda i, pid: {"respuesta": "respuesta [PARCIAL]" if i % 2 == 0 else "respuesta [CORRECTA]"})
        p3 = zsh("paso3_juez_n1.zsh", env)
        pob = json.loads(K.POBLACION.read_text(encoding="utf-8")) if K.POBLACION.exists() else {"n_pares": 0, "pares": []}
        rama("paso 3 (seco): el control del SDK, el juez de N = 1 y la población", p3.returncode == 0 and pob["n_pares"] > 0
             and "control del SDK: 5 de 5 en OK" in p3.stdout, (p3.stdout + p3.stderr).strip()[-200:])
        rama("paso 3: no imprime ningún veredicto ni brazo", not any(x in p3.stdout for x in ("correcto", "parcial", "incorrecto")
                                                                       + K.BRAZOS))
        p4 = zsh("paso4_recorridas.zsh", env)
        n_rc = len(list(K.OUT_RECORRIDAS.glob("meta_*.json")))
        rama("paso 4 (init): las re-corridas de la población, 3 por par", p4.returncode == 0 and n_rc == 3 * pob["n_pares"],
             f"{n_rc} sesiones; " + (p4.stdout + p4.stderr).strip()[-120:])
        ids_rc = [s["id"] for s in K.secuencia(orden, "recorridas", pob)]
        reemplazar(K.OUT_RECORRIDAS, ids_rc[: len(ids_rc) // 2], lambda i, pid: {"respuesta": "respuesta [CORRECTA]"})
        p5 = zsh("paso5_juez_recorridas.zsh", env)
        rama("paso 5 (seco): el control del SDK y el juez de las re-corridas", p5.returncode == 0
             and "control del SDK: 5 de 5 en OK" in p5.stdout, (p5.stdout + p5.stderr).strip()[-200:])
        # el enmascarado sobre las sesiones init reales de la corrida en seco (traen el cwd de verdad)
        js = td / "enmascarado.json"
        sc = AQUI / "enmascarar_cwd_a2_2.py"
        e1 = subprocess.run([sys.executable, "-B", str(sc), "--calcular", str(REPO_DIR), str(js)], capture_output=True, text=True)
        e2 = subprocess.run([sys.executable, "-B", str(sc), "--probar", str(REPO_DIR), str(js)], capture_output=True, text=True)
        rama("enmascarado de las sesiones init de los comandos: calcular y probar", e1.returncode == 0 and e2.returncode == 0,
             e1.stdout.strip() + " | " + e2.stdout.strip()[:80])
        for d in (K.OUT_PRUEBAS, K.OUT_N1, K.OUT_RECORRIDAS, K.JUEZ_DIR, K.POBLACION.parent):
            if d.exists():
                shutil.rmtree(d)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--sin-zsh", action="store_true")
    a = ap.parse_args(argv)
    if (REPO_DIR / ".git").exists():
        raise SystemExit("la corrida en seco corre sobre una copia del repo, no sobre el repo")
    ramas_python()
    if not a.sin_zsh:
        ramas_zsh()
    print(f"corrida en seco de A2.2: {sum(RES)} de {len(RES)} ramas en PASS")
    return 0 if all(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
