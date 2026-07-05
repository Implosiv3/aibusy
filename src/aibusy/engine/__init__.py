from aibusy.engine.execution.executor import Executor
from aibusy.engine.execution.context import ExecutionContext
from aibusy.graph.builder import GraphBuilder
from aibusy.graph.classes.port_reference import PortReference
from aibusy.engine.context import EngineContext


class Engine:
    """
    The engine that has an specific configuration
    and is capable of perform the operations to
    obtain the final result.
    """

    def __init__(
        self,
        *,
        context: EngineContext,
        executor: Executor,
        graph_builder: GraphBuilder
    ):
        self._context = context
        self._executor = executor
        self._graph_builder = graph_builder

    async def run(
        self,
        *targets: PortReference
    ):
        build = self._graph_builder.build(targets)

        context = ExecutionContext(
            engine = self._engine,
            cache = self._cache,
        )

        await self._executor.run(
            targets = build.targets,
            context = context,
        )

        values = [
            context.output(
                target.operation,
                target.name,
            )
            for target in build.targets
        ]

        if len(values) == 1:
            return values[0]

        return tuple(values)