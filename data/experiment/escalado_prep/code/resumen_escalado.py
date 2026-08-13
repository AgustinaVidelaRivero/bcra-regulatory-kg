"""Genera ../resumen_escalado.md: inventario de unidades + proyección de costo
(punto e) y catálogo de sujetos (punto f), en forma legible.

Todos los números salen de los JSON/CSV producidos por los otros scripts; este
documento no calcula nada nuevo.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

AQUI = Path(__file__).resolve().parent
PREP = AQUI.parent

TOP = 25


def main() -> None:
    proy = json.loads((PREP / "proyeccion_costo.json").read_text(encoding="utf-8"))
    suj = json.loads((PREP / "catalogo_sujetos.json").read_text(encoding="utf-8"))
    ver = json.loads((PREP / "veredictos_generalizacion.json").read_text(
        encoding="utf-8"))["por_to"]
    inv = {f["id"]: f for f in csv.DictReader(
        (PREP / "inventario_tos.csv").open(encoding="utf-8"))}

    t, ag, filas = proy["tarifas"], proy["agregado"], proy["por_to"]
    L: list[str] = []
    A = L.append

    A("# Inventario de unidades, proyección de costo y catálogo de sujetos")
    A("")
    A("Fase A del escalado. Gasto de esta unidad: **USD 0** (cero llamadas a LLM).")
    A("")
    A("## 1. Tarifas reales del corpus v2")
    A("")
    A(f"Fuente del gasto: `{t['fuente_gasto']}`, clave `fases_cerradas`.")
    A(f"Fuente de los caracteres: `{t['fuente_chars']}` (chunks sellados de E0).")
    A("")
    A("```bash")
    A("python3 -c \"import json; d=json.load(open('data/experiment/reextraccion_v2/"
      "corpus_v2/salida/estado_corpus.json'))['fases_cerradas']; "
      "print({k: (v['gasto_usd'], v['resumen']['n']) for k,v in d.items() if ':' in k})\"")
    A("```")
    A("")
    A("| fase | gasto USD | unidades | USD/unidad | chars propios | USD/char |")
    A("|---|--:|--:|--:|--:|--:|")
    for k in sorted(t["detalle_por_to_fase"]):
        d = t["detalle_por_to_fase"][k]
        marca = "  ← TO de calibración, excluido" if d["to_de_calibracion"] else ""
        A(f"| {k}{marca} | {d['gasto_usd']:.6f} | {d['n']} | {d['usd_por_unidad']:.6f} | "
          f"{d['chars_propio_to']} | {d['usd_por_char']:.3e} |")
    A("")
    A(f"Suma de las diez fases: USD {ag['referencia_corpus_v2']['gasto_total_corpus_5tos_usd']:.6f}. "
      "Con la re-extracción dirigida (USD 0,527699, misma fuente) da el total de la corrida del "
      "corpus registrado en el commit del grafo v2 final.")
    A("")
    A("`pro` queda fuera del cálculo de tarifas en ambas fases: fue el TO de calibración de")
    A("E0-E3 y entró a la corrida del corpus con la caché ya poblada — `pro:e1` costó USD 0,0")
    A("sobre 101 unidades y `pro:e3` USD 0,00205 por unidad, seis veces por debajo del")
    A("siguiente TO más barato. Los TOs nuevos no tienen caché previa.")
    A("")
    A("Tarifas usadas para proyectar:")
    A("")
    A("| fase | USD/unidad (agregado) | mín. por TO | máx. por TO | USD/char |")
    A("|---|--:|--:|--:|--:|")
    for f in ("e1", "e3"):
        d = t[f]
        A(f"| {f.upper()} | {d['usd_por_unidad_agregado']:.6f} | "
          f"{d['usd_por_unidad_min_to']:.6f} | {d['usd_por_unidad_max_to']:.6f} | "
          f"{d['usd_por_char_agregado']:.3e} |")
    A("")

    A("## 2. Inventario de unidades del universo nuevo")
    A("")
    A(f"- TOs: **{ag['tos_procesados']}** | páginas: **{ag['paginas_total']}**")
    A(f"- Chunks terminales: **{ag['chunks_terminales_total']}**")
    A(f"- Mini-chunks estructurales: **{ag['mini_chunks_total']}**")
    A(f"- **Unidades de extracción: {ag['unidades_extraccion_total']}** "
      f"({ag['chars_propio_total']} caracteres propios)")
    A("")
    A("Referencia: el corpus de 5 TOs tiene 1.763 unidades. Detalle por TO en")
    A("`inventario_unidades.csv` (152 filas, ordenado por unidades).")
    A("")

    A("## 3. Proyección de costo")
    A("")
    A("| concepto | USD |")
    A("|---|--:|")
    A(f"| E1 sobre {ag['unidades_extraccion_total']} unidades | {ag['usd_e1_central']:.2f} |")
    A(f"| E3 sobre {ag['unidades_extraccion_total']} unidades | {ag['usd_e3_central']:.2f} |")
    A(f"| **Total (tarifa agregada)** | **{ag['usd_total_central']:.2f}** |")
    A(f"| Banda baja (tarifa del TO más barato en cada fase) | {ag['usd_total_banda_baja']:.2f} |")
    A(f"| Banda alta (tarifa del TO más caro en cada fase) | {ag['usd_total_banda_alta']:.2f} |")
    A(f"| Contraste por caracteres, no por unidades | {ag['contraste_por_caracter']['usd_total']:.2f} |")
    A("")
    A("Las dos vías de proyección — por unidad y por carácter — caen a "
      f"{abs(ag['usd_total_central'] - ag['contraste_por_caracter']['usd_total']) / ag['usd_total_central'] * 100:.0f} %"
      " una de otra, así que la tarifa por unidad no está arrastrada por una diferencia de")
    A("tamaño de unidad entre el corpus v2 y el universo nuevo.")
    A("")
    A("### 3.1 Lo que esta cifra NO incluye")
    A("")
    pv, vo = ag["por_veredicto"], ag["volumen_oculto"]
    A(f"{vo['tos_con_0_unidades']} de los {ag['tos_procesados']} TOs producen **cero** unidades: "
      "E0 no engancha su estructura (ver `reporte_generalizacion.md` §5). Entran a la suma con")
    A("costo 0, que es correcto para «lo que el pipeline puede extraer hoy» y falso para «lo que")
    A("cuesta el universo completo».")
    A("")
    A("| corte | TOs | páginas | unidades | USD |")
    A("|---|--:|--:|--:|--:|")
    A(f"| digeribles | {pv['digerible']['tos']} | {pv['digerible']['paginas']} | "
      f"{pv['digerible']['unidades']} | {pv['digerible']['usd_total']:.2f} |")
    A(f"| necesitan reglas (lo que se ve hoy) | {pv['necesita_reglas']['tos']} | "
      f"{pv['necesita_reglas']['paginas']} | {pv['necesita_reglas']['unidades_visibles_hoy']} | "
      f"{pv['necesita_reglas']['usd_total_visible_hoy']:.2f} |")
    A("")
    A(f"Extrapolación del volumen invisible: los {vo['tos_con_0_unidades']} TOs sin estructura "
      f"suman {vo['paginas_de_esos_tos']} páginas. Aplicando la densidad de unidades por página")
    A("medida por categoría —")
    for k, d in vo["densidad_por_categoria"].items():
        A(f"  - {k}: {d['unidades_por_pagina']} unidades/página ({d['origen']})")
    A(f"— darían del orden de **{vo['unidades_estimadas_si_se_recuperan']} unidades** adicionales, "
      f"**USD {vo['usd_estimado_si_se_recuperan']:.2f}**. Es extrapolación, no medición: el volumen")
    A("real solo se conoce después de escribir las reglas de parseo.")
    A("")
    A(f"Techo del escalado completo, sumando ambas partes: del orden de "
      f"**USD {ag['usd_total_central'] + vo['usd_estimado_si_se_recuperan']:.0f}** en E1+E3, sobre "
      f"~{ag['unidades_extraccion_total'] + vo['unidades_estimadas_si_se_recuperan']} unidades. "
      "No incluye E2 (determinístico, USD 0), re-extracción dirigida, ni reintentos por cola.")
    A("")
    A("### 3.2 Los 25 TOs más caros")
    A("")
    A("| TO | título | unidades | USD E1 | USD E3 | USD total | veredicto |")
    A("|---|---|--:|--:|--:|--:|---|")
    for f in filas[:TOP]:
        tit = f["titulo_oficial"].replace("|", "/")
        tit = tit[:52] + ("…" if len(tit) > 52 else "")
        A(f"| {f['id']} | {tit} | {f['unidades_extraccion']} | {f['usd_e1']:.2f} | "
          f"{f['usd_e3']:.2f} | {f['usd_total']:.2f} | {f['veredicto']} |")
    A("")

    A("## 4. Catálogo de sujetos: presión de fusión cross-TO")
    A("")
    A("Proxy léxico determinístico sobre el texto que E0 extrajo, contra el catálogo cerrado de")
    A("`data/experiment/grafo_v2/esquema_v2_clases.json` (65 entradas). **No es adjudicación**: "
      "quién es sujeto de una norma lo decide E1, que no se corre en esta unidad.")
    A("")
    con_texto = {i: v for i, v in suj.items() if v["unidades_extraccion"] > 0}
    A(f"Cobertura del análisis: {len(con_texto)} de {len(suj)} TOs producen texto; los otros no "
      "aportan evidencia léxica porque E0 no los engancha.")
    A("")
    from collections import Counter
    tot = Counter()
    for v in con_texto.values():
        for cid in v["sujetos_catalogo_presentes"]:
            tot[cid] += 1
    A("### 4.1 Entradas del catálogo que reaparecen en el universo nuevo")
    A("")
    A(f"{len(tot)} de las 65 entradas del catálogo aparecen en al menos un TO nuevo. Cada una de")
    A("ellas es un punto de fusión cross-TO: el ensamblado une nodos por id canónico, mecanismo")
    A("ya medido en el corpus de 5 TOs (`reporte_ensamblado.json` → `merges_cross_to`, 27 merges,")
    A("21 de tipo `Sujeto`).")
    A("")
    A("| entrada del catálogo | TOs que la mencionan |")
    A("|---|--:|")
    for cid, n in tot.most_common(TOP):
        A(f"| `{cid}` | {n} |")
    A("")
    A("### 4.2 TOs con más presión de fusión")
    A("")
    A("| TO | título | unidades | entradas de catálogo distintas |")
    A("|---|---|--:|--:|")
    for i, v in sorted(con_texto.items(),
                       key=lambda kv: -kv[1]["n_sujetos_catalogo"])[:TOP]:
        tit = v["titulo_oficial"].replace("|", "/")
        tit = tit[:50] + ("…" if len(tit) > 50 else "")
        A(f"| {i} | {tit} | {v['unidades_extraccion']} | {v['n_sujetos_catalogo']} |")
    A("")

    A("## 5. Catálogo de sujetos: candidatos a clase nueva")
    A("")
    nuevos_tit = [i for i, v in suj.items() if v["titulo_introduce_sujeto_nuevo"]]
    A(f"### 5.1 TOs cuyo título nombra un sujeto ausente del catálogo ({len(nuevos_tit)})")
    A("")
    if not nuevos_tit:
        A("Ninguno.")
    for i in nuevos_tit:
        v = suj[i]
        A(f"- **{i}** ({v['titulo_oficial']}) — núcleo detectado: "
          f"«{v['sujeto_del_titulo']['nucleo_detectado']}»; unidades hoy: "
          f"{v['unidades_extraccion']}.")
    A("")
    con_cand = {i: v for i, v in con_texto.items() if v["n_candidatos"]}
    A(f"### 5.2 Sintagmas frecuentes fuera del catálogo ({len(con_cand)} TOs con al menos uno)")
    A("")
    A("Screening: sintagma encabezado por un núcleo nominal del propio catálogo, podado de")
    A("artículos, preposiciones y verbos, con al menos 5 apariciones en el TO. Cada uno es un")
    A("candidato a adjudicar, no un sujeto confirmado.")
    A("")
    for i, v in sorted(con_cand.items(), key=lambda kv: -kv[1]["n_candidatos"])[:TOP]:
        A(f"**{i}** — {v['titulo_oficial']}")
        A("")
        for c in v["candidatos_sujeto_nuevo"][:5]:
            ej = c["ejemplo"].replace("|", "/")
            A(f"- «{c['frase']}» ×{c['ocurrencias']}"
              + (f" — *{ej}*" if ej else ""))
        A("")
    A("Listado completo por TO en `catalogo_sujetos.json` y `catalogo_sujetos_resumen.csv`.")
    A("")

    A("## 6. Qué queda abierto")
    A("")
    A("- **D5 — definición del corpus.** Los 152 TOs son el universo publicado, no el corpus")
    A("  elegido. La selección es decisión pendiente con los mentores.")
    A("- El catálogo cerrado de sujetos fue construido sobre 5 TOs. Escalar sin ampliarlo")
    A("  empujaría a E1 a `sujeto_propuesto` masivo, que es exactamente lo que alimenta la")
    A("  cuarentena.")
    A("- Los TOs con veredicto «necesita reglas» no tienen todavía decisión: excluirlos,")
    A("  escribir reglas de parseo, o dejarlos para una segunda vuelta.")
    A("")

    (PREP / "resumen_escalado.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"escrito resumen_escalado.md ({len(L)} líneas)")


if __name__ == "__main__":
    main()
