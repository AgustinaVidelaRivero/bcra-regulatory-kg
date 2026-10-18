"""B6.1, tanda 1, T3 (desde el punto 4): copia un archivo o una carpeta de salidas del scratchpad a un destino (la copia del repo o el
staging), con las rutas reemplazadas en los archivos de texto: el scratchpad por <SCRATCHPAD> y la carpeta personal por $HOME. Frena si
el destino ya existe o si queda una ruta absoluta del scratchpad o de la carpeta personal. Los binarios van tal cual.
Uso: python3 -I -B poner_saneado_t3f.py <scratchpad> <origen> <destino>
"""
import sys
from pathlib import Path

SCR, ORIG, DEST = Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), Path(sys.argv[3])
HOME = str(Path.home())
if DEST.exists():
    raise SystemExit(f"FRENO: {DEST} ya existe")
pares = [(ORIG, DEST)] if ORIG.is_file() else [(p, DEST / p.relative_to(ORIG)) for p in sorted(ORIG.rglob("*")) if p.is_file()]
n_txt = n_bin = 0
for o, d in pares:
    d.parent.mkdir(parents=True, exist_ok=True)
    b = o.read_bytes()
    try:
        t = b.decode("utf-8")
    except UnicodeDecodeError:
        d.write_bytes(b); n_bin += 1
        continue
    t = t.replace(str(SCR), "<SCRATCHPAD>").replace(HOME, "$HOME")
    if "/private/tmp" in t or "/Users/" in t:
        raise SystemExit(f"FRENO: queda una ruta absoluta en {o}")
    d.write_text(t, encoding="utf-8"); n_txt += 1
print(f"{len(pares)} archivos: {n_txt} de texto saneados, {n_bin} binarios tal cual → {DEST}")
