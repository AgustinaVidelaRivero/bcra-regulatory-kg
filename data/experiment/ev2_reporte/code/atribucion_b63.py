#!/usr/bin/env python3
"""atribucion_b63.py — La atribución determinística de fallas sobre las sesiones del brazo del grafo de B6.3 (etapa AT1 de
ATRIB_B63: el código, probado con datos de juguete y sellado; corre sobre los datos reales recién en la AT2). USD 0: no llama
a ningún modelo, no abre Neo4j ni el codificador y no escribe fuera de --salida, --material y --clave.

La regla: `regla_atribucion.md` con su enmienda 1, firmada en df3b6d39 (`enmienda1_regla_atribucion_navegacion.md`,
`27b91460…`): las cuatro clases y su precedencia, la presencia en el grafo del banco (AnclaIndexBanco), las v1 del log R1 y
las siete de navegación (atribucion_fallas_nav.atribuir_payload, `e6759185…`), sobre el payload de adaptador_banco_nav.py
(`d14756fd…`), los dos importados sin editarlos.

Lo que hace (`correr`):
  1. la población: las corridas de B6.3 con su veredicto final, el de después de la lectura tolerante y de la adjudicación de
     la autora, calculado con las funciones del código sellado del análisis (`b63/analisis/codigo/analizar_b63.py`, la etapa B,
     `9a9d0491…`), importadas sin editarlas, en el mismo orden y con los mismos frenos que su `analizar`: importar el clon,
     la entrada sellada, el banco contra su manifiesto, corridas_de, los agregados y la adjudicación (planilla_sellada,
     adjudicar, sin_requiere) y estado_de. Cada entrada, con su sha256 (el de ESPERADO del análisis o el de su sello). Del
     brazo `kg`: las completas con veredicto entran (las `correcto` van al denominador, sin clase, como en el §1 de la regla);
     son atribuibles las de veredicto parcial o incorrecto (atribucion_fallas.VEREDICTOS_ATRIBUIBLES). Las demás no tienen
     veredicto y se declaran por estado; las incompleta_otra, también por motivo, como en analizar_b63.declarado;
  2. cada sesión con veredicto: su stream, su sesión y su log R1 de banco_b63/resultados/real/, cada uno contra el manifiesto
     commiteado (Banco.leer); el payload, de adaptador_banco_nav.adaptar sobre el stream y el log; las anclas de su pregunta,
     del archivo de las preguntas que nombra la entrada sellada, por su ruta exacta y con su sha256; AnclaIndexBanco.desde_indice
     sobre el índice por punto del grafo evaluado. Las anclas con un rango (`..` en su unidad, sin `::`) se leen como en el punto
     4 del análisis: sus unidades, de exactitud_de_cita_9_4_b63.unidades_de_las_anclas (analizar_b63.expandir sobre arbol_e0),
     importada sin editarla (`5207941b…`), y el ancla resuelve a los nodos de todas sus unidades (`AnclasConRangos`, un
     envoltorio de `resolver`). Las demás, tal cual. Después, atribuir_payload(..., log_r1=...) con las v1 del log. Una
     sesión que el adaptador no reconcilia con su log, o un control del log que falla (corrida_valida), frena la corrida
     entera antes de escribir ninguna cifra;
  3. la salida (--salida/atribucion_B63.json), sin ningún texto ni id de pregunta: por sesión, su id opaco, su clase, su
     veredicto, su tipo y sus campos de vista y consulta (por posición de ancla, sin el ancla); las cuentas por clase y por
     tipo; las anclas de las preguntas que resuelven a algún nodo, por forma, tal cual y con la lectura de los rangos; los
     pedidos a un nombre que no es una herramienta; lo declarado de la enmienda y de esta etapa;
  4. la última clase, `generacion`: si son más de 10, se sortean 10 con random.Random("B63:atribucion:ultima_clase:v1").sample
     sobre sus ids opacos ordenados (D-6, docs/preregistro_B6_3_evaluacion_final.md:494-495), y van F01 a F10 en el orden del
     sorteo; si son 10 o menos, entran todas, en el orden de sus ids. El material de la autora, en --material (fuera del
     repo): una ficha por caso (la pregunta, sus criterios con su marca final, la respuesta, el ancla y los pasos de la traza
     que la vieron o la consultaron), la planilla vacía y su estructura. La clave (ficha -> id opaco, sesión, pregunta), en
     --clave, aparte.

`sellar`: el sellador de la planilla, con la forma que lee analizar_b63.planilla_sellada (el renglón «sha256  bytes  hora
nombre»): controla las columnas, los renglones y los valores contra la estructura, y sella una sola vez.

  python3 -I -B atribucion_b63.py correr --clon <b63/v2/b2 de una copia de HEAD> --entrada … (ver --help) --salida <carpeta nueva>
      --material <carpeta nueva, fuera del repo> --clave <archivo nuevo, fuera del repo>
  python3 -I -B atribucion_b63.py sellar --planilla … --estructura … --sello …
`correr` imprime solo la salida y su sha256, o «FRENO: …» (sale con 10), o el tipo de un error inesperado y su renglón en este
archivo, sin su mensaje (sale con 12): ninguna cifra, ningún id, ninguna ancla.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import importlib.util
import io
import json
import random
import re
import sys
import traceback
import unicodedata
from collections import Counter
from datetime import datetime
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO_DIR = AQUI.parents[3]
ADAPTADOR_DIR = REPO_DIR / "data" / "experiment" / "banco_mcp" / "adaptador"
for _p in (str(AQUI), str(ADAPTADOR_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import atribucion_fallas_nav as NAV  # noqa: E402  (HEAD, sin editar)
import adaptador_banco_nav as ABN  # noqa: E402  (HEAD, sin editar)

AF = NAV.AF
CODIGO_ANALISIS = REPO_DIR / "data" / "experiment" / "banco_mcp" / "b63" / "analisis" / "codigo"
ENMIENDA = REPO_DIR / "data" / "experiment" / "ev2_reporte" / "enmienda1_regla_atribucion_navegacion.md"
SHA = {"analizar_b63": "9a9d04914c17b0e5604d8f6144f6ef84fc6b37ae3318b0a434d7bbf5ab3cdceb",
       "exactitud_de_cita_9_4_b63": "5207941b4a54dd2e7071e5d1438fe0b664c0cfd2df56794614ab56de4e6f272a",
       "enmienda": "27b91460d71b3ddbb7b5f3b74bc8ac05d27e6bbc40957c82524dcc53acdca98f",
       "atribucion_fallas_nav": "e6759185b0b66b9804a58e11f7f92794d96307223d7dafd1f0b9d8f22fa7a1c5",
       "adaptador_banco_nav": "d14756fd359441aaa5c378e5e00f9cd5b97e0afce02e59ceae4543ed615218d2",
       "manifiesto_indice": "ef036b67032175f32996513a81198f65ed29850bc336ba35ae445f7f20c152d6"}
DEL_ANALISIS = ("entrada", "manifiesto_fuera", "agregados", "agregados_tolerante", "veredictos_tolerante",
                "estructura_planilla", "clave_adjudicacion", "armado_e0", "kg", "mapping", "juez_b63",
                "aplicar_lectura_tolerante_b63")
SEMILLA = "B63:atribucion:ultima_clase:v1"
ULTIMA_CLASE = "generacion"
N_CASOS = 10
COLUMNAS_PLANILLA = ["ficha", "la_clase_se_sostiene", "comentario"]
VALORES_PLANILLA = ("sí", "no", "no decidible")
FORMAS = ("sin_rango", "con_un_rango", "las_demas")
ARGS = ("clon", "entrada", "manifiesto_fuera", "banco_b63", "agregados", "agregados_tolerante", "veredictos_tolerante",
        "planilla", "sello_planilla", "estructura_planilla", "clave_adjudicacion", "e0", "armado_e0", "indice")

DECISIONES = {
    "la_enmienda": "La enmienda 1 a la regla de atribución, firmada con el 234 (df3b6d39): las reglas de contenedores, de las "
                   "v1 del log R1 y de las herramientas de navegación, como están en HEAD. (decisiones de la autora del "
                   "29/10/2026, 14:01:46 y 15:04:55)",
    "la_ultima_clase": "La última clase de la atribución, de la que la autora lee hasta 10 casos, es generacion (G): la última "
                       "en el orden de las clases del código (atribucion_fallas.py:64) y del embudo; los casos en que el agente "
                       "consultó el ancla y la respuesta igual salió parcial o incorrecta. (decisión de la autora del "
                       "29/10/2026, 15:04:55)",
    "la_semilla": "B63:atribucion:ultima_clase:v1 (D-6, docs/preregistro_B6_3_evaluacion_final.md:494-495)",
    "las_anclas_con_un_rango": "Se leen como en el punto 4 del análisis: las unidades de un rango salen de expandir sobre "
                               "arbol_e0 del código sellado de la B, y el ancla resuelve a los nodos de todas sus unidades; las "
                               "demás anclas, tal cual.",
}
DECLARADO_DE_LA_ENMIENDA = {
    "la_presencia": "AnclaIndexBanco sobre el kg.json del grafo evaluado (el kg_path del manifiesto de su índice por punto, con "
                    "su sha256): punto exacto; contenedores, los nodos de más de 10 claves y los TextoOrdenado (§2 y §6, i)",
    "las_v1_del_banco": "leídas del log R1, controladas con su output_sha256, R7 y la salida de la sesión; un control que falla "
                        "invalida la corrida entera (§3 y §6, j y k)",
    "las_de_navegacion": "vista y consultada de la opción (a), leídas del texto del log R1 (§1 y §3)",
    "los_pedidos_sin_herramienta": "un pedido a un nombre que no es una herramienta no llegó al servidor: no es vista ni consulta "
                                   "y se cuenta aparte (§4)",
    "las_interpretaciones": "las a a h del §6, aceptadas por la autora el 29/10/2026 (11:51:20), y las i, j y k de la v2",
}
IMPLEMENTACION = {
    "la_poblacion": "la de analizar_b63.analizar, hasta el estado de cada corrida, con sus mismas funciones y frenos; del "
                    "brazo kg entran las completas con veredicto (las correcto, sin clase, en el denominador)",
    "las_anclas": "todas las de la pregunta (P[q]['anclas'], cada una por su unidad), como en la exactitud de cita del análisis; "
                  "presente, vista o consultada si alguna lo está (la regla multi-ancla del §2 de la regla)",
    "las_formas": "con_un_rango: «..» en la unidad (después de «to::») y sin «::» (la que expandir lee como rango); las_demas: "
                  "una unidad con «::» (un sufijo o un subdocumento); sin_rango: el resto. Cuentan las anclas de todas las "
                  "preguntas de la entrada, una vez por pregunta y posición",
    "los_archivos_de_la_sesion": "stream_<id>.jsonl, sesion_<id>.jsonl y log_r1_<id>.jsonl, cada uno contra el manifiesto "
                                 "commiteado; el payload, del stream y del log; el log que lee la atribución es el mismo que "
                                 "se controló (sus bytes, y su sha256 contra el que registra el adaptador)",
    "el_freno": "una sesión con veredicto que el adaptador no reconcilia con su log R1 (rechazos de R7) o que no es atribuible, "
                "o una corrida_valida falsa, frena la corrida antes de escribir --salida, --material y --clave",
    "las_fichas": "en el orden del sorteo (más de 10) o de los ids opacos (10 o menos); cada ficha, sin el id opaco ni la "
                  "sesión; los pasos que vieron o consultaron un ancla, de por_ancla de la atribución (los eventos de las "
                  "herramientas de navegación y los nodos vistos o consultados por las v1)",
    "el_sello": "el renglón «sha256  bytes  hora  nombre» que lee analizar_b63.planilla_sellada; una planilla se sella una "
                "sola vez",
}


class Freno(Exception):
    pass


def frena(m: str):
    raise Freno(m)


def sha_b(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def sha_archivo(p: Path) -> str:
    return sha_b(Path(p).read_bytes())


def plegar(s: str) -> str:
    s = unicodedata.normalize("NFD", (s or "").strip().lower())
    return " ".join("".join(c for c in s if unicodedata.category(c) != "Mn").replace("_", " ").split())


# --------------------------------------------------------------------------------------------------------------------- #
# El código sellado del análisis, importado sin editarlo                                                               #
# --------------------------------------------------------------------------------------------------------------------- #
def cargar_codigo_analisis(d: Path):
    """analizar_b63 y exactitud_de_cita_9_4_b63, de su carpeta, con el sha256 de cada archivo antes de importarlo."""
    d = Path(d)
    for nombre in ("analizar_b63", "exactitud_de_cita_9_4_b63"):
        if sha_archivo(d / f"{nombre}.py") != SHA[nombre]:
            frena(f"{nombre}.py no es el de HEAD")
    mods = []
    for nombre in ("analizar_b63", "exactitud_de_cita_9_4_b63"):
        if nombre in sys.modules:
            m = sys.modules[nombre]
            if sha_archivo(Path(m.__file__)) != SHA[nombre]:
                frena(f"el {nombre} importado no es el de HEAD")
        else:
            spec = importlib.util.spec_from_file_location(nombre, d / f"{nombre}.py")
            m = importlib.util.module_from_spec(spec)
            sys.modules[nombre] = m
            spec.loader.exec_module(m)
        mods.append(m)
    A, X = mods
    if X.A is not A:
        frena("exactitud_de_cita_9_4_b63 no importó el mismo analizar_b63")
    return A, X


def esperado_de(A) -> dict:
    return {k: A.ESPERADO[k] for k in DEL_ANALISIS} | {"manifiesto_indice": SHA["manifiesto_indice"]}


# --------------------------------------------------------------------------------------------------------------------- #
# 1. La población                                                                                                       #
# --------------------------------------------------------------------------------------------------------------------- #
def poblacion(A, rutas: dict, esperado: dict, importar=None) -> dict:
    """Lo de analizar_b63.analizar hasta el estado de cada corrida, con sus funciones y sus frenos, más el control del
    archivo de las preguntas por la ruta exacta y el sha256 que nombra la entrada sellada."""
    AP, JB = (importar or A.importar)(rutas["clon"], esperado)
    K, M = JB.K, JB.M
    entrada_b = A.controlado(rutas["entrada"], esperado["entrada"], "la entrada sellada")
    e = AP.cargar_entrada(rutas["entrada"], K)
    pr = json.loads(entrada_b)["preguntas"]
    ruta_p = Path(pr["ruta"]).expanduser()
    if not ruta_p.is_absolute():                       # la de B6.3 empieza con «~»; una relativa vale desde la entrada
        ruta_p = Path(rutas["entrada"]).parent / ruta_p
    if Path(e["_rutas"]["preguntas"]).expanduser().resolve() != ruta_p.resolve():
        frena("la entrada no carga el archivo de preguntas que nombra")
    A.controlado(ruta_p, pr["sha256"], "el archivo de las preguntas")
    P = A.cargar_preguntas_crudas(e)
    qids = list(e["preguntas"]["ids_en_orden"])
    if A.BRAZO_GRAFO not in e["brazos"] or any(P[q]["tipo"] not in A.TIPOS for q in qids):
        frena("los brazos o los tipos de la entrada no son los del pre-registro")
    banco = A.Banco(rutas["banco_b63"], rutas["manifiesto_fuera"], esperado)
    corridas = A.corridas_de(banco, e, K, JB, AP)
    corrida_de = {c["id_opaco"]: c for c in corridas if c["id_opaco"]}

    agg = json.loads(A.controlado(rutas["agregados"], esperado["agregados"], "los agregados de la lectura tolerante"))
    agregados = {x["id_opaco"]: x for x in agg["agregados"]}
    tol = {x["id_opaco"]: x for x in json.loads(A.controlado(rutas["agregados_tolerante"], esperado["agregados_tolerante"],
                                                             "los agregados de las que no se leían"))["agregados"]}
    if any(agregados.get(i) != x for i, x in tol.items()):
        frena("las que no se leían no están tal cual en los agregados")
    vtol = [json.loads(l) for l in A.controlado(rutas["veredictos_tolerante"], esperado["veredictos_tolerante"],
                                                "los veredictos de la lectura tolerante").decode("utf-8").splitlines() if l.strip()]
    if set(agregados) - set(corrida_de) or {x["id_opaco"] for x in vtol} - set(tol):
        frena("un id de los agregados no es una corrida completa")
    planilla_b = A.planilla_sellada(rutas["planilla"], rutas["sello_planilla"])
    estructura_b = A.controlado(rutas["estructura_planilla"], esperado["estructura_planilla"], "la estructura de la planilla")
    clave = json.loads(A.controlado(rutas["clave_adjudicacion"], esperado["clave_adjudicacion"], "la clave de la adjudicación"))
    adjudicadas = A.adjudicar(agregados, planilla_b, estructura_b, clave, M, corrida_de)
    veredictos = {i: {"veredicto_pregunta": (adjudicadas[i] if i in adjudicadas else a)["veredicto_pregunta"]}
                  for i, a in agregados.items()}
    A.sin_requiere(veredictos)
    for c in corridas:
        c["estado"] = A.estado_de(c, veredictos)
    modales = {i: (adjudicadas[i] if i in adjudicadas else a)["modales"] for i, a in agregados.items()}
    return {"e": e, "P": P, "qids": qids, "banco": banco, "corridas": corridas, "veredictos": veredictos,
            "modales": modales, "adjudicadas": adjudicadas}


def declarar_sin_veredicto(A, banco, kg: list) -> dict:
    """Las corridas del brazo kg sin veredicto, por estado; las incompleta_otra, por motivo, como analizar_b63.declarado."""
    inc = [c for c in kg if c["clasificacion"] == "incompleta_otra"]
    motivos, falta = Counter(), 0
    for c in inc:
        meta = A.meta_sin_texto(banco, c)
        if meta is None:
            frena("una incompleta_otra sin su meta sin texto")
        r7 = meta.get("mapa_R7") or []
        motivos["; ".join(re.sub(r"\b\d+\b", "n", m) for m in ((meta.get("completitud_R3") or {}).get("motivos_incompleta") or []))] += 1
        falta += bool(r7) and r7[-1].get("tool") == "mcp__kg" and r7[-1].get("call_id_log") is None \
            and sum(1 for x in r7 if x.get("call_id_log") is None) == 1
    return {"por_estado": dict(sorted(Counter(c["estado"] for c in kg if c["estado"] not in ("correcta", "no_correcta")).items())),
            "incompleta_otra": {"total": len(inc), "por_motivo": dict(sorted(motivos.items())),
                                "con_la_llamada_que_falta": falta}}


# --------------------------------------------------------------------------------------------------------------------- #
# 2. Las anclas y cada sesión                                                                                           #
# --------------------------------------------------------------------------------------------------------------------- #
def forma_de(ancla: str) -> str:
    u = ancla.split("::", 1)[1] if "::" in ancla else ancla
    if "::" in u:
        return "las_demas"
    return "con_un_rango" if ".." in u else "sin_rango"


class AnclasConRangos:
    """El índice de anclas que recibe atribuir_payload: un ancla con un rango resuelve a los nodos de todas sus unidades (las
    de unidades_de_las_anclas del punto 4); las demás, tal cual, por el índice de base (AnclaIndexBanco)."""

    def __init__(self, base, unidades: dict):
        self.base, self.unidades = base, unidades

    def resolver(self, to: str, ancla: str, **kw) -> list:
        clave = f"{to}::{ancla}"
        us = self.unidades.get(clave)
        if forma_de(clave) != "con_un_rango" or not us:
            return self.base.resolver(to, ancla, **kw)
        ids = []
        for u in us:
            t, _, r = u.partition("::")
            for nid in self.base.resolver(t, r, **kw):
                if nid not in ids:
                    ids.append(nid)
        return ids

    def censo(self, anclas: list) -> dict:
        resueltas, ausentes, nodos = {}, [], []
        for a in anclas:
            ids = self.resolver(a["to"], a["ancla"])
            if ids:
                resueltas[(a["to"], a["ancla"])] = ids
                nodos += [n for n in ids if n not in nodos]
            else:
                ausentes.append((a["to"], a["ancla"]))
        return {"resueltas": resueltas, "ausentes": ausentes, "nodos_gold": nodos}


def leer_log_de_bytes(b: bytes) -> dict:
    lineas = [json.loads(x) for x in b.decode("utf-8").splitlines() if x.strip()]
    return {"llamadas": [x for x in lineas if x.get("evento") == "llamada"]}


def atribuir_sesion(c: dict, dir_sesion: Path, leer, anclas: list, ai, lectura: dict, veredicto: str) -> tuple[dict, dict]:
    """(payload, atribución) de una sesión del brazo kg, con cada archivo controlado por `leer` (Banco.leer)."""
    sid = c["sesion"]
    stream, sesion, log = (Path(dir_sesion) / f"stream_{sid}.jsonl", Path(dir_sesion) / f"sesion_{sid}.jsonl",
                           Path(dir_sesion) / f"log_r1_{sid}.jsonl")
    leer(stream)
    leer(sesion)
    log_b = leer(log)
    p = ABN.adaptar(stream, log, {"caso_id": c["id_opaco"]})
    if p["meta"]["log_r1_sha256"] != sha_b(log_b):
        frena("el log R1 de una sesión no es el que se controló")
    if p["gate"]["rechazos"] or not p["gate"]["atribuible"]:
        frena("una sesión con veredicto que el adaptador no reconcilia con su log R1 o no es atribuible")
    at = NAV.atribuir_payload(p, anclas, ai, None, veredicto, lectura, log_r1=leer_log_de_bytes(log_b))
    return p, at


def registro(c: dict, veredicto: str, tipo: str, p: dict, at: dict) -> dict:
    """Lo de una sesión que va a la salida: sin anclas, sin ids de nodo, sin texto."""
    por_ancla = []
    for i, (a, pa) in enumerate(at["por_ancla"].items(), 1):
        por_ancla.append({"posicion": i, "forma": forma_de(a), "presente": pa["presente"], "n_nodos": pa["n_nodos_censo"],
                          "vista": pa["vista"], "consultada": pa["consultada"],
                          "vista_en_step": pa.get("vista_en_step"), "consultada_en_step": pa.get("consultada_en_step"),
                          "consultada_via": pa.get("consultada_via", []),
                          "vias_de_la_vista_por_navegacion": sorted({x["via"] for x in (pa.get("navegacion") or {}).get("vista", [])})})
    return {"id_opaco": c["id_opaco"], "veredicto": veredicto, "clase": at["clase"], "tipo": tipo,
            "ancla_presente": at["ancla_presente"], "ancla_vista": at["ancla_vista"], "ancla_consultada": at["ancla_consultada"],
            "por_ancla": por_ancla, "n_steps": at["n_steps"], "tool_calls_used": at["tool_calls_used"],
            "por_herramienta": dict(sorted(Counter(s["tool"] for s in p["trace"]["steps"]).items())),
            "respondible_flag": at["respondible_flag"], "replay_ok": at["replay_ok"], "replay_fuerte_ok": at["replay_fuerte_ok"],
            "pedidos_sin_herramienta": p["banco"]["pedidos_sin_herramienta"]["n"]}


# --------------------------------------------------------------------------------------------------------------------- #
# 4. La última clase: el sorteo, las fichas, la planilla y su sello                                                    #
# --------------------------------------------------------------------------------------------------------------------- #
def sortear(ids: list) -> list:
    """Hasta N_CASOS: con más, random.Random(SEMILLA).sample sobre los ids ordenados, en el orden del sorteo; si no, todos."""
    orden = sorted(ids)
    if len(orden) <= N_CASOS:
        return orden
    return random.Random(SEMILLA).sample(orden, N_CASOS)


def pasos_del_ancla(p: dict, at: dict) -> list:
    """[(n, herramienta, entrada, [qué hizo con qué ancla])]: los steps que vieron o consultaron alguna ancla."""
    steps = {s["n"]: s for s in p["trace"]["steps"]}
    por_n: dict = {}
    for i, (_, pa) in enumerate(at["por_ancla"].items(), 1):
        if not pa.get("presente"):
            continue
        nav = pa.get("navegacion") or {}
        for ev in nav.get("vista", []):
            por_n.setdefault(ev["n"], []).append(f"vio el ancla {i} ({ev['via'].replace('_', ' ')})")
        for ev in nav.get("consultada", []):
            por_n.setdefault(ev["n"], []).append(f"consultó el ancla {i} (su texto, por {ev['via']})")
        for nd in pa.get("por_nodo", []):
            if nd.get("visto_en_step") is not None and steps.get(nd["visto_en_step"], {}).get("tool") in NAV.TOOLS_V1:
                por_n.setdefault(nd["visto_en_step"], []).append(f"vio un nodo del ancla {i}")
            if nd.get("consultado_en_step") is not None:
                por_n.setdefault(nd["consultado_en_step"], []).append(f"consultó un nodo del ancla {i} (por {nd['consultado_via']})")
    return [(n, steps[n]["tool"], steps[n].get("input"), sorted(set(q))) for n, q in sorted(por_n.items()) if n in steps]


def ficha(nombre: str, q: dict, veredicto: str, modales: list, p: dict, at: dict, unidades: list) -> str:
    fj = p["trace"].get("final_json") or {}
    L = [f"# {nombre}: ¿la clase «{ULTIMA_CLASE}» se sostiene?", "",
         f"La atribución dice que el agente consultó el ancla y la respuesta igual salió «{veredicto}».", "",
         f"- Tipo de pregunta: {q.get('tipo')}", "", "## La pregunta", "", str(q.get("pregunta", "")), "",
         "## Sus criterios, con la marca final (la del juez o la de la adjudicación)", ""]
    for k, cr in enumerate(q.get("criterios") or [], 1):
        marca = modales[k - 1] if k - 1 < len(modales) else "—"
        L += [f"{k}. {cr.get('criterio', '')} — **{marca}**", f"   - Cita: «{cr.get('cita_textual', '')}» ({cr.get('unidad', '')})"]
    L += ["", "## La respuesta", "", str(fj.get("respuesta", "")), "", "Sus citas:", ""]
    L += [f"- {json.dumps(x, ensure_ascii=False)}" for x in (fj.get("citas") or [])] or ["- (sin citas)"]
    L += ["", "## El ancla", ""]
    for i, (a, us) in enumerate(zip(q.get("anclas") or [], unidades), 1):
        pa = at["por_ancla"].get(a["unidad"], {})
        extra = f"; sus unidades: {', '.join(us)}" if us != [a["unidad"]] else ""
        L.append(f"- Ancla {i} ({a.get('rol', '')}): {a['unidad']}{extra} · nodos: {pa.get('n_nodos_censo', 0)} · "
                 f"vista: {'sí' if pa.get('vista') else 'no'} · consultada: {'sí' if pa.get('consultada') else 'no'}")
    L += ["", "## Los pasos de la traza que la vieron o la consultaron", "", "| step | herramienta | entrada | qué hizo |",
          "|---|---|---|---|"]
    for n, tool, inp, que in pasos_del_ancla(p, at):
        entrada = json.dumps(inp, ensure_ascii=False).replace("|", "¦")
        L.append(f"| {n} | {tool} | {entrada} | {'; '.join(que)} |")
    L += ["", f"En la planilla, para {nombre}: «la clase se sostiene» (sí, no o no decidible) y un comentario libre.", ""]
    return "\n".join(L)


def leer_csv(b: bytes) -> tuple[list, list]:
    """Como el lector de analizar_b63 (leer_csv): acepta «,» o «;» y el BOM."""
    t = b.decode("utf-8-sig")
    pr = t.splitlines()[0] if t else ""
    d = ";" if pr.count(";") > pr.count(",") else ","
    filas = [f for f in csv.reader(io.StringIO(t), delimiter=d) if any(x.strip() for x in f)]
    if not filas:
        frena("un CSV vacío")
    return [c.strip() for c in filas[0]], [[c.strip() for c in f] for f in filas[1:]]


def sellar(planilla: Path, estructura: Path, sello: Path, hora: str | None = None) -> tuple[str, str]:
    """Controla la planilla contra su estructura y agrega al sello el renglón «sha256  bytes  hora  nombre»."""
    b = Path(planilla).read_bytes()
    est = json.loads(Path(estructura).read_text(encoding="utf-8"))
    cols, filas = leer_csv(b)
    if cols != est["columnas"] or [f[:1] for f in filas] != est["renglones"]:
        frena("la planilla no tiene las columnas y los renglones de su estructura")
    admitidos = {plegar(v) for v in est["valores_admitidos"]}
    for f in filas:
        if len(f) < 2 or plegar(f[1]) not in admitidos:
            frena("un valor de «la clase se sostiene» no es sí, no ni no decidible")
    previo = Path(sello).read_text(encoding="utf-8") if Path(sello).is_file() else ""
    if any(l.split() and l.split()[-1] == Path(planilla).name for l in previo.splitlines() if not l.startswith("#")):
        frena("la planilla ya tiene su sello")
    hora = hora or datetime.now().isoformat(timespec="seconds")
    renglon = f"{sha_b(b)}  {len(b)}  {hora}  {Path(planilla).name}\n"
    cabeza = "" if previo else "# el sello de la planilla de la atribución de B6.3: sha256  bytes  hora  nombre\n"
    Path(sello).write_text(previo + cabeza + renglon, encoding="utf-8")
    return sha_b(b), hora


# --------------------------------------------------------------------------------------------------------------------- #
# La corrida                                                                                                            #
# --------------------------------------------------------------------------------------------------------------------- #
def correr(rutas: dict, salida: Path, material: Path, clave: Path, esperado: dict | None = None, importar=None,
           codigo: Path = CODIGO_ANALISIS, enmienda: Path = ENMIENDA, raiz_indice: Path = REPO_DIR) -> dict:
    salida, material, clave = Path(salida), Path(material), Path(clave)
    for x in (salida, material, clave):
        if x.exists():
            frena("--salida, --material o --clave ya existe")
    A, X = cargar_codigo_analisis(codigo)
    esperado = esperado or esperado_de(A)
    for nombre, mod in (("atribucion_fallas_nav", NAV), ("adaptador_banco_nav", ABN)):
        if sha_archivo(Path(mod.__file__)) != SHA[nombre]:
            frena(f"{nombre}.py no es el de HEAD")
    if sha_archivo(enmienda) != SHA["enmienda"]:
        frena("la enmienda no es la firmada")

    pob = poblacion(A, rutas, esperado, importar)
    P, qids, banco = pob["P"], pob["qids"], pob["banco"]
    armado = json.loads(A.controlado(rutas["armado_e0"], esperado["armado_e0"], "el armado de la E0"))
    unidades = X.unidades_de_las_anclas(qids, P, rutas["e0"], armado)
    base = NAV.AnclaIndexBanco.desde_indice(rutas["indice"], esperado["manifiesto_indice"], raiz_indice)
    if base.fuente["kg_sha256"] != esperado["kg"]:
        frena("el índice por punto no es el del grafo evaluado")
    lectura = NAV.cargar_lectura(rutas["indice"], esperado["manifiesto_indice"], raiz_indice)
    mapa = {}
    for q in qids:
        for a, us in zip(P[q]["anclas"], unidades[q]):
            if mapa.setdefault(a["unidad"], us) != us:
                frena("un ancla con dos lecturas distintas")
    ai = AnclasConRangos(base, mapa)

    formas = {f: {"n": 0, "resuelven_tal_cual": 0, "resuelven_con_los_rangos": 0} for f in FORMAS}
    for q in qids:
        for a in P[q]["anclas"]:
            to, punto = NAV.parse_ancla(a["unidad"])
            f = formas[forma_de(a["unidad"])]
            f["n"] += 1
            f["resuelven_tal_cual"] += bool(base.resolver(to, punto))
            f["resuelven_con_los_rangos"] += bool(ai.resolver(to, punto))

    kg = [c for c in pob["corridas"] if c["brazo"] == A.BRAZO_GRAFO]
    con_veredicto = sorted((c for c in kg if c["estado"] in ("correcta", "no_correcta")), key=lambda c: c["id_opaco"])
    filas, ats, payloads, de_id = [], {}, {}, {}
    for c in con_veredicto:
        v = pob["veredictos"][c["id_opaco"]]["veredicto_pregunta"]
        anclas = [a["unidad"] for a in P[c["qid"]]["anclas"]]
        p, at = atribuir_sesion(c, banco.sesion(c), banco.leer, anclas, ai, lectura, v)
        ats[c["id_opaco"]], payloads[c["id_opaco"]], de_id[c["id_opaco"]] = at, p, c
        filas.append(registro(c, v, P[c["qid"]]["tipo"], p, at))
    if not NAV.corrida_valida(list(ats.values())):
        frena("un control del log de las v1 falló: la corrida es inválida (§3 de la regla)")

    clases = Counter(x["clase"] or "correcto" for x in filas)
    por_tipo: dict = {}
    for x in filas:
        por_tipo.setdefault(x["tipo"], Counter())[x["clase"] or "correcto"] += 1
    por_veredicto: dict = {}
    for x in filas:
        por_veredicto.setdefault(x["veredicto"], Counter())[x["clase"] or "correcto"] += 1
    ultima = sorted(i for i, at in ats.items() if at["clase"] == ULTIMA_CLASE)
    elegidos = sortear(ultima)
    codigo_sha = {"atribucion_b63.py": sha_archivo(Path(__file__)), "atribucion_fallas_nav.py": SHA["atribucion_fallas_nav"],
                  "adaptador_banco_nav.py": SHA["adaptador_banco_nav"], "atribucion_fallas.py": sha_archivo(Path(AF.__file__)),
                  "analizar_b63.py": SHA["analizar_b63"], "exactitud_de_cita_9_4_b63.py": SHA["exactitud_de_cita_9_4_b63"]}
    out = {"que": "la atribución determinística de fallas sobre las sesiones del brazo del grafo de B6.3",
           "regla": {"enmienda": "data/experiment/ev2_reporte/enmienda1_regla_atribucion_navegacion.md",
                     "sha256": SHA["enmienda"], "firmada_en": "df3b6d39", "declarado": DECLARADO_DE_LA_ENMIENDA},
           "decisiones": DECISIONES, "implementacion": IMPLEMENTACION, "codigo": codigo_sha,
           "grafo": base.fuente | {"n_anclas": len(base.por_ancla), "n_contenedores": len(base.contenedores)},
           "poblacion": {"brazo": A.BRAZO_GRAFO, "corridas": len(kg), "con_veredicto": len(filas),
                         "por_veredicto": dict(sorted(Counter(x["veredicto"] for x in filas).items())),
                         "atribuibles": sum(1 for x in filas if x["veredicto"] in AF.VEREDICTOS_ATRIBUIBLES),
                         "sin_veredicto": declarar_sin_veredicto(A, banco, kg)},
           "cuentas": {"por_clase": {k: clases.get(k, 0) for k in AF.CLASES + ["correcto"]},
                       "por_tipo_y_clase": {t: {k: c.get(k, 0) for k in AF.CLASES + ["correcto"]} for t, c in sorted(por_tipo.items())},
                       "por_veredicto_y_clase": {v: {k: c.get(k, 0) for k in AF.CLASES + ["correcto"]}
                                                 for v, c in sorted(por_veredicto.items())}},
           "anclas_por_forma": formas,
           "pedidos_sin_herramienta": {"en_las_sesiones_con_veredicto": sum(x["pedidos_sin_herramienta"] for x in filas),
                                       "sesiones_con_alguno": sum(1 for x in filas if x["pedidos_sin_herramienta"])},
           "corrida_valida": True,
           "ultima_clase": {"clase": ULTIMA_CLASE, "n": len(ultima), "semilla": SEMILLA,
                            "regla": "sorteo de 10" if len(ultima) > N_CASOS else "todas", "n_fichas": len(elegidos)},
           "por_sesion": filas,
           "entradas": {k: (sha_archivo(v) if Path(v).is_file() else Path(v).name) for k, v in sorted(rutas.items()) if k != "clon"},
           "archivos_de_banco_b63_controlados": len(banco.leidos)}

    # el material de la autora y la clave: después de todos los controles
    salida.mkdir(parents=True)
    material.mkdir(parents=True)
    casos = []
    for k, i in enumerate(elegidos, 1):
        c = de_id[i]
        nombre = f"F{k:02d}"
        q = P[c["qid"]]
        us = unidades[c["qid"]]
        (material / f"{nombre}.md").write_text(ficha(nombre, q, pob["veredictos"][i]["veredicto_pregunta"], pob["modales"][i],
                                                     payloads[i], ats[i], us), encoding="utf-8")
        casos.append({"ficha": nombre, "id_opaco": i, "sesion": c["sesion"], "pregunta": c["qid"], "repeticion": c["r"]})
    renglones = [[x["ficha"]] for x in casos]
    est = {"columnas": COLUMNAS_PLANILLA, "renglones": renglones, "valores_admitidos": list(VALORES_PLANILLA),
           "como_se_sella": "python3 -I -B atribucion_b63.py sellar --planilla <planilla> --estructura <esta> --sello <sello>"}
    (material / "estructura_planilla_atribucion_b63.json").write_text(json.dumps(est, ensure_ascii=False, indent=1) + "\n",
                                                                      encoding="utf-8")
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(COLUMNAS_PLANILLA)
    for x in casos:
        w.writerow([x["ficha"], "", ""])
    (material / "planilla_atribucion_b63.csv").write_text(buf.getvalue(), encoding="utf-8")
    clave.parent.mkdir(parents=True, exist_ok=True)
    clave.write_text(json.dumps({"que": "la clave de las fichas de la atribución de B6.3 (solo en el paquete)", "semilla": SEMILLA,
                                 "casos": casos,
                                 "sha256_fichas": {f"{x['ficha']}.md": sha_archivo(material / f"{x['ficha']}.md") for x in casos}},
                                ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    out["material"] = {"fichas": len(casos), "planilla_sha256": sha_archivo(material / "planilla_atribucion_b63.csv"),
                       "estructura_sha256": sha_archivo(material / "estructura_planilla_atribucion_b63.json")}
    (salida / "atribucion_B63.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, sort_keys=True) + "\n",
                                                encoding="utf-8")
    return out


def main(argv: list | None = None) -> int:
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("correr")
    for a in ARGS:
        c.add_argument("--" + a.replace("_", "-"), type=Path, required=True)
    c.add_argument("--codigo-analisis", type=Path, default=CODIGO_ANALISIS)
    c.add_argument("--enmienda", type=Path, default=ENMIENDA)
    c.add_argument("--raiz-indice", type=Path, default=REPO_DIR,
                   help="la raíz contra la que valen el kg_path y el e0_dir del manifiesto del índice por punto")
    for a in ("--salida", "--material", "--clave"):
        c.add_argument(a, type=Path, required=True)
    s = sub.add_parser("sellar")
    for a in ("--planilla", "--estructura", "--sello"):
        s.add_argument(a, type=Path, required=True)
    a = ap.parse_args(argv)
    try:
        if a.cmd == "sellar":
            h, hora = sellar(a.planilla, a.estructura, a.sello)
            print(f"sellada: {a.planilla.name} ({h}) a las {hora}")
            return 0
        correr({k: getattr(a, k) for k in ARGS}, a.salida, a.material, a.clave, codigo=a.codigo_analisis,
               enmienda=a.enmienda, raiz_indice=a.raiz_indice)
    except Exception as ex:  # noqa: BLE001  (sin el mensaje de un error inesperado: puede traer un id o un texto)
        if type(ex).__name__ == "Freno":
            print(f"FRENO: {ex}")
            return 10
        renglon = next((f.lineno for f in reversed(traceback.extract_tb(ex.__traceback__)) if f.filename == __file__), None)
        print(f"ERROR: {type(ex).__name__} en atribucion_b63.py:{renglon}")
        return 12
    print(f"salida: {a.salida.name}/atribucion_B63.json ({sha_archivo(a.salida / 'atribucion_B63.json')})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
