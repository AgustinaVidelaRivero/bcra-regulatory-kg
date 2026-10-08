"""U-E3-LISTAS, O5: busca en la tanda 0 r2b (los diez TOs, intento 0 de E1) los candidatos a los dos ejemplos del caso
resuelto, fuera de las 20 unidades de O3 y de los ítems que comparten con ellas el bloque que abre la lista. Sin API,
solo lectura sobre una copia.
  - Lado «no es faltante»: ítem cuyo bloque que abre la lista enuncia una norma con su salvedad (excep|salvo) y anuncia
    la lista; en las omisiones, un [meta_normativo] cuyo tramo comparte ventanas de 5 tokens con ese bloque y ninguna
    con el texto propio del ítem; el ítem tiene al menos una Condicion.
  - Lado «sí es faltante»: ítem con un [meta_normativo] cuyo tramo comparte ventanas con el texto propio del ítem y
    ninguna con el bloque que abre la lista, y trae un marcador de deber o facultad (podrá, deberá, …).
Para cada candidato, el veredicto de E3 en la verificación del intento 0 de la tanda 0 (veredictos.jsonl).
Uso: python ue3_o5_buscar_ejemplos.py <copia> <lista_sellada_O3.json> <salida.json>"""
import json, re, sys
from pathlib import Path
C, LISTA, SAL = (Path(x).resolve() for x in sys.argv[1:4])
REX = C / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador")); sys.path.insert(0, str(C / "data/experiment/pyd_r2/code"))
import comun_e3  # noqa: E402
import prompt_r2b as R  # noqa: E402
import validador_r2 as V  # noqa: E402
TOS = ["cap", "cla", "ctacte", "docvig", "ext", "lingob", "pagjub", "polcre", "pro", "ric"]
DEONT = re.compile(r"\b(podr[aá]n?|deber[aá]n?|no podr[aá]n?|tendr[aá]n? que|estar[aá]n? obligad|obligad[oa]s? a|corresponder[aá]|"
                   r"debe|deben|requerir[aá]n?)\b", re.I)
SALV = re.compile(r"excep|salvo|exceptu", re.I)

def ventanas(t):
    k = V.norm_tokens(t or ""); return {tuple(k[i:i + 5]) for i in range(len(k) - 4)}

lista = json.loads(LISTA.read_text(encoding="utf-8"))
veinte = {u["chunk_id"] for u in lista["unidades"]}
res = {"no_es_faltante": [], "si_es_faltante": [], "excluidos_por_hermanos": []}
bloques_veinte = set()
chunks_por_to = {}
for to in TOS:
    chunks_por_to[to] = {c["id"]: c for c in json.loads((REX / f"e0_chunking/salida_tanda0_r2b/chunks_{to}.json").read_text(encoding="utf-8"))}
for cid in veinte:
    ch = chunks_por_to[cid.split("::")[0]][cid]
    idx = comun_e3.indices_bloque_lista(ch)
    if idx:
        bloques_veinte.add((cid.split("::")[0], ch["herencia"][idx[0]]["unidad_origen"]))
for to in TOS:
    ver = {}
    for l in (REX / f"corpus_tanda0/salida_r2b/{to}/veredictos.jsonl").read_text(encoding="utf-8").splitlines():
        v = json.loads(l)
        if v["fase"] == "verificacion" and v["intento"] == 0:
            ver[v["chunk_id"]] = v
    for l in (REX / f"corpus_tanda0/salida_r2b/{to}/extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines():
        x = json.loads(l); cid = x["chunk_id"]; val = x.get("validacion") or {}
        ch = chunks_por_to[to].get(cid)
        if ch is None or not R.es_item(ch) or cid in veinte:
            continue
        idx = comun_e3.indices_bloque_lista(ch)
        if not idx:
            continue
        her = ch["herencia"]
        i0 = idx[0]
        if i0 > 0 and her[i0 - 1]["tipo"] == "encabezado" and her[i0 - 1]["unidad_origen"] == her[i0]["unidad_origen"]:
            idx = [i0 - 1] + list(idx)
        H = "\n".join(her[i]["texto"] for i in idx)
        bloque = (to, her[i0]["unidad_origen"])
        metas = [o for o in val.get("omisiones_no_prosa") or [] if isinstance(o, str) and o.startswith("[meta_normativo]")]
        if not metas:
            continue
        if bloque in bloques_veinte:
            res["excluidos_por_hermanos"].append(cid)
            continue
        wH, wP = ventanas(H), ventanas(ch["texto"])
        tipos = sorted({e["type"] for e in val.get("entidades") or []} - {"TextoOrdenado"})
        v0 = ver.get(cid) or {}
        fal = [{"tipo": f.get("tipo"), "severidad": f.get("severidad"), "bloqueante": f.get("bloqueante"),
                "cita": (f.get("cita_textual_del_fuente") or "")[:200], "nota": (f.get("nota") or "")[:300]}
               for f in v0.get("faltantes") or []]
        for o in metas:
            tramo, _, glosa = o[len("[meta_normativo] "):].partition(" — ")
            wt = ventanas(tramo)
            fila = {"chunk_id": cid, "bloque": f"[{her[i0]['tipo']} | punto {her[i0]['unidad_origen']}]", "encabezado": H,
                    "tramo": tramo, "glosa": glosa, "tipos": tipos, "texto_propio": ch["texto"][:600],
                    "e3_t0": {"es_completo_ok": v0.get("es_completo_ok"), "n_bloqueantes": v0.get("n_bloqueantes"), "faltantes": fal}}
            if wt & wH and not wt & wP and SALV.search(H) and "Condicion" in tipos:
                res["no_es_faltante"].append(fila)
            elif wt & wP and not wt & wH and DEONT.search(tramo):
                res["si_es_faltante"].append(fila)
res["conteo"] = {k: len(v) for k, v in res.items() if isinstance(v, list)}
SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(res["conteo"])
