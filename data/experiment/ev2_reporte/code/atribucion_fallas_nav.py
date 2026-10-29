"""
atribucion_fallas_nav.py — Atribución DETERMINÍSTICA de fallas con las herramientas de navegación del brazo del grafo
de B6.3 (ATRIB_NAV). Módulo NUEVO que IMPORTA `atribucion_fallas.py` sin editarlo.

Regla: `data/experiment/ev2_reporte/regla_atribucion.md` con su enmienda de la navegación (la opción (a); borrador en
el paquete de ATRIB_NAV, para la firma de la autora). Hasta que la enmienda esté firmada, este módulo no corre sobre
B6.3.

Lo que no cambia (se importa de atribucion_fallas, sin copiarlo):
  · las cuatro clases y su precedencia (`clasificar`);
  · la resolución del ancla (§2): `ancla_index.resolver(to, punto)`; el ancla puede venir como «to:punto» (EV2) o
    como «to::punto» (B6.3, el formato de ucita2_indicadores_banco);
  · «vista» y «consultada» de las tres herramientas v1 (§3), por `navegacion_de_traza` sobre los steps v1, con la
    re-ejecución de metrica.evaluar_traza y los dos replays (`replay_ok`, `replay_fuerte_ok`), que cubren solo
    esos steps. Sobre una traza que usa solo las tres v1, la salida es, byte a byte, la de
    `atribucion_fallas.atribuir_payload`.

Lo que suma, para las siete de navegación. Su salida es el texto del log R1, que el adaptador del banco
(adaptador_banco_nav.py) guarda en `steps_full`; no se re-ejecuta (necesitaría Neo4j y el codificador): se controla
contra `output_truncado`/`output_chars` del mismo step (metrica._check_replay, sobre el texto).
  · VISTA: el punto del ancla, o un nodo que la porta, aparece en la salida fuera de su cabecera (la primera línea,
    que repite la entrada). Se lee con:
      - las claves `to::unidad` del lector de ucita2_indicadores_banco (`leer_vista_nav`: fuera de la cabecera; el
        punto pedido de ver_punto cuando muestra su texto; en ver_descendientes, la clave de cada descendiente),
        llevadas a su punto con indice_puntos.base_punto. Cuenta la clave del punto del ancla, y cuenta un nodo del
        ancla que es uno de los nodos de alguna de esas claves en el índice por punto (`puntos.json`, `nodos`);
      - el lector nuevo de ids de nodo (`ids_en_salida`), con el mismo criterio de cabecera: cada palabra del cuerpo,
        partido por blancos, «|», «;» y «·», que es el id de un nodo del grafo (`nodos.json`). Lee las filas de
        buscar_puntos, la lista de nodos de ver_punto, las filas de vecinos_por_relacion y cualquier id que muestre
        otra salida (indice_to, tipos_de_relacion, ver_remisiones, ver_descendientes).
  · CONSULTADA: además de ver_nodo y ver_vecinos (v1), ver_punto del punto del ancla cuando muestra su texto (la
    tercera línea del cuerpo es «Texto (n caracteres):», el criterio de ucita2_indicadores_banco), y
    ver_descendientes cuando el bloque del punto del ancla trae su texto («Texto (n caracteres):», o
    «Texto (n caracteres, cortado en m):» cuando el tope lo corta). El ancla consultada por texto lo está como punto
    (`consultada_via`: «ver_punto» o «ver_descendientes»); los nodos no cambian su `consultado`.
  · Las salidas de error de una herramienta («<herramienta>: …», «herramienta desconocida: …») no muestran nada.
  · Un step cuya herramienta no es ninguna de las diez (un pedido a un nombre que no es una herramienta, como
    `mcp__kg`) no llegó al servidor: no hace vista ni consultada y se cuenta aparte, junto con los
    `banco.pedidos_sin_herramienta` del adaptador.

Lo que cambia para las trazas del banco (vuelta b, los dos cierres del §7 del borrador):
  · PRESENCIA: `AnclaIndexBanco`, con la interfaz y la regla de resolucion.AnclaIndex (punto exacto, contenedores
    excluidos) y un lector de las procedencias `{to, punto}` del grafo del banco. Son contenedores los nodos que portan
    más de 10 claves distintas y los `TextoOrdenado` (indice_puntos.TIPOS_FUERA_DE_PUNTO), que en el grafo de B6.3
    pueden portar 10 o menos. resolucion.AnclaIndex sigue sirviendo a los grafos de EV2.
  · LAS V1 DEL BANCO, DEL LOG R1 (`atribuir_payload(..., log_r1=...)`): la salida de cada step v1 es el `output_str`
    de su llamada reconciliada por R7 (el mapa del adaptador), controlada con su `output_sha256`, con la salida de la
    sesión (el control del adaptador) y leída como JSON. metrica.evaluar_traza la recibe por un índice doble
    (`IndiceDelLog`) con `verificar_replay=False`: el control del log reemplaza a la re-ejecución y `replay_ok` sale de
    él. Un control que falla invalida la corrida entera (`corrida_valida`), como una re-ejecución que diverge (§3).
    Las trazas del harness (EV2) siguen con la re-ejecución de HEAD, byte a byte.

Uso: biblioteca (`atribuir_payload`, `cargar_lectura`, `AnclaIndexBanco`, `corrida_valida`); sus pruebas, en
pruebas_atribucion_nav.py.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO_DIR = AQUI.parents[3]
SCRIPTS_DIR = REPO_DIR / "scripts"
for _p in (str(AQUI), str(SCRIPTS_DIR)):
    if _p not in sys.path:
        sys.path.insert(0, _p)

import atribucion_fallas as AF  # noqa: E402  (HEAD, sin editar)
import ucita2_indicadores_banco as U  # noqa: E402  (HEAD, sin editar: los lectores de las vistas del grafo)
from harness import TOOLS as _TOOLS_HARNESS  # noqa: E402  (cuarteto sellado: solo import; vía sys.path de comun_ev2)
from metrica import _check_replay  # noqa: E402  (sintéticas, sin editar)
from resolucion import CONTENEDOR_MAX_ANCLAS  # noqa: E402  (sintéticas, sin editar: el umbral del §2)

if AF.REPO_DIR.resolve() != REPO_DIR.resolve():
    raise SystemExit("ABORTO: atribucion_fallas.py no es el de este mismo árbol")

IP = U.IP
TOOLS_V1 = tuple(t["name"] for t in _TOOLS_HARNESS)
TOOLS_NAV = tuple(U.TOOLS_NAV)
TOOLS_KG = TOOLS_V1 + TOOLS_NAV
VIAS_TEXTO = ("ver_punto", "ver_descendientes")
RE_TEXTO_CORTADO = re.compile(r"^Texto \(\d+ caracteres, cortado en \d+\):$")
RE_SEPARADORES = re.compile(r"[\s|;·]+")
REGLA = "regla_atribucion.md con la enmienda de la navegación (opción (a)); borrador hasta su firma"


# --------------------------------------------------------------------------- #
# Anclas                                                                       #
# --------------------------------------------------------------------------- #
def parse_ancla(s: str) -> tuple[str, str]:
    """'ext::6.11' -> ('ext', '6.11'); 'ext:6.11' -> atribucion_fallas.parse_ancla. Decide el primer separador."""
    i = s.find(":")
    if i >= 0 and s[i:i + 2] == "::":
        return s[:i], s[i + 2:]
    return AF.parse_ancla(s)


def clave_de_ancla(s: str) -> str:
    to, punto = parse_ancla(s)
    return IP.base_punto(f"{to}::{punto}")


def resolver_anclas(anclas: list[str], ancla_index) -> dict[str, list[str]]:
    return {a: ancla_index.resolver(*parse_ancla(a)) for a in anclas}


class AnclaIndexBanco:
    """Índice (to, ancla) -> [ids de nodo] sobre el kg.json crudo de un grafo del banco, con procedencias
    `{to, punto, …}`. La interfaz (`resolver`, `censo`, `por_ancla`, `contenedores`, `sin_parsear`) y la regla del §2
    (punto exacto, contenedores excluidos) son las de resolucion.AnclaIndex; cambia el lector de las procedencias:
      · las procedencias de cada nodo, `provenances` o, si no está, `provenance` (indice_puntos.cargar_nodos);
      · la clave de cada procedencia con `to` y `punto`: indice_puntos.base_punto(f"{to}::{punto.strip()}");
      · contenedores: los nodos que portan más de `contenedor_max_anclas` claves distintas y los de los tipos de
        indice_puntos.TIPOS_FUERA_DE_PUNTO (`TextoOrdenado`), que portan su TO entero aunque sean 10 claves o menos.
    El ancla se lleva a su clave con el mismo base_punto (y el mismo strip)."""

    def __init__(self, kg_raw: dict, contenedor_max_anclas: int = CONTENEDOR_MAX_ANCLAS):
        self.por_ancla: dict[tuple, list] = {}
        self.sin_parsear: list[dict] = []
        self.contenedores: dict[str, int] = {}   # id -> n claves distintas
        self.fuente: dict = {}
        for n in kg_raw.get("nodes", []):
            provs = n.get("provenances") or ([n["provenance"]] if n.get("provenance") else [])
            claves = []
            for pv in provs:
                if isinstance(pv, dict) and pv.get("to") and pv.get("punto"):
                    k = IP.base_punto(f"{pv['to']}::{str(pv['punto']).strip()}")
                    if k not in claves:
                        claves.append(k)
                else:
                    self.sin_parsear.append({"node_id": n["id"]})
            if len(claves) > contenedor_max_anclas or n.get("type") in IP.TIPOS_FUERA_DE_PUNTO:
                self.contenedores[n["id"]] = len(claves)
            for k in claves:
                to, _, resto = k.partition("::")
                self.por_ancla.setdefault((to, resto), []).append(n["id"])

    @classmethod
    def desde_indice(cls, indice_dir: Path, sha256_manifiesto: str | None = None,
                     repo_dir: Path = REPO_DIR) -> "AnclaIndexBanco":
        """El grafo por el `kg_path` del manifiesto de su índice por punto, con su sha256 controlado antes de leerlo."""
        man_p = Path(indice_dir) / "manifiesto.json"
        if sha256_manifiesto is not None and IP.sha256_file(man_p) != sha256_manifiesto:
            raise SystemExit(f"ABORTO: sha256 de {man_p.name} != el esperado")
        man = json.loads(man_p.read_text(encoding="utf-8"))
        crudo = (Path(repo_dir) / man["kg_path"]).read_bytes()
        if hashlib.sha256(crudo).hexdigest() != man["kg_sha256"]:
            raise SystemExit("ABORTO: el kg.json del manifiesto del índice por punto no da su kg_sha256")
        ai = cls(json.loads(crudo))
        ai.fuente = {"kg_path": man["kg_path"], "kg_sha256": man["kg_sha256"], "grafo": man.get("grafo"),
                     "sha256_manifiesto": IP.sha256_file(man_p)}
        return ai

    @staticmethod
    def clave(to: str, ancla: str) -> str:
        return IP.base_punto(f"{to}::{str(ancla).strip()}")

    def resolver(self, to: str, ancla: str, incluir_descendientes: bool = False,
                 incluir_contenedores: bool = False) -> list:
        """Ids de los nodos que portan la clave del ancla (orden de aparición en el kg)."""
        to_k, _, resto = self.clave(to, ancla).partition("::")
        if not incluir_descendientes:
            ids = list(self.por_ancla.get((to_k, resto), []))
        else:
            ids, vistos = [], set()
            prefijo = resto + "."
            for (t, a), nodos in self.por_ancla.items():
                if t == to_k and (a == resto or a.startswith(prefijo)):
                    for nid in nodos:
                        if nid not in vistos:
                            vistos.add(nid)
                            ids.append(nid)
        if not incluir_contenedores:
            ids = [i for i in ids if i not in self.contenedores]
        return ids

    def censo(self, anclas: list[dict]) -> dict:
        """Como resolucion.AnclaIndex.censo: anclas [{'to','ancla'}] -> resueltas, ausentes y nodos_gold."""
        resueltas, ausentes, nodos, vistos = {}, [], [], set()
        for a in anclas:
            key = (a["to"], a["ancla"])
            ids = self.resolver(*key)
            if ids:
                resueltas[key] = ids
                for nid in ids:
                    if nid not in vistos:
                        vistos.add(nid)
                        nodos.append(nid)
            else:
                ausentes.append(key)
        return {"resueltas": resueltas, "ausentes": ausentes, "nodos_gold": nodos}


# --------------------------------------------------------------------------- #
# Lectores de las salidas de navegación                                        #
# --------------------------------------------------------------------------- #
def es_salida_de_error(tool: str, output_str: str) -> bool:
    """El mismo criterio que ucita2_indicadores_banco.leer_vista_nav."""
    return output_str.startswith(f"{tool}:") or output_str.startswith("herramienta desconocida:")


def _clave(par: tuple) -> str:
    return f"{par[0]}::{par[1]}"


def _sin_repetir(xs) -> list:
    return list(dict.fromkeys(xs))


def ids_en_salida(tool: str, output_str: str, ids_validos) -> list[str]:
    """Los ids de nodo que la salida muestra fuera de su cabecera: las palabras del cuerpo que son ids del grafo."""
    if es_salida_de_error(tool, output_str):
        return []
    _, _, cuerpo = output_str.partition("\n")
    return _sin_repetir(t for t in RE_SEPARADORES.split(cuerpo) if t in ids_validos)


def textos_mostrados(tool: str, output_str: str, man: dict) -> list[str]:
    """Las claves de los puntos cuyo texto propio muestra la salida: el punto pedido de ver_punto y los descendientes
    de ver_descendientes que traen su texto (entero o cortado por el tope)."""
    if es_salida_de_error(tool, output_str):
        return []
    cabecera, _, cuerpo = output_str.partition("\n")
    lineas = cuerpo.split("\n")
    out = []
    if tool == "ver_punto":
        m = U.RE_CABEZA_VP.match(cabecera)
        if m and len(lineas) > 2 and U.RE_TEXTO_VP.match(lineas[2]):
            out.append(_clave(U._clave_a_par(m.group(1), man)))
    if tool == "ver_descendientes":
        m = U.RE_CABEZA_DESC.match(cabecera)
        if m:
            to = IP.base_punto(m.group(1)).partition("::")[0]
            for i, linea in enumerate(lineas):
                b = U.RE_BLOQUE_DESC.match(linea)
                if b and i + 1 < len(lineas) and (U.RE_TEXTO_VP.match(lineas[i + 1])
                                                  or RE_TEXTO_CORTADO.match(lineas[i + 1])):
                    out.append(_clave(U._clave_a_par(f"{to}::{b.group(1)}", man)))
    return _sin_repetir(out)


def leer_paso(tool: str, output_str: str, lectura: dict) -> dict:
    """Lo que muestra la salida de una herramienta de navegación: claves de punto, ids de nodo, los nodos de esas
    claves en el índice por punto y los puntos cuyo texto muestra."""
    if tool not in TOOLS_NAV:
        raise ValueError(f"herramienta sin lector de navegación: {tool!r}")
    claves = _sin_repetir(_clave(p) for p in U.leer_vista_nav(tool, output_str, lectura["man"]))
    return {"error": es_salida_de_error(tool, output_str),
            "claves": claves,
            "ids": ids_en_salida(tool, output_str, lectura["ids"]),
            "nodos_de_claves": _sin_repetir(nid for k in claves for nid in lectura["nodos_por_punto"].get(k, ())),
            "textos": textos_mostrados(tool, output_str, lectura["man"])}


def cargar_lectura(indice_dir: Path, sha256_manifiesto: str | None = None, repo_dir: Path = REPO_DIR) -> dict:
    """El índice por punto de un grafo (puntos.json y nodos.json, con los sha256 de su manifiesto) y el manifiesto
    de TOs de los lectores de ucita2_indicadores_banco, armado como en su control 2: el archivo_a_to del índice y las
    secciones de la E0 que nombra su manifiesto (estructura_<to>.json, con sus sha256)."""
    indice_dir = Path(indice_dir)
    man_p = indice_dir / "manifiesto.json"
    if sha256_manifiesto is not None and IP.sha256_file(man_p) != sha256_manifiesto:
        raise SystemExit(f"ABORTO: sha256 de {man_p.name} != el esperado")
    man_idx = json.loads(man_p.read_text(encoding="utf-8"))
    for nombre in ("puntos.json", "nodos.json"):
        if IP.sha256_file(indice_dir / nombre) != man_idx["archivos"][nombre]:
            raise SystemExit(f"ABORTO: sha256 de {nombre} != el del manifiesto del índice por punto")
    puntos = json.loads((indice_dir / "puntos.json").read_text(encoding="utf-8"))
    nodos = json.loads((indice_dir / "nodos.json").read_text(encoding="utf-8"))
    e0 = Path(repo_dir) / man_idx["e0_dir"]
    malos = [n for n, sha in sorted(man_idx["insumos_e0"].items())
             if n.startswith("estructura_") and IP.sha256_file(e0 / n) != sha]
    if malos:
        raise SystemExit(f"ABORTO: {len(malos)} estructura_<to>.json de la E0 no son los del manifiesto del índice")
    tos = sorted(set(man_idx["archivo_a_to"].values()))
    man = U.armar_manifiesto([{"id": t, "archivo": a} for a, t in sorted(man_idx["archivo_a_to"].items())],
                             U.secciones_e0(e0, tos))
    return {"man": man,
            "nodos_por_punto": {k: list(p["nodos"]) for k, p in puntos.items() if p["tipo"] != "to"},
            "ids": frozenset(nodos),
            "fuente": {"indice_puntos": U.ruta_legible(indice_dir), "sha256_manifiesto": IP.sha256_file(man_p),
                       "grafo": man_idx.get("grafo"), "kg_sha256": man_idx.get("kg_sha256"),
                       "e0_dir": man_idx["e0_dir"], "n_puntos": len(puntos), "n_nodos": len(nodos)}}


# --------------------------------------------------------------------------- #
# Las v1 del banco, del log R1                                                 #
# --------------------------------------------------------------------------- #
def leer_log_r1(path: Path) -> dict:
    """Las líneas `llamada` de un log R1 (comun_banco.LogR1)."""
    lineas = [json.loads(x) for x in Path(path).read_text(encoding="utf-8").splitlines() if x.strip()]
    return {"llamadas": [x for x in lineas if x.get("evento") == "llamada"]}


def entrada_v1(tool: str, args: dict) -> tuple:
    """La entrada de un step v1 como la pasa metrica._reejecutar_step a la herramienta (con los defaults del harness)."""
    if tool == "buscar_nodos":
        valores = (args.get("consulta", ""), args.get("limite", 10))
    elif tool == "ver_nodo":
        valores = (args.get("id", ""),)
    else:
        valores = (args.get("id", ""), args.get("direccion", "ambas"))
    return (tool,) + tuple(json.dumps(v, ensure_ascii=False, sort_keys=True) for v in valores)


def controlar_v1_del_log(payload: dict, log: dict) -> tuple[dict, list]:
    """(tabla, fallas). Para cada step v1 de la traza: su llamada reconciliada por R7 (el `n_log` del mapa del
    adaptador, que aceptó el step, con la salida de la sesión igual a la del log o truncada por el transporte), con la
    misma herramienta y la misma entrada, un `output_str` cuyo sha256 es su `output_sha256`, y que se lee como JSON.
    La tabla va de la entrada (entrada_v1) a esa salida; dos salidas distintas para una misma entrada también fallan."""
    fallas, tabla = [], {}
    por_n = {}
    for ll in log["llamadas"]:
        if ll.get("n") in por_n:
            fallas.append({"n": None, "tool": None, "motivo": f"el log repite el n {ll.get('n')}"})
        por_n[ll.get("n")] = ll
    mapa = {m["n"]: m for m in (payload.get("gate") or {}).get("mapa_steps", [])}
    for st in payload["trace"].get("steps", []):
        if st.get("tool") not in TOOLS_V1:
            continue
        m, motivo, obj = mapa.get(st["n"]), None, None
        ll = por_n.get(m.get("n_log")) if m else None
        if m is None or not m.get("ok"):
            motivo = "R7: el step no tiene una llamada del log aceptada en el mapa del adaptador"
        elif m.get("sesion_igual_al_log") is False and not m.get("sesion_truncada_por_transporte"):
            motivo = "la salida de la sesión no es la del log"
        elif ll is None:
            motivo = "R7: el log no tiene la llamada del mapa"
        elif ll.get("tool") != st["tool"] or ll.get("input") != st.get("input"):
            motivo = "R7: la herramienta o la entrada del log no son las del step"
        elif ll.get("output_str") is None:
            motivo = "el log registró un error del servidor"
        elif hashlib.sha256(ll["output_str"].encode("utf-8")).hexdigest() != ll.get("output_sha256"):
            motivo = "el sha256 del output_str no es el output_sha256 del log"
        else:
            try:
                obj = json.loads(ll["output_str"])
            except json.JSONDecodeError:
                motivo = "la salida del log no se lee como JSON"
        if motivo is None:
            clave = entrada_v1(st["tool"], st.get("input") or {})
            if clave in tabla and tabla[clave] != obj:
                motivo = "dos salidas distintas del log para la misma entrada"
            else:
                tabla[clave] = obj
        if motivo:
            fallas.append({"n": st["n"], "tool": st["tool"], "motivo": motivo})
    return tabla, fallas


class IndiceDelLog:
    """El índice de las v1 de una traza del banco: para la entrada de cada step v1, la salida que registró el log R1,
    ya controlada (controlar_v1_del_log). Tiene la interfaz que usa metrica._reejecutar_step, así la regla v1 de HEAD
    (metrica.evaluar_traza) se aplica sin cambios. Una entrada sin salida controlada da un error, que no cuenta."""

    def __init__(self, tabla: dict):
        self.tabla = tabla

    def _de(self, clave: tuple):
        return self.tabla.get(clave, {"error": "sin salida controlada del log R1 para esta entrada"})

    def buscar_nodos(self, consulta, limite=10):
        return self._de(entrada_v1("buscar_nodos", {"consulta": consulta, "limite": limite}))

    def ver_nodo(self, id):
        return self._de(entrada_v1("ver_nodo", {"id": id}))

    def ver_vecinos(self, id, direccion="ambas"):
        return self._de(entrada_v1("ver_vecinos", {"id": id, "direccion": direccion}))


def corrida_valida(atribuciones: list[dict]) -> bool:
    """§3: la corrida es inválida si alguna traza diverge; con las v1 del log, si algún control del log falla."""
    return all(a["replay_ok"] and a["replay_fuerte_ok"] for a in atribuciones)


# --------------------------------------------------------------------------- #
# Atribución                                                                    #
# --------------------------------------------------------------------------- #
def _sumar_navegacion(nav: dict, steps_nav: list, steps_full: list, resueltas: dict, lectura: dict,
                      sin_herramienta: list, pedidos_adaptador: int) -> dict:
    """Suma a `nav` (salida de atribucion_fallas.navegacion_de_traza sobre los steps v1) lo que muestran los steps de
    navegación, y devuelve el bloque de detalle `navegacion_b63`."""
    salida_de = {sf["n"]: sf for sf in steps_full}
    lecturas, inconsistencias = [], []
    for st in sorted(steps_nav, key=lambda s: s["n"]):
        sf = salida_de.get(st["n"])
        if sf is None or sf.get("tool") != st["tool"] or not isinstance(sf.get("output"), str):
            raise ValueError(f"step {st['n']} ({st['tool']}): sin su salida de texto en steps_full "
                             "(un step rechazado por el adaptador: la traza no es atribuible)")
        falla = _check_replay(st, sf["output"])
        if falla:
            inconsistencias.append({"n": st["n"], "tool": st["tool"], "motivo": falla})
        lecturas.append({"n": st["n"], "tool": st["tool"], **leer_paso(st["tool"], sf["output"], lectura)})

    for a, ids in resueltas.items():
        pa = nav["por_ancla"][a]
        if not pa["presente"]:
            continue
        clave = clave_de_ancla(a)
        por_nodo = {p["nodo"]: p for p in pa["por_nodo"]}
        ev_vista, ev_cons = [], []
        for lec in lecturas:
            n = lec["n"]
            if clave in lec["claves"]:
                ev_vista.append({"n": n, "tool": lec["tool"], "via": "clave_del_punto"})
            for nid in ids:
                vias = [v for v, ok in (("id_de_nodo", nid in lec["ids"]),
                                        ("nodo_de_una_clave", nid in lec["nodos_de_claves"])) if ok]
                if not vias:
                    continue
                ev_vista += [{"n": n, "tool": lec["tool"], "via": v, "nodo": nid} for v in vias]
                p = por_nodo[nid]
                if not p["visto"] or n < p["visto_en_step"]:
                    p["visto"], p["visto_en_step"] = True, n
                p["brecha_visto_sin_consultar"] = p["visto"] and not p["consultado"]
            if lec["tool"] in VIAS_TEXTO and clave in lec["textos"]:
                ev_cons.append({"n": n, "tool": lec["tool"], "via": lec["tool"]})
        vistos = [p for p in pa["por_nodo"] if p["visto"]]
        cons = [p for p in pa["por_nodo"] if p["consultado"]]
        pasos_vista = [p["visto_en_step"] for p in vistos] + [e["n"] for e in ev_vista if e["via"] == "clave_del_punto"]
        pasos_cons = [p["consultado_en_step"] for p in cons] + [e["n"] for e in ev_cons]
        pa["vista"] = bool(pasos_vista)
        pa["consultada"] = bool(pasos_cons)
        pa["vista_en_step"] = min(pasos_vista) if pasos_vista else None
        pa["consultada_en_step"] = min(pasos_cons) if pasos_cons else None
        pa["consultada_via"] = sorted({p["consultado_via"] for p in cons} | {e["via"] for e in ev_cons})
        pa["navegacion"] = {"clave": clave, "vista": ev_vista, "consultada": ev_cons}
    nav["vista"] = any(x["vista"] for x in nav["por_ancla"].values())
    nav["consultada"] = any(x["consultada"] for x in nav["por_ancla"].values())

    por_tool = {}
    for lec in lecturas:
        por_tool[lec["tool"]] = por_tool.get(lec["tool"], 0) + 1
    return {"regla": REGLA,
            "n_steps_navegacion": len(steps_nav),
            "por_herramienta": dict(sorted(por_tool.items())),
            "consistencia_steps_full_ok": not inconsistencias,
            "consistencia_steps_full_fallas": inconsistencias,
            "pedidos_sin_herramienta": {"en_el_adaptador": pedidos_adaptador,
                                        "en_steps": [{"n": s.get("n"), "tool": s.get("tool")} for s in sin_herramienta]},
            "lecturas": lecturas}


def atribuir_payload(payload: dict, anclas: list[str], ancla_index, index, veredicto: str,
                     lectura: dict | None = None, replay_fuerte: bool = True, log_r1=None) -> dict:
    """Atribución de UNA traza (forma de atribucion_fallas.atribuir_payload, con los steps de navegación del brazo
    del grafo de B6.3). Las v1: en una traza del harness, `index` las re-ejecuta (harness.GraphIndex); en una traza
    del banco, `log_r1` (la ruta del log R1 de la sesión o su lectura, leer_log_r1) las da desde el log, `index` va en
    None y `replay_ok` sale del control del log. `lectura` (cargar_lectura) lee los steps de navegación y hace falta
    solo si la traza los tiene."""
    trace = payload["trace"]
    steps = trace.get("steps", [])
    steps_v1 = [s for s in steps if s.get("tool") in TOOLS_V1]
    steps_nav = [s for s in steps if s.get("tool") in TOOLS_NAV]
    sin_herramienta = [s for s in steps if s.get("tool") not in TOOLS_KG]
    pedidos_adaptador = (((payload.get("banco") or {}).get("pedidos_sin_herramienta")) or {}).get("n", 0)
    trace_v1 = {**trace, "steps": steps_v1}
    payload_v1 = {**payload, "trace": trace_v1,
                  "steps_full": [sf for sf in payload.get("steps_full", []) if sf.get("tool") in TOOLS_V1]}

    resueltas = resolver_anclas(anclas, ancla_index)
    if log_r1 is None:
        nav = AF.navegacion_de_traza(trace_v1, resueltas, index, verificar_replay=True)
    else:
        if index is not None:
            raise ValueError("con log_r1 las v1 salen del log: `index` va en None")
        tabla, fallas_log = controlar_v1_del_log(payload, log_r1 if isinstance(log_r1, dict) else leer_log_r1(log_r1))
        index = IndiceDelLog(tabla)
        nav = AF.navegacion_de_traza(trace_v1, resueltas, index, verificar_replay=False)
        nav["replay_ok"], nav["replay_fallas"] = not fallas_log, fallas_log
    fallas_fuerte = AF.verificar_steps_full(payload_v1, index) if replay_fuerte else []
    bloque = None
    if steps_nav or sin_herramienta or pedidos_adaptador:
        if steps_nav and lectura is None:
            raise ValueError("la traza tiene steps de navegación y no se pasó `lectura` (cargar_lectura)")
        bloque = _sumar_navegacion(nav, steps_nav, payload.get("steps_full", []), resueltas, lectura,
                                   sin_herramienta, pedidos_adaptador)
    fj = trace.get("final_json") or {}
    out = {
        "veredicto": veredicto,
        "clase": AF.clasificar(veredicto, nav["presente"], nav["vista"], nav["consultada"]),
        "anclas": anclas,
        "ancla_presente": nav["presente"],
        "ancla_vista": nav["vista"],
        "ancla_consultada": nav["consultada"],
        "por_ancla": nav["por_ancla"],
        "n_steps": len(steps),
        "tool_calls_used": trace.get("tool_calls_used"),
        "hit_tool_limit": trace.get("hit_tool_limit"),
        "respondible_flag": fj.get("respondible") if isinstance(fj, dict) else None,
        "replay_ok": nav["replay_ok"],
        "replay_fallas": nav["replay_fallas"],
        "replay_fuerte_ok": not fallas_fuerte,
        "replay_fuerte_fallas": fallas_fuerte,
    }
    if bloque is not None:
        out["navegacion_b63"] = bloque
    return out
