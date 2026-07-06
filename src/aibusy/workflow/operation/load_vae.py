from aibusy.graph.operation.abstract.base import Operation
from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.runtime.device import Device
from aibusy.runtime.torch_dtype import TorchDType
from aibusy.runtime.interface.vae import VAE
from aibusy.engine.execution.context import ExecutionContext
from aibusy.graph.classes.input import Input
from aibusy.graph.classes.output import Output
from aibusy.runtime.resource.spec.vae_resource_spec import VAEResourceSpec


class LoadVAE(
    Operation
):

    asset = Input(InstalledAsset)
    device = Input(Device)
    dtype = Input(TorchDType)

    vae = Output(VAE)

    async def run(
        self,
        context: ExecutionContext,
    ):
        spec = VAEResourceSpec(
            asset = self.asset,
            device = self.device,
            dtype = self.dtype,
        )

        vae = await context.engine.resources.resolve(
            spec = spec,
            context = context
        )

        return {
            'vae': vae
        }