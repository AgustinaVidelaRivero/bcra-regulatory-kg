"""
enc_tanda0.py — U-TANDA0-2A E5 (instrumento 10, parte §7): re-corridas de
encadenamiento del §7 del pre-registro de r1 para una celda de la tanda 0
(C2-C5), con su juez. Protocolo de C1 (docs/protocolo_corrida_ev2.md §3;
patrón exacto de ev2_r1/code/enc_r1.py):

  población   pares disparados = preguntas con veredicto base «parcial»
              (trigger mecánico único) + auditoría simétrica: ceil(10 % de los
              «correcto»), mínimo 1, random.Random(semilla de auditoría de la
              celda).sample sobre ids ordenados. Se DERIVA de la base de la
              celda: enc_r1 fija los conteos esperados de r1 (23 / 5 / 1 / 24);
              acá no hay conteos esperados, se persiste lo derivado y cargarlo
              re-deriva y exige igualdad.
  agente      N=3 re-corridas del agente sobre los pares, con el BACKEND DE LA
              CELDA: memoria (C3, C5) vía runner_ev2.correr_grafo, Neo4j fulltext
              (C2, C4) vía runner_ev2_neo4j.correr_grafo (una celda no mezcla
              backends entre base y §7). Labels <label>_enc_r{1,2,3}, db propia
              por rep (0 hits exigidos: compartir db replayaría en vez de
              re-muestrear); orden = el de la base filtrado. Cada traza se anota
              con meta.tanda0_enc.
  juez        evaluación CIEGA de las respuestas nuevas con el juez v1 congelado
              vía pipeline_fidelidad; ids opacos con prefijo y sal §7 de la celda
              (REP EN LA CLAVE), orden ciego con la semilla §7 de la celda, dbs
              <label>_enc_juez_r{1,2,3}. Agregación por PAR con
              enc_r1.agregar_pares IMPORTADO (que a su vez usa agregar_par /
              detalle_par / flip_descendente de agregacion_enc, 9044a04).

Reutiliza por import, sin editar: enc_r1 (agregar_pares, VEREDICTO_DISPARADOR,
FRACCION_AUDITORIA, MINIMO_AUDITORIA), agregacion_enc, pipeline_fidelidad,
juez_tanda0 (ceguera y cliente del juez parametrizados) y celdas_tanda0.

Salidas: juez_out/<celda>/{poblacion,enc,orden,desanonimizacion_SOLO_MESA,reporte}/
y trazas/<label>_enc_r{rep}/; dbs en cache/ (gitignoradas).

Uso:
  .venv/bin/python -B enc_tanda0.py --celda C2 --etapa poblacion                 ($0)
  .venv/bin/python -B enc_tanda0.py --celda C2 --etapa agente --autorizado-fase-b --tope-agente <USD>
  .venv/bin/python -B enc_tanda0.py --celda C2 --etapa juez --autorizado-fase-b \
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

import celdas_tanda0 as ce0                 # noqa: E402
import juez_tanda0 as jt                    # noqa: E402
import enc_r1 as er                         # noqa: E402  (agregar_pares y constantes, sin editar)
import pipeline_fidelidad as pf             # noqa: E402
import runner_ev2 as rv                     # noqa: E402
from comun_r1 import cf, juez               # noqa: E402

ARCHIVO_POBLACION = "poblacion_s7.json"


# --------------------------------------------------------------------------- #
# Población                                                                    #
# --------------------------------------------------------------------------- #
def veredictos_base(celda: ce0.Celda, rutas: ce0.Rutas) -> dict[str, dict]:
    """{id_pregunta: {veredicto, id_opaco_base, sha256_respuesta_base}} desde los
    agregados ciegos de la base de la celda × su tabla SOLO_MESA."""
    agg = json.loads((rutas.sub(celda, "base") / "veredictos_agregados_ciego.json")
                     .read_text(encoding="utf-8"))
    tab = json.loads((rutas.sub(celda, "desanonimizacion_SOLO_MESA") / jt.ARCHIVO_TABLA)
                     .read_text(encoding="utf-8"))
    n = len(ce0.casos_celda(celda)[0])
    if agg["n_agregados"] != n or agg["incompletas"] or tab["n"] != n:
        raise ValueError(f"{celda.id}: base inesperada (esperaba {n} agregados, 0 incompletas; "
                         f"hay {agg['n_agregados']} y {len(agg['incompletas'])} incompletas)")
    fila = {f["id_opaco"]: f for f in tab["filas"]}
    out = {}
    for a in agg["agregados"]:
        f = fila[a["id_opaco"]]
        out[f["id_pregunta"]] = {"veredicto": a["veredicto_pregunta"],
                                 "id_opaco_base": a["id_opaco"],
                                 "sha256_respuesta_base": f["sha256_respuesta"]}
    if len(out) != n:
        raise ValueError("preguntas repetidas en la base")
    return out


def derivar_poblacion(celda: ce0.Celda, rutas: ce0.Rutas) -> dict:
    vb = veredictos_base(celda, rutas)
    dist = dict(Counter(v["veredicto"] for v in vb.values()))
    parciales = sorted(q for q, v in vb.items() if v["veredicto"] == er.VEREDICTO_DISPARADOR)
    correctos = sorted(q for q, v in vb.items() if v["veredicto"] == "correcto")
    k = max(math.ceil(er.FRACCION_AUDITORIA * len(correctos)), er.MINIMO_AUDITORIA) \
        if correctos else 0
    aud = sorted(random.Random(celda.semilla_auditoria).sample(correctos, k))
    pares = [{"id_pregunta": q, "tipo": "parcial_disparado", **vb[q]} for q in parciales] \
        + [{"id_pregunta": q, "tipo": "auditoria_correcto", **vb[q]} for q in aud]
    pares.sort(key=lambda p: p["id_pregunta"])
    base_dir = rutas.sub(celda, "base")
    tab = rutas.sub(celda, "desanonimizacion_SOLO_MESA") / jt.ARCHIVO_TABLA
    return {
        "celda": celda.id,
        "fuente_base": {"agregados": ce0.rel_repo(base_dir / "veredictos_agregados_ciego.json"),
                        "sha256_agregados": ce0.sha256_path(base_dir / "veredictos_agregados_ciego.json"),
                        "tabla": ce0.rel_repo(tab), "sha256_tabla": ce0.sha256_path(tab)},
        "regla": {"disparador": f"veredicto base == '{er.VEREDICTO_DISPARADOR}' (protocolo §3)",
                  "auditoria": (f"{int(er.FRACCION_AUDITORIA * 100)} % de los 'correcto', "
                                f"random.Random('{celda.semilla_auditoria}').sample sobre ids "
                                f"ordenados, tamaño max(ceil, {er.MINIMO_AUDITORIA})"),
                  "reps_agente": ce0.REPS_AGENTE_ENC, "reps_juez": ce0.REPS_JUEZ},
        "distribucion_base": dist,
        "ids_correctos_ordenados": correctos,
        "ids_auditoria": aud,
        "n_pares": len(pares), "n_corridas_agente": len(pares) * ce0.REPS_AGENTE_ENC,
        "n_llamadas_juez": len(pares) * ce0.REPS_AGENTE_ENC * ce0.REPS_JUEZ,
        "pares": pares,
    }


def persistir_poblacion(celda: ce0.Celda, rutas: ce0.Rutas) -> dict:
    p = rutas.sub(celda, "poblacion") / ARCHIVO_POBLACION
    pob = derivar_poblacion(celda, rutas)
    if p.exists():
        prev = json.loads(p.read_text(encoding="utf-8"))
        if prev["pares"] != pob["pares"]:
            raise RuntimeError(f"{p} difiere de la derivación desde la base")
        return prev
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(pob, ensure_ascii=False, indent=2), encoding="utf-8")
    return pob


def casos_agente(celda: ce0.Celda, pob: dict) -> tuple[list[dict], dict]:
    """Los casos disparados en el orden de la base filtrado."""
    disparados = {p["id_pregunta"] for p in pob["pares"]}
    casos, fuente = ce0.casos_celda(celda)
    out = [c for c in casos if c["caso_id"] in disparados]
    if len(out) != len(disparados):
        raise ValueError(f"{len(out)} casos en orden vs {len(disparados)} pares")
    return out, {**fuente, "filtro": "pares del §7 (orden de la base filtrado)", "n": len(out)}


# --------------------------------------------------------------------------- #
# Etapa AGENTE                                                                 #
# --------------------------------------------------------------------------- #
def etapa_agente(celda: ce0.Celda, rutas: ce0.Rutas, *, client_real, tope: float,
                 indice=None) -> dict:
    pob = persistir_poblacion(celda, rutas)
    casos, fuente = casos_agente(celda, pob)
    por_par = {p["id_pregunta"]: p for p in pob["pares"]}
    total = len(casos) * ce0.REPS_AGENTE_ENC
    estado = {"gastado": 0.0, "corridos": 0, "total": total, "tope_usd": tope}
    frenado = False
    for rep in range(1, ce0.REPS_AGENTE_ENC + 1):
        label = celda.label_enc(rep)
        outdir = rutas.trazas / label
        outdir.mkdir(parents=True, exist_ok=True)
        pend = [c for c in casos if not (outdir / f"{rv._sanitizar(c['caso_id'])}.json").exists()]
        print(f"== §7 {celda.id} rep {rep} ({label}): {len(casos)} casos, "
              f"{len(casos) - len(pend)} ya persistidos, {len(pend)} pendientes ==", flush=True)
        if pend:
            ce0.correr_agente(celda, label=label, casos=pend, fuente=fuente, rutas=rutas,
                              client_real=client_real, estado_gasto=estado, indice=indice)
        _anotar_enc(celda, outdir, fuente, rep, por_par)
        if estado["corridos"] >= 3 and \
                estado["gastado"] / estado["corridos"] * estado["total"] > tope:
            print("Etapa §7 agente detenida por freno de proyección.", flush=True)
            frenado = True
            break
    idx = {"n_previstas": total, "reps": {}, "hits": {}}
    for rep in range(1, ce0.REPS_AGENTE_ENC + 1):
        outdir = rutas.trazas / celda.label_enc(rep)
        idx["reps"][rep] = len([f for f in outdir.glob("*.json")
                                if not f.name.startswith(("resumen_", "corrida_"))]) \
            if outdir.exists() else 0
        idx["hits"][rep] = ce0.hits_db(rutas.cache / f"{celda.label_enc(rep)}.db")
    res = {"celda": celda.id, "ts": datetime.now().isoformat(timespec="seconds"),
           "tope_usd": tope, "estado_gasto": estado, "frenado": frenado, "indice": idx}
    rep_dir = rutas.sub(celda, "reporte")
    rep_dir.mkdir(parents=True, exist_ok=True)
    (rep_dir / "resumen_s7_agente.json").write_text(json.dumps(res, ensure_ascii=False, indent=2),
                                                    encoding="utf-8")
    return res


def _anotar_enc(celda: ce0.Celda, outdir: Path, fuente: dict, rep: int, por_par: dict) -> int:
    n = 0
    for f in sorted(Path(outdir).glob("*.json")):
        if f.name.startswith(("resumen_", "corrida_")):
            continue
        t = json.loads(f.read_text(encoding="utf-8"))
        if "tanda0_enc" in t["meta"]:
            continue
        p = por_par[t["meta"]["caso_id"]]
        t["meta"]["tanda0_enc"] = {
            "unidad": "U-TANDA0-2A E5 §7", "celda": celda.id, "backend": celda.backend,
            "rep": rep, "reps_previstas": ce0.REPS_AGENTE_ENC, "label": celda.label_enc(rep),
            "tipo": p["tipo"], "veredicto_base": p["veredicto"],
            "id_opaco_base": p["id_opaco_base"],
            "sha256_respuesta_base": p["sha256_respuesta_base"],
            "semilla_orden_real": fuente.get("semilla_orden"),
            "regla_orden": fuente.get("regla_orden") or fuente.get("origen"),
            "model_segun_api": ce0._modelos_api(t.get("raw_turns_agent") or []),
            "regla": ("protocolo §3: N=3 disparada por veredicto base 'parcial'; "
                      "auditoria_correcto = ceil(10 %) con la semilla de auditoría de la celda"),
        }
        f.write_text(json.dumps(t, ensure_ascii=False, indent=2), encoding="utf-8")
        n += 1
    return n


# --------------------------------------------------------------------------- #
# Etapa JUEZ (§7)                                                              #
# --------------------------------------------------------------------------- #
def cargar_respuestas_enc(celda: ce0.Celda, rutas: ce0.Rutas, pob: dict) -> tuple[list[dict], list[dict]]:
    xs, faltantes = [], []
    ids = [p["id_pregunta"] for p in pob["pares"]]
    por_par = {p["id_pregunta"]: p for p in pob["pares"]}
    for rep in range(1, ce0.REPS_AGENTE_ENC + 1):
        lab = celda.label_enc(rep)
        resp, falt = ce0.cargar_respuestas(celda, rutas.trazas / lab, lab, ids, estricto=False)
        faltantes += [{**f, "rep": rep} for f in falt]
        for r in resp:
            p = por_par[r["id_pregunta"]]
            xs.append({**r, "rep": rep, "label": lab, "tipo": p["tipo"],
                       "id_opaco_base": p["id_opaco_base"], "veredicto_base": p["veredicto"]})
    return xs, faltantes


def armar_casos_enc(celda: ce0.Celda, respuestas: list[dict], gold: dict) -> list[dict]:
    """Patrón enc_r1.armar_casos_enc con ids y semilla §7 de la celda."""
    xs = []
    for r in respuestas:
        if r["pregunta_traza"].strip() != gold[r["id_pregunta"]]["pregunta"].strip():
            raise ValueError(f"{r['id_pregunta']} r{r['rep']}: pregunta de traza ≠ gold")
        sha = ce0.sha256_texto(r["respuesta"])
        xs.append({**r, "sha256_respuesta": sha,
                   "id_opaco": ce0.id_opaco_enc(celda, r["id_pregunta"], r["rep"], sha),
                   "pregunta": gold[r["id_pregunta"]]["pregunta"],
                   "criterios": gold[r["id_pregunta"]]["criterios"]})
    xs.sort(key=lambda c: (c["id_pregunta"], c["sha256_respuesta"], c["rep"]))
    ids = [c["id_opaco"] for c in xs]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids opacos")
    dup = Counter((c["id_pregunta"], c["sha256_respuesta"]) for c in xs)
    duplicados = sorted([q, s, n] for (q, s), n in dup.items() if n > 1)
    random.Random(celda.semilla_orden_juez_enc).shuffle(xs)
    for c in xs:
        c["duplicados_texto"] = duplicados
    return xs


def persistir_orden_y_tabla_enc(celda: ce0.Celda, rutas: ce0.Rutas, casos: list[dict]) -> tuple[Path, Path, Path]:
    p_ord = rutas.sub(celda, "orden") / "orden_juez_s7_ciego.json"
    p_tab = rutas.sub(celda, "desanonimizacion_SOLO_MESA") / "tabla_id_opaco_s7_SOLO_MESA.json"
    p_vin = rutas.sub(celda, "orden") / "vinculo_pares_s7_ciego.json"
    orden = {"celda": celda.id, "semilla": celda.semilla_orden_juez_enc,
             "regla": "sorted por (id_pregunta, sha256 respuesta, rep) → random.Random(semilla).shuffle",
             "n": len(casos),
             "n_textos_duplicados_por_pregunta": len(casos[0]["duplicados_texto"]) if casos else 0,
             "ids_opacos_en_orden": [c["id_opaco"] for c in casos]}
    tabla = {"SOLO_MESA": True, "celda": celda.id, "salt_id_opaco": celda.sal_enc,
             "prefijo": celda.prefijo_enc,
             "regla": "id_opaco = prefijo + sha256(salt|id_pregunta|grafo|rep|sha256(respuesta))[:10]",
             "n": len(casos),
             "filas": sorted(({"id_opaco": c["id_opaco"], "id_pregunta": c["id_pregunta"],
                               "grafo": celda.grafo, "rep": c["rep"], "label": c["label"],
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
        jt._persistir_o_verificar(p, obj)
    return p_ord, p_tab, p_vin


def factory_juez_enc(celda: ce0.Celda, rutas: ce0.Rutas):
    def _f(rep: int, _label_ignorado: str):
        return juez.construir_cliente_real(rep, run_label=celda.label_juez_enc(rep),
                                           cache_dir=rutas.cache,
                                           db_prefix=celda.db_prefix_juez_enc)
    return _f


def etapa_juez(celda: ce0.Celda, rutas: ce0.Rutas, *, client_factory=None,
               precio_in: float | None = None, precio_out: float | None = None,
               tope: float | None = None, solo_agregados: bool = False,
               verbose: bool = True) -> dict:
    pob = persistir_poblacion(celda, rutas)
    gold = ce0.cargar_gold_celda(celda)
    respuestas, faltantes = cargar_respuestas_enc(celda, rutas, pob)
    casos = armar_casos_enc(celda, respuestas, gold)
    _, _, p_vin = persistir_orden_y_tabla_enc(celda, rutas, casos)
    vinculo = json.loads(p_vin.read_text(encoding="utf-8"))
    dups = casos[0]["duplicados_texto"] if casos else []
    censo = {"celda": celda.id, "n_respuestas": len(casos), "n_previstas": pob["n_corridas_agente"],
             "preguntas_distintas": len({c["id_pregunta"] for c in casos}),
             "n_textos_duplicados": len(dups),
             "hits_intra_db_esperados_por_duplicados": ce0.REPS_JUEZ * sum(n - 1 for _, _, n in dups)}
    ciegos = cf.vista_ciega(casos)
    del casos, respuestas
    fugas = jt.verificar_ceguera(celda, ciegos, ["veredicto_base", "parcial_disparado",
                                                 "auditoria_correcto"])
    if fugas:
        raise RuntimeError(f"FUGA en requests del juez §7 (nada se llamó): {fugas[:5]}")
    out_dir = rutas.sub(celda, "enc")
    total = len(ciegos) * ce0.REPS_JUEZ
    resumen_path = out_dir / "resumen_corrida_juez_s7.json"
    gasto, resumen = None, None
    if not solo_agregados:
        out_dir.mkdir(parents=True, exist_ok=True)
        freno = None
        if precio_in is not None and precio_out is not None and tope is not None:
            # Freno de retoma declarado (patrón enc_r1.etapa_juez): con avance
            # previo, el chequeo va acá con el promedio observado en las dbs.
            ids_ciegos = {c["id_opaco"] for c in ciegos}
            n_pend = sum(len(ids_ciegos - pf._ids_en(out_dir / f"veredictos_r{r}.jsonl")
                             - pf._ids_en(out_dir / f"errores_r{r}.jsonl"))
                         for r in range(1, ce0.REPS_JUEZ + 1))
            g0 = pf.gasto_dbs(rutas.cache, ce0.REPS_JUEZ, precio_in, precio_out,
                              celda.db_prefix_juez_enc)
            if n_pend < total and g0["filas"] > 0:
                proy = g0["usd"] + n_pend * g0["usd"] / g0["filas"]
                if proy > tope:
                    return {"frenado": {"en": "retoma", "proyeccion_usd": round(proy, 4),
                                        "tope_usd": tope}}
            else:
                freno = pf.FrenoProyeccion(rutas.cache, ce0.REPS_JUEZ, precio_in, precio_out,
                                           tope, total, db_prefix=celda.db_prefix_juez_enc)
        frenado = pf.correr(ciegos, reps=ce0.REPS_JUEZ, out_dir=out_dir,
                            client_factory=client_factory or factory_juez_enc(celda, rutas),
                            freno=freno, verbose=verbose)
        if precio_in is not None and precio_out is not None:
            gasto = pf.gasto_dbs(rutas.cache, ce0.REPS_JUEZ, precio_in, precio_out,
                                 celda.db_prefix_juez_enc)
        por_rep, errores = pf.cargar_veredictos(out_dir, ce0.REPS_JUEZ)
        resumen = {"celda": celda.id, "llamadas_totales": total, "gasto_real": gasto,
                   "precios": {"in": precio_in, "out": precio_out}, "tope": tope,
                   "frenado_por_proyeccion": frenado, "ts": datetime.now().isoformat(),
                   "llamadas_hechas": sum(len(v) for v in por_rep.values())
                   + sum(len(v) for v in errores.values())}
        resumen_path.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
        if frenado:
            return {"frenado": frenado, "resumen": resumen}
    else:
        resumen = json.loads(resumen_path.read_text(encoding="utf-8")) if resumen_path.exists() else None
        if resumen and resumen["precios"]["in"] is not None:
            gasto = pf.gasto_dbs(rutas.cache, ce0.REPS_JUEZ, resumen["precios"]["in"],
                                 resumen["precios"]["out"], celda.db_prefix_juez_enc)

    agg = pf.agregar(out_dir, ce0.REPS_JUEZ, ciegos)
    ver = pf.verificar_cross_hits(jt.dbs_juez(celda, rutas, celda.db_prefix_juez_enc))
    agg["verificacion_cross_hits"] = ver
    dist = pf.distribucion(agg)
    agg["distribucion"] = dist
    (out_dir / "veredictos_agregados_ciego.json").write_text(
        json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    pares_agg = er.agregar_pares(agg, vinculo)
    rep_dir = rutas.sub(celda, "reporte")
    rep_dir.mkdir(parents=True, exist_ok=True)
    (rep_dir / "veredictos_finales_s7.json").write_text(json.dumps(
        {"generado": datetime.now().isoformat(timespec="seconds"), "celda": celda.id,
         "censo": censo, "faltantes_agente": faltantes, "verificacion_cross_hits_juez": ver,
         "gasto_juez": gasto, "distribucion_por_respuesta": dist["veredicto_pregunta"],
         **pares_agg}, ensure_ascii=False, indent=2), encoding="utf-8")
    L = [f"# §7 de la celda {celda.id} ({celda.label}) — reporte por par", "",
         f"- respuestas nuevas juzgadas: {censo['n_respuestas']} / {censo['n_previstas']} "
         f"(faltantes: {len(faltantes)})",
         f"- cross-hits juez: {ver['cross_hits']} | hits {ver['hits_total']} (esperados por "
         f"duplicados {censo['hits_intra_db_esperados_por_duplicados']}) | incompletas "
         f"{len(agg['incompletas'])}",
         f"- por respuesta (mapping §2): {dist['veredicto_pregunta']}",
         f"- disparados (base parcial) — final: {pares_agg['distribucion_final_disparados']}; "
         f"vías {pares_agg['vias_disparados']}",
         f"- auditoría (base correcto) — final: {pares_agg['distribucion_final_auditoria']}; "
         f"flips {pares_agg['auditoria']['flips']}/{pares_agg['auditoria']['n_pares']}",
         f"- pares incompletos: {pares_agg['n_pares_incompletos']}", "",
         "| id_opaco_base | tipo | votos r1/r2/r3 | final | vía | flip |", "|---|---|---|---|---|---|"]
    for x in pares_agg["pares"]:
        L.append(f"| {x['id_opaco_base']} | {x['tipo']} | "
                 f"{'/'.join(v[:4] if v != 'requiere_adjudicacion' else 'ADJ' for v in x['veredictos_reps'])} "
                 f"| {x['final']} | {x['via']} | {x['flip_descendente'] or '-'} |")
    (rep_dir / "reporte_s7.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    return {"frenado": None, "resumen": resumen, "gasto": gasto, "censo": censo,
            "distribucion": dist, "pares": pares_agg, "faltantes": faltantes}


def main() -> int:
    ap = argparse.ArgumentParser(description="Encadenamiento §7 de una celda de la tanda 0")
    ap.add_argument("--celda", required=True, choices=sorted(ce0.CELDAS))
    ap.add_argument("--etapa", required=True, choices=["poblacion", "agente", "juez"])
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--tope-agente", type=float, default=None)
    ap.add_argument("--precio-in", type=float, default=None)
    ap.add_argument("--precio-out", type=float, default=None)
    ap.add_argument("--tope-juez", type=float, default=None)
    ap.add_argument("--solo-agregados", action="store_true")
    args = ap.parse_args()
    celda = ce0.CELDAS[args.celda]
    rutas = ce0.RUTAS
    if args.etapa == "poblacion":
        pob = persistir_poblacion(celda, rutas)
        print(json.dumps({k: v for k, v in pob.items() if k != "pares"}, ensure_ascii=False, indent=2))
        return 0
    if args.etapa == "agente":
        if not args.autorizado_fase_b or args.tope_agente is None:
            print("ABORTADO: exige --autorizado-fase-b y --tope-agente. Nada se llamó.")
            return 2
        sellos = ce0.rn.verificar_sellos(verbose=True)
        driver = indice = None
        try:
            if celda.backend == "neo4j":
                driver = ce0.rn.abrir_driver()
                indice = ce0.rn.Neo4jIndex(driver, grafo=celda.grafo, modo=ce0.MODO_NEO4J)
            res = etapa_agente(celda, rutas, client_real=rv._real_client(),
                               tope=args.tope_agente, indice=indice)
        finally:
            if driver is not None:
                driver.close()
        if ce0.rn.verificar_sellos() != sellos:
            raise RuntimeError("sellos cambiaron durante la corrida")
        print(f"persistidas por rep: {res['indice']['reps']} | hits por db: {res['indice']['hits']} | "
              f"gasto ${res['estado_gasto']['gastado']:.4f}" + (" | FRENADO" if res["frenado"] else ""))
        return 1 if res["frenado"] else 0
    if not args.solo_agregados and not (args.autorizado_fase_b and args.precio_in is not None
                                        and args.precio_out is not None and args.tope_juez is not None):
        print("ABORTADO: exige --autorizado-fase-b --precio-in --precio-out --tope-juez. Nada se llamó.")
        return 2
    sellos = cf.verificar_sellos()
    res = etapa_juez(celda, rutas, precio_in=args.precio_in, precio_out=args.precio_out,
                     tope=args.tope_juez, solo_agregados=args.solo_agregados)
    if cf.verificar_sellos() != sellos:
        raise RuntimeError("sellos del instrumento cambiaron durante la corrida")
    if res["frenado"]:
        print(f"FRENO: {res['frenado']}")
        return 1
    print(f"{celda.id} §7 — por respuesta: {res['distribucion']['veredicto_pregunta']} | "
          f"disparados: {res['pares']['distribucion_final_disparados']} | auditoría: "
          f"{res['pares']['distribucion_final_auditoria']}")
    if res["gasto"]:
        print(f"gasto juez §7: USD {res['gasto']['usd']} ({res['gasto']['filas']} filas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
