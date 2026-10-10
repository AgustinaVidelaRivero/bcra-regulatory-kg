"""Corre el caso (ii) de scripts/selftest_gate6.py desde la raíz de una COPIA sin .venv: el intérprete del caso
(selftest_gate6.VENV_PY) se redirige en memoria al que se pasa, sin crear enlaces. Uso: python gate6_ii_en_copia.py <python>"""
import sys
from pathlib import Path
py = Path(sys.argv[1])
raiz = Path.cwd().resolve()
assert not (raiz / ".git").exists()
sys.path.insert(0, str(raiz / "scripts"))
import selftest_gate6 as G  # noqa: E402
assert Path(G.__file__).resolve().is_relative_to(raiz)
G.VENV_PY = py
sys.argv = ["selftest_gate6.py", "--solo", "ii"]
sys.exit(G.main())
