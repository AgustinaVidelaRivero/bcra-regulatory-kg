"""U-DIAG-PROCESO: prevalencia en la muestra azarosa de ESQ-2 (Wilson 95 %), origen de cada ficha y estrato
(ítem / mini ordenador / resto) de las 38 azarosas sobre la E0 e0-r2. Solo lectura. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B prevalencia.py <salida_e0r2_esq> <censo_estructural.json>"""
import json, sys, math, glob
from collections import Counter
e0r2, censo = sys.argv[1], json.load(open(sys.argv[2]))
sel=json.load(open('data/experiment/esq/cobertura/orden/seleccion_muestra_esq2.json'))
ids_az=[x['chunk_id'] if isinstance(x,dict) else x for x in sel['azarosa']]
ids_di=[x['chunk_id'] if isinstance(x,dict) else x for x in sel['dirigida']]
W=json.load(open('data/experiment/esq/cobertura/fichas/worksheet_fichas_esq2.json'))
n2c={f['n']:f['chunk_id'] for f in W['fichas']}
CONTAMINADAS={23,39,48,65}  # desvios_lectura_esq2.md@bbac990:48-50
for n in (11,13,48,52,64,18,39,61,72,44):
    c=n2c[n]; print(n, c, 'azarosa' if c in ids_az else ('dirigida' if c in ids_di else '??'), 'contaminada' if n in CONTAMINADAS else '')
def wilson(k,n,z=1.96):
    p=k/n; d=1+z*z/n; c=(p+z*z/(2*n))/d; h=z*math.sqrt(p*(1-p)/n+z*z/(4*n*n))/d
    return max(0.0,c-h), c+h
norm=lambda s:' '.join((s or '').split()); dp=lambda s: norm(s).endswith((':','：'))
ch={}
for f in glob.glob(e0r2+'/chunks_*.json'):
    for c in json.load(open(f)): ch[c['id']]=c
def estrato(c):
    if c['tipo']=='punto_terminal' and c.get('herencia') and dp(c['herencia'][-1]['texto']): return 'item'
    if c['tipo']=='mini_chunk' and c.get('rol_bloque') in ('intro','chapeau_seccion') and dp(c['texto']): return 'mini_ordenador'
    return 'resto'
print('estratos de las 38 azarosas:', dict(Counter(estrato(ch[i]) for i in ids_az)))
N=censo['particion_b584']['chunks']
M=censo['particion_b584']['items']+censo['particion_b584']['por_tipo']['mini_ordenador']
for nom,k,n in (('F1',5,38),('F1 sin contaminadas',4,34),('VU',1,38),('VU sin contaminadas',0,34)):
    lo,hi=wilson(k,n)
    print(f'{nom}: {k}/{n} = {k/n:.4f}  Wilson95 [{lo:.4f}, {hi:.4f}]  x {N} unidades = {k/n*N:.0f} [{lo*N:.0f}, {hi*N:.0f}]')
k_estr=sum(1 for i in ids_az if estrato(ch[i]) in ('item','mini_ordenador'))
lo,hi=wilson(5,k_estr)
print(f'F1 en el estrato ítem + mini ordenador: 5/{k_estr} = {5/k_estr:.4f} [{lo:.4f}, {hi:.4f}] x {M} = {5/k_estr*M:.0f} [{lo*M:.0f}, {hi*M:.0f}]')
