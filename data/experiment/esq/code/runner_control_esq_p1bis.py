"""
runner_control_esq_p1bis.py — RE-CORRIDA del control de instrumento de ESQ-1
bajo la adenda P1′ (U-ESQ-1d.d): brazo A′ (10 unidades dopadas de
control/dopadas_p1bis.json) + brazo C (las MISMAS 10 limpias de la selección
sellada del control original), en modo canal abierto con el prefijo NUEVO
(description del tool corregida — comun_control_esq.PREFIJO_HASH_ABIERTO_ESPERADO).

Es el MISMO runner del control (importa y reutiliza runner_control_esq:
cliente, correr, persistencia) con selección y salidas propias:
  - jsonl:   control/extracciones_control_esq_p1bis.jsonl
  - orden:   control/orden/seleccion_control_esq_p1bis.json
  - resumen: control/resumen_control_esq_p1bis.json
  - caché:   cache/esq_control_p1bis.db (propia; la del control original no
             se toca — su contenido es evidencia de U-ESQ-1c)
  - usage log component: esq_control_e1_p1bis (D3)

Umbrales P1′ (adenda, sellada por commit): A′ ≥7/10 en TOTAL y ≥3/5 en CADA
mitad (las de tipo cuentan solo si emiten tipo_propuesto en el crudo; las de
predicado, solo predicado_propuesto) — los dos sub-conteos se reportan por
separado. C: ≤1/10 emite un tipo propuesto (sin cambio). Medición sobre
tool_input_crudo (fe de erratas 7072626), decisión D-g intacta (error ==
no-emite, no se re-corre).

FRENOS DE GASTO: la corrida real exige (i) --autorizado-tope-parcial 0.50
(eco de la autorización del chat), (ii) `aprobado_por_autora: true` en
control/dopadas_p1bis.json (freno del mandato U-ESQ-1d.b: el contenido
plantado lo aprueba la autora ANTES de gastar). Tope parcial duro USD 0,50.

Uso:
  stub offline:    via selftest_control_esq_p1bis.py
  corrida real:    .venv/bin/python3 -B data/experiment/esq/code/runner_control_esq_p1bis.py \
                       --autorizado-tope-parcial 0.50
  --solo-resumen:  recomputa el resumen desde lo persistido, sin API.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402
import comun_e1                            # noqa: E402
import prompt_e1                           # noqa: E402
import cliente_e1                          # noqa: E402

FIXTURES = cc.CONTROL_DIR / "dopadas_p1bis.json"
JSONL_P1BIS = "extracciones_control_esq_p1bis.jsonl"
DB_P1BIS = cc.CACHE_DIR / "esq_control_p1bis.db"
ORDEN_P1BIS = "seleccion_control_esq_p1bis.json"
RESUMEN_P1BIS = "resumen_control_esq_p1bis.json"

# Candados de byte-identidad del modo cerrado (los mismos sha256 completos
# sellados pre-edición en selftest_canal_abierto_e1.py:53-55).
SHA256_PREFIJO_PROD = "4793d61526087fba8963041a3ef72682712ed44b45952806ab79a68c8885c719"
SHA256_TOOL_SCHEMA_PROD = "3eca62d001a282ac105f8df8b91660de4e98bc042315ca5701ccf3c983bf3473"
NAMESPACE_PROD = "e1_extraccion|cv=e1-extractor-v1-p4793d6152608|think=0"

# Umbrales de P1′ (adenda §4).
UMBRAL_APRIME_TOTAL = 7    # de 10
UMBRAL_APRIME_MITAD = 3    # de 5, en cada mitad
UMBRAL_C = cc.UMBRAL_C     # ≤1 de 10, sin cambio


class ClienteControlEsqP1bis(rc.ClienteControlEsq):
    COMPONENT = "esq_control_e1_p1bis"


def _canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def cargar_fixtures() -> dict:
    if not FIXTURES.exists():
        raise rc.Freno(f"faltan las dopadas: {FIXTURES} (construir_dopadas_p1bis.py)")
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def seleccion_p1bis(fx: dict) -> list[dict]:
    """A′ (10 dopadas, orden del fixture) + C (las 10 de la selección SELLADA
    del control original, mismo orden). El brazo C se lee del archivo
    persistido, no se re-sortea: es la misma selección."""
    sel_orig = json.loads(
        (cc.ORDEN_DIR / "seleccion_control_esq.json").read_text(encoding="utf-8"))
    c_orig = [s for s in sel_orig["seleccion"] if s["brazo"] == "C"]
    if len(c_orig) != 10:
        raise rc.Freno(f"selección original con {len(c_orig)} C (esperaba 10)")
    a_prime = [{"chunk_id": d["chunk_id_dopado"], "to": d["to"],
                "brazo": "A'", "mitad": d["mitad"], "espera": d["espera"],
                "chunk_id_base": d["chunk_id_base"]}
               for d in fx["dopadas"]]
    if len(a_prime) != 10 or sum(1 for s in a_prime if s["mitad"] == "tipo") != 5:
        raise rc.Freno("fixtures dopadas mal formados (esperaba 10 = 5 tipo + 5 predicado)")
    return a_prime + c_orig


def por_id_p1bis(fx: dict) -> dict[str, dict]:
    """chunk_id → chunk para la corrida: los reales de E0 enm01 más las 10
    dopadas de los fixtures (ids con prefijo dop::, jamás colisionan)."""
    por_id = rc.chunks_por_id()
    for d in fx["dopadas"]:
        cid = d["chunk_id_dopado"]
        if cid in por_id:
            raise rc.Freno(f"colisión imposible: {cid} existe en E0")
        por_id[cid] = d["chunk"]
    return por_id


def verificar_p1bis(fx: dict, chunk_real: dict) -> dict:
    """Guardas previas a cualquier gasto, ENCIMA de las del runner original:
    prefijo nuevo, description corregida, byte-identidad del modo cerrado,
    dopadas fuera del universo de ESQ-1 y cadenas no sembradas."""
    guardas = rc.verificar_canal_abierto(chunk_real)   # hash/namespace/schema/system

    tool_on = prompt_e1.tool_schema_e1(canal_abierto=True)
    desc_on = tool_on["description"]
    desc_off = prompt_e1.TOOL_SCHEMA_E1["description"]
    universo = cc.cargar_universo()
    sistema_on = prompt_e1.prefijo_sistema(True)
    tool_on_canon = _canon(tool_on)

    extra = {
        "descripcion_abierta_corregida": (
            "tipo_propuesto" in desc_on and "predicado_propuesto" in desc_on
            and "mutuamente excluyentes" in desc_on
            and "schema cerrado" not in desc_on),
        "descripcion_cerrada_intacta": "schema cerrado v2" in desc_off,
        "cerrado_byte_identico_prefijo": _sha(prompt_e1.PREFIJO_CANONICO) == SHA256_PREFIJO_PROD,
        "cerrado_byte_identico_tool": _sha(_canon(prompt_e1.TOOL_SCHEMA_E1)) == SHA256_TOOL_SCHEMA_PROD,
        "cerrado_namespace_produccion": cliente_e1.namespace_e1(False) == NAMESPACE_PROD,
        "dopadas_fuera_del_universo": all(
            d["chunk_id_dopado"].startswith("dop::")
            and d["chunk_id_dopado"] not in universo
            for d in fx["dopadas"]),
        "clausulas_no_sembradas": all(
            d["clausula_plantada"] not in sistema_on
            and d["clausula_plantada"] not in tool_on_canon
            for d in fx["dopadas"]),
    }
    if not all(extra.values()):
        raise rc.Freno(f"guardas P1′ fallaron: {extra} — no se gasta")
    return {**guardas, **extra}


# --------------------------------------------------------------------------- #
# Conteos P1′                                                                  #
# --------------------------------------------------------------------------- #
def conteos_p1bis(seleccion: list[dict], regs: dict[str, dict]) -> dict:
    """A′ contra el umbral compuesto de P1′; C contra el suyo sellado.
    Una dopada cuenta para su mitad SOLO si el canal esperado dispara en el
    crudo (emite el otro canal → se reporta como 'otro', no cuenta).
    Error o sin registro == no-emite (decisión D-g)."""
    detalle = {}
    for s in seleccion:
        cid = s["chunk_id"]
        reg = regs.get(cid)
        con_error = reg is None or reg.get("error") is not None
        emite = (cc.emite_propuesto(reg) if not con_error
                 else {"tipo": False, "predicado": False, "alguno": False})
        d = {"brazo": s["brazo"], "error": None if reg is None else (reg or {}).get("error"),
             "sin_registro": reg is None, "emite": emite,
             "contenedor_no_lista": bool(reg) and cc.contenedor_no_lista(reg)}
        if s["brazo"] == "A'":
            esperado = "tipo" if s["mitad"] == "tipo" else "predicado"
            otro = "predicado" if esperado == "tipo" else "tipo"
            d["mitad"] = s["mitad"]
            d["hit_esperado"] = emite[esperado]
            d["emitio"] = ("esperado" if emite[esperado]
                           else ("otro_canal" if emite[otro] else "nada"))
        detalle[cid] = d

    ap = [s["chunk_id"] for s in seleccion if s["brazo"] == "A'"]
    ap_tipo = [s["chunk_id"] for s in seleccion
               if s["brazo"] == "A'" and s["mitad"] == "tipo"]
    ap_pred = [s["chunk_id"] for s in seleccion
               if s["brazo"] == "A'" and s["mitad"] == "predicado"]
    cs = [s["chunk_id"] for s in seleccion if s["brazo"] == "C"]

    n_tipo = sum(detalle[c]["hit_esperado"] for c in ap_tipo)
    n_pred = sum(detalle[c]["hit_esperado"] for c in ap_pred)
    n_total = n_tipo + n_pred
    n_c_tipo = sum(detalle[c]["emite"]["tipo"] for c in cs)
    return {
        "A_prime": {
            "n": len(ap), "hits_total": n_total,
            "mitad_tipo": {"n": len(ap_tipo), "hits": n_tipo,
                           "umbral": f">={UMBRAL_APRIME_MITAD} de 5"},
            "mitad_predicado": {"n": len(ap_pred), "hits": n_pred,
                                "umbral": f">={UMBRAL_APRIME_MITAD} de 5"},
            "umbral_total": f">={UMBRAL_APRIME_TOTAL} de 10",
            "pasa": (n_total >= UMBRAL_APRIME_TOTAL
                     and n_tipo >= UMBRAL_APRIME_MITAD
                     and n_pred >= UMBRAL_APRIME_MITAD),
        },
        "C": {
            "n": len(cs), "emiten_tipo_propuesto": n_c_tipo,
            "umbral": f"<={UMBRAL_C} de 10 (tipo propuesto, redaccion sellada)",
            "pasa": n_c_tipo <= UMBRAL_C,
            "emiten_algun_propuesto_sin_umbral": sum(
                detalle[c]["emite"]["alguno"] for c in cs),
        },
        "contenedores_no_lista": sorted(
            c for c in detalle if detalle[c]["contenedor_no_lista"]),
        "con_error": sorted(c for c in detalle
                            if detalle[c]["error"] is not None
                            or detalle[c]["sin_registro"]),
        "detalle_por_unidad": detalle,
    }


def resumen_p1bis(seleccion: list[dict], salida: Path, cliente_resumen, corrida_meta,
                  guardas) -> dict:
    regs = rc.cargar_jsonl_last_wins(salida / JSONL_P1BIS)
    conteos = conteos_p1bis(seleccion, regs)
    agg = cc.agregar_usage([regs[s["chunk_id"]].get("usage")
                            for s in seleccion if s["chunk_id"] in regs])
    universo = cc.cargar_universo()
    factores = cc.factores_produccion()
    # Recargo pareado: usage cerrado de producción de las 20 unidades BASE
    # (para las dopadas, su unidad base; sesgo declarado: el texto dopado es
    # más largo que el base por la cláusula plantada).
    ids_base = [s.get("chunk_id_base", s["chunk_id"]) for s in seleccion]
    agg_prod = cc.usage_produccion_de(universo, ids_base)
    recargo = cc.recargo_medido(agg, factores, agg_prod)
    resumen = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "unidad": "U-ESQ-1d (re-corrida del control, adenda P1')",
        "modelo": cc.MODEL_E1,
        "tarifas_usd_mtok": {**cc.P_E1,
                             "ancla": "reextraccion_v2/corpus_v2/runner_corpus.py:76-78"},
        "guardas": guardas,
        "corrida": corrida_meta,
        "cliente": cliente_resumen,
        "conteos_P1bis": {k: v for k, v in conteos.items()
                          if k != "detalle_por_unidad"},
        "usage_agregado": agg,
        "usage_por_llamada": [{"chunk_id": s["chunk_id"], "brazo": s["brazo"],
                               **(regs[s["chunk_id"]].get("usage") or {})}
                              for s in seleccion if s["chunk_id"] in regs],
        "costo_recomputado_desde_usage_usd": round(cc.costo_usd_desde_usage(agg), 6),
        "formula_costo": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 (USD/MTok); "
                          "tarifas runner_corpus.py:76-78"),
        "recargo_medido_D7_prefijo_nuevo": {
            **recargo,
            "sesgo_declarado": ("pareado contra el usage cerrado de las 20 "
                                "unidades BASE; el texto de las 10 dopadas "
                                "excede al base en su cláusula plantada"),
        },
        "re_presupuesto_esq1_D7": cc.re_presupuesto_esq1(
            recargo, recargo["pref_abierto_medido_tok"]),
        "factores_produccion_recomputados": {k: v for k, v in factores.items()
                                             if k != "agg"},
        "detalle_por_unidad": conteos["detalle_por_unidad"],
    }
    (salida / RESUMEN_P1BIS).write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    return resumen


def persistir_orden_p1bis(seleccion: list[dict], destino: Path) -> Path:
    destino.mkdir(parents=True, exist_ok=True)
    path = destino / ORDEN_P1BIS
    doc = {"unidad": "U-ESQ-1d", "adenda": "adenda_prerregistro_esq1_P1bis.md",
           "regla": ("A' = 10 dopadas de dopadas_p1bis.json (bases: semilla "
                     "sellada 20260827, regla en construir_dopadas_p1bis.py); "
                     "C = las 10 limpias de la selección sellada del control "
                     "original, sin re-sorteo"),
           "seleccion": seleccion}
    if path.exists():
        previo = json.loads(path.read_text(encoding="utf-8"))
        if previo["seleccion"] != seleccion:
            raise rc.Freno(f"{path} existe y difiere de la selección "
                           "recomputada — no se pisa")
        return path
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                    encoding="utf-8")
    return path


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Re-corrida P1' del control de ESQ-1 (A' dopadas + C, canal abierto)")
    ap.add_argument("--stub", action="store_true")
    ap.add_argument("--salida", type=Path, default=cc.CONTROL_DIR)
    ap.add_argument("--autorizado-tope-parcial", type=float, default=None)
    ap.add_argument("--solo-resumen", action="store_true")
    args = ap.parse_args()

    fx = cargar_fixtures()
    seleccion = seleccion_p1bis(fx)
    orden_dir = (args.salida / "orden") if args.stub else cc.ORDEN_DIR
    persistir_orden_p1bis(seleccion, orden_dir)

    if args.solo_resumen:
        r = resumen_p1bis(seleccion, args.salida, None, None, None)
        print(json.dumps(r["conteos_P1bis"], ensure_ascii=False, indent=1))
        return 0

    por_id = por_id_p1bis(fx)
    guardas = verificar_p1bis(fx, por_id[seleccion[-1]["chunk_id"]])
    print(f"[guardas] namespace={guardas['namespace']} | "
          f"prefijo abierto={guardas['prefijo_hash_abierto']}", flush=True)

    if args.stub:
        cliente = rc.StubClienteControl()
    else:
        if args.autorizado_tope_parcial != cc.TOPE_PARCIAL_USD:
            print(f"ABORTADO: la corrida real exige --autorizado-tope-parcial "
                  f"{cc.TOPE_PARCIAL_USD}. Nada se llamó.")
            return 2
        if fx.get("aprobado_por_autora") is not True:
            print("ABORTADO: dopadas_p1bis.json tiene aprobado_por_autora != true "
                  "— el contenido plantado lo aprueba la autora ANTES de "
                  "cualquier gasto (mandato U-ESQ-1d.b). Nada se llamó.")
            return 2
        from dotenv import load_dotenv
        load_dotenv(comun_e1.EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            print(f"ANTHROPIC_API_KEY ausente (esperada en {comun_e1.EVAL_DIR / '.env'})")
            return 1
        cliente = ClienteControlEsqP1bis(
            **cc.P_E1, tope_usd=cc.TOPE_PARCIAL_USD,
            run_label="esq_control_e1_p1bis",
            db_path=DB_P1BIS, canal_abierto=True)

    try:
        meta = rc.correr(cliente, seleccion, args.salida, cc.TOPE_PARCIAL_USD,
                         stub=args.stub, por_id=por_id, jsonl_nombre=JSONL_P1BIS)
    finally:
        cliente_res = cliente.resumen()
        cliente.close()

    r = resumen_p1bis(seleccion, args.salida, cliente_res, meta, guardas)
    ca = r["conteos_P1bis"]["A_prime"]
    cx = r["conteos_P1bis"]["C"]
    print(f"\nA': {ca['hits_total']}/10 total ({ca['umbral_total']}) | "
          f"tipo {ca['mitad_tipo']['hits']}/5 | "
          f"predicado {ca['mitad_predicado']['hits']}/5 | pasa={ca['pasa']}")
    print(f"C: {cx['emiten_tipo_propuesto']}/10 ({cx['umbral']}) | pasa={cx['pasa']}")
    print(f"gasto cliente=USD {cliente_res.get('gasto_usd_real', 0):.4f} | "
          f"costo desde usage=USD {r['costo_recomputado_desde_usage_usd']:.4f} | "
          f"tope parcial {cc.TOPE_PARCIAL_USD}", flush=True)
    if meta.get("frenado"):
        print(f"FRENO: {meta['frenado']}", flush=True)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
