"""
armador_fichas_P.py — U-MED-UMBRALES, etapa P, tramo P-a, puntos 6 y 7: las fichas del paso 1 (§5.1 de la enmienda) de un
lote, en el orden de lectura del acta, y el formulario del lote.

Cada ficha lleva:
  - el texto de la unidad de E0 del nodo, propio y heredado (e0_chunking/salida_tanda0_r2b/chunks_<to>.json, por el
    chunk_id de la procedencia), con la cuantía entre ⟦ ⟧; en los elementos del validador, el tramo de E1 del elemento;
  - los tramos de umbral que E1 devolvió para el nodo, del crudo guardado (comun_P.crudo_e1: el archivo que lee el
    ensamblado), nunca del kg.json;
  - el tipo, la etiqueta y la descripción del nodo, con la descripción marcada como salida del extractor;
  - la ruta del PDF y la página, con el render de la página (pdftoppm -r 110, como renderizar_muestra_S1.py:34);
  - si el tramo del elemento no está verificado (tramo_verificado = «no»), el aviso y el tramo guardado.
Ninguna ficha muestra un campo del umbral en el grafo (comun_P.CAMPOS_OCULTOS); el armador lo controla y aborta si
alguno aparece. Los elementos V-vacío llevan la pregunta única del §2.5.

Corre desde la raíz de la copia del repo y escribe solo en --salida/lote<k>/.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/med_umbrales/p/code/armador_fichas_P.py \
      --acta <acta_sorteo_P.json> --lote 1 --salida DIR
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import comun_P as C  # noqa: E402
import formulario_P as F  # noqa: E402
import texto_P as T  # noqa: E402

ABRE, CIERRA = "⟦", "⟧"
MAX_PAGINAS = 3


def ruta_pdf(to: str, archivo: str) -> Path:
    return (C.PDF_DEV if to in C.DEV else C.PDF_NUEVOS) / archivo


def bloques(chunk: dict) -> list[tuple[str, int, int, list]]:
    """(rótulo, inicio, fin, páginas) de cada bloque del texto completo."""
    out, pos = [], 0
    t = chunk.get("texto") or ""
    out.append(("Texto propio", 0, len(t), chunk.get("paginas") or []))
    pos = len(t)
    for k, h in enumerate(chunk.get("herencia") or [], 1):
        ht = h.get("texto") or ""
        out.append((f"Heredado, bloque {k} ({h.get('tipo')}, de {h.get('unidad_origen')})", pos + 1, pos + 1 + len(ht),
                    h.get("paginas") or []))
        pos += 1 + len(ht)
    return out


def marcar(texto: str, spans: list[tuple[int, int]]) -> str:
    for a, b in sorted(spans, reverse=True):
        texto = texto[:a] + ABRE + texto[a:b] + CIERRA + texto[b:]
    return texto


def cita(texto: str) -> str:
    return "\n".join("> " + (x if x.strip() else "") for x in texto.split("\n"))


def ficha(etiqueta: str, pos: int, total: int, eid: str, n: dict, i: int, el: dict, lote: int) -> tuple[str, dict]:
    u = C.ubicar(n, i, el)
    vacio = C.estrato(el) == "V-vacío"
    validador = C.es_validador(el)
    props = n.get("properties") or {}
    textos = {cid: (t, ch) for cid, t, ch in C.textos_nodo(n)}
    cid = u["chunk_id"] or next(iter(textos), None)
    txt, ch = textos.get(cid, ("", {}))
    spans = list(u["spans"])
    if spans and not validador:
        spans = [T.ajustar_cuantia(txt, s, el.get("tramo") or "", C.plegar) for s in spans]
    to = n["provenance"].get("to")
    archivo = n["provenance"].get("archivo")
    L = [f"# Ficha {etiqueta} (lote {lote}, {pos} de {total})", "",
         f"- Elemento: `{eid}`",
         f"- Nodo: {n['type']}, «{n.get('label')}»",
         f"- Descripción del nodo (salida del extractor; no es la referencia): «{props.get('descripcion') or ''}»", "",
         "## Texto de la unidad de E0 (la referencia)", "",
         f"Unidad `{cid}`, «{ch.get('titulo') or ''}», páginas {ch.get('paginas')}. "
         f"PDF: `{ruta_pdf(to, archivo).relative_to(C.REPO) if archivo else '(sin archivo)'}`.", "",
         ("El tramo del elemento va entre ⟦ ⟧." if validador else "La cuantía a juzgar va entre ⟦ ⟧."), ""]
    avisos = []
    if not spans:
        avisos.append("el elemento no se ubica en el texto de E0 de la unidad; abajo, el tramo guardado")
    if len(spans) > 1 and not validador:
        avisos.append(f"la cuantía aparece {len(spans)} veces en el texto y van resaltadas todas; el paso 1 se responde "
                      f"por la que corresponde a la regla del nodo")
    if u.get("nota_tokens"):
        avisos.append("el tramo se ubicó por sus palabras (nivel «tokens» de la verificación), no literalmente")
    if el.get("tramo_verificado") == "no":
        avisos.append("el tramo guardado del elemento no está verificado contra el texto (tramo_verificado = «no»)")
    paginas_render = []
    for rot, a, b, pags in bloques(ch):
        local = [(max(x, a) - a, min(y, b) - a) for x, y in spans if x < b and y > a]
        L += [f"**{rot}**" + (f" (páginas {pags})" if pags else ""), "", cita(marcar(txt[a:b], local)), ""]
        if local or rot == "Texto propio":
            paginas_render += [p for p in pags if p not in paginas_render]
    if avisos or not spans:
        L += ["**Avisos**", ""] + [f"- {x}" for x in avisos]
        if not spans or el.get("tramo_verificado") == "no":
            L.append(f"- tramo guardado del elemento: «{el.get('tramo')}»")
        L.append("")
    L += ["## Tramos de umbral que E1 devolvió para este nodo", ""]
    fuentes = sorted(set(u["fuentes_e1"].values()))
    if u["tramos_e1"]:
        L.append(f"Del crudo de E1 guardado en `corpus_tanda0/salida_r2b/{to}/` ({'; '.join(fuentes)}):")
        L.append("")
        for k, (c2, t) in enumerate(u["tramos_e1"], 1):
            marca = " ← contiene lo resaltado" if t == u.get("tramo_e1_del_elemento") else ""
            L.append(f"{k}. «{t}» (unidad `{c2}`){marca}")
    else:
        L.append(f"E1 no devolvió tramos de umbral para este nodo (crudo: {'; '.join(fuentes) or 'sin crudo'}).")
    L += ["", "## Página del PDF", ""]
    paginas_render = paginas_render[:MAX_PAGINAS]
    for p in paginas_render:
        L.append(f"![{to}, página {p}](../paginas/{to}_p{p}.png)")
    L += ["", "## Paso 1", "",
          f"Se responde en el formulario del lote (`formulario_paso1_lote{lote}.md`), bloque {etiqueta}"
          + (", con la pregunta única del §2.5." if vacio else ".")]
    md = "\n".join(L) + "\n"
    meta = {"etiqueta": etiqueta, "id": eid, "to": to, "archivo": archivo, "chunk_id": cid,
            "paginas_render": paginas_render, "ubicacion": u["metodo"], "spans": spans, "avisos": avisos,
            "vacio": vacio, "fuentes_e1": u["fuentes_e1"]}
    return md, meta


def control_sin_campos(md: str, el: dict) -> list[str]:
    """Fugas de campos del umbral en la ficha: el nombre de un campo oculto, o un valor que no puede venir del texto de
    la norma (una comparación con guion bajo o la regla_comparacion). El valor, la base o la moneda pueden estar en el
    texto de la norma, que es la referencia: no se controlan por valor."""
    malos = [c for c in C.CAMPOS_OCULTOS if f"{c}:" in md or f"«{c}»" in md or f"`{c}`" in md or f" {c} =" in md]
    v = el.get("comparacion")
    if isinstance(v, str) and "_" in v and v in md:
        malos.append(f"comparacion={v}")
    v = el.get("regla_comparacion")
    if isinstance(v, str) and v and v in md:
        malos.append(f"regla_comparacion={v}")
    return malos


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--acta", type=Path, required=True)
    ap.add_argument("--lote", type=int, required=True)
    ap.add_argument("--salida", type=Path, required=True)
    ap.add_argument("--sin-render", action="store_true")
    a = ap.parse_args()
    acta = json.loads(a.acta.read_text(encoding="utf-8"))
    kg, s_kg = C.cargar_kg()
    if s_kg != acta["grafo"]["kg_sha256"]:
        raise SystemExit("el grafo no es el del acta")
    orden = acta["sorteo"]["orden_de_lectura"][f"lote{a.lote}"]
    idx = C.indice_elementos(kg)
    d = a.salida / f"lote{a.lote}"
    (d / "fichas").mkdir(parents=True, exist_ok=True)
    metas, bloques_form, renders = [], [], {}
    for pos, eid in enumerate(orden, 1):
        n, i, el = idx[eid]
        et = f"L{a.lote}-{pos:02d}"
        md, meta = ficha(et, pos, len(orden), eid, n, i, el, a.lote)
        malos = control_sin_campos(md, el)
        if malos:
            raise SystemExit(f"{et}: la ficha muestra campos del umbral: {malos}")
        (d / "fichas" / f"ficha_{et}.md").write_text(md, encoding="utf-8")
        metas.append(meta)
        bloques_form.append((et, eid, meta["vacio"]))
        for p in meta["paginas_render"]:
            renders[(meta["to"], meta["archivo"], p)] = None
    (d / f"formulario_paso1_lote{a.lote}.md").write_text(
        F.formulario(f"Formulario del paso 1, lote {a.lote} (U-MED-UMBRALES, etapa P)", bloques_form), encoding="utf-8")
    shas, errores = {}, []
    if not a.sin_render:
        (d / "paginas").mkdir(exist_ok=True)
        for to, archivo, p in sorted(renders, key=str):
            dest = d / "paginas" / f"{to}_p{p}"
            r = subprocess.run(["pdftoppm", "-r", "110", "-png", "-f", str(p), "-l", str(p), "-singlefile",
                                str(ruta_pdf(to, archivo)), str(dest)], capture_output=True, text=True)
            png = dest.with_suffix(".png")
            if r.returncode != 0 or not png.exists():
                errores.append({"to": to, "pagina": p, "stderr": r.stderr[-300:]})
            else:
                shas[png.name] = C.sha(png.read_bytes())
    out = {"lote": a.lote, "acta_sha256": C.sha(a.acta.read_bytes()), "grafo_sha256": s_kg,
           "comando_render": "pdftoppm -r 110 -png -f p -l p -singlefile", "renders": shas, "errores_render": errores,
           "fichas": metas,
           "nota": "metadatos de armado; no contiene ningún campo del umbral en el grafo"}
    (d / f"fichas_lote{a.lote}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(json.dumps({"lote": a.lote, "fichas": len(metas), "renders": len(shas), "errores_render": len(errores),
                      "ubicacion": {m["ubicacion"]: sum(1 for x in metas if x["ubicacion"] == m["ubicacion"]) for m in metas},
                      "con_avisos": sum(1 for m in metas if m["avisos"])}, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
