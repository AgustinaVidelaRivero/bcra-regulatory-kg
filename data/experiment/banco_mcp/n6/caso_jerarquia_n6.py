#!/usr/bin/env python3
"""caso_jerarquia_n6.py — N6 de U-NAV-DISENO: el caso obligatorio de la jerarquía (protocolo de N4, sellado en f69e95ea, §5),
sin modelo (USD 0), con las herramientas de la configuración T por el servidor nuevo (servidor_mcp_kg_nav_cand.py, por stdio
con banco_mcp/cliente_falso.py), sobre el Neo4j propio de N6.

En el acumulado, la Definicion de cla::5.1.1 y la Excepcion de cla::5.1.1.1 están a 2 aristas solo pasando por un hub, y sin
hubs no se conectan. El caso pide que, con las herramientas de la configuración, desde la Definicion se llegue a la Excepcion
en 2 llamadas como mucho. El camino, el del T8 de selftest_familias_nav.py:
  1. ver_punto del punto de la Definicion (cla::5.1.1): la salida muestra la Definicion y lista el hijo 5.1.1.1;
  2. ver_punto de cla::5.1.1.1: la salida muestra cada Excepcion del hijo.
Informativo: ver_descendientes de cla::5.1.1 con niveles 1 muestra el texto del hijo en una llamada (sin sus nodos); y, por
configuración, si tiene ver_punto (el camino de arriba).
Imprime los ids de los nodos del caso solo si son de la tanda 0 (cegamiento, mandato, §7, regla 5); las salidas, por sha256.
Uso: NEO4J_URI=bolt://127.0.0.1:57687 BANCO_VENV_VECTOR=<venv> python -B n6/caso_jerarquia_n6.py --salida <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
BANCO_DIR = AQUI.parent
MCP_KG = BANCO_DIR / "mcp_kg"
for _p in (str(BANCO_DIR), str(MCP_KG)):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import servidor_mcp_kg_nav_cand as CAND  # noqa: E402
from cliente_falso import ClienteFalso  # noqa: E402

NEO4J_URI_N6 = "bolt://127.0.0.1:57687"
CONFIG_T = AQUI / "config_mcp_kg_n6_T.json"
CONFIG_AGENTES = AQUI / "config_agentes_n6.json"
PUNTO, HIJO = "cla::5.1.1", "cla::5.1.1.1"


def sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args(argv)
    if os.environ.get("NEO4J_URI") != NEO4J_URI_N6:
        raise SystemExit(f"FRENO: NEO4J_URI no es la del Neo4j propio de N6 ({NEO4J_URI_N6})")
    cfg = json.loads(CONFIG_T.read_text(encoding="utf-8"))
    idx = json.loads((MCP_KG / cfg["indice_puntos"] / "puntos.json").read_text(encoding="utf-8"))
    nodos = json.loads((MCP_KG / cfg["indice_puntos"] / "nodos.json").read_text(encoding="utf-8"))
    defi = [n for n in idx[PUNTO]["nodos"] if nodos[n]["type"] == "Definicion"]
    exc = [n for n in idx[HIJO]["nodos"] if nodos[n]["type"] == "Excepcion"]
    if not defi or not exc:
        raise SystemExit("FRENO: el grafo no trae los nodos del caso")
    tanda1 = {n for n in defi + exc if any(p.split("::", 1)[0] not in ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob",
                                                                          "polcre", "pagjub", "docvig")
                                           for p in nodos[n].get("puntos") or [])}
    env = {k: v for k, v in os.environ.items() if k in ("NEO4J_URI", "BANCO_VENV_VECTOR", "PATH", "HOME", "TMPDIR")}
    env.update({"PYTHONDONTWRITEBYTECODE": "1", "BANCO_LOG_R1": os.devnull, "BANCO_SESION_TAG": "caso_jerarquia_n6",
                "HF_HUB_OFFLINE": "1", "TRANSFORMERS_OFFLINE": "1"})
    cmd = [sys.executable, "-B", str(MCP_KG / "servidor_mcp_kg_nav_cand.py"), "--config", str(CONFIG_T)]
    with ClienteFalso(cmd=cmd, env=env, cwd=BANCO_DIR.parents[2]) as cli:
        herramientas = [t["name"] for t in cli.listar_tools()]
        punto_defi = nodos[defi[0]]["puntos"][0]
        o1 = cli.llamar("ver_punto", {"punto": punto_defi})
        o2 = cli.llamar("ver_punto", {"punto": HIJO})
        o3 = cli.llamar("ver_descendientes", {"punto": PUNTO, "niveles": 1})
    paso1 = {"llamada": f"ver_punto(punto=«{punto_defi}»)", "muestra_la_definicion": defi[0] in o1,
             "lista_el_hijo_5.1.1.1": "5.1.1.1 · " in o1, "sha256_salida": sha(o1), "caracteres": len(o1)}
    paso2 = {"llamada": f"ver_punto(punto=«{HIJO}»)", "muestra_cada_excepcion": all(e in o2 for e in exc),
             "excepciones": len(exc), "sha256_salida": sha(o2), "caracteres": len(o2)}
    llega = paso1["muestra_la_definicion"] and paso1["lista_el_hijo_5.1.1.1"] and paso2["muestra_cada_excepcion"]
    ca = json.loads(CONFIG_AGENTES.read_text(encoding="utf-8"))
    por_conf = {b["configuracion_n6"]: {"tiene_ver_punto": "mcp__kg__ver_punto" in b["tools_esperadas"]}
                for b in ca["brazos"].values() if b.get("servidor") == "kg"}
    out = {"caso": "N4, §5: desde la Definicion de cla::5.1.1 a la Excepcion de cla::5.1.1.1, en 2 llamadas como mucho",
           "configuracion": "T", "servidor": "mcp_kg/servidor_mcp_kg_nav_cand.py", "config": "n6/config_mcp_kg_n6_T.json",
           "herramientas_de_T": herramientas,
           "definicion": defi[0] if defi[0] not in tanda1 else "(tanda 1, cegado)",
           "excepciones": [e if e not in tanda1 else "(tanda 1, cegado)" for e in exc],
           "nodos_del_caso_de_la_tanda_1": len(tanda1),
           "camino": [paso1, paso2], "llamadas": 2, "llega_en_2_llamadas_o_menos": llega,
           "informativo_ver_descendientes": {"llamada": f"ver_descendientes(punto=«{PUNTO}», niveles=1)",
                                             "muestra_el_hijo_5.1.1.1": "5.1.1.1" in o3, "sha256_salida": sha(o3)},
           "informativo_por_configuracion": por_conf}
    a.salida.parent.mkdir(parents=True, exist_ok=True)
    a.salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"caso de la jerarquía con T: {'llega' if llega else 'NO llega'} en 2 llamadas "
          f"(definición mostrada {paso1['muestra_la_definicion']}, hijo listado {paso1['lista_el_hijo_5.1.1.1']}, "
          f"{len(exc)} excepciones mostradas {paso2['muestra_cada_excepcion']}); configuraciones con ver_punto: "
          f"{sorted(k for k, v in por_conf.items() if v['tiene_ver_punto'])}")
    return 0 if llega else 1


if __name__ == "__main__":
    raise SystemExit(main())
