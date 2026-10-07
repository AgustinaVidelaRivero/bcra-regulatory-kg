"""Control de forma de la primera lectura de las 41 (enmienda 8): un veredicto válido por ficha y el ancla presente en
el texto de su ficha. No cuenta veredictos (la cifra sale después de la adjudicación).

Ancla presente: (1) literal, con los espacios colapsados y sin las marcas ⟦E:/⟦O:/⟧; si no, (2) como secuencia contigua de
tokens con la normalización del validador r2 (`norm_tokens`, que une los cortes por guion de fin de línea).
Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_a_control_anclas41.py
Escribe salida/control_anclas_lectura1_41.json.
"""
import json
import os
import re

from udiag_comun import AQUI
from udiag_a_fichas41 import norm_tokens

OUT = os.path.join(AQUI, "salida")
VEREDICTOS = {"correcta", "incorrecta", "no_decidible"}


def limpio(s):
    s = re.sub(r"⟦[EO]:", "", s or "").replace("⟧", "")
    return re.sub(r"\s+", " ", s).strip()


def main():
    fichas = {f["ficha"]: f for f in json.load(open(os.path.join(OUT, "fichas_41_exceptua_operacion.json"),
                                                     encoding="utf-8"))["fichas"]}
    lect = json.load(open(os.path.join(OUT, "lectura1_41_exceptua_operacion.json"), encoding="utf-8"))
    filas, problemas = [], []
    assert [x["ficha"] for x in lect] == sorted(fichas), "fichas faltantes, sobrantes o fuera de orden"
    for x in lect:
        f = fichas[x["ficha"]]
        textos = [h["texto"] for h in f["texto_heredado_marcado"]] + [f["texto_propio_marcado"]]
        a = limpio(x["ancla"])
        literal = bool(a) and any(a in limpio(t) for t in textos)
        at = norm_tokens(x["ancla"])
        por_tokens = False
        if not literal and at:
            for t in textos:
                tt = norm_tokens(limpio(t))
                if any(tt[i:i + len(at)] == at for i in range(len(tt) - len(at) + 1)):
                    por_tokens = True
                    break
        ok = x["veredicto"] in VEREDICTOS and (literal or por_tokens)
        filas.append({"ficha": x["ficha"], "veredicto_valido": x["veredicto"] in VEREDICTOS,
                      "ancla_literal": literal, "ancla_por_tokens": por_tokens})
        if not ok:
            problemas.append(x["ficha"])
    res = {"fichas": len(lect), "veredictos_validos": sum(r["veredicto_valido"] for r in filas),
           "anclas_literales": sum(r["ancla_literal"] for r in filas),
           "anclas_por_tokens": sum(r["ancla_por_tokens"] for r in filas),
           "con_problema": problemas, "filas": filas}
    json.dump(res, open(os.path.join(OUT, "control_anclas_lectura1_41.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    print({k: v for k, v in res.items() if k != "filas"})


if __name__ == "__main__":
    main()
