#!/usr/bin/env python3
"""sonda_ranks_buscar_nodos_UB21.py — U-B2.1 fase 1 (re-diagnóstico), pieza e
(tercera sonda: la forma de test «rank en buscar_nodos» de la decisión 3).

Retriever: el IN-MEMORY real, GraphIndex de data/experiment/evaluacion/harness.py
(cuarteto hasheado; se importa, no se edita ni se copia), sobre un
KnowledgeGraph cargado con loader.load_graph_from_path(path, adapter_key=None)
(adaptador nulo). Config que fija el rank: tokens sobre label + id
(harness._tokens: minúsculas, sin acentos, [a-z0-9]+), score =
|tokens(consulta) ∩ tokens(nodo)|, orden (-score, len(label), id)
(harness.py:148-162); limite pedido 50 (tope del harness) para ver ranks > 10;
«en top-10» = rank <= 10, que es el corte que usaron los retests.
El loader normaliza provenance a {source_doc, location} (loader.py:132-140):
en gen 3 las provenances quedan vacías en su vista, lo que NO afecta
buscar_nodos ni ver_vecinos (solo label/id y adyacencia).

Solo se sondean las consultas que ESTÁN EN EL REPO con rank sellado:
C1 retest (3), C2 retest (2), C5 propuesta (7) + proxy RT-C5-4 del retest C5
(1), C6 propuesta (11), C7 retest (3), y la posición en ver_vecinos del
retest C4 (e). Los objetivos se direccionan sin id (archivo, punto,
tipo, cadena) salvo los ids de catálogo (rol y PNFC de C6, padre e hijo de C4).

Solo lectura; imprime por stdout. Corre desde la raíz del repo:
    PYTHONDONTWRITEBYTECODE=1 .venv/bin/python3 reports/revision_UB21_diag/sonda_ranks_buscar_nodos_UB21.py
"""
import sys
sys.dont_write_bytecode = True

import hashlib
import json
import re
import unicodedata
from collections import OrderedDict
from pathlib import Path

RAIZ = Path.cwd()
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "evaluacion"))
import harness as H   # noqa: E402  (importado, no editado)
import loader as L    # noqa: E402

GRAFOS = [
    ("KG-Base", "data/experiment/run_3_ppf_core/kg.json",
     "12c226e22b8fdc8f46999cae7f1eb808930e71f5dfe803f3a4f637a88348c410"),
    ("KG-Refinado", "data/experiment/grafo_v2/reensamblado_v3/kg.json",
     "26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571"),
    ("KG-Reextraido", "data/experiment/reextraccion_v2/corpus_v2/salida/kg.json",
     "8e2eadee57b48e00ccb51ade9a953ba1469001fe089c45d97c4307ccf2725581"),
    ("KG-Reextraido-r1", "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json",
     "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"),
]
SELLADO = "KG-Refinado"      # único grafo donde los retests midieron los ranks
LIMITE = 50
RE_PUNTO = re.compile(r"punto\s+(\d+(?:\.\d+)*)")
CLA, CAP, PRO, RIC = "TO_clasificacion", "TO_capitales", "TO_proteccion", "TO_regimen_informativo"


# ------------------ direccionamiento sin id (mismo adaptador que la sonda de anclas) ------------------ #
def norm(s) -> str:
    s = unicodedata.normalize("NFD", str(s or ""))
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", s.lower()).strip()


def _vals(o):
    if isinstance(o, dict):
        for v in o.values():
            yield from _vals(v)
    elif isinstance(o, list):
        for v in o:
            yield from _vals(v)
    else:
        yield str(o)


def texto(n): return norm(" | ".join([n.get("label") or ""] + list(_vals(n.get("properties") or {}))))


def anclas(n):
    ps = list(n.get("provenances") or []) or ([n["provenance"]] if isinstance(n.get("provenance"), dict) else [])
    out = set()
    for p in ps:
        if "punto" in p:
            out.add((p.get("archivo") or "", str(p.get("punto") or "")))
        else:
            for pt in RE_PUNTO.findall(norm(p.get("location"))):
                out.add((p.get("source_doc") or "", pt))
    return out


def objetivo(N, tipo, archivo, punto, contiene=(), no_contiene=()):
    out = set()
    for n in N:
        if tipo and n["type"] != tipo:
            continue
        if not any(a.startswith(archivo) and p == punto for a, p in anclas(n)):
            continue
        t = texto(n)
        if all(norm(c) in t for c in contiene) and not any(norm(c) in t for c in no_contiene):
            out.add(n["id"])
    return out


def rank_de(idx, consulta, ids_obj):
    """Menor posición (1-based) en buscar_nodos(consulta, LIMITE) de cualquier id objetivo; None si no está."""
    res = idx.buscar_nodos(consulta, LIMITE)["resultados"]
    for k, r in enumerate(res, 1):
        if r["id"] in ids_obj:
            return k
    return None


# ------------------------------- consultas selladas ------------------------------- #
def consultas(N):
    """Lista de (grupo, consulta, {objetivo: ids}, {objetivo: rank esperado en KG-Refinado}, fuente)."""
    obj = {}
    obj["C1"] = objetivo(N, "Obligacion", CLA, "1.1", ["los clientes de la entidad (tanto residentes en el pais"])
    obj["C2.bancos"] = objetivo(N, "Restriccion", CAP, "1.2", ["bancos", "exigencia basica"], ["restantes entidades"])
    obj["C2.restantes"] = objetivo(N, "Restriccion", CAP, "1.2", ["restantes entidades", "exigencia basica"])
    obj["C2.excepcion"] = objetivo(N, "Excepcion", CAP, "1.2", ["cajas de credito cooperativas"])
    c5 = [("N1", "6.5", "cada cliente, y la totalidad de sus financiaciones comprendidas"), ("N2", "6.5.1", "situacion normal"),
          ("N3", "6.5.2", "seguimiento especial"), ("N4", "6.5.2.1", "en observacion"),
          ("N5", "6.5.2.2", "en negociacion o con acuerdos de refinanciacion"), ("N6", "6.5.2.3", "tratamiento especial"),
          ("N7", "6.5.3", "con problemas"), ("N8", "6.5.4", "alto riesgo de insolvencia"), ("N9", "6.5.5", "irrecuperable")]
    for k, pt, fr in c5:
        obj["C5." + k] = objetivo(N, None, CLA, pt, [fr])
    obj["C6.N1"] = objetivo(N, "Excepcion", PRO, "1.1.2.5", ["mutuales o cooperativas"])
    obj["C6.rol"] = {"Sujeto_rol_sujeto_obligado_proteccion"}
    obj["C6.pnfc"] = {"Sujeto_proveedor_no_financiero_de_credito"}
    obj["C7"] = objetivo(N, "Obligacion", RIC, "7.1", ["para el calculo del importe correspondiente al mes n"])

    Q = []
    f = "data/backlog/retests/C1_retest_2026-07-31.md:42-44"
    Q += [("C1", "criterio general clasificación deudores", {"C1": 1}, f),
          ("C1", "qué clientes deben ser clasificados", {"C1": 1}, f),
          ("C1", "clasificación residentes en el exterior", {"C1": 3}, f)]
    f = "data/backlog/retests/C2_retest_2026-07-31.md:61-63"
    Q += [("C2", "exigencia básica bancos", {"C2.bancos": 1, "C2.excepcion": 3, "C2.restantes": 4}, f),
          ("C2", "exigencia básica restantes entidades", {"C2.excepcion": 1, "C2.restantes": 2, "C2.bancos": 13}, f)]
    f = "data/backlog/propuestas/E4_enumeracion_65.md:281-289 (simulación pre-aplicación; retest C5 (c) 7/7 en top-10)"
    Q += [("C5", "niveles clasificación deudores cartera comercial", {"C5.N1": 1, "C5.N7": 4, "C5.N9": 5, "C5.N2": 6, "C5.N3": 8}, f),
          ("C5", "seguimiento especial deudores", {"C5.N1": 1, "C5.N4": 3, "C5.N6": 4, "C5.N5": 5, "C5.N3": 6}, f),
          ("C5", "punto 6.5 niveles clasificación", {"C5.N1": 1, "C5.N7": 2, "C5.N9": 3, "C5.N2": 4, "C5.N8": 5, "C5.N3": 6}, f),
          ("C5", "situaciones que integran el seguimiento especial", {"C5.N3": 7}, f),
          ("C5", "cinco categorías cartera comercial", {"C5.N1": 1, "C5.N7": 7, "C5.N9": 8, "C5.N2": 9, "C5.N4": 10}, f),
          ("C5", "en negociación o con acuerdos de refinanciación", {"C5.N5": 1, "C5.N3": 2}, f),
          ("C5", "situación normal cartera comercial", {"C5.N2": 1, "C5.N1": 2, "C5.N4": 3, "C5.N6": 4, "C5.N5": 5}, f),
          ("C5", "reclasificación en tratamiento especial refinanciación", {"C5.N6": 4},
           "data/backlog/retests/C5_retest_2026-08-02.md:70-72 (proxy RT-C5-4, consulta plausible mínima)")]
    f = "data/backlog/propuestas/E3_salvedad_mutuales.md:288-298 (columna post; — = fuera del top-10)"
    c6q = [("asociación mutual financiaciones proveedor no financiero crédito", 1, None, 2),
           ("sujeto obligado protección usuarios servicios financieros", 1, 5, None),
           ("proveedor no financiero crédito", None, None, 1),
           ("asociación mutual", 1, None, None),
           ("definición proveedor no financiero crédito PNFC", None, None, 1),
           ("proveedor no financiero crédito comercios empresas personas jurídicas", None, None, 1),
           ("exclusión excluido no alcanzado no incluido sujeto obligado", 4, None, None),
           ("mutuales cooperativas sujeto obligado protección usuarios", 1, 2, None),
           ("excepción asociaciones mutuales cooperativas", 1, None, None),
           ("cooperativa que otorga financiaciones protección de usuarios", 1, 5, None),
           ("asociaciones mutuales proveedores no financieros de crédito", 1, None, 2)]
    for q, n1, rol, pnfc in c6q:
        Q.append(("C6", q, {"C6.N1": n1, "C6.rol": rol, "C6.pnfc": pnfc}, f))
    f = "data/backlog/retests/C7_retest_2026-08-03.md:78"
    Q += [("C7", "esquema cálculo importe mes n disminución exigencia franquicia", {"C7": 1}, f),
          ("C7", "responsabilidad patrimonial computable cálculo importe correspondiente al mes", {"C7": 1}, f),
          ("C7", "franquicia importe correspondiente al mes n cálculo esquema", {"C7": 1}, f)]
    return obj, Q


def top10(r):
    return r is not None and r <= 10


def main() -> int:
    print("sonda_ranks_buscar_nodos_UB21 — ranks con GraphIndex (harness.py) sobre los cuatro grafos")
    for f in ("data/experiment/evaluacion/harness.py", "data/experiment/evaluacion/loader.py"):
        print(f"{f} sha256 {hashlib.sha256(Path(f).read_bytes()).hexdigest()}")
    print(f"config: limite pedido={LIMITE} (tope harness 50); top-10 = rank<=10; tokens label+id; adapter_key=None")
    todo = OrderedDict()
    fuentes = OrderedDict()
    for nombre, ruta, sha_esp in GRAFOS:
        sha = hashlib.sha256(Path(ruta).read_bytes()).hexdigest()
        print()
        print(f"===== {nombre}  {ruta}")
        print(f"sha256 {sha}  -> {'OK' if sha == sha_esp else 'DIFIERE de ' + sha_esp}")
        if sha != sha_esp:
            print("  FRENO: sha distinto del declarado en el mandato; no se corre.")
            return 1
        raw = json.loads(Path(ruta).read_text(encoding="utf-8"))
        kg = L.load_graph_from_path(ruta, adapter_key=None)
        idx = H.GraphIndex(kg)
        print(f"loader: nodos={len(kg.nodes)} aristas={len(kg.edges)} (json: {len(raw['nodes'])}/{len(raw['edges'])})")
        obj, Q = consultas(raw["nodes"])
        print("objetivos direccionados sin id (n ids): " + ", ".join(f"{k}={len(v)}" for k, v in obj.items()))
        R = OrderedDict()
        for grupo, q, esperado, fuente in Q:
            fuentes[(grupo, q)] = fuente
            fila = OrderedDict()
            for ok, esp in esperado.items():
                ids_obj = obj[ok]
                r = rank_de(idx, q, ids_obj) if ids_obj else None
                fila[ok] = {"rank": r, "top10": top10(r), "esperado_top10": esp, "objetivo_presente": bool(ids_obj)}
            R[(grupo, q)] = fila
            partes = []
            for ok, v in fila.items():
                esp = v["esperado_top10"]
                # esperado None = «fuera del top-10» en la fuente; esperado numérico = rank exacto sellado
                coin = (v["rank"] == esp) if esp is not None else (not v["top10"])
                v["coincide"] = coin
                mark = "" if nombre != SELLADO else (" =" if coin else " ≠")
                partes.append(f"{ok}: rank={v['rank']} top10={'si' if v['top10'] else 'no'} esperado={esp}{mark}" + ("" if v["objetivo_presente"] else " [objetivo AUSENTE]"))
            print(f"  [{grupo}] {q!r}\n      " + " | ".join(partes))
        # C4 (e): posición de grupo_2 en la ventana de 40 de ver_vecinos entrantes de Sujeto_entidad_financiera
        padre, hijo = "Sujeto_entidad_financiera", "Sujeto_propuesto_entidades_financieras_del_grupo_2"
        vv = idx.ver_vecinos(padre, "entrantes", 40)
        if "error" in vv:
            pos, tot = None, None
            print(f"  [C4.e] ver_vecinos({padre}, entrantes, 40): {vv['error']}")
        else:
            ents = [x["vecino_id"] for x in vv["entrantes"]]
            tot = vv["n_entrantes_total"]
            pos = ents.index(hijo) if hijo in ents else None
            print(f"  [C4.e] ver_vecinos({padre}, entrantes, 40): total_entrantes={tot} posicion_grupo_2={pos} (esperado 6 de 145 en {SELLADO}; C4_retest:58)"
                  + ("" if hijo in {n['id'] for n in raw['nodes']} else " [hijo AUSENTE en el grafo]"))
        R[("C4.e", "ver_vecinos entrantes 40")] = {"posicion": pos, "total": tot}
        todo[nombre] = R

    print()
    print("===== Resumen: consultas con TODOS sus objetivos en el rank esperado (solo tiene sentido en KG-Refinado) y objetivos en top-10 por grafo")
    for nombre in todo:
        R = todo[nombre]
        n_q = sum(1 for k in R if k[0] != "C4.e")
        coinc = sum(1 for k, fila in R.items() if k[0] != "C4.e" and all(v["coincide"] for v in fila.values()))
        objs = [v for k, fila in R.items() if k[0] != "C4.e" for v in fila.values()]
        print(f"{nombre:18s} consultas={n_q} coinciden_con_esperado={coinc} objetivos={len(objs)} en_top10={sum(1 for v in objs if v['top10'])} "
              f"esperados_en_top10={sum(1 for v in objs if v['esperado_top10'] is not None)} objetivo_ausente={sum(1 for v in objs if not v['objetivo_presente'])}")
    print()
    print("fuentes de los ranks esperados:")
    for f in sorted(set(fuentes.values())):
        print(f"  - {f}")
    canon = json.dumps({n: {f"{k[0]}|{k[1]}": v for k, v in R.items()} for n, R in todo.items()}, ensure_ascii=False, sort_keys=True)
    print()
    print(f"sha256 del JSON canonico de resultados (determinismo): {hashlib.sha256(canon.encode('utf-8')).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
