from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from aibusy.engine.execution.asset.installed import InstalledAsset
from abc import ABC, abstractmethod


class AssetInstaller(
    ABC
):
    """
    Install an asset depending on the
    `spec_type`.
    """

    spec_type: type[AssetSpec]

    @abstractmethod
    async def install(
        self,
        spec: AssetSpec
    ) -> InstalledAsset:
        ...


# An implementation could be this
"""
class HuggingfaceCheckpointInstaller(
    AssetInstaller
):

    asset_type = DiffusersCheckpointSpec

    async def install(
        self,
        spec
    ):
        ...
"""