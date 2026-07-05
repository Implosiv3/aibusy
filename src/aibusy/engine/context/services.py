from aibusy.engine.context.collection.classes import ModelExecutorCollection


class Services:
    """
    Class to group the services we have
    available.
    """

    def __init__(
        self
    ):
        self.model_executors = ModelExecutorCollection()
        # self.downloader = Downloader()
        # self.http = RequestsHttpClient()
        # self.installer = ModelInstaller()
        ...