"""U-NOSEG-LIMITE, L4 — desglose por norma de las 189 citas irresolubles por «norma fuera del
inventario» de KG-Tanda0-Diez-r2a, y cuántas apuntan a los 14 TOs fuera de las tandas.

Solo lectura, USD 0. Escribe `l4_citas_189.json` y `l4_citas_189.md`.

Fuente: data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/remisiones_registro.json (1.566
registros) y reporte_ensamblado_r2.json (`remite_a.irresolubles_por_causa`).

Regla (escrita antes de correr):
1. Unidad de conteo: el par único (chunk_id, evidencia) de los registros cuyo `irresolubles` trae la
   causa «norma fuera del inventario». Control: tiene que dar el 189 del reporte.
2. Nombre normalizado: minúsculas, sin acentos, cortes de línea con guion unidos, espacios colapsados.
3. Cruce automático con los títulos de los 157 TOs (`inventario_tos.csv` y `subset_excluido` de
   `inventario_resumen.json`), sin el prefijo «RI - » / «RI Cont. Mensual - » / «RI para … - » y sin
   punto final: el TO cuyo título normalizado es prefijo del nombre; si ninguno lo es, el TO cuyo
   título empieza con el nombre (con al menos 20 caracteres). Si hay más de uno, el de título más
   largo. [Corrección del 04/10/2026, tras la primera corrida: la versión anterior mezclaba las dos
   condiciones y el desempate por largo mandaba `pscpp` a `ri_pscpp` por el sufijo «(ri-pscpp)».]
4. Títulos repetidos entre normativa general y régimen informativo (por ejemplo `pscpp` y
   `ri_pscpp`): va al de normativa general, salvo que la evidencia diga «régimen informativo».
5. Lo que no cruza va a la tabla ADJUDICACION_MANUAL de abajo, con su clase y su nota: TO de
   desarrollo o de los 152 con el nombre deformado por la extracción, anáfora («dicho ordenamiento»),
   o norma fuera de los 157. Es lectura asistida: la columna `revision_autora` queda vacía.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/no_segmentables_limite/code/l4_citas_189.py
"""

from __future__ import annotations

import csv
import json
import re
import unicodedata
from collections import Counter, defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parents[4]
ENS = REPO / "data" / "experiment" / "reextraccion_v2" / "corpus_tanda0" / "ens_diez_r2a" / "r2"
PREP = REPO / "data" / "experiment" / "escalado_prep"
OUT = REPO / "data" / "experiment" / "no_segmentables_limite"
CATORCE = {"manual", "ri2_pm", "optico", "plandecuentas", "ri_chr", "ri_con", "ri_fcem", "ri_itme",
           "ri_pfmipyme", "ri_pscpp", "ri_pspii", "ri_rem", "ri_spi", "ri_tii"}
DESARROLLO = {"cap", "cla", "ext", "pro", "ric"}

# nombre normalizado -> (clase, to o None, nota). Se completa leyendo cada caso que no cruza.
ADJUDICACION_MANUAL = {
    "dicho ordenamiento": ("anafora", None, "remite a un ordenamiento nombrado antes; sin nombre propio"),
    "cafila 10: col4 = pitales minimos de las entidades financieras": (
        "to_deformado", "cap", "fila de tabla serializada que parte «Capitales mínimos»; cap es de desarrollo"),
    "su- 2 pervision consolidada": ("to_deformado", "supcon", "«Supervisión consolidada» partida por un salto de línea"),
    "evaluacion de entidades financieras": ("fuera_de_los_157", None, "sin TO con ese título en el inventario"),
    "posiciones de derivados no cubiertos": ("fuera_de_los_157", None, "sin TO con ese título en el inventario"),
    "confidencialidad a que se refieren las leyes de entidades financieras (arts": (
        "fuera_de_los_157", None, "remite a leyes, no a un TO"),
    "la “relacion para los activos inmovilizados y otros conceptos": (
        "to_152", "relact", "comilla inicial; normativa general"),
    # casos que no cruzaron en la primera corrida (04/10/2026), adjudicados leyendo nombre y evidencia
    "determinacion de la condicion de micro, pequena y mediana empresa": (
        "to_152", "micemp", "«y» por «o» respecto del título del inventario"),
    "determinacion de la condicion de micro, pequena y mediana empresa, que se ajusten a los cr": (
        "to_152", "micemp", "«y» por «o» respecto del título del inventario"),
    "requisitos minimos de gestion, implementacion y control de los riesgos relacionados con tecnologia "
    "informatica, sistemas de informacion y recursos asociados para las entidades financieras": (
        "to_152", "rmgcti", "título anterior del TO; la equivalencia es de lectura, NO VERIFICADA contra su historial"),
    "aplicacion del sistema de seguro de garantia de los depositos": (
        "to_152", "seggar", "«de los depósitos» por «de depósitos»"),
    "conservacion y reproduccion de documentos": (
        "to_152", "consyr", "título abreviado de «Instrumentación, conservación y reproducción de documentos»"),
    "lineamientos para la gestion de los riesgos en las entidades financieras": (
        "to_152", "lingeef", "«de los riesgos» por «de riesgos»"),
    "lineamientos para la gestion de riesgo en las entidades financieras": (
        "to_152", "lingeef", "«de riesgo» por «de riesgos»"),
    "presentacion de informaciones al banco central": (
        "uno_de_los_14", "optico", "«Sección 8. de las normas sobre “Presentación de informaciones al Banco Central”» "
        "(docvig::3.6.1); optico trae índice e historial, no el texto de sus secciones"),
    "requisitos operativos minimos de tecnologia y sistemas de informacion para las casas y agencias de cambio": (
        "to_152", "reqcac", "título abreviado en el inventario («p/ Casas…»)"),
}


def norm(s: str) -> str:
    s = re.sub(r"-\n", "", s or "")
    s = unicodedata.normalize("NFKD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.replace("–", "-").replace("—", "-")
    return re.sub(r"\s+", " ", s).strip().rstrip(".")


def titulos() -> dict[str, tuple[str, str]]:
    t = {}
    with (PREP / "inventario_tos.csv").open(encoding="utf-8") as f:
        for r in csv.DictReader(f):
            tit = re.sub(r"^ri( cont\. mensual| para [a-z ]+)? - ", "", norm(r["titulo_oficial"]))
            t[r["id"]] = (tit, r["categoria"])
    for x in json.loads((PREP / "inventario_resumen.json").read_text(encoding="utf-8"))["subset_excluido"]:
        tit = re.sub(r"^ri( cont\. mensual| para [a-z ]+)? - ", "", norm(x["titulo"]))
        t[x["id_interno"]] = (tit, "regimen_informativo" if x["id_interno"] == "ric" else "normativa_general")
    return t


def cruzar(nombre: str, evid: str, tit: dict) -> str | None:
    cands = [to for to, (t, _) in tit.items() if nombre.startswith(t)]
    if not cands:
        cands = [to for to, (t, _) in tit.items() if len(nombre) >= 20 and t.startswith(nombre)]
    if not cands:
        return None
    largo = max(len(tit[c][0]) for c in cands)
    cands = [c for c in cands if len(tit[c][0]) == largo]
    if len(cands) > 1:
        ri = "regimen informativo" in norm(evid)
        pref = [c for c in cands if (tit[c][1] == "regimen_informativo") == ri]
        cands = pref or cands
    return sorted(cands)[0]


def main() -> None:
    reg = json.loads((ENS / "remisiones_registro.json").read_text(encoding="utf-8"))
    rep = json.loads((ENS / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    esperado = rep["remite_a"]["irresolubles_por_causa"]["norma fuera del inventario"]
    filas = [x for x in reg if any(i["causa"] == "norma fuera del inventario" for i in x["irresolubles"])]
    unicos = {}
    for x in filas:
        unicos.setdefault((x["chunk_id"], x["evidencia"]), x)
    assert len(unicos) == esperado, (len(unicos), esperado)
    tit = titulos()
    por_nombre = defaultdict(list)
    for (cid, ev), x in sorted(unicos.items()):
        por_nombre[norm(x["norma_nombrada"])].append((cid, ev))
    tabla, clase_n = [], Counter()
    for nombre, casos in sorted(por_nombre.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if nombre in ADJUDICACION_MANUAL:
            clase, to, nota = ADJUDICACION_MANUAL[nombre]
            via = "lectura"
        else:
            to = cruzar(nombre, casos[0][1], tit)
            via, nota = "titulo", ""
            if to is None:
                clase = "sin_cruce"
            elif to in CATORCE:
                clase = "uno_de_los_14"
            elif to in DESARROLLO:
                clase = "to_desarrollo"
            else:
                clase = "to_152"
        clase_n[clase] += len(casos)
        tabla.append({"norma_nombrada": nombre, "citas": len(casos), "clase": clase, "to": to, "via": via,
                      "nota": nota, "tos_de_origen": dict(Counter(c.split("::")[0] for c, _ in casos)),
                      "revision_autora": ""})
    assert sum(r["citas"] for r in tabla) == esperado
    a14 = [r for r in tabla if r["clase"] == "uno_de_los_14"]
    res = {"_meta": {"unidad": "U-NOSEG-LIMITE, L4", "fuente": str((ENS / "remisiones_registro.json").relative_to(REPO)),
                     "registros_con_la_causa": len(filas), "pares_unicos": len(unicos), "reporte": esperado,
                     "nombres_distintos": len(tabla)},
           "por_clase": dict(clase_n), "a_los_14": a14, "tabla": tabla}
    (OUT / "l4_citas_189.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    L = ["# L4 — las 189 citas irresolubles por «norma fuera del inventario» (code/l4_citas_189.py)", "",
         f"Registros con la causa: {len(filas)}; pares únicos (chunk, evidencia): {len(unicos)} = reporte "
         f"({esperado}); nombres distintos: {len(tabla)}.", "",
         "Por clase: " + ", ".join(f"{k} {v}" for k, v in sorted(clase_n.items())) + ".", "",
         "| citas | norma nombrada (normalizada) | clase | TO | vía |", "|--:|---|---|---|---|"]
    for r in tabla:
        L.append(f"| {r['citas']} | {r['norma_nombrada'][:90]} | {r['clase']} | {r['to'] or '—'} | {r['via']} |")
    (OUT / "l4_citas_189.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(dict(clase_n), [(r["norma_nombrada"], r["citas"], r["to"]) for r in a14])
    print([(r["norma_nombrada"], r["citas"]) for r in tabla if r["clase"] == "sin_cruce"])


if __name__ == "__main__":
    main()
