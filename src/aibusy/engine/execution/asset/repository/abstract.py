from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from abc import ABC, abstractmethod



class AssetRepository(
    ABC
):
    """
    Resolves AssetSpecs into InstalledAssets.
    """

    @abstractmethod
    async def resolve(
        self,
        spec: AssetSpec
    ) -> InstalledAsset:
        ...