"""P3b-2, control de la unión de operaciones: corre ensamblar_tanda0.py con la Operacion unida por punto (la regla
de la fase r2b) sobre la entrada r2a, sin cambiar nada más: se parchea solo entity_slug_r2. Corre desde la raíz de
una COPIA del repo (regla l). Uso: <python> forzar_operacion_r2b.py <args de ensamblar_tanda0.py>"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path.cwd() / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ET  # noqa: E402
import e2_lib  # noqa: E402

_orig = e2_lib.entity_slug_r2
e2_lib.entity_slug_r2 = lambda e, prov, fase="r2a": _orig(e, prov, "r2b")
sys.argv = ["ensamblar_tanda0.py", *sys.argv[1:]]
sys.exit(ET.main())
