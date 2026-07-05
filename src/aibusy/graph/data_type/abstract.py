from typing import Union, TypeVar, Generic


T = TypeVar('T')

class DataType(
    Generic[T]
):
    """
    Our engine's data type class, that defines some
    conditions but also the `runtime_type` that is
    expected.
    """
    
    runtime_type: type[T]
    """
    The python type of this data type. This can be
    used to validate it.
    """

    def __init__(
        self,
        name: str,
        runtime_type: type[T],
        parent: Union['DataType', None] = None
    ):
        self.name = name
        self.runtime_type = runtime_type
        self.parent = parent

    def is_assignable_from(
        self,
        other: 'DataType'
    ) -> bool:
        current = other

        while current is not None:
            if current == self:
                return True

            current = current.parent

        return False
    
    def validate(
        self,
        value: object
    ) -> None:
        if not isinstance(value, self.runtime_type):
            raise TypeError(f'Expected "{self.runtime_type.__name__}", got "{type(value).__name__}".')
        
    def schema(
        self
    ) -> dict:
        return {
            'name': self.name,
            'runtime_type': self.runtime_type.__name__
        }
    
    def __str__(
        self
    ) -> str:
        return self.name

    def __repr__(
        self
    ) -> str:
        return f'DataType({self.name!r})'