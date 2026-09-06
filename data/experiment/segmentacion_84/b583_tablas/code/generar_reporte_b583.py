#!/usr/bin/env python3
"""B5.8.3 — reporte regenerable desde los artefactos json de la corrida
(correr_b583.py). No re-parsea nada: lee ../conteos_b583.json, los
resumen_<to>.json y ../testigo_capmin/testigo_rx10.json.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b583_tablas/code/generar_reporte_b583.py
"""

from __future__ import annotations

import json
from pathlib import Path

SALIDA = Path(__file__).resolve().parents[1]


def main() -> None:
    cons = json.load(open(SALIDA / "conteos_b583.json", encoding="utf-8"))
    meta = cons.pop("_meta")
    testigo = json.load(open(SALIDA / "testigo_capmin" / "testigo_rx10.json",
                             encoding="utf-8"))

    tos = sorted(cons)
    rinden = [t for t in tos if cons[t]["rinde"]]
    tot = {k: sum(cons[t][k] for t in tos)
           for k in ("tablas_logicas", "parseadas", "declaradas", "segmentos",
                     "costuras_aplicadas", "filas_total", "notas_pie",
                     "paginas_con_tabla_contenido")}

    L: list[str] = []
    L.append("# B5.8.3 — corrida del parser de tablas (e0_tablas.py)\n")
    L.append("Reporte regenerable con:\n")
    L.append("```bash")
    L.append("python3 data/experiment/segmentacion_84/b583_tablas/code/correr_b583.py")
    L.append("python3 data/experiment/segmentacion_84/b583_tablas/code/generar_reporte_b583.py")
    L.append("```\n")
    L.append(f"Objetivo (recomputado — regla i): **{len(tos)} TOs** = "
             f"{len(meta['de_censo'])} con familia tabular d/d_dominante en el "
             f"censo B5.8.0 ∪ {len(meta['de_b581'])} con páginas ficha_registro "
             f"declaradas por B5.8.1 (solo por esta vía: "
             f"{', '.join(sorted(set(meta['de_b581']) - set(meta['de_censo'])))}). "
             "Control testigo aparte: capmin (dev, RX-10).\n")
    L.append("## 1. Resultado agregado\n")
    L.append(f"- **Rinden {len(rinden)}/{len(tos)}** (≥1 tabla lógica parseada): "
             f"{tot['parseadas']} tablas parseadas de {tot['tablas_logicas']} "
             f"lógicas ({tot['declaradas']} declaradas con causa, no emitidas), "
             f"{tot['segmentos']} segmentos físicos, "
             f"{tot['costuras_aplicadas']} costuras aplicadas, "
             f"{tot['filas_total']} filas, {tot['notas_pie']} notas al pie "
             f"asociadas, sobre {tot['paginas_con_tabla_contenido']} páginas "
             "con tabla de contenido.")
    no_rinden = [t for t in tos if not cons[t]["rinde"]]
    for t in no_rinden:
        d = cons[t]["descartadas_por_regla"]
        L.append(f"- **{t} NO rinde, declarado**: 0 tablas de contenido con "
                 f"contenido (descartes por regla: {d}); su material dominante "
                 "es ficha de registro — parser de registro, fuera de "
                 "B5.8.1-3 (censo B5.8.0), adjudicación en B5.8.4.")
    L.append(f"- **Testigo RX-10 (capmin 1.2): resuelto={testigo['resuelto']}** — "
             f"pares por columna {testigo['pares_por_columna']} (el chunk "
             "linealizado había invertido los montos en el grafo); pérdida de "
             f"reconstrucción {testigo['pct_perdida']}.\n")
    L.append("## 2. Tabla por TO\n")
    L.append("| TO | pág | pág c/tabla | lógicas | parseadas | declaradas | "
             "segmentos | costuras | cand. | filas | notas | títulos | rinde |")
    L.append("|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|")
    for t in tos:
        c = cons[t]
        L.append(f"| {t} | {c['paginas']} | {c['paginas_con_tabla_contenido']} "
                 f"| {c['tablas_logicas']} | {c['parseadas']} | {c['declaradas']} "
                 f"| {c['segmentos']} | {c['costuras_aplicadas']} "
                 f"| {len(c['costuras_candidatas'])} | {c['filas_total']} "
                 f"| {c['notas_pie']} | {c['titulos_detectados']} "
                 f"| {'sí' if c['rinde'] else 'NO'} |")
    L.append("")
    L.append("## 3. Tablas declaradas (guardas: se declaran, no se emiten mal)\n")
    hubo = False
    for t in tos:
        for d in cons[t]["declaradas_detalle"]:
            hubo = True
            det = (f"colapso en columna {d['colapsos'][0]['columna']} "
                   f"({d['colapsos'][0]['fragmentos']} fragmentos)"
                   if d["colapsos"] else
                   f"pérdida de reconstrucción {d['pct_perdida_max']:.0%}")
            L.append(f"- `{d['id']}` (p.{d['pagina']}): {d['causas']} — {det}.")
    if not hubo:
        L.append("- (ninguna)")
    L.append("")
    L.append("## 4. Costuras candidatas no fusionadas (geometría sin "
             "encabezado repetido — se declaran, jamás se cosen)\n")
    n_cand = sum(len(cons[t]["costuras_candidatas"]) for t in tos)
    L.append(f"Total: {n_cand}. Detalle por TO en "
             "`<to>/resumen_<to>.json` (clave `costuras_candidatas`) y filas "
             "completas en `<to>/tablas_<to>.json`.\n")
    L.append("## 5. Verificación de reconstrucción (decisión 4)\n")
    chars_perdidos = sum(cons[t]["chars_perdidos_total"] for t in tos)
    L.append(f"- Caracteres perdidos declarados (todas las tablas, parseadas y "
             f"declaradas): {chars_perdidos}. Toda tabla parseada con pérdida "
             "> 20 % fue movida a declarada (regla R-VERIF); el detalle por "
             "segmento vive en `tablas_<to>.json` → `verificacion`.")
    L.append("")
    (SALIDA / "reporte_b583.md").write_text("\n".join(L), encoding="utf-8")
    print(f"reporte en {SALIDA / 'reporte_b583.md'}")


if __name__ == "__main__":
    main()
