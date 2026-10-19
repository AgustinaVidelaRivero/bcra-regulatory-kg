"""
00_control_insumos.py — U-TRIP-V: control de la copia y de los insumos antes de correr nada (y otra vez al cerrar).

  - HEAD del repo, su título, `status --porcelain --untracked-files=no` y el diff de nombres contra 593e5db2 (el commit
    que nombra el despacho) y contra a7d00025 (el HEAD con que se trabaja): si un commit posterior a a7d00025 toca un
    insumo (el pre-registro, sus dos enmiendas, el kg.json, la E0, los PDF o grafos.py), FRENO.
  - Cada archivo que se usa: blob de la copia (`git hash-object --stdin-paths`) contra `git ls-files -s` del repo y
    contra `git ls-tree a7d00025`. Los PDF de data/experiment/subset/ no están en git (.gitignore:35,
    `data/experiment/**/*.pdf`): van por sha256 y comparados byte a byte con los del repo.
  - En la copia: 0 archivos de entorno, `NO_ABRIR_*` o `*_SOLO_MESA*`, y 0 enlaces.

Solo lee: git con --no-optional-locks sobre el repo, y la copia. Escribe --salida (JSON).
  python3 -I -B 00_control_insumos.py --repo <repo> --copia <copia> --salida <json>
"""
from __future__ import annotations

import argparse
import filecmp
import json
import os
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_v as V  # noqa: E402

BASE_TRABAJO = "a7d00025"
COMMIT_DESPACHO = "593e5db2"
INSUMOS_PROTEGIDOS = ("docs/preregistro_evaluacion_tripletas.md",
                      "docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md",
                      "docs/enmienda2_preregistro_evaluacion_tripletas_2026-10-17_desambiguacion.md",
                      V.KG_REL, V.E0_REL + "/", V.PDF_DIR_REL + "/", "data/experiment/neo4j/grafos.py")
USADOS = (
    # los que rigen
    "docs/preregistro_evaluacion_tripletas.md",
    "docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md",
    "docs/enmienda2_preregistro_evaluacion_tripletas_2026-10-17_desambiguacion.md",
    "data/experiment/neo4j/grafos.py",
    # el grafo, el sellado anterior y el diff declarado del re-sellado (para la diferencia de la población)
    V.KG_REL, V.KG_PREVIO_REL, V.DIFF_RESELLADO_REL,
    "data/experiment/resellado_t0/FRENO_resellado_T0.md",
    # la cadena de ensamblado leída para la lista de fuera
    V.CADENA_REL, V.MANIFIESTO_REL, V.ENS_REL, V.E2_REL, V.MODELOS_R2_REL, V.SCHEMA_REL, V.E5_REL, V.REF_REL,
    # el solapamiento con U-LECTURA-ACEPTADAS y los precedentes de sorteo y ficha
    V.SELLOS_L0_REL, "data/experiment/lectura_aceptadas/l0_sellos.py", "data/experiment/lectura_aceptadas/l1_fichas.py",
)


def git(repo: Path, *args: str) -> str:
    return subprocess.run(["git", "-C", str(repo), "--no-optional-locks", *args], check=True,
                          capture_output=True, text=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--copia", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    out: dict = {"hora": V.hora()}

    head = git(a.repo, "rev-parse", "HEAD").strip()
    out["head"] = {"sha": head, "titulo": git(a.repo, "log", "-1", "--format=%h %s").strip(),
                   "status_porcelain_untracked_no": git(a.repo, "status", "--porcelain", "--untracked-files=no"),
                   "diff_name_status_593e5db2_HEAD": git(a.repo, "diff", "--name-status", COMMIT_DESPACHO, "HEAD"),
                   "diff_name_status_a7d00025_HEAD": git(a.repo, "diff", "--name-status", BASE_TRABAJO, "HEAD")}
    tocados = []
    for linea in out["head"]["diff_name_status_a7d00025_HEAD"].splitlines():
        ruta = linea.split("\t")[-1]
        if any(ruta == p or (p.endswith("/") and ruta.startswith(p)) for p in INSUMOS_PROTEGIDOS):
            tocados.append(linea)
    out["head"]["commits_nuevos_que_tocan_insumos"] = tocados

    # blobs: los archivos usados más todos los rastreados de la E0
    e0 = [l.split("\t", 1)[1] for l in git(a.repo, "ls-files", "-s", "--", V.E0_REL).splitlines()]
    rutas = list(USADOS) + e0
    indice = {}
    for l in git(a.repo, "ls-files", "-s", "--", *rutas).splitlines():
        meta, ruta = l.split("\t", 1)
        indice[ruta] = meta.split()[1]
    arbol = {}
    for l in git(a.repo, "ls-tree", "-r", BASE_TRABAJO, "--", *rutas).splitlines():
        meta, ruta = l.split("\t", 1)
        arbol[ruta] = meta.split()[2]
    paths_copia = [str(a.copia / r) for r in rutas]
    blobs = subprocess.run(["git", "hash-object", "--no-filters", "--stdin-paths"], input="\n".join(paths_copia) + "\n",
                           check=True, capture_output=True, text=True, cwd=a.copia.parent).stdout.split()
    filas, malos = [], []
    for r, b in zip(rutas, blobs):
        ok = indice.get(r) == b == arbol.get(r)
        filas.append({"ruta": r, "blob_copia": b, "ls_files": indice.get(r), "ls_tree_a7d00025": arbol.get(r), "ok": ok})
        if not ok:
            malos.append(r)
    out["blobs"] = {"archivos": len(filas), "e0_rastreados": len(e0), "distintos": malos, "filas": filas}
    out["kg_sha256_copia"] = V.sha_archivo(a.copia / V.KG_REL)

    # PDF: sin blob (ignorados por git); sha256 y comparación byte a byte con el repo
    pdfs = []
    for p in sorted((a.copia / V.PDF_DIR_REL).glob("*.pdf")):
        r = p.relative_to(a.copia).as_posix()
        ign = subprocess.run(["git", "-C", str(a.repo), "--no-optional-locks", "check-ignore", "-v", r],
                             capture_output=True, text=True).stdout.strip()
        pdfs.append({"ruta": r, "sha256": V.sha_archivo(p), "igual_al_repo": filecmp.cmp(p, a.repo / r, shallow=False),
                     "en_git": bool(git(a.repo, "ls-files", "--", r).strip()), "check_ignore": ign})
    out["pdfs"] = pdfs

    # la copia: nombres vedados y enlaces
    vedados, enlaces = [], []
    for raiz, dirs, archivos in os.walk(a.copia):
        for n in dirs + archivos:
            p = Path(raiz) / n
            if p.is_symlink():
                enlaces.append(str(p.relative_to(a.copia)))
            if (n == ".env" or n.startswith(".env.") or n.endswith(".env") or n.startswith("NO_ABRIR_")
                    or "_SOLO_MESA" in n):
                vedados.append(str(p.relative_to(a.copia)))
    out["copia"] = {"nombres_vedados": vedados, "enlaces": enlaces}

    ok = (not malos and all(p["igual_al_repo"] for p in pdfs) and not vedados and not enlaces and not tocados
          and out["kg_sha256_copia"] == V.KG_SHA256 and not out["head"]["status_porcelain_untracked_no"].strip())
    out["ok"] = ok
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"hora": out["hora"], "head": out["head"]["titulo"], "status_vacio":
                      not out["head"]["status_porcelain_untracked_no"].strip(),
                      "diff_593e5db2_HEAD": out["head"]["diff_name_status_593e5db2_HEAD"].splitlines(),
                      "diff_a7d00025_HEAD": out["head"]["diff_name_status_a7d00025_HEAD"].splitlines(),
                      "commits_nuevos_que_tocan_insumos": tocados,
                      "blobs": f"{len(filas) - len(malos)} de {len(filas)} iguales (E0: {len(e0)} rastreados)",
                      "distintos": malos, "kg_sha256": out["kg_sha256_copia"],
                      "pdfs": [(p["ruta"].split("/")[-1], p["sha256"][:8], p["igual_al_repo"], p["en_git"]) for p in pdfs],
                      "vedados": len(vedados), "enlaces": len(enlaces), "ok": ok}, ensure_ascii=False, indent=1))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
