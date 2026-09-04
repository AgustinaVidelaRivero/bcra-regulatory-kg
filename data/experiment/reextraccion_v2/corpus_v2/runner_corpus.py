"""
runner_corpus.py — Corrida de UN CORPUS DECLARADO POR MANIFIESTO por el
pipeline E1→E3 con la arquitectura enmendada (enmienda 01) y la política
laudada A+B. Extiende los runners de la mini-recalibración enm01 con:
multi-TO, reanudación idempotente por unidad persistida, checkpoints
intra-TO, tope global duro y freno por proyección.

U-B5.1: los TOs, el orden, la salida de E0, los límites (tope/estimados/
checkpoints/chequeos de hits) y el modo del censo (con o sin oráculo) salen
del manifiesto de corpus (--manifiesto; default: manifiestos/
desarrollo_5tos.json, cuyos valores son EXACTAMENTE los que este módulo
tenía cableados — paridad verificada en selftest_manifiesto.py). Modelos y
precios siguen siendo materia de la autorización de cada corrida (laudo
D-b del freno 1) y quedan como constantes de este módulo.

Autorización vigente (FASE B de la unidad "corrida del corpus completo"):
  - TOPE DURO GLOBAL: USD 48,50 (estimación FASE A: USD 34,59 × 1,4).
  - E1 (extractor + reintentos): claude-haiku-4-5 — 1,00/5,00/1,25/0,10 USD/MTok.
  - E3 (verificador): claude-sonnet-5 — 2,00/10,00/2,50/0,20 USD/MTok.
  - Orden: pro → cla → ric → cap → ext; SECUENCIAL dentro de cada TO (D4).
  - Freno por proyección al cierre de cada TO + checkpoints intra-TO cada
    150 unidades en cap y ext.
  - En pro: la fase E1 y las verificaciones E3 base deben ser ≈100% hits de
    la caché local (mismos requests que enm01). E1 con gasto > 0,01 ⇒ FRENO.
    Los ciclos de reintento pueden pagarse de nuevo (la política A+B cambia
    el feedback respecto de enm01: solo bloqueantes); techo declarado
    USD 1,00 para la fase E3 de pro ⇒ si se supera, FRENO.

Reanudación idempotente:
  - E1: extracciones_e1.jsonl es append-only; al relanzar se saltean las
    unidades con registro persistido sin error (last-wins por chunk_id) y se
    re-llaman SOLO las erradas/faltantes. La caché local (never-pay-twice)
    hace que nada ya pagado se vuelva a pagar.
  - E3: finales.jsonl es append-only; una unidad con expediente persistido
    (cualquier estado terminal) se saltea entera. Si el proceso muere a mitad
    de un ciclo de ratchet, el ciclo se re-corre completo al relanzar y sus
    llamadas ya pagadas son hits de caché; veredictos.jsonl puede quedar con
    filas duplicadas de esa unidad (se dedupea al agregar, declarado).
  - Contabilidad: estado_corpus.json se reescribe (temp+rename) tras cada
    unidad; el gasto de un proceso muerto entre la llamada y la escritura se
    subestima como máximo en 1 unidad (~USD 0,03), declarado.

La cola humana NO ingresa al grafo (validacion_final=None — principio "nunca
ingreso silencioso"): sus unidades quedan contabilizadas como rechazadas en el
fan-in de E2 y diagnosticadas en el censo.

Uso:
  .venv/bin/python3 runner_corpus.py --autorizado-tope 48.50            # corrida real
  .venv/bin/python3 runner_corpus.py --stub --salida <dir> [--limite N] # prueba offline
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REX = AQUI.parent
sys.path.insert(0, str(REX / "e1_extractor"))
sys.path.insert(0, str(REX / "e3_verificador"))
sys.path.insert(0, str(REX / "e2_reduce"))
sys.path.insert(0, str(REX))

import comun_e1                     # noqa: E402
import prompt_e1                    # noqa: E402
import cliente_e1                   # noqa: E402
import validador_e1                 # noqa: E402
import comun_e3                     # noqa: E402
import prompt_e3                    # noqa: E402
import cliente_e3                   # noqa: E402
import ratchet_e3                   # noqa: E402
import e2_lib                       # noqa: E402
import manifiesto_corpus            # noqa: E402

# --------------------- constantes de autorización por corrida ------------ #
MAX_TOKENS_REINTENTO = 16384        # remedio de fondo (32k) en B5.3

MODEL_E1 = "claude-haiku-4-5"
P_E1 = dict(precio_in_por_mtok=1.00, precio_out_por_mtok=5.00,
            precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10)
MODEL_E3 = "claude-sonnet-5"
P_E3 = dict(precio_in_por_mtok=2.00, precio_out_por_mtok=10.00,
            precio_cache_write_por_mtok=2.50, precio_cache_read_por_mtok=0.20)

EVAL_DIR = comun_e3.REPO / "data" / "experiment" / "evaluacion"
DB_REINTENTOS_E1 = REX / "e3_verificador" / "cache" / "e1_reintentos.db"

# --------------------- configuración por manifiesto (U-B5.1) ------------- #
MANIFIESTO_DEFAULT = REX / "manifiestos" / "desarrollo_5tos.json"

MAN = None
TOS_ORDEN: tuple[str, ...] = ()
TOPE_GLOBAL_USD: float = 0.0
MARGEN_UNIDAD_USD: float = 0.0      # margen pre-unidad (precedente enm01)
ESTIMADO_USD: dict[str, dict] = {}
ESTIMADO_TOTAL_USD: float = 0.0
CHECKPOINT_CADA: dict[str, int] = {}
CHEQUEOS_HITS: list[dict] = []
E0_DIR: Path = comun_e1.E0_SALIDA_ENM01
CENSO_ORACULO_ARG = None            # None = cargar del e0_dir; o SIN_ORACULO
LIMITACIONES: dict | None = None


def configurar(man) -> None:
    """Fija el estado de módulo desde un manifiesto cargado. Se invoca al
    importar (manifiesto de desarrollo — valores idénticos a los cableados
    históricos) y de nuevo en main() con el --manifiesto de la corrida."""
    global MAN, TOS_ORDEN, TOPE_GLOBAL_USD, MARGEN_UNIDAD_USD, ESTIMADO_USD, \
        ESTIMADO_TOTAL_USD, CHECKPOINT_CADA, CHEQUEOS_HITS, E0_DIR, \
        CENSO_ORACULO_ARG, LIMITACIONES
    MAN = man
    TOS_ORDEN = tuple(man.orden_corrida)
    lim = man.limites
    TOPE_GLOBAL_USD = lim["tope_global_usd"]
    MARGEN_UNIDAD_USD = lim["margen_unidad_usd"]
    ESTIMADO_USD = lim["estimado_usd"]
    ESTIMADO_TOTAL_USD = round(
        sum(f["e1"] + f["e3"] for f in ESTIMADO_USD.values()), 3)
    CHECKPOINT_CADA = dict(lim["checkpoint_cada"])
    CHEQUEOS_HITS = list(lim["chequeos_hits"])
    E0_DIR = man.e0_salida
    CENSO_ORACULO_ARG = None if man.tiene_oraculo else e2_lib.SIN_ORACULO
    LIMITACIONES = man.limitaciones_e0()


configurar(manifiesto_corpus.cargar(MANIFIESTO_DEFAULT))


class Freno(RuntimeError):
    pass


# ----------------------------- stubs offline ----------------------------- #
class _StubUsage:
    input_tokens = 0
    output_tokens = 0
    cache_creation_input_tokens = 0
    cache_read_input_tokens = 0


class _StubResp:
    def __init__(self, tool_input, nombre_tool):
        class B:
            type = "tool_use"
        b = B()
        b.name = nombre_tool
        b.input = tool_input
        self.content = [b]
        self.stop_reason = "tool_use"
        self.usage = _StubUsage()


class StubE1Corpus:
    """Stub E1 para el selftest del runner: extracción mínima válida por
    chunk. Interfaz dual: .create(doc=..., **kw) y .messages.create(**kw)."""

    def __init__(self):
        self.messages = self
        self.llamadas = 0
        self.llamadas_hit = 0
        self.gasto_usd = 0.0
        self.chunk_ids_llamados: list[str] = []

    def create(self, doc=None, **kwargs):
        self.llamadas += 1
        msg = kwargs["messages"][0]["content"]
        # el punto propio viene en el mensaje canónico; lo recuperamos del
        # renglón "Punto del chunk:" (hijo) / "Unidad de origen:" (mini)
        punto = None
        for linea in msg.splitlines():
            if linea.startswith(("Punto del chunk:", "Unidad de origen:")):
                punto = linea.split(":", 1)[1].strip().split(" ", 1)[0]
                break
        tool_input = {
            "entities": [{"local_id": "e1", "type": "Obligacion",
                          "label": f"obligacion stub {punto}",
                          "punto": punto, "properties": {}}],
            "relations": [],
            "omisiones_no_prosa": [],
        }
        self.chunk_ids_llamados.append(punto)
        return _StubResp(tool_input, prompt_e1.NOMBRE_TOOL)

    def resumen(self):
        return {"llamadas": self.llamadas, "hits_cache_local": self.llamadas_hit,
                "gasto_usd_real": 0.0, "stub": True}

    def close(self):
        pass


class StubE3Corpus:
    """Stub E3: siempre completo_ok (el flujo de ratchet con faltantes ya
    está cubierto por selftest_e3; acá se prueba la mecánica del runner)."""

    def __init__(self):
        self.messages = self
        self.llamadas = 0
        self.llamadas_hit = 0
        self.gasto_usd = 0.0

    def create(self, doc=None, **kwargs):
        self.llamadas += 1
        return _StubResp({"veredicto": "completo_ok", "faltantes": []},
                         prompt_e3.NOMBRE_TOOL)

    def resumen(self):
        return {"llamadas": self.llamadas, "stub": True}

    def close(self):
        pass


# ----------------------------- persistencia ------------------------------ #
def cargar_jsonl_last_wins(path: Path) -> dict[str, dict]:
    """chunk_id → último registro persistido (dedup last-wins)."""
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


class Estado:
    """Ledger global de gasto + fase actual; reescritura atómica por unidad."""

    def __init__(self, salida: Path):
        self.path = salida / "estado_corpus.json"
        if self.path.exists():
            self.d = json.loads(self.path.read_text(encoding="utf-8"))
        else:
            self.d = {"fases_cerradas": {}, "fase_actual": None,
                      "tope_global_usd": TOPE_GLOBAL_USD,
                      "estimado_total_usd": ESTIMADO_TOTAL_USD}

    def persistir(self) -> None:
        tmp = self.path.with_suffix(".json.tmp")
        tmp.write_text(json.dumps(self.d, ensure_ascii=False, indent=1),
                       encoding="utf-8")
        os.replace(tmp, self.path)

    def abrir_fase(self, key: str) -> float:
        """Devuelve el gasto previo de esta fase (de intentos anteriores)."""
        fa = self.d.get("fase_actual")
        previo = 0.0
        if fa and fa["key"] == key:
            previo = fa.get("gasto_previo_usd", 0.0) + fa.get("gasto_proceso_usd", 0.0)
        self.d["fase_actual"] = {"key": key, "gasto_previo_usd": round(previo, 6),
                                 "gasto_proceso_usd": 0.0, "unidades_hechas": 0}
        self.persistir()
        return previo

    def tick(self, gasto_proceso: float, unidades: int) -> None:
        fa = self.d["fase_actual"]
        fa["gasto_proceso_usd"] = round(gasto_proceso, 6)
        fa["unidades_hechas"] = unidades
        self.persistir()

    def cerrar_fase(self, key: str, resumen: dict) -> None:
        fa = self.d["fase_actual"]
        assert fa and fa["key"] == key
        gasto = fa["gasto_previo_usd"] + fa["gasto_proceso_usd"]
        self.d["fases_cerradas"][key] = {"gasto_usd": round(gasto, 6),
                                         "resumen": resumen}
        self.d["fase_actual"] = None
        self.persistir()

    def gasto_global(self) -> float:
        g = sum(f["gasto_usd"] for f in self.d["fases_cerradas"].values())
        fa = self.d.get("fase_actual")
        if fa:
            g += fa["gasto_previo_usd"] + fa["gasto_proceso_usd"]
        return g

    def fase_cerrada(self, key: str) -> bool:
        return key in self.d["fases_cerradas"]


# ----------------------------- proyección/freno -------------------------- #
def proyeccion(estado: Estado, fase_key: str | None, frac: float) -> dict:
    """Proyección del total con factor conservador (ratio real/estimado sobre
    lo YA PAGADO, excluyendo pro — cuyos hits distorsionarían a la baja)."""
    real_global = estado.gasto_global()
    est_corrido = est_corrido_pagado = real_pagado = 0.0
    for key, f in estado.d["fases_cerradas"].items():
        to, fase = key.split(":")
        est = ESTIMADO_USD[to][fase]
        est_corrido += est
        if to != "pro":
            est_corrido_pagado += est
            real_pagado += f["gasto_usd"]
    if fase_key:
        to, fase = fase_key.split(":")
        est = ESTIMADO_USD[to][fase] * frac
        est_corrido += est
        fa = estado.d["fase_actual"]
        if to != "pro" and fa:
            est_corrido_pagado += est
            real_pagado += fa["gasto_previo_usd"] + fa["gasto_proceso_usd"]
    ratio = (real_pagado / est_corrido_pagado) if est_corrido_pagado > 0.5 else 1.0
    factor = max(1.0, ratio)
    est_restante = max(0.0, ESTIMADO_TOTAL_USD - est_corrido)
    proy = real_global + factor * est_restante
    return {"gasto_real_global_usd": round(real_global, 4),
            "estimado_corrido_usd": round(est_corrido, 4),
            "ratio_real_vs_estimado_pagado": round(ratio, 4),
            "factor_freno": round(factor, 4),
            "estimado_restante_usd": round(est_restante, 4),
            "proyeccion_total_usd": round(proy, 4),
            "tope_global_usd": TOPE_GLOBAL_USD}


def checkpoint(salida: Path, estado: Estado, to: str, fase: str,
               n: int, total: int, etiqueta: str) -> dict:
    p = proyeccion(estado, f"{to}:{fase}", n / total if total else 1.0)
    reg = {"ts": time.strftime("%Y-%m-%dT%H:%M:%S%z"),
           "to": to, "fase": fase, "unidades": f"{n}/{total}",
           "etiqueta": etiqueta, **p}
    cdir = salida / "checkpoints"
    cdir.mkdir(parents=True, exist_ok=True)
    (cdir / f"checkpoint_{to}_{fase}_{etiqueta}.json").write_text(
        json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    (salida / "ultimo_checkpoint.json").write_text(
        json.dumps(reg, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"CHECKPOINT [{to}:{fase} {n}/{total}] gasto=USD "
          f"{p['gasto_real_global_usd']:.2f} proyección=USD "
          f"{p['proyeccion_total_usd']:.2f} (tope {TOPE_GLOBAL_USD})", flush=True)
    if p["proyeccion_total_usd"] > TOPE_GLOBAL_USD:
        raise Freno(f"proyección USD {p['proyeccion_total_usd']:.2f} supera el "
                    f"tope global USD {TOPE_GLOBAL_USD:.2f} en {to}:{fase} {n}/{total}")
    return reg


# ----------------------------- fase E1 ----------------------------------- #
def llamar_con_reintentos_api(fn, descripcion: str, max_intentos: int = 3):
    """Reintento ante errores transitorios de API (la corrida es desatendida).
    TopeExcedido NO se reintenta: es freno."""
    esperas = (20, 60, 180)
    ultimo = None
    for i in range(max_intentos):
        try:
            return fn(), None
        except (cliente_e1.TopeExcedido, cliente_e3.TopeExcedido):
            raise
        except Exception as e:  # noqa: BLE001 — transitorios de red/API
            ultimo = f"{type(e).__name__}: {e}"
            print(f"  error API en {descripcion} (intento {i+1}/{max_intentos}): "
                  f"{ultimo}", flush=True)
            if i < max_intentos - 1:
                time.sleep(esperas[i])
    return None, ultimo


def fase_e1(to: str, cliente, estado: Estado, salida: Path,
            limite: int | None, abortar_tras: int | None,
            checkpoint_cada: int | None) -> None:
    key = f"{to}:e1"
    tdir = salida / to
    tdir.mkdir(parents=True, exist_ok=True)
    jsonl = tdir / "extracciones_e1.jsonl"

    chunks = comun_e1.cargar_chunks((to,), e0_dir=E0_DIR)
    if limite:
        chunks = chunks[:limite]
    previos = cargar_jsonl_last_wins(jsonl)
    hechas_ok = {cid for cid, r in previos.items() if r.get("error") is None}
    pendientes = [c for c in chunks if c["id"] not in hechas_ok]
    print(f"[{key}] unidades={len(chunks)} ya_persistidas_ok={len(hechas_ok)} "
          f"pendientes={len(pendientes)}", flush=True)

    gasto_previo = estado.abrir_fase(key)
    errores_consecutivos = 0
    procesadas = len(hechas_ok)
    hechas_este_proceso = 0
    for c in pendientes:
        if estado.gasto_global() + MARGEN_UNIDAD_USD > TOPE_GLOBAL_USD:
            raise Freno(f"tope global antes de {c['id']}: gasto USD "
                        f"{estado.gasto_global():.4f} + margen {MARGEN_UNIDAD_USD}")
        kwargs = prompt_e1.build_request_kwargs(c, model=MODEL_E1)
        resp, err = llamar_con_reintentos_api(
            lambda: cliente.create(doc=c["archivo"], **kwargs), c["id"])
        if resp is not None:
            u = resp.usage
            usage = {"input_tokens": getattr(u, "input_tokens", 0) or 0,
                     "output_tokens": getattr(u, "output_tokens", 0) or 0,
                     "cache_write_tokens": getattr(u, "cache_creation_input_tokens", 0) or 0,
                     "cache_read_tokens": getattr(u, "cache_read_input_tokens", 0) or 0}
            stop = getattr(resp, "stop_reason", None)
            tool_input = next((b.input for b in resp.content
                               if getattr(b, "type", None) == "tool_use"), None)
            if tool_input is None:
                err = f"no_tool_use stop_reason={stop}"
            elif stop == "max_tokens":
                err = "max_tokens_hit"
        else:
            usage, stop, tool_input = {"input_tokens": 0, "output_tokens": 0,
                                       "cache_write_tokens": 0,
                                       "cache_read_tokens": 0}, None, None
        val = (validador_e1.validar_salida(tool_input, c).as_dict()
               if tool_input is not None else None)
        append_jsonl(jsonl, {
            "chunk_id": c["id"], "unidad": c["unidad"], "tipo_unidad": c["tipo"],
            "titulo": c["titulo"], "stop_reason": stop, "error": err,
            "usage": usage, "tool_input_crudo": tool_input, "validacion": val})
        procesadas += 1
        hechas_este_proceso += 1
        estado.tick(cliente.gasto_usd, procesadas)
        errores_consecutivos = 0 if err is None else errores_consecutivos + 1
        if errores_consecutivos > 5:
            raise Freno(f"{key}: más de 5 errores de API consecutivos "
                        f"(último: {err}) — problema sistémico, se frena")
        if procesadas % 25 == 0 or err:
            print(f"[{key} {procesadas}/{len(chunks)}] {c['id']:<28s} "
                  f"gasto_fase=USD {gasto_previo + cliente.gasto_usd:.4f}"
                  + (f" ERROR {err}" if err else ""), flush=True)
        if checkpoint_cada and procesadas % checkpoint_cada == 0:
            checkpoint(salida, estado, to, "e1", procesadas, len(chunks),
                       f"u{procesadas}")
        if abortar_tras and hechas_este_proceso >= abortar_tras:
            print(f"[{key}] ABORT SIMULADO tras {hechas_este_proceso} unidades "
                  f"de este proceso", flush=True)
            sys.exit(9)

    resumen = {"n_unidades": len(chunks),
               "cliente": cliente.resumen(),
               "gasto_fase_usd": round(gasto_previo + cliente.gasto_usd, 4)}
    (tdir / "resumen_e1.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    estado.cerrar_fase(key, {"gasto_usd": resumen["gasto_fase_usd"],
                             "n": len(chunks)})
    checkpoint(salida, estado, to, "e1", len(chunks), len(chunks), "cierre")


# ----------------------------- fase E3 ----------------------------------- #
def compactar_e1(to: str, salida: Path) -> Path:
    """extracciones_e1.jsonl (append-only, posibles duplicados por reanudación)
    → compactado determinístico en orden documental, last-wins."""
    tdir = salida / to
    regs = cargar_jsonl_last_wins(tdir / "extracciones_e1.jsonl")
    chunks = comun_e1.cargar_chunks((to,), e0_dir=E0_DIR)
    out = tdir / "extracciones_e1_compact.jsonl"
    with out.open("w", encoding="utf-8") as f:
        for c in chunks:
            if c["id"] in regs:
                f.write(json.dumps(regs[c["id"]], ensure_ascii=False) + "\n")
    return out


def fase_e3(to: str, cli_e3, cli_e1r, estado: Estado, salida: Path,
            limite: int | None, abortar_tras: int | None,
            checkpoint_cada: int | None) -> None:
    key = f"{to}:e3"
    tdir = salida / to
    finales = tdir / "finales.jsonl"

    chunks = comun_e3.cargar_chunks((to,), e0_dir=E0_DIR)
    if limite:
        chunks = chunks[:limite]
    unidades_corpus = {c["unidad"] for c in chunks}
    compact = compactar_e1(to, salida)
    regs = comun_e3.cargar_extracciones(compact)
    pares = comun_e3.pares_de(chunks, regs)

    previos = cargar_jsonl_last_wins(finales)
    pendientes = [(c, v) for c, v in pares if c["id"] not in previos]
    print(f"[{key}] aceptadas_e1={len(pares)} ya_persistidas={len(previos)} "
          f"pendientes={len(pendientes)}", flush=True)

    gasto_previo = estado.abrir_fase(key)
    registro = ratchet_e3.RegistroE3(tdir)
    procesadas = len(previos)
    hechas_este_proceso = 0
    for c, val in pendientes:
        gasto_fase = gasto_previo + cli_e3.gasto_usd + cli_e1r.gasto_usd
        if estado.gasto_global() + MARGEN_UNIDAD_USD > TOPE_GLOBAL_USD:
            raise Freno(f"tope global antes de {c['id']}: gasto USD "
                        f"{estado.gasto_global():.4f} + margen {MARGEN_UNIDAD_USD}")
        exp, err = llamar_con_reintentos_api(
            lambda: ratchet_e3.ciclo_ratchet(
                c, val, cliente_verificador=cli_e3, cliente_extractor=cli_e1r,
                model_e3=MODEL_E3, model_e1=MODEL_E1, registro=registro,
                max_tokens_reintento=MAX_TOKENS_REINTENTO,
                unidades_corpus=unidades_corpus),
            c["id"])
        if exp is None:
            raise Freno(f"{key}: ciclo de ratchet de {c['id']} falló tras "
                        f"reintentos de API ({err}) — se frena para no dejar "
                        f"huecos silenciosos; relanzar reanuda acá")
        append_jsonl(finales, {
            "chunk_id": c["id"], "tipo_unidad": c["tipo"],
            "estado": exp["estado"], "n_reintentos": len(exp["reintentos"]),
            "residuales": exp["residuales"],
            "validacion_final": exp["validacion_final"]})
        procesadas += 1
        hechas_este_proceso += 1
        estado.tick(cli_e3.gasto_usd + cli_e1r.gasto_usd, procesadas)
        if procesadas % 25 == 0:
            print(f"[{key} {procesadas}/{len(pares)}] {c['id']:<28s} "
                  f"{exp['estado']:<28s} gasto_fase=USD "
                  f"{gasto_previo + cli_e3.gasto_usd + cli_e1r.gasto_usd:.4f}",
                  flush=True)
        if checkpoint_cada and procesadas % checkpoint_cada == 0:
            checkpoint(salida, estado, to, "e3", procesadas, len(pares),
                       f"u{procesadas}")
        if abortar_tras and hechas_este_proceso >= abortar_tras:
            print(f"[{key}] ABORT SIMULADO tras {hechas_este_proceso} unidades "
                  f"de este proceso", flush=True)
            sys.exit(9)

    todos = cargar_jsonl_last_wins(finales)
    estados = Counter(r["estado"] for r in todos.values())
    resumen = {"n_unidades_e3": len(pares),
               "estados": dict(estados),
               "cliente_e3": cli_e3.resumen(),
               "cliente_e1_reintentos": cli_e1r.resumen(),
               "gasto_fase_usd": round(gasto_previo + cli_e3.gasto_usd
                                       + cli_e1r.gasto_usd, 4)}
    (tdir / "resumen_e3.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    estado.cerrar_fase(key, {"gasto_usd": resumen["gasto_fase_usd"],
                             "n": len(pares), "estados": dict(estados)})
    checkpoint(salida, estado, to, "e3", len(pares), len(pares), "cierre")


# ----------------------------- E2 por TO --------------------------------- #
def cerrar_e2(to: str, salida: Path, limite: int | None = None) -> dict:
    """Construye el jsonl FINAL del TO (post-E3: aceptadas con su validación
    final; cola humana y rechazos E1 como registros rechazados contabilizados)
    y corre reducir(): fan-in + ensamblado + censo contra el mapa enm01."""
    tdir = salida / to
    regs_e1 = cargar_jsonl_last_wins(tdir / "extracciones_e1_compact.jsonl")
    finales = cargar_jsonl_last_wins(tdir / "finales.jsonl")
    chunks = comun_e1.cargar_chunks((to,), e0_dir=E0_DIR)
    if limite:
        chunks = chunks[:limite]

    path_final = tdir / f"extracciones_finales_{to}.jsonl"
    with path_final.open("w", encoding="utf-8") as f:
        for c in chunks:
            cid = c["id"]
            if cid in finales and finales[cid]["validacion_final"] is not None:
                f.write(json.dumps({
                    "chunk_id": cid, "error": None,
                    "estado_e3": finales[cid]["estado"],
                    "validacion": finales[cid]["validacion_final"]},
                    ensure_ascii=False) + "\n")
            elif cid in finales:  # cola humana: NO ingresa al grafo
                f.write(json.dumps({
                    "chunk_id": cid, "error": f"cola_humana:{finales[cid]['estado']}",
                    "estado_e3": finales[cid]["estado"], "validacion": None},
                    ensure_ascii=False) + "\n")
            elif cid in regs_e1:  # rechazado en E1 (nunca llegó a E3)
                f.write(json.dumps(regs_e1[cid], ensure_ascii=False) + "\n")
    # con --limite (solo pruebas) el fan-in es parcial por construcción; la
    # corrida real va SIN flag: un ausente inesperado aborta como debe.
    res = e2_lib.reducir(to, path_final, permitir_parcial=bool(limite),
                         censo_oraculo=CENSO_ORACULO_ARG, e0_dir=E0_DIR,
                         limitaciones=LIMITACIONES)
    (tdir / f"grafo_{to}.json").write_text(res["grafo_json"], encoding="utf-8")
    (tdir / f"reporte_e2_{to}.json").write_text(
        json.dumps(res["reporte"], ensure_ascii=False, indent=1), encoding="utf-8")
    (tdir / f"censo_{to}.json").write_text(
        json.dumps(res["censo"], ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[{to}:e2] nodos={res['reporte']['nodes_total']} "
          f"aristas={res['reporte']['edges_total']} "
          f"sha256={res['reporte']['sha256_grafo'][:12]}", flush=True)
    return res["reporte"]


# ----------------------------- chequeo de hits --------------------------- #
def chequear_hits(to: str, chk: dict, estado: Estado, stub: bool) -> None:
    """Chequeo de hits declarado en el manifiesto (limites.chequeos_hits):
    umbrales de gasto por fase para un TO cuyas llamadas deberían ser hits de
    la caché local (precedente: pro en la corrida del corpus de desarrollo)."""
    if stub:
        return
    e1_max, e3_max = chk["e1_max_usd"], chk["e3_max_usd"]
    g_e1 = estado.d["fases_cerradas"][f"{to}:e1"]["gasto_usd"]
    g_e3 = estado.d["fases_cerradas"][f"{to}:e3"]["gasto_usd"]
    if g_e1 > e1_max:
        raise Freno(f"{to}:e1 gastó USD {g_e1:.4f} > {e1_max} — se "
                    f"esperaban ≈100% hits locales; algo cambió")
    if g_e3 > e3_max:
        raise Freno(f"{to}:e3 gastó USD {g_e3:.4f} > {e3_max} — más "
                    f"que el techo esperado de los ciclos de reintento nuevos "
                    f"bajo la política A+B; algo cambió")
    print(f"[{to}] chequeo de hits OK: e1=USD {g_e1:.4f} (≤{e1_max}) "
          f"e3=USD {g_e3:.4f} (≤{e3_max})", flush=True)


# ----------------------------- main -------------------------------------- #
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stub", action="store_true", help="clientes stub, offline")
    ap.add_argument("--autorizado-tope", type=float, default=None,
                    help="eco de la autorización; debe igualar el "
                         "tope_global_usd del manifiesto para corrida real")
    ap.add_argument("--salida", type=Path, default=AQUI / "salida")
    ap.add_argument("--tos", type=str, default=None,
                    help="subconjunto de TOs (default: todos, en el orden "
                         "del manifiesto)")
    ap.add_argument("--limite", type=int, default=None,
                    help="solo primeras N unidades por TO (pruebas)")
    ap.add_argument("--abortar-tras", type=int, default=None,
                    help="sys.exit(9) tras N unidades por fase (prueba de reanudación)")
    ap.add_argument("--checkpoint-cada", type=int, default=None,
                    help="override del intervalo de checkpoint intra-TO")
    ap.add_argument("--manifiesto", type=Path, default=MANIFIESTO_DEFAULT,
                    help="manifiesto de corpus (U-B5.1); default: el de "
                         "desarrollo (5 TOs)")
    args = ap.parse_args()

    if args.manifiesto != MANIFIESTO_DEFAULT:
        configurar(manifiesto_corpus.cargar(args.manifiesto))

    tos = ([t.strip() for t in args.tos.split(",") if t.strip()]
           if args.tos else list(TOS_ORDEN))
    assert all(t in TOS_ORDEN for t in tos), tos

    if not args.stub:
        if args.autorizado_tope != TOPE_GLOBAL_USD:
            print(f"corrida real exige --autorizado-tope {TOPE_GLOBAL_USD} "
                  f"(eco de la autorización, igual al tope_global_usd del "
                  f"manifiesto)")
            return 2
        from dotenv import load_dotenv
        load_dotenv(EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            print(f"ANTHROPIC_API_KEY ausente (esperada en {EVAL_DIR / '.env'})")
            return 1

    args.salida.mkdir(parents=True, exist_ok=True)
    estado = Estado(args.salida)
    t0 = time.time()
    print(f"corrida corpus_v2 | manifiesto={MAN.nombre} | stub={args.stub} "
          f"| tope global=USD {TOPE_GLOBAL_USD} | estimado=USD "
          f"{ESTIMADO_TOTAL_USD} | orden={tos} "
          f"| prefijos: E1 {prompt_e1.PREFIJO_HASH} E3 {prompt_e3.PREFIJO_HASH}",
          flush=True)

    try:
        for to in tos:
            ck = args.checkpoint_cada or CHECKPOINT_CADA.get(to)
            # ------- fase E1 -------
            if estado.fase_cerrada(f"{to}:e1"):
                print(f"[{to}:e1] ya cerrada — se saltea", flush=True)
            else:
                if args.stub:
                    cli = StubE1Corpus()
                else:
                    restante = TOPE_GLOBAL_USD - estado.gasto_global()
                    cli = cliente_e1.ClienteE1Real(
                        **P_E1, tope_usd=round(restante, 4),
                        run_label=f"corpus_{to}_e1")
                try:
                    fase_e1(to, cli, estado, args.salida, args.limite,
                            args.abortar_tras, ck)
                finally:
                    cli.close()
            # ------- fase E3 (incluye reintentos E1) -------
            if estado.fase_cerrada(f"{to}:e3"):
                print(f"[{to}:e3] ya cerrada — se saltea", flush=True)
            else:
                if args.stub:
                    c3, c1 = StubE3Corpus(), StubE1Corpus()
                else:
                    restante = TOPE_GLOBAL_USD - estado.gasto_global()
                    c3 = cliente_e3.ClienteE3Real(
                        **P_E3, tope_usd=round(restante, 4),
                        run_label=f"corpus_{to}_e3")
                    c1 = cliente_e1.ClienteE1Real(
                        **P_E1, tope_usd=round(restante, 4),
                        run_label=f"corpus_{to}_reintentos_e1",
                        db_path=DB_REINTENTOS_E1)
                try:
                    fase_e3(to, c3, c1, estado, args.salida, args.limite,
                            args.abortar_tras, ck)
                finally:
                    c3.close()
                    c1.close()
            # ------- E2 del TO (offline) + chequeos -------
            cerrar_e2(to, args.salida, args.limite)
            for chk in CHEQUEOS_HITS:
                if chk["to"] == to:
                    chequear_hits(to, chk, estado, args.stub)
    except Freno as e:
        print(f"\nFRENO: {e}", flush=True)
        estado.persistir()
        return 3

    print(f"\ncorrida completa: gasto global=USD {estado.gasto_global():.4f} "
          f"| wall={round((time.time()-t0)/60, 1)} min", flush=True)
    print("siguiente paso: ensamblar_corpus.py (kg.json global + tests de "
          "respuesta conocida)", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
