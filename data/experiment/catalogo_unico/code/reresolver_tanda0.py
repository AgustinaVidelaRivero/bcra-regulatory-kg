"""
reresolver_tanda0.py — U-CAT-UNICO C2.d: re-resolución contrafáctica, en
código y a USD 0, de los sujetos propuestos guardados de la tanda 0 (grupo
diez: data/experiment/reextraccion_v2/corpus_tanda0/ens_diez/r1/
e4_propuestos.json, 34 propuestos, 30 en cuarentena; U-LISTAS-NOMAP N1,
clave `propuestos_e4`).

Cada propuesto se resuelve con r1_e4.resolver_label (importado, no copiado)
contra el índice de E4 de la entrada generada del catálogo v3 y del r2
(generados_<v>/entrada_esqueleto_<v>.json). Control: con el v3 se reproduce
la tabla guardada fila a fila (si no, se frena). Cuenta cuántos resuelven con
r2 y no con v3. Es un dato, no una meta (L-ESQ-R2 §4.3). No escribe archivos.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/catalogo_unico/code/reresolver_tanda0.py
"""

from __future__ import annotations

import sys

sys.dont_write_bytecode = True

import json  # noqa: E402
from pathlib import Path  # noqa: E402

AQUI = Path(__file__).resolve().parent
CATALOGO_UNICO = AQUI.parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for _p in (REX, REX / "corpus_v2", REPO / "data" / "experiment" / "grafo_v2" / "code", REX / "e2_reduce"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import r1_e4  # noqa: E402 — resolver_label :97, indice_catalogo :74

PROPUESTOS_DIEZ = REX / "corpus_tanda0" / "ens_diez" / "r1" / "e4_propuestos.json"
ENTRADA = {v: CATALOGO_UNICO / f"generados_{v}" / f"entrada_esqueleto_{v}.json" for v in ("v3", "r2")}


class FrenoReresolucion(RuntimeError):
    """El control de reproducción no se cumple: se frena."""


def reresolver() -> dict:
    filas = json.loads(PROPUESTOS_DIEZ.read_text(encoding="utf-8"))
    idx = {v: r1_e4.indice_catalogo(json.loads(p.read_text(encoding="utf-8"))) for v, p in ENTRADA.items()}
    detalle = []
    for f in filas:
        res = {v: r1_e4.resolver_label(f["label"], f.get("padre_sugerido"), idx[v]) for v in idx}
        if res["v3"][0] != f.get("resuelto_a"):
            raise FrenoReresolucion(f"el v3 no reproduce la fila guardada {f['id_propuesto']}")
        detalle.append({"label": f["label"], "padre_sugerido": f.get("padre_sugerido"),
                        "guardado": f["estado"], "v3": res["v3"][0], "motivo_v3": res["v3"][1],
                        "r2": res["r2"][0], "motivo_r2": res["r2"][1]})
    return {
        "propuestos": len(filas),
        "guardado_resueltos": sum(1 for f in filas if f["estado"] == "resuelto"),
        "guardado_cuarentena": sum(1 for f in filas if f["estado"] == "cuarentena"),
        "resuelven_v3": sum(1 for d in detalle if d["v3"]),
        "resuelven_r2": sum(1 for d in detalle if d["r2"]),
        "r2_y_no_v3": [d for d in detalle if d["r2"] and not d["v3"]],
        "v3_y_no_r2": [d for d in detalle if d["v3"] and not d["r2"]],
        "cambian_de_destino": [d for d in detalle if d["v3"] and d["r2"] and d["v3"] != d["r2"]],
    }


def main() -> int:
    r = reresolver()
    print(f"tanda 0, diez ({PROPUESTOS_DIEZ.relative_to(REPO)}): {r['propuestos']} propuestos, guardado "
          f"{r['guardado_resueltos']} resueltos / {r['guardado_cuarentena']} en cuarentena")
    print(f"resuelven con v3: {r['resuelven_v3']} (reproduce la tabla guardada fila a fila); con r2: {r['resuelven_r2']}")
    print(f"resuelven con r2 y no con v3: {len(r['r2_y_no_v3'])}")
    for d in r["r2_y_no_v3"]:
        print(f"  «{d['label']}» (padre sugerido {d['padre_sugerido']}) → {d['r2']} [{d['motivo_r2']}]")
    print(f"resuelven con v3 y no con r2: {len(r['v3_y_no_r2'])}; cambian de destino: {len(r['cambian_de_destino'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
