from aibusy.engine.settings import EngineSettings
from aibusy.runtime.scheduler.collection import SchedulerCollection
from aibusy.engine.execution.resource.resolver.abstract import ResourceResolver
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
        # TODO: Why Repo here and Resolver in the other
        assets: AssetRepository,
        resources: ResourceResolver,
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
        self.resources = resources
        """
        The resources instances, such as models, that
        have been loaded.
        """
        self.schedulers = schedulers
        """
        The schedulers we have registered
        """