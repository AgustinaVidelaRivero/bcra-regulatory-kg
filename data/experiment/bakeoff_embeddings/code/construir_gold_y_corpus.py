#!/usr/bin/env python3
"""U-A2.0b-bakeoff, entregables 2-4: construye el corpus de pasajes y los
conjuntos gold bajo las dos reglas declaradas en reglas_puntuacion_declaradas.md.
Solo lectura sobre el repo. Determinístico.
"""
import json, os, hashlib, collections

REPO = "/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg"
SP = os.path.dirname(os.path.abspath(__file__))
TOS = ["cap", "cla", "ext", "pro", "ric"]
E0 = os.path.join(REPO, "data/experiment/reextraccion_v2/e0_chunking/salida_enm01")
PARES = os.path.join(REPO, "data/experiment/ablacion_retrieval/pares/pares_v3.json")
CORTE_AMBIGUO = 10


def sha_file(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


# ---------- corpus de pasajes ----------
# COMPOSICION DECLARADA: propio + herencia, en la forma exacta que E0 sella
# como "completo": "\n".join([textos de herencia] + [texto propio]).
# Verificado: reproduce chars_completo y sha256_completo de los 1763 chunks.
chunks = []
for to in TOS:
    chunks.extend(json.load(open(os.path.join(E0, f"chunks_{to}.json"))))
chunks.sort(key=lambda c: c["id"])          # orden canonico, determinista

pasajes = []
for c in chunks:
    txt = "\n".join([h["texto"] for h in c["herencia"]] + [c["texto"]])
    assert hashlib.sha256(txt.encode()).hexdigest() == c["sha256_completo"], c["id"]
    pasajes.append({"id": c["id"], "to": c["to"], "unidad": c["unidad"],
                    "tipo": c["tipo"], "texto": txt, "chars": len(txt)})
assert len(pasajes) == 1763
por_to = collections.defaultdict(list)
tipo_de = {}
for c in chunks:
    por_to[c["to"]].append(c)
    tipo_de[c["id"]] = c["tipo"]

# ---------- gold ----------
pares = json.load(open(PARES))["pares"]


def exacta(to, u):
    return sorted(c["id"] for c in por_to[to] if c["unidad"] == u)


def desc(to, u):
    return sorted(c["id"] for c in por_to[to] if c["unidad"].startswith(u + "."))


def gold_R2(to, u):
    return sorted(set(exacta(to, u)) | set(desc(to, u)))


def gold_R1(to, u):
    e = exacta(to, u)
    return e if e else desc(to, u)


def ancla_bien_formada(to, u):
    e = exacta(to, u)
    if e:
        return not all(tipo_de[i] == "mini_chunk" for i in e)   # (i)+(ii)
    return len(desc(to, u)) > 0                                  # (iii)


casos = []
for p in pares:
    g2 = sorted({i for a in p["gold"]["anclas"] for i in gold_R2(a["to"], a["ancla"])})
    g1 = sorted({i for a in p["gold"]["anclas"] for i in gold_R1(a["to"], a["ancla"])})
    bf = all(ancla_bien_formada(a["to"], a["ancla"]) for a in p["gold"]["anclas"])
    en_control = bf and len(g2) <= CORTE_AMBIGUO
    if en_control:
        # verificacion declarada en la regla: sobre el control R1 == R2
        assert g1 == g2, f"control con R1!=R2 en {p['sample_id']}"
    for var in ("literal", "antilexica"):
        casos.append({"caso_id": f"{p['sample_id']}::{var}", "sample_id": p["sample_id"],
                      "estrato": p["estrato"], "variante": var, "consulta": p[var],
                      "gold": g2, "n_gold": len(g2), "en_control": en_control,
                      "anclas": [f"{a['to']}:{a['ancla']}" for a in p["gold"]["anclas"]]})
casos.sort(key=lambda c: c["caso_id"])
assert len(casos) == 100

n_ctrl = sum(1 for c in casos if c["en_control"])
tam2 = [c["n_gold"] for c in casos]
tam_ctrl = [c["n_gold"] for c in casos if c["en_control"]]


def dist(v):
    return dict(sorted(collections.Counter(v).items()))


meta = {
    "reglas_sha256": sha_file(os.path.join(SP, "reglas_puntuacion_declaradas.md")),
    "insumos": {"pares_v3.json": sha_file(PARES),
                **{f"chunks_{t}.json": sha_file(os.path.join(E0, f"chunks_{t}.json")) for t in TOS}},
    "composicion_pasaje": "herencia + propio, en la forma que E0 sella como 'completo'",
    "n_pasajes": len(pasajes),
    "sha256_corpus": hashlib.sha256(json.dumps(pasajes, ensure_ascii=False, sort_keys=True).encode()).hexdigest(),
    "casos": {"total": 100, "control": n_ctrl,
              "pares_control": n_ctrl // 2,
              "casos_control_literal": sum(1 for c in casos if c["en_control"] and c["variante"] == "literal")},
    "dist_n_gold_R2_casos": dist(tam2),
    "dist_n_gold_control_casos": dist(tam_ctrl),
    "mediana_n_gold_R2": sorted(tam2)[len(tam2) // 2],
    "mediana_n_gold_control": sorted(tam_ctrl)[len(tam_ctrl) // 2] if tam_ctrl else None,
    "max_n_gold_R2": max(tam2), "max_n_gold_control": max(tam_ctrl) if tam_ctrl else None,
}
json.dump(pasajes, open(os.path.join(SP, "corpus_pasajes.json"), "w"), ensure_ascii=False)
json.dump(casos, open(os.path.join(SP, "casos_gold.json"), "w"), ensure_ascii=False, indent=1)
json.dump(meta, open(os.path.join(SP, "meta_gold_corpus.json"), "w"), ensure_ascii=False, indent=1)

print(json.dumps(meta, ensure_ascii=False, indent=1))
print("\n== pares EN el control ==")
for p in pares:
    c = next(x for x in casos if x["sample_id"] == p["sample_id"])
    if c["en_control"]:
        print(f"  {p['sample_id']:8s} {p['estrato']:4s} |gold|={c['n_gold']:2d} anclas={c['anclas']}")
print("\n== pares FUERA del control, con motivo ==")
for p in pares:
    c = next(x for x in casos if x["sample_id"] == p["sample_id"])
    if not c["en_control"]:
        malf = [f"{a['to']}:{a['ancla']}" for a in p["gold"]["anclas"]
                if not ancla_bien_formada(a["to"], a["ancla"])]
        mot = []
        if malf: mot.append("ancla_mal_formada=" + ",".join(malf))
        if c["n_gold"] > CORTE_AMBIGUO: mot.append(f"ambiguo(|gold|={c['n_gold']})")
        print(f"  {p['sample_id']:8s} {p['estrato']:4s} |gold|={c['n_gold']:2d} {'; '.join(mot)}")
