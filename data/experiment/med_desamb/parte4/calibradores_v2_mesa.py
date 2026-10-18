"""Mesa, §141 (17/10/2026), U-MED-DESAMB: los calibradores nuevos del juez (nota 1 al diseño sellado, decisión de la autora del 17/10/2026,
recibida a las 12:29:34). Usa como biblioteca el código sellado de la planilla (planilla_desamb_mesa.py), sin cambiarlo.

Tres pasos, en este orden:
  sortear   controla la lista sellada del sorteo (sha256 contra su sello) y, por estrato, en este orden E4, E6 y E2,
            random.Random(f"{semilla}:calibracion2:{estrato}").sample(filas, n) con n = 5, 5 y 2, sobre las filas del estrato ordenadas por
            (to, chunk_id, indice_relacion, predicado) y sin las de la lectura de la autora ni las de la muestra del juez. Escribe la lista
            (solo claves) y su sello antes de armar nada.
  normas    la norma de cada calibrador por el registro validado del runner; si alguna no aparece o no es única, FRENO.
  planilla  la planilla aparte de los calibradores, que dice que son calibradores, en el orden de
            random.Random(f"{semilla}:calibracion2:orden").shuffle, numerados K01 a K12. En E4 van las dos entradas en el orden de
            random.Random(f"{semilla}:entradas:{ítem}").shuffle, sin decir cuál es del modelo y cuál de la regla. No dice el estrato. La
            hoja lleva la columna «nota», para la línea con el porqué de cada clase. La clave va en un archivo aparte.

Uso:
  python3 -I -B calibradores_v2_mesa.py sortear --lista <lista_muestra.json> --sello <sello_muestra.json> --resolucion <jsonl>
        --semilla <s> --salida <dir>
  python3 -I -B calibradores_v2_mesa.py normas --salida <dir del sorteo> --resolucion <jsonl> --salida-runner <dir salida_r2b>
  python3 -I -B calibradores_v2_mesa.py planilla --salida <dir del sorteo> --resolucion <jsonl> --e0 <dir> --salida-runner <dir>
        --catalogo <json> --rol-por-to <json> --planilla <dir> --clave <dir>"""
import argparse
import csv
import io
import json
import random
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import planilla_desamb_mesa as PL  # noqa: E402  (código sellado, como biblioteca)

T = PL.T
CALIBRACION2 = (("E4", 5), ("E6", 5), ("E2", 2))
sha = PL.sha


def sortear(a):
    cuerpo = Path(a.lista).read_bytes()
    sello = json.loads(Path(a.sello).read_text(encoding="utf-8"))
    if sha(cuerpo) != sello["lista_muestra_sha256"]:
        raise SystemExit("FRENO: la lista del sorteo no es la sellada")
    if sha(Path(a.resolucion).read_bytes()) != sello["entradas_sha256"]["resolucion"]:
        raise SystemExit("FRENO: el registro de resolución no es el del sorteo")
    lst = json.loads(cuerpo)
    fuera = {tuple(x["clave"]) for x in lst["lista"] if x["grupo"] in ("lectura", "juez")}
    viejos = {tuple(x["clave"]) for x in lst["lista"] if x["grupo"] == "calibracion"}
    por = {}
    for r in PL._filas(a.resolucion):
        por.setdefault(T.estrato(r), []).append(r)
    lista, decl = [], {}
    for e, n in CALIBRACION2:
        pool = [r for r in por.get(e, []) if PL.clave_fila(r) not in fuera]
        nombre = f"calibracion2:{e}"
        elegidas = random.Random(f"{a.semilla}:{nombre}").sample(pool, n) if n < len(pool) else list(pool)
        decl[nombre] = {"N": len(pool), "n": len(elegidas), "censo": len(pool) <= n}
        lista += [{"grupo": "calibracion2", "estrato": nombre, "estrato_de_la_fila": e, "clave": list(PL.clave_fila(r))} for r in elegidas]
    S = Path(a.salida)
    S.mkdir(parents=True, exist_ok=True)
    cuerpo2 = json.dumps({"semilla": a.semilla, "orden_de_las_filas": PL.ORDEN, "declarado": decl, "lista": lista}, ensure_ascii=False, indent=1) + "\n"
    (S / "lista_calibradores_v2.json").write_text(cuerpo2, encoding="utf-8")
    coinciden = sum(1 for x in lista if tuple(x["clave"]) in viejos)
    sello2 = {"lista_calibradores_v2_sha256": sha(cuerpo2.encode("utf-8")), "sellado": time.strftime("%Y-%m-%d %H:%M:%S %z"), "semilla": a.semilla,
              "entradas_sha256": {"resolucion": sha(Path(a.resolucion).read_bytes()), "lista_muestra": sello["lista_muestra_sha256"]},
              "codigo_sha256": {"calibradores_v2_mesa.py": sha(Path(__file__).read_bytes()), "planilla_desamb_mesa.py": sha(Path(PL.__file__).read_bytes())},
              "calibradores_viejos_que_vuelven_a_salir": coinciden}
    (S / "sello_calibradores_v2.json").write_text(json.dumps(sello2, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("calibradores nuevos:", {k: (v["n"], v["N"]) for k, v in decl.items()}, "| viejos que vuelven a salir:", coinciden, "| sello",
          sello2["lista_calibradores_v2_sha256"][:16], sello2["sellado"])


def _lista2(a):
    S = Path(a.salida)
    cuerpo = (S / "lista_calibradores_v2.json").read_bytes()
    sello = json.loads((S / "sello_calibradores_v2.json").read_text(encoding="utf-8"))
    if sha(cuerpo) != sello["lista_calibradores_v2_sha256"]:
        raise SystemExit("FRENO: la lista de los calibradores no es la sellada")
    if sha(Path(a.resolucion).read_bytes()) != sello["entradas_sha256"]["resolucion"]:
        raise SystemExit("FRENO: el registro de resolución no es el del sorteo")
    return json.loads(cuerpo), sello, {PL.clave_fila(r): r for r in PL._filas(a.resolucion)}


def normas(a):
    lst, sello, filas = _lista2(a)
    finales = PL._finales(a.salida_runner)
    problemas = []
    for x in lst["lista"]:
        n = PL._norma(filas[tuple(x["clave"])], finales)
        if n["estado"] != "ok":
            problemas.append({"clave": x["clave"], **n})
    out = {"lista_calibradores_v2_sha256": sello["lista_calibradores_v2_sha256"], "items": len(lst["lista"]), "ok": not problemas, "problemas": problemas}
    (Path(a.salida) / "control_normas_calibradores_v2.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"control de normas de los calibradores: {len(lst['lista'])} ítems, {len(problemas)} con problema → {'OK' if not problemas else 'FRENO'}")
    if problemas:
        raise SystemExit("FRENO: hay normas sin encontrar o no únicas; no se arma la planilla de los calibradores")


def planilla(a):
    lst, sello, filas = _lista2(a)
    pc = Path(a.salida) / "control_normas_calibradores_v2.json"
    if not pc.exists() or not json.loads(pc.read_text(encoding="utf-8")).get("ok"):
        raise SystemExit("FRENO: el control de normas de los calibradores no está en OK")
    semilla = lst["semilla"]
    chunks, finales, ficha = PL._chunks(a.e0, a.salida_runner), PL._finales(a.salida_runner), PL._entradas(a.catalogo, a.rol_por_to)
    items = list(lst["lista"])
    random.Random(f"{semilla}:calibracion2:orden").shuffle(items)
    hojas, clave = [], []
    for k, x in enumerate(items, 1):
        iid = f"K{k:02d}"
        r = filas[tuple(x["clave"])]
        est = x["estrato_de_la_fila"]
        if est == "E4":
            par = [(r["sujeto_id_modelo"], "modelo"), (r["id_regla_texto"], "regla_texto")]
            random.Random(f"{semilla}:entradas:{iid}").shuffle(par)
        elif est in ("E5", "E6"):
            par = [(r["sujeto_id_modelo"], "modelo")]
        else:
            par = [(r["resuelto_a"], "resuelto")]
        c = chunks.get(r["chunk_id"])
        texto = {"propio": (c or {}).get("texto") or "", "heredado": [{"unidad": h.get("unidad_origen") or h.get("unidad"), "texto": h.get("texto") or ""}
                                                                    for h in (c or {}).get("herencia") or []], "falta": c is None}
        n = PL._norma(r, finales)
        hojas.append({"item": iid, "documento": r["to"], "punto": r["punto"], "predicado": r["predicado"], "mencion": r["mencion"],
                      "norma": {k2: n.get(k2) for k2 in ("tipo", "etiqueta", "descripcion")}, "texto": texto,
                      "entradas": [dict(ficha(i), letra=chr(65 + j)) for j, (i, _) in enumerate(par)]})
        clave.append({"item": iid, "grupo": "calibracion2", "estrato_de_la_fila": est, "clave_de_la_fila": x["clave"],
                      "metodo_resolucion": r["metodo_resolucion"], "regla_texto": r["regla_texto"],
                      "entradas": [{"letra": chr(65 + j), "id": i, "de": q} for j, (i, q) in enumerate(par)]})
    P, K = Path(a.planilla), Path(a.clave)
    P.mkdir(parents=True, exist_ok=True)
    K.mkdir(parents=True, exist_ok=True)
    cab = ("# Planilla de los calibradores del juez (U-MED-DESAMB)\n\n"
           f"Sello de la lista: `{sello['lista_calibradores_v2_sha256']}` ({sello['sellado']}). {len(hojas)} calibradores, en orden sorteado. "
           "Se leen solo si la lectura de las 52 termina antes del miércoles 21/10/2026 a las 18:00. La clase de cada entrada va en "
           "`hoja_calibradores.csv`, y en la columna `nota`, una línea con el porqué de esa clase.\n\n"
           "**Criterio (firmado el 17/10/2026):**\n"
           "- **correcta:** en esa norma, el texto se refiere a ese sujeto, con ese alcance y en ese papel;\n"
           "- **genérica:** el texto nombra un sujeto más específico que está en el catálogo debajo de la entrada;\n"
           "- **incorrecta:** es otro sujeto, la entrada es más específica que lo que dice el texto, o el sujeto no cumple ese papel en la norma;\n"
           "- **no decidible:** el texto, con su herencia, no lo identifica.\n\n"
           "En la hoja, la columna `clase` lleva una de: `correcta`, `generica`, `incorrecta`, `no_decidible`.\n\n")
    md = cab + "\n".join(PL._md(h) for h in hojas)
    (P / "planilla_calibradores.md").write_text(md, encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["item", "letra", "entrada_id", "etiqueta", "clase", "nota"])
    for h in hojas:
        for e in h["entradas"]:
            w.writerow([h["item"], e["letra"], e["id"], e["etiqueta"] or "", "", ""])
    (P / "hoja_calibradores.csv").write_text(buf.getvalue(), encoding="utf-8")
    pl = json.dumps({"sello_de_la_lista": sello["lista_calibradores_v2_sha256"], "items": hojas}, ensure_ascii=False, indent=1) + "\n"
    (P / "planilla_calibradores.json").write_text(pl, encoding="utf-8")
    (K / "CLAVE_calibradores_v2.json").write_text(json.dumps(clave, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"planilla de los calibradores: {len(hojas)} ítems | entradas {sum(len(h['entradas']) for h in hojas)} | sin texto de E0: "
          f"{sum(1 for h in hojas if h['texto']['falta'])} | md {sha(md.encode('utf-8'))[:16]} | csv {sha(buf.getvalue().encode('utf-8'))[:16]}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sortear")
    for k in ("--lista", "--sello", "--resolucion", "--semilla", "--salida"):
        s.add_argument(k, required=True)
    n = sub.add_parser("normas")
    for k in ("--salida", "--resolucion", "--salida-runner"):
        n.add_argument(k, required=True)
    p = sub.add_parser("planilla")
    for k in ("--salida", "--resolucion", "--e0", "--salida-runner", "--catalogo", "--rol-por-to", "--planilla", "--clave"):
        p.add_argument(k, required=True)
    a = ap.parse_args()
    {"sortear": sortear, "normas": normas, "planilla": planilla}[a.cmd](a)


if __name__ == "__main__":
    main()
