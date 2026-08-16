"""
analisis_acuerdo.py — Acuerdo juez-humana sobre la pasada de calibración
(pre-registro §5). Paso POSTERIOR y separado del driver: es la única pieza de
este directorio que abre la adjudicación humana de U6, y lo hace después de
que todos los veredictos del juez ya están persistidos.

Produce:
  - acuerdo por pregunta: veredicto del mapping §2 vs veredicto humano del
    jsonl (correcta/parcial/incorrecta ↔ correcto/parcial/incorrecto;
    `requiere_adjudicacion` se reporta aparte, no cuenta como acuerdo ni
    desacuerdo: es la salida "no decido" del instrumento);
  - acuerdo por criterio: NO computable directamente — la adjudicación humana
    es por pregunta; se ofrece el proxy que sí lo es: para las preguntas
    humanas `correcta`, todos los criterios deberían ser cumplidos; para las
    `incorrecta`, ninguno; las `parcial` no fijan criterio a criterio;
  - reporte de desacuerdos con TODO el material para adjudicar (pregunta,
    criterio, cita, fragmentos señalados por el juez, 3 veredictos, humano) y
    una PRE-clasificación evidencia/etiqueta con su regla explícita, que la
    autora confirma o corrige.

Regla de pre-clasificación (mecánica, declarada):
  - "evidencia": en el par decisivo el juez señaló fragmento nulo (ausencia)
    o el fragmento no aparece verbatim en la respuesta, o las 3 reps
    señalaron fragmentos distintos → el juez no fijó bien la evidencia;
  - "etiqueta": las 3 reps coinciden en fragmento (o en ausencia) y la
    justificación discute calificadores/alcance → evidencia localizada,
    clasificación distinta en zona fronteriza.
  Es un punto de partida para la adjudicación, no un veredicto.
"""

from __future__ import annotations

import json
from collections import Counter
from pathlib import Path

JUEZ_DIR = Path(__file__).resolve().parent
EXP_DIR = JUEZ_DIR.parent
ADJ_PATH = EXP_DIR / "exploracion" / "adjudicacion" / "u6_adjudicacion_humana.jsonl"
CRIT_PATH = EXP_DIR / "exploracion" / "u6_fidelidad" / "criterios_u6.json"
import argparse
_ap = argparse.ArgumentParser()
_ap.add_argument("--out", type=Path, default=JUEZ_DIR / "out")
_ap.add_argument("--fuente-respuestas", choices=("trazas", "app"), default="trazas")
_ARGS = _ap.parse_args()
AGG_PATH = _ARGS.out / "veredictos_agregados.json"
OUT_JSON = _ARGS.out / "acuerdo_juez_humana.json"
OUT_MD = _ARGS.out / "reporte_desacuerdos.md"

MAPA_H = {"correcta": "correcto", "parcial": "parcial", "incorrecta": "incorrecto"}


def main() -> int:
    agg = json.loads(AGG_PATH.read_text(encoding="utf-8"))
    hum = {json.loads(l)["qid"]: json.loads(l)["veredicto"]
           for l in ADJ_PATH.read_text(encoding="utf-8").splitlines() if l}
    crit = {p["id"]: p for p in json.loads(CRIT_PATH.read_text(encoding="utf-8"))["preguntas"]}
    import sys
    sys.path.insert(0, str(JUEZ_DIR))
    from driver_calibracion import cargar_respuestas, cargar_respuestas_app, cargar_preguntas
    preg = cargar_preguntas()
    resp = cargar_respuestas_app(preg) if _ARGS.fuente_respuestas == "app" else cargar_respuestas()

    filas, desac, adjud = [], [], []
    for a in agg["agregados"]:
        q = a["qid"]
        h = MAPA_H[hum[q]]
        j = a["veredicto_pregunta"]
        estado = ("requiere_adjudicacion" if j == "requiere_adjudicacion"
                  else "acuerdo" if j == h else "desacuerdo")
        filas.append({"qid": q, "humano": h, "juez": j, "estado": estado,
                      "modales": [c["modal"] for c in a["criterios"]],
                      "clasif_reps": a["clasificacion_respuesta_reps"],
                      "respondible_flag": a["respondible_flag"]})
        if estado == "desacuerdo":
            desac.append(a)
        elif estado == "requiere_adjudicacion":
            adjud.append(a)

    n = len(filas)
    n_acu = sum(f["estado"] == "acuerdo" for f in filas)
    n_des = sum(f["estado"] == "desacuerdo" for f in filas)
    n_adj = sum(f["estado"] == "requiere_adjudicacion" for f in filas)
    matriz = Counter((f["humano"], f["juez"]) for f in filas)

    # proxy por criterio (solo donde el veredicto humano fija todos los criterios)
    proxy = {"correcta→todos_cumplido": [0, 0], "incorrecta→ninguno_cumplido": [0, 0]}
    for f in filas:
        if f["humano"] == "correcto":
            for m in f["modales"]:
                proxy["correcta→todos_cumplido"][1] += 1
                proxy["correcta→todos_cumplido"][0] += (m == "cumplido")
        elif f["humano"] == "incorrecto":
            for m in f["modales"]:
                proxy["incorrecta→ninguno_cumplido"][1] += 1
                proxy["incorrecta→ninguno_cumplido"][0] += (m == "no_cumplido")

    # no-determinismo por par
    pares = [c for a in agg["agregados"] for c in a["criterios"]]
    unanimes = sum(len(set(c["veredictos_reps"])) == 1 for c in pares)
    dist_modal = Counter(c["modal"] for c in pares)
    dist_todos = Counter(v for c in pares for v in c["veredictos_reps"])

    # clasificación auxiliar vs flag
    aux = [(f["qid"], Counter(f["clasif_reps"]).most_common(1)[0][0], f["respondible_flag"])
           for f in filas]

    def _plano(s: str) -> str:
        # comparación de fragmentos tolerante a marcadores markdown y comillas
        # tipográficas (el juez suele devolver el texto sin ** ni «»); no altera letras
        for ch in ("**", "*", "«", "»", "“", "”", "\"", "'", "‘", "’", "`"):
            s = s.replace(ch, "")
        return " ".join(s.split())

    def estado_fragmento(fr, texto_resp, cita_gold):
        """null | verbatim | fuga_gold | no_verbatim (comparación case-insensitive
        tolerante a markdown/comillas; 'fuga_gold' = el fragmento está en la cita
        del gold y NO en la respuesta)."""
        if fr is None:
            return "null"
        f = _plano(fr).lower()
        if f in _plano(texto_resp).lower():
            return "verbatim"
        if f in _plano(cita_gold).lower():
            return "fuga_gold"
        return "no_verbatim"

    def preclasificar(a, c, texto_resp):
        frs = c["fragmentos_reps"]
        nulos = sum(fr is None for fr in frs)
        no_verbatim = sum(1 for fr in frs if fr and _plano(fr) not in _plano(texto_resp))
        distintos = len({(fr or "").strip()[:60] for fr in frs})
        if no_verbatim or (nulos and nulos < 3) or distintos > 1:
            return "evidencia", f"nulos={nulos}/3, no_verbatim={no_verbatim}/3, fragmentos_distintos={distintos}"
        return "etiqueta", f"fragmento consistente en 3/3 (nulos={nulos}/3)"

    # auditoría global de fragmentos (verbatim / no_verbatim / fuga_gold / null)
    audit = Counter()
    fugas = []
    for a in agg["agregados"]:
        for c in a["criterios"]:
            gold = crit[a["qid"]]["gold"]["criterios"][c["indice"] - 1]["cita_textual"]
            for r, fr in enumerate(c["fragmentos_reps"]):
                est = estado_fragmento(fr, resp[a["qid"]]["respuesta"], gold)
                audit[est] += 1
                if est in ("fuga_gold", "no_verbatim"):
                    fugas.append({"qid": a["qid"], "indice": c["indice"], "rep": r + 1,
                                  "veredicto": c["veredictos_reps"][r], "estado": est,
                                  "fragmento": (fr or "")[:160]})

    def bloque(a, tipo):
        q = a["qid"]
        h = MAPA_H[hum[q]]
        out = [f"## {q} — humano: **{h}** · juez (mapping): **{a['veredicto_pregunta']}** [{tipo}]",
               "", f"**Pregunta:** {preg[q]['pregunta']}", "",
               f"**Respuesta del agente (íntegra):**", "", "> " + resp[q]["respuesta"].replace("\n", "\n> "), "",
               f"Clasificación auxiliar (3 reps): {a['clasificacion_respuesta_reps']} · flag respondible: {a['respondible_flag']}",
               ""]
        for c in a["criterios"]:
            gold = crit[q]["gold"]["criterios"][c["indice"] - 1]
            pre, razon = preclasificar(a, c, resp[q]["respuesta"])
            marca = "" if len(set(c["veredictos_reps"])) == 1 else " ⚠ no unánime"
            out += [f"### criterio {c['indice']} → modal **{c['modal']}** ({c['veredictos_reps']}){marca}",
                    f"- criterio: {gold['criterio']}",
                    f"- cita del gold: «{gold['cita_textual']}»"]
            for r in range(3):
                fr = c["fragmentos_reps"][r]
                est = estado_fragmento(fr, resp[q]["respuesta"], gold["cita_textual"])
                out.append(f"- rep {r+1} [{c['veredictos_reps'][r]}] fragmento ({est}): "
                           f"{('«' + fr + '»') if fr else 'null (ausencia)'} — {c['justificaciones_reps'][r]}")
            out.append(f"- pre-clasificación mecánica del par: **{pre}** ({razon})")
            out.append("")
        return out

    md = [f"# Reporte de desacuerdos y adjudicaciones — calibración juez EV2 v1 sobre U6 (fuente respuestas: {_ARGS.fuente_respuestas})",
          "", f"Prompt sha256: `{agg['agregados'] and json.loads((JUEZ_DIR/'out'/'veredictos_r1.jsonl').read_text().splitlines()[0])['meta']['prompt_sha256']}`",
          f"Orden: semilla `{agg['semilla_orden']}`, N={agg['reps']}", "",
          "## Resumen", "",
          f"- Preguntas: {n} — acuerdo {n_acu} · desacuerdo {n_des} · requiere_adjudicacion {n_adj}",
          f"- Acuerdo sobre las decididas: {n_acu}/{n_acu + n_des}",
          f"- Matriz (humano → juez): " + ", ".join(f"{h}→{j}: {k}" for (h, j), k in sorted(matriz.items())),
          f"- Proxy por criterio: correcta→todos cumplido {proxy['correcta→todos_cumplido'][0]}/{proxy['correcta→todos_cumplido'][1]}; "
          f"incorrecta→ninguno cumplido {proxy['incorrecta→ninguno_cumplido'][0]}/{proxy['incorrecta→ninguno_cumplido'][1]}",
          f"- No-determinismo: pares unánimes {unanimes}/{len(pares)}; modales {dict(dist_modal)}; "
          f"todos los veredictos {dict(dist_todos)}",
          f"- Fragmentos ({sum(audit.values())}): {dict(audit)}" +
          ("" if not fugas else " — detalle no-verbatim/fuga_gold: " +
           "; ".join(f"{x['qid']} c{x['indice']} r{x['rep']} [{x['veredicto']}] {x['estado']}" for x in fugas)),
          f"- Clasificación auxiliar modal vs flag respondible: " +
          "; ".join(f"{q}:{cl}/flag={fl}" for q, cl, fl in aux if cl == "abstencion" or fl is False),
          "", "---", "", "# A. Desacuerdos (juez decidió distinto del humano)", ""]
    for a in desac:
        md += bloque(a, "DESACUERDO")
    md += ["---", "", "# B. requiere_adjudicacion (el instrumento no decidió)", ""]
    for a in adjud:
        md += bloque(a, "ADJUDICACIÓN")
    OUT_MD.write_text("\n".join(md), encoding="utf-8")

    OUT_JSON.write_text(json.dumps({
        "n": n, "acuerdo": n_acu, "desacuerdo": n_des, "requiere_adjudicacion": n_adj,
        "matriz_humano_juez": {f"{h}→{j}": k for (h, j), k in sorted(matriz.items())},
        "proxy_criterio": proxy,
        "no_determinismo": {"pares": len(pares), "unanimes": unanimes,
                            "modales": dict(dist_modal), "todos": dict(dist_todos)},
        "auxiliar_vs_flag": aux, "fragmentos_auditoria": dict(audit),
        "fragmentos_no_verbatim_o_fuga": fugas, "por_pregunta": filas,
    }, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"acuerdo {n_acu} / desacuerdo {n_des} / adjudicación {n_adj} de {n}")
    print("matriz:", dict(matriz))
    print(f"→ {OUT_JSON}\n→ {OUT_MD}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
