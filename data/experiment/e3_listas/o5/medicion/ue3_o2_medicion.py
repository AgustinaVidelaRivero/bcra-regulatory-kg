"""U-E3-LISTAS, O2 (sobre la de O1, con D2): vuelca el mensaje de E3 y el fuente de las citas, unidad por unidad, con el código de UNA copia
(la de HEAD o la del prototipo). Sin API: solo arma mensajes con prompt_e3.build_user_message. No escribe en la copia.

Universos:
  - r2b: las unidades verificadas por E3 en la corrida r2b de la tanda 0 (veredictos.jsonl, fase verificacion,
    intento 0), con el chunk de E0 r2b (más las partes de particiones_por_corte.json, como comun_t4.chunks) y la
    validación de E1 que vio E3 (extracciones_e1.jsonl, la última por unidad); el mensaje con la marca r2 y sin ella;
  - v3b54: la corrida sellada de la tanda 0 (corpus_tanda0/salida, E0 salida_tanda0), sin la marca r2;
  - r1: la corrida de corpus_v2/salida (E0 salida_enm01), sin la marca r2;
  - candado: los 13 casos de candado_mensaje_e3.json.
Las unidades sin chunk en la E0 del universo se cuentan aparte.

Uso: python ue3_o1_medicion.py <copia> <salida.jsonl>
"""
from __future__ import annotations

import hashlib
import inspect
import json
import sys
from pathlib import Path

C = Path(sys.argv[1]).resolve()
OUT = Path(sys.argv[2]).resolve()
REX = C / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador"))
import comun_e3  # noqa: E402
import prompt_e3 as P  # noqa: E402  (candados del prefijo y del mensaje de E3)
import prompt_r2b as R  # noqa: E402

assert Path(P.__file__).resolve().is_relative_to(C) and Path(comun_e3.__file__).resolve().is_relative_to(C)
NUEVO = "bloque_de_lista" in inspect.signature(comun_e3.fuente_para_citas).parameters
TOS10 = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
TOS5 = ("pro", "cla", "ric", "cap", "ext")
MARCA_ITEM = "abre la lista de la que este punto es un ítem"


def jl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def sha(t: str) -> str:
    return hashlib.sha256(t.encode("utf-8")).hexdigest()


def chunks(e0: Path, salida: Path, to: str) -> dict:
    d = json.loads((e0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    out = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    p = salida / to / "particiones_por_corte.json"
    if p.exists():
        for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                base = dict(out[cid])
                base.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                out[parte["id"]] = base
    return out


def fuente_de(msg: str) -> str:
    return msg.split("TEXTO FUENTE ÍNTEGRO DE LA UNIDAD", 1)[1].split("ELEMENTOS EXTRAÍDOS DE ESTA UNIDAD", 1)[0]


def registro(universo: str, to: str, c: dict, val: dict | None, con_r2: bool) -> dict:
    v = dict(val or {})
    if not con_r2:
        v.pop("forma_salida", None)
    msg = P.build_user_message(c, v)
    i = R.bloque_lista(c)
    r = {"universo": universo, "to": to, "chunk_id": c["id"], "con_marca_r2": con_r2,
         "es_item": i is not None, "linea_item_e1": MARCA_ITEM in R.build_user_message_r2b(c),
         "mini": R.es_mini_chunk(c), "encabezado_de_lista": R.es_encabezado_de_lista(c),
         "len_msg": len(msg), "sha_msg": sha(msg), "len_fuente": len(fuente_de(msg)),
         "sha_citas_default": sha(comun_e3.fuente_para_citas(c)), "len_citas_default": len(comun_e3.fuente_para_citas(c))}
    if i is not None:
        h = c["herencia"][i]
        her = c["herencia"]
        j = i  # D2: los bloques contiguos que lo preceden con el mismo tipo y unidad de origen (cuenta propia, independiente
        while j > 0 and her[j - 1]["tipo"] == h["tipo"] and her[j - 1]["unidad_origen"] == h["unidad_origen"]:  # del código)
            j -= 1
        r.update({"grupo_n": i - j + 1,
                  "grupo_chars_con_rotulo": sum(len(f"[{x['tipo']} | punto {x['unidad_origen']}]") + 1 + len(x["texto"]) + 1
                                                for x in her[j:i + 1]),
                  "bloque_chars_con_rotulo": len(f"[{h['tipo']} | punto {h['unidad_origen']}]") + 1 + len(h["texto"]) + 1})
        r.update({"bloque_tipo": h["tipo"], "bloque_unidad": h["unidad_origen"], "bloque_len": len(h["texto"]),
                  "bloque_es_ultimo": i == len(c["herencia"]) - 1,
                  "cierres_despues": sum(1 for x in c["herencia"][i + 1:] if x["tipo"] == "cierre"),
                  "otros_prosa_antes": sum(1 for x in c["herencia"][:i] if x["tipo"] != "encabezado"),
                  "herencia_recortada": bool(c.get("herencia_recortada"))})
    if NUEVO:
        fc = comun_e3.fuente_para_citas(c, True)
        r.update({"sha_citas_bloque": sha(fc), "len_citas_bloque": len(fc)})
    return r


filas: list[dict] = []
faltan: dict[str, int] = {}
# r2b
E0R2B, SR2B = REX / "e0_chunking" / "salida_tanda0_r2b", REX / "corpus_tanda0" / "salida_r2b"
for to in TOS10:
    ch = chunks(E0R2B, SR2B, to)
    e1 = {r["chunk_id"]: r for r in jl(SR2B / to / "extracciones_e1.jsonl")}
    vistos = []
    for v in jl(SR2B / to / "veredictos.jsonl"):
        if v["fase"] == "verificacion" and v["intento"] == 0 and v["chunk_id"] not in vistos:
            vistos.append(v["chunk_id"])
    for cid in vistos:
        val = (e1.get(cid) or {}).get("validacion")
        for con in (True, False):
            filas.append(registro("r2b", to, ch[cid], val, con))
# v3b54 y r1, sin la marca r2
for universo, e0, sal, tos in (("v3b54", REX / "e0_chunking" / "salida_tanda0", REX / "corpus_tanda0" / "salida", TOS10),
                               ("r1", REX / "e0_chunking" / "salida_enm01", REX / "corpus_v2" / "salida", TOS5)):
    for to in tos:
        ch = chunks(e0, sal, to)
        e1 = {r["chunk_id"]: r for r in jl(sal / to / "extracciones_e1.jsonl")}
        vistos = []
        for v in jl(sal / to / "veredictos.jsonl"):
            if v["fase"] == "verificacion" and v["intento"] == 0 and v["chunk_id"] not in vistos:
                vistos.append(v["chunk_id"])
        for cid in vistos:
            if cid not in ch:
                faltan[universo] = faltan.get(universo, 0) + 1
                continue
            val = (e1.get(cid) or {}).get("validacion")
            if (val or {}).get("forma_salida") == "r2":
                raise SystemExit(f"{universo} {cid}: validación con la marca r2")
            filas.append(registro(universo, to, ch[cid], val, False))
# candado
fix = json.loads(P.CANDADO_MENSAJE_E3_JSON.read_text(encoding="utf-8"))
for k, caso in enumerate(fix["casos"]):
    msg = P.build_user_message(caso["chunk"], caso["validacion"])
    filas.append({"universo": "candado", "caso": k, "chunk_id": caso["chunk"]["id"],
                  "con_marca_r2": (caso["validacion"] or {}).get("forma_salida") == "r2",
                  "es_item": R.es_item(caso["chunk"]), "len_msg": len(msg), "sha_msg": sha(msg)})
OUT.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")
print(json.dumps({"codigo": "O2" if NUEVO else "HEAD", "filas": len(filas), "sin_chunk": faltan,
                  "candado_sha_mensaje": P.sha256_mensajes_e3(fix["casos"]),
                  "MENSAJE_E3_SHA256_ESPERADO": P.MENSAJE_E3_SHA256_ESPERADO,
                  "prefijo_hash": P.PREFIJO_HASH}, ensure_ascii=False))
