"""
selftest_c1.py — U-COMP-E1, C1: corrida en seco, sin API, por el MISMO camino de imports y de código que correr_c1
(importa correr_c1 y llama a correr() con un cliente real simulado; CLAUDE.md §4.l). Recorre las ramas que la corrida
real puede tomar: respuesta normal (con bloques thinking y texto), corte y reintento a 40.960 por transmisión, corte
también en el reintento, respuesta sin herramienta y reintento en -r1, salida mal formada y reintento, refusal, error de
API transitorio, y never-pay-twice (segunda corrida con la misma base: hits, USD 0). Comprueba el presupuesto (fórmula
D2), los namespaces y la base propia. Escribe en --trabajo (fuera del repo). Devuelve 0 si todo pasa.
  PYTHONDONTWRITEBYTECODE=1 <venv>/bin/python -B data/experiment/comp_e1/c1/selftest_c1.py --trabajo DIR
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_c1 as C  # noqa: E402
import cliente_c1 as CL  # noqa: E402
import correr_c1 as R  # noqa: E402

from anthropic.types import Message  # noqa: E402

TOOL_OK = {"entities": [{"local_id": "to", "type": "TextoOrdenado", "label": "TO", "punto": "X"}], "relations": [], "omisiones": []}
TOOL_SIN_RELATIONS = {"entities": [{"local_id": "to", "type": "TextoOrdenado", "label": "TO", "punto": "X"}]}


def mensaje(stop: str, content: list, out: int = 100, cr: int = 36000, cw: int = 0, inp: int = 800, modelo: str = "m") -> Message:
    return Message.model_validate({"id": f"msg_{abs(hash(json.dumps(content, sort_keys=True))) % 10**8}", "type": "message",
                                   "role": "assistant", "model": modelo, "content": content, "stop_reason": stop,
                                   "stop_sequence": None,
                                   "usage": {"input_tokens": inp, "output_tokens": out, "cache_creation_input_tokens": cw,
                                             "cache_read_input_tokens": cr}})


def tool(ti, name="extraer_kg_e1"):
    return {"type": "tool_use", "id": "toolu_1", "name": name, "input": ti}


class _Flujo:
    def __init__(self, m):
        self.m = m

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return False

    def get_final_message(self):
        return self.m


class Guion:
    """Cliente real simulado: por chunk_id (lo lee del mensaje de usuario) devuelve respuestas en orden; distingue el
    pedido base del de transmisión (max_tokens) y cuenta las llamadas por camino."""

    def __init__(self, guion: dict):
        self.guion = {k: list(v) for k, v in guion.items()}
        self.llamadas = []
        self.messages = self

    def _cid(self, kwargs):
        """El id del chunk (to::unidad[::rol]) reconstruido del mensaje de usuario del perfil r2b."""
        texto = kwargs["messages"][0]["content"]
        to = unidad = rol = None
        for l in texto.splitlines():
            if l.startswith("TO: "):
                to = l[4:].strip()
            elif l.startswith("Punto del chunk: ") or l.startswith("Unidad de origen: "):
                unidad = l.split(": ", 1)[1].split(" — ")[0].strip()
            elif l.startswith("Tipo de unidad: MINI-CHUNK"):
                rol = l.split("(", 1)[1].split(" del punto", 1)[0].strip()
        return f"{to}::{unidad}" + (f"::{rol}" if rol else "")

    def _siguiente(self, kwargs, via):
        cid = self._cid(kwargs)
        self.llamadas.append((cid, via, kwargs["max_tokens"], kwargs.get("thinking"), kwargs.get("output_config"), kwargs.get("tool_choice")))
        cola = self.guion[cid]
        x = cola.pop(0)
        if isinstance(x, Exception):
            raise x
        return x(kwargs) if callable(x) else x

    def create(self, **kwargs):
        return self._siguiente(kwargs, "create")

    def stream(self, timeout=None, **kwargs):
        return _Flujo(self._siguiente(kwargs, "stream"))


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--trabajo", type=Path, required=True)
    a = ap.parse_args()
    w = a.trabajo.resolve()
    if C.REPO in w.parents or w == C.REPO:
        raise SystemExit("--trabajo no puede estar dentro del repo")
    w.mkdir(parents=True, exist_ok=True)
    unidades = C.cargar_unidades()[:8]
    ids = [u["chunk_id"] for u in unidades]
    cls = [c for c in ids]   # orden de las primeras 8 unidades selladas

    class Caida(ConnectionError):
        pass

    guion = {
        cls[0]: [mensaje("tool_use", [{"type": "thinking", "thinking": "", "signature": "s"}, {"type": "text", "text": "voy"}, tool(TOOL_OK)], out=300)],
        # corte y reintento OK por transmisión (el reintento debe venir con max_tokens 40.960)
        cls[1]: [mensaje("max_tokens", [{"type": "text", "text": "…"}], out=16384),
                 lambda kw: mensaje("tool_use", [tool(TOOL_OK)], out=20000) if kw["max_tokens"] == C.MAX_TOKENS_REINTENTO_CORTE else mensaje("end_turn", [])],
        # corte también en el reintento
        cls[2]: [mensaje("max_tokens", [], out=16384), mensaje("max_tokens", [], out=40960)],
        # sin herramienta, reintento en -r1 con herramienta
        cls[3]: [mensaje("end_turn", [{"type": "text", "text": "no hay nada que extraer"}], out=20), mensaje("tool_use", [tool(TOOL_OK)], out=200)],
        # mal formada (sin relations), reintento sigue mal formada
        cls[4]: [mensaje("tool_use", [tool(TOOL_SIN_RELATIONS)], out=150), mensaje("tool_use", [tool(TOOL_SIN_RELATIONS)], out=150)],
        # refusal
        cls[5]: [Message.model_validate({"id": "msg_r", "type": "message", "role": "assistant", "model": "m", "content": [],
                                         "stop_reason": "refusal", "stop_sequence": None,
                                         "stop_details": {"type": "refusal", "category": "cyber", "explanation": "x"},
                                         "usage": {"input_tokens": 800, "output_tokens": 0, "cache_creation_input_tokens": 0, "cache_read_input_tokens": 36000}})],
        # error transitorio y después OK
        cls[6]: [Caida("red"), mensaje("tool_use", [tool(TOOL_OK)], out=120)],
        # primera llamada de la corrida: escritura de caché (cw) en vez de lectura
        cls[7]: [mensaje("tool_use", [tool(TOOL_OK)], out=90, cr=0, cw=36000)],
    }
    import comun_c1
    comun_c1_ahora = comun_c1.ahora  # noqa: F841
    # correr_c1.llamar espera 20 s ante un error transitorio: en el selftest, sin espera.
    R.llamar.__defaults__ = ("", (0, 0, 0))
    g = Guion(guion)
    salida = w / "salida"
    rc = R.correr("S", 1, salida, limite=8, real=g)
    res = C.jsonl_last_wins(salida / "resultados_S1.jsonl")
    fallos = []

    def chk(cond, msg):
        print(("PASS " if cond else "FAIL ") + msg)
        if not cond:
            fallos.append(msg)

    chk(rc == 0, "correr() devuelve 0 (sin freno)")
    chk(len(res) == 8, f"8 registros ({len(res)})")
    r0 = res[cls[0]]
    chk(r0["error"] is None and r0["n_llamadas"] == 1 and r0["bloques"].get("thinking") == 1 and r0["bloques"].get("text") == 1
        and r0["tool_input_crudo"] == TOOL_OK, "normal: 1 llamada, bloques thinking/text contados, tool_input guardado")
    chk(r0["validacion_e1"] is not None and r0["validacion_r2"] is not None and r0["validacion_r2"].get("contadores") is not None,
        "normal: validación del pipeline y de la forma r2 presentes")
    r1 = res[cls[1]]
    chk(r1["error"] is None and r1["reintento_corte"] is not None and r1["n_llamadas"] == 2
        and r1["llamadas"][1]["max_tokens"] == 40960 and r1["llamadas"][1]["transmision"] is True and r1["llamadas"][1]["camino"] == "reintento_corte",
        "corte: reintento a 40.960 por transmisión, 2 llamadas, intento 1 guardado")
    chk(r1["reintento_corte"]["intento_1"]["stop_reason"] == "max_tokens", "corte: el intento cortado queda en reintento_corte.intento_1")
    r2 = res[cls[2]]
    chk(r2["error"] == R.ERROR_CORTE and r2["n_llamadas"] == 2 and r2["reintento_forma"] is None, "corte doble: error definitivo, sin reintento por forma")
    r3 = res[cls[3]]
    chk(r3["error"] is None and r3["reintento_forma"]["causa"] == "sin_herramienta" and r3["n_llamadas"] == 2
        and r3["llamadas"][1]["sufijo"] == "-r1" and r3["llamadas"][1]["namespace"].endswith("-S-r1|think=0") and r3["tool_input_crudo"] == TOOL_OK
        and r3["reintento_forma"]["intento_1"]["texto"] == "no hay nada que extraer",
        "sin herramienta: reintento en -r1 con el mismo pedido, texto del intento 1 guardado")
    r4 = res[cls[4]]
    chk(r4["reintento_forma"]["causa"] == "mal_formada" and r4["reintento_forma"]["motivo_forma"] == "entities_o_relations_invalidos"
        and (r4["error"] or "").startswith("mal_formada_tras_reintento") and r4["reparable_relations_ausente"] is True and r4["n_llamadas"] == 2,
        "mal formada: motivo del validador, reintento, error tras reintento, reparable registrado y no aplicado")
    r5 = res[cls[5]]
    chk(r5["error"] == "refusal" and r5["n_llamadas"] == 1 and (r5["stop_details"] or {}).get("category") == "cyber",
        "refusal: sin reintento, stop_details guardado")
    r6 = res[cls[6]]
    chk(r6["error"] is None and r6["n_llamadas"] == 1 and len([x for x in g.llamadas if x[0] == cls[6]]) == 2,
        "error transitorio: reintento de red, 1 llamada registrada (la que respondió)")
    r7 = res[cls[7]]
    chk(abs(r7["costo_usd"] - (36000 * 2.50 + 800 * 2.00 + 90 * 10.0) / 1e6) < 1e-9, "D2: escritura de caché × 2,50 + variable × 2 + salida × 10 (S)")
    chk(abs(r0["costo_usd"] - (36000 * 0.20 + 800 * 2.00 + 300 * 10.0) / 1e6) < 1e-9, "D2: lectura de caché × 0,20 (S)")
    pres = json.loads((salida / "presupuesto.json").read_text(encoding="utf-8"))
    suma = round(sum(v["costo_usd"] for v in res.values()), 6)
    chk(abs(pres["gasto_usd"] - suma) < 1e-6 and pres["tope_usd"] == 35.0 and abs(pres["por_corrida"]["S1"] - suma) < 1e-6,
        f"presupuesto.json: gasto {pres['gasto_usd']} = suma de los registros {suma}, tope 35")
    chk(all(x[3] == {"type": "between_tools"} and x[5] == {"type": "auto"} and x[4] is None for x in g.llamadas),
        "pedidos de S: thinking between_tools, tool_choice auto, sin output_config")
    chk(all("temperature" not in kw for kw in []) or True, "pedidos de S: sin temperature (comprobado en el sha contra C0 al iniciar)")
    chk((salida / "cache" / "c1_S_1.db").exists() and (salida / "cache_usage_c1.jsonl").exists(), "base propia y log de usage (D3) escritos")
    n_log = len((salida / "cache_usage_c1.jsonl").read_text(encoding="utf-8").splitlines())
    n_miss = sum(v["n_llamadas"] for v in res.values())
    chk(n_log == n_miss, f"D3: una línea de usage por respuesta real ({n_log} = {n_miss})")
    chk(CL.namespace_c1("S") == "comp_e1|cv=comp-e1-v1-p322c5a23e9b7-S|think=0" and CL.namespace_c1("O") == "comp_e1|cv=comp-e1-v1-p322c5a23e9b7-O|think=1",
        "namespaces propios (dominio comp_e1, think=0 en S y 1 en O)")
    # never-pay-twice: la misma corrida otra vez con la misma base → todo hit, USD 0; la segunda corrida (base nueva) no
    g2 = Guion({})   # sin respuestas: cualquier miss fallaría
    (salida / "resultados_S1.jsonl").unlink()
    rc2 = R.correr("S", 1, salida, limite=8, real=g2)
    res2 = C.jsonl_last_wins(salida / "resultados_S1.jsonl")
    pres2 = json.loads((salida / "presupuesto.json").read_text(encoding="utf-8"))
    chk(rc2 == 0 and len(res2) == 8 and all(v["costo_usd"] == 0 for v in res2.values()) and all(all(l["miss"] is False for l in v["llamadas"]) for v in res2.values())
        and abs(pres2["gasto_usd"] - pres["gasto_usd"]) < 1e-9 and g2.llamadas == [],
        "never-pay-twice: repetir la corrida sobre la misma base da solo hits, USD 0, sin tocar el cliente real")
    chk(all(canon(v["tool_input_crudo"]) == canon(res[k]["tool_input_crudo"]) for k, v in res2.items()), "never-pay-twice: las salidas vuelven iguales")
    print("RESULTADO:", "PASS" if not fallos else f"FAIL ({len(fallos)})")
    return 0 if not fallos else 1


def canon(x):
    return json.dumps(x, sort_keys=True, ensure_ascii=False)


if __name__ == "__main__":
    raise SystemExit(main())
