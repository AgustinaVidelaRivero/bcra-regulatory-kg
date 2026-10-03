"""U-MED-R2A, M1.e — entrada r2 de la fixture de la suite, PROPUESTA y sin sellar.

Reescribe en scripts/regression_kg_esperado.json solo la clave `propuesta_r2_sin_sellar`, que pasa a describir
KG-Tanda0-Diez-r2a con los estados de los 56 ítems medidos por la suite del perfil r2 (M1.c). La propuesta
anterior (KG-Prueba-r2-desarrollo, U-R2-CODIGO) describía un grafo fuera del repo; ese grafo es hoy
KG-Tanda0-Desarrollo-r2a (mismo sha, M1.b). `estado_esperado` y `linea_de_base_observada` no se tocan: el script
comprueba que su sha canónico no cambia y que el resto del archivo sale idéntico. Sellar la entrada (moverla a
`estado_esperado`) es una acción de la autora (decisión 4 del mandato).

Uso, desde la raíz del repo:
  PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/medicion_r2a/m1e_propuesta_r2a.py \
      scripts/regression_kg_esperado.json data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/suite_perfil_r2.json
Sin --escribir solo muestra lo que cambiaría.
"""
import hashlib
import json
import sys
from collections import OrderedDict
from pathlib import Path

NOMBRE = "KG-Tanda0-Diez-r2a"
KG = "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a/r2/kg.json"
COMANDO_KG = ("data/experiment/tanda0/code/ensamblar_tanda0.py --manifiesto "
              "data/experiment/reextraccion_v2/manifiestos/tanda0_ens_diez.json --entrada "
              "data/experiment/reextraccion_v2/corpus_tanda0/salida_dirigida --perfil-r2 --e0-r2 "
              "data/experiment/reextraccion_v2/e0_chunking/salida_tanda0_r2 --salida "
              "data/experiment/reextraccion_v2/corpus_tanda0/ens_diez_r2a")

fixture, suite_json = Path(sys.argv[1]), Path(sys.argv[2])
escribir = "--escribir" in sys.argv
crudo = fixture.read_text(encoding="utf-8")
fx = json.loads(crudo, object_pairs_hook=OrderedDict)
assert json.dumps(fx, ensure_ascii=False, indent=1) + "\n" == crudo, "la fixture no hace round-trip"


def sha(o):
    return hashlib.sha256(json.dumps(o, ensure_ascii=False, sort_keys=True).encode("utf-8")).hexdigest()


antes = {k: sha(v) for k, v in fx.items() if k != "propuesta_r2_sin_sellar"}
vieja = fx["propuesta_r2_sin_sellar"]
s = json.loads(suite_json.read_text(encoding="utf-8"))
p = s["parametros"]
assert p["kg"] == KG and p["perfil"] == "r2", (p["kg"], p["perfil"])
assert hashlib.sha256(Path(KG).read_bytes()).hexdigest() == p["kg_sha256"], "el kg del repo no es el de la corrida"
assert len(s["items"]) == 56, len(s["items"])
entrada = OrderedDict()
entrada["_rotulo"] = (
    "PROPUESTA, SIN SELLAR (U-MED-R2A, M1.e; decisión 4 del mandato docs/mandatos/UMED_R2A_medicion_r2a.md): "
    "estados medidos sobre KG-Tanda0-Diez-r2a, el grafo de la medición r2a de los diez TOs de la tanda 0. Va "
    "fuera de estado_esperado y de linea_de_base_observada, así que la suite no la lee: no computa regresión ni "
    "cambia el sha del subárbol sellado. Para sellarla, la autora la mueve a estado_esperado (PENDIENTE). "
    "Reemplaza la propuesta KG-Prueba-r2-desarrollo de U-R2-CODIGO (kg 93a7af72…, fuera del repo; hoy versionado "
    "como KG-Tanda0-Desarrollo-r2a en data/experiment/reextraccion_v2/corpus_tanda0/ens_desarrollo_r2a/r2/kg.json).")
entrada["kg"] = KG
entrada["kg_comando"] = COMANDO_KG
entrada["kg_sha256"] = p["kg_sha256"]
for k in ("generacion", "politica_cuarentena", "catalogo", "catalogo_sha256", "perfil"):
    entrada[k] = p[k]
entrada["evidencia"] = (f"{suite_json.as_posix()} (scripts/regression_kg.py --kg {KG} --perfil r2 --generacion 3 "
                        f"--catalogo {p['catalogo']} --politica-cuarentena flaggeada --esperado "
                        f"scripts/regression_kg_esperado.json), resumen {s['resumen']}")
entrada["items"] = OrderedDict((it["id"], {"estado": it["estado"]}) for it in s["items"])
# T6 y E4-b: el test fija el conjunto de TOs en los cinco de desarrollo (r1_comun.TOS_ORDEN), así que sobre un
# grafo de diez TOs dan «persiste» por construcción. Se anota para la decisión de sellado; el estado no se cambia.
NOTA_TOS = ("persiste por construcción del test, no por un defecto del grafo: T6 exige exactamente 5 TextoOrdenado con "
            "los ids de r1_comun.TOS_ORDEN, los cinco TOs de desarrollo (scripts/regression_kg.py:1306-1313 y "
            ":547-552; data/experiment/reextraccion_v2/corpus_v2/r1_comun.py:38), y KG-Tanda0-Diez-r2a tiene 10, uno por TO; los 5 fuera del esperado son los de ctacte, docvig, "
            "lingob, pagjub y polcre, y no falta ninguno. Si se sella así o se adapta el test, lo decide la autora.")
for k in ("T6", "E4-b"):
    if entrada["items"][k]["estado"] == "persiste":
        entrada["items"][k]["nota"] = NOTA_TOS + (" E4-b depende de T6 (:1506-1515)." if k == "E4-b" else "")
previa = next(iter(vieja.values()))["items"] if vieja else {}
cambian = {k: [previa.get(k, {}).get("estado"), v["estado"]] for k, v in entrada["items"].items()
           if previa.get(k, {}).get("estado") != v["estado"]}
fx["propuesta_r2_sin_sellar"] = OrderedDict([(NOMBRE, entrada)])
nuevo = json.dumps(fx, ensure_ascii=False, indent=1) + "\n"
fx2 = json.loads(nuevo, object_pairs_hook=OrderedDict)
despues = {k: sha(v) for k, v in fx2.items() if k != "propuesta_r2_sin_sellar"}
assert antes == despues, "cambió algo fuera de propuesta_r2_sin_sellar"
assert list(fx2) == list(json.loads(crudo, object_pairs_hook=OrderedDict)), "cambió el orden de las claves"
print("claves fuera de la propuesta sin cambios (sha canónico):", json.dumps(despues, ensure_ascii=False))
print("propuesta anterior:", list(vieja), "→", NOMBRE, entrada["kg_sha256"])
print("ítems que cambian contra la propuesta anterior (prueba r2 de desarrollo):", json.dumps(cambian, ensure_ascii=False))
print("resumen:", s["resumen"])
if escribir:
    fixture.write_text(nuevo, encoding="utf-8")
    print("escrito:", fixture, hashlib.sha256(nuevo.encode("utf-8")).hexdigest())
else:
    print("sin --escribir: no se escribió nada; sha256 que tendría la fixture:", hashlib.sha256(nuevo.encode("utf-8")).hexdigest())
