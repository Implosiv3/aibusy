from aibusy.engine.execution.resource.resolver.abstract import ResourceResolver
from aibusy.engine.execution.resource.manager import ExecutionResourceManager
from aibusy.runtime.resource.spec.abstract import ResourceSpec
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
        resource_manager: ExecutionResourceManager
    ):
        self._builders = resource_builders
        self._manager = resource_manager

    async def resolve(
        self,
        spec: ResourceSpec
    ):
        instance = self._manager.get_instance(spec)

        if instance is not None:
            return instance

        builder = self._builders.get(type(spec))

        resource = await builder.build(spec)

        instance = await resource.load()

        self._manager.store(
            spec,
            resource,
            instance,
        )

        return instance