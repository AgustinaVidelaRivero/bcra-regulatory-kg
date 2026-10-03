"""
nofiltracion.py — U-PROMPT-R2 P1 (USD 0): control de no-filtración
del borrador del prefijo r2, con la regla de ESQ-3b
(data/experiment/esq/prerregistro_esq3b_v2.md:42-50 y :177-184):
  (1) ninguna ventana de 5 palabras del texto de un chunk de prueba aparece en
      el texto AGREGADO al prefijo (ventanas del prefijo nuevo que no están en
      el sellado); las preexistentes se declaran (simétricas en la pareada);
  (2) bigramas y trigramas de los casos de control y de X5 en el texto
      agregado, sin palabras funcionales, listados para revisión.
Población de (1): todos los chunks (texto propio y heredado) de la E0 legada
de los diez TOs (salida_tanda0, de donde sale la muestra de P4) y de los
cuatro TOs del estrato fuera de muestra (segmentacion_84/b584_particion).
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

REPO = Path(sys.argv[1])
NUEVO = Path(sys.argv[2]).read_text(encoding="utf-8")
SALIDA = Path(sys.argv[3])
sys.path.insert(0, str(REPO / "data/experiment/b54_catalogo_v3/code"))
sys.path.insert(0, str(REPO / "data/experiment/esq/code"))
sys.path.insert(0, str(REPO / "data/experiment/reextraccion_v2/e1_extractor"))
import prompt_v3_b54 as v3  # noqa: E402

VIEJO = v3.PREFIJO_SISTEMA_V3
FUNCIONALES = set("""a al algo ante bajo cada como con contra cual cuando de del desde donde e el ella ello en entre es esa
ese eso esta este esto la las le les lo los más mas mismo muy ni no o os para pero por que qué se si sí sin sobre su sus
también tan tanto te todo todos toda todas u un una uno unos unas y ya será serán ser son está están haya hayan""".split())


def toks(s: str) -> list[str]:
    s = s.replace("-\n", "").replace("- \n", "")
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.findall(r"[a-z0-9]+", s)


def ngramas(t: list[str], n: int) -> set[tuple[str, ...]]:
    return {tuple(t[i:i + n]) for i in range(len(t) - n + 1)}


def chunks_de(path: Path) -> list[dict]:
    d = json.loads(path.read_text(encoding="utf-8"))
    return d if isinstance(d, list) else d.get("chunks", [])


def texto_chunk(c: dict) -> str:
    return "\n".join([h.get("texto", "") for h in c.get("herencia", [])] + [c.get("texto", "")])


DIEZ = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")
fuentes = [(to, REPO / f"data/experiment/reextraccion_v2/e0_chunking/salida_tanda0/chunks_{to}.json") for to in DIEZ]
fuentes += [(to, REPO / f"data/experiment/segmentacion_84/b584_particion/{to}/chunks_{to}.json") for to in FUERA]

v_nuevo, v_viejo = toks(NUEVO), toks(VIEJO)
agregadas5 = ngramas(v_nuevo, 5) - ngramas(v_viejo, 5)
choques: dict[tuple, list[str]] = {}
preexistentes: dict[tuple, list[str]] = {}
n_chunks = 0
# Casos de control fijos de P4 (decisión 19, con los ids reales decididos por la autora el 03/10/2026:
# ric::9.2.1 en lugar del ancla ric:9.2, y cap::6.2.2.6) y chunks de X5.
CONTROL = {"cap::1.2", "ric::9.2.1", "cla::5.1.1.1", "pro::1.1.2.5", "cap::6.2.2.6", "docvig::3.3::cierre",
           "ctacte::7.3.1.5", "ctacte::8.3::intro", "ctacte::8.4::intro", "lingob::2.3.2.2",
           # casos de F1-A (fichas 11, 13, 48, 52 y 64 de ESQ-2 e incisos de la 64; decisión de la autora, 03/10/2026)
           "ayccef::4.2.7.2", "expaef::6.6.2", "ayccef::3.4.1", "expaef::1.1.2.5", "adrei::4.3.1::intro",
           "adrei::4.3.1.1", "adrei::4.3.1.2", "adrei::4.3.1.3",
           # caso de control de la especie de BKL-0035 (decisión de la autora, 03/10/2026)
           "ctacte::6.4.7::intro"}
control_toks: dict[str, list[str]] = {}
for to, p in fuentes:
    for c in chunks_de(p):
        n_chunks += 1
        tk = toks(texto_chunk(c))
        g5 = ngramas(tk, 5)
        for w in g5 & agregadas5:
            choques.setdefault(w, []).append(c["id"])
        for w in g5 & (ngramas(v_nuevo, 5) & ngramas(v_viejo, 5)):
            preexistentes.setdefault(w, []).append(c["id"])
        if c["id"] in CONTROL:
            # texto propio y heredado: en los ítems, el encabezado que compone la norma está en la herencia
            control_toks[c["id"]] = toks(texto_chunk(c))

# (2) bigramas y trigramas de los casos de control en el texto agregado
agregados_23 = (ngramas(v_nuevo, 2) | ngramas(v_nuevo, 3)) - (ngramas(v_viejo, 2) | ngramas(v_viejo, 3))
dist = {}
for cid, tk in sorted(control_toks.items()):
    g = {w for w in (ngramas(tk, 2) | ngramas(tk, 3)) if not all(x in FUNCIONALES for x in w)
         and sum(x not in FUNCIONALES for x in w) >= 2}
    inter = sorted(" ".join(w) for w in g & agregados_23)
    if inter:
        dist[cid] = inter

res = {
    "chunks_controlados": n_chunks,
    "tos": list(DIEZ) + list(FUERA),
    "ventanas5_agregadas": len(agregadas5),
    "choques_ventana5_texto_agregado": {" ".join(k): sorted(set(v))[:10] for k, v in sorted(choques.items())},
    "n_choques": len(choques),
    "ventanas5_preexistentes_en_chunks": len(preexistentes),
    "control_no_encontrados": sorted(CONTROL - set(control_toks)),
    "bi_trigramas_distintivos_de_control_en_texto_agregado": dist,
}
SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "choques_ventana5_texto_agregado"}, ensure_ascii=False, indent=1))
print("choques:", json.dumps(res["choques_ventana5_texto_agregado"], ensure_ascii=False, indent=1)[:4000])

# Origen de cada choque: bloque de catálogo r2 (contenido decidido en U-CAT-UNICO) o instrucciones nuevas
bloque = (REPO / "data/experiment/catalogo_unico/generados_r2/bloque_catalogo_r2.txt").read_text(encoding="utf-8")
g_bloque = ngramas(toks(bloque), 5)
por_origen = {"bloque_catalogo_r2": sorted(" ".join(k) for k in choques if k in g_bloque),
              "instrucciones_nuevas": sorted(" ".join(k) for k in choques if k not in g_bloque)}
res["choques_por_origen"] = por_origen
SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
# Bigramas y trigramas distintivos de los casos de control, también separados por origen
g23_bloque = ngramas(toks(bloque), 2) | ngramas(toks(bloque), 3)
bt_por_origen = {"bloque_catalogo_r2": {}, "instrucciones_nuevas": {}}
for cid, lista in dist.items():
    for w in lista:
        k = "bloque_catalogo_r2" if tuple(w.split()) in g23_bloque else "instrucciones_nuevas"
        bt_por_origen[k].setdefault(cid, []).append(w)
res["bi_trigramas_de_control_por_origen"] = bt_por_origen
SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print("por origen:", {k: len(v) for k, v in por_origen.items()}, por_origen["instrucciones_nuevas"])
print("bi/trigramas por origen:", {k: sum(len(x) for x in v.values()) for k, v in bt_por_origen.items()},
      bt_por_origen["instrucciones_nuevas"])
