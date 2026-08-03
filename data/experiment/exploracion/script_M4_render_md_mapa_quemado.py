#!/usr/bin/env python3
"""Renderiza mapa_territorio_quemado.json a markdown legible (entregable M4)."""
import json, os

SCRATCH = os.path.dirname(os.path.abspath(__file__))
m = json.load(open(os.path.join(SCRATCH, 'mapa_territorio_quemado.json')))
regs = json.load(open(os.path.join(SCRATCH, 'anclajes_por_pregunta.json')))

L = []
A = L.append
A("# Mapa de territorio quemado / disponible — 5 TOs del corpus")
A("")
A("Unidad de lectura, 2026-08-03. Universo de referencia: el corpus (`data/experiment/subset/`), "
  "extraído con `pdftotext -layout`; NO el grafo.")
A("")
A("**Regla laudada aplicada**: territorio quemado = el punto normativo exacto que cada pregunta "
  "quemada ancló (con sus subpuntos), no la sección entera. Unidad de conteo: punto x.y del índice "
  "del TO; una sección cuyo índice no lista puntos cuenta como una unidad (S<n>). Un ancla más "
  "profunda que x.y quema SOLO ese subpunto (y sus hijos): la unidad x.y queda *parcialmente "
  "quemada* y su resto sigue disponible.")
A("")
A("## Sets quemados (M1)")
A("")
A("| Set | Archivo | Preguntas |")
A("|---|---|---|")
A("| EV1 | `data/experiment/evaluacion_escalon1/EV1_preguntas.json` | 36 |")
A("| CQ | `data/experiment/evaluacion/queries/eval_set_v2.json` (v1 ⊂ v2: 23 + 8 nuevas) | 31 |")
A("| CQN | `data/experiment/evaluacion/queries/eval_set_cqn.json` | 15 |")
A("| CQN2 | `data/experiment/evaluacion/queries/eval_set_cqn2.json` | 15 |")
A("")
A(f"Total: 97 preguntas; 93 anclan territorio; sin ancla (unanswerable by design): "
  f"{', '.join(m['sin_ancla'])}.")
A("")
A("## Conteos (M4)")
A("")
A("| TO | Unidades | Quemadas enteras | Parcialmente quemadas | Disponibles | % tocado | % quemado entero |")
A("|---|---|---|---|---|---|---|")
for to, d in m['por_to'].items():
    c = d['conteos']
    A(f"| {d['nombre']} | {c['unidades']} | {c['quemadas_total']} | {c['quemadas_parcial']} | "
      f"{c['disponibles']} | {c['pct_tocado']}% | {c['pct_quemado_entero']}% |")
c = m['totales']
A(f"| **Total** | **{c['unidades']}** | **{c['quemadas_total']}** | **{c['quemadas_parcial']}** | "
  f"**{c['disponibles']}** | **{c['pct_tocado']}%** | **{c['pct_quemado_entero']}%** |")
A("")
A("«% tocado» = (quemadas enteras + parciales) / unidades; «% quemado entero» excluye las parciales, "
  "cuyo resto no anclado sigue disponible.")

for to, d in m['por_to'].items():
    A("")
    A(f"## {d['nombre']} — `{d['archivo']}`")
    A("")
    A(f"### Quemadas enteras ({len(d['quemadas_enteras'])})")
    A("")
    if d['quemadas_enteras']:
        A("| Unidad | Título | Quemada por |")
        A("|---|---|---|")
        for q in d['quemadas_enteras']:
            extra = ''
            if 'anclas_adicionales' in q:
                extra = ' — además anclas internas: ' + '; '.join(
                    f"{p} ({', '.join(r)})" for p, r in q['anclas_adicionales'].items())
            A(f"| {q['unidad']} | {q['titulo']} | {', '.join(q['refs'])}{extra} |")
    else:
        A("(ninguna)")
    A("")
    A(f"### Parcialmente quemadas ({len(d['quemadas_parcialmente'])}) — solo el subpunto listado (con sus hijos) está quemado")
    A("")
    if d['quemadas_parcialmente']:
        A("| Unidad | Título | Subpuntos quemados (por) |")
        A("|---|---|---|")
        for q in d['quemadas_parcialmente']:
            subs = '; '.join(f"{p} ({', '.join(r)})" for p, r in q['puntos_quemados'].items())
            A(f"| {q['unidad']} | {q['titulo']} | {subs} |")
    else:
        A("(ninguna)")
    A("")
    A(f"### Disponibles ({len(d['disponibles'])})")
    A("")
    for q in d['disponibles']:
        A(f"- {q['unidad']} — {q['titulo']}")

A("")
A("## Anclaje por pregunta (M2) — qid → TO → puntos")
A("")
A("Estados: todas `declarado` salvo las 4 `sin_ancla` (unanswerable). CQN2-010: asignación de "
  "puntos a TO tomada de `seccion_sorteada_origen` (CLA-S6 + PRO-S1). `S<n>` = sección entera "
  "declarada como ancla por el propio set.")
A("")
for r in regs:
    if r['estado'] == 'sin_ancla':
        A(f"- {r['qid']}: sin_ancla ({r['nota']})")
    else:
        partes = '; '.join(f"{to}: {', '.join(ps)}" for to, ps in r['anclas'].items())
        A(f"- {r['qid']}: {partes}")

out = os.path.join(SCRATCH, 'mapa_territorio_quemado.md')
open(out, 'w', encoding='utf-8').write('\n'.join(L) + '\n')
print("Escrito:", out, f"({len(L)} líneas)")
