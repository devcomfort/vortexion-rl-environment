"""Player limits configuration schema.

This module provides a Pydantic schema for player-related limits.
"""

from pydantic import BaseModel, Field


class PlayerLimitsSchema(BaseModel):
    """
    Player-related limits schema.

    This schema represents all maximum limits related to player stats.

    Parameters
    ----------
    max_lives : int, optional
        Maximum number of lives allowed (1-9). Player cannot exceed this limit
        even with power-ups. Defaults to 9.
    max_weapons : int, optional
        Maximum number of weapon types (1-10). Determines the size of weapon
        arrays and UI display. Defaults to 3.
    max_weapon_level : int, optional
        Maximum level for any weapon (1-10). Weapon level cannot exceed this
        value even with power-ups. Defaults to 5.

    Examples
    --------
    >>> limits = PlayerLimitsSchema()
    >>> limits.max_lives
    9
    >>> limits.max_weapons
    3
    >>> limits.model_dump()
    {'max_lives': 9, 'max_weapons': 3, 'max_weapon_level': 5}
    """

    max_lives: int = Field(
        default=9,
        ge=1,
        le=9,
        description=(
            "Maximum number of lives allowed (1-9). "
            "Player cannot exceed this limit even with power-ups."
        ),
    )
    max_weapons: int = Field(
        default=3,
        ge=1,
        le=10,
        description=(
            "Maximum number of weapon types (1-10). "
            "Determines the size of weapon arrays and UI display."
        ),
    )
    max_weapon_level: int = Field(
        default=5,
        ge=1,
        le=10,
        description=(
            "Maximum level for any weapon (1-10). "
            "Weapon level cannot exceed this value even with power-ups."
        ),
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
