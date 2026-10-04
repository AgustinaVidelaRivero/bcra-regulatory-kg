"""U-R2-CODIGO-2, C2, freno de diseño — punto (n): versión y materia del TextoOrdenado (USD 0, sin API). Solo
escribe --out.

Lee el pie de cada página de los diez TOs de la tanda 0 con el criterio con que e0-r2 lo recorta
(`e0_lib.separar_encabezado_pie`, `pie_desde_version`): la línea que cumple `RE_PIE_VERSION` entre las últimas
`VENTANA_PIE_VERSION` y las que la siguen, más los renglones de `RE_PIE` que quedan encima («Vigencia:», la fecha).
De ese pie saca, por página, la versión de la hoja («7a.»), la Comunicación («A 7149»), el número de hoja y la fecha
de vigencia. No edita E0: mide lo que el diseño propone guardar.

Estados de una página:
  - legible: el pie trae la Comunicación (letra y número) y una fecha;
  - legible, versión ilegible: además la versión de la hoja no se lee (p. ej. «(cid:21)a.»);
  - no_legible: hay línea «Versión: … Comunicación …», pero no se leen la Comunicación o la fecha;
  - sin_pie: ninguna de las últimas líneas cumple `RE_PIE_VERSION` (carátula, tabla de origen, historial).
Versión vigente de un TO: entre las páginas legibles, la de fecha de vigencia más reciente; si empatan, la de mayor
número de Comunicación. Se contrasta con la «Última comunicación incorporada» de la carátula, donde se lee.
Materia: el título oficial del inventario (`inventario_tos.csv`, `titulo_oficial`; para los cinco de desarrollo,
`inventario_resumen.json`, `subset_excluido`), sin normalizar: `r1_referencias.titulos_de_inventario` devuelve el
título normalizado, que sirve para resolver citas y no como materia.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c2d_pies.py \
      --out data/experiment/r2_codigo2/salidas/c2d_pies.json
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import re
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
for p in (RAIZ / "data/experiment/reextraccion_v2/e0_chunking", RAIZ / "data/experiment/reextraccion_v2"):
    sys.path.insert(0, str(p))
import e0_lib as L                      # noqa: E402
import manifiesto_corpus as MC          # noqa: E402

MANIFIESTO = RAIZ / "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json"
INV_CSV = RAIZ / "data/experiment/escalado_prep/inventario_tos.csv"
INV_RESUMEN = RAIZ / "data/experiment/escalado_prep/inventario_resumen.json"
_COMILLAS = "\"“”'«»‘’"
RE_COMUNICACION = re.compile(r"comunicaci[oó]n\s*[" + _COMILLAS + r"]?\s*(?P<l>[ABC])\s*[" + _COMILLAS + r"]?\s*"
                             r"(?P<n>\d{1,2}\.?\d{3}|\d{1,4})", re.I)
RE_VERSION_HOJA = re.compile(r"versi[oó]n\s*:\s*(?P<v>\S+?)\s*comunicaci", re.I)
RE_HOJA = re.compile(r"p[aá]gina\s+(\d+)", re.I)
RE_FECHA = re.compile(r"(?<!\d)(\d{1,2})[/.](\d{1,2})[/.](\d{2,5})(?!\d)")
RE_ULTIMA = re.compile(r"ltima\s+comunicaci[oó]n\s+incorporada\s*:?\s*[" + _COMILLAS + r"]?\s*([ABC])\s*[" + _COMILLAS
                       + r"]?\s*(\S+?)-?\s*(?:texto ordenado al\s*(.*))?$", re.I)


def fecha(s: str) -> datetime.date | None:
    m = RE_FECHA.search(s)
    if not m:
        return None
    d, mes, a = int(m.group(1)), int(m.group(2)), int(m.group(3))
    a = a + 2000 if a < 100 else a
    try:
        return datetime.date(a, mes, d)
    except ValueError:
        return None


def pie_de(lineas: list) -> list[str] | None:
    """Renglones del pie con el criterio de e0-r2, o None si la página no tiene pie de versión."""
    textos = [ln.texto.strip() for ln in lineas]
    for i in range(len(textos) - 1, max(-1, len(textos) - 1 - L.VENTANA_PIE_VERSION), -1):
        if L.RE_PIE_VERSION.match(textos[i]):
            pie = textos[i:]
            j = i
            while j > 0 and any(p.match(textos[j - 1]) for p in L.RE_PIE):
                j -= 1
            return textos[j:i] + pie
    return None


def leer_pagina(lineas: list) -> OrderedDict:
    pie = pie_de(lineas)
    if pie is None:
        return OrderedDict([("estado", "sin_pie")])
    txt = " ".join(pie)
    mc, mv, mh = RE_COMUNICACION.search(txt), RE_VERSION_HOJA.search(txt), RE_HOJA.search(txt)
    f = fecha(" ".join(x for x in pie if not RE_COMUNICACION.search(x)) or txt)
    ver = mv.group("v") if mv else None
    ver_ok = bool(ver and re.fullmatch(r"\d+[aª]?\.?", ver))
    estado = "legible" if (mc and f) else "no_legible"
    return OrderedDict([
        ("estado", estado), ("version_hoja", ver if ver_ok else None), ("version_hoja_legible", ver_ok),
        ("comunicacion", f"{mc.group('l').upper()} {mc.group('n').replace('.', '')}" if mc else None),
        ("hoja", int(mh.group(1)) if mh else None), ("vigencia", f.isoformat() if f else None),
        ("lineas", pie)])


def titulos_oficiales() -> dict[str, str]:
    tit = {r["id"]: r["titulo_oficial"] for r in csv.DictReader(INV_CSV.open(encoding="utf-8"))}
    for x in json.loads(INV_RESUMEN.read_text(encoding="utf-8"))["subset_excluido"]:
        tit[x["id_interno"]] = x["titulo"]
    return tit


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    man = MC.cargar(MANIFIESTO)
    tit = titulos_oficiales()
    out = OrderedDict([("criterio_version_vigente", "entre las páginas legibles, la de vigencia más reciente; si "
                                                   "empatan, la de mayor número de Comunicación")])
    tot = Counter()
    por_to = OrderedDict()
    for to in man.ids:
        pags = L.extraer_lineas(man.pdf_de(to))
        roles = L.clasificar_paginas(pags)
        filas = []
        for i, (ls, rol) in enumerate(zip(pags, roles), 1):
            fila = OrderedDict([("pagina", i), ("rol", rol)])
            fila.update(leer_pagina(ls))
            filas.append(fila)
        leg = [f for f in filas if f["estado"] == "legible"]
        vig = max(leg, key=lambda f: (f["vigencia"], int(f["comunicacion"].split()[1]))) if leg else None
        cara = None
        for ln in pags[0][:20]:
            m = RE_ULTIMA.search(ln.texto.strip())
            if m:
                cara = {"ultima_comunicacion_incorporada": f"{m.group(1).upper()} {m.group(2)}",
                        "texto_ordenado_al": (m.group(3) or "").strip() or None, "linea": ln.texto.strip()}
                break
        cuenta = Counter(f["estado"] for f in filas)
        sin_pie_por_rol = Counter(f["rol"] for f in filas if f["estado"] == "sin_pie")
        tot.update(cuenta)
        tot["version_hoja_ilegible"] += sum(1 for f in leg if not f["version_hoja_legible"])
        por_to[to] = OrderedDict([
            ("paginas", len(filas)), ("estados", dict(sorted(cuenta.items()))),
            ("sin_pie_por_rol", dict(sorted(sin_pie_por_rol.items()))),
            ("legibles_con_version_de_hoja_ilegible", [f["pagina"] for f in leg if not f["version_hoja_legible"]]),
            ("no_legibles", [{"pagina": f["pagina"], "lineas": f["lineas"]} for f in filas
                             if f["estado"] == "no_legible"]),
            ("version_vigente", None if vig is None else OrderedDict([
                ("comunicacion", vig["comunicacion"]), ("vigencia", vig["vigencia"]), ("pagina", vig["pagina"]),
                ("valor_propuesto", f"Comunicación {vig['comunicacion']} (vigencia "
                                    f"{datetime.date.fromisoformat(vig['vigencia']).strftime('%d/%m/%Y')})")])),
            ("mayor_numero_en_los_pies", max((f["comunicacion"] for f in leg),
                                            key=lambda c: int(c.split()[1]), default=None)),
            ("caratula", cara),
            ("coincide_con_la_caratula", None if (cara is None or vig is None or not
                                                  re.fullmatch(r"\d+", cara["ultima_comunicacion_incorporada"]
                                                               .split()[1])) else
             cara["ultima_comunicacion_incorporada"] == vig["comunicacion"]),
            ("materia_propuesta", tit.get(to)),
            ("paginas_detalle", filas)])
    out["totales"] = OrderedDict([("paginas", sum(v["paginas"] for v in por_to.values()))])
    out["totales"].update(sorted(tot.items()))
    out["coincidencias_con_la_caratula"] = OrderedDict([
        ("coinciden", sum(1 for v in por_to.values() if v["coincide_con_la_caratula"] is True)),
        ("no_coinciden", sum(1 for v in por_to.values() if v["coincide_con_la_caratula"] is False)),
        ("sin_caratula_legible", sorted(t for t, v in por_to.items() if v["coincide_con_la_caratula"] is None))])
    out["por_to"] = por_to
    (RAIZ / a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out["totales"], ensure_ascii=False), json.dumps(out["coincidencias_con_la_caratula"]))
    for to, v in por_to.items():
        print(to, v["estados"], v["sin_pie_por_rol"], (v["version_vigente"] or {}).get("valor_propuesto"),
              "| carátula:", (v["caratula"] or {}).get("ultima_comunicacion_incorporada"),
              v["coincide_con_la_caratula"], "| ver. ilegible:", v["legibles_con_version_de_hoja_ilegible"],
              "| materia:", v["materia_propuesta"])


if __name__ == "__main__":
    main()
