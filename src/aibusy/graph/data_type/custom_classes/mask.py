from dataclasses import dataclass


@dataclass(frozen = True)
class Mask:
    """
    Includes:
    - `pixels` (`np.ndarray`)
    """

    # TODO: Don't want the import by now
    pixels: 'np.ndarray'