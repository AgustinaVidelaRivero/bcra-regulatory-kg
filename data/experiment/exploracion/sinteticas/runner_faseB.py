"""
runner_faseB.py — Corrida de generación de la fase B (autorizada, con tope).

Flujo por sample (§2 y §6 del diseño):
  1. Generación del par literal + anti-léxica (generador.Generador, 2 llamadas).
  2. Puertas mecánicas (validador.Validador: a, b, b_antilexica, c, d).
  3. Checks LLM flaggeados (prompts canónicos de estimacion.py):
       V1 autocontención (literal y anti-léxica, 2 llamadas)
       V2 unicidad del gold (literal, 1 llamada)
       V3 mismo-gold del par (1 llamada)
  4. Veredicto integrado: apto si puertas mecánicas OK y V1/V2/V3 OK.
     Todo descarte con motivo (patrón generacion_u6_registro).

Modos:
  --calibracion   solo los primeros 2 samples de cada estrato (orden
                  determinístico del archivo de samples: EA-001, EA-002,
                  EB-001, ... EE-002) -> out/calibracion_faseB.json y FRENO.
  --resto         los 88 restantes (tras segunda autorización), con
                  re-generación de descartadas (1 reintento por sample, con
                  el registro del intento fallido preservado)
                  -> out/preguntas_faseB.json (incluye los 10 de calibración).
  --selftest      cablea el runner completo con un cliente STUB (0 llamadas
                  reales, gratis) y verifica el pipeline de punta a punta.

El gasto se computa sobre tokens REALES (misses de caché) al precio autorizado
y se corta con tope duro (cliente_faseB.TOPE_USD). Los hits no pagan.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))

from comun import EVAL_DIR, MAPA_5SETS, Quemado, load_kg_raw, solape_lexico  # noqa: E402
from estimacion import (_prompt_validacion_comprensibilidad,  # noqa: E402
                        _prompt_validacion_mismo_gold,
                        _prompt_validacion_unicidad)
from generador import Generador, StubCliente, TokensProhibidos, render_subgrafo  # noqa: E402
from resolucion import AnclaIndex  # noqa: E402
from validador import SOLAPE_UMBRAL, Validador  # noqa: E402

SAMPLES_PATH = AQUI / "out" / "samples.json"
OUT_CALIBRACION = AQUI / "out" / "calibracion_faseB.json"
OUT_FINAL = AQUI / "out" / "preguntas_faseB.json"
N_CALIBRACION_POR_ESTRATO = 2
MAX_REINTENTOS = 1   # re-generación de descartadas: factor 1,6 presupuestado


def _parse_json_obj(crudo: str) -> dict:
    """Parsea un objeto JSON tolerando fences y texto alrededor."""
    t = (crudo or "").strip()
    t = re.sub(r"^```(?:json)?\s*|\s*```$", "", t, flags=re.IGNORECASE).strip()
    try:
        return json.loads(t)
    except json.JSONDecodeError:
        m = re.search(r"\{.*\}", t, flags=re.DOTALL)
        if m:
            return json.loads(m.group(0))
        raise


def _checks_llm(cliente, sample: dict, literal: str, antilexica: str) -> dict:
    """V1/V2/V3 sobre un par generado. Devuelve veredictos parseados."""
    v1_lit = _parse_json_obj(cliente.generar(
        _prompt_validacion_comprensibilidad(literal)))
    v1_anti = _parse_json_obj(cliente.generar(
        _prompt_validacion_comprensibilidad(antilexica)))
    v2 = _parse_json_obj(cliente.generar(
        _prompt_validacion_unicidad(literal, render_subgrafo(sample))))
    v3 = _parse_json_obj(cliente.generar(
        _prompt_validacion_mismo_gold(literal, antilexica)))
    motivos = []
    if not v1_lit.get("autocontenida"):
        motivos.append(f"V1_literal_no_autocontenida: {v1_lit.get('motivo')}")
    if not v1_anti.get("autocontenida"):
        motivos.append(f"V1_antilexica_no_autocontenida: {v1_anti.get('motivo')}")
    if not v2.get("gold_unico"):
        motivos.append(f"V2_gold_no_unico: {v2.get('respuesta_alternativa')}")
    if not v3.get("misma_pregunta"):
        motivos.append(f"V3_par_divergente: {v3.get('diferencia')}")
    return {"v1_literal": v1_lit, "v1_antilexica": v1_anti, "v2": v2, "v3": v3,
            "ok": not motivos, "motivos": motivos}


def procesar_sample(cliente, gen: Generador, val: Validador,
                    sample: dict) -> dict:
    """Genera + valida un sample completo. Un registro por intento."""
    par = gen.generar_par(sample)
    prohibidos = set(par["tokens_prohibidos"])
    mec = val.validar(sample, par["literal"], par["antilexica"], prohibidos)
    llm = _checks_llm(cliente, sample, par["literal"], par["antilexica"])
    motivos = mec["motivos"] + llm["motivos"]
    return {
        "sample_id": sample["sample_id"],
        "estrato": sample["estrato"],
        "sub_estrato": sample["sub_estrato"],
        "literal": par["literal"],
        "antilexica": par["antilexica"],
        "tokens_prohibidos": par["tokens_prohibidos"],
        "solape_literal": solape_lexico(par["literal"], prohibidos),
        "solape_antilexica": solape_lexico(par["antilexica"], prohibidos),
        "gold": sample["gold"],
        "veredicto": "apto" if not motivos else "descartado",
        "motivos": motivos,
        "puertas_mecanicas": mec,
        "checks_llm": llm,
    }


def seleccion_calibracion(samples: list) -> list:
    out = []
    for estrato in ("E-A", "E-B", "E-C", "E-D", "E-E"):
        del_estrato = [s for s in samples if s["estrato"] == estrato]
        out.extend(del_estrato[:N_CALIBRACION_POR_ESTRATO])
    return out


def _preparar(cliente):
    kg_raw = load_kg_raw()
    gen = Generador(cliente, TokensProhibidos(kg_raw))
    val = Validador(AnclaIndex(kg_raw), Quemado(MAPA_5SETS))
    with open(SAMPLES_PATH, encoding="utf-8") as f:
        data = json.load(f)
    return gen, val, data


def correr(cliente, samples: list, reintentos: int = 0,
           registros_previos: list | None = None) -> list:
    """Procesa una lista de samples; opcionalmente reintenta descartados.

    El reintento re-genera el par (la caché exige request distinto: se agrega
    una instrucción de variación con el número de intento al prompt vía
    metadatos del sample — implementado como sufijo del render)."""
    gen, val, _ = _preparar(cliente)
    registros = list(registros_previos or [])
    for s in samples:
        r = procesar_sample(cliente, gen, val, s)
        r["intento"] = 1
        registros.append(r)
        linea = f"  [{r['sample_id']}] {r['veredicto']}"
        if r["motivos"]:
            linea += f" ({'; '.join(r['motivos'])[:100]})"
        if hasattr(cliente, "gasto_usd"):
            linea += f"  gasto=${cliente.gasto_usd:.4f}"
        print(linea, flush=True)
        for k in range(reintentos):
            if registros[-1]["veredicto"] == "apto":
                break
            s2 = json.loads(json.dumps(s))
            s2["metadatos"]["reintento"] = k + 2   # cambia el prompt => cache miss
            s2["subgrafo"]["nodos"][0]["descripcion"] = (
                (s2["subgrafo"]["nodos"][0].get("descripcion") or "")
                + f"\n[reintento {k + 2}: la versión anterior fue descartada por: "
                + "; ".join(registros[-1]["motivos"])[:300] + "]")
            r2 = procesar_sample(cliente, gen, val, s2)
            r2["intento"] = k + 2
            r2["sample_id"] = s["sample_id"]
            registros.append(r2)
            print(f"  [{r2['sample_id']} reintento {k+2}] {r2['veredicto']}",
                  flush=True)
    return registros


def _resumen(registros: list, cliente) -> dict:
    aptos = [r for r in registros if r["veredicto"] == "apto"]
    por_estrato = {}
    for r in aptos:
        por_estrato[r["estrato"]] = por_estrato.get(r["estrato"], 0) + 1
    return {
        "n_registros": len(registros),
        "n_aptos": len(aptos),
        "aptos_por_estrato": por_estrato,
        "gasto": cliente.resumen() if hasattr(cliente, "resumen") else None,
    }


def modo_calibracion(cliente):
    _, _, data = _preparar(cliente)
    subset = seleccion_calibracion(data["samples"])
    print(f"== CALIBRACIÓN: {len(subset)} samples "
          f"({[s['sample_id'] for s in subset]}) ==", flush=True)
    registros = correr(cliente, subset, reintentos=MAX_REINTENTOS)
    payload = {
        "config": {"modo": "calibracion", "modelo": "claude-sonnet-5",
                   "samples": [s["sample_id"] for s in subset],
                   "semilla_samples": data["config"]["semilla"],
                   "solape_umbral": SOLAPE_UMBRAL},
        "registros": registros,
        "resumen": _resumen(registros, cliente),
    }
    OUT_CALIBRACION.parent.mkdir(parents=True, exist_ok=True)
    with OUT_CALIBRACION.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    print(json.dumps(payload["resumen"], ensure_ascii=False, indent=1))
    print(f"-> {OUT_CALIBRACION}")


def modo_resto(cliente):
    _, _, data = _preparar(cliente)
    if not OUT_CALIBRACION.exists():
        raise SystemExit("Falta out/calibracion_faseB.json: corré --calibracion "
                         "primero (freno intermedio obligatorio).")
    with OUT_CALIBRACION.open(encoding="utf-8") as f:
        calibracion = json.load(f)
    hechos = {r["sample_id"] for r in calibracion["registros"]}
    resto = [s for s in data["samples"] if s["sample_id"] not in hechos]
    print(f"== RESTO: {len(resto)} samples ==", flush=True)
    registros = correr(cliente, resto, reintentos=MAX_REINTENTOS,
                       registros_previos=calibracion["registros"])
    payload = {
        "config": {"modo": "completo", "modelo": "claude-sonnet-5",
                   "semilla_samples": data["config"]["semilla"],
                   "solape_umbral": SOLAPE_UMBRAL,
                   "max_reintentos": MAX_REINTENTOS},
        "registros": registros,
        "resumen": _resumen(registros, cliente),
    }
    with OUT_FINAL.open("w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=1)
    print(json.dumps(payload["resumen"], ensure_ascii=False, indent=1))
    print(f"-> {OUT_FINAL}")


def modo_selftest():
    """Cablea el runner completo con stub (0 API). Verifica parseo y flujo."""
    fixtures = {
        "PALABRAS PROHIBIDAS": '{"pregunta": "¿Qué requisitos rigen para el caso reformulado sin la jerga del asunto?"}',
        "auto-contenida bajo ese criterio": '{"autocontenida": true, "motivo": "ok"}',
        "admite OTRA respuesta": '{"gold_unico": true, "respuesta_alternativa": ""}',
        "EXACTAMENTE lo mismo": '{"misma_pregunta": true, "diferencia": ""}',
    }
    stub = StubCliente(
        fixtures=fixtures,
        respuesta_defecto='{"pregunta": "¿Qué establece la normativa aplicable al caso de la fixture para una entidad alcanzada?"}')
    gen, val, data = _preparar(stub)
    subset = seleccion_calibracion(data["samples"])[:3]
    regs = []
    for s in subset:
        regs.append(procesar_sample(stub, gen, val, s))
    ok_estructura = all(
        {"literal", "antilexica", "solape_literal", "veredicto",
         "checks_llm"} <= set(r) for r in regs)
    ok_llm = all(r["checks_llm"]["ok"] for r in regs)
    n_llamadas = len(stub.llamadas)
    ok_llamadas = n_llamadas == len(subset) * 6   # 2 gen + 4 checks
    print(f"selftest runner: estructura={ok_estructura} checks_llm={ok_llm} "
          f"llamadas={n_llamadas} (esperadas {len(subset)*6})")
    ok = ok_estructura and ok_llm and ok_llamadas
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="Runner fase B (generación).")
    modo = ap.add_mutually_exclusive_group(required=True)
    modo.add_argument("--calibracion", action="store_true")
    modo.add_argument("--resto", action="store_true")
    modo.add_argument("--selftest", action="store_true")
    args = ap.parse_args()

    if args.selftest:
        sys.exit(modo_selftest())

    from dotenv import load_dotenv
    load_dotenv(EVAL_DIR / ".env")
    import os
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ANTHROPIC_API_KEY no está seteada "
                         f"(esperada en {EVAL_DIR / '.env'}).")
    from cliente_faseB import ClienteFaseB
    cliente = ClienteFaseB()
    try:
        if args.calibracion:
            modo_calibracion(cliente)
        else:
            modo_resto(cliente)
    finally:
        print("GASTO FINAL:", json.dumps(cliente.resumen(), ensure_ascii=False))
        cliente.close()


if __name__ == "__main__":
    main()
