from aibusy.engine.execution.resource.spec.abstract import ResourceSpec
from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.classes.device import Device
from aibusy.classes.torch_dtype import TorchDType
from dataclasses import dataclass


@dataclass(frozen = True)
class VAEResourceSpec(
    ResourceSpec
):

    asset: InstalledAsset
    device: Device
    dtype: TorchDType