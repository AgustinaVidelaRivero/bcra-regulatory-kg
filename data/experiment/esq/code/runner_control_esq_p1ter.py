"""
runner_control_esq_p1ter.py — RE-CORRIDA del control de instrumento de ESQ-1
bajo la adenda P1″ (U-ESQ-1e / O2): brazo A′ (las MISMAS 10 unidades dopadas
de control/dopadas_p1bis.json, byte-idénticas por sha contra c25273f) + brazo
C (las MISMAS 10 limpias de la selección sellada del control original), en
modo canal abierto con los DOS cierres del system neutralizados
(prompt_e1.CIERRE_*_ABIERTO, textos sellados verbatim en
adenda_prerregistro_esq1_P1ter.md §3) — prefijo abierto nuevo
comun_control_esq.PREFIJO_HASH_ABIERTO_ESPERADO.

Cambio de UNA sola variable (adenda §1): entre P1′ y P1″ solo cambian los dos
textos de §3. Dopadas, umbrales, description del tool y brazo C idénticos.
verificar_p1ter() lo hace ejecutable: fixtures por sha256 contra el valor de
c25273f, y el system abierto == el de P1′ (reconstruido y anclado a su hash
sellado d923bf876580) con EXACTAMENTE los dos reemplazos y nada más.

Es el MISMO runner del control (reutiliza runner_control_esq: cliente, correr,
persistencia; y runner_control_esq_p1bis: fixtures, selección, conteos P1′ que
P1″ hereda sin cambio) con salidas propias:
  - jsonl:   control/extracciones_control_esq_p1ter.jsonl
  - orden:   control/orden/seleccion_control_esq_p1ter.json
  - resumen: control/resumen_control_esq_p1ter.json
  - caché:   cache/esq_control_p1ter.db (propia; las de U-ESQ-1c y U-ESQ-1d
             no se tocan — su contenido es evidencia de esas corridas)
  - usage log component: esq_control_e1_p1ter (D3)

Umbrales P1″ == P1′ (adenda §1): A′ ≥7/10 en TOTAL y ≥3/5 en CADA mitad
(sub-conteos separados; el canal equivocado se reporta como cruce y no
cuenta); C ≤1/10 emite tipo propuesto. Medición sobre tool_input_crudo
(7072626), decisión D-g intacta (error == no-emite, no se re-corre).

FRENOS DE GASTO: la corrida real exige (i) --autorizado-tope-parcial 0.50
(eco de la autorización del mandato U-ESQ-1e.c), (ii) `aprobado_por_autora:
true` en control/dopadas_p1bis.json (aprobación vigente por sha). Tope
parcial duro USD 0,50.

Uso:
  stub offline:    via selftest_control_esq_p1ter.py
  corrida real:    .venv/bin/python3 -B data/experiment/esq/code/runner_control_esq_p1ter.py \
                       --autorizado-tope-parcial 0.50
  --solo-resumen:  recomputa el resumen desde lo persistido, sin API.
"""

from __future__ import annotations

import argparse
import difflib
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
import runner_control_esq_p1bis as rp      # noqa: E402
import comun_e1                            # noqa: E402
import prompt_e1                           # noqa: E402
import cliente_e1                          # noqa: E402

ADENDA_P1TER = cc.UNIDAD_DIR / "adenda_prerregistro_esq1_P1ter.md"
JSONL_P1TER = "extracciones_control_esq_p1ter.jsonl"
DB_P1TER = cc.CACHE_DIR / "esq_control_p1ter.db"
ORDEN_P1TER = "seleccion_control_esq_p1ter.json"
RESUMEN_P1TER = "resumen_control_esq_p1ter.json"

# Candado de una-sola-variable sobre fixtures: sha256 de dopadas_p1bis.json
# tal como quedó sellado en c25273f (aprobación de la autora vigente).
# Reproducción: git show c25273f:data/experiment/esq/control/dopadas_p1bis.json | shasum -a 256
SHA256_DOPADAS_C25273F = (
    "6ae5605148c1e545ab04463a90d81039886b78b7afaf7196ee57f425aa29a7b2")

# Umbrales de P1″ == P1′ (adenda P1″ §1: idénticos, sellados).
UMBRAL_APRIME_TOTAL = rp.UMBRAL_APRIME_TOTAL   # ≥7 de 10
UMBRAL_APRIME_MITAD = rp.UMBRAL_APRIME_MITAD   # ≥3 de 5 por mitad
UMBRAL_C = rp.UMBRAL_C                         # ≤1 de 10


class ClienteControlEsqP1ter(rc.ClienteControlEsq):
    COMPONENT = "esq_control_e1_p1ter"


def _canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, ensure_ascii=False,
                      separators=(",", ":"))


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def cierres_de_adenda() -> tuple[str, str]:
    """Los dos textos de reemplazo, extraídos de la adenda sellada MISMA (no
    de una transcripción): sus dos únicos blockquotes, con las líneas
    envueltas unidas por espacio (semántica markdown de soft-wrap). El orden
    del documento es (i) encabezado del catálogo, (ii) regla 4."""
    txt = ADENDA_P1TER.read_text(encoding="utf-8")
    bloques: list[str] = []
    actual: list[str] = []
    for linea in txt.split("\n"):
        if linea.startswith(">"):
            actual.append(linea.lstrip(">").strip())
        elif actual:
            bloques.append(" ".join(actual))
            actual = []
    if actual:
        bloques.append(" ".join(actual))
    if len(bloques) != 2:
        raise rc.Freno(f"la adenda P1ter tiene {len(bloques)} blockquotes "
                       "(esperaba exactamente 2: los textos (i) y (ii) de §3)")
    return bloques[0], bloques[1]


def sistema_abierto_p1bis() -> str:
    """El system abierto de la corrida P1′ (aditivo, pre-O2), reconstruido.
    verificar_p1ter ancla esta reconstrucción al hash SELLADO de esa corrida
    (cc.PREFIJO_HASH_ABIERTO_P1BIS, verificado en c25273f): no es circular."""
    return prompt_e1.PREFIJO_SISTEMA + prompt_e1.BLOQUE_CANAL_ABIERTO


def hash_prefijo_p1bis_reconstruido() -> str:
    canon = json.dumps(
        {"system": [{"type": "text", "text": sistema_abierto_p1bis(),
                     "cache_control": {"type": "ephemeral"}}],
         "tools": [prompt_e1.TOOL_SCHEMA_E1_CANAL_ABIERTO]},
        sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:12]


def diff_system_abierto() -> str:
    """Diff unificado P1′ → P1″ del system abierto (evidencia del check de
    una sola variable; se pega en el selftest y va al resumen)."""
    return "\n".join(difflib.unified_diff(
        sistema_abierto_p1bis().split("\n"),
        prompt_e1.prefijo_sistema(True).split("\n"),
        fromfile="system_abierto_P1bis", tofile="system_abierto_P1ter",
        lineterm=""))


def verificar_una_variable(fx_path: Path = rp.FIXTURES) -> dict:
    """Check de UNA SOLA VARIABLE (mandato U-ESQ-1e.b + adenda §1):
      - fixtures byte-idénticos por sha256 al valor sellado en c25273f;
      - los dos textos de reemplazo del código == los de la adenda, verbatim;
      - el system abierto de P1′ reconstruido ancla a su hash sellado;
      - system abierto P1″ == P1′ con EXACTAMENTE los dos reemplazos aplicados
        y nada más (los textos de producción ausentes, los nuevos presentes
        exactamente una vez);
      - description del tool y tool schema abierto SIN cambio contra P1′
        (la variable es solo el system);
      - modo cerrado byte-idéntico a producción (candados sellados)."""
    ad_i, ad_ii = cierres_de_adenda()
    sys_p1bis = sistema_abierto_p1bis()
    sys_p1ter = prompt_e1.prefijo_sistema(True)
    reconstruido = (sys_p1bis
                    .replace(prompt_e1.CIERRE_CATALOGO_PROD,
                             prompt_e1.CIERRE_CATALOGO_ABIERTO)
                    .replace(prompt_e1.CIERRE_REGLA4_PROD,
                             prompt_e1.CIERRE_REGLA4_ABIERTO))
    checks = {
        "fixtures_sha256_igual_c25273f": (
            _sha(fx_path.read_text(encoding="utf-8")) == SHA256_DOPADAS_C25273F),
        "texto_i_verbatim_adenda": prompt_e1.CIERRE_CATALOGO_ABIERTO == ad_i,
        "texto_ii_verbatim_adenda": prompt_e1.CIERRE_REGLA4_ABIERTO == ad_ii,
        "p1bis_reconstruido_ancla_hash_sellado": (
            hash_prefijo_p1bis_reconstruido() == cc.PREFIJO_HASH_ABIERTO_P1BIS),
        "cierre_i_prod_una_vez_en_p1bis": (
            sys_p1bis.count(prompt_e1.CIERRE_CATALOGO_PROD) == 1),
        "cierre_ii_prod_una_vez_en_p1bis": (
            sys_p1bis.count(prompt_e1.CIERRE_REGLA4_PROD) == 1),
        "p1ter_es_p1bis_mas_exactamente_dos_reemplazos": sys_p1ter == reconstruido,
        "cierres_prod_ausentes_de_p1ter": (
            prompt_e1.CIERRE_CATALOGO_PROD not in sys_p1ter
            and prompt_e1.CIERRE_REGLA4_PROD not in sys_p1ter),
        "cierres_nuevos_exactamente_una_vez_en_p1ter": (
            sys_p1ter.count(prompt_e1.CIERRE_CATALOGO_ABIERTO) == 1
            and sys_p1ter.count(prompt_e1.CIERRE_REGLA4_ABIERTO) == 1),
        "description_tool_sin_cambio_vs_p1bis": (
            prompt_e1.tool_schema_e1(canal_abierto=True)
            == prompt_e1.TOOL_SCHEMA_E1_CANAL_ABIERTO),
        "cerrado_byte_identico_prefijo": (
            _sha(prompt_e1.PREFIJO_CANONICO) == rp.SHA256_PREFIJO_PROD),
        "cerrado_byte_identico_tool": (
            _sha(_canon(prompt_e1.TOOL_SCHEMA_E1)) == rp.SHA256_TOOL_SCHEMA_PROD),
        "cerrado_namespace_produccion": (
            cliente_e1.namespace_e1(False) == rp.NAMESPACE_PROD),
    }
    if not all(checks.values()):
        raise rc.Freno(f"check de una sola variable FALLÓ: {checks} — no se gasta")
    return checks


def verificar_p1ter(fx: dict, chunk_real: dict) -> dict:
    """Guardas previas a cualquier gasto: las del runner original (hash nuevo,
    namespace particionado, schema abierto, system) + las heredadas de P1′
    (dopadas fuera del universo, cláusulas no sembradas) + el check de una
    sola variable de P1″."""
    guardas = rc.verificar_canal_abierto(chunk_real)   # hash/namespace/schema/system

    universo = cc.cargar_universo()
    sistema_on = prompt_e1.prefijo_sistema(True)
    tool_on_canon = _canon(prompt_e1.tool_schema_e1(canal_abierto=True))
    extra = {
        "namespace_no_relee_p1bis_ni_original": (
            cc.PREFIJO_HASH_ABIERTO_P1BIS not in guardas["namespace"]
            and cc.PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL not in guardas["namespace"]),
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
        raise rc.Freno(f"guardas P1″ fallaron: {extra} — no se gasta")
    una_variable = verificar_una_variable()
    return {**guardas, **extra, "una_sola_variable": una_variable}


def comparacion_pareada_p1bis(seleccion: list[dict],
                              regs_p1ter: dict[str, dict]) -> dict:
    """Comparación dopada-por-dopada (y limpia-por-limpia) contra la corrida
    P1′ persistida: qué emitió cada unidad en cada corrida (esperado /
    otro_canal / nada — la misma clasificación de conteos_p1bis). La lectura
    semántica (¿siguió forzando?) es del reporte, sobre los crudos."""
    regs_p1bis = rc.cargar_jsonl_last_wins(cc.CONTROL_DIR / rp.JSONL_P1BIS)
    conteos_p1bis = rp.conteos_p1bis(seleccion, regs_p1bis)
    conteos_p1ter = rp.conteos_p1bis(seleccion, regs_p1ter)
    por_unidad = {}
    for s in seleccion:
        cid = s["chunk_id"]
        a = conteos_p1bis["detalle_por_unidad"].get(cid, {})
        b = conteos_p1ter["detalle_por_unidad"].get(cid, {})
        d = {"brazo": s["brazo"],
             "p1bis_emite": a.get("emite"), "p1ter_emite": b.get("emite")}
        if s["brazo"] == "A'":
            d["mitad"] = s["mitad"]
            d["p1bis_emitio"] = a.get("emitio")
            d["p1ter_emitio"] = b.get("emitio")
            d["cambio"] = a.get("emitio") != b.get("emitio")
        por_unidad[cid] = d
    return {
        "fuente_p1bis": str(cc.CONTROL_DIR / rp.JSONL_P1BIS),
        "conteos_p1bis_recomputados": {
            "A_prime_hits_total": conteos_p1bis["A_prime"]["hits_total"],
            "C_emiten_tipo_propuesto": conteos_p1bis["C"]["emiten_tipo_propuesto"]},
        "por_unidad": por_unidad,
    }


def resumen_p1ter(seleccion: list[dict], salida: Path, cliente_resumen,
                  corrida_meta, guardas) -> dict:
    regs = rc.cargar_jsonl_last_wins(salida / JSONL_P1TER)
    conteos = rp.conteos_p1bis(seleccion, regs)   # umbrales P1″ == P1′
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
        "unidad": "U-ESQ-1e (O2: cierres neutralizados, adenda P1'')",
        "modelo": cc.MODEL_E1,
        "tarifas_usd_mtok": {**cc.P_E1,
                             "ancla": "reextraccion_v2/corpus_v2/runner_corpus.py:76-78"},
        "guardas": guardas,
        "corrida": corrida_meta,
        "cliente": cliente_resumen,
        "conteos_P1ter": {k: v for k, v in conteos.items()
                          if k != "detalle_por_unidad"},
        "comparacion_pareada_P1bis": comparacion_pareada_p1bis(seleccion, regs),
        "usage_agregado": agg,
        "usage_por_llamada": [{"chunk_id": s["chunk_id"], "brazo": s["brazo"],
                               **(regs[s["chunk_id"]].get("usage") or {})}
                              for s in seleccion if s["chunk_id"] in regs],
        "costo_recomputado_desde_usage_usd": round(cc.costo_usd_desde_usage(agg), 6),
        "formula_costo": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 (USD/MTok); "
                          "tarifas runner_corpus.py:76-78"),
        "recargo_medido_D7_prefijo_p1ter": {
            **recargo,
            "sesgo_declarado": ("pareado contra el usage cerrado de las 20 "
                                "unidades BASE; el texto de las 10 dopadas "
                                "excede al base en su cláusula plantada"),
        },
        "re_presupuesto_esq1_D7": cc.re_presupuesto_esq1(
            recargo, recargo["pref_abierto_medido_tok"]),
        "factores_produccion_recomputados": {k: v for k, v in factores.items()
                                             if k != "agg"},
        "diff_system_abierto_p1bis_a_p1ter": diff_system_abierto(),
        "detalle_por_unidad": conteos["detalle_por_unidad"],
    }
    (salida / RESUMEN_P1TER).write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    return resumen


def persistir_orden_p1ter(seleccion: list[dict], destino: Path) -> Path:
    destino.mkdir(parents=True, exist_ok=True)
    path = destino / ORDEN_P1TER
    doc = {"unidad": "U-ESQ-1e", "adenda": "adenda_prerregistro_esq1_P1ter.md",
           "regla": ("misma selección que P1' (adenda P1'' §1, una sola "
                     "variable): A' = las 10 dopadas de dopadas_p1bis.json "
                     "(sha contra c25273f), C = las 10 limpias de la "
                     "selección sellada del control original, sin re-sorteo"),
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
        description="Re-corrida P1'' del control de ESQ-1 (O2: cierres "
                    "neutralizados; A' dopadas + C, canal abierto)")
    ap.add_argument("--stub", action="store_true")
    ap.add_argument("--salida", type=Path, default=cc.CONTROL_DIR)
    ap.add_argument("--autorizado-tope-parcial", type=float, default=None)
    ap.add_argument("--solo-resumen", action="store_true")
    args = ap.parse_args()

    fx = rp.cargar_fixtures()
    seleccion = rp.seleccion_p1bis(fx)   # misma selección que P1' (adenda §1)
    orden_dir = (args.salida / "orden") if args.stub else cc.ORDEN_DIR
    persistir_orden_p1ter(seleccion, orden_dir)

    if args.solo_resumen:
        r = resumen_p1ter(seleccion, args.salida, None, None, None)
        print(json.dumps(r["conteos_P1ter"], ensure_ascii=False, indent=1))
        return 0

    por_id = rp.por_id_p1bis(fx)
    guardas = verificar_p1ter(fx, por_id[seleccion[-1]["chunk_id"]])
    print(f"[guardas] namespace={guardas['namespace']} | "
          f"prefijo abierto={guardas['prefijo_hash_abierto']} | "
          f"una_sola_variable={all(guardas['una_sola_variable'].values())}",
          flush=True)

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
                  "cualquier gasto. Nada se llamó.")
            return 2
        from dotenv import load_dotenv
        load_dotenv(comun_e1.EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            print(f"ANTHROPIC_API_KEY ausente (esperada en {comun_e1.EVAL_DIR / '.env'})")
            return 1
        cliente = ClienteControlEsqP1ter(
            **cc.P_E1, tope_usd=cc.TOPE_PARCIAL_USD,
            run_label="esq_control_e1_p1ter",
            db_path=DB_P1TER, canal_abierto=True)

    try:
        meta = rc.correr(cliente, seleccion, args.salida, cc.TOPE_PARCIAL_USD,
                         stub=args.stub, por_id=por_id, jsonl_nombre=JSONL_P1TER)
    finally:
        cliente_res = cliente.resumen()
        cliente.close()

    r = resumen_p1ter(seleccion, args.salida, cliente_res, meta, guardas)
    ca = r["conteos_P1ter"]["A_prime"]
    cx = r["conteos_P1ter"]["C"]
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
