from aibusy.utils.collection.ordered import OrderedCollection
from aibusy.engine.execution.runtime.value_resolver.abstract import RuntimeValueResolver


class RuntimeValueResolverCollection(
    OrderedCollection[RuntimeValueResolver]
):
    
    ...