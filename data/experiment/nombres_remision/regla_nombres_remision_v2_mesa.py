"""La regla de los `nombres_remision` que propone la mesa, versión 2 (§131, 16/10/2026): derivada del título oficial del inventario
(`data/experiment/escalado_prep/inventario_tos.csv`, `titulo_oficial`; los cinco de desarrollo, de `inventario_resumen.json`), sin
listas a mano. Toma los tres patrones de las listas a mano de la tanda 0 que cambian alguna resolución, generalizados:

nombres(titulo_oficial) → los nombres que se suman al título oficial (que el ensamblado ya pone solo,
`r1_referencias.titulos_de_inventario`), sin repetir:
  1. abreviaturas: el título con las abreviaturas del inventario expandidas. La tabla es cerrada: son todas las que aparecen en los 157
     títulos del inventario (RI, Cont., seg. soc., seg., Adm., Prov., ges., ctrol., tec. e inf.). Patrón de pagjub y de ric;
  2. artículo: «de los» y «de las» → «de», sobre el título expandido. Patrón de pro («de los usuarios» → «de usuarios»);
  3. cola: el título expandido cortado antes de « por cuenta de ». Patrón de pagjub («Pago de beneficios de la seguridad social»);
  y la combinación de 2 y 3.
Nunca recorta la cabeza del título: un recorte del prefijo «RI …» colisiona con la norma del mismo nombre (p. ej., «Grandes exposiciones
al riesgo de crédito» es gerc, no ri_gerc). Tampoco suma la variante con la raya: se midió y resuelve mal las «normas complementarias».
"""
import re

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


def sin_articulo(t: str) -> str:
    return re.sub(r"\bde\s+(?:los|las)\s+", "de ", t, flags=re.I)


def sin_cola(t: str) -> str:
    i = t.lower().find(" por cuenta de ")
    return t[:i] if i > 0 else t


def nombres(titulo_oficial: str) -> list[str]:
    e = expandir(titulo_oficial)
    cand = [e, sin_articulo(e), sin_cola(e), sin_cola(sin_articulo(e))]
    return [x for x in dict.fromkeys(cand) if x != titulo_oficial]
