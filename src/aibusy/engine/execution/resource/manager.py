from aibusy.runtime.resource.abstract import Resource
from aibusy.runtime.resource.spec.abstract import ResourceSpec


class ExecutionResourceManager:
    """
    Class to handle the different resources and
    their instances to avoid loading the same
    resource into memory more than once.
    """

    def __init__(
        self
    ):
        self._resources: dict[ResourceSpec, Resource] = {}
        self._instances: dict[ResourceSpec, object] = {}

    def get_instance(
        self,
        spec: ResourceSpec,
    ):
        return self._instances.get(spec)

    def store(
        self,
        spec: ResourceSpec,
        resource: Resource,
        instance,
    ):
        self._resources[spec] = resource
        self._instances[spec] = instance

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