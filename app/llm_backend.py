"""llm_backend.py — construcción del cliente LLM de la app según backend (H2).

APP_LLM_BACKEND: "anthropic" (default, modo local actual) | "bedrock".
En modo bedrock el cliente es AnthropicBedrock (firma SigV4 con las
credenciales AWS del entorno o del rol IAM de la instancia; la API key de
Anthropic no existe ni se usa), envuelto en un ModelOverrideClient que
reescribe kwargs["model"] a APP_BEDROCK_MODEL_ID: el harness congelado fija
su MODEL como constante de módulo, así que el modelo se inyecta por cliente.
"""

import os


class ModelOverrideClient:
    """Wrapper drop-in que reescribe kwargs["model"] antes de delegar el create.
    Copia local del patrón ParamOverrideClient de
    data/experiment/evaluacion/runners/run_posthoc.py (el harness no se edita;
    todo override entra por el cliente inyectado)."""

    def __init__(self, inner, model_id: str):
        self._inner = inner
        self.model_id = model_id
        self.messages = _OverrideMessages(self)


class _OverrideMessages:
    def __init__(self, owner: ModelOverrideClient):
        self._o = owner

    def create(self, **kwargs):
        kwargs["model"] = self._o.model_id
        return self._o._inner.messages.create(**kwargs)


def backend_name() -> str:
    return (os.environ.get("APP_LLM_BACKEND") or "anthropic").strip() or "anthropic"


def effective_model_id() -> str:
    """Model ID que efectivamente se envía a la API en cada turno."""
    if backend_name() == "bedrock":
        return os.environ["APP_BEDROCK_MODEL_ID"]
    from harness import MODEL  # import tardío: main.py ya configuró sys.path
    return MODEL


def build_client():
    """Cliente a inyectar en GraphAgent (None = default del harness, modo
    anthropic). Valida la config al construir: en modo bedrock, variables
    faltantes fallan acá (al arranque), no a mitad de un chat."""
    backend = backend_name()
    if backend == "anthropic":
        return None
    if backend != "bedrock":
        raise RuntimeError(
            f"APP_LLM_BACKEND inválido: {backend!r}. Válidos: 'anthropic', 'bedrock'."
        )
    faltantes = [v for v in ("AWS_REGION", "APP_BEDROCK_MODEL_ID")
                 if not (os.environ.get(v) or "").strip()]
    if faltantes:
        raise RuntimeError(
            "Modo bedrock: faltan variables de entorno: " + ", ".join(faltantes)
            + ". Exportalas antes de arrancar la app."
        )
    from anthropic import AnthropicBedrock
    inner = AnthropicBedrock(aws_region=os.environ["AWS_REGION"])
    return ModelOverrideClient(inner, os.environ["APP_BEDROCK_MODEL_ID"])
