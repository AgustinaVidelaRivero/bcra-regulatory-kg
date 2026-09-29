"""
ucita2_c5_tanda0.py — U-TANDA0-2A, etapa E6 b: indicadores de cita sobre la
celda C5 (20 preguntas nuevas sobre los cinco documentos, ens_diez/r1, en
memoria). Extensión por módulo nuevo de scripts/ucita2_indicadores.py
(a48d229), que se importa SIN EDITAR. USD 0, sin API. Corre con el python3
3.12 del PATH (nota de intérprete del gate 6: el script no parsea con el
.venv 3.10).

Por qué no alcanza la CLI del script para C5 (C2 a C4 sí corren con ella):
  - archivos_tanda solo toma trazas EV2F-*.json (ucita2_indicadores.py:158-159)
    y las de C5 son T0F-*.json;
  - cargar_contexto aborta si una pregunta tiene más de una ancla
    (ucita2_indicadores.py:304-305); cinco preguntas de C5 son de varios puntos,
    con dos anclas.

Qué hace, con las funciones del script (evaluar_traza, cargar_indice,
importar_harness, agregar, _contar_tanda):
  - indicadores 1 (cita fundada) y 2 (cita existente): no dependen del ancla;
    se computan igual que en el script;
  - indicador 3 (cita al ancla): se evalúa contra cada ancla de la pregunta y
    se reportan DOS lecturas, declaradas y sin elegir entre ellas:
    «alguna ancla» (alguna cita cae en alguna de las anclas) y «todas las
    anclas» (para cada ancla, alguna cita cae en ella). Con una sola ancla las
    dos coinciden con el indicador 3 del script.
  - «cita parseable» en dos lecturas, también declaradas: la ESTRICTA del
    script (source_doc ~ ^TO_[a-z_]+_actual\\.pdf$, ucita2_indicadores.py:130) y
    la EXTENDIDA, que además acepta como source_doc cualquier `archivo` del
    manifiesto. Los PDF de los cinco documentos nuevos se llaman ctacte.pdf,
    lingob.pdf, polcre.pdf, pagjub.pdf y docvig.pdf (tanda0_10tos.json), así
    que la regla estricta los declara no parseables aunque estén en el
    manifiesto; la extendida es la única en que los indicadores 2 y 3 miden
    algo sobre ellos. La regla del harness para el indicador 1 no cambia.
Manifiesto tanda0_10tos.json y E0 de salida_tanda0 (los de esta tanda).

Salidas: reports/tanda0/ucita2_indicadores_C5.json y .md (sin fechas).

Uso:  PYTHONDONTWRITEBYTECODE=1 python3 -B data/experiment/ev2_tanda0/code/ucita2_c5_tanda0.py
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
REPO = CODE_DIR.parents[3]
sys.path.insert(0, str(REPO / "scripts"))
import ucita2_indicadores as u            # noqa: E402  (a48d229, sin editar)

MANIFIESTO = REPO / "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos.json"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
GOLD = REPO / "data/experiment/ev2_tanda0/preguntas/preguntas_tanda0.json"
SHA_GOLD = "b36e0662170004a5e1adfcf7ea26e91ba45a469dbbda058aac3a47f4c0cc3743"
TRAZAS = REPO / "data/experiment/ev2_tanda0/trazas"
TANDAS = ("ev2_c5_diez_mem", "ev2_c5_diez_mem_enc_r1", "ev2_c5_diez_mem_enc_r2", "ev2_c5_diez_mem_enc_r3")
OUT_JSON = REPO / "reports/tanda0/ucita2_indicadores_C5.json"
OUT_MD = REPO / "reports/tanda0/ucita2_indicadores_C5.md"
IND3_ALGUNA, IND3_TODAS = "ind3_alguna_ancla", "ind3_todas_las_anclas"


def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def contexto(cita_fiel, norm_loc) -> tuple[dict, dict]:
    m = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    doc2to = {t["archivo"]: t["id"] for t in m["tos"]}
    to2doc = {t["id"]: t["archivo"] for t in m["tos"]}
    indices = {}
    for to in sorted(to2doc):
        idx = u.cargar_indice(E0 / f"estructura_{to}.json")
        if idx["archivo"] != to2doc[to] or idx["to"] != to:
            raise SystemExit(f"ABORTO: índice E0 de {to} no coincide con el manifiesto")
        indices[to] = idx
    if sha(GOLD) != SHA_GOLD:
        raise SystemExit("ABORTO: preguntas de C5 con sha distinto del sellado")
    anclas = {}
    for p in json.loads(GOLD.read_text(encoding="utf-8"))["preguntas"]:
        xs = []
        for a in p["gold"]["ancla"]:
            to, punto = a.split(":", 1)
            if to != p["to"]:
                raise SystemExit(f"ABORTO: {p['id']} ancla {a!r} de otro TO")
            xs.append({"ancla": a, "to": to, "punto": punto})
        anclas[p["id"]] = xs
    ctx = {"manifiesto": doc2to, "indices": indices, "gold": {}, "cita_fiel": cita_fiel,
           "norm_loc": norm_loc, "tos": tuple(sorted(to2doc))}
    return ctx, anclas


def evaluar(tanda: str, tr: dict, ctx: dict, anclas: list[dict]) -> dict:
    filas = []
    for a in anclas:
        c = dict(ctx, gold={tr["qid"]: a})
        filas.append(u.evaluar_traza(tanda, tr, c))
    base = dict(filas[0])
    for f in filas[1:]:                               # 1 y 2 no dependen del ancla
        for k in ("ind1_cita_fundada", "ind1_byte_exacta", "ind2_cita_existente", "grupo", "control_ind1"):
            if f[k] != base[k]:
                raise SystemExit(f"ABORTO: {tanda}/{tr['qid']}: {k} depende del ancla")
    v3 = [f["ind3_cita_al_ancla"] for f in filas]
    if base["grupo"] == "sin_json" or v3[0] == u.SIN_CITAS:
        alguna = todas = v3[0]
    else:
        alguna = u.SI if u.SI in v3 else u.NO
        todas = u.SI if all(x == u.SI for x in v3) else u.NO
    base.update({"anclas": [a["ancla"] for a in anclas], "ind3_por_ancla": v3,
                 IND3_ALGUNA: alguna, IND3_TODAS: todas})
    base["ind3_cita_al_ancla"] = alguna               # para agregar(): lectura «alguna ancla»
    return base


def contar(filas: list, clave: str) -> dict:
    out = {}
    for tanda in TANDAS:
        ft = [f for f in filas if f["tanda"] == tanda]
        out[tanda] = {g: {v: sum(1 for f in fs if f[clave] == v) for v in u.VALORES}
                      for g, fs in (("todas", ft), ("contenido", [f for f in ft if f["grupo"] == "contenido"]),
                                    ("abstencion", [f for f in ft if f["grupo"] == "abstencion"]))}
    return out


class _DocExtendido:
    """Reemplazo temporal de u.RE_DOC: acepta lo que acepta la regla del
    script o un `archivo` del manifiesto."""
    def __init__(self, original, docs):
        self.original, self.docs = original, frozenset(docs)

    def match(self, s):
        return self.original.match(s) or (s if s in self.docs else None)


def filas_de(ctx: dict, anclas: dict) -> list:
    filas = []
    for tanda in TANDAS:
        for p in sorted((TRAZAS / tanda).glob("T0F-*.json"), key=lambda x: x.name):
            doc = json.loads(p.read_text(encoding="utf-8"))
            tr, meta = doc["trace"], doc.get("meta") or {}
            if tr.get("qid") != p.stem or meta.get("caso_id") != p.stem or meta.get("label") != tanda:
                raise SystemExit(f"ABORTO: {tanda}/{p.name}: qid/caso_id/label no coinciden")
            filas.append(evaluar(tanda, tr, ctx, anclas[p.stem]))
    filas.sort(key=lambda f: (f["tanda"], f["id"]))
    return filas


def bloque(filas: list) -> dict:
    return {"agregados_alguna_ancla": u.agregar(filas),
            "ind3_todas_las_anclas": contar(filas, IND3_TODAS),
            "resumen_por_tanda": {t: u._contar_tanda([f for f in filas if f["tanda"] == t]) for t in TANDAS},
            "filas": filas}


def computar() -> dict:
    cita_fiel, norm_loc = u.importar_harness()
    ctx, anclas = contexto(cita_fiel, norm_loc)
    estricta = filas_de(ctx, anclas)
    original = u.RE_DOC
    try:
        u.RE_DOC = _DocExtendido(original, ctx["manifiesto"])
        extendida = filas_de(ctx, anclas)
    finally:
        u.RE_DOC = original
    return {"unidad": "U-TANDA0-2A E6 b, celda C5 (USD 0)",
            "script_importado": {"ruta": "scripts/ucita2_indicadores.py", "sha256": sha(REPO / "scripts/ucita2_indicadores.py")},
            "insumos": {"manifiesto": sha(MANIFIESTO), "gold": SHA_GOLD,
                        "e0": {to: sha(E0 / f"estructura_{to}.json") for to in ctx["tos"]}},
            "regla_ind3": ("dos lecturas declaradas: alguna ancla y todas las anclas; con una ancla "
                           "coinciden con el indicador 3 del script"),
            "regla_parseable": ("estricta: la del script (ucita2_indicadores.py:130); extendida: además "
                                "cualquier archivo del manifiesto tanda0_10tos.json"),
            "preguntas_con_dos_anclas": sorted(q for q, a in anclas.items() if len(a) > 1),
            "lectura_estricta": bloque(estricta), "lectura_extendida": bloque(extendida)}


def render_md(r: dict) -> str:
    L = ["# Indicadores de cita de C5 (U-TANDA0-2A E6 b)", "",
         f"Script importado sin editar: `{r['script_importado']['ruta']}` (sha256 `{r['script_importado']['sha256'][:16]}…`). "
         f"Regla del indicador 3: {r['regla_ind3']}. Preguntas con dos anclas: {', '.join(r['preguntas_con_dos_anclas'])}.", "",
         f"Regla de cita parseable: {r['regla_parseable']}.", ""]
    for nombre in ("lectura_estricta", "lectura_extendida"):
        x = r[nombre]
        L += [f"## {nombre.replace('_', ' ')}", "",
              "| tanda | grupo | N | ind1 fundada sí | ind2 existente sí | ind3 alguna ancla sí | ind3 todas las anclas sí | sin citas |",
              "|---|---|---|---|---|---|---|---|"]
        for t in TANDAS:
            a, b = x["agregados_alguna_ancla"][t], x["ind3_todas_las_anclas"][t]
            for g in ("contenido", "abstencion"):
                L.append(f"| {t} | {g} | {a[g]['N']} | {a[g]['ind1_cita_fundada']['si']} | "
                         f"{a[g]['ind2_cita_existente']['si']} | {a[g]['ind3_cita_al_ancla']['si']} | "
                         f"{b[g]['si']} | {a[g]['ind1_cita_fundada']['sin_citas']} |")
        L += ["", "Citas no parseables por tanda: " + ", ".join(
            f"{t} {x['resumen_por_tanda'][t]['citas_no_parseables']} de {x['resumen_por_tanda'][t]['citas_totales']}"
            for t in TANDAS) + ". Control del indicador 1: discrepancias " + ", ".join(
            f"{t} {x['resumen_por_tanda'][t]['control_ind1_discrepancias']}" for t in TANDAS) + ".", ""]
    return "\n".join(L) + "\n"


def main() -> int:
    r1, r2 = computar(), computar()
    if json.dumps(r1, sort_keys=True, ensure_ascii=False) != json.dumps(r2, sort_keys=True, ensure_ascii=False):
        raise SystemExit("ABORTO: doble cómputo no idéntico")
    OUT_JSON.write_text(json.dumps(r1, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    OUT_MD.write_text(render_md(json.loads(OUT_JSON.read_text(encoding="utf-8"))), encoding="utf-8")
    print(f"-> {OUT_JSON.relative_to(REPO)}\n-> {OUT_MD.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
