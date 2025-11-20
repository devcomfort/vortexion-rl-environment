"""Configuration schemas for game constants."""

from .app_config import AppConfigSchema
from .config import GameConfigSchema
from .entity_type import EntityTypeSchema
from .game_limits import (
    GameLimitsSchema,
    PlayerLimitsSchema,
    ProgressionLimitsSchema,
)
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
    "GameConfigSchema",
    "EntityTypeSchema",
    "GameLimitsSchema",
    "PlayerLimitsSchema",
    "ProgressionLimitsSchema",
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
