from aibusy.engine.execution.resource.abstract import Resource
from aibusy.engine.execution.resource.spec.abstract import ResourceSpec
from abc import ABC, abstractmethod


class ResourceBuilder(
    ABC
):

    @property
    @abstractmethod
    def resource_type(
        self,
    ) -> type[ResourceSpec]:
        ...

    @abstractmethod
    def create(
        self,
        spec: ResourceSpec
    ) -> Resource:
        ...


# One implementation below
"""
class DiffusersUNetBuilder(
    ResourceBuilder
):

    resource_type = UNetResourceSpec

    def create(
        self,
        spec
    ):

        return DiffusersUNetResource(
            location=spec.asset.location,
            dtype=spec.dtype,
            device=spec.device
        )

# Using this
UNetResourceSpec(
    asset=...
    dtype=...
    compile=True
    attention="flash"
)

"""