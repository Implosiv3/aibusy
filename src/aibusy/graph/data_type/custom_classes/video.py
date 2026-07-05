"""
TODO: Maybe this will be transformed in the future
to be able to handle something stored in the disk.
"""
from aibusy.graph.data_type.custom_classes.image import Image
from dataclasses import dataclass


@dataclass(frozen = True)
class Video:
    """
    Includes:
    - `frames` (`list[np.ndarray]`)
    - `fps` (`float`)
    """

    frames: list[Image]
    fps: float