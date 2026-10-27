#!/usr/bin/env python3
"""analizar_n6.py — El análisis de N6 de U-NAV-DISENO (protocolo de N4, sellado en f69e95ea, §4, §5 y §6), escrito y probado
sobre datos de juguete antes de correr N6 (selftest_analizar_n6.py). USD 0: lee la entrada sellada, las metas, los streams y los
logs R1 de las sesiones, los agregados del juez y la lista de la familia 5; no llama a ningún modelo.

Las medidas (N4, §4), por configuración, sobre las 30 y sobre las preguntas de la necesidad de cada familia (Qk):
  · fidelidad por criterio: criterios con veredicto modal «cumplido» (las 3 repeticiones del juez, mapping.veredicto_modal)
    sobre los criterios. Principal: lo que no tiene veredicto (una sesión cortada por R5, con la salida mal formada, de
    infraestructura en sus dos intentos, de forma desconocida, o una respuesta sin sus 3 repeticiones del juez) sale de la
    métrica y se lista. Sensibilidad: eso cuenta como no cumplido (la regla de A2.2: pre-registro, §3, R5 (1); registro, §50,
    punto 6). B y F1_bm25 corren 3 veces: su fidelidad junta los criterios de sus 3 corridas, y por corrida va aparte;
  · precisión de citas, con el instrumento de la decisión 4 (scripts/ucita2_indicadores_banco.py, sin editarlo, corrido por
    su línea de comandos con un Python 3.12 o más nuevo: scripts/ucita2_indicadores.py de HEAD no compila con el 3.10 del
    .venv del repo):
    cita fundada, cita existente y, como principal, alguna cita a alguna de las anclas; cada ancla con su cita, como columna
    informativa, sin entrar en ninguna comparación. Sobre el intento final de cada sesión con meta;
  · costo: R9 (tokens × agentes/precios_sellados.json, con LA.costo_desde_tokens; nunca total_cost_usd), medio por pregunta en
    el intento final, y el total con los intentos que se re-corrieron;
  · llamadas a herramientas (las del log R1) y respuestas al tope: las de 30 llamadas o más y las cortadas por R5;
  · las cuatro clases de N1 sobre los criterios no cumplidos, con la regla sellada (n1/regla_n1_cuatro_clases_UNAV.md,
    db2cc290…): este análisis lista los criterios no cumplidos por configuración, que son la entrada de la clasificación, y
    cuenta las clases si recibe la clasificación hecha con esa regla (--clases-n1, con el sha256 de la regla); si no, las deja
    PENDIENTES. La regla está en una carpeta que el despacho de N6 veda: no se implementa acá;
  · lo verificado y lo no verificado, aparte: las mismas medidas para las sesiones que vieron una marca (la salida de una
    herramienta, en su log R1, trae «no verificada», «cola humana» o «sujeto derivado») y para las demás.
La regla de decisión (N4, §5):
  · V(Q): la mayor menos la menor fidelidad por criterio de B sobre Q en sus 3 corridas;
  · Δ(Q) de una configuración contra otra sobre las mismas preguntas, y cuántas suben, bajan o quedan igual (por pregunta, con
    las preguntas que tienen fidelidad en las dos; en B, la de sus 3 corridas juntas);
  · por familia: «T−Fk» es elegible solo si fidelidad(T, Qk) − fidelidad(T−Fk, Qk) ≤ V(Qk);
  · elección: entre B, T y las «T−Fk» elegibles, la de mayor fidelidad sobre las 30; si otras quedan dentro de V(30) de ella,
    gana la que llega menos veces al tope de llamadas y, después, la más barata (R9 medio por pregunta);
  · requisito: la elegida tiene que pasar el caso de la jerarquía: lo pasa la que tiene ver_punto (el camino de 2 llamadas,
    probado sobre T, n6/caso_jerarquia_n6.py); si no, la configuración vuelve a la autora;
  · F1 (§6): la híbrida entra al brazo de fragmentos si fidelidad(híbrida, 30) ≥ fidelidad(BM25, 30) − Vfrag(30), con Vfrag la
    variación entre las 3 corridas de BM25.
El desvío de N4 de la decisión 9 de la autora (27/10/2026): los ejemplos de la familia 6, que llevan T y T−F1 a T−F5, comparten
texto con N3-M18, N3-M21, N3-M05 y N3-C4 (FUERA_D9). Toda comparación entre una configuración con esos ejemplos y una sin ellos (B
y T−F6) va sin esas cuatro, sobre las 26, con V sobre las mismas 26, y la versión con las 30 va al lado («con_las_30»), como
sensibilidad: el Δ de B y de T−F6 contra T, la elegibilidad de la familia 6 y, si entre las candidatas hay una con los ejemplos y
otra sin ellos, la elección (sobre las 26, con V(26)). Las demás comparaciones (T contra T−F1 a T−F5, y F1), con las 30.
Qk (N4, §3): la familia 1, la de cupo 1; la 2, las de cupo 4 a 7; la 3, la de cupo 2 y las de la mezcla de subtipo remisión;
la 4, la de cupo 3 y las de la mezcla de subtipo excepción en un hijo; la 5, la lista sellada de la familia 5; la 6, las de la
mezcla de varios puntos. «La de cupo k» es la de necesidad k de N3.
No imprime ningún veredicto ni resultado: escribe el JSON (--salida) y dice dónde. Sin texto de preguntas, criterios ni respuestas.
Uso: .venv/bin/python -B data/experiment/banco_mcp/n6/analizar_n6.py --entrada <json> --sha256-entrada <hex> \\
       --salida-n6 <banco_n6> --salida <json> [--caso-jerarquia <json>] [--clases-n1 <json> --sha256-regla-n1 <hex>]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
import correr_n6 as CN                          # noqa: E402  (la entrada, la clasificación, los ids opacos)

REPO_DIR = CN.REPO_DIR
INSTRUMENTO_CITAS = REPO_DIR / "scripts" / "ucita2_indicadores_banco.py"
# Los indicadores del instrumento (scripts/ucita2_indicadores_banco.py, INDICADORES) y su «sí» (ucita2_indicadores.SI).
INDICADORES = ("ind1_cita_fundada", "ind2_cita_existente", "ind3_cita_al_ancla", "info_cada_ancla_con_cita")
SI = "si"

LA = CN.LA
E0_ACUMULADO = REPO_DIR / "data" / "experiment" / "tanda1" / "t3" / "acumulado" / "e0_acumulado_r2b"
MARCAS = ("no verificada", "cola humana", "sujeto derivado")
TOPE_LLAMADAS = 30
PREFIJO_REGLA_N1 = "db2cc290"
GRAFO = ("B", "T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5", "T-F6")
CANDIDATAS = ("B", "T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5", "T-F6")
REPETIDAS = ("B", "F1_bm25")
# La decisión 9 (desvío de N4): los ejemplos de la familia 6 (en el bloque de T y de cada «T−Fk» con k de 1 a 5) comparten texto
# con estas cuatro preguntas; toda comparación entre una configuración con esos ejemplos y una sin ellos va sin ellas.
CON_EJEMPLOS = ("T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5")
SIN_EJEMPLOS = ("B", "T-F6")
FUERA_D9 = ("N3-C4", "N3-M05", "N3-M18", "N3-M21")


def sha256_file(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# --------------------------------------------------------------------------- #
# Las sesiones, con su veredicto                                               #
# --------------------------------------------------------------------------- #
def marcas_vistas(log: Path) -> bool:
    for linea in log.read_text(encoding="utf-8").splitlines() if log.is_file() else []:
        try:
            d = json.loads(linea)
        except json.JSONDecodeError:
            continue
        if d.get("evento") == "llamada" and any(m in (d.get("output_str") or "") for m in MARCAS):
            return True
    return False


def cargar_sesiones(e: dict, salida: Path) -> list[dict]:
    """Una fila por sesión de la entrada, con su intento final, su clase, sus modales (si tiene sus 3 repeticiones del juez),
    sus llamadas, su R9 y si vio una marca. Sin texto."""
    st = CN.estado(e, salida)
    agg_p = salida / "juez" / "agregados_n6_ciego.json"
    agg = {a["id_opaco"]: a for a in (json.loads(agg_p.read_text(encoding="utf-8"))["agregados"] if agg_p.is_file() else [])}
    precios = LA.cargar(LA.PRECIOS)
    filas = []
    for k, v in st["por_sesion"].items():
        s, f = v["sesion"], v["final"]
        n_crit = len(e["_preguntas"][s["qid"]]["criterios"])
        fila = {"id": k, "qid": s["qid"], "configuracion": s["configuracion"], "rep": s["rep"], "n_criterios": n_crit,
                "clase": f["clase"] if f else "sin correr", "intento": f["id"] if f else None, "n_intentos": len(v["intentos"]),
                "r9_total_usd": round(sum(x["costo_R9_usd"] for x in v["intentos"]), 6),
                "r9_final_usd": None, "llamadas": None, "al_tope": False, "vio_marca": False, "modales": None,
                "carpeta": f["carpeta"] if f else None}
        if f and (Path(f["carpeta"]) / f"meta_{f['id']}.json").is_file():
            m = json.loads((Path(f["carpeta"]) / f"meta_{f['id']}.json").read_text(encoding="utf-8"))
            fila["r9_final_usd"] = LA.costo_desde_tokens(m["modelos_R8"]["uso_por_modelo"], precios)["total_usd"]
            fila["llamadas"] = (m.get("hb2") or {}).get("n_llamadas_log_r1")
            fila["al_tope"] = (fila["llamadas"] or 0) >= TOPE_LLAMADAS or f["clase"] == "corte_R5"
            fila["vio_marca"] = marcas_vistas(Path(f["carpeta"]) / f"log_r1_{f['id']}.jsonl")
            r = (m.get("final_json_R4") or {}).get("respuesta")
            if f["clase"] == "completa" and isinstance(r, str) and r.strip():
                io = CN.id_opaco(s["qid"], s["configuracion"], s["rep"], CN.sha256_texto(r))
                a = agg.get(io)
                if a is not None and a["n_criterios"] == n_crit:
                    fila["modales"] = a["modales"]
        filas.append(fila)
    return filas


# --------------------------------------------------------------------------- #
# Las medidas                                                                  #
# --------------------------------------------------------------------------- #
def fidelidad(filas: list[dict], Q: set, conf: str, rep: int | None = None, sensibilidad: bool = False) -> dict:
    fs = [f for f in filas if f["configuracion"] == conf and f["qid"] in Q and (rep is None or f["rep"] == rep)]
    cum = crit = 0
    faltan = []
    for f in fs:
        if f["modales"] is None:
            faltan.append(f["id"])
            if sensibilidad:
                crit += f["n_criterios"]
            continue
        cum += sum(1 for x in f["modales"] if x == "cumplido")
        crit += f["n_criterios"]
    return {"cumplidos": cum, "criterios": crit, "fidelidad": round(cum / crit, 6) if crit else None,
            "sesiones": len(fs), "sin_veredicto": len(faltan), "ids_sin_veredicto": sorted(faltan)}


def por_pregunta(filas: list[dict], Q: set, conf: str, sensibilidad: bool = False) -> dict:
    out = {}
    for q in sorted(Q):
        r = fidelidad(filas, {q}, conf, sensibilidad=sensibilidad)
        if r["fidelidad"] is not None:
            out[q] = r["fidelidad"]
    return out


def variacion_base(filas: list[dict], Q: set, sensibilidad: bool = False, conf: str = "B") -> dict:
    vs = {r: fidelidad(filas, Q, conf, rep=r, sensibilidad=sensibilidad)["fidelidad"] for r in (1, 2, 3)}
    ok = [x for x in vs.values() if x is not None]
    return {"por_corrida": vs, "V": round(max(ok) - min(ok), 6) if len(ok) == 3 else None}


def delta(filas: list[dict], Q: set, a: str, b: str, sensibilidad: bool = False) -> dict:
    fa, fb = fidelidad(filas, Q, a, sensibilidad=sensibilidad)["fidelidad"], fidelidad(filas, Q, b, sensibilidad=sensibilidad)["fidelidad"]
    pa, pb = por_pregunta(filas, Q, a, sensibilidad), por_pregunta(filas, Q, b, sensibilidad)
    comunes = sorted(set(pa) & set(pb))
    return {"delta": None if fa is None or fb is None else round(fa - fb, 6),
            "preguntas_comunes": len(comunes), "suben": sum(pa[q] > pb[q] for q in comunes),
            "bajan": sum(pa[q] < pb[q] for q in comunes), "igual": sum(pa[q] == pb[q] for q in comunes)}


def conjuntos(e: dict, lista_f5: list[str]) -> dict:
    ps = e["_preguntas"]
    cupo = lambda ks: {q for q, p in ps.items() if p["conjunto"] == "cupo" and p["necesidad"] in ks}  # noqa: E731
    mezcla = lambda f: {q for q, p in ps.items() if p["conjunto"] == "mezcla" and f(p)}  # noqa: E731
    return {"30": set(ps), 1: cupo({1}), 2: cupo({4, 5, 6, 7}),
            3: cupo({2}) | mezcla(lambda p: p["subtipo"] == "remision"),
            4: cupo({3}) | mezcla(lambda p: p["subtipo"] == "excepcion_en_hijo"),
            5: set(lista_f5) & mezcla(lambda p: True), 6: mezcla(lambda p: p["tipo"] == "varios_puntos")}


def operativo(filas: list[dict], conf: str, Q: set) -> dict:
    fs = [f for f in filas if f["configuracion"] == conf and f["qid"] in Q]
    con_meta = [f for f in fs if f["r9_final_usd"] is not None]
    ll = [f["llamadas"] for f in con_meta if f["llamadas"] is not None]
    return {"sesiones": len(fs), "clases": dict(Counter(f["clase"] for f in fs)),
            "al_tope": sum(f["al_tope"] for f in fs), "cortadas_por_R5": sum(f["clase"] == "corte_R5" for f in fs),
            "llamadas_media": round(sum(ll) / len(ll), 3) if ll else None, "llamadas_max": max(ll) if ll else None,
            "r9_medio_por_pregunta_usd": round(sum(f["r9_final_usd"] for f in con_meta) / len(con_meta), 6) if con_meta else None,
            "r9_total_con_reintentos_usd": round(sum(f["r9_total_usd"] for f in fs), 6),
            "reintentadas": sum(f["n_intentos"] > 1 for f in fs)}


def no_cumplidos(filas: list[dict]) -> list[dict]:
    """La entrada de la clasificación de N1: por sesión con veredicto, los criterios cuyo modal no es «cumplido»."""
    return [{"id": f["id"], "qid": f["qid"], "configuracion": f["configuracion"], "rep": f["rep"],
             "criterios_no_cumplidos": [i + 1 for i, x in enumerate(f["modales"]) if x != "cumplido"]}
            for f in filas if f["modales"] is not None and any(x != "cumplido" for x in f["modales"])]


def clases_n1(ruta: Path | None, sha_regla: str | None, filas: list[dict]) -> dict:
    if ruta is None:
        return {"estado": "PENDIENTE", "motivo": "la clasificación se hace con la regla sellada de N1 (db2cc290…), que vive en "
                                                 "una carpeta que el despacho de N6 veda; este análisis deja su entrada"}
    if not sha_regla or not sha_regla.startswith(PREFIJO_REGLA_N1):
        raise SystemExit("ABORTO: la clasificación de N1 no trae el sha256 de la regla sellada (db2cc290…)")
    d = json.loads(Path(ruta).read_text(encoding="utf-8"))
    if d.get("sha256_regla") != sha_regla:
        raise SystemExit("ABORTO: la clasificación no se hizo con la regla que se pasa")
    nc = {(x["id"], c) for x in no_cumplidos(filas) for c in x["criterios_no_cumplidos"]}
    filas_c = {(x["id"], x["criterio"]): x["clase"] for x in d["filas"]}
    if set(filas_c) != nc:
        raise SystemExit("ABORTO: la clasificación no cubre exactamente los criterios no cumplidos")
    conf_de = {f["id"]: f["configuracion"] for f in filas}
    out = {}
    for (sid, _), cl in filas_c.items():
        out.setdefault(conf_de[sid], Counter())[cl] += 1
    return {"estado": "contada", "sha256_regla": sha_regla, "ruta": CN.rel_repo(Path(ruta)), "sha256": sha256_file(Path(ruta)),
            "por_configuracion": {k: dict(v) for k, v in sorted(out.items())}}


def python_para_citas(python: str | None) -> str:
    """Un intérprete 3.12 o más nuevo para el instrumento de citas: el que se pasa, este si lo es, o python3 del PATH."""
    cand = python or (sys.executable if sys.version_info >= (3, 12) else shutil.which("python3"))
    v = subprocess.run([cand, "-I", "-c", "import sys; print(sys.version_info >= (3, 12))"], capture_output=True, text=True)
    if v.stdout.strip() != "True":
        raise SystemExit("ABORTO: el instrumento de citas necesita Python 3.12 o más nuevo")
    return cand


def citas(e: dict, salida: Path, filas: list[dict], trabajo: Path, e0: Path, manifiesto: Path | None,
          python: str | None = None) -> dict:
    """El instrumento de la decisión 4 sobre el intento final de cada sesión con meta; por configuración, n de N."""
    con_meta = [f for f in filas if f["carpeta"] and (Path(f["carpeta"]) / f"meta_{f['intento']}.json").is_file()]
    if not con_meta:
        return {"estado": "sin sesiones"}
    trabajo.mkdir(parents=True, exist_ok=True)
    anclas = {q: p["anclas"] for q, p in e["_preguntas"].items()}
    (trabajo / "anclas_n6.json").write_text(json.dumps(anclas, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (trabajo / "mapa_sesiones_n6.json").write_text(json.dumps({f["intento"]: f["qid"] for f in con_meta}, ensure_ascii=False,
                                                              indent=1) + "\n", encoding="utf-8")
    cmd = [python_para_citas(python), "-B", str(INSTRUMENTO_CITAS), "--sesiones",
           *[str(d) for d in sorted({Path(f["carpeta"]) for f in con_meta})],
           "--anclas", str(trabajo / "anclas_n6.json"), "--e0", str(e0), "--mapa-sesiones", str(trabajo / "mapa_sesiones_n6.json"),
           "--out-json", str(trabajo / "citas_n6.json")] + (["--manifiesto", str(manifiesto)] if manifiesto else [])
    r = subprocess.run(cmd, capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    if r.returncode:
        raise SystemExit("ABORTO: el instrumento de citas frenó: " + (r.stdout + r.stderr).strip().splitlines()[-1][:300])
    out = json.loads((trabajo / "citas_n6.json").read_text(encoding="utf-8"))
    conf_de = {f["intento"]: f["configuracion"] for f in con_meta}
    tabla = {}
    for fi in out["filas"]:
        c = conf_de[fi["sesion"]]
        t = tabla.setdefault(c, {k: Counter() for k in INDICADORES} | {"N": 0})
        t["N"] += 1
        for k in INDICADORES:
            t[k][fi[k]] += 1
    return {"estado": "medida", "instrumento": {"ruta": "scripts/ucita2_indicadores_banco.py", "sha256": out["script_sha256"]},
            "anclas_en_indice": out["anclas_en_indice"], "salida_sha256": sha256_file(trabajo / "citas_n6.json"),
            "por_configuracion": {c: {"N": t["N"], **{k: dict(t[k]) | {"si_n_de_N": f"{t[k][SI]} de {t['N']}"}
                                                   for k in INDICADORES}} for c, t in sorted(tabla.items())}}


# --------------------------------------------------------------------------- #
# La regla de decisión                                                         #
# --------------------------------------------------------------------------- #
def mezcla_ejemplos(confs) -> bool:
    """Si entre las configuraciones hay una con los ejemplos de la familia 6 y otra sin ellos (decisión 9)."""
    return bool(set(confs) & set(CON_EJEMPLOS)) and bool(set(confs) & set(SIN_EJEMPLOS))


def elegir(filas: list[dict], Q: set, v: float | None, cands: list[str], caso_jerarquia: dict | None, tiene_ver_punto: dict,
           sensibilidad: bool) -> dict:
    """La elección de N4, §5, sobre Q: la de mayor fidelidad; si otras quedan dentro de V de ella, la que llega menos veces al
    tope y, después, la más barata (R9 medio por pregunta), todo sobre Q; y el requisito de la jerarquía."""
    fid = {c: fidelidad(filas, Q, c, sensibilidad=sensibilidad)["fidelidad"] for c in cands}
    cs = [c for c in cands if fid[c] is not None]
    if not cs:
        return None
    ops = {c: operativo(filas, c, Q) for c in cs}
    mejor = max(fid[c] for c in cs)
    vv = v or 0.0
    empatadas = [c for c in cs if fid[c] >= mejor - vv - 1e-12]
    orden = sorted(empatadas, key=lambda c: (ops[c]["al_tope"], ops[c]["r9_medio_por_pregunta_usd"] or 0.0, -fid[c], c))
    gana = orden[0]
    pasa = bool(tiene_ver_punto.get(gana)) and bool((caso_jerarquia or {}).get("llega_en_2_llamadas_o_menos"))
    return {"preguntas": len(Q), "candidatas": cs, "fidelidades": fid, "mejor_fidelidad": mejor, "V": v, "dentro_de_V": empatadas,
            "al_tope": {c: ops[c]["al_tope"] for c in empatadas},
            "r9_medio_por_pregunta_usd": {c: ops[c]["r9_medio_por_pregunta_usd"] for c in empatadas},
            "orden_de_desempate": orden, "elegida": gana,
            "caso_de_la_jerarquia": {"pasa": pasa, "por": ("tiene ver_punto: el camino de 2 llamadas probado en T" if pasa else
                                                            "no tiene ver_punto o el caso no se probó: la configuración vuelve a "
                                                            "la autora")},
            "se_preregistra_asi": pasa}


def regla(filas: list[dict], Qs: dict, caso_jerarquia: dict | None, tiene_ver_punto: dict, sensibilidad: bool = False) -> dict:
    """La regla de N4, §5 y §6, con el desvío de la decisión 9: lo que compara una configuración con los ejemplos de la familia 6
    (CON_EJEMPLOS) con una sin ellos (SIN_EJEMPLOS) va sin FUERA_D9, con V sobre las mismas preguntas, y la versión con todas
    al lado («con_las_30»); lo demás, con todas."""
    fuera = set(FUERA_D9)
    Qr = {k: Q - fuera for k, Q in Qs.items()}
    V = {str(k): variacion_base(filas, Q, sensibilidad) for k, Q in Qs.items()}
    Vr = {str(k): variacion_base(filas, Q, sensibilidad) for k, Q in Qr.items()}
    fid = {c: fidelidad(filas, Qs["30"], c, sensibilidad=sensibilidad)["fidelidad"] for c in GRAFO}
    fid_r = {c: fidelidad(filas, Qr["30"], c, sensibilidad=sensibilidad)["fidelidad"] for c in GRAFO}

    def elegible(Q: set, v: dict, c: str) -> dict:
        ft, fk = (fidelidad(filas, Q, x, sensibilidad=sensibilidad)["fidelidad"] for x in ("T", c))
        dif = None if ft is None or fk is None else round(ft - fk, 6)
        return {"Qk": sorted(Q), "fidelidad_T": ft, "fidelidad_sin_la_familia": fk, "T_menos_TFk": dif, "V_Qk": v["V"],
                "elegible": dif is not None and v["V"] is not None and dif <= v["V"] + 1e-12,
                "delta_por_pregunta": delta(filas, Q, "T", c, sensibilidad)}
    familias = {}
    for k in (1, 2, 3, 4, 5, 6):
        c = f"T-F{k}"
        if c in SIN_EJEMPLOS:
            familias[c] = {"sobre": "Qk sin FUERA_D9 (decisión 9)", **elegible(Qr[k], Vr[str(k)], c),
                           "con_las_30": elegible(Qs[k], V[str(k)], c)}
        else:
            familias[c] = {"sobre": "Qk", **elegible(Qs[k], V[str(k)], c)}
    cands = [c for c in CANDIDATAS if fid[c] is not None and (c in ("B", "T") or familias[c]["elegible"])]
    eleccion = None
    if cands:
        if mezcla_ejemplos(cands):
            eleccion = {"sobre": f"las {len(Qr['30'])} sin FUERA_D9 (decisión 9)",
                        **(elegir(filas, Qr["30"], Vr["30"]["V"], cands, caso_jerarquia, tiene_ver_punto, sensibilidad) or {}),
                        "con_las_30": elegir(filas, Qs["30"], V["30"]["V"], cands, caso_jerarquia, tiene_ver_punto, sensibilidad)}
        else:
            eleccion = {"sobre": f"las {len(Qs['30'])}",
                        **(elegir(filas, Qs["30"], V["30"]["V"], cands, caso_jerarquia, tiene_ver_punto, sensibilidad) or {})}
    comparaciones = {}
    for c in GRAFO:
        if c == "T":
            continue
        if mezcla_ejemplos(("T", c)):
            comparaciones[c] = {"sobre": "sin FUERA_D9 (decisión 9)", **delta(filas, Qr["30"], c, "T", sensibilidad),
                                "con_las_30": delta(filas, Qs["30"], c, "T", sensibilidad)}
        else:
            comparaciones[c] = {"sobre": "las 30", **delta(filas, Qs["30"], c, "T", sensibilidad)}
    vf = variacion_base(filas, Qs["30"], sensibilidad, conf="F1_bm25")
    fb, fh = (fidelidad(filas, Qs["30"], c, sensibilidad=sensibilidad)["fidelidad"] for c in ("F1_bm25", "F1_hibrida"))
    f1 = {"fidelidad_bm25": fb, "fidelidad_hibrida": fh, "Vfrag_30": vf,
          "entra_la_hibrida": None if fb is None or fh is None or vf["V"] is None else fh >= fb - vf["V"] - 1e-12,
          "delta_por_pregunta": delta(filas, Qs["30"], "F1_hibrida", "F1_bm25", sensibilidad)}
    return {"fuera_de_las_comparaciones_con_y_sin_ejemplos": sorted(fuera), "V": V, "V_sin_FUERA_D9": Vr,
            "fidelidad_30": fid, "fidelidad_sin_FUERA_D9": fid_r, "familias": familias, "eleccion": eleccion,
            "contra_T": comparaciones, "F1": f1}


def analizar(e: dict, salida: Path, lista_f5: list[str], caso: dict | None, trabajo: Path, e0: Path = E0_ACUMULADO,
             manifiesto: Path | None = None, clases: Path | None = None, sha_regla: str | None = None,
             python_citas: str | None = None) -> dict:
    filas = cargar_sesiones(e, salida)
    Qs = conjuntos(e, lista_f5)
    tiene_vp = {b["configuracion_n6"]: "mcp__kg__ver_punto" in b["tools_esperadas"]
                for b in e["_cfg"]["brazos"].values() if b.get("servidor") == "kg"}
    confs = list(e["_cfg"]["configuraciones_n6"])
    medidas = {}
    for c in confs:
        m = {"30": fidelidad(filas, Qs["30"], c), "30_sensibilidad": fidelidad(filas, Qs["30"], c, sensibilidad=True),
             "sin_FUERA_D9": fidelidad(filas, Qs["30"] - set(FUERA_D9), c)}
        for k in (1, 2, 3, 4, 5, 6):
            m[f"Q{k}"] = fidelidad(filas, Qs[k], c)
        if c in REPETIDAS:
            m["por_corrida"] = {r: fidelidad(filas, Qs["30"], c, rep=r) for r in (1, 2, 3)}
        verif = {f["qid"] for f in filas if f["configuracion"] == c and f["vio_marca"]}
        m["vio_una_marca"] = fidelidad([f for f in filas if f["vio_marca"]], Qs["30"], c)
        m["no_vio_ninguna_marca"] = fidelidad([f for f in filas if not f["vio_marca"]], Qs["30"], c)
        m["preguntas_con_marca_vista"] = len(verif)
        m["operativo"] = operativo(filas, c, Qs["30"])
        medidas[c] = m
    return {"unidad": "U-NAV-DISENO, N6 — el análisis (protocolo de N4, f69e95ea, §4 a §6)",
            "analisis": {"ruta": CN.rel_repo(Path(__file__)), "sha256": sha256_file(Path(__file__))},
            "entrada_sha256": e.get("_sha"), "conjuntos": {str(k): sorted(v) for k, v in Qs.items()},
            "n_sesiones": len(filas), "clases": dict(Counter(f["clase"] for f in filas)),
            "medidas": medidas, "regla": regla(filas, Qs, caso, tiene_vp),
            "regla_sensibilidad": regla(filas, Qs, caso, tiene_vp, sensibilidad=True),
            "citas": citas(e, salida, filas, trabajo, e0, manifiesto, python_citas),
            "clases_n1": clases_n1(clases, sha_regla, filas), "no_cumplidos_para_n1": no_cumplidos(filas),
            "caso_jerarquia": None if caso is None else {k: caso.get(k) for k in ("configuracion", "llamadas",
                                                                                  "llega_en_2_llamadas_o_menos")},
            "sin_veredicto": sorted(f["id"] for f in filas if f["modales"] is None)}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", type=Path, default=CN.ENTRADA_DEFAULT)
    ap.add_argument("--sha256-entrada", required=True)
    ap.add_argument("--salida-n6", type=Path, default=CN.SALIDA_DEFAULT)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--caso-jerarquia", type=Path, default=None)
    ap.add_argument("--clases-n1", type=Path, default=None)
    ap.add_argument("--sha256-regla-n1", default=None)
    ap.add_argument("--e0", type=Path, default=E0_ACUMULADO)
    ap.add_argument("--manifiesto", type=Path, default=None)
    ap.add_argument("--python-citas", default=None,
                    help="Python 3.12 o más nuevo para el instrumento de citas (por defecto, el de la entrada sellada)")
    a = ap.parse_args(argv)
    e = CN.cargar_entrada(a.entrada, a.sha256_entrada)
    e["_sha"] = a.sha256_entrada
    lf = e.get("lista_familia5")
    lista = json.loads((REPO_DIR / lf["ruta"]).read_text(encoding="utf-8"))["lista_familia5"] if lf else []
    caso = json.loads(a.caso_jerarquia.read_text(encoding="utf-8")) if a.caso_jerarquia else None
    python_citas = a.python_citas or (str(CN.ruta_de(e["citas"]["python"]["ruta"])) if e.get("citas") else None)
    r = analizar(e, a.salida_n6.resolve(), lista, caso, a.salida.parent / "citas_n6", a.e0, a.manifiesto, a.clases_n1,
                 a.sha256_regla_n1, python_citas)
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"análisis de N6: {r['n_sesiones']} sesiones -> {CN.rel_repo(a.salida)} ({sha256_file(a.salida)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
