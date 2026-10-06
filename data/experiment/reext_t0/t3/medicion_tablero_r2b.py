"""U-REEXT-T0, T3, punto 2 — mediciones de la columna «Después de r2: r2b (prompt y re-extracción)» del tablero de
correcciones (docs/tablero_correcciones.md, filas :49 a :74) sobre KG-Tanda0-Diez-r2b y KG-Tanda0-Desarrollo-r2b.
Copia de data/experiment/medicion_r2a/m2_medicion.py (U-MED-R2A, M2) con las mismas reglas: cambian los grafos (r2b),
la E0 (salida_tanda0_r2b, la de los grafos), las entradas de la suite y de M10 (las del gate de T3, en ens_<x>_r2b/), y
se suman las dos filas que en r2a eran de r2b (f68, omisiones con registro; f69, crudo del reintento de E3), medidas
sobre la salida de la corrida. Cada medición conserva su control sobre los grafos sellados de la tanda 0.

Texto de M2, que sigue valiendo:

Solo lectura, USD 0: ninguna llamada a la API, Neo4j no se usa, no se re-extrae nada. Importa, sin editarlos, los
módulos de los que salen las reglas que se reaplican: R-CITA y R-PRES de D2 (reports/u_pre_r2/upre_d2_ausencias.py) y las reglas de cuantía de U-PYD
(data/experiment/pyd_r2/code/reglas_comparacion.py y modelos_r2.py). Escribe solo --out.

Lee además las salidas de las otras corridas de M2, que se producen antes con sus propios comandos (comandos [c25] y
siguientes del tablero; data/experiment/medicion_r2a/m2_freno.md):
  - la suite del perfil r2 sobre los dos grafos, con la fixture sellada (m2/suite_<grafo>.json);
  - M10 de scripts/metricas_intrinsecas.py --gen3 (m2/intrinsecas/<grafo>.json);
  - r1k_encabezados_descartados.py sobre la e0-r2 de la tanda 0 (m2/r1k_encabezados_descartados_e0r2.json).

Cada medición lleva un control que reproduce, sobre el grafo sellado de la tanda 0, la cifra de la columna «Valor en
la tanda 0» del tablero con la misma regla («control_sellado»). Todas las rutas del JSON son relativas al repo.

Uso, desde la raíz del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/medicion_r2a/m2_medicion.py \
      --out data/experiment/medicion_r2a/m2/m2_medicion.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import unicodedata
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[4]   # data/experiment/reext_t0/t3/
for _p in (RAIZ / "data" / "experiment" / "pyd_r2" / "code", RAIZ / "reports" / "u_pre_r2"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))
import modelos_r2 as M                # noqa: E402  UNIDADES_TEMPORALES (sin editar)
import reglas_comparacion as RCMP     # noqa: E402  detectar_cuantias (sin editar)
import upre_d2_ausencias as D2        # noqa: E402  R-CITA y R-PRES (sin editar)

REX = "data/experiment/reextraccion_v2"
T0 = f"{REX}/corpus_tanda0"
M2 = "data/experiment/medicion_r2a/m2"
GRAFOS = OrderedDict([
    ("diez", {"kg": f"{T0}/ens_diez_r2b/r2/kg.json", "reporte": f"{T0}/ens_diez_r2b/r2/reporte_ensamblado_r2.json",
              "sellado": f"{T0}/ens_diez/r1/kg.json", "reporte_sellado": f"{T0}/ens_diez/r1/reporte_ensamblado_r1.json",
              "manifiesto": f"{REX}/manifiestos/tanda0_ens_diez_r2b.json", "nombre": "KG-Tanda0-Diez-r2b"}),
    ("desarrollo", {"kg": f"{T0}/ens_desarrollo_r2b/r2/kg.json",
                    "reporte": f"{T0}/ens_desarrollo_r2b/r2/reporte_ensamblado_r2.json",
                    "sellado": f"{T0}/ens_desarrollo/r1/kg.json",
                    "reporte_sellado": f"{T0}/ens_desarrollo/r1/reporte_ensamblado_r1.json",
                    "manifiesto": f"{REX}/manifiestos/tanda0_ens_desarrollo_r2b.json",
                    "nombre": "KG-Tanda0-Desarrollo-r2b"}),
])
E0_LEGADA = f"{REX}/e0_chunking/salida_tanda0"
E0_R2 = f"{REX}/e0_chunking/salida_tanda0_r2b"   # la E0 de los grafos r2b
SALIDA_R2B = f"{T0}/salida_r2b"
FIXTURE = "scripts/regression_kg_esperado.json"
ENUMS = "data/experiment/pyd_r2/generados/enums_r2.json"
CATALOGO_R2 = "data/experiment/catalogo_unico/catalogo_sujetos_r2.json"
BLOQUE_R2 = "data/experiment/catalogo_unico/generados_r2/bloque_catalogo_r2.txt"
D2_JSON = "reports/u_pre_r2/d2_ausencias.json"
TIPOS_CONTENIDO = ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad", "Condicion", "Definicion")
CLAVES_PIPELINE = ("cola_humana", "cola_chunks", "estado_e3", "colision_cross_to", "materia_variantes",
                   "version_variantes")
# [c11]: listas y claves del prefijo congelado, tal como las define el tablero (control sobre los sellados)
C11_LISTAS = {("Restriccion", "tipo"): ("prohibicion", "limite_cuantitativo", "limite_cualitativo"),
              ("Comunicacion", "tipo"): ("A", "B", "C"),
              ("Obligacion", "tipo"): ("presentacion_informativa", "calculo", "asignacion", "comunicacion_a_cliente",
                                       "reporte_al_supervisor", "otra")}
C11_CLAVES = {"Comunicacion": ("codigo", "tipo", "numero"), "TextoOrdenado": ("materia", "archivo", "version"),
              "Operacion": ("tipo", "descripcion"), "Restriccion": ("descripcion", "tipo", "umbral"),
              "Excepcion": ("descripcion",), "Potestad": ("descripcion",), "Condicion": ("descripcion",),
              "Obligacion": ("descripcion", "tipo", "plazo", "frecuencia"), "Definicion": ("termino", "descripcion")}
RE_PIE = re.compile(r"versi[oó]n\s*:.*comunicaci[oó]n", re.I)   # [c22]
# [c14] tal como lo escribe el tablero (docs/tablero_correcciones.md, sección «Comandos»): porcentaje, «veces», plazo
# (número en cifras o en letras de la lista, opcionalmente seguido de una cifra entre paréntesis, y día, mes, año, hora
# o semana; o «días hábiles/corridos») y monto; NFC, sin distinguir mayúsculas. La regex de reports/u_umbral/
# u_umbral_u1.py es la versión anterior declarada en el tablero (sin la cifra entre paréntesis): no se usa.
_LETRAS_C14 = ("un", "una", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce",
               "quince", "veinte", "treinta", "cuarenta", "sesenta", "noventa", "ciento", "cien")
_NUM_C14 = r"(?:\d+|" + "|".join(sorted(_LETRAS_C14, key=len, reverse=True)) + r")"
_UNI_C14 = r"(?:d[ií]as?|mes(?:es)?|a[ñn]os?|horas?|semanas?)"
C14 = (re.compile(r"\d+(?:[.,]\d+)?\s*%|por\s+ciento", re.I),
       re.compile(r"\bveces\b", re.I),
       re.compile(r"\b" + _NUM_C14 + r"(?:\s*\(\s*\d+\s*\))?\s+" + _UNI_C14 + r"\b|d[ií]as\s+(?:h[aá]biles|corridos)", re.I),
       re.compile(r"(?:US\$|U\$S|USD|\$)\s*\d|\d(?:[\d.,]*)\s*(?:millones\s+de\s+|mil\s+)?(?:pesos|d[oó]lares|USD|UVA)\b",
                  re.I))


def tiene_cuantia(s) -> bool:
    s = unicodedata.normalize("NFC", str(s or ""))
    return any(p.search(s) for p in C14)


# filas de las 16 unidades de U-UMBRAL U1 (medicion_2) y de las dos anclas de D2 (tablero :63)
CHUNKS_TABLAS_4 = ("cap::2.12.2.5", "cap::2.12.2.6", "cap::2.12.2.8", "cap::2.12.3.2")
CHUNKS_TABLAS_12 = ("ric::S2", "ric::4.2", "ric::8.2", "ric::9.2.1", "ric::10.2", "cap::4.2.1.1", "cap::6.2.1.1",
                    "cap::12.1", "cap::12.2", "ext::12.1", "ctacte::13.2", "polcre::1.5")
CHUNKS_ANCLAS_D2 = ("ric::7.2", "ric::9.2", "ric::9.2.1", "ric::9.2.2")


def sha256(p: str) -> str:
    return hashlib.sha256((RAIZ / p).read_bytes()).hexdigest()


def leer(p: str):
    return json.loads((RAIZ / p).read_text(encoding="utf-8"))


def rf(e: dict):
    return e.get("rol_fuente") or (e.get("properties") or {}).get("rol_fuente")


def es_remision(e: dict) -> bool:
    """Las dos formas de la remisión entre puntos (scripts/remisiones.py: remite_a, o referencia con
    rol_fuente referencia_cruzada)."""
    return e["relation"] == "remite_a" or (e["relation"] == "referencia" and rf(e) == "referencia_cruzada")


def anclas(n: dict) -> set:
    return {(p.get("to"), str(p.get("punto") or "")) for p in n.get("provenances") or []}


def en_subarbol(punto: str, ancla: str) -> bool:
    return punto == ancla or punto.startswith(ancla + ".") or punto.startswith(ancla + "::")


def chunks_de(dir_e0: str, tos) -> dict:
    out = OrderedDict()
    for to in tos:
        d = leer(f"{dir_e0}/chunks_{to}.json")
        out[to] = d["chunks"] if isinstance(d, dict) else d
    return out


def tos_de(manifiesto: str) -> list:
    return list(leer(manifiesto)["orden_corrida"])


# --------------------------------------------------------------------------- filas
def obs10(kg: dict, unidades: int, derivadas: tuple) -> dict:
    """[c25]: [c1] con la remisión en sus dos formas, el esqueleto por rol_fuente y las establecida_en derivadas
    por su rol_fuente (DERIVADAS = derivada_de_procedencia, ensamblar_tanda0.derivar_establecida_en)."""
    E = kg["edges"]
    c = Counter()
    for e in E:
        if es_remision(e):
            c["remisiones"] += 1
        elif e["relation"] == "referencia":
            c["referencia_texto_ordenado_comunicacion"] += 1
        elif rf(e) == "esqueleto":
            c["esqueleto"] += 1
        elif e["relation"] == "establecida_en" and rf(e) in derivadas:
            c["establecida_en_derivadas"] += 1
        else:
            c["extraccion"] += 1
            if rf(e) == "cuarentena_flaggeada":
                c["de_ellas_cuarentena_flaggeada"] += 1
            if e.get("no_verificada_e3"):
                c["de_ellas_no_verificadas_e3"] += 1
    ext = c["extraccion"]
    return OrderedDict([("aristas", len(E)), ("conteos", dict(sorted(c.items()))), ("unidades_e0", unidades),
                        ("extraccion", ext), ("por_unidad", round(ext / unidades, 2)),
                        ("estricta_sin_cuarentena_flaggeada", ext - c["de_ellas_cuarentena_flaggeada"]),
                        ("estricta_por_unidad", round((ext - c["de_ellas_cuarentena_flaggeada"]) / unidades, 2)),
                        ("sin_no_verificadas_e3", ext - c["de_ellas_no_verificadas_e3"]),
                        ("sin_no_verificadas_e3_por_unidad", round((ext - c["de_ellas_no_verificadas_e3"]) / unidades, 2))])


def c1_literal(kg: dict) -> int:
    """[c1] tal cual (DERIVADAS vacío), control sobre los sellados."""
    return sum(1 for e in kg["edges"] if e.get("relation") != "referencia" and rf(e) != "esqueleto")


def obs11(kg: dict, reporte: dict) -> dict:
    """[c26]: aristas de remisión cuyo TO de destino difiere del TO de la procedencia de la arista (la definición de
    aristas_cross_to de la cadena r1, r1_referencias.py:339-340), por alcance; menciones del reporte r2."""
    cross = Counter()
    for e in kg["edges"]:
        if e["relation"] != "remite_a":
            continue
        if e["properties"]["destino"].split("::")[0] != e["provenance"]["to"]:
            cross[e["properties"]["alcance"]] += 1
    ra = reporte["remite_a"]
    return OrderedDict([("aristas_cross_to", sum(cross.values())), ("cross_to_por_alcance", dict(sorted(cross.items()))),
                        ("menciones_detectadas", ra["menciones_detectadas"]), ("citas_resueltas", ra["citas_resueltas"]),
                        ("citas_resueltas_por_alcance", ra["citas_resueltas_por_alcance"]),
                        ("aristas_por_alcance", ra["aristas_por_alcance"])])


def remisiones_por_origen(kg: dict) -> dict:
    """[c27]: remisiones por tipo del nodo de origen; las de Condicion, Definicion y Potestad; referencia con origen
    distinto de TextoOrdenado."""
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    c = Counter(tipo[e["source"]] for e in kg["edges"] if es_remision(e))
    return OrderedDict([("por_tipo_de_origen", dict(sorted(c.items()))),
                        ("condicion_definicion_potestad", sum(c[t] for t in ("Condicion", "Definicion", "Potestad"))),
                        ("referencia_con_origen_distinto_de_texto_ordenado", sum(
                            1 for e in kg["edges"] if e["relation"] == "referencia"
                            and tipo[e["source"]] != "TextoOrdenado"))])


def aislados(kg: dict) -> dict:
    """[c3], aislados: nodos sin ninguna arista, por tipo; Condicion aisladas sobre el total de Condicion."""
    con = {e["source"] for e in kg["edges"]} | {e["target"] for e in kg["edges"]}
    por_tipo = Counter(n["type"] for n in kg["nodes"] if n["id"] not in con)
    return OrderedDict([("condicion_aisladas", por_tipo.get("Condicion", 0)),
                        ("condicion_total", sum(1 for n in kg["nodes"] if n["type"] == "Condicion")),
                        ("aislados_total", sum(por_tipo.values())), ("aislados_por_tipo", dict(sorted(por_tipo.items())))])


def falsas_parafrasis(kg: dict) -> dict:
    """[c3], remisiones de nodos con procedencia en cap::8.2.3.3 hacia nodos con procedencia en cap::6.5.1 o
    debajo, y destinos de las remisiones de cap::8.2.3.3."""
    nodos = {n["id"]: n for n in kg["nodes"]}
    origen = {i for i, n in nodos.items() if ("cap", "8.2.3.3") in anclas(n)}
    rem = [e for e in kg["edges"] if es_remision(e) and e["source"] in origen]
    falsas = [e for e in rem if any(t == "cap" and en_subarbol(p, "6.5.1") for t, p in anclas(nodos[e["target"]]))]
    dest = Counter((e.get("properties") or {}).get("destino") for e in rem)
    return OrderedDict([("nodos_de_origen", len(origen)), ("remisiones_desde_cap_8_2_3_3", len(rem)),
                        ("hacia_cap_6_5_1_o_debajo", len(falsas)), ("por_destino", dict(sorted(dest.items())))])


def valores_fuera_de_lista(kg: dict, enums: dict) -> dict:
    """[c28]: [c11] con las listas y las claves del perfil r2 (pyd_r2/generados/enums_r2.json): por campo, valores
    fuera de la lista (vacío = fuera) y cuántos llevan la marca fuera_de_lista; normalizados con original guardado;
    claves de properties fuera de claves_por_tipo (sin las del pipeline) y properties_no_definidas."""
    campos = [("Restriccion", "tipo"), ("Comunicacion", "tipo"), ("Obligacion", "tipo"), ("Obligacion", "frecuencia")]
    out = OrderedDict()
    for t, k in campos:
        lista = set(enums[f"{t}.{k}"])
        fuera, marcados, con_original, distintos, normalizados = 0, 0, 0, set(), 0
        for n in kg["nodes"]:
            if n["type"] != t:
                continue
            p = n.get("properties") or {}
            if k == "frecuencia" and k not in p:
                continue
            v = p.get(k)
            if v in lista:
                if k in (n.get("originales") or {}) and (n.get("originales") or {})[k] != v:
                    normalizados += 1
                continue
            fuera += 1
            distintos.add(str(v))
            marcados += k in (n.get("fuera_de_lista") or [])
            con_original += k in (n.get("originales") or {})
        out[f"{t}.{k}"] = OrderedDict([("fuera_de_lista", fuera), ("valores_distintos", len(distintos)),
                                       ("con_marca_fuera_de_lista", marcados), ("sin_marca", fuera - marcados),
                                       ("con_original_guardado", con_original),
                                       ("sin_marca_ni_original", sum(
                                           1 for n in kg["nodes"] if n["type"] == t
                                           and not (k == "frecuencia" and k not in (n.get("properties") or {}))
                                           and (n.get("properties") or {}).get(k) not in lista
                                           and k not in (n.get("fuera_de_lista") or [])
                                           and k not in (n.get("originales") or {}))),
                                       ("normalizados_con_original_guardado", normalizados)])
    claves = enums["claves_por_tipo"]
    fuera_claves = Counter()
    for n in kg["nodes"]:
        if n["type"] == "Sujeto":
            continue
        for k in (n.get("properties") or {}):
            if k not in claves.get(n["type"], ()) and k not in CLAVES_PIPELINE:
                fuera_claves[f"{n['type']}.{k}"] += 1
    pnd = [n for n in kg["nodes"] if n.get("properties_no_definidas")]
    out["claves_fuera_de_la_definicion"] = OrderedDict([("total", sum(fuera_claves.values())),
                                                        ("por_tipo_y_clave", dict(sorted(fuera_claves.items())))])
    out["properties_no_definidas"] = OrderedDict([
        ("nodos", len(pnd)), ("claves", dict(sorted(Counter(k for n in pnd for k in n["properties_no_definidas"]).items())))])
    return out


def c11_literal(kg: dict) -> dict:
    """[c11] tal cual (control sobre los sellados)."""
    out = OrderedDict()
    for (t, k), lista in C11_LISTAS.items():
        out[f"{t}.{k}"] = sum(1 for n in kg["nodes"] if n["type"] == t and (n.get("properties") or {}).get(k) not in lista)
    out["claves_fuera"] = sum(1 for n in kg["nodes"] if n["type"] != "Sujeto"
                              for k in (n.get("properties") or {})
                              if k not in C11_CLAVES.get(n["type"], ()) and k not in CLAVES_PIPELINE)
    return out


def sujetos(kg: dict, reporte: dict) -> dict:
    """[c31]: [c12] en r2a: aplica_a y ejecuta fuera del esqueleto, con la mención guardada (sujeto_mencion) y
    mencion_verificada; registro de no mapeados y pasada residual de E4 (reporte del ensamblado r2)."""
    rel = [e for e in kg["edges"] if e["relation"] in ("aplica_a", "ejecuta") and rf(e) != "esqueleto"]
    return OrderedDict([
        ("aristas_de_sujeto", len(rel)), ("con_sujeto_mencion", sum(1 for e in rel if e.get("sujeto_mencion"))),
        ("mencion_verificada", dict(sorted(Counter(e.get("mencion_verificada") for e in rel).items()))),
        ("registro_no_mapeados", reporte["registro_no_mapeados"]),
        ("propuestos_en_el_grafo", sum(1 for n in kg["nodes"] if n["type"] == "Sujeto"
                                       and (n.get("properties") or {}).get("nivel") == "propuesto")),
        ("pasada_residual_e4_medida_no_aplicada", reporte["e4"]["pasada_residual_de_propuestos_medida_no_aplicada"])])


def catalogo() -> dict:
    """[c32]: ids del bloque de catálogo generado para el prompt r2 contra ids del catálogo r2 (sin lápidas)."""
    cat = leer(CATALOGO_R2)
    lap = set(leer(ENUMS)["sujeto_lapidas"])
    ids_c = {s["id"] for s in cat["sujetos"]} - lap
    ids_b = set(re.findall(r"^\s*(Sujeto_[a-z0-9_]+) —", (RAIZ / BLOQUE_R2).read_text(encoding="utf-8"), re.M))
    return OrderedDict([("catalogo", CATALOGO_R2), ("catalogo_sha256", sha256(CATALOGO_R2)),
                        ("bloque", BLOQUE_R2), ("bloque_sha256", sha256(BLOQUE_R2)),
                        ("ids_catalogo_sin_lapidas", len(ids_c)), ("lapidas", len(lap)), ("ids_bloque", len(ids_b)),
                        ("solo_en_bloque", sorted(ids_b - ids_c)), ("solo_en_catalogo", sorted(ids_c - ids_b))])


def cuantias(kg: dict, campo: str) -> dict:
    """[c29] (campo = «umbrales»): [c14] en r2a, nodos de los cuatro tipos con cuantía en la descripción (regex de
    [c14], `tiene_cuantia`) y sin elemento en la lista de umbrales, por tipo. Con campo = «heredado»,
    «con campo» es `umbral` o `plazo` en properties o en campos_heredados_v3 ([c14] tal cual en los sellados)."""
    tipos = ("Restriccion", "Condicion", "Obligacion", "Excepcion")
    con, sin, ids_sin = Counter(), Counter(), []
    for n in kg["nodes"]:
        if n["type"] not in tipos:
            continue
        if not tiene_cuantia((n.get("properties") or {}).get("descripcion")):
            continue
        p = n.get("properties") or {}
        if campo == "umbrales":
            tiene = bool(p.get("umbrales"))
        else:
            h = n.get("campos_heredados_v3") or {}
            tiene = any(isinstance(x.get(k), str) and x.get(k).strip() for x in (p, h) for k in ("umbral", "plazo"))
        (con if tiene else sin)[n["type"]] += 1
        if not tiene and campo == "umbrales":
            ids_sin.append(n["id"])
    return OrderedDict([("con_cuantia", sum(con.values()) + sum(sin.values())), ("sin_campo", sum(sin.values())),
                        ("sin_campo_por_tipo", {t: sin.get(t, 0) for t in tipos}),
                        ("con_cuantia_por_tipo", {t: con.get(t, 0) + sin.get(t, 0) for t in tipos})]
                       + ([("ids_sin_campo", sorted(ids_sin))] if campo == "umbrales" else []))


def limites_relativos(kg: dict) -> dict:
    """S18 aparte: Restricciones limite_cuantitativo sin lista de umbrales ni umbral guardado (la marca de S18), y
    cuántas tienen cuantía de [c14] en la descripción."""
    sin = [n for n in kg["nodes"] if n["type"] == "Restriccion"
           and (n.get("properties") or {}).get("tipo") == "limite_cuantitativo"
           and not (n.get("properties") or {}).get("umbrales") and not (n.get("campos_heredados_v3") or {}).get("umbral")]
    return OrderedDict([("restricciones_limite_cuantitativo", sum(
        1 for n in kg["nodes"] if n["type"] == "Restriccion" and (n.get("properties") or {}).get("tipo") == "limite_cuantitativo")),
        ("sin_lista_ni_marca", len(sin)),
        ("de_ellas_con_cuantia_c14", sum(1 for n in sin if tiene_cuantia(n["properties"].get("descripcion"))))])


def cap_1_2(kg: dict) -> dict:
    """[c10] en r2a: Restricciones con procedencia en cap 1.2 y lista de umbrales (valor, unidad, moneda, tramo
    verificado, verificado en tabla); marca de tabla de cap::1.2 en la e0-r2."""
    out = []
    for n in sorted(kg["nodes"], key=lambda x: x["id"]):
        if n["type"] != "Restriccion" or ("cap", "1.2") not in anclas(n):
            continue
        p = n.get("properties") or {}
        out.append(OrderedDict([("id", n["id"]), ("descripcion", p.get("descripcion")),
                                ("umbrales", [{k: u.get(k) for k in ("valor", "unidad", "moneda", "comparacion",
                                                                      "tramo_verificado", "verificado_en_tabla")}
                                              for u in p.get("umbrales") or []])]))
    ch = [c for c in chunks_de(E0_R2, ["cap"])["cap"] if c["id"] == "cap::1.2"][0]
    tablas = ch["flags"].get("tablas_e0") or []
    return OrderedDict([("restricciones_cap_1_2", out),
                        ("e0_r2_cap_1_2", OrderedDict([("contenido_tabular", ch["flags"].get("contenido_tabular")),
                                                       ("tablas_e0", [{k: t.get(k) for k in ("tabla", "estado", "serializada", "modo")}
                                                                      for t in tablas])]))])


def tablas(kg: dict) -> dict:
    """[c33]: R-CITA y R-PRES de D2 (upre_d2_ausencias.evaluar_cita, texto_nodo, CONTENEDOR) para las citas de los
    criterios no cubiertos de las filas E-tabla y G con E-tabla-no-marcada de D2 ([c17]); y la marca de tabla de E0
    en la e0-r2 de las 16 unidades de U-UMBRAL U1 y de las anclas de D2."""
    d2 = leer(D2_JSON)
    citas = OrderedDict()
    for f in d2["filas"]:
        if not (f["categoria_primaria"] == "E-tabla" or (f["categoria_primaria"] == "G" and "E-tabla-no-marcada"
                                                          in (f.get("categorias_secundarias") or []))):
            continue
        for c in f["criterios"]:
            if c.get("categoria") in ("E-tabla", "G") and c.get("cita_textual"):
                citas.setdefault((f["id_pregunta"], f["ancla"], c["cita_textual"]), c["criterio"])
    out_c = []
    for (preg, ancla, cita), criterio in citas.items():
        to, pt = ancla.split(":")
        hall = []
        for n in kg["nodes"]:
            if n["type"] in ("TextoOrdenado", "Sujeto"):
                continue
            an = anclas(n)
            if not any(t == to and en_subarbol(p, pt) for t, p in an):
                continue
            est = D2.evaluar_cita(cita, D2.texto_nodo(n))
            if est != "ausente":
                hall.append({"id": n["id"], "estado_cita": est, "contenedor": len(an) > D2.CONTENEDOR})
        presente = [h for h in hall if h["estado_cita"] == "presente" and not h["contenedor"]]
        out_c.append(OrderedDict([("pregunta", preg), ("ancla", ancla), ("cita_textual", cita),
                                  ("presente_r_pres", bool(presente)), ("nodos_con_cita", sorted(hall, key=lambda h: h["id"]))]))
    tos = sorted({c.split("::")[0] for c in CHUNKS_TABLAS_4 + CHUNKS_TABLAS_12 + CHUNKS_ANCLAS_D2})
    ch_r2 = {c["id"]: c for to, cs in chunks_de(E0_R2, tos).items() for c in cs}
    ch_l = {c["id"]: c for to, cs in chunks_de(E0_LEGADA, tos).items() for c in cs}

    def marca(cid):
        c, l = ch_r2.get(cid), ch_l.get(cid)
        return OrderedDict([("legada_contenido_tabular", None if l is None else bool(l["flags"].get("contenido_tabular"))),
                            ("e0_r2_contenido_tabular", None if c is None else bool(c["flags"].get("contenido_tabular"))),
                            ("e0_r2_tablas_e0", None if c is None else [t.get("tabla") for t in c["flags"].get("tablas_e0") or []]),
                            ("e0_r2_serializada", None if c is None else any(t.get("serializada") for t in c["flags"].get("tablas_e0") or []))])
    return OrderedDict([("citas_d2", out_c),
                        ("e0_cuatro_de_ponderadores", OrderedDict((c, marca(c)) for c in CHUNKS_TABLAS_4)),
                        ("e0_doce_e0_tablas_sin_marca", OrderedDict((c, marca(c)) for c in CHUNKS_TABLAS_12)),
                        ("e0_anclas_d2", OrderedDict((c, marca(c)) for c in CHUNKS_ANCLAS_D2))])


def crudo_reintento(reporte: dict) -> dict:
    """Origen del crudo que leyó la cadena r2 (reporte del ensamblado r2, e2_por_to.origen_crudo y rechazados)."""
    oc, rech = Counter(), 0
    for v in reporte["e2_por_to"].values():
        oc.update(v["origen_crudo"])
        rech += v["rechazados"]
    return OrderedDict([("origen_crudo", dict(sorted(oc.items()))), ("unidades", sum(oc.values())),
                        ("sin_validacion_rechazadas", rech)])


def omisiones_r2b(kg: dict, tos: list, k: str) -> dict:
    """[c15] en r2b (L-ESQ-R2 §5.4): las omisiones de la extracción final (validación r2 de la entrada de E2 r2,
    salida_r2b/<to>/extracciones_finales_r2_<to>.jsonl) con su categoría y su tramo; las que no traen una de las dos
    son las «sin registro»; el registro del ensamblado (omisiones.jsonl de ens_<x>_r2b/r2) y el ítem LN-7 de la suite."""
    n_unid, n_om, sin_cat, sin_tramo, por_cat = 0, 0, 0, 0, Counter()
    for to in tos:
        for x in (RAIZ / SALIDA_R2B / to / f"extracciones_finales_r2_{to}.jsonl").read_text(encoding="utf-8").splitlines():
            if not x.strip():
                continue
            r = json.loads(x)
            om = (r.get("validacion") or {}).get("omisiones") or []
            n_unid += bool(om)
            for o in om:
                n_om += 1
                por_cat[o.get("categoria")] += 1
                sin_cat += not o.get("categoria")
                sin_tramo += not o.get("tramo")
    reg = RAIZ / T0 / f"ens_{k}_r2b" / "r2" / "omisiones.jsonl"
    filas = [json.loads(x) for x in reg.read_text(encoding="utf-8").splitlines() if x.strip()] if reg.exists() else None
    s = leer(f"{T0}/ens_{k}_r2b/suite_perfil_r2.json")
    ln7 = next((it for it in s["items"] if it["id"] == "LN-7"), None)
    return OrderedDict([("unidades_con_omisiones", n_unid), ("omisiones", n_om), ("sin_categoria", sin_cat),
                        ("sin_tramo", sin_tramo), ("por_categoria", dict(sorted(por_cat.items(), key=lambda x: str(x[0])))),
                        ("registro_del_ensamblado_filas", None if filas is None else len(filas)),
                        ("ln7", None if ln7 is None else {"estado": ln7["estado"], "detalle": ln7["detalle"]})])


def crudo_reintento_salida(tos: list) -> dict:
    """[c16] sobre la salida de U-REEXT-T0: unidades con reintento del ratchet de E3 cuyo crudo del reintento no está
    en el archivo compañero de finales.jsonl (reintentos_e3.jsonl, R2.b), por (chunk_id, intento), last-wins."""
    con, sin, ids, sin_tool = 0, 0, [], []
    for to in tos:
        d = RAIZ / SALIDA_R2B / to
        fin = {}
        for x in (d / "finales.jsonl").read_text(encoding="utf-8").splitlines():
            if x.strip():
                r = json.loads(x)
                fin[r["chunk_id"]] = r
        comp = {}
        p = d / "reintentos_e3.jsonl"
        if p.exists():
            for x in p.read_text(encoding="utf-8").splitlines():
                if x.strip():
                    r = json.loads(x)
                    comp[(r["chunk_id"], r["intento"])] = r
        for cid, r in fin.items():
            n = r.get("n_reintentos") or 0
            if not n:
                continue
            con += 1
            if any((cid, i) not in comp for i in range(1, n + 1)):
                sin += 1
                ids.append(cid)
            elif any(comp[(cid, i)].get("tool_input") is None for i in range(1, n + 1)):
                sin_tool.append({"chunk_id": cid, "errores": [comp[(cid, i)].get("error") for i in range(1, n + 1)]})
    return OrderedDict([("unidades_con_reintento", con), ("sin_registro_del_reintento", sin), ("ids", sorted(ids)),
                        ("registro_sin_tool_input (reintento con error)", sin_tool)])


def colisiones(tos: list) -> dict:
    """[c18] sobre la e0-r2 de la tanda 0: ids repetidos por TO (apariciones de más) y renombres de
    ids_desambiguados.json."""
    rep = OrderedDict()
    for to, cs in chunks_de(E0_R2, tos).items():
        c = Counter(x["id"] for x in cs)
        rep[to] = sum(v - 1 for v in c.values() if v > 1)
    # correr_e0 escribe ids_desambiguados.json solo si hubo ids repetidos (correr_e0.py:1222-1224)
    p = f"{E0_R2}/ids_desambiguados.json"
    return OrderedDict([("ids_repetidos_por_to", rep), ("total", sum(rep.values())),
                        ("ids_desambiguados_json_existe", (RAIZ / p).exists()),
                        ("ids_desambiguados", leer(p) if (RAIZ / p).exists() else None)])


def no_verificadas(kg: dict) -> dict:
    """[c19] en r2a: aristas con no_verificada_e3, por firma."""
    tipo = {n["id"]: n["type"] for n in kg["nodes"]}
    c = Counter(f"{tipo[e['source']]}-{e['relation']}-{tipo[e['target']]}" for e in kg["edges"] if e.get("no_verificada_e3"))
    return OrderedDict([("total", sum(c.values())), ("por_firma", dict(sorted(c.items())))])


def pies(dir_e0: str, tos: list) -> dict:
    """[c22]: chunks con alguna línea de texto que cumple la regex del pie, y líneas."""
    chunks, lineas, ids = 0, 0, []
    for to, cs in chunks_de(dir_e0, tos).items():
        for c in cs:
            n = sum(1 for ln in (c.get("texto") or "").splitlines() if RE_PIE.search(ln))
            if n:
                chunks += 1
                lineas += n
                ids.append(c["id"])
    return OrderedDict([("chunks", chunks), ("de", sum(len(cs) for cs in chunks_de(dir_e0, tos).values())),
                        ("lineas", lineas), ("ids", sorted(ids))])


def frecuencia(kg: dict, reporte: dict) -> dict:
    """[c30]: plazos heredados sin cuantía temporal que llenar_umbrales_r2 manda a `frecuencia`
    (ensamblar_tanda0.py, rama de Obligacion con campos_heredados_v3.plazo), por TO de la procedencia primaria, y
    cuántos quedan fuera de la lista. Se reconoce el nodo por el plazo heredado sin cuantía temporal
    (reglas_comparacion.detectar_cuantias y modelos_r2.UNIDADES_TEMPORALES) con originales.frecuencia igual al
    plazo; el total se controla contra los contadores del reporte (umbrales.frecuencia_desde_plazo y
    frecuencia_fuera_de_lista)."""
    unidades = M.UNIDADES_TEMPORALES + M.UNIDADES_TEMPORALES_FUERA
    van, fuera = Counter(), Counter()
    valores = []
    for n in kg["nodes"]:
        if n["type"] != "Obligacion":
            continue
        v = (n.get("campos_heredados_v3") or {}).get("plazo")
        if not isinstance(v, str) or not v.strip():
            continue
        if any(c.unidad in unidades for c in RCMP.detectar_cuantias(v)):
            continue
        if (n.get("originales") or {}).get("frecuencia") != v:
            continue
        to = n["provenance"].get("to")
        van[to] += 1
        fl = "frecuencia" in (n.get("fuera_de_lista") or [])
        fuera[to] += fl
        valores.append((to, v, n["properties"].get("frecuencia"), fl))
    u = reporte["umbrales"]
    return OrderedDict([("a_frecuencia", sum(van.values())), ("fuera_de_lista", sum(fuera.values())),
                        ("por_to", OrderedDict((to, {"a_frecuencia": van[to], "fuera_de_lista": fuera[to]})
                                               for to in sorted(van))),
                        ("control_reporte", {"frecuencia_desde_plazo": u["frecuencia_desde_plazo"],
                                             "frecuencia_fuera_de_lista": u["frecuencia_fuera_de_lista"],
                                             "coincide": [sum(van.values()), sum(fuera.values())] ==
                                                         [u["frecuencia_desde_plazo"], u["frecuencia_fuera_de_lista"]]}),
                        ("valores_distintos", len({x[1] for x in valores})),
                        ("valores_por_frecuencia", dict(sorted(Counter(x[2] for x in valores if not x[3]).items())))])


def lineas_mayusculas() -> dict:
    """[c34]: las líneas de contenido de la rama de mayúsculas que la E0 legada descarta ([c20],
    r1k_encabezados_descartados.py, `por_to.<to>.contenido` con se_repite_sin_espacios falso) contra las que la e0-r2
    conserva (encabezados_conservados.json de la salida e0-r2, que correr_e0 escribe cuando la regla conserva alguna
    línea); y el efecto de la regla simulada de [c20] sobre la e0-r2 (chunks que cambiarían)."""
    r1k = leer(f"{M2}/r1k_encabezados_descartados_e0r2.json")
    contenido = [(x["to"], x["pagina"], x["texto"]) for to, v in r1k["por_to"].items() for x in v.get("contenido") or []
                 if not x.get("se_repite_sin_espacios")]
    repetidas = [(x["to"], x["pagina"], x["texto"]) for to, v in r1k["por_to"].items() for x in v.get("contenido") or []
                 if x.get("se_repite_sin_espacios")]
    cons = leer(f"{E0_R2}/encabezados_conservados.json")
    conservadas = {(to, x["pagina"], x["texto"]) for to, xs in cons.items() for x in xs}
    efecto = {to: v["efecto_en_e0_r2"]["texto_o_herencia_cambian"] for to, v in r1k["por_to"].items()
              if v["efecto_en_e0_r2"]["texto_o_herencia_cambian"]}
    return OrderedDict([("e0_legada_total", r1k["total"]),
                        ("contenido_en_e0_legada", len(contenido)),
                        ("contenido_conservado_en_e0_r2", sum(1 for c in contenido if c in conservadas)),
                        ("contenido_descartado_en_e0_r2", sum(1 for c in contenido if c not in conservadas)),
                        ("repetidas_sin_espacios_conservadas_en_e0_r2", sum(1 for c in repetidas if c in conservadas)),
                        ("conservadas_e0_r2_total", len(conservadas)),
                        ("efecto_regla_simulada_sobre_e0_r2", efecto)])


def suite(nombre: str, fixture: dict) -> dict:
    """Ítems de la suite del perfil r2 (m2/suite_<grafo>.json, fixture sellada): estados de los 56 y de los 46 de
    la partición; transiciones contra la entrada de r1 (estado_esperado.KG-Reextraido-r1); regresión contra la
    entrada r2 sellada si la hay; el ítem EJ-cla-5.1.1.1 y los de cap::1.2."""
    s = leer(f"{T0}/ens_{nombre}_r2b/suite_perfil_r2.json")   # el gate de T3
    estados = OrderedDict((it["id"], it["estado"]) for it in s["items"])
    part = s["parametros"]["particion"]
    ids46 = [i for i in estados if i not in part["items_r2"]]
    r1 = {k: (v["estado"] if isinstance(v, dict) else v) for k, v in fixture["estado_esperado"]["KG-Reextraido-r1"]["items"].items()}
    trans = Counter((r1.get(i), estados[i]) for i in ids46)
    return OrderedDict([
        ("kg_sha256", s["parametros"]["kg_sha256"]), ("resumen", s["resumen"]),
        ("particion_46", OrderedDict([("n", len(ids46)), ("estados", dict(sorted(Counter(estados[i] for i in ids46).items())))])),
        ("contra_entrada_r1", OrderedDict([
            ("transiciones_r1_a_r2a", {f"{a} -> {b}": n for (a, b), n in sorted(trans.items(), key=lambda x: (str(x[0][0]), x[0][1]))}),
            ("de_resuelto_a_persiste", sorted(i for i in ids46 if r1.get(i) == "resuelto" and estados[i] == "persiste")),
            ("de_resuelto_a_no_aplicable", sorted(i for i in ids46 if r1.get(i) == "resuelto" and estados[i] == "no_aplicable")),
            ("de_persiste_a_resuelto", sorted(i for i in ids46 if r1.get(i) == "persiste" and estados[i] == "resuelto"))])),
        ("regresion", {k: s["regresion"].get(k) for k in ("fixture_sha256", "estado_esperado_sha256", "parte", "entrada",
                                                          "n_regresiones", "coinciden", "sin_esperado", "nota")}),
        ("items", OrderedDict((it["id"], {"estado": it["estado"], "detalle": it["detalle"]}) for it in s["items"]
                              if it["id"] in ("EJ-cla-5.1.1.1", "BKL-0006", "BKL-0023", "T6", "E4-b", "LN-3", "LN-7")))])


def m10(nombre: str, k: str) -> dict:
    d = leer(f"{T0}/ens_{k}_r2b/intrinsecas_gen3/{nombre}.json")   # el gate de T3 (E0 con las partes)
    m = d["metricas"]["M10_chunks_mudos"]
    return OrderedDict([("valor", m["valor"]), ("numerador", m["numerador"]), ("denominador", m["denominador"]),
                        ("mudos", [x["chunk_id"] for x in m["notas"]["mudos_detalle"]]),
                        ("custodia", d["custodia"][0]["custodia"]), ("sha256_medido", d["custodia"][0]["sha256_medido"])])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    enums = leer(ENUMS)
    fixture = leer(FIXTURE)
    out = OrderedDict()
    out["insumos"] = OrderedDict(
        [(f"{k}_{x}", {"ruta": g[x], "sha256": sha256(g[x])}) for k, g in GRAFOS.items()
         for x in ("kg", "reporte", "sellado")] +
        [("fixture", {"ruta": FIXTURE, "sha256": sha256(FIXTURE)}), ("enums_r2", {"ruta": ENUMS, "sha256": sha256(ENUMS)}),
         ("d2", {"ruta": D2_JSON, "sha256": sha256(D2_JSON)})])
    for k, g in GRAFOS.items():
        kg, rep = leer(g["kg"]), leer(g["reporte"])
        sel = leer(g["sellado"])
        tos = tos_de(g["manifiesto"])
        unidades = sum(len(cs) for cs in chunks_de(E0_R2, tos).values())   # unidades de la E0 r2b
        f = OrderedDict()
        f["tos"] = tos
        f["unidades_e0_r2b"] = unidades
        f["f49_obs10"] = obs10(kg, unidades, ("derivada_de_procedencia",))
        f["f49_control_sellado_c1"] = {"extraccion": c1_literal(sel), "por_unidad": round(c1_literal(sel) / unidades, 2)}
        f["f50_obs11"] = obs11(kg, rep)
        f["f50_control_sellado"] = {k2: leer(g["reporte_sellado"])["referencias"][k2] for k2 in ("menciones", "aristas_cross_to")}
        f["f51_remisiones_por_origen"] = remisiones_por_origen(kg)
        f["f51_control_sellado"] = remisiones_por_origen(sel)
        f["f52_aislados"] = aislados(kg)
        f["f52_control_sellado"] = aislados(sel)
        f["f53_falsas_parafrasis"] = falsas_parafrasis(kg)
        f["f53_control_sellado"] = falsas_parafrasis(sel)
        f["f54_f55_suite"] = suite(k, fixture)
        f["f61_m10"] = m10(g["nombre"], k)
        f["f62_cap_1_2"] = cap_1_2(kg)
        f["f63_tablas"] = tablas(kg)
        f["f63_control_sellado_r_pres"] = [{x: c[x] for x in ("pregunta", "ancla", "presente_r_pres")}
                                           for c in tablas(sel)["citas_d2"]]
        f["f64_valores_fuera_de_lista"] = valores_fuera_de_lista(kg, enums)
        f["f64_control_sellado_c11"] = c11_literal(sel)
        f["f65_sujetos"] = sujetos(kg, rep)
        f["f67_cuantias"] = cuantias(kg, "umbrales")
        f["f67_mismo_criterio_con_campo_heredado"] = cuantias(kg, "heredado")
        f["f67_control_sellado_c14"] = cuantias(sel, "heredado")
        f["f67_limites_relativos_s18"] = limites_relativos(kg)
        f["f68_omisiones"] = omisiones_r2b(kg, tos, k)
        f["f69_crudo_reintento"] = crudo_reintento(rep)
        f["f69_crudo_reintento_en_la_salida"] = crudo_reintento_salida(tos)
        f["f70_colisiones_e0_r2"] = colisiones(tos)
        f["f71_no_verificadas_e3"] = no_verificadas(kg)
        f["f73_pies_e0_r2"] = pies(E0_R2, tos)
        f["f73_control_e0_legada"] = pies(E0_LEGADA, tos)
        f["f74_frecuencia"] = frecuencia(kg, rep)
        out[k] = f
    out["f66_catalogo"] = catalogo()
    out["f72_lineas_mayusculas"] = lineas_mayusculas()
    (RAIZ / a.out).parent.mkdir(parents=True, exist_ok=True)
    (RAIZ / a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("escrito:", a.out)


if __name__ == "__main__":
    main()
