"""U-DIAG-PROCESO: chapeaux en línea de título sin unidad propia en la tanda 0 (subcausa de la ficha 11):
cuántos nodos de contenido quedaron anclados en esa unidad tras E1+E3 (commiteado). Solo lectura. Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B f1a_tanda0.py <censo_estructural.json>"""
import json, glob, sys
from collections import defaultdict
d=json.load(open(sys.argv[1]))
U=d['tanda0']['chapeau_titulo_sin_unidad']
chunks={}
for f in glob.glob('data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_*.json'):
    for c in json.load(open(f)): chunks[c['id']]=c
anc=defaultdict(list)
for f in sorted(glob.glob('data/experiment/reextraccion_v2/corpus_tanda0/salida/*/extracciones_finales_*.jsonl')):
    for l in open(f):
        r=json.loads(l); v=r.get('validacion') or {}
        for e in v.get('entidades',[]):
            p=e.get('provenance') or {}
            if e['type']!='TextoOrdenado':
                anc[(p.get('to'),p.get('punto'))].append(r['chunk_id'])
con=0
for u in U:
    to,un=u.split('::')
    tit=next((h['texto'] for c in chunks.values() if c['to']==to for h in c.get('herencia',[])
              if h['unidad_origen']==un and h['tipo']=='encabezado'), '')
    n=len(anc.get((to,un),[])); con+=n>0
    hijos=sum(1 for c in chunks.values() if c['to']==to and c['unidad'].startswith(un+'.'))
    print(u,'|',' '.join(tit.split())[:110],'| nodos anclados en la unidad:',n,'| desde',sorted(set(anc.get((to,un),[]))),'| hijos',hijos)
print('unidades con al menos un nodo anclado:', con, 'de', len(U))
