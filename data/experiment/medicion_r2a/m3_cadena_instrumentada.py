"""U-MED-R2A, M3 — mediciones adicionales sobre la cadena r2, instrumentada en memoria (USD 0).

Corre `ensamblar_tanda0.correr_cadena_r2` sobre la salida guardada de la tanda 0, con la misma redirección que
`ensamblar_manifiesto_r2` y sin escribir nada salvo --out. No edita ningún módulo: envuelve, solo en memoria y durante
la corrida, tres funciones de módulos importados y las restaura al terminar.
- `r1_referencias._tramos_e0_de` y `r1_referencias.menciones_por_tramo`: registra las menciones que detecta la regla
  (i) en texto heredado. Las reconoce por el sitio de la llamada, la línea de `detectar_y_resolver_r2` que lee el bloque
  heredado (`_tramos_e0_de(p_h, chunk)` en `detectar_y_resolver_r2`, que se busca en la fuente). Clasifica las que son la línea «Sección N.» del
  contexto heredado leída como cita de la misma sección (secciones = [N], sin puntos, unidad heredada S<N>, evidencia
  que empieza con «Sección N»), y cuenta las aristas `remite_a` que terminan con esa evidencia.
- `runner_corpus.entrada_r2`: registra las unidades que quedan sin validación (`validacion` None), con su `error`.
Controles: el sha256 del grafo de la corrida tiene que ser el del grafo versionado, y el total de menciones de la
regla (i), sin las anáforas sin número, tiene que ser el contador `texto_heredado.menciones` del reporte.

Uso, desde la raíz del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/medicion_r2a/m3_cadena_instrumentada.py \
      --out data/experiment/medicion_r2a/m3/m3_cadena_instrumentada.json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "data" / "experiment" / "tanda0" / "code"))
import ensamblar_tanda0 as ENS          # noqa: E402  (sin editar; agrega al path los módulos de la cadena)
import runner_corpus as RC              # noqa: E402  (sin editar)

REF = ENS.REF
REX = "data/experiment/reextraccion_v2"
ENTRADA = f"{REX}/corpus_tanda0/salida_dirigida"
E0_R2 = f"{REX}/e0_chunking/salida_tanda0_r2"
GRAFOS = OrderedDict([
    ("diez", {"manifiesto": f"{REX}/manifiestos/tanda0_ens_diez.json", "dir": f"{REX}/corpus_tanda0/ens_diez_r2a/r2"}),
    ("desarrollo", {"manifiesto": f"{REX}/manifiestos/tanda0_ens_desarrollo.json",
                    "dir": f"{REX}/corpus_tanda0/ens_desarrollo_r2a/r2"}),
])
RE_SECCION = re.compile(r"^\s*Secci[oó]n\s+(\d+)\b", re.I)


def linea_sitio_i() -> int:
    """Línea de r1_referencias.py donde la regla (i) lee el bloque heredado."""
    fuente = Path(REF.__file__).read_text(encoding="utf-8").splitlines()
    ls = [i for i, l in enumerate(fuente, 1) if "_tramos_e0_de(p_h, chunk)" in l]
    assert len(ls) == 1, ls
    return ls[0]


def correr(nombre: str, cfg: dict) -> dict:
    man = ENS.MC.cargar(RAIZ / cfg["manifiesto"])
    perfil = ENS.perfil_e1.perfil(man.perfil_e1)
    M = ENS.E4.modulo_modelos_r2()
    cat = ENS.E4.catalogo_r2()
    linea = linea_sitio_i()
    estado = {"ultimo": None}
    menciones_i, sin_validacion = [], []
    orig_tramos, orig_men, orig_entrada = REF._tramos_e0_de, REF.menciones_por_tramo, RC.entrada_r2

    def tramos_w(p, chunk):
        out = orig_tramos(p, chunk)
        f = sys._getframe(1)
        if f.f_code.co_name == "detectar_y_resolver_r2" and f.f_lineno == linea:
            estado["ultimo"] = (out, dict(p), chunk.get("id"))
        return out

    def men_w(tramos, to_origen, reglas):
        out = orig_men(tramos, to_origen, reglas)
        u = estado["ultimo"]
        if u is not None and u[0] is tramos:
            for m in out:
                menciones_i.append({"chunk_id": u[2], "unidad_heredada": u[1].get("punto"),
                                    "tipo_herencia": u[1].get("rol_documental"), "clase": m.get("clase"),
                                    "puntos": list(m.get("puntos") or []), "secciones": list(m.get("secciones") or []),
                                    "evidencia": m.get("evidencia")})
            estado["ultimo"] = None
        return out

    def entrada_w(to, *a, **k):
        regs = orig_entrada(to, *a, **k)
        for r in regs:
            if r.get("validacion") is None:
                sin_validacion.append({"to": to, "chunk_id": r.get("chunk_id"), "error": r.get("error"),
                                       "estado_e3": r.get("estado_e3"), "origen_crudo": r.get("origen_crudo")})
        return regs

    with tempfile.TemporaryDirectory() as tmp:
        plan = ENS.plan_redirecciones_r2(man, perfil, RAIZ / ENTRADA, Path(tmp) / "r2", cat, M)
        REF._tramos_e0_de, REF.menciones_por_tramo, RC.entrada_r2 = tramos_w, men_w, entrada_w
        try:
            with ENS.redirigido(plan):
                res = ENS.correr_cadena_r2(man, perfil, None, None, RAIZ / E0_R2)
        finally:
            REF._tramos_e0_de, REF.menciones_por_tramo, RC.entrada_r2 = orig_tramos, orig_men, orig_entrada
    kg = res["kg"]
    sha_versionado = __import__("hashlib").sha256((RAIZ / cfg["dir"] / "kg.json").read_bytes()).hexdigest()
    reporte = json.loads((RAIZ / cfg["dir"] / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    contables = [m for m in menciones_i if m["clase"] != "anafora_sin_numero"]

    def es_seccion_propia(m):
        mt = RE_SECCION.match(m["evidencia"] or "")
        return (mt is not None and not m["puntos"] and m["secciones"] == [mt.group(1)]
                and m["unidad_heredada"] == f"S{mt.group(1)}")
    sec = [m for m in contables if es_seccion_propia(m)]
    # aristas remite_a con evidencia «Sección N…» y destino la misma sección S<N> del TO de la procedencia
    aristas_sec = []
    for e in kg["edges"]:
        if e["relation"] != "remite_a":
            continue
        mt = RE_SECCION.match(e["properties"].get("evidencia") or "")
        if mt and e["properties"]["destino"] == f"{e['provenance'].get('to')}::S{mt.group(1)}":
            aristas_sec.append({"source": e["source"], "destino": e["properties"]["destino"],
                                "evidencia": e["properties"]["evidencia"], "punto_procedencia": e["provenance"].get("punto"),
                                "chunk_id": e["provenance"].get("chunk_id")})
    # causa de cada unidad sin validación, del registro de E1 de la salida guardada (validacion.rechazos y forma del
    # tool_input), y si la unidad llegó a E3 (finales.jsonl)
    for s in sin_validacion:
        d = RAIZ / ENTRADA / s["to"]
        reg_e1 = next((json.loads(l) for l in (d / f"extracciones_finales_{s['to']}.jsonl").read_text(encoding="utf-8").splitlines()
                       if l.strip() and json.loads(l).get("chunk_id") == s["chunk_id"]), None)
        s["e1_rechazos"] = (reg_e1 or {}).get("validacion", {}).get("rechazos")
        s["e1_tool_input_claves"] = {k: type(v).__name__ for k, v in ((reg_e1 or {}).get("tool_input_crudo") or {}).items()}
        s["e1_stop_reason"] = (reg_e1 or {}).get("stop_reason")
        s["en_finales_e3"] = any(json.loads(l).get("chunk_id") == s["chunk_id"]
                                 for l in (d / "finales.jsonl").read_text(encoding="utf-8").splitlines() if l.strip())
    # citas del registro de remisiones versionado atribuidas por la regla (i) con esa forma, y su destino
    registro = json.loads((RAIZ / cfg["dir"] / "remisiones_registro.json").read_text(encoding="utf-8"))
    reg_sec = []
    for c in registro:
        mt = RE_SECCION.match(c.get("evidencia") or "")
        if (c.get("atribucion") == "texto_heredado" and mt and not c.get("puntos") and c.get("secciones") == [mt.group(1)]
                and c["procedencia"].get("punto") == f"S{mt.group(1)}"):
            reg_sec.append(c)
    return OrderedDict([
        ("sha256_corrida", res["sha256"]), ("sha256_versionado", sha_versionado), ("sha_coincide", res["sha256"] == sha_versionado),
        ("menciones_regla_i_todas", len(menciones_i)), ("menciones_regla_i_sin_anafora_sin_numero", len(contables)),
        ("contador_del_reporte_texto_heredado_menciones", reporte["remite_a"]["texto_heredado"]["menciones"]),
        ("contador_coincide", len(contables) == reporte["remite_a"]["texto_heredado"]["menciones"]),
        ("seccion_N_leida_como_cita_de_la_misma_seccion", OrderedDict([
            ("menciones", len(sec)),
            ("chunks_distintos", len({m["chunk_id"] for m in sec})),
            ("secciones_distintas", len({(m["chunk_id"].split("::")[0], m["secciones"][0]) for m in sec})),
            ("por_tipo_de_herencia", dict(sorted(Counter(m["tipo_herencia"] for m in sec).items()))),
            ("por_to", dict(sorted(Counter(m["chunk_id"].split("::")[0] for m in sec).items()))),
            ("ejemplos", sorted({(m["chunk_id"], m["evidencia"][:80]) for m in sec})[:10])])),
        ("otras_menciones_regla_i", OrderedDict([
            ("menciones", len(contables) - len(sec)),
            ("por_clase", dict(sorted(Counter(m["clase"] for m in contables if not es_seccion_propia(m)).items())))])),
        ("aristas_remite_a_con_evidencia_seccion_N_a_la_misma_seccion", OrderedDict([
            ("aristas", len(aristas_sec)), ("detalle", aristas_sec[:20])])),
        ("registro_citas_regla_i_seccion_N", OrderedDict([
            ("citas_en_el_registro", len(reg_sec)),
            ("con_destino", sum(1 for c in reg_sec if c.get("destinos"))),
            ("aristas_nuevas", sum(c.get("aristas_nuevas") or 0 for c in reg_sec)),
            ("irresolubles_por_causa", dict(sorted(Counter(x["causa"] for c in reg_sec for x in c.get("irresolubles") or []).items())))])),
        ("unidades_sin_validacion", OrderedDict([
            ("total", len(sin_validacion)), ("por_error", dict(sorted(Counter(s["error"] for s in sin_validacion).items()))),
            ("detalle", sorted(sin_validacion, key=lambda s: (s["to"], s["chunk_id"] or "")))])),
        ("rechazados_del_reporte", sum(v["rechazados"] for v in reporte["e2_por_to"].values())),
    ])


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = OrderedDict((k, correr(k, c)) for k, c in GRAFOS.items())
    (RAIZ / a.out).write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    for k, v in out.items():
        print(k, {x: v[x] for x in ("sha_coincide", "menciones_regla_i_sin_anafora_sin_numero", "contador_coincide")},
              v["seccion_N_leida_como_cita_de_la_misma_seccion"]["menciones"],
              v["aristas_remite_a_con_evidencia_seccion_N_a_la_misma_seccion"]["aristas"],
              v["unidades_sin_validacion"]["por_error"])


if __name__ == "__main__":
    main()
