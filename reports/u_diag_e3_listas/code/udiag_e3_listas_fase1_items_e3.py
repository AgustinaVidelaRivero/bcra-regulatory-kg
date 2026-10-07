"""U-DIAG-E3-LISTAS, fase 1 (solo lectura, USD 0): sobre una copia de HEAD sin enlaces simbólicos.

1. Para cada unidad verificada por E3 en la corrida r2b de la tanda 0 (veredictos.jsonl, fase verificacion,
   intento 0), arma el mensaje de E1 con prompt_r2b.build_user_message_r2b y marca las que llevan la línea del ítem
   de lista (LINEA_ITEM: rama `elif i is not None` de prompt_r2b.py:415-418). Para esas, el tipo del bloque que abre
   la lista (bloque_lista) y si su texto entra en la sección «TEXTO FUENTE ÍNTEGRO» del mensaje de E3, armado con
   prompt_e3.build_user_message sobre la validación de E1 (extracciones_e1.jsonl). También si el mensaje de E3 lleva
   NOTA_E3_ENCABEZADO_LISTA.
2. Busca en el prefijo de E3 (PREFIJO_SISTEMA) las palabras de la composición con el encabezado de una lista.
3. Candidatos a reclamo sobre una Excepcion en los ítems: todo faltante de todo veredicto (intento 0 y 1) de una
   unidad con LINEA_ITEM cuyo tipo es excepcion_ausente o cuya nota o cita menciona una excepción (regex sobre el
   texto normalizado sin tildes). Se clasifican a mano después (adjudicacion_polaridad.json).

Uso: python fase1_items_e3.py <copia> <salida_dir>
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
SAL = Path(sys.argv[2]).resolve()
SAL.mkdir(parents=True, exist_ok=True)
REX = COPIA / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e3_verificador"))
import comun_e3  # noqa: E402  (agrega e1_extractor al sys.path)
import prompt_r2b as R  # noqa: E402
import prompt_e3 as P  # noqa: E402

SALIDA = REX / "corpus_tanda0" / "salida_r2b"
E0 = REX / "e0_chunking" / "salida_tanda0_r2b"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")


def jl(p: Path) -> list[dict]:
    if not p.exists():
        return []
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def ultima(p: Path) -> dict:
    return {r["chunk_id"]: r for r in jl(p)}


def chunks(to: str) -> dict:
    """Como reext_t0/t4/comun_t4.chunks: E0 r2b más las partes de particiones_por_corte.json."""
    d = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
    out = {c["id"]: c for c in (d["chunks"] if isinstance(d, dict) else d)}
    p = SALIDA / to / "particiones_por_corte.json"
    if p.exists():
        for cid, v in json.loads(p.read_text(encoding="utf-8")).items():
            for parte in v["partes"]:
                base = dict(out[cid])
                base.update({k: parte[k] for k in parte if k != "id"}, id=parte["id"])
                out[parte["id"]] = base
    return out


def norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t or "")
    t = "".join(ch for ch in t if not unicodedata.combining(ch))
    return " ".join(t.lower().split())


RE_EXC = re.compile(r"excep|exceptu|salvo|excepto")
MARCA_ITEM = "abre la lista de la que este punto es un ítem"

unidades = []
candidatos = []
fallas_consistencia = []
for to in TOS:
    ch = chunks(to)
    e1 = ultima(SALIDA / to / "extracciones_e1.jsonl")
    ver = jl(SALIDA / to / "veredictos.jsonl")
    reint = {r["chunk_id"] for r in jl(SALIDA / to / "reintentos_e3.jsonl")}
    cola = ultima(SALIDA / to / "cola_humana.jsonl")
    fin = ultima(SALIDA / to / "finales.jsonl")
    ver_por = {}
    for v in ver:
        ver_por.setdefault(v["chunk_id"], []).append(v)
    for cid, vs in ver_por.items():
        if not any(v["fase"] == "verificacion" and v["intento"] == 0 for v in vs):
            continue
        c = ch[cid]
        msg1 = R.build_user_message_r2b(c)
        linea_item = MARCA_ITEM in msg1
        i = R.bloque_lista(c)
        if linea_item != (bool(c.get("herencia")) and not R.es_mini_chunk(c) and i is not None):
            fallas_consistencia.append(cid)
        u = {"chunk_id": cid, "to": to, "linea_item": linea_item, "mini": R.es_mini_chunk(c),
             "en_reintentos": cid in reint, "cola_flag": (cola.get(cid) or {}).get("flag"),
             "estado_final": (fin.get(cid) or {}).get("estado")}
        if linea_item:
            h = c["herencia"][i]
            val = (e1.get(cid) or {}).get("validacion")
            msg3 = P.build_user_message(c, val)
            fuente = msg3.split("TEXTO FUENTE ÍNTEGRO DE LA UNIDAD", 1)[1].split("ELEMENTOS EXTRAÍDOS DE ESTA UNIDAD", 1)[0]
            u.update({
                "abre_lista_tipo": h["tipo"], "abre_lista_unidad": h["unidad_origen"],
                "abre_lista_texto": h["texto"],
                "abre_lista_en_fuente_e3": norm(h["texto"]) in norm(fuente),
                "abre_lista_en_fuente_para_citas": norm(h["texto"]) in norm(comun_e3.fuente_para_citas(c)),
                "nota_encabezado_lista_en_e3": P.NOTA_E3_ENCABEZADO_LISTA in msg3,
                "forma_r2_validacion": (val or {}).get("forma_salida"),
                "n_excepcion_e1": sum(1 for e in (val or {}).get("entidades") or [] if e.get("type") == "Excepcion"),
            })
            for v in vs:
                for k, f in enumerate(v.get("faltantes") or []):
                    texto = " ".join(str(f.get(x) or "") for x in ("nota", "cita_textual_del_fuente"))
                    if f.get("tipo") == "excepcion_ausente" or RE_EXC.search(norm(texto)):
                        candidatos.append({
                            "id": f"{cid}|{v['fase']}|{v['intento']}|{k}", "chunk_id": cid, "fase": v["fase"],
                            "intento": v["intento"], "tipo": f.get("tipo"), "severidad": f.get("severidad"),
                            "bloqueante": f.get("bloqueante"), "cita_verificada": f.get("cita_verificada"),
                            "estructural_no_bloqueante": f.get("estructural_no_bloqueante"),
                            "cita": f.get("cita_textual_del_fuente"), "nota": f.get("nota"),
                            "ubicacion": f.get("ubicacion")})
        unidades.append(u)

items = [u for u in unidades if u["linea_item"]]
pref = P.PREFIJO_SISTEMA
ocurr = {}
for pal in ("lista", "encabezado", "compon", "ítem", "item"):
    lin = [ln for ln in pref.splitlines() if pal in ln.lower()]
    ocurr[pal] = {"lineas": len(lin), "muestras": [ln[:240] for ln in lin[:8]]}

# Unidades del candado del mensaje de E3 (prompt_e3.py:404-428) que llevan LINEA_ITEM
fix = json.loads((REX / "e3_verificador" / "candado_mensaje_e3.json").read_text(encoding="utf-8"))
candado_items = sorted({c["chunk"]["id"] for c in fix["casos"]
                        if MARCA_ITEM in R.build_user_message_r2b(c["chunk"])} if True else [])

resumen = {
    "unidades_verificadas_e3": len(unidades),
    "unidades_con_linea_item": len(items),
    "linea_item_por_to": dict(Counter(u["to"] for u in items)),
    "fallas_consistencia_bloque_lista": fallas_consistencia,
    "abre_lista_tipo": dict(Counter(u["abre_lista_tipo"] for u in items)),
    "abre_lista_en_fuente_e3": dict(Counter(str(u["abre_lista_en_fuente_e3"]) for u in items)),
    "abre_lista_en_fuente_e3_por_tipo": dict(Counter(f"{u['abre_lista_tipo']}|{u['abre_lista_en_fuente_e3']}" for u in items)),
    "abre_lista_en_fuente_para_citas": dict(Counter(str(u["abre_lista_en_fuente_para_citas"]) for u in items)),
    "nota_encabezado_lista_en_e3_items": dict(Counter(str(u["nota_encabezado_lista_en_e3"]) for u in items)),
    "forma_r2_validacion_items": dict(Counter(str(u["forma_r2_validacion"]) for u in items)),
    "items_con_excepcion_en_e1": sum(1 for u in items if u["n_excepcion_e1"]),
    "prefijo_e3_hash": P.PREFIJO_HASH,
    "prefijo_e3_ocurrencias": ocurr,
    "candado_e3_unidades_con_linea_item": candado_items,
    "candidatos": len(candidatos),
    "candidatos_unidades": len({c["chunk_id"] for c in candidatos}),
}
(SAL / "fase1_resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(SAL / "fase1_unidades.json").write_text(json.dumps(unidades, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(SAL / "fase1_candidatos.json").write_text(json.dumps(candidatos, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in resumen.items() if k != "prefijo_e3_ocurrencias"}, ensure_ascii=False, indent=1))
print(json.dumps(ocurr, ensure_ascii=False, indent=1))
