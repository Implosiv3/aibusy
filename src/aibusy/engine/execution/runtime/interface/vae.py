from abc import ABC, abstractmethod


class VAE(
    ABC
):

    @abstractmethod
    async def encode(
        self,
        image,
    ):
        """
        Encode an image into latent space.
        """
        ...

    @abstractmethod
    async def decode(
        self,
        latents,
    ):
        """
        Decode latents into an image tensor.
        """
        ...