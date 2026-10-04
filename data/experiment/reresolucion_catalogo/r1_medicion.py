"""U-RERESOL-CAT, R1 — mediciones del diagnóstico y del diseño (USD 0, sin API ni Neo4j).

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.k y §4.l) y solo escribe --out. Mide sobre el crudo de r2a,
el único que existe al 04/10/2026 (mandato, R1.5); la prueba de R2 corre sobre el crudo de U-REEXT-T0.

Secciones de la salida:
  registro        recuento del registro de no mapeados de los dos grafos r2a (mandato, CONTEXTO).
  frecuencias     menciones verificadas en cuarentena, agrupadas por la clave del índice de E4: filas, unidades y
                  TOs (insumo del umbral de la regla de crecimiento).
  alcance         entradas de rol_por_to_r2.json y alcance de los diez TOs de la tanda 0.
  catalogo_prueba catálogo de resolución de prueba (en memoria y en un directorio temporal, nunca en el repo):
                  T1, alta del id Sujeto_prueba_cuentacorrentista; T2, alta del alias «integrantes de la Alta
                  Gerencia» en Sujeto_alta_gerencia. Qué generados cambian si se genera todo desde un único
                  archivo, y qué claves del índice de E4 se agregan o pasan a ambiguas.
  camino_a        r1_e4.reresolver_registro con el índice de prueba, sobre los dos registros.
  camino_a_mas    la regla de decisión de r1_e4.resolver_relaciones_r2 re-aplicada a todas las filas de
                  resolucion_sujetos.jsonl con el índice de prueba: relaciones fuera del registro que cambiarían.
  camino_b        la cadena r2 entera, en memoria, sobre el crudo guardado de r2a, en tres variantes por grafo:
                  b0 sin cambios (control: el sha256 de la cadena r2a con el código de HEAD), b1 con el catálogo de
                  prueba solo en los generados que lee E4 (sin cambiar los conjuntos de ids), b2 con el catálogo de
                  prueba también en los conjuntos de ids de E2 y del merge cross-TO. Diferencias b0 → b2 contra lo
                  que predicen (a), (a+) y el esqueleto, y registro de b2 contra la salida de (a).
  docvig          relaciones de sujeto de docvig, el único TO de la tanda 0 sin alcance: qué cambiaría la regla del
                  colectivo sin alcance (nota del 04/10/2026, decisión 2) y una cota por texto, declarada como tal.
  colectivos      formas de expresión colectiva en el texto propio de las unidades de los diez TOs (e0-r2 de r2a):
                  aproximación por texto, no medición de menciones.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/r1_medicion.py \
      --out data/experiment/reresolucion_catalogo/salidas/r1_medicion.json
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import re
import sys
import tempfile
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "r2_codigo2"))
import c1_comun as K                    # noqa: E402  (importado, no editado: GRAFOS, ENTRADA, E0_R2, parcheado)

ENS = K.ENS
E4 = ENS.E4
C = ENS.C
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "catalogo_unico" / "code"))
import generar_desde_catalogo as GEN    # noqa: E402

REX = RAIZ / "data" / "experiment" / "reextraccion_v2"
CATALOGO_R2 = RAIZ / "data" / "experiment" / "catalogo_unico" / "catalogo_sujetos_r2.json"
GENERADOS_R2 = RAIZ / "data" / "experiment" / "catalogo_unico" / "generados_r2"
SHA_CADENA_HEAD = {"diez": "70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd",       # freno_c2.md:83;
                   "desarrollo": "fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a"}  # c2_cadena.json
ID_T1 = "Sujeto_prueba_cuentacorrentista"
ALIAS_T2 = ("Sujeto_alta_gerencia", "integrantes de la Alta Gerencia")
VERIFICADAS = ("exacta", "tokens")
CAMPOS_VERSION = ("catalogo_sha256", "catalogo_sha256_resolucion")
RELACIONES_ESQUELETO_Y_PADRE = ("subclase_de", "instancia_de", "parte_de", "miembro_de", "padre_sugerido")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def jsonl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def ordenado(c: Counter) -> dict:
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], str(kv[0]))))


def clave_mencion(m: str) -> str:
    """La clave con la que el índice de E4 compara un label singularizado: sin artículo inicial, normalizada y
    singularizada por token (r1_e4._norm_sing)."""
    return E4._norm_sing(E4._sin_parentesis(E4.RE_ARTICULO_INICIAL.sub("", m)))


def clave_fila(f: dict) -> tuple:
    return (f["to"], f["chunk_id"], f.get("e0_sha256_completo"), f["indice_relacion"])


# --------------------------------------------------------------------------------------------------------------- #
# registro, frecuencias y alcance                                                                                  #
# --------------------------------------------------------------------------------------------------------------- #
def medir_registro(nombre: str) -> dict:
    filas = jsonl(RAIZ / K.GRAFOS[nombre]["dir"] / "no_mapeados_sujetos.jsonl")
    cu = [f for f in filas if f["estado"] == "cuarentena"]
    return {"filas": len(filas), "por_estado": ordenado(Counter(f["estado"] for f in filas)),
            "cuarentena_por_verificacion": ordenado(Counter(f["mencion_verificada"] for f in cu)),
            "cuarentena_por_motivo": ordenado(Counter(f["motivo"] for f in cu)),
            "cuarentena_con_sugerencia_del_modelo": sum(1 for f in cu if f.get("sujeto_id_modelo")),
            "cuarentena_por_to": ordenado(Counter(f["to"] for f in cu)),
            "resueltas_a_clase_por_motivo": ordenado(Counter(f["motivo"] for f in filas if f["estado"] != "cuarentena"))}


def medir_frecuencias(nombre: str) -> dict:
    filas = [f for f in jsonl(RAIZ / K.GRAFOS[nombre]["dir"] / "no_mapeados_sujetos.jsonl")
             if f["estado"] == "cuarentena"]
    grupos: dict[str, dict] = {}
    for f in filas:
        if f["mencion_verificada"] not in VERIFICADAS:
            continue
        g = grupos.setdefault(clave_mencion(f["mencion"]), {"filas": 0, "unidades": set(), "tos": set(),
                                                            "formas": set()})
        g["filas"] += 1
        g["unidades"].add((f["to"], f["chunk_id"]))
        g["tos"].add(f["to"])
        g["formas"].add(f["mencion"])
    tabla = [{"clave": k, "filas": g["filas"], "unidades": len(g["unidades"]), "tos": sorted(g["tos"]),
              "formas": sorted(g["formas"])} for k, g in grupos.items()]
    tabla.sort(key=lambda r: (-r["unidades"], -r["filas"], r["clave"]))
    no_verif = Counter(f["mencion"] for f in filas if f["mencion_verificada"] not in VERIFICADAS)
    return {"menciones_verificadas_en_cuarentena": sum(r["filas"] for r in tabla), "grupos": len(tabla),
            "tabla": tabla,
            "grupos_por_umbral": {f"unidades>={u}": [r["clave"] for r in tabla if r["unidades"] >= u] for u in (2, 3)}
            | {"tos>=2": [r["clave"] for r in tabla if len(r["tos"]) >= 2]},
            "no_verificadas": ordenado(no_verif)}


def medir_alcance() -> dict:
    rol = json.loads((GENERADOS_R2 / "rol_por_to_r2.json").read_text(encoding="utf-8"))
    man = json.loads((REX / "manifiestos" / "tanda0_ens_diez.json").read_text(encoding="utf-8"))
    tos = []
    for t in man["tos"]:
        e = rol.get(t["archivo"])
        tos.append({"to": t["id"], "archivo": t["archivo"],
                    "alcance": None if e is None else ("rol" if (e.get("rol_id") or "").startswith("Sujeto_rol")
                                                       else "clase"),
                    "id": None if e is None else (e.get("rol_id") or e.get("clase_ids"))})
    return {"entradas": len(rol),
            "entradas_con_rol": sum(1 for e in rol.values() if (e.get("rol_id") or "").startswith("Sujeto_rol")),
            "entradas_con_clase": sum(1 for e in rol.values() if not (e.get("rol_id") or "").startswith("Sujeto_rol")),
            "tanda0": tos, "tanda0_por_alcance": ordenado(Counter(str(t["alcance"]) for t in tos))}


# --------------------------------------------------------------------------------------------------------------- #
# catálogo de prueba                                                                                               #
# --------------------------------------------------------------------------------------------------------------- #
def catalogo_prueba() -> tuple[dict, str]:
    """Catálogo del request + T1 y T2, en el formato del catálogo único. Solo en memoria."""
    texto = CATALOGO_R2.read_text(encoding="utf-8")
    cat = json.loads(texto)
    base = next(s for s in cat["sujetos"] if s["id"] == "Sujeto_cliente")
    t1 = copy.deepcopy(base)
    t1.update(id=ID_T1, label="Cuentacorrentistas", alias=["cuentacorrentista"], definicion=None,
              padre="Sujeto_cliente", disjunta_con=[], padre_inferido=None,
              provenance_esqueleto={"source_doc": "catálogo de resolución de prueba (U-RERESOL-CAT, R1)",
                                    "location": "T1"},
              estado={"valor": "vigente", "alta": "prueba de U-RERESOL-CAT R1; no entra al catálogo del repo"},
              procedencia={"id": "prueba_r1"})
    cat["sujetos"].append(t1)
    s = next(x for x in cat["sujetos"] if x["id"] == ALIAS_T2[0])
    s["alias"] = list(s["alias"]) + [ALIAS_T2[1]]
    return cat, json.dumps(cat, ensure_ascii=False, indent=1) + "\n"


def generar(texto_cat: str, directorio: Path, nombre: str) -> dict[str, str]:
    p = directorio / nombre
    p.write_text(texto_cat, encoding="utf-8")
    return GEN.generar_todo(p)


def medir_catalogo_prueba(tmp: Path) -> tuple[dict, dict]:
    texto_req = CATALOGO_R2.read_text(encoding="utf-8")
    cat, texto = catalogo_prueba()
    reserializado = json.dumps(json.loads(texto_req), ensure_ascii=False, indent=1) + "\n"
    gen_req = GEN.generar_todo(CATALOGO_R2)          # desde su ruta: los generados del repo, byte a byte
    gen_res = generar(texto, tmp, "catalogo_resolucion_prueba.json")
    en_repo = {n: sha256_bytes((GENERADOS_R2 / n).read_bytes()) for n in gen_req}
    idx_req = E4.indice_desde_lista(json.loads(gen_req["indice_e4_r2.json"]))
    idx_res = E4.indice_desde_lista(json.loads(gen_res["indice_e4_r2.json"]))
    nuevas = sorted([list(k) + [v] for k, v in idx_res.items() if k not in idx_req])
    ambiguas = sorted([list(k) for k, v in idx_res.items() if v == "__AMBIGUO__" and idx_req.get(k) != "__AMBIGUO__"])
    cambian = sorted([list(k) for k, v in idx_res.items() if k in idx_req and idx_req[k] != v])
    vig = [s["id"] for s in cat["sujetos"] if s["estado"]["valor"] == "vigente"]
    datos = {
        "sha256_catalogo_request": sha256_bytes(texto_req.encode("utf-8")),
        "serializador_reproduce_el_archivo_del_request": reserializado == texto_req,
        "sha256_catalogo_prueba": sha256_bytes(texto.encode("utf-8")),
        "ids_vigentes_request": len([s for s in json.loads(texto_req)["sujetos"] if s["estado"]["valor"] == "vigente"]),
        "ids_vigentes_prueba": len(vig),
        "generados_desde_el_request_iguales_al_repo": {n: sha256_bytes(t.encode("utf-8")) == en_repo[n]
                                                       for n, t in gen_req.items()},
        "un_solo_archivo_cambia": sorted(n for n in gen_req
                                         if sha256_bytes(gen_req[n].encode()) != sha256_bytes(gen_res[n].encode())),
        "un_solo_archivo_no_cambia": sorted(n for n in gen_req
                                            if sha256_bytes(gen_req[n].encode()) == sha256_bytes(gen_res[n].encode())),
        "indice_claves_nuevas": nuevas, "indice_claves_que_pasan_a_ambiguas": ambiguas,
        "indice_claves_que_cambian_de_id": cambian,
    }
    res_dir = tmp / "generados_resolucion_prueba"
    res_dir.mkdir(exist_ok=True)
    for n, t in gen_res.items():
        (res_dir / n).write_text(t, encoding="utf-8")
    cat_res = {"catalogo_sha256": datos["sha256_catalogo_prueba"], "indice": idx_res,
               "labels": json.loads(gen_res["labels_e2_r2.json"]),
               "rol_por_to": json.loads(gen_req["rol_por_to_r2.json"]),
               "entrada_esqueleto": json.loads(gen_res["entrada_esqueleto_r2.json"]),
               "entrada_esqueleto_path": res_dir / "entrada_esqueleto_r2.json",
               "sujetos_set": frozenset(vig), "ids_nuevos": [ID_T1], "alias_nuevos": [list(ALIAS_T2)]}
    return datos, cat_res


# --------------------------------------------------------------------------------------------------------------- #
# caminos (a) y (a+)                                                                                               #
# --------------------------------------------------------------------------------------------------------------- #
def archivo_por_to(nombre: str) -> dict:
    man = json.loads((RAIZ / K.GRAFOS[nombre]["manifiesto"]).read_text(encoding="utf-8"))
    return {t["id"]: t["archivo"] for t in man["tos"]}


def camino_a(nombre: str, cat_res: dict) -> dict:
    filas = jsonl(RAIZ / K.GRAFOS[nombre]["dir"] / "no_mapeados_sujetos.jsonl")
    r = E4.reresolver_registro(filas, cat_res["indice"], cat_res["rol_por_to"], archivo_por_to(nombre),
                               cat_res["catalogo_sha256"])
    cambiadas = [(a, b) for a, b in zip(filas, r["filas"]) if a != b]
    idem = E4.reresolver_registro(r["filas"], cat_res["indice"], cat_res["rol_por_to"], archivo_por_to(nombre),
                                  cat_res["catalogo_sha256"])
    return {"filas": len(filas), "resueltas_ahora": r["resueltas_ahora"],
            "detalle": [{"to": b["to"], "chunk_id": b["chunk_id"], "indice_relacion": b["indice_relacion"],
                         "mencion": b["mencion"], "id_nodo": b["id_nodo"], "resuelto_a": b["resuelto_a"],
                         "metodo": b["metodo"], "calificador": b["calificador"]} for _, b in cambiadas],
            "campos_que_cambian": sorted({k for a, b in cambiadas for k in b if a.get(k) != b.get(k)}),
            "idempotente_con_el_mismo_indice": idem["resueltas_ahora"] == 0 and idem["filas"] == r["filas"],
            "_filas": r["filas"]}


def decidir(f: dict, idx: dict, prefijos: list, rol: str | None, padre: str | None) -> tuple[str | None, str]:
    """La regla de decisión de r1_e4.resolver_relaciones_r2 (:415-424) sobre una fila de resolucion_sujetos."""
    m, nivel, modelo = f["mencion"], f["mencion_verificada"], f["sujeto_id_modelo"]
    regla = (E4.resolver_mencion_r2(m, padre, idx, prefijos, rol) if m and nivel in VERIFICADAS
             else {"regla": None, "id": None, "criterios": []})
    if regla["regla"] == "R1":
        return regla["id"], "R1_" + "+".join(c for c in regla["criterios"] if c in E4.CRITERIOS_R1)
    if modelo:
        return modelo, "R4_sugerencia_modelo"
    if regla["regla"] == "R2":
        return regla["id"], "R2_" + "+".join(regla["criterios"])
    if regla["regla"] in ("R2_calificador", "R3"):
        return regla["id"], regla["regla"]
    return None, "cuarentena"


def camino_a_mas(nombre: str, cat_res: dict) -> dict:
    d = RAIZ / K.GRAFOS[nombre]["dir"]
    filas = jsonl(d / "resolucion_sujetos.jsonl")
    padres = {clave_fila(f): f.get("padre_sugerido") for f in jsonl(d / "no_mapeados_sujetos.jsonl")}
    apt = archivo_por_to(nombre)
    cat0 = E4.catalogo_r2()
    pre0, pre1 = E4._prefijos(cat0["indice"]), E4._prefijos(cat_res["indice"])
    control, cambian = 0, []
    for f in filas:
        rol = (cat0["rol_por_to"].get(apt[f["to"]]) or {}).get("rol_id")
        padre = padres.get(clave_fila(f))
        antes = decidir(f, cat0["indice"], pre0, rol, padre)
        if antes != (f["resuelto_a"], f["metodo_resolucion"]):
            control += 1
        despues = decidir(f, cat_res["indice"], pre1, rol, padre)
        if despues != antes:
            cambian.append({"to": f["to"], "chunk_id": f["chunk_id"], "indice_relacion": f["indice_relacion"],
                            "predicado": f["predicado"], "mencion": f["mencion"], "antes": list(antes),
                            "despues": list(despues), "en_el_registro": clave_fila(f) in padres})
    return {"relaciones_de_sujeto": len(filas), "decision_reproduce_la_guardada": control == 0,
            "filas_que_no_reproduce": control, "cambian": cambian,
            "cambian_fuera_del_registro": [c for c in cambian if not c["en_el_registro"]],
            "nota": "padre_sugerido solo existe en las filas del registro; para las demás se usa None (afecta solo "
                    "al criterio alias_en_parentesis)"}


# --------------------------------------------------------------------------------------------------------------- #
# camino (b): la cadena entera, en memoria                                                                         #
# --------------------------------------------------------------------------------------------------------------- #
def correr_cadena(nombre: str, cat: dict | None, sujetos: frozenset | None) -> dict:
    cfg = K.GRAFOS[nombre]
    man = ENS.MC.cargar(RAIZ / cfg["manifiesto"])
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = E4.modulo_modelos_r2()
    cat = cat or E4.catalogo_r2()
    escritos: dict = {}

    def w(n: str, obj) -> None:
        escritos[n] = json.loads(json.dumps(obj, ensure_ascii=False))

    rechazos: list[dict] = []
    original = ENS.e2_lib.ensamblar_r2

    def ensamblar_r2(chunks, regs, labels, conjunto, *a, **k):
        r = original(chunks, regs, labels, conjunto if sujetos is None else sujetos, *a, **k)
        rechazos.extend(r["rechazos_e2"])
        return r
    parches = [(E4, "catalogo_r2", lambda: cat), (ENS.e2_lib, "ensamblar_r2", ensamblar_r2)]
    with tempfile.TemporaryDirectory() as tmp:
        plan = ENS.plan_redirecciones_r2(man, perfil, RAIZ / K.ENTRADA, Path(tmp) / "r2", cat, M)
        if sujetos is not None:
            plan = [(m, a, sujetos if (m is ENS.INV and a == "SUJETOS_CATALOGO_SET") else v) for m, a, v in plan]
        with ENS.redirigido(plan), K.parcheado(parches):
            res = ENS.correr_cadena_r2(man, perfil, w, w, RAIZ / K.E0_R2)
    return {"kg": res["kg"], "sha256": res["sha256"], "resumen": res["resumen"], "escritos": escritos,
            "rechazos_e2": rechazos}


def rechazos_e2(corrida: dict) -> dict:
    return ordenado(Counter(f'{r["motivo"]}: {r["detalle"]}' for r in corrida["rechazos_e2"]))


def provs_sujeto(kg: dict) -> Counter:
    """(source, relación, target, chunk_id) de cada procedencia de las aristas de sujeto."""
    c = Counter()
    for e in kg["edges"]:
        if e["relation"] in E4.PREDICADOS_SUJETO_R2:
            for p in e.get("provenances") or [e.get("provenance")]:
                c[(e["source"], e["relation"], e["target"], p.get("chunk_id"))] += 1
    return c


def diferencia(kg0: dict, kg1: dict) -> dict:
    n0, n1 = {n["id"]: n for n in kg0["nodes"]}, {n["id"]: n for n in kg1["nodes"]}
    e0 = {(e["source"], e["relation"], e["target"]): e for e in kg0["edges"]}
    e1 = {(e["source"], e["relation"], e["target"]): e for e in kg1["edges"]}
    nodos_cambian = sorted(i for i in set(n0) & set(n1) if n0[i] != n1[i])
    aristas_cambian = sorted(k for k in set(e0) & set(e1) if e0[k] != e1[k])
    return {"nodos_quitados": sorted(set(n0) - set(n1)), "nodos_agregados": sorted(set(n1) - set(n0)),
            "nodos_que_cambian": {i: sorted({k for k in set(n0[i]) | set(n1[i]) if n0[i].get(k) != n1[i].get(k)}
                                            | {f"properties.{k}" for k in set(n0[i].get("properties", {}))
                                               | set(n1[i].get("properties", {}))
                                               if n0[i].get("properties", {}).get(k) != n1[i].get("properties", {}).get(k)})
                                  for i in nodos_cambian},
            "aristas_quitadas": [list(k) for k in sorted(set(e0) - set(e1))],
            "aristas_agregadas": [list(k) for k in sorted(set(e1) - set(e0))],
            "aristas_que_cambian": [list(k) for k in aristas_cambian]}


def prediccion(nombre: str, a: dict, a_mas: dict, cat_res: dict, kg0: dict) -> dict:
    """Lo que el registro, (a+) y el catálogo predicen sobre el grafo: cada procedencia de una relación que resuelve
    se muda del nodo en cuarentena (o del id anterior) al id nuevo; un nodo en cuarentena sin filas en cuarentena
    desaparece con su arista padre_sugerido; cada id nuevo entra con su esqueleto; cada alias nuevo cambia la
    propiedad alias del nodo del esqueleto."""
    mudanzas = []          # (chunk_id, relación, destino anterior, destino nuevo)
    resueltas = {(d["to"], d["chunk_id"], d["indice_relacion"]) for d in a["detalle"]}
    nodos_kg0 = {n["id"] for n in kg0["nodes"]}

    def en_kg0(i: str, to: str) -> str:
        # un propuesto repetido en más de un TO queda renombrado con __<to> en los TOs posteriores al primero
        return i if i in nodos_kg0 or f"{i}__{to}" not in nodos_kg0 else f"{i}__{to}"
    for d in a["detalle"]:
        mudanzas.append((d["chunk_id"], en_kg0(d["id_nodo"], d["to"]), d["resuelto_a"]))
    for c in a_mas["cambian_fuera_del_registro"]:
        mudanzas.append((c["chunk_id"], c["antes"][0], c["despues"][0]))
    sigue = Counter(f["id_nodo"] for f in a["_filas"] if f["estado"] == "cuarentena")
    desaparecen = sorted({en_kg0(d["id_nodo"], d["to"]) for d in a["detalle"] if d["id_nodo"] not in sigue})
    return {"mudanzas": [list(m) for m in mudanzas], "propuestos_que_desaparecen": desaparecen,
            "ids_nuevos": [i for i in cat_res["ids_nuevos"] if i not in nodos_kg0],
            "alias_nuevos_en": sorted({i for i, _ in cat_res["alias_nuevos"]}),
            "relaciones_que_resuelven": len(resueltas)}


def contrastar(pred: dict, kg0: dict, kg2: dict) -> dict:
    """Las diferencias b0 → b2 contra la predicción. Devuelve lo explicado y lo que no."""
    dif = diferencia(kg0, kg2)
    p0, p2 = provs_sujeto(kg0), provs_sujeto(kg2)
    quitadas, agregadas = p0 - p2, p2 - p0
    explicadas, no_explicadas = [], []
    pendientes_agregadas = Counter(agregadas)
    for (src, rel, tgt, cid), n in sorted(quitadas.items()):
        m = next((x for x in pred["mudanzas"] if x[0] == cid and x[1] == tgt), None)
        if m and pendientes_agregadas[(src, rel, m[2], cid)] >= n:
            pendientes_agregadas[(src, rel, m[2], cid)] -= n
            explicadas.append([src, rel, tgt, m[2], cid, n])
        else:
            no_explicadas.append({"procedencia_quitada": [src, rel, tgt, cid], "n": n})
    no_explicadas += [{"procedencia_agregada": list(k), "n": v} for k, v in pendientes_agregadas.items() if v > 0]
    esperados_quitados = set(pred["propuestos_que_desaparecen"])
    esperados_agregados = set(pred["ids_nuevos"])
    destinos = {m[2] for m in pred["mudanzas"]} | {m[1] for m in pred["mudanzas"]}
    nodos_no_explicados = (
        [{"nodo_quitado": i} for i in dif["nodos_quitados"] if i not in esperados_quitados]
        + [{"nodo_agregado": i} for i in dif["nodos_agregados"] if i not in esperados_agregados]
        + [{"nodo_que_cambia": i, "campos": c} for i, c in dif["nodos_que_cambian"].items()
           if i not in destinos and i not in pred["alias_nuevos_en"]])
    subjetos = set(E4.PREDICADOS_SUJETO_R2)
    aristas_no_explicadas = (
        [{"arista_quitada": k} for k in dif["aristas_quitadas"]
         if k[1] not in subjetos and not (k[1] == "padre_sugerido" and k[0] in esperados_quitados)]
        + [{"arista_agregada": k} for k in dif["aristas_agregadas"]
           if k[1] not in subjetos and not (k[1] in RELACIONES_ESQUELETO_Y_PADRE and k[0] in esperados_agregados)]
        + [{"arista_que_cambia": k} for k in dif["aristas_que_cambian"] if k[1] not in subjetos])
    return {"diferencia": dif, "procedencias_de_sujeto_mudadas": explicadas,
            "no_explicado": no_explicadas + nodos_no_explicados + aristas_no_explicadas}


def proyectar(f: dict) -> dict:
    return {k: v for k, v in f.items() if k not in CAMPOS_VERSION}


def registro_b_contra_a(a: dict, b2: dict, nombre: str) -> dict:
    reg_b = b2["escritos"]["no_mapeados_sujetos.jsonl"]
    res_b = {clave_fila(f): f for f in b2["escritos"]["resolucion_sujetos.jsonl"]}
    por_a = {clave_fila(f): f for f in a["_filas"]}
    por_b = {clave_fila(f): f for f in reg_b}
    resueltas_a = [k for k, f in por_a.items() if f["estado"] == "resuelto"]
    comunes = [k for k in por_a if k in por_b]
    return {
        "filas_a": len(por_a), "filas_b": len(por_b),
        "solo_en_a": [list(k) for k in sorted(set(por_a) - set(por_b), key=str)],
        "solo_en_b": [list(k) for k in sorted(set(por_b) - set(por_a), key=str)],
        "comunes_iguales_salvo_version": sum(1 for k in comunes if proyectar(por_a[k]) == proyectar(por_b[k])),
        "comunes_distintas_salvo_version": [list(k) for k in comunes if proyectar(por_a[k]) != proyectar(por_b[k])],
        "campos_de_version_distintos_en_comunes": sorted({c for k in comunes for c in CAMPOS_VERSION
                                                          if por_a[k].get(c) != por_b[k].get(c)}),
        "resueltas_en_a": [{"clave": list(k), "a": [por_a[k]["resuelto_a"], por_a[k]["metodo"]],
                            "b_resolucion": [res_b[k]["resuelto_a"], res_b[k]["metodo_resolucion"]] if k in res_b else None}
                           for k in resueltas_a],
    }


def camino_b(nombre: str, cat_res: dict, a: dict, a_mas: dict) -> dict:
    b0 = correr_cadena(nombre, None, None)
    b1 = correr_cadena(nombre, cat_res, None)
    b2 = correr_cadena(nombre, cat_res, cat_res["sujetos_set"])
    pred = prediccion(nombre, a, a_mas, cat_res, b0["kg"])
    out = {"b0_sha256": b0["sha256"], "b0_igual_a_la_cadena_de_head": b0["sha256"] == SHA_CADENA_HEAD.get(nombre, b0["sha256"]),
           "b0_igual_al_kg_en_disco": b0["sha256"] == K.sha256_path(RAIZ / K.GRAFOS[nombre]["dir"] / "kg.json"),
           "b0_rechazos_e2": rechazos_e2(b0), "b1_sha256": b1["sha256"], "b1_rechazos_e2": rechazos_e2(b1),
           "b2_sha256": b2["sha256"], "b2_rechazos_e2": rechazos_e2(b2),
           "prediccion": pred, "b2_contra_prediccion": contrastar(pred, b0["kg"], b2["kg"]),
           "b1_contra_b0": diferencia(b0["kg"], b1["kg"]),
           "registro_b2_contra_a": registro_b_contra_a(a, b2, nombre),
           "validacion_modelos_r2_b2": b2["resumen"]["validacion_modelos_r2"],
           "registro_no_mapeados_b2": b2["resumen"]["registro_no_mapeados"]}
    return out


# --------------------------------------------------------------------------------------------------------------- #
# docvig y expresiones colectivas                                                                                  #
# --------------------------------------------------------------------------------------------------------------- #
DETERMINANTES = ("la", "las", "el", "los", "dicha", "dichas", "dicho", "dichos", "esta", "estas", "este", "estos",
                 "tales", "toda", "todas", "cada", "restantes", "demas")
RE_COLECTIVO = re.compile(r"\b(" + "|".join(DETERMINANTES) + r")\s+(entidad|entidades|sujeto obligado|sujetos obligados)"
                          r"\b(\s+\w+)?")
CLASE_SIGUE = ("financiera", "financieras", "cambiaria", "cambiarias")


def chunks_e0(to: str) -> dict[str, dict]:
    d = json.loads((RAIZ / K.E0_R2 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    return {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}


def medir_docvig() -> dict:
    filas = [f for f in jsonl(RAIZ / K.GRAFOS["diez"]["dir"] / "resolucion_sujetos.jsonl") if f["to"] == "docvig"]
    ch = chunks_e0("docvig")
    colect_en_texto = []
    for f in filas:
        t = C.norm(ch[f["chunk_id"]]["texto"]) if f["chunk_id"] in ch else ""
        formas = sorted({f"{m.group(1)} {m.group(2)}" for m in RE_COLECTIVO.finditer(t)
                         if (m.group(3) or "").strip() not in CLASE_SIGUE})
        if f["metodo_resolucion"].startswith("R4") and formas:
            colect_en_texto.append({"chunk_id": f["chunk_id"], "sujeto_id_modelo": f["sujeto_id_modelo"],
                                    "formas_en_el_texto_propio": formas})
    return {"unidades_e0": len(ch), "relaciones_de_sujeto": len(filas),
            "por_metodo": ordenado(Counter(f["metodo_resolucion"] for f in filas)),
            "con_mencion": sum(1 for f in filas if f["mencion"]),
            "r4_con_mencion": sum(1 for f in filas if f["mencion"] and f["metodo_resolucion"].startswith("R4")),
            "cambiarian_con_la_regla_en_r2a": sum(
                1 for f in filas if f["metodo_resolucion"].startswith("R4") and f["mencion"]
                and f["mencion_verificada"] in VERIFICADAS
                and E4._sin_articulo(f["mencion"]) in E4.EXPRESIONES_COLECTIVAS_R3),
            "sugerencias_r4": ordenado(Counter(f["sujeto_id_modelo"] for f in filas
                                               if f["metodo_resolucion"].startswith("R4"))),
            "cota_por_texto": {"relaciones_r4_en_unidades_con_un_colectivo_en_el_texto_propio": len(colect_en_texto),
                               "detalle": colect_en_texto}}


def medir_colectivos() -> dict:
    man = json.loads((REX / "manifiestos" / "tanda0_ens_diez.json").read_text(encoding="utf-8"))
    por_forma, por_to = Counter(), Counter()
    seguidas_de_clase = Counter()
    for t in man["tos"]:
        for c in chunks_e0(t["id"]).values():
            for m in RE_COLECTIVO.finditer(C.norm(c.get("texto") or "")):
                forma = f"{m.group(1)} {m.group(2)}"
                if (m.group(3) or "").strip() in CLASE_SIGUE:
                    seguidas_de_clase[forma] += 1
                    continue
                por_forma[forma] += 1
                por_to[t["id"]] += 1
    en_r3 = {k: v for k, v in por_forma.items() if k.split(" ", 1)[1] in E4.EXPRESIONES_COLECTIVAS_R3
             and k.split(" ", 1)[0] in E4.ARTICULOS}
    return {"lista_r3": list(E4.EXPRESIONES_COLECTIVAS_R3), "articulos_que_quita": list(E4.ARTICULOS),
            "ocurrencias_por_forma": ordenado(por_forma), "ocurrencias_por_to": ordenado(por_to),
            "ocurrencias_total": sum(por_forma.values()),
            "ocurrencias_que_la_lista_r3_cubre": sum(en_r3.values()),
            "seguidas_de_una_clase_excluidas": ordenado(seguidas_de_clase),
            "nota": "aproximación sobre el texto propio de E0 (no son menciones de E1); se excluyen las formas "
                    "seguidas de financiera(s) o cambiaria(s), que nombran una clase del catálogo"}


# --------------------------------------------------------------------------------------------------------------- #
def medir() -> dict:
    out: dict = OrderedDict()
    out["registro"] = {g: medir_registro(g) for g in K.GRAFOS}
    out["frecuencias"] = {"diez": medir_frecuencias("diez")}
    out["alcance"] = medir_alcance()
    with tempfile.TemporaryDirectory() as tmp:
        datos, cat_res = medir_catalogo_prueba(Path(tmp))
        out["catalogo_prueba"] = datos
        out["camino_a"], out["camino_a_mas"], out["camino_b"] = {}, {}, {}
        for g in K.GRAFOS:
            a = camino_a(g, cat_res)
            am = camino_a_mas(g, cat_res)
            out["camino_b"][g] = camino_b(g, cat_res, a, am)
            a.pop("_filas")
            out["camino_a"][g], out["camino_a_mas"][g] = a, am
    out["docvig"] = medir_docvig()
    out["colectivos"] = medir_colectivos()
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=Path, required=True)
    args = ap.parse_args()
    res = medir()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(res, ensure_ascii=False, indent=1, default=list) + "\n", encoding="utf-8")
    print(f"{sha256_bytes(args.out.read_bytes())}  {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
