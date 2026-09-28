#!/usr/bin/env python3
"""U-INV-RECORRIDO, Paso 4 (complemento) — ¿los grafos de las trazas tienen nodos
con 3.17.1.4 en su procedencia? Cuenta, por kg.json (lectura cruda, sin loader),
los nodos cuyo registro serializado contiene «3.17.1.4» (no seguido de dígito) y
los que contienen «3.17» como prefijo de punto. Solo lectura; salida a stdout.
Uso: python3 /tmp/u_inv_ejemplo/uinvrec_granularidad.py <raíz del repo>"""
import hashlib, json, os, re, sys
R = os.path.abspath(sys.argv[1])
KGS = {"run_3": "data/experiment/run_3_ppf_core/kg.json",
       "v2": "data/experiment/reextraccion_v2/corpus_v2/salida/kg.json",
       "v3": "data/experiment/grafo_v2/reensamblado_v3/kg.json",
       "r1": "data/experiment/reextraccion_v2/corpus_v2/salida_r1/kg.json"}
P4 = re.compile(r"3\.17\.1\.4(?![0-9])")
P317 = re.compile(r"(?<![0-9.])3\.17(?![0-9])")
for k, rel in KGS.items():
    raw = open(os.path.join(R, rel), "rb").read()
    kg = json.loads(raw)
    nodos = kg["nodes"] if isinstance(kg, dict) else kg
    def prov(n):
        return json.dumps({x: n.get(x) for x in ("provenance", "provenances", "source", "sources") if x in n}, ensure_ascii=False)
    n4 = [n["id"] for n in nodos if P4.search(prov(n))]
    n317 = [n["id"] for n in nodos if P317.search(prov(n)) or re.search(r"3\.17\.", prov(n))]
    print(f"{k:6s} {rel}  sha256 {hashlib.sha256(raw).hexdigest()[:12]}…  nodos {len(nodos)}  "
          f"con 3.17.1.4 en procedencia: {len(n4)}  con 3.17 o 3.17.x: {len(n317)}")
    for i in n4[:5]:
        print(f"         3.17.1.4 -> {i}")
