"""Factor de longitud — cuanto mas cortas son las unidades del bloque A que
las del corpus de desarrollo sobre el que se calibro la tarifa por unidad.

Existe porque la cifra viajo sin su definicion (regla i). El factor depende
de DOS elecciones que hay que declarar juntas: estadistico (mediana o media)
y poblacion (brazo prosa, brazo planilla, o el conjunto de los 191). Este
script emite la matriz completa para que ninguna combinacion quede implicita.

CONVENCION DE ESTA UNIDAD: **medianas**, por coherencia con `reporte_A1.md`
§5.b, donde el factor se publico como «mediana 93,5 contra 321» sobre los
DIEZ. La mediana es ademas robusta a la cola larga del corpus de desarrollo,
cuya media (607,5) casi duplica su mediana (321).

Uso:  python3 factor_longitud.py
"""
from __future__ import annotations

import glob
import json
import statistics as st
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402
import censo_forma as CF  # noqa: E402
from e0_lib import separar_encabezado_pie  # noqa: E402

NUEVE = tuple(t for t in C.DIEZ if t != "ri_spi")
E0_DEV = C.EXPERIMENT / "reextraccion_v2/e0_chunking/salida_enm01"


def main() -> int:
    dev = []
    for f in sorted(glob.glob(str(E0_DEV / "chunks_*.json"))):
        for c in json.loads(Path(f).read_text(encoding="utf-8")):
            if c.get("texto"):
                dev.append(len(c["texto"]))

    pobl = {"prosa": [], "planilla_ficha": [], "los_diez": []}
    for to in C.DIEZ:
        paginas, roles, modal, bloques, _d = C.leer_documento(to)
        for i, (lineas, rol) in enumerate(zip(paginas, roles), start=1):
            if rol != C.E0.ROL_CUERPO:
                continue
            cont, _x, _y = separar_encabezado_pie(lineas)
            cl = CF.clase_forma(CF.densidad_prosa(cont))
            for b in bloques[i]:
                pobl["los_diez"].append(b.n_chars)
                if to in NUEVE:
                    pobl[cl].append(b.n_chars)
    pobl["los_191_de_A2"] = pobl["prosa"] + pobl["planilla_ficha"]

    dd = {"mediana": st.median(dev), "media": round(st.mean(dev), 1)}
    out = {"_meta": {
        "convencion_de_esta_unidad": "medianas",
        "razon": "coherencia con reporte_A1.md §5.b y robustez a la cola larga "
                 "del corpus de desarrollo (media 607,5 contra mediana 321)",
        "denominador_dev": dd, "n_dev": len(dev)},
        "matriz": {}}

    print(f"corpus de desarrollo (n={len(dev)}): mediana {dd['mediana']} · "
          f"media {dd['media']}\n")
    print(f"{'poblacion':18s} {'n':>4s} {'mediana':>8s} {'media':>7s} "
          f"{'f_mediana':>10s} {'f_media':>8s}")
    for nom, v in pobl.items():
        me, mu = st.median(v), st.mean(v)
        fila = {"n": len(v), "mediana": round(me, 1), "media": round(mu, 1),
                "factor_por_mediana": round(dd["mediana"] / me, 2),
                "factor_por_media": round(dd["media"] / mu, 2)}
        out["matriz"][nom] = fila
        print(f"{nom:18s} {len(v):4d} {me:8.1f} {mu:7.1f} "
              f"{fila['factor_por_mediana']:9.2f}x {fila['factor_por_media']:7.2f}x")

    out["cifras_de_esta_unidad"] = {
        "brazo_prosa": out["matriz"]["prosa"]["factor_por_mediana"],
        "los_191_de_A2": out["matriz"]["los_191_de_A2"]["factor_por_mediana"],
        "los_diez_publicado_en_A1": out["matriz"]["los_diez"]["factor_por_mediana"],
    }
    salida = C.UNIDAD / "factor_longitud.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    print(f"\ncifras de esta unidad (medianas): "
          f"{json.dumps(out['cifras_de_esta_unidad'], ensure_ascii=False)}")
    print(f"escrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
