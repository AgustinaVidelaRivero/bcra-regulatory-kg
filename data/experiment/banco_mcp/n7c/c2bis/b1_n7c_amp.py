"""N7c+, C2-bis: B1 de N7c+, determinística, USD 0. NavegadorRel (N7c) y NavegadorRelAmp (N7c+) de la copia sobre el Neo4j
de B6.3, solo en lectura, en los puntos de los 14 documentos de N3 (el campo `to` de sus preguntas, leído por código),
contra lo calculado aparte desde el grafo evaluado (kg.json, leído en su lugar) y el índice por punto.

Mide, solo con cuentas:
  - el prefijo: en cuántos puntos la salida de N7c es un prefijo exacto de la de N7c+, seguida de un salto de línea;
  - la familia: en cuántos la sección de la familia (cabecera, renglones dentro del tope y pie, o «ninguno») es, carácter
    por carácter, la que se arma con lo calculado aparte. Lo calculado aparte, sin el código de familias_nav_rel_amp ni de
    familias_nav_rel: el árbol (`padre` e `hijos` de puntos.json), con la raíz, los niveles, el recorrido por anchura, los
    ancestros y el parentesco por el prefijo común de los caminos desde la raíz, y los puntos que la sección de N7c lista
    dentro de su tope, con la regla de la sección sobre el kg.json (la cuenta de n7c/c1/b1_n7c.py);
  - la cita: en cuántos la última línea es la calculada aparte (el PDF de `archivo_a_to` del manifiesto y «Punto n» o
    «Sección n»), el PDF es el de la cabecera, y el instrumento (n7c/lector_cita_n7c_amp.py, con un Python 3.12) la lee
    como el punto mismo, con el documento en la forma «PDF»; y, como descriptiva, en cuántos es fundada contra lo que el
    lector del instrumento ve en la misma salida (el instrumento cuenta como visto el punto pedido solo cuando la salida
    muestra su texto: las que no dan tienen que ser, como conjunto, los puntos sin texto propio);
  - el tamaño de lo que N7c+ suma sobre N7c (len(N7c+) − len(N7c), con su salto de línea), en caracteres y en tokens
    estimados (familias_nav.tokens_estimados): la mediana, el percentil 95 (rango más cercano) y el máximo; y, como
    descriptivas, las familias con «ninguno», las cortadas por el tope y los parentescos;
  - el techo en N3, con la regla de B1: en cuántas de las 17 preguntas de tipo `varios_puntos` todas las anclas que no son
    la primera quedan a la vista desde la primera: en la sección de N7c o en la familia (dentro de sus topes), en los
    ancestros o en los hijos de ver_punto, o en los nietos de ver_descendientes (niveles=2). Aparte, por fuente.
El driver va envuelto: cada sesión se abre con acceso de lectura y sin notificaciones, y cada consulta se controla contra
las palabras de escritura de Cypher. La huella del Neo4j (control_neo4j_b63.estado) y el sha256 del kg.json, antes y
después. Ninguna salida de ver_punto se escribe en disco: al lector le llegan por su entrada estándar.
Imprime y escribe solo cuentas y sha256: ninguna pregunta, ningún criterio, ningún ancla, ninguna clave de punto.
Uso: NEO4J_URI=bolt://127.0.0.1:47687 <python del .venv> -B b1_n7c_amp.py <raiz de la copia> <kg.json> <preguntas_N3.json>
     <salida.json> --python-citas <python 3.12>
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import re
import statistics
import subprocess
import sys
from collections import Counter
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, KG, PREG, SALIDA = (Path(x).resolve() for x in sys.argv[1:5])
PY312 = sys.argv[sys.argv.index("--python-citas") + 1]
BANCO = RAIZ / "data" / "experiment" / "banco_mcp"
for _p in (BANCO / "mcp_kg", BANCO / "b63" / "v2" / "b2", RAIZ / "data" / "experiment" / "neo4j"):
    sys.path.insert(0, str(_p))

import neo4j  # noqa: E402
import familias_nav_rel_amp as FNRA  # noqa: E402
import control_neo4j_b63 as CNB  # noqa: E402
from conexion import abrir_driver  # noqa: E402
from grafos import GRAFOS  # noqa: E402

FNR, FN, IP = FNRA.FNR, FNRA.FN, FNRA.IP
SHA_N3 = "6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b"
KG_SHA = "576c97256185a0d5741cb2c35a2a85e91412f3e1119ad7a85d960b7d60c35ad3"
HUELLA_B63 = "2645da6d01795d520f3c4ab5e237050c530238061f849cd7d1e0170be9223463"
ESCRITURA = re.compile(r"\b(CREATE|MERGE|SET|DELETE|DETACH|REMOVE|DROP|LOAD\s+CSV|FOREACH)\b|CALL\s+(?!\{)", re.I)
CAMPOS_NEO4J = ("ok", "kg_meta_sha256", "n_nodos", "n_aristas", "huella_estado", "huella_contenido")
LECTOR = BANCO / "n7c" / "lector_cita_n7c_amp.py"


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
        self.consultas["n"] += 1
        return self.s.run(cypher, **params)


class DriverLectura:
    def __init__(self, d):
        self.d, self.consultas = d, Counter()

    def session(self, **kw):
        return SesionLectura(self.d.session(default_access_mode=neo4j.READ_ACCESS, notifications_min_severity="OFF", **kw),
                             self.consultas)

    def close(self):
        self.d.close()


def p95(xs: list[int]) -> int:
    o = sorted(xs)
    return o[math.ceil(0.95 * len(o)) - 1]


def resumen(xs: list[int]) -> dict:
    return {"n": len(xs), "mediana": statistics.median(xs), "p95": p95(xs), "maximo": max(xs), "suma": sum(xs)}


def main() -> int:
    res: dict = {"unidad": "N7c+, C2-bis, B1"}
    res["kg_sha256_antes"] = sha_archivo(KG)
    if res["kg_sha256_antes"] != KG_SHA:
        raise SystemExit("ABORTO: el kg.json no es el grafo evaluado")
    res["neo4j_antes"] = {k: v for k, v in CNB.estado(HUELLA_B63).items() if k in CAMPOS_NEO4J}
    if not res["neo4j_antes"]["ok"]:
        raise SystemExit("ABORTO: el Neo4j de B6.3 no da su huella")
    cfg = json.loads((BANCO / "n7c" / "config_mcp_kg_n7c_amp_evaluado.json").read_text(encoding="utf-8"))
    indice = (BANCO / "mcp_kg" / cfg["indice_puntos"]).resolve()
    drv = DriverLectura(abrir_driver())
    label = GRAFOS[cfg["grafo"]]["label"]
    kw = dict(sha256_manifiesto=cfg["sha256_manifiesto_indice"], hubs_esperados=cfg["hubs_esperados"])
    amp = FNRA.NavegadorRelAmp(drv, label, indice, **kw)
    rel = FNR.NavegadorRel(drv, label, indice, **kw)

    # ---------------- Las preguntas de N3, solo por código -----------------
    b = PREG.read_bytes()
    if hashlib.sha256(b).hexdigest() != SHA_N3:
        raise SystemExit("ABORTO: las preguntas de N3 no dan su sha256")
    P = json.loads(b)["preguntas"]
    tos = sorted({p["to"] for p in P})
    res["n3"] = {"preguntas": len(P), "tos": len(tos), "varios_puntos": sum(p["tipo"] == "varios_puntos" for p in P)}

    # ---------------- Lo calculado aparte: la sección de N7c, desde el kg.json -----------------
    g = json.loads(KG.read_bytes())
    PI = json.loads((indice / "puntos.json").read_bytes())
    man = json.loads((indice / "manifiesto.json").read_bytes())
    validos = {k for k, p in PI.items() if p["tipo"] != "to"}
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
    res["aparte"] = {"contenedores_iguales_al_navegador": cont == amp.contenedores, "hubs_iguales_al_navegador": hubs == amp.hubs}
    fuera_n = cont | hubs
    pts = {i: [k for k in ks if k in validos] for i, ks in claves.items()}
    nodos_de: dict[str, list[str]] = {}
    for i, ks in pts.items():
        for k in ks:
            nodos_de.setdefault(k, []).append(i)
    sal, ent = {}, {}
    for eid, e in enumerate(g["edges"]):
        if e["relation"] in FNR.GRUPO_DE:
            sal.setdefault(e["source"], []).append((eid, e["target"]))
            ent.setdefault(e["target"], []).append((eid, e["source"]))
    del g

    def seccion_n7c_aparte(k: str) -> list[str]:
        """Las claves de la sección de N7c, en su orden y sin tope (la regla de n7c/c1/b1_n7c.py)."""
        por: dict[str, set] = {}
        for v in nodos_de.get(k, []):
            if v in fuera_n:
                continue
            for lista in (sal.get(v, []), ent.get(v, [])):
                for eid, w in lista:
                    if w in fuera_n:
                        continue
                    for p in pts.get(w, []):
                        if p != k:
                            por.setdefault(p, set()).add(eid)
        return [p for p, _ in sorted(por.items(), key=lambda x: (-len(x[1]), x[0]))]

    # ---------------- Lo calculado aparte: la familia y la cita, desde el índice -----------------
    NOMBRE = {(1, 1): "hermano", (1, 2): "sobrino", (2, 1): "tío", (2, 2): "primo"}

    def es_to(c) -> bool:
        return c is None or PI[c]["tipo"] == "to"

    def camino(c: str, raiz: str) -> list[str]:
        """De la raíz a c, por `padre`."""
        r = [c]
        while r[-1] != raiz:
            r.append(PI[r[-1]]["padre"])
        return r[::-1]

    def familia_aparte(k: str, excluir_seccion: bool = True) -> list[tuple[str, int, str]]:
        padre = PI[k]["padre"]
        if es_to(padre):
            return []
        abuelo = PI[padre]["padre"]
        raiz, niveles = (padre, 2) if es_to(abuelo) else (abuelo, 3)
        prof, frente = {raiz: 0}, [raiz]
        for d in range(1, niveles + 1):
            nuevo = []
            for c in frente:
                for h in PI[c]["hijos"]:
                    if h in PI and h not in prof:
                        prof[h] = d
                        nuevo.append(h)
            frente = nuevo
        ancestros, x = set(), padre
        while not es_to(x):
            ancestros.add(x)
            x = PI[x]["padre"]
        fuera = {k, raiz} | ancestros | set(PI[k]["hijos"]) | (set(seccion_n7c_aparte(k)[:10]) if excluir_seccion else set())
        ck = camino(k, raiz)
        filas = []
        for c in prof:
            if c in fuera:
                continue
            cc = camino(c, raiz)
            j = 0
            while j < min(len(ck), len(cc)) and ck[j] == cc[j]:
                j += 1
            s, bb = len(ck) - j, len(cc) - j
            filas.append((c, s + bb, NOMBRE.get((s, bb), f"a {s + bb} pasos")))
        return sorted(filas, key=lambda f: (f[1], f[0]))

    def texto_familia_aparte(filas: list) -> str:
        if not filas:
            return "Puntos de la misma familia: ninguno"
        lin = [f"Puntos de la misma familia ({min(len(filas), 10)} de {len(filas)}; punto | título | parentesco):"]
        lin += [f"{c} | {FN._celda(PI[c]['titulo'] or '—', 60)} | {par}" for c, _, par in filas[:10]]
        if len(filas) > 10:
            lin.append(f"y {len(filas) - 10} puntos más: indice_to o ver_descendientes")
        return "\n".join(lin)

    archivo_de_to: dict[str, str] = {}
    for a, t in man["archivo_a_to"].items():
        archivo_de_to.setdefault(t, a)

    def cita_aparte(k: str) -> str:
        u = PI[k]["unidad"]
        forma = f"Punto {u}" if re.fullmatch(r"\d+(\.\d+)*", u) else f"Sección {u[1:]}" if u.startswith("S") else u
        return f"Para citar este punto: {archivo_de_to[PI[k]['to']]} | {forma}"

    res["archivos_del_manifiesto"] = {"n": len(man["archivo_a_to"]),
                                      "iguales_con_la_regla_de_la_cabecera": sum(FN._celda(a, 200) == a
                                                                                 for a in man["archivo_a_to"])}

    # ---------------- Por punto de los 14 documentos ----------------
    claves_b1 = sorted(k for k in validos if PI[k]["to"] in tos)
    c = Counter()
    chars, toks, casos = [], [], []
    parentescos = Counter()
    shas = []
    for k in claves_b1:
        c["no_resuelve_a_si_mismo"] += amp.resolver_punto(k) != k
        viejo, nuevo = rel.ver_punto(k), amp.ver_punto(k)
        pref = nuevo.startswith(viejo) and nuevo[len(viejo):len(viejo) + 1] == "\n"
        c["prefijo"] += pref
        resto = nuevo[len(viejo) + 1:].split("\n") if pref else []
        filas = familia_aparte(k)
        c["familia_igual"] += pref and "\n".join(resto[:-1]) == texto_familia_aparte(filas)
        c["familia_igual_a_la_del_navegador"] += [f[0] for f in amp.familia(k)] == [f[0] for f in filas]
        c["cita_igual"] += pref and resto[-1:] == [cita_aparte(k)]
        c["pdf_de_la_cabecera"] += f" — {amp.archivo_de(k)} · páginas " in nuevo.split("\n", 1)[0]
        c["familia_ninguno"] += not filas
        c["familia_cortada"] += len(filas) > 10
        c["familia_con_puntos_de_la_seccion_excluidos"] += len(familia_aparte(k, excluir_seccion=False)) > len(filas)
        parentescos.update(par if not par.startswith("a ") else "a k pasos" for _, _, par in filas[:10])
        chars.append(len(nuevo) - len(viejo))
        toks.append(FN.tokens_estimados(nuevo[len(viejo):]))
        shas.append(hashlib.sha256(nuevo.encode("utf-8")).hexdigest())
        casos.append({"clave": k, "salida": nuevo})
    secciones = {}
    for k2, p in PI.items():
        if p["tipo"] == "seccion" and isinstance(p["unidad"], str) and p["unidad"].startswith("S"):
            secciones.setdefault(p["to"], []).append(p["unidad"][1:])
    entrada = {"tos": [{"id": t, "archivo": a} for t, a in sorted(archivo_de_to.items())], "secciones": secciones,
               "casos": casos}
    r = subprocess.run([PY312, "-I", "-B", str(LECTOR)], input=json.dumps(entrada, ensure_ascii=False), capture_output=True,
                       text=True, env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))
    del casos, entrada
    if r.returncode:
        raise SystemExit("ABORTO: el lector de la cita frenó")
    lc = json.loads(r.stdout)
    sin_texto = {i for i, k in enumerate(claves_b1) if not any(x.strip() for x in PI[k]["textos"])}
    c["sin_texto_propio"] = len(sin_texto)
    c["no_fundadas_iguales_a_las_sin_texto_propio"] = set(lc["no_dan"]["fundada"]) == sin_texto
    res["b1"] = {"puntos": len(claves_b1), **dict(sorted(c.items())),
                 "cita_lector": {**lc["cuentas"], "no_dan": {x: len(v) for x, v in lc["no_dan"].items()}},
                 "instrumento_sha256": lc["instrumento_sha256"],
                 "parentescos_dentro_del_tope": dict(sorted(parentescos.items())),
                 "tamano_caracteres": resumen(chars), "tamano_tokens_estimados": resumen(toks),
                 "sha256_salidas": hashlib.sha256("\n".join(shas).encode("utf-8")).hexdigest()}

    # ---------------- El techo en N3 ----------------
    def clave_ancla(a: dict) -> str | None:   # correr_n6.ancla_to_punto, resuelta como la resuelven las herramientas
        return amp.resolver_punto(f"{a['to']}::{re.sub(r'[.]+$', '', a['punto'].strip())}")

    techo = Counter()
    for p in P:
        if p["tipo"] != "varios_puntos":
            continue
        cl = [clave_ancla(a) for a in p["gold"]["anclas"]]
        primero, otras = cl[0], sorted({x for x in cl[1:] if x != cl[0]}, key=str)
        techo["preguntas"] += 1
        if primero is None or not otras or None in otras:
            techo["sin_primero_en_el_indice_o_sin_otras"] += 1
            continue
        fuentes = {"seccion": set([f[0] for f in amp.relacionados(primero)][:FNR.TOPE_RELACIONADOS]),
                   "familia": set([f[0] for f in amp.familia(primero)][:FNRA.TOPE_FAMILIA]),
                   "ancestros": set(amp._ancestros(primero)), "hijos": set(PI[primero]["hijos"]),
                   "nietos": set(amp._descendientes(primero, 2)) - set(PI[primero]["hijos"])}
        sin_tope = fuentes | {"seccion": {f[0] for f in amp.relacionados(primero)}, "familia": {f[0] for f in amp.familia(primero)}}
        vista = set().union(*fuentes.values())
        techo["con_todas_a_la_vista"] += all(x in vista for x in otras)
        techo["con_todas_a_la_vista_sin_los_topes"] += all(x in set().union(*sin_tope.values()) for x in otras)
        techo["con_todas_en_la_seccion_de_n7c"] += all(x in fuentes["seccion"] for x in otras)
        techo["con_todas_a_la_vista_sin_la_seccion_de_n7c"] += all(
            x in set().union(*(v for f, v in fuentes.items() if f != "seccion")) for x in otras)
        techo["con_todas_a_la_vista_sin_la_familia"] += all(
            x in set().union(*(v for f, v in fuentes.items() if f != "familia")) for x in otras)
        for f, v in fuentes.items():
            techo[f"anclas_en_{f}"] += sum(x in v for x in otras)
        techo["anclas_otras"] += len(otras)
    res["techo_n3"] = dict(sorted(techo.items()))
    res["techo_igual_al_de_la_mesa_8"] = techo["con_todas_a_la_vista"] == 8

    res["consultas_al_neo4j"] = drv.consultas["n"]
    drv.close()
    res["neo4j_despues"] = {k: v for k, v in CNB.estado(HUELLA_B63).items() if k in CAMPOS_NEO4J}
    res["neo4j_igual"] = res["neo4j_antes"] == res["neo4j_despues"]
    res["kg_sha256_despues"] = sha_archivo(KG)
    res["kg_igual"] = res["kg_sha256_antes"] == res["kg_sha256_despues"]
    n = len(claves_b1)
    bb = res["b1"]
    res["todos"] = {"prefijo": bb["prefijo"] == n, "familia": bb["familia_igual"] == n,
                    "cita": bb["cita_igual"] == bb["pdf_de_la_cabecera"] == bb["cita_lector"]["lee"]
                    == bb["cita_lector"]["pdf"] == n}
    SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: res[k] for k in ("n3", "aparte", "archivos_del_manifiesto", "b1", "techo_n3",
                                          "techo_igual_al_de_la_mesa_8", "todos", "neo4j_igual", "kg_igual",
                                          "consultas_al_neo4j")}, ensure_ascii=False, indent=1))
    ok = all(res["todos"].values())
    return 0 if ok and res["neo4j_igual"] and res["kg_igual"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
