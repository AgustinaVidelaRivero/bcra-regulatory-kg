"""Agregado a la tarea a (condición del §2 de la enmienda 8 a L-ESQ-R2): fichas sin veredicto de las relaciones
(Excepcion, exceptua, Operacion).

Población: las 41 rechazadas en el crudo de KG-Tanda0-Diez-r2b (las extracciones finales r2 guardadas, con su índice en
el crudo), más las filas de U-ESTUDIO-MATRIZ que no están entre ellas, tomadas de la muestra sellada SIN LEER
(`reports/u_estudio_matriz/uestmat_muestra_60.csv` en `7e72051`, sin las columnas de veredicto y nota). De las 5 de esa
muestra, M22 (`cla::6.5.5.8`, pases activos en dólares → clasificación en Irrecuperable) es la misma relación que una
de las 41; entran M21, M23, M24 y M25. Las fichas no llevan ningún veredicto.

Uso: PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B udiag_a_fichas41.py
Lee además src/uestmat_muestra_60_7e72051.csv. Escribe salida/fichas_41_exceptua_operacion.json y .md.
"""
import ast
import csv
import json
import os
import re
import unicodedata

from udiag_comun import AQUI, SRC, TOS, cargar_chunks, cargar_salida, chunk_base, vistos_e3, tipo_unidad

OUT = os.path.join(AQUI, "salida")
HOLGURA = 2
PAT = re.compile(r"^relations\[(\d+)\]: Excepcion --exceptua--> Operacion$")
SEP = re.compile(r"\s*\[\s*(?:…|\.\.\.)\s*\]\s*")
MUESTRA = os.path.join(SRC, "uestmat_muestra_60_7e72051.csv")
AGREGADAS = ("M21", "M23", "M24", "M25")
MISMA_QUE_UNA_DE_LAS_41 = {"M22": "cla::6.5.5.8: Excepcion de los pases activos en dólares y títulos públicos nacionales "
                                  "→ Operacion de clasificación en Irrecuperable"}
INSTRUCCION = ("CONEXIÓN: si la norma que la Excepcion exceptúa está en tu unidad, conectala: `exceptua` hacia la "
               "Restriccion, `exceptua_obligacion` hacia la Obligacion. Si esa norma no está en tu unidad (está en la "
               "unidad del encabezado de una lista o en otro punto), emití la Excepcion sin esa relación y decí en la "
               "descripción qué norma exceptúa: no la conectes con otro elemento del chunk, no apuntes la relación a un "
               "`local_id` que no emitiste y no vuelvas a emitir esa norma dentro de tu unidad para tener a dónde "
               "conectarla.")
FUENTE_INSTRUCCION = ("prefijo de E1 r2b: reemplazo P3B-c1 (`prompt_r2b_parche_p3b.json`) con el ajuste P3C-d1 "
                      "(`prompt_r2b_parche_p3c.json`); el texto aparece literal en los pedidos guardados en las cachés "
                      "de C1 de U-COMP-E1 (`data/experiment/comp_e1/c1/cache/`)")


def _tokens():
    src = open(os.path.join(SRC, "code", "validador_r2.py"), encoding="utf-8").read()
    nombres = {"_GUION", "_ALNUM", "fold", "tokens_con_spans", "norm_tokens", "_ventana_minima", "verificar_tramo"}
    partes = [ast.get_source_segment(src, n) for n in ast.parse(src).body
              if (isinstance(n, ast.FunctionDef) and n.name in nombres)
              or (isinstance(n, ast.Assign) and any(isinstance(t, ast.Name) and t.id in nombres for t in n.targets))]
    from collections import Counter
    from typing import Optional
    g = {"re": re, "unicodedata": unicodedata, "Counter": Counter, "Optional": Optional}
    exec("\n\n".join(partes), g)
    return g["tokens_con_spans"], g["norm_tokens"], g["verificar_tramo"]


tokens_con_spans, norm_tokens, verificar_tramo = _tokens()


def span(texto, aguja):
    """(inicio, fin) del tramo en el texto: secuencia exacta de tokens; si no, el literal mínimo de la verificación
    por tokens del validador (holgura 2); si no, None."""
    at = norm_tokens(aguja)
    tt = tokens_con_spans(texto)
    ts = [t for t, _, _ in tt]
    n = len(at)
    if n:
        for i in range(len(ts) - n + 1):
            if ts[i:i + n] == at:
                return tt[i][1], tt[i + n - 1][2]
    nivel, literal = verificar_tramo(aguja, texto, HOLGURA)
    if nivel == "tokens" and literal:
        k = texto.find(literal)
        if k >= 0:
            return k, k + len(literal)
    return None


def marcar(bloques, tramo, etiqueta):
    """Busca cada segmento del tramo en los bloques ([(clave, texto)]) y devuelve las marcas [(clave, ini, fin, etiqueta)]
    y una nota de dónde quedó."""
    marcas, notas = [], []
    if not tramo:
        return marcas, ["sin tramo en la fuente"]
    for seg in SEP.split(tramo):
        hallado = None
        for clave, texto in reversed(bloques):  # primero el texto propio (último), después la herencia más cercana
            s = span(texto, seg)
            if s:
                hallado = (clave, s[0], s[1], etiqueta)
                break
        if hallado:
            marcas.append(hallado)
            notas.append(f"marcado en {hallado[0]}")
        else:
            notas.append("no ubicado en el texto de la unidad")
    return marcas, notas


def aplicar(texto, marcas):
    out = texto
    for _, ini, fin, et in sorted(marcas, key=lambda m: (-m[1], m[2])):
        out = out[:ini] + f"⟦{et}:" + out[ini:fin] + f"⟧" + out[fin:]
    return out


def ficha_r2b(cid, to, x, loc, s, chunks, origen_crudo):
    i = int(PAT.match(x["detalle"]).group(1))
    el = x["elemento"]
    ex, op = loc[el["source"]], loc[el["target"]]
    c = chunk_base(cid, chunks)
    bloques = [(f"herencia[{k}] {h['tipo']} {h['unidad_origen']}", h["texto"]) for k, h in enumerate(c["herencia"])]
    bloques.append(("texto propio", c["texto"]))
    me, ne = marcar(bloques, (ex.get("provenance") or {}).get("tramo"), "E")
    mo, no = marcar(bloques, (op.get("provenance") or {}).get("tramo"), "O")
    marcados = {clave: aplicar(texto, [m for m in me + mo if m[0] == clave]) for clave, texto in bloques}
    vis = vistos_e3(cid, s)
    fin = s["finales"].get(cid) or {}
    rech_e1 = [y for y in vis["rechazos_e1"] if y.get("detalle", "").startswith(f"relations[{i}]")]
    return {
        "origen": "crudo de KG-Tanda0-Diez-r2b (a9631a64…), extracción final r2 guardada",
        "to": to, "chunk_id": cid, "tipo_unidad": tipo_unidad(c), "paginas": c.get("paginas"),
        "estado_e3": fin.get("estado"), "unidad_en_la_cola": cid in s["cola"],
        "crudo_que_entra_a_e2": origen_crudo,
        "relacion_rechazada": {"indice_en_el_crudo": i, **{k: el.get(k) for k in ("predicate", "source", "target", "punto")}},
        "rechazo_en_validador_e1": [f"{y['motivo']}: {y['detalle']}" for y in rech_e1],
        "rechazo_en_validador_r2": f"{x['motivo']}: {x['detalle']}",
        "visto_por_e3": i in vis["relaciones"],
        "excepcion": {"local_id": ex["local_id"], "label": ex["label"],
                      "descripcion": (ex.get("properties") or {}).get("descripcion"),
                      "tramo": (ex.get("provenance") or {}).get("tramo"), "punto": (ex.get("provenance") or {}).get("punto"),
                      "donde_esta_el_tramo": ne},
        "operacion": {"local_id": op["local_id"], "label": op["label"],
                      "descripcion": (op.get("properties") or {}).get("descripcion"),
                      "tramo": (op.get("provenance") or {}).get("tramo"), "punto": (op.get("provenance") or {}).get("punto"),
                      "donde_esta_el_tramo": no},
        "texto_heredado_marcado": [{"bloque": clave, "texto": marcados[clave]} for clave, _ in bloques[:-1]],
        "texto_propio_marcado": marcados["texto propio"],
        "instruccion_del_prefijo": INSTRUCCION,
    }


def ficha_muestra(fila):
    return {
        "origen": (f"U-ESTUDIO-MATRIZ, muestra sellada sin leer `7e72051` (uestmat_muestra_60.csv), fila "
                   f"{fila['id']}: réplica en memoria de KG-Tanda0-Desarrollo-r1 (eab2fdd0); no es una relación del crudo "
                   "r2b; agregada por el §2 de la enmienda 8"),
        "to": fila["chunk_id"].split("::")[0], "chunk_id": fila["chunk_id"], "tipo_unidad": None, "paginas": None,
        "estado_e3": "no aplica (otra extracción)", "unidad_en_la_cola": None,
        "crudo_que_entra_a_e2": "no aplica (otra extracción)",
        "relacion_rechazada": {"indice_en_el_crudo": None, "predicate": fila["predicado"], "source": None, "target": None,
                               "punto": None},
        "rechazo_en_validador_e1": [], "rechazo_en_validador_r2": "no aplica (otra extracción)", "visto_por_e3": None,
        "excepcion": {"local_id": None, "label": fila["origen_etiqueta"], "descripcion": fila["origen_descripcion"],
                      "tramo": None, "punto": None, "donde_esta_el_tramo": ["sin tramo en la fuente"]},
        "operacion": {"local_id": None, "label": fila["destino_etiqueta"], "descripcion": fila["destino_descripcion"],
                      "tramo": None, "punto": None, "donde_esta_el_tramo": ["sin tramo en la fuente"]},
        "texto_heredado_marcado": [],
        "texto_propio_marcado": fila["texto_fragmento_e0"],
        "nota_texto": "texto de E0 de la extracción de origen (títulos heredados y texto propio juntos), tal como está en la muestra",
        "instruccion_del_prefijo": INSTRUCCION,
    }


def main():
    chunks = cargar_chunks()
    orden = {cid: k for k, cid in enumerate(chunks)}
    fichas = []
    for to in TOS:
        s = cargar_salida(to)
        for r in s["fin_r2"]:
            v = r.get("validacion")
            if not v:
                continue
            loc = {e["local_id"]: e for e in v["entidades"]}
            for x in v["rechazos"]:
                if PAT.match(x.get("detalle", "")):
                    fichas.append(ficha_r2b(r["chunk_id"], to, x, loc, s, chunks, r.get("origen_crudo")))
    assert len(fichas) == 41, len(fichas)
    fichas.sort(key=lambda f: (TOS.index(f["to"]), orden.get(f["chunk_id"], orden.get(f["chunk_id"].split("::parte")[0], 0)),
                               f["relacion_rechazada"]["indice_en_el_crudo"]))
    lector = list(csv.reader(open(MUESTRA, encoding="utf-8-sig")))
    encabezado = ["id"] + lector[0][1:]
    filas = [dict(zip(encabezado, row)) for row in lector[1:]]
    sel = [f for f in filas if f["par"] == "Excepcion --exceptua--> Operacion"]
    assert [f["id"] for f in sel] == ["M21", "M22", "M23", "M24", "M25"], [f["id"] for f in sel]
    assert all(not f["veredicto"] and not f["nota"] for f in sel), "la muestra sellada no debería tener veredictos"
    for f in sel:
        if f["id"] in AGREGADAS:
            fichas.append(ficha_muestra(f))
    fichas = [{"ficha": f"EO{k:02d}", **f} for k, f in enumerate(fichas, 1)]
    cab = {"descripcion": "Fichas sin veredicto de las relaciones (Excepcion, exceptua, Operacion) para la condición del §2 "
                          "de la enmienda 8 a L-ESQ-R2. ⟦E: …⟧ marca el tramo de la Excepcion y ⟦O: …⟧ el de la Operacion.",
           "criterio": "criterio_41_exceptua_operacion.md (sellado antes de generar estas fichas)",
           "poblacion": {"crudo_r2b": 41, "agregadas_de_U_ESTUDIO_MATRIZ": list(AGREGADAS),
                         "de_U_ESTUDIO_MATRIZ_ya_entre_las_41": MISMA_QUE_UNA_DE_LAS_41},
           "instruccion_del_prefijo": INSTRUCCION, "fuente_de_la_instruccion": FUENTE_INSTRUCCION,
           "ancla_del_rechazo_en_e1": "reextraccion_v2/e1_extractor/validador_e1.py:506-510 (firma_invalida) en d007be8",
           "fichas": fichas}
    json.dump(cab, open(os.path.join(OUT, "fichas_41_exceptua_operacion.json"), "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
    lin = ["# Fichas sin veredicto: relaciones (Excepcion, exceptua, Operacion)", "",
           cab["descripcion"], "", f"Criterio: `{cab['criterio']}`.", "",
           f"Instrucción del prefijo de E1 que rige para todas ({FUENTE_INSTRUCCION}):", "", f"> {INSTRUCCION}", "",
           "Población: las 41 rechazadas en el crudo de KG-Tanda0-Diez-r2b (EO01 a EO41) y 4 de U-ESTUDIO-MATRIZ "
           "(EO42 a EO45: M21, M23, M24 y M25; M22 es la misma relación que una de las 41).", ""]
    for f in fichas:
        rr = f["relacion_rechazada"]
        lin += [f"## {f['ficha']} — `{f['chunk_id']}`", f"- origen: {f['origen']}"]
        if rr["indice_en_el_crudo"] is not None:
            lin += [f"- unidad: {f['tipo_unidad']}; páginas {f['paginas']}; estado en E3 `{f['estado_e3']}`; en la cola: "
                    f"{'sí' if f['unidad_en_la_cola'] else 'no'}; crudo que entra a E2: {f['crudo_que_entra_a_e2']}",
                    f"- relación rechazada: índice {rr['indice_en_el_crudo']} del crudo, `{rr['source']}` `{rr['predicate']}` "
                    f"`{rr['target']}` (punto {rr['punto']}); validador de E1: {'; '.join(f['rechazo_en_validador_e1'])}; "
                    f"vista por E3: {'sí' if f['visto_por_e3'] else 'no'}"]
        for k, et in (("excepcion", "Excepcion"), ("operacion", "Operacion")):
            e = f[k]
            lin.append(f"- {et}{' `' + e['local_id'] + '`' if e['local_id'] else ''}: **{e['label']}** — {e['descripcion']} "
                       f"| tramo: {e['tramo']} | punto {e['punto']} | {'; '.join(e['donde_esta_el_tramo'])}")
        for h in f["texto_heredado_marcado"]:
            lin.append(f"- heredado, {h['bloque']}: {h['texto']}")
        lin.append(f"- texto propio{' (' + f['nota_texto'] + ')' if f.get('nota_texto') else ''}:")
        lin += ["", "```", f["texto_propio_marcado"], "```", ""]
    open(os.path.join(OUT, "fichas_41_exceptua_operacion.md"), "w", encoding="utf-8").write("\n".join(lin))
    print(len(fichas), sum(1 for f in fichas if f["visto_por_e3"]), sum(1 for f in fichas if f["unidad_en_la_cola"]))


if __name__ == "__main__":
    main()
