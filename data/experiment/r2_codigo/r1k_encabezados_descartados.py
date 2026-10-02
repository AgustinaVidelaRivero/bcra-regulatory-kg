"""U-R2-CODIGO, complemento de R1 (K) — medición, sin corregir nada.

`separar_encabezado_pie` (e0_chunking/e0_lib.py:502), en la zona de
encabezado de cada página de cuerpo (hasta 5 líneas desde el principio),
descarta la línea de sección corrida, toda línea con «B.C.R.A.», toda línea
sin minúsculas (`_es_titulo_mayusculas`, :495) y la cola envuelta del título
de sección; desde el final, el pie. Para los diez TOs de la tanda 0, este
script:
  1. corre la función tal como la llama `parsear_cuerpo` en el camino vigente
     (:683) y clasifica cada línea descartada de la zona de encabezado por
     rama: sección, B.C.R.A., mayúsculas, cola de título;
  2. clasifica las de la rama de mayúsculas en `encabezado_de_pagina` (su
     texto está en las primeras 5 líneas de otra página de cuerpo del mismo
     TO) o `contenido` (no se repite), con dos criterios de igualdad: el texto
     literal y el texto sin espacios (un encabezado corrido con un espacio de
     más, «SERVI CIOS», no coincide literal);
  3. para las de contenido, el chunk de la E0 legada donde habrían caído: el
     dueño de la primera línea conservada de la misma página que sigue a la
     descartada (o, si no hay, de la última anterior);
  4. simula la regla propuesta —en la rama de mayúsculas, descartar solo lo
     que se repite, comparado sin espacios— reemplazando
     `_es_titulo_mayusculas` DENTRO de este proceso (el pipeline no se edita)
     y mide su efecto: chunks de la E0 legada sellada y de una E0 e0-r2 dada
     cuyo texto, herencia o id cambia.
USD 0, sin LLM.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
    data/experiment/r2_codigo/r1k_encabezados_descartados.py --e0-r2 <salida e0-r2> --out <json>
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
sys.path.insert(0, str(REX / "e0_chunking"))
import correr_e0 as C  # noqa: E402
import e0_lib as E0  # noqa: E402

MANIFIESTO = REX / "manifiestos" / "tanda0_10tos.json"
E0_LEGADA = REX / "e0_chunking" / "salida_tanda0"
ZONA = 5
MAX_EJEMPLOS = 10


def _rama(t: str) -> str:
    if E0.RE_SECCION.match(t) or ("B.C.R.A." in t and E0.RE_SECCION_EN_LINEA.search(t)):
        return "seccion"
    if "B.C.R.A." in t:
        return "bcra"
    if E0._es_titulo_mayusculas(t):
        return "mayusculas"
    return "cola_titulo"


def _parseo(pdf: Path, to: str, archivo: str):
    paginas = E0.extraer_lineas(pdf)
    roles = E0.clasificar_paginas(paginas)
    res = E0.parsear_cuerpo(to, archivo, paginas, roles)
    res.reasignaciones_continuidad = E0.aplicar_continuidad_enumeracion(res)
    E0.corregir_fronteras_intra_palabra(res)
    return paginas, roles, res


def _comparar(nuevos: list[dict], viejos: list[dict]) -> dict:
    a = {c["id"]: c for c in viejos}
    b = {c["id"]: c for c in nuevos}
    cambian = sorted(i for i in a.keys() & b.keys()
                     if a[i]["texto"] != b[i]["texto"] or a[i]["herencia"] != b[i]["herencia"])
    return {"chunks_antes": len(a), "chunks_despues": len(b),
            "ids_nuevos": sorted(b.keys() - a.keys()), "ids_perdidos": sorted(a.keys() - b.keys()),
            "texto_o_herencia_cambian": cambian}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--e0-r2", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    man = json.loads(MANIFIESTO.read_text(encoding="utf-8"))
    original = E0._es_titulo_mayusculas
    por_to, ejemplos = {}, []
    tot = collections.Counter()
    for t in sorted(man["tos"], key=lambda x: x["id"]):
        to, archivo, pdf = t["id"], t["archivo"], REPO / t["pdf"]
        paginas, roles, res = _parseo(pdf, to, archivo)
        cuerpo = [pi for pi, r in enumerate(roles, start=1) if r == E0.ROL_CUERPO]
        en_zona: dict[str, set[int]] = collections.defaultdict(set)
        en_zona_sin_esp: dict[str, set[int]] = collections.defaultdict(set)
        for pi in cuerpo:
            for l in paginas[pi - 1][:ZONA]:
                if l.texto.strip():
                    en_zona[l.texto.strip()].add(pi)
                    en_zona_sin_esp["".join(l.texto.split())].add(pi)
        lineas_chunk: list = []
        chunks = E0.construir_chunks(res, lineas_por_chunk=lineas_chunk)
        dueno = {id(l): chunks[i]["id"] for i, ls in enumerate(lineas_chunk) for l in ls}
        arbol = [l for l, _ in E0._recolectar_orden_documental(res)]
        n = collections.Counter()
        for pi in cuerpo:
            lineas = paginas[pi - 1]
            contenido, descartadas, _ = E0.separar_encabezado_pie(lineas)
            cab = [d for d in descartadas if not any(p.match(d.texto.strip()) for p in E0.RE_PIE)]
            n["pie"] += len(descartadas) - len(cab)
            for d in cab:
                txt = d.texto.strip()
                rama = _rama(txt)
                n[rama] += 1
                if rama != "mayusculas":
                    continue
                literal = len(en_zona[txt] - {pi}) >= 1
                sin_esp = len(en_zona_sin_esp["".join(txt.split())] - {pi}) >= 1
                if not sin_esp:
                    n["mayusculas_contenido_sin_espacios"] += 1
                if literal:
                    n["mayusculas_encabezado_de_pagina"] += 1
                    continue
                n["mayusculas_contenido"] += 1
                sig = next((l for l in arbol if l.pagina == pi and l.top > d.top), None)
                ant = next((l for l in reversed(arbol)
                            if (l.pagina, l.top) < (pi, d.top)), None)
                ref = sig or ant
                ej = {"to": to, "pagina": pi, "top": d.top, "texto": txt,
                      "se_repite_sin_espacios": sin_esp,
                      "chunk": dueno.get(id(ref)) if ref is not None else None,
                      "criterio_chunk": "linea_siguiente" if sig else "linea_anterior"}
                por_to.setdefault(to, {}).setdefault("contenido", []).append(ej)
        # simulación de la regla propuesta (solo en este proceso)
        try:
            E0._es_titulo_mayusculas = (lambda x: original(x)
                                        and len(en_zona_sin_esp.get("".join(x.split()), ())) >= 2)
            _, _, res_sim = _parseo(pdf, to, archivo)
            leg_sim, _ = C.subdividir_unidades_grandes(E0.construir_chunks(res_sim))
            _, _, res_sim2 = _parseo(pdf, to, archivo)
            r2_sim, _, no_partir = C.procesar_tablas_r2(res_sim2, pdf, to, roles)
            r2_sim, _ = C.subdividir_unidades_grandes(r2_sim, no_partir=no_partir)
        finally:
            E0._es_titulo_mayusculas = original
        sello = json.loads((E0_LEGADA / f"chunks_{to}.json").read_text(encoding="utf-8"))
        r2_act = json.loads((Path(a.e0_r2) / f"chunks_{to}.json").read_text(encoding="utf-8"))
        efecto_leg = _comparar(leg_sim, sello)
        efecto_r2 = _comparar(r2_sim, r2_act)
        por_to.setdefault(to, {})
        por_to[to].update({"paginas_cuerpo": len(cuerpo), "descartes": dict(sorted(n.items())),
                           "efecto_en_e0_legada": efecto_leg, "efecto_en_e0_r2": efecto_r2})
        tot.update(n)
    contenido = [e for to in sorted(por_to) for e in por_to[to].get("contenido", [])]
    out = {
        "unidad": "U-R2-CODIGO", "etapa": "complemento R1, K",
        "regla_medida": "e0_lib.separar_encabezado_pie, zona de encabezado de 5 líneas",
        "criterio_repeticion": "el texto está en las primeras 5 líneas de otra página de cuerpo del mismo TO",
        "regla_propuesta_simulada": ("en la rama de mayúsculas, descartar solo si el texto, sin "
                                     "espacios, está en las primeras 5 líneas de al menos 2 páginas "
                                     "de cuerpo del TO; sección, B.C.R.A., cola de título y pie, sin "
                                     "cambios"),
        "total": dict(sorted(tot.items())),
        "chunks_con_contenido_perdido": sorted({e["chunk"] for e in contenido if e["chunk"]}),
        "ejemplos": contenido[:MAX_EJEMPLOS],
        "por_to": {to: por_to[to] for to in sorted(por_to)},
        "efecto_total": {
            "e0_legada_chunks_que_cambian": sum(len(v["efecto_en_e0_legada"]["texto_o_herencia_cambian"])
                                                for v in por_to.values()),
            "e0_legada_ids_nuevos_o_perdidos": sum(len(v["efecto_en_e0_legada"]["ids_nuevos"])
                                                   + len(v["efecto_en_e0_legada"]["ids_perdidos"])
                                                   for v in por_to.values()),
            "e0_r2_chunks_que_cambian": sum(len(v["efecto_en_e0_r2"]["texto_o_herencia_cambian"])
                                            for v in por_to.values()),
            "e0_r2_ids_nuevos_o_perdidos": sum(len(v["efecto_en_e0_r2"]["ids_nuevos"])
                                               + len(v["efecto_en_e0_r2"]["ids_perdidos"])
                                               for v in por_to.values()),
        },
    }
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
