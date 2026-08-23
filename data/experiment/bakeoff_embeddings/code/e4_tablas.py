#!/usr/bin/env python3
"""Entregable 4: arma las tablas comparativas desde e3_resultados/*.json y
evalua el criterio de lectura declarado (mismo orden bajo las dos reglas)."""
import json, os

SP = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(SP, "e3_resultados")

FICHA = {  # licencia, params, ventana declarada, elegible
 "bm25":    ("—", "—", "—", "control lexico"),
 "qwen3":   ("Apache-2.0", "596M", "32.768", "si"),
 "granite": ("Apache-2.0", "312M", "32.768", "si"),
 "harrier": ("MIT", "596M", "32.768", "si"),
 "f2llm":   ("Apache-2.0", "596M", "40.960", "si"),
 "jina":    ("CC-BY-NC-4.0", "596M", "32.768", "NO ELEGIBLE (licencia)"),
}
ORDEN = ["bm25", "granite", "qwen3", "harrier", "f2llm", "jina"]
ELEGIBLES = ["bm25", "granite", "qwen3", "harrier", "f2llm"]

R = {}
for k in ORDEN:
    p = os.path.join(OUT, f"{k}.json")
    if os.path.exists(p):
        R[k] = json.load(open(p))
trunc = {f["modelo"]: f for f in json.load(open(os.path.join(SP, "e2_truncamiento.json")))}


def m(k, regla, var, at):
    return R[k]["metricas"][f"{regla}|{var}|@{at}"]["recall"]


def pc(x):
    return "—" if x is None else f"{100*x:.0f}%"


def tabla(regla):
    n = R[ORDEN[0]]["metricas"][f"{regla}|ambas|@1"]["n"]
    nl = R[ORDEN[0]]["metricas"][f"{regla}|literal|@1"]["n"]
    out = [f"### Regla {regla} — n = {n} casos ({nl} literal + {nl} anti-lexica)", "",
           "| modelo | lit@1 | lit@5 | lit@10 | anti@1 | anti@5 | anti@10 | brecha @1 | brecha @10 | ambas@1 |",
           "|---|---|---|---|---|---|---|---|---|---|"]
    for k in ORDEN:
        if k not in R: continue
        b1 = m(k, regla, "literal", 1) - m(k, regla, "antilexica", 1)
        b10 = m(k, regla, "literal", 10) - m(k, regla, "antilexica", 10)
        et = " *(no elegible)*" if k == "jina" else (" *(control)*" if k == "bm25" else "")
        out.append(f"| {k}{et} | {pc(m(k,regla,'literal',1))} | {pc(m(k,regla,'literal',5))} | "
                   f"{pc(m(k,regla,'literal',10))} | {pc(m(k,regla,'antilexica',1))} | "
                   f"{pc(m(k,regla,'antilexica',5))} | {pc(m(k,regla,'antilexica',10))} | "
                   f"{100*b1:+.0f} pp | {100*b10:+.0f} pp | {pc(m(k,regla,'ambas',1))} |")
    return "\n".join(out)


def orden_por(regla, var="ambas", at=1):
    ks = [k for k in ELEGIBLES if k in R]
    return sorted(ks, key=lambda k: (-m(k, regla, var, at), k))


def preorden(regla, var="ambas", at=1):
    ks = orden_por(regla, var, at)
    grupos, prev = [], None
    for k in ks:
        v = m(k, regla, var, at)
        if v == prev: grupos[-1].append(k)
        else: grupos.append([k]); prev = v
    return grupos


def pares_invertidos(r1, r2, var="ambas", at=1):
    ks = [k for k in ELEGIBLES if k in R]
    inv = []
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            a, b = ks[i], ks[j]
            d1 = m(a, r1, var, at) - m(b, r1, var, at)
            d2 = m(a, r2, var, at) - m(b, r2, var, at)
            if d1 * d2 < 0: inv.append((a, b, d1, d2))
    return inv


lineas = []
lineas.append(tabla("R2")); lineas.append("")
lineas.append(tabla("control")); lineas.append("")
lineas.append("### Truncamiento, tiempo de indexacion, licencia, ventana")
lineas.append("")
lineas.append("| modelo | licencia | params | ventana declarada | chunks truncados | % corpus | mayor chunk (tok de ESE tokenizador) | t. indexacion (s) | dim |")
lineas.append("|---|---|---|---|---|---|---|---|---|")
for k in ORDEN:
    if k not in R: continue
    lic, par, ven, el = FICHA[k]
    if k == "bm25":
        lineas.append(f"| bm25 *(control lexico)* | — | — | — | no aplica | — | — | {R[k]['t_indexacion_s']} | — |")
    else:
        t = trunc[k]
        lineas.append(f"| {k} | {lic} | {par} | {ven} | {t['chunks_truncados']} | {t['pct_corpus']}% | "
                      f"{t['mayor_chunk_tokens']} | {R[k]['t_indexacion_s']} | {R[k]['extra']['dim']} |")
lineas.append("")
lineas.append("### Determinismo (doble corrida del pipeline de consulta)")
lineas.append("")
lineas.append("| modelo | embeddings de consulta byte-identicos | rankings identicos |")
lineas.append("|---|---|---|")
for k in ORDEN:
    if k not in R or k == "bm25": continue
    d = R[k]["extra"]["determinismo"]
    lineas.append(f"| {k} | {'si' if d['embeddings_byte_identicos'] else 'NO'} | {'si' if d['rankings_identicos'] else 'NO'} |")
lineas.append("| bm25 | no aplica (sin modelo) | deterministico por construccion |")
lineas.append("")

lineas.append("### Criterio de lectura declarado ex ante")
lineas.append("")
for var in ("ambas", "literal", "antilexica"):
    o2 = preorden("R2", var); oc = preorden("control", var)
    inv = pares_invertidos("R2", "control", var)
    lineas.append(f"- **recall@1 {var}** — orden bajo R2: `{' > '.join('='.join(g) for g in o2)}`")
    lineas.append(f"  orden bajo control: `{' > '.join('='.join(g) for g in oc)}`")
    lineas.append(f"  parejas invertidas entre reglas: **{len(inv)}**" +
                  ("" if not inv else " → " + "; ".join(f"{a} vs {b} ({d1*100:+.0f} pp R2 / {d2*100:+.0f} pp control)" for a, b, d1, d2 in inv)))
lineas.append("")
txt = "\n".join(lineas)
open(os.path.join(SP, "e4_tablas.md"), "w").write(txt)
print(txt)
