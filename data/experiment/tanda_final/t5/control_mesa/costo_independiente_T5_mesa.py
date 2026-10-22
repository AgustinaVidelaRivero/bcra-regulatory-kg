"""Mesa, §237 (22/10/2026): el costo de T5 de la tanda final, con código propio, contra t5/salidas/cifras_t5.json. Lee del repo, sin
escribir en él: de estado_corpus.json, solo `gasto_usd` de cada fase cerrada (nada del resumen de E3); de presupuesto_compartido.json, el
gasto y el tope; del manifiesto, el estimado por TO; de tramos_tanda_final.json, los TOs y las unidades de cada tramo; de la E0 de la tanda
final (chunks_<TO>.json), solo `chars_completo`, el campo con que la nota 27bfaeb5 reparte el estimado. Las tarifas son las del §3 del
pre-registro de la tanda final (4de7f2a7). Imprime los totales por etapa y por tramo, y la parte del tramo 1 en unidades, en caracteres y
en el estimado repartido; ninguna cifra por TO.
Uso: python3 -I -B costo_independiente_T5_mesa.py <repo> <salida.json>"""
import json
import sys
from pathlib import Path

R, OUT = Path(sys.argv[1]), Path(sys.argv[2])
L = lambda p: json.loads((R / p).read_text(encoding="utf-8"))  # noqa: E731
SAL = "data/experiment/reextraccion_v2/corpus_tanda_final/salida_r2b"
tr = L("data/experiment/tanda_final/preregistro/tramos_tanda_final.json")
tos = {"tramo_1": list(tr["tramo_1_tos"]), "tramo_2": list(tr["tramo_2_tos"])}
U = {k: tr[k]["unidades"] for k in tos}
fc = L(f"{SAL}/estado_corpus.json")["fases_cerradas"]
gasto = {k: float(v["gasto_usd"]) for k, v in fc.items()}
pres = L(f"{SAL}/presupuesto_compartido.json")
est = L("data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json")["limites"]["estimado_usd"]
E0 = R / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda_final_r2b"
chars = {t: sum(c["chars_completo"] for c in json.loads((E0 / f"chunks_{t}.json").read_text(encoding="utf-8"))) for k in tos for t in tos[k]}
TAR = 0.021115
c5 = L("data/experiment/tanda_final/t5/salidas/cifras_t5.json")["costo"]
res, ok = {}, {}
for k, ts in tos.items():
    real = {e: sum(gasto[f"{t}:{e}"] for t in ts) for e in ("e1", "e3")}
    rep = sum(est[t]["e1"] + est[t]["e3"] for t in ts)
    res[k] = {"tos": len(ts), "unidades": U[k], "real_e1": round(real["e1"], 6), "real_e3": round(real["e3"], 6),
              "real": round(real["e1"] + real["e3"], 6), "estimado_s3": round(U[k] * TAR, 6), "estimado_repartido": round(rep, 6),
              "caracteres": sum(chars[t] for t in ts)}
    x = c5["por_tramo"][k]
    ok[k] = all(abs(a - b) < 2e-6 for a, b in ((res[k]["real"], x["real"]["total"]), (res[k]["real_e1"], x["real"]["e1"]),
                                                  (res[k]["real_e3"], x["real"]["e3"]), (res[k]["estimado_s3"], x["estimado_s3"]["total"]),
                                                  (res[k]["estimado_repartido"], x["estimado_repartido"]["total"])))
tot_real = sum(gasto.values())
ok["fases"] = len(gasto) == 2 * 98 and set(gasto) == {f"{t}:{e}" for k in tos for t in tos[k] for e in ("e1", "e3")}
ok["total_real"] = abs(round(tot_real, 6) - c5["total"]["real"]["total"]) < 2e-6
ok["presupuesto_compartido"] = abs(pres["gasto_usd"] - tot_real) < 1e-5 and pres["tope_usd"] == c5["total"]["presupuesto_compartido"]["tope_usd"]
UT, CT, RT = sum(U.values()), sum(chars.values()), sum(r["estimado_repartido"] for r in res.values())
# el repartido es proporcional a los caracteres de cada TO (nota 27bfaeb5): cada TO, dentro de un centavo
ok["repartido_proporcional_a_los_caracteres"] = all(abs(est[t]["e1"] + est[t]["e3"] - RT * chars[t] / CT) < 0.01 for t in chars)
res["total"] = {"real": round(tot_real, 6), "presupuesto_gasto": pres["gasto_usd"], "tope": pres["tope_usd"], "estimado_repartido": round(RT, 6)}
res["parte_del_tramo_1"] = {"en_unidades": round(U["tramo_1"] / UT, 4), "en_caracteres": round(res["tramo_1"]["caracteres"] / CT, 4),
                            "en_el_estimado_repartido": round(res["tramo_1"]["estimado_repartido"] / RT, 4),
                            "en_el_real": round(res["tramo_1"]["real"] / tot_real, 4)}
res["usd_por_unidad"] = {k: {"real": round(res[k]["real"] / U[k], 6), "estimado_s3": TAR, "estimado_repartido": round(res[k]["estimado_repartido"] / U[k], 6)}
                         for k in tos}
res["controles"] = ok
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False, indent=1))
sys.exit(0 if all(ok.values()) else 1)
