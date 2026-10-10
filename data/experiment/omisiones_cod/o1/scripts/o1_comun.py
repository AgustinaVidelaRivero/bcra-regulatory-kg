"""U-OMISIONES-COD, O1 — utilidades comunes de la medición previa (USD 0, sin API ni Neo4j).

Corre desde la raíz de una COPIA del repo: importa `ensamblar_tanda0` de la copia (el mismo camino de imports que el
ensamblado: el módulo arma su propio sys.path desde su ubicación) y arma las redirecciones del manifiesto como
`ensamblar_manifiesto_r2`. No escribe en la copia: las salidas van a la ruta que se pase.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

X = Path("data/experiment/reextraccion_v2")
T = X / "corpus_tanda0"
MAN = X / "manifiestos"
E0B = X / "e0_chunking" / "salida_tanda0_r2b"
ENTRADA_R2B = T / "salida_r2b"
MANIFIESTOS = {"diez": MAN / "tanda0_ens_diez_r2b.json", "diez_sincola": MAN / "tanda0_ens_diez_r2b_sincola.json",
               "desarrollo": MAN / "tanda0_ens_desarrollo_r2b.json",
               "desarrollo_sincola": MAN / "tanda0_ens_desarrollo_r2b_sincola.json"}


def raiz_copia() -> Path:
    """La copia es el directorio de trabajo: la medición se corre desde su raíz."""
    r = Path.cwd().resolve()
    if not (r / "data" / "experiment" / "tanda0" / "code" / "ensamblar_tanda0.py").exists():
        raise SystemExit("correr desde la raíz de una copia del repo")
    if (r / ".git").exists():
        raise SystemExit("la raíz tiene .git: esto parece el repo, no una copia")
    return r


def ensamblador():
    r = raiz_copia()
    p = str(r / "data" / "experiment" / "tanda0" / "code")
    if p not in sys.path:
        sys.path.insert(0, p)
    import ensamblar_tanda0 as ENS  # noqa: PLC0415
    assert Path(ENS.__file__).resolve().is_relative_to(r), ENS.__file__
    return ENS


def contexto(nombre: str = "diez", cat_resolucion=None):
    """(ENS, man, perfil, plan, M, V, RCMP, RC): lo que `ensamblar_manifiesto_r2` arma antes de la cadena."""
    ENS = ensamblador()
    r = raiz_copia()
    man = ENS.MC.cargar(r / MANIFIESTOS[nombre])
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = ENS.E4.modulo_modelos_r2()
    V = ENS.E4.modulo_validador_r2()
    import reglas_comparacion as RCMP  # noqa: PLC0415
    import runner_corpus as RC  # noqa: PLC0415
    for mod in (M, V, RCMP, RC):
        assert Path(mod.__file__).resolve().is_relative_to(r), mod.__file__
    cat = cat_resolucion if cat_resolucion is not None else ENS.E4.catalogo_r2()
    plan = ENS.plan_redirecciones_r2(man, perfil, r / ENTRADA_R2B, r / "_o1_no_se_escribe" / "r2", cat, M)
    return ENS, man, perfil, plan, M, V, RCMP, RC


def registros(ENS, perfil, RC, con_cola: bool = True) -> tuple[dict, dict]:
    """{to: registros de entrada_r2 (con la cola descartada si con_cola es False)}, {chunk_id: chunk con partes}.
    Llamar dentro de `ENS.redirigido(plan)`."""
    validar, _pol = RC.validador_perfil_r2(perfil)
    regs, chunks = {}, {}
    for to in ENS.C.TOS_ORDEN:
        ch = ENS._chunks_r2(to)
        chunks.update({c["id"]: c for c in ch})
        rr = RC.entrada_r2(to, ENS.C.SALIDA / to, ch, perfil, validar)
        regs[to], _ = ENS.descartar_cola_r2(rr, con_cola)
    return regs, chunks


def wilson(k: int, n: int, z: float = 1.959964) -> list:
    if n == 0:
        return [None, None]
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return [round(c - h, 4), round(c + h, 4)]


def sha256_path(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def escribir_json(p: Path, obj) -> str:
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    s = json.dumps(obj, ensure_ascii=False, indent=1) + "\n"
    p.write_text(s, encoding="utf-8")
    return hashlib.sha256(s.encode("utf-8")).hexdigest()
