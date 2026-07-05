"""
A simple test to verify that pytes is working and
the tests are being detected.
"""
import pytest


@pytest.mark.mandatory
@pytest.mark.asyncio
async def test_workflow():
    # from aibusy.engine.builder import EngineBuilder

    # builder = EngineBuilder()
    # engine = builder.build()

    # checkpoint = InstallAsset(
    #     asset = CheckpointAsset(
    #         ...
    #     )
    # )

    # unet = LoadUNet(
    #     asset = checkpoint.asset,
    #     device = 'cuda',
    #     dtype = torch.float16,
    # )

    # vae = LoadVAE(
    #     asset = checkpoint.asset,
    #     device = 'cuda',
    #     dtype = torch.float16,
    # )

    # await engine.run(
    #     unet.unet,
    #     vae.vae,
    # )

    assert True