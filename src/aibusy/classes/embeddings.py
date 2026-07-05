from dataclasses import dataclass


@dataclass(frozen = True)
class Embeddings:
    """
    Vectors of numbers that represent text in a
    high-dimensional space. Usually used outside the
    model for search, clustering, retrieval, etc.

    When an AI converts the word 'King' into a list
    of 1,536 numbers, or a photo into a numerical
    array, those vectors are embeddings. They are
    the data points used for semantic search,
    retrieval, and classification.

    These are the POINTS we plot in our latent
    space.
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