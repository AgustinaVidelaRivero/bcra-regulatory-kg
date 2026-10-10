"""U-OMISIONES-COD, O1 — diseño del clasificador determinístico de la copia de la nota de E3 (grupo A, ítem e).

Población. Las entidades de la extracción final de cada unidad aceptada tras un reintento de E3
(`aceptado_tras_reintento`). Son las únicas extracciones del grafo escritas después de leer las notas del verificador:
la cola humana entra con el crudo del primer intento (`runner_corpus.entrada_r2`), que no vio ninguna nota. Por cada
entidad, dos campos: la descripción y la etiqueta. La marca del ratchet (`ratchet_e3.copias_nota`, ventana de 5
tokens) cubre solo una parte de esa población; el clasificador no depende de ella.

Regla, sobre tokens de R-NORM (`validador_r2.norm_tokens`), con las listas cerradas de la regla de lectura de P3b-2
(`prompt_r2/p3b2/lista_copia_nota.py`: VACIAS y METALENGUAJE, importadas):
  - notas: las de los faltantes de la verificación anterior al último reintento (el feedback que leyó E1);
  - una palabra del campo es «de la nota» si está en alguna nota, no es vacía ni un número, y no está en el texto de
    la unidad (propio y heredado), ni en las citas de esos faltantes, ni en la extracción del primer intento de la
    unidad (etiquetas, descripciones y demás textos de sus entidades: lo que el modelo escribió antes de leer la nota);
  - clase 1: una palabra de metalenguaje del verificador «de la nota»;
  - clase 3: una palabra de contenido «de la nota» que tampoco es una flexión de una palabra de la unidad (la ayuda de
    lectura de T4, `lista_copia_nota_t4.candidatos_flexion`: comparte todo menos las 3 últimas letras, al menos 4,
    con una diferencia de largo de 4 o menos);
  - el campo se detecta si cae en la clase 1 o en la 3.
Marca; no rechaza ni corrige. No toca `kg.json`: va a un registro del ensamblado y a su reporte.
"""
from __future__ import annotations

ESTADO_POBLACION = "aceptado_tras_reintento"


def flexion_en(t: str, toks_unidad: set) -> bool:
    raiz = t[:max(4, len(t) - 3)]
    return any(u != t and u.startswith(raiz) and abs(len(u) - len(t)) <= 4 for u in toks_unidad)


def textos_de_entidad(e: dict) -> list[str]:
    """Todas las cadenas de una entidad (etiqueta, descripción, propiedades, tramos), recursivamente."""
    out = []

    def rec(x):
        if isinstance(x, str):
            out.append(x)
        elif isinstance(x, dict):
            for v in x.values():
                rec(v)
        elif isinstance(x, list):
            for v in x:
                rec(v)
    rec(e)
    return out


def campos_de_entidad(e: dict) -> list[tuple[str, str]]:
    props = e.get("properties") if isinstance(e.get("properties"), dict) else {}
    return [(c, t) for c, t in (("descripcion", props.get("descripcion")), ("label", e.get("label")))
            if isinstance(t, str) and t]


def clasificar_campo(texto: str, contexto: dict, V, VACIAS, METALENGUAJE, con_filtro_primer_intento: bool = True,
                     con_flexion: bool = True) -> dict:
    """contexto: toks_unidad, toks_notas, toks_citas, toks_primer_intento (conjuntos de tokens de R-NORM)."""
    toks = set(V.norm_tokens(texto))
    fuera = contexto["toks_unidad"] | contexto["toks_citas"]
    if con_filtro_primer_intento:
        fuera = fuera | contexto["toks_primer_intento"]
    de_la_nota = {t for t in toks if t in contexto["toks_notas"] and t not in fuera and not t.isdigit()}
    meta = sorted(t for t in de_la_nota if t in METALENGUAJE)
    contenido = sorted(t for t in de_la_nota if t not in VACIAS and t not in METALENGUAJE
                       and not (con_flexion and flexion_en(t, contexto["toks_unidad"])))
    clase = 1 if meta else (3 if contenido else None)
    return {"clase": clase, "metalenguaje": meta, "palabras_de_la_nota": contenido}


def ventanas(toks: list[str], n: int) -> set[tuple[str, ...]]:
    return {tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)}


def clasificar_campo_ventana(texto: str, contexto: dict, V, VACIAS, METALENGUAJE, n: int,
                             con_filtro_primer_intento: bool = True, con_flexion: bool = True) -> dict:
    """Variante por ventana: las ventanas de n tokens del campo que están en una nota y no en el texto de la unidad ni
    en las citas (la regla del ratchet, con n = 5); sobre las palabras de esas ventanas, las clases 1 y 3 como en
    `clasificar_campo`."""
    ws = ventanas(V.norm_tokens(texto), n) & contexto["ventanas_notas"][n]
    ws -= contexto["ventanas_unidad"][n] | contexto["ventanas_citas"][n]
    toks = {t for w in ws for t in w}
    fuera = contexto["toks_unidad"] | contexto["toks_citas"]
    if con_filtro_primer_intento:
        fuera = fuera | contexto["toks_primer_intento"]
    meta = sorted(t for t in toks if t in METALENGUAJE and t not in fuera)
    contenido = sorted(t for t in toks if t not in fuera and t not in VACIAS and t not in METALENGUAJE
                       and not t.isdigit() and not (con_flexion and flexion_en(t, contexto["toks_unidad"])))
    clase = 1 if meta else (3 if contenido else None)
    return {"clase": clase, "metalenguaje": meta, "palabras_de_la_nota": contenido,
            "ventanas": sorted(" ".join(w) for w in ws)[:5]}


def contexto_unidad(chunk: dict, notas: list[str], citas: list[str], primer_intento: list[dict], V,
                    tamanos=(3, 4, 5)) -> dict:
    tok = lambda xs: {t for x in xs for t in V.norm_tokens(x or "")}  # noqa: E731
    unidad = V.norm_tokens(V.texto_completo(chunk))
    nt = [V.norm_tokens(x or "") for x in notas]
    ct = V.norm_tokens(" \n ".join(citas))
    return {"toks_unidad": set(unidad), "toks_notas": tok(notas),
            "toks_citas": tok(citas), "toks_primer_intento": tok(t for e in primer_intento for t in textos_de_entidad(e)),
            "ventanas_notas": {n: set().union(*(ventanas(x, n) for x in nt)) if nt else set() for n in tamanos},
            "ventanas_unidad": {n: ventanas(unidad, n) for n in tamanos},
            "ventanas_citas": {n: ventanas(ct, n) for n in tamanos}}
