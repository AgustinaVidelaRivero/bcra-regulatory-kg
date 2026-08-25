"""
selftest_juez_r1.py — SELFTEST OFFLINE del wrapper del juez de U-B1.8 ($0,
sin API), previo a todo gasto de la etapa del juez (compromiso del README).

Cubre lo propio del wrapper (lo demás ya lo cubre selftest_r1.py):
  1. armar_casos: orden ciego determinístico (semilla juez-ev2-r1), ids
     opacos EV2R1- únicos, detección de pregunta de traza ≠ gold.
  2. Ceguera: vista ciega limpia (0 fugas) sobre el gold real; fuga
     PROVOCADA (marcador de grafo inyectado en una respuesta) detectada.
  3. Pipeline end-to-end con cliente falso: pf.correr escribe
     veredictos_r{1,2,3}.jsonl por id opaco, pf.agregar produce los
     veredictos esperados (mapping §2) y una salida no parseable del juez
     queda en errores_r{rep}.jsonl con el caso fuera de los agregados.
  4. Retomabilidad: re-lanzar pf.correr con un cliente que explota no
     re-llama nada (write-through por id opaco).

Todo bajo selftest_out/juez/ (gitignorado); no toca orden/, juez_out/ ni
desanonimizacion_SOLO_MESA/ reales.

Uso:  .venv/bin/python -B data/experiment/ev2_r1/code/selftest_juez_r1.py
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_r1 as cr                      # noqa: E402
import juez_r1 as jr                       # noqa: E402
import pipeline_fidelidad as pf            # noqa: E402
from comun_r1 import cf                    # noqa: E402
from anthropic.types import Message        # noqa: E402

OUT = cr.SELFTEST_DIR / "juez"

_checks = []


def check(nombre, cond):
    _checks.append((nombre, bool(cond)))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}")


def _msg_juez(veredictos: list[str], parseable: bool = True):
    if parseable:
        txt = json.dumps({"clasificacion_respuesta": "contenido",
                          "criterios": [{"indice": i + 1, "veredicto": v,
                                         "fragmento": None, "justificacion": ""}
                                        for i, v in enumerate(veredictos)]},
                         ensure_ascii=False)
    else:
        txt = "esto no es un JSON de veredicto"
    return Message.model_validate({
        "id": "msg_selftest_juez", "type": "message", "role": "assistant",
        "model": "claude-sonnet-4-6", "content": [{"type": "text", "text": txt}],
        "stop_reason": "end_turn", "stop_sequence": None,
        "usage": {"input_tokens": 100, "output_tokens": 50},
    })


class FakeJuez:
    """Devuelve por caso (clave: primeros chars de la pregunta) el guion dado."""

    def __init__(self, guion):
        self.guion = guion          # {pregunta: [Message por llamada, en orden]}
        self.llamadas = 0
        self.messages = self

    def create(self, **kwargs):
        preg = kwargs["messages"][0]["content"].split("\n")[1]
        cola = self.guion[preg]
        if not cola:
            raise AssertionError(f"llamada no prevista para {preg!r}")
        self.llamadas += 1
        return cola.pop(0)


class ExplodingClient:
    def __init__(self):
        self.messages = self

    def create(self, **kwargs):
        raise AssertionError("re-lanzamiento llamó al cliente real")


def main() -> int:
    print("== SELFTEST OFFLINE del juez de U-B1.8 (sin API, $0) ==")
    if OUT.exists():
        shutil.rmtree(OUT)
    OUT.mkdir(parents=True)

    gold = cf.cargar_gold()
    qids = sorted(gold)[:2]
    # la respuesta sintética NO incluye el id de pregunta: "EV2F-" es marcador
    # y el chequeo de ceguera lo flaggearía (correctamente)
    respuestas = [{"id_pregunta": q, "respuesta": f"respuesta sintética número {i}",
                   "respondible_flag": True,
                   "pregunta_traza": gold[q]["pregunta"]}
                  for i, q in enumerate(qids, 1)]

    # --- 1) armar_casos ---
    c1 = jr.armar_casos(respuestas, gold)
    c2 = jr.armar_casos(respuestas, gold)
    check("orden ciego determinístico (dos derivaciones idénticas)",
          [c["id_opaco"] for c in c1] == [c["id_opaco"] for c in c2])
    check("ids opacos EV2R1- únicos",
          all(c["id_opaco"].startswith("EV2R1-") for c in c1)
          and len({c["id_opaco"] for c in c1}) == len(c1))
    try:
        jr.armar_casos([{**respuestas[0], "pregunta_traza": "otra"}], gold)
        mismatch = False
    except ValueError:
        mismatch = True
    check("pregunta de traza ≠ gold levanta ValueError", mismatch)

    # --- 2) ceguera ---
    ciegos = jr.vista_ciega(c1)
    check("vista ciega limpia: 0 fugas en los requests",
          jr.verificar_ceguera_requests(ciegos) == [])
    sucio = [dict(ciegos[0])]
    sucio[0]["respuesta"] = ciegos[0]["respuesta"] + " ev2_base_v3"
    check("fuga PROVOCADA (marcador en la respuesta) detectada",
          jr.verificar_ceguera_requests(sucio) != [])

    # --- 3) pipeline end-to-end con cliente falso ---
    # caso A: r1 cumplido-todos / r2 cumplido-todos / r3 primero no_cumplido
    #   -> modales cumplido (2-de-3 el primero... según K criterios)
    # caso B: no parseable en r2 -> errores_r2.jsonl, caso incompleto
    guion = {}
    for c in c1:
        k = len(c["criterios"])
        if c["id_pregunta"] == qids[0]:
            guion[c["pregunta"].strip().splitlines()[0]] = [
                _msg_juez(["cumplido"] * k),
                _msg_juez(["cumplido"] * k),
                _msg_juez(["no_cumplido"] + ["cumplido"] * (k - 1)),
            ]
        else:
            guion[c["pregunta"].strip().splitlines()[0]] = [
                _msg_juez(["no_cumplido"] * k),
                _msg_juez([], parseable=False),
                _msg_juez(["no_cumplido"] * k),
            ]
    fake = FakeJuez(guion)
    frenado = pf.correr(ciegos, reps=3, out_dir=OUT,
                        client_factory=lambda rep, label: fake, freno=None,
                        verbose=False)
    check("pf.correr completó sin freno y consumió el guion",
          frenado is None and fake.llamadas == 6
          and all(not v for v in guion.values()))
    err2 = (OUT / "errores_r2.jsonl").read_text(encoding="utf-8").splitlines()
    check("salida no parseable registrada en errores_r2.jsonl", len(err2) == 1)
    agg = pf.agregar(OUT, 3, ciegos)
    por_id = {a["id_opaco"]: a for a in agg["agregados"]}
    idA = next(c["id_opaco"] for c in c1 if c["id_pregunta"] == qids[0])
    idB = next(c["id_opaco"] for c in c1 if c["id_pregunta"] == qids[1])
    check("agregado del caso A: modales por mayoría 2-de-3 → correcto",
          por_id[idA]["veredicto_pregunta"] == "correcto"
          and por_id[idA]["modales"] == ["cumplido"] * len(por_id[idA]["modales"]))
    check("caso B incompleto (una rep con error) fuera de los agregados",
          idB not in por_id and any(x["id_opaco"] == idB for x in agg["incompletas"]))

    # --- 4) retomabilidad ---
    frenado2 = pf.correr(ciegos, reps=3, out_dir=OUT,
                         client_factory=lambda rep, label: ExplodingClient(),
                         freno=None, verbose=False)
    check("re-lanzamiento no re-llama (write-through por id opaco)",
          frenado2 is None)

    passed = sum(ok for _, ok in _checks)
    print(f"\n  {passed}/{len(_checks)} checks OK")
    print("  RESULTADO:", "PASS" if passed == len(_checks) else "FAIL")
    return 0 if passed == len(_checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
