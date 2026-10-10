"""Lista las llamadas a herramientas de una transcripción de sesión (nombre, hora, entrada recortada) y, si se pide, los resultados de las
llamadas que no tocan la carpeta indicada. Uso: python3 -I -B llamadas_sesion.py <transcripcion.jsonl> <carpeta_propia> <salida.txt>"""
import json, re, sys
src, propia, out = sys.argv[1], sys.argv[2], sys.argv[3]
L = [json.loads(l) for l in open(src, encoding='utf-8') if l.strip()]
uses = {}
res = {}
for o in L:
    c = (o.get('message') or {}).get('content')
    if not isinstance(c, list):
        continue
    for b in c:
        if b.get('type') == 'tool_use':
            uses[b['id']] = (o.get('timestamp'), b.get('name'), json.dumps(b.get('input'), ensure_ascii=False))
        elif b.get('type') == 'tool_result':
            cc = b.get('content')
            res[b.get('tool_use_id')] = cc if isinstance(cc, str) else '\n'.join(x.get('text', '') for x in cc if isinstance(x, dict))
with open(out, 'w', encoding='utf-8') as f:
    f.write(f'transcripción: {src}\nllamadas: {len(uses)}\n\n')
    for k, (ts, name, inp) in uses.items():
        # rutas absolutas de la entrada: fuera si alguna no está en la carpeta propia ni en el scratchpad de la sesión;
        # una entrada sin rutas absolutas trabaja en la carpeta del último cd
        rutas = re.findall(r'/(?:Users|private)/[^"\\\n]*', inp)
        fuera = any(propia not in r and '/scratchpad' not in r for r in rutas)
        f.write(f'{ts}  {name}  {"FUERA DE LA CARPETA PROPIA" if fuera else "carpeta propia"}\n  {inp[:300]}\n')
        if fuera and name == 'Bash' and 'cat >' not in inp and 'cat >>' not in inp:
            f.write('  resultado:\n' + '\n'.join('    ' + x for x in (res.get(k) or '').splitlines()[:40]) + '\n')
print(out, len(uses))
