from aibusy.graph.classes.input import Input
from aibusy.engine.plugin.component import PluginComponent
from abc import ABC, abstractmethod


class DataTypeValidator(
    PluginComponent,
    ABC
):
    """
    A class to validate the `DataType` we handle
    in the engine, to make sure they are defined
    correctly in order to be used internally.
    """

    @abstractmethod
    def validate(
        self,
        name: str,
        port: Input,
        value: object
    ) -> None:
        """
        Check that the `value` of the `DataType` with
        the given `name` is valid or not, raising an
        exception if not.
        """
        pass

    @abstractmethod
    def schema(
        self
    ) -> dict:
        ...