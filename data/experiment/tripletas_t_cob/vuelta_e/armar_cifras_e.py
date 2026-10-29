"""
armar_cifras_e.py — U-COB-T, vuelta e, paso 6: el archivo de las cifras para la autora (CIFRAS_COB_T_e_PARA_LA_AUTORA.md, en
tripletas_t_cob/), sacadas por código de los dos JSON de salidas_e/ (acuerdo_juez_cob_t_e.json y cifras_600_cob_t_e.json), nunca a
mano. Las reglas, las del documento de la cobertura en HEAD: el acuerdo (primera nota, punto 9), el orden (punto 10), lo que se
informa (punto 11) y el recall depurado (segunda nota, punto 4). Ninguna ref, ningún texto de un pasaje, de una tripleta ni de una
nota: de D-9 entran solo las cuentas, no sus listas de refs ni el bloque por ref.
La consola no muestra ninguna cifra: solo el nombre del archivo, su sha256 y los controles en sí o no (que no trae ninguna ref,
que tiene sus seis partes y que cada cifra sale de una clave de los JSON).
  env -i PATH=… HOME=… PYTHONDONTWRITEBYTECODE=1 python3 -I -B armar_cifras_e.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path.home() / "INGENIERIA IA" / "TESIS" / "fuera_del_repo" / "tripletas_t_cob" / "codigo"))
import comun_cob_t as T  # noqa: E402
import comun_600_cob_t as M  # noqa: E402

SE = T.RAIZ / "salidas_e"
ACUERDO, CIFRAS = SE / "acuerdo_juez_cob_t_e.json", SE / "cifras_600_cob_t_e.json"
SALIDA = T.RAIZ / "CIFRAS_COB_T_e_PARA_LA_AUTORA.md"
DISTRIBUCION = {"unanimidad": "unanimidad", "2_a_1": "2 a 1", "mayoria_con_error": "mayoría con una repetición sin salida",
                "sin_consenso": "sin consenso"}
PARTES = ("## 1. El acuerdo del juez", "## 2. El orden", "## 3. El recall@10, @50 y @100",
          "## 4. Si el orden no pasa", "## 5. D-9 sobre las 30", "## 6. Los sha256")


def num(v: float | None, d: int = 3) -> str:
    return "—" if v is None else f"{v:.{d}f}".replace(".", ",")


def si(x: bool) -> str:
    return "sí" if x else "no"


def prop(p: dict) -> str:
    """x / n = proporción (Wilson al 95 %: a – b)."""
    w = p["wilson95"]
    return (f"{p['x']} / {p['n']} = {num(p['proporcion'])}" + (f" (Wilson al 95 %: {num(w[0])} a {num(w[1])})" if w else ""))


def bloque_recall(b: dict) -> list[str]:
    c, d = b["crudo"], b["depurado"]
    return [f"  - **crudo:** presentes {prop(c['presentes'])}; parciales, aparte, {prop(c['parciales_aparte'])}; "
            f"ausentes {c['ausentes']};",
            f"  - **depurado:** presentes {prop(d['presentes'])}; parciales, aparte, {prop(d['parciales_aparte'])}; "
            f"ausentes {d['ausentes']};",
            f"  - ausentes que salen por error del gold (la autora las marca «no» según el pasaje): "
            f"{b['ausentes_incorrectas_errores_del_gold']}; «no decidible», que quedan en el denominador: {b['no_decidibles']}."]


def armar(a: dict, c: dict, s_a: str, s_c: str, s_script: str) -> str:
    o, d9 = c["orden"], c["d9"]
    dist = a["distribucion_de_las_repeticiones"]
    L = ["# Cifras de la cobertura de T, vuelta e: para la autora", "",
         "Sacadas por `armar_cifras_e.py` de los dos JSON de `salidas_e/`, que escribieron `acuerdo_juez_cob_t.py` y "
         "`cifras_600_cob_t.py` de la vuelta c, sin cambios, sobre una copia de `lectura/`. Las reglas son las del documento de "
         "la cobertura en HEAD. Ninguna ref ni ningún texto.", "",
         "## 1. El acuerdo del juez (primera nota, punto 9)", "",
         f"- **Acuerdan:** {a['acuerdan']} de {a['n']} (no acuerdan {a['desacuerdan']}).",
         f"- **El juez manda a adjudicación:** {a['juez_a_adjudicacion']}; **deja sin consenso:** {a['juez_sin_consenso']}. "
         "Las dos cuentan como desacuerdo.",
         f"- **Kappa de Cohen** sobre las tres clases, en las que deciden los dos: {num(a['kappa'], 4)} (n = {a['deciden_los_dos']}).",
         "- **La distribución de las repeticiones:** "
         + "; ".join(f"{DISTRIBUCION.get(k, k)} {v}" for k, v in sorted(dist.items(), key=lambda kv: -kv[1])) + ".",
         f"- **Escala:** {si(a['escala'])}. La regla del punto 9: el juez escala si acuerda en al menos {a['umbral']}.", "",
         "## 2. El orden (primera nota, punto 10)", "",
         f"- **Esenciales o útiles en las {o['primeras']} primeras:** {o['esenciales_o_utiles_en_las_primeras']} "
         f"(proporción {num(o['proporcion_primeras'])}).",
         f"- **En las {o['control']} de control:** {o['esenciales_o_utiles_en_el_control']} "
         f"(proporción {num(o['proporcion_control'])}).",
         f"- **Pasa:** {si(o['pasa'])}. La regla del punto 10: {o['regla']}.",
         "- La importancia, por clase: en las primeras, "
         + ", ".join(f"{k} {v}" for k, v in sorted(c["importancia_de_las_primeras"].items()))
         + "; en el control, " + ", ".join(f"{k} {v}" for k, v in sorted(c["importancia_del_control"].items())) + ".", "",
         "## 3. El recall@10, @50 y @100 (primera nota, punto 11; el depurado, segunda nota, punto 4)", "",
         "Presentes / k con Wilson al 95 %, en las 100 primeras por su posición; las parciales, aparte. El depurado saca del "
         "denominador solo las ausentes que la autora marca «no» según el pasaje; las «no decidible» quedan y se cuentan.", ""]
    for k, b in c["recall"].items():
        L += [f"- **recall{k}** (posiciones {b['posiciones']}):", *bloque_recall(b)]
    L += ["", "## 4. Si el orden no pasa: el recall sobre las esenciales, sin el orden", ""]
    if o["pasa"]:
        L += ["- El orden pasa: no corresponde."]
    else:
        e = c["recall_sobre_las_esenciales_sin_orden"]
        L += [f"- **Sobre las {e['n']} que la autora marcó esenciales:**", *bloque_recall(e)]
    L += ["", "## 5. D-9 sobre las 30 (primera nota, punto 12), como lo da el script", "",
          f"- **Sorteadas:** {d9['n_sorteadas']}; descartadas en la extracción: {d9['descartadas_en_la_extraccion']['n']}"
          + (" (" + ", ".join(f"{k} {v}" for k, v in sorted(d9["descartadas_en_la_extraccion"]["por_causa"].items())) + ")"
             if d9["descartadas_en_la_extraccion"]["por_causa"] else "") + f"; filas de la hoja: {d9['filas_de_la_hoja']}.",
          f"- **No decidibles:** {d9['no_decidibles']['n']}; decididas: {d9['decididas']}; incorrectas (errores del gold): "
          f"{d9['incorrectas_errores_del_gold']['n']}.",
          f"- **Cruda** (sobre las {d9['cruda']['n']} decididas): presentes {prop(d9['cruda']['presentes'])}; parciales, aparte, "
          f"{prop(d9['cruda']['parciales_aparte'])}; ausentes {d9['cruda']['ausentes']}.",
          f"- **Depurada** (sobre las {d9['depurada']['n']} correctas): presentes {prop(d9['depurada']['presentes'])}; parciales, "
          f"aparte, {prop(d9['depurada']['parciales_aparte'])}; ausentes {d9['depurada']['ausentes']}.",
          f"- La regla: {d9['regla']}. El intervalo: {d9['intervalo']}.", "",
          "## 6. Los sha256", "",
          f"- `salidas_e/acuerdo_juez_cob_t_e.json`: `{s_a}`",
          f"- `salidas_e/cifras_600_cob_t_e.json`: `{s_c}`",
          f"- `armar_cifras_e.py`, el script que armó este archivo: `{s_script}`",
          f"- Lo que leyeron los dos scripts: la hoja de presencia `{c['hoja_presencia_sha256']}` (en el acuerdo, "
          f"`{a['hoja_sha256']}`), la de importancia `{c['hoja_importancia_sha256']}`, el orden `{c['orden_sha256']}` y los "
          f"veredictos del juez `{a['juez_sha256']}`.", ""]
    return "\n".join(L)


def main() -> int:
    if SALIDA.exists():
        print(f"FRENO: {SALIDA.name} ya existe")
        return 1
    a = json.loads(ACUERDO.read_text(encoding="utf-8"))
    c = json.loads(CIFRAS.read_text(encoding="utf-8"))
    texto = armar(a, c, T.sha_archivo(ACUERDO), T.sha_archivo(CIFRAS), T.sha_archivo(Path(__file__).resolve()))
    sin_refs = not M.PATRON_REFS.search(texto)
    partes = all(p in texto for p in PARTES)
    d = c["d9"]
    refs_d9 = (d["descartadas_en_la_extraccion"]["refs"] + d["no_decidibles"]["refs"] + d["incorrectas_errores_del_gold"]["refs"]
               + list(d["por_ref"]))
    sin_listas = not any(str(r) in texto for r in refs_d9)
    if not (sin_refs and partes and sin_listas):
        print(f"FRENO: el archivo no pasa sus controles (sin refs {si(sin_refs)}, seis partes {si(partes)}, sin las listas de "
              f"D-9 {si(sin_listas)}); no se escribe")
        return 1
    SALIDA.write_text(texto, encoding="utf-8")
    print(f"{SALIDA.name}: {T.sha_archivo(SALIDA)}")
    print(f"sin ninguna ref: {si(sin_refs)}; con sus seis partes: {si(partes)}; sin las listas de refs de D-9: {si(sin_listas)}")
    print(f"armar_cifras_e.py: {T.sha_archivo(Path(__file__).resolve())}")
    return 0


if __name__ == "__main__":
    sys.dont_write_bytecode = True
    raise SystemExit(main())
