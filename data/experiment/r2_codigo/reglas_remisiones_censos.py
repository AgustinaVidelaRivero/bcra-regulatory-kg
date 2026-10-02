"""U-R2-CODIGO, decisiones sobre el freno posterior a R3 — dos mediciones
informativas de las reglas (a) a (i) del detector de remisiones del perfil r2
(r1_referencias.detectar_menciones_r2). Solo lectura, en memoria. USD 0.

  F. Censo de la regla (f), antes de cerrar la lista de formas de cita: en los
     diez TOs de la tanda 0, las formas «inciso», «acápite», «ítem» y «numeral»
     (singular y plural, con y sin tilde) seguidas de un número con puntos, sobre
     el texto de cada chunk de E0 (texto propio, sin la herencia, para no contar
     dos veces), normalizado como en la detección (normalizar_e0, con la línea
     suelta de la regla a). Conteo por forma y por TO y una muestra por forma.
     Para comparar, el mismo conteo con «punto» y «apartado».

  E. Formas de la regla (e) en la E0 congelada de los diez TOs
     (`e0_chunking/salida_tanda0`, texto propio de cada chunk, normalizado):
     las siete de la lista de la autora, las variantes que el detector cubre
     además, las del propio TO («de las presentes normas», «de las presentes
     disposiciones», «del presente régimen») y, aparte, «de estas normas», que
     el detector no trata. Con el mismo conteo en la partición.

  G. Citas de norma sin comillas («TO sobre Gestión Crediticia, deberá…»):
     menciones de `RE_NORMA_R2` sin comilla de apertura, sobre el texto propio
     de cada chunk de la E0 congelada de los diez TOs y de la partición.

  P. Partición del corpus escalado (segmentacion_84/b584_particion, 152 TOs):
     cuántas citas cambia cada regla, acumuladas en orden, sobre el texto de cada
     chunk de E0 (texto propio más los tramos heredados de su propia unidad, como
     `_texto_e0_de` para el punto propio). Una cita es la mención con su clase,
     TO de destino o causa, puntos y secciones; «cambia» cuenta las que aparecen
     o desaparecen entre un paso y el siguiente. Inventario de la regla (g): los
     157 títulos (inventario_tos.csv y los cinco TOs de desarrollo de
     inventario_resumen.json). Antes de (g) la cadena r1 resuelve con el
     inventario cableado de cinco TOs (r1_referencias.INVENTARIO_TOS); por eso
     el paso (g) se informa además con las dos comparaciones sobre los mismos
     157 títulos: título contenido en el nombre (subcadena) contra título igual
     o que empieza con el nombre (regla g).
     No se miden en la partición: (b), porque la partición no tiene salida de
     e0-r2 (su E0 sale de correr_b584.py, con el camino sin raíz y los
     marcadores, no de correr_e0.py); (i), porque cambia a qué nodos va una cita
     del texto heredado y la partición no tiene grafo.
     Control: sin reglas, el detector r2 da exactamente las menciones de la
     cadena r1 (`detectar_menciones`) en cada chunk de la partición.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/reglas_remisiones_censos.py --out <json> \
      [--e0-r2 <salida de correr_e0.py --version-e0 e0-r2 de la tanda 0>]
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "corpus_v2", REX, REPO / "data" / "experiment" / "grafo_v2" / "code"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import r1_comun as C  # noqa: E402
import r1_referencias as REF  # noqa: E402

E0_TANDA0 = REX / "e0_chunking" / "salida_tanda0"
MAN_DIEZ = REX / "manifiestos" / "tanda0_10tos.json"
PARTICION = REPO / "data" / "experiment" / "segmentacion_84" / "b584_particion"
MUESTRA = 5
RE_FORMAS = re.compile(
    r"\b(incisos?|ac[aá]pites?|[íi]tems?|numeral(?:es)?|puntos?|apartados?)\s+(\d+(?:\.\d+)+\.?)", re.I)
FORMA_CANONICA = {"inciso": "inciso", "incisos": "inciso", "acapite": "acápite", "acapites": "acápite",
                  "item": "ítem", "items": "ítem", "numeral": "numeral", "numerales": "numeral",
                  "punto": "punto", "puntos": "punto", "apartado": "apartado", "apartados": "apartado"}
PASOS_PARTICION = ("", "a", "ac", "acd", "acde", "acdef", "acdefg", "acdefgh")


def cargar_lista(p: Path) -> list[dict]:
    d = json.loads(p.read_text(encoding="utf-8"))
    return d["chunks"] if isinstance(d, dict) else d


def censo_formas(e0_dir: Path) -> dict:
    tos = [t["id"] for t in json.loads(MAN_DIEZ.read_text(encoding="utf-8"))["tos"]]
    cuenta, por_to, muestras = Counter(), {}, {}
    for to in tos:
        c_to = Counter()
        for ch in cargar_lista(e0_dir / f"chunks_{to}.json"):
            original = ch.get("texto") or ""
            texto, mapa = REF.normalizar_e0(original, tolerar_linea_suelta=True)
            for m in RE_FORMAS.finditer(texto):
                f = FORMA_CANONICA[C.norm(m.group(1))]
                cuenta[f] += 1
                c_to[f] += 1
                if f in ("punto", "apartado") or len(muestras.setdefault(f, [])) >= MUESTRA:
                    continue
                o_ini, o_fin = mapa[m.start()], mapa[m.end() - 1] + 1
                muestras[f].append({"to": to, "chunk_id": ch["id"], "tramo": original[o_ini:o_fin],
                                    "contexto": original[max(0, o_ini - 120):o_fin + 80]})
        por_to[to] = dict(sorted(c_to.items()))
    return {"texto": str(e0_dir.relative_to(REPO)) if e0_dir.is_relative_to(REPO) else "e0-r2 (--e0-r2)",
            "criterio": RE_FORMAS.pattern, "por_forma": dict(sorted(cuenta.items())), "por_to": por_to,
            "muestras": muestras}


FORMAS_E = {
    "de las citadas normas": r"de\s+las\s+citadas\s+normas",
    "de dichas normas": r"de\s+dichas\s+normas",
    "del citado ordenamiento": r"del\s+citado\s+ordenamiento",
    "del citado TO": r"del\s+citado\s+T\.?\s?O\b",
    "dicho TO": r"\bdicho\s+T\.?\s?O\b",
    "de la citada norma": r"de\s+la\s+citada\s+norma\b",
    "de las citadas disposiciones": r"de\s+las\s+citadas\s+disposiciones",
    "variante: de las normas citadas": r"de\s+las\s+normas\s+citadas",
    "variante: de dicho ordenamiento o texto ordenado": r"de\s+dicho\s+(?:ordenamiento|texto\s+ordenado)",
    "variante: de ese ordenamiento o texto ordenado": r"de\s+ese\s+(?:ordenamiento|texto\s+ordenado)",
    "variante: de este ordenamiento o texto ordenado": r"de\s+este\s+(?:ordenamiento|texto\s+ordenado)",
    "propio TO: de las presentes normas": r"de\s+las\s+presentes\s+normas",
    "propio TO: de las presentes disposiciones": r"de\s+las\s+presentes\s+disposiciones",
    "propio TO: del presente régimen": r"del\s+presente\s+r[eé]gimen",
    "no tratada: de estas normas": r"de\s+estas\s+normas",
}


def conteo_formas_y_sin_comillas(chunks: list[tuple[str, dict]]) -> dict:
    formas, ejemplos, sin_com, total = Counter(), {}, 0, 0
    for to, ch in chunks:
        t = REF.normalizar_e0(ch.get("texto") or "")[0]
        for f, pat in FORMAS_E.items():
            for m in re.finditer(pat, t, re.I):
                formas[f] += 1
                ejemplos.setdefault(f, {"chunk_id": ch["id"], "tramo": t[max(0, m.start() - 100):m.end() + 10]})
        for m in REF.RE_NORMA_R2.finditer(t):
            total += 1
            sin_com += m.group("q") is None
    return {"formas": {f: formas[f] for f in FORMAS_E}, "ejemplos": ejemplos,
            "menciones_de_norma": total, "sin_comillas": sin_com}


def tos_particion() -> list[str]:
    return sorted(d.name for d in PARTICION.iterdir() if d.is_dir() and (d / f"chunks_{d.name}.json").exists())


def texto_chunk(ch: dict) -> str:
    partes = [h["texto"] for h in ch.get("herencia", []) if h["unidad_origen"] == ch.get("unidad")]
    return "\n".join(partes + [ch.get("texto") or ""])


def clave(cid: str, m: dict) -> tuple:
    return (cid, m["clase"], m["to_destino"], m.get("causa_irresoluble"), tuple(m["puntos"]), tuple(m["secciones"]))


def particion() -> dict:
    tos = tos_particion()
    inv = REF.titulos_de_inventario(sorted({r["id"] for r in __import__("csv").DictReader(
        REF.INVENTARIO_TITULOS.open(encoding="utf-8"))} | {"cap", "cla", "ext", "pro", "ric"}))
    REF.TITULOS_TOS = inv
    chunks = [(to, ch) for to in tos for ch in cargar_lista(PARTICION / to / f"chunks_{to}.json")]
    distintos_r1 = []
    citas: dict[str, set] = {}
    por_paso: dict[str, Counter] = {}
    for reglas in PASOS_PARTICION:
        rs = frozenset(reglas)
        s, cl = set(), Counter()
        for to, ch in chunks:
            texto = REF.normalizar_e0(texto_chunk(ch), tolerar_linea_suelta="a" in rs)[0]
            ms = REF.detectar_menciones_r2(texto, to, rs)
            if not reglas and ms != REF.detectar_menciones(texto, to):
                distintos_r1.append(ch["id"])
            for m in ms:
                s.add(clave(ch["id"], m))
                cl[m["clase"]] += 1
        citas[reglas] = s
        por_paso[reglas] = cl
    pasos = []
    for i, reglas in enumerate(PASOS_PARTICION):
        fila = {"reglas": reglas or "ninguna (regla de R3)", "citas": len(citas[reglas]),
                "menciones_por_clase": dict(sorted(por_paso[reglas].items()))}
        if i:
            a, b = citas[PASOS_PARTICION[i - 1]], citas[reglas]
            fila["contra_el_paso_anterior"] = {"aparecen": len(b - a), "desaparecen": len(a - b),
                                               "citas_que_cambian": len(a ^ b)}
        pasos.append(fila)

    # (g) sobre los mismos 157 títulos: subcadena contra la regla
    sub = Counter()
    ejemplos = []
    for to, ch in chunks:
        texto = REF.normalizar_e0(texto_chunk(ch), tolerar_linea_suelta=True)[0]
        for m in REF.RE_NORMA_R2.finditer(texto):
            z, q = m.group("z").strip(), m.group("q") is not None
            zn = C.norm(z)
            contiene = sorted(t for t, tit in inv.items() if tit and tit in zn)
            regla = REF.resolver_norma_r2(z, q)
            k = ("resuelve" if regla else "no resuelve") + " con (g) / " + (
                "algún título contenido" if contiene else "ningún título contenido")
            sub[k] += 1
            if contiene and regla not in contiene and len(ejemplos) < 15:
                ejemplos.append({"chunk_id": ch["id"], "nombre": z, "entrecomillado": q,
                                 "titulos_contenidos": contiene, "regla_g": regla})
    return {"tos": len(tos), "chunks": len(chunks), "inventario_titulos": len(inv),
            "control_sin_reglas_igual_a_cadena_r1": not distintos_r1,
            "chunks_distintos_sin_reglas": distintos_r1[:20],
            "pasos": pasos,
            "g_mismos_157_titulos": {"menciones_de_norma": sum(sub.values()), "por_criterio": dict(sorted(sub.items())),
                                     "ejemplos_titulo_contenido_que_g_no_toma": ejemplos},
            "no_medidas": {"b": "la partición no tiene salida de e0-r2: su E0 sale de correr_b584.py (camino sin "
                                "raíz y marcadores), no de correr_e0.py",
                           "i": "cambia a qué nodos va una cita del texto heredado; la partición no tiene grafo"}}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--e0-r2", type=Path, default=None,
                    help="salida de correr_e0.py --version-e0 e0-r2 de la tanda 0 (texto del censo F)")
    a = ap.parse_args()
    tos10 = [t["id"] for t in json.loads(MAN_DIEZ.read_text(encoding="utf-8"))["tos"]]
    diez = [(to, ch) for to in tos10 for ch in cargar_lista(E0_TANDA0 / f"chunks_{to}.json")]
    part = [(to, ch) for to in tos_particion() for ch in cargar_lista(PARTICION / to / f"chunks_{to}.json")]
    out = {"unidad": "U-R2-CODIGO", "etapa": "decisiones sobre el freno posterior a R3 (informativo)",
           "F_censo_formas_diez_tos": censo_formas(a.e0_r2 or E0_TANDA0),
           "E_formas_anafora_e0_congelada": {"diez_tos": conteo_formas_y_sin_comillas(diez),
                                             "particion": conteo_formas_y_sin_comillas(part)},
           "P_particion_cambios_por_regla": particion()}
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"F": out["F_censo_formas_diez_tos"]["por_forma"],
                      "P": {k: v for k, v in out["P_particion_cambios_por_regla"].items()
                            if k in ("tos", "chunks", "control_sin_reglas_igual_a_cadena_r1", "pasos")}},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
