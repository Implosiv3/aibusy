from collections.abc import Iterator
from typing import Generic, TypeVar


T = TypeVar('T')

class OrderedCollection(
    Generic[T]
):
    """
    Base class for collections whose elements
    are iterated in insertion order.
    """

    def __init__(self):
        self._items: list[T] = []

    def register(
        self,
        item: T
    ) -> None:
        self._items.append(item)

    def clear(
        self
    ) -> None:
        self._items.clear()

    def __iter__(
        self
    ) -> Iterator[T]:
        return iter(self._items)

    def __len__(
        self
    ) -> int:
        return len(self._items)

    def __contains__(
        self,
        item: T
    ) -> bool:
        return item in self._items