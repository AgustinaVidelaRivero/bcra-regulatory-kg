"""
juez_enc.py — Evaluación CIEGA de las respuestas nuevas del encadenamiento
(198 = 66 pares × 3 re-corridas) con el juez v1 congelado y el MISMO pipeline
ciego de la corrida base (pre-registro §7: "con ESTE mismo método, sin cambios").

Reutiliza sin editar `pipeline_fidelidad` (data/experiment/ev2_fidelidad_eval/
code): correr (N=3, write-through por id opaco, freno por proyección antes de
cada llamada), agregar (modal §4 + mapping §2 + auditoría de fragmentos),
verificar_cross_hits, distribucion. Lo que cambia es SOLO la carga (respuestas
leídas de trazas/ev2_enc_*), los ids opacos (nuevos, salt propio, rep en la
clave), el orden (semilla juez-ev2-enc-v1) y las dbs/labels del juez
(cache/ev2_enc_juez_r{1,2,3}.db, labels ev2_enc_juez_r{1,2,3}).

Ceguera: el pipeline recibe la vista ciega {id_opaco, pregunta, respuesta,
criterios}; el request lo arma juez.construir_kwargs. La tabla
id_opaco → (id_pregunta, grafo, rep) va a desanonimizacion_SOLO_MESA/. Las
salidas del juez van a juez_out/ (ciegas). El vínculo par → ids nuevos
(juez_orden/vinculo_pares_ciego.json) solo relaciona ids opacos entre sí.

Después del juez, agregación por PAR en código (agregacion_enc.py, protocolo
§3: mayoría de las 3 re-corridas juzgadas, empate triple → parcial) y reporte
FINAL CIEGO por id opaco de par (reporte/): veredictos finales, distribución,
tasa de flip de la auditoría, incompletas. El cruce por grafo lo hace la mesa.

Uso (fase B, solo con autorización explícita, precios y tope PROPIO):
  .venv/bin/python -B data/experiment/ev2_encadenamiento/code/juez_enc.py \
      --autorizado-fase-b --precio-in <USD/MTok> --precio-out <USD/MTok> --tope-juez <USD>
  --solo-agregados recomputa agregados y reportes sin llamar a la API.
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

import comun_enc as en                          # noqa: E402
import pipeline_fidelidad as pf                 # noqa: E402  (pipeline ciego de la base, sin editar)
import agregacion_enc as ag                     # noqa: E402
from comun_enc import cf, juez, mapping         # noqa: E402


# --------------------------------------------------------------------------- #
# Carga (con grafo) → vista ciega                                             #
# --------------------------------------------------------------------------- #
def preparar_casos(pob: dict, trazas_dir: Path = en.TRAZAS_DIR) -> tuple[list[dict], list[dict], dict]:
    gold = cf.cargar_gold()
    respuestas, faltantes = en.cargar_respuestas_nuevas(pob, trazas_dir)
    casos = en.armar_casos(respuestas, gold)
    return casos, faltantes, gold


def verificar_ceguera_requests(ciegos: list[dict]) -> list[tuple[str, str]]:
    """Cada request que se mandaría es EXACTAMENTE prompt + (pregunta, respuesta,
    criterios) y su mensaje de usuario no contiene marcador de grafo/label/id de
    pregunta/rep/tipo/veredicto base. Devuelve las fugas (vacío = OK)."""
    fugas = []
    for c in ciegos:
        if set(c) != {"id_opaco", "pregunta", "respuesta", "criterios"}:
            fugas.append((c.get("id_opaco"), "vista no ciega"))
        kw = juez.construir_kwargs(c["pregunta"], c["respuesta"], c["criterios"])
        if set(kw) != {"model", "max_tokens", "temperature", "system", "messages"} \
                or kw["system"] != juez.PROMPT_JUEZ:
            fugas.append((c["id_opaco"], "estructura del request"))
        u = kw["messages"][0]["content"]
        for m in en.buscar_marcadores(u, ["EV2R-", "EV2E-", "id_opaco", "respondible"]):
            fugas.append((c["id_opaco"], m))
    return fugas


def factory_real(rep: int, _label_ignorado: str):
    """pipeline_fidelidad.correr pasa el label de la base; acá se reemplaza por
    el label propio de esta unidad (db y label por rep, patrón rt_c6_n3)."""
    return juez.construir_cliente_real(rep, run_label=en.label_juez(rep),
                                       cache_dir=en.CACHE_DIR, db_prefix=en.DB_PREFIX_JUEZ)


def dbs_juez(cache_dir: Path = en.CACHE_DIR, reps: int = en.REPS_JUEZ) -> list[Path]:
    return [cache_dir / f"{en.DB_PREFIX_JUEZ}_r{r}.db" for r in range(1, reps + 1)]


def keys_db(p: Path) -> set[str]:
    if not p.exists():
        return set()
    conn = sqlite3.connect(str(p))
    ks = {r[0] for r in conn.execute("SELECT key FROM cache")}
    conn.close()
    return ks


def interseccion_con_base(cache_dir: Path = en.CACHE_DIR, reps: int = en.REPS_JUEZ) -> dict:
    """Keys en común entre las dbs del juez de esta unidad y las de la corrida
    base (mismo namespace por rep): informativo — dbs distintas jamás se sirven
    entre sí; una intersección solo puede provenir de una respuesta nueva con
    texto idéntico al de la base para la misma pregunta."""
    out = {}
    for r in range(1, reps + 1):
        mio = keys_db(cache_dir / f"{en.DB_PREFIX_JUEZ}_r{r}.db")
        base = keys_db(cf.CACHE_DIR / f"{cf.DB_PREFIX}_r{r}.db")
        out[f"r{r}"] = len(mio & base)
    return out


# --------------------------------------------------------------------------- #
# Agregación por par (protocolo §3) sobre los agregados ciegos por respuesta   #
# --------------------------------------------------------------------------- #
def agregar_pares(agg: dict, vinculo: dict, reps_agente: int = en.REPS_AGENTE) -> dict:
    por_id = {a["id_opaco"]: a for a in agg["agregados"]}
    incompletas_resp = {x["id_opaco"] for x in agg["incompletas"]}
    pares, incompletos = [], []
    for v in vinculo["pares"]:
        ids = [v["reps"].get(str(r)) for r in range(1, reps_agente + 1)]
        faltan = [r for r, i in zip(range(1, reps_agente + 1), ids)
                  if i is None or i in incompletas_resp or i not in por_id]
        if faltan:
            incompletos.append({"id_opaco_base": v["id_opaco_base"], "tipo": v["tipo"],
                                "ids_reps": ids, "reps_sin_veredicto": faltan,
                                "veredictos_disponibles": [por_id[i]["veredicto_pregunta"] if i in por_id else None
                                                           for i in ids]})
            continue
        votos = [por_id[i]["veredicto_pregunta"] for i in ids]
        det = ag.detalle_par(votos)
        base = "correcto" if v["tipo"] == "auditoria_correcto" else en.VEREDICTO_DISPARADOR
        pares.append({"id_opaco_base": v["id_opaco_base"], "tipo": v["tipo"], "veredicto_base": base,
                      "ids_reps": ids, "veredictos_reps": votos, "distribucion": det["distribucion"],
                      "final": det["final"], "via": det["via"], "unanime": det["unanime"],
                      "flip_descendente": ag.flip_descendente(base, det["final"]),
                      "clasificacion_auxiliar_reps": [por_id[i]["clasificacion_respuesta_modal"] for i in ids],
                      "modales_reps": [por_id[i]["modales"] for i in ids]})
    disp = [p for p in pares if p["tipo"] == "parcial_disparado"]
    aud = [p for p in pares if p["tipo"] == "auditoria_correcto"]
    return {
        "regla": ag.__doc__.strip().splitlines()[0],
        "n_pares_vinculo": vinculo["n_pares"], "n_pares_agregados": len(pares),
        "n_pares_incompletos": len(incompletos), "pares_incompletos": incompletos,
        "distribucion_final_disparados": dict(Counter(p["final"] for p in disp)),
        "distribucion_final_auditoria": dict(Counter(p["final"] for p in aud)),
        "vias_disparados": dict(Counter(p["via"] for p in disp)),
        "vias_auditoria": dict(Counter(p["via"] for p in aud)),
        "unanimes_disparados": sum(p["unanime"] for p in disp),
        "veredictos_individuales_disparados": dict(Counter(v for p in disp for v in p["veredictos_reps"])),
        "veredictos_individuales_auditoria": dict(Counter(v for p in aud for v in p["veredictos_reps"])),
        "auditoria": {"n_pares": len(aud),
                      "flips": sum(p["flip_descendente"] == "flip" for p in aud),
                      "sin_flip": sum(p["flip_descendente"] == "sin_flip" for p in aud),
                      "pendientes": sum(p["flip_descendente"] == "pendiente" for p in aud),
                      "tasa_flip_descendente": (round(sum(p["flip_descendente"] == "flip" for p in aud) / len(aud), 4)
                                                if aud else None),
                      "re_corridas_individuales_no_correcto": sum(v != "correcto" for p in aud for v in p["veredictos_reps"]),
                      "re_corridas_individuales_total": sum(len(p["veredictos_reps"]) for p in aud)},
        "pares": sorted(pares, key=lambda p: p["id_opaco_base"]),
    }


# --------------------------------------------------------------------------- #
# Reporte final ciego                                                          #
# --------------------------------------------------------------------------- #
def reporte_final_md(res: dict, dist: dict, ver: dict, inter_base: dict, gasto: dict | None,
                     sellos: dict, censo: dict, resumen_corrida: dict | None, faltantes: list) -> str:
    L = [f"# Reporte FINAL CIEGO — encadenamiento §7 EV2 (re-corridas N={en.REPS_AGENTE} del agente × juez v1 N={en.REPS_JUEZ})", "",
         "Veredictos por id OPACO. El id de par es el id opaco de la respuesta BASE",
         "(`EV2R-…`, tabla de la corrida base); las respuestas nuevas llevan ids `EV2E-…`",
         "(tabla en `desanonimizacion_SOLO_MESA/`). El cruce por grafo lo computa la mesa.", "",
         "## Instrumento y sellos", ""]
    for k, v in sellos.items():
        L.append(f"- `{k}`: `{v}`")
    L += ["", f"- modelo(s) del juez observado(s): {dist['modelos_observados']}; prompt sha256 observado: {dist['prompt_sha256_observados']}",
          f"- stop_reasons: {dist['stop_reasons']}", "",
          "## Carga", "",
          f"- respuestas nuevas juzgadas: {censo['n_respuestas']} (previstas {censo['n_previstas']}); "
          f"faltantes/incompletas del agente: {len(faltantes)} {faltantes or ''}",
          f"- textos duplicados dentro de una misma pregunta (entre re-corridas): {censo['n_textos_duplicados']} "
          f"→ hits intra-db esperados por never-pay-twice: {censo['hits_intra_db_esperados_por_duplicados']}",
          f"- criterios gold: {censo['n_criterios_gold']}; flag `respondible` (metadato, no viaja al juez): {censo['respondible_flag']}",
          "", "## Corrida del juez", ""]
    if resumen_corrida:
        L += [f"- llamadas: {resumen_corrida.get('llamadas_hechas')} / {resumen_corrida.get('llamadas_totales')}; "
              f"freno por proyección: {resumen_corrida.get('frenado_por_proyeccion')}"]
    if gasto:
        L += [f"- gasto real (desde dbs): {gasto['filas']} filas, {gasto['input_tokens']} in / {gasto['output_tokens']} out → USD {gasto['usd']}; "
              f"por rep {gasto['por_rep']}",
              f"- precios (USD/MTok): {resumen_corrida.get('precios') if resumen_corrida else 'n/d'}; tope: {resumen_corrida.get('tope') if resumen_corrida else 'n/d'}"]
    L += [f"- cross-hits entre repeticiones del juez: **{ver['cross_hits']}** (keys por db {ver['keys_por_db']}; intersecciones {ver['intersecciones']})",
          f"- hits por label dentro de cada db: {ver['hits_por_label']} (total {ver['hits_total']}; esperados por textos "
          f"duplicados {censo['hits_intra_db_esperados_por_duplicados']}; accesos {ver['accesos_por_db']})",
          f"- keys en común con las dbs del juez de la corrida base (informativo; dbs distintas): {inter_base}",
          f"- errores del juez: {res['agg']['errores_por_rep']}; respuestas incompletas: {len(res['agg']['incompletas'])} {res['agg']['incompletas'] or ''}",
          "", "## Distribución por RESPUESTA nueva (mapping §2, ciega)", "",
          f"- veredicto por respuesta: **{dist['veredicto_pregunta']}** sobre {dist['n_agregados']}",
          f"- pares (respuesta, criterio): {dist['n_pares']} — modales {dist['modales_por_par']}; unánimes {dist['pares_unanimes']}; sin_consenso {dist['pares_sin_consenso']}",
          f"- clasificación auxiliar modal: {dist['clasificacion_auxiliar_modal']}",
          f"- auditoría de fragmentos: {dist['auditoria_fragmentos']}",
          "", "## Agregación por PAR (protocolo §3: mayoría de las 3 re-corridas; empate triple → parcial)", ""]
    p = res["pares_agg"]
    L += [f"- pares agregados: {p['n_pares_agregados']} / {p['n_pares_vinculo']}; incompletos: {p['n_pares_incompletos']} {p['pares_incompletos'] or ''}",
          f"- **disparados (base parcial) — final: {p['distribucion_final_disparados']}**; vías {p['vias_disparados']}; unánimes {p['unanimes_disparados']}",
          f"- disparados — veredictos individuales de las re-corridas: {p['veredictos_individuales_disparados']}",
          f"- **auditoría (base correcto) — final: {p['distribucion_final_auditoria']}**; vías {p['vias_auditoria']}",
          f"- auditoría — flips descendentes: {p['auditoria']['flips']} / {p['auditoria']['n_pares']} (tasa {p['auditoria']['tasa_flip_descendente']}); "
          f"sin flip {p['auditoria']['sin_flip']}; pendientes {p['auditoria']['pendientes']}; re-corridas individuales no-correcto "
          f"{p['auditoria']['re_corridas_individuales_no_correcto']} / {p['auditoria']['re_corridas_individuales_total']}",
          "", "## Veredictos finales por par (id opaco base)", "",
          "| id_opaco_base | tipo | votos r1/r2/r3 | final | vía | flip |", "|---|---|---|---|---|---|"]
    for x in p["pares"]:
        L.append(f"| {x['id_opaco_base']} | {x['tipo']} | {'/'.join(v[:4] if v != 'requiere_adjudicacion' else 'ADJ' for v in x['veredictos_reps'])} "
                 f"| {x['final']} | {x['via']} | {x['flip_descendente'] or '-'} |")
    L += ["", "Abreviaturas: corr=correcto, parc=parcial, inco=incorrecto, ADJ=requiere_adjudicacion.", ""]
    return "\n".join(L)


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser(description="Juez ciego sobre las respuestas del encadenamiento (fase B)")
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--precio-in", type=float, default=None)
    ap.add_argument("--precio-out", type=float, default=None)
    ap.add_argument("--tope-juez", type=float, default=None, help="tope USD de ESTA etapa")
    ap.add_argument("--solo-agregados", action="store_true")
    args = ap.parse_args()

    sellos = en.verificar_sellos()
    pob = en.cargar_poblacion()
    casos, faltantes, gold = preparar_casos(pob)
    p_ord, p_tab, p_vin = en.persistir_orden_y_tabla(casos)
    vinculo = json.loads(p_vin.read_text(encoding="utf-8"))
    dups = casos[0]["duplicados_texto"] if casos else []
    censo = {"n_respuestas": len(casos), "n_previstas": pob["n_corridas_agente"],
             "n_textos_duplicados": len(dups),
             # un texto repetido dentro de la misma pregunta produce un request idéntico
             # → hit intra-db (never-pay-twice) en cada rep del juez; se declara
             "hits_intra_db_esperados_por_duplicados": en.REPS_JUEZ * sum(n - 1 for _, _, n in dups),
             "n_criterios_gold": sum(len(g["criterios"]) for g in gold.values()),
             "respondible_flag": dict(Counter(str(c["respondible_flag"]) for c in casos))}
    ciegos = en.vista_ciega(casos)
    del casos                                   # el resto solo ve la vista ciega
    fugas = verificar_ceguera_requests(ciegos)
    if fugas:
        raise RuntimeError(f"FUGA en requests del juez (nada se llamó): {fugas[:5]}")
    total = len(ciegos) * en.REPS_JUEZ
    resumen_path = en.JUEZ_OUT_DIR / "resumen_corrida_juez.json"

    if not args.solo_agregados:
        if not (args.autorizado_fase_b and args.precio_in is not None and args.precio_out is not None
                and args.tope_juez is not None):
            print("ABORTADO: la fase B exige --autorizado-fase-b --precio-in --precio-out --tope-juez. Nada se llamó.")
            return 2
        en.escribir_sellos("sellos_inicio_faseB_juez.txt")
        en.JUEZ_OUT_DIR.mkdir(parents=True, exist_ok=True)
        freno = pf.FrenoProyeccion(en.CACHE_DIR, en.REPS_JUEZ, args.precio_in, args.precio_out,
                                   args.tope_juez, total, db_prefix=en.DB_PREFIX_JUEZ)
        print(f"{len(ciegos)} respuestas × {en.REPS_JUEZ} reps = {total} llamadas | precios in {args.precio_in} / "
              f"out {args.precio_out} | tope etapa USD {args.tope_juez}", flush=True)
        frenado = pf.correr(ciegos, reps=en.REPS_JUEZ, out_dir=en.JUEZ_OUT_DIR, client_factory=factory_real,
                            freno=freno)
        gasto = freno.gasto()
        por_rep, errores = pf.cargar_veredictos(en.JUEZ_OUT_DIR, en.REPS_JUEZ)
        resumen = {"llamadas_totales": total, "gasto_real": gasto,
                   "precios": {"in": args.precio_in, "out": args.precio_out}, "tope": args.tope_juez,
                   "frenado_por_proyeccion": frenado, "ts": datetime.now().isoformat(),
                   "llamadas_hechas": sum(len(v) for v in por_rep.values()) + sum(len(v) for v in errores.values())}
        resumen_path.write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
        if frenado:
            print(f"FRENO POR PROYECCIÓN: {frenado}")
            return 1
    else:
        resumen = json.loads(resumen_path.read_text(encoding="utf-8")) if resumen_path.exists() else None
        gasto = None
        pin = args.precio_in if args.precio_in is not None else (resumen or {}).get("precios", {}).get("in")
        pout = args.precio_out if args.precio_out is not None else (resumen or {}).get("precios", {}).get("out")
        if pin is not None and pout is not None:
            gasto = pf.gasto_dbs(en.CACHE_DIR, en.REPS_JUEZ, pin, pout, en.DB_PREFIX_JUEZ)

    agg = pf.agregar(en.JUEZ_OUT_DIR, en.REPS_JUEZ, ciegos)
    ver = pf.verificar_cross_hits(dbs_juez())
    inter_base = interseccion_con_base()
    agg["verificacion_cross_hits"] = ver
    agg["interseccion_keys_con_base"] = inter_base
    agg["sellos"] = sellos
    dist = pf.distribucion(agg)
    agg["distribucion"] = dist
    en.JUEZ_OUT_DIR.mkdir(parents=True, exist_ok=True)
    (en.JUEZ_OUT_DIR / "veredictos_agregados_ciego.json").write_text(
        json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")

    pares_agg = agregar_pares(agg, vinculo)
    res = {"agg": agg, "pares_agg": pares_agg}
    en.REPORTE_DIR.mkdir(parents=True, exist_ok=True)
    (en.REPORTE_DIR / "veredictos_finales_ciego.json").write_text(json.dumps(
        {"generado": datetime.now().isoformat(timespec="seconds"), "sellos": sellos, "censo": censo,
         "faltantes_agente": faltantes, "verificacion_cross_hits_juez": ver,
         "interseccion_keys_con_base": inter_base, "gasto_juez": gasto,
         "distribucion_por_respuesta": dist["veredicto_pregunta"], **pares_agg},
        ensure_ascii=False, indent=2), encoding="utf-8")
    md = reporte_final_md(res, dist, ver, inter_base, gasto, sellos, censo, resumen, faltantes)
    (en.REPORTE_DIR / "reporte_final_ciego.md").write_text(md, encoding="utf-8")
    if not args.solo_agregados:
        en.escribir_sellos("sellos_fin_faseB_juez.txt")
    if en.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    print(f"por respuesta (ciego): {dist['veredicto_pregunta']} | incompletas {len(agg['incompletas'])}")
    print(f"por par — disparados: {pares_agg['distribucion_final_disparados']} | auditoría: "
          f"{pares_agg['distribucion_final_auditoria']} flips {pares_agg['auditoria']['flips']}/{pares_agg['auditoria']['n_pares']} "
          f"| incompletos {pares_agg['n_pares_incompletos']}")
    print(f"cross-hits juez: {ver['cross_hits']} | hits total {ver['hits_total']} | keys en común con base {inter_base}")
    if gasto:
        print(f"gasto real juez: USD {gasto['usd']} ({gasto['filas']} filas)")
    print(f"→ {en.REPORTE_DIR / 'reporte_final_ciego.md'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
