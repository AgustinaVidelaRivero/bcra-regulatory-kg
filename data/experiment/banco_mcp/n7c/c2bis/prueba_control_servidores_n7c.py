"""N7c, C2-bis: la prueba de n7c/control_servidores_n7c.py contra el servidor de juguete (n7c/seco/servidor_mcp_juguete_n7c.py),
USD 0. Arma, en una carpeta de trabajo nueva, el índice de juguete, los tres JSON de MCP de juguete (una variante por
configuración, con el bloque `env` del JSON real de N7c) y una pregunta del humo sintética (su primera ancla, un punto del
juguete), y corre el control desde la copia (su main, con --mcp-N7, --mcp-N7c y --mcp-N7c-amp), sobre el Neo4j de B6.3 en
lectura (el control lo exige antes de levantar nada):
  P1 los tres en su lugar: código 0 y todos sus controles en verdadero;
  P2 N7c y N7c+ cruzados: código 1 (el prefijo de N7c en N7c+ no da);
  P3 N7 servido por la variante de N7c: código 1 (N7 trae la sección);
  P4 la pregunta del humo con otro sha256: código 8, sin levantar ningún servidor.
La guarda de otro paso pago corre con un token propio (PATRON_PAGO del módulo), como en el seco: ningún pgrep de esta prueba
lleva el patrón real.
Escribe un JSON con las cuentas y los veredictos (sin rutas) y lo imprime.
Uso: NEO4J_URI=bolt://127.0.0.1:47687 <python del .venv> -B prueba_control_servidores_n7c.py <raiz de la copia> <trabajo nuevo> <salida.json>
"""
import contextlib
import hashlib
import io
import json
import sys
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ, TRABAJO, SALIDA = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
BANCO = RAIZ / "data" / "experiment" / "banco_mcp"
if TRABAJO.exists():
    raise SystemExit("ABORTO: la carpeta de trabajo tiene que ser nueva")
for _p in (BANCO / "n7c", BANCO / "mcp_kg"):
    sys.path.insert(0, str(_p))
import control_servidores_n7c as CS  # noqa: E402
import selftest_familias_nav_rel_amp as ST  # noqa: E402

# La guarda de otro paso pago, con un token propio: ningún pgrep de esta prueba lleva el patrón real.
CS.C7.G.PATRON_PAGO = r"ensayoservidores[0-9]+x\.py"

idx = TRABAJO / "indice_juguete"
ST.indice_juguete(idx)
env_real = json.loads((BANCO / "n7c" / "mcp_kg_n7c_evaluado.json").read_text(encoding="utf-8"))["mcpServers"]["kg"]["env"]
mcp = {}
for v in ("N7", "N7c", "N7c_amp"):
    p = TRABAJO / f"mcp_juguete_{v}.json"
    p.write_text(json.dumps({"mcpServers": {"kg": {"type": "stdio", "command": sys.executable,
                                                   "args": ["-B", str(BANCO / "n7c" / "seco" / "servidor_mcp_juguete_n7c.py"),
                                                            "--variante", v, "--indice", str(idx)],
                                                   "env": env_real}}}, ensure_ascii=False), encoding="utf-8")
    mcp[v] = str(p)
humo = TRABAJO / "preguntas_humo_juguete.json"
humo.write_text(json.dumps({"preguntas": [{"id": "JUG-01", "gold": {"anclas": [{"to": "jug", "punto": "1.1."}]}}]}),
                encoding="utf-8")
sha_humo = hashlib.sha256(humo.read_bytes()).hexdigest()


def correr(nombre: str, n7: str, n7c: str, n7c_amp: str, sha: str = sha_humo) -> dict:
    sal = TRABAJO / nombre
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = CS.main(["--salida", str(sal), "--preguntas-humo", str(humo), "--sha256-preguntas-humo", sha,
                      "--mcp-N7", n7, "--mcp-N7c", n7c, "--mcp-N7c-amp", n7c_amp])
    r = json.loads((sal / "control_servidores_n7c.json").read_text(encoding="utf-8")) if (sal / "control_servidores_n7c.json").is_file() else {}
    return {"codigo": rc, "controles": r.get("controles"), "tamanos": r.get("tamanos"),
            "levanto_algo": any(sal.glob("log_r1_control_*.jsonl")) if sal.exists() else False,
            "neo4j_igual": r.get("neo4j_igual"), "repo_igual": r.get("repo_igual")}


res = {"P1": correr("P1", mcp["N7"], mcp["N7c"], mcp["N7c_amp"]),
       "P2": correr("P2", mcp["N7"], mcp["N7c_amp"], mcp["N7c"]),
       "P3": correr("P3", mcp["N7c"], mcp["N7c"], mcp["N7c_amp"]),
       "P4": correr("P4", mcp["N7"], mcp["N7c"], mcp["N7c_amp"], sha="0" * 64)}
res["veredictos"] = {
    "P1 los tres en su lugar: 0, todo en verdadero": res["P1"]["codigo"] == 0 and all(res["P1"]["controles"].values())
    and res["P1"]["neo4j_igual"] and res["P1"]["repo_igual"],
    "P2 N7c y N7c+ cruzados: 1": res["P2"]["codigo"] == 1 and not res["P2"]["controles"]["N7c_prefijo_de_N7c+"],
    "P3 N7 servido por la variante de N7c: 1": res["P3"]["codigo"] == 1 and not res["P3"]["controles"]["N7_sin_las_tres_marcas"],
    "P4 la pregunta del humo con otro sha256: 8, sin levantar nada": res["P4"]["codigo"] == 8 and not res["P4"]["levanto_algo"]}
res["ok"] = all(res["veredictos"].values())
Path(SALIDA).write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res["veredictos"], ensure_ascii=False), "ok:", res["ok"])
raise SystemExit(0 if res["ok"] else 1)
