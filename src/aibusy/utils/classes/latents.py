from dataclasses import dataclass


@dataclass(frozen = True)
class Latents:
    """
    Latents are the raw, often compressed
    representations of data actively flowing
    through the neural network during encoding
    and decoding. They represent a more general,
    transient, and hidden layer of thought the
    model uses to generate outputs.
    """
    
    instance: object


"""
I don't use 'torch.Tensor' here because this
one is general and the implementation could
be 'torch.Tensor' or could be not.

Having a specific 'Latents' class allows us
to avoid receiving 'Embeddings' in a method
that is not expected, even if the 'Latents'
and the 'Embeddings' have a 'torch' value
inside. They are distinct concepts. same with
'NoisePrediction'.
"""