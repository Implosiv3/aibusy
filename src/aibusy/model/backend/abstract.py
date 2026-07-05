from aibusy.model.classes.installed import InstalledModel
from aibusy.model.spec import ModelSpec
from aibusy.engine.plugin.component import PluginComponent
from abc import ABC, abstractmethod


class ModelBackend(
    PluginComponent,
    ABC
):
    """
    Class to obtain models with the given `ModelSpec`
    from different sources (providers) and install them
    as `InstalledModel` to be able to use them later.
    """

    @property
    @abstractmethod
    def provider(
        self
    ) -> str:
        """
        Unique provider identifier (e.g. 'huggingface',
        'local', 's3').
        """
        ...

    @abstractmethod
    async def install(
        self,
        spec: ModelSpec
    ) -> InstalledModel:
        ...