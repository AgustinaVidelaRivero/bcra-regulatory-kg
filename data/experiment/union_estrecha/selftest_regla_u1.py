"""U-UNION-ESTRECHA, U1: selftest de regla_u1.py, rama por rama, con casos sintéticos (sin datos del corpus guardado).

Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B selftest_regla_u1.py <dir_fuentes>
<dir_fuentes>/code trae prompt_r2b.py y comun_e1.py (las funciones `bloque_lista` y `es_mini_chunk` del extractor,
tomadas por AST como en la pre-medición) y modelos_r2.py (la matriz r2).
"""
import sys

import premedicion_u1 as P
import regla_u1 as R

CASOS_ANUNCIO = [
    # (nombre, texto del bloque, forma, subforma, marca de excepción esperada, compatibles)
    ("S1 en la medida que + siguientes condiciones",
     "Las entidades podrán dar acceso al mercado, en la medida que se cumpla la totalidad de las siguientes condiciones:",
     "S", "S1", None, R.COMPATIBLES["S"]),
    ("S1 cada vez que + circunstancias",
     "La entidad deberá modificar la clasificación cada vez que tenga lugar alguna de las siguientes circunstancias:",
     "S", "S1", None, R.COMPATIBLES["S"]),
    ("S1 toda vez que + motivos",
     "El rechazo procederá toda vez que se observen por lo menos uno de los siguientes motivos:",
     "S", "S1", None, R.COMPATIBLES["S"]),
    ("S1 con subordinante al principio de la oración",
     "Cuando la falta de pago se deba a la existencia de al menos una de las siguientes situaciones:",
     "S", "S1", None, R.COMPATIBLES["S"]),
    ("S2 la principal antes del subordinante",
     "Dichas entidades podrán realizar operaciones de canje siempre que la contraparte sea:",
     "S", "S2", None, R.COMPATIBLES["S"]),
    ("S2 subordinante solo al final", "Serán atendidos los cheques presentados al cobro, cuando:",
     "S", "S2", None, R.COMPATIBLES["S"]),
    ("sin anuncio: el subordinante abre la oración y la lista es de la principal",
     "En la medida que corresponda a operaciones registradas quedan comprendidos:", None, None, None, ()),
    ("sin anuncio: subordinante antes de la última coma",
     "Podrán acceder cuando, en adición a los restantes requisitos aplicables, se verifique alguna de las siguientes "
     "situaciones:", None, None, None, ()),
    ("sin anuncio: subordinante en la oración anterior",
     "Podrán acceder siempre que cumplan lo previsto. La entidad deberá contar con:", None, None, None, ()),
    ("N siguientes requisitos (objeto de una obligación)",
     "La entidad deberá verificar el cumplimiento de los siguientes requisitos:", "N", "N", None,
     R.COMPATIBLES["N"]),
    ("N frase: condiciones especificadas a continuación",
     "Las entidades deberán verificar que se cumplan las condiciones especificadas a continuación:", "N", "N", None,
     R.COMPATIBLES["N"]),
    ("N recaudos", "podrá informarlo, efectuando una presentación que cumpla los siguientes recaudos:",
     "N", "N", None, R.COMPATIBLES["N"]),
    ("sin anuncio: situaciones sin subordinante",
     "Las entidades podrán también dar acceso en las siguientes situaciones:", None, None, None, ()),
    ("sin anuncio: en tanto por ciento",
     "Las tasas, en tanto por ciento con dos decimales, con el siguiente detalle:", None, None, None, ()),
    ("sin anuncio: casos",
     "Este requisito se considerará cumplimentado en los siguientes casos:", None, None, None, ()),
    ("excepción con S: no resultará aplicable cuando",
     "Este requisito no resultará aplicable cuando la operación encuadre en alguna de las siguientes situaciones:",
     "S", "S1", "no resultara aplicable", R.COMPATIBLES["EXC"]),
    ("excepción con N: excepto que + condiciones estipuladas",
     "Requerirá la conformidad previa del BCRA excepto que el deudor encuadre en alguna de las siguientes situaciones "
     "y se cumplan la totalidad de las condiciones estipuladas en cada caso:", "N", "N", "excepto",
     R.COMPATIBLES["EXC"]),
    ("excepción: quedarán exceptuados, en la oración final",
     "Quedarán exceptuados de la obligación de liquidación, en la medida que ingresen en plazo, los cobros de "
     "beneficiarias y se cumplan la totalidad de las siguientes condiciones:", "N", "N", "quedaran exceptuad",
     R.COMPATIBLES["EXC"]),
    ("palabra cortada en fin de línea",
     "Podrán computarse, siempre que se ob-\nserven los siguientes requi-\nsitos:", "S", "S1", None,
     R.COMPATIBLES["S"]),
    ("abreviatura Com. no corta la oración",
     "Conforme a la Com. «A» 1234, siempre que se cumplan las siguientes condiciones:", "S", "S1", None,
     R.COMPATIBLES["S"]),
    ("frontera de oración real",
     "Rige lo previsto en el punto 3.5. La entidad, siempre que se cumplan las siguientes condiciones:",
     "S", "S1", None, R.COMPATIBLES["S"]),
    ("dos puntos de ancho completo", "Podrán acceder siempre que se cumplan las siguientes condiciones：",
     "S", "S1", None, R.COMPATIBLES["S"]),
]


def casos_decidir():
    s = R.anuncio("Podrán acceder siempre que se cumplan las siguientes condiciones:")
    n = R.anuncio("La entidad deberá verificar los siguientes requisitos:")
    e = R.anuncio("Este requisito no resultará aplicable cuando se cumpla la totalidad de las siguientes condiciones:")
    nada = R.anuncio("Comprende los siguientes conceptos:")
    return [
        ("sin mini-chunk", (False, None, []), "sin_unidad_de_encabezado"),
        ("sin anuncio", (True, nada, [["P", "Potestad"]]), "sin_anuncio"),
        ("sin candidato", (True, s, []), "sin_candidato"),
        ("ambigua", (True, s, [["O", "Operacion"], ["P", "Potestad"]]), "ambigua"),
        ("ambigua con Restriccion", (True, s, [["P", "Potestad"], ["R", "Restriccion"]]), "ambigua"),
        ("S + Potestad", (True, s, [["P", "Potestad"]]), "union"),
        ("S + Obligacion", (True, s, [["B", "Obligacion"]]), "union"),
        ("S + Excepcion", (True, s, [["X", "Excepcion"]]), "union"),
        ("S + Restriccion", (True, s, [["R", "Restriccion"]]), "destino_no_compatible"),
        ("N + Operacion", (True, n, [["O", "Operacion"]]), "union"),
        ("N + Obligacion", (True, n, [["B", "Obligacion"]]), "destino_no_compatible"),
        ("EXC + Excepcion", (True, e, [["X", "Excepcion"]]), "union"),
        ("EXC + Potestad", (True, e, [["P", "Potestad"]]), "destino_no_compatible"),
        ("EXC + Obligacion", (True, e, [["B", "Obligacion"]]), "destino_no_compatible"),
    ]


def prov(cid):
    return {"to": "t", "chunk_id": cid, "punto": cid.split("::")[1]}


def grafo_sintetico():
    """Un TO «t» con cinco listas: anuncio S con un candidato, N con Obligacion, encabezado de título, sin anuncio y
    dos candidatos (uno por la parte de un mini-chunk partido)."""
    intro = lambda u, texto: {"tipo": "intro", "unidad_origen": u, "texto": texto}  # noqa: E731
    chunks = {}

    def mini(u, texto):
        chunks[f"t::{u}::intro"] = {"id": f"t::{u}::intro", "to": "t", "tipo": "mini_chunk", "unidad": u,
                                    "rol_bloque": "intro", "texto": texto, "herencia": []}

    def item(cid, herencia):
        chunks[cid] = {"id": cid, "to": "t", "tipo": "punto", "unidad": cid.split("::")[1], "texto": "a) algo.",
                       "herencia": herencia}

    t1 = "Las entidades podrán acceder, siempre que se cumplan los siguientes requisitos:"
    mini("1", t1)
    item("t::1.1", [intro("1", t1)])
    t2 = "La entidad deberá verificar los siguientes requisitos:"
    mini("2", t2)
    item("t::2.1", [intro("2", t2)])
    item("t::3.1", [{"tipo": "encabezado", "unidad_origen": "3", "texto": "3. Requisitos. Siempre que:"}])
    t4 = "Comprende los siguientes conceptos:"
    mini("4", t4)
    item("t::4.1", [intro("4", t4)])
    t5 = "Las entidades podrán operar, en la medida que se verifiquen las siguientes condiciones:"
    mini("5", t5)
    item("t::5.1", [intro("5", t5), {"tipo": "cierre", "unidad_origen": "5", "texto": "Lo anterior rige desde X."}])
    item("t::6", [])  # punto que no es ítem
    nodos = [
        {"id": "P1", "type": "Potestad", "provenance": prov("t::1::intro")},
        {"id": "C1", "type": "Condicion", "provenance": prov("t::1.1")},
        {"id": "B2", "type": "Obligacion", "provenance": prov("t::2::intro")},
        {"id": "C2", "type": "Condicion", "provenance": prov("t::2.1")},
        {"id": "C3", "type": "Condicion", "provenance": prov("t::3.1")},
        {"id": "D4", "type": "Definicion", "provenance": prov("t::4::intro")},
        {"id": "C4", "type": "Condicion", "provenance": prov("t::4.1")},
        {"id": "P5", "type": "Potestad", "provenance": prov("t::5::intro")},
        {"id": "O5", "type": "Operacion", "provenance": prov("t::9"),
         "provenances": [prov("t::9"), prov("t::5::intro::parte2")]},
        {"id": "C5", "type": "Condicion", "provenance": prov("t::5.1::parte1")},
        {"id": "C6", "type": "Condicion", "provenance": prov("t::6")},
        {"id": "C7", "type": "Condicion", "provenance": prov("t::1.1")},
        {"id": "X8", "type": "Excepcion", "provenance": prov("t::1.1")},
        {"id": "C9", "type": "Condicion", "provenance": prov("t::1::intro")},
    ]
    aristas = [{"source": "C7", "target": "P1", "relation": "condicion_de"}]
    esperado = {"C1": ("union", "P1"), "C2": ("destino_no_compatible", None), "C3": ("sin_unidad_de_encabezado", None),
                "C4": ("sin_anuncio", None), "C5": ("ambigua", None)}
    return {"nodes": nodos, "edges": aristas}, chunks, esperado


def main():
    fuentes = sys.argv[1]
    ok = fallos = 0

    def chequear(nombre, cond, detalle=""):
        nonlocal ok, fallos
        if cond:
            ok += 1
        else:
            fallos += 1
            print(f"FALLA {nombre}: {detalle}")

    for nombre, texto, forma, subforma, exc, comp in CASOS_ANUNCIO:
        an = R.anuncio(texto)
        chequear(nombre, (an["forma"], an["subforma"], an["marca_excepcion"], R.compatibles(an))
                 == (forma, subforma, exc, comp), an)
    try:
        R.anuncio("Bloque sin dos puntos.")
        chequear("bloque sin «:» levanta error", False)
    except ValueError:
        chequear("bloque sin «:» levanta error", True)
    for nombre, args, esperado in casos_decidir():
        chequear("decidir: " + nombre, R.decidir(*args) == esperado, R.decidir(*args))
    cod = P.cargar_codigo(fuentes)
    chequear("rango de condicion_de = matriz r2", tuple(sorted(cod["rango"])) == tuple(sorted(R.RANGO_CONDICION_DE)),
             cod["rango"])
    kg, chunks, esperado = grafo_sintetico()
    registro, aristas, encabezados = R.aplicar(kg, chunks, cod["bloque_lista"], cod["es_mini_chunk"])
    obtenido = {f["id"]: (f["resultado"], f["destino"]) for f in registro}
    chequear("aplicar: filas y resultados", obtenido == esperado, obtenido)
    chequear("aplicar: una arista derivada", aristas == [{
        "source": "C1", "target": "P1", "relation": "condicion_de", "provenance": prov("t::1.1"),
        "provenances": [prov("t::1.1")], "rol_fuente": "union_item_encabezado"}], aristas)
    chequear("aplicar: arista sin marcas de E3", all(not ({"no_verificada_e3", "coherencia_tipo_predicado",
                                                           "properties"} & set(a)) for a in aristas))
    chequear("aplicar: candidatos por parte de mini-chunk",
             next(f for f in registro if f["id"] == "C5")["candidatos"] == [["O5", "Operacion"], ["P5", "Potestad"]])
    chequear("aplicar: encabezados", sorted(encabezados) == ["t::1[intro]", "t::2[intro]", "t::3[encabezado]",
                                                            "t::4[intro]", "t::5[intro]"], sorted(encabezados))
    chunks_mal = dict(chunks)
    chunks_mal["t::1::intro bis"] = dict(chunks["t::1::intro"], id="t::1::intro bis")
    try:
        R.aplicar(kg, chunks_mal, cod["bloque_lista"], cod["es_mini_chunk"])
        chequear("dos mini-chunks para un bloque levanta error", False)
    except ValueError:
        chequear("dos mini-chunks para un bloque levanta error", True)
    print(f"selftest_regla_u1: {ok} OK, {fallos} fallas")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
