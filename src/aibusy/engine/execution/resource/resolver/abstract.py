from aibusy.engine.execution.resource.spec.abstract import ResourceSpec
from abc import ABC, abstractmethod


class ResourceResolver(
    ABC
):

    @abstractmethod
    async def resolve(
        self,
        spec: ResourceSpec
    ):
        """
        Resolve the given `ResourceSpec` into a loaded
        runtime instance.
        """