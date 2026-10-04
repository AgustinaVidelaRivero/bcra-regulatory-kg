"""
e0_fuera_p4.py — U-PROMPT-R2, P4 (USD 0): la E0 de los cuatro TOs del estrato fuera de muestra (ayccef, expaef, opefci,
adrei; decisión 19 y P4.a del mandato), producida fuera del repo y no versionada: la legada para el brazo sellado
(`correr_e0.py` sin `--version-e0`) y la e0-r2 para el nuevo (`--version-e0 e0-r2`). La misma E0 sirve a los chunks de
las fichas de F1, que son de tres de esos TOs.

El manifiesto se arma en --trabajo (nunca en el repo), con los PDFs del corpus congelado (`escalado_prep/pdfs/`, sha256
verificado por `manifiesto_corpus.cargar`) y el rol de alcance que declara el catálogo del perfil, sin oráculo.
Escribe en --trabajo: `manifiesto/p4_fuera_muestra.json`, `e0_legada/` y `e0_r2/`, más `e0_fuera_p4.json` con el sha256
de cada `chunks_<to>.json` y los conteos.

Uso (desde la raíz de una COPIA del repo; CLAUDE.md §4, regla l):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p4/e0_fuera_p4.py --trabajo DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e1_extractor"))
import perfil_e1  # noqa: E402

TOS = ("ayccef", "expaef", "opefci", "adrei")
PDFS = "data/experiment/escalado_prep/pdfs"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    w = ap.parse_args().trabajo.resolve()
    if REPO in w.parents or w == REPO:
        raise SystemExit("--trabajo no puede estar dentro del repo")
    rol = perfil_e1.perfil("v3_b54").rol_por_to
    assert all(rol.get(f"{t}.pdf") == perfil_e1.perfil("r2b").rol_por_to.get(f"{t}.pdf") for t in TOS)
    man = {"version": "1", "nombre": "p4_fuera_muestra",
           "descripcion": "U-PROMPT-R2, P4: E0 del estrato fuera de muestra, fuera del repo y no versionada.",
           "tos": [{"id": t, "archivo": f"{t}.pdf", "pdf": f"{PDFS}/{t}.pdf",
                    "sha256_pdf": sha(REPO / PDFS / f"{t}.pdf"),
                    "rol_alcance": (rol.get(f"{t}.pdf") or {}).get("rol_id"), "nombres_remision": []} for t in TOS],
           "orden_corrida": list(TOS), "perfil_e1": "v3_b54",
           "rutas": {"e0_salida": str((w / "e0_legada").relative_to(w))},
           "oraculo": {"mapa_territorio": None, "limitaciones_e0": []},
           "limites": {"tope_global_usd": 0.01, "margen_unidad_usd": 0.0,
                       "estimado_usd": {t: {"e1": 0.0, "e3": 0.0} for t in TOS},
                       "checkpoint_cada": {}, "chequeos_hits": []},
           "tests_respuesta_conocida": None, "sellos": {}, "indice_fragmentos": None}
    (w / "manifiesto").mkdir(parents=True, exist_ok=True)
    mpath = w / "manifiesto" / "p4_fuera_muestra.json"
    mpath.write_text(json.dumps(man, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    res = {"manifiesto": man["tos"], "e0": {}}
    for nombre, extra in (("e0_legada", []), ("e0_r2", ["--version-e0", "e0-r2"])):
        out = w / nombre
        r = subprocess.run([sys.executable, "-B", str(REX / "e0_chunking" / "correr_e0.py"), "--manifiesto", str(mpath),
                            "--salida", str(out), *extra], cwd=REX / "e0_chunking", capture_output=True, text=True,
                           env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})
        (w / f"log_{nombre}.txt").write_text(r.stdout[-20000:] + "\n--- stderr ---\n" + r.stderr[-20000:],
                                            encoding="utf-8")
        if r.returncode != 0:
            raise SystemExit(f"correr_e0 {nombre}: rc {r.returncode} (ver log_{nombre}.txt)")
        res["e0"][nombre] = {t: {"chunks": len(json.loads((out / f"chunks_{t}.json").read_text(encoding="utf-8"))),
                                 "sha256": sha(out / f"chunks_{t}.json")} for t in TOS}
    (w / "e0_fuera_p4.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(res["e0"], ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
