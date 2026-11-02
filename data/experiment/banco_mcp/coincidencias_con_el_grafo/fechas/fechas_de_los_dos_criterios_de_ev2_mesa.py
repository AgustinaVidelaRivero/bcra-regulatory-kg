"""fechas_de_los_dos_criterios_de_ev2_mesa.py — Mesa, §394 (01/11/2026): cuándo entró al repo cada uno de los dos criterios de EV2
que están en el grafo evaluado (`U6-002` 3 y `U6-021` 1), y cuándo entró la primera descripción que lo trae, por palabras (`\\w+` en
minúsculas, NFC, sin la puntuación). El de `U6-021` es la calibración: la §387 lo fechó por la cadena exacta (`git log -S`).
  1. El criterio: de cada versión de `criterios_u6.json` (de la más vieja a `C`), si la pregunta trae ese criterio con las mismas
     palabras; la primera que lo trae y si sigue igual hasta `C`. Además, si está en el insumo de quien redactó los criterios
     (`preguntas_u6.json` de `C`) y qué renglones de `registro_criterios_u6.md` nombran la pregunta.
  2. Los elementos del grafo evaluado que lo traen en una descripción (por el sha256 corto de su id, como la §392).
  3. La primera descripción: los rastreados de `C` que lo traen en una clave de descripción (los JSON y JSONL por `git grep` de una
     palabra ancla y después por palabras; los `.gz`, descomprimidos uno por uno), y de cada uno la primera versión que lo trae.
  4. La fecha del grafo evaluado: el commit que agrega su `kg.json.gz`.
Nunca imprime un texto: ids, sha256 cortos, rutas, commits, fechas y cuentas. USD 0.
  python3 -I -B fechas_de_los_dos_criterios_de_ev2_mesa.py <repo>
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

R = Path(sys.argv[1]).resolve()
C = "c190505c3ac63bf9d7cf51b94e3be04358cd7832"
U6 = "data/experiment/exploracion/u6_fidelidad/criterios_u6.json"
INSUMO = "data/experiment/exploracion/generacion/preguntas_u6.json"
REG = "data/experiment/exploracion/u6_fidelidad/registro_criterios_u6.md"
GRAFO = "data/experiment/reaplicacion_unica/acumulado/ens_128_r2b_sincola/r2/kg.json.gz"
CASOS = (("U6-002", 3, "b4980f51"), ("U6-021", 1, "5c298d40"))
W = re.compile(r"\w+")
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731


def p(*x):
    print(*x, flush=True)


def git(*a, check=True):
    return subprocess.run(["git", "--no-optional-locks", "-C", str(R), *a], capture_output=True, check=check).stdout


def pal(s):
    return tuple(W.findall(unicodedata.normalize("NFC", s).casefold()))


def contiene(t, aguja):
    n = len(aguja)
    return any(t[i:i + n] == aguja for i in range(len(t) - n + 1) if t[i] == aguja[0])


def criterios_de(blob, qid):
    for q in json.loads(blob)["preguntas"]:
        if q.get("id") == qid:
            return [c["criterio"] if isinstance(c, dict) else c for c in (q.get("gold") or {}).get("criterios", [])]
    return None


def descripciones(x, clave=""):
    if isinstance(x, dict):
        for k, v in x.items():
            yield from descripciones(v, str(k))
    elif isinstance(x, list):
        for v in x:
            yield from descripciones(v, clave)
    elif isinstance(x, str) and "descrip" in clave.lower():
        yield x


def trae(blob, aguja, gz=False):
    try:
        t = (gzip.decompress(blob) if gz else blob).decode("utf-8")
    except (OSError, UnicodeDecodeError, EOFError):
        return False
    docs = []
    try:
        docs = [json.loads(t)]
    except json.JSONDecodeError:
        for ln in t.splitlines():
            try:
                docs.append(json.loads(ln))
            except json.JSONDecodeError:
                continue
    return any(contiene(pal(s), aguja) for d in docs for s in descripciones(d))


u6_c = git("show", f"{C}:{U6}")
kg = json.loads(gzip.decompress(git("show", f"{C}:{GRAFO}")))
gz_rastreados = [r for r in git("ls-tree", "-r", "--name-only", C).decode().splitlines() if r.endswith(".gz")]
alta_grafo = git("log", "--diff-filter=A", "--format=%h %ad", "--date=short", C, "--", GRAFO).decode().split()
p(f"el grafo evaluado ({GRAFO}): lo agrega {alta_grafo[0]}, del {alta_grafo[1]}")
historia = [ln.split("|") for ln in git("log", "--format=%H|%ad", "--date=short", C, "--", U6).decode().splitlines()][::-1]
p(f"criterios_u6.json: {len(historia)} versiones hasta C; los .gz rastreados en C: {len(gz_rastreados)}")
for qid, n, h8 in CASOS:
    t = criterios_de(u6_c, qid)[n - 1]
    if not sha(" ".join(t.split()).encode()).startswith(h8):
        raise SystemExit(f"FRENO: {qid} {n} no da su sha256 corto")
    aguja = pal(t)
    p(f"== {qid}, criterio {n} ({h8}), {len(aguja)} palabras")
    vers = []
    for c, fecha in historia:
        cs = criterios_de(git("show", f"{c}:{U6}"), qid) or []
        vers.append((c, fecha, any(pal(x) == aguja for x in cs), n <= len(cs) and pal(cs[n - 1]) == aguja))
    prim = next((v for v in vers if v[2]), None)
    desde = vers[vers.index(prim):] if prim else []
    p(f"   1. el criterio entra con {prim[0][:8]}, del {prim[1]}; en su lugar ({n}): {prim[3]}; igual en las "
      f"{len(desde)} versiones desde ahí hasta C: {all(v[2] and v[3] for v in desde)}" if prim else "   1. NO ENCONTRADO en la historia")
    ins = json.loads(git("show", f"{C}:{INSUMO}"))
    p(f"      en el insumo (preguntas_u6.json de C): {any(contiene(pal(s), aguja) for q in ins for s in q.values() if isinstance(s, str))}"
      f"; renglones de registro_criterios_u6.md que nombran {qid}: "
      f"{[i for i, l in enumerate(git('show', f'{C}:{REG}').decode().splitlines(), 1) if qid in l]}")
    els = [(col, el) for col in ("nodes", "edges") for el in kg.get(col, [])
           if any(contiene(pal(s), aguja) for s in descripciones(el))]
    p(f"   2. elementos del grafo evaluado con el criterio en una descripción: "
      f"{[(col, sha(str(el.get('id')).encode())[:12]) for col, el in els]}")
    ancla = max((w for w in aguja if w.isascii() and len(w) >= 6), key=len, default=None)
    cand = [r.split(":", 1)[1] for r in git("grep", "-l", "-i", "-F", "-e", ancla, C, "--", ".", ":(exclude)*.gz",
                                              check=False).decode().splitlines()] if ancla else []
    con = [r for r in cand if trae(git("show", f"{C}:{r}"), aguja)]
    con += [r for r in gz_rastreados if trae(git("show", f"{C}:{r}"), aguja, gz=True)]
    primeras = {}
    for r in con:
        log = [ln.split("|") for ln in git("log", "--format=%H|%ad", "--date=short", C, "--", r).decode().splitlines()][::-1]
        primeras[r] = next(((c[:8], f) for c, f in log if trae(git("show", f"{c}:{r}", check=False), aguja, r.endswith(".gz"))),
                           ("-", "-"))
    por_carpeta = collections.Counter(re.sub(r"/[^/]+$", "", r) for r in con)
    p(f"   3. rastreados de C con el criterio en una descripción: {len(con)} (candidatos por la ancla: {len(cand)}, más los .gz); "
      f"por carpeta: {dict(sorted(por_carpeta.items()))}")
    for r in sorted(con, key=lambda r: (primeras[r][1], r)):
        p(f"      {primeras[r][1]} {primeras[r][0]} {r}")
    if primeras:
        f0 = min(primeras.values(), key=lambda x: x[1])
        p(f"      la primera descripción con el criterio entra con {f0[0]}, del {f0[1]}")
