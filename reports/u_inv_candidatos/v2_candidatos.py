"""
U-INV-CANDIDATOS-2 — candidatos (O, D) con la remisión tal como la escribe el
texto. Solo lectura del repositorio; salidas únicamente en /tmp/u_inv_candidatos/
con prefijo v2_. No sobrescribe archivos de la vuelta anterior.

Definiciones (decisiones del mandato, no re-decididas):
  - Arista de remisión: relation == "referencia" y rol_fuente == "referencia_cruzada".
  - O de una arista = (provenance.to, provenance.punto) de la arista.
  - d de una arista = properties.destino ("to::unidad").
  - D(O) = conjunto de los d de todas las aristas con ese O.
  - Criterios 2-5 como en U-INV-CANDIDATOS; en el 5, «d con remisión saliente»
    = d es O de alguna arista de remisión.
  - Criterio 6: O y cada d tienen en E0 al menos un fragmento tipo punto_terminal.
Exclusiones previas (Paso 1): aristas sin provenance.to/punto; aristas cuyo
destino no es un punto: unidad "TO" (Texto Ordenado completo) o "S<n>"
(sección), según la clasificación de r1_referencias.py:267 ("punto" vs "seccion").
Sin APIs, sin Neo4j, sin índices de búsqueda.
"""
import hashlib
import json
import re
from collections import defaultdict, Counter
from pathlib import Path

REPO = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg")
KG = REPO / "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
EV2 = REPO / "data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json"
OUT = Path("/tmp/u_inv_candidatos")
PREV = OUT / "resultado.json"
TOS = ("cap", "cla", "ext", "pro", "ric")
MAX_O, MAX_D = 80, 120
REF_O = ("ext", "3.17.1.4")
REF_O2 = ("ext", "3.18.1.2")
CRITS = ("1", "2", "3", "4", "5", "6")


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def comps(punto):
    if re.fullmatch(r"S\d+", punto):
        return [punto[1:]]
    return punto.split(".")


def es_ancestro(a, b):
    ca, cb = comps(a), comps(b)
    return len(ca) < len(cb) and cb[: len(ca)] == ca


def es_punto(unidad):
    return bool(re.fullmatch(r"\d+(\.\d+)*", unidad))


def clave_orden(p):
    to, punto = p
    ks = [(0, int(c), "") if c.isdigit() else (1, 0, c) for c in comps(punto)]
    return (TOS.index(to) if to in TOS else 99, ks)


def fmt(p):
    return f"{p[0]}::{p[1]}"


def parse(s):
    to, u = s.split("::", 1)
    return (to, u)


# ---------- carga ----------
sha_kg = sha(KG)
assert sha_kg.startswith("0226e947"), sha_kg
sha_ev2 = sha(EV2)
assert sha_ev2.startswith("1d587336"), sha_ev2
kg = json.loads(KG.read_text())
N = {n["id"]: n for n in kg["nodes"]}

frag = defaultdict(list)          # (to, unidad) -> [(id, texto)]
tipo_frag = {}                    # id -> "tipo[, rol_bloque X]"
tipo_crudo = {}                   # id -> tipo
sha_e0 = {}
for to in TOS:
    f = E0 / f"chunks_{to}.json"
    sha_e0[f.name] = sha(f)
    for x in json.loads(f.read_text()):
        frag[(x["to"], x["unidad"])].append((x["id"], x["texto"]))
        tipo_frag[x["id"]] = x["tipo"] + (f", rol_bloque {x['rol_bloque']}" if x.get("rol_bloque") else "")
        tipo_crudo[x["id"]] = x["tipo"]


def palabras(p):
    fs = frag.get(p)
    if not fs:
        return None
    return sum(len(t.split()) for _, t in fs)


def tiene_terminal(p):
    return any(tipo_crudo[fid] == "punto_terminal" for fid, _ in frag.get(p, []))


def tipos(p):
    return [tipo_frag[fid] for fid, _ in frag.get(p, [])]


ev2 = json.loads(EV2.read_text())["preguntas"]


def ev2_ids(puntos):
    res = []
    for q in ev2:
        motivos = []
        for p in puntos:
            if f"{p[0]}:{p[1]}" in q["gold"]["ancla"]:
                motivos.append(f"ancla {p[0]}:{p[1]}")
            if q["to"] == p[0] and not p[1].startswith("S"):
                pat = r"(?<![\d.])" + re.escape(p[1]) + r"(?!\.?\d)"
                for c in q["gold"]["criterios"]:
                    for campo in ("criterio", "cita_textual"):
                        if re.search(pat, c.get(campo) or ""):
                            motivos.append(f"{campo} {p[1]}")
        if motivos:
            res.append((q["id"], sorted(set(motivos))))
    return res


# ---------- Paso 1: aristas ----------
R = [e for e in kg["edges"] if e["relation"] == "referencia" and e.get("rol_fuente") == "referencia_cruzada"]
sin_prov = [e for e in R if not ((e.get("provenance") or {}).get("to") and (e.get("provenance") or {}).get("punto"))]
con_prov = [e for e in R if e not in sin_prov]
dest_to = [e for e in con_prov if parse(e["properties"]["destino"])[1] == "TO"]
dest_sec = [e for e in con_prov if re.fullmatch(r"S\d+", parse(e["properties"]["destino"])[1])]
dest_otro = [e for e in con_prov if not es_punto(parse(e["properties"]["destino"])[1])
             and e not in dest_to and e not in dest_sec]
validas = [e for e in con_prov if es_punto(parse(e["properties"]["destino"])[1])]


def O_de(e):
    return (e["provenance"]["to"], e["provenance"]["punto"])


# O con remisión saliente (criterio 5): O de cualquier arista de remisión con provenance
origenes_todas = {O_de(e) for e in con_prov}
origenes_validas = {O_de(e) for e in validas}

D = defaultdict(set)
testigos = defaultdict(list)
for i, e in enumerate(validas):
    o, d = O_de(e), parse(e["properties"]["destino"])
    D[o].add(d)
    testigos[(o, d)].append(i)

# aristas cuyo campo provenances tiene puntos que el campo provenance no muestra
ocultos = defaultdict(set)
for e in validas:
    for p in e.get("provenances", []):
        q = (p.get("to"), p.get("punto"))
        if q != O_de(e):
            ocultos[q].add(O_de(e))
n_aristas_multi = sum(1 for e in validas if len({(p.get("to"), p.get("punto")) for p in e.get("provenances", [])}) > 1)


# ---------- criterios ----------
def primer_fallo(o, ds, origenes=origenes_todas):
    if not ds:
        return "1"
    if not (1 <= len(ds) <= 3):
        return "2"
    if any(d[0] == o[0] and (es_ancestro(d[1], o[1]) or es_ancestro(o[1], d[1])) for d in ds):
        return "3"
    wo = palabras(o)
    wd = [palabras(d) for d in ds]
    if wo is None or any(w is None for w in wd) or wo > MAX_O or any(w > MAX_D for w in wd):
        return "4"
    if set(ds) & origenes:
        return "5"
    if not tiene_terminal(o) or not all(tiene_terminal(d) for d in ds):
        return "6"
    return "pasa"


pares = {o: frozenset(ds) for o, ds in D.items() if ds}
fallo = {o: primer_fallo(o, ds) for o, ds in pares.items()}
emb = {}
emb_to = {to: {} for to in TOS}
# embudo secuencial explícito
orden_crit = ["2", "3", "4", "5", "6"]
vivos = set(pares)
emb["1"] = len(vivos)
for to in TOS:
    emb_to[to]["1"] = sum(1 for o in vivos if o[0] == to)
for c in orden_crit:
    vivos = {o for o in vivos if fallo[o] != c}
    emb[c] = len(vivos)
    for to in TOS:
        emb_to[to][c] = sum(1 for o in vivos if o[0] == to)
cand = sorted([o for o in pares if fallo[o] == "pasa"], key=clave_orden)
assert len(cand) == emb["6"]

sin_texto = sorted(fmt(o) for o, ds in pares.items()
                   if fallo[o] == "4" and (palabras(o) is None or any(palabras(d) is None for d in ds)))
# sensibilidad del criterio 5 al conjunto de orígenes (todas vs solo destino-punto)
fallo_alt = {o: primer_fallo(o, ds, origenes_validas) for o, ds in pares.items()}
dif_c5 = sorted(fmt(o) for o in pares if (fallo[o] == "pasa") != (fallo_alt[o] == "pasa"))
secciones_con_terminal = sorted(fmt(k) for k in frag if re.fullmatch(r"S\d+", k[1]) and tiene_terminal(k))


# ---------- ficha ----------
def bloque_texto(lin, p):
    for fid, t in frag.get(p, []):
        lin.append(f"  - fragmento E0 `{fid}` ({tipo_frag[fid]}; campo `texto`):")
        lin.append("")
        lin.append("````text")
        lin.append(t)
        lin.append("````")
        lin.append("")
    if not frag.get(p):
        lin.append("  - (sin fragmento E0 con esa unidad)")


def ficha(o, ds):
    lin = []
    lin.append(f"- Texto Ordenado de O: `{o[0]}`")
    lin.append(f"- O = `{fmt(o)}` — {palabras(o)} palabras")
    bloque_texto(lin, o)
    for d in sorted(ds, key=clave_orden):
        mismo = "mismo Texto Ordenado que O" if d[0] == o[0] else f"otro Texto Ordenado (`{d[0]}`)"
        lin.append(f"- d = `{fmt(d)}` — {palabras(d)} palabras — {mismo}")
        bloque_texto(lin, d)
        idx = testigos.get((o, d), [])
        lin.append(f"  - aristas de remisión con provenance O y destino d: {len(idx)}")
        for i in idx:
            e = validas[i]
            s, t = N[e["source"]], N[e["target"]]
            lin.append(f"    - [{s['type']}] «{s['label']}» → [{t['type']}] «{t['label']}» "
                       f"(evidencia «{e['properties']['evidencia']}»)")
    ids = ev2_ids([o] + sorted(ds, key=clave_orden))
    lin.append("- Preguntas EV2 que citan O o algún d: "
               + ("; ".join(f"`{q}` ({', '.join(m)})" for q, m in ids) if ids else "ninguna"))
    return lin, ids


out = []
out.append("# U-INV-CANDIDATOS-2 — candidatos (O, D) con la remisión tal como la escribe el texto, grafo r1")
out.append("")
out.append(f"- Grafo: `{KG.relative_to(REPO)}` sha256 `{sha_kg}`")
out.append(f"- EV2: `{EV2.relative_to(REPO)}` sha256 `{sha_ev2}`")
for k, v in sha_e0.items():
    out.append(f"- E0: `{(E0 / k).relative_to(REPO)}` sha256 `{v}`")
out.append(f"- Aristas de remisión: {len(R)}; sin provenance to/punto: {len(sin_prov)}; "
           f"destino Texto Ordenado completo: {len(dest_to)}; destino sección: {len(dest_sec)}; "
           f"destino de otra forma no numérica: {len(dest_otro)}; válidas: {len(validas)}")
out.append("- Embudo: " + " → ".join(f"criterio {c}: {emb[c]}" for c in CRITS))
out.append("")
out.append(f"## Candidatos que pasan los seis criterios ({len(cand)})")
out.append("")
tabla = []
for n_c, o in enumerate(cand, 1):
    ds = pares[o]
    dso = sorted(ds, key=clave_orden)
    out.append(f"### V{n_c:02d} — `{fmt(o)}` → {{{', '.join(fmt(d) for d in dso)}}}")
    out.append("")
    lin, ids = ficha(o, ds)
    out.extend(lin)
    out.append("")
    tabla.append({
        "n": n_c, "to": o[0], "O": fmt(o), "D": [fmt(d) for d in dso],
        "palabras_O": palabras(o), "palabras_D": [palabras(d) for d in dso],
        "mismo_to": ["sí" if d[0] == o[0] else "no" for d in dso],
        "ev2": [q for q, _ in ids],
        "fragmentos_O": [fid for fid, _ in frag.get(o, [])],
        "fragmentos_D": {fmt(d): [fid for fid, _ in frag.get(d, [])] for d in dso},
        "tipos_fragmento": {fid: tipo_frag[fid] for q in [o, *dso] for fid, _ in frag.get(q, [])},
    })

# ---------- comparación con la vuelta anterior ----------
prev = json.loads(PREV.read_text())["candidatos"]
prev_pares = {(c["O"], tuple(c["D"])) for c in prev}
nuevos_pares = {(t["O"], tuple(t["D"])) for t in tabla}
nuevos = [t for t in tabla if (t["O"], tuple(t["D"])) not in prev_pares]
salen = []
for c in prev:
    if (c["O"], tuple(c["D"])) in nuevos_pares:
        continue
    o = parse(c["O"])
    if o not in pares:
        motivo = "1"
        det = "O no es provenance de ninguna arista válida"
        otras = sorted(fmt(d) for e in con_prov if O_de(e) == o for d in [parse(e["properties"]["destino"])])
        if otras:
            det += f" (sí de aristas excluidas en el Paso 1 con destino {otras})"
        dv2 = []
    else:
        motivo = fallo[o]
        dv2 = [fmt(d) for d in sorted(pares[o], key=clave_orden)]
        det = f"D en v2 = {dv2}"
    salen.append({"n_prev": c["n"], "O": c["O"], "D_prev": c["D"], "criterio": motivo, "detalle": det, "D_v2": dv2})

# ---------- Paso 4: protección de usuarios ----------
out.append("---")
out.append("")
pro = sorted([o for o in pares if o[0] == "pro"], key=clave_orden)
out.append(f"## Protección de usuarios (pro): todos los pares que pasan el criterio 1 ({len(pro)})")
out.append("")
out.append("| O | D | palabras O | palabras de cada d | tipo de fragmento de O | tipo de fragmento de cada d | primer criterio que no cumple |")
out.append("|---|---|---|---|---|---|---|")
pro_tabla = []
for o in pro:
    dso = sorted(pares[o], key=clave_orden)
    fila = {
        "O": fmt(o), "D": [fmt(d) for d in dso], "palabras_O": palabras(o),
        "palabras_D": [palabras(d) for d in dso], "tipos_O": tipos(o),
        "tipos_D": [tipos(d) for d in dso], "primer_fallo": fallo[o],
    }
    pro_tabla.append(fila)
    out.append(f"| `{fila['O']}` | {', '.join('`' + x + '`' for x in fila['D'])} | {fila['palabras_O']} | "
               f"{', '.join(str(w) for w in fila['palabras_D'])} | {' / '.join(fila['tipos_O']) or '—'} | "
               f"{'; '.join(' / '.join(t) or '—' for t in fila['tipos_D'])} | "
               f"{'pasa' if fila['primer_fallo'] == 'pasa' else 'criterio ' + fila['primer_fallo']} |")
out.append("")
pro_conteo = dict(Counter(fallo[o] for o in pro))
out.append("- Conteo por primer criterio no cumplido: "
           + ", ".join(f"{k}: {pro_conteo.get(k, 0)}" for k in ["2", "3", "4", "5", "6", "pasa"]))
out.append("")

# ---------- Paso 5: referencia ----------
out.append("---")
out.append("")
out.append("## REFERENCIA: `ext::3.17.1.4` con la definición de esta vuelta")
out.append("")
ref_ds = pares.get(REF_O, frozenset())
ref_dso = sorted(ref_ds, key=clave_orden)
out.append(f"- D(O) = {{{', '.join(fmt(d) for d in ref_dso)}}}")
ref_c = {
    "1": bool(ref_ds),
    "2": 1 <= len(ref_ds) <= 3,
    "3": all(not (d[0] == REF_O[0] and (es_ancestro(d[1], REF_O[1]) or es_ancestro(REF_O[1], d[1]))) for d in ref_ds),
    "4": palabras(REF_O) is not None and palabras(REF_O) <= MAX_O
         and all(palabras(d) is not None and palabras(d) <= MAX_D for d in ref_ds),
    "5": not (set(ref_ds) & origenes_todas),
    "6": tiene_terminal(REF_O) and all(tiene_terminal(d) for d in ref_ds),
}
for c in CRITS:
    out.append(f"  - criterio {c}: {'cumple' if ref_c[c] else 'NO cumple'}")
out.append(f"- Resultado del embudo para este O: {fallo.get(REF_O, 'no es O')}")
out.append("")
if ref_ds:
    lin, ids_ref = ficha(REF_O, ref_ds)
    out.extend(lin)
    out.append("")
else:
    ids_ref = []
o2_ds = pares.get(REF_O2)
out.append(f"### `ext::3.18.1.2` como O")
out.append("")
o2_multi = [e for e in validas if any((p.get("to"), p.get("punto")) == REF_O2 for p in e.get("provenances", []))]
if o2_ds:
    out.append(f"- Aparece como O con D = {{{', '.join(fmt(d) for d in sorted(o2_ds, key=clave_orden))}}}; "
               f"resultado del embudo: {fallo[REF_O2]}")
else:
    out.append("- No aparece como O: ninguna arista de remisión tiene provenance `ext::3.18.1.2`.")
out.append(f"- Aristas de remisión cuyo campo `provenances` incluye `ext::3.18.1.2`: {len(o2_multi)}; "
           f"su campo `provenance` es: {sorted({fmt(O_de(e)) for e in o2_multi})}; "
           f"sus destinos: {sorted({e['properties']['destino'] for e in o2_multi})}")
for e in o2_multi:
    s = N[e["source"]]
    out.append(f"  - nodo origen [{s['type']}] «{s['label']}» con procedencias "
               + ", ".join(f"`{p.get('to')}::{p.get('punto')}`" for p in s["provenances"])
               + f" → destino `{e['properties']['destino']}`")
out.append("- Texto propio de `ext::3.18.1.2` en E0:")
bloque_texto(out, REF_O2)
out.append("")

(OUT / "v2_candidatos.md").write_text("\n".join(out) + "\n")

res = {
    "sha_kg": sha_kg, "sha_ev2": sha_ev2, "sha_e0": sha_e0,
    "paso1": {
        "aristas_remision": len(R), "con_provenance_to_punto": len(con_prov), "sin_provenance_to_punto": len(sin_prov),
        "destino_texto_ordenado": len(dest_to), "destino_seccion": len(dest_sec), "destino_otro_no_numerico": len(dest_otro),
        "validas": len(validas),
        "destino_seccion_por_to_origen": dict(Counter(O_de(e)[0] for e in dest_sec)),
        "destino_texto_ordenado_O": sorted({fmt(O_de(e)) for e in dest_to}),
        "aristas_validas_con_provenances_multiples": n_aristas_multi,
        "puntos_solo_en_provenances_no_en_provenance": sorted(fmt(q) for q in ocultos if q not in origenes_todas),
    },
    "embudo": emb, "embudo_por_to": emb_to,
    "diagnosticos": {
        "O_sin_texto_E0_caen_en_c4": sin_texto,
        "cambio_en_candidatos_si_c5_usa_solo_aristas_validas": dif_c5,
        "secciones_con_fragmento_punto_terminal": secciones_con_terminal,
        "O_seccion_en_c1": sorted(fmt(o) for o in pares if re.fullmatch(r"S\d+", o[1])),
    },
    "candidatos": tabla,
    "nuevos_vs_prev": [{"n": t["n"], "O": t["O"], "D": t["D"]} for t in nuevos],
    "prev_que_salen": salen,
    "pro": pro_tabla, "pro_conteo": pro_conteo,
    "referencia": {"D": [fmt(d) for d in ref_dso], "criterios": ref_c, "resultado": fallo.get(REF_O, "no es O"),
                   "ev2": [q for q, _ in ids_ref]},
    "ext_3_18_1_2": {"es_O": bool(o2_ds), "D": sorted(fmt(d) for d in (o2_ds or [])),
                     "aristas_con_provenances_que_lo_incluyen": len(o2_multi),
                     "provenance_de_esas_aristas": sorted({fmt(O_de(e)) for e in o2_multi})},
}
(OUT / "v2_resultado.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n")
print(json.dumps({k: res[k] for k in res if k not in ("candidatos", "pro")}, ensure_ascii=False, indent=1))
print("candidatos:", len(tabla))
