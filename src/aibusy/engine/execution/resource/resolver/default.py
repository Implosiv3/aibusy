from aibusy.engine.execution.resource.resolver.abstract import ResourceResolver
from aibusy.engine.execution.resource.manager import ExecutionResourceManager
from aibusy.engine.execution.resource.spec.abstract import ResourceSpec
from aibusy.engine.execution.asset.repository.abstract import AssetRepository
from aibusy.engine.context.collection.classes import ResourceBuilderCollection


class DefaultResourceResolver(
    ResourceResolver
):

    def __init__(
        self,
        *,
        # asset_repository: AssetRepository,
        resource_builders: ResourceBuilderCollection
    ):
        # self._asset_repository = asset_repository
        self._manager = ExecutionResourceManager()
        self._builders = resource_builders

    async def resolve(
        self,
        spec: ResourceSpec
    ):
        builder = self._builders.get(type(spec))

        resource = builder.create(spec)

        # handle = await self._resource_manager.register(resource)

        return await self._manager.resolve(
            spec = spec,
            resource = resource
        )