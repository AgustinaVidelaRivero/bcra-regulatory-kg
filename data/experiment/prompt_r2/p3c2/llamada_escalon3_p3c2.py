"""
llamada_escalon3_p3c2.py — U-PROMPT-R2, P3c-2: la llamada real de confirmación del tercer escalón del reintento por
corte (decisión 6 de la autora sobre el FRENO P3c-1; tope USD 0,20, en una base de caché propia de P3c-2).

Con `cliente_e1.ClienteE1Real(transmision=True)`, el perfil r2b re-congelado (322c5a23e9b7) y una unidad corta ya leída
(`cla::5.1.1::intro`, de `e0_chunking/salida_tanda0_r2b`):
  0. sin red: el mismo pedido sin transmisión lo rechaza el SDK antes de enviarlo (la guarda de los 10 minutos);
  1. el pedido con max_tokens = MAX_TOKENS_LLAMADA (24.576) va por el adaptador de transmisión: el mensaje final trae
     el `tool_use`, el `usage` y el `stop_reason`. No usa el techo de 40.960: con él, el peor caso (USD 0,20 de salida
     más la escritura del prefijo) pasaría el tope de la llamada; 24.576 está por encima de LIMITE_SIN_TRANSMISION
     (21.333), así que el despacho y la transmisión son los del escalón. El techo de 40.960 lo ejercita
     selftest_ub53.py (P7) con un SDK falso;
  2. el crudo que guarda la caché tiene las claves de una llamada sin transmisión (se compara con un crudo de la base
     de P4, `--crudo-referencia`: el de la misma unidad con el prefijo de P3b-2);
  3. el mismo pedido, repetido, sale de la caché (acierto, sin API);
  4. un corte forzado: la misma unidad con un max_tokens bajo, por el adaptador, da `stop_reason` «max_tokens».
Antes de habilitar el escalón se verificó en la documentación oficial que la ventana de contexto de `claude-sonnet-5`
(E3) es de 1 M tokens (https://platform.claude.com/docs/en/models/sonnet-5/overview, consultada el 04/10/2026).

La clave de la API se lee de data/experiment/evaluacion/.env (precedente: runner_pareada_b54.py:148) y no se imprime.
El costo se calcula con la fórmula de caching (decisión 2); cada respuesta real queda en el log de usage (decisión 3).
Escribe solo en --salida (llamada_escalon3_p3c2.json) y en --db.

Uso (desde la raíz de una copia del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3c2/llamada_escalon3_p3c2.py \
      --db DIR/p3c2_e1.db --crudo-referencia DB_DE_P4 --salida DIR
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
import cliente_e1  # noqa: E402
import perfil_e1  # noqa: E402

UNIDAD = "cla::5.1.1::intro"
MODELO = "claude-haiku-4-5"
TOPE_USD = 0.20
MAX_TOKENS_LLAMADA = 24576
MAX_TOKENS_CORTE_FORZADO = 64
P_E1 = dict(precio_in_por_mtok=1.00, precio_out_por_mtok=5.00, precio_cache_write_por_mtok=1.25,
            precio_cache_read_por_mtok=0.10)


def cargar_env() -> None:
    for linea in (REPO / "data" / "experiment" / "evaluacion" / ".env").read_text(encoding="utf-8").splitlines():
        if "=" in linea and not linea.strip().startswith("#"):
            k, v = linea.split("=", 1)
            os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))


def claves(d, pref=""):
    """Las claves de un crudo, con la ruta, sin los valores (los bloques de contenido, por tipo)."""
    out = set()
    if isinstance(d, dict):
        for k, v in d.items():
            out.add(pref + k)
            if k == "content" and isinstance(v, list):
                for b in v:
                    out |= claves(b, f"{pref}content[{b.get('type')}].")
            elif k == "usage" and isinstance(v, dict):
                out |= claves(v, pref + "usage.")
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", type=Path, required=True)
    ap.add_argument("--crudo-referencia", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    for p in (a.db, a.salida):
        if REPO in p.resolve().parents:
            raise SystemExit("--db y --salida van fuera del repo")
    cargar_env()
    pf = perfil_e1.perfil("r2b")
    chunk = next(c for c in json.loads((REX / "e0_chunking" / "salida_tanda0_r2b" / "chunks_cla.json")
                                       .read_text(encoding="utf-8")) if c["id"] == UNIDAD)
    cli = cliente_e1.ClienteE1Real(**P_E1, tope_usd=TOPE_USD, run_label="p3c2_escalon3", db_path=a.db,
                                   prefijo_hash=pf.prefijo_hash_para_namespace, transmision=True)
    base = pf.build_request_kwargs(chunk, model=MODELO)
    k40 = dict(base, max_tokens=MAX_TOKENS_LLAMADA)
    assert cliente_e1.LIMITE_SIN_TRANSMISION < MAX_TOKENS_LLAMADA < cliente_e1.MAX_TOKENS_ESCALON_3_R2
    try:
        cli._real.messages.create(**k40)      # sin transmisión: el SDK lo rechaza antes de enviarlo
        guarda = "no rechazó"
    except ValueError as exc:
        guarda = f"rechazado sin enviar: {str(exc)[:80]}"
    k64 = dict(base, max_tokens=MAX_TOKENS_CORTE_FORZADO)
    r1 = cli.create(doc=chunk["archivo"], **k40)
    tu = next((b for b in r1.content if getattr(b, "type", None) == "tool_use"), None)
    stats1 = dict(cli.cache_transmision.stats())
    r2 = cli.create(doc=chunk["archivo"], **k40)
    stats2 = dict(cli.cache_transmision.stats())
    # corte forzado por el adaptador (con 64 tokens el despacho normal no transmitiría)
    r3 = cli._crear_en(cli._cache_transmision(""), cliente_e1.COMPONENTE_ESCALON_3, chunk["archivo"], k64)
    resumen = cli.resumen()
    cli.close()
    con = sqlite3.connect(a.db)
    crudos = {k: json.loads(raw) for k, raw in con.execute("SELECT key, raw_json FROM cache")}
    con.close()
    con = sqlite3.connect(f"file:{a.crudo_referencia}?mode=ro&immutable=1", uri=True)
    ref = json.loads(next(iter(con.execute("SELECT raw_json FROM cache LIMIT 1")))[0])
    con.close()
    k_ref = claves(ref)
    ns = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace)
    out = {
        "comando": "data/experiment/prompt_r2/p3c2/llamada_escalon3_p3c2.py --db DB --crudo-referencia DB_P4 --salida DIR",
        "unidad": UNIDAD, "modelo": MODELO, "namespace": ns, "prefijo_hash": pf.prefijo_hash_para_namespace,
        "documentacion_contexto_e3": {"modelo": "claude-sonnet-5", "ventana_de_contexto_tokens": 1_000_000,
                                      "fuente": "https://platform.claude.com/docs/en/models/sonnet-5/overview",
                                      "consulta": "04/10/2026"},
        "control_sin_transmision": guarda,
        "llamada_1_transmision": {"max_tokens": k40["max_tokens"], "stop_reason": r1.stop_reason,
                                  "tool_use": tu is not None, "entidades": len((tu.input or {}).get("entities") or [])
                                  if tu is not None else None,
                                  "usage": r1.usage.model_dump(mode="json"), "cache_stats": stats1},
        "llamada_2_repetida": {"stop_reason": r2.stop_reason, "cache_stats": stats2,
                               "acierto": stats2["hits"] == stats1["hits"] + 1 and stats2["misses"] == stats1["misses"]},
        "llamada_3_corte_forzado": {"max_tokens": MAX_TOKENS_CORTE_FORZADO, "stop_reason": r3.stop_reason,
                                    "usage": r3.usage.model_dump(mode="json")},
        "crudo_guardado": {"filas_en_la_db": len(crudos),
                           "claves_iguales_a_una_llamada_sin_transmision": all(
                               claves(c) <= k_ref | {"content[text].text", "content[text].type",
                                                     "content[text].citations"} and "parsed_output" not in json.dumps(c)
                               for c in crudos.values()),
                           "claves_de_referencia": sorted(k_ref),
                           "claves_por_fila": {k[:12]: sorted(claves(c)) for k, c in crudos.items()}},
        "gasto": {"usd": resumen["gasto_usd_real"], "tope_usd": TOPE_USD, "llamadas": resumen["llamadas"],
                  "hits": resumen["hits_cache_local"]},
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "llamada_escalon3_p3c2.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                        encoding="utf-8")
    print(json.dumps({k: v for k, v in out.items() if k != "crudo_guardado"}, ensure_ascii=False, indent=1))
    print("crudo:", out["crudo_guardado"]["filas_en_la_db"], out["crudo_guardado"]["claves_iguales_a_una_llamada_sin_transmision"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
