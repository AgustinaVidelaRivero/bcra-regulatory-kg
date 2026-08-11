"""
ratchet_e3.py — Mecánica del MINI-RATCHET de E3 (T2).

Política (docs/diseno_reextraccion_v2.md §3-E3, tope resuelto para la
calibración en 1 reintento — resuelve la pregunta abierta §7.a por mandato de
esta unidad, laudable de nuevo con datos de calibración):

  veredicto E3 con faltantes
    → prompt de RE-EXTRACCIÓN: el prompt E1 del chunk, ÍNTEGRO, + bloque de
      feedback estructurado, marcado como reintento. El bloque va DESPUÉS del
      breakpoint de caché (dentro del mensaje de usuario): el prefijo E1
      (system + tools + tool_choice) queda byte-idéntico y el caching no se
      invalida — verificado en el selftest.
    → re-extracción (cliente E1) → re-validación E1 → re-verificación E3.
  tope: 1 reintento. Si persisten faltantes → el chunk va a COLA HUMANA con
  flag y TODO persistido. NUNCA ingreso silencioso al grafo.

El verificador JAMÁS corrige: este módulo solo transporta su feedback al
extractor. Todos los veredictos se persisten (RegistroE3).

Capa determinística sobre el veredicto (principio 2.b: lo mecánico va en
código, encima del juicio del LLM — mismo patrón que la capa determinística
del verificador de la Fase 2.4):
  - coherencia veredicto/faltantes (completo_ok ⇔ faltantes vacío);
  - verificación de cada cita textual contra el fuente real de la unidad
    (normalización del precedente C7). Una cita que NO verifica no se inyecta
    al reintento (una cita fabricada envenenaría la re-extracción); queda
    registrada. Si NINGÚN faltante tiene cita verificada, el veredicto es
    inutilizable para el ratchet y el chunk va a cola humana con flag propio.
"""

from __future__ import annotations

import json
from pathlib import Path

import comun_e3
from comun_e3 import cita_en_fuente
import prompt_e3
import cliente_e3

import prompt_e1      # módulos de E1: solo import (mecánica de re-inyección)
import validador_e1
import cliente_e1

TOPE_REINTENTOS = 1

ESTADOS = ("completo_ok_directo", "aceptado_tras_reintento",
           "cola_humana", "cola_humana_veredicto_inutilizable",
           "cola_humana_reextraccion_invalida")

MARCA_REINTENTO = "# REINTENTO DE EXTRACCIÓN — feedback del verificador de completitud (E3)"


# ------------------------------------------------------------------------- #
# Capa determinística sobre el veredicto del LLM                             #
# ------------------------------------------------------------------------- #

def evaluar_veredicto(tool_input, chunk: dict) -> dict:
    """Evalúa determinísticamente el tool input del verificador: coherencia
    del contrato + verificación de citas contra el fuente. No juzga contenido
    (eso es del LLM): juzga formato y anclaje."""
    ev = {
        "veredicto_crudo": tool_input,
        "es_completo_ok": False,
        "faltantes": [],               # todos, cada uno con cita_verificada
        "faltantes_utilizables": [],   # solo los de cita verificada
        "incoherencias": [],
    }
    if not isinstance(tool_input, dict):
        ev["incoherencias"].append("tool_input_no_dict")
        return ev

    veredicto = tool_input.get("veredicto")
    faltantes = tool_input.get("faltantes")
    if not isinstance(faltantes, list):
        faltantes = []
        ev["incoherencias"].append("faltantes_no_lista")

    if veredicto == "completo_ok" and faltantes:
        ev["incoherencias"].append("completo_ok_con_faltantes")
    if veredicto == "faltantes_detectados" and not faltantes:
        ev["incoherencias"].append("faltantes_detectados_sin_faltantes")
    if veredicto not in ("completo_ok", "faltantes_detectados"):
        ev["incoherencias"].append(f"veredicto_invalido:{veredicto}")

    # Conservador: solo es completo_ok un veredicto coherente y sin faltantes.
    ev["es_completo_ok"] = (veredicto == "completo_ok" and not faltantes
                            and not ev["incoherencias"])

    for f in faltantes:
        if not isinstance(f, dict):
            ev["incoherencias"].append("faltante_no_dict")
            continue
        cita = f.get("cita_textual_del_fuente") or ""
        f_ev = dict(f)
        f_ev["cita_verificada"] = cita_en_fuente(cita, chunk)
        ev["faltantes"].append(f_ev)
        if f_ev["cita_verificada"]:
            ev["faltantes_utilizables"].append(f_ev)

    return ev


# ------------------------------------------------------------------------- #
# Prompt de re-extracción: prompt E1 del chunk + feedback, tras el breakpoint #
# ------------------------------------------------------------------------- #

def bloque_feedback(faltantes: list[dict], intento: int) -> str:
    """Bloque de feedback estructurado que se anexa al MENSAJE DE USUARIO del
    request E1 (después del breakpoint de caché). Solo faltantes con cita
    verificada entran acá."""
    partes = [
        MARCA_REINTENTO,
        f"(reintento {intento} de {TOPE_REINTENTOS})",
        "",
        "Un verificador de completitud, en contexto independiente, comparó tu "
        "extracción anterior de este chunk contra el texto fuente y detectó "
        "contenido normativo NO representado:",
        "",
    ]
    for i, f in enumerate(faltantes, 1):
        partes.append(
            f"{i}. [{f.get('tipo', 'otro')} | ubicación: {f.get('ubicacion', '?')} "
            f"| severidad: {f.get('severidad', '?')}]"
        )
        partes.append(f"   Cita del fuente no representada: «{f.get('cita_textual_del_fuente', '')}»")
        nota = f.get("nota")
        if nota:
            partes.append(f"   Nota: {nota}")
    partes += [
        "",
        "Re-extraé el chunk COMPLETO desde cero (no solo lo faltante), con todas "
        "las reglas del sistema vigentes, asegurando que cada cita señalada quede "
        "representada: en la descripcion de una entidad, como entidad propia "
        "(p. ej. una Excepcion) o como relación, según corresponda al schema. "
        "No inventes contenido que el fuente no sostiene.",
    ]
    return "\n".join(partes)


def build_reextraccion_kwargs(chunk: dict, faltantes: list[dict], model: str,
                              intento: int = 1,
                              max_tokens_reintento: int | None = None) -> dict:
    """Request de re-extracción: el request E1 canónico del chunk con el
    bloque de feedback ANEXADO al mensaje de usuario. El prefijo (system +
    tools + tool_choice) queda byte-idéntico al de la primera pasada: el
    feedback vive después del breakpoint y no invalida el caché.

    max_tokens_reintento: techo de salida SOLO para el reintento (el request
    base de E1 está sellado con su techo propio y no se toca). Un reintento
    que COMPLETA una extracción incompleta puede necesitar más salida que la
    primera pasada; max_tokens no integra el prefijo cacheado, así que
    cambiarlo no invalida el caché."""
    kwargs = prompt_e1.build_request_kwargs(chunk, model=model)
    if max_tokens_reintento is not None:
        kwargs["max_tokens"] = max_tokens_reintento
    mensaje = kwargs["messages"][0]["content"] + "\n\n" + bloque_feedback(faltantes, intento)
    kwargs["messages"] = [{"role": "user", "content": mensaje}]
    return kwargs


def reextraer_chunk(cliente_extractor, chunk: dict, faltantes: list[dict],
                    model: str, intento: int = 1,
                    max_tokens_reintento: int | None = None) -> dict:
    """Ejecuta la re-extracción con el cliente E1 inyectado (stub u real) y
    devuelve el tool input crudo + la re-validación E1."""
    kwargs = build_reextraccion_kwargs(chunk, faltantes, model=model, intento=intento,
                                       max_tokens_reintento=max_tokens_reintento)
    if isinstance(cliente_extractor, cliente_e1.ClienteE1Real):
        resp = cliente_extractor.create(doc=chunk["archivo"], **kwargs)
    else:
        resp = cliente_extractor.messages.create(**kwargs)

    tool_use = None
    for block in resp.content:
        if getattr(block, "type", None) == "tool_use":
            tool_use = block
            break
    tool_input = tool_use.input if tool_use is not None else None
    validacion = (validador_e1.validar_salida(tool_input, chunk).as_dict()
                  if tool_input is not None else None)
    return {
        "chunk_id": chunk["id"],
        "intento": intento,
        "tool_input": tool_input,
        "validacion": validacion,
        "error": None if tool_use is not None else "no_tool_use",
    }


# ------------------------------------------------------------------------- #
# Persistencia: todos los veredictos + cola humana con flag y TODO           #
# ------------------------------------------------------------------------- #

class RegistroE3:
    """Persistencia append-only de la corrida: veredictos.jsonl (TODOS los
    veredictos, incluidas re-verificaciones) y cola_humana.jsonl (chunks
    flaggeados con su TODO)."""

    def __init__(self, dir_salida: Path):
        self.dir = Path(dir_salida)
        self.dir.mkdir(parents=True, exist_ok=True)
        self.path_veredictos = self.dir / "veredictos.jsonl"
        self.path_cola = self.dir / "cola_humana.jsonl"

    def _append(self, path: Path, reg: dict) -> None:
        with path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(reg, ensure_ascii=False) + "\n")

    def veredicto(self, reg: dict) -> None:
        self._append(self.path_veredictos, reg)

    def cola_humana(self, chunk_id: str, estado: str, evaluacion: dict) -> None:
        pendientes = [
            {"tipo": f.get("tipo"), "cita": f.get("cita_textual_del_fuente"),
             "ubicacion": f.get("ubicacion"), "severidad": f.get("severidad"),
             "cita_verificada": f.get("cita_verificada")}
            for f in evaluacion.get("faltantes", [])
        ]
        self._append(self.path_cola, {
            "chunk_id": chunk_id,
            "flag": estado,
            "faltantes_pendientes": pendientes,
            "incoherencias": evaluacion.get("incoherencias", []),
            "todo": (
                f"TODO: revisión humana del chunk {chunk_id} — faltantes "
                f"persistentes tras {TOPE_REINTENTOS} reintento(s) del "
                f"mini-ratchet E3; el chunk NO ingresa al grafo hasta resolución."
            ),
        })


# ------------------------------------------------------------------------- #
# Ciclo completo del mini-ratchet para una unidad                            #
# ------------------------------------------------------------------------- #

def ciclo_ratchet(chunk: dict, validacion: dict, *, cliente_verificador,
                  cliente_extractor, model_e3: str, model_e1: str,
                  registro: RegistroE3 | None = None,
                  max_tokens_reintento: int | None = None) -> dict:
    """Ejecuta el ciclo E3 completo de una unidad:

      verificación → (si faltantes) re-extracción con feedback → re-validación
      E1 → re-verificación E3 → aceptación o cola humana.

    Devuelve el expediente completo (auditable). La extracción que sobrevive
    (original o re-extraída) queda en `validacion_final`; si el estado es de
    cola humana, `validacion_final` es None: nada ingresa al grafo."""

    def _persistir_veredicto(fase: str, intento: int, crudo: dict, ev: dict) -> None:
        if registro is not None:
            registro.veredicto({
                "chunk_id": chunk["id"], "fase": fase, "intento": intento,
                "tool_input": crudo["tool_input"], "error": crudo["error"],
                "es_completo_ok": ev["es_completo_ok"],
                "n_faltantes": len(ev["faltantes"]),
                "n_faltantes_utilizables": len(ev["faltantes_utilizables"]),
                "incoherencias": ev["incoherencias"],
                "faltantes": ev["faltantes"],
            })

    expediente: dict = {"chunk_id": chunk["id"], "veredictos": [], "reintentos": []}

    # --- Verificación inicial -------------------------------------------- #
    crudo1 = cliente_e3.verificar_chunk(cliente_verificador, chunk, validacion, model=model_e3)
    ev1 = evaluar_veredicto(crudo1["tool_input"], chunk)
    _persistir_veredicto("verificacion", 0, crudo1, ev1)
    expediente["veredictos"].append(ev1)

    if ev1["es_completo_ok"]:
        expediente["estado"] = "completo_ok_directo"
        expediente["validacion_final"] = validacion
        return expediente

    validacion_actual = validacion
    ev_actual = ev1
    for intento in range(1, TOPE_REINTENTOS + 1):
        if not ev_actual["faltantes_utilizables"]:
            # Veredicto sin ninguna cita verificable: inutilizable para el
            # ratchet — no se re-extrae sobre citas fabricadas.
            expediente["estado"] = "cola_humana_veredicto_inutilizable"
            expediente["validacion_final"] = None
            if registro is not None:
                registro.cola_humana(chunk["id"], expediente["estado"], ev_actual)
            return expediente

        # --- Re-extracción con feedback (después del breakpoint) --------- #
        reex = reextraer_chunk(cliente_extractor, chunk,
                               ev_actual["faltantes_utilizables"],
                               model=model_e1, intento=intento,
                               max_tokens_reintento=max_tokens_reintento)
        expediente["reintentos"].append(reex)
        if reex["error"] is not None or reex["validacion"] is None or any(
                r["nivel"] == "chunk" for r in reex["validacion"]["rechazos"]):
            expediente["estado"] = "cola_humana_reextraccion_invalida"
            expediente["validacion_final"] = None
            if registro is not None:
                registro.cola_humana(chunk["id"], expediente["estado"], ev_actual)
            return expediente

        # --- Re-verificación E3 sobre la nueva extracción ----------------- #
        validacion_actual = reex["validacion"]
        crudo_n = cliente_e3.verificar_chunk(cliente_verificador, chunk,
                                             validacion_actual, model=model_e3)
        ev_actual = evaluar_veredicto(crudo_n["tool_input"], chunk)
        _persistir_veredicto("re_verificacion", intento, crudo_n, ev_actual)
        expediente["veredictos"].append(ev_actual)

        if ev_actual["es_completo_ok"]:
            expediente["estado"] = "aceptado_tras_reintento"
            expediente["validacion_final"] = validacion_actual
            return expediente

    # --- Tope agotado: cola humana, jamás ingreso silencioso -------------- #
    expediente["estado"] = "cola_humana"
    expediente["validacion_final"] = None
    if registro is not None:
        registro.cola_humana(chunk["id"], "cola_humana", ev_actual)
    return expediente
