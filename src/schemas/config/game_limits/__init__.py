"""Game limits configuration schemas.

This module provides Pydantic schemas for all maximum limits and caps in the game.
"""

from pydantic import BaseModel, Field

from .player_limits import PlayerLimitsSchema
from .progression_limits import ProgressionLimitsSchema

__all__ = [
    "PlayerLimitsSchema",
    "ProgressionLimitsSchema",
    "GameLimitsSchema",
]


class GameLimitsSchema(BaseModel):
    """
    Game limits configuration schema.

    This schema represents all maximum limits and caps in the game,
    including player stats, progression, and system constraints.

    Parameters
    ----------
    player : PlayerLimitsSchema, optional
        Player-related limits. Defaults to PlayerLimitsSchema().
    progression : ProgressionLimitsSchema, optional
        Game progression limits. Defaults to ProgressionLimitsSchema().

    Examples
    --------
    >>> limits = GameLimitsSchema()
    >>> limits.player.max_lives
    9
    >>> limits.progression.final_stage.stage
    5
    >>> limits.model_dump()
    {'player': {'max_lives': 9, ...}, 'progression': {'final_stage': {...}}}
    """

    player: PlayerLimitsSchema = Field(
        default_factory=PlayerLimitsSchema,
        description="Player-related limits",
    )
    progression: ProgressionLimitsSchema = Field(
        default_factory=ProgressionLimitsSchema,
        description="Game progression limits",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
