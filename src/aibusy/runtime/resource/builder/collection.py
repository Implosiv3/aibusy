from aibusy.utils.collection.keyed import KeyedCollection
from aibusy.runtime.resource.builder.abstract import ResourceBuilder
from aibusy.runtime.resource.spec.abstract import ResourceSpec


class ResourceBuilderCollection(
    KeyedCollection[type[ResourceSpec], ResourceBuilder]
):

    def __init__(
        self
    ):
        self._items: dict[type[ResourceSpec], ResourceBuilder] = {}

    def register(
        self,
        builder: ResourceBuilder
    ):
        self._items[builder.spec_type] = builder

    def get(
        self,
        spec_type: type[ResourceSpec]
    ) -> ResourceBuilder:
        return self._items[spec_type]