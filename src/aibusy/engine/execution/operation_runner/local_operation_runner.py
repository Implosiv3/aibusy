from aibusy.engine.execution.operation_runner.abstract import OperationRunner
from aibusy.engine.execution.context import ExecutionContext
from aibusy.graph.operation.abstract.base import Operation


class LocalOperationRunner(
    OperationRunner
):

    async def run(
        self,
        operation: Operation,
        # Let it here to respect the structure
        inputs: dict,
        context: ExecutionContext
    ) -> dict[str, object]:
        return await operation.execute(context)