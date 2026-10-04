"""
marcas_p4.py — U-PROMPT-R2, P4.c (USD 0): las marcas de la lectura asistida de las fichas, por dimensión y por brazo
(cumple, no_cumple, no_aplica o duda), para tabla_p4.py. Revisadas por la autora el 04/10/2026 (lectura_p4.md).

Reglas, fijadas antes de marcar (las razones caso por caso están en lectura_p4.md):
  - D1, umbral con tramo literal verificado. Aplica a la ficha si su texto propio tiene una cuantía que es umbral de una
    norma (las que no lo son, por lectura: NO_UMBRAL). Sellado: no_cumple (el crudo v3 no trae tramo de umbral).
    Nuevo: cumple si cada cuantía que es umbral queda dentro de un tramo verificado (apoyo_lectura_p4.json, «d1»).
  - D2, mención verificada. Por brazo: no_aplica si no tiene relaciones de sujeto; cumple si todas tienen la mención
    verificada (exacta o por tokens).
  - D3, omisiones con categoría y tramo. Por brazo: no_aplica si no declara omisiones; cumple si todas tienen categoría
    y tramo verificado.
  - D4, la tabla de `cap::1.2`; D5, `condicion_de` con firma nueva (de Condicion a Operacion o Potestad); D6, destino de
    `limita` (L-ESQ-R2 §1.4: el acto o la magnitud que el tope acota o, si es un ponderador, la exposición que
    pondera). Por lectura (LECTURA); no_aplica en el brazo que no emite la relación.

Uso: .venv/bin/python -B marcas_p4.py --analisis A --apoyo AP --salida DIR
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

# D1: cuantías del texto que no son umbral de una norma (lectura): bandas de códigos de informe, rótulos de conceptos,
# ejemplos, un período descriptivo y los coeficientes de una fórmula.
NO_UMBRAL = {"ric::4.3.3": "bandas de plazo de códigos de informe", "ric::9.2.1": "porcentajes en el nombre de conceptos",
             "ric::4.5.1": "ejemplos", "cap::7.1.3.2": "período descriptivo de un dato a publicar",
             "ric::3.1.6": "coeficiente de una fórmula"}
# D1: fichas con alguna cuantía no cubierta que no es umbral (las demás no cubiertas sí lo son).
D1_NO_CUBIERTA_NO_ES_UMBRAL = {"ric::11.1.1": "las dos no cubiertas son rótulos de columna de un cuadro de informe"}
# D4 a D6, por lectura: {chunk: {dimensión: (sellado, nuevo)}}.
LECTURA = {
    "cap::1.2": {"tabla_cap_1_2": ("no_cumple", "cumple"), "destino_limita": ("no_cumple", "no_aplica")},
    "cap::2.5.7": {"condicion_de_firma_nueva": ("cumple", "no_aplica")},
    "cap::6.2.2.6": {"condicion_de_firma_nueva": ("no_aplica", "no_cumple"), "destino_limita": ("cumple", "cumple")},
    "cla::5.1.1.1": {"condicion_de_firma_nueva": ("cumple", "cumple")},
    "cla::6.5.4.8": {"condicion_de_firma_nueva": ("no_aplica", "cumple")},
    "ctacte::5.1.2.2": {"condicion_de_firma_nueva": ("cumple", "cumple")},
    "ext::10.2.5": {"condicion_de_firma_nueva": ("cumple", "cumple")},
    "ext::13.4.8": {"condicion_de_firma_nueva": ("no_aplica", "cumple")},
    "ext::3.3.3.3": {"condicion_de_firma_nueva": ("cumple", "no_cumple")},
    "ext::3.5.6.9": {"condicion_de_firma_nueva": ("cumple", "no_aplica")},
    "cap::10.1": {"destino_limita": ("cumple", "cumple")},
    "cap::2.12.2.4": {"destino_limita": ("no_cumple", "cumple")},
    "cap::2.12.3.2": {"destino_limita": ("cumple", "cumple")},
    "cap::4.2.1::intro": {"destino_limita": ("cumple", "cumple")},
    "cap::4.3.3.2": {"destino_limita": ("no_cumple", "cumple")},
    "cap::5.1.1": {"destino_limita": ("no_cumple", "no_aplica")},
    # Revisión de la autora (04/10/2026): el `limita` del nuevo va de Restriccion a Definicion, el validador lo
    # rechaza por la firma y no llega al grafo: no emite.
    "cap::5.4.4": {"destino_limita": ("no_aplica", "no_aplica")},
    "cap::8.4.1.19": {"destino_limita": ("no_cumple", "no_cumple")},
    "cap::8.4.1.6": {"destino_limita": ("no_cumple", "no_aplica")},
    "cap::8.5.3": {"destino_limita": ("no_aplica", "cumple")},
    "ext::13.4.4": {"destino_limita": ("no_aplica", "cumple")},
    "ext::2.7::cierre": {"destino_limita": ("no_cumple", "no_aplica")},
    "ext::7.1.1.3": {"destino_limita": ("no_aplica", "cumple")},
}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--analisis", type=Path, required=True)
    ap.add_argument("--apoyo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    an = json.loads(a.analisis.read_text(encoding="utf-8"))
    d1 = json.loads(a.apoyo.read_text(encoding="utf-8"))["d1"]
    marcas = {}
    for cid, f in an["filas"].items():
        if "falta_brazo" in f:
            continue
        m = {}
        x = d1.get(cid)
        if x and cid not in NO_UMBRAL:
            todas = x["cubiertas"] == x["cuantias"] or cid in D1_NO_CUBIERTA_NO_ES_UMBRAL
            m["umbral_tramo_verificado"] = {"sellado": "no_cumple", "nuevo": "cumple" if todas else "no_cumple"}
        for dim, clave, ok in (("mencion_verificada", "menciones", lambda h: h.get("verificada") in ("exacta", "tokens")),
                               ("omisiones_categoria_tramo", "omisiones",
                                lambda h: bool(h.get("categoria")) and h.get("verificacion") in ("exacta", "tokens"))):
            m[dim] = {}
            for b in ("sellado", "nuevo"):
                hs = f["hechos"][b].get(clave) or []
                m[dim][b] = "no_aplica" if not hs else ("cumple" if all(ok(h) for h in hs) else "no_cumple")
        for dim, (s, n) in LECTURA.get(cid, {}).items():
            m[dim] = {"sellado": s, "nuevo": n}
        marcas[cid] = m
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "marcas_lectura_p4.json").write_text(json.dumps(
        {"estado": "lectura asistida, revisada por la autora el 04/10/2026", "fichas": marcas}, ensure_ascii=False,
        indent=1) + "\n", encoding="utf-8")
    print(len(marcas), "fichas marcadas")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
