#!/usr/bin/env python3
"""juez_a2_2.py — El juez de A2.2 (pre-registro FIRMADO, a78ead7b, §4 y §6): el de EV2 tal cual, `data/experiment/ev2_juez/juez.py`
con su prompt v1 (`fd446f8e…`) y el veredicto por pregunta de `mapping.py`, importados sin editarlos. N = 3 por respuesta, con el
veredicto modal por criterio y el mapping del método de EV2 (§2 y §4).

Dos etapas, cada una sobre las respuestas de su carpeta de salida (a2_2/resultados/<etapa>/):
  n1          las respuestas de N = 1;
  recorridas  las de las tres re-corridas de la población de N = 3.
Solo se juzgan las sesiones completas por R3 con una respuesta en su JSON final; las demás quedan como faltantes, fuera de la
métrica y declaradas (§3, R5 (1)).

La ceguera (método de EV2, `:24-28` y `:47-48`): al juez viajan la pregunta, la respuesta final y los criterios con sus citas,
armados por `juez.construir_kwargs`, y nada más. Cada respuesta lleva un id opaco (`A22J-` + sha256(sal|pregunta|brazo|rep|
sha256 de la respuesta)[:10], con la repetición en la clave como en `ev2_encadenamiento/code/comun_enc.py`); la tabla id opaco →
(pregunta, brazo, repetición) va en desanonimizacion_SOLO_MESA/. Las marcas de brazo que el agente escriba en su respuesta no se
editan: se cuentan por brazo y se declaran.

El orden (A-D7): las respuestas ordenadas por (pregunta, sha256 de la respuesta, brazo, repetición) y
`random.Random("A22:orden_juez:v1").shuffle` (método de EV2, `:47-50`; `comun_enc.py`, `armar_casos`).

Las tres repeticiones del juez de una respuesta corren seguidas, cada una con su caché y su etiqueta (patrón rt_c6_n3 de EV2:
`ev2_juez/juez.py`, `construir_cliente_real`, con la caché de A2.2 en a2_2/juez/cache/a22_juez_r{1,2,3}.db). Una salida mal
formada se registra en errores_r{rep}.jsonl y no se reintenta (`pipeline_fidelidad.py`, `correr_repeticion`).

El corte del juez (§6): antes de cada respuesta, si el acumulado del juez de A2.2 (las filas de sus tres cachés, con los precios
de comun_a2_2) más el costo mayor de una respuesta ya juzgada (0,0378 mientras no haya ninguna) pasa el freno o el tope, frena
con el código 2 sin llamar. El juez sigue desde su caché sin volver a pagar (`ev2_juez/juez.py:16-18`).

El control del SDK y de la versión de la API (`scripts/control_sdk_anthropic_juez_y_banco.py`) va primero.

Modos: --modo real (con la clave que el juez de EV2 toma por su cuenta) y --modo seco (un cliente falso que no sale a la red, para
la corrida en seco). Imprime solo cuentas y costos.
Uso: .venv/bin/python -B data/experiment/banco_mcp/a2_2/juez_a2_2.py n1 --autorizado-tope 25 --freno 18.75
"""
from __future__ import annotations

import argparse
import json
import os
import random
import sqlite3
import subprocess
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
for _p in (str(AQUI), str(AQUI.parents[1] / "ev2_juez")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import comun_a2_2 as K                       # noqa: E402
import juez as J                             # noqa: E402  (EV2, congelado: solo import)
import mapping as M                          # noqa: E402  (EV2, congelado: solo import)

PROMPT_SHA256 = "fd446f8e61f46033d7de9b862121c698b2c52dcc2696b7f10993f44e509f5455"
SAL_ID_OPACO = "A22:id_opaco_juez:v1"
PREFIJO_ID = "A22J-"
DB_PREFIX = "a22_juez"
CACHE_DIR = K.JUEZ_DIR / "cache"
ETAPAS = ("n1", "recorridas")
CONTROL_SDK = K.REPO_DIR / "scripts" / "control_sdk_anthropic_juez_y_banco.py"
MARCAS_DE_BRAZO = ("mcp__", "buscar_pasajes", "buscar_nodos", "ver_nodo", "ver_vecinos", "pasaje", "fragmento", "nodo",
                   "vecino", "BM25", "embedding", "grafo")


class FrenoJuez(Exception):
    """El corte del juez: código 2."""


def controlar_instrumento() -> dict:
    if os.environ.get("JUEZ_PROMPT_VERSION") is not None:
        raise K.FrenoA22("JUEZ_PROMPT_VERSION está fijada: A2.2 corre sin esa variable (pre-registro, §4)")
    if J.PROMPT_VERSION != "v1" or J.PROMPT_SHA256 != PROMPT_SHA256 or J.MODELO != "claude-sonnet-4-6" or J.TEMPERATURE != 0.0:
        raise K.FrenoA22("el juez no es el de EV2 tal cual (prompt v1, claude-sonnet-4-6, temperatura 0)")
    return {"prompt_version": J.PROMPT_VERSION, "prompt_sha256": J.PROMPT_SHA256, "modelo": J.MODELO,
            "temperatura": J.TEMPERATURE, "code_ver": J.CODE_VER}


def control_sdk(python: str | None = None) -> dict:
    """El control de la §93, con el intérprete con que corre el juez (en el paso pago, el del .venv del repo: el control lo exige
    en su punto 1), sin red y sin leer ningún .env."""
    py = python or sys.executable
    r = subprocess.run([py, "-I", "-B", str(CONTROL_SDK)], capture_output=True, text=True)
    ok = r.returncode == 0
    if not ok:
        raise K.FrenoA22("el control del SDK y de la versión de la API frenó: " + " | ".join(
            l for l in r.stdout.splitlines() if l.startswith("FRENO")))
    return {"control_sdk": "OK", "lineas": [l for l in r.stdout.splitlines() if l.startswith(("OK", "control"))]}


# --------------------------------------------------------------------------- #
# Respuestas → casos ciegos                                                    #
# --------------------------------------------------------------------------- #
def respuestas(etapa: str, out_dir: Path, orden: dict, poblacion: dict | None = None) -> tuple[list[dict], list[dict]]:
    """(respuestas, faltantes) de las sesiones de la etapa. Una respuesta pide la meta, R3 completa y una respuesta no vacía."""
    xs, faltan = [], []
    for s in K.secuencia(orden, etapa, poblacion):
        p = out_dir / f"meta_{s['id']}.json"
        f = {"id_sesion": s["id"], "qid": s["qid"], "brazo": s["brazo"], "rep": s["rep"]}
        if not p.exists():
            faltan.append(f | {"motivo": "sin sesión"}); continue
        m = json.loads(p.read_text(encoding="utf-8"))
        if not m["completitud_R3"]["completa"]:
            faltan.append(f | {"motivo": "incompleta por R3", "motivos_R3": m["completitud_R3"]["motivos_incompleta"]}); continue
        r = (m.get("final_json_R4") or {}).get("respuesta")
        if not isinstance(r, str) or not r.strip():
            faltan.append(f | {"motivo": "sin respuesta en el JSON final"}); continue
        xs.append(f | {"respuesta": r, "respondible_flag": (m.get("final_json_R4") or {}).get("respondible")})
    return xs, faltan


def id_opaco(qid: str, brazo: str, rep: int, sha_resp: str) -> str:
    return PREFIJO_ID + K.sha256_texto(f"{SAL_ID_OPACO}|{qid}|{brazo}|{rep}|{sha_resp}")[:10]


def armar_casos(resps: list[dict], preguntas: dict) -> list[dict]:
    xs = []
    for r in resps:
        sha = K.sha256_texto(r["respuesta"])
        xs.append(r | {"sha256_respuesta": sha, "id_opaco": id_opaco(r["qid"], r["brazo"], r["rep"], sha),
                       "pregunta": preguntas[r["qid"]]["pregunta"], "criterios": preguntas[r["qid"]]["criterios"]})
    xs.sort(key=lambda c: (c["qid"], c["sha256_respuesta"], c["brazo"], c["rep"]))
    if len({c["id_opaco"] for c in xs}) != len(xs):
        raise K.FrenoA22("colisión de ids opacos")
    random.Random(K.SEMILLA_ORDEN_JUEZ).shuffle(xs)
    return xs


def vista_ciega(casos: list[dict]) -> list[dict]:
    return [{"id_opaco": c["id_opaco"], "pregunta": c["pregunta"], "respuesta": c["respuesta"], "criterios": c["criterios"]}
            for c in casos]


def verificar_ceguera(ciegos: list[dict]) -> list[str]:
    """Cada pedido es el prompt del juez + el mensaje armado con pregunta, respuesta y criterios, y nada más. Sin el texto de la
    respuesta (que no se edita), el mensaje no trae ningún id de sesión ni de brazo. Devuelve las fugas (vacío = OK)."""
    fugas = []
    for c in ciegos:
        if set(c) != {"id_opaco", "pregunta", "respuesta", "criterios"}:
            fugas.append("vista no ciega")
        kw = J.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        if set(kw) != {"model", "max_tokens", "temperature", "system", "messages"} or kw["system"] != J.PROMPT_JUEZ:
            fugas.append("estructura del pedido")
        if kw["messages"] != [{"role": "user", "content": J.construir_mensaje_usuario(c["pregunta"], c["respuesta"],
                                                                                      c["criterios"])}]:
            fugas.append("mensaje distinto del de construir_mensaje_usuario")
        sin_resp = J.construir_mensaje_usuario(c["pregunta"], "<respuesta>", c["criterios"])
        for marca in (PREFIJO_ID, "PRB-", "N1-", "RC1-", "RC2-", "RC3-", "fragmentos_bm25", "fragmentos_denso",
                      "id_opaco", "respondible"):
            if marca in sin_resp:
                fugas.append(f"marca {marca} fuera de la respuesta")
    return fugas


def marcas_por_brazo(casos: list[dict]) -> dict:
    """Cuántas respuestas de cada brazo nombran algo de su brazo (no se editan; se declaran)."""
    out = {}
    for b in K.BRAZOS:
        rs = [c["respuesta"] for c in casos if c["brazo"] == b]
        out[b] = {"n_respuestas": len(rs), "con_alguna_marca": sum(any(m.lower() in r.lower() for m in MARCAS_DE_BRAZO) for r in rs),
                  "por_marca": {m: sum(m.lower() in r.lower() for r in rs) for m in MARCAS_DE_BRAZO}}
    return out


def tabla_desanonimizacion(casos: list[dict], etapa: str) -> dict:
    return {"SOLO_MESA": True, "etapa": etapa, "sal_id_opaco": SAL_ID_OPACO, "prefijo": PREFIJO_ID,
            "regla": "id_opaco = prefijo + sha256(sal|pregunta|brazo|rep|sha256(respuesta))[:10]", "n": len(casos),
            "filas": sorted(({"id_opaco": c["id_opaco"], "qid": c["qid"], "brazo": c["brazo"], "rep": c["rep"],
                              "id_sesion": c["id_sesion"], "sha256_respuesta": c["sha256_respuesta"],
                              "respondible_flag": c["respondible_flag"], "n_criterios": len(c["criterios"])} for c in casos),
                            key=lambda f: f["id_opaco"])}


# --------------------------------------------------------------------------- #
# Gasto y corte                                                                #
# --------------------------------------------------------------------------- #
def db_path(rep: int, cache_dir: Path = CACHE_DIR) -> Path:
    return J.db_path_rep(rep, cache_dir, DB_PREFIX)


def gasto_dbs(cache_dir: Path = CACHE_DIR) -> dict:
    """El acumulado del juez de A2.2: una fila por llamada pagada (miss) en sus tres cachés, con los precios de comun_a2_2."""
    tin = tout = filas = 0
    for rep in K.REPS_JUEZ:
        p = db_path(rep, cache_dir)
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
            "usd": round(tin / 1e6 * K.PRECIO_JUEZ_IN + tout / 1e6 * K.PRECIO_JUEZ_OUT, 6)}


def costo_registro(reg: dict) -> float:
    m = reg["meta"]
    return m["input_tokens"] / 1e6 * K.PRECIO_JUEZ_IN + m["output_tokens"] / 1e6 * K.PRECIO_JUEZ_OUT


def leer(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()] if path.exists() else []


def costo_mayor_juzgada(juez_dir: Path) -> float:
    """El costo mayor de una respuesta ya juzgada en cualquier etapa de A2.2 (sus tres repeticiones); 0,0378 si no hay ninguna."""
    por_id: dict[str, dict] = {}
    for etapa in ETAPAS:
        for rep in K.REPS_JUEZ:
            for reg in leer(juez_dir / etapa / f"veredictos_r{rep}.jsonl"):
                por_id.setdefault(f"{etapa}|{reg['id_opaco']}", {})[rep] = costo_registro(reg)
    completas = [sum(v.values()) for v in por_id.values() if len(v) == len(K.REPS_JUEZ)]
    return max(completas) if completas else K.COSTO_RESPUESTA_INICIAL


# --------------------------------------------------------------------------- #
# Corrida                                                                      #
# --------------------------------------------------------------------------- #
def correr(ciegos: list[dict], *, out_dir: Path, juez_dir: Path, cache_dir: Path, client_factory, freno: float, tope: float,
           etapa: str) -> dict:
    """Respuesta por respuesta, en el orden ciego, con sus tres repeticiones seguidas. Devuelve el resumen; levanta FrenoJuez."""
    out_dir.mkdir(parents=True, exist_ok=True)
    clientes = {rep: client_factory(rep, f"a22_juez_{etapa}_r{rep}") for rep in K.REPS_JUEZ}
    hechos = {rep: {r["id_opaco"] for r in leer(out_dir / f"veredictos_r{rep}.jsonl")}
             | {r["id_opaco"] for r in leer(out_dir / f"errores_r{rep}.jsonl")} for rep in K.REPS_JUEZ}
    llamadas = errores = 0
    try:
        for k, c in enumerate(ciegos, 1):
            pend = [rep for rep in K.REPS_JUEZ if c["id_opaco"] not in hechos[rep]]
            if not pend:
                continue
            g = gasto_dbs(cache_dir)["usd"]
            mayor = costo_mayor_juzgada(juez_dir)
            if g + mayor > freno or g + mayor > tope:
                raise FrenoJuez(f"acumulado del juez {g:.4f} + {mayor:.4f} > freno {freno} (tope {tope}) antes de la "
                                f"respuesta {k} de {len(ciegos)}")
            for rep in pend:
                with (out_dir / f"veredictos_r{rep}.jsonl").open("a", encoding="utf-8") as fh, \
                        (out_dir / f"errores_r{rep}.jsonl").open("a", encoding="utf-8") as fe:
                    try:
                        r = J.juzgar(clientes[rep], c["pregunta"], c["respuesta"], c["criterios"])
                    except ValueError as e:
                        fe.write(json.dumps({"id_opaco": c["id_opaco"], "rep": rep, "error": str(e),
                                             "ts": datetime.now().isoformat()}, ensure_ascii=False) + "\n")
                        errores += 1
                        continue
                    fh.write(json.dumps({"id_opaco": c["id_opaco"], "rep": rep,
                                         "clasificacion_respuesta": r["veredicto"]["clasificacion_respuesta"],
                                         "criterios": r["veredicto"]["criterios"], "meta": r["meta"]},
                                        ensure_ascii=False) + "\n")
                    llamadas += 1
            print(f"[{k}/{len(ciegos)}] juzgada; acumulado del juez {gasto_dbs(cache_dir)['usd']:.4f}", flush=True)  # sin veredicto
    finally:
        for cl in clientes.values():
            if hasattr(cl, "close"):
                cl.close()
    return {"llamadas_nuevas": llamadas, "errores_nuevos": errores}


def agregar(out_dir: Path, ciegos: list[dict]) -> dict:
    """Agregados ciegos por id opaco: el veredicto modal de cada criterio (mapping.veredicto_modal) y el de la pregunta
    (mapping.veredicto_pregunta), más la clasificación auxiliar modal. Solo entran las respuestas con sus tres repeticiones."""
    por_rep = {rep: {r["id_opaco"]: r for r in leer(out_dir / f"veredictos_r{rep}.jsonl")} for rep in K.REPS_JUEZ}
    errores = {rep: leer(out_dir / f"errores_r{rep}.jsonl") for rep in K.REPS_JUEZ}
    agregados, incompletas = [], []
    for c in ciegos:
        regs = [por_rep[rep].get(c["id_opaco"]) for rep in K.REPS_JUEZ]
        if any(r is None for r in regs):
            incompletas.append({"id_opaco": c["id_opaco"],
                                "reps_faltantes": [rep for rep, r in zip(K.REPS_JUEZ, regs) if r is None]})
            continue
        modales = [M.veredicto_modal([r["criterios"][i]["veredicto"] for r in regs]) for i in range(len(c["criterios"]))]
        clas = [r["clasificacion_respuesta"] for r in regs]
        v, n = Counter(clas).most_common(1)[0]
        agregados.append({"id_opaco": c["id_opaco"], "n_criterios": len(c["criterios"]),
                          "veredicto_pregunta": M.veredicto_pregunta(modales), "modales": modales,
                          "veredictos_reps": [[r["criterios"][i]["veredicto"] for r in regs] for i in range(len(c["criterios"]))],
                          "clasificacion_respuesta_reps": clas,
                          "clasificacion_respuesta_modal": v if n > len(clas) / 2 else "sin_consenso",
                          "meta_reps": [{k: r["meta"][k] for k in ("modelo", "stop_reason", "input_tokens", "output_tokens",
                                                                    "prompt_sha256", "code_ver")} for r in regs]})
    return {"semilla_orden": K.SEMILLA_ORDEN_JUEZ, "reps": len(K.REPS_JUEZ), "n_casos": len(ciegos),
            "n_agregados": len(agregados), "incompletas": incompletas,
            "errores_por_rep": {rep: len(v) for rep, v in errores.items()}, "agregados": agregados,
            "distribucion": dict(Counter(a["veredicto_pregunta"] for a in agregados))}


def factory_real(cache_dir: Path):
    def f(rep: int, label: str):
        return J.construir_cliente_real(rep, run_label=label, cache_dir=cache_dir, db_prefix=DB_PREFIX)
    return f


# --------------------------------------------------------------------------- #
def etapa(et: str, *, modo: str, preguntas: dict, orden: dict, resultados_dir: Path, juez_dir: Path, cache_dir: Path,
          poblacion: dict | None, freno: float, tope: float, client_factory=None, control_sdk_python: str | None = None) -> dict:
    """Una etapa entera del juez; escribe sus salidas en juez_dir/<etapa>/ y devuelve el resumen."""
    resumen = {"etapa": et, "modo": modo, "inicio": datetime.now().isoformat(timespec="seconds"),
               "instrumento": controlar_instrumento()}
    resumen["sdk"] = control_sdk(control_sdk_python)
    out_dir = juez_dir / et
    resps, faltan = respuestas(et, resultados_dir, orden, poblacion)
    sin_sesion = sum(1 for f in faltan if f["motivo"] == "sin sesión")
    if sin_sesion:
        raise K.FrenoA22(f"faltan {sin_sesion} sesiones de la etapa {et}: el paso anterior no está completo")
    casos = armar_casos(resps, preguntas)
    ciegos = vista_ciega(casos)
    fugas = verificar_ceguera(ciegos)
    if fugas:
        raise K.FrenoA22(f"fuga en los pedidos del juez (nada se llamó): {sorted(set(fugas))}")
    out_dir.mkdir(parents=True, exist_ok=True)
    des = out_dir / "desanonimizacion_SOLO_MESA"
    des.mkdir(parents=True, exist_ok=True)
    for p, obj in ((out_dir / f"orden_juez_{et}.json", {"semilla": K.SEMILLA_ORDEN_JUEZ, "n": len(ciegos),
                                                        "ids_opacos_en_orden": [c["id_opaco"] for c in ciegos]}),
                   (des / f"tabla_id_opaco_{et}_SOLO_MESA.json", tabla_desanonimizacion(casos, et))):
        nuevo = json.dumps(obj, ensure_ascii=False, indent=1) + "\n"
        if p.exists() and p.read_text(encoding="utf-8") != nuevo:
            raise K.FrenoA22(f"{p.name} ya existe y difiere de lo recomputado")
        p.write_text(nuevo, encoding="utf-8")
    resumen["n_respuestas"], resumen["faltantes_del_agente"] = len(ciegos), len(faltan)
    resumen["faltantes_por_motivo"] = dict(Counter(f["motivo"] for f in faltan))
    resumen["marcas_de_brazo_en_las_respuestas"] = marcas_por_brazo(casos)
    del casos
    factory = client_factory or factory_real(cache_dir)
    try:
        resumen["corrida"] = correr(ciegos, out_dir=out_dir, juez_dir=juez_dir, cache_dir=cache_dir, client_factory=factory,
                                    freno=freno, tope=tope, etapa=et)
        resumen["FRENO_JUEZ"] = None
    except FrenoJuez as e:
        resumen["FRENO_JUEZ"] = str(e)
    agg = agregar(out_dir, ciegos)
    (out_dir / f"agregados_{et}_ciego.json").write_text(json.dumps(agg, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (out_dir / f"faltantes_{et}.json").write_text(json.dumps(faltan, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    resumen["gasto_juez_a2_2"] = gasto_dbs(cache_dir)
    resumen["n_agregados"], resumen["n_incompletas"] = agg["n_agregados"], len(agg["incompletas"])
    resumen["distribucion"] = agg["distribucion"]
    resumen["fin"] = datetime.now().isoformat(timespec="seconds")
    (out_dir / f"resumen_juez_{et}.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return resumen


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("etapa", choices=ETAPAS)
    ap.add_argument("--autorizado-tope", type=float, required=True)
    ap.add_argument("--freno", type=float, required=True)
    ap.add_argument("--modo", choices=["real", "seco"], default="real")
    ap.add_argument("--preguntas", type=Path, default=K.EV2_PATH)
    ap.add_argument("--sha-preguntas", default=K.EV2_SHA256)
    ap.add_argument("--orden", type=Path, default=K.ORDEN)
    ap.add_argument("--poblacion", type=Path, default=K.POBLACION)
    ap.add_argument("--resultados", type=Path, default=K.RESULTADOS)
    ap.add_argument("--juez-dir", type=Path, default=K.JUEZ_DIR)
    a = ap.parse_args(argv)
    if a.modo == "real" and (a.autorizado_tope != K.TOPE_JUEZ or a.freno != K.FRENO_JUEZ):
        raise SystemExit("la corrida real del juez usa el tope 25 y el freno 18,75 del pre-registro")
    cache_dir = a.juez_dir / "cache"
    try:
        K.verificar_entradas()
        preguntas = K.cargar_preguntas(a.preguntas, a.sha_preguntas, real=a.modo == "real")
        orden = json.loads(a.orden.read_text(encoding="utf-8"))
        if orden != K.armar_orden(sorted(preguntas)):
            raise K.FrenoA22("orden_corridas_a2_2.json difiere del orden que dan las semillas del pre-registro")
        pob = None
        if a.etapa == "recorridas":
            if not a.poblacion.exists():
                raise K.FrenoA22("falta la población de N = 1: el paso 3 no está completo")
            pob = json.loads(a.poblacion.read_text(encoding="utf-8"))
        factory = None
        if a.modo == "seco":
            import corrida_en_seco_a2_2 as CS           # el cliente falso de la corrida en seco
            factory = CS.factory_falsa(cache_dir)
        res = etapa(a.etapa, modo=a.modo, preguntas=preguntas, orden=orden,
                    resultados_dir=a.resultados / a.etapa, juez_dir=a.juez_dir, cache_dir=cache_dir, poblacion=pob,
                    freno=a.freno, tope=a.autorizado_tope, client_factory=factory)
    except K.FrenoA22 as e:
        print("FRENO DE PRECONDICIÓN DEL JUEZ:", e)
        return 5
    g = res["gasto_juez_a2_2"]
    # Sin ningún veredicto ni su distribución: la autora lee a ciegas las 20 de verificación (Q8, `:61-63`; A2.1, `:245-246`).
    print(f"juez {a.etapa}: {res['n_respuestas']} respuestas ({res['faltantes_del_agente']} faltantes del agente); "
          f"{res['n_agregados']} agregadas, {res['n_incompletas']} incompletas; "
          f"acumulado del juez USD {g['usd']:.4f} ({g['filas']} llamadas pagadas)")
    if res["FRENO_JUEZ"]:
        print("FRENO DEL JUEZ:", res["FRENO_JUEZ"])
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
