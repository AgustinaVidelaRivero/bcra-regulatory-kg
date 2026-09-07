"""U-COB-A fase A.2 — corrida de extraccion sobre los NUEVE documentos.

AUTORIZADA con tope USD 4,00 sobre el pre-registro v4 sellado
(sha 87fae986a8dc5370bef67c65e257409b26653a021f262e007d3348f21657b0ff).
Alcance: las 191 unidades, los DOS BRAZOS COMPLETOS (77 prosa + 114 planilla).

Cableado (patron obligatorio del repo, sin excepcion):
  · perfil `v3_b54` de `perfil_e1` — el prefijo v3 cableado, que integra el
    esquema CONGELADO del gate ESQ-3. Su constructor RECOMPUTA sha256 y hash
    del prefijo y FRENA si no reproducen el sello, antes de toda llamada.
  · `cliente_e1.ClienteE1Real` — CachingClient (never-pay-twice + captura del
    crudo integro), contabilidad D2 con la formula de caching, tope duro.
  · DB de cache PROPIA de la unidad (`cache/a2_bloque_a.db`): el mandato
    acota las escrituras a este directorio, y el ciclo de vida difiere del
    pipeline principal.
  · SECUENCIAL (decision 4 de docs/decisiones_caching_extraccion.md: corridas
    con prefijo identico no van en paralelo, o cada una paga el cache write).

Uso:  python3 correr_a2.py [--dry]      (--dry no llama a la API)
"""
from __future__ import annotations

import json
import os
import sys
import time
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402

E1_DIR = C.EXPERIMENT / "reextraccion_v2" / "e1_extractor"
B54_DIR = C.EXPERIMENT / "b54_catalogo_v3" / "code"
for d in (str(E1_DIR), str(B54_DIR)):
    if d not in sys.path:
        sys.path.insert(0, d)

import perfil_e1  # noqa: E402
import cliente_e1  # noqa: E402
import validador_e1  # noqa: E402
from comun_e1 import EVAL_DIR  # noqa: E402

MODEL = "claude-haiku-4-5"
P_IN, P_OUT, P_CW, P_CR = 1.00, 5.00, 1.25, 0.10      # USD/MTok, Haiku 4.5
TOPE_USD = 4.00                                        # autorizacion del 07/09
ESTIMADO_USD = 0.9711                                  # via caracter (calibrada)
RUN_LABEL = "ucoba_a2_bloque_a_v4"
PERFIL = "v3_b54"

SELLO_PRERREGISTRO = (
    "87fae986a8dc5370bef67c65e257409b26653a021f262e007d3348f21657b0ff")

OUT_DIR = C.UNIDAD / "a2_salida"
DB_PATH = C.UNIDAD / "cache" / "a2_bloque_a.db"


def main() -> int:
    dry = "--dry" in sys.argv

    # --- candado 1: el pre-registro sellado no cambio ---
    import hashlib
    sha = hashlib.sha256(
        (C.UNIDAD / "prerregistro_A2_v4.md").read_bytes()).hexdigest()
    if sha != SELLO_PRERREGISTRO:
        print(f"FRENO: el pre-registro v4 no reproduce su sello\n  esperado "
              f"{SELLO_PRERREGISTRO}\n  medido   {sha}")
        return 1
    print(f"pre-registro v4 sellado OK: {sha[:16]}...")

    # --- candado 2: el perfil recomputa el sello del prefijo v3 ---
    p = perfil_e1.perfil(PERFIL)
    print(f"perfil={PERFIL} · prefijo_hash={p.prefijo_hash_para_namespace}")

    chunks = json.loads((C.UNIDAD / "chunks_a2.json").read_text(encoding="utf-8"))
    assert len(chunks) == 191, len(chunks)
    n_prosa = sum(1 for c in chunks if c["brazo"] == "prosa")
    assert n_prosa == 77 and len(chunks) - n_prosa == 114
    print(f"unidades: {len(chunks)} = {n_prosa} prosa + {len(chunks)-n_prosa} planilla")

    if dry:
        print("--dry: no se llama a la API")
        return 0

    from dotenv import load_dotenv
    load_dotenv(EVAL_DIR / ".env")
    if not os.environ.get("ANTHROPIC_API_KEY", "").strip():
        print(f"ANTHROPIC_API_KEY ausente (esperada en {EVAL_DIR / '.env'})")
        return 1

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    cli = cliente_e1.ClienteE1Real(
        precio_in_por_mtok=P_IN, precio_out_por_mtok=P_OUT,
        precio_cache_write_por_mtok=P_CW, precio_cache_read_por_mtok=P_CR,
        tope_usd=TOPE_USD, run_label=RUN_LABEL, db_path=DB_PATH,
        prefijo_hash=p.prefijo_hash_para_namespace,
    )
    print(f"modelo={MODEL} · tope=USD {TOPE_USD:.2f} · estimado=USD "
          f"{ESTIMADO_USD:.4f} · db={DB_PATH.name}")

    jsonl = OUT_DIR / "extracciones_a2.jsonl"
    t0 = time.time()
    frenado = None
    with jsonl.open("w", encoding="utf-8") as fh:
        for i, ch in enumerate(chunks, start=1):
            kwargs = p.build_request_kwargs(ch, model=MODEL)
            try:
                # contrato: (response FINAL, response del corte o None)
                resp, resp_corte = cliente_e1.crear_con_reintento_corte(
                    cli, kwargs, doc=ch["archivo"])
            except Exception as e:                       # tope o error de red
                msg = f"{type(e).__name__}: {e}"
                if "tope" in msg.lower():
                    frenado = msg
                    print(f"\nFRENO POR TOPE en la unidad {i}/{len(chunks)}: {msg}")
                    break
                fh.write(json.dumps({"chunk_id": ch["id"], "error": msg},
                                    ensure_ascii=False) + "\n")
                continue

            tool_use = next((b for b in resp.content
                             if getattr(b, "type", None) == "tool_use"), None)
            tool_input = tool_use.input if tool_use is not None else None
            res = (validador_e1.validar_salida(tool_input, ch, esquema=p.esquema)
                   if tool_input is not None else None)
            fh.write(json.dumps({
                "chunk_id": ch["id"], "to": ch["to"], "brazo": ch["brazo"],
                "unidad": ch["unidad"], "paginas": ch["paginas"],
                "granularidad_procedencia": ch["granularidad_procedencia"],
                "stop_reason": getattr(resp, "stop_reason", None),
                "reintento_por_corte": resp_corte is not None,
                "tool_input_crudo": tool_input,
                "entidades": res.entidades if res else [],
                "relaciones": res.relaciones if res else [],
                "rechazos": res.rechazos if res else [],
                "metricas": res.metricas if res else None,
                "error": None if tool_use is not None else "no_tool_use",
            }, ensure_ascii=False, default=str) + "\n")

            if i % 20 == 0 or i == len(chunks):
                print(f"  {i:3d}/{len(chunks)} · USD {cli.gasto_usd:.4f} · "
                      f"hits {cli.llamadas_hit}/{cli.llamadas}")

    est = cli.estado() if hasattr(cli, "estado") else {}
    resumen = {
        "unidad": "U-COB-A fase A.2",
        "sello_prerregistro_v4": SELLO_PRERREGISTRO,
        "perfil": PERFIL, "prefijo_hash": p.prefijo_hash_para_namespace,
        "modelo": MODEL, "tope_usd": TOPE_USD, "estimado_usd": ESTIMADO_USD,
        "unidades_pedidas": len(chunks),
        "gasto_usd": round(cli.gasto_usd, 6),
        "llamadas": cli.llamadas, "llamadas_hit": cli.llamadas_hit,
        "segundos": round(time.time() - t0, 1),
        "frenado_por_tope": frenado,
        "estado_cliente": est,
    }
    (OUT_DIR / "resumen_corrida_a2.json").write_text(
        json.dumps(resumen, ensure_ascii=False, indent=1, default=str) + "\n",
        encoding="utf-8")
    cli.close()
    print(f"\ngasto USD {cli.gasto_usd:.4f} de tope {TOPE_USD:.2f} · "
          f"{cli.llamadas} llamadas ({cli.llamadas_hit} hits) · "
          f"{resumen['segundos']}s")
    print(f"escrito: {jsonl.relative_to(C.REPO)}")
    return 1 if frenado else 0


if __name__ == "__main__":
    raise SystemExit(main())
