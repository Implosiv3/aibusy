from aibusy.engine.execution.resource.abstract import Resource
from aibusy.engine.execution.resource.spec.abstract import ResourceSpec


class ExecutionResourceManager:
    """
    Class to handle the different resources and
    their instances.
    """

    def __init__(
        self
    ):
        self._resources: dict[ResourceSpec, Resource] = {}
        self._instances: dict[ResourceSpec, object] = {}
    
    async def resolve(
        self,
        spec: ResourceSpec,
        resource: Resource
    ):
        """
        Try to find the instance of the `Resource`
        associated to the `key` that is in the
        `handle` given, or load the resource, creating
        the first instance, and return it.

        From `ResourceHandle` to `Resource` instance.
        """
        if spec in self._instances:
            return self._instances[spec]

        instance = await resource.load()

        self._resources[spec] = resource
        self._instances[spec] = instance

        return instance
    
    # async def release(
    #     self,
    #     spec: ResourceSpec
    # ):
    #     instance = self._instances[spec]
    #     resource = self._resources[spec]

    #     await resource.unload(instance)

    async def release_all(
        self
    ) -> None:
        """
        Release all the instances and the resources
        register. This must be called by the
        Executor when the whole execution has
        finished.
        """
        for spec, instance in self._instances.items():
            resource = self._resources[spec]

            await resource.unload(instance)

        # TODO: Should we do this?
        # self._instances.clear()
        # self._resources.clear()