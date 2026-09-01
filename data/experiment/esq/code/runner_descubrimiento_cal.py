"""
runner_descubrimiento_cal.py — Corrida de CALIBRACIÓN del instrumento de
descubrimiento (U-ESQ-2-cal.c): las 20 unidades de la vara sellada — brazo A′
(las 10 dopadas de control/dopadas_p1bis.json, byte-idénticas por sha contra
c25273f) + brazo C (las MISMAS 10 limpias de la selección sellada del control
original) — con el instrumento NUEVO de descubrimiento_cal.py.

Pre-registro: prerregistro_descubrimiento_cal.md (FIRMADO, commit bca863f).
Instrumento separado del pipeline: NO toca prompt_e1.py ni ningún módulo de
producción (los imports de abajo son solo-lectura: fixtures, selección y
helpers de persistencia; el selftest verifica los candados byte-idénticos de
producción). Caché y namespace PROPIOS:
  - dominio "esq_descubrimiento_cal" (≠ e1_extraccion: cero colisión posible
    con los tres namespaces de la escalera y con producción)
  - db propia cache/esq_descubrimiento_cal.db (las de U-ESQ-1c/1d/1e no se
    tocan — su contenido es evidencia de esas corridas)
  - CODE_VER manual "descubrimiento-cal-v1" + hash del contrato (bumpear a
    mano si cambia la lógica sin cambiar el contrato)
  - usage log component "esq_descubrimiento_cal" (D3)

Salidas:
  - jsonl:   control/descubrimiento_cal.jsonl (append-only, reanudable)
  - orden:   control/orden/seleccion_descubrimiento_cal.json
  - resumen: control/resumen_descubrimiento_cal.json

El resumen trae SOLO el conteo MECÁNICO de lo inequívoco (unidades con cero
hallazgos reportados) y el material para la adjudicación. NO computa el
veredicto contra P-cal: la adjudicación fila por fila es de la autora, con la
regla sellada del pre-registro §4.

FRENOS DE GASTO (la corrida real exige los tres):
  (i)   --autorizado-tope-parcial 0.50 (eco de la autorización del mandato);
  (ii)  aprobado_por_autora: true en control/dopadas_p1bis.json (vigente,
        verificada por sha contra c25273f);
  (iii) manifiesto del prompt APROBADO: Estado: APROBADO en
        control/manifiesto_prompt_descubrimiento_cal.md Y sha256 del contrato
        vigente == el registrado en ese manifiesto (freno (a) del mandato).
Tope parcial duro USD 0,50.

Salida malformada del modelo: se persiste el crudo con error
"salida_malformada: …", la corrida sigue (no re-paga a las demás) y main()
termina con exit 2 — jamás salteo silencioso.

Uso:
  stub offline:    via selftest_descubrimiento_cal.py
  corrida real:    .venv/bin/python3 -B data/experiment/esq/code/runner_descubrimiento_cal.py \
                       --autorizado-tope-parcial 0.50
  --solo-resumen:  recomputa el resumen desde lo persistido, sin API.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
import time
import unicodedata
from datetime import datetime, timezone
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_control_esq as cc             # noqa: E402
import runner_control_esq as rc            # noqa: E402
import runner_control_esq_p1bis as rp      # noqa: E402
import runner_control_esq_p1ter as rt      # noqa: E402
import descubrimiento_cal as dc            # noqa: E402
import comun_e1                            # noqa: E402  (solo paths/.env; agrega EVAL_DIR al path)
import cliente_e1                          # noqa: E402  (solo lectura: namespaces de la escalera)
import prompt_e1                           # noqa: E402  (solo lectura: candado de producción intacta)
import llm_cache as lc                     # noqa: E402

JSONL_DESC = "descubrimiento_cal.jsonl"
DB_DESC = cc.CACHE_DIR / "esq_descubrimiento_cal.db"
ORDEN_DESC = "seleccion_descubrimiento_cal.json"
RESUMEN_DESC = "resumen_descubrimiento_cal.json"
MANIFIESTO_DOPADAS = cc.CONTROL_DIR / "manifiesto_dopadas_p1bis.md"

DOMAIN_DESC = "esq_descubrimiento_cal"
CODE_VER_DESC = "descubrimiento-cal-v1"
COMPONENT_DESC = "esq_descubrimiento_cal"

# Marcadores de los 10 conceptos plantados (manifiesto_dopadas_p1bis.md),
# normalizados sin acentos: NINGUNO puede aparecer en el contrato del
# instrumento (no sembrar). Lista declarada a mano, patrón del selftest de
# U-ESQ-1e; el check de cláusulas y conceptos verbatim corre aparte y es
# 100 % mecánico contra el manifiesto.
MARCADORES_CONCEPTOS = (
    "sancion", "multa", "presuncion", "prueba en contrario", "definicion",
    "termino definido", "vigencia", "transitoria", "facultad", "potestad",
    "permiso", "equivalen", "asimila", "complementa", "acredita",
    "computo conjunto", "computara conjuntamente", "conjuntamente",
)


def namespace_descubrimiento() -> str:
    return lc.make_namespace(
        DOMAIN_DESC,
        code_ver=f"{CODE_VER_DESC}-p{dc.PREFIJO_HASH_DESC}",
        thinking=False,
    )


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def _norm(s: str) -> str:
    """minúsculas + sin acentos, para el check de marcadores."""
    return "".join(ch for ch in unicodedata.normalize("NFD", s.lower())
                   if unicodedata.category(ch) != "Mn")


def conceptos_del_manifiesto() -> dict[str, str]:
    """chunk_id_dopado → concepto plantado, parseado MECÁNICAMENTE del
    manifiesto aprobado de las dopadas (fuente: manifiesto_dopadas_p1bis.md,
    formato '### dop::…' + línea '- **Concepto plantado:** …')."""
    txt = MANIFIESTO_DOPADAS.read_text(encoding="utf-8")
    out: dict[str, str] = {}
    actual = None
    for linea in txt.split("\n"):
        m = re.match(r"^### (dop::\S+)\s*$", linea)
        if m:
            actual = m.group(1)
            continue
        m = re.match(r"^- \*\*Concepto plantado:\*\* (.+)$", linea)
        if m and actual:
            out[actual] = m.group(1).strip()
            actual = None
    if len(out) != 10:
        raise rc.Freno(f"esperaba 10 conceptos plantados en el manifiesto de "
                       f"dopadas; parseé {len(out)}")
    return out


def manifiesto_prompt_aprobado(path: Path | None = None) -> dict:
    """Gate del freno (a): el manifiesto del prompt existe, dice APROBADO y su
    sha registrado coincide con el contrato vigente. `path` es inyectable solo
    para el selftest; la corrida real usa el manifiesto de control/."""
    p = path or dc.MANIFIESTO_PROMPT
    if not p.exists():
        return {"existe": False, "aprobado": False, "sha_coincide": False}
    txt = p.read_text(encoding="utf-8")
    return {
        "existe": True,
        "aprobado": dc.manifiesto_dice_aprobado(txt),
        "sha_coincide": dc.SHA256_CONTRATO_DESC in txt,
    }


def verificar_descubrimiento(fx: dict) -> dict:
    """Guardas previas a cualquier gasto (mandato U-ESQ-2-cal.b). Si algo no
    cierra, Freno: nada se llama."""
    conceptos = conceptos_del_manifiesto()
    contrato = dc.CONTRATO_CANONICO_DESC
    contrato_norm = _norm(contrato)
    ns = namespace_descubrimiento()
    ns_escalera = [
        lc.make_namespace(cliente_e1.DOMAIN,
                          code_ver=f"{cliente_e1.CODE_VER}-p{h}",
                          thinking=False)
        for h in (cc.PREFIJO_HASH_ABIERTO_CONTROL_ORIGINAL,
                  cc.PREFIJO_HASH_ABIERTO_P1BIS,
                  cc.PREFIJO_HASH_ABIERTO_ESPERADO)]
    universo = cc.cargar_universo()
    checks = {
        "fixtures_sha256_igual_c25273f": (
            _sha(rp.FIXTURES.read_text(encoding="utf-8"))
            == rt.SHA256_DOPADAS_C25273F),
        "aprobacion_dopadas_vigente": fx.get("aprobado_por_autora") is True,
        "clausulas_no_sembradas": all(
            d["clausula_plantada"] not in contrato for d in fx["dopadas"]),
        "conceptos_no_sembrados": all(
            c not in contrato for c in conceptos.values()),
        "marcadores_no_sembrados": all(
            m not in contrato_norm for m in MARCADORES_CONCEPTOS),
        "namespace_propio_sin_colision": (
            ns not in ns_escalera and ns != rp.NAMESPACE_PROD
            and ns.startswith(DOMAIN_DESC + "|")),
        "db_propia": DB_DESC.name == "esq_descubrimiento_cal.db"
        and DB_DESC not in (rc.DB_CONTROL, rp.DB_P1BIS, rt.DB_P1TER),
        "dopadas_fuera_del_universo": all(
            d["chunk_id_dopado"].startswith("dop::")
            and d["chunk_id_dopado"] not in universo
            for d in fx["dopadas"]),
        "produccion_intacta_prefijo": (
            _sha(prompt_e1.PREFIJO_CANONICO) == rp.SHA256_PREFIJO_PROD),
        "tipos_y_predicados_del_contrato_completos": all(
            t in dc.PREFIJO_DESCUBRIMIENTO for t in dc.TIPOS_6)
        and all(p in dc.PREFIJO_DESCUBRIMIENTO for p in dc.PREDICADOS_12),
    }
    if not all(checks.values()):
        raise rc.Freno(f"guardas del descubrimiento fallaron: {checks} — "
                       "no se gasta")
    return {"checks": checks, "namespace": ns,
            "contrato_sha256": dc.SHA256_CONTRATO_DESC,
            "manifiesto_prompt": manifiesto_prompt_aprobado()}


# --------------------------------------------------------------------------- #
# Clientes                                                                     #
# --------------------------------------------------------------------------- #
class ClienteDescubrimiento:
    """Cliente real never-pay-twice del instrumento (patrón llm-capture,
    calcado de cliente_e1.ClienteE1Real con dominio/db/component propios).
    Solo se construye con precios y tope explícitos."""

    def __init__(self, *, precio_in_por_mtok: float, precio_out_por_mtok: float,
                 precio_cache_write_por_mtok: float,
                 precio_cache_read_por_mtok: float, tope_usd: float,
                 run_label: str, db_path: Path = DB_DESC):
        if min(precio_in_por_mtok, precio_out_por_mtok,
               precio_cache_write_por_mtok,
               precio_cache_read_por_mtok) <= 0 or tope_usd <= 0:
            raise ValueError("precios y tope deben ser positivos")
        import anthropic
        db_path.parent.mkdir(parents=True, exist_ok=True)
        self.p_in = precio_in_por_mtok
        self.p_out = precio_out_por_mtok
        self.p_cw = precio_cache_write_por_mtok
        self.p_cr = precio_cache_read_por_mtok
        self.tope_usd = tope_usd
        self.cache = lc.CachingClient(
            anthropic.Anthropic(max_retries=3),
            domain=DOMAIN_DESC,
            db_path=db_path,
            namespace=namespace_descubrimiento(),
            thinking_enabled=False,
            run_label=run_label,
        )
        self.gasto_usd = 0.0
        self.llamadas = 0
        self.llamadas_hit = 0
        # Proyección conservadora de una llamada fría: prefijo entero como
        # cache write + mensaje variable + salida máxima.
        self._proyeccion_usd = (
            3000 / 1e6 * self.p_cw
            + 3000 / 1e6 * self.p_in
            + dc.MAX_OUTPUT_TOKENS_DESC / 1e6 * self.p_out
        )

    def _log_usage(self, usage, doc) -> None:
        cliente_e1.CACHE_USAGE_LOG.parent.mkdir(parents=True, exist_ok=True)
        line = {
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "component": COMPONENT_DESC,
            "doc": doc,
            "input_tokens": getattr(usage, "input_tokens", None),
            "cache_creation_input_tokens": getattr(
                usage, "cache_creation_input_tokens", None),
            "cache_read_input_tokens": getattr(
                usage, "cache_read_input_tokens", None),
            "output_tokens": getattr(usage, "output_tokens", None),
        }
        with cliente_e1.CACHE_USAGE_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")

    def create(self, *, doc: str | None = None, **kwargs):
        if self.gasto_usd + self._proyeccion_usd > self.tope_usd:
            raise cliente_e1.TopeExcedido(
                f"gasto acumulado USD {self.gasto_usd:.4f} + proyección "
                f"{self._proyeccion_usd:.4f} supera el tope {self.tope_usd:.2f}")
        antes = dict(self.cache._stats)
        resp = self.cache.messages.create(**kwargs)
        despues = self.cache._stats
        fue_miss = despues["misses"] > antes["misses"]
        self.llamadas += 1
        if fue_miss:
            self._log_usage(resp.usage, doc)
            d_in = despues["tokens_in"] - antes["tokens_in"]
            d_out = despues["tokens_out"] - antes["tokens_out"]
            d_cw = despues["cache_write"] - antes["cache_write"]
            d_cr = despues["cache_read"] - antes["cache_read"]
            self.gasto_usd += (d_in * self.p_in + d_out * self.p_out
                               + d_cw * self.p_cw + d_cr * self.p_cr) / 1e6
        else:
            self.llamadas_hit += 1
        return resp

    def resumen(self) -> dict:
        return {"llamadas": self.llamadas,
                "hits_cache_local": self.llamadas_hit,
                "gasto_usd_real": round(self.gasto_usd, 4),
                "tope_usd": self.tope_usd,
                "precios_por_mtok": {"in": self.p_in, "out": self.p_out,
                                     "cache_write": self.p_cw,
                                     "cache_read": self.p_cr},
                "cache_stats": self.cache.stats()}

    def close(self) -> None:
        self.cache.close()


class StubClienteDescubrimiento:
    """Cliente offline del selftest: tool inputs enlatados por chunk_id
    (default: cero hallazgos). Usage en cero, jamás toca la red."""

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
            b.name = dc.NOMBRE_TOOL_DESC
            b.input = tool_input
            self.content = [b]
            self.stop_reason = "tool_use"
            self.usage = StubClienteDescubrimiento._U()

    def __init__(self, por_chunk: dict | None = None):
        self.por_chunk = por_chunk or {}
        self.gasto_usd = 0.0
        self.llamadas = 0
        self.requests: list[dict] = []

    def create(self, doc=None, **kwargs):
        self.llamadas += 1
        self.requests.append(kwargs)
        cid = self.por_chunk.get("_actual")
        ti = self.por_chunk.get(cid, {"hallazgos": []})
        return StubClienteDescubrimiento._R(ti)

    def resumen(self):
        return {"llamadas": self.llamadas, "gasto_usd_real": 0.0, "stub": True}

    def close(self):
        pass


# --------------------------------------------------------------------------- #
# Corrida                                                                      #
# --------------------------------------------------------------------------- #
def correr_descubrimiento(cliente, seleccion: list[dict], salida: Path,
                          tope_parcial_usd: float, stub: bool,
                          por_id: dict[str, dict]) -> dict:
    """Loop secuencial (D4) sobre las 20 unidades. Reanudación idempotente:
    las persistidas sin error se saltean. Salida malformada → se persiste con
    error, la corrida sigue (exit 2 lo decide main)."""
    salida.mkdir(parents=True, exist_ok=True)
    jsonl = salida / JSONL_DESC
    faltan = [s["chunk_id"] for s in seleccion if s["chunk_id"] not in por_id]
    if faltan:
        raise rc.Freno(f"chunks ausentes: {faltan}")

    previos = rc.cargar_jsonl_last_wins(jsonl)
    hechas_ok = {cid for cid, r in previos.items() if r.get("error") is None}
    pendientes = [s for s in seleccion if s["chunk_id"] not in hechas_ok]
    print(f"[descubrimiento] unidades={len(seleccion)} "
          f"ya_persistidas_ok={len(hechas_ok)} pendientes={len(pendientes)}",
          flush=True)

    t0 = time.time()
    frenado = None
    for s in pendientes:
        c = por_id[s["chunk_id"]]
        if cliente.gasto_usd >= tope_parcial_usd:
            frenado = (f"tope parcial USD {tope_parcial_usd:.2f} tocado antes "
                       f"de {c['id']}: gasto USD {cliente.gasto_usd:.4f}")
            break
        kwargs = dc.build_request_kwargs_descubrimiento(c)
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
        hallazgos = None
        if tool_input is None:
            err = f"no_tool_use stop_reason={stop}"
        elif stop == "max_tokens":
            err = "max_tokens_hit"
        else:
            try:
                hallazgos = dc.parsear_descubrimiento(tool_input)
            except dc.SalidaMalformada as e:
                err = f"salida_malformada: {e}"
        rc.append_jsonl(jsonl, {
            "chunk_id": c["id"], "unidad": c["unidad"],
            "tipo_unidad": c["tipo"], "titulo": c["titulo"],
            "stop_reason": stop, "error": err, "usage": usage,
            "tool_input_crudo": tool_input,
            "hallazgos": hallazgos,
            "n_hallazgos": len(hallazgos) if hallazgos is not None else None})
        n = len(hallazgos) if hallazgos is not None else "-"
        print(f"  [{s['brazo']}] {c['id']:<28s} hallazgos={n} "
              f"gasto=USD {cliente.gasto_usd:.4f}"
              + (f" ERROR {err}" if err else ""), flush=True)
        if cliente.gasto_usd >= tope_parcial_usd:
            frenado = (f"tope parcial USD {tope_parcial_usd:.2f} tocado tras "
                       f"{c['id']}: gasto USD {cliente.gasto_usd:.4f}")
            break
    return {"wall_s": round(time.time() - t0, 1), "frenado": frenado}


# --------------------------------------------------------------------------- #
# Conteo mecánico (solo lo inequívoco; la adjudicación es de la autora)        #
# --------------------------------------------------------------------------- #
def conteo_mecanico(seleccion: list[dict], regs: dict[str, dict]) -> dict:
    """Únicamente hechos mecánicos: cuántos hallazgos reportó cada unidad,
    qué unidades reportaron CERO (inequívoco: sin detección posible), errores
    y contenedores no-lista. NINGÚN cruce contra conceptos esperados, NINGÚN
    veredicto contra P-cal (regla del mandato: la adjudicación es de la
    autora)."""
    detalle = {}
    for s in seleccion:
        cid = s["chunk_id"]
        reg = regs.get(cid)
        ti = (reg or {}).get("tool_input_crudo")
        contenedor_no_lista = (isinstance(ti, dict)
                               and not isinstance(ti.get("hallazgos"), list))
        detalle[cid] = {
            "brazo": s["brazo"],
            "mitad": s.get("mitad"),
            "error": None if reg is None else reg.get("error"),
            "sin_registro": reg is None,
            "n_hallazgos": (reg or {}).get("n_hallazgos"),
            "contenedor_no_lista": contenedor_no_lista,
        }
    def _ids(brazo):
        return [s["chunk_id"] for s in seleccion if s["brazo"] == brazo]
    cero = {b: sorted(c for c in _ids(b)
                      if detalle[c]["n_hallazgos"] == 0)
            for b in ("A'", "C")}
    con_algo = {b: sorted(c for c in _ids(b)
                          if (detalle[c]["n_hallazgos"] or 0) > 0)
                for b in ("A'", "C")}
    return {
        "nota": ("conteo MECÁNICO preliminar: solo lo inequívoco (cero "
                 "hallazgos = sin detección posible). La validez de cada "
                 "detección la adjudica la autora con la regla sellada del "
                 "pre-registro §4; este resumen NO computa P-cal."),
        "cero_hallazgos": cero,
        "n_cero_hallazgos": {b: len(v) for b, v in cero.items()},
        "con_hallazgos": con_algo,
        "n_con_hallazgos": {b: len(v) for b, v in con_algo.items()},
        "contenedores_no_lista": sorted(
            c for c in detalle if detalle[c]["contenedor_no_lista"]),
        "con_error": sorted(c for c in detalle
                            if detalle[c]["error"] is not None
                            or detalle[c]["sin_registro"]),
        "detalle_por_unidad": detalle,
    }


def resumen_descubrimiento(seleccion: list[dict], salida: Path,
                           cliente_resumen, corrida_meta, guardas) -> dict:
    regs = rc.cargar_jsonl_last_wins(salida / JSONL_DESC)
    conteo = conteo_mecanico(seleccion, regs)
    agg = cc.agregar_usage([regs[s["chunk_id"]].get("usage")
                            for s in seleccion if s["chunk_id"] in regs])
    resumen = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "unidad": "U-ESQ-2-cal (calibración del instrumento de descubrimiento, modo ii)",
        "prerregistro": "prerregistro_descubrimiento_cal.md (FIRMADO, bca863f)",
        "modelo": dc.MODEL_DESC,
        "contrato_sha256": dc.SHA256_CONTRATO_DESC,
        "namespace": namespace_descubrimiento(),
        "tarifas_usd_mtok": {**cc.P_E1,
                             "ancla": "reextraccion_v2/corpus_v2/runner_corpus.py:76-78"},
        "guardas": guardas,
        "corrida": corrida_meta,
        "cliente": cliente_resumen,
        "conteo_mecanico": {k: v for k, v in conteo.items()
                            if k != "detalle_por_unidad"},
        "usage_agregado": agg,
        "usage_por_llamada": [{"chunk_id": s["chunk_id"], "brazo": s["brazo"],
                               **(regs[s["chunk_id"]].get("usage") or {})}
                              for s in seleccion if s["chunk_id"] in regs],
        "costo_recomputado_desde_usage_usd": round(cc.costo_usd_desde_usage(agg), 6),
        "formula_costo": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 "
                          "(USD/MTok); tarifas runner_corpus.py:76-78"),
        "detalle_por_unidad": conteo["detalle_por_unidad"],
    }
    (salida / RESUMEN_DESC).write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    return resumen


def persistir_orden_descubrimiento(seleccion: list[dict], destino: Path) -> Path:
    destino.mkdir(parents=True, exist_ok=True)
    path = destino / ORDEN_DESC
    doc = {"unidad": "U-ESQ-2-cal",
           "prerregistro": "prerregistro_descubrimiento_cal.md (bca863f)",
           "regla": ("vara sellada del pre-registro §2, cero cambios: A' = "
                     "las 10 dopadas de dopadas_p1bis.json (sha contra "
                     "c25273f), C = las 10 limpias de la selección sellada "
                     "del control original, sin re-sorteo"),
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


def codigo_salida(seleccion: list[dict], regs: dict[str, dict],
                  frenado) -> int:
    """3 si la corrida frenó por tope; 2 si alguna unidad quedó con salida
    malformada (no salteo silencioso); 0 si no."""
    if frenado:
        return 3
    malformadas = [s["chunk_id"] for s in seleccion
                   if (regs.get(s["chunk_id"]) or {}).get("error", "")
                   and str(regs[s["chunk_id"]]["error"]).startswith(
                       "salida_malformada")]
    if malformadas:
        print(f"SALIDAS MALFORMADAS (exit 2, revisar antes de seguir): "
              f"{malformadas}", flush=True)
        return 2
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Calibración del instrumento de descubrimiento "
                    "(U-ESQ-2-cal: A' 10 dopadas + C 10 limpias)")
    ap.add_argument("--stub", action="store_true")
    ap.add_argument("--salida", type=Path, default=cc.CONTROL_DIR)
    ap.add_argument("--autorizado-tope-parcial", type=float, default=None)
    ap.add_argument("--solo-resumen", action="store_true")
    args = ap.parse_args()

    fx = rp.cargar_fixtures()
    seleccion = rp.seleccion_p1bis(fx)   # la vara sellada: mismas 20 unidades
    orden_dir = (args.salida / "orden") if args.stub else cc.ORDEN_DIR
    persistir_orden_descubrimiento(seleccion, orden_dir)

    if args.solo_resumen:
        r = resumen_descubrimiento(seleccion, args.salida, None, None, None)
        print(json.dumps(r["conteo_mecanico"], ensure_ascii=False, indent=1))
        return 0

    guardas = verificar_descubrimiento(fx)
    print(f"[guardas] namespace={guardas['namespace']} | "
          f"contrato={guardas['contrato_sha256'][:12]} | "
          f"checks={all(guardas['checks'].values())}", flush=True)

    por_id = rp.por_id_p1bis(fx)

    if args.stub:
        cliente = StubClienteDescubrimiento()
    else:
        if args.autorizado_tope_parcial != cc.TOPE_PARCIAL_USD:
            print(f"ABORTADO: la corrida real exige --autorizado-tope-parcial "
                  f"{cc.TOPE_PARCIAL_USD}. Nada se llamó.")
            return 2
        if fx.get("aprobado_por_autora") is not True:
            print("ABORTADO: dopadas_p1bis.json sin aprobado_por_autora: true. "
                  "Nada se llamó.")
            return 2
        gate = manifiesto_prompt_aprobado()
        if not (gate["existe"] and gate["aprobado"] and gate["sha_coincide"]):
            print(f"ABORTADO: manifiesto del prompt sin aprobar o con sha "
                  f"desactualizado (freno (a) del mandato): {gate}. "
                  "Nada se llamó.")
            return 2
        from dotenv import load_dotenv
        load_dotenv(comun_e1.EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            print(f"ANTHROPIC_API_KEY ausente (esperada en "
                  f"{comun_e1.EVAL_DIR / '.env'})")
            return 1
        cliente = ClienteDescubrimiento(
            **cc.P_E1, tope_usd=cc.TOPE_PARCIAL_USD,
            run_label=COMPONENT_DESC, db_path=DB_DESC)

    try:
        meta = correr_descubrimiento(cliente, seleccion, args.salida,
                                     cc.TOPE_PARCIAL_USD, stub=args.stub,
                                     por_id=por_id)
    finally:
        cliente_res = cliente.resumen()
        cliente.close()

    r = resumen_descubrimiento(seleccion, args.salida, cliente_res, meta,
                               guardas)
    cm = r["conteo_mecanico"]
    cero_ap = cm["n_cero_hallazgos"]["A'"]
    cero_c = cm["n_cero_hallazgos"]["C"]
    print(f"\ncero hallazgos: A' {cero_ap}/10 | C {cero_c}/10 "
          f"(mecánico; la adjudicación es de la autora)")
    print(f"gasto cliente=USD {cliente_res.get('gasto_usd_real', 0):.4f} | "
          f"costo desde usage=USD {r['costo_recomputado_desde_usage_usd']:.4f} | "
          f"tope parcial {cc.TOPE_PARCIAL_USD}", flush=True)
    regs = rc.cargar_jsonl_last_wins(args.salida / JSONL_DESC)
    rcode = codigo_salida(seleccion, regs, meta.get("frenado"))
    if meta.get("frenado"):
        print(f"FRENO: {meta['frenado']}", flush=True)
    return rcode


if __name__ == "__main__":
    raise SystemExit(main())
