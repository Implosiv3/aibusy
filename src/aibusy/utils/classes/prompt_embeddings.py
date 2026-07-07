from dataclasses import dataclass


@dataclass(frozen = True)
class PromptEmbeddings:
    """
    *Dataclass*

    Class to include the embeddings of the
    prompt.
    """

    value: object