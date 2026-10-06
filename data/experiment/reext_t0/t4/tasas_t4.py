"""U-REEXT-T0, T4, segundo tramo: las tasas de los puntos 1 y 5 a 8 sobre la marca adjudicada. Lee las fichas del primer
tramo (salida/fichas_punto*.json, commiteadas en be6b074) y la adjudicación de la autora (adjudicacion_autora.json,
volcada antes de computar); la marca adjudicada es la de la adjudicación donde la hay y, si no, la propuesta de la
ficha. Escribe salida/tasas_t4.json y salida/tasas_t4.md. USD 0, sin red.

  Intervalo: Wilson al 95 % con z = 1,959964, la fórmula de la enmienda al protocolo entre tandas del 04/10/2026
  (docs/enmienda_protocolo_entre_tandas_2026-10-04_cola_humana.md, §2, firmada en 8d01b04).
  Punto 1: unidades con error sobre 30 y la regla del §1, punto 6, de esa enmienda (con muestra: se dispara si el
    límite superior supera 0,25).
  Punto 5: fracciones por grupo; la variación contra P5 es la de la ficha.
  Punto 6: fracciones por tipo y rol y por lista; ctacte::3.2 aparte; y, aparte, los encabezados de ext::3.13.1 y
    ext::3.6.1 leídos con el criterio de b2 (lectura mía, sin adjudicar; la cifra sellada no cambia).
  Punto 7: la tasa del criterio sellado por unidad y la medida por supuesto (decisión 6 de la autora, posterior al
    resultado): los supuestos de la fase A (salida/grupo_c_fase_a.md) de las 30 unidades, cada uno anclado a su fila
    por un fragmento literal, en cinco clases. La clasificación es mía, de la extracción final ya leída en las fichas;
    una cláusula de excepción extraída como Excepcion con su relación cuenta en la primera clase.
  Punto 8: normativas con y sin remisiones puras (decisión 2), habilitantes, el tramo heredado aparte (decisión 5),
    y la estimación al universo de cada grupo (733 y 404) por la fracción de normativas con el tramo propio, con el
    intervalo de Wilson por N, bajo el supuesto de muestra aleatoria simple dentro de cada grupo.

Uso (desde la raíz de una copia): python -B data/experiment/reext_t0/t4/tasas_t4.py
"""
from __future__ import annotations

import hashlib
import json
import re
from collections import Counter, OrderedDict
from math import sqrt
from pathlib import Path

AQUI = Path(__file__).resolve().parent
SAL = AQUI / "salida"
Z = 1.959964
UMBRAL_COLA = 0.25
POBLACION_8 = {"sin_marca": 733, "con_marca": 404}
SHA_FICHAS = {  # sha256 de las fichas en be6b074 (precondición b del segundo tramo)
    "fichas_punto1_cola.json": "9e8e5514eda2c457b1af481365d88cdb22f090fb00e2b68c894f5f884c1e1ba5",
    "fichas_punto5_p4b.json": "06af7524b90076a7c2403515d2a7def26876f1b4527b65987217b0b5f9e02235",
    "fichas_punto6_listas.json": "a1cde88301b25c7170b3a96f0fb999122bd2942b5731646f1a667fad49809d63",
    "fichas_punto7_grupo_c.json": "f93cda8e0fb674cce24ce9d5f06ba16f52c1c5ae8f4b7efdfe4d8f5b244c77a4",
    "fichas_punto8_omisiones.json": "077a690da539469398748747ce8d6e3b0359b9d754bc1d1a3001fc0cb1ba0c0a",
}
SHA_FASE_A = "5f7812d9ae132905a7bcfb0ad5124210b59bd0198171c00b55ffb7a0c7b3b6ec"
C, N = "cumple", "no_cumple"

# ---------------------------------------------------------------------- punto 6: encabezados b1 con la forma de b2
# Lectura mía, sin adjudicar: el criterio de b2 para el encabezado es la norma unida a su excepción.
ENCABEZADOS_B2 = {
    "ext::3.13.1::intro": (C, "la Obligacion e3 de la conformidad previa y la Excepcion e4, unidas por "
                              "exceptua_obligacion"),
    "ext::3.6.1::intro": (C, "la Restriccion e1 de la prohibición y la Excepcion e2, unidas por exceptua"),
}

# ------------------------------------------------------------------------------- punto 7: medida por supuesto
R, DN, FU, OM, SR = "condicion_con_relacion", "dentro_de_norma", "fusionado", "omitido", "sin_relacion"
CLASES_7 = OrderedDict([
    (R, "Condicion con su relación hacia la norma que condiciona (o Excepcion con su relación, si es una cláusula de "
        "excepción)"),
    (DN, "dentro de una norma: en la descripción o el tramo de otra entidad, o extraído como una norma de otro tipo"),
    (FU, "fusionado: una Condicion junta el supuesto con otro supuesto o con su norma"),
    (OM, "omitido: sin extraer, o solo en una omisión"),
    (SR, "sin relación: Condicion (o Excepcion) sin relación hacia la norma que condiciona"),
])
SUBTIPOS_SR = OrderedDict([
    ("norma_en_heredado", "la norma que condiciona está fuera de la unidad, en el texto heredado"),
    ("norma_presente", "la norma está en la unidad y la Condicion no tiene relación hacia ella"),
    ("norma_no_emitida", "la norma está en el texto propio pero no se emitió como entidad"),
])
# unidad → [(fragmento literal de su fila de la fase A, miembros o None, clase, subtipo, dónde quedó)]
SUPUESTOS_7 = {
    "ext::10.5.5.2": [
        ("i) control de cambios", None, R, "", "e2 Condicion → e1 Operacion"),
        ("ii) insolvencia (con a y b)", None, R, "", "e3 Condicion → e1"),
        ("a hasta USD 100.000", None, R, "", "e4 Condicion con el umbral → e1"),
        ("b acciones judiciales", None, R, "", "e5 Condicion → e1"),
        ("percepción en moneda extranjera", None, DN, "", "dentro de la Obligacion e7")],
    "ext::10.4.4": [
        ("emitidas desde el 13/12/23", None, R, "", "e2 Condicion con el umbral → e3 Obligacion"),
        ("desde el 14/04/25", None, R, "", "e6 Condicion con el umbral → e7 Potestad"),
        ("con pagos a la vista", None, DN, "", "dentro de la Potestad e7"),
        ("sin oficialización a 90 días", None, R, "", "e10 Condicion con el umbral → e11 Obligacion")],
    "polcre::7.1.2": [
        ("financiaciones de más de $ 30.000 millones", None, SR, "norma_en_heredado",
         "c1 Condicion con el umbral, sin relación; la norma («Se encuentran comprendidos… los clientes… que reúnan "
         "concurrentemente las siguientes condiciones») está en el texto heredado"),
        ("pases o cauciones en 90 días", None, SR, "norma_en_heredado", "c2 Condicion con el umbral, sin relación; ídem"),
        ("declaración jurada contra la Central de deudores", None, R, "",
         "c3 Condicion → o1 Obligacion (un solo supuesto, por la adjudicación)"),
        ("MiPyME", None, R, "", "e1 Excepcion —exceptua_obligacion→ o1")],
    "pro::2.3.5.1": [
        ("conceptos i) a vii)", ["i)", "ii)", "iii)", "iv)", "v)", "vi)", "vii)"], DN, "",
         "cada concepto como Restriccion (e2 a e8) hacia la Operacion, no como Condicion del reintegro"),
        ("plazo por reclamo", None, DN, "", "dentro de la Obligacion e9"),
        ("por constatación", None, DN, "", "dentro de la Obligacion e10"),
        ("tasa no disponible", None, OM, "", "sin extraer"),
        ("cuenta a la vista", None, DN, "", "dentro de la Obligacion e13"),
        ("si no fuera posible", None, DN, "", "dentro de la Obligacion e14")],
    "cap::6.2.3.5": [
        ("instrumentos idénticos", None, R, "", "e2 Condicion → e1 Operacion"),
        ("futuro con gama de instrumentos", None, DN, "", "dentro de la Restriccion e4"),
        ("a) futuros a 7 días", None, DN, "", "dentro de la Restriccion e9, con el umbral"),
        ("b) swaps y FRAs", None, DN, "", "dentro de la Restriccion e10"),
        ("c) tramos de fechas", None, DN, "", "dentro de las Restriccion e11 a e13"),
        ("futuros sobre títulos", None, R, "", "e15 Excepcion —exceptua→ e14 Restriccion")],
    "ext::10.3.6": [
        ("emitidas desde el 13/12/23 (más 15 días)", None, R, "", "e4 Condicion con el umbral → e5 Obligacion"),
        ("desde el 14/04/25", None, R, "", "e8 Condicion con el umbral → e9 Obligacion"),
        ("con pagos a la vista", None, R, "", "e10 Condicion → e9")],
    "cla::6.5.3.10": [
        ("sin cancelar el 15 %", None, SR, "norma_en_heredado",
         "c2 Condicion con el umbral, hacia o1 (el cómputo de las garantías) y no hacia la norma que condiciona, la "
         "clasificación «Con problemas», que está en el texto heredado"),
        ("acuerdo alcanzado en alto riesgo o irrecuperable", None, SR, "norma_en_heredado", "c3 Condicion hacia o1; ídem"),
        ("acuerdos de más de 2,5 veces el importe de referencia", None, R, "", "c4 Condicion con el umbral → p1 Potestad")],
    "ext::7.9.4": [
        ("endeudamientos con cuentas de garantía", None, DN, "", "dentro de la Obligacion e3"),
        ("proyectos del 7.9.2", None, R, "", "e5 Condicion → e6 Obligacion"),
        ("proyecto sin aprobación de la Ley 26.360", None, DN, "", "dentro de la Obligacion e8")],
    "cla::7.2.2.1": [
        ("cancelado el 10 %", None, SR, "norma_presente",
         "e2 Condicion con el umbral, sin relación hacia la Definicion e1 de la categoría"),
        ("pago de 1 cuota", None, R, "", "e4 Condicion con el umbral → e3 Operacion"),
        ("pago único o irregular con 5 %", None, R, "", "e5 Condicion con el umbral → e3"),
        ("financiación adicional sin cancelar", None, DN, "", "dentro de la Restriccion e6"),
        ("atrasos de más de 31 días", None, R, "", "e7 Condicion con el umbral → e8 Operacion")],
    "cap::3.1.14.1": [
        ("refinanciación distribuida", None, DN, "", "dentro de la Obligacion e3"),
        ("valores residuales no significativos", None, DN, "", "dentro de la Obligacion e3"),
        ("minoristas 5 años", None, FU, "", "e8 Condicion junta el supuesto y la norma (5 años), sin relación"),
        ("resto 7", None, FU, "", "e9 Condicion junta el supuesto y la norma (7 años), sin relación"),
        ("salvo el período de 2 años", None, DN, "", "dentro de la Obligacion e11"),
        ("condiciones a) a d)", ["a)", "b)", "c)", "d)"], DN, "", "cada condición como Obligacion (e11 a e14)")],
    "cla::7.2.4": [
        ("concurso con 20 % o más", None, DN, "", "dentro de la Definicion e2"),
        ("entre 5 % y 20 % con 90 días", None, DN, "", "dentro de la Definicion e2"),
        ("levantamiento del pedido", None, DN, "", "dentro de la Potestad e3"),
        ("refinanciados", None, DN, "", "dentro de la Operacion e5"),
        ("más de 540 días", None, DN, "", "dentro de la Operacion e6"),
        ("atrasos de más de 31 días", None, DN, "", "dentro de la Operacion e9")],
    "ext::14.5.7": [
        ("i) a iii) en la medida que", ["i)", "ii)", "iii)"], R, "", "e2, e6 y e9 Condicion → e1 Operacion"),
        ("al menos 90 % del FOB", None, R, "", "e3 Condicion con el umbral → e1"),
        ("en caso de no disponer la documentación", None, DN, "", "dentro de la Obligacion e7"),
        ("VPU con cobros de exportaciones", None, DN, "", "dentro de la Obligacion e12")],
    "cla::6.5.5.9": [
        ("deuda de más del 2,5 % de la RPC o del importe de referencia", None, DN, "",
         "como Restriccion e2 («no podrá exceder»), con el umbral"),
        ("excepción de concurso hasta 540 días", None, R, "", "e4 Excepcion con el umbral —exceptua_obligacion→ e3"),
        ("siempre que haya informe", None, R, "", "e5 Condicion → e4 Excepcion"),
        ("primera declaración", None, FU, "", "e6 Condicion junta la primera declaración y las actualizaciones"),
        ("actualizaciones", None, FU, "", "ídem, e6")],
    "cla::7.2.3": [
        ("sin cancelar el 10 %", None, SR, "norma_presente",
         "e2 Condicion con el umbral, sin relación hacia la Definicion e1 de la categoría"),
        ("pago de 2 cuotas", None, R, "", "e4 Condicion con los umbrales → e6 Potestad"),
        ("pago único o irregular con 5 %", None, R, "", "e5 Condicion con el umbral → e6"),
        ("financiación adicional sin cancelar", None, DN, "", "dentro de la Restriccion e8"),
        ("atrasos de más de 31 días", None, DN, "", "dentro de la Obligacion e9, con el umbral")],
    "cap::2.1": [
        ("en tanto no se comunique la calificación", None, FU, "",
         "e4 Condicion lleva el supuesto y la consecuencia (k = 1,03), sin relación"),
        ("el cronograma opera desde que las obras se usan económicamente", None, DN, "",
         "dentro de las Obligacion e19 a e21")],
    "pro::3.1.3": [
        ("presentación por teléfono o Internet", None, DN, "", "dentro de la Obligacion e7"),
        ("presentante que no recibe el número automáticamente", None, DN, "", "dentro de la Obligacion e8")],
    "cap::7.3.2": [
        ("grupo B (17 %)", None, DN, "", "dentro de la Restriccion e1"),
        ("calificación 1, 2 o 3 (11 %)", None, R, "", "e3 Condicion → e2 Restriccion"),
        ("calificación 1 o 2 (7 %)", None, R, "", "e5 Condicion → e4 Restriccion")],
    "ext::4.1.3.2": [
        ("emisoras no financieras", None, OM, "", "sin extraer"),
        ("pago en día inhábil", None, FU, "",
         "e3 Condicion junta la regla del tipo de cambio, el pago en pesos y el día inhábil")],
    "cap::3.1.11.3": [
        ("i) a iii) según D, A y KA", ["i)", "ii)", "iii)"], DN, "", "dentro de las Restriccion e2 a e4"),
        ("si no existiera la posición pari passu", None, DN, "", "dentro de la Operacion e5"),
        ("mínimos por STC", None, DN, "", "dentro de las Restriccion e6 a e8"),
        ("look-through menor que el mínimo", None, R, "", "e10 Excepcion —exceptua→ e6, e7 y e8")],
    "ext::3.16.3.6": [
        ("garantía desde el vencimiento", None, DN, "", "dentro de la Obligacion e3"),
        ("fondos usados en 10 días", None, DN, "", "dentro de la Obligacion e4, con el umbral"),
        ("repatriación a 1 año", None, R, "", "e6 Condicion con los umbrales → e4 Obligacion"),
        ("BOPREAL hasta el monto suscripto", None, DN, "", "dentro de la Obligacion e11"),
        ("valor de mercado que no supere la diferencia", None, DN, "", "dentro de la Obligacion e12")],
    "cap::6.3.2.2": [
        ("arbitrajes del a) (dos guiones)", ["primer guion", "segundo guion"], DN, "",
         "dentro de las Excepcion e6 y e7"),
        ("b) canasta de al menos 90 %", None, R, "", "e11 Condicion con el umbral → e9 Restriccion"),
        ("c) sólo si se tienen en cuenta los costos", None, R, "", "e14 Condicion → e13 Potestad")],
    "ext::4.1.3.1": [
        ("emisor entidad financiera", None, OM, "", "solo en una omisión meta_normativo"),
        ("pago en día inhábil", None, DN, "", "dentro de la Restriccion e2"),
        ("débito automático pactado", None, R, "", "e3 Condicion → e4 Restriccion")],
    "ric::9.1.3": [
        ("obligación del plan de regularización", None, R, "", "c1 Condicion → r1 Restriccion"),
        ("incrementos de más del 5 %", None, R, "", "c2 Condicion con el umbral → r1"),
        ("base consolidada", None, SR, "norma_no_emitida",
         "c3 Condicion sin relación: la norma que condiciona (la asimilación de las partidas) no se emite y queda en "
         "una omisión meta_normativo"),
        ("mientras persista", None, R, "", "c4 Condicion → r1")],
    "ext::8.4.2": [
        ("exportación de varios productos", None, DN, "", "dentro de la Operacion e2"),
        ("fecha no hábil", None, FU, "", "e4 Condicion lleva el supuesto y la consecuencia, sin relación"),
        ("ampliación del plazo", None, DN, "", "dentro de la Operacion e5"),
        ("reducción del plazo", None, DN, "", "dentro de la Restriccion e6")],
    "ric::6.1.2": [
        ("código 22600000 (tres «cuando»)", ["opciones de exclusión", "respaldo implícito", "cancelación anticipada"],
         DN, "", "dentro de la Operacion e12"),
        ("código 22700000", None, DN, "", "dentro de la Operacion e14"),
        ("código 21800000", None, DN, "", "dentro de la Operacion e7")],
    "cla::6.5.4.5": [
        ("bienes en pago", None, DN, "", "dentro de la Restriccion e2"),
        ("recategorización siempre que…", None, R, "", "e4 Condicion → e3 Potestad"),
        ("pago del 10 %", None, DN, "", "dentro de la Obligacion e5, con el umbral"),
        ("financiación adicional sin cancelar", None, R, "", "e8 Condicion → e7 Obligacion"),
        ("salvo otras pautas", None, R, "", "e9 Excepcion —exceptua_obligacion→ e7")],
    "cap::3.1.11.2": [
        ("estructura con SPE", None, DN, "", "dentro de la Obligacion e3"),
        ("si puede demostrar", None, SR, "norma_presente",
         "e4 Excepcion sin relación hacia e3 (la unidad no tiene ninguna relación)"),
        ("sintéticas con fondos aportados", None, DN, "", "dentro de la Obligacion e5"),
        ("previsión específica", None, DN, "", "dentro de la Obligacion e7"),
        ("desconocida para 5 % o menos", None, DN, "", "dentro de la Obligacion e14, con el umbral"),
        ("para más del 5 %", None, DN, "", "dentro de la Restriccion e15, con el umbral")],
    "ric::4.5.2": [
        ("«C» si es compra a término", None, DN, "", "dentro de la Obligacion e7"),
        ("«V» si es venta", None, DN, "", "dentro de la Obligacion e7")],
    "polcre::7.1::cierre": [
        ("reúne 7.1.1", None, R, "", "e1 Condicion → e4 Potestad"),
        ("no supera $ 30.000 millones", None, DN, "", "como Restriccion e2, con el umbral"),
        ("sin pases", None, DN, "", "como Restriccion e3, con el umbral"),
        ("desembolsos que no superen el importe", None, DN, "", "dentro de la Potestad e4"),
        ("conjuntos económicos", None, DN, "", "como Definicion e6")],
    "cla::6.5.5.2": [
        ("sin cancelación efectiva previa", None, DN, "", "dentro de la Restriccion e5"),
        ("pago del 15 %", None, R, "", "e7 Condicion con los umbrales → e6 Potestad"),
        ("financiación adicional sin cancelar", None, R, "", "e10 Condicion → e8 Restriccion")],
}


# --------------------------------------------------------------------------------------------------------- ayudas
def wilson(k: int, n: int) -> list[float]:
    p = k / n
    den = 1 + Z * Z / n
    centro = (p + Z * Z / (2 * n)) / den
    medio = Z * sqrt(p * (1 - p) / n + Z * Z / (4 * n * n)) / den
    return [round(max(0.0, centro - medio), 4), round(min(1.0, centro + medio), 4)]


def tasa(k: int, n: int) -> OrderedDict:
    return OrderedDict([("k", k), ("n", n), ("fraccion", f"{k}/{n}"), ("wilson95", wilson(k, n) if n else None)])


def fmt(t: dict) -> str:
    lo, hi = t["wilson95"]
    return f"{t['fraccion']} [{lo:.3f}; {hi:.3f}]".replace(".", ",")


def num(e: dict) -> str:
    lo, hi = e["intervalo"]
    return f"{e['estimacion']:.1f} [{lo:.1f}; {hi:.1f}]".replace(".", ",")


def leer(nombre: str) -> dict:
    crudo = (SAL / nombre).read_bytes()
    assert hashlib.sha256(crudo).hexdigest() == SHA_FICHAS[nombre], f"{nombre} no es la ficha de be6b074"
    return json.loads(crudo)


def adjudicadas(adj: dict, punto: int) -> dict:
    return {a["clave"]: a for a in adj["adjudicaciones"] if a["punto"] == punto}


# --------------------------------------------------------------------------------------------------------- puntos
def punto1(adj: dict) -> dict:
    f = leer("fichas_punto1_cola.json")["fichas"]
    a = adjudicadas(adj, 1)
    filas = []
    for x in f:
        marca = a[x["chunk_id"]]["marca_adjudicada"] if x["chunk_id"] in a else x["propuesta"]
        assert marca in ("con error", "sin error"), x["chunk_id"]
        filas.append({"n": x["n"], "chunk_id": x["chunk_id"], "propuesta": x["propuesta"], "adjudicada": marca,
                      "no_sostenido": x["no_sostenido"], "omisiones_aparte": x["omisiones_aparte"]})
    k = sum(r["adjudicada"] == "con error" for r in filas)
    t = tasa(k, len(filas))
    return OrderedDict([
        ("unidades", len(filas)), ("con_error", t), ("sin_error", len(filas) - k),
        ("regla", "enmienda al protocolo del 04/10/2026, §1, punto 6: con muestra, se dispara si el límite superior "
                  "de Wilson al 95 % de la tasa de error supera 0,25"),
        ("regla_se_dispara", t["wilson95"][1] > UMBRAL_COLA),
        ("salidas_de_la_enmienda", ["re-procesar las 74 unidades de la cola humana de la tanda 0",
                                    "sacar las 74 unidades del grafo evaluado de la tanda 0"]),
        ("eleccion", "PENDIENTE de la autora"),
        ("unidades_con_error", [{"chunk_id": r["chunk_id"], "no_sostenido": r["no_sostenido"]}
                                for r in filas if r["adjudicada"] == "con error"]),
        ("omisiones_aparte", [{"chunk_id": r["chunk_id"], "omision": r["omisiones_aparte"]}
                              for r in filas if r["omisiones_aparte"]]),
        ("cambios_por_la_adjudicacion", [{"chunk_id": r["chunk_id"], "propuesta": r["propuesta"],
                                          "adjudicada": r["adjudicada"]} for r in filas
                                         if r["propuesta"] != r["adjudicada"]])])


def punto5(adj: dict) -> dict:
    d = leer("fichas_punto5_p4b.json")
    assert not adjudicadas(adj, 5), "el punto 5 no tiene adjudicaciones: vale la propuesta"
    grupos = OrderedDict()
    for x in d["fichas"]:
        g = grupos.setdefault(x["grupo"], [0, 0])
        g[0] += x["marca"] == C
        g[1] += 1
    k = sum(v[0] for v in grupos.values())
    n = sum(v[1] for v in grupos.values())
    r = d["resumen"]
    return OrderedDict([
        ("regla", "reglas de marcado de P4b (marcas_p4b.py) sobre la respuesta de E1; vale la propuesta, sin segunda "
                  "lectura"),
        ("por_grupo", OrderedDict((g, tasa(*v)) for g, v in grupos.items())), ("total", tasa(k, n)),
        ("variacion_contra_p5", {"identicas_a_alguna_de_p5": r["identicas_a_alguna_de_p5"],
                                 "difieren_de_las_dos": n - r["identicas_a_alguna_de_p5"],
                                 "cambia_la_marca_contra_a": len(r["cambia_la_marca_contra_a"]),
                                 "cambia_la_marca_contra_b": len(r["cambia_la_marca_contra_b"])}),
        ("ext_10_3_6", "punto 5 «cumple» (regla de P4b sobre la respuesta de E1, marca de P5); punto 7 «cumple» sobre la "
                       "extracción final; con la regla del punto 7, la respuesta de E1 no cumpliría (decisión 1: se "
                       "declara, no se reconcilia)")])


def punto6(adj: dict) -> dict:
    d = leer("fichas_punto6_listas.json")
    a = adjudicadas(adj, 6)
    tabla, por_lista = OrderedDict(), OrderedDict()
    for x in d["fichas"]:
        marca = x["marca"]
        if x["chunk_id"] in a:
            assert a[x["chunk_id"]]["marca_adjudicada"] == marca, x["chunk_id"]
        k = ("aparte_" if x["aparte"] else "") + f"{x['tipo']}_{'encabezados' if x['rol'] == 'encabezado' else 'items'}"
        tabla.setdefault(k, [0, 0])
        tabla[k][0] += marca == C
        tabla[k][1] += 1
        por_lista.setdefault(x["lista"], {"tipo": x["tipo"], "aparte": x["aparte"], "cumple": 0, "de": 0})
        por_lista[x["lista"]]["cumple"] += marca == C
        por_lista[x["lista"]]["de"] += 1
    enc = {x["chunk_id"]: x["marca"] for x in d["fichas"] if x["rol"] == "encabezado" and x["tipo"] == "b1"
           and not x["aparte"]}
    con_b2 = dict(enc)
    con_b2.update({k: v[0] for k, v in ENCABEZADOS_B2.items()})
    return OrderedDict([
        ("regla", "b1: Excepcion del miembro con la norma exceptuada (ítems) y Definicion de la clase (encabezado); b2: "
                  "Condicion del supuesto con el cuantificador y la norma exceptuada (ítems) y la norma unida a su "
                  "excepción (encabezado); ctacte::3.2 aparte, declarada"),
        ("por_tipo_y_rol", OrderedDict((k, tasa(*v)) for k, v in tabla.items())),
        ("por_lista", por_lista),
        ("encabezados_b1_con_forma_de_b2", OrderedDict([
            ("nota", "ext::3.13.1 y ext::3.6.1 están selladas como b1 y sus encabezados tienen la forma de b2 (la norma "
                     "y una excepción general); lectura mía con el criterio de b2, sin adjudicar; la cifra sellada no "
                     "cambia; los ítems no se releyeron con el criterio de b2"),
            ("lectura", {k: {"marca_con_criterio_b2": v[0], "razon": v[1], "marca_sellada": enc[k]}
                         for k, v in ENCABEZADOS_B2.items()}),
            ("b1_encabezados_si_esos_dos_se_leen_como_b2", tasa(sum(v == C for v in con_b2.values()), len(con_b2))),
            ("si_las_dos_listas_fueran_b2", {
                "b1_encabezados": tasa(sum(v == C for k, v in enc.items() if k not in ENCABEZADOS_B2),
                                       len([k for k in enc if k not in ENCABEZADOS_B2])),
                "b2_encabezados": tasa(tabla["b2_encabezados"][0] + sum(v[0] == C for v in ENCABEZADOS_B2.values()),
                                       tabla["b2_encabezados"][1] + len(ENCABEZADOS_B2))})]))])


def fila_fase_a(cid: str, md: str) -> str:
    for linea in md.splitlines():
        partes = [p.strip() for p in linea.split("|")]
        if len(partes) > 4 and partes[2] == cid:
            return partes[4]
    raise KeyError(cid)


def punto7(adj: dict) -> dict:
    d = leer("fichas_punto7_grupo_c.json")
    md_a = (SAL / "grupo_c_fase_a.md").read_text(encoding="utf-8")
    assert hashlib.sha256(md_a.encode("utf-8")).hexdigest() == SHA_FASE_A, "grupo_c_fase_a.md no es el del primer tramo"
    a = adjudicadas(adj, 7)
    leidas = [x for x in d["fichas"] if x["mas_de_un_supuesto"]]
    assert sorted(x["chunk_id"] for x in leidas) == sorted(SUPUESTOS_7), "la medida por supuesto no cubre las 30"
    unidades = []
    for x in leidas:
        marca, etq = x["marca"], list(x["etiquetas"])
        if x["chunk_id"] in a:
            texto = a[x["chunk_id"]]["marca_adjudicada"]
            marca = N if texto.startswith(N) else C
            if "sin_relacion" in texto:
                etq = [e for e in etq if e != "fusion"] + ([] if "sin_relacion" in etq else ["sin_relacion"])
        unidades.append({"chunk_id": x["chunk_id"], "marca": marca, "etiquetas": etq})
    k = sum(u["marca"] == C for u in unidades)
    supuestos = []
    for cid, lista in SUPUESTOS_7.items():
        fila = fila_fase_a(cid, md_a)
        for frag, miembros, clase, sub, donde in lista:
            assert frag in fila, (cid, frag)
            assert (clase == SR) == bool(sub) and (not sub or sub in SUBTIPOS_SR), (cid, frag)
            for m in miembros or [None]:
                supuestos.append({"to": cid.split("::")[0], "chunk_id": cid, "fragmento_fase_a": frag, "miembro": m,
                                  "clase": clase, "subtipo_sin_relacion": sub, "donde": donde})
    marca_u = {u["chunk_id"]: u["marca"] for u in unidades}
    for cid in SUPUESTOS_7:  # una unidad que cumple tiene todos sus supuestos de la fase A en la primera clase
        if marca_u[cid] == C:
            assert all(s["clase"] == R for s in supuestos if s["chunk_id"] == cid), cid
    total = len(supuestos)
    por_clase = OrderedDict((c, tasa(sum(s["clase"] == c for s in supuestos), total)) for c in CLASES_7)
    assert sum(t["k"] for t in por_clase.values()) == total
    tos = sorted({s["to"] for s in supuestos})
    por_to = OrderedDict()
    for to in tos:
        ss = [s for s in supuestos if s["to"] == to]
        por_to[to] = OrderedDict([("unidades", len({s["chunk_id"] for s in ss})), ("supuestos", len(ss)),
                                  ("por_clase", OrderedDict((c, tasa(sum(s["clase"] == c for s in ss), len(ss)))
                                                            for c in CLASES_7))])
        assert sum(t["k"] for t in por_to[to]["por_clase"].values()) == len(ss)
    sub = OrderedDict((st, sum(s["subtipo_sin_relacion"] == st for s in supuestos)) for st in SUBTIPOS_SR)
    return OrderedDict([
        ("criterio_sellado", OrderedDict([
            ("regla", "criterio c de P4b: una Condicion por supuesto, con label, descripción, tramo y umbral del mismo "
                      "supuesto, hacia su norma; 30 unidades con más de un supuesto, decidido en la fase A sobre el texto"),
            ("cumple", tasa(k, len(unidades))),
            ("por_etiqueta_adjudicada", dict(Counter(e for u in unidades for e in u["etiquetas"]).most_common())),
            ("cambios_por_la_adjudicacion", {c: a[c]["marca_adjudicada"] for c in a})])),
        ("por_supuesto", OrderedDict([
            ("nota", "decisión 6 de la autora, posterior al resultado; la cifra del criterio sellado no cambia. "
                     "Supuestos: los de la fase A, anclados a su fila por un fragmento literal; un fragmento que nombra "
                     "una enumeración («i) a vii)», «a) a d)», «tres «cuando»», «dos guiones») cuenta cada miembro. "
                     "Clasificación mía sobre la extracción final ya leída en las fichas, sin segunda lectura"),
            ("clases", CLASES_7), ("total_supuestos", total), ("por_clase", por_clase),
            ("sin_relacion_por_subtipo", OrderedDict([("subtipos", SUBTIPOS_SR), ("cuentas", sub)])),
            ("por_documento", por_to), ("supuestos", supuestos)]))])


def punto8(adj: dict) -> dict:
    d = leer("fichas_punto8_omisiones.json")
    a = adjudicadas(adj, 8)
    filas = []
    for x in d["fichas"]:
        clave = f"{x['grupo']}:{x['n']}"
        r = {"grupo": x["grupo"], "n": x["n"], "chunk_id": x["chunk_id"], "en": x["en"], "normativo": x["normativo"],
             "clase": x["clase"], "habilitante": x["habilitante"], "remision_pura": False,
             "adjudicada": clave in a}
        if clave in a:
            ad = a[clave]
            assert ad["unidad"] == x["chunk_id"], clave
            m = ad["marca_adjudicada"]
            if m.startswith("remisión pura"):
                assert x["normativo"] and x["clase"] == "remisión", clave
                r["remision_pura"] = True
            else:
                r["normativo"] = m.startswith("normativa")
                r["clase"] = m.split(", ")[1]
                r["habilitante"] = "no habilitante" not in m
        filas.append(r)
    out = OrderedDict([("regla", "§1 de la enmienda 7 (44c6e1b); habilitante: pre-registro de ESQ-3b v2 (40493c9) y "
                                 "§4 de la enmienda 7; remisión pura (sin ninguna de las siete clases del contador) "
                                 "fuera de la cifra «sin remisiones» (decisión 2); tramo heredado aparte (decisión 5)"),
                       ("supuesto_de_la_estimacion", "muestra aleatoria simple de 30 dentro de cada grupo; estimación "
                                                     "= N × fracción, intervalo = N × Wilson")])
    for g in ("sin_marca", "con_marca"):
        fs = [r for r in filas if r["grupo"] == g]
        n = len(fs)
        nor = [r for r in fs if r["normativo"]]
        sin_rem = [r for r in nor if not r["remision_pura"]]
        prop = [r for r in fs if r["en"] == "propio"]
        her = [r for r in fs if r["en"] == "heredado"]
        assert len(prop) + len(her) == n
        npop = POBLACION_8[g]

        def est(k: int, base: int = n) -> OrderedDict:
            t = tasa(k, base)
            return OrderedDict([("fraccion", t["fraccion"]), ("estimacion", round(npop * k / base, 1)),
                                ("intervalo", [round(npop * t["wilson95"][0], 1), round(npop * t["wilson95"][1], 1)])])
        out[g] = OrderedDict([
            ("poblacion", npop), ("leidas", n),
            ("normativas_con_remisiones", tasa(len(nor), n)), ("normativas_sin_remisiones", tasa(len(sin_rem), n)),
            ("habilitantes", tasa(sum(r["habilitante"] for r in fs), n)),
            ("por_clase", dict(Counter(r["clase"] for r in nor).most_common())),
            ("tramo_heredado", OrderedDict([("leidas", len(her)), ("normativas", sum(r["normativo"] for r in her)),
                                            ("habilitantes", sum(r["habilitante"] for r in her))])),
            ("tramo_propio", OrderedDict([
                ("leidas", len(prop)),
                ("normativas_con_remisiones", tasa(sum(r["normativo"] for r in prop), n)),
                ("normativas_sin_remisiones", tasa(sum(r["normativo"] and not r["remision_pura"] for r in prop), n)),
                ("habilitantes", tasa(sum(r["habilitante"] for r in prop), n))])),
            ("estimacion_universo_tramo_propio", OrderedDict([
                ("con_remisiones", est(sum(r["normativo"] for r in prop))),
                ("sin_remisiones", est(sum(r["normativo"] and not r["remision_pura"] for r in prop))),
                ("habilitantes", est(sum(r["habilitante"] for r in prop)))])),
            ("estimacion_universo_tramo_heredado", est(len(her))),
            ("cambios_por_la_adjudicacion", [f"{r['grupo']}:{r['n']} {r['chunk_id']}" for r in fs if r["adjudicada"]])])
    e8 = out["sin_marca"]["estimacion_universo_tramo_propio"]
    out["se_le_escapan_al_contador"] = (f"la cifra del grupo sin marca, con el tramo propio: {num(e8['sin_remisiones'])} "
                                        f"sin remisiones y {num(e8['con_remisiones'])} con remisiones, de 733")
    return out


# ------------------------------------------------------------------------------------------------------- informe
def md(res: dict) -> list[str]:
    p1, p5, p6, p7, p8 = (res[f"punto_{i}"] for i in (1, 5, 6, 7, 8))
    L = ["# Tasas de T4 de U-REEXT-T0 (segundo tramo), sobre la marca adjudicada", "",
         "Wilson al 95 % (z = 1,959964); fracciones crudas, sin porcentajes. Adjudicación: `adjudicacion_autora.json`.", "",
         "## Punto 1, cola humana", "",
         f"- Unidades con error: **{fmt(p1['con_error'])}**. Regla del 25 %: el límite superior "
         f"{str(p1['con_error']['wilson95'][1]).replace('.', ',')} {'supera' if p1['regla_se_dispara'] else 'no supera'} "
         f"0,25: la regla {'se dispara' if p1['regla_se_dispara'] else 'no se dispara'}. Salidas de la enmienda: "
         f"{' o '.join(p1['salidas_de_la_enmienda'])}. Elección: {p1['eleccion']}.", ""]
    L += [f"  - `{u['chunk_id']}`: {u['no_sostenido']}" for u in p1["unidades_con_error"]]
    L += ["", "- Omisiones, aparte (" + str(len(p1["omisiones_aparte"])) + " unidades): " +
          "; ".join(f"`{o['chunk_id']}` ({o['omision']})" for o in p1["omisiones_aparte"]), ""]
    L += ["## Punto 5, las 27 de P4b", "", "| grupo | cumple |", "|---|---|"]
    L += [f"| {g} | {fmt(t)} |" for g, t in p5["por_grupo"].items()] + [f"| total | {fmt(p5['total'])} |", ""]
    v = p5["variacion_contra_p5"]
    L += [f"Variación contra P5: {v['identicas_a_alguna_de_p5']} idénticas a una de P5 y {v['difieren_de_las_dos']} "
          f"difieren; la marca cambia en {v['cambia_la_marca_contra_a']} contra a y {v['cambia_la_marca_contra_b']} "
          f"contra b. `ext::10.3.6`: {p5['ext_10_3_6']}.", ""]
    L += ["## Punto 6, listas", "", "| tipo y rol | cumple |", "|---|---|"]
    L += [f"| {k} | {fmt(t)} |" for k, t in p6["por_tipo_y_rol"].items()] + ["", "| lista | tipo | cumple |",
                                                                            "|---|---|---|"]
    L += [f"| {k}{' (aparte)' if x['aparte'] else ''} | {x['tipo']} | {x['cumple']}/{x['de']} |"
          for k, x in p6["por_lista"].items()]
    e = p6["encabezados_b1_con_forma_de_b2"]
    L += ["", f"Encabezados b1 con la forma de b2: {e['nota']}. Con el criterio de b2: "
          + "; ".join(f"`{k}` {x['marca_con_criterio_b2']} ({x['razon']})" for k, x in e["lectura"].items())
          + f". b1 encabezados con esos dos leídos como b2: {fmt(e['b1_encabezados_si_esos_dos_se_leen_como_b2'])}; "
          f"si las dos listas fueran b2: b1 encabezados {fmt(e['si_las_dos_listas_fueran_b2']['b1_encabezados'])} y b2 "
          f"encabezados {fmt(e['si_las_dos_listas_fueran_b2']['b2_encabezados'])}.", ""]
    s = p7["criterio_sellado"]
    q = p7["por_supuesto"]
    L += ["## Punto 7, grupo c", "", f"- Criterio sellado: cumple **{fmt(s['cumple'])}**. Etiquetas adjudicadas: "
          f"{s['por_etiqueta_adjudicada']}.", f"- Por supuesto ({q['total_supuestos']} supuestos de la fase A): "
          + "; ".join(f"{c} {fmt(t)}" for c, t in q["por_clase"].items())
          + f". Sin relación, por subtipo: {dict(q['sin_relacion_por_subtipo']['cuentas'])}.", "",
          "| documento | unidades | supuestos | " + " | ".join(q["clases"]) + " |",
          "|---|---|---|" + "---|" * len(q["clases"])]
    L += [f"| {to} | {x['unidades']} | {x['supuestos']} | " + " | ".join(t["fraccion"] for t in x["por_clase"].values())
          + " |" for to, x in q["por_documento"].items()]
    L += [f"| total | 30 | {q['total_supuestos']} | " + " | ".join(t["fraccion"] for t in q["por_clase"].values()) + " |",
          "", "Supuestos, uno por uno:", ""]
    L += [f"- `{x['chunk_id']}` «{x['fragmento_fase_a']}»{' ' + x['miembro'] if x['miembro'] else ''}: {x['clase']}"
          f"{' (' + x['subtipo_sin_relacion'] + ')' if x['subtipo_sin_relacion'] else ''} — {x['donde']}"
          for x in q["supuestos"]]
    L += ["", "## Punto 8, omisiones meta_normativo", ""]
    for g in ("sin_marca", "con_marca"):
        x = p8[g]
        tp, ep = x["tramo_propio"], x["estimacion_universo_tramo_propio"]
        L += [f"- **{g.replace('_', ' ')}** (N = {x['poblacion']}): normativas {fmt(x['normativas_con_remisiones'])} con "
              f"remisiones y {fmt(x['normativas_sin_remisiones'])} sin; habilitantes {fmt(x['habilitantes'])}; tramo "
              f"heredado {x['tramo_heredado']['leidas']} ({x['tramo_heredado']['normativas']} normativas). Tramo propio: "
              f"normativas {fmt(tp['normativas_con_remisiones'])} con remisiones y {fmt(tp['normativas_sin_remisiones'])} "
              f"sin; estimación al universo {num(ep['con_remisiones'])} con remisiones y {num(ep['sin_remisiones'])} sin."]
    L += ["", f"Se le escapan al contador: {p8['se_le_escapan_al_contador']}. Supuesto: {p8['supuesto_de_la_estimacion']}."]
    return L


def main() -> int:
    adj_crudo = (AQUI / "adjudicacion_autora.json").read_bytes()
    adj = json.loads(adj_crudo)
    res = OrderedDict([
        ("unidad", "U-REEXT-T0, T4, segundo tramo: tasas sobre la marca adjudicada"),
        ("adjudicacion_sha256", hashlib.sha256(adj_crudo).hexdigest()), ("fichas_sha256", SHA_FICHAS),
        ("wilson", f"95 %, z = {Z}"),
        ("punto_1", punto1(adj)), ("punto_5", punto5(adj)), ("punto_6", punto6(adj)), ("punto_7", punto7(adj)),
        ("punto_8", punto8(adj))])
    (SAL / "tasas_t4.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (SAL / "tasas_t4.md").write_text("\n".join(md(res)) + "\n", encoding="utf-8")
    print(json.dumps({"p1": res["punto_1"]["con_error"], "p1_regla": res["punto_1"]["regla_se_dispara"],
                      "p7": res["punto_7"]["criterio_sellado"]["cumple"],
                      "p7_supuestos": {c: t["fraccion"] for c, t in res["punto_7"]["por_supuesto"]["por_clase"].items()}},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
