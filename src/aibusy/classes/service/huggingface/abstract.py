from abc import ABC, abstractmethod
from typing import Union


class HuggingfaceClient(
    ABC
):
    
    # TODO: Add '__init__' with token (?)

    @abstractmethod
    async def download_snapshot(
        self,
        *,
        repository: str,
        revision: Union[str, None] = None,
    ) -> str:
        """
        Download the `repository` snapshot and return
        the local directory where it has been installed.
        """
        ...