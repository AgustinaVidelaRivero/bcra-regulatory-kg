"""
l1_veredictos.py — U-LECTURA-ACEPTADAS, L1, puntos 2 y 3 (mandato FIRMADO en 9502ca4, §1, §4 y §5): la primera
lectura (la de la instancia, asistida, sin API) de las 60 fichas de fichas_l1.jsonl, en un archivo aparte de las
fichas para que la mesa lea a ciegas, y los conteos por estrato (k de 30) con los descriptivos por estado y por TO.
Sin estimadores ponderados: van en L2, con la adjudicación. USD 0.

Criterio (mandato §1, el del punto 1 de T4 de U-REEXT-T0): una unidad tiene error si al menos un nodo o una relación
suya no se sostiene en el texto de la unidad (propio o heredado); las omisiones van aparte y no cuentan. Reglas de
lectura que apliqué, calibradas con la lectura adjudicada de T4 (reext_t0/t4/salida/fichas_punto1_cola.json y
adjudicacion_autora.json):
  R1. Cuenta como error la modalidad cambiada (facultad, permiso o recomendación sin su marca leídos como deber; un
      deber acotado leído como prohibición), el sujeto equivocado en aplica_a (el deber de una parte atribuido a
      otra) y la relación que afirma lo que el texto no dice (destino equivocado, sentido invertido, una excepción
      que el texto no establece, una prohibición donde el texto fija una causal de rechazo).
  R2. No cuenta como error: la elección entre tipos cercanos con la descripción fiel y sin cambio deóntico, la
      propiedad `tipo` que no corresponde, el deber condicional leído como Condicion, la lectura laxa de un
      predicado (T4: cap::8.4.1.16) ni el aplica_a con una mención que no está en el texto cuando el sujeto
      resuelto es el que corresponde (T4: cap::6.2.2.4, adjudicada sin error). Van como observación o duda.
  R3. El tramo se comprueba contra el texto: uno no literal que une el encabezado heredado y el propio, con el
      contenido presente, es observación, no error.
  R4. remite_a (remision_derivada): juzgo si la cita está en el texto de la unidad (propio o heredado) y si el
      destino es el punto citado (TO y número). La atribución del origen (D1) y el reparto a los nodos del destino
      son de diseño (docs/plan_remite_a.md, decisiones 5 y D1) y no los juzgo. Las estructurales (establecida_en,
      referencia) y padre_sugerido se miran; un tipo documental equivocado (un punto o el título de una norma como
      Comunicacion) es observación, no error, porque no cambia el contenido normativo.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l) y escribe solo --salida/veredictos_l1.{jsonl,md} y
--salida/conteos_l1.json.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/lectura_aceptadas/l1_veredictos.py \
      --fichas <ruta>/fichas_l1.jsonl --cabecera <ruta>/fichas_l1_cabecera.json --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from datetime import datetime
from pathlib import Path

E, S = "con_error", "sin_error"
ESTRATOS = ("item", "no_item")


def ns(elemento: str, refs: str, por_que: str) -> dict:
    return {"elemento": elemento, "refs": refs.split(","), "por_que": por_que}


# Por unidad: (veredicto, lo no sostenido, omisiones aparte, dudas, observaciones).
LECTURA: dict[str, tuple] = {
    # ---------------------------------------------------------------------------------------- estrato item
    "cap::5.4.5": (E, [ns("arista", "A1", "N5 —exceptua→ N8 hace del reconocimiento parcial una excepción a la regla "
                                          "de no reconocer la CRC con plazo original inferior a un año o residual no "
                                          "mayor a tres meses; el texto no exceptúa esa regla: el reconocimiento "
                                          "parcial rige cuando el cómputo es factible, es decir, para la CRC con "
                                          "descalce que la regla anterior no excluye")],
                   "el ajuste P = P x (t – 0,25) / (T – 0,25) y sus variables no se extraen",
                   "«Cuando en estos casos sea factible el cómputo» admite una lectura literal en la que «estos casos» "
                   "son los excluidos; con esa lectura el texto se contradice («no será reconocida» y «será parcial»)",
                   "N1 («deberán medirse en forma conservadora») va como Condicion sin relación: deber leído como "
                   "condición (R2)"),
    "ext::3.17.3.4": (E, [ns("arista", "A2", "N3 —limita→ N2 limita la emisión de las «Certificaciones de aumento "
                                             "de exportaciones de bienes» (punto 3.18), que en el texto son el "
                                             "concepto que se deduce; lo que el tope limita es la emisión de las "
                                             "certificaciones del Decreto 277/22 («podrá emitir… por hasta el "
                                             "monto… neto de…», encabezado 3.17.3)")],
                      "la Potestad de emitir las certificaciones del Decreto 277/22 (heredado) no está en la unidad",
                      "", ""),
    "pro::3.2.3.1": (S, [], "la ubicación («en la sede en la cual desempeñe sus funciones el responsable…») no se "
                            "extrae", "",
                     "el tramo de N1 (verificado «no») une el final del encabezado heredado y el texto propio; el "
                     "contenido está en el texto (R3)"),
    "ext::3.5.6.9": (S, [], "", "", "remite_a a ext::3.5: la cita «comprendidos en este punto 3.5.» está en el "
                                    "encabezado heredado"),
    "cla::6.5.4.4": (S, [], "las tres Condicion no se vinculan a la categoría «con alto riesgo de insolvencia» de "
                            "la que son indicadores", "", ""),
    "ext::7.5.7.2": (S, [], "la Condicion no se vincula a la facultad de extender el plazo (heredado 7.5.7)", "", ""),
    "cap::2.11.3.2": (S, [], "las tres Condicion no se vinculan a la Definicion por condicion_de", "", ""),
    "cap::6.8.1": (S, [], "", "", "«tomar en consideración… enunciar» se lee como «deberán enunciar»: paráfrasis "
                                  "que no cambia el sentido"),
    "cla::6.5.5.5": (S, [], "la Condicion no se vincula a la categoría «irrecuperable»", "", ""),
    "ctacte::6.1.2.5": (E, [ns("nodo", "N2", "Restriccion «Prohibición — firmante inhabilitado en Central»: el "
                                              "texto define un defecto formal, causal de rechazo del cheque "
                                              "(encabezados 6.1 y 6.1.2), no prohíbe emitir"),
                            ns("arista", "A1", "N2 —prohibe→ N1 (emisión de cheque): misma razón")],
                        "la causal de rechazo como tal no se extrae", "", ""),
    "ctacte::12.1.2.7": (S, [], "el deber de la entidad de comunicar las recomendaciones a los usuarios (encabezado "
                                "12.1.2) no se extrae", "",
                         "N1 y N2 llevan la marca «Recomendación» en el rótulo y la descripción, como pide la lectura "
                         "de T4 (lingob::7.1.8); requiere de la Operacion de depósito hacia las recomendaciones es "
                         "lectura laxa (R2)"),
    "ctacte::8.3.5": (S, [], "", "", ""),
    "ext::8.5.17.14": (S, [], "", "la descripción de N3 aplica la condición del área franca también a las "
                                  "exportaciones «al resto del territorio de la Nación», que el texto no condiciona; "
                                  "N2, la Excepcion, la limita bien al área franca", ""),
    "ext::14.2.1.6": (S, [], "", "A3 resuelve el titular de la Potestad con la mención «entidades financieras "
                                 "locales», que en el texto son las que otorgaron la financiación; el titular es «las "
                                 "entidades» del encabezado 14.2.1. La clase resuelta (Entidades financieras) "
                                 "incluye al titular: la doy por sostenida (R2), pero puede leerse como sujeto "
                                 "equivocado (R1)",
                      "remite_a a ext::3.3, 3.5, 3.6 y 10.3.2: la cita está en el encabezado heredado"),
    "ext::7.9.1.1": (E, [ns("nodo", "N2", "Obligacion «Habilitación aplicación cobros exportaciones»: el texto "
                                          "habilita («estará habilitada»), es un permiso; leído como deber (como "
                                          "ext::8.5.13.2 en T4)")],
                     "N3 no remite a ext::3.5 aunque su tramo cita el punto 3.5", "", ""),
    "ext::4.6.1.4": (S, [], "el punto iii) de la declaración jurada (toma de conocimiento) no va como condición de "
                            "la verificación", "", ""),
    "ctacte::6.1.2.7": (E, [ns("nodo", "N3", "Restriccion «Prohibición giro sobre librador»: el texto define un "
                                              "defecto formal, causal de rechazo (encabezados 6.1 y 6.1.2), no "
                                              "prohíbe girar"),
                            ns("arista", "A2", "N3 —prohibe→ N2: misma razón"),
                            ns("arista", "A1", "N1 —exceptua→ N3 exceptúa una prohibición que el texto no "
                                               "establece; la salvedad es del defecto formal")],
                        "", "", ""),
    "cap::8.2.1.9": (S, [], "N3 (se restan los conceptos de 8.4.1 y 8.4.2) no remite a esos puntos", "",
                     "N2 tipa como Operacion «Emisión de acciones» un componente del capital y N3 como Restriccion "
                     "una regla de cálculo: tipos cercanos con la descripción fiel (R2)"),
    "ext::10.3.2.1": (S, [], "N11 (el total de pagos no supera lo facturado) no se vincula a la certificación", "",
                      ""),
    "ext::11.1.3.9": (S, [], "la unidad no aporta nodos de contenido: el dato que debe constar en la certificación "
                             "(código de concepto) no se extrae", "", ""),
    "lingob::2.3.2.1": (E, [ns("arista", "A1", "N1 —condicion_de→ N2 hace de los conflictos de intereses el "
                                               "supuesto de la obligación; en el texto son la situación que los "
                                               "procedimientos deben prevenir o limitar («tales como»): la "
                                               "obligación no se aplica cuando hay conflicto")],
                        "", "la modalidad: 2.3 enmarca el punto como buena práctica («se considera como buena "
                            "práctica que el Directorio…»); N2 va como Obligacion sin esa marca. No lo cuento porque "
                            "«se asegurará» es categórico",
                        ""),
    "ext::3.15.2.3": (S, [], "la Condicion no se vincula a la facultad de acceso (heredado 3.15.2)", "", ""),
    "ext::10.10.2.12": (S, [], "", "", "N1 —condicion_de→ N2 (los bienes en el Plan como condición del deber de "
                                       "contar con la documentación): lectura laxa (R2)"),
    "ext::10.6.6.2": (S, [], "", "", "N2 lleva `tipo` presentacion_informativa, que no corresponde (R2)"),
    "ext::2.6.1.2": (S, [], "la Excepcion no se vincula por exceptua_obligacion a la obligación de liquidar", "",
                     "N2 tipa como Condicion la regla del cierre (sin otro tratamiento diferencial): lectura "
                     "laxa (R2)"),
    "ctacte::12.1.2.1": (S, [], "", "", "A1 resuelve a Bancos con la mención «los bancos», que no está en el texto "
                                        "(«personal del banco»); el sujeto es el que corresponde (R2, T4: "
                                        "cap::6.2.2.4)"),
    "ext::11.1.3.1": (S, [], "la unidad no aporta nodos de contenido: el dato que debe constar en la certificación "
                             "(código de la entidad emisora) no se extrae", "", ""),
    "ext::7.8.2.5": (S, [], "la Potestad no se vincula por regula a la Operacion", "", ""),
    "ctacte::8.4.2": (S, [], "", "", ""),
    "ext::13.3.6": (S, [], "la Condicion no se vincula a la admisión del acceso (heredado 13.3)", "", ""),
    # ------------------------------------------------------------------------------------- estrato no_item
    "ext::1.7": (S, [], "", "", "la norma citada está fuera del inventario: sin remite_a, como corresponde"),
    "cap::6.1.4.2": (S, [], "", "la descripción de N4 («facultad de elegir») no recoge «según corresponda», que "
                                "acota la elección; el tramo sí lo trae",
                     "N1 y N2 tipan como Comunicacion los puntos 6.6.2 y 6.6.3 del mismo TO, con sus aristas "
                     "referencia: tipo documental (R4); la remisión ya está como remite_a"),
    "cap::2.12.2.7": (S, [], "", "", ""),
    "cla::1.2.1": (S, [], "", "", "N2 —condiciona→ N3 (la evaluación condiciona la imputación): lectura laxa (R2)"),
    "ext::5.8.1": (S, [], "la facultad de elaborar un boleto global diario (heredado 5.8) no se extrae", "",
                   "N1 —condicion_de→ N3 condiciona la Operacion con su propia descripción: lectura laxa (R2)"),
    "ric::11.1.4": (S, [], "las citas a «Lineamientos para la gestión de riesgos» quedan sin remite_a (fuera del "
                           "inventario)", "", "A1 resuelve «Las entidades del Grupo “A”» a la clase general; el "
                                               "rótulo de N1 conserva el Grupo A (R2)"),
    "ext::7.3.11": (E, [ns("nodo", "N4", "Obligacion «Certificación proporcional — múltiples entidades "
                                         "liquidadoras»: el texto dice «cada una podrá certificar», una facultad "
                                         "leída como deber"),
                        ns("arista", "A3", "N3 —aplica_a→ N9 atribuye el deber de «contar con la certificación de "
                                           "la entidad que cursó la operación de canje y/o arbitraje» a esa misma "
                                           "entidad, que es la que emite la certificación, no la que debe contar "
                                           "con ella")],
                    "", "", "C1 y C2 (padre_sugerido de los dos sujetos propuestos hacia las entidades autorizadas) "
                            "se sostienen"),
    "ric::8.1.7": (S, [], "el punto 5.1 citado queda sin remite_a", "",
                   "N1 infiere el deber de informar del renglón del régimen informativo («Código 70300000»): lectura "
                   "del régimen, no cambia el sentido"),
    "cla::9.1": (S, [], "", "", ""),
    "ext::10.2.4::cierre": (E, [ns("nodo", "N1", "Definicion rotulada «Deuda comercial por importación de bienes» "
                                                 "con el contenido de las deudas que NO encuadran como comerciales; "
                                                 "y el texto no define: fija el régimen aplicable a esos pagos (el "
                                                 "de los préstamos financieros)")],
                            "", "la propiedad `termino` sí nombra bien el concepto («deudas… que no encuadren como "
                                "deudas comerciales»); el error está en el rótulo y en el tipo", ""),
    "cap::3.1.1.6": (S, [], "", "", ""),
    "ctacte::1.5.2.9": (E, [ns("nodo", "N9", "Restriccion de tipo prohibicion «No verificar autenticidad de firma "
                                             "de endosantes»: el texto acota el deber («la regularidad de la serie "
                                             "de endosos pero no la autenticidad de la firma»), no prohíbe "
                                             "verificarla")],
                        "N2 (truncamiento) no se vincula por exceptua_obligacion a N5", "", ""),
    "ctacte::9.1.3": (E, [ns("arista", "A3", "N2 —condiciona→ N3 hace del cierre de cuentas un requisito del "
                                             "rechazo de cheques; en el texto es al revés: el rechazo sin percibir "
                                             "las multas es el supuesto del deber de cerrar")],
                      "", "puede leerse como lectura laxa de un predicado (R2); la cuento porque invierte el "
                          "sentido", ""),
    "cap::2.5.6": (S, [], "la Excepcion no se vincula por exceptua al tratamiento del sector público", "", ""),
    "ext::4.2::cierre": (S, [], "", "", "A3 resuelve el sujeto de la Restriccion con «las entidades», que no está "
                                        "en el texto (R2)"),
    "cap::8.2.2.2": (S, [], "", "la descripción agrega «en los casos de consolidación, se incluyen también en este "
                                "concepto»: el texto («Además, en los casos de consolidación, incluye:») abre la "
                                "lista siguiente; el agregado no contradice el texto, pero no lo dice", ""),
    "ext::3.11.5": (S, [], "", "", "remite_a de N3 y N7 a ext::3.11.1 y 3.11.2 con la cita de la primera oración: "
                                   "atribución D1, de diseño (R4)"),
    "pro::S5": (S, [], "", "N3 tipa como Obligacion la sujeción a sanciones («serán pasibles»); el esquema no tiene "
                           "un tipo para la sanción y la descripción es fiel",
                "N1 y N2 parten en dos Comunicacion el título de una sola norma, con leyes como código: tipo "
                "documental (R4)"),
    "ctacte::4.5.2::intro": (S, [], "", "", "bloque de apertura de lista: la unidad no aporta nodos de contenido"),
    "docvig::1.2.1": (S, [], "la unidad no aporta nodos de contenido: que la Libreta de Enrolamiento es documento "
                             "válido para mayores de 75 años e incapaces (encabezado 1.2) no se extrae", "", ""),
    "ric::11.2::intro": (S, [], "las descripciones de N1 y N2 no nombran los depósitos sin vencimiento "
                                "(40111 a 40116 y 40211 a 40216)", "",
                         "cuatro Definicion para cuatro cuadros: tipo documental con la descripción fiel"),
    "ext::13.1::cierre": (S, [], "", "", "N3 lee «quedan sujetos a la conformidad previa del BCRA» como Potestad "
                                         "del BCRA: tipo cercano (R2)"),
    "ric::10.1.2": (S, [], "la cita al punto 1.2 de las normas de ratio de apalancamiento queda sin remite_a (fuera "
                           "del inventario)", "",
                    "N2 lee «surgirá de aplicar la expresión» como deber de calcular, del régimen informativo; A1 con "
                    "mención no literal (R2)"),
    "cla::10.2.1": (S, [], "", "", "N1 (la cartera que corresponda) como Condicion y N3 —requiere→ N2: lecturas "
                                   "laxas (R2); el tramo de N3 (verificado «no») difiere en un artículo (R3)"),
    "lingob::1.3::intro": (S, [], "", "", "bloque de apertura de lista: la unidad no aporta nodos de contenido"),
    "pagjub::1.6": (S, [], "", "", ""),
    "ext::7.3.5": (S, [], "la admisión del caso (heredado 7.3, «en los casos admitidos en los puntos 7.3.1. a "
                          "7.3.11.») no se vincula", "", ""),
    "ctacte::10.2.2::intro": (S, [], "", "", "bloque de apertura de lista: la unidad no aporta nodos de contenido"),
    "ext::11.1.1::intro": (S, [], "", "", "bloque de apertura de lista: la unidad no aporta nodos de contenido"),
    "cap::3.1.3::cierre": (S, [], "", "", ""),
}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--fichas", type=Path, required=True)
    ap.add_argument("--cabecera", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()

    cab = json.loads(a.cabecera.read_text(encoding="utf-8"))
    s_fichas = sha(a.fichas.read_bytes())
    if s_fichas != cab["fichas_l1.jsonl_sha256"]:
        raise SystemExit(f"fichas_l1.jsonl con sha256 {s_fichas}, no el de su cabecera")
    fichas = [json.loads(x) for x in a.fichas.read_text(encoding="utf-8").splitlines() if x.strip()]
    ids = [f["id"] for f in fichas]
    if len(fichas) != 60 or set(ids) != set(LECTURA) or len(set(ids)) != 60:
        raise SystemExit(f"la lectura no cubre las 60 fichas: faltan {sorted(set(ids) - set(LECTURA))}, "
                         f"sobran {sorted(set(LECTURA) - set(ids))}")
    hora = datetime.now().astimezone().isoformat(timespec="seconds")

    filas, md = [], [
        "# U-LECTURA-ACEPTADAS, L1: primera lectura (la de la instancia) de las 60 fichas", "",
        f"Fichas: `fichas_l1.jsonl` (sha256 `{s_fichas}`). Veredictos generados a las {hora}. Criterio y reglas de "
        "lectura R1 a R4: cabecera de `l1_veredictos.py`. Las omisiones van aparte y no cuentan como error.", "",
        "| n | id | estrato | estado | veredicto | lo no sostenido |", "|--:|---|---|---|---|---|"]
    for f in fichas:
        ver, nosost, omis, dudas, obs = LECTURA[f["id"]]
        refs_ficha = {n["ref"] for n in f["nodos"]} | {x["ref"] for x in f["aristas"]}
        for x in nosost:
            for r in x["refs"]:
                if r not in refs_ficha:
                    raise SystemExit(f"{f['id']}: la referencia {r} no está en la ficha")
        if (ver == E) != bool(nosost):
            raise SystemExit(f"{f['id']}: veredicto {ver} con {len(nosost)} elementos no sostenidos")
        rem = [x for x in f["aristas"] if x["clase"] == "remision_derivada"]
        filas.append({"n": f["n"], "id": f["id"], "estrato": f["estrato"], "to": f["to"], "estado": f["estado"],
                      "veredicto": ver, "no_sostenido": nosost, "omisiones": omis, "dudas": dudas,
                      "observaciones": obs,
                      "remisiones_derivadas": {"aristas": len(rem),
                                               "destinos": sorted({x["properties"].get("destino") for x in rem}),
                                               "no_sostenidas": 0},
                      "nodos_de_contenido": sum(1 for n in f["nodos"] if n["type"] not in ("TextoOrdenado",
                                                                                          "Sujeto"))})
        md.append(f"| {f['n']} | `{f['id']}` | {f['estrato']} | {f['estado']} | {ver} | "
                  + ("; ".join(f"{x['elemento']} {','.join(x['refs'])}" for x in nosost) or "—") + " |")
    md.append("")
    for x in filas:
        if x["veredicto"] == E or x["dudas"]:
            md.append(f"- **{x['n']}. `{x['id']}`** ({x['veredicto']})")
            for y in x["no_sostenido"]:
                md.append(f"  - no sostenido, {y['elemento']} {', '.join(y['refs'])}: {y['por_que']}")
            if x["dudas"]:
                md.append(f"  - duda: {x['dudas']}")

    # conteos (sin estimadores ponderados: L2)
    def tabla(clave: str) -> dict:
        out = {}
        for e in ESTRATOS:
            c = Counter((x[clave], x["veredicto"]) for x in filas if x["estrato"] == e)
            out[e] = {v: {"con_error": c[(v, E)], "de": c[(v, E)] + c[(v, S)]}
                      for v in sorted({x[clave] for x in filas if x["estrato"] == e})}
        return out
    por_estrato = {e: {"k": sum(1 for x in filas if x["estrato"] == e and x["veredicto"] == E),
                       "n": sum(1 for x in filas if x["estrato"] == e)} for e in ESTRATOS}
    conteos = {
        "unidad": "U-LECTURA-ACEPTADAS, L1 (primera lectura; sin adjudicar)", "hora": hora,
        "fichas_l1.jsonl_sha256": s_fichas, "sellos_l0_sha256": cab["sellos_l0_sha256"],
        "por_estrato": por_estrato,
        "total_muestra": {"k": sum(v["k"] for v in por_estrato.values()), "n": len(filas),
                          "nota": "suma sin ponderar, solo descriptiva; la tasa del grafo es la ponderada de L2"},
        "por_estado": tabla("estado"), "por_to": tabla("to"),
        "elementos_no_sostenidos": {e: dict(Counter(y["elemento"] for x in filas if x["estrato"] == e
                                                    for y in x["no_sostenido"]
                                                    for _ in y["refs"])) for e in ESTRATOS},
        "remisiones_derivadas": {"aristas": sum(x["remisiones_derivadas"]["aristas"] for x in filas),
                                 "unidades_con_remisiones": sum(1 for x in filas
                                                                if x["remisiones_derivadas"]["aristas"]),
                                 "no_sostenidas": 0},
        "unidades_sin_nodos_de_contenido": {e: sorted(x["id"] for x in filas if x["estrato"] == e
                                                      and x["nodos_de_contenido"] == 0) for e in ESTRATOS},
        "con_omisiones": {e: sum(1 for x in filas if x["estrato"] == e and x["omisiones"]) for e in ESTRATOS},
        "con_dudas": sorted(x["id"] for x in filas if x["dudas"]),
        "l1_veredictos.py_sha256": sha(Path(__file__).read_bytes()),
    }
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "veredictos_l1.jsonl").write_text("\n".join(json.dumps(x, ensure_ascii=False) for x in filas) + "\n",
                                                  encoding="utf-8")
    (a.salida / "veredictos_l1.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    (a.salida / "conteos_l1.json").write_text(json.dumps(conteos, ensure_ascii=False, indent=1) + "\n",
                                              encoding="utf-8")
    print(json.dumps({"hora": hora, "por_estrato": por_estrato, "total": conteos["total_muestra"]["k"],
                      "elementos": conteos["elementos_no_sostenidos"],
                      "remisiones": conteos["remisiones_derivadas"],
                      "sin_contenido": {e: len(v) for e, v in conteos["unidades_sin_nodos_de_contenido"].items()},
                      "con_omisiones": conteos["con_omisiones"], "con_dudas": len(conteos["con_dudas"])},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
