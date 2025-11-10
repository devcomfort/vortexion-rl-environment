"""
Game mechanics configuration schema.

This module provides a Pydantic schema for game mechanics constants.
"""

from pydantic import BaseModel, Field


class GameMechanicsSchema(BaseModel):
    """
    Game mechanics configuration schema.

    This schema represents game mechanics constants including
    score values and damage values.

    Parameters
    ----------
    enemy_score_normal : int, optional
        Score awarded for defeating a normal enemy (1-10000). Defaults to 100.
    enemy_score_boss : int, optional
        Score awarded for defeating a boss enemy (1-100000). Defaults to 5000.
    player_shot_damage : int, optional
        Damage dealt by player shots (1-100). Defaults to 1.
    bomb_damage : int, optional
        Damage dealt by bombs (1-1000). Defaults to 30.

    Examples
    --------
    >>> mechanics = GameMechanicsSchema()
    >>> mechanics.enemy_score_normal
    100
    >>> mechanics.bomb_damage
    30
    >>> mechanics.model_dump()
    {'enemy_score_normal': 100, 'enemy_score_boss': 5000, ...}
    """

    enemy_score_normal: int = Field(
        default=100,
        ge=1,
        le=10000,
        description="Score awarded for defeating a normal enemy (1-10000)",
    )
    enemy_score_boss: int = Field(
        default=5000,
        ge=1,
        le=100000,
        description="Score awarded for defeating a boss enemy (1-100000)",
    )
    player_shot_damage: int = Field(
        default=1, ge=1, le=100, description="Damage dealt by player shots (1-100)"
    )
    bomb_damage: int = Field(
        default=30, ge=1, le=1000, description="Damage dealt by bombs (1-1000)"
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
