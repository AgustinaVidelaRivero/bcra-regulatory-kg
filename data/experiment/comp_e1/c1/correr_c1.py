"""
correr_c1.py — U-COMP-E1, C1: E1 de un brazo (S u O) en una corrida (1 o 2) sobre las 87 unidades selladas, sin E3, sin
ratchet y sin lectura. Una ejecución por corrida, en serie (S1, S2, O1, O2; decisión 4 del «seguí»).

Por unidad: el pedido adaptado (comun_c1.pedido_adaptado, comprobado contra el sha256 que C0 contó antes de la primera
llamada), la respuesta por cliente_c1.ClienteC1 (CachingClient, base propia), y las reglas del pedido (:46):
  - corte (stop_reason max_tokens): UN reintento con max_tokens 40.960 por transmisión; si vuelve a cortar, error
    `max_tokens_hit_tras_reintento` (sin partición ni tercer escalón);
  - respuesta sin llamada a la herramienta, o mal formada (validador_e1 rechaza la unidad entera: salida_no_parseable,
    salida_no_dict, entities_o_relations_invalidos): UN reintento igual (el mismo pedido, con el techo que produjo la
    salida) en el namespace -r1; si vuelve mal o sin herramienta, error `<causa>_tras_reintento` (sin reparación
    determinística: no es una corrida del pipeline);
  - stop_reason refusal: se registra con stop_details y no se reintenta (como en P6).
De cada unidad quedan: todas las llamadas (clave, namespace, stop_reason, usage, costo, segundos, id), la salida final
(tool_input crudo), la validación del pipeline (validador_e1.validar_salida con el esquema r2b) y la de la forma r2
(validador_r2.validar, con el tramo de cada entidad y omisión verificado por código contra el texto propio y heredado),
el motivo de forma, los reintentos, y el costo real por la fórmula de caching (D2). Registro append-only, reanudable.

  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c1/correr_c1.py --brazo S --corrida 1 \
      --env <repo>/data/experiment/evaluacion/.env --salida DIR --autorizado-tope 35
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_c1 as C  # noqa: E402
import cliente_c1 as CL  # noqa: E402
import validador_e1  # noqa: E402
import validador_r2  # noqa: E402
from pydantic import ValidationError  # noqa: E402

ERROR_CORTE = "max_tokens_hit_tras_reintento"
MAX_ERRORES_CONSECUTIVOS = 5


def llamar(cliente: CL.ClienteC1, kwargs: dict, doc: str, sufijo: str = "", esperas=(20, 60, 180)):
    """Reintento ante errores transitorios de la API (la corrida es desatendida); TopeExcedido no se reintenta."""
    ultimo = None
    for i in range(len(esperas)):
        try:
            return cliente.create(kwargs, doc, sufijo=sufijo), None
        except CL.TopeExcedido:
            raise
        except ValidationError as e:
            # No transitorio: el SDK 0.100.0 no reconstruye una respuesta con un valor que no conoce (p. ej. una
            # categoría de refusal fuera de «cyber» y «bio») en los caminos que validan estricto (transmisión, hit).
            return None, f"ValidationError (respuesta no reconstruible por el SDK): {str(e)[:500]}"
        except Exception as e:  # noqa: BLE001 — transitorios de red o de la API
            ultimo = f"{type(e).__name__}: {e}"
            print(f"  error API ({doc}, intento {i + 1}/{len(esperas)}): {ultimo[:300]}", flush=True)
            if i < len(esperas) - 1:
                time.sleep(esperas[i])
    return None, ultimo


def validar(ti, chunk: dict, perfil) -> tuple[dict | None, dict | None, str | None]:
    if ti is None:
        return None, None, None
    val_e1 = validador_e1.validar_salida(ti, chunk, esquema=perfil.esquema).as_dict()
    val_r2 = validador_r2.validar(ti, chunk, forma="r2")
    return val_e1, val_r2, C.motivo_forma_e1(val_e1)


def extraer(cliente: CL.ClienteC1, chunk: dict, kw: dict, perfil) -> dict:
    """Una unidad por las reglas del pedido; devuelve el registro completo."""
    cid, doc = chunk["id"], chunk["archivo"]
    reg: dict = {"chunk_id": cid, "brazo": cliente.brazo, "corrida": cliente.corrida, "modelo": C.MODELOS[cliente.brazo],
                 "etiqueta": cliente.etiqueta, "sha256_pedido_canonico": C.sha_pedido(kw), "cuando_utc": C.ahora(),
                 "llamadas": [], "error": None, "reintento_corte": None, "reintento_forma": None,
                 "marca_intento0_haiku": C.MARCAS_INTENTO0_HAIKU.get(cid)}

    def registrar_llamada(camino: str, info: dict, resp):
        r = C.resumen_respuesta(resp)
        reg["llamadas"].append({"camino": camino, **info, **{k: v for k, v in r.items() if k != "tool_input_crudo"}})
        return r

    par, err = llamar(cliente, kw, doc)
    if par is None:
        reg.update({"error": f"api_error: {err}", "stop_reason": None, "usage": None, "tool_input_crudo": None,
                    "validacion_e1": None, "validacion_r2": None, "motivo_forma": None})
        return cerrar(reg)
    resp, info = par
    r = registrar_llamada("base", info, resp)
    kw_vigente = kw
    # 1. Corte: un reintento a 40.960 con transmisión.
    if r["stop_reason"] == "max_tokens":
        kw2 = dict(kw, max_tokens=C.MAX_TOKENS_REINTENTO_CORTE)
        par2, err2 = llamar(cliente, kw2, doc)
        reg["reintento_corte"] = {"max_tokens_reintento": C.MAX_TOKENS_REINTENTO_CORTE, "intento_1": r}
        if par2 is None:
            reg.update({"error": f"api_error_en_reintento_corte: {err2}", "stop_reason": r["stop_reason"], "usage": r["usage"],
                        "tool_input_crudo": r["tool_input_crudo"], "validacion_e1": None, "validacion_r2": None, "motivo_forma": None})
            return cerrar(reg)
        resp, info = par2
        r = registrar_llamada("reintento_corte", info, resp)
        kw_vigente = kw2
        if r["stop_reason"] == "max_tokens":
            reg["error"] = ERROR_CORTE
    # 2. Rechazo del modelo: se registra, no se reintenta.
    if reg["error"] is None and r["stop_reason"] == "refusal":
        reg["error"] = "refusal"
    ti = r["tool_input_crudo"]
    val_e1 = val_r2 = motivo = None
    if reg["error"] is None:
        val_e1, val_r2, motivo = validar(ti, chunk, perfil)
        causa = "sin_herramienta" if ti is None else ("mal_formada" if motivo else None)
        # 3. Sin herramienta o mal formada: un solo reintento igual, en el namespace -r1.
        if causa:
            reg["reintento_forma"] = {"causa": causa, "motivo_forma": motivo, "namespace": CL.namespace_c1(cliente.brazo, CL.SUFIJO_REINTENTO),
                                      "max_tokens": kw_vigente["max_tokens"], "intento_1": r}
            par3, err3 = llamar(cliente, kw_vigente, doc, sufijo=CL.SUFIJO_REINTENTO)
            if par3 is None:
                reg["error"] = f"api_error_en_reintento_forma: {err3}"
            else:
                resp, info = par3
                r = registrar_llamada("reintento_forma", info, resp)
                ti = r["tool_input_crudo"]
                if r["stop_reason"] == "max_tokens":
                    reg["error"] = f"{causa}_tras_reintento: corte"
                elif r["stop_reason"] == "refusal":
                    reg["error"] = f"{causa}_tras_reintento: refusal"
                elif ti is None:
                    reg["error"] = f"{causa}_tras_reintento: sin_herramienta"
                    val_e1 = val_r2 = motivo = None
                else:
                    val_e1, val_r2, motivo = validar(ti, chunk, perfil)
                    if motivo:
                        reg["error"] = f"{causa}_tras_reintento: mal_formada ({motivo})"
    reg.update({"stop_reason": r["stop_reason"], "stop_details": r["stop_details"], "usage": r["usage"], "id_respuesta": r["id_respuesta"],
                "modelo_respuesta": r["modelo_respuesta"], "bloques": r["bloques"], "n_tool_use": r["n_tool_use"],
                "largo_pensamiento_devuelto": r["largo_pensamiento_devuelto"], "texto": r["texto"],
                "tool_input_crudo": ti, "validacion_e1": val_e1, "validacion_r2": val_r2, "motivo_forma": motivo,
                "reparable_relations_ausente": (isinstance(ti, dict) and "relations" not in ti and isinstance(ti.get("entities"), list))})
    return cerrar(reg)


def cerrar(reg: dict) -> dict:
    tot = {"input_tokens": 0, "output_tokens": 0, "cache_write_tokens": 0, "cache_read_tokens": 0}
    for ll in reg["llamadas"]:
        for k in tot:
            tot[k] += (ll.get("usage") or {}).get(k, 0)
    reg["usage_total"] = tot
    reg["costo_usd"] = round(sum(ll.get("costo_usd", 0.0) for ll in reg["llamadas"]), 6)
    reg["n_llamadas"] = len(reg["llamadas"])
    reg["segundos"] = round(sum(ll.get("segundos", 0.0) for ll in reg["llamadas"]), 1)
    reg["tramo_entidad"] = ((reg.get("validacion_r2") or {}).get("contadores") or {}).get("tramo_entidad")
    reg["rechazos_r2_por_motivo"] = ((reg.get("validacion_r2") or {}).get("metricas") or {}).get("rechazos_por_motivo")
    return reg


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--brazo", choices=("S", "O"), required=True)
    ap.add_argument("--corrida", type=int, choices=(1, 2), required=True)
    ap.add_argument("--env", type=Path, default=None)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--autorizado-tope", type=float, default=None)
    ap.add_argument("--limite", type=int, default=None, help="solo las primeras N unidades (pruebas)")
    a = ap.parse_args()
    if a.autorizado_tope != C.TOPE_USD:
        raise SystemExit(f"corrida real exige --autorizado-tope {C.TOPE_USD}")
    if a.env is None:
        raise SystemExit("corrida real exige --env")
    from dotenv import load_dotenv  # noqa: PLC0415
    load_dotenv(a.env)               # la clave no se imprime ni se escribe
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        raise SystemExit("ANTHROPIC_API_KEY ausente en el entorno tras cargar --env")
    return correr(a.brazo, a.corrida, a.salida, limite=a.limite)


def correr(brazo: str, corrida: int, salida: Path, limite: int | None = None, real=None) -> int:
    """El cuerpo de una corrida; el selftest lo llama con un cliente real simulado."""
    salida.mkdir(parents=True, exist_ok=True)
    etiqueta = f"{brazo}{corrida}"
    perfil = C.perfil_r2b()
    unidades = C.cargar_unidades()
    if limite:
        unidades = unidades[:limite]
    chunks = C.cargar_chunks(unidades)
    shas_c0 = C.shas_pedidos_c0()
    # Control previo, sin llamadas: los pedidos son los que C0 contó.
    pedidos = {}
    distintos = []
    for u in unidades:
        kw = C.pedido_adaptado(perfil, chunks[u["chunk_id"]], brazo)
        pedidos[u["chunk_id"]] = kw
        if C.sha_pedido(kw) != shas_c0.get((brazo, u["chunk_id"])):
            distintos.append(u["chunk_id"])
    if distintos:
        raise SystemExit(f"[{etiqueta}] {len(distintos)} pedidos distintos de los que C0 contó: {distintos[:5]} — se frena sin llamar")
    presupuesto = C.PresupuestoC1(C.TOPE_USD, salida / "presupuesto.json")
    cliente = CL.ClienteC1(brazo, corrida, salida / "cache" / f"c1_{brazo}_{corrida}.db", presupuesto,
                           salida / "cache_usage_c1.jsonl", real=real)
    resultados = salida / f"resultados_{etiqueta}.jsonl"
    hechos = C.jsonl_last_wins(resultados)
    pendientes = [u for u in unidades if not (u["chunk_id"] in hechos and hechos[u["chunk_id"]].get("error") is None)]
    print(f"[{etiqueta}] {C.MODELOS[brazo]} | unidades={len(unidades)} hechas_ok={len(unidades) - len(pendientes)} "
          f"pendientes={len(pendientes)} | namespace={CL.namespace_c1(brazo)} | db={cliente.db_path.name} | tope={C.TOPE_USD} "
          f"gasto_previo={presupuesto.gasto_usd:.4f}", flush=True)
    t0 = time.time()
    resumen = {"unidad": "U-COMP-E1, C1", "etiqueta": etiqueta, "brazo": brazo, "corrida": corrida, "modelo": C.MODELOS[brazo],
               "namespace": CL.namespace_c1(brazo), "namespace_reintento": CL.namespace_c1(brazo, CL.SUFIJO_REINTENTO),
               "db": cliente.db_path.name, "inicio_utc": C.ahora(), "unidades": len(unidades), "pendientes_al_iniciar": len(pendientes)}
    consecutivos = 0
    freno = None
    try:
        for i, u in enumerate(pendientes, 1):
            cid = u["chunk_id"]
            reg = extraer(cliente, chunks[cid], pedidos[cid], perfil)
            C.append_jsonl(resultados, reg)
            consecutivos = 0 if not (reg["error"] or "").startswith("api_error") else consecutivos + 1
            marcas = (" CORTE" if reg["reintento_corte"] else "") + (f" {reg['reintento_forma']['causa'].upper()}" if reg["reintento_forma"] else "")
            print(f"[{etiqueta} {i}/{len(pendientes)}] {cid:<22s} stop={reg['stop_reason']} out={(reg.get('usage') or {}).get('output_tokens')} "
                  f"err={reg['error']}{marcas} | USD {reg['costo_usd']:.4f} acum {presupuesto.gasto_usd:.4f}", flush=True)
            if consecutivos > MAX_ERRORES_CONSECUTIVOS:
                raise RuntimeError(f"más de {MAX_ERRORES_CONSECUTIVOS} errores de API consecutivos — se frena")
    except (CL.TopeExcedido, RuntimeError) as e:
        freno = str(e)
        print(f"\nFRENO: {e}", flush=True)
    finally:
        todos = C.jsonl_last_wins(resultados)
        errores = {k: v["error"] for k, v in todos.items() if v.get("error")}
        resumen.update({"fin_utc": C.ahora(), "segundos": round(time.time() - t0, 1), "freno": freno,
                        "registradas": len(todos), "con_error": len(errores), "errores": errores,
                        "cortes": sum(1 for v in todos.values() if v.get("reintento_corte")),
                        "reintentos_forma": {k: v["reintento_forma"]["causa"] for k, v in todos.items() if v.get("reintento_forma")},
                        "refusals": sum(1 for v in todos.values() if v.get("stop_reason") == "refusal"),
                        "usage_total": {k: sum((v.get("usage_total") or {}).get(k, 0) for v in todos.values())
                                        for k in ("input_tokens", "output_tokens", "cache_write_tokens", "cache_read_tokens")},
                        "gasto_usd_registros": round(sum(v.get("costo_usd", 0.0) for v in todos.values()), 6),
                        "gasto_usd_cliente_este_proceso": round(cliente.gasto_usd, 6),
                        "gasto_usd_presupuesto_corrida": round(presupuesto.por_corrida.get(etiqueta, 0.0), 6),
                        "gasto_usd_presupuesto_total": round(presupuesto.gasto_usd, 6), "cliente": cliente.resumen()})
        cliente.close()
        (salida / f"resumen_{etiqueta}.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(json.dumps({k: v for k, v in resumen.items() if k not in ("cliente", "errores", "reintentos_forma")}, ensure_ascii=False), flush=True)
    return 3 if freno else 0


if __name__ == "__main__":
    raise SystemExit(main())
