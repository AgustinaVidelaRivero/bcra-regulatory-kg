"""U-NOSEG-LIMITE, L4 — complemento de l4_citas_189.py: menciones léxicas de los títulos de los 14 TOs
fuera de las tandas en el texto de E0 (e0-r2) de los diez TOs de la tanda 0. No son citas del detector
de remisiones: un chunk cuenta si su texto propio contiene la frase distintiva del título (normalizada:
minúsculas, sin acentos, cortes con guion unidos). Escribe `l4_menciones_14.json`.

Uso: PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l4_menciones_14.py
"""
import json
import re
import unicodedata
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
E0 = REPO / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida_tanda0_r2"
OUT = REPO / "data" / "experiment" / "no_segmentables_limite"
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
FRASES = {
    "manual": "manual de cuentas",
    "ri2_pm": "casas y agencias de cambio - plan y manual",
    "plandecuentas": "plan de cuentas",
    "optico": "presentacion de informaciones al",
    "ri_chr": "cheques rechazados",
    "ri_con": "estado de consolidacion de entidades locales",
    "ri_fcem": "regimen informativo de facturas de credito",
    "ri_itme": "tenencias en moneda extranjera de casas",
    "ri_pfmipyme": "regimen informativo de plataformas",
    "ri_pscpp": "ri-pscpp",
    "ri_pspii": "proveedores de servicios de pago - informacion contable",
    "ri_rem": "pago de remuneraciones mediante acreditacion",
    "ri_spi": "seguimiento de pagos de importaciones",
    "ri_tii": "transferencias inmediatas intraentidades",
}


def norm(s):
    s = re.sub(r"-\n", "", s or "")
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c)).replace("–", "-")
    return re.sub(r"\s+", " ", s)


res = {}
for t14, frase in FRASES.items():
    por_to = {}
    for to in TOS:
        ch = json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))
        ch = ch["chunks"] if isinstance(ch, dict) else ch
        ids = [c["id"] for c in ch if frase in norm(c["texto"])]
        if ids:
            por_to[to] = ids
    res[t14] = {"frase": frase, "chunks": sum(len(v) for v in por_to.values()), "por_to": por_to}
(OUT / "l4_menciones_14.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for k, v in res.items():
    print(k, v["chunks"], {t: len(i) for t, i in v["por_to"].items()})
