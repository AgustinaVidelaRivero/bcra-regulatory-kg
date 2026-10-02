"""U-R2-CODIGO, R2.b — lector del crudo de los reintentos de E3.

El reintento de E3 es la re-extracción de E1 con el feedback del verificador
(ratchet_e3.ciclo_ratchet). Su crudo (`tool_input`) no quedaba en ningún
archivo de la corrida: `finales.jsonl` solo guarda `n_reintentos`.
  - Corridas nuevas: el runner lo persiste en `reintentos_e3.jsonl`, archivo
    compañero de `finales.jsonl` en el directorio de cada TO
    (runner_corpus.fase_e3; `leer_companero`).
  - Corridas ya hechas (r1 y la tanda 0): `leer_desde_cache` reconstruye el
    request de cada reintento registrado en `finales.jsonl` con el código del
    pipeline (veredicto de la verificación en `veredictos.jsonl` →
    `evaluar_veredicto` → bloqueantes con cita → `build_reextraccion_kwargs`
    con el perfil, el modelo y el techo de salida de la corrida), calcula su
    clave de caché y lee el crudo de `e3_verificador/cache/e1_reintentos.db`
    abierta con `mode=ro&immutable=1`.
El informe (`main`) cuenta, por generación, los reintentos de `finales.jsonl`
cuya clave está en la db y las entradas de la db que ninguna clave
reconstruida alcanza, con su fecha de creación y el `run_label` de su
acceso, para explicar la diferencia de r1 (431 entradas contra 406
reintentos; reports/u_listas_nomap/n1_inventario.json, `reintentos_db.r1`).
USD 0, sin LLM, sin red.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/lector_reintentos_e3.py --out <json>
"""

from __future__ import annotations

import argparse
import collections
import json
import sqlite3
import sys
import urllib.parse
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "e1_extractor", REX / "e3_verificador", REX, REPO / "data" / "experiment" / "evaluacion",
          REPO / "data" / "experiment" / "mantenimiento" / "code"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import cliente_e1  # noqa: E402
import comun_e3  # noqa: E402
import llm_cache  # noqa: E402
import perfil_e1  # noqa: E402
import ratchet_e3  # noqa: E402
import selftest_clave_cache as SCC  # noqa: E402  (constantes del runner por AST)

DB = REX / "e3_verificador" / "cache" / "e1_reintentos.db"
COMPANERO = "reintentos_e3.jsonl"
GENERACIONES = {
    "r1": {"salida": REX / "corpus_v2" / "salida", "perfil": "produccion_dev",
           "e0": REX / "e0_chunking" / "salida_enm01", "tos": ("pro", "cla", "ric", "cap", "ext")},
    "t0": {"salida": REX / "corpus_tanda0" / "salida", "perfil": "v3_b54",
           "e0": REX / "e0_chunking" / "salida_tanda0",
           "tos": ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")},
    "t0_dirigida": {"salida": REX / "corpus_tanda0" / "salida_dirigida", "perfil": "v3_b54",
                    "e0": REX / "e0_chunking" / "salida_tanda0",
                    "tos": ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre",
                            "pagjub", "docvig")},
}


def leer_companero(tdir: Path) -> dict[tuple[str, int], dict]:
    """(chunk_id, intento) → registro del archivo compañero (last-wins)."""
    out: dict[tuple[str, int], dict] = {}
    p = Path(tdir) / COMPANERO
    if p.exists():
        for linea in p.read_text(encoding="utf-8").splitlines():
            if linea.strip():
                r = json.loads(linea)
                out[(r["chunk_id"], r["intento"])] = r
    return out


def _jsonl(p: Path) -> list[dict]:
    return [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]


def claves_reintentos(salida: Path, to: str, perfil_nombre: str, e0: Path) -> list[dict]:
    """Por cada unidad con reintento en finales.jsonl, la clave del request
    del reintento (TOPE_REINTENTOS = 1: un reintento por unidad)."""
    k = SCC.constantes_runner()
    perfil = perfil_e1.perfil(perfil_nombre)
    ns = cliente_e1.namespace_e1(prefijo_hash=perfil.prefijo_hash_para_namespace)
    chunks = {c["id"]: c for c in comun_e3.cargar_chunks((to,), e0_dir=e0)}
    unidades = {c["unidad"] for c in chunks.values()}
    tdir = salida / to
    finales = {r["chunk_id"]: r for r in _jsonl(tdir / "finales.jsonl")}
    verif = {}
    for r in _jsonl(tdir / "veredictos.jsonl"):
        if r["fase"] == "verificacion":
            verif[r["chunk_id"]] = r          # last-wins, como cargar_jsonl_last_wins
    out = []
    for cid, f in finales.items():
        if not f.get("n_reintentos"):
            continue
        ev = ratchet_e3.evaluar_veredicto(verif[cid]["tool_input"], chunks[cid], unidades)
        kw = ratchet_e3.build_reextraccion_kwargs(
            chunks[cid], ev["bloqueantes_utilizables"], model=k["MODEL_E1"], intento=1,
            max_tokens_reintento=k["MAX_TOKENS_REINTENTO"],
            perfil=None if perfil_nombre == "produccion_dev" else perfil)
        out.append({"chunk_id": cid, "intento": 1, "namespace": ns,
                    "clave": llm_cache.compute_key(ns, llm_cache.canonical_request(kw))})
    return out


def _db():
    return sqlite3.connect(f"file:{urllib.parse.quote(str(DB.resolve()))}?mode=ro&immutable=1",
                           uri=True)


def leer_desde_cache(salida: Path, to: str, perfil_nombre: str, e0: Path) -> dict[tuple[str, int], dict]:
    """(chunk_id, intento) → {tool_input, error} leído de e1_reintentos.db por
    la clave reconstruida; las claves sin entrada no figuran."""
    out = {}
    con = _db()
    try:
        for r in claves_reintentos(salida, to, perfil_nombre, e0):
            fila = con.execute("select raw_json from cache where key = ?", (r["clave"],)).fetchone()
            if fila is None:
                continue
            msg = json.loads(fila[0])
            tis = [b.get("input") for b in (msg.get("content") or [])
                   if isinstance(b, dict) and b.get("type") == "tool_use"]
            out[(r["chunk_id"], r["intento"])] = {
                "chunk_id": r["chunk_id"], "intento": r["intento"], "clave": r["clave"],
                "tool_input": tis[0] if tis else None,
                "error": None if tis else "no_tool_use"}
    finally:
        con.close()
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    con = _db()
    informe = {"unidad": "U-R2-CODIGO", "etapa": "R2.b", "db": str(DB.relative_to(REPO)),
               "archivo_companero": COMPANERO, "generaciones": {}}
    try:
        for g, cfg in GENERACIONES.items():
            claves = []
            for to in cfg["tos"]:
                claves += [dict(r, to=to) for r in
                           claves_reintentos(cfg["salida"], to, cfg["perfil"], cfg["e0"])]
            ns = claves[0]["namespace"] if claves else None
            en_db = {k for (k,) in con.execute("select key from cache where namespace = ?", (ns,))}
            halladas = [r for r in claves if r["clave"] in en_db]
            sobrantes = sorted(en_db - {r["clave"] for r in claves})
            detalle = []
            for key in sobrantes:
                creado, req = con.execute("select created_at, request_json from cache where key = ?",
                                          (key,)).fetchone()
                labels = sorted({l for (l,) in con.execute(
                    "select run_label from access_log where key = ?", (key,)) if l})
                u = json.loads(req)["messages"][0]["content"]
                u = u if isinstance(u, str) else " ".join(b.get("text", "") for b in u)
                to = next((l[4:] for l in u.splitlines() if l.startswith("TO: ")), None)
                pto = next((l.split(": ", 1)[1].split(" ")[0] for l in u.splitlines()
                            if l.startswith("Punto del chunk: ")), None)
                detalle.append({"clave": key, "creada": creado[:10], "run_labels": labels,
                                "to": to, "punto": pto})
            informe["generaciones"][g] = {
                "namespace": ns, "entradas_db": len(en_db),
                "reintentos_en_finales": len(claves),
                "claves_reconstruidas_en_db": len(halladas),
                "reintentos_sin_entrada": [r["chunk_id"] for r in claves if r["clave"] not in en_db],
                "entradas_sin_reintento_en_finales": len(sobrantes),
                "sobrantes_por_fecha": dict(sorted(collections.Counter(d["creada"] for d in detalle).items())),
                "sobrantes_por_run_label": dict(sorted(collections.Counter(
                    "|".join(d["run_labels"]) for d in detalle).items())),
                "sobrantes": detalle,
            }
    finally:
        con.close()
    Path(a.out).write_text(json.dumps(informe, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
