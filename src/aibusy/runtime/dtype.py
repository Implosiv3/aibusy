from dataclasses import dataclass


@dataclass(frozen = True)
class DType:
    """
    The type of the data, identified by a str.
    """

    identifier: str

    def __str__(
        self
    ):
        return self.identifier
    

FLOAT16 = DType('float16')
BFLOAT16 = DType('bfloat16')
FLOAT32 = DType('float32')