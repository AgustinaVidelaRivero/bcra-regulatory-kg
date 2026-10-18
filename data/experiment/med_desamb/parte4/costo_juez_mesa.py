"""Mesa, §139 y §140 (17/10/2026), U-MED-DESAMB, parte 4: el costo estimado del juez de modelo y las cuentas de los umbrales. USD 0, sin API.

Supuestos (NO VERIFICADOS hasta la prueba de humo del juez, que da los tokens reales de la API):
- tokens = caracteres / 3,5 (castellano);
- el ítem mide 3.331 caracteres de media (planilla de prueba de r2a, consola_prueba_r2a.txt; 14 ítems);
- el prefijo cacheable (instrucciones, criterio y 12 calibradores) mide 1.500 tokens más 12 ítems;
- la salida, con el razonamiento, 600 tokens por llamada.
Precios de claude-opus-5-5 por millón de tokens: entrada 4, salida 20, escritura de caché 5, lectura 0,20
(data/experiment/comp_e1/c1/comun_c1.py:34-35, páginas consultadas el 05/10/2026). La entrada y la salida las verificó la mesa de
apoyo en la página oficial de precios, según la autora (17/10/2026, hoja de ruta de la mesa, §140); la escritura y la lectura de caché
siguen con el ancla de comun_c1.py.
Uso: python3 -I -B costo_juez_mesa.py"""
import importlib.util
from pathlib import Path

_s = importlib.util.spec_from_file_location("est", str(Path(__file__).resolve().parent / "estimadores_desamb_mesa.py"))
EST = importlib.util.module_from_spec(_s)
_s.loader.exec_module(EST)

N_RS1 = {"E1": 365, "E2": 168, "E3": 1010, "E4": 277, "E5": 334, "E6": 200, "E7": 8, "E8": 16, "E9": 20}  # verificado en §139 (b)
N_POR_ESTRATO = 50
REPETICIONES = 3
P = {"in": 4.00, "out": 20.00, "cw": 5.00, "cr": 0.20}
CHARS_ITEM, CHARS_POR_TOKEN = 3331, 3.5
PREFIJO = 1500 + 12 * CHARS_ITEM / CHARS_POR_TOKEN
SALIDA = 600

n = {e: min(N, N_POR_ESTRATO) for e, N in N_RS1.items()}
items = sum(n.values())
item_tok = CHARS_ITEM / CHARS_POR_TOKEN
por_llamada = (PREFIJO * P["cr"] + item_tok * P["in"] + SALIDA * P["out"]) / 1e6
escrituras = REPETICIONES * 3 * PREFIJO * P["cw"] / 1e6       # tres escrituras de caché por repetición, holgadas
LECTURA = 52                                                    # E4 26, E6 16 y control 10 (§140): el acuerdo; los 12 calibradores no
validez = LECTURA * REPETICIONES * por_llamada                  # el juez también sobre los 52 ítems de la lectura, para el acuerdo
total = items * REPETICIONES * por_llamada + escrituras + validez
print(f"ítems por estrato: {n} | total {items} (censo de E7, E8 y E9)")
print(f"por llamada: USD {por_llamada:.4f} (prefijo {PREFIJO:.0f} tokens leídos de caché, ítem {item_tok:.0f}, salida {SALIDA})")
print(f"llamadas: {items * REPETICIONES} de la cifra + {LECTURA * REPETICIONES} del acuerdo | costo estimado USD {total:.2f} | tope autorizado USD 40")
for k, m in ((26, 30), (68, 78), (67, 78), (66, 78), (44, 52)):
    p, lo, hi = EST.wilson(k, m)
    print(f"Wilson {k}/{m}: p {p:.4f}, IC 95 % ({lo:.4f}, {hi:.4f})")
r = EST.ponderado({e: (N_RS1[e], int(round(0.85 * n[e])), n[e]) for e in N_RS1})
print(f"n efectivo de Kish de la cifra ponderada con esos n (Kish depende solo de N y n): {r['n_efectivo_kish']:.1f}")
