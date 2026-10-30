"""N7c, C2, paso 2: la prueba, a USD 0, de que el lanzador de una sesión de N6 no recibe la configuración de agentes de la
entrada. Corre sobre la copia de trabajo, sin lanzar nada: el `subprocess.Popen` del lote, `preparar_sesion` y el `lanzar`
de lanzar_agente_n6 quedan reemplazados por registradores en memoria, que frenan si alguien los llama de más.

  1. el comando que arma `lanzar_lote_paralelo.Lote.lanzar` para una sesión, con el lanzador `n6/lanzar_agente_n6.py` y el
     `config_agentes` de la entrada en el lote (`a.config_agentes`, como lo pasa correr_n6.py:722): si trae `--config-agentes`;
  2. ese comando, leído por el `main` de lanzar_agente_n6 (su argparse, sin lanzar): la configuración que usaría la sesión;
     y, como control positivo, el mismo comando con `--config-agentes` agregado: la configuración pasa a ser la de la opción;
  3. `lanzar_agente_n6_prueba.lanzar` con esa configuración y el brazo `kg_N7c`: dónde termina (antes de preparar la sesión).
Imprime solo booleanos y rutas relativas al banco. Uso: python3 -I -B prueba_lanzador_sin_config.py <raiz de la copia>
<carpeta de trabajo nueva> <salida.json>
"""
import json
import sys
import types
from pathlib import Path

RAIZ, TRABAJO, SALIDA = (Path(x).resolve() for x in sys.argv[1:4])
BANCO = RAIZ / "data" / "experiment" / "banco_mcp"
for _p in (BANCO, BANCO / "agentes", BANCO / "paralelo", BANCO / "a2_1", BANCO / "n6"):
    sys.path.insert(0, str(_p))
if TRABAJO.exists():
    raise SystemExit("FRENO: la carpeta de trabajo tiene que ser nueva")
TRABAJO.mkdir(parents=True)

import lanzar_lote_paralelo as BASE      # noqa: E402
import lanzar_agente_n6 as LN6           # noqa: E402
import lanzar_agente_n6_prueba as LP     # noqa: E402

res = {"modulos_de_la_copia": all(Path(m.__file__).resolve().is_relative_to(RAIZ) for m in (BASE, LN6, LP))}


class PopenRegistrador:
    llamadas: list = []

    def __init__(self, cmd, **kw):
        PopenRegistrador.llamadas.append(list(cmd))
        self.pid = 0


BASE.subprocess = types.SimpleNamespace(Popen=PopenRegistrador, DEVNULL=None)
lanzador = BANCO / "n6" / "lanzar_agente_n6.py"
a = types.SimpleNamespace(modo="real", via="api", timeout_s=1800.0, config_agentes="n7c/config_agentes_n7c.json")
lote = types.SimpleNamespace(a=a, out=TRABAJO / "agente", raiz=TRABAJO / "sesiones", lanzador=lanzador, abiertos={})
BASE.Lote.lanzar(lote, {"id": "PRUEBA-1", "brazo": "kg_N7c"}, "consulta sintética de la prueba", 1)
for fo, fe in lote.abiertos.values():
    fo.close()
    fe.close()
cmd = PopenRegistrador.llamadas[0]
res["1_un_comando"] = len(PopenRegistrador.llamadas) == 1
res["1_lanzador_del_comando"] = str(Path(cmd[2]).relative_to(BANCO))
res["1_opciones_del_comando"] = [x for x in cmd if x.startswith("--")]
res["1_trae_config_agentes"] = "--config-agentes" in cmd

capturado = {}


def lanzar_registrador(brazo, pid, pregunta, out, modo, via, cwd, timeout_s, sesiones, ruta_cfg):
    capturado["ruta_cfg"] = Path(ruta_cfg)
    return {"configuracion_n6": None, "inventario_tools_R6": {"coincide": None}, "completitud_R3": {"completa": None},
            "tokens_R9": {"costo_recomputado": {"total_usd": 0.0}}, "duracion_s": 0.0}


lanzar_real = LN6.lanzar
LN6.lanzar = lanzar_registrador
sys.argv = cmd[2:]
LN6.main()
cfg_usada = capturado["ruta_cfg"].resolve()
# Control positivo: el mismo comando con `--config-agentes` (lo que el lote no agrega) sí cambia la configuración.
sys.argv = cmd[2:] + ["--config-agentes", str(BANCO / "n7c" / "config_agentes_n7c.json")]
LN6.main()
LN6.lanzar = lanzar_real
res["2_control_positivo_con_la_opcion"] = str(capturado["ruta_cfg"].resolve().relative_to(BANCO))
res["2_config_que_usaria_la_sesion"] = str(cfg_usada.relative_to(BANCO))
res["2_es_la_de_n6"] = cfg_usada == (BANCO / "n6" / "config_agentes_n6.json").resolve()
brazos = json.loads(cfg_usada.read_text(encoding="utf-8"))["brazos"]
res["2_brazos_kg_N7_y_kg_N7c_en_esa_config"] = {b: b in brazos for b in ("kg_N7", "kg_N7c")}


def no_llamar(*_a, **_k):
    raise AssertionError("se llamó a algo que prepara o lanza una sesión")


LP.LA.preparar_sesion = no_llamar
LP.subprocess = types.SimpleNamespace(Popen=no_llamar, run=no_llamar)
try:
    LP.lanzar("kg_N7c", "PRUEBA-1", "consulta sintética de la prueba", TRABAJO / "no_se_usa", "real", "api", None, 1800.0,
              TRABAJO / "sesiones", cfg_usada)
    res["3_lanzar"] = "terminó sin frenar"
except SystemExit as x:
    res["3_lanzar"] = f"SystemExit: {x}"
except AssertionError as x:
    res["3_lanzar"] = f"AssertionError: {x}"
res["3_frena_antes_de_preparar_la_sesion"] = res["3_lanzar"] == "SystemExit: brazo desconocido: kg_N7c"
res["prueba_ok"] = (res["modulos_de_la_copia"] and res["1_un_comando"] and not res["1_trae_config_agentes"]
                    and res["2_es_la_de_n6"] and res["2_control_positivo_con_la_opcion"] == "n7c/config_agentes_n7c.json"
                    and not any(res["2_brazos_kg_N7_y_kg_N7c_en_esa_config"].values())
                    and res["3_frena_antes_de_preparar_la_sesion"])
SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
