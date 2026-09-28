"""Punto 4: desglose de los rechazos firma_invalida de E1 (tanda 0, salida_dirigida) y
verificacion de que cada uno es revalidable desde el crudo conservado. Solo lectura."""
import json, glob, re, sys, collections, os
REPO = "/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg"
sys.path.insert(0, REPO + "/data/experiment/esq/code")
import prompt_congelado as pc  # noqa
BASE = REPO + "/data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida"
RE_DET = re.compile(r"^relations\[(\d+)\]: (\S+) --(\S+)--> (\S+)$")
filas = []
lineas = 0
for f in sorted(glob.glob(BASE + "/*/extracciones_e1.jsonl")):
    to = f.split("/")[-2]
    # finales: que registro entro al grafo por chunk
    finales = {}
    for ln in open(BASE + f"/{to}/extracciones_finales_{to}.jsonl"):
        d = json.loads(ln); finales[d["chunk_id"]] = d.get("estado_e3")
    for nl, ln in enumerate(open(f), 1):
        lineas += 1
        d = json.loads(ln)
        crudo = d.get("tool_input_crudo")
        val = d.get("validacion") or {}
        for r in val.get("rechazos", []):
            if r["motivo"] != "firma_invalida":
                continue
            m = RE_DET.match(r["detalle"])
            i, st, p, tt = int(m.group(1)), m.group(2), m.group(3), m.group(4)
            chk = {"crudo_presente": isinstance(crudo, dict)}
            rel = None
            if chk["crudo_presente"]:
                rels = crudo.get("relations") or []
                rel = rels[i] if i < len(rels) else None
                chk["relacion_i_en_crudo"] = rel is not None
                chk["elemento_igual_crudo"] = rel == r["elemento"]
                ents = {e.get("local_id"): e.get("type") for e in (crudo.get("entities") or []) if isinstance(e, dict)}
                if p in pc.SUJETO_PREDICATES:
                    ext = rel.get("source") if p == "aplica_a" else rel.get("target")
                    tt_c = ents.get(ext)
                    s_c, t_c = (tt_c, "Sujeto") if p == "aplica_a" else ("Sujeto", tt_c)
                else:
                    s_c, t_c = ents.get(rel.get("source")), ents.get(rel.get("target"))
                chk["tipos_resueltos_desde_crudo"] = (s_c, t_c) == (st, tt)
                chk["firma_congelada_recomputada_invalida"] = not pc.firma_valida(s_c, p, t_c)
            filas.append({"to": to, "linea": nl, "chunk_id": d["chunk_id"], "idx": i,
                          "origen": st, "predicado": p, "destino": tt,
                          "estado_e3_final": finales.get(d["chunk_id"]), **chk})
tot = len(filas)
por_par = collections.Counter((x["origen"], x["predicado"], x["destino"]) for x in filas)
por_to = collections.Counter(x["to"] for x in filas)
ok = collections.Counter()
for x in filas:
    for k in ("crudo_presente", "relacion_i_en_crudo", "elemento_igual_crudo", "tipos_resueltos_desde_crudo", "firma_congelada_recomputada_invalida"):
        ok[k] += bool(x.get(k))
por_estado = collections.Counter(x["estado_e3_final"] for x in filas)
# chunks repetidos (re-extraccion dirigida)
rep = collections.Counter((x["to"], x["chunk_id"]) for x in filas)
res = {"lineas_e1": lineas, "rechazos_firma_invalida": tot,
       "por_par": [{"origen": a, "predicado": b, "destino": c, "n": n} for (a, b, c), n in por_par.most_common()],
       "suma_por_par": sum(por_par.values()),
       "por_to": dict(por_to), "verificacion_crudo": dict(ok),
       "por_estado_e3_del_registro_final": dict(por_estado)}
json.dump(res, open("/tmp/u_audit_tipos/p4_resumen.json", "w"), ensure_ascii=False, indent=1)
json.dump(filas, open("/tmp/u_audit_tipos/p4_filas.json", "w"), ensure_ascii=False, indent=0)
print(json.dumps(res, ensure_ascii=False, indent=1))
