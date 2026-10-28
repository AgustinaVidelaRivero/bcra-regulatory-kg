"""armar_n7_v3_mesa.py — mesa, §312 (27/10/2026; la de la §299 con la elección sobre las 26 de la decisión 9): N7 de U-NAV-DISENO, el pre-registro de la configuración elegida, armado desde el análisis
sellado de N6. USD 0: no llama a ningún modelo ni levanta nada; lee el JSON del análisis de N6 (analizar_n6.py), los archivos de N6 y
las configs del grafo evaluado de HEAD (218, 6b3dd5ab), y escribe la configuración sellada de cada brazo de B6.3 en una carpeta nueva.

Lo que hace, en orden; si algo no da, frena con su código y no escribe nada:
  1. la regla de N4, §5, otra vez, sobre los agregados del análisis (la fidelidad, la elegibilidad de cada «T−Fk», V, las veces al
     tope y el R9 medio): las candidatas, las que quedan dentro de V y el desempate. Si la elección del análisis va sobre las 26 sin
     FUERA_D9 (la decisión 9, su «sobre»), usa la fidelidad sin FUERA_D9, V(26) y, para el desempate, las veces al tope y el R9 medio
     sobre las 26 que la elección trae de las que quedan dentro de V; si no, la fidelidad sobre las 30, V(30) y lo operativo de las 30. Tiene que dar la misma elegida que
     el análisis (10 si no). Con `--eleccion` se lee la elección que corresponda (la principal de la decisión 5 de las 12:09:14 sale de la
     etapa a bis de N6, con el nombre de clave que fije su FRENO);
  2. el requisito de la jerarquía: si el análisis dice que la elegida no se pre-registra así, vuelve a la autora (11);
  3. F1 (N4, §6): BM25 o la híbrida como principal del brazo de fragmentos, según `entra_la_hibrida` (12 si no está decidido);
  4. R5 (pre-registro de B6.3, §5): si más del 5 % de las sesiones de N6 de la configuración elegida de cualquiera de los dos brazos
     llegó al tope (30 llamadas o más en el log R1, o cortada por R5), el tope sube en los dos a 45, 47 y 3,30; si no, queda en 30, 32 y
     1,80. «Si en N7 más del 5 %…», leído sobre las sesiones de N6 de lo elegido en cada brazo: lo confirmó la autora el 27/10/2026
     (recibido a las 15:04:04);
  5. el brazo del grafo sobre el grafo evaluado: la config del evaluado de HEAD con las familias, la firma de herramientas, el denso y la
     versión del servidor de la elegida en N6; su JSON de MCP con el servidor nuevo (servidor_mcp_kg_nav_cand.py, como en N6); su bloque
     y la plantilla de N6, byte a byte;
  6. el brazo de fragmentos: la principal y el denso, por las configs del evaluado de HEAD, y su bloque de N6 (el de la config de
     agentes de N6, como el del grafo: T−F6 usa el de B);
  7. los ejemplos de la familia 6: si la elegida los lleva (T y T−F1 a T−F5), el brazo de fragmentos lleva los mismos 3 resueltos con su
     herramienta (U-NAV, :190-193). La autora decidió cómo (15:04:04): las mismas 3 preguntas, con las salidas reales de su herramienta
     sobre el grafo evaluado y la forma de los del grafo, armadas por una unidad a USD 0 y aprobadas por ella antes de sellar N7. Queda
     PENDIENTE, nombrado en la salida, hasta esa aprobación;
  8. el registro (n7_configuracion_sellada.json): cada archivo con su ruta y su sha256, las reglas aplicadas y lo pendiente.
Imprime solo nombres de configuraciones, cuentas, sha256 y veredictos.
  python3 -I -B armar_n7_mesa.py --analisis <analisis_n6.json> --n6 <carpeta n6 de N6> --banco <banco_mcp de HEAD o de su copia>
         --config-agentes <n6/config_agentes_n6.json> --salida <carpeta nueva> [--eleccion regla.eleccion]
"""
import argparse
import hashlib
import json
import sys
from pathlib import Path

CANDIDATAS = ("B", "T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5", "T-F6")
CON_EJEMPLOS_F6 = ("T", "T-F1", "T-F2", "T-F3", "T-F4", "T-F5")
R5_BASE = {"tope_tool_calls_prompt": 30, "max_turns": 32, "max_budget_usd": 1.80}
R5_SUBIDO = {"tope_tool_calls_prompt": 45, "max_turns": 47, "max_budget_usd": 3.30}
UMBRAL_TOPE = 0.05
EVALUADO = {"kg": "mcp_kg/config_mcp_kg_nav_evaluado.json", "bm25": "mcp_vector/config_fragmentos_bm25_evaluado_r2b.json",
            "hibrida": "mcp_vector/config_fragmentos_hibrida_evaluado_r2b.json", "denso": "mcp_vector/config_fragmentos_denso_evaluado_r2b.json"}
MCP_FRAG = {"bm25": "mcp_vector/mcp_fragmentos_bm25_evaluado.json", "hibrida": "mcp_vector/mcp_fragmentos_hibrida_evaluado.json",
            "denso": "mcp_vector/mcp_fragmentos_denso_evaluado.json"}
SERVIDOR_N6 = "data/experiment/banco_mcp/mcp_kg/servidor_mcp_kg_nav_cand.py"
EPS = 1e-12


class Freno(Exception):
    def __init__(self, codigo, motivo):
        super().__init__(motivo)
        self.codigo, self.motivo = codigo, motivo


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def leer_clave(d: dict, ruta: str):
    for k in ruta.split("."):
        if not isinstance(d, dict) or k not in d:
            raise Freno(13, f"el análisis no trae «{ruta}»")
        d = d[k]
    return d


def regla_otra_vez(a: dict, clave_regla: str, el: dict) -> dict:
    """La regla de N4, §5, sobre los agregados del análisis: candidatas, dentro de V y el desempate (al tope, R9, fidelidad, nombre).
    Con la decisión 9 (la elección «sobre» las 26 sin FUERA_D9): la fidelidad sin FUERA_D9, V(26) y lo operativo de las 26 que trae
    la elección; si no, la fidelidad sobre las 30, V(30) y lo operativo de las 30."""
    r = leer_clave(a, clave_regla)
    d9 = "FUERA_D9" in str(el.get("sobre") or "")
    fid = r["fidelidad_sin_FUERA_D9"] if d9 else r["fidelidad_30"]
    v = ((r["V_sin_FUERA_D9"] if d9 else r["V"])["30"]["V"] or 0.0)
    fam = r["familias"]
    cands = [c for c in CANDIDATAS if fid.get(c) is not None and (c in ("B", "T") or fam[c]["elegible"])]
    if not cands:
        raise Freno(10, "ninguna candidata con fidelidad")
    mejor = max(fid[c] for c in cands)
    dentro = [c for c in cands if fid[c] >= mejor - v - EPS]
    if d9:
        at, r9 = el.get("al_tope") or {}, el.get("r9_medio_por_pregunta_usd") or {}
        if set(at) != set(dentro) or set(r9) != set(dentro):
            raise Freno(10, f"la elección sobre las 26 no trae lo operativo de las que quedan dentro de V: {sorted(dentro)}")
        ops = {c: {"al_tope": at[c], "r9_medio_por_pregunta_usd": r9[c]} for c in dentro}
    else:
        ops = {c: a["medidas"][c]["operativo"] for c in CANDIDATAS}
    orden = sorted(dentro, key=lambda c: (ops[c]["al_tope"], ops[c]["r9_medio_por_pregunta_usd"] or 0.0, -fid[c], c))
    return {"sobre": "las 26 sin FUERA_D9 (decisión 9)" if d9 else "las 30", "candidatas": cands, "dentro_de_V": dentro,
            "orden_de_desempate": orden, "elegida": orden[0], "V": v, "fidelidad_elegida": fid[orden[0]]}


def armar(args) -> dict:
    a = json.loads(Path(args.analisis).read_text(encoding="utf-8"))
    clave_regla = args.eleccion.rsplit(".", 1)[0]
    el = leer_clave(a, args.eleccion)
    otra = regla_otra_vez(a, clave_regla, el or {})
    if el is None or el.get("elegida") != otra["elegida"] or el.get("orden_de_desempate") != otra["orden_de_desempate"] \
            or el.get("candidatas") != otra["candidatas"] or el.get("dentro_de_V") != otra["dentro_de_V"]:
        raise Freno(10, f"la regla otra vez da {otra['elegida']} y el análisis {None if el is None else el.get('elegida')}")
    X = otra["elegida"]
    if not el.get("se_preregistra_asi"):
        raise Freno(11, f"la elegida ({X}) no pasa el requisito de la jerarquía: vuelve a la autora")
    f1 = leer_clave(a, f"{clave_regla}.F1")
    if f1.get("entra_la_hibrida") is None:
        raise Freno(12, "F1 no está decidido (falta una fidelidad o la variación de BM25)")
    principal = "hibrida" if f1["entra_la_hibrida"] else "bm25"
    conf_frag = "F1_hibrida" if principal == "hibrida" else "F1_bm25"
    # R5, con las sesiones de N6 de lo elegido en cada brazo
    tope = {}
    for c in (X, conf_frag):
        op = a["medidas"][c]["operativo"]
        tope[c] = {"al_tope": op["al_tope"], "sesiones": op["sesiones"],
                   "fraccion": round(op["al_tope"] / op["sesiones"], 6) if op["sesiones"] else None}
    sube = any(t["fraccion"] is not None and t["fraccion"] > UMBRAL_TOPE + EPS for t in tope.values())
    r5 = dict(R5_SUBIDO if sube else R5_BASE)
    n6, banco, sal = Path(args.n6), Path(args.banco), Path(args.salida)
    if sal.exists():
        raise Freno(14, "la carpeta de salida ya existe")
    cfg_n6 = json.loads((n6 / f"config_mcp_kg_n6_{X}.json").read_text(encoding="utf-8"))
    ev = json.loads((banco / EVALUADO["kg"]).read_text(encoding="utf-8"))
    cfg = dict(ev)
    for k in ("version", "familias", "firma_tools", "denso"):
        if k in cfg_n6:
            cfg[k] = cfg_n6[k]
        elif k in cfg:
            del cfg[k]
    cfg["configuracion_n7"] = X
    cfg["nota"] = (f"N7 de U-NAV-DISENO: la configuración elegida en N6 ({X}) sobre el grafo evaluado de B6.3. La config del evaluado de "
                   f"HEAD ({EVALUADO['kg']}) con las familias, la firma de las herramientas, el denso y la versión del servidor de "
                   f"n6/config_mcp_kg_n6_{X}.json; la sirve servidor_mcp_kg_nav_cand.py, como en N6.")
    mcp = json.loads((banco / "mcp_kg" / "mcp_kg_nav_evaluado.json").read_text(encoding="utf-8"))
    kg = mcp["mcpServers"]["kg"]
    kg["args"] = ["-B", "${BANCO_REPO}/" + SERVIDOR_N6, "--config", "${BANCO_REPO}/data/experiment/banco_mcp/n7/config_mcp_kg_n7_evaluado.json"]
    agentes = json.loads(Path(args.config_agentes).read_text(encoding="utf-8"))
    tools_x = bloque_x = bloque_frag = None
    carga = bool(cfg.get("familias")) and bool((cfg.get("denso") or {}).get("requerido"))
    if True:
        for b in agentes["brazos"].values():
            if b.get("configuracion_n6") == X:
                tools_x, bloque_x = b.get("tools_esperadas"), b.get("bloque_tools")
                if b.get("carga_codificador") is not None and b["carga_codificador"] != carga:
                    raise Freno(15, f"la config de agentes de N6 dice que {X} carga el codificador: {b['carga_codificador']}; su config, {carga}")
            if b.get("configuracion_n6") == conf_frag:
                bloque_frag = b.get("bloque_tools")
    if not bloque_x or not bloque_frag:
        raise Freno(16, f"la config de agentes de N6 no trae el bloque de {X} o de {conf_frag}")
    archivos = {
        "config_mcp_kg_n7_evaluado.json": (json.dumps(cfg, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        "mcp_kg_n7_evaluado.json": (json.dumps(mcp, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
        "bloque_tools_kg_n7.txt": (banco / bloque_x).read_bytes(),
        "bloque_tools_fragmentos_n7.txt": (banco / bloque_frag).read_bytes(),
        "plantilla_prompt_n7.txt": (n6 / "plantilla_prompt_n6.txt").read_bytes(),
    }
    pendiente = []
    if X in CON_EJEMPLOS_F6:
        pendiente.append({"que": "los 3 ejemplos de la familia 6 en el brazo de fragmentos, resueltos con su herramienta (U-NAV, :190-193)",
                          "por": f"la elegida, {X}, los lleva: los arma la unidad de los ejemplos de fragmentos y los aprueba la autora "
                                 "antes de sellar N7"})
    registro = {
        "unidad": "U-NAV-DISENO, N7: la configuración sellada de cada brazo de B6.3",
        "analisis_n6": {"ruta": str(args.analisis_rel or Path(args.analisis).name), "sha256": sha(Path(args.analisis).read_bytes()),
                        "eleccion": args.eleccion},
        "regla_N4_5": {"del_analisis": {k: el.get(k) for k in ("sobre", "candidatas", "dentro_de_V", "orden_de_desempate", "elegida")},
                       "otra_vez": otra, "iguales": True, "requisito_jerarquia": el.get("caso_de_la_jerarquia")},
        "F1": {"entra_la_hibrida": f1["entra_la_hibrida"], "principal_de_fragmentos": principal},
        "R5": {"regla": "más del 5 % de las sesiones de N6 de lo elegido en cualquiera de los dos brazos, al tope: sube a 45, 47 y 3,30 "
                        "(confirmada por la autora el 27/10/2026, 15:04:04)",
               "por_brazo": tope, "sube": sube, "valores": r5},
        "brazo_grafo": {"configuracion_n6": X, "familias": cfg.get("familias"), "carga_el_codificador": carga,
                        "herramientas_esperadas": tools_x, "servidor": SERVIDOR_N6,
                        "indice_puntos": {"ruta": cfg["indice_puntos"], "sha256_manifiesto": cfg["sha256_manifiesto_indice"]},
                        "hubs_esperados": cfg.get("hubs_esperados"), "grafo": cfg["grafo"], "kg_sha256": cfg["kg_sha256_esperado"],
                        "archivos": {k: sha(v) for k, v in archivos.items()}},
        "brazo_fragmentos": {"principal": {"afinidad": principal, "config": EVALUADO[principal],
                                           "sha256": sha((banco / EVALUADO[principal]).read_bytes()), "mcp": MCP_FRAG[principal],
                                           "sha256_mcp": sha((banco / MCP_FRAG[principal]).read_bytes())},
                             "denso": {"config": EVALUADO["denso"], "sha256": sha((banco / EVALUADO["denso"]).read_bytes()),
                                       "mcp": MCP_FRAG["denso"], "sha256_mcp": sha((banco / MCP_FRAG["denso"]).read_bytes())},
                             "bloque_tools_de_N6": bloque_frag, "configuracion_n6": conf_frag},
        "bloques_de_N6": {"grafo": bloque_x, "fragmentos": bloque_frag},
        "plantilla": {"de_N6": "n6/plantilla_prompt_n6.txt", "sha256": sha(archivos["plantilla_prompt_n7.txt"])},
        "pendiente": pendiente,
    }
    sal.mkdir(parents=True)
    for k, v in archivos.items():
        (sal / k).write_bytes(v)
    (sal / "n7_configuracion_sellada.json").write_text(json.dumps(registro, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return registro


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--analisis", required=True)
    ap.add_argument("--analisis-rel", default=None, help="la ruta del análisis que va al registro (desde la raíz del repo)")
    ap.add_argument("--n6", required=True)
    ap.add_argument("--banco", required=True)
    ap.add_argument("--salida", required=True)
    ap.add_argument("--eleccion", default="regla.eleccion")
    ap.add_argument("--config-agentes", required=True)
    args = ap.parse_args(argv)
    try:
        r = armar(args)
    except Freno as f:
        print(f"FRENO {f.codigo}: {f.motivo}")
        return f.codigo
    print(f"N7: elegida {r['brazo_grafo']['configuracion_n6']} (familias {r['brazo_grafo']['familias']}, carga el codificador "
          f"{r['brazo_grafo']['carga_el_codificador']}); fragmentos con {r['F1']['principal_de_fragmentos']}; R5 {r['R5']['valores']} "
          f"(sube: {r['R5']['sube']}); pendiente: {len(r['pendiente'])}; registro {sha((Path(args.salida) / 'n7_configuracion_sellada.json').read_bytes())[:16]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
