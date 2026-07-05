from aibusy.engine.execution.asset.repository.abstract import AssetRepository
from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.engine.execution.asset.installer.collection import AssetInstallerCollection


class DefaultAssetRepository(
    AssetRepository
):
    """
    Resolve `AssetSpec` into `InstalledAsset`,
    installing if needed, with the `installers`
    provided.
    """

    def __init__(
        self,
        *,
        installers: AssetInstallerCollection
    ):
        self._installers = installers
        self._installed: dict[AssetSpec, InstalledAsset]

    async def install(
        self,
        spec: AssetSpec
    ) -> InstalledAsset:
        if spec in self._installed:
            return self._installed[spec]

        installer = self._installers.get(type(spec))

        installed = await installer.install(spec)

        self._installed[spec] = installed

        return installed