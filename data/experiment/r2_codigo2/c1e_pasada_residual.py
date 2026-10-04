"""U-R2-CODIGO-2, C1.e — la pasada residual de E4 en el perfil r2 (USD 0, sin API ni Neo4j). Solo escribe --out.

En `ensamblar_tanda0.correr_cadena_r2` la pasada residual de propuestos corre sobre una copia del grafo
(`E4.resolver_propuestos(deepcopy(kg), catalogo)`), se resume en el reporte (`e4.pasada_residual_de_propuestos_
medida_no_aplicada`) y se escribe en `e4_pasada_residual_medida.json`. El catálogo que carga la misma línea lo usa
después el esqueleto (`inyectar_esqueleto_v3`), así que no se retira con ella.

Qué mide, sobre KG-Tanda0-Diez-r2a y KG-Tanda0-Desarrollo-r2a: (1) lo que la pasada propone hoy; (2) contrafáctico,
con `r1_e4.resolver_propuestos` reemplazado en memoria por una función que no resuelve nada y devuelve la forma
vacía: el sha256 del grafo tiene que ser el del grafo versionado (la pasada no toca el grafo).

Uso, desde la raíz de una copia del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/r2_codigo2/c1e_pasada_residual.py \
      --out data/experiment/r2_codigo2/salidas/c1e_pasada_residual.json
"""
from __future__ import annotations

import argparse
import hashlib
import json
from collections import OrderedDict

import c1_comun as K

E4 = K.ENS.E4


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = OrderedDict()
    for nombre in K.GRAFOS:
        base = K.correr_r2(nombre)
        llamadas, catalogos = [], []

        def sin_pasada(kg, catalogo):
            llamadas.append(1)
            catalogos.append(hashlib.sha256(json.dumps(catalogo, sort_keys=True, ensure_ascii=False,
                                                       default=str).encode("utf-8")).hexdigest())
            return {"tabla": [], "n_resueltos": 0, "motivos": {}}
        contra = K.correr_r2(nombre, [(E4, "resolver_propuestos", sin_pasada)])
        tabla = base["escritos"]["e4_pasada_residual_medida.json"]
        out[nombre] = OrderedDict([
            ("control_sha", K.control_sha(nombre, base)),
            ("pasada_medida_en_r2a", base["resumen"]["e4"]["pasada_residual_de_propuestos_medida_no_aplicada"]),
            ("filas_de_la_tabla", len(tabla)),
            ("filas_con_resolucion", sum(1 for f in tabla if f.get("resuelto_a"))),
            ("sin_la_pasada_sha256_kg", contra["sha256"]),
            ("sin_la_pasada_el_grafo_es_el_versionado", contra["sha256"] == K.GRAFOS[nombre]["sha256"]),
            ("llamadas_a_resolver_propuestos_en_la_cadena_r2", len(llamadas)),
            ("sha256_del_catalogo_que_recibe", sorted(set(catalogos)))])
    K.escribir_json(K.RAIZ / a.out, out)
    for k, v in out.items():
        print(k, v["control_sha"]["reproduce"], v["pasada_medida_en_r2a"], v["sin_la_pasada_el_grafo_es_el_versionado"],
              v["llamadas_a_resolver_propuestos_en_la_cadena_r2"])


if __name__ == "__main__":
    main()
