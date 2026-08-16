"""
pipeline_fidelidad.py — Evaluación de fidelidad de las 120 respuestas de EV2 con
el juez calibrado y congelado (data/experiment/ev2_juez/, prompt v1 sha256
fd446f8e61f4…), según docs/preregistro_evaluacion_fidelidad_ev2.md (be8a84f).

Qué hace (fase B, gateada):
  - N=3 repeticiones por (respuesta, criterio): tres pasadas completas sobre las
    120 respuestas en el orden §3, cada una bajo db de caché y label propios
    (cache/ev2_eval_r{1,2,3}.db, labels ev2_eval_r{1,2,3}; patrón rt_c6_n3);
  - persistencia write-through por id OPACO en out/veredictos_r{rep}.jsonl
    (re-lanzar retoma; jamás se paga dos veces);
  - freno por proyección: antes de cada llamada, gasto real desde las dbs +
    restantes × costo promedio observado; si supera el tope, frena ANTES de
    llamar;
  - agregación en código: veredicto modal por par (§4) y veredicto por
    pregunta por mapping fijo (§2) — mapping.py del juez, sin cambios —,
    más clasificación auxiliar, fragmentos, y auditoría mecánica de
    fragmentos (auditoria_fragmentos.py);
  - verificación de 0 cross-hits entre repeticiones (keys disjuntas y
    access_log) y gasto real desde las dbs;
  - REPORTE CIEGO por id opaco (out/reporte_ciego.md + veredictos_agregados_
    ciego.json). El cruce veredicto × grafo NO se computa acá: la tabla
    id_opaco → (pregunta, grafo) vive en desanonimizacion/ y lo cruza la
    revisión.

Ceguera: el pipeline solo recibe la VISTA CIEGA (id_opaco, pregunta, respuesta,
criterios); ningún objeto con grafo/label entra a este módulo. El request al
juez lo arma juez.construir_kwargs (pregunta, respuesta, criterios) y nada más.

Errores del juez (salida no parseable / truncada): se registran en
out/errores_r{rep}.jsonl con su causa y NO se reintentan (una salida cacheada
mal formada volvería a fallar igual); la respuesta queda "incompleta", fuera de
los agregados y declarada en el reporte para laudo.

Uso (fase B, solo con autorización explícita):
  .venv/bin/python -B data/experiment/ev2_fidelidad_eval/code/pipeline_fidelidad.py \
      --autorizado-fase-b --precio-in <USD/MTok> --precio-out <USD/MTok> --tope <USD>
  --solo-agregados recomputa agregados/reporte sin llamar a la API.
"""

from __future__ import annotations

import argparse
import json
import sqlite3
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_fidelidad as cf          # noqa: E402
from comun_fidelidad import juez, mapping  # noqa: E402
from auditoria_fragmentos import ESTADOS, auditar_caso  # noqa: E402


# --------------------------------------------------------------------------- #
# Gasto real desde dbs + freno por proyección                                 #
# --------------------------------------------------------------------------- #
def gasto_dbs(cache_dir: Path, reps: int, pin: float, pout: float,
              db_prefix: str = cf.DB_PREFIX) -> dict:
    """Gasto real desde las dbs: filas de la tabla cache (una por miss pagado)."""
    tin = tout = filas = 0
    por_rep = {}
    for rep in range(1, reps + 1):
        p = cache_dir / f"{db_prefix}_r{rep}.db"
        if not p.exists():
            por_rep[rep] = {"filas": 0, "in": 0, "out": 0, "usd": 0.0}
            continue
        conn = sqlite3.connect(str(p))
        n, i, o = conn.execute(
            "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), COALESCE(SUM(output_tokens),0) "
            "FROM cache").fetchone()
        conn.close()
        por_rep[rep] = {"filas": n, "in": i, "out": o,
                        "usd": round(i / 1e6 * pin + o / 1e6 * pout, 4)}
        filas += n; tin += i; tout += o
    return {"filas": filas, "input_tokens": tin, "output_tokens": tout,
            "usd": round(tin / 1e6 * pin + tout / 1e6 * pout, 4), "por_rep": por_rep}


class FrenoProyeccion:
    """proyección = gasto_real + restantes × promedio_por_llamada_observado;
    si supera el tope (con ≥ min_filas observadas) → frenar antes de llamar."""

    def __init__(self, cache_dir: Path, reps: int, pin: float, pout: float,
                 tope: float, total_llamadas: int, min_filas: int = 3,
                 db_prefix: str = cf.DB_PREFIX):
        self.cache_dir, self.reps, self.pin, self.pout = cache_dir, reps, pin, pout
        self.tope, self.total, self.min_filas, self.db_prefix = tope, total_llamadas, min_filas, db_prefix

    def gasto(self) -> dict:
        return gasto_dbs(self.cache_dir, self.reps, self.pin, self.pout, self.db_prefix)

    def chequear(self, hechas: int, donde: str) -> dict | None:
        g = self.gasto()
        restantes = self.total - hechas
        prom = g["usd"] / g["filas"] if g["filas"] else 0.0
        proy = g["usd"] + restantes * prom
        if g["filas"] >= self.min_filas and proy > self.tope:
            return {"en": donde, "gasto_usd": g["usd"], "proyeccion_usd": round(proy, 4),
                    "tope_usd": self.tope, "hechas": hechas, "restantes": restantes}
        return None


# --------------------------------------------------------------------------- #
# Corrida                                                                     #
# --------------------------------------------------------------------------- #
def _ids_en(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return {json.loads(l)["id_opaco"] for l in path.read_text(encoding="utf-8").splitlines() if l}


def correr_repeticion(rep: int, casos_ciegos: list[dict], client, out_dir: Path,
                      freno: FrenoProyeccion | None, hechas_previas: int,
                      verbose: bool = True) -> tuple[int, dict | None]:
    """Una pasada completa (una repetición) sobre los casos ciegos, en orden.
    Devuelve (llamadas hechas o ya hechas en esta rep, freno o None)."""
    out_path = out_dir / f"veredictos_r{rep}.jsonl"
    err_path = out_dir / f"errores_r{rep}.jsonl"
    ya = _ids_en(out_path) | _ids_en(err_path)
    pend = [c for c in casos_ciegos if c["id_opaco"] not in ya]
    if verbose:
        print(f"[rep {rep}] {len(ya)} ya juzgados, {len(pend)} pendientes", flush=True)
    hechas = hechas_previas + len(ya)
    with out_path.open("a", encoding="utf-8") as fh, err_path.open("a", encoding="utf-8") as fe:
        for c in pend:
            if freno is not None:
                f = freno.chequear(hechas, f"rep {rep} {c['id_opaco']}")
                if f:
                    return hechas, f
            try:
                r = juez.juzgar(client, c["pregunta"], c["respuesta"], c["criterios"])
            except ValueError as e:
                fe.write(json.dumps({"id_opaco": c["id_opaco"], "rep": rep,
                                     "error": str(e), "ts": datetime.now().isoformat()},
                                    ensure_ascii=False) + "\n")
                fe.flush()
                hechas += 1
                if verbose:
                    print(f"  [rep {rep}] {c['id_opaco']} ERROR {e}", flush=True)
                continue
            reg = {"id_opaco": c["id_opaco"], "rep": rep,
                   "clasificacion_respuesta": r["veredicto"]["clasificacion_respuesta"],
                   "criterios": r["veredicto"]["criterios"],
                   "meta": r["meta"]}
            fh.write(json.dumps(reg, ensure_ascii=False) + "\n")
            fh.flush()
            hechas += 1
            if verbose:
                extra = ""
                if freno is not None:
                    extra = f" | acumulado USD {freno.gasto()['usd']}"
                print(f"  [rep {rep}] {c['id_opaco']} in={r['meta']['input_tokens']} "
                      f"out={r['meta']['output_tokens']} stop={r['meta']['stop_reason']}{extra}",
                      flush=True)
    return hechas, None


def correr(casos_ciegos: list[dict], *, reps: int, out_dir: Path, client_factory,
           freno: FrenoProyeccion | None = None, verbose: bool = True) -> dict | None:
    """client_factory(rep, run_label) → cliente con .messages.create (el selftest
    inyecta su cliente falso). Devuelve el dict de freno si frenó, o None."""
    out_dir.mkdir(parents=True, exist_ok=True)
    hechas = 0
    for rep in range(1, reps + 1):
        client = client_factory(rep, f"{cf.RUN_LABEL_BASE}_r{rep}")
        try:
            hechas, f = correr_repeticion(rep, casos_ciegos, client, out_dir, freno,
                                          hechas, verbose)
        finally:
            if hasattr(client, "close"):
                client.close()
        if f:
            return f
    return None


# --------------------------------------------------------------------------- #
# Agregación ciega (modal §4 + mapping §2 + auditoría de fragmentos)          #
# --------------------------------------------------------------------------- #
def cargar_veredictos(out_dir: Path, reps: int) -> tuple[dict, dict]:
    por_rep, errores = {}, {}
    for rep in range(1, reps + 1):
        p = out_dir / f"veredictos_r{rep}.jsonl"
        regs = [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l] \
            if p.exists() else []
        por_rep[rep] = {r["id_opaco"]: r for r in regs}
        if len(por_rep[rep]) != len(regs):
            raise ValueError(f"id_opaco duplicado en veredictos_r{rep}.jsonl")
        pe = out_dir / f"errores_r{rep}.jsonl"
        errores[rep] = [json.loads(l) for l in pe.read_text(encoding="utf-8").splitlines() if l] \
            if pe.exists() else []
    return por_rep, errores


def agregar(out_dir: Path, reps: int, casos_ciegos: list[dict]) -> dict:
    """Agregados CIEGOS por id opaco. Solo casos con las N reps completas entran;
    el resto se lista en `incompletas` (para laudo)."""
    por_rep, errores = cargar_veredictos(out_dir, reps)
    agregados, incompletas = [], []
    for c in casos_ciegos:
        oid = c["id_opaco"]
        regs = [por_rep[rep].get(oid) for rep in range(1, reps + 1)]
        if any(r is None for r in regs):
            incompletas.append({"id_opaco": oid,
                                "reps_faltantes": [rep for rep, r in zip(range(1, reps + 1), regs) if r is None]})
            continue
        crits = []
        for i in range(len(c["criterios"])):
            reps_par = [r["criterios"][i]["veredicto"] for r in regs]
            crits.append({
                "indice": i + 1,
                "veredictos_reps": reps_par,                       # distribución completa (§4)
                "modal": mapping.veredicto_modal(reps_par),
                "fragmentos_reps": [r["criterios"][i]["fragmento"] for r in regs],
                "justificaciones_reps": [r["criterios"][i]["justificacion"] for r in regs],
            })
        aud = auditar_caso(c["respuesta"], c["criterios"], crits)
        for cr, est in zip(crits, aud["por_criterio"]):
            cr["auditoria_fragmentos_reps"] = est
        clas = [r["clasificacion_respuesta"] for r in regs]
        agregados.append({
            "id_opaco": oid,
            "n_criterios": len(c["criterios"]),
            "veredicto_pregunta": mapping.veredicto_pregunta([x["modal"] for x in crits]),
            "modales": [x["modal"] for x in crits],
            "clasificacion_respuesta_reps": clas,
            "clasificacion_respuesta_modal": _modal_libre(clas),
            "auditoria_fragmentos": aud["conteo"],
            "criterios": crits,
            "meta_reps": [{"rep": r["rep"], "modelo": r["meta"]["modelo"],
                           "stop_reason": r["meta"]["stop_reason"],
                           "input_tokens": r["meta"]["input_tokens"],
                           "output_tokens": r["meta"]["output_tokens"],
                           "prompt_sha256": r["meta"]["prompt_sha256"],
                           "code_ver": r["meta"]["code_ver"]} for r in regs],
        })
    return {"semilla_orden": cf.SEMILLA_ORDEN, "reps": reps,
            "n_casos": len(casos_ciegos), "n_agregados": len(agregados),
            "incompletas": incompletas,
            "errores_por_rep": {rep: len(v) for rep, v in errores.items()},
            "errores": errores,
            "agregados": agregados}


def _modal_libre(xs: list[str]) -> str:
    """Moda con mayoría estricta para la clasificación auxiliar (dominio
    abstencion/contenido); sin mayoría → 'sin_consenso'. Auxiliar: no entra al
    veredicto (pre-registro §1)."""
    v, n = Counter(xs).most_common(1)[0]
    return v if n > len(xs) / 2 else "sin_consenso"


# --------------------------------------------------------------------------- #
# Verificación de 0 cross-hits                                                #
# --------------------------------------------------------------------------- #
def verificar_cross_hits(db_paths: list[Path]) -> dict:
    """(1) keys pairwise disjuntas entre dbs de repeticiones; (2) hits por
    run_label dentro de cada db (primera pasada sana = 0 hits)."""
    keys, hits, accesos = {}, {}, {}
    for p in db_paths:
        if not p.exists():
            keys[p.name], hits[p.name], accesos[p.name] = set(), {}, 0
            continue
        conn = sqlite3.connect(str(p))
        keys[p.name] = {r[0] for r in conn.execute("SELECT key FROM cache")}
        hits[p.name] = {k: int(v or 0) for k, v in conn.execute(
            "SELECT run_label, SUM(hit) FROM access_log GROUP BY run_label")}
        accesos[p.name] = conn.execute("SELECT COUNT(*) FROM access_log").fetchone()[0]
        conn.close()
    nombres = sorted(keys)
    inter = {f"{a}∩{b}": len(keys[a] & keys[b])
             for i, a in enumerate(nombres) for b in nombres[i + 1:]}
    return {"keys_por_db": {n: len(keys[n]) for n in nombres},
            "accesos_por_db": accesos,
            "intersecciones": inter,
            "cross_hits": sum(inter.values()),
            "hits_por_label": hits,
            "hits_total": sum(v for d in hits.values() for v in d.values())}


# --------------------------------------------------------------------------- #
# Reporte ciego                                                               #
# --------------------------------------------------------------------------- #
def distribucion(agg: dict) -> dict:
    ags = agg["agregados"]
    pares = [c for a in ags for c in a["criterios"]]
    d = {
        "n_agregados": len(ags),
        "n_incompletas": len(agg["incompletas"]),
        "veredicto_pregunta": dict(Counter(a["veredicto_pregunta"] for a in ags)),
        "n_pares": len(pares),
        "modales_por_par": dict(Counter(c["modal"] for c in pares)),
        "veredictos_todas_las_reps": dict(Counter(v for c in pares for v in c["veredictos_reps"])),
        "pares_unanimes": sum(len(set(c["veredictos_reps"])) == 1 for c in pares),
        "pares_no_unanimes_con_dudoso": sum(len(set(c["veredictos_reps"])) > 1
                                            and "dudoso" in c["veredictos_reps"] for c in pares),
        "pares_sin_consenso": sum(c["modal"] == "sin_consenso" for c in pares),
        "clasificacion_auxiliar_modal": dict(Counter(a["clasificacion_respuesta_modal"] for a in ags)),
        "clasificacion_auxiliar_todas_las_reps": dict(Counter(
            v for a in ags for v in a["clasificacion_respuesta_reps"])),
        "clasificacion_auxiliar_no_unanime": sum(
            len(set(a["clasificacion_respuesta_reps"])) > 1 for a in ags),
        "auditoria_fragmentos": {e: sum(a["auditoria_fragmentos"][e] for a in ags) for e in ESTADOS},
        "auditoria_detalle_no_verbatim_o_fuga": [
            {"id_opaco": a["id_opaco"], "indice": c["indice"], "rep": r + 1,
             "veredicto": c["veredictos_reps"][r], "estado": est,
             "fragmento": (c["fragmentos_reps"][r] or "")[:200]}
            for a in ags for c in a["criterios"]
            for r, est in enumerate(c["auditoria_fragmentos_reps"])
            if est in ("fuga_gold", "no_verbatim")],
        "veredicto_x_clasificacion_auxiliar": dict(Counter(
            f"{a['clasificacion_respuesta_modal']}→{a['veredicto_pregunta']}" for a in ags)),
        "stop_reasons": dict(Counter(m["stop_reason"] for a in ags for m in a["meta_reps"])),
        "prompt_sha256_observados": sorted({m["prompt_sha256"] for a in ags for m in a["meta_reps"]}),
        "modelos_observados": sorted({m["modelo"] for a in ags for m in a["meta_reps"]}),
    }
    return d


def reporte_ciego_md(agg: dict, dist: dict, ver: dict, gasto: dict | None,
                     sellos: dict, censo: dict, resumen_corrida: dict | None) -> str:
    L = [f"# Reporte CIEGO — fidelidad EV2 ({agg['n_casos']} respuestas × juez v1, N={agg['reps']})", "",
         "Veredictos por id OPACO. La tabla id_opaco → (pregunta, grafo) vive en",
         "`desanonimizacion/tabla_id_opaco.json` y NO se cruza acá: el cruce",
         "veredicto × grafo lo computa la revisión (pre-registro §3, ceguera de grafo).", "",
         "## Instrumento y sellos", ""]
    for k, v in sellos.items():
        L.append(f"- `{k}`: `{v}`")
    L += ["", f"- modelo(s) observado(s): {dist['modelos_observados']}",
          f"- prompt sha256 observado en las respuestas del juez: {dist['prompt_sha256_observados']}",
          f"- stop_reasons: {dist['stop_reasons']}",
          f"- semilla de orden: `{agg['semilla_orden']}`; N={agg['reps']}", "",
          "## Carga", "",
          f"- respuestas: {censo['n_respuestas']} — por grafo {censo['por_grafo']}; "
          f"{censo['preguntas_distintas']} preguntas × {censo['respuestas_por_pregunta']} respuestas; "
          f"criterios gold {censo['n_criterios_gold']}",
          f"- flag `respondible` del agente (metadato de trazas, no viaja al juez): {censo['respondible_flag']}",
          "", "## Corrida", ""]
    if resumen_corrida:
        L += [f"- llamadas: {resumen_corrida.get('llamadas_hechas')} / {resumen_corrida.get('llamadas_totales')}",
              f"- freno por proyección: {resumen_corrida.get('frenado_por_proyeccion')}"]
    if gasto:
        L += [f"- gasto real (desde dbs, filas de `cache`): {gasto['filas']} filas, "
              f"{gasto['input_tokens']} in / {gasto['output_tokens']} out → USD {gasto['usd']}",
              f"- por repetición: {gasto['por_rep']}",
              f"- precios (USD/MTok): {resumen_corrida.get('precios') if resumen_corrida else 'n/d'}; "
              f"tope: {resumen_corrida.get('tope') if resumen_corrida else 'n/d'}"]
    L += [f"- cross-hits entre repeticiones: **{ver['cross_hits']}** (keys por db {ver['keys_por_db']}; "
          f"intersecciones {ver['intersecciones']})",
          f"- hits por label dentro de cada db: {ver['hits_por_label']} (total {ver['hits_total']}); "
          f"accesos por db {ver['accesos_por_db']}",
          f"- errores del juez (no parseable/truncado): {agg['errores_por_rep']}; "
          f"respuestas incompletas (fuera de agregados): {len(agg['incompletas'])} {agg['incompletas'] or ''}",
          "", "## Distribución (ciega, sobre los agregados)", "",
          f"- veredicto por pregunta (mapping §2): **{dist['veredicto_pregunta']}** sobre {dist['n_agregados']}",
          f"- pares (respuesta, criterio): {dist['n_pares']} — modales {dist['modales_por_par']}; "
          f"todas las reps {dist['veredictos_todas_las_reps']}",
          f"- no-determinismo: unánimes {dist['pares_unanimes']}/{dist['n_pares']}; "
          f"no unánimes con dudoso {dist['pares_no_unanimes_con_dudoso']}; sin_consenso {dist['pares_sin_consenso']}",
          f"- clasificación auxiliar (modal): {dist['clasificacion_auxiliar_modal']}; todas las reps "
          f"{dist['clasificacion_auxiliar_todas_las_reps']}; no unánime en {dist['clasificacion_auxiliar_no_unanime']} respuestas",
          f"- veredicto × clasificación auxiliar: {dist['veredicto_x_clasificacion_auxiliar']}",
          f"- auditoría de fragmentos ({sum(dist['auditoria_fragmentos'].values())}): {dist['auditoria_fragmentos']}",
          ]
    det = dist["auditoria_detalle_no_verbatim_o_fuga"]
    if det:
        L += ["", f"### Fragmentos no_verbatim / fuga_gold ({len(det)})", ""]
        for x in det:
            L.append(f"- {x['id_opaco']} c{x['indice']} r{x['rep']} [{x['veredicto']}] {x['estado']}: «{x['fragmento']}»")
    L += ["", "## Veredictos por id opaco", "",
          "| id_opaco | K | modales por criterio | veredicto (mapping) | clasif. aux. (3 reps) | fragmentos null/verb/fuga/no_verb |",
          "|---|---|---|---|---|---|"]
    for a in sorted(agg["agregados"], key=lambda a: a["id_opaco"]):
        f = a["auditoria_fragmentos"]
        L.append(f"| {a['id_opaco']} | {a['n_criterios']} | {' '.join(m[:4] if m!='sin_consenso' else 'S/C' for m in a['modales'])} "
                 f"| {a['veredicto_pregunta']} | {'/'.join(x[:4] for x in a['clasificacion_respuesta_reps'])} "
                 f"| {f['null']}/{f['verbatim']}/{f['fuga_gold']}/{f['no_verbatim']} |")
    L += ["", "Abreviaturas: cump=cumplido, no_c=no_cumplido, dudo=dudoso, S/C=sin_consenso; "
          "abst=abstencion, cont=contenido.", ""]
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# Main (fase B)                                                               #
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Evaluación de fidelidad EV2 (juez v1, N=3)")
    ap.add_argument("--autorizado-fase-b", action="store_true",
                    help="autorización explícita con precios y tope (fase B)")
    ap.add_argument("--precio-in", type=float, default=None, help="USD por MTok de entrada")
    ap.add_argument("--precio-out", type=float, default=None, help="USD por MTok de salida")
    ap.add_argument("--tope", type=float, default=None, help="tope de gasto en USD (freno por proyección)")
    ap.add_argument("--reps", type=int, default=cf.REPS)
    ap.add_argument("--solo-agregados", action="store_true",
                    help="recomputa agregados y reporte sin llamar a la API")
    args = ap.parse_args()

    sellos = cf.verificar_sellos()
    gold, respuestas, censo, casos = cf.cargar_todo()
    p_ord, p_tab = cf.persistir_orden_y_tabla(casos)
    ciegos = cf.vista_ciega(casos)
    del casos, respuestas  # el resto del main solo ve la vista ciega
    total = len(ciegos) * args.reps
    resumen_path = cf.OUT_DIR / "resumen_corrida.json"

    if not args.solo_agregados:
        if not (args.autorizado_fase_b and args.precio_in is not None
                and args.precio_out is not None and args.tope is not None):
            print("ABORTADO: la fase B exige --autorizado-fase-b --precio-in --precio-out --tope "
                  "(autorización explícita con precios y tope). Nada se llamó.")
            return 2
        cf.OUT_DIR.mkdir(parents=True, exist_ok=True)
        freno = FrenoProyeccion(cf.CACHE_DIR, args.reps, args.precio_in, args.precio_out,
                                args.tope, total)
        print(f"{len(ciegos)} respuestas × {args.reps} reps = {total} llamadas | precios in "
              f"{args.precio_in} / out {args.precio_out} USD/MTok | tope USD {args.tope}", flush=True)
        factory = lambda rep, label: juez.construir_cliente_real(
            rep, run_label=label, cache_dir=cf.CACHE_DIR, db_prefix=cf.DB_PREFIX)
        frenado = correr(ciegos, reps=args.reps, out_dir=cf.OUT_DIR, client_factory=factory,
                         freno=freno)
        gasto = freno.gasto()
        resumen = {"llamadas_totales": total, "gasto_real": gasto,
                   "precios": {"in": args.precio_in, "out": args.precio_out}, "tope": args.tope,
                   "frenado_por_proyeccion": frenado, "ts": datetime.now().isoformat()}
        por_rep, errores = cargar_veredictos(cf.OUT_DIR, args.reps)
        resumen["llamadas_hechas"] = sum(len(v) for v in por_rep.values()) + \
            sum(len(v) for v in errores.values())
        resumen_path.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
        if frenado:
            print(f"FRENO POR PROYECCIÓN: {frenado}")
            print(json.dumps(resumen, ensure_ascii=False, indent=2))
            return 1
    else:
        resumen = json.loads(resumen_path.read_text(encoding="utf-8")) if resumen_path.exists() else None
        gasto = None
        if resumen and args.precio_in is not None and args.precio_out is not None:
            gasto = gasto_dbs(cf.CACHE_DIR, args.reps, args.precio_in, args.precio_out)
        elif resumen:
            gasto = gasto_dbs(cf.CACHE_DIR, args.reps, resumen["precios"]["in"], resumen["precios"]["out"])

    agg = agregar(cf.OUT_DIR, args.reps, ciegos)
    ver = verificar_cross_hits([cf.CACHE_DIR / f"{cf.DB_PREFIX}_r{r}.db" for r in range(1, args.reps + 1)])
    agg["verificacion_cross_hits"] = ver
    agg["sellos"] = sellos
    dist = distribucion(agg)
    agg["distribucion"] = dist
    (cf.OUT_DIR / "veredictos_agregados_ciego.json").write_text(
        json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    md = reporte_ciego_md(agg, dist, ver, gasto, sellos, censo, resumen)
    (cf.OUT_DIR / "reporte_ciego.md").write_text(md, encoding="utf-8")
    sellos_fin = cf.verificar_sellos()
    if sellos_fin != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    print(f"veredictos por pregunta (ciego): {dist['veredicto_pregunta']} | incompletas {len(agg['incompletas'])}")
    print(f"cross-hits: {ver['cross_hits']} (esperado 0) | hits total {ver['hits_total']}")
    if gasto:
        print(f"gasto real: USD {gasto['usd']} ({gasto['filas']} filas)")
    print(f"→ {cf.OUT_DIR / 'veredictos_agregados_ciego.json'}\n→ {cf.OUT_DIR / 'reporte_ciego.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
