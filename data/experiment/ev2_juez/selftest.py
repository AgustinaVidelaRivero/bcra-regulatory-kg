"""
selftest.py — Selftest OFFLINE del juez de fidelidad EV2 (cero API, cero costo).

Ejercita el circuito completo de calibración con un cliente falso que devuelve
veredictos SCRIPTEADOS sobre casos sintéticos inventados, verificando:

  1. persistencia completa (jsonl por repetición + distribución de las N reps
     en los agregados + write-through en las dbs);
  2. N=3 con dbs separadas: tres .db distintas, keys pairwise disjuntas
     (0 cross-hits estructural) y never-pay-twice (replay = hit, mismo objeto);
  3. mapping correcto: los veredictos scripteados producen exactamente los
     cuatro desenlaces del §2 (correcto / incorrecto / parcial /
     requiere_adjudicacion, este último por ambas vías: dudoso y sin_consenso);
  4. cero fuga del veredicto humano al input del juez, verificado
     estructuralmente: (a) los fuentes del juez/driver/prompt no referencian
     la adjudicación humana ni sus campos; (b) cada request capturado contiene
     EXACTAMENTE el prompt del juez + (pregunta, respuesta, criterios) — nada más.

Además chequea la carga real de respuestas de U6 (lectura local, sin API).

Correr:  .venv/bin/python data/experiment/ev2_juez/selftest.py
"""

from __future__ import annotations

import json
import shutil
import sys
from pathlib import Path

JUEZ_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(JUEZ_DIR))

import juez  # noqa: E402  (al importarse agrega evaluacion/ al sys.path)
import llm_cache as lc  # noqa: E402
from driver_calibracion import (agregar, armar_casos, cargar_criterios,  # noqa: E402
                                cargar_respuestas, correr, verificar_cross_hits,
                                SEMILLA_ORDEN)

OUT = JUEZ_DIR / "selftest_out"
CHECKS: list[tuple[str, bool]] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    CHECKS.append((nombre, cond))
    print(f"  [{'PASS' if cond else 'FAIL'}] {nombre}{(' — ' + detalle) if detalle else ''}")


# --------------------------------------------------------------------------- #
# Casos sintéticos + guion de veredictos                                      #
# --------------------------------------------------------------------------- #
# Cada caso: 2 criterios sintéticos inventados. El guion fija, por repetición,
# el veredicto de cada criterio y la clasificación auxiliar, eligiendo los
# escenarios para cubrir los cuatro casos del mapping (§2) por ambas vías.
GUION = {
    # qid: (clasificacion, {rep: [veredicto_c1, veredicto_c2]}, esperado_pregunta)
    "SYN-CORR": ("contenido", {1: ["cumplido", "cumplido"],
                               2: ["cumplido", "cumplido"],
                               3: ["cumplido", "cumplido"]}, "correcto"),
    "SYN-INCO": ("abstencion", {1: ["no_cumplido", "no_cumplido"],
                                2: ["no_cumplido", "no_cumplido"],
                                3: ["no_cumplido", "no_cumplido"]}, "incorrecto"),
    "SYN-PARC": ("contenido", {1: ["cumplido", "no_cumplido"],
                               2: ["cumplido", "no_cumplido"],
                               3: ["no_cumplido", "no_cumplido"]}, "parcial"),
    "SYN-DUDO": ("contenido", {1: ["cumplido", "dudoso"],
                               2: ["cumplido", "dudoso"],
                               3: ["cumplido", "dudoso"]}, "requiere_adjudicacion"),
    "SYN-SINC": ("contenido", {1: ["cumplido", "cumplido"],
                               2: ["cumplido", "no_cumplido"],
                               3: ["cumplido", "dudoso"]}, "requiere_adjudicacion"),
}
# Modales esperados por construcción: SYN-PARC c1 = cumplido (2-1), c2 = no_cumplido
# → parcial; SYN-SINC c2 = tres distintos → sin_consenso → requiere_adjudicacion.

PREGUNTAS_SYN = {q: {"id": q, "pregunta": f"[{q}] ¿Pregunta sintética de selftest?"}
                 for q in GUION}
RESPUESTAS_SYN = {q: {"respuesta": f"Respuesta sintética del caso {q}: fragmento_alfa. "
                                   f"Luego fragmento_beta.",
                      "respondible": q != "SYN-INCO"}
                  for q in GUION}
CRITERIOS_SYN = [{"id_pregunta": q,
                  "criterios": [
                      {"criterio": f"Criterio sintético 1 de {q}",
                       "cita_textual": f"Cita sintética uno de {q}."},
                      {"criterio": f"Criterio sintético 2 de {q}",
                       "cita_textual": f"Cita sintética dos de {q}."}]}
                 for q in sorted(GUION)]


class ClienteFalso:
    """Rol de 'cliente real' debajo de CachingClient: devuelve Messages del SDK
    construidos desde el guion, y captura cada request recibido (para la
    verificación estructural de fuga)."""

    def __init__(self, rep: int, registro: list):
        self._rep = rep
        self._registro = registro
        self.messages = self

    def create(self, **kwargs):
        from anthropic.types import Message
        self._registro.append({"rep": self._rep, "kwargs": kwargs})
        texto_usuario = kwargs["messages"][0]["content"]
        qid = texto_usuario.split("[", 1)[1].split("]", 1)[0]
        clasif, por_rep, _ = GUION[qid]
        vs = por_rep[self._rep]
        cuerpo = {"clasificacion_respuesta": clasif,
                  "criterios": [{"indice": i + 1, "veredicto": v,
                                 "fragmento": None if v == "no_cumplido" else "fragmento_alfa",
                                 "justificacion": f"scripteado rep {self._rep}"}
                                for i, v in enumerate(vs)]}
        texto = json.dumps(cuerpo, ensure_ascii=False)
        return Message.model_validate({
            "id": f"fake_{qid}_r{self._rep}", "type": "message", "role": "assistant",
            "model": "cliente-falso", "stop_reason": "end_turn", "stop_sequence": None,
            "content": [{"type": "text", "text": texto}],
            "usage": {"input_tokens": len(kwargs["system"]) // 4 +
                      len(texto_usuario) // 4,
                      "output_tokens": len(texto) // 4}})


def main() -> int:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "cache").mkdir(parents=True)
    (OUT / "out").mkdir(parents=True)

    # --- insumos reales de solo-lectura (sin API) ---
    print("== carga real de respuestas U6 (offline) ==")
    reales = cargar_respuestas()
    check("25 respuestas reales cargadas", len(reales) == 25, f"n={len(reales)}")
    check("todas con texto no vacío", all(r["respuesta"] for r in reales.values()))
    check("flags respondible=False detectados",
          sorted(q for q, r in reales.items() if r["respondible"] is False)
          == ["U6-012", "U6-021"])

    # --- esquema fijo de criterios_u6.json (vía archivo, mismo camino que producción) ---
    print("== esquema de criterios y orden sellado ==")
    crit_path = OUT / "criterios_selftest.json"
    crit_path.write_text(json.dumps(CRITERIOS_SYN, ensure_ascii=False, indent=2),
                         encoding="utf-8")
    criterios = cargar_criterios(crit_path)
    check("criterios sintéticos validados", set(criterios) == set(GUION))
    malo = [{"id_pregunta": "SYN-X", "criterios": [{"criterio": "c", "cita_textual": ""}]}]
    (OUT / "criterios_malos.json").write_text(json.dumps(malo), encoding="utf-8")
    try:
        cargar_criterios(OUT / "criterios_malos.json")
        check("cita_textual vacía rechazada", False)
    except ValueError:
        check("cita_textual vacía rechazada", True)

    casos = armar_casos(PREGUNTAS_SYN, RESPUESTAS_SYN, criterios)
    import random
    esperado = sorted(GUION)
    random.Random(SEMILLA_ORDEN).shuffle(esperado)
    check("orden = shuffle determinístico de la semilla",
          [c["qid"] for c in casos] == esperado, " ".join(esperado))

    # --- corrida N=3 con cliente falso bajo CachingClient (dbs separadas) ---
    print("== corrida N=3 (cliente falso + caché real) ==")
    registro: list = []

    def factory(rep: int, label: str):
        return lc.CachingClient(
            ClienteFalso(rep, registro), domain="juez_ev2",
            db_path=OUT / "cache" / f"juez_calibracion_r{rep}.db",
            namespace=lc.make_namespace(f"juez_ev2_r{rep}",
                                        code_ver=juez.CODE_VER, thinking=False),
            thinking_enabled=False, run_label=label)

    correr(casos, reps=3, out_dir=OUT / "out", client_factory=factory)

    dbs = sorted((OUT / "cache").glob("*.db"))
    check("3 dbs de caché separadas", len(dbs) == 3,
          " ".join(p.name for p in dbs))
    ver = verificar_cross_hits(dbs)
    check("keys por db = n casos", all(n == len(casos) for n in ver["keys_por_db"].values()),
          str(ver["keys_por_db"]))
    check("0 cross-hits (keys pairwise disjuntas)", ver["cross_hits"] == 0,
          str(ver["intersecciones"]))
    check("0 hits en primera pasada (re-muestreo real)",
          all((h or 0) == 0 for d in ver["hits_por_label"].values() for h in d.values()),
          str(ver["hits_por_label"]))

    # never-pay-twice: repetir UN caso de rep 1 con cliente nuevo sobre la misma db
    replay = lc.CachingClient(
        ClienteFalso(1, []), domain="juez_ev2",
        db_path=OUT / "cache" / "juez_calibracion_r1.db",
        namespace=lc.make_namespace("juez_ev2_r1", code_ver=juez.CODE_VER, thinking=False),
        thinking_enabled=False, run_label="selftest_replay")
    r_replay = juez.juzgar(replay, casos[0]["pregunta"], casos[0]["respuesta"],
                           casos[0]["criterios"])
    st = replay.stats()
    replay.close()
    primera = [json.loads(l) for l in
               (OUT / "out" / "veredictos_r1.jsonl").read_text().splitlines()
               if json.loads(l)["qid"] == casos[0]["qid"]][0]
    check("replay es hit (never-pay-twice)", st["hits"] == 1 and st["misses"] == 0, str(st["hit_rate"]))
    check("replay reproduce el veredicto persistido",
          r_replay["veredicto"]["criterios"] == primera["criterios"])

    # --- persistencia completa + mapping sobre veredictos scripteados ---
    print("== persistencia + mapping (§2, cuatro casos) ==")
    for rep in (1, 2, 3):
        regs = [json.loads(l) for l in
                (OUT / "out" / f"veredictos_r{rep}.jsonl").read_text().splitlines() if l]
        check(f"rep {rep}: {len(GUION)}/{len(GUION)} casos persistidos",
              len(regs) == len(GUION))
    agg = agregar(OUT / "out", 3, casos)
    por_qid = {a["qid"]: a for a in agg["agregados"]}
    for qid, (_, _, esperado_v) in GUION.items():
        check(f"{qid} → {esperado_v}",
              por_qid[qid]["veredicto_pregunta"] == esperado_v,
              f"obtenido {por_qid[qid]['veredicto_pregunta']}")
    check("distribución completa persistida (3 veredictos por par)",
          all(len(cr["veredictos_reps"]) == 3
              for a in agg["agregados"] for cr in a["criterios"]))
    check("sin_consenso visible en SYN-SINC c2",
          por_qid["SYN-SINC"]["criterios"][1]["modal"] == "sin_consenso")
    check("clasificación auxiliar persistida (abstencion en SYN-INCO)",
          por_qid["SYN-INCO"]["clasificacion_respuesta_reps"] == ["abstencion"] * 3)
    (OUT / "out" / "veredictos_agregados.json").write_text(
        json.dumps(agg, ensure_ascii=False, indent=2), encoding="utf-8")

    # --- cero fuga del veredicto humano (estructural) ---
    print("== ceguera del veredicto humano ==")
    marcadores = ["u6_adjudicacion_humana", "mitad_fallada", "sintoma_enviado",
                  "cohorte_sintoma", "fuente_sintoma", "pulgar",
                  "notas_adjudicacion"]
    fuentes = ["juez.py", "driver_calibracion.py", "mapping.py", "prompt_juez_v1.md"]
    for f in fuentes:
        texto = (JUEZ_DIR / f).read_text(encoding="utf-8")
        hallados = [m for m in marcadores if m in texto]
        check(f"{f}: sin referencias a la adjudicación humana", not hallados,
              str(hallados) if hallados else "")

    check("requests capturados = 3 reps × casos",
          len(registro) == 3 * len(GUION), f"n={len(registro)}")
    claves_ok = all(set(r["kwargs"]) == {"model", "max_tokens", "temperature",
                                         "system", "messages"} for r in registro)
    check("request sin campos extra", claves_ok)
    check("system == prompt del juez, verbatim",
          all(r["kwargs"]["system"] == juez.PROMPT_JUEZ for r in registro))
    por_qid_caso = {c["qid"]: c for c in casos}
    exacto = all(
        r["kwargs"]["messages"] == [{
            "role": "user",
            "content": juez.construir_mensaje_usuario(
                por_qid_caso[r["kwargs"]["messages"][0]["content"].split("[", 1)[1].split("]", 1)[0]]["pregunta"],
                por_qid_caso[r["kwargs"]["messages"][0]["content"].split("[", 1)[1].split("]", 1)[0]]["respuesta"],
                por_qid_caso[r["kwargs"]["messages"][0]["content"].split("[", 1)[1].split("]", 1)[0]]["criterios"])}]
        for r in registro)
    check("mensaje de usuario == (pregunta, respuesta, criterios) y nada más", exacto)
    payload = json.dumps([r["kwargs"] for r in registro], ensure_ascii=False, default=str)
    hallados = [m for m in marcadores if m in payload]
    check("payloads sin rastro de la adjudicación humana", not hallados, str(hallados))

    # --- medición de tokens del guion (insumo de estimacion.py) ---
    med = {"chars_system": len(juez.PROMPT_JUEZ),
           "chars_salida_json_por_caso": [len(json.dumps(
               {"clasificacion_respuesta": g[0],
                "criterios": [{"indice": i + 1, "veredicto": v,
                               "fragmento": "fragmento_alfa", "justificacion": "x" * 120}
                              for i, v in enumerate(g[1][1])]}, ensure_ascii=False))
               for g in GUION.values()]}
    (OUT / "medicion_selftest.json").write_text(json.dumps(med, indent=2), encoding="utf-8")

    fallos = [n for n, ok in CHECKS if not ok]
    print(f"\nRESULTADO: {'PASS ✅' if not fallos else 'FAIL ❌'} "
          f"({len(CHECKS) - len(fallos)}/{len(CHECKS)} checks)")
    return 0 if not fallos else 1


if __name__ == "__main__":
    sys.exit(main())
