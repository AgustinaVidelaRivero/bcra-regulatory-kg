"""
selftest_instrumento_v1_P.py — U-MED-UMBRALES, etapa P: casos sintéticos del instrumento v1 (desde el lote 2; regla v1, §5, y
nota del 10/10/2026 al pie de la enmienda 1): el id opaco, qué resalta la ficha, la ficha sin campos del grafo, la declaración de
la misma unidad, y los formularios de los dos pasos con su nota. No lee el grafo ni ningún dato de un lote: el nodo, el texto y
los elementos son inventados, y las funciones que leen E0 y E1 se reemplazan por las del caso.

  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B selftest_instrumento_v1_P.py [--ejemplo SALIDA.md]
Corre sobre una copia (CLAUDE.md §4.l): usa los tokens de validador_r2 de la copia. Sale con 1 si algún caso falla.
"""
from __future__ import annotations

import argparse
import hashlib
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import armador_fichas_P as A  # noqa: E402
import comparador_paso2_P as K  # noqa: E402
import comun_P as C  # noqa: E402
import formulario_P as F  # noqa: E402

CID, CID2 = "inv::9.9.9", "inv::9.9.8"
TEXTO = ("9.9.9. Las entidades inventadas no podrán superar el 5 % de su capital inventado, salvo lo previsto en el punto "
         "6.3.2.2. El plazo será de 30 días corridos y el importe mínimo es 5 veces el importe de referencia.")
CH = {"id": CID, "titulo": "Punto inventado", "paginas": [1], "texto": TEXTO, "herencia": []}
NODO = {"id": "Condicion_regla_inventada_para_el_selftest_abc123", "type": "Condicion",
        "label": "Regla inventada para el selftest",
        "properties": {"descripcion": "Descripción inventada del nodo, salida del extractor, que la ficha no puede mostrar.",
                       "umbrales": []},
        "provenance": {"to": "inv", "archivo": "inventado.pdf", "chunk_id": CID},
        "provenances": [{"to": "inv", "archivo": "inventado.pdf", "chunk_id": CID}]}
EID = NODO["id"] + "#u0"


def span(s: str, desde: int = 0) -> tuple[int, int]:
    a = TEXTO.index(s, desde)
    return a, a + len(s)


def con(u: dict, textos=None):
    """Reemplaza las funciones de comun_P que leen E0 y E1 por las del caso."""
    base = {"chunk_id": None, "spans": [], "metodo": None, "nota": None, "tramos_e1": [], "fuentes_e1": {},
            "tramo_e1_del_elemento": None}
    C.ubicar = lambda n, i, el: {**base, **u}
    C.textos_nodo = lambda n: textos if textos is not None else [(CID, TEXTO, CH)]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ejemplo", type=Path)
    a = ap.parse_args()
    R = []

    def ok(c, q):
        R.append((bool(c), q))

    # 1. id opaco (C25)
    o = A.opaco("s1", 2, EID)
    ok(len(o) == 6 and o.isalpha() and o.islower() and o == A.opaco("s1", 2, EID),
       "id opaco: seis letras minúsculas, el mismo con la misma semilla")
    ok(o != A.opaco("s2", 2, EID) and o != A.opaco("s1", 3, EID) and o != A.opaco("s1", 2, EID + "x"),
       "id opaco: cambia con la semilla, el lote y el id")
    n = int(hashlib.sha256(f"s1:ids_opacos:lote2:{EID}".encode()).hexdigest(), 16)
    ok(o == "".join(chr(97 + (n // 26 ** k) % 26) for k in range(6)), "id opaco: se reproduce con la derivación declarada")

    # 2. dígitos de un número de punto o de un separador
    a2, b2 = span("6.3.2.2")
    ok(A.dentro_de_un_numero(TEXTO, a2 + 4, a2 + 5) and A.dentro_de_un_numero(TEXTO, a2 + 6, a2 + 7),
       "un dígito de «6.3.2.2» está dentro de un número")
    ok(not A.dentro_de_un_numero(TEXTO, *span("30")), "«30 días» no está dentro de un número")
    ok(A.dentro_de_un_numero("$ 1.000.000", 4, 7), "un grupo de «1.000.000» está dentro de un número")
    ok(not A.dentro_de_un_numero("es de 30. Los", 6, 8), "«30» al final de la oración no está dentro de un número")
    ok(A.literal(TEXTO, (span("5 %")[0], span("5 %")[0] + 1), "5 %") == span("5 %"), "literal: «5 %» completo")
    ok(A.literal(TEXTO, span("5 veces")[:1] + (span("5 veces")[0] + 1,), "5 %") is None,
       "literal: el «5» de «5 veces» no es el literal «5 %»")

    # 3. qué resalta la ficha (C24 y la decisión del 10/10/2026)
    el = {"tramo": "5 %", "valor": "5", "unidad": "porcentaje", "origen": "e1", "regla_comparacion": "maximo",
          "tramo_verificado": "exacta"}
    con({"chunk_id": CID, "spans": [span("5")], "metodo": "cuantia_dentro_del_tramo_de_e1"})
    r = A.ubicar_v1(NODO, 0, el)
    ok(r["spans"] == [span("5 %")] and not r["avisos"], "con el tramo de E1: resalta la cuantía, con su signo")
    con({"chunk_id": CID, "spans": [span("5"), span("5", span("5")[1])], "metodo": "cuantia_sola"})
    r = A.ubicar_v1(NODO, 0, el)
    ok(r["spans"] == [span("5 %")], "sin el tramo de E1: «5 %» una vez literal y «5» suelto en «5 veces»: resalta el literal")
    el2 = {**el, "tramo": "2", "valor": "2", "unidad": "veces"}
    con({"chunk_id": CID, "spans": [], "metodo": "cuantia_sola"},
        [(CID, TEXTO.replace("5 veces", "2 veces"), {**CH, "texto": TEXTO.replace("5 veces", "2 veces")})])
    r = A.ubicar_v1(NODO, 0, el2)
    t2 = TEXTO.replace("5 veces", "2 veces")
    ok(len(r["spans"]) == 1 and t2[slice(*r["spans"][0])] == "2" and r["spans"][0][0] == t2.index("2 veces"),
       "sin el tramo de E1: los «2» de «6.3.2.2» no cuentan, y el «2» de «2 veces» es el único")
    t3 = TEXTO + " Otro plazo de 30 días."
    con({"chunk_id": CID, "spans": [], "metodo": "cuantia_sola"}, [(CID, t3, {**CH, "texto": t3})])
    r = A.ubicar_v1(NODO, 0, {**el, "tramo": "30 días", "valor": "30", "unidad": "dias"})
    ok(r["spans"] == [] and r["guardado"] == "30 días" and "más de una vez" in r["avisos"][0],
       "la cuantía aparece dos veces y el tramo no indica cuál: no resalta, lo dice y muestra lo guardado")
    con({"chunk_id": CID, "spans": [span("5")], "metodo": "cuantia_dentro_del_tramo_de_e1"})
    r = A.ubicar_v1(NODO, 0, {**el, "tramo_verificado": "no"})
    ok(r["spans"] == [] and r["guardado"] == "5 %" and "no está verificado" in r["avisos"][0],
       "tramo no verificado: no resalta, lo dice y muestra lo guardado")
    con({"chunk_id": None, "spans": [], "metodo": "no_ubicada"})
    r = A.ubicar_v1(NODO, 0, {**el, "tramo": "7 %", "valor": "7"})
    ok(r["spans"] == [] and "no se ubica" in r["avisos"][0], "no se ubica: no resalta, lo dice y muestra lo guardado")
    elv = {"tramo": "no podrán superar el 5 % de su capital inventado", "comparacion": "maximo_inclusivo", "origen": "e1",
           "regla_comparacion": "limite_relativo:marcador", "tramo_verificado": "exacta"}
    con({"chunk_id": CID, "spans": [span("no podrán superar el 5 % de su capital inventado")],
         "metodo": "tramo_del_elemento (validador)"})
    r = A.ubicar_v1(NODO, 0, elv)
    ok(r["spans"] == [span("no podrán superar el 5 % de su capital inventado")], "validador: resalta el tramo del elemento")
    con({"chunk_id": CID, "spans": [span("no podrán superar")], "metodo": "tramo_del_elemento (validador)",
         "nota": "1 de 2 segmentos del tramo no se ubican en E0"})
    r = A.ubicar_v1(NODO, 0, elv)
    ok(r["spans"] == [] and r["guardado"] == elv["tramo"], "validador con un segmento sin ubicar: no resalta y muestra lo guardado")

    # 4. la ficha v1 (C23, C24, C27) y su control
    con({"chunk_id": CID, "spans": [span("5")], "metodo": "cuantia_dentro_del_tramo_de_e1",
         "tramos_e1": [(CID, "no podrán superar el 5 % de su capital inventado")]})
    nodo = {**NODO, "properties": {**NODO["properties"], "umbrales": [el]}}
    md, meta = A.ficha_v1("L2-01", 1, 20, o, nodo, 0, el, 2, None)
    ok(A.control_ficha_v1(md, EID, nodo, el, meta) == [], "ficha v1: el control no encuentra nada")
    ok(not any(x in md for x in (nodo["label"], nodo["properties"]["descripcion"], "Condicion", EID, "Tramos de umbral",
                                 "maximo", "porcentaje")),
       "ficha v1: sin etiqueta, descripción, tipo, ids, tramos de E1 ni valores del grafo")
    ok(A.resaltados(md) == ["5 %"] and f"`{o}`" in md, "ficha v1: un resaltado, la cuantía, y el id opaco")
    md_mal = md.replace("## Página del PDF", f"- Nodo: Condicion, «{nodo['label']}»\n\n## Página del PDF")
    ok(len(A.control_ficha_v1(md_mal, EID, nodo, el, meta)) >= 2, "control: una ficha con el tipo y la etiqueta no pasa")
    ok(A.control_ficha_v1(md.replace("importe mínimo", "importe máximo"), EID, nodo, el, meta) != [],
       "control: una ficha con el texto de E0 cambiado no pasa")
    ok(A.control_ficha_v1(md, EID, nodo, {**el, "regla_comparacion": "capital"}, meta) == [],
       "control: un valor de campo que es una palabra de la norma citada no frena")
    md_dos = md.replace("30 días", "⟦30 días⟧")
    ok(A.control_ficha_v1(md_dos, EID, nodo, el, meta) != [], "control: una ficha con dos resaltados no pasa")
    md27, meta27 = A.ficha_v1("L2-05", 5, 20, A.opaco("s1", 2, EID + "b"), nodo, 0, el, 2, "L2-01")
    ok("Misma unidad que otra ficha (C27)" in md27 and "L2-01" in md27 and meta27["informada_por"] == "L2-01",
       "C27: la ficha declara la ficha anterior de la misma unidad")
    con({"chunk_id": CID, "spans": [span("5")], "metodo": "cuantia_dentro_del_tramo_de_e1"})
    mdn, metan = A.ficha_v1("L2-02", 2, 20, o, nodo, 0, {**el, "tramo_verificado": "no"}, 2, None)
    ok(A.control_ficha_v1(mdn, EID, nodo, {**el, "tramo_verificado": "no"}, metan) == [] and A.resaltados(mdn) == []
       and "lo que el elemento guarda como cuantía: «5 %»" in mdn, "ficha sin resaltado: lo dice y muestra lo guardado")

    con({"chunk_id": None, "spans": [], "metodo": "no_ubicada"})
    el7 = {**el, "tramo": "7 %", "valor": "7"}
    md7, meta7 = A.ficha_v1("L2-03", 3, 20, o, nodo, 0, el7, 2, None)
    ok(A.control_ficha_v1(md7, EID, nodo, el7, meta7) == [] and A.resaltados(md7) == []
       and "lo que el elemento guarda como cuantía: «7 %»" in md7, "ficha de un elemento que no se ubica: pasa el control")
    for k, mot in enumerate(("el tramo del elemento no está verificado contra el texto", "el elemento no se ubica en el texto "
                             "de E0 de la unidad", "la cuantía aparece más de una vez en el texto y el tramo del elemento no "
                             "indica cuál")):
        ok(A.control_sin_campos(f"- {mot}; {A.NO_RESALTA}", {}) == [], f"el aviso {k + 1} no nombra un campo oculto")

    propio, her = "3.5.3. Plazo de los 3", "(tres) días hábiles a la fecha de la solicitud."
    chp = {"id": CID2, "titulo": "Punto partido", "paginas": [1], "texto": propio,
           "herencia": [{"tipo": "intro", "unidad_origen": "3.5.3", "texto": her, "paginas": [1]}]}
    tp_ = propio + "\n" + her
    a3 = tp_.index("3", len("3.5.3. Plazo de los "))
    con({"chunk_id": CID2, "spans": [(a3, a3 + 1)], "metodo": "cuantia_dentro_del_tramo_de_e1"}, [(CID2, tp_, chp)])
    el3 = {**el, "tramo": "3 (tres) días hábiles", "valor": "3", "unidad": "dias"}
    nodo3 = {**nodo, "provenance": {**nodo["provenance"], "chunk_id": CID2}, "provenances": [{**nodo["provenance"], "chunk_id": CID2}]}
    md3, meta3 = A.ficha_v1("L2-04", 4, 20, o, nodo3, 0, el3, 2, None)
    ok(A.control_ficha_v1(md3, EID, nodo3, el3, meta3) == [] and A.resaltados(md3) == ["3", "(tres) días hábiles"],
       "una cuantía que E0 partió entre dos bloques se resalta en dos piezas y pasa el control")

    # 5. formulario del paso 1 v1 (C7, C23, C25, C26, C27)
    form = F.formulario_v1("prueba", [("L2-01", o, False, None), ("L2-02", "qwerty", True, None), ("L2-03", "asdfgh", False, "L2-01")])
    leido = F.leer(form)
    ok(list(leido) == [o, "qwerty", "asdfgh"], "formulario v1: la cabecera es la etiqueta y el id opaco")
    ok("pertinencia" not in leido[o]["campos"] and "nota" in leido[o]["campos"] and "nota" in leido["qwerty"]["campos"],
       "formulario v1: sin la pertinencia, con la nota")
    ok(set(leido["qwerty"]["campos"]) == {c for c, _ in F.CAMPOS_VACIO}, "formulario v1: el vacío lleva la pregunta del §2.5")
    ok("Misma unidad de E0 que la ficha L2-01" in form, "formulario v1: la declaración de C27 en el bloque")
    ok("no nombra" in dict(F.CAMPOS_V1)["moneda"] and "remision generica" in dict(F.CAMPOS_V1)["destino_de_la_base"],
       "formulario v1: las opciones de C14 y C18")
    ok(A.control_formulario_v1(form, [{"etiqueta": "L2-01", "opaco": o}, {"etiqueta": "L2-02", "opaco": "qwerty"},
                                      {"etiqueta": "L2-03", "opaco": "asdfgh"}], [EID]) == [],
       "formulario v1: el control no encuentra nada")
    ok(A.control_formulario_v1(form + f"\n{EID}\n", [{"etiqueta": "L2-01", "opaco": o}, {"etiqueta": "L2-02", "opaco": "qwerty"},
                                                    {"etiqueta": "L2-03", "opaco": "asdfgh"}], [EID]) != [],
       "formulario v1: el control encuentra un id del grafo")

    # 6. paso 2 v1: la pertinencia primero (C7) y las diferencias con nota por fila (C26)
    fila_p = {"etiqueta": "L2-01", "opaco": o, "indice": 0, "etiqueta_nodo": nodo["label"],
              "tramos_e1": ["no podrán superar el 5 % de su capital inventado"],
              "tramo_e1_del_elemento": "no podrán superar el 5 % de su capital inventado", "resaltado": "5 %",
              "guardado": None, "cuantias_nodo": ["5 %", "30 días"]}
    tp = K.informe_pertinencia(2, [fila_p])
    lp = F.leer(tp)
    ok(set(lp[o]["campos"]) == {"pertinencia", "nota"} and "← el del elemento" in tp and "← este elemento" in tp,
       "pertinencia: la etiqueta, los tramos, los elementos del nodo, y solo la pertinencia y la nota")
    ok("maximo" not in tp and "porcentaje" not in tp, "pertinencia: sin valores del grafo de los demás campos")
    fila_d = {"etiqueta": "L2-01", "opaco": o, **K.comparar(
        {"valor": "5", "unidad": "porcentaje", "comparacion": "maximo_inclusivo", "fuera_de_lista": []},
        {"pertinencia": "pertinente", "valor": "6", "unidad": "horas", "moneda": "no aplica", "tipo_de_dias": "no aplica",
         "comparacion": "maximo_inclusivo", "base": "sin base", "destino_de_la_base": "no aplica", "no_decidible": "no"}, {})}
    td = K.informe_v1(2, [fila_d, {"etiqueta": "L2-02", "opaco": "qwerty", "vacio": True, "clase_vacio": "no es un umbral"}])
    ld = F.leer(td)
    ok({"clasificacion_valor", "nota_valor", "corrijo_mi_paso_uno_valor", "clasificacion_unidad", "nota_unidad",
        "nota_de_la_ficha"} <= set(ld[o]["campos"]) and "nota_de_la_ficha" in ld["qwerty"]["campos"],
       "diferencias: cada fila con su clasificación y su nota, y una nota por ficha")
    ok(K.clave("unidad (marca fuera_de_lista)") == "unidad_marca_fuera_de_lista", "diferencias: la clave de la fila")
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / "x.md"
        p.write_text("contenido", encoding="utf-8")
        try:
            K.leer_sellado(p, "0" * 64, "x")
            rechaza = False
        except SystemExit:
            rechaza = True
        ok(rechaza and K.leer_sellado(p, hashlib.sha256(b"contenido").hexdigest(), "x") == b"contenido",
           "lo sellado se lee solo con su sha256")

    malos = 0
    for b, q in R:
        print(("PASS" if b else "FAIL"), "|", q)
        malos += not b
    print(f"{len(R) - malos}/{len(R)}")
    if a.ejemplo:
        con({"chunk_id": CID, "spans": [span("5")], "metodo": "cuantia_dentro_del_tramo_de_e1",
             "tramos_e1": [(CID, "no podrán superar el 5 % de su capital inventado")]})
        md_e, _ = A.ficha_v1("L9-01", 1, 1, o, nodo, 0, el, 9, None)
        a.ejemplo.write_text(
            "# Ejemplo inventado del instrumento v1 (no es del marco)\n\nUn nodo, un texto y un elemento inventados, para ver el "
            "formato: la ficha del paso 1, su bloque del formulario, el bloque de la pertinencia y el de las diferencias. La "
            "página del PDF no existe.\n\n---\n\n" + md_e + "\n---\n\n"
            + F.formulario_v1("Formulario del paso 1 (ejemplo)", [("L9-01", o, False, None)]) + "\n---\n\n"
            + K.informe_pertinencia(9, [{**fila_p, "etiqueta": "L9-01"}]) + "\n---\n\n"
            + K.informe_v1(9, [{**fila_d, "etiqueta": "L9-01"}]), encoding="utf-8")
    return 1 if malos else 0


if __name__ == "__main__":
    raise SystemExit(main())
