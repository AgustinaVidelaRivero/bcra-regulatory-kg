"""
encabezados_lista.py — U-PROMPT-R2, P1 (USD 0): la unidad del encabezado de una lista con la regla 1 de
F1-A, E3 sobre esas unidades y los encabezados en línea de título de la tanda 0.

Solo lectura del repo; ninguna llamada a la API. Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/encabezados_lista.py .
Escribe data/experiment/prompt_r2/p1/salida/encabezados_lista.json y encabezados_lista.md.

Definiciones (las de U-DIAG-PROCESO, reports/u_diag_proceso/code/censo_estructural.py, 93ce4b7):
- ENCABEZADO DE LISTA con unidad propia (MINI ORDENADOR): mini-chunk intro o chapeau_seccion cuyo texto
  termina en «:».
- ENCABEZADO EN LÍNEA DE TÍTULO: unidad U cuya línea de título termina en «:» (bloque heredado de tipo
  `encabezado` de U en un hijo) y sin mini-chunk U::intro en la E0.
- Contenido de una unidad: entidades de tipo distinto de TextoOrdenado en la validación guardada.
Fuentes de la tanda 0: primera pasada de E1, veredictos de E3 y estado final en
data/experiment/reextraccion_v2/corpus_tanda0/salida/<to>/ (último commit ad6d5ad).
"""
from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(sys.argv[1]).resolve()
OUT = REPO / "data/experiment/prompt_r2/p1/salida"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
T0 = REPO / "data/experiment/reextraccion_v2/corpus_tanda0/salida"
E0 = {"legada": REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0",
      "e0_r2": REPO / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2"}
sys.path.insert(0, str(REPO / "data/experiment/reextraccion_v2/e3_verificador"))
sys.path.insert(0, str(Path(__file__).resolve().parent))
from comun_e3 import normalizar_para_cita  # noqa: E402
import mensaje_r2_borrador as MB  # noqa: E402

norm = lambda s: " ".join((s or "").split())  # noqa: E731
termina_dp = lambda s: norm(s).endswith((":", "："))  # noqa: E731
# Marcas de un plazo o una condición dentro de la cláusula que abre la lista (proxy declarado, no lectura).
RE_MARCA = re.compile(r"\b(dentro de|plazo|d[ií]as|meses|hasta (el|la|que)|antes de|a partir de|cuando|"
                      r"siempre que|en la medida|en caso|si |salvo|excepto|con excepci[oó]n|sin perjuicio)", re.I)
# Marcas de que la cláusula anuncia supuestos o condiciones: por R30, los ítems son Condicion y la unidad del
# encabezado conserva la norma principal (no queda vacía por la regla 1).
RE_SUPUESTOS = re.compile(r"\b(casos|supuestos|situaciones|condiciones|circunstancias)\b", re.I)


def cargar_chunks(d: Path) -> dict:
    out = {}
    for to in TOS:
        for c in json.loads((d / f"chunks_{to}.json").read_text(encoding="utf-8")):
            out[c["id"]] = c
    return out


def jsonl(p: Path):
    for line in p.read_text(encoding="utf-8").splitlines():
        if line.strip():
            yield json.loads(line)


def es_mini_ordenador(c: dict) -> bool:
    return c["tipo"] == "mini_chunk" and c.get("rol_bloque") in ("intro", "chapeau_seccion") and termina_dp(c["texto"])


def contenido(val: dict | None) -> list[dict]:
    return [e for e in (val or {}).get("entidades", []) if e.get("type") != "TextoOrdenado"]


def clausula_ordenadora(texto: str) -> str:
    """La última oración del bloque, la que abre la lista (sin la numeración de la línea de título)."""
    t = norm(texto)
    i = t.rfind(". ", 0, len(t) - 1)
    return t[i + 2:] if i != -1 else t


def resto_del_bloque(c: dict) -> str:
    """El texto del mini sin la cláusula que abre la lista ni la línea de título de su unidad."""
    t = norm(c["texto"])
    cl = clausula_ordenadora(c["texto"])
    resto = t[: len(t) - len(cl)].strip()
    tit = norm(c.get("titulo") or "")
    for pref in (f"{c['unidad']}. {tit}", f"{c['unidad']}.", tit):
        if pref and resto.startswith(pref):
            resto = resto[len(pref):].strip()
    return resto


chunks = {k: cargar_chunks(v) for k, v in E0.items()}
assert set(chunks["legada"]) == set(chunks["e0_r2"]), "las dos E0 tienen ids distintos"

primera, veredictos, finales = {}, defaultdict(list), {}
for to in TOS:
    for r in jsonl(T0 / to / "extracciones_e1.jsonl"):
        primera[r["chunk_id"]] = r.get("validacion")
    for v in jsonl(T0 / to / "veredictos.jsonl"):
        veredictos[v["chunk_id"]].append(v)
    for r in jsonl(T0 / to / "finales.jsonl"):
        finales[r["chunk_id"]] = r

res: dict = {"fuente_tanda0": "data/experiment/reextraccion_v2/corpus_tanda0/salida/<to>/ (ad6d5ad)"}

# ------------------------------------------------------------------------- #
# 1. Minis ordenadores: cuántos, cuántos vacíos en la primera pasada y qué hizo E3 con ellos  #
# ------------------------------------------------------------------------- #
minis = {k: sorted(i for i, c in ch.items() if es_mini_ordenador(c)) for k, ch in chunks.items()}
res["minis_ordenadores"] = {k: len(v) for k, v in minis.items()}
res["minis_ordenadores_solo_en_una_e0"] = {"solo_legada": sorted(set(minis["legada"]) - set(minis["e0_r2"])),
                                          "solo_e0_r2": sorted(set(minis["e0_r2"]) - set(minis["legada"]))}


def cita_es_clausula(f: dict, c: dict) -> bool:
    """La condición de cita de la guarda LAUDO B (ratchet_e3.py:117-118): cita verificada, normalizada,
    que termina en «:» y está contenida en el bloque."""
    cn = normalizar_para_cita(f.get("cita_textual_del_fuente") or "")
    return bool(f.get("cita_verificada")) and cn.endswith(":") and cn in normalizar_para_cita(c["texto"])


vacios = []
for cid in minis["legada"]:
    if primera.get(cid) is None or contenido(primera[cid]):
        continue
    c = chunks["legada"][cid]
    vs = sorted(veredictos.get(cid, []), key=lambda v: v["intento"])
    fin = finales.get(cid) or {}
    vacios.append({
        "chunk_id": cid,
        "texto": norm(c["texto"]),
        "veredictos": [{"fase": v["fase"], "intento": v["intento"], "n_bloqueantes": v["n_bloqueantes"],
                        "faltantes": [{"tipo": f["tipo"], "severidad": f["severidad"], "bloqueante": f["bloqueante"],
                                       "estructural_no_bloqueante": f["estructural_no_bloqueante"],
                                       "cita_es_clausula_ordenadora": cita_es_clausula(f, c),
                                       "cita": f["cita_textual_del_fuente"]} for f in v["faltantes"]]}
                       for v in vs],
        "estado_final": fin.get("estado"),
        "n_reintentos": fin.get("n_reintentos"),
        "contenido_final": [{"type": e["type"], "label": e.get("label"),
                             "descripcion": (e.get("properties") or {}).get("descripcion")}
                            for e in contenido(fin.get("validacion_final"))],
    })
res["vacios_primera_pasada"] = vacios
bloq = [x for x in vacios if x["veredictos"] and x["veredictos"][0]["n_bloqueantes"] > 0]
res["vacios_resumen"] = {
    "n": len(vacios),
    "bloqueados_por_e3_en_la_verificacion": len(bloq),
    "con_nodo_creado_por_el_reintento": sum(1 for x in vacios if x["n_reintentos"] and x["contenido_final"]),
    "bloqueos_con_cita_en_la_clausula_ordenadora": sum(
        1 for x in bloq if any(f["bloqueante"] and f["cita_es_clausula_ordenadora"] for f in x["veredictos"][0]["faltantes"])),
    "tipos_de_faltante_bloqueante": dict(Counter(f["tipo"] for x in bloq for f in x["veredictos"][0]["faltantes"]
                                                 if f["bloqueante"])),
    "estados_finales": dict(Counter(x["estado_final"] for x in vacios)),
}

# E3 sobre todos los minis ordenadores (no solo los vacíos): faltantes bloqueantes de la verificación cuya cita es
# la cláusula ordenadora (lo que la guarda ampliada dejaría de bloquear) y los que ya marca la guarda de hoy.
amp = Counter()
amp_ids = defaultdict(list)
for cid in minis["legada"]:
    c = chunks["legada"][cid]
    for v in veredictos.get(cid, []):
        for f in v["faltantes"]:
            if f["estructural_no_bloqueante"]:
                amp[f"{v['fase']}|guarda_actual"] += 1
            if f["bloqueante"] and cita_es_clausula(f, c):
                amp[f"{v['fase']}|bloqueante_con_cita_en_la_clausula|{f['tipo']}"] += 1
                amp_ids[v["fase"]].append(cid)
res["e3_en_minis_ordenadores"] = {"conteos": dict(sorted(amp.items())),
                                  "unidades_bloqueadas_por_la_clausula": {k: sorted(set(v)) for k, v in amp_ids.items()}}
res["e3_unidades_en_la_verificacion"] = sum(1 for cid in minis["legada"] if veredictos.get(cid))
n_reint = sum((r.get("n_reintentos") or 0) for r in finales.values())
res["reintentos_tanda0"] = n_reint

# ------------------------------------------------------------------------- #
# 2. Proyección con la regla 1: cuántos encabezados quedarían vacíos (proxy textual sobre e0-r2) #
# ------------------------------------------------------------------------- #
proy = Counter()
proy_ids = defaultdict(list)
emitido = defaultdict(Counter)
RE_NUMERACION = re.compile(r"^\s*(?:[0-9]+\.)+\s*")


def clausula_completa(c: dict) -> str:
    """La cláusula que abre la lista; si el bloque no tiene una oración propia y empieza a mitad de una oración
    que viene de la línea de título de su misma unidad (sin punto final), las dos partes (como en
    ctacte::1.5.4::intro y ctacte::3.2.1::intro)."""
    cl = clausula_ordenadora(c["texto"])
    her = c.get("herencia") or []
    if cl == norm(c["texto"]) and her and her[-1]["unidad_origen"] == c["unidad"] \
            and her[-1]["tipo"] == "encabezado" and not norm(her[-1]["texto"]).endswith("."):
        cl = RE_NUMERACION.sub("", norm(her[-1]["texto"])) + " " + cl
    return cl


for cid in minis["e0_r2"]:
    c = chunks["e0_r2"][cid]
    cl = clausula_completa(c)
    resto = resto_del_bloque(c)
    if resto:
        k = "con_otro_texto"
    elif RE_SUPUESTOS.search(cl):
        k = "solo_la_clausula_que_anuncia_supuestos"
    elif RE_MARCA.search(cl):
        k = "solo_la_clausula_con_marca_de_plazo_o_condicion"
    else:
        k = "solo_la_clausula_sin_marca"
    proy[k] += 1
    proy_ids[k].append(cid)
    ents = contenido(primera.get(cid))
    emitido[k]["vacio" if not ents else "con_contenido"] += 1
    for e in ents:
        emitido[k + "|tipos"][e["type"]] += 1
# Límite de la proxy (declarado a pedido de la autora, 03/10/2026): RE_MARCA no reconoce «en el caso de que» ni
# «en los casos en que»; ext::4.8.6::intro, que abre con una condición en su línea de título, cae en «sin marca».
RE_MARCA_CASO = re.compile(r"\ben (el|los) casos? (de que|en que|de)\b", re.I)
sens = [cid for cid in proy_ids["solo_la_clausula_sin_marca"] if RE_MARCA_CASO.search(clausula_completa(chunks["e0_r2"][cid]))]
res["proyeccion_regla1"] = {"clases": dict(proy), "ids": {k: sorted(v) for k, v in proy_ids.items()},
                            "primera_pasada_por_clase": {k: dict(v) for k, v in emitido.items()},
                            "limite_de_la_proxy": {
                                "caso": "ext::4.8.6::intro",
                                "clasificado_como": next(k for k, v in proy_ids.items() if "ext::4.8.6::intro" in v),
                                "sin_marca_que_abren_con_en_el_caso": sorted(sens),
                                "sin_marca_si_se_suma_esa_marca": len(proy_ids["solo_la_clausula_sin_marca"]) - len(sens)}}

# ------------------------------------------------------------------------- #
# 2b. Guarda LAUDO B ampliada, recontada sobre la tanda 0: una unidad se desbloquea si TODOS sus faltantes
#     bloqueantes tienen la cita en la cláusula ordenadora y la unidad tiene descendientes en la E0 (la condición
#     de ratchet_e3.py:93-99, recontada en `minis_con_descendientes`). Variante con salvaguarda: además, la
#     extracción verificada no tiene Obligacion, Restriccion ni Potestad.
# ------------------------------------------------------------------------- #
unidades_por_to = defaultdict(set)
for c in chunks["legada"].values():
    unidades_por_to[c["to"]].add(c["unidad"])


def con_descendientes(c: dict) -> bool:
    u = c["unidad"]
    pref = (u[1:] + ".") if u.startswith("S") else (u + ".")
    return any(x.startswith(pref) for x in unidades_por_to[c["to"]])


NORMATIVOS = ("Obligacion", "Restriccion", "Potestad")
guarda = {"minis_con_descendientes": sum(1 for cid in minis["legada"] if con_descendientes(chunks["legada"][cid]))}
for fase in ("verificacion", "re_verificacion"):
    bloq_u, desb, desb_salv = [], [], []
    for cid in minis["legada"]:
        c = chunks["legada"][cid]
        for v in veredictos.get(cid, []):
            if v["fase"] != fase:
                continue
            b = [f for f in v["faltantes"] if f["bloqueante"]]
            if not b:
                continue
            bloq_u.append(cid)
            if con_descendientes(c) and all(cita_es_clausula(f, c) for f in b):
                desb.append(cid)
                val = primera.get(cid) if fase == "verificacion" else None
                if val is not None and not any(e["type"] in NORMATIVOS for e in contenido(val)):
                    desb_salv.append(cid)
    guarda[fase] = {"unidades_con_bloqueo": len(bloq_u), "desbloqueadas": len(desb),
                    "desbloqueadas_ids": sorted(desb),
                    "estado_final_de_las_desbloqueadas": dict(Counter((finales.get(i) or {}).get("estado") for i in desb))}
    if fase == "verificacion":
        guarda[fase]["desbloqueadas_con_salvaguarda"] = len(desb_salv)
        guarda[fase]["desbloqueadas_con_salvaguarda_ids"] = sorted(desb_salv)
res["guarda_ampliada_tanda0"] = guarda

# NOTA de E3 para los encabezados de lista (salida a): a qué unidades llega y cuánto agrega, sobre e0-r2.
nota = {cid: MB.nota_e3_encabezado_r2(chunks["e0_r2"][cid]) for cid in chunks["e0_r2"]}
nota = {k: v for k, v in nota.items() if v}
censo = json.loads((OUT / "censo_p1.json").read_text(encoding="utf-8"))
cal_in = censo["calibracion"]["mensaje"]["tokens_por_caracter"]
t0 = censo["tanda0_fases_cerradas"]
e3_por_llamada = t0["e3_verificador_usd"] / t0["e3_tokens"]["llamadas"]
e1_reintento = t0["e3_reintentos_e1_usd"] / n_reint
factor_e1_r2 = censo["costos"]["A_central"]["e1_por_unidad_usd"] / (t0["e1_usd"] / t0["n_e1"])
chars = sum(len(v) + 1 for v in nota.values())
res["nota_e3_encabezado"] = {
    "unidades": len(nota), "igual_a_los_minis_ordenadores_e0_r2": sorted(nota) == minis["e0_r2"],
    "caracteres_por_unidad": len(next(iter(nota.values()))), "caracteres_total": chars,
    "costo_usd": round(chars * cal_in * 2.00 / 1e6, 4),
    "base": "tokens por calibración del mensaje de E1 (censo_p1.json), a la tarifa de entrada de E3 (USD 2/MTok)",
}
res["costo_ciclo_de_reintento_usd"] = {
    "e1_reintento_tanda0": round(e1_reintento, 5), "e3_reverificacion_tanda0": round(e3_por_llamada, 5),
    "ciclo_tanda0": round(e1_reintento + e3_por_llamada, 5),
    "ciclo_r2_central": round(e1_reintento * factor_e1_r2 + e3_por_llamada, 5),
    "base": "media de la tanda 0: reintentos de E1 del ratchet (USD 2,325 entre los reintentos de finales.jsonl) "
            "y verificador por llamada (19,9529 entre 2.681); E1 r2 escalado por el costo por unidad central A",
}

# ------------------------------------------------------------------------- #
# 3. Encabezados en línea de título sin unidad propia: contexto, ítems y lo que quedó en la tanda 0  #
# ------------------------------------------------------------------------- #
def titulo_sin_unidad(ch: dict) -> dict:
    out = {}
    for c in ch.values():
        if c["tipo"] != "punto_terminal":
            continue
        for h in c.get("herencia", []):
            if h["tipo"] == "encabezado" and termina_dp(h["texto"]) and h["unidad_origen"] != c["unidad"] \
                    and f"{c['to']}::{h['unidad_origen']}::intro" not in ch:
                out.setdefault(f"{c['to']}::{h['unidad_origen']}", norm(h["texto"]))
    return out


tit = {k: titulo_sin_unidad(ch) for k, ch in chunks.items()}
res["titulo_sin_unidad"] = {k: sorted(v) for k, v in tit.items()}
fichas = []
for u in sorted(tit["legada"]):
    to, un = u.split("::")
    hijos = sorted((c for c in chunks["e0_r2"].values() if c["to"] == to and c["unidad"].startswith(un + ".")),
                   key=lambda c: [int(x) if x.isdigit() else x for x in re.split(r"[.:]", c["id"].split("::", 1)[1])])
    her = hijos[0].get("herencia", []) if hijos else []
    fichas.append({
        "unidad": u,
        "titulo": tit["legada"][u],
        "sin_unidad_tambien_en_e0_r2": u in tit["e0_r2"],
        "ancestros": [f"[{h['tipo']} | {h['unidad_origen']}] {norm(h['texto'])}" for h in her
                      if h["unidad_origen"] != un],
        "items": [{"chunk_id": h["id"], "texto": norm(h["texto"]),
                   "final_tanda0": [f"{e['type']}: {(e.get('properties') or {}).get('descripcion') or e.get('label')}"
                                    for e in contenido((finales.get(h["id"]) or {}).get("validacion_final"))]}
                  for h in hijos],
    })
res["encabezados_titulo"] = fichas

# Partición B5.8.4 (152 TOs, E0 legada, commiteada): encabezados en línea de título sin unidad propia, con una
# proxy mecánica (no lectura) de si sus ítems son condiciones o supuestos y de cómo se unen: la marca de la
# cláusula del título y la conjunción con que termina el penúltimo ítem («y» conjuntiva, «o» alternativa).
part = {}
for d in sorted((REPO / "data/experiment/segmentacion_84/b584_particion").iterdir()):
    f = d / f"chunks_{d.name}.json"
    if d.is_dir() and f.exists():
        for c in json.loads(f.read_text(encoding="utf-8")):
            part[c["id"]] = c
tit_part = titulo_sin_unidad(part)
RE_COND_TIT = re.compile(r"siempre que|cuando|en la medida|\b(casos|supuestos|situaciones|condiciones|circunstancias|"
                         r"requisitos)\b", re.I)
prox = Counter()
for u, t in tit_part.items():
    to, un = u.split("::")
    hijos = sorted((c for c in part.values() if c["to"] == to and c["tipo"] == "punto_terminal"
                    and c["unidad"].startswith(un + ".") and c["unidad"].count(".") == un.count(".") + 1),
                   key=lambda c: [int(x) if x.isdigit() else x for x in c["unidad"].split(".")])
    pen = norm(hijos[-2]["texto"]) if len(hijos) >= 2 else ""
    conj = "y" if re.search(r"[;,]?\s+y$", pen) else "o" if re.search(r"[;,]?\s+o$", pen) else "sin_conjuncion"
    prox[("anuncia_condiciones_o_supuestos" if RE_COND_TIT.search(t) else "sin_marca", conj)] += 1
res["particion_titulo_sin_unidad"] = {"n": len(tit_part),
                                      "proxy": {f"{a}|{b}": n for (a, b), n in sorted(prox.items())}}

OUT.mkdir(parents=True, exist_ok=True)
(OUT / "encabezados_lista.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

md = ["# Encabezados de lista: insumo de lectura (generado por p1/encabezados_lista.py)", ""]
md.append("## Minis ordenadores vacíos en la primera pasada de E1 de la tanda 0")
for x in vacios:
    md.append(f"- `{x['chunk_id']}`: «{x['texto']}» — estado final `{x['estado_final']}`, reintentos "
              f"{x['n_reintentos']}, contenido final: {x['contenido_final'] or 'ninguno'}")
    for v in x["veredictos"]:
        for f in v["faltantes"]:
            md.append(f"  - {v['fase']} {v['intento']}: {f['tipo']}, {f['severidad']}, bloqueante {f['bloqueante']}, "
                      f"guarda {f['estructural_no_bloqueante']}, cita en la cláusula {f['cita_es_clausula_ordenadora']}")
md += ["", "## Encabezados en línea de título sin unidad propia (tanda 0)"]
for f in fichas:
    md += ["", f"### `{f['unidad']}` — «{f['titulo']}» (sin unidad también en e0-r2: {f['sin_unidad_tambien_en_e0_r2']})"]
    md += [f"- ancestro: {a}" for a in f["ancestros"]]
    for it in f["items"]:
        md.append(f"- ítem `{it['chunk_id']}`: «{it['texto'][:400]}»")
        md += [f"  - final tanda 0: {e}" for e in it["final_tanda0"]]
(OUT / "encabezados_lista.md").write_text("\n".join(md) + "\n", encoding="utf-8")
print(json.dumps({k: res[k] for k in ("minis_ordenadores", "vacios_resumen", "e3_unidades_en_la_verificacion",
                                      "reintentos_tanda0")}, ensure_ascii=False, indent=1))
print(json.dumps(res["proyeccion_regla1"]["clases"], ensure_ascii=False), json.dumps(res["proyeccion_regla1"]["limite_de_la_proxy"], ensure_ascii=False))
print(json.dumps(res["proyeccion_regla1"]["primera_pasada_por_clase"], ensure_ascii=False))
print(json.dumps(res["e3_en_minis_ordenadores"]["conteos"], ensure_ascii=False, indent=1))
print(res["minis_ordenadores_solo_en_una_e0"], {k: len(v) for k, v in res["titulo_sin_unidad"].items()})
print(json.dumps({k: v for k, v in res["guarda_ampliada_tanda0"].items()}, ensure_ascii=False, indent=1))
print(json.dumps(res["particion_titulo_sin_unidad"], ensure_ascii=False))
print(json.dumps(res["nota_e3_encabezado"], ensure_ascii=False), json.dumps(res["costo_ciclo_de_reintento_usd"], ensure_ascii=False))
