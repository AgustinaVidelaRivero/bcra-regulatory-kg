"""
t1_control_entradas.py — U-REEXT-T0, T1, punto 2 (mandato firmado en e2027dd): control de las entradas, cada una
contra su valor de «Lo que llega de las unidades anteriores». USD 0, sin red, sin clave de la API.

Controla:
  a. el prefijo de E1 del perfil r2b: hash, sha256, caracteres, el parche de P3c y la base de P3b-2 (los 27.840 tokens
     son una medición de la API en P3c-2: T1 no la repite);
  b. el tool schema (sha256 del archivo generado y el del pedido);
  c. el namespace de E1 y el del reintento por salida mal formada;
  d. el prefijo de E3 y su namespace;
  e. los 57 archivos de `e0_chunking/salida_tanda0_r2b/`, uno por uno, contra los del commit de C2 (9f6361e), leídos de
     los objetos de git del repo (`git show`, solo lectura);
  f. el candado del catálogo r2 (modelos_r2.py) y los insumos del prefijo con candado (bloque de catálogo, tabla de
     alcance, labels);
  g. la temperatura del pedido de E1 (0) en todas las unidades, y la del reintento por salida mal formada (1), con el
     resto del pedido igual;
  h. los candados de lo que no entra al hash del prefijo (F04b, F22, F22b y F23): los módulos cargan con sus sha256
     esperados; las variaciones R29, R29b, R30 y R32 del selftest de claves se leen del JSON que se le pasa;
  i. el recorte de herencia en `salida_tanda0_r2b/`: qué unidades lo llevan y cuántas veces lleva su mensaje la línea
     del recorte;
  j. el rol de alcance por TO (`rol_por_to_r2.json`): cuáles lo tienen, con rol propio o con clase, y docvig sin él;
  k. los sellos de los tres manifiestos r2b contra lo que el código carga.
El control del código (`git diff --stat 53b7708 HEAD` sobre la cadena) va en la batería de shell, con su salida.

Corre desde la raíz de una COPIA del repo (la regla l de CLAUDE.md §4); `--git-repo` es el repo, del que solo se leen
objetos de git. Escribe solo `--out`.
  PYTHONDONTWRITEBYTECODE=1 <repo>/.venv/bin/python -B data/experiment/reext_t0/t1_control_entradas.py \
      --git-repo <repo> --clave-cache-json <json del selftest de claves corrido en la copia> --out <json>
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[2]
REX = REPO / "data" / "experiment" / "reextraccion_v2"
for sub in ("e1_extractor", "e3_verificador", "e2_reduce", "corpus_v2", "e0_chunking"):
    sys.path.insert(0, str(REX / sub))
sys.path.insert(0, str(REX))
sys.path.insert(0, str(REPO / "data" / "experiment" / "evaluacion"))
sys.path.insert(0, str(REPO / "data" / "experiment" / "pyd_r2" / "code"))

E0_REL = "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2b"
COMMIT_C2 = "9f6361e"
MANIFIESTOS = ("tanda0_10tos_r2b.json", "tanda0_ens_diez_r2b.json", "tanda0_ens_desarrollo_r2b.json")
TOS = ("pro", "cla", "ric", "cap", "ext", "ctacte", "lingob", "polcre", "pagjub", "docvig")

# «Lo que llega de las unidades anteriores» (mandato, e2027dd:386-449). Los prefijos de 8 caracteres son los del
# texto firmado; el valor completo sale del código y se compara contra ese prefijo.
ESPERADO = {
    "prefijo_hash": "322c5a23e9b7",
    "prefijo_sha256_inicio": "ccffa4e3",
    "prefijo_caracteres": 59909,
    "parche_p3c_sha256_inicio": "5e3761c1",
    "base_p3b2_sha256_inicio": "8d84364f",
    "namespace_e1": "e1_extraccion|cv=e1-extractor-v1-p322c5a23e9b7|think=0",
    "sufijo_reintento_forma": "-rforma1",
    "tool_schema_sha256_inicio": "0c391f2b",
    "prefijo_e3_hash": "21a836c7de6d",
    "tablas_forzadas_sha256_inicio": "98cc96b2",
    "candado_mensaje_r2b_json_inicio": "4d69f7f4",
    "mensaje_r2b_inicio": "a9cb702c",
    "candado_mensaje_e3_json_inicio": "e8fa5dc4",
    "mensaje_e3_inicio": "da17c22e",
    "archivos_e0": 57,
    "temperatura_e1": 0,
    "temperatura_reintento_forma": 1,
    "variaciones_frena": ("R29", "R29b", "R30", "R32"),
    "unidad_herencia_recortada": "ric::11.2.3",
}


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def git(repo: Path, *args: str) -> bytes:
    return subprocess.run(["git", "-C", str(repo), *args], check=True, capture_output=True).stdout


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--git-repo", type=Path, required=True)
    ap.add_argument("--clave-cache-json", type=Path, required=True)
    ap.add_argument("--out", type=Path, required=True)
    a = ap.parse_args()
    if a.out.resolve().is_relative_to(a.git_repo.resolve()):
        raise SystemExit("--out no puede estar dentro del repo")

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
          parche_p3c_sha256=sha(P.PARCHE_P3C_JSON.read_bytes()), base_p3b2_sha256=P.PREFIJO_SHA256_R2B_P3B,
          tokens="27.840 medidos en P3c-2 con la API; T1 no los mide")

    s_tool = sha(P.TOOL_SCHEMA_R2_JSON.read_bytes())
    chunks_all = {to: comun_e1.cargar_chunks((to,), e0_dir=REPO / E0_REL) for to in TOS}
    c0 = chunks_all["pro"][0]
    kw0 = pf.build_request_kwargs(c0, model=RC.MODEL_E1)
    check("b_tool_schema", s_tool == P.TOOL_SCHEMA_R2_SHA256_ESPERADO
          and s_tool.startswith(ESPERADO["tool_schema_sha256_inicio"])
          and kw0["tools"] == [json.loads(P.TOOL_SCHEMA_R2_JSON.read_text(encoding="utf-8"))]
          and kw0["tools"] == [P.TOOL_SCHEMA_R2B],
          sha256=s_tool)

    ns1 = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace)
    nsf = cliente_e1.namespace_e1(prefijo_hash=pf.prefijo_hash_para_namespace, sufijo=cliente_e1.SUFIJO_REINTENTO_FORMA)
    check("c_namespace_e1", ns1 == ESPERADO["namespace_e1"]
          and cliente_e1.SUFIJO_REINTENTO_FORMA == ESPERADO["sufijo_reintento_forma"]
          and nsf == ESPERADO["namespace_e1"].replace("|think=0", "-rforma1|think=0"),
          namespace_e1=ns1, namespace_reintento_forma=nsf)

    ns3 = cliente_e3.namespace_e3()
    check("d_prefijo_y_namespace_e3", prompt_e3.PREFIJO_HASH == ESPERADO["prefijo_e3_hash"]
          and ns3 == f"e3_verificacion|cv=e3-verificador-v1-p{ESPERADO['prefijo_e3_hash']}|think=0",
          prefijo_hash=prompt_e3.PREFIJO_HASH, namespace_e3=ns3)

    # e. los 57 archivos contra los objetos de git de C2
    e0 = REPO / E0_REL
    locales = sorted(p.name for p in e0.iterdir() if p.is_file())
    arbol = git(a.git_repo, "ls-tree", "-r", "--name-only", COMMIT_C2, "--", E0_REL + "/").decode().split()
    nombres_c2 = sorted(Path(x).name for x in arbol)
    distintos = []
    for n in nombres_c2:
        if (e0 / n).exists():
            if sha((e0 / n).read_bytes()) != sha(git(a.git_repo, "show", f"{COMMIT_C2}:{E0_REL}/{n}")):
                distintos.append(n)
    check("e_salida_tanda0_r2b", len(locales) == ESPERADO["archivos_e0"] == len(nombres_c2)
          and locales == nombres_c2 and not distintos,
          archivos_copia=len(locales), archivos_c2=len(nombres_c2), distintos=distintos,
          solo_en_copia=sorted(set(locales) - set(nombres_c2)), solo_en_c2=sorted(set(nombres_c2) - set(locales)),
          pies=sorted(n for n in locales if n.startswith("pies_")))

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
          sujetos_vigentes=len(modelos_r2.SUJETOS_R2), insumos_del_prefijo=ins_ok,
          nota="«Lo que llega» no trae un valor del catálogo: la referencia es el candado del código "
               "(modelos_r2.py, CATALOGO_R2_SHA256) y el archivo en su commit")

    # g. temperatura
    n = t0 = forma_ok = 0
    for to in TOS:
        for c in chunks_all[to]:
            kw = pf.build_request_kwargs(c, model=RC.MODEL_E1)
            n += 1
            t0 += kw.get("temperature") == ESPERADO["temperatura_e1"] and type(kw.get("temperature")) is int
            kf = RC.kwargs_reintento_forma(kw, pf)
            forma_ok += (kf.get("temperature") == ESPERADO["temperatura_reintento_forma"]
                         and {k: v for k, v in kf.items() if k != "temperature"}
                         == {k: v for k, v in kw.items() if k != "temperature"}
                         and kw.get("temperature") == 0)
    check("g_temperatura", n == t0 == forma_ok and P.TEMPERATURA_E1_R2B == 0
          and P.TEMPERATURA_REINTENTO_FORMA_R2B == 1,
          unidades=n, con_temperatura_0=t0, reintento_forma_con_1_y_resto_igual=forma_ok,
          constantes={"TEMPERATURA_E1_R2B": P.TEMPERATURA_E1_R2B,
                      "TEMPERATURA_REINTENTO_FORMA_R2B": P.TEMPERATURA_REINTENTO_FORMA_R2B})

    # h. candados F04b, F22, F22b y F23
    s_tab = sha(P.TABLAS_FORZADAS_JSON.read_bytes())
    s_cm = sha(P.CANDADO_MENSAJE_JSON.read_bytes())
    s_m = P.sha256_mensajes(json.loads(P.CANDADO_MENSAJE_JSON.read_text(encoding="utf-8"))["chunks"])
    s_cm3 = sha(prompt_e3.CANDADO_MENSAJE_E3_JSON.read_bytes())
    cc = json.loads(a.clave_cache_json.read_text(encoding="utf-8"))
    var = {v["id"]: v for v in cc["perfil_r2b"]["variaciones"]}
    frenan = {vid: {"e1": var[vid]["e1"].get("observado") or var[vid]["e1"].get("token"),
                    "e3": var[vid]["e3"].get("observado") or var[vid]["e3"].get("token"),
                    "ok": var[vid]["e1"]["ok"] and var[vid]["e3"]["ok"],
                    "error": var[vid]["detalle"].get("error_e1") or var[vid]["detalle"].get("error_e3")}
              for vid in ESPERADO["variaciones_frena"]}
    frena_alguna = {vid: "frena" in (f["e1"], f["e3"]) for vid, f in frenan.items()}
    check("h_candados_F04b_F22_F22b_F23",
          s_tab == P.TABLAS_FORZADAS_SHA256_ESPERADO and s_tab.startswith(ESPERADO["tablas_forzadas_sha256_inicio"])
          and s_cm == P.CANDADO_MENSAJE_JSON_SHA256_ESPERADO and s_cm.startswith(ESPERADO["candado_mensaje_r2b_json_inicio"])
          and s_m == P.MENSAJE_R2B_SHA256_ESPERADO and s_m.startswith(ESPERADO["mensaje_r2b_inicio"])
          and s_cm3 == prompt_e3.CANDADO_MENSAJE_E3_JSON_SHA256_ESPERADO
          and s_cm3.startswith(ESPERADO["candado_mensaje_e3_json_inicio"])
          and prompt_e3.MENSAJE_E3_SHA256_ESPERADO.startswith(ESPERADO["mensaje_e3_inicio"])
          and all(f["ok"] for f in frenan.values()) and all(frena_alguna.values())
          and cc.get("veredicto") == "OK",
          tablas_forzadas_sha256=s_tab, candado_mensaje_r2b_json_sha256=s_cm, mensaje_r2b_sha256=s_m,
          candado_mensaje_e3_json_sha256=s_cm3, mensaje_e3_sha256=prompt_e3.MENSAJE_E3_SHA256_ESPERADO,
          variaciones=frenan, veredicto_selftest_claves=cc.get("veredicto"),
          variaciones_r2b=len(cc["perfil_r2b"]["variaciones"]))

    # i. recorte de herencia
    con_recorte = [c for to in TOS for c in chunks_all[to] if c.get("herencia_recortada")]
    lineas = {c["id"]: P.build_user_message_r2b(c).count(P.LINEA_RECORTE) for c in con_recorte}
    sin_linea_fuera = sum(P.LINEA_RECORTE in P.build_user_message_r2b(c)
                          for to in TOS for c in chunks_all[to] if not c.get("herencia_recortada"))
    check("i_herencia_recortada", [c["id"] for c in con_recorte] == [ESPERADO["unidad_herencia_recortada"]]
          and lineas.get(ESPERADO["unidad_herencia_recortada"]) == 1 and sin_linea_fuera == 0,
          unidades=[c["id"] for c in con_recorte], lineas_del_recorte=lineas,
          recorte=[c.get("herencia_recortada") for c in con_recorte], linea_en_otras_unidades=sin_linea_fuera)

    # j. rol de alcance
    man10 = MC.cargar(REX / "manifiestos" / MANIFIESTOS[0])
    roles = {}
    for to in TOS:
        ent = P.ROL_POR_TO_R2.get(man10.archivo_de(to))
        roles[to] = None if ent is None else ("clase" if ent.get("clase_ids") else "rol", ent.get("rol_id"))
    con = [t for t in TOS if roles[t] is not None]
    check("j_rol_de_alcance", len(con) == 9 and roles["docvig"] is None,
          por_to=roles, con_alcance=len(con),
          rol_propio=sum(1 for t in con if roles[t][0] == "rol"), clase=sum(1 for t in con if roles[t][0] == "clase"))

    # k. sellos de los manifiestos
    sellos = {}
    for m in MANIFIESTOS:
        man = MC.cargar(REX / "manifiestos" / m)
        s = man.sellos
        sellos[m] = {"e0": man._d["rutas"]["e0_salida"], "tope": man.limites["tope_global_usd"],
                     "ok": (man._d["rutas"]["e0_salida"] == E0_REL and man.limites["tope_global_usd"] == 80.0
                            and s["prefijo_e1"]["hash"] == pf.prefijo_hash and s["prefijo_e1"]["sha256"] == s_pref
                            and s["prefijo_e1"]["caracteres"] == len(texto)
                            and s["prefijo_e1"]["parche_p3c_sha256"] == P.PARCHE_P3C_SHA256_ESPERADO
                            and s["prefijo_e1"]["base_p3b2_sha256"] == P.PREFIJO_SHA256_R2B_P3B
                            and s["tool_schema_sha256"] == s_tool and s["namespace_e1"] == ns1
                            and s["namespace_reintento_forma"] == nsf and s["namespace_e3"] == ns3
                            and s["prefijo_e3_hash"] == prompt_e3.PREFIJO_HASH
                            and s["temperatura_e1"] == P.TEMPERATURA_E1_R2B
                            and s["temperatura_reintento_forma"] == P.TEMPERATURA_REINTENTO_FORMA_R2B
                            and s["candados"] == {"tablas_forzadas_sha256": s_tab,
                                                  "candado_mensaje_r2b_json_sha256": s_cm,
                                                  "mensaje_r2b_sha256": s_m,
                                                  "candado_mensaje_e3_json_sha256": s_cm3,
                                                  "mensaje_e3_sha256": prompt_e3.MENSAJE_E3_SHA256_ESPERADO}
                            and s["e0"]["archivos"] == len(locales) and man.perfil_e1 == "r2b")}
    check("k_sellos_manifiestos", all(v["ok"] for v in sellos.values()), manifiestos=sellos)

    res["veredicto"] = "OK" if all(v["ok"] for v in C.values()) else "FRENA"
    a.out.write_text(json.dumps(res, ensure_ascii=False, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    for k, v in C.items():
        print(f"{'OK ' if v['ok'] else 'FALLA'} {k}")
    print("veredicto:", res["veredicto"])
    return 0 if res["veredicto"] == "OK" else 1


if __name__ == "__main__":
    sys.exit(main())
