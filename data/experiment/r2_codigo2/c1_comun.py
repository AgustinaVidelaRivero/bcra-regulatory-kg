"""U-R2-CODIGO-2, C1 — piezas comunes de los scripts de diagnóstico (USD 0, sin API ni Neo4j).

La cadena r2 de los grafos r2a corre en memoria, como en `medicion_r2a/m3_cadena_instrumentada.py`: misma redirección
que `ensamblar_tanda0.ensamblar_manifiesto_r2`, sin escribir nada. Los objetos que la cadena escribiría (registro de
remisiones, de Comunicaciones, pasada residual de E4) se capturan en un diccionario. Los parches son reemplazos de
atributos de módulos importados, aplicados solo durante la corrida y restaurados al terminar: ningún módulo de la
cadena se edita.

Control de cada corrida sin parches: el sha256 del grafo tiene que ser el del grafo versionado (KG-Tanda0-Diez-r2a
`99fe2bfa…`, KG-Tanda0-Desarrollo-r2a `93a7af72…`).
"""
from __future__ import annotations

import contextlib
import hashlib
import json
import sys
import tempfile
from collections import OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
REX = "data/experiment/reextraccion_v2"
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ENS          # noqa: E402  (sin editar; agrega al path los módulos de la cadena)

REF = ENS.REF
ENTRADA = f"{REX}/corpus_tanda0/salida_dirigida"
E0_R2 = f"{REX}/e0_chunking/salida_tanda0_r2"
E0_LEGADA = f"{REX}/e0_chunking/salida_tanda0"
GRAFOS = OrderedDict([
    ("diez", {"manifiesto": f"{REX}/manifiestos/tanda0_ens_diez.json",
              "dir": f"{REX}/corpus_tanda0/ens_diez_r2a/r2",
              "sha256": "99fe2bfa0de05704e4c636bdf9b0455a30e29b378e3b0e61eadc49dad3f7c649"}),
    ("desarrollo", {"manifiesto": f"{REX}/manifiestos/tanda0_ens_desarrollo.json",
                    "dir": f"{REX}/corpus_tanda0/ens_desarrollo_r2a/r2",
                    "sha256": "93a7af7279a415ee72cfec547bcd080d4c85a96746e219ed94dea4239007e8dd"}),
])


def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


@contextlib.contextmanager
def parcheado(parches: list[tuple] | None):
    """(módulo, atributo, valor) aplicados durante el bloque y restaurados al salir."""
    parches = parches or []
    originales = [(m, a, getattr(m, a)) for m, a, _ in parches]
    try:
        for m, a, v in parches:
            setattr(m, a, v)
        yield
    finally:
        for m, a, v in originales:
            setattr(m, a, v)


def correr_r2(nombre: str, parches: list[tuple] | None = None) -> dict:
    """Cadena r2 del grafo `nombre` en memoria. Devuelve {kg, sha256, resumen, escritos}; `escritos` tiene lo que la
    cadena escribiría con `w` (nombre de archivo → objeto)."""
    cfg = GRAFOS[nombre]
    man = ENS.MC.cargar(RAIZ / cfg["manifiesto"])
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = ENS.E4.modulo_modelos_r2()
    cat = ENS.E4.catalogo_r2()
    escritos: dict = {}

    def w(n: str, obj) -> None:
        escritos[n] = json.loads(json.dumps(obj, ensure_ascii=False))

    with tempfile.TemporaryDirectory() as tmp:
        plan = ENS.plan_redirecciones_r2(man, perfil, RAIZ / ENTRADA, Path(tmp) / "r2", cat, M)
        with ENS.redirigido(plan), parcheado(parches):
            res = ENS.correr_cadena_r2(man, perfil, w, None, RAIZ / E0_R2)
    return {"kg": res["kg"], "sha256": res["sha256"], "resumen": res["resumen"], "escritos": escritos}


def control_sha(nombre: str, corrida: dict) -> dict:
    """La corrida sin parches reproduce el grafo versionado."""
    cfg = GRAFOS[nombre]
    en_disco = sha256_path(RAIZ / cfg["dir"] / "kg.json")
    return {"sha256_corrida": corrida["sha256"], "sha256_versionado": en_disco,
            "sha256_esperado": cfg["sha256"],
            "reproduce": corrida["sha256"] == en_disco == cfg["sha256"]}


def tripla(e: dict) -> tuple:
    return (e["source"], e["relation"], e["target"])


def diferencia_aristas(kg_a: dict, kg_b: dict, relacion: str | None = None) -> dict:
    """Aristas de `kg_a` que no están en `kg_b` (quitadas) y al revés (agregadas), por (source, relation, target)."""
    a = {tripla(e): e for e in kg_a["edges"] if relacion is None or e["relation"] == relacion}
    b = {tripla(e): e for e in kg_b["edges"] if relacion is None or e["relation"] == relacion}
    return {"quitadas": [a[k] for k in sorted(set(a) - set(b))],
            "agregadas": [b[k] for k in sorted(set(b) - set(a))]}


def escribir_json(ruta: Path, obj) -> None:
    Path(ruta).write_text(json.dumps(obj, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
