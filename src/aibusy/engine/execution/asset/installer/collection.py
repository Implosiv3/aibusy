from aibusy.utils.collection.keyed import KeyedCollection
from aibusy.engine.execution.asset.installer.abstract import AssetInstaller
from aibusy.engine.execution.asset.spec.abstract import AssetSpec


class AssetInstallerCollection(
    KeyedCollection[type[AssetSpec], AssetInstaller]
):

    def __init__(
        self
    ):
        self._items: dict[type[AssetSpec], AssetInstaller] = {}

    def register(
        self,
        installer: AssetInstaller
    ):
        self._installers[installer.spec_type] = installer

    def get(
        self,
        spec_type: type[AssetSpec]
    ) -> AssetInstaller:
        return self._installers[spec_type]