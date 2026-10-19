"""
t1_control_entradas_tanda_final.py — B6.1, tanda final, T1, punto 2.4 (pre-registro firmado de la tanda final, §4.1,
punto 3; el modelo es data/experiment/tanda1/t1/t1_control_entradas.py): control de las entradas de T2, cada una contra
su valor del §2. USD 0, sin red, sin clave de la API.

Dos modos:

  volcar --raiz <árbol> --e0-tanda-final <dir> --manifiesto-tanda-final <json> --out <json>
      Por el camino del runner (como data/experiment/alcance_e1/a3/scripts/mensajes_runner_a3.py): pone en el sys.path
      solo la carpeta del runner, importa runner_corpus de <árbol>, lo configura con el manifiesto r2b de la tanda 0
      (runner_corpus.configurar → perfil_e1.perfil("r2b") → prompt_r2b, con sus candados) y arma el pedido de E1 de cada
      unidad con runner_corpus.PERFIL.build_request_kwargs, con las unidades cargadas como fase_e1
      (comun_e1.cargar_chunks y chunks_sin_ids_repetidos):
        - tanda 0: las 2.439 unidades de los diez TOs de tanda0_10tos_r2b.json (runner_corpus.E0_DIR);
        - tanda 1: las 3.290 de los 20 de tanda1_20tos_r2b.json, con salida_tanda1_r2b/;
        - tanda final: las 4.951 de los 98 de --manifiesto-tanda-final (leído como JSON, sin validarlo, para que corra
          también con el código de la base de A3), con --e0-tanda-final.
      Por unidad escribe el sha256 del mensaje y del pedido canónico, la línea «Alcance de este TO» (si la hay) y el
      sha256 del mensaje sin esa línea y sin el renglón vacío que la sigue (el «línea + salto + salto» de A3). Además, que
      todo módulo de data/experiment cargado venga de <árbol>. Se corre en la copia (el código de HEAD, que es el de A3)
      y en un árbol de la base de A3 (5289b02f), armado con `git archive 5289b02f` de las 78 rutas, más las E0, los
      manifiestos y los PDF.

  controlar --raiz <copia> --git-repo <repo> --clave-cache-json <json> --mensajes-copia <json> --mensajes-base <json>
            --manifiesto-contra <json> --out <json>
      a. el prefijo de E1 del perfil r2b: hash, sha256, caracteres, el parche de P3c y la base de P3b-2;
      b. el tool schema (el archivo y el del pedido);
      c. el namespace de E1 y los de los dos reintentos por salida mal formada; los modelos del runner;
      d. el prefijo de E3 y su namespace;
      e. los 490 archivos por TO de salida_tanda_final_r2b/ contra su entrada del manifiesto de S0-6b, y la cuenta de
         archivos contra los sellos del manifiesto de la tanda final;
      f. el candado del catálogo r2 y los insumos del prefijo con candado;
      g. la temperatura del pedido de E1 (0) en las 2.439 unidades de la tanda 0, en las 3.290 de la tanda 1 y en las
         4.951 de la tanda final, y la del reintento por salida mal formada (1), con el resto del pedido igual;
      h. los candados que no entran al hash del prefijo: las tablas forzadas, el candado del mensaje de E1 y el mensaje
         (6b758517… / eeb11b9a…), el derivado de A3 (c8dea08a…) y el candado del mensaje de E3 (079d2489… / 66bc8656…); y
         `selftest_clave_cache` en OK (su JSON con las cuentas de claves retiradas), con R29, R29b, R30 y R32 frenando;
      i. los mensajes de E1 de la tanda 0 y de la tanda 1, byte a byte iguales a los del código de la base de A3; en la
         tanda final, cambian solo las unidades de los 33 documentos con entrada nueva del derivado, todas, y solo en la
         línea de alcance (sin esa línea, el mensaje es el de la base);
      j. el recorte de herencia en la tanda final: la línea del recorte aparece una vez en el mensaje de cada unidad que
         lo lleva y en ninguna otra;
      k. el rol de alcance de los 98: el del manifiesto contra el `rol_por_to` del perfil;
      l. los sellos del manifiesto de la tanda final contra lo que el código carga, el tope (151,5835) y el estimado: su
         suma es exacta contra U × 0,021115 más las líneas de alcance de A3 por documento, y a cuatro decimales contra
         U × 0,021115 más el total de A3 (0,209440; las líneas por documento, redondeadas, suman 0,209438);
      m. la carga del manifiesto de la tanda final con `manifiesto_corpus.cargar` y sus valores por defecto (sha256 de
         los PDF y roles), y el control en contra: el mismo manifiesto armado con el perfil anterior a A3 (el derivado
         e06933e7…) frena al cargarse, en un documento de los 33.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l); `--git-repo` es el repo, del que solo se leen objetos de
git. Escribe solo `--out`, fuera de la copia y del repo.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B t1_control_entradas_tanda_final.py volcar|controlar ...
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from decimal import ROUND_HALF_UP, Decimal
from pathlib import Path

sys.dont_write_bytecode = True
REX_REL = "data/experiment/reextraccion_v2"
MAN_T0_REL = f"{REX_REL}/manifiestos/tanda0_10tos_r2b.json"
MAN_T1_REL = f"{REX_REL}/manifiestos/tanda1_20tos_r2b.json"
MAN_TF_REL = f"{REX_REL}/manifiestos/tanda_final_98tos_r2b.json"
MAN_S06B_REL = "data/experiment/segmentacion_oficial_e0r2/s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json"
MEDICION_A3_REL = "data/experiment/alcance_e1/a3/salidas/medicion_mensajes_tres_tandas_a3.json"
E0_T1_REL = f"{REX_REL}/e0_chunking/salida_tanda1_r2b"
E0_TF_REL = f"{REX_REL}/e0_chunking/salida_tanda_final_r2b"
MODEL_E1 = "claude-haiku-4-5"     # runner_corpus.py:91; se controla abajo contra RC.MODEL_E1

# Valores del §2 del pre-registro de la tanda final (que remite al de la tanda 1) y de la versión derivada de T1.
ESPERADO = {
    "prefijo_hash": "322c5a23e9b7",
    "prefijo_sha256_inicio": "ccffa4e3",
    "prefijo_caracteres": 59909,
    "parche_p3c_sha256_inicio": "5e3761c1",
    "base_p3b2_sha256_inicio": "8d84364f",
    "namespace_e1": "e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0",
    "sufijo_reintento_forma": "-rforma1",
    "sufijo_reintento_forma_2": "-rforma2",
    "tool_schema_sha256_inicio": "0c391f2b",
    "prefijo_e3_hash": "21a836c7de6d",
    "tablas_forzadas_sha256_inicio": "98cc96b2",
    "candado_mensaje_r2b_json": "6b758517cee0f2e36c26c54f0f6738b3d49d11d0cf3141c26cff166ce6820325",
    "mensaje_r2b": "eeb11b9a3bf699d5535fcf2bbe79541ba746ae7bdae3341af962840990a97362",
    "registro_alcance_r2b": "c8dea08a2ffe2eeb401855f952cc80f26542da8ea2489eac7a6f83530b6857ca",
    "registro_alcance_r2b_anterior_inicio": "e06933e7",
    "candado_mensaje_e3_json_inicio": "079d2489",
    "mensaje_e3_inicio": "66bc8656",
    "temperatura_e1": 0,
    "temperatura_reintento_forma": 1,
    "variaciones_frena": ("R29", "R29b", "R30", "R32"),
    "unidades_t0": 2439,
    "unidades_t1": 3290,
    "unidades_tf": 4951,
    "tos_tf": 98,
    "documentos_con_entrada_nueva": 33,
    "unidades_que_cambian": 1178,
    "commit_codigo": "c66c7ecd",
    "tope_usd": 151.5835,
    "u_por_tarifa_mas_lineas_a3": Decimal("4951") * Decimal("0.021115") + Decimal("0.209440"),
}
POR_TO = ("chunks", "estructura", "indice", "pies", "tablas")
PREFIJO_ALCANCE = "Alcance de este TO"


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True).stdout


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def sin_linea(msg: str, linea: str | None) -> str:
    """El mensaje sin la línea de alcance y sin el renglón vacío que la sigue (prompt_r2b.linea_alcance)."""
    if linea is None:
        return msg
    partes = msg.split("\n")
    i = partes.index(linea)
    assert partes[i + 1] == "", "la línea de alcance no va seguida de un renglón vacío"
    del partes[i:i + 2]
    return "\n".join(partes)


# ------------------------------------------------------------------ volcar
def volcar(a) -> int:
    raiz = a.raiz.resolve()
    if a.out.resolve().is_relative_to(raiz):
        raise SystemExit("--out no puede estar dentro del árbol")
    sys.path.insert(0, str(raiz / REX_REL / "corpus_v2"))
    import runner_corpus as RC  # noqa: PLC0415 — el runner, con su sys.path
    RC.configurar(RC.manifiesto_corpus.cargar(raiz / MAN_T0_REL))
    if RC.PERFIL.nombre != "r2b":
        raise SystemExit(f"perfil {RC.PERFIL.nombre}")
    import llm_cache as lc  # noqa: PLC0415 — del sys.path que armó el runner

    def fila(to: str, c: dict) -> dict:
        kw = RC.PERFIL.build_request_kwargs(c, model=RC.MODEL_E1)
        m = kw["messages"][0]["content"]
        alc = [x for x in m.split("\n") if x.startswith(PREFIJO_ALCANCE)]
        linea = alc[0] if alc else None
        return {"to": to, "chunk_id": c["id"], "sha256_mensaje": sha(m.encode()),
                "sha256_pedido": sha(lc.canonical_request(kw).encode()),
                "lineas_alcance": len(alc), "linea_alcance": linea,
                "sha256_sin_linea": sha(sin_linea(m, linea).encode())}

    out = {}
    man0 = leer(raiz / MAN_T0_REL)
    out["tanda0"] = [fila(t["id"], c) for t in man0["tos"]
                     for c in RC.chunks_sin_ids_repetidos(RC.comun_e1.cargar_chunks((t["id"],), e0_dir=RC.E0_DIR), t["id"])]
    for nombre, man, e0 in (("tanda1", raiz / MAN_T1_REL, raiz / E0_T1_REL),
                            ("tanda_final", a.manifiesto_tanda_final.resolve(), a.e0_tanda_final.resolve())):
        orden = leer(man)["orden_corrida"]
        out[nombre] = [fila(to, c) for to in orden
                       for c in RC.chunks_sin_ids_repetidos(RC.comun_e1.cargar_chunks((to,), e0_dir=e0), to)]
    import prompt_r2b  # noqa: PLC0415 — ya importado por el perfil
    ajenos = sorted(m.__file__ for n, m in list(sys.modules.items())
                    if n != "__main__" and getattr(m, "__file__", None) and "/data/experiment/" in m.__file__
                    and raiz not in Path(m.__file__).resolve().parents)
    res = {"perfil": RC.PERFIL.nombre, "prefijo_hash": RC.PERFIL.prefijo_hash,
           "derivado_sha256_en_el_modulo": prompt_r2b.REGISTRO_ALCANCE_R2B_SHA256_ESPERADO,
           "derivado_entradas": len(prompt_r2b.REGISTRO_ALCANCE_R2B),
           "modulos_de_data_experiment_fuera_del_arbol": ajenos,
           "unidades": {k: len(v) for k, v in out.items()}, **out}
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print({"unidades": res["unidades"], "derivado": res["derivado_sha256_en_el_modulo"][:12],
           "entradas_del_derivado": res["derivado_entradas"], "modulos_fuera_del_arbol": len(ajenos)})
    return 0 if not ajenos else 1


# ------------------------------------------------------------------ controlar
def controlar(a) -> int:
    REPO = a.raiz.resolve()
    if a.out.resolve().is_relative_to(a.git_repo.resolve()) or a.out.resolve().is_relative_to(REPO):
        raise SystemExit("--out no puede estar dentro del repo ni de la copia")
    REX = REPO / REX_REL
    for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
        sys.path.insert(0, str(REX / sub))
    sys.path.insert(0, str(REX))
    sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
    sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))
    import comun_e1
    import perfil_e1
    import prompt_r2b as P
    import cliente_e1
    import cliente_e3
    import prompt_e3
    import modelos_r2
    import manifiesto_corpus as MC
    import runner_corpus as RC

    res: dict = {"copia": "<copia>", "controles": {}}
    C = res["controles"]

    def check(clave: str, ok: bool, **detalle) -> None:
        C[clave] = {"ok": bool(ok), **detalle}

    def unidades(man_path: Path, e0: Path) -> list[tuple[str, dict]]:
        man = leer(man_path)
        return [(to, c) for to in man["orden_corrida"]
                for c in RC.chunks_sin_ids_repetidos(comun_e1.cargar_chunks((to,), e0_dir=e0), to)]

    pf = perfil_e1.perfil("r2b")
    texto = P.PREFIJO_SISTEMA_R2B
    s_pref = sha(texto.encode("utf-8"))
    check("a_prefijo", pf.prefijo_hash == ESPERADO["prefijo_hash"] == P.PREFIJO_HASH_R2B
          and s_pref == P.PREFIJO_SHA256_R2B_ESPERADO and s_pref.startswith(ESPERADO["prefijo_sha256_inicio"])
          and len(texto) == ESPERADO["prefijo_caracteres"]
          and P.PARCHE_P3C_SHA256_ESPERADO.startswith(ESPERADO["parche_p3c_sha256_inicio"])
          and sha(P.PARCHE_P3C_JSON.read_bytes()) == P.PARCHE_P3C_SHA256_ESPERADO
          and P.PREFIJO_SHA256_R2B_P3B.startswith(ESPERADO["base_p3b2_sha256_inicio"]),
          hash=pf.prefijo_hash, sha256=s_pref, caracteres=len(texto),
          parche_p3c_sha256=sha(P.PARCHE_P3C_JSON.read_bytes()), base_p3b2_sha256=P.PREFIJO_SHA256_R2B_P3B)

    man0 = leer(REPO / MAN_T0_REL)
    t0 = [(t["id"], c) for t in man0["tos"]
          for c in RC.chunks_sin_ids_repetidos(comun_e1.cargar_chunks((t["id"],), e0_dir=REPO / man0["rutas"]["e0_salida"]),
                                               t["id"])]
    t1 = unidades(REPO / MAN_T1_REL, REPO / E0_T1_REL)
    tf = unidades(REPO / MAN_TF_REL, REPO / E0_TF_REL)
    s_tool = sha(P.TOOL_SCHEMA_R2_JSON.read_bytes())
    kw0 = pf.build_request_kwargs(tf[0][1], model=RC.MODEL_E1)
    check("b_tool_schema", s_tool == P.TOOL_SCHEMA_R2_SHA256_ESPERADO
          and s_tool.startswith(ESPERADO["tool_schema_sha256_inicio"])
          and kw0["tools"] == [json.loads(P.TOOL_SCHEMA_R2_JSON.read_text(encoding="utf-8"))]
          and kw0["tools"] == [P.TOOL_SCHEMA_R2B], sha256=s_tool)

    ns1 = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace)
    nsf = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA)
    nsf2 = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace,
                                   sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA_2)
    check("c_namespace_e1", ns1 == ESPERADO["namespace_e1"]
          and cliente_e1.SUFIJO_REINTENTO_FORMA == ESPERADO["sufijo_reintento_forma"]
          and cliente_e1.SUFIJO_REINTENTO_FORMA_2 == ESPERADO["sufijo_reintento_forma_2"]
          and nsf == ESPERADO["namespace_e1"].replace("|think=0", "-rforma1|think=0")
          and nsf2 == ESPERADO["namespace_e1"].replace("|think=0", "-rforma2|think=0")
          and RC.MODEL_E1 == MODEL_E1 and RC.MODEL_E3 == "claude-sonnet-5",
          namespace_e1=ns1, namespace_reintento_forma=nsf, namespace_reintento_forma_2=nsf2,
          modelo_e1=RC.MODEL_E1, modelo_e3=RC.MODEL_E3, modelo_e1_igual=RC.MODEL_E1 == MODEL_E1)

    ns3 = cliente_e3.namespace_e3()
    check("d_prefijo_y_namespace_e3", prompt_e3.PREFIJO_HASH == ESPERADO["prefijo_e3_hash"]
          and ns3 == f"e3_verificacion|cv=e3-verificador-v1-p{ESPERADO['prefijo_e3_hash']}|think=0",
          prefijo_hash=prompt_e3.PREFIJO_HASH, namespace_e3=ns3)

    # e. los 490 archivos por TO de la E0 de la tanda final contra el manifiesto de S0-6b
    m06 = leer(REPO / MAN_S06B_REL)
    esperados = {k[len("e0/"):]: v for k, v in m06["sha256"].items() if k.startswith("e0/")}
    manf = leer(REPO / MAN_TF_REL)
    e0 = REPO / E0_TF_REL
    por_to = {}
    for to in manf["orden_corrida"]:
        for pre in POR_TO:
            n = f"{pre}_{to}.json"
            p = e0 / n
            por_to[n] = p.is_file() and sha(p.read_bytes()) == esperados[n]["sha256"] and p.stat().st_size == esperados[n]["bytes"]
    archivos = sorted(p.name for p in e0.iterdir() if p.is_file())
    check("e_salida_tanda_final_r2b", sum(por_to.values()) == 5 * ESPERADO["tos_tf"] == len(por_to)
          and len(archivos) == manf["sellos"]["e0"]["archivos"],
          por_to_iguales=sum(por_to.values()), por_to_esperados=len(por_to),
          distintos=sorted(n for n, v in por_to.items() if not v), archivos=len(archivos),
          archivos_en_sellos=manf["sellos"]["e0"]["archivos"],
          agregados=[n for n in archivos if not n.startswith(POR_TO)],
          manifiesto_s06b_sha256=sha((REPO / MAN_S06B_REL).read_bytes()))

    # f. candado del catálogo y de los insumos del prefijo
    s_cat = sha(modelos_r2.CATALOGO_R2.read_bytes())
    s_enum = sha(modelos_r2.ENUMS_CATALOGO_R2.read_bytes())
    s_cat_bd = sha(git(a.git_repo, "show", f"{modelos_r2.CATALOGO_R2_COMMIT}:data/experiment/catalogo_unico/"
                                          "catalogo_sujetos_r2.json"))
    insumos = {"bloque_catalogo_r2": (P.BLOQUE_CATALOGO_R2, P.BLOQUE_CATALOGO_R2_SHA256_ESPERADO),
               "rol_por_to_r2": (P.ROL_POR_TO_R2_JSON, P.ROL_POR_TO_R2_SHA256_ESPERADO),
               "labels_e2_r2": (P.LABELS_E2_R2_JSON, P.LABELS_E2_R2_SHA256_ESPERADO),
               "reemplazos_p2": (P.REEMPLAZOS_JSON, P.REEMPLAZOS_SHA256_ESPERADO),
               "parche_p3b": (P.PARCHE_P3B_JSON, P.PARCHE_P3B_SHA256_ESPERADO)}
    ins_ok = {k: sha(p.read_bytes()) == e for k, (p, e) in insumos.items()}
    check("f_candado_catalogo", s_cat == modelos_r2.CATALOGO_R2_SHA256 == s_cat_bd
          and s_enum == modelos_r2.ENUMS_CATALOGO_R2_SHA256 and all(ins_ok.values())
          and modelos_r2.SUJETOS_R2_SET == pf.esquema.sujetos_catalogo_set,
          catalogo_sha256=s_cat, catalogo_commit=modelos_r2.CATALOGO_R2_COMMIT, enums_sha256=s_enum,
          sujetos_vigentes=len(modelos_r2.SUJETOS_R2), insumos_del_prefijo=ins_ok)

    # g. temperatura, en las tres tandas
    temp = {}
    for nombre, uu in (("tanda0", t0), ("tanda1", t1), ("tanda_final", tf)):
        n = n0 = forma_ok = 0
        for _, c in uu:
            kw = pf.build_request_kwargs(c, model=RC.MODEL_E1)
            n += 1
            n0 += kw.get("temperature") == ESPERADO["temperatura_e1"] and type(kw.get("temperature")) is int
            kf = RC.kwargs_reintento_forma(kw, pf)
            forma_ok += (kf.get("temperature") == ESPERADO["temperatura_reintento_forma"]
                         and {k: v for k, v in kf.items() if k != "temperature"}
                         == {k: v for k, v in kw.items() if k != "temperature"})
        temp[nombre] = {"unidades": n, "con_temperatura_0": n0, "reintento_forma_con_1_y_resto_igual": forma_ok}
    check("g_temperatura", all(v["unidades"] == v["con_temperatura_0"] == v["reintento_forma_con_1_y_resto_igual"]
                               for v in temp.values())
          and temp["tanda0"]["unidades"] == ESPERADO["unidades_t0"] and temp["tanda1"]["unidades"] == ESPERADO["unidades_t1"]
          and temp["tanda_final"]["unidades"] == ESPERADO["unidades_tf"]
          and P.TEMPERATURA_E1_R2B == 0 and P.TEMPERATURA_REINTENTO_FORMA_R2B == 1,
          por_tanda=temp, constantes={"TEMPERATURA_E1_R2B": P.TEMPERATURA_E1_R2B,
                                      "TEMPERATURA_REINTENTO_FORMA_R2B": P.TEMPERATURA_REINTENTO_FORMA_R2B})

    # h. candados F04b, F22, F22b, F13c y F23, y el selftest de claves (con las cuentas retiradas)
    s_tab = sha(P.TABLAS_FORZADAS_JSON.read_bytes())
    s_cm = sha(P.CANDADO_MENSAJE_JSON.read_bytes())
    s_m = P.sha256_mensajes(json.loads(P.CANDADO_MENSAJE_JSON.read_text(encoding="utf-8"))["chunks"])
    s_reg = sha(P.REGISTRO_ALCANCE_R2B_JSON.read_bytes())
    s_cm3 = sha(prompt_e3.CANDADO_MENSAJE_E3_JSON.read_bytes())
    cc = leer(a.clave_cache_json)
    var = {v["id"]: v for v in cc["perfil_r2b"]["variaciones"]}
    frenan = {vid: {"e1": var[vid]["e1"].get("observado") or var[vid]["e1"].get("token"),
                    "e3": var[vid]["e3"].get("observado") or var[vid]["e3"].get("token"),
                    "ok": var[vid]["e1"]["ok"] and var[vid]["e3"]["ok"]}
              for vid in ESPERADO["variaciones_frena"]}
    frena_alguna = {vid: "frena" in (f["e1"], f["e3"]) for vid, f in frenan.items()}
    check("h_candados_y_selftest_claves",
          s_tab == P.TABLAS_FORZADAS_SHA256_ESPERADO and s_tab.startswith(ESPERADO["tablas_forzadas_sha256_inicio"])
          and s_cm == P.CANDADO_MENSAJE_JSON_SHA256_ESPERADO == ESPERADO["candado_mensaje_r2b_json"]
          and s_m == P.MENSAJE_R2B_SHA256_ESPERADO == ESPERADO["mensaje_r2b"]
          and s_reg == P.REGISTRO_ALCANCE_R2B_SHA256_ESPERADO == ESPERADO["registro_alcance_r2b"]
          and s_cm3 == prompt_e3.CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO
          and s_cm3.startswith(ESPERADO["candado_mensaje_e3_json_inicio"])
          and prompt_e3.MENSAJE_E3_SHA256_ESPERADO.startswith(ESPERADO["mensaje_e3_inicio"])
          and all(f["ok"] for f in frenan.values()) and all(frena_alguna.values())
          and cc.get("veredicto") == "OK",
          tablas_forzadas_sha256=s_tab, candado_mensaje_r2b_json_sha256=s_cm, mensaje_r2b_sha256=s_m,
          registro_alcance_r2b_json_sha256=s_reg, candado_mensaje_e3_json_sha256=s_cm3,
          mensaje_e3_sha256=prompt_e3.MENSAJE_E3_SHA256_ESPERADO, variaciones=frenan,
          veredicto_selftest_claves=cc.get("veredicto"), variaciones_r2b=len(cc["perfil_r2b"]["variaciones"]),
          clave_cache_json_sin_cuentas_sha256=sha(a.clave_cache_json.read_bytes()))

    # i. mensajes de E1: copia (A3) contra la base de A3
    mc, mb = leer(a.mensajes_copia), leer(a.mensajes_base)
    alc_a3 = leer(REPO / MEDICION_A3_REL)["tanda_final"]
    nuevos = set(alc_a3["entradas_nuevas_del_derivado"] if isinstance(alc_a3["entradas_nuevas_del_derivado"], list)
                 else alc_a3["documentos_con_linea_nueva"])
    msj = {}
    for nombre in ("tanda0", "tanda1"):
        x, y = mc[nombre], mb[nombre]
        claves = lambda f: (f["to"], f["chunk_id"], f["sha256_mensaje"], f["sha256_pedido"])
        distintos = [p["chunk_id"] for p, q in zip(x, y) if claves(p) != claves(q)]
        msj[nombre] = {"unidades_copia": len(x), "unidades_base": len(y),
                       "iguales": len(x) - len(distintos) if len(x) == len(y) else None, "distintos": distintos[:20]}
    x, y = mc["tanda_final"], mb["tanda_final"]
    mismo_orden = [(p["to"], p["chunk_id"]) for p in x] == [(q["to"], q["chunk_id"]) for q in y]
    cambian = [p for p, q in zip(x, y) if p["sha256_mensaje"] != q["sha256_mensaje"]]
    docs_cambian = sorted({p["to"] for p in cambian})
    solo_la_linea = sum(1 for p, q in zip(x, y) if p["sha256_mensaje"] != q["sha256_mensaje"]
                        and p["lineas_alcance"] == 1 and q["lineas_alcance"] == 0
                        and p["sha256_sin_linea"] == q["sha256_mensaje"])
    unidades_nuevos = sum(1 for p in x if p["to"] in nuevos)
    iguales_resto = all(p["sha256_mensaje"] == q["sha256_mensaje"] and p["sha256_pedido"] == q["sha256_pedido"]
                        for p, q in zip(x, y) if p["to"] not in nuevos)
    msj["tanda_final"] = {"unidades_copia": len(x), "unidades_base": len(y), "mismo_orden": mismo_orden,
                          "unidades_que_cambian": len(cambian), "documentos_que_cambian": len(docs_cambian),
                          "documentos_que_cambian_son_los_33": docs_cambian == sorted(nuevos),
                          "unidades_de_los_33": unidades_nuevos,
                          "cambian_solo_en_la_linea_de_alcance": solo_la_linea,
                          "los_otros_documentos_iguales_byte_a_byte": iguales_resto}
    check("i_mensajes_e1_contra_la_base_de_a3",
          all(v["unidades_copia"] == v["unidades_base"] == v["iguales"] for k, v in msj.items() if k != "tanda_final")
          and msj["tanda0"]["unidades_copia"] == ESPERADO["unidades_t0"]
          and msj["tanda1"]["unidades_copia"] == ESPERADO["unidades_t1"]
          and len(x) == len(y) == ESPERADO["unidades_tf"] and mismo_orden
          and len(nuevos) == ESPERADO["documentos_con_entrada_nueva"] and docs_cambian == sorted(nuevos)
          and len(cambian) == unidades_nuevos == solo_la_linea == ESPERADO["unidades_que_cambian"] and iguales_resto
          and not mc["modulos_de_data_experiment_fuera_del_arbol"] and not mb["modulos_de_data_experiment_fuera_del_arbol"]
          and mb["derivado_sha256_en_el_modulo"].startswith(ESPERADO["registro_alcance_r2b_anterior_inicio"])
          and mc["derivado_sha256_en_el_modulo"] == ESPERADO["registro_alcance_r2b"],
          por_tanda=msj, derivado_copia=mc["derivado_sha256_en_el_modulo"], derivado_base=mb["derivado_sha256_en_el_modulo"],
          mensajes_copia_sha256=sha(a.mensajes_copia.read_bytes()), mensajes_base_sha256=sha(a.mensajes_base.read_bytes()))

    # j. recorte de herencia en la tanda final
    con_recorte = [c for _, c in tf if c.get("herencia_recortada")]
    lineas = {c["id"]: P.build_user_message_r2b(c).count(P.LINEA_RECORTE) for c in con_recorte}
    fuera = sum(P.LINEA_RECORTE in P.build_user_message_r2b(c) for _, c in tf if not c.get("herencia_recortada"))
    check("j_herencia_recortada_tanda_final", all(v == 1 for v in lineas.values()) and fuera == 0,
          unidades=len(lineas), por_to={to: sum(1 for t, c in tf if t == to and c.get("herencia_recortada"))
                                        for to in sorted({t for t, c in tf if c.get("herencia_recortada")})},
          linea_en_otras_unidades=fuera)

    # k. rol de alcance de los 98
    roles = {}
    for t in manf["tos"]:
        ent = pf.rol_por_to.get(t["archivo"])
        esperado = None if ent is None else (ent.get("rol_id") or list(ent["clase_ids"]))
        roles[t["id"]] = {"manifiesto": t["rol_alcance"], "perfil": esperado, "igual": t["rol_alcance"] == esperado,
                          "de_la_tabla_de_la_release": t["archivo"] in P.ROL_POR_TO_R2,
                          "del_derivado": t["archivo"] in P.REGISTRO_ALCANCE_R2B}
    check("k_rol_de_alcance", all(v["igual"] for v in roles.values()) and len(roles) == ESPERADO["tos_tf"],
          con_alcance=sum(v["perfil"] is not None for v in roles.values()),
          sin_alcance=sorted(t for t, v in roles.items() if v["perfil"] is None),
          de_la_tabla=sum(v["de_la_tabla_de_la_release"] for v in roles.values()),
          del_derivado=sum(v["del_derivado"] and not v["de_la_tabla_de_la_release"] for v in roles.values()),
          distintos=sorted(t for t, v in roles.items() if not v["igual"]))

    # l. sellos del manifiesto de la tanda final
    s = manf["sellos"]
    head_commit = git(a.git_repo, "rev-parse", ESPERADO["commit_codigo"]).decode().strip()
    estimado = sum(Decimal(str(v["e1"])) + Decimal(str(v["e3"])) for v in manf["limites"]["estimado_usd"].values())
    lineas_doc = sum(Decimal(str(v["usd_agregados"])) for v in alc_a3["por_documento"].values())
    u_lineas_doc = Decimal(ESPERADO["unidades_tf"]) * Decimal("0.021115") + lineas_doc
    sellos_ok = {
        "commit_codigo": s["commit_codigo"] == ESPERADO["commit_codigo"] and head_commit.startswith(s["commit_codigo"]),
        "e0": s["e0"]["ruta"] == manf["rutas"]["e0_salida"] == E0_TF_REL and s["e0"]["archivos"] == len(archivos),
        "prefijo_e1": (s["prefijo_e1"]["hash"] == pf.prefijo_hash and s["prefijo_e1"]["sha256"] == s_pref
                       and s["prefijo_e1"]["caracteres"] == len(texto)
                       and s["prefijo_e1"]["parche_p3c_sha256"] == P.PARCHE_P3C_SHA256_ESPERADO
                       and s["prefijo_e1"]["base_p3b2_sha256"] == P.PREFIJO_SHA256_R2B_P3B),
        "tool_schema": s["tool_schema_sha256"] == s_tool,
        "namespaces": s["namespace_e1"] == ns1 and s["namespace_reintento_forma"] == nsf and s["namespace_e3"] == ns3,
        "prefijo_e3": s["prefijo_e3_hash"] == prompt_e3.PREFIJO_HASH,
        "temperaturas": (s["temperatura_e1"] == P.TEMPERATURA_E1_R2B
                         and s["temperatura_reintento_forma"] == P.TEMPERATURA_REINTENTO_FORMA_R2B),
        "candados": s["candados"] == {"tablas_forzadas_sha256": s_tab, "candado_mensaje_r2b_json_sha256": s_cm,
                                      "mensaje_r2b_sha256": s_m, "registro_alcance_r2b_json_sha256": s_reg,
                                      "candado_mensaje_e3_json_sha256": s_cm3,
                                      "mensaje_e3_sha256": prompt_e3.MENSAJE_E3_SHA256_ESPERADO},
        "perfil": manf["perfil_e1"] == "r2b",
        "tope": manf["limites"]["tope_global_usd"] == ESPERADO["tope_usd"],
        "estimado_igual_a_u_por_tarifa_mas_lineas_por_documento": estimado == u_lineas_doc,
        "estimado_a_4_decimales_igual_a_u_por_tarifa_mas_lineas_a3":
            estimado.quantize(Decimal("0.0001"), ROUND_HALF_UP)
            == ESPERADO["u_por_tarifa_mas_lineas_a3"].quantize(Decimal("0.0001"), ROUND_HALF_UP),
    }
    check("l_sellos_manifiesto_tanda_final", all(sellos_ok.values()), detalle=sellos_ok,
          commit_codigo_completo=head_commit, estimado_usd=str(estimado),
          u_por_tarifa_mas_lineas_a3_usd=str(ESPERADO["u_por_tarifa_mas_lineas_a3"]),
          lineas_a3_por_documento_sumadas_usd=str(lineas_doc), u_por_tarifa_mas_lineas_por_documento_usd=str(u_lineas_doc),
          diferencia=str(estimado - ESPERADO["u_por_tarifa_mas_lineas_a3"]), tope_usd=manf["limites"]["tope_global_usd"])

    # m. la carga y el control en contra
    try:
        m = MC.cargar(REPO / MAN_TF_REL)
        carga = {"ok": True, "tos": len(m.ids), "perfil": m.perfil_e1, "orden_igual": list(m.orden_corrida)
                 == manf["orden_corrida"]}
    except Exception as e:   # noqa: BLE001
        carga = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    try:
        MC.cargar(a.manifiesto_contra)
        contra = {"frena": False}
    except MC.ErrorManifiesto as e:
        to_err = str(e).split("'")[1] if "'" in str(e) else None
        contra = {"frena": True, "error": str(e), "en_un_documento_de_los_33": to_err in nuevos, "documento": to_err}
    mcontra = leer(a.manifiesto_contra)
    check("m_carga_y_control_en_contra", carga["ok"] and carga.get("tos") == ESPERADO["tos_tf"] and carga.get("orden_igual")
          and contra["frena"] and contra.get("en_un_documento_de_los_33"), carga=carga, control_en_contra=contra,
          manifiesto_tanda_final_sha256=sha((REPO / MAN_TF_REL).read_bytes()),
          manifiesto_contra_sha256=sha(a.manifiesto_contra.read_bytes()),
          manifiesto_contra_null_en_los_33=sum(1 for t in mcontra["tos"] if t["id"] in nuevos and t["rol_alcance"] is None),
          manifiesto_contra_difiere_solo_en_rol_alcance=(
              {k: v for k, v in mcontra.items() if k != "tos"} == {k: v for k, v in manf.items() if k != "tos"}
              and [{k: v for k, v in t.items() if k != "rol_alcance"} for t in mcontra["tos"]]
              == [{k: v for k, v in t.items() if k != "rol_alcance"} for t in manf["tos"]]))

    res["veredicto"] = "OK" if all(v["ok"] for v in C.values()) else "FRENA"
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    for k, v in C.items():
        print(f"{'OK ' if v['ok'] else 'FALLA'} {k}")
    print("veredicto:", res["veredicto"])
    return 0 if res["veredicto"] == "OK" else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="modo", required=True)
    v = sp.add_parser("volcar")
    for k in ("--raiz", "--e0-tanda-final", "--manifiesto-tanda-final", "--out"):
        v.add_argument(k, type=Path, required=True)
    c = sp.add_parser("controlar")
    for k in ("--raiz", "--git-repo", "--clave-cache-json", "--mensajes-copia", "--mensajes-base",
              "--manifiesto-contra", "--out"):
        c.add_argument(k, type=Path, required=True)
    a = ap.parse_args()
    return volcar(a) if a.modo == "volcar" else controlar(a)


if __name__ == "__main__":
    sys.exit(main())
