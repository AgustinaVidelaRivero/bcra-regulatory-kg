# Trazabilidad del algoritmo de búsqueda del harness (`buscar_nodos`)

> Tarea forense de solo lectura sobre el repo. Reconstruyo el origen del algoritmo de
> búsqueda léxica del harness KG-RAG (`data/experiment/evaluacion/harness.py`,
> `GraphIndex.buscar_nodos`), su justificación documental (si existe), su caracterización
> en términos de recuperación de información, y el límite de lo que el repo permite saber.
> Todos los hashes, fechas y números salen de `git log` / `git blame` / `git grep`
> ejecutados hoy (2026-07-25); nada es estimación.

## 1. Arqueología git

### 1.1 Historia completa del archivo

`git log --follow --oneline -- data/experiment/evaluacion/harness.py` devuelve **un único
commit**:

```
7e8b91e freeze harness + caching multi-turn (2.05x) — equivalencia verificada:
        divergencias off-vs-on atribuidas a no-determinismo run-to-run via control
        off-vs-off2 + investigacion CQ-029 (8 corridas)
```

- **Hash completo:** `7e8b91ec32eab7d1505f9692367ec3f9a29e92c5`
- **Fecha (autor y commit coinciden):** 2026-06-10 07:48:10 -0300
- **Archivos del commit:** `harness.py` (660 líneas, creación completa),
  `ab_caching.py` (159), `03c_cq029_investigacion.md` (36). Solo adiciones (+855).
- **Commit padre:** `1910df5` — "freeze judge v2.1.1 — calibrado 12/12 vs veredictos
  humanos" (2026-06-09 19:11:23 -0300).

Es decir: `harness.py` **nació entero y congelado** en `7e8b91e` y **nunca volvió a ser
modificado** — ni el scoring ni ninguna otra línea. Lo confirma el blame (§1.3). El patrón
de la historia alrededor (el padre inmediato es "freeze judge", y el gran commit de la fase,
`d56020e` "FASE 2.3 — harness KG-RAG de evaluación: loader+harness+juez congelados..."
del 2026-06-23, agrega el resto de la infraestructura pero **no toca** `harness.py`)
muestra que el desarrollo ocurrió en sesiones de trabajo previas al commit y se selló en
git por tandas de "freeze". No hay historia incremental del algoritmo dentro del repo:
no existe un commit donde el scoring haya sido distinto.

Verifiqué además con pickaxe (`git log --all -S "buscar_nodos"`) que ningún commit
anterior a `7e8b91e`, en ninguna rama, contiene el identificador `buscar_nodos` (ni
`GraphIndex`, ni `_node_tokens`) en código: `7e8b91e` es la primera aparición. Los
commits posteriores que matchean el pickaxe solo *mencionan* la función en documentación
y en módulos nuevos que la replican (p. ej. `test_alcanzabilidad.py`), sin modificarla.

### 1.2 El diff que introdujo el algoritmo (fragmento relevante de `7e8b91e`)

Como el commit es la creación del archivo, el "diff" es el contenido mismo. El núcleo
([harness.py:130-161](data/experiment/evaluacion/harness.py:130)):

```python
class GraphIndex:
    """Índices en memoria sobre el KnowledgeGraph del loader para las 3 tools."""

    def __init__(self, kg: KnowledgeGraph):
        self.kg = kg
        self.by_id = {n.id: n for n in kg.nodes}
        # tokens por nodo (label + id)
        self._node_tokens = {
            n.id: set(_tokens(n.label) + _tokens(n.id)) for n in kg.nodes
        }
        ...

    # --- tool 1 ---
    def buscar_nodos(self, consulta: str, limite: int = 10) -> dict:
        q = set(_tokens(consulta))
        if not q:
            return {"consulta": consulta, "resultados": [], "total": 0}
        scored = []
        for n in self.kg.nodes:
            score = len(q & self._node_tokens[n.id])
            if score:
                scored.append((score, len(n.label or ""), n))
        scored.sort(key=lambda t: (-t[0], t[1], t[2].id))
        try:
            limite = max(1, min(int(limite), 50))
        except (TypeError, ValueError):
            limite = 10
```

Con la normalización léxica ([harness.py:98-107](data/experiment/evaluacion/harness.py:98)):

```python
def _strip_accents(s: str) -> str:
    nfkd = unicodedata.normalize("NFKD", s)
    return "".join(c for c in nfkd if not unicodedata.combining(c))

_TOKEN_RE = re.compile(r"[a-z0-9]+")

def _tokens(s: str) -> list:
    return _TOKEN_RE.findall(_strip_accents((s or "").lower()))
```

### 1.3 Blame de las líneas del score actual

`git blame -L 130,175 data/experiment/evaluacion/harness.py`: **el 100 % de las líneas de
`GraphIndex` y `buscar_nodos` (130-175) pertenece a `7e8b91ec`, 2026-06-10.** No hay
ninguna línea del algoritmo atribuible a otro commit. Commits que tocaron el scoring
después de su introducción: **ninguno**.

## 2. Contexto documental de la época

### 2.1 La única justificación escrita contemporánea: el docstring del propio harness

El registro de diseño más cercano al momento de introducción está **dentro del archivo
mismo**, en su docstring de cabecera ([harness.py:7-13](data/experiment/evaluacion/harness.py:7)),
verbatim:

> ```
> Spec (decidida con la autora):
>   - Modelo: claude-haiku-4-5-20251001, FIJO para los 5 grafos. Temperature 0.
>   - Tools (operan sobre el modelo en memoria del loader):
>       buscar_nodos(consulta, limite=10) — búsqueda léxica sobre label e id
>           (normalizada: lowercase + sin acentos, por tokens, ranking por
>           nº de tokens matcheados). Devuelve id, type, label y un resumen
>           corto de properties. Sin embeddings (decisión explícita revisable).
> ```

Esto documenta **qué** se decidió (búsqueda léxica por tokens sobre label e id, ranking
por cantidad de tokens matcheados) y registra **una** decisión de diseño con carácter de
tal: "**Sin embeddings (decisión explícita revisable)**". No documenta **por qué** se
eligió el conteo de intersección como función de score, ni menciona alternativas léxicas
ponderadas (TF-IDF, BM25), ni justifica el desempate `(-score, len(label), id)`, el
default `limite=10` o el clamp a 50.

### 2.2 Qué dicen (y qué no dicen) los demás docs de la época

Revisé los documentos tracked contemporáneos al freeze y a la Fase 2.3
(`00_inventario.md`, `01_validacion_loader.md`, `02_calibracion_juez.md`,
`03_ab_caching.md`, `03b_ab_control.md`, `03c_cq029_investigacion.md`,
`04_auditoria_instrumentacion.md`, más `docs/ARQUITECTURA.md`):

- **Ninguno contiene una justificación del diseño de la búsqueda ni un registro de
  alternativas consideradas.** Lo digo explícitamente: no hay en el repo ningún documento
  que discuta por qué intersección de tokens y no otra cosa, ni que registre haber
  evaluado y descartado TF-IDF, BM25, stemming o expansión de sinónimos para esta tool.
- `docs/ARQUITECTURA.md:98` solo describe: "`harness.py` [CONGELADO] | Agente respondedor
  KG-RAG: Haiku 4.5 fijo, temp 0, 3 tools de grafo (buscar_nodos / ver_nodo /
  ver_vecinos)".
- `00_inventario.md` (el documento sobre el que se tomaron las 4 decisiones de diseño de
  la Fase 2.3 registradas en `CLAUDE.md`) trata la normalización de los grafos, los
  duplicados de Run 5, la API y el provenance — **no** el mecanismo de búsqueda.
- El descarte de similitud semántica con embeddings sí tiene un antecedente documentado,
  pero en **otro contexto** (canonización de tipos del Run 4, previo al harness):
  [run_4_schema_light/schema.md:199-201](data/experiment/run_4_schema_light/schema.md:199)
  concluye que "**MiniLM multilingüe está dominado por los adjetivos del dominio
  regulatorio en español** (...) y produce sim ≥ 0.85 a pares con head nouns distintos",
  y decide: "la canonización semántica vía MiniLM se descarta para este run". Es evidencia
  de clima de diseño (desconfianza empírica de embeddings off-the-shelf en este dominio),
  no una justificación directa de la tool del harness.

### 2.3 Documentación *posterior* que fija la semántica del algoritmo

Aunque no hay justificación de origen, el algoritmo quedó especificado con precisión en
documentos posteriores, porque la capa determinística del verificador (Fase 2.4/2.5) lo
replica:

- [test_alcanzabilidad.py:27-29](data/experiment/evaluacion/test_alcanzabilidad.py:27)
  (docstring, semántica pre-registrada): "La réplica del scoring de
  `harness.GraphIndex.buscar_nodos` es literal: score = |tokens(consulta) ∩
  tokens(label+id del nodo)|, orden (-score, len(label), id), top-`limite`. Un score 0
  deja al nodo FUERA del ranking".
- [docs/especificacion_capa_deterministica.md:38-50](docs/especificacion_capa_deterministica.md:38)
  (módulo D1): "simula el índice léxico real (`harness.GraphIndex`, réplica exacta del
  scoring de `buscar_nodos`)".
- [docs/evidencia_capa_d/reporte_d1.md:29-35](docs/evidencia_capa_d/reporte_d1.md:29):
  réplica verificada con pytest, incluida una aserción corregida durante el desarrollo
  porque "el desempate por label más corto del índice pone primero a otro nodo con el
  mismo score (...) ese desempate es precisamente el comportamiento real replicado".

## 3. Caracterización técnica honesta

**Qué es.** `buscar_nodos` es *matching booleano OR con ranking por nivel de
coordinación*: la consulta y cada nodo se reducen a conjuntos de tokens (lowercase,
acentos removidos vía NFKD, tokenización por regex `[a-z0-9]+`), el score de un nodo es
la **cardinalidad de la intersección** `|Q ∩ D|` (con `D` = tokens de label + id,
solamente), se descarta todo nodo con intersección vacía, y se ordena por
`(-score, len(label), id)` — score descendente, con desempate primero por label más
corto y después alfabético por id. El `limite` se clampea a `[1, 50]` con default 10.

**Qué NO es.** No hay ponderación de ningún tipo:

- **Sin pesos por rareza de término** (sin IDF): el token "entidades", presente en media
  colección, vale exactamente lo mismo que un término discriminante raro.
- **Sin frecuencia de término ni normalización por largo del documento** (sin TF, sin la
  normalización por longitud de BM25): los tokens de nodo son un *set*, y el largo del
  label solo interviene como desempate, no como normalización del score.
- **Sin stemming ni lematización**: singular/plural no matchean — limitación ya medida
  por el proyecto (§4).
- **Sin sinónimos, sin expansión de consulta, sin embeddings**: la única "semántica" es
  la coincidencia exacta de tokens normalizados.
- **Indexa únicamente label e id** — no `description` ni el resto de `properties`, que
  es donde vive la mayor parte del contenido de los nodos.

**¿Corresponde a un método con nombre?** El pariente más cercano en la literatura de IR
es el ranking de *coordination level* (ordenar los resultados de una búsqueda booleana OR
por cantidad de términos de la consulta presentes en el documento), una técnica de la era
pre-ponderación de los sistemas booleanos; visto como medida de conjuntos, el score es un
solapamiento sin normalizar (la versión no normalizada de Jaccard/overlap coefficient).
Pero decir "implementa coordination-level ranking" sería sobre-atribuir: **el hallazgo
honesto es que se trata de la heurística naive estándar** — "contar cuántas palabras de
la consulta aparecen en el título" — que cualquier persona escribe como primera versión
de una búsqueda léxica, sin que el repo muestre rastro de que se haya partido de la
literatura, comparado contra un método ponderado, o considerado siquiera la alternativa.
No hay nada malo en documentarlo así; lo incorrecto sería vestirlo de método con nombre.

## 4. Veredicto de trazabilidad

**El algoritmo fue introducido en el commit `7e8b91ec32eab7d1505f9692367ec3f9a29e92c5`
(2026-06-10 07:48 -0300, "freeze harness + caching multi-turn"), SIN justificación
documentada** de la función de score — el único registro de diseño contemporáneo es la
spec del docstring del propio archivo, que fija el mecanismo ("búsqueda léxica sobre
label e id (...) ranking por nº de tokens matcheados") y una sola decisión explícita
("Sin embeddings (decisión explícita revisable)"), sin rationale del scoring ni
alternativas registradas. **Su origen es una heurística ad-hoc genérica** (matching
booleano por solapamiento de tokens; lo más cercano con nombre en la literatura es el
coordination-level ranking de los sistemas booleanos, pero no hay evidencia de filiación
deliberada). **Las limitaciones conocidas y ya medidas del proyecto que se derivan de él
son:**

1. **Indexación label+id solamente → inalcanzabilidad léxica ("existe pero
   inalcanzable", el tercer estado).**
   [docs/hallazgos_tesis.md:70-86](docs/hallazgos_tesis.md:70) (H6, CQ-031): "el nodo
   (...) existe en run_3 con la description verbatim del Punto 4.5 del PDF; las 10
   búsquedas reales del agente y 3 consultas razonables mínimas dan 0 hits (...) Causa:
   `buscar_nodos` indexa label e id (no description); el label no comparte vocabulario
   con la pregunta y el id se trunca antes de 'garantías'". La taxonomía v2 lo incorporó
   como categoría propia `alcanzabilidad_kg`, el estado intermedio entre "falta"
   (`completitud_kg`) y "no lo encontré yo"
   ([taxonomia.md:48](.claude/skills/kg-refinement/references/taxonomia.md) y su regla:
   "está pero no se llega"), y la capa determinística D1 lo volvió medible ex ante
   ([docs/especificacion_capa_deterministica.md:38](docs/especificacion_capa_deterministica.md:38)).

2. **Empates y entierro por ranking (mecanismo B′).** El desempate por label más corto
   decide posiciones entre scores iguales
   ([docs/evidencia_capa_d/reporte_d1.md:32-35](docs/evidencia_capa_d/reporte_d1.md:32)),
   y el corte `limite` produce el mecanismo B′ — match léxico positivo, nunca visible:
   [docs/casos_gate_cqn2.md:358-372](docs/casos_gate_cqn2.md:358) (CQN2-015): "el
   portador existe, fiel y ENTERRADO POR RANKING (mecanismo B′) (...) posición global 11
   de 50 con límite 10 (...) el D1 formal medido da negativo por UN SOLO puesto";
   medición verbatim en
   [docs/evidencia_gate_cqn2/cqn2_015.md:299](docs/evidencia_gate_cqn2/cqn2_015.md:299),
   y la laguna de instrumento (D2 no distingue B′ de la inalcanzabilidad) en
   [docs/lectura_ciclo2.md:105-107](docs/lectura_ciclo2.md:105).

3. **Sin tratamiento de sinónimos ni morfología.** Caso medido de singular/plural:
   [casos_validacion.md:253](.claude/skills/kg-refinement/references/casos_validacion.md)
   ("`deudor_en_situacion_normal` vs 'deudores'; el índice no tiene stemming"; ídem
   línea 99: "singular/plural sin stemming en el índice — hermano del token truncado de
   CQ-031"). La ausencia de capa semántica es consistente con el hallazgo MiniLM del
   proyecto ([run_4_schema_light/schema.md:199-201](data/experiment/run_4_schema_light/schema.md:199)):
   los embeddings multilingües off-the-shelf, dominados por los adjetivos del dominio,
   producían fusiones falsas — el descarte de embeddings fue una decisión explícita y
   revisable del harness, y el único punto del diseño de búsqueda con antecedente
   empírico en el repo.

## 5. Nota final: lo que el repo NO permite responder

Límite honesto del forense — estas preguntas quedan sin respuesta desde el repositorio:

1. **El razonamiento de la sesión que escribió el algoritmo no quedó registrado.** El
   commit `7e8b91e` sella un archivo terminado ("freeze"); el desarrollo ocurrió fuera de
   git y no hay borradores, iteraciones ni discusión de diseño en la historia. No puedo
   saber si el scoring por intersección fue una elección deliberada entre opciones o
   simplemente la primera implementación razonable que funcionó.
2. **No sé si TF-IDF/BM25/stemming fueron consideradas y descartadas, o nunca
   consideradas.** La ausencia de mención en todos los docs de la época es compatible con
   ambas cosas; solo el descarte de embeddings quedó registrado como decisión.
3. **El rationale de los parámetros concretos** — desempate por `(len(label), id)`,
   default `limite=10`, clamp a 50 — no está documentado en ninguna parte; hoy se conocen
   sus consecuencias (B′ depende directamente del corte en 10) pero no su motivación.
4. **La spec dice "decidida con la autora"**, lo que indica que hubo una conversación de
   diseño previa al freeze; su contenido no está en el repo más allá de lo que el
   docstring resume.

Lo que sí está garantizado por la evidencia de §1: el algoritmo que corre hoy es
byte-idéntico al introducido el 2026-06-10, ningún commit posterior lo tocó, y toda la
instrumentación posterior (D1/D2) lo trata como semántica congelada a replicar, no a
corregir.
