from aibusy.engine.plugin.abstract import Plugin
from aibusy.engine.engine import Engine
from aibusy.engine.context.engine import EngineContext
from aibusy.graph.builder import GraphBuilder
from aibusy.engine.cache.memory_cache import MemoryCache
from aibusy.engine.execution.operation_runner.local_operation_runner import LocalOperationRunner
from aibusy.engine.execution.operation_runner.abstract import OperationRunner
from aibusy.engine.execution.executor import Executor
from aibusy.engine.execution.runtime.value_resolver.port_reference_resolver import PortReferenceRuntimeValueResolver
from aibusy.engine.execution.runtime.value_resolver.abstract import RuntimeValueResolver
from aibusy.engine.settings import EngineSettings
from aibusy.engine.plugin.context import PluginContext
from typing import Callable, Union


class EngineBuilder:
    """
    A builder to get an Engine capable of
    performing operations.

    Use it like this:
    ```
    engine = (
        EngineBuilder()
        .add_plugin(
            DiffusersRuntimePlugin()
        )
        .add_plugin(
            HuggingfaceBackendPlugin()
        )
        .build()
    )
    ```
    """

    def __init__(
        self
    ):
        from aibusy.service.container import ServiceContainer
        from aibusy.engine.execution.asset.installer.collection import AssetInstallerCollection
        from aibusy.runtime.scheduler.collection import SchedulerCollection
        from aibusy.runtime.resource.builder.collection import ResourceBuilderCollection
        from aibusy.engine.execution.runtime.value_resolver.collection import RuntimeValueResolverCollection

        self.services = ServiceContainer()
        self.schedulers = SchedulerCollection()
        self.runtime_value_resolvers = RuntimeValueResolverCollection()
        self.assets_installers = AssetInstallerCollection()
        self.resources_builders = ResourceBuilderCollection()

        self._operation_runner = LocalOperationRunner()
        self._graph_builder = GraphBuilder()
        # TODO: How to handle this properly (?) Collection (?)
        self._registered_plugins = {}

        self._instantiate_executor()

        self._was_built: bool = False
        """
        Internal boolean flag to control when the
        builder has already built an engine.
        """

    def _instantiate_executor(
        self
    ) -> 'EngineBuilder':
        """
        *For internal use only*

        Create (or recreate if existing) the executor
        instance:

        ```
        self._executor = Executor(
            graph_builder = self._graph_builder,
            operation_runner = self._operation_runner,
            runtime_value_resolvers = self._runtime_value_resolvers
        )
        ```
        """
        self._executor = Executor(
            graph_builder = self._graph_builder,
            operation_runner = self._operation_runner,
            runtime_value_resolvers = self.runtime_value_resolvers
        )

        return self

    def set_operation_runner(
        self,
        operation_runner: OperationRunner
    ) -> 'EngineBuilder':
        self._operation_runner = operation_runner

        self._instantiate_executor()

        return self

    def add_plugin(
        self,
        plugin: Plugin
    ) -> 'EngineBuilder':
        """
        Add the `plugin` provided with the
        dependencies (if existing), that will
        be installed before the plugin itself.
        """
        self._ensure_not_built()

        for plugin_type in plugin.dependencies:
            self.add_plugin(
                plugin_type()
            )

        if plugin_type in self._registered_plugins:
            # TODO: Maybe just 'pass'
            raise Exception(f'The "{plugin_type}" plugin is already installed.')

        plugin.register(self)

        return self
    
    def build(
        self
    ) -> Engine:
        """
        Build the `Engine` instance by creating
        and `EngineContext` and using the graph
        builder and the executor.
        """
        self._ensure_not_built()

        engine_context = self._build_engine_context()

        self._was_built = True

        return Engine(
            context = engine_context,
            executor = self._executor,
            graph_builder = self._graph_builder,
        )
    
    def _build_engine_context(
        self
    ) -> EngineContext:
        # TODO: This has to be changed
        plugin_context = PluginContext(
            builder = self
        )

        self._configure_components(plugin_context)

        from aibusy.engine.execution.asset.repository.default import DefaultAssetRepository
        from aibusy.engine.execution.resource.resolver.default import DefaultResourceResolver

        asset_repository = DefaultAssetRepository(
            installers = self._assets_installers
        )

        resource_resolver = DefaultResourceResolver(
            builders = self._resources_builders,
        )

        return EngineContext(
            settings = self.settings,
            services = self.services,
            assets = asset_repository,
            resources = resource_resolver,
            schedulers = self.schedulers,
        )
    
    def _configure_components(
        self,
        plugin_context: PluginContext
    ) -> None:
        """
        *For internal use only*

        Method to iterate over all the components
        to configure them by passing the plugin
        context to let each component register the
        settings associated.
        """
        # TODO: I think this has to change
        for installer in self._assets_installers:
            installer.configure(plugin_context)

        for builder in self._resources_builders:
            builder.configure(plugin_context)

        for runtime_value_resolver in list(self.runtime_value_resolvers):
            runtime_value_resolver.configure(plugin_context)

        # components = [
        #     *self._runtime_value_resolvers.values(),
        #     # *self._data_type_validators,
        # ]

        # for component in components:
        #     component.configure(plugin_context)
    
    def _ensure_not_built(
        self
    ) -> None:
        if self._was_built:
            raise RuntimeError('This EngineBuilder has already been used to build an Engine.')
        
    