"""
selftest_cobertura_esq2.py — FASE (c) de U-ESQ-2: selftest previo al gasto
($0, sin API). Patrón [PASS]/RESULTADO de la saga ESQ.

Guardas verificadas:
  1. Universo: la lista de 10 TOs del código coincide con la SELLADA en el
     pre-registro §1 (parseada del archivo, no transcripta a mano) y el
     conteo de unidades es 762 (recomputado de los chunks).
  2. Tarifas/modelo: transcripción verbatim contra runner_corpus.py:76-78
     (leído como texto, sin importarlo).
  3. Flag apagado byte-idéntico contra los candados: hash del prefijo cerrado
     == candado == hash del namespace de producción presente en la db real
     (read-only); system == PREFIJO_SISTEMA de producción; tool schema ES el
     objeto de producción, sin campos del canal abierto; claves del request.
  4. Cuarentena D5 del rol: ninguno de los 762 archivos resuelve rol en
     ROL_POR_TO y ningún mensaje trae bloque de alcance.
  5. Caché/namespace propios sin colisión: db nueva, distinta de producción y
     de las 4 dbs de la saga ESQ; namespace propio ausente de TODAS las dbs
     existentes (query read-only) y distinto del de producción.
  6. Tope duro cableado: chequear_tope frena; el create() del cliente frena
     por proyección ANTES de tocar caché o red (instancia sin __init__ — no
     se construye ningún cliente de API en el selftest).
  7. Reanudación idempotente del runner (stub, salida propia en selftest_out):
     corrida parcial abortada → re-corrida saltea lo persistido y completa;
     tercera corrida no llama nada.
  8. Claves de persistencia idénticas a las de producción (runner_corpus).
  8bis. Regla CORREGIDA del ranking de la dirigida (fe de erratas del
     pre-registro §4, 930f289) sobre listas sintéticas multi-TO: ningún TO
     acapara la selección mientras otros TOs tienen candidatos pendientes;
     ciclo de TOs por disparador; dedup entre disparadores; exclusión de la
     azarosa; pares agotados salteados sin loop infinito; determinismo.
  9. Sella producción por sha256 (código E1 + jsonl de producción + db + los
     10 chunks E0 de escalado_prep) en cobertura/sellos_produccion_sha256.json
     — el cierre de la fase (d) re-verifica contra este archivo.

Uso:  .venv/bin/python3 -B data/experiment/esq/code/selftest_cobertura_esq2.py
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

CODE_DIR = Path(__file__).resolve().parent
if str(CODE_DIR) not in sys.path:
    sys.path.insert(0, str(CODE_DIR))

import comun_cobertura_esq2 as cc          # noqa: E402
import runner_cobertura_esq2 as runner     # noqa: E402
import comun_e1                            # noqa: E402
import prompt_e1                           # noqa: E402
from schema import ROL_POR_TO              # noqa: E402

FALLAS: list[str] = []
N_CHECKS = 0


def check(nombre: str, cond: bool, detalle: str = "") -> None:
    global N_CHECKS
    N_CHECKS += 1
    if cond:
        print(f"[PASS] {nombre}" + (f" — {detalle}" if detalle else ""))
    else:
        print(f"[FAIL] {nombre}" + (f" — {detalle}" if detalle else ""))
        FALLAS.append(nombre)


def main() -> int:
    # ---- 1. universo sellado ------------------------------------------------
    prer = (cc.UNIDAD_DIR / "prerregistro_esq2.md").read_text(encoding="utf-8")
    m = re.search(r"escalado_prep/`\):\s*(.*?)\s*—\s*762", prer, re.DOTALL)
    tos_sellados = tuple(t.strip() for t in m.group(1).replace("\n", " ")
                         .replace("  ", " ").split(",")) if m else ()
    check("lista de TOs == pre-registro §1 (parseada del archivo)",
          tos_sellados == cc.TOS_ESQ2, f"{tos_sellados}")
    chunks = cc.cargar_chunks_esq2()
    por_to = {}
    for c in chunks:
        por_to[c["to"]] = por_to.get(c["to"], 0) + 1
    check("762 unidades recomputadas de los chunks",
          len(chunks) == cc.N_UNIDADES_ESQ2,
          f"total={len(chunks)} por_to={por_to}")
    ids = [c["id"] for c in chunks]
    check("chunk_ids únicos", len(ids) == len(set(ids)))

    # ---- 2. tarifas verbatim ------------------------------------------------
    rc = (cc.EXP_DIR / "reextraccion_v2" / "corpus_v2" / "runner_corpus.py"
          ).read_text(encoding="utf-8")
    check("modelo verbatim runner_corpus.py:76",
          f'MODEL_E1 = "{cc.MODEL_E1}"' in rc)
    check("tarifas verbatim runner_corpus.py:77-78",
          "precio_in_por_mtok=1.00, precio_out_por_mtok=5.00" in rc
          and "precio_cache_write_por_mtok=1.25, precio_cache_read_por_mtok=0.10" in rc
          and cc.P_E1 == dict(precio_in_por_mtok=1.00, precio_out_por_mtok=5.00,
                              precio_cache_write_por_mtok=1.25,
                              precio_cache_read_por_mtok=0.10))

    # ---- 3. flag apagado byte-idéntico -------------------------------------
    h = prompt_e1.prefijo_hash(False)
    check("candado del prefijo cerrado",
          h == cc.PREFIJO_HASH_CERRADO_ESPERADO, h)
    db_prod = cc.E1_DIR / "cache" / "e1_extraccion.db"
    conn = cc.conectar_db_readonly(db_prod)
    ns_db = [r[0] for r in conn.execute("SELECT DISTINCT namespace FROM cache")]
    conn.close()
    ns_prod = cc.namespace_produccion()
    check("namespace de producción presente en la db real y con el hash cerrado",
          ns_prod in ns_db and f"p{h}" in ns_prod, ns_prod)
    kwargs = prompt_e1.build_request_kwargs(chunks[0], model=cc.MODEL_E1)
    check("system == PREFIJO_SISTEMA de producción (byte-idéntico)",
          kwargs["system"][0]["text"] == prompt_e1.PREFIJO_SISTEMA
          and kwargs["system"][0]["cache_control"] == {"type": "ephemeral"})
    props_e = kwargs["tools"][0]["input_schema"]["properties"]["entities"]["items"]["properties"]
    props_r = kwargs["tools"][0]["input_schema"]["properties"]["relations"]["items"]["properties"]
    check("tool schema ES el objeto de producción, sin canal abierto",
          kwargs["tools"][0] is prompt_e1.TOOL_SCHEMA_E1
          and "tipo_propuesto" not in props_e
          and "predicado_propuesto" not in props_r)
    check("claves del request exactas",
          set(kwargs) == {"model", "max_tokens", "system", "tools",
                          "tool_choice", "messages"}
          and kwargs["tool_choice"] == {"type": "tool",
                                        "name": prompt_e1.NOMBRE_TOOL}
          and kwargs["model"] == cc.MODEL_E1)

    # ---- 4. cuarentena D5 del rol ------------------------------------------
    archivos = sorted({c["archivo"] for c in chunks})
    con_rol = [a for a in archivos if ROL_POR_TO.get(a) is not None]
    mensajes_con_alcance = 0
    for c in chunks:
        if "Alcance de este TO" in prompt_e1.build_user_message(c):
            mensajes_con_alcance += 1
    check("ningún archivo de los 10 TOs resuelve rol en ROL_POR_TO",
          not con_rol, f"archivos={archivos}")
    check("ningún mensaje de las 762 trae bloque de alcance",
          mensajes_con_alcance == 0)

    # ---- 5. caché/namespace propios sin colisión ---------------------------
    ns = cc.namespace_cobertura()
    check("db propia distinta de producción y de la saga ESQ",
          all(cc.DB_COBERTURA.resolve() != p.resolve() for p in cc.DBS_AJENAS),
          str(cc.DB_COBERTURA.relative_to(cc.REPO_DIR)))
    ns_existentes = set()
    for p in cc.DBS_AJENAS:
        if p.exists():
            conn = cc.conectar_db_readonly(p)
            ns_existentes |= {r[0] for r in conn.execute(
                "SELECT DISTINCT namespace FROM cache")}
            conn.close()
    if cc.DB_COBERTURA.exists():
        conn = cc.conectar_db_readonly(cc.DB_COBERTURA)
        propios = {r[0] for r in conn.execute("SELECT DISTINCT namespace FROM cache")}
        conn.close()
        check("db propia (si existe) solo contiene el namespace propio",
              propios <= {ns}, str(propios))
    check("namespace propio ausente de todas las dbs ajenas y != producción",
          ns not in ns_existentes and ns != ns_prod, ns)

    # ---- 6. tope duro cableado ---------------------------------------------
    try:
        cc.chequear_tope(6.49, 0.05, cc.TOPE_USD)
        frena = False   # 6,49 + 0,05 > 6,50 debía frenar
    except cc.TopeExcedido:
        frena = True
    check("chequear_tope frena en el borde (6,49 + 0,05 > 6,50)", frena)
    cli = object.__new__(cc.ClienteCoberturaEsq2)   # sin __init__: sin API
    cli.gasto_usd = cc.TOPE_USD
    cli._proyeccion_usd = 0.05
    cli.tope_usd = cc.TOPE_USD
    cli.cache = None   # si el freno no corta antes de la caché, esto explota
    try:
        cli.create(doc="x", model="m")
        frena2 = False
    except cc.TopeExcedido:
        frena2 = True
    check("create() del cliente frena por proyección antes de tocar caché/red",
          frena2)

    # ---- 7. reanudación idempotente (stub) ---------------------------------
    st_dir = cc.SELFTEST_DIR / "cobertura_reanudacion"
    if st_dir.exists():
        shutil.rmtree(st_dir)
    st_dir.mkdir(parents=True)
    stub1 = runner.StubClienteCobertura()
    try:
        runner.correr(stub1, st_dir, cc.TOPE_USD, stub=True,
                      limite=2, abortar_tras=7)
        abortado = False
    except SystemExit as e:
        abortado = (e.code == 9)
    check("corrida stub abortada a mitad (exit 9 simulado)",
          abortado and stub1.llamadas == 7)
    stub2 = runner.StubClienteCobertura()
    runner.correr(stub2, st_dir, cc.TOPE_USD, stub=True, limite=2)
    total_limite = 2 * len(cc.TOS_ESQ2)
    check("re-corrida completa salteando lo persistido",
          stub2.llamadas == total_limite - 7,
          f"llamadas={stub2.llamadas} de {total_limite - 7} pendientes")
    stub3 = runner.StubClienteCobertura()
    runner.correr(stub3, st_dir, cc.TOPE_USD, stub=True, limite=2)
    check("tercera corrida: 0 llamadas (todo persistido)",
          stub3.llamadas == 0)
    regs = {}
    for to in cc.TOS_ESQ2:
        regs.update(cc.cargar_jsonl_last_wins(
            st_dir / to / f"extracciones_e1_{to}.jsonl"))
    check("persistidas todas las unidades del límite, sin errores",
          len(regs) == total_limite
          and all(r.get("error") is None for r in regs.values()))

    # ---- 8. claves de persistencia == producción ---------------------------
    reg = next(iter(regs.values()))
    claves_prod = ["chunk_id", "unidad", "tipo_unidad", "titulo",
                   "stop_reason", "error", "usage", "tool_input_crudo",
                   "validacion"]
    check("claves del registro == producción (runner_corpus.fase_e1)",
          list(reg) == claves_prod, f"{list(reg)}")

    # ---- 8bis. regla corregida del ranking (fe de erratas §4, 930f289) -----
    import disparadores_esq2 as disp
    tos_sint = ("aaa", "bbb", "ccc")
    # s1: un disparador con un TO dominante — sin monopolio mientras otros
    # TOs tienen pendientes (la degeneración que la fe de erratas corrige).
    cand1 = {"d1": [f"aaa::u{i}" for i in range(10)]
             + ["bbb::u0", "bbb::u1", "ccc::u0", "ccc::u1"]}
    sel1 = disp.ranking_dirigida_anidado(cand1, set(), 6, tos=tos_sint)
    por_to1 = {}
    for e in sel1:
        por_to1[e["to"]] = por_to1.get(e["to"], 0) + 1
    check("8bis: sin monopolio — TO dominante no acapara con otros pendientes",
          por_to1 == {"aaa": 2, "bbb": 2, "ccc": 2}, f"{por_to1}")
    # s2: desempate por menor chunk_id dentro de cada par (disparador, TO)
    check("8bis: menor chunk_id por par",
          [e["chunk_id"] for e in sel1][:3] == ["aaa::u0", "bbb::u0", "ccc::u0"])
    # s3: dedup entre disparadores + ciclo propio por disparador
    cand2 = {"d1": ["aaa::u0", "bbb::u0"], "d2": ["aaa::u0", "aaa::u1", "bbb::u1"]}
    sel2 = disp.ranking_dirigida_anidado(cand2, set(), 4, tos=tos_sint)
    ids2 = [e["chunk_id"] for e in sel2]
    check("8bis: dedup entre disparadores (ninguna unidad dos veces)",
          len(ids2) == len(set(ids2)) == 4
          and set(ids2) == {"aaa::u0", "aaa::u1", "bbb::u0", "bbb::u1"},
          f"{ids2}")
    # s4: exclusión de la azarosa + pares agotados sin loop infinito
    sel3 = disp.ranking_dirigida_anidado(
        {"d1": ["aaa::u0", "bbb::u0"]}, {"aaa::u0"}, 5, tos=tos_sint)
    check("8bis: excluidas fuera y agotamiento devuelve lo que hay",
          [e["chunk_id"] for e in sel3] == ["bbb::u0"])
    # s5: determinismo (misma entrada → misma salida)
    check("8bis: determinismo",
          disp.ranking_dirigida_anidado(cand1, set(), 6, tos=tos_sint) == sel1)

    # ---- 9. sellos de producción -------------------------------------------
    a_sellar = [
        "data/experiment/reextraccion_v2/e1_extractor/prompt_e1.py",
        "data/experiment/reextraccion_v2/e1_extractor/cliente_e1.py",
        "data/experiment/reextraccion_v2/e1_extractor/validador_e1.py",
        "data/experiment/reextraccion_v2/e1_extractor/comun_e1.py",
        "data/experiment/grafo_v2/code/schema.py",
        "data/experiment/evaluacion/llm_cache.py",
        "data/experiment/reextraccion_v2/e1_extractor/cache/e1_extraccion.db",
    ]
    a_sellar += [f"data/experiment/reextraccion_v2/corpus_v2/salida/{to}/extracciones_e1.jsonl"
                 for to in comun_e1.TOS]
    a_sellar += [f"data/experiment/escalado_prep/e0_dry/{to}/chunks_{to}.json"
                 for to in cc.TOS_ESQ2]
    sellos = {"generado": datetime.now().isoformat(timespec="seconds"),
              "archivos": {rel: runner.sha256_de(cc.REPO_DIR / rel)
                           for rel in a_sellar}}
    cc.COBERTURA_DIR.mkdir(parents=True, exist_ok=True)
    (cc.COBERTURA_DIR / "sellos_produccion_sha256.json").write_text(
        json.dumps(sellos, ensure_ascii=False, indent=1), encoding="utf-8")
    check("sellos de producción escritos",
          len(sellos["archivos"]) == len(a_sellar),
          f"{len(a_sellar)} archivos sellados")

    print(f"\nRESULTADO: {'PASS' if not FALLAS else 'FAIL'} "
          f"({N_CHECKS - len(FALLAS)}/{N_CHECKS} checks) "
          f"| fallados: {FALLAS if FALLAS else 'ninguno'}")
    return 0 if not FALLAS else 1


if __name__ == "__main__":
    raise SystemExit(main())
