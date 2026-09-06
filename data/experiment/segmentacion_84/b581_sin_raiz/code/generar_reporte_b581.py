#!/usr/bin/env python3
"""B5.8.1 — reporte de la corrida del modo sin raíz, regenerable desde
conteos_b581.json (correr_b581.py) y censo_84.json. Cero LLM.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b581_sin_raiz/code/generar_reporte_b581.py
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[5]
SALIDA = Path(__file__).resolve().parents[1]
CENSO = REPO / "data/experiment/segmentacion_84/censo_84.json"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from correr_b581 import CONTROL_EXTRA, tos_objetivo  # noqa: E402


def main() -> None:
    conteos = json.load(open(SALIDA / "conteos_b581.json", encoding="utf-8"))
    censo = json.load(open(CENSO, encoding="utf-8"))
    objetivo = tos_objetivo()
    parciales = sorted(t for t in objetivo
                       if censo[t]["veredicto_preliminar"].startswith("parcialmente"))

    rinden = sorted(t for t in objetivo if conteos[t]["rinde"])
    no_rinden = sorted(t for t in objetivo if not conteos[t]["rinde"])
    sanos = sorted(t for t in objetivo if conteos[t]["healthcheck_veredicto"] == "sano")
    u_total = sum(conteos[t]["unidades_extraccion"] for t in objetivo)

    L = []
    L.append("# B5.8.1 — corrida del modo de lectura sin raíz de sección\n")
    L.append("Reporte regenerable con:\n")
    L.append("```bash")
    L.append("python3 data/experiment/segmentacion_84/b581_sin_raiz/code/correr_b581.py")
    L.append("python3 data/experiment/segmentacion_84/b581_sin_raiz/code/generar_reporte_b581.py")
    L.append("```\n")
    L.append(f"Objetivo (recomputado de `censo_84.json`, familias a/c con veredicto "
             f"que REMITE a B5.8.1): **{len(objetivo)} TOs** "
             f"({len(objetivo) - len(parciales)} plenos + {len(parciales)} parciales: "
             f"{', '.join(parciales)}). Control adicional declarado: "
             f"{', '.join(CONTROL_EXTRA)} (familia a sin espina utilizable, vía "
             f"B5.8.3; se espera que NO rinda). La fila del plan de reglas del censo "
             f"dice 42 porque su corte es «familia a/c y no candidato», que suma "
             f"ri_acsf y no remite a B5.8.1 — discrepancia declarada, no ajustada.\n")
    L.append(f"## 1. Resultado agregado\n")
    L.append(f"- **Rinden {len(rinden)}/{len(objetivo)}** (unidades > 0 y ≥1 raíz "
             f"de lectura), {u_total} unidades de extracción en total.")
    L.append(f"- Health-check 'sano': {len(sanos)}/{len(objetivo)}; el resto "
             f"declara señales (detalle §2).")
    if no_rinden:
        L.append(f"- No rinden: {', '.join(no_rinden)} (causa por TO en §2).")
    ctl = [t for t in CONTROL_EXTRA if t in conteos]
    for t in ctl:
        c = conteos[t]
        L.append(f"- Control {t}: rinde={'sí' if c['rinde'] else 'NO'} "
                 f"(raíces {c['raices_de_lectura']}, unidades "
                 f"{c['unidades_extraccion']}) — esperado NO, vía B5.8.3.")
    L.append("")
    L.append("## 2. Tabla por TO\n")
    L.append("| TO | fam | pág | roles (cuerpo/registro) | raíces (impl.) | unid. "
             "(term.+mini) | sub-chunk | rechazos | cob. | salud | rinde |")
    L.append("|---|---|--:|---|--:|--:|---|--:|---|---|---|")
    for t in objetivo + ctl:
        c = conteos[t]
        r = c["roles_pagina"]
        salud = ("sano" if c["healthcheck_veredicto"] == "sano"
                 else ",".join(c["healthcheck_veredicto"]))
        sub = (f"{c['sub_chunking']['particiones']}p/"
               f"{c['sub_chunking']['no_particionables']}np"
               if (c["sub_chunking"]["particiones"]
                   or c["sub_chunking"]["no_particionables"]) else "—")
        L.append(f"| {t} | {censo[t]['familia_primaria']} | {c['paginas']} "
                 f"| {r.get('cuerpo', 0)}/{r.get('ficha_registro', 0)} "
                 f"| {c['raices_de_lectura']} ({c['raices_implicitas']}) "
                 f"| {c['unidades_extraccion']} "
                 f"({c['chunks_terminales']}+{c['mini_chunks']}) | {sub} "
                 f"| {c['rechazos_header']} "
                 f"| {'sí' if c['cobertura_exacta'] else 'NO'} | {salud} "
                 f"| {'sí' if c['rinde'] else 'NO'} |")
    L.append("")
    L.append("## 3. Verificaciones transversales\n")
    cob_ok = sorted(t for t in objetivo + ctl if not conteos[t]["cobertura_exacta"])
    L.append(f"- Cobertura exacta (cero pérdida) en "
             f"{len(objetivo) + len(ctl) - len(cob_ok)}/{len(objetivo) + len(ctl)} TOs"
             + (f"; sin cobertura exacta: {', '.join(cob_ok)}." if cob_ok else "."))
    activados = sorted(t for t in objetivo + ctl
                       if not conteos[t]["activado_por_cero_unidades"])
    L.append("- Activación por cero unidades vigentes: "
             + ("42/42 (todos los TOs de la corrida entraron al modo tras "
                "comprobar cero unidades por el camino vigente)."
                if not activados else
                f"NO activaron (produjeron unidades vigentes): {', '.join(activados)}."))
    con_sub = sorted(t for t in objetivo + ctl
                     if conteos[t]["sub_chunking"]["particiones"]
                     or conteos[t]["sub_chunking"]["no_particionables"])
    L.append(f"- Sub-chunking de U-B5.3 sobre unidades nuevas: interviene en "
             f"{len(con_sub)} TOs ({', '.join(con_sub)}); detalle en "
             f"`<to>/sub_chunking_<to>.json`.")
    L.append("")
    (SALIDA / "reporte_b581.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"reporte -> {SALIDA / 'reporte_b581.md'}")


if __name__ == "__main__":
    main()
