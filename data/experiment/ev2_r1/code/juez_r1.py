"""
juez_r1.py — Evaluación CIEGA de las 40 respuestas base de r1 con el juez v1
congelado y el MISMO pipeline ciego de la corrida base de EV2 (U-B1.8 fase B
etapa 1; pre-registro ev2_r1/preregistro_ev2_r1.md §4; método
docs/preregistro_evaluacion_fidelidad_ev2.md).

Reutiliza sin editar `pipeline_fidelidad` (ev2_fidelidad_eval/code): correr
(N=3, write-through por id opaco, freno por proyección antes de cada llamada),
agregar (modal §4 + mapping §2 + auditoría de fragmentos), verificar_cross_hits,
distribucion, reporte. Lo que cambia es SOLO la carga (respuestas leídas de
trazas/ev2_r1_base/), los ids opacos (EV2R1-, salt juez-ev2-r1), el orden
(semilla juez-ev2-r1) y las dbs/labels del juez (cache/ev2_r1_eval_r{1,2,3}.db,
labels ev2_r1_eval_r{1,2,3}) — patrón exacto de juez_enc (9044a04).

Ceguera: el pipeline recibe la vista ciega {id_opaco, pregunta, respuesta,
criterios}; el request lo arma juez.construir_kwargs; verificación estructural
de no-fuga ANTES de llamar (aborta ante cualquier marcador). La tabla
id_opaco → (id_pregunta, sha, respondible) va a desanonimizacion_SOLO_MESA/.
Con un solo grafo, la distribución ciega del reporte ES la distribución de r1;
la ceguera protege el juicio del juez, no un cruce por grafo.

Uso (fase B, solo con autorización explícita, precios verificados y tope):
  .venv/bin/python -B data/experiment/ev2_r1/code/juez_r1.py \
      --autorizado-fase-b --precio-in <USD/MTok> --precio-out <USD/MTok> --tope <USD>
  --solo-agregados recomputa agregados y reporte sin llamar a la API.
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

import comun_r1 as cr                      # noqa: E402  (registra r1 al importarse)
import pipeline_fidelidad as pf            # noqa: E402  (pipeline ciego, sin editar)
from comun_r1 import cf, juez              # noqa: E402  (juez congelado vía comun_fidelidad)

TRAZAS_BASE_R1 = cr.TRAZAS_DIR / cr.R1["label"]

# Marcadores que jamás pueden aparecer en un input del juez ni en una salida
# ciega (los de la base + los propios de esta unidad).
MARCADORES = list(cf.MARCADORES_GRAFO) + ["ev2_r1", "EV2F-", "salida_r1",
                                          "0226e947", "\"id_pregunta\""]


def buscar_marcadores(texto: str, extra: list[str] = ()) -> list[str]:
    return [m for m in MARCADORES + list(extra) if m in texto]


# --------------------------------------------------------------------------- #
# Carga (con identidad) → vista ciega                                          #
# --------------------------------------------------------------------------- #
def cargar_respuestas_r1(trazas_dir: Path = TRAZAS_BASE_R1) -> list[dict]:
    """Una entrada por traza EV2F-* de r1 (patrón cf.cargar_respuestas, un solo
    label). Exige 40 trazas con respuesta parseada no vacía."""
    xs = []
    for f in sorted(trazas_dir.glob("EV2F-*.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        m, tr = t["meta"], t["trace"]
        fj = tr.get("final_json") or {}
        if m["eje"] != "fidelidad" or m["label"] != cr.R1["label"] \
                or m["grafo"] != cr.R1_KEY or m["kg_sha256"] != cr.R1["sha256"]:
            raise ValueError(f"{f}: meta inesperada")
        if m["caso_id"] != tr["qid"] or m["caso_id"] != f.stem:
            raise ValueError(f"{f}: caso_id/qid/nombre inconsistentes")
        if not tr.get("parse_ok") or not isinstance(fj.get("respuesta"), str) \
                or not fj["respuesta"].strip():
            raise ValueError(f"{f}: traza sin respuesta parseada")
        xs.append({"id_pregunta": m["caso_id"], "respuesta": fj["respuesta"],
                   "respondible_flag": fj.get("respondible"),
                   "pregunta_traza": t["pregunta"]})
    if len(xs) != 40 or len({x["id_pregunta"] for x in xs}) != 40:
        raise ValueError(f"se esperaban 40 trazas EV2F-* únicas en {trazas_dir}: {len(xs)}")
    return xs


def armar_casos(respuestas: list[dict], gold: dict) -> list[dict]:
    """Casos COMPLETOS en el orden ciego pre-declarado: sorted por
    (id_pregunta, sha256 respuesta) → shuffle `juez-ev2-r1` (pre-registro §4)."""
    xs = []
    for r in respuestas:
        if r["pregunta_traza"].strip() != gold[r["id_pregunta"]]["pregunta"].strip():
            raise ValueError(f"{r['id_pregunta']}: pregunta de traza ≠ gold")
        sha = cr.sha256_texto(r["respuesta"])
        xs.append({"id_pregunta": r["id_pregunta"], "sha256_respuesta": sha,
                   "id_opaco": cr.id_opaco_base(r["id_pregunta"], sha),
                   "pregunta": gold[r["id_pregunta"]]["pregunta"],
                   "respuesta": r["respuesta"],
                   "respondible_flag": r["respondible_flag"],
                   "criterios": gold[r["id_pregunta"]]["criterios"]})
    xs.sort(key=lambda c: (c["id_pregunta"], c["sha256_respuesta"]))
    ids = [c["id_opaco"] for c in xs]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids opacos")
    import random
    random.Random(cr.SEMILLA_ORDEN_JUEZ).shuffle(xs)
    return xs


def vista_ciega(casos: list[dict]) -> list[dict]:
    return cf.vista_ciega(casos)


def tabla_desanonimizacion(casos: list[dict]) -> dict:
    return {"SOLO_MESA": True, "salt_id_opaco": cr.SAL_ID_BASE,
            "prefijo": cr.PREFIJO_BASE, "grafo": cr.R1_KEY,
            "regla": ("id_opaco = prefijo + sha256(salt|id_pregunta|r1|"
                      "sha256(respuesta))[:10]"),
            "n": len(casos),
            "filas": sorted(({"id_opaco": c["id_opaco"],
                              "id_pregunta": c["id_pregunta"],
                              "grafo": cr.R1_KEY, "label": cr.R1["label"],
                              "sha256_respuesta": c["sha256_respuesta"],
                              "respondible_flag": c["respondible_flag"],
                              "n_criterios": len(c["criterios"])} for c in casos),
                            key=lambda f: f["id_opaco"])}


def orden_ciego(casos: list[dict]) -> dict:
    return {"semilla": cr.SEMILLA_ORDEN_JUEZ,
            "regla": "sorted por (id_pregunta, sha256 respuesta) → random.Random(semilla).shuffle",
            "n": len(casos),
            "ids_opacos_en_orden": [c["id_opaco"] for c in casos]}


def persistir_orden_y_tabla(casos: list[dict]) -> tuple[Path, Path]:
    cr.ORDEN_DIR.mkdir(parents=True, exist_ok=True)
    cr.DESANON_DIR.mkdir(parents=True, exist_ok=True)
    p_ord = cr.ORDEN_DIR / "orden_juez_r1_ciego.json"
    p_tab = cr.DESANON_DIR / "tabla_id_opaco_r1_SOLO_MESA.json"
    for p, obj in ((p_ord, orden_ciego(casos)), (p_tab, tabla_desanonimizacion(casos))):
        nuevo = json.dumps(obj, ensure_ascii=False, indent=2)
        if p.exists():
            if p.read_text(encoding="utf-8") != nuevo:
                raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
        else:
            p.write_text(nuevo, encoding="utf-8")
    return p_ord, p_tab


def verificar_ceguera_requests(ciegos: list[dict]) -> list[tuple[str, str]]:
    """Patrón juez_enc.verificar_ceguera_requests: cada request es EXACTAMENTE
    prompt + (pregunta, respuesta, criterios) y sin marcadores. Vacío = OK."""
    fugas = []
    for c in ciegos:
        if set(c) != {"id_opaco", "pregunta", "respuesta", "criterios"}:
            fugas.append((c.get("id_opaco"), "vista no ciega"))
        kw = juez.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        if set(kw) != {"model", "max_tokens", "temperature", "system", "messages"} \
                or kw["system"] != juez.PROMPT_JUEZ:
            fugas.append((c["id_opaco"], "estructura del request"))
        u = kw["messages"][0]["content"]
        for m in buscar_marcadores(u, ["EV2R1-", "EV2E1-", "id_opaco", "respondible"]):
            fugas.append((c["id_opaco"], m))
    return fugas


def factory_real(rep: int, _label_ignorado: str):
    """pipeline_fidelidad.correr pasa el label de la base; se reemplaza por el
    de esta unidad (db y label por rep, patrón rt_c6_n3)."""
    return juez.construir_cliente_real(rep, run_label=cr.label_juez(rep),
                                       cache_dir=cr.CACHE_DIR,
                                       db_prefix=cr.DB_PREFIX_JUEZ)


def dbs_juez() -> list[Path]:
    return [cr.CACHE_DIR / f"{cr.DB_PREFIX_JUEZ}_r{r}.db" for r in range(1, cr.REPS_JUEZ + 1)]


def keys_db(p: Path) -> set[str]:
    if not p.exists():
        return set()
    conn = sqlite3.connect(str(p))
    ks = {r[0] for r in conn.execute("SELECT key FROM cache")}
    conn.close()
    return ks


def interseccion_con_base() -> dict:
    """Keys en común con las dbs del juez de la corrida base de EV2
    (informativo; dbs distintas jamás se sirven entre sí — una intersección
    solo puede provenir de una respuesta de r1 con texto idéntico al de un
    grafo de la base para la misma pregunta)."""
    return {f"r{r}": len(keys_db(cr.CACHE_DIR / f"{cr.DB_PREFIX_JUEZ}_r{r}.db")
                        & keys_db(cf.CACHE_DIR / f"{cf.DB_PREFIX}_r{r}.db"))
            for r in range(1, cr.REPS_JUEZ + 1)}


# --------------------------------------------------------------------------- #
# Main                                                                         #
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Juez v1 N=3 sobre las 40 respuestas base de r1 (fase B etapa 1)")
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--precio-in", type=float, default=None, help="USD/MTok entrada (verificado el día de la corrida)")
    ap.add_argument("--precio-out", type=float, default=None, help="USD/MTok salida")
    ap.add_argument("--tope", type=float, default=None, help="tope USD de ESTA etapa")
    ap.add_argument("--solo-agregados", action="store_true")
    args = ap.parse_args()

    sellos = cr.verificar_sellos()
    gold = cf.cargar_gold()
    respuestas = cargar_respuestas_r1()
    casos = armar_casos(respuestas, gold)
    p_ord, p_tab = persistir_orden_y_tabla(casos)
    censo = {"n_respuestas": len(casos), "por_grafo": {cr.R1_KEY: len(casos)},
             "preguntas_distintas": len({c["id_pregunta"] for c in casos}),
             "respuestas_por_pregunta": dict(Counter(Counter(
                 c["id_pregunta"] for c in casos).values())),
             "n_criterios_gold": sum(len(g["criterios"]) for g in gold.values()),
             "respondible_flag": dict(Counter(str(c["respondible_flag"]) for c in casos))}
    ciegos = vista_ciega(casos)
    del casos, respuestas                     # el resto solo ve la vista ciega
    fugas = verificar_ceguera_requests(ciegos)
    if fugas:
        raise RuntimeError(f"FUGA en requests del juez (nada se llamó): {fugas[:5]}")
    total = len(ciegos) * cr.REPS_JUEZ
    resumen_path = cr.JUEZ_OUT_DIR / "resumen_corrida_juez_r1.json"

    if not args.solo_agregados:
        if not (args.autorizado_fase_b and args.precio_in is not None
                and args.precio_out is not None and args.tope is not None):
            print("ABORTADO: la fase B exige --autorizado-fase-b --precio-in "
                  "--precio-out --tope. Nada se llamó.")
            return 2
        cr.escribir_sellos("sellos_inicio_faseB_juez.txt")
        cr.JUEZ_OUT_DIR.mkdir(parents=True, exist_ok=True)
        freno = pf.FrenoProyeccion(cr.CACHE_DIR, cr.REPS_JUEZ, args.precio_in,
                                   args.precio_out, args.tope, total,
                                   db_prefix=cr.DB_PREFIX_JUEZ)
        print(f"{len(ciegos)} respuestas × {cr.REPS_JUEZ} reps = {total} llamadas | "
              f"precios in {args.precio_in} / out {args.precio_out} | tope USD {args.tope}",
              flush=True)
        frenado = pf.correr(ciegos, reps=cr.REPS_JUEZ, out_dir=cr.JUEZ_OUT_DIR,
                            client_factory=factory_real, freno=freno)
        gasto = freno.gasto()
        por_rep, errores = pf.cargar_veredictos(cr.JUEZ_OUT_DIR, cr.REPS_JUEZ)
        resumen = {"llamadas_totales": total, "gasto_real": gasto,
                   "precios": {"in": args.precio_in, "out": args.precio_out},
                   "tope": args.tope, "frenado_por_proyeccion": frenado,
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
        pin = args.precio_in if args.precio_in is not None else (resumen or {}).get("precios", {}).get("in")
        pout = args.precio_out if args.precio_out is not None else (resumen or {}).get("precios", {}).get("out")
        if pin is not None and pout is not None:
            gasto = pf.gasto_dbs(cr.CACHE_DIR, cr.REPS_JUEZ, pin, pout, cr.DB_PREFIX_JUEZ)

    agg = pf.agregar(cr.JUEZ_OUT_DIR, cr.REPS_JUEZ, ciegos)
    ver = pf.verificar_cross_hits(dbs_juez())
    inter_base = interseccion_con_base()
    agg["verificacion_cross_hits"] = ver
    agg["interseccion_keys_con_base_ev2"] = inter_base
    agg["sellos"] = sellos
    dist = pf.distribucion(agg)
    agg["distribucion"] = dist
    cr.JUEZ_OUT_DIR.mkdir(parents=True, exist_ok=True)
    (cr.JUEZ_OUT_DIR / "veredictos_agregados_ciego.json").write_text(
        json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    md = pf.reporte_ciego_md(agg, dist, ver, gasto, sellos, censo, resumen)
    md = md.replace("# Reporte CIEGO — fidelidad EV2",
                    "# Reporte CIEGO — fidelidad EV2 de KG-Reextraído-r1 (U-B1.8)")
    (cr.JUEZ_OUT_DIR / "reporte_ciego_r1.md").write_text(md, encoding="utf-8")
    if not args.solo_agregados:
        cr.escribir_sellos("sellos_fin_faseB_juez.txt")
    if cr.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    print(f"veredictos por pregunta (r1): {dist['veredicto_pregunta']} | "
          f"incompletas {len(agg['incompletas'])}")
    print(f"cross-hits: {ver['cross_hits']} (esperado 0) | hits total {ver['hits_total']} | "
          f"keys en común con dbs base EV2 (informativo): {inter_base}")
    if gasto:
        print(f"gasto real juez: USD {gasto['usd']} ({gasto['filas']} filas)")
    print(f"→ {cr.JUEZ_OUT_DIR / 'reporte_ciego_r1.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
