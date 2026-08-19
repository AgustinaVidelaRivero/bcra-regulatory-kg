#!/usr/bin/env python3
"""medicion_transporte.py — Límites MEDIDOS del transporte de Claude Code.

U-A2.0-gate, entregable 1 (§5 de inventario_campos.md). Costo USD 0: solo lee
los jsonl de sesión ya existentes en el disco de la autora.

Qué mide, sobre TODOS los archivos de sesión del proyecto:
  · Bash    -> len(toolUseResult.stdout) y len del bloque tool_result que ve el
               modelo; máximo observado = cap del transporte.
  · MCP     -> len(toolUseResult[*].text) (los resultados MCP llegan como lista
               de bloques de texto con el payload crudo del server).
  · marcas de truncado en el bloque que ve el modelo.

NO persiste contenido de las sesiones: solo longitudes y conteos. El corpus de
sesiones vive fuera del repo y no se copia.

Uso (el directorio de sesiones se deriva del cwd, sin rutas absolutas en el
código: Claude Code slugifica el cwd reemplazando '/' y ' ' por '-'):

  python3 -B data/experiment/banco_mcp/gate/code/medicion_transporte.py \
      --proyecto "$HOME/.claude/projects/$(pwd | tr '/ ' '--')"
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

MARCA_TRUNCADO = re.compile(r"\[(\d+) characters truncated\]")


def medir(proyecto: Path) -> dict:
    archivos = sorted(proyecto.glob("*.jsonl"))
    bash, mcp_txt, marcas, previews = [], [], [], []
    for f in archivos:
        try:
            lineas = f.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for l in lineas:
            if '"toolUseResult"' not in l:
                continue
            try:
                d = json.loads(l)
            except json.JSONDecodeError:
                continue
            tur = d.get("toolUseResult")
            visto = ""
            for c in (d.get("message") or {}).get("content", []) or []:
                if isinstance(c, dict) and c.get("type") == "tool_result":
                    visto = c.get("content") if isinstance(c.get("content"), str) else json.dumps(
                        c.get("content"), ensure_ascii=False)
            if isinstance(tur, dict) and "stdout" in tur:
                n = len(tur.get("stdout") or "")
                bash.append(n)
                if n >= 1000:
                    previews.append((n, len(visto or "")))
            elif isinstance(tur, list):
                for b in tur:
                    if isinstance(b, dict) and b.get("type") == "text":
                        mcp_txt.append(len(b.get("text") or ""))
            for m in MARCA_TRUNCADO.finditer(visto or ""):
                marcas.append(int(m.group(1)))
    bash.sort(reverse=True); mcp_txt.sort(reverse=True)
    return {
        "n_archivos_sesion": len(archivos),
        "bash": {"n_resultados": len(bash), "max_stdout_chars": bash[0] if bash else None,
                 "top10_stdout_chars": bash[:10],
                 "n_en_el_maximo": sum(1 for x in bash if bash and x == bash[0])},
        "bash_preview_vs_stdout": {
            "n_pares_stdout_ge_1000": len(previews),
            "ejemplos_max": sorted(previews, reverse=True)[:5],
        },
        "mcp": {"n_resultados_texto": len(mcp_txt), "max_text_chars": mcp_txt[0] if mcp_txt else None,
                "top10_text_chars": mcp_txt[:10]},
        "marcas_truncado": {"n": len(marcas), "chars_truncados_min": min(marcas) if marcas else None,
                            "chars_truncados_max": max(marcas) if marcas else None},
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--proyecto", type=Path, required=True)
    ap.add_argument("--out", type=Path, default=None)
    a = ap.parse_args()
    res = medir(a.proyecto.expanduser())
    txt = json.dumps(res, ensure_ascii=False, indent=2)
    print(txt)
    if a.out:
        a.out.parent.mkdir(parents=True, exist_ok=True)
        a.out.write_text(txt + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
