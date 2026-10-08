"""
preparar_espejo_P.py — U-MED-UMBRALES, etapa P: arma la copia del repo sobre la que corren los demás scripts del piloto
(CLAUDE.md §4.l: se copian archivos, nunca enlaces simbólicos). Corre desde la raíz del repo y escribe solo en --destino.

  - cada insumo rastreado: `git show <commit>:<ruta>` (HEAD salvo la enmienda, que se toma del commit de la firma,
    CLAUDE.md §4.k);
  - los PDFs de los diez TOs (ignorados por .gitignore:35): copia de bytes, con su sha256; los de los cinco TOs nuevos se
    controlan contra data/experiment/escalado_prep/manifest_pdfs.sha256 (rastreado);
  - el código del piloto (los .py de --codigo) en data/experiment/med_umbrales/p/code/ de la copia.
Escribe --destino/insumos_espejo_P.json con la ruta, el origen y el sha256 de cada archivo.

  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B preparar_espejo_P.py --destino DIR --codigo DIR_CODIGO
"""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
from pathlib import Path

TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
ARCHIVO_DEV = {"cap": "TO_capitales_minimos_actual.pdf", "cla": "TO_clasificacion_deudores_actual.pdf",
               "ext": "TO_exterior_cambios_actual.pdf", "pro": "TO_proteccion_usuarios_servicios_financieros_actual.pdf",
               "ric": "TO_regimen_informativo_contable_mensual_actual.pdf"}
REX = "data/experiment/reextraccion_v2"
FIJOS = [f"{REX}/corpus_tanda0/ens_diez_r2b_sincola/r2/kg.json",
         f"{REX}/corpus_tanda0/ens_diez_r2b_sincola/r2/reporte_ensamblado_r2.json",
         "data/experiment/pyd_r2/code/reglas_comparacion.py",
         f"{REX}/e2_reduce/e2_lib.py",
         "data/experiment/grafo_v2/code/schema.py",
         "data/experiment/grafo_v2/esquema_v2_clases.json",
         "data/experiment/escalado_prep/manifest_pdfs.sha256",
         "data/experiment/pyd_r2/code/validador_r2.py",
         "data/experiment/pyd_r2/code/modelos_r2.py",
         f"{REX}/e1_extractor/comun_e1.py",
         "data/experiment/catalogo_unico/catalogo_sujetos_r2.json",
         "data/experiment/catalogo_unico/generados_r2/enums_tool_schema_r2.json"]
POR_TO = [f"{REX}/e0_chunking/salida_tanda0_r2b/chunks_{{to}}.json",
          f"{REX}/corpus_tanda0/salida_r2b/{{to}}/extracciones_e1_compact.jsonl",
          f"{REX}/corpus_tanda0/salida_r2b/{{to}}/finales.jsonl",
          f"{REX}/corpus_tanda0/salida_r2b/{{to}}/reintentos_e3.jsonl",
          f"{REX}/corpus_tanda0/salida_r2b/{{to}}/particiones_por_corte.json"]
ENMIENDA = ("a0f9815", "docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def rastreado(commit: str, ruta: str) -> bool:
    r = subprocess.run(["git", "cat-file", "-e", f"{commit}:{ruta}"], capture_output=True)
    return r.returncode == 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--destino", type=Path, required=True)
    ap.add_argument("--codigo", type=Path, required=True)
    a = ap.parse_args()
    head = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True, check=True).stdout.strip()
    registro, ausentes = [], []

    def de_git(commit: str, ruta: str) -> None:
        b = subprocess.run(["git", "show", f"{commit}:{ruta}"], capture_output=True, check=True).stdout
        d = a.destino / ruta
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_bytes(b)
        registro.append({"ruta": ruta, "origen": f"git show {commit}:{ruta}", "sha256": sha(b)})

    for ruta in FIJOS:
        de_git(head, ruta)
    for to in TOS:
        for plantilla in POR_TO:
            ruta = plantilla.format(to=to)
            if rastreado(head, ruta):
                de_git(head, ruta)
            else:
                ausentes.append(ruta)
    de_git(*ENMIENDA)

    manifiesto = {}
    for x in (a.destino / "data/experiment/escalado_prep/manifest_pdfs.sha256").read_text(encoding="utf-8").splitlines():
        if x.strip():
            h, nombre = x.split()[:2]
            manifiesto[nombre] = h
    for to in TOS:
        ruta = f"data/experiment/subset/{ARCHIVO_DEV[to]}" if to in ARCHIVO_DEV else f"data/experiment/escalado_prep/pdfs/{to}.pdf"
        b = Path(ruta).read_bytes()
        h = sha(b)
        control = None
        if to not in ARCHIVO_DEV:
            control = manifiesto.get(f"{to}.pdf") == h
            if not control:
                raise SystemExit(f"{ruta}: sha256 {h} distinto del de manifest_pdfs.sha256")
        d = a.destino / ruta
        d.parent.mkdir(parents=True, exist_ok=True)
        d.write_bytes(b)
        registro.append({"ruta": ruta, "origen": "copia de bytes del árbol de trabajo (ignorado por .gitignore:35)",
                         "sha256": h, "igual_a_manifest_pdfs": control})

    dcod = a.destino / "data/experiment/med_umbrales/p/code"
    dcod.mkdir(parents=True, exist_ok=True)
    for p in sorted(a.codigo.glob("*.py")):
        shutil.copyfile(p, dcod / p.name)
        registro.append({"ruta": f"data/experiment/med_umbrales/p/code/{p.name}", "origen": "código del piloto",
                         "sha256": sha(p.read_bytes())})

    out = {"head": head, "archivos": registro, "rastreados_ausentes_en_head": ausentes,
           "nota": "rastreados_ausentes_en_head: archivos por TO que no existen en HEAD (por ejemplo, un TO sin partes "
                   "por corte o sin reintentos); los lectores los tratan como vacíos"}
    (a.destino / "insumos_espejo_P.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(len(registro), "archivos;", len(ausentes), "ausentes en HEAD")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
