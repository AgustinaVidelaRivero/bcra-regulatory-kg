"""B6.1, tanda final, T3: el grep de convenciones (CLAUDE.md, §5) sobre los archivos de texto nuevos o cambiados de esta parte, sin los
NO_ABRIR_, como en el FRENO T1 de la tanda final (§11). Solo lee; escribe <salida.json>.
  - Los tokens del nombre salen de `git config user.name` del repo, en memoria (se parte en palabras de 3 letras o más, también las pegadas
    en mayúsculas): no se escriben en ningún archivo ni se imprimen.
  - Los términos: slack|e-?mail|correo|whatsapp|reuni[oó]n con|como dijo|pedido por|seg[uú]n (el|la) (mail|mensaje|reuni), sin mayúsculas.
  - Las rutas absolutas: /Users/ o /private/tmp.
  - Aparte, las coincidencias de los tokens del nombre dentro de una ruta absoluta (la carpeta personal o la del scratchpad, que lleva la
    cuenta del usuario) y fuera de ellas, y las de cada término; sin imprimir ningún token.
  - El control positivo: un renglón armado con el primer token y «slack» tiene que dar 2 coincidencias, una por término.
Uso: python3 -I -B grep_convenciones_tf.py <repo> <salida.json> <ruta relativa al repo> [...]   (una carpeta va entera)
"""
import json
import re
import subprocess
import sys
from pathlib import Path

R, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
nombre = subprocess.run(["git", "-C", str(R), "config", "user.name"], capture_output=True, text=True, check=True).stdout.strip()
tokens = sorted({t for t in re.findall(r"[A-ZÁÉÍÓÚÑ]?[a-záéíóúñ]+", nombre) if len(t) >= 3})
TERMINOS = r"slack|e-?mail|correo|whatsapp|reuni[oó]n con|como dijo|pedido por|seg[uú]n (el|la) (mail|mensaje|reuni)"
RX = re.compile("|".join([re.escape(t) for t in tokens] + [TERMINOS]), re.I)
RT = re.compile("|".join(re.escape(t) for t in tokens), re.I) if tokens else None
RTER = re.compile(TERMINOS, re.I)
RUTA = re.compile(r"(/Users/|/private/tmp/[^\s\"']*-Users-)[^\s\"']*", re.I)
ABS = re.compile(r"/Users/|/private/tmp")
archivos = []
for rel in sys.argv[3:]:
    p = R / rel
    archivos += sorted(x for x in p.rglob("*") if x.is_file()) if p.is_dir() else [p]
res = {"archivos": 0, "binarios_o_no_texto": 0, "coincidencias": 0, "archivos_con_coincidencias": [], "con_rutas_absolutas": [],
       "control_positivo": len(RX.findall(f"{tokens[0]} slack")) if tokens else None, "tokens_del_nombre": len(tokens),
       "tokens_dentro_de_rutas_absolutas": 0, "tokens_fuera_de_rutas": 0, "archivos_con_tokens_fuera_de_rutas": [], "por_termino": {}}
for p in archivos:
    if p.name.startswith("NO_ABRIR_"):
        continue
    try:
        t = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        res["binarios_o_no_texto"] += 1
        continue
    res["archivos"] += 1
    n = sum(1 for linea in t.splitlines() if RX.search(linea))
    if n:
        res["coincidencias"] += n
        res["archivos_con_coincidencias"].append({"archivo": str(p.relative_to(R)), "renglones": n})
    if RT:
        n_all, n_fuera = len(RT.findall(t)), len(RT.findall(RUTA.sub("", t)))
        res["tokens_dentro_de_rutas_absolutas"] += n_all - n_fuera
        res["tokens_fuera_de_rutas"] += n_fuera
        if n_fuera:
            res["archivos_con_tokens_fuera_de_rutas"].append({"archivo": str(p.relative_to(R)), "coincidencias": n_fuera})
    for m in RTER.finditer(t):
        k = m.group(0).lower()
        res["por_termino"][k] = res["por_termino"].get(k, 0) + 1
    if ABS.search(t):
        res["con_rutas_absolutas"].append({"archivo": str(p.relative_to(R)), "renglones": sum(1 for x in t.splitlines() if ABS.search(x))})
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
