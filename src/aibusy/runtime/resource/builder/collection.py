from aibusy.utils.collection.keyed import KeyedCollection
from aibusy.runtime.resource.builder.abstract import ResourceBuilder
from aibusy.runtime.resource.spec.abstract import ResourceSpec


class ResourceBuilderCollection(
    KeyedCollection[type[ResourceSpec], ResourceBuilder]
):

    def __init__(
        self
    ):
        self._builders: dict[type[ResourceSpec], ResourceBuilder] = {}

    def register(
        self,
        builder: ResourceBuilder
    ):
        self._builders[builder.resource_type] = builder

    def get(
        self,
        resource_type: type[ResourceSpec]
    ) -> ResourceBuilder:
        return self._builders[resource_type]