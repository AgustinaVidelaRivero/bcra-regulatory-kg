"""
cliente_c1.py — U-COMP-E1, C1: cliente de los brazos S y O sobre llm_cache.CachingClient (capa sellada, se envuelve,
jamás se edita), con base propia por corrida y namespace propio por brazo, fuera del dominio y del namespace del pipeline
(decisión 3 del «seguí»; skill llm-capture, checklist «dominio nuevo»).

  dominio      comp_e1 (el pipeline usa e1_extraccion)
  namespace    comp_e1|cv=comp-e1-v1-p322c5a23e9b7-<brazo>[-r1]|think=<0 en S, 1 en O>
               (el mismo para las dos corridas del brazo: la clave de una unidad es la misma y cada corrida tiene su
               base, así que la segunda no sale de la caché local; -r1 es el namespace del reintento por respuesta sin
               herramienta o mal formada, el mismo pedido)
  base         <salida>/cache/c1_<brazo>_<corrida>.db
Decisiones de caching (docs/decisiones_caching_extraccion.md): D1, el pedido lo arma el perfil r2b (system como bloque
único con cache_control) y acá viaja tal cual; D2, el gasto se computa con la fórmula de caching sobre los deltas de las
estadísticas de la caché, por respuesta real; D3, cada respuesta real deja una línea de usage con component
comp_e1_<brazo>_c<corrida> en <salida>/cache_usage_c1.jsonl y en logs/cache_usage.jsonl de la raíz desde la que corre;
D4, las corridas van en serie (correr_c1 se ejecuta una vez por corrida); D5, no toca la evaluación.
Los pedidos con max_tokens por encima de cliente_e1.LIMITE_SIN_TRANSMISION (el reintento por corte a 40.960) van por
cliente_e1.AdaptadorTransmision (transmisión con timeout explícito), debajo del CachingClient, como en el perfil r2.
"""
from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path

import comun_c1 as C
import llm_cache as lc  # noqa: E402 — capa sellada, solo import
import cliente_e1  # noqa: E402 — solo AdaptadorTransmision y LIMITE_SIN_TRANSMISION

DOMAIN = "comp_e1"
CODE_VER = "comp-e1-v1"
SUFIJO_REINTENTO = "-r1"
CACHE_USAGE_LOG_RAIZ = C.REPO / "logs" / "cache_usage.jsonl"


class TopeExcedido(RuntimeError):
    pass


def namespace_c1(brazo: str, sufijo: str = "") -> str:
    return lc.make_namespace(DOMAIN, code_ver=f"{CODE_VER}-p{C.PREFIJO}-{brazo}{sufijo}", thinking=(brazo == "O"))


class ClienteC1:
    def __init__(self, brazo: str, corrida: int, db_path: Path, presupuesto: C.PresupuestoC1, log_path: Path, real=None):
        if brazo not in C.MODELOS:
            raise ValueError(brazo)
        if real is None:
            import anthropic  # noqa: PLC0415 — solo con el cliente real
            real = anthropic.Anthropic(max_retries=3)
        self.brazo, self.corrida, self.real = brazo, corrida, real
        self.etiqueta = f"{brazo}{corrida}"
        self.db_path = Path(db_path)
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self.presupuesto, self.log_path = presupuesto, Path(log_path)
        self.p = C.PRECIOS[brazo]
        self.run_label = f"comp_e1_{self.etiqueta}"
        self.componente = f"comp_e1_{brazo}_c{corrida}"
        self._caches: dict[tuple[str, bool], lc.CachingClient] = {}
        self.gasto_usd = 0.0
        self.llamadas = self.llamadas_hit = 0

    def _cache(self, sufijo: str, transmision: bool) -> lc.CachingClient:
        k = (sufijo, transmision)
        if k not in self._caches:
            real = cliente_e1.AdaptadorTransmision(self.real) if transmision else self.real
            self._caches[k] = lc.CachingClient(real, domain=DOMAIN, db_path=self.db_path, namespace=namespace_c1(self.brazo, sufijo),
                                               thinking_enabled=(self.brazo == "O"), run_label=self.run_label)
        return self._caches[k]

    def _proyeccion(self, max_tokens: int) -> float:
        # Conservadora: prefijo entero como escritura de caché (36.000, C0), mensaje variable máximo (6.704, C0) a
        # precio base y la salida al techo del pedido.
        return (36000 * self.p["cw"] + 6704 * self.p["in"] + max_tokens * self.p["out"]) / 1e6

    def _log_usage(self, usage: dict, doc: str, camino: str) -> None:
        line = {"timestamp": datetime.now(timezone.utc).isoformat(), "component": self.componente, "camino": camino, "doc": doc,
                "input_tokens": usage["input_tokens"], "cache_creation_input_tokens": usage["cache_write_tokens"],
                "cache_read_input_tokens": usage["cache_read_tokens"], "output_tokens": usage["output_tokens"]}
        for p in (self.log_path, CACHE_USAGE_LOG_RAIZ):
            p.parent.mkdir(parents=True, exist_ok=True)
            with p.open("a", encoding="utf-8") as f:
                f.write(json.dumps(line, ensure_ascii=False) + "\n")

    def create(self, kwargs: dict, doc: str, sufijo: str = ""):
        """Una llamada (hit o miss) por el camino que corresponde; devuelve (respuesta, info de la llamada)."""
        transmision = (kwargs.get("max_tokens") or 0) > cliente_e1.LIMITE_SIN_TRANSMISION
        cache = self._cache(sufijo, transmision)
        proy = self._proyeccion(kwargs["max_tokens"])
        if self.presupuesto.excedido(proy):
            raise TopeExcedido(f"presupuesto: gasto USD {self.presupuesto.gasto_usd:.4f} + proyección {proy:.4f} supera el tope "
                               f"{self.presupuesto.tope_usd:.2f}")
        antes = dict(cache._stats)
        t0 = datetime.now(timezone.utc)
        resp = cache.messages.create(**kwargs)
        seg = (datetime.now(timezone.utc) - t0).total_seconds()
        despues = cache._stats
        miss = despues["misses"] > antes["misses"]
        usage = C.usage_de(resp)
        delta = 0.0
        self.llamadas += 1
        if miss:
            d_in, d_out = despues["tokens_in"] - antes["tokens_in"], despues["tokens_out"] - antes["tokens_out"]
            d_cw, d_cr = despues["cache_write"] - antes["cache_write"], despues["cache_read"] - antes["cache_read"]
            delta = (d_in * self.p["in"] + d_out * self.p["out"] + d_cw * self.p["cw"] + d_cr * self.p["cr"]) / 1e6
            self.gasto_usd += delta
            self.presupuesto.registrar(delta, self.etiqueta)
            self._log_usage(usage, doc, "transmision" if transmision else "base")
        else:
            self.llamadas_hit += 1
        return resp, {"namespace": cache.namespace, "clave": lc.compute_key(cache.namespace, lc.canonical_request(kwargs)),
                      "max_tokens": kwargs["max_tokens"], "transmision": transmision, "sufijo": sufijo, "miss": miss,
                      "costo_usd": round(delta, 6), "segundos": round(seg, 1), "cuando_utc": t0.isoformat(timespec="seconds")}

    def resumen(self) -> dict:
        return {"brazo": self.brazo, "corrida": self.corrida, "modelo": C.MODELOS[self.brazo], "db": str(self.db_path.name),
                "llamadas": self.llamadas, "hits_cache_local": self.llamadas_hit, "gasto_usd_real": round(self.gasto_usd, 6),
                "precios_por_mtok": self.p, "cache_stats": {f"{k[0] or 'base'}{'|transmision' if k[1] else ''}": c.stats()
                                                            for k, c in self._caches.items()}}

    def close(self) -> None:
        for c in self._caches.values():
            c.close()
