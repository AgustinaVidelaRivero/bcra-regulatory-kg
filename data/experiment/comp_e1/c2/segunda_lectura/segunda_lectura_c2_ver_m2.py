"""Vista para M2: por omisión de T4 y código, solapamiento propio (independiente del material) entre el tramo omitido
y los tramos de entidades y omisiones. Uso: python3 ver_m2.py <unidad> [<unidad> ...]"""
import json
import re
import sys
import unicodedata

M = json.load(open("material.json", encoding="utf-8"))


def norm(s):
    s = unicodedata.normalize("NFKC", s or "")
    s = s.replace("“", '"').replace("”", '"').replace("«", '"').replace("»", '"').replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().lower()


def toks(s):
    return re.findall(r"\w+", norm(s))


def segs(tramo):
    return [p.strip(" .;:") for p in re.split(r"\[(?:…|\.\.\.)\]", tramo or "") if p.strip(" .;:")]


def cobertura(om, tramo):
    o = norm(om).strip(" .;:")
    t = norm(tramo)
    contiene = o in t or any(o in norm(sg) for sg in segs(tramo))
    contenido = any(norm(sg) in o for sg in segs(tramo) if len(norm(sg)) > 8)
    ot = toks(om)
    tt = set(toks(tramo))
    frac = sum(1 for w in ot if w in tt) / max(1, len(ot))
    return contiene, contenido, frac


def main():
    for u in sys.argv[1:]:
        x = M[u]
        print("#", u, "—", x["titulo"])
        print(x.get("cabecera", ""))
        for o in x["omisiones_t4"]:
            print(f"OMI {o['clave']} [{o['attrs']}] «{o['frase']}»")
            on = norm(o["frase"])[:60]
            for k, t in x["texto"]:
                if on[:40] and on[:40] in norm(t):
                    i = norm(t).find(on[:40])
                    print(f"  en [{k}]: …{t[max(0, i - 200): i + len(o['frase']) + 200]}…")
            for cod, c in x["codigos"].items():
                print(f"  == {cod} == material: {c['cand_omi'][o['clave']]}")
                for e in c["entidades"]:
                    cont, conten, frac = cobertura(o["frase"], e["tramo"])
                    trunc = " TRUNC" if (e["tramo"] or "").endswith("…") else ""
                    if cont or conten or frac >= 0.3 or trunc:
                        print(f"    {trunc} ENT {e['id']} {e['tipo']} «{e['label']}» [{e['tramo_nivel']}] contiene={cont} contenido_en={conten} tok={frac:.2f} | tramo «{e['tramo']}»")
                    elif norm(o["frase"])[:30] and norm(o["frase"])[:30] in norm(e["desc"]):
                        print(f"     (solo descr.) {e['id']} {e['tipo']} «{e['label']}»")
                for i, om in enumerate(c["omisiones"]):
                    cont, conten, frac = cobertura(o["frase"], om["tramo"])
                    print(f"     OMIS#{i} {om['cat']} [{om['nivel']}] contiene={cont} contenido_en={conten} tok={frac:.2f} | «{om['tramo'][:160]}» — {(om['nota'] or '')[:160]}")
                if not c["entidades"]:
                    print("     (sin entidades)")
        print()


main()
