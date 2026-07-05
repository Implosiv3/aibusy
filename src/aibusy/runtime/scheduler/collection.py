from aibusy.utils.collection.keyed import KeyedCollection
from aibusy.runtime.interface.scheduler import Scheduler


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