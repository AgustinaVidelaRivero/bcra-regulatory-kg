"""
nofiltracion_p3b.py — U-PROMPT-R2, P3b-1 (USD 0): control de no-filtración del parche, con la regla de ESQ-3b que
aplicó P1 (`data/experiment/prompt_r2/p1/nofiltracion.py`; prerregistro_esq3b_v2.md:42-50 y :177-184):
  (1) ninguna ventana de 5 palabras del texto de un chunk aparece en el texto AGREGADO: las ventanas del prefijo con
      el parche que no están en el prefijo congelado (`14d6b63b508e`), y las de los literales nuevos del mensaje de
      E1 y de la NOTA de E3;
  (2) bigramas y trigramas de los casos de control en el texto agregado, sin palabras funcionales, listados.
Población de (1): los chunks (texto propio y heredado) de la E0 legada y de la e0-r2 de los diez TOs y de los cuatro
TOs del estrato fuera de muestra. Casos de control: los de P1, los de P4 que suma la nota del 04/10/2026
(`cla::5.1.1::intro`) y las unidades de los hallazgos que el parche atiende.

Uso (desde la raíz de una copia):
  .venv/bin/python -B data/experiment/prompt_r2/p3b/nofiltracion_p3b.py PREFIJO_BORRADOR LITERALES SALIDA.json
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

P3B = Path(__file__).resolve().parent
REPO = P3B.parents[3]
sys.path.insert(0, str(REPO / "data" / "experiment" / "reextraccion_v2" / "e1_extractor"))
import prompt_r2b as P  # noqa: E402

NUEVO = Path(sys.argv[1]).read_text(encoding="utf-8")
LITERALES = Path(sys.argv[2]).read_text(encoding="utf-8")
SALIDA = Path(sys.argv[3])
VIEJO = P.PREFIJO_SISTEMA_R2B
FUNCIONALES = set("""a al algo ante bajo cada como con contra cual cuando de del desde donde e el ella ello en entre es esa
ese eso esta este esto la las le les lo los más mas mismo muy ni no o os para pero por que qué se si sí sin sobre su sus
también tan tanto te todo todos toda todas u un una uno unos unas y ya será serán ser son está están haya hayan""".split())
DIEZ = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FUERA = ("ayccef", "expaef", "opefci", "adrei")
E0 = REPO / "data/experiment/reextraccion_v2/e0_chunking"
FUENTES = ([E0 / "salida_tanda0" / f"chunks_{t}.json" for t in DIEZ]
           + [E0 / "salida_tanda0_r2" / f"chunks_{t}.json" for t in DIEZ]
           + [REPO / f"data/experiment/segmentacion_84/b584_particion/{t}/chunks_{t}.json" for t in FUERA])
CONTROL = {
    # de P1 (p1/nofiltracion.py)
    "cap::1.2", "ric::9.2.1", "cla::5.1.1.1", "pro::1.1.2.5", "cap::6.2.2.6", "docvig::3.3::cierre",
    "ctacte::7.3.1.5", "ctacte::8.3::intro", "ctacte::8.4::intro", "lingob::2.3.2.2", "ayccef::4.2.7.2",
    "expaef::6.6.2", "ayccef::3.4.1", "expaef::1.1.2.5", "adrei::4.3.1::intro", "adrei::4.3.1.1", "adrei::4.3.1.2",
    "adrei::4.3.1.3", "ctacte::6.4.7::intro",
    # caso fijo nuevo de P4 (nota del 04/10/2026)
    "cla::5.1.1::intro",
    # hallazgos que atiende el parche (reports/u_revision_libre/freno_a.md y freno_a1.md)
    "lingob::2.1.2", "lingob::2.1.1", "pagjub::2.9.2", "ctacte::6.5.1", "pro::3.2.1.3", "ext::2.2.1", "pro::3.1.6",
    "cla::3.4.4", "cap::8.5.1", "cap::8.5.2", "cap::8.5.3", "pro::4.2.1::intro", "cap::2.7.2::intro", "lingob::6.1",
    "ctacte::12.10.2", "cla::6.3.3", "cap::12.3"}


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


v_viejo = toks(VIEJO)
textos = {"prefijo": toks(NUEVO), "literales_mensaje_y_nota_e3": toks(LITERALES)}
agregadas5 = {k: ngramas(v, 5) - ngramas(v_viejo, 5) for k, v in textos.items()}
agregadas23 = {k: (ngramas(v, 2) | ngramas(v, 3)) - (ngramas(v_viejo, 2) | ngramas(v_viejo, 3))
               for k, v in textos.items()}
choques = {k: {} for k in textos}
control_toks: dict[str, list[str]] = {}
n = 0
for p in FUENTES:
    for c in chunks_de(p):
        n += 1
        tk = toks(texto_chunk(c))
        g5 = ngramas(tk, 5)
        for k in textos:
            for w in g5 & agregadas5[k]:
                choques[k].setdefault(" ".join(w), set()).add(c["id"])
        if c["id"] in CONTROL:
            control_toks.setdefault(c["id"], tk)
dist = {k: {} for k in textos}
for cid, tk in sorted(control_toks.items()):
    g = {w for w in (ngramas(tk, 2) | ngramas(tk, 3)) if sum(x not in FUNCIONALES for x in w) >= 2}
    for k in textos:
        inter = sorted(" ".join(w) for w in g & agregadas23[k])
        if inter:
            dist[k][cid] = inter
res = {"chunks_controlados": n, "fuentes": [str(p.relative_to(REPO)) for p in FUENTES],
       "ventanas5_agregadas": {k: len(v) for k, v in agregadas5.items()},
       "choques_ventana5": {k: {w: sorted(ids)[:8] for w, ids in sorted(v.items())} for k, v in choques.items()},
       "n_choques": {k: len(v) for k, v in choques.items()},
       "control_no_encontrados": sorted(CONTROL - set(control_toks)),
       "bi_trigramas_de_control_en_texto_agregado": dist}
SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k not in ("fuentes",)}, ensure_ascii=False, indent=1)[:6000])
