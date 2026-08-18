"""
selftest_tools_v2.py — Tests de respuesta conocida de las tools v2 (U-A1.2).
Determinístico, sin API, USD 0. Exit 0 = todos los tests que RIGEN pasan.

Regla del mandato: TODO valor esperado se DERIVA del kg.json correspondiente
dentro de este mismo script (vista runtime del loader, `grafos.cargar_vista_runtime`,
= la vista que ve el harness), NUNCA se hardcodea. Si lo derivado difiere de lo
que el backlog o los docs citan, mandan los archivos y se reporta.

Material EV2 (preguntas, criterios, pares, trazas de ev2_corrida): NO se abre.
La verdad-terreno de buscar_nodos_v2 es la designada FUERA de EV2: CQ-031 y
CQN2-015 (docs/decision_backend_grafo.md §5; consultas verbatim de
docs/evidencia_vara_v3/verificaciones_vara_v3.md §2c y
docs/evidencia_gate_cqn2/{cqn2_015.md,barrido_kg_gate_cqn2.md}), BKL-0003 y
BKL-0022 (data/backlog/backlog.jsonl). Esa parte es REGISTRO INFORMATIVO
(posiciones), sin conclusiones — la medición real es A1.4.

Secciones (por grafo donde aplica):
  0. Integridad: sha del kg.json (grafos.verificar_sha) y KG_Meta.kg_sha256 en Neo4j.
  A. BKL-0027 — asimetría direccional: v1 'salientes' reproduce el 0; v2 en UNA
     llamada devuelve ambas direcciones con totales == derivados; unión de páginas
     de entrantes == multiconjunto exacto; filtro miembro_de == derivado.
  B. BKL-0022 — huérfano léxico: posición derivada en los entrantes del hub;
     alcanzable por paginación con ventanas 40/10/5/1 (página y posición derivadas);
     posición registrada para la nota del backlog.
  C. Paginación — hubs máximos (entrante y saliente) + nodos de A/B: unión de
     páginas == lista exacta de vecinos (orden, sin pérdida ni duplicado) para
     ventanas 40 y 7; página fuera de rango vacía; parámetros inválidos → defaults.
  D. Filtro por relación — filtrado == subconjunto exacto del sin-filtro, por
     relación; suma de por_relacion == total; relación inexistente → 0.
  E. buscar_nodos_v2 (informativo) — CQ-031, CQN2-015, BKL-0003, BKL-0022:
     portadores localizados por contenido en cada grafo; posición v1 (réplica del
     scoring del harness) y v2 (top-10 de la tool, rank global por réplica del ORDER BY).
  F. ver_nodo_v2 == GraphIndex.ver_nodo byte a byte (adaptador declarado sin cambio).
  G. Provenances: GraphAgent._collect_provs (harness, sin editar) recoge TODAS las
     provenances de los outputs v2 (layout de listas en primer nivel).
  H. GraphAgentV2 — ask() textualmente igual al harness salvo las 2 sustituciones;
     despacho _run_tool == ToolsV2 byte a byte; prompt default == SYSTEM_PROMPT del
     harness; specs = specs_tools_v2.json.

Salida: selftest_tools_v2_resultados.json (sin timestamps → doble corrida
byte-idéntica) + resumen en stdout.
"""

from __future__ import annotations

import argparse
import difflib
import hashlib
import json
import sys
from pathlib import Path

AGENTE_V2_DIR = Path(__file__).resolve().parent
NEO4J_DIR = AGENTE_V2_DIR.parent / "neo4j"
for _p in (str(NEO4J_DIR), str(AGENTE_V2_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from grafos import GRAFOS, CLAVES, cargar_vista_runtime, verificar_sha, rel_repo  # noqa: E402
from conexion import abrir_driver  # noqa: E402
from harness import GraphIndex, GraphAgent, SYSTEM_PROMPT, TOOLS, _tokens, _strip_accents  # noqa: E402
from tools_v2 import ToolsV2, TOOLS_V2, POR_PAGINA_DEFAULT, POR_PAGINA_MAX  # noqa: E402
from agente_v2 import GraphAgentV2, verificar_ask_copiado, PROMPTS, SYSTEM_PROMPT_V2_PROPUESTO  # noqa: E402

SALIDA_DEFAULT = AGENTE_V2_DIR / "selftest_tools_v2_resultados.json"

# Identificadores del backlog (los VALORES esperados se derivan del kg.json).
NODO_BKL0027 = "Sujeto_rol_sujeto_obligado_proteccion"
REL_BKL0027 = "miembro_de"
NODO_BKL0022 = "Sujeto_propuesto_entidades_financieras_del_grupo_2"
HUB_BKL0022 = "Sujeto_entidad_financiera"
NODO_BKL0003 = ("Excepcion_otros_proveedores_no_financieros_de_credito_"
                "alcanzados_por_las_normas_sobre_prov_5f95b9")

# Verdad-terreno FUERA de EV2 para buscar_nodos_v2 (informativo).
# Portadores localizados POR CONTENIDO (substring normalizado en label+properties):
# los ids de run_3 citados en los docs no existen en KG-Refinado / KG-Reextraído
# (pipeline v2 re-hashea ids), así que se localiza el equivalente en cada grafo.
CASOS_BUSQUEDA = {
    "CQ-031": {
        "fuente": "docs/evidencia_vara_v3/verificaciones_vara_v3.md §2c (10 consultas verbatim de la traza) + pregunta (docs/evidencia_capa_d/reporte_d1.md)",
        "portador_run3": "Restriccion_los_deudores_cuyas_financiaciones_se_encuentren_cubiertas_totalmente_con_garanti",
        "huella_contenido": ["cubiertas totalmente con garantias preferidas"],
        "consultas": [
            "deudores no deben ser objeto clasificación",
            "capacidad de repago evaluación deudores",
            "deudores exclusión clasificación estado nacional provincia municipio",
            "garantías preferidas A financiaciones",
            "punto 4.5 deudores no deben clasificación estado nacional",
            "punto 4.4 garantías preferidas A estado nacional provincia",
            "estado nacional provincia municipio banco central deudores",
            "cesión sin responsabilidad cedente deudores",
            "garantías preferidas A definición estado nacional provincia",
            "garantías preferidas A créditos estado nacional provincia municipio",
            "¿Qué deudores no deben ser objeto de clasificación y respecto de qué deudores no corresponde evaluar la capacidad de repago?",
        ],
    },
    "CQN2-015": {
        "fuente": "docs/evidencia_gate_cqn2/barrido_kg_gate_cqn2.md (K-I, pasos 1,2,3,7,9) + cqn2_015.md (pasos 4,5,13)",
        "portador_run3": "Restriccion_prohibicion_de_ponderador_menor_para_deudores_no_calificados",
        "huella_contenido": ["pais de constitucion"],
        "consultas": [
            "capital mínimo riesgo crédito ponderador deudor no calificado",
            "piso ponderador riesgo exposición deudor",
            "deudor no calificado ponderador piso",
            "no calificado ponderador",
            "ponderador riesgo exposición deudor sin calificación",
            "exposición deudor no calificado 100%",
            "ponderador riesgo 100 deudor calificado",
            "deudor sin calificación 100",
        ],
    },
    "BKL-0003": {
        "fuente": "data/backlog/backlog.jsonl BKL-0003 (asociación mutual); variantes de neo4j/indices.py",
        "portador_id": NODO_BKL0003,
        "huella_contenido": ["asociaciones mutuales"],
        "consultas": [
            "asociación mutual",
            "asociacion mutual",
            "asociaciones mutuales",
            "mutual cooperativa crédito",
            "excepto que se trate de asociaciones mutuales",
            "otros proveedores no financieros de crédito",
        ],
    },
    "BKL-0022": {
        "fuente": "data/backlog/backlog.jsonl BKL-0022 (huérfano léxico: tokens del label + label completo)",
        "portador_id": NODO_BKL0022,
        "huella_contenido": [],
        "consultas": [],   # se completan con los tokens del label (derivados) + label completo + 'grupo 2'
    },
}


# --------------------------------------------------------------------------- #
# utilidades
# --------------------------------------------------------------------------- #
def ser(x) -> str:
    """Serialización con la que el harness entrega cada output al modelo (línea 512)."""
    return json.dumps(x, ensure_ascii=False)


def sha_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def norm(s: str) -> str:
    return " ".join(_tokens(s or ""))


def clave_item(it: dict) -> tuple:
    return (it["relation"], it["vecino_id"], ser(it["provenances"]))


class Registro:
    def __init__(self):
        self.tests = []          # {seccion, grafo, nombre, rige, ok, esperado, observado}
        self.info = {}

    def test(self, seccion, grafo, nombre, ok, esperado=None, observado=None, rige=True, nota=None):
        self.tests.append({"seccion": seccion, "grafo": grafo, "nombre": nombre, "rige": rige,
                           "ok": bool(ok), "esperado": esperado, "observado": observado,
                           **({"nota": nota} if nota else {})})
        marca = "✓" if ok else ("✗" if rige else "~")
        print(f"  {marca} [{seccion}] {nombre}" + ("" if ok else f"  esperado={esperado!r} observado={observado!r}"))
        return ok

    def resumen(self) -> dict:
        rigen = [t for t in self.tests if t["rige"]]
        fallas = [t for t in rigen if not t["ok"]]
        return {"tests_total": len(self.tests), "rigen": len(rigen), "pasan": len(rigen) - len(fallas),
                "fallan": len(fallas), "informativos": len(self.tests) - len(rigen)}


# --------------------------------------------------------------------------- #
# derivación desde el kg.json (vista runtime del loader)
# --------------------------------------------------------------------------- #
class Derivado:
    """Todo lo esperado, calculado desde el KnowledgeGraph del loader."""

    def __init__(self, kg):
        self.kg = kg
        self.by_id = {n.id: n for n in kg.nodes}
        self.out, self.inn = {}, {}
        for e in kg.edges:                       # orden = posición en kg.edges (= r.orden)
            self.out.setdefault(e.source, []).append(e)
            self.inn.setdefault(e.target, []).append(e)

    def items(self, nid: str, direccion: str, relacion=None) -> list:
        """Lista de ítems en el formato de la tool (mismo que v1), en orden de kg.edges."""
        res = []
        edges = self.out.get(nid, []) if direccion == "salientes" else self.inn.get(nid, [])
        for e in edges:
            if relacion is not None and e.relation != relacion:
                continue
            otro = e.target if direccion == "salientes" else e.source
            v = self.by_id.get(otro)
            res.append({"relation": e.relation, "vecino_id": otro,
                        "vecino_label": v.label if v else None, "provenances": e.provenances})
        return res

    def por_relacion(self, nid: str, direccion: str) -> dict:
        c = {}
        for it in self.items(nid, direccion):
            c[it["relation"]] = c.get(it["relation"], 0) + 1
        return {k: v for k, v in sorted(c.items(), key=lambda t: (-t[1], t[0]))}

    def grado(self, nid: str) -> tuple:
        return len(self.out.get(nid, [])), len(self.inn.get(nid, []))

    def hub_max(self, direccion: str) -> str:
        d = self.inn if direccion == "entrantes" else self.out
        return max(self.by_id, key=lambda i: (len(d.get(i, [])), i))   # desempate por id, determinístico

    def nodos_sobre(self, ventana: int) -> dict:
        o = sum(1 for i in self.by_id if len(self.out.get(i, [])) > ventana)
        e = sum(1 for i in self.by_id if len(self.inn.get(i, [])) > ventana)
        a = sum(1 for i in self.by_id if len(self.out.get(i, [])) > ventana or len(self.inn.get(i, [])) > ventana)
        return {"salientes": o, "entrantes": e, "alguna": a}

    def localizar_por_contenido(self, huellas: list) -> list:
        """ids cuyo label+properties (normalizados) contienen TODAS las huellas."""
        res = []
        for n in self.kg.nodes:
            texto = norm(n.label) + " " + norm(json.dumps(n.properties, ensure_ascii=False))
            if all(norm(h) in texto for h in huellas):
                res.append(n.id)
        return sorted(res)

    def rank_v1(self, gi: GraphIndex, consulta: str, nid: str) -> dict:
        """Réplica del scoring de GraphIndex.buscar_nodos (rank global 1-based) —
        misma réplica que docs/evidencia_vara_v3/verificaciones_vara_v3.md §2c."""
        q = set(_tokens(consulta))
        scored = [(len(q & gi._node_tokens[n.id]), len(n.label or ""), n.id)
                  for n in self.kg.nodes if len(q & gi._node_tokens[n.id]) > 0]
        scored.sort(key=lambda t: (-t[0], t[1], t[2]))
        ids = [t[2] for t in scored]
        r = (ids.index(nid) + 1) if nid in ids else None
        return {"rank_global": r, "total_con_match": len(scored),
                "score": next((t[0] for t in scored if t[2] == nid), 0)}


def rank_v2_global(driver, tools: ToolsV2, consulta: str, nid: str) -> dict:
    """Rank global BM25 (réplica del ORDER BY de Neo4jIndex._buscar_fulltext, sin
    slice) — diagnóstico del selftest, no una tool."""
    toks = _tokens(consulta)
    if not toks:
        return {"rank_global": None, "total_con_match": 0}
    with driver.session() as s:
        ids = [r["id"] for r in s.run(
            f"CALL db.index.fulltext.queryNodes('{tools.index.indice}', $q) YIELD node, score "
            "WITH node, score ORDER BY score DESC, size(node.label) ASC, node.id ASC "
            "RETURN node.id AS id", q=" ".join(toks))]
    return {"rank_global": (ids.index(nid) + 1) if nid in ids else None, "total_con_match": len(ids)}


def paginar_todo(tools: ToolsV2, nid: str, por_pagina: int, relacion=None) -> dict:
    """Recorre todas las páginas; devuelve listas concatenadas por dirección + metadatos."""
    out, inn, metas = [], [], []
    pagina = 1
    while True:
        r = tools.ver_vecinos_v2(nid, relacion=relacion, pagina=pagina, por_pagina=por_pagina)
        if "error" in r:
            return {"error": r}
        out.extend(r["salientes"]); inn.extend(r["entrantes"])
        metas.append({k: r[k] for k in ("pagina", "salientes_total", "salientes_paginas",
                                        "salientes_pagina_siguiente", "entrantes_total",
                                        "entrantes_paginas", "entrantes_pagina_siguiente")})
        sig = [x for x in (r["salientes_pagina_siguiente"], r["entrantes_pagina_siguiente"]) if x]
        if not sig:
            break
        pagina = min(sig)
        if pagina > 10_000:   # guarda
            break
    return {"salientes": out, "entrantes": inn, "paginas_recorridas": len(metas), "metas": metas,
            "primera": metas[0]}


def kg_meta_sha(driver, clave: str):
    with driver.session() as s:
        rec = s.run("MATCH (m:KG_Meta {grafo: $g}) RETURN m.kg_sha256 AS sha, m.n_nodos AS n, m.n_aristas AS a",
                    g=clave).single()
    return (rec["sha"], rec["n"], rec["a"]) if rec else None


class ClienteDummy:
    class messages:  # noqa: N801
        @staticmethod
        def create(**kw):
            raise RuntimeError("sin API en A1.2")


# --------------------------------------------------------------------------- #
# secciones
# --------------------------------------------------------------------------- #
def seccion_0(reg, driver, clave):
    g = GRAFOS[clave]
    sha = verificar_sha(clave)
    reg.test("0.integridad", clave, "sha256 kg.json == sellado", sha == g["sha256"], g["sha256"], sha)
    meta = kg_meta_sha(driver, clave)
    reg.test("0.integridad", clave, "KG_Meta.kg_sha256 en Neo4j == sellado",
             meta is not None and meta[0] == g["sha256"], g["sha256"], meta)
    reg.test("0.integridad", clave, "KG_Meta conteos == sellados",
             meta is not None and (meta[1], meta[2]) == (g["n_nodos"], g["n_aristas"]),
             (g["n_nodos"], g["n_aristas"]), meta[1:] if meta else None)


def seccion_A(reg, tools, der, gi, clave) -> dict:
    """BKL-0027."""
    print(f"\n== {clave} / A. BKL-0027 (asimetría direccional) ==")
    if NODO_BKL0027 not in der.by_id:
        reg.test("A.BKL-0027", clave, "nodo existe", False, rige=False, nota="N/A en este grafo")
        return {"aplica": False}
    n_out, n_in = der.grado(NODO_BKL0027)
    esp_out = der.items(NODO_BKL0027, "salientes")
    esp_in = der.items(NODO_BKL0027, "entrantes")
    esp_rel_in = der.por_relacion(NODO_BKL0027, "entrantes")
    esp_rel_out = der.por_relacion(NODO_BKL0027, "salientes")
    esp_miembro = der.items(NODO_BKL0027, "entrantes", REL_BKL0027)
    # v1: reproduce la llamada que falló (dirección 'salientes')
    v1 = gi.ver_vecinos(NODO_BKL0027, direccion="salientes")
    reg.test("A.BKL-0027", clave, "v1 ver_vecinos(rol,'salientes') devuelve len(salientes) == derivado (la llamada que dio 0 en RT-C6-3)",
             len(v1["salientes"]) == n_out, n_out, len(v1["salientes"]))
    reg.test("A.BKL-0027", clave, "v1 no incluye 'entrantes' en esa llamada (el output solo declaraba n_entrantes_total)",
             "entrantes" not in v1 and v1["n_entrantes_total"] == n_in, {"entrantes_key": False, "n_entrantes_total": n_in},
             {"entrantes_key": "entrantes" in v1, "n_entrantes_total": v1["n_entrantes_total"]})
    # v2: UNA llamada, sin dirección
    v2 = tools.ver_vecinos_v2(NODO_BKL0027)
    reg.test("A.BKL-0027", clave, "v2 UNA llamada: salientes_total == derivado", v2["salientes_total"] == n_out, n_out, v2["salientes_total"])
    reg.test("A.BKL-0027", clave, "v2 UNA llamada: entrantes_total == derivado", v2["entrantes_total"] == n_in, n_in, v2["entrantes_total"])
    reg.test("A.BKL-0027", clave, "v2 ambas listas presentes y rotuladas en la misma respuesta",
             isinstance(v2.get("salientes"), list) and isinstance(v2.get("entrantes"), list), True,
             (type(v2.get("salientes")).__name__, type(v2.get("entrantes")).__name__))
    reg.test("A.BKL-0027", clave, "v2 entrantes_por_relacion == derivado", v2["entrantes_por_relacion"] == esp_rel_in, esp_rel_in, v2["entrantes_por_relacion"])
    reg.test("A.BKL-0027", clave, "v2 salientes_por_relacion == derivado", v2["salientes_por_relacion"] == esp_rel_out, esp_rel_out, v2["salientes_por_relacion"])
    reg.test("A.BKL-0027", clave, "v2 primera página de entrantes == derivado[:40] byte a byte",
             ser(v2["entrantes"]) == ser(esp_in[:POR_PAGINA_DEFAULT]), f"{min(n_in, 40)} ítems", f"{len(v2['entrantes'])} ítems")
    todo = paginar_todo(tools, NODO_BKL0027, POR_PAGINA_DEFAULT)
    reg.test("A.BKL-0027", clave, "v2 unión de páginas (entrantes) == multiconjunto exacto derivado, mismo orden",
             ser(todo["entrantes"]) == ser(esp_in) and ser(todo["salientes"]) == ser(esp_out),
             {"entrantes": n_in, "salientes": n_out, "paginas": (n_in + 39) // 40 if n_in else 0},
             {"entrantes": len(todo["entrantes"]), "salientes": len(todo["salientes"]), "paginas": todo["paginas_recorridas"]})
    # filtro miembro_de (en KG-Reextraído la relación no existe → derivado 0)
    f = tools.ver_vecinos_v2(NODO_BKL0027, relacion=REL_BKL0027)
    reg.test("A.BKL-0027", clave, f"v2 filtro relacion={REL_BKL0027!r}: entrantes == derivado ({len(esp_miembro)}) byte a byte",
             ser(f["entrantes"]) == ser(esp_miembro) and f["entrantes_total"] == len(esp_miembro),
             len(esp_miembro), f["entrantes_total"])
    pos_miembro_v1 = [i + 1 for i, it in enumerate(esp_in[:40]) if it["relation"] == REL_BKL0027]
    return {"aplica": True, "n_salientes": n_out, "n_entrantes": n_in,
            "entrantes_por_relacion": esp_rel_in, "salientes_por_relacion": esp_rel_out,
            "n_miembro_de_entrantes": len(esp_miembro),
            "posiciones_miembro_de_en_ventana40_v1": pos_miembro_v1,
            "v1_salientes_len": len(v1["salientes"]), "v2_paginas_entrantes": todo["paginas_recorridas"],
            "backlog_cita": "7 aristas miembro_de ENTRANTES; 168 vecinos entrantes (BKL-0027, sobre KG-Refinado)"}


def seccion_B(reg, tools, der, gi, clave) -> dict:
    """BKL-0022."""
    print(f"\n== {clave} / B. BKL-0022 (huérfano léxico bajo ventana 40) ==")
    if NODO_BKL0022 not in der.by_id or HUB_BKL0022 not in der.by_id:
        reg.test("B.BKL-0022", clave, "nodo y hub existen", False, rige=False, nota="N/A en este grafo")
        return {"aplica": False}
    esp_in = der.items(HUB_BKL0022, "entrantes")
    n_in = len(esp_in)
    pos = [i + 1 for i, it in enumerate(esp_in) if it["vecino_id"] == NODO_BKL0022]
    reg.test("B.BKL-0022", clave, "el huérfano aparece exactamente una vez entre los entrantes del hub", len(pos) == 1, 1, len(pos))
    if len(pos) != 1:
        return {"aplica": True, "posiciones": pos}
    pos = pos[0]
    rel = next(it["relation"] for it in esp_in if it["vecino_id"] == NODO_BKL0022)
    # v1: visible solo si pos <= 40
    v1 = gi.ver_vecinos(HUB_BKL0022, direccion="entrantes")
    pos_v1 = [i + 1 for i, it in enumerate(v1["entrantes"]) if it["vecino_id"] == NODO_BKL0022]
    reg.test("B.BKL-0022", clave, "v1 ver_vecinos(hub,'entrantes'): posición en la ventana de 40 == derivada (visible sii pos<=40)",
             pos_v1 == ([pos] if pos <= 40 else []), [pos] if pos <= 40 else [], pos_v1)
    # v2: alcanzable por paginación con cualquier ventana
    ventanas = {}
    for w in (POR_PAGINA_DEFAULT, 10, 5, 1):
        pag_esp = (pos - 1) // w + 1
        pos_esp = (pos - 1) % w + 1
        r = tools.ver_vecinos_v2(HUB_BKL0022, pagina=pag_esp, por_pagina=w)
        pos_obs = [i + 1 for i, it in enumerate(r["entrantes"]) if it["vecino_id"] == NODO_BKL0022]
        ok = pos_obs == [pos_esp] and r["entrantes_paginas"] == (n_in + w - 1) // w
        reg.test("B.BKL-0022", clave, f"v2 por_pagina={w}: huérfano en página {pag_esp} posición {pos_esp} (derivado de pos global {pos}/{n_in})",
                 ok, {"pagina": pag_esp, "posicion": pos_esp, "paginas": (n_in + w - 1) // w},
                 {"pagina": pag_esp, "posicion": pos_obs, "paginas": r["entrantes_paginas"]})
        ventanas[w] = {"pagina": pag_esp, "posicion": pos_esp, "paginas": (n_in + w - 1) // w}
    # filtro por su relación
    esp_f = der.items(HUB_BKL0022, "entrantes", rel)
    pos_f = [i + 1 for i, it in enumerate(esp_f) if it["vecino_id"] == NODO_BKL0022][0]
    r = tools.ver_vecinos_v2(HUB_BKL0022, relacion=rel)
    pos_f_obs = [i + 1 for i, it in enumerate(r["entrantes"]) if it["vecino_id"] == NODO_BKL0022]
    reg.test("B.BKL-0022", clave, f"v2 filtro relacion={rel!r}: huérfano en posición {pos_f} de {len(esp_f)} (derivado)",
             pos_f_obs == [pos_f] and r["entrantes_total"] == len(esp_f), {"pos": pos_f, "total": len(esp_f)},
             {"pos": pos_f_obs, "total": r["entrantes_total"]})
    # sentido inverso: desde el huérfano, su arista al hub
    esp_out_h = der.items(NODO_BKL0022, "salientes")
    r2 = tools.ver_vecinos_v2(NODO_BKL0022)
    reg.test("B.BKL-0022", clave, "v2 desde el huérfano: salientes == derivado byte a byte",
             ser(r2["salientes"]) == ser(esp_out_h) and ser(r2["entrantes"]) == ser(der.items(NODO_BKL0022, "entrantes")),
             {"salientes": len(esp_out_h)}, {"salientes": len(r2["salientes"])})
    return {"aplica": True, "posicion_derivada": pos, "n_entrantes_hub": n_in, "relacion": rel,
            "posicion_con_filtro": pos_f, "total_con_filtro": len(esp_f), "ventanas": ventanas,
            "visible_v1_ventana40": pos <= 40,
            "backlog_cita": "nota 2026-08-02: pos 6 de la ventana de 40; A1.1 (9e131bf): pos 7"}


def seccion_C(reg, tools, der, clave, nodos_extra: list) -> dict:
    """Paginación."""
    print(f"\n== {clave} / C. paginación ==")
    hub_in = der.hub_max("entrantes")
    hub_out = der.hub_max("salientes")
    nodos = []
    for nid in [hub_in, hub_out] + nodos_extra:
        if nid in der.by_id and nid not in nodos:
            nodos.append(nid)
    # chars por ítem de arista (serialización del harness), sobre TODAS las aristas:
    # justificación medible del techo por_pagina=40 (README §C.4).
    tam = sorted(len(ser(it)) for nid in der.out for it in der.items(nid, "salientes"))
    info = {"hub_max_entrantes": (hub_in, der.grado(hub_in)), "hub_max_salientes": (hub_out, der.grado(hub_out)),
            "nodos_sobre_40": der.nodos_sobre(40),
            "chars_por_item_arista": {"n": len(tam), "mediana": tam[len(tam) // 2], "p95": tam[int(len(tam) * 0.95)],
                                      "max": tam[-1], "chars_40_items_mediana": 40 * tam[len(tam) // 2]},
            "recorridos": {}}
    for nid in nodos:
        n_out, n_in = der.grado(nid)
        esp_out, esp_in = der.items(nid, "salientes"), der.items(nid, "entrantes")
        for w in (POR_PAGINA_DEFAULT, 7):
            todo = paginar_todo(tools, nid, w)
            ok_out = ser(todo["salientes"]) == ser(esp_out)
            ok_in = ser(todo["entrantes"]) == ser(esp_in)
            # sin duplicados ni pérdida: multiconjuntos de claves
            claves_obs = sorted(clave_item(x) for x in todo["salientes"] + todo["entrantes"])
            claves_esp = sorted(clave_item(x) for x in esp_out + esp_in)
            pag_esp = max((n_out + w - 1) // w, (n_in + w - 1) // w, 1)
            reg.test("C.paginacion", clave, f"{nid[:48]}… w={w}: unión de páginas == vecinos exactos (orden), sin pérdida ni duplicado; páginas={pag_esp}",
                     ok_out and ok_in and claves_obs == claves_esp and todo["paginas_recorridas"] == pag_esp,
                     {"salientes": n_out, "entrantes": n_in, "paginas": pag_esp},
                     {"salientes": len(todo["salientes"]), "entrantes": len(todo["entrantes"]),
                      "paginas": todo["paginas_recorridas"], "orden_ok": (ok_out, ok_in)})
            m = todo["primera"]
            reg.test("C.paginacion", clave, f"{nid[:48]}… w={w}: metadatos página 1 (totales, paginas, siguiente) == derivados",
                     m["salientes_total"] == n_out and m["entrantes_total"] == n_in
                     and m["salientes_paginas"] == (n_out + w - 1) // w and m["entrantes_paginas"] == (n_in + w - 1) // w
                     and m["salientes_pagina_siguiente"] == (2 if n_out > w else None)
                     and m["entrantes_pagina_siguiente"] == (2 if n_in > w else None),
                     {"s_tot": n_out, "e_tot": n_in, "s_pag": (n_out + w - 1) // w, "e_pag": (n_in + w - 1) // w}, m)
            info["recorridos"][f"{nid}|w={w}"] = {"salientes": n_out, "entrantes": n_in, "paginas": todo["paginas_recorridas"]}
        # página fuera de rango
        w = POR_PAGINA_DEFAULT
        fuera = max((n_out + w - 1) // w, (n_in + w - 1) // w) + 1
        r = tools.ver_vecinos_v2(nid, pagina=fuera)
        reg.test("C.paginacion", clave, f"{nid[:48]}… página fuera de rango ({fuera}): listas vacías, siguiente null, totales intactos",
                 r["salientes"] == [] and r["entrantes"] == [] and r["salientes_pagina_siguiente"] is None
                 and r["entrantes_pagina_siguiente"] is None and r["salientes_total"] == n_out and r["entrantes_total"] == n_in,
                 True, {"s": len(r["salientes"]), "e": len(r["entrantes"])})
    # parámetros inválidos → defaults / clamps (sobre el hub entrante)
    base = tools.ver_vecinos_v2(hub_in)
    casos = {"pagina=0": dict(pagina=0), "pagina=-3": dict(pagina=-3), "pagina='x'": dict(pagina="x"),
             "pagina=None": dict(pagina=None), "por_pagina=0": dict(por_pagina=0), "por_pagina=999": dict(por_pagina=999),
             "por_pagina='abc'": dict(por_pagina="abc"), "por_pagina=None": dict(por_pagina=None),
             "relacion=''": dict(relacion="")}
    for nombre, kw in casos.items():
        r = tools.ver_vecinos_v2(hub_in, **kw)
        if nombre == "por_pagina=0":
            ok = r["por_pagina"] == 1 and len(r["entrantes"]) == min(1, der.grado(hub_in)[1])
        elif nombre == "por_pagina=999":
            ok = r["por_pagina"] == POR_PAGINA_MAX and ser(r) == ser(base)
        else:
            ok = ser(r) == ser(base)
        reg.test("C.paginacion", clave, f"parámetro inválido {nombre} → default/clamp", ok, "== default" if nombre != "por_pagina=0" else "por_pagina=1",
                 {"pagina": r["pagina"], "por_pagina": r["por_pagina"], "filtro": r["filtro_relacion"]})
    # id inexistente
    r = tools.ver_vecinos_v2("__no_existe__")
    reg.test("C.paginacion", clave, "id inexistente → mismo error que v1", "error" in r and "sugerencia" in r, True, r)
    return info


def seccion_D(reg, tools, der, clave, nodos: list) -> dict:
    """Filtro por relación."""
    print(f"\n== {clave} / D. filtro por relación ==")
    info = {}
    for nid in nodos:
        if nid not in der.by_id:
            continue
        rels = sorted(set(der.por_relacion(nid, "salientes")) | set(der.por_relacion(nid, "entrantes")))
        sin = paginar_todo(tools, nid, POR_PAGINA_DEFAULT)
        suma_out = suma_in = 0
        for rel in rels:
            con = paginar_todo(tools, nid, POR_PAGINA_DEFAULT, relacion=rel)
            sub_out = [x for x in sin["salientes"] if x["relation"] == rel]
            sub_in = [x for x in sin["entrantes"] if x["relation"] == rel]
            ok = (ser(con["salientes"]) == ser(sub_out) and ser(con["entrantes"]) == ser(sub_in)
                  and ser(sub_out) == ser(der.items(nid, "salientes", rel))
                  and ser(sub_in) == ser(der.items(nid, "entrantes", rel))
                  and con["primera"]["salientes_total"] == len(sub_out)
                  and con["primera"]["entrantes_total"] == len(sub_in))
            reg.test("D.filtro", clave, f"{nid[:40]}… relacion={rel!r}: filtrado == subconjunto exacto del sin-filtro (s={len(sub_out)}, e={len(sub_in)})",
                     ok, {"s": len(sub_out), "e": len(sub_in)},
                     {"s": len(con["salientes"]), "e": len(con["entrantes"]),
                      "tot": (con["primera"]["salientes_total"], con["primera"]["entrantes_total"])})
            suma_out += len(sub_out); suma_in += len(sub_in)
        reg.test("D.filtro", clave, f"{nid[:40]}… suma por relación == totales sin filtro",
                 (suma_out, suma_in) == der.grado(nid), der.grado(nid), (suma_out, suma_in))
        r = tools.ver_vecinos_v2(nid, relacion="__relacion_inexistente__")
        reg.test("D.filtro", clave, f"{nid[:40]}… relación inexistente → listas vacías, totales 0, por_relacion y n_*_total intactos",
                 r["salientes"] == [] and r["entrantes"] == [] and r["salientes_total"] == 0 and r["entrantes_total"] == 0
                 and (r["n_salientes_total"], r["n_entrantes_total"]) == der.grado(nid)
                 and r["entrantes_por_relacion"] == der.por_relacion(nid, "entrantes"),
                 True, {"s": r["salientes_total"], "e": r["entrantes_total"]})
        info[nid] = {"relaciones": rels, "grado": der.grado(nid)}
    return info


def seccion_E(reg, driver, tools, der, gi, clave) -> dict:
    """buscar_nodos_v2 — informativo (verdad-terreno fuera de EV2)."""
    print(f"\n== {clave} / E. buscar_nodos_v2 (INFORMATIVO, sin conclusiones) ==")
    out = {}
    for caso, spec in CASOS_BUSQUEDA.items():
        if "portador_id" in spec:
            portadores = [spec["portador_id"]] if spec["portador_id"] in der.by_id else []
            if not portadores and spec["huella_contenido"]:
                portadores = der.localizar_por_contenido(spec["huella_contenido"])
            metodo = "id" if spec["portador_id"] in der.by_id else "contenido"
        else:
            portadores = der.localizar_por_contenido(spec["huella_contenido"])
            metodo = "contenido"
        consultas = list(spec["consultas"])
        if caso == "BKL-0022" and portadores:
            lab = der.by_id[portadores[0]].label
            consultas = _tokens(lab) + [lab, "grupo 2"]
        res_caso = {"fuente": spec["fuente"], "portadores": portadores, "metodo_localizacion": metodo,
                    "portador_run3_existe": spec.get("portador_run3") in der.by_id if spec.get("portador_run3") else None,
                    "consultas": []}
        if not portadores:
            reg.test("E.busqueda", clave, f"{caso}: portador localizado en el grafo", False, rige=False,
                     nota="N/A: sin portador en este grafo (ni por id ni por contenido)")
            out[caso] = res_caso
            continue
        for p in portadores:
            n = der.by_id[p]
            res_caso.setdefault("portadores_detalle", {})[p] = {"type": n.type, "label": n.label, "grado": der.grado(p)}
        for c in consultas:
            v2 = tools.buscar_nodos_v2(c)                 # default limite=10
            v2_50 = tools.buscar_nodos_v2(c, limite=50)
            ids10 = [r["id"] for r in v2.get("resultados", [])]
            ids50 = [r["id"] for r in v2_50.get("resultados", [])]
            v1 = gi.buscar_nodos(c)
            ids10_v1 = [r["id"] for r in v1.get("resultados", [])]
            fila = {"consulta": c, "v1_total_con_match": v1.get("total_con_match", v1.get("total")),
                    "v2_total_con_match": v2.get("total_con_match", v2.get("total")), "por_portador": {}}
            for p in portadores:
                rv1 = der.rank_v1(gi, c, p)
                rv2 = rank_v2_global(driver, tools, c, p)
                fila["por_portador"][p] = {
                    "v1_pos_top10": (ids10_v1.index(p) + 1) if p in ids10_v1 else None,
                    "v1_rank_global": rv1["rank_global"], "v1_score": rv1["score"],
                    "v2_pos_top10": (ids10.index(p) + 1) if p in ids10 else None,
                    "v2_pos_top50": (ids50.index(p) + 1) if p in ids50 else None,
                    "v2_rank_global": rv2["rank_global"],
                }
                # consistencia interna del registro (rige): la posición en el top-10 de la tool
                # coincide con el rank global replicado cuando este es <=10.
                pos10 = fila["por_portador"][p]["v2_pos_top10"]
                rg = rv2["rank_global"]
                reg.test("E.busqueda", clave, f"{caso} {c[:38]!r}: top-10 de la tool consistente con rank global BM25 (rank={rg})",
                         (pos10 == rg) if (rg is not None and rg <= 10) else (pos10 is None), rg if (rg and rg <= 10) else None, pos10)
            res_caso["consultas"].append(fila)
            resumen = "; ".join(f"v1={fila['por_portador'][p]['v1_rank_global']} v2={fila['por_portador'][p]['v2_rank_global']}"
                                for p in portadores)
            print(f"    · {caso} {c[:60]!r}: {resumen}")
        # registro agregado (informativo, no rige)
        for p in portadores:
            en10 = sum(1 for f in res_caso["consultas"] if f["por_portador"][p]["v2_pos_top10"] is not None)
            en10_v1 = sum(1 for f in res_caso["consultas"] if f["por_portador"][p]["v1_pos_top10"] is not None)
            res_caso.setdefault("resumen", {})[p] = {"consultas": len(consultas), "en_top10_v1": en10_v1, "en_top10_v2": en10}
            reg.test("E.busqueda", clave, f"{caso} {p[:40]}…: en top-10 v1 {en10_v1}/{len(consultas)} vs v2 {en10}/{len(consultas)} (registro)",
                     True, rige=False)
        out[caso] = res_caso
    return out


def seccion_F(reg, tools, gi, der, clave, ids: list):
    print(f"\n== {clave} / F. ver_nodo_v2 == harness ==")
    for nid in ids + ["__no_existe__"]:
        a, b = gi.ver_nodo(nid), tools.ver_nodo_v2(nid)
        reg.test("F.ver_nodo", clave, f"ver_nodo_v2({nid[:40]}…) byte-idéntico a GraphIndex.ver_nodo", ser(a) == ser(b),
                 sha_texto(ser(a))[:12], sha_texto(ser(b))[:12])


def seccion_G(reg, tools, der, clave, ids: list):
    print(f"\n== {clave} / G. provenances recogidas por GraphAgent._collect_provs ==")
    for nid in ids:
        if nid not in der.by_id:
            continue
        r = tools.ver_vecinos_v2(nid)
        sink, ordenadas = set(), []
        GraphAgent._collect_provs(r, sink, ordenadas)
        esp = []
        vistos = set()
        for it in r["salientes"] + r["entrantes"]:
            for p in it["provenances"]:
                k = (p.get("source_doc"), p.get("location"))
                if k not in vistos:
                    vistos.add(k); esp.append({"source_doc": k[0], "location": k[1]})
        reg.test("G.provenances", clave, f"ver_vecinos_v2({nid[:40]}…): _collect_provs recoge exactamente las provenances de ambas listas ({len(esp)})",
                 ser(ordenadas) == ser(esp), len(esp), len(ordenadas))
        rn = tools.ver_nodo_v2(nid)
        sink2, ord2 = set(), []
        GraphAgent._collect_provs(rn, sink2, ord2)
        reg.test("G.provenances", clave, f"ver_nodo_v2({nid[:40]}…): _collect_provs recoge las provenances del nodo ({len(rn['provenances'])})",
                 len(ord2) == len({(p.get('source_doc'), p.get('location')) for p in rn["provenances"]}),
                 len(rn["provenances"]), len(ord2))


def seccion_H(reg, driver, tools, clave):
    print(f"\n== {clave} / H. GraphAgentV2 ==")
    v = verificar_ask_copiado()
    reg.test("H.agente", clave, "GraphAgentV2.ask == GraphAgent.ask salvo 2 sustituciones (system=, tools=)",
             v["identico_salvo_sustituciones"] and v["conteo_sustituciones"] == {"system=SYSTEM_PROMPT,": 1, "tools=TOOLS)": 1},
             {"identico": True, "conteos": {"system=SYSTEM_PROMPT,": 1, "tools=TOOLS)": 1}}, v)
    ag = GraphAgentV2(driver, grafo=clave, client=ClienteDummy())
    reg.test("H.agente", clave, "prompt default == SYSTEM_PROMPT del harness (verbatim)", ag.system_prompt == SYSTEM_PROMPT,
             sha_texto(SYSTEM_PROMPT)[:12], sha_texto(ag.system_prompt)[:12])
    reg.test("H.agente", clave, "tools del request == specs_tools_v2.json", ag.tools is TOOLS_V2 and ser(ag.tools) == ser(TOOLS_V2), True, ag.tools is TOOLS_V2)
    reg.test("H.agente", clave, "MODEL/MAX_TOOL_CALLS heredados del harness (por import)",
             ag.backend["model"] == "claude-haiku-4-5-20251001" and ag.backend["tools_version"] == "v2", True, ag.backend)
    llamadas = [("buscar_nodos", {"consulta": "asociación mutual"}),
                ("buscar_nodos", {"consulta": "entidades financieras", "limite": 3}),
                ("ver_nodo", {"id": HUB_BKL0022}),
                ("ver_vecinos", {"id": NODO_BKL0027}),
                ("ver_vecinos", {"id": HUB_BKL0022, "pagina": 2, "por_pagina": 10, "relacion": "aplica_a"}),
                ("ver_vecinos", {"id": HUB_BKL0022, "direccion": "salientes"}),   # arg v1 ignorado
                ("tool_x", {})]
    for name, args in llamadas:
        a = ag._run_tool(name, dict(args))
        if name == "buscar_nodos":
            b = tools.buscar_nodos_v2(args["consulta"], args.get("limite", 10))
        elif name == "ver_nodo":
            b = tools.ver_nodo_v2(args["id"])
        elif name == "ver_vecinos":
            b = tools.ver_vecinos_v2(args["id"], relacion=args.get("relacion"), pagina=args.get("pagina", 1),
                                     por_pagina=args.get("por_pagina", POR_PAGINA_DEFAULT))
        else:
            b = {"error": f"tool desconocida: {name}"}
        reg.test("H.agente", clave, f"_run_tool({name}, {json.dumps(args, ensure_ascii=False)}) == ToolsV2 byte a byte",
                 ser(a) == ser(b), sha_texto(ser(b))[:12], sha_texto(ser(a))[:12])
    # el prompt propuesto difiere del harness en exactamente las 2 frases (informativo)
    d = list(difflib.unified_diff(SYSTEM_PROMPT.splitlines(), SYSTEM_PROMPT_V2_PROPUESTO.splitlines(), lineterm="", n=0))
    cambios = [l for l in d if l.startswith(("+", "-")) and not l.startswith(("+++", "---"))]
    reg.test("H.agente", clave, f"prompt propuesto (INERTE, pendiente de laudo): {len(cambios)} líneas cambiadas vs harness", True, rige=False,
             nota="; ".join(cambios))
    # specs: nombres, parámetros
    nombres = [t["name"] for t in TOOLS_V2]
    params = {t["name"]: sorted(t["input_schema"]["properties"]) for t in TOOLS_V2}
    reg.test("H.agente", clave, "specs v2: nombres == v1 y parámetros declarados",
             nombres == [t["name"] for t in TOOLS] and params == {"buscar_nodos": ["consulta", "limite"], "ver_nodo": ["id"],
                                                                 "ver_vecinos": ["id", "pagina", "por_pagina", "relacion"]},
             None, params)
    reg.test("H.agente", clave, "contexto_de: NotImplementedError (punto de extensión)",
             _lanza_ni(tools), True, None)


def _lanza_ni(tools) -> bool:
    try:
        tools.contexto_de("x")
    except NotImplementedError:
        return True
    return False


# --------------------------------------------------------------------------- #
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(SALIDA_DEFAULT))
    ap.add_argument("--grafos", nargs="*", default=CLAVES)
    args = ap.parse_args()

    driver = abrir_driver()
    reg = Registro()
    resultados = {"unidad": "U-A1.2", "descripcion": "selftest determinístico de tools v2 (valores esperados derivados del kg.json)",
                  "por_grafo": {}}
    for clave in args.grafos:
        g = GRAFOS[clave]
        print(f"\n######## {clave} ({g['nombre_canonico']}, {g['sha256'][:8]}) ########")
        seccion_0(reg, driver, clave)
        kg = cargar_vista_runtime(clave)
        der = Derivado(kg)
        gi = GraphIndex(kg)
        tools = ToolsV2(driver, grafo=clave)
        info = {"kg": rel_repo(g["path"]), "sha256": g["sha256"], "n_nodos": len(kg.nodes), "n_aristas": len(kg.edges),
                "relaciones": sorted({e.relation for e in kg.edges})}
        info["A_BKL0027"] = seccion_A(reg, tools, der, gi, clave)
        info["B_BKL0022"] = seccion_B(reg, tools, der, gi, clave)
        info["C_paginacion"] = seccion_C(reg, tools, der, clave, [NODO_BKL0027, HUB_BKL0022])
        info["D_filtro"] = seccion_D(reg, tools, der, clave, [der.hub_max("entrantes"), NODO_BKL0027, HUB_BKL0022])
        info["E_busqueda"] = seccion_E(reg, driver, tools, der, gi, clave)
        ids_f = [x for x in (NODO_BKL0027, NODO_BKL0022, HUB_BKL0022, NODO_BKL0003, der.hub_max("entrantes")) if x in der.by_id]
        seccion_F(reg, tools, gi, der, clave, ids_f)
        seccion_G(reg, tools, der, clave, [NODO_BKL0027, HUB_BKL0022, der.hub_max("salientes")])
        seccion_H(reg, driver, tools, clave)
        resultados["por_grafo"][clave] = info
    driver.close()

    resultados["tests"] = reg.tests
    resultados["resumen"] = reg.resumen()
    resultados["defaults"] = {"limite": 10, "por_pagina": POR_PAGINA_DEFAULT, "por_pagina_max": POR_PAGINA_MAX}
    txt = json.dumps(resultados, ensure_ascii=False, indent=1)
    Path(args.salida).write_text(txt, encoding="utf-8")
    r = reg.resumen()
    print(f"\nRESUMEN: rigen {r['rigen']} → pasan {r['pasan']} / fallan {r['fallan']}; informativos {r['informativos']}")
    print(f"salida: {args.salida}  sha256={sha_texto(txt)}")
    sys.exit(0 if r["fallan"] == 0 else 1)


if __name__ == "__main__":
    main()
