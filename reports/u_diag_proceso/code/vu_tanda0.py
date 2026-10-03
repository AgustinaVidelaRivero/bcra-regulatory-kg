"""U-DIAG-PROCESO: indicador mecánico del vínculo entre unidades en la tanda 0 (extracción final E1+E3,
commiteada). Condicion de un ITEM (último tramo heredado termina en ':') sin `condicion_de` saliente;
Excepcion bajo encabezado de salvedad sin `exceptua`/`exceptua_obligacion` saliente. Solo lectura."""
import json, glob, re, sys
from collections import Counter
norm=lambda s:' '.join((s or '').split())
dp=lambda s: norm(s).endswith((':','：'))
RE_SALV=re.compile(r'excepci[oó]n|exclusi[oó]n|no alcanzad|no comprendid',re.I)
chunks={}
for f in glob.glob('data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_*.json'):
    for c in json.load(open(f)): chunks[c['id']]=c
cnt=Counter(); ej={'cond':[], 'exc':[]}
for f in sorted(glob.glob('data/experiment/reextraccion_v2/corpus_tanda0/salida/*/extracciones_finales_*.jsonl')):
    for l in open(f):
        r=json.loads(l); c=chunks.get(r['chunk_id']); v=r.get('validacion') or {}
        if not c or c['tipo']!='punto_terminal' or not c.get('herencia'): continue
        ents={e['local_id']:e for e in v.get('entidades',[])}
        rels=v.get('relaciones',[])
        rech=[x.get('elemento') or {} for x in v.get('rechazos',[]) if x.get('nivel')=='relacion']
        sal=lambda lid,preds: any(x['source']==lid and x['predicate'] in preds for x in rels)
        sal_rech=lambda lid,preds: any(x.get('source')==lid and x.get('predicate') in preds for x in rech)
        item=dp(c['herencia'][-1]['texto'])
        enc_salv=any(h['tipo']=='encabezado' and RE_SALV.search(h['texto']) for h in c['herencia'])
        for lid,e in ents.items():
            if e['type']=='Condicion' and item:
                cnt['cond_item']+=1
                if not sal(lid,{'condicion_de'}):
                    cnt['cond_item_sin_condicion_de']+=1
                    if sal_rech(lid,{'condicion_de'}):
                        cnt['cond_item_condicion_de_rechazada_recuperable_r2a']+=1
                    else:
                        cnt['cond_item_sin_condicion_de_ni_rechazada']+=1; ej['cond'].append(r['chunk_id'])
            if e['type']=='Excepcion' and enc_salv:
                cnt['exc_salv']+=1
                if not sal(lid,{'exceptua','exceptua_obligacion'}) and not sal_rech(lid,{'exceptua','exceptua_obligacion'}):
                    cnt['exc_salv_sin_exceptua']+=1; ej['exc'].append(r['chunk_id'])
print(dict(cnt))
print('ejemplos cond:', sorted(set(ej['cond']))[:12])
print('ejemplos exc:', sorted(set(ej['exc']))[:12])
