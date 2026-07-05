from aibusy.model.classes.installed import InstalledModel
from aibusy.model.classes.loaded import LoadedModel
from aibusy.engine.plugin.component import PluginComponent
from aibusy.classes.device import Device
from abc import ABC, abstractmethod


class ModelLoader(
    PluginComponent,
    ABC
):
    """
    Class to load a model and make it ready to use.
    This will transform an `InstalledModel` into a
    `LoadedModel` that can be used in the way it
    should be; I mean, the implementation will be
    specifically made for that model, which could
    be using transformers, torch, diffusers, etc.
    """
    
    @property
    @abstractmethod
    def family(
        self
    ) -> str:
        """
        The family of the model loader.
        """
        ...

    def is_supported(
        self,
        family: str
    ) -> str:
        return self.family == family

    @abstractmethod
    async def load(
        self,
        installed_model: InstalledModel,
        device: Device,
        # TODO: Maybe add 'dtype' here
    ) -> object:
        ...

    async def unload(
        self,
        instance: LoadedModel
    ):
        pass