"""U-ESTUDIO-MATRIZ — carga común (solo lectura, sin API).

Lee la salida de la tanda 0 (salida_dirigida, la entrada declarada de
ens_desarrollo/r1), los chunks de E0 (salida_tanda0), la caché de reintentos
de E1 (immutable=1) y el grafo KG-Tanda0-Desarrollo-r1. No escribe nada.
"""
from __future__ import annotations

import dataclasses
import hashlib
import json
import sqlite3
import sys
from pathlib import Path

REPO = Path("/Users/agustinavidelarivero/INGENIERIA IA/TESIS/bcra-regulatory-kg")
EXP = REPO / "data" / "experiment"
REX = EXP / "reextraccion_v2"
for _p in (REX / "e1_extractor", REX / "e3_verificador", EXP / "esq" / "code",
           EXP / "grafo_v2" / "code"):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import comun_e1  # noqa: E402,F401  (wiring de sys.path de E1)
import perfil_e1  # noqa: E402
import validador_e1  # noqa: E402
import prompt_congelado as pc  # noqa: E402

SALIDA = REX / "corpus_tanda0" / "salida_dirigida"
E0 = REX / "e0_chunking" / "salida_tanda0"
DB_REINT = REX / "e3_verificador" / "cache" / "e1_reintentos.db"
NS_E1 = "e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0"
KG_DEV = REX / "corpus_tanda0" / "ens_desarrollo" / "r1" / "kg.json"
KG_DEV_SHA = "eab2fdd01dec4dad026d596a793919e666920fab127d7efb14b5b00857ae64ef"
AUDIT = REPO / "reports" / "u_audit_tipos_v3"
TOS_10 = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
TOS_DEV = ("pro", "cla", "ric", "cap", "ext")
MARCA_REINTENTO = "# REINTENTO DE EXTRACCIÓN — feedback del verificador de completitud (E3)"


def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def leer_jsonl(p: Path) -> list[dict]:
    with open(p, encoding="utf-8") as f:
        return [json.loads(ln) for ln in f if ln.strip()]


def perfil_v3():
    return perfil_e1.perfil("v3_b54")


def esquema_ampliado(extra: dict[str, tuple[set, set]]):
    """Copia EN MEMORIA de la matriz congelada con tipos agregados al dominio
    y/o rango de algunos predicados. prompt_congelado no se modifica: se
    parte de DOMAIN_RANGE_CONGELADO y se arma un dict nuevo."""
    dr = {p: (set(d), set(r)) for p, (d, r) in pc.DOMAIN_RANGE_CONGELADO.items()}
    for p, (dom_add, ran_add) in extra.items():
        dr[p][0].update(dom_add)
        dr[p][1].update(ran_add)

    def firma(s, p, t):
        if p not in dr:
            return False
        d, r = dr[p]
        return s in d and t in r

    base = perfil_v3().esquema
    return dataclasses.replace(base, firma_valida=firma), dr


def cargar_chunks(to: str) -> list[dict]:
    return json.loads((E0 / f"chunks_{to}.json").read_text(encoding="utf-8"))


def texto_completo(chunk: dict) -> str:
    """Texto completo del fragmento tal como lo define E0 (e0_lib: herencia
    unida por saltos de línea + texto propio); se verifica contra
    sha256_completo."""
    th = "\n".join(h["texto"] for h in chunk.get("herencia", []))
    completo = (th + "\n" + chunk["texto"]) if th else chunk["texto"]
    if hashlib.sha256(completo.encode("utf-8")).hexdigest() != chunk["sha256_completo"]:
        raise RuntimeError(f"texto completo no reproduce sha256_completo: {chunk['id']}")
    return completo


def filas_reintentos() -> list[dict]:
    con = sqlite3.connect(f"file:{DB_REINT}?mode=ro&immutable=1", uri=True)
    out = []
    for key, req, raw in con.execute(
            "SELECT key, request_json, raw_json FROM cache WHERE namespace=? ORDER BY key", (NS_E1,)):
        req = json.loads(req)
        raw = json.loads(raw)
        tool_input = None
        for b in raw.get("content", []):
            if b.get("type") == "tool_use":
                tool_input = b.get("input")
                break
        out.append({"key": key, "mensaje": req["messages"][0]["content"], "tool_input": tool_input})
    con.close()
    return out
