"""U-R2-CODIGO, decisión 5 sobre el FRENO R3 — desglose por causa de las
remisiones que se pierden al pasar a la regla firmada de `remite_a` (detección
sobre el texto de E0 del punto, desde cada procedencia, con atribución D1). Dos
conjuntos de referencia, que no se mezclan:

  A. las remisiones de los grafos sellados (aristas `referencia` con
     `rol_fuente = referencia_cruzada`) que la regla firmada no reproduce:
     KG-Tanda0-Desarrollo-r1, KG-Tanda0-Diez-r1 y KG-Reextraído-r1. Son las que el
     grafo pierde respecto de hoy;
  B. los pares origen → destino del conjunto por paráfrasis con los siete tipos de
     origen (la variante de la cadena r1 de la simulación de U-AUDIT-TIPOS-V3:
     paráfrasis, procedencia primaria, sin `termino`; 7.929 pares en desarrollo)
     que la regla firmada no reproduce. Se informa también el conteo contra el
     conjunto con cada procedencia y `termino` (7.940), que es contra el que se
     midió el 656 de R3.

Para cada par perdido toma la cita de la referencia que lo produjo (la cadena r1
reproducida en memoria, que da exactamente los pares sellados) y la busca, con
el mismo detector, en el texto de E0 del punto de esa procedencia
(r1_referencias._texto_e0_de, normalizar_e0), en el texto de los puntos
superiores que el chunk hereda, en el texto propio de los chunks emisores y en
el de las otras procedencias del nodo. Causas, en este orden:
  - e0_cita_a_otra_norma: el texto del punto cita esa unidad con el nombre de
    otra norma (o de una fuera del inventario); la paráfrasis lo había perdido;
  - e0_misma_cita_atribuida_a_otros_nodos: el texto del punto tiene la misma
    cita; D1 la dio a los nodos del punto que contienen la unidad y el origen no
    la contiene;
  - e0_misma_cita_par_ausente: la misma cita, el origen la contiene y el par no
    aparece (se lista);
  - cita_literal_no_detectada (con subtipo): el número de la unidad está en el
    texto del punto en una cita que el detector no toma;
  - anafora_del_punto: el texto dice «este punto» o «el presente punto» y la
    paráfrasis le puso número;
  - cita_de_un_punto_superior: la cita está en el texto de un punto superior que
    el chunk hereda; se informa si la remisión queda desde ese punto;
  - cita_del_punto_que_extrajo_el_nodo: la procedencia es de herencia y la cita
    está en el texto propio de un chunk emisor (de otro punto); se informa si la
    remisión queda desde ese punto;
  - cita_de_otra_procedencia_del_nodo: la cita está en el texto de otra
    procedencia del mismo nodo;
  - unidad_ausente_del_texto_de_e0: ningún texto de E0 del nodo la cita; la
    paráfrasis la agregó.
Una unidad de un rango que la paráfrasis expandió y que no es literal recibe la
causa de las otras unidades de la misma cita.

Veredicto por cita (lectura mía, sin revisión de la autora, en LECTURA para las
causas que no se deciden solas): «pérdida real» (la cita está en el texto de E0 y
la regla firmada no la toma o la resuelve mal), «corrección» (la remisión sellada
o de la paráfrasis era falsa), «queda desde otro punto», «no es una cita del
texto» o «límite declarado» (lo deja afuera una regla decidida por la autora:
(h) anáfora sin número, (i) nodo que no nombra la unidad, (g) norma fuera del
inventario).

Desde las decisiones sobre el freno posterior a R3, la regla firmada lleva las
nueve reglas del detector (a a i) y, con `--e0-r2`, el texto de e0-r2 (regla
b); la clasificación usa el mismo detector y el mismo texto. Con `--reglas ""`
reproduce el desglose de ese freno. Solo lectura, en memoria. USD 0.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r3_perdidas_remisiones.py --out <json> \
      [--e0-r2 <salida de correr_e0.py --version-e0 e0-r2 de la tanda 0>] [--reglas abcdefghi]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import r3d_remisiones as D  # noqa: E402
from r3d_remisiones import C, REF  # noqa: E402

MUESTRA = 5
RE_ANAFORA = re.compile(r"\b(?:este|el presente|dicho)\s+punto\b", re.I)
REALES = ("cita_literal_no_detectada",)
# (procedencia, unidad de destino o «*») → (veredicto, lectura)
LECTURA: dict[tuple[str, str], tuple[str, str]] = {
    ("cap::2.12.2.8 (punto_propio)", "cap::4.1.1"): (
        "corrección", "el texto de E0 dice «del TO sobre Financiamiento al Sector Público no Financiero»: el "
                      "4.1.1 es de otra norma, fuera del inventario"),
    ("cap::8.2.3.3 (punto_propio)", "cap::6.5.1"): (
        "corrección", "«de las normas sobre “Clasificación de deudores”»: la remisión va a cla::6.5.1"),
    ("cla::6.5.5.8 (punto_propio)", "cla::3.1"): (
        "corrección", "«puntos 3.1. y 3.2. … de las normas sobre “Evaluaciones crediticias”»: otra norma"),
    ("ctacte::1.5.2.3 (punto_propio)", "ctacte::3.2"): (
        "corrección", "«punto 3.2. de las normas sobre “Sistema Nacional de Pagos – Transferencias”»: otra norma"),
    ("cap::2.1 (punto_propio)", "cap::S2"): (
        "corrección", "«la Sección 2. del TO sobre Incumplimientos de Capitales Mínimos y Relaciones Técnicas»: la "
                      "sección es de otra norma, fuera del inventario; la cadena r1 la resolvía a cap por la "
                      "subcadena «capitales mínimos» (regla g)"),
    ("cap::8.5 (bloque_cierre)", "cap::1.4"): (
        "pérdida real (declarada)", "«lo previsto por el punto 1.4. de estas normas y la Sección 1. de las normas "
                                    "sobre “Incumplimientos de capitales mínimos…”»: el 1.4 es de cap («de estas "
                                    "normas»); la regla (d) solo mira otros puntos y la mención más cercana a la "
                                    "norma es una sección, así que el 1.4 queda atribuido a Incumplimientos, que con "
                                    "la regla (g) está fuera del inventario. La cadena r1 acertaba por la subcadena"),
    ("cap::2.1 (punto_propio)", "cap::3.2.4"): (
        "corrección", "«el punto 5.1. del TO sobre Financiamiento al Sector Público no Financiero y el punto 3.2.4. del "
                      "citado ordenamiento»: el 3.2.4 es de esa norma, fuera del inventario (regla e); la remisión "
                      "sellada interna era falsa"),
    ("polcre::9.1 (punto_propio)", "polcre::TO"): (
        "límite declarado (g)", "«TO sobre Política de Crédito en forma individual»: sin comillas, el nombre sigue "
                                "con texto corrido y no coincide con el título"),
    ("polcre::9.2 (punto_propio)", "polcre::TO"): (
        "límite declarado (g)", "«TO de Política de Crédito sobre base consolidada mensual»: sin comillas, el nombre "
                                "sigue con texto corrido y no coincide con el título"),
    ("ric::S2 (punto_propio)", "ric::6.2"): (
        "corrección", "«el punto 6.2. de las normas citadas»: las normas citadas son las de «Supervisión "
                      "consolidada», nombradas antes en el punto y fuera del inventario (regla e); la remisión "
                      "sellada interna era falsa"),
    ("ric::10.1.2 (punto_propio)", "ric::1.2"): (
        "corrección", "«el punto 1.2. de las citadas normas»: son las normas sobre «Ratio de apalancamiento», "
                      "nombradas en el punto anterior (ric::10.1.1); la remisión sellada interna era falsa y la cita "
                      "queda irresoluble como anáfora sin antecedente (regla e)"),
    ("pagjub::2.2 (punto_propio)", "*"): (
        "límite declarado (g)", "cita el TO propio por su nombre completo («Pago de beneficios de la seguridad social "
                                "por cuenta de la Administración Nacional de la Seguridad Social»); el título del "
                                "inventario está abreviado («seg. soc.», «Adm.») y no coincide"),
    ("cla::5.1.2.3 (punto_propio)", "cla::3.7"): (
        "pérdida real", "«establecido en el punto 3.7.– y a microemprendedores (según lo previsto en el punto "
                        "1.1.3.4. de las normas sobre “Gestión crediticia”)»: la ventana de 120 caracteres atribuye "
                        "también el 3.7 a la norma nombrada después de otro punto; el 3.7 es de cla y la cita "
                        "queda irresoluble"),
    ("ric::3.1.2 (punto_propio)", "cap::4.1.1"): (
        "pérdida real", "«punto 4.1.1. de las citadas normas»: la anáfora de la norma no se reconoce y la cita "
                        "se resuelve como interna (ric::4.1.1)"),
    ("ric::3.1.6 (punto_propio)", "cap::4.2.1.3"): (
        "pérdida real", "«punto 4.2.1.3. de las citadas disposiciones»: la anáfora de la norma no se reconoce y "
                        "la cita se resuelve como interna (ric::4.2.1.3)"),
    ("ric::9.1.1 (punto_propio)", "ric::S2"): (
        "corrección", "la norma es «Incumplimientos de capitales mínimos y relaciones técnicas», fuera del "
                      "inventario: la remisión sellada a ric::S2 era falsa. La arista ric::9.1.1 → cap::S2 de la "
                      "regla viene de otra cita del mismo punto («Sección 2. de las normas sobre “Capitales mínimos "
                      "de las entidades financieras”»)"),
    ("ext::10.11.7.3 (punto_propio)", "ext::10.11.7"): (
        "límite declarado (h)", "«en el marco de los mecanismos previstos en este punto»: remite al punto que lo "
                                "contiene sin nombrarlo; queda en el registro como anáfora sin número"),
    ("cla::6.5.4.10 (punto_propio)", "*"): (
        "no es una cita del texto", "el texto del punto no cita el 6.5.4; la paráfrasis nombra el punto padre"),
    ("ext::11.1.3.6 (punto_propio)", "*"): (
        "no es una cita del texto", "el texto del punto no cita el 11.1.3; la paráfrasis nombra el punto padre"),
    ("ext::13.3.8 (punto_propio)", "*"): (
        "no es una cita del texto", "el texto del 13.3.8 no cita los puntos 13.3.1 a 13.3.8; la paráfrasis los "
                                    "enumera"),
}
LECTURA_LITERAL = {
    "token_suelto_entre_punto_y_numero": "un subíndice que E0 extrae como línea suelta queda entre «punto» y el número",
    "celdas_de_tabla_intercaladas": "las celdas de la tabla linealizada quedan entre «punto» y el número",
    "rango_o_lista_cortado_por_parentesis": "un paréntesis corta la lista o el rango de puntos",
    "otra_forma": "la cita no usa «punto»",
}


def veredicto(f: dict, reglas: frozenset = frozenset()) -> tuple[str, str]:
    if (f["procedencia"], f["unidad_destino"]) in LECTURA:
        return LECTURA[(f["procedencia"], f["unidad_destino"])]
    if f["causa"] == "cita_literal_no_detectada":
        return "pérdida real", LECTURA_LITERAL.get(f["subtipo"], f["subtipo"])
    if f["causa"] in ("cita_de_un_punto_superior", "cita_del_punto_que_extrajo_el_nodo"):
        if f["remision_conservada_desde_otro_punto"]:
            return "queda desde otro punto", "la remisión queda desde el punto cuyo texto la cita"
        if "i" in reglas and f["causa"] == "cita_de_un_punto_superior" and not f.get("origen_nombra_la_unidad"):
            return "límite declarado (i)", "la cita está en el texto heredado y el nodo de origen no nombra la unidad"
        return "pérdida real", "la remisión no queda desde el punto cuyo texto la cita"
    if f["causa"] == "anafora_del_punto" and "h" in reglas:
        return "límite declarado (h)", "anáfora sin número: queda en el registro, sin remisión"
    return LECTURA.get((f["procedencia"], f["unidad_destino"])) or LECTURA.get((f["procedencia"], "*")) \
        or ("SIN LECTURA", "")
VARIANTE_R1 = dict(fuente="parafrasis", por_procedencia=False, propios="nodo", leer_termino=False)


def re_numero(d: str) -> re.Pattern:
    if d.startswith("S"):
        return re.compile(r"\bSecci(?:o|ó)n(?:es)?\s+(?:\d+\s*(?:,|y)\s*)*" + re.escape(d[1:]) + r"\b", re.I)
    return re.compile(r"(?<![\d.])" + re.escape(d) + r"(?!\.?\d)")


def cita(m: dict, d: str) -> bool:
    return d in m["puntos"] if not d.startswith("S") else d[1:] in m["secciones"]


def subtipo_literal(texto: str, pat: re.Pattern) -> str:
    m = pat.search(texto)
    antes = texto[max(0, m.start() - 70):m.start()]
    if re.search(r"\bpuntos?\s+(?:\S{1,3}\s+){1,2}$", antes, re.I):
        return "token_suelto_entre_punto_y_numero"
    if re.search(r"\)\s*(?:a|al|y|hasta)\s+$", antes):
        return "rango_o_lista_cortado_por_parentesis"
    if re.search(r"\bpuntos?\b[^.;]*\d+(?:,\d+)?\s*%", antes, re.I) or re.search(r"\bpuntos?\s+[A-ZÁÉÍÓÚ]", antes):
        return "celdas_de_tabla_intercaladas"
    return "otra_forma"


def recorte(texto: str, pat: re.Pattern, ancho: int = 110) -> str:
    m = pat.search(texto)
    return texto[:2 * ancho] if not m else texto[max(0, m.start() - ancho):m.end() + ancho]


def clasificar(perdidos: list, ref: dict, re0: dict, kg: dict, em: dict,
               reglas: frozenset = frozenset(), e0r2: dict | None = None) -> dict:
    nodos = {n["id"]: n for n in kg["nodes"]}
    chunks = {c["id"]: c for to in C.TOS_ORDEN for c in C.cargar_chunks_enm01(to)}
    if "b" in reglas and e0r2:
        chunks.update({k: v for k, v in e0r2.items() if k in chunks})
    linea = "a" in reglas

    def detectar(t: str, to: str) -> list[dict]:
        return [m for m in REF.detectar_menciones_r2(t, to, reglas) if m["clase"] != "anafora_sin_numero"]
    por_par: dict[tuple, dict] = {}
    for c in ref["registro"]:
        for d in c["destinos"]:
            for o in c["origenes"]:
                for t in d["nodos"]:
                    por_par.setdefault((o, t), {"cita": c, "destino": d["destino"]})
    destinos_e0 = {(e["provenance"]["to"], e["provenance"]["punto"], e["properties"]["destino"])
                   for e in re0["nuevas"]}

    def texto_punto(p: dict) -> tuple:
        cid = REF._chunk_de_procedencia(p, em)
        ch = chunks.get(cid)
        if ch is None:
            return cid, "", ""
        propio = REF.normalizar_e0(REF._texto_e0_de(p, ch), linea)[0]
        sup = REF.normalizar_e0("\n".join(h["texto"] for h in ch.get("herencia", [])
                                          if h["unidad_origen"] != p.get("punto")), linea)[0]
        return cid, propio, sup

    def texto_del_chunk(cid) -> str:
        ch = chunks.get(cid)
        return REF.normalizar_e0(ch["texto"], linea)[0] if ch else ""

    filas = []
    for src, tgt in perdidos:
        c, destino = por_par[(src, tgt)]["cita"], por_par[(src, tgt)]["destino"]
        td, d = destino.split("::", 1)
        p = c["procedencia"]
        cid, propio, superior = texto_punto(p)
        pat = re_numero(d)
        m_propio = [m for m in detectar(propio, p["to"]) if cita(m, d)] if propio else []
        m_sup = [m for m in detectar(superior, p["to"]) if cita(m, d)] if superior else []
        otros = []
        for q in nodos[src]["provenances"]:
            if REF._chunk_de_procedencia(q, em) != cid:
                _, tq, _ = texto_punto(q)
                otros += [m for m in detectar(tq, q.get("to")) if cita(m, d)] if tq else []
        sub, conservada = None, None
        if any(m["to_destino"] != td for m in m_propio):
            causa = "e0_cita_a_otra_norma"
        elif m_propio:
            causa = ("e0_misma_cita_atribuida_a_otros_nodos"
                     if not REF._contiene_unidad(REF._texto_r2(nodos[src]), m_propio[0], reglas or None)
                     else "e0_misma_cita_par_ausente")
        elif pat.search(propio):
            causa, sub = "cita_literal_no_detectada", subtipo_literal(propio, pat)
        elif RE_ANAFORA.search(propio):
            causa = "anafora_del_punto"
        elif m_sup:
            causa = "cita_de_un_punto_superior"
            conservada = any(x[2] == destino and x[0] == p["to"] for x in destinos_e0 if x[1] != p["punto"])
        elif (p.get("rol_documental") or "").startswith("herencia_") and any(
                cita(m, d) for e in (em.get((p["to"], p["punto"], p.get("rol_documental"))) or [cid])
                for m in detectar(texto_del_chunk(e), p["to"])):
            causa = "cita_del_punto_que_extrajo_el_nodo"
            conservada = any(x[2] == destino and x[0] == p["to"] for x in destinos_e0 if x[1] != p["punto"])
        elif otros:
            causa = "cita_de_otra_procedencia_del_nodo"
        else:
            causa = "unidad_ausente_del_texto_de_e0"
        nombra = (REF.nombra_unidad(REF._texto_r2(nodos[src]), seccion=d[1:]) if d.startswith("S")
                  else REF.nombra_unidad(REF._texto_r2(nodos[src]), punto=d))
        filas.append({
            "causa": causa, "subtipo": sub, "remision_conservada_desde_otro_punto": conservada,
            "origen_nombra_la_unidad": nombra,
            "origen": src, "tipo_origen": nodos[src]["type"], "label_origen": nodos[src]["label"],
            "texto_guardado_origen": REF._texto_r2(nodos[src])[:300],
            "destino_nodo": tgt, "tipo_destino": nodos[tgt]["type"], "unidad_destino": destino,
            "procedencia": f"{p['to']}::{p['punto']} ({p.get('rol_documental')})", "chunk_id": cid,
            "evidencia_referencia": c["evidencia"],
            "menciones_e0_de_la_unidad": [{k: m[k] for k in ("clase", "to_destino", "puntos", "secciones",
                                                              "norma_nombrada")} for m in m_propio],
            "texto_e0_del_punto": recorte(propio, pat),
            "texto_e0_superior": recorte(superior, pat) if causa == "cita_de_un_punto_superior" else None})
    por_cita: dict[tuple, list] = {}
    for f in filas:
        por_cita.setdefault((f["procedencia"], f["evidencia_referencia"]), []).append(f)
    for f in filas:
        if f["causa"] == "unidad_ausente_del_texto_de_e0":
            h = next((g for g in por_cita[(f["procedencia"], f["evidencia_referencia"])]
                      if g["causa"] == "cita_literal_no_detectada"), None)
            if h is not None:
                f.update(causa=h["causa"], subtipo=h["subtipo"], unidad_de_un_rango=True)
    for f in filas:
        f["veredicto"], f["lectura"] = veredicto(f, reglas)
    clave = lambda f: f["causa"] + (f" / {f['subtipo']}" if f["subtipo"] else "")  # noqa: E731
    cuenta = Counter(clave(f) for f in filas)
    citas = {k: sorted({(f["procedencia"], f["unidad_destino"]) for f in filas if clave(f) == k}) for k in cuenta}
    muestras = {}
    for k in sorted(cuenta):
        vistas, ms = set(), []
        for f in filas:
            if clave(f) == k and (f["procedencia"], f["unidad_destino"]) not in vistas:
                vistas.add((f["procedencia"], f["unidad_destino"]))
                ms.append(f)
            if len(ms) == MUESTRA:
                break
        muestras[k] = ms
    cons = [f for f in filas if f["remision_conservada_desde_otro_punto"] is not None]
    ver = Counter(f["veredicto"] for f in filas)
    citas_ver = {v: sorted({(f["procedencia"], f["unidad_destino"]) for f in filas if f["veredicto"] == v})
                 for v in ver}
    reales = sorted({(f["procedencia"], f["evidencia_referencia"]) for f in filas
                     if f["veredicto"].startswith("pérdida real") or f["veredicto"] == "SIN LECTURA"})
    return {"pares_perdidos": len(filas),
            "por_veredicto": {v: {"pares": n, "citas": len(citas_ver[v])} for v, n in sorted(ver.items())},
            "citas_con_perdida_real": [{"procedencia": pr, "unidades": sorted({f["unidad_destino"] for f in filas
                                                                                 if f["procedencia"] == pr
                                                                                 and f["evidencia_referencia"] == ev}),
                                        "veredicto": next(f["veredicto"] for f in filas if f["procedencia"] == pr),
                                        "lectura": next(f["lectura"] for f in filas if f["procedencia"] == pr
                                                        and f["evidencia_referencia"] == ev)}
                                       for pr, ev in reales],
            "por_causa": dict(sorted(cuenta.items())),
            "citas_distintas_por_causa": {k: len(v) for k, v in sorted(citas.items())},
            "nodos_de_origen_por_causa": {k: len({f["origen"] for f in filas if clave(f) == k})
                                          for k in sorted(cuenta)},
            "remision_conservada_desde_otro_punto": {
                k: dict(Counter(str(f["remision_conservada_desde_otro_punto"]) for f in cons if f["causa"] == k))
                for k in sorted({f["causa"] for f in cons})},
            "perdidas_reales": {k: v for k, v in sorted(cuenta.items()) if k.split(" / ")[0] in REALES},
            "citas_de_perdidas_reales": {k: v for k, v in sorted(citas.items()) if k.split(" / ")[0] in REALES},
            "muestras": muestras, "filas": filas}


def resumen(r: dict) -> dict:
    return {k: r[k] for k in ("pares_referencia", "pares_regla_firmada", "pares_perdidos", "por_veredicto",
                              "por_causa", "citas_distintas_por_causa", "citas_con_perdida_real") if k in r}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--e0-r2", type=Path, default=None,
                    help="salida de correr_e0.py --version-e0 e0-r2 de la tanda 0 (regla b)")
    ap.add_argument("--reglas", default="".join(sorted(REF.REGLAS_R2)),
                    help="reglas del detector r2 (por defecto, todas; \"\" = la regla del freno posterior a R3)")
    a = ap.parse_args()
    reglas = frozenset(a.reglas)
    out: dict = {"unidad": "U-R2-CODIGO", "etapa": "decisiones sobre el freno posterior a R3",
                 "reglas": "".join(sorted(reglas)), "e0_r2": bool(a.e0_r2),
                 "A_remisiones_selladas_que_se_pierden": {}, "B_parafrasis_siete_tipos_desarrollo": None}
    for nombre in ("desarrollo", "diez", "r1"):
        with D.redirigido(nombre):
            kg, base, sellados = D.cargar(nombre)
            em = D.emisores()
            r4 = D.correr(base, em, tipos_origen=D.ORIG4, **VARIANTE_R1)
            if r4["pares"] != sellados:
                raise SystemExit(f"{nombre}: la cadena r1 en memoria no reproduce los pares sellados")
            e0r2 = D.chunks_e0_r2(a.e0_r2)
            re0 = D.correr(base, em, reglas=reglas, chunks_e0_r2=e0r2)
            r = clasificar(sorted(sellados - re0["pares"]), r4, re0, kg, em, reglas, e0r2)
            r = {"grafo": f"{nombre} ({D.SHA[nombre]})", "pares_referencia": len(sellados),
                 "pares_regla_firmada": len(re0["pares"]), **r}
            out["A_remisiones_selladas_que_se_pierden"][nombre] = r
            if nombre == "desarrollo":
                r7 = D.correr(base, em, **VARIANTE_R1)
                rp = D.correr(base, em, fuente="parafrasis", por_procedencia=True, propios="procedencia",
                              leer_termino=True)
                b = clasificar(sorted(r7["pares"] - re0["pares"]), r7, re0, kg, em, reglas, e0r2)
                out["B_parafrasis_siete_tipos_desarrollo"] = {
                    "grafo": f"desarrollo ({D.SHA['desarrollo']})", "pares_referencia": len(r7["pares"]),
                    "pares_regla_firmada": len(re0["pares"]),
                    "conteo_contra_cada_procedencia_y_termino": {"pares_referencia": len(rp["pares"]),
                                                                 "pares_perdidos": len(rp["pares"] - re0["pares"])},
                    **b}
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"A": {k: resumen(v) for k, v in out["A_remisiones_selladas_que_se_pierden"].items()},
                      "B": resumen(out["B_parafrasis_siete_tipos_desarrollo"]),
                      "B_contra_7940": out["B_parafrasis_siete_tipos_desarrollo"][
                          "conteo_contra_cada_procedencia_y_termino"]}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
