"""
manifiesto_esq3b.py — FASE (c) de U-ESQ-3b ($0): el MANIFIESTO del freno 1.

Imprime, todo reproducible por este único comando:
  (i)   el diff unificado del prefijo RETOCADO contra el de PRODUCCIÓN, con
        sha256 de los dos textos y los hashes de prefijo (system+tools) que
        particionan el namespace de caché;
  (ii)  la selección persistida de los dos brazos, con conteos y anomalías;
  (iii) la estimación de costo contra el tope USD 1,00, calculada desde el
        usage REAL de ESQ-2 (no de una tarifa inventada), con la fórmula D2.

No llama a la API, no escribe nada en el repo y no decide nada.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/manifiesto_esq3b.py
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

import comun_esq3b as cc      # noqa: E402
import prompt_esq3b as pr     # noqa: E402
import prompt_e1              # noqa: E402

SELECCION = cc.ORDEN_DIR / "seleccion_brazos_esq3b.json"


def diff_prefijo() -> str:
    viejo = prompt_e1.PREFIJO_SISTEMA.splitlines(keepends=True)
    nuevo = pr.PREFIJO_SISTEMA_RETOCADO.splitlines(keepends=True)
    return "".join(difflib.unified_diff(
        viejo, nuevo,
        fromfile="prompt_e1.PREFIJO_SISTEMA (producción)",
        tofile="prompt_esq3b.PREFIJO_SISTEMA_RETOCADO (U-ESQ-3b)",
        n=2))


def diff_tool_schema() -> str:
    viejo = json.dumps(prompt_e1.TOOL_SCHEMA_E1, ensure_ascii=False,
                       indent=1, sort_keys=True).splitlines(keepends=True)
    nuevo = json.dumps(pr.TOOL_SCHEMA_RETOCADO, ensure_ascii=False,
                       indent=1, sort_keys=True).splitlines(keepends=True)
    return "".join(difflib.unified_diff(
        viejo, nuevo, fromfile="TOOL_SCHEMA_E1 (producción)",
        tofile="TOOL_SCHEMA_RETOCADO (U-ESQ-3b)", n=1))


def estimacion_costo(n_unidades: int) -> dict:
    """Estimación anclada en el usage REAL de ESQ-2 (762 unidades, USD 4,1079,
    `cobertura/resumen_cobertura_esq2.json`), escalada por el crecimiento
    medido del prefijo. Sin números inventados: cada factor sale de un archivo."""
    r2 = json.loads((cc.COBERTURA_DIR / "resumen_cobertura_esq2.json"
                     ).read_text(encoding="utf-8"))
    f = r2["filas_db_namespace_propio"]
    n2 = f["n"]
    factor_prefijo = (len(pr.PREFIJO_SISTEMA_RETOCADO)
                      / len(prompt_e1.PREFIJO_SISTEMA))
    # por unidad, de ESQ-2
    in_u = f["input_tokens"] / n2
    out_u = f["output_tokens"] / n2
    cr_u = f["cache_read_tokens"] / n2
    cw_total_2 = f["cache_write_tokens"]
    # escenario base: el prefijo crece → crece el cache read; la salida crece
    # porque hay tres tipos más donde alojar contenido (margen ×1,3, declarado).
    margen_salida = 1.30
    agg_base = {"input_tokens": in_u * n_unidades,
                "output_tokens": out_u * margen_salida * n_unidades,
                "cache_read_tokens": cr_u * factor_prefijo * n_unidades,
                "cache_write_tokens": 0}
    costo_lecturas = cc.costo_usd_desde_usage(agg_base)
    # escrituras de caché: ESQ-2 pagó `n_escrituras` writes en 762 unidades; acá
    # se toma un techo de 4 escrituras del prefijo entero (corrida corta,
    # secuencial, TTL de 5 minutos).
    tok_prefijo = cr_u * factor_prefijo
    costo_writes = cc.costo_usd_desde_usage(
        {"cache_write_tokens": 4 * tok_prefijo})
    return {
        "fuente_base": "cobertura/resumen_cobertura_esq2.json (762 u, USD 4,1079)",
        "por_unidad_esq2": {"input": round(in_u), "output": round(out_u),
                            "cache_read": round(cr_u)},
        "escrituras_cache_esq2_total_tokens": cw_total_2,
        "factor_crecimiento_prefijo": round(factor_prefijo, 4),
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
    n = sel["objetivo"]["n_unidades"] + sel["regresion"]["n_unidades"]

    print("=" * 78)
    print("MANIFIESTO DE U-ESQ-3b — post freno 1 APROBADO y Adenda 1 `f1fe0d8`")
    print("Estado: fase (d) NO corrida. Gasto a la fecha: USD 0,00.")
    print("=" * 78)

    print("\n## (i) PREFIJO RETOCADO — sellos\n")
    print(f"sha256 texto prefijo PRODUCCIÓN : "
          f"{hashlib.sha256(prompt_e1.PREFIJO_SISTEMA.encode()).hexdigest()}")
    print(f"sha256 texto prefijo RETOCADO   : {pr.PREFIJO_SHA256_RETOCADO}")
    print(f"hash prefijo (system+tools) producción : "
          f"{prompt_e1.prefijo_hash(False)}")
    print(f"hash prefijo (system+tools) retocado   : {pr.PREFIJO_HASH_RETOCADO}")
    print(f"namespace de caché de la unidad        : {cc.namespace_esq3b()}")
    print(f"db de caché (nueva, gitignorada)       : "
          f"{cc.DB_ESQ3B.relative_to(cc.REPO_DIR)}")
    print(f"longitud: {len(prompt_e1.PREFIJO_SISTEMA)} → "
          f"{len(pr.PREFIJO_SISTEMA_RETOCADO)} caracteres")
    print("\nDominio de establecida_en — decisión de AUTORA (Adenda 1 §1):")
    for k, v in pr.DECISIONES_DECLARADAS.items():
        print(f"  - {k}: {v}")

    print("\n## (i.a) DIFF del prefijo de sistema\n")
    print(diff_prefijo())
    print("\n## (i.b) DIFF del tool schema\n")
    print(diff_tool_schema())

    print("\n## (ii) SELECCIÓN DE BRAZOS (persistida antes de gastar)\n")
    print(f"archivo: {SELECCION.relative_to(cc.REPO_DIR)}")
    print(f"sha256 : {hashlib.sha256(SELECCION.read_bytes()).hexdigest()}")
    print(f"\nBRAZO OBJETIVO — {sel['objetivo']['n_unidades']} unidades")
    for u in sel["objetivo"]["unidades"]:
        rets = ", ".join(sel["objetivo"]["mapa_ficha_retoque"][u["chunk_id"]])
        print(f"  f.{u['n_ficha']:>2}  {u['chunk_id']:<26s} {u['to']:<8s} "
              f"[{rets}]")
    print(f"\nBRAZO REGRESIÓN — {sel['regresion']['n_unidades']} unidades "
          f"(objetivo del pre-registro §3: 35)")
    for u in sel["regresion"]["unidades"]:
        print(f"  f.{u['n_ficha']:>2}  {u['chunk_id']:<26s} {u['to']:<8s} "
              f"q1={u['q1_esq2']:<11s} q2={u['q2_esq2']:<8s} "
              f"{u['origen_muestra_esq2']}")
    print(f"\nsolapamiento entre brazos: {sel['solapamiento_brazos']}")
    print(f"total de unidades a re-extraer: {n}")
    print("\nR8 (derivación mecánica):")
    r8 = sel["r8_derivacion"]
    print(f"  unidades: {r8['unidades']}")
    print(f"  tripletas aplica_a con firma_invalida: "
          f"{r8['tripletas_aplica_a_firma_invalida']}")
    print(f"  firma_invalida de cualquier predicado en las 75 fichas: "
          f"{r8['conteo_transversal_firma_invalida_75_fichas']}")
    print(f"  sujeto_extremo_invalido en las 75 fichas: "
          f"{r8['conteo_transversal_sujeto_extremo_invalido_75_fichas']}")
    for a in sel["anomalias_declaradas"]:
        print(f"\nANOMALÍA DECLARADA: {a}")

    print("\n## (iii) ESTIMACIÓN DE COSTO contra el tope\n")
    est = estimacion_costo(n)
    print(json.dumps(est, ensure_ascii=False, indent=1))
    if est["estimacion_total_usd"] > cc.TOPE_USD:
        print("\nLA ESTIMACIÓN SUPERA EL TOPE — la corrida no se autoriza así.")
        return 1
    print(f"\nEstimación USD {est['estimacion_total_usd']:.4f} contra tope "
          f"USD {cc.TOPE_USD:.2f} — margen USD "
          f"{est['margen_sobre_el_tope']:.4f}.")
    print("\nGASTO A LA FECHA DE ESTE MANIFIESTO: USD 0,00 (ninguna llamada a "
          "la API salió; el brazo base son las extracciones ya persistidas de "
          "ESQ-2 y el gate de pareo es read-only).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
