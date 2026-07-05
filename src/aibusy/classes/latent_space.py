from dataclasses import dataclass


@dataclass(frozen = True)
class LatentSpace:
    """
    The space in which all the internal vectors
    (embeddings) live, where they are plotted and
    compared. The internal geometry created by the
    model's parameters.

    This is the CANVAS (space) in which we plot the
    embeddings, and is only affected when tunning
    parameters or training the model.
    """

    channels: int
    width: int
    height: int
    batch_size: int = 1

    def to_shape(
        self
    ) -> tuple[int, int, int, int]:
        """
        Transform the `LatentSpace` instance into a
        shape, useful to be sent to the noise
        generator. The shape is a tuple like this:
        ```
        (
            self.batch_size,
            self.channels,
            self.height,
            self.width
        )
        ```
        """
        return (
            self.batch_size,
            self.channels,
            self.height,
            self.width
        )