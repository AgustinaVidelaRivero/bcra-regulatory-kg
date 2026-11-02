"""criterios_en_el_grafo_por_palabras_t2_mesa.py — Mesa, §392 (01/11/2026): los criterios de evaluación de B6.3, B6.4 y EV2 (U6) que
aparecen en el grafo evaluado cuando se busca palabra por palabra, sin mayúsculas ni puntuación, y por qué la búsqueda por el texto
normalizado con espacios (la del tramo 2 y la de la §387) no los da. Para cada criterio que aparece entero en algún texto del grafo:
  - su sha256 (forma normalizada por espacios), su fuente, el id de su pregunta y su número de criterio (ids, no texto);
  - si es texto de la norma: si aparece entero en el texto de alguna unidad de la E0 (palabra por palabra);
  - en cada texto del grafo donde aparece: la clase y el campo, el sha256 corto del id del elemento, y cuatro preguntas sobre la forma:
    si está igual (normalizado por espacios), igual sin mayúsculas, igual sin mayúsculas ni puntuación, y qué parte del texto ocupa.
Nunca imprime ni escribe un texto: solo sha256, ids, campos, cuentas y booleanos. USD 0.
  python3 -I -B criterios_en_el_grafo_por_palabras_t2_mesa.py <repo> <fuera_del_repo>
"""
import collections
import gzip
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

R, F = (Path(x).resolve() for x in sys.argv[1:3])
C = "c190505c3ac63bf9d7cf51b94e3be04358cd7832"
B63 = F / ("scratchpads/d0348a29-aaa4-4292-82f3-0c0149e3787e/scratchpad/hoja_de_ruta_tanda1_mesa/decisiones_317_mesa/entrada/"
           "salida/preguntas_96_B63.json")
B64 = "data/experiment/banco_mcp/b64/preguntas/aprobadas_B64.json"
U6 = "data/experiment/exploracion/u6_fidelidad/criterios_u6.json"
GRAFO = "data/experiment/reaplicacion_unica/acumulado/ens_128_r2b_sincola/r2/kg.json.gz"
E0 = "data/experiment/tanda_final/t3/acumulado/e0_acumulado_128_r2b/"
DECLARADAS = {"3137d333", "5c298d40"}
W = re.compile(r"\w+")
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731


def p(*x):
    print(*x, flush=True)


def git(*a):
    return subprocess.run(["git", "--no-optional-locks", "-C", str(R), *a], capture_output=True, check=True).stdout


def norm(s):
    return " ".join(s.split())


def sin_puntuacion(s):
    return " ".join(W.findall(unicodedata.normalize("NFC", s).casefold()))


crit = []      # (fuente, id de la pregunta, número de criterio, texto)
b63 = json.loads(B63.read_bytes())
assert sha(B63.read_bytes()).startswith("a5993d5b")
for q in b63["preguntas"]:
    for i, c in enumerate(q.get("criterios", []), 1):
        crit.append(("B6.3", q.get("id"), i, c["criterio"] if isinstance(c, dict) else c))
b64b = git("show", f"{C}:{B64}")
assert sha(b64b).startswith("2ce2ac81")
for q in json.loads(b64b)["preguntas"]:
    for i, c in enumerate(q.get("criterios", []), 1):
        crit.append(("B6.4", q.get("id"), i, c["criterio"] if isinstance(c, dict) else c))
for q in json.loads(git("show", f"{C}:{U6}"))["preguntas"]:
    for i, c in enumerate((q.get("gold") or {}).get("criterios", []), 1):
        crit.append(("EV2 (U6)", q.get("id"), i, c["criterio"] if isinstance(c, dict) else c))
crit = [(f, q, i, t) for f, q, i, t in crit if len(norm(t)) >= 40 and len(W.findall(t)) >= 6]
p(f"criterios de 40 caracteres y 6 palabras o más: {len(crit)} (por fuente: {dict(collections.Counter(c[0] for c in crit))})")
toks = {j: tuple(W.findall(unicodedata.normalize('NFC', t).casefold())) for j, (_, _, _, t) in enumerate(crit)}
indice = collections.defaultdict(list)
for j, t in toks.items():
    indice[t[:5]].append(j)


def buscar(s):
    t = tuple(W.findall(unicodedata.normalize("NFC", s).casefold()))
    out = set()
    for i in range(len(t) - 4):
        for j in indice.get(t[i:i + 5], ()):
            if t[i:i + len(toks[j])] == toks[j]:
                out.add(j)
    return out, len(t)


kg = json.loads(gzip.decompress(git("show", f"{C}:{GRAFO}")))


def textos_de(x, camino=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from textos_de(v, f"{camino}.{k}" if camino else k)
    elif isinstance(x, list):
        for v in x:
            yield from textos_de(v, camino + "[]")
    elif isinstance(x, str) and len(x) >= 40:
        yield camino, x


hall = collections.defaultdict(list)
for col in ("nodes", "edges"):
    for el in kg.get(col, []):
        for camino, s in textos_de(el):
            js, n = buscar(s)
            for j in js:
                t = crit[j][3]
                hall[j].append({"donde": f"{col}.{camino}", "elemento": sha(str(el.get("id")).encode())[:12],
                                "igual_por_espacios": norm(t) in norm(s), "igual_sin_mayusculas": norm(t).casefold() in norm(s).casefold(),
                                "igual_sin_puntuacion": True, "parte": f"{len(toks[j])} de {n} palabras"})
units = {}
for ln in git("ls-tree", "-r", "--name-only", C, "--", E0).decode().splitlines():
    if ln.endswith(".json"):
        units[ln] = git("show", f"{C}:{ln}")
textos_e0 = []


def rec(x):
    if isinstance(x, dict):
        for k, v in x.items():
            if k in ("texto", "texto_propio", "text") and isinstance(v, str):
                textos_e0.append(v)
            else:
                rec(v)
    elif isinstance(x, list):
        for v in x:
            rec(v)


for b in units.values():
    rec(json.loads(b))
en_norma = collections.Counter()
objetivo = set(hall)
for s in textos_e0:
    js, _ = buscar(s)
    for j in js & objetivo:
        en_norma[j] += 1
p(f"criterios que aparecen enteros, palabra por palabra, en algún texto del grafo: {len(hall)}")
for j in sorted(hall, key=lambda j: (crit[j][0], str(crit[j][1]), crit[j][2])):
    f, q, i, t = crit[j]
    h = sha(norm(t).encode())[:8]
    elems = {x["elemento"] for x in hall[j]}
    p(f"- {f} | pregunta {q} | criterio {i} | sha256 {h} | declarada: {h in DECLARADAS} | {len(toks[j])} palabras | entera en "
      f"{en_norma[j]} textos de la E0 | en {len(hall[j])} textos de {len(elems)} elementos del grafo")
    for x in hall[j][:6]:
        p(f"    {x['donde']} | elemento {x['elemento']} | igual por espacios {x['igual_por_espacios']} | igual sin mayúsculas "
          f"{x['igual_sin_mayusculas']} | {x['parte']}")
