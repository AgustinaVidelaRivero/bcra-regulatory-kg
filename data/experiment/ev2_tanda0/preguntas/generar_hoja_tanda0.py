"""generar_hoja_tanda0.py — hoja de clasificación A CIEGAS de las 20 preguntas de
la tanda 0 (fase 2b), con el molde de scripts/ev2_tipo_generar_hoja.py (U-EV2-TIPO):
columnas orden, id, to, pregunta, ancla, criterios, texto_ancla, tipo, nota.
SIN tipo_previsto. Orden de lectura: regla v2 §Procedimiento 1 aplicada a este
conjunto (enmienda (12) §Alcance): ids ordenados alfabéticamente, barajados con
random.Random(20260927).shuffle. Texto del punto ancla desde el índice E0 real
de la tanda 0 (e0_chunking/salida_tanda0/estructura_<to>.json), con su subárbol,
mismo render que la hoja de EV2. Diferencias con el molde: (a) admite 1 o 2
anclas por pregunta (varios puntos): se renderizan las dos, separadas por una
línea «=====»; (b) el chequeo «prefijo == subárbol» del molde se reporta en vez
de abortar; (c) un ancla de sección sin puntos («S10», chunk <to>::S10 de E0)
se resuelve al nodo de tipo «seccion» con numero «10» de la estructura. Solo lectura sobre el repo; escribe únicamente la hoja.
Uso: PYTHONDONTWRITEBYTECODE=1 python3 data/experiment/ev2_tanda0/preguntas/generar_hoja_tanda0.py
"""
import csv, hashlib, json, random, sys
from pathlib import Path

BASE = Path("data/experiment/reextraccion_v2/e0_chunking/salida_tanda0")
QPATH = Path("data/experiment/ev2_tanda0/preguntas/preguntas_tanda0.json")
OUT = Path("data/experiment/ev2_tanda0/preguntas/tipo_pregunta_hoja_tanda0.csv")
SEMILLA = 20260927
TOS = ["ctacte", "lingob", "polcre", "pagjub", "docvig"]
SHA_Q_ESPERADO = "b36e0662170004a5"   # prefijo; el sha completo se imprime

if OUT.exists():
    sys.exit("FRENO: la hoja ya existe")
sha_q = hashlib.sha256(QPATH.read_bytes()).hexdigest()
if not sha_q.startswith(SHA_Q_ESPERADO):
    sys.exit(f"FRENO: preguntas_tanda0.json con sha inesperado {sha_q}")

qs = json.load(open(QPATH, encoding="utf-8"))["preguntas"]
byid = {q["id"]: q for q in qs}
ids = sorted(byid)
rng = random.Random(SEMILLA)
rng.shuffle(ids)
orden = {id_: i + 1 for i, id_ in enumerate(ids)}
E0 = {to: json.load(open(BASE / f"estructura_{to}.json", encoding="utf-8")) for to in TOS}


def flat(nodes, acc):
    for n in nodes:
        acc.append(n); flat(n.get("hijos", []), acc)
    return acc


def in_scope(num, ancla):
    return num == ancla or num.startswith(ancla + ".")


def numkey(num):
    try:
        return tuple(int(x) for x in num.split("."))
    except ValueError:
        return (10**9, num)


def faltantes_por_saltos(d, ancla):
    miss = []
    for s in d.get("saltos_numeracion", []):
        if s.get("tipo") != "salto_hermano":
            continue
        for k in range(s["de"] + 1, s["a"]):
            num = f"{s['padre']}.{k}"
            if in_scope(num, ancla):
                miss.append(num)
    return miss


def render(n, faltantes, blocks, no_enc):
    num = n["numero"]
    tit = (n.get("titulo") or "").strip()
    segs = n.get("segmentos", [])
    lead = [s for s in segs if s["rol"] != "cierre"]
    cierre = [s for s in segs if s["rol"] == "cierre"]
    if not segs and not tit and not n.get("hijos"):
        blocks.append(f"[{num}] NO ENCONTRADO"); no_enc.append(num)
    else:
        parts = [f"[{num}] {tit}".rstrip()]
        for s in lead:
            t = s["texto"]
            if s["rol"] == "intersticial":
                t = "(intersticial) " + t
            parts.append(t)
        blocks.append("\n".join(parts))
    items = [(numkey(h["numero"]), "nodo", h) for h in n.get("hijos", [])]
    items += [(numkey(m), "falta", m) for m in faltantes if m.rsplit(".", 1)[0] == num]
    for _, kind, obj in sorted(items, key=lambda x: x[0]):
        if kind == "nodo":
            render(obj, faltantes, blocks, no_enc)
        else:
            blocks.append(f"[{obj}] NO ENCONTRADO"); no_enc.append(obj)
    if cierre:
        blocks.append("\n".join([f"[{num}] (cierre)"] + [s["texto"] for s in cierre]))


def texto_de(to, num, id_, no_enc, avisos):
    d = E0[to]
    nodes = flat(d["secciones"], [])
    anc = next((n for n in nodes if n["numero"] == num), None)
    if anc is None and num.startswith("S") and num[1:].isdigit():
        # ancla de sección sin puntos («S10»): en la estructura la sección lleva numero «10»
        # y tipo «seccion»; el chunk de E0 se llama <to>::S10 (seccion_sin_puntos).
        anc = next((n for n in nodes if n.get("tipo") == "seccion" and n["numero"] == num[1:]), None)
        if anc is not None:
            avisos.append((id_, f"{to}:{num}", "ancla de sección resuelta a la sección", anc["numero"], (anc.get("titulo") or "")[:40]))
    if anc is None:
        no_enc.append(num); return f"[{num}] NO ENCONTRADO"
    pref = [n["numero"] for n in nodes if in_scope(n["numero"], num)]
    sub = []
    def _sub(n):
        sub.append(n["numero"])
        for h in n.get("hijos", []): _sub(h)
    _sub(anc)
    if pref != sub:
        avisos.append((id_, f"{to}:{num}", "prefijo≠subárbol", len(pref), len(sub)))
    blocks = []
    render(anc, faltantes_por_saltos(d, num), blocks, no_enc)
    return "\n\n".join(blocks)


rows, no_enc_ids, pipes, avisos = [], [], [], []
for id_ in ids:
    q = byid[id_]
    anclas = q["gold"]["ancla"]
    assert 1 <= len(anclas) <= 2, (id_, anclas)
    textos, no_enc = [], []
    for a in anclas:
        to, num = a.split(":")
        assert to == q["to"], (id_, to, q["to"])
        textos.append(texto_de(to, num, id_, no_enc, avisos))
    texto = "\n\n=====\n\n".join(textos)
    if no_enc:
        no_enc_ids.append((id_, anclas, no_enc))
    crits = [c["criterio"] for c in q["gold"]["criterios"]]
    if any("|" in c for c in crits):
        pipes.append(id_)
    rows.append({"orden": orden[id_], "id": id_, "to": q["to"], "pregunta": q["pregunta"],
                 "ancla": " ; ".join(anclas), "criterios": " | ".join(crits), "texto_ancla": texto,
                 "tipo": "", "nota": ""})

cols = ["orden", "id", "to", "pregunta", "ancla", "criterios", "texto_ancla", "tipo", "nota"]
with open(OUT, "w", encoding="utf-8", newline="") as f:
    w = csv.DictWriter(f, fieldnames=cols, lineterminator="\n"); w.writeheader()
    for r in rows: w.writerow(r)

print("preguntas_tanda0.json sha256:", sha_q)
print(f"orden de lectura (semilla {SEMILLA}):", ids)
print("ids con NO ENCONTRADO:", no_enc_ids if no_enc_ids else "ninguno")
print("criterios que contienen '|':", pipes if pipes else "ninguno")
print("avisos prefijo≠subárbol (anclas de sección):", avisos if avisos else "ninguno")
print(f"{'orden':>5}  {'id':<8} {'ancla':<32} {'bytes':>7}")
tot = 0
for r in rows:
    b = len(r["texto_ancla"].encode("utf-8")); tot += b
    print(f"{r['orden']:>5}  {r['id']:<8} {r['ancla']:<32} {b:>7}")
print(f"{'':>5}  {'TOTAL':<8} {'':<32} {tot:>7}")
print("hoja:", OUT, "sha256:", hashlib.sha256(OUT.read_bytes()).hexdigest())
