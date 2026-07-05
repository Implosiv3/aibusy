from aibusy.graph.operation.abstract.base import Operation
from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.runtime.device import Device
from aibusy.runtime.torch_dtype import TorchDType
from aibusy.runtime.interface.unet import UNet
from aibusy.graph.classes.input import Input
from aibusy.graph.classes.output import Output
from aibusy.runtime.resource.spec.unet_resource_spec import UNetResourceSpec


class LoadUNet(
    Operation
):

    checkpoint: Input[InstalledAsset]
    device: Input[Device]
    # TODO: What about this type (?)
    dtype: Input[TorchDType]
    unet: Output[UNet]

    async def run(
        self,
        context: ExecutionContext,
    ):
        spec = UNetResourceSpec(
            asset = self.checkpoint,
            device = self.device,
            dtype = self.dtype,
        )

        unet = await context.engine.resources.resolve(spec)

        return {
            'unet': unet
        }