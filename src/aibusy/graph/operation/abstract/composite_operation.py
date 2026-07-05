from aibusy.graph.operation.abstract.base import Operation
from aibusy.graph.classes.port_reference import PortReference
from abc import ABC, abstractmethod


class CompositeOperation(
    Operation,
    ABC
):
    
    @abstractmethod
    def expand(
        self
    ) -> dict[str, PortReference]:
        """
        The ability to expand it into different
        operations. It doesn't exist if it is a
        simple operation.
        """
        ...