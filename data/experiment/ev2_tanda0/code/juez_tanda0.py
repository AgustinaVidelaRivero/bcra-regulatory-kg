"""
juez_tanda0.py — U-TANDA0-2A E5 (instrumento 10, parte juez): evaluación CIEGA
de la corrida base de una celda (C2-C5) con el juez v1 congelado, N=3, voto
modal y mapping §2, por el MISMO pipeline ciego de C1 (pipeline_fidelidad sin
editar; patrón exacto de ev2_r1/code/juez_r1.py).

Reutiliza por import, sin editar: pipeline_fidelidad (correr con write-through
por id opaco, FrenoProyeccion, agregar, verificar_cross_hits, distribucion,
reporte_ciego_md, gasto_dbs), comun_fidelidad (vista_ciega), el juez congelado
(juez.construir_kwargs / construir_cliente_real, prompt v1 fd446f8e…) y
juez_r1 (buscar_marcadores y el patrón de orden ciego, tabla SOLO_MESA y
verificación de requests). Parametriza por celda, vía celdas_tanda0, lo que
juez_r1 cablea a r1 en comun_r1: trazas y label, grafo y sha esperados,
cantidad de respuestas (40 o 20), gold (EV2 o preguntas de C5), ids opacos
(sal y prefijo propios), semilla del orden ciego, dbs y labels del juez.

Salidas por celda (mandato decisión 10): data/experiment/ev2_tanda0/juez_out/<celda>/
  base/            veredictos_r{1,2,3}.jsonl, errores, veredictos_agregados_ciego.json,
                   reporte_ciego_<label>.md, resumen_corrida_juez.json
  orden/           orden_juez_base_ciego.json
  desanonimizacion_SOLO_MESA/  tabla_id_opaco_base_SOLO_MESA.json
dbs: data/experiment/ev2_tanda0/cache/<label>_juez_r{1,2,3}.db (gitignoradas).

Uso (fase B, solo con autorización explícita, precios verificados y tope):
  .venv/bin/python -B data/experiment/ev2_tanda0/code/juez_tanda0.py --celda C2 \
      --autorizado-fase-b --precio-in <USD/MTok> --precio-out <USD/MTok> --tope <USD>
  --solo-agregados recomputa agregados y reporte sin llamar a la API.
"""

from __future__ import annotations

import argparse
import json
import random
import sqlite3
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import celdas_tanda0 as ce0                 # noqa: E402  (registro de celdas; importa comun_r1 y comun_tanda0)
import juez_r1 as jr                        # noqa: E402  (marcadores y patrón, sin editar)
import pipeline_fidelidad as pf             # noqa: E402  (pipeline ciego, sin editar)
from comun_r1 import cf, juez               # noqa: E402  (juez congelado vía comun_fidelidad)

ARCHIVO_ORDEN = "orden_juez_base_ciego.json"
ARCHIVO_TABLA = "tabla_id_opaco_base_SOLO_MESA.json"


# --------------------------------------------------------------------------- #
# Carga → casos en orden ciego → vista ciega                                   #
# --------------------------------------------------------------------------- #
def cargar_respuestas_base(celda: ce0.Celda, rutas: ce0.Rutas) -> list[dict]:
    casos, _ = ce0.casos_celda(celda)
    xs, _ = ce0.cargar_respuestas(celda, rutas.trazas / celda.label, celda.label,
                                  [c["caso_id"] for c in casos], estricto=True)
    return xs


def armar_casos(celda: ce0.Celda, respuestas: list[dict], gold: dict) -> list[dict]:
    """Patrón juez_r1.armar_casos: sorted por (id_pregunta, sha256 respuesta) →
    shuffle con la semilla del orden ciego de la celda."""
    xs = []
    for r in respuestas:
        if r["pregunta_traza"].strip() != gold[r["id_pregunta"]]["pregunta"].strip():
            raise ValueError(f"{r['id_pregunta']}: pregunta de traza ≠ gold")
        sha = ce0.sha256_texto(r["respuesta"])
        xs.append({"id_pregunta": r["id_pregunta"], "sha256_respuesta": sha,
                   "id_opaco": ce0.id_opaco_base(celda, r["id_pregunta"], sha),
                   "pregunta": gold[r["id_pregunta"]]["pregunta"],
                   "respuesta": r["respuesta"],
                   "respondible_flag": r["respondible_flag"],
                   "criterios": gold[r["id_pregunta"]]["criterios"]})
    xs.sort(key=lambda c: (c["id_pregunta"], c["sha256_respuesta"]))
    ids = [c["id_opaco"] for c in xs]
    if len(set(ids)) != len(ids):
        raise ValueError("colisión de ids opacos")
    random.Random(celda.semilla_orden_juez).shuffle(xs)
    return xs


def vista_ciega(casos: list[dict]) -> list[dict]:
    return cf.vista_ciega(casos)


def verificar_ceguera(celda: ce0.Celda, ciegos: list[dict], extra: list[str] = ()) -> list[tuple]:
    """Patrón juez_r1.verificar_ceguera_requests con los marcadores de la celda:
    cada request es EXACTAMENTE prompt + (pregunta, respuesta, criterios) y sin
    marcadores. Vacío = OK."""
    marc = ce0.marcadores_celda(celda) + list(extra)
    fugas = []
    for c in ciegos:
        if set(c) != {"id_opaco", "pregunta", "respuesta", "criterios"}:
            fugas.append((c.get("id_opaco"), "vista no ciega"))
        kw = juez.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        if set(kw) != {"model", "max_tokens", "temperature", "system", "messages"} \
                or kw["system"] != juez.PROMPT_JUEZ:
            fugas.append((c["id_opaco"], "estructura del request"))
        u = kw["messages"][0]["content"]
        for m in jr.buscar_marcadores(u, marc):
            fugas.append((c["id_opaco"], m))
    return fugas


def tabla_desanonimizacion(celda: ce0.Celda, casos: list[dict]) -> dict:
    return {"SOLO_MESA": True, "celda": celda.id, "salt_id_opaco": celda.sal_base,
            "prefijo": celda.prefijo_base, "grafo": celda.grafo,
            "regla": "id_opaco = prefijo + sha256(salt|id_pregunta|grafo|sha256(respuesta))[:10]",
            "n": len(casos),
            "filas": sorted(({"id_opaco": c["id_opaco"], "id_pregunta": c["id_pregunta"],
                              "grafo": celda.grafo, "label": celda.label,
                              "sha256_respuesta": c["sha256_respuesta"],
                              "respondible_flag": c["respondible_flag"],
                              "n_criterios": len(c["criterios"])} for c in casos),
                            key=lambda f: f["id_opaco"])}


def orden_ciego(celda: ce0.Celda, casos: list[dict]) -> dict:
    return {"celda": celda.id, "semilla": celda.semilla_orden_juez,
            "regla": "sorted por (id_pregunta, sha256 respuesta) → random.Random(semilla).shuffle",
            "n": len(casos), "ids_opacos_en_orden": [c["id_opaco"] for c in casos]}


def _persistir_o_verificar(p: Path, obj) -> None:
    nuevo = json.dumps(obj, ensure_ascii=False, indent=2)
    if p.exists():
        if p.read_text(encoding="utf-8") != nuevo:
            raise RuntimeError(f"{p} ya existe y difiere de lo recomputado")
    else:
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(nuevo, encoding="utf-8")


def persistir_orden_y_tabla(celda: ce0.Celda, rutas: ce0.Rutas, casos: list[dict]) -> tuple[Path, Path]:
    p_ord = rutas.sub(celda, "orden") / ARCHIVO_ORDEN
    p_tab = rutas.sub(celda, "desanonimizacion_SOLO_MESA") / ARCHIVO_TABLA
    _persistir_o_verificar(p_ord, orden_ciego(celda, casos))
    _persistir_o_verificar(p_tab, tabla_desanonimizacion(celda, casos))
    return p_ord, p_tab


# --------------------------------------------------------------------------- #
# Clientes y dbs                                                               #
# --------------------------------------------------------------------------- #
def factory_real(celda: ce0.Celda, rutas: ce0.Rutas):
    """pipeline_fidelidad.correr pasa el label de la base; se reemplaza por el
    de la celda (db y label por rep, patrón juez_r1.factory_real)."""
    def _f(rep: int, _label_ignorado: str):
        return juez.construir_cliente_real(rep, run_label=celda.label_juez(rep),
                                           cache_dir=rutas.cache,
                                           db_prefix=celda.db_prefix_juez)
    return _f


def dbs_juez(celda: ce0.Celda, rutas: ce0.Rutas, prefix: str | None = None) -> list[Path]:
    prefix = prefix or celda.db_prefix_juez
    return [rutas.cache / f"{prefix}_r{r}.db" for r in range(1, ce0.REPS_JUEZ + 1)]


# --------------------------------------------------------------------------- #
# Corrida del juez de la base                                                  #
# --------------------------------------------------------------------------- #
def juzgar_base(celda: ce0.Celda, rutas: ce0.Rutas, *, client_factory=None,
                precio_in: float | None = None, precio_out: float | None = None,
                tope: float | None = None, solo_agregados: bool = False,
                verbose: bool = True) -> dict:
    """Corre (o solo agrega) el juez de la base de la celda. `client_factory`
    inyectable (el selftest usa un cliente falso); default: cliente real."""
    gold = ce0.cargar_gold_celda(celda)
    respuestas = cargar_respuestas_base(celda, rutas)
    casos = armar_casos(celda, respuestas, gold)
    persistir_orden_y_tabla(celda, rutas, casos)
    censo = {"n_respuestas": len(casos), "por_grafo": {celda.grafo: len(casos)},
             "preguntas_distintas": len({c["id_pregunta"] for c in casos}),
             "respuestas_por_pregunta": dict(Counter(Counter(
                 c["id_pregunta"] for c in casos).values())),
             "n_criterios_gold": sum(len(g["criterios"]) for g in gold.values()),
             "respondible_flag": dict(Counter(str(c["respondible_flag"]) for c in casos))}
    ciegos = vista_ciega(casos)
    del casos, respuestas
    fugas = verificar_ceguera(celda, ciegos)
    if fugas:
        raise RuntimeError(f"FUGA en requests del juez (nada se llamó): {fugas[:5]}")
    out_dir = rutas.sub(celda, "base")
    total = len(ciegos) * ce0.REPS_JUEZ
    resumen_path = out_dir / "resumen_corrida_juez.json"
    gasto, resumen = None, None
    if not solo_agregados:
        out_dir.mkdir(parents=True, exist_ok=True)
        freno = None
        if precio_in is not None and precio_out is not None and tope is not None:
            freno = pf.FrenoProyeccion(rutas.cache, ce0.REPS_JUEZ, precio_in, precio_out,
                                       tope, total, db_prefix=celda.db_prefix_juez)
        frenado = pf.correr(ciegos, reps=ce0.REPS_JUEZ, out_dir=out_dir,
                            client_factory=client_factory or factory_real(celda, rutas),
                            freno=freno, verbose=verbose)
        por_rep, errores = pf.cargar_veredictos(out_dir, ce0.REPS_JUEZ)
        if precio_in is not None and precio_out is not None:
            gasto = pf.gasto_dbs(rutas.cache, ce0.REPS_JUEZ, precio_in, precio_out,
                                 celda.db_prefix_juez)
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
        pin = precio_in if precio_in is not None else ((resumen or {}).get("precios") or {}).get("in")
        pout = precio_out if precio_out is not None else ((resumen or {}).get("precios") or {}).get("out")
        if pin is not None and pout is not None:
            gasto = pf.gasto_dbs(rutas.cache, ce0.REPS_JUEZ, pin, pout, celda.db_prefix_juez)

    agg = pf.agregar(out_dir, ce0.REPS_JUEZ, ciegos)
    ver = pf.verificar_cross_hits(dbs_juez(celda, rutas))
    agg["verificacion_cross_hits"] = ver
    dist = pf.distribucion(agg)
    agg["distribucion"] = dist
    agg["celda"] = celda.id
    (out_dir / "veredictos_agregados_ciego.json").write_text(
        json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")
    md = pf.reporte_ciego_md(agg, dist, ver, gasto, {}, censo, resumen)
    md = md.replace("# Reporte CIEGO — fidelidad EV2",
                    f"# Reporte CIEGO — fidelidad EV2, celda {celda.id} de la tanda 0 ({celda.label})")
    (out_dir / f"reporte_ciego_{celda.label}.md").write_text(md, encoding="utf-8")
    return {"frenado": None, "resumen": resumen, "gasto": gasto, "censo": censo,
            "distribucion": dist, "incompletas": agg["incompletas"], "cross_hits": ver}


def main() -> int:
    ap = argparse.ArgumentParser(description="Juez v1 N=3 sobre la corrida base de una celda de la tanda 0")
    ap.add_argument("--celda", required=True, choices=sorted(ce0.CELDAS))
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--precio-in", type=float, default=None, help="USD/MTok entrada (verificado el día)")
    ap.add_argument("--precio-out", type=float, default=None, help="USD/MTok salida")
    ap.add_argument("--tope", type=float, default=None, help="tope USD de ESTA etapa")
    ap.add_argument("--solo-agregados", action="store_true")
    args = ap.parse_args()
    celda = ce0.CELDAS[args.celda]
    if not args.solo_agregados and not (args.autorizado_fase_b and args.precio_in is not None
                                        and args.precio_out is not None and args.tope is not None):
        print("ABORTADO: la fase B exige --autorizado-fase-b --precio-in --precio-out --tope. "
              "Nada se llamó.")
        return 2
    sellos = cf.verificar_sellos()
    res = juzgar_base(celda, ce0.RUTAS, precio_in=args.precio_in, precio_out=args.precio_out,
                      tope=args.tope, solo_agregados=args.solo_agregados)
    if cf.verificar_sellos() != sellos:
        raise RuntimeError("sellos del instrumento cambiaron durante la corrida")
    if res["frenado"]:
        print(f"FRENO POR PROYECCIÓN: {res['frenado']}")
        return 1
    print(f"{celda.id}: veredictos por pregunta {res['distribucion']['veredicto_pregunta']} | "
          f"incompletas {len(res['incompletas'])} | cross-hits {res['cross_hits']['cross_hits']}")
    if res["gasto"]:
        print(f"gasto real juez: USD {res['gasto']['usd']} ({res['gasto']['filas']} filas)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
