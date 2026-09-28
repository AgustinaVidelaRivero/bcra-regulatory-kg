"""U-ESTUDIO-MATRIZ, paso 5 — muestra complementaria para los dos pares que
concentran el efecto (solo lectura, sin API).

Estratos y tamaños (hasta 30 filas por par sumando la muestra M01–M60):
  Condicion --condicion_de--> Operacion: +20
  Condicion --condicion_de--> Potestad:  +25
Procedimiento (el del paso 3): por estrato, filas de p4_filas.json del par,
ordenadas por (to, chunk_id, idx), EXCLUIDAS las ya sorteadas en M01–M60
(clave (to, chunk_id, idx) tomada de la copia commiteada de
uestmat_paso3_muestra.json, verificada contra la de este directorio);
random.Random(20260929).sample(lista, k) con una instancia nueva por estrato.
Orden de filas: estratos en el orden de arriba; dentro de cada estrato, las
sorteadas por (to, chunk_id, idx); ids C01–C45 en ese orden.
Columnas y constructor de fila: los del paso 3. Control: el mismo
constructor, aplicado a la traza de M01–M60, reproduce campo a campo el CSV
commiteado de la muestra de 60.
Salidas: uestmat_muestra_complementaria.csv (UTF-8 con BOM, veredicto y nota
vacíos) y uestmat_muestra_complementaria.json (procedimiento, conteos, clave
de cada fila). La salida estándar solo muestra conteos y controles.
"""
from __future__ import annotations

import csv
import hashlib
import json
import random
from pathlib import Path

import uestmat_comun as U

OUT = Path("/tmp/u_estudio_matriz")
SELLADO = U.REPO / "reports" / "u_estudio_matriz"
SEMILLA = 20260929
ESTRATOS = (("Condicion --condicion_de--> Operacion", 20),
            ("Condicion --condicion_de--> Potestad", 25))


def par_str(s, p, t):
    return f"{s} --{p}--> {t}"


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


class Constructor:
    """Constructor de fila del paso 3 (mismas columnas, mismas fuentes)."""

    def __init__(self):
        self.e1 = {to: U.leer_jsonl(U.SALIDA / to / "extracciones_e1.jsonl") for to in U.TOS_10}
        self.chunks = {to: {c["id"]: c for c in U.cargar_chunks(to)} for to in U.TOS_10}
        self.labels_cat = U.perfil_v3().labels_catalogo

    def fila(self, mid: str, h: str, f: dict) -> dict:
        d = self.e1[f["to"]][f["linea"] - 1]
        assert d["chunk_id"] == f["chunk_id"]
        cr = d["tool_input_crudo"]
        rel = cr["relations"][f["idx"]]
        ents = {e["local_id"]: e for e in cr["entities"]}
        src = ents[rel["source"]]
        if f["predicado"] == "aplica_a":
            sid = rel.get("sujeto_id") or rel.get("sujeto_propuesto")
            dst = {"type": "Sujeto", "label": sid, "properties": {}}
            assert rel.get("sujeto_id") is None or rel["sujeto_id"] in self.labels_cat
        else:
            dst = ents[rel["target"]]
        assert (src["type"], rel["predicate"], dst["type"]) == (f["origen"], f["predicado"], f["destino"])
        ch = self.chunks[f["to"]][f["chunk_id"]]
        return {
            "id_muestra": mid,
            "par": h,
            "chunk_id": f["chunk_id"],
            "texto_fragmento_e0": U.texto_completo(ch),
            "origen_tipo": src["type"],
            "origen_etiqueta": src.get("label", ""),
            "origen_descripcion": (src.get("properties") or {}).get("descripcion", ""),
            "predicado": rel["predicate"],
            "destino_tipo": dst["type"],
            "destino_etiqueta": dst.get("label", ""),
            "destino_descripcion": (dst.get("properties") or {}).get("descripcion", ""),
            "veredicto": "",
            "nota": "",
        }


def main() -> None:
    ctrl: dict = {}
    # Muestra previa: copia commiteada, verificada contra la de este directorio.
    for nombre in ("uestmat_paso3_muestra.json", "uestmat_muestra_60.csv"):
        ctrl[f"copia_commiteada_igual_{nombre}"] = sha(SELLADO / nombre) == sha(OUT / nombre)
        assert ctrl[f"copia_commiteada_igual_{nombre}"], nombre
    m3 = json.loads((SELLADO / "uestmat_paso3_muestra.json").read_text(encoding="utf-8"))
    previas = {(f["to"], f["chunk_id"], f["idx"]) for f in m3["filas"]}
    assert len(previas) == 60

    filas = json.loads((U.AUDIT / "p4_filas.json").read_text(encoding="utf-8"))
    por_clave = {(f["to"], f["chunk_id"], f["idx"]): f for f in filas}
    assert len(por_clave) == len(filas)

    K = Constructor()

    # Control: el constructor reproduce M01–M60 campo a campo.
    with open(SELLADO / "uestmat_muestra_60.csv", encoding="utf-8-sig", newline="") as fh:
        m60 = list(csv.DictReader(fh))
    rehechas = [K.fila(t["id_muestra"], t["par"], por_clave[(t["to"], t["chunk_id"], t["idx"])])
                for t in m3["filas"]]
    ctrl["constructor_reproduce_M01_M60"] = rehechas == m60
    assert ctrl["constructor_reproduce_M01_M60"]

    filas_csv, traza, conteos = [], [], []
    n_id = 0
    for h, k in ESTRATOS:
        estrato = sorted((f for f in filas if par_str(f["origen"], f["predicado"], f["destino"]) == h),
                         key=lambda f: (f["to"], f["chunk_id"], f["idx"]))
        ya = [f for f in estrato if (f["to"], f["chunk_id"], f["idx"]) in previas]
        lista = [f for f in estrato if (f["to"], f["chunk_id"], f["idx"]) not in previas]
        sel = random.Random(SEMILLA).sample(lista, k)
        sel.sort(key=lambda f: (f["to"], f["chunk_id"], f["idx"]))
        assert not {(f["to"], f["chunk_id"], f["idx"]) for f in sel} & previas
        conteos.append({"par": h, "n_poblacion": len(estrato), "n_ya_en_M01_M60": len(ya),
                        "n_elegibles": len(lista), "n_complementaria": k,
                        "n_total_con_M01_M60": len(ya) + k})
        for f in sel:
            n_id += 1
            mid = f"C{n_id:02d}"
            filas_csv.append(K.fila(mid, h, f))
            traza.append({"id_muestra": mid, "par": h, "to": f["to"], "linea_e1": f["linea"],
                          "chunk_id": f["chunk_id"], "idx": f["idx"]})
    assert n_id == 45 and len({(t["to"], t["chunk_id"], t["idx"]) for t in traza}) == 45

    campos = list(filas_csv[0].keys())
    assert campos == list(m60[0].keys())
    with open(OUT / "uestmat_muestra_complementaria.csv", "w", encoding="utf-8-sig", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=campos, quoting=csv.QUOTE_ALL)
        w.writeheader()
        w.writerows(filas_csv)

    res = {
        "unidad": "U-ESTUDIO-MATRIZ (muestra complementaria)",
        "poblacion": "reports/u_audit_tipos_v3/p4_filas.json (982 rechazos firma_invalida de E1, 10 TOs)",
        "exclusion": ("filas de M01–M60 por clave (to, chunk_id, idx), tomadas de "
                      "reports/u_estudio_matriz/uestmat_paso3_muestra.json"),
        "semilla": SEMILLA,
        "procedimiento": ("por estrato: filas del par ordenadas por (to, chunk_id, idx), sin las de M01–M60; "
                          "random.Random(20260929).sample(lista, k), instancia nueva por estrato"),
        "orden_filas": "estratos en el orden de conteos_por_estrato; dentro, por (to, chunk_id, idx); ids C01–C45",
        "conteos_por_estrato": conteos,
        "total_complementaria": n_id,
        "columnas_csv": campos,
        "controles": ctrl,
        "filas": traza,
    }
    (OUT / "uestmat_muestra_complementaria.json").write_text(
        json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps({"controles": ctrl, "conteos_por_estrato": conteos, "total": n_id},
                     ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
