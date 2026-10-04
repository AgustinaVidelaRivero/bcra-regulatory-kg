"""U-R2-CODIGO-2, C2, freno de diseño — punto (h): tope de la herencia en e0-r2 (USD 0, sin API). Solo escribe --out.

Simula, sobre los `chunks_<to>.json` de una salida de E0, el recorte que el diseño propone para `herencia_de`
(`e0_chunking/e0_lib.py:1618-1651`). Mide qué unidades cambian y qué texto se omite. No edita E0.

Regla simulada (la del diseño):
  - rige solo en la unidad cuya herencia (suma de los textos de sus tramos) supera U caracteres;
  - los tramos `encabezado` (títulos de todos los ancestros) quedan siempre enteros;
  - cada bloque de prosa heredado conserva su tramo más cercano a la unidad (si pasa B, recortado por renglones
    desde su extremo cercano hasta B, sin partir un bloque de tabla serializada) y, a continuación, tramos enteros
    hasta sumar B caracteres más. Un bloque es el grupo de tramos de la misma unidad de origen y el mismo rol (la
    intro o el chapeau de sección, el cierre); los intersticiales de un ancestro forman un bloque por lado de la
    unidad (antes y después);
  - extremo más cercano: el final, en la intro y el chapeau (preceden a los hijos: ahí está la cláusula que abre
    la lista); el comienzo, en el cierre (sigue a los hijos: «lo dispuesto precedentemente no rige…» va al
    principio); en el intersticial, el final si está antes de la unidad y el comienzo si está después. En la
    implementación la posición sale de la línea de cada segmento; acá, de las páginas (si se superponen, cuenta
    como antes, y se cuenta aparte);
  - en el lugar de lo omitido va un tramo marcador de una línea, con el rol del bloque y los caracteres omitidos.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c2d_herencia.py \
      --salida-e0 tanda0=data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2 \
      --salida-e0 particion=data/experiment/segmentacion_84/b584_particion \
      [--salida-e0 e0r2_152=<dir de e0-r2 de los 152>] --out data/experiment/r2_codigo2/salidas/c2d_herencia.json
"""
from __future__ import annotations

import argparse
import json
import re
from collections import Counter, OrderedDict
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[3]
U_REFERENCIA = 13091          # correr_e0.OBJETIVO_CHARS_PARTE (correr_e0.py:75)
B_PROPUESTO = 2000
ESTRATO_FUERA_DE_MUESTRA = ("ayccef", "expaef", "opefci", "adrei")
FUERA_DE_LAS_TANDAS = RAIZ / "data" / "experiment" / "no_segmentables_limite" / "l1_peso.json"
# frases de un cierre que vale para todos los ítems: si aparecen en la parte omitida, el recorte puede perder alcance
RE_ALCANCE = re.compile(r"precedente|lo dispuesto|no (?:rige|ser[aá] de aplicaci[oó]n|alcanza)|"
                        r"en todos los casos|a los efectos de (?:este|estos|los) (?:punto|apartado)", re.I)
MARCA = "[recorte de E0: no se transcriben {n} caracteres de este bloque heredado]"


def marcador(n: int) -> str:
    return MARCA.format(n=n)


def lado(tramo: dict, paginas_unidad: list[int]) -> tuple[str, bool]:
    """Extremo que se conserva y si la posición del intersticial quedó ambigua."""
    if tramo["tipo"] in ("intro", "chapeau_seccion"):
        return "final", False
    if tramo["tipo"] == "cierre":
        return "inicio", False
    pt, pu = tramo.get("paginas") or [], paginas_unidad or []
    if pt and pu and min(pt) > max(pu):
        return "inicio", False
    ambiguo = not (pt and pu and max(pt) < min(pu))
    return "final", ambiguo


def bloques(herencia: list[dict], paginas_unidad: list[int]) -> tuple[list[tuple[str, list[int]]], int]:
    """Bloques de prosa heredados: (extremo que se conserva, índices de sus tramos). La intro o el chapeau y el
    cierre de cada ancestro son un bloque cada uno; los intersticiales de un ancestro forman un bloque por lado de
    la unidad (antes y después). Devuelve también los intersticiales de posición ambigua."""
    grupos: dict[tuple, list[int]] = {}
    orden: list[tuple] = []
    ambiguos = 0
    for i, t in enumerate(herencia):
        if t["tipo"] == "encabezado":
            continue
        sentido, amb = lado(t, paginas_unidad)
        ambiguos += amb
        clave = (t["unidad_origen"], "intersticial" if t["tipo"] == "intersticial" else t["tipo"], sentido)
        if clave not in grupos:
            grupos[clave] = []
            orden.append(clave)
        grupos[clave].append(i)
    return [(k[2], grupos[k]) for k in orden], ambiguos


def _piezas(texto: str) -> list[str]:
    """Renglones del tramo; un bloque de tabla serializada ([TABLA … FIN TABLA …]) es una sola pieza."""
    out, tabla = [], None
    for ln in texto.split("\n"):
        if tabla is not None:
            tabla.append(ln)
            if ln.startswith("[FIN TABLA "):
                out.append("\n".join(tabla))
                tabla = None
        elif ln.startswith("[TABLA "):
            tabla = [ln]
        else:
            out.append(ln)
    if tabla is not None:
        out.append("\n".join(tabla))
    return out


def recortar_tramo(texto: str, sentido: str, B: int) -> str:
    """Piezas enteras desde el extremo cercano hasta B; la más cercana entra siempre."""
    piezas = _piezas(texto)
    idx = list(range(len(piezas)))
    if sentido == "final":
        idx.reverse()
    acum, quedan = 0, []
    for k, i in enumerate(idx):
        n = len(piezas[i]) + 1
        if k == 0 or acum + n <= B:
            quedan.append(i)
            acum += n
        else:
            break
    return "\n".join(piezas[i] for i in sorted(quedan))


def recortar(herencia: list[dict], paginas_unidad: list[int], U: int, B: int) -> tuple[list[dict], list[dict], int]:
    total = sum(len(t["texto"]) for t in herencia)
    if total <= U:
        return herencia, [], 0
    reemplazo: dict[int, list[dict]] = {}
    declarados = []
    blqs, ambiguos = bloques(herencia, paginas_unidad)
    for sentido, blq in blqs:
        orden = list(reversed(blq)) if sentido == "final" else list(blq)
        # el tramo más cercano entra siempre (recortado por renglones si pasa B) y no consume B; B es el
        # presupuesto del contexto que se suma desde ahí
        acum, conservados = 0, [orden[0]]
        for i in orden[1:]:
            n = len(herencia[i]["texto"])
            if acum + n <= B:
                conservados.append(i)
                acum += n
            else:
                break
        omitidos = [i for i in blq if i not in conservados]
        cercano = orden[0]
        recorte_cercano = None
        if len(herencia[cercano]["texto"]) > B:
            recorte_cercano = recortar_tramo(herencia[cercano]["texto"], sentido, B)
            if recorte_cercano == herencia[cercano]["texto"]:
                recorte_cercano = None
        if not omitidos and recorte_cercano is None:
            continue
        n_om = sum(len(herencia[i]["texto"]) for i in omitidos)
        texto_om = "\n".join(herencia[i]["texto"] for i in omitidos)
        if recorte_cercano is not None:
            n_om += len(herencia[cercano]["texto"]) - len(recorte_cercano)
            texto_om += "\n" + herencia[cercano]["texto"].replace(recorte_cercano, "", 1)
        t0 = herencia[blq[0]]
        declarados.append({"unidad_origen": t0["unidad_origen"], "tipo": t0["tipo"], "conservado": sentido,
                           "tramos_omitidos": len(omitidos), "tramo_cercano_recortado": recorte_cercano is not None,
                           "caracteres_omitidos": n_om, "omitido_inicio": texto_om.strip()[:120],
                           "omitido_fin": texto_om.strip()[-120:],
                           "omitido_con_frase_de_alcance": bool(RE_ALCANCE.search(texto_om))})
        marca = {"tipo": t0["tipo"], "unidad_origen": t0["unidad_origen"], "texto": marcador(n_om),
                 "paginas": sorted({p for i in blq for p in herencia[i].get("paginas") or []})}
        for i in omitidos:
            reemplazo[i] = []
        nuevo_cercano = ([{**herencia[cercano], "texto": recorte_cercano}] if recorte_cercano is not None
                         else [herencia[cercano]])
        # el marcador va del lado de lo omitido: antes de lo conservado (final) o después (inicio)
        reemplazo[cercano] = [marca] + nuevo_cercano if sentido == "final" else nuevo_cercano + [marca]
        if omitidos and sentido == "final":
            reemplazo[cercano] = nuevo_cercano
            reemplazo[min(omitidos)] = [marca]
        elif omitidos:
            reemplazo[cercano] = nuevo_cercano
            reemplazo[max(omitidos)] = [marca]
    nueva = []
    for i, t in enumerate(herencia):
        nueva.extend(reemplazo.get(i, [t]))
    return nueva, declarados, ambiguos


def cargar(d: Path) -> dict[str, list[dict]]:
    out = {}
    for p in sorted(Path(d).rglob("chunks_*.json")):
        to = p.stem.split("_", 1)[1]
        x = json.loads(p.read_text(encoding="utf-8"))
        out[to] = x["chunks"] if isinstance(x, dict) else x
    return out


def medir(nombre: str, d: Path, U: int, B: int, fuera: set[str], detalle: bool) -> OrderedDict:
    por_to = cargar(d)
    sobre, cambian, filas = [], [], []
    omitidos_total, ambiguos, despues_sobre, con_alcance = 0, 0, [], 0
    for to, cs in sorted(por_to.items()):
        for c in cs:
            h = c.get("herencia") or []
            tot = sum(len(t["texto"]) for t in h)
            if tot <= U:
                continue
            sobre.append((to, c["id"], tot))
            nueva, decl, amb = recortar(h, c.get("paginas") or [], U, B)
            ambiguos += amb
            tot2 = sum(len(t["texto"]) for t in nueva)
            if tot2 > U:
                despues_sobre.append({"to": to, "chunk_id": c["id"], "antes": tot, "despues": tot2,
                                      "cambia": bool(decl),
                                      "tramo_mayor": max(len(t["texto"]) for t in nueva),
                                      "tramos_de_prosa": sum(1 for t in nueva if t["tipo"] != "encabezado")})
            if not decl:
                continue
            om = sum(x["caracteres_omitidos"] for x in decl)
            omitidos_total += om
            con_alcance += sum(x["omitido_con_frase_de_alcance"] and x["tipo"] == "cierre" for x in decl)
            cambian.append((to, c["id"]))
            if detalle or to in ESTRATO_FUERA_DE_MUESTRA:
                filas.append({"to": to, "chunk_id": c["id"], "herencia_antes": tot, "herencia_despues": tot2,
                              "bloques_recortados": decl})
    tos_sobre = sorted({t for t, _, _ in sobre})
    return OrderedDict([
        ("salida_e0", str(d.relative_to(RAIZ)) if d.resolve().is_relative_to(RAIZ.resolve()) else d.name),
        ("tos", len(por_to)), ("chunks", sum(len(v) for v in por_to.values())),
        ("unidades_sobre_U", len(sobre)), ("tos_con_unidades_sobre_U", len(tos_sobre)),
        ("maximo_heredado", max((s[2] for s in sobre), default=0)),
        ("sobre_U_sin_los_14_fuera_de_las_tandas", OrderedDict([
            ("unidades", sum(1 for s in sobre if s[0] not in fuera)),
            ("tos", len({s[0] for s in sobre if s[0] not in fuera}))])),
        ("por_to", dict(Counter(s[0] for s in sobre))),
        ("unidades_que_cambian", len(cambian)),
        ("caracteres_omitidos", omitidos_total),
        ("siguen_sobre_U_despues", despues_sobre),
        ("intersticiales_de_posicion_ambigua", ambiguos),
        ("cierres_recortados_con_frase_de_alcance_en_lo_omitido", con_alcance),
        ("estrato_fuera_de_muestra_que_cambia", sorted({t for t, _ in cambian if t in ESTRATO_FUERA_DE_MUESTRA})),
        ("detalle", filas)])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida-e0", action="append", required=True, help="nombre=directorio")
    ap.add_argument("--umbral", type=int, default=U_REFERENCIA)
    ap.add_argument("--bloque", type=int, default=B_PROPUESTO, nargs="+")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    fuera = {x["to"] for x in json.loads(FUERA_DE_LAS_TANDAS.read_text(encoding="utf-8"))["por_to"]}
    out = OrderedDict([("umbral_U", a.umbral), ("regla", __doc__.split("Regla simulada (la del diseño):")[1]
                                                                  .split("Uso,")[0].strip()),
                       ("marcador", MARCA), ("fuera_de_las_tandas", sorted(fuera))])
    bloques_b = a.bloque if isinstance(a.bloque, list) else [a.bloque]
    for par in a.salida_e0:
        nombre, d = par.split("=", 1)
        d = Path(d) if Path(d).is_absolute() else RAIZ / d
        out[nombre] = OrderedDict((f"B={b}", medir(nombre, d, a.umbral, b, fuera, detalle=(nombre == "tanda0")))
                                  for b in bloques_b)
    (RAIZ / a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in out.items():
        if isinstance(v, dict) and any(x.startswith("B=") for x in v):
            for b, m in v.items():
                print(k, b, {x: m[x] for x in ("unidades_sobre_U", "tos_con_unidades_sobre_U", "maximo_heredado",
                                               "unidades_que_cambian", "caracteres_omitidos",
                                               "intersticiales_de_posicion_ambigua",
                                               "cierres_recortados_con_frase_de_alcance_en_lo_omitido",
                                               "estrato_fuera_de_muestra_que_cambia")},
                      "siguen_sobre_U:", len(m["siguen_sobre_U_despues"]))


if __name__ == "__main__":
    main()
