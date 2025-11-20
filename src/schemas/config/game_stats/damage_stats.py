"""Damage stats configuration schema.

This module provides a Pydantic schema for damage-related game stats.
"""

from pydantic import BaseModel, Field


class DamageStatsSchema(BaseModel):
    """
    Damage stats configuration schema.

    This schema represents all damage-related game stats.

    Parameters
    ----------
    player_shot_damage : int, optional
        Damage dealt by player shots (1-100). Defaults to 1.
    bomb_damage : int, optional
        Damage dealt by bombs (1-1000). Defaults to 30.

    Examples
    --------
    >>> damage = DamageStatsSchema()
    >>> combat.player_shot_damage
    1
    >>> combat.bomb_damage
    30
    >>> combat.model_dump()
    {'player_shot_damage': 1, 'bomb_damage': 30}
    """

    player_shot_damage: int = Field(
        default=1, ge=1, le=100, description="Damage dealt by player shots (1-100)"
    )
    bomb_damage: int = Field(
        default=30, ge=1, le=1000, description="Damage dealt by bombs (1-1000)"
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
