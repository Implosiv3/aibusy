from aibusy.graph.graph import Graph
from aibusy.graph.classes.port_reference import PortReference
from dataclasses import dataclass


@dataclass(frozen = True)
class GraphBuildResult:
    """
    Result of building a graph.

    It contains the graph itself and the final
    target ports after expanding all composite
    operations.
    """

    graph: Graph
    targets: tuple[PortReference, ...]