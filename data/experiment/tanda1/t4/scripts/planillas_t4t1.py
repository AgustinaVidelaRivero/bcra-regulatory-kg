"""B6.1, tanda 1, T4, primer tramo, puntos 6 y 7: la lectura asistida de las ocho muestras, en un JSON con la regla de cada muestra, y las
planillas de la autora, una por muestra, con el convertidor de la exportación de Numbers. No lee ninguna unidad ni juzga nada: toma las
propuestas que escribí al leer las fichas (<propuestas>/<muestra>.json, una por elemento) y las controla contra el sorteo y el material.

  - Las ocho muestras, en el orden de lectura: cola, aceptadas_items, aceptadas_no_items, vigilancia_2, vigilancia_7 (sorteos y material de
    T3, tanda1/t3/muestras/), vigilancia_1, vigilancia_3 y observacion_12 (sorteos y material de este tramo, tanda1/t4/muestras/). La
    observación (12) de T3 no se lee.
  - Controles: los ids de cada archivo de propuestas son los de las fichas de su muestra, en su orden; cada propuesta es una de las
    respuestas válidas de su muestra; cada justificación tiene texto entre comillas angulares («…»), que es la cita.
  - Escribe en <salida>:
      lectura_asistida/lectura_asistida_t4_tramo1.json  el modelo, la regla y las respuestas válidas de cada muestra, y por elemento la
                                                       propuesta, la justificación y, aparte, las omisiones y las observaciones;
      lectura_asistida/omisiones_y_observaciones_t4_tramo1.md  lo que va aparte, por muestra, para leer;
      lectura_autora/<muestra>.csv                       UTF-8, «;» y «\\n»: id, celda, ficha (la ruta del .md de su material, con el
                                                       número de la ficha tras «#»), propuesta, justificacion, veredicto_autora y
                                                       nota_autora, las dos últimas vacías;
      lectura_autora/convertir_lectura_T4.py             el convertidor, con el sha256 de cada planilla adentro (sale de la plantilla
                                                       de abajo; solo se reemplaza @@SHA_PLANILLAS@@).
Uso: python3 -I -B planillas_t4t1.py <raíz> <muestras de T4> <propuestas> <salida>
"""
import csv
import hashlib
import io
import json
import re
import sys
from collections import Counter, OrderedDict
from datetime import datetime
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, M4, PROP, OUT = (Path(x).resolve() for x in sys.argv[1:5])
T3R = "data/experiment/tanda1/t3/muestras"
T4R = "data/experiment/tanda1/t4/muestras"
M3 = RAIZ / T3R
MODELO = {"modelo": "Claude Opus 5.5", "id": "claude-opus-5-5",
          "como": "lectura propia de la ejecutora en su sesión de Claude Code, sobre las fichas del material; sin API y USD 0. Es una "
                  "propuesta: adjudica la autora (D2, lectura asistida con revisión de la autora, como en la tanda 0)"}
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado"]
R_UNIDAD = ("unidad con error si al menos un nodo o una relación no lo sostiene el texto de la unidad (propio o heredado); sin error; o "
            "dudosa. Las omisiones van aparte (enmienda de la cola humana, :26-28)")
MUESTRAS = OrderedDict([
    ("cola", {"de": "T3", "pregunta": R_UNIDAD, "validas": ["con error", "sin error", "dudosa"]}),
    ("aceptadas_items", {"de": "T3", "pregunta": R_UNIDAD, "validas": ["con error", "sin error", "dudosa"]}),
    ("aceptadas_no_items", {"de": "T3", "pregunta": R_UNIDAD, "validas": ["con error", "sin error", "dudosa"]}),
    ("vigilancia_2", {"de": "T3", "pregunta": "vaciamiento (el texto porta contenido normativo y la unidad no tiene relaciones), no "
                                              "vaciamiento o no decidible",
                      "validas": ["vaciamiento", "no vaciamiento", "no decidible"]}),
    ("vigilancia_7", {"de": "T3", "pregunta": "¿la arista ejecuta desde el rol de alcance tiene apoyo textual? con apoyo, sin apoyo o no decidible",
                      "validas": ["con apoyo", "sin apoyo", "no decidible"]}),
    ("vigilancia_1", {"de": "T4", "pregunta": "¿la Condicion expresa un deber explícito (debe, deberá, está obligado a) que el texto de su "
                                              "unidad formula como obligación, y no como condición? sí (migración), no o no decidible; "
                                              "«no decidible» queda fuera de la tasa y se declara con su cuenta (decisión 1.4)",
                      "validas": ["sí", "no", "no decidible"]}),
    ("vigilancia_3", {"de": "T4", "pregunta": "¿los nodos del grupo repiten el mismo contenido normativo (duplicación), o son contenidos "
                                              "distintos sobre el mismo pasaje? El grupo por tramo igual no ve duplicaciones con tramos "
                                              "distintos (decisión 1.4)",
                      "validas": ["duplicación", "distintos"]}),
    ("observacion_12", {"de": "T4", "pregunta": "correcta, incorrecta o no decidible; en las incorrectas, la regla implicada con el "
                                                "vocabulario capa_pipeline (enmienda de la observación 12, §2.1)",
                        "validas": ["correcta", "no decidible"] + [f"incorrecta ({c})" for c in CAPAS]}),
])
CRITERIOS = {
    "unidad": ["tipos cercanos con la descripción fiel, condicion_de o requiere laxos y `tipo` que no corresponde: sin error, como "
               "observación (lectura laxa, R2, como en la lectura de las aceptadas de la tanda 0)",
               "con error: una facultad o un fin leído como deber, un supuesto o una regla invertidos, un sujeto que no es el del texto, "
               "una relación que el texto no sostiene o contenido que no está en el texto",
               "dudosa: el contenido viene de otro punto del documento y no está en el texto de la unidad, o el texto admite las dos lecturas",
               "los tipos documentales mal asignados (Comunicacion para una ley o un TO) son observación, no error, como en la tanda 0",
               "las remite_a no entran en el veredicto: se cuentan aparte por cita y destino, como en la tanda 0; si una no sostiene su "
               "destino, va como observación"],
    "vigilancia_2": ["vaciamiento: el ítem fija un dato, una medida, un concepto o un sujeto del régimen, o el texto fija una regla o una "
                     "tabla del modelo de información, y la unidad no tiene relaciones",
                     "no vaciamiento: el texto propio solo abre una lista (sus ítems llevan el contenido como heredado), es un título o es "
                     "un formulario"],
    "vigilancia_1": ["sí: el texto formula el deber (debe, deberá, o un futuro prescriptivo como «se aplicará») y la Condicion lo lleva",
                     "el «debe» que pone la descripción del extractor no cuenta: decide el texto"],
    "vigilancia_3": ["duplicación: el mismo contenido normativo (deber, facultad, prohibición, regla, definición o supuesto) está en dos "
                     "nodos del grupo",
                     "distintos: cada nodo dice algo que el otro no; incluye el par deber y acto regulado (Obligacion —regula→ "
                     "Operacion, prompt_e1.py:67 y :184-189) cuando la descripción del acto no repite el deber"],
    "observacion_12": ["establecida_en: correcta si el nodo de origen está en el texto de su unidad y es de ese TO",
                       "las demás: la relación contra el texto; un defecto del nodo de destino que no cambia la relación va como "
                       "observación"],
}
COLS = ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"]


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def id_txt(x) -> str:
    return x if isinstance(x, str) else " | ".join(x)


res = OrderedDict([("hora", datetime.now().astimezone().isoformat(timespec="seconds")), ("lectura", MODELO),
                   ("criterios_de_la_propuesta", CRITERIOS), ("muestras", OrderedDict())])
(OUT / "lectura_autora").mkdir(parents=True, exist_ok=True)
(OUT / "lectura_asistida").mkdir(parents=True, exist_ok=True)
sha_planillas, aparte = OrderedDict(), []
for m, cfg in MUESTRAS.items():
    base = (M3 if cfg["de"] == "T3" else M4) / "material" / m
    ruta_md = f"{T3R if cfg['de'] == 'T3' else T4R}/material/{m}/fichas_{m}.md"
    fichas = [json.loads(x) for x in (base / f"fichas_{m}.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    sor = (M3 / f"{m}.json") if cfg["de"] == "T3" else (M4 / f"{m}.json")
    props = json.loads((PROP / f"{m}.json").read_text(encoding="utf-8"))
    assert len(props) == len(fichas), (m, len(props), len(fichas))
    filas, elems = [], []
    for f, p in zip(fichas, props):
        assert p["n"] == f["n"] and id_txt(p["id"]) == id_txt(f["id"]), (m, p["n"], p["id"], f["id"])
        assert p["propuesta"] in cfg["validas"], (m, p["n"], p["propuesta"])
        j = p["justificacion"].strip()
        assert j and re.search(r"«[^»]+»", j), (m, p["n"], "justificación sin cita")
        elems.append(OrderedDict([("n", f["n"]), ("id", f["id"]), ("celda", f["celda"]), ("ficha", f"{ruta_md}#{f['n']}"),
                                  ("propuesta", p["propuesta"]), ("regla", cfg["pregunta"]), ("justificacion", j),
                                  ("omisiones", p.get("omisiones", "")), ("observaciones", p.get("observaciones", ""))]))
        filas.append([id_txt(f["id"]), f["celda"], f"{ruta_md}#{f['n']}", p["propuesta"], j, "", ""])
        if p.get("omisiones") or p.get("observaciones"):
            aparte.append((m, f["n"], id_txt(f["id"]), p.get("omisiones", ""), p.get("observaciones", "")))
    buf = io.StringIO()
    w = csv.writer(buf, delimiter=";", lineterminator="\n")
    w.writerow(COLS)
    w.writerows(filas)
    pl = OUT / "lectura_autora" / f"{m}.csv"
    pl.write_text(buf.getvalue(), encoding="utf-8")
    sha_planillas[m] = sha(pl.read_bytes())
    res["muestras"][m] = OrderedDict([
        ("material", ruta_md), ("material_jsonl_sha256", sha((base / f"fichas_{m}.jsonl").read_bytes())),
        ("sorteo", f"{T3R if cfg['de'] == 'T3' else T4R}/{m}.json"), ("sorteo_sha256", sha(sor.read_bytes())),
        ("pregunta", cfg["pregunta"]), ("respuestas_validas", cfg["validas"]), ("elementos", len(elems)),
        ("propuestas", dict(Counter(e["propuesta"] for e in elems))),
        ("con_omisiones", sum(1 for e in elems if e["omisiones"])), ("con_observaciones", sum(1 for e in elems if e["observaciones"])),
        ("planilla", f"data/experiment/tanda1/t4/lectura_autora/{m}.csv"), ("planilla_sha256", sha_planillas[m]),
        ("detalle", elems)])
(OUT / "lectura_asistida" / "lectura_asistida_t4_tramo1.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n",
                                                                         encoding="utf-8")
md = ["# Lectura asistida de T4, primer tramo: lo que va aparte del veredicto", "",
      "Las omisiones y las observaciones de mi lectura. No cuentan para el veredicto: van aparte, como en la tanda 0. La propuesta de "
      "cada elemento está en su planilla (`lectura_autora/<muestra>.csv`).", ""]
for m in MUESTRAS:
    xs = [a for a in aparte if a[0] == m]
    if not xs:
        continue
    md += [f"## {m}", ""]
    for _, n, i, om, ob in xs:
        md.append(f"- **{n}.** `{i}`" + (f" — omisiones: {om}" if om else "") + (f" — observaciones: {ob}" if ob else ""))
    md.append("")
(OUT / "lectura_asistida" / "omisiones_y_observaciones_t4_tramo1.md").write_text("\n".join(md), encoding="utf-8")
plantilla = (Path(__file__).resolve().parent / "convertir_lectura_T4_plantilla.py").read_text(encoding="utf-8")
assert plantilla.count("@@SHA_PLANILLAS@@") == 1
conv = plantilla.replace("@@SHA_PLANILLAS@@", json.dumps(sha_planillas, ensure_ascii=False, indent=4))
(OUT / "lectura_autora" / "convertir_lectura_T4.py").write_text(conv, encoding="utf-8")
for m, x in res["muestras"].items():
    print(f"{m}: {x['elementos']} elementos {x['propuestas']}; omisiones {x['con_omisiones']}, observaciones {x['con_observaciones']}; "
          f"planilla {x['planilla_sha256'][:16]}…")
print("hora", res["hora"], "| lectura_asistida_t4_tramo1.json",
      sha((OUT / 'lectura_asistida' / 'lectura_asistida_t4_tramo1.json').read_bytes()),
      "| convertir_lectura_T4.py", sha((OUT / 'lectura_autora' / 'convertir_lectura_T4.py').read_bytes()))
