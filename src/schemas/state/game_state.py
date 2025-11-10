"""
Game state schema for serialization.

This module provides a Pydantic schema for game state serialization.
"""

from typing import List

from pydantic import BaseModel, Field, field_validator

from ..state.stage import StageSchema


class GameStateSchema(BaseModel):
    """
    Game state schema for serialization/deserialization.

    This schema allows game state to be serialized to JSON
    and deserialized back with validation. It includes all game variables
    that need to be persisted.

    Parameters
    ----------
    score : int, optional
        Current game score (0-999999). Defaults to 0.
    high_score : int, optional
        Highest score achieved (0-999999). Defaults to 0.
    selected_weapon : int, optional
        Index of currently selected weapon (0-2). Defaults to 0.
    lives : int, optional
        Current number of lives (0-9). Defaults to 3.
    weapon_levels : List[int], optional
        List of weapon levels for each weapon (length 3, each 0-5). Defaults to [0, 0, 0].
    current_stage : StageSchema, optional
        Current stage schema. Defaults to StageSchema(stage=1).

    Examples
    --------
    >>> schema = GameStateSchema(score=1000, lives=5)
    >>> schema.score
    1000
    >>> schema.lives
    5
    >>> schema.model_dump()
    {'score': 1000, 'high_score': 0, 'selected_weapon': 0, 'lives': 5, ...}
    """

    score: int = Field(
        default=0, ge=0, le=999999, description="Current game score (0-999999)"
    )
    high_score: int = Field(
        default=0, ge=0, le=999999, description="Highest score achieved (0-999999)"
    )
    selected_weapon: int = Field(
        default=0, ge=0, le=2, description="Index of currently selected weapon (0-2)"
    )
    lives: int = Field(
        default=3, ge=0, le=9, description="Current number of lives (0-9)"
    )
    weapon_levels: List[int] = Field(
        default_factory=lambda: [0, 0, 0],
        min_length=3,
        max_length=3,
        description="List of weapon levels for each weapon (length 3)",
    )
    current_stage: StageSchema = Field(
        default_factory=lambda: StageSchema(stage=1),
        description="Current stage schema",
    )

    @field_validator("weapon_levels")
    @classmethod
    def validate_weapon_levels(cls, v: List[int]) -> List[int]:
        """
        Validate weapon levels are within valid range (0-5).

        Parameters
        ----------
        v : List[int]
            List of weapon levels to validate.

        Returns
        -------
        List[int]
            Validated weapon levels.

        Raises
        ------
        ValueError
            If any weapon level is outside the valid range (0-5).
        """
        if len(v) != 3:
            raise ValueError("weapon_levels must have exactly 3 elements")
        for level in v:
            if not (0 <= level <= 5):
                raise ValueError(f"weapon_level must be between 0 and 5, got {level}")
        return v

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
