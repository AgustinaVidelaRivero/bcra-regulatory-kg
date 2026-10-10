"""Marcas de la mesa (decisión de la autora del 10/10/2026): en cada lote del piloto, los elementos cuyo texto de E0 (propio y heredado)
contiene un ejemplo resuelto de la regla v0. Coincidencia por cadena, después de plegar. Escribe un JSON por lote, en un renglón; no imprime ids ni
cuántos (la autora no los ve). Corre sobre la copia del paso 2.
Uso: python3 -I -B marcas_ejemplos_v0_mesa.py <espejo> <dir_salida>"""
import json, re, sys, unicodedata, hashlib
from pathlib import Path
esp, out = sys.argv[1:3]
sys.path.insert(0, str(Path(esp) / "data/experiment/med_umbrales/p/code")); sys.dont_write_bytecode = True
import comun_P as C
kg, kg_sha = C.cargar_kg()
acta = json.load(open(Path(esp) / "data/experiment/med_umbrales/p/acta_sorteo_P.json"))
nodos = {n["id"]: n for n in kg["nodes"]}
def plegar(s):
    s = unicodedata.normalize("NFKD", s); s = "".join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r"\s+", " ", s)
V0 = ["1,25 %", "$ 5.000 millones", "dos veces", "180 (ciento ochenta) días", "el quinto día hábil", "treinta y cinco",
      "10 % de la responsabilidad patrimonial computable del mes anterior", "pesos o su equivalente en otras monedas",
      "dólares estadounidenses", "los plazos se computan en días hábiles", "dentro de los 10 días de recibida la solicitud",
      "importe de referencia establecido en el punto 3.7", "no superarán el 1,25 % de los activos ponderados", "hasta el 31 de diciembre",
      "entre 30 días y 90 días"]
for lote in ("lote1", "lote2"):
    orden = acta["sorteo"]["orden_de_lectura"][lote]
    filas = []
    for k, eid in enumerate(orden, 1):
        t = plegar(" ".join(x for _, x, _ in C.textos_nodo(nodos[eid.split("#u")[0]])))
        hits = [q for q in V0 if plegar(q) in t]
        filas.append({"posicion_en_el_orden_de_lectura": k, "elemento": eid,
                      "marca": "coincide con un ejemplo resuelto de la v0" if hits else None, "ejemplos": hits})
    doc = {"lote": lote, "regla": "v0 (22eb6a78…)", "grafo_kg_sha256": kg_sha, "criterio": "el texto de E0 del nodo, propio y heredado, contiene el ejemplo, plegado",
           "decision": "autora, 10/10/2026: marcar sin decirle cuáles ni cuántos", "filas": filas}
    p = Path(out) / f"NO_ABRIR_marcas_ejemplos_v0_{lote}_mesa.json"
    p.write_text(json.dumps(doc, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")  # un renglón: el número de renglones no dice cuántas marcas hay
    print(p.name, hashlib.sha256(p.read_bytes()).hexdigest())
