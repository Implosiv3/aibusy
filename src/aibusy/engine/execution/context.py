from aibusy.engine.context.engine import EngineContext
from aibusy.graph.operation.abstract.base import Operation
from aibusy.engine.cache import Cache
from uuid import UUID


class ExecutionContext:
    """
    Context used during a single execution of the Engine.

    It contains the execution state (outputs, acquired
    resources, cache...) together with a reference to
    the permanent EngineContext.

    You can do things like this:
    ```
    context.engine.model_backends.register(...)
    ```
    """

    def __init__(
        self,
        *,
        engine: EngineContext,
        cache: Cache,
    ):
        self.engine = engine
        """
        Permanent engine context.
        """
        self.cache = cache
        """
        Execution cache.
        """
        self._operation_outputs: dict[UUID, dict[str, object]] = {}

    @property
    def settings(
        self
    ):
        return self.engine.settings

    @property
    def services(
        self
    ):
        return self.engine.services

    def has_result(
        self,
        operation: Operation
    ) -> bool:
        return operation.id in self._operation_outputs

    def store(
        self,
        operation: Operation,
        outputs: dict[str, object]
    ) -> None:
        self._operation_outputs[operation.id] = outputs

    def outputs(
        self,
        operation: Operation
    ) -> dict[str, object]:
        return self._operation_outputs[operation.id]

    def output(
        self,
        operation: Operation,
        name: str
    ) -> object:
        return self._operation_outputs[operation.id][name]