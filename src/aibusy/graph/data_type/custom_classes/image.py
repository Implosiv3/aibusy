from dataclasses import dataclass


@dataclass(frozen = True)
class Image:
    """
    Includes:
    - `pixels` (`np.ndarray`)
    """

    # TODO: Don't want the import by now
    pixels: 'np.ndarray'