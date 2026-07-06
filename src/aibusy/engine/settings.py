from dataclasses import dataclass, field
from pathlib import Path

import tempfile
import os


@dataclass
class EngineSettings:
    """
    Global configuration shared by the engine and
    all plugins.
    """

    models_directory: Path = field(
        # default_factory = lambda: Path.home() / '.aibusy' / 'models'
        default_factory = lambda: os.getenv('MODELS_DIRECTORY', Path.home() / '.aibusy' / 'models')
    )

    cache_directory: Path = field(
        # default_factory = lambda: Path.home() / '.aibusy' / 'cache'
        default_factory = lambda: os.getenv('CACHE_DIRECTORY', Path.home() / '.aibusy' / 'cache')
    )

    temporary_directory: Path = field(
        # default_factory = lambda: Path(tempfile.gettempdir()) / 'aibusy'
        default_factory = lambda: os.getenv('TEMPORARY_DIRECTORY', Path(tempfile.gettempdir()) / 'aibusy')
    )