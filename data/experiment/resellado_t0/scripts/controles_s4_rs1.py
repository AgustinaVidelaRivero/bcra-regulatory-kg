"""Re-sellado único de la tanda 0, §4 del mandato: tres controles que esperan el re-sellado, sobre los grafos nuevos. USD 0,
solo lee; escribe solo --out. Corre desde la raíz de una COPIA del repo.

  A. U-CONF-MATRIZ (docs/mandatos/UCONF_MATRIZ_lectura_confirmacion.md:35-38): las 60 aristas leídas (conf_matriz/c1/
     fichas_c1.jsonl, sorteadas en KG-Tanda0-Diez-r2b-sincola, e22fae1a) siguen en el grafo re-sellado con los mismos
     extremos (origen, predicado, destino). Se mira en los cuatro grafos nuevos; el que corresponde es el diez sin la cola.
  B. Laudo B2.4 (docs/laudo_B2.4_sujetos.md:25-28): la re-medición de las aristas de sujeto (aplica_a y ejecuta, sin las del
     esqueleto) de los puntos de los ocho patrones, con la consulta del control o de reext_t0/t3/controles_t3.py (la
     arista se ubica por su propia procedencia), más ext::7.9 para BKL-0015 (laudo, §3.1: «vale ext::7.9.6»). Sobre el
     diez sellado (a9631a64, el grafo del laudo), los de antes de O2 y de O2 (reproducidos) y el re-sellado; cada arista
     que sale o entra lleva el paso que la mueve.
  C. Condición 10 del checklist (como en U-SINCOLA-T0): la función c10 de sincola_t0/sc1/controles_sc1.py, copiada sin
     cambios, sobre los cuatro grafos nuevos y sus sellados.
Uso: python -I -B controles_s4_rs1.py --corridas <dir con preO2/ y o2/> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import unicodedata
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

ap = argparse.ArgumentParser()
ap.add_argument("--corridas", type=Path, required=True)
ap.add_argument("--out", type=Path, required=True)
a = ap.parse_args()
RAIZ = Path.cwd().resolve()
assert not (RAIZ / ".git").exists(), "corre sobre una copia"
REX = RAIZ / "data/experiment/reextraccion_v2"
T0 = REX / "corpus_tanda0"
SAL = T0 / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
GRAFOS = OrderedDict([
    ("diez", ("ens_diez_r2b", "ens_diez_r2b_rs1", "r2b_diez")),
    ("diez_sin_cola", ("ens_diez_r2b_sincola", "ens_diez_r2b_sincola_rs1", "r2b_sincola_diez")),
    ("desarrollo", ("ens_desarrollo_r2b", "ens_desarrollo_r2b_rs1", "r2b_desarrollo")),
    ("desarrollo_sin_cola", ("ens_desarrollo_r2b_sincola", "ens_desarrollo_r2b_sincola_rs1", "r2b_sincola_desarrollo")),
])


def leer(p):
    return json.loads(Path(p).read_text(encoding="utf-8"))


def jsonl(p) -> list:
    p = Path(p)
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def last_wins(p) -> dict:
    return {r["chunk_id"]: r for r in jsonl(p)}


def chunks_e0(p) -> list:
    d = leer(p)
    return d["chunks"] if isinstance(d, dict) else d


def provs(x: dict) -> list:
    return [p for p in [x.get("provenance")] + (x.get("provenances") or []) if p]


def chunks_de(x: dict) -> set:
    return {p.get("chunk_id") for p in provs(x) if p.get("chunk_id")}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "")
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return " ".join(re.sub(r"[^a-z0-9]+", " ", s).split())


def marca(x: dict) -> bool:
    return (x.get("properties") or {}).get("cola_humana") == "true"


def kg_de(d: Path) -> tuple[dict, dict, str]:
    b = (d / "kg.json").read_bytes()
    kg = json.loads(b)
    return kg, {n["id"]: n for n in kg["nodes"]}, hashlib.sha256(b).hexdigest()


res = OrderedDict([("unidad", "Re-sellado único de la tanda 0, §4 (controles_s4_rs1.py)")])
G = {}
for g, (sel, nue, cor) in GRAFOS.items():
    G[g] = {"sellado": kg_de(T0 / sel / "r2"), "nuevo": kg_de(T0 / nue / "r2"),
            "antes_de_O2": kg_de(a.corridas / "preO2" / cor / "r2"), "O2": kg_de(a.corridas / "o2" / cor / "r2")}
res["sha256"] = {g: {k: v[2] for k, v in x.items()} for g, x in G.items()}

# ---------------------------------------------------------------------------------------------- A. U-CONF-MATRIZ
fichas = jsonl(RAIZ / "data/experiment/conf_matriz/c1/fichas_c1.jsonl")
acta = leer(RAIZ / "data/experiment/conf_matriz/c1/acta_c1.json")
A = OrderedDict([("fichas", len(fichas)), ("grafo_del_sorteo", acta["grafo"]["nombre"]),
                 ("grafo_del_sorteo_sha256", acta["grafo"]["kg_sha256"]), ("por_grafo", OrderedDict())])
for g in GRAFOS:
    for k in ("sellado", "nuevo"):
        kg, idx, sha = G[g][k]
        aristas = {(e["source"], e["relation"], e["target"]) for e in kg["edges"]}
        faltan = []
        for f in fichas:
            t = (f["origen"]["id"], f["predicado"], f["destino"]["id"])
            if t not in aristas:
                mismo_par = sorted(r for s, r, d in aristas if s == t[0] and d == t[2])
                faltan.append({"ficha": f["ficha"], "origen_en_el_grafo": t[0] in idx, "destino_en_el_grafo": t[2] in idx,
                               "otras_relaciones_entre_los_mismos_extremos": mismo_par,
                               "unidad": f["unidad"]["chunk_id"]})
        A["por_grafo"][f"{g}|{k}"] = {"sha256": sha, "presentes": len(fichas) - len(faltan), "faltan": faltan}
A["el_que_corresponde"] = "diez_sin_cola|nuevo"
A["ok"] = not A["por_grafo"]["diez_sin_cola|nuevo"]["faltan"] and not A["por_grafo"]["diez_sin_cola|sellado"]["faltan"]
res["A_conf_matriz"] = A

# ---------------------------------------------------------------------------------------------- B. laudo B2.4
CASOS = OrderedDict([("BKL-0009 T1", ("cap", ("2.5",))), ("BKL-0010 T2", ("ext", ("14.5",))), ("BKL-0011 T3", ("ric", ("3.1",))),
                     ("BKL-0012 T4", ("ext", ("13.4",))), ("BKL-0013 T5", ("ext", ("14.5", "3.17", "3.18", "9.7"))),
                     ("BKL-0014 T6", ("ext", ("14.1",))), ("BKL-0015 T7", ("ext", ("3.17", "7.9"))), ("BKL-0016 T8", ("ext", ("3.18",)))])


def aristas_caso(kg: dict, to: str, pts: tuple) -> dict:
    es = [e for e in kg["edges"] if e["relation"] in ("aplica_a", "ejecuta") and e.get("rol_fuente") != "esqueleto"
          and any(p.get("to") == to and any(str(p.get("punto")) == q or str(p.get("punto")).startswith(q + ".") for q in pts)
                  for p in provs(e))]
    return {(e["source"], e["relation"], e["target"]): e for e in es}


B = OrderedDict([("grafo", "diez (el del laudo: a9631a64)"), ("casos", OrderedDict())])
pasos_kg = [("sellado", G["diez"]["sellado"][0]), ("antes_de_O2", G["diez"]["antes_de_O2"][0]),
            ("O2", G["diez"]["O2"][0]), ("nuevo", G["diez"]["nuevo"][0])]
nombre_paso = {("sellado", "antes_de_O2"): "R2-3", ("antes_de_O2", "O2"): "O2", ("O2", "nuevo"): "R0"}
movidas_total = 0
for caso, (to, pts) in CASOS.items():
    por = OrderedDict((k, aristas_caso(kg, to, pts)) for k, kg in pasos_kg)
    s, n = por["sellado"], por["nuevo"]
    mov = []
    for kk in sorted(set(s) ^ set(n)):
        pasos = [nombre_paso[(x, y)] for (x, _), (y, _) in zip(pasos_kg, pasos_kg[1:]) if (kk in por[x]) != (kk in por[y])]
        e = n.get(kk) or s.get(kk)
        mov.append({"arista": "|".join(kk), "cambio": "sale" if kk in s else "entra", "pasos": pasos,
                    "mencion": e.get("sujeto_mencion"), "chunks": sorted(chunks_de(e))})
    cambian_campos = sorted("|".join(kk) for kk in set(s) & set(n)
                            if {k: v for k, v in s[kk].items()} != {k: v for k, v in n[kk].items()})
    movidas_total += len(mov)
    B["casos"][caso] = OrderedDict([("to", to), ("puntos", list(pts)), ("aristas", {k: len(v) for k, v in por.items()}),
                                    ("por_sujeto_nuevo", dict(sorted(Counter(k[2] if k[1] == "aplica_a" else k[0]
                                                                             for k in n).items()))),
                                    ("salen_o_entran_del_sellado_al_nuevo", mov),
                                    ("siguen_con_otros_campos", cambian_campos)])
B["aristas_que_se_mueven_del_sellado_al_nuevo"] = movidas_total
res["B_laudo_B24"] = B

# ---------------------------------------------------------------------------------------------- C. condición 10
CHUNKS = {}
for f in sorted(E0.glob("chunks_*.json")):
    for c in chunks_e0(f):
        CHUNKS[c["id"]] = c
for p in sorted(SAL.glob("*/particiones_por_corte.json")):
    for v in leer(p).values():
        for c in v["partes"]:
            CHUNKS[c["id"]] = c
TOS_DIEZ = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FIN = {to: last_wins(SAL / to / "finales.jsonl") for to in TOS_DIEZ}
cola_set = {cid for to in TOS_DIEZ for cid, r in FIN[to].items() if str(r.get("estado")).startswith("cola_humana")}
FR2 = {to: last_wins(SAL / to / f"extracciones_finales_r2_{to}.jsonl") for to in TOS_DIEZ}
fin_val = {cid: r["validacion"] for to in TOS_DIEZ for cid, r in FR2[to].items() if r.get("validacion")}


def c10(kg: dict, idx: dict) -> OrderedDict:
    def anclado(n, to, punto, exacto=True):
        return any(p.get("to") == to and (str(p.get("punto")) == punto if exacto else
                                          (str(p.get("punto")) == punto or str(p.get("punto")).startswith(punto + ".")))
                   for p in provs(n))
    n5111 = [n for n in kg["nodes"] if "cla::5.1.1.1" in chunks_de(n)]
    intro = [n for n in kg["nodes"] if "cla::5.1.1::intro" in chunks_de(n)]
    hijos_chunks = sorted(cid for cid in CHUNKS if cid.startswith("cla::5.1.1.") )
    hijos = defaultdict(list)
    for n in kg["nodes"]:
        for p in provs(n):
            cid = p.get("chunk_id") or ""
            if cid.startswith("cla::5.1.1.") and n["type"] not in ("TextoOrdenado", "Sujeto"):
                hijos[cid].append((n["id"], "5.1.1" in (p.get("ancestros") or []), marca(n)))
    exc = [n for n in n5111 if n["type"] == "Excepcion"]
    rb = [e for e in kg["edges"] if e["relation"] == "remite_a" and anclado(idx[e["source"]], "cla", "5.1.1.1")
          and anclado(idx[e["target"]], "cla", "3.7")]
    rb_sub = [e for e in kg["edges"] if e["relation"] == "remite_a" and anclado(idx[e["source"]], "cla", "5.1.1.1")
              and anclado(idx[e["target"]], "cla", "3.7", exacto=False)]
    return OrderedDict([
        ("i_excepcion_de_5_1_1_1", [{"id": n["id"], "label": n.get("label"), "cola": marca(n), "chunks": sorted(chunks_de(n)),
                                     "en_la_cola": bool(chunks_de(n) & cola_set)} for n in exc]),
        ("i_ok", len(exc) >= 1 and not any(marca(n) or (chunks_de(n) & cola_set) for n in exc)),
        ("ii_nodos_del_intro", [{"id": n["id"], "type": n["type"], "cola": marca(n)} for n in intro if n["type"] not in ("TextoOrdenado", "Sujeto")]),
        ("ii_chunks_hijos_de_5_1_1_en_e0", hijos_chunks),
        ("ii_alcanzados_por_hijo", OrderedDict((cid, {"nodos": len(v), "todos_con_ancestro_5_1_1": all(x[1] for x in v),
                                                      "con_marca": sum(1 for x in v if x[2]), "ids": sorted({x[0] for x in v})})
                                               for cid, v in sorted(hijos.items()))),
        ("ii_ok", all(cid in hijos and hijos[cid] for cid in ("cla::5.1.1.1", "cla::5.1.1.2"))
                  and all(all(x[1] for x in v) for v in hijos.values())),
        ("iii_intro_conserva_definicion_de_alcance", any(n["type"] == "Definicion" and "alcance" in norm(n.get("label")) for n in intro)),
        ("iii_tipos_en_5_1_1_1", dict(sorted(Counter(n["type"] for n in n5111).items()))),
        ("iv_x17_remite_a_5_1_1_1_a_3_7", len(rb)), ("iv_a_3_7_o_debajo", len(rb_sub)),
        ("iv_aristas", [{"source": e["source"], "target": e["target"], "chunks": sorted(chunks_de(e))} for e in rb_sub]),
        ("iv_ok", len(rb) >= 1),
        ("relaciones_rechazadas_en_5_1_1_1", [r for r in (fin_val.get("cla::5.1.1.1") or {}).get("rechazos", []) if r.get("nivel") == "relacion"])])


C = OrderedDict()
for g in GRAFOS:
    cn, cs = c10(G[g]["nuevo"][0], G[g]["nuevo"][1]), c10(G[g]["sellado"][0], G[g]["sellado"][1])
    C[g] = OrderedDict([("nuevo", cn),
                        ("resumen", {k: {"nuevo": cn[k], "sellado": cs[k]} for k in
                                     ("i_ok", "ii_ok", "iii_intro_conserva_definicion_de_alcance", "iii_tipos_en_5_1_1_1",
                                      "iv_x17_remite_a_5_1_1_1_a_3_7", "iv_a_3_7_o_debajo", "iv_ok")}),
                        ("alcanzados_por_hijo_igual_al_sellado", cn["ii_alcanzados_por_hijo"] == cs["ii_alcanzados_por_hijo"]),
                        ("excepcion_igual_al_sellado", cn["i_excepcion_de_5_1_1_1"] == cs["i_excepcion_de_5_1_1_1"]),
                        ("aristas_x17_iguales_al_sellado", cn["iv_aristas"] == cs["iv_aristas"])])
res["C_condicion_10"] = C
a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("A:", {k: (v["presentes"], [x["ficha"] for x in v["faltan"]]) for k, v in A["por_grafo"].items()}, "ok", A["ok"])
print("B: movidas", movidas_total, {c: (v["aristas"], [(m["cambio"], m["pasos"]) for m in v["salen_o_entran_del_sellado_al_nuevo"]],
                                         len(v["siguen_con_otros_campos"])) for c, v in B["casos"].items()})
print("C:", {g: {k: v["nuevo"] for k, v in x["resumen"].items()} for g, x in C.items()})
print("C igual al sellado:", {g: (x["alcanzados_por_hijo_igual_al_sellado"], x["excepcion_igual_al_sellado"], x["aristas_x17_iguales_al_sellado"]) for g, x in C.items()})
