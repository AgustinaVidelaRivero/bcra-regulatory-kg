"""
driver_calibracion.py — Corrida de calibración del juez de fidelidad EV2 sobre
los 25 casos de U6 (pre-registro §5), N=3 con veredicto modal (§4) y mapping
fijo por pregunta (§2).

CEGUERA DEL VEREDICTO HUMANO: este driver no recibe, no abre y no conoce la
adjudicación previa de U6 — no existe parámetro ni ruta para ella. El cómputo
de acuerdo juez-humana es un paso POSTERIOR y separado, del lado del análisis;
el input del juez se arma únicamente con (pregunta, respuesta, criterios).

Entradas:
  - preguntas:  data/experiment/exploracion/generacion/preguntas_u6.json
  - respuestas: trace.final_json.respuesta de las trazas de u6_exploracion
                (SOLO ese campo viaja al juez; el flag `respondible` se persiste
                aparte como contraste de la clasificación auxiliar)
  - criterios:  data/experiment/exploracion/u6_fidelidad/criterios_u6.json
                (sellado en commit 2ac2fab, sha256 b8d65789…; 25 preguntas /
                92 criterios). Esquema: {"preguntas": [{"id", "to", "pregunta",
                "gold": {"ancla", "criterios": [{"criterio", "cita_textual"}]}}]}.
                Se lee tal cual; solo criterio + cita_textual viajan al juez.

Orden: shuffle determinístico con semilla "juez-calibracion-v1" sobre los ids
ordenados. Cada repetición corre bajo label y db propios (patrón rt_c6_n3);
al cierre se verifica y declara 0 cross-hits entre repeticiones.

Persistencia write-through: cada caso juzgado se appendea a su jsonl al
instante; re-lanzar retoma donde quedó (los ya juzgados se saltean y, de
llamarse igual, serían hits de caché — nunca se paga dos veces).

Uso:
  .venv/bin/python data/experiment/ev2_juez/driver_calibracion.py \
      --criterios data/experiment/ev2_juez/calibracion/criterios_u6.json
  (--reps 3 --out out/ --cache-dir cache/ por defecto; --solo-agregados
   recomputa agregados sin llamar a la API)
"""

from __future__ import annotations

import argparse
import json
import random
import sqlite3
from pathlib import Path

from juez import construir_cliente_real, juzgar
from mapping import veredicto_modal, veredicto_pregunta

JUEZ_DIR = Path(__file__).resolve().parent
EXP_DIR = JUEZ_DIR.parent
PREGUNTAS_PATH = EXP_DIR / "exploracion" / "generacion" / "preguntas_u6.json"
TRAZAS_DIR = (EXP_DIR / "evaluacion" / "posthoc_run" / "traces"
              / "u6_exploracion" / "reensamblado_v3")

SEMILLA_ORDEN = "juez-calibracion-v1"
REPS_DEFAULT = 3
RUN_LABEL_BASE = "juez_calib"


# --------------------------------------------------------------------------- #
# Carga de insumos                                                            #
# --------------------------------------------------------------------------- #
def cargar_preguntas(path: Path = PREGUNTAS_PATH) -> dict[str, dict]:
    xs = json.loads(path.read_text(encoding="utf-8"))
    return {x["id"]: x for x in xs}


def cargar_respuestas(trazas_dir: Path = TRAZAS_DIR) -> dict[str, dict]:
    """{qid: {"respuesta": str, "respondible": bool|None}} desde las trazas.
    Solo `respuesta` viaja al juez; `respondible` se persiste como contraste."""
    out = {}
    for f in sorted(trazas_dir.glob("*.json")):
        t = json.loads(f.read_text(encoding="utf-8"))[0]
        fj = t["trace"]["final_json"] or {}
        if not fj.get("respuesta"):
            raise ValueError(f"traza sin respuesta parseada: {f.name}")
        out[t["qid"]] = {"respuesta": fj["respuesta"],
                         "respondible": fj.get("respondible")}
    return out


# Sesión de la app local en la que se hicieron las 25 preguntas de U6 y sobre
# cuyas respuestas se hizo la adjudicación humana (la planilla de adjudicación
# apunta a esta sesión como fuente; laudo №0 de laudos_sellado_u6.md). Las trazas de
# u6_exploracion son la corrida apareada (B2) del mismo agente: 21/25 respuestas
# DIFIEREN de las adjudicadas. Para calibrar contra el veredicto humano la fuente
# correcta es esta sesión.
APP_SESION_PATH = (JUEZ_DIR.parent.parent.parent / "app" / "sessions" / "local"
                   / "09beef6a-a147-4417-8a53-cea3da678930.jsonl")


def cargar_respuestas_app(preguntas: dict[str, dict],
                          path: Path = APP_SESION_PATH) -> dict[str, dict]:
    """{qid: {"respuesta", "respondible"}} desde la sesión de la app, apareando
    cada turno con la pregunta de U6 por texto exacto. Exige un único turno por
    pregunta y 25/25 apareadas; solo `respuesta` viaja al juez."""
    por_texto = {p["pregunta"].strip(): qid for qid, p in preguntas.items()}
    out: dict[str, dict] = {}
    for ln in path.read_text(encoding="utf-8").splitlines():
        if not ln.strip():
            continue
        r = json.loads(ln)
        if r.get("tipo") != "turno":
            continue
        qid = por_texto.get((r.get("pregunta") or "").strip())
        if not qid:
            continue
        if qid in out:
            raise ValueError(f"{qid}: más de un turno en la sesión de la app")
        rr = r.get("respuesta")
        texto = rr.get("respuesta") if isinstance(rr, dict) else rr
        if not texto:
            raise ValueError(f"{qid}: turno sin respuesta en la sesión de la app")
        out[qid] = {"respuesta": texto,
                    "respondible": rr.get("respondible") if isinstance(rr, dict) else None}
    faltan = sorted(set(preguntas) - set(out))
    if faltan:
        raise ValueError(f"preguntas sin turno en la sesión de la app: {faltan}")
    return out


def cargar_criterios(path: Path) -> dict[str, list[dict]]:
    """Devuelve {qid: [{"criterio", "cita_textual"}, …]} validando el esquema.

    Acepta dos formas del archivo de criterios:
      (a) el esquema SELLADO de data/experiment/exploracion/u6_fidelidad/
          criterios_u6.json (commit 2ac2fab): {"preguntas": [{"id", "to",
          "pregunta", "gold": {"ancla", "criterios": [{"criterio",
          "cita_textual"}]}}]} — solo se lee; el contenido no se altera;
      (b) la forma plana [{"id_pregunta", "criterios": [...]}] del selftest.
    Al juez le llegan únicamente `criterio` y `cita_textual`, en el orden del
    archivo (ni `ancla` ni `to` viajan al modelo)."""
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict) and "preguntas" in data:
        xs = [{"id_pregunta": p["id"],
               "criterios": [{"criterio": c["criterio"], "cita_textual": c["cita_textual"]}
                             for c in p["gold"]["criterios"]]}
              for p in data["preguntas"]]
    elif isinstance(data, list):
        xs = data
    else:
        raise ValueError("criterios_u6.json: esquema no reconocido")
    out = {}
    for i, x in enumerate(xs):
        qid = x.get("id_pregunta")
        crits = x.get("criterios")
        if not qid or not isinstance(crits, list) or not crits:
            raise ValueError(f"entrada {i} inválida: falta id_pregunta o criterios")
        for j, c in enumerate(crits, start=1):
            if not isinstance(c.get("criterio"), str) or not c["criterio"].strip():
                raise ValueError(f"{qid} criterio {j}: campo 'criterio' vacío o ausente")
            if not isinstance(c.get("cita_textual"), str) or not c["cita_textual"].strip():
                raise ValueError(f"{qid} criterio {j}: campo 'cita_textual' vacío o ausente")
        if qid in out:
            raise ValueError(f"id_pregunta duplicado: {qid}")
        out[qid] = crits
    return out


def armar_casos(preguntas: dict, respuestas: dict, criterios: dict) -> list[dict]:
    """Casos completos en el orden aleatorizado sellado. Exige correspondencia
    exacta pregunta↔respuesta↔criterios (nada se juzga a medias)."""
    faltan_r = sorted(set(preguntas) - set(respuestas))
    faltan_c = sorted(set(preguntas) - set(criterios))
    sobran_c = sorted(set(criterios) - set(preguntas))
    if faltan_r or faltan_c or sobran_c:
        raise ValueError(f"correspondencia rota — sin respuesta: {faltan_r}; "
                         f"sin criterios: {faltan_c}; criterios huérfanos: {sobran_c}")
    orden = sorted(preguntas)
    random.Random(SEMILLA_ORDEN).shuffle(orden)
    return [{"qid": q,
             "pregunta": preguntas[q]["pregunta"],
             "respuesta": respuestas[q]["respuesta"],
             "respondible_flag": respuestas[q]["respondible"],
             "criterios": criterios[q]} for q in orden]


# --------------------------------------------------------------------------- #
# Corrida                                                                     #
# --------------------------------------------------------------------------- #
def _ya_juzgados(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {json.loads(l)["qid"] for l in path.read_text(encoding="utf-8").splitlines() if l}


def correr_repeticion(rep: int, casos: list[dict], client, out_path: Path) -> None:
    hechos = _ya_juzgados(out_path)
    pend = [c for c in casos if c["qid"] not in hechos]
    print(f"[rep {rep}] {len(hechos)} ya juzgados, {len(pend)} pendientes")
    with out_path.open("a", encoding="utf-8") as fh:
        for c in pend:
            r = juzgar(client, c["pregunta"], c["respuesta"], c["criterios"])
            reg = {"qid": c["qid"], "rep": rep,
                   "clasificacion_respuesta": r["veredicto"]["clasificacion_respuesta"],
                   "criterios": r["veredicto"]["criterios"],
                   "respondible_flag": c["respondible_flag"],
                   "meta": r["meta"]}
            fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
            fh.flush()
            print(f"  [rep {rep}] {c['qid']} ok "
                  f"(in={r['meta']['input_tokens']} out={r['meta']['output_tokens']})")


def correr(casos: list[dict], *, reps: int, out_dir: Path,
           client_factory) -> list[Path]:
    """client_factory(rep, run_label) → cliente con .messages.create; el selftest
    inyecta acá su cliente falso sin tocar el resto del circuito."""
    out_dir.mkdir(parents=True, exist_ok=True)
    paths = []
    for rep in range(1, reps + 1):
        out_path = out_dir / f"veredictos_r{rep}.jsonl"
        client = client_factory(rep, f"{RUN_LABEL_BASE}_r{rep}")
        try:
            correr_repeticion(rep, casos, client, out_path)
        finally:
            if hasattr(client, "close"):
                client.close()
        paths.append(out_path)
    return paths


# --------------------------------------------------------------------------- #
# Agregación (distribución completa + modal + mapping)                        #
# --------------------------------------------------------------------------- #
def agregar(out_dir: Path, reps: int, casos: list[dict]) -> dict:
    por_rep = {}
    for rep in range(1, reps + 1):
        path = out_dir / f"veredictos_r{rep}.jsonl"
        regs = [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l]
        por_rep[rep] = {r["qid"]: r for r in regs}

    agregados = []
    for c in casos:
        qid = c["qid"]
        regs = [por_rep[rep][qid] for rep in range(1, reps + 1)]
        crits = []
        for i in range(len(c["criterios"])):
            reps_par = [r["criterios"][i]["veredicto"] for r in regs]
            crits.append({
                "indice": i + 1,
                "criterio": c["criterios"][i]["criterio"],
                "veredictos_reps": reps_par,          # distribución completa (§4)
                "modal": veredicto_modal(reps_par),
                "fragmentos_reps": [r["criterios"][i]["fragmento"] for r in regs],
                "justificaciones_reps": [r["criterios"][i]["justificacion"] for r in regs],
            })
        agregados.append({
            "qid": qid,
            "veredicto_pregunta": veredicto_pregunta([x["modal"] for x in crits]),
            "clasificacion_respuesta_reps": [r["clasificacion_respuesta"] for r in regs],
            "respondible_flag": c["respondible_flag"],
            "criterios": crits,
        })
    return {"semilla_orden": SEMILLA_ORDEN, "reps": reps, "agregados": agregados}


# --------------------------------------------------------------------------- #
# Verificación de 0 cross-hits entre repeticiones                             #
# --------------------------------------------------------------------------- #
def verificar_cross_hits(db_paths: list[Path]) -> dict:
    """Dos verificaciones empíricas sobre las dbs de las repeticiones:
    (1) las keys de cada db son pairwise disjuntas (namespaces por rep);
    (2) hits por run_label dentro de cada db (una primera pasada sana = 0)."""
    keys, hits = {}, {}
    for p in db_paths:
        conn = sqlite3.connect(str(p))
        keys[p.name] = {r[0] for r in conn.execute("SELECT key FROM cache")}
        hits[p.name] = dict(conn.execute(
            "SELECT run_label, SUM(hit) FROM access_log GROUP BY run_label"))
        conn.close()
    nombres = sorted(keys)
    inter = {f"{a}∩{b}": len(keys[a] & keys[b])
             for i, a in enumerate(nombres) for b in nombres[i + 1:]}
    return {"keys_por_db": {n: len(keys[n]) for n in nombres},
            "intersecciones": inter,
            "cross_hits": sum(inter.values()),
            "hits_por_label": hits}


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Calibración del juez de fidelidad EV2 (U6)")
    ap.add_argument("--criterios", required=True, type=Path)
    ap.add_argument("--reps", type=int, default=REPS_DEFAULT)
    ap.add_argument("--out", type=Path, default=JUEZ_DIR / "out")
    ap.add_argument("--cache-dir", type=Path, default=JUEZ_DIR / "cache")
    ap.add_argument("--solo-agregados", action="store_true",
                    help="recomputa agregados y verificación sin llamar a la API")
    ap.add_argument("--fuente-respuestas", choices=("trazas", "app"), default="trazas",
                    help="'trazas' = corrida B2 de u6_exploracion; 'app' = sesión de la "
                         "app adjudicada por la humana (fuente correcta para calibrar)")
    args = ap.parse_args()

    preguntas = cargar_preguntas()
    respuestas = (cargar_respuestas_app(preguntas) if args.fuente_respuestas == "app"
                  else cargar_respuestas())
    casos = armar_casos(preguntas, respuestas, cargar_criterios(args.criterios))
    print(f"{len(casos)} casos, orden {SEMILLA_ORDEN}: "
          f"{' '.join(c['qid'] for c in casos[:5])} …")

    if not args.solo_agregados:
        factory = lambda rep, label: construir_cliente_real(
            rep, run_label=label, cache_dir=args.cache_dir)
        correr(casos, reps=args.reps, out_dir=args.out, client_factory=factory)

    agg = agregar(args.out, args.reps, casos)
    ver = verificar_cross_hits(
        [args.cache_dir / f"juez_calibracion_r{r}.db" for r in range(1, args.reps + 1)])
    agg["verificacion_cross_hits"] = ver

    salida = args.out / "veredictos_agregados.json"
    salida.write_text(json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    dist = {}
    for a in agg["agregados"]:
        dist[a["veredicto_pregunta"]] = dist.get(a["veredicto_pregunta"], 0) + 1
    print(f"veredictos por pregunta: {dist}")
    print(f"cross-hits entre repeticiones: {ver['cross_hits']} (esperado 0)")
    print(f"agregados → {salida}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
