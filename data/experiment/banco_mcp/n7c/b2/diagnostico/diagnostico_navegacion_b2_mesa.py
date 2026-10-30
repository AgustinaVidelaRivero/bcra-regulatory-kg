"""Mesa, §362 (30/10/2026), USD 0: el diagnóstico de la navegación con los datos de B2 (N7, N7c y N7c+ sobre N3), por código y solo
con cuentas, y los techos en N3 de los arreglos posibles. Imprime y escribe solo cuentas, ids de pregunta de N3, nombres de herramientas
y de configuraciones: ningún texto, ninguna clave de punto.

Qué lee (solo lectura):
  · las sesiones de B2 (`fuera_del_repo/banco_n7c/agente/lote_*/N6-*`), cada una en su último intento: su log R1 (las llamadas, con su
    herramienta, su entrada y su salida) y su meta;
  · las preguntas de N3 (`unav_n3/preguntas_N3.json`, por su sha256): solo su tipo, su subtipo y sus anclas;
  · el índice por punto del grafo evaluado (el del árbol del repo, por el sha256 de su manifiesto) y su lectura, con
    `atribucion_fallas_nav.py` de HEAD (desde la copia de la mesa, sin editar);
  · el kg.json del grafo evaluado (en su lugar, sin rastrear, por su sha256), para las listas sin tope;
  · los errores del juez y el análisis de B2, para repartir por configuración las respuestas sin agregado estricto.

Qué cuenta:
  1. consultada, como el lector de la enmienda 1 de B2 (`n7c/lector_anclas_n7c.py`): por texto (los `textos` de `leer_paso`) o por
     nodo (ver_nodo o ver_vecinos con un nodo del ancla que no es contenedor). Control: las sesiones con todas las anclas consultadas
     tienen que dar las del análisis (35, 38 y 36 de 51);
  2. por cada ancla que faltó en una sesión de varios puntos: si estaba en la sección «Puntos relacionados» de alguna salida de
     ver_punto de la sesión, en la de la familia, en otra salida (vista), o en ninguna; las herramientas, las llamadas y las que le
     quedaban hasta 30 (el tope de las instrucciones);
  3. por pregunta y por subtipo, para cada configuración;
  4. los techos en N3 (la regla de B1: todas las anclas a la vista desde la primera) de: la sección y la familia sin tope; con tope 20;
     y las anclas que caen fuera del tope de hoy.
Uso: <python 3.12> -I -B este.py <copia de HEAD> <repo> <banco_n7c> <preguntas_N3.json> <kg evaluado> <salida.json>
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.dont_write_bytecode = True
COPIA, REPO, BANCO, PREG, KG, SALIDA = (Path(x).resolve() for x in sys.argv[1:7])
sys.path.insert(0, str(COPIA / "data" / "experiment" / "ev2_reporte" / "code"))
import atribucion_fallas_nav as AN  # noqa: E402  (HEAD, sin editar)
sys.path.insert(0, str(COPIA / "data" / "experiment" / "banco_mcp" / "mcp_kg"))
import familias_nav as FN  # noqa: E402  (HEAD, sin editar: resolver_punto)

IP = AN.IP
IDX = REPO / "data" / "experiment" / "banco_mcp" / "mcp_kg" / "indice_puntos" / "KG_Acumulado_Tandas0y1yFinal_r2b_sincola"
SHA = {"n3": "6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b",
       "man": "ef036b670321",
       "kg": "576c97256185"}
CONFIGS = ("N7", "N7c", "N7c_amp")
NOMBRE = {"N7": "N7", "N7c": "N7c", "N7c_amp": "N7c+"}
RE_SESION = re.compile(r"^N6-(N3-[A-Z]+\d+)-(N7(?:c(?:_amp)?)?)-r(\d+)(?:-i(\d+))?$")
RE_FILA = re.compile(r"^([a-z0-9_]+::\S+) \|")
TOPE_LLAMADAS = 30
C2 = ("remite_a", "condiciona", "exceptua", "exceptua_obligacion", "condicion_de")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def secciones(out: str) -> dict:
    """Las claves de las filas de la sección de relacionados y de la de familia de una salida de ver_punto."""
    res = {"rel": set(), "fam": set()}
    cur = None
    for linea in out.split("\n"):
        if linea.startswith("Puntos relacionados ("):
            cur = "rel"
            continue
        if linea.startswith("Puntos de la misma familia ("):
            cur = "fam"
            continue
        if cur and (linea.startswith("Para citar") or linea.startswith("y ") or not linea.strip()):
            cur = None if not linea.startswith("y ") else cur
            continue
        m = RE_FILA.match(linea)
        if cur and m:
            res[cur].add(m.group(1))
    return res


def main() -> int:
    res: dict = {"unidad": "mesa §362: el diagnóstico de la navegación con los datos de B2, y los techos en N3"}
    ok = {"n3": sha(PREG) == SHA["n3"], "man": sha(IDX / "manifiesto.json").startswith(SHA["man"]), "kg": sha(KG).startswith(SHA["kg"])}
    res["insumos_ok"] = ok
    if not all(ok.values()):
        raise SystemExit(f"ABORTO: {ok}")
    Q = {}
    for p in json.loads(PREG.read_bytes())["preguntas"]:
        anc = [f"{a['to']}::{re.sub(r'[.]+$', '', a['punto'].strip())}" for a in p["gold"]["anclas"]]
        Q[p["id"]] = {"tipo": p["tipo"], "subtipo": str(p.get("subtipo") or "—"), "anclas": anc}
    lec = AN.cargar_lectura(IDX, None, REPO)
    puntos = json.loads((IDX / "puntos.json").read_text(encoding="utf-8"))
    nodos = json.loads((IDX / "nodos.json").read_text(encoding="utf-8"))
    fuera = {n for n, x in nodos.items() if len(x["puntos"]) > AN.CONTENEDOR_MAX_ANCLAS or x["type"] in AN.IP.TIPOS_FUERA_DE_PUNTO}
    nav = FN.Navegador.__new__(FN.Navegador)
    nav.puntos = puntos

    # ---------------------------------------------------------------- las sesiones, en su último intento
    finales = {}
    for d in sorted((BANCO / "agente").glob("lote_0*/N6-*")):
        m = RE_SESION.match(d.name)
        if not m or not (d / f"log_r1_{d.name}.jsonl").is_file():
            continue
        clave = (m.group(1), m.group(2), int(m.group(3)))
        intento = int(m.group(4) or 1)
        if clave not in finales or intento >= finales[clave][0]:
            finales[clave] = (intento, d)
    res["sesiones_por_configuracion"] = dict(Counter(c for (_, c, _) in finales))

    filas = []
    for (qid, cid, rep), (_, d) in sorted(finales.items()):
        if Q[qid]["tipo"] != "varios_puntos":
            continue
        llamadas = []
        for x in (d / f"log_r1_{d.name}.jsonl").read_text(encoding="utf-8").splitlines():
            y = json.loads(x)
            if y.get("evento") == "llamada":
                llamadas.append((y.get("tool"), y.get("input") or {}, y.get("output_str")))
        claves = list(dict.fromkeys(AN.clave_de_ancla(a) for a in Q[qid]["anclas"]))
        nodos_de = {k: {n for n in lec["nodos_por_punto"].get(k, ()) if n not in fuera} for k in claves}
        textos, consultados_n, vistas, vistos_n = set(), set(), set(), set()
        en_rel, en_fam = set(), set()
        for tool, inp, out in llamadas:
            if not isinstance(out, str) or AN.es_salida_de_error(tool, out):
                continue
            if tool in AN.TOOLS_NAV:
                r = AN.leer_paso(tool, out, lec)
                textos |= set(r["textos"])
                vistas |= set(r["claves"])
                vistos_n |= set(r["ids"])
                if tool == "ver_punto":
                    s = secciones(out)
                    en_rel |= s["rel"]
                    en_fam |= s["fam"]
            elif tool in ("ver_nodo", "ver_vecinos"):
                nid = inp.get("id")
                if isinstance(nid, str):
                    consultados_n.add(nid)
        cons = {k for k in claves if k in textos or nodos_de[k] & consultados_n}
        faltan = [k for k in claves if k not in cons]
        detalle = []
        for k in faltan:
            donde = ("en_relacionados" if k in en_rel else "en_familia" if k in en_fam else
                     "vista_en_otra_salida" if (k in vistas or nodos_de[k] & vistos_n) else "no_aparecio")
            detalle.append(donde)
        filas.append({"qid": qid, "cid": cid, "rep": rep, "subtipo": Q[qid]["subtipo"], "anclas": len(claves),
                      "consultadas": len(cons), "todas": not faltan, "faltan": detalle,
                      "llamadas": len(llamadas), "herramientas": dict(Counter(t for t, _, _ in llamadas)),
                      "primera_ancla_consultada": bool(claves) and claves[0] in cons})

    # ---------------------------------------------------------------- 1. el control contra el análisis
    res["control_contra_el_analisis"] = {NOMBRE[c]: f"{sum(f['todas'] for f in filas if f['cid'] == c)} de "
                                                    f"{sum(f['cid'] == c for f in filas)}" for c in CONFIGS}
    # ---------------------------------------------------------------- 2. las anclas que faltaron
    por_cfg = {}
    for c in CONFIGS:
        fs = [f for f in filas if f["cid"] == c and not f["todas"]]
        por_cfg[NOMBRE[c]] = {
            "sesiones_sin_todas": len(fs),
            "anclas_que_faltaron": dict(Counter(x for f in fs for x in f["faltan"])),
            "llamadas_media": round(sum(f["llamadas"] for f in fs) / len(fs), 2) if fs else None,
            "llamadas_max": max((f["llamadas"] for f in fs), default=None),
            "les_quedaban_hasta_30_min": min((TOPE_LLAMADAS - f["llamadas"] for f in fs), default=None),
            "herramientas": dict(sum((Counter(f["herramientas"]) for f in fs), Counter())),
            "consultaron_la_primera_ancla": sum(f["primera_ancla_consultada"] for f in fs),
            "con_todas_llamadas_media": round(sum(f["llamadas"] for f in filas if f["cid"] == c and f["todas"])
                                              / max(1, sum(f["cid"] == c and f["todas"] for f in filas)), 2)}
    res["las_que_no_consultaron_todas"] = por_cfg
    # ---------------------------------------------------------------- 3. por pregunta y por subtipo
    pq = defaultdict(dict)
    for f in filas:
        e = pq[f["qid"]].setdefault(NOMBRE[f["cid"]], {"todas": 0, "de": 0, "faltan": Counter()})
        e["todas"] += f["todas"]
        e["de"] += 1
        e["faltan"].update(f["faltan"])
    res["por_pregunta"] = {q: {"subtipo": Q[q]["subtipo"], "anclas": len(set(AN.clave_de_ancla(a) for a in Q[q]["anclas"])),
                               **{c: f"{v['todas']} de {v['de']}" + (f" (faltaron: {dict(v['faltan'])})" if v["faltan"] else "")
                                  for c, v in sorted(d.items())}} for q, d in sorted(pq.items())}
    ps = defaultdict(lambda: defaultdict(lambda: [0, 0]))
    for f in filas:
        ps[f["subtipo"]][NOMBRE[f["cid"]]][0] += f["todas"]
        ps[f["subtipo"]][NOMBRE[f["cid"]]][1] += 1
    res["por_subtipo"] = {s: {c: f"{a} de {b}" for c, (a, b) in d.items()} for s, d in sorted(ps.items())}
    # ---------------------------------------------------------------- 4. los techos, con las listas sin tope
    g = json.loads(KG.read_bytes())
    sal, ent = defaultdict(list), defaultdict(list)
    grado = Counter()
    for eid, e in enumerate(g["edges"]):
        grado[e["source"]] += 1
        grado[e["target"]] += 1
        sal[e["source"]].append((eid, e["relation"], e["target"]))
        ent[e["target"]].append((eid, e["relation"], e["source"]))
    orden = sorted((grado.get(n["id"], 0) for n in g["nodes"]), reverse=True)
    umbral = orden[max(0, -(-len(orden) // 100) - 1)]
    hubs = {n["id"] for n in g["nodes"] if grado.get(n["id"], 0) >= umbral}
    pdn = defaultdict(list)
    for k, p in puntos.items():
        if p["tipo"] != "to":
            for nid in p["nodos"]:
                pdn[nid].append(k)
    excl = fuera | hubs

    def relacionados(k):
        por = defaultdict(set)
        for v in puntos[k]["nodos"]:
            if v in excl:
                continue
            for eid, rel, w in sal[v] + ent[v]:
                if rel in C2 and w not in excl:
                    for p in pdn[w]:
                        if p != k:
                            por[p].add(eid)
        return [p for p, _ in sorted(((p, len(x)) for p, x in por.items()), key=lambda f: (-f[1], f[0]))]

    def subida(k):
        return IP.ancestros(puntos, k)[::-1]

    def desc(k, niv):
        out, nivel = set(), [k]
        for _ in range(niv):
            nivel = [h for x in nivel for h in puntos[x]["hijos"] if h in puntos]
            out.update(nivel)
        return out

    def dist(a, b):
        sa, sb = [a] + subida(a), [b] + subida(b)
        c = next((x for x in sa if x in sb), None)
        return sa.index(c) + sb.index(c) if c is not None else 99

    def familia(k, ya):
        P = puntos
        padre = P[k]["padre"] if P[k]["padre"] in P and P[P[k]["padre"]]["tipo"] != "to" else None
        abuelo = P[padre]["padre"] if padre and P[padre]["padre"] in P and P[P[padre]["padre"]]["tipo"] != "to" else None
        raiz, niv = (abuelo, 3) if abuelo else (padre, 2) if padre else (None, 0)
        if raiz is None:
            return []
        excl_f = {k} | set(subida(k)) | set(P[k]["hijos"]) | set(ya)
        return sorted((x for x in desc(raiz, niv) if x not in excl_f and P[x]["tipo"] != "to"), key=lambda x: (dist(k, x), x))

    def techo(tope_rel, tope_fam):
        n = 0
        afuera = 0
        for q, d in Q.items():
            if d["tipo"] != "varios_puntos":
                continue
            ks = [nav.resolver_punto(a) for a in d["anclas"]]
            ks = list(dict.fromkeys(k for k in ks if k is not None))
            if not ks:
                continue
            k0 = ks[0]
            rel_all = relacionados(k0)
            rel = rel_all[:tope_rel] if tope_rel else rel_all
            fam_all = familia(k0, set(rel_all[:10]))
            fam = fam_all[:tope_fam] if tope_fam else fam_all
            vis = {k0} | set(subida(k0)) | set(puntos[k0]["hijos"]) | set(rel) | set(fam) | desc(k0, 2)
            n += all(k in vis for k in ks[1:])
            afuera += sum(1 for k in ks[1:] if k not in vis and (k in rel_all or k in familia(k0, set())))
        return n, afuera

    res["techos_N3"] = {"con_los_topes_de_hoy_10_y_10": techo(10, 10)[0], "con_tope_20_y_20": techo(20, 20)[0],
                        "sin_tope": techo(None, None)[0],
                        "anclas_en_las_listas_sin_tope_que_el_tope_de_hoy_deja_afuera": techo(10, 10)[1]}
    # ---------------------------------------------------------------- 5. el juez, por configuración
    ag = json.loads((BANCO / "analisis" / "analisis_b2_n7c.json").read_text(encoding="utf-8"))
    res["sin_agregado_estricto_por_configuracion"] = {
        NOMBRE[c]: ag["medidas"][c]["fidelidad"]["total_lectura_estricta"]["sin_veredicto"] for c in CONFIGS}
    res["sin_veredicto_con_la_tolerante"] = ag["sin_veredicto"]
    oid_a = {}
    for (qid, cid, rep), (_, d) in finales.items():
        meta = json.loads((d / f"meta_{d.name}.json").read_text(encoding="utf-8"))
        resp = (meta.get("final_json_R4") or {}).get("respuesta")
        if isinstance(resp, str) and resp.strip():
            s_r = hashlib.sha256(resp.encode("utf-8")).hexdigest()
            oid = "N6J-" + hashlib.sha256(f"N6:id_opaco_juez:v1|{qid}|{cid}|{rep}|{s_r}".encode("utf-8")).hexdigest()[:10]
            oid_a[oid] = cid
    err = Counter()
    sin = 0
    for k in (1, 2, 3):
        for x in (BANCO / "juez" / f"errores_r{k}.jsonl").read_text(encoding="utf-8").splitlines():
            if x.strip():
                c = oid_a.get(json.loads(x)["id_opaco"])
                if c:
                    err[NOMBRE[c]] += 1
                else:
                    sin += 1
    res["errores_del_juez_por_configuracion"] = {**dict(err), "sin_ubicar": sin}
    SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k in ("insumos_ok", "sesiones_por_configuracion", "control_contra_el_analisis", "las_que_no_consultaron_todas", "por_subtipo",
              "techos_N3", "sin_agregado_estricto_por_configuracion", "sin_veredicto_con_la_tolerante",
              "errores_del_juez_por_configuracion"):
        print(k, json.dumps(res[k], ensure_ascii=False))
    print("por pregunta:")
    for q, v in res["por_pregunta"].items():
        print(" ", q, json.dumps(v, ensure_ascii=False))
    print(f"-> {SALIDA.name} {sha(SALIDA)[:12]}…")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
