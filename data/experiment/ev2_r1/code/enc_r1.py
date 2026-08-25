"""
enc_r1.py — Encadenamiento §7 de U-B1.8 sobre KG-Reextraído-r1 (protocolo
docs/protocolo_corrida_ev2.md §3; pre-registro ev2_r1/preregistro_ev2_r1.md §4;
autorización de la mesa: tope propio USD 5,50, población 24 pares).

Dos etapas, ambas gateadas y retomables:
  --etapa agente : re-corridas N=3 del agente sobre los pares disparados —
      23 "parcial" de la corrida base de r1 (trigger mecánico único) + 1 de
      auditoría simétrica (ceil(10 % de 5 correctos) = 1, mínimo 1, semilla
      `auditoria-ev2-r1` sobre ids ordenados, generador nuevo — regla de
      9044a04). Reutiliza runner_ev2.correr_grafo sin editar (labels
      ev2_r1_enc_r{1,2,3}, db propia por rep, 0 hits exigido: compartir db
      replayaría en vez de re-muestrear). Cada traza se anota con
      meta.u_b18_enc (precedente meta.encadenamiento de 9044a04).
  --etapa juez : evaluación CIEGA de las 72 respuestas nuevas con el juez v1
      congelado vía pipeline_fidelidad sin editar. Ids opacos EV2E1- (salt
      juez-ev2-r1-enc, REP EN LA CLAVE: dos re-corridas de un par pueden dar
      texto idéntico), orden ciego `juez-ev2-r1-enc`, dbs/labels
      ev2_r1_enc_juez_r{1,2,3}. Después: agregación por PAR con agregar_par
      IMPORTADO de ev2_encadenamiento/code/agregacion_enc.py (mayoría; empate
      triple → parcial; regla de votos ADJ por invariancia) + flip de la
      auditoría → reporte/veredictos_finales_r1.json + reporte_s7_r1.md.

La población se deriva de juez_out/ (base de r1) y se persiste en
poblacion/poblacion_s7_r1.json; cargarla re-deriva y exige igualdad.

Uso:
  .venv/bin/python -B enc_r1.py --etapa poblacion                 (offline, $0)
  .venv/bin/python -B enc_r1.py --etapa agente --autorizado-fase-b --tope-agente <USD>
  .venv/bin/python -B enc_r1.py --etapa juez   --autorizado-fase-b \
      --precio-in <USD/MTok> --precio-out <USD/MTok> --tope-juez <USD>
  --solo-agregados (etapa juez) recomputa agregados y reporte sin API.
"""

from __future__ import annotations

import argparse
import json
import math
import random
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402  (registra r1 al importarse)
import runner_ev2 as rv                    # noqa: E402  (runner base, sin editar)
import pipeline_fidelidad as pf            # noqa: E402  (pipeline ciego, sin editar)
import agregacion_enc as ag                # noqa: E402  (regla por par, sellada 9044a04)
import juez_r1 as jr                       # noqa: E402  (marcadores + patrón de tablas)
from comun_r1 import cf, juez              # noqa: E402

POBLACION_DIR = cr.UNIDAD_DIR / "poblacion"
JUEZ_OUT_ENC = cr.UNIDAD_DIR / "juez_out_enc"        # salidas CIEGAS del juez §7
REPORTE_DIR = cr.UNIDAD_DIR / "reporte"

FRACCION_AUDITORIA = 0.10
MINIMO_AUDITORIA = 1
VEREDICTO_DISPARADOR = "parcial"
ESPERADO = {"parciales": 23, "correctos": 5, "auditoria": 1, "pares": 24}


# --------------------------------------------------------------------------- #
# Población disparada                                                          #
# --------------------------------------------------------------------------- #
def veredictos_base_r1() -> dict[str, dict]:
    """{id_pregunta: {veredicto, id_opaco_base, sha256_respuesta_base}} desde
    los agregados ciegos de la base de r1 × su tabla SOLO_MESA."""
    agg = json.loads((cr.JUEZ_OUT_DIR / "veredictos_agregados_ciego.json")
                     .read_text(encoding="utf-8"))
    tab = json.loads((cr.DESANON_DIR / "tabla_id_opaco_r1_SOLO_MESA.json")
                     .read_text(encoding="utf-8"))
    if agg["n_agregados"] != 40 or agg["incompletas"] or tab["n"] != 40:
        raise ValueError("base de r1 inesperada (esperaba 40 agregados, 0 incompletas)")
    fila = {f["id_opaco"]: f for f in tab["filas"]}
    out = {}
    for a in agg["agregados"]:
        f = fila[a["id_opaco"]]
        out[f["id_pregunta"]] = {"veredicto": a["veredicto_pregunta"],
                                 "id_opaco_base": a["id_opaco"],
                                 "sha256_respuesta_base": f["sha256_respuesta"]}
    if len(out) != 40:
        raise ValueError("preguntas repetidas en la base")
    return out


def derivar_poblacion() -> dict:
    vb = veredictos_base_r1()
    dist = dict(Counter(v["veredicto"] for v in vb.values()))
    parciales = sorted(q for q, v in vb.items() if v["veredicto"] == VEREDICTO_DISPARADOR)
    correctos = sorted(q for q, v in vb.items() if v["veredicto"] == "correcto")
    k = max(math.ceil(FRACCION_AUDITORIA * len(correctos)), MINIMO_AUDITORIA) \
        if correctos else 0
    aud = sorted(random.Random(cr.SEMILLA_AUDITORIA).sample(correctos, k))
    pares = [{"id_pregunta": q, "tipo": "parcial_disparado", **vb[q]} for q in parciales] \
        + [{"id_pregunta": q, "tipo": "auditoria_correcto", **vb[q]} for q in aud]
    pares.sort(key=lambda p: p["id_pregunta"])
    ok = (len(parciales) == ESPERADO["parciales"] and len(correctos) == ESPERADO["correctos"]
          and len(aud) == ESPERADO["auditoria"] and len(pares) == ESPERADO["pares"])
    if not ok:
        raise ValueError(f"población fuera de lo autorizado: parciales {len(parciales)}, "
                         f"correctos {len(correctos)}, auditoría {len(aud)}")
    return {
        "fuente_base": {
            "agregados": cr.rel_repo(cr.JUEZ_OUT_DIR / "veredictos_agregados_ciego.json"),
            "sha256_agregados": cr.sha256_path(cr.JUEZ_OUT_DIR / "veredictos_agregados_ciego.json"),
            "tabla": cr.rel_repo(cr.DESANON_DIR / "tabla_id_opaco_r1_SOLO_MESA.json"),
            "sha256_tabla": cr.sha256_path(cr.DESANON_DIR / "tabla_id_opaco_r1_SOLO_MESA.json")},
        "regla": {"disparador": f"veredicto base == '{VEREDICTO_DISPARADOR}' (protocolo §3)",
                  "auditoria": (f"{int(FRACCION_AUDITORIA*100)} % de los 'correcto', "
                                f"random.Random('{cr.SEMILLA_AUDITORIA}').sample sobre ids "
                                f"ordenados, tamaño max(ceil, {MINIMO_AUDITORIA})"),
                  "reps_agente": cr.REPS_AGENTE_ENC, "reps_juez": cr.REPS_JUEZ},
        "distribucion_base": dist,
        "ids_correctos_ordenados": correctos,
        "ids_auditoria": aud,
        "n_pares": len(pares), "n_corridas_agente": len(pares) * cr.REPS_AGENTE_ENC,
        "n_llamadas_juez": len(pares) * cr.REPS_AGENTE_ENC * cr.REPS_JUEZ,
        "pares": pares,
    }


def persistir_poblacion() -> dict:
    POBLACION_DIR.mkdir(parents=True, exist_ok=True)
    p = POBLACION_DIR / "poblacion_s7_r1.json"
    pob = derivar_poblacion()
    nuevo = json.dumps(pob, ensure_ascii=False, indent=2)
    if p.exists():
        prev = json.loads(p.read_text(encoding="utf-8"))
        if prev["pares"] != pob["pares"]:
            raise RuntimeError(f"{p} difiere de la derivación desde la base")
        return prev
    p.write_text(nuevo, encoding="utf-8")
    return pob


def casos_agente(pob: dict) -> list[dict]:
    """Los 24 casos en el orden de orden_agente_r1.json filtrado (el orden
    relativo de la corrida base de r1 se conserva; patrón casos_agente de 9044a04)."""
    disparados = {p["id_pregunta"] for p in pob["pares"]}
    out = [c for c in cr.casos_fidelidad_r1() if c["caso_id"] in disparados]
    if len(out) != len(disparados):
        raise ValueError(f"{len(out)} casos en orden vs {len(disparados)} pares")
    return out


# --------------------------------------------------------------------------- #
# Etapa AGENTE                                                                 #
# --------------------------------------------------------------------------- #
def db_enc(rep: int) -> Path:
    return cr.CACHE_DIR / f"{cr.label_enc(rep)}.db"


def anotar_trazas_enc(pob: dict, rep: int) -> int:
    por_par = {p["id_pregunta"]: p for p in pob["pares"]}
    outdir = cr.TRAZAS_DIR / cr.label_enc(rep)
    n = 0
    for f in sorted(outdir.glob("EV2F-*.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        if "u_b18_enc" in t["meta"]:
            continue
        p = por_par[t["meta"]["caso_id"]]
        t["meta"]["u_b18_enc"] = {
            "unidad": "ev2_r1 (U-B1.8) §7", "rep": rep,
            "reps_previstas": cr.REPS_AGENTE_ENC, "label": cr.label_enc(rep),
            "tipo": p["tipo"], "veredicto_base": p["veredicto"],
            "id_opaco_base": p["id_opaco_base"],
            "sha256_respuesta_base": p["sha256_respuesta_base"],
            "semilla_orden_real": cr.SEMILLA_ORDEN_R1,
            "regla": ("protocolo §3: N=3 disparada por veredicto base 'parcial'; "
                      "auditoria_correcto = ceil(10 %) con semilla auditoria-ev2-r1; "
                      "meta.semilla_orden es campo heredado del runner base"),
        }
        f.write_text(json.dumps(t, ensure_ascii=False, indent=2), encoding="utf-8")
        n += 1
    return n


def etapa_agente(tope_usd: float) -> int:
    sellos = cr.verificar_sellos(verbose=True)
    cr.escribir_sellos("sellos_inicio_s7_agente.txt")
    pob = persistir_poblacion()
    casos = casos_agente(pob)
    total = len(casos) * cr.REPS_AGENTE_ENC
    estado = {"gastado": 0.0, "corridos": 0, "total": total, "tope_usd": tope_usd}
    real = None
    frenado = False
    for rep in range(1, cr.REPS_AGENTE_ENC + 1):
        label = cr.label_enc(rep)
        outdir = cr.TRAZAS_DIR / label
        outdir.mkdir(parents=True, exist_ok=True)
        pend = [c for c in casos
                if not (outdir / f"{rv._sanitizar(c['caso_id'])}.json").exists()]
        print(f"== §7 r1 rep {rep} ({label}): {len(casos)} casos, "
              f"{len(casos) - len(pend)} ya persistidos, {len(pend)} pendientes ==",
              flush=True)
        if pend:
            if real is None:
                real = rv._real_client()
            rv.correr_grafo(cr.R1_KEY, client_real=real, db_path=db_enc(rep),
                            label=label, casos=pend, outdir=outdir,
                            estado_gasto=estado)
        anotar_trazas_enc(pob, rep)
        if estado["corridos"] >= 3 and \
                estado["gastado"] / estado["corridos"] * estado["total"] > tope_usd:
            print("Etapa §7 agente detenida por freno de proyección.", flush=True)
            frenado = True
            break
    # índice + hits por db (0 exigido)
    idx = {"n_previstas": total, "reps": {}, "hits": {}}
    import sqlite3
    for rep in range(1, cr.REPS_AGENTE_ENC + 1):
        outdir = cr.TRAZAS_DIR / cr.label_enc(rep)
        n = len(list(outdir.glob("EV2F-*.json"))) if outdir.exists() else 0
        idx["reps"][rep] = n
        p = db_enc(rep)
        if p.exists():
            conn = sqlite3.connect(str(p))
            idx["hits"][rep] = sum(int(v or 0) for _, v in conn.execute(
                "SELECT run_label, SUM(hit) FROM access_log GROUP BY run_label"))
            conn.close()
    REPORTE_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTE_DIR / "resumen_s7_agente_r1.json").write_text(json.dumps(
        {"ts": datetime.now().isoformat(timespec="seconds"), "tope_usd": tope_usd,
         "estado_gasto": estado, "frenado": frenado, "indice": idx},
        ensure_ascii=False, indent=2), encoding="utf-8")
    cr.escribir_sellos("sellos_fin_s7_agente.txt")
    if cr.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    print(f"persistidas por rep: {idx['reps']} | hits por db: {idx['hits']} | "
          f"gasto ${estado['gastado']:.4f}" + (" | FRENADO" if frenado else ""),
          flush=True)
    return 1 if frenado else 0


# --------------------------------------------------------------------------- #
# Etapa JUEZ (§7)                                                              #
# --------------------------------------------------------------------------- #
def cargar_respuestas_enc(pob: dict) -> tuple[list[dict], list[dict]]:
    xs, faltantes = [], []
    for p in pob["pares"]:
        for rep in range(1, cr.REPS_AGENTE_ENC + 1):
            lab = cr.label_enc(rep)
            f = cr.TRAZAS_DIR / lab / f"{p['id_pregunta']}.json"
            if not f.exists():
                faltantes.append({"id_pregunta": p["id_pregunta"], "rep": rep,
                                  "motivo": "traza inexistente"})
                continue
            t = json.loads(f.read_text(encoding="utf-8"))
            m, tr = t["meta"], t["trace"]
            fj = tr.get("final_json") or {}
            if m["label"] != lab or m["grafo"] != cr.R1_KEY \
                    or m["caso_id"] != p["id_pregunta"] or tr["qid"] != p["id_pregunta"]:
                raise ValueError(f"{f}: meta inconsistente")
            if not tr.get("parse_ok") or not isinstance(fj.get("respuesta"), str) \
                    or not fj["respuesta"].strip():
                faltantes.append({"id_pregunta": p["id_pregunta"], "rep": rep,
                                  "motivo": f"sin respuesta parseada (error={tr.get('error')})"})
                continue
            xs.append({"id_pregunta": p["id_pregunta"], "rep": rep, "label": lab,
                       "tipo": p["tipo"], "id_opaco_base": p["id_opaco_base"],
                       "veredicto_base": p["veredicto"],
                       "respuesta": fj["respuesta"],
                       "respondible_flag": fj.get("respondible"),
                       "pregunta_traza": t["pregunta"]})
    return xs, faltantes


def armar_casos_enc(respuestas: list[dict], gold: dict) -> list[dict]:
    xs = []
    for r in respuestas:
        if r["pregunta_traza"].strip() != gold[r["id_pregunta"]]["pregunta"].strip():
            raise ValueError(f"{r['id_pregunta']} r{r['rep']}: pregunta de traza ≠ gold")
        sha = cr.sha256_texto(r["respuesta"])
        xs.append({**r, "sha256_respuesta": sha,
                   "id_opaco": cr.id_opaco_enc(r["id_pregunta"], r["rep"], sha),
                   "pregunta": gold[r["id_pregunta"]]["pregunta"],
                   "criterios": gold[r["id_pregunta"]]["criterios"]})
    xs.sort(key=lambda c: (c["id_pregunta"], c["sha256_respuesta"], c["rep"]))
    ids = [c["id_opaco"] for c in xs]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids opacos")
    dup = Counter((c["id_pregunta"], c["sha256_respuesta"]) for c in xs)
    duplicados = sorted([q, s, n] for (q, s), n in dup.items() if n > 1)
    random.Random(cr.SEMILLA_ORDEN_JUEZ_ENC).shuffle(xs)
    for c in xs:
        c["duplicados_texto"] = duplicados
    return xs


def persistir_orden_y_tabla_enc(casos: list[dict]) -> tuple[Path, Path, Path]:
    cr.ORDEN_DIR.mkdir(parents=True, exist_ok=True)
    cr.DESANON_DIR.mkdir(parents=True, exist_ok=True)
    p_ord = cr.ORDEN_DIR / "orden_juez_s7_r1_ciego.json"
    p_tab = cr.DESANON_DIR / "tabla_id_opaco_s7_r1_SOLO_MESA.json"
    p_vin = cr.ORDEN_DIR / "vinculo_pares_s7_r1_ciego.json"
    orden = {"semilla": cr.SEMILLA_ORDEN_JUEZ_ENC,
             "regla": ("sorted por (id_pregunta, sha256 respuesta, rep) → "
                       "random.Random(semilla).shuffle"),
             "n": len(casos),
             "n_textos_duplicados_por_pregunta": len(casos[0]["duplicados_texto"]) if casos else 0,
             "ids_opacos_en_orden": [c["id_opaco"] for c in casos]}
    tabla = {"SOLO_MESA": True, "salt_id_opaco": cr.SAL_ID_ENC,
             "prefijo": cr.PREFIJO_ENC,
             "regla": ("id_opaco = prefijo + sha256(salt|id_pregunta|r1|rep|"
                       "sha256(respuesta))[:10]"),
             "n": len(casos),
             "filas": sorted(({"id_opaco": c["id_opaco"], "id_pregunta": c["id_pregunta"],
                               "grafo": cr.R1_KEY, "rep": c["rep"], "label": c["label"],
                               "tipo": c["tipo"], "id_opaco_base": c["id_opaco_base"],
                               "veredicto_base": c["veredicto_base"],
                               "sha256_respuesta": c["sha256_respuesta"],
                               "respondible_flag": c["respondible_flag"],
                               "n_criterios": len(c["criterios"])} for c in casos),
                             key=lambda f: f["id_opaco"])}
    por_par: dict[str, dict] = {}
    for c in casos:
        d = por_par.setdefault(c["id_opaco_base"], {"id_opaco_base": c["id_opaco_base"],
                                                    "tipo": c["tipo"], "reps": {}})
        d["reps"][str(c["rep"])] = c["id_opaco"]
    vinculo = {"n_pares": len(por_par), "pares": [por_par[k] for k in sorted(por_par)]}
    for p, obj in ((p_ord, orden), (p_tab, tabla), (p_vin, vinculo)):
        nuevo = json.dumps(obj, ensure_ascii=False, indent=2)
        if p.exists():
            if p.read_text(encoding="utf-8") != nuevo:
                raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
        else:
            p.write_text(nuevo, encoding="utf-8")
    return p_ord, p_tab, p_vin


def verificar_ceguera_enc(ciegos: list[dict]) -> list[tuple[str, str]]:
    extra = ["EV2R1-", "EV2E1-", "id_opaco", "respondible", "ev2_r1_enc",
             "veredicto_base", "parcial_disparado", "auditoria_correcto"]
    fugas = []
    for c in ciegos:
        if set(c) != {"id_opaco", "pregunta", "respuesta", "criterios"}:
            fugas.append((c.get("id_opaco"), "vista no ciega"))
        kw = juez.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        if set(kw) != {"model", "max_tokens", "temperature", "system", "messages"} \
                or kw["system"] != juez.PROMPT_JUEZ:
            fugas.append((c["id_opaco"], "estructura del request"))
        u = kw["messages"][0]["content"]
        for m in jr.buscar_marcadores(u, extra):
            fugas.append((c["id_opaco"], m))
    return fugas


def factory_juez_enc(rep: int, _label_ignorado: str):
    return juez.construir_cliente_real(rep, run_label=cr.label_juez_enc(rep),
                                       cache_dir=cr.CACHE_DIR,
                                       db_prefix=cr.DB_PREFIX_JUEZ_ENC)


def agregar_pares(agg: dict, vinculo: dict) -> dict:
    """Agregación por PAR con agregar_par/detalle_par/flip_descendente de
    9044a04 (importados)."""
    por_id = {a["id_opaco"]: a for a in agg["agregados"]}
    incompletas = {x["id_opaco"] for x in agg["incompletas"]}
    pares, incompletos = [], []
    for v in vinculo["pares"]:
        ids = [v["reps"].get(str(r)) for r in range(1, cr.REPS_AGENTE_ENC + 1)]
        faltan = [r for r, i in zip(range(1, cr.REPS_AGENTE_ENC + 1), ids)
                  if i is None or i in incompletas or i not in por_id]
        if faltan:
            incompletos.append({"id_opaco_base": v["id_opaco_base"], "tipo": v["tipo"],
                                "reps_sin_veredicto": faltan})
            continue
        votos = [por_id[i]["veredicto_pregunta"] for i in ids]
        det = ag.detalle_par(votos)
        base = "correcto" if v["tipo"] == "auditoria_correcto" else VEREDICTO_DISPARADOR
        pares.append({"id_opaco_base": v["id_opaco_base"], "tipo": v["tipo"],
                      "veredicto_base": base, "ids_reps": ids, "veredictos_reps": votos,
                      "distribucion": det["distribucion"], "final": det["final"],
                      "via": det["via"], "unanime": det["unanime"],
                      "flip_descendente": ag.flip_descendente(base, det["final"]),
                      "clasificacion_auxiliar_reps": [por_id[i]["clasificacion_respuesta_modal"]
                                                      for i in ids]})
    disp = [p for p in pares if p["tipo"] == "parcial_disparado"]
    aud = [p for p in pares if p["tipo"] == "auditoria_correcto"]
    return {"regla": ag.__doc__.strip().splitlines()[0],
            "n_pares_vinculo": vinculo["n_pares"], "n_pares_agregados": len(pares),
            "n_pares_incompletos": len(incompletos), "pares_incompletos": incompletos,
            "distribucion_final_disparados": dict(Counter(p["final"] for p in disp)),
            "distribucion_final_auditoria": dict(Counter(p["final"] for p in aud)),
            "vias_disparados": dict(Counter(p["via"] for p in disp)),
            "unanimes_disparados": sum(p["unanime"] for p in disp),
            "veredictos_individuales_disparados": dict(Counter(
                v for p in disp for v in p["veredictos_reps"])),
            "auditoria": {"n_pares": len(aud),
                          "flips": sum(p["flip_descendente"] == "flip" for p in aud),
                          "sin_flip": sum(p["flip_descendente"] == "sin_flip" for p in aud),
                          "pendientes": sum(p["flip_descendente"] == "pendiente" for p in aud)},
            "pares": sorted(pares, key=lambda p: p["id_opaco_base"])}


def etapa_juez(args) -> int:
    sellos = cr.verificar_sellos()
    pob = persistir_poblacion()
    gold = cf.cargar_gold()
    respuestas, faltantes = cargar_respuestas_enc(pob)
    casos = armar_casos_enc(respuestas, gold)
    p_ord, p_tab, p_vin = persistir_orden_y_tabla_enc(casos)
    vinculo = json.loads(p_vin.read_text(encoding="utf-8"))
    dups = casos[0]["duplicados_texto"] if casos else []
    censo = {"n_respuestas": len(casos), "por_grafo": {cr.R1_KEY: len(casos)},
             "n_previstas": pob["n_corridas_agente"],
             "preguntas_distintas": len({c["id_pregunta"] for c in casos}),
             "respuestas_por_pregunta": dict(Counter(Counter(
                 c["id_pregunta"] for c in casos).values())),
             "n_textos_duplicados": len(dups),
             "hits_intra_db_esperados_por_duplicados":
                 cr.REPS_JUEZ * sum(n - 1 for _, _, n in dups),
             "n_criterios_gold": sum(len(g["criterios"]) for g in gold.values()),
             "respondible_flag": dict(Counter(str(c["respondible_flag"]) for c in casos))}
    ciegos = cf.vista_ciega(casos)
    del casos, respuestas
    fugas = verificar_ceguera_enc(ciegos)
    if fugas:
        raise RuntimeError(f"FUGA en requests del juez §7 (nada se llamó): {fugas[:5]}")
    total = len(ciegos) * cr.REPS_JUEZ
    resumen_path = JUEZ_OUT_ENC / "resumen_corrida_juez_s7_r1.json"

    if not args.solo_agregados:
        if not (args.autorizado_fase_b and args.precio_in is not None
                and args.precio_out is not None and args.tope_juez is not None):
            print("ABORTADO: exige --autorizado-fase-b --precio-in --precio-out "
                  "--tope-juez. Nada se llamó.")
            return 2
        cr.escribir_sellos("sellos_inicio_s7_juez.txt")
        JUEZ_OUT_ENC.mkdir(parents=True, exist_ok=True)
        # Pendientes REALES (ids ciegos aún sin veredicto ni error, por rep).
        # FrenoProyeccion del pipeline congelado proyecta como pagables los
        # ya-persistidos de reps futuras (restantes = total - hechas): en una
        # RETOMA sobreestima y frena de más. Freno de retoma declarado: si hay
        # avance previo, el chequeo contra el tope se hace ACÁ, antes de llamar,
        # con el promedio observado en las dbs; recién entonces se corre con el
        # write-through (que no re-paga nada). En corrida limpia, el freno del
        # pipeline queda activo tal cual.
        ids_ciegos = {c["id_opaco"] for c in ciegos}
        n_pend = sum(len(ids_ciegos - pf._ids_en(JUEZ_OUT_ENC / f"veredictos_r{r}.jsonl")
                         - pf._ids_en(JUEZ_OUT_ENC / f"errores_r{r}.jsonl"))
                     for r in range(1, cr.REPS_JUEZ + 1))
        g0 = pf.gasto_dbs(cr.CACHE_DIR, cr.REPS_JUEZ, args.precio_in,
                          args.precio_out, cr.DB_PREFIX_JUEZ_ENC)
        if n_pend < total and g0["filas"] > 0:
            prom = g0["usd"] / g0["filas"]
            proy = g0["usd"] + n_pend * prom
            print(f"RETOMA: {n_pend} llamadas pendientes reales de {total}; gasto "
                  f"{g0['usd']} + proyección {round(proy, 4)} vs tope {args.tope_juez}",
                  flush=True)
            if proy > args.tope_juez:
                print(f"FRENO DE RETOMA: proyección {round(proy, 4)} > tope. Nada se llamó.")
                return 1
            freno = None
        else:
            freno = pf.FrenoProyeccion(cr.CACHE_DIR, cr.REPS_JUEZ, args.precio_in,
                                       args.precio_out, args.tope_juez, total,
                                       db_prefix=cr.DB_PREFIX_JUEZ_ENC)
        print(f"{len(ciegos)} respuestas × {cr.REPS_JUEZ} reps = {total} llamadas | "
              f"tope USD {args.tope_juez}", flush=True)
        frenado = pf.correr(ciegos, reps=cr.REPS_JUEZ, out_dir=JUEZ_OUT_ENC,
                            client_factory=factory_juez_enc, freno=freno)
        gasto = pf.gasto_dbs(cr.CACHE_DIR, cr.REPS_JUEZ, args.precio_in,
                             args.precio_out, cr.DB_PREFIX_JUEZ_ENC)
        if freno is None and gasto["usd"] > args.tope_juez:
            raise RuntimeError(f"gasto de retoma {gasto['usd']} superó el tope "
                               f"{args.tope_juez}: reportar antes de continuar")
        por_rep, errores = pf.cargar_veredictos(JUEZ_OUT_ENC, cr.REPS_JUEZ)
        resumen = {"llamadas_totales": total, "gasto_real": gasto,
                   "precios": {"in": args.precio_in, "out": args.precio_out},
                   "tope": args.tope_juez, "frenado_por_proyeccion": frenado,
                   "ts": datetime.now().isoformat(),
                   "llamadas_hechas": sum(len(v) for v in por_rep.values())
                   + sum(len(v) for v in errores.values())}
        resumen_path.write_text(json.dumps(resumen, ensure_ascii=False, indent=2),
                                encoding="utf-8")
        if frenado:
            print(f"FRENO POR PROYECCIÓN: {frenado}")
            return 1
    else:
        resumen = json.loads(resumen_path.read_text(encoding="utf-8")) \
            if resumen_path.exists() else None
        gasto = None
        if resumen:
            gasto = pf.gasto_dbs(cr.CACHE_DIR, cr.REPS_JUEZ, resumen["precios"]["in"],
                                 resumen["precios"]["out"], cr.DB_PREFIX_JUEZ_ENC)

    agg = pf.agregar(JUEZ_OUT_ENC, cr.REPS_JUEZ, ciegos)
    ver = pf.verificar_cross_hits(
        [cr.CACHE_DIR / f"{cr.DB_PREFIX_JUEZ_ENC}_r{r}.db" for r in (1, 2, 3)])
    agg["verificacion_cross_hits"] = ver
    agg["sellos"] = sellos
    dist = pf.distribucion(agg)
    agg["distribucion"] = dist
    JUEZ_OUT_ENC.mkdir(parents=True, exist_ok=True)
    (JUEZ_OUT_ENC / "veredictos_agregados_ciego.json").write_text(
        json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    pares_agg = agregar_pares(agg, vinculo)
    REPORTE_DIR.mkdir(parents=True, exist_ok=True)
    (REPORTE_DIR / "veredictos_finales_s7_r1.json").write_text(json.dumps(
        {"generado": datetime.now().isoformat(timespec="seconds"), "sellos": sellos,
         "censo": censo, "faltantes_agente": faltantes,
         "verificacion_cross_hits_juez": ver, "gasto_juez": gasto,
         "distribucion_por_respuesta": dist["veredicto_pregunta"], **pares_agg},
        ensure_ascii=False, indent=2), encoding="utf-8")
    L = [f"# §7 de r1 — reporte por par (re-corridas N=3 × juez v1 N=3)", "",
         f"- respuestas nuevas juzgadas: {censo['n_respuestas']} / {censo['n_previstas']} "
         f"(faltantes: {len(faltantes)} {faltantes or ''})",
         f"- textos duplicados por pregunta: {censo['n_textos_duplicados']} → hits "
         f"intra-db esperados {censo['hits_intra_db_esperados_por_duplicados']}; "
         f"observados {ver['hits_total']}",
         f"- cross-hits juez: {ver['cross_hits']} | errores {agg['errores_por_rep']} | "
         f"incompletas {len(agg['incompletas'])}",
         f"- por respuesta (mapping §2): {dist['veredicto_pregunta']}",
         f"- **disparados (base parcial) — final: {pares_agg['distribucion_final_disparados']}**; "
         f"vías {pares_agg['vias_disparados']}; unánimes {pares_agg['unanimes_disparados']}",
         f"- **auditoría (base correcto) — final: {pares_agg['distribucion_final_auditoria']}**; "
         f"flips {pares_agg['auditoria']['flips']}/{pares_agg['auditoria']['n_pares']}",
         f"- pares incompletos: {pares_agg['n_pares_incompletos']}",
         "", "| id_opaco_base | tipo | votos r1/r2/r3 | final | vía | flip |",
         "|---|---|---|---|---|---|"]
    for x in pares_agg["pares"]:
        L.append(f"| {x['id_opaco_base']} | {x['tipo']} | "
                 f"{'/'.join(v[:4] if v != 'requiere_adjudicacion' else 'ADJ' for v in x['veredictos_reps'])} "
                 f"| {x['final']} | {x['via']} | {x['flip_descendente'] or '-'} |")
    (REPORTE_DIR / "reporte_s7_r1.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    if not args.solo_agregados:
        cr.escribir_sellos("sellos_fin_s7_juez.txt")
    if cr.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    print(f"por respuesta: {dist['veredicto_pregunta']} | incompletas {len(agg['incompletas'])}")
    print(f"por par — disparados: {pares_agg['distribucion_final_disparados']} | "
          f"auditoría: {pares_agg['distribucion_final_auditoria']} "
          f"flips {pares_agg['auditoria']['flips']}/{pares_agg['auditoria']['n_pares']}")
    print(f"cross-hits: {ver['cross_hits']} | hits total {ver['hits_total']} "
          f"(esperados por duplicados {censo['hits_intra_db_esperados_por_duplicados']})")
    if gasto:
        print(f"gasto juez §7: USD {gasto['usd']} ({gasto['filas']} filas)")
    print(f"→ {REPORTE_DIR / 'reporte_s7_r1.md'}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Encadenamiento §7 de U-B1.8 (fase B)")
    ap.add_argument("--etapa", required=True, choices=["poblacion", "agente", "juez"])
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--tope-agente", type=float, default=None)
    ap.add_argument("--precio-in", type=float, default=None)
    ap.add_argument("--precio-out", type=float, default=None)
    ap.add_argument("--tope-juez", type=float, default=None)
    ap.add_argument("--solo-agregados", action="store_true")
    args = ap.parse_args()

    if args.etapa == "poblacion":
        pob = persistir_poblacion()
        print(json.dumps({k: v for k, v in pob.items() if k != "pares"},
                         ensure_ascii=False, indent=2))
        return 0
    if args.etapa == "agente":
        if not args.autorizado_fase_b or args.tope_agente is None:
            print("ABORTADO: exige --autorizado-fase-b y --tope-agente. Nada se llamó.")
            return 2
        return etapa_agente(args.tope_agente)
    return etapa_juez(args)


if __name__ == "__main__":
    raise SystemExit(main())
