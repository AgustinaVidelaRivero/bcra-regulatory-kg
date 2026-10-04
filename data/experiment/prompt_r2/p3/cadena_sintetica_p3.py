"""
cadena_sintetica_p3.py — U-PROMPT-R2, P3.b y P3.c (USD 0, sin API): la cadena de lectura del perfil r2b sobre un
crudo sintético que cubre cada campo nuevo, y las shapes (S27 en fase r2b) y la suite (LN-3 y LN-7) sobre el grafo
que sale. Es también el selftest de entrada_r2 con la forma r2 (nota del 04/10/2026 al mandato, puntos b y c).

Arma en <salida>/corrida/cla/ los archivos de una corrida r2b de cinco unidades de cla sobre la e0-r2
(extracciones_e1_compact.jsonl, finales.jsonl y reintentos_e3.jsonl), con el crudo en la forma r2 y, como
validación de E1, la que produce validador_e1 con el perfil r2b (lo que vio E3):
  - cla::5.1.1.1 (ítem de lista): tramo de dos segmentos, umbral con cuantía, Condicion → Operacion (firma
    nueva), un tipo por alias, otras_propiedades en una relación, relacion_sin_predicado con source y destino, y
    una relación del crudo que la validación guardada no pasó a E3 (simula una divergencia entre los validadores);
  - cla::3.7: Definicion con término literal y una ley como Comunicacion «externa»;
  - cla::6.5::intro: límite relativo (tramo sin cuantía) y mención sin id;
  - cla::5.1.1.2: con un reintento de E3; entra el crudo del reintento (archivo compañero);
  - cla::3.5.1: cola humana; entra el crudo del primer intento, con la marca.
Después corre runner_corpus.cerrar_e2_r2 con el manifiesto tanda0_10tos_r2b y, sobre su grafo y su registro,
scripts/shapes_validator.py --perfil r2 --fase r2b y scripts/regression_kg.py --perfil r2 --solo LN-3,LN-7; y el
ensamblado r2b completo (ensamblar_tanda0.py con tanda0_ens_desarrollo_r2b) sobre la misma corrida, con el llenado
de umbrales (par A), la establecida_en derivada y las mismas shapes y suite sobre su grafo.
Una segunda corrida quita los índices de la validación guardada de una unidad: queda sin validación, con su error.

Escribe solo en <salida>. Sale con 1 si algún control falla.

Uso (desde la raíz de una copia del repo; CLAUDE.md §4, regla l):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3/cadena_sintetica_p3.py --salida DIR
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

P3 = Path(__file__).resolve().parent
REPO = P3.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
import manifiesto_corpus as MC  # noqa: E402
import comun_e1  # noqa: E402
import perfil_e1  # noqa: E402
import validador_e1  # noqa: E402
import runner_corpus as RC  # noqa: E402

TO = "cla"
OK: list[tuple[str, bool, str]] = []


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    OK.append((nombre, bool(cond), detalle))
    print(f"  {'ok  ' if cond else 'FAIL'} {nombre}" + (f"  [{detalle}]" if not cond and detalle else ""))


def ent(lid, tipo, label, punto, props=None, **kw):
    d = {"local_id": lid, "type": tipo, "label": label, "punto": punto}
    if props is not None:
        d["properties"] = props
    d.update(kw)
    return d


def rel(pred, punto, **kw):
    return {"predicate": pred, "punto": punto, **kw}


ENC = "Abarca todas las financiaciones comprendidas, con excepción de las siguientes"
CRUDOS = {
    "cla::5.1.1.1": {
        "entities": [
            ent("to", "TextoOrdenado", "Clasificación de deudores", "5.1.1.1"),
            ent("r", "Restriccion", "Consumo o vivienda sobre dos veces el importe de referencia", "5.1.1.1",
                {"descripcion": "Los créditos de esta clase que superen el equivalente a dos veces el importe de "
                                "referencia se incluyen en la cartera comercial.", "tipo": "limite_cuantitativo"},
                tramo=f"{ENC} […] Los créditos de esta clase que superen el equivalente a dos veces el importe de "
                      "referencia",
                umbrales=[{"tramo": "superen el equivalente a dos veces el importe de referencia"}]),
            ent("c", "Condicion", "Repago vinculado a la actividad productiva", "5.1.1.1",
                {"descripcion": "Repago no vinculado a ingresos fijos sino a la actividad productiva o comercial."},
                tramo="cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente"),
            ent("op", "Operacion", "Créditos para consumo o vivienda", "5.1.1.1",
                {"tipo": "credito", "descripcion": "Créditos para consumo o vivienda."},
                tramo="Los créditos para consumo o vivienda"),
            ent("x", "Restriction", "Inclusión en la cartera comercial", "5.1.1.1",
                {"descripcion": "Se incluirán dentro de la cartera comercial."},
                tramo="se incluirán dentro de la cartera comercial"),
        ],
        "relations": [
            rel("establecida_en", "5.1.1.1", source="r", target="to"),
            rel("aplica_a", "5.1.1.1", source="r", sujeto_mencion="del cliente", sujeto_id="Sujeto_cliente"),
            rel("condicion_de", "5.1.1.1", source="c", target="op", otras_propiedades={"alcance": "repago"}),
            rel("condicion_de", "5.1.1.1", source="c", target="r"),
            rel("establecida_en", "5.1.1.1", source="x", target="to"),
            rel("limita", "5.1.1.1", source="r", target="op"),
            rel("regula", "5.1.1.1", source="x", target="op"),
        ],
        "omisiones": [{"categoria": "relacion_sin_predicado", "tramo": "importe de referencia establecido en el "
                       "punto 3.7", "nota": "remite_a: la remisión la deriva el código", "source": "r",
                       "destino": "def_3_7"}],
    },
    "cla::3.7": {
        "entities": [
            ent("to", "TextoOrdenado", "Clasificación de deudores", "3.7"),
            ent("d", "Definicion", "Importe de referencia", "3.7",
                {"termino": "Importe de referencia", "descripcion": "Nivel máximo de ventas anuales de la categoría "
                                                                    "Micro del sector Comercio."},
                tramo="El importe a considerar será el nivel máximo del valor de ventas totales anuales para la "
                      "categoría “Micro”"),
            ent("ley", "Comunicacion", "Ley 24.467", "3.7", {"codigo": "Ley 24.467"}, tramo="Ley 24.467"),
        ],
        "relations": [rel("establecida_en", "3.7", source="d", target="to"),
                      rel("referencia", "3.7", source="to", target="ley")],
        "omisiones": [],
    },
    "cla::6.5::intro": {
        "entities": [
            ent("to", "TextoOrdenado", "Clasificación de deudores", "6.5"),
            ent("r", "Restriccion", "Financiaciones de clientes nuevos hasta el importe resultante", "6.5",
                {"descripcion": "Financiaciones que no superen el importe resultante de aplicar sobre el saldo de "
                                "deuda el porcentaje del punto 2.2.5.", "tipo": "limite_cuantitativo"},
                tramo="que no superen el importe resultante de aplicar sobre el saldo de deuda registrado en el "
                      "sistema financiero",
                umbrales=[{"tramo": "no superen el importe resultante de aplicar sobre el saldo de deuda "
                                    "registrado en el sistema financiero"}]),
        ],
        "relations": [rel("establecida_en", "6.5", source="r", target="to"),
                      rel("aplica_a", "6.5", source="r",
                          sujeto_mencion="Los clientes que no registren asistencia crediticia de la entidad")],
        "omisiones": [{"categoria": "fuera_de_tipos", "tramo": "se definen teniendo en cuenta las condiciones",
                       "nota": "Clasificacion (tipo que se habría usado)"}],
    },
}
CRUDO_PRIMERO_5112 = {"entities": [ent("q", "Potestad", "Opción de agrupar", "5.1.1.2", {"descripcion": "d"},
                                       tramo="A opción de la entidad")],
                      "relations": [], "omisiones": []}
CRUDO_REINTENTO_5112 = {
    "entities": [ent("to", "TextoOrdenado", "Clasificación de deudores", "5.1.1.2"),
                 ent("p", "Potestad", "Agrupar financiaciones comerciales con consumo", "5.1.1.2",
                     {"descripcion": "A opción de la entidad, las financiaciones comerciales de hasta dos veces el "
                                     "importe de referencia podrán agruparse con los créditos para consumo."},
                     tramo="A opción de la entidad, las financiaciones de naturaleza comercial")],
    "relations": [rel("establecida_en", "5.1.1.2", source="p", target="to"),
                  rel("aplica_a", "5.1.1.2", source="p", sujeto_mencion="la entidad",
                      sujeto_id="Sujeto_entidad_financiera")],
    "omisiones": []}
CRUDO_COLA_351 = {"entities": [ent("to", "TextoOrdenado", "Clasificación de deudores", "3.5.1"),
                               ent("o", "Obligacion", "Asignar a un área independiente", "3.5.1",
                                   {"descripcion": "Asignar la tarea a un área independiente.", "tipo": "otra"},
                                   tramo="A un área independiente del sector encargado del otorgamiento")],
                  "relations": [rel("establecida_en", "3.5.1", source="o", target="to")], "omisiones": []}
NO_PASADA_A_E3 = ("cla::5.1.1.1", 6)     # relations[6]: la que la validación guardada no pasa a E3


def jl(p: Path, filas: list[dict]) -> None:
    p.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")


def armar_corrida(tdir: Path, chunks: dict, esq, sin_indices: str | None = None) -> None:
    tdir.mkdir(parents=True, exist_ok=True)

    def val(ti, cid):
        return validador_e1.validar_salida(copy.deepcopy(ti), chunks[cid], esquema=esq).as_dict()
    compact, finales, reintentos = [], [], []
    for cid, ti in CRUDOS.items():
        v = val(ti, cid)
        if cid == NO_PASADA_A_E3[0]:
            v["relaciones"] = [r for r in v["relaciones"] if r["indice_crudo"] != NO_PASADA_A_E3[1]]
        if cid == sin_indices:
            for x in v["entidades"] + v["relaciones"]:
                x.pop("indice_crudo")
        compact.append({"chunk_id": cid, "error": None, "tool_input_crudo": ti, "validacion": v})
        finales.append({"chunk_id": cid, "tipo_unidad": chunks[cid]["tipo"], "estado": "completo_ok_directo",
                        "n_reintentos": 0, "residuales": [], "validacion_final": v})
    compact.append({"chunk_id": "cla::5.1.1.2", "error": None, "tool_input_crudo": CRUDO_PRIMERO_5112,
                    "validacion": val(CRUDO_PRIMERO_5112, "cla::5.1.1.2")})
    reintentos.append({"chunk_id": "cla::5.1.1.2", "intento": 1, "tool_input": CRUDO_REINTENTO_5112, "error": None})
    finales.append({"chunk_id": "cla::5.1.1.2", "tipo_unidad": "punto_terminal", "estado": "completo_ok_reintento",
                    "n_reintentos": 1, "residuales": [], "validacion_final": val(CRUDO_REINTENTO_5112, "cla::5.1.1.2")})
    compact.append({"chunk_id": "cla::3.5.1", "error": None, "tool_input_crudo": CRUDO_COLA_351,
                    "validacion": val(CRUDO_COLA_351, "cla::3.5.1")})
    finales.append({"chunk_id": "cla::3.5.1", "tipo_unidad": "punto_terminal", "estado": "cola_humana",
                    "n_reintentos": 1, "residuales": [], "validacion_final": None})
    reintentos.append({"chunk_id": "cla::3.5.1", "intento": 1, "tool_input": CRUDO_COLA_351, "error": None})
    jl(tdir / "extracciones_e1_compact.jsonl", compact)
    jl(tdir / "finales.jsonl", finales)
    jl(tdir / "reintentos_e3.jsonl", reintentos)


def correr(args: list[str]) -> subprocess.CompletedProcess:
    return subprocess.run([sys.executable, "-B", *args], cwd=REPO, capture_output=True, text=True,
                          env={"PYTHONDONTWRITEBYTECODE": "1", "PATH": "/usr/bin:/bin"})


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--salida", type=Path, required=True)
    sal = ap.parse_args().salida.resolve()
    if REPO in sal.parents or sal == REPO:
        raise SystemExit("--salida no puede estar dentro del repo: el script corre sobre una copia y escribe afuera")
    man = MC.cargar(MC.MANIFIESTOS_DIR / "tanda0_10tos_r2b.json")
    RC.configurar(man)
    esq = perfil_e1.perfil("r2b").esquema
    chunks = {c["id"]: c for c in comun_e1.cargar_chunks((TO,), e0_dir=man.e0_salida)}
    corrida = sal / "corrida"
    armar_corrida(corrida / TO, chunks, esq)
    rep = RC.cerrar_e2_r2(TO, corrida)
    tdir = corrida / TO
    regs = {r["chunk_id"]: r for r in map(json.loads, (tdir / f"extracciones_finales_r2_{TO}.jsonl")
                                          .read_text(encoding="utf-8").splitlines())}
    grafo = json.loads((tdir / f"grafo_r2_{TO}.json").read_text(encoding="utf-8"))

    print("[1] entrada_r2 con la forma r2: entra lo que pasó por E3")
    v = regs["cla::5.1.1.1"]["validacion"]
    check("cla::5.1.1.1: la relación que la validación guardada no pasó a E3 no entra y queda en no_vistos_e3",
          [x["elemento"] for x in v["no_vistos_e3"]] == ["relations[6]"] and len(v["relaciones"]) == 6)
    check("el tipo por alias («Restriction») llega corregido de validador_e1 y entra con el original",
          any(e["local_id"] == "x" and e["type"] == "Restriccion" and e["originales"].get("type") == "Restriction"
              for e in v["entidades"]))
    check("todo lo que entra pasó por E3: entidades con paso_por_e3 y relaciones sin no_verificada_e3, incluida "
          "la condicion_de → Operacion",
          all(e.get("paso_por_e3") is True for r in regs.values() if r["validacion"] for e in r["validacion"]["entidades"])
          and all(x.get("no_verificada_e3") is False and x.get("paso_por_e3") is True
                  for r in regs.values() if r["validacion"] for x in r["validacion"]["relaciones"])
          and any(x["predicate"] == "condicion_de" and x["tipo_target"] == "Operacion" for x in v["relaciones"]))
    check("cla::5.1.1.2 entra con el crudo del reintento (archivo compañero) y cla::3.5.1, de la cola humana, con el "
          "del primer intento y la marca",
          regs["cla::5.1.1.2"]["origen_crudo"] == "reintento_1:companero"
          and [e["local_id"] for e in regs["cla::5.1.1.2"]["validacion"]["entidades"]] == ["to", "p"]
          and regs["cla::3.5.1"].get("cola_humana") is True and regs["cla::3.5.1"]["origen_crudo"] == "e1")
    check("reporte de E2 r2: elementos sin verificar 0; la cola humana contada aparte (1 unidad, 2 entidades, 1 "
          "relación); 1 relación excluida; 0 unidades sin índices",
          rep.get("paso_por_e3") == {"entidades_sin_verificar": 0, "relaciones_sin_verificar": 0,
                                     "cola_humana": {"unidades": 1, "por_estado": {"cola_humana": 1},
                                                     "entidades": 2, "relaciones": 1},
                                     "excluidos_entidades": 0, "excluidos_relaciones": 1,
                                     "unidades_sin_indices_e3": 0}, str(rep.get("paso_por_e3")))

    print("[2] campos nuevos en el grafo y en los registros")
    nodos = {n["id"]: n for n in grafo["nodes"]}

    def de_la_cola(o):
        return "cla::3.5.1" in {p.get("chunk_id") for p in o.get("provenances", [])}
    cola_n = [n for n in grafo["nodes"] if de_la_cola(n)]
    cola_e = [x for x in grafo["edges"] if de_la_cola(x)]
    check("cola humana (decisión de la autora, A5): sus nodos y aristas entran con la marca cola_humana, con la "
          "regla nueva (sin no_verificada_e3, contados aparte)",
          len(cola_n) == 2 and len(cola_e) == 1
          and all(o["properties"].get("cola_humana") == "true" and "cla::3.5.1" in o["properties"]["cola_chunks"]
                  and o["properties"].get("estado_e3") == "cola_humana" for o in cola_n + cola_e)
          and all(not x.get("no_verificada_e3") for x in cola_e))
    def nodo(tipo, en_label):
        return next(n for n in grafo["nodes"] if n["type"] == tipo and en_label in n["label"])
    r5 = nodo("Restriccion", "dos veces")
    check("tramo de dos segmentos en la procedencia del nodo, exacta",
          r5["provenance"].get("tramo_verificado") == "exacta" and "[…]" in r5["provenance"].get("tramo", ""))
    check("el TextoOrdenado sin tramo; su archivo lo deriva E2 de la procedencia",
          all("tramo_verificado" not in p for n in grafo["nodes"] if n["type"] == "TextoOrdenado"
              for p in n["provenances"])
          and all(n["properties"].get("archivo") == chunks["cla::3.7"]["archivo"]
                  for n in grafo["nodes"] if n["type"] == "TextoOrdenado"))
    d = nodo("Definicion", "Importe de referencia")
    check("Definicion: término verificado (exacta) en la procedencia", d["provenance"].get("termino_verificado") == "exacta")
    ley = nodo("Comunicacion", "24.467")
    check("Comunicacion: «externa» derivada del código, sin número", ley["properties"].get("tipo") == "externa"
          and "numero" not in ley["properties"])
    r65 = nodo("Restriccion", "importe resultante")
    u = r65["properties"].get("umbrales") or []
    check("límite relativo: elemento sin valor con comparación y base en el nodo",
          len(u) == 1 and "valor" not in u[0] and u[0]["comparacion"] == "maximo_inclusivo"
          and u[0]["base"].startswith("importe resultante"))
    oms = [json.loads(x) for x in (tdir / "omisiones.jsonl").read_text(encoding="utf-8").splitlines()]
    check("omisiones.jsonl: dos omisiones con categoría; relacion_sin_predicado con source y destino",
          len(oms) == 2 and {o["categoria"] for o in oms} == {"relacion_sin_predicado", "fuera_de_tipos"}
          and any(o.get("source") == "r" and o.get("destino") == "def_3_7" for o in oms))
    rel_cond = next(x for x in v["relaciones"] if x["predicate"] == "condicion_de" and x["target"] == "op")
    arista = next((e for e in grafo["edges"] if e["relation"] == "condicion_de" and nodos[e["target"]]["type"]
                   == "Operacion"), {})
    check("otras_propiedades de la relación → properties_no_definidas en la relación validada",
          rel_cond.get("properties_no_definidas") == {"alcance": "repago"})
    # Era un LÍMITE de P3 (E2 no copiaba properties_no_definidas a la arista); lo levanta P3b-2 (c8c3970): en la
    # fase r2b, e2_lib.ensamblar_r2 las pasa de la relación a la arista.
    check("properties_no_definidas de la relación → la arista (fase r2b de e2_lib.ensamblar_r2, P3b-2)",
          arista.get("properties_no_definidas") == {"alcance": "repago"})

    print("[3] shapes (fase r2b) y suite (LN-3, LN-7) sobre el grafo sintético")
    kg = sal / "kg_sintetico_p3.json"
    kg.write_text(json.dumps(grafo, ensure_ascii=False, indent=1), encoding="utf-8")
    s = correr(["scripts/shapes_validator.py", "--kg", str(kg), "--perfil", "r2", "--fase", "r2b",
                "--registro-dir", str(tdir), "--e0", str(man.e0_salida), "--out", str(sal / "shapes_r2b.md")])
    sh = json.loads((sal / "shapes_r2b.json").read_text(encoding="utf-8")) if (sal / "shapes_r2b.json").exists() else {}
    s27 = (sh.get("shapes") or {}).get("S27")
    check("S27 en fase r2b: bloqueante y PASS (mención, verificación y método en cada arista de sujeto)",
          s27 is not None and s27.get("result") == "PASS" and s27.get("severidad") == "bloqueante"
          and s27["conteos"]["aristas_de_sujeto"] == 3, (s.stderr or "")[-300:] + str(s27)[:300])
    t = correr(["scripts/regression_kg.py", "--kg", str(kg), "--generacion", "3", "--catalogo",
                "data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json", "--politica-cuarentena",
                "flaggeada", "--perfil", "r2", "--registro-dir", str(tdir), "--solo", "LN-3,LN-7",
                "--sin-censos", "--out", str(sal / "suite_ln3_ln7.md")])
    su = json.loads((sal / "suite_ln3_ln7.json").read_text(encoding="utf-8")) if (sal / "suite_ln3_ln7.json").exists() else {}
    items = {x.get("id"): x for x in su.get("items", su.get("resultados", []))}
    check("LN-3: toda arista de sujeto con mención y verificación → resuelto",
          items.get("LN-3", {}).get("estado") == "resuelto", (t.stderr or "")[-300:] + str(items.get("LN-3"))[:300])
    check("LN-7: toda omisión con categoría del enum y tramo verificado o marcado → resuelto",
          items.get("LN-7", {}).get("estado") == "resuelto", str(items.get("LN-7"))[:300])

    print("[3b] ensamblado r2b completo (tanda0_ens_desarrollo_r2b) sobre la corrida sintética")
    ens = sal / "ensamblado"
    e = correr(["data/experiment/tanda0/code/ensamblar_tanda0.py", "--manifiesto",
                "data/experiment/reextraccion_v2/manifiestos/tanda0_ens_desarrollo_r2b.json",
                "--entrada", str(corrida), "--salida", str(ens)])
    kg_e = json.loads((ens / "r2" / "kg.json").read_text(encoding="utf-8")) if (ens / "r2" / "kg.json").exists() else {}
    rep_e = json.loads((ens / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8")) \
        if (ens / "r2" / "reporte_ensamblado_r2.json").exists() else {}
    vm = rep_e.get("validacion_modelos_r2", {})
    check("el ensamblado corre (doble corrida byte a byte) y todo nodo y arista cumple NodoR2 y AristaR2",
          e.returncode == 0 and rep_e.get("doble_corrida_byte_identica") is True
          and vm.get("nodos_fuera_del_modelo") == 0 and vm.get("aristas_fuera_del_modelo") == 0,
          (e.stderr or "")[-300:])
    restr = {n["provenance"].get("chunk_id"): n for n in kg_e.get("nodes", []) if n["type"] == "Restriccion"
             and n["properties"].get("umbrales")}
    u5 = (restr.get("cla::5.1.1.1") or {}).get("properties", {}).get("umbrales", [{}])
    check("par A: el elemento con cuantía sale del tramo de E1 (origen e1), verificado y con la base resuelta",
          len(u5) == 1 and u5[0].get("origen") == "e1" and u5[0].get("valor") == "2"
          and u5[0].get("tramo_verificado") == "exacta" and u5[0].get("base_via") == "definicion")
    u6 = (restr.get("cla::6.5::intro") or {}).get("properties", {}).get("umbrales", [{}])
    check("el elemento sin valor del límite relativo llega al nodo del ensamblado",
          len(u6) == 1 and "valor" not in u6[0] and u6[0].get("regla_comparacion", "").startswith("limite_relativo"))
    def de_la_cola_e(o):
        return "cla::3.5.1" in {p.get("chunk_id") for p in o.get("provenances", [])}
    check("cola humana en el ensamblado: todo nodo y arista con procedencia de la unidad lleva la marca",
          all(o.get("properties", {}).get("cola_humana") == "true"
              for o in kg_e.get("nodes", []) + kg_e.get("edges", []) if de_la_cola_e(o))
          and sum(1 for o in kg_e.get("nodes", []) if de_la_cola_e(o)) == 2)
    der = [x for x in kg_e.get("edges", []) if x.get("rol_fuente") == "derivada_de_procedencia"]
    check("establecida_en derivada de la procedencia: sin marcas de E1 (la valida AristaR2)",
          der and all(x["relation"] == "establecida_en" and not x.get("no_verificada_e3") for x in der))
    check("reporte del ensamblado: 0 relaciones y 0 aristas con no_verificada_e3",
          rep_e.get("aristas_no_verificadas_e3", {}).get("total") == 0
          and all(v.get("relaciones_no_verificadas_e3") == 0 for v in rep_e.get("e2_por_to", {}).values()))
    s2 = correr(["scripts/shapes_validator.py", "--kg", str(ens / "r2" / "kg.json"), "--perfil", "r2", "--fase",
                 "r2b", "--registro-dir", str(ens / "r2"), "--e0", str(man.e0_salida),
                 "--out", str(sal / "shapes_r2b_ensamblado.md")])
    sh2 = json.loads((sal / "shapes_r2b_ensamblado.json").read_text(encoding="utf-8")) \
        if (sal / "shapes_r2b_ensamblado.json").exists() else {}
    check("shapes sobre el grafo ensamblado, fase r2b: S27 y S18 en PASS",
          (sh2.get("shapes") or {}).get("S27", {}).get("result") == "PASS"
          and (sh2.get("shapes") or {}).get("S18", {}).get("result") == "PASS", (s2.stderr or "")[-300:])
    t2 = correr(["scripts/regression_kg.py", "--kg", str(ens / "r2" / "kg.json"), "--generacion", "3", "--catalogo",
                 "data/experiment/catalogo_unico/generados_r2/catalogo_suite_r2.json", "--politica-cuarentena",
                 "flaggeada", "--perfil", "r2", "--registro-dir", str(ens / "r2"), "--solo", "LN-3,LN-7",
                 "--sin-censos", "--out", str(sal / "suite_ln3_ln7_ensamblado.md")])
    su2 = json.loads((sal / "suite_ln3_ln7_ensamblado.json").read_text(encoding="utf-8")) \
        if (sal / "suite_ln3_ln7_ensamblado.json").exists() else {}
    items2 = {x.get("id"): x for x in su2.get("items", [])}
    check("LN-3 sobre el grafo ensamblado → resuelto", items2.get("LN-3", {}).get("estado") == "resuelto",
          (t2.stderr or "")[-300:])
    check("LÍMITE (el ensamblado no escribe omisiones.jsonl: ensamblar_tanda0.py, fuera de las escrituras): LN-7 "
          "sobre el grafo ensamblado → no_aplicable", items2.get("LN-7", {}).get("estado") == "no_aplicable")

    print("[4] guarda: una validación guardada sin índices")
    corrida2 = sal / "corrida_sin_indices"
    armar_corrida(corrida2 / TO, chunks, esq, sin_indices="cla::3.7")
    rep2 = RC.cerrar_e2_r2(TO, corrida2)
    regs2 = {r["chunk_id"]: r for r in map(json.loads, (corrida2 / TO / f"extracciones_finales_r2_{TO}.jsonl")
                                           .read_text(encoding="utf-8").splitlines())}
    check("la unidad queda sin validación, con el error validacion_e3_sin_indices_r2, y se cuenta",
          regs2["cla::3.7"]["validacion"] is None and regs2["cla::3.7"]["error"] == "validacion_e3_sin_indices_r2"
          and rep2["paso_por_e3"]["unidades_sin_indices_e3"] == 1)

    resumen = {"comando": "data/experiment/prompt_r2/p3/cadena_sintetica_p3.py --salida DIR",
               "manifiesto": "tanda0_10tos_r2b.json", "perfil": RC.PERFIL.nombre,
               "reporte_e2_r2": {k: rep[k] for k in ("nodes_total", "edges_total", "paso_por_e3", "sha256_grafo")},
               "shapes_r2b_S27": s27,
               "shapes_r2b_veredicto": {"veredicto": sh.get("veredicto"), "bloqueantes_en_fail": sh.get(
                   "bloqueantes_en_fail"), "nota": "grafo de E2 r2 de un TO: sin el llenado de umbrales (par A) ni "
                   "el esqueleto del ensamblado, que no corren en cerrar_e2_r2"},
               "suite": {k: items.get(k) for k in ("LN-3", "LN-7")},
               "ensamblado": {"kg_sha256": rep_e.get("sha256_kg"), "nodos": rep_e.get("nodes_total"),
                              "aristas": rep_e.get("edges_total"),
                              "validacion_modelos_r2": vm, "umbrales": rep_e.get("umbrales"),
                              "shapes_r2b": {k: (sh2.get("shapes") or {}).get(k, {}).get("result")
                                             for k in sorted(sh2.get("shapes") or {})},
                              "shapes_veredicto": sh2.get("veredicto"),
                              "suite": {k: items2.get(k) for k in ("LN-3", "LN-7")}},
               "controles": [{"nombre": n, "ok": b} for n, b, _ in OK]}
    texto = json.dumps(resumen, ensure_ascii=False, indent=1).replace(str(sal), "<SALIDA>")
    (sal / "resumen_cadena_sintetica_p3.json").write_text(texto + "\n", encoding="utf-8")
    n_ok = sum(b for _, b, _ in OK)
    print(f"\nRESULTADO: {n_ok}/{len(OK)}  (grafo sha256 {hashlib.sha256(kg.read_bytes()).hexdigest()[:12]}…)")
    return 0 if n_ok == len(OK) else 1


if __name__ == "__main__":
    raise SystemExit(main())
