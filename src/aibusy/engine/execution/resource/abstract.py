from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar("T")


class Resource(
    Generic[T],
    ABC
):
    """
    Represents something that knows how to
    create and destroy a runtime instance.
    """

    @abstractmethod
    async def load(
        self
    ) -> T:
        ...

    async def unload(
        self,
        instance: T
    ) -> None:
        pass


# One implementation
"""
class UNetResource(
    Resource[UNet2DConditionModel]
):

    def __init__(
        self,
        ...
    ):
        ...

    async def load(
        self
    ):
        return UNet2DConditionModel.from_pretrained(...)


class DiffusersUNetResource(
    Resource
):

    def __init__(
        self,
        *,
        location,
        dtype,
        device
    ):
        self._location = location
        self._dtype = dtype
        self._device = device

    async def load(self):
        ...
"""