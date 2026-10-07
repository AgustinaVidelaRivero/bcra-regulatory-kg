"""
c0b_api.py — U-COMP-E1, etapa C0, punto (b). USD 0: ninguna llamada a messages.create; solo la lista de modelos
(GET /v1/models), la ficha de cada modelo y el conteo de tokens (POST /v1/messages/count_tokens, sin costo).

Qué hace (mandato docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md, firmado en cbcb823, etapa C0 (b) y tabla BRAZOS):
  1. Disponibilidad para la cuenta de claude-sonnet-5-5 (brazo S) y claude-opus-5-5 (brazo O), y de claude-haiku-4-5
     (brazo H): client.models.list y client.models.retrieve; se guarda la ficha tal cual.
  2. Conteo de tokens, por brazo, del pedido adaptado de cada una de las 87 unidades de unidades.json (C0 (a)):
       H: el pedido de E1 del perfil r2b tal cual (temperature 0, tool_choice forzado, max_tokens 8.192);
       S: sin temperature; tool_choice auto; thinking between_tools; max_tokens 16.384;
       O: sin temperature; tool_choice auto; output_config.effort low; max_tokens 16.384.
     count_tokens no recibe max_tokens ni temperature (no son parámetros del conteo); recibe model, system (con su
     cache_control), tools, messages, tool_choice y thinking u output_config. Más un conteo del prefijo con un mensaje
     mínimo por brazo. Si la API rechaza un pedido, el error se guarda tal cual. Cada respuesta se persiste completa
     (model_dump) en conteo_tokens_c0.jsonl; de la primera llamada de cada modelo se guardan los encabezados de límites.
  3. Estimación de costo de las cuatro corridas (S×2, O×2) con la fórmula de caching (decisión 2 de
     docs/decisiones_caching_extraccion.md): escritura del prefijo en la primera llamada de cada corrida, lectura en las
     86 siguientes (corridas en serie, decisión 4), entrada variable a precio base, salida estimada = tokens de salida
     del intento 0 de Haiku × factor del tokenizador medido en la entrada. Contra el tope de la decisión 3 (USD 35) y
     contra el «≤ 25» que quedó escrito en C0 (b).

La clave de la API se carga de --env (python-dotenv) y no se imprime ni se escribe. Corre sobre una COPIA del repo
(CLAUDE.md §4.l) con PYTHONDONTWRITEBYTECODE=1 y python -B:
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c0/c0b_api.py --env <repo>/data/experiment/evaluacion/.env \
      --unidades DIR/unidades.json --intento0 DIR/intento0_haiku.jsonl --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e1_extractor"))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import llm_cache as lc  # noqa: E402 — solo canonical_request, para identificar cada pedido
import perfil_e1  # noqa: E402

PREFIJO = "322c5a23e9b7"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
SALIDA_R2B = REX / "corpus_tanda0" / "salida_r2b"
MODELOS = {"H": "claude-haiku-4-5", "S": "claude-sonnet-5-5", "O": "claude-opus-5-5"}
MAX_TOKENS_ADAPTADO = 16384
# Precios por millón de tokens (entrada, salida, escritura de caché de 5 minutos, lectura de caché): los del borrador
# P6 (docs/mandatos/UPROMPT_R2_P6_exploracion_modelo_E1.md, páginas de cada modelo consultadas el 05/10/2026) y de la
# tabla COSTO del mandato; coinciden con la tabla de modelos de la skill claude-api (caché del 25/09/2026).
PRECIOS = {"H": {"in": 1.00, "out": 5.00, "cw": 1.25, "cr": 0.10},
           "S": {"in": 2.00, "out": 10.00, "cw": 2.50, "cr": 0.20},
           "O": {"in": 4.00, "out": 20.00, "cw": 5.00, "cr": 0.20}}
TOPE_DECISION_3 = 35.0
UMBRAL_TEXTO_C0B = 25.0
MARGEN = 0.15
CORRIDAS = {"S": 2, "O": 2}
ESTIMACION_MANDATO = {"corrida_S": 4.08, "corrida_O": 8.16, "cuatro_corridas": 24.5, "con_margen": 28.2}


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def chunks_de(to: str) -> dict:
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    out = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    p = SALIDA_R2B / to / "particiones_por_corte.json"
    if p.exists():
        for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                base = dict(out[cid])
                base.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                out[parte["id"]] = base
    return out


def pedido_adaptado(perfil, chunk: dict, brazo: str) -> dict:
    """El pedido de E1 del perfil r2b y, en S y O, solo lo que cambia la tabla BRAZOS del mandato."""
    kw = perfil.build_request_kwargs(chunk, model=MODELOS[brazo])
    if brazo == "H":
        return kw
    kw.pop("temperature", None)
    kw["tool_choice"] = {"type": "auto"}
    kw["max_tokens"] = MAX_TOKENS_ADAPTADO
    if brazo == "S":
        kw["thinking"] = {"type": "between_tools"}
    else:
        kw["output_config"] = {"effort": "low"}
    return kw


def kwargs_conteo(kw: dict) -> dict:
    """Lo que recibe count_tokens: todo el pedido salvo max_tokens y temperature (no son parámetros del conteo)."""
    return {k: v for k, v in kw.items() if k not in ("max_tokens", "temperature")}


def error_tal_cual(e) -> dict:
    d = {"tipo": type(e).__name__, "mensaje": str(e)}
    for attr in ("status_code", "body"):
        if hasattr(e, attr):
            v = getattr(e, attr)
            d[attr] = v if isinstance(v, (int, str, dict, list, type(None))) else str(v)
    rid = getattr(getattr(e, "response", None), "headers", {}) or {}
    if rid:
        d["request_id"] = rid.get("request-id")
    return d


def contar(client, kw_c: dict, con_encabezados: bool):
    """count_tokens con reintentos ante 429/5xx/red; un 400 se devuelve como error tal cual."""
    import anthropic  # noqa: PLC0415
    esperas = (5, 15, 30, 60, 120)
    for i in range(len(esperas) + 1):
        t0 = time.time()
        try:
            if con_encabezados:
                raw = client.messages.with_raw_response.count_tokens(**kw_c)
                enc = {k: v for k, v in raw.headers.items() if k.lower().startswith("anthropic-ratelimit") or k.lower() == "request-id"}
                resp = raw.parse()
            else:
                enc, resp = None, client.messages.count_tokens(**kw_c)
            return {"input_tokens": resp.input_tokens, "crudo": resp.model_dump(mode="json"), "segundos": round(time.time() - t0, 3),
                    "encabezados": enc, "error": None, "intentos": i + 1}
        except anthropic.BadRequestError as e:
            return {"input_tokens": None, "crudo": None, "segundos": round(time.time() - t0, 3), "encabezados": None,
                    "error": error_tal_cual(e), "intentos": i + 1}
        except (anthropic.RateLimitError, anthropic.InternalServerError, anthropic.APIConnectionError, anthropic.APITimeoutError) as e:
            if i == len(esperas):
                return {"input_tokens": None, "crudo": None, "segundos": round(time.time() - t0, 3), "encabezados": None,
                        "error": error_tal_cual(e), "intentos": i + 1}
            ra = getattr(getattr(e, "response", None), "headers", {}) or {}
            espera = esperas[i]
            try:
                espera = max(espera, int(ra.get("retry-after", "0")))
            except ValueError:
                pass
            print(f"  {type(e).__name__}: espera {espera} s", flush=True)
            time.sleep(espera)
        except anthropic.APIStatusError as e:
            return {"input_tokens": None, "crudo": None, "segundos": round(time.time() - t0, 3), "encabezados": None,
                    "error": error_tal_cual(e), "intentos": i + 1}


def wilson_no_aplica():
    return None


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", type=Path, required=True)
    ap.add_argument("--unidades", type=Path, required=True)
    ap.add_argument("--intento0", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--brazos", type=str, default="H,S,O")
    a = ap.parse_args()
    a.salida.mkdir(parents=True, exist_ok=True)
    from dotenv import load_dotenv  # noqa: PLC0415
    load_dotenv(a.env)              # la clave no se imprime ni se escribe
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ANTHROPIC_API_KEY ausente en el entorno tras cargar --env")
    import anthropic  # noqa: PLC0415
    client = anthropic.Anthropic(max_retries=0)  # los reintentos los hace contar(), para registrarlos

    perfil = perfil_e1.perfil("r2b")
    if perfil.prefijo_hash != PREFIJO:
        raise SystemExit(f"el perfil r2b da el prefijo {perfil.prefijo_hash}, no {PREFIJO}")
    unidades = json.loads(a.unidades.read_text(encoding="utf-8"))["unidades"]
    intento0 = {}
    for x in a.intento0.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            intento0[r["chunk_id"]] = r
    chunks: dict = {}
    for to in sorted({u["to"] for u in unidades}):
        chunks.update(chunks_de(to))
    brazos = [b.strip() for b in a.brazos.split(",") if b.strip()]

    # 1. Modelos.
    modelos = {"cuando_utc": ahora(), "lista": [], "fichas": {}, "disponibles": {}}
    try:
        for m in client.models.list(limit=100):
            modelos["lista"].append(m.model_dump(mode="json"))
    except Exception as e:  # noqa: BLE001 — se guarda tal cual
        modelos["error_lista"] = error_tal_cual(e)
    ids_lista = {m.get("id") for m in modelos["lista"]}
    for b, mid in MODELOS.items():
        modelos["disponibles"][mid] = {"en_lista": mid in ids_lista}
        try:
            modelos["fichas"][mid] = client.models.retrieve(mid).model_dump(mode="json")
            modelos["disponibles"][mid]["retrieve"] = "ok"
        except Exception as e:  # noqa: BLE001
            modelos["disponibles"][mid]["retrieve"] = error_tal_cual(e)
    (a.salida / "modelos_c0.json").write_text(json.dumps(modelos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"modelos": modelos["disponibles"], "n_lista": len(modelos["lista"])}, ensure_ascii=False), flush=True)

    # 2. Conteo de tokens.
    jsonl = a.salida / "conteo_tokens_c0.jsonl"
    hechos = {}
    if jsonl.exists():
        for x in jsonl.read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                if r.get("error") is None:
                    hechos[(r["brazo"], r["chunk_id"])] = r
    conteos: dict = {b: {} for b in brazos}
    encabezados: dict = {}
    for b in brazos:
        print(f"[{b}] {MODELOS[b]}", flush=True)
        primera = True
        # prefijo con un mensaje mínimo
        kw0 = pedido_adaptado(perfil, chunks[unidades[0]["chunk_id"]], b)
        kw0["messages"] = [{"role": "user", "content": "."}]
        items = [("__prefijo__", kw0)] + [(u["chunk_id"], pedido_adaptado(perfil, chunks[u["chunk_id"]], b)) for u in unidades]
        rechazado_prefijo = False
        for cid, kw in items:
            if (b, cid) in hechos:
                conteos[b][cid] = hechos[(b, cid)]
                continue
            kw_c = kwargs_conteo(kw)
            r = contar(client, kw_c, con_encabezados=primera)
            primera = False
            if r["encabezados"]:
                encabezados[MODELOS[b]] = r["encabezados"]
            reg = {"brazo": b, "modelo": MODELOS[b], "chunk_id": cid, "cuando_utc": ahora(),
                   "pedido_sin_prefijo_ni_mensaje": {k: v for k, v in kw.items() if k not in ("system", "tools", "messages")},
                   "sha256_pedido_canonico": hashlib.sha256(lc.canonical_request(kw).encode("utf-8")).hexdigest(),
                   "sha256_conteo_canonico": hashlib.sha256(lc.canonical_request(kw_c).encode("utf-8")).hexdigest(),
                   "parametros_del_conteo": sorted(kw_c.keys()), **r}
            with jsonl.open("a", encoding="utf-8") as f:
                f.write(json.dumps(reg, ensure_ascii=False) + "\n")
            conteos[b][cid] = reg
            if r["error"] is not None:
                print(f"  {cid}: ERROR {r['error'].get('tipo')} {str(r['error'].get('mensaje'))[:200]}", flush=True)
                if cid == "__prefijo__":
                    rechazado_prefijo = True
                elif rechazado_prefijo:
                    # el prefijo y la primera unidad rechazados: el brazo no acepta el pedido; se deja constancia y no se
                    # repite el mismo error 86 veces
                    print(f"  [{b}] pedido rechazado en el prefijo y en la primera unidad: se interrumpe el brazo", flush=True)
                    break
            else:
                rechazado_prefijo = False
            time.sleep(0.2)

    # 3. Agregados y estimación.
    def tot(b):
        return sum(r["input_tokens"] for cid, r in conteos[b].items() if cid != "__prefijo__" and r["input_tokens"] is not None)

    def n_ok(b):
        return sum(1 for cid, r in conteos[b].items() if cid != "__prefijo__" and r["input_tokens"] is not None)

    agreg = {"cuando_utc": ahora(), "unidades": len(unidades), "por_brazo": {}}
    haiku_out = {u["chunk_id"]: intento0[u["chunk_id"]]["usage"]["output_tokens"] for u in unidades}
    haiku_in_medido = {u["chunk_id"]: intento0[u["chunk_id"]]["usage"] for u in unidades}
    for b in brazos:
        pre = conteos[b].get("__prefijo__", {}).get("input_tokens")
        por_u = {cid: r["input_tokens"] for cid, r in conteos[b].items() if cid != "__prefijo__"}
        errores = {cid: r["error"] for cid, r in conteos[b].items() if r["error"] is not None}
        var = {cid: (t - pre) if (t is not None and pre is not None) else None for cid, t in por_u.items()}
        agreg["por_brazo"][b] = {"modelo": MODELOS[b], "prefijo_con_mensaje_minimo": pre, "contadas": n_ok(b),
                                 "errores": len(errores), "errores_detalle": errores,
                                 "total_entrada": tot(b) if n_ok(b) else None,
                                 "variable_total": sum(v for v in var.values() if v is not None) if pre is not None else None,
                                 "variable_min_max": ([min(v for v in var.values() if v is not None), max(v for v in var.values() if v is not None)]
                                                      if pre is not None and any(v is not None for v in var.values()) else None),
                                 "por_unidad": por_u}
    if "H" in brazos and n_ok("H"):
        cr = {u["chunk_id"]: haiku_in_medido[u["chunk_id"]]["cache_read_tokens"] for u in unidades}
        inp = {u["chunk_id"]: haiku_in_medido[u["chunk_id"]]["input_tokens"] for u in unidades}
        agreg["haiku_medido_en_la_corrida"] = {"cache_read_valores": sorted(set(cr.values())),
                                               "variable_total_medida": sum(inp.values()),
                                               "variable_total_contada": agreg["por_brazo"]["H"]["variable_total"],
                                               "nota": "la corrida r2b midió cache_read (prefijo) + input_tokens (variable) por unidad; el "
                                                       "conteo de H repite la entrada con el mismo tokenizador"}
    factores = {}
    for b in ("S", "O"):
        if b in brazos and "H" in brazos and n_ok(b) and n_ok("H"):
            comunes = [cid for cid in agreg["por_brazo"][b]["por_unidad"] if agreg["por_brazo"][b]["por_unidad"][cid] is not None
                       and agreg["por_brazo"]["H"]["por_unidad"].get(cid) is not None]
            tb = sum(agreg["por_brazo"][b]["por_unidad"][c] for c in comunes)
            th = sum(agreg["por_brazo"]["H"]["por_unidad"][c] for c in comunes)
            factores[b] = {"unidades_comunes": len(comunes), "entrada_total_brazo": tb, "entrada_total_haiku": th,
                           "factor": round(tb / th, 4) if th else None}
    agreg["factor_tokenizador_entrada"] = factores
    agreg["haiku_salida_intento0"] = {"total": sum(haiku_out.values()), "max": max(haiku_out.values()), "min": min(haiku_out.values())}

    est = {"cuando_utc": ahora(), "precios_por_mtok": PRECIOS, "formula": "escritura del prefijo × precio de escritura (1 vez por corrida) + "
           "lectura del prefijo × precio de lectura (86 veces) + entrada variable × precio base + salida estimada × precio de salida; "
           "salida estimada = salida del intento 0 de Haiku × factor del tokenizador medido en la entrada (supuesto: la salida se "
           "infla como la entrada); escenario B: la salida de O lleva además un 50 % por el pensamiento con effort low (supuesto, como "
           "en P6); techo teórico: cada unidad agota max_tokens 16.384",
           "supuestos_no_medidos": ["la salida de S y O se infla como la entrada", "el pensamiento de O con effort low no se midió",
                                    "cada corrida de 87 unidades entra en la ventana de 5 minutos de la caché de prompts entre llamadas "
                                    "consecutivas (corridas en serie, decisión 4)"],
           "por_brazo": {}}
    total_a = total_b = total_techo = 0.0
    for b in ("S", "O"):
        if b not in brazos or not n_ok(b):
            continue
        p = PRECIOS[b]
        pre = agreg["por_brazo"][b]["prefijo_con_mensaje_minimo"]
        var = agreg["por_brazo"][b]["variable_total"]
        n = agreg["por_brazo"][b]["contadas"]
        f = (factores.get(b) or {}).get("factor") or 1.3
        out_est = sum(haiku_out.values()) * f
        c_pre = (pre * p["cw"] + (n - 1) * pre * p["cr"]) / 1e6
        c_var = var * p["in"] / 1e6
        c_out = out_est * p["out"] / 1e6
        corrida_a = c_pre + c_var + c_out
        corrida_b = corrida_a + (0.5 * c_out if b == "O" else 0.0)
        techo = c_pre + c_var + n * MAX_TOKENS_ADAPTADO * p["out"] / 1e6
        est["por_brazo"][b] = {"modelo": MODELOS[b], "unidades_contadas": n, "prefijo_tokens": pre, "variable_tokens": var,
                               "factor_salida": f, "salida_estimada_tokens": round(out_est),
                               "costo_prefijo_por_corrida": round(c_pre, 4), "costo_variable_por_corrida": round(c_var, 4),
                               "costo_salida_por_corrida": round(c_out, 4),
                               "corrida_escenario_A": round(corrida_a, 4), "corrida_escenario_B": round(corrida_b, 4),
                               "corrida_techo_teorico": round(techo, 4), "corridas": CORRIDAS[b],
                               "total_A": round(corrida_a * CORRIDAS[b], 4), "total_B": round(corrida_b * CORRIDAS[b], 4),
                               "total_techo": round(techo * CORRIDAS[b], 4)}
        total_a += corrida_a * CORRIDAS[b]
        total_b += corrida_b * CORRIDAS[b]
        total_techo += techo * CORRIDAS[b]
    est["cuatro_corridas"] = {"escenario_A": round(total_a, 4), "escenario_A_con_margen_15": round(total_a * (1 + MARGEN), 4),
                              "escenario_B": round(total_b, 4), "escenario_B_con_margen_15": round(total_b * (1 + MARGEN), 4),
                              "techo_teorico": round(total_techo, 4),
                              "tope_decision_3": TOPE_DECISION_3, "umbral_escrito_en_C0_b": UMBRAL_TEXTO_C0B,
                              "pasa_tope_35_escenario_B_con_margen": total_b * (1 + MARGEN) > TOPE_DECISION_3,
                              "pasa_25_escenario_B_con_margen": total_b * (1 + MARGEN) > UMBRAL_TEXTO_C0B,
                              "estimacion_del_mandato": ESTIMACION_MANDATO}
    (a.salida / "conteo_tokens_c0.json").write_text(json.dumps({**agreg, "encabezados_limites": encabezados}, ensure_ascii=False, indent=1) + "\n",
                                                   encoding="utf-8")
    (a.salida / "estimacion_costo_c0.json").write_text(json.dumps(est, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"por_brazo": {b: {k: v for k, v in d.items() if k != "por_unidad" and k != "errores_detalle"} for b, d in agreg["por_brazo"].items()},
                      "factores": factores, "estimacion": est["cuatro_corridas"], "encabezados": encabezados}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
