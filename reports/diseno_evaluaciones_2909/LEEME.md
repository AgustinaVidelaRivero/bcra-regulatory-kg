# LEEME — reports/diseno_evaluaciones_2909/ (U-DISENO-EVAL, 29/09/2026)

Unidad de solo lectura sobre HEAD `8e0597c`; no se commitea (la autora
commitea con rutas explícitas). Archivos:

| Archivo | sha256 | Qué es |
|---|---|---|
| `fichas.md` | `14e3b1e00eff3be42c190123add14b1326ebd6ea27f6704091e2ab00a5709d1a` | Estado de H1 a H13 con fuente (9 en (a), 4 en (b)), respuestas Q1 a Q6 con evidencia, contradicciones C-1 a C-7, decisiones fuera de la lista, propuestas F-1 a F-6 y comandos de recuento |
| `bloques_comentarios.tex` | `a265ce224831961e23df0ad6d7e7ba865b1e753b8148eca79b69da41307017d8` | Siete bloques de comentarios LaTeX (4.7, 5.1, 5.2, 5.3, 5.4, 5.5 y 6.4), todas las líneas con `%` |
| `LEEME.md` | (este archivo; su sha no se autodeclara) | Índice |

Verificación del criterio 2:
`grep -vn '^%' reports/diseno_evaluaciones_2909/bloques_comentarios.tex | grep -v '^[0-9]*:$'` da vacío.
