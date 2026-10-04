"""
control_reproduccion_p3b2.py — U-PROMPT-R2, P3b-2 (USD 0): control de reproducción con los perfiles existentes,
sobre una COPIA del repo (CLAUDE.md §4 k y l), con el código del árbol de trabajo (P3b-2 aplicado). Es el de P3
(sin la E0 legada: P3b-2 no toca E0) más el control de la unión de las operaciones por punto (paso d).

  1. sha256 de los archivos del repo (rastreados y no ignorados) antes;
  2. copia sin enlaces simbólicos (rsync --copy-links), sin .git, .venv ni data/raw; se controla que no tenga enlaces;
  3. en la copia:
     a. E0 legada de la tanda 0 (correr_e0.py sin --version-e0, manifiesto tanda0_10tos) → los 34 archivos de
        e0_chunking/salida_tanda0 del repo, byte a byte;
     b. los tres ensamblados sellados (tanda0_ens_cinco, _diez y _desarrollo, entrada salida_dirigida, motor
        replica) → los 13 archivos de corpus_tanda0/ens_<x> del repo;
     c. los dos grafos r2a (--perfil-r2 con la e0-r2) → corpus_tanda0/ens_<x>_r2a del repo (kg 99fe2bfa… y
        93a7af72…);
     d. los mismos dos grafos con la Operacion unida por punto (regla de la fase r2b, forzar_operacion_r2b.py,
        que parchea solo entity_slug_r2): la lista de las operaciones que se separan, con sus puntos; que ninguna
        unión dentro de un mismo punto cambie; y lo que cambia aguas abajo (aristas que tocan esos nodos y
        cuántas son remite_a, adjudicación de colisiones entre TOs y conflictos);
  4. sha256 del repo después: tiene que ser igual.
Las comparaciones de reportes normalizan la ruta de salida (los reportes la registran).

Uso: <python del repo> control_reproduccion_p3b2.py <repo> <dir de trabajo fuera del repo>
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(sys.argv[1]).resolve()
TRAB = Path(sys.argv[2]).resolve()
assert REPO not in TRAB.parents and TRAB != REPO, "el directorio de trabajo no puede estar dentro del repo"
PY = str(REPO / ".venv" / "bin" / "python")
COPIA = TRAB / "copia"
OUT = TRAB / "salidas"
ENV = {"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"}
res: dict = {}


def sha_repo() -> dict:
    r = subprocess.run(["git", "ls-files", "-z", "-co", "--exclude-standard"], cwd=REPO, capture_output=True,
                       check=True)
    out = {}
    for rel in sorted(x for x in r.stdout.decode().split("\0") if x):
        p = REPO / rel
        if p.is_file():
            out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def comparar_dir(a: Path, b: Path, normalizar: tuple[str, ...] = ()) -> dict:
    fa = {str(p.relative_to(a)) for p in a.rglob("*") if p.is_file()}
    fb = {str(p.relative_to(b)) for p in b.rglob("*") if p.is_file()}
    iguales, iguales_norm, distintos = [], [], []
    for rel in sorted(fa & fb):
        x, y = (a / rel).read_bytes(), (b / rel).read_bytes()
        if x == y:
            iguales.append(rel)
            continue
        tx, ty = x.decode("utf-8", "replace"), y.decode("utf-8", "replace")
        for viejo, nuevo in normalizar:
            tx, ty = tx.replace(viejo, nuevo), ty.replace(viejo, nuevo)
        (iguales_norm if tx == ty else distintos).append(rel)
    return {"solo_en_repo": sorted(fa - fb), "solo_en_copia": sorted(fb - fa), "iguales": len(iguales),
            "iguales_con_ruta_normalizada": iguales_norm, "distintos": distintos, "total_repo": len(fa)}


def correr(args: list[str], nombre: str) -> int:
    r = subprocess.run([PY, "-B", *args], cwd=COPIA, env=ENV, capture_output=True, text=True)
    (OUT / f"{nombre}.log").write_text(r.stdout[-20000:] + "\n--- stderr ---\n" + r.stderr[-20000:], encoding="utf-8")
    return r.returncode


FORZAR = Path(__file__).resolve().parent / "forzar_operacion_r2b.py"


def analizar_union(sellado: Path, forzado: Path, e2_dir: Path) -> dict:
    """d. Operacion de r2a (sellado) contra la unida por punto (forzado), sobre el kg final de cada uno. Cada grupo
    (TO, punto) de procedencias de una Operacion sellada tiene que ser un nodo del forzado, con el id que da la regla
    de la fase r2b (e2_lib.entity_slug_r2 con la etiqueta del nodo sellado) y exactamente esas procedencias."""
    if str(e2_dir) not in sys.path:
        sys.path.insert(0, str(e2_dir))
    import e2_lib  # noqa: PLC0415 — el de la copia
    a = json.loads((sellado / "r2" / "kg.json").read_text(encoding="utf-8"))
    b = json.loads((forzado / "r2" / "kg.json").read_text(encoding="utf-8"))

    def provs(n):
        return n.get("provenances") or [n["provenance"]]

    def pk(p):
        return json.dumps(p, sort_keys=True, ensure_ascii=False)
    ops_a = [n for n in a["nodes"] if n["type"] == "Operacion"]
    ops_b = {n["id"]: n for n in b["nodes"] if n["type"] == "Operacion"}
    esperados, de_separada, fallos = {}, set(), []
    for n in ops_a:
        g = defaultdict(set)
        for p in provs(n):
            g[(p.get("to"), p.get("punto"))].add(pk(p))
        for (to, punto), x in g.items():
            gid = "Operacion_" + e2_lib.entity_slug_r2({"type": "Operacion", "label": n["label"],
                                                         "properties": n.get("properties") or {}},
                                                        {"to": to, "punto": punto}, "r2b")
            esperados[gid] = x
            if len(g) > 1:
                de_separada.add(gid)
            if gid not in ops_b or {pk(p) for p in provs(ops_b[gid])} != x:
                fallos.append(gid)
    separadas = [n for n in ops_a if len({(p.get("to"), p.get("punto")) for p in provs(n)}) > 1]
    ids_sep = {n["id"] for n in separadas}

    def aristas(kg, ids):
        es = [e for e in kg["edges"] if e["source"] in ids or e["target"] in ids]
        return {"aristas": len(es), "remite_a": sum(1 for e in es if e["relation"] == "remite_a"),
                "por_relacion": dict(sorted(Counter(e["relation"] for e in es).items()))}
    otros_a = {n["id"]: n for n in a["nodes"] if n["type"] != "Operacion"}
    otros_b = {n["id"]: n for n in b["nodes"] if n["type"] != "Operacion"}
    sin_op_a = {pk(e) for e in a["edges"] if e["source"] not in {n["id"] for n in ops_a}
                and e["target"] not in {n["id"] for n in ops_a}}
    sin_op_b = {pk(e) for e in b["edges"] if e["source"] not in ops_b and e["target"] not in ops_b}

    def leer(d, nombre):
        f = d / "r2" / nombre
        return json.loads(f.read_text(encoding="utf-8")) if f.exists() else None
    adj_a, adj_b = leer(sellado, "adjudicacion_cross_to.json"), leer(forzado, "adjudicacion_cross_to.json")
    con_a, con_b = leer(sellado, "e4_conflictos.json"), leer(forzado, "e4_conflictos.json")
    rep_a, rep_b = leer(sellado, "reporte_ensamblado_r2.json"), leer(forzado, "reporte_ensamblado_r2.json")
    rem_a, rem_b = leer(sellado, "remisiones_registro.json") or [], leer(forzado, "remisiones_registro.json") or []

    def clave_rem(r):
        return pk({k: r.get(k) for k in ("chunk_id", "clase", "norma_nombrada", "to_destino", "puntos", "secciones",
                                         "evidencia")})
    ra, rb = defaultdict(list), defaultdict(list)
    for r in rem_a:
        ra[clave_rem(r)].append(r)
    for r in rem_b:
        rb[clave_rem(r)].append(r)
    cambio_atrib = Counter()
    for k in set(ra) | set(rb):
        at_a = sorted(r.get("atribucion") or "" for r in ra.get(k, []))
        at_b = sorted(r.get("atribucion") or "" for r in rb.get(k, []))
        if at_a != at_b or sorted(len(r.get("origenes") or []) for r in ra.get(k, [])) != sorted(
                len(r.get("origenes") or []) for r in rb.get(k, [])):
            cambio_atrib[f"{'+'.join(at_a) or '—'} → {'+'.join(at_b) or '—'}"] += 1

    def conflictos_e2(rep):
        return {to: v.get("conflictos_properties") for to, v in ((rep or {}).get("e2_por_to") or {}).items()}

    def reales(c):
        return {"n_total": c.get("n_total"), "n_reales": c.get("n_reales"),
                "reales_por_tipo_property": c.get("reales_por_tipo_property")} if isinstance(c, dict) else c
    return {
        "operacion_nodos": [len(ops_a), len(ops_b)],
        "separadas": len(separadas), "separadas_en_nodos": len(de_separada),
        "separadas_por_to": dict(sorted(Counter(provs(n)[0].get("to") for n in separadas).items())),
        "union_dentro_del_mismo_punto": {
            "nodos_de_un_punto_con_mas_de_una_unidad": sum(
                1 for n in ops_a if len({(p.get("to"), p.get("punto")) for p in provs(n)}) == 1
                and len({p.get("chunk_id") for p in provs(n)}) > 1)},
        "cada_grupo_es_un_nodo_con_su_id_y_sus_procedencias": not fallos and set(esperados) == set(ops_b),
        "fallos_de_grupo": fallos[:20],
        "otros_nodos": {"iguales": sum(1 for k, v in otros_a.items() if otros_b.get(k) == v),
                        "distintos": sorted(k for k, v in otros_a.items() if k in otros_b and otros_b[k] != v),
                        "solo_sellado": sorted(set(otros_a) - set(otros_b)),
                        "solo_forzado": sorted(set(otros_b) - set(otros_a))},
        "aristas": [len(a["edges"]), len(b["edges"])],
        "aristas_sin_operacion_distintas": {
            "solo_sellado": dict(Counter(json.loads(x)["relation"] for x in sin_op_a - sin_op_b)),
            "solo_forzado": dict(Counter(json.loads(x)["relation"] for x in sin_op_b - sin_op_a))},
        "aristas_que_tocan_las_separadas": aristas(a, ids_sep),
        "aristas_que_tocan_sus_nodos_nuevos": aristas(b, de_separada),
        "remisiones_registro": {"filas": [len(rem_a), len(rem_b)],
                                "remisiones_con_otra_atribucion": dict(sorted(cambio_atrib.items()))},
        "adjudicacion_cross_to": {"sellado": len(adj_a or []), "forzado": len(adj_b or []),
                                  "ids_sellado": [str(y.get("id", ""))[:90] for y in (adj_a or [])]},
        "e4_conflictos": {"sellado": reales(con_a), "forzado": reales(con_b)},
        "conflictos_properties_e2_por_to": {"sellado": conflictos_e2(rep_a), "forzado": conflictos_e2(rep_b)},
        "lista_separadas": [{"id": n["id"], "label": n["label"],
                             "puntos": sorted({f"{p.get('to')}::{p.get('punto')}" for p in provs(n)})}
                            for n in sorted(separadas, key=lambda n: n["id"])],
    }


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    antes = sha_repo()
    res["repo_archivos"] = len(antes)
    if COPIA.exists():
        subprocess.run(["rm", "-rf", str(COPIA)], check=True)
    subprocess.run(["rsync", "-a", "--copy-links", "--exclude", ".git", "--exclude", ".venv", "--exclude", "data/raw",
                    "--exclude", "__pycache__", "--exclude", "*.pyc", f"{REPO}/", f"{COPIA}/"], check=True)
    enlaces = sum(1 for _r, ds, fs in os.walk(COPIA) for x in ds + fs if os.path.islink(os.path.join(_r, x)))
    res["copia_enlaces"] = enlaces
    assert enlaces == 0
    REX = "data/experiment/reextraccion_v2"
    MAN = f"{REX}/manifiestos"
    # b. ensamblados sellados
    for x in ("cinco", "diez", "desarrollo"):
        sal = OUT / f"ens_{x}"
        rc = correr(["data/experiment/tanda0/code/ensamblar_tanda0.py", "--manifiesto", f"{MAN}/tanda0_ens_{x}.json",
                     "--entrada", f"{REX}/corpus_tanda0/salida_dirigida", "--salida", str(sal)], f"ens_{x}")
        res[f"ens_{x}"] = {"rc": rc, **comparar_dir(REPO / REX / "corpus_tanda0" / f"ens_{x}", sal,
                                                    ((str(sal), "<SALIDA>"), (str(COPIA) + "/", ""), (str(REPO) + "/", ""), (f"{REX}/corpus_tanda0/ens_{x}", "<SALIDA>"),
                                                     (str(COPIA) + "/", ""), (str(REPO) + "/", "")))}
    # c. r2a
    for x, esperado in (("diez", "99fe2bfa0de05704e4c636bdf9b0455a30e29b378e3b0e61eadc49dad3f7c649"),
                        ("desarrollo", "93a7af7279a415ee72cfec547bcd080d4c85a96746e219ed94dea4239007e8dd")):
        sal = OUT / f"ens_{x}_r2a"
        rc = correr(["data/experiment/tanda0/code/ensamblar_tanda0.py", "--manifiesto", f"{MAN}/tanda0_ens_{x}.json",
                     "--entrada", f"{REX}/corpus_tanda0/salida_dirigida", "--perfil-r2",
                     "--e0-r2", f"{REX}/e0_chunking/salida_tanda0_r2", "--salida", str(sal)], f"ens_{x}_r2a")
        kg = sal / "r2" / "kg.json"
        res[f"ens_{x}_r2a"] = {"rc": rc, "sha256_kg": sha(kg) if kg.exists() else None,
                               "kg_igual_al_sellado": kg.exists() and sha(kg) == esperado,
                               **comparar_dir(REPO / REX / "corpus_tanda0" / f"ens_{x}_r2a", sal,
                                              ((str(sal), "<SALIDA>"), (str(COPIA) + "/", ""), (str(REPO) + "/", ""), (f"{REX}/corpus_tanda0/ens_{x}_r2a", "<SALIDA>"),
                                               (str(COPIA) + "/", ""), (str(REPO) + "/", "")))}
    # d. unión de las operaciones por punto
    for x in ("diez", "desarrollo"):
        sal = OUT / f"ens_{x}_r2a_operacion_por_punto"
        rc = correr([str(FORZAR), "--manifiesto", f"{MAN}/tanda0_ens_{x}.json",
                     "--entrada", f"{REX}/corpus_tanda0/salida_dirigida", "--perfil-r2",
                     "--e0-r2", f"{REX}/e0_chunking/salida_tanda0_r2", "--salida", str(sal)],
                    f"ens_{x}_r2a_operacion_por_punto")
        res[f"union_operaciones_{x}"] = {"rc": rc, **analizar_union(REPO / REX / "corpus_tanda0" / f"ens_{x}_r2a", sal,
                                                                     COPIA / REX / "e2_reduce")}
    despues = sha_repo()
    res["repo_sin_cambios"] = antes == despues
    res["repo_cambiados"] = sorted(k for k in set(antes) | set(despues) if antes.get(k) != despues.get(k))
    (TRAB / "control_reproduccion_p3b2.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n",
                                                       encoding="utf-8")
    print(json.dumps({k: ({kk: vv for kk, vv in v.items() if kk not in ("iguales_con_ruta_normalizada",
                                                                         "lista_separadas")}
                          if isinstance(v, dict) else v) for k, v in res.items()}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
