"""
c0c_sellos.py — U-COMP-E1, etapa C0, punto (c). USD 0, sin API.

Sella con sha256, tamaño y hora (UTC y local), antes de toda llamada paga, los insumos que el mandato
(docs/mandatos/UCOMP_E1_comparacion_chica_modelo.md, firmado en cbcb823, etapa C0 (c)) manda sellar:
  - la lista de unidades (comp_e1/unidades.json, donde la manda el mandato) y el intento 0 de Haiku de las 87
    (c0/salida/intento0_haiku.jsonl), de C0 (a), más c0/salida/claves_c0.json;
  - las fichas de T4 que se usan de base (fichas_punto7_grupo_c.json/.md, fichas_punto8_omisiones.json/.md), la
    adjudicación de la autora (t4/adjudicacion_autora.json) y las tasas (tasas_t4.json), de U-REEXT-T0;
  - el texto del criterio (criterio_c0.md) y el de las reglas de lectura (reglas_lectura_c0.md), extraídos verbatim del
    mandato en su commit de firma;
  - el mandato tal como está en el repo (que debe dar el sha256 del commit de la firma).
Control cruzado: el sha256 de cada ficha de T4 contra el que tasas_t4.json dejó sellado (clave fichas_sha256).
Escribe sellos_c0.json y sellos_c0.txt en --salida. Ninguna ruta absoluta en las salidas.

  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c0/c0c_sellos.py --salida data/experiment/comp_e1/c0/salida --head <sha de HEAD>
"""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
T4 = REPO / "data" / "experiment" / "reext_t0" / "t4"
MANDATO = REPO / "docs" / "mandatos" / "UCOMP_E1_comparacion_chica_modelo.md"
MANDATO_SHA256_FIRMA = "89ce5508c574c4bc09f669df01468aeab1712af5651231eda16f63bc2d26d012"   # git show cbcb823:<ruta> | shasum -a 256


def sha(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--head", type=str, required=True)
    a = ap.parse_args()
    utc = datetime.now(timezone.utc)
    local = utc.astimezone()
    grupos = {
        "c0_a": [AQUI.parent / "unidades.json", a.salida / "intento0_haiku.jsonl", a.salida / "claves_c0.json"],
        "fichas_t4": [T4 / "salida" / "fichas_punto7_grupo_c.json", T4 / "salida" / "fichas_punto7_grupo_c.md",
                      T4 / "salida" / "fichas_punto8_omisiones.json", T4 / "salida" / "fichas_punto8_omisiones.md",
                      T4 / "adjudicacion_autora.json", T4 / "salida" / "tasas_t4.json"],
        "criterio_y_reglas": [AQUI / "criterio_c0.md", AQUI / "reglas_lectura_c0.md"],
        "mandato": [MANDATO],
    }
    sellos = {"unidad": "U-COMP-E1", "etapa": "C0 (c)", "hora_utc": utc.isoformat(timespec="seconds"),
              "hora_local": local.isoformat(timespec="seconds"), "head": a.head,
              "mandato_commit_firma": "cbcb823", "mandato_sha256_en_la_firma": MANDATO_SHA256_FIRMA, "archivos": []}
    for g, ps in grupos.items():
        for p in ps:
            if not p.exists():
                raise SystemExit(f"falta {p}")
            ruta = str(p.relative_to(REPO)) if p.is_relative_to(REPO) else f"<salida>/{p.name}"
            sellos["archivos"].append({"grupo": g, "ruta": ruta, "sha256": sha(p), "bytes": p.stat().st_size})
    tasas = json.loads((T4 / "salida" / "tasas_t4.json").read_text(encoding="utf-8"))
    cruz = {}
    for nombre, esperado in tasas["fichas_sha256"].items():
        p = T4 / "salida" / nombre
        cruz[nombre] = {"sha256_en_tasas_t4": esperado, "sha256_ahora": sha(p) if p.exists() else None,
                        "coincide": p.exists() and sha(p) == esperado}
    sellos["control_cruzado_fichas_vs_tasas_t4"] = cruz
    sellos["adjudicacion_sha256_en_tasas_t4"] = tasas.get("adjudicacion_sha256")
    sellos["adjudicacion_sha256_ahora"] = sha(T4 / "adjudicacion_autora.json")
    sellos["adjudicacion_coincide"] = sellos["adjudicacion_sha256_ahora"] == tasas.get("adjudicacion_sha256")
    sellos["mandato_coincide_con_la_firma"] = sha(MANDATO) == MANDATO_SHA256_FIRMA
    (a.salida / "sellos_c0.json").write_text(json.dumps(sellos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    lineas = [f"SELLOS C0 — U-COMP-E1 — {sellos['hora_utc']} (UTC) / {sellos['hora_local']} (local) — HEAD {a.head}",
              f"mandato: commit de la firma cbcb823, sha256 {MANDATO_SHA256_FIRMA}; el archivo actual coincide: {sellos['mandato_coincide_con_la_firma']}"]
    for x in sellos["archivos"]:
        lineas.append(f"{x['sha256']}  {x['bytes']:>9d}  [{x['grupo']}] {x['ruta']}")
    lineas.append("control cruzado contra tasas_t4.json.fichas_sha256: " + ", ".join(f"{k}={v['coincide']}" for k, v in cruz.items())
                  + f"; adjudicacion_autora.json={sellos['adjudicacion_coincide']}")
    (a.salida / "sellos_c0.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
    print("\n".join(lineas))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
