"""
U-INV-CANDIDATOS — candidatos a ejemplo conductor: remisiones entre puntos del
grafo r1. Solo lectura del repositorio; salidas únicamente en /tmp/u_inv_candidatos/.

Definiciones operativas (ver reporte):
  - Arista de remisión resuelta: relation == "referencia" y
    rol_fuente == "referencia_cruzada" (r1_referencias.py:33-36, 231-236;
    una remisión sin destino resoluble no genera arista, r1_referencias.py:6-7).
  - Punto = par (to, punto) de cada entrada de `provenances` de un nodo; un
    nodo con varias procedencias cuenta para cada una.
  - D(O) = conjunto de TODOS los puntos alcanzados por aristas de remisión
    resuelta desde nodos con procedencia en O (un par por punto origen).
  - Texto propio de un punto = campo `texto` de los fragmentos E0 cuya
    `unidad` es el punto (en el orden del archivo); palabras = len(texto.split())
    sumado sobre esos fragmentos.
  - Ancestro/descendiente en la numeración: prefijo propio por componentes
    separados por '.', con "S<n>" equivalente al componente "<n>"; solo dentro
    del mismo Texto Ordenado.
Sin APIs, sin Neo4j, sin índices de búsqueda.
"""
import hashlib
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg")
KG = REPO / "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_enm01"
EV2 = REPO / "data/experiment/exploracion/ev2_fidelidad/preguntas_ev2_fidelidad.json"
OUT = Path("/tmp/u_inv_candidatos")
TOS = ("cap", "cla", "ext", "pro", "ric")
MAX_O, MAX_D = 80, 120
REF_O = ("ext", "3.17.1.4")
REF_D = [("ext", "3.4.1"), ("ext", "3.4.2"), ("ext", "3.4.3")]


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def comps(punto):
    if re.fullmatch(r"S\d+", punto):
        return [punto[1:]]
    return punto.split(".")


def es_ancestro(a, b):
    """a es ancestro propio de b en la numeración."""
    ca, cb = comps(a), comps(b)
    return len(ca) < len(cb) and cb[: len(ca)] == ca


def clave_orden(p):
    to, punto = p
    ks = []
    for c in comps(punto):
        ks.append((0, int(c), "") if c.isdigit() else (1, 0, c))
    return (TOS.index(to) if to in TOS else 99, ks)


def fmt(p):
    return f"{p[0]}::{p[1]}"


# ---------- carga ----------
sha_kg = sha(KG)
assert sha_kg.startswith("0226e947"), sha_kg
sha_ev2 = sha(EV2)
assert sha_ev2.startswith("1d587336"), sha_ev2
kg = json.loads(KG.read_text())
N = {n["id"]: n for n in kg["nodes"]}

frag = defaultdict(list)          # (to, unidad) -> [(id, texto)]
tipo_frag = {}                    # id -> "tipo[, rol_bloque X]"
sha_e0 = {}
for to in TOS:
    f = E0 / f"chunks_{to}.json"
    sha_e0[f.name] = sha(f)
    for x in json.loads(f.read_text()):
        frag[(x["to"], x["unidad"])].append((x["id"], x["texto"]))
        tipo_frag[x["id"]] = f"{x['tipo']}" + (f", rol_bloque {x['rol_bloque']}" if x.get("rol_bloque") else "")


def palabras(p):
    fs = frag.get(p)
    if not fs:
        return None
    return sum(len(t.split()) for _, t in fs)


ev2 = json.loads(EV2.read_text())["preguntas"]


def ev2_ids(puntos):
    """ids EV2 cuyo gold.ancla o criterios (criterio / cita_textual) citan
    alguno de los puntos. Ancla: igualdad exacta 'to:punto'. Criterios:
    el número de punto como token (sin dígito ni '.dígito' adyacente), solo en
    preguntas del mismo Texto Ordenado."""
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


# ---------- aristas de remisión ----------
refs_todas = [e for e in kg["edges"] if e["relation"] == "referencia"]
R = [e for e in refs_todas if e.get("rol_fuente") == "referencia_cruzada"]
otras_ref = [e for e in refs_todas if e.get("rol_fuente") != "referencia_cruzada"]

por_to_origen = defaultdict(int)
por_to_destino = defaultdict(int)
cross = 0
via = defaultdict(int)
for e in R:
    to_o = e["provenance"]["to"]
    to_d = e["properties"]["destino"].split("::")[0]
    por_to_origen[to_o] += 1
    por_to_destino[to_d] += 1
    cross += to_o != to_d
    via[e["properties"]["via"]] += 1

D = defaultdict(set)                     # O -> set(d)
testigos = defaultdict(list)             # (O, d) -> [edge idx]
origenes = set()                         # todo punto con procedencia de un nodo fuente de R
for i, e in enumerate(R):
    S = {(p.get("to"), p.get("punto")) for p in N[e["source"]]["provenances"]}
    T = {(p.get("to"), p.get("punto")) for p in N[e["target"]]["provenances"]}
    origenes |= S
    for o in S:
        for d in T:
            D[o].add(d)
            testigos[(o, d)].append(i)

# ---------- embudo ----------
emb = {}
c1 = {o: frozenset(ds) for o, ds in D.items() if ds}
emb["1_arista_resuelta"] = len(c1)
c2 = {o: ds for o, ds in c1.items() if 1 <= len(ds) <= 3}
emb["2_tam_D_1a3"] = len(c2)


def crit3(o, ds):
    return all(not (d[0] == o[0] and (es_ancestro(d[1], o[1]) or es_ancestro(o[1], d[1]))) for d in ds)


c3 = {o: ds for o, ds in c2.items() if crit3(o, ds)}
emb["3_sin_ancestro_descendiente"] = len(c3)
sin_texto = []


def crit4(o, ds):
    wo = palabras(o)
    wd = [palabras(d) for d in ds]
    if wo is None or any(w is None for w in wd):
        sin_texto.append(fmt(o))
        return False
    return wo <= MAX_O and all(w <= MAX_D for w in wd)


c4 = {o: ds for o, ds in c3.items() if crit4(o, ds)}
emb["4_palabras_O80_D120"] = len(c4)


def crit5(ds):
    return not (set(ds) & origenes)


c5 = {o: ds for o, ds in c4.items() if crit5(ds)}
emb["5_D_sin_remision_saliente"] = len(c5)

# diagnósticos del embudo
diag = {
    "pares_con_O_en_D_tras_c1": sum(1 for o, ds in c1.items() if o in ds),
    "pares_con_O_en_D_tras_c4": sum(1 for o, ds in c4.items() if o in ds),
    "O_con_arista_via_texto_ordenado": sorted(
        {fmt((p.get("to"), p.get("punto"))) for e in R if e["properties"]["via"] == "texto_ordenado"
         for p in N[e["source"]]["provenances"]}),
    "O_sin_texto_E0_en_c4": sorted(set(sin_texto)),
    "puntos_origen_con_to_o_punto_nulo": sorted(fmt(o) for o in c1 if None in o),
}

# chequeo cruzado de la numeración contra el campo `ancestros` del grafo
anc = {}
for n in kg["nodes"]:
    for p in n["provenances"]:
        if p.get("to") and p.get("punto") and "ancestros" in p:
            anc[(p["to"], p["punto"])] = set(p["ancestros"])
discrepa = []
for o, ds in c2.items():
    for d in ds:
        if d[0] != o[0]:
            continue
        num = es_ancestro(d[1], o[1]) or es_ancestro(o[1], d[1])
        if o in anc and d in anc:
            grafo = d[1] in anc[o] or o[1] in anc[d]
            if num != grafo:
                discrepa.append((fmt(o), fmt(d), num, grafo))
diag["discrepancias_numeracion_vs_ancestros_en_c2"] = discrepa


# ---------- ficha ----------
def ficha(o, ds, ref=False):
    lin = []
    to = o[0]
    lin.append(f"- Texto Ordenado de O: `{to}`")
    wo = palabras(o)
    lin.append(f"- O = `{fmt(o)}` — {wo} palabras")
    for fid, t in frag.get(o, []):
        lin.append(f"  - fragmento E0 `{fid}` ({tipo_frag[fid]}; campo `texto`):")
        lin.append("")
        lin.append("````text")
        lin.append(t)
        lin.append("````")
        lin.append("")
    if not frag.get(o):
        lin.append("  - (sin fragmento E0 con esa unidad)")
    for d in sorted(ds, key=clave_orden):
        mismo = "mismo Texto Ordenado que O" if d[0] == to else f"otro Texto Ordenado (`{d[0]}`)"
        lin.append(f"- d = `{fmt(d)}` — {palabras(d)} palabras — {mismo}")
        for fid, t in frag.get(d, []):
            lin.append(f"  - fragmento E0 `{fid}` ({tipo_frag[fid]}; campo `texto`):")
            lin.append("")
            lin.append("````text")
            lin.append(t)
            lin.append("````")
            lin.append("")
        if not frag.get(d):
            lin.append("  - (sin fragmento E0 con esa unidad)")
        idx = testigos.get((o, d), [])
        if idx and all(R[i]["properties"]["destino"] != fmt(d) for i in idx):
            lin.append("  - d entra a D solo por procedencia múltiple del nodo destino "
                       "(ninguna arista O → d tiene `destino` = d)")
        lin.append(f"  - aristas de remisión resuelta O → d: {len(idx)}")
        for i in idx:
            e = R[i]
            s, t = N[e["source"]], N[e["target"]]
            extra = ""
            if len(s["provenances"]) > 1:
                extra += "; procedencias del nodo origen: " + ", ".join(
                    f"`{p.get('to')}::{p.get('punto')}`" for p in s["provenances"])
            if len(t["provenances"]) > 1:
                extra += "; procedencias del nodo destino: " + ", ".join(
                    f"`{p.get('to')}::{p.get('punto')}`" for p in t["provenances"])
            lin.append(f"    - [{s['type']}] «{s['label']}» → [{t['type']}] «{t['label']}» "
                       f"(destino `{e['properties']['destino']}`; evidencia «{e['properties']['evidencia']}»{extra})")
    ids = ev2_ids([o] + sorted(ds, key=clave_orden))
    if ids:
        lin.append("- Preguntas EV2 que citan O o algún d: "
                   + "; ".join(f"`{q}` ({', '.join(m)})" for q, m in ids))
    else:
        lin.append("- Preguntas EV2 que citan O o algún d: ninguna")
    return lin, ids


out = []
out.append("# U-INV-CANDIDATOS — candidatos (O, D) de remisión entre puntos, grafo r1")
out.append("")
out.append(f"- Grafo: `{KG.relative_to(REPO)}` sha256 `{sha_kg}`")
out.append(f"- EV2: `{EV2.relative_to(REPO)}` sha256 `{sha_ev2}`")
for k, v in sha_e0.items():
    out.append(f"- E0: `{(E0 / k).relative_to(REPO)}` sha256 `{v}`")
out.append(f"- Arista de remisión resuelta: `referencia` con `rol_fuente = referencia_cruzada` ({len(R)} aristas)")
out.append("- Embudo: " + " → ".join(f"{k}: {v}" for k, v in emb.items()))
out.append("")
out.append(f"## Candidatos que pasan los cinco criterios ({len(c5)})")
out.append("")
tabla = []
orden = sorted(c5, key=clave_orden)
for n_c, o in enumerate(orden, 1):
    ds = c5[o]
    out.append(f"### C{n_c:02d} — `{fmt(o)}` → {{{', '.join(fmt(d) for d in sorted(ds, key=clave_orden))}}}")
    out.append("")
    lin, ids = ficha(o, ds)
    out.extend(lin)
    out.append("")
    tabla.append({
        "n": n_c, "to": o[0], "O": fmt(o), "D": [fmt(d) for d in sorted(ds, key=clave_orden)],
        "palabras_O": palabras(o), "palabras_D": [palabras(d) for d in sorted(ds, key=clave_orden)],
        "mismo_to": ["sí" if d[0] == o[0] else "no" for d in sorted(ds, key=clave_orden)],
        "ev2": [q for q, _ in ids],
        "fragmentos_O": [fid for fid, _ in frag.get(o, [])],
        "fragmentos_D": {fmt(d): [fid for fid, _ in frag.get(d, [])] for d in ds},
        "tipos_fragmento": {fid: tipo_frag[fid] for q in [o, *ds] for fid, _ in frag.get(q, [])},
        "d_solo_por_multiprocedencia": [fmt(d) for d in sorted(ds, key=clave_orden)
                                        if all(R[i]["properties"]["destino"] != fmt(d) for i in testigos[(o, d)])],
        "O_solo_por_procedencia_no_primaria": all(
            (R[i]["provenance"].get("to"), R[i]["provenance"].get("punto")) != o
            for d in ds for i in testigos[(o, d)]),
    })

# ---------- referencia ----------
out.append("---")
out.append("")
out.append("## REFERENCIA (no es candidato salvo que figure arriba): `ext::3.17.1.4` → {ext::3.4.1, ext::3.4.2, ext::3.4.3}")
out.append("")
ref_ds = frozenset(REF_D)
r1_ok = all(testigos.get((REF_O, d)) for d in REF_D)
r2_ok = 1 <= len(ref_ds) <= 3
r3_ok = crit3(REF_O, ref_ds)
wo = palabras(REF_O)
wds = {fmt(d): palabras(d) for d in REF_D}
r4_ok = wo is not None and wo <= MAX_O and all(w is not None and w <= MAX_D for w in wds.values())
inter5 = sorted(fmt(d) for d in set(REF_D) & origenes)
r5_ok = not inter5
ref_eval = {
    "1": (r1_ok, {fmt(d): len(testigos.get((REF_O, d), [])) for d in REF_D}),
    "2": (r2_ok, len(ref_ds)),
    "3": (r3_ok, None),
    "4": (r4_ok, {"O": wo, **wds}),
    "5": (r5_ok, {"puntos_de_D_con_remision_saliente": inter5}),
}
out.append("- Criterios con el D fijado por el mandato:")
out.append(f"  - 1 (arista resuelta O→cada d): {'cumple' if r1_ok else 'NO cumple'} — aristas por d: {ref_eval['1'][1]}")
out.append(f"  - 2 (|D| entre 1 y 3): {'cumple' if r2_ok else 'NO cumple'} — |D| = {len(ref_ds)}")
out.append(f"  - 3 (sin ancestro/descendiente en el mismo TO): {'cumple' if r3_ok else 'NO cumple'}")
out.append(f"  - 4 (O ≤ 80, cada d ≤ 120 palabras): {'cumple' if r4_ok else 'NO cumple'} — {ref_eval['4'][1]}")
out.append(f"  - 5 (ningún d con remisión saliente): {'cumple' if r5_ok else 'NO cumple'} — puntos de D con remisión saliente: {inter5}")
real = sorted(D.get(REF_O, set()), key=clave_orden)
out.append(f"- D(O) completo según el grafo (todos los puntos alcanzados desde `{fmt(REF_O)}`): "
           f"{[fmt(d) for d in real]} ({len(real)} puntos)")
for d in real:
    if d in ref_ds:
        continue
    out.append(f"  - `{fmt(d)}` (fuera del D fijado) — {palabras(d)} palabras; aristas O → d:")
    for i in testigos[(REF_O, d)]:
        e = R[i]
        s_, t_ = N[e["source"]], N[e["target"]]
        out.append(f"    - [{s_['type']}] «{s_['label']}» → [{t_['type']}] «{t_['label']}» "
                   f"(destino `{e['properties']['destino']}`; procedencias del nodo destino: "
                   + ", ".join(f"`{p.get('to')}::{p.get('punto')}`" for p in t_["provenances"]) + ")")
out.append(f"- Con D = D(O) completo ({len(real)} puntos) el par no pasa el criterio 2; "
           f"por eso no figura entre los candidatos.")
anc_ev2 = [q["id"] for q in ev2 if any(a.startswith("ext:") and es_ancestro(a.split(":", 1)[1], REF_O[1])
                                         for a in q["gold"]["ancla"])]
out.append(f"- Nota: preguntas EV2 cuyo ancla es ancestro de O en la numeración (no cuenta como cita exacta): {anc_ev2}")
out.append("")
lin, ids_ref = ficha(REF_O, ref_ds, ref=True)
out.extend(lin)
out.append("")

(OUT / "candidatos.md").write_text("\n".join(out) + "\n")

res = {
    "sha_kg": sha_kg, "sha_ev2": sha_ev2, "sha_e0": sha_e0,
    "aristas_referencia_total": len(refs_todas),
    "aristas_remision_resuelta": len(R),
    "otras_referencia": {
        "n": len(otras_ref),
        "tipos_fuente_destino": sorted({(N[e["source"]]["type"], N[e["target"]]["type"]) for e in otras_ref}),
        "con_estado_e3": sum(1 for e in otras_ref if "estado_e3" in e.get("properties", {})),
    },
    "por_to_origen": dict(por_to_origen), "por_to_destino": dict(por_to_destino),
    "cross_to": cross, "via": dict(via),
    "embudo": emb, "diagnosticos": diag,
    "candidatos": tabla,
    "referencia": {k: [v[0], v[1]] for k, v in ref_eval.items()},
    "referencia_D_real": [fmt(d) for d in real],
    "referencia_ev2": [q for q, _ in ids_ref],
    "referencia_ev2_ancla_ancestro": anc_ev2,
}
(OUT / "resultado.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n")
print(json.dumps({k: res[k] for k in res if k != "candidatos"}, ensure_ascii=False, indent=1))
print("candidatos:", len(tabla))
