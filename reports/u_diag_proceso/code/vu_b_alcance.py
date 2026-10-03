"""U-DIAG-PROCESO: alcance de la opción VU-B en la tanda 0 (solo lectura, commiteado). Para cada Condicion de
un ITEM sin condicion_de (ni rechazada) y cada Excepcion bajo encabezado de salvedad sin exceptua*: ¿la unidad
del último tramo heredado tiene mini-chunk con nodos de contenido de un tipo destino admitido?"""
import json, glob, re
from collections import Counter
norm=lambda s:' '.join((s or '').split()); dp=lambda s: norm(s).endswith((':','：'))
RE_SALV=re.compile(r'excepci[oó]n|exclusi[oó]n|no alcanzad|no comprendid',re.I)
DEST={'Condicion':{'Excepcion','Obligacion','Restriccion','Operacion','Potestad'},'Excepcion':{'Restriccion','Obligacion'}}
chunks={}
for f in glob.glob('data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_*.json'):
    for c in json.load(open(f)): chunks[c['id']]=c
fin={}
for f in sorted(glob.glob('data/experiment/reextraccion_v2/corpus_tanda0/salida/*/extracciones_finales_*.jsonl')):
    for l in open(f):
        r=json.loads(l)
        if r.get('validacion'): fin[r['chunk_id']]=r['validacion']
cnt=Counter(); ejemplos=[]
for cid,v in fin.items():
    c=chunks.get(cid)
    if not c or c['tipo']!='punto_terminal' or not c.get('herencia'): continue
    rels=v.get('relaciones',[]); rech=[x.get('elemento') or {} for x in v.get('rechazos',[]) if x.get('nivel')=='relacion']
    out=lambda lid,P: any(x['source']==lid and x['predicate'] in P for x in rels) or any(x.get('source')==lid and x.get('predicate') in P for x in rech)
    ult=c['herencia'][-1]; item=dp(ult['texto'])
    salv=any(h['tipo']=='encabezado' and RE_SALV.search(h['texto']) for h in c['herencia'])
    for e in v.get('entidades',[]):
        t=e['type']
        if t=='Condicion' and item and not out(e['local_id'],{'condicion_de'}):
            pass
        elif t=='Excepcion' and salv and not out(e['local_id'],{'exceptua','exceptua_obligacion'}):
            pass
        else:
            continue
        cnt[(t,'colgante')]+=1
        U=ult['unidad_origen']; mini=f"{c['to']}::{U}::intro"
        vm=fin.get(mini)
        destinos=[x for x in (vm or {}).get('entidades',[]) if x['type'] in DEST[t]] if vm else []
        if ult['tipo']=='intro' and destinos:
            cnt[(t,'encabezado_con_nodos_destino')]+=1; ejemplos.append((cid,t,mini,[x['type'] for x in destinos]))
        elif ult['tipo']=='encabezado':
            cnt[(t,'encabezado_es_titulo_sin_unidad_o_titulo')]+=1
        else:
            cnt[(t,'otro')]+=1
print({'|'.join(k):n for k,n in sorted(cnt.items())})
for x in ejemplos[:10]: print(' ',x)
