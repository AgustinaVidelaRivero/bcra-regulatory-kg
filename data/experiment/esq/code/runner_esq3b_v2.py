"""
runner_esq3b_v2.py — FASE (e) de U-ESQ-3b-v2: re-extracción de las 27
unidades seleccionadas con el PREFIJO V2.

Los brazos BASE **no se corren** (pre-registro v2 §2): para las 15 del
objetivo es la extracción de la VUELTA 1 (`esq3b/extracciones/
pareado_esq3b.jsonl`, prefijo `f0a421fb9466`, db `esq_3b.db`) y para las 12
de regresión fresca es la extracción de ESQ-2 (`cobertura/`, sellos
`a7788c1`, db `esq_cobertura.db`) — ambas a costo USD 0. Acá solo corre el
brazo NUEVO, sobre las unidades que `seleccion_esq3b_v2.py` persistió antes
de gastar.

Frenos (todos duros, ninguno se puede saltear con un flag):
  - guardas de modo v2 ANTES de la primera llamada (si algo no cierra, nada
    se gasta);
  - gate de pareo read-only DOBLE, USD 0: cada unidad del objetivo tiene su
    fila del brazo base en la db de la VUELTA 1 bajo el namespace v1, y cada
    unidad de regresión fresca la tiene en la db de ESQ-2 bajo el namespace
    de ESQ-2 (prueba de que el brazo base existe y de que el mensaje de
    usuario es byte-idéntico entre brazos);
  - cliente: proyección pre-llamada contra el tope USD 0,40 (TopeExcedido);
  - runner: margen por unidad antes de cada llamada y proyección lineal cada
    10 unidades;
  - corrida real solo con `--autorizado-tope 0.40` (eco de la autorización
    del chat, posterior al freno 1) — sin ese eco, nada se llama.

Persistencia: `esq3b_v2/extracciones/pareado_esq3b_v2.jsonl`, append-only,
reanudación idempotente por last-wins. SECUENCIAL (D4): un cliente, un loop,
orden por brazo y `chunk_id`.

Cierre: gasto real desde la db propia (una fila = una response real pagada),
modelo RESUELTO por llamada leído del crudo, cruce db==jsonl, verificación de
que producción, `cobertura/` y los artefactos de la vuelta 1 siguen intactos
por sha256.

Uso:
  selftest offline:  via selftest_esq3b_v2.py (--stub, salida propia)
  corrida real (SOLO con autorización explícita de la autora en el chat,
  posterior a la aprobación del freno 1):
    .venv/bin/python3 -B data/experiment/esq/code/runner_esq3b_v2.py \
        --autorizado-tope 0.40
  --solo-cierre: recomputa el resumen desde lo persistido, sin API.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_esq3b_v2 as cc      # noqa: E402
import prompt_esq3b_v2 as pr     # noqa: E402
import chequeo_esq3b_v2 as chk   # noqa: E402
import comun_e1                  # noqa: E402
import prompt_e1                 # noqa: E402
import prompt_esq3b as pr1       # noqa: E402
import llm_cache as lc           # noqa: E402

SALIDA_JSONL = cc.EXTRACCIONES_DIR / "pareado_esq3b_v2.jsonl"
RESUMEN_JSON = cc.ESQ3B_V2_DIR / "resumen_esq3b_v2.json"
SELECCION_JSON = cc.ORDEN_DIR / "seleccion_brazos_esq3b_v2.json"

MARGEN_UNIDAD_USD = 0.06   # > proyección de una llamada fría del cliente


class Freno(RuntimeError):
    pass


# --------------------------------------------------------------------------- #
# Guardas previas a cualquier gasto                                           #
# --------------------------------------------------------------------------- #
def verificar_modo_v2(chunk: dict) -> dict:
    """Asserts de que el request lleva el prefijo V2 de esta vuelta y de que
    la caché es la propia. Corre antes de la primera llamada."""
    ns = cc.namespace_v2()
    kwargs = pr.build_request_kwargs_v2(chunk, model=cc.MODEL_E1)
    ent_enum = kwargs["tools"][0]["input_schema"]["properties"]["entities"][
        "items"]["properties"]["type"]["enum"]
    rel_enum = kwargs["tools"][0]["input_schema"]["properties"]["relations"][
        "items"]["properties"]["predicate"]["enum"]
    props_e = kwargs["tools"][0]["input_schema"]["properties"]["entities"][
        "items"]["properties"]
    props_r = kwargs["tools"][0]["input_schema"]["properties"]["relations"][
        "items"]["properties"]
    ok = {
        "candado_prefijo_produccion": (
            prompt_e1.prefijo_hash(False) == cc.PREFIJO_HASH_PRODUCCION_ESPERADO),
        "candado_prefijo_v1": (
            pr1.PREFIJO_HASH_RETOCADO == cc.PREFIJO_HASH_V1_ESPERADO),
        "system_es_prefijo_v2": (
            kwargs["system"][0]["text"] == pr.PREFIJO_SISTEMA_V2),
        "system_distinto_de_v1_y_produccion": (
            kwargs["system"][0]["text"] != pr1.PREFIJO_SISTEMA_RETOCADO
            and kwargs["system"][0]["text"] != prompt_e1.PREFIJO_SISTEMA),
        "breakpoint_cache_declarado": (
            kwargs["system"][0].get("cache_control") == {"type": "ephemeral"}),
        "enum_tipos_9": list(ent_enum) == list(pr.ENTITY_TYPES_V2),
        "enum_predicados_13": list(rel_enum) == list(pr.PREDICATES_V2),
        "sin_exceptua_operacion": (
            "exceptua_operacion" not in rel_enum
            and "exceptua_operacion" not in kwargs["system"][0]["text"]),
        "sin_tipo_propuesto": "tipo_propuesto" not in props_e,
        "sin_predicado_propuesto": "predicado_propuesto" not in props_r,
        "mensaje_igual_a_produccion": (
            kwargs["messages"]
            == prompt_e1.build_request_kwargs(chunk, model=cc.MODEL_E1)["messages"]),
        "namespace_distinto_produccion": ns != cc.namespace_produccion(),
        "namespace_distinto_esq2": ns != cc.namespace_cobertura_esq2(),
        "namespace_distinto_v1": ns != cc.namespace_v1(),
        "namespace_propio": ns.startswith(cc.DOMAIN),
        "db_propia": str(cc.DB_V2) not in {str(p) for p in cc.DBS_AJENAS},
    }
    fallas = [k for k, v in ok.items() if v is not True]
    if fallas:
        raise Freno(f"guarda de modo v2 falló: {fallas} — no se gasta")
    return {"namespace": ns, "prefijo_v2": pr.PREFIJO_HASH_V2,
            "prefijo_v1": pr1.PREFIJO_HASH_RETOCADO,
            "prefijo_produccion": prompt_e1.prefijo_hash(False),
            "model_pedido": kwargs["model"], **ok}


def verificar_sin_rol(chunk: dict, mensaje: str) -> None:
    """Cuarentena D5 heredada de ESQ-2/vuelta 1: el archivo no resuelve rol y
    el mensaje no trae bloque de alcance. Es además condición del pareo — los
    brazos base corrieron así."""
    from schema import ROL_POR_TO
    if ROL_POR_TO.get(chunk["archivo"]) is not None:
        raise Freno(f"{chunk['id']}: archivo {chunk['archivo']} resuelve rol "
                    f"en ROL_POR_TO — cuarentena D5 violada")
    if "Alcance de este TO" in mensaje:
        raise Freno(f"{chunk['id']}: el mensaje trae bloque de alcance — "
                    f"cuarentena D5 violada")


def gate_pareo_readonly(seleccion: dict, chunks: dict) -> dict:
    """Gate de pareo DOBLE a USD 0 (pre-registro v2 §2): el brazo base de cada
    unidad existe en su db, bajo su namespace, con su request (la key se
    recomputa desde el chunk, no se busca a ciegas). Lectura estricta mode=ro:
      - objetivo (15): db de la VUELTA 1 (esq_3b.db), namespace v1, request
        con el prefijo v1 (build_request_kwargs_retocado);
      - regresión fresca (12): db de ESQ-2 (esq_cobertura.db), namespace de
        ESQ-2, request de PRODUCCIÓN (build_request_kwargs)."""
    faltan: list[str] = []

    ns1 = cc.namespace_v1()
    conn = cc.conectar_db_readonly(cc.DB_V1)
    for u in seleccion["objetivo"]["unidades"]:
        c = chunks[u["chunk_id"]]
        kwargs_v1 = pr1.build_request_kwargs_retocado(c, model=cc.MODEL_E1)
        key = lc.compute_key(ns1, lc.canonical_request(kwargs_v1))
        if conn.execute("SELECT 1 FROM cache WHERE key = ?", (key,)).fetchone() is None:
            faltan.append(f"objetivo:{c['id']}")
    conn.close()

    ns2 = cc.namespace_cobertura_esq2()
    conn = cc.conectar_db_readonly(cc.CACHE_DIR / "esq_cobertura.db")
    for u in seleccion["regresion_fresca"]["unidades"]:
        c = chunks[u["chunk_id"]]
        kwargs_prod = prompt_e1.build_request_kwargs(c, model=cc.MODEL_E1)
        key = lc.compute_key(ns2, lc.canonical_request(kwargs_prod))
        if conn.execute("SELECT 1 FROM cache WHERE key = ?", (key,)).fetchone() is None:
            faltan.append(f"regresion_fresca:{c['id']}")
    conn.close()

    if faltan:
        raise Freno(f"gate de pareo doble: {len(faltan)} unidades sin fila del "
                    f"brazo base ({faltan[:5]}) — no se gasta")
    n = (len(seleccion["objetivo"]["unidades"])
         + len(seleccion["regresion_fresca"]["unidades"]))
    return {"unidades_pareadas": n, "namespace_v1": ns1,
            "namespace_esq2": ns2, "faltantes": []}


# --------------------------------------------------------------------------- #
# Stub offline (selftest)                                                     #
# --------------------------------------------------------------------------- #
class StubClienteV2:
    """Cliente offline: extracción mínima válida bajo el esquema V2 (emite un
    tipo nuevo, un predicado nuevo y una Obligacion con
    requisito_de_estructura, para que el selftest ejercite el chequeo de
    firmas y la q4 de las fichas). Interfaz .create(doc=..., **kw); usage en
    cero."""

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
            b.name = pr.NOMBRE_TOOL
            b.input = tool_input
            self.content = [b]
            self.stop_reason = "tool_use"
            self.usage = StubClienteV2._U()

    def __init__(self):
        self.gasto_usd = 0.0
        self.llamadas = 0
        self.llamadas_hit = 0
        self.puntos_llamados: list[str] = []

    def create(self, doc=None, **kwargs):
        self.llamadas += 1
        msg = kwargs["messages"][0]["content"]
        punto = None
        for linea in msg.splitlines():
            if linea.startswith(("Punto del chunk:", "Unidad de origen:")):
                punto = linea.split(":", 1)[1].strip().split(" ", 1)[0]
                break
        self.puntos_llamados.append(punto)
        return StubClienteV2._R({
            "entities": [
                {"local_id": "to", "type": "TextoOrdenado", "label": "TO stub",
                 "punto": punto, "properties": {}},
                {"local_id": "e1", "type": "Potestad",
                 "label": f"potestad stub {punto}", "punto": punto,
                 "properties": {"descripcion": "stub"}},
                {"local_id": "e2", "type": "Condicion",
                 "label": f"condicion stub {punto}", "punto": punto,
                 "properties": {"descripcion": "stub"}},
                {"local_id": "e3", "type": "Obligacion",
                 "label": f"obligacion stub {punto}", "punto": punto,
                 "properties": {"descripcion": "stub",
                                "tipo": "requisito_de_estructura"}},
            ],
            "relations": [
                {"source": "e1", "target": "to", "predicate": "establecida_en",
                 "punto": punto},
                {"source": "e2", "target": "e3", "predicate": "condicion_de",
                 "punto": punto},
            ],
            "omisiones_no_prosa": [],
        })

    def resumen(self):
        return {"llamadas": self.llamadas, "hits_cache_local": self.llamadas_hit,
                "gasto_usd_real": 0.0, "stub": True}

    def close(self):
        pass


# --------------------------------------------------------------------------- #
# Corrida                                                                     #
# --------------------------------------------------------------------------- #
def append_jsonl(path: Path, reg: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(reg, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def llamar_con_reintentos_api(fn, descripcion: str, max_intentos: int = 3):
    """Reintento ante errores transitorios de API. TopeExcedido NO se
    reintenta: es freno."""
    esperas = (20, 60, 180)
    ultimo = None
    for i in range(max_intentos):
        try:
            return fn(), None
        except cc.TopeExcedido:
            raise
        except Exception as e:  # noqa: BLE001 — transitorios de red/API
            ultimo = f"{type(e).__name__}: {e}"
            print(f"  error API en {descripcion} (intento {i+1}/{max_intentos}): "
                  f"{ultimo}", flush=True)
            if i < max_intentos - 1:
                time.sleep(esperas[i])
    return None, ultimo


def unidades_seleccionadas(seleccion: dict) -> list[tuple[str, str]]:
    """[(brazo, chunk_id)] en orden estable: objetivo primero (por chunk_id),
    regresión fresca después (en el orden persistido)."""
    out = [("objetivo", u["chunk_id"]) for u in seleccion["objetivo"]["unidades"]]
    out += [("regresion_fresca", u["chunk_id"])
            for u in seleccion["regresion_fresca"]["unidades"]]
    return out


def correr(cliente, salida_jsonl: Path, tope_usd: float, stub: bool,
           seleccion: dict, limite: int | None = None,
           abortar_tras: int | None = None) -> dict:
    chunks = {c["id"]: c for c in cc.cargar_chunks_esq2()}
    pares = unidades_seleccionadas(seleccion)
    if limite:
        pares = pares[:limite]

    guardas = verificar_modo_v2(chunks[pares[0][1]])
    print(f"[guardas] namespace={guardas['namespace']} | prefijo v2="
          f"{guardas['prefijo_v2']} | prefijo v1={guardas['prefijo_v1']} | "
          f"prefijo producción={guardas['prefijo_produccion']} (candados OK)",
          flush=True)
    pareo = gate_pareo_readonly(seleccion, chunks)
    print(f"[gate pareo doble USD 0] {pareo['unidades_pareadas']} unidades "
          f"con brazo base (objetivo→db v1, fresca→db ESQ-2)", flush=True)

    previos = cc.cargar_jsonl_last_wins(salida_jsonl)
    hechas_ok = {cid for cid, r in previos.items() if r.get("error") is None}
    pendientes = [(b, cid) for b, cid in pares if cid not in hechas_ok]
    print(f"[corrida] seleccionadas={len(pares)} ya_persistidas_ok={len(hechas_ok)} "
          f"pendientes={len(pendientes)}", flush=True)

    t0 = time.time()
    hechas = len(hechas_ok)
    hechas_este_proceso = 0
    errores_consecutivos = 0
    for brazo, cid in pendientes:
        c = chunks[cid]
        if cliente.gasto_usd + MARGEN_UNIDAD_USD > tope_usd:
            raise Freno(f"tope USD {tope_usd:.2f} antes de {cid}: gasto USD "
                        f"{cliente.gasto_usd:.4f} + margen {MARGEN_UNIDAD_USD}")
        kwargs = pr.build_request_kwargs_v2(c, model=cc.MODEL_E1)
        verificar_sin_rol(c, kwargs["messages"][0]["content"])
        resp, err = llamar_con_reintentos_api(
            lambda: cliente.create(doc=c["archivo"], **kwargs), cid)
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
        chequeo = chk.chequear(tool_input, c) if tool_input is not None else None
        append_jsonl(salida_jsonl, {
            "chunk_id": cid, "brazo": brazo, "unidad": c["unidad"],
            "tipo_unidad": c["tipo"], "titulo": c["titulo"],
            "stop_reason": stop, "error": err, "usage": usage,
            "tool_input_crudo": tool_input, "chequeo_esquema_v2": chequeo})
        hechas += 1
        hechas_este_proceso += 1
        errores_consecutivos = 0 if err is None else errores_consecutivos + 1
        if errores_consecutivos > 5:
            raise Freno(f"más de 5 errores de API consecutivos (último: {err}) "
                        f"— problema sistémico, se frena")
        if hechas_este_proceso % 10 == 0 or err:
            print(f"[{hechas}/{len(pares)}] {cid:<28s} gasto=USD "
                  f"{cliente.gasto_usd:.4f}" + (f" ERROR {err}" if err else ""),
                  flush=True)
            if not stub and hechas_este_proceso:
                proy = cliente.gasto_usd / hechas_este_proceso * len(pendientes)
                if proy > tope_usd:
                    raise Freno(f"proyección USD {proy:.4f} supera el tope "
                                f"{tope_usd:.2f}")
        if abortar_tras and hechas_este_proceso >= abortar_tras:
            print(f"ABORT SIMULADO tras {hechas_este_proceso} unidades", flush=True)
            sys.exit(9)

    return {"wall_s": round(time.time() - t0, 1), "total": len(pares),
            "hechas": hechas, "guardas": guardas, "gate_pareo": pareo}


# --------------------------------------------------------------------------- #
# Cierre                                                                      #
# --------------------------------------------------------------------------- #
def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def cierre(salida_jsonl: Path = SALIDA_JSONL, db_path: Path = cc.DB_V2,
           seleccion_path: Path = SELECCION_JSON) -> dict:
    seleccion = json.loads(seleccion_path.read_text(encoding="utf-8"))
    chunks = {c["id"]: c for c in cc.cargar_chunks_esq2()}
    ns = cc.namespace_v2()
    regs = cc.cargar_jsonl_last_wins(salida_jsonl)

    conn = cc.conectar_db_readonly(db_path)
    modelos: dict[str, int] = {}
    ok_cruce = dif_cruce = sin_fila = 0
    detalle: list[str] = []
    for brazo, cid in unidades_seleccionadas(seleccion):
        reg = regs.get(cid)
        if reg is None or reg.get("error") is not None:
            detalle.append(f"{cid}: sin registro válido en el jsonl")
            continue
        kwargs = pr.build_request_kwargs_v2(chunks[cid], model=cc.MODEL_E1)
        key = lc.compute_key(ns, lc.canonical_request(kwargs))
        row = conn.execute("SELECT * FROM cache WHERE key = ?", (key,)).fetchone()
        if row is None:
            sin_fila += 1
            detalle.append(f"{cid}: sin fila en la db propia")
            continue
        modelo = cc.modelo_de_raw(row["raw_json"])
        modelos[modelo] = modelos.get(modelo, 0) + 1
        if cc.tool_input_de_raw(row["raw_json"]) == reg.get("tool_input_crudo"):
            ok_cruce += 1
        else:
            dif_cruce += 1
            detalle.append(f"{cid}: tool_input db != jsonl")
    filas = conn.execute(
        "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), "
        "COALESCE(SUM(output_tokens),0), COALESCE(SUM(cache_write_tokens),0), "
        "COALESCE(SUM(cache_read_tokens),0) FROM cache WHERE namespace = ?",
        (ns,)).fetchone()
    conn.close()
    agg = {"n": filas[0], "input_tokens": filas[1], "output_tokens": filas[2],
           "cache_write_tokens": filas[3], "cache_read_tokens": filas[4]}
    gasto_real = cc.costo_usd_desde_usage(agg)

    # producción + cobertura intactas por sha (sellos de ESQ-2, lectura) y
    # artefactos de la vuelta 1 intactos (sha registrados en la selección v2).
    sellos_path = cc.COBERTURA_DIR / "sellos_produccion_sha256.json"
    intacta, sellos_dif = None, []
    if sellos_path.exists():
        sellos = json.loads(sellos_path.read_text(encoding="utf-8"))
        for rel, sha in sellos["archivos"].items():
            p = cc.REPO_DIR / rel
            actual = sha256_de(p) if p.exists() else "AUSENTE"
            if actual != sha:
                sellos_dif.append(f"{rel}: {sha[:12]} → {actual[:12]}")
        intacta = not sellos_dif
    sel_sha = json.loads(seleccion_path.read_text(encoding="utf-8"))["insumos_sha256"]
    v1_dif = []
    for rel, sha in sel_sha.items():
        p = cc.UNIDAD_DIR / rel
        actual = sha256_de(p) if p.exists() else "AUSENTE"
        if actual != sha:
            v1_dif.append(f"{rel}: {sha[:12]} → {actual[:12]}")

    anomalias = []
    extracciones_vacias = []
    for cid, r in regs.items():
        if r.get("error"):
            anomalias.append({"chunk_id": cid, "error": r["error"],
                              "stop_reason": r.get("stop_reason")})
        else:
            ents = (r.get("tool_input_crudo") or {}).get("entities") or []
            if sum(1 for e in ents if isinstance(e, dict)
                   and e.get("type") != "TextoOrdenado") == 0:
                extracciones_vacias.append(cid)

    por_brazo: dict[str, int] = {}
    for brazo, cid in unidades_seleccionadas(seleccion):
        if cid in regs and regs[cid].get("error") is None:
            por_brazo[brazo] = por_brazo.get(brazo, 0) + 1

    resumen = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "unidad": "U-ESQ-3b-v2",
        "namespace": ns,
        "prefijo_v2_hash": pr.PREFIJO_HASH_V2,
        "prefijo_v2_sha256_texto": pr.PREFIJO_SHA256_V2,
        "db": str(db_path.relative_to(cc.REPO_DIR)),
        "db_sha256": sha256_de(db_path) if db_path.exists() else None,
        "seleccionadas": len(unidades_seleccionadas(seleccion)),
        "persistidas_sin_error_por_brazo": por_brazo,
        "anomalias": anomalias,
        "n_extracciones_vacias_sin_identidad": len(extracciones_vacias),
        "modelo_resuelto_por_llamada": modelos,
        "cruce_db_jsonl": {"ok": ok_cruce, "dif": dif_cruce,
                           "sin_fila_db": sin_fila, "detalle": detalle[:50]},
        "filas_db_namespace_propio": agg,
        "gasto_real_usd_desde_db": round(gasto_real, 4),
        "formula_costo": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 "
                          "(USD/MTok), decisiones_caching_extraccion.md:32-42; "
                          "tarifas runner_corpus.py:76-78"),
        "tope_usd": cc.TOPE_USD,
        "produccion_y_cobertura_intactas_por_sha": intacta,
        "sellos_divergentes": sellos_dif,
        "insumos_v1_intactos_por_sha": not v1_dif,
        "insumos_v1_divergentes": v1_dif,
    }
    RESUMEN_JSON.parent.mkdir(parents=True, exist_ok=True)
    RESUMEN_JSON.write_text(json.dumps(resumen, ensure_ascii=False, indent=1),
                            encoding="utf-8")
    return resumen


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Re-extracción con prefijo v2 (U-ESQ-3b-v2)")
    ap.add_argument("--stub", action="store_true", help="cliente stub, offline")
    ap.add_argument("--salida", type=Path, default=SALIDA_JSONL)
    ap.add_argument("--db", type=Path, default=cc.DB_V2)
    ap.add_argument("--seleccion", type=Path, default=SELECCION_JSON)
    ap.add_argument("--autorizado-tope", type=float, default=None,
                    help="eco de la autorización; debe ser 0.40 para corrida real")
    ap.add_argument("--limite", type=int, default=None)
    ap.add_argument("--abortar-tras", type=int, default=None)
    ap.add_argument("--solo-cierre", action="store_true")
    args = ap.parse_args()

    if args.solo_cierre:
        r = cierre(args.salida, db_path=args.db, seleccion_path=args.seleccion)
        print(json.dumps({k: r[k] for k in (
            "seleccionadas", "persistidas_sin_error_por_brazo",
            "modelo_resuelto_por_llamada", "gasto_real_usd_desde_db",
            "produccion_y_cobertura_intactas_por_sha",
            "insumos_v1_intactos_por_sha")},
            ensure_ascii=False, indent=1))
        return 0

    seleccion = json.loads(args.seleccion.read_text(encoding="utf-8"))

    if args.stub:
        cliente = StubClienteV2()
    else:
        if args.autorizado_tope != cc.TOPE_USD:
            print(f"ABORTADO: la corrida real exige --autorizado-tope "
                  f"{cc.TOPE_USD:.2f} (eco de la autorización del chat, "
                  f"posterior al freno 1). Nada se llamó.")
            return 2
        from dotenv import load_dotenv
        load_dotenv(comun_e1.EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            print(f"ANTHROPIC_API_KEY ausente (esperada en "
                  f"{comun_e1.EVAL_DIR / '.env'})")
            return 1
        cliente = cc.ClienteEsq3bV2(**cc.P_E1, tope_usd=cc.TOPE_USD,
                                    run_label="esq3b_v2_pareado_e1",
                                    db_path=args.db)

    try:
        meta = correr(cliente, args.salida, cc.TOPE_USD, stub=args.stub,
                      seleccion=seleccion, limite=args.limite,
                      abortar_tras=args.abortar_tras)
    except Freno as e:
        print(f"\nFRENO: {e}", flush=True)
        return 3
    finally:
        res = cliente.resumen()
        cliente.close()

    print(f"\ncorrida: {meta['hechas']}/{meta['total']} unidades | "
          f"wall={meta['wall_s']}s | gasto cliente=USD "
          f"{res.get('gasto_usd_real', 0):.4f}", flush=True)

    if not args.stub and not args.limite and meta["hechas"] >= meta["total"]:
        r = cierre(args.salida, db_path=args.db, seleccion_path=args.seleccion)
        print(f"cierre: gasto real db=USD {r['gasto_real_usd_desde_db']:.4f} "
              f"| cruce db==jsonl ok={r['cruce_db_jsonl']['ok']} "
              f"dif={r['cruce_db_jsonl']['dif']} | modelos="
              f"{r['modelo_resuelto_por_llamada']} | intactas="
              f"{r['produccion_y_cobertura_intactas_por_sha']}/"
              f"{r['insumos_v1_intactos_por_sha']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
