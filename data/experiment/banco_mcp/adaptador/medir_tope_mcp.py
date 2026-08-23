#!/usr/bin/env python3
"""medir_tope_mcp.py — Tope de tamaño de resultado por el transporte MCP del banco
(U-A2.0-banco, entregable 7: «medí y declará el tope... el gate no pudo»).

Dos topes distintos, y se declaran por separado:

  1. TOPE DEL TRANSPORTE (servidor + SDK mcp 1.29 + stdio JSON-RPC + cliente):
     medido acá. Se construye un grafo sintético (fuera del repo, en el
     scratchpad) con un nodo cuya descripción mide N chars y se llama
     `ver_nodo` a través del servidor MCP real del KG (backend `memoria`, mismo
     código que el de producción) para N creciente; criterio: el texto recibido
     es byte-idéntico al `json.dumps` directo y el log R1 lo registra íntegro.
  2. TOPE DE CLAUDE CODE (lo que el modelo ve): documentado, NO medido acá —
     requiere una sesión real (fase B). Doc oficial (docs/en/mcp, «MCP output
     limits and warnings»): advertencia a partir de 10.000 tokens; límite por
     defecto 25.000 tokens (`MAX_MCP_OUTPUT_TOKENS`); por encima «results that
     exceed the default threshold are persisted to disk and replaced with a
     file reference in the conversation». El banco NO usa la anotación
     `anthropic/maxResultSizeChars`. El log R1 sigue siendo la fuente de verdad
     del contenido en cualquier caso.

Uso:
  .venv/bin/python -B medir_tope_mcp.py [--tamanios 100000,1000000,5000000,20000000,50000000]
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
for _p in (str(BANCO_DIR),):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from cliente_falso import ClienteFalso                              # noqa: E402
from comun_banco import rel_repo, serializar_payload, sha256_bytes, sha256_file  # noqa: E402

SERVIDOR = BANCO_DIR / "mcp_kg" / "servidor_mcp_kg.py"
SCRATCH = Path(os.environ.get("BANCO_SCRATCH", Path.home() / ".cache" / "banco_mcp_tope"))


def grafo_sintetico(n_chars: int, destino: Path) -> Path:
    nodo = {"id": "Nodo_grande", "type": "Obligacion", "label": "Nodo grande sintetico",
            "properties": {"descripcion": ("x" * 99 + "\n") * (n_chars // 100) + "x" * (n_chars % 100)},
            "provenances": [{"source_doc": "sintetico.pdf", "location": "Punto 1.1."}]}
    kg = {"nodes": [nodo, {"id": "Nodo_chico", "type": "Obligacion", "label": "Nodo chico", "properties": {},
                           "provenances": []}],
          "edges": [{"source": "Nodo_grande", "target": "Nodo_chico", "relation": "APLICA_A", "properties": {},
                     "provenances": []}]}
    destino.write_text(json.dumps(kg, ensure_ascii=False), encoding="utf-8")
    return destino


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--tamanios", default="100000,1000000,5000000,20000000,50000000")
    ap.add_argument("--out", type=Path, default=AQUI / "resultados" / "tope_mcp.json")
    a = ap.parse_args()
    SCRATCH.mkdir(parents=True, exist_ok=True)
    sys.path.insert(0, str(BANCO_DIR / "mcp_kg"))
    from servidor_mcp_kg import abrir_backend, despachar   # mismo código que producción

    filas = []
    for n in [int(x) for x in a.tamanios.split(",")]:
        kg = grafo_sintetico(n, SCRATCH / f"kg_tope_{n}.json")
        cfg = {"servidor": "mcp_kg", "version": "1.0", "backend": "memoria", "kg_path": str(kg),
               "kg_sha256_esperado": sha256_file(kg), "firma_tools": "v1", "nota": "medición de tope"}
        cfg_path = SCRATCH / f"config_tope_{n}.json"
        cfg_path.write_text(json.dumps(cfg) + "\n", encoding="utf-8")
        log = SCRATCH / f"log_tope_{n}.jsonl"
        if log.exists():
            log.unlink()
        idx, _ = abrir_backend(cfg)
        directo = serializar_payload(despachar(idx, "ver_nodo", {"id": "Nodo_grande"}))
        fila = {"n_chars_descripcion": n, "chars_resultado": len(directo), "bytes_utf8": len(directo.encode("utf-8"))}
        t0 = time.perf_counter()
        try:
            with ClienteFalso([sys.executable, "-B", str(SERVIDOR), "--config", str(cfg_path)],
                              env={"BANCO_LOG_R1": str(log), "BANCO_SESION_TAG": f"tope_{n}"}, timeout_s=900) as cli:
                via = cli.llamar("ver_nodo", {"id": "Nodo_grande"})
            fila |= {"ok_transporte": True, "byte_identico": via == directo, "segundos": round(time.perf_counter() - t0, 2)}
        except Exception as e:
            fila |= {"ok_transporte": False, "byte_identico": False, "error": f"{type(e).__name__}: {str(e)[:200]}",
                     "segundos": round(time.perf_counter() - t0, 2)}
        ll = [json.loads(l) for l in log.read_text(encoding="utf-8").splitlines()] if log.exists() else []
        llam = [l for l in ll if l["evento"] == "llamada"]
        fila["log_r1_integro"] = bool(llam and llam[0]["output_chars"] == len(directo)
                                      and llam[0]["output_sha256"] == sha256_bytes(directo.encode("utf-8")))
        filas.append(fila)
        print(fila)
        kg.unlink(); cfg_path.unlink()
        if not fila["ok_transporte"] or not fila["byte_identico"]:
            break
    max_ok = max([f["chars_resultado"] for f in filas if f["ok_transporte"] and f["byte_identico"]] or [0])
    res = {"generado": datetime.now().isoformat(timespec="seconds"),
           "unidad": "U-A2.0-banco — entregable 7 (tope de resultado MCP)",
           "servidor": rel_repo(SERVIDOR), "sdk_mcp": "1.29.0", "transporte": "stdio JSON-RPC, un TextContent",
           "tope_transporte": {"max_chars_verificado_byte_identico": max_ok,
                               "primer_fallo": next((f for f in filas if not (f["ok_transporte"] and f["byte_identico"])), None),
                               "nota": "el transporte MCP del banco no impuso tope en los tamaños probados; el límite práctico es memoria/tiempo"},
           "tope_claude_code_documentado": {"warning_tokens": 10000, "limite_default_tokens": 25000,
                                            "variable": "MAX_MCP_OUTPUT_TOKENS",
                                            "comportamiento": "results that exceed the default threshold are persisted to disk and replaced with a file reference in the conversation",
                                            "anotacion_no_usada": "anthropic/maxResultSizeChars (hasta 500.000 chars)",
                                            "medicion": "fase B (requiere sesión real)",
                                            "fuente": "docs/en/mcp, sección MCP output limits and warnings (copia en el paquete de revisión del freno A1)"},
           "resultados_naturales_maximos_medidos": {"mcp_kg_neo4j_limite_50": 17719, "mcp_kg_juguete_nodo_grande_gate10": 42248,
                                                    "mcp_vector_limite_50": 81275},
           "mediciones": filas}
    a.out.parent.mkdir(parents=True, exist_ok=True)
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("tope transporte verificado:", max_ok, "chars ->", rel_repo(a.out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
