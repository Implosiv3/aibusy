from aibusy.engine.execution.asset.repository.abstract import AssetRepository
from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.engine.context.collection.classes import AssetInstallerCollection


class DefaultAssetRepository(
    AssetRepository
):

    def __init__(
        self,
        *,
        installers: AssetInstallerCollection
    ):
        self._installers = installers

    async def resolve(
        self,
        spec: AssetSpec
    ) -> InstalledAsset:
        installer = self._installers.get(type(spec))

        return await installer.install(spec)