"""U-REEXT-T0, T4: las fichas de lectura de los puntos 1, 5, 6, 7 y 8 del mandato (lecturas asistidas, que la autora
adjudica antes de computar las tasas). Por unidad: el texto de E0 r2b (propio y heredado), la extracción (entidades con
su tramo y sus umbrales, relaciones con sus extremos, omisiones) y mi lectura con el criterio del punto, con su razón.
La lectura es la de los diccionarios de abajo; el script solo la cruza con los sorteos y los sellos, la controla y la
cuenta. No computa tasas ni intervalos: eso es del segundo tramo, después de la adjudicación.

  Punto 1, cola humana: la muestra de 30 de salida/sorteos_t4.json, sobre la extracción final. Error: al menos un nodo
    o una relación que el texto de la unidad no sostiene; las omisiones van aparte.
  Punto 5, las 27 unidades de P4b (sellos_t4.json, a): sobre la respuesta de E1 de esta corrida (tool_input_crudo), con
    las reglas de marcado de P4b (data/experiment/prompt_r2/p4b/marcas_p4b.py). Las 27 claves son las de P5 (freno T1,
    punto 3); la variación se mide contra las corridas a y b de P5 (p5/salida/resultados_p5.jsonl) con
    p5/analisis_p5.comparar, y la marca se compara con la de P5 (p5/salida/marcas_p5.json). Donde la respuesta es
    idéntica a una de P5, la marca es la de P5.
  Punto 6, las once listas selladas (sellos_t4.json, b), sobre la extracción final; ctacte::3.2 aparte, declarada.
  Punto 7, grupo c: la fase A (más de un supuesto, decidido sobre el texto antes de mirar la extracción) está registrada
    con su hora en salida/grupo_c_fase_a.md; aquí se controla que la decisión codificada sea la misma. La fase B lee
    la extracción final de las 30 con el criterio c de P4b (una Condicion por supuesto, con label, descripción, tramo
    y umbral del mismo supuesto, hacia su norma).
  Punto 8, las 60 omisiones meta_normativo sorteadas (salida/sorteos_t4.json): si el tramo es contenido normativo
    según el §1 de la enmienda 7 a L-ESQ-R2 (texto firmado en 44c6e1b, sha256 81177f0c…) y si es habilitante (una
    norma cuyo efecto es que un sujeto pueda realizar algo: pre-registro de ESQ-3b v2, 40493c9; enmienda 7, §4). El
    script ubica el tramo en el texto propio o en el heredado.

Escribe solo en --salida: fichas_punto{1,5,6,7,8}_*.md y .json, y resumen_lecturas_t4.json. USD 0, sin red.
Uso (desde la raíz de una copia): python -B data/experiment/reext_t0/t4/fichas_t4.py --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[3]
sys.path.insert(0, str(AQUI))
import comun_t4 as K  # noqa: E402
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "prompt_r2" / "p5"))
import analisis_p5 as A5  # noqa: E402 — comparar y forma_salida de P5, importadas

SELLOS = RAIZ / "data" / "experiment" / "reext_t0" / "sellos_t4.json"
SHA_SELLOS = "7845d11ac2955e7c606357e1f7b50d6ef2d951bb21acb111c16f31e117fac560"
SORTEOS = AQUI / "salida" / "sorteos_t4.json"
FASE_A = AQUI / "salida" / "grupo_c_fase_a.md"
P5 = RAIZ / "data" / "experiment" / "prompt_r2" / "p5" / "salida"
OMISIONES = K.REX / "corpus_tanda0" / "ens_diez_r2b" / "r2" / "omisiones.jsonl"

C, N = "cumple", "no_cumple"
E, S, D = "con error", "sin error", "dudosa"

# ------------------------------------------------------------------------------------------------ punto 1, cola humana
# unidad → (clase, lo que el texto no sostiene, omisiones (aparte), observación)
LECTURA_1 = {
    "lingob::7.1.7": (E, "e1 Obligacion «deben definir la política…»: el texto dice «Es deseable incluir… la siguiente "
                         "información» (recomendación de divulgar, no deber de definir la política)", "", ""),
    "ctacte::1.5.1.3": (E, "aplica_a de e1 hacia Sujeto_banco (mención «la entidad»): la obligación es del "
                           "cuentacorrentista (encabezado 1.5.1); la entidad solo estima la necesidad", "", ""),
    "ext::10.4.3.5": (E, "e2 Obligacion «debe dar acceso…»: el texto dice «podrá dar acceso… en la medida que "
                         "verifique…» (facultad)", "", ""),
    "ext::14.2.1.8": (S, "", "", ""),
    "ext::3.18.1.1": (E, "e2 Restriccion «Se prohíbe… sin la conformidad previa» y su prohibe hacia e1: el texto habilita "
                         "ese pago sin la conformidad (3.18.1: «podrá acceder… para realizar»)", "", ""),
    "cap::6.2.2.4": (D, "aplica_a de e2 hacia Sujeto_rol_alcance_capmin con la mención «las entidades», no verificada: el "
                        "texto no nombra al sujeto", "filas y columna de la tabla", ""),
    "ext::5.4.1": (E, "aplica_a de e2 hacia Sujeto_rol_entidad_autorizada_exterior (mención «La entidad»): la obligación "
                      "de presentar el documento es del cliente", "", ""),
    "ext::8.5.13.2": (E, "ob1 Obligacion para «La entidad podrá considerar cumplimentado…»: es una facultad", "", ""),
    "cap::4.2.1.2::parte1": (S, "", "", "53 entidades sostenidas por el texto y 0 relaciones, por la reparación; e49 y "
                                       "e51 tipan como Restriccion «límite de 0,5 / de 5» los multiplicadores del SF "
                                       "(«se multiplicará por 0,5 / por 5»)"),
    "ctacte::1.5.1.12": (E, "aplica_a de e1 hacia Sujeto_banco (mención «el cuentacorrentista», no verificada): la "
                            "obligación es del cuentacorrentista (1.5.1)", "", ""),
    "ext::3.9::intro": (S, "", "«sin la conformidad previa del BCRA»", ""),
    "ext::7.1.1.2": (E, "aplica_a de e2 hacia Sujeto_rol_entidad_autorizada_exterior (mención «las entidades», no "
                        "verificada): la obligación de ingresar y liquidar es del exportador (7.1.1)", "",
                     "el tipo «presentacion_informativa» no corresponde"),
    "ext::10.4.3.3": (S, "", "la facultad «podrá dar acceso»", "«debe verificar previamente» se sostiene como deber "
                                                              "condicional"),
    "ext::10.10.2.9": (S, "", "", ""),
    "ext::3.8.1": (S, "", "", "la Restriccion del efectivo «limita» la Operacion descrita con débito en cuenta; la "
                              "Condicion del efectivo la acota"),
    "pagjub::2.7.2": (E, "e1 --prohibe--> e2 «Presentación de soportes con archivos»: el texto no prohíbe acompañar los "
                         "soportes; rechaza la presentación que no los acompaña", "", ""),
    "ext::4.7.1": (S, "", "la relación de la Condicion con su norma", ""),
    "lingob::7.1.8": (E, "e1 Obligacion «Incluir en los sitios públicos… las políticas…» sin la marca de recomendación: "
                         "el texto dice «Es deseable incluir»", "", "e2 («deberán contemplar») se sostiene"),
    "cap::8.4.1.16": (S, "", "", "el «limita» de la deducción hacia la Operacion de asistencia es una lectura laxa"),
    "ext::8.5.18.2": (S, "", "", "o3 «deberá contar con una certificación», como requisito de la facultad"),
    "pagjub::2.8.1.2": (E, "aplica_a de e2 hacia Sujeto_rol_alcance_pagjub (mención «la entidad participante»): la "
                           "obligación de acreditar es del BCRA («El BCRA… procederá a»); la entidad es la beneficiaria",
                        "", ""),
    "ext::3.17.1.2": (S, "", "", "las tres Condicion van juntas a la Operacion, sin la estructura «y/o»"),
    "cap::10.3.3.1": (E, "e3 (igual o preferente, del inciso i) --condicion_de--> e2 (la regla de la emisión calificada), "
                         "y e4 (no podrá usarse la calificación) --prohibe--> e1 (la inversión en la emisión calificada): "
                         "lo prohibido es usar la calificación, no invertir", "", ""),
    "ext::10.3.5.4": (S, "", "", ""),
    "ext::3.4.1": (S, "", "", ""),
    "pro::4.2.1.4": (S, "", "la facultad «podrá informar»", "el recaudo de la presentación, como deber condicional"),
    "ext::3.6.1.1": (S, "", "", ""),
    "ext::3.13.1.10": (S, "", "", ""),
    "ext::14.2.1.11": (S, "", "", ""),
    "ext::9.3.7": (S, "", "la facultad «La entidad podrá emitir» (queda como Operacion, sin Potestad)", ""),
}

# ------------------------------------------------------------------------------------------ punto 5, unidades de P4b
IGUAL_A_P5 = "idéntica a una respuesta de P5: la marca es la de P5"
# unidad → (marca, razón, dudosa); IGUAL_A_P5 donde la respuesta es idéntica a una de P5 (el script lo controla)
LECTURA_5 = {
    "ext::13.1.4": (N, "sin omisión meta_normativo, pero la facultad «Los clientes podrán suscribir» va como Operacion "
                       "(con Restriccion de tope), sin Potestad: el contenido no va con su tipo", False),
    "ext::6.1.1": (IGUAL_A_P5, "", False),
    "cap::10.3.3.1": (N, "registra «De lo contrario, será de aplicación lo siguiente:» como meta_normativo (contador: "
                         "alcance), como P5 a y b (lectura dudosa de P5: el régimen alternativo)", False),
    "cap::11.4": (IGUAL_A_P5, "", False),
    "cap::5.3.1.3": (N, "las ocho de a) a h) como Condicion de la Restriccion del 0 %; el supuesto «participante "
                        "esencial» va en la Operacion y los de ii) y iii) van como Operacion y Restriccion, no como "
                        "Condicion (como en P5)", False),
    "cla::6.5.4.5": (IGUAL_A_P5, "", False),
    "ext::10.4.2.5": (N, "c2 junta dos supuestos (no persona humana y constituida hasta 365 días) y el monto (más de USD "
                         "5 millones) va como umbral de la Restriccion, como en P5", False),
    "ext::10.3.6": (C, "una Condicion por supuesto (documentación; desde el 13/12/23; salvo 10.10.2.11; desde el "
                       "14/04/25), cada una hacia su norma, como en P5. Con la regla de la fase B del punto 7 sería "
                       "no_cumple: el supuesto «cuando correspondía a la porción… pagos a la vista» va dentro de la "
                       "Excepcion e8", True),
    "ext::10.4.3.6": (C, "sin entidad aparte para la facultad del encabezado (la registra como meta_normativo); su "
                         "verificación como Condicion y el acceso como Operacion, como en P5", False),
    "ext::4.1.4.7": (N, "la Obligacion compone el ítem en la descripción, pero su tramo es solo el del encabezado (P5 a "
                        "no cumple por eso; P5 b cumple con tramo de dos segmentos)", True),
    "polcre::2.1.15": (C, "sin entidad aparte para el deber del encabezado (meta_normativo), como en P5", False),
    "cap::10.2.2.4": (C, "sin entidad aparte para el deber del encabezado («deberán cumplir cada uno de los seis "
                         "criterios»); cuatro Obligacion de divulgación del ítem (P5 a y b no cumplían)", False),
    "cap::6.3.2::intro": (N, "aplica_a con la mención «los restantes derivados sobre acciones y las posiciones fuera de "
                             "balance…»: verifica en el texto, pero no es un sujeto (como P5 b)", False),
    "cap::3.2::intro": (C, "sin relación de sujeto", False),
    "cap::6.3.2.1": (C, "sin relación de sujeto", False),
    "polcre::5.3": (C, "sin relación de sujeto (P5 a y b: aplica_a «las entidades», que el texto no nombra)", False),
    "ctacte::3.2.2": (N, "Restriccion, no Excepcion; dos prohibe colgantes rechazados", False),
    "ctacte::3.2.5": (N, "Operacion y Restriccion, no Excepcion", False),
    "ctacte::3.2.4": (N, "Restriccion, no Excepcion", False),
    "ext::3.5.3.4": (N, "las Condicion van a la Operacion y no nombran la norma exceptuada ni el cuantificador; la nombra "
                        "una Excepcion compuesta con el tramo del encabezado, con exceptua_obligacion hacia la "
                        "Restriccion del ítem", False),
    "ext::3.5.3.5": (N, "la Condicion del supuesto va a la Excepcion y no lleva el cuantificador ni la norma exceptuada; "
                        "la norma la nombra la Excepcion", False),
    "ext::3.5.3.1": (N, "una Condicion hacia la Operacion; ninguna nombra la norma exceptuada ni el cuantificador",
                     False),
    "ctacte::3.2::intro": (N, "Restriccion, no Definicion de la clase", False),
    "ext::3.5.3::intro": (N, "la norma (Potestad del BCRA) y la Excepcion, sin relación entre ellas "
                             "(relacion_sin_predicado)", False),
    "cla::5.1.1::intro": (IGUAL_A_P5, "", False),
    "cla::5.1.1.1": (C, "Excepcion, Operacion de inclusión en la cartera comercial y una Condicion por cada condición "
                        "(monto y repago), hacia esa Operacion", False),
    "cap::6.2.2.6": (C, "ningún porcentaje de cap::tabla037 copiado (umbrales vacíos) y la omisión `tabla` declarada",
                     False),
}

# ------------------------------------------------------------------------------------------------- punto 6, listas
# unidad → (marca, razón, dudosa)
LECTURA_6 = {
    # cla::5.1.1 (b1)
    "cla::5.1.1::intro": (C, "Definicion «Cartera comercial — alcance» (la clase)", False),
    "cla::5.1.1.1": (C, "Excepcion «quedan exceptuados de la cartera comercial» (el miembro, con la norma); el exceptua "
                        "fue rechazado por la firma, sin colgante", False),
    "cla::5.1.1.2": (N, "sin Excepcion: el miembro (financiaciones comerciales de hasta dos veces el importe) va como "
                        "Operacion y Potestad de agrupar", False),
    # ext::3.5.4 (b2)
    "ext::3.5.4::intro": (C, "la Excepcion «El requisito de conformidad previa del BCRA… no resultará aplicable cuando "
                             "se cumpla la totalidad de las condiciones» lleva la norma y su excepción en una entidad, "
                             "con la Condicion de vigencia", True),
    "ext::3.5.4.1": (N, "la Condicion nombra la norma exceptuada (suspende el requisito de conformidad previa) pero no "
                        "el cuantificador («la totalidad»)", False),
    "ext::3.5.4.2": (N, "la Condicion no nombra la norma exceptuada ni el cuantificador", False),
    "ext::3.5.4.3": (N, "la Condicion del supuesto no nombra la norma ni el cuantificador; trae una Excepcion compuesta "
                        "en el ítem", False),
    # ext::2.6.1 (b2)
    "ext::2.6.1::intro": (C, "Excepcion «quedan exceptuadas de la obligación de liquidación…» (la norma con su "
                             "excepción) y Condicion «la totalidad de las condiciones»", False),
    "ext::2.6.1.1": (N, "Condicion sin la norma exceptuada ni el cuantificador", False),
    "ext::2.6.1.2": (N, "Condicion sin norma ni cuantificador, hacia una Excepcion compuesta que repite la del "
                        "encabezado", False),
    "ext::2.6.1.3": (N, "la Condicion nombra la excepción de liquidación, pero no el cuantificador", False),
    # ext::7.8.4 (b2)
    "ext::7.8.4::intro": (C, "Excepcion de la obligación de liquidación y Condicion «la totalidad»", False),
    "ext::7.8.4.1": (N, "Operacion y Obligacion (declaración jurada); sin Condicion del supuesto", False),
    "ext::7.8.4.2": (N, "Operacion y Condicion sin norma ni cuantificador", False),
    "ext::7.8.4.3": (N, "Condicion sin norma ni cuantificador", False),
    # ext::2.7 (b2)
    "ext::2.7::intro": (C, "Excepcion «No será exigible la liquidación… cuando se cumplan todas las condiciones» y "
                           "Condicion «la totalidad»", False),
    "ext::2.7.1": (N, "la Condicion nombra la excepción a la obligación de liquidación, pero no el cuantificador", False),
    "ext::2.7.2": (N, "Condicion sin norma ni cuantificador", False),
    "ext::2.7.3": (N, "dos Condicion sin norma ni cuantificador", False),
    "ext::2.7.4": (N, "Obligacion (neutralidad fiscal), sin Condicion del supuesto", False),
    # ctacte::3.2 (b1, lectura dudosa: aparte, declarada)
    "ctacte::3.2::intro": (N, "Restriccion «Título sin valor como cheque», no Definicion de la clase", False),
    "ctacte::3.2.1::intro": (N, "Restriccion, no Excepcion", False),
    "ctacte::3.2.2": (N, "dos Restriccion, no Excepcion", False),
    "ctacte::3.2.3": (N, "Restriccion y Operacion con prohibe, no Excepcion", False),
    "ctacte::3.2.4": (N, "Restriccion y Operacion con prohibe, no Excepcion", False),
    "ctacte::3.2.5": (N, "Operacion y Restriccion, no Excepcion", False),
    # ext::3.5.3 (b2)
    "ext::3.5.3::intro": (N, "la norma (Potestad del BCRA) y la Excepcion, sin relación (relacion_sin_predicado)", False),
    "ext::3.5.3.1": (N, "Condicion hacia la Operacion, sin la norma exceptuada ni el cuantificador", False),
    "ext::3.5.3.2": (N, "Condicion sin norma ni cuantificador, hacia una Excepcion compuesta en el ítem", False),
    "ext::3.5.3.3": (N, "Condicion hacia la Operacion; Excepcion compuesta en el ítem, con exceptua hacia la Restriccion "
                        "del ítem", False),
    "ext::3.5.3.4": (N, "Condicion hacia la Operacion, sin norma ni cuantificador; Excepcion compuesta en el ítem", False),
    "ext::3.5.3.5": (N, "las Condicion son las del encabezado, copiadas; el supuesto (VPU adherido al RIGI) va en la "
                        "Excepcion, sin Condicion propia", False),
    # ext::3.13.1 (b1)
    "ext::3.13.1::intro": (N, "dos Operacion, la Obligacion de la conformidad previa y una Excepcion general con "
                              "exceptua_obligacion; no hay Definicion de la clase", False),
    "ext::3.13.1.1": (C, "Excepcion «…quedan exceptuadas del requisito de conformidad previa del BCRA» por el miembro "
                         "(organismos internacionales), sin exceptua colgante", False),
    "ext::3.13.1.2": (C, "Excepcion por el miembro (representaciones diplomáticas), con la norma", False),
    "ext::3.13.1.3": (C, "Excepcion por el miembro (representaciones de tribunales…), con la norma", False),
    "ext::3.13.1.4": (N, "sin Excepcion; repite la Obligacion de la conformidad previa del encabezado", False),
    "ext::3.13.1.5": (N, "la Excepcion es de otra cosa (las liquidaciones de títulos no se computan en el tope); sin la "
                         "del miembro", False),
    "ext::3.13.1.6": (C, "Excepcion por el miembro, con la norma, y exceptua hacia la Restriccion de la conformidad del "
                         "mismo ítem (no colgante)", False),
    "ext::3.13.1.7": (N, "Operacion y Condicion; sin Excepcion", False),
    "ext::3.13.1.8": (N, "Operacion y Condicion; sin Excepcion", False),
    "ext::3.13.1.9": (N, "Operacion y Condicion; sin Excepcion", False),
    "ext::3.13.1.10": (N, "Operacion, Condicion y Obligacion; sin Excepcion", False),
    "ext::3.13.1.11": (N, "Operacion y Condicion; sin Excepcion", False),
    "ext::3.13.1.12": (N, "la Excepcion es de otra cosa (cobro en moneda extranjera); sin la del miembro", False),
    "ext::3.13.1.13": (N, "Operacion y Condicion; sin Excepcion", False),
    # ext::3.6.1 (b1)
    "ext::3.6.1::intro": (N, "Restriccion de la prohibición, Excepcion y Condicion; no hay Definicion de la clase", False),
    "ext::3.6.1.1": (C, "Excepcion por el miembro (financiaciones de entidades locales) con la norma («Excepción a la "
                        "prohibición…»), exceptua hacia la Restriccion del mismo ítem", False),
    "ext::3.6.1.2": (C, "Excepcion por el miembro (emisiones para refinanciar), con la norma", False),
    "ext::3.6.1.3": (N, "Operacion, Condicion y la Restriccion del encabezado copiada; sin Excepcion", False),
    "ext::3.6.1.4": (C, "Excepcion por el miembro (pagarés RG 1.003/24), con la norma", False),
    "ext::3.6.1.5": (N, "la Excepcion es la genérica del encabezado y no nombra al miembro (valores de deuda "
                        "fiduciaria), que va en la Operacion", True),
    "ext::3.6.1.6": (C, "Excepcion por el miembro (reestructuraciones sin desembolsos), con la norma (además de la "
                        "genérica)", False),
    # ext::3.6.4 (b2)
    "ext::3.6.4::intro": (N, "la norma (Potestad) y la Excepcion, sin relación entre ellas", False),
    "ext::3.6.4.1": (N, "una Condicion con el cuantificador y la norma («la totalidad… para que la excepción a la "
                        "conformidad previa sea aplicable»), pero el supuesto va en una Excepcion compuesta, no en una "
                        "Condicion", True),
    "ext::3.6.4.2": (N, "Condicion sin norma ni cuantificador", False),
    "ext::3.6.4.3": (N, "Condicion sin norma ni cuantificador", False),
    "ext::3.6.4.4": (N, "Condicion sin norma ni cuantificador", False),
    "ext::3.6.4.5": (N, "Condicion sin norma ni cuantificador; la norma en una Potestad compuesta", False),
    "ext::3.6.4.6": (N, "Condicion sin norma ni cuantificador", False),
    "ext::3.6.4.7": (N, "la Condicion del supuesto (VPU adherido al RIGI) sin norma ni cuantificador", False),
    # ext::10.11 (b2)
    "ext::10.11::intro": (C, "la Obligacion de la conformidad previa y su Excepcion, unidas por exceptua_obligacion",
                          False),
    "ext::10.11.1": (N, "Condicion sin norma ni cuantificador, hacia una Excepcion compuesta en el ítem", False),
    "ext::10.11.2": (N, "Condicion sin norma ni cuantificador", False),
    "ext::10.11.3": (N, "Condicion sin norma ni cuantificador", False),
    "ext::10.11.4": (N, "Condicion sin norma ni cuantificador", False),
    "ext::10.11.5": (N, "Condicion sin norma ni cuantificador", False),
    "ext::10.11.6": (N, "Condicion sin norma ni cuantificador", False),
    "ext::10.11.7::intro": (N, "Condicion del supuesto (MiPyMe) y una del cuantificador de su sublista; sin la norma "
                               "exceptuada", False),
}

# ---------------------------------------------------------------------------------------------- punto 7, grupo c
# Fase A (registrada con su hora en salida/grupo_c_fase_a.md): posición en el orden sellado → (unidad, más de un
# supuesto, dudosa). El script controla que coincida con la tabla del archivo.
FASE_A_7 = {
    1: ("ext::10.5.5.2", True, False), 2: ("ext::10.4.4", True, False), 3: ("polcre::7.1.2", True, False),
    4: ("cap::5.4.6", False, False), 5: ("pro::2.3.5.1", True, False), 6: ("cap::6.2.3.5", True, False),
    7: ("ext::10.3.6", True, False), 8: ("cla::6.5.3.10", True, False), 9: ("ext::3.12.1", False, False),
    10: ("ric::5.1.3.2", False, False), 11: ("ext::7.9.4", True, False), 12: ("cla::7.2.2.1", True, False),
    13: ("cap::3.1.14.1", True, False), 14: ("cla::7.2.4", True, False), 15: ("cap::3.1.13.3", False, True),
    16: ("ext::14.5.7", True, False), 17: ("cla::6.5.5.9", True, False), 18: ("cla::7.2.3", True, False),
    19: ("cap::2.1", True, False), 20: ("pro::3.1.3", True, False), 21: ("cap::7.3.2", True, False),
    22: ("ext::4.1.3.2", True, False), 23: ("cap::3.1.11.3", True, False), 24: ("ext::3.16.3.6", True, False),
    25: ("cap::6.3.2.2", True, False), 26: ("ext::4.1.3.1", True, False), 27: ("ric::9.1.3", True, False),
    28: ("ext::8.4.2", True, False), 29: ("ric::6.1.2", True, False), 30: ("cla::6.5.4.5", True, False),
    31: ("ric::6.2", False, False), 32: ("cap::3.1.11.2", True, False), 33: ("ric::4.5.2", True, True),
    34: ("polcre::7.1::cierre", True, False), 35: ("cla::6.5.5.2", True, False),
}
ETIQUETAS_7 = {
    "en_norma": "el supuesto va dentro de una entidad de norma (descripción o tramo), no como Condicion",
    "fusion": "una Condicion junta dos supuestos, o el supuesto y su norma",
    "omitido": "el supuesto no se extrae, o queda solo en una omisión",
    "umbral_en_norma": "la cuantía del supuesto va como umbral de una norma",
    "sin_relacion": "la Condicion no tiene relación hacia su norma",
    "incoherente": "la Condicion va hacia otra norma, o no es un supuesto",
}
# Fase B: unidad → (marca, etiquetas, razón, dudosa)
LECTURA_7 = {
    "ext::10.5.5.2": (N, ["en_norma"], "i), ii), iii a) (con USD 100.000) y iii b) bien; «si el importador percibiera» "
                      "dentro de la Obligacion e7; «mientras se demuestre la vigencia» en la Potestad e8 y en una "
                      "omisión meta_normativo", False),
    "ext::10.4.4": (N, ["en_norma"], "13/12/23, salvo 10.10.2.11, 14/04/25 y 90 días bien; «en la medida que se "
                    "verifique que se cumplían las condiciones» en la Operacion e1; «cuando correspondía a la porción… "
                    "pagos a la vista» en la Potestad e7", False),
    "polcre::7.1.2": (N, ["fusion"], "c1 (30.000 millones) y c2 (pases, 90 días) bien; c3 junta la declaración jurada y "
                      "lo que surge de la Central; MiPyME como Excepcion; c4 (vigencia de 90 días) no es un supuesto",
                      True),
    "pro::2.3.5.1": (N, ["en_norma", "omitido"], "los conceptos i) a vii) van como Restriccion; cuenta a la vista (e13), "
                     "si no fuera posible (e14), correo aceptado (e17), reclamo y constatación (e9, e10) dentro de las "
                     "Obligacion; «cuando la tasa… no estuviera disponible» sin extraer", False),
    "cap::6.2.3.5": (N, ["en_norma"], "«si se corresponden exactamente» (Operacion e3), «cuando el futuro permita "
                     "entregar una gama» (Restriccion e4), «si consideran que están compensadas» (Potestad e6), y a), "
                     "b), c) con los tres tramos de fechas dentro de las Restriccion e9 a e13", False),
    "ext::10.3.6": (C, [], "documentación, 13/12/23, salvo 10.10.2.11, 14/04/25 y porción con pagos a la vista, cada "
                    "una en su Condicion hacia su norma (tras el reintento; en E1 la porción iba dentro de la "
                    "Excepcion)", False),
    "cla::6.5.3.10": (N, ["incoherente", "en_norma"], "c1, c2 (15 %) y c3 van hacia o1 (el cómputo del 50 % de las "
                      "garantías), que no es la norma que condicionan; c4 (2,5 veces) bien; «siempre que no medie "
                      "objeción por parte de la SEFyC» dentro de la Potestad p1", False),
    "ext::7.9.4": (N, ["en_norma"], "proyectos del 7.9.2 bien; «si existen endeudamientos…» dentro de e3; «cuando el "
                   "mismo no cuente con la aprobación… Ley 26.360» dentro de e8", False),
    "cla::7.2.2.1": (N, ["en_norma", "sin_relacion"], "1 cuota (31 días), pago único (5 %) y atrasos de más de 31 días "
                     "bien; la financiación adicional sin cancelar dentro de la Restriccion e6; e2 (10 %) sin relación "
                     "hacia la Definicion e1", False),
    "cap::3.1.14.1": (N, ["en_norma", "fusion", "sin_relacion"], "refinanciación distribuida y valores residuales "
                      "dentro de e3; «salvo… el período de 2 años» dentro de e11; e8 (5 años) y e9 (7 años) juntan el "
                      "supuesto y la norma, sin relación", False),
    "cla::7.2.4": (N, ["en_norma"], "concurso con 20 % o entre 5 % y 20 % (Definicion e2), levantamiento del pedido "
                   "(Potestad e3), refinanciados (Operacion e5), 540 días (e6), financiación adicional (e8) y atrasos de "
                   "31 días (e9) dentro de normas; solo e7 es Condicion", False),
    "ext::14.5.7": (N, ["en_norma"], "i), 90 %, ii) y iii) bien; la declaración jurada, segunda condición del 90 %, como "
                    "Obligacion e4; «en caso de no disponerla» dentro de e7; la repatriación con cobros de "
                    "exportaciones dentro de e12", False),
    "cla::6.5.5.9": (N, ["en_norma", "umbral_en_norma", "fusion"], "el supuesto del 2,5 % como Restriccion «no podrá "
                     "exceder», con el umbral; la falta de declaración jurada como Obligacion e3; concurso (Excepcion "
                     "con 540 días) e informe de abogado bien; e6 junta la primera declaración y las actualizaciones",
                     False),
    "cla::7.2.3": (N, ["en_norma", "umbral_en_norma", "sin_relacion"], "2 cuotas, pago único y resto de deudas bien; la "
                   "financiación adicional dentro de la Restriccion e8; los atrasos de más de 31 días dentro de la "
                   "Obligacion e9, con su umbral; e2 (10 %) sin relación", False),
    "cap::2.1": (N, ["en_norma", "fusion", "sin_relacion"], "e4 lleva el supuesto y la consecuencia (k = 1,03), sin "
                 "relación; el inicio del cronograma dentro de e19 a e21", False),
    "pro::3.1.3": (N, ["en_norma"], "teléfono o Internet dentro de e7; número no recibido automáticamente dentro de e8; "
                   "ninguna Condicion", False),
    "cap::7.3.2": (N, ["en_norma"], "calificación 1, 2 o 3 y calificación 1 o 2 bien; «en el caso de entidades del grupo "
                   "B» dentro de la Restriccion e1 (única falla)", False),
    "ext::4.1.3.2": (N, ["omitido", "fusion"], "«cuando se trate de empresas no financieras emisoras» sin extraer; e3 "
                     "junta la regla del tipo de cambio, el pago en pesos y el día inhábil", False),
    "cap::3.1.11.3": (N, ["en_norma"], "i) a iii), «si tal posición no existiera» y los mínimos por STC dentro de "
                      "Restriccion y Operacion; ninguna Condicion", False),
    "ext::3.16.3.6": (N, ["en_norma", "umbral_en_norma"], "a) a e) bien; la cláusula de garantía (e3), los fondos "
                      "usados en 10 días (e4, con su umbral), el monto adquirido (e11) y el valor de mercado (e12) "
                      "dentro de Obligacion", False),
    "cap::6.3.2.2": (N, ["en_norma"], "b) (deliberada, 90 %), c) (costos) y la evidencia bien; los dos supuestos de "
                     "arbitraje del a) dentro de las Excepcion e6 y e7", False),
    "ext::4.1.3.1": (N, ["omitido", "en_norma"], "«cuando el emisor de la tarjeta sea una entidad financiera» solo en "
                     "una omisión meta_normativo; el día inhábil dentro de la Restriccion e2; el débito automático "
                     "bien", False),
    "ric::9.1.3": (N, ["sin_relacion"], "c1, c2 (5 %) y c4 (mientras persista) bien; c3 (base consolidada) sin relación: "
                   "la norma que condiciona (la asimilación de las partidas) no se emite y queda en una omisión "
                   "meta_normativo", True),
    "ext::8.4.2": (N, ["en_norma", "fusion", "sin_relacion"], "varios productos (e2), ampliación (e5) y reducción (e6) "
                   "dentro de normas; e4 lleva el supuesto (día no hábil) y la consecuencia, sin relación", False),
    "ric::6.1.2": (N, ["en_norma"], "los tres «cuando» del código 22600000 (e12), el del 22700000 (e14) y el del "
                   "21800000 (e7) dentro de Operacion; ninguna Condicion", False),
    "cla::6.5.4.5": (N, ["en_norma", "umbral_en_norma", "incoherente"], "otras condiciones (e4, e6) y financiación "
                     "adicional (e8) bien, y «salvo otras pautas» como Excepcion; bienes en pago y «salvo condiciones "
                     "del mercado» dentro de la Restriccion e2; el pago del 10 % dentro de la Obligacion e5, con su "
                     "umbral; e10 es la concesiva «aun cuando haya cancelado», como Condicion", False),
    "cap::3.1.11.2": (N, ["en_norma", "umbral_en_norma"], "SPE (e3), sintéticas (e5), previsión (e7), 5 % o menos (e14) "
                      "y más del 5 % (e15, con su umbral) dentro de normas; «si puede demostrar» y «a menos que» como "
                      "Excepcion; ninguna Condicion", False),
    "ric::4.5.2": (N, ["en_norma"], "compra o venta dentro de la Obligacion e7 (unidad dudosa en la fase A)", False),
    "polcre::7.1::cierre": (N, ["en_norma", "umbral_en_norma"], "7.1.1 bien, hacia la Potestad; el monto de $ 30.000 "
                            "millones y los pases como Restriccion con su umbral; «en la medida que con tales "
                            "desembolsos no se supere» dentro de la Potestad e4; los conjuntos económicos como "
                            "Definicion", False),
    "cla::6.5.5.2": (N, ["en_norma"], "atrasos de más de un año, refinanciación, pérdidas de explotación, pago del 15 %, "
                     "crédito adicional y no cancelación bien; «cuando previamente no se haya producido la cancelación "
                     "efectiva» dentro de la Restriccion e5 (única falla)", False),
}

# ----------------------------------------------------------------------------------- punto 8, omisiones meta_normativo
# (grupo, posición en el orden del sorteo) → (unidad, normativo, clase, habilitante, dudosa, razón)
LECTURA_8 = {
    ("sin_marca", 1): ("ric::4.1.1.5", False, "", False, False, "identificador de la partida (código), sin norma"),
    ("sin_marca", 2): ("ext::10.3.2.1", True, "condición", False, True,
                       "alternativa de cumplimiento de la condición de acceso («o cuenta con una certificación…»); no "
                       "habilitante: la facultad está en el encabezado y esto es una condición (dudosa: la nota la "
                       "llama habilitante)"),
    ("sin_marca", 3): ("pro::2.7::intro", True, "modalidad", False, False,
                       "lo que los hipervínculos deben permitir: el contenido del deber que el encabezado fija para "
                       "cada ítem (§1.5); quitarla cambia lo exigido"),
    ("sin_marca", 4): ("ext::10.5::intro", True, "alcance", False, False,
                       "«a los efectos cambiarios» limita para qué vale la regularización: sin la frase valdría para "
                       "todo efecto (§1.4)"),
    ("sin_marca", 5): ("pro::3.2.3.5", False, "", False, False, "«según corresponda», vacío"),
    ("sin_marca", 6): ("ctacte::1.5.2.6", True, "aplicabilidad temporal", False, False,
                       "el deber de pagar se rige por las disposiciones vigentes a la fecha de emisión del cheque "
                       "(§1.2)"),
    ("sin_marca", 7): ("cap::2.8.3.4", False, "", False, False, "conectivo «En consecuencia»"),
    ("sin_marca", 8): ("ctacte::3.2.1.2", True, "alcance", False, True,
                       "«no valdrá como cheque»: lo que queda afuera de la clase «cheque» (§1.2; como ctacte::3.2.5 en "
                       "P4b); dudosa: también se lee como cláusula que niega un efecto jurídico (§1.1)"),
    ("sin_marca", 9): ("ext::7.1.3", True, "remisión", False, True,
                       "la consecuencia de la norma de la unidad, por remisión («resultará aplicable lo dispuesto en el "
                       "punto 14.1.4»); dudosa por ser remisión"),
    ("sin_marca", 10): ("ext::7.1.1.5", True, "alcance", False, True,
                        "el plazo de 365 días vale para todo bien exportado por EXPORTA SIMPLE, por encima del plazo "
                        "por bien (§1.4); dudosa"),
    ("sin_marca", 11): ("ctacte::6.1.2.7", True, "alcance", False, False,
                        "definición de la clase «defecto formal» (§1.3: lo que abarca una clase es una Definicion)"),
    ("sin_marca", 12): ("ric::5.1.3.4", True, "modalidad", False, True,
                        "lo que la partida debe reflejar (la situación de la entidad respecto de su calificación); "
                        "dudosa: también se lee como finalidad"),
    ("sin_marca", 13): ("ric::3.1.7", True, "remisión", False, True,
                        "la modalidad del deber de consignar, por remisión al modelo del 3.1.4; dudosa por ser remisión"),
    ("sin_marca", 14): ("pagjub::2.8.4.3", False, "", False, False,
                        "enunciado descriptivo que anuncia los movimientos de fondos"),
    ("sin_marca", 15): ("ext::7.2.2", False, "", False, False, "título de la unidad"),
    ("sin_marca", 16): ("pagjub::2.2", False, "", False, False, "campo del formulario"),
    ("sin_marca", 17): ("ctacte::2.3.5::intro", False, "", False, False,
                        "anuncio de la enumeración («con el siguiente detalle»), sin deber, modalidad, cuantificador ni "
                        "condición propios"),
    ("sin_marca", 18): ("ext::2.1", False, "", False, False, "remisión estructural a las secciones 7 a 9, sin norma"),
    ("sin_marca", 19): ("ext::9.3.9", True, "alcance", False, True,
                        "«admitidos en el punto 7.9» delimita a qué títulos se aplica la certificación (§1.4); dudosa: "
                        "está en el título de la unidad"),
    ("sin_marca", 20): ("ric::12.4", False, "", False, False,
                        "la fecha desde la que rige la suspensión: de una frase de vigencia, solo la fecha es "
                        "meta-normativa (§1.1 y §1.2)"),
    ("sin_marca", 21): ("cap::4.3.1.2", True, "alcance", False, False,
                        "«a los efectos del cálculo de la exigencia de capital» limita para qué la segunda CCP es "
                        "miembro compensador (§1.4)"),
    ("sin_marca", 22): ("cap::5.2.1.3", False, "", False, False, "«por ejemplo»"),
    ("sin_marca", 23): ("ric::6.1.2", True, "remisión", False, True,
                        "qué existencias se informan, por remisión al punto 8.4.1.3; dudosa por ser remisión"),
    ("sin_marca", 24): ("ext::13.5", True, "condición", False, False,
                        "el supuesto de las cartas emitidas a partir del 13/12/23"),
    ("sin_marca", 25): ("ctacte::2.1.1.4", True, "deber", False, False,
                        "el ítem es el contenido del deber del encabezado (las boletas deben contener lugar y fecha), "
                        "que se extrae en el ítem (§1.5)"),
    ("sin_marca", 26): ("cap::8.2.3::cierre", False, "", False, False, "«de corresponder», vacío"),
    ("sin_marca", 27): ("ctacte::3.5.3", True, "condición", False, True,
                        "«En su defecto» introduce el supuesto (si el tenedor no presenta) de la consecuencia; dudosa: "
                        "el tramo es solo el conector"),
    ("sin_marca", 28): ("cap::7.1.3::intro", True, "remisión", False, True,
                        "la modalidad del deber de divulgar, por remisión a requerimientos que se establezcan; dudosa "
                        "por ser remisión"),
    ("sin_marca", 29): ("lingob::3.1.6", True, "remisión", False, True,
                        "la modalidad del deber, por remisión a la Sección 5; dudosa por ser remisión"),
    ("sin_marca", 30): ("ext::9.3.12::intro", True, "alcance", False, False,
                        "«en el marco de lo previsto en el punto 7.10» delimita el alcance (como ext::3.5.3.5 en P4b)"),
    ("con_marca", 1): ("ext::13.3.9", True, "facultad", True, False,
                       "«También será admisible el acceso… cuando… se verifique el encuadre»: la facultad de acceso, "
                       "con su condición"),
    ("con_marca", 2): ("lingob::2.3.2.1", True, "deber (recomendación)", False, False,
                       "buena práctica: paridad de género en el Directorio; la finalidad que sigue no cambia la lectura"),
    ("con_marca", 3): ("ext::9.1.5", False, "", False, False, "título de la sección («9.1. Operaciones comprendidas.»)"),
    ("con_marca", 4): ("lingob::4.2.1", True, "deber (recomendación)", False, False,
                       "«deberían tener un rol clave»: recomendación sobre la composición de los comités"),
    ("con_marca", 5): ("polcre::6.2.1.5", True, "condición", False, False,
                       "el encabezado que somete las operaciones UVI a las condiciones de los ítems (§1.5)"),
    ("con_marca", 6): ("ext::5.8.2.2", True, "condición", False, False,
                       "la unidad entera es una condición (ítem de las condiciones del 5.8.2): queda sin extraer"),
    ("con_marca", 7): ("cla::6.5.1.1", True, "cuantificador", False, True,
                       "el cuantificador de la lista (los indicadores no son taxativos: «entre los indicadores… se "
                       "destacan»), como ctacte::3.2::intro en P4b; dudosa"),
    ("con_marca", 8): ("cla::2.2.4.4", True, "condición", False, False,
                       "«siempre que se observen los siguientes requisitos»: la condición que el encabezado fija para "
                       "cada ítem (§1.5)"),
    ("con_marca", 9): ("cla::2.1.6", True, "alcance", False, False,
                       "delimita la clase (fideicomisos no alcanzados por esas normas)"),
    ("con_marca", 10): ("cap::10.3.1.1", True, "deber", False, False,
                        "«las entidades financieras deberán establecer…»: un deber (§1.2), aunque reformule el de e2"),
    ("con_marca", 11): ("cla::6.5.3.7", True, "alcance", False, False,
                        "lo que abarca la categoría «Con problemas» (§1.3)"),
    ("con_marca", 12): ("cla::3.5::intro", True, "facultad", True, False,
                        "«La tarea de clasificación podrá ser encomendada»: una facultad"),
    ("con_marca", 13): ("ext::9.3.10.4", False, "", False, False,
                        "«en caso de corresponder», vacío (la marca del contador es un falso positivo)"),
    ("con_marca", 14): ("lingob::3.2::intro", False, "", False, True,
                        "«en orden a las buenas prácticas»: finalidad; dudosa: también marca que la norma es de buena "
                        "práctica"),
    ("con_marca", 15): ("cap::3.1.2.2", True, "deber", False, False,
                        "el deber de aplicar el criterio e informar a la SEFyC, con su condición (la incertidumbre)"),
    ("con_marca", 16): ("cla::6.5.4.7", True, "condición", False, True,
                        "la condición de la reclasificación, por remisión («si se observan las condiciones allí "
                        "previstas»); dudosa por ser remisión"),
    ("con_marca", 17): ("ext::1.5", True, "alcance", False, True,
                        "los incumplimientos quedan alcanzados por la Ley del Régimen Penal Cambiario: el alcance del "
                        "régimen sancionatorio; dudosa"),
    ("con_marca", 18): ("ext::3.9::intro", False, "", False, False, "parte del título de la unidad"),
    ("con_marca", 19): ("lingob::4.2.1", True, "deber (recomendación)", False, False,
                        "«es conveniente que la mayoría… revistan la condición de independiente»: recomendación"),
    ("con_marca", 20): ("ext::3.11.2::intro", True, "condición", False, True,
                        "«en las siguientes condiciones» fija que los ítems son condiciones del acceso (§1.5); dudosa: el "
                        "tramo es solo el anuncio"),
    ("con_marca", 21): ("lingob::4.2.2", True, "deber (recomendación)", False, False,
                        "«se recomienda el establecimiento de otros comités especializados»"),
    ("con_marca", 22): ("lingob::7.1.7", True, "deber (recomendación)", False, False,
                        "«Es deseable incluir… la siguiente información»: la recomendación del encabezado"),
    ("con_marca", 23): ("ext::7.5.3", True, "facultad", True, False,
                        "«podrá conceder extensiones… en las siguientes circunstancias»: una facultad"),
    ("con_marca", 24): ("ext::10.11.5", True, "excepción", False, False,
                        "la excepción a la conformidad previa; no habilitante: niega la exigibilidad de un deber "
                        "(pre-registro de ESQ-3b v2)"),
    ("con_marca", 25): ("lingob::7.1.1", True, "deber (recomendación)", False, True,
                        "«es recomendable una apropiada divulgación de la información»; dudosa: el tramo empieza por la "
                        "finalidad"),
    ("con_marca", 26): ("cla::6.5.5.9", False, "", False, True,
                        "«sin perjuicio de…» aclara que la norma no excluye esas deudas; quitarla no cambia a qué se "
                        "aplica (§1.4); dudosa"),
    ("con_marca", 27): ("ext::8.5.22", True, "deber", False, False, "el deber de archivar la documentación"),
    ("con_marca", 28): ("ctacte::5.1.2.2", True, "alcance", False, False,
                        "delimita el sujeto (fiduciarios de fideicomisos comprendidos en la LEF)"),
    ("con_marca", 29): ("cap::3.1.1.5", True, "modalidad", False, True,
                        "cómo se determina la exigencia (por la realidad económica, no por la forma jurídica); dudosa: "
                        "también se lee como cláusula interpretativa"),
    ("con_marca", 30): ("ext::8.5.18.1", True, "deber", False, False, "el deber de archivar la documentación"),
}


# --------------------------------------------------------------------------------------------------------- ayudas
def norm(s) -> str:
    """Espacios simples, comillas rectas y sin el corte de palabra con guion de la E0 («dispo- siciones»)."""
    s = re.sub(r"\s+", " ", (s or "").replace("“", '"').replace("”", '"'))
    return re.sub(r"(\w)- (\w)", r"\1\2", s).strip()


def bloque_texto(cid: str) -> list[str]:
    t = K.texto(cid)
    out = []
    for h in t["heredado"]:
        out.append(f"> *heredado:* {norm(h)}")
    out.append(f"> *propio:* {norm(t['propio'])}")
    return out


def bloque_extraccion(x: dict) -> list[str]:
    out = [f"- Estado final: `{x['estado_final']}`; rechazos: {x['rechazos']}"]
    for e in x["entidades"]:
        if e["type"] == "TextoOrdenado":
            continue
        u = e.get("umbrales_tramos") or [u.get("tramo") for u in (e.get("properties") or {}).get("umbrales") or []]
        props = {k: v for k, v in (e.get("properties") or {}).items() if k != "umbrales" and v not in (None, "", [], {})}
        out.append(f"- **{e['local_id']} {e['type']}** «{e['label']}» — {e['descripcion'] or ''}"
                   + (f" · props: `{json.dumps(props, ensure_ascii=False)}`" if props else "")
                   + (f" · umbral: {u}" if u else "") + f" · tramo: «{norm(e['tramo'])}»")
    for r in x["relaciones"]:
        if r["predicate"] == "establecida_en":
            continue
        out.append(f"- R: {r['source']} —{r['predicate']}→ {r['target']}"
                   + (f" [{r['coherencia']}]" if r.get("coherencia") else ""))
    for o in x["omisiones"]:
        m = f" (marcas {o['marcas']})" if o.get("marcas") else ""
        out.append(f"- Omisión `{o['categoria']}`{m}: «{norm(o['tramo'])}» — {norm(o.get('nota'))}")
    for f in x.get("faltantes_e3") or []:
        out.append(f"- Faltante de E3 pendiente ({f.get('tipo')}, {f.get('severidad')}): «{norm(f.get('cita'))}»")
    return out


def escribir(salida: Path, nombre: str, datos: dict, md: list[str]) -> None:
    (salida / f"{nombre}.json").write_text(json.dumps(datos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (salida / f"{nombre}.md").write_text("\n".join(md) + "\n", encoding="utf-8")


# --------------------------------------------------------------------------------------------------------- puntos
def punto1(sorteos: dict, salida: Path) -> dict:
    muestra = [m["chunk_id"] for m in sorteos["punto_1_cola_humana"]["muestra_en_orden_del_sorteo"]]
    assert sorted(muestra) == sorted(LECTURA_1), "la lectura del punto 1 no cubre la muestra"
    filas, md = [], ["# Punto 1: cola humana, muestra de 30 de 74 (U-REEXT-T0, T4) — fichas para adjudicar", "",
                     "Criterio: error = al menos un nodo o una relación que el texto de la unidad no sostiene; las "
                     "omisiones van aparte. Extracción final (la que entra al grafo). Orden: el del sorteo "
                     "(salida/sorteos_t4.json). La clase es mi propuesta; adjudica la autora.", ""]
    for i, cid in enumerate(muestra, 1):
        clase, error, omis, obs = LECTURA_1[cid]
        assert (clase == S) == (not error), cid
        filas.append(OrderedDict([("n", i), ("chunk_id", cid), ("propuesta", clase), ("no_sostenido", error),
                                  ("omisiones_aparte", omis), ("observacion", obs)]))
        md += [f"## {i}. `{cid}` — propuesta: **{clase}**", ""] + bloque_texto(cid) + [""] + bloque_extraccion(
            K.extraccion(cid)) + ["", f"- **Lectura:** {error or 'nada que el texto no sostenga'}"]
        md += [f"- **Omisiones (aparte):** {omis}"] if omis else []
        md += [f"- **Observación:** {obs}"] if obs else []
        md.append("")
    cuenta = dict(Counter(f["propuesta"] for f in filas))
    res = {"unidades": len(filas), "propuesta": cuenta,
           "con_error": [f["chunk_id"] for f in filas if f["propuesta"] == E],
           "dudosas": [f["chunk_id"] for f in filas if f["propuesta"] == D],
           "con_omisiones_aparte": [f["chunk_id"] for f in filas if f["omisiones_aparte"]]}
    escribir(salida, "fichas_punto1_cola", {"resumen": res, "fichas": filas}, md)
    return res


def punto5(sellos: dict, salida: Path) -> dict:
    unidades = sellos["a_unidades_p4b"]["unidades"]
    assert sorted(u["id"] for u in unidades) == sorted(LECTURA_5), "la lectura del punto 5 no cubre las 27"
    p5 = {}
    for x in (P5 / "resultados_p5.jsonl").read_text(encoding="utf-8").splitlines():
        if x.strip():
            r = json.loads(x)
            if r["corrida"] in ("a", "b"):
                p5[(r["id"], r["corrida"])] = r["tool_input"]
    marcas_p5 = json.loads((P5 / "marcas_p5.json").read_text(encoding="utf-8"))["lectura"]
    filas, md = [], ["# Punto 5: las 27 unidades de P4b, tercera respuesta al pedido de P5 (U-REEXT-T0, T4) — fichas",
                     "", "Sobre la respuesta de E1 de esta corrida (tool_input_crudo), con las reglas de marcado de "
                     "P4b. Las 27 claves son las de P5 (freno T1, punto 3: 27/27). Variación contra las corridas a y "
                     "b de P5 con `analisis_p5.comparar`. La marca es mi propuesta; adjudica la autora.", ""]
    for u in unidades:
        cid, grupo = u["id"], u["grupo"]
        ti = K.extracciones_e1(cid.split("::")[0])[cid]["tool_input_crudo"]
        comp = {c: A5.comparar(p5[(cid, c)], ti) for c in ("a", "b")}
        iguales = [c for c in ("a", "b") if comp[c]["igual_byte_a_byte"] or comp[c]["igual_con_claves_ordenadas"]]
        marca, razon, dudosa = LECTURA_5[cid]
        if marca == IGUAL_A_P5:
            assert iguales, f"{cid}: la lectura dice idéntica a P5 y no lo es"
            mp = marcas_p5[cid][iguales[0]]
            marca, razon = mp["marca"], f"idéntica a P5 {iguales[0]}: {mp['razon']}"
        else:
            assert not iguales, f"{cid}: idéntica a P5 {iguales}; la marca debe ser la de P5"
        cambia = {c: marca != marcas_p5[cid][c]["marca"] for c in ("a", "b")}
        dif = {c: (None if c in iguales else comp[c]["diferencia"]) for c in ("a", "b")}
        filas.append(OrderedDict([("chunk_id", cid), ("grupo", grupo), ("marca", marca), ("razon", razon),
                                  ("dudosa", dudosa), ("identica_a_p5", iguales),
                                  ("diferencia_contra_p5", dif),
                                  ("marca_p5", {c: marcas_p5[cid][c]["marca"] for c in ("a", "b")}),
                                  ("cambia_la_marca_contra_p5", cambia)]))
        md += [f"## `{cid}` — grupo {grupo} — propuesta: **{marca}**{' (dudosa)' if dudosa else ''}", ""] + \
            bloque_texto(cid) + ["", "Respuesta de E1 de esta corrida:", ""] + bloque_extraccion(K.respuesta_e1(cid)) + \
            ["", f"- **Lectura:** {razon}",
             f"- **Contra P5:** idéntica a {', '.join(iguales) if iguales else 'ninguna'}; diferencia (esta menos P5) "
             f"a: `{json.dumps(dif['a'], ensure_ascii=False)}`, b: `{json.dumps(dif['b'], ensure_ascii=False)}`; marca "
             f"de P5 a/b: {marcas_p5[cid]['a']['marca']}/{marcas_p5[cid]['b']['marca']}", ""]
    por_grupo = OrderedDict()
    for f in filas:
        g = por_grupo.setdefault(f["grupo"], {"cumple": 0, "de": 0})
        g["de"] += 1
        g["cumple"] += f["marca"] == C
    res = {"unidades": len(filas), "por_grupo": por_grupo,
           "identicas_a_alguna_de_p5": sum(bool(f["identica_a_p5"]) for f in filas),
           "cambia_la_marca_contra_a": [f["chunk_id"] for f in filas if f["cambia_la_marca_contra_p5"]["a"]],
           "cambia_la_marca_contra_b": [f["chunk_id"] for f in filas if f["cambia_la_marca_contra_p5"]["b"]],
           "dudosas": [f["chunk_id"] for f in filas if f["dudosa"]]}
    escribir(salida, "fichas_punto5_p4b", {"resumen": res, "fichas": filas}, md)
    return res


def punto6(sellos: dict, salida: Path) -> dict:
    listas = sellos["b_listas_que_exceptuan"]["listas"]
    ids = [cid for lst in listas for cid in [lst["intro"]] + lst["items"]]
    assert sorted(ids) == sorted(LECTURA_6), "la lectura del punto 6 no cubre las listas"
    filas, md = [], ["# Punto 6: listas que exceptúan, b1 y b2 (U-REEXT-T0, T4) — fichas para adjudicar", "",
                     "Sobre la extracción final. b1: Excepcion del miembro con la norma exceptuada (ítems) y "
                     "Definicion de la clase (encabezado); b2: Condicion del supuesto con el cuantificador y la norma "
                     "exceptuada (ítems) y la norma unida a su excepción (encabezado). `ctacte::3.2` va aparte, "
                     "declarada. La marca es mi propuesta; adjudica la autora.", ""]
    for lst in listas:
        aparte = lst["contenedor"] == "ctacte::3.2"
        md += [f"# Lista `{lst['contenedor']}` ({lst['tipo']}){' — aparte, declarada' if aparte else ''}", ""]
        for cid in [lst["intro"]] + lst["items"]:
            marca, razon, dudosa = LECTURA_6[cid]
            rol = "encabezado" if cid == lst["intro"] else "ítem"
            filas.append(OrderedDict([("lista", lst["contenedor"]), ("tipo", lst["tipo"]), ("aparte", aparte),
                                      ("chunk_id", cid), ("rol", rol), ("marca", marca), ("razon", razon),
                                      ("dudosa", dudosa)]))
            md += [f"## `{cid}` ({rol}) — propuesta: **{marca}**{' (dudosa)' if dudosa else ''}", ""] + \
                bloque_texto(cid) + [""] + bloque_extraccion(K.extraccion(cid)) + ["", f"- **Lectura:** {razon}", ""]
    tabla = OrderedDict()
    for f in filas:
        k = ("aparte_" if f["aparte"] else "") + f"{f['tipo']}_{'encabezados' if f['rol'] == 'encabezado' else 'items'}"
        t = tabla.setdefault(k, {"cumple": 0, "de": 0})
        t["de"] += 1
        t["cumple"] += f["marca"] == C
    por_lista = OrderedDict()
    for f in filas:
        t = por_lista.setdefault(f["lista"], {"tipo": f["tipo"], "cumple": 0, "de": 0})
        t["de"] += 1
        t["cumple"] += f["marca"] == C
    res = {"listas": len(listas), "unidades": len(filas), "por_tipo_y_rol": tabla, "por_lista": por_lista,
           "dudosas": [f["chunk_id"] for f in filas if f["dudosa"]]}
    escribir(salida, "fichas_punto6_listas", {"resumen": res, "fichas": filas}, md)
    return res


def fase_a_del_archivo() -> dict:
    out = {}
    for x in FASE_A.read_text(encoding="utf-8").splitlines():
        m = re.match(r"\| (\d+) \| (\S+) \| (sí|no)", x)
        if m:
            out[int(m.group(1))] = (m.group(2), m.group(3) == "sí", "dudosa" in x.split("|")[3])
    return out


def punto7(sellos: dict, salida: Path) -> dict:
    orden = sellos["c_grupo_c"]["orden"]
    archivo = fase_a_del_archivo()
    assert archivo == FASE_A_7, "la fase A codificada no es la registrada en grupo_c_fase_a.md"
    assert all(orden[i - 1] == cid for i, (cid, _, _) in FASE_A_7.items()), "la fase A no sigue el orden sellado"
    con = [cid for i, (cid, mas, _) in sorted(FASE_A_7.items()) if mas]
    assert len(con) == 30 and FASE_A_7[max(FASE_A_7)][1], "la fase A debe cerrar en la unidad 30 con más de un supuesto"
    assert sorted(con) == sorted(LECTURA_7), "la fase B no cubre las 30"
    filas, md = [], ["# Punto 7: grupo c, una Condicion por supuesto (U-REEXT-T0, T4) — fichas para adjudicar", "",
                     "Fase A (registrada con su hora antes de mirar la extracción): `salida/grupo_c_fase_a.md`. Fase B: "
                     "la extracción final de las 30, con el criterio c de P4b. Etiquetas de la falla:", ""]
    md += [f"- `{k}`: {v}" for k, v in ETIQUETAS_7.items()] + [""]
    for i, (cid, mas, dud) in sorted(FASE_A_7.items()):
        if not mas:
            filas.append(OrderedDict([("orden", i), ("chunk_id", cid), ("mas_de_un_supuesto", False),
                                      ("dudosa_fase_a", dud)]))
            continue
        marca, etq, razon, dudosa = LECTURA_7[cid]
        assert set(etq) <= set(ETIQUETAS_7) and ((marca == C) == (not etq)), cid
        filas.append(OrderedDict([("orden", i), ("chunk_id", cid), ("mas_de_un_supuesto", True),
                                  ("dudosa_fase_a", dud), ("marca", marca), ("etiquetas", etq), ("razon", razon),
                                  ("dudosa", dudosa)]))
        md += [f"## {i}. `{cid}` — propuesta: **{marca}**{' (dudosa)' if dudosa else ''}"
               f"{' — dudosa en la fase A' if dud else ''}", ""] + bloque_texto(cid) + [""] + \
            bloque_extraccion(K.extraccion(cid)) + ["", f"- **Lectura:** {razon}",
                                                    f"- **Etiquetas:** {', '.join(etq) or '—'}", ""]
    leidas = [f for f in filas if f["mas_de_un_supuesto"]]
    res = {"leidas_en_fase_a": len(filas), "con_mas_de_un_supuesto": len(leidas),
           "salteadas": [f["chunk_id"] for f in filas if not f["mas_de_un_supuesto"]],
           "propuesta": {"cumple": sum(f["marca"] == C for f in leidas), "de": len(leidas)},
           "por_etiqueta": dict(Counter(e for f in leidas for e in f["etiquetas"]).most_common()),
           "dudosas": [f["chunk_id"] for f in leidas if f["dudosa"]],
           "dudosas_fase_a": [f["chunk_id"] for f in filas if f["dudosa_fase_a"]]}
    escribir(salida, "fichas_punto7_grupo_c", {"resumen": res, "fichas": filas}, md)
    return res


def punto8(sorteos: dict, salida: Path) -> dict:
    filas_om = [json.loads(x) for x in OMISIONES.read_text(encoding="utf-8").splitlines() if x.strip()]
    pos, por_clave = Counter(), {}
    for f in filas_om:
        por_clave[(f["chunk_id"], pos[f["chunk_id"]])] = f
        pos[f["chunk_id"]] += 1
    filas, md = [], ["# Punto 8: omisiones meta_normativo, 30 sin marca y 30 con marca (U-REEXT-T0, T4) — fichas", "",
                     "De cada omisión: si el tramo es contenido normativo según el §1 de la enmienda 7 a L-ESQ-R2 "
                     "(texto firmado en 44c6e1b) y si es habilitante (una norma cuyo efecto es que un sujeto pueda "
                     "realizar algo: pre-registro de ESQ-3b v2, 40493c9; enmienda 7, §4). Dónde está el tramo (texto "
                     "propio o heredado) lo ubica el script. La lectura es mi propuesta; adjudica la autora.", ""]
    for g in ("sin_marca", "con_marca"):
        md += [f"# Grupo {g.replace('_', ' ')}", ""]
        for i, m in enumerate(sorteos["punto_8_omisiones"][g]["muestra_en_orden_del_sorteo"], 1):
            cid, normativo, clase, habil, dudosa, razon = LECTURA_8[(g, i)]
            assert cid == m["chunk_id"], (g, i, cid, m["chunk_id"])
            assert normativo or not (clase or habil), (g, i)
            f = por_clave[(m["chunk_id"], m["posicion"])]
            assert f.get("categoria") == "meta_normativo", (g, i)
            tramo = norm(f.get("tramo_modelo") or f.get("tramo"))
            t = K.texto(cid)
            propio, heredado = norm(t["propio"]), " ".join(norm(h) for h in t["heredado"])
            donde = "propio" if tramo in propio else ("heredado" if tramo in heredado else "no_ubicado")
            assert donde != "no_ubicado", (g, i)
            filas.append(OrderedDict([("grupo", g), ("n", i), ("chunk_id", cid), ("posicion", m["posicion"]),
                                      ("marcas_del_contador", m["marcas"]), ("tramo", tramo), ("en", donde),
                                      ("normativo", normativo), ("clase", clase), ("habilitante", habil),
                                      ("dudosa", dudosa), ("razon", razon), ("nota_del_modelo", norm(f.get("nota")))]))
            md += [f"## {g} {i}. `{cid}` #{m['posicion']} — marcas {m['marcas'] or '—'} — texto {donde} — propuesta: "
                   f"**{'normativo' if normativo else 'no normativo'}**{' (' + clase + ')' if clase else ''}"
                   f"{', habilitante' if habil else ''}{' (dudosa)' if dudosa else ''}", "",
                   f"- **Tramo:** «{tramo}»", f"- **Nota del modelo:** {norm(f.get('nota')) or '—'}",
                   f"- **Lectura:** {razon}", ""] + bloque_texto(cid) + [""]
    res = OrderedDict()
    for g in ("sin_marca", "con_marca"):
        fs = [f for f in filas if f["grupo"] == g]
        her = [f for f in fs if f["en"] == "heredado"]
        res[g] = OrderedDict([
            ("leidas", len(fs)), ("normativas", sum(f["normativo"] for f in fs)),
            ("habilitantes", sum(f["habilitante"] for f in fs)),
            ("por_clase", dict(Counter(f["clase"] for f in fs if f["normativo"]).most_common())),
            ("dudosas", sum(f["dudosa"] for f in fs)),
            ("tramo_en_heredado", {"leidas": len(her), "normativas": sum(f["normativo"] for f in her),
                                   "habilitantes": sum(f["habilitante"] for f in her)}),
            ("tramo_en_propio", {"leidas": len(fs) - len(her),
                                 "normativas": sum(f["normativo"] for f in fs if f["en"] == "propio"),
                                 "habilitantes": sum(f["habilitante"] for f in fs if f["en"] == "propio")})])
    escribir(salida, "fichas_punto8_omisiones", {"resumen": res, "fichas": filas}, md)
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    a.salida.mkdir(parents=True, exist_ok=True)
    crudo = SELLOS.read_bytes()
    assert hashlib.sha256(crudo).hexdigest() == SHA_SELLOS, "sellos_t4.json no es el sellado en T1"
    sellos, sorteos = json.loads(crudo), json.loads(SORTEOS.read_text(encoding="utf-8"))
    res = OrderedDict([("nota", "propuestas de lectura a adjudicar por la autora; sin tasas ni intervalos"),
                       ("sorteos_t4_sha256", hashlib.sha256(SORTEOS.read_bytes()).hexdigest()),
                       ("grupo_c_fase_a_sha256", hashlib.sha256(FASE_A.read_bytes()).hexdigest()),
                       ("punto_1", punto1(sorteos, a.salida)), ("punto_5", punto5(sellos, a.salida)),
                       ("punto_6", punto6(sellos, a.salida)), ("punto_7", punto7(sellos, a.salida)),
                       ("punto_8", punto8(sorteos, a.salida))])
    (a.salida / "resumen_lecturas_t4.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
    print(json.dumps(res, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
