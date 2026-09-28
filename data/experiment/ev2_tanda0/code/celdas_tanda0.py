"""
celdas_tanda0.py — U-TANDA0-2A E5: registro de las celdas C2-C5 de EV2 de la
tanda 0 y todo lo que el protocolo de C1 parametriza por celda (pre-registro
docs/preregistro_tanda0.md A3.1; enmienda a551c57 §2.3; mandato U-TANDA0-2A
decisión 4).

Qué fija por celda (y por qué no reusa las constantes de comun_r1): grafo,
backend, label de la corrida base, sha del kg.json, conjunto de preguntas,
orden del agente, sales y prefijos de ids opacos, semillas del orden ciego del
juez y de la auditoría del §7, labels y prefijos de las dbs del juez y del
§7. comun_r1 cablea todo eso a r1 (comun_r1.py, constantes de módulo), y
juez_r1 / enc_r1 lo leen de ahí; las celdas nuevas necesitan valores propios
("ids opacos con sal propia por celda", mandato decisión 4).

Qué reutiliza por import (sin editar): comun_r1 (registra r1 en memoria;
casos_fidelidad_r1 = los 40 casos de EV2 en el orden sellado de C1; gold
esperado), comun_tanda0 (instrumento 9: vista runtime de los grafos de la tanda
0), runner_ev2.correr_grafo (backend en memoria, celdas C3 y C5),
runner_ev2_neo4j.correr_grafo (backend Neo4j fulltext, celdas C2 y C4),
comun_fidelidad (gold de EV2, vista ciega, marcadores) y juez_r1.MARCADORES.

Orden del agente por celda:
  - C2, C3, C4: los 40 casos de fidelidad de EV2 en el orden de C1
    (comun_r1.casos_fidelidad_r1, semilla orden-ev2-r1), para que los pares
    C1-C2, C1-C3 y C2-C4 comparen las mismas preguntas en el mismo orden.
  - C5: las 20 preguntas del archivo sellado preguntas_tanda0.json (fd03a0f)
    en el orden del archivo (T0F-001 a T0F-020). El archivo no declara otra
    semilla de orden de corrida; si la autora fija otra, se cambia acá antes
    de gastar.

Rutas (mandato decisión 10): trazas, juez_out y cache bajo
data/experiment/ev2_tanda0/. Toda función recibe un objeto Rutas: el selftest
las redirige a un directorio temporal.

Corrida base: C2 y C4 corren con la CLI del gate 4 (runner_ev2_neo4j.py,
mandato E5.b); C3 y C5, con `correr_base` de este módulo, que llama
runner_ev2.correr_grafo sobre el grafo registrado en memoria y anota cada
traza con meta.tanda0 (runner_ev2 escribe meta.semilla_orden = orden-ev2-v1 y
meta.unidad = ev2_corrida, campos heredados; precedente de la anotación
meta.u_b18 de C1).
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent                  # ev2_tanda0/code
TANDA0_DIR = CODE_DIR.parent                                # data/experiment/ev2_tanda0
EXP_DIR = TANDA0_DIR.parent                                 # data/experiment
REPO_DIR = EXP_DIR.parent.parent
TANDA0_CODE = EXP_DIR / "tanda0" / "code"

for _p in (CODE_DIR, TANDA0_CODE):
    if str(_p) not in sys.path:
        sys.path.insert(0, str(_p))

import runner_ev2_neo4j as rn               # noqa: E402  (arma sys.path; importa comun_r1)
import comun_r1 as cr                       # noqa: E402  (registra r1 en memoria)
import comun_tanda0 as ct                   # noqa: E402  (registra la tanda 0 en memoria)
import runner_ev2 as rv                     # noqa: E402  (runner base, sin editar)
import juez_r1 as jr                        # noqa: E402  (marcadores)
from comun_r1 import cf                     # noqa: E402  (gold EV2, vista ciega)
import grafos as G                          # noqa: E402  (registro de Neo4j)

PREGUNTAS_C5 = TANDA0_DIR / "preguntas" / "preguntas_tanda0.json"
SHA_PREGUNTAS_C5 = "b36e0662170004a5e1adfcf7ea26e91ba45a469dbbda058aac3a47f4c0cc3743"
COMMIT_PREGUNTAS_C5 = "fd03a0f"
N_PREGUNTAS_C5, N_CRITERIOS_C5 = 20, 60

# Criterios de C5 sin cita textual: las dos preguntas de abstención (T0F-008,
# T0F-013) tienen criterios que afirman una AUSENCIA en la norma y no traen
# cita (registro_generacion_tanda0.md). EV2 no tiene ninguno y
# comun_fidelidad.cargar_gold los rechaza; el juez v1 congelado los recibiría
# como «Cita textual de la norma: «»». Se aceptan SOLO los declarados acá por
# decisión de la autora (FRENO interno de E5.a, 28/09/2026: opción (a), pasan al
# juez tal como están sellados; el gold no se toca). Quedan fuera del dominio de
# calibración del juez: el reporte de E5 los marca y lista sus veredictos aparte.
CRITERIOS_CITA_VACIA_AUTORIZADOS: frozenset = frozenset({
    ("T0F-008", 1), ("T0F-008", 3), ("T0F-013", 1)})

REPS_JUEZ = cr.REPS_JUEZ                    # 3 (protocolo de C1)
REPS_AGENTE_ENC = cr.REPS_AGENTE_ENC        # 3
MODO_NEO4J = "fulltext"


def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def rel_repo(p: Path) -> str:
    p = Path(p).resolve()
    try:
        return str(p.relative_to(REPO_DIR))
    except ValueError:
        return str(p)


# --------------------------------------------------------------------------- #
# Celdas                                                                      #
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class Celda:
    id: str                 # "C2" ... "C5"
    backend: str            # "neo4j" | "memoria"
    grafo: str              # clave de grafos.py (neo4j) o de comun_ev2.GRAFOS (memoria)
    label: str              # label de la corrida base del agente
    kg_sha256: str
    conjunto: str           # "ev2" (40 preguntas) | "tanda0" (20 preguntas nuevas)

    @property
    def c(self) -> str:
        return self.id.lower()

    # ids opacos y semillas (sal propia por celda)
    @property
    def sal_base(self) -> str:
        return f"juez-ev2-tanda0-{self.c}"

    @property
    def sal_enc(self) -> str:
        return f"juez-ev2-tanda0-{self.c}-enc"

    @property
    def prefijo_base(self) -> str:
        return f"T0{self.id}B-"

    @property
    def prefijo_enc(self) -> str:
        return f"T0{self.id}E-"

    @property
    def semilla_orden_juez(self) -> str:
        return f"juez-ev2-tanda0-{self.c}"

    @property
    def semilla_orden_juez_enc(self) -> str:
        return f"juez-ev2-tanda0-{self.c}-enc"

    @property
    def semilla_auditoria(self) -> str:
        return f"auditoria-ev2-tanda0-{self.c}"

    @property
    def semilla_orden_agente(self) -> str | None:
        return cr.SEMILLA_ORDEN_R1 if self.conjunto == "ev2" else None

    # labels y dbs
    def label_juez(self, rep: int) -> str:
        return f"{self.label}_juez_r{rep}"

    @property
    def db_prefix_juez(self) -> str:
        return f"{self.label}_juez"

    def label_enc(self, rep: int) -> str:
        return f"{self.label}_enc_r{rep}"

    def label_juez_enc(self, rep: int) -> str:
        return f"{self.label}_enc_juez_r{rep}"

    @property
    def db_prefix_juez_enc(self) -> str:
        return f"{self.label}_enc_juez"


CELDAS = {
    "C2": Celda("C2", "neo4j", "KG_Reextraido_r1", "ev2_c2_r1_neo4j",
                G.GRAFOS["KG_Reextraido_r1"]["sha256"], "ev2"),
    "C3": Celda("C3", "memoria", "tanda0_ens_desarrollo", "ev2_c3_dev_mem",
                ct.TANDA0["tanda0_ens_desarrollo"]["sha256"], "ev2"),
    "C4": Celda("C4", "neo4j", "KG_Tanda0_Desarrollo_r1", "ev2_c4_dev_neo4j",
                G.GRAFOS["KG_Tanda0_Desarrollo_r1"]["sha256"], "ev2"),
    "C5": Celda("C5", "memoria", "tanda0_ens_diez", "ev2_c5_diez_mem",
                ct.TANDA0["tanda0_ens_diez"]["sha256"], "tanda0"),
}


def kg_path(celda: Celda) -> Path:
    return G.GRAFOS[celda.grafo]["path"] if celda.backend == "neo4j" \
        else ct.TANDA0[celda.grafo]["path"]


# --------------------------------------------------------------------------- #
# Rutas                                                                       #
# --------------------------------------------------------------------------- #
@dataclass(frozen=True)
class Rutas:
    base: Path

    @property
    def trazas(self) -> Path:
        return self.base / "trazas"

    @property
    def cache(self) -> Path:
        return self.base / "cache"

    @property
    def juez_out(self) -> Path:
        return self.base / "juez_out"

    def celda(self, celda: Celda) -> Path:
        return self.juez_out / celda.id

    def sub(self, celda: Celda, nombre: str) -> Path:
        """base/, enc/, orden/, desanonimizacion_SOLO_MESA/, poblacion/, reporte/, sellos/"""
        return self.celda(celda) / nombre


RUTAS = Rutas(TANDA0_DIR)


# --------------------------------------------------------------------------- #
# Casos y gold                                                                #
# --------------------------------------------------------------------------- #
def cargar_preguntas_c5() -> list[dict]:
    sha = sha256_path(PREGUNTAS_C5)
    if sha != SHA_PREGUNTAS_C5:
        raise RuntimeError(f"preguntas de C5 alteradas: {sha} != {SHA_PREGUNTAS_C5}")
    ps = json.loads(PREGUNTAS_C5.read_text(encoding="utf-8"))["preguntas"]
    if len(ps) != N_PREGUNTAS_C5 or len({p["id"] for p in ps}) != N_PREGUNTAS_C5:
        raise ValueError(f"se esperaban {N_PREGUNTAS_C5} preguntas únicas en C5: {len(ps)}")
    return ps


def casos_celda(celda: Celda) -> tuple[list[dict], dict]:
    """(casos en orden, fuente). Casos {caso_id, eje, pregunta, pos_orden_global}."""
    if celda.conjunto == "ev2":
        casos = cr.casos_fidelidad_r1()
        return casos, {"origen": "comun_r1.casos_fidelidad_r1 (orden sellado de C1)",
                       "semilla_orden": cr.SEMILLA_ORDEN_R1, "n": len(casos)}
    ps = cargar_preguntas_c5()
    casos = [{"caso_id": p["id"], "eje": "fidelidad", "pregunta": p["pregunta"],
              "pos_orden_global": i} for i, p in enumerate(ps, 1)]
    return casos, {"origen": rel_repo(PREGUNTAS_C5), "sha256": SHA_PREGUNTAS_C5,
                   "commit": COMMIT_PREGUNTAS_C5, "semilla_orden": None,
                   "regla_orden": "orden del archivo sellado (T0F-001 a T0F-020)",
                   "n": len(casos)}


def criterios_cita_vacia() -> list[tuple[str, int]]:
    """(id_pregunta, índice 1..K) de los criterios de C5 con cita_textual vacía."""
    return [(p["id"], j) for p in cargar_preguntas_c5()
            for j, c in enumerate(p["gold"]["criterios"], 1) if not c["cita_textual"].strip()]


def cargar_gold_celda(celda: Celda, autorizados: frozenset | None = None) -> dict[str, dict]:
    """{id_pregunta: {pregunta, criterios[{criterio, cita_textual}], to}} — mismo
    formato que comun_fidelidad.cargar_gold (EV2: 40 / 164, candado propio). En
    C5, un criterio sin cita solo se acepta si (id_pregunta, índice) está en
    `autorizados` (default CRITERIOS_CITA_VACIA_AUTORIZADOS)."""
    if celda.conjunto == "ev2":
        return cf.cargar_gold()
    autorizados = CRITERIOS_CITA_VACIA_AUTORIZADOS if autorizados is None else autorizados
    out, no_autorizados = {}, []
    for p in cargar_preguntas_c5():
        crits = [{"criterio": c["criterio"], "cita_textual": c["cita_textual"]}
                 for c in p["gold"]["criterios"]]
        for j, c in enumerate(crits, 1):
            if not c["criterio"].strip():
                raise ValueError(f"{p['id']} criterio {j}: criterio vacío")
            if not c["cita_textual"].strip() and (p["id"], j) not in autorizados:
                no_autorizados.append((p["id"], j))
        out[p["id"]] = {"pregunta": p["pregunta"], "criterios": crits, "to": p["to"]}
    if no_autorizados:
        raise ValueError(f"C5: criterios sin cita textual no autorizados {no_autorizados} "
                         "(decisión de la autora pendiente: CRITERIOS_CITA_VACIA_AUTORIZADOS)")
    n_crit = sum(len(v["criterios"]) for v in out.values())
    if len(out) != N_PREGUNTAS_C5 or n_crit != N_CRITERIOS_C5:
        raise ValueError(f"gold de C5 inesperado: {len(out)} preguntas / {n_crit} criterios")
    return out


# --------------------------------------------------------------------------- #
# Ids opacos y marcadores de ceguera                                          #
# --------------------------------------------------------------------------- #
def id_opaco_base(celda: Celda, id_pregunta: str, sha_resp: str) -> str:
    return celda.prefijo_base + sha256_texto(
        f"{celda.sal_base}|{id_pregunta}|{celda.grafo}|{sha_resp}")[:10]


def id_opaco_enc(celda: Celda, id_pregunta: str, rep: int, sha_resp: str) -> str:
    return celda.prefijo_enc + sha256_texto(
        f"{celda.sal_enc}|{id_pregunta}|{celda.grafo}|{rep}|{sha_resp}")[:10]


def marcadores_celda(celda: Celda) -> list[str]:
    """Lo que jamás puede aparecer en un input del juez de esta celda: los de la
    base y de r1 (juez_r1.MARCADORES) más label, grafo, sha, prefijos de ids y
    de preguntas, y los nombres internos de la tanda 0."""
    return list(jr.MARCADORES) + [
        celda.label, celda.grafo, celda.kg_sha256[:12], "ev2_tanda0",
        celda.prefijo_base, celda.prefijo_enc, "EV2F-", "T0F-",
        "id_opaco", "respondible"]


# --------------------------------------------------------------------------- #
# Trazas                                                                      #
# --------------------------------------------------------------------------- #
def cargar_respuestas(celda: Celda, trazas_dir: Path, label: str,
                      esperados: list[str], estricto: bool = True) -> tuple[list[dict], list[dict]]:
    """Una entrada por traza esperada (patrón juez_r1.cargar_respuestas_r1,
    parametrizado por celda): exige meta.label, meta.grafo y meta.kg_sha256 de
    la celda, eje fidelidad y caso_id = qid = nombre de archivo. Con
    estricto=True (corrida base) levanta ante cualquier faltante o traza sin
    respuesta parseada; con estricto=False (§7) los devuelve como faltantes."""
    xs, faltantes = [], []
    for qid in esperados:
        f = Path(trazas_dir) / f"{rv._sanitizar(qid)}.json"
        if not f.exists():
            faltantes.append({"id_pregunta": qid, "motivo": "traza inexistente"})
            continue
        t = json.loads(f.read_text(encoding="utf-8"))
        m, tr = t["meta"], t["trace"]
        fj = tr.get("final_json") or {}
        if m["eje"] != "fidelidad" or m["label"] != label or m["grafo"] != celda.grafo \
                or m["kg_sha256"] != celda.kg_sha256:
            raise ValueError(f"{f}: meta inesperada (label/grafo/sha/eje)")
        if m["caso_id"] != tr["qid"] or m["caso_id"] != qid:
            raise ValueError(f"{f}: caso_id/qid/nombre inconsistentes")
        if not tr.get("parse_ok") or not isinstance(fj.get("respuesta"), str) \
                or not fj["respuesta"].strip():
            faltantes.append({"id_pregunta": qid,
                              "motivo": f"sin respuesta parseada (error={tr.get('error')})"})
            continue
        xs.append({"id_pregunta": qid, "respuesta": fj["respuesta"],
                   "respondible_flag": fj.get("respondible"),
                   "pregunta_traza": t["pregunta"]})
    if estricto and faltantes:
        raise ValueError(f"{celda.id}: {len(faltantes)} trazas faltantes o sin respuesta "
                         f"en {trazas_dir}: {faltantes[:5]}")
    return xs, faltantes


def _modelos_api(raw_turns: list[dict]) -> list[str]:
    return sorted({(t.get("raw") or {}).get("model") for t in raw_turns} - {None})


def anotar_trazas(celda: Celda, outdir: Path, fuente: dict, clave: str, extra: dict) -> int:
    """Agrega meta[clave] a cada traza del directorio (idempotente). Para el
    backend en memoria agrega además model_segun_api desde raw_turns_agent
    (el runner de Neo4j ya lo escribe en meta)."""
    n = 0
    for f in sorted(Path(outdir).glob("*.json")):
        if f.name.startswith(("resumen_", "corrida_")):
            continue
        t = json.loads(f.read_text(encoding="utf-8"))
        if clave in t["meta"]:
            continue
        t["meta"][clave] = {
            "unidad": "U-TANDA0-2A E5", "celda": celda.id, "backend": celda.backend,
            "semilla_orden_real": fuente.get("semilla_orden"),
            "regla_orden": fuente.get("regla_orden") or fuente.get("origen"),
            "model_segun_api": _modelos_api(t.get("raw_turns_agent") or []),
            "nota": ("meta.semilla_orden y meta.unidad son campos heredados del runner "
                     "base (runner_ev2); el orden real es semilla_orden_real/regla_orden"),
            **extra}
        f.write_text(json.dumps(t, ensure_ascii=False, indent=2), encoding="utf-8")
        n += 1
    return n


def hits_db(p: Path) -> int:
    import sqlite3
    if not Path(p).exists():
        return 0
    conn = sqlite3.connect(str(p))
    n = sum(int(v or 0) for (v,) in conn.execute("SELECT hit FROM access_log"))
    conn.close()
    return n


# --------------------------------------------------------------------------- #
# Corrida del agente (base o §7) — despacho por backend                       #
# --------------------------------------------------------------------------- #
def correr_agente(celda: Celda, *, label: str, casos: list[dict], fuente: dict,
                  rutas: Rutas, client_real, estado_gasto: dict, indice=None) -> dict:
    """Corre `casos` (N=1) con el backend de la celda, db cache/<label>.db y
    trazas en trazas/<label>/. `indice` (Neo4jIndex) es obligatorio en neo4j."""
    outdir = rutas.trazas / label
    db = rutas.cache / f"{label}.db"
    outdir.mkdir(parents=True, exist_ok=True)
    if celda.backend == "memoria":
        return rv.correr_grafo(celda.grafo, client_real=client_real, db_path=db,
                               label=label, casos=casos, outdir=outdir,
                               estado_gasto=estado_gasto)
    if indice is None:
        raise ValueError(f"{celda.id}: el backend neo4j exige un Neo4jIndex")
    return rn.correr_grafo(celda.grafo, modo=MODO_NEO4J, label=label,
                           client_real=client_real, indice=indice, db_path=db,
                           outdir=outdir, casos=casos, fuente_casos=fuente,
                           estado_gasto=estado_gasto)


def correr_base(celda: Celda, *, rutas: Rutas, client_real, tope: float, indice=None) -> dict:
    """Corrida base de la celda (retomable: saltea los casos con traza)."""
    casos, fuente = casos_celda(celda)
    outdir = rutas.trazas / celda.label
    pend = [c for c in casos if not (outdir / f"{rv._sanitizar(c['caso_id'])}.json").exists()]
    estado = {"gastado": 0.0, "corridos": 0, "total": len(pend), "tope_usd": tope}
    resumen = None
    if pend:
        resumen = correr_agente(celda, label=celda.label, casos=pend, fuente=fuente,
                                rutas=rutas, client_real=client_real,
                                estado_gasto=estado, indice=indice)
    n_anot = anotar_trazas(celda, outdir, fuente, "tanda0", {"etapa": "base"}) \
        if celda.backend == "memoria" else 0
    return {"celda": celda.id, "label": celda.label, "n_casos": len(casos),
            "n_pendientes": len(pend), "estado_gasto": estado, "resumen": resumen,
            "trazas_anotadas": n_anot, "hits_db": hits_db(rutas.cache / f"{celda.label}.db")}


def main() -> int:
    ap = argparse.ArgumentParser(description="Corrida base del agente para las celdas en "
                                             "memoria de la tanda 0 (C3, C5). C2 y C4 corren "
                                             "con runner_ev2_neo4j.py.")
    ap.add_argument("--celda", required=True, choices=["C3", "C5"])
    ap.add_argument("--autorizado-fase-b", action="store_true")
    ap.add_argument("--tope", type=float, default=None, help="tope USD de ESTA corrida")
    args = ap.parse_args()
    if not args.autorizado_fase_b or args.tope is None:
        print("ABORTADO: el modo real exige --autorizado-fase-b y --tope <USD>. Nada se llamó.")
        return 2
    celda = CELDAS[args.celda]
    sellos = rn.verificar_sellos(verbose=True)
    print(f"  sha256 OK  {celda.grafo}: {sha256_path(kg_path(celda))} (esperado {celda.kg_sha256})")
    if sha256_path(kg_path(celda)) != celda.kg_sha256:
        raise RuntimeError("kg.json de la celda alterado")
    res = correr_base(celda, rutas=RUTAS, client_real=rv._real_client(), tope=args.tope)
    if rn.verificar_sellos() != sellos:
        raise RuntimeError("sellos cambiaron durante la corrida")
    rep_dir = RUTAS.sub(celda, "reporte")
    rep_dir.mkdir(parents=True, exist_ok=True)
    (rep_dir / f"corrida_base_{celda.label}.json").write_text(
        json.dumps({"ts": datetime.now().isoformat(timespec="seconds"), **res},
                   ensure_ascii=False, indent=2, default=str), encoding="utf-8")
    e = res["estado_gasto"]
    frenado = e["corridos"] < res["n_pendientes"]
    print(f"{celda.id}: corridos {e['corridos']}/{res['n_pendientes']} pendientes | "
          f"gasto ${e['gastado']:.4f} | hits db {res['hits_db']}"
          + (" | FRENADO POR PROYECCIÓN" if frenado else ""), flush=True)
    return 1 if frenado else 0


if __name__ == "__main__":
    raise SystemExit(main())
