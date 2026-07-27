#!/usr/bin/env python3
"""Driver del verificador diagnóstico para el escalón 1 (PASO 6).

El runner interno del verificador congelado (`_parse_casos`) solo acepta los
labels históricos "off"/"on"; las trazas del escalón viven bajo labels
`escalon1_r{N}`. Este driver replica el loop del runner (verificador.py:
1113-1122) llamando a `investigar_falla` directamente — el verificador NO se
edita, se importa en modo lectura (patrón "módulo aparte").

Alcance (protocolo §6): SOLO fallas de run_3. Sobre grafo_v2 no se corre.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
EVAL = HERE.parent / "evaluacion"
sys.path.insert(0, str(EVAL))

import verificador  # noqa: E402  (importa loader/harness/pdf_locate read-only)

CASOS = [
    ("escalon1_r1", "run_3", "EV1-023"),
    ("escalon1_r1", "run_3", "EV1-011"),
    ("escalon1_r1", "run_3", "EV1-028"),
]
OUTDIR = HERE / "verificador"


def main():
    from dotenv import load_dotenv
    import os
    import anthropic
    load_dotenv(EVAL / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ANTHROPIC_API_KEY no seteada en evaluacion/.env")
    real = anthropic.Anthropic(max_retries=3)

    OUTDIR.mkdir(parents=True, exist_ok=True)
    kg_cache: dict = {}
    for label, run, qid in CASOS:
        for g, r, q in [(label, run, qid)]:
            assert r == "run_3", "protocolo §6: verificador solo sobre run_3"
        dest = OUTDIR / f"{label}_{run}_{qid}.json"
        print(f"[driver] investigando {label}/{run}/{qid} …", flush=True)
        rec = verificador.investigar_falla(real, label, run, qid,
                                           _kg_cache=kg_cache)
        rec["_meta"]["label"] = label
        dest.write_text(json.dumps(rec, ensure_ascii=False, indent=1),
                        encoding="utf-8")
        det = rec["detectores"]
        print(f"[driver]   → {dest.name} · atribuciones={len(rec['atribuciones'])} · "
              f"formato_invalido={rec['formato_invalido']} · "
              f"tools={det['tool_calls_usadas']}/{det['max_tool_calls']} · "
              f"flags: encuadre={det['flag_encuadre_invertido']} "
              f"contexto={det['flag_contexto']}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
