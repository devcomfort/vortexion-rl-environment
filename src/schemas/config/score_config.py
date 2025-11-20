"""Score configuration schema.

This module provides a Pydantic schema for score-related configuration.
"""

from pydantic import BaseModel, Field


class ScoreConfigSchema(BaseModel):
    """
    Score configuration schema.

    This schema represents all score-related configuration constants.

    Parameters
    ----------
    max_score : int, optional
        Maximum score cap (1-9999999). Score cannot exceed this value.
        Used for both gameplay balance and UI display limits. Defaults to 999999.
    enemy_normal : int, optional
        Score awarded for defeating a normal enemy (1-10000). Defaults to 100.
    enemy_boss : int, optional
        Score awarded for defeating a boss enemy (1-100000). Defaults to 5000.

    Examples
    --------
    >>> score = ScoreConfigSchema()
    >>> score.max_score
    999999
    >>> score.enemy_normal
    100
    >>> score.model_dump()
    {'max_score': 999999, 'enemy_normal': 100, 'enemy_boss': 5000}
    """

    max_score: int = Field(
        default=999999,
        ge=1,
        le=9999999,
        description=(
            "Maximum score cap (1-9999999). "
            "Score cannot exceed this value. "
            "Used for both gameplay balance and UI display limits."
        ),
    )
    enemy_normal: int = Field(
        default=100,
        ge=1,
        le=10000,
        description="Score awarded for defeating a normal enemy (1-10000)",
    )
    enemy_boss: int = Field(
        default=5000,
        ge=1,
        le=100000,
        description="Score awarded for defeating a boss enemy (1-100000)",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
