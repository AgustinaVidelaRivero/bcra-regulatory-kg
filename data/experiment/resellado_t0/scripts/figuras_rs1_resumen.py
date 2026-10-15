"""Re-sellado único de la tanda 0, §4 (figuras): el resumen de las corridas de los cuatro generadores sobre los clones (línea
de base con los sellados y corrida con los re-sellados, más la 4.5 con el grafo de desarrollo, sellado y re-sellado, por el
«mismo vecindario» de su LEEME), contra las figuras del repo. Solo lee.
Uso: python3 -I -B figuras_rs1_resumen.py <dir de salidas de figuras (base/ y rs1/)> <repo> <salida.json>
"""
import hashlib, json, sys
from pathlib import Path
O, R, SAL = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
F = R / "docs/tesis/figuras"
FIG = {"ensamblado": "figura_ensamblado_ejemplo", "catalogo": "figura_catalogo_sujetos", "norma": "figura_norma_a_grafo", "tripleta": "figura_tripleta"}
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
res = {"metodo": ("cada generador corre sobre un clon de la copia del repo: primero tal cual (línea de base, con los sellados) y después "
                  "con el grafo re-sellado (4.5 por --grafo y --sha256-grafo; los otros tres con la ruta y el candado cambiados solo en el clon); "
                  "se compara cada salida con la del directorio de figuras del repo"),
       "grafos_nuevos": {"diez": "fda6c07dbb95602f5992f7e1ad9bf148ff1c2a72b9f69ff2ebbce891c15740ea", "desarrollo": "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31"},
       "figuras": {}}
for k, b in FIG.items():
    res["figuras"][b] = {}
    for ext in ("svg", "png", "pdf"):
        if not (O / "base" / k / f"{b}.{ext}").exists():
            continue
        r, rb, rn = F / f"{b}.{ext}", O / "base" / k / f"{b}.{ext}", O / "rs1" / k / f"{b}.{ext}"
        res["figuras"][b][ext] = {"repo": sha(r), "linea_de_base": sha(rb), "re_sellado": sha(rn),
                                  "linea_de_base_igual_al_repo": sha(rb) == sha(r), "re_sellado_igual_al_repo": sha(rn) == sha(r)}
    for c in ("base", "rs1"):
        res["figuras"][b][f"rc_{c}"] = (O / c / f"consola_{k}.txt").read_text(encoding="utf-8").strip().splitlines()[-1]
res["ok"] = all(v[e]["re_sellado_igual_al_repo"] and v[e]["linea_de_base_igual_al_repo"] for v in res["figuras"].values() for e in v if not e.startswith("rc_"))
b = "figura_ensamblado_ejemplo"
res["figura_ensamblado_ejemplo_con_el_grafo_de_desarrollo"] = {
    "nota": "el LEEME (§1) dice que el vecindario de la unidad es el mismo en el grafo de desarrollo: se corre también con el de desarrollo, sellado y re-sellado",
    "grafo_sellado": "6e7560433148cfe0c476cdd61199c32278187c4196d6f90dc0a38976a6d8e9a2",
    "grafo_re_sellado": "acb26dca0885e9ea83ab02637f15c1dac57885f0cf017c5fb16173ac7dfcac31",
    **{ext: {"repo": sha(F / f"{b}.{ext}"), "sellado": sha(O / "base/ensamblado_desarrollo" / f"{b}.{ext}"),
             "re_sellado": sha(O / "rs1/ensamblado_desarrollo" / f"{b}.{ext}")} for ext in ("svg", "png", "pdf")}}
x = res["figura_ensamblado_ejemplo_con_el_grafo_de_desarrollo"]
res["ok"] = res["ok"] and all(x[e]["repo"] == x[e]["sellado"] == x[e]["re_sellado"] for e in ("svg", "png", "pdf"))
SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("ok", res["ok"])
