class PluginContext:
    """
    Shared context passed to all plugin components
    that includes the `settings` and the `services`.
    """

    def __init__(
        self,
        builder: 'EngineBuilder',
    ):
        self.builder = builder