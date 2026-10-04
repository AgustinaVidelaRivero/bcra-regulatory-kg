"""U-R2-CODIGO-2, C2 — controles de la cadena r2 sobre el crudo de r2a (USD 0, sin API ni Neo4j). Solo escribe --out
y, con --volcar, los archivos que la cadena escribiría (en un directorio fuera del repo).

Corridas, en memoria, por grafo (KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a), con el código de C2:
  r2a      la cadena con la fase r2a, la de los grafos sellados: reproduce el grafo salvo los cambios declarados de
           los puntos que rigen en las dos fases (a, c, d, e, i, j, k); los de (m) a (t) no actúan;
  r2b      el mismo crudo con las reglas de r2b (`correr_cadena_r2(fase="r2b")`): suma la separación de las
           operaciones por punto y las propiedades no definidas en la arista (P3b de U-PROMPT-R2) y los puntos
           (m) a (s) de C2;
  r2b_sin_p3b  como r2b, con e2_lib.ensamblar_r2 en la fase r2a: aísla los puntos de C2 de los de P3b.
La E0 de las tres es la de los grafos r2a (`salida_tanda0_r2/`, f8dedd4); para el punto (n), los `pies_<to>.json`
de la E0 nueva (`--pies`), copiados a un directorio temporal junto a esa E0: así ningún cambio de E0 (f, h, l)
entra en estas corridas.

Salidas, por grafo: el sha256 de cada corrida; la diferencia r2a sellado → r2a, por regla (aristas `remite_a` del
punto a, elementos de umbral de c, i, j y k y de la enmienda 5 a L-ESQ-R2, registro de remisiones, contador de d,
clave de e); r2b_sin_p3b → r2b (P3b, aparte); r2a → r2b_sin_p3b (los puntos m a s); y los casos de control
(cla::5.1.1.1, las filas de M3.b).

Las dos correcciones de la revisión del freno (enmienda 5, puntos 1.d y 3.b) se miden con dos corridas r2a más, cada
una con la corrección quitada en memoria (`SIN_O_NO`, `SIN_MAS_MENOS_DEL`): los elementos que cambian entre esa
corrida y la r2a son los de la corrección. Lo mismo sobre el texto propio de las unidades de la E0 nueva (`--pies`):
las cuantías cuya comparación cambia (`cuantias_en_texto`).

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c2_cadena.py \
      --pies <salida nueva de e0-r2> --out data/experiment/r2_codigo2/salidas/c2_cadena.json
"""
from __future__ import annotations

import argparse
import json
import re
import shutil
import tempfile
from collections import Counter, OrderedDict
from pathlib import Path

import c1_comun as K

ENS, REF = K.ENS, K.REF
ENS.E4.modulo_modelos_r2()            # pone pyd_r2/code en el path
import reglas_comparacion as RCMP     # noqa: E402
E2 = ENS.e2_lib
TIPOS_UMBRAL = ("Restriccion", "Obligacion", "Condicion", "Excepcion")
ESTRATO = ("cap", "cla", "ctacte", "docvig", "ext", "lingob", "pagjub", "polcre", "pro", "ric")


# Las dos correcciones de la revisión del freno, quitadas en memoria (para medirlas).
SIN_O_NO = [(RCMP, "_no_de_o_no", lambda toks, j: False)]
SIN_MAS_MENOS_DEL = [(RCMP, "SIMPLES", tuple(
    (sentido, forma, re.compile(r"\bmas\s+de\b") if forma == "mas_de" else
     re.compile(r"\bmenos\s+de\b") if forma == "menos_de" else pat) for sentido, forma, pat in RCMP.SIMPLES))]
O_NO, MAS_MENOS_DEL = "i: «o no» (enmienda 5, 1.d)", "«más del» y «menos del» (enmienda 5, 3.b)"


def correr(nombre: str, fase: str, e0_dir: Path, sin_p3b: bool = False, parches_extra: list | None = None) -> dict:
    """Cadena r2 del grafo `nombre` en memoria con la `fase` dada; captura lo que escribiría con w y wl."""
    cfg = K.GRAFOS[nombre]
    man = ENS.MC.cargar(K.RAIZ / cfg["manifiesto"])
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = ENS.E4.modulo_modelos_r2()
    cat = ENS.E4.catalogo_r2()
    escritos: dict = {}

    def w(n: str, obj) -> None:
        escritos[n] = json.loads(json.dumps(obj, ensure_ascii=False))

    def wl(n: str, filas: list) -> None:
        escritos[n] = json.loads(json.dumps(filas, ensure_ascii=False))

    parches = []
    if sin_p3b:
        orig = E2.ensamblar_r2

        def ensamblar_r2_fase_r2a(*a, **kw):
            kw["fase"] = "r2a"
            return orig(*a, **kw)
        parches.append((E2, "ensamblar_r2", ensamblar_r2_fase_r2a))
    parches += parches_extra or []
    with tempfile.TemporaryDirectory() as tmp:
        plan = ENS.plan_redirecciones_r2(man, perfil, K.RAIZ / K.ENTRADA, Path(tmp) / "r2", cat, M)
        with ENS.redirigido(plan), K.parcheado(parches):
            res = ENS.correr_cadena_r2(man, perfil, w, wl, e0_dir, fase=fase)
    return {"kg": res["kg"], "sha256": res["sha256"], "resumen": res["resumen"], "escritos": escritos,
            "kg_json": res["kg_json"]}


def _umbrales(kg: dict) -> dict:
    return {n["id"]: n for n in kg["nodes"] if n["type"] in TIPOS_UMBRAL}


CAMPOS = ("tramo", "valor", "unidad", "dias_tipo", "comparacion", "regla_comparacion", "comparacion_asumida",
          "origen", "base", "base_destino", "base_via", "base_no_resuelta")


def reglas_del_elemento(antes: dict | None, despues: dict | None, clave: tuple, conjuntos: dict) -> list[str]:
    """Reglas que explican el cambio de un elemento de umbral, por sus campos y por las corridas sin cada corrección
    (`conjuntos`: regla → claves (nodo, valor, unidad, origen) de los elementos que esa corrección cambia). Un
    elemento puede tener más de una (p. ej., deja `coeficiente` por el comparador pegado y el comparador es «más
    del»)."""
    if antes is None or despues is None:
        x = despues or antes
        t = RCMP_plegar(x.get("tramo") or "")
        if re.search(r"\bhs\b|\bhrs?\b", t):
            return ["c: «hs.»"]
        if re.search(r"\bo\s+mas\b", t):
            return ["c: «o más» entre el paréntesis y la unidad"]
        if re.match(r"^(?:\d+\s*[°º]|[a-z]+)\s", t) and not re.match(r"^\d", t):
            return ["c: ordinal con marcador"]
        return ["c: otra"]
    ra, rb = antes.get("regla_comparacion") or "", despues.get("regla_comparacion") or ""
    de_correccion = [r for r, cl in conjuntos.items() if clave in cl]
    out = []
    if (antes.get("tramo"), antes.get("dias_tipo")) != (despues.get("tramo"), despues.get("dias_tipo")):
        out.append("c: «hábil»/«corrido» en singular")
    if rb.startswith("encabezado:"):
        out.append("k: marcador del encabezado")
    if ra == "coeficiente" and rb != "coeficiente":
        out.append("j: comparador pegado (enmienda 5, 2)")
    out += de_correccion
    # la negación nueva: el mismo comparador, antes leído sin negar (una cuantía que deja `coeficiente` con una
    # negación cercana es del comparador pegado)
    if rb.startswith("negacion:") and ra.startswith("simple:") and not de_correccion:
        out.append("i: negación (enmienda 5, 1.a a 1.c)")
    if rb.startswith("compuesta:igual_o_") and ra.startswith("simple:"):
        out.append("i: «igual o superior» (enmienda 5, 3.a)")
    if ra == "sin_marcador_plazo" and rb == "sin_marcador_plazo":
        out.append("m: plazo sin marcador")
    if (antes.get("base_destino"), antes.get("base_via"), antes.get("base_no_resuelta")) != \
            (despues.get("base_destino"), despues.get("base_via"), despues.get("base_no_resuelta")):
        out.append("r: base con el detector de remite_a")
    return out or ["otra"]


def RCMP_plegar(t: str) -> str:
    import reglas_comparacion as RCMP   # noqa: PLC0415 — pyd_r2/code, en el path por la cadena
    return RCMP.plegar(t)


def diferencia_umbrales(kg_a: dict, kg_b: dict, conjuntos: dict | None = None) -> dict:
    """Elementos de umbral que cambian entre dos grafos, por nodo, con las reglas que lo explican; y los nodos cuya
    `frecuencia` cambia (plazo heredado que deja de ir a frecuencia)."""
    conjuntos = conjuntos or {}
    na, nb = _umbrales(kg_a), _umbrales(kg_b)
    filas, por_regla = [], Counter()
    for i in sorted(set(na) | set(nb)):
        a, b = na.get(i), nb.get(i)
        if a is None or b is None:
            continue
        ua, ub = a["properties"].get("umbrales") or [], b["properties"].get("umbrales") or []
        fa, fb = a["properties"].get("frecuencia"), b["properties"].get("frecuencia")
        if ua == ub and fa == fb:
            continue
        ca = Counter(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in ua)
        cb = Counter(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in ub)
        solo_a = [json.loads(x) for x in sorted((ca - cb).elements())]
        solo_b = [json.loads(x) for x in sorted((cb - ca).elements())]
        pares = []
        for x in list(solo_b):
            y = next((z for z in solo_a if (z.get("valor"), z.get("unidad"), z.get("origen"))
                      == (x.get("valor"), x.get("unidad"), x.get("origen"))), None)
            if y is not None:
                solo_a.remove(y)
                solo_b.remove(x)
                pares.append((y, x))
        def cl(x):
            return (i, x.get("valor"), x.get("unidad"), x.get("origen"))
        cambios = ([{"reglas": reglas_del_elemento(y, x, cl(x), conjuntos),
                     "antes": {k: y.get(k) for k in CAMPOS if y.get(k) != x.get(k)},
                     "despues": {k: x.get(k) for k in CAMPOS if y.get(k) != x.get(k)},
                     "valor": x.get("valor"), "unidad": x.get("unidad"), "tramo": x.get("tramo")} for y, x in pares]
                   + [{"reglas": reglas_del_elemento(None, x, cl(x), conjuntos),
                       "agregado": {k: x.get(k) for k in CAMPOS}} for x in solo_b]
                   + [{"reglas": reglas_del_elemento(y, None, cl(y), conjuntos),
                       "quitado": {k: y.get(k) for k in CAMPOS}} for y in solo_a])
        if fa != fb:
            cambios.append({"reglas": ["c: el plazo heredado deja de ir a frecuencia" if fb is None else "otra"],
                            "frecuencia": {"antes": fa, "despues": fb}})
        por_regla.update(r for c in cambios for r in c["reglas"])
        filas.append(OrderedDict([("nodo", i), ("chunk_id", b["provenance"].get("chunk_id")), ("cambios", cambios)]))
    return {"nodos": len(filas), "elementos": sum(len(f["cambios"]) for f in filas),
            "elementos_por_regla": dict(sorted(por_regla.items())), "detalle": filas}


def claves_que_cambian(kg_a: dict, kg_b: dict) -> set:
    """Claves (nodo, valor, unidad, origen) de los elementos de umbral que cambian entre dos grafos."""
    na, nb = _umbrales(kg_a), _umbrales(kg_b)
    out = set()
    for i in set(na) & set(nb):
        ca = Counter(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in na[i]["properties"].get("umbrales") or [])
        cb = Counter(json.dumps(x, sort_keys=True, ensure_ascii=False) for x in nb[i]["properties"].get("umbrales") or [])
        for x in list((ca - cb).elements()) + list((cb - ca).elements()):
            x = json.loads(x)
            out.add((i, x.get("valor"), x.get("unidad"), x.get("origen")))
    return out


def correccion(kg_sin: dict, kg_con: dict) -> dict:
    """Elementos que cambia una corrección: de la corrida sin ella a la r2a."""
    d = diferencia_umbrales(kg_sin, kg_con)
    return {"nodos": d["nodos"], "elementos": d["elementos"], "detalle": [
        {"nodo": f["nodo"], "chunk_id": f["chunk_id"], "cambios": [{k: v for k, v in c.items() if k != "reglas"}
                                                                   for c in f["cambios"]]} for f in d["detalle"]]}


def cuantias_en_texto(e0_dir: Path) -> dict:
    """Las dos correcciones sobre el texto propio de cada unidad de la E0 (`reglas_comparacion.analizar` sobre el
    texto, como un tramo): las cuantías cuya comparación cambia al quitar cada corrección."""
    chunks = [c for p in sorted(Path(e0_dir).glob("chunks_*.json")) for c in json.loads(p.read_text(encoding="utf-8"))]
    out = OrderedDict([("unidades", len(chunks))])
    for nombre, parches in (("o_no", SIN_O_NO), ("mas_menos_del", SIN_MAS_MENOS_DEL)):
        filas = []
        for c in chunks:
            t = c.get("texto") or ""
            con = RCMP.analizar(t)
            with K.parcheado(parches):
                sin = RCMP.analizar(t)
            vs = {(x.inicio, x.texto): x for x in sin}
            for x in con:
                y = vs.get((x.inicio, x.texto))
                if y is None or (y.comparacion, y.regla) != (x.comparacion, x.regla):
                    filas.append({"chunk_id": c["id"], "cuantia": x.texto,
                                  "sin_la_correccion": None if y is None else [y.comparacion, y.regla],
                                  "con_la_correccion": [x.comparacion, x.regla], "marcador": x.marcador})
        out[nombre] = {"cuantias": len(filas), "unidades": sorted({f["chunk_id"] for f in filas}), "filas": filas}
    return out


def resumen_umbrales(kg: dict) -> dict:
    u = [x for n in kg["nodes"] for x in (n["properties"].get("umbrales") or [])]
    return {"elementos": len(u), "comparacion_asumida": sum(bool(x.get("comparacion_asumida")) for x in u),
            "no_determinada": sum(x.get("comparacion") == "no_determinada" for x in u),
            "base_por_via": dict(sorted(Counter(x.get("base_via") or ("no_resuelta" if x.get("base_no_resuelta")
                                                                      else "sin_base")
                                                for x in u).items()))}


def diferencia_grafo(kg_a: dict, kg_b: dict) -> dict:
    """Nodos y aristas que cambian entre dos grafos: por tipo y por relación, y las aristas por (s, r, t)."""
    na, nb = {n["id"]: n for n in kg_a["nodes"]}, {n["id"]: n for n in kg_b["nodes"]}
    ea = {K.tripla(e): e for e in kg_a["edges"]}
    eb = {K.tripla(e): e for e in kg_b["edges"]}
    cambian_n = [i for i in sorted(set(na) & set(nb)) if na[i] != nb[i]]
    cambian_e = [k for k in sorted(set(ea) & set(eb)) if ea[k] != eb[k]]
    def por(it):
        return dict(sorted(Counter(it).items()))
    return OrderedDict([
        ("nodos", (len(na), len(nb))), ("aristas", (len(ea), len(eb))),
        ("nodos_quitados_por_tipo", por(na[i]["type"] for i in set(na) - set(nb))),
        ("nodos_agregados_por_tipo", por(nb[i]["type"] for i in set(nb) - set(na))),
        ("nodos_que_cambian_por_tipo", por(nb[i]["type"] for i in cambian_n)),
        ("aristas_quitadas_por_relacion", por(k[1] for k in set(ea) - set(eb))),
        ("aristas_agregadas_por_relacion", por(k[1] for k in set(eb) - set(ea))),
        ("aristas_que_cambian_por_relacion", por(k[1] for k in cambian_e)),
        ("_ids", {"nodos_quitados": sorted(set(na) - set(nb)), "nodos_agregados": sorted(set(nb) - set(na)),
                  "nodos_que_cambian": cambian_n,
                  "aristas_quitadas": sorted(set(ea) - set(eb)), "aristas_agregadas": sorted(set(eb) - set(ea)),
                  "aristas_que_cambian": cambian_e})])


def _campos_que_cambian(a: dict, b: dict) -> list[str]:
    out = []
    for k in sorted(set(a) | set(b)):
        if a.get(k) == b.get(k):
            continue
        if k == "properties":
            out += [f"properties.{x}" for x in sorted(set(a[k]) | set(b[k])) if a[k].get(x) != b[k].get(x)]
        else:
            out.append(k)
    return out


def remite_a(kg_a: dict, kg_b: dict) -> dict:
    d = K.diferencia_aristas(kg_a, kg_b, "remite_a")

    def fila(e):
        return OrderedDict([("source", e["source"]), ("target", e["target"]),
                            ("destino", e["properties"].get("destino")), ("alcance", e["properties"].get("alcance")),
                            ("chunk_id", e["provenance"].get("chunk_id")), ("tramo", e["properties"].get("evidencia"))])
    return {"quitadas": [fila(e) for e in d["quitadas"]], "agregadas": [fila(e) for e in d["agregadas"]]}


def registro(r: dict) -> dict:
    reg = r["escritos"].get("remisiones_registro.json") or []
    return {"filas": len(reg), "por_clase": dict(sorted(Counter(c["clase"] for c in reg).items())),
            "norma_tras_el_numero": dict(sorted(Counter(c.get("norma_tras_el_numero") for c in reg
                                                        if c.get("norma_tras_el_numero")).items())),
            "autorreferencias_desde_texto_heredado": sum(
                1 for c in reg if c.get("atribucion") == "texto_heredado"
                and any(x["causa"] == "autorreferencia al punto propio" for x in c["irresolubles"]))}


def control_base_cla(kg: dict) -> list:
    n = [x for x in kg["nodes"] if any(p.get("chunk_id") == "cla::5.1.1.1" for p in x.get("provenances", []))]
    return [{"nodo": x["id"], "base": u.get("base"), "base_destino": u.get("base_destino"), "base_via": u.get("base_via")}
            for x in n for u in (x["properties"].get("umbrales") or []) if u.get("base")]


def filas_m3b_detector(r: dict) -> list[OrderedDict]:
    """Punto a, fila por fila: las 18 filas «detector» de M3.b (c1a_detector.filas_m3b, FILAS_PATRON) en el registro
    de remisiones de la corrida: la cita del chunk de origen al punto citado, su clase, su destino y su causa."""
    import c1a_detector as C1A          # noqa: PLC0415 — en esta carpeta
    reg = r["escritos"].get("remisiones_registro.json") or []
    out = []
    for f in C1A.filas_m3b():
        if f["veredicto"] != "detector":
            continue
        patron = next(p for p, fs in C1A.FILAS_PATRON.items() if f["id_lectura"] in fs)
        punto = f["destino_citado"].split("::", 1)[1]
        citas = [c for c in reg if c.get("chunk_id") == f["chunk_origen"] and punto in c["puntos"]]
        out.append(OrderedDict([
            ("id_lectura", f["id_lectura"]), ("patron", patron), ("chunk_origen", f["chunk_origen"]),
            ("destino_citado", f["destino_citado"]),
            ("citas", [OrderedDict([("clase", c["clase"]), ("norma_nombrada", c["norma_nombrada"]),
                                    ("to_destino", c["to_destino"]), ("norma_tras_el_numero",
                                                                      c.get("norma_tras_el_numero")),
                                    ("destinos", [d["destino"] for d in c["destinos"]]),
                                    ("irresolubles", [x["causa"] for x in c["irresolubles"]])]) for c in citas])]))
    return out


def control_filas_m3b(filas: list[dict]) -> dict:
    """Lo que el mandato pide de cada patrón (C2, a)."""
    def ok(f):
        cs = f["citas"]
        internas = [c for c in cs if c["clase"] == "interna"]
        if f["patron"] == "1":
            # ninguna cita del chunk a ese punto queda interna; la de la fila es externa
            return not internas and any(c["clase"] == "externa" for c in cs)
        if f["patron"] == "2":
            return not internas and any(c["clase"] == "comunicacion_anexo"
                                        and c["irresolubles"] == [REF.CAUSA_ANEXO_COMUNICACION] for c in cs)
        # patrón 3: la cita de la fila sigue interna e irresoluble (punto inexistente en E0)
        return any(c["irresolubles"] == ["punto inexistente en E0"] for c in internas)
    return {p: {"filas": sum(1 for f in filas if f["patron"] == p), "cumplen": sum(1 for f in filas
                                                                                 if f["patron"] == p and ok(f))}
            for p in ("1", "2", "3")}


def base_cap_6_11(kg: dict) -> list:
    """Punto c: la base del 25 % de cap::6.11 (el ordinal «segundo mes» no la corta)."""
    return [{"nodo": n["id"], "tramo": u.get("tramo"), "base": u.get("base")} for n in kg["nodes"]
            if any(p.get("chunk_id") == "cap::6.11" for p in n.get("provenances", []))
            for u in (n["properties"].get("umbrales") or []) if u.get("valor") == "25"]


def medir(nombre: str, e0_dir: Path, volcar: Path | None) -> OrderedDict:
    sellado = json.loads((K.RAIZ / K.GRAFOS[nombre]["dir"] / "kg.json").read_text(encoding="utf-8"))
    rep_sellado = json.loads((K.RAIZ / K.GRAFOS[nombre]["dir"] / "reporte_ensamblado_r2.json")
                             .read_text(encoding="utf-8"))
    a = correr(nombre, "r2a", e0_dir)
    a_sin_o_no = correr(nombre, "r2a", e0_dir, parches_extra=SIN_O_NO)
    a_sin_del = correr(nombre, "r2a", e0_dir, parches_extra=SIN_MAS_MENOS_DEL)
    conjuntos = {O_NO: claves_que_cambian(a_sin_o_no["kg"], a["kg"]),
                 MAS_MENOS_DEL: claves_que_cambian(a_sin_del["kg"], a["kg"])}
    b = correr(nombre, "r2b", e0_dir)
    bs = correr(nombre, "r2b", e0_dir, sin_p3b=True)
    if volcar is not None:
        for etiqueta, r in (("r2a", a), ("r2b", b), ("r2b_sin_p3b", bs)):
            d = volcar / nombre / etiqueta
            d.mkdir(parents=True, exist_ok=True)
            (d / "kg.json").write_text(r["kg_json"], encoding="utf-8")
            (d / "resumen.json").write_text(json.dumps(r["resumen"], ensure_ascii=False, indent=1), encoding="utf-8")
            for k, v in r["escritos"].items():
                p = d / k
                p.parent.mkdir(parents=True, exist_ok=True)
                if k.endswith(".jsonl"):
                    p.write_text("".join(json.dumps(x, ensure_ascii=False) + "\n" for x in v), encoding="utf-8")
                else:
                    p.write_text(json.dumps(v, ensure_ascii=False, indent=1), encoding="utf-8")
    th_s = rep_sellado["remite_a"]["texto_heredado"]
    th_a = a["resumen"]["remite_a"]["texto_heredado"]
    dif_a = diferencia_grafo(sellado, a["kg"])
    n_otros = [i for i in dif_a["_ids"]["nodos_que_cambian"]
               if {f for f in _campos_que_cambian({n["id"]: n for n in sellado["nodes"]}[i],
                                                  {n["id"]: n for n in a["kg"]["nodes"]}[i])}
               - {"properties.umbrales", "properties.frecuencia", "originales", "fuera_de_lista"}]
    ops_s = sum(1 for n in sellado["nodes"] if n["type"] == "Operacion")
    out = OrderedDict([
        ("sha256", {"sellado": K.GRAFOS[nombre]["sha256"], "r2a": a["sha256"], "r2b": b["sha256"],
                    "r2b_sin_p3b": bs["sha256"]}),
        ("r2a_frente_al_sellado", OrderedDict([
            ("grafo", {k: v for k, v in dif_a.items() if k != "_ids"}),
            ("nodos_que_cambian_fuera_de_los_umbrales", n_otros),
            ("a_remite_a", remite_a(sellado, a["kg"])),
            ("a_registro", {"sellado": None, "r2a": registro(a)}),
            ("a_filas_m3b_detector", filas_m3b_detector(a) if nombre == "diez" else None),
            ("a_comunicaciones_citas_a_puntos_de_anexo",
             a["escritos"]["comunicaciones_registro.json"].get("citas_a_puntos_de_anexo")),
            ("a_remite_a_resumen", {k: (rep_sellado["remite_a"].get(k), a["resumen"]["remite_a"].get(k))
                                    for k in ("citas_resueltas", "citas_irresolubles", "aristas", "reglas")}),
            ("a_irresolubles_por_causa", {"sellado": rep_sellado["remite_a"]["irresolubles_por_causa"],
                                          "r2a": a["resumen"]["remite_a"]["irresolubles_por_causa"]}),
            ("d_texto_heredado", {"sellado": th_s, "r2a": th_a}),
            ("e_pasada_residual", a["resumen"]["e4"]["pasada_residual_de_propuestos_medida_no_aplicada"]),
            ("e_escribe_e4_pasada_residual_medida", "e4_pasada_residual_medida.json" in a["escritos"]),
            ("umbrales", diferencia_umbrales(sellado, a["kg"], conjuntos)),
            ("correcciones_de_la_revision", OrderedDict([
                ("o_no", correccion(a_sin_o_no["kg"], a["kg"])),
                ("mas_menos_del", correccion(a_sin_del["kg"], a["kg"]))])),
            ("c_base_25_cap_6_11", {"sellado": base_cap_6_11(sellado), "r2a": base_cap_6_11(a["kg"])}),
            ("umbrales_resumen", {"sellado": resumen_umbrales(sellado), "r2a": resumen_umbrales(a["kg"])}),
            ("reporte_umbrales", {"sellado": rep_sellado["umbrales"], "r2a": a["resumen"]["umbrales"]})])),
        ("p3b_r2b_sin_p3b_frente_a_r2b", OrderedDict([
            ("grafo", {k: v for k, v in diferencia_grafo(bs["kg"], b["kg"]).items() if k != "_ids"}),
            ("operaciones", {"sellado": ops_s, "r2a": sum(1 for n in a["kg"]["nodes"] if n["type"] == "Operacion"),
                             "r2b": sum(1 for n in b["kg"]["nodes"] if n["type"] == "Operacion")})])),
        ("c2_r2a_frente_a_r2b_sin_p3b", OrderedDict([
            ("grafo", {k: v for k, v in diferencia_grafo(a["kg"], bs["kg"]).items() if k != "_ids"}),
            ("umbrales", diferencia_umbrales(a["kg"], bs["kg"])),
            ("umbrales_resumen", resumen_umbrales(bs["kg"])),
            ("reporte_umbrales", bs["resumen"]["umbrales"]),
            ("n_texto_ordenado", bs["resumen"].get("texto_ordenado_version_materia")),
            ("p_omisiones", bs["resumen"].get("omisiones")),
            ("q_aristas_derivadas", bs["resumen"].get("aristas_derivadas_que_tocan_un_nodo_solo_de_la_cola")),
            ("s_paso_por_e3", bs["resumen"].get("paso_por_e3")),
            ("r_control_cla_5_1_1_1", {"r2a": control_base_cla(a["kg"]), "r2b": control_base_cla(bs["kg"])}),
            ("nodos_que_cambian_fuera_de_umbrales_y_texto_ordenado", [
                i for i in diferencia_grafo(a["kg"], bs["kg"])["_ids"]["nodos_que_cambian"]
                if not i.startswith("TextoOrdenado_")
                and {f for f in _campos_que_cambian({n["id"]: n for n in a["kg"]["nodes"]}[i],
                                                    {n["id"]: n for n in bs["kg"]["nodes"]}[i])}
                - {"properties.umbrales", "properties.frecuencia", "originales", "fuera_de_lista"}])])),
        ("r2b_reporte_igual_al_r2b_sin_p3b_salvo_e2", sorted(
            k for k in set(b["resumen"]) | set(bs["resumen"]) if b["resumen"].get(k) != bs["resumen"].get(k)))])
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--pies", type=Path, required=True, help="salida nueva de e0-r2 (pies_<to>.json)")
    ap.add_argument("--out", required=True)
    ap.add_argument("--volcar", type=Path, default=None, help="directorio fuera del repo para los archivos")
    a = ap.parse_args()
    if a.volcar is not None and a.volcar.resolve().is_relative_to(K.RAIZ.resolve()):
        raise SystemExit("--volcar dentro del repo")
    with tempfile.TemporaryDirectory() as tmp:
        e0 = Path(tmp) / "e0_r2_con_pies"
        shutil.copytree(K.RAIZ / K.E0_R2, e0)
        for to in ESTRATO:
            shutil.copy2(a.pies / f"pies_{to}.json", e0 / f"pies_{to}.json")
        out = OrderedDict([("e0", {"textos_y_tablas": K.E0_R2, "pies": "salida nueva de e0-r2 (pies_<to>.json)"})])
        for nombre in K.GRAFOS:
            out[nombre] = medir(nombre, e0, a.volcar)
        out["diez"]["r2a_frente_al_sellado"]["a_control_filas_m3b"] = control_filas_m3b(
            out["diez"]["r2a_frente_al_sellado"]["a_filas_m3b_detector"])
    out["cuantias_en_texto"] = cuantias_en_texto(a.pies)
    K.escribir_json(K.RAIZ / a.out, out)
    for nombre in K.GRAFOS:
        x = out[nombre]
        print(nombre, json.dumps(x["sha256"]), json.dumps(x["r2a_frente_al_sellado"]["umbrales"]["elementos_por_regla"],
                                                          ensure_ascii=False))


if __name__ == "__main__":
    main()
