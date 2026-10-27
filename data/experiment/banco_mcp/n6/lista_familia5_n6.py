#!/usr/bin/env python3
"""lista_familia5_n6.py — N6 de U-NAV-DISENO, paso 0: la lista de la familia 5 (vecinos selectivos) con la regla del
protocolo de N4 (sellado en f69e95ea, §3), sobre las 30 preguntas de N3, fuera de línea y a USD 0. Se calcula y se sella
antes de la primera llamada de N6.

La regla (N4, §3, de la medición 4 de N1): una pregunta pasa por un hub si (a) un nodo de su gold es hub del 1 % del
acumulado (grado ≥ 38: 216 nodos, comun_unav.hubs), o (b) desde el primer resultado de buscar_nodos con la pregunta, el
camino más corto al gold con todas las aristas es más corto que sin pasar por hubs del 1 % ni por TextoOrdenado, o sin
ellos no hay camino en 6 pasos. Gold: los portadores de sus criterios por R-CITA (la cita sin los cortes de palabra) en el
TO del ancla; si no hay, los nodos del ancla. La familia 5 se informa en las de la mezcla que pasan (N4, §3, la tabla).

Cómo se aplica, con el código de m234_acumulado_unav.py (la función de los pasos), sin editarlo y sin correr su main:
  · m234 importa al cargarse n1_trazas_unav.py, de una carpeta que esta unidad no abre, y su main lee EV2 y las preguntas de
    la tanda 0; los pasos son funciones anidadas en ese main. Así que este script lee m234 (su sha256, controlado), toma de
    su árbol sintáctico, tal cual, la función sin_cortes y, del cuerpo de main, las sentencias que arman el grafo, los hubs,
    la adyacencia y el backend, las funciones vecinos y dist y el bucle de los pasos (SENTENCIAS), y las ejecuta en orden;
    el sha256 de cada sentencia queda en la salida;
  · lo que ese código pide de n1_trazas_unav.py (claves, tokens, texto_nodo y evaluar_T) sale de R-CITA de D2
    (reports/u_pre_r2/upre_d2_ausencias.py: claves, tokens, texto_nodo y evaluar_cita, tomadas de su árbol sintáctico,
    tal cual, sin importar el módulo, que carga material de EV2): m234 declara «R-CITA de D2, sin cambios». evaluar_T es
    evaluar_cita con las claves y los tokens ya calculados, y la salida controla que den lo mismo en las 30;
  · las preguntas de N3 entran con la forma de EV2 que lee ese código: el ancla «to:punto», con el punto como lo nombra la
    procedencia de los nodos («5.1.1.» da «5.1.1»; «Sección 3.», «S3»), y cada criterio con su cita como cita_textual;
  · buscar_nodos corre sobre el Neo4j propio de N6 (servidor_mcp_kg.abrir_backend, como en m234).
Imprime y guarda solo ids de preguntas, booleanos y cuentas: ningún texto de pregunta, cita ni nodo.
Uso: NEO4J_URI=bolt://127.0.0.1:57687 python -B n6/lista_familia5_n6.py --salida <dir> [--sellar]
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import os
import re
import sys
import textwrap
import unicodedata
from collections import Counter, defaultdict, deque
from datetime import datetime
from pathlib import Path
from types import SimpleNamespace

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
COPIA = BANCO_DIR.parents[2]
FDR = Path.home() / "INGENIERIA IA" / "TESIS" / "fuera_del_repo"
M234 = FDR / "unav_parte1" / "scripts" / "m234_acumulado_unav.py"
COMUN = FDR / "unav_parte1" / "scripts" / "comun_unav.py"
PREGUNTAS_N3 = FDR / "unav_n3" / "preguntas_N3.json"
SELLO_N3 = FDR / "unav_n3" / "sello_N3.txt"
D2 = COPIA / "reports" / "u_pre_r2" / "upre_d2_ausencias.py"
SHA = {"m234": "67c4930f77bd517a17a96dc1dca2aa1ca267487fb9e5ab634392aaa8f07df31f",
       "comun_unav": "d66af9af1eede4eae3a2df75a5cfcf95e139f969ce5906ae48c2a5ec42f8ce25",
       "preguntas_N3": "6a92d18145e4957f39a0b87d9193a38ca592128c6e248fac0b8d1c9ecd82613b",
       "sello_N3": "dfb660fc82e15444c8cfc3cf74f6c5b5c44451bf1f4d89a53a363c72bf0d653a",
       "d2": "91fd1213bd0b517de5327ecb3cd36ec7c599a8e77c152ffadcc968a14ab6fa27"}
HUBS_CONFIG = {"umbral": 38, "n": 216, "sha256": "223866c9c217bc248b7c0c621548c9b2347bf54070df9c2867b52063ad808ea0"}
NEO4J_URI_N6 = "bolt://127.0.0.1:57687"
# Las sentencias del cuerpo de main de m234 que se ejecutan, en su orden, por su primer nombre asignado (o la función).
SENTENCIAS = ("kg", "ceg", "nodos", "puntos", "contenedor", "catalogo", "T", "grado", "h1", "sal", "for:sal",
              "GR.GRAFOS", "idx", "def:vecinos", "def:dist", "pasos", "for:pasos")
D2_NOMBRES = ("STOP", "RE_NUM", "RE_SIGLA", "RE_PAL", "normalizar", "claves", "tokens", "evaluar_cita", "texto_nodo")
CAMPOS_SALIDA = ("n_gold", "origen_gold", "gold_es_hub1", "entrada_es_hub1", "pasos_todas", "pasos_sin_hubs", "pasos_vista_40",
                 "pasos_mejor_top10_todas", "pasos_mejor_top10_sin_hubs", "pasa_por_un_hub")


def sha256_file(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def sha256_texto(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def controlar(p: Path, clave: str) -> str:
    s = sha256_file(p)
    if s != SHA[clave]:
        raise SystemExit(f"FRENO: {clave} da {s[:12]}…, no {SHA[clave][:12]}…")
    return s


def _nombre(t) -> str | None:
    if isinstance(t, ast.Name):
        return t.id
    if isinstance(t, ast.Tuple) and t.elts and isinstance(t.elts[0], ast.Name):
        return t.elts[0].id
    if isinstance(t, ast.Subscript) and isinstance(t.value, ast.Attribute):
        return f"{ast.unparse(t.value)}"
    return None


def sentencias_m234(src: str) -> tuple[list[tuple[str, str]], str]:
    """[(nombre, código)] de las SENTENCIAS de main, tal cual (get_source_segment y dedent), y el código de sin_cortes."""
    arbol = ast.parse(src)
    sin_cortes = next(n for n in arbol.body if isinstance(n, ast.FunctionDef) and n.name == "sin_cortes")
    main = next(n for n in arbol.body if isinstance(n, ast.FunctionDef) and n.name == "main")
    out = []
    for st in main.body:
        seg = textwrap.dedent(ast.get_source_segment(src, st, padded=True))
        nombre = None
        if isinstance(st, ast.Assign):
            nombre = _nombre(st.targets[0])
        elif isinstance(st, ast.FunctionDef):
            nombre = f"def:{st.name}"
        elif isinstance(st, ast.For):
            if "kg[\"edges\"]" in ast.get_source_segment(src, st.iter) and "sal[" in seg:
                nombre = "for:sal"
            elif "pasos.append" in seg:
                nombre = "for:pasos"
        if nombre in SENTENCIAS and nombre not in {n for n, _ in out}:
            out.append((nombre, seg))
    if [n for n, _ in out] != list(SENTENCIAS):
        raise SystemExit(f"FRENO: m234 no trae las sentencias esperadas, en su orden: {[n for n, _ in out]}")
    return out, ast.get_source_segment(src, sin_cortes)


def r_cita_de_d2(src: str) -> dict:
    """R-CITA de D2, tomada de su árbol sintáctico tal cual, sin importar el módulo."""
    import regression_kg as RK                   # noqa: PLC0415  (scripts/, solo biblioteca estándar)
    arbol = ast.parse(src)
    ns = {"re": re, "unicodedata": unicodedata, "RK": RK}
    partes = {}
    for st in arbol.body:
        nombre = st.name if isinstance(st, ast.FunctionDef) else (_nombre(st.targets[0]) if isinstance(st, ast.Assign) else None)
        if nombre in D2_NOMBRES:
            seg = ast.get_source_segment(src, st)
            exec(compile(seg, f"upre_d2_ausencias.py:{nombre}", "exec"), ns)
            partes[nombre] = sha256_texto(seg)
    if sorted(partes) != sorted(D2_NOMBRES):
        raise SystemExit(f"FRENO: D2 no trae {sorted(set(D2_NOMBRES) - set(partes))}")
    ns["_partes"] = partes
    return ns


def evaluar_T_de(ns: dict):
    def evaluar_T(cl: tuple, T: set) -> str:
        """evaluar_cita de D2 con las claves (claves(cita)) y los tokens (tokens(texto)) ya calculados."""
        nums, siglas, pals = cl
        req_ok = all(x in T for x in nums + siglas)
        cov = (sum(1 for w in pals if w in T) / len(pals)) if pals else 1.0
        if req_ok and cov >= 0.8:
            return "presente"
        if cov >= 0.5:
            return "parcial"
        return "ausente"
    return evaluar_T


def punto_de_procedencia(punto: str) -> str:
    """El punto de un ancla de N3 como lo nombra la procedencia de los nodos del acumulado."""
    s = re.sub(r"\.+$", "", punto.strip())
    m = re.match(r"^Secci[oó]n\s+(\S+)$", s)
    if m:
        return "S" + m.group(1)
    m = re.match(r"^Punto\s+(\S+)$", s)
    return m.group(1) if m else s


def preguntas_n3() -> tuple[list[dict], dict]:
    controlar(SELLO_N3, "sello_N3")
    controlar(PREGUNTAS_N3, "preguntas_N3")
    d = json.loads(PREGUNTAS_N3.read_text(encoding="utf-8"))
    ps = d["preguntas"]
    meta = {p["id"]: {"conjunto": p["conjunto"], "tipo": p["tipo"], "subtipo": p["subtipo"], "necesidad": p["necesidad"],
                      "n_criterios": len(p["gold"]["criterios"]), "n_anclas": len(p["gold"]["anclas"])} for p in ps}
    ev2 = [{"conjunto": "N3", "id": p["id"], "pregunta": p["pregunta"],
            "gold": {"ancla": [f"{a['to']}:{punto_de_procedencia(a['punto'])}" for a in p["gold"]["anclas"]],
                     "criterios": [{"cita_textual": c["cita"]} for c in p["gold"]["criterios"]]}} for p in ps]
    return ev2, meta


def calcular() -> dict:
    if os.environ.get("NEO4J_URI") != NEO4J_URI_N6:
        raise SystemExit(f"FRENO: NEO4J_URI no es la del Neo4j propio de N6 ({NEO4J_URI_N6})")
    fuentes = {"m234": controlar(M234, "m234"), "comun_unav": controlar(COMUN, "comun_unav"), "d2": controlar(D2, "d2")}
    for p in (str(M234.parent), str(BANCO_DIR / "mcp_kg"), str(COPIA / "scripts")):
        if p not in sys.path:
            sys.path.insert(0, p)
    import comun_unav as CU                      # noqa: PLC0415
    import servidor_mcp_kg as S                  # noqa: PLC0415  (agrega neo4j al path)
    import grafos as GR                          # noqa: PLC0415
    ev2, meta = preguntas_n3()
    fuentes |= {"preguntas_N3": SHA["preguntas_N3"], "sello_N3": SHA["sello_N3"]}
    sentencias, src_sin_cortes = sentencias_m234(M234.read_text(encoding="utf-8"))
    d2 = r_cita_de_d2(D2.read_text(encoding="utf-8"))
    N1 = SimpleNamespace(claves=d2["claves"], tokens=d2["tokens"], texto_nodo=d2["texto_nodo"], evaluar_T=evaluar_T_de(d2))
    ns = {"COPIA": COPIA, "CU": CU, "N1": N1, "S": S, "GR": GR, "defaultdict": defaultdict, "deque": deque,
          "Counter": Counter, "json": json, "re": re, "Path": Path, "preguntas": lambda: ev2}
    exec(compile(src_sin_cortes, "m234_acumulado_unav.py:sin_cortes", "exec"), ns)
    codigo = [{"sentencia": "sin_cortes", "sha256": sha256_texto(src_sin_cortes)}]
    for nombre, seg in sentencias:
        exec(compile(seg, f"m234_acumulado_unav.py:main:{nombre}", "exec"), ns)
        codigo.append({"sentencia": nombre, "sha256": sha256_texto(seg)})
    h1 = ns["h1"]
    hubs = {"umbral": ns["u1"], "n": len(h1), "sha256": sha256_texto("\n".join(sorted(h1)))}
    if hubs != HUBS_CONFIG:
        raise SystemExit(f"FRENO: los hubs del 1 % no son los de la config: {hubs}")
    # evaluar_T == evaluar_cita de D2, en los criterios de las 30 y una muestra de nodos de su TO
    nodos, T, puntos = ns["nodos"], ns["T"], ns["puntos"]
    iguales = total = 0
    for p in ev2:
        tos = {a.split(":", 1)[0] for a in p["gold"]["ancla"]}
        cand = sorted(n for n in nodos if any(tp[0] in tos for tp in puntos[n]))[::40]
        for cr in p["gold"]["criterios"]:
            c = ns["sin_cortes"](cr["cita_textual"])
            cl = N1.claves(c)
            for n in cand:
                total += 1
                iguales += N1.evaluar_T(cl, T[n]) == d2["evaluar_cita"](c, N1.texto_nodo(nodos[n]))
    filas = {f["id_pregunta"]: f for f in ns["pasos"]}
    por_pregunta = []
    for qid, m in meta.items():
        f = filas[qid]
        por_pregunta.append({"id": qid, **m, **{k: f.get(k) for k in CAMPOS_SALIDA}})
    lista = sorted(r["id"] for r in por_pregunta if r["conjunto"] == "mezcla" and r["pasa_por_un_hub"])
    pasan_todas = sorted(r["id"] for r in por_pregunta if r["pasa_por_un_hub"])
    return {
        "que": "la lista de la familia 5 de N6 (protocolo de N4, f69e95ea, §3): las preguntas de la mezcla de N3 que pasan por un hub",
        "regla": "N4, §3, la regla de la familia 5, aplicada con el código de m234_acumulado_unav.py (ver el docstring)",
        "fuentes": fuentes, "codigo_ejecutado_de_m234": codigo, "r_cita_de_d2": d2["_partes"],
        "hubs_1pc": hubs, "evaluar_T_igual_a_evaluar_cita": {"iguales": iguales, "total": total},
        "neo4j": {"NEO4J_URI": os.environ.get("NEO4J_URI")},
        "n_preguntas": len(por_pregunta), "por_pregunta": por_pregunta,
        "cuentas": {"pasan_por_un_hub_de_las_30": len(pasan_todas), "pasan_por_un_hub_de_la_mezcla": len(lista),
                    "por_a_gold_hub": sum(1 for r in por_pregunta if r["pasa_por_un_hub"] and r["gold_es_hub1"]),
                    "origen_gold": dict(Counter(r["origen_gold"] for r in por_pregunta)),
                    "sin_entrada_o_sin_gold": sum(1 for r in por_pregunta if r["pasos_todas"] is None)},
        "pasan_por_un_hub_de_las_30": pasan_todas,
        "lista_familia5": lista,
    }


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--sellar", action="store_true", help="escribe el sello (sha256 y hora) de la lista")
    a = ap.parse_args(argv)
    r = calcular()
    a.salida.mkdir(parents=True, exist_ok=True)
    p = a.salida / "lista_familia5_N6.json"
    texto = json.dumps(r, ensure_ascii=False, indent=1) + "\n"
    if p.exists() and p.read_text(encoding="utf-8") != texto:
        raise SystemExit(f"FRENO: {p.name} ya existe y difiere de lo recomputado")
    p.write_text(texto, encoding="utf-8")
    s = sha256_texto(texto)
    print(f"lista de la familia 5: {len(r['lista_familia5'])} de las de la mezcla pasan por un hub: {r['lista_familia5']}")
    print(f"cuentas: {json.dumps(r['cuentas'], ensure_ascii=False)}; hubs {r['hubs_1pc']['umbral']}, {r['hubs_1pc']['n']}; "
          f"evaluar_T = evaluar_cita: {r['evaluar_T_igual_a_evaluar_cita']}")
    print(f"{s}  {p.name}")
    if a.sellar:
        sello = a.salida / "sello_lista_familia5_N6.txt"
        if sello.exists():
            raise SystemExit("FRENO: el sello ya existe; la lista se sella una sola vez")
        hora = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M:%S %z")
        sello.write_text(f"# sello de la lista de la familia 5 de N6 (N4, §3 y §8, punto 6): sha256, bytes y hora\n"
                         f"# sellado: {hora}, antes de la primera llamada de N6 (ninguna sesión de N6 corrió)\n"
                         f"{s}  {len(texto.encode('utf-8'))}  lista_familia5_N6.json\n", encoding="utf-8")
        print(f"sellada: {hora}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
