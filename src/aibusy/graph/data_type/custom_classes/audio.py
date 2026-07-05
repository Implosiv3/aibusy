from dataclasses import dataclass


@dataclass(frozen = True)
class Audio:
    """
    Includes:
    - `samples` (`np.ndarray`)
    - `sample_rate` (`int`)
    """

    # TODO: Don't want the import by now
    samples: 'np.ndarray'
    sample_rate: int