"""
lazo_e3_p3b.py — U-PROMPT-R2, P3b-1 (USD 0, sin API): medidas del lazo de E3 sobre la tanda 0, para los puntos j y k
de la etapa P3b (notas del 04/10/2026 al pie del mandato, `4f3bcff` y `8d01b04`).

j (hallazgo 2.2). Veredictos de E3 con `faltantes` como texto. En las unidades de la cola humana, el último veredicto
de cada una; si `faltantes` es un string, se lee de dos maneras:
  - estricta: `json.loads` del string;
  - con reparo: el primer valor JSON del string (`json.JSONDecoder.raw_decode`) y el `veredicto` del resto, si viene
    como `"veredicto": "…"`.
Con lo leído se re-evalúa el veredicto con la capa determinística vigente (`ratchet_e3.evaluar_veredicto`, LAUDO A y
LAUDO B, con el set de unidades del TO) y se dice a qué estado iría la unidad con la política del ratchet:
  - en la verificación: `completo_ok_directo`, `aceptado_con_residuales`, a un reintento (re-extracción y
    re-verificación, con su costo) o sigue en la cola (`cola_humana_veredicto_inutilizable`);
  - en la re-verificación: `aceptado_tras_reintento` o sigue en la cola (`cola_humana`).
Opción 2, volver a pedir el veredicto: costo por llamada de E3 y de E1 en reintento, de los `resumen_e3.json`.

k (hallazgo 2.14). Unidades aceptadas tras el reintento: la extracción del reintento reemplaza a la primera.
  - Pérdidas: entidades y relaciones de menos, por conteo; y entidades de la primera sin par en el reintento (mismo
    tipo y misma etiqueta o descripción normalizadas).
  - Copia de la nota de E3 (agregado 2 del 04/10/2026). REGLA, declarada antes de contar: tokens de R-NORM
    (`validador_r2.norm_tokens`: NFKD sin diacríticos, minúsculas, alfanuméricos); ventana de 5 tokens seguidos; una
    entidad del reintento copia la nota si su descripción o su etiqueta tiene una ventana que está en alguna `nota`
    de los faltantes que se le pasaron al reintento (los bloqueantes con cita verificada) y que no está ni en el texto
    de la unidad (propio y heredado) ni en las citas de esos faltantes. Se listan todos los casos.

Escribe solo en --salida (lazo_e3_p3b.json). Sobre una copia del repo (CLAUDE.md §4, regla l).

Uso (desde la raíz de la copia):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3b/lazo_e3_p3b.py --salida DIR
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

P3B = Path(__file__).resolve().parent
REPO = P3B.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
import comun_e1  # noqa: E402
import ratchet_e3  # noqa: E402
import validador_r2 as V  # noqa: E402

E0 = REX / "e0_chunking" / "salida_tanda0"
CORRIDAS = {"salida_dirigida": REX / "corpus_tanda0" / "salida_dirigida", "salida": REX / "corpus_tanda0" / "salida"}
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")
VENTANA = 5
RE_VEREDICTO = re.compile(r'"veredicto"\s*:\s*"([a-z_]+)"')


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def leer_faltantes(texto: str) -> dict:
    """Las dos lecturas del string de `faltantes`."""
    out = {"estricta": None, "reparo": None, "veredicto_en_texto": None}
    try:
        v = json.loads(texto)
        out["estricta"] = v
    except json.JSONDecodeError:
        pass
    try:
        v, fin = json.JSONDecoder().raw_decode(texto.lstrip())
        out["reparo"] = v
        m = RE_VEREDICTO.search(texto.lstrip()[fin:])
        out["veredicto_en_texto"] = m.group(1) if m else None
    except json.JSONDecodeError:
        pass
    return out


def a_tool_input(ti: dict, leido) -> dict | None:
    """El tool input que habría llegado bien formado, desde lo leído."""
    if isinstance(leido, dict) and "faltantes" in leido:
        return {"veredicto": leido.get("veredicto") or ti.get("veredicto"), "faltantes": leido.get("faltantes")}
    if isinstance(leido, list):
        return {"veredicto": ti.get("veredicto"), "faltantes": leido}
    return None


def estado_con_politica(ev: dict, fase: str) -> str:
    if fase == "verificacion":
        if ev["es_completo_ok"]:
            return "completo_ok_directo"
        if ev["aceptable"]:
            return "aceptado_con_residuales"
        if ev["bloqueantes_utilizables"]:
            return "reintento (re-extracción y re-verificación)"
        return "sigue: cola_humana_veredicto_inutilizable"
    return "aceptado_tras_reintento" if ev["es_completo_ok"] or ev["aceptable"] else "sigue: cola_humana"


def costos(salida: Path) -> dict:
    g3 = n3 = g1 = n1 = 0.0
    for to in TOS:
        r = json.loads((salida / to / "resumen_e3.json").read_text(encoding="utf-8"))
        g3 += r["cliente_e3"]["gasto_usd_real"]
        n3 += r["cliente_e3"]["llamadas"]
        g1 += r["cliente_e1_reintentos"]["gasto_usd_real"]
        n1 += r["cliente_e1_reintentos"]["llamadas"]
    return {"e3_gasto": round(g3, 4), "e3_llamadas": int(n3), "e3_usd_por_llamada": round(g3 / n3, 6),
            "e1_reintento_gasto": round(g1, 4), "e1_reintento_llamadas": int(n1),
            "e1_reintento_usd_por_llamada": round(g1 / n1, 6)}


def ventanas(s: str) -> set[tuple[str, ...]]:
    t = V.norm_tokens(s or "")
    return {tuple(t[i:i + VENTANA]) for i in range(len(t) - VENTANA + 1)}


def norm(s) -> str:
    return " ".join(V.norm_tokens(str(s or "")))


def medir(nombre: str, salida: Path) -> dict:
    res: dict = {"corrida": str(salida.relative_to(REPO)), "j": {"unidades": []}, "k": {}}
    perdidas: dict = {"unidades": 0, "menos_entidades": 0, "menos_relaciones": 0, "menos_ambas": 0,
                      "con_entidad_sin_par": 0, "entidades_sin_par": 0, "relaciones_de_menos": 0, "casos": []}
    copias: list[dict] = []
    for to in TOS:
        tdir = salida / to
        chunks = {c["id"]: c for c in comun_e1.cargar_chunks((to,), e0_dir=E0)}
        unidades = {c["unidad"] for c in chunks.values()}
        fin = {r["chunk_id"]: r for r in jl(tdir / "finales.jsonl")}
        comp = {r["chunk_id"]: r for r in jl(tdir / "extracciones_e1_compact.jsonl")}
        ver: dict = {}
        for v in jl(tdir / "veredictos.jsonl"):
            ver[(v["chunk_id"], v["fase"], v["intento"])] = v
        for cid, f in sorted(fin.items()):
            ch = chunks.get(cid)
            # ---------------- j ----------------
            if f.get("validacion_final") is None:
                vs = sorted((v for k, v in ver.items() if k[0] == cid), key=lambda v: v["intento"])
                v = vs[-1]
                ti = v.get("tool_input") or {}
                if isinstance(ti, dict) and isinstance(ti.get("faltantes"), str):
                    lect = leer_faltantes(ti["faltantes"])
                    fila = {"chunk_id": cid, "estado_hoy": f["estado"], "fase": v["fase"],
                            "veredicto_arriba": ti.get("veredicto"), "veredicto_en_texto": lect["veredicto_en_texto"],
                            "lee_estricta": lect["estricta"] is not None, "lee_con_reparo": lect["reparo"] is not None}
                    for modo in ("estricta", "reparo"):
                        t2 = a_tool_input(ti, lect[modo])
                        if t2 is not None and modo == "reparo" and t2["veredicto"] is None:
                            t2["veredicto"] = lect["veredicto_en_texto"]
                        if t2 is None:
                            fila[f"estado_opcion1_{modo}"] = "sigue en la cola: no se lee"
                            continue
                        ev = ratchet_e3.evaluar_veredicto(t2, ch, unidades, None)
                        fila[f"estado_opcion1_{modo}"] = estado_con_politica(ev, v["fase"])
                        if modo == "reparo":
                            fila["veredicto_leido"] = t2["veredicto"]
                            fila["faltantes_leidos"] = len(t2["faltantes"]) if isinstance(t2["faltantes"], list) else None
                            fila["alta"] = sum(1 for x in (t2["faltantes"] or []) if isinstance(x, dict)
                                               and x.get("severidad") == "alta")
                            fila["bloqueantes_con_cita"] = len(ev["bloqueantes_utilizables"])
                    res["j"]["unidades"].append(fila)
            # ---------------- k ----------------
            if f["estado"] != "aceptado_tras_reintento":
                continue
            v1 = (comp.get(cid) or {}).get("validacion") or {}
            v2 = f["validacion_final"] or {}
            e1, e2 = v1.get("entidades") or [], v2.get("entidades") or []
            r1, r2 = v1.get("relaciones") or [], v2.get("relaciones") or []
            perdidas["unidades"] += 1
            me, mr = len(e2) < len(e1), len(r2) < len(r1)
            perdidas["menos_entidades"] += me
            perdidas["menos_relaciones"] += mr
            perdidas["menos_ambas"] += me and mr
            perdidas["relaciones_de_menos"] += max(0, len(r1) - len(r2))
            claves2 = {(e["type"], norm(e["label"])) for e in e2} | {
                (e["type"], norm((e.get("properties") or {}).get("descripcion"))) for e in e2}
            sin_par = [e for e in e1 if e["type"] != "TextoOrdenado"
                       and (e["type"], norm(e["label"])) not in claves2
                       and (e["type"], norm((e.get("properties") or {}).get("descripcion"))) not in claves2]
            if sin_par:
                perdidas["con_entidad_sin_par"] += 1
                perdidas["entidades_sin_par"] += len(sin_par)
            if me or mr:
                perdidas["casos"].append({"chunk_id": cid, "entidades": [len(e1), len(e2)],
                                          "relaciones": [len(r1), len(r2)], "entidades_sin_par": len(sin_par)})
            # copia de la nota: los faltantes que se le pasaron al reintento
            v0 = ver.get((cid, "verificacion", 0))
            if v0 is None:
                continue
            ev0 = ratchet_e3.evaluar_veredicto(v0["tool_input"], ch, unidades, None)
            notas = [x.get("nota") or "" for x in ev0["bloqueantes_utilizables"]]
            citas = " \n ".join(x.get("cita_textual_del_fuente") or "" for x in ev0["bloqueantes_utilizables"])
            prohibidas = ventanas(V.texto_completo(ch)) | ventanas(citas)
            de_la_nota = set().union(*(ventanas(n) for n in notas)) - prohibidas if notas else set()
            for e in e2:
                for campo, txt in (("descripcion", (e.get("properties") or {}).get("descripcion")),
                                   ("label", e.get("label"))):
                    comunes = ventanas(txt) & de_la_nota
                    if comunes:
                        copias.append({"chunk_id": cid, "local_id": e["local_id"], "type": e["type"], "campo": campo,
                                       "ventanas": sorted(" ".join(w) for w in comunes)[:5], "texto": txt,
                                       "notas": notas})
    j = res["j"]["unidades"]
    res["j"]["resumen"] = {
        "unidades": len(j), "por_estado_hoy": dict(Counter(x["estado_hoy"] for x in j)),
        "por_veredicto_leido": dict(Counter(str(x.get("veredicto_leido")) for x in j)),
        "lee_estricta": sum(x["lee_estricta"] for x in j), "lee_con_reparo": sum(x["lee_con_reparo"] for x in j),
        "opcion1_estricta": dict(Counter(x["estado_opcion1_estricta"] for x in j)),
        "opcion1_reparo": dict(Counter(x["estado_opcion1_reparo"] for x in j))}
    res["k"]["perdidas"] = perdidas
    res["k"]["copia_nota"] = {"regla": f"R-NORM, ventana de {VENTANA} tokens, en la nota y no en la unidad ni en las "
                                       "citas; descripción y etiqueta de cada entidad del reintento",
                              "unidades": sorted({c["chunk_id"] for c in copias}), "casos": copias}
    res["costos"] = costos(salida)
    return res


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo")
    out = {"comando": "data/experiment/prompt_r2/p3b/lazo_e3_p3b.py --salida DIR",
           "corridas": {k: medir(k, v) for k, v in CORRIDAS.items()}}
    sal.mkdir(parents=True, exist_ok=True)
    (sal / "lazo_e3_p3b.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    d = out["corridas"]["salida_dirigida"]["k"]["copia_nota"]
    md = ["# Copia de la nota de E3 en el reintento: los casos (salida_dirigida)", "", f"Regla: {d['regla']}.", "",
          f"{len(d['casos'])} casos en {len(d['unidades'])} unidades.", "",
          "| Unidad | Entidad | Campo | Ventanas en común | Texto de la entidad |", "|---|---|---|---|---|"]
    for c in d["casos"]:
        md.append(f"| `{c['chunk_id']}` | {c['local_id']} ({c['type']}) | {c['campo']} | "
                  f"{'; '.join(c['ventanas'])} | {str(c['texto']).replace('|', '/')[:160]} |")
    (sal / "copia_nota_casos.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    for k, r in out["corridas"].items():
        print(k, json.dumps(r["j"]["resumen"], ensure_ascii=False))
        p = r["k"]["perdidas"]
        print("   k", {x: y for x, y in p.items() if x != "casos"}, "copia_nota:", len(r["k"]["copia_nota"]["unidades"]),
              "unidades,", len(r["k"]["copia_nota"]["casos"]), "casos")
        print("   costos", r["costos"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
