#!/usr/bin/env python3
"""aplicar_lectura_tolerante_n6.py — La lectura tolerante (lectura_tolerante_juez.py) sobre las salidas del juez de N6 que no se
leen como JSON, con su prueba (decisión de la autora del 27/10/2026, recibida a las 23:26:23, puntos 1 y 2; mesa, §312). USD 0: no
llama a ningún modelo. Lee la salida de N6 sin escribir en ella (las cachés del juez, en solo lectura) y no abre
desanonimizacion_SOLO_MESA/ ni el archivo de preguntas de N3.

Cada repetición del juez de N6 corrió una sola vez, en el orden ciego de juez/orden_juez_n6.json, y cada respuesta llamó a sus 3
repeticiones seguidas (correr_n6.py, correr_juez). Por eso la fila k de la caché de la repetición r, en el orden en que se
guardaron, es la llamada de la respuesta k del orden ciego. La prueba lo controla contra lo que el corredor registró.

La prueba (P1 a P8), toda tiene que dar; si no, sale con 1 y no escribe nada fuera de su informe:
  P1 el orden: 418 ids opacos distintos; en cada caché, 418 filas en orden de guardado, con la hora creciente, el espacio de nombres
     del juez de EV2 de esa repetición y `end_turn`;
  P2 la correspondencia: cada fila que la lectura estricta (`juez.parsear_veredicto`) lee da el veredicto registrado de su id en
     veredictos_r{r}.jsonl, con sus tokens; cada fila que no lee da el error registrado de su id en errores_r{r}.jsonl, con el mismo
     texto; cada renglón registrado se usa una vez;
  P3 los criterios: N, el del pedido («CRITERIOS (N):»), es el de los veredictos registrados de ese id, y el mismo en las 3 cachés;
  P4 las 1.202 lecturas: en cada salida que la estricta lee, la tolerante da lo mismo;
  P5 las 52: la lectura tolerante aplica justo a las salidas que la estricta rechaza por JSON, y en cada una da un veredicto por
     criterio, con los N índices en orden y una clasificación;
  P6 los 394 agregados: correr_n6.agregar, sin editarlo, sobre los veredictos registrados, reproduce byte a byte
     juez/agregados_n6_ciego.json;
  P7 con las 52: los agregados juntan las 418 respuestas, sin ninguna incompleta, y los 394 de antes quedan iguales;
  P8 en contra: la lectura tolerante rechaza seis salidas armadas a mano (un índice de menos, uno fuera de orden, un veredicto fuera
     del dominio, uno separado de su índice, dos clasificaciones y un índice de más dentro de un fragmento) y lee bien dos.

Escribe (con --salida <dir>, que no puede existir): <dir>/juez_con_lectura_tolerante/ con los veredictos_r{1,2,3}.jsonl de N6 más
los de la lectura tolerante, marcados, y su agregados_n6_ciego.json de 418; <dir>/veredictos_lectura_tolerante_n6.jsonl, solo los
52; y <dir>/informe_lectura_tolerante_n6.json. Sin --salida, solo corre la prueba y escribe el informe en --informe.
Imprime solo cuentas y sha256: ningún veredicto, pregunta, criterio ni respuesta.

  python -B aplicar_lectura_tolerante_n6.py --salida-n6 <banco_n6> [--clon <carpeta n6 de una copia de HEAD>]
      (--informe <json> | --salida <dir>)
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sqlite3
import sys
import tempfile
from collections import Counter
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPS = (1, 2, 3)
N_CRITERIOS = re.compile(r"\n\nCRITERIOS \((\d+)\):\n")


def sha(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def lj(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()]


def texto_de(raw: str) -> str:
    return "".join(b.get("text", "") for b in json.loads(raw).get("content", []) if b.get("type") == "text")


def filas_cache(db: Path) -> list[dict]:
    con = sqlite3.connect(f"file:{db}?mode=ro&immutable=1", uri=True)
    try:
        rs = con.execute("SELECT rowid, created_at, namespace, stop_reason, input_tokens, output_tokens, model, request_json, "
                         "raw_json FROM cache ORDER BY rowid").fetchall()
    finally:
        con.close()
    out = []
    for rowid, ca, ns, stop, it, ot, model, req, raw in rs:
        m = N_CRITERIOS.search(json.loads(req)["messages"][0]["content"])
        out.append({"rowid": rowid, "creado": datetime.fromisoformat(ca), "namespace": ns, "stop": stop, "input_tokens": it,
                    "output_tokens": ot, "modelo": model, "n": int(m.group(1)) if m else None, "texto": texto_de(raw)})
    return out


def pruebas_en_contra(LT) -> dict:
    def sal(crits, cl='"clasificacion_respuesta": "contenido", '):
        return "{" + cl + '"criterios": [' + ", ".join(crits) + "]}"
    c = lambda k, v, frag="null": f'{{"indice": {k}, "veredicto": "{v}", "fragmento": {frag}, "justificacion": "x"}}'  # noqa: E731
    malas = {
        "un índice de menos": (sal([c(1, "cumplido")]), 2),
        "un índice fuera de orden": (sal([c(2, "cumplido"), c(1, "dudoso")]), 2),
        "un veredicto fuera del dominio": (sal([c(1, "cumplido"), c(2, "parcial")]), 2),
        "un veredicto separado de su índice": (sal(['{"indice": 1, "fragmento": null, "veredicto": "cumplido"}']), 1),
        "dos clasificaciones": (sal([c(1, "cumplido")], cl='"clasificacion_respuesta": "contenido", '
                                    '"clasificacion_respuesta": "abstencion", '), 1),
        "un índice de más dentro de un fragmento": (sal([c(1, "cumplido", '"dice "indice": 2, sin escapar"'), c(2, "dudoso")]), 2),
    }
    out = {}
    for k, (t, n) in malas.items():
        try:
            LT.leer(t, n)
            out[k] = "la leyó (mal)"
        except ValueError:
            out[k] = "la rechaza"
    buenas = {"con comillas sin escapar en el fragmento": (sal([c(1, "cumplido", '"dice "tal cosa" en el punto"'),
                                                                 c(2, "no_cumplido")]), 2, ["cumplido", "no_cumplido"]),
              "con la clave del veredicto repetida": (sal(['{"indice": 1, "veredicto": "dudoso", "fragmento": null, '
                                                           '"veredicto": "cumplido", "justificacion": "x"}']), 1, ["cumplido"])}
    for k, (t, n, esp) in buenas.items():
        try:
            r = LT.leer(t, n)
            out[k] = "la lee bien" if [x["veredicto"] for x in r["criterios"]] == esp else "la lee mal"
        except ValueError:
            out[k] = "la rechaza (mal)"
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida-n6", type=Path, required=True)
    ap.add_argument("--clon", type=Path, default=AQUI, help="la carpeta banco_mcp/n6 de donde se importan correr_n6 y el juez")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--informe", type=Path)
    g.add_argument("--salida", type=Path)
    a = ap.parse_args(argv)
    for p in (str(AQUI), str(AQUI.parent), str(a.clon.resolve())):
        if p not in sys.path:
            sys.path.insert(0, p)
    import correr_n6 as CN                      # noqa: PLC0415  (solo import: agregar, el juez de EV2)
    import lectura_tolerante_juez as LT         # noqa: PLC0415
    J = CN.J
    if a.salida is not None and a.salida.exists():
        raise SystemExit("ABORTO: --salida ya existe")
    N6 = a.salida_n6.resolve()
    JD = N6 / "juez"
    ids = json.loads((JD / "orden_juez_n6.json").read_text(encoding="utf-8"))["ids_opacos_en_orden"]
    ver = {r: lj(JD / f"veredictos_r{r}.jsonl") for r in REPS}
    err = {r: lj(JD / f"errores_r{r}.jsonl") for r in REPS}
    filas = {r: filas_cache(JD / "cache" / f"n6_juez_r{r}.db") for r in REPS}
    P, falla = {}, []

    # P1
    ns_esperado = {r: CN.J.lc.make_namespace(f"juez_ev2_r{r}", code_ver=J.CODE_VER, thinking=False) for r in REPS}
    p1 = {"ids": len(ids), "ids_distintos": len(set(ids))}
    for r in REPS:
        fs = filas[r]
        p1[f"r{r}"] = {"filas": len(fs), "hora_creciente": all(x["creado"] < y["creado"] for x, y in zip(fs, fs[1:])),
                       "espacio_de_nombres": all(x["namespace"] == ns_esperado[r] for x in fs),
                       "end_turn": sum(x["stop"] == "end_turn" for x in fs)}
    P["P1"] = p1
    if len(ids) != 418 or len(set(ids)) != 418 or any(p1[f"r{r}"] != {"filas": 418, "hora_creciente": True,
                                                                      "espacio_de_nombres": True, "end_turn": 418} for r in REPS):
        falla.append("P1")

    # P2, P3, P4 y P5
    n_de, rescate, usados_v, usados_e = {}, [], Counter(), Counter()
    p2 = {"veredictos_iguales": 0, "errores_iguales": 0, "distintos": 0}
    p4 = {"iguales": 0, "distintas": 0}
    p5 = {"aplica_en_las_rechazadas_por_json": 0, "aplica_en_otras": 0, "leidas": 0, "no_leidas": 0,
          "criterios_con_mas_de_un_veredicto": 0}
    v_por = {r: {x["id_opaco"]: x for x in ver[r]} for r in REPS}
    e_por = {r: {x["id_opaco"]: x for x in err[r]} for r in REPS}
    for r in REPS:
        for k, f in enumerate(filas[r]):
            i = ids[k] if k < len(ids) else None
            n_de.setdefault(i, set()).add(f["n"])
            try:
                estricta = J.parsear_veredicto(f["texto"], f["n"])
            except ValueError as x:
                estricta, error = None, str(x)
            if estricta is not None:
                reg = v_por[r].get(i)
                ok = (reg is not None and reg["clasificacion_respuesta"] == estricta["clasificacion_respuesta"]
                      and reg["criterios"] == estricta["criterios"] and reg["meta"]["input_tokens"] == f["input_tokens"]
                      and reg["meta"]["output_tokens"] == f["output_tokens"])
                p2["veredictos_iguales" if ok else "distintos"] += 1
                usados_v[(r, i)] += 1
                try:
                    p4["iguales" if LT.igual_a_la_estricta(LT.leer(f["texto"], f["n"]), estricta) else "distintas"] += 1
                except ValueError:
                    p4["distintas"] += 1
                p5["aplica_en_otras"] += LT.aplica(f["texto"], f["stop"])
                continue
            reg = e_por[r].get(i)
            ok = reg is not None and reg["error"] == error
            p2["errores_iguales" if ok else "distintos"] += 1
            usados_e[(r, i)] += 1
            por_json = LT.aplica(f["texto"], f["stop"])
            if not por_json:
                p5["no_leidas"] += 1
                continue
            try:
                t = LT.leer(f["texto"], f["n"])
            except ValueError:
                p5["no_leidas"] += 1
                continue
            p5["aplica_en_las_rechazadas_por_json"] += 1
            p5["leidas"] += 1
            p5["criterios_con_mas_de_un_veredicto"] += sum(c["veredictos_en_el_criterio"] > 1 for c in t["criterios"])
            rescate.append({"id_opaco": i, "rep": r, "clasificacion_respuesta": t["clasificacion_respuesta"],
                            "criterios": [{"indice": c["indice"], "veredicto": c["veredicto"]} for c in t["criterios"]],
                            "meta": {"modelo": f["modelo"], "stop_reason": f["stop"], "input_tokens": f["input_tokens"],
                                     "output_tokens": f["output_tokens"], "fila_de_la_cache": f["rowid"]},
                            "lectura": "tolerante", "lectura_sha256": sha(Path(LT.__file__)),
                            "error_de_la_estricta": error})
    p2["renglones_registrados"] = sum(len(v) for v in ver.values()) + sum(len(v) for v in err.values())
    p2["renglones_usados_una_vez"] = sum(1 for v in usados_v.values() if v == 1) + sum(1 for v in usados_e.values() if v == 1)
    P["P2"] = p2
    if p2["distintos"] or p2["renglones_usados_una_vez"] != p2["renglones_registrados"] \
            or p2["veredictos_iguales"] + p2["errores_iguales"] != 3 * 418:
        falla.append("P2")
    reg_n = {i: len(x["criterios"]) for r in REPS for i, x in v_por[r].items()}
    p3 = {"ids_con_un_solo_N": sum(1 for v in n_de.values() if len(v) == 1 and None not in v),
          "N_igual_al_registrado": sum(1 for i, nn in reg_n.items() if n_de.get(i) == {nn}), "ids_con_veredicto": len(reg_n)}
    P["P3"] = p3
    if p3["ids_con_un_solo_N"] != 418 or p3["N_igual_al_registrado"] != p3["ids_con_veredicto"]:
        falla.append("P3")
    P["P4"] = p4
    if p4["distintas"] or p4["iguales"] != sum(len(v) for v in ver.values()):
        falla.append("P4")
    P["P5"] = p5
    if p5["aplica_en_otras"] or p5["no_leidas"] or p5["leidas"] != sum(len(v) for v in err.values()) \
            or p5["aplica_en_las_rechazadas_por_json"] != p5["leidas"]:
        falla.append("P5")

    # P6 y P7
    n_por_id = {i: next(iter(v)) for i, v in n_de.items()}
    casos = [{"id_opaco": i, "criterios": [None] * n_por_id[i]} for i in ids]
    original = (JD / "agregados_n6_ciego.json").read_bytes()
    rehecho = (json.dumps(CN.agregar(JD, casos), ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    P["P6"] = {"reproduce_byte_a_byte": rehecho == original, "sha256_original": hashlib.sha256(original).hexdigest()}
    if rehecho != original:
        falla.append("P6")
    with tempfile.TemporaryDirectory() as td:
        tj = Path(td)
        for r in REPS:
            lineas = (JD / f"veredictos_r{r}.jsonl").read_text(encoding="utf-8")
            extra = "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in rescate if x["rep"] == r)
            (tj / f"veredictos_r{r}.jsonl").write_text(lineas + extra, encoding="utf-8")
        agg52 = CN.agregar(tj, casos)
        textos52 = {r: (tj / f"veredictos_r{r}.jsonl").read_text(encoding="utf-8") for r in REPS}
    antes = {x["id_opaco"]: x for x in json.loads(original)["agregados"]}
    despues = {x["id_opaco"]: x for x in agg52["agregados"]}
    P["P7"] = {"n_agregados": agg52["n_agregados"], "incompletas": len(agg52["incompletas"]),
               "los_394_iguales": sum(1 for i, x in antes.items() if despues.get(i) == x), "antes": len(antes)}
    if agg52["n_agregados"] != 418 or agg52["incompletas"] or P["P7"]["los_394_iguales"] != len(antes):
        falla.append("P7")

    # P8
    P["P8"] = pruebas_en_contra(LT)
    if any(v not in ("la rechaza", "la lee bien") for v in P["P8"].values()) or len(P["P8"]) != 8:
        falla.append("P8")

    informe = {"unidad": "N6: la lectura tolerante de las salidas del juez que no se leen como JSON (opción B, 27/10/2026)",
               "codigo": {"lectura_tolerante_juez.py": sha(Path(LT.__file__)), Path(__file__).name: sha(Path(__file__))},
               "juez": {"code_ver": J.CODE_VER, "prompt_sha256": J.PROMPT_SHA256, "modelo": J.MODELO},
               "entradas": {**{f"juez/{n}": sha(JD / n) for n in ["orden_juez_n6.json", "agregados_n6_ciego.json"]
                               + [f"veredictos_r{r}.jsonl" for r in REPS] + [f"errores_r{r}.jsonl" for r in REPS]},
                            **{f"juez/cache/n6_juez_r{r}.db": sha(JD / "cache" / f"n6_juez_r{r}.db") for r in REPS}},
               "prueba": P, "prueba_da": not falla, "fallan": falla,
               "las_52": sorted([x["id_opaco"], x["rep"]] for x in rescate)}
    if a.salida is not None and not falla:
        sal = a.salida
        (sal / "juez_con_lectura_tolerante").mkdir(parents=True)
        for r in REPS:
            (sal / "juez_con_lectura_tolerante" / f"veredictos_r{r}.jsonl").write_text(textos52[r], encoding="utf-8")
        (sal / "juez_con_lectura_tolerante" / "agregados_n6_ciego.json").write_text(
            json.dumps(agg52, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (sal / "veredictos_lectura_tolerante_n6.jsonl").write_text(
            "".join(json.dumps(x, ensure_ascii=False) + "\n" for x in rescate), encoding="utf-8")
        informe["salidas"] = {str(p.relative_to(sal)): sha(p) for p in sorted(sal.rglob("*")) if p.is_file()}
        destino = sal / "informe_lectura_tolerante_n6.json"
    else:
        destino = a.informe if a.informe is not None else None
    if destino is not None:
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(json.dumps(informe, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"prueba": P, "prueba_da": not falla, "fallan": falla}, ensure_ascii=False, indent=1))
    if destino is not None:
        print(f"informe: {destino.name} ({sha(destino)})")
    return 0 if not falla else 1


if __name__ == "__main__":
    raise SystemExit(main())
