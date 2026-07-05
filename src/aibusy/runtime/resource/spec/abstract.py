from dataclasses import dataclass
from abc import ABC


@dataclass(frozen = True)
class ResourceSpec(
    ABC
):
    """
    Describes a resource that can be created.

    A ResourceSpec does not know how to load
    itself.
    """



# An implementation
"""
@dataclass(frozen = True)
class UNetResourceSpec(
    ResourceSpec
):

    installed_asset: InstalledAsset

    device: Device

    dtype: TorchDataType
"""