from abc import ABC, abstractmethod


class TextEncoder(
    ABC
):

    @abstractmethod
    async def encode(
        self,
        tokens,
    ):
        """
        Convert tokens into embeddings.
        """
        ...