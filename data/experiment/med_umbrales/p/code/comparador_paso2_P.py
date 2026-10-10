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

Instrumento v1, desde el lote 2 (regla v1, §5; nota del 10/10/2026 al pie de la enmienda 1). El lote 1 corre igual que antes. El
paso 2 tiene dos partes, y cada una exige el sha256 de lo que lee (el mapa de ids opacos y los formularios sellados):
  - pertinencia: con el paso 1 sellado, arma el formulario de la pertinencia (C7). Por ficha muestra solo la etiqueta del nodo,
    los tramos de umbral que E1 devolvió para el nodo (marcado el del elemento, si se sabe), lo que la ficha resaltó y la cuantía
    guardada de cada elemento del nodo, en el orden del grafo; ningún otro valor del grafo. Los elementos vacíos (§2.5) no tienen
    esta parte: su pregunta única está en el paso 1.
  - diferencias: con la pertinencia llena y sellada, compara como en el lote 1 y devuelve las diferencias, con el valor del grafo
    a la vista. Cada fila lleva su nota, y cada ficha una nota más (C26).
La cabecera de cada bloque es la etiqueta y el id opaco (C25); el id del elemento sale del mapa y va solo en el JSON.
  ... comparador_paso2_P.py --lote K --etapa pertinencia --mapa <NO_ABRIR_mapa_ids_loteK.json> --sha-mapa <sha256> \
      --formulario <formulario del paso 1 sellado> --sha-formulario <sha256> --salida DIR
  ... comparador_paso2_P.py --lote K --etapa diferencias --mapa ... --sha-mapa ... --formulario ... --sha-formulario ... \
      --pertinencia <formulario de la pertinencia sellado> --sha-pertinencia <sha256> --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
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


# ------------------------------------------------------------------------------------------- instrumento v1 (lote 2)
def clave(campo: str) -> str:
    """Nombre de campo de una fila del formulario de diferencias: «unidad (marca fuera_de_lista)» → unidad_marca_fuera_de_lista."""
    return re.sub(r"[^a-z0-9]+", "_", plegar(campo)).strip("_")


def leer_sellado(p: Path, sha: str, que: str) -> bytes:
    b = p.read_bytes()
    if hashlib.sha256(b).hexdigest() != sha:
        raise SystemExit(f"FRENO: {que} no da el sha256 de su sello")
    return b


def bloque_pertinencia(fila: dict) -> str:
    L = [f"## {fila['etiqueta']} · `{fila['opaco']}`", "", f"- Etiqueta del nodo: «{fila['etiqueta_nodo']}»"]
    if fila["tramos_e1"]:
        L.append("- Tramos de umbral que E1 devolvió para el nodo:")
        L += [f"  {k}. «{t}»" + (" ← el del elemento" if t == fila["tramo_e1_del_elemento"] else "")
              for k, t in enumerate(fila["tramos_e1"], 1)]
    else:
        L.append("- E1 no devolvió tramos de umbral para el nodo.")
    L.append(f"- Lo que la ficha resaltó: «{fila['resaltado']}»" if fila["resaltado"] is not None
             else f"- La ficha no resaltó nada; lo que el elemento guarda como cuantía: «{fila['guardado']}»")
    L.append("- Elementos del nodo, en el orden del grafo (la cuantía guardada de cada uno):")
    L += [f"  {k}. «{c}»" + (" ← este elemento" if k - 1 == fila["indice"] else "") for k, c in enumerate(fila["cuantias_nodo"], 1)]
    L += [f"- {c} [{v}]: {F.VACIO}" for c, v in F.CAMPOS_PERTINENCIA]
    return "\n".join(L) + "\n"


def informe_pertinencia(lote: int, filas: list[dict]) -> str:
    cab = [f"# Paso 2, lote {lote}, primera parte: la pertinencia (U-MED-UMBRALES, etapa P, regla v1)", "",
           "Se juzga primero (C7), con lo que muestra cada bloque: la etiqueta del nodo, los tramos de E1, lo que la ficha resaltó y "
           "la cuantía guardada de cada elemento del nodo. Los valores del grafo de los demás campos llegan después, en la segunda "
           "parte, con la pertinencia ya sellada. Se llena reemplazando «______»; la nota es libre (C26). Los elementos vacíos (§2.5) "
           "no tienen esta parte.", ""]
    return "\n".join(cab) + "\n" + "\n".join(bloque_pertinencia(f) for f in filas)


def informe_v1(lote: int, filas: list[dict]) -> str:
    L = [f"# Paso 2, lote {lote}, segunda parte: diferencias entre la lectura y el grafo (U-MED-UMBRALES, etapa P, regla v1)", "",
         "Solo las diferencias, con el valor del grafo a la vista. En cada una: la clasificación con el §2.3 "
         f"({CLASES_23}); en una comparación omitida, también {CLASES_24}; si la diferencia es un error del paso 1, "
         "`corrijo_mi_paso_uno_<campo>: sí: <motivo>`, que se registra y se cuenta. Cada fila lleva su nota, y cada ficha una "
         "nota más (C26).", ""]
    for f in filas:
        L.append(f"## {f['etiqueta']} · `{f['opaco']}`")
        if f.get("vacio"):
            L += [f"- elemento vacío (§2.5): clase de la lectora «{f.get('clase_vacio')}»",
                  f"- nota_de_la_ficha [libre]: {F.VACIO}", ""]
            continue
        if f["marcas"]:
            L.append(f"- marcas del paso 1 y de la pertinencia: {f['marcas']}")
        if f["sin_llenar"]:
            L.append(f"- campos sin llenar en el paso 1: {f['sin_llenar']}")
        if not f["diferencias"]:
            L.append("- sin diferencias")
        for d in f["diferencias"]:
            k = clave(d["campo"])
            extra = f"; {d['candidata']}" if d.get("candidata") else ""
            L.append(f"- **{d['campo']}**: grafo «{d['grafo']}», paso 1 «{d['autora']}»{extra}")
            L.append(f"  - clasificacion_{k} [{CLASES_23}]: {F.VACIO}")
            if d.get("candidata"):
                L.append(f"  - clase_de_la_omision_{k} [{CLASES_24}]: {F.VACIO}")
            L.append(f"  - corrijo_mi_paso_uno_{k} [no | sí: <motivo>]: {F.VACIO}")
            L.append(f"  - nota_{k} [libre]: {F.VACIO}")
        L += [f"- nota_de_la_ficha [libre]: {F.VACIO}", ""]
    return "\n".join(L) + "\n"


def main_v1(a, C, kg: dict, s_kg: str) -> int:
    import armador_fichas_P as A  # noqa: PLC0415
    for k in ("etapa", "mapa", "sha_mapa", "sha_formulario"):
        if getattr(a, k) is None:
            raise SystemExit(f"FRENO: desde el lote 2 hace falta --{k.replace('_', '-')}")
    mapa = json.loads(leer_sellado(a.mapa, a.sha_mapa, "el mapa de ids opacos"))
    if mapa["lote"] != a.lote:
        raise SystemExit("FRENO: el mapa es de otro lote")
    por_opaco = {m["opaco"]: m for m in mapa["fichas"]}
    paso1 = F.leer(leer_sellado(a.formulario, a.sha_formulario, "el formulario del paso 1").decode("utf-8"))
    if list(paso1) != [m["opaco"] for m in mapa["fichas"]]:
        raise SystemExit("FRENO: el formulario del paso 1 no tiene las fichas del mapa, en su orden")
    idx = C.indice_elementos(kg)
    salida = a.salida
    if a.etapa == "pertinencia":
        filas = []
        for op, b in paso1.items():
            n, i, el = idx[por_opaco[op]["id"]]
            if C.estrato(el) == "V-vacío":
                continue
            u, r = C.ubicar(n, i, el), A.ubicar_v1(n, i, el)
            txt = dict((cid, t) for cid, t, _ in C.textos_nodo(n)).get(r["chunk_id"], "")
            filas.append({"etiqueta": b["etiqueta"], "opaco": op, "id": por_opaco[op]["id"], "indice": i,
                          "etiqueta_nodo": n.get("label"), "tramos_e1": [t for _, t in u["tramos_e1"]],
                          "tramo_e1_del_elemento": u["tramo_e1_del_elemento"],
                          "resaltado": " […] ".join(txt[x:y] for x, y in r["spans"]) if r["spans"] else None,
                          "guardado": r["guardado"],
                          "cuantias_nodo": [C.cuantia_del_elemento(x) for x in (n.get("properties") or {}).get("umbrales") or []]})
        salida.mkdir(parents=True, exist_ok=True)
        dest = salida / f"pertinencia_paso2_lote{a.lote}.md"
        if dest.exists():
            raise SystemExit(f"FRENO: {dest} ya existe")
        dest.write_text(informe_pertinencia(a.lote, filas), encoding="utf-8")
        print(f"formulario de la pertinencia en {dest}")
        return 0
    if a.pertinencia is None or a.sha_pertinencia is None:
        raise SystemExit("FRENO: las diferencias piden la pertinencia sellada (--pertinencia y --sha-pertinencia)")
    pert = F.leer(leer_sellado(a.pertinencia, a.sha_pertinencia, "el formulario de la pertinencia").decode("utf-8"))
    nodos = {n["id"]: n for n in kg["nodes"]}
    filas = []
    for op, b in paso1.items():
        eid = por_opaco[op]["id"]
        n, i, el = idx[eid]
        if C.estrato(el) == "V-vacío":
            filas.append({"etiqueta": b["etiqueta"], "opaco": op, "id": eid, "vacio": True,
                          "clase_vacio": b["campos"].get("clase_vacio"), "campos": b["campos"]})
            continue
        p = (pert.get(op) or {}).get("campos") or {}
        if not p.get("pertinencia"):
            raise SystemExit(f"FRENO: {b['etiqueta']}: la pertinencia no está llena")
        campos = {**b["campos"], "pertinencia": p["pertinencia"]}
        filas.append({"etiqueta": b["etiqueta"], "opaco": op, "id": eid, "nota_pertinencia": p.get("nota"),
                      **comparar(el, campos, nodos)})
    salida.mkdir(parents=True, exist_ok=True)
    dj, dm = salida / f"diferencias_paso2_lote{a.lote}.json", salida / f"diferencias_paso2_lote{a.lote}.md"
    if dj.exists() or dm.exists():
        raise SystemExit("FRENO: la salida de las diferencias ya existe")
    dj.write_text(json.dumps({"lote": a.lote, "grafo_sha256": s_kg, "mapa_sha256": a.sha_mapa,
                              "formulario_sha256": a.sha_formulario, "pertinencia_sha256": a.sha_pertinencia,
                              "filas": filas}, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    dm.write_text(informe_v1(a.lote, filas), encoding="utf-8")
    print(f"diferencias en {dm} y {dj}")
    return 0


def main() -> int:
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import comun_P as C  # noqa: PLC0415
    ap = argparse.ArgumentParser()
    ap.add_argument("--formulario", type=Path, required=True)
    ap.add_argument("--lote", type=int, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--etapa", choices=("pertinencia", "diferencias"))
    ap.add_argument("--mapa", type=Path)
    for k in ("--sha-mapa", "--sha-formulario", "--sha-pertinencia"):
        ap.add_argument(k)
    ap.add_argument("--pertinencia", type=Path)
    a = ap.parse_args()
    kg, s_kg = C.cargar_kg()
    if a.lote >= 2:
        return main_v1(a, C, kg, s_kg)
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
