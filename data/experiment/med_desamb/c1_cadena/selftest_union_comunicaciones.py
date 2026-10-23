"""Selftest de la regla C1 en la cadena r2: la bandera --union-comunicaciones de `tanda0/code/ensamblar_tanda0.py`
(`cargar_union_comunicaciones`, `preparar_union_c1` y la guarda de `reextraccion_v2/corpus_v2/r1_invariantes.py` con
`codigo_comunicacion`) y el script de su lista (`armar_no_unir_c1.py`), sobre grafos armados a mano en el selftest, sin datos
del corpus. Cada caso pasa por el mismo camino que `correr_cadena_r2`: `preparar_union_c1` y después
`INV.merge_grafos_guardado` con los grafos y la función que devuelve. Una rama por caso:

  1. bandera apagada: la guarda entregada da, sin `codigo_comunicacion` y con None, exactamente lo que la de HEAD (la de la
     segunda pasada), en todos los grafos del selftest;
  2. bandera con la lista vacía: los cuatro controles de C1 de `parte3/selftest_reglas_candidatas_mesa.py` (el mismo código en
     tres documentos queda en un nodo y los marcadores, separados; la colisión no va a la adjudicación y queda en uniones_c1 con
     sus nodos; las diferencias de label y de código quedan como conflictos del merge; las aristas se re-apuntan al nodo unido y
     los invariantes dan OK), lo mismo que la guarda con la normalización sola, y el id con la guarda de cada nodo unido;
  3. con un código en la lista: sus nodos quedan como con la bandera apagada y los demás se unen;
  4. con la lista de nodos: (a) un código en tres documentos con uno de sus nodos en la lista: los otros dos se unen y el de la
     lista queda como con la bandera apagada, sea el primero o no, también cuando comparte su id con los que se unen (sin el
     renombre previo de la guarda, la unión lo absorbería: el control lo muestra); (b) un código en dos documentos con uno en la
     lista: no se une ninguno; (c) un código con tres nodos, uno en la lista y los otros dos en el mismo documento: no se une
     ninguno; (d) el sha256 de la lista de nodos que no coincide frena, y una sola de sus dos entradas da error; (e) sin la lista
     de nodos, la salida es la de la rama de la lista vacía, y con la lista de nodos vacía, también;
  5. los candados y la bandera: el sha256 de la lista de códigos que no coincide frena, la normalización con otro sha256 frena
     antes de cargarse, la normalización no se carga sin la bandera y la bandera fuera de la cadena r2 da error;
  6. el script de la lista: une_mal entra y une_bien no; una decisión vacía o distinta frena nombrando la fila, sin su texto;
  7. el árbol de sintaxis de r1_invariantes.py entregado es el del parchado (`parte3/codigo_preparado/`).

Corre desde una COPIA del repo; escribe solo en --trabajo (las listas y las hojas de prueba). USD 0, sin API.
Uso: PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/med_desamb/c1_cadena/selftest_union_comunicaciones.py
     --invariantes-head <r1_invariantes.py de HEAD> --trabajo <directorio vacío>
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import subprocess
import sys
import types
from copy import deepcopy
from pathlib import Path
from unittest import mock

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
ENS_PATH = REPO / "data" / "experiment" / "tanda0" / "code" / "ensamblar_tanda0.py"
PARCHADO = REPO / "data" / "experiment" / "med_desamb" / "parte3" / "codigo_preparado" / "r1_invariantes_con_reglas_candidatas.py"
PARCHADO_SHA256 = "a56a3ec3bb002488dbbf46e2544c34eadbd4c9fd34b3f8003e3cc47d0acbf08a"
HEAD_SHA256 = "771231420d7fd3eaa6056ae1c910a1f94cf7055eb5042320a1b0aba6734f29e0"
ARMAR = AQUI / "armar_no_unir_c1.py"
MANIFIESTO_NO_R2 = REPO / "data" / "experiment" / "reextraccion_v2" / "manifiestos" / "tanda0_ens_desarrollo.json"
sys.path.insert(0, str(ENS_PATH.parent))
import ensamblar_tanda0 as ENS  # noqa: E402

NORMALIZACION_CARGADA_AL_IMPORTAR = ENS.MODULO_NORMALIZACION_C1 in sys.modules
INV, C = ENS.INV, ENS.C
TOS = list(C.TOS_ORDEN)
RES: list[tuple[str, str, bool, str]] = []
TRABAJO: Path = Path()
_N = [0]


def check(grupo: str, nombre: str, ok: bool, detalle: str = "") -> None:
    RES.append((grupo, nombre, bool(ok), detalle))


# ------------------------------------------------------------------------- #
# Grafos armados a mano                                                      #
# ------------------------------------------------------------------------- #
def com(i: str, cod: str, label: str, tipo: str = "A") -> dict:
    return {"id": i, "type": "Comunicacion", "label": label, "properties": {"codigo": cod, "tipo": tipo}}


def grafos_de(por_to: dict[int, list[dict]]) -> dict[str, dict]:
    """Un grafo por TO de C.TOS_ORDEN: su TextoOrdenado y una arista referencia a cada Comunicacion (I5 pide `provenance` y
    `provenances` no vacío)."""
    out = {}
    for k, to in enumerate(TOS):
        pv = {"to": to, "punto": "1", "chunk_id": f"{to}/1"}
        t = {"id": f"TextoOrdenado_{to}", "type": "TextoOrdenado", "label": to, "properties": {}, "provenance": pv,
             "provenances": [pv]}
        cs = [dict(deepcopy(c), provenance=pv, provenances=[pv]) for c in por_to.get(k, [])]
        out[to] = {"nodes": [t] + cs, "edges": [{"source": t["id"], "relation": "referencia", "target": c["id"],
                                                 "provenance": pv, "provenances": [pv]} for c in cs]}
    return out


# el caso de parte3/selftest_reglas_candidatas_mesa.py
REGLAS = {0: [com("Comunicacion_a_6847", "A-6847", "Com. A 6847")],
          1: [com("Comunicacion_comunicacion_a_6847", "Comunicación A 6847", "Comunicación A 6847")],
          2: [com("Comunicacion_a_6847", "A-6847", "A 6847")],
          3: [com("Comunicacion_a_sin_especificar", "A-<sin especificar>", "Com. A —")],
          4: [com("Comunicacion_a_sin_especificar", "A-<sin especificar>", "Com. A —")]}
G_REGLAS = grafos_de(REGLAS)
# un segundo código, en dos documentos, para la lista de códigos
DOS_CODIGOS = deepcopy(REGLAS)
DOS_CODIGOS[1].append(com("Comunicacion_b_1234", "B-1234", "Com. B 1234", "B"))
DOS_CODIGOS[3].append(com("Comunicacion_com_b_1234", "Com. B 1234", "Comunicación B 1234", "B"))
G_DOS_CODIGOS = grafos_de(DOS_CODIGOS)
# (a) un código en tres documentos; los dos primeros comparten el id
G_TRES = grafos_de({0: [com("Comunicacion_c_7711", "C-7711", "Com. C 7711", "C")],
                    1: [com("Comunicacion_c_7711", "C-7711", "C 7711", "C")],
                    2: [com("Comunicacion_com_c_7711", "Com. C 7711", "Comunicación C 7711", "C")]})
# (a') un código en tres documentos con ids distintos
G_TRES_IDS = grafos_de({0: [com("Comunicacion_p_5005", "P-5005", "Com. P 5005", "P")],
                        2: [com("Comunicacion_com_p_5005", "Com. P 5005", "P 5005", "P")],
                        4: [com("Comunicacion_comunicacion_p_5005", "Comunicación P 5005", "Comunicación P 5005", "P")]})
# (b) un código en dos documentos con el mismo id
G_DOS = grafos_de({0: [com("Comunicacion_b_8080", "B-8080", "Com. B 8080", "B")],
                   3: [com("Comunicacion_b_8080", "B-8080", "B 8080", "B")]})
# (c) tres nodos de un código: dos en el mismo documento
G_MISMO_DOC = grafos_de({0: [com("Comunicacion_c_9090", "C-9090", "Com. C 9090", "C"),
                             com("Comunicacion_com_c_9090", "Com. C 9090", "C 9090", "C")],
                         2: [com("Comunicacion_c_9090", "C-9090", "Comunicación C 9090", "C")]})
TODOS = {"reglas": G_REGLAS, "dos_codigos": G_DOS_CODIGOS, "tres": G_TRES, "tres_ids": G_TRES_IDS, "dos": G_DOS,
         "mismo_doc": G_MISMO_DOC}


# ------------------------------------------------------------------------- #
# Utilidades                                                                 #
# ------------------------------------------------------------------------- #
def archivo(nombre: str, obj) -> tuple[Path, str]:
    _N[0] += 1
    p = TRABAJO / f"{_N[0]:02d}_{nombre}"
    p.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return p, hashlib.sha256(p.read_bytes()).hexdigest()


def union(no_unir=(), nodos=None) -> dict:
    p, s = archivo("no_unir.json", {"no_unir": list(no_unir)})
    if nodos is None:
        return ENS.cargar_union_comunicaciones(p, s)
    pn, sn = archivo("nodos.json", sorted(nodos))
    return ENS.cargar_union_comunicaciones(p, s, pn, sn)


def apagada(g: dict, mod=None, **kw) -> dict:
    return (mod or INV).merge_grafos_guardado(deepcopy(g), **kw)


def con_c1(g: dict, u: dict) -> tuple[dict, dict]:
    """El camino de correr_cadena_r2 con la bandera."""
    prep = ENS.preparar_union_c1(deepcopy(g), u)
    return INV.merge_grafos_guardado(prep["grafos"], codigo_comunicacion=prep["codigo_comunicacion"]), prep


def j(x) -> str:
    return json.dumps(x, ensure_ascii=False, sort_keys=True, default=str)


def kg(m: dict) -> dict:
    return {"nodes": m["nodes"], "edges": m["edges"]}


def nodos(m: dict) -> dict[str, dict]:
    return {n["id"]: n for n in m["nodes"]}


def coms(m: dict) -> list[str]:
    return sorted(n["id"] for n in m["nodes"] if n["type"] == "Comunicacion")


def invariantes_ok(m: dict) -> bool:
    k = kg(m)
    return INV.verificar_invariantes(k, m["grafos_pre_merge"], merges_nodo=len(m["merges_cross_to"]),
                                     merges_arista=INV.merges_arista_de(m["grafos_pre_merge"], k["edges"]))["ok"]


def de_codigo(m: dict, norm, c: str) -> dict[str, dict]:
    return {n["id"]: n for n in m["nodes"] if n["type"] == "Comunicacion" and norm(n) == c}


def aristas_fuera(m: dict, ids: set[str]) -> str:
    return j(sorted((e for e in m["edges"] if e["source"] not in ids and e["target"] not in ids),
                    key=lambda e: (e["source"], e["relation"], e["target"])))


def ids_u(m: dict, prep: dict) -> set[str]:
    """U: los ids del registro de las uniones (el canónico, los de antes y el de cada nodo con la guarda)."""
    return {u["id"] for u in m["uniones_c1"]} | {x["id_antes"] for u in m["uniones_c1"] for x in u["nodos"]} | {
        prep["guarda_de"][(x["to"], x["id_antes"])] for u in m["uniones_c1"] for x in u["nodos"]}


def correr_ens(*args: str) -> subprocess.CompletedProcess:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ANTHROPIC_API_KEY", None)
    return subprocess.run([sys.executable, "-B", str(ENS_PATH), *args], capture_output=True, text=True, env=env, cwd=REPO)


# ------------------------------------------------------------------------- #
# Ramas                                                                      #
# ------------------------------------------------------------------------- #
def rama_5_antes_de_cargar() -> None:
    """La normalización no se carga sin la bandera, y con otro sha256 frena antes de cargarse (va primero: después de la
    primera carga buena la normalización queda en sys.modules)."""
    check("5 candados", "importar ensamblar_tanda0 no carga la normalización", not NORMALIZACION_CARGADA_AL_IMPORTAR)
    alterada = TRABAJO / "normalizacion_alterada.py"
    alterada.write_bytes(ENS.NORMALIZACION_C1.read_bytes() + b"\n")
    p, s = archivo("no_unir.json", {"no_unir": []})
    with mock.patch.object(ENS, "NORMALIZACION_C1", alterada):
        try:
            ENS.cargar_union_comunicaciones(p, s)
            frena, msg = False, ""
        except RuntimeError as e:
            frena, msg = True, str(e)
    check("5 candados", "la normalización con otro sha256 frena y lo dice", frena and "candado de la normalización" in msg
          and hashlib.sha256(alterada.read_bytes()).hexdigest() in msg and ENS.NORMALIZACION_C1_SHA256 in msg)
    check("5 candados", "y no se carga", ENS.MODULO_NORMALIZACION_C1 not in sys.modules)


def rama_1(head) -> None:
    for nombre, g in TODOS.items():
        h = apagada(g, head)
        check("1 apagada", f"{nombre}: la guarda sin codigo_comunicacion da lo de HEAD", j(apagada(g)) == j(h))
        check("1 apagada", f"{nombre}: con codigo_comunicacion=None, también", j(apagada(g, codigo_comunicacion=None)) == j(h))
        check("1 apagada", f"{nombre}: sin la clave uniones_c1", "uniones_c1" not in apagada(g))


def rama_2(u0: dict) -> tuple[dict, dict]:
    m, prep = con_c1(G_REGLAS, u0)
    ids = coms(m)
    check("2 lista vacía", "el mismo código en tres documentos queda en un nodo; los marcadores, separados",
          ids == ["Comunicacion_a_6847", "Comunicacion_a_sin_especificar", f"Comunicacion_a_sin_especificar__{TOS[4]}"],
          str(ids))
    check("2 lista vacía", "la colisión no va a la adjudicación y queda en uniones_c1 con sus 3 nodos",
          [a["id"] for a in m["adjudicacion_cross_to"]] == ["Comunicacion_a_sin_especificar"] and len(m["uniones_c1"]) == 1
          and len(m["uniones_c1"][0]["nodos"]) == 3)
    check("2 lista vacía", "las diferencias de label y de código quedan como conflictos del merge",
          any(c["property"] == "label" for c in m["conflictos"]) and any(c["property"] == "codigo" for c in m["conflictos"]))
    refs = [e for e in m["edges"] if e["relation"] == "referencia" and e["target"] == "Comunicacion_a_6847"]
    check("2 lista vacía", "las 3 aristas referencia apuntan al nodo unido y los invariantes dan OK",
          len(refs) == 3 and invariantes_ok(m), str(len(refs)))
    directo = apagada(G_REGLAS, codigo_comunicacion=u0["codigo_normalizado"])
    check("2 lista vacía", "lo mismo que la guarda con la normalización sola (el código preparado)", j(m) == j(directo))
    guarda = sorted(prep["guarda_de"][(x["to"], x["id_antes"])] for x in m["uniones_c1"][0]["nodos"])
    check("2 lista vacía", "el id con la guarda de cada nodo unido es el de la salida con la bandera apagada",
          guarda == sorted(["Comunicacion_a_6847", "Comunicacion_comunicacion_a_6847", f"Comunicacion_a_6847__{TOS[2]}"])
          and set(guarda) <= set(nodos(apagada(G_REGLAS))), str(guarda))
    off = apagada(G_REGLAS)
    U = ids_u(m, prep)
    cambian = {i for i in set(nodos(off)) | set(nodos(m)) if j(nodos(off).get(i)) != j(nodos(m).get(i))}
    check("2 lista vacía", "lo que cambia contra la bandera apagada son solo Comunicacion de U, y sus aristas",
          cambian <= U and all((nodos(off).get(i) or nodos(m).get(i))["type"] == "Comunicacion" for i in cambian)
          and aristas_fuera(off, U) == aristas_fuera(m, U), f"{len(cambian)} nodos")
    c = prep["cuentas"]
    check("2 lista vacía", "las cuentas: ningún código ni nodo fuera por las listas",
          c["codigos_en_la_lista"] == 0 and c["codigos_que_no_se_unen_por_la_lista"] == 0
          and c["codigos_que_no_se_unen_por_la_lista_de_nodos"] == 0 and c["nodos_sha256"] is None, j(c))
    return m, prep


def rama_3(u0: dict) -> None:
    norm = u0["codigo_normalizado"]
    u = union(["A 6847"])
    m, prep = con_c1(G_DOS_CODIGOS, u)
    off = apagada(G_DOS_CODIGOS)
    check("3 lista de códigos", "los nodos del código de la lista quedan como con la bandera apagada",
          j(de_codigo(m, norm, "A 6847")) == j(de_codigo(off, norm, "A 6847")) and len(de_codigo(off, norm, "A 6847")) == 3)
    check("3 lista de códigos", "el otro código se une",
          len(de_codigo(m, norm, "B 1234")) == 1 and len(de_codigo(off, norm, "B 1234")) == 2
          and [x["codigo_normalizado"] for x in m["uniones_c1"]] == ["B 1234"])
    check("3 lista de códigos", "la adjudicación del código de la lista es la de siempre",
          [a["id"] for a in m["adjudicacion_cross_to"]] == [a["id"] for a in off["adjudicacion_cross_to"]])
    check("3 lista de códigos", "los invariantes dan OK", invariantes_ok(m))
    check("3 lista de códigos", "las cuentas: 1 código no se une por la lista, 1 se une",
          prep["cuentas"]["codigos_que_no_se_unen_por_la_lista"] == 1 and len(m["uniones_c1"]) == 1, j(prep["cuentas"]))


def rama_4(u0: dict, m_vacia: dict) -> None:
    norm = u0["codigo_normalizado"]
    # (a) el de la lista no es el primero y comparte el id con el primero
    off = apagada(G_TRES)
    listado = f"Comunicacion_c_7711__{TOS[1]}"
    m, prep = con_c1(G_TRES, union((), [listado]))
    check("4a nodos", "tres documentos, el segundo en la lista (comparte el id): queda como con la bandera apagada",
          j(nodos(m).get(listado)) == j(nodos(off)[listado]))
    check("4a nodos", "los otros dos se unen", len(m["uniones_c1"]) == 1 and len(m["uniones_c1"][0]["nodos"]) == 2
          and len(de_codigo(m, norm, "C 7711")) == 2 and "Comunicacion_com_c_7711" not in nodos(m))
    U = ids_u(m, prep)
    check("4a nodos", "todo lo demás, igual: nodos y aristas fuera de U",
          j({i: n for i, n in nodos(m).items() if i not in U}) == j({i: n for i, n in nodos(off).items() if i not in U})
          and aristas_fuera(m, U) == aristas_fuera(off, U) and listado not in U and invariantes_ok(m))
    check("4a nodos", "las cuentas: el nodo de la lista está en el grafo y su id recibió el renombre previo",
          prep["cuentas"]["nodos_de_la_lista_en_el_grafo"] == 1 and prep["cuentas"]["ids_con_el_renombre_de_la_guarda_antes_de_unir"]
          == 1 and prep["cuentas"]["codigos_que_no_se_unen_por_la_lista_de_nodos"] == 0, j(prep["cuentas"]))
    # control: sin el renombre previo (solo None para el de la lista, que se reconoce por identidad), la unión lo absorbe
    g = deepcopy(G_TRES)
    marcado = next(n for n in g[TOS[1]]["nodes"] if n["type"] == "Comunicacion")
    ingenua = INV.merge_grafos_guardado(g, codigo_comunicacion=lambda n: None if n is marcado else norm(n))
    check("4a nodos", "control: sin el renombre previo de la guarda, la unión absorbería el nodo de la lista",
          listado not in nodos(ingenua) and len(de_codigo(ingenua, norm, "C 7711")) == 1)
    # (a) el de la lista es el primero y comparte el id con el segundo
    primero = "Comunicacion_c_7711"
    m, prep = con_c1(G_TRES, union((), [primero]))
    check("4a nodos", "tres documentos, el primero en la lista: queda como con la bandera apagada",
          j(nodos(m).get(primero)) == j(nodos(off)[primero]))
    check("4a nodos", "los otros dos se unen, con el id de la guarda del primero que queda",
          len(m["uniones_c1"]) == 1 and m["uniones_c1"][0]["id"] == f"Comunicacion_c_7711__{TOS[1]}"
          and len(de_codigo(m, norm, "C 7711")) == 2 and invariantes_ok(m))
    # (a') ids distintos, el del medio en la lista
    off_ids = apagada(G_TRES_IDS)
    m, prep = con_c1(G_TRES_IDS, union((), ["Comunicacion_com_p_5005"]))
    check("4a nodos", "ids distintos, el del medio en la lista: queda aparte y los otros dos se unen",
          j(nodos(m).get("Comunicacion_com_p_5005")) == j(nodos(off_ids)["Comunicacion_com_p_5005"])
          and len(m["uniones_c1"]) == 1 and len(de_codigo(m, norm, "P 5005")) == 2
          and prep["cuentas"]["ids_con_el_renombre_de_la_guarda_antes_de_unir"] == 0)
    # (b) dos documentos, uno en la lista
    off_dos = apagada(G_DOS)
    m, prep = con_c1(G_DOS, union((), [f"Comunicacion_b_8080__{TOS[3]}"]))
    check("4b nodos", "dos documentos, uno en la lista: no se une ninguno (la salida de la bandera apagada)",
          j(kg(m)) == j(kg(off_dos)) and m["uniones_c1"] == []
          and j(m["adjudicacion_cross_to"]) == j(off_dos["adjudicacion_cross_to"]))
    check("4b nodos", "las cuentas: 1 código no se une por la lista de nodos",
          prep["cuentas"]["codigos_que_no_se_unen_por_la_lista_de_nodos"] == 1, j(prep["cuentas"]))
    # (c) tres nodos, uno en la lista, los otros dos en el mismo documento
    off_md = apagada(G_MISMO_DOC)
    sin_lista, _ = con_c1(G_MISMO_DOC, u0)
    m, prep = con_c1(G_MISMO_DOC, union((), [f"Comunicacion_c_9090__{TOS[2]}"]))
    check("4c nodos", "control: sin la lista, ese código se une (tres nodos en dos documentos)",
          len(de_codigo(sin_lista, norm, "C 9090")) == 1)
    check("4c nodos", "tres nodos, uno en la lista y dos en el mismo documento: no se une ninguno",
          j(kg(m)) == j(kg(off_md)) and m["uniones_c1"] == []
          and prep["cuentas"]["codigos_que_no_se_unen_por_la_lista_de_nodos"] == 1)
    # (d) el sha256 de la lista de nodos y sus dos entradas
    p, s = archivo("no_unir.json", {"no_unir": []})
    pn, sn = archivo("nodos.json", [listado])
    try:
        ENS.cargar_union_comunicaciones(p, s, pn, "0" * 64)
        frena, msg = False, ""
    except RuntimeError as e:
        frena, msg = True, str(e)
    check("4d nodos", "el sha256 de la lista de nodos que no coincide frena", frena
          and "candado de --union-comunicaciones-nodos" in msg and sn in msg)
    base = ["--manifiesto", str(MANIFIESTO_NO_R2), "--entrada", str(TRABAJO / "no_existe"), "--salida",
            str(TRABAJO / "salida_que_no_se_escribe"), "--union-comunicaciones", str(p), "--union-comunicaciones-sha256", s]
    r1 = correr_ens(*base, "--union-comunicaciones-nodos", str(pn))
    r2 = correr_ens(*base, "--union-comunicaciones-nodos-sha256", sn)
    r3 = correr_ens(*base[:6], "--union-comunicaciones-nodos", str(pn), "--union-comunicaciones-nodos-sha256", sn)
    check("4d nodos", "solo la lista de nodos, sin su sha256: error", r1.returncode == 2 and "van juntas" in r1.stderr)
    check("4d nodos", "solo el sha256, sin la lista de nodos: error", r2.returncode == 2 and "van juntas" in r2.stderr)
    check("4d nodos", "la lista de nodos sin --union-comunicaciones: error",
          r3.returncode == 2 and "va con --union-comunicaciones" in r3.stderr)
    check("4d nodos", "ninguno escribe la salida", not (TRABAJO / "salida_que_no_se_escribe").exists())
    # (e) sin la lista de nodos, y con la lista de nodos vacía
    m_sin, _ = con_c1(G_REGLAS, union(()))
    m_vac, prep_vac = con_c1(G_REGLAS, union((), []))
    check("4e nodos", "sin la lista de nodos, la salida es la de la rama de la lista vacía", j(m_sin) == j(m_vacia))
    check("4e nodos", "con la lista de nodos vacía, también", j(m_vac) == j(m_vacia)
          and prep_vac["cuentas"]["nodos_de_la_lista"] == 0)


def rama_5_despues() -> None:
    p, s = archivo("no_unir.json", {"no_unir": []})
    try:
        ENS.cargar_union_comunicaciones(p, "f" * 64)
        frena, msg = False, ""
    except RuntimeError as e:
        frena, msg = True, str(e)
    check("5 candados", "el sha256 de la lista de códigos que no coincide frena", frena
          and "candado de --union-comunicaciones" in msg and s in msg)
    pm, sm = archivo("no_unir_mal.json", ["A 1"])
    try:
        ENS.cargar_union_comunicaciones(pm, sm)
        frena = False
    except RuntimeError:
        frena = True
    check("5 candados", "una lista de códigos sin la forma {\"no_unir\": [...]} frena", frena)
    r = correr_ens("--manifiesto", str(MANIFIESTO_NO_R2), "--entrada", str(TRABAJO / "no_existe"), "--salida",
                   str(TRABAJO / "salida_no_r2"), "--union-comunicaciones", str(p), "--union-comunicaciones-sha256", s)
    check("5 candados", "la bandera fuera de la cadena r2 da error y no escribe nada",
          r.returncode == 2 and "solo de la cadena r2" in r.stderr and not (TRABAJO / "salida_no_r2").exists())
    check("5 candados", "con la bandera, la normalización queda cargada de su archivo",
          ENS.MODULO_NORMALIZACION_C1 in sys.modules
          and Path(sys.modules[ENS.MODULO_NORMALIZACION_C1].__file__).resolve() == ENS.NORMALIZACION_C1.resolve())


def rama_6() -> None:
    def hoja(nombre: str, filas: list[list[str]]) -> tuple[Path, str]:
        p = TRABAJO / nombre
        p.write_text("\n".join(",".join(f) for f in [["colision", "codigo_normalizado", "nodos", "decision", "nota"]] + filas)
                     + "\n", encoding="utf-8")
        return p, hashlib.sha256(p.read_bytes()).hexdigest()

    def armar(p: Path, s: str, salida: Path) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, "-I", "-B", str(ARMAR), "--hoja", str(p), "--hoja-sha256", s, "--salida",
                               str(salida)], capture_output=True, text=True)
    p, s = hoja("hoja_buena.csv", [["c1", "A 6847", "3", "une_mal", "nota uno"], ["c2", "B 1234", "2", "une_bien", ""],
                                   ["c3", "C 7711", "2", " une_mal ", "nota tres"]])
    out = TRABAJO / "no_unir_de_la_hoja.json"
    r = armar(p, s, out)
    lista = json.loads(out.read_text(encoding="utf-8")) if out.exists() else None
    check("6 script", "une_mal entra y une_bien no", r.returncode == 0 and lista == {"no_unir": ["A 6847", "C 7711"]},
          r.stdout.strip())
    sha_out = hashlib.sha256(out.read_bytes()).hexdigest() if out.exists() else ""
    check("6 script", "da el sha256 de la lista, y la lista entra en la bandera con él",
          sha_out in r.stdout and ENS.cargar_union_comunicaciones(out, sha_out)["no_unir"] == frozenset({"A 6847", "C 7711"}))
    p, s = hoja("hoja_sin_mal.csv", [["c1", "A 6847", "3", "une_bien", ""]])
    out = TRABAJO / "no_unir_sin_une_mal.json"
    r = armar(p, s, out)
    check("6 script", "sin filas une_mal, la lista va vacía",
          r.returncode == 0 and json.loads(out.read_text(encoding="utf-8")) == {"no_unir": []})
    secreto = "TEXTO_QUE_NO_SE_MUESTRA"
    casos = (("vacía", "", "vacía"), ("distinta", "une_" + secreto, "no es une_bien ni une_mal"))
    for k, (nombre, dec, motivo) in enumerate(casos):
        p, s = hoja(f"hoja_decision_{k}.csv", [["c1", "A 6847", "3", "une_bien", ""],
                                               [secreto, secreto, "2", dec, secreto]])
        out = TRABAJO / f"no_unir_decision_{k}.json"
        r = armar(p, s, out)
        check("6 script", f"una decisión {nombre} frena nombrando la fila, sin su texto",
              r.returncode == 1 and "línea 3" in r.stderr and motivo in r.stderr and secreto not in r.stderr + r.stdout
              and not out.exists(), r.stderr.strip())
    p, s = hoja("hoja_sha.csv", [["c1", "A 6847", "3", "une_mal", ""]])
    r = armar(p, "0" * 64, TRABAJO / "no_unir_sha.json")
    check("6 script", "la hoja con otro sha256 frena", r.returncode == 1 and not (TRABAJO / "no_unir_sha.json").exists())


def rama_7() -> None:
    fuente = Path(INV.__file__).read_text(encoding="utf-8")
    parchado = PARCHADO.read_text(encoding="utf-8")
    check("7 árbol", "el parchado es el del sello", hashlib.sha256(PARCHADO.read_bytes()).hexdigest() == PARCHADO_SHA256)
    check("7 árbol", "r1_invariantes.py entregado y el parchado tienen el mismo árbol de sintaxis",
          ast.dump(ast.parse(fuente)) == ast.dump(ast.parse(parchado)))
    distintas = [(a, b) for a, b in zip(fuente.splitlines(), parchado.splitlines()) if a != b]
    check("7 árbol", "solo cambian líneas de comentario",
          len(fuente.splitlines()) == len(parchado.splitlines()) and distintas
          and all(a.strip().startswith("#") and b.strip().startswith("#") for a, b in distintas), f"{len(distintas)} líneas")


def main() -> int:
    global TRABAJO
    ap = argparse.ArgumentParser()
    ap.add_argument("--invariantes-head", type=Path, required=True, help="el r1_invariantes.py de HEAD (git show)")
    ap.add_argument("--trabajo", type=Path, required=True, help="directorio vacío para las listas y las hojas de prueba")
    a = ap.parse_args()
    TRABAJO = a.trabajo.resolve()
    TRABAJO.mkdir(parents=True, exist_ok=True)
    if any(TRABAJO.iterdir()):
        raise SystemExit(f"--trabajo no está vacío: {TRABAJO}")
    datos_head = a.invariantes_head.read_bytes()
    head = types.ModuleType("r1_invariantes_head")
    head.__file__ = INV.__file__
    exec(compile(datos_head, str(a.invariantes_head), "exec"), head.__dict__)
    print(f"r1_invariantes.py de HEAD: sha256 {hashlib.sha256(datos_head).hexdigest()}; TOs del selftest: {len(TOS)}")
    check("1 apagada", "el r1_invariantes.py de HEAD es el del sello", hashlib.sha256(datos_head).hexdigest() == HEAD_SHA256)
    rama_5_antes_de_cargar()
    rama_1(head)
    u0 = union(())
    m_vacia, _ = rama_2(u0)
    rama_3(u0)
    rama_4(u0, m_vacia)
    rama_5_despues()
    rama_6()
    rama_7()
    for g, n, ok, d in RES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {g} | {n}" + (f" | {d}" if d and not ok else ""))
    n_ok = sum(1 for r in RES if r[2])
    print(f"SELFTEST C1 EN LA CADENA R2: {n_ok}/{len(RES)} PASS")
    return 0 if n_ok == len(RES) else 1


if __name__ == "__main__":
    sys.exit(main())
