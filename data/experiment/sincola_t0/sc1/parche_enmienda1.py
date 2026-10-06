"""U-SINCOLA-T0, SC1-bis: el cambio del punto 3 de la enmienda 1 (1f7c159), como reemplazos exactos sobre una raíz
(copia del repo primero; el repo después, con el mismo script). Cada reemplazo exige que el texto viejo aparezca
exactamente una vez; si no, no escribe nada. Toca solo las tres escrituras del punto 7 de la enmienda:
  - data/experiment/tanda0/code/ensamblar_tanda0.py: main() pasa con_cola a la rama r2; ensamblar_manifiesto_r2 lo
    recibe y lo pasa a sus dos corridas; correr_cadena_r2 lo recibe y descarta los registros de la cola después de
    entrada_r2, en ese único punto (descartar_cola_r2); el resumen declara con_cola y cola_descartada_por_to;
  - data/experiment/r2_codigo/selftest_r3.py: grupo T9 (el caso nuevo del punto 4.iii);
  - data/experiment/mantenimiento/tabla_reprocesamiento.md: nota a la fila F15 (punto 4.iv).
Uso: python -B parche_sc1bis.py <raiz>
"""
import sys
from pathlib import Path

RAIZ = Path(sys.argv[1]).resolve()
ENS = RAIZ / "data/experiment/tanda0/code/ensamblar_tanda0.py"
SELF = RAIZ / "data/experiment/r2_codigo/selftest_r3.py"
TABLA = RAIZ / "data/experiment/mantenimiento/tabla_reprocesamiento.md"

R_ENS = [
    # (a) main(): la rama r2 recibe la bandera
    ('        res = ensamblar_manifiesto_r2(man, args.entrada, args.salida, tablas)\n',
     '        res = ensamblar_manifiesto_r2(man, args.entrada, args.salida, tablas, con_cola=not args.sin_cola)\n'),
    ('    ap.add_argument("--sin-cola", action="store_true",\n'
     '                    help="no inyectar la cola flaggeada (r1 corrió CON cola: default con cola)")\n',
     '    ap.add_argument("--sin-cola", action="store_true",\n'
     '                    help="no inyectar la cola flaggeada (r1 corrió CON cola: default con cola); en la cadena r2 "\n'
     '                         "(U-SINCOLA-T0, enmienda 1) descarta los registros de la cola humana después de entrada_r2")\n'),
    # (b) ensamblar_manifiesto_r2 recibe con_cola y lo pasa a sus dos corridas
    ('def ensamblar_manifiesto_r2(man: MC.Manifiesto, entrada: Path, salida: Path,\n'
     '                            tablas_dir: Path | None = None) -> dict:\n'
     '    perfil = perfil_e1.perfil(man.perfil_e1)\n',
     'def ensamblar_manifiesto_r2(man: MC.Manifiesto, entrada: Path, salida: Path,\n'
     '                            tablas_dir: Path | None = None, con_cola: bool = True) -> dict:\n'
     '    """`con_cola` (U-SINCOLA-T0, enmienda 1 al mandato, 06/10/2026): con False,\n'
     '    las dos corridas de `correr_cadena_r2` descartan los registros de la cola\n'
     '    humana (`descartar_cola_r2`); el reporte declara `con_cola` y las unidades\n'
     '    descartadas por TO. Con True (default), la salida de siempre."""\n'
     '    perfil = perfil_e1.perfil(man.perfil_e1)\n'),
    ('        a = correr_cadena_r2(man, perfil, w, wl, tablas_dir)\n',
     '        a = correr_cadena_r2(man, perfil, w, wl, tablas_dir, con_cola=con_cola)\n'),
    ('        b = correr_cadena_r2(man, perfil, None, None, tablas_dir)\n',
     '        b = correr_cadena_r2(man, perfil, None, None, tablas_dir, con_cola=con_cola)\n'),
    # (c) correr_cadena_r2 recibe con_cola y descarta en un único punto
    ('def correr_cadena_r2(man: MC.Manifiesto, perfil, w=None, wl=None, tablas_dir: Path | None = None,\n'
     '                     fase: str | None = None) -> dict:\n',
     'def descartar_cola_r2(regs: list[dict], con_cola: bool) -> tuple[list[dict], list[str]]:\n'
     '    """U-SINCOLA-T0, enmienda 1 al mandato (06/10/2026), punto 3.c: con\n'
     '    `con_cola` False, los registros de la cola humana que devuelve\n'
     '    `runner_corpus.entrada_r2` (`cola_humana` True) se descartan antes de\n'
     '    `resolver_relaciones_r2` y de `ensamblar_r2`, en ese único punto; el\n'
     '    registro de omisiones, el paso por E3, `cola_estados`, `flaggear_cola_r2`\n'
     '    y `aristas_derivadas_de_cola` se computan sobre lo que queda. Con True, los\n'
     '    registros vuelven tal cual. Devuelve (registros, chunk_ids descartados en\n'
     '    el orden de E0)."""\n'
     '    if con_cola:\n'
     '        return regs, []\n'
     '    return ([r for r in regs if not r.get("cola_humana")],\n'
     '            [r["chunk_id"] for r in regs if r.get("cola_humana")])\n'
     '\n'
     '\n'
     'def correr_cadena_r2(man: MC.Manifiesto, perfil, w=None, wl=None, tablas_dir: Path | None = None,\n'
     '                     fase: str | None = None, con_cola: bool = True) -> dict:\n'),
    ('    en el reporte (s); el plazo sin marcador (m) va por `llenar_umbrales_r2`."""\n',
     '    en el reporte (s); el plazo sin marcador (m) va por `llenar_umbrales_r2`.\n'
     '    `con_cola` (U-SINCOLA-T0, enmienda 1, 06/10/2026): con False, los registros\n'
     '    de la cola humana se descartan después de `entrada_r2`, en ese único punto\n'
     '    (`descartar_cola_r2`), y lo que sigue se computa sobre lo que queda."""\n'),
    ('    if r2b:\n'
     '        resumen["fase"] = fase\n'
     '    omisiones: list[dict] = []\n',
     '    if r2b:\n'
     '        resumen["fase"] = fase\n'
     '    resumen["con_cola"] = con_cola\n'
     '    resumen["cola_descartada_por_to"] = {}\n'
     '    omisiones: list[dict] = []\n'),
    ('        regs = RC.entrada_r2(to, C.SALIDA / to, chunks, perfil, validar)\n'
     '        res = E4.resolver_relaciones_r2(regs, cat["indice"], cat["rol_por_to"], versiones)\n',
     '        regs = RC.entrada_r2(to, C.SALIDA / to, chunks, perfil, validar)\n'
     '        regs, descartadas = descartar_cola_r2(regs, con_cola)\n'
     '        resumen["cola_descartada_por_to"][to] = {"n": len(descartadas), "chunks": descartadas}\n'
     '        res = E4.resolver_relaciones_r2(regs, cat["indice"], cat["rol_por_to"], versiones)\n'),
]

T9 = '''def t9():
    print("T9. U-SINCOLA-T0, enmienda 1: con_cola en la cadena r2 (descartar_cola_r2 antes de E2)")
    sys.path.insert(0, str(REPO / "data" / "experiment" / "tanda0" / "code"))
    import ensamblar_tanda0 as ET  # noqa: PLC0415
    M = E4.modulo_modelos_r2()
    cat = E4.catalogo_r2()
    prov = {"to": "cla", "archivo": "a.pdf", "punto": "1.1", "rol_documental": "punto_propio"}

    def ent(lid, tipo, label, desc):
        return {"local_id": lid, "type": tipo, "label": label, "properties": {"descripcion": desc, "tipo": "otra"},
                "provenance": dict(prov)}

    def reg(cid, entidades, relaciones, omisiones, cola=False):
        r = {"chunk_id": cid, "to": "cla", "archivo": "a.pdf", "e0_sha256_completo": "h", "error": None,
             "estado_e3": "cola_humana" if cola else "completo_ok_directo", "origen_crudo": "e1",
             "validacion": {"entidades": entidades, "relaciones": relaciones, "rechazos": [], "omisiones": omisiones}}
        if cola:
            r["cola_humana"] = True
        return r
    # dos partes del mismo punto: la primera aceptada, la segunda en cola; la Obligacion «O» sale en las dos (un nodo
    # con dos procedencias); la Condicion y su condicion_de, solo en la de la cola, igual que sus omisiones
    a = reg("cla::1.1::parte1", [ent("e1", "Obligacion", "O", "d")], [], [])
    b = reg("cla::1.1::parte2", [ent("e1", "Obligacion", "O", "d"), ent("c1", "Condicion", "C", "cuando x")],
            [{"predicate": "condicion_de", "source": "c1", "target": "e1", "punto": "1.1", "indice_crudo": 0,
              "provenance": dict(prov)}], [{"categoria": "deber", "tramo": "t"}], cola=True)
    regs = [a, b]
    ch = [{"id": "cla::1.1::parte1"}, {"id": "cla::1.1::parte2"}]
    con, desc_con = ET.descartar_cola_r2(regs, True)
    sin, desc_sin = ET.descartar_cola_r2(regs, False)
    check("T9a con con_cola=True nada se descarta", con == regs and desc_con == [])
    check("T9b con con_cola=False se descarta la unidad en cola y solo ella",
          [r["chunk_id"] for r in sin] == ["cla::1.1::parte1"] and desc_sin == ["cla::1.1::parte2"])
    e2 = lambda rs: e2_lib.ensamblar_r2(ch, rs, cat["labels"], M.SUJETOS_R2_SET, M.firma_r2, M.TIPOS_ENTIDAD,  # noqa: E731
                                        M.PREDICADOS, [], fase="r2b")
    ens_con, ens_sin = e2(con), e2(sin)
    ob_con = [n for n in ens_con["nodes"] if n["type"] == "Obligacion"]
    ob_sin = [n for n in ens_sin["nodes"] if n["type"] == "Obligacion"]
    chunks_de = lambda o: [p.get("chunk_id") for p in o["provenances"]]  # noqa: E731
    check("T9c con la cola (la salida de hoy): un nodo con dos procedencias, la Condicion y su condicion_de",
          len(ob_con) == 1 and chunks_de(ob_con[0]) == ["cla::1.1::parte1", "cla::1.1::parte2"]
          and sum(1 for n in ens_con["nodes"] if n["type"] == "Condicion") == 1
          and sum(1 for e in ens_con["edges"] if e["relation"] == "condicion_de") == 1,
          f"{len(ob_con)} {chunks_de(ob_con[0]) if ob_con else None} rechazos_e2={len(ens_con['rechazos_e2'])}")
    check("T9d sin la cola, la unidad en cola no aporta nodos ni aristas",
          all("cla::1.1::parte2" not in chunks_de(o) for o in ens_sin["nodes"] + ens_sin["edges"])
          and not any(n["type"] == "Condicion" for n in ens_sin["nodes"])
          and not any(e["relation"] == "condicion_de" for e in ens_sin["edges"]))
    check("T9e sin la cola, el nodo compartido queda solo con la otra procedencia, con el mismo id",
          len(ob_sin) == 1 and ob_sin[0]["id"] == ob_con[0]["id"] and chunks_de(ob_sin[0]) == ["cla::1.1::parte1"])
    om = lambda rs: [o for r in rs for o in (r.get("validacion") or {}).get("omisiones", [])]  # noqa: E731
    check("T9f sin la cola, el registro de omisiones no lleva las suyas", om(sin) == [] and len(om(con)) == 1)
    cola_est = lambda rs: {r["chunk_id"]: r["estado_e3"] for r in rs if r.get("cola_humana")}  # noqa: E731
    g_sin = {"nodes": ens_sin["nodes"], "edges": ens_sin["edges"]}
    g_con = {"nodes": ens_con["nodes"], "edges": ens_con["edges"]}
    rc_sin, rc_con = e2_lib.flaggear_cola_r2(g_sin, cola_est(sin)), e2_lib.flaggear_cola_r2(g_con, cola_est(con))
    check("T9g sin la cola, 0 marcas y aristas_derivadas_de_cola en 0; con la cola, la marca de hoy",
          rc_sin["nodos_marcados"] == 0 and rc_sin["aristas_marcadas"] == 0
          and ET.aristas_derivadas_de_cola(g_sin, set(cola_est(sin)))["aristas"] == 0
          and rc_con["nodos_marcados"] == 2 and rc_con["aristas_marcadas"] == 1,
          f"sin {rc_sin} | con {rc_con}")


'''

R_SELF = [
    ('      sin norma: sigue irresoluble) y el contador del punto d (la autocita del\n'
     '      encabezado de sección, contada aparte y fuera del registro).\n'
     'Escribe solo en un directorio temporal (TMPDIR). USD 0.\n',
     '      sin norma: sigue irresoluble) y el contador del punto d (la autocita del\n'
     '      encabezado de sección, contada aparte y fuera del registro);\n'
     '  T9  U-SINCOLA-T0, enmienda 1 (06/10/2026): `con_cola` en la cadena r2\n'
     '      (`descartar_cola_r2` antes de E2): con False, la unidad en cola no\n'
     '      aporta nodos ni aristas, el nodo compartido queda solo con la otra\n'
     '      procedencia y el registro de omisiones no lleva las suyas; con True, la\n'
     '      salida de hoy.\n'
     'Escribe solo en un directorio temporal (TMPDIR). USD 0.\n'),
    ('def main() -> int:\n    t1()\n', T9 + 'def main() -> int:\n    t1()\n'),
    ('    t8()\n    ok = sum(1 for _, b, _ in RES if b)\n', '    t8()\n    t9()\n    ok = sum(1 for _, b, _ in RES if b)\n'),
]

NOTA_F15 = ('- **F15. Parámetro `con_cola` de la cadena r2 (U-SINCOLA-T0, enmienda 1 al mandato, 06/10/2026).**\n'
            '  `ensamblar_tanda0.py --sin-cola` llega ahora también a la cadena r2: `correr_cadena_r2` descarta, en un\n'
            '  único punto y después de `entrada_r2`, los registros de la cola humana (`descartar_cola_r2`), y lo que\n'
            '  sigue (omisiones, paso por E3, marca de la cola, aristas derivadas que tocan la cola) se computa sobre lo\n'
            '  que queda; el reporte del ensamblado declara `con_cola` y las unidades descartadas por TO. Es solo código\n'
            '  sobre lo guardado: no toca el request de E1 ni el de E3, así que no mueve ninguna clave de la caché\n'
            '  (`selftest_clave_cache` sigue en verde, A1r y A3r OK). Sin la bandera, la salida es la de siempre: los dos\n'
            '  r2b sellados, byte a byte.\n')
R_TABLA = [('- **F18a.**', NOTA_F15 + '- **F18a.**')]


def aplicar(p: Path, reemplazos: list[tuple[str, str]]) -> None:
    s = p.read_text(encoding="utf-8")
    for viejo, nuevo in reemplazos:
        n = s.count(viejo)
        assert n == 1, f"{p.name}: el texto viejo aparece {n} veces (se esperaba 1): {viejo[:80]!r}"
        s = s.replace(viejo, nuevo)
    p.write_text(s, encoding="utf-8")
    print(f"parcheado: {p.relative_to(RAIZ)} ({len(reemplazos)} reemplazos)")


aplicar(ENS, R_ENS)
aplicar(SELF, R_SELF)
aplicar(TABLA, R_TABLA)
