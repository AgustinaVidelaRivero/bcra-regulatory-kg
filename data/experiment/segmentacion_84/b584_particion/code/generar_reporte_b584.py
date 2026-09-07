#!/usr/bin/env python3
"""B5.8.4 — reporte regenerable de la partición final (insumo de las filas
10–15 del mapa de fuentes del capítulo del esquema; restricción 5 de la
adenda B5.5: cada número con su comando de recómputo).

Lee ../conteos_b584.json, ../adjudicaciones_b584.json y ../particion_152.json
(productos de correr_b584.py y adjudicar_b584.py) y escribe ../reporte_b584.md.

Uso (desde cualquier cwd):
    python3 data/experiment/segmentacion_84/b584_particion/code/generar_reporte_b584.py
"""

from __future__ import annotations

import json
from pathlib import Path

SALIDA = Path(__file__).resolve().parents[1]
BASE = "data/experiment/segmentacion_84/b584_particion"


def leer(nombre: str):
    return json.loads((SALIDA / nombre).read_text(encoding="utf-8"))


conteos = leer("conteos_b584.json")
adj = leer("adjudicaciones_b584.json")
part = leer("particion_152.json")
por_to, agg = part["por_to"], part["agregados"]

L: list[str] = []
A = L.append


def salud_txt(s) -> str:
    return "sano" if s == "sano" else ",".join(s)


A("# B5.8.4 — Partición final del corpus (152/152)")
A("")
A("Reporte regenerable con:")
A("")
A("```bash")
A(f"python3 {BASE}/code/correr_b584.py")
A(f"python3 {BASE}/code/adjudicar_b584.py")
A(f"python3 {BASE}/code/generar_reporte_b584.py")
A("```")
A("")
A("Corrida con el código commiteado en HEAD, SIN reglas nuevas (escalera "
  "vigente → marcadores → sin raíz + parser de tablas B5.8.3 en su objetivo "
  "sellado); adjudicaciones contra criterios YA sellados, citados por fila "
  "en `adjudicaciones_b584.json` (fuentes S1–S6 en su cabecera).")
A("")

# ------------------------------------------------------------ partición
A("## 1. Partición final (152 = 68 previos + 84 adjudicados)")
A("")
A("| clase | TOs | páginas | unidades E0 | tablas lógicas parseadas | health-check sano |")
A("|---|--:|--:|--:|--:|--:|")
for clase, et in [("reconocido_pleno", "reconocidos plenos"),
                  ("parcial_declarado", "parciales declarados"),
                  ("no_segmentable_declarado", "no segmentables declarados")]:
    a = agg[clase]
    A(f"| {et} | {a['tos']} | {a['paginas']} | {a['unidades']} | "
      f"{a['tablas_logicas']} | {a['sanos']} |")
tot = {k: sum(a[k] for a in agg.values())
       for k in ("tos", "paginas", "unidades", "tablas_logicas", "sanos")}
A(f"| **suma** | **{tot['tos']}** | **{tot['paginas']}** | "
  f"**{tot['unidades']}** | **{tot['tablas_logicas']}** | **{tot['sanos']}** |")
A("")
A("Recómputo de la tabla:")
A("")
A("```bash")
A("python3 -c \"import json; p=json.load(open('" + BASE + "/particion_152.json'));"
  " print(json.dumps(p['agregados'], ensure_ascii=False, indent=1))\"")
A("```")
A("")
A("Recómputo de los agregados desde `por_to` (verifica que la tabla suma):")
A("")
A("```bash")
A("python3 -c \"import json,collections; p=json.load(open('" + BASE
  + "/particion_152.json'))['por_to']; t=collections.Counter(d['clase'] for d "
  "in p.values()); print(dict(t), sum(t.values()), "
  "sum(d['paginas'] for d in p.values()), "
  "sum(d['unidades'] for d in p.values()))\"")
A("```")
A("")

# desglose por vía dentro de reconocidos
A("### 1.1 Reconocidos plenos por vía de lectura")
A("")
vias: dict[str, list[str]] = {}
for to, d in sorted(por_to.items()):
    if d["clase"] == "reconocido_pleno":
        vias.setdefault(d["via"], []).append(to)
A("| vía | TOs | unidades | páginas |")
A("|---|--:|--:|--:|")
for via, tos in sorted(vias.items()):
    A(f"| {via} | {len(tos)} | {sum(por_to[t]['unidades'] for t in tos)} | "
      f"{sum(por_to[t]['paginas'] for t in tos)} |")
A("")
A("```bash")
A("python3 -c \"import json,collections; p=json.load(open('" + BASE
  + "/particion_152.json'))['por_to']; t=collections.Counter(d['via'] for d in "
  "p.values() if d['clase']=='reconocido_pleno'); print(dict(t))\"")
A("```")
A("")

# ------------------------------------------------- cuenta del alcance
A("## 2. La cuenta del alcance (regla i, re-recomputada)")
A("")
A("84 TOs del censo = 41 (rinden por B5.8.1) + 7 (B5.8.2) + 1 (ri_tsa, "
  "regla vigente B5.2) + 1 (ri_acsf, vía tabular) + 22 (b_pts) + 12 "
  "(candidatos a NO) — partición disjunta, cero sin clasificar:")
A("")
A("```bash")
A("python3 -c \"import json; c=json.load(open('data/experiment/segmentacion_84/censo_84.json')); "
  "b1=json.load(open('data/experiment/segmentacion_84/b581_sin_raiz/conteos_b581.json')); "
  "b2=json.load(open('data/experiment/segmentacion_84/b582_marcadores/conteos_b582.json')); "
  "g1={t for t,d in b1.items() if d['unidades_extraccion']>0 and t!='ri_acsf'}; "
  "g2={t for t in b2 if t!='ri_tsa'}; "
  "g5={t for t,d in c.items() if d['familia_primaria']=='b_pts'}; "
  "g6={t for t,d in c.items() if d['veredicto_preliminar'].startswith('candidato a NO')}; "
  "gs=[g1,g2,{'ri_tsa'},{'ri_acsf'},g5,g6]; "
  "assert all(not (a&b) for i,a in enumerate(gs) for b in gs[i+1:]); "
  "u=set().union(*gs); print([len(g) for g in gs], len(u), set(c)==u)\"")
A("```")
A("")

# --------------------------------------------------- adjudicaciones 3.a
A("## 3. Adjudicaciones (criterio citado por fila; detalle en "
  "`adjudicaciones_b584.json`)")
A("")
A("### 3.a Los 22 b_pts — contra los umbrales C4–C8 del censo (evaluar() "
  "sellado sobre las unidades emitidas) + health-check")
A("")
A("| TO | cat | pág | unid | fallas C* selladas (censo) | fallas C* corrida "
  "b584 | salud | marginal | adjudicación |")
A("|---|---|--:|--:|---|---|---|---|---|")
for f in adj["a_bpts"]:
    cs = ",".join(sorted({x.split(" ")[0] for x in f["fallas_selladas_censo"]}))
    cn = ",".join(sorted({x.split(" ")[0] for x in f["evaluar_b584"]["fallas"]
                          if x.startswith("C")})) or "—"
    A(f"| {f['to']} | {f['categoria']} | {f['paginas']} | {f['unidades']} | "
      f"{cs} | {cn} | {salud_txt(f['salud'])} | "
      f"{'sí' if f['marginal_censo'] else 'no'} | {f['adjudicacion']} |")
A("")
A("Los 22 producen unidades por el camino VIGENTE (jamás entran a las "
  "etapas nuevas; columna `vigente_confirmado` en el JSON). El afinado "
  "opcional de B5.8.2 no se construyó (cerró con cero reglas b_pts): las "
  "fallas C* remanentes quedan DECLARADAS, no remediadas. El único "
  "`reconocido_pleno_digerible` quedó CURADO por las reglas B5.2 vigentes "
  "(evaluar sellado: digerible, cero fallas, salud sana — fila corregida "
  "en la revisión del freno).")
A("")
A("```bash")
A("python3 -c \"import json,collections; a=json.load(open('" + BASE
  + "/adjudicaciones_b584.json'))['a_bpts']; "
  "print(len(a), dict(collections.Counter(f['adjudicacion'] for f in a)), "
  "sum(1 for f in a if f['marginal_censo']))\"")
A("```")
A("")

# ----------------------------------------------------------------- 3.b
b = adj["b_ri_tsa"]
A("### 3.b ri_tsa — verificación de la re-corrida (B5.2) y su partición")
A("")
v = b["verificacion_control_b582"]
A(f"- Control S4 (b582) vs corrida b584: **{'COINCIDE' if v['coincide'] else 'NO COINCIDE'}** "
  f"— modo `{v['obtenido_b584']['modo_lectura']}`, "
  f"{v['obtenido_b584']['unidades_extraccion']} unidades, "
  f"{v['obtenido_b584']['raices_de_lectura']} raíces, salud "
  f"{salud_txt(v['obtenido_b584']['healthcheck_veredicto'])}.")
q = b["que_queda_fuera"]
A(f"- Hallazgo 2 del censo verificado: {q['paginas_portada']} páginas "
  f"previas al índice quedan en rol `portada`; de ellas, "
  f"**{q['portada_cubierta_por_tablas']} tienen tabla lógica parseada por la "
  f"vía B5.8.3** ({q['tablas_logicas_total']} tablas lógicas en el TO); las "
  f"{q['paginas_portada'] - q['portada_cubierta_por_tablas']} restantes "
  f"quedan declaradas (lista en el JSON).")
A(f"- Adjudicación: **{b['adjudicacion']}**.")
A("")

# ----------------------------------------------------------------- 3.c
A("### 3.c Reinicios por anexo/apartado (límite citado de b581/b582, "
  "no re-medido)")
A("")
A("| TO | pág | unid | raíces | salud | límite medido (S4) | adjudicación |")
A("|---|--:|--:|--:|---|---|---|")
for f in adj["c_reinicios"]:
    A(f"| {f['to']} | {f['paginas']} | {f['unidades']} | {f['raices']} | "
      f"{salud_txt(f['salud'])} | {f['limite_medido'][:80]}… | "
      f"{f['adjudicacion']} |")
A("")

# ----------------------------------------------------------------- 3.d
A("### 3.d Familia declarada «parser de registro» (fuera de B5.8.1-3)")
A("")
A("| TO | pág | pág ficha_registro | tablas lógicas parseadas |")
A("|---|--:|--:|--:|")
for f in adj["d_parser_registro"]["filas"]:
    A(f"| {f['to']} | {f['paginas']} | {f['paginas_ficha_registro']} | "
      f"{f['tablas_logicas_parseadas']} |")
A("")
A(adj["d_parser_registro"]["declaracion"])
A("")
A("```bash")
A("python3 -c \"import json; c=json.load(open('" + BASE
  + "/conteos_b584.json')); print({t: d['roles_pagina'].get('ficha_registro',0) "
  "for t,d in c.items() if d['roles_pagina'].get('ficha_registro',0)>0})\"")
A("```")
A("")

# ----------------------------------------------------------------- 3.e
A("### 3.e Los 12 candidatos a NO segmentable — declaración final")
A("")
A("| TO | cat | pág | causa censal | modo final | unid | raíces | declaración |")
A("|---|---|--:|---|---|--:|--:|---|")
for f in adj["e_no_segmentables"]:
    A(f"| {f['to']} | {f['categoria']} | {f['paginas']} | "
      f"{f['causa_censo'][:70]}… | {f['evidencia_b584']['modo_final']} | "
      f"{f['evidencia_b584']['unidades']} | {f['evidencia_b584']['raices']} | "
      f"{f['declaracion']} |")
A("")
A("```bash")
A("python3 -c \"import json; a=json.load(open('" + BASE
  + "/adjudicaciones_b584.json'))['e_no_segmentables']; print(len(a), "
  "sum(1 for f in a if f['declaracion']=='no_segmentable_declarado'))\"")
A("```")
A("")

# ----------------------------------------------------------------- 3.f
A("### 3.f Huecos de alcance de B5.4 (docvig, fimipyme) — SOLO REPORTE")
A("")
for f in adj["f_huecos_b54"]["filas"]:
    idx = f["entradas_indice_alcance"]
    uni = f["unidades_alcance"]
    A(f"- **{f['to']}** (modo `{f['modo_lectura']}`, "
      f"{f['unidades_totales']} unidades, salud {salud_txt(f['salud'])}): "
      f"entradas de índice con «alcanzad»: "
      f"{[e['titulo'][:60] for e in idx] or 'ninguna'}; unidades con "
      f"«alcanzad» en el título: {[u['id'] for u in uni] or 'ninguna'}; "
      f"anunciado_sin_cuerpo con «alcanzad»: "
      f"{f['anunciado_sin_cuerpo_alcance'] or 'ninguno'}.")
A("")
A(adj["f_huecos_b54"]["nota"])
A("")

# --------------------------------------------------- re-laudo tanda 2
r = adj["tabla_relaudo_tanda2"]
A("## 4. Tabla del re-laudo de tanda 2 (solo informa)")
A("")
A(r["nota"])
A("")
A("| TO | clase | pág | unidades reales | tablas lógicas | health-check |")
A("|---|---|--:|--:|--:|---|")
for f in r["filas"]:
    A(f"| {f['to']} | {f['clase']} | {f['paginas']} | {f['unidades_reales']} | "
      f"{f['tablas_logicas']} | {salud_txt(f['salud'])} |")
A(f"| **{len(r['filas'])}** | | | **{r['total_unidades_reales']}** | | "
  f"**{r['con_salud_verde']} sanos** |")
A("")
A("```bash")
A("python3 -c \"import json; r=json.load(open('" + BASE
  + "/adjudicaciones_b584.json'))['tabla_relaudo_tanda2']; "
  "print(len(r['filas']), sum(f['unidades_reales'] for f in r['filas']), "
  "r['con_salud_verde'])\"")
A("```")
A("")

# --------------------------------------------------- tabla por TO
A("## 5. Tabla por TO (los 152)")
A("")
A("`unid` = unidades de extracción E0 de la corrida b584; `tab` = tablas "
  "lógicas parseadas (vía B5.8.3); `ficha` = páginas declaradas "
  "ficha_registro; señales de salud = health-check por TO (S5: lectura, "
  "no gate).")
A("")
A("| TO | cat | clase | vía | pág | unid | tab | ficha | salud |")
A("|---|---|---|---|--:|--:|--:|--:|---|")
for to in sorted(por_to):
    d = por_to[to]
    A(f"| {to} | {d['categoria']} | {d['clase'].replace('_declarado','').replace('_pleno','')} | "
      f"{d['via']} | {d['paginas']} | {d['unidades']} | {d['tablas_logicas']} | "
      f"{d['paginas_ficha_registro']} | {salud_txt(d['salud'])} |")
A("")
A("```bash")
A("python3 -c \"import json; c=json.load(open('" + BASE
  + "/conteos_b584.json')); print(len(c), sum(d['unidades_extraccion'] for d "
  "in c.values()), sum(d['paginas'] for d in c.values()))\"")
A("```")

(SALIDA / "reporte_b584.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"reporte -> {SALIDA / 'reporte_b584.md'} ({len(L)} líneas)")
