"""
cifras_reparto_t1.py — B6.1, tanda final, «seguí» de T2, parte 1 (el estimado repartido, antes de T2): las cifras de la
sección 15 del FRENO T1, desde sus archivos (pre-registro firmado de la tanda final, §7: «toda cifra del FRENO sale por
script»). USD 0, sin API. Solo lee (git solo con `diff --numstat`); escribe --md y --json. No abre ningún NO_ABRIR_.

Fuentes, relativas a --repo:
  - los tres archivos del cambio y la alternativa (sha256), `git diff --numstat` contra HEAD y la lista para T2, controlada
    renglón por renglón como `shasum -a 256 -c`;
  - data/experiment/tanda_final/t1/entradas_reparto/: el control de entradas con el manifiesto nuevo, los logs de las tres
    pruebas del lanzador, las bases de la caché antes y después, el volcado de los mensajes y el ancla de la hora de fin de T1.
Uso: python3 -I -B cifras_reparto_t1.py --repo <raíz> --md <salida.md> --json <salida.json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True
D = "data/experiment/tanda_final/t1/entradas_reparto"
TRES = ("data/experiment/reextraccion_v2/manifiestos/tanda_final_98tos_r2b.json",
        "data/experiment/tanda_final/t2/lanzar_t2.py", "data/experiment/tanda_final/t1/sha256_para_T2.txt")
ALT = "data/experiment/tanda_final/t1/manifiesto/tanda_final_98tos_r2b_reparto_alternativa.json"
LOGS = ("lanzador_reparto_prueba_1_punta_a_punta.log", "lanzador_reparto_prueba_2_autorizado_tramo_2.log",
        "lanzador_reparto_prueba_3_retomar_tras_pausa.log")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=Path, required=True)
    ap.add_argument("--md", type=Path, required=True)
    ap.add_argument("--json", type=Path, required=True)
    a = ap.parse_args()
    r = a.repo.resolve()
    sha = lambda rel: hashlib.sha256((r / rel).read_bytes()).hexdigest()  # noqa: E731
    md, out = [], {}

    def tabla(t, cab, filas):
        md.append(f"\n### {t}\n")
        md.append("| " + " | ".join(cab) + " |")
        md.append("|" + "|".join("---" for _ in cab) + "|")
        md.extend("| " + " | ".join(str(x) for x in f) + " |" for f in filas)

    # A. el cambio
    num = subprocess.run(["git", "-C", str(r), "diff", "--numstat", "--", *TRES], capture_output=True, text=True,
                         check=True).stdout.strip().splitlines()
    lista = (r / TRES[2]).read_text(encoding="utf-8").splitlines()
    ok = sum(1 for x in lista if (m := re.match(r"([0-9a-f]{64})  (.+)$", x)) and sha(m.group(2)) == m.group(1))
    out["cambio"] = {"sha256": {p: sha(p) for p in TRES}, "alternativa_sha256": sha(ALT),
                     "manifiesto_igual_a_la_alternativa": (r / TRES[0]).read_bytes() == (r / ALT).read_bytes(),
                     "numstat": num, "lista_renglones": len(lista), "lista_ok": ok}
    tabla("A. El cambio y su control", ["control", "resultado"],
          [[f"sha256 de {Path(p).name}", sha(p)] for p in TRES]
          + [["el manifiesto es la alternativa, byte a byte", out["cambio"]["manifiesto_igual_a_la_alternativa"]],
             ["git diff --numstat (agregados, quitados, archivo)", "; ".join(n.replace("\t", " ") for n in num)],
             ["sha256_para_T2.txt: renglones y OK", f"{len(lista)} y {ok}"]])

    # B. el control de entradas con el manifiesto nuevo
    ce = json.loads((r / D / "control_entradas_reparto_t2.json").read_text(encoding="utf-8"))
    l_, m_ = ce["controles"]["l_sellos_manifiesto_tanda_final"], ce["controles"]["m_carga_y_control_en_contra"]
    vol = (r / D / "volcado_mensajes_copia_reparto_contra_t1.txt").read_text(encoding="utf-8").split()
    out["entradas"] = {"veredicto": ce["veredicto"], "controles": {k: v["ok"] for k, v in ce["controles"].items()},
                       "l": {k: l_[k] for k in ("estimado_usd", "tope_usd", "diferencia")}, "m": m_["control_en_contra"],
                       "volcado_igual_al_de_T1": vol[0] == vol[2]}
    tabla("B. El control de entradas con el manifiesto nuevo", ["control", "resultado"],
          [[k, "OK" if v["ok"] else "FALLA"] for k, v in ce["controles"].items()]
          + [["veredicto", ce["veredicto"]], ["l: estimado, tope y diferencia con U × tarifa + 0,209440",
                                              f"{l_['estimado_usd']}, {l_['tope_usd']}, {l_['diferencia']}"],
             ["m: carga", m_["carga"]], ["m: el contra frena en", f"{m_['control_en_contra']['documento']} (de los 33: {m_['control_en_contra']['en_un_documento_de_los_33']})"],
             ["m: el contra difiere solo en rol_alcance", m_["manifiesto_contra_difiere_solo_en_rol_alcance"]],
             ["m: sha256 del manifiesto y del contra", f"{m_['manifiesto_tanda_final_sha256']}, {m_['manifiesto_contra_sha256']}"],
             ["el volcado de los mensajes de la copia, igual al de T1", out["entradas"]["volcado_igual_al_de_T1"]]])

    # C. las tres pruebas del lanzador
    filas = []
    for log in LOGS:
        lin = (r / D / "pruebas_t2" / log).read_text(encoding="utf-8").splitlines()
        ev = [json.loads(x) for x in lin if x.startswith("{")]
        rc = next(x for x in lin if x.startswith("rc="))
        ini = next(e for e in ev if e["evento"] == "inicio_lanzador")
        cp = next(e for e in ev if e["evento"] == "controles_previos")
        fm = [e.get("resultado") for e in ev if e["evento"] == "freno_modelo_antes"] + [e["freno_modelo"] for e in ev if e["evento"] == "to_fin"]
        filas.append([log, rc, ", ".join(e["to"] for e in ev if e["evento"] == "to_inicio"),
                      f"{cp['ok']} (sha256 del manifiesto: {cp['manifiesto_sha256_ok']}; {', '.join(cp['rutas_78'])})",
                      ", ".join(fm), ", ".join(e["resultado"] for e in ev if e["evento"] == "control_entre_tramos") or "—",
                      f"autorizado_tramo_2={ini['autorizado_tramo_2']}, retomar_tras_pausa={ini['retomar_tras_pausa']}, "
                      f"hora_simulada={ini['hora_simulada']}",
                      "; ".join(e["motivo"] for e in ev if e["evento"] == "parada") or "—"])
    out["pruebas"] = filas
    tabla("C. Las tres pruebas del lanzador con el manifiesto nuevo", ["prueba", "salida", "TOs lanzados", "controles previos",
                                                                     "freno por modelo", "control entre tramos", "opciones", "parada"], filas)

    # D. las bases de la caché y el ancla de la hora de fin
    antes = (r / D / "pruebas_t2" / "bases_cache_antes_pruebas_reparto.sha").read_text(encoding="utf-8").splitlines()
    desp = (r / D / "pruebas_t2" / "bases_cache_despues_pruebas_reparto.txt").read_text(encoding="utf-8").splitlines()
    ahora = {m.group(2): sha(m.group(2)) == m.group(1) for x in antes if (m := re.match(r"([0-9a-f]{64})  (.+)$", x))}
    ancla = [x for x in (r / D / "ancla_hora_fin_T1.txt").read_text(encoding="utf-8").splitlines() if re.match(r"\d{4}-", x)]
    out["bases"] = {"despues": desp, "hoy_iguales_a_antes": ahora}
    out["ancla_hora_fin_T1"] = ancla
    tabla("D. Las bases de la caché del repo y el ancla de la hora de fin de T1", ["control", "resultado"],
          [["shasum -a 256 -c, después de las pruebas", "; ".join(desp)],
           ["hoy, contra el sha256 de antes", {Path(k).name: v for k, v in ahora.items()}]]
          + [["ancla (stat)", x] for x in ancla])
    a.md.write_text("# Cifras de la sección 15 del FRENO T1 (las genera cifras_reparto_t1.py)\n" + "\n".join(md) + "\n", encoding="utf-8")
    a.json.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"{a.md.name}: {len(md)} renglones; {a.json.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
