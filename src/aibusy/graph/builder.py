from aibusy.graph.graph import Graph
from aibusy.graph.build_result import GraphBuildResult
from aibusy.graph.operation.abstract.base import Operation
from aibusy.graph.operation.abstract.composite_operation import CompositeOperation
from aibusy.graph.operation.abstract.atomic_operation import AtomicOperation
from aibusy.graph.classes.port_reference import PortReference
from aibusy.graph.operation.dependency.finder import DependencyFinder
from typing import Union, Iterable
from uuid import UUID


class GraphBuilder:
    """
    Class capable of building the `Graph`
    by using all the `targets` provided,
    that can be `Operation` or `PortReference`.
    """

    def __init__(
        self
    ):
        self._dependency_finder = DependencyFinder()

    def build(
        self,
        targets: Union[Operation, PortReference, Iterable[Union[Operation, PortReference]]]
    ) -> GraphBuildResult:
        if isinstance(targets, (Operation, PortReference)):
            targets = [targets]

        operations: dict[UUID, Operation] = {}
        replacements: dict[tuple[UUID, str], PortReference] = {}

        for target in targets:
            if isinstance(target, Operation):
                self._visit_operation(
                    operation = target,
                    operations = operations,
                    replacements = replacements
                )
            elif isinstance(target, PortReference):
                self._visit_operation(
                    operation = target.operation,
                    operations = operations,
                    replacements = replacements
                )
            else:
                raise TypeError(f'Unsupported target: {type(target)}')

        graph = Graph()

        for operation in operations.values():
            graph.add(operation)

        resolved_targets = tuple(
            replacements.get(
                (target.operation.id, target.name),
                target
            )
            for target in targets
            if isinstance(target, PortReference)
        )

        return GraphBuildResult(
            graph = graph,
            targets = resolved_targets
        )
    
    def _visit_operation(
        self,
        operation: Union[AtomicOperation, CompositeOperation],
        operations: dict[UUID, Operation],
        replacements: dict[tuple[UUID, str], PortReference]
    ) -> None:
        """
        *For internal use only*

        Visit the `operation` provided to register
        it.
        """
        if isinstance(operation, CompositeOperation):
            return self._visit_composite_operation(
                operation = operation,
                operations = operations,
                replacements = replacements
            )

        return self._visit_atomic_operation(
            operation = operation,
            operations = operations,
            replacements = replacements
        )

    def _visit_atomic_operation(
        self,
        operation: AtomicOperation,
        operations: dict[UUID, Operation],
        replacements: dict[tuple[UUID, str], PortReference]
    ) -> None:
        """
        *For internal use only*

        Visit an `AtomicOperation` to obtain the
        output from it.
        """
        operations[operation.id] = operation

        for dependency in self._dependency_finder.find(operation):
            self._visit_operation(
                operation = dependency,
                operations = operations,
                replacements = replacements
            )

        return

    def _visit_composite_operation(
        self,
        operation: CompositeOperation,
        operations: dict[UUID, Operation],
        replacements: dict[tuple[UUID, str], PortReference]
    ) -> None:
        """
        *For internal use only*

        Decompose a `CompositeOperation` and visit
        all the atomic operations in it.
        """
        expanded = operation.expand()

        for output_name, port in expanded.items():
            replacements[
                (operation.id, output_name)
            ] = port

        for port in expanded.values():
            self._visit_operation(
                operation = port.operation,
                operations = operations,
                replacements = replacements
            )

        self._replace_references(
            composite = operation,
            expanded = expanded,
            operations = operations
        )
    
    def _replace_references(
        self,
        composite: CompositeOperation,
        expanded: dict[str, PortReference],
        operations: dict[UUID, Operation]
    ) -> None:
        """
        *For internal use only*

        Replace the references of a `CompositeOperation`
        to act like if it didn't exist but the atomic
        ones inside.
        """
        for operation in operations.values():
            for input_name, value in operation._connections.items():
                if not isinstance(value, PortReference):
                    continue

                if value.operation is not composite:
                    continue

                operation._connections[input_name] = expanded[value.name]