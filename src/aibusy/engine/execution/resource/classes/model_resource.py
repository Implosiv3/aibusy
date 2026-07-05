from aibusy.engine.execution.resource.abstract import Resource
from aibusy.engine.execution.resource.key import ResourceKey
from aibusy.classes.device import Device
from aibusy.model.classes.installed import InstalledModel
from aibusy.model.classes.loaded import LoadedModel
from aibusy.model.loader.abstract import ModelLoader
from aibusy.graph.classes.port_reference import PortReference
from typing import Union


class ModelResource(
    Resource[LoadedModel]
):
    """
    A model resource that is capable of loading
    a model by using its specific loader.
    """
    
    @property
    def key(
        self
    ):
        return ResourceKey(
            category = 'model',
            identifier = f'{self._installed_model.provider}:{self._installed_model.family}:{self._installed_model.identifier}',
            variant = str(self._device)
        )

    def __init__(
        self,
        installed_model: InstalledModel,
        loader: Union[ModelLoader, PortReference],
        device: Union[Device, PortReference]
    ):
        self._installed_model = installed_model
        self._loader = loader
        self._device = device

    async def _load(
        self
    ) -> LoadedModel:
        """
        *For internal use only*

        Load the model resource by using the loader
        provided.
        """
        return await self._loader.load(
            installed_model = self._installed_model,
            device = self._device
        )
    
    async def unload(
        self,
        instance
    ) -> None:
        await self._loader.unload(instance)