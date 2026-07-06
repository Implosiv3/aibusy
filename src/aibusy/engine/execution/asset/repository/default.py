from aibusy.engine.execution.asset.repository.abstract import AssetRepository
from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.engine.execution.asset.installer.collection import AssetInstallerCollection
from pathlib import Path


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
        self._installed: dict[AssetSpec, InstalledAsset] = {}

    async def install(
        self,
        spec: AssetSpec,
        destination_path: Path
    ) -> InstalledAsset:
        if spec in self._installed:
            return self._installed[spec]

        installer = self._installers.get(type(spec))

        path = spec.get_install_path(destination_path)

        installed = await installer.install(
            spec = spec,
            install_path = path
        )

        self._installed[spec] = installed

        return installed