"""
tabla_p4.py — U-PROMPT-R2, P4.c (USD 0): la tabla pareada con Wilson al 95 %, desde las marcas de la lectura asistida
(`marcas_lectura_p4.json`, revisadas por la autora) y la muestra.

Por dimensión y por grupo (los 40 sorteados aparte de los fijos, F1, las listas, el fuera de muestra y la pata de E3):
- fichas en que la dimensión aplica;
- cuántas cumple cada brazo, con su intervalo de Wilson al 95 %;
- el cruce pareado: los dos, solo el nuevo, solo el sellado, ninguno;
- las DUDA, que no cuentan para ningún lado y se listan.

Marcas por ficha y dimensión: {"sellado": m, "nuevo": m}, con m en cumple, no_cumple, no_aplica o duda.

Escribe solo en --salida. Uso: .venv/bin/python -B tabla_p4.py --muestra M --marcas MARCAS --salida DIR
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

DIMENSIONES = ("umbral_tramo_verificado", "mencion_verificada", "omisiones_categoria_tramo", "tabla_cap_1_2",
               "condicion_de_firma_nueva", "destino_limita")


def wilson(k: int, n: int, z: float = 1.959964) -> list | None:
    if n == 0:
        return None
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [max(0.0, round(c - h, 3)), min(1.0, round(c + h, 3))]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--muestra", type=Path, required=True)
    ap.add_argument("--marcas", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    m = json.loads(a.muestra.read_text(encoding="utf-8"))
    marcas = json.loads(a.marcas.read_text(encoding="utf-8"))["fichas"]
    grupo = {c: "sorteo" for e in m["sorteo"] for c in m["sorteo"][e]["elegidos"]}
    grupo |= {c: "fijos" for c in m["fijos"]} | {c: "f1" for c in m["f1"]}
    grupo |= {c: "listas" for v in m["listas_excepciones"].values() for c in v["tomados"]}
    grupo |= {c: "fuera" for v in m["fuera_de_muestra"].values() for c in v} | {c: "pata_e3" for c in m["pata_e3"][:3]}
    tabla = {}
    for g in ("sorteo", "fijos", "listas", "f1", "fuera", "pata_e3"):
        ids = sorted(c for c in marcas if grupo.get(c) == g)
        for d in DIMENSIONES:
            pares = [(marcas[c][d]["sellado"], marcas[c][d]["nuevo"], c) for c in ids if d in marcas[c]]
            aplica = [(s, n, c) for s, n, c in pares if "no_aplica" not in (s, n)]
            dudas = [c for s, n, c in aplica if "duda" in (s, n)]
            firmes = [(s, n) for s, n, c in aplica if "duda" not in (s, n)]
            ks, kn = sum(s == "cumple" for s, _ in firmes), sum(n == "cumple" for _, n in firmes)
            tabla.setdefault(g, {})[d] = {
                "fichas_que_aplica": len(aplica), "firmes": len(firmes),
                "sellado_cumple": ks, "sellado_wilson95": wilson(ks, len(firmes)),
                "nuevo_cumple": kn, "nuevo_wilson95": wilson(kn, len(firmes)),
                "pareado": {"los_dos": sum(s == n == "cumple" for s, n in firmes),
                            "solo_nuevo": sum(s != "cumple" and n == "cumple" for s, n in firmes),
                            "solo_sellado": sum(s == "cumple" and n != "cumple" for s, n in firmes),
                            "ninguno": sum(s != "cumple" and n != "cumple" for s, n in firmes)},
                "duda": dudas}
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "tabla_pareada_p4.json").write_text(json.dumps(tabla, ensure_ascii=False, indent=1) + "\n",
                                                   encoding="utf-8")
    print(json.dumps(tabla.get("sorteo"), ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
