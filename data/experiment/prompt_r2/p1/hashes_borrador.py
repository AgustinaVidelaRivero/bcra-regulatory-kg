"""
hashes_borrador.py — U-PROMPT-R2, P1 (USD 0): huellas de los borradores del
prefijo r2, con el mismo método que la cadena sellada:
  - sha256 del texto del system (como PREFIJO_SHA256_V3 en prompt_v3_b54.py);
  - hash canónico system + tools, 12 caracteres (como PREFIJO_HASH en
    prompt_e1.py:415-419 y PREFIJO_HASH_V3 en prompt_v3_b54.py:516-520): JSON
    de {"system": [bloque con cache_control], "tools": [tool schema]} con
    sort_keys, ensure_ascii=False y separadores compactos;
  - namespace de caché de E1 que tendría (cliente_e1.namespace_e1).
Control: el mismo cálculo sobre el sellado v3_b54 tiene que dar 35e88c2d… y
54a111e2175f; si no, frena.

Son provisionales: cambian con cada ajuste del borrador hasta que P2 congele el
texto. Escribe data/experiment/prompt_r2/p1/salida/hashes_borrador.json.

Uso (desde la raíz del repo, después de reproducir_p1.py):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/hashes_borrador.py
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

P1 = Path(__file__).resolve().parent
REPO = P1.parents[3]
SAL = P1 / "salida"
for p in ("data/experiment/b54_catalogo_v3/code", "data/experiment/esq/code",
          "data/experiment/reextraccion_v2/e1_extractor"):
    sys.path.insert(0, str(REPO / p))
import cliente_e1  # noqa: E402
import prompt_v3_b54 as v3  # noqa: E402


def huellas(texto: str, tool_schema: dict) -> dict:
    canon = json.dumps({"system": [{"type": "text", "text": texto, "cache_control": {"type": "ephemeral"}}],
                        "tools": [tool_schema]}, sort_keys=True, ensure_ascii=False, separators=(",", ":"))
    h = hashlib.sha256(canon.encode("utf-8")).hexdigest()[:12]
    return {"caracteres_system": len(texto), "sha256_texto": hashlib.sha256(texto.encode("utf-8")).hexdigest(),
            "hash_canonico": h, "namespace_e1": cliente_e1.namespace_e1(prefijo_hash=h)}


def main() -> None:
    sellado = huellas(v3.PREFIJO_SISTEMA_V3, v3.TOOL_SCHEMA_V3)
    if (sellado["sha256_texto"] != "35e88c2dd0a2920302c29005b08ab9689405606d4bd5fcf8fb7ce807b1a3c512"
            or sellado["hash_canonico"] != "54a111e2175f"):
        raise SystemExit(f"el método no reproduce el sello v3_b54: {sellado}")
    ts_path = SAL / "generados_d15_17" / "tool_schema_r2.json"
    ts = json.loads(ts_path.read_text(encoding="utf-8"))
    out = {"metodo": "prompt_e1.py:415-419 y prompt_v3_b54.py:516-520", "control_sellado_v3_b54": sellado,
           "tool_schema": {"ruta": str(ts_path.relative_to(REPO)),
                           "sha256": hashlib.sha256(ts_path.read_bytes()).hexdigest()}}
    for v in ("A", "B"):
        out[f"borrador_{v}"] = huellas((SAL / f"prefijo_r2_borrador_{v}.txt").read_text(encoding="utf-8"), ts)
    (SAL / "hashes_borrador.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k in ("borrador_A", "borrador_B"):
        print(k, out[k]["hash_canonico"], out[k]["sha256_texto"][:16])


if __name__ == "__main__":
    main()
