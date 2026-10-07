"""U-RERESOL-CAT, R2-1 — medición de la enmienda 6 a L-ESQ-R2 (§A.2 y §B.2) y del umbral de la regla de crecimiento
(enmienda 4 al protocolo, §1.2), sobre el crudo de U-REEXT-T0 (corpus_tanda0/salida_r2b, prefijo 322c5a23e9b7,
temperatura 0) y los registros de los ensamblados sellados. No implementa ninguna regla: simula. USD 0, sin API ni Neo4j.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.k y §4.l) y solo escribe --out y, con --fichas, las fichas de la
lectura de la parte B. La entrada de la cadena (entrada_r2 y resolver_relaciones_r2 por TO) se arma en memoria con las
redirecciones del ensamblador (plan_redirecciones_r2), como la cadena; control: las filas de resolución en memoria son
las de resolucion_sujetos.jsonl del ensamblado sellado.

Secciones de la salida:
  control         la entrada en memoria reproduce resolucion_sujetos.jsonl de KG-Tanda0-Diez-r2b (a9631a64).
  umbral          menciones verificadas en cuarentena, por clave del índice de E4: filas, unidades y TOs, en los registros
                  de los cuatro ensamblados r2b (diez y desarrollo, con la cola y sin ella); claves con 2 y 3 unidades.
  parte_a         documentos sin alcance (sin entrada en rol_por_to): relaciones que pasarían de la sugerencia del
                  modelo a cuarentena por la regla 1 (con la lista de hoy, con el singular y con el singular y los
                  determinantes) y por la regla 2 (sin mención; con una mención que no verifica), con los ids que
                  sugería el modelo; y las que ya están en cuarentena.
  no_verifican    las menciones que no verifican, en todos los documentos: expresión colectiva de cada lista o no, con
                  la lista de las demás, y cuántas están en el texto heredado de su unidad.
  r3_ampliada     documentos con alcance: relaciones en que cambia la decisión o la marca de desacuerdo si la lista de R3
                  se amplía (con el singular, que es «la entidad» y «el sujeto obligado»; con el singular y los
                  determinantes).
  parte_b         la población de la parte B, por simulación: normas (Obligacion, Restriccion, Potestad) de unidades
                  aceptadas de documentos con alcance sin aplica_a con mención verificada, con sus categorías; el caso
                  abierto (norma con una aplica_a con mención verificada y otra sin mención o con mención que no
                  verifica); la muestra de 30 con la semilla declarada (SEMILLA), sorteada antes de leer.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/r2_1_medicion.py \
      --out data/experiment/reresolucion_catalogo/salidas/r2_1_medicion.json \
      --fichas data/experiment/reresolucion_catalogo/salidas/r2_1_fichas_parte_b.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import sys
import tempfile
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ENS          # noqa: E402  (agrega al path los módulos de la cadena)

E4, C = ENS.E4, ENS.C
REX = "data/experiment/reextraccion_v2"
MANIFIESTO = f"{REX}/manifiestos/tanda0_ens_diez_r2b.json"
ENTRADA = f"{REX}/corpus_tanda0/salida_r2b"
E0_R2B = f"{REX}/e0_chunking/salida_tanda0_r2b"
ENSAMBLADOS = OrderedDict([("diez", f"{REX}/corpus_tanda0/ens_diez_r2b/r2"),
                           ("desarrollo", f"{REX}/corpus_tanda0/ens_desarrollo_r2b/r2"),
                           ("diez_sincola", f"{REX}/corpus_tanda0/ens_diez_r2b_sincola/r2"),
                           ("desarrollo_sincola", f"{REX}/corpus_tanda0/ens_desarrollo_r2b_sincola/r2")])
SHA_DIEZ_R2B = "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57"
SEMILLA = 20261006                      # declarada antes de sortear y de leer (FRENO R2-1)
MUESTRA = 30
NORMAS = ("Obligacion", "Restriccion", "Potestad")
VERIFICADAS = ("exacta", "tokens")
ARTICULOS = ("el", "la", "los", "las")
DETERMINANTES = ("cada", "esta", "estas", "este", "estos", "dicha", "dichas", "dicho", "dichos", "tal", "tales")
NUCLEOS_PLURAL = ("entidades", "sujetos obligados")           # la lista de R3 de hoy (r1_e4.py:306)
NUCLEOS_SINGULAR = ("entidad", "sujeto obligado")
LISTAS = OrderedDict([("hoy", (ARTICULOS, NUCLEOS_PLURAL)),
                      ("con_singular", (ARTICULOS, NUCLEOS_PLURAL + NUCLEOS_SINGULAR)),
                      ("con_singular_y_determinantes", (ARTICULOS + DETERMINANTES, NUCLEOS_PLURAL + NUCLEOS_SINGULAR))])


def jsonl(p) -> list[dict]:
    return [json.loads(x) for x in (RAIZ / p).read_text(encoding="utf-8").splitlines() if x.strip()]


def ordenado(c: Counter) -> dict:
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], str(kv[0]))))


def clave(f: dict) -> tuple:
    return (f["to"], f["chunk_id"], f.get("e0_sha256_completo"), f["indice_relacion"])


def colectiva(mencion: str | None, lista: str) -> bool:
    """La mención, normalizada y sin un determinante inicial de la lista, es un núcleo colectivo de la lista."""
    if not mencion:
        return False
    dets, nucleos = LISTAS[lista]
    w = C.norm(mencion).split()
    if w and w[0] in dets:
        w = w[1:]
    return " ".join(w) in nucleos


def clave_indice(m: str) -> str:
    return E4._norm_sing(E4._sin_parentesis(E4.RE_ARTICULO_INICIAL.sub("", m)))


# --------------------------------------------------------------------------------------------------------------- #
# entrada de la cadena en memoria                                                                                  #
# --------------------------------------------------------------------------------------------------------------- #
def entrada_en_memoria() -> dict:
    import runner_corpus as RC          # noqa: PLC0415
    man = ENS.MC.cargar(RAIZ / MANIFIESTO)
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = E4.modulo_modelos_r2()
    cat = E4.catalogo_r2()
    validar, pol = RC.validador_perfil_r2(perfil)
    versiones = {"catalogo_sha256": cat["catalogo_sha256"], "politica_sha256": pol.sha256, "perfil": "r2",
                 "prefijo_hash": perfil.prefijo_hash}
    por_to: dict = OrderedDict()
    with tempfile.TemporaryDirectory() as tmp:
        plan = ENS.plan_redirecciones_r2(man, perfil, RAIZ / ENTRADA, Path(tmp) / "r2", cat, M)
        with ENS.redirigido(plan):
            orden = list(C.TOS_ORDEN)       # redirigido: el orden del manifiesto (fuera del bloque vuelve al de dev)
            for to in orden:
                chunks = ENS._chunks_r2(to)
                regs = RC.entrada_r2(to, C.SALIDA / to, chunks, perfil, validar)
                res = E4.resolver_relaciones_r2(regs, cat["indice"], cat["rol_por_to"], versiones)
                por_to[to] = {"chunks": chunks, "regs": regs, "res": res}
    archivo = {t["id"]: t["archivo"] for t in man.tos}
    return {"por_to": por_to, "cat": cat, "archivo": archivo, "orden": orden}


def chunks_e0() -> dict[str, dict]:
    out = {}
    for p in sorted((RAIZ / E0_R2B).glob("chunks_*.json")):
        d = json.loads(p.read_text(encoding="utf-8"))
        for c in (d["chunks"] if isinstance(d, dict) else d):
            out[c["id"]] = c
    return out


# --------------------------------------------------------------------------------------------------------------- #
# secciones                                                                                                        #
# --------------------------------------------------------------------------------------------------------------- #
def medir_umbral() -> dict:
    out = OrderedDict()
    for g, d in ENSAMBLADOS.items():
        filas = jsonl(f"{d}/no_mapeados_sujetos.jsonl")
        grupos: dict[str, dict] = {}
        for f in filas:
            if f["estado"] != "cuarentena" or f["mencion_verificada"] not in VERIFICADAS:
                continue
            x = grupos.setdefault(clave_indice(f["mencion"]), {"filas": 0, "unidades": set(), "tos": set(), "formas": set()})
            x["filas"] += 1
            x["unidades"].add(f["chunk_id"])
            x["tos"].add(f["to"])
            x["formas"].add(f["mencion"])
        tabla = sorted(({"clave": k, "filas": v["filas"], "unidades": len(v["unidades"]), "tos": sorted(v["tos"]),
                         "formas": sorted(v["formas"]), "colectiva_con_singular": colectiva(k, "con_singular")}
                        for k, v in grupos.items()), key=lambda r: (-r["unidades"], -r["filas"], r["clave"]))
        cu = [f for f in filas if f["estado"] == "cuarentena"]
        out[g] = {"filas_registro": len(filas), "por_estado": ordenado(Counter(f["estado"] for f in filas)),
                  "cuarentena": len(cu), "cuarentena_por_verificacion": ordenado(Counter(f["mencion_verificada"] for f in cu)),
                  "cuarentena_con_sugerencia_del_modelo": sum(1 for f in cu if f.get("sujeto_id_modelo")),
                  "verificadas_en_cuarentena": sum(r["filas"] for r in tabla), "claves": len(tabla),
                  "claves_con_2_unidades_o_mas": [r for r in tabla if r["unidades"] >= 2],
                  "claves_con_3_unidades_o_mas": [r["clave"] for r in tabla if r["unidades"] >= 3],
                  "claves_en_2_tos_o_mas": [r["clave"] for r in tabla if len(r["tos"]) >= 2],
                  "tabla": tabla}
    return out


def filas_resolucion(mem: dict) -> list[dict]:
    return [f for v in mem["por_to"].values() for f in v["res"]["resolucion"]]


def rol_de(mem: dict, to: str) -> str | None:
    return (mem["cat"]["rol_por_to"].get(mem["archivo"][to]) or {}).get("rol_id")


def medir_parte_a(mem: dict) -> dict:
    sin_alcance = [to for to in mem["orden"] if mem["archivo"][to] not in mem["cat"]["rol_por_to"]]
    filas = [f for f in filas_resolucion(mem) if f["to"] in sin_alcance]
    r4 = [f for f in filas if f["metodo_resolucion"] == "R4_sugerencia_modelo"]
    tabla = OrderedDict()
    for lista in LISTAS:
        x = [f for f in r4 if f["mencion"] and f["mencion_verificada"] in VERIFICADAS and colectiva(f["mencion"], lista)
             and f["regla_texto"] is None]
        tabla[f"regla_1_{lista}"] = {"relaciones": len(x), "ids_sugeridos": ordenado(Counter(f["sujeto_id_modelo"] for f in x)),
                                     "menciones": ordenado(Counter(f["mencion"] for f in x))}
    x = [f for f in r4 if not f["mencion"]]
    tabla["regla_2_sin_mencion"] = {"relaciones": len(x), "ids_sugeridos": ordenado(Counter(f["sujeto_id_modelo"] for f in x))}
    x = [f for f in r4 if f["mencion"] and f["mencion_verificada"] not in VERIFICADAS]
    tabla["regla_2_mencion_no_verifica"] = {"relaciones": len(x),
                                            "ids_sugeridos": ordenado(Counter(f["sujeto_id_modelo"] for f in x)),
                                            "menciones": ordenado(Counter(f["mencion"] for f in x))}
    resto = [f for f in r4 if f["mencion"] and f["mencion_verificada"] in VERIFICADAS
             and not colectiva(f["mencion"], "con_singular_y_determinantes")]
    return OrderedDict([
        ("documentos_sin_alcance", sin_alcance),
        ("relaciones_de_sujeto", len(filas)), ("por_metodo", ordenado(Counter(f["metodo_resolucion"] for f in filas))),
        ("por_verificacion", ordenado(Counter(str(f["mencion_verificada"]) for f in filas))),
        ("ya_en_cuarentena", sum(1 for f in filas if f["metodo_resolucion"] == "cuarentena")),
        ("tabla_a2", tabla),
        ("r4_con_mencion_verificada_no_colectiva_no_cambian", {"relaciones": len(resto),
                                                               "menciones": ordenado(Counter(f["mencion"] for f in resto))}),
        ("por_predicado", ordenado(Counter(f["predicado"] for f in r4)))])


def medir_no_verifican(mem: dict, ch: dict) -> dict:
    filas = [f for f in filas_resolucion(mem) if f["mencion"] and f["mencion_verificada"] not in VERIFICADAS]

    def en_heredado(f) -> bool:
        her = " ".join(C.norm(h.get("texto") or "") for h in (ch.get(f["chunk_id"], {}).get("herencia") or []))
        return bool(E4._sin_articulo(f["mencion"])) and E4._sin_articulo(f["mencion"]) in her

    def en_propio_sin_articulo(f) -> bool:
        """Sin el artículo inicial, la mención está en el texto propio normalizado (p. ej. «el Comité de auditoría»
        contra «del Comité de auditoría»): la verificación literal no la encuentra por la contracción."""
        t = " " + C.norm(ch.get(f["chunk_id"], {}).get("texto") or "") + " "
        return bool(E4._sin_articulo(f["mencion"])) and f" {E4._sin_articulo(f['mencion'])} " in t
    out = OrderedDict([("menciones_que_no_verifican", len(filas)),
                       ("por_verificacion", ordenado(Counter(f["mencion_verificada"] for f in filas))),
                       ("por_to", ordenado(Counter(f["to"] for f in filas))),
                       ("por_metodo", ordenado(Counter(f["metodo_resolucion"] for f in filas)))])
    for lista in LISTAS:
        out[f"colectivas_{lista}"] = sum(1 for f in filas if colectiva(f["mencion"], lista))
    otras = [f for f in filas if not colectiva(f["mencion"], "con_singular_y_determinantes")]
    out["nombran_otra_cosa"] = len(otras)
    out["nombran_otra_cosa_en_el_texto_heredado"] = sum(1 for f in otras if en_heredado(f))
    out["colectivas_en_el_texto_heredado"] = sum(1 for f in filas if f not in otras and en_heredado(f))
    out["nombran_otra_cosa_sin_el_articulo_en_el_texto_propio"] = sum(1 for f in otras if en_propio_sin_articulo(f))
    out["nombran_otra_cosa_en_el_heredado_o_sin_el_articulo_en_el_propio"] = sum(
        1 for f in otras if en_heredado(f) or en_propio_sin_articulo(f))
    out["colectivas_sin_el_articulo_en_el_texto_propio"] = sum(1 for f in filas if f not in otras
                                                               and en_propio_sin_articulo(f))
    out["lista_de_las_que_nombran_otra_cosa"] = ordenado(Counter(
        f"{f['to']} | {f['mencion']} | {'heredado' if en_heredado(f) else 'no en el heredado'} | "
        f"{'sin artículo en el propio' if en_propio_sin_articulo(f) else 'no en el propio'} | "
        f"{f['metodo_resolucion']} {f['resuelto_a'] or ''}".strip() for f in otras))
    return out


def medir_r3_ampliada(mem: dict) -> dict:
    out = OrderedDict()
    filas = [f for f in filas_resolucion(mem) if rol_de(mem, f["to"])]
    for lista in ("con_singular", "con_singular_y_determinantes"):
        nuevas = [f for f in filas if f["mencion"] and f["mencion_verificada"] in VERIFICADAS
                  and f["regla_texto"] is None and colectiva(f["mencion"], lista) and not colectiva(f["mencion"], "hoy")]
        decision = [f for f in nuevas if not f["sujeto_id_modelo"]]
        desac = [f for f in nuevas if f["sujeto_id_modelo"] and f["sujeto_id_modelo"] != rol_de(mem, f["to"])]
        out[lista] = OrderedDict([
            ("relaciones_que_alcanza_r3", len(nuevas)),
            ("cambia_la_decision_cuarentena_a_r3", len(decision)),
            ("cambia_la_decision_por_to", ordenado(Counter(f["to"] for f in decision))),
            ("cambia_la_marca_de_desacuerdo", len(desac)),
            ("desacuerdo_por_id_del_modelo", ordenado(Counter(f"{f['to']}: {f['sujeto_id_modelo']}" for f in desac))),
            ("sin_cambio_el_modelo_sugiere_el_rol", len(nuevas) - len(decision) - len(desac)),
            ("menciones", ordenado(Counter(f["mencion"] for f in nuevas)))])
    return out


def medir_parte_b(mem: dict, ch: dict) -> dict:
    pob, abierto = [], []
    normas_total = Counter()
    for to in mem["orden"]:
        rol = rol_de(mem, to)
        if not rol:
            continue
        v = mem["por_to"][to]
        orden_e0 = {c["id"]: i for i, c in enumerate(v["chunks"])}
        reg_por = {(f["chunk_id"], f["indice_relacion"]): f for f in v["res"]["registro"]}
        for reg in v["regs"]:
            if ENS.e2_lib._estado_registro(reg)[0] != "aceptado" or reg["chunk_id"] not in orden_e0:
                continue
            val = reg["validacion"]
            rels = [r for r in val["relaciones"] if r["predicate"] == "aplica_a"]
            for e in val["entidades"]:
                if e["type"] not in NORMAS:
                    continue
                normas_total[to] += 1
                suyas = [r for r in rels if r["source"] == e["local_id"]]
                verif = [r for r in suyas if r.get("sujeto_mencion") and r.get("mencion_verificada") in VERIFICADAS
                         and (reg_por.get((reg["chunk_id"], r.get("indice_crudo"))) or {}).get("estado") != "descartado"]
                sin_m = [r for r in suyas if not r.get("sujeto_mencion")]
                no_v = [r for r in suyas if r.get("sujeto_mencion") and r.get("mencion_verificada") not in VERIFICADAS]
                desc = [r for r in suyas if (reg_por.get((reg["chunk_id"], r.get("indice_crudo"))) or {}).get("estado")
                        == "descartado"]
                rels_info = [{"indice": r.get("indice_crudo"), "mencion": r.get("sujeto_mencion"),
                              "mencion_verificada": r.get("mencion_verificada"),
                              "sujeto_id_modelo": r.get("sujeto_id_modelo"), "resuelto_a": r.get("sujeto_id_resuelto"),
                              "metodo": r.get("metodo_resolucion")} for r in suyas]
                fila = OrderedDict([("to", to), ("chunk_id", reg["chunk_id"]), ("orden_e0", orden_e0[reg["chunk_id"]]),
                                    ("local_id", e["local_id"]), ("tipo", e["type"]), ("label", e["label"]),
                                    ("descripcion", (e.get("properties") or {}).get("descripcion")),
                                    ("tramo", (e.get("provenance") or {}).get("tramo")),
                                    ("punto", (e.get("provenance") or {}).get("punto")),
                                    ("rol_de_alcance", rol), ("cola_humana", bool(reg.get("cola_humana"))),
                                    ("aplica_a", rels_info)])
                if not verif:
                    fila["categoria"] = ("sin_aplica_a" if not suyas else
                                         "aplica_a_sin_mencion" if sin_m and not no_v else
                                         "aplica_a_mencion_no_verifica" if no_v and not sin_m else
                                         "aplica_a_sin_mencion_y_no_verifica" if sin_m and no_v else
                                         "aplica_a_descartada")
                    fila["sugerencia_distinta_del_rol"] = any(r.get("sujeto_id_modelo") and r.get("sujeto_id_modelo") != rol
                                                              for r in suyas)
                    pob.append(fila)
                elif sin_m or no_v:
                    fila["destinos_verificados"] = sorted({r.get("sujeto_id_resuelto") or "cuarentena" for r in verif})
                    fila["destinos_de_las_otras"] = sorted({r.get("sujeto_id_resuelto") or "cuarentena" for r in sin_m + no_v})
                    abierto.append(fila)
    pob.sort(key=lambda f: (mem["orden"].index(f["to"]), f["orden_e0"], f["local_id"]))
    rnd = random.Random(SEMILLA)
    idx = sorted(rnd.sample(range(len(pob)), min(MUESTRA, len(pob))))
    muestra = [dict(pob[i], ficha=f"F{k:02d}", indice_en_la_poblacion=i) for k, i in enumerate(idx, 1)]
    for m in muestra:
        c = ch.get(m["chunk_id"]) or {}
        m["texto_de_la_unidad"] = c.get("texto")
        m["texto_heredado"] = [{"unidad_origen": h.get("unidad_origen"), "tipo": h.get("tipo"), "texto": h.get("texto")}
                               for h in (c.get("herencia") or [])]
        lab = (mem["cat"]["labels"].get(m["rol_de_alcance"]) or {}).get("label")
        alc = mem["cat"]["rol_por_to"].get(mem["archivo"][m["to"]]) or {}
        m["rol_de_alcance_label"] = lab
        m["rol_de_alcance_miembros"] = alc.get("miembros_labels")
    cats = Counter(f["categoria"] for f in pob)
    otra_misma = sum(1 for f in abierto if set(f["destinos_de_las_otras"]) <= set(f["destinos_verificados"]))
    return OrderedDict([
        ("normas_en_documentos_con_alcance", sum(normas_total.values())),
        ("normas_por_to", dict(normas_total)),
        ("poblacion", len(pob)),
        ("poblacion_por_to", ordenado(Counter(f["to"] for f in pob))),
        ("poblacion_por_tipo", ordenado(Counter(f["tipo"] for f in pob))),
        ("poblacion_por_categoria", ordenado(cats)),
        ("con_una_relacion_sin_mencion", sum(v for k, v in cats.items() if "sin_mencion" in k)),
        ("con_una_relacion_cuya_mencion_no_verifica", sum(v for k, v in cats.items() if "no_verifica" in k)),
        ("con_una_sugerencia_distinta_del_rol", sum(1 for f in pob if f["sugerencia_distinta_del_rol"])),
        ("en_la_cola_humana", sum(1 for f in pob if f["cola_humana"])),
        ("caso_abierto", OrderedDict([("normas", len(abierto)), ("por_to", ordenado(Counter(f["to"] for f in abierto))),
                                      ("las_otras_van_al_mismo_destino_que_la_verificada", otra_misma),
                                      ("las_otras_van_a_otro_destino", len(abierto) - otra_misma),
                                      ("detalle", abierto)])),
        ("muestra", OrderedDict([("semilla", SEMILLA), ("n", len(muestra)),
                                 ("indices_en_la_poblacion", idx),
                                 ("por_to", ordenado(Counter(m["to"] for m in muestra))),
                                 ("por_categoria", ordenado(Counter(m["categoria"] for m in muestra))),
                                 ("en_la_cola_humana", sum(1 for m in muestra if m["cola_humana"]))])),
        ("_muestra", muestra), ("_poblacion", pob)])


def medir() -> tuple[dict, list]:
    mem = entrada_en_memoria()
    ch = chunks_e0()
    sellado = jsonl(f"{ENSAMBLADOS['diez']}/resolucion_sujetos.jsonl")
    memoria = filas_resolucion(mem)
    out = OrderedDict()
    out["control"] = {"relaciones_en_memoria": len(memoria), "relaciones_selladas": len(sellado),
                      "resolucion_en_memoria_igual_a_la_sellada": memoria == sellado,
                      "kg_sellado_sha256": hashlib.sha256((RAIZ / ENSAMBLADOS["diez"] / "kg.json").read_bytes()).hexdigest(),
                      "kg_sellado_es_a9631a64": hashlib.sha256((RAIZ / ENSAMBLADOS["diez"] / "kg.json").read_bytes()).hexdigest()
                      == SHA_DIEZ_R2B}
    out["listas"] = {k: {"determinantes": list(v[0]), "nucleos": list(v[1])} for k, v in LISTAS.items()}
    out["umbral"] = medir_umbral()
    out["parte_a"] = medir_parte_a(mem)
    out["no_verifican"] = medir_no_verifican(mem, ch)
    out["r3_ampliada"] = medir_r3_ampliada(mem)
    pb = medir_parte_b(mem, ch)
    muestra = pb.pop("_muestra")
    pob = pb.pop("_poblacion")
    out["parte_b"] = pb
    out["parte_b_poblacion"] = [{k: f[k] for k in ("to", "chunk_id", "local_id", "tipo", "label", "categoria",
                                                   "sugerencia_distinta_del_rol", "cola_humana")} for f in pob]
    return out, muestra


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--out", type=Path, required=True)
    ap.add_argument("--fichas", type=Path, default=None, help="JSON con las 30 fichas de la muestra de la parte B")
    args = ap.parse_args()
    res, muestra = medir()
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{hashlib.sha256(args.out.read_bytes()).hexdigest()}  {args.out}")
    if args.fichas:
        args.fichas.write_text(json.dumps({"semilla": SEMILLA, "fichas": muestra}, ensure_ascii=False, indent=1) + "\n",
                               encoding="utf-8")
        print(f"{hashlib.sha256(args.fichas.read_bytes()).hexdigest()}  {args.fichas}")
    return 0 if res["control"]["resolucion_en_memoria_igual_a_la_sellada"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
