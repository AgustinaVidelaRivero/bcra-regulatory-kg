"""
sondeo_temperatura_e3.py — U-PROMPT-R2, P5, control 1 (antes de tocar código): una llamada que confirma que la API
rechaza `temperature` 0 con el modelo de E3 (`runner_corpus.MODEL_E3`). Se espera un error 400. Si la API la acepta,
P5 frena y decide la autora.

El pedido es mínimo y no pasa por la caché local ni por el cliente de E3 (no es un pedido de E3: no lleva su prefijo,
su tool schema ni su mensaje). Cota de costo si la API lo aceptara: menos de 20 tokens de entrada y `max_tokens` 8, a
la tarifa del modelo (USD 2 y 10 por millón, documentación del modelo consultada el 05/10/2026): menos de USD 0,0002.
Un error 400 no se factura. Sin reintentos (`max_retries=0`).

Escribe solo --salida. La clave de la API se lee de data/experiment/evaluacion/.env (--env) y no se imprime.
Uso (desde la raíz de una copia del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/sondeo_temperatura_e3.py \
      --env ENV --salida DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
import runner_corpus as RC  # noqa: E402 — solo el modelo de E3

PEDIDO = {"model": RC.MODEL_E3, "max_tokens": 8, "temperature": 0,
          "messages": [{"role": "user", "content": "Respondé solo: ok"}]}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--env", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    out_dir = a.salida.resolve()
    if REPO in out_dir.parents or out_dir == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    out_dir.mkdir(parents=True, exist_ok=True)
    from dotenv import load_dotenv  # noqa: PLC0415
    load_dotenv(a.env)              # la clave no se imprime
    import anthropic  # noqa: PLC0415
    cli = anthropic.Anthropic(max_retries=0)
    out = {"cuando_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"), "sdk": anthropic.__version__,
           "pedido": PEDIDO}
    try:
        resp = cli.messages.create(**PEDIDO)
        u = resp.usage
        out.update({"aceptada": True, "modelo_respuesta": resp.model, "stop_reason": resp.stop_reason,
                    "usage": {"input_tokens": u.input_tokens, "output_tokens": u.output_tokens}})
    except anthropic.APIStatusError as e:
        cuerpo = e.body if isinstance(e.body, (dict, list, str)) else str(e.body)
        out.update({"aceptada": False, "status_code": e.status_code, "tipo": type(e).__name__,
                    "request_id": getattr(e, "request_id", None), "cuerpo": cuerpo})
    (out_dir / "sondeo_temperatura_e3.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
    print(json.dumps(out, ensure_ascii=False), flush=True)
    return 0 if out["aceptada"] is False and out.get("status_code") == 400 else 3


if __name__ == "__main__":
    raise SystemExit(main())
