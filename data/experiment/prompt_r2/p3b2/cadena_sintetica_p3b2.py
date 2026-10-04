"""
cadena_sintetica_p3b2.py — U-PROMPT-R2, P3b-2 (USD 0, sin API): la cadena del perfil r2b con lo que agrega P3b, de
punta a punta, con stubs en lugar de los modelos:

  ratchet de E3 (ratchet_e3.ciclo_ratchet con StubClienteE3 y StubClienteE1, perfil r2b) → finales.jsonl y
  reintentos_e3.jsonl como los escribe runner_corpus → entrada_r2 (vistos_por_e3 lleva la marca de la copia de la
  nota) → validador_r2 → E2 r2 con la fase r2b (cerrar_e2_r2) → ensamblado r2b completo (tanda0_ens_desarrollo_r2b).

Unidades de cla sobre la e0-r2 (manifiesto tanda0_10tos_r2b):
  - cla::5.1.1.2: el veredicto de E3 llega como texto (j) y el reintento copia la nota en una descripción (defensa
    2); entra el reintento, con la marca de lectura en la validación final y la de la copia en el nodo. Tiene una
    Operacion en su punto y otra anclada en 5.1.1;
  - cla::3.5.1: el reintento tiene menos entidades (k4): entra con la marca; se cuenta desde finales.jsonl;
  - cla::6.5::intro: faltantes que siguen tras el reintento: cola humana, con el `todo` de la forma r2;
  - cla::5.1.1.1: la modalidad y la consecuencia copiadas, una relación con otras_propiedades, una Operacion con la
    misma etiqueta que la de 5.1.1.2 en su punto y otra anclada en 5.1.1, como la de 5.1.1.2;
  - cla::3.7: Comunicacion desde el tramo verificado (l): la ley, una ley con código de Comunicación y un tramo que
    no verifica;
  - cla::2.2.4::intro: mini-chunk a mitad de oración (h): un tramo que cruza del título al cuerpo.
Escribe solo en <salida>. Sale con 1 si algún control falla.

Uso (desde la raíz de una copia del repo; CLAUDE.md §4, regla l):
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p3b2/cadena_sintetica_p3b2.py --salida DIR
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
import manifiesto_corpus as MC  # noqa: E402
import comun_e1  # noqa: E402
import perfil_e1  # noqa: E402
import validador_e1  # noqa: E402
import cliente_e1  # noqa: E402
import cliente_e3  # noqa: E402
import ratchet_e3  # noqa: E402
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


def to_(punto):
    return ent("to", "TextoOrdenado", "Clasificación de deudores", punto)


OP_PUNTO = "Créditos para consumo o vivienda"
OP_511 = "Financiaciones comprendidas en la cartera comercial"
NOTA = "falta la potestad de agrupar las financiaciones comerciales con los créditos de consumo"
COMPLETO = {"veredicto": "completo_ok", "faltantes": []}


def faltante(cita: str, nota: str = "falta un elemento") -> dict:
    return {"tipo": "otro", "severidad": "alta", "ubicacion": "unidad", "cita_textual_del_fuente": cita, "nota": nota}


CITA_5112 = "las financiaciones de naturaleza comercial de hasta el equivalente a dos veces el importe de referencia"
CITA_351 = "A un área independiente del sector encargado del otorgamiento de créditos y garantías"
CITA_65 = "Cada cliente, y la totalidad de sus financiaciones comprendidas, se incluirá en una de las"

UNIDADES = {
    # cid: (crudo del primer intento, veredictos de E3, crudos de los reintentos)
    "cla::5.1.1.1": ({
        "entities": [to_("5.1.1.1"),
                     ent("o", "Obligacion", "Incluir en la cartera comercial", "5.1.1.1",
                         {"descripcion": "Es una recomendación y no un deber: incluir los créditos en la cartera "
                                         "comercial.", "tipo": "otra"},
                         tramo="se incluirán dentro de la cartera comercial",
                         otras_propiedades={"modalidad": "se recomienda"}),
                     ent("s", "Obligacion", "Sancionar el incumplimiento", "5.1.1.1",
                         {"descripcion": "El incumplimiento dará lugar a sanciones.", "tipo": "otra"},
                         tramo="se incluirán dentro de la cartera comercial",
                         otras_propiedades={"consecuencia": "dará lugar a la aplicación de sanciones"}),
                     ent("c", "Condicion", "Repago vinculado a la actividad productiva", "5.1.1.1",
                         {"descripcion": "Repago no vinculado a ingresos fijos."},
                         tramo="cuyo repago no se encuentre vinculado a ingresos fijos o periódicos del cliente"),
                     ent("op", "Operacion", OP_PUNTO, "5.1.1.1", tramo="Los créditos para consumo o vivienda"),
                     ent("op2", "Operacion", OP_511, "5.1.1", tramo="cartera comercial")],
        "relations": [rel("establecida_en", "5.1.1.1", source="o", target="to"),
                      rel("condicion_de", "5.1.1.1", source="c", target="op",
                          otras_propiedades={"alcance": "repago"})],
        "omisiones": []}, [COMPLETO], []),
    "cla::5.1.1.2": ({
        "entities": [to_("5.1.1.2"),
                     ent("q", "Potestad", "Opción de agrupar", "5.1.1.2", {"descripcion": "d"},
                         tramo="A opción de la entidad"),
                     ent("op", "Operacion", OP_PUNTO, "5.1.1.2", tramo="créditos para consumo"),
                     ent("op2", "Operacion", OP_511, "5.1.1", tramo="naturaleza comercial")],
        "relations": [rel("establecida_en", "5.1.1.2", source="q", target="to")], "omisiones": []},
        [{"veredicto": "faltantes_detectados", "faltantes": json.dumps([faltante(CITA_5112, NOTA)],
                                                                         ensure_ascii=False)}, COMPLETO],
        [{"entities": [to_("5.1.1.2"),
                       ent("p", "Potestad", "Agrupar financiaciones comerciales con consumo", "5.1.1.2",
                           {"descripcion": "Es facultad de la entidad: falta la potestad de agrupar las "
                                           "financiaciones comerciales con los créditos de consumo."},
                           tramo="A opción de la entidad, las financiaciones de naturaleza comercial"),
                       ent("op", "Operacion", OP_PUNTO, "5.1.1.2", tramo="créditos para consumo"),
                       ent("op2", "Operacion", OP_511, "5.1.1", tramo="naturaleza comercial")],
          "relations": [rel("establecida_en", "5.1.1.2", source="p", target="to")], "omisiones": []}]),
    "cla::3.5.1": ({
        "entities": [to_("3.5.1"),
                     ent("o", "Obligacion", "Asignar a un área independiente", "3.5.1",
                         {"descripcion": "Asignar la tarea a un área independiente.", "tipo": "otra"},
                         tramo="A un área independiente del sector encargado del otorgamiento"),
                     ent("o2", "Obligacion", "Separar del otorgamiento", "3.5.1",
                         {"descripcion": "Separar la tarea del sector de otorgamiento.", "tipo": "otra"},
                         tramo="del sector encargado del otorgamiento de créditos y garantías")],
        "relations": [rel("establecida_en", "3.5.1", source="o", target="to")], "omisiones": []},
        [{"veredicto": "faltantes_detectados", "faltantes": [faltante(CITA_351)]}, COMPLETO],
        [{"entities": [to_("3.5.1"),
                       ent("o", "Obligacion", "Asignar a un área independiente", "3.5.1",
                           {"descripcion": "Asignar la tarea a un área independiente.", "tipo": "otra"},
                           tramo="A un área independiente del sector encargado del otorgamiento")],
          "relations": [rel("establecida_en", "3.5.1", source="o", target="to")], "omisiones": []}]),
    "cla::6.5::intro": ({
        "entities": [to_("6.5"),
                     ent("o", "Obligacion", "Incluir a cada cliente en una categoría", "6.5",
                         {"descripcion": "Incluir a cada cliente en una de cinco categorías.", "tipo": "otra"},
                         tramo="se incluirá en una de las")],
        "relations": [rel("establecida_en", "6.5", source="o", target="to")], "omisiones": []},
        [{"veredicto": "faltantes_detectados", "faltantes": [faltante(CITA_65)]},
         {"veredicto": "faltantes_detectados", "faltantes": [faltante(CITA_65)]}],
        [{"entities": [to_("6.5"),
                       ent("o", "Obligacion", "Incluir a cada cliente en una categoría", "6.5",
                           {"descripcion": "Incluir a cada cliente en una de cinco categorías.", "tipo": "otra"},
                           tramo="se incluirá en una de las")],
          "relations": [rel("establecida_en", "6.5", source="o", target="to")], "omisiones": []}]),
    "cla::3.7": ({
        "entities": [to_("3.7"),
                     ent("ley", "Comunicacion", "Ley 24.467", "3.7", {"codigo": "Ley 24.467"}, tramo="Ley 24.467"),
                     ent("a39", "Comunicacion", "Com. A 39", "3.7", {"codigo": "A-39"}, tramo="Ley 24.467"),
                     ent("nv", "Comunicacion", "Com. A 7825", "3.7", {"codigo": "A 7825"},
                         tramo="Comunicación A 7825")],
        "relations": [rel("referencia", "3.7", source="to", target="ley")], "omisiones": []}, [COMPLETO], []),
    "cla::2.2.4::intro": ({
        "entities": [to_("2.2.4"),
                     ent("o", "Obligacion", "Financiaciones de sucursales", "2.2.4",
                         {"descripcion": "Financiaciones otorgadas por sucursales y subsidiarias.", "tipo": "otra"},
                         tramo="otorgados por sucursales y subsidiarias locales de entidades")],
        "relations": [rel("establecida_en", "2.2.4", source="o", target="to")], "omisiones": []}, [COMPLETO], []),
}


def jl(p: Path, filas: list[dict]) -> None:
    p.write_text("".join(json.dumps(f, ensure_ascii=False) + "\n" for f in filas), encoding="utf-8")


def correr_e3(tdir: Path, chunks: dict, perfil) -> dict:
    """Fase E3 de la corrida con stubs: lo que escribe runner_corpus por unidad (finales y el crudo de cada
    reintento) y la extracción de E1 (compact)."""
    tdir.mkdir(parents=True, exist_ok=True)
    registro = ratchet_e3.RegistroE3(tdir)
    unidades = {c["unidad"] for c in chunks.values()}
    compact, finales, reintentos, exps = [], [], [], {}
    for cid, (crudo, veredictos, reint) in UNIDADES.items():
        c = chunks[cid]
        val = validador_e1.validar_salida(copy.deepcopy(crudo), c, esquema=perfil.esquema).as_dict()
        compact.append({"chunk_id": cid, "error": None, "tool_input_crudo": crudo, "validacion": val})
        exp = ratchet_e3.ciclo_ratchet(
            c, val, cliente_verificador=cliente_e3.StubClienteE3(copy.deepcopy(veredictos)),
            cliente_extractor=cliente_e1.StubClienteE1(copy.deepcopy(reint)), model_e3="M3", model_e1="M1",
            registro=registro, unidades_corpus=unidades, perfil=perfil)
        exps[cid] = exp
        for reex in exp["reintentos"]:
            reintentos.append({"chunk_id": cid, "intento": reex["intento"], "tool_input": reex["tool_input"],
                               "error": reex["error"]})
        finales.append({"chunk_id": cid, "tipo_unidad": c["tipo"], "estado": exp["estado"],
                        "n_reintentos": len(exp["reintentos"]), "residuales": exp["residuales"],
                        "validacion_final": exp["validacion_final"]})
    jl(tdir / "extracciones_e1_compact.jsonl", compact)
    jl(tdir / "finales.jsonl", finales)
    jl(tdir / RC.REINTENTOS_E3, reintentos)
    return exps


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
    perfil = perfil_e1.perfil("r2b")
    chunks = {c["id"]: c for c in comun_e1.cargar_chunks((TO,), e0_dir=man.e0_salida)}
    corrida = sal / "corrida"
    tdir = corrida / TO

    print("[1] ratchet de E3 con stubs (forma r2)")
    exps = correr_e3(tdir, chunks, perfil)
    e5, e3_, e6 = exps["cla::5.1.1.2"], exps["cla::3.5.1"], exps["cla::6.5::intro"]
    m5 = e5.get("marcas_e3") or {}
    check("j: el veredicto como texto se lee («json») y la unidad sale por el reintento, con la marca de lectura",
          e5["estado"] == "aceptado_tras_reintento"
          and m5.get("lectura_veredicto_e3") == [{"fase": "verificacion", "intento": 0, "lectura": "json"}])
    copias = m5.get("copia_nota_e3") or []
    check("defensa 2: la descripción que copia la nota queda marcada, con su índice del crudo",
          len(copias) == 1 and copias[0]["type"] == "Potestad" and copias[0]["indice_crudo"] == 1
          and "descripcion" in copias[0]["campos"])
    check("defensa 1: el pedido del reintento lleva el aviso de la nota",
          ratchet_e3.AVISO_NOTA_REINTENTO in ratchet_e3.build_reextraccion_kwargs(
              chunks["cla::5.1.1.2"], [faltante(CITA_5112, NOTA)], model="M1", perfil=perfil)["messages"][0]["content"])
    check("k4: el reintento con menos entidades entra con la marca y los conteos",
          e3_["estado"] == "aceptado_tras_reintento" and e3_.get("marcas_e3") == {
              "reintento_con_menos_elementos": {"entidades": [3, 2], "relaciones": [1, 1]}})
    cola = [json.loads(x) for x in (tdir / "cola_humana.jsonl").read_text(encoding="utf-8").splitlines()]
    check("cola humana: la unidad que no terminó, con el todo de la forma r2",
          e6["estado"] == "cola_humana" and len(cola) == 1 and cola[0]["chunk_id"] == "cla::6.5::intro"
          and "entra al grafo con la marca cola_humana" in cola[0]["todo"])
    fin = [json.loads(x) for x in (tdir / "finales.jsonl").read_text(encoding="utf-8").splitlines()]
    k4 = sum(1 for f in fin if "reintento_con_menos_elementos" in ((f.get("validacion_final") or {})
                                                                   .get("marcas_e3") or {}))
    check("k4 se cuenta por tanda desde finales.jsonl: 1 unidad", k4 == 1)
    check("copias_nota_e3.jsonl: una línea, la de cla::5.1.1.2",
          [json.loads(x)["chunk_id"] for x in (tdir / "copias_nota_e3.jsonl").read_text(encoding="utf-8")
           .splitlines()] == ["cla::5.1.1.2"])

    print("[2] E2 r2 con la fase r2b (cerrar_e2_r2)")
    rep = RC.cerrar_e2_r2(TO, corrida)
    regs = {r["chunk_id"]: r for r in map(json.loads, (tdir / f"extracciones_finales_r2_{TO}.jsonl")
                                          .read_text(encoding="utf-8").splitlines())}
    grafo = json.loads((tdir / f"grafo_r2_{TO}.json").read_text(encoding="utf-8"))
    nodos = grafo["nodes"]

    def nd(n):
        return n.get("properties_no_definidas") or {}
    # Desde C2 de U-R2-CODIGO-2 (punto t), vistos_por_e3 lleva las tres marcas de E3, no solo la de la copia.
    check("vistos_por_e3 lleva las tres marcas de E3 a la validación r2 (copia de la nota, lectura del veredicto y "
          "reintento con menos elementos)",
          regs["cla::5.1.1.2"]["validacion"].get("marcas_e3") == {
              "copia_nota_e3": copias,
              "lectura_veredicto_e3": [{"fase": "verificacion", "intento": 0, "lectura": "json"}]}
          and regs["cla::3.5.1"]["validacion"].get("marcas_e3") == {
              "reintento_con_menos_elementos": {"entidades": [3, 2], "relaciones": [1, 1]}})
    pot = [n for n in nodos if n["type"] == "Potestad" and "copia_nota_e3" in nd(n)]
    check("la marca de la copia llega al nodo, en properties_no_definidas",
          len(pot) == 1 and pot[0]["label"].startswith("Agrupar") and nd(pot[0])["copia_nota_e3"] == copias[0]["campos"])
    mc = sorted((nd(n).get("modalidad_clasificada"), n["label"]) for n in nodos if "modalidad_clasificada" in nd(n))
    check("modalidad y consecuencia clasificadas, junto al tramo copiado",
          mc == [("consecuencia_de_incumplimiento", "Sancionar el incumplimiento"),
                 ("recomendacion", "Incluir en la cartera comercial")], str(mc))
    arista = [e for e in grafo["edges"] if e["relation"] == "condicion_de"]
    check("las properties_no_definidas de la relación llegan a la arista",
          len(arista) == 1 and arista[0].get("properties_no_definidas") == {"alcance": "repago"})
    ops = sorted((n["label"], sorted({p["punto"] for p in n["provenances"]}),
                  sorted({p["chunk_id"] for p in n["provenances"]})) for n in nodos if n["type"] == "Operacion")
    check("Operacion: la misma etiqueta en dos puntos queda en dos nodos; la de 5.1.1 de dos unidades, en uno",
          ops == [(OP_PUNTO, ["5.1.1.1"], ["cla::5.1.1.1"]), (OP_PUNTO, ["5.1.1.2"], ["cla::5.1.1.2"]),
                  (OP_511, ["5.1.1"], ["cla::5.1.1.1", "cla::5.1.1.2"])], str(ops))
    com = {n["label"]: n["properties"] for n in nodos if n["type"] == "Comunicacion"}
    check("l: la ley y la ley con código de Comunicación dan «externa» desde el tramo; sin tramo verificado, no se "
          "deriva", com.get("Ley 24.467", {}).get("tipo") == "externa" and com.get("Com. A 39", {}).get("tipo")
          == "externa" and "numero" not in com.get("Com. A 39", {}) and "tipo" not in com.get("Com. A 7825", {}),
          str(com))
    v224 = regs["cla::2.2.4::intro"]["validacion"]
    o224 = next(e for e in v224["entidades"] if e["local_id"] == "o")
    check("h: el tramo que cruza del título al cuerpo verifica en orden de lectura",
          o224["provenance"].get("tramo_verificado") == "exacta"
          and v224["contadores"]["tramo_entidad"].get("orden_de_lectura:exacta") == 1)
    p3b = (rep.get("stats") or {}).get("p3b")
    check("reporte de E2 r2: stats p3b cuenta aparte las claves nuevas y las marcas que llegaron",
          p3b == {"nodos_con_clave": {"modalidad": 1, "consecuencia": 1, "modalidad_clasificada": 2,
                                      "copia_nota_e3": 1},
                  "modalidad_clasificada": {"consecuencia_de_incumplimiento": 1, "recomendacion": 1},
                  "aristas_con_properties_no_definidas": 1,
                  "unidades_con_marca_e3": {"copia_nota_e3": 1, "lectura_veredicto_e3": 1,
                                            "reintento_con_menos_elementos": 1}}, str(p3b))
    check("reporte de E2 r2: 0 elementos sin verificar; la cola humana aparte",
          rep["paso_por_e3"]["entidades_sin_verificar"] == 0 and rep["paso_por_e3"]["relaciones_sin_verificar"] == 0
          and rep["paso_por_e3"]["cola_humana"]["unidades"] == 1)

    print("[3] ensamblado r2b completo (tanda0_ens_desarrollo_r2b) sobre la corrida sintética")
    ens = sal / "ensamblado"
    e = correr(["data/experiment/tanda0/code/ensamblar_tanda0.py", "--manifiesto",
                "data/experiment/reextraccion_v2/manifiestos/tanda0_ens_desarrollo_r2b.json",
                "--entrada", str(corrida), "--salida", str(ens)])
    kg = json.loads((ens / "r2" / "kg.json").read_text(encoding="utf-8")) if (ens / "r2" / "kg.json").exists() else {}
    rep_e = json.loads((ens / "r2" / "reporte_ensamblado_r2.json").read_text(encoding="utf-8")) \
        if (ens / "r2" / "reporte_ensamblado_r2.json").exists() else {}
    vm = rep_e.get("validacion_modelos_r2", {})
    check("el ensamblado corre (doble corrida byte a byte) y todo nodo y arista cumple NodoR2 y AristaR2",
          e.returncode == 0 and rep_e.get("doble_corrida_byte_identica") is True
          and vm.get("nodos_fuera_del_modelo") == 0 and vm.get("aristas_fuera_del_modelo") == 0,
          (e.stderr or "")[-400:])
    kn = kg.get("nodes", [])
    check("en el kg: la marca de la copia, la modalidad clasificada y la arista con properties_no_definidas",
          sum(1 for n in kn if "copia_nota_e3" in nd(n)) == 1
          and sum(1 for n in kn if "modalidad_clasificada" in nd(n)) == 2
          and sum(1 for x in kg.get("edges", []) if x.get("properties_no_definidas")) == 1)
    check("en el kg: tres nodos Operacion (dos por punto y uno de 5.1.1)",
          sum(1 for n in kn if n["type"] == "Operacion") == 3)
    check("reporte del ensamblado: stats p3b por TO",
          ((rep_e.get("e2_por_to") or {}).get(TO, {}).get("stats") or {}).get("p3b") == p3b)

    resumen = {"comando": "data/experiment/prompt_r2/p3b2/cadena_sintetica_p3b2.py --salida DIR",
               "manifiesto": "tanda0_10tos_r2b.json", "perfil": RC.PERFIL.nombre, "prefijo_hash": RC.PERFIL.prefijo_hash,
               "estados_e3": {cid: x["estado"] for cid, x in exps.items()},
               "marcas_e3": {cid: x.get("marcas_e3") for cid, x in exps.items() if x.get("marcas_e3")},
               "reporte_e2_r2": {k: rep.get(k) for k in ("nodes_total", "edges_total", "paso_por_e3", "sha256_grafo")},
               "stats_p3b": p3b,
               "ensamblado": {"kg_sha256": rep_e.get("sha256_kg"), "nodos": rep_e.get("nodes_total"),
                              "aristas": rep_e.get("edges_total"), "validacion_modelos_r2": vm},
               "controles": [{"nombre": n, "ok": b} for n, b, _ in OK]}
    texto = json.dumps(resumen, ensure_ascii=False, indent=1).replace(str(sal), "<SALIDA>")
    (sal / "resumen_cadena_sintetica_p3b2.json").write_text(texto + "\n", encoding="utf-8")
    n_ok = sum(b for _, b, _ in OK)
    print(f"\nRESULTADO: {n_ok}/{len(OK)}  (grafo E2 sha256 "
          f"{hashlib.sha256((tdir / f'grafo_r2_{TO}.json').read_bytes()).hexdigest()[:12]}…)")
    return 0 if n_ok == len(OK) else 1


if __name__ == "__main__":
    raise SystemExit(main())
