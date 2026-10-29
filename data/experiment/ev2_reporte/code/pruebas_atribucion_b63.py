"""
pruebas_atribucion_b63.py — La prueba de atribucion_b63.py (etapa AT1 de ATRIB_B63), sin ningún dato real de B6.3. USD 0, sin
API, sin Neo4j y sin el codificador. Todo lo que escribe va a --out; nada de lo que imprime trae texto de B6.3.

Las ramas:
  1. el humo del banco (banco_mcp/paralelo/humo/), con su atribución por atribuir_sesion: cada archivo controlado, el payload
     del adaptador, las anclas que lee la propia traza (y una que no existe), AnclaIndexBanco y la lectura sobre el índice del
     grafo del humo, y las v1 del log;
  2. los sintéticos de las vueltas a y b (pruebas_atribucion_nav.sinteticos);
  3. una población de juguete con las cuatro clases, por `correr` entero: el código sellado del análisis (analizar_b63 y
     exactitud_de_cita_9_4_b63, de --repo-head, con su sha256) sobre un banco de juguete con su manifiesto, la entrada, las
     preguntas, los agregados, la lectura tolerante y una adjudicación con su planilla sellada, y dobles del clon
     (cargar_entrada, casos_de_b63, orden_bloques, veredicto_pregunta);
  4. un ancla de juguete con un rango, que tal cual no resuelve y con la lectura de los rangos resuelve a los nodos de sus
     unidades, y otra sin rango que queda igual;
  5. el sorteo de la semilla, con más de 10, con 10 y con menos;
  6. un control del log que falla y frena (el sha256 de una salida del log y una salida v1 que no es JSON, con el manifiesto al
     día) y un archivo que no da el sha256 del manifiesto: la corrida frena sin escribir --salida, --material ni --clave;
  7. las fichas de juguete, la planilla y su sellador (y planilla_sellada del análisis que lee el sello).

  python3 -I -B pruebas_atribucion_b63.py --out <carpeta> [--repo-head <raíz de un árbol de HEAD con b63/analisis/codigo y la
      enmienda firmada; por defecto, la de este archivo>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import shutil
import sys
from collections import Counter
from pathlib import Path
from types import SimpleNamespace

AQUI = Path(__file__).resolve().parent
REPO_DIR = AQUI.parents[3]
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))

import atribucion_b63 as R  # noqa: E402
import pruebas_atribucion_nav as PN  # noqa: E402  (HEAD: los ayudantes del mundo chico y los sintéticos de las vueltas a y b)

NAV, ABN, AF = R.NAV, R.ABN, R.AF
DOC = PN.DOC


class Registro(PN.Registro):
    pass


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_p(p: Path) -> str:
    return sha(Path(p).read_bytes())


def escribir_json(p: Path, obj) -> Path:
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return p


# --------------------------------------------------------------------------------------------------------------------- #
# 1. El humo del banco                                                                                                  #
# --------------------------------------------------------------------------------------------------------------------- #
def humo(out: Path) -> list:
    Rg = Registro()
    sesiones = sorted(d for d in PN.HUMO_DIR.glob("humo_*/HUMO-*-kg") if d.is_dir())
    resumen = []
    for k, d in enumerate(sesiones, 1):
        sid = d.name
        archivos = {d / f"{n}_{sid}.jsonl": sha_p(d / f"{n}_{sid}.jsonl") for n in ("stream", "sesion", "log_r1")}
        leidos = []

        def leer(p, archivos=archivos, leidos=leidos):
            b = Path(p).read_bytes()
            if archivos.get(Path(p)) != sha(b):
                R.frena("un archivo del humo no da su sha256")
            leidos.append(Path(p).name)
            return b
        ini = json.loads((d / f"log_r1_{sid}.jsonl").read_text(encoding="utf-8").splitlines()[0])
        cfg = ini["config"]
        indice = PN.BANCO_DIR / "mcp_kg" / cfg["indice_puntos"]
        base = NAV.AnclaIndexBanco.desde_indice(indice, cfg["sha256_manifiesto_indice"])
        lect = NAV.cargar_lectura(indice, cfg["sha256_manifiesto_indice"])
        ai = R.AnclasConRangos(base, {})
        p0 = ABN.adaptar(d / f"stream_{sid}.jsonl", d / f"log_r1_{sid}.jsonl")
        claves = []
        for sf in p0["steps_full"]:
            if sf["tool"] in NAV.TOOLS_NAV:
                lec = NAV.leer_paso(sf["tool"], sf["output"], lect)
                claves += lec["claves"] + lec["textos"]
        anclas = list(dict.fromkeys(claves))[:6] + ["ext::999.999"]
        c = {"sesion": sid, "id_opaco": f"HUMO-{k}"}
        p, at = R.atribuir_sesion(c, d, leer, anclas, ai, lect, "parcial")
        reg = R.registro(c, "parcial", "dato_directo", p, at)
        sin_anclas = not any(a in json.dumps(reg, ensure_ascii=False) for a in anclas)
        Rg.caso(f"humo {sid}: atribuir_sesion con los tres archivos controlados, las v1 del log y el índice del humo",
                NAV.corrida_valida([at]) and sorted(leidos) == sorted([f"stream_{sid}.jsonl", f"sesion_{sid}.jsonl",
                                                                       f"log_r1_{sid}.jsonl"]) and at["clase"] is not None,
                {"clase": at["clase"], "steps": at["n_steps"]})
        Rg.caso(f"humo {sid}: el registro de la salida no trae ninguna ancla", sin_anclas)
        resumen.append({"sesion": sid, "clase": at["clase"], "n_steps": at["n_steps"], "n_anclas": len(anclas),
                        "por_herramienta": reg["por_herramienta"], "replay_ok": at["replay_ok"]})
    escribir_json(out / "humo.json", {"sesiones": resumen, "casos": Rg.casos})
    return Rg.casos


# --------------------------------------------------------------------------------------------------------------------- #
# 3. La población de juguete                                                                                            #
# --------------------------------------------------------------------------------------------------------------------- #
BRAZOS_J = ["fragmentos_hibrida", "kg"]
# qid: (tipo, anclas, clasificación del kg, veredicto del kg o None, llamadas de la sesión del kg)
PREGUNTAS_J = {
    "JUG-Q1": ("dato_directo", ["ext::6.99"], "completa", "incorrecto", [("ver_punto", {"punto": "ext::6.11"})]),
    "JUG-Q2": ("dato_directo", ["ext::7.2"], "completa", "requiere_adjudicacion",
               [("buscar_nodos", {"consulta": "gamma tope", "limite": 10})]),
    "JUG-Q3": ("varios_puntos", ["ext::6.11"], "completa", "parcial", [("buscar_puntos", {"consulta": "alfa conformidad"})]),
    "JUG-Q4": ("varios_puntos", ["ext::6.11..6.12", "ext::7.1"], "completa", "parcial",
               [("ver_nodo", {"id": "Operacion_vecino_B"})]),
    "JUG-Q5": ("dato_directo", ["ext::6.11"], "completa", "incorrecto", [("ver_punto", {"punto": "ext::6.11"})]),
    "JUG-Q6": ("dato_directo", ["ext::6.11"], "completa", "correcto", [("ver_nodo", {"id": "Obligacion_ancla_A"})]),
    "JUG-Q7": ("dato_directo", ["ext::7.1"], "cortada", None, None),
    "JUG-Q8": ("dato_directo", ["ext::6.11::intro"], "incompleta_otra", None, None),
    "JUG-Q9": ("dato_directo", ["ext::7.2"], "completa", None, [("ver_nodo", {"id": "Excepcion_delta_D"})]),
}
MODALES_J = {"incorrecto": ["no_cumplido", "no_cumplido"], "parcial": ["cumplido", "no_cumplido"],
             "correcto": ["cumplido", "cumplido"], "requiere_adjudicacion": ["cumplido", "dudoso"]}


def opaco(q: str, brazo: str) -> str:
    return f"OP-{q[-2:]}-{'kg' if brazo == 'kg' else 'fh'}"


def sesion_id(q: str, brazo: str) -> str:
    return f"{q}-r1-{brazo}"


def veredicto_pregunta(modales: list) -> str:
    if any(m in ("dudoso", "sin_consenso") for m in modales):
        return "requiere_adjudicacion"
    if all(m == "cumplido" for m in modales):
        return "correcto"
    if all(m == "no_cumplido" for m in modales):
        return "incorrecto"
    return "parcial"


def dobles_del_clon(raiz: Path):
    """AP, JB y K de juguete, con la interfaz que usan las funciones selladas del análisis."""
    K = SimpleNamespace(orden_bloques=lambda ids, k, brazos: [{"bloque": f"{q}|r{r}", "qid": q, "r": r}
                                                              for q in ids for r in range(1, k + 1)])

    def cargar_entrada(ruta, K_):
        d = json.loads(Path(ruta).read_text(encoding="utf-8"))
        return {"preguntas": {"ids_en_orden": d["preguntas"]["ids_en_orden"]}, "k": d["k"], "brazos": d["brazos"],
                "_rutas": {"preguntas": str((Path(ruta).parent / d["preguntas"]["ruta"]).resolve())}}

    def casos_de_b63(b63, e, K_, JB_):
        st = json.loads((Path(b63) / "resultados" / "real" / "estado_b63.json").read_text(encoding="utf-8"))
        out = []
        for blq in st["bloques"].values():
            for brazo, f in blq["final"].items():
                if f.get("clasificacion") == "completa":
                    q, r = blq["qid"], blq["r"]
                    out.append({"qid": q, "r": r, "brazo": brazo, "id_opaco": opaco(q, brazo)})
        return out
    AP = SimpleNamespace(cargar_entrada=cargar_entrada, casos_de_b63=casos_de_b63)
    JB = SimpleNamespace(K=K, M=SimpleNamespace(veredicto_pregunta=veredicto_pregunta))
    return lambda clon, esperado: (AP, JB)


def mundo_de_juguete(raiz: Path, variante: str | None = None) -> tuple[dict, dict, object]:
    """(rutas, esperado, importar) de una población de juguete completa, en `raiz`."""
    raiz.mkdir(parents=True)
    repo, fuera = raiz / "repo", raiz / "fuera"
    nav = PN.navegador_chico()
    _, index, _ = AF._mini_grafo()
    puntos, nodos, _ = PN.mundo_puntos()
    # el grafo en la forma del banco, su E0 (con un rango posible en la sección 6), su índice por punto y el armado
    kg = {"nodes": [{"id": i, "type": nd["type"], "label": nd["label"],
                     "provenances": [PN._pv(*k.split("::", 1)) for k in nd["puntos"]]} for i, nd in nodos.items()], "edges": []}
    estructura = {"to": "ext", "archivo": DOC, "secciones": [
        {"tipo": "seccion", "numero": "6", "hijos": [{"tipo": "punto", "numero": "6.11", "hijos": [{"tipo": "punto", "numero": "6.11.1"}]},
                                                    {"tipo": "punto", "numero": "6.12"}]},
        {"tipo": "seccion", "numero": "7", "hijos": [{"tipo": "punto", "numero": "7.1"}, {"tipo": "punto", "numero": "7.2"}]}]}
    p_kg = escribir_json(repo / "grafo" / "kg.json", kg)
    p_est = escribir_json(repo / "e0" / "estructura_ext.json", estructura)
    p_pun = escribir_json(repo / "indice" / "puntos.json", puntos)
    p_nod = escribir_json(repo / "indice" / "nodos.json", nodos)
    man_idx = {"grafo": "Juguete", "kg_path": "grafo/kg.json", "kg_sha256": sha_p(p_kg), "e0_dir": "e0",
               "insumos_e0": {"estructura_ext.json": sha_p(p_est)}, "archivo_a_to": {DOC: "ext"},
               "archivos": {"puntos.json": sha_p(p_pun), "nodos.json": sha_p(p_nod)}}
    p_man_idx = escribir_json(repo / "indice" / "manifiesto.json", man_idx)
    p_armado = escribir_json(repo / "armado_e0.json", {"e0": [{"to": "ext", "archivo": "estructura_ext.json", "sha256": sha_p(p_est)}]})
    # las preguntas y la entrada
    preguntas = {"preguntas": [{"id": q, "tipo": t, "to": "ext", "pregunta": f"Pregunta de juguete {q[-1]}",
                                "criterios": [{"criterio": f"criterio {k} de juguete", "cita_textual": f"cita {k} de juguete",
                                               "unidad": "ext::6.11"} for k in (1, 2)],
                                "anclas": [{"unidad": a, "rol": "ancla" if i == 0 else "otro punto"} for i, a in enumerate(an)]}
                               for q, (t, an, *_r) in PREGUNTAS_J.items()]}
    p_preg = escribir_json(fuera / "preguntas_juguete.json", preguntas)
    entrada = {"preguntas": {"ruta": "../fuera/preguntas_juguete.json", "sha256": sha_p(p_preg), "ids_en_orden": list(PREGUNTAS_J)},
               "k": 1, "brazos": BRAZOS_J}
    p_ent = escribir_json(repo / "entrada_juguete.json", entrada)
    # el banco: el estado, las metas y las sesiones del kg
    b63 = fuera / "banco_b63"
    real = b63 / "resultados" / "real"
    bloques = {}
    agregados = []
    for q, (t, an, cl, ver, llamadas) in PREGUNTAS_J.items():
        final = {}
        for brazo in BRAZOS_J:
            sid = sesion_id(q, brazo)
            clas = cl if brazo == "kg" else "completa"
            final[brazo] = {"clasificacion": clas, "salida": f"pasada1/{sid}", "id": sid}
            d = real / "pasada1" / sid
            d.mkdir(parents=True, exist_ok=True)
            if clas == "completa":
                escribir_json(d / f"meta_{sid}.json", {"brazo": brazo, "de_juguete": True})
                v = ver if brazo == "kg" else "correcto"
                if v is not None:
                    agregados.append({"id_opaco": opaco(q, brazo), "veredicto_pregunta": v, "modales": MODALES_J[v]})
            if brazo == "kg" and clas == "incompleta_otra":
                escribir_json(d / f"meta_sin_texto_{sid}.json",
                              {"completitud_R3": {"motivos_incompleta": ["log 1 llamadas vs sesión 2 tool_use a herramientas"]},
                               "mapa_R7": [{"n": 1, "tool": "mcp__kg__ver_punto", "call_id_log": "mcp_kg-1-1"},
                                           {"n": 2, "tool": "mcp__kg", "call_id_log": None}]})
            if brazo == "kg" and clas == "completa":
                usos, log = [], []
                for tool, inp in llamadas:
                    s = PN.salida_de(nav, index, tool, inp)
                    if variante == "salida_v1_no_json" and q == "JUG-Q6":
                        s = "esto no es JSON"
                    usos.append((ABN.PREFIJO_KG + tool, inp, s, False))
                    log.append((tool, inp, s))
                PN._sesion(d, sid, usos, log)
                if variante == "sha_del_log" and q == "JUG-Q3":
                    lineas = (d / f"log_r1_{sid}.jsonl").read_text(encoding="utf-8").splitlines()
                    x = json.loads(lineas[1])
                    x["output_sha256"] = "0" * 64
                    lineas[1] = json.dumps(x, ensure_ascii=False)
                    (d / f"log_r1_{sid}.jsonl").write_text("\n".join(lineas) + "\n", encoding="utf-8")
                (d / f"sesion_{sid}.jsonl").write_bytes((d / f"stream_{sid}.jsonl").read_bytes())
        bloques[f"{q}|r1"] = {"qid": q, "r": 1, "final": final, "intentos_por_brazo": {b: 1 for b in BRAZOS_J}}
    escribir_json(real / "estado_b63.json", {"bloques": bloques})
    archivos = [{"ruta": str(p.relative_to(fuera)), "sha256": sha_p(p)} for p in sorted(b63.rglob("*")) if p.is_file()]
    if variante == "manifiesto_distinto":
        archivos = [dict(a, sha256="0" * 64) if a["ruta"].endswith("stream_JUG-Q5-r1-kg.jsonl") else a for a in archivos]
    p_man = escribir_json(repo / "manifiesto_banco_juguete.json", {"archivos": archivos})
    # los agregados, la lectura tolerante y la adjudicación
    p_agg = escribir_json(fuera / "agregados.json", {"agregados": agregados})
    tol = [a for a in agregados if a["id_opaco"] == opaco("JUG-Q3", "kg")]
    p_tol = escribir_json(fuera / "agregados_tolerante.json", {"agregados": tol})
    p_vtol = fuera / "veredictos_tolerante.jsonl"
    p_vtol.write_text(json.dumps({"id_opaco": tol[0]["id_opaco"]}) + "\n", encoding="utf-8")
    p_est_pl = escribir_json(repo / "estructura_planilla.json", {"columnas": ["ficha", "criterio", "marca"], "renglones": [["A01", "2"]]})
    p_pl = fuera / "planilla_adjudicacion.csv"
    p_pl.write_text("ficha,criterio,marca\nA01,2,no cumplido\n", encoding="utf-8")
    p_sello = repo / "sello_adjudicacion.txt"
    p_sello.write_text(f"# sello de juguete\n{sha_p(p_pl)}  {len(p_pl.read_bytes())}  2026-10-29T00:00:00  {p_pl.name}\n",
                       encoding="utf-8")
    p_clave = escribir_json(fuera / "clave_adjudicacion.json", {"fichas": [
        {"ficha": "A01", "id_opaco": opaco("JUG-Q2", "kg"), "brazo": "kg", "pregunta": "JUG-Q2", "repeticion": 1,
         "criterios_que_se_adjudican": [2], "modal_del_juez_de_los_demas": {"1": "cumplido"}}]})
    rutas = {"clon": raiz / "clon_de_juguete", "entrada": p_ent, "manifiesto_fuera": p_man, "banco_b63": b63,
             "agregados": p_agg, "agregados_tolerante": p_tol, "veredictos_tolerante": p_vtol, "planilla": p_pl,
             "sello_planilla": p_sello, "estructura_planilla": p_est_pl, "clave_adjudicacion": p_clave, "e0": repo / "e0",
             "armado_e0": p_armado, "indice": repo / "indice"}
    esperado = {"entrada": sha_p(p_ent), "manifiesto_fuera": sha_p(p_man), "agregados": sha_p(p_agg),
                "agregados_tolerante": sha_p(p_tol), "veredictos_tolerante": sha_p(p_vtol), "estructura_planilla": sha_p(p_est_pl),
                "clave_adjudicacion": sha_p(p_clave), "armado_e0": sha_p(p_armado), "kg": sha_p(p_kg),
                "manifiesto_indice": sha_p(p_man_idx)}
    return rutas, esperado, dobles_del_clon(raiz)


def correr_juguete(raiz: Path, repo_head: Path, variante: str | None = None) -> tuple[dict | None, str | None, dict]:
    rutas, esperado, importar = mundo_de_juguete(raiz / "mundo", variante)
    sal, mat, cla = raiz / "salida", raiz / "material", raiz / "clave" / "clave_atribucion_b63.json"
    try:
        out = R.correr(rutas, sal, mat, cla, esperado=esperado, importar=importar,
                       codigo=repo_head / "data/experiment/banco_mcp/b63/analisis/codigo",
                       enmienda=repo_head / "data/experiment/ev2_reporte/enmienda1_regla_atribucion_navegacion.md",
                       raiz_indice=raiz / "mundo" / "repo")
        return out, None, {"salida": sal, "material": mat, "clave": cla, "rutas": rutas}
    except Exception as ex:  # noqa: BLE001
        if type(ex).__name__ != "Freno":
            raise
        return None, str(ex), {"salida": sal, "material": mat, "clave": cla, "rutas": rutas}


def poblacion_de_juguete(out: Path, repo_head: Path) -> list:
    Rg = Registro()
    o, freno, donde = correr_juguete(out / "poblacion", repo_head)
    Rg.caso("población de juguete: correr termina sin frenar", o is not None, freno)
    if o is None:
        return Rg.casos
    cl = {x["id_opaco"]: x["clase"] for x in o["por_sesion"]}
    esperadas = {"OP-Q1-kg": "ausencia_kg", "OP-Q2-kg": "alcanzabilidad", "OP-Q3-kg": "vista_no_consultada",
                 "OP-Q4-kg": "generacion", "OP-Q5-kg": "generacion", "OP-Q6-kg": None}
    Rg.caso("población de juguete: las cuatro clases, una correcta sin clase, por sesión", cl == esperadas, cl)
    Rg.caso("población de juguete: solo el brazo kg, con su veredicto final (la adjudicación de Q2 da parcial)",
            o["poblacion"]["corridas"] == 9 and o["poblacion"]["con_veredicto"] == 6 and o["poblacion"]["atribuibles"] == 5
            and {x["id_opaco"]: x["veredicto"] for x in o["por_sesion"]}["OP-Q2-kg"] == "parcial",
            o["poblacion"])
    Rg.caso("población de juguete: las que no tienen veredicto, por estado y la incompleta_otra por motivo",
            o["poblacion"]["sin_veredicto"] == {"por_estado": {"cortada": 1, "incompleta_otra": 1, "sin_veredicto": 1},
                                                "incompleta_otra": {"total": 1, "por_motivo": {
                                                    "log n llamadas vs sesión n tool_use a herramientas": 1},
                                                                    "con_la_llamada_que_falta": 1}},
            o["poblacion"]["sin_veredicto"])
    Rg.caso("población de juguete: las cuentas por clase y por tipo",
            o["cuentas"]["por_clase"] == {"ausencia_kg": 1, "alcanzabilidad": 1, "vista_no_consultada": 1, "generacion": 2,
                                          "correcto": 1}
            and o["cuentas"]["por_tipo_y_clase"]["varios_puntos"] == {"ausencia_kg": 0, "alcanzabilidad": 0,
                                                                      "vista_no_consultada": 1, "generacion": 1, "correcto": 0},
            o["cuentas"])
    Rg.caso("población de juguete: las anclas por forma, tal cual y con la lectura de los rangos",
            o["anclas_por_forma"] == {"sin_rango": {"n": 8, "resuelven_tal_cual": 7, "resuelven_con_los_rangos": 7},
                                      "con_un_rango": {"n": 1, "resuelven_tal_cual": 0, "resuelven_con_los_rangos": 1},
                                      "las_demas": {"n": 1, "resuelven_tal_cual": 1, "resuelven_con_los_rangos": 1}},
            o["anclas_por_forma"])
    texto = (donde["salida"] / "atribucion_B63.json").read_text(encoding="utf-8")
    Rg.caso("población de juguete: la salida no trae ninguna ancla, ningún id de pregunta ni ninguna sesión",
            "ext::" not in texto and "JUG-Q" not in texto and "Pregunta de juguete" not in texto)
    Rg.caso("población de juguete: la última clase, con 2 casos, entran las dos (F01 y F02, en el orden de sus ids)",
            o["ultima_clase"] == {"clase": "generacion", "n": 2, "semilla": R.SEMILLA, "regla": "todas", "n_fichas": 2}
            and [x["id_opaco"] for x in json.loads(donde["clave"].read_text(encoding="utf-8"))["casos"]] == ["OP-Q4-kg", "OP-Q5-kg"])
    Rg.caso("población de juguete: la corrida es válida y lo controlado del banco, contado",
            o["corrida_valida"] and o["archivos_de_banco_b63_controlados"] > 0)
    return Rg.casos


# --------------------------------------------------------------------------------------------------------------------- #
# 4. El ancla con un rango                                                                                              #
# --------------------------------------------------------------------------------------------------------------------- #
def ancla_con_rango(out: Path, repo_head: Path) -> list:
    Rg = Registro()
    rutas, esperado, _ = mundo_de_juguete(out / "rango" / "mundo")
    A, X = R.cargar_codigo_analisis(repo_head / "data/experiment/banco_mcp/b63/analisis/codigo")
    armado = json.loads(A.controlado(rutas["armado_e0"], esperado["armado_e0"], "el armado"))
    P = {"R1": {"anclas": [{"unidad": "ext::6.11..6.12"}, {"unidad": "ext::7.1"}]}}
    us = X.unidades_de_las_anclas(["R1"], P, rutas["e0"], armado)["R1"]
    base = NAV.AnclaIndexBanco.desde_indice(rutas["indice"], esperado["manifiesto_indice"], out / "rango" / "mundo" / "repo")
    ai = R.AnclasConRangos(base, {"ext::6.11..6.12": us[0], "ext::7.1": us[1]})
    Rg.caso("rango: las unidades del ancla, por expandir sobre arbol_e0 (unidades_de_las_anclas)",
            us == [["ext::6.11", "ext::6.12"], ["ext::7.1"]], us)
    Rg.caso("rango: tal cual no resuelve; con la lectura de los rangos, los nodos de sus dos unidades",
            base.resolver("ext", "6.11..6.12") == [] and ai.resolver("ext", "6.11..6.12") == ["Obligacion_ancla_A", "Operacion_vecino_B"],
            ai.resolver("ext", "6.11..6.12"))
    Rg.caso("rango: el ancla sin rango queda igual", base.resolver("ext", "7.1") == ai.resolver("ext", "7.1") == ["Restriccion_gamma_C"])
    Rg.caso("rango: las formas", [R.forma_de(a) for a in ("ext::6.11", "ext::6.11..6.12", "ext::6.11::intro", "ri::SD::rep3")]
            == ["sin_rango", "con_un_rango", "las_demas", "las_demas"])
    return Rg.casos


# --------------------------------------------------------------------------------------------------------------------- #
# 5. El sorteo                                                                                                          #
# --------------------------------------------------------------------------------------------------------------------- #
def sorteo() -> list:
    Rg = Registro()
    muchos = [f"OP-{i:03d}" for i in range(25, 0, -1)]
    s1, s2 = R.sortear(muchos), R.sortear(list(reversed(muchos)))
    Rg.caso("sorteo con 25: 10, con random.Random(«B63:atribucion:ultima_clase:v1»).sample sobre los ids ordenados",
            s1 == random.Random("B63:atribucion:ultima_clase:v1").sample(sorted(muchos), 10) and len(set(s1)) == 10)
    Rg.caso("sorteo con 25: el mismo, sea cual sea el orden en que llegan los ids", s1 == s2)
    Rg.caso("sorteo con 10: entran todas, ordenadas", R.sortear(muchos[:10]) == sorted(muchos[:10]))
    Rg.caso("sorteo con 3: entran todas, ordenadas", R.sortear(muchos[:3]) == sorted(muchos[:3]))
    return Rg.casos


# --------------------------------------------------------------------------------------------------------------------- #
# 6. Los frenos                                                                                                         #
# --------------------------------------------------------------------------------------------------------------------- #
def frenos(out: Path, repo_head: Path) -> list:
    Rg = Registro()
    for variante, motivo in (("sha_del_log", "no reconcilia con su log R1"), ("salida_v1_no_json", "no reconcilia con su log R1"),
                             ("manifiesto_distinto", "no da el sha256 de su manifiesto")):
        o, freno, donde = correr_juguete(out / f"freno_{variante}", repo_head, variante)
        nada = not any(donde[k].exists() for k in ("salida", "material", "clave"))
        Rg.caso(f"freno ({variante}): la corrida frena y no escribe --salida, --material ni --clave",
                o is None and freno is not None and motivo in freno and nada, freno)
    return Rg.casos


# --------------------------------------------------------------------------------------------------------------------- #
# 7. Las fichas de juguete y el sellador                                                                                #
# --------------------------------------------------------------------------------------------------------------------- #
def fichas_y_sellador(out: Path, repo_head: Path) -> list:
    Rg = Registro()
    mat = out / "poblacion" / "material"
    A, _ = R.cargar_codigo_analisis(repo_head / "data/experiment/banco_mcp/b63/analisis/codigo")
    f1 = (mat / "F01.md").read_text(encoding="utf-8")
    Rg.caso("fichas: F01 y F02, con la pregunta, los criterios con su marca, la respuesta, el ancla y los pasos",
            sorted(p.name for p in mat.glob("F*.md")) == ["F01.md", "F02.md"]
            and all(s in f1 for s in ("## La pregunta", "Pregunta de juguete 4", "criterio 1 de juguete — **cumplido**",
                                      "## La respuesta", "Ancla 1 (ancla): ext::6.11..6.12; sus unidades: ext::6.11, ext::6.12",
                                      "| 1 | ver_nodo |", "consultó un nodo del ancla 1 (por ver_nodo)")))
    Rg.caso("fichas: ninguna trae el id opaco ni la sesión", not any(x in f1 for x in ("OP-Q4", "JUG-Q4-r1")))
    est = json.loads((mat / "estructura_planilla_atribucion_b63.json").read_text(encoding="utf-8"))
    Rg.caso("planilla: vacía, con sus columnas y sus renglones",
            (mat / "planilla_atribucion_b63.csv").read_text(encoding="utf-8") == "ficha,la_clase_se_sostiene,comentario\nF01,,\nF02,,\n"
            and est["renglones"] == [["F01"], ["F02"]] and est["valores_admitidos"] == list(R.VALORES_PLANILLA))
    tr = out / "sellos"
    tr.mkdir(parents=True)
    pl = tr / "planilla_atribucion_b63.csv"
    pl.write_text("ficha,la_clase_se_sostiene,comentario\nF01,sí,se sostiene: consultó el rango\nF02,no decidible,\n", encoding="utf-8")
    h, hora = R.sellar(pl, mat / "estructura_planilla_atribucion_b63.json", tr / "sello.txt", hora="2026-10-29T12:00:00")
    lee = A.planilla_sellada(pl, tr / "sello.txt")
    Rg.caso("sellador: sella con el renglón «sha256  bytes  hora  nombre», y planilla_sellada del análisis la lee",
            lee == pl.read_bytes() and (tr / "sello.txt").read_text(encoding="utf-8").splitlines()[-1]
            == f"{h}  {len(pl.read_bytes())}  2026-10-29T12:00:00  planilla_atribucion_b63.csv")
    for nombre, contenido in (("otra vez", None), ("un valor que no está", "ficha,la_clase_se_sostiene,comentario\nF01,quizás,\nF02,no,\n"),
                              ("un renglón de más", "ficha,la_clase_se_sostiene,comentario\nF01,sí,\nF02,no,\nF03,no,\n")):
        p = pl if contenido is None else tr / f"planilla_{len(nombre)}.csv"
        if contenido is not None:
            p.write_text(contenido, encoding="utf-8")
        try:
            R.sellar(p, mat / "estructura_planilla_atribucion_b63.json", tr / "sello.txt", hora="2026-10-29T12:00:00")
            Rg.caso(f"sellador: {nombre} -> frena", False)
        except R.Freno:
            Rg.caso(f"sellador: {nombre} -> frena", True)
    return Rg.casos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--repo-head", type=Path, default=REPO_DIR)
    a = ap.parse_args()
    if a.out.exists():
        print("FRENO: --out ya existe")
        return 10
    a.out.mkdir(parents=True)
    ramas = {}
    ramas["1_humo"] = humo(a.out / "humo")
    sint = PN.sinteticos(a.out / "sinteticos_nav")
    ramas["2_sinteticos_vueltas_a_y_b"] = [{"caso": f"sintéticos de las vueltas a y b: {sint['n_ok']} de {sint['n_casos']}",
                                            "ok": sint["n_ok"] == sint["n_casos"], "detalle": None}]
    ramas["3_poblacion_de_juguete"] = poblacion_de_juguete(a.out, a.repo_head)
    ramas["4_ancla_con_rango"] = ancla_con_rango(a.out, a.repo_head)
    ramas["5_sorteo"] = sorteo()
    ramas["6_frenos"] = frenos(a.out, a.repo_head)
    ramas["7_fichas_y_sellador"] = fichas_y_sellador(a.out, a.repo_head)
    resumen = {r: {"n": len(c), "ok": sum(1 for x in c if x["ok"])} for r, c in ramas.items()}
    escribir_json(a.out / "pruebas_atribucion_b63.json", {"ramas": ramas, "resumen": resumen,
                                                         "codigo": {"atribucion_b63.py": sha_p(Path(R.__file__)),
                                                                    "pruebas_atribucion_b63.py": sha_p(Path(__file__))}})
    for r, x in resumen.items():
        print(f"== rama {r}: {x['ok']} de {x['n']}")
    total, ok = sum(x["n"] for x in resumen.values()), sum(x["ok"] for x in resumen.values())
    print(f"== total: {ok} de {total} PASS")
    return 0 if ok == total else 1


if __name__ == "__main__":
    raise SystemExit(main())
