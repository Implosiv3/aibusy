from abc import ABC, abstractmethod


class UNet(
    ABC
):

    @abstractmethod
    async def infer(
        self,
        *,
        latents,
        timestep,
        encoder_hidden_states,
    ):
        """
        Infer...

        TODO: Explain better
        """
        ...

# This will be implemented in 'aibusy-runtime-diffusers'
"""
class DiffusersUNet(
    UNet
):
    def __init__(
        self,
        module
    ):
        self._module = module

    async def predict_noise(
        ...
    ):
        return self._module(
            ...
        ).sample
"""