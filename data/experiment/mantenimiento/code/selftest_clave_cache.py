"""
selftest_clave_cache.py — U-MANT, etapa M1 (b): qué cambio mueve la clave de
la caché local de E1 y de E3, verificado sin llamar a la API.

La clave es sha256(namespace + "\\n" + request canónico)
(data/experiment/evaluacion/llm_cache.py:110-126). Este selftest arma los
requests con el código real del pipeline —`build_request_kwargs_v3` del perfil
`v3_b54` para E1 (data/experiment/b54_catalogo_v3/code/prompt_v3_b54.py:524) y
`prompt_e3.build_request_kwargs` para E3
(data/experiment/reextraccion_v2/e3_verificador/prompt_e3.py:266)— y calcula
la clave con `compute_key`, sin importar ni construir ningún cliente de la API.

Tres bloques:

  A. Anclaje. Las claves recalculadas para las 2.434 unidades de E0 de la
     tanda 0 se buscan en la caché de E1, y las de la primera verificación de
     E3 en la caché de E3. Las dbs se abren en solo lectura
     (`mode=ro&immutable=1`): no se escribe nada en ellas. Si una db no está en
     disco (no se versionan), el bloque queda NO_VERIFICABLE y el resto corre.
  B. Variaciones, una entrada por vez, sobre una muestra fija de diez unidades
     de la tanda 0 (una por TO). Cada variación declara qué unidades deberían
     cambiar de clave en E1 y en E3; el selftest compara contra lo observado.
     Las variaciones de los catálogos JSON corren en un proceso hijo que
     redirige la lectura del JSON a una versión alterada EN MEMORIA (ningún
     archivo se escribe ni se modifica).
  C. Contraste fila por fila con la tabla de
     data/experiment/mantenimiento/tabla_reprocesamiento.md: cada fila declara
     el comportamiento de la clave de E1 y de E3 y las variaciones que la
     prueban; una discrepancia es FRENO.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B \\
      data/experiment/mantenimiento/code/selftest_clave_cache.py \\
      --out data/experiment/mantenimiento/selftest_clave_cache.json

Salida determinística (sin fechas): dos corridas dan el mismo JSON byte a byte.
Costo de API: USD 0. Sin red.
"""

from __future__ import annotations

import argparse
import ast
import builtins
import copy
import dataclasses
import hashlib
import io
import json
import os
import pathlib
import re
import sqlite3
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent                    # mantenimiento/code
REPO = AQUI.parents[3]
EXP = REPO / "data" / "experiment"
REX = EXP / "reextraccion_v2"
E0_TANDA0 = REX / "e0_chunking" / "salida_tanda0"
SALIDA_DIRIGIDA = REX / "corpus_tanda0" / "salida_dirigida"
DB_E1 = REX / "e1_extractor" / "cache" / "e1_extraccion.db"
DB_E3 = REX / "e3_verificador" / "cache" / "e3_verificacion.db"
RUNNER = REX / "corpus_v2" / "runner_corpus.py"
DIRIGIDA = SALIDA_DIRIGIDA / "reextraccion_dirigida.json"
PARTICION = EXP / "segmentacion_84" / "b584_particion"
JSON_V2 = EXP / "grafo_v2" / "esquema_v2_clases.json"
JSON_V3 = EXP / "esq_v3_miembros" / "esquema_v3_clases.json"
TABLA_MD = AQUI.parent / "tabla_reprocesamiento.md"

PERFIL = "v3_b54"          # perfil de la tanda 0 (manifiestos/tanda0_10tos.json)
TOS_TANDA0 = ("pro", "cla", "ric", "cap", "ext",
              "ctacte", "lingob", "polcre", "pagjub", "docvig")

# Muestra fija: una unidad por TO de la tanda 0, elegida para cubrir los tipos
# de unidad y de herencia de E0 (salida_tanda0/chunks_<to>.json).
MUESTRA = (
    "pro::2.3.1.1",        # punto terminal con herencia de prosa (intro)
    "cla::2.2.4::intro",   # mini-chunk
    "ric::3.1.4",          # marcado como contenido tabular por E0
    "cap::4.3.3.1",        # una de las tres unidades de la re-extracción dirigida
    "ext::7.1.1.3",        # tabular, con herencia intro y cierre
    "ctacte::1.3.1.1",     # TO nuevo de la tanda 0, con rol de alcance v3
    "lingob::1.1",         # TO nuevo, punto sin herencia de prosa
    "polcre::2.1.1",       # TO nuevo, herencia con diez bloques de cierre
    "pagjub::2.7::intro",  # mini-chunk de un TO nuevo
    "docvig::3.3.1",       # TO sin rol de alcance (hueco F1.2)
)
TO_ROL_VARIADO = "cla"     # TO cuya línea de alcance se altera (variaciones V11 y V21)
TO_NUEVO = "snp_psp"       # TO de la partición fuera de la tanda 0 (V23)
UNIDAD_TO_NUEVO = "snp_psp::1.3.1.1"
RENUMERACION = {"to": "pro", "insertar_antes_de": "2.3"}   # V24

# Módulos que corren DESPUÉS de E3 o que no arman requests: un cambio en ellos
# es «solo código». V19 verifica que ninguno se carga al armar los requests.
MODULOS_SOLO_CODIGO = ("e2_lib", "validador_e1", "ensamblar_corpus",
                       "ensamblar_r1", "ensamblar_tanda0", "r1_e4",
                       "r1_e5_esqueleto", "r1_referencias", "r1_provenance",
                       "r1_invariantes", "assemble", "manifiesto_corpus")


# ------------------------------------------------------------------------- #
# Utilidades                                                                 #
# ------------------------------------------------------------------------- #

def _rutas_import() -> None:
    for p in (REX / "e1_extractor", REX / "e3_verificador", REX / "e2_reduce", REX,
              EXP / "evaluacion"):
        if str(p) not in sys.path:
            sys.path.insert(0, str(p))


def sha256_archivo(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for bloque in iter(lambda: f.read(1 << 20), b""):
            h.update(bloque)
    return h.hexdigest()


def constantes_runner() -> dict:
    """MODEL_E1, MODEL_E3 y MAX_TOKENS_REINTENTO leídos del runner por AST, sin
    importarlo (importarlo carga el manifiesto y los clientes)."""
    arbol = ast.parse(RUNNER.read_text(encoding="utf-8"))
    out = {}
    for nodo in arbol.body:
        if isinstance(nodo, ast.Assign) and len(nodo.targets) == 1 \
                and isinstance(nodo.targets[0], ast.Name) \
                and nodo.targets[0].id in ("MODEL_E1", "MODEL_E3", "MAX_TOKENS_REINTENTO"):
            out[nodo.targets[0].id] = ast.literal_eval(nodo.value)
            out[nodo.targets[0].id + "_linea"] = nodo.lineno
    return out


def cargar_chunks(to: str, e0_dir: Path = E0_TANDA0) -> list[dict]:
    return json.loads((e0_dir / f"chunks_{to}.json").read_text(encoding="utf-8"))


def cargar_validaciones(to: str) -> dict[str, dict]:
    """Validación de E1 por unidad (salida_dirigida: igual a salida/ salvo las
    tres unidades de cap re-extraídas), con el criterio de aceptación de E3."""
    import comun_e3
    regs = comun_e3.cargar_extracciones(SALIDA_DIRIGIDA / to / "extracciones_e1_compact.jsonl")
    return {cid: r["validacion"] for cid, r in regs.items() if comun_e3.chunk_aceptado(r)}


def claves_db(db: Path, namespace: str) -> set[str] | None:
    if not db.exists():
        return None
    uri = "file:" + str(db.resolve()) + "?mode=ro&immutable=1"
    con = sqlite3.connect(uri, uri=True)
    try:
        return {k for (k,) in con.execute(
            "SELECT key FROM cache WHERE namespace = ?", (namespace,))}
    finally:
        con.close()


class Armado:
    """Arma requests y claves de E1 y E3 con el código del pipeline."""

    def __init__(self):
        _rutas_import()
        import llm_cache as lc
        import perfil_e1
        import cliente_e1
        import prompt_e3
        import cliente_e3
        self.lc = lc
        self.perfil_e1 = perfil_e1
        self.cliente_e1 = cliente_e1
        self.prompt_e3 = prompt_e3
        self.cliente_e3 = cliente_e3
        self.pf = perfil_e1.perfil(PERFIL)
        k = constantes_runner()
        self.model_e1, self.model_e3 = k["MODEL_E1"], k["MODEL_E3"]
        self.constantes = k
        self.ns_e1 = cliente_e1.namespace_e1(prefijo_hash=self.pf.prefijo_hash_para_namespace)
        self.ns_e3 = cliente_e3.namespace_e3()

    def kw_e1(self, chunk: dict, **extra) -> dict:
        return self.pf.build_request_kwargs(chunk, model=self.model_e1, **extra)

    def kw_e3(self, chunk: dict, val: dict) -> dict:
        return self.prompt_e3.build_request_kwargs(chunk, val, model=self.model_e3)

    def clave(self, ns: str, kw: dict) -> str:
        return self.lc.compute_key(ns, self.lc.canonical_request(kw))

    def k_e1(self, chunk: dict, **extra) -> str:
        return self.clave(self.ns_e1, self.kw_e1(chunk, **extra))

    def k_e3(self, chunk: dict, val: dict) -> str:
        return self.clave(self.ns_e3, self.kw_e3(chunk, val))

    @staticmethod
    def hash_prefijo(kw: dict) -> str:
        """Mismo cálculo que PREFIJO_CANONICO_V3 / PREFIJO_HASH_V3
        (prompt_v3_b54.py:516-520) y prompt_e3.PREFIJO_HASH (prompt_e3.py:213-217)."""
        canon = json.dumps({"system": kw["system"], "tools": kw["tools"]},
                           sort_keys=True, ensure_ascii=False, separators=(",", ":"))
        return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:12]


def cargar_muestra() -> tuple[dict, dict]:
    chunks, vals = {}, {}
    for cid in MUESTRA:
        to = cid.split("::", 1)[0]
        por_id = {c["id"]: c for c in cargar_chunks(to)}
        chunks[cid] = por_id[cid]
        vals[cid] = cargar_validaciones(to).get(cid)
    return chunks, vals


# ------------------------------------------------------------------------- #
# A. Anclaje contra la caché guardada                                        #
# ------------------------------------------------------------------------- #

def bloque_anclaje(ar: Armado) -> dict:
    out: dict = {"namespace_e1": ar.ns_e1, "namespace_e3": ar.ns_e3,
                 "prefijo_hash_e1": ar.pf.prefijo_hash,
                 "prefijo_hash_e3": ar.prompt_e3.PREFIJO_HASH,
                 "model_e1": ar.model_e1, "model_e3": ar.model_e3,
                 "constantes_runner": {k: v for k, v in ar.constantes.items()}}
    calc_e1: dict[str, str] = {}
    n_unidades = 0
    for to in TOS_TANDA0:
        for c in cargar_chunks(to):
            n_unidades += 1
            calc_e1[ar.k_e1(c)] = c["id"]
    out["unidades_e0_tanda0"] = n_unidades
    db1 = claves_db(DB_E1, ar.ns_e1)
    if db1 is None:
        out["e1"] = {"estado": "NO_VERIFICABLE", "motivo": "db de E1 ausente"}
    else:
        en_db = sum(1 for k in calc_e1 if k in db1)
        extra = db1 - set(calc_e1)
        # Las claves de la db que no salen del request base: se prueban contra
        # el request de la re-extracción dirigida (mismo request con max_tokens
        # de la dirigida; reextraccion_dirigida.json).
        dirigida = json.loads(DIRIGIDA.read_text(encoding="utf-8"))
        cap = {c["id"]: c for c in cargar_chunks("cap")}
        k_dir = {ar.k_e1(cap[cid], max_tokens=dirigida["max_tokens"]): cid
                 for cid in sorted(dirigida["casos"])}
        explicadas = sorted(k_dir[k] for k in extra if k in k_dir)
        out["e1"] = {
            "estado": "OK" if (en_db == n_unidades and len(extra) == len(explicadas))
            else "DISCREPANCIA",
            "claves_calculadas": len(calc_e1),
            "calculadas_presentes_en_db": en_db,
            "claves_db_en_namespace": len(db1),
            "claves_db_no_calculadas": len(extra),
            "explicadas_por_dirigida_max_tokens": {
                "max_tokens": dirigida["max_tokens"], "unidades": explicadas},
        }
    # E3: primera verificación de cada unidad aceptada por E1.
    import comun_e3
    calc_e3 = set()
    n_pares = 0
    for to in TOS_TANDA0:
        chunks = cargar_chunks(to)
        regs = comun_e3.cargar_extracciones(SALIDA_DIRIGIDA / to / "extracciones_e1_compact.jsonl")
        for c, v in comun_e3.pares_de(chunks, regs):
            n_pares += 1
            calc_e3.add(ar.k_e3(c, v))
    db3 = claves_db(DB_E3, ar.ns_e3)
    if db3 is None:
        out["e3"] = {"estado": "NO_VERIFICABLE", "motivo": "db de E3 ausente"}
    else:
        en_db3 = sum(1 for k in calc_e3 if k in db3)
        out["e3"] = {
            "estado": "OK" if en_db3 == n_pares == len(calc_e3) else "DISCREPANCIA",
            "pares_aceptados_e1": n_pares,
            "claves_calculadas": len(calc_e3),
            "calculadas_presentes_en_db": en_db3,
            "claves_db_en_namespace": len(db3),
            "nota": ("la db de E3 guarda también re-verificaciones del ratchet y "
                     "las corridas previas con el mismo namespace; solo se exige "
                     "que las claves calculadas estén"),
        }
    return out


# ------------------------------------------------------------------------- #
# B. Variaciones                                                             #
# ------------------------------------------------------------------------- #

def _primero(herencia: list[dict], prosa: bool) -> int | None:
    for i, h in enumerate(herencia):
        if (h["tipo"] != "encabezado") == prosa:
            return i
    return None


def _var_texto(c, v):
    c = copy.deepcopy(c)
    c["texto"] = c["texto"] + " [variación]"
    return c, v


def _var_herencia(prosa: bool):
    def f(c, v):
        i = _primero(c.get("herencia", []), prosa)
        if i is None:
            return None
        c = copy.deepcopy(c)
        c["herencia"][i]["texto"] = c["herencia"][i]["texto"] + " [variación]"
        return c, v
    return f


def _var_flags(c, v):
    c = copy.deepcopy(c)
    f = dict(c.get("flags") or {})
    f["contenido_tabular"] = not f.get("contenido_tabular")
    c["flags"] = f
    return c, v


def _var_paginas(c, v):
    c = copy.deepcopy(c)
    c["paginas"] = [p + 1 for p in c.get("paginas", [])]
    for h in c.get("herencia", []):
        h["paginas"] = [p + 1 for p in h.get("paginas", [])]
    return c, v


def _var_metadatos(c, v):
    c = copy.deepcopy(c)
    c["id"] = c["id"] + "__2"
    for k in ("sha256_propio", "sha256_completo"):
        if k in c:
            c[k] = "0" * 64
    for k in ("chars_propio", "chars_completo"):
        if k in c:
            c[k] = c[k] + 1
    return c, v


def _var_unidad(c, v):
    c = copy.deepcopy(c)
    vieja = c["unidad"]
    nueva = vieja + "9"
    c["unidad"] = nueva
    if c["texto"].startswith(vieja):
        c["texto"] = nueva + c["texto"][len(vieja):]
    return c, v


def _var_validacion(c, v):
    """Lo que haría una política por campo del validador: normalizar el valor
    de `tipo` de la primera entidad que lo tenga, o, si ninguna lo tiene,
    descartar la última relación."""
    if v is None:
        return None
    v = copy.deepcopy(v)
    for e in v.get("entidades", []):
        props = e.get("properties") or {}
        if "tipo" in props:
            props["tipo"] = "otra" if props["tipo"] != "otra" else "otra_2"
            return c, v
    if v.get("relaciones"):
        v["relaciones"] = v["relaciones"][:-1]
        return c, v
    return None


VARIACIONES_CHUNK = {
    # id: (descripción, transformación, E1 esperado, E3 esperado)
    "V01": ("texto propio de la unidad", _var_texto, True, True),
    "V02": ("texto de un bloque heredado de tipo encabezado", _var_herencia(False), True, True),
    "V03": ("texto de un bloque heredado de prosa (intro, cierre, chapeau, intersticial)",
            _var_herencia(True), True, False),
    "V04": ("marca de contenido tabular de E0 invertida, mismo texto", _var_flags, True, True),
    "V05": ("páginas de la unidad y de su herencia, mismo texto", _var_paginas, False, False),
    "V06": ("id, sha256 y conteos de caracteres de la unidad", _var_metadatos, False, False),
    "V07": ("número de la unidad (unidad y numeral del texto)", _var_unidad, True, True),
    "V18": ("salida validada de E1 alterada como lo haría una política por campo",
            _var_validacion, False, True),
}


def correr_variaciones_chunk(ar: Armado, chunks, vals, base_e1, base_e3) -> list[dict]:
    res = []
    for vid, (desc, fn, esp1, esp3) in VARIACIONES_CHUNK.items():
        aplica, cambia1, cambia3 = [], [], []
        for cid in MUESTRA:
            r = fn(chunks[cid], vals[cid])
            if r is None:
                continue
            c2, v2 = r
            aplica.append(cid)
            if ar.k_e1(c2) != base_e1[cid]:
                cambia1.append(cid)
            if vals[cid] is not None and ar.k_e3(c2, v2) != base_e3[cid]:
                cambia3.append(cid)
        con_e3 = [c for c in aplica if vals[c] is not None]
        res.append(_registro(vid, desc, aplica,
                             esperado_e1=aplica if esp1 else [], cambia_e1=cambia1,
                             esperado_e3=con_e3 if esp3 else [], cambia_e3=cambia3,
                             universo_e3=con_e3))
    return res


def _registro(vid, desc, aplica, *, esperado_e1, cambia_e1, esperado_e3, cambia_e3,
              universo_e3=None, extra=None, e3_aplica=True) -> dict:
    ok1 = sorted(esperado_e1) == sorted(cambia_e1)
    ok3 = (sorted(esperado_e3) == sorted(cambia_e3)) if e3_aplica else True
    reg = {
        "id": vid, "descripcion": desc, "unidades_aplicables": sorted(aplica),
        "e1": {"esperadas_que_cambian": sorted(esperado_e1),
               "observadas_que_cambian": sorted(cambia_e1),
               "token": _token(esperado_e1, cambia_e1, ok1), "ok": ok1},
        "e3": ({"esperadas_que_cambian": sorted(esperado_e3),
                "observadas_que_cambian": sorted(cambia_e3),
                "universo": sorted(universo_e3 if universo_e3 is not None else aplica),
                "token": _token(esperado_e3, cambia_e3, ok3), "ok": ok3}
               if e3_aplica else {"token": "no aplica", "ok": True}),
    }
    if extra:
        reg["detalle"] = extra
    reg["ok"] = ok1 and ok3
    return reg


def _token(esperado, observado, ok) -> str:
    if not ok:
        return "DISCREPANCIA"
    return "cambia" if observado else "no cambia"


def variaciones_request(ar: Armado, chunks, vals, base_e1, base_e3) -> list[dict]:
    """Variaciones del request completo: prefijo, tool schema, catálogo en el
    bloque, modelo y parámetros, versión de código del namespace, prompt y
    modelo de E3, tabla TO→rol en memoria y cambio de solo código."""
    res = []
    todas = list(MUESTRA)
    con_e3 = [c for c in MUESTRA if vals[c] is not None]
    v3 = sys.modules["prompt_v3_b54"]

    def e1_con(mod_kw, ns_fn=None):
        cambia = []
        hashes = set()
        for cid in MUESTRA:
            kw = copy.deepcopy(ar.kw_e1(chunks[cid]))
            mod_kw(kw)
            ns = ns_fn(kw) if ns_fn else ar.ns_e1
            hashes.add(ns)
            if ar.clave(ns, kw) != base_e1[cid]:
                cambia.append(cid)
        return cambia, sorted(hashes)

    def ns_por_prefijo(kw):
        return ar.lc.make_namespace(ar.cliente_e1.DOMAIN,
                                    code_ver=f"{ar.cliente_e1.CODE_VER}-p{ar.hash_prefijo(kw)}",
                                    thinking=False)

    # V08 prefijo de E1 (texto del sistema), con el namespace recalculado.
    def m08(kw):
        kw["system"][0]["text"] = kw["system"][0]["text"] + "\n"
    c, ns = e1_con(m08, ns_por_prefijo)
    res.append(_registro("V08", "prefijo de E1: un salto de línea al final del texto de sistema",
                         todas, esperado_e1=todas, cambia_e1=c, esperado_e3=[], cambia_e3=[],
                         universo_e3=con_e3,
                         extra={"namespace_nuevo": ns, "namespace_base": ar.ns_e1}))

    # V09 tool schema de E1.
    def m09(kw):
        kw["tools"][0]["description"] = kw["tools"][0].get("description", "") + " "
    c, ns = e1_con(m09, ns_por_prefijo)
    res.append(_registro("V09", "tool schema de E1: un espacio al final de la descripción",
                         todas, esperado_e1=todas, cambia_e1=c, esperado_e3=[], cambia_e3=[],
                         universo_e3=con_e3, extra={"namespace_nuevo": ns}))

    # V10 catálogo en el bloque del prompt (texto) y en el enum del tool schema.
    def m10(kw):
        t = kw["system"][0]["text"]
        i = t.index(v3.ANCLA_FIN_BLOQUE)
        kw["system"][0]["text"] = t[:i] + "\nSujeto_variacion_selftest — Variación" + t[i:]
    c, ns = e1_con(m10, ns_por_prefijo)
    res.append(_registro("V10", "catálogo en el bloque del prompt: una línea de sujeto más",
                         todas, esperado_e1=todas, cambia_e1=c, esperado_e3=[], cambia_e3=[],
                         universo_e3=con_e3, extra={"namespace_nuevo": ns}))

    def m10b(kw):
        props = kw["tools"][0]["input_schema"]["properties"]["relations"]["items"]["properties"]
        props["sujeto_id"]["enum"] = props["sujeto_id"]["enum"] + ["Sujeto_variacion_selftest"]
    c, ns = e1_con(m10b, ns_por_prefijo)
    res.append(_registro("V10b", "catálogo en el enum `sujeto_id` del tool schema: un id más",
                         todas, esperado_e1=todas, cambia_e1=c, esperado_e3=[], cambia_e3=[],
                         universo_e3=con_e3, extra={"namespace_nuevo": ns}))

    # V11 tabla TO→rol (línea de alcance del mensaje de usuario), en memoria.
    import prompt_e1
    archivo = next(chunks[c]["archivo"] for c in MUESTRA if chunks[c]["to"] == TO_ROL_VARIADO)
    tablas = [prompt_e1.ROL_POR_TO, v3.ROL_POR_TO_V3]
    guardado = [copy.deepcopy(t.get(archivo)) for t in tablas]
    try:
        for t in tablas:
            if t.get(archivo) is not None:
                t[archivo]["miembros_labels"] = t[archivo]["miembros_labels"][:-1]
        c11 = [cid for cid in MUESTRA if ar.k_e1(chunks[cid]) != base_e1[cid]]
        c11_e3 = [cid for cid in con_e3 if ar.k_e3(chunks[cid], vals[cid]) != base_e3[cid]]
    finally:
        for t, g in zip(tablas, guardado):
            if g is not None:
                t[archivo] = g
    esperadas = [c for c in MUESTRA if chunks[c]["to"] == TO_ROL_VARIADO]
    res.append(_registro("V11", f"tabla TO→rol en memoria: un miembro menos en el rol de {TO_ROL_VARIADO}",
                         todas, esperado_e1=esperadas, cambia_e1=c11,
                         esperado_e3=[], cambia_e3=c11_e3, universo_e3=con_e3))

    # V12 modelo de E1; V13 max_tokens; V14 temperature.
    for vid, desc, mod in (
            ("V12", "modelo de E1", lambda kw: kw.__setitem__("model", kw["model"] + "-otro")),
            ("V13", "max_tokens de E1", lambda kw: kw.__setitem__("max_tokens", kw["max_tokens"] * 2)),
            ("V14", "temperature agregada al request de E1", lambda kw: kw.__setitem__("temperature", 0.0))):
        c, _ = e1_con(mod)
        res.append(_registro(vid, desc, todas, esperado_e1=todas, cambia_e1=c,
                             esperado_e3=[], cambia_e3=[], universo_e3=con_e3))

    # V15 versión de código del cliente (CODE_VER del namespace), request idéntico.
    ns15 = ar.lc.make_namespace(ar.cliente_e1.DOMAIN,
                                code_ver=f"{ar.cliente_e1.CODE_VER}-x-p{ar.pf.prefijo_hash}",
                                thinking=False)
    c = [cid for cid in MUESTRA if ar.clave(ns15, ar.kw_e1(chunks[cid])) != base_e1[cid]]
    res.append(_registro("V15", "CODE_VER del namespace de E1, mismo request", todas,
                         esperado_e1=todas, cambia_e1=c, esperado_e3=[], cambia_e3=[],
                         universo_e3=con_e3))

    # V16 prompt de E3 (con namespace recalculado); V17 modelo de E3.
    def e3_con(mod_kw, ns_fn=None):
        cambia = []
        for cid in con_e3:
            kw = copy.deepcopy(ar.kw_e3(chunks[cid], vals[cid]))
            mod_kw(kw)
            ns = ns_fn(kw) if ns_fn else ar.ns_e3
            if ar.clave(ns, kw) != base_e3[cid]:
                cambia.append(cid)
        return cambia

    def ns3(kw):
        return ar.lc.make_namespace(ar.cliente_e3.DOMAIN,
                                    code_ver=f"{ar.cliente_e3.CODE_VER}-p{ar.hash_prefijo(kw)}",
                                    thinking=False)

    def m16(kw):
        kw["system"][0]["text"] = kw["system"][0]["text"] + "\n"
    c3 = e3_con(m16, ns3)
    res.append(_registro("V16", "prompt de E3: un salto de línea al final del texto de sistema",
                         todas, esperado_e1=[], cambia_e1=[], esperado_e3=con_e3,
                         cambia_e3=c3, universo_e3=con_e3))
    c3 = e3_con(lambda kw: kw.__setitem__("model", kw["model"] + "-otro"))
    res.append(_registro("V17", "modelo de E3", todas, esperado_e1=[], cambia_e1=[],
                         esperado_e3=con_e3, cambia_e3=c3, universo_e3=con_e3))

    # V19 solo código: perfil sin vocabulario de validación ni labels de E2, y
    # los módulos posteriores a E3 reemplazados por funciones que fallan.
    pf_mod = dataclasses.replace(ar.pf, esquema=None, labels_catalogo={})
    sabotaje = {}
    for nombre in MODULOS_SOLO_CODIGO:
        mod = sys.modules.get(nombre)
        if mod is not None:
            sabotaje[nombre] = mod
        sys.modules[nombre] = None          # un import posterior fallaría
    try:
        c19 = [cid for cid in MUESTRA
               if ar.clave(ar.ns_e1, pf_mod.build_request_kwargs(chunks[cid], model=ar.model_e1))
               != base_e1[cid]]
        c19_e3 = [cid for cid in con_e3 if ar.k_e3(chunks[cid], vals[cid]) != base_e3[cid]]
    finally:
        for nombre in MODULOS_SOLO_CODIGO:
            if nombre in sabotaje:
                sys.modules[nombre] = sabotaje[nombre]
            else:
                sys.modules.pop(nombre, None)
    res.append(_registro("V19", "solo código: perfil sin vocabulario del validador ni labels de E2, "
                         "y módulos de validación, E2, ensamblado, E4 y esqueleto bloqueados",
                         todas, esperado_e1=[], cambia_e1=c19, esperado_e3=[], cambia_e3=c19_e3,
                         universo_e3=con_e3,
                         extra={"modulos_bloqueados": list(MODULOS_SOLO_CODIGO)}))
    return res


def variacion_to_nuevo(ar: Armado) -> dict:
    """V23: una unidad de un TO que la tanda 0 no tiene, armada con el mismo
    perfil, no está en la caché (miss); las claves de la muestra no dependen
    de qué otros TOs existan (cada request es función de una sola unidad)."""
    ch = {c["id"]: c for c in cargar_chunks(TO_NUEVO, PARTICION / TO_NUEVO)}
    c = ch[UNIDAD_TO_NUEVO]
    k = ar.k_e1(c)
    db1 = claves_db(DB_E1, ar.ns_e1)
    presente = None if db1 is None else (k in db1)
    reg = _registro("V23", f"unidad de un TO nuevo ({UNIDAD_TO_NUEVO}, partición b584)",
                    [UNIDAD_TO_NUEVO],
                    esperado_e1=[UNIDAD_TO_NUEVO],
                    cambia_e1=[UNIDAD_TO_NUEVO] if presente is False else [],
                    esperado_e3=[], cambia_e3=[], e3_aplica=False,
                    extra={"clave_en_cache_e1": presente,
                           "lectura": "cambia = la clave no está en la caché (miss)"})
    if presente is None:
        reg["e1"]["token"] = "NO_VERIFICABLE"
    return reg


def _renombrar_unidad(u: str, mapa: dict[str, str]) -> str:
    for viejo, nuevo in mapa.items():
        if u == viejo or u.startswith(viejo + "."):
            return nuevo + u[len(viejo):]
    return u


RE_NUMERAL = re.compile(r"^(\d+(?:\.\d+)*)")


def _renombrar_texto(t: str, mapa: dict[str, str]) -> str:
    m = RE_NUMERAL.match(t)
    if not m:
        return t
    return _renombrar_unidad(m.group(1), mapa) + t[m.end():]


def variacion_renumeracion(ar: Armado) -> dict:
    """V24: se incorpora un punto nuevo antes de `insertar_antes_de` en un TO de
    la tanda 0; los hermanos siguientes y sus descendientes se renumeran (unidad,
    numeral del texto, unidad de origen y numeral de la herencia). Se cuentan
    las claves de E1 y E3 que cambian en todo el TO."""
    to, antes = RENUMERACION["to"], RENUMERACION["insertar_antes_de"]
    chunks = cargar_chunks(to)
    vals = cargar_validaciones(to)
    padre, ultimo = antes.rsplit(".", 1)
    nivel = antes.count(".")
    hermanos = set()
    for c in chunks:
        for u in [c["unidad"]] + [h["unidad_origen"] for h in c.get("herencia", [])]:
            partes = u.split(".")
            if len(partes) > nivel and ".".join(partes[:nivel]) == padre:
                hermanos.add(".".join(partes[:nivel + 1]))
    renum = sorted((h for h in hermanos if int(h.rsplit(".", 1)[1]) >= int(ultimo)),
                   key=lambda h: int(h.rsplit(".", 1)[1]))
    mapa = {h: f"{padre}.{int(h.rsplit('.', 1)[1]) + 1}" for h in renum}

    def afectado(c):
        us = [c["unidad"]] + [h["unidad_origen"] for h in c.get("herencia", [])]
        return any(_renombrar_unidad(u, mapa) != u for u in us)

    cambia1, cambia3, esperado, esperado3 = [], [], [], []
    for c in chunks:
        c2 = copy.deepcopy(c)
        c2["unidad"] = _renombrar_unidad(c["unidad"], mapa)
        c2["texto"] = _renombrar_texto(c["texto"], mapa)
        for h in c2.get("herencia", []):
            h["unidad_origen"] = _renombrar_unidad(h["unidad_origen"], mapa)
            h["texto"] = _renombrar_texto(h["texto"], mapa)
        if afectado(c):
            esperado.append(c["id"])
            if c["id"] in vals:
                esperado3.append(c["id"])
        if ar.k_e1(c2) != ar.k_e1(c):
            cambia1.append(c["id"])
        if c["id"] in vals and ar.k_e3(c2, vals[c["id"]]) != ar.k_e3(c, vals[c["id"]]):
            cambia3.append(c["id"])
    return _registro(
        "V24", f"punto nuevo antes de {to}::{antes}: renumeración de los hermanos siguientes "
               "y de sus descendientes", [c["id"] for c in chunks],
        esperado_e1=esperado, cambia_e1=cambia1, esperado_e3=esperado3, cambia_e3=cambia3,
        universo_e3=sorted(vals),
        extra={"to": to, "unidades_del_to": len(chunks), "puntos_renumerados": mapa,
               "unidades_afectadas_e1": len(esperado), "unidades_afectadas_e3": len(esperado3),
               "unidad_nueva": "1 (sin clave previa: miss)"})


# ------------------------------------------------------------------------- #
# Proceso hijo: catálogos JSON alterados en memoria e inventario de insumos   #
# ------------------------------------------------------------------------- #

def _instalar_redireccion(redir: dict[str, str], leidos: set[str]) -> None:
    """Redirige la lectura de los JSON de `redir` a un contenido alterado en
    memoria y registra todo archivo abierto. No escribe nada."""
    abrir_orig = builtins.open
    path_open_orig = pathlib.Path.open

    def _servir(rp, mode):
        if "b" in mode:
            return io.BytesIO(redir[rp].encode("utf-8"))
        return io.StringIO(redir[rp])

    def _open(file, mode="r", *a, **k):
        try:
            rp = str(Path(os.fspath(file)).resolve())
        except TypeError:
            return abrir_orig(file, mode, *a, **k)
        leidos.add(rp)
        if rp in redir and "r" in mode:
            return _servir(rp, mode)
        return abrir_orig(file, mode, *a, **k)

    def _path_open(self, mode="r", buffering=-1, encoding=None, errors=None, newline=None):
        rp = str(self.resolve())
        leidos.add(rp)
        if rp in redir and "r" in mode:
            return _servir(rp, mode)
        return path_open_orig(self, mode, buffering, encoding, errors, newline)

    builtins.open = _open
    io.open = _open
    pathlib.Path.open = _path_open


def _alterar(variante: str) -> dict[str, str]:
    if variante == "V20":          # JSON del esqueleto y de E4: una clase más
        d = json.loads(JSON_V3.read_text(encoding="utf-8"))
        d["clases"].append({"id": "Sujeto_variacion_selftest", "label": "Variación",
                            "nivel": "clase", "padre": "Sujeto_sujeto", "disjunta_con": [],
                            "alias": [], "provenance": {"source_doc": "selftest",
                                                        "location": "selftest"}})
        return {str(JSON_V3.resolve()): json.dumps(d, ensure_ascii=False, indent=1)}
    if variante == "V21":          # JSON v2: un miembro menos en el rol de un TO de desarrollo
        d = json.loads(JSON_V2.read_text(encoding="utf-8"))
        cambiados = 0
        for r in d["roles"]:
            if r["to"].startswith("TO_clasificacion_deudores"):
                r["miembros"] = r["miembros"][:-1]
                cambiados += 1
        assert cambiados == 1, cambiados
        return {str(JSON_V2.resolve()): json.dumps(d, ensure_ascii=False, indent=1)}
    if variante == "V22":          # JSON v2: un alias más en una clase
        d = json.loads(JSON_V2.read_text(encoding="utf-8"))
        cl = next(c for c in d["clases"] if c["id"] == "Sujeto_entidad_financiera")
        cl["alias"] = list(cl.get("alias") or []) + ["variación del selftest"]
        return {str(JSON_V2.resolve()): json.dumps(d, ensure_ascii=False, indent=1)}
    if variante == "inventario":
        return {}
    raise ValueError(variante)


def main_hijo(variante: str) -> int:
    redir = _alterar(variante)
    leidos: set[str] = set()
    _instalar_redireccion(redir, leidos)
    out: dict = {"variante": variante}
    try:
        ar = Armado()
    except Exception as exc:  # noqa: BLE001 — se reporta: el candado frena
        out["estado"] = "frena"
        out["error"] = f"{type(exc).__name__}: {str(exc)[:300]}"
        print(json.dumps(out, ensure_ascii=False, sort_keys=True))
        return 0
    repo = str(REPO.resolve())

    def _datos(conj):
        return sorted(os.path.relpath(p, repo) for p in conj
                      if p.startswith(repo) and "__pycache__" not in p
                      and "/.venv/" not in p and not p.endswith(".py"))

    # Lo leído hasta acá es lo que construye los prefijos y el perfil (al
    # importar); lo que sigue es lo que se lee por unidad.
    al_construir = set(leidos)
    chunks, vals = cargar_muestra()
    out["estado"] = "armado"
    out["e1"] = {cid: ar.k_e1(chunks[cid]) for cid in MUESTRA}
    out["e3"] = {cid: ar.k_e3(chunks[cid], vals[cid]) for cid in MUESTRA if vals[cid] is not None}
    out["datos_leidos_al_construir_prefijos_y_perfil"] = _datos(al_construir)
    out["datos_leidos_por_unidad"] = _datos(leidos - al_construir)
    out["json_redirigido_leido"] = {os.path.relpath(p, repo): (p in leidos) for p in redir}
    modulos = sorted(
        os.path.relpath(str(Path(m.__file__).resolve()), repo)
        for m in list(sys.modules.values())
        if getattr(m, "__file__", None) and str(Path(m.__file__).resolve()).startswith(repo)
        and ".venv" not in m.__file__)
    out["modulos_del_repo_cargados"] = modulos
    print(json.dumps(out, ensure_ascii=False, sort_keys=True))
    return 0


def correr_hijo(variante: str) -> dict:
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")
    r = subprocess.run([sys.executable, "-B", str(Path(__file__).resolve()),
                        "--hijo", variante], cwd=str(REPO), env=env,
                       capture_output=True, text=True, check=False)
    if r.returncode != 0:
        return {"estado": "error_hijo", "stderr": r.stderr[-800:]}
    return json.loads(r.stdout.strip().splitlines()[-1])


def variaciones_json(base_e1, base_e3, vals) -> tuple[list[dict], dict]:
    res = []
    con_e3 = [c for c in MUESTRA if vals[c] is not None]
    inv = correr_hijo("inventario")
    # Control del hijo: sin alteración reproduce las claves del padre.
    ok_inv = inv.get("e1") == base_e1 and inv.get("e3") == {c: base_e3[c] for c in con_e3}
    for vid, desc, esp1, esp3 in (
            ("V20", "JSON del esqueleto y de E4 (esquema_v3_clases.json): una clase más",
             [], []),
            ("V21", "JSON v2 (esquema_v2_clases.json): un miembro menos en el rol de cla",
             [c for c in MUESTRA if c.startswith("cla::")], []),
            ("V22", "JSON v2 (esquema_v2_clases.json): un alias más en Sujeto_entidad_financiera",
             None, None)):
        h = correr_hijo(vid)
        if h.get("estado") == "frena":
            reg = {"id": vid, "descripcion": desc, "unidades_aplicables": list(MUESTRA),
                   "e1": {"token": "frena", "ok": esp1 is None, "error": h["error"]},
                   "e3": {"token": "no aplica", "ok": True}, "ok": esp1 is None}
        elif h.get("estado") == "armado":
            c1 = [c for c in MUESTRA if h["e1"][c] != base_e1[c]]
            c3 = [c for c in con_e3 if h["e3"][c] != base_e3[c]]
            reg = _registro(vid, desc, list(MUESTRA),
                            esperado_e1=esp1 if esp1 is not None else ["<frena>"],
                            cambia_e1=c1, esperado_e3=esp3 if esp3 is not None else [],
                            cambia_e3=c3, universo_e3=con_e3,
                            extra={"json_redirigido_leido": h["json_redirigido_leido"]})
        else:
            reg = {"id": vid, "descripcion": desc, "e1": {"token": "DISCREPANCIA", "ok": False},
                   "e3": {"token": "DISCREPANCIA", "ok": False}, "ok": False,
                   "detalle": h}
        res.append(reg)
    inventario = {
        "control_reproduce_claves_del_padre": ok_inv,
        "datos_leidos_al_construir_prefijos_y_perfil":
            inv.get("datos_leidos_al_construir_prefijos_y_perfil"),
        "datos_leidos_por_unidad": inv.get("datos_leidos_por_unidad"),
        "modulos_del_repo_cargados": inv.get("modulos_del_repo_cargados"),
    }
    # V19 (complemento): ningún módulo posterior a E3 se carga al armar.
    cargados = {Path(m).stem for m in inv.get("modulos_del_repo_cargados") or []}
    inventario["modulos_solo_codigo_cargados"] = sorted(cargados & set(MODULOS_SOLO_CODIGO))
    return res, inventario


# ------------------------------------------------------------------------- #
# C. Contraste con la tabla                                                  #
# ------------------------------------------------------------------------- #

COLUMNAS = ("fila", "cambio", "entra", "recomputa", "e1", "e3", "clase",
            "principio", "ancla", "variaciones")


def leer_tabla(md: Path) -> list[dict]:
    filas = []
    for linea in md.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\|\s*F\d{2}[a-z]?\s*\|", linea):
            continue
        celdas = [c.strip() for c in linea.strip().strip("|").split("|")]
        if len(celdas) != len(COLUMNAS):
            filas.append({"fila": celdas[0], "error": f"{len(celdas)} columnas"})
            continue
        filas.append(dict(zip(COLUMNAS, celdas)))
    return filas


def contraste(md: Path, variaciones: list[dict], anclaje: dict) -> dict:
    if not md.exists():
        return {"estado": "PENDIENTE", "motivo": "tabla aún no escrita"}
    por_id = {v["id"]: v for v in variaciones}
    usados, filas_out, discrepancias = set(), [], []
    for f in leer_tabla(md):
        if "error" in f:
            discrepancias.append(f)
            continue
        ids = re.findall(r"V\d{2}b?|A[13]", f["variaciones"])
        if not ids:
            discrepancias.append({"fila": f["fila"], "motivo": "sin variación del selftest"})
        obs = []
        for i in ids:
            usados.add(i)
            if i in ("A1", "A3"):
                est = anclaje["e1" if i == "A1" else "e3"]["estado"]
                obs.append({"variacion": i, "anclaje": est})
                if est == "DISCREPANCIA":
                    discrepancias.append({"fila": f["fila"], "variacion": i, "anclaje": est})
                continue
            v = por_id.get(i)
            if v is None:
                discrepancias.append({"fila": f["fila"], "variacion": i, "motivo": "no existe"})
                continue
            t1, t3 = v["e1"]["token"], v["e3"]["token"]
            # E3 «no aplica»: la variación no puede armar el request de E3 (no
            # hay salida de E1 previa); la fila se contrasta solo en E1.
            coincide = _norm(f["e1"]) == t1 and (t3 == "no aplica" or _norm(f["e3"]) == t3)
            obs.append({"variacion": i, "e1": t1, "e3": t3, "coincide": coincide})
            if not coincide or not v["ok"]:
                discrepancias.append({"fila": f["fila"], "variacion": i,
                                      "tabla": [f["e1"], f["e3"]], "selftest": [t1, t3]})
        filas_out.append({"fila": f["fila"], "tabla_e1": f["e1"], "tabla_e3": f["e3"],
                          "clase": f["clase"], "observado": obs})
    sin_fila = sorted(set(por_id) - usados)
    for i in sin_fila:
        discrepancias.append({"variacion": i, "motivo": "variación sin fila en la tabla"})
    return {"estado": "OK" if not discrepancias else "FRENO",
            "filas": filas_out, "discrepancias": discrepancias}


def _norm(celda: str) -> str:
    """Primer token de la celda de la tabla: `cambia`, `no cambia`, `frena`
    o `no aplica` (lo que sigue, entre paréntesis, es el alcance)."""
    c = celda.split("(")[0].strip().strip("*").strip().lower()
    return c


# ------------------------------------------------------------------------- #
# main                                                                       #
# ------------------------------------------------------------------------- #

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hijo", default=None)
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    if a.hijo:
        return main_hijo(a.hijo)

    ar = Armado()
    chunks, vals = cargar_muestra()
    base_e1 = {cid: ar.k_e1(chunks[cid]) for cid in MUESTRA}
    base_e3 = {cid: ar.k_e3(chunks[cid], vals[cid]) for cid in MUESTRA if vals[cid] is not None}

    anclaje = bloque_anclaje(ar)
    variaciones = correr_variaciones_chunk(ar, chunks, vals, base_e1, base_e3)
    variaciones += variaciones_request(ar, chunks, vals, base_e1, base_e3)
    vj, inventario = variaciones_json(base_e1, base_e3, vals)
    variaciones += vj
    variaciones.append(variacion_to_nuevo(ar))
    variaciones.append(variacion_renumeracion(ar))
    variaciones.sort(key=lambda v: v["id"])
    ok_inv = inventario["control_reproduce_claves_del_padre"] \
        and not inventario["modulos_solo_codigo_cargados"]

    resultado = {
        "selftest": "U-MANT M1 — clave de caché de E1 y E3",
        "perfil_e1": PERFIL,
        "insumos": {
            "e0_tanda0": {to: sha256_archivo(E0_TANDA0 / f"chunks_{to}.json")
                          for to in TOS_TANDA0},
            "tabla_md_presente": TABLA_MD.exists(),
        },
        "muestra": {cid: {"tipo": chunks[cid]["tipo"],
                          "herencia": [h["tipo"] for h in chunks[cid].get("herencia", [])],
                          "flags_tabular": bool((chunks[cid].get("flags") or {}).get("contenido_tabular")),
                          "con_validacion_e1": vals[cid] is not None,
                          "clave_e1": base_e1[cid], "clave_e3": base_e3.get(cid)}
                    for cid in MUESTRA},
        "anclaje": anclaje,
        "inventario_del_armado": inventario,
        "variaciones": variaciones,
    }
    resultado["contraste_tabla"] = contraste(TABLA_MD, variaciones, anclaje)
    fallas = [v["id"] for v in variaciones if not v["ok"]]
    anclaje_ok = all(anclaje[k]["estado"] in ("OK", "NO_VERIFICABLE") for k in ("e1", "e3"))
    resultado["veredicto"] = (
        "OK" if not fallas and anclaje_ok and ok_inv
        and resultado["contraste_tabla"]["estado"] in ("OK", "PENDIENTE") else "FRENO")
    resultado["variaciones_con_discrepancia"] = fallas

    texto = json.dumps(resultado, ensure_ascii=False, indent=1, sort_keys=True) + "\n"
    if a.out:
        Path(a.out).write_text(texto, encoding="utf-8")
    for v in variaciones:
        print(f"{v['id']:5s} e1={v['e1']['token']:<12s} e3={v['e3']['token']:<12s} "
              f"{'OK ' if v['ok'] else 'MAL'} {v['descripcion']}")
    print("anclaje e1:", anclaje["e1"].get("estado"), "| e3:", anclaje["e3"].get("estado"))
    print("inventario: hijo reproduce =", inventario["control_reproduce_claves_del_padre"],
          "| módulos solo-código cargados =", inventario["modulos_solo_codigo_cargados"])
    print("contraste con la tabla:", resultado["contraste_tabla"]["estado"])
    print("VEREDICTO:", resultado["veredicto"])
    return 0 if resultado["veredicto"] == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
