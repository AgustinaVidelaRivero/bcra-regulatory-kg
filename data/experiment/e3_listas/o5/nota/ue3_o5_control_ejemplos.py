"""U-E3-LISTAS, O5: controles de los dos ejemplos del caso resuelto (sin API, solo lectura sobre una copia).
  1. Cada fragmento citado entre «» es verbatim (con los espacios y saltos normalizados) del texto de su unidad de
     origen: el bloque que abre la lista de ext::10.11.5 (intro del 10.11) y el texto propio de cla::6.5.5.8.
  2. Ningún fragmento citado ni ventana de 5 tokens de los dos ejemplos aparece en el fuente con bloque de las 20
     unidades de O3 (lista sellada), ni en sus omisiones declaradas.
  3. Las dos unidades de origen no están entre las 20 ni comparten con ellas el bloque que abre la lista.
Uso: python ue3_o5_control_ejemplos.py <copia> <lista_sellada_O3.json> <texto_nota.txt>"""
import json, re, sys
from pathlib import Path
C, LISTA, NOTA = (Path(x).resolve() for x in sys.argv[1:4])
REX = C / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador")); sys.path.insert(0, str(C / "data/experiment/pyd_r2/code"))
import comun_e3  # noqa: E402
import validador_r2 as V  # noqa: E402
norm = lambda t: " ".join((t or "").split())  # noqa: E731

def ventanas(t):
    k = V.norm_tokens(t or ""); return {tuple(k[i:i + 5]) for i in range(len(k) - 4)}

def chunk(cid):
    return {c["id"]: c for c in json.loads((REX / f"e0_chunking/salida_tanda0_r2b/chunks_{cid.split('::')[0]}.json").read_text(encoding="utf-8"))}[cid]

nota = NOTA.read_text(encoding="utf-8")
citas = re.findall(r"«([^»]*)»", nota)
partes = [norm(p) for c in citas for p in c.split("…") if norm(p)]
ej1, ej2 = chunk("ext::10.11.5"), chunk("cla::6.5.5.8")
f1 = norm("\n".join(ej1["herencia"][i]["texto"] for i in comun_e3.indices_bloque_lista(ej1)))
f2 = norm(ej2["texto"])
res = {"citas": citas, "fragmentos": {p: {"en_ext_10_11_bloque": p in f1, "en_cla_6_5_5_8_texto_propio": p in f2} for p in partes}}
lista = json.loads(LISTA.read_text(encoding="utf-8"))
veinte = [u["chunk_id"] for u in lista["unidades"]]
w_ej = set().union(*(ventanas(c) for c in citas))
choques = {}
for cid in veinte:
    ch = chunk(cid)
    fuente = norm(comun_e3.fuente_integro(ch, True))
    to = cid.split("::")[0]
    x = next(json.loads(l) for l in (REX / f"corpus_tanda0/salida_r2b/{to}/extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines()
             if json.loads(l)["chunk_id"] == cid)
    om = " ".join(x["validacion"].get("omisiones_no_prosa") or [])
    frag = [p for p in partes if p in fuente or p in norm(om)]
    vent = len(w_ej & (ventanas(fuente) | ventanas(om)))
    if frag or vent:
        choques[cid] = {"fragmentos": frag, "ventanas_compartidas": vent}
res["choques_con_las_20"] = choques
bloques = {(c.split("::")[0], chunk(c)["herencia"][comun_e3.indices_bloque_lista(chunk(c))[0]]["unidad_origen"])
           for c in veinte if comun_e3.indices_bloque_lista(chunk(c))}
res["origen_fuera_de_las_20"] = {c: c not in veinte for c in ("ext::10.11.5", "cla::6.5.5.8")}
res["bloque_de_origen_fuera_de_las_listas_de_las_20"] = {
    c: (c.split("::")[0], chunk(c)["herencia"][comun_e3.indices_bloque_lista(chunk(c))[0]]["unidad_origen"]) not in bloques
    for c in ("ext::10.11.5", "cla::6.5.5.8")}
print(json.dumps(res, ensure_ascii=False, indent=1))
