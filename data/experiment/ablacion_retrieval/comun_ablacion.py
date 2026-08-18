"""
comun_ablacion.py — Infraestructura común de la ablación de retrieval (U-A1.3,
plan de tesis carril A / bloque A1 / issue #5).

Este directorio NO edita ningún archivo de fuera: importa el cuarteto hasheado
(`data/experiment/evaluacion/`), el pipeline de pares sintéticos
(`data/experiment/exploracion/sinteticas/`), el backend Neo4j de U-A1.1
(`data/experiment/neo4j/`) y las tools v2 de U-A1.2 (`data/experiment/agente_v2/`)
tal cual están en el repo, y CONGELA por sha256 cada pieza de la que depende el
pre-registro (`preregistro_ablacion.md` §1–§2). `verificar_piezas()` aborta
ruidosamente si alguna pieza sellada cambió: la config de la ablación no se
ajusta mirando resultados, ni por accidente.

Provee:
  - rutas de los directorios reusados y del propio;
  - `PIEZAS_SELLADAS`: {nombre: (ruta relativa al repo, sha256 esperado)};
  - `sha256_de`, `shas_actuales`, `verificar_piezas`;
  - `KG_REFINADO_*` (ruta y sha del grafo de la ablación).
"""

from __future__ import annotations

import hashlib
import sys
from pathlib import Path

ABLACION_DIR = Path(__file__).resolve().parent            # data/experiment/ablacion_retrieval
EXPERIMENT_DIR = ABLACION_DIR.parent                      # data/experiment
REPO_DIR = EXPERIMENT_DIR.parents[1]
EVAL_DIR = EXPERIMENT_DIR / "evaluacion"
SINTETICAS_DIR = EXPERIMENT_DIR / "exploracion" / "sinteticas"
EXPLORACION_DIR = EXPERIMENT_DIR / "exploracion"
NEO4J_DIR = EXPERIMENT_DIR / "neo4j"
AGENTE_V2_DIR = EXPERIMENT_DIR / "agente_v2"
EV2_CODE_DIR = EXPERIMENT_DIR / "ev2_corrida" / "code"

# Orden de inserción: los módulos del pipeline de sintéticas se llaman `comun`,
# `sampler`, `metrica`…; los de neo4j/agente_v2 no colisionan con ellos.
for _p in (str(SINTETICAS_DIR), str(EXPLORACION_DIR), str(EVAL_DIR),
           str(NEO4J_DIR), str(AGENTE_V2_DIR), str(EV2_CODE_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

# Salidas propias
MUESTREO_DIR = ABLACION_DIR / "muestreo"
CELDAS_DIR = ABLACION_DIR / "celdas"
PARES_DIR = ABLACION_DIR / "pares"
CACHE_DIR = ABLACION_DIR / "cache"        # dbs de la fase B (gitignore local)

# Grafo de la ablación: KG-Refinado (nomenclatura docs/nomenclatura_grafos.md)
KG_REFINADO_PATH = EXPERIMENT_DIR / "grafo_v2" / "reensamblado_v3" / "kg.json"
KG_REFINADO_SHA256 = "26fac8b49f6c08c1aa364b47273d36958d831f240d4e6b4ee7700b6a0bff3571"

SEMILLA_V3 = "sinteticas-faseA-v3"


def sha256_de(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def rel_repo(path: Path | str) -> str:
    try:
        return str(Path(path).resolve().relative_to(REPO_DIR))
    except ValueError:
        return str(path)


# --------------------------------------------------------------------------- #
# Piezas selladas por sha256 (medidas al inicio de U-A1.3, HEAD 49f82b7)      #
# --------------------------------------------------------------------------- #
# Toda pieza de la que depende el diseño de la ablación. Si una cambia, la
# verificación falla y el pre-registro deja de describir lo que se corre.
PIEZAS_SELLADAS: dict[str, tuple[Path, str]] = {
    # cuarteto hasheado (intocable)
    "loader.py":     (EVAL_DIR / "loader.py",    "5aba8b7a0aa46e8d5c4c83b33884b8cae7d0a099884a7d3bc935de4d3097af8b"),
    "harness.py":    (EVAL_DIR / "harness.py",   "fd267e833866f86850e43130e627b08d78e05523b97484696de0ab0c8c9fba9e"),
    "judge.py":      (EVAL_DIR / "judge.py",     "7169145aaeb3f2d90a7e3873964378aa6520c5688fed136cf5a79ea63b589eaa"),
    "llm_cache.py":  (EVAL_DIR / "llm_cache.py", "fc86b0e48df464d01d87aa1d8067168d2d522f66ead53f594092a16484c22752"),
    # grafo de la ablación
    "kg_refinado.json": (KG_REFINADO_PATH, KG_REFINADO_SHA256),
    # backend Neo4j (U-A1.1) — config del retriever
    "neo4j/indices.py":     (NEO4J_DIR / "indices.py",     "215b4b8783345479f2b9e730c6e6b6e0be740163ba9a5796377b4672335ace26"),
    "neo4j/neo4j_index.py": (NEO4J_DIR / "neo4j_index.py", "5f38db1b915caf8a4cd71e0f7f0d281ba5a9ca6867d327a9e0f4aac67cd2d0c1"),
    "neo4j/grafos.py":      (NEO4J_DIR / "grafos.py",      "eb78280b1358db095be0ab08bfa8ff934bf881f86b80c9b00a40e06d9cec8d57"),
    "neo4j/agente_neo4j.py": (NEO4J_DIR / "agente_neo4j.py", "403a9b4295961f461c73a35b46ccc4d973a20cefdddf2ae97b50231dd7a3576a"),
    # paquete tools v2 (U-A1.2) — factor "tools"
    "agente_v2/tools_v2.py":        (AGENTE_V2_DIR / "tools_v2.py",        "22d672709a59678cf070c1af9f1ee6240bf0cdb860a5d23600fd7a51ff9cf16e"),
    "agente_v2/specs_tools_v2.json": (AGENTE_V2_DIR / "specs_tools_v2.json", "88b696258b69eaee1b047b235b026763380ea9f14707d31398e6ab2f4d598a55"),
    "agente_v2/agente_v2.py":       (AGENTE_V2_DIR / "agente_v2.py",       "7beb0037d45b317cc8b0e03fa996b54d21fdda9110ceebcc3ee4ef0d1f3e88a4"),
    "agente_v2/specs_diff_v1_v2.txt": (AGENTE_V2_DIR / "specs_diff_v1_v2.txt", "28bad98fb67b5b710c4cef7fda8a9eaec0ababda56ef74d1e8eb98d1b5772f32"),
    # pipeline de pares sintéticos (a611ed2 / 5ceb816) — se importa, no se edita
    "sinteticas/comun.py":         (SINTETICAS_DIR / "comun.py",         "94c1d4fe0d31e75c5b673889af86b7bf3dbeee53e8142fef5189d0f8d067cca3"),
    "sinteticas/sampler.py":       (SINTETICAS_DIR / "sampler.py",       "01b0f0e64dec5d57b80c0a6cd6d29ba3e4986cccc4ed4fbfae4be10a057ee05f"),
    "sinteticas/generador.py":     (SINTETICAS_DIR / "generador.py",     "45f72fa4b8510ff06c2613d66421168f9e17af7a46e3047e4a3539b27520b82f"),
    "sinteticas/validador.py":     (SINTETICAS_DIR / "validador.py",     "6791996e59e7a66e4d733fde7b2856b1e6de375cd846607a1921c15500b4ef42"),
    "sinteticas/resolucion.py":    (SINTETICAS_DIR / "resolucion.py",    "afe66ee951cd847bc4e02486c8086b06e7a588c59a48b385b2245e6214b6c51b"),
    "sinteticas/metrica.py":       (SINTETICAS_DIR / "metrica.py",       "059f411b0f429dd371635bbcf9c382c1321342e6e88f89cd31bd51a154febb7e"),
    "sinteticas/estimacion.py":    (SINTETICAS_DIR / "estimacion.py",    "0ffad2ad34f45cc6f6dc38945eb738cd7a9fbb40170c63242d5710a9545f6fad"),
    "sinteticas/runner_faseB.py":  (SINTETICAS_DIR / "runner_faseB.py",  "0818d3404811f5f9f3781bba8190155c33b8722d1d0c7e2fa442415ddd23569a"),
    "sinteticas/cliente_faseB.py": (SINTETICAS_DIR / "cliente_faseB.py", "e2191ca654008392c0b201edf92c8cd508613c78280cdaf75d7c0017030148fe"),
    "exploracion/validar_anclas.py": (EXPLORACION_DIR / "validar_anclas.py", "9efda31a0fdb251050aaded467b70b13ac2e7af598671e9fe78a0289b6c8aebc"),
    "exploracion/mapa_territorio_quemado_5TOs_5sets.json": (
        EXPLORACION_DIR / "mapa_territorio_quemado_5TOs_5sets.json",
        "d94f1c99e7d7ce14fe7d526f7acf5b33a808c1b45a283fb4e167ad8d8800e88c"),
    # métrica de navegabilidad EV2 (5b02d22) — replay estándar + fuerte
    "ev2_corrida/code/metrica_ev2.py": (EV2_CODE_DIR / "metrica_ev2.py", "5c629c00e993bd3a0e7b1aafdf95ae5fcf1cd695dff1c8018f1b16a766b99c75"),
}


def shas_actuales() -> dict[str, dict]:
    out = {}
    for nombre, (path, esperado) in PIEZAS_SELLADAS.items():
        actual = sha256_de(path) if path.exists() else None
        out[nombre] = {"path": rel_repo(path), "sha256_sellado": esperado,
                       "sha256_actual": actual, "ok": actual == esperado}
    return out


def verificar_piezas(verbose: bool = True) -> dict[str, dict]:
    """Aborta si alguna pieza sellada difiere del sha registrado."""
    res = shas_actuales()
    malas = [n for n, r in res.items() if not r["ok"]]
    if verbose:
        for n, r in res.items():
            print(f"  {'OK ' if r['ok'] else 'DIF'}  {r['sha256_actual'] or '-':.16}…  {n}")
    if malas:
        raise RuntimeError("piezas selladas con sha distinto: " + ", ".join(malas))
    return res


if __name__ == "__main__":
    print("verificación de piezas selladas (U-A1.3):")
    verificar_piezas()
    print("todas OK")
