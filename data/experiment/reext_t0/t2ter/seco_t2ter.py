"""Corrida en seco de T2-ter de U-REEXT-T0 (copia adaptada de t2bis/seco_t2bis.py; USD 0, sin red), sobre una COPIA del repo sin .env.

Ejercita el mismo camino que la corrida real (CLAUDE.md §4, regla l, nota del 06/10/2026): importa el runner de la
copia desde su archivo, sin tocar el sys.path por fuera (el runner arma el suyo), y llama a main() con el comando de
T2-ter: E1 tiene que salir entera de la caché (0 pedidos de E1 al SDK) y E3 verificar las dos unidades reparadas. Lo único que se reemplaza es el cliente del SDK (anthropic.Anthropic): un cliente falso que devuelve un
Message con un tool_use mínimo y registra cada pedido que le llega, es decir, cada fallo de la caché local. Los
aciertos de la caché salen de las bases copiadas, como en la corrida real. La red queda bloqueada (socket.connect) y la
clave del entorno es una cadena de prueba.

Variantes (marcas separadas por «+»):
  tal_cual       el runner como queda con los puntos a, b y c; el cliente falso nunca corta.
  sin_e2_v3      cerrar_e2 (E2 del perfil de E1) reemplazado por un no-op, para ver el resto del camino
                 (cerrar_e2_r2) si cerrar_e2 se detiene.
  cortes_partes  el pedido de E1 de una parte corta en 8.192 y en 16.384, y el tercer escalón (40.960, por
                 transmisión) responde: la rama que la razón p90 de T2 hace probable para las dos partes.

Uso: python -B seco_t2ter.py <copia> <variante> <salida_json>
"""
import json
import os
import re
import socket
import sys
import importlib.util
from pathlib import Path

COPIA = Path(sys.argv[1]).resolve()
VARIANTE = sys.argv[2]
MARCAS = set(VARIANTE.split("+")) - {"tal_cual"}
SALIDA = Path(sys.argv[3]).resolve()
assert MARCAS <= {"sin_e2_v3", "cortes_partes"}, VARIANTE
assert not (COPIA / "data/experiment/evaluacion/.env").exists(), "la copia no debe tener .env"
os.chdir(COPIA)
os.environ["ANTHROPIC_API_KEY"] = "seco-sin-red"


def _sin_red(*a, **k):
    raise RuntimeError("red bloqueada en la corrida en seco de T2-ter")


socket.socket.connect = _sin_red
socket.create_connection = _sin_red

import anthropic                       # noqa: E402
from anthropic.types import Message    # noqa: E402

PEDIDOS: list[dict] = []


def _punto(kw: dict) -> str | None:
    msg = kw["messages"][0]["content"]
    if isinstance(msg, list):
        msg = "\n".join(b.get("text", "") for b in msg if isinstance(b, dict))
    for linea in msg.splitlines():
        if linea.startswith(("Punto del chunk:", "Unidad de origen:")):
            return linea.split(":", 1)[1].strip().split(" ", 1)[0]
    m = re.search(r"cap::[0-9.]+(?:::parte\d)?", msg)
    return m.group(0) if m else None


class _Mensajes:
    def create(self, **kw):
        return _respuesta(kw, "create")

    def stream(self, timeout=None, **kw):
        final = _respuesta(kw, "stream")

        class _Flujo:
            def __enter__(self):
                return self

            def __exit__(self, *a):
                return False

            def get_final_message(self):
                return final
        return _Flujo()


def _respuesta(kw: dict, camino: str):
    tool = (kw.get("tools") or [{}])[0].get("name")
    n = len(PEDIDOS) + 1
    PEDIDOS.append({"n": n, "camino": camino, "tool": tool, "model": kw.get("model"),
                    "max_tokens": kw.get("max_tokens"), "temperature": kw.get("temperature", "sin fijar"),
                    "punto": _punto(kw)})
    msg = json.dumps(kw["messages"], ensure_ascii=False)
    corta = ("cortes_partes" in MARCAS and tool != "verificar_completitud_e3" and "(parte " in msg
             and kw.get("max_tokens") in (8192, 16384))
    PEDIDOS[-1]["corta_en_seco"] = corta
    if tool == "verificar_completitud_e3":
        inp = {"veredicto": "completo_ok", "faltantes": []}
    elif corta:
        inp = {}
    elif re.search(r"\(parte (\d)/(\d)\)", msg):
        # una parte de cap::4.2.1.2: una Operacion con un tramo literal de su texto propio, para seguir su procedencia
        # hasta el E2 r2
        k = int(re.search(r"\(parte (\d)/(\d)\)", msg).group(1))
        part = json.loads((COPIA / "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b/cap/particiones_por_corte.json")
                          .read_text(encoding="utf-8"))["cap::4.2.1.2"]["partes"][k - 1]
        tramo = next(x.strip() for x in part["texto"].splitlines()[1:] if len(x.strip()) > 20)
        inp = {"entities": [{"type": "TextoOrdenado", "local_id": "to", "label": "TO seco", "punto": "4.2.1.2"},
                            {"type": "Operacion", "local_id": "e1", "label": f"Operacion en seco, parte {k}",
                             "punto": "4.2.1.2", "tramo": tramo,
                             "properties": {"tipo": "cálculo", "descripcion": "Prueba en seco."}}],
               "relations": [{"predicate": "establecida_en", "punto": "4.2.1.2", "source": "e1", "target": "to"}],
               "omisiones": []}
        PEDIDOS[-1]["tramo_en_seco"] = tramo
    else:
        inp = {"entities": [{"local_id": "to", "type": "TextoOrdenado", "label": "TO seco", "punto": _punto(kw)}],
               "relations": [], "omisiones": []}
    return Message.model_validate({
        "id": f"msg_seco_{n}", "type": "message", "role": "assistant", "model": f"{kw.get('model')}-seco",
        "content": [{"type": "tool_use", "id": f"toolu_seco_{n}", "name": tool, "input": inp}],
        "stop_reason": "max_tokens" if corta else "tool_use", "stop_sequence": None,
        "usage": {"input_tokens": 100, "output_tokens": kw["max_tokens"] if corta else 50, "cache_creation_input_tokens": 0,
                  "cache_read_input_tokens": 0}})


class ClienteFalso:
    def __init__(self, *a, **k):
        self.messages = _Mensajes()


anthropic.Anthropic = ClienteFalso

RUNNER = COPIA / "data/experiment/reextraccion_v2/corpus_v2/runner_corpus.py"
# `python runner_corpus.py` pone la carpeta del script en sys.path[0] (de ahí importa cerrar_e2_r2 a r1_e4): se
# reproduce ese modo script, en lugar de la carpeta de este harness; el resto del path lo arma el runner.
sys.path[0] = str(RUNNER.parent)
spec = importlib.util.spec_from_file_location("runner_corpus", RUNNER)
RC = importlib.util.module_from_spec(spec)
sys.modules["runner_corpus"] = RC
spec.loader.exec_module(RC)
if "sin_e2_v3" in MARCAS:
    RC.cerrar_e2 = lambda to, salida, limite=None: {"omitido_en_seco": True}

sys.argv = ["runner_corpus.py",
            "--manifiesto", "data/experiment/reextraccion_v2/manifiestos/tanda0_10tos_r2b.json",
            "--salida", "data/experiment/reextraccion_v2/corpus_tanda0/salida_r2b",
            "--perfil-r2", "--tos", "cap", "--reabrir-fase", "cap:e1,cap:e3", "--autorizado-tope", "80.0"]
res = {"variante": VARIANTE, "argv": sys.argv[1:]}
try:
    res["rc"] = RC.main()
except Exception as e:   # noqa: BLE001 — se registra la excepción que la corrida real dejaría escapar
    res["rc"] = None
    res["excepcion"] = f"{type(e).__name__}: {e}"
res["pedidos_al_sdk"] = PEDIDOS
SALIDA.write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "pedidos_al_sdk"}, ensure_ascii=False))
print("pedidos al SDK:", len(PEDIDOS))
for p in PEDIDOS:
    print(" ", p)
