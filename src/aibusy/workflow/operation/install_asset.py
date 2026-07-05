from aibusy.graph.operation.abstract.atomic_operation import AtomicOperation
from graph.data_type.types import ASSET_SPEC, INSTALLED_ASSET
from aibusy.graph.classes.input import Input
from aibusy.graph.classes.output import Output


class InstallAsset(
    AtomicOperation
):
    
    asset: Input[ASSET_SPEC]

    installed_asset: Output[INSTALLED_ASSET]

    async def execute(
        self,
        context: 'ExecutionContext'
    ) -> dict[str, object]:
        installed_asset = await context.assets.install(
            self.asset
        )

        return {
            'installed_asset': installed_asset
        }