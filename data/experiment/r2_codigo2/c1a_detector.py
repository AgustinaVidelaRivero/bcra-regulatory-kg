"""U-R2-CODIGO-2, C1.a — detector de citas externas por patrón (USD 0, sin API ni Neo4j). Solo escribe --out.

Qué mide, sobre KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a (cadena r2 en memoria, `c1_comun`):
  1. Por qué cada una de las 18 filas «detector» de M3.b (`git show 4244028:…/m3b_lectura_puntos_inexistentes.csv`)
     quedó como cita interna: la rama de `detectar_menciones_r2` que la clasifica y el texto que sigue a la mención.
  2. Las citas internas que hoy siguen el patrón (1) (número seguido del nombre de otra norma) o el (2) («del Anexo
     de la Comunicación A NNNN»), con su chunk, su tramo, la norma nombrada y lo que crean: las de un número que
     existe en el TO de origen son relaciones `remite_a` falsas.
  3. Contrafáctico de la regla propuesta (`RE_PATRON_1`, `RE_PATRON_2`, en este script; la cadena no se edita): la
     cadena corre con `detectar_menciones_r2` envuelto, que convierte la mención interna de los patrones (1) y (2), y
     se listan las aristas `remite_a` que cambian contra el grafo r2a.
  4. Informativo: las mismas formas en el texto de E0 de los 152 TOs de la partición (`segmentacion_84/b584_particion`).

Patrón (3) (cita sin norma nombrada a un punto que el TO no tiene): queda irresoluble (decisión 7 del mandato); el
script solo controla que sus cinco filas sigan irresolubles en el contrafáctico.

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c1a_detector.py \
      --out data/experiment/r2_codigo2/salidas/c1a_detector.json
"""
from __future__ import annotations

import argparse
import csv
import io
import json
import re
import subprocess
from collections import Counter, OrderedDict

import c1_comun as K

REF = K.REF
LECTURA_M3B = "data/experiment/medicion_r2a/m3/lecturas/m3b_lectura_puntos_inexistentes.csv"
COMMIT_M3 = "4244028"
PARTICION = K.RAIZ / "data" / "experiment" / "segmentacion_84" / "b584_particion"

# Filas «detector» de M3.b por patrón (mandato, C1.a).
FILAS_PATRON = {"1": ("B01", "B03", "B04", "B07", "B08", "B10", "B11", "B12", "B16"),
                "2": ("B13", "B14", "B15", "B17"),
                "3": ("B19", "B21", "B22", "B29", "B30")}

# ----------------------------------------------------------------------------------------------------------------
# Regla propuesta. Se aplica al texto normalizado (normalizar_e0), en la posición donde termina la mención de puntos
# que `detectar_menciones_r2` clasificó como interna (sin marca de propio TO).
# (1) número seguido del nombre de otra norma, con o sin título intermedio entre comillas: «de la NIIF 9», «“Deterioro
#     de Valor” de la Norma Internacional de Información Financiera (NIIF) 9», «de las normas de “X”», «de las normas
#     “X”», «de la “Reglamentación de la cuenta corriente bancaria”». El nombre entre comillas se resuelve con la
#     regla (g) (`resolver_norma_r2_via`); NIIF y NIC nunca son un TO del inventario.
# (2) «del Anexo de la Comunicación A NNNN»: la cita va al registro de Comunicaciones, sin arista.
# ----------------------------------------------------------------------------------------------------------------
_ABRE, _CIERRA = "\"“«‘", "\"”»’"
RE_PATRON_1 = re.compile(
    r"\s*(?:[–—-]\s*)?"
    r"(?:(?P<titulo>[" + _ABRE + r"][^" + _CIERRA + r"]{1,120}[" + _CIERRA + r"])\s*,?\s*)?"
    r"(?:de|del)\s+(?:(?:la|las|los|el)\s+)?"
    r"(?:"
    r"(?:[Nn]ormas?|[Dd]isposiciones|[Rr]eglamentaci[oó]n|[Tt]exto\s+[Oo]rdenado|T\.?\s?O\.?)\s+"
    r"(?:(?:de|sobre)\s+(?:(?:la|las|los|el)\s+)?)?"
    r"(?P<q1>[" + _ABRE + r"])(?P<n1>[^" + _CIERRA + r"]{3,200})[" + _CIERRA + r"]"
    r"|(?P<q2>[" + _ABRE + r"])(?P<n2>[^" + _CIERRA + r"]{3,200})[" + _CIERRA + r"]"
    r"|(?P<n3>(?:NIIF|NIC)\s*\d+|Norma\s+Internacional\s+de\s+Informaci[oó]n\s+Financiera\s*(?:\(\s*NIIF\s*\)\s*)?\d+)"
    r")")
RE_PATRON_2 = re.compile(
    r"\s*(?:[–—-]\s*)?(?:del|de\s+la)\s+[Aa]nexo(?:\s+[IVX]+)?\s+(?:a\s+|de\s+)?la\s+Comunicaci[oó]n\s*"
    r"[\"“”'«»]?\s*(?P<letra>[ABC])\s*[\"“”'«»]?\s*(?:N[°º]\s*)?(?P<num>\d{1,2}\.?\d{3}|\d{1,4})")
CAUSA_PATRON_2 = "punto del Anexo de una Comunicación"
# Un nombre entre comillas que empieza como una división del documento («de la “Sección 3 – Criterio generales”»,
# ri_dcpc::7.2 en la partición) no es otra norma: la mención sigue interna.
RE_NO_ES_NORMA = re.compile(r"(?:Secci[oó]n|Anexo|Cap[ií]tulo|T[ií]tulo|Punto|Apartado)\b", re.I)


def clasificar_siguiente(texto: str, fin: int) -> dict | None:
    """Patrón (1) o (2) del texto que sigue a una mención de puntos que termina en `fin`, o None."""
    m = RE_PATRON_2.match(texto, fin)
    if m:
        return {"patron": "2", "norma_nombrada": f"Comunicación {m.group('letra')} {m.group('num').replace('.', '')}",
                "fin": m.end(), "entrecomillada": False, "titulo_intermedio": None}
    m = RE_PATRON_1.match(texto, fin)
    if m:
        nombre = (m.group("n1") or m.group("n2") or m.group("n3")).strip()
        if m.group("n3") is None and RE_NO_ES_NORMA.match(nombre):
            return None
        return {"patron": "1", "norma_nombrada": " ".join(nombre.split()), "fin": m.end(),
                "entrecomillada": m.group("n3") is None,
                "titulo_intermedio": m.group("titulo")}
    return None


def _posiciones_internas(texto: str, reglas: frozenset) -> dict:
    """(evidencia, puntos) → posiciones de las menciones de puntos, como las arma la rama interna del detector."""
    re_p = REF._re_puntos_r2(reglas) if reglas & frozenset("cf") else REF.RE_PUNTOS
    pos: dict = {}
    for pm in re_p.finditer(texto):
        ev = texto[max(0, pm.start() - 60):pm.end() + 20].strip()
        pos.setdefault((ev, tuple(REF._expandir_puntos_r2(pm.group(1), reglas))), []).append(pm)
    return pos


def envolver(convertir: bool, tabla: dict):
    """Envoltorios de `detectar_menciones_r2` y `menciones_por_tramo`. Con `convertir=False` solo marcan la mención
    interna de los patrones (1) y (2) (la salida de la cadena no cambia); con True la convierten: patrón (1) en
    mención externa a la norma nombrada; patrón (2) en mención a la Comunicación, irresoluble con causa propia.
    `tabla`: evidencia literal → datos de la mención marcada o convertida."""
    det_orig, mpt_orig = REF.detectar_menciones_r2, REF.menciones_por_tramo

    def det(texto, to_origen, reglas=REF.REGLAS_R2, normas_previas=None):
        ms = det_orig(texto, to_origen, reglas, normas_previas)
        reglas = frozenset(reglas)
        if not reglas:
            return ms
        pos = _posiciones_internas(texto, reglas)
        out = []
        for m in ms:
            if m["clase"] == "interna" and m["puntos"] and not m.get("marca_propio_to"):
                cands = pos.get((m["evidencia"], tuple(m["puntos"])))
                pm = cands.pop(0) if cands else None
                c = clasificar_siguiente(texto, pm.end()) if pm is not None else None
                if c is not None:
                    marca = {"patron": c["patron"], "norma_nombrada": c["norma_nombrada"],
                             "titulo_intermedio": c["titulo_intermedio"],
                             "siguiente": texto[pm.end():c["fin"]].strip(),
                             "evidencia_interna": m["evidencia"]}
                    if not convertir:
                        m = {**m, "_patron": marca}
                    elif c["patron"] == "1":
                        to, via = (REF.resolver_norma_r2_via(c["norma_nombrada"], True, reglas, c["norma_nombrada"])
                                   if c["entrecomillada"] else (None, None))
                        m = {"clase": "externa", "norma_nombrada": c["norma_nombrada"], "to_destino": to,
                             "puntos": m["puntos"], "secciones": [],
                             "evidencia": texto[pm.start():c["fin"]].strip(), "_patron": marca}
                        if via:
                            m["via_norma"] = via
                    else:
                        m = {"clase": "comunicacion_anexo", "norma_nombrada": c["norma_nombrada"], "to_destino": None,
                             "puntos": m["puntos"], "secciones": [],
                             "evidencia": texto[pm.start():c["fin"]].strip(),
                             "causa_irresoluble": CAUSA_PATRON_2, "_patron": marca}
            out.append(m)
        return out

    def mpt(tramos, to_origen, reglas):
        out = mpt_orig(tramos, to_origen, reglas)
        for m in out:
            if "_patron" in m:
                x = {**m["_patron"], "clase": m["clase"], "puntos": list(m["puntos"]),
                     "to_destino": m["to_destino"]}
                previo = tabla.setdefault(m["evidencia"], x)
                if previo != x:
                    previo.setdefault("colisiones", []).append(x)
        return out

    return [(REF, "detectar_menciones_r2", det), (REF, "menciones_por_tramo", mpt)]


def _clave_cita(c: dict) -> tuple:
    return (c.get("chunk_id"), c["evidencia"], tuple(c["puntos"]), tuple(c["secciones"]))


def citas_de_patron(registro: list[dict], tabla: dict) -> list[dict]:
    """Citas del registro de remisiones cuya mención está en `tabla` (marcada o convertida)."""
    out = []
    for c in registro:
        t = tabla.get(c["evidencia"])
        if t is None or not set(c["puntos"]) <= set(t["puntos"]):
            continue
        out.append(OrderedDict([
            ("patron", t["patron"]), ("chunk_id", c.get("chunk_id")),
            ("procedencia", c["procedencia"]), ("atribucion", c.get("atribucion")),
            ("clase", c["clase"]), ("norma_nombrada", t["norma_nombrada"]),
            ("titulo_intermedio", t["titulo_intermedio"]), ("texto_que_sigue", t["siguiente"]),
            ("tramo", c["evidencia"]), ("puntos", c["puntos"]), ("to_destino", c["to_destino"]),
            ("destinos", [{"destino": d["destino"], "alcance": d["alcance"], "n_nodos": len(d["nodos"])}
                          for d in c["destinos"]]),
            ("irresolubles", c["irresolubles"]), ("aristas_nuevas", c["aristas_nuevas"]),
            ("origenes", c["origenes"])]))
    return out


def _resumen_arista(e: dict, tabla: dict) -> dict:
    t = tabla.get(e["properties"].get("evidencia"))
    return OrderedDict([("source", e["source"]), ("target", e["target"]),
                        ("destino", e["properties"].get("destino")), ("alcance", e["properties"].get("alcance")),
                        ("chunk_id", e["provenance"].get("chunk_id")), ("tramo", e["properties"].get("evidencia")),
                        ("patron", t["patron"] if t else None),
                        ("norma_nombrada", t["norma_nombrada"] if t else None)])


def filas_m3b() -> list[dict]:
    txt = subprocess.run(["git", "show", f"{COMMIT_M3}:{LECTURA_M3B}"], cwd=K.RAIZ, capture_output=True, text=True,
                         check=False).stdout
    if not txt:
        # en una copia sin .git: el mismo archivo, que M3 commiteó en 4244028 y no cambió desde entonces
        txt = (K.RAIZ / LECTURA_M3B).read_text(encoding="utf-8")
    return list(csv.DictReader(io.StringIO(txt)))


def diagnostico_filas(base: dict, contra: dict, tabla_b: dict, tabla_c: dict) -> list[dict]:
    """Para cada fila «detector» de M3.b (diez): rama que la clasifica, texto que sigue, patrón y qué pasa con la
    regla propuesta."""
    reg_b = base["escritos"]["remisiones_registro.json"]
    reg_c = contra["escritos"]["remisiones_registro.json"]
    out = []
    for f in filas_m3b():
        if f["veredicto"] != "detector":
            continue
        dest = f["destino_citado"]
        cita = next((c for c in reg_b if c.get("chunk_id") == f["chunk_origen"] and c["evidencia"] == f["evidencia"]
                     and any(x["destino"] == dest for x in c["irresolubles"])), None)
        t = tabla_b.get(f["evidencia"])
        patron_mandato = next(p for p, fs in FILAS_PATRON.items() if f["id_lectura"] in fs)
        despues = None
        if cita is not None and t is None:
            # patrón (3): lo que sigue a la mención, para mostrar que no hay norma nombrada
            despues = "(sin norma nombrada a continuación)"
        # la misma mención en el contrafáctico: mismo chunk, mismos puntos y, si no es de los patrones (1) o (2),
        # la misma clase
        tc = [c for c in reg_c if cita is not None and c.get("chunk_id") == f["chunk_origen"]
              and c["puntos"] == cita["puntos"] and (t is not None or c["clase"] == cita["clase"])]
        out.append(OrderedDict([
            ("id_lectura", f["id_lectura"]), ("chunk_origen", f["chunk_origen"]), ("destino_citado", dest),
            ("patron_del_mandato", patron_mandato), ("patron_detectado", t["patron"] if t else None),
            ("norma_nombrada", t["norma_nombrada"] if t else None),
            ("texto_que_sigue", t["siguiente"] if t else despues),
            ("en_el_registro_r2a", cita is not None),
            ("clase_r2a", cita["clase"] if cita else None),
            ("rama", "interna por puntos: r1_referencias.py:735-744 (detectar_menciones_r2; en la cadena r1, :179-187)"
             if cita is not None and cita["puntos"] and not cita["secciones"] else None),
            ("por_que", "norma_despues (r1_referencias.py:727-733) no encuentra RE_NORMA (:63-65) ni una anáfora "
                        "(RE_ANAFORA_NORMA, :482-489) en los 90 caracteres que siguen (VENTANA_DESPUES, :50)"),
            ("causa_r2a", [x["causa"] for x in cita["irresolubles"] if x["destino"] == dest] if cita else None),
            ("con_la_regla", [OrderedDict([("clase", c["clase"]), ("norma_nombrada", c["norma_nombrada"]),
                                           ("to_destino", c["to_destino"]),
                                           ("destinos", [d["destino"] for d in c["destinos"]]),
                                           ("irresolubles", c["irresolubles"])]) for c in tc])]))
    return out


def censo_particion() -> dict:
    """Informativo: menciones internas de los patrones (1) y (2) en el texto propio de E0 de los 152 TOs."""
    conteos = json.loads((PARTICION / "conteos_b584.json").read_text(encoding="utf-8"))
    tos = sorted(t for t, v in conteos.items() if isinstance(v, dict))
    titulos_previos = REF.TITULOS_TOS
    # títulos de los 157: los 152 de la partición y los cinco de desarrollo (inventario_resumen.json)
    desarrollo = [x["id_interno"] for x in json.loads(REF.INVENTARIO_RESUMEN.read_text(encoding="utf-8"))["subset_excluido"]]
    REF.TITULOS_TOS = REF.titulos_de_inventario(sorted(set(tos) | set(desarrollo)))
    try:
        por_patron, nombres, filas = Counter(), Counter(), []
        for to in tos:
            p = PARTICION / to / f"chunks_{to}.json"
            if not p.exists():
                continue
            d = json.loads(p.read_text(encoding="utf-8"))
            for c in (d["chunks"] if isinstance(d, dict) else d):
                texto, _ = REF.normalizar_e0(c.get("texto") or "", tolerar_linea_suelta=True)
                ms = REF.detectar_menciones_r2(texto, to, REF.REGLAS_R2, [])
                pos = _posiciones_internas(texto, REF.REGLAS_R2)
                for m in ms:
                    if m["clase"] != "interna" or not m["puntos"] or m.get("marca_propio_to"):
                        continue
                    cands = pos.get((m["evidencia"], tuple(m["puntos"])))
                    pm = cands.pop(0) if cands else None
                    k = clasificar_siguiente(texto, pm.end()) if pm is not None else None
                    if k is None:
                        continue
                    to_n = (REF.resolver_norma_r2(k["norma_nombrada"], True, REF.REGLAS_R2, k["norma_nombrada"])
                            if k["patron"] == "1" and k["entrecomillada"] else None)
                    por_patron[k["patron"]] += 1
                    nombres[(k["patron"], k["norma_nombrada"][:70], to_n)] += 1
                    filas.append({"to": to, "chunk_id": c["id"], "patron": k["patron"],
                                  "norma_nombrada": k["norma_nombrada"], "to_resuelto": to_n,
                                  "tramo": texto[pm.start():k["fin"]][:200]})
    finally:
        REF.TITULOS_TOS = titulos_previos
    return OrderedDict([
        ("tos", len(tos)), ("menciones_por_patron", dict(sorted(por_patron.items()))),
        ("chunks", len({f["chunk_id"] for f in filas})),
        ("nombres", [{"patron": p, "norma_nombrada": n, "to_resuelto": t, "menciones": v}
                     for (p, n, t), v in sorted(nombres.items(), key=lambda kv: (-kv[1], kv[0]))]),
        ("filas", filas)])


def medir(nombre: str) -> tuple[OrderedDict, dict, dict, dict, dict]:
    tabla_b, tabla_c = {}, {}
    base = K.correr_r2(nombre, envolver(False, tabla_b))
    control = K.control_sha(nombre, base)
    contra = K.correr_r2(nombre, envolver(True, tabla_c))
    reg_b = base["escritos"]["remisiones_registro.json"]
    citas = citas_de_patron(reg_b, tabla_b)
    dif = K.diferencia_aristas(base["kg"], contra["kg"], "remite_a")
    # aristas que siguen, con otra evidencia (también las sostenía otra cita)
    b = {K.tripla(e): e for e in base["kg"]["edges"] if e["relation"] == "remite_a"}
    c = {K.tripla(e): e for e in contra["kg"]["edges"] if e["relation"] == "remite_a"}
    cambian = [k for k in sorted(set(b) & set(c)) if b[k] != c[k]]
    reg_c = contra["escritos"]["remisiones_registro.json"]
    com_c = [c_ for c_ in reg_c if c_["clase"] == "comunicacion_anexo"]

    def por(lista, f):
        return dict(sorted(Counter(f(x) for x in lista).items()))
    resumen = OrderedDict([
        ("control_sha_sin_cambio", control),
        ("control_sha_marcado_igual_al_versionado", base["sha256"] == K.GRAFOS[nombre]["sha256"]),
        ("citas_internas_de_patron_en_r2a", OrderedDict([
            ("total", len(citas)), ("por_patron", por(citas, lambda x: x["patron"])),
            ("con_destino_resuelto", por([x for x in citas if x["destinos"]], lambda x: x["patron"])),
            ("aristas_nuevas_que_crean", por([x for x in citas for _ in range(x["aristas_nuevas"])],
                                             lambda x: x["patron"])),
            ("irresolubles_por_causa", por([(x["patron"], i["causa"]) for x in citas for i in x["irresolubles"]],
                                           lambda t: f"{t[0]}: {t[1]}"))])),
        ("contrafactico", OrderedDict([
            ("sha256_kg", contra["sha256"]),
            ("remite_a_r2a", len(b)), ("remite_a_con_la_regla", len(c)),
            ("quitadas", len(dif["quitadas"])), ("agregadas", len(dif["agregadas"])),
            ("siguen_con_otra_evidencia_o_procedencia", len(cambian)),
            ("quitadas_por_patron", por(dif["quitadas"], lambda e: (tabla_b.get(e["properties"]["evidencia"])
                                                                   or {}).get("patron"))),
            ("citas_a_comunicacion_por_anexo", len({_clave_cita(x) for x in com_c})),
            ("citas_resueltas", contra["resumen"]["remite_a"]["citas_resueltas"]),
            ("citas_resueltas_r2a", base["resumen"]["remite_a"]["citas_resueltas"]),
            ("citas_irresolubles", contra["resumen"]["remite_a"]["citas_irresolubles"]),
            ("citas_irresolubles_r2a", base["resumen"]["remite_a"]["citas_irresolubles"]),
            ("irresolubles_por_causa", contra["resumen"]["remite_a"]["irresolubles_por_causa"]),
            ("irresolubles_por_causa_r2a", base["resumen"]["remite_a"]["irresolubles_por_causa"]),
            ("nodos_y_aristas_iguales_salvo_remite_a",
             len(base["kg"]["nodes"]) == len(contra["kg"]["nodes"])
             and not K.diferencia_aristas({"edges": [e for e in base["kg"]["edges"] if e["relation"] != "remite_a"]},
                                          {"edges": [e for e in contra["kg"]["edges"]
                                                     if e["relation"] != "remite_a"]})["quitadas"])])),
    ])
    detalle = OrderedDict([
        ("citas_internas_de_patron_en_r2a", citas),
        ("aristas_quitadas", [_resumen_arista(e, tabla_b) for e in dif["quitadas"]]),
        ("aristas_agregadas", [_resumen_arista(e, tabla_c) for e in dif["agregadas"]]),
        ("aristas_que_siguen_con_otra_evidencia", [{"antes": _resumen_arista(b[k], tabla_b),
                                                    "despues": _resumen_arista(c[k], tabla_c)} for k in cambian]),
        ("citas_a_comunicacion_por_anexo", [{"chunk_id": x.get("chunk_id"), "comunicacion": x["norma_nombrada"],
                                             "puntos": x["puntos"], "tramo": x["evidencia"]}
                                            for x in sorted({_clave_cita(y): y for y in com_c}.values(),
                                                            key=_clave_cita)]),
    ])
    return resumen, detalle, base, contra, (tabla_b, tabla_c)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--sin-particion", action="store_true", help="omite el censo informativo de los 152 TOs")
    a = ap.parse_args()
    out = OrderedDict([("regla_propuesta", OrderedDict([
        ("patron_1", RE_PATRON_1.pattern), ("patron_2", RE_PATRON_2.pattern),
        ("causa_patron_2", CAUSA_PATRON_2)]))])
    for nombre in K.GRAFOS:
        resumen, detalle, base, contra, (tb, tc) = medir(nombre)
        out[nombre] = OrderedDict([("resumen", resumen), ("detalle", detalle)])
        if nombre == "diez":
            out["filas_m3b_detector"] = diagnostico_filas(base, contra, tb, tc)
    if not a.sin_particion:
        out["particion_152_informativo"] = censo_particion()
    K.escribir_json(K.RAIZ / a.out, out)
    for nombre in K.GRAFOS:
        r = out[nombre]["resumen"]
        print(nombre, r["control_sha_sin_cambio"]["reproduce"], json.dumps(r["citas_internas_de_patron_en_r2a"],
                                                                         ensure_ascii=False),
              json.dumps({k: r["contrafactico"][k] for k in ("quitadas", "agregadas",
                                                             "siguen_con_otra_evidencia_o_procedencia")}))


if __name__ == "__main__":
    main()
