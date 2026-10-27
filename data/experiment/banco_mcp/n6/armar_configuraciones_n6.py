#!/usr/bin/env python3
"""armar_configuraciones_n6.py — Las 8 configuraciones del brazo del grafo de N6 (protocolo de N4, sellado en f69e95ea, §2)
y las 2 de F1 (§6), armadas por código desde archivos de HEAD que no se editan. USD 0.

Escribe, en n6/:
  · plantilla_prompt_n6.txt: la de A2.2 (a2_2/plantilla_prompt_a2_2.txt, ff6c3d0a…, sin los cinco nombres de TOs) con la
    parte común de la decisión 9 del mandato (descomponer la pregunta y revisar las condiciones y las excepciones antes de
    responder), tal como la trae agentes/plantilla_prompt.txt de HEAD (renglones 14 a 19, el bloque «Antes de responder:»),
    en el mismo lugar: entre las reglas duras y la pregunta. Es la misma para las 10 configuraciones (N4, §1 y §6);
  · los bloques de herramientas (N4, §2), sin editar los de HEAD:
      B y T−F6  el de hoy: los tres renglones de las tres herramientas de hoy (agentes/bloque_tools_kg.txt antes de la
                familia 6; el blob de 17a51a42^), sin marcas;
      T         agentes/bloque_tools_kg.txt de HEAD (cccfcefd…, la familia 6) más el renglón de `ver_descendientes`
                (RENGLON_VER_DESCENDIENTES), después del de `ver_punto`;
      T−Fk      el de T sin los renglones de las herramientas de la familia k (la 2 saca `ver_punto` y
                `ver_descendientes`); los tres ejemplos quedan como están;
  · por configuración del grafo, su config del servidor (la de mcp_kg/config_mcp_kg_nav_acumulado.json con su `familias`,
    la versión del servidor nuevo y su nombre de configuración) y su JSON de MCP (el de mcp_kg/mcp_kg_nav.json con el
    servidor nuevo, mcp_kg/servidor_mcp_kg_nav_cand.py, y su config). T−F1, que no sirve buscar_puntos (la única herramienta
    que consulta el denso), va sin el denso: su servidor no lanza el codificador de consultas (SIN_CODIFICADOR; probado byte a
    byte con n6/comparar_tf1_sin_codificador.py);
  · config_agentes_n6.json, con la forma de paralelo/config_agentes_n6_prueba.json: el modelo, la versión del CLI y R5
    (30, 32 y 1,80) de A2.2, y por configuración su brazo (servidor, JSON de MCP, bloque y herramientas esperadas). Las
    dos de F1 son las de fragmentos del acumulado de HEAD (BM25 de A2.2 y la híbrida), con la plantilla de N6.

Modos: sin argumentos escribe (y no pisa un archivo distinto salvo --reescribir); --verificar arma en memoria y compara
byte a byte con lo que hay en disco (código 1 si algo difiere). Imprime solo nombres de archivo, sha256 y cuentas.
Uso: python3 -B n6/armar_configuraciones_n6.py [--verificar] [--reescribir]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent

PLANTILLA_A22 = BANCO_DIR / "a2_2" / "plantilla_prompt_a2_2.txt"
PLANTILLA_HEAD = BANCO_DIR / "agentes" / "plantilla_prompt.txt"
BLOQUE_HEAD = BANCO_DIR / "agentes" / "bloque_tools_kg.txt"
CONFIG_ACUM = BANCO_DIR / "mcp_kg" / "config_mcp_kg_nav_acumulado.json"
MCP_NAV = BANCO_DIR / "mcp_kg" / "mcp_kg_nav.json"
CONFIG_A22 = BANCO_DIR / "a2_2" / "config_agentes_a2_2.json"
SHA = {"plantilla_a2_2": "ff6c3d0a46c1ef5348bb824d93062658e8137374e3d0d5c2772af4fdc5372ab9",
       "plantilla_head": "dd99bfd3b220c7c5fc6464e1e203c75037af9ec88d9aa36fcf28409d646cca8c",
       "bloque_head": "cccfcefdfa61860269866d737e000897eafe5b5e1c57cb4cc743622f71ef7839",
       "bloque_de_hoy": "7ced741bffce79c339c741546df10393271e79a40a26341a92c5f47232a1f38c",
       "config_acumulado": "10229763ccd447204a6ceeec6bb962ed5743699855ce05e3ba13bf557981e636",
       "config_agentes_a2_2": "fd4ce4e4ce7d4c7cd0550af1ed2ba7d2cbd3d1a2301ee82060ba7d6eba4697c0"}

# Los cinco TOs de desarrollo, como los nombraba la plantilla de antes de A2.2 (mandato, §5): ninguna plantilla de N6
# los nombra (N4, §8, punto 2).
CINCO_TOS = ("capitales mínimos", "clasificación de deudores", "exterior y cambios",
             "protección de usuarios de servicios financieros", "régimen informativo contable mensual")
PARTE_COMUN_INICIO = "Antes de responder:\n"
ANCLA_PREGUNTA = "Pregunta: {{PREGUNTA}}\n"

# El renglón de instrucciones de ver_descendientes del bloque de T, PROPUESTO desde la descripción de la herramienta
# (familias_nav_cand.TOOL_VER_DESCENDIENTES), con la forma de los demás renglones de la familia 6. Lo aprueba la autora.
RENGLON_VER_DESCENDIENTES = (
    "- `ver_descendientes(punto, niveles)`: para leer de una vez el texto entero de los subpuntos de un punto, en orden de lectura,\n"
    "  hasta 3 niveles. Si la respuesta puede estar en los hijos de un punto, leelos así antes que abrirlos uno por uno con `ver_punto`.\n")

# El primer renglón de la entrada de cada herramienta en las instrucciones de la familia 6 (agentes/bloque_tools_kg.txt).
ENTRADA_DE = {"buscar_puntos": "- `buscar_puntos(", "ver_punto": "- `ver_punto(", "indice_to": "- `indice_to(",
              "ver_remisiones": "- `ver_remisiones(",
              "tipos_de_relacion": "- `tipos_de_relacion(id)` y `vecinos_por_relacion(",
              "ver_descendientes": "- `ver_descendientes("}
HERRAMIENTAS_DE_FAMILIA = {1: ("buscar_puntos",), 2: ("ver_punto", "ver_descendientes"), 3: ("ver_remisiones",),
                           4: ("indice_to",), 5: ("tipos_de_relacion", "vecinos_por_relacion")}
TRES_DE_HOY = ("buscar_nodos", "ver_nodo", "ver_vecinos")
# Las 8 configuraciones del grafo (N4, §2): id, familias del servidor y bloque.
CONFIGURACIONES = (("B", (), "B"), ("T", (1, 2, 3, 4, 5), "T"),
                   ("T-F1", (2, 3, 4, 5), "T-F1"), ("T-F2", (1, 3, 4, 5), "T-F2"), ("T-F3", (1, 2, 4, 5), "T-F3"),
                   ("T-F4", (1, 2, 3, 5), "T-F4"), ("T-F5", (1, 2, 3, 4), "T-F5"), ("T-F6", (1, 2, 3, 4, 5), "B"))
REPETICIONES = {"B": 3, "F1_bm25": 3}     # las demás, 1 (N4, §2 y §6; decisión 4)
# Las configuraciones del grafo con navegador que no sirven buscar_puntos: su servidor va sin el denso (decisión de la autora
# del 27/10/2026, punto 8, con la comparación byte a byte de n6/comparar_tf1_sin_codificador.py).
SIN_CODIFICADOR = ("T-F1",)
ARCHIVOS_SERVIDOR_KG = ["mcp_kg/servidor_mcp_kg_nav_cand.py", "mcp_kg/servidor_mcp_kg_nav.py", "mcp_kg/servidor_mcp_kg.py",
                        "mcp_kg/familias_nav.py", "mcp_kg/familias_nav_cand.py", "mcp_kg/indice_puntos.py",
                        "mcp_kg/codificador_consultas.py"]


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def leer(p: Path, clave: str) -> str:
    b = p.read_bytes()
    if sha256_bytes(b) != SHA[clave]:
        raise SystemExit(f"ABORTO: {p.relative_to(BANCO_DIR)} no da el sha256 esperado ({clave})")
    return b.decode("utf-8")


def brazo_kg(cid: str) -> str:
    return f"kg_{cid}"


def carga_codificador(cid: str, familias) -> bool:
    """Si el servidor de la configuración del grafo lanza el codificador de consultas: con navegador y con el denso."""
    return bool(familias) and cid not in SIN_CODIFICADOR


def herramientas(familias) -> list[str]:
    return list(TRES_DE_HOY) + [h for k in sorted(familias) for h in HERRAMIENTAS_DE_FAMILIA[k]]


# --------------------------------------------------------------------------- #
# Plantilla                                                                    #
# --------------------------------------------------------------------------- #
def parte_comun() -> str:
    """El bloque «Antes de responder:» de agentes/plantilla_prompt.txt de HEAD, con su renglón en blanco final."""
    t = leer(PLANTILLA_HEAD, "plantilla_head")
    i, j = t.index(PARTE_COMUN_INICIO), t.index(ANCLA_PREGUNTA)
    bloque = t[i:j]
    if t.count(PARTE_COMUN_INICIO) != 1 or not bloque.endswith("\n\n") or bloque.count("\n") != 6:
        raise SystemExit("ABORTO: la parte común no tiene la forma esperada en agentes/plantilla_prompt.txt")
    return bloque


def plantilla_n6() -> str:
    t = leer(PLANTILLA_A22, "plantilla_a2_2")
    if t.count(ANCLA_PREGUNTA) != 1 or PARTE_COMUN_INICIO in t:
        raise SystemExit("ABORTO: la plantilla de A2.2 no tiene la forma esperada")
    return t.replace(ANCLA_PREGUNTA, parte_comun() + ANCLA_PREGUNTA)


def control_plantilla(t: str) -> dict:
    """N4, §8, punto 2: ningún nombre de los cinco TOs de desarrollo (sin distinguir mayúsculas) y la parte común presente;
    y, como control de la forma, que sea la de HEAD con el renglón 1 de A2.2."""
    bajo = t.lower()
    nombres = {n: bajo.count(n) for n in CINCO_TOS}
    head = PLANTILLA_HEAD.read_text(encoding="utf-8").split("\n")
    a22 = PLANTILLA_A22.read_text(encoding="utf-8").split("\n")
    return {"nombres_de_los_cinco_TOs": sum(nombres.values()), "por_nombre": nombres,
            "parentesis_de_los_cinco": "(Textos Ordenados:" in t,
            "parte_comun_presente": t.count(parte_comun()) == 1,
            "es_la_de_HEAD_con_el_renglon_1_de_A2_2": t.split("\n") == [a22[0]] + head[1:],
            "placeholders": {p: t.count(p) for p in ("{{BLOQUE_TOOLS}}", "{{TOPE_TOOL_CALLS}}", "{{PREGUNTA}}")}}


# --------------------------------------------------------------------------- #
# Bloques                                                                      #
# --------------------------------------------------------------------------- #
def _entradas(lineas: list[str]) -> dict[str, tuple[int, int]]:
    """Por herramienta, el rango [i, j) de su entrada en las instrucciones (antes de los ejemplos): su primer renglón y
    los que siguen con sangría de dos espacios."""
    fin = next(i for i, l in enumerate(lineas) if l.startswith("Ejemplos de navegación."))
    out = {}
    for h, pref in ENTRADA_DE.items():
        idx = [i for i in range(fin) if lineas[i].startswith(pref)]
        if len(idx) > 1:
            raise SystemExit(f"ABORTO: la entrada de {h} aparece {len(idx)} veces")
        if idx:
            j = idx[0] + 1
            while j < fin and lineas[j].startswith("  "):
                j += 1
            out[h] = (idx[0], j)
    return out


def bloque_de_hoy() -> str:
    t = leer(BLOQUE_HEAD, "bloque_head")
    b = "".join(t.splitlines(keepends=True)[:3])
    if sha256_bytes(b.encode("utf-8")) != SHA["bloque_de_hoy"]:
        raise SystemExit("ABORTO: los tres primeros renglones del bloque de HEAD no son el bloque de hoy")
    return b


def bloque_T() -> str:
    lineas = leer(BLOQUE_HEAD, "bloque_head").splitlines(keepends=True)
    e = _entradas(lineas)
    if set(e) != set(ENTRADA_DE) - {"ver_descendientes"}:
        raise SystemExit(f"ABORTO: las entradas de la familia 6 de HEAD no son las esperadas: {sorted(e)}")
    j = e["ver_punto"][1]
    return "".join(lineas[:j]) + RENGLON_VER_DESCENDIENTES + "".join(lineas[j:])


def bloque_sin_familia(k: int) -> str:
    lineas = bloque_T().splitlines(keepends=True)
    e = _entradas(lineas)
    fuera = set()
    for h in HERRAMIENTAS_DE_FAMILIA[k]:
        if h in e:
            fuera |= set(range(*e[h]))
    if not fuera:
        raise SystemExit(f"ABORTO: la familia {k} no tiene renglones en el bloque de T")
    return "".join(l for i, l in enumerate(lineas) if i not in fuera)


def bloques() -> dict[str, str]:
    out = {"B": bloque_de_hoy(), "T": bloque_T()}
    for k in (1, 2, 3, 4, 5):
        out[f"T-F{k}"] = bloque_sin_familia(k)
    return out


def control_bloques(bs: dict[str, str]) -> dict:
    """Lo que saca cada bloque respecto de T, en renglones y por herramienta; y los ejemplos, iguales en T y en cada T−Fk."""
    lt = bs["T"].splitlines(keepends=True)
    ej = lambda t: t[t.index("Ejemplos de navegación."):]  # noqa: E731
    out = {"T": {"renglones": len(lt), "suma_respecto_de_HEAD": RENGLON_VER_DESCENDIENTES.count("\n"),
                 "entradas": sorted(_entradas(lt))}}
    for k in (1, 2, 3, 4, 5):
        c = f"T-F{k}"
        lc = bs[c].splitlines(keepends=True)
        out[c] = {"renglones": len(lc), "saca": len(lt) - len(lc), "entradas": sorted(_entradas(lc)),
                  "sin_las_de_la_familia": not (set(_entradas(lc)) & set(HERRAMIENTAS_DE_FAMILIA[k])),
                  "ejemplos_iguales_a_T": ej(bs[c]) == ej(bs["T"]),
                  "es_T_menos_esos_renglones": all(l in lt for l in lc)}
    out["B"] = {"renglones": bs["B"].count("\n"), "sha256": sha256_bytes(bs["B"].encode("utf-8"))}
    return out


# --------------------------------------------------------------------------- #
# Configs                                                                      #
# --------------------------------------------------------------------------- #
def config_servidor(cid: str, familias) -> dict:
    c = json.loads(leer(CONFIG_ACUM, "config_acumulado"))
    c["version"] = "1.0-nav-cand"
    c["familias"] = list(familias)
    c["firma_tools"] = ("v1 (harness.TOOLS, laudo R2 opcion B) + familias 1 a 5 de U-NAV-DISENO (diseño de N2) + "
                        "ver_descendientes en la familia 2 (protocolo de N4, §9)")
    c["configuracion_n6"] = cid
    if cid in SIN_CODIFICADOR:
        c["denso"] = {"requerido": False,
                      "nota": ("sin el codificador de consultas: esta configuración no sirve buscar_puntos, la única herramienta "
                               "que consulta el denso (familias_nav.Navegador.buscar_puntos); sus salidas dan iguales byte a byte "
                               "con y sin él (n6/comparar_tf1_sin_codificador.py)")}
    c["nota"] = (f"N6 de U-NAV-DISENO (protocolo de N4, f69e95ea, §2): la configuración {cid}. La de "
                 "mcp_kg/config_mcp_kg_nav_acumulado.json de HEAD con su lista de familias, servida por "
                 "mcp_kg/servidor_mcp_kg_nav_cand.py, que suma ver_descendientes a la familia 2. Con la lista vacía (B) "
                 "sirve solo las tres herramientas de hoy y no abre el navegador ni el denso.")
    return c


def mcp_json(cid: str) -> dict:
    m = json.loads(MCP_NAV.read_text(encoding="utf-8"))
    s = m["mcpServers"]["kg"]
    s["args"] = ["-B", "${BANCO_REPO}/data/experiment/banco_mcp/mcp_kg/servidor_mcp_kg_nav_cand.py",
                 "--config", f"${{BANCO_REPO}}/data/experiment/banco_mcp/n6/config_mcp_kg_n6_{cid}.json"]
    return m


def config_agentes(sha_plantilla: str) -> dict:
    a22 = json.loads(leer(CONFIG_A22, "config_agentes_a2_2"))
    brazos = {}
    for cid, fams, bl in CONFIGURACIONES:
        brazos[brazo_kg(cid)] = {
            "configuracion_n6": cid, "familias": list(fams), "carga_codificador": carga_codificador(cid, fams),
            "mcp_config": f"n6/mcp_kg_n6_{cid}.json", "servidor": "kg",
            "bloque_tools": f"n6/bloque_tools_kg_n6_{bl}.txt", "allowed_tools": "mcp__kg__*",
            "tools_esperadas": sorted(f"mcp__kg__{h}" for h in herramientas(fams)),
            "tools_esperadas_nota": "en el orden en que las lista el CLI en system/init (alfabético), porque armar_meta compara las listas",
            "config_servidor": f"n6/config_mcp_kg_n6_{cid}.json", "archivos_servidor": ARCHIVOS_SERVIDOR_KG,
            "venv": "el .venv del repo para el servidor (lo fija el JSON de MCP) y BANCO_VENV_VECTOR para su codificador de consultas"}
    for cid, nombre, mcp, bloque, cfg in (
            ("F1_bm25", "fragmentos_bm25", "mcp_vector/mcp_fragmentos_bm25_acumulado.json",
             "a2_1/bloque_tools_fragmentos_bm25.txt", "mcp_vector/config_fragmentos_bm25_acumulado_r2b.json"),
            ("F1_hibrida", "fragmentos_hibrida", "mcp_vector/mcp_fragmentos_hibrida_acumulado.json",
             "a2_1/bloque_tools_fragmentos_hibrida.txt", "mcp_vector/config_fragmentos_hibrida_acumulado_r2b.json")):
        brazos[nombre] = {"configuracion_n6": cid, "carga_codificador": cid == "F1_hibrida", "mcp_config": mcp,
                          "servidor": "fragmentos", "bloque_tools": bloque,
                          "allowed_tools": "mcp__fragmentos__*", "tools_esperadas": ["mcp__fragmentos__buscar_pasajes"],
                          "config_servidor": cfg,
                          "archivos_servidor": ["mcp_vector/servidor_mcp_vector.py", "mcp_vector/bm25_fragmentos.py"],
                          "venv": "BANCO_VENV_VECTOR"}
    corte = a22["corte_R5"]
    return {
        "unidad": "U-NAV-DISENO, N6 — configuración de los agentes de las 8 configuraciones del grafo y las 2 de F1 "
                  "(protocolo de N4, sellado en f69e95ea, §1, §2 y §6)",
        "por_que": ("N6 mide las ablaciones de la navegación con el agente del banco y el R5 de A2.2. La forma es la de "
                    "paralelo/config_agentes_n6_prueba.json: un brazo por configuración. Lo arma "
                    "n6/armar_configuraciones_n6.py desde archivos de HEAD que no se editan."),
        "base": {"ruta": "a2_2/config_agentes_a2_2.json", "sha256": SHA["config_agentes_a2_2"],
                 "que_se_hereda": ("modelo, modo del harness, versión sellada del CLI, flags y R5 (30, 32 y 1,80): los de "
                                   "A2.2 (N4, §1). Lo que cambia: los brazos (las 8 configuraciones del grafo con el "
                                   "servidor nuevo y las 2 de F1 sobre el acumulado) y la plantilla (la de A2.2 con la "
                                   "parte común de la decisión 9).")},
        "claude_code_version_sellada": a22["claude_code_version_sellada"], "modelo": a22["modelo"],
        "modo_harness": a22["modo_harness"], "brazos": brazos,
        "prompt": {"plantilla": "n6/plantilla_prompt_n6.txt", "sha256": sha_plantilla,
                   "como_se_pasa": a22["prompt"]["como_se_pasa"],
                   "diferencia_entre_brazos": "exclusivamente el bloque {{BLOQUE_TOOLS}}: la plantilla es la misma en las 10"},
        "corte_R5": {"max_turns": corte["max_turns"], "tope_tool_calls_en_prompt": corte["tope_tool_calls_en_prompt"],
                     "max_budget_usd_por_sesion": corte["max_budget_usd_por_sesion"],
                     "nota": "R5 de A2.2 (N4, §1 y §8, punto 1), igual en todas las sesiones de N6."},
        "R5": {"tope_tool_calls_prompt": corte["tope_tool_calls_en_prompt"], "max_turns": corte["max_turns"],
               "max_budget_usd": corte["max_budget_usd_por_sesion"]},
        "configuraciones_n6": {**{cid: {"brazo": brazo_kg(cid), "repeticiones": REPETICIONES.get(cid, 1), "familias": list(f),
                                        "bloque": f"n6/bloque_tools_kg_n6_{b}.txt", "carga_codificador": carga_codificador(cid, f)}
                                  for cid, f, b in CONFIGURACIONES},
                               "F1_bm25": {"brazo": "fragmentos_bm25", "repeticiones": REPETICIONES["F1_bm25"],
                                           "carga_codificador": False},
                               "F1_hibrida": {"brazo": "fragmentos_hibrida", "repeticiones": 1, "carga_codificador": True}},
        "carga_codificador_nota": ("si la sesión carga el modelo denso: el servidor del grafo con el denso (su codificador de "
                                   "consultas) o el de fragmentos de la híbrida. Ordena los dos lotes de N6 (decisión de la "
                                   "autora del 27/10/2026, puntos 1 y 8): no cambia lo que mide cada sesión."),
        "env_por_sesion": {
            "BANCO_REPO": "raíz del repo (expansión en los JSON de MCP)",
            "BANCO_VENV_VECTOR": "venv 3.12 del servidor de fragmentos; en todos los brazos (el del grafo lo usa para su codificador de consultas)",
            "BANCO_LOG_R1": "ruta del log R1 de ESA sesión (un archivo por sesión)",
            "BANCO_SESION_TAG": "id de la sesión (se copia a cada línea del log)",
            "NEO4J_URI": "pasa por la lista (§88) desde la terminal que lanza el lote: el Neo4j propio de N6 (bolt://127.0.0.1:57687)",
            "MCP_TIMEOUT": "180000"},
    }


def _json(d: dict) -> str:
    return json.dumps(d, ensure_ascii=False, indent=2) + "\n"


def armar() -> dict[str, str]:
    """{ruta relativa al banco: contenido} de todo lo que arma."""
    out = {}
    p = plantilla_n6()
    out["n6/plantilla_prompt_n6.txt"] = p
    for nombre, t in bloques().items():
        out[f"n6/bloque_tools_kg_n6_{nombre}.txt"] = t
    for cid, fams, _ in CONFIGURACIONES:
        out[f"n6/config_mcp_kg_n6_{cid}.json"] = _json(config_servidor(cid, fams))
        out[f"n6/mcp_kg_n6_{cid}.json"] = _json(mcp_json(cid))
    out["n6/config_agentes_n6.json"] = _json(config_agentes(sha256_bytes(p.encode("utf-8"))))
    return out


def controles(archivos: dict[str, str]) -> dict:
    bs = {k.split("bloque_tools_kg_n6_")[1][:-4]: v for k, v in archivos.items() if "bloque_tools_kg_n6_" in k}
    return {"plantilla": control_plantilla(archivos["n6/plantilla_prompt_n6.txt"]), "bloques": control_bloques(bs),
            "renglon_ver_descendientes": {"renglones": RENGLON_VER_DESCENDIENTES.count("\n"),
                                          "largos": [len(l) for l in RENGLON_VER_DESCENDIENTES.splitlines()],
                                          "sha256": sha256_bytes(RENGLON_VER_DESCENDIENTES.encode("utf-8"))},
            "archivos": {k: sha256_bytes(v.encode("utf-8")) for k, v in sorted(archivos.items())}}


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--verificar", action="store_true")
    ap.add_argument("--reescribir", action="store_true")
    ap.add_argument("--controles", type=Path, default=None, help="escribe en este JSON lo que se controló")
    a = ap.parse_args(argv)
    archivos = armar()
    c = controles(archivos)
    distintos = []
    for rel, txt in sorted(archivos.items()):
        p = BANCO_DIR / rel
        if a.verificar:
            if not p.is_file() or p.read_bytes() != txt.encode("utf-8"):
                distintos.append(rel)
        else:
            if p.exists() and p.read_bytes() != txt.encode("utf-8") and not a.reescribir:
                raise SystemExit(f"ABORTO: {rel} ya existe y difiere (--reescribir para pisarlo)")
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_bytes(txt.encode("utf-8"))
    if a.controles:
        a.controles.write_text(json.dumps(c, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    pl = c["plantilla"]
    print(f"archivos: {len(archivos)}; plantilla: nombres de los cinco TOs {pl['nombres_de_los_cinco_TOs']}, parte común "
          f"{'presente' if pl['parte_comun_presente'] else 'AUSENTE'}, la de HEAD con el renglón 1 de A2.2: "
          f"{pl['es_la_de_HEAD_con_el_renglon_1_de_A2_2']}")
    for rel, s in c["archivos"].items():
        print(f"{s}  {rel}")
    if a.verificar:
        print(f"verificación: {len(archivos) - len(distintos)} de {len(archivos)} iguales byte a byte; distintos: {distintos}")
        return 1 if distintos else 0
    ok = pl["nombres_de_los_cinco_TOs"] == 0 and pl["parte_comun_presente"] and pl["es_la_de_HEAD_con_el_renglon_1_de_A2_2"]
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
