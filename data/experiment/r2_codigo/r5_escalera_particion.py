"""U-R2-CODIGO, ajuste D antes de R5 — control de la escalera de E0 en e0-r2
sobre los 152 TOs de la partición del corpus escalado. USD 0.

Dos modos:
  --correr: corre `correr_e0.correr(..., version_e0="e0-r2")` sobre los TOs
     pedidos (`--tos`, por defecto los 152), con un manifiesto mínimo (ids,
     archivo y PDF de `escalado_prep/pdfs/`; sin oráculo). Escribe solo en
     `--salida`, que no puede estar dentro del repo.
  --comparar: compara, por TO, los ids de chunk de una o más salidas de e0-r2
     (`--salida`, repetible) con los de `segmentacion_84/b584_particion` y
     cuenta las diferencias por clase:
       - ids desambiguados: un id de la partición repetido dentro del TO, que
         e0-r2 renombra a `::rep<k>` (regla L);
       - partición por tamaño no aplicada por tabla: la partición tiene
         `<id>::parteK` y e0-r2 la unidad entera, declarada en `sub_chunking`
         como `tabla_serializada` (e0-r2 no parte una unidad con tabla);
       - otra: cualquier otra diferencia de ids (se lista).
     Y, entre los ids comunes, los chunks cuyo texto cambia, por clase:
     tablas (bloque [TABLA … FIN TABLA] de e0-r2), pies (solo se quitaron
     líneas de pie: criterio [c22] o `e0_lib.RE_PIE`), K (solo se agregaron
     líneas de encabezado conservadas por K) y otra (se lista).
     Controles: ningún TO que la partición segmenta queda en 0 chunks; el modo
     de lectura de e0-r2 es el de `conteos_b584.json`.
  --atribuir (con --comparar): para los TOs con diferencias de clase «otra»,
     vuelve a parsear el PDF en el modo de lectura del TO con las dos reglas
     nuevas de e0-r2 que actúan antes de los chunks (K y el pie desde la línea
     «Versión»), encendidas y apagadas, y atribuye: los ids, a la regla cuya
     ausencia reproduce los de la partición; las líneas de texto, a la regla
     que las quita o las conserva (registro de `separar_encabezado_pie` por
     variante). Lo que ninguna explica queda como «otra» y se lista. En un TO
     cuyos ids cambian por una regla, los chunks con id posicional
     (`::intersticial::N`) o que ceden líneas a una unidad nueva cambian de
     texto por arrastre: clase «<regla> (arrastre de un cambio de ids)».

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r5_escalera_particion.py --correr \
      --salida <dir del scratchpad> [--tos a,b,c]
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r5_escalera_particion.py --comparar \
      --salida <dir> [--salida <dir> …] --out <json>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
E0_DIR = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking"
PARTICION = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
PDFS = REPO / "data" / "experiment" / "escalado_prep" / "pdfs"
RE_C22 = re.compile(r"versi[oó]n\s*:.*comunicaci[oó]n", re.I)
RE_REP = re.compile(r"::rep\d+$")
RE_PARTE = re.compile(r"::parte\d+$")


class ManifiestoMinimo:
    """Lo que `correr_e0.correr` usa del manifiesto."""
    tiene_oraculo = False
    mapa_territorio = None

    def __init__(self, ids: list[str]):
        self.ids = list(ids)

    def archivo_de(self, t: str) -> str:
        return f"{t}.pdf"

    def pdf_de(self, t: str) -> Path:
        return PDFS / f"{t}.pdf"


def tos_particion() -> list[str]:
    c = json.loads((PARTICION / "conteos_b584.json").read_text(encoding="utf-8"))
    return sorted(t for t, v in c.items() if isinstance(v, dict))


def correr(salida: Path, tos: list[str]) -> None:
    if salida.resolve().is_relative_to(REPO.resolve()):
        raise SystemExit(f"--salida dentro del repo: {salida}")
    if str(E0_DIR) not in sys.path:
        sys.path.insert(0, str(E0_DIR))
    import correr_e0  # noqa: PLC0415
    correr_e0.correr(salida, ManifiestoMinimo(tos), version_e0="e0-r2")


def cargar(p: Path) -> list[dict]:
    if not p.exists():
        return []
    d = json.loads(p.read_text(encoding="utf-8"))
    return d["chunks"] if isinstance(d, dict) else d


def es_pie(linea: str) -> bool:
    if str(E0_DIR) not in sys.path:
        sys.path.insert(0, str(E0_DIR))
    import e0_lib as E0  # noqa: PLC0415
    t = linea.strip()
    return bool(RE_C22.search(t)) or any(p.match(t) for p in E0.RE_PIE) or bool(E0.RE_PIE_VERSION.match(t))


def _e0():
    if str(E0_DIR) not in sys.path:
        sys.path.insert(0, str(E0_DIR))
    import e0_lib as E0  # noqa: PLC0415
    return E0


VARIANTES = (("sin K ni pie", False, False), ("solo K", True, False),
             ("solo pie", False, True), ("K y pie", True, True))


def variantes(to: str, pdf: Path, modo: str) -> dict:
    """Ids de chunk (antes de L, tablas y partición por tamaño) y líneas
    descartadas por `separar_encabezado_pie`, por variante de las reglas K y
    pie, en el modo de lectura `modo` (el de la escalera)."""
    E0 = _e0()
    paginas = E0.extraer_lineas(pdf)
    roles_v = E0.clasificar_paginas(paginas)
    kw: dict = {}
    if modo == "vigente":
        roles = roles_v
    else:
        roles = E0.clasificar_paginas(paginas, marcadores_b582=True)
        if modo == "marcadores":
            kw = {"marcadores_b582": True}
        else:
            roles = E0.roles_para_modo_sin_raiz(paginas, roles)
            kw = {"modo_sin_raiz": True}
    rep = E0.titulos_mayusculas_repetidos(paginas, roles)
    original = E0.separar_encabezado_pie
    out = {}
    for nombre, k, pie in VARIANTES:
        desc: set = set()

        def registrar(lineas, *a, **kw2):
            c, d, sc = original(lineas, *a, **kw2)
            desc.update((x.pagina, x.texto.strip()) for x in d)
            return c, d, sc
        E0.separar_encabezado_pie = registrar
        try:
            r = E0.parsear_cuerpo(to, pdf.name, paginas, roles, mayusculas_repetidas=rep if k else None,
                                  pie_desde_version=pie, **kw)
        finally:
            E0.separar_encabezado_pie = original
        r.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(r)
        E0.corregir_fronteras_intra_palabra(r)
        out[nombre] = {"ids": [c["id"] for c in E0.construir_chunks(r)], "descartadas": desc}
    return out


def _norm(ids: list[str]) -> set:
    """Ids sin el sufijo de L ni el de la partición por tamaño, como conjunto
    (una unidad partida da varios `::parteK` con la misma base)."""
    return {RE_PARTE.sub("", RE_REP.sub("", x)) for x in ids}


def atribuir_ids(v: dict, ids_b: list[str], ids_r: list[str]) -> str:
    """La regla cuya ausencia reproduce los ids de la base, si con las dos
    reglas se reproducen los de e0-r2."""
    nb, nr = _norm(ids_b), _norm(ids_r)
    if _norm(v["K y pie"]["ids"]) != nr or _norm(v["sin K ni pie"]["ids"]) != nb:
        return "otra"
    if _norm(v["solo pie"]["ids"]) == nb:
        return "K"
    if _norm(v["solo K"]["ids"]) == nb:
        return "pie"
    return "K y pie"


def lineas_por_regla(v: dict) -> dict:
    base = v["sin K ni pie"]["descartadas"]
    return {"K_quita": v["solo K"]["descartadas"] - base,
            "K_conserva": base - v["solo K"]["descartadas"],
            "pie_quita": v["solo pie"]["descartadas"] - base}


def clase_texto(tb: str, tr: str, cons_txt: set, por_regla: dict | None) -> tuple[str, list, list]:
    """Clase de un chunk cuyo texto cambia (ver docstring del módulo)."""
    lb, lr = tb.split("\n"), tr.split("\n")
    quitadas = [x for x in lb if x not in lr]
    agregadas = [x for x in lr if x not in lb]
    if "[TABLA " in tr:
        return "tablas", quitadas, agregadas
    k_quita = {t for _, t in por_regla["K_quita"]} if por_regla else set()
    k_cons = {t for _, t in por_regla["K_conserva"]} if por_regla else set()
    p_quita = {t for _, t in por_regla["pie_quita"]} if por_regla else set()
    clases = set()
    for x in quitadas:
        t = x.strip()
        if es_pie(x) or t in p_quita or _forma_pie(t) != "otra":
            clases.add("pies")
        elif t in k_quita:
            clases.add("K")
        else:
            return "otra", quitadas, agregadas
    for x in agregadas:
        if x.strip() in cons_txt or x.strip() in k_cons:
            clases.add("K")
        else:
            return "otra", quitadas, agregadas
    return (" y ".join(sorted(clases, key=["pies", "K"].index)) or "otra"), quitadas, agregadas


def _forma_pie(t: str) -> str:
    aqui = str(Path(__file__).resolve().parent)
    if aqui not in sys.path:
        sys.path.insert(0, aqui)
    import r4_pies_e0  # noqa: PLC0415
    return r4_pies_e0.forma_de_pie(t)


def comparar(salidas: list[Path], atribuir: bool = False) -> dict:
    conteos_b = json.loads((PARTICION / "conteos_b584.json").read_text(encoding="utf-8"))
    por_salida = {}
    for s in salidas:
        conteos = json.loads((s / "conteos.json").read_text(encoding="utf-8")) if (s / "conteos.json").exists() else {}
        sub = json.loads((s / "sub_chunking.json").read_text(encoding="utf-8")) if (s / "sub_chunking.json").exists() else {}
        conservados = (json.loads((s / "encabezados_conservados.json").read_text(encoding="utf-8"))
                       if (s / "encabezados_conservados.json").exists() else {})
        for to in conteos:
            por_salida[to] = (s, conteos[to], sub.get(to, {}), conservados.get(to, []))
    filas, clases_ids, clases_texto = [], Counter(), Counter()
    otras_ids, otras_texto, en_cero, modo_distinto, faltan = [], [], [], [], []
    ids_por_causa, unidades_por_causa = Counter(), {}
    for to in tos_particion():
        b = cargar(PARTICION / to / f"chunks_{to}.json")
        if to not in por_salida:
            faltan.append(to)
            continue
        s, cnt, sub, cons = por_salida[to]
        r = cargar(s / f"chunks_{to}.json")
        ib, ir = [c["id"] for c in b], [c["id"] for c in r]
        if b and not r:
            en_cero.append(to)
        mb = conteos_b[to].get("modo_lectura")
        if mb != cnt.get("modo_lectura"):
            modo_distinto.append({"to": to, "b584": mb, "e0_r2": cnt.get("modo_lectura")})
        sb, sr = set(ib), set(ir)
        solo_b, solo_r = sorted(sb - sr), sorted(sr - sb)
        dup_b = {x for x in ib if ib.count(x) > 1}
        rep = [x for x in solo_r if RE_REP.search(x)]
        bases_rep = {RE_REP.sub("", x) for x in rep}
        tabla_np = {x["id"] for x in sub.get("no_particionables", []) if x.get("motivo") == "tabla_serializada"}
        partes = [x for x in solo_b if RE_PARTE.search(x) and RE_PARTE.sub("", x) in tabla_np]
        resto_b = [x for x in solo_b if x not in partes and x not in bases_rep]
        resto_r = [x for x in solo_r if x not in rep and x not in tabla_np]
        n_otra = len(resto_b) + len(resto_r)
        tb = {c["id"]: c["texto"] for c in b if ib.count(c["id"]) == 1}
        tr = {c["id"]: c["texto"] for c in r}
        cons_txt = {x["texto"].strip() for x in cons}
        distintos = [cid for cid in sorted(set(tb) & set(tr)) if tb[cid] != tr[cid]]
        v = por_regla = causa = None
        if atribuir and (n_otra or any(clase_texto(tb[c], tr[c], cons_txt, None)[0] == "otra" for c in distintos)):
            v = variantes(to, PDFS / f"{to}.pdf", mb)
            por_regla = lineas_por_regla(v)
        if n_otra:
            causa = atribuir_ids(v, ib, ir) if v else "sin atribuir"
            ids_por_causa[causa] += n_otra
            unidades_por_causa.setdefault(causa, []).append(
                {"to": to, "solo_b584": resto_b, "solo_e0_r2": resto_r})
        c_ids = {"ids_desambiguados": len(rep), "particion_no_aplicada_por_tabla": len({RE_PARTE.sub("", x) for x in partes}),
                 "otra": n_otra}
        for k, val in c_ids.items():
            clases_ids[k] += val
        if resto_b or resto_r:
            otras_ids.append({"to": to, "causa": causa, "solo_b584": resto_b[:10], "solo_e0_r2": resto_r[:10],
                              "n": (len(resto_b), len(resto_r)), "duplicados_b584": sorted(dup_b)[:5]})
        # texto, entre ids comunes y únicos en las dos
        c_txt = Counter()
        for cid in distintos:
            clase, quitadas, agregadas = clase_texto(tb[cid], tr[cid], cons_txt, por_regla)
            if clase == "otra" and causa in ("K", "pie", "K y pie"):
                clase = f"{causa} (arrastre de un cambio de ids)"
            if clase == "otra":
                otras_texto.append({"to": to, "chunk": cid, "quitadas": quitadas[:6], "agregadas": agregadas[:6]})
            c_txt[clase] += 1
        for k, v in c_txt.items():
            clases_texto[k] += v
        filas.append({"to": to, "chunks_b584": len(ib), "chunks_e0_r2": len(ir), "modo_b584": mb,
                      "modo_e0_r2": cnt.get("modo_lectura"), "ids": c_ids, "texto": dict(c_txt)})
    return {"unidad": "U-R2-CODIGO", "etapa": "ajuste D: escalera de E0 en e0-r2 sobre la partición",
            "tos": len(filas), "faltan": faltan, "tos_en_cero_que_la_particion_segmenta": en_cero,
            "modo_de_lectura_distinto": modo_distinto,
            "tos_con_ids_iguales": sum(1 for f in filas if not sum(f["ids"].values())),
            "diferencias_de_ids_por_clase": dict(sorted(clases_ids.items())),
            "diferencias_de_ids_otra_por_causa": dict(sorted(ids_por_causa.items())),
            "unidades_por_causa": unidades_por_causa,
            "chunks_con_texto_distinto_por_clase": dict(sorted(clases_texto.items())),
            "diferencias_de_ids_otra": otras_ids, "texto_distinto_otra": otras_texto, "por_to": filas}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--correr", action="store_true")
    ap.add_argument("--comparar", action="store_true")
    ap.add_argument("--salida", type=Path, action="append", required=True)
    ap.add_argument("--tos", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--atribuir", action="store_true")
    a = ap.parse_args()
    if a.correr:
        correr(a.salida[0], a.tos.split(",") if a.tos else tos_particion())
    if a.comparar:
        r = comparar(a.salida, a.atribuir)
        Path(a.out).write_text(json.dumps(r, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(json.dumps({k: v for k, v in r.items() if k not in ("por_to", "diferencias_de_ids_otra", "texto_distinto_otra",
                                                                  "unidades_por_causa")},
                         ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
