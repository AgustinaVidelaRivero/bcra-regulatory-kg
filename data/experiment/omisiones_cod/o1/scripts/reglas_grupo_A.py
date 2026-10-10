"""U-OMISIONES-COD, O1 — diseño de las marcas (a) a (d) del grupo A, tal como O2 las lleva al ensamblado
(`ensamblar_tanda0.py`, cadena r2 con la fase r2b, donde hoy se arma el registro de omisiones). Funciones puras: reciben
la omisión o la entidad validada, el chunk de E0 (con sus partes) y el módulo `validador_r2` (V), y devuelven las marcas.
No tocan `kg.json`.

(a) `tramo_en_heredado`: la omisión cuyo tramo se ubica solo en el texto heredado. Se reproduce, sin cambiarla, la
    regla de `V.verificar_tramo_omision` (primero el texto propio; si no, el texto completo; en un mini-chunk a mitad de
    oración, el orden de lectura), con el tramo que recibió el validador (`tramo_modelo` si el guardado es el literal).
    La marca va cuando la ubicación es «heredado»; «orden_de_lectura» se cuenta aparte y no se marca.
(b) `revisar`: en las omisiones `meta_normativo`, con marca del contador (`V.marcas_meta_normativo`, sobre el mismo
    tramo que vio el validador) o con una recomendación (RECOMENDACION, lista cerrada; decisión 3 de la autora sobre
    el FRENO T4: «es deseable», «se recomienda», «es conveniente», «debería» son normativas, modalidad de consejo).
(c) `unidad_entera`: la omisión cuyo tramo cubre todo el texto propio de su unidad, sin la numeración inicial
    (cobertura 1,0 sobre la secuencia de tokens de R-NORM), en cualquier categoría (el reporte las cuenta por
    categoría). Es una sola marca; lleva dos atributos descriptivos, que no la deciden: `es_item` (`V._es_item`) y
    `con_extraccion` (la unidad tiene alguna entidad de contenido). Los dos casos de la v7 son ítems con extracción:
    `ext::5.8.2.2` (el texto entero quedó como omisión y, además, en dos Condicion y una Operacion de la unidad) y
    `ctacte::2.1.1.4` (el ítem quedó como omisión y como segundo segmento del tramo compuesto de la Obligacion
    anclada en el encabezado).
(d) `supuesto_en_norma`: la entidad de contenido (no Condicion) cuya descripción o tramo lleva un supuesto, por un
    conector condicional de la lista cerrada CONECTORES_SUPUESTO. Mide y no corrige.
"""
from __future__ import annotations

import re
import unicodedata

UMBRAL_COBERTURA_UNIDAD = 1.0
TIPOS_SUPUESTO_EN_NORMA = ("Obligacion", "Restriccion", "Potestad", "Excepcion", "Operacion", "Definicion")
_COP = r"(es|son|sea|sean|sera|seran|seria|serian|resulta|resultan|resulte|resulten|resultaria|resultarian)"
RECOMENDACION = {
    "copula_deseable": re.compile(r"\b" + _COP + r"( (muy|altamente|particularmente))? "
                                  r"(deseables?|convenientes?|recomendables?|aconsejables?)\b"),
    "se_recomienda": re.compile(r"\bse (recomienda|recomiendan|recomendara|aconseja|aconsejan|sugiere|sugieren)\b"),
    "deberia": re.compile(r"\b(deberia|deberian)\b"),
    "buena_practica": re.compile(r"\bbuenas? practicas?\b"),
}
CONECTORES_SUPUESTO = {
    "cuando": re.compile(r"\bcuando\b"),
    "siempre_que": re.compile(r"\bsiempre (y cuando|que)\b"),
    "en_tanto": re.compile(r"\ben tanto\b"),
    "mientras": re.compile(r"\bmientras\b"),
    "en_la_medida": re.compile(r"\ben la medida (en )?que\b"),
    "en_caso": re.compile(r"\ben (el )?casos? (de|en que|que)\b|\ben los casos (en )?que\b"),
    "a_condicion": re.compile(r"\b(a|con la) condicion de\b"),
    "de_no": re.compile(r"\bde no\b"),
    "si": re.compile(r"\bsi\b(?! bien\b)"),
}


def norm(s) -> str:
    s = unicodedata.normalize("NFKD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def _sin_numeracion(toks: list[str]) -> list[str]:
    i = 0
    while i < len(toks) and toks[i].isdigit():
        i += 1
    return toks[i:]


def donde_tramo_omision(tramo: str, chunk: dict, V, holgura: int) -> str:
    """La ubicación que `V.verificar_tramo_omision` cuenta, sin el registro: propio, heredado, orden_de_lectura o no."""
    nivel = V.verificar_tramo(tramo, chunk.get("texto") or "", holgura)[0]
    if nivel != "no":
        return "propio"
    donde = "no"
    n_c = V.verificar_tramo(tramo, V.texto_completo(chunk), holgura)[0]
    nivel = n_c
    if n_c != "no":
        donde = "heredado"
    if nivel != "exacta" and V._mini_a_mitad(chunk):
        n_l = V.verificar_tramo(tramo, V.texto_en_orden_de_lectura(chunk), holgura)[0]
        if V._ORDEN_NIVEL[n_l] > V._ORDEN_NIVEL[nivel]:
            donde = "orden_de_lectura"
    return donde


def cobertura_unidad(tramo: str, chunk: dict, V) -> float | None:
    """Fracción de los tokens del texto propio (sin la numeración inicial) que cubre una aparición contigua del
    tramo (sin su numeración). None si el tramo no aparece contiguo en el texto propio."""
    propio = _sin_numeracion(V.norm_tokens(chunk.get("texto") or ""))
    t = _sin_numeracion(V.norm_tokens(tramo or ""))
    if not propio or not t:
        return None
    for i in range(len(propio) - len(t) + 1):
        if propio[i:i + len(t)] == t:
            return len(t) / len(propio)
    return None


TIPOS_SIN_CONTENIDO = ("TextoOrdenado", "Sujeto", "Comunicacion")


def con_extraccion(validacion: dict | None) -> bool:
    return any(e.get("type") not in TIPOS_SIN_CONTENIDO for e in (validacion or {}).get("entidades", []))


def marcas_omision(o: dict, chunk: dict, V, holgura: int = 2, extraccion: bool = False) -> dict:
    tramo_validador = o.get("tramo_modelo") or o.get("tramo")
    out = {"tramo": o.get("tramo"), "donde_tramo": "ausente", "tramo_en_heredado": False, "marca_contador": [],
           "recomendacion": [], "revisar": False, "unidad_entera": False, "es_item": None, "con_extraccion": None,
           "cobertura": None}
    if not tramo_validador:
        return out
    out["donde_tramo"] = donde_tramo_omision(tramo_validador, chunk, V, holgura)
    out["tramo_en_heredado"] = out["donde_tramo"] == "heredado"
    t = " ".join(V.norm_tokens(tramo_validador))
    out["recomendacion"] = [k for k, rx in RECOMENDACION.items() if rx.search(t)]
    if o.get("categoria") == "meta_normativo":
        out["marca_contador"] = V.marcas_meta_normativo(tramo_validador)
        out["revisar"] = bool(out["marca_contador"] or out["recomendacion"])
    if out["donde_tramo"] == "propio":
        out["cobertura"] = cobertura_unidad(o.get("tramo"), chunk, V)
        if out["cobertura"] is not None and out["cobertura"] >= UMBRAL_COBERTURA_UNIDAD:
            out["unidad_entera"] = True
            out["es_item"] = bool(V._es_item(chunk))
            out["con_extraccion"] = extraccion
    return out


def supuesto_en_norma(e: dict, V) -> list[str]:
    if e.get("type") not in TIPOS_SUPUESTO_EN_NORMA:
        return []
    desc = (e.get("properties") or {}).get("descripcion") if isinstance(e.get("properties"), dict) else None
    textos = [x for x in (desc, (e.get("provenance") or {}).get("tramo")) if isinstance(x, str) and x]
    t = " ".join(" ".join(V.norm_tokens(x)) for x in textos)
    return [k for k, rx in CONECTORES_SUPUESTO.items() if rx.search(t)]


_RE_DONDE = re.compile(r"dentro de (?:la|las) (Obligacion|Restriccion|Potestad|Excepcion|Operacion|Definicion) "
                       r"e(\d+)(?:\s*(?:a|y)\s*e(\d+))?")


def entidades_de_donde(donde: str) -> list[tuple[str, list[str]]]:
    """Las entidades que nombra el campo «donde» de un supuesto de T4 «dentro_de_norma»: «dentro de la Obligacion e7»,
    «dentro de las Restriccion e11 a e13», «dentro de las Excepcion e6 y e7»."""
    out = []
    for m in _RE_DONDE.finditer(donde):
        a = int(m.group(2))
        if m.group(3) is None:
            ids = [a]
        elif " y e" in m.group(0):
            ids = [a, int(m.group(3))]
        else:
            ids = list(range(a, int(m.group(3)) + 1))
        out.append((m.group(1), [f"e{i}" for i in ids]))
    return out
