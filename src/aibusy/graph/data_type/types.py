"""
All the `DataType` classes we have in
our system. We can have more classes in
the specific projects that implement a
new functionality and runtime.
"""
from aibusy.graph.data_type.abstract import DataType
from aibusy.graph.data_type.custom_classes.audio import Audio
from aibusy.graph.data_type.custom_classes.image import Image
from aibusy.graph.data_type.custom_classes.video import Video
from aibusy.engine.execution.asset.spec.abstract import AssetSpec
from aibusy.utils.classes.prompt_embeddings import PromptEmbeddings
from aibusy.utils.classes.noise import Noise
from aibusy.utils.classes.latents import Latents
from aibusy.engine.execution.asset.installed import InstalledAsset
from aibusy.runtime.resource.abstract import Resource
from aibusy.runtime.resource.spec.abstract import ResourceSpec
from aibusy.runtime.resource.reference import ResourceReference
from aibusy.runtime.device import Device
from pathlib import Path


# Basic pythonic types
STRING = DataType(
    name = 'String',
    runtime_type = str,
    parent = None
)
FLOAT = DataType(
    name = 'Float',
    runtime_type = float,
    parent = None
)
INT = DataType(
    name = 'Int',
    runtime_type = int,
    parent = None
)
BOOLEAN = DataType(
    name = 'Boolean',
    runtime_type = bool,
    parent = None
)
OBJECT = DataType(
    name = 'Object',
    runtime_type = object,
    parent = None
)
PATH = DataType(
    name = 'Path',
    runtime_type = Path,
    parent = None
)

# Specific internal
ASSET_SPEC = DataType(
    name = 'AssetSpec',
    runtime_type = AssetSpec,
    parent = None
)
INSTALLED_ASSET = DataType(
    name = 'InstalledAsset',
    runtime_type = InstalledAsset,
    parent = None
)
RESOURCE_SPEC = DataType(
    name = 'ResourceSpec',
    runtime_type = ResourceSpec,
    parent = None
)
RESOURCE_INSTANCE = DataType(
    name = 'ResourceInstance',
    runtime_type = Resource,
    parent = None
)


"""
AI related types below
"""
PROMPT = DataType(
    name = 'Prompt',
    runtime_type = str,
    parent = None
)
PROMPT_EMBEDDINGS = DataType(
    name = 'PromptEmbeddings',
    runtime_type = PromptEmbeddings,
    parent = None
)
NOISE = DataType(
    name = 'Noise',
    runtime_type = Noise,
    parent = None
)
LATENTS = DataType(
    name = 'Latents',
    runtime_type = Latents,
    parent = None
)
CLIP_PROMPT_ENCODER_RESOURCE_REFERENCE = DataType(
    name = 'CLIPPromptEncoderResourceReference',
    runtime_type = ResourceReference,
    parent = None
)
GAUSSIAN_NOISE_GENERATOR_RESOURCE_REFERENCE = DataType(
    name = 'GaussianNoiseGeneratorResourceReference',
    runtime_type = ResourceReference,
    parent = None
)

UNET_RESOURCE_REFERENCE = DataType(
    name = 'UNetResourceReference',
    runtime_type = ResourceReference,
    parent = None
)
VAE_RESOURCE_REFERENCE = DataType(
    name = 'VAEResourceReference',
    runtime_type = ResourceReference,
    parent = None
)
SCHEDULER_RESOURCE_REFERENCE = DataType(
    name = 'SchedulerResourceReference',
    runtime_type = ResourceReference,
    parent = None
)



"""
Specific wrapping types below
"""
AUDIO = DataType(
    name = 'Audio',
    runtime_type = Audio,
    parent = None
)
DEVICE = DataType(
    name = 'Device',
    runtime_type = Device,
    parent = None
)
IMAGE = DataType(
    name = 'Image',
    runtime_type = Image,
    parent = None
)
VIDEO = DataType(
    name = 'Video',
    runtime_type = Video,
    parent = None
)