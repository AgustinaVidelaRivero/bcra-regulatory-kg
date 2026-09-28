#!/usr/bin/env python3
"""U-INV-RECORRIDO, Paso 4 — trazas persistidas de EV2F-013 (ancla ext:3.17).

Solo lectura del repositorio; escribe únicamente en /tmp/u_inv_ejemplo/.
Para cada archivo de traza: grafo, etiqueta de corrida y la secuencia de
llamadas (herramienta e input, textuales, de steps_full) hasta la primera
llamada ver_nodo cuyo output lista una procedencia con 3.17.1.4; si ninguna
lo hace, la secuencia completa y «nunca lo abrió». Se excluyen los archivos
*_SOLO_MESA y las trazas de selftest (cliente simulado).
Uso: PYTHONDONTWRITEBYTECODE=1 python3 /tmp/u_inv_ejemplo/uinvrec_trazas.py <raíz del repo>
"""
import hashlib, json, os, re, sys

RAIZ = os.path.abspath(sys.argv[1])
OUT = "/tmp/u_inv_ejemplo/uinvrec_trazas_resultado.json"
TRAZAS = [
    "data/experiment/ev2_corrida/trazas/ev2_base_run3/EV2F-013.json",
    "data/experiment/ev2_corrida/trazas/ev2_base_v2/EV2F-013.json",
    "data/experiment/ev2_corrida/trazas/ev2_base_v3/EV2F-013.json",
    "data/experiment/ev2_r1/trazas/ev2_r1_base/EV2F-013.json",
    "data/experiment/ev2_encadenamiento/trazas/ev2_enc_run3_r1/EV2F-013.json",
    "data/experiment/ev2_encadenamiento/trazas/ev2_enc_run3_r2/EV2F-013.json",
    "data/experiment/ev2_encadenamiento/trazas/ev2_enc_run3_r3/EV2F-013.json",
    "data/experiment/ev2_encadenamiento/trazas/ev2_enc_v2_r1/EV2F-013.json",
    "data/experiment/ev2_encadenamiento/trazas/ev2_enc_v2_r2/EV2F-013.json",
    "data/experiment/ev2_encadenamiento/trazas/ev2_enc_v2_r3/EV2F-013.json",
]
PAT = re.compile(r"3\.17\.1\.4(?![0-9])")


def main():
    salida = []
    for rel in TRAZAS:
        p = os.path.join(RAIZ, rel)
        raw = open(p, "rb").read()
        t = json.loads(raw)
        m, tr, sf = t["meta"], t["trace"], t.get("steps_full") or []
        if len(sf) != tr.get("tool_calls_used"):
            raise SystemExit(f"{rel}: steps_full no está 1:1 con tool_calls_used")
        llamadas, abierto = [], None
        for s in sf:
            fila = {"n": s["n"], "tool": s["tool"], "input": s["input"]}
            out = s["output"] if isinstance(s["output"], dict) else {}
            if s["tool"] == "ver_nodo":
                locs = [pv.get("location") for pv in (out.get("provenances") or [])]
                fila["ver_nodo_resultado"] = {"id": out.get("id"), "type": out.get("type"),
                                              "label": out.get("label"), "locations": locs,
                                              "error": out.get("error")}
                if abierto is None and any(PAT.search(str(l or "")) for l in locs):
                    abierto = s["n"]
            if s["tool"] == "buscar_nodos":
                fila["buscar_nodos_ids"] = [r.get("id") for r in out.get("resultados", [])]
                fila["total_con_match"] = out.get("total_con_match")
            if s["tool"] == "ver_vecinos":
                fila["ver_vecinos_totales"] = {"n_salientes_total": out.get("n_salientes_total"),
                                               "n_entrantes_total": out.get("n_entrantes_total")}
            llamadas.append(fila)
        vistas = [pv for pv in tr.get("seen_provenances") or [] if PAT.search(str(pv.get("location") or ""))]
        salida.append({
            "archivo": rel, "sha256": hashlib.sha256(raw).hexdigest(),
            "label": m.get("label"), "grafo": m.get("grafo"), "kg_path": m.get("kg_path"),
            "kg_sha256": m.get("kg_sha256"), "timestamp_inicio": m.get("timestamp_inicio"),
            "pregunta": tr.get("question"), "tool_calls_used": tr.get("tool_calls_used"),
            "hit_tool_limit": tr.get("hit_tool_limit"),
            "primera_apertura_3_17_1_4": abierto,
            "procedencias_3_17_1_4_vistas_en_la_traza": vistas,
            "llamadas": llamadas})
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(salida, fh, ensure_ascii=False, indent=1)

    for c in salida:
        print(f"\n=== {c['archivo']}")
        print(f"    label {c['label']} · grafo {c['grafo']} · {c['kg_path']} · kg sha {c['kg_sha256'][:12]}… · "
              f"{c['timestamp_inicio']} · tool calls {c['tool_calls_used']} · tope {c['hit_tool_limit']}")
        print(f"    primera apertura con 3.17.1.4: "
              f"{'llamada ' + str(c['primera_apertura_3_17_1_4']) if c['primera_apertura_3_17_1_4'] else 'NUNCA'}"
              f"   · procedencias 3.17.1.4 vistas en toda la traza: {len(c['procedencias_3_17_1_4_vistas_en_la_traza'])}")
        tope = c["primera_apertura_3_17_1_4"] or len(c["llamadas"])
        for f in c["llamadas"][:tope]:
            extra = ""
            if "ver_nodo_resultado" in f:
                v = f["ver_nodo_resultado"]
                extra = f"  -> {v['type']} «{v['label']}» {v['locations']}" if not v["error"] else f"  -> error"
            elif "buscar_nodos_ids" in f:
                extra = f"  -> total {f['total_con_match']}, {len(f['buscar_nodos_ids'])} devueltos"
            elif "ver_vecinos_totales" in f:
                extra = f"  -> {f['ver_vecinos_totales']}"
            print(f"    {f['n']:2d} {f['tool']:12s} {json.dumps(f['input'], ensure_ascii=False)}{extra}")
    print(f"\nJSON: {OUT}  sha256 {hashlib.sha256(open(OUT, 'rb').read()).hexdigest()}")


if __name__ == "__main__":
    main()
