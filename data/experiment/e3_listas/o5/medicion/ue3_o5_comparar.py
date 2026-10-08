"""U-E3-LISTAS, O5: compara el mensaje de E3 antes (HEAD) y después (código de O5), unidad por unidad, sobre los volcados
de ue3_o2_medicion.py, y estima los tokens y el costo agregados como O2 (razón marginal de E1, 3,06 caracteres por token,
UE3_LISTAS_O2_razon_tokens_e1.json; tarifa de entrada de E3, USD 2 por millón). Sin API; no escribe en la copia.
  - Cuenta, por universo, cuántos mensajes cambian; con la marca r2, separa ítems y no ítems.
  - Control byte a byte de lo que cambia: con el código de O5 arma el mensaje de cada ítem, le quita el párrafo nuevo
    («\\n» + NOTA_E3_ITEM_CASOS) y comprueba que da el sha256 del mensaje de HEAD.
  - El fuente y las citas no cambian en ninguna fila.
  - Llamadas por corrida del tamaño de la tanda 0: las 1.054 primeras verificaciones de ítems y, aparte, sumando las
    re-verificaciones de ítems de la tanda 0 (veredictos.jsonl, fase distinta de verificacion).
Uso: python ue3_o5_comparar.py <copia_o5> <antes.jsonl> <despues.jsonl> <razon_tokens.json> <salida.json>"""
import hashlib, json, sys
from collections import Counter
from pathlib import Path
C = Path(sys.argv[1]).resolve()
A = [json.loads(x) for x in Path(sys.argv[2]).read_text(encoding="utf-8").splitlines()]
D = [json.loads(x) for x in Path(sys.argv[3]).read_text(encoding="utf-8").splitlines()]
RAZON = json.loads(Path(sys.argv[4]).read_text(encoding="utf-8"))
OUT = Path(sys.argv[5]).resolve()
REX = C / "data/experiment/reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador"))
import comun_e3  # noqa: E402
import prompt_e3 as P  # noqa: E402
assert Path(P.__file__).resolve().is_relative_to(C)
assert len(A) == len(D)
clave = lambda x: (x["universo"], x.get("to"), x["chunk_id"], x.get("con_marca_r2"), x.get("caso"))  # noqa: E731
pares = list(zip(A, D))
assert all(clave(a) == clave(d) for a, d in pares)
res = {"filas": len(pares)}
por = Counter(); cambia = Counter()
for a, d in pares:
    k = (a["universo"], "con_marca" if a.get("con_marca_r2") else "sin_marca", "item" if a.get("es_item") else "no_item")
    por[k] += 1; cambia[k] += a["sha_msg"] != d["sha_msg"]
res["por_universo"] = {" / ".join(k): {"filas": por[k], "cambian": cambia[k]} for k in sorted(por)}
res["fuente_y_citas_iguales_en_todas"] = all(a.get("len_fuente") == d.get("len_fuente") and a.get("sha_citas_default") == d.get("sha_citas_default")
                                             and a.get("sha_citas_bloque") == d.get("sha_citas_bloque") for a, d in pares if a["universo"] != "candado")
agregado = "\n" + P.NOTA_E3_ITEM_CASOS
items = [(a, d) for a, d in pares if a["universo"] == "r2b" and a.get("con_marca_r2") and a.get("es_item")]
dif = Counter(d["len_msg"] - a["len_msg"] for a, d in items)
res["items_r2b"] = {"items": len(items), "cambian": sum(a["sha_msg"] != d["sha_msg"] for a, d in items),
                    "caracteres_agregados_por_item": dict(dif), "largo_del_parrafo_con_su_salto": len(agregado)}
# control byte a byte: el mensaje de O5 menos el párrafo da el de HEAD
ch = {}
for to in sorted({a["to"] for a, _ in items}):
    for c in comun_e3.cargar_chunks((to,), e0_dir=REX / "e0_chunking/salida_tanda0_r2b"):
        ch[c["id"]] = c
    pp = REX / "corpus_tanda0/salida_r2b" / to / "particiones_por_corte.json"
    if pp.exists():  # las partes de una partición por corte, como ue3_o2_medicion.py
        for cid, v in json.loads(pp.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                base = dict(ch[cid]); base.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                ch[parte["id"]] = base
val = {}
for to in sorted({a["to"] for a, _ in items}):
    for l in (REX / f"corpus_tanda0/salida_r2b/{to}/extracciones_e1.jsonl").read_text(encoding="utf-8").splitlines():
        x = json.loads(l); val[x["chunk_id"]] = x["validacion"]
ok, sin_chunk = 0, []
for a, d in items:
    c = ch.get(a["chunk_id"])
    if c is None:
        sin_chunk.append(a["chunk_id"]); continue
    v = dict(val[a["chunk_id"]], forma_salida="r2")
    m = P.build_user_message(c, v)
    assert hashlib.sha256(m.encode("utf-8")).hexdigest() == d["sha_msg"], a["chunk_id"]
    assert m.count(agregado) == 1
    ok += hashlib.sha256(m.replace(agregado, "", 1).encode("utf-8")).hexdigest() == a["sha_msg"]
res["control_byte_a_byte_items"] = {"cumple": ok, "de": len(items) - len(sin_chunk), "sin_chunk_en_e0": sin_chunk}
chars = sum(d["len_msg"] - a["len_msg"] for a, d in items)
marg = RAZON["chars_por_token_marginal"]
reverif = 0
items_ids = {a["chunk_id"] for a, _ in items}
for to in sorted({a["to"] for a, _ in items}):
    for l in (REX / f"corpus_tanda0/salida_r2b/{to}/veredictos.jsonl").read_text(encoding="utf-8").splitlines():
        v = json.loads(l)
        reverif += v["fase"] != "verificacion" and v["chunk_id"] in items_ids
tok_item = len(agregado) / marg
res["costo"] = {"razon_marginal_chars_por_token": marg, "caracteres_agregados_items": chars,
                "tokens_agregados_items": round(chars / marg), "usd_por_corrida_items": round(chars / marg * 2 / 1e6, 4),
                "re_verificaciones_de_items_tanda0": reverif, "llamadas_con_re_verificaciones": len(items) + reverif,
                "tokens_agregados_con_re_verificaciones": round((len(items) + reverif) * tok_item),
                "usd_con_re_verificaciones": round((len(items) + reverif) * tok_item * 2 / 1e6, 4)}
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
