"""U-R2-CODIGO-2, C2 — controles de la E0 e0-r2 nueva (puntos f, h, l y n) (USD 0, sin API ni Neo4j). Solo escribe
--out.

Compara la salida nueva de e0-r2 de la tanda 0 (`--nueva`, la de `salida_tanda0_r2b/`) con:
  - su segunda corrida (`--doble`): byte a byte idénticas;
  - la versionada en f8dedd4 (`--base`, `salida_tanda0_r2/`): los archivos de los otros 9 TOs iguales byte a byte;
    en ric, solo los cambios declarados de f, h y l; en los archivos agregados, solo la entrada de ric; y los
    `pies_<to>.json`, uno por TO, como archivos nuevos;
y, si se pasan `--p152-base` y `--p152-nuevo` (e0-r2 de los 152 TOs de la partición con el código anterior y con el
nuevo, fuera del repo; `c2_e0_152.py`), la misma comparación sobre los 152: ningún id cambia (f), los renglones que se
ganan o se pierden (l) y las unidades con la herencia recortada (h). Con `--p152-regla-general` (la corrida de
`c2_e0_152.py --cola-en-toda-pagina`), la misma comparación para la regla de la cola de título en toda página: es la
medición que dejó la regla del punto l en una lista de páginas.

Además:
  f  las unidades renumeradas, con el número impreso en sus flags, y las citas de ric a 4.4.1 y 4.4.2 (las de M3.b),
     que ahora tienen unidad en la E0;
  h  las citas del texto omitido de la herencia de `ric::11.2.3` que dejan de atribuirse en esa unidad por la
     regla (i) de remite_a: las menciones del bloque heredado antes y después del recorte, y los nodos de la unidad
     en KG-Tanda0-Diez-r2a que las nombran;
  l  los renglones recuperados, con su página y su chunk;
  n  los diez `pies_<to>.json`: estados de las páginas, versión vigente y contraste con la carátula.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c2_e0.py \
      --nueva data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b --doble <segunda corrida> \
      [--p152-base <dir> --p152-nuevo <dir>] --out data/experiment/r2_codigo2/salidas/c2_e0.json
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict
from pathlib import Path

import c1_comun as K

import sys  # noqa: E402
sys.path.insert(0, str(K.RAIZ / K.REX / "e0_chunking"))
import correr_e0 as CE  # noqa: E402

REF = K.REF
U = CE.TOPE_HERENCIA_E0_R2[0]
DIEZ = ("cap", "cla", "ctacte", "docvig", "ext", "lingob", "pagjub", "polcre", "pro", "ric")
AGREGADOS = ("cobertura.json", "conteos.json", "correcciones.json", "divergencias_indice_cuerpo.json",
             "sub_chunking.json", "encabezados_conservados.json", "ids_desambiguados.json", "version_e0.json")
DECLARADOS_RIC = OrderedDict([
    ("ids_nuevos", ["ric::4.4::intro", "ric::4.4.1", "ric::4.4.2", "ric::4.4.3", "ric::4.4.4"]),
    ("texto_cambia", {"ric::4.3.3": "f", "ric::4.3.1.2": "l", "ric::6.1.2": "l", "ric::11.2::intro": "l",
                      "ric::12.4": "l"}),
    ("herencia_cambia", {"ric::11.2.3": "h"})])
CAMPOS_HERENCIA = {"herencia", "herencia_recortada", "chars_completo", "sha256_completo"}


def titulos_diez() -> dict:
    """Títulos del inventario de los diez TOs (regla g del detector), como los fija el ensamblado."""
    man = json.loads((K.RAIZ / K.GRAFOS["diez"]["manifiesto"]).read_text(encoding="utf-8"))
    return REF.titulos_de_inventario([t["id"] for t in man["tos"]],
                                     {t["id"]: t.get("nombres_remision", []) for t in man["tos"]})


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def chunks(d: Path, to: str) -> list[dict]:
    p = Path(d) / f"chunks_{to}.json"
    return leer(p) if p.exists() else []


def lineas_por_chunk(cs: list[dict]) -> Counter:
    return Counter((c["id"], ln) for c in cs for ln in (c.get("texto") or "").split("\n"))


def comparar_to(base: Path, nueva: Path, to: str) -> OrderedDict:
    cb, cn = chunks(base, to), chunks(nueva, to)
    ib, inn = [c["id"] for c in cb], [c["id"] for c in cn]
    db, dn = {c["id"]: c for c in cb}, {c["id"]: c for c in cn}
    comunes = [i for i in ib if i in dn]
    cambian = OrderedDict()
    for i in comunes:
        if db[i] != dn[i]:
            cambian[i] = sorted(k for k in set(db[i]) | set(dn[i]) if db[i].get(k) != dn[i].get(k))
    lb, ln = lineas_por_chunk(cb), lineas_por_chunk(cn)
    # renglones del texto propio, por TO (sin el chunk): los que se ganan y los que se pierden
    tb = Counter(x for (_, x), v in lb.items() for _ in range(v))
    tn = Counter(x for (_, x), v in ln.items() for _ in range(v))
    ganados = sorted((tn - tb).elements())
    perdidos = sorted((tb - tn).elements())
    return OrderedDict([
        ("chunks", (len(cb), len(cn))), ("ids_nuevos", [i for i in inn if i not in db]),
        ("ids_que_desaparecen", [i for i in ib if i not in dn]),
        ("orden_igual_en_comunes", [i for i in ib if i in dn] == [i for i in inn if i in db]),
        ("cambian", cambian),
        ("cambian_solo_en_la_herencia", sorted(i for i, ks in cambian.items() if set(ks) <= CAMPOS_HERENCIA)),
        ("renglones_ganados", ganados), ("renglones_perdidos", perdidos),
        ("con_herencia_recortada", sorted(c["id"] for c in cn if c.get("herencia_recortada")))])


def renglones_con_pagina(nueva: Path, to: str, renglones: list[str]) -> list[dict]:
    """Página y chunk de cada renglón recuperado, desde la estructura de E0 (segmentos con texto y páginas)."""
    cn = chunks(nueva, to)
    out = []
    for r in renglones:
        c = next((x for x in cn if r in (x.get("texto") or "").split("\n")), None)
        out.append({"renglon": r, "chunk_id": c["id"] if c else None, "paginas_del_chunk": c["paginas"] if c else None})
    return out


def control_diez(base: Path, nueva: Path, doble: Path) -> OrderedDict:
    fb = {p.name for p in base.glob("*.json")}
    fn = {p.name for p in nueva.glob("*.json")}
    fd = {p.name for p in doble.glob("*.json")}
    distintos_doble = sorted(n for n in fn & fd if (nueva / n).read_bytes() != (doble / n).read_bytes())
    por_to = OrderedDict()
    for to in DIEZ:
        archivos = sorted(n for n in fb if re.fullmatch(rf"(?:chunks|estructura|indice|tablas)_{to}\.json", n))
        iguales = [n for n in archivos if (nueva / n).exists() and (base / n).read_bytes() == (nueva / n).read_bytes()]
        por_to[to] = OrderedDict([("archivos", len(archivos)), ("iguales_byte_a_byte", len(iguales)),
                                  ("distintos", sorted(set(archivos) - set(iguales))),
                                  ("comparacion", comparar_to(base, nueva, to))])
    agregados = OrderedDict()
    for n in AGREGADOS:
        if not (base / n).exists() and not (nueva / n).exists():
            continue
        a, b = leer(base / n) if (base / n).exists() else {}, leer(nueva / n) if (nueva / n).exists() else {}
        agregados[n] = sorted(k for k in set(a) | set(b) if a.get(k) != b.get(k)) if isinstance(a, dict) else (
            "distinto" if a != b else [])
    ric = por_to["ric"]["comparacion"]
    texto_decl = DECLARADOS_RIC["texto_cambia"]
    cambian_texto = sorted(i for i, ks in ric["cambian"].items() if "texto" in ks)
    otros = sorted(i for i in ric["cambian"] if i not in texto_decl and i not in DECLARADOS_RIC["herencia_cambia"])
    nuevos_pies = sorted(fn - fb)
    return OrderedDict([
        ("doble_corrida", {"archivos": len(fn), "iguales": len(fn & fd) - len(distintos_doble),
                           "distintos": distintos_doble, "solo_en_una": sorted(fn ^ fd)}),
        ("archivos_nuevos", nuevos_pies), ("archivos_que_faltan", sorted(fb - fn)),
        ("otros_9_tos_iguales_byte_a_byte", all(not v["distintos"] for t, v in por_to.items() if t != "ric")),
        ("agregados_claves_que_cambian", agregados),
        ("ric_control", OrderedDict([
            ("ids_nuevos_igual_a_los_declarados", ric["ids_nuevos"] == DECLARADOS_RIC["ids_nuevos"]),
            ("ningun_id_desaparece", not ric["ids_que_desaparecen"]),
            ("texto_cambia_igual_a_los_declarados", cambian_texto == sorted(texto_decl)),
            ("herencia_cambia_igual_a_la_declarada",
             sorted(set(ric["cambian"]) - set(texto_decl)) == sorted(DECLARADOS_RIC["herencia_cambia"])),
            ("otros_cambios", otros)])),
        ("por_to", por_to)])


def control_f(base: Path, nueva: Path) -> OrderedDict:
    est = leer(nueva / "estructura_ric.json")
    base_est = leer(base / "estructura_ric.json")
    cn = {c["id"]: c for c in chunks(nueva, "ric")}
    unidades = {c["unidad"] for c in cn.values()}
    renum = [a for a in est["avisos"] if a["tipo"] == "renumerado_por_lista"]
    citas = []
    previos, REF.TITULOS_TOS = REF.TITULOS_TOS, titulos_diez()
    try:
        for c in cn.values():
            for men in REF.menciones_por_tramo([c.get("texto") or ""], "ric", REF.REGLAS_R2):
                for p in men["puntos"]:
                    if p.startswith("4.4") and men["clase"] == "interna":
                        citas.append({"chunk_id": c["id"], "punto": p, "unidad_en_la_e0_nueva": p in unidades,
                                      "tramo": men["evidencia"][:140]})
    finally:
        REF.TITULOS_TOS = previos
    return OrderedDict([
        ("avisos_renumerado_por_lista", renum),
        ("flags_de_las_unidades_renumeradas", {i: {k: cn[i]["flags"].get(k) for k in ("numero_impreso",
                                                                                       "correccion_numeracion")}
                                               for i in ("ric::4.4::intro", "ric::4.4.1", "ric::4.4.2") if i in cn}),
        ("rechazos_header_en_4_3_y_4_4", {
            "base": [{k: r.get(k) for k in ("pagina", "texto", "motivo")} for r in base_est["rechazos_header"]
                     if re.match(r"4\.[34]\.", r.get("texto") or "")],
            "nueva": [{k: r.get(k) for k in ("pagina", "texto", "motivo")} for r in est["rechazos_header"]
                      if re.match(r"4\.[34]\.", r.get("texto") or "")]}),
        ("citas_internas_a_4_4", citas),
        ("citas_a_4_4_1_y_4_4_2_con_unidad", all(x["unidad_en_la_e0_nueva"] for x in citas
                                                if x["punto"] in ("4.4.1", "4.4.2")) and any(
            x["punto"] in ("4.4.1", "4.4.2") for x in citas))])


def control_h(base: Path, nueva: Path) -> OrderedDict:
    cid, u = "ric::11.2.3", "11.2"
    vb = next(c for c in chunks(base, "ric") if c["id"] == cid)
    vn = next(c for c in chunks(nueva, "ric") if c["id"] == cid)
    titulos_previos, REF.TITULOS_TOS = REF.TITULOS_TOS, titulos_diez()
    try:
        def menciones(ch):
            tramos = [h["texto"] for h in ch["herencia"] if h["unidad_origen"] == u]
            return [m for m in REF.menciones_por_tramo(tramos, "ric", REF.REGLAS_R2)
                    if m["clase"] != "anafora_sin_numero" and not REF.es_autocita_de_encabezado(m, u)]
        mb, mn = menciones(vb), menciones(vn)
    finally:
        REF.TITULOS_TOS = titulos_previos

    def clave(m):
        return (m["clase"], m["to_destino"], tuple(m["puntos"]), tuple(m["secciones"]), m["evidencia"])
    perdidas = [m for m in mb if clave(m) not in {clave(x) for x in mn}]
    kg = leer(K.RAIZ / K.GRAFOS["diez"]["dir"] / "kg.json")
    nodos = [n for n in kg["nodes"] if any(p.get("chunk_id") == cid for p in n.get("provenances", []))
             and n["type"] in REF.TIPOS_CONTENIDO_R2]
    filas = []
    for m in perdidas:
        unidades = [("punto", p) for p in m["puntos"]] + [("seccion", s) for s in m["secciones"]]
        for tipo, x in unidades:
            nombran = [n["id"] for n in nodos if REF.nombra_unidad(REF._texto_r2(n, True),
                                                                  **({"punto": x} if tipo == "punto" else {"seccion": x}))]
            filas.append({"unidad_citada": x, "clase": m["clase"], "to_destino": m["to_destino"],
                          "tramo": m["evidencia"][:160], "nodos_de_la_unidad_que_la_nombran": nombran})
    return OrderedDict([
        ("chunk_id", cid), ("herencia_antes", sum(len(t["texto"]) for t in vb["herencia"])),
        ("herencia_despues", sum(len(t["texto"]) for t in vn["herencia"])),
        ("herencia_recortada", vn.get("herencia_recortada")),
        ("tramos_despues", [{"tipo": t["tipo"], "unidad_origen": t["unidad_origen"], "caracteres": len(t["texto"]),
                             "inicio": t["texto"][:80]} for t in vn["herencia"]]),
        ("menciones_del_bloque_heredado", {"antes": len(mb), "despues": len(mn)}),
        ("menciones_en_el_texto_omitido", len(perdidas)),
        ("nodos_de_la_unidad_en_r2a", len(nodos)),
        ("citas_que_dejan_de_atribuirse_por_la_regla_i",
         sum(1 for f in filas if f["nodos_de_la_unidad_que_la_nombran"])),
        ("detalle", filas)])


def control_n(nueva: Path) -> OrderedDict:
    tot, filas = Counter(), OrderedDict()
    for to in DIEZ:
        p = leer(nueva / f"pies_{to}.json")
        tot.update(p["estados"])
        tot["paginas"] += p["paginas"]
        filas[to] = {"paginas": p["paginas"], "estados": p["estados"],
                     "version_vigente": (p["version_vigente"] or {}).get("valor"),
                     "caratula": (p["caratula"] or {}).get("ultima_comunicacion_incorporada"),
                     "coincide_con_la_caratula": p["coincide_con_la_caratula"]}
    return OrderedDict([("totales", dict(sorted(tot.items()))),
                        ("coinciden_con_la_caratula", sum(1 for f in filas.values() if f["coincide_con_la_caratula"])),
                        ("no_coinciden", sorted(t for t, f in filas.items() if f["coincide_con_la_caratula"] is False)),
                        ("por_to", filas)])


def control_152(base: Path, nueva: Path) -> OrderedDict:
    tos = sorted(p.stem.split("_", 1)[1] for p in base.glob("chunks_*.json"))
    ids_cambian, ganados, perdidos, recortadas, otros, cambian_por_to = {}, {}, {}, {}, {}, {}
    sobre_u = []
    completo_sobre_u, propio_sobre_u = 0, 0
    partes_recortadas = 0
    for to in tos:
        c = comparar_to(base, nueva, to)
        if c["cambian"]:
            cambian_por_to[to] = len(c["cambian"])
        if c["ids_nuevos"] or c["ids_que_desaparecen"] or not c["orden_igual_en_comunes"]:
            ids_cambian[to] = {k: c[k] for k in ("ids_nuevos", "ids_que_desaparecen", "orden_igual_en_comunes")}
        if c["renglones_ganados"]:
            ganados[to] = c["renglones_ganados"]
        if c["renglones_perdidos"]:
            perdidos[to] = c["renglones_perdidos"]
        if c["con_herencia_recortada"]:
            recortadas[to] = len(c["con_herencia_recortada"])
        ot = sorted(i for i, ks in c["cambian"].items() if not set(ks) <= CAMPOS_HERENCIA
                    and not ({"texto", "chars_propio", "sha256_propio"} & set(ks)))
        if ot:
            otros[to] = ot
        for ch in chunks(nueva, to):
            if sum(len(t["texto"]) for t in ch.get("herencia") or []) > U:
                sobre_u.append(ch["id"])
            completo_sobre_u += ch["chars_completo"] > U
            propio_sobre_u += ch["chars_propio"] > U
            if "sub_chunk" in ch and ch.get("herencia_recortada"):
                partes_recortadas += 1
    fb = {p.name for p in base.glob("*.json")}
    fn = {p.name for p in nueva.glob("*.json")}
    distintos_otros = sorted(n for n in fb & fn if not n.startswith(("chunks_", "estructura_", "tablas_"))
                             and n not in AGREGADOS and (base / n).read_bytes() != (nueva / n).read_bytes())
    return OrderedDict([
        ("tos", len(tos)), ("tos_con_ids_que_cambian", ids_cambian),
        ("chunks_que_cambian_por_to", cambian_por_to),
        ("renglones_ganados_por_to", {t: len(v) for t, v in ganados.items()}),
        ("renglones_perdidos_por_to", {t: len(v) for t, v in perdidos.items()}),
        ("renglones_ganados", ganados), ("renglones_perdidos", perdidos),
        ("unidades_con_herencia_recortada", {"total": sum(recortadas.values()), "tos": len(recortadas),
                                             "por_to": recortadas}),
        ("partes_con_herencia_recortada", partes_recortadas),
        ("unidades_que_siguen_sobre_U", sobre_u),
        # informativo: el tope de (h) es de la herencia; por tamaño completo (texto propio y herencia) o por texto
        # propio, una unidad puede seguir sobre U
        ("unidades_sobre_U_por_tamano_completo", completo_sobre_u),
        ("unidades_sobre_U_por_texto_propio", propio_sobre_u),
        ("chunks_con_otros_campos_que_cambian", otros),
        ("archivos_nuevos", len(fn - fb)), ("archivos_que_faltan", sorted(fb - fn)),
        ("otros_archivos_distintos", distintos_otros)])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--nueva", type=Path, required=True)
    ap.add_argument("--doble", type=Path, required=True)
    ap.add_argument("--base", type=Path, default=K.RAIZ / K.E0_R2)
    ap.add_argument("--p152-base", type=Path, default=None)
    ap.add_argument("--p152-nuevo", type=Path, default=None)
    ap.add_argument("--p152-regla-general", type=Path, default=None)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    nueva = a.nueva if a.nueva.is_absolute() else K.RAIZ / a.nueva
    base = a.base if a.base.is_absolute() else K.RAIZ / a.base
    out = OrderedDict([("diez", control_diez(base, nueva, a.doble))])
    ric = out["diez"]["por_to"]["ric"]["comparacion"]
    out["l_renglones_recuperados_ric"] = renglones_con_pagina(nueva, "ric", ric["renglones_ganados"])
    out["f"] = control_f(base, nueva)
    out["h"] = control_h(base, nueva)
    out["n"] = control_n(nueva)
    if a.p152_base and a.p152_nuevo:
        out["particion_152"] = control_152(a.p152_base, a.p152_nuevo)
    if a.p152_base and a.p152_regla_general:
        out["particion_152_cola_en_toda_pagina"] = control_152(a.p152_base, a.p152_regla_general)
    K.escribir_json(K.RAIZ / a.out, out)
    d = out["diez"]
    print(json.dumps({"doble": d["doble_corrida"], "otros_9_iguales": d["otros_9_tos_iguales_byte_a_byte"],
                      "ric": d["ric_control"], "agregados": d["agregados_claves_que_cambian"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
