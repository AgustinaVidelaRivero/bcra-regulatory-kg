"""U-R2-CODIGO — selftest de R2 (identificadores, persistencia y candado de E3), sin API.

Bloques:
  A. Desambiguación de ids de E0 (BKL-0037; e0_lib.desambiguar_ids): par y
     terna sintéticos; la partición del corpus escalado (69 ids repetidos en
     adfsp, ceninf, cirmo3 y ri_niif, leídos sin escribir); la E0 de la tanda 0
     sin ids repetidos y sin cambios.
  B. El runner se detiene ante un par de chunks de igual id
     (runner_corpus.chunks_sin_ids_repetidos), también de punta a punta en la
     compactación de E1, sin escribir el compactado.
  C. Persistencia del crudo del reintento de E3: fase_e3 con el ciclo de E3
     reemplazado en este proceso por uno fijo que devuelve un reintento;
     `reintentos_e3.jsonl` se escribe antes de `finales.jsonl` y el lector lo
     lee. Sin reintentos, el archivo no se crea.
  D. Lector de la caché (tanda 0, salida_dirigida, cap): un crudo por
     reintento de finales.jsonl, leído con immutable=1.
  E. Candado del prefijo de E3: con los datos actuales no frena; con una
     copia alterada de chunks_ric.json (un archivo de datos de los
     calibradores) en un directorio temporal, la importación frena.
  F. Docstring de ratchet_e3.build_reextraccion_kwargs.
Todo lo que escribe va a directorios temporales (tempfile).

Uso:
  TMPDIR=<scratchpad> PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/selftest_r2.py
"""

from __future__ import annotations

import copy
import json
import os
import shutil
import subprocess
import sys
import tempfile
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "e0_chunking", REX / "corpus_v2", AQUI):
    sys.path.insert(0, str(p))
import e0_lib as E0  # noqa: E402
import runner_corpus as RC  # noqa: E402
import lector_reintentos_e3 as LR  # noqa: E402

RESULTADOS: list[tuple[str, bool, str]] = []
PARTICION = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
E0_TANDA0 = REX / "e0_chunking" / "salida_tanda0"


def check(nombre: str, ok: bool, detalle: str = "") -> None:
    RESULTADOS.append((nombre, ok, detalle))
    print(f"  [{'PASS' if ok else 'FAIL'}] {nombre}" + (f" — {detalle}" if detalle else ""))


def _chunk(cid: str, unidad: str, texto: str) -> dict:
    return {"id": cid, "to": "x", "archivo": "x.pdf", "unidad": unidad, "titulo": "t",
            "tipo": "punto_terminal", "paginas": [1], "texto": texto, "chars_propio": len(texto),
            "chars_completo": len(texto), "herencia": [],
            "flags": {"contenido_tabular": False, "formula": False,
                      "evidencia_tabular": [], "evidencia_formula": []},
            "sha256_propio": "", "sha256_completo": ""}


def bloque_a() -> None:
    print("A. Desambiguación de ids de E0 (BKL-0037)")
    par = [_chunk("x::6.1", "6.1", "índice"), _chunk("x::6.1", "6.1", "cuerpo")]
    ren = E0.desambiguar_ids(par)
    check("A1 par: el primero conserva el id, el segundo recibe ::rep2",
          [c["id"] for c in par] == ["x::6.1", "x::6.1::rep2"]
          and par[1]["id_e0_original"] == "x::6.1" and "id_e0_original" not in par[0]
          and par[1]["unidad"] == "6.1" and ren == [{"id_e0_original": "x::6.1", "id": "x::6.1::rep2"}])
    terna = [_chunk("x::7.1", "7.1", str(i)) for i in range(3)]
    E0.desambiguar_ids(terna)
    check("A2 terna: ::rep2 y ::rep3", [c["id"] for c in terna] == ["x::7.1", "x::7.1::rep2", "x::7.1::rep3"])
    unicos = [_chunk("x::1.1", "1.1", "a"), _chunk("x::1.2", "1.2", "b")]
    antes = copy.deepcopy(unicos)
    check("A3 sin ids repetidos no toca nada", E0.desambiguar_ids(unicos) == [] and unicos == antes)
    por_to = {}
    for to in ("adfsp", "ceninf", "cirmo3", "ri_niif"):
        ch = json.loads((PARTICION / to / f"chunks_{to}.json").read_text(encoding="utf-8"))
        ren = E0.desambiguar_ids(ch)
        por_to[to] = (len(ren), max(Counter(c["id"] for c in ch).values()))
    check("A4 partición: 69 renombres (adfsp 9, ceninf 4, cirmo3 52, ri_niif 4) y ningún id repetido después",
          {k: v[0] for k, v in por_to.items()} == {"adfsp": 9, "ceninf": 4, "cirmo3": 52, "ri_niif": 4}
          and all(v[1] == 1 for v in por_to.values()), str(por_to))
    reps, ren_t0 = 0, 0
    for p in sorted(E0_TANDA0.glob("chunks_*.json")):
        ch = json.loads(p.read_text(encoding="utf-8"))
        reps += sum(v - 1 for v in Counter(c["id"] for c in ch).values())
        ren_t0 += len(E0.desambiguar_ids(ch))
    check("A5 tanda 0: 0 ids repetidos y 0 renombres", reps == 0 and ren_t0 == 0)


def bloque_b(tmp: Path) -> None:
    print("B. El runner se detiene ante ids repetidos")
    par = [_chunk("x::6.1", "6.1", "índice"), _chunk("x::6.1", "6.1", "cuerpo")]
    try:
        RC.chunks_sin_ids_repetidos(par, "x")
        check("B1 par de igual id → IdsRepetidos", False)
    except RC.IdsRepetidos as e:
        check("B1 par de igual id → IdsRepetidos", "x::6.1" in str(e))
    unicos = [_chunk("x::1.1", "1.1", "a")]
    check("B2 ids únicos: devuelve la misma lista", RC.chunks_sin_ids_repetidos(unicos, "x") is unicos)
    e0 = tmp / "e0"
    e0.mkdir()
    (e0 / "chunks_x.json").write_text(json.dumps(par, ensure_ascii=False), encoding="utf-8")
    sal = tmp / "salida"
    (sal / "x").mkdir(parents=True)
    with (sal / "x" / "extracciones_e1.jsonl").open("w", encoding="utf-8") as f:
        for i in range(2):
            f.write(json.dumps({"chunk_id": "x::6.1", "error": None, "n": i}) + "\n")
    viejo = RC.E0_DIR
    RC.E0_DIR = e0
    try:
        RC.compactar_e1("x", sal)
        check("B3 compactación de E1 con ids repetidos se detiene", False)
    except RC.IdsRepetidos:
        check("B3 compactación de E1 con ids repetidos se detiene y no escribe el compactado",
              not (sal / "x" / "extracciones_e1_compact.jsonl").exists())
    finally:
        RC.E0_DIR = viejo


def bloque_c(tmp: Path) -> None:
    print("C. Persistencia del crudo del reintento de E3")
    c = _chunk("x::2.1", "2.1", "2.1. Texto del punto.")
    e0 = tmp / "e0c"
    e0.mkdir()
    (e0 / "chunks_x.json").write_text(json.dumps([c], ensure_ascii=False), encoding="utf-8")
    val = {"rechazos": [], "entities": [], "relations": []}

    def correr(sal: Path, con_reintento: bool) -> None:
        (sal / "x").mkdir(parents=True)
        (sal / "x" / "extracciones_e1.jsonl").write_text(
            json.dumps({"chunk_id": "x::2.1", "error": None, "validacion": val}) + "\n",
            encoding="utf-8")
        exp = {"chunk_id": "x::2.1", "estado": "aceptado_tras_reintento" if con_reintento
               else "completo_ok_directo", "residuales": [], "validacion_final": val,
               "veredictos": [], "reintentos": ([{"chunk_id": "x::2.1", "intento": 1,
                                                  "tool_input": {"entities": ["crudo"]},
                                                  "validacion": val, "error": None}]
                                                if con_reintento else [])}
        orig_ciclo, orig_e0 = RC.ratchet_e3.ciclo_ratchet, RC.E0_DIR
        orig_est = RC.ESTIMADO_USD
        RC.ratchet_e3.ciclo_ratchet = lambda *a, **k: exp
        RC.E0_DIR = e0
        RC.ESTIMADO_USD = {"x": {"e1": 0.0, "e3": 0.0}}   # estimación nula del TO sintético
        try:
            RC.fase_e3("x", RC.StubE3Corpus(), RC.StubE1Corpus(), RC.Estado(sal), sal,
                       None, None, None)
        finally:
            RC.ratchet_e3.ciclo_ratchet, RC.E0_DIR = orig_ciclo, orig_e0
            RC.ESTIMADO_USD = orig_est

    sal = tmp / "sal_c1"
    correr(sal, True)
    comp = LR.leer_companero(sal / "x")
    fin = [json.loads(l) for l in (sal / "x" / "finales.jsonl").read_text(encoding="utf-8").splitlines()]
    check("C1 con reintento: reintentos_e3.jsonl con el crudo, leído por el lector",
          comp.get(("x::2.1", 1), {}).get("tool_input") == {"entities": ["crudo"]}
          and fin[0]["n_reintentos"] == 1)
    check("C2 el archivo compañero se escribe antes que finales.jsonl",
          (sal / "x" / RC.REINTENTOS_E3).stat().st_mtime_ns
          <= (sal / "x" / "finales.jsonl").stat().st_mtime_ns)
    sal2 = tmp / "sal_c2"
    correr(sal2, False)
    check("C3 sin reintentos, el archivo compañero no se crea",
          not (sal2 / "x" / RC.REINTENTOS_E3).exists() and (sal2 / "x" / "finales.jsonl").exists())


def bloque_d() -> None:
    print("D. Lector de la caché (tanda 0, salida_dirigida, cap)")
    cfg = LR.GENERACIONES["t0_dirigida"]
    fin = [json.loads(l) for l in (cfg["salida"] / "cap" / "finales.jsonl")
           .read_text(encoding="utf-8").splitlines() if l.strip()]
    n = sum(1 for f in fin if f.get("n_reintentos"))
    crudos = LR.leer_desde_cache(cfg["salida"], "cap", cfg["perfil"], cfg["e0"])
    check("D1 un crudo por reintento de cap (immutable=1)",
          n > 0 and len(crudos) == n and all(v["tool_input"] is not None for v in crudos.values()),
          f"{len(crudos)}/{n}")


def _espejo(dst: Path) -> None:
    """Copia de reextraccion_v2 con los .py copiados y el resto enlazado."""
    exp = dst / "data" / "experiment"
    rv = exp / "reextraccion_v2"
    rv.mkdir(parents=True)
    for x in REX.iterdir():
        if x.name == "__pycache__":
            continue
        if x.is_dir():
            (rv / x.name).mkdir()
            for y in x.iterdir():
                if y.name == "__pycache__":
                    continue
                if y.is_file() and y.suffix == ".py":
                    shutil.copy2(y, rv / x.name / y.name)
                else:
                    os.symlink(y, rv / x.name / y.name)
        elif x.suffix == ".py":
            shutil.copy2(x, rv / x.name)
        else:
            os.symlink(x, rv / x.name)
    for d in (REPO / "data" / "experiment").iterdir():
        if d.name != "reextraccion_v2":
            os.symlink(d, exp / d.name)


def _importa_prompt_e3(raiz: Path) -> subprocess.CompletedProcess:
    e3 = raiz / "data" / "experiment" / "reextraccion_v2" / "e3_verificador"
    return subprocess.run([sys.executable, "-B", "-c",
                           "import sys; sys.path.insert(0, sys.argv[1]); import prompt_e3; "
                           "print(prompt_e3.PREFIJO_HASH)", str(e3)],
                          capture_output=True, text=True,
                          env=dict(os.environ, PYTHONDONTWRITEBYTECODE="1"))


def bloque_e(tmp: Path) -> None:
    print("E. Candado del prefijo de E3")
    sano = tmp / "espejo_sano"
    _espejo(sano)
    r = _importa_prompt_e3(sano)
    check("E1 con los datos actuales no frena y el hash es 21a836c7de6d",
          r.returncode == 0 and r.stdout.strip() == "21a836c7de6d", (r.stderr or r.stdout).strip()[-80:])
    alt = tmp / "espejo_alterado"
    _espejo(alt)
    sal = alt / "data" / "experiment" / "reextraccion_v2" / "e0_chunking" / "salida"
    real = Path(os.readlink(sal))
    sal.unlink()
    shutil.copytree(real, sal)
    ric = json.loads((sal / "chunks_ric.json").read_text(encoding="utf-8"))
    for c in ric:
        if c["id"] == "ric::7.1":
            c["texto"] += " X"
    (sal / "chunks_ric.json").write_text(json.dumps(ric, ensure_ascii=False, indent=1), encoding="utf-8")
    r = _importa_prompt_e3(alt)
    check("E2 con chunks_ric.json alterado (copia temporal), la importación frena",
          r.returncode != 0 and "candado E3" in r.stderr, r.stderr.strip()[-120:])
    check("E3 el archivo real no cambió",
          json.loads((real / "chunks_ric.json").read_text(encoding="utf-8")) != ric)


def bloque_f() -> None:
    print("F. Docstring de ratchet_e3.build_reextraccion_kwargs")
    doc = RC.ratchet_e3.build_reextraccion_kwargs.__doc__
    check("F1 dice que max_tokens no invalida la caché de prompts de la API y sí la local",
          "no invalida la caché de prompts de la API" in doc
          and "pero sí la caché local: su clave incluye max_tokens" in " ".join(doc.split()))


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="selftest_r2_") as td:
        tmp = Path(td)
        bloque_a()
        bloque_b(tmp)
        bloque_c(tmp)
        bloque_d()
        bloque_e(tmp)
        bloque_f()
    ok = sum(1 for _, b, _ in RESULTADOS if b)
    print(f"\nSELFTEST R2: {ok}/{len(RESULTADOS)} PASS")
    return 0 if ok == len(RESULTADOS) else 1


if __name__ == "__main__":
    sys.exit(main())
