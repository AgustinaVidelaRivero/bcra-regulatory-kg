"""Mesa, §139 y §140 (17/10/2026), U-MED-DESAMB, parte 4: el sorteo sellado, el control de las normas y la planilla de la lectura de la
autora, sin modelo. Diseño firmado por la autora el 17/10/2026 (§140) y sellado antes del sorteo (diseno_sellado_med_desamb_2026-10-17.md).

Tres pasos, en este orden:
  sortear   las filas de resolucion_sujetos.jsonl ordenadas por (to, chunk_id, indice_relacion, predicado); por estrato,
            random.Random(f"{semilla}:{estrato}").sample(filas, n), o censo si el estrato tiene n o menos (declarado):
              - la lectura: E4 26, E6 16; el control, fijo: E1 4, E3 3, E5 3;
              - los calibradores: 12 de E1 a E9, sin las filas de la lectura (estrato «calibracion»);
              - la muestra del juez: 50 por estrato de E1 a E6 y censo de E7, E8 y E9, sin los calibradores (estrato «juez:Eh»).
            Escribe la lista (solo claves, sin texto) y su sello: sha256, hora, semilla y el sha256 de cada entrada.
  normas    para cada fila de la lectura y de la calibración, la norma por el registro validado del runner (la relación de igual
            indice_crudo y predicado). Si alguna no se encuentra, o no es única, FRENO: no hay planilla.
  planilla  controla el sello y el control de normas, y arma la planilla con los 64 ítems mezclados en un orden sorteado
            («{semilla}:orden»): planilla_lectura.md (un ítem por sección), hoja_clases.csv (una fila por entrada, para cargar la clase) y
            planilla_lectura.json; sin la vía ni el estrato. En E4 van las dos entradas, la del modelo y la de la regla, en orden sorteado
            («{semilla}:entradas:{ítem}») y sin decir cuál es cuál. La clave va en un archivo aparte.
Nada de E3: no copia estado_e3 ni lee archivos de reintentos o de veredictos.

Uso:
  python3 -I -B planilla_desamb_mesa.py sortear --resolucion <jsonl> --semilla <s> --salida <dir>
  python3 -I -B planilla_desamb_mesa.py normas --lista <dir> --lista-resolucion <jsonl> --salida-runner <dir salida_r2b>
  python3 -I -B planilla_desamb_mesa.py planilla --lista <dir> --lista-resolucion <jsonl> --e0 <dir chunks_<to>.json>
        --salida-runner <dir salida_r2b> --catalogo <catalogo_sujetos_r2.json> --rol-por-to <rol_por_to_r2.json> --salida <dir>"""
import argparse
import csv
import hashlib
import io
import json
import random
import sys
import time
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "parte2"))
import tamanos_desamb_mesa as T  # noqa: E402  (la función de estratos es una sola, la de la parte 2)

ORDEN = ("to", "chunk_id", "indice_relacion", "predicado")
LECTURA = {"E4": 26, "E6": 16, "E1": 4, "E3": 3, "E5": 3}     # firmado el 17/10/2026 (§140): E4, E6 y el control fijo
CALIBRACION = 12
JUEZ_POR_ESTRATO = 50
ESTRATOS_SUJETOS = ("E1", "E2", "E3", "E4", "E5", "E6", "E7", "E8", "E9")
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731
clave_fila = lambda r: tuple(r[k] for k in ORDEN)  # noqa: E731


def _sk(t):
    return tuple("" if x is None else (f"{x:09d}" if isinstance(x, int) else str(x)) for x in t)


def _filas(p):
    fs = [json.loads(l) for l in open(p, encoding="utf-8") if l.strip()]
    fs.sort(key=lambda r: _sk(clave_fila(r)))
    return fs


def sortear(a):
    filas = _filas(a.resolucion)
    por = {}
    for r in filas:
        por.setdefault(T.estrato(r), []).append(r)
    lista, usados, decl = [], set(), {}

    def tomar(nombre, pool, n, grupo, marcar=True):
        pool = [r for r in pool if not (marcar and clave_fila(r) in usados)]
        n_ef = min(n, len(pool))
        decl[nombre] = {"grupo": grupo, "N": len(pool), "n_pedido": n, "n": n_ef, "censo": len(pool) <= n}
        elegidas = random.Random(f"{a.semilla}:{nombre}").sample(pool, n_ef) if n_ef < len(pool) else list(pool)
        for r in elegidas:
            if marcar:
                usados.add(clave_fila(r))
            lista.append({"grupo": grupo, "estrato": nombre, "estrato_de_la_fila": T.estrato(r), "clave": list(clave_fila(r))})
    for e, n in LECTURA.items():
        tomar(e, por.get(e, []), n, "lectura")
    tomar("calibracion", [r for e in ESTRATOS_SUJETOS for r in por.get(e, [])], CALIBRACION, "calibracion")
    calib = {tuple(x["clave"]) for x in lista if x["grupo"] == "calibracion"}
    for e in ESTRATOS_SUJETOS:      # la muestra del juez: independiente de la lectura, sin los calibradores
        tomar(f"juez:{e}", [r for r in por.get(e, []) if clave_fila(r) not in calib], JUEZ_POR_ESTRATO, "juez", marcar=False)
    S = Path(a.salida)
    S.mkdir(parents=True, exist_ok=True)
    cuerpo = json.dumps({"semilla": a.semilla, "orden_de_las_filas": ORDEN, "declarado": decl, "lista": lista}, ensure_ascii=False, indent=1) + "\n"
    (S / "lista_muestra.json").write_text(cuerpo, encoding="utf-8")
    sello = {"lista_muestra_sha256": sha(cuerpo.encode("utf-8")), "sellado": time.strftime("%Y-%m-%d %H:%M:%S %z"),
             "semilla": a.semilla, "entradas_sha256": {"resolucion": sha(Path(a.resolucion).read_bytes())},
             "codigo_sha256": {"planilla_desamb_mesa.py": sha(Path(__file__).read_bytes()),
                               "tamanos_desamb_mesa.py": sha((AQUI.parent / "parte2" / "tamanos_desamb_mesa.py").read_bytes())}}
    (S / "sello_muestra.json").write_text(json.dumps(sello, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("sorteo:", {k: (v["n"], v["N"], "censo" if v["censo"] else "muestra") for k, v in decl.items()}, "| sello",
          sello["lista_muestra_sha256"][:16], sello["sellado"])


def _lista_sellada(a):
    L = Path(a.lista)
    cuerpo = (L / "lista_muestra.json").read_bytes()
    sello = json.loads((L / "sello_muestra.json").read_text(encoding="utf-8"))
    if sha(cuerpo) != sello["lista_muestra_sha256"]:
        raise SystemExit("FRENO: la lista no es la sellada")
    if sha(Path(a.lista_resolucion).read_bytes()) != sello["entradas_sha256"]["resolucion"]:
        raise SystemExit("FRENO: el registro de resolución no es el del sorteo")
    filas = {clave_fila(r): r for r in _filas(a.lista_resolucion)}
    return json.loads(cuerpo), sello, filas


def _finales(salida_runner):
    out = {}
    for f in sorted(Path(salida_runner).glob("*/extracciones_finales_r2_*.jsonl")):
        for l in open(f, encoding="utf-8"):
            if l.strip():
                d = json.loads(l)
                out[d["chunk_id"]] = d.get("validacion") or {}     # solo la validación; estado_e3 no se copia
    return out


def _norma(fila, finales):
    v = finales.get(fila["chunk_id"])
    if v is None:
        return {"estado": "sin_registro_del_chunk"}
    ents = {e["local_id"]: e for e in v.get("entidades", [])}
    rels = [r for r in v.get("relaciones", []) if r.get("indice_crudo") == fila["indice_relacion"] and r.get("predicate") == fila["predicado"]]
    if len(rels) != 1:
        return {"estado": "relacion_no_unica" if rels else "relacion_no_encontrada", "candidatas": len(rels)}
    r = rels[0]
    e = ents.get(r["source"] if r["predicate"] == "aplica_a" else r["target"])
    if not e:
        return {"estado": "entidad_no_encontrada"}
    p = e.get("properties") or {}
    return {"estado": "ok", "tipo": e.get("type"), "etiqueta": e.get("label"), "descripcion": p.get("descripcion"),
            "mencion_del_registro": r.get("sujeto_mencion")}


def normas(a):
    lst, sello, filas = _lista_sellada(a)
    finales = _finales(a.salida_runner)
    items = [x for x in lst["lista"] if x["grupo"] in ("lectura", "calibracion")]
    res, problemas, menciones = [], [], 0
    for x in items:
        n = _norma(filas[tuple(x["clave"])], finales)
        res.append({"clave": x["clave"], "estado": n["estado"]})
        if n["estado"] != "ok":
            problemas.append({"clave": x["clave"], **n})
        elif n["mencion_del_registro"] != filas[tuple(x["clave"])]["mencion"]:
            menciones += 1
    ok = not problemas
    out = {"lista_muestra_sha256": sello["lista_muestra_sha256"], "items": len(items), "ok": ok, "problemas": problemas,
           "menciones_distintas_entre_el_registro_y_la_resolucion": menciones,
           "nota": "la planilla toma la mención de la fila de resolución; del registro validado, solo la norma"}
    Path(a.lista, "control_normas.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"control de normas: {len(items)} ítems, {len(problemas)} con problema, {menciones} menciones distintas → {'OK' if ok else 'FRENO'}")
    if not ok:
        raise SystemExit("FRENO: hay normas sin encontrar o no únicas; no se arma la planilla")


def _chunks(e0, salida_runner):
    out = {}
    for f in sorted(Path(e0).glob("chunks_*.json")):
        d = json.loads(f.read_text(encoding="utf-8"))
        for c in (d["chunks"] if isinstance(d, dict) else d):
            out[c["id"]] = c
    for f in sorted(Path(salida_runner).glob("*/particiones_por_corte.json")):
        for unidad in json.loads(f.read_text(encoding="utf-8")).values():
            for c in unidad.get("partes", []):
                out[c["id"]] = c
    return out


def _entradas(catalogo, rol_por_to):
    cat = {s["id"]: s for s in json.loads(Path(catalogo).read_text(encoding="utf-8"))["sujetos"]}
    roles = {}
    rp = json.loads(Path(rol_por_to).read_text(encoding="utf-8"))
    for v in (rp.values() if isinstance(rp, dict) else rp):
        if isinstance(v, dict) and v.get("rol_id"):
            roles.setdefault(v["rol_id"], v)

    def ficha(i):
        if i in cat:
            s = cat[i]
            return {"id": i, "etiqueta": s.get("label"), "alias": s.get("alias") or [], "definicion": s.get("definicion"), "padre": s.get("padre")}
        if i in roles:
            r = roles[i]
            return {"id": i, "etiqueta": r.get("label"), "alias": [], "definicion": "rol de alcance del documento; miembros: "
                    + ", ".join(r.get("miembros_labels") or []), "padre": None}
        return {"id": i, "etiqueta": None, "alias": [], "definicion": None, "padre": None, "fuera_del_catalogo": True}
    return ficha


def _cita(t):
    return "\n".join("> " + (l if l.strip() else "") for l in (t or "").split("\n")) if t else "> (vacío)"


def _md(h):
    out = [f"## {h['item']}", "",
           f"- **Documento:** {h['documento']} · **Punto:** {h['punto']} · **Relación:** {h['predicado']}",
           f"- **Mención del sujeto:** «{h['mencion']}»",
           f"- **Norma:** {h['norma']['tipo']}: {h['norma']['etiqueta']}", "", _cita(h["norma"].get("descripcion")), "",
           "**Texto propio de la unidad:**", "", _cita(h["texto"]["propio"]), ""]
    if h["texto"]["heredado"]:
        out += ["**Texto heredado:**", ""]
        for x in h["texto"]["heredado"]:
            out += [f"*{x['unidad']}*", "", _cita(x["texto"]), ""]
    out += ["**Entradas a clasificar:**", ""]
    for e in h["entradas"]:
        alias = ", ".join(e["alias"]) if e["alias"] else "sin alias"
        out.append(f"- **{e['letra']}.** `{e['id']}`: {e['etiqueta']} ({alias}). Definición: {e['definicion'] or 'sin definición'}. "
                   f"Padre: {e['padre'] or 'sin padre'}.")
    return "\n".join(out) + "\n"


def planilla(a):
    lst, sello, filas = _lista_sellada(a)
    pc = Path(a.lista, "control_normas.json")
    if not pc.exists():
        raise SystemExit("FRENO: falta el control de normas; se corre antes de la planilla")
    ctl = json.loads(pc.read_text(encoding="utf-8"))
    if not ctl.get("ok") or ctl.get("lista_muestra_sha256") != sello["lista_muestra_sha256"]:
        raise SystemExit("FRENO: el control de normas no está en OK para esta lista")
    semilla = lst["semilla"]
    chunks = _chunks(a.e0, a.salida_runner)
    finales = _finales(a.salida_runner)
    ficha = _entradas(a.catalogo, a.rol_por_to)
    items = [x for x in lst["lista"] if x["grupo"] in ("lectura", "calibracion")]
    random.Random(f"{semilla}:orden").shuffle(items)
    hojas, clave = [], []
    for k, x in enumerate(items, 1):
        iid = f"D{k:03d}"
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
        n = _norma(r, finales)
        hojas.append({"item": iid, "documento": r["to"], "punto": r["punto"], "predicado": r["predicado"], "mencion": r["mencion"],
                      "norma": {k2: n.get(k2) for k2 in ("tipo", "etiqueta", "descripcion")}, "texto": texto,
                      "entradas": [dict(ficha(i), letra=chr(65 + j)) for j, (i, _) in enumerate(par)]})
        clave.append({"item": iid, "grupo": x["grupo"], "estrato_del_sorteo": x["estrato"], "estrato_de_la_fila": est,
                      "clave_de_la_fila": x["clave"], "metodo_resolucion": r["metodo_resolucion"], "regla_texto": r["regla_texto"],
                      "entradas": [{"letra": chr(65 + j), "id": i, "de": q} for j, (i, q) in enumerate(par)]})
    S = Path(a.salida)
    S.mkdir(parents=True, exist_ok=True)
    cab = ("# Planilla de lectura de U-MED-DESAMB\n\n"
           f"Sello de la lista: `{sello['lista_muestra_sha256']}` ({sello['sellado']}). {len(hojas)} ítems en orden sorteado: 52 de la lectura "
           "y 12 calibradores, mezclados. La clase de cada entrada va en `hoja_clases.csv`.\n\n"
           "**Criterio (firmado el 17/10/2026):**\n"
           "- **correcta:** en esa norma, el texto se refiere a ese sujeto, con ese alcance y en ese papel;\n"
           "- **genérica:** el texto nombra un sujeto más específico que está en el catálogo debajo de la entrada;\n"
           "- **incorrecta:** es otro sujeto, la entrada es más específica que lo que dice el texto, o el sujeto no cumple ese papel en la norma;\n"
           "- **no decidible:** el texto, con su herencia, no lo identifica.\n\n"
           "En la hoja, la columna `clase` lleva una de: `correcta`, `generica`, `incorrecta`, `no_decidible`.\n\n")
    md = cab + "\n".join(_md(h) for h in hojas)
    (S / "planilla_lectura.md").write_text(md, encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["item", "letra", "entrada_id", "etiqueta", "clase", "nota"])
    for h in hojas:
        for e in h["entradas"]:
            w.writerow([h["item"], e["letra"], e["id"], e["etiqueta"] or "", "", ""])
    (S / "hoja_clases.csv").write_text(buf.getvalue(), encoding="utf-8")
    pl = json.dumps({"sello_de_la_lista": sello["lista_muestra_sha256"], "items": hojas}, ensure_ascii=False, indent=1) + "\n"
    (S / "planilla_lectura.json").write_text(pl, encoding="utf-8")
    (S / "CLAVE_aparte_no_abrir_antes_de_cerrar_la_lectura.json").write_text(json.dumps(clave, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    faltan = sum(1 for h in hojas if h["texto"]["falta"])
    print(f"planilla: {len(hojas)} ítems | entradas {sum(len(h['entradas']) for h in hojas)} | sin texto de E0: {faltan} | "
          f"md {sha(md.encode('utf-8'))[:16]} | csv {sha(buf.getvalue().encode('utf-8'))[:16]}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    s = sub.add_parser("sortear")
    s.add_argument("--resolucion", required=True)
    s.add_argument("--semilla", required=True)
    s.add_argument("--salida", required=True)
    n = sub.add_parser("normas")
    n.add_argument("--lista", required=True)
    n.add_argument("--lista-resolucion", required=True)
    n.add_argument("--salida-runner", required=True)
    p = sub.add_parser("planilla")
    p.add_argument("--lista", required=True)
    p.add_argument("--lista-resolucion", required=True)
    p.add_argument("--e0", required=True)
    p.add_argument("--salida-runner", required=True)
    p.add_argument("--catalogo", required=True)
    p.add_argument("--rol-por-to", required=True)
    p.add_argument("--salida", required=True)
    a = ap.parse_args()
    {"sortear": sortear, "normas": normas, "planilla": planilla}[a.cmd](a)


if __name__ == "__main__":
    main()
