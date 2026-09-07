"""
reconstruir_tabla_f1.py — U-ESQ-V3: RECONSTRUCCIÓN de tabla_to_rol_post_f1.md.

Por qué existe. El laudo B5.4 fase 1 (FIRMADO 05/09/2026) cita esa tabla como
«la guarda del mapeo» de los 66 TOs, y el artefacto **no está en el
repositorio ni en su historia** (verificado en el §5 del diseño del hueco):
vivió solo en el paquete de revisión de aquella sesión. Un laudo firmado no
puede citar como guarda un artefacto que no existe, y esta unidad la necesita
como insumo directo — los miembros del rol se adjudican sobre esos mismos
pasajes.

Cómo se reconstruye. Se ejecuta el generador ORIGINAL de aquella sesión
(`gen_tabla_to_rol_f1.py`, versionado al lado de este archivo sin una sola
edición, sha256 3ce38f2d8cb7ab5db8ec95a708fa9701de2e90be758be393a30b3fd497def158),
redirigiendo solo su directorio de salida. No se reescribe su TABLA ni su
render: la tabla que sale es la que el laudo cita, no una versión mejorada.
Sus dos asserts corren y son la verificación de que la reconstrucción es
fiel — las 68 filas tienen que coincidir exactamente con los 68 TOs
`digerible` de `veredictos_generalizacion.json`.

Qué se le AGREGA. Solo una nota de reconstrucción al tope del .md, fuera del
cuerpo generado, con dos cosas que el lector necesita para no confundirse:
(1) que este archivo reconstruye un artefacto citado por un laudo firmado, y
(2) que su recuento 35 clase / 31 rol es el de F1 y quedó SUPERADO por el
mini-laudo del freno 2, que movió snp_cec de rol a clase (30 rol / 36 clase),
que es el estado que el catálogo v3 sellado materializa.

Uso:  python3 reconstruir_tabla_f1.py [--out DIR]
Escribe: tabla_to_rol_post_f1.md (+ los dos subproductos del generador
original: medicion_deltas_rol_f1.json y bloque_borrador_roles_A1_f1.txt).
"""

from __future__ import annotations

import argparse
import os
import runpy
from pathlib import Path

import comun_v3m as C

CODE = Path(__file__).resolve().parent
GEN = CODE / "gen_tabla_to_rol_f1.py"
SHA_GEN_ESPERADO = "3ce38f2d8cb7ab5db8ec95a708fa9701de2e90be758be393a30b3fd497def158"

NOTA = """> **NOTA DE RECONSTRUCCIÓN (U-ESQ-V3).** Este archivo **reconstruye** el
> artefacto que el laudo B5.4 fase 1 (FIRMADO 05/09/2026) cita como «la guarda
> del mapeo» y que no estaba en el repositorio ni en su historia: vivió solo en
> el paquete de revisión de aquella sesión. Se regeneró ejecutando el generador
> original de esa sesión sin editarlo (`gen_tabla_to_rol_f1.py`, versionado al
> lado, sha256 `{sha}`), de modo que el contenido es el que el laudo cita y no
> una versión mejorada. Comando:
> `python3 code/reconstruir_tabla_f1.py` desde `data/experiment/esq_v3_miembros/`.
>
> **Su recuento está SUPERADO y se conserva tal cual a propósito.** La tabla
> dice 35 clase / 31 rol porque es el estado de la fase 1. El mini-laudo del
> freno 2 (05/09/2026) movió `snp_cec` de rol a clase —con la CEC ya en el
> catálogo, su alcance ES clase exacta y el rol duplicaba a la clase—, con lo
> que el estado vigente, el que el catálogo v3 sellado materializa, es
> **30 rol / 36 clase / 2 huecos = 68**. La corrección de `docs/plan_tesis.md`
> a esos números ya fue aplicada por la instancia del plan.

"""


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=C.UNIDAD)
    args = ap.parse_args()
    out = args.out.resolve()

    import hashlib
    sha = hashlib.sha256(GEN.read_bytes()).hexdigest()
    if sha != SHA_GEN_ESPERADO:
        raise RuntimeError(
            f"el generador del freno 1 no es el original (sha {sha[:12]}…, "
            f"esperado {SHA_GEN_ESPERADO[:12]}…) — se frena")

    # El generador resuelve OUT como el directorio de su propio archivo y REPO
    # desde la variable de entorno BCRA_KG_REPO. Se ejecuta desde una copia
    # colocada en el destino, para no editarlo ni tocar su lógica.
    os.environ["BCRA_KG_REPO"] = str(C.REPO)
    tmp = out / "_gen_tabla_to_rol_f1_run.py"
    tmp.write_bytes(GEN.read_bytes())
    try:
        runpy.run_path(str(tmp), run_name="__main__")
    finally:
        tmp.unlink()

    md = out / "tabla_to_rol_post_f1.md"
    md.write_text(NOTA.format(sha=SHA_GEN_ESPERADO) + md.read_text(encoding="utf-8"),
                  encoding="utf-8")
    print(f"-> {md}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
