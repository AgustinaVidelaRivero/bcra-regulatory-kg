"""
reproducir_p1.py — U-PROMPT-R2, P1 (USD 0): reproduce los artefactos de P1
que salen del crudo guardado de la tanda 0, en este orden:
  1. tool schema de borrador con las decisiones 15 a 17 (espejo fuera del repo);
  2. borrador del prefijo r2, variantes A y B de la decisión 20;
  3. control de no-filtración de cada variante y del texto fijo del mensaje;
  4. censo de P1.c y P1.d (el mensaje y la NOTA de E3 sobre la E0 e0-r2, f8dedd4);
  5. ejemplos del mensaje nuevo y la sección «lado a lado» del diseño;
  6. huellas de los borradores (sha256 del texto, hash canónico y namespace);
  7. la unidad del encabezado de una lista, E3 y los encabezados en línea de título (§4.5 y §10, punto 18);
  8. los valores de `frecuencia` fuera de la lista en el grafo r2a (§9).
Escribe solo en data/experiment/prompt_r2/p1/salida/ y en el espejo, que debe
estar fuera del repo. Ninguna llamada a la API.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/reproducir_p1.py --espejo <dir fuera del repo>
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import subprocess
import sys
from pathlib import Path

P1 = Path(__file__).resolve().parent
REPO = P1.parents[3]
SAL = P1 / "salida"


def correr(*args: str) -> None:
    subprocess.run([sys.executable, "-B", *args], check=True, cwd=REPO,
                   env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})


def literales_mensaje() -> str:
    """Texto fijo del mensaje y de la NOTA de borrador: las constantes de
    p1/mensaje_r2_borrador.py de más de 20 caracteres que no son docstrings,
    para el control de no-filtración."""
    arbol = ast.parse((P1 / "mensaje_r2_borrador.py").read_text(encoding="utf-8"))
    docs = {id(n.body[0].value) for n in ast.walk(arbol)
            if isinstance(n, (ast.Module, ast.FunctionDef)) and n.body and isinstance(n.body[0], ast.Expr)
            and isinstance(n.body[0].value, ast.Constant)}
    return "\n".join(n.value for n in ast.walk(arbol) if isinstance(n, ast.Constant) and isinstance(n.value, str)
                     and len(n.value) > 20 and id(n) not in docs)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--espejo", required=True)
    a = ap.parse_args()
    SAL.mkdir(parents=True, exist_ok=True)
    correr(str(P1 / "espejo_tool_schema.py"), "--espejo", a.espejo, "--salida", str(SAL))
    for v in ("A", "B"):
        correr(str(P1 / "borrador_prefijo_r2.py"), "--repo", str(REPO), "--variante", v, "--salida", str(SAL))
        correr(str(P1 / "nofiltracion.py"), str(REPO), str(SAL / f"prefijo_r2_borrador_{v}.txt"),
               str(SAL / f"nofiltracion_{v}.json"))
    (SAL / "literales_mensaje_r2.txt").write_text(literales_mensaje(), encoding="utf-8")
    correr(str(P1 / "nofiltracion.py"), str(REPO), str(SAL / "literales_mensaje_r2.txt"),
           str(SAL / "nofiltracion_mensaje.json"))
    correr(str(P1 / "censo_p1.py"), str(REPO), str(SAL), str(SAL / "censo_p1.json"))
    correr(str(P1 / "ejemplos_mensaje_r2.py"))
    correr(str(P1 / "lado_a_lado.py"))
    correr(str(P1 / "hashes_borrador.py"))
    correr(str(P1 / "encabezados_lista.py"), str(REPO))
    correr(str(P1 / "frecuencia_r2a.py"))
    for p in sorted(SAL.rglob("*")):
        if p.is_file():
            print(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(REPO)}")


if __name__ == "__main__":
    main()
