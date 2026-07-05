from typing import Generic, TypeVar
from collections.abc import Iterator


K = TypeVar('K')
V = TypeVar('V')

class KeyedCollection(
    Generic[K, V]
):
    """
    Base class for collections indexed
    by a key.
    """

    def __init__(self):
        self._items: dict[K, V] = {}

    def register(
        self,
        key: K,
        value: V
    ) -> None:
        if key in self._items:
            raise ValueError(f'"{key}" is already registered.')

        self._items[key] = value

    def get(
        self,
        key: K
    ) -> V:
        try:
            return self._items[key]
        except KeyError:
            raise LookupError(f'No item registered with key "{key}".')

    def clear(
        self
    ) -> None:
        self._items.clear()

    def keys(
        self
    ):
        return self._items.keys()

    def values(
        self
    ):
        return self._items.values()

    def items(
        self
    ):
        return self._items.items()

    def __len__(
        self
    ) -> int:
        return len(self._items)

    def __iter__(
        self
    ) -> Iterator[V]:
        return iter(self._items.values())
    
    def __contains__(
        self,
        key: K
    ) -> bool:
        return key in self._items