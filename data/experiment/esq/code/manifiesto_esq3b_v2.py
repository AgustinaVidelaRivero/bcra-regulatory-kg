"""
manifiesto_esq3b_v2.py — FASE (d) de U-ESQ-3b-v2 ($0): el MANIFIESTO del
freno 1 de la vuelta 2.

Imprime, todo reproducible por este único comando:
  (i)   el diff unificado del prefijo V2 contra el V1, con sha256 de ambos
        textos y los hashes de prefijo (system+tools) que particionan el
        namespace de caché;
  (ii)  la selección persistida de los dos brazos, con conteos, cuotas y sha;
  (iii) la salida VERBATIM del selftest de no-filtración de DOS niveles
        (pre-registro v2 §5);
  (iv)  la estimación de costo contra el tope USD 0,40, calculada desde el
        usage REAL de la vuelta 1 (43 unidades, USD 0,2471,
        `esq3b/reporte_freno_final_esq3b.json`), con la fórmula D2.

No llama a la API, no escribe nada en el repo y no decide nada.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/manifiesto_esq3b_v2.py
"""

from __future__ import annotations

import difflib
import hashlib
import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc       # noqa: E402
import prompt_esq3b_v2 as pr      # noqa: E402
import prompt_esq3b as pr1        # noqa: E402
import no_filtracion_v2 as nf     # noqa: E402

SELECCION = cc.ORDEN_DIR / "seleccion_brazos_esq3b_v2.json"
REPORTE_V1 = cc.ESQ3B_DIR / "reporte_freno_final_esq3b.json"


def diff_prefijo() -> str:
    viejo = pr1.PREFIJO_SISTEMA_RETOCADO.splitlines(keepends=True)
    nuevo = pr.PREFIJO_SISTEMA_V2.splitlines(keepends=True)
    return "".join(difflib.unified_diff(
        viejo, nuevo,
        fromfile="prompt_esq3b.PREFIJO_SISTEMA_RETOCADO (v1, f0a421fb9466)",
        tofile="prompt_esq3b_v2.PREFIJO_SISTEMA_V2 (U-ESQ-3b-v2)",
        n=2))


def diff_tool_schema() -> str:
    viejo = json.dumps(pr1.TOOL_SCHEMA_RETOCADO, ensure_ascii=False,
                       indent=1, sort_keys=True).splitlines(keepends=True)
    nuevo = json.dumps(pr.TOOL_SCHEMA_V2, ensure_ascii=False,
                       indent=1, sort_keys=True).splitlines(keepends=True)
    return "".join(difflib.unified_diff(
        viejo, nuevo, fromfile="TOOL_SCHEMA_RETOCADO (v1)",
        tofile="TOOL_SCHEMA_V2 (U-ESQ-3b-v2)", n=1))


def estimacion_costo(n_unidades: int) -> dict:
    """Estimación anclada en el usage REAL de la vuelta 1 (43 unidades,
    USD 0,2471, esq3b/reporte_freno_final_esq3b.json), escalada por el
    crecimiento medido del prefijo. Sin números inventados: cada factor sale
    de un archivo."""
    r1 = json.loads(REPORTE_V1.read_text(encoding="utf-8"))
    f = r1["costo"]["via_b_db_namespace_propio"]
    n1 = f["n"]
    factor_prefijo = (len(pr.PREFIJO_SISTEMA_V2)
                      / len(pr1.PREFIJO_SISTEMA_RETOCADO))
    in_u = f["input_tokens"] / n1
    out_u = f["output_tokens"] / n1
    cr_u = f["cache_read_tokens"] / n1
    # escenario base: el prefijo crece → crece el cache read; la salida lleva
    # un margen declarado ×1,15 (la vuelta 2 no agrega tipos nuevos donde
    # alojar contenido: las delimitaciones acotan, no expanden).
    margen_salida = 1.15
    agg_base = {"input_tokens": in_u * n_unidades,
                "output_tokens": out_u * margen_salida * n_unidades,
                "cache_read_tokens": cr_u * factor_prefijo * n_unidades,
                "cache_write_tokens": 0}
    costo_lecturas = cc.costo_usd_desde_usage(agg_base)
    # escrituras de caché: techo de 4 escrituras del prefijo entero (corrida
    # corta, secuencial, TTL de 5 minutos) — mismo techo declarado que v1.
    tok_prefijo = cr_u * factor_prefijo
    costo_writes = cc.costo_usd_desde_usage(
        {"cache_write_tokens": 4 * tok_prefijo})
    return {
        "fuente_base": ("esq3b/reporte_freno_final_esq3b.json (43 u, "
                        "USD 0,2471 — costo real de la vuelta 1)"),
        "por_unidad_v1": {"input": round(in_u), "output": round(out_u),
                          "cache_read": round(cr_u)},
        "factor_crecimiento_prefijo_v2_vs_v1": round(factor_prefijo, 4),
        "margen_salida_declarado": margen_salida,
        "n_unidades": n_unidades,
        "costo_lecturas_usd": round(costo_lecturas, 4),
        "costo_escrituras_techo_4_usd": round(costo_writes, 4),
        "estimacion_total_usd": round(costo_lecturas + costo_writes, 4),
        "tope_usd": cc.TOPE_USD,
        "margen_sobre_el_tope": round(
            cc.TOPE_USD - (costo_lecturas + costo_writes), 4),
        "formula": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 (USD/MTok), "
                    "decisiones_caching_extraccion.md:32-42"),
    }


def main() -> int:
    sel = json.loads(SELECCION.read_text(encoding="utf-8"))
    n = sel["objetivo"]["n_unidades"] + sel["regresion_fresca"]["n_unidades"]

    print("=" * 78)
    print("MANIFIESTO DE U-ESQ-3b-v2 — FRENO 1 (pre-registro v2 `40493c9`)")
    print("Estado: fase (e) NO corrida. Gasto a la fecha: USD 0,00.")
    print("=" * 78)

    print("\n## (i) PREFIJO V2 — sellos\n")
    print(f"sha256 texto prefijo V1 (base)  : "
          f"{hashlib.sha256(pr1.PREFIJO_SISTEMA_RETOCADO.encode()).hexdigest()}")
    print(f"sha256 texto prefijo V2         : {pr.PREFIJO_SHA256_V2}")
    print(f"hash prefijo (system+tools) v1  : {pr1.PREFIJO_HASH_RETOCADO}")
    print(f"hash prefijo (system+tools) v2  : {pr.PREFIJO_HASH_V2}")
    print(f"namespace de caché de la vuelta : {cc.namespace_v2()}")
    print(f"db de caché (nueva, gitignorada): "
          f"{cc.DB_V2.relative_to(cc.REPO_DIR)}")
    print(f"longitud: {len(pr1.PREFIJO_SISTEMA_RETOCADO)} → "
          f"{len(pr.PREFIJO_SISTEMA_V2)} caracteres")
    print(f"reemplazos declarados sobre el v1: {len(pr.REEMPLAZOS_V2)} "
          f"({', '.join(n for n, _, _ in pr.REEMPLAZOS_V2)})")

    print("\n## (i.a) DIFF del prefijo de sistema (v1 → v2)\n")
    print(diff_prefijo())
    print("\n## (i.b) DIFF del tool schema (v1 → v2)\n")
    print(diff_tool_schema())

    print("\n## (ii) SELECCIÓN DE BRAZOS (persistida antes de gastar)\n")
    print(f"archivo: {SELECCION.relative_to(cc.REPO_DIR)}")
    print(f"sha256 : {hashlib.sha256(SELECCION.read_bytes()).hexdigest()}")
    print(f"\nBRAZO OBJETIVO — {sel['objetivo']['n_unidades']} unidades "
          f"(brazo base: extracción de la vuelta 1)")
    for u in sel["objetivo"]["unidades"]:
        grupos = ", ".join(sel["objetivo"]["mapa_unidad_grupos"][u["chunk_id"]])
        print(f"  {u['chunk_id']:<26s} {u['to']:<8s} [{grupos}]")
    print(f"\nBRAZO REGRESIÓN FRESCA — {sel['regresion_fresca']['n_unidades']} "
          f"unidades (brazo base: extracción de ESQ-2; pool "
          f"{sel['regresion_fresca']['pool_n']} no fichadas; semilla "
          f"{sel['regresion_fresca']['semilla']})")
    for u in sel["regresion_fresca"]["unidades"]:
        print(f"  {u['chunk_id']:<26s} {u['to']:<8s} {u['tipo_unidad']}")
    print(f"\ncuotas por TO: {sel['regresion_fresca']['cuotas_por_to']}")
    print(f"solapamiento entre brazos: {sel['solapamiento_brazos']}")
    print(f"total de unidades a re-extraer: {n}")

    print("\n## (iii) NO-FILTRACIÓN DE DOS NIVELES — salida verbatim\n")
    res = nf.verificar()
    nf.imprimir(res)
    if not res["verde"]:
        print("\nNO-FILTRACIÓN EN ROJO — la corrida no se autoriza así.")
        return 1

    print("\n## (iv) ESTIMACIÓN DE COSTO contra el tope\n")
    est = estimacion_costo(n)
    print(json.dumps(est, ensure_ascii=False, indent=1))
    if est["estimacion_total_usd"] > cc.TOPE_USD:
        print("\nLA ESTIMACIÓN SUPERA EL TOPE — la corrida no se autoriza así.")
        return 1
    print(f"\nEstimación USD {est['estimacion_total_usd']:.4f} contra tope "
          f"USD {cc.TOPE_USD:.2f} — margen USD "
          f"{est['margen_sobre_el_tope']:.4f}.")
    print("\nGASTO A LA FECHA DE ESTE MANIFIESTO: USD 0,00 (ninguna llamada a "
          "la API salió; los brazos base son extracciones ya persistidas — "
          "vuelta 1 y ESQ-2 — y el gate de pareo doble es read-only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
