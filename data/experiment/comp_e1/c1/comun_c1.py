"""
comun_c1.py — U-COMP-E1, etapa C1: rutas, pedido adaptado, carga de unidades y chunks, presupuesto y utilidades.

Mandato: docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md (firmado en cbcb823; notas al pie hasta la del 06/10/2026 en
25480b9); «seguí» de C1 del 06/10/2026 (decisiones 1 a 5). El pedido adaptado es, byte a byte, el que C0 contó
(c0/c0b_api.py, pedido_adaptado): S sin temperature, tool_choice auto, thinking between_tools, max_tokens 16.384; O sin
temperature, tool_choice auto, output_config.effort low, max_tokens 16.384; mismo prefijo r2b con su punto de caché,
mismo mensaje por unidad, mismo tool schema sin strict. correr_c1 lo comprueba contra sha256_pedido_canonico de
c0/salida/conteo_tokens_c0.jsonl antes de la primera llamada.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent            # comp_e1/c1
COMP_E1 = AQUI.parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "e1_extractor", REPO / "data" / "experiment" / "evaluacion", REPO / "data" / "experiment" / "pyd_r2" / "code"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import llm_cache as lc  # noqa: E402 — capa sellada, solo import
import perfil_e1  # noqa: E402

PREFIJO = "322c5a23e9b7"
MODELOS = {"S": "claude-sonnet-5-5", "O": "claude-opus-5-5"}
# Precios por millón de tokens (entrada, salida, escritura de caché de 5 minutos, lectura de caché): los de C0
# (c0/c0b_api.py, PRECIOS; borrador P6 con las páginas consultadas el 05/10/2026; tabla COSTO del mandato).
PRECIOS = {"S": {"in": 2.00, "out": 10.00, "cw": 2.50, "cr": 0.20},
           "O": {"in": 4.00, "out": 20.00, "cw": 5.00, "cr": 0.20}}
MAX_TOKENS_BASE = 16384
MAX_TOKENS_REINTENTO_CORTE = 40960      # regla del pedido (:46): si corta, un reintento a 40.960 con transmisión
TOPE_USD = 35.0                          # decisión 3 al firmar; nota al pie del 06/10/2026
MOTIVOS_FORMA_E1 = ("salida_no_parseable", "salida_no_dict", "entities_o_relations_invalidos")   # runner_corpus:481
UNIDADES_JSON = COMP_E1 / "unidades.json"
UNIDADES_SHA256 = "b607d1f6c3131129141b994c76e54f4c119c99810ed04d3f0b87b64aaac0fd07"     # sellado en C0 (c)
INTENTO0_JSONL = COMP_E1 / "c0" / "salida" / "intento0_haiku.jsonl"
CONTEO_C0 = COMP_E1 / "c0" / "salida" / "conteo_tokens_c0.jsonl"
ESTIMACION_C0 = COMP_E1 / "c0" / "salida" / "estimacion_costo_c0.json"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
SALIDA_R2B = REX / "corpus_tanda0" / "salida_r2b"
# Los dos intentos 0 de Haiku con marca (C0 (a); nota al pie del 06/10/2026): se declaran en el registro y en M3.
MARCAS_INTENTO0_HAIKU = {"cap::3.1.14.1": "intento 0 de Haiku = reintento (corte, a 16.384)",
                         "ctacte::5.1.2.2": "intento 0 de Haiku = reintento (forma, temperatura 1, namespace -rforma1)"}


def ahora() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256_archivo(p: Path) -> str:
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def cargar_unidades() -> list[dict]:
    """Las 87 unidades selladas en C0 (c); frena si el archivo no es el sellado."""
    sha = sha256_archivo(UNIDADES_JSON)
    if sha != UNIDADES_SHA256:
        raise RuntimeError(f"unidades.json con sha256 {sha[:12]}… (sellado {UNIDADES_SHA256[:12]}…) — se frena")
    return json.loads(UNIDADES_JSON.read_text(encoding="utf-8"))["unidades"]


def chunks_de(to: str) -> dict:
    """Chunks de la E0 r2b del TO, más las partes de particiones_por_corte.json (como en C0 y en reext_t0/t4/comun_t4)."""
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


def cargar_chunks(unidades: list[dict]) -> dict:
    out: dict = {}
    for to in sorted({u["to"] for u in unidades}):
        out.update(chunks_de(to))
    return out


def perfil_r2b():
    perfil = perfil_e1.perfil("r2b")
    if perfil.prefijo_hash != PREFIJO:
        raise RuntimeError(f"el perfil r2b da el prefijo {perfil.prefijo_hash}, no {PREFIJO} — se frena")
    return perfil


def pedido_adaptado(perfil, chunk: dict, brazo: str) -> dict:
    """El pedido de E1 del perfil r2b y solo lo que cambia la tabla BRAZOS del mandato (idéntico a c0/c0b_api.py)."""
    kw = perfil.build_request_kwargs(chunk, model=MODELOS[brazo])
    kw.pop("temperature", None)
    kw["tool_choice"] = {"type": "auto"}
    kw["max_tokens"] = MAX_TOKENS_BASE
    if brazo == "S":
        kw["thinking"] = {"type": "between_tools"}
    else:
        kw["output_config"] = {"effort": "low"}
    return kw


def sha_pedido(kw: dict) -> str:
    return hashlib.sha256(lc.canonical_request(kw).encode("utf-8")).hexdigest()


def shas_pedidos_c0() -> dict[tuple[str, str], str]:
    out = {}
    for x in CONTEO_C0.read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            out[(r["brazo"], r["chunk_id"])] = r["sha256_pedido_canonico"]
    return out


def jsonl_last_wins(p: Path, clave: str = "chunk_id") -> dict:
    out: dict = {}
    if Path(p).exists():
        for x in Path(p).read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                out[r[clave]] = r
    return out


def append_jsonl(p: Path, reg: dict) -> None:
    with Path(p).open("a", encoding="utf-8") as f:
        f.write(json.dumps(reg, ensure_ascii=False) + "\n")


def motivo_forma_e1(val: dict | None) -> str | None:
    """Motivo de forma con que validador_e1 rechazó la unidad entera, o None (runner_corpus.motivo_forma_e1)."""
    return next((r["motivo"] for r in (val or {}).get("rechazos", [])
                 if r.get("nivel") == "chunk" and r.get("motivo") in MOTIVOS_FORMA_E1), None)


def usage_de(resp) -> dict:
    u = getattr(resp, "usage", None)
    g = lambda n: int(getattr(u, n, 0) or 0) if u is not None else 0
    return {"input_tokens": g("input_tokens"), "output_tokens": g("output_tokens"),
            "cache_write_tokens": g("cache_creation_input_tokens"), "cache_read_tokens": g("cache_read_input_tokens")}


def bloques_de(resp) -> dict:
    """Conteo de bloques por tipo, el primer tool_use (y cuántos hay), el largo del pensamiento devuelto y un
    fragmento del texto, si lo hay."""
    tipos: dict[str, int] = {}
    tool_use = None
    n_tool = 0
    largo_thinking = 0
    texto = []
    for b in getattr(resp, "content", None) or []:
        t = getattr(b, "type", None)
        tipos[t] = tipos.get(t, 0) + 1
        if t == "tool_use":
            n_tool += 1
            if tool_use is None:
                tool_use = b
        elif t == "thinking":
            largo_thinking += len(getattr(b, "thinking", "") or "")
        elif t == "text":
            texto.append(getattr(b, "text", "") or "")
    return {"bloques": tipos, "n_tool_use": n_tool, "nombre_tool": getattr(tool_use, "name", None) if tool_use else None,
            "tool_input": tool_use.input if tool_use is not None else None,
            "largo_pensamiento_devuelto": largo_thinking,
            "texto": ("\n".join(texto))[:1000] if texto else None}


def resumen_respuesta(resp) -> dict:
    b = bloques_de(resp)
    sd = getattr(resp, "stop_details", None)
    return {"stop_reason": getattr(resp, "stop_reason", None),
            "stop_details": (sd.model_dump(mode="json") if hasattr(sd, "model_dump") else sd) if sd is not None else None,
            "usage": usage_de(resp), "id_respuesta": getattr(resp, "id", None), "modelo_respuesta": getattr(resp, "model", None),
            **{k: v for k, v in b.items() if k != "tool_input"}, "tool_input_crudo": b["tool_input"]}


class PresupuestoC1:
    """Freno duro del presupuesto de la unidad (decisión 4 del «seguí»): un archivo, tope 35, consultado antes de cada
    llamada y actualizado tras cada respuesta real (como runner_corpus.PresupuestoCompartido)."""

    def __init__(self, tope_usd: float, path: Path):
        if tope_usd <= 0:
            raise ValueError("tope positivo")
        self.tope_usd, self.path, self.gasto_usd = tope_usd, Path(path), 0.0
        self.por_corrida: dict[str, float] = {}
        if self.path.exists():
            d = json.loads(self.path.read_text(encoding="utf-8"))
            self.gasto_usd = float(d["gasto_usd"])
            self.por_corrida = dict(d.get("por_corrida") or {})
            if d.get("tope_usd") != tope_usd:
                print(f"[presupuesto] tope persistido {d.get('tope_usd')} ≠ configurado {tope_usd}: manda el configurado", flush=True)
        else:
            self._persistir()

    def excedido(self, proyeccion_usd: float) -> bool:
        return self.gasto_usd + proyeccion_usd > self.tope_usd

    def registrar(self, delta_usd: float, corrida: str) -> None:
        self.gasto_usd += delta_usd
        self.por_corrida[corrida] = self.por_corrida.get(corrida, 0.0) + delta_usd
        self._persistir()

    def _persistir(self) -> None:
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps({"unidad": "U-COMP-E1", "tope_usd": self.tope_usd, "gasto_usd": round(self.gasto_usd, 6),
                                   "por_corrida": {k: round(v, 6) for k, v in self.por_corrida.items()},
                                   "actualizado_utc": ahora()}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        os.replace(tmp, self.path)
