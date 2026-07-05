from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from abc import ABC, abstractmethod


class AssetRepository(
    ABC
):
    """
    Resolve `AssetSpec` into `InstalledAsset`,
    installing if needed.
    """

    @abstractmethod
    async def install(
        self,
        spec: AssetSpec
    ) -> InstalledAsset:
        """
        Return an InstalledAsset for the given AssetSpec.

        If the asset is not already installed, install it
        before returning it.
        """
        ...