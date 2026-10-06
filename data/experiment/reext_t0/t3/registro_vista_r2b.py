"""U-REEXT-T0, T3, punto 4: registro EN MEMORIA de la vista runtime de los dos grafos r2b de la tanda 0, con el patrón
de data/experiment/tanda0/code/comun_tanda0.py y sin editarlo: agrega las dos claves a su tabla TANDA0 en memoria y
vuelve a llamar a su registro (idempotente). Lo importa data/experiment/neo4j/grafos.py (cargar_vista_runtime) por los
campos requiere_registro_dir y requiere_registro_modulo de las entradas KG_Tanda0_*_r2b. La vista es la de
comun_tanda0.cargar_runtime_gen3 (provenance primaria mapeada a {source_doc, location}); el kg.json no se toca.
r2b no se evalúa con EV2 (laudo de r2, §3.1, punto 7): esta vista sirve a la carga en Neo4j y a su verificación."""
import sys
from pathlib import Path

CODE_T0 = Path(__file__).resolve().parents[2] / "tanda0" / "code"   # data/experiment/tanda0/code
if str(CODE_T0) not in sys.path:
    sys.path.insert(0, str(CODE_T0))

import comun_tanda0 as T0   # noqa: E402  (registra la tanda 0 al importarse)

R2B = {
    "tanda0_ens_diez_r2b": {
        "path": T0.ENS_DIR / "ens_diez_r2b" / "r2" / "kg.json",
        "sha256": "12c5cfc3ea4c46536c72b6eafdb6c890c626b550f76dd96c50a579156975e055",
        "label": "r2b_diez_mem",
    },
    "tanda0_ens_desarrollo_r2b": {
        "path": T0.ENS_DIR / "ens_desarrollo_r2b" / "r2" / "kg.json",
        "sha256": "6de41495105736330a11e8f19d3625f57987938570e4bcf84aa623bea5a952f0",
        "label": "r2b_desarrollo_mem",
    },
}


def registrar_r2b() -> None:
    T0.TANDA0.update(R2B)
    T0.registrar_tanda0()


registrar_r2b()
