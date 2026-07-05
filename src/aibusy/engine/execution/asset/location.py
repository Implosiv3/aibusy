"""
TODO: This class will be replaced by a resolver
in the future, but now, as we only have paths,
is simple.
"""
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass(frozen = True)
class AssetLocation:

    uri: str

    @property
    def scheme(
        self
    ) -> str:
        """
        URI scheme.

        Examples:
            file:///models/sd15  -> 'file'
            hf://runwayml/sd15   -> 'hf'
            s3://bucket/model    -> 's3'
        """
        return urlparse(self.uri).scheme

    @property
    def is_local(
        self
    ) -> bool:
        """
        Whether this asset points to a local filesystem location.
        """
        return self.scheme == 'file'

    @property
    def path(
        self
    ) -> str:
        """
        Return the filesystem path.

        Raises:
            RuntimeError:
                If the asset is not stored locally.
        """
        parsed = urlparse(self.uri)

        if parsed.scheme != 'file':
            raise RuntimeError(
                f'The asset "{self.uri}" is not stored locally.'
            )

        return parsed.path
    
    @property
    def name(
        self
    ) -> str:
        """
        Last path component.
        """
        from pathlib import Path

        return Path(self.path).name
    
    @property
    def parent(
        self
    ) -> str:
        from pathlib import Path

        return str(
            Path(self.path).parent
        )