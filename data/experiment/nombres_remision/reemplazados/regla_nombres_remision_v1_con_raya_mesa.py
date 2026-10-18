"""La regla de los `nombres_remision` que propone la mesa (§131, 16/10/2026): derivada del título oficial del inventario
(`data/experiment/escalado_prep/inventario_tos.csv`, `titulo_oficial`; los cinco de desarrollo, de `inventario_resumen.json`), sin
listas a mano.

nombres(titulo_oficial) → lista de nombres que se suman al título oficial (que el ensamblado ya pone solo,
`r1_referencias.titulos_de_inventario`):
  1. el título con las abreviaturas del inventario expandidas, si alguna cambia. La tabla es cerrada y sale de las abreviaturas que
     aparecen en los 157 títulos del inventario (todas las que hay): RI, Cont., seg. soc., seg., Adm., Prov., ges., ctrol., tec. e inf.;
  2. con GUIONES = True (variante en contra, para medir): además, el título y el expandido con la raya (–) en lugar del guion entre
     espacios (" - "), como los citan algunos textos.
No agrega nombres cortos ni recortes: en la tanda 0 no sumaron ninguna resolución, y un recorte del prefijo «RI …» colisiona con la
norma del mismo nombre (p. ej., «Grandes exposiciones al riesgo de crédito» es gerc, no ri_gerc).
"""
import re

GUIONES = True
# (patrón, expansión): en este orden, para que «seg. soc.» gane sobre «seg.»
ABREVIATURAS = [
    (r"\bRI\b", "Régimen Informativo"),
    (r"\bCont\.", "Contable"),
    (r"\bseg\.\s+soc\.", "seguridad social"),
    (r"\bseg\.", "seguridad"),
    (r"\bAdm\.", "Administración"),
    (r"\bProv\.", "Provinciales"),
    (r"\bges\.", "gestión"),
    (r"\bctrol\.", "control"),
    (r"\btec\.", "tecnología"),
    (r"\binf\.", "información"),
]


def expandir(t: str) -> str:
    for pat, exp in ABREVIATURAS:
        t = re.sub(pat, exp, t)
    return t


def nombres(titulo_oficial: str) -> list[str]:
    out = []
    e = expandir(titulo_oficial)
    if e != titulo_oficial:
        out.append(e)
    if GUIONES:
        for x in [titulo_oficial] + out:
            if " - " in x:
                out.append(x.replace(" - ", " – "))
    return list(dict.fromkeys(out))
