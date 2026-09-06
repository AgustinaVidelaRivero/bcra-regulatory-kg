"""
comparar_pareada_b54.py — U-B5.4 fase 3: comparación mecánica pareada + fichas.

$0 (sin API). Lee resultados_pareada_b54.jsonl (después: tool_input crudo bajo
el prefijo v3) y las extracciones persistidas del universo primario (antes:
capa validacion.relaciones, la sellada en las predicciones; el crudo del antes
se muestra como columna informativa cuando difiere). Emite:
  - reporte_pareada_b54.md  (comparación por unidad contra las predicciones
    SELLADAS de predicciones_pareada_selladas_b54.md, commit f19e978)
  - fichas_pareada_b54.md   (SOLO casos de juicio semántico, en orden
    aleatorizado con semilla declarada b54-pareada-v1)

Asimetría de capas DECLARADA: el "después" no pasa por el validador de
producción (call-site prohibido en esta unidad); la comparación de sujetos es
robusta a eso porque los campos de sujeto no son alterados por el validador
(precedente: tabla lateral de U-SUJ-FREQ §5).

Uso (desde cualquier cwd): python3 <ruta>/comparar_pareada_b54.py
"""

from __future__ import annotations

import json
import random
import sys
from pathlib import Path

_CODE_DIR = Path(__file__).resolve().parent
_UNIT = _CODE_DIR.parent
_REPO = _CODE_DIR.parents[3]
if str(_CODE_DIR) not in sys.path:
    sys.path.insert(0, str(_CODE_DIR))

from runner_pareada_b54 import SELECCION, TOS_DEV  # noqa: E402

SEMILLA = "b54-pareada-v1"
EF = "Sujeto_entidad_financiera"

# rol → TO propio (para la predicción global de no-migración cross-TO)
ROL_A_TO = {
    "Sujeto_rol_sujeto_obligado_proteccion": "pro",
    "Sujeto_rol_entidad_autorizada_exterior": "ext",
    "Sujeto_rol_obligado_a_clasificar_clasificacion": "cla",
    "Sujeto_rol_entidad_comprendida_reginf": "ric",
    "Sujeto_rol_alcance_capmin": "cap",
}

ROL_DEV_DE = {"cap": "Sujeto_rol_alcance_capmin", "cla": "Sujeto_rol_obligado_a_clasificar_clasificacion",
              "pro": "Sujeto_rol_sujeto_obligado_proteccion", "ric": "Sujeto_rol_entidad_comprendida_reginf",
              "ext": "Sujeto_rol_entidad_autorizada_exterior"}


def sujetos_de(relaciones: list[dict]) -> dict:
    ids, props, ejecuta_ids = [], [], []
    for r in relaciones or []:
        if r.get("predicate") not in ("aplica_a", "ejecuta"):
            continue
        sid, sp = r.get("sujeto_id"), r.get("sujeto_propuesto")
        if sid:
            ids.append(sid)
            if r.get("predicate") == "ejecuta":
                ejecuta_ids.append(sid)
        if sp:
            props.append(sp)
    return {"ids": sorted(set(ids)), "propuestos": sorted(set(props)),
            "ejecuta_ids": sorted(set(ejecuta_ids))}


def cargar_antes() -> dict[str, dict]:
    necesarios = {cid for cid, _ in SELECCION}
    tos = sorted({cid.split("::", 1)[0] for cid in necesarios})
    filas: dict[str, dict] = {}
    for to in tos:
        if to in TOS_DEV:
            path = _REPO / "data/experiment/reextraccion_v2/corpus_v2/salida" / to / "extracciones_e1.jsonl"
        else:
            path = _REPO / "data/experiment/esq/cobertura" / to / f"extracciones_e1_{to}.jsonl"
        for line in path.read_text().splitlines():
            r = json.loads(line)
            if r.get("chunk_id") in necesarios:
                filas[r["chunk_id"]] = r  # dedupe: gana el último (regla U-SUJ-FREQ)
    faltan = necesarios - set(filas)
    if faltan:
        raise RuntimeError(f"antes no encontrado para: {sorted(faltan)}")
    out = {}
    for cid, r in filas.items():
        val = (r.get("validacion") or {}).get("relaciones") or []
        crudo = ((r.get("tool_input_crudo") or {}).get("relations")) or []
        out[cid] = {"validacion": sujetos_de(val), "crudo": sujetos_de(crudo)}
    return out


def contiene(props: list[str], *terminos: str) -> bool:
    import unicodedata
    def n(s):
        s = unicodedata.normalize("NFD", s.lower())
        return "".join(c for c in s if unicodedata.category(c) != "Mn")
    return any(all(t in n(p) for t in terminos) for p in props)


def veredicto(cid: str, brazo: str, antes: dict, desp: dict) -> tuple[str, str, bool]:
    """→ (veredicto, detalle, ficha). Reglas mecánicas de las predicciones selladas."""
    ids, props = desp["ids"], desp["propuestos"]
    to = cid.split("::", 1)[0]
    if brazo == "A":
        rol = ROL_DEV_DE[to]
        ok = rol in ids
        return ("PASA" if ok else "NO_CUMPLE", f"rol propio {rol} {'presente' if ok else 'AUSENTE'}", not ok)
    if brazo == "B":
        esperado = {"ayccef": EF, "actgar": EF, "expaef": EF,
                    "lavdin": "Sujeto_rol_alcance_lavdin", "cryl": "Sujeto_rol_alcance_cryl"}[to]
        ajeno_previo = [i for i in antes["validacion"]["ids"] if i.startswith("Sujeto_rol_")]
        ajeno_persiste = [i for i in ids if i in ajeno_previo]
        if esperado in ids and not ajeno_persiste:
            return ("PASA", f"{esperado} presente; rol ajeno previo {ajeno_previo} ya no aparece", False)
        if ajeno_persiste:
            return ("FICHA", f"persiste rol ajeno {ajeno_persiste} (¿referencia legítima al régimen ajeno?)", True)
        return ("FICHA", f"esperado {esperado} no emitido; ids={ids} props={props}", True)
    if brazo == "C":
        if cid == "cap::6.2.1.1":
            fallas = []
            if "Sujeto_banco_central_del_exterior" not in ids: fallas.append("banco_central_del_exterior AUSENTE")
            if "Sujeto_fmi" not in ids: fallas.append("fmi AUSENTE")
            if not contiene(props, "pagos internacionales"): fallas.append("BIS no quedó en propuesto")
            ok = not fallas
            return ("PASA" if ok else "NO_CUMPLE", "; ".join(fallas) or "BCE/bancos centrales→clase, FMI→instancia, BIS→propuesto", not ok)
        if cid == "cryl::3.1":
            fallas = []
            if "Sujeto_camara_electronica_de_compensacion" not in ids: fallas.append("clase CEC AUSENTE")
            if not contiene(props, "mercados"): fallas.append("Mercados de Valores no quedó en propuesto")
            if not contiene(props, "depositarias"): fallas.append("Centrales Depositarias no quedó en propuesto")
            ok = not fallas
            return ("PASA" if ok else "NO_CUMPLE", "; ".join(fallas) or "CEC→clase; mercados/CDV→propuestos", not ok)
        if to == "traval":
            det = f"ids={ids} props={props}"
            return ("FICHA", f"predicción sellada: FICHA en ambos sentidos — {det}", True)
        if to == "expaef":  # 9.3 / 9.5.3
            mal = "Sujeto_empresa_de_servicios_complementarios" in ids
            agencia = contiene(props, "agencia") or contiene(props, "complementar")
            if not mal and agencia:
                return ("PASA", "agencia complementaria sigue en propuesto; no atraída", False)
            if mal:
                return ("NO_CUMPLE", "atracción a Sujeto_empresa_de_servicios_complementarios", True)
            return ("FICHA", f"agencia no aparece como propuesto; ids={ids} props={props}", True)
    if brazo == "D":
        ej = desp["ejecuta_ids"]
        ok = ("Sujeto_bcra" in ids or "Sujeto_sefyc" in ids) and all(
            e in ("Sujeto_bcra", "Sujeto_sefyc") for e in ej)
        det = f"ejecuta={ej}; ids={ids}"
        return ("PASA" if ok else "NO_CUMPLE", det, not ok)
    if brazo == "E":
        ok = EF in ids
        return ("PASA" if ok else "NO_CUMPLE", f"EF {'presente' if ok else 'AUSENTE'}; ids={ids}", not ok)
    if brazo == "F":
        mal = "Sujeto_entidad_originante" in ids
        det = f"ids={ids} props={props}"
        if mal:
            return ("NO_CUMPLE", "MIGRÓ a Sujeto_entidad_originante (violación de la guarda)", True)
        return ("PASA", f"no migró al id SNP; {det}", False)
    raise RuntimeError(f"brazo desconocido {brazo}")


def main() -> None:
    res = [json.loads(l) for l in (_UNIT / "resultados_pareada_b54.jsonl").read_text().splitlines()]
    antes = cargar_antes()
    por_id = {r["chunk_id"]: r for r in res}
    assert len(por_id) == len(SELECCION) == 34, "resultados incompletos"

    filas, fichas = [], []
    violaciones_global = []
    for cid, brazo in SELECCION:
        r = por_id[cid]
        desp = sujetos_de((r.get("tool_input_crudo") or {}).get("relations") or [])
        v, det, ficha = veredicto(cid, brazo, antes[cid], desp)
        # global: no-migración cross-TO de roles (P-B-global)
        to = cid.split("::", 1)[0]
        for i in desp["ids"]:
            if i.startswith("Sujeto_rol_"):
                to_del_rol = ROL_A_TO.get(i) or i.removeprefix("Sujeto_rol_alcance_")
                if to_del_rol != to:
                    violaciones_global.append((cid, i))
        filas.append({"chunk_id": cid, "brazo": brazo, "veredicto": v, "detalle": det,
                      "antes_validacion": antes[cid]["validacion"], "antes_crudo": antes[cid]["crudo"],
                      "despues": desp})
        if ficha:
            fichas.append(filas[-1])

    n = {"PASA": 0, "FICHA": 0, "NO_CUMPLE": 0}
    for f in filas:
        n[f["veredicto"]] += 1
    por_brazo = {}
    for f in filas:
        b = por_brazo.setdefault(f["brazo"], {"PASA": 0, "FICHA": 0, "NO_CUMPLE": 0})
        b[f["veredicto"]] += 1

    # ------------------ reporte ------------------ #
    L = ["# Verificación pareada U-B5.4 — comparación mecánica contra predicciones selladas",
         "",
         "Predicciones: `predicciones_pareada_selladas_b54.md` (commit f19e978). Después:",
         "tool_input crudo bajo el prefijo v3 (`29af2e29880b…`); antes: capa",
         "`validacion.relaciones` persistida (columna cruda informativa). Reproduce:",
         "`python3 data/experiment/b54_catalogo_v3/code/comparar_pareada_b54.py`.",
         "",
         f"**Totales: {n['PASA']} PASA / {n['FICHA']} FICHA / {n['NO_CUMPLE']} NO_CUMPLE** "
         f"(34 unidades). Por brazo: " + "; ".join(
             f"{b}: {c['PASA']}/{c['FICHA']}/{c['NO_CUMPLE']}" for b, c in sorted(por_brazo.items())),
         "",
         "**P-B-global (no-migración cross-TO de roles): " +
         ("SIN violaciones ✓" if not violaciones_global else f"VIOLACIONES: {violaciones_global}") + "**",
         "",
         "| unidad | brazo | veredicto | detalle | antes (validación) | después (crudo v3) |",
         "|---|---|---|---|---|---|"]
    for f in filas:
        a = f["antes_validacion"]; d = f["despues"]
        fmt = lambda s: ("ids: " + ", ".join(x.removeprefix("Sujeto_") for x in s["ids"]) +
                         ("; prop: " + "; ".join(p[:40] for p in s["propuestos"]) if s["propuestos"] else "")) or "—"
        L.append(f"| `{f['chunk_id']}` | {f['brazo']} | **{f['veredicto']}** | {f['detalle'][:160]} | {fmt(a)[:180]} | {fmt(d)[:180]} |")
    (_UNIT / "reporte_pareada_b54.md").write_text("\n".join(L) + "\n")

    # ------------------ fichas (aleatorizadas, semilla declarada) ------------------ #
    rng = random.Random(SEMILLA)
    orden = list(range(len(fichas)))
    rng.shuffle(orden)
    F = ["# Fichas de adjudicación — pareada U-B5.4 (solo juicio semántico)",
         "",
         f"Orden aleatorizado con semilla declarada `{SEMILLA}` ({len(fichas)} fichas).",
         "La adjudicación es de la autora; la predicción sellada NO se fuerza sobre",
         "estos casos. Cada ficha: qué decía el texto, qué emitió el prefijo congelado",
         "(antes) y qué emitió el v3 (después), y la pregunta a adjudicar.",
         ""]
    chunks_texto = {}
    from runner_pareada_b54 import cargar_chunks
    for cid, ch in cargar_chunks().items():
        chunks_texto[cid] = (ch.get("texto") or "").replace("\n", " ")[:600]
    for num, idx in enumerate(orden, 1):
        f = fichas[idx]
        F += [f"## Ficha {num} — `{f['chunk_id']}` (brazo {f['brazo']})",
              "",
              f"**Texto del punto (recortado):** {chunks_texto[f['chunk_id']]}",
              "",
              f"**Antes (validación):** ids={f['antes_validacion']['ids']} propuestos={f['antes_validacion']['propuestos']}",
              f"**Antes (crudo, informativo):** ids={f['antes_crudo']['ids']} propuestos={f['antes_crudo']['propuestos']}",
              f"**Después (crudo v3):** ids={f['despues']['ids']} propuestos={f['despues']['propuestos']}",
              "",
              f"**Detalle mecánico:** {f['detalle']}",
              "",
              "**Adjudicación de la autora:** [ ] correcto v3 · [ ] correcto antes · [ ] ambos defendibles · [ ] otro: ______",
              ""]
    (_UNIT / "fichas_pareada_b54.md").write_text("\n".join(F) + "\n")

    print(f"totales: {n} | fichas: {len(fichas)} | violaciones cross-TO: {len(violaciones_global)}")
    print("escritos: reporte_pareada_b54.md, fichas_pareada_b54.md")


if __name__ == "__main__":
    main()
