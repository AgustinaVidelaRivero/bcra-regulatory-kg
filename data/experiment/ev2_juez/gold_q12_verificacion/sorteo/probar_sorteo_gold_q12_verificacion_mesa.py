"""probar_sorteo_gold_q12_verificacion_mesa.py — mesa, §276: la prueba en seco del sorteo de la mitad de verificación, antes de su
sello, sobre entradas sintéticas con la forma de las reales: 40 preguntas con la dosificación de EV2 (ext 16, cap 8, cla 6, ric 5, pro 5)
y 40 respuestas por brazo, menos 2 sin juicio y unas `requiere_adjudicacion`. Corre la misma función `sortear` del script. Ningún dato
real. Imprime OK o MAL por prueba. USD 0.
  python3 -I -B probar_sorteo_gold_q12_verificacion_mesa.py
"""
import importlib.util
import random
from pathlib import Path

spec = importlib.util.spec_from_file_location("S", Path(__file__).with_name("sortear_gold_q12_verificacion_mesa.py"))
S = importlib.util.module_from_spec(spec)
spec.loader.exec_module(S)
TOS = {"ext": 16, "cap": 8, "cla": 6, "ric": 5, "pro": 5}
QIDS = [f"Q{i:03d}" for i in range(40)]
TO_DE = {q: t for q, t in zip(QIDS, [t for t, n in TOS.items() for _ in range(n)])}
res = []


def c(n, ok):
    res.append(bool(ok))
    print("OK " if ok else "MAL", n)


def sinteticas(p_correcto, semilla, sacar_adj=8):
    r = random.Random(semilla)
    filas = []
    for b in S.BRAZOS:
        for q in QIDS:
            filas.append({"id_opaco": f"A22J-{r.getrandbits(40):010x}", "qid": q, "brazo": b, "id_sesion": f"N1-{q}-{b}",
                          "sha256_respuesta": f"{r.getrandbits(64):016x}", "n_criterios": r.randint(3, 5),
                          "clase": "correcto" if r.random() < p_correcto[b] else "parcial_o_incorrecto"})
    r.shuffle(filas)
    return filas[2 + sacar_adj:]          # 2 sin juicio y unas requiere_adjudicacion, fuera


def invariantes(k, filas):
    f = k["fichas"]
    por_b = {b: sum(1 for x in f if x["brazo"] == b) for b in S.BRAZOS}
    hay = {(b, cl) for b in S.BRAZOS for cl in S.CLASES if any(x["brazo"] == b and x["clase"] == cl for x in filas)}
    sale = {(x["brazo"], x["clase"]) for x in f}
    return (len(f) == 20 and len({x["id_pregunta"] for x in f}) == 20 and sorted(por_b.values()) == [6, 7, 7]
            and hay <= sale and [x["ficha"] for x in f] == [f"VG{i:02d}" for i in range(1, 21)]
            and all(x["id_opaco"] in {y["id_opaco"] for y in filas} for x in f))


f1 = sinteticas({"kg": 0.6, "fragmentos_bm25": 0.4, "fragmentos_denso": 0.5}, 1)
k1, k1b = S.sortear(f1, TO_DE), S.sortear(f1, TO_DE)
c("20 fichas, 20 preguntas distintas, 7, 7 y 6 por brazo, cada clase presente en su brazo, ids VG01 a VG20", invariantes(k1, f1))
c("el mismo sorteo con las mismas entradas: determinístico", k1 == k1b)
c("las cuotas por clase son proporcionales dentro de cada brazo (restos mayores, con al menos 1 por clase)",
  all(abs(k1["celdas"][f"{b}|correcto"] - k1["cuota_por_brazo"][b] *
          sum(1 for x in f1 if x["brazo"] == b and x["clase"] == "correcto") / sum(1 for x in f1 if x["brazo"] == b)) < 1.0001
      for b in S.BRAZOS))
f2 = sinteticas({"kg": 0.97, "fragmentos_bm25": 0.03, "fragmentos_denso": 0.5}, 2)
k2 = S.sortear(f2, TO_DE)
c("con una clase casi vacía en dos brazos, cada una igual entra al menos una vez", invariantes(k2, f2))
f3 = [dict(x, clase="parcial_o_incorrecto") if x["brazo"] == "fragmentos_bm25" else x for x in f1]
k3 = S.sortear(f3, TO_DE)
c("un brazo sin ninguna «correcto»: su cuota va entera a la otra clase", invariantes(k3, f3) and k3["celdas"]["fragmentos_bm25|correcto"] == 0)
otro = random.Random(9)
f4 = [x for x in f1 if not (x["brazo"] == "kg" and otro.random() < 0.8)]
try:
    k4 = S.sortear(f4, TO_DE)
    c("con pocas respuestas en un brazo, pasa a la otra clase o completa igual: invariantes", invariantes(k4, f4))
except SystemExit as e:
    c(f"con pocas respuestas en un brazo frena con su motivo ({str(e)[:60]})", "FRENO" in str(e))
try:
    S.sortear([x for x in f1 if x["brazo"] != "kg" or x["qid"] in QIDS[:5]], TO_DE)
    c("un brazo con menos respuestas que su cuota frena", False)
except SystemExit as e:
    c("un brazo con menos respuestas que su cuota frena", "menos respuestas que su cuota" in str(e))
c("la clave no trae ningún dato real: los ids sintéticos", all(x["id_sesion"].startswith("N1-Q") for x in k1["fichas"]))
print(f"pruebas: {sum(res)} de {len(res)}")
