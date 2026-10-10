"""U-OMISIONES-COD, O1 — grupo A, ítem e: el clasificador de la copia de la nota de E3 sobre el diez r2b (USD 0, sin
API ni Neo4j). Corre desde la raíz de una COPIA del repo.

  --modo calibrar  Sobre el conjunto de diseño (los 86 casos de las 64 unidades que leyó T4: lista_copia_nota_t4.json
                   y clasificacion_copia_nota_t4.json), el cruce de cada variante con la lectura de T4. Fuera de esas
                   64 unidades solo imprime cuentas: no muestra ninguna detección.
  --modo lista     Con la variante elegida, escribe la lista completa de detecciones (chunk_id, TO, entidad, campo,
                   texto y las palabras que la deciden) en --out, con la cuenta dentro y fuera de las 64 unidades, y
                   no imprime ninguna fila. La lectura de la precisión es de otra sesión (nota del 09/10/2026 a la v7).

Uso: PYTHONDONTWRITEBYTECODE=1 <python> -B <scripts>/medir_e.py --modo calibrar|lista [--variante V] --out <json>
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter, OrderedDict
from pathlib import Path

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parent))
import o1_comun as OC  # noqa: E402
import clasificador_copia_nota as CL  # noqa: E402

T4 = Path("data/experiment/reext_t0/t4/salida")
VARIANTES = OrderedDict([("palabra", (None, False, False)), ("palabra+primer_intento+flexion", (None, True, True))]
                        + [(f"ventana{n}{'+primer_intento' if fpi else ''}{'+flexion' if fl else ''}", (n, fpi, fl))
                           for n in (5, 4, 3) for fpi in (False, True) for fl in (False, True)])


def jl(p: Path) -> list[dict]:
    return [json.loads(x) for x in p.read_text(encoding="utf-8").splitlines() if x.strip()] if p.exists() else []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--modo", choices=("calibrar", "lista"), required=True)
    ap.add_argument("--variante", choices=tuple(VARIANTES), default=None)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    p3b2 = str(Path("data/experiment/prompt_r2/p3b2").resolve())
    sys.path.insert(0, p3b2)
    import lista_copia_nota as L0  # noqa: PLC0415 — VACIAS y METALENGUAJE de la regla de lectura
    assert Path(L0.__file__).resolve().is_relative_to(OC.raiz_copia())
    ENS, man, perfil, plan, M, V, RCMP, RC = OC.contexto("diez")
    with ENS.redirigido(plan):
        regs, chunks = OC.registros(ENS, perfil, RC, con_cola=True)
        salida = Path(ENS.C.SALIDA)
    t4 = json.loads((T4 / "lista_copia_nota_t4.json").read_text(encoding="utf-8"))["casos"]
    cls = json.loads((T4 / "clasificacion_copia_nota_t4.json").read_text(encoding="utf-8"))
    clases_t4 = {c["n"]: c["clase"] for c in (cls.get("casos") or cls.get("clasificacion") or [])}
    unidades64 = sorted({c["chunk_id"] for c in t4})
    # población: unidades aceptadas tras reintento, con sus notas, citas y primer intento
    filas = {v: [] for v in VARIANTES}
    pobl = Counter()
    for to in regs:
        fin = {r["chunk_id"]: r for r in jl(salida / to / "finales.jsonl")}
        ver = jl(salida / to / "veredictos.jsonl")
        e1 = {r["chunk_id"]: r for r in jl(salida / to / "extracciones_e1_compact.jsonl")}
        por_chunk = {}
        for v in ver:
            por_chunk.setdefault(v["chunk_id"], []).append(v)
        for r in regs[to]:
            f = fin.get(r["chunk_id"])
            if not f or f["estado"] != CL.ESTADO_POBLACION or not r.get("validacion"):
                continue
            n = f.get("n_reintentos") or 0
            previa = [v for v in por_chunk.get(r["chunk_id"], []) if v.get("intento") == n - 1][-1:]
            notas = [x.get("nota") or "" for v in previa for x in (v.get("faltantes") or [])]
            citas = [x.get("cita_textual_del_fuente") or "" for v in previa for x in (v.get("faltantes") or [])]
            primer = ((e1.get(r["chunk_id"]) or {}).get("tool_input_crudo") or {}).get("entities") or []
            ctx = CL.contexto_unidad(chunks[r["chunk_id"]], notas, citas, primer, V)
            pobl["unidades"] += 1
            pobl["unidades_dentro_de_las_64"] += r["chunk_id"] in unidades64
            for e in r["validacion"].get("entidades", []):
                for campo, texto in CL.campos_de_entidad(e):
                    pobl["campos"] += 1
                    for nom, (nv, fpi, flex) in VARIANTES.items():
                        c = (CL.clasificar_campo(texto, ctx, V, L0.VACIAS, L0.METALENGUAJE, fpi, flex) if nv is None
                             else CL.clasificar_campo_ventana(texto, ctx, V, L0.VACIAS, L0.METALENGUAJE, nv, fpi, flex))
                        if c["clase"] is not None:
                            filas[nom].append({"chunk_id": r["chunk_id"], "to": to, "local_id": e.get("local_id"),
                                               "type": e.get("type"), "campo": campo, "texto": texto, **c,
                                               "dentro_de_las_64_de_T4": r["chunk_id"] in unidades64})
    res = OrderedDict([("poblacion", dict(pobl)), ("unidades_T4", len(unidades64)), ("casos_T4", len(t4)),
                       ("clases_T4", dict(Counter(clases_t4.values())))])
    cuentas = OrderedDict()
    for nom, fs in filas.items():
        cuentas[nom] = {"detecciones": len(fs), "dentro_de_las_64": sum(f["dentro_de_las_64_de_T4"] for f in fs),
                        "fuera_de_las_64": sum(not f["dentro_de_las_64_de_T4"] for f in fs),
                        "unidades_fuera": len({f["chunk_id"] for f in fs if not f["dentro_de_las_64_de_T4"]}),
                        "por_clase": dict(Counter(str(f["clase"]) for f in fs))}
    res["cuentas_por_variante"] = cuentas
    if a.modo == "calibrar":
        cal = OrderedDict()
        for nom, fs in filas.items():
            det = {(f["chunk_id"], f["local_id"], f["campo"]) for f in fs}
            cru = Counter()
            for c in t4:
                k = (c["chunk_id"], c["local_id"], c["campo"])
                cru[f"{clases_t4.get(c['n'])}|{'detectado' if k in det else 'no_detectado'}"] += 1
            tp = cru["copia real|detectado"]
            fp = cru["coincidencia legítima|detectado"] + cru["dudosa|detectado"]
            cal[nom] = {"cruce_con_los_86": dict(sorted(cru.items())),
                        "precision_en_los_86": f"{tp}/{tp + fp}", "wilson": OC.wilson(tp, tp + fp),
                        "cobertura_de_las_copias_reales": f"{tp}/{sum(1 for v in clases_t4.values() if v == 'copia real')}",
                        "detecciones_en_las_64_fuera_de_los_86": sum(
                            1 for f in fs if f["dentro_de_las_64_de_T4"]
                            and (f["chunk_id"], f["local_id"], f["campo"]) not in
                            {(c["chunk_id"], c["local_id"], c["campo"]) for c in t4})}
        res["calibracion_T4"] = cal
        res["casos_T4_por_variante"] = {nom: [{"n": c["n"], "clase_T4": clases_t4.get(c["n"]),
                                               "detectado": (c["chunk_id"], c["local_id"], c["campo"]) in
                                               {(f["chunk_id"], f["local_id"], f["campo"]) for f in fs}}
                                              for c in t4] for nom, fs in filas.items()}
        sha = OC.escribir_json(a.out, res)
        print(json.dumps({k: v for k, v in res.items() if k != "casos_T4_por_variante"}, ensure_ascii=False, indent=1))
        print("sha256", sha)
        return 0
    lista = filas[a.variante]
    res["variante"] = a.variante
    res["detecciones"] = lista
    sha = OC.escribir_json(a.out, res)
    print(json.dumps({"variante": a.variante, **cuentas[a.variante]}, ensure_ascii=False))
    print("sha256", sha)
    return 0


if __name__ == "__main__":
    sys.exit(main())
