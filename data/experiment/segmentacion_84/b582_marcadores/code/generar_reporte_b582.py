#!/usr/bin/env python3
"""B5.8.2 — reporte de la corrida de reglas de marcador, regenerable desde
conteos_b582.json (correr_b582.py) y censo_84.json. Cero LLM.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b582_marcadores/code/generar_reporte_b582.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
SALIDA = Path(__file__).resolve().parents[1]
CENSO = REPO / "data/experiment/segmentacion_84/censo_84.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from correr_b582 import CONTROL_EXTRA, tos_objetivo  # noqa: E402


def main() -> None:
    conteos = json.load(open(SALIDA / "conteos_b582.json", encoding="utf-8"))
    censo = json.load(open(CENSO, encoding="utf-8"))
    objetivo = tos_objetivo()

    rinden = sorted(t for t in objetivo if conteos[t]["rinde"])
    no_rinden = sorted(t for t in objetivo if not conteos[t]["rinde"])
    sanos = sorted(t for t in objetivo if conteos[t]["healthcheck_veredicto"] == "sano")
    u_total = sum(conteos[t]["unidades_extraccion"] for t in objetivo)
    por_modo = {m: sorted(t for t in objetivo if conteos[t]["modo_lectura"] == m)
                for m in ("marcadores", "sin_raiz", "vigente")}

    L = []
    L.append("# B5.8.2 — corrida de las reglas de marcador por familia\n")
    L.append("Reporte regenerable con:\n")
    L.append("```bash")
    L.append("python3 data/experiment/segmentacion_84/b582_marcadores/code/correr_b582.py")
    L.append("python3 data/experiment/segmentacion_84/b582_marcadores/code/generar_reporte_b582.py")
    L.append("```\n")
    L.append(f"Objetivo (recomputado de `censo_84.json`, familias b_idx/b_sec con "
             f"veredicto que REMITE a la regla de marcador de B5.8.2): "
             f"**{len(objetivo)} TOs**. El octavo TO de la familia b_idx del censo "
             f"(ri_tsa, veredicto «regla vigente (B5.2)») corre como CONTROL "
             f"declarado: produce unidades por el camino vigente y se espera que "
             f"JAMÁS entre a las etapas nuevas; su re-corrida adjudicada es de "
             f"B5.8.4.\n")
    L.append("## 1. Resultado agregado\n")
    L.append(f"- **Rinden {len(rinden)}/{len(objetivo)}** (unidades > 0 y ≥1 raíz "
             f"de lectura), {u_total} unidades de extracción en total.")
    L.append(f"- Por etapa que produjo la lectura: marcadores "
             f"{len(por_modo['marcadores'])} ({', '.join(por_modo['marcadores'])}); "
             f"sin_raiz sobre roles de marcadores {len(por_modo['sin_raiz'])} "
             f"({', '.join(por_modo['sin_raiz'])}).")
    L.append(f"- Health-check 'sano': {len(sanos)}/{len(objetivo)}; el resto "
             f"declara señales (detalle §2).")
    if no_rinden:
        L.append(f"- No rinden: {', '.join(no_rinden)} (causa por TO en §2).")
    for t in (t for t in CONTROL_EXTRA if t in conteos):
        c = conteos[t]
        L.append(f"- Control {t}: modo={c['modo_lectura']}, activado_por_cero="
                 f"{'sí' if c['activado_por_cero_unidades'] else 'NO'} — esperado "
                 f"modo vigente sin activación (un TO que produce unidades jamás "
                 f"entra a las etapas nuevas).")
    L.append("")
    L.append("## 2. Tabla por TO\n")
    L.append("| TO | fam | pág | modo | roles (índice/cuerpo) | secciones/raíces | "
             "unid. (term.+mini) | sub-chunk | rechazos | saltos | cob. | salud | rinde |")
    L.append("|---|---|--:|---|---|---|--:|---|--:|--:|---|---|---|")
    ctl = [t for t in CONTROL_EXTRA if t in conteos]
    for t in objetivo + ctl:
        c = conteos[t]
        r = c["roles_pagina"]
        salud = ("sano" if c["healthcheck_veredicto"] == "sano"
                 else ",".join(c["healthcheck_veredicto"]))
        sub = (f"{c['sub_chunking']['particiones']}p/"
               f"{c['sub_chunking']['no_particionables']}np"
               if (c["sub_chunking"]["particiones"]
                   or c["sub_chunking"]["no_particionables"]) else "—")
        secs = ",".join(c["secciones_por_numero"][:10])
        if len(c["secciones_por_numero"]) > 10:
            secs += ",…"
        L.append(f"| {t} | {censo[t]['familia_primaria']} | {c['paginas']} "
                 f"| {c['modo_lectura']} "
                 f"| {r.get('indice', 0)}/{r.get('cuerpo', 0)} "
                 f"| {secs} "
                 f"| {c['unidades_extraccion']} "
                 f"({c['chunks_terminales']}+{c['mini_chunks']}) | {sub} "
                 f"| {c['rechazos_header']} | {c['saltos_numeracion']} "
                 f"| {'sí' if c['cobertura_exacta'] else 'NO'} | {salud} "
                 f"| {'sí' if c['rinde'] else 'NO'} |")
    L.append("")
    L.append("## 3. Verificaciones transversales\n")
    todos = objetivo + ctl
    cob_no = sorted(t for t in todos if not conteos[t]["cobertura_exacta"])
    L.append(f"- Cobertura exacta (cero pérdida) en "
             f"{len(todos) - len(cob_no)}/{len(todos)} TOs"
             + (f"; sin cobertura exacta: {', '.join(cob_no)}." if cob_no else "."))
    sin_act = sorted(t for t in objetivo
                     if not conteos[t]["activado_por_cero_unidades"])
    L.append("- Activación por cero unidades vigentes en los "
             f"{len(objetivo)} objetivo: "
             + (f"{len(objetivo)}/{len(objetivo)} (todos comprobaron cero "
                "unidades por el camino vigente antes de entrar)."
                if not sin_act else
                f"NO activaron: {', '.join(sin_act)}."))
    con_sub = sorted(t for t in todos
                     if conteos[t]["sub_chunking"]["particiones"]
                     or conteos[t]["sub_chunking"]["no_particionables"])
    L.append(f"- Sub-chunking de U-B5.3 sobre unidades nuevas: interviene en "
             f"{len(con_sub)} TOs ({', '.join(con_sub) if con_sub else '—'})"
             f"{'; detalle en `<to>/sub_chunking_<to>.json`.' if con_sub else '.'}")
    L.append("- Límite medido DECLARADO (sin regla nueva, territorio B5.8.4): "
             "nmaeef — reinicio de numeración por ANEXO (jerarquía alternativa): "
             "el marcador de índice se reconoce y el modo sin raíz abre "
             f"{conteos['nmaeef']['raices_de_lectura']} raíces, pero las raíces "
             "1–11 provienen de la página-lista del Anexo I y el cuerpo de los "
             "anexos posteriores ancla bajo la última raíz abierta "
             f"({conteos['nmaeef']['rechazos_header']} rechazos registrados, "
             "señal C8 con partición de sub-chunking); mismo patrón que "
             "ri_tar/ri_transpa en B5.8.1.")
    L.append("")
    (SALIDA / "reporte_b582.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"reporte -> {SALIDA / 'reporte_b582.md'}")


if __name__ == "__main__":
    main()
