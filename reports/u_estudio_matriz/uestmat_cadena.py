"""U-ESTUDIO-MATRIZ — re-ensamblado EN MEMORIA de KG-Tanda0-Desarrollo-r1.

Usa la réplica de la cadena r1 de tanda0/code/ensamblar_tanda0.py
(correr_cadena con w=None: no escribe intermedios) con las mismas
redirecciones en memoria que usó el ensamblado sellado. Para una variante de
matriz, reemplaza en memoria e2_lib.ensamblar por un envoltorio que:
  1. re-valida el crudo de cada unidad (el que produjo su validación final,
     ubicado y verificado en el paso 1) con el esquema ampliado;
  2. llama al e2_lib.ensamblar original con ese esquema.
Ningún archivo del repo se edita; el envoltorio se restaura al salir.
Supuesto declarado: las relaciones que pasan a válidas entran al grafo sin
nueva verificación E3 (cota superior del efecto antes de re-verificar).
"""
from __future__ import annotations

import contextlib
import copy
import json
import sys
from pathlib import Path

import uestmat_comun as U

sys.path.insert(0, str(U.EXP / "tanda0" / "code"))
import ensamblar_tanda0 as ET  # noqa: E402  (solo import; redirecciones en memoria)
import manifiesto_corpus as MC  # noqa: E402
import e2_lib  # noqa: E402

MANIFIESTO = U.REX / "manifiestos" / "tanda0_ens_desarrollo.json"
SALIDA_R1_NO_USADA = Path("/tmp/u_estudio_matriz/_salida_r1_no_usada")  # w=None: nunca se crea

_ENSAMBLAR_ORIGINAL = e2_lib.ensamblar


def cargar_crudos() -> dict[str, dict]:
    """(chunk_id) → crudo que produjo la validación final de la unidad
    (fuente verificada en el paso 1: e1 last-wins, compact last-wins o caché
    de reintentos)."""
    pob = json.loads(Path("/tmp/u_estudio_matriz/uestmat_poblacion_final.json").read_text(encoding="utf-8"))
    filas = {x["key"]: x for x in U.filas_reintentos()}
    e1_lw: dict[str, dict] = {}
    comp_lw: dict[str, dict] = {}
    for to in U.TOS_10:
        for d in U.leer_jsonl(U.SALIDA / to / "extracciones_e1.jsonl"):
            e1_lw[d["chunk_id"]] = d
        for d in U.leer_jsonl(U.SALIDA / to / "extracciones_e1_compact.jsonl"):
            comp_lw[d["chunk_id"]] = d
    out = {}
    for k, v in pob.items():
        cid = v["chunk_id"]
        if not v["reproduce"]:
            raise RuntimeError(f"unidad sin crudo verificado: {k}")
        if v["fuente_crudo"] == "cache_reintentos":
            out[cid] = filas[v["cache_keys"][0]]["tool_input"]
        elif v["fuente_crudo"] == "e1_compact_last_wins":
            out[cid] = comp_lw[cid]["tool_input_crudo"]
        else:
            out[cid] = e1_lw[cid]["tool_input_crudo"]
    return out


class Envoltorio:
    def __init__(self, esquema, crudos: dict[str, dict]):
        self.esquema = esquema
        self.crudos = crudos
        self.relaciones_nuevas: list[dict] = []   # (chunk_id, relación) aceptadas por la ampliación
        self.unidades_revalidadas = 0

    def __call__(self, chunks, registros, esquema=None, labels_catalogo=None):
        por_id = {c["id"]: c for c in chunks}
        nuevos = []
        for reg in registros:
            val = reg.get("validacion")
            cid = reg.get("chunk_id")
            if val is None or reg.get("error") or cid not in por_id:
                nuevos.append(reg)
                continue
            base = U.validador_e1.validar_salida(self.crudos[cid], por_id[cid], esquema=esquema).as_dict()
            if base != val:
                raise RuntimeError(f"la re-validación congelada no reproduce el registro: {cid}")
            amp = U.validador_e1.validar_salida(self.crudos[cid], por_id[cid], esquema=self.esquema).as_dict()
            self.unidades_revalidadas += 1
            if len(amp["relaciones"]) != len(val["relaciones"]):
                claves_base = [json.dumps(r, sort_keys=True) for r in val["relaciones"]]
                for r in amp["relaciones"]:
                    if json.dumps(r, sort_keys=True) not in claves_base:
                        self.relaciones_nuevas.append({"chunk_id": cid, "relacion": r})
            r2 = copy.deepcopy(reg)
            r2["validacion"] = amp
            nuevos.append(r2)
        return _ENSAMBLAR_ORIGINAL(chunks, nuevos, esquema=self.esquema, labels_catalogo=labels_catalogo)


def correr(esquema_variante=None, crudos=None) -> dict:
    """Corre la cadena r1 completa en memoria. esquema_variante=None →
    e2_lib.ensamblar original (control de reproducción del sello)."""
    man = MC.cargar(MANIFIESTO)
    perfil = U.perfil_v3()
    plan = ET.plan_redirecciones(man, perfil, U.SALIDA, SALIDA_R1_NO_USADA)
    env = None
    if esquema_variante is not None:
        env = Envoltorio(esquema_variante, crudos)
        plan = plan + [(e2_lib, "ensamblar", env)]
    with contextlib.redirect_stdout(sys.stderr):
        with ET.redirigido(plan):
            est = ET.correr_cadena(perfil, con_cola=True, hasta="final", w=None)
    assert e2_lib.ensamblar is _ENSAMBLAR_ORIGINAL
    kg = json.loads(est["kg_json"])
    return {"sha256": est["sha256"], "kg": kg, "envoltorio": env}
