#!/usr/bin/env python3
"""analizar_n7c.py — El análisis de B2 de N7c, escrito y probado sobre datos de juguete antes de correr B2
(n7c/selftest_analizar_n7c.py). USD 0: lee la entrada, las metas, los streams y los logs R1 de las sesiones, los veredictos del
juez y sus cachés; no llama a ningún modelo. Usa, sin editarlas, las funciones de N6 (n6/analizar_n6.py: fidelidad, operativo y
citas; n6/correr_n6.py: estado, casos_del_juez y agregar).

Por configuración (N7, N7c y N7c+; N7c+ con la clave N7c_amp):
  - fidelidad por criterio, con el juez de EV2 y su lectura tolerante (lectura_tolerante_juez.py, como en N6): la salida del
    juez que la lectura estricta rechazó (errores_r{k}.jsonl) se busca en la caché de su repetición por su clave
    (llm_cache.compute_key del espacio de nombres del juez y el pedido, que se rearma con juez.construir_kwargs) y, si la
    lectura tolerante aplica y lee, entra como veredicto; con eso, correr_n6.agregar da los agregados tolerantes. Principal:
    con la lectura tolerante; al lado, la estricta (los agregados del corredor) y la sensibilidad (lo que no tiene veredicto
    cuenta como no cumplido). En el total y en las de tipo `dato_directo`;
  - en las de tipo `varios_puntos`, la fracción de sesiones que consultaron todas las anclas, con el lector de la enmienda 1
    (n7c/lector_anclas_n7c.py sobre atribucion_fallas_nav.py, con un Python 3.12): cada sesión de esas preguntas cuenta, y una
    sin log R1 o sin llamadas no consultó ninguna; por subtipo, como descriptiva;
  - las citas, con scripts/ucita2_indicadores_banco.py por su línea de comandos (analizar_n6.citas, sin editarlo), sobre la
    E0 del grafo evaluado: cita fundada, existente y al ancla, «n de N» y su fracción;
  - las sesiones con 30 llamadas o más, las cortadas por R5, las que están al tope (una u otra, analizar_n6.operativo) y su
    fracción, y el costo R9.
La regla de adopción (D-B2-9), fijada acá antes de correr B2. Para N7c y para N7c+, frente a N7:
  (i)   la fracción de las de varios puntos que consultaron todas las anclas sube (estrictamente);
  (ii)  la fidelidad no baja más de 5 puntos (0,05), ni en el total ni en dato directo;
  (iii) las sesiones al tope de 30 llamadas (30 llamadas o más, o cortadas por R5) no pasan del 5 % de sus sesiones;
  (iv)  solo para N7c+: su fracción de sesiones con cita fundada no baja frente a N7.
Se adopta N7c+ si cumple (i) a (iv); si no, N7c, si cumple (i) a (iii); si no, N7. Una medida que falta (None) no cumple.
Escribe el JSON (--salida) y lo imprime resumido: solo cuentas, fracciones y sí o no. Sin texto de preguntas, criterios ni
respuestas.
Uso: .venv/bin/python -B data/experiment/banco_mcp/n7c/analizar_n7c.py --entrada n7c/entrada_n7c_n3.json --sha256-entrada <hex>
       --salida-b2 ~/INGENIERIA IA/TESIS/fuera_del_repo/banco_n7c --salida <json fuera del repo>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sqlite3
import subprocess
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(AQUI), str(BANCO_DIR / "n6"), str(BANCO_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import correr_n7c as C7                          # noqa: E402
import analizar_n6 as AN                         # noqa: E402  (HEAD, sin editar)
import lectura_tolerante_juez as LT              # noqa: E402  (HEAD, sin editar)

CN = C7.CN
J, M, LA = CN.J, CN.M, CN.LA
REPO_DIR = CN.REPO_DIR
CONFIGS = ("N7", "N7c", "N7c_amp")
NOMBRE = {"N7": "N7", "N7c": "N7c", "N7c_amp": "N7c+"}
CANDIDATAS = ("N7c", "N7c_amp")
UMBRAL_FIDELIDAD, UMBRAL_TOPE = 0.05, 0.05
EPS = 1e-12
LECTOR_ANCLAS = AQUI / "lector_anclas_n7c.py"
_CFG_N7 = json.loads((BANCO_DIR / "n7" / "config_mcp_kg_n7_evaluado.json").read_text(encoding="utf-8"))
INDICE = (BANCO_DIR / "mcp_kg" / _CFG_N7["indice_puntos"]).resolve()
SHA_MANIFIESTO = _CFG_N7["sha256_manifiesto_indice"]
E0_EVALUADO = REPO_DIR / json.loads((INDICE / "manifiesto.json").read_text(encoding="utf-8"))["e0_dir"] \
    if (INDICE / "manifiesto.json").is_file() else None


def sha256_file(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def fraccion(n: int, d: int) -> float | None:
    return round(n / d, 6) if d else None


# --------------------------------------------------------------------------- #
# El juez con su lectura tolerante                                             #
# --------------------------------------------------------------------------- #
def texto_de(raw: str) -> str:
    return "".join(b.get("text", "") for b in json.loads(raw).get("content", []) if b.get("type") == "text")


def filas_cache(db: Path) -> dict:
    """{clave: (stop_reason, texto, input_tokens, output_tokens)} de la caché de una repetición, en solo lectura."""
    if not db.is_file():
        return {}
    con = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    try:
        rs = con.execute("SELECT key, stop_reason, raw_json, input_tokens, output_tokens FROM cache").fetchall()
    finally:
        con.close()
    return {k: (stop, texto_de(raw), it, ot) for k, stop, raw, it, ot in rs}


def lectura_tolerante(e: dict, salida: Path, trabajo: Path) -> tuple[dict, dict, dict]:
    """(agregados estrictos, agregados con la lectura tolerante, informe). Los estrictos, recomputados con correr_n6.agregar
    desde los veredictos del corredor, tienen que ser los del archivo del corredor (se informa)."""
    juez_dir = salida / "juez"
    casos, _ = CN.casos_del_juez(e, salida)
    estrictos = CN.agregar(juez_dir, casos)
    archivo = juez_dir / "agregados_n6_ciego.json"
    informe = {"estrictos_iguales_a_los_del_corredor": archivo.is_file()
               and json.loads(archivo.read_text(encoding="utf-8"))["agregados"] == estrictos["agregados"]}
    lc = J.lc
    nuevos = {rep: [] for rep in CN.REPS_JUEZ}
    cuenta = Counter()
    for rep in CN.REPS_JUEZ:
        errores = {r["id_opaco"] for r in CN.leer_jsonl(juez_dir / f"errores_r{rep}.jsonl")}
        cache = filas_cache(CN.db_juez(rep, juez_dir / "cache"))
        ns = lc.make_namespace(f"juez_ev2_r{rep}", code_ver=J.CODE_VER, thinking=False)
        for c in casos:
            if c["id_opaco"] not in errores:
                continue
            cuenta["rechazadas_por_la_estricta"] += 1
            clave = lc.compute_key(ns, lc.canonical_request(J.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])))
            if clave not in cache:
                cuenta["sin_su_salida_en_la_cache"] += 1
                continue
            stop, texto, it, ot = cache[clave]
            if not LT.aplica(texto, stop):
                cuenta["la_tolerante_no_aplica"] += 1
                continue
            try:
                v = LT.leer(texto, len(c["criterios"]))
            except ValueError:
                cuenta["la_tolerante_no_lee"] += 1
                continue
            cuenta["leidas_por_la_tolerante"] += 1
            nuevos[rep].append({"id_opaco": c["id_opaco"], "rep": rep, "clasificacion_respuesta": v["clasificacion_respuesta"],
                                "criterios": v["criterios"], "meta": {"input_tokens": it, "output_tokens": ot},
                                "lectura": "tolerante"})
    tol_dir = trabajo / "juez_con_lectura_tolerante"
    tol_dir.mkdir(parents=True, exist_ok=True)
    for rep in CN.REPS_JUEZ:
        filas = CN.leer_jsonl(juez_dir / f"veredictos_r{rep}.jsonl") + nuevos[rep]
        (tol_dir / f"veredictos_r{rep}.jsonl").write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in filas),
                                                         encoding="utf-8")
    tolerantes = CN.agregar(tol_dir, casos)
    (tol_dir / "agregados_n6_ciego.json").write_text(json.dumps(tolerantes, ensure_ascii=False, indent=1) + "\n",
                                                     encoding="utf-8")
    informe |= dict(sorted(cuenta.items())) | {"agregados_estrictos": estrictos["n_agregados"],
                                               "agregados_tolerantes": tolerantes["n_agregados"]}
    return estrictos, tolerantes, informe


def cargar_filas(e: dict, salida: Path, agregados: dict) -> list[dict]:
    """analizar_n6.cargar_sesiones con los agregados que se pasan (estrictos o tolerantes) en lugar de los del archivo."""
    st = CN.estado(e, salida)
    agg = {a["id_opaco"]: a for a in agregados["agregados"]}
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
            fila["al_tope"] = (fila["llamadas"] or 0) >= AN.TOPE_LLAMADAS or f["clase"] == "corte_R5"
            fila["vio_marca"] = AN.marcas_vistas(Path(f["carpeta"]) / f"log_r1_{f['id']}.jsonl")
            r = (m.get("final_json_R4") or {}).get("respuesta")
            if f["clase"] == "completa" and isinstance(r, str) and r.strip():
                a = agg.get(CN.id_opaco(s["qid"], s["configuracion"], s["rep"], CN.sha256_texto(r)))
                if a is not None and a["n_criterios"] == n_crit:
                    fila["modales"] = a["modales"]
        filas.append(fila)
    return filas


# --------------------------------------------------------------------------- #
# Las anclas consultadas                                                       #
# --------------------------------------------------------------------------- #
def anclas_consultadas(e: dict, filas: list[dict], python: str, lectura: dict) -> dict:
    """Por sesión de las preguntas de varios puntos: cuántas anclas, cuántas consultadas y si todas (lector_anclas_n7c.py)."""
    ps = e["_preguntas"]
    ses = [{"id": f["id"], "anclas": ps[f["qid"]]["anclas"],
            "log": str(Path(f["carpeta"]) / f"log_r1_{f['intento']}.jsonl") if f["carpeta"] else None}
           for f in filas if ps[f["qid"]]["tipo"] == "varios_puntos"]
    r = subprocess.run([python, "-I", "-B", str(LECTOR_ANCLAS)], input=json.dumps(lectura | {"sesiones": ses}, ensure_ascii=False),
                       capture_output=True, text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    if r.returncode:
        raise SystemExit("ABORTO: el lector de las anclas frenó: " + (r.stdout + r.stderr).strip().splitlines()[-1][:300])
    return json.loads(r.stdout)["sesiones"]


def varios_puntos(e: dict, filas: list[dict], consultas: dict, conf: str) -> dict:
    ps = e["_preguntas"]
    fs = [f for f in filas if f["configuracion"] == conf and ps[f["qid"]]["tipo"] == "varios_puntos"]
    todas = [f for f in fs if consultas[f["id"]]["todas"] and consultas[f["id"]]["con_llamadas"]]
    por_subtipo = {}
    for st in sorted({ps[f["qid"]]["subtipo"] or "—" for f in fs}):
        g = [f for f in fs if (ps[f["qid"]]["subtipo"] or "—") == st]
        n = sum(1 for f in g if f in todas)
        por_subtipo[st] = {"sesiones": len(g), "con_todas_las_anclas_consultadas": n, "fraccion": fraccion(n, len(g))}
    return {"sesiones": len(fs), "con_todas_las_anclas_consultadas": len(todas), "fraccion": fraccion(len(todas), len(fs)),
            "anclas": sum(consultas[f["id"]]["anclas"] for f in fs),
            "anclas_consultadas": sum(consultas[f["id"]]["consultadas"] for f in fs),
            "por_subtipo_descriptiva": por_subtipo}


# --------------------------------------------------------------------------- #
# La regla de adopción (D-B2-9)                                                #
# --------------------------------------------------------------------------- #
def _ge(a, b, tol: float = 0.0) -> bool:
    return a is not None and b is not None and a >= b - tol - EPS


def regla_adopcion(m: dict) -> dict:
    """m: {conf: {"fidelidad_30", "fidelidad_dato_directo", "varios_fraccion", "al_tope_fraccion", "cita_fundada_fraccion"}}."""
    base = m["N7"]
    partes = {}
    for c in CANDIDATAS:
        x = m[c]
        p = {"i_varios_puntos_sube": x["varios_fraccion"] is not None and base["varios_fraccion"] is not None
             and x["varios_fraccion"] > base["varios_fraccion"] + EPS,
             "ii_fidelidad_total_no_baja_mas_de_5_puntos": _ge(x["fidelidad_30"], base["fidelidad_30"], UMBRAL_FIDELIDAD),
             "ii_fidelidad_dato_directo_no_baja_mas_de_5_puntos": _ge(x["fidelidad_dato_directo"],
                                                                      base["fidelidad_dato_directo"], UMBRAL_FIDELIDAD),
             "iii_al_tope_hasta_el_5_por_ciento": x["al_tope_fraccion"] is not None
             and x["al_tope_fraccion"] <= UMBRAL_TOPE + EPS}
        if c == "N7c_amp":
            p["iv_cita_fundada_no_baja"] = _ge(x["cita_fundada_fraccion"], base["cita_fundada_fraccion"])
        p["cumple_i_a_iii"] = all(v for k, v in p.items() if not k.startswith("iv"))
        if c == "N7c_amp":
            p["cumple_i_a_iv"] = p["cumple_i_a_iii"] and p["iv_cita_fundada_no_baja"]
        partes[NOMBRE[c]] = p
    adoptada = ("N7c+" if partes["N7c+"]["cumple_i_a_iv"] else "N7c" if partes["N7c"]["cumple_i_a_iii"] else "N7")
    return {"frente_a": "N7", "umbral_fidelidad": UMBRAL_FIDELIDAD, "umbral_al_tope": UMBRAL_TOPE, "partes": partes,
            "adoptada": adoptada}


# --------------------------------------------------------------------------- #
def analizar(e: dict, salida: Path, trabajo: Path, python_citas: str, e0: Path, lectura: dict) -> dict:
    estrictos, tolerantes, informe_juez = lectura_tolerante(e, salida, trabajo)
    filas_t, filas_e = cargar_filas(e, salida, tolerantes), cargar_filas(e, salida, estrictos)
    reproduce = [{k: v for k, v in f.items()} for f in AN.cargar_sesiones(e, salida)] == filas_e
    ps = e["_preguntas"]
    Q = {"30": set(ps), "dato_directo": {q for q, p in ps.items() if p["tipo"] == "dato_directo"},
         "varios_puntos": {q for q, p in ps.items() if p["tipo"] == "varios_puntos"}}
    consultas = anclas_consultadas(e, filas_t, python_citas, lectura)
    citas = AN.citas(e, salida, filas_t, trabajo / "citas", e0, None, python_citas)
    medidas, para_regla = {}, {}
    for c in CONFIGS:
        op = AN.operativo(filas_t, c, Q["30"])
        fs = [f for f in filas_t if f["configuracion"] == c]
        con30 = sum(1 for f in fs if (f["llamadas"] or 0) >= AN.TOPE_LLAMADAS)
        ct = (citas.get("por_configuracion") or {}).get(c)
        fundada = None if ct is None else {"si": ct["ind1_cita_fundada"].get(AN.SI, 0), "N": ct["N"],
                                           "fraccion": fraccion(ct["ind1_cita_fundada"].get(AN.SI, 0), ct["N"])}
        m = {"nombre": NOMBRE[c],
             "fidelidad": {"total": AN.fidelidad(filas_t, Q["30"], c), "dato_directo": AN.fidelidad(filas_t, Q["dato_directo"], c),
                           "total_sensibilidad": AN.fidelidad(filas_t, Q["30"], c, sensibilidad=True),
                           "dato_directo_sensibilidad": AN.fidelidad(filas_t, Q["dato_directo"], c, sensibilidad=True),
                           "total_lectura_estricta": AN.fidelidad(filas_e, Q["30"], c),
                           "dato_directo_lectura_estricta": AN.fidelidad(filas_e, Q["dato_directo"], c)},
             "varios_puntos": varios_puntos(e, filas_t, consultas, c),
             "citas": None if ct is None else {k: ct[k]["si_n_de_N"] for k in AN.INDICADORES} | {"N": ct["N"]},
             "cita_fundada": fundada,
             "operativo": op | {"con_30_llamadas_o_mas": con30, "fraccion_al_tope": fraccion(op["al_tope"], op["sesiones"])}}
        for k in ("fidelidad",):
            for kk, v in m[k].items():
                v.pop("ids_sin_veredicto", None)
        medidas[c] = m
        para_regla[c] = {"fidelidad_30": m["fidelidad"]["total"]["fidelidad"],
                         "fidelidad_dato_directo": m["fidelidad"]["dato_directo"]["fidelidad"],
                         "varios_fraccion": m["varios_puntos"]["fraccion"],
                         "al_tope_fraccion": m["operativo"]["fraccion_al_tope"],
                         "cita_fundada_fraccion": None if fundada is None else fundada["fraccion"]}
    return {"unidad": "N7c, B2 — el análisis (n7c/analizar_n7c.py)",
            "analisis": {"ruta": CN.rel_repo(Path(__file__)), "sha256": sha256_file(Path(__file__))},
            "entrada_sha256": e.get("_sha"), "n_sesiones": len(filas_t), "clases": dict(Counter(f["clase"] for f in filas_t)),
            "preguntas": {k: len(v) for k, v in Q.items()},
            "juez": informe_juez | {"filas_estrictas_iguales_a_las_de_analizar_n6": reproduce},
            "citas": {k: v for k, v in citas.items() if k != "por_configuracion"},
            "medidas": medidas, "para_la_regla": para_regla, "regla_de_adopcion": regla_adopcion(para_regla),
            "sin_veredicto": sorted(f["id"] for f in filas_t if f["modales"] is None)}


def resumen(r: dict) -> str:
    lin = [f"análisis de B2 de N7c: {r['n_sesiones']} sesiones; juez: estrictos {r['juez']['agregados_estrictos']}, "
           f"con la lectura tolerante {r['juez']['agregados_tolerantes']} agregados"]
    for c in CONFIGS:
        x, m = r["para_la_regla"][c], r["medidas"][c]
        lin.append(f"{NOMBRE[c]}: fidelidad {x['fidelidad_30']} (dato directo {x['fidelidad_dato_directo']}); varios puntos "
                   f"{m['varios_puntos']['con_todas_las_anclas_consultadas']} de {m['varios_puntos']['sesiones']} "
                   f"({x['varios_fraccion']}); cita fundada {x['cita_fundada_fraccion']}; al tope "
                   f"{m['operativo']['al_tope']} de {m['operativo']['sesiones']} ({x['al_tope_fraccion']}); R9 medio "
                   f"{m['operativo']['r9_medio_por_pregunta_usd']}")
    reg = r["regla_de_adopcion"]
    for c, p in reg["partes"].items():
        lin.append(f"{c}: " + "; ".join(f"{k} {'sí' if v else 'no'}" for k, v in p.items()))
    lin.append(f"adoptada: {reg['adoptada']}")
    return "\n".join(lin)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", type=Path, required=True)
    ap.add_argument("--sha256-entrada", required=True)
    ap.add_argument("--salida-b2", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--e0", type=Path, default=E0_EVALUADO)
    ap.add_argument("--python-citas", default=None,
                    help="Python 3.12 o más nuevo para el instrumento de citas y el lector de la enmienda (por defecto, el de "
                         "la entrada)")
    a = ap.parse_args(argv)
    e = CN.cargar_entrada(a.entrada, a.sha256_entrada)
    e["_sha"] = a.sha256_entrada
    salida = a.salida.resolve()
    if salida.is_relative_to(REPO_DIR):
        raise SystemExit("ABORTO: la salida del análisis está dentro del repo")
    python = AN.python_para_citas(a.python_citas or str(CN.ruta_de(e["citas"]["python"]["ruta"])))
    lectura = {"modo": "indice", "indice": str(INDICE), "sha256_manifiesto": SHA_MANIFIESTO, "repo": str(REPO_DIR)}
    trabajo = salida.parent / "trabajo_analisis_n7c"
    r = analizar(e, a.salida_b2.resolve(), trabajo, python, a.e0, lectura)
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(resumen(r))
    print(f"-> {CN.rel_repo(salida)} ({sha256_file(salida)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
