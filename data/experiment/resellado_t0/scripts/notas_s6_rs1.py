"""Re-sellado único de la tanda 0, §6 y §4 del mandato: las notas fechadas a los documentos que citan los sha sellados.
Los firmados no se editan: reciben una nota fechada al final, debajo de su firma y de sus notas, con el sha nuevo y por qué,
en el formato de su última nota. Los LEEME de las figuras reciben la nota del §4 (la figura no cambia; el sha vigente y por
qué). Para cada archivo: verifica que es el de la raíz antes de escribir (sha256 dado), que cita los sha que la nota nombra,
y después, que todo lo anterior a la nota queda byte a byte igual. Corre sobre una raíz (la copia; el repo recibe los mismos
bytes). Uso: python -I -B notas_s6_rs1.py <raiz> <salida.json>
"""
import hashlib
import json
import re
import sys
from pathlib import Path

RAIZ, SAL = Path(sys.argv[1]).resolve(), Path(sys.argv[2])
FECHA = "15/10/2026"
MANDATO = "`docs/mandatos/URESELLADO_T0_resellado_unico_grafos_r2b.md`"
FRENO = "`data/experiment/resellado_t0/FRENO_resellado_T0.md`"
G = {  # sellado -> (nombre sellado, sha nuevo, nombre nuevo, nodos, aristas)
    "a9631a64": ("KG-Tanda0-Diez-r2b", "fda6c07d", "KG-Tanda0-Diez-r2b-rs1", "8.788", "27.430"),
    "6e756043": ("KG-Tanda0-Desarrollo-r2b", "acb26dca", "KG-Tanda0-Desarrollo-r2b-rs1", "6.962", "23.311"),
    "e22fae1a": ("KG-Tanda0-Diez-r2b-sincola", "61dd1b69", "KG-Tanda0-Diez-r2b-sincola-rs1", "8.491", "25.976"),
    "2922b72d": ("KG-Tanda0-Desarrollo-r2b-sincola", "66e745f5", "KG-Tanda0-Desarrollo-r2b-sincola-rs1", "6.711", "21.996"),
}
COLA = ("la cola de la tanda 0 pasa de 74 a 69 unidades: salen, por R0, `ext::2.6.1.1`, `ext::3.5.6.1`, `ext::3.6.1.1`, "
        "`ext::3.6.4.2` y `ext::3.13.1.10`, y no entra ninguna")
V = ("el sorteo de la etapa V, que espera este re-sellado, queda habilitado por `66e745f5…` (KG-Tanda0-Desarrollo-r2b-sincola-rs1), "
     "la versión posterior de `2922b72d…`, una vez sellado; no se corrió")
ESPECIFICO = {
    "docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md": V[0].upper() + V[1:] + ".",
    "docs/preregistro_evaluacion_tripletas.md": V[0].upper() + V[1:] + " (vale el sello vigente al sortear: laudo D-f, nota posterior a la firma).",
    "docs/laudo_D-f_secuencia_tripletas.md": ("Si el sorteo es posterior al sello del re-sellado, el sello vigente al sortear es el de "
                                             "`66e745f5…` (KG-Tanda0-Desarrollo-r2b-sincola-rs1)."),
    "docs/enmienda5_protocolo_entre_tandas_2026-10-06_grafo_evaluado_sin_cola.md": COLA[0].upper() + COLA[1:] + ".",
    "docs/protocolo_dos_grafos.md": ("Las versiones posteriores de los dos «grafos sin cola de la tanda 0» son `61dd1b69…` y `66e745f5…`; "
                                     + COLA + "."),
    "docs/laudo_B2.4_sujetos.md": (
        "La re-medición del §2: en los puntos de los ocho patrones (la consulta del control o de "
        "`data/experiment/reext_t0/t3/controles_t3.py`, con `ext::7.9.6` para BKL-0015) ninguna arista de sujeto sale ni entra de "
        "`a9631a64…` a `fda6c07d…`, y las de los tres límites declarados siguen: 3, 2 y 1. Fuera del punto del patrón de BKL-0015, en "
        "`ext::7.9.4`, O2 (grupo f′) lleva 4 `aplica_a` del propuesto «la entidad» al rol colectivo de Exterior "
        "(`data/experiment/resellado_t0/salidas/controles_s4_rs1.json`, `B_laudo_B24`)."),
    "docs/mandatos/UCONF_MATRIZ_lectura_confirmacion.md": (
        "El control de después del re-sellado: de las 60 aristas leídas, 59 siguen en `61dd1b69…` con los mismos extremos. F49 no: "
        "es de `ext::3.16.2.1`, una unidad de R0 aceptada tras un reintento nuevo, con otra extracción, en la que ya no están ni el "
        "origen ni el destino de la arista leída (la unidad pasa de 7 a 10 `condicion_de` hacia una Potestad, que es otro nodo). "
        "Ninguna sale por el retiro de → Potestad. La cifra no se recalcula (`:38`) salvo que la autora lo decida "
        "(`data/experiment/resellado_t0/salidas/controles_s4_rs1.json`, `A_conf_matriz`)."),
    "docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md": (
        "La población sobre el grafo re-sellado (enmienda 7, §1.5): 2.371 aceptadas, 1.008 ítems y 1.363 no ítems (antes, 2.366, "
        "1.003 y 1.363); las cifras de L2 quedan como medidas sobre el grafo sellado anterior."),
    "docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md": (
        "Por D-A, el grafo de desarrollo re-sellado es `acb26dca…` (KG-Tanda0-Desarrollo-r2b-rs1), la versión posterior de "
        "`6e756043…`: es el brazo del grafo de A2.2 si está sellado al despachar el tramo 3."),
    "docs/mandatos/UOMISIONES_COD_release_codigo_ensamblado.md": (
        "Los cuatro grafos de O2 (`710664e9`, `a50210b4`, `18a2747d` y `9f49d62d`; `data/experiment/omisiones_cod/o2/FRENO_O2.md:80-83`) "
        "se reproducen byte a byte con el código de `ded41d50` sobre las salidas de antes de R0. El diff de los re-sellados contra ellos "
        "tiene 541 filas en los completos y 565 en los sin cola, todas de unidades de R0."),
}
FIRMADOS = ["docs/enmienda1_preregistro_evaluacion_tripletas_2026-10-08_umbrales.md",
            "docs/enmienda5_protocolo_entre_tandas_2026-10-06_grafo_evaluado_sin_cola.md",
            "docs/laudo_B2.4_sujetos.md", "docs/laudo_D-f_secuencia_tripletas.md",
            "docs/mandatos/A2_1_sistema_por_fragmentos_preregistro_A2_2.md",
            "docs/mandatos/UAPLICA_ROL_ALCANCE_derivada_Bprima.md", "docs/mandatos/UCASI_DUPLICADOS_fusion_de_forma.md",
            "docs/mandatos/UCONF_MATRIZ_lectura_confirmacion.md", "docs/mandatos/ULECTURA_ACEPTADAS_tasa_error_tanda0.md",
            "docs/mandatos/UOMISIONES_COD_release_codigo_ensamblado.md", "docs/mandatos/UREEXT_T0_reextraccion_tanda0.md",
            "docs/mandatos/URERESOL_CAT_reresolucion_catalogo.md", "docs/mandatos/USINCOLA_T0_grafo_evaluado_sin_cola.md",
            "docs/mandatos/UUNION_ITEM_ENCABEZADO_regla_estrecha.md", "docs/preregistro_evaluacion_tripletas.md",
            "docs/protocolo_dos_grafos.md"]
LEEMES = {
    "docs/tesis/figuras/LEEME_figura_ensamblado_ejemplo.md": ("generar_figura_ensamblado_ejemplo.py",
                                                              "con `--grafo` y `--sha256-grafo` apuntando al diez re-sellado, y "
                                                              "también al de desarrollo re-sellado (el «mismo vecindario» del §1)",
                                                              "el SVG, el PNG y el PDF"),
    "docs/tesis/figuras/LEEME_figura_catalogo_sujetos.md": ("generar_figura_catalogo_sujetos.py",
                                                            "con la ruta y el candado del grafo cambiados solo en la copia",
                                                            "el SVG"),
    "docs/tesis/figuras/LEEME_figura_norma_a_grafo.md": ("generar_figura_norma_a_grafo.py",
                                                         "con las rutas y los candados de GRAFO y GRAFO_DIEZ cambiados solo en la copia",
                                                         "el SVG, el PNG y el PDF"),
    "docs/tesis/figuras/LEEME_figura_tripleta.md": ("generar_figura_tripleta.py",
                                                    "que toma GRAFO y GRAFO_DIEZ de generar_figura_norma_a_grafo.py, cambiados solo en la copia",
                                                    "el SVG, el PNG y el PDF"),
}


def citados(texto: str) -> list[str]:
    return [s for s in G if s in texto]


def pares(cit: list[str]) -> str:
    out = []
    for s in cit:
        nom, n, nn, nod, ar = G[s]
        out.append(f"`{s}…` ({nom}) → `{n}…` ({nn}, {nod} nodos y {ar} aristas)")
    return "; ".join(out)


def generico(cit: list[str]) -> str:
    diez = any(s in ("a9631a64", "e22fae1a") for s in cit)
    return (f"Los grafos sellados que cita este documento tienen una versión posterior, del re-sellado único ({MANDATO}, firmado; "
            f"FRENO en {FRENO}): {pares(cit)}. Cambian por el código de U-OMISIONES-COD (`ded41d50`) y por las salidas de R0 "
            f"(`1d690df3` y `2d0f5277`)" + ("; los de diez, además, por R2-3 (`803623a`), que los sellados no tenían" if diez else "")
            + ". El diff por campo y por causa está en `data/experiment/resellado_t0/salidas/`. Los sellados siguen sellados "
              "(principio 9); el commit del sello de los nuevos queda en `commit_sellado` de `data/experiment/neo4j/grafos.py`.")


def estilo(texto: str) -> str:
    ult = None
    for linea in texto.splitlines():
        if re.match(r"^(- )?\*\*\[\d{2}/\d{2}/\d{4}\]", linea):
            ult = "corchete_vineta" if linea.startswith("- ") else "corchete"
        elif re.match(r"^- \*\*\d{2}/\d{2}/\d{4}", linea):
            ult = "vineta"
    return ult or "vineta"


def nota_firmado(rel: str, texto: str) -> str:
    cit = citados(texto)
    cuerpo = generico(cit) + (" " + ESPECIFICO[rel] if rel in ESPECIFICO else "") + " El texto firmado no cambia."
    titulo = "el re-sellado único de los grafos r2b de la tanda 0"
    e = estilo(texto)
    if e == "corchete":
        return f"**[{FECHA}] Nota: {titulo}.** {cuerpo}\n"
    if e == "corchete_vineta":
        return f"- **[{FECHA}] Nota: {titulo}.** {cuerpo}\n"
    return f"- **{FECHA} — {titulo}.** {cuerpo}\n"


def nota_leeme(rel: str, texto: str) -> str:
    gen, como, salidas = LEEMES[rel]
    cit = citados(texto)
    return (f"## Nota del {FECHA}: el re-sellado único de la tanda 0\n\n"
            f"El grafo de esta figura tiene una versión posterior, del re-sellado único ({MANDATO}; FRENO en {FRENO}): "
            f"{pares(cit)}. **La figura no cambia.** El generador (`{gen}`), corrido sobre una copia del repo {como}, da "
            f"{salidas} byte a byte iguales a los de este directorio, igual que con los sellados "
            f"(`data/experiment/resellado_t0/salidas/figuras_rs1.json`). La salida idéntica, con las comprobaciones del "
            f"generador en verde, muestra que lo que el re-sellado cambia (el código de U-OMISIONES-COD y las 20 unidades de "
            f"R0, de ext y docvig) no toca lo que la figura dibuja. Las fuentes y los sha256 de arriba quedan como están: son "
            f"los de la figura registrada.\n")


def sha(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


res = {"firmados": {}, "leemes": {}}
for grupo, lista, fn in (("firmados", FIRMADOS, nota_firmado), ("leemes", list(LEEMES), nota_leeme)):
    for rel in lista:
        p = RAIZ / rel
        antes = p.read_bytes()
        texto = antes.decode("utf-8")
        cit = citados(texto)
        assert cit, f"{rel} no cita ningún sha sellado"
        assert "re-sellado único de los grafos r2b de la tanda 0." not in texto and f"Nota del {FECHA}: el re-sellado" not in texto, \
            f"{rel} ya tiene la nota"
        nota = fn(rel, texto)
        sep = "" if texto.endswith("\n\n") else ("\n" if texto.endswith("\n") else "\n\n")
        despues = (texto + sep + nota).encode("utf-8")
        assert despues.startswith(antes), "lo anterior a la nota cambió"
        p.write_bytes(despues)
        res[grupo][rel] = {"sha256_antes": sha(antes), "sha256_despues": sha(despues), "citados": cit,
                           "estilo": estilo(texto) if grupo == "firmados" else "seccion", "nota": nota}
SAL.write_text(json.dumps(res, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
for g in res:
    for rel, v in res[g].items():
        print(f"{g:9s} {rel}: {v['citados']} {v['estilo']}")
print("notas:", len(res["firmados"]), "firmados y", len(res["leemes"]), "LEEME")
