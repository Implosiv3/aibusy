from aibusy.runtime.resource.spec.abstract import ResourceSpec
from dataclasses import dataclass


@dataclass(frozen = True)
class ResourceReference:
    """
    Class to represente a resource that has
    been loaded in an operation, but we don't
    send the whole instance but a reference
    that will identify it and load it.
    """

    resource_spec: ResourceSpec