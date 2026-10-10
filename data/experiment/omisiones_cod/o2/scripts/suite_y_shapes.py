"""U-OMISIONES-COD, O1 — la suite del perfil r2 y las shapes de r2b sobre los grafos r2b con el código de HEAD y con el
de O1, con las funciones de U-RERESOL-CAT (`reresolver_catalogo.suite` y `.shapes`, importadas de la copia). Corre
desde la raíz de una COPIA; escribe solo en --out-dir.
Uso: python -B suite_y_shapes.py --par nombre=<dir r2 HEAD>,<dir r2 nuevo>,<manifiesto> [...] --out-dir <dir>"""
import argparse, json, sys
from pathlib import Path
ap = argparse.ArgumentParser(); ap.add_argument("--par", action="append", required=True); ap.add_argument("--out-dir", type=Path, required=True)
a = ap.parse_args()
raiz = Path.cwd().resolve(); assert not (raiz / ".git").exists()
sys.path.insert(0, str(raiz / "data/experiment/reresolucion_catalogo"))
import reresolver_catalogo as RR  # noqa: E402
assert Path(RR.__file__).resolve().is_relative_to(raiz)
E0 = raiz / "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
a.out_dir.mkdir(parents=True, exist_ok=True)
res = {}
for p in a.par:
    nom, rutas = p.split("=", 1); dh, dn, man = [Path(x) for x in rutas.split(",")]
    sh = {k: RR.shapes(d / "kg.json", d, E0, "r2b", None) for k, d in (("head", dh), ("nuevo", dn))}
    su = {k: RR.suite(d / "kg.json", d, raiz / man, None, a.out_dir / f"suite_{nom}_{k}.md") for k, d in (("head", dh), ("nuevo", dn))}
    tab = lambda s: {rid: (v["result"], v["severidad"], json.dumps(v.get("conteos"), sort_keys=True)) for rid, v in s["shapes"].items()}
    th, tn = tab(sh["head"]), tab(sh["nuevo"])
    js = {k: json.loads((a.out_dir / f"suite_{nom}_{k}.json").read_text(encoding="utf-8")) for k in ("head", "nuevo")}
    ih = {i["id"]: i for i in js["head"]["items"]}; inn = {i["id"]: i for i in js["nuevo"]["items"]}
    res[nom] = {"shapes": {k: {"veredicto": sh[k]["veredicto"], "bloqueantes_en_fail": sh[k]["bloqueantes_en_fail"]} for k in sh},
                "shapes_que_cambian": {rid: {"head": th.get(rid), "nuevo": tn[rid]} for rid in tn if th.get(rid) != tn[rid]},
                "suite_resumen": {k: js[k]["resumen"] for k in js},
                "suite_items_que_cambian_de_estado": {i: [ih[i]["estado"], inn[i]["estado"]] for i in inn if i in ih and ih[i]["estado"] != inn[i]["estado"]},
                "suite_items_que_cambian_de_detalle": sorted(i for i in inn if i in ih and ih[i].get("detalle") != inn[i].get("detalle"))}
    print(nom, json.dumps({k: v for k, v in res[nom].items() if k != "shapes_que_cambian"}, ensure_ascii=False)[:1500])
    print("   shapes que cambian:", {rid: (v["head"][0] if v["head"] else None, v["nuevo"][0]) for rid, v in res[nom]["shapes_que_cambian"].items()})
(a.out_dir / "suite_y_shapes.json").write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
