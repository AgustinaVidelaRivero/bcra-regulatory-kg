"""Re-sellado único de la tanda 0, §4 (figuras): en un CLON de la copia del repo (nunca en el repo), cambia la ruta y el
candado del grafo de los generadores que los tienen escritos (generar_figura_catalogo_sujetos.py: KG y SHA_KG;
generar_figura_norma_a_grafo.py: GRAFO y GRAFO_DIEZ, que generar_figura_tripleta.py toma de ahí) por los del re-sellado, por
reemplazo exacto de líneas que aparecen una sola vez. La figura 4.5 no lo necesita: su generador recibe --grafo y
--sha256-grafo. Uso, desde <clon>/docs/tesis/figuras: python3 figuras_rs1_parche_clon.py <sha diez nuevo> <sha desarrollo nuevo>
"""
import sys
from pathlib import Path
DZ, DS = sys.argv[1], sys.argv[2]
SZ, SS = "a9631a64b422bdae634fb05135373c6f04c6272cdf7acd43a1be9f5b6c1f5f57", "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2"
p = Path("generar_figura_catalogo_sujetos.py"); s = p.read_text(encoding="utf-8")
o1 = '      / "ens_diez_r2b" / "r2" / "kg.json")'; assert s.count(o1) == 1
o2 = f'SHA_KG = "{SZ}"'; assert s.count(o2) == 1
p.write_text(s.replace(o1, '      / "ens_diez_r2b_rs1" / "r2" / "kg.json")').replace(o2, f'SHA_KG = "{DZ}"'), encoding="utf-8")
p = Path("generar_figura_norma_a_grafo.py"); s = p.read_text(encoding="utf-8")
a1 = 'GRAFO = ("data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2b/r2/kg.json",'
a2 = 'GRAFO_DIEZ = ("data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2b/r2/kg.json",'
for x in (a1, a2, f'"{SS}")', f'"{SZ}")'):
    assert s.count(x) == 1, x
s = s.replace(a1, a1.replace("ens_desarrollo_r2b/", "ens_desarrollo_r2b_rs1/")).replace(a2, a2.replace("ens_diez_r2b/", "ens_diez_r2b_rs1/"))
s = s.replace(f'"{SS}")', f'"{DS}")').replace(f'"{SZ}")', f'"{DZ}")')
p.write_text(s, encoding="utf-8")
print("parcheado en el clon")
