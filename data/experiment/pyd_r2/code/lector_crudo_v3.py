"""
lector_crudo_v3.py — U-PYD, etapa P2: lectura del crudo guardado de E1 (perfil
v3 de la tanda 0 y perfil de desarrollo de r1) para re-validarlo con el perfil
r2.

Capas (las de N1, reports/u_listas_nomap/u_listas_n1.py, R-CAPAS):
  - L0: primer intento de E1, `extracciones_e1_compact.jsonl`, campo
    `tool_input_crudo`;
  - L0r: reintentos de E3, `e3_verificador/cache/e1_reintentos.db`, abierta solo
    con `file:…?immutable=1`; cada entrada se asigna a su chunk por «TO:» y
    «Punto del chunk:» o «MINI-CHUNK de bloque estructural (<bloque> del punto
    <u>)» del mensaje de usuario, con el id verificado contra E0 (misma regla
    que N1, u_listas_n1.py:568-610).

Rutas y sha256: los de `entradas` de n1_inventario.json, leído en el commit de
la firma del mandato (`git show 3ffb99d:…`, candado de sha256; CLAUDE.md §4.k).
Todo archivo cuyo sha256 no coincide frena la lectura.

La lectura en la forma r2 (sujeto_propuesto como mención; cada cadena de
omisiones_no_prosa como omisión sin categoría ni tramo) la hace
`validador_r2.desde_v3`, que la corrida aplica con `forma="v3"`.

Solo lectura: no escribe nada. Sin API.
"""

from __future__ import annotations

import hashlib
import json
import re
import sqlite3
import subprocess
import sys
import urllib.parse
from collections import OrderedDict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import modelos_r2 as M  # noqa: E402

REPO = M.REPO
COMMIT_MANDATO = "3ffb99d"  # firma del mandato U-PYD
N1_RUTA = "reports/u_listas_nomap/n1_inventario.json"
N1_SHA256 = "ada70bfe80295618b53af10277a6e600e31a48ac2837bf1b7f6636dce0d128a0"

TOS_R1 = ("cap", "cla", "ext", "pro", "ric")
TOS_DEV = ("cap", "cla", "ext", "pro", "ric")
TOS_CINCO = ("ctacte", "docvig", "lingob", "pagjub", "polcre")
TOS_DIEZ = tuple(sorted(TOS_DEV + TOS_CINCO))

# Generaciones y grupos: los de N1 (u_listas_n1.py:136-159).
GEN = OrderedDict([
    ("r1", {"prefijo_entrada": "r1", "tos": TOS_R1, "perfil": "produccion_dev",
            "ns": "e1_extraccion|cv=e1-extractor-v1-p4793d6152608|think=0"}),
    ("t0", {"prefijo_entrada": "t0", "tos": TOS_DIEZ, "perfil": "v3_b54",
            "ns": "e1_extraccion|cv=e1-extractor-v1-p54a111e2175f|think=0"}),
])
GRUPOS = OrderedDict([
    ("r1", {"gen": "r1", "tos": TOS_R1}),
    ("desarrollo", {"gen": "t0", "tos": TOS_DEV}),
    ("cinco", {"gen": "t0", "tos": TOS_CINCO}),
    ("diez", {"gen": "t0", "tos": TOS_DIEZ}),
])


class FrenoLectura(SystemExit):
    pass


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git_show(commit: str, ruta: str) -> bytes:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"{commit}:{ruta}"],
                       capture_output=True, check=False)
    if r.returncode != 0:
        raise FrenoLectura(f"no se pudo leer {commit}:{ruta} con git show")
    return r.stdout


def leer_firmado(commit: str, ruta: str, sha: str) -> bytes:
    """Contenido de `ruta` en `commit`, con candado de sha256."""
    b = git_show(commit, ruta)
    s = sha256_bytes(b)
    if s != sha:
        raise FrenoLectura(f"candado: {commit}:{ruta} da {s[:12]}… (esperado {sha[:12]}…)")
    return b


def n1_inventario() -> dict:
    return json.loads(leer_firmado(COMMIT_MANDATO, N1_RUTA, N1_SHA256).decode("utf-8"))


def _leer_jsonl(p: Path) -> list[dict]:
    with open(p, encoding="utf-8") as f:
        return [json.loads(x) for x in f if x.strip()]


class Crudo:
    """El crudo de r1 y de la tanda 0, con sellos de N1."""

    def __init__(self):
        self.n1 = n1_inventario()
        self.entradas = self.n1["entradas"]
        self.sellos: OrderedDict = OrderedDict()
        self.chunks: dict[str, dict] = {}
        for to in TOS_DIEZ:
            for c in json.loads(self._verificado(f"e0_{to}").decode("utf-8")):
                if c["id"] in self.chunks:
                    raise FrenoLectura(f"id de chunk repetido en E0: {c['id']}")
                self.chunks[c["id"]] = c
        self.compact: dict[str, dict[str, list]] = {}
        self.finales: dict[str, dict[str, list]] = {}
        for g, cfg in GEN.items():
            self.compact[g], self.finales[g] = {}, {}
            for to in cfg["tos"]:
                pre = cfg["prefijo_entrada"]
                self.compact[g][to] = [json.loads(x) for x in
                                       self._verificado(f"{pre}_{to}_compact").decode("utf-8").splitlines()
                                       if x.strip()]
                self.finales[g][to] = [json.loads(x) for x in
                                       self._verificado(f"{pre}_{to}_finales").decode("utf-8").splitlines()
                                       if x.strip()]
        self._verificado("e1_reintentos_db", leer=False)
        self.reintentos = self._cargar_reintentos()

    def _verificado(self, clave: str, leer: bool = True) -> bytes:
        e = self.entradas[clave]
        p = REPO / e["ruta"]
        b = p.read_bytes()
        s = sha256_bytes(b)
        if s != e["sha256"]:
            raise FrenoLectura(f"sha256 de {e['ruta']} = {s[:12]}…; N1 declara {e['sha256'][:12]}…")
        self.sellos[clave] = {"ruta": e["ruta"], "sha256": s}
        return b if leer else b""

    def _cargar_reintentos(self) -> dict[str, list[dict]]:
        dbp = (REPO / self.entradas["e1_reintentos_db"]["ruta"]).resolve()
        db = sqlite3.connect(f"file:{urllib.parse.quote(str(dbp))}?immutable=1", uri=True)
        out: dict[str, list[dict]] = {}
        try:
            for g, cfg in GEN.items():
                filas = db.execute("select key, request_json, raw_json from cache where namespace = ? "
                                   "order by key", (cfg["ns"],)).fetchall()
                asignadas = []
                for key, req, raw in filas:
                    msgs = json.loads(req).get("messages") or []
                    c0 = msgs[0]["content"] if msgs else ""
                    u = c0 if isinstance(c0, str) else " ".join(
                        b.get("text", "") for b in c0 if isinstance(b, dict))
                    m_to = re.search(r"^TO: (\S+)$", u, re.M)
                    m_pt = re.search(r"^Punto del chunk: (\S+)", u, re.M)
                    m_mc = re.search(r"MINI-CHUNK de bloque estructural \((\S+) del punto (\S+)\)", u)
                    if not m_to or not (m_pt or m_mc):
                        raise FrenoLectura(f"reintento sin asignar: {key}")
                    to = m_to.group(1)
                    cid = f"{to}::{m_pt.group(1)}" if m_pt else f"{to}::{m_mc.group(2)}::{m_mc.group(1)}"
                    if to not in cfg["tos"] or cid not in self.chunks:
                        raise FrenoLectura(f"reintento fuera del corpus o del E0: {key} → {cid}")
                    msg = json.loads(raw)
                    tis = [b.get("input") for b in (msg.get("content") or [])
                           if isinstance(b, dict) and b.get("type") == "tool_use"]
                    asignadas.append({"key": key, "chunk_id": cid, "to": to,
                                      "tool_input": tis[0] if tis else None})
                out[g] = asignadas
        finally:
            db.close()
        return out

    def registros(self, grupo: str, capa: str) -> list[dict]:
        """Registros de un grupo y una capa, en orden estable: por TO (orden del
        grupo) y, dentro, el del archivo (L0) o el de la clave de la db (L0r).
        Cada uno: {to, chunk_id, tool_input, origen, error}."""
        cfg = GRUPOS[grupo]
        g = cfg["gen"]
        out = []
        if capa == "L0":
            for to in cfg["tos"]:
                for r in self.compact[g][to]:
                    out.append({"to": to, "chunk_id": r["chunk_id"], "tool_input": r.get("tool_input_crudo"),
                                "validacion_v3": r.get("validacion"), "error": r.get("error"),
                                "origen": "compact"})
        elif capa == "L0r":
            por_to: dict[str, list] = {}
            for a in self.reintentos[g]:
                por_to.setdefault(a["to"], []).append(a)
            for to in cfg["tos"]:
                for a in por_to.get(to, []):
                    out.append({"to": to, "chunk_id": a["chunk_id"], "tool_input": a["tool_input"],
                                "validacion_v3": None, "error": None, "origen": a["key"]})
        else:
            raise ValueError(capa)
        return out
