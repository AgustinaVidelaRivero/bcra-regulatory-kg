"""U-REEXT-T0, T4, punto 7, fase A: el texto de E0 r2b (propio y último heredado) de las unidades del grupo c, en el
orden sellado, sin la extracción, para decidir sobre el texto si la unidad tiene más de un supuesto. La decisión se
registra con su hora en salida/grupo_c_fase_a.md antes de mirar la extracción. Solo lee e imprime. USD 0.

Uso (desde la raíz de una copia): python -B data/experiment/reext_t0/t4/solo_texto_t4.py <raíz de la copia> <desde> <hasta>
(posiciones del orden sellado, desde 0, hasta excluida).
"""
import json
import sys

sys.path.insert(0, sys.argv[1] + "/data/experiment/reext_t0/t4")
import comun_t4 as K  # noqa: E402

orden = json.load(open(sys.argv[1] + "/data/experiment/reext_t0/sellos_t4.json"))["c_grupo_c"]["orden"]
for i in range(int(sys.argv[2]), int(sys.argv[3])):
    cid = orden[i]
    t = K.texto(cid)
    print(f"## {i + 1}. {cid}")
    if t["heredado"]:
        print("   HEREDADO (último):", " ".join(t["heredado"][-1].split())[:300])
    print("   PROPIO:", " ".join(t["propio"].split())[:6000])
