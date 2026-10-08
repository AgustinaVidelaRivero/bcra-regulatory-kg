"""VERIF-FORMAS-SEG — los ocho grupos de formas del capítulo 3 contados sobre el texto completo de los
157 TOs, sin depender de la segmentación (solo lectura, USD 0, sin API).

Uso (desde la raíz del repo; escribe solo en --out-dir, que debe existir):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B <este script> --out-dir <dir>
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B <este script> --out-dir <dir> --pdftotext

Salida: <out-dir>/recuento_formas_texto_completo.json. Determinístico: sin fechas ni rutas absolutas,
claves ordenadas. Sale con código 1 si un control da False.

Reglas:
  F0  Conjuntos = los de U-CAP3-DOC C1: corpus_152 = claves de particion_152.json['por_to'], con su PDF
      en escalado_prep/pdfs/<to>.pdf (sha256 contra manifest_pdfs.sha256); desarrollo_5 =
      desarrollo_5tos.json tos[], con su PDF en tos[].pdf (sha256 contra tos[].sha256_pdf).
  F1  Texto = la lectura del PDF que usa la segmentación: extraer_lineas de e0_lib.py (palabras de
      pdfplumber agrupadas por renglón), tomada del blob de COMMIT_E0 y controlada por el sha256 de la
      función, que es el mismo en COMMIT_VERIF. Renglones unidos con "\\n" y páginas unidas con "\\n":
      TODAS las páginas y TODOS los renglones (portada, índice, tabla de norma de origen, historial,
      encabezados y pies de página incluidos).
  F2  Normalización = R7 de U-INSUMOS-CAP I1 (u_insumos_i1.py:159-161): se quita cada "-\\n" y \\s+ → " ".
  F3  Expresiones = las de C1 (u_cap3_doc_c1.py:73-86, re.I); permiso = «podrá(n)» sin «no» entre las
      tres palabras (\\w+) anteriores (:89; negado() y coincidencias(), :163-171). En el texto
      completo la ventana de
      tres palabras corre sobre el texto continuo, no dentro de una unidad. La negación se evalúa con
      los finales de palabra precomputados (negado_rapido); es exacta porque cada «podrá» empieza en
      un límite de palabra, y el control F3b la compara con negado() en todas las unidades de C1.
  F4  Ocurrencias = coincidencias no superpuestas de finditer. Cada una se atribuye a la página donde
      empieza y al rol que la segmentación le dio a esa página, reconstruido con las funciones del
      mismo blob y el camino de cada TO: en los 152, el de correr_b584.py:111-148 (78a757c), elegido
      por modo_lectura de conteos_b584.json (vigente: clasificar_paginas; marcadores:
      clasificar_paginas con marcadores_b582; sin_raiz: roles_para_modo_sin_raiz sobre esa última);
      en desarrollo, clasificar_paginas por defecto (correr_e0.py:233-234, 47c9283). Control F4b: por
      TO, el conteo de roles y de páginas es igual a roles_pagina y paginas de conteos_b584.json y de
      salida_tanda0/conteos.json.
  F5  Control de equivalencia: el mismo conteo, sobre el texto propio de las unidades que leyó C1
      (b584_particion/<to>/chunks_<to>.json y salida_tanda0/chunks_<to>.json), da las cifras de C1.
  F6  Con --pdftotext, la misma cuenta sobre la salida de `pdftotext -enc UTF-8 <pdf> -` (modo por
      defecto), para comparar con el recálculo del 01/10/2026.
  F7  Serie solo cuerpo (series.texto_completo_e0_solo_cuerpo): las ocurrencias de F4 que empiezan en
      una página con rol «cuerpo», en total y por conjunto. Por TO: el rol de cada página en rangos
      (paginas_por_rol_rangos, páginas del PDF desde 1) y la fuente de ese rol (fuente_rol: el camino,
      el archivo de conteos con sus claves, el código que eligió el camino y las funciones que lo
      calculan). Control F7: la serie es igual a la suma por TO y a por_rol_157.cuerpo.
"""

from __future__ import annotations

import argparse
import ast
import collections
import hashlib
import json
import re
import subprocess
import sys
import types
from array import array
from bisect import bisect_right
from pathlib import Path

sys.dont_write_bytecode = True

EXP = "data/experiment"
PARTICION = f"{EXP}/segmentacion_84/b584_particion/particion_152.json"
B584 = f"{EXP}/segmentacion_84/b584_particion"
T0 = f"{EXP}/reextraccion_v2/e0_chunking/salida_tanda0"
CONTEOS_B584 = f"{B584}/conteos_b584.json"
CONTEOS_T0 = f"{T0}/conteos.json"
MANIFIESTO_DEV = f"{EXP}/reextraccion_v2/manifiestos/desarrollo_5tos.json"
PDFS_152 = f"{EXP}/escalado_prep/pdfs"
MANIFIESTO_PDFS = f"{EXP}/escalado_prep/manifest_pdfs.sha256"
E0_LIB = f"{EXP}/reextraccion_v2/e0_chunking/e0_lib.py"
I1_PY = "reports/u_insumos_cap/u_insumos_i1.py"
C1_PY = "reports/u_cap3_doc/u_cap3_doc_c1.py"

# F1: el blob de e0_lib.py del cierre de B5.8.4 (78a757c), el código que produjo la partición; el
# mismo blob está en 47c9283, el de la E0 de desarrollo de salida_tanda0.
COMMIT_E0 = "78a757c"
SHA_E0_LIB_BLOB = "ba297f65f12a9075121baee76bf9e4cd664de9aeb9861b5d82967b3f81d65637"
SHA_EXTRAER_LINEAS = "9ee0e450baa538fc"
COMMIT_VERIF = "4dba33f"
# F2: el commit de I1 y la línea de R7.
COMMIT_I1 = "ded3494"
R7_FUENTE = 'return re.sub(r"\\s+", " ", texto.replace("-\\n", ""))'

ORDEN = ("deber", "prohibicion", "limite", "excepcion", "permiso", "condicion", "definicion",
         "remision_explicita")
# F3: copia literal de u_cap3_doc_c1.py:73-86 (solo las regex).
GRUPOS = {
    "deber": r"\bdeber[áa]n?\b",
    "prohibicion": r"\bno\s+podr[áa]n?\b",
    "limite": r"\bno\s+podr[áa]n?\s+(?:superar|exceder)\b",
    "excepcion": r"\bsalvo\b|\bexcepto\b|\bcon\s+excepci[óo]n\s+del?\b",
    "permiso": r"\bpodr[áa]n?\b",
    "condicion": r"\bsiempre\s+(?:que|y\s+cuando)\b",
    "definicion": r"\bse\s+entiende\s+por\b|\bse\s+entender[áa]\s+por\b|\bse\s+considera\b",
    "remision_explicita": r"\b(?:establecido|previsto|dispuesto)\s+en\s+el\s+punto\b",
}
VENTANA_NEGACION = 3
RX = {g: re.compile(p, re.I) for g, p in GRUPOS.items()}
PALABRA = re.compile(r"\w+")

# F5: cifras de C1 (c1_marcadores.json, conjuntos.*.ocurrencias), por conjunto.
C1_ESPERADO = {
    "corpus_152": {"deber": 5434, "prohibicion": 357, "limite": 85, "excepcion": 493,
                   "permiso": 1336, "condicion": 248, "definicion": 87, "remision_explicita": 657},
    "desarrollo_5": {"deber": 966, "prohibicion": 50, "limite": 6, "excepcion": 110,
                     "permiso": 363, "condicion": 63, "definicion": 12, "remision_explicita": 221},
}

ROLES = ("portada", "indice", "tabla_norma_origen", "historial", "ficha_registro", "cuerpo")

# F7: el código que eligió el rol de página y las funciones que lo calculan, por camino.
CODIGO_ROL_152 = f"{B584}/code/correr_b584.py:111-148 @ {COMMIT_E0}"
CODIGO_ROL_DEV = f"{EXP}/reextraccion_v2/e0_chunking/correr_e0.py:233-234 @ 47c9283"
FUNCIONES_ROL = {
    "vigente": f"e0_lib.clasificar_paginas(paginas) @ {COMMIT_E0}",
    "marcadores": f"e0_lib.clasificar_paginas(paginas, marcadores_b582=True) @ {COMMIT_E0}",
    "sin_raiz": (f"e0_lib.roles_para_modo_sin_raiz(paginas, "
                 f"clasificar_paginas(paginas, marcadores_b582=True)) @ {COMMIT_E0}"),
}


# ---------------------------------------------------------------- utilidades

def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", *args], cwd=repo, capture_output=True, check=True).stdout


def normalizar(texto: str) -> str:
    """F2 (R7)."""
    return re.sub(r"\s+", " ", texto.replace("-\n", ""))


def negado(texto: str, pos: int) -> bool:
    """F3, como C1: «no» entre las tres palabras anteriores."""
    return any(p.lower() == "no" for p in PALABRA.findall(texto[:pos])[-VENTANA_NEGACION:])


class Texto:
    """Texto normalizado con los finales de palabra precomputados (F3, negado_rapido)."""

    def __init__(self, texto: str):
        self.texto = texto
        self.fines = array("q")
        self.es_no = bytearray()
        for m in PALABRA.finditer(texto):
            self.fines.append(m.end())
            self.es_no.append(m.group().lower() == "no")

    def negado_rapido(self, pos: int) -> bool:
        k = bisect_right(self.fines, pos)
        return any(self.es_no[i] for i in range(max(0, k - VENTANA_NEGACION), k))

    def coincidencias(self, grupo: str) -> list[re.Match]:
        if grupo == "permiso":
            return [m for m in RX["permiso"].finditer(self.texto)
                    if not self.negado_rapido(m.start())]
        return list(RX[grupo].finditer(self.texto))

    def contar(self) -> dict:
        return {g: len(self.coincidencias(g)) for g in ORDEN}


def normalizar_con_mapa(raw: str) -> tuple[str, array]:
    """R7 con el índice del texto crudo de cada carácter de la salida (para F4)."""
    piezas, idx = [], array("q")
    i, n = 0, len(raw)
    while True:
        j = raw.find("-\n", i)
        if j < 0:
            piezas.append(raw[i:])
            idx.extend(range(i, n))
            break
        piezas.append(raw[i:j])
        idx.extend(range(i, j))
        i = j + 2
    inter = "".join(piezas)
    out, mapa, pos = [], array("q"), 0
    for m in re.finditer(r"\s+", inter):
        out.append(inter[pos:m.start()])
        mapa.extend(idx[pos:m.start()])
        out.append(" ")
        mapa.append(idx[m.start()])
        pos = m.end()
    out.append(inter[pos:])
    mapa.extend(idx[pos:])
    return "".join(out), mapa


def bloque_extraer_lineas(texto: str) -> str:
    m = re.search(r"^def extraer_lineas.*?(?=^# -{60} roles de página)", texto, re.S | re.M)
    return sha256_bytes(m.group(0).encode("utf-8"))[:16]


def cargar_e0(repo: Path) -> tuple[types.ModuleType, dict]:
    """F1: e0_lib.py del blob de COMMIT_E0, ejecutado en memoria (nada se escribe)."""
    fuente = git(repo, "show", f"{COMMIT_E0}:{E0_LIB}")
    texto = fuente.decode("utf-8")
    texto_verif = git(repo, "show", f"{COMMIT_VERIF}:{E0_LIB}").decode("utf-8")
    mod = types.ModuleType("e0_lib_" + COMMIT_E0)
    sys.modules[mod.__name__] = mod
    exec(compile(texto, f"{COMMIT_E0}:{E0_LIB}", "exec"), mod.__dict__)
    return mod, {"commit": COMMIT_E0, "ruta": E0_LIB, "sha256_blob": sha256_bytes(fuente),
                 "sha256_extraer_lineas_16": bloque_extraer_lineas(texto),
                 "commit_comparado": COMMIT_VERIF,
                 "sha256_extraer_lineas_16_en_commit_comparado": bloque_extraer_lineas(texto_verif),
                 "TOL_TOP": mod.TOL_TOP}


def control_r7(repo: Path) -> dict:
    lin = git(repo, "show", f"{COMMIT_I1}:{I1_PY}").decode("utf-8").splitlines()
    k = next(i for i, l in enumerate(lin) if l.startswith("def normalizar("))
    return {"commit": COMMIT_I1, "ruta": I1_PY, "linea_def": k + 1,
            "misma_regla": lin[k + 2].strip() == R7_FUENTE}


def control_c1(repo: Path) -> dict:
    """F3: las regex y la ventana de este script son las de C1, si el archivo de C1 está."""
    p = repo / C1_PY
    if not p.exists():
        return {"ruta": C1_PY, "presente": False}
    src = p.read_text(encoding="utf-8")
    grupos, ventana = None, None
    for nodo in ast.parse(src).body:
        if isinstance(nodo, ast.Assign) and getattr(nodo.targets[0], "id", None) == "GRUPOS":
            grupos = {k: v[1] for k, v in ast.literal_eval(nodo.value).items()}
        if isinstance(nodo, ast.Assign) and getattr(nodo.targets[0], "id", None) == "VENTANA_NEGACION":
            ventana = ast.literal_eval(nodo.value)
    return {"ruta": C1_PY, "presente": True, "sha256": sha256_bytes(p.read_bytes()),
            "mismas_regex": grupos == GRUPOS, "misma_ventana": ventana == VENTANA_NEGACION}


def conjuntos(repo: Path) -> tuple[list[dict], dict]:
    """F0: (conjunto, to, pdf, sha esperado) de los 157 y el sha de las listas."""
    fuentes = {}
    for rel in (PARTICION, MANIFIESTO_DEV, MANIFIESTO_PDFS, CONTEOS_B584, CONTEOS_T0):
        fuentes[rel] = sha256_bytes((repo / rel).read_bytes())
    conteos_b584 = json.loads((repo / CONTEOS_B584).read_text(encoding="utf-8"))
    conteos_t0 = json.loads((repo / CONTEOS_T0).read_text(encoding="utf-8"))
    esperado = {}
    for l in (repo / MANIFIESTO_PDFS).read_text(encoding="utf-8").splitlines():
        sha, nombre = l.split(maxsplit=1)
        esperado[nombre.strip()] = sha
    tos = []
    por_to = json.loads((repo / PARTICION).read_text(encoding="utf-8"))["por_to"]
    for to in sorted(por_to):
        c = conteos_b584[to]
        tos.append({"conjunto": "corpus_152", "to": to, "pdf": f"{PDFS_152}/{to}.pdf",
                    "sha256_esperado": esperado[f"{to}.pdf"],
                    "chunks": f"{B584}/{to}/chunks_{to}.json",
                    "camino": c["modo_lectura"], "roles_pagina": c["roles_pagina"],
                    "paginas": c["paginas"],
                    "fuente_rol": {"camino": c["modo_lectura"], "conteos": CONTEOS_B584,
                                   "claves": [f"{to}.modo_lectura", f"{to}.roles_pagina",
                                              f"{to}.paginas"],
                                   "codigo": CODIGO_ROL_152,
                                   "funciones": FUNCIONES_ROL[c["modo_lectura"]]}})
    dev = json.loads((repo / MANIFIESTO_DEV).read_text(encoding="utf-8"))["tos"]
    for t in sorted(dev, key=lambda t: t["id"]):
        c = conteos_t0[t["id"]]
        tos.append({"conjunto": "desarrollo_5", "to": t["id"], "pdf": t["pdf"],
                    "sha256_esperado": t["sha256_pdf"],
                    "chunks": f"{T0}/chunks_{t['id']}.json",
                    "camino": "vigente", "roles_pagina": c["roles_pagina"],
                    "paginas": c["paginas"],
                    "fuente_rol": {"camino": "vigente", "conteos": CONTEOS_T0,
                                   "claves": [f"{t['id']}.roles_pagina", f"{t['id']}.paginas"],
                                   "codigo": CODIGO_ROL_DEV,
                                   "funciones": FUNCIONES_ROL["vigente"]}})
    return tos, fuentes


# ---------------------------------------------------------------- recuentos

def contar_segmentacion(repo: Path, tos: list[dict]) -> tuple[dict, dict, str, dict]:
    """F5 y F3b: el conteo sobre el texto propio de las unidades de C1."""
    tot = {c: collections.Counter() for c in C1_ESPERADO}
    por_to = {}
    lista = []
    negacion = {"podra_evaluadas": 0, "distintas": 0}
    for t in tos:
        b = (repo / t["chunks"]).read_bytes()
        lista.append(f"{sha256_bytes(b)}  {t['chunks']}\n")
        ct = collections.Counter()
        for ch in json.loads(b.decode("utf-8")):
            tx = Texto(normalizar(ch["texto"]))
            ct.update(tx.contar())
            for m in RX["permiso"].finditer(tx.texto):
                negacion["podra_evaluadas"] += 1
                if tx.negado_rapido(m.start()) != negado(tx.texto, m.start()):
                    negacion["distintas"] += 1
        tot[t["conjunto"]].update(ct)
        por_to[t["to"]] = {g: ct[g] for g in ORDEN}
    sha_lista = sha256_bytes("".join(sorted(lista)).encode("utf-8"))
    return {c: {g: tot[c][g] for g in ORDEN} for c in tot}, por_to, sha_lista, negacion


def roles_de_la_segmentacion(e0, paginas, camino: str) -> list[str]:
    """F4: el rol de cada página en el camino que tomó la segmentación."""
    if camino == "vigente":
        return e0.clasificar_paginas(paginas)
    roles_m = e0.clasificar_paginas(paginas, marcadores_b582=True)
    if camino == "marcadores":
        return roles_m
    if camino == "sin_raiz":
        return e0.roles_para_modo_sin_raiz(paginas, roles_m)
    raise SystemExit(f"camino desconocido: {camino}")


def rangos_por_rol(roles: list[str]) -> dict:
    """F7: las páginas (desde 1) de cada rol, como rangos «a-b» separados por coma."""
    out = {}
    for rol in ROLES:
        pags = [i + 1 for i, r in enumerate(roles) if r == rol]
        if not pags:
            continue
        tramos, a, b = [], pags[0], pags[0]
        for q in pags[1:]:
            if q == b + 1:
                b = q
            else:
                tramos.append((a, b))
                a = b = q
        tramos.append((a, b))
        out[rol] = ",".join(str(a) if a == b else f"{a}-{b}" for a, b in tramos)
    return out


def contar_texto_completo(e0, pdf: Path, camino: str) -> dict:
    """F1-F4 para un TO."""
    paginas = e0.extraer_lineas(pdf)
    roles = roles_de_la_segmentacion(e0, paginas, camino)
    textos = ["\n".join(l.texto for l in lineas) for lineas in paginas]
    n_paginas, n_renglones = len(paginas), sum(len(p) for p in paginas)
    del paginas
    inicios, pos = [], 0
    for tx in textos:
        inicios.append(pos)
        pos += len(tx) + 1
    raw = "\n".join(textos)
    del textos
    norm, mapa = normalizar_con_mapa(raw)
    if norm != normalizar(raw):
        raise SystemExit(f"normalizar_con_mapa distinto de R7 en {pdf.name}")
    del raw
    tx = Texto(norm)
    total = {}
    por_rol = {r: collections.Counter() for r in ROLES}
    for g in ORDEN:
        ms = tx.coincidencias(g)
        total[g] = len(ms)
        for m in ms:
            por_rol[roles[bisect_right(inicios, mapa[m.start()]) - 1]][g] += 1
    podras = list(RX["permiso"].finditer(norm))
    inicios_prohibicion = {m.start() for m in RX["prohibicion"].finditer(norm)}
    paginas_por_rol = collections.Counter(roles)
    return {
        "camino": camino,
        "paginas": n_paginas,
        "renglones": n_renglones,
        "caracteres_normalizados": len(norm),
        "paginas_por_rol": {r: paginas_por_rol[r] for r in ROLES},
        "paginas_por_rol_rangos": rangos_por_rol(roles),
        "ocurrencias": total,
        "ocurrencias_por_rol": {r: {g: por_rol[r][g] for g in ORDEN} for r in ROLES},
        "podra_total": len(podras),
        "podra_descartadas_por_no": sum(1 for m in podras if tx.negado_rapido(m.start())),
        "limite_fuera_de_prohibicion": sum(1 for m in RX["limite"].finditer(norm)
                                           if m.start() not in inicios_prohibicion),
    }


def pdftotext_version() -> str:
    r = subprocess.run(["pdftotext", "-v"], capture_output=True, text=True)
    return (r.stderr or r.stdout).splitlines()[0].strip()


def contar_pdftotext(pdf: Path) -> dict:
    """F6."""
    txt = subprocess.run(["pdftotext", "-enc", "UTF-8", str(pdf), "-"], capture_output=True,
                         check=True).stdout.decode("utf-8")
    return Texto(normalizar(txt)).contar()


def sumar(filas: list[dict]) -> dict:
    c = collections.Counter()
    for f in filas:
        c.update(f)
    return {g: c[g] for g in ORDEN}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out-dir", required=True)
    ap.add_argument("--pdftotext", action="store_true")
    args = ap.parse_args()
    repo = Path.cwd()
    out = Path(args.out_dir)
    if not out.is_dir():
        raise SystemExit(f"--out-dir no existe: {out}")

    import pdfminer
    import pdfplumber

    e0, info_e0 = cargar_e0(repo)
    tos, fuentes = conjuntos(repo)
    r7 = control_r7(repo)
    c1 = control_c1(repo)
    controles = {
        "F1_blob_e0_lib_esperado": info_e0["sha256_blob"] == SHA_E0_LIB_BLOB,
        "F1_extraer_lineas_igual_en_commit_comparado": (
            info_e0["sha256_extraer_lineas_16"]
            == info_e0["sha256_extraer_lineas_16_en_commit_comparado"] == SHA_EXTRAER_LINEAS),
        "F2_R7_igual_a_I1": r7["misma_regla"],
        "F3_regex_y_ventana_iguales_a_C1": ((c1["mismas_regex"] and c1["misma_ventana"])
                                            if c1["presente"] else "C1 ausente: no verificable"),
    }

    sha_pdfs, mal = {}, []
    for t in tos:
        sha = sha256_bytes((repo / t["pdf"]).read_bytes())
        sha_pdfs[t["pdf"]] = sha
        if sha != t["sha256_esperado"]:
            mal.append(t["pdf"])
    controles["F0_157_pdfs_con_sha_del_manifiesto"] = (len(tos) == 157 and not mal)

    seg_conj, seg_por_to, sha_chunks, negacion = contar_segmentacion(repo, tos)
    controles["F5_conteo_sobre_unidades_igual_a_C1"] = seg_conj == C1_ESPERADO
    controles["F3b_negacion_rapida_igual_a_negado_en_unidades"] = negacion["distintas"] == 0

    por_to = {}
    for t in tos:
        r = contar_texto_completo(e0, repo / t["pdf"], t["camino"])
        r["conjunto"] = t["conjunto"]
        r["fuente_rol"] = t["fuente_rol"]
        r["roles_igual_a_la_segmentacion"] = (
            {k: v for k, v in r["paginas_por_rol"].items() if v} == t["roles_pagina"]
            and r["paginas"] == t["paginas"])
        r["ocurrencias_segmentacion_C1"] = seg_por_to[t["to"]]
        if args.pdftotext:
            r["ocurrencias_pdftotext"] = contar_pdftotext(repo / t["pdf"])
        por_to[t["to"]] = r
        print(f"{t['to']}: {r['paginas']} pp.", file=sys.stderr, flush=True)

    def agregado(clave: str, conj: str | None = None) -> dict:
        return sumar([r[clave] for r in por_to.values() if conj is None or r["conjunto"] == conj])

    completo = {"total_157": agregado("ocurrencias"),
                "corpus_152": agregado("ocurrencias", "corpus_152"),
                "desarrollo_5": agregado("ocurrencias", "desarrollo_5"),
                "por_rol_157": {rol: sumar([r["ocurrencias_por_rol"][rol] for r in por_to.values()])
                                for rol in ROLES},
                "paginas_157": sum(r["paginas"] for r in por_to.values()),
                "paginas_por_rol_157": {rol: sum(r["paginas_por_rol"][rol] for r in por_to.values())
                                        for rol in ROLES},
                "podra_total_157": sum(r["podra_total"] for r in por_to.values()),
                "podra_descartadas_por_no_157": sum(r["podra_descartadas_por_no"]
                                                    for r in por_to.values())}
    def solo_cuerpo(conj: str | None = None) -> dict:
        return sumar([r["ocurrencias_por_rol"]["cuerpo"] for r in por_to.values()
                      if conj is None or r["conjunto"] == conj])

    cuerpo = {"total_157": solo_cuerpo(),
              "corpus_152": solo_cuerpo("corpus_152"),
              "desarrollo_5": solo_cuerpo("desarrollo_5"),
              "paginas_cuerpo_157": sum(r["paginas_por_rol"]["cuerpo"] for r in por_to.values())}
    controles["F7_solo_cuerpo_igual_a_la_suma_por_TO_y_al_rol_cuerpo"] = (
        cuerpo["total_157"] == completo["por_rol_157"]["cuerpo"]
        == sumar([cuerpo["corpus_152"], cuerpo["desarrollo_5"]]))
    controles["F4_roles_suman_el_total"] = (sumar(list(completo["por_rol_157"].values()))
                                            == completo["total_157"])
    controles["F4b_roles_y_paginas_iguales_a_los_conteos_de_la_segmentacion"] = all(
        r["roles_igual_a_la_segmentacion"] for r in por_to.values())
    controles["K3_permiso_mas_descartadas_igual_total"] = (
        completo["total_157"]["permiso"] + completo["podra_descartadas_por_no_157"]
        == completo["podra_total_157"])
    controles["K3_limite_dentro_de_prohibicion"] = all(r["limite_fuera_de_prohibicion"] == 0
                                                      for r in por_to.values())
    salida = {
        "unidad": "VERIF-FORMAS-SEG",
        "comando": ("PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B "
                    "reports/verificaciones_tesis/VERIF-FORMAS-SEG/recuento_formas_texto_completo.py "
                    "--out-dir <dir>" + (" --pdftotext" if args.pdftotext else "")),
        "orden_grupos": list(ORDEN),
        "regex": GRUPOS,
        "ventana_negacion_permiso": VENTANA_NEGACION,
        "fuentes": {"listas": fuentes, "pdfs_sha256": sha_pdfs,
                    "chunks_C1_sha256_de_la_lista_ordenada": sha_chunks,
                    "e0_lib": info_e0, "R7": r7, "C1": c1},
        "herramientas": {"python": sys.version.split()[0], "pdfplumber": pdfplumber.__version__,
                         "pdfminer": pdfminer.__version__},
        "series": {"C1_segmentacion": {"total_157": sumar(list(seg_conj.values())), **seg_conj},
                   "texto_completo_e0": completo,
                   "texto_completo_e0_solo_cuerpo": cuerpo},
        "negacion_en_unidades_C1": negacion,
        "por_to": por_to,
        "controles": controles,
        "pdfs_con_sha_distinto": mal,
    }
    if args.pdftotext:
        salida["herramientas"]["pdftotext"] = pdftotext_version()
        salida["series"]["pdftotext_defecto"] = {
            "total_157": agregado("ocurrencias_pdftotext"),
            "corpus_152": agregado("ocurrencias_pdftotext", "corpus_152"),
            "desarrollo_5": agregado("ocurrencias_pdftotext", "desarrollo_5")}
    (out / "recuento_formas_texto_completo.json").write_text(
        json.dumps(salida, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    fallos = [k for k, v in controles.items() if v is False]
    print("controles:", "OK" if not fallos else f"FALLAN {fallos}", file=sys.stderr)
    return 1 if fallos else 0


if __name__ == "__main__":
    raise SystemExit(main())
