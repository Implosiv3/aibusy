from abc import ABC


class AssetSpec(
    ABC
):
    """
    Describes an asset independently of whether
    it is installed.
    """

# Can evolve into this
"""
@dataclass(frozen=True)
class DiffusersCheckpointSpec(AssetSpec):

    model_id: str
    revision: str | None = None
    variant: str | None = None
"""