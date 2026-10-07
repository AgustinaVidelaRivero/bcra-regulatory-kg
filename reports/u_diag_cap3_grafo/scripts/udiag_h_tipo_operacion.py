"""Grupo H de U-OMISIONES-COD v2 (propuesta): `tipo_normalizado` de la Operacion, medido sobre a9631a64 y e22fae1a.

Normalización propuesta (solo código, sin lista de sinónimos): minúsculas; sin tildes ni diacríticos (NFKD); todo
carácter que no sea letra o dígito pasa a espacio; espacios colapsados; sin espacios al borde (el punto final cae con
la regla anterior). Se conserva `tipo` tal cual. Variantes medidas para el desglose: solo minúsculas; minúsculas y sin
tildes; la normalización entera.
Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_h_tipo_operacion.py
Escribe salida/tipo_operacion_h.json.
"""
import collections
import json
import os
import re
import unicodedata

from udiag_comun import AQUI, cargar_kg


def sin_tildes(s):
    return "".join(c for c in unicodedata.normalize("NFKD", s) if not unicodedata.combining(c))


def tipo_normalizado(s):
    s = sin_tildes(s.lower())
    s = re.sub(r"[^0-9a-zñ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def main():
    out = {}
    for nombre in ("diez", "sincola"):
        kg = cargar_kg(nombre)
        ops = [n for n in kg["nodes"] if n["type"] == "Operacion"]
        tipos = [(n.get("properties") or {}).get("tipo") for n in ops]
        con = [t for t in tipos if isinstance(t, str) and t.strip()]
        norm_ = collections.Counter(tipo_normalizado(t) for t in con)
        out[nombre] = {
            "operaciones": len(ops), "con_tipo": len(con),
            "distintos_tal_cual": len(set(con)),
            "distintos_minusculas": len({t.lower() for t in con}),
            "distintos_minusculas_sin_tildes": len({sin_tildes(t.lower()) for t in con}),
            "distintos_normalizados": len(norm_),
            "unicos_normalizados_con_un_solo_nodo": sum(1 for v in norm_.values() if v == 1),
            "diez_mas_frecuentes_normalizados": norm_.most_common(10),
            "diez_mas_frecuentes_tal_cual": collections.Counter(con).most_common(10),
            "ejemplos_que_se_unen": sorted(
                [(k, sorted({t for t in con if tipo_normalizado(t) == k})) for k in norm_
                 if len({t for t in con if tipo_normalizado(t) == k}) > 2], key=lambda x: -len(x[1]))[:8],
        }
        print(nombre, {k: v for k, v in out[nombre].items() if k.startswith(("operaciones", "con_tipo", "distintos", "unicos"))})
    json.dump(out, open(os.path.join(AQUI, "salida", "tipo_operacion_h.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print(out["diez"]["diez_mas_frecuentes_normalizados"])


if __name__ == "__main__":
    main()
