from aibusy.runtime.resource.spec.abstract import ResourceSpec
from abc import ABC, abstractmethod


class ResourceResolver(
    ABC
):
    """
    Resolve a `ResourceSpec` to an instance of
    that resource.
    """

    @abstractmethod
    async def resolve(
        self,
        spec: ResourceSpec
    ):
        """
        Resolve the given `ResourceSpec` into a loaded
        runtime instance.
        """