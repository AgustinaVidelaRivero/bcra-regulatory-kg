"""U-PROC-HERENCIA — selftest de C1 y C2 (`tanda0/code/ensamblar_tanda0.py`: `corregir_procedencia_g_r` con
`procedencia_heredada`, `procedencia_heredada_c1_c2`, `bloque_ubicado_g_r` e `id_nodo_e2_r2`) y del detector de remisiones
con el punto de E1 (`corpus_v2/r1_referencias.py`: `detectar_y_resolver_r2` con `punto_declarado_e1`), una rama por caso
del §4 del mandato y de la opción D, sobre unidades armadas a mano en el selftest, sin datos del corpus:

  1. declarada con el punto propio y con el tramo solo en un párrafo heredado de un ancestro: C1 cambia el punto y el
     rol, guarda lo declarado, y C2 marca;
  2. el tramo en el texto propio, en un título, en el bloque que abre la lista (también en el bloque contiguo que va
     con él, y el ubicado por tokens en ese bloque) o en ninguna parte, y el que cruza un título y un párrafo: ni C1
     ni C2;
  3. sin tramo: ni C1 ni C2;
  4. un mini-chunk (el tramo en su bloque, y el que empieza en su último título y sigue en el bloque): ni C1 ni C2;
  5. una Comunicacion, fuera de TIPOS_G_R: C1 no cambia nada y C2 marca;
  6. declarada con un ancestro: G-r como siempre (la misma salida con la bandera prendida y apagada), y C2 marca si
     corresponde;
  7. con la bandera apagada: la salida de G-r del código de HEAD, igual. El `ensamblar_tanda0.py` de HEAD lo da
     --ensamblar-head; se ejecuta con el `__file__` del entregado, para que resuelva las mismas rutas;
  8. la unión evitada (opción D, (b)): con el id nuevo que ya es el de un nodo y con dos entidades que C1 llevaría al
     mismo id, C1 no se aplica, la entidad queda con lo que declaró E1, C2 la marca y la fila va a
     `uniones_evitadas`; E2 (`e2_lib.ensamblar_r2`) da los mismos nodos con la bandera y sin ella. Una entidad de un
     registro que E2 no lleva al grafo no cuenta como nodo;
  9. el detector con el punto de E1 (opción D, (c)): en una procedencia que corrigió C1, las citas que lee y
     resuelve y las aristas que salen de su grupo son las de sin la bandera, salvo el id del origen; leída con el
     punto de C1 (sin `punto_declarado_e1`) cambian. Los destinos siguen el punto de C1: lo que cambia tiene un
     extremo en el nodo de C1;
 10. con la bandera apagada, la salida del detector es la del `r1_referencias.py` de HEAD (--referencias-head), sobre
     el grafo sin C1 y sobre el grafo con C1.
Las ramas 9 y 10 corren el detector sobre un TO armado a mano: el inventario de E0 (`r1_comun.TOS_ORDEN`,
`cargar_chunks_enm01`, `cargar_estructura_enm01`) y los títulos de la regla (g) se reemplazan en memoria mientras corren.

Corre desde una COPIA del repo; no escribe nada. USD 0, sin API.
Uso: PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/proc_herencia/selftest_procedencia_heredada.py
     --ensamblar-head <ensamblar_tanda0.py de HEAD> --referencias-head <r1_referencias.py de HEAD>
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import json
import sys
import types
from copy import deepcopy
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parents[3]
ENS_PATH = REPO / "data" / "experiment" / "tanda0" / "code" / "ensamblar_tanda0.py"
sys.path.insert(0, str(ENS_PATH.parent))
import ensamblar_tanda0 as ENS  # noqa: E402

REF, C = ENS.REF, ENS.C
REF_PATH = Path(REF.__file__).resolve()
V = ENS.E4.modulo_validador_r2()
HOLGURA = V.politica_default().holgura
CAMPOS_NUEVOS = ("punto_declarado_e1", "rol_declarado_e1", "tramo_fuera_del_texto_de_e3")
RES: list[tuple[str, str, bool, str]] = []


def check(grupo: str, nombre: str, ok: bool, detalle: str = "") -> None:
    RES.append((grupo, nombre, bool(ok), str(detalle)[:300]))


def chunk(cid, unidad, texto, herencia=(), **extra):
    return {"id": cid, "to": "syn", "archivo": "syn.pdf", "unidad": unidad, "texto": texto, "herencia": list(herencia),
            "paginas": [1], "tipo": "punto_terminal", "titulo": "", **extra}


# Un ítem de una lista: el bloque que abre la lista es el «intro» de 5.1 (termina en «:» y después solo hay un
# cierre). E3 ve los títulos de 5 y de 5.1, ese bloque y el texto propio; E1 ve además el «chapeau_seccion» de 5 y el
# «cierre» de 5.1.
ITEM = chunk("syn::5.1.2", "5.1.2", "5.1.2. Lugar y fecha de emisión.", [
    {"unidad_origen": "5", "tipo": "encabezado", "texto": "5. Depósitos."},
    {"unidad_origen": "5", "tipo": "chapeau_seccion",
     "texto": "Las entidades financieras informarán los saldos diarios al cierre de cada jornada."},
    {"unidad_origen": "5.1", "tipo": "encabezado", "texto": "5.1. Boletas de depósito."},
    {"unidad_origen": "5.1", "tipo": "intro", "texto": "Las boletas deben contener los siguientes datos:"},
    {"unidad_origen": "5.1", "tipo": "cierre", "texto": "El incumplimiento dará lugar a las sanciones previstas."}])
# El bloque que abre la lista partido en dos bloques contiguos del mismo tipo y la misma unidad (D2 de U-E3-LISTAS).
ITEM_PARTIDO = chunk("syn::6.1.1", "6.1.1", "6.1.1. Firma del titular.", [
    {"unidad_origen": "6", "tipo": "encabezado", "texto": "6. Cheques."},
    {"unidad_origen": "6.1", "tipo": "encabezado", "texto": "6.1. Requisitos."},
    {"unidad_origen": "6.1", "tipo": "intro", "texto": "Los cheques librados por personas humanas"},
    {"unidad_origen": "6.1", "tipo": "intro", "texto": "deberán contener:"}])
# Un mini-chunk: el bloque «chapeau_seccion» de 7, con su cadena de títulos.
MINI = chunk("syn::7#b1", "7", "Las cuentas se abrirán a solicitud del titular.", [
    {"unidad_origen": "7", "tipo": "encabezado", "texto": "7. Cuentas."}], tipo="mini_chunk",
    rol_bloque="chapeau_seccion")
# Un mini-chunk a mitad de oración: la última línea de títulos es el comienzo de la oración del bloque.
MINI_MITAD = chunk("syn::4.2#b1", "4.2", "la información dentro de los diez días.", [
    {"unidad_origen": "4", "tipo": "encabezado", "texto": "4. Régimen informativo."},
    {"unidad_origen": "4.2", "tipo": "encabezado", "texto": "4.2. Las entidades deberán remitir"}], tipo="mini_chunk",
    rol_bloque="intro")
CHUNKS = {c["id"]: c for c in (ITEM, ITEM_PARTIDO, MINI, MINI_MITAD)}


def reg(ch, punto, rol, tramo, tipo="Obligacion", lid="e1", con_tramo=True):
    prov = {"to": "syn", "archivo": "syn.pdf", "punto": punto, "rol_documental": rol}
    if con_tramo:
        prov["tramo"] = tramo
    return {"chunk_id": ch["id"], "validacion": {"entidades": [
        {"local_id": lid, "type": tipo, "label": "x", "punto": punto, "provenance": prov}]}}


def correr(r, flag=True, modulo=ENS):
    res = modulo.corregir_procedencia_g_r([r], CHUNKS, V, HOLGURA, procedencia_heredada=flag) if flag else \
        modulo.corregir_procedencia_g_r([r], CHUNKS, V, HOLGURA)
    return res, r["validacion"]["entidades"][0]


def nada(r, res, e, antes):
    """Ni C1 ni C2: la entidad queda como entró y la bandera no registra C1 ni C2."""
    ph = res["procedencia_heredada"]
    return e == antes and not ph["c1"] and not ph["c2"] and not ph["uniones_evitadas"] and not res["cambios"]


def s_c1_c2() -> None:
    g = "1 C1 y C2"
    for nombre, tramo, esperado in (
            ("el tramo solo en el chapeau de un ancestro", "Las entidades financieras informarán los saldos diarios",
             ("5", "herencia_chapeau_seccion")),
            ("el tramo solo en el cierre del punto que contiene la lista", "El incumplimiento dará lugar a las "
                                                                            "sanciones previstas",
             ("5.1", "herencia_cierre"))):
        r = reg(ITEM, "5.1.2", "punto_propio", tramo)
        res, e = correr(r)
        p, ph = e["provenance"], res["procedencia_heredada"]
        check(g, f"{nombre}: el punto y el rol pasan al bloque", (p["punto"], p["rol_documental"]) == esperado
              and e["punto"] == esperado[0], p)
        check(g, f"{nombre}: lo declarado por E1 queda en la procedencia",
              (p.get("punto_declarado_e1"), p.get("rol_declarado_e1")) == ("5.1.2", "punto_propio"), p)
        check(g, f"{nombre}: C2 marca", p.get("tramo_fuera_del_texto_de_e3") is True and len(ph["c2"]) == 1, ph["c2"])
        check(g, f"{nombre}: una fila de C1, sin cambios de G-r y con el chunk_id de la unidad",
              len(ph["c1"]) == 1 and not res["cambios"] and ph["c1"][0]["punto_c1"] == esperado[0]
              and ph["c1"][0]["rol_c1"] == esperado[1] and r["chunk_id"] == "syn::5.1.2", ph["c1"])


def s_ninguno() -> None:
    g = "2 ni C1 ni C2"
    casos = (("el tramo en el texto propio", ITEM, "Lugar y fecha de emisión", None),
             ("el tramo en el título de un ancestro", ITEM, "Boletas de depósito", None),
             ("el tramo en el bloque que abre la lista", ITEM, "Las boletas deben contener los siguientes datos", None),
             ("el tramo en el bloque contiguo que va con el que abre la lista (D2)", ITEM_PARTIDO,
              "Los cheques librados por personas humanas", None),
             ("el tramo ubicado por tokens en el bloque que abre la lista (condición 3)", ITEM,
              "Las boletas contener los siguientes datos", ("parrafo", True)),
             ("el tramo en ninguna parte", ITEM, "otra cosa que no está en la unidad", ("no_ubicado", None)),
             ("el tramo que cruza el título y el párrafo de un ancestro", ITEM,
              "Depósitos. Las entidades financieras informarán", ("cruza_titulo_y_parrafo", None)))
    for nombre, ch, tramo, sin_c1 in casos:
        r = reg(ch, ch["unidad"], "punto_propio", tramo)
        antes = deepcopy(r["validacion"]["entidades"][0])
        res, e = correr(r)
        ph = res["procedencia_heredada"]
        check(g, nombre, nada(r, res, e, antes), (e, ph))
        filas = ph["c1_sin_las_otras_dos"]
        if sin_c1 is None:
            check(g, f"{nombre}: no cumple la condición 1, no figura entre las de C1 sin las otras dos", not filas, filas)
        else:
            check(g, f"{nombre}: figura entre las de C1 sin las otras dos, con su lugar",
                  len(filas) == 1 and filas[0]["lugar"] == sin_c1[0]
                  and filas[0]["bloque_que_abre_la_lista"] == sin_c1[1], filas)


def s_sin_tramo() -> None:
    g = "3 sin tramo"
    for nombre, r in (("sin la clave tramo", reg(ITEM, "5.1.2", "punto_propio", None, con_tramo=False)),
                      ("con tramo None", reg(ITEM, "5.1.2", "punto_propio", None)),
                      ("con tramo vacío", reg(ITEM, "5.1.2", "punto_propio", ""))):
        antes = deepcopy(r["validacion"]["entidades"][0])
        res, e = correr(r)
        check(g, nombre, nada(r, res, e, antes) and not res["procedencia_heredada"]["c1_sin_las_otras_dos"], (e, res))


def s_mini() -> None:
    g = "4 mini-chunk"
    r = reg(MINI, "7", "bloque_chapeau_seccion", "Las cuentas se abrirán a solicitud del titular")
    antes = deepcopy(r["validacion"]["entidades"][0])
    res, e = correr(r)
    check(g, "el tramo en el bloque del mini-chunk: ni C1 ni C2", nada(r, res, e, antes)
          and not res["procedencia_heredada"]["c1_sin_las_otras_dos"], (e, res))
    r = reg(MINI_MITAD, "4.2", "bloque_intro", "Las entidades deberán remitir la información dentro de los diez días")
    antes = deepcopy(r["validacion"]["entidades"][0])
    res, e = correr(r)
    filas = res["procedencia_heredada"]["c1_sin_las_otras_dos"]
    check(g, "a mitad de oración, el tramo del último título y el bloque: ni C1 ni C2", nada(r, res, e, antes), (e, res))
    check(g, "a mitad de oración: fuera del texto de E3 (los rótulos), ubicado en el texto propio",
          len(filas) == 1 and filas[0]["lugar"] == "texto_propio", filas)


def s_comunicacion() -> None:
    g = "5 Comunicacion"
    r = reg(ITEM, "5.1.2", "punto_propio", "Las entidades financieras informarán los saldos diarios", tipo="Comunicacion")
    res, e = correr(r)
    p, ph = e["provenance"], res["procedencia_heredada"]
    check(g, "C1 no cambia el punto ni el rol", (p["punto"], p["rol_documental"]) == ("5.1.2", "punto_propio")
          and e["punto"] == "5.1.2" and "punto_declarado_e1" not in p and "rol_declarado_e1" not in p
          and not ph["c1"] and not ph["c1_sin_las_otras_dos"], p)
    check(g, "C2 marca", p.get("tramo_fuera_del_texto_de_e3") is True and len(ph["c2"]) == 1, ph)


def s_ancestro() -> None:
    g = "6 declarada con un ancestro"
    casos = (("el tramo en el cierre de 5.1: G-r da el rol del bloque y C2 marca",
              ("5.1", "herencia_encabezado", "El incumplimiento dará lugar a las sanciones previstas"),
              ("5.1", "herencia_cierre"), True),
             ("el tramo en el bloque que abre la lista: G-r da el rol del bloque y C2 no marca",
              ("5.1", "herencia_encabezado", "Las boletas deben contener los siguientes datos"),
              ("5.1", "herencia_intro"), False),
             ("el tramo en el texto propio por tokens: G-r lo pasa a la unidad, C1 no lo toca y C2 no marca",
              ("5.1", "herencia_encabezado", "Lugar fecha de emisión"), ("5.1.2", "punto_propio"), False),
             ("el tramo en el chapeau de 5, declarado con 5.1: G-r lo pasa a 5 y C2 marca",
              ("5.1", "herencia_encabezado", "Las entidades financieras informarán los saldos diarios"),
              ("5", "herencia_chapeau_seccion"), True))
    for nombre, (punto, rol, tramo), esperado, marca in casos:
        r_on, r_off = reg(ITEM, punto, rol, tramo), reg(ITEM, punto, rol, tramo)
        res_on, e_on = correr(r_on)
        res_off, e_off = correr(r_off, flag=False)
        p = e_on["provenance"]
        ph = res_on["procedencia_heredada"]
        check(g, f"{nombre}: G-r", (p["punto"], p["rol_documental"]) == esperado and not ph["c1"]
              and "punto_declarado_e1" not in p and "rol_declarado_e1" not in p, (p, ph))
        check(g, f"{nombre}: la salida de G-r es la misma con la bandera apagada",
              {k: v for k, v in res_on.items() if k != "procedencia_heredada"} == res_off
              and {k: v for k, v in p.items() if k not in CAMPOS_NUEVOS} == e_off["provenance"], (res_on, res_off))
        check(g, f"{nombre}: C2", (p.get("tramo_fuera_del_texto_de_e3") is True) == marca
              and len(ph["c2"]) == int(marca), ph["c2"])


def bateria() -> list[dict]:
    """Los registros de todas las ramas, para comparar la bandera apagada con HEAD."""
    out = []
    for ch, tramos in ((ITEM, ("Las entidades financieras informarán los saldos diarios", "El incumplimiento dará "
                                "lugar a las sanciones previstas", "Lugar y fecha de emisión", "Boletas de depósito",
                                "Las boletas deben contener los siguientes datos", "Las boletas contener los "
                                "siguientes datos", "otra cosa que no está en la unidad", "Depósitos. Las entidades "
                                "financieras informarán", "Lugar fecha de emisión", None, "",
                                "Las boletas deben contener los siguientes datos: […] Lugar y fecha de emisión")),
                       (ITEM_PARTIDO, ("Los cheques librados por personas humanas", "Firma del titular")),
                       (MINI, ("Las cuentas se abrirán a solicitud del titular",)),
                       (MINI_MITAD, ("Las entidades deberán remitir la información dentro de los diez días",))):
        rol_propio = f"bloque_{ch['rol_bloque']}" if ch.get("tipo") == "mini_chunk" else "punto_propio"
        puntos = [(ch["unidad"], rol_propio)] + sorted({(h["unidad_origen"], f"herencia_{h['tipo']}")
                                                        for h in ch["herencia"] if h["unidad_origen"] != ch["unidad"]})
        for tramo in tramos:
            for punto, rol in puntos:
                for tipo in ("Obligacion", "Definicion", "Comunicacion"):
                    out.append(reg(ch, punto, rol, tramo, tipo=tipo))
    return out


def blob(p: Path) -> str:
    b = p.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def s_bandera_apagada(head: Path | None) -> None:
    g = "7 bandera apagada"
    if head is None:
        check(g, "falta --ensamblar-head", False)
        return
    src = head.read_text(encoding="utf-8")
    H = types.ModuleType("ensamblar_tanda0_head")
    H.__file__ = str(ENS_PATH)
    exec(compile(src, str(head), "exec"), H.__dict__)  # noqa: S102 — el código de HEAD, con las rutas del entregado
    check(g, f"el código de HEAD no tiene la bandera (blob {blob(head)[:12]})",
          "procedencia_heredada" not in src and "procedencia_heredada" in ENS_PATH.read_text(encoding="utf-8"))
    regs = bateria()
    r_head, r_ent = deepcopy(regs), deepcopy(regs)
    res_head = H.corregir_procedencia_g_r(r_head, CHUNKS, V, HOLGURA)
    res_ent = ENS.corregir_procedencia_g_r(r_ent, CHUNKS, V, HOLGURA)
    res_ent_f = ENS.corregir_procedencia_g_r(deepcopy(regs), CHUNKS, V, HOLGURA, procedencia_heredada=False)
    check(g, f"la salida de G-r es la de HEAD ({len(regs)} registros, {res_head['entidades_que_cambian']} cambios)",
          json.dumps(res_head, sort_keys=True) == json.dumps(res_ent, sort_keys=True) == json.dumps(res_ent_f,
                                                                                                   sort_keys=True)
          and res_head["entidades_que_cambian"] > 0, (res_head, res_ent))
    check(g, "los registros quedan como con HEAD, sin los campos nuevos",
          json.dumps(r_head, sort_keys=True) == json.dumps(r_ent, sort_keys=True)
          and not any(k in e["provenance"] for r in r_ent for e in r["validacion"]["entidades"] for k in CAMPOS_NUEVOS))
    r_on = deepcopy(regs)
    res_on = ENS.corregir_procedencia_g_r(r_on, CHUNKS, V, HOLGURA, procedencia_heredada=True)
    ph = res_on["procedencia_heredada"]
    # La batería repite la misma entidad en todos los puntos del chunk: con la bandera, el id que C1 le daría ya es el
    # de otro nodo, y C1 pasa a unión evitada (rama 8). Uno por uno, C1 se aplica.
    sueltos = [ENS.corregir_procedencia_g_r([r], CHUNKS, V, HOLGURA, procedencia_heredada=True)["procedencia_heredada"]
               for r in deepcopy(regs)]
    n = {k: len(v) for k, v in ph.items()}
    check(g, f"con la bandera prendida, la batería da C2 y C1 pasa a unión evitada, y G-r no cambia ({n})",
          n["c1"] == 0 and n["uniones_evitadas"] > 0 and n["c2"] > 0
          and json.dumps({k: v for k, v in res_on.items() if k != "procedencia_heredada"}, sort_keys=True)
          == json.dumps(res_head, sort_keys=True), n)
    def claves(filas):
        return sorted(json.dumps([f[k] for k in ("chunk_id", "type", "tramo", "punto", "punto_c1", "rol_c1")],
                                 ensure_ascii=False) for f in filas)
    check(g, "registro por registro, la batería da C1 en las mismas entidades, sin uniones evitadas",
          claves([f for x in sueltos for f in x["c1"]]) == claves(ph["uniones_evitadas"])
          and not any(x["uniones_evitadas"] for x in sueltos),
          [sum(len(x[k]) for x in sueltos) for k in ("c1", "uniones_evitadas")])


# --- 8. La unión evitada ------------------------------------------------------------------------------------------------
# El mini-chunk del chapeau de 5 (el nodo de la unidad de origen) y dos ítems hermanos de 5.1 que heredan ese chapeau.
MINI5 = chunk("syn::5#b1", "5", "Las entidades financieras informarán los saldos diarios al cierre de cada jornada.", [
    {"unidad_origen": "5", "tipo": "encabezado", "texto": "5. Depósitos."}], tipo="mini_chunk", rol_bloque="chapeau_seccion")
ITEM3 = chunk("syn::5.1.3", "5.1.3", "5.1.3. Firma del depositante.", ITEM["herencia"])
CHAPEAU = "Las entidades financieras informarán los saldos diarios"


def ent(lid, punto, rol, tramo, desc="Informar los saldos diarios", tipo="Obligacion"):
    return {"local_id": lid, "type": tipo, "label": "x", "punto": punto, "properties": {"descripcion": desc},
            "provenance": {"to": "syn", "archivo": "syn.pdf", "punto": punto, "rol_documental": rol, "tramo": tramo}}


def registro(ch, *ents, rechazado=False):
    val = {"entidades": list(ents), "relaciones": []}
    if rechazado:
        val["rechazos"] = [{"nivel": "chunk", "motivo": "sintético"}]
    return {"chunk_id": ch["id"], "validacion": val}


def nodos_e2(chs, regs) -> list[str]:
    """Los ids de los nodos que arma E2 (`e2_lib.ensamblar_r2`, fase r2b) con estos registros."""
    ens = ENS.e2_lib.ensamblar_r2(chs, deepcopy(regs), {}, frozenset(), lambda *a: True, ENS.TIPOS_G_R, (), [],
                                  fase="r2b")
    return [n["id"] for n in ens["nodes"]]


def s_union_evitada() -> None:
    g = "8 unión evitada"
    # (a) el id nuevo ya es el de un nodo: la entidad del chapeau en su mini-chunk
    chs = [MINI5, ITEM]
    regs = [registro(MINI5, ent("e1", "5", "bloque_chapeau_seccion", CHAPEAU)),
            registro(ITEM, ent("e1", "5.1.2", "punto_propio", CHAPEAU))]
    on, off = deepcopy(regs), deepcopy(regs)
    ph = ENS.corregir_procedencia_g_r(on, {c["id"]: c for c in chs}, V, HOLGURA, procedencia_heredada=True)[
        "procedencia_heredada"]
    ENS.corregir_procedencia_g_r(off, {c["id"]: c for c in chs}, V, HOLGURA)
    p = on[1]["validacion"]["entidades"][0]["provenance"]
    ev = ph["uniones_evitadas"]
    check(g, "con un nodo que ya existe: C1 no se aplica y la entidad queda con lo que declaró E1",
          not ph["c1"] and (p["punto"], p["rol_documental"]) == ("5.1.2", "punto_propio")
          and "punto_declarado_e1" not in p and "rol_declarado_e1" not in p, (p, ph))
    check(g, "con un nodo que ya existe: C2 la marca igual", p.get("tramo_fuera_del_texto_de_e3") is True
          and len(ph["c2"]) == 1 and ph["c2"][0]["punto"] == "5.1.2", ph["c2"])
    id_mini = ENS.id_nodo_e2_r2(on[0]["validacion"]["entidades"][0], MINI5["id"])
    check(g, "con un nodo que ya existe: el contador sube, con el id que C1 le habría dado (el del nodo)",
          len(ev) == 1 and ev[0]["con"] == "nodo_existente" and ev[0]["id_c1"] == id_mini
          and (ev[0]["punto"], ev[0]["punto_c1"], ev[0]["rol_c1"]) == ("5.1.2", "5", "herencia_chapeau_seccion"), ev)
    check(g, "con un nodo que ya existe: E2 da los mismos nodos con la bandera y sin ella (2)",
          nodos_e2(chs, on) == nodos_e2(chs, off) and len(nodos_e2(chs, on)) == 2 and id_mini in nodos_e2(chs, on))
    # (b) dos entidades que C1 llevaría al mismo id: gana la primera en el orden de E0, aunque llegue después
    chs = [ITEM, ITEM3]
    regs = [registro(ITEM3, ent("e1", "5.1.3", "punto_propio", CHAPEAU)),
            registro(ITEM, ent("e1", "5.1.2", "punto_propio", CHAPEAU))]
    on, off = deepcopy(regs), deepcopy(regs)
    ph = ENS.corregir_procedencia_g_r(on, {c["id"]: c for c in chs}, V, HOLGURA, procedencia_heredada=True)[
        "procedencia_heredada"]
    ENS.corregir_procedencia_g_r(off, {c["id"]: c for c in chs}, V, HOLGURA)
    p3, p2 = (r["validacion"]["entidades"][0]["provenance"] for r in on)
    ev = ph["uniones_evitadas"]
    check(g, "dos entidades al mismo id: C1 se aplica a la primera del orden de E0",
          [f["chunk_id"] for f in ph["c1"]] == [ITEM["id"]] and p2["punto"] == "5"
          and p2.get("punto_declarado_e1") == "5.1.2", (ph["c1"], p2))
    check(g, "dos entidades al mismo id: la segunda queda con lo que declaró E1 y el contador sube",
          (p3["punto"], p3["rol_documental"]) == ("5.1.3", "punto_propio") and "punto_declarado_e1" not in p3
          and len(ev) == 1 and ev[0]["chunk_id"] == ITEM3["id"] and ev[0]["con"] == "c1_en_otra_entidad"
          and ev[0]["id_c1"] == ENS.id_nodo_e2_r2(on[1]["validacion"]["entidades"][0], ITEM["id"]), (p3, ev))
    check(g, "dos entidades al mismo id: C2 marca las dos",
          p2.get("tramo_fuera_del_texto_de_e3") is True and p3.get("tramo_fuera_del_texto_de_e3") is True
          and len(ph["c2"]) == 2, ph["c2"])
    check(g, "dos entidades al mismo id: E2 da la misma cantidad de nodos con la bandera y sin ella (2)",
          len(nodos_e2(chs, on)) == len(nodos_e2(chs, off)) == 2)
    # (c) la entidad de un registro que E2 no lleva al grafo no es un nodo: C1 se aplica
    chs = [MINI5, ITEM]
    regs = [registro(MINI5, ent("e1", "5", "bloque_chapeau_seccion", CHAPEAU), rechazado=True),
            registro(ITEM, ent("e1", "5.1.2", "punto_propio", CHAPEAU))]
    on = deepcopy(regs)
    ph = ENS.corregir_procedencia_g_r(on, {c["id"]: c for c in chs}, V, HOLGURA, procedencia_heredada=True)[
        "procedencia_heredada"]
    check(g, "con el mismo id en un registro rechazado: C1 se aplica y no hay unión evitada",
          len(ph["c1"]) == 1 and not ph["uniones_evitadas"]
          and on[1]["validacion"]["entidades"][0]["provenance"]["punto"] == "5", ph)


# --- 9 y 10. El detector de remisiones ----------------------------------------------------------------------------------
HER_R = [{"unidad_origen": "5", "tipo": "encabezado", "texto": "5. Depósitos."},
         {"unidad_origen": "5", "tipo": "chapeau_seccion", "texto": "Las entidades informarán los saldos diarios."},
         {"unidad_origen": "5.1", "tipo": "encabezado", "texto": "5.1. Boletas de depósito."},
         {"unidad_origen": "5.1", "tipo": "intro", "texto": "Las boletas deben contener los siguientes datos:"},
         {"unidad_origen": "5.1", "tipo": "cierre", "texto": "El incumplimiento dará lugar a las sanciones del punto 3.3."}]
HER_3 = [{"unidad_origen": "3", "tipo": "encabezado", "texto": "3. Requisitos."}]
DET_CHUNKS = [chunk("syn::3.1", "3.1", "3.1. Requisitos de emisión.", HER_3),
              chunk("syn::3.3", "3.3", "3.3. Sanciones aplicables a lo dispuesto en el punto 5.1.", HER_3),
              chunk("syn::5.1.1", "5.1.1", "5.1.1. Nombre del titular, salvo lo previsto en el punto 5.1.2.", HER_R),
              chunk("syn::5.1.2", "5.1.2", "5.1.2. Lugar y fecha de emisión, conforme al punto 3.1.", HER_R)]


def nodo(punto, chunk_id, desc, tramo, **prov):
    """Un nodo de E2 con una procedencia (la de una entidad de `ent`), con su id de E2."""
    e = ent("e1", punto, "punto_propio", tramo, desc=desc)
    e["provenance"].update(prov)
    p = {**e["provenance"], "chunk_id": chunk_id}
    return {"id": ENS.id_nodo_e2_r2(e, chunk_id), "type": "Obligacion", "label": "x",
            "properties": {"descripcion": desc}, "provenance": dict(p), "provenances": [dict(p)]}


# El nodo de C1 (X): declarado con el punto propio de 5.1.2 y con el tramo en el cierre de 5.1, sin y con C1.
X_SIN = nodo("5.1.2", "syn::5.1.2", "Sanciones por el incumplimiento del punto 3.1", "El incumplimiento dará lugar")
X_C1 = nodo("5.1", "syn::5.1.2", "Sanciones por el incumplimiento del punto 3.1", "El incumplimiento dará lugar",
            rol_documental="herencia_cierre", punto_declarado_e1="5.1.2", rol_declarado_e1="punto_propio",
            tramo_fuera_del_texto_de_e3=True)
OTROS = [nodo("5.1.2", "syn::5.1.2", "Lugar y fecha de emisión conforme al punto 3.1", "Lugar y fecha de emisión"),
         nodo("3.1", "syn::3.1", "Requisitos de emisión", "Requisitos de emisión"),
         nodo("3.3", "syn::3.3", "Sanciones aplicables", "Sanciones aplicables"),
         nodo("5.1.1", "syn::5.1.1", "Nombre del titular", "Nombre del titular")]
KG_SIN = {"nodes": [X_SIN] + OTROS, "edges": []}
KG_C1 = {"nodes": [X_C1] + OTROS, "edges": []}
A_SIN = {X_C1["id"]: X_SIN["id"]}  # la tabla id con C1 → id sin C1


@contextlib.contextmanager
def to_sintetico(*modulos):
    """El inventario de E0 del detector, con el TO armado a mano, mientras corre."""
    with contextlib.ExitStack() as st:
        st.enter_context(mock.patch.object(C, "TOS_ORDEN", ("syn",)))
        st.enter_context(mock.patch.object(C, "cargar_chunks_enm01", lambda to: deepcopy(DET_CHUNKS)))
        st.enter_context(mock.patch.object(C, "cargar_estructura_enm01", lambda to: {"secciones": []}))
        for m in modulos:
            st.enter_context(mock.patch.object(m, "TITULOS_TOS", {"syn": ("normas sinteticas",)}))
        yield


def detectar(modulo, kg, **op) -> tuple[dict, dict]:
    """El detector de la cadena r2b (procedencia propia y grupos sin el rol) sobre una copia del grafo."""
    kg = deepcopy(kg)
    with to_sintetico(modulo):
        r = modulo.detectar_y_resolver_r2(kg, procedencia_propia=True, agrupar_sin_rol=True, **op)
    return r, kg


def triplas(kg, tabla=None) -> set:
    t = tabla or {}
    return {(t.get(e["source"], e["source"]), e["relation"], t.get(e["target"], e["target"]),
             json.dumps(e.get("properties"), sort_keys=True, ensure_ascii=False)) for e in kg["edges"]}


def citas_del_chunk(r, chunk_id, tabla=None) -> list[str]:
    t = tabla or {}
    out = []
    for c in r["registro"]:
        if c.get("chunk_id") != chunk_id:
            continue
        c = {**c, "origenes": [t.get(o, o) for o in c["origenes"]],
             "destinos": [{**d, "nodos": [t.get(i, i) for i in d["nodos"]]} for d in c["destinos"]]}
        out.append(json.dumps(c, sort_keys=True, ensure_ascii=False))
    return sorted(out)


def s_detector_punto_e1() -> None:
    g = "9 detector con el punto de E1"
    r_sin, kg_sin = detectar(REF, KG_SIN)
    r_d, kg_d = detectar(REF, KG_C1, punto_declarado_e1=True)
    r_c1, kg_c1 = detectar(REF, KG_C1)
    del_grupo = {i for i in (X_SIN["id"], OTROS[0]["id"])}
    sale = {x for x in triplas(kg_sin) if x[0] in del_grupo}
    check(g, f"el grafo sin C1 tiene remisiones desde el grupo de la procedencia de C1 ({len(sale)})",
          len(sale) == 2 and any(x[0] == X_SIN["id"] for x in sale), sorted(sale))
    check(g, "las citas que lee y resuelve la procedencia de C1 son las de sin la bandera, salvo el id del origen",
          citas_del_chunk(r_d, "syn::5.1.2", A_SIN) == citas_del_chunk(r_sin, "syn::5.1.2")
          and len(citas_del_chunk(r_sin, "syn::5.1.2")) > 0)
    check(g, "las aristas que salen de su grupo son las de sin la bandera, salvo el id del origen",
          {x for x in triplas(kg_d, A_SIN) if x[0] in del_grupo} == sale)
    prov_x = [e["provenance"] for e in kg_d["edges"] if e["source"] == X_C1["id"]]
    check(g, "la arista lleva la procedencia del nodo de C1", prov_x and all(
        p.get("punto_declarado_e1") == "5.1.2" and p["punto"] == "5.1" for p in prov_x), prov_x)
    cambia = {x for x in triplas(kg_c1, A_SIN) if x[0] in del_grupo} != sale
    check(g, "leída con el punto de C1 (sin punto_declarado_e1), las remisiones de su grupo cambian", cambia)
    solo_sin, solo_d = triplas(kg_sin) - triplas(kg_d, A_SIN), triplas(kg_d, A_SIN) - triplas(kg_sin)
    check(g, "los destinos siguen el punto de C1: sale la cita al punto declarado y entra la cita al ancestro",
          {(x[0], x[2]) for x in solo_sin} == {(OTROS[3]["id"], X_SIN["id"])}
          and {(x[0], x[2]) for x in solo_d} == {(OTROS[2]["id"], X_SIN["id"])}, (sorted(solo_sin), sorted(solo_d)))
    check(g, "toda remite_a que cambia tiene un extremo en el nodo de C1",
          all(X_SIN["id"] in (x[0], x[2]) for x in solo_sin | solo_d))


def s_detector_apagado(head: Path | None) -> None:
    g = "10 detector con la bandera apagada"
    if head is None:
        check(g, "falta --referencias-head", False)
        return
    src = head.read_text(encoding="utf-8")
    H = types.ModuleType("r1_referencias_head")
    H.__file__ = str(REF_PATH)
    exec(compile(src, str(head), "exec"), H.__dict__)  # noqa: S102 — el código de HEAD, con las rutas del entregado
    check(g, f"el código de HEAD no tiene el parámetro (blob {blob(head)[:12]})",
          "punto_declarado_e1" not in src and "punto_declarado_e1" in REF_PATH.read_text(encoding="utf-8"))
    for nombre, kg in (("el grafo sin C1", KG_SIN), ("el grafo con C1", KG_C1)):
        r_h, kg_h = detectar(H, kg)
        r_e, kg_e = detectar(REF, kg)
        r_f, kg_f = detectar(REF, kg, punto_declarado_e1=False)
        a = json.dumps([r_h, kg_h], sort_keys=True, ensure_ascii=False)
        check(g, f"{nombre}: la salida y el grafo son los de HEAD ({len(kg_h['edges'])} remite_a)",
              a == json.dumps([r_e, kg_e], sort_keys=True, ensure_ascii=False)
              == json.dumps([r_f, kg_f], sort_keys=True, ensure_ascii=False) and kg_h["edges"])


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--ensamblar-head", type=Path, default=None)
    ap.add_argument("--referencias-head", type=Path, default=None)
    a = ap.parse_args()
    print(f"ensamblar_tanda0.py entregado: blob {blob(ENS_PATH)}; holgura {HOLGURA}")
    print(f"r1_referencias.py entregado: blob {blob(REF_PATH)}")
    if a.ensamblar_head is not None:
        print(f"ensamblar_tanda0.py de HEAD: blob {blob(a.ensamblar_head)}")
    if a.referencias_head is not None:
        print(f"r1_referencias.py de HEAD: blob {blob(a.referencias_head)}")
    s_c1_c2()
    s_ninguno()
    s_sin_tramo()
    s_mini()
    s_comunicacion()
    s_ancestro()
    s_bandera_apagada(a.ensamblar_head)
    s_union_evitada()
    s_detector_punto_e1()
    s_detector_apagado(a.referencias_head)
    for grupo, nombre, ok, det in RES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {grupo} | {nombre}" + ("" if ok else f" — {det}"))
    ok = sum(1 for x in RES if x[2])
    print(f"SELFTEST U-PROC-HERENCIA: {ok}/{len(RES)} {'PASS' if ok == len(RES) else 'FAIL'}")
    return 0 if ok == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
