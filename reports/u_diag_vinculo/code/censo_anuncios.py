"""U-DIAG-VINCULO, tareas 3 y 4: censo de los párrafos sin numerar que anuncian el contenido de sus subpuntos
(tanda 0 y partición), muestra de 10 casos, derivación simulada de la dirección (a) sobre KG-Tanda0-Diez-r2a
y sorteo de la muestra de precisión. Implementa `reports/u_diag_vinculo/regla_deteccion.md`, escrita antes de
correr este script (su sha256 se imprime al empezar).

Solo lectura, USD 0. Corre sobre una copia copiada del repo (regla l). Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B censo_anuncios.py <espejo> <regla_deteccion.md> <dir_salida>
"""
import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

espejo, regla, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
out.mkdir(parents=True, exist_ok=True)
SEMILLA = 20261004
T0 = espejo / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0"
T0R2 = espejo / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2"
PART = espejo / "data/experiment/segmentacion_84/b584_particion"
KG_DIEZ = espejo / "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json"
ROLES_CONT = ("intro", "chapeau_seccion", "intersticial")
TIPOS_CONTENIDO = ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad", "Condicion", "Definicion")

lineas: list[str] = []


def p(*a):
    s = " ".join(str(x) for x in a)
    lineas.append(s)
    print(s)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


p("regla:", regla.name, "sha256", sha(regla))

# --- §3 y §5: expresiones (copiadas de la regla) --------------------------------------------------------
CATAFORA = re.compile(r"\b(los|las) siguientes\b|\blo siguiente\b|\ba continuaci[oó]n\b|\bseguidamente\b|"
                      r"\b(en|de) (los|las) (puntos|apartados|incisos) (siguientes|que siguen)\b", re.I)
CORTE = re.compile(r"(?<=[.;])\s+(?=[A-ZÁÉÍÓÚÑ¿«“\"(])")
EXC_NEG = re.compile(r"sin excepci[oó]n|salvo (que|disposici[oó]n|lo (dispuesto|previsto|establecido|indicado)|"
                     r"indicaci[oó]n|expresa|autorizaci[oó]n|en (los|las|el|la) casos? (previst|indicad|establecid))")
EXC = re.compile(r"excepci[oó]n|excepto|exceptu|salvo|exclu[iy]|exclusi[oó]n|exim|"
                 r"no (se )?(alcanza|comprend|inclu|consider|computa|aplica)|"
                 r"no (ser[aá]n?|estar[aá]n?|quedar[aá]n?) (de aplicaci[oó]n|aplicables?|alcanzad|comprendid|"
                 r"incluid|considerad|computad|sujet)|quedan? (excluid|exceptuad|eximid|fuera)|no corresponder[aá]")
C1A = re.compile(r"\b(siempre que|siempre y cuando|en la medida (en )?que|a condici[oó]n de que|en tanto que?)\b")
C1B = re.compile(r"\b(siguientes|estos|tales) (casos|supuestos|situaciones|circunstancias|hip[oó]tesis)\b")
C1C = re.compile(r"\b(cuando|si)\b[^.;:]{0,40}:\s*$")
C1D = re.compile(r"\bsiguientes (condiciones|requisitos|exigencias|recaudos|extremos|par[aá]metros|criterios)\b")
C1D_NEG = re.compile(r"\bdeber[aá]n?\s+(observar|cumplir|reunir|satisfacer|contar con|contener|incluir|presentar|"
                     r"verificar)\b")
C2 = re.compile(r"\bcuando\b|\ben (el|los) casos? (de|en) que\b|\ben caso de\b|\bsi\b|\bcondici[oó]n|"
                r"\bsiempre que\b|\ben la medida\b")
ALC = re.compile(r"\babarca|\bcomprende|\bcomprender[aá]n?\b|\bincluye|\bincluir[aá]n?\b|\bse incluyen\b|\balcanza|"
                 r"\balcanzar[aá]n?\b|\bse (considerar[aá]n?|entender[aá]n?|entiende|consideran?)\b|\bcomprendid|"
                 r"\balcanzad|\bintegra|\bcompon|\bconforma|\bson (las|los) siguientes\b|\bser[aá]n? (elegibles|"
                 r"considerad)|\btales como\b|\ba saber\b|\bse (clasificar|agrupar)[aá]n?\b|\bcategor[ií]as?\b|"
                 r"\bse definen?\b|\bdefin[ei]|\bconceptos?\b|\bclases?\b|\btipos? de\b")


def normalizar(t: str) -> str:
    return " ".join(re.sub(r"-\n(?=[a-záéíóúñ])", "", t or "").split())


def anuncia(texto: str):
    """Devuelve (anuncia, criterio, clausula, lista_en_linea)."""
    t = normalizar(texto)
    if t.rstrip().endswith((":", "：")):
        return True, "A1", CORTE.split(t)[-1], False
    ms = list(CATAFORA.finditer(t))
    if not ms:
        return False, None, None, False
    resto = t[ms[-1].end():]
    if re.search(r":\s*\S", resto):
        return False, None, None, True
    pos, clausula = 0, t
    for seg in CORTE.split(t):
        ini = t.find(seg, pos)
        if ini <= ms[-1].start() < ini + len(seg):
            clausula = seg
            break
        pos = ini + len(seg)
    return True, "A2", clausula, False


def tipo_anuncio(clausula: str) -> str:
    c = clausula.lower()
    if EXC.search(EXC_NEG.sub(" ", c)):
        return "excepcion"
    if C1A.search(c) or C1B.search(c) or C1C.search(c) or (C1D.search(c) and not C1D_NEG.search(c)):
        return "condicion_c1"
    if C2.search(c):
        return "condicion_c2"
    if ALC.search(c):
        return "alcance"
    return "enumeracion"


def unidad_de(c: dict) -> str:
    return (c.get("unidad") or "").split(" ")[0]


def es_hijo(v: str, u: str) -> bool:
    m = re.fullmatch(r"S(\d+)", u)
    if m:
        return re.fullmatch(rf"{m.group(1)}\.\d+", v) is not None
    return re.fullmatch(rf"{re.escape(u)}\.\d+", v) is not None


def censo(chunks: list[dict]):
    por_to: dict[str, list[dict]] = defaultdict(list)
    for c in chunks:
        por_to[c["to"]].append(c)
    conts, n_en_linea, n_no_anuncia, n_sin_hijos = [], 0, 0, 0
    for to, cs in por_to.items():
        unidades = defaultdict(list)
        for c in cs:
            unidades[unidad_de(c)].append(c)
        for k in cs:
            if k["tipo"] != "mini_chunk" or k.get("rol_bloque") not in ROLES_CONT:
                continue
            u = unidad_de(k)
            ok, crit, clausula, en_linea = anuncia(k["texto"])
            if en_linea:
                n_en_linea += 1
            if not ok:
                n_no_anuncia += 1
                continue
            hijos = sorted(v for v in unidades if es_hijo(v, u))
            if k["rol_bloque"] == "intersticial":
                hijos = [v for v in hijos if any(h["tipo"] == "intersticial" and h["unidad_origen"] == u
                                                 for c in unidades[v] for h in c.get("herencia", []))]
            if not hijos:
                n_sin_hijos += 1
                continue
            conts.append({"id": k["id"], "to": to, "unidad": u, "rol": k["rol_bloque"], "criterio": crit,
                          "tipo": tipo_anuncio(clausula), "clausula": clausula, "texto": normalizar(k["texto"]),
                          "hijos": hijos, "chunks_hijos": {v: [c["id"] for c in unidades[v]] for v in hijos},
                          "texto_primer_hijo": normalizar(unidades[hijos[0]][0]["texto"])[:160],
                          "id_primer_hijo": unidades[hijos[0]][0]["id"]})
    candidatos = sum(1 for c in chunks if c["tipo"] == "mini_chunk" and c.get("rol_bloque") in ROLES_CONT)
    return conts, {"chunks": len(chunks), "parrafos_candidatos": candidatos, "no_anuncian": n_no_anuncia,
                   "lista_en_linea": n_en_linea, "anuncian_sin_hijos": n_sin_hijos, "contenedores": len(conts),
                   "pares": sum(len(c["hijos"]) for c in conts),
                   "por_tipo_contenedores": dict(Counter(c["tipo"] for c in conts)),
                   "por_tipo_pares": dict(Counter(c["tipo"] for c in conts for _ in c["hijos"])),
                   "por_rol": dict(Counter(c["rol"] for c in conts)),
                   "por_criterio": dict(Counter(c["criterio"] for c in conts))}


def cargar(dirpath: Path, patron: str) -> list[dict]:
    res = []
    for f in sorted(dirpath.glob(patron)):
        res += json.loads(f.read_text(encoding="utf-8"))
    return res


t0 = cargar(T0, "chunks_*.json")
t0r2 = cargar(T0R2, "chunks_*.json")
part = cargar(PART, "*/chunks_*.json")
c_t0, r_t0 = censo(t0)
c_t0r2, r_t0r2 = censo(t0r2)
c_part, r_part = censo(part)
p("\n== tarea 3: censo")
for nombre, r in (("tanda0 (E0 legada)", r_t0), ("tanda0 (e0-r2, control)", r_t0r2), ("particion B5.8.4", r_part)):
    p(f"  {nombre}: {json.dumps(r, ensure_ascii=False)}")
p("  control e0-r2 = legada (mismos contenedores, tipos e hijos):",
  [(c["id"], c["tipo"], c["hijos"]) for c in c_t0] == [(c["id"], c["tipo"], c["hijos"]) for c in c_t0r2])
ej = next((c for c in c_t0 if c["id"] == "cla::5.1.1::intro"), None)
p("  control positivo cla::5.1.1::intro:", None if ej is None else (ej["tipo"], ej["criterio"], ej["hijos"]))

# --- §6: muestra de 10 ---------------------------------------------------------------------------------
pool = {c["id"]: dict(c, poblacion="particion") for c in c_part}
for c in c_t0:
    pool[c["id"]] = dict(c, poblacion="tanda0")
rng = random.Random(SEMILLA)
cuota = (("excepcion", 3), ("condicion_c1", 2), ("condicion_c2", 1), ("alcance", 2), ("enumeracion", 2))
muestra10 = []
for tipo, n in cuota:
    ids = sorted(i for i, c in pool.items() if c["tipo"] == tipo)
    muestra10 += [pool[i] for i in rng.sample(ids, min(n, len(ids)))]
p("\n== tarea 3: muestra de 10 (semilla", SEMILLA, ")")
for i, c in enumerate(muestra10, 1):
    p(f"  [{i}] {c['tipo']} | {c['id']} ({c['poblacion']}, {c['rol']}, {c['criterio']}) | hijos: {len(c['hijos'])}")
    p(f"      contenedor: «{c['texto']}»")
    p(f"      primer hijo {c['id_primer_hijo']}: «{c['texto_primer_hijo']}»")

# --- §7: derivación simulada de (a) en KG-Tanda0-Diez-r2a ------------------------------------------------
raw = KG_DIEZ.read_bytes()
p("\n== tarea 4 (a): derivación simulada; kg", KG_DIEZ.name, "sha256", hashlib.sha256(raw).hexdigest())
kg = json.loads(raw)
nodo = {n["id"]: n for n in kg["nodes"]}
anclados: dict[str, set] = defaultdict(set)
for n in kg["nodes"]:
    if n["type"] not in TIPOS_CONTENIDO:
        continue
    for pv in n.get("provenances") or [n.get("provenance")]:
        if pv and not (pv.get("rol_documental") or "").startswith("herencia"):
            anclados[pv.get("chunk_id")].add(n["id"])
salientes: dict[str, set] = defaultdict(set)
existentes = set()
for e in kg["edges"]:
    salientes[e["source"]].add(e["relation"])
    existentes.add((e["source"], e["relation"], e["target"]))

DESTINOS_C1 = ("Excepcion", "Obligacion", "Restriccion", "Operacion", "Potestad")
pares_aT, pares_aR = [], []
cont_aT = Counter()
for c in c_t0:
    n_k = sorted(anclados.get(c["id"], set()))
    for v in c["hijos"]:
        n_v = sorted({i for ch in c["chunks_hijos"][v] for i in anclados.get(ch, set())})
        par = {"contenedor": c["id"], "tipo": c["tipo"], "hijo": v, "chunks_hijo": c["chunks_hijos"][v],
               "nodos_contenedor": n_k, "nodos_hijo": n_v}
        cont_aT["pares_sin_nodos_contenedor"] += not n_k
        cont_aT["pares_sin_nodos_hijo"] += bool(n_k) and not n_v
        aR = [(s, "remite_a", t) for s in n_k for t in n_v if (s, "remite_a", t) not in existentes]
        if aR:
            pares_aR.append(dict(par, derivadas=aR))
        aT_todos, aT_unico = [], []
        if c["tipo"] == "excepcion":
            dest = [t for t in n_k if nodo[t]["type"] in ("Restriccion", "Obligacion")]
            for s in n_v:
                if nodo[s]["type"] == "Excepcion" and not salientes[s] & {"exceptua", "exceptua_obligacion"}:
                    cont_aT["excepcion_origenes_colgantes"] += 1
                    for t in dest:
                        pr = "exceptua" if nodo[t]["type"] == "Restriccion" else "exceptua_obligacion"
                        aT_todos.append((s, pr, t))
                    if len(dest) == 1:
                        aT_unico += aT_todos[-1:]
        elif c["tipo"] == "condicion_c1":
            dest = [t for t in n_k if nodo[t]["type"] in DESTINOS_C1]
            for s in n_v:
                if nodo[s]["type"] == "Condicion" and "condicion_de" not in salientes[s]:
                    cont_aT["c1_origenes_colgantes"] += 1
                    aT_todos += [(s, "condicion_de", t) for t in dest]
                    if len(dest) == 1:
                        aT_unico.append((s, "condicion_de", dest[0]))
        cont_aT["aristas_todos_destinos"] += len(aT_todos)
        cont_aT["aristas_destino_unico"] += len(aT_unico)
        if aT_unico:
            pares_aT.append(dict(par, derivadas=aT_unico))

tipos_par = Counter(c["tipo"] for c in c_t0 for _ in c["hijos"])
p("  pares de la tanda 0 por tipo:", dict(tipos_par))
p("  (a-T):", dict(cont_aT), "| pares con arista (destino único):", len(pares_aT),
  "| por tipo:", dict(Counter(x["tipo"] for x in pares_aT)),
  "| por predicado:", dict(Counter(a[1] for x in pares_aT for a in x["derivadas"])))
p("  (a-R): pares con arista:", len(pares_aR), "| aristas:", sum(len(x["derivadas"]) for x in pares_aR),
  "| por tipo de anuncio:", dict(Counter(x["tipo"] for x in pares_aR)),
  "| firmas:", dict(Counter(f"{nodo[s]['type']}->{nodo[t]['type']}" for x in pares_aR for s, _, t in x["derivadas"])
                    .most_common(8)))
ej_par = [x for x in pares_aR if x["contenedor"] == "cla::5.1.1::intro"]
p("  ejemplo, (a-R) para cla::5.1.1::intro:", [(x["hijo"], len(x["derivadas"])) for x in ej_par],
  "| (a-T):", [(x["hijo"], x["derivadas"]) for x in pares_aT if x["contenedor"] == "cla::5.1.1::intro"])

# --- §8: muestra de precisión ----------------------------------------------------------------------------
clave = lambda x: (x["contenedor"], x["hijo"])
m_aT = random.Random(SEMILLA).sample(sorted(pares_aT, key=clave), min(15, len(pares_aT)))
m_aR = random.Random(SEMILLA).sample(sorted(pares_aR, key=clave), min(15, len(pares_aR)))
porid = {c["id"]: c for c in t0}


def ficha(x: dict) -> list[str]:
    k = porid[x["contenedor"]]
    s = [f"### {x['contenedor']} -> hijo {x['hijo']} (tipo {x['tipo']})",
         f"CONTENEDOR: «{normalizar(k['texto'])}»"]
    for ch in x["chunks_hijo"]:
        s.append(f"HIJO {ch}: «{normalizar(porid[ch]['texto'])[:900]}»")
    for rot, ids in (("nodos contenedor", x["nodos_contenedor"]), ("nodos hijo", x["nodos_hijo"])):
        for i in ids:
            pr = nodo[i].get("properties", {})
            s.append(f"  {rot}: {nodo[i]['type']} | {nodo[i]['label']} | {pr.get('descripcion') or pr.get('termino')}"
                     f" | {i[:60]}")
    for a in x["derivadas"]:
        s.append(f"  DERIVADA: {nodo[a[0]]['type']}:{nodo[a[0]]['label']} -{a[1]}-> "
                 f"{nodo[a[2]]['type']}:{nodo[a[2]]['label']}")
    return s


txt = ["# Muestra de precisión, dirección (a) — fichas para la lectura (regla §9)", ""]
for rot, m in (("(a-T) predicado tipado, destino único", m_aT), ("(a-R) remite_a estructural", m_aR)):
    txt += [f"## {rot}: {len(m)} pares, {sum(len(x['derivadas']) for x in m)} aristas", ""]
    for i, x in enumerate(m, 1):
        txt += [f"[{i}]"] + ficha(x) + [""]
(out / "muestra_precision_fichas.md").write_text("\n".join(txt), encoding="utf-8")
p("\n== tarea 4 (a): muestra de precisión sorteada")
p("  (a-T):", len(m_aT), "pares,", sum(len(x["derivadas"]) for x in m_aT), "aristas:",
  [clave(x) for x in m_aT])
p("  (a-R):", len(m_aR), "pares,", sum(len(x["derivadas"]) for x in m_aR), "aristas:",
  [clave(x) for x in m_aR])

json.dump({"regla_sha256": sha(regla), "tanda0": r_t0, "tanda0_e0r2": r_t0r2, "particion": r_part,
           "contenedores_tanda0": c_t0, "contenedores_particion": c_part,
           "muestra10": [c["id"] for c in muestra10],
           "derivacion_a": {"aT": dict(cont_aT), "pares_aT": pares_aT, "pares_aR_n": len(pares_aR),
                            "aristas_aR": sum(len(x["derivadas"]) for x in pares_aR)},
           "muestra_aT": [clave(x) for x in m_aT], "muestra_aR": [clave(x) for x in m_aR]},
          open(out / "censo_anuncios.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
(out / "censo_anuncios.txt").write_text("\n".join(lineas) + "\n", encoding="utf-8")
