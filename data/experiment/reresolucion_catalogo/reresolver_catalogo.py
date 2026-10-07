"""U-RERESOL-CAT, R2 — re-resolución de los sujetos cuando crece el catálogo de resolución (USD 0, sin API ni Neo4j).

Dos catálogos (freno R1, §2; decisión 1 de la autora): el del request de E1 (`catalogo_unico/catalogo_sujetos_r2.json`,
fijo por release, con sus candados en modelos_r2 y prompt_r2b) y el de resolución, que es el del request más una lista de
ampliaciones que solo agrega: alta de un id con su padre, o alta de un alias de un id que ya existe. El catálogo de
resolución lo lee el código (E4, E2, merge entre TOs, esqueleto, S19 y la suite); el bloque del prefijo, el enum y el
tool schema salen solo del catálogo del request, así que ningún request de E1 cambia.

El alcance de los documentos nuevos (enmienda 4 al protocolo, §2; R2-2) entra por el registro de alcance por tanda
(`catalogo_unico/registro_alcance_por_tanda.md`), que solo agrega: una entrada por documento con alcance (clase o rol
reutilizado) que el catálogo de resolución suma al `rol_por_to` de la release. La regla de la parte A de la enmienda 6 a
L-ESQ-R2 (firmada el 06/10/2026) corre en r2b: en un documento sin alcance, la expresión colectiva y la relación sin
mención o con mención que no verifica van a cuarentena con la sugerencia guardada (r1_e4.resolver_relaciones_r2).

Se corre desde la raíz de una COPIA del repo (CLAUDE.md §4.k y §4.l). Subcomandos:

  registro --md R.md --salida J.json
      Lee el registro de alcance por tanda tal como está y escribe su forma legible por código: las filas por tanda y, por
      tanda, las entradas con la forma de rol_por_to_r2.json y los documentos sin alcance declarado.

  componer --ampliaciones A.json --salida G [--registro-alcance R.md] [--tandas 1,2]
      Compone el catálogo de resolución y escribe en G sus generados de resolución (índice de E4, labels de E2,
      rol_por_to, entrada del esqueleto, ids de S19 y catálogo de la suite), la lista de ampliaciones, el catálogo
      compuesto (solo si hay ampliaciones o alcances) y el manifiesto con los tres sha256 (request, ampliaciones y
      compuesto), que es el candado que lee r1_e4.catalogo_resolucion_r2. Con el registro, el compuesto lleva sus
      entradas (clave `alcance_de_resolucion`) y el rol_por_to de resolución las suma al de la release. Sin ampliaciones
      ni alcances, el compuesto es el del request y los generados salen byte a byte iguales a los de generados_r2/.
      Escribe además G/reporte_composicion.json, fuera del candado: las claves del índice de E4 que se agregan, que pasan
      a ambiguas o que cambian de id, y las entradas de alcance nuevas.

  correr --manifiesto M --entrada E --e0-r2 D --anterior A --generados-resolucion G --salida S
         [--generados-anterior G0] [--sin-cola] [--sin-gate]
      A es el directorio r2/ del ensamblado anterior; G0, los generados de resolución con que se armó (sin la opción,
      los del request). Corre:
        (a)  r1_e4.reresolver_registro sobre el registro anterior con el catálogo de resolución: las filas en
             cuarentena con la mención verificada que pasan a resuelto;
        (a+) la regla de decisión de r1_e4.resolver_relaciones_r2 re-aplicada a todas las relaciones de
             resolucion_sujetos.jsonl, con el catálogo anterior (control: reproduce la decisión guardada) y con el de
             resolución: las relaciones que cambian de destino, de método, de calificador o de marca de desacuerdo,
             también las que resolvió el modelo (R1 le gana) y las del registro que no están en cuarentena;
        (b)  el ensamblado entero desde el crudo guardado, con el catálogo de resolución, por el camino del ensamblador
             (ensamblar_tanda0.ensamblar_manifiesto_r2 con el parámetro cat_resolucion, W1), en S/r2/.
      Contrasta (b) contra lo que predicen (a), (a+) y el esqueleto (procedencias de sujeto, nodos, aristas y archivos);
      la resolución de (b) contra la de (a+), relación por relación; y el registro de (b) contra el acumulado. El
      registro acumulado (el anterior actualizado por (a) y (a+), más las filas que (b) agregue) reemplaza al de la cadena
      en S/r2/no_mapeados_sujetos.jsonl, y el de la cadena queda en S/r2/no_mapeados_sujetos_cadena.jsonl. Después,
      salvo --sin-gate: shapes r2 con los ids de S19 y la entrada del esqueleto de G, y la suite del perfil con el
      catálogo de la suite de G y LN-6 sobre G (opción --generados-resolucion, W3), sobre la salida y sobre la anterior.
      Escribe S/reporte_reresolucion.json. Lo que ningún camino explica va a `no_explicado` y el código de salida es 1.

Las rutas que se escriben en los reportes son relativas a la raíz (o al directorio de salida): la salida va dentro de la
copia para que ningún reporte lleve una ruta absoluta.
"""
from __future__ import annotations

import argparse
import contextlib
import copy
import hashlib
import json
import os
import re
import subprocess
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ENS          # noqa: E402  (el ensamblador, con W1; agrega al path los módulos de la cadena)
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "catalogo_unico" / "code"))
import generar_desde_catalogo as GEN    # noqa: E402

E4 = ENS.E4
C = ENS.C
CATALOGO_REQUEST = RAIZ / "data" / "experiment" / "catalogo_unico" / "catalogo_sujetos_r2.json"
GENERADOS_REQUEST = RAIZ / "data" / "experiment" / "catalogo_unico" / "generados_r2"
FORMATO_AMPLIACIONES = "ampliaciones_resolucion_r2/1"
ARCHIVO_AMPLIACIONES = "ampliaciones_resolucion_r2.json"
ARCHIVO_COMPUESTO = "catalogo_resolucion_r2.json"
SOLO_DEL_REQUEST = ("bloque_catalogo_r2.txt", "enums_tool_schema_r2.json")
GENERADOR = "data/experiment/reresolucion_catalogo/reresolver_catalogo.py"
OPERACIONES = ("alta_id", "alta_alias")
REGISTRO_ALCANCE_MD = RAIZ / "data" / "experiment" / "catalogo_unico" / "registro_alcance_por_tanda.md"
FORMATO_REGISTRO_ALCANCE = "registro_alcance_por_tanda/1"
DECISIONES_ALCANCE = (("clase", "clase"), ("rol reutilizado", "rol_reutilizado"), ("sin alcance declarado", "sin_alcance"))
VERIFICADAS = ("exacta", "tokens")
REGISTRO = "no_mapeados_sujetos.jsonl"
REGISTRO_CADENA = "no_mapeados_sujetos_cadena.jsonl"
RESOLUCION = "resolucion_sujetos.jsonl"
CAMPOS_VERSION = ("catalogo_sha256", "catalogo_sha256_resolucion")
CAMPOS_DECISION = ("resuelto_a", "metodo_resolucion", "desacuerdo_regla_modelo", "regla_texto", "id_regla_texto",
                   "criterios", "calificador")
RELACIONES_ESQUELETO = ("subclase_de", "instancia_de", "parte_de", "miembro_de")
# archivos de la salida del ensamblado que una ampliación del catálogo de sujetos puede cambiar
ARCHIVOS_QUE_CAMBIAN = ("kg.json", REGISTRO, RESOLUCION, "reporte_ensamblado_r2.json",
                        "propuestos_descartados_aristas_quitadas.jsonl")


class ErrorAmpliacion(RuntimeError):
    """La lista de ampliaciones no cumple su formato o una regla del crecimiento."""


class ErrorRegistroAlcance(RuntimeError):
    """El registro de alcance por tanda no cumple su formato o choca con el alcance de la release."""


# --------------------------------------------------------------------------------------------------------------- #
# utilidades                                                                                                       #
# --------------------------------------------------------------------------------------------------------------- #
def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha256_texto(s: str) -> str:
    return sha256_bytes(s.encode("utf-8"))


def sha256_path(p: Path) -> str:
    return sha256_bytes(Path(p).read_bytes())


def json_texto(obj) -> str:
    return json.dumps(obj, ensure_ascii=False, indent=1) + "\n"


def leer_jsonl(p: Path) -> list[dict]:
    return [json.loads(x) for x in Path(p).read_text(encoding="utf-8").splitlines() if x.strip()]


def escribir_jsonl(p: Path, filas: list[dict]) -> None:
    """Como `wl` del ensamblador: una fila por línea, sin indentar."""
    with Path(p).open("w", encoding="utf-8") as f:
        for r in filas:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")


def ruta(p) -> str:
    """Relativa a la raíz si está adentro; si no, el nombre con el marcador <fuera>."""
    p = Path(p).resolve()
    try:
        return str(p.relative_to(RAIZ.resolve()))
    except ValueError:
        return f"<fuera>/{p.name}"


def clave(f: dict) -> tuple:
    return (f["to"], f["chunk_id"], f.get("e0_sha256_completo"), f["indice_relacion"])


def ordenado(c: Counter) -> dict:
    return dict(sorted(c.items(), key=lambda kv: (-kv[1], str(kv[0]))))


# --------------------------------------------------------------------------------------------------------------- #
# registro de alcance por tanda (enmienda 4 al protocolo, §2 y §4; R2-2)                                           #
# --------------------------------------------------------------------------------------------------------------- #
def leer_registro_alcance(md: Path) -> OrderedDict:
    """El registro de alcance por tanda, leído tal como está: las filas de las tablas bajo «## Tanda N …», con las
    columnas TO | título | decisión | id(s) del catálogo | base | pasaje. Decisión: «clase» o «clase (dos)» (una o dos
    clases del catálogo), «rol reutilizado» (un rol que ya tiene alcance en la release) o «sin alcance declarado» (sin
    ids). El archivo del documento es `<TO>.pdf`, la convención de `escalado_prep/pdfs/` y de las claves de rol_por_to
    de los documentos fuera del subset. Las tablas que no están bajo un encabezado de tanda (los candidatos) no entran.
    Frena (ErrorRegistroAlcance) ante una fila que no cumple."""
    texto = Path(md).read_text(encoding="utf-8")
    tandas: OrderedDict = OrderedDict()
    tanda = None
    for n, linea in enumerate(texto.splitlines(), 1):
        m = re.match(r"^## Tanda (\S+)", linea)
        if m:
            tanda = m.group(1)
            tandas.setdefault(tanda, [])
            continue
        if linea.startswith("## "):
            tanda = None
            continue
        if tanda is None or not linea.startswith("|") or linea.startswith("|---"):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if celdas and celdas[0] == "TO":
            continue
        if len(celdas) != 6:
            raise ErrorRegistroAlcance(f"línea {n}: {len(celdas)} columnas (esperadas 6)")
        to, titulo, decision, ids_txt, base, _pasaje = celdas
        tipo = next((v for k, v in DECISIONES_ALCANCE if decision.startswith(k)), None)
        ids = re.findall(r"`(Sujeto_[A-Za-z0-9_]+)`", ids_txt)
        if tipo is None:
            raise ErrorRegistroAlcance(f"línea {n}: decisión {decision!r} desconocida")
        if (tipo == "clase" and len(ids) != (2 if "(dos)" in decision else 1)) or \
                (tipo == "rol_reutilizado" and len(ids) != 1) or (tipo == "sin_alcance" and ids):
            raise ErrorRegistroAlcance(f"línea {n}: {len(ids)} ids para la decisión {decision!r}")
        tandas[tanda].append(OrderedDict([("to", to), ("archivo", f"{to}.pdf"), ("titulo", titulo),
                                          ("decision", tipo), ("ids", ids), ("base", base), ("linea", n)]))
    return OrderedDict([("formato", FORMATO_REGISTRO_ALCANCE), ("fuente", ruta(md)),
                        ("fuente_sha256", sha256_texto(texto)), ("tandas", tandas)])


def entradas_de_alcance(registro: dict, rol_por_to: dict, labels: dict, tandas=None) -> OrderedDict:
    """archivo → entrada con la forma de rol_por_to_r2.json (generar_desde_catalogo.generar_rol_por_to): una clase o
    dos, la de un mapeo a clase (`rol_id` es la clase si es una, None si son dos); rol reutilizado, la entrada del rol en
    el rol_por_to de la release, sin cambios. Sin alcance declarado, sin entrada. Solo agrega: frena si el documento ya
    tiene alcance o aparece dos veces, si un id no es del catálogo o no es del nivel que pide la decisión, o si el rol no
    tiene entrada en la release."""
    roles = {}
    for e in rol_por_to.values():
        if e.get("rol_id") and (labels.get(e["rol_id"]) or {}).get("nivel") == "rol":
            roles.setdefault(e["rol_id"], e)
    out: OrderedDict = OrderedDict()
    for tanda, filas in registro["tandas"].items():
        if tandas is not None and tanda not in tandas:
            continue
        for f in filas:
            if f["decision"] == "sin_alcance":
                continue
            a = f["archivo"]
            if a in rol_por_to or a in out:
                raise ErrorRegistroAlcance(f"{f['to']}: el documento ya tiene alcance (solo agrega)")
            for i in f["ids"]:
                nivel = (labels.get(i) or {}).get("nivel")
                if nivel is None or (nivel == "rol") != (f["decision"] == "rol_reutilizado"):
                    raise ErrorRegistroAlcance(f"{f['to']}: {i} no es un id de nivel válido para «{f['decision']}»")
            if f["decision"] == "rol_reutilizado":
                if f["ids"][0] not in roles:
                    raise ErrorRegistroAlcance(f"{f['to']}: el rol {f['ids'][0]} no tiene alcance en la release")
                out[a] = copy.deepcopy(roles[f["ids"][0]])
            else:
                lbl = [labels[i]["label"] for i in f["ids"]]
                out[a] = OrderedDict([("rol_id", f["ids"][0] if len(f["ids"]) == 1 else None),
                                      ("clase_ids", list(f["ids"])), ("label", " / ".join(lbl)),
                                      ("miembros_ids", list(f["ids"])), ("miembros_labels", lbl)])
    return out


def registro_legible(md: Path) -> OrderedDict:
    """La forma legible por código del registro: las filas por tanda y, por tanda, sus entradas de rol_por_to (contra el
    rol_por_to y los labels del catálogo del request) y los documentos sin alcance declarado."""
    reg = leer_registro_alcance(md)
    cat = E4.catalogo_r2()
    out = OrderedDict(reg)
    out["rol_por_to_por_tanda"] = OrderedDict((t, entradas_de_alcance(reg, cat["rol_por_to"], cat["labels"], [t]))
                                              for t in reg["tandas"])
    out["sin_alcance_declarado_por_tanda"] = OrderedDict(
        (t, [f["to"] for f in filas if f["decision"] == "sin_alcance"]) for t, filas in reg["tandas"].items())
    return out


# --------------------------------------------------------------------------------------------------------------- #
# componer: el catálogo de resolución y sus generados                                                              #
# --------------------------------------------------------------------------------------------------------------- #
def _formas(texto: str) -> set[str]:
    """Las formas con que una mención igualaría a `texto` por R1: normalizada y sin el artículo inicial."""
    return {C.norm(texto), E4._sin_articulo(texto)}


def componer(cat_request: dict, sha_request: str, ampl: dict) -> dict:
    """El catálogo de resolución: el del request más las ampliaciones, en su orden. Frena (ErrorAmpliacion) si la
    lista no es del catálogo del request, si una ampliación no trae evidencia y aprobación, si un label o un alias es una
    expresión colectiva de la lista de R3 (R1 se evalúa antes y le ganaría: freno R1, §5), si choca con un label o un
    alias que ya existe, o si el id o el padre no cumplen."""
    if ampl.get("formato") != FORMATO_AMPLIACIONES:
        raise ErrorAmpliacion(f"formato {ampl.get('formato')!r} ≠ {FORMATO_AMPLIACIONES}")
    if ampl.get("catalogo_request_sha256") != sha_request:
        raise ErrorAmpliacion("la lista de ampliaciones no es del catálogo del request vigente")
    cat = copy.deepcopy(cat_request)
    por_id = {s["id"]: s for s in cat["sujetos"]}
    usadas: dict[str, str] = {}
    for s in cat["sujetos"]:
        for t in [s["label"], *(s.get("alias") or [])]:
            for f in _formas(t):
                usadas.setdefault(f, s["id"])
    for k, a in enumerate(ampl.get("ampliaciones") or [], 1):
        op = a.get("operacion")
        if op not in OPERACIONES:
            raise ErrorAmpliacion(f"ampliación {k}: operación {op!r} fuera de {OPERACIONES}")
        if not a.get("evidencia") or not a.get("aprobacion"):
            raise ErrorAmpliacion(f"ampliación {k}: sin evidencia o sin aprobación")
        textos = [a.get("label") or "", *(a.get("alias") or [])] if op == "alta_id" else [a.get("alias") or ""]
        for t in textos:
            if not t.strip():
                raise ErrorAmpliacion(f"ampliación {k}: label o alias vacío")
            if E4._sin_articulo(t) in E4.EXPRESIONES_COLECTIVAS_R3:
                raise ErrorAmpliacion(f"ampliación {k}: «{t}» es una expresión colectiva de la lista de R3")
            choque = next((usadas[f] for f in sorted(_formas(t)) if f in usadas), None)
            if choque:
                raise ErrorAmpliacion(f"ampliación {k}: «{t}» ya es label o alias de {choque}")
        if op == "alta_id":
            i, padre = a.get("id") or "", por_id.get(a.get("padre"))
            if not i.startswith("Sujeto_") or i in por_id:
                raise ErrorAmpliacion(f"ampliación {k}: id {i!r} inválido o ya existente")
            if padre is None or padre["estado"]["valor"] != "vigente" or padre["nivel"] != "clase":
                raise ErrorAmpliacion(f"ampliación {k}: el padre {a.get('padre')!r} no es una clase vigente")
            nuevo = copy.deepcopy(padre)           # mismas claves, en el mismo orden, que una clase del catálogo
            nuevo.update(id=i, nivel="clase", label=a["label"], alias=list(a.get("alias") or []),
                         definicion=a.get("definicion"), padre=a["padre"], instancia_de=None, parte_de=None,
                         disjunta_con=[], padre_inferido=None,
                         provenance_esqueleto={"source_doc": ARCHIVO_AMPLIACIONES, "location": f"ampliación {k}"},
                         rol=None, rol_por_to=[], marca_revision=None,
                         estado={"valor": "vigente", "alta": f"catálogo de resolución, ampliación {k}"},
                         procedencia={"id": "ampliacion_resolucion"})
            cat["sujetos"].append(nuevo)
            por_id[i] = nuevo
            destino = i
        else:
            s = por_id.get(a.get("id"))
            if s is None or s["estado"]["valor"] != "vigente":
                raise ErrorAmpliacion(f"ampliación {k}: el id {a.get('id')!r} no es un sujeto vigente")
            s["alias"] = list(s["alias"]) + [a["alias"]]
            destino = s["id"]
        for t in textos:
            for f in _formas(t):
                usadas[f] = destino
    return cat


def generar_resolucion(ruta_ampliaciones: Path, salida: Path, registro_md: Path | None = None,
                       tandas: list[str] | None = None) -> dict:
    """Escribe en `salida` el catálogo de resolución y sus generados, con el manifiesto. Devuelve el reporte. Con
    `registro_md`, las entradas de alcance de esas tandas (todas, sin `tandas`) entran al compuesto (clave
    `alcance_de_resolucion`, que cambia su sha) y al rol_por_to de resolución, después de las de la release."""
    M = E4.modulo_modelos_r2()
    texto_req = CATALOGO_REQUEST.read_text(encoding="utf-8")
    sha_req = sha256_texto(texto_req)
    if sha_req != M.CATALOGO_R2_SHA256:
        raise RuntimeError("el catálogo del request no es el que fija modelos_r2")
    b_ampl = Path(ruta_ampliaciones).read_bytes()
    ampl = json.loads(b_ampl.decode("utf-8"))
    cat = componer(json.loads(texto_req), sha_req, ampl)
    alcances, reg = OrderedDict(), None
    if registro_md is not None:
        reg = leer_registro_alcance(registro_md)
        req = E4.catalogo_r2()
        alcances = entradas_de_alcance(reg, req["rol_por_to"], req["labels"], tandas)
        cat["alcance_de_resolucion"] = OrderedDict([
            ("registro", reg["fuente"]), ("registro_sha256", reg["fuente_sha256"]),
            ("tandas", list(tandas) if tandas is not None else list(reg["tandas"])), ("entradas", alcances)])
    texto = json.dumps(cat, ensure_ascii=False, indent=1) + "\n"
    n = len(ampl.get("ampliaciones") or []) + len(alcances)
    salida = Path(salida)
    salida.mkdir(parents=True, exist_ok=True)
    if n == 0:
        if texto != texto_req:
            raise RuntimeError("sin ampliaciones, el compuesto tiene que ser el catálogo del request byte a byte")
        fuente = CATALOGO_REQUEST
    else:
        fuente = salida / ARCHIVO_COMPUESTO
        fuente.write_text(texto, encoding="utf-8")
    gen = GEN.generar_todo(fuente)
    if alcances:
        rol = json.loads(gen["rol_por_to_r2.json"])
        gen["rol_por_to_r2.json"] = json_texto({**rol, **alcances})
    (salida / ARCHIVO_AMPLIACIONES).write_bytes(b_ampl)
    archivos = OrderedDict()
    for nombre in E4.ARCHIVOS_RESOLUCION_R2:
        (salida / nombre).write_text(gen[nombre], encoding="utf-8")
        archivos[nombre] = sha256_texto(gen[nombre])
    man = OrderedDict([("formato", E4.FORMATO_RESOLUCION_R2), ("catalogo_request", ruta(CATALOGO_REQUEST)),
                       ("catalogo_request_sha256", sha_req), ("ampliaciones", ARCHIVO_AMPLIACIONES),
                       ("ampliaciones_sha256", sha256_bytes(b_ampl)), ("n_ampliaciones", n),
                       ("n_altas", n - len(alcances)), ("n_alcances", len(alcances)),
                       ("registro_alcance", reg["fuente"] if reg else None),
                       ("registro_alcance_sha256", reg["fuente_sha256"] if reg else None),
                       ("catalogo", ARCHIVO_COMPUESTO if n else ruta(CATALOGO_REQUEST)),
                       ("catalogo_sha256", sha256_texto(texto)), ("generador", GENERADOR),
                       ("no_generados_solo_del_request", list(SOLO_DEL_REQUEST)), ("archivos", archivos)])
    (salida / E4.MANIFIESTO_RESOLUCION_R2).write_text(json_texto(man), encoding="utf-8")
    idx_req = E4.indice_desde_lista(json.loads((GENERADOS_REQUEST / "indice_e4_r2.json").read_text(encoding="utf-8")))
    idx_res = E4.indice_desde_lista(json.loads(gen["indice_e4_r2.json"]))
    rep = OrderedDict([
        ("manifiesto", man),
        ("ids_nuevos", [s["id"] for s in cat["sujetos"] if s["id"] not in {x["id"] for x in json.loads(texto_req)["sujetos"]}]),
        ("alias_nuevos", [[a["id"], a["alias"]] for a in ampl.get("ampliaciones") or [] if a["operacion"] == "alta_alias"]),
        ("generados_iguales_a_generados_r2", {nm: sha256_texto(gen[nm]) == sha256_path(GENERADOS_REQUEST / nm)
                                             for nm in E4.ARCHIVOS_RESOLUCION_R2}),
        ("solo_del_request_sin_cambios_si_no_hay_ampliaciones",
         {nm: sha256_texto(gen[nm]) == sha256_path(GENERADOS_REQUEST / nm) for nm in SOLO_DEL_REQUEST}),
        ("indice_claves_nuevas", sorted([list(k) + [v] for k, v in idx_res.items() if k not in idx_req])),
        ("indice_claves_que_pasan_a_ambiguas", sorted([list(k) for k, v in idx_res.items()
                                                       if v == "__AMBIGUO__" and idx_req.get(k, "__AMBIGUO__") != v])),
        ("indice_claves_que_cambian_de_id", sorted([list(k) + [idx_req[k], v] for k, v in idx_res.items()
                                                    if k in idx_req and idx_req[k] != v and v != "__AMBIGUO__"])),
        ("alcances_nuevos", alcances),
    ])
    (salida / "reporte_composicion.json").write_text(json_texto(rep), encoding="utf-8")
    return rep


# --------------------------------------------------------------------------------------------------------------- #
# (a) y (a+)                                                                                                       #
# --------------------------------------------------------------------------------------------------------------- #
def camino_a(filas: list[dict], cat_res: dict, archivo_por_to: dict) -> dict:
    r = E4.reresolver_registro(filas, cat_res["indice"], cat_res["rol_por_to"], archivo_por_to,
                               cat_res["catalogo_sha256"])
    idem = E4.reresolver_registro(r["filas"], cat_res["indice"], cat_res["rol_por_to"], archivo_por_to,
                                  cat_res["catalogo_sha256"])
    resueltas = [b for a, b in zip(filas, r["filas"]) if a != b]
    return {"filas": r["filas"], "resueltas_ahora": r["resueltas_ahora"],
            "idempotente": idem["resueltas_ahora"] == 0 and idem["filas"] == r["filas"],
            "resueltas": [{"to": b["to"], "chunk_id": b["chunk_id"], "indice_relacion": b["indice_relacion"],
                           "mencion": b["mencion"], "id_nodo": b["id_nodo"], "resuelto_a": b["resuelto_a"],
                           "metodo": b["metodo"], "calificador": b["calificador"]} for b in resueltas],
            "campos_que_cambian": sorted({k for a, b in zip(filas, r["filas"]) if a != b for k in b
                                          if a.get(k) != b.get(k)})}


def decidir(f: dict, padre: str | None, idx: dict, prefijos: list, rol: str | None, sin_alcance: bool = False) -> dict:
    """La regla de decisión de r1_e4.resolver_relaciones_r2 sobre una fila de resolucion_sujetos.jsonl, con los mismos
    campos que la fila guarda. `sin_alcance`: la parte A de la enmienda 6 rige (fase r2b) y el documento no tiene
    entrada en rol_por_to. El control `reproduce_la_decision_guardada` la contrasta con la de la cadena."""
    m, nivel, modelo = f.get("mencion"), f.get("mencion_verificada"), f.get("sujeto_id_modelo")
    regla = (E4.resolver_mencion_r2(m, padre, idx, prefijos, rol) if m and nivel in VERIFICADAS
             else {"regla": None, "id": None, "criterios": [], "calificador": None,
                   "motivo": "mencion_no_verificada" if m else "sin_mencion"})
    final, metodo = None, None
    if regla["regla"] == "R1":
        final, metodo = regla["id"], "R1_" + "+".join(c for c in regla["criterios"] if c in E4.CRITERIOS_R1)
    elif sin_alcance and regla.get("motivo") in E4.MOTIVOS_PARTE_A:
        pass
    elif modelo:
        final, metodo = modelo, "R4_sugerencia_modelo"
    elif regla["regla"] == "R2":
        final, metodo = regla["id"], "R2_" + "+".join(regla["criterios"])
    elif regla["regla"] in ("R2_calificador", "R3"):
        final, metodo = regla["id"], regla["regla"]
    return {"resuelto_a": final, "metodo_resolucion": metodo or "cuarentena",
            "desacuerdo_regla_modelo": bool(regla["id"] and modelo and regla["id"] != modelo),
            "regla_texto": regla["regla"], "id_regla_texto": regla["id"], "criterios": regla["criterios"],
            "calificador": regla["calificador"]}


def camino_a_mas(resolucion: list[dict], registro: list[dict], cat_ant: dict, cat_res: dict,
                 archivo_por_to: dict, parte_a: bool = False) -> dict:
    por_reg = {clave(f): f for f in registro}
    pre_ant, pre_res = E4._prefijos(cat_ant["indice"]), E4._prefijos(cat_res["indice"])
    no_reproduce, cambian = [], []
    for f in resolucion:
        k = clave(f)
        fr = por_reg.get(k) or {}
        padre = fr.get("padre_sugerido")
        rol_ant = (cat_ant["rol_por_to"].get(archivo_por_to.get(f["to"])) or {}).get("rol_id")
        rol_res = (cat_res["rol_por_to"].get(archivo_por_to.get(f["to"])) or {}).get("rol_id")
        archivo = archivo_por_to.get(f["to"])
        antes = decidir(f, padre, cat_ant["indice"], pre_ant, rol_ant, parte_a and archivo not in cat_ant["rol_por_to"])
        guardada = {c: f.get(c) for c in CAMPOS_DECISION}
        if antes != guardada:
            no_reproduce.append({"clave": list(k), "guardada": guardada, "recomputada": antes})
        despues = decidir(f, padre, cat_res["indice"], pre_res, rol_res, parte_a and archivo not in cat_res["rol_por_to"])
        if despues != antes:
            campos = [c for c in CAMPOS_DECISION if antes[c] != despues[c]]
            tipo = ("destino" if "resuelto_a" in campos else "metodo" if "metodo_resolucion" in campos
                    else "calificador" if "calificador" in campos else "desacuerdo" if "desacuerdo_regla_modelo" in campos
                    else "regla_texto")
            cambian.append({"clave": list(k), "to": f["to"], "chunk_id": f["chunk_id"],
                            "indice_relacion": f["indice_relacion"], "predicado": f["predicado"],
                            "mencion": f.get("mencion"), "mencion_verificada": f.get("mencion_verificada"),
                            "sujeto_id_modelo": f.get("sujeto_id_modelo"), "tipo": tipo, "campos": campos,
                            "antes": antes, "despues": despues, "estado_registro": fr.get("estado"),
                            "id_nodo_registro": fr.get("id_nodo")})
    return {"relaciones_de_sujeto": len(resolucion), "reproduce_la_decision_guardada": not no_reproduce,
            "no_reproduce": no_reproduce, "cambian": cambian,
            "cambian_por_tipo": ordenado(Counter(c["tipo"] for c in cambian)),
            "cambian_por_estado_registro": ordenado(Counter(str(c["estado_registro"]) for c in cambian)),
            "nota": "padre_sugerido solo está en las filas del registro; para las demás relaciones se usa None (afecta "
                    "solo al criterio alias_en_parentesis); el control reproduce_la_decision_guardada lo cubre"}


# --------------------------------------------------------------------------------------------------------------- #
# (b): el ensamblado entero, por el camino del ensamblador                                                         #
# --------------------------------------------------------------------------------------------------------------- #
@contextlib.contextmanager
def observar_rechazos_e2(destino: list):
    """Observa, sin cambiarlo, lo que devuelve e2_lib.ensamblar_r2 en cada llamada: guarda la lista de rechazos de
    E2 (control de W1: cero relaciones rechazadas sin registro). Restaura la función al salir."""
    original = ENS.e2_lib.ensamblar_r2

    def envoltura(*a, **k):
        r = original(*a, **k)
        destino.append(list(r["rechazos_e2"]))
        return r
    ENS.e2_lib.ensamblar_r2 = envoltura
    try:
        yield
    finally:
        ENS.e2_lib.ensamblar_r2 = original


def camino_b(manifiesto: Path, entrada: Path, salida: Path, e0_r2: Path, con_cola: bool, cat_res: dict) -> dict:
    man = ENS.MC.cargar(manifiesto)
    llamadas: list = []
    with observar_rechazos_e2(llamadas):
        res = ENS.ensamblar_manifiesto_r2(man, entrada, salida, e0_r2, con_cola=con_cola, cat_resolucion=cat_res)
    mitad = len(llamadas) // 2
    rechazos = [x for lst in llamadas[:mitad] for x in lst]
    segunda = [x for lst in llamadas[mitad:] for x in lst]
    return {"resultado": res, "rechazos_e2_por_motivo": ordenado(Counter(r["motivo"] for r in rechazos)),
            "rechazos_e2_sujeto_id_fuera_de_catalogo": [r for r in rechazos if r["motivo"] == "sujeto_id_fuera_de_catalogo"],
            "rechazos_iguales_en_las_dos_corridas": rechazos == segunda and len(llamadas) % 2 == 0}


# --------------------------------------------------------------------------------------------------------------- #
# registro acumulado                                                                                               #
# --------------------------------------------------------------------------------------------------------------- #
def proyectar(f: dict, quitar=CAMPOS_VERSION) -> dict:
    return {k: v for k, v in f.items() if k not in quitar}


def registro_acumulado(filas_a: list[dict], a_mas: dict, reg_b: list[dict], res_b: list[dict], cat_res: dict) -> dict:
    """El registro anterior actualizado por (a) (cuarentena → resuelto, `reresolver_registro`) y por (a+) (las filas
    resueltas a clase cuya decisión cambia), con el id_nodo de (b) en las filas que siguen en cuarentena, más las
    filas de (b) que el anterior no tiene. `catalogo_sha256` es la versión con la que la fila entró y no cambia;
    `catalogo_sha256_resolucion`, la versión con la que resolvió. Controles: (1) las filas que siguen sin resolver
    son las de (b), salvo la versión; (2) el destino de cada fila resuelta es el de su relación en (b); (3) las filas de
    (b) fuera del registro anterior se listan."""
    por_b = {clave(f): f for f in reg_b}
    res_por_b = {clave(f): f for f in res_b}
    cambio = {tuple(c["clave"]): c for c in a_mas["cambian"]}
    acum, renombres, actualizadas_a_mas = [], [], []
    for f in filas_a:
        g = dict(f)
        k = clave(f)
        if f["estado"] == "resuelto_a_clase" and k in cambio:
            d = cambio[k]["despues"]
            g.update(resuelto_a=d["resuelto_a"], metodo=d["metodo_resolucion"], calificador=d["calificador"],
                     catalogo_sha256_resolucion=cat_res["catalogo_sha256"],
                     estado="resuelto_a_clase" if d["metodo_resolucion"] == "R2_calificador" else "resuelto")
            actualizadas_a_mas.append(list(k))
        if g["estado"] in ("cuarentena", "descartado") and k in por_b and por_b[k].get("id_nodo") != g.get("id_nodo"):
            renombres.append({"clave": list(k), "id_anterior": g.get("id_nodo"), "id_nodo": por_b[k].get("id_nodo")})
            g["id_nodo"] = por_b[k].get("id_nodo")
        acum.append(g)
    claves_ant = {clave(f) for f in filas_a}
    nuevas = [f for f in reg_b if clave(f) not in claves_ant]
    acum += nuevas
    por_acum = {clave(f): f for f in acum}
    sin_resolver_distintas = []
    for k, f in por_acum.items():
        if f["estado"] in ("cuarentena", "descartado"):
            if k not in por_b or proyectar(f) != proyectar(por_b[k]):
                sin_resolver_distintas.append({"clave": list(k), "acumulado": f, "b": por_b.get(k)})
    b_sin_resolver_fuera = [list(k) for k, f in por_b.items() if f["estado"] in ("cuarentena", "descartado")
                            and por_acum.get(k, {}).get("estado") not in ("cuarentena", "descartado")]
    destino_distinto = [{"clave": list(k), "acumulado": [f["resuelto_a"], f.get("metodo")],
                         "b": [res_por_b.get(k, {}).get("resuelto_a"), res_por_b.get(k, {}).get("metodo_resolucion")]}
                        for k, f in por_acum.items() if f["estado"] in ("resuelto", "resuelto_a_clase")
                        and (k not in res_por_b or res_por_b[k]["resuelto_a"] != f["resuelto_a"])]
    estado_distinto_de_b = [{"clave": list(k), "acumulado": f["estado"], "b": por_b[k]["estado"]}
                            for k, f in por_acum.items() if k in por_b and f["estado"] != por_b[k]["estado"]]
    return {"filas": acum,
            "control": OrderedDict([
                ("filas_anterior", len(filas_a)), ("filas_b", len(reg_b)), ("filas_acumulado", len(acum)),
                ("por_estado_acumulado", ordenado(Counter(f["estado"] for f in acum))),
                ("por_estado_b", ordenado(Counter(f["estado"] for f in reg_b))),
                ("1_sin_resolver_iguales_a_b_salvo_version", not sin_resolver_distintas and not b_sin_resolver_fuera),
                ("1_sin_resolver_distintas", sin_resolver_distintas), ("1_b_sin_resolver_fuera", b_sin_resolver_fuera),
                ("2_destino_de_las_resueltas_igual_a_b", not destino_distinto), ("2_destino_distinto", destino_distinto),
                ("3_filas_de_b_fuera_del_anterior", [list(clave(f)) for f in nuevas]),
                ("renombres_de_id_nodo", renombres), ("actualizadas_por_a_mas", actualizadas_a_mas),
                ("estado_distinto_de_b", estado_distinto_de_b)])}


# --------------------------------------------------------------------------------------------------------------- #
# contraste de (b) contra lo que predicen (a), (a+) y el esqueleto                                                 #
# --------------------------------------------------------------------------------------------------------------- #
def provs_sujeto(kg: dict) -> Counter:
    c = Counter()
    for e in kg["edges"]:
        if e["relation"] in E4.PREDICADOS_SUJETO_R2:
            for p in e.get("provenances") or [e.get("provenance")]:
                c[(e["source"], e["relation"], e["target"], p.get("chunk_id"))] += 1
    return c


def diferencia(kg0: dict, kg1: dict) -> dict:
    n0, n1 = {n["id"]: n for n in kg0["nodes"]}, {n["id"]: n for n in kg1["nodes"]}
    e0 = {(e["source"], e["relation"], e["target"]): e for e in kg0["edges"]}
    e1 = {(e["source"], e["relation"], e["target"]): e for e in kg1["edges"]}
    return {"nodos_quitados": sorted(set(n0) - set(n1)), "nodos_agregados": sorted(set(n1) - set(n0)),
            "nodos_que_cambian": {i: sorted({k for k in set(n0[i]) | set(n1[i]) if n0[i].get(k) != n1[i].get(k)})
                                  for i in sorted(set(n0) & set(n1)) if n0[i] != n1[i]},
            "aristas_quitadas": [list(k) for k in sorted(set(e0) - set(e1))],
            "aristas_agregadas": [list(k) for k in sorted(set(e1) - set(e0))],
            "aristas_que_cambian": {"|".join(k): sorted({c for c in set(e0[k]) | set(e1[k]) if e0[k].get(c) != e1[k].get(c)})
                                    for k in sorted(set(e0) & set(e1)) if e0[k] != e1[k]}}


def prediccion(a: dict, a_mas: dict, acum: dict, comp: dict, kg0: dict, tos_alcance_nuevo=()) -> dict:
    """Cambios de destino por procedencia (chunk, destino anterior, destino nuevo): de (a), las filas que resuelven
    (del nodo en cuarentena al id); de (a+), las relaciones fuera de la cuarentena que cambian de destino; y los
    renombres de id_nodo de las filas que siguen en cuarentena. Más los propuestos que desaparecen (ninguna fila sigue
    en cuarentena con su id), los ids nuevos con su esqueleto, los ids que reciben un alias y los TOs que reciben
    alcance (sus propuestos sin padre toman el rol de alcance como padre por defecto)."""
    cambios = []
    for d in a["resueltas"]:
        cambios.append([d["chunk_id"], d["id_nodo"], d["resuelto_a"], "a"])
    nuevas_b = {tuple(k) for k in acum["control"]["3_filas_de_b_fuera_del_anterior"]}
    por_acum = {clave(f): f for f in acum["filas"]}
    for c in a_mas["cambian"]:
        if c["estado_registro"] == "cuarentena" or c["antes"]["resuelto_a"] == c["despues"]["resuelto_a"]:
            continue
        antes = c["antes"]["resuelto_a"] or (c["id_nodo_registro"] if c["estado_registro"] != "descartado" else None)
        despues = c["despues"]["resuelto_a"]
        if despues is None and tuple(c["clave"]) in nuevas_b:
            despues = por_acum[tuple(c["clave"])].get("id_nodo")
        cambios.append([c["chunk_id"], antes, despues, "a+"])
    for r in acum["control"]["renombres_de_id_nodo"]:
        cambios.append([r["clave"][1], r["id_anterior"], r["id_nodo"], "renombre"])
    sigue = {f.get("id_nodo") for f in acum["filas"] if f["estado"] == "cuarentena"}
    viejos = {c[1] for c in cambios if c[1]}
    nodos0 = {n["id"] for n in kg0["nodes"]}
    return {"cambios_de_destino": cambios,
            "propuestos_que_desaparecen": sorted(i for i in viejos if i not in sigue and i.startswith("Sujeto_propuesto_")),
            "ids_nuevos": [i for i in comp["ids_nuevos"] if i not in nodos0],
            "alias_nuevos_en": sorted({i for i, _ in comp["alias_nuevos"]}),
            "tos_con_alcance_nuevo": sorted(tos_alcance_nuevo),
            "a_mas_por_procedencia": [[c["chunk_id"], c["despues"]["resuelto_a"] or c["antes"]["resuelto_a"]]
                                      for c in a_mas["cambian"]]}


def contrastar(pred: dict, kg0: dict, kg1: dict) -> dict:
    dif = diferencia(kg0, kg1)
    p0, p1 = provs_sujeto(kg0), provs_sujeto(kg1)
    quitadas, agregadas = p0 - p1, p1 - p0
    por_quitar = Counter((c[0], c[1]) for c in pred["cambios_de_destino"] if c[1])
    por_agregar = Counter((c[0], c[2]) for c in pred["cambios_de_destino"] if c[2])
    no_explicado, explicadas = [], 0
    for (src, rel, tgt, cid), n in sorted(quitadas.items()):
        if por_quitar[(cid, tgt)] >= n:
            por_quitar[(cid, tgt)] -= n
            explicadas += n
        else:
            no_explicado.append({"procedencia_quitada": [src, rel, tgt, cid], "n": n})
    for (src, rel, tgt, cid), n in sorted(agregadas.items()):
        if por_agregar[(cid, tgt)] >= n:
            por_agregar[(cid, tgt)] -= n
            explicadas += n
        else:
            no_explicado.append({"procedencia_agregada": [src, rel, tgt, cid], "n": n})
    pendientes = ([{"prediccion_sin_quitar": list(k), "n": v} for k, v in por_quitar.items() if v > 0]
                  + [{"prediccion_sin_agregar": list(k), "n": v} for k, v in por_agregar.items() if v > 0])
    quitados_ok = set(pred["propuestos_que_desaparecen"]) | {c[1] for c in pred["cambios_de_destino"]
                                                              if c[3] == "renombre"}
    agregados_ok = set(pred["ids_nuevos"]) | {c[2] for c in pred["cambios_de_destino"] if c[2]}
    tocados = {c[1] for c in pred["cambios_de_destino"] if c[1]} | {c[2] for c in pred["cambios_de_destino"] if c[2]}
    tos_nuevos = set(pred.get("tos_con_alcance_nuevo") or ())
    tocados |= {n["id"] for n in kg1["nodes"] if n["type"] == "Sujeto" and n["properties"].get("nivel") == "propuesto"
                and any(p.get("to") in tos_nuevos for p in n.get("provenances") or [])}
    no_explicado += [{"nodo_quitado": i} for i in dif["nodos_quitados"] if i not in quitados_ok]
    no_explicado += [{"nodo_agregado": i} for i in dif["nodos_agregados"] if i not in agregados_ok]
    no_explicado += [{"nodo_que_cambia": i, "campos": c} for i, c in dif["nodos_que_cambian"].items()
                     if i not in tocados and i not in pred["alias_nuevos_en"]]
    sujeto = set(E4.PREDICADOS_SUJETO_R2)
    quitados = set(dif["nodos_quitados"])
    agregados = set(dif["nodos_agregados"])
    no_explicado += [{"arista_quitada": k} for k in dif["aristas_quitadas"]
                     if k[1] not in sujeto and not (k[0] in quitados or k[2] in quitados)]
    no_explicado += [{"arista_agregada": k} for k in dif["aristas_agregadas"]
                     if k[1] not in sujeto and not (k[0] in agregados and (k[1] in RELACIONES_ESQUELETO
                                                                           or k[1] == "padre_sugerido"))
                     and not (k[1] == "padre_sugerido" and k[0] in tocados)]
    procedencias_a_mas = {tuple(x) for x in pred["a_mas_por_procedencia"]}
    kg1_aristas = {(e["source"], e["relation"], e["target"]): e for e in kg1["edges"]}
    for k, campos in dif["aristas_que_cambian"].items():
        s, r, t = k.split("|")
        if r == "padre_sugerido" and s in tocados:
            continue
        if r not in sujeto:
            no_explicado.append({"arista_que_cambia": k, "campos": campos})
            continue
        chunks = {p.get("chunk_id") for p in kg1_aristas[(s, r, t)].get("provenances") or []}
        if campos != ["provenances"] and not any((cid, t) in procedencias_a_mas for cid in chunks) \
                and t not in tocados:
            no_explicado.append({"arista_de_sujeto_que_cambia": k, "campos": campos})
    return {"diferencia": dif, "procedencias_de_sujeto_explicadas": explicadas,
            "prediccion_sin_observar": pendientes, "no_explicado": no_explicado + pendientes}


def resolucion_b_contra_a_mas(res_ant: list[dict], res_b: list[dict], a_mas: dict, cat_res: dict) -> dict:
    """Relación por relación: la decisión de (b) es la que predice (a+) (la anterior si no cambia)."""
    cambio = {tuple(c["clave"]): c["despues"] for c in a_mas["cambian"]}
    por_b = {clave(f): f for f in res_b}
    distintas, faltan = [], []
    for f in res_ant:
        k = clave(f)
        esperado = cambio.get(k) or {c: f.get(c) for c in CAMPOS_DECISION}
        g = por_b.get(k)
        if g is None:
            faltan.append(list(k))
            continue
        obs = {c: g.get(c) for c in CAMPOS_DECISION}
        if obs != esperado:
            distintas.append({"clave": list(k), "esperado": esperado, "observado": obs})
    sobran = [list(k) for k in por_b if k not in {clave(f) for f in res_ant}]
    version = Counter(f.get("catalogo_sha256") for f in res_b)
    return {"relaciones_anterior": len(res_ant), "relaciones_b": len(res_b), "faltan_en_b": faltan,
            "sobran_en_b": sobran, "decision_distinta_de_la_predicha": distintas,
            "iguales": not faltan and not sobran and not distintas,
            "catalogo_sha256_en_b": dict(version),
            "todas_con_el_sha_de_resolucion": set(version) == {cat_res["catalogo_sha256"]}}


def archivos_contra_anterior(anterior: Path, salida_r2: Path, tos_tocados: set[str]) -> dict:
    """Cada archivo de la salida contra el del ensamblado anterior. Cambian, explicados: el grafo, los registros, el
    reporte y los registros por TO de los TOs con cambios; en los demás TOs, los registros por TO solo pueden diferir
    en la versión del catálogo (cada fila lleva el sha con que se resolvió, P-d4). Cualquier otro archivo distinto queda
    sin explicar."""
    fa = {str(p.relative_to(anterior)) for p in anterior.rglob("*") if p.is_file()}
    fb = {str(p.relative_to(salida_r2)) for p in salida_r2.rglob("*") if p.is_file()} - {REGISTRO_CADENA}
    distintos, solo_version, no_explicados = [], [], []
    for rel in sorted(fa & fb):
        if (anterior / rel).read_bytes() == (salida_r2 / rel).read_bytes():
            continue
        distintos.append(rel)
        partes = Path(rel).parts
        por_to = len(partes) == 3 and partes[0] == "por_to" and partes[2] in (REGISTRO, RESOLUCION)
        if rel in ARCHIVOS_QUE_CAMBIAN or (por_to and partes[1] in tos_tocados):
            continue
        if por_to and [proyectar(f) for f in leer_jsonl(anterior / rel)] == [proyectar(f) for f in leer_jsonl(salida_r2 / rel)]:
            solo_version.append(rel)
            continue
        no_explicados.append(rel)
    return {"solo_en_anterior": sorted(fa - fb), "solo_en_salida": sorted(fb - fa), "distintos": distintos,
            "distintos_solo_en_la_version_del_catalogo": solo_version, "distintos_no_explicados": no_explicados}


# --------------------------------------------------------------------------------------------------------------- #
# gate: shapes r2 y suite del perfil                                                                               #
# --------------------------------------------------------------------------------------------------------------- #
def shapes(kg_path: Path, registro_dir: Path, e0_dir: Path, fase: str, gen_dir: Path | None) -> dict:
    sys.path.insert(0, str(RAIZ / "scripts"))
    import shapes_validator as SV       # noqa: PLC0415  (importado, no editado)
    vocab = SV.cargar_vocabulario_r2()
    g = json.loads(Path(kg_path).read_text(encoding="utf-8"))
    kw = {} if gen_dir is None else {"ids_s19_ruta": str(gen_dir / "ids_s19_r2.json"),
                                      "excepciones_ruta": str(gen_dir / "entrada_esqueleto_r2.json")}
    resultados, veredicto, meta = SV.evaluar_perfil_r2(g, vocab, fase, str(Path(registro_dir) / REGISTRO), str(e0_dir), **kw)
    return {"veredicto": veredicto, "bloqueantes_en_fail": meta["bloqueantes_en_fail"],
            "bloqueantes_no_computables": meta["bloqueantes_no_computables"],
            "catalogo_s19": {"ruta": ruta(meta["catalogo"]["ruta"]), "n_ids": meta["catalogo"]["n_ids"]},
            "shapes": {rid: {"severidad": "bloqueante" if rid in meta["bloqueantes"] else "informativa",
                             "result": r["result"], "resumen": r["resumen"], "conteos": r.get("conteos")}
                       for rid, r in resultados.items()}}


def suite(kg_path: Path, registro_dir: Path, manifiesto: Path, gen_dir: Path | None, out_md: Path) -> dict:
    cat_suite = (gen_dir / "catalogo_suite_r2.json") if gen_dir else (GENERADOS_REQUEST / "catalogo_suite_r2.json")
    cmd = [sys.executable, "-B", str(RAIZ / "scripts" / "regression_kg.py"), "--kg", str(kg_path), "--perfil", "r2",
           "--generacion", "3", "--catalogo", str(cat_suite), "--politica-cuarentena", "flaggeada",
           "--registro-dir", str(registro_dir), "--manifiesto", str(manifiesto), "--out", str(out_md)]
    if gen_dir is not None:
        cmd += ["--generados-resolucion", str(gen_dir)]
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    env.pop("ANTHROPIC_API_KEY", None)
    r = subprocess.run(cmd, cwd=RAIZ, env=env, capture_output=True, text=True)
    out = json.loads(out_md.with_suffix(".json").read_text(encoding="utf-8")) if out_md.with_suffix(".json").exists() else {}
    return {"codigo": r.returncode, "resumen": out.get("resumen"),
            "items": {i["id"]: {"estado": i["estado"], "detalle": i.get("detalle")} for i in out.get("items", [])},
            "stderr_cola": r.stderr[-2000:]}


def comparar_gate(ant: dict, nuevo: dict) -> dict:
    sh = {rid: {"anterior": [ant["shapes"]["shapes"][rid]["result"], ant["shapes"]["shapes"][rid]["resumen"]],
                "nuevo": [v["result"], v["resumen"]]}
          for rid, v in nuevo["shapes"]["shapes"].items()
          if (ant["shapes"]["shapes"].get(rid) or {}).get("conteos") != v.get("conteos")
          or (ant["shapes"]["shapes"].get(rid) or {}).get("result") != v["result"]}
    su = {i: {"anterior": ant["suite"]["items"].get(i), "nuevo": v} for i, v in nuevo["suite"]["items"].items()
          if (ant["suite"]["items"].get(i) or {}) != v}
    return {"shapes_veredicto": [ant["shapes"]["veredicto"], nuevo["shapes"]["veredicto"]],
            "shapes_que_cambian": sh,
            "suite_resumen": [ant["suite"]["resumen"], nuevo["suite"]["resumen"]],
            "suite_estados_que_cambian": {i: [d["anterior"]["estado"] if d["anterior"] else None, d["nuevo"]["estado"]]
                                          for i, d in su.items()
                                          if (d["anterior"] or {}).get("estado") != d["nuevo"]["estado"]},
            "suite_detalles_que_cambian": sorted(su)}


# --------------------------------------------------------------------------------------------------------------- #
# correr                                                                                                           #
# --------------------------------------------------------------------------------------------------------------- #
def correr(args) -> int:
    manifiesto = Path(args.manifiesto)
    man = ENS.MC.cargar(manifiesto)
    archivo_por_to = {t["id"]: t["archivo"] for t in man.tos}
    import runner_corpus as RC          # noqa: PLC0415 — en el path por el ensamblador
    parte_a = bool(RC.perfil_forma_r2(ENS.perfil_e1.perfil(man.perfil_e1)))      # la cadena la activa en r2b
    cat_res = E4.catalogo_resolucion_r2(args.generados_resolucion)
    cat_ant = E4.catalogo_resolucion_r2(args.generados_anterior) if args.generados_anterior else E4.catalogo_r2()
    gen_res = Path(args.generados_resolucion)
    comp_path = gen_res / "reporte_composicion.json"
    comp = json.loads(comp_path.read_text(encoding="utf-8"))
    anterior, salida = Path(args.anterior), Path(args.salida)
    salida_r2 = salida / "r2"
    reg_ant = leer_jsonl(anterior / REGISTRO)
    res_ant = leer_jsonl(anterior / RESOLUCION)
    kg_ant = json.loads((anterior / "kg.json").read_text(encoding="utf-8"))

    a = camino_a(reg_ant, cat_res, archivo_por_to)
    a_mas = camino_a_mas(res_ant, reg_ant, cat_ant, cat_res, archivo_por_to, parte_a)
    tos_alcance_nuevo = {to for to, arch in archivo_por_to.items()
                         if arch in cat_res["rol_por_to"] and arch not in cat_ant["rol_por_to"]}
    print(f"(a) resueltas {a['resueltas_ahora']}; (a+) cambian {len(a_mas['cambian'])} {a_mas['cambian_por_tipo']}; "
          f"reproduce la decisión guardada: {a_mas['reproduce_la_decision_guardada']}", flush=True)
    b = camino_b(manifiesto, Path(args.entrada), salida, Path(args.e0_r2), not args.sin_cola, cat_res)
    reg_b = leer_jsonl(salida_r2 / REGISTRO)
    res_b = leer_jsonl(salida_r2 / RESOLUCION)
    kg_b = json.loads((salida_r2 / "kg.json").read_text(encoding="utf-8"))
    acum = registro_acumulado(a["filas"], a_mas, reg_b, res_b, cat_res)
    (salida_r2 / REGISTRO).rename(salida_r2 / REGISTRO_CADENA)
    escribir_jsonl(salida_r2 / REGISTRO, acum["filas"])
    pred = prediccion(a, a_mas, acum, comp, kg_ant, tos_alcance_nuevo)
    cont = contrastar(pred, kg_ant, kg_b)
    res_vs = resolucion_b_contra_a_mas(res_ant, res_b, a_mas, cat_res)
    cuarentena_a = {tuple(x["clave"]) for x in a_mas["cambian"] if x["estado_registro"] == "cuarentena"}
    a_y_a_mas = sorted([d["to"], d["chunk_id"], d["indice_relacion"]] for d in a["resueltas"]
                       if not any(k[0] == d["to"] and k[1] == d["chunk_id"] and k[3] == d["indice_relacion"]
                                  for k in cuarentena_a))
    tos_tocados = ({c[0].split("::")[0] for c in pred["cambios_de_destino"]} | {x["to"] for x in a_mas["cambian"]}
                   | tos_alcance_nuevo)
    arch = archivos_contra_anterior(anterior, salida_r2, tos_tocados)
    rep = OrderedDict()
    rep["entrada"] = OrderedDict([("manifiesto", ruta(manifiesto)), ("entrada", ruta(args.entrada)),
                                  ("e0_r2", ruta(args.e0_r2)), ("anterior", ruta(anterior)),
                                  ("generados_resolucion", ruta(gen_res)),
                                  ("generados_anterior", ruta(args.generados_anterior) if args.generados_anterior
                                   else "catálogo del request (generados_r2/)"),
                                  ("con_cola", not args.sin_cola)])
    rep["versiones"] = OrderedDict([("anterior", cat_ant["catalogo_sha256"]), ("resolucion", cat_res["versiones_catalogo"])])
    rep["composicion"] = {k: comp[k] for k in ("ids_nuevos", "alias_nuevos", "indice_claves_nuevas",
                                                "indice_claves_que_pasan_a_ambiguas", "indice_claves_que_cambian_de_id")}
    rep["camino_a"] = {k: a[k] for k in ("resueltas_ahora", "idempotente", "resueltas", "campos_que_cambian")}
    rep["camino_a_mas"] = a_mas
    rep["a_y_a_mas_coinciden_en_la_cuarentena"] = {"resueltas_por_a_sin_cambio_en_a_mas": a_y_a_mas,
                                                    "coinciden": not a_y_a_mas and len(cuarentena_a) == a["resueltas_ahora"]}
    rep["camino_b"] = OrderedDict([("ensamblado", b["resultado"]),
                                   ("sha256_kg", sha256_path(salida_r2 / "kg.json")),
                                   ("rechazos_e2_por_motivo", b["rechazos_e2_por_motivo"]),
                                   ("rechazos_sujeto_id_fuera_de_catalogo", b["rechazos_e2_sujeto_id_fuera_de_catalogo"]),
                                   ("rechazos_iguales_en_las_dos_corridas", b["rechazos_iguales_en_las_dos_corridas"])])
    rep["registro_acumulado"] = acum["control"]
    rep["prediccion"] = {k: v for k, v in pred.items() if k != "a_mas_por_procedencia"}
    rep["contraste_b"] = cont
    rep["resolucion_b_contra_a_mas"] = res_vs
    rep["archivos_contra_anterior"] = arch
    rep["resueltos_por_version"] = OrderedDict([
        ("relaciones_por_catalogo_sha256", dict(Counter(f.get("catalogo_sha256") for f in res_b))),
        ("registro_por_version_de_entrada", dict(Counter(f.get("catalogo_sha256") for f in acum["filas"]))),
        ("registro_resueltas_por_version", dict(Counter(f.get("catalogo_sha256_resolucion") for f in acum["filas"]
                                                        if f["estado"] in ("resuelto", "resuelto_a_clase")))),
        ("registro_por_estado", ordenado(Counter(f["estado"] for f in acum["filas"])))])
    # enmienda 6, parte A (r2b): filas en cuarentena con la sugerencia guardada, filas resueltas por R4 con una mención
    # que no verifica (se cuentan aparte, decisión de la autora del 07/10/2026) y la fila sin mención en cuarentena,
    # condición con disparador (decisión 5 del despacho de R2-2): si aparece, el script la marca y se frena
    sin_mencion = [list(clave(f)) for f in acum["filas"] if f["estado"] == "cuarentena" and f.get("motivo") == "sin_mencion"]
    rep["parte_a"] = OrderedDict([
        ("rige", parte_a), ("tos_con_alcance_nuevo", sorted(tos_alcance_nuevo)),
        ("cuarentena_con_sugerencia_por_motivo", ordenado(Counter(
            f["motivo"] for f in acum["filas"] if f["estado"] == "cuarentena" and f.get("sujeto_id_modelo")))),
        ("resueltas_por_r4_con_mencion_no_verificada", [list(clave(f)) for f in acum["filas"]
                                                        if f.get("metodo") == "R4_sugerencia_modelo"
                                                        and f.get("mencion_verificada") not in VERIFICADAS]),
        ("filas_sin_mencion_en_cuarentena", sin_mencion)])
    no_explicado = list(cont["no_explicado"])
    if sin_mencion:
        no_explicado.append({"disparador_fila_sin_mencion_en_cuarentena": len(sin_mencion)})
    if not a_mas["reproduce_la_decision_guardada"]:
        no_explicado.append({"a_mas_no_reproduce_la_decision_guardada": len(a_mas["no_reproduce"])})
    if not a["idempotente"]:
        no_explicado.append({"camino_a_no_idempotente": True})
    if not rep["a_y_a_mas_coinciden_en_la_cuarentena"]["coinciden"]:
        no_explicado.append({"a_y_a_mas_no_coinciden_en_la_cuarentena": a_y_a_mas})
    if b["rechazos_e2_sujeto_id_fuera_de_catalogo"]:
        no_explicado.append({"relaciones_rechazadas_sin_registro": len(b["rechazos_e2_sujeto_id_fuera_de_catalogo"])})
    if not res_vs["iguales"]:
        no_explicado.append({"resolucion_b_distinta_de_a_mas": len(res_vs["decision_distinta_de_la_predicha"])
                             + len(res_vs["faltan_en_b"]) + len(res_vs["sobran_en_b"])})
    c = acum["control"]
    if not c["1_sin_resolver_iguales_a_b_salvo_version"] or not c["2_destino_de_las_resueltas_igual_a_b"]:
        no_explicado.append({"registro_acumulado_distinto_de_b": [len(c["1_sin_resolver_distintas"]),
                                                                  len(c["1_b_sin_resolver_fuera"]),
                                                                  len(c["2_destino_distinto"])]})
    if c["3_filas_de_b_fuera_del_anterior"]:
        no_explicado.append({"filas_de_b_fuera_del_anterior_a_leer": len(c["3_filas_de_b_fuera_del_anterior"])})
    if arch["distintos_no_explicados"]:
        no_explicado.append({"archivos_distintos_no_explicados": arch["distintos_no_explicados"]})
    if not args.sin_gate:
        fase = json.loads((salida_r2 / "reporte_ensamblado_r2.json").read_text(encoding="utf-8")).get("fase") or "r2a"
        gate_dir = salida / "gate"
        gate_dir.mkdir(parents=True, exist_ok=True)
        gen_ant = Path(args.generados_anterior) if args.generados_anterior else None
        g_ant = {"shapes": shapes(anterior / "kg.json", anterior, Path(args.e0_r2), fase, gen_ant),
                 "suite": suite(anterior / "kg.json", anterior, manifiesto, gen_ant, gate_dir / "suite_anterior.md")}
        g_new = {"shapes": shapes(salida_r2 / "kg.json", salida_r2, Path(args.e0_r2), fase, gen_res),
                 "suite": suite(salida_r2 / "kg.json", salida_r2, manifiesto, gen_res, gate_dir / "suite_salida.md")}
        (gate_dir / "shapes_anterior.json").write_text(json_texto(g_ant["shapes"]), encoding="utf-8")
        (gate_dir / "shapes_salida.json").write_text(json_texto(g_new["shapes"]), encoding="utf-8")
        rep["gate"] = OrderedDict([("anterior", {"shapes_veredicto": g_ant["shapes"]["veredicto"],
                                                 "suite_resumen": g_ant["suite"]["resumen"],
                                                 "suite_codigo": g_ant["suite"]["codigo"]}),
                                   ("salida", {"shapes_veredicto": g_new["shapes"]["veredicto"],
                                               "shapes_bloqueantes_en_fail": g_new["shapes"]["bloqueantes_en_fail"],
                                               "suite_resumen": g_new["suite"]["resumen"],
                                               "suite_codigo": g_new["suite"]["codigo"],
                                               "ln6": g_new["suite"]["items"].get("LN-6")}),
                                   ("comparacion", comparar_gate(g_ant, g_new))])
        if g_new["shapes"]["bloqueantes_en_fail"]:
            no_explicado.append({"shapes_bloqueantes_en_fail": g_new["shapes"]["bloqueantes_en_fail"]})
        if (g_new["suite"]["items"].get("LN-6") or {}).get("estado") != "resuelto":
            no_explicado.append({"ln6_no_resuelto": g_new["suite"]["items"].get("LN-6")})
    rep["no_explicado"] = no_explicado
    (salida / "reporte_reresolucion.json").write_text(json_texto(rep), encoding="utf-8")
    print(f"(b) sha256 {rep['camino_b']['sha256_kg']}; resolución (b) = (a+): {res_vs['iguales']}; "
          f"registro acumulado: {c['por_estado_acumulado']}; no explicado: {len(no_explicado)}", flush=True)
    return 0 if not no_explicado else 1


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    r = sub.add_parser("registro", help="forma legible por código del registro de alcance por tanda")
    r.add_argument("--md", type=Path, default=REGISTRO_ALCANCE_MD)
    r.add_argument("--salida", type=Path, required=True)
    p = sub.add_parser("componer", help="compone el catálogo de resolución y escribe sus generados con el candado")
    p.add_argument("--ampliaciones", type=Path, required=True)
    p.add_argument("--salida", type=Path, required=True)
    p.add_argument("--registro-alcance", dest="registro_alcance", type=Path, default=None)
    p.add_argument("--tandas", default=None, help="tandas del registro, separadas por coma (default: todas)")
    q = sub.add_parser("correr", help="(a), (a+), (b), contraste, registro acumulado y gate")
    q.add_argument("--manifiesto", type=Path, required=True)
    q.add_argument("--entrada", type=Path, required=True)
    q.add_argument("--e0-r2", dest="e0_r2", type=Path, required=True)
    q.add_argument("--anterior", type=Path, required=True, help="directorio r2/ del ensamblado anterior")
    q.add_argument("--generados-resolucion", dest="generados_resolucion", type=Path, required=True)
    q.add_argument("--generados-anterior", dest="generados_anterior", type=Path, default=None)
    q.add_argument("--salida", type=Path, required=True)
    q.add_argument("--sin-cola", dest="sin_cola", action="store_true")
    q.add_argument("--sin-gate", dest="sin_gate", action="store_true")
    args = ap.parse_args()
    if args.cmd == "registro":
        out = registro_legible(args.md)
        args.salida.parent.mkdir(parents=True, exist_ok=True)
        args.salida.write_text(json_texto(out), encoding="utf-8")
        print(f"{sha256_path(args.salida)}  {ruta(args.salida)}: " + ", ".join(
            f"tanda {t}: {len(f)} filas, {len(out['rol_por_to_por_tanda'][t])} con alcance" for t, f in out["tandas"].items()))
        return 0
    if args.cmd == "componer":
        rep = generar_resolucion(args.ampliaciones, args.salida, args.registro_alcance,
                                 args.tandas.split(",") if args.tandas else None)
        print(json.dumps({k: rep[k] for k in ("ids_nuevos", "alias_nuevos", "indice_claves_que_pasan_a_ambiguas",
                                              "indice_claves_que_cambian_de_id")}, ensure_ascii=False))
        print(f"catálogo de resolución {rep['manifiesto']['catalogo_sha256']} ({rep['manifiesto']['n_altas']} altas, "
              f"{rep['manifiesto']['n_alcances']} alcances) en {ruta(args.salida)}")
        return 0
    return correr(args)


if __name__ == "__main__":
    raise SystemExit(main())
