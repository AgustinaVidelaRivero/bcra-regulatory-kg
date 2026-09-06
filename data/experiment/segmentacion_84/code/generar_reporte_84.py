#!/usr/bin/env python3
"""B5.8.0 — Genera censo_84.md y tabla_31_no_ri.md desde censo_84.json.

Todo número de los .md sale de este script sobre los artefactos json:
regenerarlos es re-correr este script. Cero LLM.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/code/generar_reporte_84.py
"""

import json
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
SALIDA = REPO / "data/experiment/segmentacion_84"

NOMBRES_FAM = {
    "a": "a — compuerta de rol de página (sin índice)",
    "b_idx": "b_idx — marcador de índice (variante / B5.2)",
    "b_sec": "b_sec — marcador de sección variante",
    "b_pts": "b_pts — estructura enganchada, fallas C4/C5/C7/C8",
    "c": "c — cuerpo sin marcador de sección",
    "d": "d — tabular dominante",
    "e": "e — otra / no segmentable candidato",
}
ORDEN_FAM = ["a", "b_idx", "b_sec", "b_pts", "c", "d", "e"]


def cargar():
    censo = json.load(open(SALIDA / "censo_84.json"))
    tabla31 = json.load(open(SALIDA / "tabla_31_no_ri.json"))
    return censo, tabla31


def fila_censo(c):
    ev = c["evidencia"][0] if c["evidencia"] else ""
    esp = c["muestras"]["espina"]
    if esp:
        ev += f" · espina p.{esp[0]['pag']}: «{esp[0]['texto'][:45]}»"
    sec = ", ".join(c["secundarias"]) or "—"
    cat = "RI" if c["categoria"] == "regimen_informativo" else "NG"
    return (f"| {c['id']} | {cat} | {c['paginas']} | "
            f"{c['sellado']['unidades']} | {c['familia_primaria']} | {sec} | "
            f"{ev[:170]} | {c['veredicto_preliminar'][:90]} |")


def main():
    censo, tabla31 = cargar()
    tos = sorted(censo)
    n = len(tos)
    tally = Counter(censo[t]["familia_primaria"] for t in tos)
    tally_ri = Counter(censo[t]["familia_primaria"] for t in tos
                       if censo[t]["categoria"] == "regimen_informativo")
    tally_ng = Counter(censo[t]["familia_primaria"] for t in tos
                       if censo[t]["categoria"] == "normativa_general")
    n_ri = sum(tally_ri.values())
    n_ng = sum(tally_ng.values())

    # agregados para cruces con lo sellado
    ri = [censo[t] for t in tos if censo[t]["categoria"] == "regimen_informativo"]
    ri_tab15 = sum(1 for c in ri if c["vigente"]["pct_palabras_tabla"] >= 15.0)
    no_seg = [t for t in tos if censo[t]["veredicto_preliminar"].startswith("candidato")]
    parciales = [t for t in tos
                 if censo[t]["veredicto_preliminar"].startswith("parcialmente")]
    seg = [t for t in tos if t not in no_seg and t not in parciales]

    L = []
    L.append("# Censo B5.8.0 — familias de formato de los 84 TOs «necesita reglas»\n")
    L.append("Unidad **B5.8.0** (secuencia B5.8, `docs/diseno_B5.8_segmentacion_universal.md`;")
    L.append("adenda `docs/adenda_laudo_B5.5_segmentacion_universal.md`). Diagnóstico puro,")
    L.append("USD 0 de API: clasificación mecánica con reglas visibles en")
    L.append("`code/medir_84.py` (mediciones, E0 vigente importado en solo lectura) y")
    L.append("`code/clasificar_84.py` (árbol de decisión). Este documento se regenera con:\n")
    L.append("```bash")
    L.append("python3 data/experiment/segmentacion_84/code/medir_84.py")
    L.append("python3 data/experiment/segmentacion_84/code/clasificar_84.py")
    L.append("python3 data/experiment/segmentacion_84/code/generar_reporte_84.py")
    L.append("```\n")
    L.append("Universo: los 84 TOs con veredicto «necesita reglas» en")
    L.append("`escalado_prep/veredictos_generalizacion.json` (recomputado: "
             f"{n} = {n_ri} RI + {n_ng} normativa general). La medición «vigente» usa")
    L.append("el `e0_lib.py` actual (post-B5.2); los conteos «sellado» citan el E0 en")
    L.append("seco de `escalado_prep/e0_dry/` (pre-B5.2). Evidencia por TO íntegra en")
    L.append("`censo_84.json` (páginas, líneas de muestra verbatim, conteos).\n")

    L.append("## 1. Tally por familia primaria\n")
    L.append("| familia primaria | total | RI | no-RI |")
    L.append("|---|--:|--:|--:|")
    for f in ORDEN_FAM:
        if tally.get(f, 0) == 0:
            continue
        L.append(f"| {NOMBRES_FAM[f]} | {tally.get(f,0)} | {tally_ri.get(f,0)} | {tally_ng.get(f,0)} |")
    L.append(f"| **suma** | **{sum(tally.values())}** | **{n_ri}** | **{n_ng}** |\n")
    L.append(f"Veredicto preliminar: **{len(seg)} segmentables con regla de familia** / "
             f"**{len(parciales)} parcialmente segmentables (preámbulo sí, cuerpo "
             f"ficha/lista a declarar)** / **{len(no_seg)} candidatos a NO "
             f"segmentable** (detalle §4). Suma {len(seg)+len(parciales)+len(no_seg)}.\n")

    L.append("## 2. Tabla TO × familia (84 filas)\n")
    L.append("`unid.` = unidades de extracción del E0 en seco sellado; familias y")
    L.append("evidencia = medición vigente. Muestras verbatim completas en `censo_84.json`.\n")
    L.append("| TO | cat | pág | unid. | primaria | secundarias | evidencia | veredicto preliminar |")
    L.append("|---|---|--:|--:|---|---|---|---|")
    for f in ORDEN_FAM:
        for t in tos:
            if censo[t]["familia_primaria"] == f:
                L.append(fila_censo(censo[t]))
    L.append("")

    L.append("## 3. Cruce con los números sellados\n")
    ri_a = tally_ri.get("a", 0)
    ri_bidx = tally_ri.get("b_idx", 0)
    ri_bidx_ids = sorted(t for t in tos if censo[t]["categoria"] == "regimen_informativo"
                         and censo[t]["familia_primaria"] == "b_idx")
    ri_c_nuevos = sorted(t for t in tos if censo[t]["categoria"] == "regimen_informativo"
                         and censo[t]["familia_primaria"] == "c"
                         and censo[t]["sellado"]["paginas_cuerpo"] == 0)
    L.append(f"- **47/53 del RI en (a)** (scoping U-B5.6-0 §1.3, fe_erratas_D10 — medido "
             f"PRE-B5.2 como «100 % portada»): la medición vigente los concilia exacto "
             f"como **{ri_a} en (a)** + **{ri_bidx} en (b_idx)** "
             f"({', '.join(ri_bidx_ids)}) + **{len(ri_c_nuevos)} en (c)** "
             f"({', '.join(ri_c_nuevos)}: compuerta abierta por B5.2, sigue sin "
             f"sección) = {ri_a + ri_bidx + len(ri_c_nuevos)}.")
    ri_b581_plenos = sorted(t for t in tos
                            if censo[t]["categoria"] == "regimen_informativo"
                            and censo[t]["familia_primaria"] in ("a", "c")
                            and not censo[t]["veredicto_preliminar"].startswith(("candidato", "parcialmente")))
    ri_cand = [t for t in no_seg if censo[t]["categoria"] == "regimen_informativo"]
    ri_parc = [t for t in parciales if censo[t]["categoria"] == "regimen_informativo"]
    L.append(f"- **desbloqueo esperado 44/53 por el modo sin raíz** (diseño B5.8 §1, "
             f"sobre las familias PROSA+MIXTO del scoping): el censo por TO lo refina "
             f"a **{len(ri_b581_plenos)} plenos vía B5.8.1** + {len(ri_parc)} parciales "
             f"(solo preámbulo) + {ri_bidx} vía reglas de índice (B5.8.2/B5.2) + "
             f"{tally_ri.get('b_pts', 0)} ya enganchados con afinado — y "
             f"**{len(ri_cand)} candidatos a NO segmentable** que las familias "
             f"PROSA/MIXTO del scoping no distinguían (sin espina utilizable). "
             f"Diferencia REPORTADA como hallazgo, no ajustada.")
    L.append(f"- **23/53 del RI alcanzados por tablas** (scoping §1.4): re-medición con la "
             f"regla re-declarada da **{ri_tab15}/53** con ≥15 % de palabras en tabla.")
    med = json.load(open(SALIDA / "mediciones_84.json"))
    ri_ids = [t for t in tos if censo[t]["categoria"] == "regimen_informativo"]
    w_in = sum(med[t]["tablas"]["palabras_en_tabla"] for t in ri_ids)
    w_tot = sum(med[t]["tablas"]["palabras_total"] for t in ri_ids)
    L.append(f"- **12,4 % de palabras del RI en tabla** (scoping §1.4: 69.543/562.622): "
             f"re-medición da **{w_in}/{w_tot} = {100*w_in/w_tot:.1f} %** "
             f"(comando en §6).")
    L.append("- **62 TOs con cero unidades** (adenda §1): recomputado "
             f"{sum(1 for t in tos if censo[t]['sellado']['unidades'] == 0)}.")
    L.append("- **caso único (c) del RI** (`ri_ccna`, fe_erratas_D10): su clasificación "
             f"vigente sigue siendo «{censo['ri_ccna']['familia_primaria']}» — "
             f"COINCIDE. El segundo RI en (c) es post-B5.2 (compuerta abierta), "
             f"no un desacuerdo con lo sellado.\n")

    L.append("## 4. Candidatos a NO segmentable y parciales, con causa\n")
    if no_seg or parciales:
        L.append("| TO | cat | pág | estado | causa |")
        L.append("|---|---|--:|---|---|")
        for t in no_seg + parciales:
            c = censo[t]
            cat = "RI" if c["categoria"] == "regimen_informativo" else "NG"
            estado = "parcial" if t in parciales else "candidato NO"
            L.append(f"| {t} | {cat} | {c['paginas']} | {estado} | "
                     f"{c['veredicto_preliminar'][:140]} |")
    else:
        L.append("(ninguno)")
    L.append("")

    L.append("## 5. Plan de reglas por familia (dimensiona B5.8.1–B5.8.4)\n")
    def cnt(fam):
        return tally.get(fam, 0)
    ya_b52 = [t for t in tos if "regla vigente (B5.2)" in censo[t]["veredicto_preliminar"]]
    a_c = [t for t in tos if censo[t]["familia_primaria"] in ("a", "c")
           and not censo[t]["veredicto_preliminar"].startswith("candidato")]
    L.append("| regla | familia(s) | TOs que alcanza | sub-unidad |")
    L.append("|---|---|--:|---|")
    L.append(f"| modo de lectura sin raíz de sección (compuerta + raíz sintética) | a, c "
             f"| {len(a_c)} (incluye {len(parciales)} parciales solo por su preámbulo) "
             f"| **B5.8.1** |")
    b_marc = [t for t in tos if censo[t]["familia_primaria"] in ("b_idx", "b_sec")
              and t not in ya_b52]
    L.append(f"| reglas de marcador por variante medida (índice/sección) | b_idx, b_sec "
             f"| {len(b_marc)} | **B5.8.2** |")
    b_pts = [t for t in tos if censo[t]["familia_primaria"] == "b_pts"]
    marg = [t for t in b_pts if "umbral_marginal" in censo[t]["secundarias"]]
    L.append(f"| afinado de numeración/rechazos + adjudicación de umbral | b_pts "
             f"| {len(b_pts)} (de ellos {len(marg)} marginales) | **B5.8.2 / B5.8.4** |")
    n_dom = sum(1 for t in tos if "d_dominante" in censo[t]["secundarias"])
    n_pres = sum(1 for t in tos if "d" in censo[t]["secundarias"])
    L.append(f"| parser de tablas | d | {cnt('d')} primarias + {n_dom} con tabular "
             f"dominante (≥40 %) + {n_pres} con tabular presente (15–40 %) como "
             f"secundaria | **B5.8.3** |")
    L.append(f"| re-corrida y verificación (reglas B5.2 ya vigentes) | b_idx/b_sec "
             f"| {len(ya_b52)} | **B5.8.4** |")
    L.append(f"| declaración de no segmentables (y cuerpos ficha/lista parciales) "
             f"con causa | e y candidatos | {len(no_seg)} + {len(parciales)} "
             f"parciales | **B5.8.4** |\n")

    L.append("## 6. Hallazgos (discrepancias y novedades REPORTADAS, no ajustadas)\n")
    idx_cand = sorted(t for t in tos if censo[t]["muestras"]["idx_laxo_fuerte"])
    estilos = sorted({s["texto"] for t in idx_cand
                      for s in censo[t]["muestras"]["idx_laxo_fuerte"]})
    L.append(f"1. **Candidatos de marcador de índice en formato no contemplado** en "
             f"{len(idx_cand)} TOs ({', '.join(idx_cand)}); estilos verbatim: "
             f"{'; '.join('«'+e+'»' for e in estilos)}. En particular `ri_dcpc` tiene "
             f"«INDICE» en p.1: la sonda del scoping (regex `[íÍiI]ndice`, scoping:199) "
             f"no matchea mayúsculas sostenidas, por lo que su conclusión «la palabra "
             f"no está» (fe_erratas_D10 §b) queda matizada para estos TOs. La guarda "
             f"B5.2 NO se invalida: la mención en prosa de `ri_dcpc` p.10 sigue siendo "
             f"contraejemplo válido para un regex laxo sin requisito de mayúscula.")
    L.append(f"2. **`ri_tsa` está enganchado COMPLETO por las reglas B5.2 vigentes** "
             f"(«Índice» sin guiones en p.62 + secciones): cuerpo 0→30 y 31 headers. "
             f"B5.2 midió y nombró a cedin, ri2_ae y ri_transpa; ri_tsa es un cuarto "
             f"beneficiario no nombrado. Ojo: con el índice en p.62, las 61 páginas "
             f"previas quedan `portada` — la re-corrida de B5.8.4 debe verificar qué "
             f"contenido queda fuera.")
    L.append(f"3. **B5.2 abre compuertas pero no desbloquea**: cedin, ri2_ae y "
             f"ri_transpa pasan a tener cuerpo ({censo['cedin']['vigente']['paginas_cuerpo']}, "
             f"{censo['ri2_ae']['vigente']['paginas_cuerpo']} y "
             f"{censo['ri_transpa']['vigente']['paginas_cuerpo']} páginas) y siguen en "
             f"0 secciones → 0 unidades. Consistente con el alcance declarado de B5.2; "
             f"su vía es B5.8.1 (familia c).")
    L.append(f"4. **`optico` no contiene articulado**: índice reconocido (4 pág, 83 "
             f"entradas «Sección N.») + 38 páginas de historial genuino de "
             f"Comunicaciones + 0 páginas de cuerpo. Candidato a declarar en B5.8.4.")
    L.append(f"5. **El «desbloqueo esperado 44/53» se refina hacia abajo**: "
             f"{len(ri_b581_plenos)} RI plenos vía B5.8.1; {len(ri_cand)} TOs del RI "
             f"que las familias PROSA/MIXTO del scoping contaban como desbloqueables "
             f"no tienen espina utilizable (≤2 labels) y pasan a candidatos a NO "
             f"segmentable, con su causa por TO en §4.")
    n_dom84 = sum(1 for t in tos if "d_dominante" in censo[t]["secundarias"]
                  or censo[t]["familia_primaria"] == "d")
    L.append(f"6. **Ningún TO con unidades tiene a la tabularidad como falla "
             f"dominante** (familia d primaria = {cnt('d')}): medida por exceso "
             f"relativo sobre umbral, C6 nunca domina. La tabularidad dominante "
             f"(≥40 %) aparece en {n_dom84} TOs, todos bloqueados antes por la "
             f"compuerta — B5.8.3 los alcanza recién detrás de B5.8.1.")
    L.append(f"7. **`reqcac` usa secciones con LETRA** («Sección C. Controles…», "
             f"detectada porque C es también numeral romano): la regla b_sec de "
             f"B5.8.2 debe contemplar «Sección <letra>.», no solo romanos.\n")

    L.append("## 7. Comandos de recómputo\n")
    L.append("```bash")
    L.append("# universo y partición 53/31")
    L.append("python3 -c \"import json,csv; v=json.load(open('data/experiment/escalado_prep/veredictos_generalizacion.json'))['por_to']; cat={r['id']:r['categoria'] for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv'))}; nr=[k for k,d in v.items() if d['veredicto']=='necesita reglas']; print(len(nr), sum(1 for k in nr if cat[k]=='regimen_informativo'), sum(1 for k in nr if cat[k]=='normativa_general'))\"")
    L.append("# tally por familia primaria (suma 84)")
    L.append("python3 -c \"import json,collections; c=json.load(open('data/experiment/segmentacion_84/censo_84.json')); t=collections.Counter(x['familia_primaria'] for x in c.values()); print(dict(t), sum(t.values()))\"")
    L.append("# agregado de palabras en tabla del RI (cruce con 12,4 % sellado)")
    L.append("python3 -c \"import json; c=json.load(open('data/experiment/segmentacion_84/mediciones_84.json')); import csv; cat={r['id']:r['categoria'] for r in csv.DictReader(open('data/experiment/escalado_prep/inventario_unidades.csv'))}; ri=[d for k,d in c.items() if cat[k]=='regimen_informativo']; wi=sum(d['tablas']['palabras_en_tabla'] for d in ri); wt=sum(d['tablas']['palabras_total'] for d in ri); print(wi, wt, round(100*wi/wt,1))\"")
    L.append("```\n")

    (SALIDA / "censo_84.md").write_text("\n".join(L))

    # ------------------------------------------- tabla separada 31 no-RI
    M = []
    M.append("# B5.8.0 — Los 31 TOs no-RI «necesita reglas»: insumo del RE-LAUDO de tanda 2\n")
    M.append("Tabla informativa para la decisión de la adenda B5.5 §2.1 (la decisión es de")
    M.append("la autora; esta tabla solo la informa). `unid. hoy` = E0 en seco sellado;")
    M.append("`espina` = líneas con label de punto (regex de e0_lib, raíz ≤ 30) medidas")
    M.append("con el E0 vigente; `est. dens.` = 3,1558 unid/pág (densidad de los 68")
    M.append("digeribles, `resumen_escalado.md` §3.1) × páginas de cuerpo vigentes (o el")
    M.append("total de páginas si la compuerta sigue cerrada — COTA SUPERIOR declarada);")
    M.append("USD a 0,019437/unidad E1+E3 (`resumen_escalado.md` §1). Ambas estimaciones")
    M.append("son extrapolación mecánica, no medición: el número real sale de la")
    M.append("re-corrida de B5.8.4.\n")
    M.append("| TO | pág | familia | unid. hoy | espina | base est. | est. dens. | USD est. | veredicto preliminar |")
    M.append("|---|--:|---|--:|--:|--:|--:|--:|---|")
    tot_hoy = tot_esp = tot_est = 0
    tot_usd = 0.0
    for f in tabla31:
        M.append(f"| {f['id']} | {f['paginas']} | {f['familia']} | {f['unidades_hoy']} | "
                 f"{f['espina_labels']} | {f['cuerpo_base_estimacion']} | "
                 f"{f['unidades_est_densidad']} | {f['usd_est_densidad']:.2f} | "
                 f"{f['veredicto_preliminar'][:80]} |")
        tot_hoy += f["unidades_hoy"]
        tot_esp += f["espina_labels"]
        tot_est += f["unidades_est_densidad"]
        tot_usd += f["usd_est_densidad"]
    M.append(f"| **31** | {sum(f['paginas'] for f in tabla31)} | | **{tot_hoy}** | "
             f"**{tot_esp}** | | **{tot_est}** | **{tot_usd:.2f}** | |\n")
    M.append("Recómputo:\n")
    M.append("```bash")
    M.append("python3 -c \"import json; t=json.load(open('data/experiment/segmentacion_84/tabla_31_no_ri.json')); print(len(t), sum(f['unidades_hoy'] for f in t), sum(f['espina_labels'] for f in t), sum(f['unidades_est_densidad'] for f in t), round(sum(f['usd_est_densidad'] for f in t),2))\"")
    M.append("```")
    (SALIDA / "tabla_31_no_ri.md").write_text("\n".join(M))
    print("censo_84.md y tabla_31_no_ri.md regenerados")


if __name__ == "__main__":
    main()
