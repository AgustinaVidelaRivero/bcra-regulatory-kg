"""U-ALCANCE-E1, A3 (USD 0; solo lee las corridas y escribe en el paquete): copia al paquete, en
data/experiment/alcance_e1/a3/salidas/, las salidas de los criterios con nombres únicos (unidad y estado), como pide CLAUDE.md
§4.g. Al copiar:
  - las rutas de la máquina pasan a marcadores: la carpeta de la reproducción a `$WR`, la de trabajo a `$W`, el scratchpad a
    `$S` y la carpeta personal a `$HOME` (como sin_rutas_a2.py de A2), para que nada escriba la cuenta del sistema;
  - las salidas de selftest_clave_cache van sin las cuentas de claves de la caché (clave_cache_sin_cuentas_a3.py), y sus
    originales, solo por su sha256;
  - los controles de blobs van sin el mapa de los blobs iguales (solo sus cuentas y lo distinto);
  - los mensajes de la corrida en seco (decenas de MB) van solo por su sha256: se regeneran con mensajes_runner_a3.py.
Uso: python3 -I -B armar_paquete_a3.py <scratchpad> <paquete>
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

S, PAQ = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
W, WR = S / "a3", S / "a3_repro"
M, MR, E0T = W / "med" / "bateria", WR / "med", W / "e0t"
SAL = PAQ / "data" / "experiment" / "alcance_e1" / "a3" / "salidas"
H = PAQ / "data" / "experiment" / "alcance_e1" / "a3" / "scripts"
SAL.mkdir(parents=True, exist_ok=True)


def marcar(t: str) -> str:
    for x, y in ((WR, "$WR"), (W, "$W"), (S, "$S")):
        for v in sorted({str(x), os.path.realpath(x)}, key=len, reverse=True):
            t = t.replace(v, y)
    return t.replace(os.path.expanduser("~"), "$HOME")


def texto(origen: Path, nombre: str) -> None:
    (SAL / nombre).write_text(marcar(origen.read_text(encoding="utf-8")), encoding="utf-8")


def json_sin(origen: Path, nombre: str, quitar: tuple) -> None:
    d = json.loads(origen.read_text(encoding="utf-8"))
    for k in quitar:
        d.pop(k, None)
    (SAL / nombre).write_text(marcar(json.dumps(d, ensure_ascii=False, indent=1)) + "\n", encoding="utf-8")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


COPIAS = [  # (origen, nombre en el paquete)
    (M / "bateria_a3.log", "bateria_a3.txt"),
    (W / "med" / "lote_e0_consola.txt", "lote_e0_consola_a3.txt"),
    (E0T / "lote_a3.log", "lote_e0_a3.txt"),
    (E0T / "control_e0_S2a.json", "control_e0_contra_S0-6b_a3.json"),
    (E0T / "comparacion_foto_lote.json", "foto_repo_lote_e0_comparacion_a3.json"),
    (M / "pdfs_copia_head.json", "pdfs_contra_manifiestos_a3.json"),
    (M / "reporte_derivado_corrida1.json", "reporte_derivado_tandas_1_final_a3.json"),
    (M / "diff_derivado_head_a3.txt", "diff_derivado_head_contra_a3.txt"),
    (M / "filas_tanda_final_a3.json", "filas_tanda_final_parser_propio_a3.json"),
    (M / "sellos_a3_proceso1" / "sellos_a2.json", "sellos_candado_a3.json"),
    (M / "sellos_head" / "sellos_a2.json", "sellos_candado_head_mismo_metodo_a3.json"),
    (M / "sellos_a3_verificacion" / "verificacion_sellos_a2.json", "verificacion_sellos_candado_a3.json"),
    (M / "selftest_prompt_r2b_HEAD_sobre_HEAD.txt", "selftest_prompt_r2b_HEAD_sobre_HEAD_a3.txt"),
    (M / "selftest_prompt_r2b_a3.txt", "selftest_prompt_r2b_a3.txt"),
    (M / "selftest_prompt_r2b_a3_con_codigo_HEAD.txt", "selftest_prompt_r2b_a3_con_codigo_HEAD.txt"),
    (M / "control_negativo_selftest_prompt_r2b_a3.json", "control_negativo_selftest_prompt_r2b_a3.json"),
    (M / "candado_del_derivado_con_codigo_HEAD.txt", "candado_del_derivado_con_codigo_HEAD_a3.txt"),
    (M / "seco" / "resumen_head.json", "resumen_mensajes_runner_head_a3.json"),
    (M / "seco" / "resumen_a3.json", "resumen_mensajes_runner_a3.json"),
    (M / "medicion_a3.json", "medicion_mensajes_tres_tandas_a3.json"),
    (M / "comparacion_consola.txt", "comparacion_mensajes_consola_a3.txt"),
    (M / "comparacion_lista_tanda1_a3.json", "comparacion_lista_tanda1_a3.json"),
    (M / "cadena_78_a3.json", "cadena_78_rutas_a3.json"),
    (MR / "reproduccion_a3.log", "reproduccion_a3.txt"),
    (MR / "comparacion_con_la_oficial.json", "comparacion_reproduccion_con_la_oficial_a3.json"),
    (MR / "comparacion_foto_repo.json", "foto_repo_reproduccion_comparacion_a3.json"),
]
for s in ("catalogo_unico", "reresolver_catalogo", "cablev3", "manifiesto"):
    for e in ("head", "a3"):
        COPIAS.append((M / f"selftest_{s}_{e}.txt", f"selftest_{s}_{e}_a3.txt"))
for origen, nombre in COPIAS:
    texto(origen, nombre)

for c in ("head", "a3"):
    json_sin(M / f"blobs_copia_{c}_contra_base.json", f"blobs_copia_{c}_contra_base_a3.json", ("blobs_iguales",))
json_sin(MR / "blobs_copia_nueva_contra_base.json", "blobs_copia_nueva_reproduccion_contra_base_a3.json", ("blobs_iguales",))

fotos = []
for p in sorted((M / "fotos").glob("*_comparacion.json")):
    d = json.loads(p.read_text(encoding="utf-8"))
    fotos.append({"paso": p.name.replace("_comparacion.json", ""), **d})
(SAL / "fotos_repo_bateria_comparaciones_a3.json").write_text(json.dumps(fotos, ensure_ascii=False, indent=1) + "\n",
                                                              encoding="utf-8")

CC = H / "clave_cache_sin_cuentas_a3.py"
originales = []
for origen, nombre in ((M / "selftest_clave_cache_head.json", "selftest_clave_cache_head_sin_cuentas_a3.json"),
                       (M / "selftest_clave_cache_a3_1.json", "selftest_clave_cache_a3_sin_cuentas_a3.json"),
                       (M / "consola_clave_cache_head.txt", "consola_selftest_clave_cache_head_sin_cuentas_a3.txt"),
                       (M / "consola_clave_cache_a3_1.txt", "consola_selftest_clave_cache_a3_sin_cuentas_a3.txt")):
    subprocess.run([sys.executable, "-I", "-B", str(CC), "retirar", str(origen), str(SAL / nombre)], check=True)
for p in ("selftest_clave_cache_head.json", "selftest_clave_cache_a3_1.json", "selftest_clave_cache_a3_2.json",
          "consola_clave_cache_head.txt", "consola_clave_cache_a3_1.txt", "consola_clave_cache_a3_2.txt"):
    originales.append(f"{sha(M / p)}  {p}")
(SAL / "sha256_selftest_clave_cache_originales_a3.txt").write_text(
    "# sha256 de las salidas de selftest_clave_cache de la batería oficial, que no van al paquete porque traen cuentas de\n"
    "# claves de la caché que incluyen la extracción de la tanda 1 (van sin ellas, en *_sin_cuentas_a3.*).\n"
    + "\n".join(originales) + "\n", encoding="utf-8")
(SAL / "sha256_mensajes_seco_a3.txt").write_text(
    "# sha256 de los mensajes de E1 de la corrida en seco (mensajes_runner_a3.py), una fila por unidad; se regeneran.\n"
    + "\n".join(f"{sha(M / 'seco' / p)}  {p}" for p in ("mensajes_head.jsonl", "mensajes_a3.jsonl")) + "\n",
    encoding="utf-8")
print("salidas:", len(list(SAL.iterdir())))
