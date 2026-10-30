"""N7c, C1, paso 6: B1, determinística, USD 0. NavegadorRel (familias_nav_rel.py de la copia) sobre el Neo4j de B6.3, solo
en lectura, en los puntos de los 14 documentos de N3 (el campo `to` de sus preguntas, leído por código), contra lo
calculado aparte desde el grafo evaluado (kg.json, leído en su lugar).

Mide, solo con cuentas:
  - el prefijo: en cuántos puntos la salida de NavegadorCand.ver_punto es un prefijo exacto de la de NavegadorRel, seguida
    de un salto de línea y la sección;
  - la lista: en cuántos la sección entera (cabecera, renglones dentro del tope y pie) es, carácter por carácter, la que
    se arma con lo calculado aparte;
  - las remisiones: cuando ni la sección ni ver_remisiones(punto, «ambas», 1, 20) se cortan, en cuántos el conjunto de
    puntos del grupo «remisión» es el de ver_remisiones a un salto (y las dos inclusiones, aparte);
  - el tamaño: lo que suma la sección (len(nueva) − len(anterior), con su salto de línea), en caracteres y en tokens
    estimados (familias_nav.tokens_estimados, 2,78 caracteres por token): la mediana, el percentil 95 (rango más
    cercano: el valor en la posición ⌈0,95·n⌉ del orden ascendente) y el máximo; y en cuántos puntos se corta la lista;
  - el techo en N3: en cuántas de las 17 preguntas de tipo `varios_puntos` las anclas del gold que no son la primera
    quedan unidas al punto de la primera por una arista de esos tipos (todas, alguna, y todas dentro del tope).
Lo calculado aparte, desde el kg.json y sin el código de familias_nav_rel: las claves de cada nodo (sus procedencias
con `to` y `punto`, por indice_puntos.base_punto), los contenedores (más de 10 claves o `TextoOrdenado`), los hubs (el
grado en el 1 % más alto, contado en las aristas del kg.json) y, por punto, los puntos unidos por las aristas de los
siete tipos, con la misma regla de la sección; los títulos y la existencia de cada punto, de puntos.json del índice.
El driver va envuelto: cada sesión se abre con acceso de lectura y cada consulta se controla contra las palabras de
escritura de Cypher. La huella del Neo4j (control_neo4j_b63.estado) y el sha256 del kg.json, antes y después.
Imprime y escribe solo cuentas y sha256: ninguna pregunta, ningún criterio, ningún ancla, ninguna clave de punto.
Uso: NEO4J_URI=bolt://127.0.0.1:47687 <python del .venv> -B b1_n7c.py <raiz de la copia> <kg.json> <preguntas_N3.json> <salida.json>
"""
from __future__ import annotations

import hashlib
import json
import math
import re
import statistics
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, KG, PREG, SALIDA = (Path(x).resolve() for x in sys.argv[1:5])
BANCO = RAIZ / "data" / "experiment" / "banco_mcp"
for _p in (BANCO / "mcp_kg", BANCO / "b63" / "v2" / "b2", RAIZ / "data" / "experiment" / "neo4j"):
    sys.path.insert(0, str(_p))

import neo4j  # noqa: E402
import familias_nav_rel as FNR  # noqa: E402
import control_neo4j_b63 as CNB  # noqa: E402
from conexion import abrir_driver  # noqa: E402
from grafos import GRAFOS  # noqa: E402

FNC, FN, IP = FNR.FNC, FNR.FN, FNR.IP
SHA_N3 = "6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b"
HUELLA_B63 = "2645da6d01795d520f3c4ab5e237050c530238061f849cd7d1e0170be9223463"
ESCRITURA = re.compile(r"\b(CREATE|MERGE|SET|DELETE|DETACH|REMOVE|DROP|LOAD\s+CSV|FOREACH)\b|CALL\s+(?!\{)", re.I)


def sha_archivo(p: Path) -> str:
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


class SesionLectura:
    def __init__(self, s, consultas: Counter):
        self.s, self.consultas = s, consultas

    def __enter__(self):
        return self

    def __exit__(self, *a):
        self.s.close()
        return False

    def run(self, cypher, **params):
        if ESCRITURA.search(cypher):
            raise SystemExit("ABORTO: una consulta con una palabra de escritura")
        self.consultas[cypher.split(" RETURN ", 1)[0][:60]] += 1
        return self.s.run(cypher, **params)


class DriverLectura:
    def __init__(self, d):
        self.d, self.consultas = d, Counter()

    def session(self, **kw):
        return SesionLectura(self.d.session(default_access_mode=neo4j.READ_ACCESS, **kw), self.consultas)

    def close(self):
        self.d.close()


def p95(xs: list[int]) -> int:
    o = sorted(xs)
    return o[math.ceil(0.95 * len(o)) - 1]


def resumen(xs: list[int]) -> dict:
    return {"n": len(xs), "mediana": statistics.median(xs), "p95": p95(xs), "maximo": max(xs), "suma": sum(xs)}


def main() -> int:
    res: dict = {"unidad": "N7c, C1, B1"}
    res["kg_sha256_antes"] = sha_archivo(KG)
    res["neo4j_antes"] = {k: v for k, v in CNB.estado(HUELLA_B63).items() if k in ("ok", "kg_meta_sha256", "n_nodos",
                                                                                   "n_aristas", "huella_estado",
                                                                                   "huella_contenido")}
    if not res["neo4j_antes"]["ok"]:
        raise SystemExit("ABORTO: el Neo4j de B6.3 no da su huella")
    cfg = json.loads((BANCO / "n7c" / "config_mcp_kg_n7c_evaluado.json").read_text(encoding="utf-8"))
    indice = (BANCO / "mcp_kg" / cfg["indice_puntos"]).resolve()
    drv = DriverLectura(abrir_driver())
    label = GRAFOS[cfg["grafo"]]["label"]
    kw = dict(sha256_manifiesto=cfg["sha256_manifiesto_indice"], hubs_esperados=cfg["hubs_esperados"])
    nav = FNR.NavegadorRel(drv, label, indice, **kw)
    cand = FNC.NavegadorCand(drv, label, indice, **kw)
    res["navegador"] = {"hubs": len(nav.hubs), "umbral_hub": nav.umbral_hub, "contenedores": len(nav.contenedores)}

    # ---------------- Las preguntas de N3, solo por código -----------------
    b = PREG.read_bytes()
    if hashlib.sha256(b).hexdigest() != SHA_N3:
        raise SystemExit("ABORTO: las preguntas de N3 no dan su sha256")
    P = json.loads(b)["preguntas"]
    tos = sorted({p["to"] for p in P})
    res["n3"] = {"preguntas": len(P), "tos": len(tos), "varios_puntos": sum(p["tipo"] == "varios_puntos" for p in P)}

    def clave_ancla(a: dict) -> str | None:   # correr_n6.ancla_to_punto, resuelta como la resuelven las herramientas
        return nav.resolver_punto(f"{a['to']}::{re.sub(r'[.]+$', '', a['punto'].strip())}")

    # ---------------- Lo calculado aparte, desde el kg.json -----------------
    g = json.loads(KG.read_bytes())
    puntos_idx = json.loads((indice / "puntos.json").read_bytes())
    validos = {k for k, p in puntos_idx.items() if p["tipo"] != "to"}
    claves, tipo_n = {}, {}
    for n in g["nodes"]:
        provs = n.get("provenances") or ([n["provenance"]] if n.get("provenance") else [])
        ks = []
        for pv in provs:
            if isinstance(pv, dict) and pv.get("to") and pv.get("punto"):
                k = IP.base_punto(f"{pv['to']}::{str(pv['punto']).strip()}")
                if k not in ks:
                    ks.append(k)
        claves[n["id"]], tipo_n[n["id"]] = ks, n.get("type")
    cont = {i for i, ks in claves.items() if len(ks) > 10 or tipo_n[i] == "TextoOrdenado"}
    grado = Counter()
    for e in g["edges"]:
        grado[e["source"]] += 1
        grado[e["target"]] += 1
    gr = {i: grado.get(i, 0) for i in claves}
    orden = sorted(gr.values(), reverse=True)
    umbral = orden[math.ceil(0.01 * len(orden)) - 1]
    hubs = {i for i, x in gr.items() if x >= umbral}
    sha_hubs = IP.sha256_bytes("\n".join(sorted(hubs)).encode("utf-8"))
    res["aparte"] = {"contenedores": len(cont), "de_mas_de_10": sum(len(claves[i]) > 10 for i in cont),
                     "textoordenado_de_10_o_menos": sum(len(claves[i]) <= 10 for i in cont),
                     "contenedores_iguales_al_navegador": cont == nav.contenedores,
                     "hubs": {"umbral": umbral, "n": len(hubs), "sha256": sha_hubs},
                     "hubs_iguales_a_la_config": {"umbral": umbral, "n": len(hubs), "sha256": sha_hubs} == cfg["hubs_esperados"],
                     "hubs_iguales_al_navegador": hubs == nav.hubs}
    fuera = cont | hubs
    pts = {i: [k for k in ks if k in validos] for i, ks in claves.items()}
    nodos_de: dict[str, list[str]] = {}
    for i, ks in pts.items():
        for k in ks:
            nodos_de.setdefault(k, []).append(i)
    sal, ent = {}, {}
    tipos_kg = Counter()
    for eid, e in enumerate(g["edges"]):
        if e["relation"] in FNR.GRUPO_DE:
            tipos_kg[e["relation"]] += 1
            sal.setdefault(e["source"], []).append((eid, e["relation"], e["target"]))
            ent.setdefault(e["target"], []).append((eid, e["relation"], e["source"]))
    del g
    with drv.session() as s:
        tipos_neo = {r["t"]: r["c"] for r in s.run(f"MATCH (:`{label}`)-[r]->(:`{label}`) WHERE type(r) IN $tipos "
                                                    "RETURN type(r) AS t, count(r) AS c",
                                                    tipos=list(FNR.TIPOS_RELACIONADOS)).data()}
    res["aristas_de_los_siete_tipos"] = {"kg": dict(sorted(tipos_kg.items())), "neo4j": dict(sorted(tipos_neo.items())),
                                         "iguales": dict(tipos_kg) == tipos_neo}
    GRUPOS = [x for x, _ in FNR.GRUPOS_RELACION]

    def esperado(k: str) -> list[tuple]:
        por: dict[str, dict] = {}
        for v in nodos_de.get(k, []):
            if v in fuera:
                continue
            for sentido, lista in (("sale", sal.get(v, [])), ("entra", ent.get(v, []))):
                for eid, rel, w in lista:
                    if w in fuera:
                        continue
                    for p in pts.get(w, []):
                        if p == k:
                            continue
                        x = por.setdefault(p, [set(), set(), set()])
                        x[0].add(eid)
                        x[1].add(FNR.GRUPO_DE[rel])
                        x[2].add(sentido)
        filas = [(p, [gg for gg in GRUPOS if gg in x[1]],
                  "las dos" if len(x[2]) == 2 else next(iter(x[2])), len(x[0])) for p, x in por.items()]
        return sorted(filas, key=lambda f: (-f[3], f[0]))

    def seccion_esperada(filas: list[tuple]) -> str:
        if not filas:
            return "Puntos relacionados: ninguno"
        lin = [f"Puntos relacionados ({min(len(filas), 10)} de {len(filas)}; punto | título | relación | dirección | aristas):"]
        lin += [f"{p} | {FN._celda(puntos_idx[p]['titulo'] or '—', 60)} | {', '.join(gs)} | {d} | {n}"
                for p, gs, d, n in filas[:10]]
        if len(filas) > 10:
            lin.append(f"y {len(filas) - 10} puntos más: ver_remisiones o vecinos_por_relacion")
        return "\n".join(lin)

    def claves_ver_remisiones(out: str) -> set | None:
        cuerpo = out.split("\n")
        if any(x.startswith("(") for x in cuerpo):
            return None
        return {x.split(" | ")[1] for x in cuerpo if x.startswith(("cita | ", "lo_citan | "))}

    # ---------------- Por punto de los 14 documentos ----------------
    claves_b1 = sorted(k for k in validos if puntos_idx[k]["to"] in tos)
    n_pref = n_pref_estricto = n_lista = cortados = no_resuelve = 0
    rem = Counter()
    chars, toks, shas = [], [], []
    for k in claves_b1:
        kr = nav.resolver_punto(k)
        no_resuelve += kr != k
        viejo, nuevo = cand.ver_punto(k), nav.ver_punto(k)
        n_pref += nuevo.startswith(viejo)
        estricto = nuevo.startswith(viejo) and nuevo[len(viejo):len(viejo) + 1] == "\n"
        n_pref_estricto += estricto
        seccion = nuevo[len(viejo) + 1:] if estricto else None
        filas = esperado(kr) if kr else []
        n_lista += seccion == (seccion_esperada(filas) if kr else None)
        cortados += len(filas) > 10
        extra = len(nuevo) - len(viejo)
        chars.append(extra)
        toks.append(FN.tokens_estimados(nuevo[len(viejo):]))
        shas.append(hashlib.sha256(nuevo.encode("utf-8")).hexdigest())
        if len(filas) <= 10:
            vr = claves_ver_remisiones(nav.ver_remisiones(kr, "ambas", 1, 20)) if kr else set()
            if vr is None:
                rem["ver_remisiones_cortada"] += 1
                continue
            mias = {p for p, gs, _, _ in filas if "remisión" in gs}
            rem["comparables"] += 1
            rem["iguales"] += mias == vr
            rem["seccion_dentro_de_ver_remisiones"] += mias <= vr
            rem["ver_remisiones_dentro_de_la_seccion"] += vr <= mias
            rem["las_dos_vacias"] += not mias and not vr
        else:
            rem["seccion_cortada"] += 1
    res["b1"] = {"puntos": len(claves_b1), "no_resuelven_a_si_mismos": no_resuelve, "prefijo_exacto": n_pref,
                 "prefijo_con_salto_y_seccion": n_pref_estricto, "lista_igual_a_la_calculada": n_lista,
                 "lista_cortada": cortados, "remisiones": dict(sorted(rem.items())),
                 "tamano_caracteres": resumen(chars), "tamano_tokens_estimados": resumen(toks),
                 "sha256_salidas": hashlib.sha256("\n".join(shas).encode("utf-8")).hexdigest()}

    # ---------------- El techo en N3 ----------------
    techo = Counter()
    for p in P:
        if p["tipo"] != "varios_puntos":
            continue
        cl = [clave_ancla(a) for a in p["gold"]["anclas"]]
        primero, otras = cl[0], sorted({c for c in cl[1:] if c != cl[0]}, key=str)
        techo["preguntas"] += 1
        if primero is None or not otras or None in otras:
            techo["sin_primero_en_el_indice_o_sin_otras"] += 1
            continue
        todos = [f[0] for f in nav.relacionados(primero)]
        techo["con_todas_unidas"] += all(c in todos for c in otras)
        techo["con_alguna_unida"] += any(c in todos for c in otras)
        techo["con_todas_dentro_del_tope"] += all(c in todos[:10] for c in otras)
        techo["con_todas_unidas_segun_lo_calculado_aparte"] += all(c in [f[0] for f in esperado(primero)] for c in otras)
    res["techo_n3"] = dict(sorted(techo.items()))

    res["consultas_al_neo4j"] = sum(drv.consultas.values())
    drv.close()
    res["neo4j_despues"] = {k: v for k, v in CNB.estado(HUELLA_B63).items() if k in ("ok", "kg_meta_sha256", "n_nodos",
                                                                                     "n_aristas", "huella_estado",
                                                                                     "huella_contenido")}
    res["neo4j_igual"] = res["neo4j_antes"] == res["neo4j_despues"]
    res["kg_sha256_despues"] = sha_archivo(KG)
    res["kg_igual"] = res["kg_sha256_antes"] == res["kg_sha256_despues"]
    SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("navegador", "n3", "aparte", "aristas_de_los_siete_tipos", "b1", "techo_n3",
                                          "neo4j_igual", "kg_igual", "consultas_al_neo4j")}, ensure_ascii=False, indent=1))
    ok = res["b1"]["prefijo_exacto"] == res["b1"]["lista_igual_a_la_calculada"] == len(claves_b1)
    return 0 if ok and res["neo4j_igual"] and res["kg_igual"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
