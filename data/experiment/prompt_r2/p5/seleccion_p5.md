# Selección de P5 de U-PROMPT-R2, sellada antes de correr

Sello: `p5/salida/seleccion_p5.json`, sha256 `a5640ffcfa9946202eaf6959be2878a6698cea4d125daf9289367b8519699502`,
tomado el 05/10/2026 a las 10:25:30 (-0300), antes de la primera llamada de la medición. La genera
`p5/seleccion_p5.py` (sha256 `57f3ee62…`), con la semilla `U-PROMPT-R2:P5:2026-10-05`:

```bash
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -B data/experiment/prompt_r2/p5/seleccion_p5.py --salida DIR
```

**E1, dos corridas:** las 27 unidades de P4b (`p4b/salida/seleccion_p4b.json`, sha256 `e2551cf3…`), en su orden y con
su grupo.

**E3, dos corridas sobre la salida de E1 de la corrida a: 10 unidades.**
- Las 5 de la pata de E3 de P4b: `ctacte::3.2::intro`, `ext::3.5.3::intro`, `cla::5.1.1::intro`, `ext::13.1.4` y
  `ext::6.1.1`.
- 5 más, por regla:
  - fijas, el ítem del ejemplo y la unidad de f, que tienen lectura propia en P4b y ninguna verificación de E3:
    `cla::5.1.1.1` y `cap::6.2.2.6`;
  - una de cada grupo c, d y e, que no tienen ninguna en la pata, sorteada con
    `random.Random(f"{SEMILLA}:e3:{grupo}").choice` sobre sus unidades en el orden de P4b: `cap::5.3.1.3` (c),
    `cap::10.2.2.4` (d) y `polcre::5.3` (e).
- Los ítems de b1 y b2 no suman ninguna: la pata ya trae sus dos encabezados.

**Reintento por salida mal formada, forzado con temperatura 1:** `ctacte::3.2.4`, la unidad más corta de las 27 por
texto propio (la regla de la llamada del tercer escalón de P4b).
