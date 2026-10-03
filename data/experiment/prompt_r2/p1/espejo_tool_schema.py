"""
espejo_tool_schema.py — U-PROMPT-R2, P1 (USD 0): tool schema de BORRADOR con
los cambios de las decisiones 15 a 17 del mandato, para medirlo antes de P2.

No edita el repo. Copia (sin enlaces simbólicos; CLAUDE.md §4 l) a un espejo
fuera del repo `modelos_r2.py`, `generar_r2.py`, la política y los dos
archivos del catálogo r2 que el modelo lee con candado; aplica en la copia
los cambios declarados abajo (cada ancla única) y corre `generar_r2.py
--salida` dos veces:
  - `generados_hoy/`: el modelo vigente sin cambios (control de la decisión
    13: el tool schema y los enums deben ser los del repo);
  - `generados_d15_17/`: el modelo con las decisiones 15 a 17.
Los cambios que haga P2 en `modelos_r2.py` son los de esta lista, salvo lo que
el FRENO P1 decida distinto (el `tramo` del TextoOrdenado, decisión abierta).

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p1/espejo_tool_schema.py \
      --espejo <dir fuera del repo> --salida <dir>
"""
from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]

COPIAS = (
    "data/experiment/pyd_r2/code/modelos_r2.py",
    "data/experiment/pyd_r2/code/generar_r2.py",
    "data/experiment/pyd_r2/politica_campos_r2.json",
    "data/experiment/catalogo_unico/catalogo_sujetos_r2.json",
    "data/experiment/catalogo_unico/generados_r2/enums_tool_schema_r2.json",
)

# (decisión, ancla en modelos_r2.py, texto nuevo)
CAMBIOS: tuple[tuple[str, str, str], ...] = (
    ("16: Comunicacion.tipo y numero salen del tool schema",
     '''class PropsComunicacionE1(_PropsE1):
    codigo: str = Field(default=None, description='Código de la Comunicación, ej. "A-7825".')
    tipo: Literal[COMUNICACION_TIPO] = Field(  # type: ignore[valid-type]
        default=None, description='"A", "B" o "C"; "externa" para una ley, un decreto o una resolución.')
    numero: int = Field(default=None, description="Número de la Comunicación.")
''',
     '''class PropsComunicacionE1(_PropsE1):
    # Decisión 16 (protocolo D7): tipo y numero se derivan en código desde codigo.
    codigo: str = Field(default=None, description=(
        'Código de la Comunicación, ej. "A-7825"; para una ley, un decreto o una resolución, su denominación '
        'tal como la cita el texto.'))
'''),
    ("16: el TextoOrdenado sin properties (materia, archivo y version salen)",
     '''class PropsTextoOrdenadoE1(_PropsE1):
    materia: str = Field(default=None)
    archivo: str = Field(default=None)
    version: str = Field(default=None)


''', ''),
    ("16: el TextoOrdenado sin properties (la entidad)",
     '''class TextoOrdenadoE1(_EntidadE1):
    type: Literal["TextoOrdenado"]
    properties: PropsTextoOrdenadoE1 = Field(default=None)
''',
     '''class TextoOrdenadoE1(_EntidadE1):
    # Decisión 16 (protocolo D7): materia, archivo y version se derivan en código desde E0.
    type: Literal["TextoOrdenado"]
'''),
    ("16: Definicion.termino literal",
     '''class PropsDefinicionE1(_PropsE1):
    termino: str = Field(default=None)
''',
     '''class PropsDefinicionE1(_PropsE1):
    termino: str = Field(default=None, description="Término definido, copiado tal cual lo nombra el texto.")
'''),
    ("15: descripción del tramo de evidencia",
     '''_DESC_OTRAS = (''',
     '''_DESC_TRAMO = ("Tramo del texto que funda la entidad, copiado tal cual: el más corto que la sostenga "
               "por sí solo.")
_DESC_OTRAS = ('''),
    ("15: tramo de evidencia por entidad (todas salvo el TextoOrdenado: decisión abierta del FRENO P1)",
     '''    otras_propiedades: dict[str, str] = Field(default=None, description=_DESC_OTRAS)


class ComunicacionE1(_EntidadE1):''',
     '''    otras_propiedades: dict[str, str] = Field(default=None, description=_DESC_OTRAS)


class _EntidadConTramoE1(_EntidadE1):
    # Decisión 15 (protocolo D6): tramo literal de evidencia por entidad.
    tramo: str = Field(description=_DESC_TRAMO)


class ComunicacionE1(_EntidadConTramoE1):'''),
) + tuple(
    (f"15: {t} hereda el tramo", f"class {t}E1(_EntidadE1):", f"class {t}E1(_EntidadConTramoE1):")
    for t in ("Operacion", "Restriccion", "Excepcion", "Obligacion", "Potestad", "Condicion", "Definicion")
) + (
    ("17: otras_propiedades en las relaciones",
     '''    sujeto_propuesto_padre_sugerido: SujetoIdR2 = Field(default=None, description=(  # type: ignore[valid-type]
        "Opcional, sin sujeto_id: id del catálogo sugerido como padre del sujeto mencionado."))
''',
     '''    sujeto_propuesto_padre_sugerido: SujetoIdR2 = Field(default=None, description=(  # type: ignore[valid-type]
        "Opcional, sin sujeto_id: id del catálogo sugerido como padre del sujeto mencionado."))
    otras_propiedades: dict[str, str] = Field(default=None, description=_DESC_OTRAS)
'''),
    ("17: source y destino en la omisión; la nota pide el tipo o el predicado",
     '''    nota: str = Field(default=None, description="Por qué quedó afuera.")
''',
     '''    nota: str = Field(default=None, description=(
        "Por qué quedó afuera; en fuera_de_tipos y relacion_sin_predicado, el tipo o el predicado que se habría usado."))
    source: str = Field(default=None, description=(
        "Solo relacion_sin_predicado: local_id de la entidad de origen, si se extrajo."))
    destino: str = Field(default=None, description=(
        "Solo relacion_sin_predicado: local_id de la entidad de destino, si se extrajo."))
'''),
    ("15: la descripción del tool nombra el tramo",
     '''"cerrado de sujetos). Todo elemento lleva `punto`. Los umbrales van como tramos literales; la "
    "mención del sujeto, tal cual aparece; las omisiones, con categoría y tramo.")''',
     '''"cerrado de sujetos). Todo elemento lleva `punto`; toda entidad salvo el TextoOrdenado, el tramo literal que la "
    "funda. Los umbrales van como tramos literales; la mención del sujeto, tal cual aparece; las omisiones, con "
    "categoría y tramo.")'''),
)


def armar_espejo(espejo: Path) -> None:
    espejo = espejo.resolve()
    if espejo == REPO or REPO in espejo.parents:
        raise SystemExit("el espejo no puede estar dentro del repo (CLAUDE.md §4 k y l)")
    if espejo.exists():
        shutil.rmtree(espejo)
    for rel in COPIAS:
        dst = espejo / rel
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(REPO / rel, dst)  # copia de bytes, nunca enlace


def generar(espejo: Path, salida: Path) -> None:
    subprocess.run([sys.executable, "-B", str(espejo / "data/experiment/pyd_r2/code/generar_r2.py"),
                    "--salida", str(salida)], check=True, cwd=espejo,
                   env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--espejo", required=True)
    ap.add_argument("--salida", required=True)
    a = ap.parse_args()
    espejo, salida = Path(a.espejo), Path(a.salida)
    armar_espejo(espejo)
    generar(espejo, salida / "generados_hoy")
    p = espejo / "data/experiment/pyd_r2/code/modelos_r2.py"
    t = p.read_text(encoding="utf-8")
    for nombre, viejo, nuevo in CAMBIOS:
        n = t.count(viejo)
        if n != 1:
            raise SystemExit(f"cambio «{nombre}»: el ancla aparece {n} veces (esperado 1)")
        t = t.replace(viejo, nuevo)
    p.write_text(t, encoding="utf-8")
    generar(espejo, salida / "generados_d15_17")
    print(f"{len(CAMBIOS)} cambios aplicados en la copia; espejo: {espejo}")


if __name__ == "__main__":
    main()
