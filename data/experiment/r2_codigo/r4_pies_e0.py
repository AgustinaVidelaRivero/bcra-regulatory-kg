"""U-R2-CODIGO, agregado 8 de las decisiones sobre el freno R3 — pies de página
dentro del texto de E0: diagnóstico por caso. Solo lectura. USD 0.

Criterio de la fila del tablero ([c22]): un chunk tiene pie si alguna línea de
su `texto` cumple `versi[oó]n\\s*:.*comunicaci[oó]n` (sin distinguir mayúsculas).
Conjuntos: la E0 de la tanda 0 (`e0_chunking/salida_tanda0/`, diez TOs; la de
r1 es byte-idéntica en sus cinco TOs) y la partición del corpus escalado
(`segmentacion_84/b584_particion/<to>/`). Con `--e0-r2 <dir>` cuenta también
sobre esa salida de e0-r2 de la tanda 0.

Para cada línea de pie busca, en las páginas del chunk (`paginas`), la línea
del PDF con el mismo texto (e0_lib.extraer_lineas, que es el corpus de E0) y
mira qué la sigue en la página. El recorte de pie de E0
(e0_lib.separar_encabezado_pie) quita líneas desde el final mientras cumplan
RE_PIE; la causa por caso:
  - pie_seguido_de_linea_no_reconocida: la línea de pie cumple RE_PIE pero la
    sigue en la página una línea que no lo cumple (se informa cuál), así que el
    recorte se detiene antes;
  - pie_con_forma_no_reconocida: la línea de pie no cumple RE_PIE (se informa
    la forma);
  - linea_no_encontrada_en_el_pdf: ninguna página del chunk tiene esa línea
    exacta.

Con `--simular`, además, la regla de e0-r2 (e0_lib.separar_encabezado_pie con
`pie_desde_version`) página por página, sobre todas las páginas de los PDFs de
la tanda 0 y de los 152 de la partición: líneas que cumplen el criterio [c22]
y quedan como contenido con el recorte histórico y con la regla, y formas de
las líneas que la regla quita y el recorte histórico no (para leer que sean
de pie).

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/r4_pies_e0.py --out <json> \
      [--e0-r2 <salida de correr_e0.py --version-e0 e0-r2 de la tanda 0>] [--sin-particion] [--simular]
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
if str(E0_DIR) not in sys.path:
    sys.path.insert(0, str(E0_DIR))
import e0_lib as E0  # noqa: E402

RE_C22 = re.compile(r"versi[oó]n\s*:.*comunicaci[oó]n", re.I)
MAN_DIEZ = REPO / "data" / "experiment" / "reextraccion_v2" / "manifiestos" / "tanda0_10tos.json"
TANDA0 = E0_DIR / "salida_tanda0"
PARTICION = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
PDFS_PARTICION = REPO / "data" / "experiment" / "escalado_prep" / "pdfs"


def cargar(p: Path) -> list[dict]:
    d = json.loads(p.read_text(encoding="utf-8"))
    return d["chunks"] if isinstance(d, dict) else d


def es_pie(t: str) -> bool:
    return any(p.match(t.strip()) for p in E0.RE_PIE)


def con_pie(chunks: list[dict]) -> list[tuple[dict, list[str]]]:
    out = []
    for c in chunks:
        ls = [l for l in (c.get("texto") or "").split("\n") if RE_C22.search(l)]
        if ls:
            out.append((c, ls))
    return out


def diagnosticar(to: str, pdf: Path, casos: list[tuple[dict, list[str]]], cache: dict) -> list[dict]:
    if to not in cache:
        cache[to] = E0.extraer_lineas(pdf)
    paginas = cache[to]
    filas = []
    for c, ls in casos:
        for l in ls:
            fila = {"to": to, "chunk_id": c["id"], "linea": l, "cumple_RE_PIE": es_pie(l)}
            hallada = None
            for pn in c.get("paginas") or range(1, len(paginas) + 1):
                if not 1 <= pn <= len(paginas):
                    continue
                pag = paginas[pn - 1]
                for i, x in enumerate(pag):
                    if x.texto.strip() == l.strip():
                        hallada = (pn, i, pag)
                        break
                if hallada:
                    break
            if hallada is None:
                fila["causa"] = "linea_no_encontrada_en_el_pdf"
            else:
                pn, i, pag = hallada
                despues = [x.texto for x in pag[i + 1:]]
                fila.update(pagina=pn, lineas_despues=despues,
                            primera_no_reconocida=next((t for t in reversed(despues) if not es_pie(t)), None))
                if not fila["cumple_RE_PIE"]:
                    fila["causa"] = "pie_con_forma_no_reconocida"
                else:
                    fila["causa"] = "pie_seguido_de_linea_no_reconocida"
            filas.append(fila)
    return filas


def forma(f: dict) -> str:
    """Subtipo legible de la causa."""
    if f["causa"] == "pie_con_forma_no_reconocida":
        t = f["linea"]
        if re.search(r"P[aá]gina\s*:\s*\d", t):
            return "«Página:N» con dos puntos"
        if not re.search(r"P[aá]gina", t, re.I):
            return "sin «Página» en la línea"
        return "otra"
    if f["causa"] == "pie_seguido_de_linea_no_reconocida":
        t = (f.get("primera_no_reconocida") or "").strip()
        if re.fullmatch(r"\d{1,2}\.\d{1,2}\.\d{2,4}", t):
            return "fecha con puntos"
        if re.fullmatch(r"\d{1,2}/\d{1,2}/\d{5,}", t):
            return "fecha con año de más de cuatro dígitos"
        if re.fullmatch(r"P[aá]gina\s*:\s*\d+", t):
            return "«Página:N» con dos puntos"
        return "contenido u otra línea después del pie"
    return "-"


def resumen(filas: list[dict]) -> dict:
    return {"lineas_de_pie": len(filas), "chunks": len({f["chunk_id"] for f in filas}),
            "tos": len({f["to"] for f in filas}),
            "por_causa": dict(sorted(Counter(f["causa"] for f in filas).items())),
            "por_subtipo": dict(sorted(Counter(f"{f['causa']} / {forma(f)}" for f in filas).items()))}


FORMAS_PIE = [
    ("versión", re.compile(r"^Versi[oó]n\s*:", re.I)),
    ("vigencia", re.compile(r"^Vigencia\s*:?", re.I)),
    ("fecha", re.compile(r"^\d{1,2}[./]\d{1,2}[./]\d{2,5}(\s+\d+\s+de\s+\d+)?$")),
    ("circular CONAU", re.compile(r"^(Circular\s+)?CONAU\b", re.I)),
    ("comunicación C", re.compile(r"^Comunicaci[oó]n\s+[“\"]C[”\"]\s*\d+$", re.I)),
    ("página", re.compile(r"^P[aá]gina\s*:?\s*\d+", re.I)),
]


def forma_de_pie(t: str) -> str:
    """Forma de una línea que la regla quita: una de FORMAS_PIE u «otra»."""
    t = t.strip()
    return next((nombre for nombre, pat in FORMAS_PIE if pat.search(t)), "otra")


def simular(pdfs: dict[str, Path], cache: dict, tanda0: set[str] | None = None) -> dict:
    """Recorte histórico contra la regla de e0-r2, en todas las páginas. Las
    líneas que la regla quita y el recorte histórico no se listan una por una
    (texto exacto y conteo), en la tanda 0 y en el total, con su forma; las de
    forma «otra», con TO y página."""
    queda_hist, queda_regla, extra = Counter(), Counter(), Counter()
    exactas = {"tanda0": Counter(), "total": Counter()}
    otras = []
    ejemplos_queda, paginas_con_extra = [], 0
    for to, pdf in sorted(pdfs.items()):
        if to not in cache:
            cache[to] = E0.extraer_lineas(pdf)
        for pag in cache[to]:
            c_h, d_h, _ = E0.separar_encabezado_pie(pag)
            c_r, d_r, _ = E0.separar_encabezado_pie(pag, pie_desde_version=True)
            queda_hist[to] += sum(1 for l in c_h if RE_C22.search(l.texto))
            n_r = [l for l in c_r if RE_C22.search(l.texto)]
            queda_regla[to] += len(n_r)
            if n_r and len(ejemplos_queda) < 20:
                ejemplos_queda.append({"to": to, "pagina": n_r[0].pagina, "linea": n_r[0].texto,
                                       "lineas_despues": len(c_r) - 1 - c_r.index(n_r[0])})
            ids_h = {id(l) for l in d_h}
            nuevas = [l for l in d_r if id(l) not in ids_h]
            if nuevas:
                paginas_con_extra += 1
            for l in nuevas:
                extra[re.sub(r"\d", "9", l.texto.strip())[:80]] += 1
                exactas["total"][l.texto.strip()] += 1
                if tanda0 and to in tanda0:
                    exactas["tanda0"][l.texto.strip()] += 1
                if forma_de_pie(l.texto) == "otra":
                    otras.append({"to": to, "pagina": l.pagina, "linea": l.texto,
                                  "contexto_hasta_la_linea": [x.texto for x in pag if x.top <= l.top][-3:]})
    return {"pdfs": len(pdfs), "lineas_c22_en_contenido": {"recorte_historico": sum(queda_hist.values()),
                                                          "regla_e0_r2": sum(queda_regla.values())},
            "por_to_con_regla": {k: v for k, v in sorted(queda_regla.items()) if v},
            "ejemplos_que_quedan_con_la_regla": ejemplos_queda,
            "paginas_donde_la_regla_quita_mas": paginas_con_extra,
            "lineas_que_la_regla_quita_de_mas": sum(extra.values()),
            "formas_que_la_regla_quita_de_mas": dict(extra.most_common()),
            "lineas_distintas_que_la_regla_quita_de_mas": {
                k: {"lineas_distintas": len(v), "lineas": sum(v.values()),
                    "por_forma": dict(sorted(Counter(forma_de_pie(t) for t in v.elements()).items())),
                    "lista": [{"linea": t, "n": n, "forma": forma_de_pie(t)} for t, n in sorted(v.items())]}
                for k, v in exactas.items()},
            "lineas_de_forma_otra": otras}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--e0-r2", type=Path, default=None)
    ap.add_argument("--sin-particion", action="store_true")
    ap.add_argument("--simular", action="store_true")
    a = ap.parse_args()
    man = json.loads(MAN_DIEZ.read_text(encoding="utf-8"))
    out: dict = {"unidad": "U-R2-CODIGO", "etapa": "agregado 8: pies de página dentro del texto de E0",
                 "criterio": RE_C22.pattern + " (sin distinguir mayúsculas), sobre las líneas de `texto`"}
    cache: dict = {}
    filas_t0 = []
    for t in man["tos"]:
        casos = con_pie(cargar(TANDA0 / f"chunks_{t['id']}.json"))
        if casos:
            filas_t0 += diagnosticar(t["id"], REPO / t["pdf"], casos, cache)
    out["tanda0"] = {"chunks_totales": sum(len(cargar(TANDA0 / f"chunks_{t['id']}.json")) for t in man["tos"]),
                     **resumen(filas_t0), "casos": filas_t0}
    if a.e0_r2:
        n = {t["id"]: con_pie(cargar(a.e0_r2 / f"chunks_{t['id']}.json")) for t in man["tos"]}
        out["tanda0_e0_r2"] = {"chunks_con_pie": sum(len(v) for v in n.values()),
                               "lineas_de_pie": sum(len(ls) for v in n.values() for _, ls in v),
                               "chunks": sorted(c["id"] for v in n.values() for c, _ in v)}
    if not a.sin_particion:
        filas_p, total = [], 0
        for d in sorted(x for x in PARTICION.iterdir() if x.is_dir()):
            p = d / f"chunks_{d.name}.json"
            if not p.exists():
                continue
            cs = cargar(p)
            total += len(cs)
            casos = con_pie(cs)
            if casos:
                filas_p += diagnosticar(d.name, PDFS_PARTICION / f"{d.name}.pdf", casos, cache)
        out["particion"] = {"chunks_totales": total, **resumen(filas_p),
                            "por_to": dict(sorted(Counter(f["to"] for f in filas_p).items())), "casos": filas_p}
    if a.simular:
        pdfs = {t["id"]: REPO / t["pdf"] for t in man["tos"]}
        if not a.sin_particion:
            pdfs.update({d.name: PDFS_PARTICION / f"{d.name}.pdf" for d in PARTICION.iterdir()
                         if d.is_dir() and (PDFS_PARTICION / f"{d.name}.pdf").exists()})
        out["simulacion_regla_e0_r2"] = simular(pdfs, cache, {t["id"] for t in man["tos"]})
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk not in ("casos",)} if isinstance(v, dict) else v
                      for k, v in out.items()}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
