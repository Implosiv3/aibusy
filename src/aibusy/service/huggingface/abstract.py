from abc import ABC, abstractmethod
from pathlib import Path
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
        local_dir: Union[str, None] = None,
        allow_patterns: Union[list[str], None] = None,
        ignore_patterns: Union[list[str], None] = None,
    ) -> Path:
        """
        Download the `repository` snapshot and return
        the local directory where it has been installed.
        """
        ...