from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.engine.execution.asset.installer.collection import AssetInstallerCollection
from aibusy.engine.execution.asset.spec.abstract import AssetSpec


class AssetRepository:

    def __init__(
        self,
        installers: AssetInstallerCollection
    ):
        self._installers = installers

        self._assets: dict[
            AssetSpec,
            InstalledAsset
        ] = {}

    async def resolve(
        self,
        spec: AssetSpec
    ) -> InstalledAsset:
        """
        Ensure the asset described by `spec` is installed
        and return its identifier.
        """
        installer = self._installers.get(type(spec))

        installed = await installer.install(spec)

        self._assets.setdefault(
            installed.spec,
            installed
        )

        return installed