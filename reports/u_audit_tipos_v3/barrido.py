"""Barrido de lineas con literales de tipos de nodo o predicados (solo lectura)."""
import re, sys, json, collections
TIPOS = ["Restriccion","Excepcion","Obligacion","Operacion","TextoOrdenado","Comunicacion","Sujeto","Condicion","Potestad","Definicion","EntidadFinanciera"]
PREDS = ["establecida_en","referencia","modificada_por","aplica_a","regula","exceptua","exceptua_obligacion","exceptua_operacion","prohibe","limita","ejecuta","requiere","condiciona","condicion_de","subclase_de","miembro_de","instancia_de","parte_de","padre_sugerido"]
rt = re.compile(r"[\"'](%s)[\"']" % "|".join(TIPOS))
rp = re.compile(r"[\"'](%s)[\"']" % "|".join(PREDS))
files = [l.strip() for l in open('/tmp/u_audit_tipos/py_files.txt') if l.strip()]
out = []
por_archivo = collections.Counter()
for f in files:
    try: lines = open(f, encoding='utf-8').read().split('\n')
    except Exception as e: print('ERR', f, e); continue
    for i, l in enumerate(lines, 1):
        t = rt.findall(l); p = rp.findall(l)
        if t or p:
            out.append({"archivo": f, "linea": i, "tipos": sorted(set(t)), "preds": sorted(set(p)), "texto": l.strip()[:220]})
            por_archivo[f] += 1
json.dump(out, open('/tmp/u_audit_tipos/barrido_lineas.json','w'), ensure_ascii=False, indent=0)
print(len(out), 'lineas en', len(por_archivo), 'archivos')
for f,c in por_archivo.most_common(): print(c, f)
