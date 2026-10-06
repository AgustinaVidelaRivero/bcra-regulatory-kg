"""U-REEXT-T0, T3-bis, punto 5: registro EN MEMORIA de la vista runtime de los dos grafos r2b de la tanda 0
re-ensamblados en T3-bis, con el patrón de data/experiment/tanda0/code/comun_tanda0.py y sin editarlo: agrega las dos
claves a su tabla TANDA0 en memoria y vuelve a llamar a su registro (idempotente). Reemplaza al de T3
(data/experiment/reext_t0/t3/registro_vista_r2b.py, con los sha de los grafos de T3). Lo importa
data/experiment/neo4j/grafos.py (cargar_vista_runtime) por los campos requiere_registro_dir y requiere_registro_modulo
de las entradas KG_Tanda0_*_r2b. La vista es la de comun_tanda0.cargar_runtime_gen3; el kg.json no se toca. r2b no se
evalúa con EV2 (laudo de r2, §3.1, punto 7): esta vista sirve a la carga en Neo4j y a su verificación."""
import sys
from pathlib import Path

CODE_T0 = Path(__file__).resolve().parents[2] / "tanda0" / "code"   # data/experiment/tanda0/code
if str(CODE_T0) not in sys.path:
    sys.path.insert(0, str(CODE_T0))

import comun_tanda0 as T0   # noqa: E402  (registra la tanda 0 al importarse)

R2B = {
    "tanda0_ens_diez_r2b": {
        "path": T0.ENS_DIR / "ens_diez_r2b" / "r2" / "kg.json",
        "sha256": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
        "label": "r2b_diez_mem",
    },
    "tanda0_ens_desarrollo_r2b": {
        "path": T0.ENS_DIR / "ens_desarrollo_r2b" / "r2" / "kg.json",
        "sha256": "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2",
        "label": "r2b_desarrollo_mem",
    },
}


def registrar_r2b() -> None:
    T0.TANDA0.update(R2B)
    T0.registrar_tanda0()


registrar_r2b()
