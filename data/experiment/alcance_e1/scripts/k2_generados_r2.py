"""U-ALCANCE-E1, A1: reproduce la condición de K2 de selftest_catalogo_unico.py (:387-392 en HEAD) sobre la raíz dada:
generados_r2/ en disco = generación determinística en memoria, ni un archivo más. Uso: k2_generados_r2.py RAIZ"""
import sys
from pathlib import Path

raiz = Path(sys.argv[1]).resolve()
sys.path.insert(0, str(raiz / "data/experiment/catalogo_unico/code"))
import generar_desde_catalogo as GEN  # noqa: E402

cu = raiz / "data/experiment/catalogo_unico"
g1, g2 = GEN.generar_todo(cu / "catalogo_sujetos_r2.json"), GEN.generar_todo(cu / "catalogo_sujetos_r2.json")
en_disco = sorted(p.name for p in (cu / "generados_r2").iterdir())
ok = g1 == g2 and en_disco == sorted(g1) and all((cu / "generados_r2" / n).read_text(encoding="utf-8") == t
                                                  for n, t in g1.items())
print("K2", "PASA" if ok else "FALLA", "| en disco:", len(en_disco), "| generados:", len(g1),
      "| de más:", sorted(set(en_disco) - set(g1)))
