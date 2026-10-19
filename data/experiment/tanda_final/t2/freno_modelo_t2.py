"""
freno_modelo_t2.py — B6.1, tanda final, T2: el freno por id de modelo (pre-registro firmado de la tanda final, §2, que
sigue al de la tanda 1, §2: «la corrida frena si una llamada de E1 devuelve un id distinto de claude-haiku-4-5-20251001»).
Es el de la tanda 1 (data/experiment/tanda1/t2/freno_modelo_t2.py), con este encabezado y sin otro cambio. El código sellado no lo tiene: lo
hace este script, con el runner detenido. USD 0, sin red.

Qué hace:
  1. copia las tres bases del runner, con sus `-wal` y `-shm` si existen, a una sola copia de trabajo fuera del repo
     (--trabajo), pisando la anterior: `e1_extractor/cache/e1_extraccion.db` (E1), `e3_verificador/cache/
     e1_reintentos.db` (los reintentos de E1 de la fase de E3) y `e3_verificador/cache/e3_verificacion.db` (E3).
     Las bases del repo solo se copian: no se abren ni se escriben en su lugar;
  2. en la copia, las filas de un TO son las de `access_log` con `run_label` igual a `corpus_<TO>_e1`,
     `corpus_<TO>_reintentos_e1` y `corpus_<TO>_e3` (runner_corpus.py:1409, :1433, :1430), cruzadas por `key` con
     `cache.model`, que es el id de la respuesta (llm_cache.py:133-157, :316);
  3. imprime solo OK o FRENO, el conjunto de ids de E1 (con sus reintentos) y el de E3. FRENO si algún id de E1 no es
     claude-haiku-4-5-20251001; el de E3 se reporta y no frena. No imprime cantidades de llamadas, porque contarían
     los reintentos (el cegamiento de U-MED-VERIF, §7).
Con --etiquetas-existentes, en lugar de los ids, dice cuáles de las etiquetas de los TOs pedidos ya están en las bases
(solo los nombres): antes de la tanda final no tiene que haber ninguna.

La copia se abre como una base común (no `immutable`), para que lea también lo que esté en el `-wal`; como es una
copia, lo que SQLite escriba al abrirla queda en ella.

Uso: <python> -B freno_modelo_t2.py --repo <raíz> --trabajo <dir fuera del repo> --tos a,b,c [--etiquetas-existentes]
      [--borrar]   (borra --trabajo al terminar; el lanzador la borra él)
Salida: 0 OK, 10 FRENO (o etiquetas ya existentes), 2 error de uso. Lo importa lanzar_t2.py (función controlar).
"""
from __future__ import annotations

import argparse
import shutil
import sqlite3
import sys
from pathlib import Path

ID_E1 = "claude-haiku-4-5-20251001"
BASES = {
    "e1": "data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db",
    "e1_reintentos": "data/experiment/reextraccion_v2/e3_verificador/cache/e1_reintentos.db",
    "e3": "data/experiment/reextraccion_v2/e3_verificador/cache/e3_verificacion.db",
}
ETIQUETA = {"e1": "corpus_{}_e1", "e1_reintentos": "corpus_{}_reintentos_e1", "e3": "corpus_{}_e3"}
SUFIJOS = ("", "-wal", "-shm")


def copiar_bases(repo: Path, trabajo: Path) -> dict[str, Path | None]:
    trabajo.mkdir(parents=True, exist_ok=True)
    out = {}
    for nombre, rel in BASES.items():
        origen = repo / rel
        for suf in SUFIJOS:                       # se pisa la copia anterior entera, también sus -wal y -shm
            p = trabajo / f"{nombre}.db{suf}"
            if p.exists():
                p.unlink()
        if not origen.exists():
            out[nombre] = None
            continue
        for suf in SUFIJOS:
            o = Path(str(origen) + suf)
            if o.exists():
                shutil.copy2(o, trabajo / f"{nombre}.db{suf}")
        out[nombre] = trabajo / f"{nombre}.db"
    return out


def _consulta(db: Path | None, sql: str, params: list[str]) -> set[str]:
    if db is None:
        return set()
    con = sqlite3.connect(str(db))
    try:
        tablas = {r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type = 'table'")}
        if not {"access_log", "cache"} <= tablas:
            return set()
        return {r[0] for r in con.execute(sql, params)}
    finally:
        con.close()


def controlar(repo: Path, trabajo: Path, tos: list[str]) -> dict:
    """Copia las bases y devuelve {"resultado": "OK"|"FRENO", "ids_e1": [...], "ids_e3": [...]}."""
    repo, trabajo = Path(repo).resolve(), Path(trabajo).resolve()
    if trabajo.is_relative_to(repo):
        raise ValueError("la copia de trabajo de las bases tiene que estar fuera del repo")
    copias = copiar_bases(repo, trabajo)
    ids = {}
    for nombre, db in copias.items():
        etiquetas = [ETIQUETA[nombre].format(t) for t in tos]
        marcas = ",".join("?" * len(etiquetas))
        ids[nombre] = _consulta(db, f"SELECT DISTINCT c.model FROM access_log a JOIN cache c ON c.key = a.key "
                                    f"WHERE a.run_label IN ({marcas})", etiquetas)
    ids_e1 = sorted(ids["e1"] | ids["e1_reintentos"])
    return {"resultado": "OK" if all(x == ID_E1 for x in ids_e1) else "FRENO", "ids_e1": ids_e1,
            "ids_e3": sorted(ids["e3"])}


def etiquetas_existentes(repo: Path, trabajo: Path, tos: list[str]) -> list[str]:
    repo, trabajo = Path(repo).resolve(), Path(trabajo).resolve()
    if trabajo.is_relative_to(repo):
        raise ValueError("la copia de trabajo de las bases tiene que estar fuera del repo")
    copias = copiar_bases(repo, trabajo)
    encontradas = set()
    for nombre, db in copias.items():
        etiquetas = [ETIQUETA[nombre].format(t) for t in tos]
        marcas = ",".join("?" * len(etiquetas))
        encontradas |= _consulta(db, f"SELECT DISTINCT run_label FROM access_log WHERE run_label IN ({marcas})",
                                 etiquetas)
    return sorted(encontradas)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--trabajo", type=Path, required=True)
    ap.add_argument("--tos", required=True)
    ap.add_argument("--etiquetas-existentes", action="store_true")
    ap.add_argument("--borrar", action="store_true")
    a = ap.parse_args()
    try:
        return _main(a)
    finally:
        if a.borrar and a.trabajo.exists():
            shutil.rmtree(a.trabajo)


def _main(a) -> int:
    tos = [t.strip() for t in a.tos.split(",") if t.strip()]
    try:
        if a.etiquetas_existentes:
            e = etiquetas_existentes(a.repo, a.trabajo, tos)
            print("etiquetas de esos TOs ya en las bases:", ", ".join(e) if e else "ninguna")
            return 10 if e else 0
        r = controlar(a.repo, a.trabajo, tos)
    except ValueError as e:
        print(f"error: {e}")
        return 2
    print("ids de E1 (con sus reintentos):", r["ids_e1"])
    print("ids de E3:", r["ids_e3"])
    print("RESULTADO:", r["resultado"])
    return 0 if r["resultado"] == "OK" else 10


if __name__ == "__main__":
    sys.exit(main())
