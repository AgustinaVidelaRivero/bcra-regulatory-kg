"""Rama de caída de B6.3, opción A (decisión de la autora del 15/10/2026, recibida a las 14:15:41): desde qué N cada clase llega a la
suma de sus topes. USD 0, solo lectura.

El reparto de la decisión: 50 / 25 / 25 % por clase (O2), dentro de cada clase en proporción a las unidades, con un piso de 4 y un tope
de la mitad de las unidades (entera, hacia abajo). Como el reparto dentro de la clase es en proporción a las unidades y el tope es la
mitad de las unidades, los documentos de una clase llegan a su tope casi juntos, cerca de cuando la clase llega a la suma de sus topes.
Un documento con unidades impares llega un poco antes, porque su tope se redondea hacia abajo. El script da el N de cada documento y el
de cada clase, sin redondear las preguntas: el redondeo no está fijado.

Lee los elegibles de la rama de caída (`elegibles_O2.json`, `rama_de_caida_tanda_1`) y las unidades de la E0 corregida
(`unidades_por_to` del manifiesto de S0-6b). Con `--sumar <id>` agrega un documento elegible a su clase (el sucesor de ri_oc, cuando lo
fije S2).

Uso: python3 -I -B reparto_rama_caida_mesa.py <repo> [--sumar <id>]
"""
import json
import sys
from pathlib import Path

R = Path(sys.argv[1])
SUMAR = sys.argv[3:4] if sys.argv[2:3] == ["--sumar"] else []
el = json.load(open(R / "data/experiment/esq/elegibles_B63_O2_2026-10-15/elegibles_O2.json", encoding="utf-8"))
man = R / "data/experiment/segmentacion_oficial_e0r2/s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json"
u = json.load(open(man, encoding="utf-8"))["unidades_por_to"]
clase = {t: c for c, v in el["elegibles_final"].items() if isinstance(v, list) for t in v}
PESO = {"RI": 0.50, "NG_digerible": 0.25, "NG_necesita_reglas": 0.25}
ids = list(el["rama_de_caida_tanda_1"]["ids"])
for t in SUMAR:
    assert t in clase, f"{t} no es elegible (elegibles_final)"
    ids.append(t)
print(f"documentos: {len(ids)}" + (f" (con {', '.join(SUMAR)})" if SUMAR else " (sin el sucesor de ri_oc)"))
topes = {}
for c, p in PESO.items():
    d = sorted(t for t in ids if clase[t] == c)
    topes[c] = sum(u[t] // 2 for t in d)
    uc = sum(u[t] for t in d)
    por_doc = ", ".join(f"{t} {u[t]} (tope {u[t] // 2}, N > {(u[t] // 2) * uc / u[t] / p:.1f})" for t in d)
    print(f"{c}: {por_doc} | suma de los topes {topes[c]} | la clase llega a ella con N > {topes[c] / p:.0f}")
for n in (64, 104, 125):
    pide = {c: p * n for c, p in PESO.items()}
    tope = {c: min(pide[c], topes[c]) for c in PESO}
    print(f"N = {n}: pide {[round(v, 2) for v in pide.values()]} | con los topes {[round(v, 2) for v in tope.values()]}"
          f" | suma {round(sum(tope.values()), 2)}")
