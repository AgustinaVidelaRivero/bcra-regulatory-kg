"""B6.1, tanda final, T4, primer tramo (puntos 3 y 4 del «seguí»): arma, desde los borradores de la lectura asistida, lo que va al repo:
  - t4/lectura_asistida/borradores/<muestra>.jsonl: copia de los borradores (una propuesta por ficha: n, propuesta, regla,
    justificacion y, si hay, omisiones y observacion), para que todo lo demás se rehaga desde el repo;
  - t4/lectura_asistida/lectura_asistida_t4_tramo1.json: el modelo y su versión, la hora de la lectura (st_birthtime y st_mtime de los
    borradores), los criterios de la propuesta, las reglas usadas, las propuestas por muestra y su cuenta por respuesta;
  - t4/lectura_asistida/omisiones_y_observaciones_t4_tramo1.md: lo que va aparte del veredicto, por muestra y por ficha;
  - t4/lectura_autora/<muestra>.csv: las ocho planillas de la autora (UTF-8, «;» y «\\n»), con id, celda, ficha, propuesta,
    justificacion y las dos columnas de la autora vacías.
Controles antes de escribir (frena si alguno no cierra):
  - los ids y las celdas, en su orden, son los de la planilla en blanco de T3 (t3/muestras/material/<m>/planilla_<m>.csv);
  - los pares (celda, id) son los de la muestra (t3/muestras/<m>.json, celdas → elementos), y su cantidad, la de la muestra;
  - cada ficha del .jsonl del material tiene ese n, ese id y esa celda, y el .md tiene su encabezado «## n. `id` — celda»;
  - hay una propuesta por ficha (n de 1 a N), con una respuesta válida del LEEME y una justificación sin saltos de línea.
No lee el estado de E3 ni sus marcas (el material no los tiene: control_material_tf.json da 0 claves vedadas). Solo escribe en t4/.
Uso: python3 -I -B armar_lectura_t4.py <repo> <dir de los borradores>
"""
import csv
import hashlib
import io
import json
import re
import shutil
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

R, B = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve()
TF = R / "data/experiment/tanda_final"
M3, T4 = TF / "t3/muestras", TF / "t4"
MUESTRAS = ["cola", "aceptadas_items", "aceptadas_no_items", "vigilancia_2", "vigilancia_7", "vigilancia_1", "vigilancia_3", "observacion_12"]
CAPAS = ["E0", "E1-prompt", "E1-validador", "catálogo", "E2", "E3", "ensamblado"]
U = ["con error", "sin error", "dudosa"]
VALIDAS = {"cola": U, "aceptadas_items": U, "aceptadas_no_items": U, "vigilancia_2": ["vaciamiento", "no vaciamiento", "no decidible"],
           "vigilancia_7": ["con apoyo", "sin apoyo", "no decidible"], "vigilancia_1": ["sí", "no", "no decidible"],
           "vigilancia_3": ["duplicación", "distintos"], "observacion_12": ["correcta", "no decidible"] + [f"incorrecta ({c})" for c in CAPAS]}
COLS = ["id", "celda", "ficha", "propuesta", "justificacion", "veredicto_autora", "nota_autora"]
NOMBRE = {"cola": "cola", "aceptadas_items": "aceptadas ítems", "aceptadas_no_items": "aceptadas no ítems", "vigilancia_2": "vigilancia (2)",
          "vigilancia_7": "vigilancia (7)", "vigilancia_1": "vigilancia (1)", "vigilancia_3": "vigilancia (3)",
          "observacion_12": "observación (12)"}
CRITERIOS = {
    "general": [
        "Leo cada ficha en su .jsonl del material de T3 (punto 7.5), con ver_fichas_t4.py, que solo la compacta; es el mismo contenido "
        "que el .md que lee la autora, sin el estado ni las marcas de E3.",
        "Juzgo contra el texto que muestra la ficha (el que vio E3: encabezados, bloque de la lista, herencia que se muestra y texto "
        "propio). Lo que la ficha no muestra no lo doy por leído.",
        "Cada justificación cita el texto entre «»; los nodos van por su referencia (e1, N2) o su etiqueta.",
        "Las omisiones y las observaciones van aparte (omisiones_y_observaciones_t4_tramo1.md) y no cambian ninguna propuesta.",
        "Una regla por propuesta (campo `regla`); su definición está abajo, por muestra."],
    "cola y aceptadas (la unidad tiene error si al menos un nodo o una relación no lo sostiene el texto de la unidad, propio o heredado)": {
        "U-sostenida → sin error": [
            "cada nodo y cada relación tiene su pasaje en el texto;",
            "el nodo TextoOrdenado y las establecida_en son estructurales: se dan por sostenidos si el TO es el de la unidad, y su "
            "etiqueta no se juzga;",
            "la subclase (propiedad `tipo`) se da por sostenida si es la más cercana del vocabulario; un desajuste va como observación;",
            "un aplica_a al obligado del régimen que el texto no nombra (mención no verificada, en cuarentena) se da por sostenido; un "
            "aplica_a a uno de los sujetos que el texto nombra también, y los que faltan son omisión;",
            "una remite_a derivada al punto que el texto cita se da por sostenida;",
            "un tipo discutible que no contradice el texto (una regla de cálculo como Obligacion, un campo o una fila de una tabla como "
            "Definicion, un requisito de elegibilidad como Condicion) se da por sostenido."],
        "U-no-sostenida → con error": [
            "un nodo o una relación dice algo que el texto no dice: contenido agregado o cambiado; una relación entre nodos que el texto "
            "no une (por ejemplo, una prohibición de lo que el texto permite); un sujeto que no es el obligado (el objeto de una pasiva, "
            "el destinatario de un aviso, otro actor); una remite_a derivada a un punto que el texto no cita."],
        "U-tipo → con error": [
            "el tipo contradice la modalidad del texto: un deber de conducta tipado Condicion o Excepcion, un permiso tipado Obligacion, "
            "un deber tipado Potestad. El futuro normativo («se informará», «admitirán», «se tendrán en cuenta») se lee como deber."],
        "U-fuera-del-texto → dudosa": [
            "un nodo sin pasaje en el texto que muestra la ficha; vendría de la herencia que E1 ve y E3 no (registro, §31), y la ficha no "
            "deja decidir."],
        "U-dudosa → dudosa": ["el sostén de un nodo o de una relación depende de una lectura del texto que admite dos."],
        "nota": "La regla de las dudosas (registro, §35: cuentan como error para la tasa, la atención y el freno) es del segundo tramo; la "
                "propuesta no calcula nada."},
    "vigilancia (2) (vaciamiento: el texto porta contenido normativo y la unidad no tiene relaciones, en la extracción final)": {
        "V2-con-contenido → vaciamiento": [
            "el texto da un deber, una prohibición, un permiso, una condición, un plazo, una regla de cálculo o un criterio que la norma "
            "aplica, y la extracción no tiene ningún nodo de contenido (solo el TO)."],
        "V2-dato-a-informar → vaciamiento": ["el texto es un dato que el régimen pide informar (un ítem de la lista de datos), sin nodo."],
        "V2-sin-contenido → no vaciamiento": [
            "títulos y encabezados, remisiones puras, descripciones de la estructura, valores de una lista de códigos o de categorías, "
            "tablas de códigos de referencia, campos de un modelo para completar y datos que el BCRA pone a disposición de las entidades."],
        "V2-marco-de-lista → no vaciamiento": [
            "el bloque que abre una lista («deberá:», «en los siguientes casos:»): su deber, su sujeto y su momento son el marco de cada "
            "ítem, que los extrae con ese bloque (registro, §31: E1 extrae del bloque que abre la lista)."],
        "V2-cubierto → no vaciamiento": ["la extracción tiene el contenido del texto en un nodo."]},
    "vigilancia (7) (¿la arista ejecuta desde el rol de alcance tiene apoyo textual?)": {
        "V7-ejecutor-alcanzado → con apoyo": [
            "el texto da como ejecutor de la operación a un sujeto alcanzado por el TO del rol (las entidades del régimen, un "
            "participante del servicio que regula)."],
        "V7-otro-ejecutor → sin apoyo": [
            "el texto da otro ejecutor (otro actor, el BCRA, un tercero), no describe una operación del sujeto, o el rol es el de otro TO."]},
    "vigilancia (1) (¿la Condicion lleva un deber explícito que el texto formula como obligación?)": {
        "V1-deber → sí": [
            "la Condicion recoge un deber que el texto formula como tal («debe», «deberá», el futuro normativo, el mandato de una lista "
            "de requisitos), no como supuesto."],
        "V1-condicion → no": [
            "el texto la formula como supuesto («cuando», «en caso de», «ante», «en la medida que», «de verificarse»), como motivo de "
            "inclusión o como requisito de elegibilidad, o la Condicion no lleva ningún deber (una duración, un plazo, una descripción)."]},
    "vigilancia (3) (un grupo es duplicación solo si un nodo repite el contenido normativo de otro; el par del deber y el acto regulado "
    "no es, por sí mismo, duplicación: registro, §31)": {
        "V3-repite → duplicación": [
            "un nodo repite el contenido normativo de otro: una definición que repite un deber o una regla, o una operación cuya "
            "descripción es el deber mismo."],
        "V3-par-deber-acto → distintos": ["el par del deber y el acto regulado (§31)."],
        "V3-par-modalidad-acto → distintos": [
            "el par de una facultad o de un límite y el acto al que se aplica, por analogía con el del deber y el acto (§31)."],
        "V3-contenido-distinto → distintos": ["los nodos dan contenidos distintos sobre el mismo pasaje."]},
    "observación (12) (¿la arista es correcta contra el texto?; en las incorrectas, la regla implicada con el vocabulario capa_pipeline)": {
        "O12-correcta → correcta": [
            "la arista dice lo que el texto dice: en establecida_en, el nodo es del TO; en aplica_a y ejecuta, el sujeto es el del texto; "
            "en regula y condicion_de, el texto une esos nodos así."],
        "O12-sujeto-de-otro-TO → incorrecta (catálogo)": [
            "el destino es el rol de alcance de otro TO, que la resolución del sujeto tomó de la sugerencia del modelo."]},
}


def frenar(msg: str) -> None:
    raise SystemExit(f"FRENO: {msg}")


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def hora(t: float) -> str:
    return datetime.fromtimestamp(t).astimezone().isoformat(timespec="seconds")


def ident(x) -> str:
    return x if isinstance(x, str) else " | ".join(x)


salida = {"unidad": "B6.1, tanda final, T4, primer tramo: la lectura asistida (pre-registro firmado en 4de7f2a7, §6: lectura asistida "
                    "con revisión de la autora, D2, como en el T4 de la tanda 1)",
          "modelo": {"nombre": "Claude Opus 5.5", "id": "claude-opus-5-5",
                     "como": "la ejecutora de esta sesión de Claude Code lee cada ficha y escribe su propuesta; sin API ni otro modelo, "
                             "USD 0"},
          "hora_de_la_lectura": {}, "material": {}, "criterios_de_la_propuesta": CRITERIOS, "reglas_usadas": {}, "cuentas": {},
          "propuestas": {}}
aparte = ["# Omisiones y observaciones de la lectura asistida, T4 de la tanda final, primer tramo", "",
          "Lo que va aparte del veredicto: no cambia ninguna propuesta (las propuestas y sus criterios están en "
          "`lectura_asistida_t4_tramo1.json`). Las omisiones son contenido del texto sin nodo o sin relación; las observaciones, lo que "
          "noté en la ficha y no decide la propuesta. Por muestra y por ficha, con el número del encabezado «## n.» de su `.md`.", ""]
planillas, horas = {}, []
for m in MUESTRAS:
    mat = M3 / "material" / m
    blanca = list(csv.DictReader(io.StringIO((mat / f"planilla_{m}.csv").read_text(encoding="utf-8"), newline="")))
    fichas = [json.loads(x) for x in (mat / f"fichas_{m}.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    md = (mat / f"fichas_{m}.md").read_text(encoding="utf-8")
    mu = json.loads((M3 / f"{m}.json").read_text(encoding="utf-8"))
    pb = B / f"{m}.jsonl"
    borr = {x["n"]: x for x in (json.loads(l) for l in pb.read_text(encoding="utf-8").splitlines() if l.strip())}
    st = pb.stat()
    horas.append((st.st_birthtime, st.st_mtime))
    salida["hora_de_la_lectura"][m] = {"primera_propuesta": hora(st.st_birthtime), "ultima_escritura": hora(st.st_mtime)}
    de_la_muestra = [(c, ident(e)) for c, x in mu["celdas"].items() for e in x["elementos"]]
    if len(de_la_muestra) != mu["n"]:
        frenar(f"{m}: la muestra tiene {len(de_la_muestra)} elementos y n={mu['n']}")
    if sorted(de_la_muestra) != sorted((r["celda"], r["id"]) for r in blanca):
        frenar(f"{m}: los pares (celda, id) de la planilla en blanco no son los de la muestra")
    if len(fichas) != len(blanca) or sorted(borr) != list(range(1, len(blanca) + 1)):
        frenar(f"{m}: {len(fichas)} fichas, {len(blanca)} filas en blanco y {len(borr)} propuestas")
    filas, props = [COLS], []
    for r, f in zip(blanca, fichas):
        n = int(r["n"])
        if f["n"] != n or ident(f["id"]) != r["id"] or f["celda"] != r["celda"]:
            frenar(f"{m}: la ficha {n} del .jsonl no es la fila {n} de la planilla en blanco")
        if f"## {n}. `{r['id']}` — {r['celda']} ·" not in md:
            frenar(f"{m}: el .md no tiene el encabezado de la ficha {n}")
        p = borr[n]
        if p["propuesta"] not in VALIDAS[m] or not p["justificacion"].strip() or re.search(r"[\r\n\t]", p["justificacion"]):
            frenar(f"{m}: la propuesta {n} no tiene una respuesta válida o su justificación no es de una línea")
        ficha = f"data/experiment/tanda_final/t3/muestras/material/{m}/fichas_{m}.md#{n}"
        filas.append([r["id"], r["celda"], ficha, p["propuesta"], p["justificacion"].strip(), "", ""])
        props.append({"n": n, "id": r["id"], "celda": r["celda"], "ficha": ficha, "propuesta": p["propuesta"], "regla": p["regla"],
                      "justificacion": p["justificacion"].strip()})
    planillas[m] = filas
    salida["propuestas"][m] = props
    salida["cuentas"][m] = dict(Counter(p["propuesta"] for p in props))
    salida["reglas_usadas"][m] = dict(Counter(p["regla"] for p in props))
    salida["material"][m] = {"fichas_md": f"data/experiment/tanda_final/t3/muestras/material/{m}/fichas_{m}.md",
                             "sha256_md": sha(mat / f"fichas_{m}.md"), "sha256_jsonl": sha(mat / f"fichas_{m}.jsonl"),
                             "sha256_planilla_en_blanco": sha(mat / f"planilla_{m}.csv"), "fichas": len(props)}
    aparte += [f"## {NOMBRE[m]} ({len(props)} fichas; `{m}.csv`)", ""]
    hubo = False
    for n in sorted(borr):
        p = borr[n]
        partes = [f"omisión: {p['omisiones']}" if p.get("omisiones") else None,
                  f"observación: {p['observacion']}" if p.get("observacion") else None]
        partes = [x for x in partes if x]
        if partes:
            hubo = True
            aparte.append(f"- **{n}.** `{blanca[n - 1]['id'][:90]}{'…' if len(blanca[n - 1]['id']) > 90 else ''}` — " + " ".join(partes))
    if not hubo:
        aparte.append("- Ninguna.")
    aparte.append("")
salida["hora_de_la_lectura"]["toda"] = {"primera_propuesta": hora(min(h[0] for h in horas)), "ultima_escritura": hora(max(h[1] for h in horas)),
                                        "ancla": "st_birthtime y st_mtime de cada borrador, en el directorio de los borradores"}
salida["total"] = {"fichas": sum(len(v) for v in salida["propuestas"].values())}
LA, LU = T4 / "lectura_asistida", T4 / "lectura_autora"
(LA / "borradores").mkdir(parents=True, exist_ok=True)
LU.mkdir(parents=True, exist_ok=True)
for m in MUESTRAS:
    dst = LA / "borradores" / f"{m}.jsonl"
    if dst.exists() and sha(dst) != sha(B / f"{m}.jsonl"):
        frenar(f"{dst} ya existe y es distinto: no lo piso")
    shutil.copyfile(B / f"{m}.jsonl", dst)
    p = LU / f"{m}.csv"
    buf = io.StringIO()
    csv.writer(buf, delimiter=";", lineterminator="\n").writerows(planillas[m])
    if p.exists() and p.read_text(encoding="utf-8") != buf.getvalue():
        frenar(f"{p} ya existe y es distinta: no la piso")
    p.write_text(buf.getvalue(), encoding="utf-8")
    salida["material"][m]["planilla_de_la_autora"] = {"ruta": f"data/experiment/tanda_final/t4/lectura_autora/{m}.csv", "sha256": sha(p)}
(LA / "lectura_asistida_t4_tramo1.json").write_text(json.dumps(salida, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
(LA / "omisiones_y_observaciones_t4_tramo1.md").write_text("\n".join(aparte), encoding="utf-8")
print(json.dumps({"total": salida["total"], "hora": salida["hora_de_la_lectura"]["toda"], "cuentas": salida["cuentas"],
                  "planillas": {m: salida["material"][m]["planilla_de_la_autora"]["sha256"] for m in MUESTRAS}}, ensure_ascii=False, indent=1))
