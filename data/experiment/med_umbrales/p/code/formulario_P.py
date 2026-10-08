"""
formulario_P.py — U-MED-UMBRALES, etapa P, tramo P-a, punto 7: el formulario del paso 1 (§5.2 de la enmienda), uno por
lote, en markdown que la autora llena a mano y el código lee. Un bloque por ficha, en el orden de lectura del acta.

Formato de cada bloque:
    ## L<k>-<nn> · `<id del elemento>`
    - <campo> [<valores admitidos>]: ______
Se llena reemplazando «______» por el valor. Un campo que queda en «______» o vacío se lee como no llenado.
"""
from __future__ import annotations

import re

VACIO = "______"
UNIDADES = ("porcentaje", "moneda", "dias", "meses", "anios", "veces", "uva")       # lista cerrada (modelos_r2.UNIDAD)
UNIDADES_FUERA = ("horas", "semanas")                                             # con la marca fuera_de_lista
COMPARACIONES = ("maximo_inclusivo", "maximo_estricto", "minimo_inclusivo", "minimo_estricto", "igual", "coeficiente",
                 "no_determinada")                                                # §2.4 de la enmienda
CLASES_VACIO = ("oculta un umbral", "límite sin cuantía en la letra", "no es un umbral")   # §2.5

CAMPOS = (
    ("pertinencia", "pertinente | no pertinente | inexistente | duplicado"),
    ("valor", "número con punto decimal y sin separador de miles («1.25», «5000000000»), o «sin valor»"),
    ("unidad", " | ".join(UNIDADES + UNIDADES_FUERA) + " | sin unidad | otra: <cuál>"),
    ("moneda", "ARS | USD | EUR | no aplica"),
    ("tipo_de_dias", "habiles | corridos | sin tipo | no aplica"),
    ("comparacion", " | ".join(COMPARACIONES)),
    ("palabras_de_la_comparacion", "las palabras de la norma que fijan el sentido, literales, o «ninguna»"),
    ("base", "el tramo exacto de la base, o «sin base»"),
    ("destino_de_la_base", "<to>::<punto> | definicion: <término> | no remite | no aplica"),
    ("no_decidible", "no | sí: <motivo>"),
    ("nota", "libre"),
    ("hora_inicio", "hh:mm"),
    ("hora_fin", "hh:mm"),
)
CAMPOS_VACIO = (
    ("clase_vacio", " | ".join(CLASES_VACIO)),
    ("si_oculta_un_umbral", "lo que la letra fija y el elemento no guarda: valor, unidad, comparación y base"),
    ("no_decidible", "no | sí: <motivo>"),
    ("nota", "libre"),
    ("hora_inicio", "hh:mm"),
    ("hora_fin", "hh:mm"),
)
_RE_BLOQUE = re.compile(r"^## (L\d+-\d+) · `([^`]+)`", re.M)
_RE_CAMPO = re.compile(r"^- ([a-z_]+)(?: \[[^\]]*\])?:[ \t]*(.*)$")


def bloque(etiqueta: str, eid: str, vacio: bool) -> str:
    lin = [f"## {etiqueta} · `{eid}`", ""]
    if vacio:
        lin.append("Pregunta única del §2.5: ¿la letra fija acá una cuantía, un sentido o una base?")
    for c, v in (CAMPOS_VACIO if vacio else CAMPOS):
        lin.append(f"- {c} [{v}]: {VACIO}")
    return "\n".join(lin) + "\n"


def formulario(titulo: str, bloques: list[tuple[str, str, bool]]) -> str:
    cab = [f"# {titulo}", "",
           "Paso 1 de la enmienda (§5.2): se responde desde la norma, con la ficha del mismo número, sin ver los campos "
           "del grafo. Se llena reemplazando «______». La regla de calificación es la v0 (`regla_calificacion_v0.md`, el "
           "§2 firmado). Un campo que no se puede decidir va en `no_decidible`, con su motivo.", ""]
    return "\n".join(cab) + "\n" + "\n".join(bloque(*b) for b in bloques)


def leer(texto: str) -> dict[str, dict]:
    """{id: {'etiqueta', 'campos': {campo: valor o None}}}. Un campo sin llenar queda en None."""
    out = {}
    marcas = list(_RE_BLOQUE.finditer(texto))
    for k, m in enumerate(marcas):
        fin = marcas[k + 1].start() if k + 1 < len(marcas) else len(texto)
        campos = {}
        for linea in texto[m.end():fin].splitlines():
            c = _RE_CAMPO.match(linea.strip())
            if c:
                v = c.group(2).strip()
                campos[c.group(1)] = None if (not v or v == VACIO) else v
        out[m.group(2)] = {"etiqueta": m.group(1), "campos": campos}
    return out
