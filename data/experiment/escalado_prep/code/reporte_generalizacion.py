"""Genera ../reporte_generalizacion.md a partir de la corrida E0 en seco.

Veredicto por TO: "digerible" o "necesita reglas". Los umbrales NO son
inventados: son el peor valor observado entre los 5 TOs del subset congelado,
que son la única evidencia disponible de que E0+E1+E3 digieren un TO de punta
a punta. Se recalculan en cada corrida desde ../referencia_subset.json (misma
ruta de código que los TOs nuevos, paridad byte a byte con salida_enm01
verificada por referencia_subset.py).

Criterios (H = duro, incumplirlo es fallo estructural; C = de banda):
  H1 cobertura exacta de líneas (cero pérdida, cero duplicados, cero huérfanas)
  H2 el parser engancha estructura (≥1 sección y ≥1 chunk terminal)
  H3 cero fronteras intra-palabra después de la regla 2
  C4 rechazos de header por unidad ≤ peor del subset
  C5 puntos anunciados por el índice sin cuerpo ≤ max(1, tasa peor del subset)
  C6 % de chunks con contenido tabular ≤ peor del subset
  C7 avisos de parseo por unidad ≤ peor del subset
  C8 chunk terminal más grande ≤ peor del subset (detecta no-segmentación)
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI.parent
E0_DRY = PREP / "e0_dry"


def umbrales(ref: dict) -> dict:
    def peor(f):
        return max(f(v) for v in ref.values())
    return {
        "C4_rechazos_por_unidad": peor(
            lambda v: v["diagnostico"]["rechazos_header"]["total"] / v["unidades_extraccion"]),
        "C5_tasa_anunciado_sin_cuerpo": peor(
            lambda v: (v["diagnostico"]["indice"]["anunciado_sin_cuerpo"]
                       / max(1, v["diagnostico"]["indice"]["puntos_en_indice"]))),
        "C6_pct_tabular": peor(lambda v: v["diagnostico"]["tabular"]["pct_chunks_tabulares"]),
        "C7_avisos_por_unidad": peor(
            lambda v: v["diagnostico"]["avisos"]["total"] / v["unidades_extraccion"]),
        "C8_max_chars_terminal": peor(
            lambda v: v["diagnostico"]["escala"]["max_chars_propio_terminal"]),
    }


def evaluar(c: dict, u: dict) -> tuple[str, list[str], list[str]]:
    g = c["diagnostico"]
    n = max(1, c["unidades_extraccion"])
    fallas: list[str] = []
    flags: list[str] = []

    if not g["cobertura"]["cobertura_exacta"]:
        fallas.append(
            f"H1 cobertura no exacta: parseadas={g['cobertura']['lineas_contenido_parseadas']}, "
            f"en estructura={g['cobertura']['lineas_en_estructura']}, "
            f"duplicadas={g['cobertura']['lineas_duplicadas']}, "
            f"huérfanas={g['cobertura']['lineas_huerfanas']}")
    if c["secciones"] < 1 or c["chunks_terminales"] < 1:
        fallas.append(f"H2 el parser no engancha estructura: secciones={c['secciones']}, "
                      f"chunks terminales={c['chunks_terminales']}")
    if g["fronteras"]["intra_palabra_despues"] != 0:
        fallas.append(f"H3 quedan {g['fronteras']['intra_palabra_despues']} fronteras "
                      f"intra-palabra tras la regla 2")

    r = g["rechazos_header"]["total"] / n
    if r > u["C4_rechazos_por_unidad"]:
        top = sorted(g["rechazos_header"]["por_motivo"].items(), key=lambda kv: -kv[1])[:3]
        fallas.append(f"C4 rechazos de header {g['rechazos_header']['total']} sobre {n} unidades "
                      f"= {r:.3f}/u > {u['C4_rechazos_por_unidad']:.3f}/u; motivos dominantes: "
                      + ", ".join(f"{k}×{v}" for k, v in top))

    pi = g["indice"]["puntos_en_indice"]
    asc = g["indice"]["anunciado_sin_cuerpo"]
    if pi == 0:
        flags.append("sin índice parseable: el contraste índice↔cuerpo no puede correrse")
    else:
        tasa = asc / pi
        if asc > 1 and tasa > u["C5_tasa_anunciado_sin_cuerpo"]:
            fallas.append(f"C5 el índice anuncia {asc} de {pi} puntos que no aparecen en el "
                          f"cuerpo = {tasa:.3f} > {u['C5_tasa_anunciado_sin_cuerpo']:.3f}")

    if g["tabular"]["pct_chunks_tabulares"] > u["C6_pct_tabular"]:
        fallas.append(f"C6 {g['tabular']['chunks_con_contenido_tabular']} chunks con contenido "
                      f"tabular = {g['tabular']['pct_chunks_tabulares']:.2f} % > "
                      f"{u['C6_pct_tabular']:.2f} %")

    a = g["avisos"]["total"] / n
    if a > u["C7_avisos_por_unidad"]:
        top = sorted(g["avisos"]["por_tipo"].items(), key=lambda kv: -kv[1])[:3]
        fallas.append(f"C7 avisos de parseo {g['avisos']['total']} sobre {n} unidades = {a:.3f}/u "
                      f"> {u['C7_avisos_por_unidad']:.3f}/u; tipos: "
                      + ", ".join(f"{k}×{v}" for k, v in top))

    mx = g["escala"]["max_chars_propio_terminal"]
    if mx > u["C8_max_chars_terminal"]:
        fallas.append(f"C8 chunk terminal más grande {mx} chars > {u['C8_max_chars_terminal']} "
                      f"chars (señal de tramo no segmentado)")

    if g["indice"]["en_cuerpo_sin_anunciar"] > 12:
        flags.append(f"{g['indice']['en_cuerpo_sin_anunciar']} unidades del cuerpo no anunciadas "
                     f"por el índice (peor del subset: 12)")
    if g["saltos_numeracion"] > 2:
        flags.append(f"{g['saltos_numeracion']} saltos de numeración (peor del subset: 2)")
    if g["tabular"]["chunks_con_formula"] > 24:
        flags.append(f"{g['tabular']['chunks_con_formula']} chunks con fórmula "
                     f"(peor del subset: 24)")

    return ("digerible" if not fallas else "necesita reglas"), fallas, flags


def main() -> None:
    ref = json.loads((PREP / "referencia_subset.json").read_text(encoding="utf-8"))
    conteos = json.loads((E0_DRY / "conteos_e0_dry.json").read_text(encoding="utf-8"))
    fallos = json.loads((E0_DRY / "fallos_e0_dry.json").read_text(encoding="utf-8"))
    inv = {f["id"]: f for f in csv.DictReader((PREP / "inventario_tos.csv").open(encoding="utf-8"))}
    u = umbrales(ref)

    veredictos = {}
    for ident, c in conteos.items():
        v, fallas, flags = evaluar(c, u)
        veredictos[ident] = {"veredicto": v, "fallas": fallas, "flags": flags}
    (PREP / "veredictos_generalizacion.json").write_text(
        json.dumps({"umbrales": u, "por_to": veredictos}, ensure_ascii=False, indent=1),
        encoding="utf-8")

    ok = [i for i, v in veredictos.items() if v["veredicto"] == "digerible"]
    ko = [i for i, v in veredictos.items() if v["veredicto"] == "necesita reglas"]

    L: list[str] = []
    A = L.append
    A("# Reporte de generalización del parser E0 sobre el universo de TOs del BCRA")
    A("")
    A("Corrida EN SECO (código determinístico puro, cero llamadas a LLM, gasto USD 0) del")
    A("E0 calibrado sobre los 5 TOs del subset — `data/experiment/reextraccion_v2/e0_chunking/`,")
    A("invocado sin editar — aplicado a los TOs del índice oficial del BCRA que NO están en el")
    A("subset congelado.")
    A("")
    A("## 1. Alcance y reproducción")
    A("")
    A(f"- TOs del inventario: **{len(inv)}** (`inventario_tos.csv`).")
    A(f"- TOs con E0 corrido: **{len(conteos)}**. TOs que abortaron: **{len(fallos)}**.")
    A(f"- Veredicto **digerible**: {len(ok)}. Veredicto **necesita reglas**: {len(ko)}.")
    A("")
    A("```bash")
    A("python3 code/construir_inventario.py     # inventario desde el índice oficial congelado")
    A("python3 code/descargar_pdfs.py           # PDFs a pdfs/ (idempotente)")
    A("python3 code/referencia_subset.py        # banda de referencia + paridad con salida_enm01")
    A("python3 code/correr_e0_seco.py           # E0 + censo en seco sobre pdfs/")
    A("python3 code/reporte_generalizacion.py   # este documento")
    A("```")
    A("")
    A("## 2. Banda de referencia y umbrales")
    A("")
    A("El driver de esta unidad reproduce **byte a byte** los chunks sellados de los 5 TOs del")
    A("subset (`referencia_subset.json`, campo `paridad_con_salida_enm01.identicos`): es el mismo")
    A("E0, no una reimplementación. Los umbrales son el **peor valor observado en esos 5 TOs**,")
    A("que son la única evidencia empírica de que un TO se digiere de punta a punta.")
    A("")
    A("| criterio | umbral (peor del subset) |")
    A("|---|---|")
    A("| H1 cobertura exacta de líneas | debe ser verdadera |")
    A("| H2 estructura enganchada | ≥1 sección y ≥1 chunk terminal |")
    A("| H3 fronteras intra-palabra tras regla 2 | 0 |")
    A(f"| C4 rechazos de header por unidad | ≤ {u['C4_rechazos_por_unidad']:.4f} |")
    A(f"| C5 tasa de puntos anunciados sin cuerpo | ≤ {u['C5_tasa_anunciado_sin_cuerpo']:.4f} (y ≤1 en absoluto) |")
    A(f"| C6 % de chunks con contenido tabular | ≤ {u['C6_pct_tabular']:.2f} % |")
    A(f"| C7 avisos de parseo por unidad | ≤ {u['C7_avisos_por_unidad']:.4f} |")
    A(f"| C8 chunk terminal más grande | ≤ {u['C8_max_chars_terminal']} chars |")
    A("")
    A("Valores del subset, uno por uno:")
    A("")
    A("| TO | unid. | cobertura | rech./u | anunc. sin cuerpo | % tabular | avisos/u | max chars |")
    A("|---|--:|:--:|--:|--:|--:|--:|--:|")
    for to, v in ref.items():
        g = v["diagnostico"]
        n = v["unidades_extraccion"]
        A(f"| {to} | {n} | {'OK' if g['cobertura']['cobertura_exacta'] else 'NO'} | "
          f"{g['rechazos_header']['total'] / n:.4f} | "
          f"{g['indice']['anunciado_sin_cuerpo']}/{g['indice']['puntos_en_indice']} | "
          f"{g['tabular']['pct_chunks_tabulares']:.2f} | {g['avisos']['total'] / n:.4f} | "
          f"{g['escala']['max_chars_propio_terminal']} |")
    A("")

    if fallos:
        A("## 3. TOs que abortaron E0")
        A("")
        for ident, f in sorted(fallos.items()):
            A(f"### {ident} — {inv[ident]['titulo_oficial']}")
            A("")
            A(f"Archivo `{f['archivo']}`, {f['bytes']} bytes. Error textual:")
            A("")
            A("```")
            A(f["traceback"].rstrip())
            A("```")
            A("")
    else:
        A("## 3. TOs que abortaron E0")
        A("")
        A("Ninguno: E0 corrió de punta a punta sobre los "
          f"{len(conteos)} TOs del inventario.")
        A("")

    A("## 4. Tabla por TO")
    A("")
    A("`unid.` = chunks terminales + mini-chunks estructurales (unidades de extracción de E1).")
    A("`idx a/b` = puntos anunciados por el índice sin cuerpo / puntos que el índice declara.")
    A("`cuerpo s/a` = unidades del cuerpo que el índice no anuncia.")
    A("`front.` = fronteras intra-palabra antes → después de la regla 2.")
    A("")
    A("| TO | título | pág | sec | term | mini | unid. | idx a/b | cuerpo s/a | rech. | front. | % tab | fórm | max chars | veredicto |")
    A("|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|")
    for ident in sorted(conteos, key=lambda i: (-conteos[i]["unidades_extraccion"], i)):
        c = conteos[ident]
        g = c["diagnostico"]
        tit = inv[ident]["titulo_oficial"].replace("|", "/")
        tit = tit[:60] + ("…" if len(tit) > 60 else "")
        A(f"| {ident} | {tit} | {c['paginas']} | {c['secciones']} | {c['chunks_terminales']} | "
          f"{c['mini_chunks']} | {c['unidades_extraccion']} | "
          f"{g['indice']['anunciado_sin_cuerpo']}/{g['indice']['puntos_en_indice']} | "
          f"{g['indice']['en_cuerpo_sin_anunciar']} | {g['rechazos_header']['total']} | "
          f"{g['fronteras']['intra_palabra_antes']}→{g['fronteras']['intra_palabra_despues']} | "
          f"{g['tabular']['pct_chunks_tabulares']:.1f} | {g['tabular']['chunks_con_formula']} | "
          f"{g['escala']['max_chars_propio_terminal']} | "
          f"{'digerible' if veredictos[ident]['veredicto'] == 'digerible' else '**necesita reglas**'} |")
    A("")

    causas = {}
    causa_path = PREP / "causa_sin_estructura.json"
    if causa_path.exists():
        causas = json.loads(causa_path.read_text(encoding="utf-8"))
    if causas:
        agrup: dict[str, list[str]] = {}
        for ident, c in causas.items():
            agrup.setdefault(c["causa"], []).append(ident)
        A("## 5. Causa raíz de los TOs sin estructura (fallo H2)")
        A("")
        A(f"{len(causas)} TOs no producen ninguna unidad. `code/causa_sin_estructura.py` "
          "separa el mecanismo, porque cada uno pide una regla distinta:")
        A("")
        A("| causa | TOs | cuáles |")
        A("|---|--:|---|")
        for causa, ids in sorted(agrup.items(), key=lambda kv: -len(kv[1])):
            A(f"| {causa} | {len(ids)} | {', '.join(sorted(ids))} |")
        A("")
        cat = {}
        for ident in causas:
            cat[inv[ident]["categoria"]] = cat.get(inv[ident]["categoria"], 0) + 1
        A(f"Reparto por categoría del índice oficial: "
          + ", ".join(f"{k}: {v}" for k, v in sorted(cat.items())) + ".")
        A("")
        A("Detalle por TO (roles de página, líneas con marca de índice, líneas "
          "`Sección N.`, primeras líneas del documento) en `causa_sin_estructura.json`.")
        A("")

    A("## 6. Evidencia de los TOs con veredicto «necesita reglas»")
    A("")
    if not ko:
        A("Ninguno.")
    for ident in sorted(ko, key=lambda i: -conteos[i]["unidades_extraccion"]):
        c = conteos[ident]
        g = c["diagnostico"]
        A(f"### {ident} — {inv[ident]['titulo_oficial']}")
        A("")
        A(f"`{inv[ident]['archivo_oficial']}`, {c['paginas']} páginas "
          f"({c['paginas_cuerpo']} de cuerpo), {c['unidades_extraccion']} unidades "
          f"({c['chunks_terminales']} terminales + {c['mini_chunks']} mini-chunks).")
        A("")
        A("Criterios incumplidos:")
        for f in veredictos[ident]["fallas"]:
            A(f"- {f}")
        if veredictos[ident]["flags"]:
            A("")
            A("Señales adicionales (no deciden el veredicto):")
            for f in veredictos[ident]["flags"]:
                A(f"- {f}")
        A("")
        A(f"Roles de página: {json.dumps(c['roles_pagina'], ensure_ascii=False)}. "
          f"Rechazos de header por motivo: "
          f"{json.dumps(g['rechazos_header']['por_motivo'], ensure_ascii=False)}. "
          f"Avisos por tipo: {json.dumps(g['avisos']['por_tipo'], ensure_ascii=False)}.")
        A("")
        A(f"Detalle completo en `e0_dry/{ident}/` "
          f"(`divergencias_{ident}.json`, `estructura_{ident}.json`, `chunks_{ident}.json`).")
        A("")

    A("## 7. TOs digeribles con señales de atención")
    A("")
    con_flag = [i for i in ok if veredictos[i]["flags"]]
    if not con_flag:
        A("Ninguno.")
    for ident in sorted(con_flag, key=lambda i: -conteos[i]["unidades_extraccion"]):
        A(f"- **{ident}** ({inv[ident]['titulo_oficial']}): "
          + "; ".join(veredictos[ident]["flags"]))
    A("")

    (PREP / "reporte_generalizacion.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"digeribles={len(ok)} necesitan_reglas={len(ko)} abortados={len(fallos)}")
    print("necesitan reglas:", ", ".join(sorted(ko)))


if __name__ == "__main__":
    main()
