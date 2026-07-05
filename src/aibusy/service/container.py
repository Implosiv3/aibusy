class ServiceContainer:
    """
    The container in which we accumulate the
    different services we register with the
    plugins.

    The service will be registered by the
    interface it is implementing.

    You can register a service like this:
    ```
    builder.services.register(
        HttpClient,
        RequestsHttpClient(),
    )
    ```
    """

    def __init__(
        self
    ):
        self._services = {}

    def register(
        self,
        service_type,
        instance,
    ):
        """
        Register the service `instance` provided with
        the `service_type` as the key.
        """
        self._services[service_type] = instance

    def get(
        self,
        service_type,
    ):
        try:
            return self._services[service_type]
        except KeyError:
            raise ServiceNotFoundError(service_type)
        

# TODO: Move this
class ServiceNotFoundError(
    Exception
):
    
    ...
