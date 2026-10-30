#!/usr/bin/env python3
"""selftest_analizar_n7c.py — La prueba de n7c/analizar_n7c.py sobre un B2 de juguete, USD 0: sin modelo, sin Neo4j y sin el
instrumento real de B2 (las preguntas, la E0 y el índice son de juguete).

Arma, en una carpeta de trabajo nueva:
  - el índice por punto de juguete (mcp_kg/selftest_familias_nav_rel_amp.py) y su E0 (estructura_jug.json);
  - seis preguntas sintéticas: JUG-1, JUG-2 y JUG-6 de dato directo (un ancla), JUG-3 y JUG-4 de varios puntos y subtipo
    remisión (anclas 1.1 y 2.2), JUG-5 de varios puntos y subtipo excepción en hijo (anclas 5 y 8); dos criterios cada una;
  - su entrada seca (correr_n7c, con la configuración del humo: una sesión por configuración, 18 sesiones);
  - las 18 sesiones, como las deja el lanzador: meta, stream con su `result` y log R1 con las salidas reales del navegador de
    juguete de cada configuración (NavegadorCand para N7, NavegadorRel para N7c y NavegadorRelAmp para N7c+). N7 abre con
    ver_punto solo la primera ancla; N7c y N7c+, todas. N7 llega a 31 llamadas en JUG-6; N7c queda cortada por R5 en JUG-4;
  - el juez: correr_n6.correr_juez con el juez falso de A2.2 y una marca más, [TOLERANTE], cuya salida trae comillas sin
    escapar en un fragmento (la lectura estricta la rechaza y la tolerante la lee). N7c+ tiene [TOLERANTE] en JUG-1 y la salida
    mal formada en JUG-3 (que ninguna lectura lee).
Casos, contra lo escrito a mano:
  A1 el juez: 6 salidas rechazadas por la estricta, 3 leídas por la tolerante y 3 a las que no aplica; los agregados estrictos
     recomputados son los del corredor; las filas estrictas son las de analizar_n6.cargar_sesiones;
  A2 la fidelidad con la lectura tolerante (N7 8/12, N7c 8/10, N7c+ 8/10; en dato directo 4/6 las tres) y la estricta de N7c+
     (6/8 y 2/4);
  A3 las de varios puntos que consultaron todas las anclas: N7 0 de 3, N7c 3 de 3, N7c+ 3 de 3; por subtipo;
  A4 las citas: cita fundada N7 5 de 6, N7c 5 de 6 (la cortada no tiene JSON final), N7c+ 6 de 6;
  A5 el tope: N7 1 (31 llamadas), N7c 1 (cortada por R5), N7c+ 0;
  A6 la regla: N7c no cumple (iii) y N7c+ cumple (i) a (iv): se adopta N7c+;
  A7 la regla sola, con medidas armadas a mano: (iv) que falla da N7c; (ii) que falla en las dos da N7; el borde de 5 puntos y
     del 5 % cumple y apenas más no; una fracción igual no «sube»; una medida que falta no cumple.
Escribe un JSON sin rutas ni horas (dos corridas dan el mismo archivo) y sale con 1 si algo falla.
Uso: <python del .venv> -B data/experiment/banco_mcp/n7c/selftest_analizar_n7c.py --trabajo <carpeta nueva> --salida <json>
     [--python-citas <python 3.12>]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
if str(AQUI.parent / "mcp_kg") not in sys.path:
    sys.path.insert(0, str(AQUI.parent / "mcp_kg"))
import analizar_n7c as A7                                  # noqa: E402
import selftest_familias_nav_rel_amp as ST                 # noqa: E402

C7, CN, AN = A7.C7, A7.CN, A7.AN
CONFIG_HUMO = AQUI / "config_agentes_n7c_humo.json"
MODELO = "claude-sonnet-5"
PREGUNTAS = {"JUG-1": ("dato_directo", None, ["1.1."]), "JUG-2": ("dato_directo", None, ["1.1."]),
             "JUG-3": ("varios_puntos", "remision", ["1.1.", "2.2."]), "JUG-4": ("varios_puntos", "remision", ["1.1.", "2.2."]),
             "JUG-5": ("varios_puntos", "excepcion_en_hijo", ["5.", "8."]), "JUG-6": ("dato_directo", None, ["4."])}
MARCA = {"N7": {"JUG-1": "[CORRECTA]", "JUG-2": "[INCORRECTA]", "JUG-3": "[CORRECTA]", "JUG-4": "[INCORRECTA]",
                "JUG-5": "[CORRECTA]", "JUG-6": "[CORRECTA]"},
         "N7c": {"JUG-1": "[CORRECTA]", "JUG-2": "[INCORRECTA]", "JUG-3": "[CORRECTA]", "JUG-4": None,
                 "JUG-5": "[CORRECTA]", "JUG-6": "[CORRECTA]"},
         "N7c_amp": {"JUG-1": "[TOLERANTE]", "JUG-2": "[INCORRECTA]", "JUG-3": "[MALFORMADA]", "JUG-4": "[CORRECTA]",
                     "JUG-5": "[CORRECTA]", "JUG-6": "[CORRECTA]"}}


# --------------------------------------------------------------------------- #
# El juez falso, con la marca [TOLERANTE]                                      #
# --------------------------------------------------------------------------- #
def factory_juez(cache_dir: Path):
    import corrida_en_seco_a2_2 as CS             # noqa: PLC0415  (A2.2: solo import)
    from anthropic.types import Message           # noqa: PLC0415
    lc = CN.J.lc

    class _Mensajes:
        def __init__(self, rep: int):
            self.base, self.rep = CS._Mensajes(rep), rep

        def create(self, **kw):
            u = kw["messages"][0]["content"]
            resp = u.split("RESPUESTA:", 1)[1].split("CRITERIOS (", 1)[0]
            if "[TOLERANTE]" not in resp:
                return self.base.create(**kw)
            n = int(u.split("CRITERIOS (", 1)[1].split(")", 1)[0])
            crits = ", ".join(f'{{"indice": {i}, "veredicto": "cumplido", "fragmento": "dice "esto" tal cual", '
                              f'"justificacion": "sintética"}}' for i in range(1, n + 1))
            texto = '{"clasificacion_respuesta": "contenido", "criterios": [' + crits + "]}"
            return Message.model_validate({"id": f"msg_falso_{self.rep}", "type": "message", "role": "assistant",
                                           "model": kw["model"], "content": [{"type": "text", "text": texto}],
                                           "stop_reason": "end_turn", "stop_sequence": None,
                                           "usage": {"input_tokens": 1000, "output_tokens": 200}})

    class _Cliente:
        def __init__(self, rep: int):
            self.messages = _Mensajes(rep)

    def f(rep: int, label: str):
        cache_dir.mkdir(parents=True, exist_ok=True)
        return lc.CachingClient(_Cliente(rep), domain="juez_ev2", db_path=CN.db_juez(rep, cache_dir),
                                namespace=lc.make_namespace(f"juez_ev2_r{rep}", code_ver=CN.J.CODE_VER, thinking=False),
                                thinking_enabled=False, run_label=label)
    return f


# --------------------------------------------------------------------------- #
# El B2 de juguete                                                             #
# --------------------------------------------------------------------------- #
def e0_juguete(d: Path) -> None:
    def nodo(u: str) -> dict:
        hijos = [x for x, p in ST.PADRE.items() if p == u]
        return {"tipo": "seccion" if u.startswith("S") else "punto", "numero": u[1:] if u.startswith("S") else u,
                "hijos": [nodo(h) for h in hijos]}
    d.mkdir(parents=True)
    (d / "estructura_jug.json").write_text(json.dumps({"to": "jug", "archivo": ST.PDF, "secciones": [
        nodo(u) for u, p in ST.PADRE.items() if p is None]}, ensure_ascii=False), encoding="utf-8")


def preguntas_juguete(p: Path) -> str:
    ps = [{"id": q, "conjunto": "mezcla", "to": "jug", "tipo": t, "subtipo": st, "necesidad": None, "familia": None,
           "cuenta_para_la_mezcla": True, "pregunta": f"consulta sintética {q} del análisis de B2",
           "gold": {"anclas": [{"to": "jug", "punto": a, "detalle": "sintético", "pagina_pdf": 1} for a in anclas],
                    "criterios": [{"id": f"c{j}", "criterio": f"criterio sintético {q}.{j}", "cita": f"cita sintética {j}",
                                   "ancla": anclas[0], "pagina_pdf": 1} for j in (1, 2)]}}
          for q, (t, st, anclas) in PREGUNTAS.items()]
    p.write_text(json.dumps({"version": 1, "unidad": "B2 — selftest del análisis", "preguntas": ps}, ensure_ascii=False,
                            indent=1) + "\n", encoding="utf-8")
    return CN.sha256_file(p)


def escribir_sesion(d: Path, sid: str, conf: str, qid: str, navs: dict) -> None:
    d.mkdir(parents=True)
    _, _, anclas = PREGUNTAS[qid]
    puntos = [f"jug::{a.rstrip('.')}" for a in anclas]
    abre = puntos[:1] if conf == "N7" else puntos
    llamadas = [("ver_punto", {"punto": k}, navs[conf].ver_punto(k)) for k in abre]
    if conf == "N7" and qid == "JUG-6":
        llamadas += [("buscar_nodos", {"consulta": "plazo"}, json.dumps({"resultados": []}))] * (31 - len(llamadas))
    log = [{"evento": "inicio", "servidor": "mcp_kg"}]
    log += [{"evento": "llamada", "n": i, "tool": t, "input": a, "output_str": o} for i, (t, a, o) in enumerate(llamadas, 1)]
    log += [{"evento": "fin", "n_llamadas": len(llamadas)}]
    (d / f"log_r1_{sid}.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in log), encoding="utf-8")
    marca = MARCA[conf][qid]
    corte = marca is None
    if conf == "N7" and qid == "JUG-5":
        citas = [f"{ST.PDF} | Punto 9"]
    elif conf == "N7c_amp":
        citas = [navs[conf].ver_punto(abre[0]).split("\n")[-1][len("Para citar este punto: "):]]
    else:
        citas = [f"{ST.PDF} | Punto {abre[0].split('::')[1]}"]
    (d / f"stream_{sid}.jsonl").write_text(json.dumps({"type": "result", "subtype": "error_max_turns" if corte else "success",
                                                       "is_error": corte}) + "\n", encoding="utf-8")
    meta = {"modelos_R8": {"uso_por_modelo": {MODELO: {"inputTokens": 10000, "outputTokens": 1000, "cacheReadInputTokens": 0,
                                                       "cacheCreationInputTokens": 0}}},
            "servidores_mcp": {"en_init": [{"name": "kg", "status": "connected"}]}, "inventario_tools_R6": {"coincide": True},
            "completitud_R3": {"completa": not corte, "motivos_incompleta": ["cortada por R5"] if corte else []},
            "hb2": {"n_llamadas_log_r1": len(llamadas)}, "brazo": {"N7": "kg_N7", "N7c": "kg_N7c", "N7c_amp": "kg_N7c_amp"}[conf],
            "final_json_R4": None if corte else {"respuesta": f"respuesta sintética {marca}", "citas": citas, "respondible": True}}
    (d / f"meta_{sid}.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


class Casos:
    def __init__(self):
        self.res, self.fallos = {}, []

    def ver(self, caso: str, nombre: str, ok: bool, **extra):
        self.res.setdefault(caso, {})[nombre] = {"ok": bool(ok), **extra}
        if not ok:
            self.fallos.append(f"{caso}:{nombre}")


def regla_sola(K: Casos) -> None:
    base = {"N7": {"fidelidad_30": 0.70, "fidelidad_dato_directo": 0.80, "varios_fraccion": 0.20, "al_tope_fraccion": 0.0,
                   "cita_fundada_fraccion": 0.90}}
    bien = {"fidelidad_30": 0.70, "fidelidad_dato_directo": 0.80, "varios_fraccion": 0.50, "al_tope_fraccion": 0.0,
            "cita_fundada_fraccion": 0.90}
    R = lambda n7c, amp: A7.regla_adopcion(base | {"N7c": bien | n7c, "N7c_amp": bien | amp})["adoptada"]  # noqa: E731
    K.ver("A7", "las dos cumplen: N7c+", R({}, {}) == "N7c+")
    K.ver("A7", "(iv) falla en N7c+: N7c", R({}, {"cita_fundada_fraccion": 0.89}) == "N7c")
    K.ver("A7", "(ii) falla en las dos: N7", R({"fidelidad_30": 0.64}, {"fidelidad_dato_directo": 0.74}) == "N7")
    K.ver("A7", "el borde: 5 puntos menos y el 5 % al tope cumplen",
          R({}, {"fidelidad_30": 0.65, "fidelidad_dato_directo": 0.75, "al_tope_fraccion": 0.05}) == "N7c+")
    K.ver("A7", "apenas más no", R({}, {"fidelidad_30": 0.6499}) == "N7c" and R({}, {"al_tope_fraccion": 0.0501}) == "N7c")
    K.ver("A7", "una fracción igual no sube", R({"varios_fraccion": 0.20}, {"varios_fraccion": 0.20}) == "N7")
    K.ver("A7", "una medida que falta no cumple", R({"fidelidad_dato_directo": None}, {"cita_fundada_fraccion": None}) == "N7")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--python-citas", default=None)
    a = ap.parse_args()
    T = a.trabajo.resolve()
    if T.exists():
        raise SystemExit("ABORTO: --trabajo tiene que ser una carpeta nueva")
    CN.G.PATRON_PAGO = r"ensayoanalisis[0-9]+x\.py"     # ningún pgrep de esta prueba lleva el patrón real
    idx = T / "indice_juguete"
    sha_man = ST.indice_juguete(idx)
    drv = ST.DriverJuguete()
    navs = {"N7": ST.FNC.NavegadorCand(drv, ST.LABEL, idx, sha256_manifiesto=sha_man),
            "N7c": ST.FNR.NavegadorRel(drv, ST.LABEL, idx, sha256_manifiesto=sha_man),
            "N7c_amp": ST.FNRA.NavegadorRelAmp(drv, ST.LABEL, idx, sha256_manifiesto=sha_man)}
    e0_juguete(T / "e0")
    p = T / "preguntas_juguete.json"
    s_p = preguntas_juguete(p)
    ent = T / "entrada_juguete.json"
    if C7.main(["entrada", "--modo-entrada", "seco", "--preguntas", str(p), "--sha-preguntas", s_p, "--config-agentes",
                str(CONFIG_HUMO), "--lanzador", str(AQUI / "lanzar_agente_n7c.py"), "--entrada", str(ent)]):
        raise SystemExit("ABORTO: no se armó la entrada de juguete")
    s_e = CN.sha256_file(ent)
    e = CN.cargar_entrada(ent, s_e)
    salida = T / "salida"
    for x in e["orden"]["sesiones"]:
        escribir_sesion(salida / "agente" / "lote_01" / x["id"], x["id"], x["configuracion"], x["qid"], navs)
    reg = CN.Registro(salida, s_e)
    CN.correr_juez(e, salida, reg, client_factory=factory_juez(salida / "juez" / "cache"))
    python = AN.python_para_citas(a.python_citas)
    lectura = {"modo": "juguete", "indice": str(idx), "tos": [{"id": "jug", "archivo": ST.PDF}],
               "secciones": {"jug": ["1", "2", "3", "9", "A"]}}
    r = A7.analizar(e, salida, T / "trabajo_analisis", python, T / "e0", lectura)
    K = Casos()
    j = r["juez"]
    K.ver("A1", "el juez y su lectura tolerante", j["rechazadas_por_la_estricta"] == 6 and j["leidas_por_la_tolerante"] == 3
          and j["la_tolerante_no_aplica"] == 3 and j["estrictos_iguales_a_los_del_corredor"]
          and j["agregados_tolerantes"] == j["agregados_estrictos"] + 1, **{k: v for k, v in j.items()})
    K.ver("A1", "las filas estrictas son las de analizar_n6.cargar_sesiones", j["filas_estrictas_iguales_a_las_de_analizar_n6"])
    m = r["medidas"]
    fid = {c: (m[c]["fidelidad"]["total"]["cumplidos"], m[c]["fidelidad"]["total"]["criterios"],
               m[c]["fidelidad"]["dato_directo"]["cumplidos"], m[c]["fidelidad"]["dato_directo"]["criterios"]) for c in m}
    K.ver("A2", "la fidelidad con la lectura tolerante", fid == {"N7": (8, 12, 4, 6), "N7c": (8, 10, 4, 6), "N7c_amp": (8, 10, 4, 6)},
          fidelidad=fid)
    est = (m["N7c_amp"]["fidelidad"]["total_lectura_estricta"]["cumplidos"],
           m["N7c_amp"]["fidelidad"]["total_lectura_estricta"]["criterios"],
           m["N7c_amp"]["fidelidad"]["dato_directo_lectura_estricta"]["cumplidos"],
           m["N7c_amp"]["fidelidad"]["dato_directo_lectura_estricta"]["criterios"])
    K.ver("A2", "la estricta de N7c+", est == (6, 8, 2, 4), estricta=est)
    vp = {c: (m[c]["varios_puntos"]["con_todas_las_anclas_consultadas"], m[c]["varios_puntos"]["sesiones"]) for c in m}
    K.ver("A3", "varios puntos con todas las anclas consultadas", vp == {"N7": (0, 3), "N7c": (3, 3), "N7c_amp": (3, 3)},
          varios=vp)
    sub = m["N7c"]["varios_puntos"]["por_subtipo_descriptiva"]
    K.ver("A3", "por subtipo", {k: (v["con_todas_las_anclas_consultadas"], v["sesiones"]) for k, v in sub.items()}
          == {"excepcion_en_hijo": (1, 1), "remision": (2, 2)})
    cf = {c: (m[c]["cita_fundada"]["si"], m[c]["cita_fundada"]["N"]) for c in m}
    K.ver("A4", "cita fundada", cf == {"N7": (5, 6), "N7c": (5, 6), "N7c_amp": (6, 6)}, cita_fundada=cf)
    tope = {c: (m[c]["operativo"]["al_tope"], m[c]["operativo"]["con_30_llamadas_o_mas"], m[c]["operativo"]["cortadas_por_R5"])
            for c in m}
    K.ver("A5", "el tope", tope == {"N7": (1, 1, 0), "N7c": (1, 0, 1), "N7c_amp": (0, 0, 0)}, tope=tope)
    reg_ = r["regla_de_adopcion"]
    K.ver("A6", "la regla sobre el juguete: N7c no cumple (iii) y se adopta N7c+",
          not reg_["partes"]["N7c"]["iii_al_tope_hasta_el_5_por_ciento"] and reg_["partes"]["N7c+"]["cumple_i_a_iv"]
          and reg_["adoptada"] == "N7c+", partes=reg_["partes"])
    regla_sola(K)
    out = {"unidad": "N7c, B2: selftest_analizar_n7c.py", "casos": K.res, "fallos": K.fallos,
           "resumen_del_analisis": {"n_sesiones": r["n_sesiones"], "clases": r["clases"], "para_la_regla": r["para_la_regla"],
                                    "adoptada": reg_["adoptada"]},
           "sha256_modulos": {x: CN.sha256_file(AQUI / x) for x in ("analizar_n7c.py", "lector_anclas_n7c.py", "correr_n7c.py")}}
    a.salida.write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    n_ok = sum(v["ok"] for c in K.res.values() for v in c.values())
    n = sum(len(c) for c in K.res.values())
    print(f"selftest_analizar_n7c: {n_ok} de {n} en verde; fallos: {K.fallos or 'ninguno'}")
    return 0 if not K.fallos else 1


if __name__ == "__main__":
    raise SystemExit(main())
