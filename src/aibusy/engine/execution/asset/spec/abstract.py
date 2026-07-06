from pathlib import Path
from abc import ABC, abstractmethod


class AssetSpec(
    ABC
):
    """
    Describes an asset independently of whether
    it is installed.
    """

    @abstractmethod
    def get_install_path(
        self,
        rooth_path: Path,
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