"""B6.1, tanda final, T3, punto 5: envoltorio en memoria de data/experiment/tanda0/code/cargar_neo4j_tanda0.py para los dos grafos de
la tanda final (pre-registro de la tanda final, §7; es tanda1/t3/scripts/cargar_neo4j_t3f.py con las claves de la tanda final). El
cargador acepta en --grafo solo CLAVES_TANDA0, las
claves de grafos.py que empiezan con «KG_Tanda0_» (cargar_neo4j_tanda0.py:56, :122). Este envoltorio importa el cargador desde <raíz>
sin editarlo, reemplaza EN MEMORIA CLAVES_TANDA0 por exactamente las dos claves de la tanda final y llama a su main() con
--grafo <clave> --out-dir <salida>, una vez por clave (nunca «todos»): el mismo camino de código y las mismas salidas. Las salidas
heredan los rótulos de la tanda 0 (carga_neo4j_tanda0.json, «U-TANDA0-2A E3.c», «PARIDAD (tanda 0)»), que no se corrigen.
Uso (desde <raíz>): python -B cargar_neo4j_tf.py <raíz> <clave> <out-dir>
"""
import importlib.util
import sys
from pathlib import Path

CLAVES_TF = ["KG_TandaFinal_r2b", "KG_TandaFinal_r2b_sincola"]
RAIZ, CLAVE, OUT = Path(sys.argv[1]).resolve(), sys.argv[2], sys.argv[3]
if CLAVE not in CLAVES_TF:
    raise SystemExit(f"FRENO: {CLAVE} no es una de {CLAVES_TF}")
spec = importlib.util.spec_from_file_location("cargar_neo4j_tanda0", RAIZ / "data/experiment/tanda0/code/cargar_neo4j_tanda0.py")
CN = importlib.util.module_from_spec(spec)
sys.modules["cargar_neo4j_tanda0"] = CN
spec.loader.exec_module(CN)
assert Path(CN.G.__file__).resolve().is_relative_to(RAIZ) and all(k in CN.G.GRAFOS for k in CLAVES_TF)
CN.CLAVES_TANDA0 = list(CLAVES_TF)
sys.argv = ["cargar_neo4j_tanda0.py", "--grafo", CLAVE, "--out-dir", OUT]
sys.exit(CN.main())
