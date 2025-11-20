"""Game stats configuration schemas.

This module provides Pydantic schemas for game stats constants.
"""

from pydantic import BaseModel, Field

from .damage_stats import DamageStatsSchema
from .score_stats import ScoreStatsSchema

__all__ = [
    "ScoreStatsSchema",
    "DamageStatsSchema",
    "GameStatsSchema",
]


class GameStatsSchema(BaseModel):
    """
    Game stats configuration schema.

    This schema represents game stats constants including
    score values and damage values.

    Parameters
    ----------
    score : ScoreStatsSchema, optional
        Score-related game stats. Defaults to ScoreStatsSchema().
    damage : DamageStatsSchema, optional
        Damage-related game stats. Defaults to DamageStatsSchema().

    Examples
    --------
    >>> stats = GameStatsSchema()
    >>> stats.score.enemy_normal
    100
    >>> stats.damage.bomb_damage
    30
    >>> stats.model_dump()
    {'score': {'max_score': 999999, ...}, 'damage': {'player_shot_damage': 1, ...}}
    """

    score: ScoreStatsSchema = Field(
        default_factory=ScoreStatsSchema,
        description="Score-related game stats",
    )
    damage: DamageStatsSchema = Field(
        default_factory=DamageStatsSchema,
        description="Damage-related game stats",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
