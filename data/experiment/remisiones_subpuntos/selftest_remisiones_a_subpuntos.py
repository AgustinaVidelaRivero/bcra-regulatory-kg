"""U-REMISIONES-SUBPUNTOS — selftest de la opción B del detector de remisiones (`corpus_v2/r1_referencias.py`:
`detectar_y_resolver_r2` con `remisiones_a_subpuntos` y `unidades_excluidas`) y de su bandera en la cadena r2
(`tanda0/code/ensamblar_tanda0.py`: --remisiones-a-subpuntos), una rama por caso, sobre dos TOs armados a mano en el
selftest, sin datos del corpus:

  1. con la bandera apagada (sin el parámetro, con False y con la lista de unidades excluidas), el registro, el
     resumen y las aristas son los del `r1_referencias.py` de la segunda pasada de U-PROC-HERENCIA (--referencias-
     segunda-pasada, ejecutado con el `__file__` del entregado); la bandera llega a la cadena r2 apagada por defecto;
  2. un punto padre sin nodos con hijos con nodos: los destinos son los nodos de los hijos;
  3. una sección S<n>: los destinos son los de sus puntos de menor profundidad con nodos;
  4. dos ramas con su primer punto con nodos a distinta profundidad: B toma solo el nivel más alto del subárbol;
  5. sin subpuntos con nodos: la cita sigue con punto_sin_nodos;
  6. el origen dentro del subárbol citado (D-3): su unidad no es destino;
  7. un par que ya es remite_a por la resolución exacta: esa arista no cambia, ni su procedencia;
  8. la cita a una unidad excluida, en el grafo sin cola (la unidad, o una que empieza con ella más «::»): queda con
     su causa, y `irresolubles_en_unidad_excluida` del ensamblado le da la suya; con la cola, se resuelve;
  9. las propiedades de la arista nueva son exactamente alcance, destino y evidencia, el destino es la unidad citada
     y el alcance es interna o externa según el TO;
 10. los modelos r2 (`modelos_r2.py`: AristaR2 y la firma) validan las aristas nuevas.
El inventario de E0 del detector (`r1_comun.TOS_ORDEN`, `cargar_chunks_enm01`, `cargar_estructura_enm01`) y los
títulos de la regla (g) se reemplazan en memoria mientras corre.

Corre desde una COPIA del repo; no escribe nada. USD 0, sin API.
Uso: PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B \\
         data/experiment/remisiones_subpuntos/selftest_remisiones_a_subpuntos.py \\
         --referencias-segunda-pasada <r1_referencias.py de la segunda pasada de U-PROC-HERENCIA>
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import inspect
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
M = ENS.E4.modulo_modelos_r2()
RES: list[tuple[str, str, bool, str]] = []


def check(grupo: str, nombre: str, ok: bool, detalle: str = "") -> None:
    RES.append((grupo, nombre, bool(ok), str(detalle)[:300]))


def blob(p: Path) -> str:
    b = p.read_bytes()
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


# --- Dos TOs armados a mano -----------------------------------------------------------------------------------------
# «syn»: las unidades de origen (sección 1) y los subárboles citados (secciones 2 a 8); «otr»: el subárbol de una
# cita externa. Cada unidad tiene su chunk; la estructura declara todas las unidades.
def chunk(to, unidad, texto):
    return {"id": f"{to}::{unidad}", "to": to, "archivo": f"{to}.pdf", "unidad": unidad, "texto": texto,
            "herencia": [], "paginas": [1], "tipo": "punto_terminal", "titulo": ""}


TEXTOS = {
    "syn": {
        "1.1": "1.1. Plazos. Las entidades aplicarán lo previsto en el punto 2.1.",
        "1.2": "1.2. Alcance. Rige lo dispuesto en la Sección 3.",
        "1.3": "1.3. Montos. Se aplicará lo establecido en el punto 4.1.",
        "1.4": "1.4. Avisos. Se observará lo previsto en el punto 5.1.",
        "1.5": "1.5. Registros. Se cumplirá lo dispuesto en el punto 7.1 y en el punto 8.1.",
        "1.6": "1.6. Informes. Se presentarán según el punto 2.1.2.",
        "1.7": "1.7. Constancias. Se conservarán según el punto 2.1.",
        "1.8": "1.8. Remisión. Rige el punto 2.1 de las normas sobre “Normas otras”.",
        "2.1": "2.1. Requisitos.",
        "2.1.1": "2.1.1. Requisitos generales. Su aplicación se ajusta a lo previsto en el punto 2.1.",
        "2.1.2": "2.1.2. Requisitos particulares.",
        "3.1": "3.1. Primer apartado.", "3.2": "3.2. Segundo apartado.", "3.2.1": "3.2.1. Detalle del segundo.",
        "4.1": "4.1. Montos.", "4.1.1": "4.1.1. Montos generales.", "4.1.1.1": "4.1.1.1. Monto mínimo.",
        "4.1.2": "4.1.2. Montos particulares.",
        "5.1": "5.1. Avisos.", "5.1.1": "5.1.1. Avisos generales.",
        "7.1": "7.1. Registros.", "7.1.1": "7.1.1. Registro diario.",
        "8.1": "8.1. Archivos.", "8.1.1": "8.1.1. Archivo diario.",
    },
    "otr": {"2.1": "2.1. Requisitos.", "2.1.1": "2.1.1. Primer requisito.", "2.1.2": "2.1.2. Segundo requisito."},
}
CHUNKS = {to: [chunk(to, u, t) for u, t in ts.items()] for to, ts in TEXTOS.items()}


def estructura(to):
    """Las secciones del TO con sus puntos, para `unidades_e0` (S<n> y cada número)."""
    secs: dict[str, list[dict]] = {}
    for u in TEXTOS[to]:
        secs.setdefault(u.split(".")[0], []).append({"tipo": "punto", "numero": u, "hijos": []})
    return {"secciones": [{"tipo": "seccion", "numero": s, "hijos": h} for s, h in sorted(secs.items())]}


def prov(to, punto):
    return {"to": to, "archivo": f"{to}.pdf", "punto": punto, "rol_documental": "punto_propio",
            "chunk_id": f"{to}::{punto}", "paginas": [1], "ancestros": [punto.split(".")[0]],
            "tramo": TEXTOS[to][punto][:20], "tramo_verificado": "exacta"}


def nodo(nid, to, *puntos, desc="Obligación de la unidad"):
    ps = [prov(to, p) for p in puntos]
    return {"id": nid, "type": "Obligacion", "label": "x", "properties": {"descripcion": desc},
            "provenance": dict(ps[0]), "provenances": [dict(p) for p in ps]}


# Orígenes (sección 1) y destinos (secciones 2 a 8 de syn y sección 2 de otr). El texto guardado del origen de D-3
# nombra la unidad citada, para que la atribución D1 lo tome a él solo dentro de su punto.
O1, O2, O3, O4, O5 = (nodo(f"n:o{k}", "syn", f"1.{k}") for k in range(1, 6))
O6 = nodo("n:o6", "syn", "1.6", "1.7")
O8 = nodo("n:o8", "syn", "1.8")
OD = nodo("n:od", "syn", "2.1.1", desc="Ajuste a lo previsto en el punto 2.1")
A1, A2 = nodo("n:a1", "syn", "2.1.1"), nodo("n:a2", "syn", "2.1.2")
B1, B2, B3 = nodo("n:b1", "syn", "3.1"), nodo("n:b2", "syn", "3.2"), nodo("n:b3", "syn", "3.2.1")
C1, C2 = nodo("n:c1", "syn", "4.1.1.1"), nodo("n:c2", "syn", "4.1.2")
E1, E2 = nodo("n:e1", "syn", "7.1.1"), nodo("n:e2", "syn", "8.1.1")
X1, X2 = nodo("n:x1", "otr", "2.1.1"), nodo("n:x2", "otr", "2.1.2")
KG = {"nodes": [O1, O2, O3, O4, O5, O6, O8, OD, A1, A2, B1, B2, B3, C1, C2, E1, E2, X1, X2], "edges": []}
EXCLUIDAS = ["syn::7.1", "syn::8.1::1"]  # 7.1 es la unidad excluida; 8.1, por una de sus partes («::»)


@contextlib.contextmanager
def tos_sinteticos(*modulos):
    """El inventario de E0 del detector, con los dos TOs armados a mano, mientras corre."""
    titulos = {"syn": ("normas sinteticas",), "otr": ("normas otras",)}
    with contextlib.ExitStack() as st:
        st.enter_context(mock.patch.object(C, "TOS_ORDEN", ("syn", "otr")))
        st.enter_context(mock.patch.object(C, "cargar_chunks_enm01", lambda to: deepcopy(CHUNKS[to])))
        st.enter_context(mock.patch.object(C, "cargar_estructura_enm01", estructura))
        for m in modulos:
            st.enter_context(mock.patch.object(m, "TITULOS_TOS", titulos))
            st.enter_context(mock.patch.object(m, "INVENTARIO_TOS", titulos))
        yield


def detectar(modulo, kg=KG, **op) -> tuple[dict, dict]:
    """El detector de la cadena r2b (procedencia propia y grupos sin el rol) sobre una copia del grafo."""
    kg = deepcopy(kg)
    with tos_sinteticos(modulo):
        r = modulo.detectar_y_resolver_r2(kg, procedencia_propia=True, agrupar_sin_rol=True, **op)
    return r, kg


def cj(x) -> str:
    return json.dumps(x, sort_keys=True, ensure_ascii=False)


def aristas(kg) -> dict[tuple[str, str], dict]:
    return {(e["source"], e["target"]): e for e in kg["edges"]}


def citas(r, chunk_id) -> list[dict]:
    return [c for c in r["registro"] if c.get("chunk_id") == chunk_id]


def destino_b(r, chunk_id, destino) -> dict | None:
    return next((d for c in citas(r, chunk_id) for d in c["destinos"]
                 if d["destino"] == destino and d.get("remision_a_subpuntos") == "B"), None)


def causas(r, chunk_id, destino) -> list[str]:
    return [x["causa"] for c in citas(r, chunk_id) for x in c["irresolubles"] if x["destino"] == destino]


def ids(*ns) -> set[str]:
    return {n["id"] for n in ns}


# --- Las corridas ---------------------------------------------------------------------------------------------------
R_OFF, KG_OFF = detectar(REF)
R_ON, KG_ON = detectar(REF, remisiones_a_subpuntos=True)
R_ON_SC, KG_ON_SC = detectar(REF, remisiones_a_subpuntos=True, unidades_excluidas=EXCLUIDAS)
NUEVAS = {k: e for k, e in aristas(KG_ON).items() if k not in aristas(KG_OFF)}


def s_bandera_apagada(segunda: Path | None) -> None:
    g = "1 bandera apagada"
    if segunda is None:
        check(g, "falta --referencias-segunda-pasada", False)
        return
    src = segunda.read_text(encoding="utf-8")
    H = types.ModuleType("r1_referencias_segunda_pasada")
    H.__file__ = str(REF_PATH)
    exec(compile(src, str(segunda), "exec"), H.__dict__)  # noqa: S102 — la segunda pasada, con las rutas del entregado
    check(g, f"la segunda pasada no tiene el parámetro (blob {blob(segunda)[:12]})",
          "remisiones_a_subpuntos" not in src and "remisiones_a_subpuntos" in REF_PATH.read_text(encoding="utf-8"))
    r_h, kg_h = detectar(H)
    base = cj([r_h, kg_h])
    for nombre, op in (("sin el parámetro", {}), ("con False", {"remisiones_a_subpuntos": False}),
                       ("con False y la lista de excluidas", {"remisiones_a_subpuntos": False,
                                                              "unidades_excluidas": EXCLUIDAS})):
        r_e, kg_e = detectar(REF, **op)
        check(g, f"{nombre}: el registro, el resumen y las aristas son los de la segunda pasada "
                 f"({len(kg_h['edges'])} remite_a)",
              cj([r_e, kg_e]) == base and r_e["registro"] == r_h["registro"] and r_e["resumen"] == r_h["resumen"]
              and kg_e["edges"] == kg_h["edges"] and kg_h["edges"])
    check(g, "sin la bandera, el resumen no tiene la clave remisiones_a_subpuntos",
          "remisiones_a_subpuntos" not in R_OFF["resumen"] and "remisiones_a_subpuntos" in R_ON["resumen"])
    por_defecto = {f.__name__: inspect.signature(f).parameters["remisiones_a_subpuntos"].default
                   for f in (ENS.correr_cadena_r2, ENS.ensamblar_manifiesto_r2, REF.detectar_y_resolver_r2)}
    check(g, "la bandera de la cadena r2 está apagada por defecto", all(v is False for v in por_defecto.values()),
          por_defecto)
    check(g, "con la bandera, las aristas de la resolución exacta siguen todas, iguales",
          all(aristas(KG_ON).get(k) == e for k, e in aristas(KG_OFF).items()))


def s_padre() -> None:
    g = "2 punto padre con hijos con nodos"
    d = destino_b(R_ON, "syn::1.1", "syn::2.1")
    check(g, "la cita a 2.1 sin la bandera es punto_sin_nodos", causas(R_OFF, "syn::1.1", "syn::2.1") == ["punto_sin_nodos"])
    check(g, "con la bandera se resuelve: los destinos son los nodos de 2.1.1 y 2.1.2",
          d is not None and set(d["nodos"]) == ids(A1, A2, OD) and d["unidades"] == ["syn::2.1.1", "syn::2.1.2"]
          and not causas(R_ON, "syn::1.1", "syn::2.1"), d)
    check(g, "las aristas nuevas desde el origen van a esos nodos",
          {t for (s, t) in NUEVAS if s == O1["id"]} == ids(A1, A2, OD))


def s_seccion() -> None:
    g = "3 sección S<n>"
    d = destino_b(R_ON, "syn::1.2", "syn::S3")
    check(g, "la cita a la Sección 3 sin la bandera es punto_sin_nodos",
          causas(R_OFF, "syn::1.2", "syn::S3") == ["punto_sin_nodos"])
    check(g, "con la bandera, los destinos son los de 3.1 y 3.2 (no los de 3.2.1)",
          d is not None and set(d["nodos"]) == ids(B1, B2) and d["unidades"] == ["syn::3.1", "syn::3.2"], d)
    check(g, "las aristas nuevas desde el origen van a esos nodos",
          {t for (s, t) in NUEVAS if s == O2["id"]} == ids(B1, B2))


def s_nivel() -> None:
    g = "4 dos ramas a distinta profundidad"
    d = destino_b(R_ON, "syn::1.3", "syn::4.1")
    check(g, "B toma solo el nivel más alto con nodos de todo el subárbol (4.1.2, no 4.1.1.1)",
          d is not None and d["nodos"] == [C2["id"]] and d["unidades"] == ["syn::4.1.2"], d)
    check(g, "ninguna arista nueva va al nodo de 4.1.1.1", not any(t == C1["id"] for (_, t) in NUEVAS))


def s_sin_subpuntos() -> None:
    g = "5 sin subpuntos con nodos"
    check(g, "la cita a 5.1 sigue con punto_sin_nodos y sin destino",
          causas(R_ON, "syn::1.4", "syn::5.1") == ["punto_sin_nodos"] and destino_b(R_ON, "syn::1.4", "syn::5.1") is None)
    check(g, "no sale ninguna arista del origen", not any(s == O4["id"] for (s, _) in NUEVAS))


def s_d3() -> None:
    g = "6 el origen dentro del subárbol citado (D-3)"
    d = destino_b(R_ON, "syn::2.1.1", "syn::2.1")
    check(g, "la cita desde 2.1.1 a 2.1 toma solo 2.1.2: la unidad del origen no es destino",
          d is not None and d["unidades"] == ["syn::2.1.2"] and d["nodos"] == [A2["id"]], d)
    check(g, "las aristas nuevas desde el origen van solo al nodo de 2.1.2 (no a su vecino de 2.1.1)",
          {t for (s, t) in NUEVAS if s == OD["id"]} == ids(A2))


def s_par_existente() -> None:
    g = "7 par que ya es remite_a"
    k = (O6["id"], A2["id"])
    e_off, e_on = aristas(KG_OFF).get(k), aristas(KG_ON).get(k)
    check(g, "la resolución exacta crea la arista al nodo de 2.1.2, con la procedencia de 1.6",
          e_off is not None and [p["punto"] for p in e_off["provenances"]] == ["1.6"]
          and e_off["properties"]["destino"] == "syn::2.1.2")
    check(g, "con la bandera esa arista no cambia en nada (ni su destino ni su procedencia)", e_on == e_off)
    d = destino_b(R_ON, "syn::1.7", "syn::2.1")
    check(g, "la cita de 1.7 a 2.1 se resuelve con B y sus otras aristas son nuevas, con la procedencia de 1.7",
          d is not None and {t for (s, t) in NUEVAS if s == O6["id"]} == ids(A1, OD)
          and all([p["punto"] for p in NUEVAS[(O6["id"], t)]["provenances"]] == ["1.7"] for t in ids(A1, OD)), d)
    b = R_ON["resumen"]["remisiones_a_subpuntos"]
    check(g, "el resumen cuenta el par aparte (1) y las remite_a nuevas son las del grafo",
          b["pares_que_ya_existian"] == 1 and b["remite_a_nuevas"] == len(NUEVAS), b)


def s_excluida() -> None:
    g = "8 cita a una unidad excluida (sin cola)"
    for dest, nodo_b in (("syn::7.1", E1), ("syn::8.1", E2)):
        check(g, f"sin cola, la cita a {dest} queda con punto_sin_nodos y sin arista nueva",
              causas(R_ON_SC, "syn::1.5", dest) == ["punto_sin_nodos"] and destino_b(R_ON_SC, "syn::1.5", dest) is None
              and (O5["id"], nodo_b["id"]) not in aristas(KG_ON_SC))
        check(g, f"con la cola, la cita a {dest} se resuelve con B",
              (destino_b(R_ON, "syn::1.5", dest) or {}).get("nodos") == [nodo_b["id"]]
              and (O5["id"], nodo_b["id"]) in aristas(KG_ON))
    reg = deepcopy(R_ON_SC["registro"])
    ENS.irresolubles_en_unidad_excluida(reg, EXCLUIDAS)
    check(g, "irresolubles_en_unidad_excluida le da su causa propia a las dos",
          sorted(x["causa"] for c in reg if c.get("chunk_id") == "syn::1.5" for x in c["irresolubles"])
          == [ENS.CAUSA_UNIDAD_EXCLUIDA] * 2)
    b = R_ON_SC["resumen"]["remisiones_a_subpuntos"]
    check(g, "el resumen cuenta las dos citas a una unidad excluida", b["citas_a_unidad_excluida"] == 2
          and R_ON["resumen"]["remisiones_a_subpuntos"]["citas_a_unidad_excluida"] == 0, b)
    solo_sc = {k for k in aristas(KG_ON) if k not in aristas(KG_ON_SC)}
    check(g, "lo único que cambia sin cola son las dos aristas de esas citas",
          solo_sc == {(O5["id"], E1["id"]), (O5["id"], E2["id"])} and set(aristas(KG_ON_SC)) <= set(aristas(KG_ON)))


def s_forma() -> None:
    g = "9 forma de la arista nueva"
    check(g, f"hay aristas nuevas ({len(NUEVAS)})", len(NUEVAS) > 0)
    check(g, "las propiedades son exactamente alcance, destino y evidencia",
          all(set(e["properties"]) == {"alcance", "destino", "evidencia"} for e in NUEVAS.values())
          and set(M.PROPIEDADES_REMISION) == {"alcance", "destino", "evidencia"})
    check(g, "el destino es la unidad citada, no el subpunto",
          all(e["properties"]["destino"] in ("syn::2.1", "syn::S3", "syn::4.1", "syn::7.1", "syn::8.1", "otr::2.1")
              for e in NUEVAS.values()))
    a_otro_to = {k for k, e in NUEVAS.items() if e["properties"]["destino"].startswith("otr::")}
    check(g, "la cita a otro TO da alcance externa, y a sus nodos",
          a_otro_to == {(O8["id"], X1["id"]), (O8["id"], X2["id"])}
          and all(NUEVAS[k]["properties"]["alcance"] == "externa" for k in a_otro_to))
    check(g, "la cita al mismo TO da alcance interna",
          all(e["properties"]["alcance"] == "interna" for k, e in NUEVAS.items() if k not in a_otro_to))
    check(g, "la procedencia de la arista es la del origen en el punto de la cita",
          all(e["provenance"] == e["provenances"][0] and e["provenance"]["to"] == "syn"
              and e["provenance"]["chunk_id"] == f"syn::{e['provenance']['punto']}" for e in NUEVAS.values()))
    r2, kg2 = detectar(REF, remisiones_a_subpuntos=True)
    check(g, "dos corridas con la bandera dan lo mismo", cj([r2, kg2]) == cj([R_ON, KG_ON]))


def s_modelos() -> None:
    g = "10 modelos r2"
    from pydantic import ValidationError  # noqa: PLC0415
    tipo = {n["id"]: n["type"] for n in KG_ON["nodes"]}
    malas = []
    for k, e in sorted(NUEVAS.items()):
        try:
            M.AristaR2.model_validate(e)
        except ValidationError as x:
            malas.append((k, str(x).splitlines()[:2]))
            continue
        if not M.firma_arista(tipo[e["source"]], e["relation"], tipo[e["target"]]):
            malas.append((k, "firma"))
    check(g, f"AristaR2 y la firma validan las {len(NUEVAS)} aristas nuevas", not malas and NUEVAS, malas)
    mala = deepcopy(next(iter(NUEVAS.values())))
    mala["properties"]["unidades"] = ["syn::2.1.1"]
    try:
        M.AristaR2.model_validate(mala)
        rechaza = False
    except ValidationError:
        rechaza = True
    check(g, "control: con una propiedad de más, AristaR2 la rechaza", rechaza)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--referencias-segunda-pasada", type=Path, default=None)
    a = ap.parse_args()
    print(f"r1_referencias.py entregado: blob {blob(REF_PATH)}")
    print(f"ensamblar_tanda0.py entregado: blob {blob(ENS_PATH)}")
    if a.referencias_segunda_pasada is not None:
        print(f"r1_referencias.py de la segunda pasada: blob {blob(a.referencias_segunda_pasada)}")
    s_bandera_apagada(a.referencias_segunda_pasada)
    s_padre()
    s_seccion()
    s_nivel()
    s_sin_subpuntos()
    s_d3()
    s_par_existente()
    s_excluida()
    s_forma()
    s_modelos()
    for grupo, nombre, ok, det in RES:
        print(f"  [{'PASS' if ok else 'FAIL'}] {grupo} | {nombre}" + ("" if ok else f" — {det}"))
    ok = sum(1 for x in RES if x[2])
    print(f"SELFTEST U-REMISIONES-SUBPUNTOS: {ok}/{len(RES)} {'PASS' if ok == len(RES) else 'FAIL'}")
    return 0 if ok == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
