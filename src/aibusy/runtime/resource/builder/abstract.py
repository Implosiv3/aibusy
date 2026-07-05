from aibusy.runtime.resource.abstract import Resource
from aibusy.runtime.resource.spec.abstract import ResourceSpec
from abc import ABC, abstractmethod


class ResourceBuilder(
    ABC
):
    """
    Build a `Resource` instance from the
    `resource_spec` provided.
    """

    @property
    @abstractmethod
    def spec_type(
        self,
    ) -> type[ResourceSpec]:
        ...

    @abstractmethod
    def build(
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