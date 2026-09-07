"""Ancla de PR-2 — tasa de unidades que RINDEN en el corpus de desarrollo.

Conserva las CUATRO cifras con su definicion, y declara al lado cual es la
convencion laudada, para que ningun numero viaje suelto en prosa.

HALLAZGO que motiva este script: la ambiguedad del ancla no estaba en el
filtro de tipo sino en QUE CAMPO DE PROCEDENCIA se cuenta. Bajo procedencia
PRIMARIA (`provenance`), restringir a tipos normativos no mueve una sola
unidad: los dos conjuntos son identicos. La diferencia aparece solo al usar
la lista completa (`provenances`), y su brecha de 51 unidades esta sostenida
integramente por nodos `TextoOrdenado`.

CONVENCION LAUDADA (07/09) — «rinde» se mide con `provenance` PRIMARIA, y el
ancla comparable de PR-2 es 96,2 %. Sus dos razones:
  (i)  una unidad rinde si GENERO contenido normativo, no si aparece listada
       entre las procedencias de un nodo generado en otra unidad;
  (ii) el ancla se midio con ese mismo campo, de modo que usar la lista
       completa compararia dos cosas medidas con reglas distintas.

Uso:  python3 ancla_pr2.py
"""
from __future__ import annotations

import glob
import json
import sys
from collections import Counter
from pathlib import Path

AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI))
import comun_coba as C  # noqa: E402

KG_VIGENTE = C.EXPERIMENT / "reextraccion_v2/corpus_v2/salida_r1/kg.json"
KG_SHA = "0226e9477baee02d772bbfecee78a49441b189d0e0512ca5e22956dfb084196a"
E0_DEV = C.EXPERIMENT / "reextraccion_v2/e0_chunking/salida_enm01"

# tipos normativos del esquema congelado (excluye TextoOrdenado, Comunicacion
# y Sujeto, que son andamiaje documental o de catalogo, no contenido de la
# unidad)
NORMATIVOS = frozenset({"Operacion", "Restriccion", "Excepcion", "Obligacion",
                        "Potestad", "Condicion", "Definicion"})

CONVENCION = "primaria_normativo"


def main() -> int:
    kg = json.loads(KG_VIGENTE.read_text(encoding="utf-8"))
    unidades = set()
    for f in sorted(glob.glob(str(E0_DEV / "chunks_*.json"))):
        for c in json.loads(Path(f).read_text(encoding="utf-8")):
            unidades.add(c["id"])

    conj: dict[str, set] = {k: set() for k in
                            ("primaria_cualquiera", "primaria_normativo",
                             "lista_cualquiera", "lista_normativo")}
    for n in kg["nodes"]:
        norm = n["type"] in NORMATIVOS
        cid = (n.get("provenance") or {}).get("chunk_id")
        if cid:
            conj["primaria_cualquiera"].add(cid)
            if norm:
                conj["primaria_normativo"].add(cid)
        for p in (n.get("provenances") or []):
            c2 = p.get("chunk_id")
            if c2:
                conj["lista_cualquiera"].add(c2)
                if norm:
                    conj["lista_normativo"].add(c2)

    d = len(unidades)
    cifras = {k: {"unidades": len(v & unidades),
                  "denominador": d,
                  "fraccion": round(len(v & unidades) / d, 4)}
              for k, v in conj.items()}

    brecha = (conj["lista_cualquiera"] & unidades) - (conj["lista_normativo"] & unidades)
    tipos_brecha = Counter()
    for n in kg["nodes"]:
        for p in (n.get("provenances") or []):
            if p.get("chunk_id") in brecha:
                tipos_brecha[n["type"]] += 1

    out = {
        "_meta": {
            "grafo_vigente": "KG-Reextraido-r1", "sha256": KG_SHA,
            "denominador": "las 1.763 unidades E0 de e0_chunking/salida_enm01",
            "tipos_normativos": sorted(NORMATIVOS),
            "convencion_laudada": CONVENCION,
            "razon_i": "una unidad rinde si GENERO contenido normativo, no si "
                       "aparece listada entre las procedencias de un nodo "
                       "generado en otra unidad",
            "razon_ii": "el ancla se midio con ese mismo campo; usar la lista "
                        "completa compararia dos cosas medidas con reglas "
                        "distintas",
        },
        "cifras": cifras,
        "hallazgo": {
            "primaria_cualquiera_igual_a_primaria_normativo":
                (conj["primaria_cualquiera"] & unidades)
                == (conj["primaria_normativo"] & unidades),
            "nota": "bajo procedencia primaria, restringir a tipos normativos "
                    "no mueve una sola unidad: la ambiguedad del ancla no era "
                    "el filtro de tipo sino que campo de procedencia cuenta",
            "brecha_lista": len(brecha),
            "tipos_que_sostienen_la_brecha": dict(tipos_brecha),
        },
        "ancla_de_PR2": cifras[CONVENCION]["fraccion"],
        "umbral_PR2": 0.80,
    }

    salida = C.UNIDAD / "ancla_pr2.json"
    salida.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    for k, v in cifras.items():
        marca = "  <== CONVENCION LAUDADA" if k == CONVENCION else ""
        print(f"  {k:22s} {v['unidades']:5d}/{v['denominador']} = "
              f"{v['fraccion']:.1%}{marca}")
    print(f"\nconjuntos primarios identicos: "
          f"{out['hallazgo']['primaria_cualquiera_igual_a_primaria_normativo']}")
    print(f"brecha de la lista: {len(brecha)} unidades, tipos "
          f"{dict(tipos_brecha)}")
    print(f"\nescrito: {salida.relative_to(C.REPO)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
