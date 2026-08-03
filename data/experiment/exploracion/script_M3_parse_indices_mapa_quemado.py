#!/usr/bin/env python3
"""M3: parsea el -Índice- de cada TO (pdftotext -layout) → inventario de secciones y puntos x.y con título.
Universo de referencia = el corpus (los 5 PDFs), no el grafo."""
import json, re, sys, os

SCRATCH = os.path.dirname(os.path.abspath(__file__))
TXT = os.path.join(SCRATCH, 'txt')

TOS = {
    'cap': 'TO_capitales_minimos_actual',
    'cla': 'TO_clasificacion_deudores_actual',
    'ext': 'TO_exterior_cambios_actual',
    'pro': 'TO_proteccion_usuarios_servicios_financieros_actual',
    'ric': 'TO_regimen_informativo_contable_mensual_actual',
}

# líneas de encabezado/pie de página a descartar dentro del índice
NOISE = re.compile(r'Versión:|COMUNICACIÓN|Vigencia:|Página|B\.C\.R\.A\.|TEXTO ORDENADO|-Índice-|- Índice|EXTERIOR Y CAMBIOS|CAPITALES MÍNIMOS|CLASIFICACION DE DEUDORES|PROTECCIÓN DE LOS USUARIOS|REGIMEN INFORMATIVO|R\.I\.-C\.M\.|Última comunicación|Texto ordenado al')
SEC = re.compile(r'^\s*Sección\s+(\d+)\.?\s*(.*)$')
PUNTO = re.compile(r'^\s+(\d+\.\d+)\.?\s+(\S.*)$')

def indice_lines(path):
    lines = open(path, encoding='utf-8').read().splitlines()
    # inicio: primera línea con marcador de índice
    start = next(i for i, l in enumerate(lines) if re.search(r'-\s*Índice\s*[-–]', l))
    # fin: 'Tabla de correlaciones' si existe antes de la línea 400; si no (RIC), el
    # segundo 'Sección 1.' (arranque del cuerpo)
    end = None
    for i, l in enumerate(lines[:400]):
        if 'Tabla de correlaciones' in l:
            end = i
            break
    if end is None:
        secs1 = [i for i, l in enumerate(lines[:400]) if re.match(r'^\s*Sección\s+1\.', l)]
        end = secs1[1]  # el segundo es el cuerpo
    return lines[start:end]

def parse(path):
    secciones = {}   # num -> titulo
    puntos = {}      # 'x.y' -> {'titulo':..., 'seccion': num}
    cur = None       # ('sec', num) | ('punto', clave)
    for raw in indice_lines(path):
        line = raw.rstrip()
        if not line.strip():
            cur = None
            continue
        # SEC/PUNTO se chequean ANTES que NOISE: hay títulos legítimos que
        # contienen tokens del filtro (p.ej. "Facilidades otorgadas por el B.C.R.A.")
        m = SEC.match(line)
        if m:
            num = int(m.group(1))
            if num not in secciones:
                secciones[num] = m.group(2).strip()
                cur = ('sec', num)
            else:
                cur = None
            continue
        m = PUNTO.match(line)
        if m:
            clave, titulo = m.group(1), m.group(2).strip()
            sec = int(clave.split('.')[0])
            if clave not in puntos:
                puntos[clave] = {'titulo': titulo, 'seccion': sec}
                cur = ('punto', clave)
            else:
                cur = None
            continue
        if NOISE.search(line):
            cur = None
            continue
        # línea de continuación de título (sin numeración): anexar al último ítem
        if cur:
            cont = line.strip()
            if cur[0] == 'sec':
                secciones[cur[1]] = (secciones[cur[1]] + ' ' + cont).strip()
            else:
                puntos[cur[1]]['titulo'] = (puntos[cur[1]]['titulo'] + ' ' + cont).strip()
    return secciones, puntos

def limpiar(s):
    return re.sub(r'\s+', ' ', s).strip()

# Puntos que existen en el cuerpo del TO pero que su -Índice- no lista.
# Evidencia (pdftotext -layout, TO_regimen_informativo_contable_mensual_actual.txt):
#  - línea 96: "puntos 4.3., 4.4. y 4.5. de la Sección 4." (instrucciones generales)
#  - línea 609: encabezado "4.3. Información complementaria ... riesgo de mercado"
#  - línea 621: referencia a "modelos de información previstos en el punto 4.4.";
#    subpuntos 4.4.1/4.4.3/4.4.4 en líneas 629/825/844
#  - línea 861: encabezado "4.5. Información sobre instrumentos derivados"
AUGMENT = {
    'ric': {
        '4.3': {'titulo': 'Información complementaria vinculada al cálculo de la exigencia '
                          'por riesgo de mercado - Normas de procedimiento [no listado en índice]',
                'seccion': 4},
        '4.4': {'titulo': 'Información complementaria vinculada al cálculo de la exigencia '
                          'por riesgo de mercado - Modelos de información [no listado en índice]',
                'seccion': 4},
        '4.5': {'titulo': 'Información sobre instrumentos derivados [no listado en índice]',
                'seccion': 4},
    }
}

inv = {}
for sigla, base in TOS.items():
    secciones, puntos = parse(os.path.join(TXT, base + '.txt'))
    secciones = {k: limpiar(v) for k, v in secciones.items()}
    for v in puntos.values():
        v['titulo'] = limpiar(v['titulo'])
    for clave, v in AUGMENT.get(sigla, {}).items():
        if clave not in puntos:
            puntos[clave] = dict(v)
    inv[sigla] = {
        'archivo': base + '.pdf',
        'secciones': {str(k): v for k, v in sorted(secciones.items())},
        'puntos': dict(sorted(puntos.items(), key=lambda kv: [int(x) for x in kv[0].split('.')])),
    }
    print(f"== {sigla} ({base}): {len(secciones)} secciones, {len(puntos)} puntos x.y ==")
    for n, t in sorted(secciones.items()):
        ps = [k for k, v in inv[sigla]['puntos'].items() if v['seccion'] == n]
        print(f"  Sección {n}. {t}  [{len(ps)} puntos: {', '.join(ps) if ps else '—'}]")

out = os.path.join(SCRATCH, 'inventario_puntos_por_TO.json')
json.dump(inv, open(out, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print("\nEscrito:", out)
