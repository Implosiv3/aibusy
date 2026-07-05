from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from aibusy.engine.execution.asset.location import AssetLocation
from dataclasses import dataclass


@dataclass(frozen = True)
class InstalledAsset:

    spec: AssetSpec
    location: AssetLocation