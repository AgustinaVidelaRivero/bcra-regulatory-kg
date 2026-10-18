"""Mesa, §158: la prueba del sello derivado con los controles reales del juez (`controles_de_corrida` de `juez/juez_desamb_mesa.py`,
importado desde un clon de HEAD, no desde el repo). Con el sello derivado, ninguno de los dos controles del sello de la lectura falla; con
una hora posterior al límite, falla el del límite; sin el archivo, falla el de la falta. Los demás controles (autorización, calibradores,
tanda final) fallan en los tres casos, porque esta prueba no los arma: se declara. No hace ninguna llamada. USD 0.
Uso: python3 -I -B probar_sello_con_el_juez_mesa.py <clon> <sello_cierre_para_el_juez.json> <salida.txt>"""
import argparse
import importlib.util
import json
import sys
import tempfile
from pathlib import Path

CL, SELLO, OUT = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
F = CL / "data/experiment/med_desamb/juez/juez_desamb_mesa.py"
spec = importlib.util.spec_from_file_location("juez_desamb_mesa", F)
J = importlib.util.module_from_spec(spec)
spec.loader.exec_module(J)
assert Path(J.__file__).resolve().is_relative_to(CL)
FALTA, TARDE = "falta el sello del cierre de la lectura de la autora", "la lectura de la autora cerró después del miércoles"
sal, mal = [], 0
with tempfile.TemporaryDirectory(prefix="sello_juez_") as t:
    T = Path(t)
    tarde = T / "tarde.json"
    tarde.write_text(json.dumps({**json.loads(SELLO.read_text(encoding="utf-8")), "sellado": "2026-10-21 18:00:01 -0300"}), encoding="utf-8")
    casos = [("el sello derivado", SELLO, set()), ("una hora posterior al límite", tarde, {TARDE}), ("sin el archivo", T / "no_esta.json", {FALTA})]
    for nombre, ruta, esperado in casos:
        a = argparse.Namespace(salida=str(T / "salida"), autorizacion=None, sello_lectura=str(ruta), sello_tanda_final=None, repo=str(CL))
        falla = J.controles_de_corrida(a, ps="")
        del_sello = {m for m in (FALTA, TARDE) if any(f.startswith(m) for f in falla)}
        bien = del_sello == esperado
        mal += not bien
        sal.append(f"{'OK ' if bien else 'MAL'} {nombre}: controles del sello que fallan {sorted(del_sello) or 'ninguno'}; "
                   f"los demás que fallan (esta prueba no los arma): {len(falla) - len(del_sello)}")
sal.append(f"RESULTADO: {'PASA' if not mal else 'MAL'} ({len(casos) - mal} de {len(casos)})")
OUT.write_text("\n".join(sal) + "\n", encoding="utf-8")
print("\n".join(sal))
sys.exit(1 if mal else 0)
