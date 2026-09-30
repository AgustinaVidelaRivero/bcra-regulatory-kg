"""U-INSUMOS-CAP, etapa I1 — estadísticas descriptivas del corpus (solo lectura).

Insumo citable para los capítulos 3 y 4 de la tesis: describe los tres conjuntos
de Textos Ordenados (TOs) desde la partición del segmentador (B5.8.4), la salida
de E0 de la tanda 0, la sonda de procedencia y los dos grafos de referencia.
No escribe prosa de la tesis ni toca nada fuera de su directorio de salida.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i1.py
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B reports/u_insumos_cap/u_insumos_i1.py --out-dir <dir>

Salidas: <out-dir>/estadisticas_corpus.json y <out-dir>/estadisticas_corpus.md
(por defecto, el directorio de este script). Determinístico: sin fechas, sin
rutas absolutas, claves ordenadas. Sale con código 1 si las cifras publicadas de
la partición (reporte_b584.md:20) no se reproducen.

Reglas (declaradas antes de aplicarlas; se repiten en el .md, §1):
  R0  Conjuntos. corpus_152 = claves de particion_152.json['por_to'];
      desarrollo_5 = manifiestos/desarrollo_5tos.json tos[].id;
      tanda0_5 = ctacte, lingob, polcre, pagjub, docvig (docs/preregistro_tanda0.md,
      A2.2). Fuentes por TO: b584_particion/<to>/ para corpus_152 y tanda0_5;
      e0_chunking/salida_tanda0/ para desarrollo_5.
  R1  Clase = particion por_to.clase. Categoría = inventario_tos.csv 'categoria';
      desarrollo: regla de construir_inventario.py:34-45 sobre
      indice_oficial_raw.json; clase de la partición: no aplica.
  R2  Páginas por rol = suma de roles_pagina.
  R3  Unidad = elemento de chunks_<to>.json; tipo = campo 'tipo'.
  R4  Profundidad de unidad desde 'unidad': 'S…' → 1; si no, componentes
      separados por '.'. Los mini-chunks llevan la 'unidad' del padre.
  R5  Tablas lógicas = particion 'tablas_logicas' (parseadas) y conteos_b584
      'tabular'; chunks marcados = flags.contenido_tabular / flags.formula.
  R6  Largo = chars_propio (== len(texto)) y chars_completo; mediana =
      statistics.median; percentiles por rango más cercano; máximo.
  R7  Normalización de texto para R8 y R9: quitar "-\\n"; \\s+ → " ".
  R8  Remisiones: regex y separación de corpus_v2/r1_referencias.py
      (:49-50, :63-69, :139-197); excluida la mención de sección en el offset 0.
  R9  Marcadores deónticos (IGNORECASE): deber[áa]n, no podr[áa]n, salvo, excepto.
  R10 Páginas por TO: mínimo, mediana, máximo.
  R11 Profundidad máxima de la numeración por TO, desde estructura_<to>.json.
  R12 Puntos de estructura: terminal (sin hijos) / contenedor (con hijos).
  R13 TOs con tablas (a, b), con fórmulas y con anexo (regex medir_84.py:54).
  R14 Tabla de origen presente si roles_pagina.tabla_norma_origen > 0.
  R15 Procedencia: sonda por_to.portada_comunicacion y texto_ordenado_al, sin
      inferir desde el pie.
  R16 Grafos: sha256, nodes[].type, edges[].relation.
  R17 Cifras publicadas: agregados, suma de por_to, conteos_b584 y chunks,
      contra reporte_b584.md:20.
"""

from __future__ import annotations

import argparse
import collections
import csv
import hashlib
import json
import math
import re
import statistics
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[1]

EXP = "data/experiment"
B584 = f"{EXP}/segmentacion_84/b584_particion"
T0 = f"{EXP}/reextraccion_v2/e0_chunking/salida_tanda0"
ENM01 = f"{EXP}/reextraccion_v2/e0_chunking/salida_enm01"
PARTICION = f"{B584}/particion_152.json"
CONTEOS_B584 = f"{B584}/conteos_b584.json"
REPORTE_B584 = f"{B584}/reporte_b584.md"
CONTEOS_T0 = f"{T0}/conteos.json"
INVENTARIO_RESUMEN = f"{EXP}/escalado_prep/inventario_resumen.json"
INVENTARIO_CSV = f"{EXP}/escalado_prep/inventario_tos.csv"
INDICE_OFICIAL = f"{EXP}/escalado_prep/indice_oficial_raw.json"
MANIFIESTO_DEV = f"{EXP}/reextraccion_v2/manifiestos/desarrollo_5tos.json"
SONDA = f"{EXP}/job_actualizacion/sonda_procedencia.json"
TESTIGO_CAPMIN = f"{EXP}/segmentacion_84/b583_tablas/testigo_capmin/tablas_capmin.json"
KG_T0_DEV = f"{EXP}/reextraccion_v2/corpus_tanda0/ens_desarrollo/r1/kg.json"
KG_R1 = f"{EXP}/reextraccion_v2/corpus_v2/salida_r1/kg.json"

TANDA0_5 = ["ctacte", "lingob", "polcre", "pagjub", "docvig"]
LINEA_PUBLICADA = 20  # reporte_b584.md:20, fila «suma»

# R1: construir_inventario.py:34-45 (archivo publicado → id del subset; lista del
# índice oficial → categoría).
SUBSET_ARCHIVOS = {"t-excbio.pdf": "ext", "t-capmin.pdf": "cap", "t-cladeu.pdf": "cla",
                   "t-pusf.pdf": "pro", "t-RI-CM.pdf": "ric"}
CATEGORIAS = [("normativa_general", "textos_ordenados"),
              ("regimen_informativo", "regimenes_informativos")]

# R8: copia de corpus_v2/r1_referencias.py:49-50 y :63-69.
VENTANA_ANTES = 120
VENTANA_DESPUES = 90
RE_NORMA = re.compile(
    r"(?:[Nn]ormas?\s+sobre|\bT\.?O\.?\s+(?:sobre|de)|[Tt]exto\s+[Oo]rdenado\s+(?:sobre|de))\s*"
    r"[\"“'«]?\s*([^\"”'»\.;\)]{3,90})")
RE_DICHO = re.compile(r"de\s+(?:dicho|ese|este)\s+(?:ordenamiento|texto\s+ordenado)", re.I)
RE_PUNTOS = re.compile(r"\bpuntos?\s+((?:\d+(?:\.\d+)+\.?)(?:\s*(?:,|y|al|a|e|ó|o|hasta)\s*\d+(?:\.\d+)+\.?)*)", re.I)
RE_SECCION = re.compile(r"\bSecci(?:o|ó)n(?:es)?\s+(\d+)(?:\s*(?:,|y)\s*(\d+))?", re.I)
# Sensibilidad de R8: «normas de» no está en RE_NORMA (plan_tesis.md, fila B2.10, punto 3).
RE_NORMAS_DE = re.compile(r"\b[Nn]ormas?\s+de\b")

# R9
DEONTICOS = {
    "deberán": re.compile(r"\bdeber[áa]n\b", re.I),
    "no podrán": re.compile(r"\bno\s+podr[áa]n\b", re.I),
    "salvo": re.compile(r"\bsalvo\b", re.I),
    "excepto": re.compile(r"\bexcepto\b", re.I),
}

# R13: medir_84.py:54.
RE_ANEXO = re.compile(r"^\s*(ANEXO|Anexo)\s*(\d+|[IVXLC]+)?\s*[.:—–-]?\s*$")

PERCENTILES = (10, 25, 75, 90, 99)
CONJUNTOS = ("corpus_152", "desarrollo_5", "tanda0_5")
CMD = ("PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B "
       "reports/u_insumos_cap/u_insumos_i1.py")


# ---------------------------------------------------------------- utilidades

def ruta(rel: str) -> Path:
    return REPO / rel


def cargar(rel: str):
    return json.loads(ruta(rel).read_text(encoding="utf-8"))


def sha256(rel: str) -> str:
    return hashlib.sha256(ruta(rel).read_bytes()).hexdigest()


def ordenar(c: dict) -> dict:
    return {k: c[k] for k in sorted(c, key=lambda x: (str(type(x)), x))}


def rango_cercano(vals_ordenados: list, p: int):
    n = len(vals_ordenados)
    k = max(1, math.ceil(p / 100 * n))
    return vals_ordenados[k - 1]


def resumen_largos(vals: list[int]) -> dict:
    v = sorted(vals)
    if not v:
        return {"n": 0}
    return {
        "n": len(v),
        "minimo": v[0],
        "mediana": statistics.median(v),
        **{f"p{p}": rango_cercano(v, p) for p in PERCENTILES},
        "maximo": v[-1],
    }


def normalizar(texto: str) -> str:
    """R7."""
    return re.sub(r"\s+", " ", texto.replace("-\n", ""))


def profundidad_unidad(unidad: str) -> int:
    """R4."""
    if unidad.startswith("S"):
        return 1
    return len(unidad.split("."))


def profundidad_numero(nodo: dict) -> int:
    if nodo.get("tipo") == "seccion":
        return 1
    return len(str(nodo["numero"]).split("."))


# ---------------------------------------------------------------- remisiones

def contar_remisiones(texto: str) -> dict:
    """R8: separación de detectar_menciones (r1_referencias.py:139-197), solo
    conteo de menciones; sin resolución de destino."""
    externas = anaforicas = internas = internas_normas_de = 0
    consumidos: list[tuple[int, int]] = []
    for m in RE_NORMA.finditer(texto):
        ini = max(0, m.start() - VENTANA_ANTES)
        ventana = texto[ini:m.start()]
        for pm in RE_PUNTOS.finditer(ventana):
            consumidos.append((ini + pm.start(), ini + pm.end()))
        for sm in RE_SECCION.finditer(ventana):
            consumidos.append((ini + sm.start(), ini + sm.end()))
        externas += 1
    for m in RE_DICHO.finditer(texto):
        ini = max(0, m.start() - VENTANA_ANTES)
        ventana = texto[ini:m.start()]
        for pm in RE_PUNTOS.finditer(ventana):
            consumidos.append((ini + pm.start(), ini + pm.end()))
        anaforicas += 1

    def consumido(a: int, b: int) -> bool:
        return any(a >= x and b <= y for x, y in consumidos)

    for rx, es_seccion in ((RE_PUNTOS, False), (RE_SECCION, True)):
        for pm in rx.finditer(texto):
            if es_seccion and pm.start() == 0:
                continue  # encabezado propio de la unidad
            if consumido(pm.start(), pm.end()):
                continue
            despues = texto[pm.end():pm.end() + VENTANA_DESPUES]
            if RE_NORMA.search(despues) or RE_DICHO.search(despues):
                continue
            internas += 1
            if RE_NORMAS_DE.search(despues):
                internas_normas_de += 1
    return {"externas": externas, "externas_anaforicas": anaforicas,
            "internas": internas, "internas_con_normas_de": internas_normas_de}


# ---------------------------------------------------------------- carga

def categoria_desarrollo() -> dict:
    """R1 para los 5 de desarrollo: construir_inventario.py:34-45."""
    crudo = cargar(INDICE_OFICIAL)
    out = {}
    for categoria, clave in CATEGORIAS:
        for it in crudo[clave]:
            if it["archivo"] in SUBSET_ARCHIVOS:
                out[SUBSET_ARCHIVOS[it["archivo"]]] = categoria
    return out


def cargar_conjuntos() -> tuple[dict, dict]:
    particion = cargar(PARTICION)["por_to"]
    conteos_b584 = cargar(CONTEOS_B584)
    conteos_t0 = cargar(CONTEOS_T0)
    inv = {r["id"]: r for r in csv.DictReader(
        ruta(INVENTARIO_CSV).open(encoding="utf-8"))}
    dev_ids = [t["id"] for t in cargar(MANIFIESTO_DEV)["tos"]]
    cat_dev = categoria_desarrollo()

    fuentes: dict[str, str] = {}

    def por_to_b584(to: str) -> dict:
        fc = f"{B584}/{to}/chunks_{to}.json"
        fe = f"{B584}/{to}/estructura_{to}.json"
        fuentes[fc] = sha256(fc)
        fuentes[fe] = sha256(fe)
        c = conteos_b584[to]
        p = particion[to]
        tab = c.get("tabular") or {}
        return {
            "to": to, "chunks": cargar(fc), "estructura": cargar(fe),
            "paginas": c["paginas"], "roles_pagina": c["roles_pagina"],
            "clase": p["clase"], "categoria": inv[to]["categoria"],
            "tablas_logicas_parseadas": p["tablas_logicas"],
            "tabular_detectadas": tab.get("tablas_logicas", 0),
            "tabular_declaradas": tab.get("declaradas", 0),
            "fuente_chunks": fc, "fuente_estructura": fe,
            "fuente_paginas": f"{CONTEOS_B584} → {to}.paginas",
            "fuente_roles": f"{CONTEOS_B584} → {to}.roles_pagina",
        }

    def por_to_dev(to: str) -> dict:
        fc = f"{T0}/chunks_{to}.json"
        fe = f"{T0}/estructura_{to}.json"
        fuentes[fc] = sha256(fc)
        fuentes[fe] = sha256(fe)
        c = conteos_t0[to]
        return {
            "to": to, "chunks": cargar(fc), "estructura": cargar(fe),
            "paginas": c["paginas"], "roles_pagina": c["roles_pagina"],
            "clase": None, "categoria": cat_dev[to],
            "tablas_logicas_parseadas": None,
            "tabular_detectadas": None, "tabular_declaradas": None,
            "fuente_chunks": fc, "fuente_estructura": fe,
            "fuente_paginas": f"{CONTEOS_T0} → {to}.paginas",
            "fuente_roles": f"{CONTEOS_T0} → {to}.roles_pagina",
        }

    conjuntos = {
        "corpus_152": [por_to_b584(t) for t in sorted(particion)],
        "desarrollo_5": [por_to_dev(t) for t in sorted(dev_ids)],
        "tanda0_5": [por_to_b584(t) for t in sorted(TANDA0_5)],
    }
    return conjuntos, fuentes


# ---------------------------------------------------------------- estadísticas

def estadisticas_conjunto(nombre: str, tos: list[dict], sonda: dict) -> dict:
    n_tos = len(tos)
    es_dev = nombre == "desarrollo_5"

    # R1
    clase_cat = collections.Counter()
    for t in tos:
        clase_cat[f"{t['clase'] or 'no_aplica'} · {t['categoria']}"] += 1
    por_categoria = collections.Counter(t["categoria"] for t in tos)
    por_clase = collections.Counter(t["clase"] or "no_aplica" for t in tos)

    # R2, R10, R14
    roles = collections.Counter()
    for t in tos:
        roles.update(t["roles_pagina"])
    paginas = sorted(t["paginas"] for t in tos)
    tabla_origen = {t["to"]: t["roles_pagina"].get("tabla_norma_origen", 0) for t in tos}

    # R3–R6, R8, R9, R13 (sobre chunks)
    tipos = collections.Counter()
    roles_mini = collections.Counter()
    prof = collections.Counter()
    tipo_prof = collections.Counter()
    largos_propio, largos_completo = [], []
    largos_por_tipo: dict[str, list[int]] = collections.defaultdict(list)
    flag_tab = flag_form = sub_chunks = 0
    deon_occ = collections.Counter()
    deon_uni = collections.Counter()
    rem_tot = collections.Counter()
    rem_uni = collections.Counter()
    por_to: dict[str, dict] = {}
    chars_total = 0
    chars_propio_ok = True

    for t in tos:
        to = t["to"]
        rt = collections.Counter()
        dt = collections.Counter()
        anexo_lineas = 0
        ft = ff = 0
        for ch in t["chunks"]:
            tipos[ch["tipo"]] += 1
            if ch["tipo"] == "mini_chunk":
                roles_mini[ch.get("rol_bloque")] += 1
            if "sub_chunk" in ch:
                sub_chunks += 1
            d = profundidad_unidad(ch["unidad"])
            prof[d] += 1
            tipo_prof[f"{ch['tipo']} | {d}"] += 1
            if len(ch["texto"]) != ch["chars_propio"]:
                chars_propio_ok = False
            largos_propio.append(ch["chars_propio"])
            largos_completo.append(ch["chars_completo"])
            largos_por_tipo[ch["tipo"]].append(ch["chars_propio"])
            chars_total += ch["chars_propio"]
            if ch["flags"]["contenido_tabular"]:
                flag_tab += 1
                ft += 1
            if ch["flags"]["formula"]:
                flag_form += 1
                ff += 1
            for linea in ch["texto"].split("\n"):
                if RE_ANEXO.match(linea):
                    anexo_lineas += 1
            norm = normalizar(ch["texto"])
            r = contar_remisiones(norm)
            rt.update(r)
            for k, v in r.items():
                if v:
                    rem_uni[k] += 1
            if r["externas"] or r["externas_anaforicas"] or r["internas"]:
                rem_uni["con_alguna"] += 1
            for mk, rx in DEONTICOS.items():
                k = len(rx.findall(norm))
                if k:
                    dt[mk] += k
                    deon_uni[mk] += 1
        rem_tot.update(rt)
        deon_occ.update(dt)

        # R11, R12 (sobre estructura)
        term = cont = 0
        pmax = 0

        def rec(nodo: dict) -> None:
            nonlocal term, cont, pmax
            pmax = max(pmax, profundidad_numero(nodo))
            if nodo.get("tipo") == "punto":
                if nodo.get("hijos"):
                    cont += 1
                else:
                    term += 1
            for h in nodo.get("hijos", []):
                rec(h)

        for s in t["estructura"]["secciones"]:
            rec(s)

        proc = sonda["por_to"].get(to, {})
        por_to[to] = {
            "clase": t["clase"],
            "categoria": t["categoria"],
            "paginas": t["paginas"],
            "unidades": len(t["chunks"]),
            "tabla_norma_origen_paginas": tabla_origen[to],
            "tabla_norma_origen_presente": tabla_origen[to] > 0,
            "tablas_logicas_parseadas": t["tablas_logicas_parseadas"],
            "chunks_contenido_tabular": ft,
            "chunks_formula": ff,
            "lineas_anexo": anexo_lineas,
            "profundidad_maxima": pmax,
            "puntos_terminales": term,
            "puntos_contenedores": cont,
            "remisiones": ordenar(dict(rt)),
            "deonticos": ordenar(dict(dt)),
            "portada_comunicacion": proc.get("portada_comunicacion"),
            "texto_ordenado_al": proc.get("texto_ordenado_al"),
            "portada_ilegible_por_glifos": proc.get("portada_ilegible_por_glifos"),
            "sonda_paginas": proc.get("paginas"),
        }

    n_uni = sum(tipos.values())
    term_tot = sum(v["puntos_terminales"] for v in por_to.values())
    cont_tot = sum(v["puntos_contenedores"] for v in por_to.values())
    pmax_dist = collections.Counter(v["profundidad_maxima"] for v in por_to.values())
    rem_por_to = {to: v["remisiones"] for to, v in por_to.items()}
    ext_por_to = sorted(v["remisiones"].get("externas", 0) for v in por_to.values())
    int_por_to = sorted(v["remisiones"].get("internas", 0) for v in por_to.values())

    tos_tablas_a = sorted(to for to, v in por_to.items()
                          if (v["tablas_logicas_parseadas"] or 0) > 0)
    tos_tablas_b = sorted(to for to, v in por_to.items() if v["chunks_contenido_tabular"] > 0)
    tos_formula = sorted(to for to, v in por_to.items() if v["chunks_formula"] > 0)
    tos_anexo = sorted(to for to, v in por_to.items() if v["lineas_anexo"] > 0)
    tos_origen = sorted(to for to, v in por_to.items() if v["tabla_norma_origen_presente"])

    con_portada = sorted(to for to, v in por_to.items() if v["portada_comunicacion"])
    con_fecha = sorted(to for to, v in por_to.items() if v["texto_ordenado_al"])
    ilegibles = sorted(to for to, v in por_to.items() if v["portada_ilegible_por_glifos"])

    tablas = {
        "tablas_logicas_parseadas": (None if es_dev else
                                     sum(t["tablas_logicas_parseadas"] for t in tos)),
        "tablas_logicas_detectadas_conteos_b584": (None if es_dev else
                                                   sum(t["tabular_detectadas"] for t in tos)),
        "tablas_logicas_declaradas_conteos_b584": (None if es_dev else
                                                   sum(t["tabular_declaradas"] for t in tos)),
        "chunks_contenido_tabular": flag_tab,
        "chunks_formula": flag_form,
        "denominador_chunks": n_uni,
    }
    if es_dev:
        testigo = cargar(TESTIGO_CAPMIN)["conteos"]
        tablas["testigo_capmin_b583"] = {
            "to": "cap", "tablas_logicas": testigo["tablas_logicas"],
            "parseadas": testigo["parseadas"], "declaradas": testigo["declaradas"],
            "fuente": f"{TESTIGO_CAPMIN} → conteos",
        }
        tablas["cla_ext_pro_ric"] = "NO ENCONTRADO"

    return {
        "tos": n_tos,
        "ids": [t["to"] for t in tos],
        "R1_tos_por_clase": ordenar(dict(por_clase)),
        "R1_tos_por_categoria": ordenar(dict(por_categoria)),
        "R1_tos_por_clase_y_categoria": ordenar(dict(clase_cat)),
        "R2_paginas_por_rol": ordenar(dict(roles)),
        "R2_paginas_total": sum(roles.values()),
        "R2_paginas_total_suma_por_to": sum(paginas),
        "R3_unidades_por_tipo": ordenar(dict(tipos)),
        "R3_mini_chunks_por_rol": ordenar(dict(roles_mini)),
        "R3_unidades_sub_chunk": sub_chunks,
        "R3_unidades_total": n_uni,
        "R4_unidades_por_profundidad": ordenar(dict(prof)),
        "R4_unidades_por_tipo_y_profundidad": ordenar(dict(tipo_prof)),
        "R5_tablas": tablas,
        "R6_largo_chars_propio": resumen_largos(largos_propio),
        "R6_largo_chars_completo": resumen_largos(largos_completo),
        "R6_largo_chars_propio_por_tipo": {k: resumen_largos(v)
                                           for k, v in sorted(largos_por_tipo.items())},
        "R6_chars_propio_igual_len_texto": chars_propio_ok,
        "R8_remisiones_total": ordenar(dict(rem_tot)),
        "R8_unidades_con_remision": ordenar(dict(rem_uni)),
        "R8_remisiones_por_to": rem_por_to,
        "R8_externas_por_to_resumen": {"minimo": ext_por_to[0],
                                       "mediana": statistics.median(ext_por_to),
                                       "maximo": ext_por_to[-1],
                                       "tos_con_alguna": sum(1 for x in ext_por_to if x)},
        "R8_internas_por_to_resumen": {"minimo": int_por_to[0],
                                       "mediana": statistics.median(int_por_to),
                                       "maximo": int_por_to[-1],
                                       "tos_con_alguna": sum(1 for x in int_por_to if x)},
        "R9_deonticos_ocurrencias": ordenar(dict(deon_occ)),
        "R9_deonticos_unidades_con_al_menos_una": ordenar(dict(deon_uni)),
        "R9_chars_propio_total": chars_total,
        "R10_paginas_por_to": {"minimo": paginas[0], "mediana": statistics.median(paginas),
                               "maximo": paginas[-1]},
        "R11_profundidad_maxima_por_to_distribucion": ordenar(dict(pmax_dist)),
        "R11_profundidad_maxima_del_conjunto": max(pmax_dist),
        "R12_puntos_terminales": term_tot,
        "R12_puntos_contenedores": cont_tot,
        "R12_puntos_total": term_tot + cont_tot,
        "R13_tos_con_tablas_logicas_parseadas": (None if es_dev else tos_tablas_a),
        "R13_tos_con_chunk_contenido_tabular": tos_tablas_b,
        "R13_tos_con_chunk_formula": tos_formula,
        "R13_tos_con_linea_anexo": tos_anexo,
        "R14_tos_con_tabla_norma_origen": tos_origen,
        "R15_procedencia_cobertura": {
            "con_portada_comunicacion": len(con_portada),
            "con_texto_ordenado_al": len(con_fecha),
            "portada_ilegible_por_glifos": ilegibles,
            "sin_portada_comunicacion": sorted(set(por_to) - set(con_portada)),
            "denominador_tos": n_tos,
        },
        "por_to": por_to,
    }


def estadisticas_grafo(rel: str) -> dict:
    g = cargar(rel)
    tipos = collections.Counter(n["type"] for n in g["nodes"])
    rels = collections.Counter(e["relation"] for e in g["edges"])
    return {
        "ruta": rel,
        "sha256": sha256(rel),
        "nodos": len(g["nodes"]),
        "aristas": len(g["edges"]),
        "tipos_de_nodo": len(tipos),
        "tipos_de_relacion": len(rels),
        "nodos_por_tipo": ordenar(dict(tipos)),
        "aristas_por_relacion": ordenar(dict(rels)),
    }


def cifras_publicadas(conjuntos: dict) -> dict:
    """R17."""
    p = cargar(PARTICION)
    ag = p["agregados"]
    por_to = p["por_to"]
    cb = cargar(CONTEOS_B584)
    linea = ruta(REPORTE_B584).read_text(encoding="utf-8").splitlines()[LINEA_PUBLICADA - 1]
    celdas = [c.strip().strip("*") for c in linea.strip().strip("|").split("|")]
    publicada = {"tos": int(celdas[1]), "paginas": int(celdas[2]),
                 "unidades": int(celdas[3]), "tablas_logicas": int(celdas[4])}
    vias = {
        "agregados": {k: sum(v[k] for v in ag.values())
                      for k in ("tos", "paginas", "unidades", "tablas_logicas")},
        "suma_por_to": {"tos": len(por_to),
                        "paginas": sum(d["paginas"] for d in por_to.values()),
                        "unidades": sum(d["unidades"] for d in por_to.values()),
                        "tablas_logicas": sum(d["tablas_logicas"] for d in por_to.values())},
        "conteos_b584": {"tos": len(cb),
                         "paginas": sum(d["paginas"] for d in cb.values()),
                         "unidades": sum(d["unidades_extraccion"] for d in cb.values()),
                         "tablas_logicas": sum((d.get("tabular") or {}).get("parseadas", 0)
                                               for d in cb.values())},
        "chunks_y_roles": {"tos": len(conjuntos["corpus_152"]),
                           "paginas": sum(sum(t["roles_pagina"].values())
                                          for t in conjuntos["corpus_152"]),
                           "unidades": sum(len(t["chunks"]) for t in conjuntos["corpus_152"]),
                           "tablas_logicas": None},
    }
    ok = all(v[k] == publicada[k] for v in vias.values() for k in publicada
             if v[k] is not None)
    return {"linea_publicada": f"{REPORTE_B584}:{LINEA_PUBLICADA}",
            "publicada": publicada, "reproducida_por_via": vias, "coinciden": ok}


def controles(conjuntos: dict, sonda: dict) -> dict:
    out = {}
    # tanda0_5: b584 == salida_tanda0, byte a byte
    ident = {}
    for to in TANDA0_5:
        for f in ("chunks", "estructura"):
            a = f"{B584}/{to}/{f}_{to}.json"
            b = f"{T0}/{f}_{to}.json"
            ident[f"{to}.{f}"] = sha256(a) == sha256(b)
    out["tanda0_5_b584_igual_salida_tanda0"] = ident
    # desarrollo_5: salida_tanda0 == salida_enm01 (E0 de r1)
    ident = {}
    for t in conjuntos["desarrollo_5"]:
        to = t["to"]
        for f in ("chunks", "estructura"):
            ident[f"{to}.{f}"] = sha256(f"{T0}/{f}_{to}.json") == sha256(f"{ENM01}/{f}_{to}.json")
    out["desarrollo_5_salida_tanda0_igual_salida_enm01"] = ident
    # unidades = unidades_extraccion (b584) / chunks (conteos tanda 0)
    cb = cargar(CONTEOS_B584)
    ct = cargar(CONTEOS_T0)
    dif = {}
    for t in conjuntos["corpus_152"]:
        if len(t["chunks"]) != cb[t["to"]]["unidades_extraccion"]:
            dif[t["to"]] = [len(t["chunks"]), cb[t["to"]]["unidades_extraccion"]]
    for t in conjuntos["desarrollo_5"]:
        if len(t["chunks"]) != ct[t["to"]]["chunks"]:
            dif[t["to"]] = [len(t["chunks"]), ct[t["to"]]["chunks"]]
    out["unidades_distintas_de_conteos"] = dif
    # páginas de la sonda vs páginas de E0
    dif = {}
    for nombre in ("corpus_152", "desarrollo_5"):
        for t in conjuntos[nombre]:
            sp = sonda["por_to"].get(t["to"], {}).get("paginas")
            if sp != t["paginas"]:
                dif[t["to"]] = [t["paginas"], sp]
    out["paginas_sonda_distintas_de_e0"] = dif
    # puntos terminales de estructura vs chunks punto_terminal (con y sin sub-chunking)
    dif, dif_unidades = {}, {}
    for nombre in ("corpus_152", "desarrollo_5"):
        for t in conjuntos[nombre]:
            pts = [c for c in t["chunks"] if c["tipo"] == "punto_terminal"]
            pt = len(pts)
            pt_unidades = len({c["unidad"] for c in pts})
            term = 0

            def rec(n: dict) -> None:
                nonlocal term
                if n.get("tipo") == "punto" and not n.get("hijos"):
                    term += 1
                for h in n.get("hijos", []):
                    rec(h)
            for s in t["estructura"]["secciones"]:
                rec(s)
            if pt != term:
                dif[t["to"]] = {"chunks_punto_terminal": pt,
                                "chunks_punto_terminal_sub_chunk": sum(1 for c in pts
                                                                        if "sub_chunk" in c),
                                "unidades_distintas_punto_terminal": pt_unidades,
                                "estructura_puntos_sin_hijos": term}
            if pt_unidades != term:
                dif_unidades[t["to"]] = [pt_unidades, term]
    out["puntos_terminales_estructura_vs_chunks"] = dif
    out["puntos_terminales_estructura_vs_unidades_distintas"] = dif_unidades
    # ids de chunk repetidos dentro de un mismo TO
    rep = {}
    for nombre in ("corpus_152", "desarrollo_5"):
        for t in conjuntos[nombre]:
            g: dict[str, list] = collections.defaultdict(list)
            for c in t["chunks"]:
                g[c["id"]].append(c["sha256_propio"])
            dups = {k: v for k, v in g.items() if len(v) > 1}
            if dups:
                rep[t["to"]] = {
                    "ids_repetidos": len(dups),
                    "chunks_de_mas": sum(len(v) - 1 for v in dups.values()),
                    "ids_con_mismo_texto": sum(1 for v in dups.values() if len(set(v)) == 1),
                    "ejemplos": sorted(dups)[:3],
                }
    out["ids_de_chunk_repetidos"] = rep
    out["diferencia_terminales_explicada_por_ids_repetidos"] = all(
        to in rep and term - pt_u == rep[to]["chunks_de_mas"]
        for to, (pt_u, term) in dif_unidades.items())
    # salida del parser de tablas en la E0 de r1 y de la tanda 0
    out["archivos_tablas_en_salida_enm01_y_salida_tanda0"] = sorted(
        str(p.relative_to(REPO)) for d in (ENM01, T0) for p in ruta(d).glob("tablas_*"))
    # grupos de la sonda
    ids152 = {t["to"] for t in conjuntos["corpus_152"]}
    grupo152 = {k for k, v in sonda["por_to"].items() if v.get("grupo") == "inventariado_152"}
    out["sonda_grupo_152_igual_particion"] = grupo152 == ids152
    return out


# ---------------------------------------------------------------- markdown

def fmt(x) -> str:
    if x is None:
        return "—"
    if isinstance(x, bool):
        return "sí" if x else "no"
    if isinstance(x, float):
        if x.is_integer():
            return fmt(int(x))
        return f"{x:,.1f}".replace(",", "X").replace(".", ",").replace("X", ".")
    if isinstance(x, int):
        return f"{x:,}".replace(",", ".")
    return str(x)


def frac(a: int, b: int) -> str:
    """Fracción cruda; porcentaje solo con denominador ≥ 100."""
    s = f"{fmt(a)} de {fmt(b)}"
    if b >= 100:
        pct = 100 * a / b
        s += f" ({pct:.1f} %)".replace(".", ",")
    return s


def md(res: dict) -> str:
    L: list[str] = []
    A = L.append
    C = res["conjuntos"]
    c1, cd, c0 = C["corpus_152"], C["desarrollo_5"], C["tanda0_5"]

    A("# U-INSUMOS-CAP · I1 — Estadísticas descriptivas del corpus")
    A("")
    A("Insumo citable para los capítulos 3 y 4 (mesa de escritura). No es prosa de la tesis.")
    A("Todas las cifras salen de artefactos del repo; ninguna llamada a la API.")
    A("")
    A("Regenerar (desde la raíz del repo; doble corrida byte a byte idéntica):")
    A("")
    A("```bash")
    A(CMD)
    A("```")
    A("")
    A("Cada cifra de este documento está en `reports/u_insumos_cap/estadisticas_corpus.json`; "
      "la línea «Claves» debajo de cada tabla da la ruta dentro de `conjuntos.<conjunto>` (o la "
      "raíz indicada). Consulta de una clave:")
    A("")
    A("```bash")
    A("python3 -c \"import json; d=json.load(open('reports/u_insumos_cap/estadisticas_corpus.json')); "
      "print(json.dumps(d['conjuntos']['corpus_152']['R2_paginas_por_rol'], ensure_ascii=False))\"")
    A("```")
    A("")
    A("Conjuntos: **corpus_152** = los 152 TOs de la partición del segmentador "
      "(`particion_152.json`, clave `por_to`; no incluye a los cinco de desarrollo, "
      "`inventario_resumen.json` → `subset_excluido`); **desarrollo_5** = `cap`, `cla`, `ext`, "
      "`pro`, `ric` (`manifiestos/desarrollo_5tos.json`); **tanda0_5** = el conjunto de la "
      "tanda 0 en la convención de `docs/preregistro_tanda0.md` (A2.2): `ctacte`, `lingob`, "
      "`polcre`, `pagjub`, `docvig`, que también están dentro de corpus_152.")
    A("")

    # §0
    cp = res["cifras_publicadas"]
    A("## 0. Cifras publicadas de la partición, reproducidas")
    A("")
    A(f"Fila publicada: `{cp['linea_publicada']}`. Resultado: "
      f"**{'coinciden las cuatro por todas las vías' if cp['coinciden'] else 'DIFERENCIA — FRENO'}**.")
    A("")
    A("| vía | TOs | páginas | unidades | tablas lógicas |")
    A("|---|--:|--:|--:|--:|")
    pb = cp["publicada"]
    A(f"| publicada (`reporte_b584.md:20`) | {fmt(pb['tos'])} | {fmt(pb['paginas'])} | "
      f"{fmt(pb['unidades'])} | {fmt(pb['tablas_logicas'])} |")
    etiquetas = {
        "agregados": "`particion_152.json` → `agregados` (suma de clases)",
        "suma_por_to": "`particion_152.json` → suma de `por_to`",
        "conteos_b584": "`conteos_b584.json` (`paginas`, `unidades_extraccion`, `tabular.parseadas`)",
        "chunks_y_roles": "chunks_<to>.json (cantidad) y suma de `roles_pagina`",
    }
    for k, v in cp["reproducida_por_via"].items():
        A(f"| {etiquetas[k]} | {fmt(v['tos'])} | {fmt(v['paginas'])} | {fmt(v['unidades'])} | "
          f"{fmt(v['tablas_logicas'])} |")
    A("")
    A("Clave: `cifras_publicadas`. Recómputo independiente de una línea:")
    A("")
    A("```bash")
    A("python3 -c \"import json; p=json.load(open('data/experiment/segmentacion_84/b584_particion/"
      "particion_152.json')); a=p['agregados']; print({k: sum(v[k] for v in a.values()) for k in "
      "('tos','paginas','unidades','tablas_logicas')})\"")
    A("```")
    A("")
    A("Matiz de nomenclatura: en `particion_152.json` la clave `tablas_logicas` cuenta tablas "
      "**parseadas** (559); en `conteos_b584.json`, `tabular.tablas_logicas` cuenta las "
      f"**detectadas** ({fmt(c1['R5_tablas']['tablas_logicas_detectadas_conteos_b584'])} = "
      f"{fmt(c1['R5_tablas']['tablas_logicas_parseadas'])} parseadas + "
      f"{fmt(c1['R5_tablas']['tablas_logicas_declaradas_conteos_b584'])} declaradas sin parsear, "
      "en `ri_niif` y `snp_tr`).")
    A("")

    # §1 reglas
    A("## 1. Reglas declaradas (antes de aplicarlas)")
    A("")
    A("Las reglas se fijaron en el checkpoint de la unidad antes de escribir el script; el "
      "script las implementa con el mismo número.")
    A("")
    reglas = [
        ("R0", "Conjuntos y fuentes. corpus_152 y tanda0_5: `data/experiment/segmentacion_84/"
               "b584_particion/<to>/{chunks,estructura}_<to>.json`, `conteos_b584.json`, "
               "`particion_152.json`. desarrollo_5: `data/experiment/reextraccion_v2/e0_chunking/"
               "salida_tanda0/{chunks,estructura}_<to>.json` y `conteos.json` (byte-idénticos a "
               "`salida_enm01`, la E0 que lee el ensamblado de KG-Reextraído-r1: "
               "`corpus_v2/r1_comun.py:29` y `corpus_v2/ensamblar_r1.py:56`; control en §6)."),
        ("R1", "Clase = `particion_152.json` → `por_to.<to>.clase`. Categoría = "
               "`escalado_prep/inventario_tos.csv`, campo `categoria`. Desarrollo: regla de "
               "`escalado_prep/code/construir_inventario.py:34-45` (la lista del índice oficial "
               "`indice_oficial_raw.json` donde figura el archivo: `textos_ordenados` → "
               "normativa_general; `regimenes_informativos` → regimen_informativo); la clase de "
               "la partición no aplica (los cinco no están en `particion_152.json`)."),
        ("R2", "Páginas por rol = suma de `roles_pagina` por conjunto; denominador = páginas "
               "del conjunto."),
        ("R3", "Unidad = cada elemento de `chunks_<to>.json` (las partes de sub-chunking cuentan "
               "como unidades, igual que `unidades_extraccion`); tipo = campo `tipo` "
               "(`punto_terminal`, `mini_chunk`, `seccion_sin_puntos`)."),
        ("R4", "Profundidad de una unidad, desde su campo `unidad`: si empieza con `S` (sección) "
               "vale 1; si no, la cantidad de componentes separados por punto (`1.2` → 2, "
               "`1.2.3` → 3). Los mini-chunks (`::intro`, `::cierre`, `::intersticial`, "
               "`::chapeau_seccion`) llevan en `unidad` el número del padre, así que toman la "
               "profundidad del padre."),
        ("R5", "Tablas lógicas = `particion_152.json` → `por_to.<to>.tablas_logicas` (parseadas por "
               "B5.8.3) y, aparte, `conteos_b584.json` → `<to>.tabular` (detectadas y declaradas). "
               "Chunks marcados = `flags.contenido_tabular` y `flags.formula` de E0. Desarrollo: "
               "no hay archivos `tablas_*` en `salida_enm01/` ni en `salida_tanda0/` (control en "
               "§6); solo `cap` tiene el testigo de B5.8.3 "
               "(`b583_tablas/testigo_capmin/tablas_capmin.json`)."),
        ("R6", "Largo de unidad = `chars_propio` (igual a `len(texto)`, verificado) y, aparte, "
               "`chars_completo` (con encabezados heredados). Mediana = `statistics.median`; "
               "p10, p25, p75, p90 y p99 por rango más cercano (posición ⌈p/100·n⌉ de la lista "
               "ordenada, desde 1); máximo."),
        ("R7", "Normalización del texto para R8 y R9: se quita cada guion de fin de línea "
               "(`-\\n`) y todo blanco consecutivo pasa a un espacio."),
        ("R8", "Remisiones: `RE_NORMA`, `RE_DICHO`, `RE_PUNTOS` y `RE_SECCION` copiadas de "
               "`data/experiment/reextraccion_v2/corpus_v2/r1_referencias.py:63-69`, ventanas de "
               "120 y 90 caracteres (`:49-50`) y separación de `detectar_menciones` (`:139-197`), "
               "aplicadas al texto de E0 de cada unidad (no a la paráfrasis del grafo). Cada "
               "mención de norma (`RE_NORMA`) cuenta como una remisión **externa** y consume los "
               "puntos y secciones de sus 120 caracteres previos; cada «de dicho/ese/este "
               "ordenamiento» (`RE_DICHO`) cuenta como una externa anafórica; cada mención de "
               "punto o sección no consumida y sin norma en sus 90 caracteres siguientes cuenta "
               "como una remisión **interna** (al mismo TO). No se cuenta la mención de sección "
               "en el offset 0 del texto (el encabezado propio de la unidad). Unidad de conteo: "
               "la mención (una lista «puntos 1.1. y 1.2.» es una). Límites: la norma nombrada no "
               "se resuelve contra el inventario, así que «externa» es «hacia una norma "
               "nombrada», que puede ser el mismo TO; `RE_NORMA` no reconoce «normas de» "
               "(plan, fila B2.10, punto 3): la sensibilidad `internas_con_normas_de` cuenta las "
               "internas con `\\b[Nn]ormas?\\s+de\\b` en sus 90 caracteres siguientes."),
        ("R9", "Marcadores deónticos, sin distinguir mayúsculas, sobre el texto normalizado (R7): "
               "«deberán» `\\bdeber[áa]n\\b`; «no podrán» `\\bno\\s+podr[áa]n\\b`; «salvo» "
               "`\\bsalvo\\b`; «excepto» `\\bexcepto\\b`. Se reportan ocurrencias y unidades con "
               "al menos una; denominadores: unidades y caracteres del conjunto."),
        ("R10", "Páginas por TO: mínimo, mediana (`statistics.median`) y máximo de `paginas`."),
        ("R11", "Profundidad máxima de la numeración por TO, desde `estructura_<to>.json`: un "
                "punto vale la cantidad de componentes de su `numero`; una sección vale 1."),
        ("R12", "Puntos de la estructura (`tipo` = `punto`; las secciones no cuentan): "
                "**terminal** si no tiene hijos, **contenedor** si tiene. Proporción sobre los "
                "puntos del conjunto."),
        ("R13", "TO con tablas: (a) al menos una tabla lógica parseada; (b) al menos un chunk "
                "con `contenido_tabular`. TO con fórmulas: al menos un chunk con `formula`. TO "
                "con anexo: al menos una línea del texto crudo de sus chunks que matchea la regex "
                "de encabezado de anexo de `data/experiment/segmentacion_84/code/medir_84.py:54` "
                "(`^\\s*(ANEXO|Anexo)\\s*(\\d+|[IVXLC]+)?\\s*[.:—–-]?\\s*$`); es cota inferior: "
                "un anexo fuera de los chunks de E0 no se ve."),
        ("R14", "Tabla de origen de las disposiciones presente si "
                "`roles_pagina.tabla_norma_origen` > 0."),
        ("R15", "Procedencia: `sonda_procedencia.json` → `por_to.<to>.portada_comunicacion` "
                "(«Última comunicación incorporada», forma P) y `texto_ordenado_al`; no se infiere "
                "desde el pie de página (`job_actualizacion/diseno_job_actualizacion.md`, §4). "
                "Cobertura = TOs con el campo no nulo sobre los TOs del conjunto."),
        ("R16", "Grafos: sha256 del archivo; conteo de `nodes[].type` y de `edges[].relation`."),
        ("R17", "Cifras publicadas: cuatro vías independientes contra `reporte_b584.md:20` (§0)."),
    ]
    for k, v in reglas:
        A(f"- **{k}.** {v}")
    A("")

    # §2 tablas
    A("## 2. Estadísticas por conjunto")
    A("")
    A("Clave base: `conjuntos.<conjunto>.<clave>`. «—» = no aplica o sin artefacto (ver notas).")
    A("")

    A("### 2.1 TOs por clase de la partición y por categoría (R1)")
    A("")
    A("| clase · categoría | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    claves = sorted(set(c1["R1_tos_por_clase_y_categoria"]) | set(cd["R1_tos_por_clase_y_categoria"])
                    | set(c0["R1_tos_por_clase_y_categoria"]))
    for k in claves:
        A(f"| {k} | " + " | ".join(fmt(C[n]["R1_tos_por_clase_y_categoria"].get(k, 0))
                                    for n in CONJUNTOS) + " |")
    A("| **total** | " + " | ".join(fmt(C[n]["tos"]) for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R1_tos_por_clase_y_categoria`, `R1_tos_por_clase`, `R1_tos_por_categoria`. "
      "Control: `inventario_resumen.json` → `por_categoria` da normativa_general 99 y "
      "regimen_informativo 53 para los 152.")
    A("")

    A("### 2.2 Páginas por rol (R2) y páginas por TO (R10)")
    A("")
    A("| rol | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    rs = sorted(set().union(*(C[n]["R2_paginas_por_rol"] for n in CONJUNTOS)))
    for r in rs:
        A(f"| {r} | " + " | ".join(
            frac(C[n]["R2_paginas_por_rol"].get(r, 0), C[n]["R2_paginas_total"]) for n in CONJUNTOS)
          + " |")
    A("| **páginas** | " + " | ".join(fmt(C[n]["R2_paginas_total"]) for n in CONJUNTOS) + " |")
    for k, et in (("minimo", "páginas por TO: mínimo"), ("mediana", "páginas por TO: mediana"),
                  ("maximo", "páginas por TO: máximo")):
        A(f"| {et} | " + " | ".join(fmt(C[n]["R10_paginas_por_to"][k]) for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R2_paginas_por_rol`, `R2_paginas_total`, `R10_paginas_por_to`.")
    A("")

    A("### 2.3 Unidades por tipo y por profundidad (R3, R4)")
    A("")
    A("| | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    for t in ("punto_terminal", "mini_chunk", "seccion_sin_puntos"):
        A(f"| tipo {t} | " + " | ".join(
            frac(C[n]["R3_unidades_por_tipo"].get(t, 0), C[n]["R3_unidades_total"])
            for n in CONJUNTOS) + " |")
    for r in sorted(set().union(*(C[n]["R3_mini_chunks_por_rol"] for n in CONJUNTOS))):
        A(f"| · mini_chunk {r} | " + " | ".join(
            fmt(C[n]["R3_mini_chunks_por_rol"].get(r, 0)) for n in CONJUNTOS) + " |")
    A("| unidades de sub-chunking (incluidas arriba) | " + " | ".join(
        fmt(C[n]["R3_unidades_sub_chunk"]) for n in CONJUNTOS) + " |")
    ps = sorted(set().union(*(C[n]["R4_unidades_por_profundidad"] for n in CONJUNTOS)))
    for p in ps:
        A(f"| profundidad {p} | " + " | ".join(
            frac(C[n]["R4_unidades_por_profundidad"].get(p, 0), C[n]["R3_unidades_total"])
            for n in CONJUNTOS) + " |")
    A("| **unidades** | " + " | ".join(fmt(C[n]["R3_unidades_total"]) for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R3_unidades_por_tipo`, `R3_mini_chunks_por_rol`, `R3_unidades_sub_chunk`, "
      "`R4_unidades_por_profundidad`; el cruce tipo × profundidad está en "
      "`R4_unidades_por_tipo_y_profundidad`.")
    A("")

    A("### 2.4 Tablas y fórmulas (R5, R13)")
    A("")
    A("| | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    tb = {n: C[n]["R5_tablas"] for n in CONJUNTOS}
    A("| tablas lógicas parseadas | " + " | ".join(
        fmt(tb[n]["tablas_logicas_parseadas"]) for n in CONJUNTOS) + " |")
    A("| tablas lógicas detectadas (`conteos_b584`) | " + " | ".join(
        fmt(tb[n]["tablas_logicas_detectadas_conteos_b584"]) for n in CONJUNTOS) + " |")
    A("| chunks con `contenido_tabular` | " + " | ".join(
        frac(tb[n]["chunks_contenido_tabular"], tb[n]["denominador_chunks"]) for n in CONJUNTOS) + " |")
    A("| chunks con `formula` | " + " | ".join(
        frac(tb[n]["chunks_formula"], tb[n]["denominador_chunks"]) for n in CONJUNTOS) + " |")
    A("| TOs con tabla lógica parseada (a) | " + " | ".join(
        "—" if C[n]["R13_tos_con_tablas_logicas_parseadas"] is None else
        frac(len(C[n]["R13_tos_con_tablas_logicas_parseadas"]), C[n]["tos"]) for n in CONJUNTOS) + " |")
    A("| TOs con chunk `contenido_tabular` (b) | " + " | ".join(
        frac(len(C[n]["R13_tos_con_chunk_contenido_tabular"]), C[n]["tos"]) for n in CONJUNTOS) + " |")
    A("| TOs con chunk `formula` | " + " | ".join(
        frac(len(C[n]["R13_tos_con_chunk_formula"]), C[n]["tos"]) for n in CONJUNTOS) + " |")
    A("| TOs con línea de encabezado de anexo | " + " | ".join(
        frac(len(C[n]["R13_tos_con_linea_anexo"]), C[n]["tos"]) for n in CONJUNTOS) + " |")
    A("")
    tc = cd["R5_tablas"]["testigo_capmin_b583"]
    A(f"Desarrollo: no hay archivos `tablas_*` en la E0 de r1 ni en la de la tanda 0 (§6); el "
      f"testigo de B5.8.3 sobre `cap` "
      f"tiene {fmt(tc['tablas_logicas'])} tablas lógicas, {fmt(tc['parseadas'])} parseadas "
      f"(`{TESTIGO_CAPMIN}` → `conteos`); para `cla`, `ext`, `pro` y `ric`: NO ENCONTRADO. "
      "Claves: `R5_tablas`, `R13_*`.")
    A("")
    for n in CONJUNTOS:
        A(f"- {n}, TOs con fórmula: {', '.join('`'+x+'`' for x in C[n]['R13_tos_con_chunk_formula']) or 'ninguno'}.")
    for n in CONJUNTOS:
        A(f"- {n}, TOs con encabezado de anexo: "
          f"{', '.join('`'+x+'`' for x in C[n]['R13_tos_con_linea_anexo']) or 'ninguno'}.")
    A("")

    A("### 2.5 Largo de unidad en caracteres (R6)")
    A("")
    A("| medida | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    for campo, et in (("R6_largo_chars_propio", "propio"), ("R6_largo_chars_completo", "completo")):
        for k in ("minimo", "p10", "p25", "mediana", "p75", "p90", "p99", "maximo"):
            A(f"| {et}: {k} | " + " | ".join(fmt(C[n][campo][k]) for n in CONJUNTOS) + " |")
    A("| n (unidades) | " + " | ".join(fmt(C[n]["R6_largo_chars_propio"]["n"]) for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R6_largo_chars_propio`, `R6_largo_chars_completo`, `R6_largo_chars_propio_por_tipo`.")
    A("")

    A("### 2.6 Estructura de la numeración (R11, R12)")
    A("")
    A("| | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    A("| profundidad máxima del conjunto | " + " | ".join(
        fmt(C[n]["R11_profundidad_maxima_del_conjunto"]) for n in CONJUNTOS) + " |")
    pm = sorted(set().union(*(C[n]["R11_profundidad_maxima_por_to_distribucion"] for n in CONJUNTOS)))
    for p in pm:
        A(f"| TOs con profundidad máxima {p} | " + " | ".join(
            frac(C[n]["R11_profundidad_maxima_por_to_distribucion"].get(p, 0), C[n]["tos"])
            for n in CONJUNTOS) + " |")
    A("| puntos terminales | " + " | ".join(
        frac(C[n]["R12_puntos_terminales"], C[n]["R12_puntos_total"]) for n in CONJUNTOS) + " |")
    A("| puntos contenedores | " + " | ".join(
        frac(C[n]["R12_puntos_contenedores"], C[n]["R12_puntos_total"]) for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R11_profundidad_maxima_por_to_distribucion`, `R11_profundidad_maxima_del_conjunto`, "
      "`R12_*`; por TO, `por_to.<to>.profundidad_maxima`.")
    A("")

    A("### 2.7 Remisiones (R8)")
    A("")
    A("| | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    for k, et in (("internas", "internas (al mismo TO)"), ("externas", "externas (norma nombrada)"),
                  ("externas_anaforicas", "externas anafóricas («dicho ordenamiento»)"),
                  ("internas_con_normas_de", "sensibilidad: internas con «normas de» después")):
        A(f"| {et} | " + " | ".join(fmt(C[n]["R8_remisiones_total"].get(k, 0)) for n in CONJUNTOS) + " |")
    A("| unidades con alguna remisión | " + " | ".join(
        frac(C[n]["R8_unidades_con_remision"].get("con_alguna", 0), C[n]["R3_unidades_total"])
        for n in CONJUNTOS) + " |")
    for k, et in (("R8_internas_por_to_resumen", "internas"), ("R8_externas_por_to_resumen", "externas")):
        for q in ("minimo", "mediana", "maximo"):
            A(f"| {et} por TO: {q} | " + " | ".join(fmt(C[n][k][q]) for n in CONJUNTOS) + " |")
        A(f"| TOs con alguna {et[:-1]} | " + " | ".join(
            frac(C[n][k]["tos_con_alguna"], C[n]["tos"]) for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R8_remisiones_total`, `R8_unidades_con_remision`, `R8_remisiones_por_to`, "
      "`R8_internas_por_to_resumen`, `R8_externas_por_to_resumen`.")
    A("")

    A("### 2.8 Marcadores deónticos (R9)")
    A("")
    A("| marcador | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    for mk in DEONTICOS:
        A(f"| «{mk}»: ocurrencias | " + " | ".join(
            fmt(C[n]["R9_deonticos_ocurrencias"].get(mk, 0)) for n in CONJUNTOS) + " |")
        A(f"| «{mk}»: unidades con ≥ 1 | " + " | ".join(
            frac(C[n]["R9_deonticos_unidades_con_al_menos_una"].get(mk, 0), C[n]["R3_unidades_total"])
            for n in CONJUNTOS) + " |")
    A("| caracteres (`chars_propio`) | " + " | ".join(
        fmt(C[n]["R9_chars_propio_total"]) for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R9_deonticos_ocurrencias`, `R9_deonticos_unidades_con_al_menos_una`, "
      "`R9_chars_propio_total`.")
    A("")

    A("### 2.9 Tabla de origen de las disposiciones (R14) y procedencia (R15)")
    A("")
    A("| | corpus_152 | desarrollo_5 | tanda0_5 |")
    A("|---|--:|--:|--:|")
    A("| TOs con tabla de origen | " + " | ".join(
        frac(len(C[n]["R14_tos_con_tabla_norma_origen"]), C[n]["tos"]) for n in CONJUNTOS) + " |")
    A("| TOs con «última comunicación incorporada» legible | " + " | ".join(
        frac(C[n]["R15_procedencia_cobertura"]["con_portada_comunicacion"], C[n]["tos"])
        for n in CONJUNTOS) + " |")
    A("| TOs con «texto ordenado al» | " + " | ".join(
        frac(C[n]["R15_procedencia_cobertura"]["con_texto_ordenado_al"], C[n]["tos"])
        for n in CONJUNTOS) + " |")
    A("| TOs con portada ilegible por glifos | " + " | ".join(
        frac(len(C[n]["R15_procedencia_cobertura"]["portada_ilegible_por_glifos"]), C[n]["tos"])
        for n in CONJUNTOS) + " |")
    A("")
    A("Claves: `R14_tos_con_tabla_norma_origen`, `R15_procedencia_cobertura`; por TO, "
      "`por_to.<to>.{portada_comunicacion,texto_ordenado_al}`. La sonda leyó los PDF de "
      "`escalado_prep/pdfs/` y los del subset (`data/experiment/subset/`): "
      "`job_actualizacion/code/sonda_procedencia.py`, función `objetivo`.")
    A("")

    # §3 por TO
    A("## 3. Por TO: conjunto de desarrollo y conjunto de la tanda 0")
    A("")
    A("| TO | categoría | pág. | tabla de origen (pág.) | unidades | prof. máx. | "
      "puntos term./cont. | remisiones int./ext. | deberán | no podrán | salvo | excepto | "
      "última com. incorporada | texto ordenado al |")
    A("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|---|")
    for n in ("desarrollo_5", "tanda0_5"):
        for to, v in C[n]["por_to"].items():
            r = v["remisiones"]
            d = v["deonticos"]
            com = v["portada_comunicacion"] or ("ilegible (glifos)" if v["portada_ilegible_por_glifos"]
                                                else "sin dato")
            A(f"| `{to}` | {v['categoria']} | {fmt(v['paginas'])} | "
              f"{fmt(v['tabla_norma_origen_paginas'])} | {fmt(v['unidades'])} | "
              f"{fmt(v['profundidad_maxima'])} | {fmt(v['puntos_terminales'])}/"
              f"{fmt(v['puntos_contenedores'])} | {fmt(r.get('internas', 0))}/"
              f"{fmt(r.get('externas', 0) + r.get('externas_anaforicas', 0))} | "
              f"{fmt(d.get('deberán', 0))} | {fmt(d.get('no podrán', 0))} | {fmt(d.get('salvo', 0))} | "
              f"{fmt(d.get('excepto', 0))} | {com} | {v['texto_ordenado_al'] or 'sin dato'} |")
    A("")
    A("Clave: `conjuntos.<conjunto>.por_to.<to>`. «ext.» suma externas y anafóricas. Los 152, "
      "por TO, están en `conjuntos.corpus_152.por_to`.")
    A("")

    # §4 grafos
    A("## 4. Grafos (R16)")
    A("")
    g0, g1 = res["grafos"]["KG-Tanda0-Desarrollo-r1"], res["grafos"]["KG-Reextraído-r1"]
    A("| | KG-Tanda0-Desarrollo-r1 | KG-Reextraído-r1 |")
    A("|---|--:|--:|")
    A(f"| sha256 | `{g0['sha256'][:16]}…` | `{g1['sha256'][:16]}…` |")
    A(f"| nodos | {fmt(g0['nodos'])} | {fmt(g1['nodos'])} |")
    A(f"| aristas | {fmt(g0['aristas'])} | {fmt(g1['aristas'])} |")
    A(f"| tipos de nodo | {fmt(g0['tipos_de_nodo'])} | {fmt(g1['tipos_de_nodo'])} |")
    A(f"| tipos de relación | {fmt(g0['tipos_de_relacion'])} | {fmt(g1['tipos_de_relacion'])} |")
    A("")
    A("Nodos por tipo:")
    A("")
    A("| tipo | KG-Tanda0-Desarrollo-r1 | KG-Reextraído-r1 |")
    A("|---|--:|--:|")
    for k in sorted(set(g0["nodos_por_tipo"]) | set(g1["nodos_por_tipo"])):
        A(f"| {k} | {fmt(g0['nodos_por_tipo'].get(k, 0))} | {fmt(g1['nodos_por_tipo'].get(k, 0))} |")
    A("")
    A("Aristas por predicado:")
    A("")
    A("| predicado | KG-Tanda0-Desarrollo-r1 | KG-Reextraído-r1 |")
    A("|---|--:|--:|")
    for k in sorted(set(g0["aristas_por_relacion"]) | set(g1["aristas_por_relacion"])):
        A(f"| {k} | {fmt(g0['aristas_por_relacion'].get(k, 0))} | "
          f"{fmt(g1['aristas_por_relacion'].get(k, 0))} |")
    A("")
    A(f"Rutas: `{g0['ruta']}`, `{g1['ruta']}`. Clave: `grafos`. Sha completos en el JSON. "
      "Recómputo de una línea:")
    A("")
    A("```bash")
    A("python3 -c \"import json,collections; g=json.load(open('" + KG_R1 + "')); "
      "print(len(g['nodes']), len(g['edges']), dict(collections.Counter(n['type'] for n in g['nodes'])))\"")
    A("```")
    A("")

    # §5 fuentes
    A("## 5. Fuentes principales (sha256)")
    A("")
    A("| archivo | sha256 |")
    A("|---|---|")
    for k, v in res["fuentes_principales"].items():
        A(f"| `{k}` | `{v}` |")
    A("")
    A(f"Los sha256 de los {fmt(len(res['fuentes_por_to']))} archivos `chunks_<to>.json` y "
      "`estructura_<to>.json` leídos están en la clave `fuentes_por_to`.")
    A("")

    # §6 controles
    ct = res["controles"]
    A("## 6. Controles de consistencia")
    A("")
    ok_t0 = all(ct["tanda0_5_b584_igual_salida_tanda0"].values())
    ok_dev = all(ct["desarrollo_5_salida_tanda0_igual_salida_enm01"].values())
    A(f"- tanda0_5: `b584_particion/<to>/` y `salida_tanda0/` byte-idénticos (chunks y "
      f"estructura): {fmt(ok_t0)}.")
    A(f"- desarrollo_5: `salida_tanda0/` y `salida_enm01/` (E0 de KG-Reextraído-r1) byte-idénticos: "
      f"{fmt(ok_dev)}.")
    A(f"- Unidades contadas distintas de `unidades_extraccion` / `chunks` de los conteos: "
      f"{len(ct['unidades_distintas_de_conteos'])} TOs.")
    A(f"- `chars_propio` == `len(texto)` en todas las unidades: "
      f"{fmt(all(C[n]['R6_chars_propio_igual_len_texto'] for n in CONJUNTOS))}.")
    A(f"- TOs del grupo `inventariado_152` de la sonda iguales a los 152 de la partición: "
      f"{fmt(ct['sonda_grupo_152_igual_particion'])}.")
    dp = ct["paginas_sonda_distintas_de_e0"]
    A(f"- Páginas de la sonda distintas de las de E0: {len(dp)} TOs"
      + (": " + ", ".join(f"`{k}` (E0 {fmt(v[0])}, sonda {fmt(v[1])})" for k, v in dp.items())
         if dp else "") + ".")
    dt = ct["puntos_terminales_estructura_vs_chunks"]
    du = ct["puntos_terminales_estructura_vs_unidades_distintas"]
    todos_sub = all(v["chunks_punto_terminal_sub_chunk"] > 0 for v in dt.values())
    A(f"- Puntos sin hijos de la estructura contra chunks `punto_terminal`: difieren en {len(dt)} "
      "TOs"
      + (" (" + ", ".join(f"`{k}` {fmt(v['estructura_puntos_sin_hijos'])} contra "
                          f"{fmt(v['chunks_punto_terminal'])}" for k, v in dt.items()) + ")"
         if dt else "")
      + f"; todos con partes de sub-chunking: {fmt(todos_sub)}. Contra las unidades distintas de "
        "esos chunks (las partes de una misma unidad cuentan una vez), esos TOs coinciden: "
        f"{fmt(not (set(dt) & set(du)))}; difieren en cambio otros {len(du)} TOs"
      + (" (" + ", ".join(f"`{k}` {fmt(v[1])} contra {fmt(v[0])}" for k, v in du.items()) + ")"
         if du else "")
      + ", explicados en el punto siguiente. Por eso R12 (estructura) y R3 (chunks) no dan el "
        "mismo número de terminales en corpus_152. Claves "
        "`controles.puntos_terminales_estructura_vs_chunks` y "
        "`controles.puntos_terminales_estructura_vs_unidades_distintas`.")
    rp = ct["ids_de_chunk_repetidos"]
    A(f"- Ids de chunk repetidos dentro de un mismo TO: {len(rp)} TOs, "
      f"{fmt(sum(v['chunks_de_mas'] for v in rp.values()))} chunks de más"
      + (" (" + ", ".join(f"`{k}` {fmt(v['chunks_de_mas'])}" for k, v in rp.items()) + ")"
         if rp else "")
      + f"; con el mismo texto: {fmt(sum(v['ids_con_mismo_texto'] for v in rp.values()))}. Son "
        "colisiones de numeración (texto distinto bajo el mismo `id`), no chunks duplicados; "
        "las 9.324 unidades las incluyen. La diferencia que queda entre puntos sin hijos de la "
        "estructura y unidades distintas es igual, TO por TO, a esos chunks de más: "
        f"{fmt(ct['diferencia_terminales_explicada_por_ids_repetidos'])}. Claves "
        "`controles.ids_de_chunk_repetidos` y "
        "`controles.diferencia_terminales_explicada_por_ids_repetidos`.")
    A(f"- Archivos `tablas_*` en `salida_enm01/` y `salida_tanda0/`: "
      f"{len(ct['archivos_tablas_en_salida_enm01_y_salida_tanda0'])}.")
    A("")

    # §7 límites
    A("## 7. Límites y NO ENCONTRADO")
    A("")
    A("- Clase de la partición para desarrollo_5: no aplica (no están en `particion_152.json`).")
    A("- Tablas lógicas de `cla`, `ext`, `pro` y `ric`: NO ENCONTRADO (sin archivos `tablas_*` "
      "en la E0 de r1; solo `cap` tiene testigo de B5.8.3).")
    A("- Remisiones: detector por regex sobre el texto de E0, sin resolución del destino; "
      "«externa» no garantiza otro TO. No es el conteo de aristas `referencia` de los grafos.")
    A("- Anexos: cota inferior (solo encabezados de anexo que quedaron dentro de chunks de E0).")
    A("- Procedencia: TOs sin portada legible quedan sin dato; no se infiere desde el pie.")
    A("")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--out-dir", default=str(AQUI))
    args = ap.parse_args()
    out = Path(args.out_dir)

    conjuntos, fuentes_por_to = cargar_conjuntos()
    sonda = cargar(SONDA)
    res = {
        "unidad": "U-INSUMOS-CAP I1",
        "comando": CMD,
        "cifras_publicadas": cifras_publicadas(conjuntos),
        "conjuntos": {n: estadisticas_conjunto(n, conjuntos[n], sonda) for n in CONJUNTOS},
        "grafos": {"KG-Tanda0-Desarrollo-r1": estadisticas_grafo(KG_T0_DEV),
                   "KG-Reextraído-r1": estadisticas_grafo(KG_R1)},
        "controles": controles(conjuntos, sonda),
        "fuentes_principales": {r: sha256(r) for r in (
            PARTICION, CONTEOS_B584, REPORTE_B584, CONTEOS_T0, INVENTARIO_RESUMEN,
            INVENTARIO_CSV, INDICE_OFICIAL, MANIFIESTO_DEV, SONDA, TESTIGO_CAPMIN,
            KG_T0_DEV, KG_R1)},
        "fuentes_por_to": dict(sorted(fuentes_por_to.items())),
    }
    (out / "estadisticas_corpus.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    (out / "estadisticas_corpus.md").write_text(md(res), encoding="utf-8")
    cp = res["cifras_publicadas"]
    print("cifras publicadas:", cp["publicada"], "coinciden:", cp["coinciden"])
    return 0 if cp["coinciden"] else 1


if __name__ == "__main__":
    sys.exit(main())
