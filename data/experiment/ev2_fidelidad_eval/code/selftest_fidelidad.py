"""
selftest_fidelidad.py — Selftest OFFLINE (cero API, cero costo) del pipeline de
evaluación de fidelidad EV2 (fase A.c).

Parte 1 — insumos REALES, solo lectura:
  sellos del instrumento y del cuarteto; carga 120 = 40 × 3 grafos = 3 por
  pregunta, 164 criterios; ids opacos únicos; orden §3 reproducible y coincidente
  con orden/; tabla de des-anonimización coincidente y FUERA de out/; los 120
  requests reales que se mandarían al juez son EXACTAMENTE prompt + (pregunta,
  respuesta, criterios), sin marcador alguno de grafo/label/id ni veredicto.

Parte 2 — pipeline completo con CLIENTE FALSO sobre casos sintéticos (4
preguntas × 3 variantes = 12 respuestas), bajo el CachingClient real:
  persistencia write-through por id opaco; N=3 con tres dbs, keys disjuntas,
  0 cross-hits, 0 hits en primera pasada (re-muestreo real) y replay = hit;
  mapping §2 por las cuatro vías (correcto / incorrecto / parcial /
  requiere_adjudicacion por dudoso Y por sin_consenso); clasificación auxiliar;
  auditoría de fragmentos con los cuatro estados provocados a propósito;
  freno por proyección (frena antes de llamar y la re-lanzada retoma sin pagar
  dos veces); error de parseo registrado y respuesta declarada incompleta;
  ceguera: ningún request contiene grafo/variante/id opaco/veredicto previo;
  ningún archivo de out/ contiene grafo, id de pregunta ni variante; la tabla
  sí los contiene y vive aparte; cruce_mesa.py (herramienta de la revisión)
  reproduce sobre los datos SINTÉTICOS el cruce esperado por construcción.

Además: tests_mapping.py del juez (20 checks) y auditoria_fragmentos.py
idéntica, línea a línea, a la regla de analisis_acuerdo.py.

Correr:  .venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/selftest_fidelidad.py
"""

from __future__ import annotations

import hashlib
import json
import random
import shutil
import subprocess
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(CODE_DIR))
import comun_fidelidad as cf                       # noqa: E402
from comun_fidelidad import juez, mapping           # noqa: E402
import llm_cache as lc                              # noqa: E402  (vía juez → evaluacion/)
import pipeline_fidelidad as pf                     # noqa: E402
import auditoria_fragmentos as af                   # noqa: E402
import cruce_mesa                                   # noqa: E402

OUT = cf.UNIDAD_DIR / "selftest_out"
CHECKS: list[tuple[str, bool]] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    CHECKS.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}{(' — ' + detalle) if detalle else ''}")


# --------------------------------------------------------------------------- #
# Parte 1 — insumos reales                                                    #
# --------------------------------------------------------------------------- #
def parte_real() -> None:
    print("== 1. sellos e insumos reales (offline) ==")
    sellos = cf.verificar_sellos()
    check("prompt v1 sha256 esperado", sellos["prompt_juez_v1.md"] == cf.PROMPT_SHA256_ESPERADO)
    check("cuarteto 4/4 intacto", all(sellos[k] == v for k, v in cf.CUARTETO.items()))
    check("JUEZ_PROMPT_VERSION = v1", juez.PROMPT_VERSION == "v1")
    check("modelo del juez claude-sonnet-4-6 / temp 0", juez.MODELO == "claude-sonnet-4-6" and juez.TEMPERATURE == 0.0)

    gold, respuestas, censo, casos = cf.cargar_todo()
    check("120 respuestas cargadas", censo["n_respuestas"] == 120)
    check("40 por grafo (3 grafos)", censo["por_grafo"] == {"run_3": 40, "v2": 40, "v3": 40}, str(censo["por_grafo"]))
    check("3 respuestas por pregunta, 40 preguntas", censo["respuestas_por_pregunta"] == {3: 40})
    check("164 criterios en el gold", censo["n_criterios_gold"] == 164)
    check("pregunta de cada traza == pregunta del gold", not censo["pregunta_traza_distinta_del_gold"])
    ids = [c["id_opaco"] for c in casos]
    check("120 ids opacos únicos", len(set(ids)) == 120)
    check("ids opacos con prefijo y 10 hex", all(i.startswith("EV2R-") and len(i) == 15 for i in ids))
    check("sin empates en la clave de orden (id_pregunta, sha256 respuesta)",
          not casos[0]["empates_clave_orden"])

    # orden reproducible desde la regla
    clave = sorted(((c["id_pregunta"], c["sha256_respuesta"], c["id_opaco"]) for c in casos))
    ids_ordenados = [x[2] for x in clave]
    random.Random(cf.SEMILLA_ORDEN).shuffle(ids_ordenados)
    check("orden = shuffle(semilla) sobre sorted(id_pregunta, sha256)", ids_ordenados == ids)
    p_ord = cf.ORDEN_DIR / "orden_ev2_fidelidad_ciego.json"
    p_tab = cf.DESANON_DIR / "tabla_id_opaco.json"
    check("orden/ persistido y coincidente", p_ord.exists()
          and json.loads(p_ord.read_text())["ids_opacos_en_orden"] == ids)
    check("orden/ no contiene grafo ni ids de pregunta",
          p_ord.exists() and not cf.buscar_marcadores(p_ord.read_text(), ["EV2F-", "\"id_pregunta\""]))
    tab = json.loads(p_tab.read_text()) if p_tab.exists() else {}
    check("tabla de des-anonimización persistida (120 filas, fuera de out/)",
          p_tab.exists() and tab.get("n") == 120 and cf.OUT_DIR not in p_tab.parents)
    check("tabla reproduce los ids desde la regla",
          all(cf.id_opaco(f["id_pregunta"], f["grafo"], f["sha256_respuesta"]) == f["id_opaco"]
              for f in tab.get("filas", [])))
    check("tabla: 40 ids por grafo", tab and
          sorted(__import__("collections").Counter(f["grafo"] for f in tab["filas"]).values()) == [40, 40, 40])
    check("sha256 de respuesta de la tabla == sha256 del texto que viaja al juez",
          tab and all(cf.sha256_texto(next(c["respuesta"] for c in casos if c["id_opaco"] == f["id_opaco"]))
                      == f["sha256_respuesta"] for f in tab["filas"]))

    # los 120 requests reales: exactos y sin fuga
    ciegos = cf.vista_ciega(casos)
    check("vista ciega sin grafo/label/id_pregunta/flag/sha",
          all(set(c) == {"id_opaco", "pregunta", "respuesta", "criterios"} for c in ciegos))
    fugas, exactos, claves_ok = [], 0, 0
    marcas_extra = ["EV2F-", "EV2R-", "id_opaco", "respondible"]
    # NOTA: la no-fuga de veredicto se garantiza por igualdad estructural del
    # request (abajo), no por palabras: 'cumplido' es vocabulario normativo legítimo.
    for c in ciegos:
        kw = juez.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        claves_ok += set(kw) == {"model", "max_tokens", "temperature", "system", "messages"}
        exactos += (kw["system"] == juez.PROMPT_JUEZ and kw["messages"] == [
            {"role": "user", "content": juez.construir_mensaje_usuario(
                c["pregunta"], c["respuesta"], c["criterios"])}])
        u = kw["messages"][0]["content"]
        fugas += [(c["id_opaco"], m) for m in cf.buscar_marcadores(u, marcas_extra)]
    check("120/120 requests reales con claves exactas", claves_ok == 120, str(claves_ok))
    check("120/120 requests reales == prompt + (pregunta, respuesta, criterios)", exactos == 120)
    check("0 marcadores de grafo/id/veredicto en los 120 mensajes de usuario reales", not fugas, str(fugas[:5]))
    check("system prompt sin marcadores de grafo", not cf.buscar_marcadores(juez.PROMPT_JUEZ))
    check("censo_carga.json persistido", (cf.CARGA_DIR / "censo_carga.json").exists())


# --------------------------------------------------------------------------- #
# Parte 2 — pipeline sintético con cliente falso                              #
# --------------------------------------------------------------------------- #
# 4 preguntas sintéticas × 3 variantes (juegan el rol de los 3 grafos, con
# nombres neutros). Guion: por (qid, variante) → clasificación, veredictos por
# rep (lista por criterio) y fragmento por criterio (para provocar los cuatro
# estados de la auditoría). Cada pregunta tiene 2 criterios.
VARIANTES = ("alfa", "beta", "gamma")
GOLD_SYN = {
    f"SYN-{i:03d}": {"pregunta": f"¿Pregunta sintética número {i}?", "to": "syn",
                     "criterios": [{"criterio": f"Criterio sintético 1 de la pregunta {i}",
                                    "cita_textual": f"cita normativa uno de la pregunta {i} texto gold único"},
                                   {"criterio": f"Criterio sintético 2 de la pregunta {i}",
                                    "cita_textual": f"cita normativa dos de la pregunta {i} texto gold único"}]}
    for i in range(1, 5)}
RESP_SYN = {(q, v): f"Respuesta sintética pregunta {int(q[-3:])} variante {k}: fragmento uno de la {int(q[-3:])}. "
                    f"Luego fragmento dos de la {int(q[-3:])}."
            for q in GOLD_SYN for k, v in enumerate(VARIANTES, start=1)}
# fragmento: "A" = verbatim (fragmento uno de la i), None = null, "GOLD" = copia de la
# cita del gold (fuga_gold), "X" = texto inexistente (no_verbatim)
GUION = {
    # (qid, variante): (clasif, {rep: [v_c1, v_c2]}, [frag_c1, frag_c2], esperado)
    ("SYN-001", "alfa"):  ("contenido", {1: ["cumplido", "cumplido"], 2: ["cumplido", "cumplido"], 3: ["cumplido", "cumplido"]}, ["A", "A"], "correcto"),
    ("SYN-001", "beta"):  ("abstencion", {1: ["no_cumplido"] * 2, 2: ["no_cumplido"] * 2, 3: ["no_cumplido"] * 2}, [None, None], "incorrecto"),
    ("SYN-001", "gamma"): ("contenido", {1: ["cumplido", "no_cumplido"], 2: ["cumplido", "no_cumplido"], 3: ["no_cumplido", "no_cumplido"]}, ["A", None], "parcial"),
    ("SYN-002", "alfa"):  ("contenido", {1: ["cumplido", "dudoso"], 2: ["cumplido", "dudoso"], 3: ["cumplido", "dudoso"]}, ["A", "GOLD"], "requiere_adjudicacion"),
    ("SYN-002", "beta"):  ("contenido", {1: ["cumplido", "cumplido"], 2: ["cumplido", "no_cumplido"], 3: ["cumplido", "dudoso"]}, ["A", "X"], "requiere_adjudicacion"),
    ("SYN-002", "gamma"): ("contenido", {1: ["cumplido"] * 2, 2: ["cumplido"] * 2, 3: ["cumplido"] * 2}, ["A", "A"], "correcto"),
    ("SYN-003", "alfa"):  ("contenido", {1: ["cumplido"] * 2, 2: ["cumplido"] * 2, 3: ["cumplido"] * 2}, ["A", "A"], "correcto"),
    ("SYN-003", "beta"):  ("contenido", {1: ["no_cumplido", "cumplido"], 2: ["no_cumplido", "cumplido"], 3: ["no_cumplido", "cumplido"]}, [None, "A"], "parcial"),
    ("SYN-003", "gamma"): ("abstencion", {1: ["no_cumplido"] * 2, 2: ["no_cumplido"] * 2, 3: ["no_cumplido"] * 2}, [None, None], "incorrecto"),
    ("SYN-004", "alfa"):  ("contenido", {1: ["cumplido"] * 2, 2: ["cumplido"] * 2, 3: ["cumplido"] * 2}, ["A", "A"], "correcto"),
    ("SYN-004", "beta"):  ("contenido", {1: ["cumplido", "cumplido"], 2: ["cumplido", "no_cumplido"], 3: ["cumplido", "cumplido"]}, ["A", "A"], "correcto"),
    ("SYN-004", "gamma"): ("contenido", {1: ["no_cumplido"] * 2, 2: ["no_cumplido"] * 2, 3: ["no_cumplido"] * 2}, [None, None], "incorrecto"),
}
# ERROR provocado: (SYN-004, gamma) rep 2 devuelve JSON mal formado (criterio faltante)
ERROR_EN = ("SYN-004", "gamma", 2)
# Cruce esperado por construcción (variante → veredicto), sin la incompleta
CRUCE_ESPERADO = {
    "alfa": {"correcto": 3, "requiere_adjudicacion": 1},
    "beta": {"incorrecto": 1, "requiere_adjudicacion": 1, "parcial": 1, "correcto": 1},
    "gamma": {"parcial": 1, "correcto": 1, "incorrecto": 1},   # SYN-004/gamma incompleta
}


class ClienteFalso:
    """Debajo de CachingClient: devuelve Messages del SDK construidos desde el
    guion, identificando el caso por el sha del texto de la respuesta que llega
    en el request — o sea, SOLO por lo que efectivamente ve el juez."""

    def __init__(self, rep: int, registro: list, sha_a_caso: dict):
        self._rep, self._registro, self._s2c = rep, registro, sha_a_caso
        self.messages = self

    def create(self, **kwargs):
        from anthropic.types import Message
        self._registro.append({"rep": self._rep, "kwargs": kwargs})
        u = kwargs["messages"][0]["content"]
        resp_txt = u.split("RESPUESTA:\n", 1)[1].split("\n\nCRITERIOS (", 1)[0]
        qid, variante = self._s2c[cf.sha256_texto(resp_txt)]
        clasif, por_rep, frags, _ = GUION[(qid, variante)]
        vs = por_rep[self._rep]
        crits = []
        for i, v in enumerate(vs):
            f = frags[i]
            frag = (None if f is None else
                    f"fragmento uno de la {int(qid[-3:])}" if f == "A" else
                    GOLD_SYN[qid]["criterios"][i]["cita_textual"] if f == "GOLD" else
                    "texto que no está en ningún lado")
            crits.append({"indice": i + 1, "veredicto": v, "fragmento": frag,
                          "justificacion": f"scripteado-{hashlib.md5(f'{qid}{variante}{i}{self._rep}'.encode()).hexdigest()[:12]}"})
        if (qid, variante, self._rep) == ERROR_EN:
            crits = crits[:1]   # criterio faltante → parsear_veredicto levanta
        cuerpo = {"clasificacion_respuesta": clasif, "criterios": crits}
        texto = json.dumps(cuerpo, ensure_ascii=False)
        return Message.model_validate({
            "id": f"fake_{qid}_{variante}_r{self._rep}", "type": "message", "role": "assistant",
            "model": "cliente-falso", "stop_reason": "end_turn", "stop_sequence": None,
            "content": [{"type": "text", "text": texto}],
            "usage": {"input_tokens": len(kwargs["system"]) // 4 + len(u) // 4,
                      "output_tokens": len(texto) // 4}})


def parte_sintetica() -> None:
    print("== 2. pipeline sintético (cliente falso + caché real) ==")
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "cache").mkdir(parents=True)
    (OUT / "out").mkdir(parents=True)

    respuestas = [{"id_pregunta": q, "grafo": v, "label": f"syn_base_{v}", "respuesta": RESP_SYN[(q, v)],
                   "respondible_flag": None, "pregunta_traza": GOLD_SYN[q]["pregunta"]}
                  for q in GOLD_SYN for v in VARIANTES]
    casos = cf.armar_casos(respuestas, GOLD_SYN)
    check("12 casos sintéticos, ids únicos", len(casos) == 12 and len({c["id_opaco"] for c in casos}) == 12)
    p_ord, p_tab = cf.persistir_orden_y_tabla(casos, OUT / "orden", OUT / "desanonimizacion")
    tabla = json.loads(p_tab.read_text())
    id2gv = {f["id_opaco"]: (f["id_pregunta"], f["grafo"]) for f in tabla["filas"]}
    ciegos = cf.vista_ciega(casos)
    sha_a_caso = {cf.sha256_texto(RESP_SYN[(q, v)]): (q, v) for (q, v) in RESP_SYN}

    registro: list = []

    def factory(rep: int, label: str):
        return lc.CachingClient(
            ClienteFalso(rep, registro, sha_a_caso), domain="juez_ev2",
            db_path=OUT / "cache" / f"{cf.DB_PREFIX}_r{rep}.db",
            namespace=lc.make_namespace(f"juez_ev2_r{rep}", code_ver=juez.CODE_VER, thinking=False),
            thinking_enabled=False, run_label=label)

    # --- freno por proyección: tope minúsculo → frena antes de llamar ---
    freno_chico = pf.FrenoProyeccion(OUT / "cache", 3, 3.0, 15.0, tope=0.0001,
                                     total_llamadas=36, min_filas=3)
    f = pf.correr(ciegos, reps=3, out_dir=OUT / "out", client_factory=factory,
                  freno=freno_chico, verbose=False)
    n_llamadas_freno = len(registro)
    check("freno por proyección frenó (con ≥3 filas observadas)",
          f is not None and f["hechas"] == 3 and n_llamadas_freno == 3, str(f))
    check("freno: proyección > tope declarada", f is not None and f["proyeccion_usd"] > f["tope_usd"])

    # --- re-lanzada con tope amplio: retoma sin repetir llamadas ---
    freno_ok = pf.FrenoProyeccion(OUT / "cache", 3, 3.0, 15.0, tope=100.0, total_llamadas=36)
    f2 = pf.correr(ciegos, reps=3, out_dir=OUT / "out", client_factory=factory,
                   freno=freno_ok, verbose=False)
    check("re-lanzada completa sin freno", f2 is None)
    check("36 llamadas en total (3 + 33), ninguna repetida", len(registro) == 36, str(len(registro)))
    dbs = sorted((OUT / "cache").glob("*.db"))
    check("3 dbs de caché separadas (ev2_eval_r1..3)", [p.name for p in dbs] ==
          [f"{cf.DB_PREFIX}_r{r}.db" for r in (1, 2, 3)])
    ver = pf.verificar_cross_hits(dbs)
    check("keys por db = 12", all(n == 12 for n in ver["keys_por_db"].values()), str(ver["keys_por_db"]))
    check("0 cross-hits (keys pairwise disjuntas)", ver["cross_hits"] == 0, str(ver["intersecciones"]))
    check("0 hits (re-muestreo real, incluida la re-lanzada)", ver["hits_total"] == 0, str(ver["hits_por_label"]))
    check("labels por rep = ev2_eval_r{rep}", all(list(d) == [f"ev2_eval_r{r}"] for r, d in
                                                  zip((1, 2, 3), (ver["hits_por_label"][p.name] for p in dbs))))
    gasto = pf.gasto_dbs(OUT / "cache", 3, 3.0, 15.0)
    check("gasto desde dbs: 36 filas, tokens > 0", gasto["filas"] == 36 and gasto["input_tokens"] > 0)

    # --- never-pay-twice: replay de un caso de rep 1 → hit y mismo veredicto ---
    replay = lc.CachingClient(
        ClienteFalso(1, [], sha_a_caso), domain="juez_ev2",
        db_path=OUT / "cache" / f"{cf.DB_PREFIX}_r1.db",
        namespace=lc.make_namespace("juez_ev2_r1", code_ver=juez.CODE_VER, thinking=False),
        thinking_enabled=False, run_label="selftest_replay")
    c0 = next(c for c in ciegos if id2gv[c["id_opaco"]] != ("SYN-004", "gamma"))
    r_replay = juez.juzgar(replay, c0["pregunta"], c0["respuesta"], c0["criterios"])
    st = replay.stats(); replay.close()
    primera = next(json.loads(l) for l in (OUT / "out" / "veredictos_r1.jsonl").read_text().splitlines()
                   if json.loads(l)["id_opaco"] == c0["id_opaco"])
    check("replay = hit (never-pay-twice)", st["hits"] == 1 and st["misses"] == 0)
    check("replay reproduce el veredicto persistido", r_replay["veredicto"]["criterios"] == primera["criterios"])

    # --- persistencia + error + agregación + mapping ---
    por_rep, errores = pf.cargar_veredictos(OUT / "out", 3)
    check("persistidos 12/12/11 (rep 2 con 1 error)", [len(por_rep[r]) for r in (1, 2, 3)] == [12, 11, 12])
    check("error de parseo registrado en errores_r2.jsonl (1)", [len(errores[r]) for r in (1, 2, 3)] == [0, 1, 0]
          and "criterios" in errores[2][0]["error"])
    agg = pf.agregar(OUT / "out", 3, ciegos)
    check("agregados 11 + 1 incompleta (rep faltante [2])", agg["n_agregados"] == 11 and
          agg["incompletas"] == [{"id_opaco": next(i for i, gv in id2gv.items() if gv == ("SYN-004", "gamma")),
                                  "reps_faltantes": [2]}])
    por_id = {a["id_opaco"]: a for a in agg["agregados"]}
    ok_map = True
    for a in agg["agregados"]:
        q, v = id2gv[a["id_opaco"]]
        esperado = GUION[(q, v)][3]
        if a["veredicto_pregunta"] != esperado:
            ok_map = False
            print(f"    mapping: {q}/{v} esperado {esperado} obtenido {a['veredicto_pregunta']}")
    check("mapping §2: 11/11 veredictos esperados (4 vías cubiertas)", ok_map)
    vias = {a["veredicto_pregunta"] for a in agg["agregados"]}
    check("las cuatro salidas del mapping aparecen", vias == set(mapping.VEREDICTOS_PREGUNTA))
    id_sinc = next(i for i, gv in id2gv.items() if gv == ("SYN-002", "beta"))
    id_dudo = next(i for i, gv in id2gv.items() if gv == ("SYN-002", "alfa"))
    check("sin_consenso visible (SYN-002/beta c2) y dudoso unánime (SYN-002/alfa c2)",
          por_id[id_sinc]["criterios"][1]["modal"] == "sin_consenso"
          and por_id[id_dudo]["criterios"][1]["modal"] == "dudoso")
    check("distribución completa: 3 veredictos por par", all(len(c["veredictos_reps"]) == 3
                                                          for a in agg["agregados"] for c in a["criterios"]))
    check("clasificación auxiliar persistida (abstencion ×3 en SYN-001/beta)",
          por_id[next(i for i, gv in id2gv.items() if gv == ("SYN-001", "beta"))]["clasificacion_respuesta_reps"]
          == ["abstencion"] * 3)
    # auditoría de fragmentos: estados provocados
    aud = agg and pf.distribucion(agg)["auditoria_fragmentos"]
    check("auditoría: fuga_gold detectada (SYN-002/alfa c2 ×3)",
          por_id[id_dudo]["criterios"][1]["auditoria_fragmentos_reps"] == ["fuga_gold"] * 3)
    check("auditoría: no_verbatim detectado (SYN-002/beta c2 ×3)",
          por_id[id_sinc]["criterios"][1]["auditoria_fragmentos_reps"] == ["no_verbatim"] * 3)
    check("auditoría: null y verbatim presentes; total = 66 = 11 casos × 2 × 3",
          aud["null"] > 0 and aud["verbatim"] > 0 and sum(aud.values()) == 66, str(aud))
    check("auditoría: fuga_gold total 3, no_verbatim total 3", aud["fuga_gold"] == 3 and aud["no_verbatim"] == 3)

    # --- ceguera de los requests ---
    check("requests capturados = 36", len(registro) == 36)
    check("request sin campos extra", all(set(r["kwargs"]) == {"model", "max_tokens", "temperature", "system", "messages"}
                                          for r in registro))
    check("system == prompt del juez verbatim", all(r["kwargs"]["system"] == juez.PROMPT_JUEZ for r in registro))
    por_sha = {cf.sha256_texto(c["respuesta"]): c for c in ciegos}

    def caso_de(r):
        u = r["kwargs"]["messages"][0]["content"]
        return por_sha[cf.sha256_texto(u.split("RESPUESTA:\n", 1)[1].split("\n\nCRITERIOS (", 1)[0])]
    check("mensaje de usuario == (pregunta, respuesta, criterios) y nada más",
          all(r["kwargs"]["messages"] == [{"role": "user", "content": juez.construir_mensaje_usuario(
              caso_de(r)["pregunta"], caso_de(r)["respuesta"], caso_de(r)["criterios"])}] for r in registro))
    payload = json.dumps([r["kwargs"]["messages"] for r in registro], ensure_ascii=False)
    marcas_syn = list(VARIANTES) + ["syn_base_", "id_opaco", "EV2R-", "grafo", "label", "respondible"]
    check("payloads sin grafo/variante/label/id opaco", not cf.buscar_marcadores(payload, marcas_syn),
          str(cf.buscar_marcadores(payload, marcas_syn)))
    justifs = [c["justificacion"] for rep in por_rep.values() for r in rep.values() for c in r["criterios"]]
    check("payloads sin rastro de veredicto alguno (justificaciones de reps previas ausentes)",
          all(j not in payload for j in justifs) and "scripteado" not in payload)
    check("payloads de rep 2/3 no contienen fragmentos de salida de rep 1 fuera de la respuesta",
          all(k not in payload for k in ("\"veredicto\"", "clasificacion_respuesta")))

    # --- ceguera de out/ ---
    textos_out = {p.name: p.read_text(encoding="utf-8") for p in (OUT / "out").glob("*") if p.is_file()}
    marcas_out = list(VARIANTES) + ["syn_base_", "SYN-00", "\"id_pregunta\"", "\"grafo\"", "\"label\"", "EV2F-"]
    fugas_out = {n: cf.buscar_marcadores(t, marcas_out) for n, t in textos_out.items()}
    fugas_out = {n: f for n, f in fugas_out.items() if f}
    # veredictos_agregados_ciego.json y reporte se escriben acá para auditar
    agg["verificacion_cross_hits"] = ver
    dist = pf.distribucion(agg)
    agg["distribucion"] = dist
    (OUT / "out" / "veredictos_agregados_ciego.json").write_text(json.dumps(agg, ensure_ascii=False, indent=2))
    (OUT / "out" / "reporte_ciego.md").write_text(pf.reporte_ciego_md(
        agg, dist, ver, gasto, {"selftest": "sí"}, {"n_respuestas": 12, "por_grafo": "n/d (selftest)",
                                                    "preguntas_distintas": 4, "respuestas_por_pregunta": {3: 4},
                                                    "n_criterios_gold": 8, "respondible_flag": {}}, None))
    textos_out = {p.name: p.read_text(encoding="utf-8") for p in (OUT / "out").glob("*") if p.is_file()}
    fugas_out = {n: cf.buscar_marcadores(t, marcas_out) for n, t in textos_out.items()}
    fugas_out = {n: f for n, f in fugas_out.items() if f}
    check("out/ (veredictos, errores, agregados, reporte) sin grafo/variante/id de pregunta",
          not fugas_out, str(fugas_out))
    check("tabla de des-anonimización SÍ contiene grafo e id de pregunta y vive fuera de out/",
          "grafo" in p_tab.read_text() and "SYN-001" in p_tab.read_text() and (OUT / "out") not in p_tab.parents)

    # --- cruce de la mesa sobre datos SINTÉTICOS ---
    cruce = cruce_mesa.cruzar(agg, tabla)
    check("cruce_mesa reproduce el cruce esperado por construcción (sintético)",
          cruce["veredicto_por_grafo"] == CRUCE_ESPERADO, str(cruce["veredicto_por_grafo"]))
    check("cruce_mesa: 11 filas + 1 incompleta atribuida", cruce["n_filas"] == 11 and
          cruce["incompletas_por_grafo"] == {"gamma": 1})


def parte_estatica() -> None:
    print("== 3. mapping del juez y regla de auditoría ==")
    r = subprocess.run([sys.executable, "-B", str(cf.JUEZ_DIR / "tests_mapping.py")],
                       capture_output=True, text=True, cwd=str(cf.JUEZ_DIR))
    check("tests_mapping.py del juez PASS", r.returncode == 0 and "FAIL" not in r.stdout,
          r.stdout.strip().splitlines()[-1] if r.stdout.strip() else r.stderr[-200:])
    import inspect
    origen = (cf.JUEZ_DIR / "analisis_acuerdo.py").read_text(encoding="utf-8")
    import textwrap
    for fn in (af._plano, af.estado_fragmento):
        src = textwrap.dedent(inspect.getsource(fn))
        # en analisis_acuerdo.py las funciones viven anidadas (indentadas 4 espacios)
        anidada = textwrap.indent(src, "    ")
        check(f"auditoria_fragmentos.{fn.__name__} idéntica a analisis_acuerdo.py", anidada in origen)


def main() -> int:
    parte_real()
    parte_sintetica()
    parte_estatica()
    fallos = [n for n, ok in CHECKS if not ok]
    print(f"\nRESULTADO: {'PASS ✅' if not fallos else 'FAIL ❌'} ({len(CHECKS) - len(fallos)}/{len(CHECKS)} checks)")
    if fallos:
        print("fallos:", fallos)
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
