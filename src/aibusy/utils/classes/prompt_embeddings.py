from dataclasses import dataclass


@dataclass(frozen = True)
class PromptEmbeddings:
    """
    *Dataclass*

    Class to include the `positive` and the
    `negative` prompt embeddings at the same
    time.
    """

    positive: object
    negative: object