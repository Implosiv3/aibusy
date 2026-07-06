from aibusy.runtime.resource.reference import ResourceReference
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
        reference: ResourceReference
    ):
        """
        Resolve the given `ResourceSpec` into a loaded
        runtime instance.
        """