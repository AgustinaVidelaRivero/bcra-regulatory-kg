"""U-R2-CODIGO, R3 — selftest del perfil r2 en el ensamblado y en el runner.

Grupos (casos sintéticos salvo donde se indica):
  T1  remite_a y variantes `::rep<k>` (precisión del «seguí» de R3.d): una cita
      a una unidad con variantes se resuelve al id canónico de la regla L; con
      más de una variante con texto de cuerpo, «destino ambiguo», sin arista;
      criterio de texto de cuerpo; sin perfil r2, la cadena r1 no cambia;
  T2  texto de E0: unión de cortes de palabra y evidencia literal; alcance;
      registro de citas a Comunicaciones (pie no recortado);
  T3  resolución de sujetos por relación (L-ESQ-R2 §3.3) con el índice r2:
      R1, R2, calificador, R3, sin match; decisión regla/modelo; registro;
  T4  re-resolución del registro: idempotente y sensible al sha del catálogo;
  T5  E2 r2: procedencia con chunk_id, Sujeto_propuesto desde el registro,
      marcas en la arista; establecida_en derivada;
  T6  runner: entrada r2 (crudo del intento aceptado, cola, rechazado en E1)
      y claves de los reintentos iguales a las del lector de R2 (cla, tanda 0
      dirigida, datos reales, solo lectura);
  T7  reglas (a) a (i) del detector r2 (decisiones sobre el freno posterior a
      R3): un caso positivo y uno negativo por regla, «Superintendencia» no es
      norma, y sin reglas el detector r2 es el de la cadena r1.
Escribe solo en un directorio temporal (TMPDIR). USD 0.

Uso:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo/selftest_r3.py
"""

from __future__ import annotations

import contextlib
import json
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for p in (REX / "corpus_v2", REX, REPO / "data" / "experiment" / "grafo_v2" / "code", REX / "e2_reduce",
          REX / "e1_extractor", REX / "e3_verificador", REPO / "data" / "experiment" / "r2_codigo"):
    if str(p) not in sys.path:
        sys.path.insert(0, str(p))
import r1_comun as C  # noqa: E402
import r1_referencias as REF  # noqa: E402
import r1_e4 as E4  # noqa: E402
import e2_lib  # noqa: E402
import runner_corpus as RC  # noqa: E402

RES: list[tuple[str, bool, str]] = []


def check(nombre: str, ok: bool, detalle: str = "") -> None:
    RES.append((nombre, ok, detalle))
    print(f"  [{'PASS' if ok else 'FAIL'}] {nombre}" + (f" — {detalle}" if detalle else ""))


@contextlib.contextmanager
def e0_sintetico(chunks: list[dict]):
    with tempfile.TemporaryDirectory() as d:
        Path(d, "chunks_syn.json").write_text(json.dumps(chunks, ensure_ascii=False), encoding="utf-8")
        Path(d, "estructura_syn.json").write_text(json.dumps({"secciones": []}), encoding="utf-8")
        orig = (C.E0_ENM01, C.TOS_ORDEN, REF.INVENTARIO_TOS, REF.TITULOS_TOS)
        C.E0_ENM01, C.TOS_ORDEN, REF.INVENTARIO_TOS = Path(d), ("syn",), {"syn": ("sintetico",)}
        REF.TITULOS_TOS = {"syn": "sintetico"}
        try:
            yield
        finally:
            C.E0_ENM01, C.TOS_ORDEN, REF.INVENTARIO_TOS, REF.TITULOS_TOS = orig


def chunk(cid, unidad, texto, original=None):
    c = {"id": cid, "to": "syn", "archivo": "syn.pdf", "unidad": unidad, "texto": texto, "herencia": [],
         "paginas": [1], "tipo": "punto_terminal", "titulo": "", "sha256_completo": cid}
    if original:
        c["id_e0_original"] = original
    return c


def nodo(nid, tipo, punto, cid, desc="x"):
    p = {"to": "syn", "archivo": "syn.pdf", "punto": punto, "rol_documental": "punto_propio", "chunk_id": cid}
    return {"id": nid, "type": tipo, "label": nid, "properties": {"descripcion": desc}, "provenance": dict(p),
            "provenances": [dict(p)]}


def t1():
    print("T1. remite_a y variantes ::rep")
    to_n = {"id": "TextoOrdenado_syn", "type": "TextoOrdenado", "label": "S", "properties": {},
            "provenance": {"to": "syn", "punto": "1.1", "rol_documental": "punto_propio"},
            "provenances": [{"to": "syn", "punto": "1.1", "rol_documental": "punto_propio"}]}
    base_chunks = [chunk("syn::1.1", "1.1", "Las entidades observarán lo dispuesto en el punto 2.1. de estas normas."),
                   chunk("syn::2.1", "2.1", "2.1. Título.\nTexto de cuerpo con contenido normativo.\nOtra línea.")]
    kg = {"nodes": [to_n, nodo("Obligacion_a", "Obligacion", "1.1", "syn::1.1", "observar el punto 2.1"),
                    nodo("Restriccion_b", "Restriccion", "2.1", "syn::2.1"),
                    nodo("Restriccion_idx", "Restriccion", "2.1", "syn::2.1::rep2")], "edges": []}
    idx_rep = chunk("syn::2.1::rep2", "2.1", "2.1. Título.", original="syn::2.1")
    with e0_sintetico(base_chunks + [idx_rep]):
        r = REF.detectar_y_resolver(json.loads(json.dumps(kg)), perfil="r2")
    pares = {(e["source"], e["target"]) for e in r["nuevas"]}
    check("T1a variante de índice: la cita se resuelve al canónico (solo sus nodos)",
          pares == {("Obligacion_a", "Restriccion_b")}, str(pares))
    e = r["nuevas"][0] if r["nuevas"] else {}
    check("T1b arista remite_a: alcance interna, destino syn::2.1, evidencia literal, sin rol_fuente",
          e.get("relation") == "remite_a" and e.get("properties", {}).get("alcance") == "interna"
          and e["properties"].get("destino") == "syn::2.1" and "punto 2.1" in e["properties"].get("evidencia", "")
          and "rol_fuente" not in e and set(e["properties"]) == {"alcance", "destino", "evidencia"})
    check("T1c la cita a una unidad con variantes se cuenta", r["resumen"]["citas_a_unidad_con_variantes"] == 1)
    cuerpo_rep = chunk("syn::2.1::rep2", "2.1", "2.1. Título.\nOtro texto de cuerpo.\nY más.", original="syn::2.1")
    with e0_sintetico(base_chunks + [cuerpo_rep]):
        r2 = REF.detectar_y_resolver(json.loads(json.dumps(kg)), perfil="r2")
    check("T1d dos variantes con texto de cuerpo: destino ambiguo, sin arista, contado",
          not r2["nuevas"] and r2["resumen"]["irresolubles_por_causa"].get("destino ambiguo") == 1,
          json.dumps(r2["resumen"]["irresolubles_por_causa"]))
    check("T1e criterio: línea de índice sin cuerpo", not REF.tiene_texto_de_cuerpo("6.1. Solicitud de participación."))
    check("T1f criterio: rótulo con cola de título partido, sin cuerpo",
          not REF.tiene_texto_de_cuerpo("6.8. Cronograma global de amortización del capital por el\nBanco Central."))
    check("T1g criterio: varias líneas de índice seguidas, sin cuerpo",
          not REF.tiene_texto_de_cuerpo("7.52. Moneda.\nSección 8. Cheques cancelatorios.\n8.1. Características."))
    check("T1h criterio: rótulo y texto, con cuerpo",
          REF.tiene_texto_de_cuerpo("6.1. Solicitud de participación.\nLugar y fecha,\nA la Gerencia"))
    try:
        REF.detectar_y_resolver({"nodes": [], "edges": []}, fuente="e0")
        check("T1i sin perfil r2 las opciones r2 no se aceptan", False)
    except TypeError:
        check("T1i sin perfil r2 las opciones r2 no se aceptan", True)


def t2():
    print("T2. texto de E0, alcance y Comunicaciones")
    orig = "puntos 6.5.1. y 7.2.1. de las nor-\nmas sobre “Clasificación de deudores”"
    norm, mapa = REF.normalizar_e0(orig)
    check("T2a corte de palabra unido y salto a espacio", "normas sobre" in norm and "\n" not in norm, norm)
    ev = REF.evidencia_literal(orig, norm, mapa, norm[norm.index("puntos"):])
    check("T2b la evidencia es un tramo literal del original", ev in orig and "nor-\nmas" in ev, repr(ev))
    with e0_sintetico([chunk("syn::1.1", "1.1", "x")]):
        men = REF.detectar_menciones(norm, "cap")
    check("T2c con el texto unido, la cita nombra la norma (no es interna)",
          any(m["clase"] == "externa" and m["puntos"] == ["6.5.1", "7.2.1"] for m in men))
    t3 = "el equivalente a dos veces el importe de\nreferencia establecido en el punto 3.7. y cuyo repago no se encuentre"
    n3, m3 = REF.normalizar_e0(t3)
    ev3 = REF.evidencia_literal(t3, n3, m3, n3[n3.index("ente a dos"):n3.index("repago") + 3])
    check("T2g evidencia extendida al límite de palabra en los dos extremos, literal",
          ev3 == "equivalente a dos veces el importe de\nreferencia establecido en el punto 3.7. y cuyo repago"
          and ev3 in t3, repr(ev3))
    t4 = "de las nor-\nmas sobre x, puntos 3.6.1.3. a 3.6.1.5."
    n4, m4 = REF.normalizar_e0(t4)
    ev4 = REF.evidencia_literal(t4, n4, m4, n4[n4.index("mas sobre"):n4.index("3.6.1.5") + 3])
    check("T2h el corte de palabra al final de línea y los números con puntos cuentan como una palabra",
          ev4 == "nor-\nmas sobre x, puntos 3.6.1.3. a 3.6.1.5", repr(ev4))
    mini = {"texto": "fondos destinados a proyectos que generen:", "herencia": [
        {"unidad_origen": "7.9", "tipo": "encabezado", "texto": "7.9. Título superior."},
        {"unidad_origen": "7.9.2", "tipo": "encabezado",
         "texto": "7.9.2. Las operaciones de los puntos 7.9.1.1. a 7.9.1.3. serán elegibles en la medida que los"}]}
    tp = REF._texto_e0_de({"punto": "7.9.2", "rol_documental": "bloque_intro"}, mini)
    check("T2i texto del punto de un mini-chunk: su encabezado heredado y su texto, sin los puntos superiores",
          "7.9.1.1." in tp and "generen" in tp and "Título superior" not in tp)
    hijo = {"texto": "4.8.4.1. Texto del hijo.", "herencia": [
        {"unidad_origen": "4.8.4", "tipo": "encabezado", "texto": "4.8.4. Los clientes que suscribieron por un"},
        {"unidad_origen": "4.8.4", "tipo": "intro", "texto": "monto para los puntos 4.4. y 4.5., podrán acceder"}]}
    th = REF._texto_e0_de({"punto": "4.8.4", "rol_documental": "herencia_encabezado"}, hijo)
    check("T2j procedencia de herencia: todos los tramos de la unidad, no solo el del rol, y no el texto del hijo",
          "4.4. y 4.5." in th and "Los clientes" in th and "Texto del hijo" not in th)
    check("T2d alcance: interna, externa y to_entero",
          (REF.alcance_remision("cla", "cla", False), REF.alcance_remision("cla", "cap", False),
           REF.alcance_remision("cla", "cla", True)) == ("interna", "externa", "to_entero"))
    reg = REF.registro_comunicaciones({"syn": [
        chunk("syn::1.1", "1.1", "conforme la Comunicación “A” 6847 y 7000, y la Com. B 12.345."),
        chunk("syn::1.2", "1.2", "Texto.\nVersión: 2a. COMUNICACIÓN “A” 3244 Vigencia: 01/01/2001 Página 3")]})
    t = reg["total"]
    check("T2e citas a Comunicaciones: 4 citas, 2 chunks, 4 Comunicaciones",
          (t["citas"], t["chunks"], t["comunicaciones_distintas"]) == (4, 2, 4), json.dumps(t))
    check("T2f el pie de página no recortado se declara aparte",
          t["citas_en_pie_no_recortado"] == 1 and reg["pies_no_recortados"][0]["comunicacion"] == "A 3244")


def t3_t4():
    print("T3. resolución de sujetos por relación (índice r2 real)")
    cat = E4.catalogo_r2()
    idx, pref = cat["indice"], E4._prefijos(cat["indice"])
    rol = "Sujeto_rol_obligado_a_clasificar_clasificacion"
    casos = {
        "Entidades financieras": ("R1", "Sujeto_entidad_financiera"),
        "las entidades financieras": ("R1", "Sujeto_entidad_financiera"),
        "entidad financiera": ("R2", "Sujeto_entidad_financiera"),
        "Entidades financieras del exterior": ("R1", "Sujeto_entidad_financiera_del_exterior"),
        "Entidades financieras comprendidas en el Grupo A": ("R2_calificador", "Sujeto_entidad_financiera"),
        "las entidades": ("R3", rol),
        "administradores de las carteras crediticias": (None, None),
    }
    for m, (regla, i) in casos.items():
        r = E4.resolver_mencion_r2(m, None, idx, pref, rol)
        check(f"T3 «{m}» → {regla} {i}", (r["regla"], r["id"]) == (regla, i), f"{r['regla']} {r['id']}")
    r = E4.resolver_mencion_r2("Entidades financieras comprendidas en el Grupo A", None, idx, pref, rol)
    check("T3 el calificador se guarda", r["calificador"] == "comprendidas en el grupo a", str(r["calificador"]))

    def rel(i, mencion, nivel, modelo, original_id=None):
        r = {"predicate": "aplica_a", "source": "e1", "target": None, "punto": "1.1", "indice_crudo": i,
             "sujeto_mencion": mencion, "mencion_verificada": nivel, "sujeto_id_modelo": modelo,
             "padre_sugerido": None, "padre_sugerido_crudo": None, "originales": {}}
        if original_id:
            r["originales"] = {"sujeto_id": original_id}
        return r
    otro = "Sujeto_banco"
    rels = [rel(0, "Entidades financieras", "exacta", otro),
            rel(1, "entidad financiera", "exacta", otro),
            rel(2, "entidad financiera", "exacta", None),
            rel(3, "Entidades financieras", "no", otro),
            rel(4, "algo no verificado", "no", None),
            rel(5, None, "ausente", otro),
            rel(6, "Entidades financieras comprendidas en el Grupo A", "exacta", None),
            rel(7, "administradores de las carteras crediticias", "tokens", None),
            rel(8, None, "ausente", None, original_id="Sujeto_inexistente")]
    regs = [{"chunk_id": "cla::1.1", "to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf",
             "e0_sha256_completo": "h", "validacion": {"entidades": [
                 {"local_id": "e1", "type": "Obligacion", "label": "O"}], "relaciones": rels}}]
    vers = {"catalogo_sha256": cat["catalogo_sha256"], "politica_sha256": "p", "perfil": "r2", "prefijo_hash": "h"}
    res = E4.resolver_relaciones_r2(regs, idx, cat["rol_por_to"], vers)
    met = [(f["metodo_resolucion"], f["resuelto_a"], f["desacuerdo_regla_modelo"]) for f in res["resolucion"]]
    esperado = [("R1_label_exacto", "Sujeto_entidad_financiera", True),
                ("R4_sugerencia_modelo", otro, True),
                ("R2_id_slug+label_singularizado", "Sujeto_entidad_financiera", False),
                ("R4_sugerencia_modelo", otro, False),
                ("cuarentena", None, False),
                ("R4_sugerencia_modelo", otro, False),
                ("R2_calificador", "Sujeto_entidad_financiera", False),
                ("cuarentena", None, False),
                ("cuarentena", None, False)]
    for k, (a, b) in enumerate(zip(met, esperado)):
        check(f"T3 decisión, caso {k}", a == b, f"{a} vs {b}")
    motivos = {(f["indice_relacion"], f["estado"], f["motivo"]) for f in res["registro"]}
    check("T3 registro: calificador como candidato, no verificada, sin match e id fuera de catálogo",
          motivos == {(6, "resuelto_a_clase", "calificador"), (4, "cuarentena", "mencion_no_verificada"),
                      (7, "cuarentena", "sin_match"), (8, "cuarentena", "id_fuera_de_catalogo")}, str(motivos))
    check("T3 la relación sin resolver apunta a su fila", rels[7].get("registro_no_mapeados")
          == {"chunk_id": "cla::1.1", "indice_relacion": 7})

    print("T4. re-resolución del registro")
    archivo = {"cla": "TO_clasificacion_deudores_actual.pdf"}
    a = E4.reresolver_registro(res["registro"], idx, cat["rol_por_to"], archivo, "sha_nuevo")
    check("T4a con el mismo índice no resuelve nada", a["resueltas_ahora"] == 0)
    idx2 = dict(idx)
    idx2[("label_exacto", C.norm("administradores de las carteras crediticias"))] = "Sujeto_banco"
    b = E4.reresolver_registro(res["registro"], idx2, cat["rol_por_to"], archivo, "sha_nuevo")
    fila7 = next(f for f in b["filas"] if f["indice_relacion"] == 7)
    check("T4b con un id nuevo resuelve la fila, con el sha nuevo",
          b["resueltas_ahora"] == 1 and fila7["estado"] == "resuelto" and fila7["resuelto_a"] == "Sujeto_banco"
          and fila7["catalogo_sha256_resolucion"] == "sha_nuevo")
    c = E4.reresolver_registro(b["filas"], idx2, cat["rol_por_to"], archivo, "sha_nuevo")
    check("T4c idempotente", c["filas"] == b["filas"] and c["resueltas_ahora"] == 0)
    return res, regs, cat


def t5(res, regs, cat):
    print("T5. E2 r2 y establecida_en derivada")
    M = E4.modulo_modelos_r2()
    val = regs[0]["validacion"]
    val["entidades"] = [{"local_id": "e1", "type": "Obligacion", "label": "O",
                         "properties": {"descripcion": "d", "tipo": "otra"},
                         "provenance": {"to": "cla", "archivo": "a.pdf", "punto": "1.1",
                                        "rol_documental": "punto_propio"}}]
    for r in val["relaciones"]:
        r["provenance"] = {"to": "cla", "archivo": "a.pdf", "punto": "1.1", "rol_documental": "punto_propio"}
    val["rechazos"] = []
    regs[0]["error"] = None
    ch = [{"id": "cla::1.1"}]
    ens = e2_lib.ensamblar_r2(ch, regs, cat["labels"], M.SUJETOS_R2_SET, M.firma_r2, M.TIPOS_ENTIDAD,
                              M.PREDICADOS, res["registro"])
    props = [n for n in ens["nodes"] if n["properties"].get("nivel") == "propuesto"]
    check("T5a Sujeto_propuesto desde el registro, con el id del nodo en su fila",
          {n["label"] for n in props} == {"administradores de las carteras crediticias", "algo no verificado",
                                          "Sujeto_inexistente"}
          and all(f["id_nodo"] for f in res["registro"] if f["estado"] == "cuarentena"))
    check("T5b procedencia con chunk_id", all(n["provenance"].get("chunk_id") == "cla::1.1" for n in ens["nodes"]))
    a0 = next(e for e in ens["edges"] if e["target"] == "Sujeto_entidad_financiera")
    check("T5c la arista guarda método, mención y sugerencia del modelo",
          a0.get("metodo_resolucion") == "R1_label_exacto" and a0.get("sujeto_id_modelo") == "Sujeto_banco"
          and a0.get("sujeto_mencion") == "Entidades financieras")
    invalidos = 0
    for n in ens["nodes"]:
        M.NodoR2.model_validate(n)
    for e in ens["edges"]:
        try:
            M.AristaR2.model_validate(e)
        except Exception:  # noqa: BLE001
            invalidos += 1
    check("T5d nodos y aristas válidos con NodoR2 y AristaR2", invalidos == 0)
    solo = [{**regs[0], "validacion": {**val, "relaciones": [r for r in val["relaciones"]
                                                             if r.get("indice_crudo") == 6]}}]
    ens6 = e2_lib.ensamblar_r2(ch, solo, cat["labels"], M.SUJETOS_R2_SET, M.firma_r2, M.TIPOS_ENTIDAD,
                               M.PREDICADOS, [])
    a6 = [e for e in ens6["edges"] if e["relation"] == "aplica_a"]
    check("T5f el calificador llega a la arista de sujeto",
          len(a6) == 1 and a6[0].get("calificador") == "comprendidas en el grupo a"
          and M.AristaR2.model_validate(a6[0]) is not None, str(a6[0].get("calificador") if a6 else None))
    grafo_cola = {"nodes": [{"id": "Operacion_c", "type": "Operacion", "label": "O", "properties": {"descripcion": "d"},
                             "provenance": {"chunk_id": "cla::7.1"}, "provenances": [{"chunk_id": "cla::7.1"}]}],
                  "edges": [{"source": "Operacion_c", "target": "x", "relation": "regula",
                             "provenance": {"chunk_id": "cla::7.1"}, "provenances": [{"chunk_id": "cla::7.1"}]}]}
    rc = e2_lib.flaggear_cola_r2(grafo_cola, {"cla::7.1": "cola_humana"})
    check("T5g la cola humana queda marcada en el nodo y en la arista, válida con NodoR2",
          rc["nodos_marcados"] == 1 and rc["aristas_marcadas"] == 1
          and grafo_cola["nodes"][0]["properties"]["cola_chunks"] == ["cla::7.1"]
          and M.NodoR2.model_validate(grafo_cola["nodes"][0]) is not None)
    sys.path.insert(0, str(REPO / "data" / "experiment" / "tanda0" / "code"))
    import ensamblar_tanda0 as ET  # noqa: PLC0415
    kg = {"nodes": [nodo("Operacion_x", "Operacion", "1.1", "syn::1.1"), nodo("Condicion_y", "Condicion", "1.1",
                                                                             "syn::1.1"),
                    {"id": "TO_syn", "type": "TextoOrdenado", "label": "t", "properties": {}, "provenance": {},
                     "provenances": []}],
          "edges": [{"source": "Operacion_x", "target": "TO_syn", "relation": "establecida_en", "provenance": {},
                     "provenances": []}]}
    r = ET.derivar_establecida_en(kg, {"syn": "TO_syn"})
    nueva = [e for e in kg["edges"] if e.get("rol_fuente") == "derivada_de_procedencia"]
    check("T5e establecida_en derivada solo donde falta, con su procedencia",
          r["aristas_derivadas"] == 1 and nueva[0]["source"] == "Condicion_y"
          and r["nodos_de_contenido_sin_establecida_en"] == 0 and nueva[0]["provenance"]["chunk_id"] == "syn::1.1")


def t6():
    print("T6. runner: entrada r2 y claves de los reintentos")
    with tempfile.TemporaryDirectory() as d:
        t = Path(d)
        crudo = lambda s: {"entities": [{"local_id": "e1", "type": "Operacion", "label": s, "punto": "1"}],  # noqa: E731
                           "relations": [], "omisiones_no_prosa": []}
        filas = {"extracciones_e1_compact.jsonl": [
            {"chunk_id": "syn::1", "tool_input_crudo": crudo("primero")},
            {"chunk_id": "syn::2", "tool_input_crudo": crudo("cola")},
            {"chunk_id": "syn::3", "tool_input_crudo": None, "error": "salida_no_parseable"}],
            "finales.jsonl": [{"chunk_id": "syn::1", "estado": "aceptado_tras_reintento", "n_reintentos": 1,
                               "validacion_final": {}},
                              {"chunk_id": "syn::2", "estado": "cola_humana", "n_reintentos": 1,
                               "validacion_final": None}],
            "reintentos_e3.jsonl": [{"chunk_id": "syn::1", "intento": 1, "tool_input": crudo("reintento"),
                                     "error": None},
                                    {"chunk_id": "syn::2", "intento": 1, "tool_input": crudo("no"), "error": None}],
            "veredictos.jsonl": []}
        for n, fs in filas.items():
            (t / n).write_text("".join(json.dumps(x) + "\n" for x in fs), encoding="utf-8")
        chunks = [chunk(f"syn::{k}", str(k), "t") for k in (1, 2, 3)]
        regs = RC.entrada_r2("syn", t, chunks, RC.PERFIL, lambda ti, c: {"crudo": ti["entities"][0]["label"]})
    por = {r["chunk_id"]: r for r in regs}
    check("T6a con reintento aceptado, el crudo del reintento (archivo compañero)",
          por["syn::1"]["validacion"] == {"crudo": "reintento"} and por["syn::1"]["origen_crudo"]
          == "reintento_1:companero")
    check("T6b cola humana: el primer intento, marcado",
          por["syn::2"]["validacion"] == {"crudo": "cola"} and por["syn::2"].get("cola_humana") is True)
    check("T6c rechazado en E1: queda rechazado", por["syn::3"]["validacion"] is None)
    import lector_reintentos_e3 as L  # noqa: PLC0415
    import perfil_e1  # noqa: PLC0415
    cfg = L.GENERACIONES["t0_dirigida"]
    import comun_e3  # noqa: PLC0415
    ch = comun_e3.cargar_chunks(("cla",), e0_dir=cfg["e0"])
    a = [(r["chunk_id"], r["clave"]) for r in RC.claves_reintentos_cache(cfg["salida"] / "cla", ch,
                                                                          perfil_e1.perfil(cfg["perfil"]))]
    b = [(r["chunk_id"], r["clave"]) for r in L.claves_reintentos(cfg["salida"], "cla", cfg["perfil"], cfg["e0"])]
    check("T6d claves de los reintentos de cla (tanda 0 dirigida): runner = lector de R2",
          a == b and len(a) == 13, f"{len(a)} claves")


TITULOS_T7 = {"cap": "capitales minimos de las entidades financieras", "cla": "clasificacion de deudores",
              "depaho": "depositos de ahorro, cuenta sueldo y especiales", "polcre": "politica de credito",
              "gescre": "gestion crediticia", "garant": "garantias",
              "garopt": "garantias por intermediacion en operaciones entre terceros", "syn": "sintetico"}


def det(texto: str, reglas: str, to: str = "syn") -> list[dict]:
    rs = frozenset(reglas)
    return REF.detectar_menciones_r2(REF.normalizar_e0(texto, tolerar_linea_suelta="a" in rs)[0], to, rs)


def internas(ms: list[dict]) -> list[str]:
    return [p for m in ms if m["clase"] == "interna" for p in m["puntos"]]


def t7():
    print("T7. reglas (a) a (i) del detector r2")
    todas = "".join(sorted(REF.REGLAS_R2))
    orig = REF.TITULOS_TOS
    REF.TITULOS_TOS = dict(TITULOS_T7)
    try:
        textos = ["del punto 4.1.1. de las citadas normas", "puntos 1.2. y 1.3. de las normas sobre “Capitales mínimos”",
                  "en este punto y en la Sección 2. de dicho ordenamiento", "punto 3.7.– y (punto 1.1. de las normas "
                  "sobre “Gestión crediticia”)"]
        check("T7.0 sin reglas, el detector r2 da las menciones de la cadena r1",
              all(REF.detectar_menciones_r2(t, "cap", frozenset()) == REF.detectar_menciones(t, "cap") for t in textos))
        # (a)
        t_a = "observando los criterios establecidos en el punto\nn1\n8.3.5.\nA los conceptos citados"
        check("T7a+ (a) línea suelta de dos caracteres entre «punto» y el número",
              internas(det(t_a, "a")) == ["8.3.5"] and internas(det(t_a, "")) == [])
        n_a, m_a = REF.normalizar_e0(t_a, tolerar_linea_suelta=True)
        ev = REF.evidencia_literal(t_a, n_a, m_a, det(t_a, "a")[0]["evidencia"])
        check("T7a+ (a) la evidencia conserva la línea suelta (tramo literal)", "punto\nn1\n8.3.5." in ev, repr(ev))
        check("T7a- (a) una línea de tres caracteres no se tolera",
              internas(det("establecidos en el punto\nabc\n8.3.5.\nA los", "a")) == [])
        # (c)
        t_c = ("en los puntos 3.6.1.3.\n(únicamente cuando los fondos hayan sido liquidados a partir del 16/10/20) a "
               "3.6.1.5. y destinados")
        check("T7c+ (c) paréntesis dentro de un rango", internas(det(t_c, "c")) == ["3.6.1.3", "3.6.1.4", "3.6.1.5"]
              and internas(det(t_c, "")) == ["3.6.1.3"], str(internas(det(t_c, "c"))))
        check("T7c- (c) el número dentro del paréntesis no entra en la lista",
              internas(det("los puntos 1.1. (ver el 9.9.9.) y 1.2. de estas normas", "c")) == ["1.1", "1.2"],
              str(internas(det("los puntos 1.1. (ver el 9.9.9.) y 1.2. de estas normas", "c"))))
        # (d)
        t_d = ("establecido en el punto 3.7.– y a microemprendedores (según lo previsto en el punto 1.1.3.4. de las "
               "normas sobre “Gestión crediticia”)")
        ext_d = [m for m in det(t_d, "d") if m["clase"] == "externa"]
        check("T7d+ (d) el punto más lejano no se atribuye a la norma",
              internas(det(t_d, "d")) == ["3.7"] and ext_d and ext_d[0]["puntos"] == ["1.1.3.4"]
              and [m for m in det(t_d, "") if m["clase"] == "externa"][0]["puntos"] == ["3.7", "1.1.3.4"])
        t_d2 = "los puntos 1.2. y 1.3. de las normas sobre “Capitales mínimos de las entidades financieras”"
        m_d2 = det(t_d2, todas, "cla")
        check("T7d- (d) una lista inmediata a la norma sigue siendo de la norma",
              internas(m_d2) == [] and [(m["to_destino"], m["puntos"]) for m in m_d2] == [("cap", ["1.2", "1.3"])])
        # (e)
        t_e = ("según la Sección 3. de las normas sobre “Capitales mínimos de las entidades financieras”. Las DvP "
               "calculadas de acuerdo con el punto 4.1.1. de las citadas normas")
        an = [m for m in det(t_e, todas, "ric") if m["clase"] == "externa_anaforica"]
        check("T7e+ (e) «de las citadas normas» resuelve a la última norma nombrada antes",
              an and an[0]["to_destino"] == "cap" and an[0]["puntos"] == ["4.1.1"]
              and internas(det(t_e, todas, "ric")) == [] and "4.1.1" in internas(det(t_e, "", "ric")))
        sin = det("Surgirá de aplicar la expresión prevista en el punto 1.2. de las citadas normas:", todas, "ric")
        check("T7e- (e) sin norma antes en el punto: irresoluble, nunca interna",
              internas(sin) == [] and [m.get("causa_irresoluble") for m in sin] == ["anáfora sin antecedente"])
        sup = det("conforme lo disponga la Superintendencia de Entidades Financieras y Cambiarias, según el punto "
                  "4.1.1. de las citadas normas", todas, "ric")
        check("T7e- «Superintendencia» no es norma: no hay mención externa y la anáfora no tiene antecedente",
              not [m for m in sup if m["clase"] == "externa"] and internas(sup) == []
              and [m.get("causa_irresoluble") for m in sup] == ["anáfora sin antecedente"])
        fuera = det("punto 6.1. de las normas sobre “Supervisión consolidada”; con el alcance del punto 6.2. de las "
                    "normas citadas", todas, "ric")
        check("T7e- (e) la norma nombrada antes está fuera del inventario: irresoluble con esa causa",
              internas(fuera) == [] and [m.get("causa_irresoluble") for m in fuera if m["clase"] ==
                                         "externa_anaforica"] == ["norma fuera del inventario"])
        t_338 = ("3.3.8. Las entidades podrán aplicar esta modalidad conforme a lo previsto en el TO sobre Gestión "
                 "Crediticia, debiendo dejar constancia –en cada caso– de su utilización de acuerdo con el punto 1.3.5. "
                 "del citado TO.")
        a338 = [m for m in det(t_338, todas, "cla") if m["clase"] == "externa_anaforica"]
        check("T7e+ (e) cla::3.3.8 vigente (sintético): «del citado TO» resuelve a la norma nombrada antes",
              [(m["to_destino"], m["puntos"], m["forma_anafora"]) for m in a338] == [("gescre", ["1.3.5"], "del citado to.")]
              and internas(det(t_338, todas, "cla")) == [], str(a338))
        formas = ["de las citadas normas", "de dichas normas", "del citado ordenamiento", "del citado TO", "dicho TO",
                  "de la citada norma", "de las citadas disposiciones"]
        check("T7e+ (e) las siete formas de la lista son anáfora y, sin norma antes, irresolubles y nunca internas",
              all([(m["clase"], m.get("causa_irresoluble")) for m in det(f"según el punto 1.2. {f}.", todas)]
                  == [("externa_anaforica", "anáfora sin antecedente")] for f in formas))
        t_prop = ("los puntos 4.1.1.1. a 4.1.1.3. del presente régimen y la Sección 2. de las normas sobre “Capitales "
                  "mínimos de las entidades financieras”")
        m_prop = det(t_prop, todas, "ric")
        check("T7e+ (e) «del presente régimen» es el propio TO: interna aunque después se nombre otra norma",
              internas(m_prop) == ["4.1.1.1", "4.1.1.2", "4.1.1.3"]
              and [(m["to_destino"], m["puntos"], m["secciones"]) for m in m_prop if m["clase"] == "externa"]
              == [("cap", [], ["2"])] and internas(det(t_prop, "", "ric")) == [])
        m_sec = [m for m in det("según la Ley 1. y el TO sobre “Gestión crediticia”; lo establecido en la Sección 4. de "
                                "dichas normas", todas) if m["clase"] == "externa_anaforica"]
        check("T7e+ (e) la anáfora toma también la sección de su ventana",
              [(m["to_destino"], m["secciones"]) for m in m_sec] == [("gescre", ["4"])], str(m_sec))
        check("T7e+ (e) «de las presentes normas» y «de las presentes disposiciones» también",
              internas(det("el punto 2.1. de las presentes normas y el 3.1. de las normas sobre “Gestión crediticia”",
                           todas)) == ["2.1"]
              and internas(det("del punto 5.1. de las presentes disposiciones", todas)) == ["5.1"])
        # (f)
        t_f = "a cuya orden esté la cuenta, salvo lo previsto en el apartado 12.2.3.2."
        check("T7f+ (f) «apartado» con número de punto es forma de cita",
              internas(det(t_f, "f")) == ["12.2.3.2"] and internas(det(t_f, "")) == [])
        check("T7f- (f) «apartado» sin número de punto e «inciso» no son citas",
              internas(det("según el apartado A del Régimen; el inciso 1.2.3. del contrato", "f")) == [])
        # (g)
        rg = lambda z, q: REF.resolver_norma_r2(z, q, frozenset("g"))  # noqa: E731
        check("T7g+ (g) con comillas; sin comillas seguida de coma o de texto corrido; título con coma",
              (rg("Capitales mínimos de las entidades financieras", True),
               rg("Gestión Crediticia, deberá observarse lo previsto", False),
               rg("Política de Crédito en forma individual", False),
               rg("Clasificación de Deudores– y a las financiaciones", False),
               rg("Depósitos de Ahorro, Cuenta Sueldo y Especiales", False)) == ("cap", "gescre", "polcre", "cla", "depaho"))
        check("T7g+ (g) si calzan varios títulos, gana el más largo",
              (rg("Garantías por intermediación en operaciones entre terceros y otras", False), rg("Garantías", True))
              == ("garopt", "garant"))
        check("T7g- (g) «Incumplimientos de capitales mínimos…» no resuelve a cap; un nombre más corto que el título "
              "tampoco; «Superintendencia» no es norma",
              (rg("Incumplimientos de capitales mínimos y relaciones técnicas", True), rg("Capitales mínimos", True),
               rg("Garantíasx", False), rg("Superintendencia de Entidades", False)) == (None, None, None, None))
        check("T7g+ «TO sobre <título>» y «texto ordenado sobre <título>» nombran la norma como «normas sobre»",
              [[(m["clase"], m["to_destino"]) for m in det(t, todas)] for t in (
                  "conforme el TO sobre Gestión Crediticia, deberá observarse", "según el texto ordenado sobre Gestión "
                  "Crediticia.", "de las normas sobre “Gestión crediticia”")] == [[("externa", "gescre")]] * 3)
        m_g = det("del texto ordenado de las normas sobre “Capitales mínimos de las entidades financieras”", todas)
        check("T7g+ (g) «texto ordenado de las normas sobre “X”» es una cita a X",
              [(m["clase"], m["to_destino"]) for m in m_g] == [("externa", "cap")])
        # (h)
        t_h = "en el marco de los mecanismos previstos en este punto."
        check("T7h+ (h) «este punto» sin número queda registrado como anáfora sin número, sin remisión",
              [(m["clase"], m.get("causa_irresoluble"), m["to_destino"]) for m in det(t_h, "h")]
              == [("anafora_sin_numero", "anáfora sin número", None)] and det(t_h, "") == [])
        check("T7h- (h) «este punto» con número no es anáfora sin número",
              [m["clase"] for m in det("lo dispuesto en este punto 3.2. de estas normas", "h")] == ["interna"])
    finally:
        REF.TITULOS_TOS = orig
    # (b) e (i), por el ensamblado de remisiones
    kg_b = {"nodes": [nodo("Obligacion_o", "Obligacion", "6.2.1.1", "syn::6.2.1.1", "punto 2.12.3.1"),
                      nodo("Restriccion_d", "Restriccion", "2.12.3.1", "syn::2.12.3.1")], "edges": []}
    leg = [chunk("syn::6.2.1.1", "6.2.1.1", "Bancos multilaterales del punto Plazo residual 1,6% 2.12.3.1."),
           chunk("syn::2.12.3.1", "2.12.3.1", "2.12.3.1. Texto de cuerpo.\nOtra línea.")]
    r2c = {"syn::6.2.1.1": chunk("syn::6.2.1.1", "6.2.1.1", "Bancos multilaterales del punto 2.12.3.1. | col2 = 1,6%")}
    with e0_sintetico(leg):
        con = REF.detectar_y_resolver(json.loads(json.dumps(kg_b)), perfil="r2", chunks_e0_r2=r2c)
        sin_b = REF.detectar_y_resolver(json.loads(json.dumps(kg_b)), perfil="r2", chunks_e0_r2=r2c,
                                        reglas=REF.REGLAS_R2 - {"b"})
        sin_dir = REF.detectar_y_resolver(json.loads(json.dumps(kg_b)), perfil="r2")
    check("T7b+ (b) con el texto de e0-r2, la cita que la tabla linealizada cortaba",
          [(e["source"], e["target"]) for e in con["nuevas"]] == [("Obligacion_o", "Restriccion_d")]
          and con["resumen"]["texto_de_e0"]["e0-r2"] >= 1)
    check("T7b- (b) sin la regla o sin la salida de e0-r2, el texto de E0 legado (sin la cita)",
          not sin_b["nuevas"] and not sin_dir["nuevas"] and sin_dir["resumen"]["texto_de_e0"]["e0-r2"] == 0)
    hijo = chunk("syn::5.1.2", "5.1.2", "5.1.2. Texto propio sin citas.")
    hijo["herencia"] = [{"unidad_origen": "5.1", "tipo": "encabezado",
                         "texto": "5.1. Operaciones.\nLas comprendidas en los puntos 3.1. a 3.3."}]
    leg_i = [hijo] + [chunk(f"syn::3.{k}", f"3.{k}", f"3.{k}. Cuerpo.\nTexto.") for k in (1, 2, 3)]
    kg_i = {"nodes": [nodo("Obligacion_nombra", "Obligacion", "5.1.2", "syn::5.1.2", "operaciones del punto 3.2."),
                      nodo("Obligacion_no", "Obligacion", "5.1.2", "syn::5.1.2", "operaciones sin número"),
                      nodo("Obligacion_sub", "Obligacion", "5.1.2", "syn::5.1.2", "lo del punto 3.2.1.")]
            + [nodo(f"Restriccion_3{k}", "Restriccion", f"3.{k}", f"syn::3.{k}") for k in (1, 2, 3)], "edges": []}
    with e0_sintetico(leg_i):
        ri = REF.detectar_y_resolver(json.loads(json.dumps(kg_i)), perfil="r2")
        ri_sin = REF.detectar_y_resolver(json.loads(json.dumps(kg_i)), perfil="r2", reglas=REF.REGLAS_R2 - {"i"})
    pares_i = sorted((e["source"], e["target"]) for e in ri["nuevas"])
    e_i = ri["nuevas"][0] if ri["nuevas"] else {}
    check("T7i+ (i) el nodo que nombra la unidad recibe la arista de la cita heredada, solo a esa unidad",
          pares_i == [("Obligacion_nombra", "Restriccion_32")], str(pares_i))
    check("T7i+ (i) evidencia literal del tramo heredado y procedencia del bloque heredado",
          "puntos 3.1. a 3.3." in e_i.get("properties", {}).get("evidencia", "")
          and e_i["properties"]["evidencia"] in hijo["herencia"][0]["texto"]
          and e_i.get("provenance", {}).get("punto") == "5.1"
          and e_i["provenance"].get("rol_documental") == "herencia_encabezado", json.dumps(e_i.get("provenance")))
    check("T7i- (i) los nodos que no nombran la unidad (ni «3.2.1» por «3.2») no la reciben; sin la regla, nada",
          not ri_sin["nuevas"] and not any(s in ("Obligacion_no", "Obligacion_sub") for s, _ in pares_i))


def main() -> int:
    t1()
    t2()
    res, regs, cat = t3_t4()
    t5(res, regs, cat)
    t6()
    t7()
    ok = sum(1 for _, b, _ in RES if b)
    print(f"SELFTEST R3: {ok}/{len(RES)} {'PASS' if ok == len(RES) else 'FAIL'}")
    return 0 if ok == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
