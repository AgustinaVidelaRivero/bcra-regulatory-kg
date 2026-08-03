#!/usr/bin/env python3
"""M4: cruza anclajes_por_pregunta.json contra inventario_puntos_por_TO.json.

Unidad de conteo = punto x.y del índice del TO; una sección sin puntos en el
índice cuenta como una unidad propia (S<n>).
Regla laudada: territorio quemado = el punto exacto anclado con sus subpuntos,
no la sección entera. Por eso:
 - ancla 'S<n>'      -> toda la sección quemada entera (todas sus unidades);
 - ancla 'x.y'       -> unidad x.y quemada entera (incluye subpuntos);
 - ancla más profunda -> unidad x.y (o S<n> si el índice no lista puntos)
                         quemada PARCIALMENTE: solo ese subpunto y sus hijos.
"""
import json, os
from collections import defaultdict

SCRATCH = os.path.dirname(os.path.abspath(__file__))
inv = json.load(open(os.path.join(SCRATCH, 'inventario_puntos_por_TO.json')))
regs = json.load(open(os.path.join(SCRATCH, 'anclajes_por_pregunta.json')))

NOMBRE = {'cap': 'Capitales Mínimos', 'cla': 'Clasificación de Deudores',
          'ext': 'Exterior y Cambios', 'pro': 'Protección de Usuarios',
          'ric': 'Régimen Informativo Contable Mensual (R.I.-C.M.)'}


def unidades(to):
    """Lista ordenada de unidades del TO: puntos x.y + S<n> para secciones sin puntos."""
    d = inv[to]
    secs_con_puntos = {v['seccion'] for v in d['puntos'].values()}
    out = []
    for n in sorted(d['secciones'], key=int):
        if int(n) in secs_con_puntos:
            out += [p for p, v in d['puntos'].items() if v['seccion'] == int(n)]
        else:
            out.append(f"S{n}")
    return out


def titulo(to, unidad):
    if unidad.startswith('S'):
        return inv[to]['secciones'][unidad[1:]] + ' (sección sin puntos en índice)'
    return inv[to]['puntos'][unidad]['titulo']


# estado por unidad: {} | {'total': [refs]} | {'parcial': {subpunto: [refs]}}
estado = {to: defaultdict(lambda: {'total': [], 'parcial': defaultdict(list)}) for to in inv}
avisos = []

for r in regs:
    ref = f"{r['set']}:{r['qid']}"
    for to, anclas in r['anclas'].items():
        us = unidades(to)
        for a in anclas:
            if a.startswith('S'):
                sec = a[1:]
                if sec not in inv[to]['secciones']:
                    avisos.append(f"{ref}: sección {sec} no existe en índice de {to}")
                    continue
                objetivo = [u for u in us if (u == a) or (not u.startswith('S') and u.split('.')[0] == sec)]
                for u in objetivo:
                    estado[to][u]['total'].append(ref + f" (Sección {sec} entera)")
                continue
            partes = a.split('.')
            xy = '.'.join(partes[:2])
            if xy in inv[to]['puntos']:
                if len(partes) == 2:
                    estado[to][xy]['total'].append(ref)
                else:
                    estado[to][xy]['parcial'][a].append(ref)
            else:
                # el índice no lista puntos de esa sección: la unidad es S<n>
                su = f"S{partes[0]}"
                if su in us:
                    estado[to][su]['parcial'][a].append(ref)
                else:
                    avisos.append(f"{ref}: ancla {a} sin unidad en índice de {to}")

# --- armar mapa y conteos ---
mapa = {}
tot_global = {'unidades': 0, 'quemadas_total': 0, 'quemadas_parcial': 0, 'disponibles': 0}
for to in ['cap', 'cla', 'ext', 'pro', 'ric']:
    us = unidades(to)
    quemadas, parciales, disponibles = [], [], []
    for u in us:
        e = estado[to].get(u)
        if e and e['total']:
            item = {'unidad': u, 'titulo': titulo(to, u), 'refs': sorted(set(e['total']))}
            if e['parcial']:
                item['anclas_adicionales'] = {k: sorted(set(v)) for k, v in sorted(e['parcial'].items())}
            quemadas.append(item)
        elif e and e['parcial']:
            parciales.append({'unidad': u, 'titulo': titulo(to, u),
                              'puntos_quemados': {k: sorted(set(v)) for k, v in sorted(e['parcial'].items())}})
        else:
            disponibles.append({'unidad': u, 'titulo': titulo(to, u)})
    n = len(us)
    c = {'unidades': n, 'quemadas_total': len(quemadas), 'quemadas_parcial': len(parciales),
         'disponibles': len(disponibles),
         'pct_tocado': round(100 * (len(quemadas) + len(parciales)) / n, 1),
         'pct_quemado_entero': round(100 * len(quemadas) / n, 1)}
    for k in tot_global:
        tot_global[k] += c[k]
    mapa[to] = {'archivo': inv[to]['archivo'], 'nombre': NOMBRE[to], 'conteos': c,
                'quemadas_enteras': quemadas, 'quemadas_parcialmente': parciales,
                'disponibles': disponibles}

tot_global['pct_tocado'] = round(100 * (tot_global['quemadas_total'] + tot_global['quemadas_parcial']) / tot_global['unidades'], 1)
tot_global['pct_quemado_entero'] = round(100 * tot_global['quemadas_total'] / tot_global['unidades'], 1)

salida = {'regla': 'quemado = punto exacto anclado con sus subpuntos; unidad de conteo = punto x.y del índice (o sección sin puntos)',
          'sets': {'EV1': 36, 'CQ': 31, 'CQN': 15, 'CQN2': 15},
          'sin_ancla': [r['qid'] for r in regs if r['estado'] == 'sin_ancla'],
          'totales': tot_global, 'por_to': mapa, 'avisos': avisos}
out = os.path.join(SCRATCH, 'mapa_territorio_quemado.json')
json.dump(salida, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

print("AVISOS:", avisos if avisos else "ninguno")
print(f"{'TO':4} {'unid':>5} {'quem':>5} {'parc':>5} {'disp':>5} {'%toc':>6} {'%quem':>6}")
for to, m in mapa.items():
    c = m['conteos']
    print(f"{to:4} {c['unidades']:>5} {c['quemadas_total']:>5} {c['quemadas_parcial']:>5} "
          f"{c['disponibles']:>5} {c['pct_tocado']:>6} {c['pct_quemado_entero']:>6}")
c = tot_global
print(f"TOT  {c['unidades']:>5} {c['quemadas_total']:>5} {c['quemadas_parcial']:>5} "
      f"{c['disponibles']:>5} {c['pct_tocado']:>6} {c['pct_quemado_entero']:>6}")
print("Escrito:", out)
