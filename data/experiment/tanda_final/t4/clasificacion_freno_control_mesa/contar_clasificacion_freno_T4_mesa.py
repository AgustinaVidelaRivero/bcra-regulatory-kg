"""Mesa, §236 (22/10/2026): el control y la cuenta de la clasificación del freno de T4, para cuando la autora la selle. USD 0, solo
lectura. Lee de la carpeta `t4/clasificacion_freno/` del repo la planilla, su sha256, la marcada y su sello; controla que la marcada dé el
sha256 del sello, que la planilla sea la esperada (`e45f6e70…`, la que da el preparador sobre HEAD) y que las siete columnas fijas de la
marcada sean las de la planilla; y cuenta por código, sin leer `nota_de_la_lectura` ni `nota_clasificacion` ni imprimir ningún id:
- por capa, por campo y por falla de esquema, en total, por tramo y por celda;
- cuántas se repiten;
- la regla de la autora (registro, §89): si hay alguna «sí» o «no_se» en falla_de_esquema, se ve antes de seguir; si no, el freno se
  acepta y se declara como residuo, con su tasa.
Uso: python3 -I -B contar_clasificacion_freno_T4_mesa.py <carpeta clasificacion_freno> <salida.json> [sha256 esperado, solo en la prueba]"""
import csv
import hashlib
import io
import json
import sys
from collections import Counter
from pathlib import Path

C, OUT = Path(sys.argv[1]), Path(sys.argv[2])
ESPERADA = sys.argv[3] if len(sys.argv) > 3 else "e45f6e707c71acb2a68cf940ef2025f513b78dd55ac8d8648522065654d72bb1"   # el tercero, solo en la prueba
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()  # noqa: E731
pl, ma, se, ps = (C / n for n in ("clasificacion_freno_T4.csv", "clasificacion_freno_T4_marcada.csv", "sello_clasificacion_freno_T4.txt",
                                  "planilla_clasificacion_freno_T4.sha256"))
res = {"controles": {}}
k = res["controles"]
k["la_planilla_es_la_esperada"] = sha(pl) == ESPERADA and ps.read_text().split()[0] == ESPERADA
lin = [l for l in se.read_text(encoding="utf-8").splitlines() if l.split()[1:2] == [ma.name]]
k["la_marcada_da_su_sello"] = len(lin) == 1 and lin[0].split()[0] == sha(ma)
k["hora_del_sello"] = " ".join(lin[0].split()[2:]) if lin else None
P = list(csv.reader(io.StringIO(pl.read_text(encoding="utf-8")), delimiter=";"))
M = list(csv.reader(io.StringIO(ma.read_text(encoding="utf-8")), delimiter=";"))
k["16_filas_y_las_columnas_fijas_iguales"] = len(M) == 17 and M[0] == P[0] and all(m[:7] == p[:7] for m, p in zip(M[1:], P[1:]))
ok = all(v is True for kk, v in k.items() if kk != "hora_del_sello")
if ok:
    filas = [dict(zip(M[0], m)) for m in M[1:]]
    def cuenta(col, por=None, varias=False):
        if por is None:
            return dict(Counter(x for f in filas for x in (f[col].split("+") if varias else [f[col]])))
        return {g: dict(Counter(x for f in filas if f[por] == g for x in (f[col].split("+") if varias else [f[col]])))
                for g in sorted({f[por] for f in filas})}
    res["capa"] = {"total": cuenta("capa", varias=True), "por_tramo": cuenta("capa", "tramo", True), "por_celda": cuenta("capa", "celda", True)}
    res["campo"] = {"total": cuenta("campo", varias=True), "por_tramo": cuenta("campo", "tramo", True)}
    res["falla_de_esquema"] = {"total": cuenta("falla_de_esquema"), "por_tramo": cuenta("falla_de_esquema", "tramo")}
    res["se_repite"] = cuenta("se_repite")
    fe = res["falla_de_esquema"]["total"]
    res["lo_que_sigue"] = ("se ve antes de seguir: hay falla de esquema («sí» o «no_se»)" if fe.get("sí") or fe.get("no_se")
                           else "sin falla de esquema: el freno se acepta y se declara como residuo, con su tasa")
OUT.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(json.dumps(res, ensure_ascii=False))
sys.exit(0 if ok else 1)
