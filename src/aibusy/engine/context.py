from aibusy.engine.settings import EngineSettings
from aibusy.runtime.scheduler.collection import SchedulerCollection
# from aibusy.engine.execution.resource.resolver.abstract import ResourceResolver
from aibusy.runtime.resource.builder.collection import ResourceBuilderCollection
from aibusy.engine.execution.asset.repository.abstract import AssetRepository
from aibusy.service.container import ServiceContainer


class EngineContext:
    """
    Permanent context shared by every execution
    of the Engine.

    It contains the long-lived infrastructure
    required during execution.
    """

    def __init__(
        self,
        *,
        settings: EngineSettings,
        services: ServiceContainer,
        assets: AssetRepository,
        # resources: ResourceResolver,
        resource_builders: ResourceBuilderCollection,
        schedulers: SchedulerCollection,
    ):
        self.settings = settings
        """
        Global engine settings.
        """
        self.services = services
        """
        The services we have in the engine.
        """
        self.assets = assets
        """
        The assets we have available that can be loaded
        and transformed into resources.
        """
        # self.resources = resources
        # """
        # Resolver capable of resolving runtime resources
        # from ResourceSpec objects.
        # """
        self.resource_builders = resource_builders
        """
        Collection of builders capable of constructing
        Resource objects from ResourceSpec objects.
        """
        self.schedulers = schedulers
        """
        The schedulers we have registered
        """