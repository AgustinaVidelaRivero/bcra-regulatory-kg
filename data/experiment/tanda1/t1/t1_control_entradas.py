"""
t1_control_entradas.py — B6.1, tanda 1, T1, punto 2.4 (pre-registro firmado en 95b18217, §4.1, punto 3): control de las
entradas de T2, cada una contra su valor del §2. USD 0, sin red, sin clave de la API. El modelo es
`data/experiment/reext_t0/t1_control_entradas.py` (U-REEXT-T0).

Dos modos:

  volcar --out <json>
      El sha256 del mensaje de E1 y del pedido canónico de cada unidad de la tanda 0 (los diez TOs de
      `tanda0_10tos_r2b.json`, E0 `salida_tanda0_r2b/`, 2.439 unidades) y de la tanda 1 (los 20 de
      `tanda1_20tos_r2b.json`, E0 `salida_tanda1_r2b/`, 3.290), armados con el perfil r2b de la raíz donde corre.
      Se corre en la copia y en un árbol armado con `git archive HEAD` (más la E0 de la tanda 1, que todavía no está
      en git): «los mensajes de E1 salen byte a byte iguales a los de HEAD».

  controlar --git-repo <repo> --clave-cache-json <json> --mensajes-head <json> --out <json>
      a. el prefijo de E1 del perfil r2b: hash, sha256, caracteres, el parche de P3c y la base de P3b-2;
      b. el tool schema (el archivo y el del pedido);
      c. el namespace de E1 y los de los dos reintentos por salida mal formada;
      d. el prefijo de E3 y su namespace;
      e. los 100 archivos por TO de `salida_tanda1_r2b/` contra su entrada del manifiesto de S0-6b, y la cuenta de
         archivos contra los sellos del manifiesto de la tanda 1;
      f. el candado del catálogo r2 y los insumos del prefijo con candado;
      g. la temperatura del pedido de E1 (0) en las 2.439 unidades de la tanda 0 y en las 3.290 de la tanda 1, y la del
         reintento por salida mal formada (1), con el resto del pedido igual;
      h. los candados que no entran al hash del prefijo: las tablas forzadas, el candado del mensaje de E1 en el valor
         de A2 (6b758517… / eeb11b9a…), el derivado del registro de alcance (e06933e7…) y el candado del mensaje de E3
         (079d2489… / 66bc8656…); y `selftest_clave_cache` en OK, con las variaciones R29, R29b, R30 y R32 frenando;
      i. los mensajes de E1 de las 2.439 unidades de la tanda 0 (y, además, los de las 3.290 de la tanda 1), byte a byte
         iguales a los del árbol de HEAD (`--mensajes-head`, del modo volcar);
      j. el recorte de herencia en la tanda 1: la línea del recorte aparece una vez en el mensaje de cada unidad que lo
         lleva y en ninguna otra;
      k. el rol de alcance de los 20: el del manifiesto contra el `rol_por_to` del perfil;
      l. los sellos del manifiesto de la tanda 1 contra lo que el código carga, el tope y el estimado;
      m. la carga del manifiesto de la tanda 1 con `manifiesto_corpus.cargar` y sus valores por defecto (sha256 de los
         PDF y roles), y el control en contra: el manifiesto de los 152 de S1-ter frena al cargarse con el perfil de
         A2, en manori.

Corre desde la raíz de una COPIA del repo (CLAUDE.md §4.l); `--git-repo` es el repo, del que solo se leen objetos de
git. Escribe solo `--out`.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/tanda1/t1/t1_control_entradas.py controlar \
      --git-repo <repo> --clave-cache-json <selftest de claves corrido en la copia> --mensajes-head <json> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from decimal import Decimal
from pathlib import Path

sys.dont_write_bytecode = True
AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))

MAN_T0 = REX / "manifiestos" / "tanda0_10tos_r2b.json"
MAN_T1 = REX / "manifiestos" / "tanda1_20tos_r2b.json"
MAN_S1TER = REPO / "data/experiment/segmentacion_oficial_e0r2/s1ter/manifiesto/segmentacion_oficial_e0r2_152.json"
MAN_S06B = REPO / "data/experiment/segmentacion_oficial_e0r2/s0_6/b/manifiestos/manifest_salida_e0_152_S0-6b.json"
E0_T0 = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
E0_T1 = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda1_r2b"
MODEL_E1 = "claude-haiku-4-5"     # runner_corpus.py:91; se controla abajo contra RC.MODEL_E1

# Valores del §2 del pre-registro (y de su tabla de sellos). Los prefijos de 8 caracteres son los del texto firmado;
# el valor completo sale del código y se compara contra ese prefijo.
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
    "candado_mensaje_r2b_json_inicio": "6b758517",
    "mensaje_r2b_inicio": "eeb11b9a",
    "registro_alcance_r2b_inicio": "e06933e7",
    "candado_mensaje_e3_json_inicio": "079d2489",
    "mensaje_e3_inicio": "66bc8656",
    "temperatura_e1": 0,
    "temperatura_reintento_forma": 1,
    "variaciones_frena": ("R29", "R29b", "R30", "R32"),
    "unidades_t0": 2439,
    "unidades_t1": 3290,
    "commit_codigo": "47c9f1b3",
    "tope_usd": 100.7291,
    "estimado_usd": Decimal("69.6592"),
}
POR_TO = ("chunks", "estructura", "indice", "pies", "tablas")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True).stdout


def leer(p: Path):
    return json.loads(p.read_text(encoding="utf-8"))


def unidades(man_path: Path, e0_rel: str) -> list[tuple[str, dict]]:
    import comun_e1
    man = leer(man_path)
    return [(to, c) for to in man["orden_corrida"] for c in comun_e1.cargar_chunks((to,), e0_dir=REPO / e0_rel)]


def volcar(a) -> int:
    import llm_cache as lc
    import perfil_e1
    pf = perfil_e1.perfil("r2b")
    out = {}
    for nombre, man, e0 in (("tanda0", MAN_T0, E0_T0), ("tanda1", MAN_T1, E0_T1)):
        filas = []
        for to, c in unidades(man, e0):
            kw = pf.build_request_kwargs(c, model=MODEL_E1)
            filas.append({"to": to, "chunk_id": c["id"], "sha256_mensaje": sha(kw["messages"][0]["content"].encode()),
                          "sha256_pedido": sha(lc.canonical_request(kw).encode())})
        out[nombre] = filas
    a.out.write_text(json.dumps(out, ensure_ascii=False, indent=0) + "\n", encoding="utf-8")
    print({k: len(v) for k, v in out.items()})
    return 0


def controlar(a) -> int:
    if a.out.resolve().is_relative_to(a.git_repo.resolve()):
        raise SystemExit("--out no puede estar dentro del repo")
    import comun_e1
    import perfil_e1
    import prompt_r2b as P
    import cliente_e1
    import cliente_e3
    import prompt_e3
    import modelos_r2
    import llm_cache as lc
    import manifiesto_corpus as MC
    import runner_corpus as RC

    res: dict = {"copia": "<copia>", "controles": {}}
    C = res["controles"]

    def check(clave: str, ok: bool, **detalle) -> None:
        C[clave] = {"ok": bool(ok), **detalle}

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

    t0 = unidades(MAN_T0, E0_T0)
    t1 = unidades(MAN_T1, E0_T1)
    s_tool = sha(P.TOOL_SCHEMA_R2_JSON.read_bytes())
    kw0 = pf.build_request_kwargs(t1[0][1], model=RC.MODEL_E1)
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
          and nsf2 == ESPERADO["namespace_e1"].replace("|think=0", "-rforma2|think=0"),
          namespace_e1=ns1, namespace_reintento_forma=nsf, namespace_reintento_forma_2=nsf2,
          modelo_e1=RC.MODEL_E1, modelo_e3=RC.MODEL_E3, modelo_e1_igual=RC.MODEL_E1 == MODEL_E1)

    ns3 = cliente_e3.namespace_e3()
    check("d_prefijo_y_namespace_e3", prompt_e3.PREFIJO_HASH == ESPERADO["prefijo_e3_hash"]
          and ns3 == f"e3_verificacion|cv=e3-verificador-v1-p{ESPERADO['prefijo_e3_hash']}|think=0",
          prefijo_hash=prompt_e3.PREFIJO_HASH, namespace_e3=ns3)

    # e. los 100 archivos por TO de la E0 de la tanda 1 contra el manifiesto de S0-6b
    m06 = leer(MAN_S06B)
    esperados = {k[len("e0/"):]: v for k, v in m06["sha256"].items() if k.startswith("e0/")}
    man1 = leer(MAN_T1)
    e0 = REPO / E0_T1
    por_to = {}
    for to in man1["orden_corrida"]:
        for pre in POR_TO:
            n = f"{pre}_{to}.json"
            p = e0 / n
            por_to[n] = p.is_file() and sha(p.read_bytes()) == esperados[n]["sha256"] and p.stat().st_size == esperados[n]["bytes"]
    archivos = sorted(p.name for p in e0.iterdir() if p.is_file())
    check("e_salida_tanda1_r2b", sum(por_to.values()) == 100 == len(por_to)
          and len(archivos) == man1["sellos"]["e0"]["archivos"],
          por_to_iguales=sum(por_to.values()), por_to_esperados=len(por_to),
          distintos=sorted(n for n, v in por_to.items() if not v), archivos=len(archivos),
          archivos_en_sellos=man1["sellos"]["e0"]["archivos"],
          agregados=[n for n in archivos if not n.startswith(POR_TO)], manifiesto_s06b_sha256=sha(MAN_S06B.read_bytes()))

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

    # g. temperatura, en las dos tandas
    temp = {}
    for nombre, uu in (("tanda0", t0), ("tanda1", t1)):
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
          and P.TEMPERATURA_E1_R2B == 0 and P.TEMPERATURA_REINTENTO_FORMA_R2B == 1,
          por_tanda=temp, constantes={"TEMPERATURA_E1_R2B": P.TEMPERATURA_E1_R2B,
                                      "TEMPERATURA_REINTENTO_FORMA_R2B": P.TEMPERATURA_REINTENTO_FORMA_R2B})

    # h. candados F04b, F22, F22b, F13c y F23, y el selftest de claves
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
          and s_cm == P.CANDADO_MENSAJE_JSON_SHA256_ESPERADO and s_cm.startswith(ESPERADO["candado_mensaje_r2b_json_inicio"])
          and s_m == P.MENSAJE_R2B_SHA256_ESPERADO and s_m.startswith(ESPERADO["mensaje_r2b_inicio"])
          and s_reg == P.REGISTRO_ALCANCE_R2B_SHA256_ESPERADO and s_reg.startswith(ESPERADO["registro_alcance_r2b_inicio"])
          and s_cm3 == prompt_e3.CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO
          and s_cm3.startswith(ESPERADO["candado_mensaje_e3_json_inicio"])
          and prompt_e3.MENSAJE_E3_SHA256_ESPERADO.startswith(ESPERADO["mensaje_e3_inicio"])
          and all(f["ok"] for f in frenan.values()) and all(frena_alguna.values())
          and cc.get("veredicto") == "OK",
          tablas_forzadas_sha256=s_tab, candado_mensaje_r2b_json_sha256=s_cm, mensaje_r2b_sha256=s_m,
          registro_alcance_r2b_json_sha256=s_reg, candado_mensaje_e3_json_sha256=s_cm3,
          mensaje_e3_sha256=prompt_e3.MENSAJE_E3_SHA256_ESPERADO, variaciones=frenan,
          veredicto_selftest_claves=cc.get("veredicto"), variaciones_r2b=len(cc["perfil_r2b"]["variaciones"]),
          clave_cache_json_sha256=sha(a.clave_cache_json.read_bytes()))

    # i. mensajes de E1 contra el árbol de HEAD
    head = leer(a.mensajes_head)
    msj = {}
    for nombre, uu in (("tanda0", t0), ("tanda1", t1)):
        aqui = [{"to": to, "chunk_id": c["id"],
                 "sha256_mensaje": sha(pf.build_request_kwargs(c, model=RC.MODEL_E1)["messages"][0]["content"].encode()),
                 "sha256_pedido": sha(lc.canonical_request(pf.build_request_kwargs(c, model=RC.MODEL_E1)).encode())}
                for to, c in uu]
        h = head[nombre]
        distintos = [x["chunk_id"] for x, y in zip(aqui, h) if x != y]
        msj[nombre] = {"unidades_copia": len(aqui), "unidades_head": len(h), "iguales": len(aqui) - len(distintos)
                       if len(aqui) == len(h) else None, "distintos": distintos[:20]}
    check("i_mensajes_e1_iguales_a_head", all(v["unidades_copia"] == v["unidades_head"] == v["iguales"]
                                              for v in msj.values())
          and msj["tanda0"]["unidades_copia"] == ESPERADO["unidades_t0"],
          por_tanda=msj, mensajes_head_sha256=sha(a.mensajes_head.read_bytes()))

    # j. recorte de herencia en la tanda 1
    con_recorte = [c for _, c in t1 if c.get("herencia_recortada")]
    lineas = {c["id"]: P.build_user_message_r2b(c).count(P.LINEA_RECORTE) for c in con_recorte}
    fuera = sum(P.LINEA_RECORTE in P.build_user_message_r2b(c) for _, c in t1 if not c.get("herencia_recortada"))
    check("j_herencia_recortada_tanda1", all(v == 1 for v in lineas.values()) and fuera == 0,
          unidades=sorted(lineas), lineas_del_recorte=lineas, linea_en_otras_unidades=fuera)

    # k. rol de alcance de los 20
    roles = {}
    for t in man1["tos"]:
        ent = pf.rol_por_to.get(t["archivo"])
        esperado = None if ent is None else (ent.get("rol_id") or list(ent["clase_ids"]))
        roles[t["id"]] = {"manifiesto": t["rol_alcance"], "perfil": esperado, "igual": t["rol_alcance"] == esperado,
                          "clase_ids": None if ent is None else ent.get("clase_ids"),
                          "de_la_tabla_de_la_release": t["archivo"] in P.ROL_POR_TO_R2,
                          "del_derivado": t["archivo"] in P.REGISTRO_ALCANCE_R2B}
    check("k_rol_de_alcance", all(v["igual"] for v in roles.values()) and len(roles) == 20,
          por_to=roles, con_alcance=sum(v["perfil"] is not None for v in roles.values()),
          sin_alcance=sorted(t for t, v in roles.items() if v["perfil"] is None),
          de_la_tabla=sum(v["de_la_tabla_de_la_release"] for v in roles.values()),
          del_derivado=sum(v["del_derivado"] and not v["de_la_tabla_de_la_release"] for v in roles.values()))

    # l. sellos del manifiesto de la tanda 1
    s = man1["sellos"]
    head_commit = git(a.git_repo, "rev-parse", ESPERADO["commit_codigo"]).decode().strip()
    estimado = sum(Decimal(str(v["e1"])) + Decimal(str(v["e3"])) for v in man1["limites"]["estimado_usd"].values())
    sellos_ok = {
        "commit_codigo": s["commit_codigo"] == ESPERADO["commit_codigo"] and head_commit.startswith(s["commit_codigo"]),
        "e0": s["e0"]["ruta"] == man1["rutas"]["e0_salida"] == E0_T1 and s["e0"]["archivos"] == len(archivos),
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
        "perfil": man1["perfil_e1"] == "r2b",
        "tope": man1["limites"]["tope_global_usd"] == ESPERADO["tope_usd"],
        "estimado": estimado.quantize(Decimal("0.0001")) == ESPERADO["estimado_usd"],
    }
    check("l_sellos_manifiesto_tanda1", all(sellos_ok.values()), detalle=sellos_ok, commit_codigo_completo=head_commit,
          estimado_usd=str(estimado), tope_usd=man1["limites"]["tope_global_usd"])

    # m. la carga y el control en contra
    try:
        m = MC.cargar(MAN_T1)
        carga = {"ok": True, "tos": len(m.ids), "orden": list(m.orden_corrida), "perfil": m.perfil_e1}
    except Exception as e:   # noqa: BLE001
        carga = {"ok": False, "error": f"{type(e).__name__}: {e}"}
    try:
        MC.cargar(MAN_S1TER)
        contra = {"frena": False}
    except MC.ErrorManifiesto as e:
        contra = {"frena": True, "error": str(e), "en_manori": "'manori'" in str(e)}
    check("m_carga_y_control_en_contra", carga["ok"] and carga.get("tos") == 20 and contra["frena"]
          and contra.get("en_manori"), carga=carga, control_en_contra=contra,
          manifiesto_tanda1_sha256=sha(MAN_T1.read_bytes()), manifiesto_s1ter_sha256=sha(MAN_S1TER.read_bytes()))

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
    v.add_argument("--out", type=Path, required=True)
    c = sp.add_parser("controlar")
    for k in ("--git-repo", "--clave-cache-json", "--mensajes-head", "--out"):
        c.add_argument(k, type=Path, required=True)
    a = ap.parse_args()
    return volcar(a) if a.modo == "volcar" else controlar(a)


if __name__ == "__main__":
    sys.exit(main())
