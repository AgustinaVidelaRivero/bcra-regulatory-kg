#!/usr/bin/env python3
"""M2: extrae por pregunta (qid) los puntos normativos anclados, normalizados a
(TO, punto) o (TO, seccion N). Estados: declarado | inferido | sin_ancla."""
import json, re, os

REPO = os.environ.get(
    'BCRA_KG_REPO',
    os.path.expanduser('~/INGENIERIA IA/TESIS/bcra-regulatory-kg')) + '/data/experiment'
SCRATCH = os.path.dirname(os.path.abspath(__file__))

SIGLA_POR_ARCHIVO = {
    'TO_capitales_minimos_actual.pdf': 'cap',
    'TO_clasificacion_deudores_actual.pdf': 'cla',
    'TO_exterior_cambios_actual.pdf': 'ext',
    'TO_proteccion_usuarios_servicios_financieros_actual.pdf': 'pro',
    'TO_regimen_informativo_contable_mensual_actual.pdf': 'ric',
}
# nombres cortos usados por eval_set_v2 (tos_fuente) y prefijos en ground_truth
SIGLA_POR_NOMBRE = {
    'capitales': 'cap', 'clasificacion': 'cla', 'exterior': 'ext',
    'proteccion': 'pro', 'regimen': 'ric',
}
PREFIJOS = [
    (re.compile(r'^\s*protecci[oó]n', re.I), 'pro'),
    (re.compile(r'^\s*clasificaci[oó]n', re.I), 'cla'),
    (re.compile(r'^\s*capitales', re.I), 'cap'),
    (re.compile(r'^\s*exterior', re.I), 'ext'),
    (re.compile(r'^\s*r[ée]gimen', re.I), 'ric'),
]
# desambiguadores entre paréntesis usados por CQN2 multi-TO
PARENTESIS = [
    (re.compile(r'capitales m[ií]nimos', re.I), 'cap'),
    (re.compile(r'exterior y cambios', re.I), 'ext'),
    (re.compile(r'r\.i\.-c\.m\.', re.I), 'ric'),
]

NUM = re.compile(r'\d+(?:\.\d+)+')
RANGO = re.compile(r'(\d+\.\d+)\s*[-–]\s*(\d+\.\d+)')
SECCION = re.compile(r'Secci[oó]n\s+(\d+)', re.I)

def norm(p):
    return p.rstrip('.')

def expandir_rango(seg):
    """'puntos 4.3-4.5' -> ['4.3','4.4','4.5']"""
    out = []
    for a, b in RANGO.findall(seg):
        pa, pb = a.split('.'), b.split('.')
        if pa[0] == pb[0]:
            out += [f"{pa[0]}.{i}" for i in range(int(pa[1]), int(pb[1]) + 1)]
    return out

def parse_segmento(seg, to_default):
    """Un segmento de ground_truth -> (sigla_to, [anclas]) donde ancla es
    'x.y[.z...]' o 'S<n>' (sección entera)."""
    to = to_default
    for rx, s in PREFIJOS:
        if rx.match(seg):
            to = s
            break
    for rx, s in PARENTESIS:
        if rx.search(seg):
            to = s
            break
    rangos = expandir_rango(seg)
    if rangos:
        return to, rangos
    # quitar el nombre de archivo si viene embebido (CQN) para no capturar números del nombre
    seg2 = re.sub(r'TO_\w+\.pdf', '', seg)
    puntos = [norm(m.group(0)) for m in NUM.finditer(seg2)]
    if puntos:
        return to, sorted(set(puntos), key=lambda p: [int(x) for x in p.split('.')])
    m = SECCION.search(seg2)
    if m:
        return to, [f"S{m.group(1)}"]
    return to, []

def anclas_de_lista(gts, tos_archivos, contexto):
    """gts: lista de strings; devuelve dict sigla -> lista de anclas."""
    default = None
    siglas = [SIGLA_POR_ARCHIVO.get(t, SIGLA_POR_NOMBRE.get(t)) for t in (tos_archivos or [])]
    if len(set(siglas)) == 1:
        default = siglas[0]
    out = {}
    for gt in gts:
        for seg in gt.split(';'):
            to, anclas = parse_segmento(seg, default)
            if not anclas:
                continue
            if to is None:
                raise ValueError(f"{contexto}: segmento sin TO resoluble: {seg!r}")
            out.setdefault(to, [])
            for a in anclas:
                if a not in out[to]:
                    out[to].append(a)
    return out

registros = []

def registrar(qset, qid, anclas, estado, nota=None):
    registros.append({'set': qset, 'qid': qid,
                      'anclas': anclas, 'estado': estado, **({'nota': nota} if nota else {})})

# --- CQ (eval_set_v2.json, 31 preguntas; ids CQ-xxx) ---
d = json.load(open(f"{REPO}/evaluacion/queries/eval_set_v2.json"))['preguntas']
for q in d:
    if q['categoria'] == 'unanswerable':
        registrar('CQ', q['id'], {}, 'sin_ancla', 'unanswerable by design: no ancla punto normativo')
        continue
    anclas = anclas_de_lista(q['ground_truth_secciones'], q['tos_fuente'], q['id'])
    registrar('CQ', q['id'], anclas, 'declarado')

# --- CQN (eval_set_cqn.json, 15) ---
d = json.load(open(f"{REPO}/evaluacion/queries/eval_set_cqn.json"))['preguntas']
for q in d:
    # cada entrada de ground_truth trae su propio archivo TO embebido
    out = {}
    for gt in q['ground_truth_secciones']:
        m = re.match(r'(TO_\w+\.pdf)\s+(.*)', gt)
        to = SIGLA_POR_ARCHIVO[m.group(1)]
        _, anclas = parse_segmento(m.group(2), to)
        out.setdefault(to, [])
        for a in anclas:
            if a not in out[to]:
                out[to].append(a)
    registrar('CQN', q['id'], out, 'declarado')

# --- CQN2 (eval_set_cqn2.json, 15) ---
SIGLA_POR_CODIGO = {'CAP': 'cap', 'CLA': 'cla', 'EXT': 'ext', 'PRO': 'pro', 'RIC': 'ric'}
d = json.load(open(f"{REPO}/evaluacion/queries/eval_set_cqn2.json"))
for q in d:
    # mapa sección->TO desde seccion_sorteada_origen (p.ej. 'CLA-S6 + PRO-S1')
    sec2to = {}
    for cod, sec in re.findall(r'(CAP|CLA|EXT|PRO|RIC)-S(\d+)', str(q.get('seccion_sorteada_origen', ''))):
        sec2to.setdefault(sec, SIGLA_POR_CODIGO[cod])
    out, nota = {}, None
    for gt in q['ground_truth_secciones']:
        try:
            to, anclas = parse_segmento(gt, None if len(q['tos_fuente']) > 1 else
                                        SIGLA_POR_ARCHIVO[q['tos_fuente'][0]])
        except Exception:
            to, anclas = None, []
        if anclas and to is None:
            # desambiguar por la sección de origen sorteada
            to = sec2to.get(anclas[0].split('.')[0].lstrip('S'))
            nota = 'TO asignado por seccion_sorteada_origen'
        if not anclas:
            raise ValueError(f"{q['id']}: sin anclas en {gt!r}")
        if to is None:
            raise ValueError(f"{q['id']}: TO no resoluble en {gt!r}")
        out.setdefault(to, [])
        for a in anclas:
            if a not in out[to]:
                out[to].append(a)
    registrar('CQN2', q['id'], out, 'declarado', nota)

# --- EV1 (EV1_preguntas.json, 36; campo puntos_citados) ---
d = json.load(open(f"{REPO}/evaluacion_escalon1/EV1_preguntas.json"))
for q in d:
    anclas = anclas_de_lista(q['puntos_citados'], q['tos_fuente'], q['id'])
    registrar('EV1', q['id'], anclas, 'declarado')

# --- salida ---
for r in registros:
    print(r['set'], r['qid'], '|', r['estado'], '|',
          json.dumps(r['anclas'], ensure_ascii=False), '|', r.get('nota', ''))

out = os.path.join(SCRATCH, 'anclajes_por_pregunta.json')
json.dump(registros, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
tot = len(registros)
print(f"\nTotal preguntas: {tot} (CQ {sum(1 for r in registros if r['set']=='CQ')}, "
      f"CQN {sum(1 for r in registros if r['set']=='CQN')}, "
      f"CQN2 {sum(1 for r in registros if r['set']=='CQN2')}, "
      f"EV1 {sum(1 for r in registros if r['set']=='EV1')})")
print("sin_ancla:", [r['qid'] for r in registros if r['estado'] == 'sin_ancla'])
print("Escrito:", out)
