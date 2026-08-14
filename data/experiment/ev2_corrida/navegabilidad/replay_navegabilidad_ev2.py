"""replay_navegabilidad_ev2.py — Driver de la unidad de navegabilidad EV2.

Invoca (SIN editar) code/metrica_ev2.py sobre las trazas de navegabilidad de
los tres labels de la corrida base (bb89a8e), con el replay fuerte activado
(igualdad exacta contra steps_full). Determinístico, $0, cero llamadas a API.

Las trazas del eje de fidelidad (EV2F-*) están fuera del alcance de esta
unidad y NO se abren: el filtrado es por NOMBRE de archivo (prefijo EV2F- y
resumen_), armando un directorio de symlinks solo-navegabilidad que se pasa
como trazas_dir a evaluar_label (parámetro ya existente de la función).

Salidas (todas dentro de navegabilidad/):
  - trazas_nav/<label>/          symlinks a las trazas de navegabilidad
  - resultados_navegabilidad_<label>.json   detalle por caso + por ancla
"""

import sys
from pathlib import Path

NAV_DIR = Path(__file__).resolve().parent           # ev2_corrida/navegabilidad
EV2_DIR = NAV_DIR.parent
sys.path.insert(0, str(EV2_DIR / "code"))

from comun_ev2 import GRAFOS, verificar_grafos      # noqa: E402
from metrica_ev2 import evaluar_label               # noqa: E402


def preparar_trazas_nav(label: str) -> tuple[Path, int]:
    """Symlinks a las trazas de navegabilidad del label, filtradas por nombre
    de archivo (EV2F-* y resumen_* excluidas sin abrirlas)."""
    src = EV2_DIR / "trazas" / label
    dst = NAV_DIR / "trazas_nav" / label
    dst.mkdir(parents=True, exist_ok=True)
    n = 0
    for p in sorted(src.glob("*.json")):
        if p.name.startswith("EV2F-") or p.name.startswith("resumen_"):
            continue
        link = dst / p.name
        if link.is_symlink() or link.exists():
            link.unlink()
        link.symlink_to(p)
        n += 1
    return dst, n


def main() -> int:
    print("verificación sha256 de los tres grafos (comun_ev2.verificar_grafos):")
    verificar_grafos()
    for grafo, g in GRAFOS.items():
        label = g["label"]
        trazas_dir, n = preparar_trazas_nav(label)
        print(f"\n{label} ({grafo}): {n} trazas de navegabilidad enlazadas "
              "(EV2F-*/resumen_* excluidas por nombre, sin abrirlas)")
        out = NAV_DIR / f"resultados_navegabilidad_{label}.json"
        agg = evaluar_label(label, grafo, trazas_dir=trazas_dir, out_path=out)
        print(f"  casos evaluados: {agg['n_casos_evaluados']}"
              f"  replay_ok_todos={agg['replay_ok_todos']}"
              f"  replay_fuerte_ok_todos={agg['replay_fuerte_ok_todos']}")
        for r in agg["resultados"]:
            if not (r["replay_ok"] and r["replay_fuerte_ok"]):
                print(f"  DIVERGENCIA replay: {r['caso_id']}"
                      f" replay_ok={r['replay_ok']}"
                      f" replay_fuerte_ok={r['replay_fuerte_ok']}"
                      f" fallas={r['replay_fallas']}"
                      f" fallas_fuerte={r['replay_fuerte_fallas']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
