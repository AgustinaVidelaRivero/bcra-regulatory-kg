"""U-DIAG-PROCESO: tasa de unidades sin contenido (entidades distintas de TextoOrdenado) en ITEMS y MINIS
ORDENADORES: ESQ-2 (E1 solo, prefijo de producción; commiteado) frente a la tanda 0 (E1 v3_b54 + E3 con un
reintento; commiteado). Indicador mecánico; no es lectura. Solo lectura. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B vacios_esq_vs_t0.py <salida_e0r2_esq>"""
import json, glob, sys
from collections import Counter
from pathlib import Path
E0R2=Path(sys.argv[1])
norm=lambda s:' '.join((s or '').split()); dp=lambda s: norm(s).endswith((':','：'))
def cls(c):
    if c['tipo']=='punto_terminal' and c.get('herencia') and dp(c['herencia'][-1]['texto']): return 'item'
    if c['tipo']=='mini_chunk' and c.get('rol_bloque') in ('intro','chapeau_seccion') and dp(c['texto']): return 'mini_ordenador'
    return 'otro_terminal' if c['tipo']=='punto_terminal' else 'otro'
def contar(chunks, ext):
    r=Counter()
    for cid,c in chunks.items():
        k=cls(c); v=ext.get(cid)
        if v is None: r[(k,'sin_salida')]+=1; continue
        n=sum(1 for e in v.get('entidades',[]) if e['type']!='TextoOrdenado')
        r[(k,'vacio' if n==0 else 'con_contenido')]+=1
    return r
esq_chunks={}
for f in glob.glob(str(E0R2/'chunks_*.json')):
    for c in json.load(open(f)): esq_chunks[c['id']]=c
esq_ext={}
for f in glob.glob('data/experiment/esq/cobertura/*/extracciones_e1_*.jsonl'):
    for l in open(f):
        r=json.loads(l); esq_ext[r['chunk_id']]=r.get('validacion') or {}
t0_chunks={}
for f in glob.glob('data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_*.json'):
    for c in json.load(open(f)): t0_chunks[c['id']]=c
t0_ext={}
for f in glob.glob('data/experiment/reextraccion_v2/corpus_tanda0/salida/*/extracciones_finales_*.jsonl'):
    for l in open(f):
        r=json.loads(l)
        if r.get('validacion'): t0_ext[r['chunk_id']]=r['validacion']
for nombre,(ch,ex) in {'esq2_e1solo':(esq_chunks,esq_ext),'tanda0_e1_e3':(t0_chunks,t0_ext)}.items():
    r=contar(ch,ex)
    print(nombre, 'chunks', len(ch), 'con salida', sum(1 for k in ch if k in ex))
    for k in ('item','mini_ordenador','otro_terminal'):
        print('  ',k, {e:r[(k,e)] for e in ('con_contenido','vacio','sin_salida')})
# tanda 0, primera pasada de E1 (antes de E3), mismo indicador
t0_e1={}
for f in glob.glob('data/experiment/reextraccion_v2/corpus_tanda0/salida/*/extracciones_e1.jsonl'):
    for l in open(f):
        r=json.loads(l)
        if r.get('validacion'): t0_e1[r['chunk_id']]=r['validacion']
r=contar(t0_chunks,t0_e1)
print('tanda0_e1_primera_pasada', 'con salida', sum(1 for k in t0_chunks if k in t0_e1))
for k in ('item','mini_ordenador','otro_terminal'):
    print('  ',k, {e:r[(k,e)] for e in ('con_contenido','vacio','sin_salida')})
