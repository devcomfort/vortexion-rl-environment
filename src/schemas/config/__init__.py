"""Configuration schemas for game constants."""

from .app_config import AppConfigSchema
from .player_config import PlayerConfigSchema
from .score_config import ScoreConfigSchema
from .graphics_config import GraphicsConfigSchema
from .resources import (
    AudioResourcesSchema,
    GraphicsResourcesSchema,
    MapResourcesSchema,
)
from .resources_config import ResourcesConfigSchema

__all__ = [
    "AppConfigSchema",
    "PlayerConfigSchema",
    "ScoreConfigSchema",
    "GraphicsConfigSchema",
    "GraphicsResourcesSchema",
    "AudioResourcesSchema",
    "MapResourcesSchema",
    "ResourcesConfigSchema",
]
