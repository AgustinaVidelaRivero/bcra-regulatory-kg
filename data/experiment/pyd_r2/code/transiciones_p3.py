"""
transiciones_p3.py — U-PYD, etapa P3: qué cambia con la calibración de las
reglas de comparación y del validador (decisiones de la autora sobre P2).

1. Comparación, cuantía por cuantía: sobre la población del par B (nodos
   Restriccion, Condicion, Obligacion y Excepcion con cuantía [c14] en los
   grafos r1, desarrollo, cinco y diez; la de mediciones_p2.py), las reglas de
   P2 (reglas_comparacion.py en b706d37, leído con `git show` y candado de
   sha256, ejecutado en memoria sin escribir archivos) contra las de P3. Las
   cuantías son las mismas (el detector no cambió; se verifica span por span).
2. Validador: contadores de la corrida sobre el crudo de P2
   (resultados/prueba_crudo_t0.json en b706d37) contra los de P3 (el mismo
   archivo, re-generado): mención por nivel, omisiones, adaptación del crudo
   v3, rechazos y controles C1 a C3.

Correr después de prueba_crudo_t0.py. Escribe resultados/transiciones_p3.json
y .md (o en --salida), sin fechas ni rutas absolutas.

Uso (desde la raíz del repo):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/transiciones_p3.py
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

AQUI = Path(__file__).resolve().parent
if str(AQUI) not in sys.path:
    sys.path.insert(0, str(AQUI))
import modelos_r2 as M  # noqa: E402
import reglas_comparacion as RC  # noqa: E402
import lector_crudo_v3 as L  # noqa: E402
import mediciones_p2 as MP  # noqa: E402

REPO = M.REPO
SALIDA = M.PYD_R2 / "resultados"
COMANDO = "PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/pyd_r2/code/transiciones_p3.py"
COMMIT_P2 = "b706d37"
REGLAS_P2 = "data/experiment/pyd_r2/code/reglas_comparacion.py"
REGLAS_P2_SHA = "213ab140aa2953affa5081f379cede985b985e21c5cce6affc66553ce8d3aaaf"
PRUEBA_P2 = "data/experiment/pyd_r2/resultados/prueba_crudo_t0.json"
PRUEBA_P2_SHA = "a00e97c19b970a29294f2b8d94a65e723816d02f73cf905d938811ff9fc3fd71"
GRUPOS_DETALLE = ("diez", "r1")


def reglas_p2():
    """El módulo de reglas de P2, ejecutado desde el contenido del commit."""
    src = L.leer_firmado(COMMIT_P2, REGLAS_P2, REGLAS_P2_SHA).decode("utf-8")
    nombre = "reglas_comparacion_p2"
    spec = importlib.util.spec_from_loader(nombre, loader=None)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[nombre] = mod  # las dataclasses lo buscan en sys.modules
    exec(compile(src, f"{COMMIT_P2}:{REGLAS_P2}", "exec"), mod.__dict__)
    return mod


def transiciones(crudo, viejo) -> dict:
    out = OrderedDict()
    for g in ("r1", "desarrollo", "cinco", "diez"):
        kg = json.loads(crudo._verificado(f"{g}_kg.json").decode("utf-8"))
        nodos = sorted((n for n in kg["nodes"] if n["type"] in MP.TIPOS_CUANTIA
                        and MP.tiene_c14((n.get("properties") or {}).get("descripcion"))), key=lambda n: n["id"])
        trans, por_regla, cambios = Counter(), Counter(), []
        antes_c, despues_c = Counter(), Counter()
        asumida = Counter()
        n_cuantias = 0
        for n in nodos:
            d = n["properties"]["descripcion"]
            t = MP._titulo(n, crudo.chunks)
            a, b = viejo.analizar(d, d, t), RC.analizar(d, d, t)
            if [(x.inicio, x.fin) for x in a] != [(x.inicio, x.fin) for x in b]:
                raise L.FrenoLectura(f"{g}: las cuantías de {n['id']} cambiaron entre P2 y P3")
            for x, y in zip(a, b):
                n_cuantias += 1
                antes_c[x.comparacion] += 1
                despues_c[y.comparacion] += 1
                asumida[(x.comparacion_asumida, y.comparacion_asumida)] += 1
                if x.comparacion != y.comparacion or x.regla != y.regla:
                    trans[(x.comparacion, y.comparacion)] += 1
                    por_regla[(x.regla, y.regla)] += 1
                    if g in GRUPOS_DETALLE:
                        cambios.append({"id": n["id"], "cuantia": y.texto, "antes": [x.comparacion, x.regla],
                                        "despues": [y.comparacion, y.regla], "ventana": y.ventana})
        out[g] = {
            "nodos": len(nodos), "cuantias": n_cuantias,
            "cambian_de_comparacion": sum(v for (a, b), v in trans.items() if a != b),
            "cambian_solo_de_regla": sum(v for (a, b), v in trans.items() if a == b),
            "transiciones_comparacion": [{"antes": a, "despues": b, "n": v}
                                         for (a, b), v in sorted(trans.items(), key=lambda kv: (-kv[1], kv[0]))],
            "transiciones_regla": [{"antes": a, "despues": b, "n": v}
                                   for (a, b), v in sorted(por_regla.items(), key=lambda kv: (-kv[1], kv[0]))],
            "comparacion_antes": dict(sorted(antes_c.items())), "comparacion_despues": dict(sorted(despues_c.items())),
            "comparacion_asumida_antes": sum(v for (a, _), v in asumida.items() if a),
            "comparacion_asumida_despues": sum(v for (_, b), v in asumida.items() if b),
            "cambios": cambios,
        }
    return out


def validador() -> dict:
    viejo = json.loads(L.leer_firmado(COMMIT_P2, PRUEBA_P2, PRUEBA_P2_SHA).decode("utf-8"))
    nuevo = json.loads((REPO / PRUEBA_P2).read_text(encoding="utf-8"))
    filas = OrderedDict()
    for g in viejo["grupos"]:
        for capa in viejo["grupos"][g]:
            a, b = viejo["grupos"][g][capa], nuevo["grupos"][g][capa]
            d = OrderedDict()
            for campo in ("sujeto_mencion", "omisiones", "coherencia_tipo_predicado"):
                ca, cb = a["contadores"].get(campo, {}), b["contadores"].get(campo, {})
                dif = {k: [ca.get(k, 0), cb.get(k, 0)] for k in sorted(set(ca) | set(cb)) if ca.get(k, 0) != cb.get(k, 0)}
                if dif:
                    d[campo] = dif
            aa, ab = a["adaptacion_v3"], b["adaptacion_v3"]
            dif = {k: [aa.get(k, 0), ab.get(k, 0)] for k in sorted(set(aa) | set(ab)) if aa.get(k, 0) != ab.get(k, 0)}
            if dif:
                d["adaptacion_v3"] = dif
            ra, rb = a["rechazos_por_motivo"], b["rechazos_por_motivo"]
            dif = {k: [ra.get(k, 0), rb.get(k, 0)] for k in sorted(set(ra) | set(rb)) if ra.get(k, 0) != rb.get(k, 0)}
            if dif:
                d["rechazos_por_motivo"] = dif
            pa, pb = a["pendientes_no_mapeados_por_motivo"], b["pendientes_no_mapeados_por_motivo"]
            dif = {k: [pa.get(k, 0), pb.get(k, 0)] for k in sorted(set(pa) | set(pb)) if pa.get(k, 0) != pb.get(k, 0)}
            if dif:
                d["pendientes_no_mapeados"] = dif
            filas[f"{g}|{capa}"] = d
    C = nuevo["controles"]
    controles = {
        "c1_todos_iguales_a_n1": all(v["fuera_igual_a_n1"] and v["totales_igual_a_resumen_por_lista"]
                                     for v in C["c1_fuera_de_lista_contra_n1"].values()),
        "reconciliacion_filas_n1_que_cierran": [sum(1 for f in C["reconciliacion"] if f["origen"] == "n1" and f["cierra"]),
                                                sum(1 for f in C["reconciliacion"] if f["origen"] == "n1")],
        "c2_A_coincide": all(x["coincide"] for d in C["c2_matriz"]["A"].values() for x in d.values()),
        "c2_B_coincide": all(x["coincide"] for d in C["c2_matriz"]["B"].values() for x in d["por_par"].values()),
        "c3_perdidos": sum(len(v["perdidos"]) for v in C["c3_sin_perdidas"].values()),
        "c3_omisiones_v3_contra_r2": {k: [v["omisiones_v3"], v["omisiones_r2_desde_v3"]]
                                      for k, v in C["c3_sin_perdidas"].items()
                                      if v["omisiones_v3"] != v["omisiones_r2_desde_v3"]},
        "c4_coincide": all(v["coincide"] for v in C["c4_bkl_0038_poblacion_final_vs_grafo"].values()),
    }
    return {"diferencias_por_grupo_y_capa": filas, "controles_p3": controles,
            "politica_p2": viejo["politica"]["sha256"], "politica_p3": nuevo["politica"]["sha256"]}


def _t(filas, cab):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for f in filas:
        out.append("| " + " | ".join(str(x) for x in f) + " |")
    return out


def escribir_md(J: dict) -> str:
    L_ = ["# U-PYD P3 — transiciones por la calibración", "", f"Comando: `{J['comando']}`.", "",
          f"Reglas de P2: `{REGLAS_P2}` en `{COMMIT_P2}` (sha256 `{REGLAS_P2_SHA[:12]}…`), ejecutadas en memoria.", "",
          "## 1. Comparación de las cuantías ([c14], descripciones de los grafos)", ""]
    T = J["comparacion"]
    L_ += _t([[g, d["nodos"], d["cuantias"], d["cambian_de_comparacion"], d["cambian_solo_de_regla"],
               d["comparacion_asumida_antes"], d["comparacion_asumida_despues"]] for g, d in T.items()],
             ["grafo", "nodos", "cuantías", "cambian de comparación", "cambian solo de regla",
              "comparacion_asumida antes", "después"]) + [""]
    for g, d in T.items():
        L_ += [f"### {g}: hacia dónde", ""]
        L_ += _t([[x["antes"], x["despues"], x["n"]] for x in d["transiciones_comparacion"]],
                 ["comparación P2", "comparación P3", "cuantías"]) + [""]
        L_ += _t([[x["antes"], x["despues"], x["n"]] for x in d["transiciones_regla"]],
                 ["regla P2", "regla P3", "cuantías"]) + [""]
    for g in GRUPOS_DETALLE:
        L_ += [f"### {g}: cuantías que cambian", ""]
        L_ += _t([[x["id"][:60], x["cuantia"], " / ".join(x["antes"]), " / ".join(x["despues"]),
                   x["ventana"].replace("|", "/")[:140]] for x in T[g]["cambios"]],
                 ["nodo", "cuantía", "P2", "P3", "ventana"]) + [""]
    V_ = J["validador"]
    L_ += ["## 2. Validador sobre el crudo (prueba_crudo_t0.json, P2 contra P3)", "",
           f"Política: P2 `{V_['politica_p2'][:12]}…`, P3 `{V_['politica_p3'][:12]}…`.", ""]
    filas = []
    for k, d in V_["diferencias_por_grupo_y_capa"].items():
        for campo, dif in d.items():
            for clave, (a, b) in dif.items():
                filas.append([k, campo, clave, a, b])
    L_ += _t(filas, ["grupo|capa", "campo", "clave", "P2", "P3"]) + [""]
    L_ += ["Controles en P3: " + ", ".join(f"{k} = {v}" for k, v in V_["controles_p3"].items()) + ".", ""]
    return "\n".join(L_) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", default=str(SALIDA))
    out = Path(ap.parse_args().salida)
    out.mkdir(parents=True, exist_ok=True)
    crudo = L.Crudo()
    viejo = reglas_p2()
    J = {"unidad": "U-PYD", "etapa": "P3", "comando": COMANDO,
         "reglas_p2": {"ruta": REGLAS_P2, "commit": COMMIT_P2, "sha256": REGLAS_P2_SHA},
         "comparacion": transiciones(crudo, viejo), "validador": validador()}
    b_json = (json.dumps(J, ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    b_md = escribir_md(J).encode("utf-8")
    for nombre, b in (("transiciones_p3.json", b_json), ("transiciones_p3.md", b_md)):
        (out / nombre).write_bytes(b)
        print(f"{hashlib.sha256(b).hexdigest()}  {nombre}")


if __name__ == "__main__":
    main()
