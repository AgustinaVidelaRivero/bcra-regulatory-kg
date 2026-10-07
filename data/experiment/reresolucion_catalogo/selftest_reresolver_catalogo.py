"""U-RERESOL-CAT, R2 — selftest de reresolver_catalogo.py y de los cambios W1 a W3 (casos sintéticos; USD 0).

Importa el script (y por él, el ensamblador y r1_e4) por el mismo camino que la corrida real: no arregla el sys.path por
fuera. Escribe solo en un directorio temporal (TMPDIR).

Grupos:
  S1  componer: sin ampliaciones, el compuesto es el catálogo del request byte a byte; alta de un id (con las claves y el
      grupo de su padre, sin rol_por_to) y alta de un alias; frena con formato o sha ajenos, sin evidencia, con una
      expresión colectiva, con un label o alias que ya existe, con un id existente y con un padre que no es clase.
  S2  generados de resolución y su candado (W2, r1_e4.catalogo_resolucion_r2): sin ampliaciones, iguales a
      generados_r2/ y con el conjunto de ids del request; con ampliaciones, el id nuevo en el conjunto y en los labels;
      frena si cambia un generado, la lista de ampliaciones, el sha del request del manifiesto o si falta un id del
      request.
  S3  W2, un solo nombre de método: reresolver_registro escribe el mismo método que resolver_relaciones_r2 (R1 con sus
      criterios, R2, calificador, R3).
  S4  `decidir` reproduce la decisión de resolver_relaciones_r2, campo por campo, en los casos de la regla.
  S5  (a+): un alias nuevo hace ganar a R1 sobre la sugerencia del modelo (cambia el destino) y no toca lo demás.
  S6  registro acumulado: la fila que resuelve conserva la versión de entrada y lleva la de resolución; la que sigue en
      cuarentena es la de (b) salvo la versión; la fila nueva de (b) se agrega y se lista; una diferencia frena.
  S7  contraste: la mudanza predicha, el propuesto que desaparece y el id nuevo con su esqueleto quedan explicados; una
      arista no predicha, no.
  S8  W1: sujetos_de_resolucion y las redirecciones; en E2, sin el conjunto de resolución la relación al id nuevo se
      rechaza (sujeto_id_fuera_de_catalogo) y con él entra.
  S9  W3: LN-6 con --generados-resolucion lee el catálogo de resolución con su candado: el registro ya re-resuelto es
      idempotente y uno sin re-resolver no.
  S10 R2-2, parte A de la enmienda 6: `decidir` reproduce la cadena con la parte A en un documento sin alcance; la fila
      resuelta por calificador queda en `resuelto_a_clase`, como en la cadena; con un alcance nuevo de prueba, (a) da lo
      mismo que la cadena (R4 con la sugerencia guardada, también con la mención que no verifica, que conserva su marca)
      y (a+) predice esos cambios.
  S11 R2-2, registro de alcance por tanda: lector del .md (clase, dos clases, rol reutilizado, sin alcance), entradas con
      la forma de rol_por_to (la misma que la de una clase de la release), los frenos (decisión desconocida, ids que no
      cierran, documento que ya tiene alcance, rol sin alcance en la release) y el catálogo de resolución con alcances
      (sha propio, rol_por_to de la release intacto más las entradas nuevas, candado del cargador).

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reresolucion_catalogo/selftest_reresolver_catalogo.py
"""
from __future__ import annotations

import copy
import json
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import reresolver_catalogo as RR       # noqa: E402  (el script, por su propio camino de imports)

ENS, E4, C = RR.ENS, RR.E4, RR.C
M = E4.modulo_modelos_r2()
RES: list[tuple[str, bool, str]] = []


def check(nombre: str, ok: bool, detalle: str = "") -> None:
    RES.append((nombre, bool(ok), detalle))
    print(f"  {'OK ' if ok else 'FALLA'} {nombre}" + ("" if ok or not detalle else f" — {detalle}"))


def frena(fn, *a) -> bool:
    try:
        fn(*a)
    except (RR.ErrorAmpliacion, RuntimeError):
        return True
    return False


TEXTO_REQ = RR.CATALOGO_REQUEST.read_text(encoding="utf-8")
SHA_REQ = RR.sha256_texto(TEXTO_REQ)
CAT_REQ = json.loads(TEXTO_REQ)


def lista(*ampl) -> dict:
    return {"formato": RR.FORMATO_AMPLIACIONES, "catalogo_request_sha256": SHA_REQ, "ampliaciones": list(ampl)}


ALTA_ID = {"operacion": "alta_id", "id": "Sujeto_prueba_selftest", "label": "Integrantes de prueba",
           "alias": ["integrante de prueba"], "padre": "Sujeto_cliente", "evidencia": [{"to": "x"}], "aprobacion": "s"}
ALTA_ALIAS = {"operacion": "alta_alias", "id": "Sujeto_alta_gerencia", "alias": "miembros de la Alta Gerencia",
              "evidencia": [{"to": "x"}], "aprobacion": "s"}


def s1():
    print("S1. componer")
    vacio = RR.componer(CAT_REQ, SHA_REQ, lista())
    check("S1a sin ampliaciones el compuesto es el request byte a byte",
          json.dumps(vacio, ensure_ascii=False, indent=1) + "\n" == TEXTO_REQ)
    cat = RR.componer(CAT_REQ, SHA_REQ, lista(ALTA_ID, ALTA_ALIAS))
    por = {s["id"]: s for s in cat["sujetos"]}
    padre = por["Sujeto_cliente"]
    nuevo = por["Sujeto_prueba_selftest"]
    check("S1b alta de un id: mismas claves que su padre, su grupo, sin rol_por_to, vigente, al final",
          list(nuevo) == list(padre) and nuevo["grupo_bloque"] == padre["grupo_bloque"] and nuevo["rol_por_to"] == []
          and nuevo["padre"] == "Sujeto_cliente" and nuevo["estado"]["valor"] == "vigente"
          and cat["sujetos"][-1]["id"] == "Sujeto_prueba_selftest")
    check("S1c alta de un alias: se agrega al final de los alias del id",
          por["Sujeto_alta_gerencia"]["alias"][-1] == "miembros de la Alta Gerencia")
    check("S1d el catálogo del request no se muta", json.dumps(CAT_REQ, ensure_ascii=False, indent=1) + "\n" == TEXTO_REQ)
    malas = {
        "formato ajeno": dict(lista(), formato="otro/1"),
        "sha ajeno": dict(lista(), catalogo_request_sha256="0" * 64),
        "sin evidencia": lista(dict(ALTA_ALIAS, evidencia=[])),
        "expresión colectiva": lista(dict(ALTA_ALIAS, alias="las entidades")),
        "alias que ya es un label": lista(dict(ALTA_ALIAS, alias="Bancos")),
        "id existente": lista(dict(ALTA_ID, id="Sujeto_banco")),
        "padre inexistente": lista(dict(ALTA_ID, padre="Sujeto_no_existe")),
        "padre que no es clase": lista(dict(ALTA_ID, padre="Sujeto_rol_alcance_capmin")),
        "operación desconocida": lista(dict(ALTA_ALIAS, operacion="baja_id")),
        "alias repetido en la misma lista": lista(ALTA_ALIAS, dict(ALTA_ALIAS, id="Sujeto_directorio")),
    }
    for nombre, l in malas.items():
        check(f"S1e frena: {nombre}", frena(RR.componer, CAT_REQ, SHA_REQ, l))


def escribir(d: Path, l: dict) -> Path:
    p = d / "ampl.json"
    p.write_text(json.dumps(l, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return p


def s2(tmp: Path) -> dict:
    print("S2. generados de resolución y candado (W2)")
    g0 = tmp / "g0"
    rep0 = RR.generar_resolucion(escribir(tmp, lista()), g0)
    c0 = E4.catalogo_resolucion_r2(g0)
    check("S2a sin ampliaciones: generados iguales a generados_r2/ y sin compuesto propio",
          all(rep0["generados_iguales_a_generados_r2"].values()) and not (g0 / RR.ARCHIVO_COMPUESTO).exists())
    check("S2b sin ampliaciones: sha del request y conjunto de ids del request",
          c0["catalogo_sha256"] == M.CATALOGO_R2_SHA256 and c0["sujetos_set"] == M.SUJETOS_R2_SET)
    cr = E4.catalogo_r2()
    check("S2c sin ampliaciones: índice, labels, rol_por_to y esqueleto iguales a los de catalogo_r2()",
          all(c0[k] == cr[k] for k in ("indice", "labels", "rol_por_to", "entrada_esqueleto")))
    g1 = tmp / "g1"
    rep1 = RR.generar_resolucion(escribir(tmp, lista(ALTA_ID, ALTA_ALIAS)), g1)
    c1 = E4.catalogo_resolucion_r2(g1)
    check("S2d con ampliaciones: el id nuevo en el conjunto y en los labels; el request entero adentro",
          "Sujeto_prueba_selftest" in c1["sujetos_set"] and "Sujeto_prueba_selftest" in c1["labels"]
          and M.SUJETOS_R2_SET < c1["sujetos_set"] and c1["catalogo_sha256"] != M.CATALOGO_R2_SHA256)
    check("S2e con ampliaciones: claves nuevas en el índice, ninguna ambigua ni cambiada",
          ["alias_exacto", "miembros de la alta gerencia", "Sujeto_alta_gerencia"] in rep1["indice_claves_nuevas"]
          and not rep1["indice_claves_que_pasan_a_ambiguas"] and not rep1["indice_claves_que_cambian_de_id"])
    check("S2f el bloque y el enum no se escriben en los generados de resolución",
          not any((g1 / n).exists() for n in RR.SOLO_DEL_REQUEST))
    check("S2g versiones: request, ampliaciones y compuesto",
          c1["versiones_catalogo"]["catalogo_request_sha256"] == M.CATALOGO_R2_SHA256
          and c1["versiones_catalogo"]["n_ampliaciones"] == 2)

    def con(nombre: str, mutar) -> bool:
        d = tmp / f"m_{nombre}"
        RR.generar_resolucion(escribir(tmp, lista(ALTA_ID, ALTA_ALIAS)), d)
        mutar(d)
        return frena(E4.catalogo_resolucion_r2, d)

    def tocar(d: Path, n: str) -> None:
        (d / n).write_text((d / n).read_text(encoding="utf-8") + " ", encoding="utf-8")

    def man(d: Path, f) -> None:
        p = d / E4.MANIFIESTO_RESOLUCION_R2
        m = json.loads(p.read_text(encoding="utf-8"))
        f(m)
        p.write_text(json.dumps(m), encoding="utf-8")

    def sin_id_del_request(d: Path) -> None:
        ids = [i for i in json.loads((d / "ids_s19_r2.json").read_text(encoding="utf-8")) if i != "Sujeto_banco"]
        t = json.dumps(ids)
        (d / "ids_s19_r2.json").write_text(t, encoding="utf-8")
        man(d, lambda m: m["archivos"].__setitem__("ids_s19_r2.json", RR.sha256_texto(t)))
    check("S2h candado: un generado cambiado", con("indice", lambda d: tocar(d, "indice_e4_r2.json")))
    check("S2i candado: la lista de ampliaciones cambiada", con("ampl", lambda d: tocar(d, RR.ARCHIVO_AMPLIACIONES)))
    check("S2j candado: el compuesto cambiado", con("comp", lambda d: tocar(d, RR.ARCHIVO_COMPUESTO)))
    check("S2k candado: el manifiesto no deriva del request de modelos_r2",
          con("req", lambda d: man(d, lambda m: m.__setitem__("catalogo_request_sha256", "0" * 64))))
    check("S2l candado: falta un id del request (el catálogo de resolución solo agrega)", con("ids", sin_id_del_request))
    check("S2m candado: formato ajeno", con("fmt", lambda d: man(d, lambda m: m.__setitem__("formato", "x/1"))))
    return {"g0": g0, "g1": g1, "c0": c0, "c1": c1}


def registro_sintetico(rels: list[dict], to: str = "cla",
                       archivo: str = "TO_clasificacion_deudores_actual.pdf") -> list[dict]:
    return [{"chunk_id": f"{to}::1.1", "to": to, "archivo": archivo, "e0_sha256_completo": "h",
             "validacion": {"entidades": [{"local_id": "e1", "type": "Obligacion", "label": "O"}], "relaciones": rels}}]


def rel(i: int, mencion, nivel: str, modelo=None) -> dict:
    return {"predicate": "aplica_a", "source": "e1", "target": None, "punto": "1.1", "indice_crudo": i,
            "sujeto_mencion": mencion, "mencion_verificada": nivel, "sujeto_id_modelo": modelo,
            "padre_sugerido": None, "padre_sugerido_crudo": None, "originales": {}}


VERS = {"catalogo_sha256": "sha_v0", "politica_sha256": "p", "perfil": "r2", "prefijo_hash": "h"}


def s3():
    print("S3. W2: un solo nombre de método")
    cat = E4.catalogo_r2()
    idx = cat["indice"]
    menciones = ["los bancos", "los operadores de cambio", "Entidades financieras comprendidas en el Grupo A",
                 "el banco", "las entidades"]
    quitar = {k for k in idx if k[0] in ("label_exacto", "alias_exacto", "label_singularizado", "id_slug")
              and k[1] in ("bancos", "operadores de cambio", "banco", "entidades financieras", "entidad financiera")}
    # sin las claves de esas menciones, la cadena las manda a cuarentena; R3 queda fuera por el rol (TO sin alcance)
    idx_sin = {k: v for k, v in idx.items() if k not in quitar}
    rels = [rel(i, m, "exacta") for i, m in enumerate(menciones)]
    sin_rol = {}
    r0 = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico(rels)), idx_sin, sin_rol, VERS)
    check("S3a sin las claves, las cinco van a cuarentena", sum(f["estado"] == "cuarentena" for f in r0["registro"]) == 5,
          str([(f["mencion"], f["estado"]) for f in r0["registro"]]))
    rol = cat["rol_por_to"]
    rr = E4.reresolver_registro(r0["registro"], idx, rol, {"cla": "TO_clasificacion_deudores_actual.pdf"}, "sha_v1")
    r1 = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico(rels)), idx, rol, VERS)
    met_rr = {f["indice_relacion"]: f["metodo"] for f in rr["filas"]}
    met_cad = {f["indice_relacion"]: f["metodo_resolucion"] for f in r1["resolucion"]}
    check("S3b reresolver_registro y la cadena escriben el mismo método en las cinco",
          met_rr == met_cad and rr["resueltas_ahora"] == 5, f"{met_rr} vs {met_cad}")
    check("S3c los métodos cubren R1 con sus criterios, R2, calificador y R3",
          {"R1_label_exacto", "R1_alias_exacto", "R2_calificador", "R3"} <= set(met_rr.values())
          and any(m.startswith("R2_") and m != "R2_calificador" for m in met_rr.values()), str(met_rr))


def s4():
    print("S4. decidir = resolver_relaciones_r2")
    cat = E4.catalogo_r2()
    idx, pref, rol_to = cat["indice"], E4._prefijos(cat["indice"]), cat["rol_por_to"]
    otro = "Sujeto_banco"
    rels = [rel(0, "Entidades financieras", "exacta", otro), rel(1, "entidad financiera", "exacta", otro),
            rel(2, "entidad financiera", "exacta"), rel(3, "Entidades financieras", "no", otro),
            rel(4, "algo no verificado", "no"), rel(5, None, "ausente", otro),
            rel(6, "Entidades financieras comprendidas en el Grupo A", "exacta"),
            rel(7, "administradores de las carteras crediticias", "tokens"), rel(8, "las entidades", "exacta"),
            rel(9, "las entidades", "exacta", otro)]
    for to, arch in (("cla", "TO_clasificacion_deudores_actual.pdf"), ("docvig", "docvig.pdf")):
        res = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico(rels, to, arch)), idx, rol_to, VERS)
        rol = (rol_to.get(arch) or {}).get("rol_id")
        malas = [f["indice_relacion"] for f in res["resolucion"]
                 if RR.decidir(f, None, idx, pref, rol) != {c: f[c] for c in RR.CAMPOS_DECISION}]
        check(f"S4 {to} ({'con' if rol else 'sin'} alcance): decidir reproduce las diez decisiones", not malas, str(malas))


def s5(g: dict):
    print("S5. (a+)")
    cat0, cat1 = E4.catalogo_r2(), g["c1"]
    rels = [rel(0, "los miembros de la Alta Gerencia", "exacta", "Sujeto_directorio"),
            rel(1, "Entidades financieras", "exacta", "Sujeto_banco"), rel(2, "los integrantes de prueba", "exacta")]
    res = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico(rels)), cat0["indice"], cat0["rol_por_to"],
                                    {**VERS, "catalogo_sha256": cat0["catalogo_sha256"]})
    am = RR.camino_a_mas(res["resolucion"], res["registro"], cat0, cat1, {"cla": "TO_clasificacion_deudores_actual.pdf"})
    tipos = {c["indice_relacion"]: (c["tipo"], c["antes"]["resuelto_a"], c["despues"]["resuelto_a"]) for c in am["cambian"]}
    check("S5a reproduce la decisión guardada", am["reproduce_la_decision_guardada"])
    check("S5b el alias nuevo gana a la sugerencia del modelo (destino) y el id nuevo resuelve la cuarentena",
          tipos == {0: ("destino", "Sujeto_directorio", "Sujeto_alta_gerencia"),
                    2: ("destino", None, "Sujeto_prueba_selftest")}, str(tipos))


def s6():
    print("S6. registro acumulado")
    base = {"to": "cla", "e0_sha256_completo": "h", "punto": "1", "predicado": "aplica_a", "mencion": "m",
            "mencion_verificada": "exacta", "sujeto_id_modelo": None, "motivo": "sin_match", "calificador": None,
            "catalogo_sha256": "v0", "catalogo_sha256_resolucion": None, "resuelto_a": None, "metodo": None}
    A = dict(base, chunk_id="cla::1", indice_relacion=0, estado="resuelto", resuelto_a="Sujeto_x", metodo="R1_alias_exacto",
             catalogo_sha256_resolucion="v1", id_nodo="Sujeto_propuesto_a")
    B = dict(base, chunk_id="cla::2", indice_relacion=0, estado="cuarentena", id_nodo="Sujeto_propuesto_b")
    Bb = dict(B, catalogo_sha256="v1")
    D = dict(base, chunk_id="cla::3", indice_relacion=0, estado="cuarentena", id_nodo="Sujeto_propuesto_d",
             catalogo_sha256="v1")
    res_b = [{**{k: base[k] for k in ("to", "e0_sha256_completo")}, "chunk_id": "cla::1", "indice_relacion": 0,
              "resuelto_a": "Sujeto_x", "metodo_resolucion": "R1_alias_exacto"},
             {"to": "cla", "e0_sha256_completo": "h", "chunk_id": "cla::2", "indice_relacion": 0, "resuelto_a": None,
              "metodo_resolucion": "cuarentena"}]
    cat_res = {"catalogo_sha256": "v1"}
    ac = RR.registro_acumulado([A, B], {"cambian": []}, [Bb, D], res_b, cat_res)
    c = ac["control"]
    por = {(f["chunk_id"]): f for f in ac["filas"]}
    check("S6a la fila resuelta conserva la versión de entrada y lleva la de resolución",
          por["cla::1"]["catalogo_sha256"] == "v0" and por["cla::1"]["catalogo_sha256_resolucion"] == "v1")
    check("S6b la que sigue en cuarentena es la de (b) salvo la versión; el destino de la resuelta es el de (b)",
          c["1_sin_resolver_iguales_a_b_salvo_version"] and c["2_destino_de_las_resueltas_igual_a_b"]
          and por["cla::2"]["catalogo_sha256"] == "v0")
    check("S6c la fila nueva de (b) se agrega y se lista", c["3_filas_de_b_fuera_del_anterior"] == [["cla", "cla::3", "h", 0]]
          and len(ac["filas"]) == 3)
    ac2 = RR.registro_acumulado([A, B], {"cambian": []}, [dict(Bb, motivo="ambiguo"), D], res_b, cat_res)
    check("S6d una fila sin resolver distinta de (b) se detecta", not ac2["control"]["1_sin_resolver_iguales_a_b_salvo_version"])
    res_b2 = [dict(res_b[0], resuelto_a="Sujeto_y"), res_b[1]]
    ac3 = RR.registro_acumulado([A, B], {"cambian": []}, [Bb, D], res_b2, cat_res)
    check("S6e un destino distinto del de (b) se detecta", not ac3["control"]["2_destino_de_las_resueltas_igual_a_b"])


def s7():
    print("S7. contraste")
    def n(i, t="Sujeto", **p):
        return {"id": i, "type": t, "label": i, "properties": p, "provenance": {}, "provenances": []}

    def e(s, r, t, cid):
        return {"source": s, "relation": r, "target": t, "provenance": {"chunk_id": cid}, "provenances": [{"chunk_id": cid}]}
    kg0 = {"nodes": [n("Obligacion_o", "Obligacion"), n("Sujeto_propuesto_a", nivel="propuesto"), n("Sujeto_cliente")],
           "edges": [e("Obligacion_o", "aplica_a", "Sujeto_propuesto_a", "cla::1"),
                     e("Sujeto_propuesto_a", "padre_sugerido", "Sujeto_cliente", "cla::1")]}
    kg1 = {"nodes": [n("Obligacion_o", "Obligacion"), n("Sujeto_cliente"), n("Sujeto_x")],
           "edges": [e("Obligacion_o", "aplica_a", "Sujeto_x", "cla::1"), e("Sujeto_x", "subclase_de", "Sujeto_cliente", "")]}
    pred = {"cambios_de_destino": [["cla::1", "Sujeto_propuesto_a", "Sujeto_x", "a"]],
            "propuestos_que_desaparecen": ["Sujeto_propuesto_a"], "ids_nuevos": ["Sujeto_x"], "alias_nuevos_en": [],
            "a_mas_por_procedencia": []}
    c = RR.contrastar(pred, kg0, kg1)
    check("S7a mudanza, propuesto que desaparece e id nuevo con su esqueleto: todo explicado",
          not c["no_explicado"] and c["procedencias_de_sujeto_explicadas"] == 2, json.dumps(c["no_explicado"]))
    kg2 = copy.deepcopy(kg1)
    kg2["edges"].append(e("Obligacion_o", "regula", "Sujeto_cliente", "cla::9"))
    c2 = RR.contrastar(pred, kg0, kg2)
    check("S7b una arista no predicha queda sin explicar", any("arista_agregada" in x for x in c2["no_explicado"]))
    c3 = RR.contrastar(dict(pred, cambios_de_destino=[]), kg0, kg1)
    check("S7c una mudanza no predicha queda sin explicar", any("procedencia_agregada" in x for x in c3["no_explicado"]))


def s8(g: dict):
    print("S8. W1: conjunto de ids de resolución en las redirecciones y en E2")
    c1 = g["c1"]
    check("S8a sujetos_de_resolucion: sin el catálogo de resolución, SUJETOS_R2_SET; con él, el suyo",
          ENS.sujetos_de_resolucion(E4.catalogo_r2(), M) is M.SUJETOS_R2_SET
          and ENS.sujetos_de_resolucion(c1, M) == c1["sujetos_set"])
    man = ENS.MC.cargar(RR.RAIZ / "data" / "experiment" / "reextraccion_v2" / "manifiestos" / "tanda0_ens_diez_r2b.json")
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    plan = ENS.plan_redirecciones_r2(man, perfil, Path("e"), Path("s"), c1, M)
    v = {(m.__name__, a): x for m, a, x in plan}
    check("S8b las redirecciones llevan el esqueleto y el conjunto de ids del catálogo de resolución",
          v[("r1_invariantes", "SUJETOS_CATALOGO_SET")] == c1["sujetos_set"]
          and v[("r1_comun", "CATALOGO_PATH")] == c1["entrada_esqueleto_path"])
    plan0 = ENS.plan_redirecciones_r2(man, perfil, Path("e"), Path("s"), E4.catalogo_r2(), M)
    v0 = {(m.__name__, a): x for m, a, x in plan0}
    check("S8c sin el catálogo de resolución, las redirecciones de siempre",
          v0[("r1_invariantes", "SUJETOS_CATALOGO_SET")] is M.SUJETOS_R2_SET)
    prov = {"to": "cla", "archivo": "a.pdf", "punto": "1.1", "rol_documental": "punto_propio"}
    r = rel(0, "los integrantes de prueba", "exacta")
    r.update(sujeto_id_resuelto="Sujeto_prueba_selftest", metodo_resolucion="R1_alias_exacto", provenance=prov)
    regs = [{"chunk_id": "cla::1.1", "to": "cla", "archivo": "a.pdf", "e0_sha256_completo": "h", "error": None,
             "validacion": {"entidades": [{"local_id": "e1", "type": "Obligacion", "label": "O",
                                           "properties": {"descripcion": "d", "tipo": "otra"}, "provenance": prov}],
                            "relaciones": [r], "rechazos": []}}]
    ch = [{"id": "cla::1.1"}]
    sin = ENS.e2_lib.ensamblar_r2(ch, copy.deepcopy(regs), c1["labels"], M.SUJETOS_R2_SET, M.firma_r2,
                                  M.TIPOS_ENTIDAD, M.PREDICADOS, [])
    con = ENS.e2_lib.ensamblar_r2(ch, copy.deepcopy(regs), c1["labels"], ENS.sujetos_de_resolucion(c1, M), M.firma_r2,
                                  M.TIPOS_ENTIDAD, M.PREDICADOS, [])
    check("S8d sin el conjunto de resolución, E2 rechaza la relación al id nuevo (y no deja fila)",
          [x["motivo"] for x in sin["rechazos_e2"]] == ["sujeto_id_fuera_de_catalogo"]
          and not any(e["relation"] == "aplica_a" for e in sin["edges"]))
    check("S8e con el conjunto de resolución, entra con el nodo del id nuevo",
          not con["rechazos_e2"] and any(e["relation"] == "aplica_a" and e["target"] == "Sujeto_prueba_selftest"
                                         for e in con["edges"]))


def s9(tmp: Path, g: dict):
    print("S9. W3: LN-6 con los generados de resolución")
    sys.path.insert(0, str(RR.RAIZ / "scripts"))
    import regression_kg as RK          # noqa: PLC0415
    fila = {"to": "cla", "chunk_id": "cla::1.1", "e0_sha256_completo": "h", "indice_relacion": 0,
            "mencion": "los integrantes de prueba", "mencion_verificada": "exacta", "padre_sugerido": None,
            "estado": "cuarentena", "id_nodo": "Sujeto_propuesto_x", "resuelto_a": None, "metodo": None,
            "calificador": None, "catalogo_sha256": "v0", "catalogo_sha256_resolucion": None}
    d = tmp / "registro_ln6"
    d.mkdir()
    nodo = {"id": "Sujeto_propuesto_x", "type": "Sujeto", "label": "x", "properties": {"nivel": "propuesto"},
            "provenance": {"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "1.1"},
            "provenances": [{"to": "cla", "archivo": "TO_clasificacion_deudores_actual.pdf", "punto": "1.1"}]}
    G = RK.Grafo({"nodes": [nodo], "edges": []})

    def ln6(filas, gen):
        RR.escribir_jsonl(d / RK.REGISTRO_NO_MAPEADOS, filas)
        ctx = RK.Contexto(G, RK.Catalogo({"version": "r2", "clases": [], "roles": []}, "c", "0" * 64), 3, "flaggeada",
                          perfil="r2", registro_dir=d, generados_resolucion=gen)
        return RK.t_ln_6(ctx)
    r_req = ln6([fila], None)
    r_sin = ln6([fila], g["g1"])
    rr = E4.reresolver_registro([fila], g["c1"]["indice"], g["c1"]["rol_por_to"],
                                {"cla": "TO_clasificacion_deudores_actual.pdf"}, g["c1"]["catalogo_sha256"])
    r_con = ln6(rr["filas"], g["g1"])
    check("S9a sin la opción, LN-6 lee el request: la fila no resuelve y es idempotente", r_req["estado"] == "resuelto")
    check("S9b con la opción y el registro sin re-resolver, LN-6 lo detecta", r_sin["estado"] == "persiste",
          r_sin["detalle"])
    check("S9c con la opción y el registro re-resuelto, idempotente", r_con["estado"] == "resuelto"
          and "de resolución" in r_con["detalle"], r_con["detalle"])
    malo = tmp / "g_malo"
    RR.generar_resolucion(escribir(tmp, lista(ALTA_ID)), malo)
    (malo / "indice_e4_r2.json").write_text("[]\n", encoding="utf-8")
    check("S9d con la opción, el candado del catálogo de resolución frena", frena(ln6, rr["filas"], malo))


def s10():
    print("S10. parte A: decidir, calificador y alcance nuevo")
    cat = E4.catalogo_r2()
    idx, pref, rol_to = cat["indice"], E4._prefijos(cat["indice"]), cat["rol_por_to"]
    m = "Sujeto_sujeto_regulado"
    rels = [rel(0, "las entidades", "exacta", m), rel(1, None, "ausente", m), rel(2, "los obligados", "no", m),
            rel(3, "Entidades financieras", "exacta", m), rel(4, "administradores de las carteras crediticias", "exacta", m),
            rel(5, "Entidades financieras comprendidas en el Grupo A", "exacta")]
    vers = {**VERS, "catalogo_sha256": cat["catalogo_sha256"]}
    res = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico(rels, "docvig", "docvig.pdf")), idx, rol_to, vers,
                                    parte_a=True)
    malas = [f["indice_relacion"] for f in res["resolucion"]
             if RR.decidir(f, None, idx, pref, None, True) != {c: f[c] for c in RR.CAMPOS_DECISION}]
    check("S10a decidir reproduce la cadena con la parte A en un documento sin alcance", not malas, str(malas))
    check("S10b la cadena manda a cuarentena el colectivo, la sin mención y la no verificada",
          [f["metodo_resolucion"] for f in res["resolucion"]][:3] == ["cuarentena"] * 3)
    idx_sin = {k: v for k, v in idx.items() if k[1] not in ("entidades financieras", "entidad financiera")}
    r_cal = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico([rels[5]])), idx_sin, rol_to, vers)
    rr_cal = E4.reresolver_registro(r_cal["registro"], idx, rol_to, {"cla": "TO_clasificacion_deudores_actual.pdf"}, "v1")
    r_cad = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico([rels[5]])), idx, rol_to, vers)
    check("S10c el calificador deja la fila en resuelto_a_clase, como la cadena (decisión 4)",
          rr_cal["filas"][0]["estado"] == "resuelto_a_clase" == r_cad["registro"][0]["estado"]
          and rr_cal["filas"][0]["metodo"] == "R2_calificador", str(rr_cal["filas"][0]["estado"]))
    nuevo = dict(rol_to, **{"docvig.pdf": RR.entradas_de_alcance(
        {"tandas": {"p": [{"to": "docvig", "archivo": "docvig.pdf", "decision": "clase",
                           "ids": ["Sujeto_entidad_financiera"]}]}}, rol_to, cat["labels"])["docvig.pdf"]})
    cat0 = {**cat}
    cat1 = {**cat, "rol_por_to": nuevo, "catalogo_sha256": "sha_alcance"}
    aa = RR.camino_a(res["registro"], cat1, {"docvig": "docvig.pdf"})
    cadena = E4.resolver_relaciones_r2(copy.deepcopy(registro_sintetico(rels, "docvig", "docvig.pdf")), idx, nuevo,
                                       vers, parte_a=True)
    dest_a = {f["indice_relacion"]: (f["resuelto_a"], f["metodo"]) for f in aa["filas"] if f["estado"] != "cuarentena"}
    dest_b = {f["indice_relacion"]: (f["resuelto_a"], f["metodo_resolucion"]) for f in cadena["resolucion"]}
    check("S10d con el alcance nuevo, (a) resuelve las tres como la cadena (R4) y es idempotente",
          aa["resueltas_ahora"] == 3 and aa["idempotente"] and all(dest_a[i] == dest_b[i] for i in (0, 1, 2)),
          f"{dest_a} | {dest_b}")
    check("S10e la resuelta con la mención que no verifica conserva su marca",
          next(f for f in aa["filas"] if f["indice_relacion"] == 2)["mencion_verificada"] == "no")
    am = RR.camino_a_mas(res["resolucion"], res["registro"], cat0, cat1, {"docvig": "docvig.pdf"}, parte_a=True)
    check("S10f (a+) reproduce la decisión guardada con la parte A y predice las tres del alcance nuevo",
          am["reproduce_la_decision_guardada"]
          and sorted(c["indice_relacion"] for c in am["cambian"] if c["tipo"] == "destino") == [0, 1, 2], str(am["cambian_por_tipo"]))


MD_PRUEBA = """# Registro de prueba

## Tanda 7 — prueba

| TO | título | decisión | id(s) del catálogo | base | pasaje |
|---|---|---|---|---|---|
| doc_a | A | clase | `Sujeto_banco` | pasaje | x |
| doc_b | B | clase (dos) | `Sujeto_entidad_financiera`, `Sujeto_banco` | pasaje | x |
| doc_c | C | rol reutilizado | `Sujeto_rol_alcance_capmin` | sección | x |
| doc_d | D | sin alcance declarado | — | no hay pasaje | x |

## Candidatos (no decididos)

| estado | TO | clase |
|---|---|---|
| candidato | doc_e | `Sujeto_banco` |
"""


def s11(tmp: Path):
    print("S11. registro de alcance por tanda")
    cat = E4.catalogo_r2()
    md = tmp / "registro.md"
    md.write_text(MD_PRUEBA, encoding="utf-8")
    reg = RR.leer_registro_alcance(md)
    filas = reg["tandas"]["7"]
    check("S11a lector: cuatro filas de la tanda, los candidatos fuera",
          list(reg["tandas"]) == ["7"] and [(f["to"], f["decision"], len(f["ids"])) for f in filas]
          == [("doc_a", "clase", 1), ("doc_b", "clase", 2), ("doc_c", "rol_reutilizado", 1), ("doc_d", "sin_alcance", 0)])
    ent = RR.entradas_de_alcance(reg, cat["rol_por_to"], cat["labels"])
    ref = cat["rol_por_to"]["ctacte.pdf"]                      # la release mapea ctacte a la clase Sujeto_banco
    capmin = next(e for e in cat["rol_por_to"].values() if e.get("rol_id") == "Sujeto_rol_alcance_capmin")
    check("S11b entradas: una clase como en la release, dos clases sin rol, el rol reutilizado igual a su entrada, "
          "sin alcance sin entrada",
          list(ent) == ["doc_a.pdf", "doc_b.pdf", "doc_c.pdf"] and dict(ent["doc_a.pdf"]) == dict(ref)
          and ent["doc_b.pdf"]["rol_id"] is None and ent["doc_b.pdf"]["clase_ids"] == ["Sujeto_entidad_financiera", "Sujeto_banco"]
          and dict(ent["doc_c.pdf"]) == dict(capmin))
    malos = {"decisión desconocida": MD_PRUEBA.replace("| clase | `Sujeto_banco` |", "| quizás | `Sujeto_banco` |"),
             "ids que no cierran": MD_PRUEBA.replace("clase (dos)", "clase"),
             "columnas de menos": MD_PRUEBA.replace("| doc_d | D | sin alcance declarado | — | no hay pasaje | x |", "| doc_d | D |")}
    for nombre, texto in malos.items():
        (tmp / "malo.md").write_text(texto, encoding="utf-8")
        check(f"S11c frena: {nombre}", frena(RR.leer_registro_alcance, tmp / "malo.md"))
    ya = {"tandas": {"7": [{"to": "ctacte", "archivo": "ctacte.pdf", "decision": "clase", "ids": ["Sujeto_banco"]}]}}
    sin_rol = {"tandas": {"7": [{"to": "x", "archivo": "x.pdf", "decision": "rol_reutilizado",
                                 "ids": ["Sujeto_entidad_financiera"]}]}}
    check("S11d frena: el documento ya tiene alcance (solo agrega)",
          frena(RR.entradas_de_alcance, ya, cat["rol_por_to"], cat["labels"]))
    check("S11e frena: un rol reutilizado que no es un rol", frena(RR.entradas_de_alcance, sin_rol, cat["rol_por_to"], cat["labels"]))
    g = tmp / "g_alcance"
    rep = RR.generar_resolucion(escribir(tmp, lista()), g, md)
    c = E4.catalogo_resolucion_r2(g)
    check("S11f catálogo de resolución con alcances: sha propio, n_alcances 3, rol_por_to = release + las tres",
          c["catalogo_sha256"] != M.CATALOGO_R2_SHA256 and rep["manifiesto"]["n_alcances"] == 3
          and rep["manifiesto"]["n_altas"] == 0
          and list(c["rol_por_to"]) == list(cat["rol_por_to"]) + ["doc_a.pdf", "doc_b.pdf", "doc_c.pdf"]
          and all(c["rol_por_to"][k] == v for k, v in cat["rol_por_to"].items()))
    req = E4.catalogo_r2()
    sin_deriva = lambda e: {k: v for k, v in e.items() if k != "deriva_de"}  # noqa: E731
    check("S11g con alcances, el índice, los labels y el esqueleto son los del request (el esqueleto, salvo de qué "
          "catálogo deriva)", c["indice"] == req["indice"] and c["labels"] == req["labels"]
          and sin_deriva(c["entrada_esqueleto"]) == sin_deriva(req["entrada_esqueleto"]))


def main() -> int:
    s1()
    with tempfile.TemporaryDirectory(prefix="selftest_reresolver_") as t:
        tmp = Path(t)
        g = s2(tmp)
        s3()
        s4()
        s5(g)
        s6()
        s7()
        s8(g)
        s9(tmp, g)
        s10()
        s11(tmp)
    ok = sum(1 for _, o, _ in RES if o)
    print(f"\nselftest_reresolver_catalogo: {ok}/{len(RES)} OK")
    return 0 if ok == len(RES) else 1


if __name__ == "__main__":
    raise SystemExit(main())
