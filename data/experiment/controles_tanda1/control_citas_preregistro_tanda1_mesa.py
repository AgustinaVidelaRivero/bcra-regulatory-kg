"""Mesa, 16/10/2026: controla las citas del pre-registro de la tanda 1 (punto 8 del pedido de la autora del 16/10/2026): que cada ruta que
cita exista en HEAD o en el commit que la trae, y que cada sha256 que cita coincida con su archivo. Solo lee (git ls-tree, git cat-file,
git log, git grep y los archivos que se le pasan); no escribe en el repo.
Qué controla, de cada token entre comillas invertidas:
  - una ruta (lleva «/» o termina en una extensión de archivo), con o sin renglones (`ruta:12`, `ruta:12-14`): existe en HEAD (tal cual,
    bajo data/experiment/, o como el único archivo de HEAD que termina así), o la trae el commit (--nuevos), o está en el paquete de la
    mesa (--paquete) y el texto la declara fuera del repo; si lleva renglones, el archivo los tiene;
  - un hash corto sin «…»: es un commit del repo;
  - un sha256 (64 hexadecimales, o un prefijo con «…»): es el sha256 de un archivo de HEAD, del commit o del paquete, o de una versión
    anterior de una ruta citada en el mismo renglón; si no es el de ningún archivo, se busca como valor registrado en un archivo de HEAD.
  - las filas de la tabla de textos firmados (fuente, commit, texto firmado, sha256) se recalculan con git show <commit>:<ruta>, sobre el
    archivo entero o sus primeras N líneas.
Clasifica aparte, sin contarlas como fallas: las rutas del sistema y las direcciones web; las que crea la tanda 1 (FUTURAS); las que el
propio texto declara ausentes («no está en el repo» en el mismo renglón); y los nombres de archivo que se repiten en HEAD, que se
resuelven por la lista sellada del código si está entre los candidatos.
Uso: python3 -I -B <este> <raíz del repo> <pre-registro> <salida.json> [--nuevos <carpeta con los archivos del commit, «/» como «%»>]
     [--paquete <carpeta del paquete de la mesa>] [--codigo <codigo_de_la_cadena_*.json>]"""
import argparse, hashlib, json, os, re, subprocess, sys
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("repo"); ap.add_argument("prereg"); ap.add_argument("salida")
ap.add_argument("--nuevos"); ap.add_argument("--paquete"); ap.add_argument("--codigo"); a = ap.parse_args()
CODIGO = {x["ruta"] for x in json.load(open(a.codigo))["rutas"]} if a.codigo else set()
FUTURAS = {"corpus_tanda1/": "la crea la tanda 1 (nombres de los grafos)", "NO_ABRIR_salida_e3_tanda1.txt": "la crea la tanda 1",
           "NO_ABRIR_conteos_reextracciones_tanda1.json": "la crea la tanda 1"}
FIRMAS = {"protocolo entre tandas": "docs/protocolo_entre_tandas.md",
          "enmienda de la cola humana": "docs/enmienda_protocolo_entre_tandas_2026-10-04_cola_humana.md",
          "enmienda 4": "docs/enmienda4_protocolo_entre_tandas_2026-10-04_crecimiento_del_catalogo_y_alcance.md",
          "enmienda 5": "docs/enmienda5_protocolo_entre_tandas_2026-10-06_grafo_evaluado_sin_cola.md",
          "enmienda 6": "docs/enmienda6_protocolo_entre_tandas_2026-10-08_cambio_de_modelo_del_extractor.md",
          "enmienda 7": "docs/enmienda7_protocolo_entre_tandas_2026-10-08_excepcion_tanda0_en_el_resellado.md",
          "pre-registro de la tanda 0 (plantilla)": "docs/preregistro_tanda0.md"}
def git(*x, check=True): return subprocess.run(["git", "--no-optional-locks", "-C", a.repo, *x], capture_output=True, check=check).stdout
texto = Path(a.prereg).read_text(encoding="utf-8"); lineas = texto.splitlines()
# Índice de HEAD: ruta -> sha256 y cantidad de renglones
arbol = [l.split("\t", 1) for l in git("ls-tree", "-r", "HEAD").decode().splitlines()]
blobs = [(meta.split()[2], ruta) for meta, ruta in arbol if meta.split()[1] == "blob"]
import tempfile
_ent = tempfile.TemporaryFile(); _ent.write("".join(b + "\n" for b, _ in blobs).encode()); _ent.seek(0)
p = subprocess.Popen(["git", "--no-optional-locks", "-C", a.repo, "cat-file", "--batch"], stdin=_ent, stdout=subprocess.PIPE)
sha_head, renglones_head = {}, {}
for b, ruta in blobs:
    cab = p.stdout.readline().split(); n = int(cab[2]); datos = p.stdout.read(n); p.stdout.read(1)
    sha_head[ruta] = hashlib.sha256(datos).hexdigest(); renglones_head[ruta] = datos.count(b"\n") + (0 if datos.endswith(b"\n") or not datos else 1)
p.wait()
nuevos = {}
if a.nuevos:
    for f in os.listdir(a.nuevos):
        b = (Path(a.nuevos) / f).read_bytes(); nuevos[f.replace("%", "/")] = (hashlib.sha256(b).hexdigest(), b.count(b"\n"))
paquete = {}
if a.paquete:
    for r, _, fs in os.walk(a.paquete):
        for f in fs:
            q = Path(r) / f; rel = str(q.relative_to(a.paquete))
            if rel == "manifest.txt": continue
            paquete[rel] = hashlib.sha256(q.read_bytes()).hexdigest()
sha_a_rutas = {}
for ruta, s in sha_head.items(): sha_a_rutas.setdefault(s, []).append(("HEAD", ruta))
for ruta, (s, _) in nuevos.items(): sha_a_rutas.setdefault(s, []).append(("commit", ruta))
for ruta, s in paquete.items(): sha_a_rutas.setdefault(s, []).append(("paquete", ruta))
EXT = r"\.(md|py|json|jsonl|txt|csv|sh|zsh|yml|yaml|pdf|db)"
def resolver_ruta(tok):
    m = re.match(r"^(.*?" + EXT + r")(?::([0-9][0-9,\-y ]*))?$", tok)
    base = m.group(1) if m else tok; rng = m.group(3) if m else None
    cand = []
    for r in (base, "data/experiment/" + base):
        if r in sha_head: cand = [("HEAD", r)]; break
        if r in nuevos: cand = [("commit", r)]; break
        if r.endswith("/") and any(x.startswith(r) for x in sha_head): cand = [("HEAD", r)]; break
    if not cand:
        suf = [x for x in sha_head if x.endswith("/" + base)] + [x for x in nuevos if x.endswith("/" + base)]
        if base.endswith("/"): suf = sorted({x[: x.index("/" + base) + len(base) + 1] for x in sha_head if ("/" + base) in x})
        if len(suf) == 1: cand = [("HEAD" if suf[0] in sha_head or suf[0].endswith("/") else "commit", suf[0])]
        elif len(suf) > 1:
            enc = [x for x in suf if x in CODIGO]
            if len(enc) == 1: cand = [("HEAD", enc[0])]
            else: return {"estado": "nombre repetido en HEAD", "candidatos": suf[:4], "n": len(suf)}
    if not cand:
        if base.endswith("/"):
            pkd = sorted({x[: x.index(base) + len(base)] for x in paquete if x.startswith(base) or ("/" + base) in x})
            if pkd: return {"estado": "en el paquete de la mesa", "ruta": pkd[0]}
        pk = [x for x in paquete if x == base or x.endswith("/" + base)]
        if pk: return {"estado": "en el paquete de la mesa", "ruta": pk[0]}
        return {"estado": "no encontrada"}
    donde, r = cand[0]; out = {"estado": "en HEAD" if donde == "HEAD" else "la trae el commit", "ruta": r}
    if rng:
        nums = [int(x) for x in re.findall(r"\d+", rng)]
        tot = renglones_head.get(r) if donde == "HEAD" else nuevos.get(r, (None, None))[1]
        out["renglones"] = rng.strip(); out["renglones_ok"] = tot is not None and max(nums) <= tot; out["renglones_del_archivo"] = tot
    return out
def es_commit(h):
    return git("cat-file", "-t", h, check=False).strip() == b"commit"
citas = []
for i, l in enumerate(lineas, 1):
    for tok in re.findall(r"`([^`]+)`", l):
        tok = tok.strip()
        if re.search(r"[<>{}*\s]", tok) and not re.match(r"^[0-9a-f]{6,64}…$", tok): continue
        hexm = re.match(r"^([0-9a-f]{6,64})(…|\.\.\.)?$", tok)
        if hexm:
            h, puntos = hexm.group(1), hexm.group(2)
            if not puntos and len(h) <= 12 and es_commit(h): citas.append({"renglon": i, "token": tok, "tipo": "commit", "estado": "commit del repo"}); continue
            pass
            arch = [x for s, xs in sha_a_rutas.items() if s.startswith(h) for x in xs]
            if arch: citas.append({"renglon": i, "token": tok, "tipo": "sha256", "estado": "archivo", "de": arch[:4]}); continue
            citas.append({"renglon": i, "token": tok, "tipo": "sha256", "estado": "pendiente", "prefijo": h}); continue
        if "/" in tok or re.search(EXT + r"(:[0-9][0-9,\-y ]*)?$", tok):
            if tok.startswith(":"): continue
            if tok.startswith(("http://", "https://")) or (tok.startswith("/") and not tok.startswith("/data")):
                citas.append({"renglon": i, "token": tok, "tipo": "ruta", "estado": "fuera del repo (sistema o web)"}); continue
            if tok in FUTURAS: citas.append({"renglon": i, "token": tok, "tipo": "ruta", "estado": "la crea la tanda 1", "por": FUTURAS[tok]}); continue
            r = resolver_ruta(tok)
            if r["estado"] == "no encontrada" and "no está en el repo" in (l + " " + (lineas[i] if i < len(lineas) else "")):
                r = {"estado": "declarada ausente en el texto"}
            citas.append({"renglon": i, "token": tok, "tipo": "ruta", **r})
# sha256 que no son de un archivo de HEAD, del commit ni del paquete: versiones anteriores de rutas del mismo renglón, o valor registrado
pend = [c for c in citas if c.get("estado") == "pendiente"]
for c in pend:
    rutas_renglon = [x["ruta"] for x in citas if x["renglon"] == c["renglon"] and x.get("tipo") == "ruta" and x.get("ruta") and x["ruta"] in sha_head]
    for r in rutas_renglon:
        for com in git("log", "--format=%H", "--", r).decode().split():
            b = git("show", f"{com}:{r}", check=False)
            if b and hashlib.sha256(b).hexdigest().startswith(c["prefijo"]):
                c["estado"] = "versión anterior de una ruta del renglón"; c["de"] = [r, com[:8]]; break
        if c["estado"] != "pendiente": break
pend = [c for c in citas if c.get("estado") == "pendiente"]
if pend:
    pat = sorted({c["prefijo"] for c in pend})
    r = subprocess.run(["git", "--no-optional-locks", "-C", a.repo, "grep", "-I", "-l", "-F", *sum([["-e", x] for x in pat], []), "HEAD", "--",
                        ".", ":!docs/preregistro_tanda1.md"], capture_output=True)
    archivos = [x.split(":", 1)[1] for x in r.stdout.decode().splitlines()]
    paquete_texto = {}
    if a.paquete:
        for rel in paquete:
            q = Path(a.paquete) / rel
            if q.stat().st_size <= 5_000_000 and q.suffix in (".md", ".json", ".txt", ".jsonl", ".py", ".sh", ".csv"): paquete_texto[rel] = q.read_bytes()
    for c in pend:
        donde = []
        for f in archivos:
            if c["prefijo"].encode() in git("show", f"HEAD:{f}"): donde.append(f)
            if len(donde) >= 3: break
        if donde: c["estado"] = "valor registrado en el repo"; c["en"] = donde
        else:
            pk = [rel for rel in paquete_texto if c["prefijo"].encode() in paquete_texto[rel]][:3]
            c["estado"] = "valor registrado en el paquete de la mesa" if pk else "no encontrado"
            if pk: c["en"] = pk
# La tabla de textos firmados: se recalcula cada fila
firmas = []
for i, l in enumerate(lineas, 1):
    m = re.match(r"^\| ([^|]+?) \| `([0-9a-f]{7,12})` \| ([^|]+?) \| `([0-9a-f]{8,64})…?` \|$", l)
    if not m or m.group(1) not in FIRMAS: continue
    fuente, com, como, pref = m.groups(); ruta = FIRMAS[fuente]
    datos = git("show", f"{com}:{ruta}", check=False)
    n = re.search(r"primeras (\d+) líneas", como)
    if n: datos = b"".join(datos.splitlines(keepends=True)[: int(n.group(1))])
    s = hashlib.sha256(datos).hexdigest()
    firmas.append({"renglon": i, "fuente": fuente, "ruta": ruta, "commit": com, "texto": como, "citado": pref, "calculado": s[:16], "coincide": s.startswith(pref)})
    for c in citas:
        if c["renglon"] == i and c.get("prefijo") == pref or (c["renglon"] == i and c["token"].startswith(pref)):
            c["estado"] = "texto firmado recalculado" if s.startswith(pref) else "texto firmado NO coincide"; c["de"] = [ruta, com]
from collections import Counter
res = {"preregistro": a.prereg.split("/")[-1], "sha256_preregistro": hashlib.sha256(texto.encode()).hexdigest(), "head": git("rev-parse", "HEAD").decode().strip(),
       "citas": len(citas), "por_tipo_y_estado": {f"{k[0]}: {k[1]}": v for k, v in sorted(Counter((c["tipo"], c["estado"]) for c in citas).items())},
       "renglones_mal": [c for c in citas if c.get("renglones_ok") is False], "textos_firmados": firmas,
       "a_revisar": [c for c in citas if c["estado"] in ("no encontrada", "no encontrado", "ambigua", "texto firmado NO coincide")], "detalle": citas}
Path(a.salida).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: res[k] for k in ("citas", "por_tipo_y_estado")}, ensure_ascii=False, indent=1))
print("textos firmados:", [(f["fuente"], f["coincide"]) for f in firmas])
print("renglones fuera del archivo:", len(res["renglones_mal"]), "| a revisar:", len(res["a_revisar"]))
for c in res["a_revisar"] + res["renglones_mal"]: print("  ", c["renglon"], c["token"][:90], "|", c["estado"], c.get("candidatos", "") or c.get("renglones_del_archivo", ""))
