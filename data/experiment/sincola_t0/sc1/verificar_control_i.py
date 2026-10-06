"""U-SINCOLA-T0, SC1-bis, control (i): verificación de que las diferencias que control_repro_sc1bis.py reporta como
«distintos» son solo rutas absolutas (la de la copia fuente, la del directorio de trabajo y la del repo original, que
los reportes sellados guardan) y, en los r2b sin bandera, los dos campos nuevos del reporte; y que el bloque r2a (suite
y shapes) coincide con el control de T3 / T3-bis. Uso: verificar_control_i.py <scratchpad> <repo>"""
import json, sys
from pathlib import Path
SCR, REPO = sys.argv[1], sys.argv[2]
F = Path(SCR) / "copia_sc1bis"; W = Path(SCR) / "trabajo_control_i"; C = W / "copia"; O = W / "salidas"
REX = "data/experiment/reextraccion_v2"
def norm(t, extra):
    for a, b in extra: t = t.replace(a, b)
    return t
ok = True
print("=== r1: los 3 'distintos' con la ruta del repo original también normalizada ===")
for x in ("cinco", "diez", "desarrollo"):
    sal = O / f"ens_{x}"
    for rel in ("r1/e5_esqueleto.json", "r1/reporte_ensamblado_r1.json", "reporte_ensamblado.json"):
        a = (F / REX / "corpus_tanda0" / f"ens_{x}" / rel).read_text(encoding="utf-8")
        b = (sal / rel).read_text(encoding="utf-8")
        ex = ((str(sal), "<SALIDA>"), (f"{REX}/corpus_tanda0/ens_{x}", "<SALIDA>"), (str(C) + "/", ""), (str(F) + "/", ""), (REPO + "/", ""),
              (str(C / REX / "corpus_tanda0" / "salida_dirigida"), f"{REX}/corpus_tanda0/salida_dirigida"))
        r = norm(a, ex) == norm(b, ex); ok &= r
        print(f"  ens_{x}/{rel}: igual con rutas normalizadas = {r}")
print("=== r2b sin bandera: reporte sin los dos campos nuevos y con las rutas normalizadas ===")
for x in ("diez", "desarrollo"):
    sal = O / f"ens_{x}_r2b_sin_bandera"
    a = json.loads((F / REX / "corpus_tanda0" / f"ens_{x}_r2b" / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    b = json.loads((sal / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8"))
    for k in ("con_cola", "cola_descartada_por_to"): b.pop(k, None); a.pop(k, None)
    ta, tb = (json.dumps(d, ensure_ascii=False, indent=1, sort_keys=True) for d in (a, b))
    ex = ((str(sal), "<SALIDA>"), (f"{REX}/corpus_tanda0/ens_{x}_r2b", "<SALIDA>"), (str(C) + "/", ""), (str(F) + "/", ""), (REPO + "/", ""))
    r = norm(ta, ex) == norm(tb, ex); ok &= r
    print(f"  {x}: igual = {r}")
print("=== r2a: suite y shapes contra el control de T3 y de T3-bis ===")
mine = json.loads((Path(SCR) / "salida_sc1bis" / "control_i_repro.json").read_text(encoding="utf-8"))
for p in ("data/experiment/reext_t0/t3/salida/control_repro_t3.json", "data/experiment/reext_t0/t3bis/salida/control_repro_t3bis.json"):
    t3 = json.loads((Path(REPO) / p).read_text(encoding="utf-8"))
    for x in ("diez", "desarrollo"):
        a, b = t3[f"ens_{x}_r2a"], mine[f"ens_{x}_r2a"]
        r = (a["suite"]["items_que_cambian_de_estado"] == b["suite"]["items_que_cambian_de_estado"] and a["suite"]["resumen"] == b["suite"]["resumen"]
             and a["shapes"]["shapes_que_cambian"] == b["shapes"]["shapes_que_cambian"] and a["shapes"]["fail_nuevo"] == b["shapes"]["fail_nuevo"]); ok &= r
        print(f"  {p.split('/')[-1]} {x}: suite y shapes iguales al control = {r} | resumen {b['suite']['resumen']} | fail {b['shapes']['fail_nuevo']}")
print("=== la fuente cambió durante el control solo por las corridas con --sin-cola (SC1.3), que escribían en paralelo ===")
camb = mine["fuente_archivos_que_cambiaron"]
r = all(("_r2b_sincola/" in c or "_r2b_sincola_corrida2/" in c) for c in camb); ok &= r
print(f"  {len(camb)} archivos, todos bajo ens_*_r2b_sincola{{,_corrida2}}/ = {r}")
print("VEREDICTO control (i):", "OK" if ok else "REVISAR")
