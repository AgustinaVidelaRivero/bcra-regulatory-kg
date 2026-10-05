"""
t1_propuesta_entrada_r2b.py — U-REEXT-T0, T1, punto 5 (mandato firmado en e2027dd): la entrada de la suite para los
dos grafos r2b (diez y desarrollo), el estado esperado ítem por ítem, PROPUESTA para que la autora la selle antes del
gate de T3 (laudo de r2, §3.1, punto 2). No se escribe en scripts/regression_kg_esperado.json: eso lo hace la autora.

Base: los estados medidos con el código de T1 sobre los grafos r2a (KG-Tanda0-Diez-r2a, 99fe2bfa…, y
KG-Tanda0-Desarrollo-r2a, 93a7af72…), que pasa por --suite-diez y --suite-desarrollo (salidas .json de
scripts/regression_kg.py --perfil r2). Cada ítem lleva:
  - el estado propuesto para r2b en cada grafo;
  - la clase: «código o catálogo» (lo fija el código o el catálogo, no la extracción: r2b da lo mismo que r2a),
    «dirigido por r2b» (la extracción de r2b apunta a ese defecto: el propuesto es el que busca la release) o
    «extracción, no dirigido» (depende de la extracción y r2b no apunta a él: el propuesto es el de r2a);
  - la razón, con su ancla.
Un ítem de extracción puede cambiar por la variación del modelo (FRENO P5 de U-PROMPT-R2: 6 de 27 respuestas iguales
entre dos corridas): la clase lo marca para que la autora decida si lo sella con estado o en null (NO VERIFICADA).

Escribe en --salida (fuera de la copia): entrada_suite_r2b_propuesta.json y .md.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t1_propuesta_entrada_r2b.py \
      --suite-diez DIR/suite_KG-Tanda0-Diez-r2a_despues.json --suite-desarrollo DIR/suite_KG-Tanda0-Desarrollo-r2a_despues.json \
      --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

COD, DIR, EXT = "código o catálogo", "dirigido por r2b", "extracción, no dirigido"
R2A = "como en r2a"
# ítem → (clase, propuesto en diez, propuesto en desarrollo, razón). R2A = el estado medido en r2a en ese grafo.
PROPUESTA = {
    "BKL-0017": (EXT, R2A, R2A, "criterio general de cla 1.1: r2b no apunta a él"),
    "BKL-0006": (DIR, "resuelto", "resuelto", "la tabla de cap::1.2 va serializada en el mensaje (e0-r2); con el prefijo "
                 "nuevo, P4 la copió bien (data/experiment/prompt_r2/freno_p4.md:77; una corrida)"),
    "BKL-0023": (DIR, "resuelto", "resuelto", "el monto de bancos sale de la misma tabla de cap::1.2 (BKL-0006)"),
    "BKL-0019": (EXT, R2A, R2A, "padre_sugerido de los propuestos: depende de qué propuestos deje la extracción"),
    "BKL-0004": (EXT, R2A, R2A, "FALLA CONOCIDA (mandato, T1, punto 5): la enumeración del 6.5 de Clasificación persiste "
                 "en r2a sin corrección dirigida; si persiste en r2b, entra como falla conocida con su evidencia (el "
                 "detalle de la suite: nodos 8 de 9, N3 del 6.5.2 ausente, regula 0 de 8)"),
    "BKL-0003": (EXT, R2A, R2A, "la Excepcion de mutuales sin exceptua_obligacion; P3b sumó la Excepcion conectada, sin "
                 "medición sobre este punto"),
    "BKL-0005": (EXT, R2A, R2A, "calificadores del 7.1 de ric, presentes en r2a"),
    "BKL-0007": (EXT, R2A, R2A, "= BKL-0017"),
    "BKL-0026": (COD, R2A, R2A, "no convertible (conducta del agente)"),
    "BKL-0027": (COD, R2A, R2A, "no convertible (conducta del agente)"),
    "BKL-0028": (COD, R2A, R2A, "catálogo r2 (bd2122d)"),
    "BKL-0029": (COD, R2A, R2A, "catálogo r2 y esqueleto"),
    "RT-C5-1": (EXT, R2A, R2A, "niveles del 6.5 (ver BKL-0004)"),
    "RT-C5-2": (EXT, R2A, R2A, "N3 del 6.5.2 (ver BKL-0004)"),
    "RT-C5-3": (EXT, R2A, R2A, "presente en r2a"),
    "RT-C5-4": (EXT, R2A, R2A, "tratamiento especial, gold 1 de 3 en r2a"),
    "RT-C5-5": (COD, R2A, R2A, "sin nodos con punto 7.2: falla por ancla de E0"),
    "RT-C6-1": (EXT, R2A, R2A, "salvedad de mutuales, presente en r2a"),
    "RT-C6-2": (EXT, R2A, R2A, "= RT-C6-1"),
    "RT-C6-5": (EXT, R2A, R2A, "cláusula «por las financiaciones que otorguen», ausente en r2a"),
    "RT-C6-3": (COD, R2A, R2A, "miembros del rol en el esqueleto"),
    "RT-C6-4": (EXT, R2A, R2A, "emisoras en el rol de pro"),
    "RT-C7-1": (EXT, R2A, R2A, "presente en r2a"),
    "RT-C7-2": (EXT, R2A, R2A, "presente en r2a"),
    "RT-C7-3": (EXT, R2A, R2A, "presente en r2a"),
    "T1": (EXT, R2A, R2A, "BKL-0024, presente en r2a"),
    "T2": (EXT, R2A, R2A, "125 % en cinco nodos de ext, presente en r2a"),
    "T3": (EXT, R2A, R2A, "salvedad de 1.1.2.5, presente en r2a"),
    "T4": (COD, R2A, R2A, "esqueleto del catálogo (R-T4)"),
    "T5": (EXT, R2A, R2A, "R-T5, 25 de 30 en r2a; remite_a depende de los nodos de cada punto"),
    "T6": (COD, R2A, R2A, "un TextoOrdenado por TO del manifiesto (punto 4.a)"),
    "T7": (EXT, R2A, R2A, "cuarentena flaggeada de los propuestos"),
    "I1": (COD, R2A, R2A, "no convertible"),
    "I2": (COD, R2A, R2A, "no convertible"),
    "I3": (COD, R2A, R2A, "invariantes del ensamblado"),
    "I4": (COD, R2A, R2A, "invariantes del ensamblado"),
    "I5": (COD, R2A, R2A, "invariantes del ensamblado"),
    "E4-a1": (COD, R2A, R2A, "resolución de propuestos en código"), "E4-a2": (COD, R2A, R2A, "ídem"),
    "E4-a3": (COD, R2A, R2A, "ídem"), "E4-a4": (COD, R2A, R2A, "ídem"), "E4-a5": (COD, R2A, R2A, "ídem"),
    "E4-a6": (COD, R2A, R2A, "ídem"), "E4-a7": (COD, R2A, R2A, "ídem"),
    "E4-a8": (COD, R2A, R2A, "el perfil r2 no deja e4_propuestos.json"),
    "E4-b": (COD, R2A, R2A, "= T6 más properties.archivo (punto 4.a)"),
    "E4-c": (COD, R2A, R2A, "no observable sobre un kg.json"),
    "EJ-cla-5.1.1.1": (DIR, "resuelto", "resuelto", "el ejemplo salió completo en las dos corridas de P5 con temperatura 0 "
                       "(data/experiment/prompt_r2/freno_p5.md, §5.c); si el nodo no sale, la condición 10 vuelve a la "
                       "autora (mandato, T3, 3.c)"),
    "LN-1": (COD, R2A, R2A, "listas cerradas con marca fuera_de_lista, en código"),
    "LN-2": (COD, R2A, R2A, "claves cerradas por tipo, en código"),
    "LN-3": (DIR, "resuelto", "resuelto", "en r2b E1 emite la mención de cada relación de sujeto; persiste en r2a hasta la "
             "mención de E1 de r2b (P-b1; scripts/regression_kg.py, nota de LN-3)"),
    "LN-4": (COD, R2A, R2A, "método de resolución, en código"),
    "LN-5": (COD, R2A, R2A, "registro de no mapeados ↔ grafo, en código"),
    "LN-6": (COD, R2A, R2A, "re-resolución idempotente, en código"),
    "LN-7": (DIR, "resuelto", "resuelto", "el ensamblado r2b escribe omisiones.jsonl (punto p de C2); las omisiones con "
             "categoría y tramo son de r2b (L-ESQ-R2 §5.4)"),
    "LN-8": (COD, R2A, R2A, "bloque del prompt = JSON único del catálogo"),
    "BKL-0001": (EXT, R2A, R2A, "test por punto (4.f): resuelto en r2a"),
    "BKL-0002": (EXT, R2A, R2A, "test por punto (4.f): resuelto en r2a"),
    "FIRMAS-condicion_de": (DIR, "resuelto", "resuelto", "en r2b E3 verifica las relaciones nuevas: 0 no verificadas en el "
                            "grafo de la release (L-ESQ-R2 §6.4 y §6.5)"),
    "SIN-VERIF-E3": (DIR, "resuelto", "resuelto", "con r2b solo entra al grafo lo que pasó por E3, con la cola humana "
                     "aparte (FRENO P3 de U-PROMPT-R2, A2 a A5)"),
    "ID-entidad_financiera_del_exterior": (COD, R2A, R2A, "catálogo; en la tanda 0 el colectivo es solo contraparte"),
    "ID-banco_del_exterior": (COD, R2A, R2A, "ídem"),
    "ID-entidad_cambiaria_del_exterior": (COD, R2A, R2A, "catálogo; sin mención en la tanda 0"),
    "ID-titular_de_cuenta_corriente_en_el_bcra": (COD, R2A, R2A, "catálogo y esqueleto (rol de convca)"),
    "ID-instancia_de_gobierno_societario": (COD, R2A, R2A, "catálogo y esqueleto"),
    "ID-directorio": (DIR, "resuelto", R2A, "en r2b el bloque del catálogo del prefijo trae el id (L-ESQ-R2 §7.4) y E1 "
                      "emite la mención; condición de cierre de BKL-0034 (lingob::2.3.2::intro); en desarrollo no hay lingob"),
    "ID-alta_gerencia": (DIR, "resuelto", R2A, "ídem (lingob 3.1); en desarrollo no hay lingob"),
    "ID-comite_de_auditoria": (DIR, "resuelto", R2A, "ídem (lingob 4.1 y 5.1.4); en desarrollo no hay lingob"),
}


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--suite-diez", type=Path, required=True)
    ap.add_argument("--suite-desarrollo", type=Path, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    a = ap.parse_args()
    base = {g: json.loads(p.read_text(encoding="utf-8")) for g, p in (("diez", a.suite_diez), ("desarrollo", a.suite_desarrollo))}
    medido = {g: {it["id"]: it["estado"] for it in d["items"]} for g, d in base.items()}
    ids = [it["id"] for it in base["diez"]["items"]]
    if set(ids) != set(PROPUESTA) or set(medido["desarrollo"]) != set(PROPUESTA):
        raise SystemExit(f"ítems sin propuesta o de más: {sorted(set(ids) ^ set(PROPUESTA))}")
    entradas = {}
    for g, nombre in (("diez", "KG-Tanda0-Diez-r2b"), ("desarrollo", "KG-Tanda0-Desarrollo-r2b")):
        items = {}
        for i in ids:
            clase, p_diez, p_des, razon = PROPUESTA[i]
            p = p_diez if g == "diez" else p_des
            est = medido[g][i] if p == R2A else p
            items[i] = {"estado": est, "clase": clase, "r2a_medido": medido[g][i],
                        "cambia_respecto_de_r2a": est != medido[g][i], "razon": razon}
        par = base[g]["parametros"]
        entradas[nombre] = {
            "_rotulo": "PROPUESTA de U-REEXT-T0, T1, punto 5 (sin sellar): la sella la autora antes del gate de T3",
            "kg": f"data/experiment/reextraccion_v2/corpus_tanda0/ens_{g}_r2b/r2/kg.json",
            "kg_sha256": None, "_kg_sha256": "se completa en T3 con el sha256 del ensamblado r2b (doble corrida)",
            "generacion": 3, "politica_cuarentena": "flaggeada", "perfil": "r2",
            "catalogo": par["catalogo"], "catalogo_sha256": par["catalogo_sha256"],
            "base_r2a": {"kg": par["kg"], "kg_sha256": par["kg_sha256"], "resumen": base[g]["resumen"]},
            "items": items}
    out = {"unidad": "U-REEXT-T0, T1, punto 5", "mandato": "docs/mandatos/UREEXT_T0_reextraccion_tanda0.md (e2027dd)",
           "suite": "scripts/regression_kg.py con el código de T1", "entradas": entradas,
           "insumos": {"suite_diez": {"archivo": a.suite_diez.name, "sha256": sha(a.suite_diez)},
                       "suite_desarrollo": {"archivo": a.suite_desarrollo.name, "sha256": sha(a.suite_desarrollo)}}}
    a.salida.mkdir(parents=True, exist_ok=True)
    (a.salida / "entrada_suite_r2b_propuesta.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                                                              encoding="utf-8")
    L = ["# Entrada de la suite para los grafos r2b — PROPUESTA (U-REEXT-T0, T1, punto 5)", "",
         "Sin sellar: la sella la autora antes del gate de T3. `kg_sha256` se completa en T3. Base: estados medidos con "
         "el código de T1 sobre KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a. Clases: «código o catálogo» (r2b da lo "
         "mismo que r2a), «dirigido por r2b» (el propuesto es el que busca la release), «extracción, no dirigido» (el "
         "propuesto es el de r2a; puede cambiar por la variación del modelo).", ""]
    for nombre, ent in entradas.items():
        c = {}
        for v in ent["items"].values():
            c[v["estado"]] = c.get(v["estado"], 0) + 1
        L += [f"## {nombre}", "", f"Propuesto: {len(ent['items'])} ítems, {dict(sorted(c.items()))}; base r2a "
              f"{ent['base_r2a']['resumen']}.", "", "| Ítem | Propuesto | r2a | Clase | Razón |", "|---|---|---|---|---|"]
        for i, v in ent["items"].items():
            marca = " **(cambia)**" if v["cambia_respecto_de_r2a"] else ""
            L.append(f"| {i} | {v['estado']}{marca} | {v['r2a_medido']} | {v['clase']} | {v['razon']} |")
        L.append("")
    (a.salida / "entrada_suite_r2b_propuesta.md").write_text("\n".join(L), encoding="utf-8")
    for nombre, ent in entradas.items():
        c = {}
        for v in ent["items"].values():
            c[v["estado"]] = c.get(v["estado"], 0) + 1
        print(nombre, dict(sorted(c.items())), "cambian:", [i for i, v in ent["items"].items() if v["cambia_respecto_de_r2a"]])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
