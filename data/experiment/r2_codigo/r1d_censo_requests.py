"""U-R2-CODIGO, R1.d — censo de los requests de E1 que cambian con la E0 e0-r2.

Arma, sin llamar a la API, el request de E1 de cada unidad de la tanda 0 con
el código del pipeline (perfil `v3_b54`, el de la tanda 0) sobre la E0
legada sellada y sobre una E0 e0-r2, y calcula su clave de caché. Reutiliza
`Armado` y `claves_db` de data/experiment/mantenimiento/code/
selftest_clave_cache.py (U-MANT, commit e18d616), sin editarlo. Por unidad:
  - si la clave cambia;
  - por qué: texto propio, herencia o flags (la clave de la unidad e0-r2 con
    los flags legados se compara con la de la unidad e0-r2);
  - anclaje: la clave legada está en la caché de E1 y la e0-r2 no (miss
    proyectado). La db se abre en solo lectura (`mode=ro&immutable=1`).
Costo estimado: unidades que cambian × USD 0,0166 por unidad con E1, E3 y
reintentos (laudo de la release r2, §1.3; tarifa de la corrida de E2 de la
tanda 0, USD 40,3495 / 2.434 unidades).
Declaración: U-REEXT-T0 re-extrae la tanda 0 completa con el prefijo nuevo
de E1 (plan, B2.11, unidad 11); este censo mide la parte atribuible a las
tablas con el prefijo de la tanda 0, no el tope de esa unidad.
USD 0, sin LLM, sin red.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1d_censo_requests.py --e0-r2 <salida e0-r2> --out <json>
"""

from __future__ import annotations

import argparse
import collections
import copy
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
E0_LEGADA = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0"
MANT = REPO / "data" / "experiment" / "mantenimiento" / "code"
sys.path.insert(0, str(MANT))
import selftest_clave_cache as SCC  # noqa: E402

TARIFA_USD_POR_UNIDAD = 0.0166
DECLARACION = ("U-REEXT-T0 re-extrae la tanda 0 completa con el prefijo nuevo de E1 "
               "(plan, B2.11, unidad 11): este censo mide la parte atribuible a las "
               "tablas con el prefijo de la tanda 0, no el tope de esa unidad.")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    ar = SCC.Armado()
    cache = SCC.claves_db(SCC.DB_E1, ar.ns_e1)
    por_to = {}
    unidades = []
    for to in SCC.TOS_TANDA0:
        leg = SCC.cargar_chunks(to)
        r2 = SCC.cargar_chunks(to, Path(a.e0_r2))
        assert [c["id"] for c in leg] == [c["id"] for c in r2], to
        n = collections.Counter()
        for v, c in zip(leg, r2):
            k_leg, k_r2 = ar.k_e1(v), ar.k_e1(c)
            n["unidades"] += 1
            if cache is not None:
                n["clave_legada_en_cache"] += k_leg in cache
                n["clave_r2_en_cache"] += k_r2 in cache
            if k_leg == k_r2:
                continue
            mezcla = copy.deepcopy(c)
            mezcla["flags"] = copy.deepcopy(v["flags"])
            motivos = []
            if c["texto"] != v["texto"]:
                motivos.append("texto_propio")
            if c["herencia"] != v["herencia"]:
                motivos.append("herencia")
            if ar.k_e1(mezcla) != k_r2:
                motivos.append("flags")
            n["cambian"] += 1
            for m in motivos:
                n["motivo_" + m] += 1
            n["combinacion_" + "+".join(motivos)] += 1
            unidades.append({"unidad": c["id"], "motivos": motivos,
                             "miss_proyectado": None if cache is None else k_r2 not in cache})
        n["costo_estimado_usd"] = round(n["cambian"] * TARIFA_USD_POR_UNIDAD, 4)
        por_to[to] = dict(sorted(n.items()))
    tot = collections.Counter()
    for v in por_to.values():
        for k, x in v.items():
            if k != "costo_estimado_usd":
                tot[k] += x
    out = {
        "unidad": "U-R2-CODIGO", "etapa": "R1.d",
        "perfil": SCC.PERFIL, "namespace_e1": ar.ns_e1,
        "cache_e1_disponible": cache is not None,
        "tarifa_usd_por_unidad": TARIFA_USD_POR_UNIDAD,
        "declaracion": DECLARACION,
        "total": dict(sorted(tot.items())),
        "costo_estimado_total_usd": round(tot["cambian"] * TARIFA_USD_POR_UNIDAD, 4),
        "por_to": por_to,
        "unidades_que_cambian": unidades,
    }
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                           encoding="utf-8")


if __name__ == "__main__":
    main()
