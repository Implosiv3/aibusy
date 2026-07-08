from dataclasses import dataclass


@dataclass(frozen = True)
class PredictedNoise:
    """
    The estimation of data distortion that will
    be used in machine learning to provide a
    different result.
    """

    value: object