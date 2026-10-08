"""
comparador_paso2_P.py — U-MED-UMBRALES, etapa P, tramo P-a, punto 8: el paso 2 (§5.3 de la enmienda). Lee el formulario
del paso 1 llenado por la autora y el grafo (copia), y devuelve solo las diferencias, ahora con el valor del grafo a la
vista, para que la autora las clasifique con el §2.3 (correcto, contradicho, omitido, espurio, parcial, no aplica, no
decidible) y las comparaciones omitidas con las dos clases del §2.4 (de implementación, de la definición).

Igualdades (§5.3):
  - valor: como Decimal («sin valor» ↔ sin valor en el grafo);
  - unidad, moneda, tipo de días y comparación: exactas, después de normalizar la escritura (minúsculas, sin tildes,
    guion bajo por espacio); «sin unidad», «no aplica» y «sin tipo» ↔ campo vacío en el grafo; una unidad fuera de la
    lista cerrada (horas, semanas) pide además la marca fuera_de_lista en el grafo;
  - base: igualdad después de plegar (minúsculas, sin tildes, sin artículo inicial ni conjunción final, espacios y
    puntuación de los extremos normalizados); «sin base» ↔ sin base;
  - destino: igualdad de id. «<to>::<punto>» contra base_destino; «definicion: <término>» contra el término de la
    Definicion que es el base_destino; «no remite» o «no aplica» ↔ sin destino.
La pertinencia, el «no decidible» y los campos sin llenar se listan siempre. Los elementos V-vacío no se comparan: se
registra la clase del §2.5.

  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/med_umbrales/p/code/comparador_paso2_P.py \
      --formulario <formulario_paso1_loteK.md llenado> --lote K --salida DIR
Corre desde la raíz de la copia del repo y escribe solo en --salida.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import formulario_P as F  # noqa: E402

CLASES_23 = "correcto | contradicho | omitido | espurio | parcial | no aplica | no decidible"
CLASES_24 = "de implementación | de la definición"
NULOS = {"sin valor", "sin unidad", "no aplica", "sin tipo", "sin base", "no remite", "ninguna", "ninguno"}
_ART = re.compile(r"^(?:el|la|los|las|lo|un|una|unos|unas)\s+")
_CONJ = re.compile(r"(?:\s+(?:y/o|y|o|e|u))+$")


def plegar(s: str) -> str:
    import unicodedata
    d = unicodedata.normalize("NFKD", s)
    return "".join(c for c in d if not unicodedata.combining(c)).lower()


def norm_palabra(v):
    if v is None:
        return None
    s = " ".join(plegar(str(v)).replace("_", " ").split())
    return None if s in NULOS else s.replace(" ", "_")


SINONIMOS_UNIDAD = {"anos": "anios", "ano": "anios", "anio": "anios", "dia": "dias", "mes": "meses", "hora": "horas",
                    "semana": "semanas", "%": "porcentaje", "por_ciento": "porcentaje", "vez": "veces"}


def norm_unidad(v):
    s = norm_palabra(v)
    return SINONIMOS_UNIDAD.get(s, s) if s else s


def norm_valor(v):
    if v is None:
        return None
    s = str(v).strip()
    if plegar(s) in NULOS:
        return None
    try:
        return Decimal(s)
    except InvalidOperation:
        return ("no_numerico", s)


def norm_base(v):
    if v is None:
        return None
    s = " ".join(plegar(str(v)).split())
    if s in NULOS:
        return None
    s = s.strip(" «»\"'.,;:()")
    s = _ART.sub("", s)
    s = _CONJ.sub("", s)
    return s.strip(" .,;:") or None


def norm_destino_autora(v):
    if v is None:
        return None
    s = " ".join(str(v).split())
    if plegar(s) in NULOS:
        return None
    m = re.match(r"(?i)^definici[oó]n\s*:\s*(.+)$", s)
    if m:
        return ("definicion", norm_base(m.group(1)))
    return ("punto", s.lower())


def norm_destino_grafo(v, kg_nodos: dict):
    if v is None:
        return None
    if "::" in v:
        return ("punto", v.lower())
    n = kg_nodos.get(v)
    if n is not None and n.get("type") == "Definicion":
        return ("definicion", norm_base((n.get("properties") or {}).get("termino") or ""))
    return ("nodo", v)


def comparar(el: dict, campos: dict, kg_nodos: dict) -> dict:
    """Diferencias de un elemento con contenido. `campos`: lo que leyó formulario_P.leer de su bloque."""
    dif, sin_llenar = [], []

    def par(campo, grafo, autora, igual):
        if not igual:
            dif.append({"campo": campo, "grafo": grafo, "autora": autora})

    for c in ("pertinencia", "valor", "unidad", "moneda", "tipo_de_dias", "comparacion", "base", "destino_de_la_base"):
        if campos.get(c) is None:
            sin_llenar.append(c)
    a = campos
    if a.get("valor") is not None:
        g, x = norm_valor(el.get("valor")), norm_valor(a["valor"])
        par("valor", el.get("valor"), a["valor"], g == x)
    if a.get("unidad") is not None:
        g, x = norm_unidad(el.get("unidad")), norm_unidad(a["unidad"])
        par("unidad", el.get("unidad"), a["unidad"], g == x)
        if x in F.UNIDADES_FUERA and g == x and "unidad" not in (el.get("fuera_de_lista") or []):
            dif.append({"campo": "unidad (marca fuera_de_lista)", "grafo": el.get("fuera_de_lista") or [],
                        "autora": a["unidad"]})
    if a.get("moneda") is not None:
        g, x = el.get("moneda"), norm_palabra(a["moneda"])
        par("moneda", g, a["moneda"], (g.lower() if g else None) == x)
    if a.get("tipo_de_dias") is not None:
        g, x = norm_palabra(el.get("dias_tipo")), norm_palabra(a["tipo_de_dias"])
        par("tipo_de_dias", el.get("dias_tipo"), a["tipo_de_dias"], g == x)
    if a.get("comparacion") is not None:
        g, x = norm_palabra(el.get("comparacion")), norm_palabra(a["comparacion"])
        if g != x:
            d = {"campo": "comparacion", "grafo": el.get("comparacion"), "autora": a["comparacion"],
                 "palabras_de_la_autora": a.get("palabras_de_la_comparacion")}
            if g == "no_determinada" and x not in (None, "no_determinada"):
                d["candidata"] = "omitida: clasificar " + CLASES_24
            dif.append(d)
    if a.get("base") is not None:
        g, x = norm_base(el.get("base")), norm_base(a["base"])
        par("base", el.get("base"), a["base"], g == x)
    if a.get("destino_de_la_base") is not None:
        g = norm_destino_grafo(el.get("base_destino"), kg_nodos)
        x = norm_destino_autora(a["destino_de_la_base"])
        par("destino_de_la_base", el.get("base_destino"), a["destino_de_la_base"], g == x)
    marcas = {}
    if a.get("pertinencia") and norm_palabra(a["pertinencia"]) != "pertinente":
        marcas["pertinencia"] = a["pertinencia"]
    if a.get("no_decidible") and norm_palabra(a["no_decidible"]) != "no":
        marcas["no_decidible"] = a["no_decidible"]
    return {"diferencias": dif, "sin_llenar": sin_llenar, "marcas": marcas}


def informe(lote: int, filas: list[dict]) -> str:
    L = [f"# Paso 2, lote {lote}: diferencias entre la lectura y el grafo (U-MED-UMBRALES, etapa P)", "",
         "Solo las diferencias, con el valor del grafo a la vista. En cada una: `clasificacion` con el §2.3 "
         f"({CLASES_23}); en una comparación omitida, también {CLASES_24}; si la diferencia es un error del paso 1, "
         "`corrijo_mi_paso_1: <motivo>`, que se registra y se cuenta.", ""]
    for f in filas:
        L.append(f"## {f['etiqueta']} · `{f['id']}`")
        if f.get("vacio"):
            L += [f"- elemento vacío (§2.5): clase de la autora «{f.get('clase_vacio')}»", ""]
            continue
        if f["marcas"]:
            L.append(f"- marcas del paso 1: {f['marcas']}")
        if f["sin_llenar"]:
            L.append(f"- campos sin llenar en el paso 1: {f['sin_llenar']}")
        if not f["diferencias"]:
            L += ["- sin diferencias", ""]
            continue
        for d in f["diferencias"]:
            extra = f"; {d['candidata']}" if d.get("candidata") else ""
            L.append(f"- **{d['campo']}**: grafo «{d['grafo']}», paso 1 «{d['autora']}»{extra}")
            L.append(f"  - clasificacion [{CLASES_23}]: {F.VACIO}")
            if d.get("candidata"):
                L.append(f"  - clase_de_la_omision [{CLASES_24}]: {F.VACIO}")
            L.append(f"  - corrijo_mi_paso_1 [no | sí: <motivo>]: {F.VACIO}")
        L.append("")
    return "\n".join(L) + "\n"


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import comun_P as C  # noqa: PLC0415
    ap = argparse.ArgumentParser()
    ap.add_argument("--formulario", type=Path, required=True)
    ap.add_argument("--lote", type=int, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    kg, s_kg = C.cargar_kg()
    idx = C.indice_elementos(kg)
    nodos = {n["id"]: n for n in kg["nodes"]}
    leido = F.leer(a.formulario.read_text(encoding="utf-8"))
    filas = []
    for eid, b in leido.items():
        n, i, el = idx[eid]
        if C.estrato(el) == "V-vacío":
            filas.append({"etiqueta": b["etiqueta"], "id": eid, "vacio": True,
                          "clase_vacio": b["campos"].get("clase_vacio"), "campos": b["campos"]})
            continue
        filas.append({"etiqueta": b["etiqueta"], "id": eid, **comparar(el, b["campos"], nodos)})
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / f"diferencias_paso2_lote{a.lote}.json").write_text(
        json.dumps({"lote": a.lote, "grafo_sha256": s_kg, "formulario_sha256": C.sha(a.formulario.read_bytes()),
                    "filas": filas}, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    (a.salida / f"diferencias_paso2_lote{a.lote}.md").write_text(informe(a.lote, filas), encoding="utf-8")
    print(json.dumps({"fichas": len(filas), "con_diferencias": sum(1 for f in filas if f.get("diferencias"))},
                     ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
