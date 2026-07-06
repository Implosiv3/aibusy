from aibusy.engine.execution.resource.resolver.abstract import ResourceResolver
from aibusy.engine.execution.resource.manager import ExecutionResourceManager
from aibusy.engine.context import EngineContext
from aibusy.runtime.resource.reference import ResourceReference
from aibusy.runtime.resource.builder.collection import ResourceBuilderCollection


class DefaultResourceResolver(
    ResourceResolver
):
    """
    Resolve a `ResourceSpec` to an instance of
    that resource, using the `resource_builders`
    provided.
    """

    def __init__(
        self,
        *,
        resource_builders: ResourceBuilderCollection,
        resource_manager: ExecutionResourceManager,
        engine_context: EngineContext
    ):
        self._builders = resource_builders
        self._manager = resource_manager
        self._engine_context = engine_context

    async def resolve(
        self,
        reference: ResourceReference
    ):
        spec = reference.spec
        instance = self._manager.get_instance(spec)

        if instance is not None:
            return instance

        builder = self._builders.get(type(spec))

        resource = await builder.build(
            spec = spec,
            context = self._engine_context
        )

        instance = await resource.load()

        self._manager.store(
            spec = spec,
            resource = resource,
            instance = instance,
        )

        return instance