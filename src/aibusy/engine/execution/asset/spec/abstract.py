from pathlib import Path
from abc import ABC, abstractmethod
from typing import Sequence, Union


class AssetSpec(
    ABC
):
    """
    Describes an asset independently of whether
    it is installed.
    """

    @property
    def allow_patterns(
        self,
    ) -> Union[Sequence[str], None]:
        """
        Files that should be downloaded.

        None means "download everything".
        """
        return None

    @property
    def ignore_patterns(
        self,
    ) -> Union[Sequence[str], None]:
        """
        Files that should be ignored.
        """
        return None

    @abstractmethod
    def get_install_path(
        self,
        root_path: Path,
    ) -> Path:
        """
        Get the path where the diffusers checkpoint files
        must be downloaded.
        """
        ...

# Can evolve into this
"""
@dataclass(frozen=True)
class DiffusersCheckpointSpec(AssetSpec):

    model_id: str
    revision: str | None = None
    variant: str | None = None
"""