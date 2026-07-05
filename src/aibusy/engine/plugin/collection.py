from aibusy.utils.collection.keyed import KeyedCollection
from aibusy.engine.plugin.abstract import Plugin


class PluginCollection(
    KeyedCollection[str, Plugin]
):
    """
    The plugins we have, identified by the
    class name.
    """

    def register(
        self,
        plugin: Plugin
    ):
        super().register(
            plugin.__class__.__name__,
            plugin
        )