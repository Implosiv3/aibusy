from aibusy.engine.context.collection.ordered import OrderedCollection
from aibusy.engine.context.collection.keyed import KeyedCollection
from aibusy.model.loader.abstract import ModelLoader
from aibusy.model.backend.abstract import ModelBackend
from aibusy.engine.execution.runtime.value_resolver.abstract import RuntimeValueResolver
from aibusy.engine.execution.resource.builder.abstract import ResourceBuilder
from aibusy.engine.execution.resource.spec.abstract import ResourceSpec
from aibusy.engine.plugin.abstract import Plugin
from aibusy.engine.execution.asset.installer.abstract import AssetInstaller
from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from aibusy.model.executor.abstract import ModelExecutor
from aibusy.model.spec import ModelSpec


class ModelLoaderCollection(
    KeyedCollection[str, ModelLoader]
):
    """
    The model loaders we have, identified by
    the `family` field.
    """

    def register(
        self,
        loader: ModelLoader
    ):
        super().register(
            loader.family,
            loader
        )

    # TODO: Maybe remove this (?)
    def get_from_model_spec(
        self,
        model_spec: ModelSpec
    ):
        return super().get(model_spec.family)
    
    def get_from_family(
        self,
        family: str
    ):
        return super().get(family)
    

class ModelBackendCollection(
    KeyedCollection[str, ModelBackend]
):
    """
    The model backends we have, identified by
    the `provider` field.
    """
    
    def register(
        self,
        model_backend: ModelBackend
    ):
        super().register(
            model_backend.provider,
            model_backend
        )

    # TODO: Maybe remove this (?)
    def get_from_model_spec(
        self,
        model_spec: ModelSpec
    ):
        return super().get(model_spec.provider)
    
    def get_from_provider(
        self,
        provider: str
    ):
        return super().get(provider)
    

class ModelExecutorCollection(
    KeyedCollection[str, ModelExecutor]
):
    """
    The model executors we have, identified
    by the `family` field.
    """
    
    def register(
        self,
        model_executor: ModelExecutor
    ):
        super().register(
            model_executor.family,
            model_executor
        )

    # TODO: Maybe remove this (?)
    def get_from_model_spec(
        self,
        model_spec: ModelSpec
    ):
        return super().get(model_spec.family)
    
    def get_from_family(
        self,
        family: str
    ):
        return super().get(family)
    

# TODO: We need to creaete the 'NoiseGenerator' class
class NoiseGenerator:
    ...


class NoiseGeneratorCollection(
    KeyedCollection[str, NoiseGenerator]
):
    """
    The noise generators we have, identified
    by the class name.
    """

    def register(
        self,
        noise_generator: NoiseGenerator
    ):
        super().register(
            noise_generator.__class__.__name__,
            noise_generator
        )



# TODO: We need to create the 'Scheduler' class
class Scheduler:
    ...


class SchedulerCollection(
    KeyedCollection[str, Scheduler]
):
    """
    The schedulers we have, identified by
    the `identifier` field.
    """
    
    def register(
        self,
        scheduler: Scheduler
    ):
        super().register(
            scheduler.identifier,
            scheduler
        )


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


class RuntimeValueResolverCollection(
    OrderedCollection[RuntimeValueResolver]
):
    
    ...


class ResourceBuilderCollection:

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
    

class AssetInstallerCollection:

    def __init__(
        self
    ):
        self._installers = {}

    def register(
        self,
        installer: AssetInstaller
    ):
        self._installers[installer.spec_type] = installer

    def get(
        self,
        spec_type: type[AssetSpec]
    ) -> AssetInstaller:
        return self._installers[spec_type]