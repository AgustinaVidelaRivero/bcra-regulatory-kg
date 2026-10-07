"""U-RERESOL-CAT, R2-2 — controles y pre-medición (USD 0, sin API ni Neo4j). Corre desde la raíz de una COPIA del repo y
solo escribe --out-controles y --out-premedicion.

Controles (--cadenas D: el directorio con las cadenas corridas con el código nuevo por controles_r2_1.sh, una carpeta por
cadena con su r2/):
  parte_a        en r2b diez y r2b sin cola diez, contra los ensamblados sellados: las relaciones de
                 resolucion_sujetos.jsonl que cambian, una por una (destino antes y después), las filas nuevas del
                 registro, y las diferencias del grafo (nodos y aristas; procedencias de sujeto que se mudan); que todo
                 sea de docvig, el único documento de la tanda 0 sin alcance (enmienda 6, A.2: regla 1 = 4, regla 2 = 0).
  con_alcance    en los nueve documentos con alcance, las filas de resolucion_sujetos.jsonl y del registro de no mapeados,
                 byte a byte iguales a las selladas (A.5).
  mensaje_e1     el registro de alcance por tanda (catalogo_unico/registro_alcance_por_tanda.md) sumado en memoria al
                 rol_por_to de la release que lee prompt_r2b: el mensaje de E1 de toda unidad ya extraída (las de la E0
                 r2b de la tanda 0 y las del candado del mensaje) sale byte a byte igual; y la línea de alcance que
                 recibiría cada documento del registro. prompt_r2b no se edita: el atributo se reemplaza durante el
                 control y se restaura.
Pre-medición de la parte B rediseñada (BKL-0040): de las normas sin aplica_a de los documentos con alcance (población de
la parte B de R2-1, categoría `sin_aplica_a`), cuántas tienen en el texto propio o heredado de su unidad un label o un alias
de un Sujeto del catálogo distinto del rol de alcance (las claves R1 y el singular del índice de E4, como palabras
enteras), con la lista por TO y los diez sujetos más frecuentes; aparte, excluyendo también a los miembros del rol. Solo
medición; sin lectura.

Resumen (--trabajo W --out-resumen J, solo esto): junta lo que dejaron en W las cadenas, el catálogo sin ampliaciones por
la línea de comando, la suite con el código de HEAD y el nuevo, los selftests y las corridas de reresolver_catalogo.py,
con la doble corrida.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/r2_2_medicion.py \\
      --cadenas <dir de las cadenas> --out-controles <json> --out-premedicion <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import reresolver_catalogo as RR        # noqa: E402  (por él, el ensamblador y r1_e4)
import r2_1_medicion as M1              # noqa: E402  (población de la parte B, la de R2-1)

ENS, E4, C, RAIZ = RR.ENS, RR.E4, RR.C, RR.RAIZ
T = "data/experiment/reextraccion_v2/corpus_tanda0"
SELLADOS = OrderedDict([("r2b_diez", f"{T}/ens_diez_r2b/r2"), ("r2b_sincola_diez", f"{T}/ens_diez_r2b_sincola/r2")])
CRITERIOS_TEXTO = ("label_exacto", "alias_exacto", "label_singularizado")


def jsonl(p) -> list[dict]:
    return [json.loads(x) for x in Path(p).read_text(encoding="utf-8").splitlines() if x.strip()]


def lineas(p) -> list[str]:
    return Path(p).read_text(encoding="utf-8").splitlines()


def ordenado(c: Counter) -> dict:
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], str(kv[0]))))


# --------------------------------------------------------------------------------------------------------------- #
def control_parte_a(nuevo: Path, sellado: Path) -> dict:
    r0, r1 = jsonl(sellado / "resolucion_sujetos.jsonl"), jsonl(nuevo / "resolucion_sujetos.jsonl")
    g0, g1 = jsonl(sellado / "no_mapeados_sujetos.jsonl"), jsonl(nuevo / "no_mapeados_sujetos.jsonl")
    cambian = [OrderedDict([("to", b["to"]), ("chunk_id", b["chunk_id"]), ("indice_relacion", b["indice_relacion"]),
                            ("predicado", b["predicado"]), ("mencion", b["mencion"]),
                            ("mencion_verificada", b["mencion_verificada"]), ("sujeto_id_modelo", b["sujeto_id_modelo"]),
                            ("antes", [a["resuelto_a"], a["metodo_resolucion"]]),
                            ("despues", [b["resuelto_a"], b["metodo_resolucion"]])])
               for a, b in zip(r0, r1) if a != b]
    claves0 = {RR.clave(f) for f in g0}
    nuevas = [f for f in g1 if RR.clave(f) not in claves0]
    kg0 = json.loads((sellado / "kg.json").read_text(encoding="utf-8"))
    kg1 = json.loads((nuevo / "kg.json").read_text(encoding="utf-8"))
    dif = RR.diferencia(kg0, kg1)
    p0, p1 = RR.provs_sujeto(kg0), RR.provs_sujeto(kg1)
    nodos1 = {n["id"]: n for n in kg1["nodes"]}
    destino_de = {f["chunk_id"]: f["id_nodo"] for f in nuevas}
    return OrderedDict([
        ("sha256_sellado", hashlib.sha256((sellado / "kg.json").read_bytes()).hexdigest()),
        ("sha256_nuevo", hashlib.sha256((nuevo / "kg.json").read_bytes()).hexdigest()),
        ("relaciones", [len(r0), len(r1)]), ("relaciones_que_cambian", cambian),
        ("todas_de_docvig", all(c["to"] == "docvig" for c in cambian) and all(f["to"] == "docvig" for f in nuevas)),
        ("registro_filas", [len(g0), len(g1)]),
        ("registro_filas_nuevas", [OrderedDict([(k, f.get(k)) for k in ("to", "chunk_id", "indice_relacion", "mencion",
                                                                       "mencion_verificada", "sujeto_id_modelo", "motivo",
                                                                       "estado", "id_nodo")]) for f in nuevas]),
        ("registro_filas_que_cambian", sum(1 for a in g0 if RR.clave(a) in {RR.clave(b) for b in g1}
                                           and a != next(b for b in g1 if RR.clave(b) == RR.clave(a)))),
        ("grafo", OrderedDict([("nodos", [len(kg0["nodes"]), len(kg1["nodes"])]),
                               ("aristas", [len(kg0["edges"]), len(kg1["edges"])]),
                               ("nodos_agregados", [[i, nodos1[i]["label"], nodos1[i]["properties"]]
                                                    for i in dif["nodos_agregados"]]),
                               ("nodos_quitados", dif["nodos_quitados"]), ("nodos_que_cambian", dif["nodos_que_cambian"]),
                               ("aristas_agregadas", dif["aristas_agregadas"]), ("aristas_quitadas", dif["aristas_quitadas"]),
                               ("aristas_que_cambian", dif["aristas_que_cambian"]),
                               ("procedencias_de_sujeto_quitadas", [list(k) + [v] for k, v in sorted((p0 - p1).items())]),
                               ("procedencias_de_sujeto_agregadas", [list(k) + [v] for k, v in sorted((p1 - p0).items())]),
                               ("destino_en_el_registro", destino_de)]))])


def control_con_alcance(nuevo: Path, sellado: Path, sin_alcance: set[str]) -> dict:
    out = OrderedDict()
    for nombre in ("resolucion_sujetos.jsonl", "no_mapeados_sujetos.jsonl"):
        a = [x for x in lineas(sellado / nombre) if json.loads(x)["to"] not in sin_alcance]
        b = [x for x in lineas(nuevo / nombre) if json.loads(x)["to"] not in sin_alcance]
        out[nombre] = {"filas": [len(a), len(b)], "byte_a_byte_iguales": a == b}
    tos = sorted(p.name for p in (sellado / "por_to").iterdir() if p.is_dir() and p.name not in sin_alcance)
    out["por_to_iguales"] = {to: all((sellado / "por_to" / to / n).read_bytes() == (nuevo / "por_to" / to / n).read_bytes()
                                     for n in ("resolucion_sujetos.jsonl", "no_mapeados_sujetos.jsonl")) for to in tos}
    return out


def control_mensaje_e1() -> dict:
    import prompt_r2b as P              # noqa: PLC0415 — en el path por el ensamblador; se importa con sus candados
    reg = RR.leer_registro_alcance(RR.REGISTRO_ALCANCE_MD)
    cat = E4.catalogo_r2()
    entradas = RR.entradas_de_alcance(reg, P.ROL_POR_TO_R2, cat["labels"])
    man = json.loads((RAIZ / M1.MANIFIESTO).read_text(encoding="utf-8"))
    chunks = []
    for t in man["tos"]:
        d = json.loads((RAIZ / M1.E0_R2B / f"chunks_{t['id']}.json").read_text(encoding="utf-8"))
        chunks += d["chunks"] if isinstance(d, dict) else d
    candado = json.loads(P.CANDADO_MENSAJE_JSON.read_text(encoding="utf-8"))["chunks"]
    original = P.ROL_POR_TO_R2
    antes = [P.build_user_message_r2b(c) for c in chunks]
    antes_c = P.sha256_mensajes(candado)
    try:
        P.ROL_POR_TO_R2 = {**original, **entradas}
        despues = [P.build_user_message_r2b(c) for c in chunks]
        despues_c = P.sha256_mensajes(candado)
        lineas_nuevas = {a: P.linea_alcance(P.ROL_POR_TO_R2[a])[0] for a in entradas}
    finally:
        P.ROL_POR_TO_R2 = original
    distintos = [c["id"] for c, a, b in zip(chunks, antes, despues) if a != b]
    sha = lambda ms: hashlib.sha256("\n\x1e\n".join(ms).encode("utf-8")).hexdigest()  # noqa: E731
    return OrderedDict([
        ("registro", reg["fuente"]), ("registro_sha256", reg["fuente_sha256"]),
        ("entradas_del_registro", list(entradas)),
        ("sin_alcance_declarado", [f["to"] for fs in reg["tandas"].values() for f in fs if f["decision"] == "sin_alcance"]),
        ("unidades_tanda0_e0_r2b", len(chunks)), ("tos", [t["id"] for t in man["tos"]]),
        ("mensajes_distintos", distintos), ("sha256_mensajes_antes", sha(antes)), ("sha256_mensajes_despues", sha(despues)),
        ("candado_unidades", len(candado)), ("candado_sha256_antes", antes_c), ("candado_sha256_despues", despues_c),
        ("candado_sellado", P.MENSAJE_R2B_SHA256_ESPERADO),
        ("rol_por_to_de_la_release_restaurado", P.ROL_POR_TO_R2 is original),
        ("linea_de_alcance_de_los_documentos_del_registro", lineas_nuevas)])


# --------------------------------------------------------------------------------------------------------------- #
def premedicion() -> dict:
    mem = M1.entrada_en_memoria()
    ch = M1.chunks_e0()
    pb = M1.medir_parte_b(mem, ch)
    pob = [f for f in pb["_poblacion"] if f["categoria"] == "sin_aplica_a"]
    cat = mem["cat"]
    claves = sorted({(k, i) for (crit, k), i in cat["indice"].items()
                     if crit in CRITERIOS_TEXTO and k and i != "__AMBIGUO__"}, key=lambda x: (-len(x[0]), x[0]))
    filas, por_to1, por_to2, sin_raiz = [], Counter(), Counter(), Counter()
    ids1, ids2, claves_vistas = Counter(), Counter(), Counter()
    for f in pob:
        c = ch.get(f["chunk_id"]) or {}
        texto = " " + C.norm(" ".join([c.get("texto") or ""] + [h.get("texto") or "" for h in c.get("herencia") or []])) + " "
        entrada = cat["rol_por_to"].get(mem["archivo"][f["to"]]) or {}
        rol, miembros = f["rol_de_alcance"], set(entrada.get("miembros_ids") or [])
        hallados = OrderedDict()
        for k, i in claves:
            if f" {k} " in texto and i not in hallados:
                hallados[i] = k
        otros1 = OrderedDict((i, k) for i, k in hallados.items() if i != rol)
        otros2 = OrderedDict((i, k) for i, k in otros1.items() if i not in miembros)
        if otros1:
            por_to1[f["to"]] += 1
            ids1.update(otros1.keys())
            claves_vistas.update(otros1.values())
        if any(i != "Sujeto_sujeto" for i in otros1):
            sin_raiz[f["to"]] += 1
        if otros2:
            por_to2[f["to"]] += 1
            ids2.update(otros2.keys())
        filas.append(OrderedDict([("to", f["to"]), ("chunk_id", f["chunk_id"]), ("local_id", f["local_id"]),
                                  ("tipo", f["tipo"]), ("label", f["label"]), ("rol_de_alcance", rol),
                                  ("otros_sujetos", otros1), ("otros_fuera_de_los_miembros_del_rol", list(otros2))]))
    poblacion_por_to = Counter(f["to"] for f in pob)
    return OrderedDict([
        ("definicion", "normas (Obligacion, Restriccion, Potestad) de unidades aceptadas de los documentos con alcance sin "
                       "ninguna aplica_a (categoría sin_aplica_a de la población de la parte B de R2-1); el texto es el "
                       "propio de la unidad más el heredado, normalizado; un sujeto aparece si una clave del índice de E4 "
                       "de criterio label_exacto, alias_exacto o label_singularizado (no ambigua) está como palabra entera; "
                       "«otro» = distinto del rol de alcance; la segunda variante excluye además a los miembros del rol"),
        ("normas", len(pob)), ("normas_por_to", ordenado(poblacion_por_to)),
        ("con_otro_sujeto", sum(por_to1.values())), ("con_otro_sujeto_por_to", ordenado(por_to1)),
        ("con_otro_sujeto_sin_contar_la_raiz", sum(sin_raiz.values())),
        ("nota_raiz", "Sujeto_sujeto es la raíz del catálogo (label «Sujetos»): la palabra «sujeto(s)» la nombra sin nombrar "
                      "a nadie en particular; la cifra sin contarla está al lado"),
        ("con_otro_sujeto_fuera_de_los_miembros_del_rol", sum(por_to2.values())),
        ("con_otro_sujeto_fuera_de_los_miembros_por_to", ordenado(por_to2)),
        ("diez_sujetos_mas_frecuentes", [[i, n] for i, n in ordenado(ids1).items()][:10]),
        ("diez_sujetos_mas_frecuentes_fuera_de_los_miembros", [[i, n] for i, n in ordenado(ids2).items()][:10]),
        ("diez_claves_mas_frecuentes", [[k, n] for k, n in ordenado(claves_vistas).items()][:10]),
        ("control_poblacion_de_r2_1", OrderedDict([("poblacion", pb["poblacion"]),
                                                  ("sin_aplica_a", pb["poblacion_por_categoria"].get("sin_aplica_a"))])),
        ("detalle", filas)])


def sha(p) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def resumen(w: Path) -> dict:
    import r2_1_resumen_controles as RC1   # noqa: PLC0415 — comparar_dir, importado
    sellados = {"r2a_diez": "70d51e429b0e2cc1aafa697e32bc83462d371dfdd5edafb34e92fe4f7be45bdd",
                "r2a_desarrollo": "fa4c1043d859081e49dce6cb940a9f5d4c09fc6d449efb85355f95312257178a",
                "r2b_diez": "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57",
                "r2b_desarrollo": "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2",
                "r2b_sincola_diez": "e22fae1afc3cf37fbe5b49ee0b220d51d0ec5febc13abeb6ebf7b74226da34fb",
                "r2b_sincola_desarrollo": "2922b72dca2c2bcb204a04f53fc89f265ac2c57e83e6aaab2ce1af8b82d413e4"}
    out = OrderedDict()
    out["cadenas_sin_parametro"] = OrderedDict(
        (n, {"sha256": sha(w / "control" / "cadenas" / n / "r2" / "kg.json"), "sha256_de_siempre": s,
             "igual_al_de_siempre": sha(w / "control" / "cadenas" / n / "r2" / "kg.json") == s,
             "rc": (w / "control" / "cadenas" / f"consola_{n}.txt").read_text(encoding="utf-8").strip().splitlines()[-1]})
        for n, s in sellados.items())
    out["cli_con_catalogo_sin_ampliaciones"] = OrderedDict(
        (n, {"sha256": sha(w / "control" / "catalogo_vacio" / n / "r2" / "kg.json"),
             "igual_a_la_cadena_sin_parametro": sha(w / "control" / "catalogo_vacio" / n / "r2" / "kg.json")
             == sha(w / "control" / "cadenas" / c / "r2" / "kg.json")})
        for n, c in (("vacio_r2b_diez", "r2b_diez"), ("vacio_r2b_sincola_diez", "r2b_sincola_diez")))
    su = w / "control" / "suite"
    out["suite_head_contra_nuevo"] = OrderedDict(
        (p.stem.replace("suite_viejo_", ""), {"json_igual": p.read_bytes() == p.with_name(p.name.replace("viejo", "nuevo")).read_bytes(),
                                              "md_igual": p.with_suffix(".md").read_bytes()
                                              == p.with_name(p.name.replace("viejo", "nuevo")).with_suffix(".md").read_bytes()})
        for p in sorted(su.glob("suite_viejo_*.json")))
    out["selftests"] = OrderedDict((p.stem.replace("nuevo_", ""), p.read_text(encoding="utf-8").strip().splitlines()[-2:])
                                   for p in sorted((w / "control" / "selftests").glob("nuevo_*.txt")))
    co = OrderedDict()
    for p in sorted((w / "corridas").glob("*/reporte_reresolucion.json")):
        r = json.loads(p.read_text(encoding="utf-8"))
        g = r.get("gate") or {}
        co[p.parent.name] = OrderedDict([
            ("rc", (p.parent.parent / f"{p.parent.name}.log").read_text(encoding="utf-8").strip().splitlines()[-1]),
            ("anterior", r["entrada"]["anterior"]), ("generados_resolucion", r["entrada"]["generados_resolucion"]),
            ("sha256_kg", r["camino_b"]["sha256_kg"]), ("no_explicado", r["no_explicado"]),
            ("a_resueltas", r["camino_a"]["resueltas_ahora"]), ("a_mas_cambian", r["camino_a_mas"]["cambian_por_tipo"]),
            ("a_mas_reproduce", r["camino_a_mas"]["reproduce_la_decision_guardada"]),
            ("resolucion_b_igual_a_a_mas", r["resolucion_b_contra_a_mas"]["iguales"]),
            ("a_y_a_mas_coinciden", r["a_y_a_mas_coinciden_en_la_cuarentena"]["coinciden"]),
            ("parte_a", r["parte_a"]), ("rechazos_e2", r["camino_b"]["rechazos_e2_por_motivo"]),
            ("registro_por_estado", r["resueltos_por_version"]["registro_por_estado"]),
            ("gate_salida", {k: g.get("salida", {}).get(k) for k in ("shapes_veredicto", "shapes_bloqueantes_en_fail",
                                                                      "suite_resumen")}
             | {"ln6": (g.get("salida", {}).get("ln6") or {}).get("estado")}),
            ("gate_cambios", {"suite_estados": (g.get("comparacion") or {}).get("suite_estados_que_cambian"),
                              "shapes": (g.get("comparacion") or {}).get("shapes_que_cambian")})])
    out["corridas_del_script"] = co
    a1, a2 = w / "corridas" / "vacia_estable_diez_1", w / "corridas" / "vacia_estable_diez_2"
    c = RC1.comparar_dir(a1, a2, (("vacia_estable_diez_1", "<SALIDA>"), ("vacia_estable_diez_2", "<SALIDA>")))
    out["doble_corrida"] = {"iguales": c["iguales"], "iguales_con_ruta_normalizada": c["iguales_con_ruta_normalizada"],
                            "distintos": c["distintos"], "solo_en_una": c["solo_en_a"] + c["solo_en_b"]}
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--cadenas", type=Path, default=None)
    ap.add_argument("--out-controles", type=Path, default=None)
    ap.add_argument("--out-premedicion", type=Path, default=None)
    ap.add_argument("--trabajo", type=Path, default=None)
    ap.add_argument("--out-resumen", type=Path, default=None)
    a = ap.parse_args()
    if a.out_resumen:
        a.out_resumen.parent.mkdir(parents=True, exist_ok=True)
        a.out_resumen.write_text(json.dumps(resumen(a.trabajo), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{sha(a.out_resumen)}  {RR.ruta(a.out_resumen)}")
        return 0
    sin_alcance = {t["id"] for t in json.loads((RAIZ / M1.MANIFIESTO).read_text(encoding="utf-8"))["tos"]
                   if t["archivo"] not in E4.catalogo_r2()["rol_por_to"]}
    out = OrderedDict([("documentos_sin_alcance_de_la_tanda_0", sorted(sin_alcance))])
    for nombre, sellado in SELLADOS.items():
        nuevo = a.cadenas / nombre / "r2"
        out[nombre] = OrderedDict([("parte_a", control_parte_a(nuevo, RAIZ / sellado)),
                                   ("con_alcance", control_con_alcance(nuevo, RAIZ / sellado, sin_alcance))])
    out["mensaje_e1"] = control_mensaje_e1()
    pre = premedicion()
    for p, obj in ((a.out_controles, out), (a.out_premedicion, pre)):
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"{hashlib.sha256(p.read_bytes()).hexdigest()}  {RR.ruta(p)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
