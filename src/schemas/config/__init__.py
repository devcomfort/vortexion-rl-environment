"""Configuration schemas for game constants."""

from .app_config import AppConfigSchema
from .entity_type import EntityTypeSchema
from .player_config import PlayerConfigSchema
from .game_stats import (
    DamageStatsSchema,
    GameStatsSchema,
    ScoreStatsSchema,
)
from .graphics_config import GraphicsConfigSchema
from .resources import (
    AudioResourcesSchema,
    GraphicsResourcesSchema,
    TilemapResourcesSchema,
)
from .resources_config import ResourcesConfigSchema
from .stage_config import StageConfigSchema

__all__ = [
    "AppConfigSchema",
    "EntityTypeSchema",
    "PlayerConfigSchema",
    "GameStatsSchema",
    "ScoreStatsSchema",
    "DamageStatsSchema",
    "GraphicsConfigSchema",
    "GraphicsResourcesSchema",
    "AudioResourcesSchema",
    "TilemapResourcesSchema",
    "ResourcesConfigSchema",
    "StageConfigSchema",
]
