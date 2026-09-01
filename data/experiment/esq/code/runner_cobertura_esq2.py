"""
runner_cobertura_esq2.py — FASE (d) de U-ESQ-2: extracción E1-solo de las 762
unidades de los 10 TOs del universo sellado (pre-registro §1), modo cerrado,
flag apagado, sin el atajo del rol (cuarentena D5 heredada — los 10 archivos
no están en ROL_POR_TO; guarda por chunk).

Invoca el pipeline de extracción SIN modificarlo: prompt_e1.build_request_kwargs
(canal_abierto=False, default de producción) + validador_e1.validar_salida.
Cliente propio de la unidad (comun_cobertura_esq2.ClienteCoberturaEsq2): db
esq/cache/esq_cobertura.db + namespace esq2_cobertura_e1 (propios, sin colisión
con producción ni con la saga ESQ), tope duro USD 6,50 cableado.

Frenos (todos duros):
  - cliente: proyección pre-llamada contra el tope (TopeExcedido).
  - runner: margen por unidad antes de cada llamada; proyección lineal
    gasto/hechas × 762 al cierre de cada TO.
  - corrida real solo con --autorizado-tope 6.50 (eco de la autorización).

Persistencia (patrón runner_corpus.fase_e1, MISMAS claves que producción):
cobertura/<to>/extracciones_e1_<to>.jsonl append-only (chunk_id, unidad,
tipo_unidad, titulo, stop_reason, error, usage, tool_input_crudo, validacion);
reanudación idempotente por last-wins (se saltean las persistidas sin error).
SECUENCIAL (D4): un cliente, un loop, orden sellado de TOS_ESQ2.

Cierre (corre solo al completar las 762): resumen global con gasto real desde
la db propia (una fila = una response real pagada), modelo RESUELTO por llamada
leído de la db, cruce db==jsonl por unidad, verificación de producción intacta
por sha (contra cobertura/sellos_produccion_sha256.json del selftest) y
creación de data/experiment/esq/documentos_excluidos_esq.json (laudo §1.iv).

Uso:
  selftest offline: via selftest_cobertura_esq2.py (--stub, salida propia)
  corrida real (SOLO con autorización explícita de la autora en el chat):
    .venv/bin/python3 -B data/experiment/esq/code/runner_cobertura_esq2.py \
        --autorizado-tope 6.50
  --solo-cierre: recomputa resumen/cruces desde lo persistido, sin API.
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

import comun_cobertura_esq2 as cc      # noqa: E402
import comun_e1                        # noqa: E402
import prompt_e1                       # noqa: E402
import validador_e1                    # noqa: E402
import llm_cache as lc                 # noqa: E402

MARGEN_UNIDAD_USD = 0.06   # > proyección de una llamada fría del cliente


class Freno(RuntimeError):
    pass


# --------------------------------------------------------------------------- #
# Guardas previas a cualquier gasto                                           #
# --------------------------------------------------------------------------- #
def verificar_cerrado(chunk: dict) -> dict:
    """Asserts de que el request es EXACTAMENTE el de producción flag-off y de
    que la caché es la propia. Corre antes de la primera llamada; si algo no
    cierra, nada se gasta."""
    ns = cc.namespace_cobertura()
    ns_prod = cc.namespace_produccion()
    kwargs = prompt_e1.build_request_kwargs(chunk, model=cc.MODEL_E1)
    props_e = kwargs["tools"][0]["input_schema"]["properties"]["entities"][
        "items"]["properties"]
    props_r = kwargs["tools"][0]["input_schema"]["properties"]["relations"][
        "items"]["properties"]
    ok = {
        "prefijo_hash_cerrado": prompt_e1.prefijo_hash(False),
        "namespace": ns,
        "candado_prefijo": prompt_e1.prefijo_hash(False) == cc.PREFIJO_HASH_CERRADO_ESPERADO,
        "system_es_prefijo_produccion": (
            kwargs["system"][0]["text"] == prompt_e1.PREFIJO_SISTEMA),
        "tool_schema_es_produccion": kwargs["tools"][0] is prompt_e1.TOOL_SCHEMA_E1,
        "sin_tipo_propuesto": "tipo_propuesto" not in props_e,
        "sin_predicado_propuesto": "predicado_propuesto" not in props_r,
        "namespace_propio_distinto_produccion": ns != ns_prod and ns.startswith(cc.DOMAIN),
        "db_propia": str(cc.DB_COBERTURA) not in {str(p) for p in cc.DBS_AJENAS},
        "model": kwargs["model"],
    }
    if not all(v is True for k, v in ok.items()
               if k not in ("prefijo_hash_cerrado", "namespace", "model")):
        raise Freno(f"guarda de modo cerrado falló: {ok} — no se gasta")
    return ok


def verificar_sin_rol(chunk: dict, mensaje: str) -> None:
    """Cuarentena D5 por chunk: el archivo no resuelve rol y el mensaje no
    trae bloque de alcance."""
    from schema import ROL_POR_TO
    if ROL_POR_TO.get(chunk["archivo"]) is not None:
        raise Freno(f"{chunk['id']}: archivo {chunk['archivo']} resuelve rol "
                    f"en ROL_POR_TO — cuarentena D5 violada")
    if "Alcance de este TO" in mensaje:
        raise Freno(f"{chunk['id']}: el mensaje trae bloque de alcance — "
                    f"cuarentena D5 violada")


# --------------------------------------------------------------------------- #
# Stub offline (selftest)                                                     #
# --------------------------------------------------------------------------- #
class StubClienteCobertura:
    """Cliente offline: extracción mínima válida por chunk; interfaz
    .create(doc=..., **kw) como el real; usage en cero."""

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
            self.usage = StubClienteCobertura._U()

    def __init__(self):
        self.gasto_usd = 0.0
        self.llamadas = 0
        self.llamadas_hit = 0
        self.chunk_ids_llamados: list[str] = []

    def create(self, doc=None, **kwargs):
        self.llamadas += 1
        msg = kwargs["messages"][0]["content"]
        punto = None
        for linea in msg.splitlines():
            if linea.startswith(("Punto del chunk:", "Unidad de origen:")):
                punto = linea.split(":", 1)[1].strip().split(" ", 1)[0]
                break
        self.chunk_ids_llamados.append(punto)
        return StubClienteCobertura._R({
            "entities": [{"local_id": "to", "type": "TextoOrdenado",
                          "label": "TO stub", "punto": punto, "properties": {}},
                         {"local_id": "e1", "type": "Obligacion",
                          "label": f"obligación stub {punto}",
                          "punto": punto, "properties": {}}],
            "relations": [{"source": "e1", "target": "to",
                           "predicate": "establecida_en", "punto": punto}],
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
    with path.open("a", encoding="utf-8") as f:
        f.write(json.dumps(reg, ensure_ascii=False) + "\n")
        f.flush()
        os.fsync(f.fileno())


def llamar_con_reintentos_api(fn, descripcion: str, max_intentos: int = 3):
    """Reintento ante errores transitorios de API (patrón runner_corpus).
    TopeExcedido NO se reintenta: es freno."""
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


def correr(cliente, salida: Path, tope_usd: float, stub: bool,
           tos: tuple[str, ...] = cc.TOS_ESQ2,
           limite: int | None = None, abortar_tras: int | None = None) -> dict:
    total_global = 0
    hechas_global = 0
    hechas_este_proceso = 0
    t0 = time.time()
    todos_los_chunks: list[tuple[str, dict]] = []
    for to in tos:
        chunks = [c for c in cc.cargar_chunks_esq2((to,))]
        if limite:
            chunks = chunks[:limite]
        todos_los_chunks.append((to, chunks))
        total_global += len(chunks)

    guardas = verificar_cerrado(todos_los_chunks[0][1][0])
    print(f"[guardas] namespace={guardas['namespace']} | prefijo cerrado="
          f"{guardas['prefijo_hash_cerrado']} (candado OK)", flush=True)

    for to, chunks in todos_los_chunks:
        tdir = salida / to
        tdir.mkdir(parents=True, exist_ok=True)
        jsonl = tdir / f"extracciones_e1_{to}.jsonl"
        previos = cc.cargar_jsonl_last_wins(jsonl)
        hechas_ok = {cid for cid, r in previos.items() if r.get("error") is None}
        pendientes = [c for c in chunks if c["id"] not in hechas_ok]
        hechas_global += len(hechas_ok)
        print(f"[{to}] unidades={len(chunks)} ya_persistidas_ok={len(hechas_ok)} "
              f"pendientes={len(pendientes)}", flush=True)

        errores_consecutivos = 0
        for c in pendientes:
            if cliente.gasto_usd + MARGEN_UNIDAD_USD > tope_usd:
                raise Freno(f"tope USD {tope_usd:.2f} antes de {c['id']}: "
                            f"gasto USD {cliente.gasto_usd:.4f} + margen "
                            f"{MARGEN_UNIDAD_USD}")
            kwargs = prompt_e1.build_request_kwargs(c, model=cc.MODEL_E1)
            verificar_sin_rol(c, kwargs["messages"][0]["content"])
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
            hechas_global += 1
            hechas_este_proceso += 1
            errores_consecutivos = 0 if err is None else errores_consecutivos + 1
            if errores_consecutivos > 5:
                raise Freno(f"{to}: más de 5 errores de API consecutivos "
                            f"(último: {err}) — problema sistémico, se frena")
            if hechas_global % 25 == 0 or err:
                print(f"[{hechas_global}/{total_global}] {c['id']:<28s} "
                      f"gasto=USD {cliente.gasto_usd:.4f}"
                      + (f" ERROR {err}" if err else ""), flush=True)
            if abortar_tras and hechas_este_proceso >= abortar_tras:
                print(f"ABORT SIMULADO tras {hechas_este_proceso} unidades "
                      f"de este proceso", flush=True)
                sys.exit(9)

        # resumen del TO + freno por proyección lineal
        regs_to = cc.cargar_jsonl_last_wins(jsonl)
        agg_to = cc.agregar_usage([r.get("usage") for r in regs_to.values()])
        (tdir / f"resumen_e1_{to}.json").write_text(json.dumps({
            "to": to, "n_unidades": len(chunks),
            "persistidas": len(regs_to),
            "con_error": sorted(cid for cid, r in regs_to.items()
                                if r.get("error") is not None),
            "usage_agregado": agg_to,
            "gasto_cliente_acumulado_usd": round(cliente.gasto_usd, 4),
        }, ensure_ascii=False, indent=1), encoding="utf-8")
        if hechas_global and not stub:
            proy = cliente.gasto_usd / hechas_global * total_global
            print(f"[{to}] cierre: gasto=USD {cliente.gasto_usd:.4f} "
                  f"proyección_762=USD {proy:.4f} (tope {tope_usd})", flush=True)
            if proy > tope_usd:
                raise Freno(f"proyección USD {proy:.4f} supera el tope "
                            f"{tope_usd:.2f} al cierre de {to}")

    return {"wall_s": round(time.time() - t0, 1),
            "total": total_global, "hechas": hechas_global,
            "guardas": guardas}


# --------------------------------------------------------------------------- #
# Cierre: gasto real desde la db, modelo por llamada, cruce db==jsonl,        #
# producción intacta, documentos_excluidos_esq.json                           #
# --------------------------------------------------------------------------- #
def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def cierre(salida: Path, db_path: Path = cc.DB_COBERTURA,
           tos: tuple[str, ...] = cc.TOS_ESQ2) -> dict:
    ns = cc.namespace_cobertura()
    conn = cc.conectar_db_readonly(db_path)

    total = ok_cruce = dif_cruce = sin_fila = con_error = 0
    modelos: dict[str, int] = {}
    usage_db = []
    detalle_dif: list[str] = []
    for to in tos:
        jsonl = salida / to / f"extracciones_e1_{to}.jsonl"
        regs = cc.cargar_jsonl_last_wins(jsonl)
        for c in cc.cargar_chunks_esq2((to,)):
            total += 1
            reg = regs.get(c["id"])
            if reg is None or reg.get("error") is not None:
                con_error += 1
                if reg is None:
                    detalle_dif.append(f"{c['id']}: sin registro en jsonl")
                continue
            kwargs = prompt_e1.build_request_kwargs(c, model=cc.MODEL_E1)
            key = lc.compute_key(ns, lc.canonical_request(kwargs))
            row = conn.execute("SELECT * FROM cache WHERE key = ?",
                               (key,)).fetchone()
            if row is None:
                sin_fila += 1
                detalle_dif.append(f"{c['id']}: sin fila en la db propia")
                continue
            modelos[row["model"]] = modelos.get(row["model"], 0) + 1
            usage_db.append({"input_tokens": row["input_tokens"],
                             "output_tokens": row["output_tokens"],
                             "cache_write_tokens": row["cache_write_tokens"],
                             "cache_read_tokens": row["cache_read_tokens"]})
            if cc.tool_input_de_raw(row["raw_json"]) == reg.get("tool_input_crudo"):
                ok_cruce += 1
            else:
                dif_cruce += 1
                detalle_dif.append(f"{c['id']}: tool_input db != jsonl")
    # gasto real: TODAS las filas del namespace propio (una fila = una response
    # real pagada; incluye eventuales llamadas con error persistidas en db)
    filas_ns = conn.execute(
        "SELECT COUNT(*), COALESCE(SUM(input_tokens),0), "
        "COALESCE(SUM(output_tokens),0), COALESCE(SUM(cache_write_tokens),0), "
        "COALESCE(SUM(cache_read_tokens),0) FROM cache WHERE namespace = ?",
        (ns,)).fetchone()
    agg_ns = {"n": filas_ns[0], "input_tokens": filas_ns[1],
              "output_tokens": filas_ns[2], "cache_write_tokens": filas_ns[3],
              "cache_read_tokens": filas_ns[4]}
    conn.close()
    gasto_real = cc.costo_usd_desde_usage(agg_ns)

    # producción intacta por sha (contra los sellos del selftest)
    sellos_path = cc.COBERTURA_DIR / "sellos_produccion_sha256.json"
    produccion_intacta = None
    sellos_dif = []
    if sellos_path.exists():
        sellos = json.loads(sellos_path.read_text(encoding="utf-8"))
        for rel, sha in sellos["archivos"].items():
            p = cc.REPO_DIR / rel
            actual = sha256_de(p) if p.exists() else "AUSENTE"
            if actual != sha:
                sellos_dif.append(f"{rel}: {sha[:12]} → {actual[:12]}")
        produccion_intacta = not sellos_dif

    # documentos_excluidos_esq.json (laudo §1.iv) — 10 IDs + sha256 de los PDF
    manifest = {}
    for linea in (cc.EXP_DIR / "escalado_prep" / "manifest_pdfs.sha256"
                  ).read_text(encoding="utf-8").splitlines():
        if linea.strip():
            sha, nombre = linea.split()
            manifest[nombre] = sha
    docs_excluidos = []
    for to in tos:
        pdf = cc.ESCALADO_PDFS / f"{to}.pdf"
        sha = sha256_de(pdf)
        docs_excluidos.append({
            "id": to, "archivo": f"{to}.pdf", "sha256": sha,
            "coincide_manifest": manifest.get(f"{to}.pdf") == sha})
    excluidos_doc = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "regla": ("laudo ESQ-2 §1.iii/§1.iv (8dea823) + pre-registro §1 "
                  "(2240c9c): los 10 TOs extraídos por ESQ-2 pasan al conjunto "
                  "de desarrollo a efectos del esquema y quedan EXCLUIDOS de "
                  "la evaluación final; B6.3 cita este archivo al construir "
                  "su eval set"),
        "sorteo": "D4/ESQ-1, semilla 20260827 (docs/laudo_ESQ-1_diseno.md)",
        "sha256_fuente": ("recomputado de escalado_prep/pdfs/<to>.pdf y "
                          "cruzado contra escalado_prep/manifest_pdfs.sha256"),
        "documentos": docs_excluidos,
    }
    (cc.UNIDAD_DIR / "documentos_excluidos_esq.json").write_text(
        json.dumps(excluidos_doc, ensure_ascii=False, indent=1), encoding="utf-8")

    resumen = {
        "generado": datetime.now().isoformat(timespec="seconds"),
        "namespace": ns,
        "db": str(db_path.relative_to(cc.REPO_DIR)),
        "unidades_universo": total,
        "persistidas_sin_error": total - con_error,
        "con_error_o_sin_registro": con_error,
        "modelo_resuelto_por_llamada": modelos,
        "cruce_db_jsonl": {"ok": ok_cruce, "dif": dif_cruce,
                           "sin_fila_db": sin_fila,
                           "detalle": detalle_dif[:50]},
        "filas_db_namespace_propio": agg_ns,
        "gasto_real_usd_desde_db": round(gasto_real, 4),
        "formula_costo": ("D2: in×1,00 + out×5,00 + cw×1,25 + cr×0,10 "
                          "(USD/MTok), decisiones_caching_extraccion.md:32-42; "
                          "tarifas runner_corpus.py:76-78"),
        "tope_usd": cc.TOPE_USD,
        "produccion_intacta_por_sha": produccion_intacta,
        "sellos_divergentes": sellos_dif,
        "documentos_excluidos": str((cc.UNIDAD_DIR / "documentos_excluidos_esq.json"
                                     ).relative_to(cc.REPO_DIR)),
    }
    (cc.COBERTURA_DIR / "resumen_cobertura_esq2.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1), encoding="utf-8")
    return resumen


def main() -> int:
    ap = argparse.ArgumentParser(description="Extracción E1-solo ESQ-2 (762 u, modo cerrado)")
    ap.add_argument("--stub", action="store_true", help="cliente stub, offline")
    ap.add_argument("--salida", type=Path, default=cc.COBERTURA_DIR)
    ap.add_argument("--db", type=Path, default=cc.DB_COBERTURA)
    ap.add_argument("--autorizado-tope", type=float, default=None,
                    help="eco de la autorización; debe ser 6.50 para corrida real")
    ap.add_argument("--limite", type=int, default=None,
                    help="solo primeras N unidades por TO (pruebas)")
    ap.add_argument("--abortar-tras", type=int, default=None,
                    help="sys.exit(9) tras N unidades (prueba de reanudación)")
    ap.add_argument("--solo-cierre", action="store_true",
                    help="recomputa el cierre desde lo persistido, sin API")
    args = ap.parse_args()

    if args.solo_cierre:
        r = cierre(args.salida, db_path=args.db)
        print(json.dumps({k: r[k] for k in ("unidades_universo",
              "persistidas_sin_error", "modelo_resuelto_por_llamada",
              "gasto_real_usd_desde_db", "produccion_intacta_por_sha")},
              ensure_ascii=False, indent=1))
        return 0

    if args.stub:
        cliente = StubClienteCobertura()
    else:
        if args.autorizado_tope != cc.TOPE_USD:
            print(f"ABORTADO: la corrida real exige --autorizado-tope "
                  f"{cc.TOPE_USD} (eco de la autorización del chat). "
                  f"Nada se llamó.")
            return 2
        from dotenv import load_dotenv
        load_dotenv(comun_e1.EVAL_DIR / ".env")
        if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
            print(f"ANTHROPIC_API_KEY ausente (esperada en {comun_e1.EVAL_DIR / '.env'})")
            return 1
        cliente = cc.ClienteCoberturaEsq2(
            **cc.P_E1, tope_usd=cc.TOPE_USD, run_label="esq2_cobertura_e1",
            db_path=args.db)

    try:
        meta = correr(cliente, args.salida, cc.TOPE_USD, stub=args.stub,
                      limite=args.limite, abortar_tras=args.abortar_tras)
    except Freno as e:
        print(f"\nFRENO: {e}", flush=True)
        return 3
    finally:
        cliente_res = cliente.resumen()
        cliente.close()

    print(f"\ncorrida: {meta['hechas']}/{meta['total']} unidades | "
          f"wall={meta['wall_s']}s | gasto cliente=USD "
          f"{cliente_res.get('gasto_usd_real', 0):.4f}", flush=True)

    if not args.stub and not args.limite and meta["hechas"] >= meta["total"]:
        r = cierre(args.salida, db_path=args.db)
        print(f"cierre: gasto real db=USD {r['gasto_real_usd_desde_db']:.4f} "
              f"| cruce db==jsonl ok={r['cruce_db_jsonl']['ok']} "
              f"dif={r['cruce_db_jsonl']['dif']} | modelos="
              f"{r['modelo_resuelto_por_llamada']} | producción intacta="
              f"{r['produccion_intacta_por_sha']}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
