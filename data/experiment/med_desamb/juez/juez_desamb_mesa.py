"""Mesa, §142 y §143 (17/10/2026), U-MED-DESAMB: el juez de modelo de la cifra descriptiva de sujetos. Diseño: §8 del diseño sellado y la nota 1
(`data/experiment/med_desamb/diseno_sellado_med_desamb_2026-10-17.md`); pedido de la autora del 17/10/2026 (hoja de ruta de la mesa,
§142). Usa como biblioteca el código sellado de la planilla (`parte4/planilla_desamb_mesa.py`) y los estimadores, sin cambiarlos.

Pasos (subcomandos), en este orden:
  preparar      los ítems del juez: los 344 de la muestra del juez (lista sellada `811bd20f…`, grupo «juez») y las 52 de la lectura
                de la autora, estas tal cual las ve ella en su planilla (mismas entradas y mismo orden). Una fila que está en las dos se
                juzga una sola vez, con el formato de la planilla de la autora. Sin la vía ni el estrato. El mapa ítem → fila queda aparte
                (`--clave`), fuera del repo.
  seco          la prueba en seco: arma todos los pedidos (ítems × 3 repeticiones) SIN ENVIARLOS y sin importar el SDK, y estima los
                tokens con la regla del §5.5 del informe (caracteres / 3,5) y el costo con los precios del diseño. Los calibradores
                van con un texto de relleno del largo esperado, marcado, porque la hoja de la autora no está cargada.
  calibradores  carga la hoja de los calibradores de la autora (clase y porqué de cada entrada) y completa el lugar de los ejemplos
                resueltos del prompt. Frena si falta una clase o un porqué.
  humo          la prueba de humo, 5 llamadas reales. NO CORRE sin todos sus controles (ver `controles_de_corrida`).
  correr        la corrida entera, con los mismos controles, el registro de uso y la cuenta propios.
  evaluar       el acuerdo con las 78 clasificaciones de la autora (68 o más) y la cifra por estrato. Lee las clasificaciones de la autora
                solo acá, después de las corridas; el prompt no las ve nunca.

Requisitos de la autora (nota 1, §3, y pedido del §142):
  - los calibradores entran al prompt como ejemplos resueltos: el caso, la clase de la autora y su porqué;
  - el juez recibe la misma información que la autora, con el anexo de las entradas;
  - la salida «requiere_adjudicacion» existe y la adjudica la autora;
  - el prompt dice que el instrumento no se ajusta sin su decisión, que ningún ajuste se justifica mirando sus clasificaciones de
    las 52, y que sin 68 de 78 la cifra no se usa, sin segunda vuelta;
  - el juez no ve ninguna clasificación de la autora salvo las de los calibradores.
"""
import argparse
import csv
import hashlib
import importlib.util
import json
import random
import re
import subprocess
import sys
import time
from collections import Counter
from datetime import datetime, timedelta, timezone
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "parte4"))
import planilla_desamb_mesa as PL  # noqa: E402  (código sellado, como biblioteca)

_s = importlib.util.spec_from_file_location("estimadores_desamb_mesa", str(AQUI.parent / "parte4" / "estimadores_desamb_mesa.py"))
EST = importlib.util.module_from_spec(_s)
_s.loader.exec_module(EST)
T = PL.T
sha = PL.sha

MODELO = "claude-opus-5-5"
PRECIOS = {"in": 4.00, "out": 20.00, "cw": 5.00, "cr": 0.20}      # USD por millón (diseño, §8; comp_e1/c1/comun_c1.py:34-35)
TOPE_USD = 40.0                                                    # autorizado por la autora (diseño, §8)
REPETICIONES = 3
MAX_TOKENS = 1024
CHARS_POR_TOKEN = 3.5                                              # regla del §5.5 del informe de la mesa, NO VERIFICADA
SALIDA_TOKENS_SUPUESTA = 600                                       # supuesto del §5.5, NO VERIFICADO
VALIDEZ_MINIMA, VALIDEZ_N = 68, 78
LECTURA_CERRADA_A_MAS_TARDAR = datetime(2026, 10, 21, 18, 0, tzinfo=timezone(timedelta(hours=-3)))
VENTANA_HASTA = datetime(2026, 10, 27, 23, 59, 59, tzinfo=timezone(timedelta(hours=-3)))
CLASES = ("correcta", "generica", "incorrecta", "no_decidible", "requiere_adjudicacion")
CLASES_AUTORA = ("correcta", "generica", "incorrecta", "no_decidible")
MARCA_RELLENO = "[RELLENO DE LA PRUEBA EN SECO: la clase y el porqué de la autora van acá cuando cargue la hoja de los calibradores]"
LUGAR_CALIBRADORES = "{{CALIBRADORES_RESUELTOS_POR_LA_AUTORA}}"
N_HUMO = 5

HERRAMIENTA = {
    "name": "clasificar",
    "description": "Registra la clase de cada entrada del ítem, según el criterio, con una línea de porqué.",
    "input_schema": {"type": "object", "properties": {"entradas": {"type": "array", "items": {"type": "object", "properties": {
        "letra": {"type": "string", "description": "La letra de la entrada (A, B, …)."},
        "porque": {"type": "string", "description": "Primero: una línea que cita, entre comillas, las palabras del texto que identifican al sujeto (o dice que no las hay), y por qué esa clase."},
        "clase": {"type": "string", "enum": list(CLASES)}},
        "required": ["letra", "porque", "clase"]}}}, "required": ["entradas"]},
}

PLANTILLA = """[Repetición {repeticion} de 3 · U-MED-DESAMB]

Sos un lector de los textos ordenados del Banco Central de la República Argentina. En cada ítem hay una norma de un documento, la
relación con un sujeto (`aplica_a`: a quién se aplica; `ejecuta`: quién hace la operación), la mención del sujeto tal como aparece, el
texto propio y heredado de la unidad del documento, y una o dos entradas del catálogo de sujetos. Tu tarea es clasificar cada entrada
según el criterio de abajo. No se te dice de dónde sale cada entrada: cuando hay dos, se juzgan por separado y las dos pueden tener
cualquier clase.

## El criterio (firmado por la autora el 17/10/2026)

- **correcta:** en esa norma, el texto se refiere a ese sujeto, con ese alcance y en ese papel;
- **genérica:** el texto nombra un sujeto más específico que está en el catálogo debajo de la entrada;
- **incorrecta:** es otro sujeto, la entrada es más específica que lo que dice el texto, o el sujeto no cumple ese papel en la norma;
- **no decidible:** el texto, con su herencia, no lo identifica.

Además, **requiere_adjudicacion:** usala cuando el caso necesita la decisión de la autora, porque el texto admite dos lecturas razonables
o el criterio no alcanza para decidir. La adjudica la autora.

## Cómo responder

Usá la herramienta `clasificar` una sola vez, con una entrada por cada letra del ítem. En cada entrada va primero `porque`: una línea
que cita, entre comillas, las palabras del texto que identifican al sujeto (o dice que no las hay), y por qué esa clase. Después va
`clase`, uno de: `correcta`, `generica`, `incorrecta`, `no_decidible`, `requiere_adjudicacion`.

## Las reglas de este instrumento

Este instrumento no se ajusta sin una decisión de la autora, y ningún ajuste se justifica mirando las clasificaciones de la autora de los
52 ítems de su lectura. Si el acuerdo con ella no llega a 68 de 78, la cifra de este juez no se usa, sin segunda vuelta.

## Ejemplos resueltos por la autora

Doce casos que la autora ya clasificó, con su clase y su porqué. Son del mismo grafo y siguen el mismo criterio.

{calibradores}

## Anexo: las entradas del catálogo

{anexo}
"""


def _item(r, finales, chunks, ficha, par, iid):
    c = chunks.get(r["chunk_id"])
    n = PL._norma(r, finales)
    return {"item": iid, "documento": r["to"], "punto": r["punto"], "predicado": r["predicado"], "mencion": r["mencion"],
            "norma": {k: n.get(k) for k in ("tipo", "etiqueta", "descripcion")},
            "texto": {"propio": (c or {}).get("texto") or "", "heredado": [{"unidad": h.get("unidad_origen") or h.get("unidad"), "texto": h.get("texto") or ""}
                                                                         for h in (c or {}).get("herencia") or []], "falta": c is None},
            "entradas": [dict(ficha(i), letra=chr(65 + j)) for j, (i, _) in enumerate(par)]}


def _par(r, est, semilla, iid):
    if est == "E4":
        par = [(r["sujeto_id_modelo"], "modelo"), (r["id_regla_texto"], "regla_texto")]
        random.Random(f"{semilla}:juez:entradas:{iid}").shuffle(par)
        return par
    if est in ("E5", "E6"):
        return [(r["sujeto_id_modelo"], "modelo")]
    return [(r["resuelto_a"], "resuelto")]


def anexo_de(items, catalogo, rol_por_to):
    cat = {s["id"]: s for s in json.loads(Path(catalogo).read_text(encoding="utf-8"))["sujetos"]}
    rp = json.loads(Path(rol_por_to).read_text(encoding="utf-8"))
    docs = {}
    for archivo, v in (rp.items() if isinstance(rp, dict) else []):
        if isinstance(v, dict) and v.get("rol_id"):
            docs.setdefault(v["rol_id"], []).append(archivo)
    out = []
    for i in sorted({e["id"] for h in items for e in h["entradas"]}):
        s = cat.get(i, {})
        out.append(f"### `{i}`\n- Etiqueta: {s.get('label')}\n- Alias: {', '.join(s.get('alias') or []) or 'sin alias'}\n"
                   f"- Definición: {s.get('definicion') or 'sin definición'}\n- Padre: {s.get('padre') or 'sin padre'}")
        rol = s.get("rol") or {}
        if rol.get("miembros"):
            out[-1] += "\n- Es un rol; sus miembros: " + ", ".join(cat.get(m, {}).get("label") or m for m in rol["miembros"])
        if docs.get(i):
            out[-1] += "\n- Es el alcance de: " + ", ".join(sorted(docs[i]))
    return "\n\n".join(out)


def preparar(a):
    cuerpo = Path(a.lista).read_bytes()
    sello = json.loads(Path(a.sello).read_text(encoding="utf-8"))
    if sha(cuerpo) != sello["lista_muestra_sha256"]:
        raise SystemExit("FRENO: la lista del sorteo no es la sellada")
    if sha(Path(a.resolucion).read_bytes()) != sello["entradas_sha256"]["resolucion"]:
        raise SystemExit("FRENO: el registro de resolución no es el del sorteo")
    lst = json.loads(cuerpo)
    semilla = lst["semilla"]
    filas = {PL.clave_fila(r): r for r in PL._filas(a.resolucion)}
    pl = json.loads(Path(a.planilla_lectura).read_text(encoding="utf-8"))
    if pl["sello_de_la_lista"] != sello["lista_muestra_sha256"]:
        raise SystemExit("FRENO: la planilla de la autora no es la de esta lista")
    clave_pl = json.loads(Path(a.clave_planilla).read_text(encoding="utf-8"))
    por_item = {h["item"]: h for h in pl["items"]}
    lectura = {tuple(c["clave_de_la_fila"]): c for c in clave_pl if c["grupo"] == "lectura"}
    finales, chunks, ficha = PL._finales(a.salida_runner), PL._chunks(a.e0, a.salida_runner), PL._entradas(a.catalogo, a.rol_por_to)
    items, mapa = [], []
    for c in sorted(lectura.values(), key=lambda c: c["item"]):          # las 52, tal cual las ve la autora
        items.append(por_item[c["item"]])
        mapa.append({"item": c["item"], "grupos": ["lectura"], "clave_de_la_fila": c["clave_de_la_fila"], "estrato": c["estrato_de_la_fila"],
                     "entradas": c["entradas"]})
    k = 0
    for x in lst["lista"]:
        if x["grupo"] != "juez":
            continue
        key = tuple(x["clave"])
        if key in lectura:                                                  # la misma fila: se juzga una vez, con el formato de la autora
            m = next(m for m in mapa if tuple(m["clave_de_la_fila"]) == key)
            m["grupos"].append("juez")
            continue
        k += 1
        iid = f"J{k:03d}"
        r = filas[key]
        par = _par(r, x["estrato_de_la_fila"], semilla, iid)
        items.append(_item(r, finales, chunks, ficha, par, iid))
        mapa.append({"item": iid, "grupos": ["juez"], "clave_de_la_fila": list(key), "estrato": x["estrato_de_la_fila"],
                     "entradas": [{"letra": chr(65 + j), "id": i, "de": q} for j, (i, q) in enumerate(par)]})
    if any(h["texto"]["falta"] for h in items):
        raise SystemExit("FRENO: un ítem del juez no tiene su texto de E0")
    cal = json.loads(Path(a.planilla_calibradores).read_text(encoding="utf-8"))
    anexo = anexo_de(items + cal["items"], a.catalogo, a.rol_por_to)
    S, K = Path(a.salida), Path(a.clave)
    S.mkdir(parents=True, exist_ok=True)
    K.mkdir(parents=True, exist_ok=True)
    cuerpo_items = json.dumps({"lista_muestra_sha256": sello["lista_muestra_sha256"], "items": items}, ensure_ascii=False, indent=1) + "\n"
    (S / "items_juez.json").write_text(cuerpo_items, encoding="utf-8")
    (S / "anexo_juez.md").write_text(anexo + "\n", encoding="utf-8")
    (K / "mapa_items_juez.json").write_text(json.dumps(mapa, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    n_juez = sum(1 for m in mapa if "juez" in m["grupos"])
    n_ambos = sum(1 for m in mapa if len(m["grupos"]) == 2)
    print(f"ítems del juez: {len(items)} distintos ({n_juez} de la muestra del juez, 52 de la lectura, {n_ambos} en las dos) | "
          f"entradas {sum(len(h['entradas']) for h in items)} | anexo {len(anexo)} caracteres | items {sha(cuerpo_items.encode())[:16]}")


def _bloque_calibradores(cal_items, clases=None):
    """Los ejemplos resueltos: el caso (con el formato de la planilla), la clase y el porqué de la autora por entrada. Sin `clases`
    (prueba en seco), un relleno marcado del largo esperado."""
    out = []
    for n, h in enumerate(sorted(cal_items, key=lambda h: h["item"]), 1):
        caso = f"### Ejemplo {n}" + PL._md(h)[PL._md(h).index("\n"):]
        res = []
        for e in h["entradas"]:
            if clases is None:
                res.append(f"- Entrada {e['letra']}: porqué: {'x' * 120}; clase {MARCA_RELLENO}")
            else:
                cl, pq = clases[(h["item"], e["letra"])]
                res.append(f"- Entrada {e['letra']}: porqué: {pq}; clase **{cl}**")
        out.append(caso + "\n**Clasificación de la autora:**\n" + "\n".join(res) + "\n")
    return "\n".join(out)


def prompt_sistema(plantilla_resuelta, repeticion):
    return plantilla_resuelta.replace("{repeticion}", str(repeticion))


def contenido(item):
    """El ítem con el formato de la planilla de la autora, con un encabezado neutro: el juez no ve el número del ítem (D, de la
    lectura, o J, de la muestra del juez)."""
    md = PL._md(item)
    return "## Ítem" + md[md.index("\n"):]


def pedido(sistema, item):
    """El pedido de una llamada: el prefijo (con su punto de caché) y el ítem, con el mismo formato que la planilla."""
    return {"model": MODELO, "max_tokens": MAX_TOKENS,
            "system": [{"type": "text", "text": sistema, "cache_control": {"type": "ephemeral"}}],
            "tools": [HERRAMIENTA], "tool_choice": {"type": "tool", "name": "clasificar"},
            "messages": [{"role": "user", "content": contenido(item)}]}


def _plantilla(anexo, bloque):
    return PLANTILLA.replace("{calibradores}", bloque).replace("{anexo}", anexo)


def seco(a):
    S = Path(a.salida)
    d = json.loads((S / "items_juez.json").read_text(encoding="utf-8"))
    anexo = (S / "anexo_juez.md").read_text(encoding="utf-8").rstrip("\n")
    cal = json.loads(Path(a.planilla_calibradores).read_text(encoding="utf-8"))
    plantilla = _plantilla(anexo, _bloque_calibradores(cal["items"]))
    (S / "plantilla_prompt_juez.md").write_text(PLANTILLA, encoding="utf-8")
    # nombres técnicos de la vía y de E3, que no aparecen en el texto del corpus (las palabras comunes, como «estrato», sí podrían)
    vedado = ("metodo_resolucion", "R4_sugerencia", "regla_texto", "desacuerdo_regla_modelo", "estado_e3", "NO_DEBE_COPIARSE")
    resumen = {"modelo": MODELO, "max_tokens": MAX_TOKENS, "repeticiones": REPETICIONES, "items": len(d["items"]),
               "pedidos": 0, "caracteres": {"prefijo_por_repeticion": [], "item_total": 0}, "controles": {}}
    shas, prefijos = [], set()
    muestras = []
    for rep in range(1, REPETICIONES + 1):
        sistema = prompt_sistema(plantilla, rep)
        prefijos.add(sha(sistema.encode()))
        resumen["caracteres"]["prefijo_por_repeticion"].append(len(sistema))
        for h in d["items"]:
            p = pedido(sistema, h)
            t = json.dumps(p, ensure_ascii=False)
            if any(v in t for v in vedado):
                raise SystemExit(f"FRENO: el pedido de {h['item']} trae un dato que el juez no ve")
            shas.append(sha(t.encode()))
            resumen["pedidos"] += 1
            if rep == 1:
                resumen["caracteres"]["item_total"] += len(p["messages"][0]["content"])
                if len(muestras) < 3 and h["item"].startswith("J"):
                    muestras.append(p)
    n_items = len(d["items"])
    pref_tok = sum(resumen["caracteres"]["prefijo_por_repeticion"]) / REPETICIONES / CHARS_POR_TOKEN
    item_tok = resumen["caracteres"]["item_total"] / n_items / CHARS_POR_TOKEN
    llamadas = n_items * REPETICIONES
    costo = (REPETICIONES * pref_tok * PRECIOS["cw"] + (llamadas - REPETICIONES) * pref_tok * PRECIOS["cr"]
             + llamadas * item_tok * PRECIOS["in"] + llamadas * SALIDA_TOKENS_SUPUESTA * PRECIOS["out"]) / 1e6
    humo = (N_HUMO * (pref_tok * PRECIOS["cw"] + item_tok * PRECIOS["in"] + MAX_TOKENS * PRECIOS["out"])) / 1e6
    resumen["controles"] = {"prefijos_distintos_por_repeticion": len(prefijos) == REPETICIONES,
                            "lugar_de_los_calibradores_con_relleno_marcado": MARCA_RELLENO in plantilla,
                            "ningun_dato_vedado_en_los_pedidos": True,
                            "sdk_importado": "anthropic" in sys.modules}
    resumen["estimacion"] = {"regla": "tokens = caracteres / 3,5 (§5.5 del informe), NO VERIFICADA; salida supuesta de 600 tokens",
                             "tokens_prefijo": round(pref_tok), "tokens_item_medio": round(item_tok), "llamadas": llamadas,
                             "costo_usd": round(costo, 2), "tope_usd": TOPE_USD, "humo_cota_usd": round(humo, 4),
                             "humo_cota": "5 llamadas, cada una escribiendo el prefijo en caché y con la salida máxima"}
    resumen["sha256_de_los_pedidos"] = sha("".join(shas).encode())
    (S / "resumen_prueba_en_seco_juez.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    (S / "muestra_de_pedidos_en_seco.json").write_text(json.dumps(muestras, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    if resumen["controles"]["sdk_importado"] or not all(v for k, v in resumen["controles"].items() if k != "sdk_importado"):
        raise SystemExit(f"FRENO: un control de la prueba en seco falló: {resumen['controles']}")
    print(f"prueba en seco: {resumen['pedidos']} pedidos armados y no enviados ({n_items} ítems × {REPETICIONES}) | prefijo ~{round(pref_tok)} tokens, "
          f"ítem ~{round(item_tok)} | costo estimado USD {costo:.2f} de {TOPE_USD} | humo, cota USD {humo:.4f} | controles {resumen['controles']}")


def calibradores(a):
    """Carga la hoja de la autora y completa el lugar de los ejemplos resueltos. No lee ninguna otra clasificación suya."""
    cal = json.loads(Path(a.planilla_calibradores).read_text(encoding="utf-8"))
    hoja = list(csv.DictReader(open(a.hoja_calibradores, encoding="utf-8")))
    clases = {}
    for f in hoja:
        cl, pq = (f.get("clase") or "").strip(), (f.get("nota") or "").strip()
        if cl not in CLASES_AUTORA or not pq:
            raise SystemExit(f"FRENO: la entrada {f.get('item')}{f.get('letra')} no tiene clase válida o porqué")
        clases[(f["item"], f["letra"])] = (cl, pq)
    esperadas = {(h["item"], e["letra"]) for h in cal["items"] for e in h["entradas"]}
    if set(clases) != esperadas:
        raise SystemExit("FRENO: la hoja de los calibradores no cubre exactamente sus entradas")
    S = Path(a.salida)
    anexo = (S / "anexo_juez.md").read_text(encoding="utf-8").rstrip("\n")
    plantilla = _plantilla(anexo, _bloque_calibradores(cal["items"], clases))
    (S / "plantilla_con_calibradores.md").write_text(plantilla, encoding="utf-8")
    out = {"plantilla_sha256": sha(plantilla.encode()), "hoja_calibradores_sha256": sha(Path(a.hoja_calibradores).read_bytes()),
           "cargada": time.strftime("%Y-%m-%d %H:%M:%S %z")}
    (S / "calibradores_cargados.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("calibradores cargados:", out)


def procesos_de_extraccion(ps=None):
    salida = ps if ps is not None else subprocess.run(["ps", "-axo", "command"], capture_output=True, text=True).stdout
    return [l for l in salida.splitlines() if ("runner_corpus.py" in l or "lanzar_t" in l) and "grep" not in l]


def controles_de_corrida(a, ahora=None, ps=None, repo=None):
    """Lo que tiene que pasar antes de cualquier llamada real. Devuelve la lista de lo que falla (vacía: se puede)."""
    falla = []
    ahora = ahora or datetime.now(timezone.utc)
    S = Path(a.salida)
    if not getattr(a, "autorizacion", None):
        falla.append("falta la autorización de la autora (--autorizacion, con la hora de su mensaje)")
    if not (S / "calibradores_cargados.json").exists() or not (S / "plantilla_con_calibradores.md").exists():
        falla.append("los calibradores no están cargados")
    else:
        c = json.loads((S / "calibradores_cargados.json").read_text(encoding="utf-8"))
        if sha((S / "plantilla_con_calibradores.md").read_bytes()) != c["plantilla_sha256"]:
            falla.append("la plantilla con los calibradores no es la cargada")
    sl = Path(a.sello_lectura) if getattr(a, "sello_lectura", None) else None
    if sl is None or not sl.exists():
        falla.append("falta el sello del cierre de la lectura de la autora")
    else:
        t = datetime.strptime(json.loads(sl.read_text(encoding="utf-8"))["sellado"], "%Y-%m-%d %H:%M:%S %z")
        if t > LECTURA_CERRADA_A_MAS_TARDAR:
            falla.append("la lectura de la autora cerró después del miércoles 21/10/2026 a las 18:00: el juez no corre")
    if not getattr(a, "sello_tanda_final", None) or len(a.sello_tanda_final) < 7:
        falla.append("falta el commit del sello de la tanda final (la ventana empieza ahí)")
    if ahora > VENTANA_HASTA:
        falla.append("fuera de la ventana: después del martes 27/10/2026")
    if procesos_de_extraccion(ps):
        falla.append("hay una extracción corriendo")
    repo = repo if repo is not None else getattr(a, "repo", None)
    if repo is None:
        falla.append("falta la raíz del repo (--repo), para controlar que la salida quede fuera")
    elif Path(repo).resolve() in [S.resolve(), *S.resolve().parents]:
        falla.append("la salida del juez está dentro del repo")
    return falla


class Presupuesto:
    def __init__(self, p, tope=TOPE_USD):
        self.p, self.tope = Path(p), tope
        self.gasto = json.loads(self.p.read_text(encoding="utf-8"))["gasto_usd"] if self.p.exists() else 0.0

    def puede(self, proyeccion):
        return self.gasto + proyeccion <= self.tope

    def registrar(self, usd):
        self.gasto += usd
        self.p.write_text(json.dumps({"gasto_usd": self.gasto, "tope_usd": self.tope}) + "\n", encoding="utf-8")


def costo_de(usage):
    return (usage.get("input_tokens", 0) * PRECIOS["in"] + usage.get("output_tokens", 0) * PRECIOS["out"]
            + usage.get("cache_creation_input_tokens", 0) * PRECIOS["cw"] + usage.get("cache_read_input_tokens", 0) * PRECIOS["cr"]) / 1e6


def leer_salida(resp, letras):
    """La clasificación de una respuesta, o None si no es válida (sin tool_use, letras distintas o clase fuera de la lista)."""
    for b in getattr(resp, "content", None) or []:
        if getattr(b, "type", None) == "tool_use" and getattr(b, "name", None) == "clasificar":
            ent = (b.input or {}).get("entradas") or []
            out = {e.get("letra"): (e.get("clase"), e.get("porque")) for e in ent}
            if set(out) == set(letras) and all(c in CLASES for c, _ in out.values()):
                return out
    return None


def _usage(resp):
    u = getattr(resp, "usage", None)
    return {k: int(getattr(u, k, 0) or 0) for k in ("input_tokens", "output_tokens", "cache_creation_input_tokens", "cache_read_input_tokens")}


def _llamar(cliente, presupuesto, registro, sistema, item, rep, etiqueta):
    """Una llamada, con un solo reintento si la salida no es válida. Devuelve la clasificación o None."""
    letras = [e["letra"] for e in item["entradas"]]
    for intento in (1, 2):
        proy = costo_de({"input_tokens": len(contenido(item)) / CHARS_POR_TOKEN, "cache_creation_input_tokens": len(sistema) / CHARS_POR_TOKEN,
                         "output_tokens": MAX_TOKENS})
        if not presupuesto.puede(proy):
            raise SystemExit(f"FRENO: el tope de USD {presupuesto.tope} no alcanza para la próxima llamada (gasto {presupuesto.gasto:.4f})")
        resp = cliente.messages.create(**pedido(sistema, item))
        u = _usage(resp)
        usd = costo_de(u)
        presupuesto.registrar(usd)
        clas = leer_salida(resp, letras)
        with open(registro, "a", encoding="utf-8") as f:
            f.write(json.dumps({"etiqueta": etiqueta, "item": item["item"], "repeticion": rep, "intento": intento, "usage": u, "usd": usd,
                                "stop_reason": getattr(resp, "stop_reason", None), "valida": clas is not None,
                                "clasificacion": clas}, ensure_ascii=False) + "\n")
        if clas is not None:
            return clas
    return None


def _cliente(a):
    if getattr(a, "cliente_de_prueba", None) is not None:
        return a.cliente_de_prueba
    import anthropic  # noqa: PLC0415 — solo con una corrida real autorizada
    return anthropic.Anthropic(max_retries=3)


def _corrida(a, items, repeticiones, etiqueta):
    falla = controles_de_corrida(a, ps=getattr(a, "ps_de_prueba", None), repo=getattr(a, "repo", None))
    if falla:
        raise SystemExit("FRENO, no se llama a la API: " + "; ".join(falla))
    S = Path(a.salida)
    plantilla = (S / "plantilla_con_calibradores.md").read_text(encoding="utf-8")
    pres = Presupuesto(S / "presupuesto_juez.json")
    cliente = _cliente(a)
    out = {}
    for rep in repeticiones:
        sistema = prompt_sistema(plantilla, rep)
        for h in items:
            out[(h["item"], rep)] = _llamar(cliente, pres, S / f"registro_{etiqueta}.jsonl", sistema, h, rep, etiqueta)
    return out, pres.gasto


def controles(a):
    """La prueba en seco de la humo y de la corrida: los mismos controles, sin llamar a la API."""
    falla = controles_de_corrida(a)
    print("controles de la corrida:", "pasan" if not falla else "FRENAN: " + "; ".join(falla))
    raise SystemExit(0 if not falla else 1)


def humo(a):
    d = json.loads((Path(a.salida) / "items_juez.json").read_text(encoding="utf-8"))
    items = [h for h in d["items"] if h["item"].startswith("J")][:N_HUMO]
    out, gasto = _corrida(a, items, [1], "humo")
    print(f"humo: {len(items)} llamadas, válidas {sum(1 for v in out.values() if v)}, gasto USD {gasto:.4f}. Sus salidas no entran a la cifra.")


def correr(a):
    d = json.loads((Path(a.salida) / "items_juez.json").read_text(encoding="utf-8"))
    out, gasto = _corrida(a, d["items"], list(range(1, REPETICIONES + 1)), "corrida")
    votos = {}
    for (iid, rep), clas in out.items():
        for letra, (cl, _) in (clas or {}).items():
            votos.setdefault((iid, letra), []).append(cl)
    (Path(a.salida) / "votos_juez.json").write_text(json.dumps({f"{k[0]}|{k[1]}": v for k, v in votos.items()}, ensure_ascii=False, indent=1) + "\n",
                                                    encoding="utf-8")
    print(f"corrida: {len(out)} llamadas, gasto USD {gasto:.4f}")


def modal(votos):
    """El veredicto modal de las repeticiones válidas: la clase con 2 votos o más; sin moda, o con moda «requiere_adjudicacion», va a
    la adjudicación de la autora (None)."""
    if not votos:
        return None
    cl, n = Counter(votos).most_common(1)[0]
    return cl if n >= 2 and cl != "requiere_adjudicacion" else None


def acuerdo(juez_modal, autora):
    """El acuerdo binario (correcta o no) sobre las 78 clasificaciones de la autora. PRECISIÓN DE LA MESA, para confirmar: una entrada
    que el juez manda a adjudicación, o sin moda, cuenta como desacuerdo."""
    n = acuerdan = 0
    for k, cl_a in autora.items():
        n += 1
        cl_j = juez_modal.get(k)
        acuerdan += int(cl_j is not None and (cl_j == "correcta") == (cl_a == "correcta"))
    return {"n": n, "acuerdan": acuerdan, "valido": n == VALIDEZ_N and acuerdan >= VALIDEZ_MINIMA}


N_RS1 = {"E1": 365, "E2": 168, "E3": 1010, "E4": 277, "E5": 334, "E6": 200, "E7": 8, "E8": 16, "E9": 20}   # diseño sellado, §2


def evaluar(a):
    """Después de las corridas: el acuerdo con las 78 clasificaciones de la autora y la cifra por estrato. Es el único paso que lee la
    hoja de la autora de las 52; ningún resultado de acá vuelve al prompt."""
    S = Path(a.salida)
    votos = {tuple(k.split("|")): v for k, v in json.loads((S / "votos_juez.json").read_text(encoding="utf-8")).items()}
    mapa = json.loads(Path(a.mapa).read_text(encoding="utf-8"))
    salteados = set(re.findall(r"\bD\d{3}\b", Path(a.saltear).read_text(encoding="utf-8")))
    if len(salteados) != 12:
        raise SystemExit("FRENO: no son 12 los números que se saltean")
    hoja = [f for f in csv.DictReader(open(a.hoja_lectura, encoding="utf-8")) if f["item"] not in salteados]
    autora = {(f["item"], f["letra"]): f["clase"].strip() for f in hoja}
    if any(v not in CLASES_AUTORA for v in autora.values()):
        raise SystemExit("FRENO: la hoja de la autora tiene una clase vacía o fuera de la lista")
    juez = {k: modal(v) for k, v in votos.items()}
    ac = acuerdo(juez, autora)
    adj = {}
    if a.adjudicacion:
        adj = {(f["item"], f["letra"]): f["clase"].strip() for f in csv.DictReader(open(a.adjudicacion, encoding="utf-8"))}
    pendientes, por = [], {}
    for m in mapa:
        if "juez" not in m["grupos"]:
            continue
        e = next(x for x in m["entradas"] if x["de"] in ("modelo", "resuelto"))      # la entrada que está hoy en rs1 (la cifra principal)
        k = (m["item"], e["letra"])
        cl = juez.get(k) or adj.get(k)
        if cl is None:
            pendientes.append(list(k))
            continue
        por.setdefault(m["estrato"], []).append(cl)
    def cifras(por_estrato, n_por_estrato):
        out = {}
        for acierto, nombre in ((EST.ACIERTO, "criterio"), (EST.ACIERTO_SENSIBILIDAD, "sensibilidad")):
            est = {h: (n_por_estrato[h], sum(c in acierto for c in v), len(v)) for h, v in por_estrato.items()}
            out[nombre] = {"por_estrato": {h: {"aciertos": x[1], "n": x[2], "wilson_95": EST.wilson(x[1], x[2])} for h, x in sorted(est.items())},
                           "ponderada": EST.ponderado(est)}
        return out
    principal = cifras(por, N_RS1)
    # la cifra con las reglas aplicadas (decisión de la autora del §143), descriptiva y declarada: con S1, en E4 vale la clase que el
    # juez le dio a la entrada de la regla del texto (sale de la misma corrida); con S2, las relaciones de E6 van a cuarentena y salen
    # de la cifra de sujetos, que se informa sin E6 y con su N aparte (PRECISIÓN DE LA MESA).
    con_reglas = None
    if a.s1_paso or a.s2_paso:
        por2, pend2 = {}, []
        for m in mapa:
            if "juez" not in m["grupos"] or (a.s2_paso and m["estrato"] == "E6"):
                continue
            de = ("regla_texto",) if (a.s1_paso and m["estrato"] == "E4") else ("modelo", "resuelto")
            e = next(x for x in m["entradas"] if x["de"] in de)
            k = (m["item"], e["letra"])
            cl = juez.get(k) or adj.get(k)
            if cl is None:
                pend2.append(list(k))
                continue
            por2.setdefault(m["estrato"], []).append(cl)
        n2 = {h: v for h, v in N_RS1.items() if not (a.s2_paso and h == "E6")}
        con_reglas = {"s1": bool(a.s1_paso), "s2": bool(a.s2_paso), "a_cuarentena_por_S2": N_RS1["E6"] if a.s2_paso else 0,
                      "adjudicacion_pendiente": pend2, "cifra": cifras(por2, n2) if ac["valido"] and not pend2 else None}
    out = {"acuerdo": ac, "la_cifra_se_usa": ac["valido"], "adjudicacion_pendiente": pendientes,
           "cifra": principal if ac["valido"] and not pendientes else None,
           "cifra_con_las_reglas_aplicadas_descriptiva": con_reglas}
    (S / "evaluacion_juez.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=str) + "\n", encoding="utf-8")
    print(f"acuerdo {ac['acuerdan']} de {ac['n']} → {'se usa' if ac['valido'] else 'NO se usa, sin segunda vuelta'} | adjudicación pendiente: {len(pendientes)}")


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("preparar")
    for k in ("--lista", "--sello", "--resolucion", "--planilla-lectura", "--clave-planilla", "--planilla-calibradores", "--e0",
              "--salida-runner", "--catalogo", "--rol-por-to", "--salida", "--clave"):
        p.add_argument(k, required=True)
    s = sub.add_parser("seco")
    s.add_argument("--salida", required=True)
    s.add_argument("--planilla-calibradores", required=True)
    c = sub.add_parser("calibradores")
    for k in ("--salida", "--planilla-calibradores", "--hoja-calibradores"):
        c.add_argument(k, required=True)
    for nombre in ("humo", "correr", "controles"):
        x = sub.add_parser(nombre)
        x.add_argument("--salida", required=True)
        x.add_argument("--autorizacion", help="la hora del mensaje de la autora que autoriza esta corrida")
        x.add_argument("--sello-lectura", help="el sello del cierre de la lectura de la autora (JSON con «sellado»)")
        x.add_argument("--sello-tanda-final", help="el commit del sello de la tanda final")
        x.add_argument("--repo", required=True, help="la raíz del repo, para controlar que la salida quede fuera")
    e = sub.add_parser("evaluar")
    for k in ("--salida", "--mapa", "--hoja-lectura", "--saltear"):
        e.add_argument(k, required=True)
    e.add_argument("--adjudicacion", help="CSV de la autora con item, letra y clase de lo que el juez mandó a adjudicación")
    e.add_argument("--s1-paso", action="store_true", help="S1 pasó su regla de decisión: se informa además la cifra con S1 aplicada")
    e.add_argument("--s2-paso", action="store_true", help="S2 pasó su regla de decisión: se informa además la cifra con S2 aplicada")
    a = ap.parse_args()
    {"preparar": preparar, "seco": seco, "calibradores": calibradores, "humo": humo, "correr": correr, "evaluar": evaluar,
     "controles": controles}[a.cmd](a)


if __name__ == "__main__":
    main()
