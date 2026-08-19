#!/usr/bin/env python3
"""faseB_runner.py — Corridas reales de la FASE B con `claude -p` (U-A2.0-gate).

Corre UNA sesión no interactiva por caso, con el modelo y el tope declarados en
`gate/faseB_predeclaracion.md`, y persiste la salida `--output-format json` de
cada sesión (la fuente de contabilidad: `total_cost_usd`, `session_id`,
`modelUsage`).

Guardas implementadas, no prometidas:
  · tope por sesión aplicado por el propio CLI (`--max-budget-usd`);
  · tope ACUMULADO: antes de lanzar cada sesión suma lo gastado y frena si la
    proyección de una sesión más superaría el tope. El freno es del runner, no
    del operador.
  · aislamiento por capacidad: `--tools Bash` + `--allowedTools "Bash(python3 *)"`
    (el agente no tiene ninguna otra tool);
  · cwd limpio FUERA del repo: el agente no hereda el CLAUDE.md del proyecto.

NO re-corre casos: si el archivo de salida de un caso ya existe, lo saltea. Un
caso que salió mal se reporta como salió (el mandato prohíbe re-correr para
"mejorar" un caso).

Uso:
  faseB_runner.py --casos GATE-01,GATE-02 --cwd <dir limpio> --out <dir>
                  [--tope-acumulado 1.50] [--max-budget-usd 0.15]
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime
from pathlib import Path

GATE_DIR = Path(__file__).resolve().parents[1]
TOOLS = GATE_DIR / "code" / "tools_juguete.py"

MODELO = "claude-sonnet-5"          # declarado en faseB_predeclaracion.md §1
MAX_TOOL_CALLS = 8                  # declarado en §2

PREGUNTAS = {
    "GATE-01": ("v1", "Que establece el punto 9.9 del texto ordenado de exterior y cambios? "
                      "Si no existe, decilo."),
    "GATE-02": ("v1", "Que obligacion fija el punto 3.3 del texto ordenado de exterior y cambios?"),
    "GATE-03": ("v1", "Que limite temporal se aplica a la operacion epsilon de acreditacion?"),
    "GATE-04": ("v1", "Que exige el procedimiento eta de acreditacion complementaria?"),
    "GATE-05": ("v1", "Sobre que sujeto recae la obligacion alfa de acreditacion de fondos, "
                      "y en que punto esta anclada?"),
    "GATE-06": ("v1", "A que obligacion aplica la operacion epsilon puente de acreditacion?"),
    "GATE-07": ("v1", "Que designa el prefijo 'ext' en un ancla de la forma ext:6.11? "
                      "Respondé solo si podés justificarlo."),
    "GATE-08": ("v1", "Que requisitos de capital minimo fija este texto ordenado?"),
    "GATE-10": ("v1", "Que contiene la obligacion delta de registro extenso?"),
    "GATE-11": ("v2", "A que obligacion aplica la operacion epsilon puente de acreditacion?"),
}

PLANTILLA = """Sos un agente que responde preguntas sobre un grafo de conocimiento regulatorio SINTETICO (contenido inventado, no es normativa real).

Tenes exactamente tres tools sobre el grafo. Se invocan con Bash, UNA invocacion por comando, sin pipes ni encadenamientos:

  python3 -B "{tools}" {contrato}--caso {caso} buscar_nodos --consulta "palabras clave" --limite 10
  python3 -B "{tools}" {contrato}--caso {caso} ver_nodo --id ID_EXACTO
  python3 -B "{tools}" {contrato}--caso {caso} ver_vecinos --id ID_EXACTO {vecinos}

Reglas duras:
- Pasa SIEMPRE --caso {caso} en cada invocacion.
- Un comando = una sola invocacion. Nada de pipes, redirecciones ni &&.
- Tope de {tope} llamadas a tools en esta sesion. Si lo alcanzas, responde con lo que tengas.
- No tenes acceso a ningun otro archivo ni herramienta.
- Si concluis que no podes responder con las tools disponibles, responde igual y marca respondible en false.

Pregunta: {pregunta}

Terminada la navegacion, tu ultimo mensaje debe ser UNICAMENTE un bloque JSON con esta forma exacta:
{{"respuesta": "...", "citas": ["ext:6.11"], "respondible": true}}
"""


def prompt_de(caso: str) -> str:
    contrato, pregunta = PREGUNTAS[caso]
    return PLANTILLA.format(
        tools=TOOLS, caso=caso, pregunta=pregunta, tope=MAX_TOOL_CALLS,
        contrato="--contrato v2 " if contrato == "v2" else "",
        vecinos="--pagina 1 --por-pagina 40" if contrato == "v2" else "--direccion ambas")


def gastado(out_dir: Path) -> float:
    total = 0.0
    for p in sorted(out_dir.glob("*.json")):
        try:
            total += float(json.loads(p.read_text(encoding="utf-8")).get("total_cost_usd") or 0.0)
        except (json.JSONDecodeError, ValueError):
            continue
    return total


def correr(caso: str, cwd: Path, out_dir: Path, max_budget: float) -> dict:
    destino = out_dir / f"run_{caso}.json"
    prompt_path = out_dir / f"prompt_{caso}.txt"
    prompt_path.write_text(prompt_de(caso), encoding="utf-8")
    cmd = ["claude", "-p", prompt_de(caso), "--model", MODELO, "--output-format", "json",
           "--tools", "Bash", "--allowedTools", "Bash(python3 *)",
           "--max-budget-usd", str(max_budget), "--safe-mode"]
    r = subprocess.run(cmd, cwd=str(cwd), capture_output=True, text=True, stdin=subprocess.DEVNULL)
    salida = r.stdout
    # el CLI puede anteponer avisos a la línea JSON: se conserva el crudo íntegro
    (out_dir / f"raw_{caso}.txt").write_text(salida + "\n--- stderr ---\n" + r.stderr, encoding="utf-8")
    i = salida.find("{")
    if i < 0:
        raise SystemExit(f"{caso}: la salida no trae JSON. Ver raw_{caso}.txt. FRENAR.")
    d = json.loads(salida[i:])
    d["_gate"] = {"caso": caso, "modelo_declarado": MODELO, "max_tool_calls_declarado": MAX_TOOL_CALLS,
                  "cwd": str(cwd), "corrido": datetime.now().isoformat(timespec="seconds"),
                  "comando": cmd[:2] + ["<prompt>"] + cmd[3:]}
    destino.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return d


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--casos", required=True)
    ap.add_argument("--cwd", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--tope-acumulado", dest="tope", type=float, default=1.50)
    ap.add_argument("--max-budget-usd", dest="max_budget", type=float, default=0.15)
    a = ap.parse_args()
    a.out.mkdir(parents=True, exist_ok=True)

    for caso in a.casos.split(","):
        caso = caso.strip()
        if caso not in PREGUNTAS:
            raise SystemExit(f"caso desconocido: {caso}")
        if (a.out / f"run_{caso}.json").exists():
            print(f"{caso}: ya corrido, se saltea (no se re-corre)"); continue
        ya = gastado(a.out)
        if ya + a.max_budget > a.tope:
            print(f"FRENO: gastado {ya:.4f} + tope de sesion {a.max_budget} superaria "
                  f"el tope acumulado {a.tope}. No se lanza {caso}.")
            return 2
        d = correr(caso, a.cwd, a.out, a.max_budget)
        mu = d.get("modelUsage", {})
        print(f"{caso}: turns={d.get('num_turns')} is_error={d.get('is_error')} "
              f"costo={d.get('total_cost_usd'):.4f} acumulado={gastado(a.out):.4f} "
              f"modelos={sorted(mu)} denials={len(d.get('permission_denials') or [])}")
    print(f"gasto acumulado total: USD {gastado(a.out):.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
