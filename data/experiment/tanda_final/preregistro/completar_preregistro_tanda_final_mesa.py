"""Completa los huecos `⟦id⟧` del pre-registro de la tanda final desde sus fuentes (mesa, §155, 18/10/2026; v3 de la §163: los momentos,
el sha256 del JSON de huecos y las cifras con las que corre la tanda).

- Lee el pre-registro y `huecos_preregistro_tanda_final.json`. Cada hueco tiene su `momento`: T1 (antes de T1 del despacho),
  lectura_tramo1 (antes de la primera lectura del tramo 1) o T5 (antes del FRENO T5 de la tanda final).
- **Con `--momento M`,** completa los huecos de M y de los momentos anteriores, y deja los posteriores como `⟦id⟧`. Para cada uno lee su
  fuente:
  - una ruta del repo, con `git show <commit>:<ruta>` (HEAD si el hueco no tiene `commit`), nunca desde el árbol;
  - o, con «paquete:», una ruta del paquete de la mesa (segundo argumento).
- **Frena sin escribir** si un hueco del texto no está en el JSON o no tiene momento; si un hueco que toca tiene la fuente, el commit o la
  clave en «PENDIENTE»; si la fuente no existe o la clave o la regex no dan nada; o si queda un hueco que tocaba.
- **La versión derivada** es el texto con los huecos completados y una sección final: el momento, el sha256 del pre-registro y del JSON
  de huecos que usó, los huecos que esperan a un momento posterior y las cifras con las que corre la tanda (`_cifras_derivadas`, la
  salida de `cifras_preregistro_tanda_final_mesa.py`, con `--sin` si salió un documento). Va con un JSON con el valor, la fuente y el
  sha256 de la fuente de cada hueco. El texto firmado no cambia.
- USD 0. Solo lee el repo.
Uso: python3 -I -B completar_preregistro_tanda_final_mesa.py <pre-registro.md> <paquete H> <huecos.json> <salida.md> --momento M
     [--repo <ruta>]"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

MOMENTOS = ["T1", "lectura_tramo1", "T5"]
argv = sys.argv[1:]
opc = {}
for k in ("--repo", "--momento"):
    if k in argv:
        i = argv.index(k)
        opc[k] = argv[i + 1]
        del argv[i:i + 2]
repo = Path(opc.get("--repo", Path.home() / "INGENIERIA IA/TESIS/bcra-regulatory-kg"))
if opc.get("--momento") not in MOMENTOS:
    raise SystemExit(f"FRENO: --momento tiene que ser uno de {MOMENTOS}")
HASTA = MOMENTOS.index(opc["--momento"])
PRE, PAQ, HJ, OUT = Path(argv[0]), Path(argv[1]), Path(argv[2]), Path(argv[3])
HUECO = re.compile(r"⟦([A-Za-z0-9_.]+)⟧")
texto = PRE.read_text(encoding="utf-8")
hj_bytes = HJ.read_bytes()
huecos = json.loads(hj_bytes)
sha = lambda b: hashlib.sha256(b).hexdigest()  # noqa: E731


def frenar(m):
    raise SystemExit(f"FRENO: {m}")


def toca(h: dict, hid: str) -> bool:
    if h.get("momento") not in MOMENTOS:
        frenar(f"el hueco {hid} no tiene un momento válido")
    return MOMENTOS.index(h["momento"]) <= HASTA


def fuente_bytes(h: dict) -> tuple[bytes, str]:
    f = h["fuente"]
    if f.startswith("PENDIENTE") or str(h.get("commit", "")).startswith("PENDIENTE"):
        frenar(f"fuente o commit PENDIENTE: {f} / {h.get('commit')}")
    if f.startswith("paquete:"):
        p = PAQ / f.split(":", 1)[1].strip()
        if not p.exists():
            frenar(f"no existe en el paquete: {p}")
        return p.read_bytes(), f
    c = h.get("commit", "HEAD")
    r = subprocess.run(["git", "--no-optional-locks", "-C", str(repo), "show", f"{c}:{f}"], capture_output=True)
    if r.returncode != 0:
        frenar(f"no existe en {c}: {f}")
    return r.stdout, f"{c}:{f}"


valores, esperan = {}, []
for hid in sorted(set(HUECO.findall(texto))):
    if hid not in huecos:
        frenar(f"el hueco {hid} no está en {HJ.name}")
    h = huecos[hid]
    if not toca(h, hid):
        esperan.append(f"{hid} ({h['momento']})")
        continue
    b, donde = fuente_bytes(h)
    if h["tipo"] == "json":
        if str(h.get("clave", "")).startswith("PENDIENTE"):
            frenar(f"clave PENDIENTE en {hid}")
        v = json.loads(b)
        for k in h["clave"].split("/"):
            if not isinstance(v, dict) or k not in v:
                frenar(f"{hid}: la clave {h['clave']} no está en {donde}")
            v = v[k]
        valor = v if isinstance(v, str) else json.dumps(v, ensure_ascii=False)
    elif h["tipo"] == "regex":
        m = re.search(h["regex"], b.decode("utf-8"))
        if not m:
            frenar(f"{hid}: la regex no da nada en {donde}")
        valor = m.group(1)
    elif h["tipo"] == "texto":
        valor = b.decode("utf-8").strip()
    else:
        frenar(f"{hid}: tipo desconocido {h['tipo']}")
    valores[hid] = {"valor": valor, "fuente": donde, "fuente_sha256": sha(b), "momento": h["momento"]}
out = HUECO.sub(lambda m: valores[m.group(1)]["valor"] if m.group(1) in valores else m.group(0), texto)
quedan = {x for x in HUECO.findall(out) if toca(huecos[x], x)}
if quedan:
    frenar(f"quedaron huecos que tocaban: {sorted(quedan)}")
cif = huecos.get("_cifras_derivadas")
if cif is None or not toca(cif, "_cifras_derivadas"):
    frenar("falta _cifras_derivadas en el JSON de huecos")
cb, cdonde = fuente_bytes(cif)
c = json.loads(cb)
co, tr, ba = c["costo"], c["tramos"], c["bases_control_entre_tramos"]
seccion = ["", "## Versión derivada (la escribe el script; no es parte del texto firmado)", "",
           f"- **El momento:** {opc['--momento']}.",
           f"- **El pre-registro:** sha256 `{sha(PRE.read_bytes())}`. **El JSON de huecos que usé:** sha256 `{sha(hj_bytes)}`.",
           f"- **Los huecos completados:** {len(valores)}. **Los que esperan a un momento posterior:** {', '.join(esperan) or 'ninguno'}.",
           f"- **Las cifras con las que corre la tanda** (`{cdonde}`, sha256 `{sha(cb)}`). Mandan sobre las del texto:",
           f"  - documentos fuera: {', '.join(c.get('documentos_fuera') or []) or 'ninguno'};",
           f"  - {c['alcance_s2c']['tos']} TOs y U = {co['U']} unidades; el estimado, USD {co['estimado']}; el tope, USD {co['tope']};",
           f"  - el tramo 1, {tr['tramo_1']['tos']} TOs y {tr['tramo_1']['unidades']} unidades; el tramo 2, {tr['tramo_2']['tos']} TOs y "
           f"{tr['tramo_2']['unidades']} unidades;",
           f"  - las bases del control entre tramos: el costo por unidad {ba['base_costo_por_unidad']} (umbral {ba['umbral_costo_por_unidad_1_3']}), "
           f"la cola {ba['base_proporcion_cola']} (umbral {ba['umbral_proporcion_cola_1_5']})."]
OUT.write_text(out.rstrip("\n") + "\n" + "\n".join(seccion) + "\n", encoding="utf-8")
OUT.with_suffix(".huecos.json").write_text(json.dumps({"momento": opc["--momento"], "huecos_json_sha256": sha(hj_bytes),
                                                       "cifras": {"fuente": cdonde, "sha256": sha(cb)}, "valores": valores,
                                                       "esperan": esperan}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print(f"completo hasta {opc['--momento']}: {len(valores)} huecos; esperan {len(esperan)}; {OUT.name} sha256 {sha(OUT.read_bytes())}")
