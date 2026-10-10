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

Instrumento v1, desde el lote 2 (regla v1, §5; nota del 10/10/2026 al pie de la enmienda 1). El lote 1 se arma igual que antes.
  - La ficha no muestra ningún campo del grafo: ni el tipo, ni la etiqueta, ni la descripción del nodo, ni los tramos de E1, ni
    el id del elemento (C23). Lleva un id opaco de seis letras, derivado de la semilla del acta (C25); el mapa del id opaco al id
    del elemento va aparte, en NO_ABRIR_mapa_ids_lote<k>.json, con su sha256 en la salida.
  - Resalta solo la cuantía, ubicada con el tramo del elemento, sin mostrar la extensión del tramo (C24); ver ubicar_v1.
  - En los elementos del validador resalta el tramo del elemento (excepción declarada a C24). Si el elemento no se ubica en el
    texto o su tramo no está verificado, la ficha lo dice, no resalta nada y muestra solo lo que el elemento guarda como cuantía.
  - Si la unidad de E0 de la ficha ya salió en una ficha anterior del orden de lectura (del mismo lote o de uno anterior), la
    ficha y su bloque del formulario lo declaran (C27). No se vuelve a sortear.
  - El formulario del paso 1 no lleva la pertinencia, que va primero en el paso 2 (C7), y lleva nota (C26).
  - Los metadatos de armado, con los ids, van en NO_ABRIR_armado_lote<k>.json. La salida estándar no trae cifras del lote.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/med_umbrales/p/code/armador_fichas_P.py \
      --acta <acta_sorteo_P.json> --lote 2 --salida DIR
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
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
        spans = [T.ajustar_cuantia(txt, s, C.cuantia_del_elemento(el), C.plegar) for s in spans]
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


# ------------------------------------------------------------------------------------------- instrumento v1 (lote 2)
def opaco(semilla: str, lote: int, eid: str) -> str:
    """Id opaco de una ficha (C25): seis letras de sha256('<semilla>:ids_opacos:lote<k>:<id del elemento>'). Oculta el id a
    quien lee; no lo cifra (quien tiene el grafo y el acta lo recalcula), y por eso el mapa se sella aparte."""
    n = int(hashlib.sha256(f"{semilla}:ids_opacos:lote{lote}:{eid}".encode("utf-8")).hexdigest(), 16)
    s = ""
    for _ in range(6):
        s += chr(ord("a") + n % 26)
        n //= 26
    return s


def dentro_de_un_numero(texto: str, a: int, b: int) -> bool:
    """El span es parte de un número con punto o coma («6.3.2.2», «1.000.000»): un dígito pegado a un punto o a una coma
    del otro lado de uno de sus bordes. El número de un punto no es una cuantía (§2.3, pertinencia)."""
    return bool(re.search(r"\d[.,]$", texto[max(0, a - 2):a]) or re.match(r"[.,]\d", texto[b:b + 2]))


def literal(texto: str, span: tuple[int, int], cuantia: str) -> tuple[int, int] | None:
    """El span del literal de la cuantía (sin distinguir mayúsculas, tildes ni espacios) que empieza donde el span por
    tokens, como texto_P.ajustar_cuantia; None si el literal no está ahí."""
    toks = re.findall(r"\S+", C.plegar(cuantia))
    if not toks:
        return None
    pat = re.compile(r"\s*".join(re.escape(t) for t in toks))
    p = C.plegar(texto)
    for m in pat.finditer(p, max(0, span[0] - 3), min(len(p), span[1] + 3 + len(cuantia))):
        if abs(m.start() - span[0]) <= 3 and m.end() >= span[1]:
            return m.start(), m.end()
    return None


NO_RESALTA = "la ficha no resalta nada"


def ubicar_v1(n: dict, i: int, el: dict) -> dict:
    """Qué resalta la ficha v1: {'chunk_id', 'spans', 'como', 'avisos', 'guardado', 'metodo_comun'}.
      - tramo_verificado = «no»: no resalta; la ficha lo dice y muestra lo que el elemento guarda como cuantía.
      - Elemento del validador: el tramo del elemento, si se ubican todos sus segmentos (comun_P.ubicar); si no, no resalta.
      - Los demás: la cuantía dentro del tramo de E1 del que sale el elemento (comun_P.ubicar, «cuantia_dentro_del_tramo_de_e1»).
        Si ese tramo no la ubica, la cuantía guardada solo si aparece una vez en los textos de E0 del nodo, sin contar los
        dígitos de un número con punto o coma y prefiriendo las apariciones literales a las que coinciden solo por tokens. Si
        aparece más de una vez, o ninguna, no resalta.
    'guardado' es lo que la ficha muestra cuando no resalta (comun_P.cuantia_del_elemento: en el validador, su tramo)."""
    u = C.ubicar(n, i, el)
    textos = C.textos_nodo(n)
    txt_de = {cid: t for cid, t, _ in textos}
    cuantia = C.cuantia_del_elemento(el)
    out = {"chunk_id": u["chunk_id"] or (textos[0][0] if textos else None), "spans": [], "como": None, "avisos": [],
           "guardado": None, "metodo_comun": u["metodo"]}

    def no_resalta(motivo: str) -> dict:
        out.update(spans=[], como="sin resaltado", guardado=cuantia)
        out["avisos"].append(f"{motivo}; {NO_RESALTA}")
        return out

    if el.get("tramo_verificado") == "no":
        return no_resalta("el tramo del elemento no está verificado contra el texto")
    if C.es_validador(el):
        if u["spans"] and not u["nota"]:
            out.update(spans=list(u["spans"]), como="tramo del elemento (validador)")
            if u.get("nota_tokens"):
                out["avisos"].append("el tramo se ubicó por sus palabras (nivel «tokens» de la verificación), no literalmente")
            return out
        return no_resalta("el elemento no se ubica en el texto de E0 de la unidad")
    if u["metodo"] == "cuantia_dentro_del_tramo_de_e1":
        cid, (a, b) = u["chunk_id"], u["spans"][0]
        if not dentro_de_un_numero(txt_de[cid], a, b):
            out.update(chunk_id=cid, spans=[literal(txt_de[cid], (a, b), cuantia) or (a, b)],
                       como="cuantía dentro del tramo de E1 del elemento")
            return out
    cands = [(cid, s) for cid, t, _ in textos for s in C.ocurrencias(t, cuantia) if not dentro_de_un_numero(t, *s)]
    lits = [(cid, literal(txt_de[cid], s, cuantia)) for cid, s in cands]
    elegidas = [(cid, s) for cid, s in lits if s] or cands
    if len(elegidas) == 1:
        out.update(chunk_id=elegidas[0][0], spans=[elegidas[0][1]], como="cuantía guardada, una sola aparición en el texto")
        return out
    if elegidas:
        return no_resalta("la cuantía aparece más de una vez en el texto y el tramo del elemento no indica cuál")
    return no_resalta("el elemento no se ubica en el texto de E0 de la unidad")


def unidad_v0(n: dict, i: int, el: dict) -> str | None:
    """La unidad de E0 que muestra la ficha del lote 1 (la misma regla que ficha())."""
    return C.ubicar(n, i, el)["chunk_id"] or next((cid for cid, _, _ in C.textos_nodo(n)), None)


def procedencia(n: dict, cid: str | None) -> dict:
    return next((p for p in n.get("provenances") or [] if p.get("chunk_id") == cid), n["provenance"])


def ficha_v1(etiqueta: str, pos: int, total: int, op: str, n: dict, i: int, el: dict, lote: int,
             informada_por: str | None) -> tuple[str, dict]:
    vacio = C.estrato(el) == "V-vacío"
    r = ubicar_v1(n, i, el)
    textos = {cid: (t, ch) for cid, t, ch in C.textos_nodo(n)}
    cid = r["chunk_id"]
    txt, ch = textos.get(cid, ("", {}))
    if ABRE in txt or CIERRA in txt:
        raise SystemExit(f"{etiqueta}: el texto de E0 trae los signos del resaltado")
    p = procedencia(n, cid)
    to, archivo = p.get("to"), p.get("archivo")
    if r["spans"]:
        leyenda = "El tramo del elemento va entre ⟦ ⟧." if C.es_validador(el) else "La cuantía a juzgar va entre ⟦ ⟧."
    else:
        leyenda = "Esta ficha no resalta nada: ver los avisos, debajo del texto."
    L = [f"# Ficha {etiqueta} (lote {lote}, {pos} de {total})", "",
         f"- Id de la ficha: `{op}`", "",
         "## Texto de la unidad de E0 (la referencia)", "",
         f"Unidad `{cid}`, «{ch.get('titulo') or ''}», páginas {ch.get('paginas')}. "
         f"PDF: `{ruta_pdf(to, archivo).relative_to(C.REPO) if archivo else '(sin archivo)'}`.", "",
         leyenda, ""]
    paginas_render, piezas = [], 0
    for rot, a, b, pags in bloques(ch):
        local = [(max(x, a) - a, min(y, b) - a) for x, y in r["spans"] if x < b and y > a]
        piezas += len(local)
        L += [f"**{rot}**" + (f" (páginas {pags})" if pags else ""), "", cita(marcar(txt[a:b], local)), ""]
        if local or rot == "Texto propio":
            paginas_render += [q for q in pags if q not in paginas_render]
    if r["avisos"]:
        L += ["**Avisos**", ""] + [f"- {x}" for x in r["avisos"]]
        if r["guardado"] is not None:
            L.append(f"- lo que el elemento guarda como cuantía: «{r['guardado']}»")
        L.append("")
    if informada_por:
        L += ["**Misma unidad que otra ficha (C27)**", "",
              f"Esta ficha es de la misma unidad de E0 que la ficha {informada_por}, leída antes: su lectura queda informada por "
              f"aquella.", ""]
    L += ["## Página del PDF", ""]
    paginas_render = paginas_render[:MAX_PAGINAS]
    for q in paginas_render:
        L.append(f"![{to}, página {q}](../paginas/{to}_p{q}.png)")
    L += ["", "## Paso 1", "",
          f"Se responde en el formulario del lote (`formulario_paso1_lote{lote}.md`), bloque {etiqueta} · `{op}`"
          + (", con la pregunta única del §2.5." if vacio
             else ": los campos de la cuantía resaltada, sin la pertinencia, que se juzga primero en el paso 2 (C7).")]
    md = "\n".join(L) + "\n"
    meta = {"etiqueta": etiqueta, "opaco": op, "id": None, "to": to, "archivo": archivo, "chunk_id": cid,
            "paginas_render": paginas_render, "como": r["como"], "metodo_comun": r["metodo_comun"], "spans": r["spans"],
            "piezas_resaltadas": piezas, "avisos": r["avisos"], "guardado": r["guardado"] is not None, "vacio": vacio,
            "informada_por": informada_por}
    return md, meta


def resaltados(md: str) -> list[str]:
    """Lo resaltado en el texto citado de la ficha (las líneas «> »), sin la leyenda."""
    citado = "\n".join(x[2:] if x.startswith("> ") else "" for x in md.split("\n") if x.startswith(">"))
    return re.findall(re.escape(ABRE) + r"(.*?)" + re.escape(CIERRA), citado, re.S)


def control_ficha_v1(md: str, eid: str, n: dict, el: dict, meta: dict) -> list[str]:
    """Lo que la ficha v1 no puede mostrar (C23) y lo que tiene que resaltar (C24 y la decisión del 10/10/2026). Las fugas se
    buscan en lo que escribe el armador (todo menos las líneas citadas); el texto citado tiene que ser el de E0 de la unidad,
    igual salvo los signos del resaltado. Así una palabra de la norma que coincide con un campo («coeficiente») no frena.
    Una cuantía que E0 partió entre dos bloques (el fin de un encabezado y el comienzo del bloque que sigue) se resalta en dos
    piezas: es un solo resaltado."""
    escrito = "\n".join(x for x in md.split("\n") if not x.startswith(">"))
    malos = control_sin_campos(escrito, el)
    props = n.get("properties") or {}
    for marca in ("- Elemento:", "- Nodo:", "Descripción del nodo", "Tramos de umbral", "contiene lo resaltado"):
        if marca in escrito:
            malos.append(f"marca de la ficha v0: {marca}")
    if eid in md or n["id"] in md:
        malos.append("el id del elemento o del nodo")
    if n.get("label") and f"«{n['label']}»" in escrito:
        malos.append("la etiqueta del nodo")
    d = props.get("descripcion") or ""
    if len(d) >= 30 and d in escrito:
        malos.append("la descripción del nodo")
    txt, ch = next(((t, c) for cid, t, c in C.textos_nodo(n) if cid == meta["chunk_id"]), ("", {}))
    citado = [x for x in md.split("\n") if x.startswith(">")]
    esperado = [x for _, a, b, _ in bloques(ch) for x in cita(txt[a:b]).split("\n")]
    if [x.replace(ABRE, "").replace(CIERRA, "") for x in citado] != esperado:
        malos.append("el texto citado no es el de E0 de la unidad")
    hs = resaltados(md)
    if len(hs) != meta["piezas_resaltadas"]:
        malos.append("los resaltados no son los del armado")
    if meta["spans"] and not C.es_validador(el):
        V = C.validador()
        if len(meta["spans"]) != 1:
            malos.append("más de un resaltado en un elemento con cuantía")
        elif V.norm_tokens(" ".join(hs)) != V.norm_tokens(C.cuantia_del_elemento(el)):
            malos.append("lo resaltado no es la cuantía del elemento")
    if not meta["spans"] and (hs or not meta["guardado"]):
        malos.append("una ficha sin resaltado tiene que mostrar lo guardado, y nada resaltado")
    return malos


def control_formulario_v1(texto: str, mapa: list[dict], kg_ids: list[str]) -> list[str]:
    malos = []
    leido = F.leer(texto)
    if [(v["etiqueta"], k) for k, v in leido.items()] != [(m["etiqueta"], m["opaco"]) for m in mapa]:
        malos.append("las cabeceras no son las del mapa, en el orden de lectura")
    for k, v in leido.items():
        if not re.fullmatch(r"[a-z]{6}", k):
            malos.append(f"{v['etiqueta']}: id opaco mal formado")
        if "pertinencia" in v["campos"] or "nota" not in v["campos"]:
            malos.append(f"{v['etiqueta']}: el bloque lleva la pertinencia o no lleva la nota")
    if any(x in texto for x in kg_ids):
        malos.append("el formulario trae un id del grafo")
    return malos


def renderizar(d: Path, renders: dict) -> tuple[dict, list]:
    shas, errores = {}, []
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
    return shas, errores


def armar_v1(a, acta: dict, kg: dict, s_kg: str) -> int:
    semilla = acta["semilla"]["P"]
    orden_todos = acta["sorteo"]["orden_de_lectura"]
    orden = orden_todos[f"lote{a.lote}"]
    idx = C.indice_elementos(kg)
    d = a.salida / f"lote{a.lote}"
    if d.exists():
        raise SystemExit(f"FRENO: {d} ya existe; el armado v1 no pisa una salida")
    (d / "fichas").mkdir(parents=True)
    vistas: dict[str, str] = {}
    for k in range(1, a.lote):
        for pos, eid in enumerate(orden_todos[f"lote{k}"], 1):
            n, i, el = idx[eid]
            cid = unidad_v0(n, i, el) if k == 1 else ubicar_v1(n, i, el)["chunk_id"]
            if cid:
                vistas.setdefault(cid, f"L{k}-{pos:02d} del lote {k}")
    mapa = [{"etiqueta": f"L{a.lote}-{pos:02d}", "opaco": opaco(semilla, a.lote, eid), "id": eid}
            for pos, eid in enumerate(orden, 1)]
    if len({m["opaco"] for m in mapa}) != len(mapa):
        raise SystemExit("FRENO: dos ids opacos iguales en el lote")
    metas, bloques_form, renders = [], [], {}
    for pos, (m, eid) in enumerate(zip(mapa, orden), 1):
        n, i, el = idx[eid]
        r_cid = ubicar_v1(n, i, el)["chunk_id"]
        informada_por = vistas.get(r_cid) if r_cid else None
        md, meta = ficha_v1(m["etiqueta"], pos, len(orden), m["opaco"], n, i, el, a.lote, informada_por)
        malos = control_ficha_v1(md, eid, n, el, meta)
        if malos:
            raise SystemExit(f"FRENO: {m['etiqueta']}: {malos}")
        if r_cid:
            vistas.setdefault(r_cid, m["etiqueta"])
        meta["id"] = eid
        (d / "fichas" / f"ficha_{m['etiqueta']}.md").write_text(md, encoding="utf-8")
        metas.append(meta)
        bloques_form.append((m["etiqueta"], m["opaco"], meta["vacio"], informada_por))
        for q in meta["paginas_render"]:
            renders[(meta["to"], meta["archivo"], q)] = None
    form = F.formulario_v1(f"Formulario del paso 1, lote {a.lote} (U-MED-UMBRALES, etapa P, regla v1)", bloques_form)
    malos = control_formulario_v1(form, mapa, [x for eid in orden for x in (eid, idx[eid][0]["id"])])
    if malos:
        raise SystemExit(f"FRENO: formulario: {malos}")
    (d / f"formulario_paso1_lote{a.lote}.md").write_text(form, encoding="utf-8")
    shas, errores = ({}, []) if a.sin_render else renderizar(d, renders)
    b_mapa = (json.dumps({"lote": a.lote, "semilla": semilla,
                          "derivacion": "seis letras de sha256('<semilla>:ids_opacos:lote<k>:<id del elemento>'), "
                                        "armador_fichas_P.opaco",
                          "acta_sha256": C.sha(a.acta.read_bytes()), "fichas": mapa},
                         ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    (d / f"NO_ABRIR_mapa_ids_lote{a.lote}.json").write_bytes(b_mapa)
    b_armado = (json.dumps({"lote": a.lote, "instrumento": "v1", "acta_sha256": C.sha(a.acta.read_bytes()),
                            "grafo_sha256": s_kg, "mapa_sha256": C.sha(b_mapa),
                            "comando_render": "pdftoppm -r 110 -png -f p -l p -singlefile", "renders": shas,
                            "errores_render": errores, "fichas": metas,
                            "nota": "metadatos de armado, con los ids del grafo: no se abren antes de cerrar el paso 1 del lote"},
                           ensure_ascii=False, indent=1) + "\n").encode("utf-8")
    (d / f"NO_ABRIR_armado_lote{a.lote}.json").write_bytes(b_armado)
    if errores:
        raise SystemExit(f"FRENO: hubo errores de render; están en NO_ABRIR_armado_lote{a.lote}.json")
    print(f"lote {a.lote}, instrumento v1: fichas, formulario y páginas en {d}")
    print(f"NO_ABRIR_mapa_ids_lote{a.lote}.json sha256 {C.sha(b_mapa)}")
    print(f"NO_ABRIR_armado_lote{a.lote}.json sha256 {C.sha(b_armado)}")
    return 0


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
    if a.lote >= 2:
        return armar_v1(a, acta, kg, s_kg)
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
