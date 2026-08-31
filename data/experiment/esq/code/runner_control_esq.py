"""
runner_control_esq.py — Corrida del CONTROL DE INSTRUMENTO de ESQ-1: las 40
unidades de los tres brazos (comun_control_esq.seleccionar), en modo canal
abierto (canal_abierto=True en prefijo, tool schema, validador y namespace).

Invoca el pipeline de extracción sin modificarlo (patrón del pre-registro §8):
prompt_e1.build_request_kwargs / cliente_e1.ClienteE1Real / validador_e1, todos
con el flag explícito. Namespace particionado por construcción
(e1_extraccion|cv=e1-extractor-v1-p<PREFIJO_HASH_ABIERTO_ESPERADO>|think=0;
la corrida original U-ESQ-1c usó pbca492bbf7c8): la caché de
producción no recibe una sola escritura; además la corrida usa .db PROPIA
(esq/cache/esq_control.db, gitignorada) — doble aislamiento (scoping §2.5).

Decisiones de caching (docs/decisiones_caching_extraccion.md):
  - D1: el flag va en el prefijo estable, nada variable por chunk antes del
    breakpoint (build_request_kwargs, sin tocar).
  - D2: todo costo con la fórmula de caching (comun_control_esq.costo_usd_desde_usage).
  - D3: component propio "esq_control_e1" (ClienteControlEsq._log_usage) — el
    gasto de ESQ es auditable por separado del de producción.
  - D4: corrida SECUENCIAL (un solo cliente, un solo loop).

Gasto: presupuesto USD 0,32 (scoping §5.3 «Control»); TOPE PARCIAL DURO
USD 0,50 (mandato U-ESQ-1c): si el acumulado lo toca, FRENO inmediato con
reporte. El tope del cliente (TopeExcedido) se fija en 0,50: freno real.

Persistencia: control/extracciones_control_esq.jsonl, append-only, MISMAS
claves que producción (runner_corpus.fase_e1: chunk_id, unidad, tipo_unidad,
titulo, stop_reason, error, usage, tool_input_crudo, validacion); el brazo de
cada unidad vive en control/orden/seleccion_control_esq.json, no en el jsonl.
Reanudación idempotente: las unidades persistidas sin error se saltean.

Uso:
  selftest offline (sin API, escribe en selftest_out/): via selftest_control_esq.py
  corrida real (SOLO con autorización explícita en el chat):
    .venv/bin/python3 -B data/experiment/esq/code/runner_control_esq.py \
        --autorizado-tope-parcial 0.50
  --solo-resumen: recomputa el resumen desde el jsonl persistido, sin API.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402  (agrega e1_extractor al path)
import comun_e1                            # noqa: E402
import prompt_e1                           # noqa: E402
import cliente_e1                          # noqa: E402
import validador_e1                        # noqa: E402

DB_CONTROL = cc.CACHE_DIR / "esq_control.db"
JSONL_CONTROL = "extracciones_control_esq.jsonl"


class Freno(RuntimeError):
    pass


class ClienteControlEsq(cliente_e1.ClienteE1Real):
    """ClienteE1Real con component propio en el log de usage (D3 del scoping
    §2: «esq» no reusa reextraccion_v2_e1). No cambia nada más."""

    COMPONENT = "esq_control_e1"

    def _log_usage(self, usage, doc):
        cliente_e1.CACHE_USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
        line = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "component": self.COMPONENT,
            "doc": doc,
            "input_tokens": getattr(usage, "input_tokens", None),
            "cache_creation_input_tokens": getattr(usage, "cache_creation_input_tokens", None),
            "cache_read_input_tokens": getattr(usage, "cache_read_input_tokens", None),
            "output_tokens": getattr(usage, "output_tokens", None),
        }
        with cliente_e1.CACHE_USAGE_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")


# --------------------------------------------------------------------------- #
# Guardas previas a cualquier gasto                                            #
# --------------------------------------------------------------------------- #
def verificar_canal_abierto(chunk: dict) -> dict:
    """Asserts de que el flag va ENCENDIDO en la request y el namespace es el
    particionado. Corre antes de la primera llamada; si algo no cierra, nada
    se gasta. Devuelve las evidencias para el resumen."""
    ns = cliente_e1.namespace_e1(canal_abierto=True)
    h = prompt_e1.prefijo_hash(True)
    kwargs = prompt_e1.build_request_kwargs(chunk, model=cc.MODEL_E1,
                                            canal_abierto=True)
    props_e = kwargs["tools"][0]["input_schema"]["properties"]["entities"][
        "items"]["properties"]
    props_r = kwargs["tools"][0]["input_schema"]["properties"]["relations"][
        "items"]["properties"]
    ok = {
        "prefijo_hash_abierto": h,
        "namespace": ns,
        "namespace_particionado": h == cc.PREFIJO_HASH_ABIERTO_ESPERADO
        and f"p{cc.PREFIJO_HASH_ABIERTO_ESPERADO}" in ns,
        "tool_schema_tipo_propuesto": "tipo_propuesto" in props_e,
        "tool_schema_predicado_propuesto": "predicado_propuesto" in props_r,
        "system_es_prefijo_abierto": (
            kwargs["system"][0]["text"] == prompt_e1.prefijo_sistema(True)),
        "model": kwargs["model"],
    }
    if not all(v is True for k, v in ok.items()
               if k not in ("prefijo_hash_abierto", "namespace", "model")):
        raise Freno(f"guarda de canal abierto falló: {ok} — no se gasta")
    return ok


# --------------------------------------------------------------------------- #
# Stub offline (selftest)                                                      #
# --------------------------------------------------------------------------- #
class StubClienteControl:
    """Cliente offline: tool inputs enlatados por chunk_id (default mínimo
    válido). Interfaz .create(doc=..., **kw) como el real; usage en cero."""

    class _U:
        input_tokens = 0
        output_tokens = 0
        cache_creation_input_tokens = 0
        cache_read_input_tokens = 0

    class _R:
        def __init__(self, tool_input):
            class B:
                type = "tool_use"
            b = B()
            b.name = prompt_e1.NOMBRE_TOOL
            b.input = tool_input
            self.content = [b]
            self.stop_reason = "tool_use"
            self.usage = StubClienteControl._U()

    def __init__(self, por_chunk: dict | None = None):
        self.por_chunk = por_chunk or {}
        self.gasto_usd = 0.0
        self.llamadas = 0
        self.llamadas_hit = 0
        self.requests: list[dict] = []

    def create(self, doc=None, **kwargs):
        self.llamadas += 1
        self.requests.append(kwargs)
        cid = self.por_chunk.get("_actual")
        ti = self.por_chunk.get(cid, {"entities": [], "relations": [],
                                      "omisiones_no_prosa": []})
        return StubClienteControl._R(ti)

    def resumen(self):
        return {"llamadas": self.llamadas, "hits_cache_local": self.llamadas_hit,
                "gasto_usd_real": 0.0, "stub": True}

    def close(self):
        pass


# --------------------------------------------------------------------------- #
# Corrida                                                                      #
# --------------------------------------------------------------------------- #
def cargar_jsonl_last_wins(path: Path) -> dict[str, dict]:
    regs: dict[str, dict] = {}
    if path.exists():
        with path.open(encoding="utf-8") as f:
            for linea in f:
                linea = linea.strip()
                if linea:
                    r = json.loads(linea)
                    regs[r["chunk_id"]] = r
    return regs


def append_jsonl(path: Path, reg: dict) -> None:
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(reg, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def chunks_por_id() -> dict[str, dict]:
    chunks = comun_e1.cargar_chunks(cc.TOS, e0_dir=comun_e1.E0_SALIDA_ENM01)
    return {c["id"]: c for c in chunks}


def persistir_orden(seleccion: list[dict], universo: dict, destino: Path) -> Path:
    po = cc.pools(universo)
    destino.mkdir(parents=True, exist_ok=True)
    path = destino / "seleccion_control_esq.json"
    doc = {
        "semilla": cc.SEMILLA,
        "regla": ("scoping_esq1.md §6.1-6.3 + decisiones D-a..D-f de "
                  "comun_control_esq.py; pools ordenados por chunk_id; "
                  "Random(20260827) consumido A(cap)->A(ric)->A(ext∪cla)->B->"
                  "C(cap,cla,ext,pro,ric)"),
        "pools": {"A_por_to": {t: len(v) for t, v in po["A"].items()},
                  "A_total": sum(len(v) for v in po["A"].values()),
                  "B_total": len(po["B"]),
                  "B_interseccion_A": len(set(po["B"])
                                          & {s["chunk_id"] for s in seleccion
                                             if s["brazo"] == "A"}),
                  "C_por_to": {t: len(v) for t, v in po["C"].items()}},
        "seleccion": seleccion,
    }
    if path.exists():
        previo = json.loads(path.read_text(encoding="utf-8"))
        if previo["seleccion"] != seleccion or previo["semilla"] != cc.SEMILLA:
            raise Freno(f"{path} existe y difiere de la selección recomputada "
                        "— no se pisa; revisar antes de correr")
        return path
    path.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                    encoding="utf-8")
    return path


def correr(cliente, seleccion: list[dict], salida: Path,
           tope_parcial_usd: float, stub: bool,
           por_id: dict[str, dict] | None = None,
           jsonl_nombre: str = JSONL_CONTROL) -> dict:
    """por_id/jsonl_nombre son inyectables para la re-corrida P1′ (U-ESQ-1d):
    las unidades dopadas no viven en E0 sino en fixtures de control/. Con los
    defaults el comportamiento es EXACTAMENTE el de U-ESQ-1c."""
    salida.mkdir(parents=True, exist_ok=True)
    jsonl = salida / jsonl_nombre
    if por_id is None:
        por_id = chunks_por_id()
    faltan = [s["chunk_id"] for s in seleccion if s["chunk_id"] not in por_id]
    if faltan:
        raise Freno(f"chunks ausentes en E0_SALIDA_ENM01: {faltan}")

    previos = cargar_jsonl_last_wins(jsonl)
    hechas_ok = {cid for cid, r in previos.items() if r.get("error") is None}
    pendientes = [s for s in seleccion if s["chunk_id"] not in hechas_ok]
    print(f"[control] unidades={len(seleccion)} ya_persistidas_ok={len(hechas_ok)} "
          f"pendientes={len(pendientes)}", flush=True)

    t0 = time.time()
    frenado = None
    for s in pendientes:
        c = por_id[s["chunk_id"]]
        if cliente.gasto_usd >= tope_parcial_usd:
            frenado = (f"tope parcial USD {tope_parcial_usd:.2f} tocado antes de "
                       f"{c['id']}: gasto USD {cliente.gasto_usd:.4f}")
            break
        kwargs = prompt_e1.build_request_kwargs(c, model=cc.MODEL_E1,
                                                canal_abierto=True)
        if stub:
            cliente.por_chunk["_actual"] = c["id"]
        try:
            resp = cliente.create(doc=c["archivo"], **kwargs)
        except cliente_e1.TopeExcedido as e:
            frenado = f"TopeExcedido del cliente: {e}"
            break
        u = resp.usage
        usage = {"input_tokens": getattr(u, "input_tokens", 0) or 0,
                 "output_tokens": getattr(u, "output_tokens", 0) or 0,
                 "cache_write_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
                 "cache_read_tokens": getattr(u, "cache_read_input_tokens", 0) or 0}
        stop = getattr(resp, "stop_reason", None)
        tool_input = next((b.input for b in resp.content
                           if getattr(b, "type", None) == "tool_use"), None)
        err = None
        if tool_input is None:
            err = f"no_tool_use stop_reason={stop}"
        elif stop == "max_tokens":
            err = "max_tokens_hit"
        val = (validador_e1.validar_salida(tool_input, c, canal_abierto=True)
               .as_dict() if tool_input is not None else None)
        append_jsonl(jsonl, {
            "chunk_id": c["id"], "unidad": c["unidad"], "tipo_unidad": c["tipo"],
            "titulo": c["titulo"], "stop_reason": stop, "error": err,
            "usage": usage, "tool_input_crudo": tool_input, "validacion": val})
        print(f"  [{s['brazo']}] {c['id']:<24s} gasto=USD {cliente.gasto_usd:.4f}"
              + (f" ERROR {err}" if err else ""), flush=True)
        if cliente.gasto_usd >= tope_parcial_usd:
            frenado = (f"tope parcial USD {tope_parcial_usd:.2f} tocado tras "
                       f"{c['id']}: gasto USD {cliente.gasto_usd:.4f}")
            break
    return {"wall_s": round(time.time() - t0, 1), "frenado": frenado}


def resumen_control(seleccion: list[dict], salida: Path, universo: dict,
                    cliente_resumen: dict | None, corrida_meta: dict | None,
                    guardas: dict | None) -> dict:
    regs = cargar_jsonl_last_wins(salida / JSONL_CONTROL)
    conteos = cc.conteos_por_brazo(seleccion, regs)
    usages = [regs[s["chunk_id"]].get("usage") for s in seleccion
              if s["chunk_id"] in regs]
    agg = cc.agregar_usage(usages)
    factores = cc.factores_produccion()
    agg_prod = cc.usage_produccion_de(universo, [s["chunk_id"] for s in seleccion])
    recargo = cc.recargo_medido(agg, factores, agg_prod)
    resumen = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "modelo": cc.MODEL_E1,
        "tarifas_usd_mtok": {**cc.P_E1,
                             "ancla": "reextraccion_v2/corpus_v2/runner_corpus.py:76-78"},
        "guardas_canal_abierto": guardas,
        "corrida": corrida_meta,
        "cliente": cliente_resumen,
        "conteos_por_brazo": {k: v for k, v in conteos.items()
                              if k != "detalle_por_unidad"},
        "usage_agregado": agg,
        "usage_por_llamada": [{"chunk_id": s["chunk_id"], "brazo": s["brazo"],
                               **(regs[s["chunk_id"]].get("usage") or {})}
                              for s in seleccion if s["chunk_id"] in regs],
        "costo_recomputado_desde_usage_usd": round(cc.costo_usd_desde_usage(agg), 6),
        "formula_costo": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 (USD/MTok), "
                          "decisiones_caching_extraccion.md:32-42; tarifas "
                          "runner_corpus.py:76-78"),
        "recargo_medido_D7": recargo,
        "re_presupuesto_esq1_D7": cc.re_presupuesto_esq1(
            recargo, recargo["pref_abierto_medido_tok"]),
        "factores_produccion_recomputados": {k: v for k, v in factores.items()
                                             if k != "agg"},
        "detalle_por_unidad": conteos["detalle_por_unidad"],
    }
    (salida / "resumen_control_esq.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    return resumen


def main() -> int:
    ap = argparse.ArgumentParser(description="Control de instrumento ESQ-1 (40 u, canal abierto)")
    ap.add_argument("--stub", action="store_true", help="cliente stub, offline")
    ap.add_argument("--salida", type=Path, default=cc.CONTROL_DIR)
    ap.add_argument("--autorizado-tope-parcial", type=float, default=None,
                    help="eco de la autorización; debe ser 0.50 para corrida real")
    ap.add_argument("--solo-resumen", action="store_true",
                    help="recomputa el resumen desde lo persistido, sin API")
    args = ap.parse_args()

    universo = cc.cargar_universo()
    seleccion = cc.seleccionar(universo)
    orden_dir = (args.salida / "orden") if args.stub else cc.ORDEN_DIR
    persistir_orden(seleccion, universo, orden_dir)

    if args.solo_resumen:
        r = resumen_control(seleccion, args.salida, universo, None, None, None)
        print(json.dumps(r["conteos_por_brazo"], ensure_ascii=False, indent=1))
        return 0

    por_id = chunks_por_id()
    guardas = verificar_canal_abierto(por_id[seleccion[0]["chunk_id"]])
    print(f"[guardas] namespace={guardas['namespace']} | "
          f"prefijo abierto={guardas['prefijo_hash_abierto']}", flush=True)

    if args.stub:
        cliente = StubClienteControl()
    else:
        if args.autorizado_tope_parcial != cc.TOPE_PARCIAL_USD:
            print(f"ABORTADO: la corrida real exige --autorizado-tope-parcial "
                  f"{cc.TOPE_PARCIAL_USD} (eco de la autorización del chat). "
                  f"Nada se llamó.")
            return 2
        from dotenv import load_dotenv
        load_dotenv(comun_e1.EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            print(f"ANTHROPIC_API_KEY ausente (esperada en {comun_e1.EVAL_DIR / '.env'})")
            return 1
        cliente = ClienteControlEsq(
            **cc.P_E1, tope_usd=cc.TOPE_PARCIAL_USD, run_label="esq_control_e1",
            db_path=DB_CONTROL, canal_abierto=True)

    try:
        meta = correr(cliente, seleccion, args.salida,
                      cc.TOPE_PARCIAL_USD, stub=args.stub)
    finally:
        cliente_res = cliente.resumen()
        cliente.close()

    r = resumen_control(seleccion, args.salida, universo, cliente_res, meta, guardas)
    ca = r["conteos_por_brazo"]
    print(f"\nA: {ca['A']['emiten_algun_propuesto']}/20 (umbral {ca['A']['umbral']}) | "
          f"B: {ca['B']['reportan_relacion']}/10 ({ca['B']['umbral']}) | "
          f"C: {ca['C']['emiten_tipo_propuesto']}/10 ({ca['C']['umbral']})", flush=True)
    print(f"gasto cliente=USD {cliente_res.get('gasto_usd_real', 0):.4f} | "
          f"costo desde usage=USD {r['costo_recomputado_desde_usage_usd']:.4f} | "
          f"presupuesto {cc.PRESUPUESTO_USD} | tope parcial {cc.TOPE_PARCIAL_USD}",
          flush=True)
    if meta.get("frenado"):
        print(f"FRENO: {meta['frenado']}", flush=True)
        return 3
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
