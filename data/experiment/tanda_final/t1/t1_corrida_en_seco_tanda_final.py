"""
t1_corrida_en_seco_tanda_final.py — B6.1, tanda final, T1, puntos 2.5, 2.6 y 2.7 (pre-registro firmado de la tanda
final, §4.1, puntos 1, 2 y 4): la corrida en seco de T2 con `--stub`, las unidades que no entran en una llamada con el
censo de unidades grandes, y el estimado por TO. USD 0, sin red, sin clave de la API. El modelo es
`data/experiment/tanda1/t1/t1_corrida_en_seco.py` (que sigue a `reext_t0/t1_corrida_en_seco.py`, con la lección de su
T2; CLAUDE.md §4.l): el mismo camino que el runner. Cambia la raíz: el script no está en la copia (la cláusula del
despacho excluye tanda_final/), y la copia se pasa con --raiz.

El camino. Importa `runner_corpus.py` de la copia desde su archivo y llama a su `main()` con el comando de T2 más
`--stub` (sin `--tos`: los 98, en el orden del manifiesto; con --tos, los que se pidan, en ese orden). Del `sys.path` solo pone en `sys.path[0]` la carpeta del
runner, que es lo que hace `python runner_corpus.py` (de ahí importa `cerrar_e2_r2` a `r1_e4`); el resto lo arma el
runner (`runner_corpus.py:64-69`). No llama a `configurar` ni a ninguna fase por fuera.

Lo que se reemplaza: las dos clases stub del runner (`StubE1Corpus` y `StubE3Corpus`, que `main()` construye con
`--stub`) por subclases que registran cada pedido (modelo, max_tokens, temperatura, namespace y clave de caché) y
devuelven, para unidades elegidas, las respuestas de cada rama:
  - corte: con la hipótesis de la salida por carácter del p90 de la tanda 0 (1,5051 tokens por carácter de texto
    propio; `reext_t0/freno_t2.md:12`), un pedido corta (stop_reason max_tokens) si chars_propio × 1,5051 pasa su
    max_tokens. Así cada unidad grande recorre en el runner su mecanismo real: reintento por corte (16.384), partición
    por corte (`correr_e0.particionar_por_corte`) o tercer escalón (40.960). Si la E0 no trae un caso natural de una
    rama, se fuerza en la unidad mayor que la toma, y se declara;
  - reintento: el del ratchet de E3 (un faltante de severidad alta con una cita verificable de la unidad, después
    completo_ok) y el reintento por corte de arriba;
  - salida mal formada: tres unidades chicas sin `relations` en el primer intento, la primera elegible de cada uno de
    los tres primeros TOs del orden que tienen una; en una el `-rforma1` sale bien, en otra el `-rforma1` y el
    `-rforma2` salen sin `relations` y la unidad se repara (T2-ter), y en la tercera el `-rforma2` trae `entities` que
    no es lista y la unidad queda con `salida_mal_formada_tras_reintento`. El ratchet va en la siguiente elegible del
    primero de esos TOs que tenga otra.
  El stub de E1 tiene además `crear_reintento_forma`, como el cliente real (`cliente_e1.py:285`), para que
  `cliente_e1.crear_reintento_forma` tome la misma rama que con el cliente real y el namespace del reintento quede
  registrado; el stub del runner no lo tiene y despacha por `messages.create`.
Ningún cliente real se construye: el constructor de `ClienteE1Real` y el de `ClienteE3Real` quedan reemplazados por
una función que cuenta y frena (las clases quedan, porque `cliente_e1._crear` despacha con `isinstance`),
`anthropic.Anthropic` también, y la red queda bloqueada (`socket.connect`, `socket.create_connection`). La clave
no está en el entorno y la copia no tiene `.env`.

Con --stub-con-texto-ordenado (solo para la salida que alimenta la prueba del ensamblado, punto 2.8), cada respuesta del
stub de E1 suma la entidad TextoOrdenado del documento (`properties.archivo`, la clave de E2, e2_lib.entity_slug_v3), que
E1 real emite y el stub del runner no: sin ella, `ensamblar_tanda0.derivar_establecida_en` deja las aristas
`establecida_en` colgantes (I4).

Salidas (en --salida, fuera de la copia; ninguna lleva texto de unidades):
  corrida_en_seco_t1.json        rc, llamadas a la API, pedidos por etapa (modelos, max_tokens, temperaturas, claves
                                 distintas, namespaces), claves ya en las bases de la copia, las ramas recorridas;
  pedidos_t1.jsonl               un renglón por pedido a un stub (sin el mensaje);
  censo_unidades_grandes_t1.json la clase A y el censo (punto 2.6);
  estimado_por_to_t1.json        el estimado por TO, con la tarifa del §3, contra el del manifiesto y el tope (punto 2.7);
  runner/                        la --salida del runner (sintética).
La salida de pantalla del runner va a stdout; el resumen de este script, a stderr.

Uso:
  env -u ANTHROPIC_API_KEY PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B \
      t1_corrida_en_seco_tanda_final.py --raiz <copia> --salida <dir> > <consola del runner>
"""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import os
import socket
import sqlite3
import sys
from collections import Counter
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True
COPIA = Path()                                  # la fija main() con --raiz
RUNNER = Path()
MANIFIESTO_REL = "data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json"
MEDICION_A3_REL = "data/experiment/alcance_e1/a3/salidas/medicion_mensajes_tres_tandas_a3.json"

RAZON_MEDIANA, RAZON_P90 = 1.1582, 1.5051      # reext_t0/freno_t2.md:12 (decisión 4: la p90)
TARIFA_E1, TARIFA_E3 = Decimal("0.010135"), Decimal("0.010980")
P_SALIDA_E1 = 5.00                             # USD por millón de tokens de salida de E1 (runner_corpus.py:92)
UMBRAL_HC = 26182                              # healthcheck_e0.UMBRAL_CHARS_TERMINAL


class ErrorDelStub(BaseException):
    """Un error dentro de los stubs: sale de main() sin pasar por el reintento de API del runner
    (`llamar_con_reintentos_api` atrapa Exception y espera 20 y 60 s entre intentos)."""


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def texto_mensaje(kw: dict) -> str:
    m = kw["messages"][0]["content"]
    if isinstance(m, list):
        return "\n".join(b.get("text", "") for b in m if isinstance(b, dict))
    return m


# ------------------------------------------------------------------ guardas
def guardas() -> dict:
    prohibidos = [str(Path(r, n).relative_to(COPIA)) for r, _, fs in os.walk(COPIA) for n in fs
                  if n == ".env" or n.startswith(".env.") or n.endswith(".env") or n.startswith("NO_ABRIR_")
                  or "_SOLO_MESA" in n]
    if prohibidos:
        raise SystemExit(f"la copia trae {len(prohibidos)} archivos .env, NO_ABRIR_ o _SOLO_MESA: se frena")
    os.environ.pop("ANTHROPIC_API_KEY", None)
    cuenta = {"socket": 0, "anthropic": 0, "cliente_real": 0}

    def sin_red(*a, **k):
        cuenta["socket"] += 1
        raise RuntimeError("red bloqueada en la corrida en seco")
    socket.socket.connect = sin_red
    socket.create_connection = sin_red
    import anthropic

    class AnthropicProhibido:
        def __init__(self, *a, **k):
            cuenta["anthropic"] += 1
            raise RuntimeError("cliente de la API construido en la corrida en seco")
    anthropic.Anthropic = AnthropicProhibido
    return cuenta


def cargar_runner():
    sys.path[0] = str(RUNNER.parent)          # el modo script de `python runner_corpus.py`
    spec = importlib.util.spec_from_file_location("runner_corpus", RUNNER)
    rc = importlib.util.module_from_spec(spec)
    sys.modules["runner_corpus"] = rc
    spec.loader.exec_module(rc)
    return rc


def main() -> int:
    global COPIA, RUNNER
    ap = argparse.ArgumentParser()
    ap.add_argument("--raiz", type=Path, required=True, help="la raíz de la copia")
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--tos", default=None, help="el --tos del runner (para la salida stub de un tramo)")
    ap.add_argument("--stub-con-texto-ordenado", action="store_true",
                    help="solo para la salida que alimenta la prueba del ensamblado (punto 2.8): cada respuesta del stub "
                         "de E1 suma la entidad TextoOrdenado del documento, como la emite E1 real")
    a = ap.parse_args()
    COPIA = a.raiz.resolve()
    RUNNER = COPIA / "data" / "experiment" / "reextraccion_v2" / "corpus_v2" / "runner_corpus.py"
    sal = a.salida.resolve()
    if sal.is_relative_to(COPIA):
        raise SystemExit("--salida no puede estar dentro de la copia")
    sal.mkdir(parents=True, exist_ok=False)
    cuenta = guardas()
    os.chdir(COPIA)
    RC = cargar_runner()
    import correr_e0                          # del sys.path que armó el runner (e0_chunking)
    import llm_cache as lc                    # ídem (evaluacion, por comun_e3)
    import ratchet_e3
    import prompt_e3
    cliente_e1, cliente_e3 = RC.cliente_e1, RC.cliente_e3

    def real_prohibido(self, *a, **k):
        cuenta["cliente_real"] += 1
        raise RuntimeError("cliente real construido en la corrida en seco")
    # se tapa el constructor y no la clase: cliente_e1._crear despacha con isinstance(cliente, ClienteE1Real)
    RC.cliente_e1.ClienteE1Real.__init__ = real_prohibido
    RC.cliente_e3.ClienteE3Real.__init__ = real_prohibido

    # ---------------------------------------------------- las unidades y sus mensajes (sin texto en la salida)
    man = RC.manifiesto_corpus.cargar(COPIA / MANIFIESTO_REL)
    pf = RC.perfil_e1.perfil(man.perfil_e1)
    e0 = COPIA / man._d["rutas"]["e0_salida"]
    orden = list(man.orden_corrida) if not a.tos else [t for t in a.tos.split(",") if t]
    assert all(t in man.orden_corrida for t in orden), orden
    por_to = {to: RC.chunks_sin_ids_repetidos(RC.comun_e1.cargar_chunks((to,), e0_dir=e0), to) for to in orden}
    todas = [(to, c) for to in orden for c in por_to[to]]
    msg2c: dict[str, tuple[str, dict]] = {}
    partes_de: dict[str, tuple[list | None, dict]] = {}
    for to, c in todas:
        msg2c[sha(texto_mensaje(pf.build_request_kwargs(c, model=RC.MODEL_E1)))] = (to, c)
        if c["chars_propio"] > 5000:
            partes, info = correr_e0.particionar_por_corte(c)
            partes_de[c["id"]] = (partes, info)
            for p in partes or ():
                msg2c[sha(texto_mensaje(pf.build_request_kwargs(p, model=RC.MODEL_E1)))] = (to, p)
    techo, esc3 = cliente_e1.MAX_TOKENS_REINTENTO_CORTE_R2, cliente_e1.MAX_TOKENS_ESCALON_3_R2
    cap_med, cap_p90 = techo / RAZON_MEDIANA, techo / RAZON_P90
    cap3_med, cap3_p90 = esc3 / RAZON_MEDIANA, esc3 / RAZON_P90

    # ramas naturales con la hipótesis p90, y las forzadas si faltan
    grandes = [(to, c) for to, c in todas if c["chars_propio"] > cap_p90]
    nat_part = [c["id"] for _, c in grandes if partes_de[c["id"]][0]]
    nat_esc3 = [c["id"] for _, c in grandes if not partes_de[c["id"]][0]] + [
        p["id"] for _, c in grandes for p in (partes_de[c["id"]][0] or ()) if p["chars_propio"] > cap_p90]
    forzadas: dict[str, str] = {}
    if not nat_part:
        cand = sorted((c for _, c in todas if partes_de.get(c["id"], (None,))[0]), key=lambda c: -c["chars_propio"])
        forzadas[cand[0]["id"]] = "particion"
    if not nat_esc3:
        cand = sorted((c for _, c in todas if c["id"] in partes_de and not partes_de[c["id"]][0]),
                      key=lambda c: -c["chars_propio"])
        forzadas[cand[0]["id"]] = "tercer_escalon"
    # salida mal formada: la primera unidad elegible (no mini, menos de 3.000 caracteres propios, con su par
    # (unidad, título) único) de cada uno de los tres primeros TOs del orden que tienen una; el ratchet: la siguiente
    # elegible del primero de esos TOs que tenga otra
    clave_e3 = Counter((c["unidad"], c["titulo"]) for _, c in todas)

    def primeras(to: str, n: int) -> list[dict]:
        return [c for c in por_to[to] if c["tipo"] != "mini_chunk" and c["chars_propio"] < 3000
                and clave_e3[(c["unidad"], c["titulo"])] == 1][:n]
    con_elegibles = [to for to in orden if primeras(to, 1)][:3]
    assert len(con_elegibles) == 3, con_elegibles
    forma = {primeras(con_elegibles[0], 1)[0]["id"]: "rforma1_bien", primeras(con_elegibles[1], 1)[0]["id"]: "reparada",
             primeras(con_elegibles[2], 1)[0]["id"]: "error"}
    rat = next(primeras(to, 2)[1] for to in con_elegibles if len(primeras(to, 2)) == 2)
    assert rat["id"] not in forma
    lineas = [x.strip() for x in rat["texto"].split("\n") if len(x.strip()) >= 40]
    cita_rat = lineas[len(lineas) // 2][:60]
    marca_rat = f"Unidad bajo verificación: {rat['unidad']} — {rat['titulo']}\n"

    ns1 = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace)
    ns_f = {cliente_e1.SUFIJO_REINTENTO_FORMA: cliente_e1.namespace_e1(
                prefijo_hash=pf.prefijo_hash_para_namespace, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA),
            cliente_e1.SUFIJO_REINTENTO_FORMA_2: cliente_e1.namespace_e1(
                prefijo_hash=pf.prefijo_hash_para_namespace, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA_2)}
    ns3 = cliente_e3.namespace_e3()
    pedidos: list[dict] = []
    e3_vistas = Counter()

    def corta(c: dict, max_tokens: int) -> bool:
        if forzadas.get(c["id"]) and max_tokens < esc3:
            return True
        return c["chars_propio"] * RAZON_P90 > max_tokens

    class StubE1T1(RC.StubE1Corpus):
        def _responder(self, kwargs: dict, sufijo: str | None):
            msg = texto_mensaje(kwargs)
            ratchet = ratchet_e3.MARCA_REINTENTO in msg
            ent = None if ratchet else msg2c.get(sha(msg))
            ns = ns_f[sufijo] if sufijo else ns1
            reg = {"etapa": "e1_ratchet" if ratchet else ("e1_reintento_forma" if sufijo else "e1"),
                   "chunk_id": ent[1]["id"] if ent else None, "model": kwargs.get("model"),
                   "max_tokens": kwargs.get("max_tokens"), "temperature": kwargs.get("temperature", "sin fijar"),
                   "namespace": ns, "sufijo": sufijo, "clave": lc.compute_key(ns, lc.canonical_request(kwargs))}
            base = super().create(**kwargs)
            if a.stub_con_texto_ordenado:
                archivo = next(x.split(":", 1)[1].strip() for x in msg.splitlines() if x.startswith("Documento fuente:"))
                punto = base.content[0].input["entities"][0]["punto"]
                base.content[0].input["entities"].append({"local_id": "e2", "type": "TextoOrdenado", "label": archivo,
                                                          "punto": punto, "properties": {"archivo": archivo}})
            simulado = "ok"
            if ent is not None:
                c = ent[1]
                esc = forma.get(c["id"])
                if esc and sufijo is None:
                    simulado = "sin_relations"
                elif esc and sufijo == cliente_e1.SUFIJO_REINTENTO_FORMA and esc != "rforma1_bien":
                    simulado = "sin_relations"
                elif esc and sufijo == cliente_e1.SUFIJO_REINTENTO_FORMA_2:
                    simulado = "sin_relations" if esc == "reparada" else "entities_no_lista"
                elif not esc and corta(c, kwargs["max_tokens"]):
                    simulado = "corte"
            reg["simulado"] = simulado
            pedidos.append(reg)
            if simulado == "ok":
                return base
            ti = dict(base.content[0].input)
            if simulado == "corte":
                r = RC._StubResp({}, base.content[0].name)
                r.stop_reason = "max_tokens"
                return r
            ti.pop("relations", None)
            if simulado == "entities_no_lista":
                ti["entities"] = "no es una lista"
            return RC._StubResp(ti, base.content[0].name)

        def create(self, doc=None, **kwargs):
            try:
                return self._responder(kwargs, None)
            except Exception as e:             # noqa: BLE001
                raise ErrorDelStub(f"stub de E1: {type(e).__name__}: {e}") from e

        def crear_reintento_forma(self, *, doc=None, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA, **kwargs):
            try:
                return self._responder(kwargs, sufijo)
            except Exception as e:             # noqa: BLE001
                raise ErrorDelStub(f"stub de E1: {type(e).__name__}: {e}") from e

    class StubE3T1(RC.StubE3Corpus):
        def create(self, doc=None, **kwargs):
            try:
                return self._responder(kwargs)
            except Exception as e:             # noqa: BLE001
                raise ErrorDelStub(f"stub de E3: {type(e).__name__}: {e}") from e

        def _responder(self, kwargs: dict):
            msg = texto_mensaje(kwargs)
            es_rat = marca_rat in msg
            reg = {"etapa": "e3", "chunk_id": rat["id"] if es_rat else None, "model": kwargs.get("model"),
                   "max_tokens": kwargs.get("max_tokens"), "temperature": kwargs.get("temperature", "sin fijar"),
                   "namespace": ns3, "sufijo": None, "clave": lc.compute_key(ns3, lc.canonical_request(kwargs))}
            base = super().create(**kwargs)
            if es_rat:
                e3_vistas[rat["id"]] += 1
                if e3_vistas[rat["id"]] == 1:
                    reg["simulado"] = "faltante_alta"
                    pedidos.append(reg)
                    return RC._StubResp({"veredicto": "faltantes_detectados", "faltantes": [
                        {"tipo": prompt_e3.TIPOS_FALTANTE[0], "cita_textual_del_fuente": cita_rat,
                         "ubicacion": rat["unidad"], "severidad": "alta",
                         "nota": "faltante sintético de la corrida en seco"}]}, prompt_e3.NOMBRE_TOOL)
            reg["simulado"] = "completo_ok"
            pedidos.append(reg)
            return base

    RC.StubE1Corpus = StubE1T1
    RC.StubE3Corpus = StubE3T1

    salida_runner = sal / "runner"
    sys.argv = ["runner_corpus.py", "--manifiesto", MANIFIESTO_REL, "--salida", str(salida_runner), "--stub"]
    if a.tos:
        sys.argv += ["--tos", a.tos]
    try:
        rc = RC.main()
        excepcion = None
    except ErrorDelStub as e:
        rc, excepcion = None, f"ErrorDelStub: {e}"
    except SystemExit as e:                    # noqa: TRY302 — se registra como la corrida real la dejaría salir
        rc, excepcion = e.code, f"SystemExit({e.code})"
    except Exception as e:                     # noqa: BLE001
        rc, excepcion = None, f"{type(e).__name__}: {e}"
    sys.stdout.flush()

    with open(sal / "pedidos_t1.jsonl", "w", encoding="utf-8") as f:
        for p in pedidos:
            f.write(json.dumps(p, ensure_ascii=False, sort_keys=True) + "\n")

    # ---------------------------------------------------- pedidos por etapa y claves en las bases de la copia
    def resumen_etapa(filas: list[dict]) -> dict:
        return {"pedidos": len(filas), "claves_distintas": len({p["clave"] for p in filas}),
                "modelos": dict(Counter(p["model"] for p in filas)),
                "max_tokens": dict(sorted(Counter(p["max_tokens"] for p in filas).items())),
                "temperaturas": dict(Counter(str(p["temperature"]) for p in filas)),
                "namespaces": dict(Counter(p["namespace"] for p in filas)),
                "simulado": dict(Counter(p["simulado"] for p in filas))}
    etapas = {e: resumen_etapa([p for p in pedidos if p["etapa"] == e])
              for e in ("e1", "e1_reintento_forma", "e1_ratchet", "e3")}
    primeros = [p for p in pedidos if p["etapa"] == "e1" and p["max_tokens"] == RC.PERFIL.build_request_kwargs(
        todas[0][1], model=RC.MODEL_E1)["max_tokens"]]

    def en_db(db: Path, claves: set[str]) -> dict:
        if not db.exists():
            return {"existe": False}
        con = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
        try:
            n = sum(1 for k in claves if con.execute("SELECT 1 FROM cache WHERE key = ?", (k,)).fetchone())
        finally:
            con.close()
        return {"existe": True, "claves_controladas": len(claves), "presentes": n}
    claves_db = {
        "e1_extraccion_db": en_db(cliente_e1.DB_PATH, {p["clave"] for p in pedidos if p["etapa"] in ("e1", "e1_reintento_forma")}),
        "e1_reintentos_db": en_db(RC.DB_REINTENTOS_E1, {p["clave"] for p in pedidos if p["etapa"] == "e1_ratchet"}),
        "e3_verificacion_db": en_db(cliente_e3.DB_PATH, {p["clave"] for p in pedidos if p["etapa"] == "e3"})}

    # ---------------------------------------------------- las ramas, en los registros del runner
    def last_wins(p: Path) -> dict:
        out = {}
        if p.exists():
            for x in p.read_text(encoding="utf-8").splitlines():
                if x.strip():
                    r = json.loads(x)
                    out[r["chunk_id"]] = r
        return out
    regs = {to: last_wins(salida_runner / to / "extracciones_e1.jsonl") for to in orden}
    todos_regs = {cid: r for d in regs.values() for cid, r in d.items()}
    particiones = {}
    for to in orden:
        particiones.update(RC.partes_por_corte(salida_runner / to))
    ramas = {
        "corte_y_reintento_por_corte_resuelto": sorted(cid for cid, r in todos_regs.items()
                                                      if "reintento_corte" in r and r.get("error") is None
                                                      and not r.get("escalon_3")),
        "particion_por_corte": {k: [p["id"] for p in v["partes"]] for k, v in sorted(particiones.items())},
        "tercer_escalon": sorted(cid for cid, r in todos_regs.items() if r.get("escalon_3")),
        "tercer_escalon_corta_tambien": sorted(cid for cid, r in todos_regs.items()
                                              if r.get("error") == RC.ERROR_TRAS_ESCALON_3),
        "salida_mal_formada_rforma1_bien": sorted(cid for cid, r in todos_regs.items() if "reintento_forma" in r
                                                 and "reintento_2" not in r["reintento_forma"] and r.get("error") is None),
        "salida_mal_formada_reparada": sorted(cid for cid, r in todos_regs.items() if "reparacion_forma" in r),
        "salida_mal_formada_error": sorted(cid for cid, r in todos_regs.items()
                                          if r.get("error") == RC.ERROR_FORMA_TRAS_REINTENTO),
        "reintento_ratchet_e3": {"unidad": rat["id"], "verificaciones_e3": e3_vistas[rat["id"]],
                                 "reextracciones_e1": sum(1 for p in pedidos if p["etapa"] == "e1_ratchet")},
    }
    recorridas = {
        "corte": bool(ramas["corte_y_reintento_por_corte_resuelto"]),
        "reintento": bool(ramas["corte_y_reintento_por_corte_resuelto"]) and ramas["reintento_ratchet_e3"]["verificaciones_e3"] == 2
                     and ramas["reintento_ratchet_e3"]["reextracciones_e1"] >= 1,
        "particion": bool(ramas["particion_por_corte"]),
        "tercer_escalon": bool(ramas["tercer_escalon"]),
        "salida_mal_formada": bool(ramas["salida_mal_formada_rforma1_bien"] and ramas["salida_mal_formada_reparada"]
                                   and ramas["salida_mal_formada_error"]),
    }
    esperadas_forma = {"rforma1_bien": "salida_mal_formada_rforma1_bien", "reparada": "salida_mal_formada_reparada",
                       "error": "salida_mal_formada_error"}
    forma_ok = all(cid in ramas[esperadas_forma[e]] for cid, e in forma.items())

    # ---------------------------------------------------- 2.6: la clase A y el censo de unidades grandes
    censo = []
    for to, c in grandes:
        partes, info = partes_de[c["id"]]
        d = {"to": to, "chunk_id": c["id"], "tipo": c["tipo"], "chars_propio": c["chars_propio"],
             "salida_proyectada_mediana": round(c["chars_propio"] * RAZON_MEDIANA),
             "salida_proyectada_p90": round(c["chars_propio"] * RAZON_P90),
             "pasa_capacidad_mediana": c["chars_propio"] > cap_med, "se_parte": partes is not None,
             "particion": {k: v for k, v in info.items() if k != "id"},
             "tercer_escalon_si_el_reintento_corta": RC.corresponde_escalon_3(c),
             "sobre_umbral_healthcheck": c["chars_propio"] > UMBRAL_HC}
        if partes:
            d["partes"] = [{"id": p["id"], "chars_propio": p["chars_propio"],
                            "pasa_capacidad_p90": p["chars_propio"] > cap_p90,
                            "tercer_escalon_si_corta": RC.corresponde_escalon_3(p),
                            "pasa_tercer_escalon_p90": p["chars_propio"] > cap3_p90} for p in partes]
            if any(p["pasa_tercer_escalon_p90"] for p in d["partes"]):
                d["mecanismo"] = ("8.192 → 16.384 → partición por corte; una parte pasa también el tercer escalón: "
                                  "queda con max_tokens_hit_tras_escalon_3, declarada en errores_definitivos")
            else:
                d["mecanismo"] = ("8.192 → 16.384 → partición por corte; cada parte 8.192 → 16.384 → tercer escalón "
                                  "40.960 (una parte no se vuelve a partir)")
        elif c["chars_propio"] > cap3_p90:
            d["mecanismo"] = ("8.192 → 16.384 → tercer escalón 40.960 (no se parte: " + info.get("motivo", "") + "); "
                              "pasa también el tercer escalón con la p90: queda con max_tokens_hit_tras_escalon_3, "
                              "declarada en errores_definitivos")
        else:
            d["mecanismo"] = "8.192 → 16.384 → tercer escalón 40.960 (no se parte: " + info.get("motivo", "") + ")"
        r = todos_regs.get(c["id"]) or {}
        d["en_la_corrida_en_seco"] = {
            "error": r.get("error"), "reintento_corte": "reintento_corte" in r, "escalon_3": bool(r.get("escalon_3")),
            "partes": [x["id"] for x in particiones.get(c["id"], {}).get("partes", [])],
            "partes_con_escalon_3": sorted(p for p in (x["id"] for x in particiones.get(c["id"], {}).get("partes", []))
                                           if (todos_regs.get(p) or {}).get("escalon_3")),
            "partes_con_error": {p: todos_regs[p].get("error") for p in
                                 (x["id"] for x in particiones.get(c["id"], {}).get("partes", []))
                                 if todos_regs.get(p, {}).get("error")}}
        d["declarada"] = bool(d.get("mecanismo"))
        censo.append(d)
    clase_a = [d for d in censo if not d["se_parte"]]
    resultado_censo = {
        "capacidad": {"reintento_por_corte_max_tokens": techo, "tercer_escalon_max_tokens": esc3,
                      "razon_mediana": RAZON_MEDIANA, "razon_p90": RAZON_P90,
                      "reintento_mediana_chars": round(cap_med, 1), "reintento_p90_chars": round(cap_p90, 1),
                      "tercer_escalon_mediana_chars": round(cap3_med, 1), "tercer_escalon_p90_chars": round(cap3_p90, 1),
                      "fuente": "reext_t0/freno_t2.md:12; correr_e0.CAPACIDAD_ESCALON_3_R6 = "
                                f"{correr_e0.CAPACIDAD_ESCALON_3_R6}, OBJETIVO_PARTES_RENGLONES_R6 = "
                                f"{correr_e0.OBJETIVO_PARTES_RENGLONES_R6}"},
        "unidades_de_la_tanda": len(todas),
        "censo_sobre_la_capacidad_p90": len(censo),
        "censo_sobre_la_capacidad_mediana": sum(d["pasa_capacidad_mediana"] for d in censo),
        "clase_a_sin_particion_posible": [d["chunk_id"] for d in clase_a],
        "clase_a_sobre_la_capacidad_mediana": [d["chunk_id"] for d in clase_a if d["pasa_capacidad_mediana"]],
        "sobre_el_tercer_escalon_p90": [d["chunk_id"] for d in censo if not d["se_parte"] and d["chars_propio"] > cap3_p90]
                                       + [p["id"] for d in censo for p in d.get("partes", []) if p["pasa_tercer_escalon_p90"]],
        "sin_declarar": [d["chunk_id"] for d in censo if not d["declarada"]],
        "entre_8192_y_16384_con_la_p90": sum(1 for _, c in todas if 8192 / RAZON_P90 < c["chars_propio"] <= cap_p90),
        "forzadas_en_la_corrida_en_seco": forzadas,
        "censo": censo}
    (sal / "censo_unidades_grandes_t1.json").write_text(json.dumps(resultado_censo, ensure_ascii=False, indent=1) + "\n",
                                                        encoding="utf-8")

    # ---------------------------------------------------- 2.7: el estimado por TO
    alc = json.loads((COPIA / MEDICION_A3_REL).read_text(encoding="utf-8"))["tanda_final"]["por_documento"]
    est_man = man.limites["estimado_usd"]
    filas, tot, tot_man = {}, Decimal(0), Decimal(0)
    for to in orden:
        n = len(por_to[to])
        e1 = n * TARIFA_E1 + Decimal(str(alc[to]["usd_agregados"])) if to in alc else n * TARIFA_E1
        e3 = n * TARIFA_E3
        m1, m3 = Decimal(str(est_man[to]["e1"])), Decimal(str(est_man[to]["e3"]))
        resumen = json.loads((salida_runner / to / "resumen_e1.json").read_text(encoding="utf-8")) \
            if (salida_runner / to / "resumen_e1.json").exists() else {}
        cortes = [p for p in pedidos if p["simulado"] == "corte" and p["chunk_id"]
                  and (p["chunk_id"] in {c["id"] for c in por_to[to]} or p["chunk_id"].split("::parte")[0]
                       in {c["id"] for c in por_to[to]})]
        filas[to] = {"unidades_e0": n, "unidades_en_la_corrida_en_seco": resumen.get("n_unidades"),
                     "gasto_stub_usd": resumen.get("gasto_fase_usd"),
                     "chars_completo": sum(c["chars_completo"] for c in por_to[to]),
                     "e1_usd": str(e1), "e3_usd": str(e3), "total_usd": str(e1 + e3),
                     "manifiesto_e1_usd": str(m1), "manifiesto_e3_usd": str(m3), "manifiesto_total_usd": str(m1 + m3),
                     "igual_al_manifiesto": e1 == m1 and e3 == m3,
                     "manifiesto_sobre_tarifa": str(((m1 + m3) / (e1 + e3)).quantize(Decimal("0.0001"))),
                     "pedidos_que_cortan_con_la_p90": len(cortes),
                     "salida_de_los_cortes_usd_cota": round(sum(p["max_tokens"] for p in cortes) * P_SALIDA_E1 / 1e6, 4)}
        tot += e1 + e3
        tot_man += m1 + m3
    estado = json.loads((salida_runner / "estado_corpus.json").read_text(encoding="utf-8"))
    cortes_usd = sum(f["salida_de_los_cortes_usd_cota"] for f in filas.values())
    estimado = {"tarifa_por_unidad_usd": str(TARIFA_E1 + TARIFA_E3), "por_to": filas,
                "tos": len(filas), "unidades": sum(f["unidades_e0"] for f in filas.values()),
                "iguales_al_manifiesto": sum(f["igual_al_manifiesto"] for f in filas.values()),
                "total_usd": str(tot), "total_manifiesto_usd": str(tot_man),
                "total_igual_al_manifiesto": tot == tot_man,
                "total_a_4_decimales": str(tot.quantize(Decimal("0.0001"))),
                "tope_usd": man.limites["tope_global_usd"],
                "margen_usd": str(Decimal(str(man.limites["tope_global_usd"])) - tot),
                "tope_sobre_estimado": str((Decimal(str(man.limites["tope_global_usd"])) / tot).quantize(Decimal("0.0001"))),
                "estimado_total_del_runner_usd": estado.get("estimado_total_usd"),
                "gasto_global_stub_usd": sum(f["gasto_usd"] for f in estado["fases_cerradas"].values()),
                "salida_de_los_cortes_p90_usd_cota": round(cortes_usd, 4),
                "nota_cortes": ("cota de la salida de los pedidos que cortan con la hipótesis p90 (max_tokens del pedido "
                                "cortado a USD 5 por millón; sin la entrada ni el tercer escalón que responde): lo que "
                                "la tarifa por unidad no incluye si la salida real fuera la del p90. El freno por "
                                "proyección del runner lo controla con el gasto real (runner_corpus.py:400-451).")}
    (sal / "estimado_por_to_t1.json").write_text(json.dumps(estimado, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    res = {
        "comando": "t1_corrida_en_seco_tanda_final.py --raiz <copia> --salida DIR" + (f" --tos {a.tos}" if a.tos else ""),
        "argv_del_runner": [x.replace(str(salida_runner), "<salida>/runner") for x in sys.argv[1:]],
        "rc_del_runner": rc, "excepcion": excepcion,
        "llamadas_a_la_api": cuenta["socket"] + cuenta["anthropic"] + cuenta["cliente_real"],
        "guardas": {"conexiones_de_red_intentadas": cuenta["socket"], "clientes_anthropic_construidos": cuenta["anthropic"],
                    "clientes_reales_construidos": cuenta["cliente_real"]},
        "manifiesto": {"nombre": man.nombre, "tos": len(man.ids), "perfil": pf.nombre,
                       "tope_global_usd": RC.TOPE_GLOBAL_USD, "estimado_total_runner_usd": RC.ESTIMADO_TOTAL_USD},
        "unidades_e0": len(todas),
        "pedidos_por_etapa": etapas,
        "primer_intento_e1": {"pedidos": len(primeros), "claves_distintas": len({p["clave"] for p in primeros}),
                              "max_tokens": sorted({p["max_tokens"] for p in primeros})},
        "claves_ya_en_las_bases_de_la_copia": claves_db,
        "ramas": ramas, "ramas_recorridas": recorridas, "salida_mal_formada_por_unidad": forma,
        "salida_mal_formada_como_se_esperaba": forma_ok, "ramas_forzadas": forzadas,
        "ratchet": {"unidad": rat["id"]},
        "clase_a": resultado_censo["clase_a_sin_particion_posible"],
        "censo_sobre_la_capacidad_p90": resultado_censo["censo_sobre_la_capacidad_p90"],
        "sin_declarar": resultado_censo["sin_declarar"],
        "estimado_total_usd": estimado["total_usd"], "tope_usd": estimado["tope_usd"],
        "veredicto": "OK" if (rc == 0 and excepcion is None and cuenta["socket"] + cuenta["anthropic"]
                              + cuenta["cliente_real"] == 0 and all(recorridas.values()) and forma_ok
                              and not resultado_censo["sin_declarar"]) else "FALLA"}
    if a.tos:
        res["tos_pedidos"] = orden
    res["stub_con_texto_ordenado"] = a.stub_con_texto_ordenado
    (sal / "corrida_en_seco_t1.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("rc_del_runner", "excepcion", "llamadas_a_la_api", "ramas_recorridas",
                                          "salida_mal_formada_como_se_esperaba", "ramas_forzadas", "clase_a",
                                          "censo_sobre_la_capacidad_p90", "sin_declarar", "estimado_total_usd",
                                          "veredicto")}, ensure_ascii=False), file=sys.stderr)
    return 0 if res["veredicto"] == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
